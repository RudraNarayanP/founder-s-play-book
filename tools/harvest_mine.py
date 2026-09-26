#!/usr/bin/env python3
"""
harvest_mine.py -- turn harvester HITS into held BYTES, without an agent in the loop.

Why: `periodical_harvest.py` classifies a search result as TIER1_CANDIDATE from metadata --
title, date, collection. That is a lead, not evidence, and a tier verdict built on leads is the
"unqueried family read as a null" error wearing the opposite costume. Downloading and grepping
each candidate is mechanical, so it must not cost model tokens.

For each company this script:
  1. reads `founders_playbook/00_universe/harvest/candidates.csv`
  2. keeps TIER1_CANDIDATE / LEAD_ONLY rows whose metadata date falls inside the company's
     origin window (from `tools/company_windows.py`-style table below, overridable by flag)
  3. downloads the item's real OCR text layer through `ia_text.py` (metadata-resolved filename)
  4. greps the company name variants and reports hits WITH LINE NUMBERS and surrounding text
  5. writes a per-company dossier at <company dir>/research/A4_harvest_mine.md plus a machine
     index at sources/harvest_mine/_index.json

Classification stays honest: a zero over held KB is a NULL; a 404/403/timeout or an item with no
text layer is UNANSWERED; an item never attempted because of --limit is UNTRIED. Nothing here ever
asserts a fact -- it produces bytes and counts for a human or an agent to interpret.
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
    ap.add_argument("--insecure", action="store_true", default=True)
    ap.add_argument("--min-year", help="override window start")
    ap.add_argument("--max-year", help="override window end")
    a = ap.parse_args()
    if not os.path.exists(CAND):
        print("no candidates.csv -- run tools/periodical_harvest.py first")
        return 2
    rows = list(csv.DictReader(open(CAND, encoding="utf-8")))
    dirs = company_dirs()
    want = [s.lower() for s in (a.company or [])] or sorted({r.get("company", "").lower() for r in rows})
    report = {}
    for slug in want:
        sub = [r for r in rows if (r.get("company") or "").strip().lower() == slug
               and (r.get("classification") or "").startswith(("TIER1", "LEAD"))]
        if not sub:
            continue
        lo, hi = WINDOWS.get(slug, (a.min_year or "1800-01-01", a.max_year or "2010-12-31"))
        if a.min_year:
            lo = a.min_year
        if a.max_year:
            hi = a.max_year
        pats = sorted({re.sub(r"[^A-Za-z0-9 ]", "", (r.get("query_label") or "").lower())
                       for r in sub if r.get("query_label")})
        # the grep term: company slug words plus any multi-word label token
        terms = [slug] + [p for p in pats if len(p.split()) > 1][:3]
        pattern = "|".join(re.escape(t) for t in dict.fromkeys(terms) if t)
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
            if len(results) >= a.limit:
                untried += 1
                continue
            seen.add(ident)
            cdir = dirs.get(slug, ".")
            path, status, nbytes = ia_text.fetch(cdir, ident, a.max_mb, a.insecure)
            if not path:
                results.append({"identifier": ident, "date": d, "status": status,
                                "verdict": "UNANSWERED", "hits": 0})
                continue
            hits = ia_text.grep_local(path, pattern or re.escape(slug))
            results.append({"identifier": ident, "date": d, "title_year": ey,
                            "date_mismatch": bool(ey and d and ey not in d),
                            "in_window": bool((d and lo <= d <= hi) or (ey and lo + "-01-01" <= ey + "-12-31" <= hi)),
                            "title": (r.get("title") or "")[:120],
                            "family": r.get("source_family"), "meta_date": d,
                            "status": status, "bytes": nbytes, "pattern": pattern,
                            "verdict": ("TIER1_CANDIDATE_TEXT" if hits else
                                        ("NULL" if nbytes > 400 else "UNANSWERED")),
                            "hits": len(hits), "sample": hits[:5]})
        report[slug] = {"window": [lo, hi], "candidates": len(sub), "mined": len(results),
                        "untried_by_limit": untried, "items": report_items(results)}
        write_dossier(dirs.get(slug), slug, report[slug])
    print(json.dumps({k: {"window": v["window"], "candidates": v["candidates"],
                          "mined": v["mined"],
                          "with_text_hits": sum(1 for i in v["items"]
                                                if i["verdict"] == "TIER1_CANDIDATE_TEXT"),
                          "null": sum(1 for i in v["items"] if i["verdict"] == "NULL"),
                          "unanswered": sum(1 for i in v["items"] if i["verdict"] == "UNANSWERED"),
                          "bytes": sum(i.get("bytes", 0) for i in v["items"])}
                      for k, v in report.items()}, indent=1))
    return 0


def report_items(results):
    return [{k: v for k, v in r.items() if k != "sample"} | {"sample": r.get("sample", [])[:3]}
            for r in results]


def write_dossier(cdir, slug, data):
    if not cdir:
        return
    d = os.path.join(cdir, "sources", "harvest_mine")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "_index.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1)
    lines = ["# Harvest mining -- %s" % slug, "",
             "Window applied: %s .. %s (a WIDE window where the founding date is itself "
             "unestablished -- narrowing it here would silently discard the evidence that could "
             "establish it)." % tuple(data["window"]), "",
             "%d candidate rows in the harvest index; %d items mined; %d left untried at the "
             "--limit." % (data["candidates"], data["mined"], data["untried_by_limit"]), "",
             "**Nothing on this page is a finding.** It is held bytes, hit counts and line "
             "numbers for an agent to interpret. A zero over held KB is a NULL; a missing text "
             "layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.", "",
             "| identifier | dates (scan/title) | window | bytes | hits | verdict |",
             "|---|---|---|---|---|---|",
             "", "_The scan-date field is often the digitisation year, so `outside?` means the "
             "metadata does not place it in the window -- not that the item is out of scope._"]
    for it in data["items"]:
        lines.append("| `%s` | %s | %s | %s | %s | %s |" % (
            it["identifier"], (it.get("date") or "?") + (" / title:" + it["title_year"]
                                                       if it.get("title_year") else ""),
            ("in-window" if it.get("in_window") else "outside?")
            + (" MISMATCH" if it.get("date_mismatch") else ""),
            format(it.get("bytes", 0), ","), it.get("hits", 0), it["verdict"]))
    lines += ["", "## Sample hit lines (verbatim, with the held file's line numbers)", ""]
    for it in data["items"]:
        for h in it.get("sample") or []:
            lines.append("- `%s` l.%s: %s" % (it["identifier"], h.get("line"),
                                               (h.get("text") or "").strip()[:240]))
    with open(os.path.join(cdir, "research", "A4_harvest_mine.md"), "w",
              encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main())
