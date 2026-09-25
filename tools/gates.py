#!/usr/bin/env python3
"""
gates.py -- mechanical audit gates for the Founder's Playbook.

Why this exists: five of the audit classes this run has been paying subagents for are
mechanical (column drift, dangling register keys, anchor parity, non-verbatim quotes,
stage vocabulary). Agents did them slowly, expensively, and sometimes wrongly. Scripts
do them completely, in seconds, and repeatably after every repair.

Every gate here is validated against the exact defect it is supposed to catch -- see
`--self-test`, which plants each previously-missed defect into a copy and asserts the
detector fires. A gate that cannot catch its own historical defect is a broken gate.

  python tools/gates.py --company-dir founders_playbook/01_companies/company_001_amazon
  python tools/gates.py --company-dir <dir> --checks csv,quotes,anchors,keys
  python tools/gates.py --self-test

Exit: 0 all pass, 1 findings present (report is authoritative), 2 harness error.
"""

import argparse
import csv
import glob
import hashlib
import io
import json
import os
import re
import shutil
import sys
import tempfile
import unicodedata

REGISTERS = ["timeline.csv", "quantitative.csv", "conflicts.csv", "sources.csv",
             "data_gaps.csv", "validation.csv", "failures.csv", "decisions.csv",
             "channels.csv"]
STAGE_VOCAB = {"stage1", "stage2", "stage2-consequence", "stage3", ""}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
MIN_QUOTE_WORDS = 8
TAG_RE = re.compile(r"<[^>]+>")
WS_RE = re.compile(r"\s+")

NARR_GLOBS = {
    "stage1": ["stage_1.md"],
    "stage2": ["stage_2_part_*.md", "stage_2.md"],
    "stage3": ["stage_3_part_*.md", "stage_3.md"],
}


def _norm_text(s):
    s = unicodedata.normalize("NFKD", s)
    s = s.replace("‘", "'").replace("’", "'").replace("“", '"').replace("”", '"')
    s = s.replace("–", "-").replace("—", "-").replace("\u00a0", " ")
    return WS_RE.sub(" ", s).strip().lower()


def strip_html(s):
    s = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", s)
    s = TAG_RE.sub(" ", s)
    s = (s.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
          .replace("&quot;", '"').replace("&#39;", "'").replace("&nbsp;", " ")
          .replace("&#160;", " "))
    return _norm_text(s)


def read_rows(path):
    with open(path, "r", encoding="utf-8", errors="replace", newline="") as f:
        sample = f.read(4000)
        f.seek(0)
        try:
            dialect = csv.Sniffer().sniff(sample, delimiters=",;")
        except csv.Error:
            dialect = csv.excel
        rdr = csv.reader(f, dialect)
        rows = list(rdr)
    if not rows:
        return [], [], 0
    return rows[0], rows[1:], len(sample)


def plant(path, fn):
    """Rewrite a fixture file. Reads fully before opening for write -- the reverse order
    truncates the file before the read happens and silently destroys the case."""
    text = open(path, encoding="utf-8").read()
    with open(path, "w", encoding="utf-8") as f:
        f.write(fn(text))


def col_counts(rows):
    """Field counts per row. An unquoted comma shifts fields while sometimes PRESERVING
    the count, so this alone is necessary and not sufficient -- see check_quotes."""
    return sorted({len(r) for r in rows})


# ---------------------------------------------------------------- gates

def locate(company, name):
    """Company root, then research/. Walmart/Apple/UnitedHealth keep their registers under
    research/ until assembly, and a gate that silently read nothing reported a false clean."""
    for d in ("", "research"):
        p = os.path.join(company, d, name) if d else os.path.join(company, name)
        if os.path.exists(p):
            return p
    return None


def narr_files(company):
    out = []
    for globs in NARR_GLOBS.values():
        for g in globs:
            out += glob.glob(os.path.join(company, g))
            out += glob.glob(os.path.join(company, "research", g))
            out += glob.glob(os.path.join(company, "_parts", g))
    if not out:
        out += glob.glob(os.path.join(company, "_parts", "s[0-9]_p[0-9]*.md"))
    return sorted(set(out))


def gate_csv(company, report):
    for name in REGISTERS:
        p = locate(company, name)
        if not p:
            continue
        hdr, rows, _ = read_rows(p)
        idx = {h.strip().lower(): i for i, h in enumerate(hdr)}
        bad = [(i + 2, len(r)) for i, r in enumerate(rows) if len(r) != len(hdr)]
        if bad:
            report.fail("csv", name, "width drift: %d rows off (%s...)" % (len(bad), bad[:3]))
        else:
            report.ok("csv", name, "%d rows x %d cols" % (len(rows), len(hdr)))
        # duplicate PRIMARY keys only. source_id repeats legitimately: many records cite
        # the same filing, and an earlier version of this gate called that a defect.
        key_cols = [c for c in idx if c.endswith("_id") and c not in ("source_id",)]
        if name == "sources.csv":
            key_cols = ["source_id"]
        for idcol in key_cols:
            seen, dups = {}, []
            for i, r in enumerate(rows):
                if len(r) > idx[idcol]:
                    v = r[idx[idcol]].strip()
                    if v and v in seen:
                        dups.append("%s (l%d,l%d)" % (v, seen[v], i + 2))
                    elif v:
                        seen[v] = i + 2
            if dups:
                report.fail("csv", name, "duplicate %s: %s" % (idcol, ", ".join(dups[:8])))
        # stage vocabulary (numbers in a stage column are the defect seen on 2026-09-25)
        if "stage" in idx:
            vals = {r[idx["stage"]].strip() for r in rows if len(r) > idx["stage"]}
            badv = sorted(v for v in vals if v not in STAGE_VOCAB)
            if badv:
                report.fail("csv", name, "stage vocabulary illegal: %s" % ", ".join(badv[:6]))
        # A date column must contain a four-digit year. Fiscal-year labels, month
        # precision and ranges are all legal; a value with no year at all is either a
        # shifted field or prose that has wandered into a date column.
        SENTINELS = ("unknown", "n/a", "none", "not dated", "see notes", "untried",
                     "not retrieved", "in-window", "continuous", "undated", "no dated")
        for cand in ("date", "date_or_range", "event_date", "publication_date",
                     "source_date", "access_date", "date_tested"):
            if cand in idx:
                bad2 = [r[idx[cand]] for r in rows
                        if len(r) > idx[cand] and r[idx[cand]].strip()
                        and not re.search(r"\d{4}", r[idx[cand]])
                        and not any(s in r[idx[cand]].lower() for s in SENTINELS)]
                if bad2:
                    report.fail("csv", name, "%s carries no four-digit year: %s"
                                % (cand, bad2[:4]))
        # source_id resolution: only S#### tokens are checked; prose is not a key
        if "source_id" in idx:
            sp = locate(company, "sources.csv")
            if sp and os.path.basename(p) != "sources.csv":
                sh, srows, _ = read_rows(sp)
                sidx = {h.strip().lower(): i for i, h in enumerate(sh)}
                key = "source_id" if "source_id" in sidx else None
                if key is not None:
                    have = {r[sidx[key]].strip() for r in srows if len(r) > sidx[key]}
                    tok = re.compile(r"\bS\d{3,6}[a-z]?\b")
                    miss = set()
                    for r in rows:
                        if len(r) <= idx["source_id"]:
                            continue
                        cell = r[idx["source_id"]]
                        for t in tok.findall(cell):
                            if t not in have:
                                miss.add(t)
                    if miss:
                        report.fail("csv", name, "source_id token not a key in sources.csv: %s"
                                    % ", ".join(sorted(miss)[:10]))
                    else:
                        report.ok("csv", name + ".source_id", "all S#### tokens resolve")


def stage_docs(company):
    """Final volumes, plus the in-flight `_parts/` intermediates (named s1_p1.md, not
    stage_*.md) ONLY while no merged volume exists. An assembled company's `_parts/` are a
    superseded audit trail, and gating them would resurface retired keys as fresh defects."""
    out = []
    for d in ("", "research"):
        out += glob.glob(os.path.join(company, d, "stage_*.md"))
    if not out:
        out += glob.glob(os.path.join(company, "_parts", "s[0-9]_p[0-9]*.md"))
    return sorted(set(out))


def gate_keys(company, report):
    """Narrative must not cite retired/temporary register keys."""
    sp = locate(company, "sources.csv")
    have = set()
    if sp:
        h, rows, _ = read_rows(sp)
        idx = {x.strip().lower(): i for i, x in enumerate(h)}
        key = next((c for c in ("source_id", "id") if c in idx), None)
        if key is not None:
            have = {r[idx[key]].strip() for r in rows if len(r) > idx[key]}
    token = re.compile(r"\bS\d{3,6}[a-z]?\b")
    legacy = re.compile(r"\bS\d{1,2}[A-Z]?-\d{2,5}\b")
    for md in stage_docs(company):
        txt = open(md, encoding="utf-8", errors="replace").read()
        body = re.sub(r"(?s)```.*?```", " ", txt)
        label = os.path.relpath(md, company).replace("\\", "/")
        hits_legacy = sorted(set(legacy.findall(body)))
        if hits_legacy:
            # Dossier record ids (S2A-04) are legitimate stable labels in this corpus, so
            # this is a review list, not a defect. Superseded prefixes show up here too and
            # must be adjudicated by a human or an agent that can read the re-key map.
            report.note("keys", "%s cites %d hyphenated record keys: %s%s"
                        % (label, len(hits_legacy),
                           ", ".join(hits_legacy[:8]), " ..." if len(hits_legacy) > 8 else ""))
        cited = set(token.findall(body))
        dangling = sorted(c for c in cited if c not in have)
        if dangling:
            report.fail("keys", label,
                        "unresolvable source tokens: %s" % ", ".join(dangling[:15]))
        elif cited:
            report.ok("keys", label, "%d source tokens all resolve" % len(cited))


def _anchors(text):
    return {m.group(0) for m in re.finditer(r"\bU\.(\d+[a-z]?)\b", text)}


DECL_ANCHOR_RE = re.compile(r"(?m)^\s{0,3}(?:#{1,6}\s*|\*\*)?(U\.\d+[a-z]?)(?=\s|\*|\)|:|$)")


def _anchors_declared(text):
    """Anchors the narrative actually STATES as a section label, at line start. Prose that
    merely points at another section ('see U.49') is a forward reference, not an anchor,
    and counting it produced false parity breaks on the first real run."""
    out = set()
    for line in text.splitlines():
        s = line.strip()
        if not s:
            continue
        m = re.match(r"^(?:#{1,6}\s*|\*\s*|\-\s*)?\**\s*(U\.\d+[a-z]?)\b", s)
        if m:
            out.add(m.group(1))
        elif s.startswith("|"):
            for cell in s.split("|"):
                c = cell.strip().strip("*").strip()
                if re.fullmatch(r"U\.\d+[a-z]?", c):
                    out.add(c)
    return out


def _reg_anchor_tokens(company):
    out = set()
    for name in REGISTERS:
        p = locate(company, name)
        if p:
            out |= _anchors(open(p, encoding="utf-8", errors="replace").read())
    return out


def gate_anchors(company, report):
    """Global parity: every declared U.nnn anchor in the narrative has at least one
    register row citing it, and every register anchor is declared somewhere."""
    reg = _reg_anchor_tokens(company)
    files = narr_files(company)
    all_nar = set()
    for p in files:
        nar = _anchors_declared(open(p, encoding="utf-8", errors="replace").read())
        all_nar |= nar
        if nar:
            report.note("anchors", "%s declares %d anchors"
                        % (os.path.relpath(p, company).replace("\\", "/"), len(nar)))
    if not reg:
        report.note("anchors", "no register anchors found -- UNANSWERED, not passed")
    if not all_nar:
        report.note("anchors", "no narrative anchors found -- UNANSWERED, not passed")
    if not reg or not all_nar:
        return
    orphan_nar = sorted(all_nar - reg, key=_anchor_sort)
    orphan_reg = sorted(reg - all_nar, key=_anchor_sort)
    if orphan_nar:
        report.fail("anchors", "narrative", "anchor with no register row: %s"
                    % ", ".join(orphan_nar[:12]))
    if orphan_reg:
        report.fail("anchors", "registers", "register row citing an anchor absent from the "
                    "narrative: %s" % ", ".join(orphan_reg[:12]))
    if not orphan_nar and not orphan_reg:
        report.ok("anchors", "parity", "%d narrative anchors <-> %d register anchors"
                  % (len(all_nar), len(reg)))


def _anchor_sort(a):
    m = re.match(r"U\.(\d+)([a-z]?)", a)
    return (int(m.group(1)), m.group(2)) if m else (10 ** 9, a)


def _squash(s):
    """Alphanumerics and single spaces only. Punctuation differs between a filing's HTML
    table cell and a narrative transcription far more often than wording does, so matching
    on bare tokens is what makes this gate measure citation fidelity rather than typography."""
    s = re.sub(r"[^a-z0-9 ]+", " ", _norm_text(s))
    return WS_RE.sub(" ", s).strip()


QUOTE_INTRO = re.compile(
    r"(?:said|says|stated|states|wrote|writes|read[s]?s|notes?|quoted|quotes|titled|named"
    r"|verbatim|exact(?:ly)?|as filed|headline|title|according to|per)\b[^\"”]{0,40}$")
# A span containing these is commentary ABOUT a source, not a quotation FROM one.
REJECT_IN_QUOTE = re.compile(r"(l\.\s*\d|§|cor-\d|`|\||https?://|\[\d|\bnosuchkey\b|"
                             r"\bfilingline\b|\bverbatim marker\b|<[^>]+>)", re.I)


def gate_quotes(company, report, min_words=MIN_QUOTE_WORDS):
    corpus = []
    for pat in ("*.txt", "*.htm", "*.html", "*.sgml", "*.sgm"):
        for p in glob.glob(os.path.join(company, "sources", "**", pat), recursive=True):
            corpus.append(_squash(strip_html(open(p, encoding="utf-8", errors="replace").read())))
    blob = " ".join(corpus)
    report.note("quotes", "corpus: %d chars of squashed local source text indexed" % len(blob))
    if not corpus:
        report.note("quotes", "no local sources -> quote gate UNANSWERED, not passed")
        return
    qre = re.compile(r"\"([^\"]{%d,900})\"" % (min_words * 4))
    checked = unmatched = skipped = 0
    unattr = []
    misses = []
    for md in stage_docs(company):
        txt = open(md, encoding="utf-8", errors="replace").read()
        txt = re.sub(r"(?s)```.*?```", " ", txt)
        label = os.path.relpath(md, company).replace("\\", "/")
        for m in qre.finditer(txt):
            q = m.group(1)
            if q.count(" ") + 1 < min_words or REJECT_IN_QUOTE.search(q):
                skipped += 1
                continue
            pre = txt[max(0, m.start() - 60):m.start()]
            attributed = bool(QUOTE_INTRO.search(pre) or re.search(r"[:—-]\s*$", pre))
            norm = _squash(q)
            frags = [f for f in re.split(r"\s*\[[^\]]*\]\s*", norm) if f.count(" ") + 1 >= 4]
            if not frags:
                skipped += 1
                continue
            bad = [f for f in frags if f not in blob]
            if not attributed:
                # A quotation with no attribution verb is its own defect class: nothing in
                # the sentence says who said it, which is where paraphrases enter as quotes.
                if bad:
                    unattr.append((label, bad[0][:110]))
                continue
            checked += 1
            if bad:
                unmatched += 1
                if len(misses) < 40:
                    misses.append((label, bad[0][:110]))
    rate = (unmatched / checked) if checked else 1.0
    report.note("quotes", "candidates %d, attributed+checked %d, skipped %d, unmatched %d (%.0f%%)"
                % (checked + skipped + len(unattr), checked, skipped, unmatched, 100 * rate))
    if unattr:
        # Advisory only: most of these are scare-quotes and labelled phrases, not
        # citations, so a count is honest signal and a defect list would not be.
        report.note("quotes", "unattributed spans unmatched: %d (advisory, e.g. %s)"
                    % (len(unattr), "; ".join("%s::%s" % u for u in unattr[:2])))
    if not checked:
        report.note("quotes", "no attributed quotable spans identified -- UNANSWERED")
        return
    if rate > 0.25:
        # A high miss rate means the detector or the local corpus is wrong, not that 179
        # citations are fabricated: quotes from secondary print that was never saved under
        # sources/ can never match locally. Say so rather than emitting a list an agent
        # would "repair" by mangling real quotes.
        report.fail("quotes", "ADVISORY", "%d of %d checked spans unmatched (%.0f%%) -- gate "
                    "precision is not established, treat as a triage list, NOT as defects"
                    % (unmatched, checked, 100 * rate))
    elif unmatched:
        report.fail("quotes", "verbatim", "%d of %d quoted spans not found in local sources"
                    % (unmatched, checked))
    else:
        report.ok("quotes", "verbatim", "%d quoted spans all present in local sources" % checked)
    for f, s in misses:
        report.detail("quotes", "%s :: %s" % (f, s))


def gate_budgets(company, report, tier):
    caps = {"exemplar": 60000, "core": 22000, "register": 8000}
    cap = caps.get(tier, 60000)
    for md in stage_docs(company):
        w = len(re.findall(r"\S+", open(md, encoding="utf-8", errors="replace").read()))
        if w > cap:
            report.fail("budget", os.path.basename(md), "%d words > %s cap %d (split required)"
                        % (w, tier, cap))
        else:
            report.ok("budget", os.path.basename(md), "%d words (cap %d)" % (w, cap))


# ---------------------------------------------------------------- harness

class Report:
    def __init__(self):
        self.findings, self.passes, self.notes, self.details = [], [], [], []

    def fail(self, gate, subject, msg):
        self.findings.append({"gate": gate, "subject": subject, "msg": msg})

    def ok(self, gate, subject, msg):
        self.passes.append("%-8s %-34s %s" % (gate, subject, msg))

    def note(self, gate, msg):
        self.notes.append("%-8s %s" % (gate, msg))

    def detail(self, gate, msg):
        self.details.append(msg)

    def render(self, company):
        out = io.StringIO()
        out.write("# Mechanical gate report -- %s\n\n" % os.path.basename(company.rstrip("/\\")))
        out.write("Findings: **%d** | Passes: %d\n\n" % (len(self.findings), len(self.passes)))
        if self.findings:
            out.write("| gate | subject | finding |\n|---|---|---|\n")
            for f in self.findings:
                out.write("| %s | %s | %s |\n" % (f["gate"], f["subject"], f["msg"]))
            out.write("\n")
        for n in self.notes:
            out.write("- %s\n" % n)
        out.write("\n## Passing checks\n\n```\n" + "\n".join(self.passes) + "\n```\n")
        if self.details:
            out.write("\n## Evidence lines for findings\n\n```\n"
                      + "\n".join(self.details[:80]) + "\n```\n")
        return out.getvalue()


def run(company, checks, tier, outdir=None):
    rep = Report()
    # A gate that found nothing to read must never report clean.
    regs = [n for n in REGISTERS if locate(company, n)]
    docs = stage_docs(company)
    srcs = [p for pat in ("*.txt", "*.htm", "*.html")
            for p in glob.glob(os.path.join(company, "sources", "**", pat), recursive=True)]
    if not regs:
        rep.fail("coverage", "registers", "no register CSVs at root or research/ -- "
                 "csv/anchors gates DID NOT RUN")
    if not docs:
        rep.fail("coverage", "narrative", "no stage_*.md volumes found -- keys/anchors gates "
                 "DID NOT RUN")
    if not srcs:
        rep.fail("coverage", "sources", "no local source text under sources/ -- quotes gate "
                 "DID NOT RUN")
    rep.note("coverage", "%d registers, %d stage volumes, %d source documents"
             % (len(regs), len(docs), len(srcs)))
    if "csv" in checks:
        gate_csv(company, rep)
    if "keys" in checks:
        gate_keys(company, rep)
    if "anchors" in checks:
        gate_anchors(company, rep)
    if "quotes" in checks:
        gate_quotes(company, rep)
    if "budget" in checks:
        gate_budgets(company, rep, tier)
    md = rep.render(company)
    if outdir:
        os.makedirs(outdir, exist_ok=True)
        base = os.path.basename(company.rstrip("/\\"))
        open(os.path.join(outdir, "gates_%s.md" % base), "w", encoding="utf-8").write(md)
        json.dump({"findings": rep.findings}, open(os.path.join(outdir, "gates_%s.json" % base),
                                                   "w", encoding="utf-8"), indent=1)
    print(md)
    return len(rep.findings)


# ---------------------------------------------------------------- self-test
# Each defect below was actually missed by an agent pass at some point in this run.

def self_test():
    ok = True
    tmp = tempfile.mkdtemp(prefix="gates_selftest_")
    comp = os.path.join(tmp, "company_999_selftest")
    os.makedirs(os.path.join(comp, "sources"))
    try:
        # canonical fixture
        open(os.path.join(comp, "sources.csv"), "w", encoding="utf-8").write(
            "source_id,title,date,stage\nS0001,Original S-1,1997-03-24,stage1\n"
            "S0002,FY1997 10-K,1998-03-30,stage2\n")
        open(os.path.join(comp, "timeline.csv"), "w", encoding="utf-8").write(
            "record_id,event_date,description,stage,source_id,anchor\nT0001,1994-07-05,found,"
            "stage1,S0001,U.1\n")
        open(os.path.join(comp, "stage_1.md"), "w", encoding="utf-8").write(
            "### U.1 Founding\nThe company stated \"the Board of Directors and the sole "
            "stockholder on September 15, 1994\" (S0001).\n")
        open(os.path.join(comp, "sources", "s1.txt"), "w", encoding="utf-8").write(
            "<html>the Board of Directors and the sole stockholder on September 15, 1994 "
            "and other text</html>")

        def findings_for(mut, tag):
            d = os.path.join(tmp, "case_%02d" % tag)
            shutil.copytree(comp, d)
            mut(d)
            r = Report()
            gate_csv(d, r)
            gate_quotes(d, r, min_words=8)
            gate_anchors(d, r)
            gate_keys(d, r)
            gate_budgets(d, r, "core")
            return r

        cases = {}

        def plant_unquoted_comma(d):
            plant(os.path.join(d, "timeline.csv"), lambda t: t.replace(
                "record_id,event_date,description,stage,source_id",
                "record_id,event_date,description, with comma,stage,source_id"))
        cases["unquoted comma shifts fields"] = plant_unquoted_comma

        def plant_numeric_stage(d):
            plant(os.path.join(d, "timeline.csv"),
                  lambda t: t.replace("stage1,S0001", "1,S0001"))
        cases["numeric stage vocabulary"] = plant_numeric_stage

        def plant_duplicate_id(d):
            with open(os.path.join(d, "timeline.csv"), "a", encoding="utf-8") as f:
                f.write("T0001,1994-07-05,dupe,stage1,S0001,U.1\n")
        cases["duplicate record id"] = plant_duplicate_id

        def plant_dangling_source(d):
            plant(os.path.join(d, "timeline.csv"), lambda t: t.replace("S0001", "S9999"))
        cases["dangling source_id"] = plant_dangling_source

        def plant_wrong_width(d):
            with open(os.path.join(d, "timeline.csv"), "a", encoding="utf-8") as f:
                f.write("T0002,1995-05-15,short\n")
        cases["row with wrong column count"] = plant_wrong_width

        def plant_paraphrase_as_quote(d):
            plant(os.path.join(d, "stage_1.md"), lambda t:
                  '### U.1 Founding\nThe company stated "the board and one owner in '
                  'nineteen ninety four" (S0001).\n')
        cases["paraphrase presented as quote"] = plant_paraphrase_as_quote

        def plant_orphan_anchor(d):
            p = os.path.join(d, "stage_1.md")
            open(p, "a", encoding="utf-8").write("\n### U.77 Orphan\nnothing registers this\n")
        cases["anchor with no register row"] = plant_orphan_anchor

        def plant_wrong_width(d):
            p = os.path.join(d, "timeline.csv")
            open(p, "a", encoding="utf-8").write("T0002,1995-05-15,short\n")
        cases["row with wrong column count"] = plant_wrong_width

        def plant_retired_key(d):
            plant(os.path.join(d, "stage_1.md"), lambda t: t + "\nCited to S0999 which is not a key.\n")
        cases["unresolvable source token in narrative"] = plant_retired_key

        GATE_OF = {"unquoted comma shifts fields": "csv",
                   "numeric stage vocabulary": "csv",
                   "duplicate record id": "csv",
                   "dangling source_id": "csv",
                   "row with wrong column count": "csv",
                   "paraphrase presented as quote": "quotes",
                   "anchor with no register row": "anchors",
                   "unresolvable source token in narrative": "keys"}
        cases = {k: (GATE_OF[k], v) for k, v in cases.items()}

        for tag, (label, (gate_want, mut)) in enumerate(sorted(cases.items()), start=1):
            r = findings_for(mut, tag)
            fired = any(f["gate"] == gate_want for f in r.findings)
            print("%-40s %-8s %s" % (label, "[%s]" % gate_want,
                                     "CAUGHT" if fired else "*** NOT DETECTED BY ITS OWN GATE ***"))
            if not fired:
                ok = False
        # negative control: the clean fixture must produce zero findings
        clean = findings_for(lambda d: None, 0)
        if clean.findings:
            print("%-40s %s" % ("clean fixture", "FALSE POSITIVE %s" % clean.findings[:2]))
            ok = False
        else:
            print("%-40s %s" % ("clean fixture", "CLEAN"))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print("\nself-test: %s" % ("PASS" if ok else "FAIL -- a gate cannot catch its own defect"))
    return 0 if ok else 2


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--company-dir")
    ap.add_argument("--checks", default="csv,keys,anchors,quotes,budget")
    ap.add_argument("--tier", default="exemplar", choices=["exemplar", "core", "register"])
    ap.add_argument("--out")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    if not a.company_dir:
        raise SystemExit("need --company-dir or --self-test")
    n = run(a.company_dir, [c.strip() for c in a.checks.split(",")], a.tier, a.out)
    return 1 if n else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main())
