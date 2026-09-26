#!/usr/bin/env python3
"""
harvest_mine.py -- turn harvester HITS into held BYTES, without an agent in the loop.

Why: `periodical_harvest.py` classifies a search result as TIER1_CANDIDATE from metadata --
title, date, collection. That is a lead, not evidence, and a tier verdict built on leads is the
"unqueried family read as a null" error wearing the opposite costume. Downloading and grepping
each candidate is mechanical, so it must not cost model tokens.

For each company this script:
  1. reads `founders_playbook/00_universe/harvest/candidates.csv`
  2. keeps TIER1_CANDIDATE / LEAD_ONLY rows and RANKS them by whether either date field lands in
     the company's origin window -- never filters on it, because `date_or_issue` is often the scan
     year (see the rank() comment)
  3. downloads the item's real OCR text layer through `ia_text.py` (metadata-resolved filename)
  4. greps and CLASSIFIES BY MATCH CLASS, because a hit is not a naming (see below)
  5. writes a per-company dossier at <company dir>/research/A4_harvest_mine.md plus a machine
     index at sources/harvest_mine/_index.json

**A bare company word is not a naming, and this script proved it to itself.** Grepping Apple's
window on the slug alone returned 162 hits in a 1976 federal education report -- over "APPLE
Observation System", an acronym for *Anecdotal Processing to Promote Learning Experience* -- and 6
hits in a foundation-for-the-blind report signed by a man surnamed Apple. Costco's hits were real:
a 1991 San Francisco environmental impact report printing "COSTCO WHOLESALE". The difference is the
**match class**, so the verdict now carries it: an entity-bearing phrase (two or more words from the
query label, e.g. "costco wholesale", "wal mart stores") is `TIER1_CANDIDATE_TEXT`; the bare slug
alone is `BARE_WORD_MATCH`, which is a lead about a *word*, never a naming; zero hits over held KB
is `NULL`; no bytes is `UNANSWERED`; an item not attempted is `UNTRIED`. Nothing here ever asserts a
fact -- it produces bytes, line numbers and match classes for a reader to interpret.
"""

import argparse
import csv
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ia_text  # noqa: E402  (same repo, same stdlib-only rules)

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAND = os.path.join(REPO, "founders_playbook", "00_universe", "harvest", "candidates.csv")

# origin window per company slug: (start, end) -- deliberately WIDE where the founding date is
# itself unestablished in our corpus; a narrow window here would silently drop the evidence that
# could establish it. `UNREFINED` marks windows copied from the universe CSV's fiscal column.
WINDOWS = {
    "walmart": ("1945-01-01", "1972-12-31"), "unitedhealth": ("1974-01-01", "1995-12-31"),
    "apple": ("1975-01-01", "1980-12-31"), "alphabet": ("1996-01-01", "2004-12-31"),
    "cvs": ("1963-01-01", "1996-12-31"), "berkshire": ("1962-01-01", "1978-12-31"),
    "mckesson": ("1969-01-01", "1995-12-31"), "exxonmobil": ("1866-01-01", "1999-12-31"),
    "cencora": ("1985-01-01", "2000-12-31"), "microsoft": ("1975-01-01", "1986-12-31"),
    "jpmorgan": ("1799-01-01", "1960-12-31"), "costco": ("1975-01-01", "1993-12-31"),
    "cigna": ("1979-01-01", "1995-12-31"), "cardinal": ("1971-01-01", "1995-12-31"),
    "nvidia": ("1993-01-01", "1999-12-31"), "meta": ("2003-01-01", "2012-12-31"),
    "elevance": ("1944-01-01", "2014-12-31"), "centene": ("1984-01-01", "2002-12-31"),
    "bofa": ("1791-01-01", "1998-12-31"), "chevron": ("1879-01-01", "1984-12-31"),
    "ford": ("1903-01-01", "1950-12-31"), "gm": ("1908-01-01", "1930-12-31"),
    "citigroup": ("1812-01-01", "1998-12-31"), "homedepot": ("1978-01-01", "1990-12-31"),
    "fanniemae": ("1938-01-01", "1970-12-31"), "kroger": ("1883-01-01", "1960-12-31"),
    "verizon": ("1877-01-01", "2000-12-31"), "phillips66": ("1917-01-01", "2002-12-31"),
    "marathon": ("1887-01-01", "2011-12-31"), "stonex": ("1984-01-01", "2000-12-31"),
    "statefarm": ("1922-01-01", "1960-12-31"), "freddiemac": ("1970-01-01", "1990-12-31"),
    "humana": ("1961-01-01", "1985-12-31"), "att": ("1885-01-01", "1984-12-31"),
    "goldman": ("1869-01-01", "1950-12-31"), "comcast": ("1963-01-01", "1990-12-31"),
    "wellsfargo": ("1852-01-01", "1998-12-31"), "morganstanley": ("1924-01-01", "1960-12-31"),
    "valero": ("1979-01-01", "2001-12-31"), "dell": ("1984-01-01", "1992-12-31"),
    "target": ("1902-01-01", "1970-12-31"), "tesla": ("2003-01-01", "2010-12-31"),
    "disney": ("1923-01-01", "1945-12-31"), "jnj": ("1886-01-01", "1960-12-31"),
    "pepsico": ("1898-01-01", "1965-12-31"), "boeing": ("1916-01-01", "1940-12-31"),
    "ups": ("1907-01-01", "1960-12-31"), "rtx": ("1920-01-01", "1997-12-31"),
    "fedex": ("1971-01-01", "1985-12-31"), "amazon": ("1994-01-01", "1997-12-31"),
}
DIR_FOR = {}   # slug -> company dir, discovered from the repo layout

# Ordered strongest-first: the verdict a row carries is which of these tests fired, and a reader
# deciding whether to open a file needs the strength, not just the count.
VERDICTS = ("TIER1_CANDIDATE_TEXT", "VARIANT_TERM_HIT", "BARE_WORD_MATCH", "NULL", "UNANSWERED")
SUM_LABEL = {"TIER1_CANDIDATE_TEXT": "entity_naming", "VARIANT_TERM_HIT": "variant_term",
             "BARE_WORD_MATCH": "bare_word_only", "NULL": "null", "UNANSWERED": "unanswered"}


def phrase_regex(phrases):
    r"""One alternation over entity phrases, with a separator class between their words.

    Not decoration, twice over. OCR layers run "COSTCO  WHOLESALE" with two spaces, and catalogue
    and print text hyphenates -- "Wal-Mart Stores" is the registrant's own spelling, and a
    literal-space pattern built from the de-punctuated query label "wal mart stores" would miss
    every occurrence of it. So: a word boundary, and a whitespace/dot/dash class between words.
    This project's held bytes are the positive control for both halves of that choice.
    """
    return "|".join(r"\b%s\b" % r"[\s.\-]+".join(re.escape(w) for w in p.split())
                    for p in phrases)


def entity_adjacency(names):
    r"""The promotion test: the company word sitting hard against a word only a company is next to.

    Needed because most quoted query terms are a single word -- `'Costco'`, `'Target'`, `'Microsoft'`
    -- so `split_terms` has no multi-word name phrase to promote a hit with, and a page printing
    "COSTCO  WHOLESALE" would otherwise be filed with the surnames. The three cases this separates
    are all bytes this repository holds:
      "COSTCO  WHOLESALE"                      -> the entity; `wholesale` sits next to it.
      "*APPLE Observation System"              -> an acronym (Anecdotal Processing to Promote
                                                 Learning Experience); nothing corporate is
                                                 adjacent, so it is a word, not a naming.
      "Loyal  E.  Apple,  Executive Director"  -> a surname.

    Deliberately tight -- at most three separator characters, same line -- and so deliberately
    under-claiming: a page that names the company with no adjacent identity word stays
    BARE_WORD_MATCH, which is still a lead with its sample lines printed, never a discarded item.
    """
    ctx = ("inc|incorporated|corp|corporation|co|company|companies|ltd|llc|plc|"
           "stores|wholesale|retail|retailers|computer|computers|systems|software|"
           "industries|holdings|group|enterprises|enterprise|international|"
           "shares|stock|nasdaq|nyse|wall\\ street|revenue|sales|employees|supermarket")
    alt = "|".join(re.escape(n) for n in names if n)
    if not alt:
        return None
    return re.compile(r"\b(?:%s)\b[\s.,;:'\`\-\u2019]{0,3}(?:%s)\b" % (alt, ctx), re.I)


def quoted_terms(rows):
    r"""The entity vocabulary the HARVESTER used, taken from its own `query` column.

    The queries are written as `'Costco'`, `'Price Club'`, `'Apple Computer'`, `'Micro-Soft'`,
    `'Dayton Hudson'` -- quoted terms, including the predecessor and variant spellings that were
    the whole reason those rows exist. Using them is both more accurate and less invented than any
    list I could type here. **The column is `query`; there is no `query_label`.** An earlier
    revision of this script read `query_label`, got an empty string for all 1,562 rows, and so
    classified every single hit as a bare word -- the same assumed-column-name failure RD-121
    recorded for `identifier`/`date`. Enumerate the header before trusting a field.
    """
    out = set()
    for r in rows:
        for a, b in re.findall(r"'([^']+)'|\"([^\"]+)\"", (r.get("query") or "")):
            t = de_punct(a or b)
            if 2 < len(t) <= 40:
                out.add(t)
    return sorted(out)


def de_punct(text):
    """Lower-case, and punctuation becomes a SPACE: deleting it glues "Wal-Mart" into "walmart",
    and a term built from that can never match the registrant's own hyphenated print spelling."""
    return re.sub(r"[^A-Za-z0-9]+", " ", (text or "").lower()).strip()


def is_name_phrase(phrase, slug):
    """Does this quoted term name the company, or is it a word that merely sits near it?

    'costco wholesale', 'wal mart', 'micro soft', 'apple computer' -> yes, the slug is in there once
    the spaces are removed ('walmart' from 'wal mart', 'microsoft' from 'micro soft').
    'price club', 'dayton hudson', 'charter med' -> no: those are predecessor and sister registrants,
    and 'chain store age' / 'discount store news' -> no: those are the trade-press TITLES the
    harvester quoted while searching for the company. The query field mixes all three kinds, so the
    classifier separates them instead of promoting anything that merely came from a quote.
    """
    j = phrase.replace(" ", "")
    return bool(j) and (slug in j or j in slug)


def split_terms(terms, slug):
    """(name phrases, other entity terms) -- see is_name_phrase for why the second is not a naming."""
    named, other = [], []
    for t in terms:
        if " " not in t:
            continue
        (named if is_name_phrase(t, slug) else other).append(t)
    return named[:40], other[:40]


def which_phrases(hits, pat_phrase, cap=6):
    """Which entity phrase actually matched -- so a reader sees the carrier, not just a count."""
    if not pat_phrase:
        return []
    rx = re.compile(pat_phrase, re.I)
    got = set()
    for h in hits:
        for txt in [h.get("text", "")] + list(h.get("context") or []):
            m = rx.search(txt or "")
            if m:
                got.add(m.group(0).lower())
        if len(got) >= cap:
            break
    return sorted(got)


def promoted_by(hits, rx, cap=8):
    """The bare-word hits the adjacency test promotes, each carrying the string that promoted it.

    A promotion without its evidence would be exactly the thing this classifier was written to
    stop -- a label a reader cannot check.
    """
    out = []
    if not rx:
        return out
    for h in hits:
        for txt in [h.get("text", "")] + list(h.get("context") or []):
            m = rx.search(txt or "")
            if m:
                hh = dict(h)
                hh["promoted"] = m.group(0).lower()
                out.append(hh)
                break
        if len(out) >= cap:
            break
    return out


def classify_item(nbytes, named_hits, adj_hits, other_hits, bare_hits):
    if named_hits or adj_hits:
        return "TIER1_CANDIDATE_TEXT"
    if other_hits:
        return "VARIANT_TERM_HIT"
    if bare_hits:
        return "BARE_WORD_MATCH"
    return "NULL" if nbytes > 400 else "UNANSWERED"


def self_test():
    r"""Controls for the classifier, run through the REAL path -- same quoted_terms, same split,
    same grep, same classify_item. A detector that has not been shown the case it exists to reject
    is not a detector, and this project has now paid for that twice (gates.py's planted defects,
    ia_text's failed positive control).

    Every fixture line is a byte this repository actually held:
      the 1976 federal education report whose "APPLE" is an acronym (Anecdotal Processing to Promote
        Learning Experience), which the old bare-slug grep returned as 162 Tier-1 hits;
      a foundation-for-the-blind report signed by a man surnamed Apple (6 more);
      the 1991 San Francisco environmental report printing "COSTCO  WHOLESALE", a real one;
      FY1972 registrant print spelling itself "WAL-MART STORES", which a de-punctuated pattern
        glued into "walmartstores" and lost;
      a Target-window file whose only entity is the predecessor "Dayton Hudson" -- related, but not
        a naming of the company the row is about.
    """
    import tempfile
    fixtures = [
        ("an acronym that happens to spell the company is NOT a naming",
         ["*APPLE Observation System",
          "the final report describes the APPLE (Anecdotal Processing to Promote",
          "Learning Experience) Observation System, a low inference descriptive",
          "Loyal  E.  Apple,  Executive Director, American Foundation for the Blind"],
         "apple", ["'Apple Computer'", "'Apple II'", "'Steve Jobs'"], "BARE_WORD_MATCH"),
        ("the company word beside an identity word IS a candidate",
         ["COSTCO  WHOLESALE :", "Distribution List for the Costco WholesaIe Project Draft EIR"],
         "costco", ["'Costco'", "'Price Club'", "'Chain Store Age'"], "TIER1_CANDIDATE_TEXT"),
        ("a de-punctuated term still matches the hyphenated print spelling",
         ["FY1972 ANNUAL REPORT OF WAL-MART STORES, INC.",
          "(Reports). The Wal-Mart Stores, Inc. board met at Bentonville."],
         "walmart", ["'Wal-Mart Stores'", "'Walton'"], "TIER1_CANDIDATE_TEXT"),
        ("a predecessor name alone is a clue about a different registrant",
         ["THE DAYTON HUDSON COMPANY, NINTH AND GATEWAY AVENUES, MINNEAPOLIS"],
         "target", ["'Target'", "'Dayton Hudson'"], "VARIANT_TERM_HIT"),
        ("no match at all over held bytes is a NULL",
         ["nothing here at all " * 40], "walmart", ["'Wal-Mart Stores'"], "NULL"),
        ("text that never arrived is UNANSWERED, not a NULL",
         ["short"], "walmart", ["'Wal-Mart Stores'"], "UNANSWERED"),
    ]
    checks = []
    for name, body, slug, quoted, want in fixtures:
        d = tempfile.mkdtemp()
        p = os.path.join(d, "t.txt")
        with open(p, "w", encoding="utf-8") as f:
            f.write("\n".join(body) + "\n")
        rows = [{"query": q} for q in quoted]
        named, other = split_terms(quoted_terms(rows), slug)
        pat_named, pat_other = phrase_regex(named), phrase_regex(other)
        hn = ia_text.grep_local(p, pat_named) if named else []
        ho = ia_text.grep_local(p, pat_other) if other else []
        hb = ia_text.grep_local(p, r"\b%s\b" % re.escape(slug))
        adj = promoted_by(hb, entity_adjacency([slug] + [t for t in quoted_terms(rows)
                                                         if " " not in t]))
        got = classify_item(os.path.getsize(p), hn, adj, ho, hb)
        checks.append((got == want, name,
                       "%-19s named=%s promoted=%s other=%s bare=%d" % (
                           got, which_phrases(hn, pat_named),
                           [h["promoted"] for h in adj][:2],
                           which_phrases(ho, pat_other), len(hb))))
    for ok, name, detail in checks:
        print("  %-58s %s  %s" % (name, "PASS" if ok else "FAIL", detail))
    bad = [c for c in checks if not c[0]]
    print("selftest: %d checks, %d failing" % (len(checks), len(bad)))
    return 1 if bad else 0


def company_dirs():
    out = {}
    base = os.path.join(REPO, "founders_playbook", "01_companies")
    if not os.path.isdir(base):
        return out
    for d in os.listdir(base):
        m = re.match(r"company_\d+_(.+)$", d)
        if m:
            out[m.group(1)] = os.path.join(base, d)
    return out


def date_of(row):
    for k in ("date_or_issue", "date", "year", "beginning_date"):
        v = (row.get(k) or "").strip()
        if v:
            m = re.search(r"\d{4}", v)
            if m:
                return m.group(0) + "-01-01"
    return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--company", action="append", help="slug(s) to mine; default all with candidates")
    ap.add_argument("--limit", type=int, default=6, help="max items mined per company")
    ap.add_argument("--max-mb", type=float, default=8.0)
    ap.add_argument("--insecure", action="store_true", default=True,
                    help="allow the stale-CA fallback, and only for ia_text.INSECURE_HOSTS "
                         "(this machine's CA store is out of date, so the fleet default is on; "
                         "every such fetch is stamped ok-INSECURE in its sidecar)")
    ap.add_argument("--self-test", action="store_true",
                    help="run the match-class controls and exit")
    ap.add_argument("--min-year", help="override window start")
    ap.add_argument("--max-year", help="override window end")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    if not os.path.exists(CAND):
        print("no candidates.csv -- run tools/periodical_harvest.py first")
        return 2
    rows = list(csv.DictReader(open(CAND, encoding="utf-8")))
    dirs = company_dirs()
    want = [s.lower() for s in (a.company or [])] or sorted({r.get("company", "").lower() for r in rows})
    report = {}
    skipped_no_dir = []
    for slug in want:
        if slug not in dirs:
            # No company directory yet. The first fleet run fell back to "." and wrote 11.4 MB of
            # held bytes into a root-level sources/ -- real primary text, in the wrong place and
            # invisible to every company gate. A company that has not been scaffolded is UNTRIED,
            # and says so; it never borrows the repository root as a cache.
            sub0 = [r for r in rows if (r.get("company") or "").strip().lower() == slug]
            if sub0:
                skipped_no_dir.append((slug, len(sub0)))
            continue
        sub = [r for r in rows if (r.get("company") or "").strip().lower() == slug
               and (r.get("classification") or "").startswith(("TIER1", "LEAD"))]
        if not sub:
            continue
        lo, hi = WINDOWS.get(slug, (a.min_year or "1800-01-01", a.max_year or "2010-12-31"))
        if a.min_year:
            lo = a.min_year
        if a.max_year:
            hi = a.max_year
        # The entity vocabulary comes from the harvester's own quoted query terms -- including the
        # predecessor spellings and hyphen variants those queries were written to catch. Split into
        # terms that NAME this registrant and terms that merely travel with it (see is_name_phrase).
        # Vocabulary from the company's WHOLE query set, not only the rows that survived
        # classification: a NULL-classified query still states the predecessor spelling it searched,
        # and that name is needed to judge the rows that did survive.
        terms = quoted_terms([r for r in rows
                              if (r.get("company") or "").strip().lower() == slug])
        named, other = split_terms(terms, slug)
        # Three classes of hit, because they are three different kinds of claim:
        #   a name phrase ("wal mart stores", "micro soft")  -> the entity, and the term is printed;
        #   the company word hard against an identity word ("COSTCO  WHOLESALE") -> also the entity;
        #   the bare word alone -> can be a surname, an acronym or a fruit, so it is a lead only.
        # A hit on an OTHER term ('price club', 'dayton hudson', 'chain store age') is its own
        # class: the file mentions a related name, which is a clue, not a naming of this company.
        pat_named = phrase_regex(named)
        pat_other = phrase_regex(other)
        pat_bare = r"\b%s\b" % re.escape(slug)
        rx_adj = entity_adjacency([slug] + [t for t in terms if " " not in t])
        # The harvest index's `date_or_issue` is frequently the SCAN or UPLOAD year, not the
        # publication year -- "Corporate Directory of US Public Companies 1995" arrives dated
        # 2016-06-11. Filtering a window on that field silently discards the in-window evidence
        # the window exists to find, which is the untried-family-as-null error again. So: RANK by
        # date agreement, never EXCLUDE. Both dates are reported and a mismatch is flagged.
        def rank(r):
            d = date_of(r)
            ty = re.search(r"(1[89]\d{2}|20[01]\d)", (r.get("title") or ""))
            ey = (ty.group(1) + "-01-01") if ty else ""
            inw = "9" if (d and lo <= d <= hi) or (ey and lo <= ey <= hi) else "0"
            cls = "9" if (r.get("classification") or "").startswith("TIER1") else "5"
            return inw + cls
        sub = sorted(sub, key=rank, reverse=True)
        seen, results, untried = set(), [], 0
        for r in sub:
            ident = (r.get("item_id") or r.get("identifier") or "").strip()
            d = date_of(r)
            ty = re.search(r"(1[89]\d{2}|20[01]\d)", (r.get("title") or ""))
            ey = ty.group(1) if ty else ""
            if not ident or ident in seen or ident.startswith("http"):
                continue
            if len(results) >= a.limit:
                untried += 1
                continue
            seen.add(ident)
            cdir = dirs[slug]
            path, status, nbytes = ia_text.fetch(cdir, ident, a.max_mb, a.insecure)
            if not path:
                results.append({"identifier": ident, "date": d, "status": status,
                                "verdict": "UNANSWERED", "hits": 0})
                continue
            ph = ia_text.grep_local(path, pat_named) if named else []
            vt = ia_text.grep_local(path, pat_other) if other else []
            bare = ia_text.grep_local(path, pat_bare)
            adj = promoted_by(bare, rx_adj)
            verdict = classify_item(nbytes, ph, adj, vt, bare)
            results.append({"identifier": ident, "date": d, "title_year": ey,
                            "date_mismatch": bool(ey and d and ey not in d),
                            "in_window": bool((d and lo <= d <= hi) or (ey and lo + "-01-01" <= ey + "-12-31" <= hi)),
                            "title": (r.get("title") or "")[:120],
                            "family": r.get("source_family"), "meta_date": d,
                            "status": status, "bytes": nbytes,
                            "named_terms": named, "other_terms": other,
                            "verdict": verdict,
                            "hits": len(bare), "phrase_hits": len(ph),
                            "entity_hits": len(ph) + len(adj),
                            "matched_entities": sorted(set(
                                which_phrases(ph, pat_named)
                                + [h["promoted"] for h in adj])),
                            "matched_other_terms": sorted(set(
                                which_phrases(vt, pat_other))),
                            "sample": (ph or adj or vt or bare)[:5]})
        report[slug] = {"window": [lo, hi], "candidates": len(sub), "mined": len(results),
                        "untried_by_limit": untried, "items": report_items(results)}
        write_dossier(dirs[slug], slug, report[slug])
    out = {k: dict(
               {"window": v["window"], "candidates": v["candidates"], "mined": v["mined"],
                "bytes": sum(i.get("bytes", 0) for i in v["items"])},
               **{SUM_LABEL[verd]: sum(1 for i in v["items"] if i.get("verdict") == verd)
                  for verd in VERDICTS})
           for k, v in report.items()}
    print(json.dumps(out, indent=1))
    if skipped_no_dir:
        print("UNTRIED -- no company directory yet (%d slugs, %d candidate rows waiting on "
              "scaffolding, not on a search): %s"
              % (len(skipped_no_dir), sum(n for _, n in skipped_no_dir),
                 ", ".join("%s(%d)" % s for s in skipped_no_dir[:12])))
    return 0


def report_items(results):
    return [{k: v for k, v in r.items() if k != "sample"} | {"sample": r.get("sample", [])[:3]}
            for r in results]


def write_dossier(cdir, slug, data):
    """The per-company page: held bytes, counts, line numbers and a match class. Never a finding."""
    if not cdir:
        return
    d = os.path.join(cdir, "sources", "harvest_mine")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "_index.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1)
    items = data["items"]
    n = {k: sum(1 for i in items if i.get("verdict") == k) for k in VERDICTS}
    named = sorted({t for i in items for t in i.get("named_terms") or []})
    other = sorted({t for i in items for t in i.get("other_terms") or []})
    lines = [
        "# Harvest mining -- %s" % slug, "",
        "Window applied: %s .. %s (deliberately WIDE where the founding date is itself "
        "unestablished -- narrowing it here would silently discard the evidence that could "
        "establish it)." % tuple(data["window"]), "",
        "%d candidate rows in the harvest index; %d items mined; %d left untried at the --limit."
        % (data["candidates"], data["mined"], data["untried_by_limit"]), "",
        "**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for "
        "an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a "
        "404/403 is UNANSWERED; an item not attempted is UNTRIED.", "",
        "**The match class is the verdict, and it is the half that keeps this honest.**",
        "",
        "| class | here | what it means |",
        "|---|---|---|",
        "| `TIER1_CANDIDATE_TEXT` | %d | a phrase naming this registrant, or its word hard "
        "against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in "
        "the `promoted by` column, so the label is checkable rather than trusted. |" % n[
            "TIER1_CANDIDATE_TEXT"],
        "| `VARIANT_TERM_HIT` | %d | a hit on a quoted term that is NOT this registrant's name -- a "
        "predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside "
        "(`chain store age`). Related and worth opening; not a naming of this company. |"
        % n["VARIANT_TERM_HIT"],
        "| `BARE_WORD_MATCH` | %d | only the company *word* matched, and that word is also a "
        "surname, an acronym and a fruit. The 1976 federal education report whose APPLE means "
        "*Anecdotal Processing to Promote Learning Experience* is the case that produced this "
        "class, at 162 fake Tier-1 hits. |" % n["BARE_WORD_MATCH"],
        "| `NULL` | %d | text held, zero hits. |" % n["NULL"],
        "| `UNANSWERED` | %d | no text reached the corpus, so nothing is known either way. |"
        % n["UNANSWERED"], "",
        "A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, "
        "and never counted in a tier verdict.", "",
        "Entity vocabulary this pass applied -- **name phrases**: %s; **other quoted terms** "
        "(predecessors, siblings, trade titles): %s. Both come from the harvester's own `query` "
        "column, not from a list I typed."
        % (", ".join("`%s`" % t for t in named) or "none",
           ", ".join("`%s`" % t for t in other) or "none"), "",
        "| identifier | dates (scan/title) | window | bytes | word hits | entity hits | "
        "promoted by | verdict |",
        "|---|---|---|---|---|---|---|---|"]
    for it in items:
        lines.append("| `%s` | %s | %s | %s | %s | %s | %s | %s |" % (
            it["identifier"],
            (it.get("date") or "?") + (" / title:" + it["title_year"] if it.get("title_year")
                                       else ""),
            ("in-window" if it.get("in_window") else "outside?")
            + (" MISMATCH" if it.get("date_mismatch") else ""),
            format(it.get("bytes", 0), ","), it.get("hits", 0),
            format(it.get("entity_hits", 0), ","),
            ", ".join("`%s`" % p for p in it.get("matched_entities") or []) or "-",
            it.get("verdict")))
    lines += ["", "_The scan-date field is often the digitisation year, so `outside?` means the "
              "metadata does not place it in the window -- not that the item is out of scope._",
              "", "## Sample hit lines (verbatim, with the held file's line numbers)", ""]
    for it in items:
        for h in it.get("sample") or []:
            lines.append("- `%s` l.%s: %s" % (it["identifier"], h.get("line"),
                                              (h.get("text") or "").strip()[:240]))
    with open(os.path.join(cdir, "research", "A4_harvest_mine.md"), "w",
              encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main())
