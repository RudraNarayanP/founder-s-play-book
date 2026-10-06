#!/usr/bin/env python3
"""
legacy_cik.py -- find the CIK of a PREDECESSOR registrant, because the ticker answers with the survivor.

Why this exists: by 2026-09-30 three separate findings had the same shape. `XOM` resolves to
"ExxonMobil Holdings Corp" (CIK 2115436, filings from 2026) while the historic registrant is CIK 34088
"EXXON MOBIL CORP"; Comcast's index floor is 2002-02-11 because CIK 1166691 is the 2002 successor and the
1963 company filed under another CIK; AT&T, Bank of America, Cigna, Goldman, Morgan Stanley, Wells Fargo and
Verizon each have the same structure. For every one of them an in-window search of the CURRENT registrant
returns nothing, and "the filings family answers nothing in-window" is then a statement about the wrong legal
person.

This tool does NOT download anything and does NOT decide attribution. It lists candidates with the dates and
forms EDGAR itself reports, so a human or a probe can choose. The registrant guard in sec_intake.py stays the
thing that decides whether bytes may land in a company directory.

Stdlib only. Usage:
  python tools/legacy_cik.py search "Comcast"                     # name-root candidates
  python tools/legacy_cik.py search "Bank of Italy" --forms S-1,3-2
  python tools/legacy_cik.py detail 34088 1166691                 # name/form range per CIK
"""
import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request

UA = "FounderPlaybook Research AdminContact@example.com"
H = {"User-Agent": UA, "Referer": "https://www.sec.gov/"}
POLITE = 0.4


def get(url):
    for attempt in range(3):
        try:
            r = urllib.request.urlopen(urllib.request.Request(url, headers=H), timeout=60)
            return r.read()
        except Exception as e:
            if attempt == 2:
                return None
            time.sleep(2.0 * (attempt + 1))
    return None


def search(term, forms=None):
    """Name-root candidates from EDGAR's own company search.

    The ATOM output is not usable for this: EDGAR renders `title` and `name` as Perl string refs
    (`title="ARRAY(0x5606c0ae1cd0)"`) and carries no company name at all, which is how a first version
    of this tool returned "0 candidates" for `comcast` -- a false null about a company that has filed for
    decades. The HTML rows do carry CIK and name together, so that is what gets parsed, and a parse that
    yields nothing is reported as UNANSWERED rather than as an empty result set.
    """
    q = urllib.parse.quote(term)
    url = ("https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=%s"
           "&type=&dateb=&owner=include&count=250" % q)
    body = get(url)
    if body is None:
        print("SEARCH UNANSWERED for %r: EDGAR did not answer (this is not a null)." % term)
        return []
    txt = body.decode("utf-8", "replace")
    # The row markup puts the digits where a name should be, so the name is NOT read from this page: each
    # candidate's authoritative name comes from its own submissions JSON in `detail` below. A search that
    # finds CIKs is useful; a search that invents names is not.
    ciks = []
    for m in re.finditer(r"CIK=(\d{10})", txt):
        c = int(m.group(1))
        if c not in ciks:
            ciks.append(c)
    if not ciks:
        print("SEARCH PARSE FAILED for %r: EDGAR answered %d bytes and no CIK was read -- UNANSWERED, "
              "not zero candidates. Inspect the HTML before concluding anything." % (term, len(txt)))
        return []
    print("search %r -> %d candidate CIK(s); names and perimeters follow" % (term, len(ciks)))
    if forms:
        print("(--forms is informational; this tool never downloads)")
    for c in sorted(ciks)[:25]:
        time.sleep(POLITE)
        detail(c)
    return [(c, "") for c in ciks]


def detail(cik):
    u = "https://data.sec.gov/submissions/CIK%010d.json" % cik
    body = get(u)
    if body is None:
        print("  CIK %s: UNANSWERED" % cik)
        return None
    j = json.loads(body)
    rec = j.get("filings", {}).get("recent", {})
    dates = [d for d in rec.get("filingDate", []) if d]
    forms = sorted({f for f in rec.get("form", []) if f})
    n_slices = len(j.get("filings", {}).get("files", []) or [])
    print("  CIK %010d %-46s | recent rows %d, earliest %s, latest %s | %d archive slice(s)"
          % (cik, (j.get("name") or "")[:46], len(dates),
             min(dates) if dates else "?", max(dates) if dates else "?", n_slices))
    print("     tickers %s | formers %s" % (j.get("tickers"),
                                            [f.get("name") for f in (j.get("formerNames") or [])][:6]))
    print("     forms in `recent` (a full history needs the slices): %s" % ", ".join(forms[:22]))
    return j


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search")
    s.add_argument("term")
    s.add_argument("--forms", default="", help="comma list, informational only")
    d = sub.add_parser("detail")
    d.add_argument("ciks", nargs="+")
    a = ap.parse_args()
    if a.cmd == "search":
        cands = search(a.term)
        return 0 if cands else 1
    for c in a.ciks:
        time.sleep(POLITE)
        detail(int(re.sub(r"\D", "", c)))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main())
