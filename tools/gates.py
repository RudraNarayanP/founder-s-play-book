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
    "stage1": ["stage_1.md", "stage_1_part_*.md"],
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
    """Plain excel dialect -- doublequote=True, RFC-4180. An earlier version sniffed the
    dialect from a 4,000-byte sample, and on Amazon's registers csv.Sniffer returned
    doublequote=False, so correctly escaped "" fields shattered every record after them and
    the gate invented 43 width-drift findings that did not exist. Sniffing a header-bound
    property from a truncated sample is never safe."""
    with open(path, "r", encoding="utf-8", errors="replace", newline="") as f:
        rows = list(csv.reader(f, csv.excel))
    if not rows:
        return [], [], 0
    return rows[0], rows[1:], sum(len(r) for r in rows)


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

HARD_CAP = 60000   # method s9.2: the only word count that is a defect to exceed

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
        # A volume map and a claim-record appendix match `stage_*.md` by NAME but are not narrative
        # volumes: counting them made the coverage line report 3-4 volumes for a 1-volume company
        # (Tesla, 2026-09-30), and the budget gate would then grade an index at volume caps.
        out += [p for p in glob.glob(os.path.join(company, d, "stage_*.md"))
                if "_index" not in os.path.basename(p)
                and "claim_records" not in os.path.basename(p)]
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
    # A retired key that is being DISCUSSED (a collision note, a re-key map, a range like
    # `S3001…S3081`, a backticked example) is protected history, not a dangling citation.
    # An agent that re-pointed those would be deleting the record of how the ids collided.
    PROTECTED = re.compile(r"collision|re-?key|retired|supersed|provisional|UNRESOLVED|"
                           r"defect workaround|scheme|\brange\b|\bwas\b|formerly|backtick", re.I)
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
        cited = set()
        protected = set()
        # A token inside a quoted span is PRINT, not a pointer. Microsoft's merge found `keys`
        # reporting `S435` as an unresolvable citation: BYTE Dec 1980 l.38112 prints
        # "(MBASIC) S435/S45" because the OCR layer renders "$" as "S", so the string is a price
        # ($435 list / $45 dealer) quoted verbatim. Two "fixes" were available and both break a
        # harder rule: rewriting a protected byte-slice quotation, or minting a source row for a
        # dollar amount (RD-123). So the gate, not the corpus, is what changes here.
        quoted_spans = [(qm.start(), qm.end()) for qm in
                        re.finditer(r'"[^"\n]{4,}"', body)]
        for m in token.finditer(body):
            t = m.group(0)
            if t in have:
                cited.add(t)
                continue
            if any(a <= m.start() < b for a, b in quoted_spans):
                protected.add(t)
                continue
            window = body[max(0, m.start() - 60):m.end() + 60]
            backticked = body[max(0, m.start() - 1):m.start()] == "`"
            if PROTECTED.search(window) or backticked or re.search(r"[…-]\s*$|^\s*(to|–)",
                                                                   window[window.find(t) + len(t):]
                                                                   if t in window else ""):
                protected.add(t)
            else:
                cited.add(t)
        dangling = sorted(c for c in cited if c not in have)
        if protected:
            report.note("keys", "%s mentions %d retired keys inside collision/re-key/range "
                        "text -- protected history, not re-pointed: %s"
                        % (label, len(protected), ", ".join(sorted(protected)[:8])))
        if dangling:
            report.fail("keys", label,
                        "unresolvable source tokens: %s" % ", ".join(dangling[:15]))
        elif cited:
            report.ok("keys", label, "%d source tokens all resolve" % len(cited))


def declared_anchors(text):
    """An explicit ANCHORS declaration in a volume is authoritative when present.

    Written with no regex and no escapes on purpose. Walmart's merge proved the alternative is
    hopeless: conflict anchors are U.001-style at that company and U.1-style at Amazon, and
    section U ALSO numbers its subsections U.1, U.4, so no pattern can tell an anchor from a
    subsection across companies. Declaring the set removes the guess instead of encoding a
    guess about zero-padding width.

        <!-- ANCHORS: U.001-U.048, U.101-U.116, U.201-U.222 -->
    """
    i = text.find("ANCHORS:")
    if i < 0:
        return None
    j = text.find("-->", i)
    if j < 0:
        return None
    out = set()
    for tok in text[i + len("ANCHORS:"):j].replace(",", " ").split():
        if not tok.startswith("U."):
            continue
        if "-" in tok:
            lo, _, hi = tok.partition("-")
            try:
                a, b = int(lo.split(".")[1]), int(hi.split(".")[1] if "." in hi else hi)
            except (IndexError, ValueError):
                continue
            width = len(lo.split(".")[1])
            for n in range(min(a, b), max(a, b) + 1):
                out.add("U." + str(n).rjust(width, "0"))
        else:
            out.add(tok)
    return out or None


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
    """Whole-register scan. I tried restricting this to identifier columns on 2026-09-27 after the
    Wal-Mart audit showed §U's `U.0`-`U.4` subsection headings being echoed in prose columns and so
    "passing" parity by accident -- but it destroyed real coverage, because anchors legitimately
    live in `section` and `gap` cells (Apple's documented nulls U.025-U.039 vanished). The echo
    weakness is therefore handled by the ANCHORS declaration instead of by dropping columns."""
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
        body = open(p, encoding="utf-8", errors="replace").read()
        nar = declared_anchors(body)
        if nar is not None:
            report.note("anchors", "%s declares an explicit ANCHORS set (%d ids)"
                        % (os.path.relpath(p, company).replace("\\", "/"), len(nar)))
        else:
            nar = _anchors_declared(body)
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
    # A citation is not a declaration. Volume 2 of a split company declares zero anchors but
    # cites hundreds, and nothing until now asked whether each cited id actually exists. A row
    # or sentence pointing at U.077 when §U stops at U.055 is the same defect class as a
    # dangling source_id, and it silently strands the reader.
    cited_reg, cited_nar, reserved = set(), set(), set()

    def scan(paths, sink):
        for p in paths:
            if not (p and os.path.exists(p)):
                continue
            body = open(p, encoding="utf-8", errors="replace").read()
            for m in re.finditer(r"U\.\d+[a-z]?", body):
                t = m.group(0)
                pre = body[max(0, m.start() - 2):m.start()]
                post = body[m.end():m.end() + 3]
                # Backticked ids are being DISCUSSED (a dossier-local id, a reserve range like
                # `U.100`-`U.199`), not cited as an address -- same protected-history rule as
                # retired source keys. A range endpoint is a block reservation, not a pointer.
                if "`" in pre or "`" in post:
                    reserved.add(t)
                elif re.match(r"^[\s-]{1,2}U\.", post) or re.search(r"U\.\d+[a-z]?[\s-]{1,2}$", pre):
                    reserved.add(t)
                else:
                    sink.add(t)

    scan([locate(company, n) for n in REGISTERS], cited_reg)
    scan(stage_docs(company), cited_nar)
    # A register cell is structured: a row pointing at a section that was never written is
    # unambiguous damage. Prose is not -- it holds placeholder patterns (U.1n), reserved blocks
    # and id discussions -- so an unresolved prose mention is reported, never failed.
    hard = sorted(cited_reg - all_nar - reserved, key=_anchor_sort)
    advisory = sorted((cited_nar | cited_reg) - all_nar - reserved - set(hard), key=_anchor_sort)
    if reserved:
        report.note("anchors", "%d id(s) read as backticked references or range endpoints, not "
                    "citations (%s)" % (len(reserved), ", ".join(sorted(reserved)[:8])))
    if advisory:
        report.note("anchors", "%d prose mention(s) match no declared entry, ADVISORY only: %s"
                    % (len(advisory), ", ".join(advisory[:12])))
    unresolved = hard
    if unresolved:
        report.fail("anchors", "citation resolution",
                    "%d REGISTER row(s) cite a §U entry that is never declared: %s"
                    % (len(unresolved), ", ".join(unresolved[:15])))
    else:
        report.ok("anchors", "citation resolution", "every register-cited anchor resolves (%d "
                  "distinct ids across registers and volumes)"
                  % len(cited_reg | cited_nar | all_nar))
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


COR_RE = re.compile(r"\bCOR-(\d{2,3})\b")


def gate_corrections(company, report):
    """A retraction that reaches the narrative and not the registers is the failure this run
    keeps paying for (RD-059, RD-090, RD-105): CORRECTIONS.md withdraws a claim, `conflicts.csv`
    keeps asserting it, and the next reader trusts the register. So propagation is checked
    mechanically: every COR-nn must be referenced in the register layer AND in at least one
    stage volume that carried the withdrawn text."""
    cpath = locate(company, "CORRECTIONS.md")
    if not cpath:
        report.note("corrections", "no CORRECTIONS.md -- gate DID NOT RUN (not a pass)")
        return
    ids = sorted(set(COR_RE.findall(open(cpath, encoding="utf-8", errors="replace").read())))
    if not ids:
        report.note("corrections", "CORRECTIONS.md exists but names no COR-nn ids -- UNANSWERED")
        return
    reg_text, vol_text = "", ""
    for name in REGISTERS:
        p = locate(company, name)
        if p:
            reg_text += open(p, encoding="utf-8", errors="replace").read()
    for md in stage_docs(company):
        vol_text += open(md, encoding="utf-8", errors="replace").read()
    miss_reg, miss_vol = [], []
    for i in ids:
        tag = "COR-%s" % i
        if tag not in reg_text:
            miss_reg.append(tag)
        if tag not in vol_text and tag.lower() not in vol_text.lower():
            miss_vol.append(tag)
    report.note("corrections", "%d retraction ids; register layer reaches %d, volumes %d"
                % (len(ids), len(ids) - len(miss_reg), len(ids) - len(miss_vol)))
    if miss_reg:
        report.fail("corrections", "registers", "%d retraction(s) reach the prose but NOT any "
                    "register, so the register layer still teaches the withdrawn claim: %s"
                    % (len(miss_reg), ", ".join(miss_reg[:12])))
    if miss_vol:
        report.fail("corrections", "volumes", "%d retraction(s) name no stage volume -- either the "
                    "withdrawn text was never in a volume or the pointer is missing: %s"
                    % (len(miss_vol), ", ".join(miss_vol[:12])))
    if not miss_reg and not miss_vol:
        report.ok("corrections", "propagation", "all %d retraction(s) reach registers and volumes"
                  % len(ids))


STAGE_BIND = re.compile(r"stage\s*([123])\b[^\w]{1,8}\bT([123])\b", re.I)
CELL_HEAD = re.compile(r"\**\s*(?:s(?:tage?)?\s*)?([123])\b", re.I)
CELL_SUB = re.compile(r"\**\s*(?:s(?:tage?)?\s*)?[123]\s*[A-Za-z]\b", re.I)
CELL_ANY = re.compile(r"stage\s*([123])\b", re.I)
CELL_TIER = re.compile(r"\**\s*T([123])\b", re.I)
COMPANY_TIER = re.compile(r"^\s*\**\s*(?:the\s+|company\s+|planning\s+|overall\s+)*tier\s*[:=]\s*\**\s*T([123])\b",
                          re.I)


def _tier_bindings(line):
    """The (rank, stage, tier) assignments a line MAKES -- not the tiers it mentions.

    Three shapes carry an issuance, per s15.2 / RD-112, in decreasing specificity:

      rank 1  a dispatch line    `- **Stage 1 -- T2 core (22k w/stage, 6-9 runs). Dispatch it.**`
      rank 2  a per-stage table  `| **Stage 1** | 1908-1930 | ... | **T2 core** | 22k w/stage |`
      rank 3  a company line     `**TIER: T2 on the evidence standing on disk right now**`

    A tier token in prose is NOT an assignment. Boeing's probe writes "I would not claim T1 for Stage 1,
    and I would not claim T3 either" and JPMorgan's writes "No stage reaches T1, and Stage 1 cannot reach
    T1": binding on nearest-token proximity would issue Stage 1 as T1 from a sentence whose whole point is
    that it is NOT T1, so the separator run between the stage number and the tier token is restricted to
    non-word characters. Sub-window rows (CVS `S1a`/`S1d`, PepsiCo `1A`/`1B`) are skipped: they grade a
    slice of a stage, and the stage's own row (`| **Whole Stage 1 as dispatched** | ... | T2 core |`)
    is the number a `stage_1.md` volume is measured against.
    """
    out = [(1, int(m.group(1)), "T" + m.group(2)) for m in STAGE_BIND.finditer(line)]
    s = line.strip()
    if s.startswith("|") and s.count("|") >= 3:
        cells = [c.strip() for c in s.strip("|").split("|")]
        head = CELL_HEAD.match(cells[0])
        sg = None
        if head and not CELL_SUB.match(cells[0]):
            sg = int(head.group(1))
        else:
            m_any = CELL_ANY.search(cells[0])
            if m_any and not re.search(r"[123]\s*[A-Za-z]\b", m_any.group(0), re.I):
                sg = int(m_any.group(1))
        if sg:
            for c in cells[1:]:
                mc = CELL_TIER.match(c)
                if mc:
                    out.append((2, sg, "T" + mc.group(1)))
    elif not out:
        mc = COMPANY_TIER.match(line)
        if mc:
            out.append((3, None, "T" + mc.group(1)))
    return out


def doc_stage(path):
    b = os.path.basename(path).lower()
    m = re.match(r"(?:stage|s)_?([123])\b", b)
    return int(m.group(1)) if m else None


_TIER_CACHE = {}


def issued_tier(company, stage=None):
    """The tier THIS company's own dossier issued -- never the loosest default.

    The tier used to be a CLI flag defaulting to `exemplar`, so a T3 register company measured against a
    60,000-word cap passed by accident (RD-128's "a wrong checker needs a narrower claim"). Scope is
    `research/` ONLY, and a tier-verdict dossier outranks a passing mention: a merged volume discusses all
    three tiers while arguing its five-family verdict, and reading THAT as the issuance graded UnitedHealth
    as T3 on its own narrative's mention. Order: verdict-bearing filename, then dossier number, then mtime.

    `stage` is the volume's own stage number. s15.2 tiers are PER STAGE (RD-112), and a company's three
    stages are routinely issued at different tiers -- JPMorgan Stage 1 T2 core, Stages 2-3 T3 register --
    so grading one narrative volume at a company-wide tier was wrong in both directions. Three authors
    (GM, Boeing, JPMorgan, 2026-10-01/02) reported `--tier auto` measuring T3 while their probe's s5
    issued Stage 1 at T2: the verdict was written as a table row or a `Stage 1 -- T2 core` bullet, which
    the prose-only reader never recognised, and the register cap was then aimed at a core volume.
    """
    key = (os.path.abspath(company), stage)
    if key in _TIER_CACHE:
        return _TIER_CACHE[key]
    rx = re.compile(r"\bT([123])\b(?:\s*(?:core|register|exemplar|tier))?", re.I)
    verdict = re.compile(r"regrade|feasibility|tier|verdict|density", re.I)
    # A dossier discusses all three tiers while arguing its per-stage verdicts, so a mention-scan that
    # sorts by (file, offset) and takes the last hit reads a passing "not T1" as the issuance -- the Cigna
    # probe (2026-09-30) measured exactly that: it issued `T2 core, PROVISIONAL` and the gate read T3,
    # because on a single-file tie `sort(reverse=True)` fell through to the label string. Read the lines
    # that STATE a verdict, and prefer the planning/summary line over an early per-stage table.
    says = re.compile(r"\b(planning tier|tier verdict|verdict[:\s]|per[- ]stage tiers?|deliverable|"
                      r"tier[:=]|planned tier|stage 1[^.]{0,40}tier)\b|"
                      r"\bT[123]\s*(?:core|register|exemplar)\b", re.I)
    binds = []
    hits = []
    for p in glob.glob(os.path.join(company, "research", "*.md")):
        stem = os.path.basename(p)
        txt = open(p, encoding="utf-8", errors="replace").read()
        num = re.match(r"[A-Za-z]+(\d+)", stem)
        lines = txt.splitlines()
        mt = os.stat(p).st_mtime_ns
        for i, line in enumerate(lines):
            for rank, sg, tr in _tier_bindings(line):
                binds.append((rank, mt, int(num.group(1)) if num else 0, i, sg, tr, stem))
            for m in rx.finditer(line):
                hits.append((1 if says.search(line) or _tier_bindings(line) else 0,
                             1 if verdict.search(stem) else 0,
                             mt, int(num.group(1)) if num else 0, i, stem, "T" + m.group(1)))
    result = _resolve_tier(company, stage, binds, hits)
    _TIER_CACHE[key] = result
    return result


def _resolve_tier(company, stage, binds, hits):
    # binds: (rank, mtime, dossier no, line, stage, tier, stem); rank 1 = dispatch line,
    # 2 = per-stage table row, 3 = company-level `TIER: Tn` (stage None, so it answers for every volume).
    def pick(pool):
        pool = sorted(pool, key=lambda b: (-b[0], b[1], b[2], b[3]), reverse=True)
        return pool[0], pool

    if stage is not None:
        mine = [b for b in binds if b[4] in (stage, None)]
        if mine:
            top, pool = pick(mine)
            same_rank = {b[5] for b in pool if b[0] == top[0]}
            others = sorted({b[4] for b in binds if b[4] not in (stage, None)})
            return top[5], ("tier %s assigned to Stage %d by %s l.%d (rank %d: %s)%s%s"
                            % (top[5], stage, top[6], top[3] + 1, top[0],
                               "dispatch line" if top[0] == 1 else
                               "per-stage table row" if top[0] == 2 else "company tier line",
                               "" if len(same_rank) == 1 else
                               " -- DISAGREES (%s at this rank), newest wins; pass --tier if the "
                               "dossier means otherwise" % "/".join(sorted(same_rank)),
                               "" if not others else " (other stages bound separately, s15.2/RD-112)"))
    if binds and stage is None:
        pairs = sorted({(b[4], b[5]) for b in binds if b[4] is not None})
        if pairs:
            want = 1 if any(sg == 1 for sg, _ in pairs) else pairs[0][0]
            return (pick([b for b in binds if b[4] == want])[0][5],
                    "issuances read in research/: %s -- Stage %d shown; each volume is graded at its "
                    "own stage's tier" % (", ".join("Stage %d %s" % (sg, tr) for sg, tr in pairs), want))
        top, _pool = pick(binds)
        return top[5], "company-wide issuance read in research/: %s from %s l.%d" % (
            top[5], top[6], top[3] + 1)
    if not hits:
        return "exemplar", "no tier stated in this company's research/ dossiers -- exemplar assumed"
    hits.sort(reverse=True)
    latest = hits[0][6]
    verdict_hits = [h for h in hits if h[0]]
    if verdict_hits:
        verdict_hits.sort(key=lambda h: (h[2], h[3], h[4]), reverse=True)
        latest = verdict_hits[0][6]
    distinct = sorted({h[6] for h in hits})
    note = ("tier %s%s from %s%s" % (latest, " (a stated-verdict line)" if verdict_hits else "",
                                     hits[0][5],
                                     "" if len(distinct) == 1 else
                                     " -- %s all mentioned in research/ (%d mentions, %d on a "
                                     "verdict line); no per-stage assignment line was found, so this "
                                     "is the LAST-RESORT reading: if the dossier's own text names a "
                                     "different tier, trust the dossier and pass --tier explicitly, "
                                     "because this reader is not the authority on your finding"
                                     % ("/".join(distinct), len(hits), len(verdict_hits))))
    return latest, note


def gate_budgets(company, report, tier):
    caps = {"exemplar": 60000, "core": 22000, "register": 8000,
            "T1": 60000, "T2": 22000, "T3": 8000}
    for md in stage_docs(company):
        # `auto` resolves PER VOLUME: a company whose probe issues Stage 1 T2 and Stage 3 T3 must not
        # have its core volume aimed at the register cap (nor its register volume let off at the core one).
        used = tier
        if tier in ("auto", "TIER"):
            used, _why = issued_tier(company, stage=doc_stage(md))
        cap = caps.get(used, 60000)
        w = len(re.findall(r"\S+", open(md, encoding="utf-8", errors="replace").read()))
        base = os.path.basename(md)
        if w > HARD_CAP:
            # The only breach that is a defect: a file past the method's own volume limit.
            report.fail("budget", base, "%d words > the %d hard cap -- split at a section boundary, "
                        "never renumber (method s9.2/s9.3)" % (w, HARD_CAP))
        elif w > cap:
            # A tier cap is a DENSITY TARGET, not a file limit: "make it fit" has previously been
            # answered by deleting evidence. Advisory, so no agent can be told to repair real data.
            report.fail("advisory", base, "%d words over the %s (this volume's issued tier) density "
                        "target %d -- NOT a split mandate and NOT a defect; recorded so the tier is "
                        "measurable" % (w, used, cap))
        else:
            report.ok("budget", base, "%d words (tier %s target %d, hard cap %d)"
                      % (w, used, cap, HARD_CAP))


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
    if tier in ("auto", "TIER"):
        tier, why = issued_tier(company)
        print("tier: %s (%s)" % (tier, why))
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
    if "corrections" in checks:
        gate_corrections(company, rep)
    md = rep.render(company)
    if outdir:
        # Every brief in this run writes `--out <file>.md`, and the tool only took a directory, so two
        # agents re-saved stdout by hand and one reported the tool as broken. Accept both now: a path
        # ending in .md is the file, anything else is the folder the named report lands in.
        base = os.path.basename(company.rstrip("/\\"))
        if outdir.lower().endswith(".md"):
            mdpath = outdir
            jpath = outdir[:-3] + ".json"
            os.makedirs(os.path.dirname(os.path.abspath(mdpath)), exist_ok=True)
        else:
            os.makedirs(outdir, exist_ok=True)
            mdpath = os.path.join(outdir, "gates_%s.md" % base)
            jpath = os.path.join(outdir, "gates_%s.json" % base)
        open(mdpath, "w", encoding="utf-8").write(md)
        json.dump({"findings": rep.findings}, open(jpath, "w", encoding="utf-8"), indent=1)
        print("written: %s" % mdpath)
    print(md)
    substantive = [f for f in rep.findings if not is_advisory(f)]
    return len(rep.findings), len(substantive)


def is_advisory(f):
    """§15.6: an ADVISORY output is not a defect, so it must not decide the exit code.

    The filter used to read only the gate NAME, and Target's re-certifier ran a pass whose only finding
    was labelled ADVISORY yet still got exit 1. gate_quotes writes that marker in its MESSAGE; Target's
    fourth certifier then found the second half of the bug -- the SAME gate files the marker in the
    finding's SUBJECT, so a company with zero substantive findings exited 1 anyway. Classify on all three
    fields, and keep this at module scope so the self-test can drive it with a real finding.
    """
    return (f["gate"] in ("coverage", "advisory")
            or "ADVISORY" in str(f.get("msg", "")).upper()[:12]
            or "ADVISORY" in str(f.get("subject", "")).upper())


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
            gate_corrections(d, r)
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

        def plant_proper_escaping(d):
            # Negative control for the bug an agent caught in this gate: an RFC-correct
            # `""` escape plus an embedded comma must NOT read as width drift.
            with open(os.path.join(d, "timeline.csv"), "a", encoding="utf-8", newline="") as f:
                f.write('T0009,1996-01-01,"he said ""it works"", clearly",stage1,S0001,U.1\n')
        cases["correctly escaped doublequote must stay clean"] = plant_proper_escaping

        def plant_paraphrase_as_quote(d):
            plant(os.path.join(d, "stage_1.md"), lambda t:
                  '### U.1 Founding\nThe company stated "the board and one owner in '
                  'nineteen ninety four" (S0001).\n')
        cases["paraphrase presented as quote"] = plant_paraphrase_as_quote

        def plant_unpropagated_retraction(d):
            # A retraction recorded in CORRECTIONS.md that never reaches the register layer:
            # RD-105's exact shape (COR-16 appears 3x in prose, 0x in conflicts.csv).
            with open(os.path.join(d, "CORRECTIONS.md"), "w", encoding="utf-8") as f:
                f.write("# Corrections\n\nCOR-77 supersedes COR-2: the range claim is withdrawn;"
                        " the S-1 field is blank.\n")
        cases["retraction never reaches the registers"] = plant_unpropagated_retraction

        def plant_propagated_retraction(d):
            # Negative control: the same retraction, properly propagated, must stay clean.
            plant(os.path.join(d, "stage_1.md"),
                  lambda t: t + "\nSee COR-77 (supersedes COR-2).\n")
            with open(os.path.join(d, "CORRECTIONS.md"), "w", encoding="utf-8") as f:
                f.write("# Corrections\n\nCOR-77 supersedes COR-2: range withdrawn.\n")
            with open(os.path.join(d, "conflicts.csv"), "w", encoding="utf-8") as f:
                f.write("conflict_id,section,confidence,notes\n"
                        "U.1,§A,High,withdrawn reading superseded per COR-77\n")
        cases["propagated retraction must stay clean"] = plant_propagated_retraction

        def plant_dangling_anchor_citation(d):
            # A row that points at a section which does not exist. Same class as a dangling
            # source_id: the reader arrives and there is nothing there.
            plant(os.path.join(d, "timeline.csv"),
                  lambda t: t + "T0021,1996-06-01,cites a section that was never written,"
                              "stage1,S0001,U.777\n")
        cases["cited anchor matches no declaration"] = plant_dangling_anchor_citation

        def plant_backticked_anchor_is_reference(d):
            # Negative control: a dossier-local id being DISCUSSED is protected history, not a
            # broken pointer. Walmart's `U.100`-`U.199` reserve ranges are this case.
            plant(os.path.join(d, "stage_1.md"), lambda t: t + "\nReserve block `U.100`-`U.199`"
                  " is set aside for later conflicts; see `U.777`.\n")
        cases["backticked anchor id stays clean"] = plant_backticked_anchor_is_reference

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

        def plant_quoted_price_token(d):
            # NEGATIVE CONTROL for Microsoft's `S435` (RD-131): BYTE Dec 1980 l.38112 prints
            # "(MBASIC) S435/S45" because the OCR layer renders "$" as "S". Quoted verbatim inside a
            # passage, that string is PRINT about a price, not a pointer to a document -- and the
            # finding used to push a repair agent to either rewrite a protected quotation or mint a
            # source row for a dollar amount, both worse than the noise.
            plant(os.path.join(d, "stage_1.md"), lambda t: t + '\nAdvertised as "To licensed '
                  'users of Microsoft BASIC-80 (MBASIC) S435/S45" [OCR: $ list/$ dealer] (S0001).\n')
        cases["quoted OCR price token is print, not a citation"] = plant_quoted_price_token


        def plant_over_tier_target(d):
            # The old budget gate wrote "(split required)" for a TIER overage, which an honest agent
            # answers by deleting evidence: a density target is not a file limit (s15.2 vs s9.2).
            # 4,700 repeats x 5 words = 23,500 words: over `core` 22,000, under the 60,000 hard cap.
            open(os.path.join(d, "stage_2.md"), "w", encoding="utf-8").write(
                "# volume\n" + "lorem ipsum dolor sit amet " * 4700)
        cases["tier overage reads advisory"] = plant_over_tier_target

        def plant_over_hard_cap(d):
            # 12,200 repeats x 5 words = 61,000 words: past the only word count that is a defect.
            open(os.path.join(d, "stage_3.md"), "w", encoding="utf-8").write(
                "# volume\n" + "lorem ipsum dolor sit amet " * 12200)
        cases["hard cap breach is a defect"] = plant_over_hard_cap

        GATE_OF = {"unquoted comma shifts fields": "csv",
                   "numeric stage vocabulary": "csv",
                   "duplicate record id": "csv",
                   "dangling source_id": "csv",
                   "row with wrong column count": "csv",
                   "paraphrase presented as quote": "quotes",
                   "anchor with no register row": "anchors",
                   "cited anchor matches no declaration": "anchors",
                   "backticked anchor id stays clean": "anchors-NEGATIVE",
                   "quoted OCR price token is print, not a citation": "keys-NEGATIVE",
                   "unresolvable source token in narrative": "keys",
                   "correctly escaped doublequote must stay clean": "csv-NEGATIVE",
                   "retraction never reaches the registers": "corrections",
                   "propagated retraction must stay clean": "corrections-NEGATIVE",
                   "tier overage reads advisory": "advisory",
                   "hard cap breach is a defect": "budget"}
        cases = {k: (GATE_OF[k], v) for k, v in cases.items()}

        for tag, (label, (gate_want, mut)) in enumerate(sorted(cases.items()), start=1):
            if gate_want.endswith("-NEGATIVE"):
                r = findings_for(mut, tag)
                clean = not any(f["gate"] == gate_want[:-9] for f in r.findings)
                print("%-40s %-8s %s" % (label, "[neg]",
                                         "STAYS CLEAN" if clean else
                                         "*** FALSE POSITIVE *** %s" % r.findings[:2]))
                ok = ok and clean
                continue
            r = findings_for(mut, tag)
            fired = any(f["gate"] == gate_want for f in r.findings)
            print("%-40s %-8s %s" % (label, "[%s]" % gate_want,
                                     "CAUGHT" if fired else "*** NOT DETECTED BY ITS OWN GATE ***"))
            if not fired:
                ok = False
        # negative control: the clean fixture must produce zero findings
        cases.setdefault("retraction never reaches the registers", None)
        clean = findings_for(lambda d: None, 0)
        if clean.findings:
            print("%-40s %s" % ("clean fixture", "FALSE POSITIVE %s" % clean.findings[:2]))
            ok = False
        else:
            print("%-40s %s" % ("clean fixture", "CLEAN"))

        # issued_tier: the newest write wins, and a disagreement is reported rather than averaged.
        tc = os.path.join(tmp, "tier_case")
        os.makedirs(os.path.join(tc, "research"))
        open(os.path.join(tc, "research", "A_chronology_feasibility.md"), "w",
             encoding="utf-8").write("tier T3 register on the probe evidence\n")
        open(os.path.join(tc, "research", "A3_intake_regrade.md"), "w",
             encoding="utf-8").write("TIER: T2 core after intake\n")
        got, why = issued_tier(tc)
        print("%-40s %-8s %s" % ("tier regrade beats the probe", "[tier]",
                                 "PASS (%s)" % got if got == "T2" else "*** FAILED: %s %s" % (got, why)))
        ok = ok and got == "T2"

        # Per-stage issuance. GM, Boeing and JPMorgan's authors all reported the same thing on
        # 2026-10-01/02: `--tier auto` measured T3 while their probe's §5 issued Stage 1 at T2 core,
        # because the verdict was written as a TABLE ROW or a `Stage 1 -- T2 core` bullet and the reader
        # only recognised prose verdict lines. The trap line below is real prose from those dossiers:
        # "No stage reaches T1, and Stage 1 cannot reach T1" must NOT bind Stage 1 to T1.
        tsc = os.path.join(tmp, "tier_stage_case")
        os.makedirs(os.path.join(tsc, "research"))
        open(os.path.join(tsc, "research", "A_chronology_feasibility.md"), "w",
             encoding="utf-8").write(
                 "| stage | window | families | tier | w/stage | runs |\n"
                 "|---|---|---|---|---|---|\n"
                 "| **Stage 1** | 1799-01-01 -> 1955-12-31 | 2 | **T2 core** | 22k | 6-9 |\n"
                 "| **Stage 2** | 1956-01-01 -> 1999-12-31 | 1 | **T3 register, PROVISIONAL** "
                 "| 8k | 3-4 |\n"
                 "\n- **Stage 1 -- T2 core (22k w/stage, 6-9 runs). Dispatch it.**\n"
                 "- **Stage 2 -- T3 PROVISIONAL.** One opened carrier flips it to T2.\n"
                 "\n**Tier discipline, so it cannot be mis-inherited.** No stage reaches T1, and "
                 "Stage 1 cannot reach T1 through any family a 0-web probe can run.\n")
        for want, ask, label in (("T2", 1, "stage-1 table row reads T2"),
                                 ("T3", 2, "stage-2 table row reads T3")):
            got, why = issued_tier(tsc, stage=ask)
            print("%-40s %-8s %s" % (label, "[tier]",
                                     "PASS (%s)" % got if got == want
                                     else "*** FAILED: %s %s ***" % (got, why)))
            ok = ok and got == want
        # The banner `run()` prints resolves with stage=None, and a per-stage dossier reaches that
        # branch FIRST on every real run -- it crashed on the live dossiers minutes after the per-stage
        # path passed its own test. So the global call is a control, not a courtesy.
        got, why = issued_tier(tsc)
        print("%-40s %-8s %s" % ("global call on a per-stage dossier", "[tier]",
                                 "PASS (%s / %s...)" % (got, why[:34])
                                 if got == "T2" and "Stage 1 T2" in why
                                 else "*** FAILED: %s %s ***" % (got, why)))
        ok = ok and got == "T2" and "Stage 1 T2" in why

        # ... and the cap must follow the volume, not one company-wide guess: 12,000 words is inside
        # Stage 1's T2 target and outside the T3 cap the old reader applied to it.
        open(os.path.join(tsc, "stage_1.md"), "w", encoding="utf-8").write(
            "# volume\n" + "lorem ipsum dolor sit amet " * 2400)
        r = Report()
        gate_budgets(tsc, r, "auto")
        warn = [f for f in r.findings if f["subject"] == "stage_1.md"]
        print("%-40s %-8s %s" % ("core volume not capped at register tier", "[budget]",
                                 "PASS" if not warn else "*** FAILED: %s ***" % warn[:1]))
        ok = ok and not warn

        # The exit-code half of RD-140: gate_quotes files its ADVISORY marker in the finding's SUBJECT,
        # so a pass whose only finding is that advisory must still be substantive-free. This fixture
        # produces the finding by REAL retrieval, not by hand-writing a dict.
        qc = os.path.join(tmp, "case_adv")
        shutil.copytree(comp, qc)
        plant(os.path.join(qc, "stage_1.md"), lambda t:
              t + '\n### U.2 Nothing\nThe report notes "an entirely invented phrase that appears in '
                  'no carrier at all in this corpus" (S0001).\n')
        r = Report()
        gate_quotes(qc, r, min_words=8)
        adv = [f for f in r.findings if f["gate"] == "quotes"]
        fired = bool(adv) and adv[0]["subject"] == "ADVISORY"
        clean_exit = bool(adv) and not [f for f in r.findings if not is_advisory(f)]
        print("%-40s %-8s %s" % ("quotes ADVISORY must not fail the exit code", "[exit]",
                                 "PASS" if fired and clean_exit
                                 else "*** FAILED: fired=%s findings=%s ***" % (fired, adv[:1])))
        ok = ok and fired and clean_exit
        # Negative half: the same gate's real defect class must still count as substantive.
        still_bad = [f for f in [{"gate": "quotes", "subject": "verbatim", "msg": "3 of 200 unmatched"}]
                     if not is_advisory(f)]
        print("%-40s %-8s %s" % ("quotes verbatim defect stays substantive", "[exit]",
                                 "PASS" if still_bad else "*** FAILED ***"))
        ok = ok and bool(still_bad)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print("\nself-test: %s" % ("PASS" if ok else "FAIL -- a gate cannot catch its own defect"))
    return 0 if ok else 2


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--company-dir")
    ap.add_argument("--checks",
                    default="csv,keys,anchors,quotes,budget,corrections")
    ap.add_argument("--tier", default="auto", choices=["auto", "exemplar", "core", "register",
                                                       "T1", "T2", "T3"],
                    help="'auto' (default) reads the tier the company's own dossier issued; an "
                         "explicit value overrides it. The default used to be 'exemplar', so a T3 "
                         "company measured against a 60k cap passed by accident.")
    ap.add_argument("--out")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--fail-on", default="substantive", choices=["substantive", "all"],
                    help="'substantive' (default): exit non-zero only on real findings. A "
                         "coverage finding means a gate had no input yet -- which is the NORMAL "
                         "state for a freshly probed company with no volumes or registers, so "
                         "failing CI on it turns every early-stage company into a red X and the "
                         "signal stops meaning anything. 'all' fails on those too.")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    if not a.company_dir:
        raise SystemExit("need --company-dir or --self-test")
    total, substantive = run(a.company_dir, [c.strip() for c in a.checks.split(",")],
                             a.tier, a.out)
    if total != substantive:
        print(chr(10) + "coverage-only findings (a gate had no input yet): %d of %d -- expected "
              "for a freshly probed company, and NOT failing the exit code unless --fail-on all"
              % (total - substantive, total))
    metric = total if a.fail_on == "all" else substantive
    return 1 if metric else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main())
