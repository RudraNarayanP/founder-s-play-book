#!/usr/bin/env python3
"""
sec_intake.py -- deterministic SEC EDGAR intake for the Founder's Playbook.

Why this exists: filing retrieval was being done by research subagents, one URL at
a time, inside turns that also carried interpretation and authoring. Retrieval is
mechanical, so it is no longer agent work. This script builds the per-company source
index and downloads documents with provenance sidecars, so a dossier agent starts
from an index and local bytes instead of a search budget.

Stdlib only.  Usage:
  python tools/sec_intake.py resolve --ticker MSFT
  python tools/sec_intake.py index   --cik 1018724 --company-dir <dir>
  python tools/sec_intake.py facts   --cik 1018724 --company-dir <dir> --from 1994-01-01 --to 1998-12-31
  python tools/sec_intake.py grab    --cik 1018724 --company-dir <dir> --accession 0000891618-97-001309
  python tools/sec_intake.py auto    --cik 1018724 --company-dir <dir> --from 1994-01-01 --to 1997-12-31
                                     [--max-docs 40] [--max-mb 60]

Exit codes: 0 ok, 1 partial (some UNANSWERED), 2 hard failure.
A non-200 is recorded as UNANSWERED, never as a null. See 00_METHOD_AND_STYLE.md s14 r6.
"""

import argparse
import csv
import gzip
import hashlib
import io
import json
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.request

# Declared contact is mandatory: sec.gov returns 403 "Your Request Originates from an
# Undeclared Automated Tool" without it. Plain ASCII, no parentheses.
UA = "FounderPlaybook Research AdminContact@example.com"
REFERER = "https://www.sec.gov/"
POLITE_SECONDS = 0.12
HARD_DOC_CAP_BYTES = 60 * 1024 * 1024

# Forms that carry early-history evidence, in priority order for `auto`.
EARLY_FORMS = [
    "S-1", "S-1/A", "S-11", "S-4", "S-4/A", "424B1", "424B2", "424B4", "SB-2",
    "10-12B", "10-K", "10-K405", "10-K/A", "10-KB", "8-K", "DEF 14A", "SC 13D",
    "SC 13G", "SC 13G/A", "3-2", "S-3", "POS AM",
]
ERROR_MARKERS = (
    b"<Error><Code>NoSuchKey</Code>",
    b"<Code>NoSuchKey</Code>",
    b"x-amz-error-code",
    b"Request Rate Threshold Exceeded",
    "<title>Access Denied",
    b"Invalid Request",
)


def _ctx():
    # Local CA stores on this machine are stale for some CDN hosts; degrade only the
    # verification depth for the EDGAR hosts, never globally for other fetches.
    ctx = ssl.create_default_context()
    return ctx


def http_get(url, binary=False, tries=3):
    """Return (status, bytes_or_text, note). 'note' carries UNANSWERED reasons."""
    last = None
    for attempt in range(tries):
        req = urllib.request.Request(url)
        req.add_header("User-Agent", UA)
        req.add_header("Referer", REFERER)
        req.add_header("Accept-Encoding", "gzip, deflate")
        try:
            with urllib.request.urlopen(req, timeout=60, context=_ctx()) as r:
                raw = r.read()
                if r.headers.get("Content-Encoding", "").lower() == "gzip":
                    try:
                        raw = gzip.decompress(raw)
                    except OSError:
                        pass
                status = r.status
            if not binary:
                body = raw.decode("utf-8", "replace")
                # Legacy EDGAR pages are sometimes latin-1 tables in a utf-8 envelope.
                if "Request Rate Threshold Exceeded" in body:
                    return status, None, "THROTTLED (UNANSWERED, retry later)"
                return status, body, "ok"
            for marker in ERROR_MARKERS:
                if marker in raw:
                    return status, None, "ERROR PAGE, not saved"
            return status, raw, "ok"
        except urllib.error.HTTPError as e:
            last = "HTTP %s" % e.code
            if e.code in (403, 503, 504, 429):
                time.sleep(1.5 * (attempt + 1))
                continue
            return e.code, None, last
        except Exception as e:  # timeout / DNS / TLS: unanswered, not null
            last = "%s: %s" % (type(e).__name__, e)
            time.sleep(1.0 * (attempt + 1))
    return 0, None, "UNANSWERED after %d tries (%s)" % (tries, last)


def cik10(cik):
    return "%010d" % int(re.sub(r"\D", "", str(cik)))


def submissions_index(cik, max_slices=8):
    """Full filing list, following the archive slices -- the `recent` block stops ~2001."""
    c = cik10(cik)
    status, body, note = http_get("https://data.sec.gov/submissions/CIK%s.json" % c)
    if body is None:
        raise SystemExit("submissions fetch failed: %s" % note)
    j = json.loads(body)
    name = j.get("name")
    ticks = j.get("tickers") or []
    rows = []
    rec = j.get("filings", {}).get("recent", {})
    rows.extend(_as_records(rec, "recent"))
    files = j.get("filings", {}).get("files", []) or []
    if not files:
        note = "UNANSWERED: submissions JSON listed no archive slices, so pre-`recent` history is untested"
        rows.append({"accession": "", "form": "", "filingDate": "", "primaryDocument": "",
                     "source": "(no files[] block)", "status": note})
    for f in files[:max_slices]:
        # Slices live on the JSON API host, NOT under /Archives/edgar/data/<cik>/ --
        # the Archives form returns 503/404 and made `index` silently stop at 2020.
        url = "https://data.sec.gov/submissions/%s" % f["name"]
        s2, b2, n2 = http_get(url)
        if b2 is None:
            rows.append({"accession": "", "form": "", "filingDate": "",
                         "primaryDocument": "", "source": f["name"], "status": "UNANSWERED: " + n2})
            continue
        try:
            sj = json.loads(b2)
        except ValueError:
            rows.append({"accession": "", "form": "", "filingDate": "",
                         "primaryDocument": "", "source": f["name"], "status": "UNPARSEABLE JSON"})
            continue
        # Archive slices do NOT share the `recent` shape: some are flat column dicts.
        if isinstance(sj, dict) and "accessionNumber" in sj:
            rows.extend(_as_records(sj, f["name"]))
        else:
            for blk in (sj.get("filings", {}) or {}).values() if isinstance(sj.get("filings"), dict) else []:
                rows.extend(_as_records(blk, f["name"]))
    return name, (ticks[0] if ticks else ""), rows


def _as_records(block, source):
    keys = ["accessionNumber", "form", "filingDate", "primaryDocument", "primaryDocDescription", "reportDate"]
    n = max([len(block.get(k, []) or []) for k in keys] or [0])
    out = []
    for i in range(n):
        rec = {"source": source}
        for k in keys:
            vals = block.get(k, []) or []
            rec[k] = vals[i] if i < len(vals) else ""
        out.append(rec)
    return out


def _norm(rec):
    return {
        "accession": rec.get("accession", "") or rec.get("accessionNumber", ""),
        "form": (rec.get("form") or "").strip(),
        "filingDate": rec.get("filingDate") or "",
        "reportDate": rec.get("reportDate") or "",
        "primaryDocument": rec.get("primaryDocument") or "",
        "source": rec.get("source") or "",
    }


def write_index(company_dir, cik, name, ticker, rows):
    d = os.path.join(company_dir, "sources", "_index")
    os.makedirs(d, exist_ok=True)
    norm = [_norm(r) for r in rows if (r.get("accession") or r.get("accessionNumber"))]
    norm.sort(key=lambda r: (r["filingDate"] or "9999", r["form"]))
    with open(os.path.join(d, "submissions.json"), "w", encoding="utf-8") as f:
        json.dump({"cik": cik, "company": name, "ticker": ticker,
                   "built": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                   "count": len(norm), "filings": norm}, f, indent=1)
    with open(os.path.join(d, "submissions.csv"), "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["filingDate", "form", "accession", "reportDate",
                                          "primaryDocument", "source"])
        w.writeheader()
        for r in norm:
            w.writerow({k: r[k] for k in w.fieldnames})
    earliest = {}
    for r in norm:
        if r["form"] and r["form"] not in earliest and r["filingDate"]:
            earliest[r["form"]] = r
    lines = ["# SEC submissions index -- %s (CIK %s, %s)" % (name, cik10(cik), ticker),
             "",
             "Built by `tools/sec_intake.py` at %s. %d filings enumerated"
             % (time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime()), len(norm)),
             "",
             "**This file is the source of truth for what exists.** Do not re-search EDGAR for",
             "coverage; grep `submissions.csv` and report a form as absent only from this list.",
             "",
             "## Earliest filing per form", "",
             "| form | filed | accession | primary document |", "|---|---|---|---|"]
    for form in sorted(earliest, key=lambda x: earliest[x]["filingDate"]):
        r = earliest[form]
        lines.append("| %s | %s | %s | %s |" % (form, r["filingDate"], r["accession"], r["primaryDocument"]))
    lines += ["", "## UNANSWERED slices (never report these as absent)", ""]
    unanswered = [r for r in rows if "UNANSWERED" in str(r.get("status", ""))]
    if not unanswered:
        lines.append("(none)")
    for r in unanswered:
        lines.append("- `%s` -- %s" % (r.get("source"), r.get("status")))
    with open(os.path.join(d, "_INDEX.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    return len(norm), earliest


def doc_listing(cik, accession):
    acc = accession.replace("-", "")
    url = "https://www.sec.gov/Archives/edgar/data/%s/%s/index.json" % (cik10(cik), acc)
    s, body, note = http_get(url)
    if body is None:
        return None, note
    try:
        j = json.loads(body)
    except ValueError:
        return None, "UNPARSEABLE index.json (returned a page, not a listing)"
    items = j.get("directory", {}).get("item", []) or []
    out = []
    for it in items:
        try:
            size = int(it.get("size", "0") or 0)  # size arrives as a STRING
        except ValueError:
            size = 0
        out.append({"name": it.get("name", ""), "size": size})
    return out, "ok"


def grab(company_dir, cik, accession, filename, subdir="sec"):
    acc = accession.replace("-", "")
    safe = re.sub(r"[^A-Za-z0-9._-]", "_", filename)
    rel = os.path.join(subdir, "%s_%s" % (accession, safe))
    path = os.path.join(company_dir, "sources", rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    url = "https://www.sec.gov/Archives/edgar/data/%s/%s/%s" % (cik10(cik), acc, filename)
    s, raw, note = http_get(url, binary=True)
    if raw is None:
        return {"accession": accession, "file": filename, "status": note, "path": ""}
    if len(raw) > HARD_DOC_CAP_BYTES:
        return {"accession": accession, "file": filename, "status": "SKIPPED over cap", "path": ""}
    txt = raw.decode("utf-8", "replace")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(txt)
    words = len(re.findall(r"\S+", re.sub(r"<[^>]+>", " ", txt)))
    side = {"url": url, "fetched": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "sha1": hashlib.sha1(raw).hexdigest(), "bytes": len(raw), "words": words,
            "cik": cik10(cik), "accession": accession, "document": filename,
            "html_stripped_word_count": True}
    with open(path + ".meta.json", "w", encoding="utf-8") as f:
        json.dump(side, f, indent=1)
    return {"accession": accession, "file": filename, "status": "ok", "path": rel,
            "bytes": len(raw), "words": words}


def xbrl_facts(company_dir, cik, lo, hi, tags):
    url = "https://data.sec.gov/api/xbrl/companyfacts/CIK%s.json" % cik10(cik)
    s, body, note = http_get(url)
    if body is None:
        return None, note
    j = json.loads(body)
    rows = []
    for taxonomy in ("us-gaap", "dei"):
        for tag, spec in (j.get("facts", {}) or {}).get(taxonomy, {}).items():
            if tags and tag not in tags:
                continue
            for unit, us in (spec.get("units", {}) or {}).items():
                for u in us:
                    fy = u.get("fy")
                    fp = u.get("fp") or ""
                    end = u.get("end", "")
                    if not end or end < lo or end > hi:
                        continue
                    rows.append({"tag": tag, "unit": unit, "start": u.get("start", ""), "end": end,
                                 "value": u.get("val"), "fy": fy, "fp": fp, "form": u.get("form", ""),
                                 "fyEnd": u.get("fyEnd", ""), "frame": u.get("frame", ""),
                                 "accn": u.get("accn", "")})
    rows.sort(key=lambda r: (r["tag"], r["end"], r["start"]))
    d = os.path.join(company_dir, "sources", "financials")
    os.makedirs(d, exist_ok=True)
    p = os.path.join(d, "xbrl_early_series.csv")
    if rows:
        with open(p, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)
    return len(rows), p


KEY_TAGS = {"Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax",
            "RevenueFromContractWithCustomerIncludingAssessedTax", "SalesRevenueNet",
            "NetIncomeLoss", "ProfitLoss", "Assets", "StockholdersEquity",
            "Liabilities", "LongTermDebt", "CommonStockSharesOutstanding",
            "WeightedAverageNumberOfDilutedSharesOutstanding", "OperatingIncomeLoss",
            "ResearchAndDevelopmentExpense", "SellingAndGeneralExpense",
            "GrossProfit", "EntityCommonStockSharesOutstanding", "OffBalanceSheetArrangements"}


def resolve_ticker(ticker):
    s, body, note = http_get("https://www.sec.gov/files/company_tickers.json")
    if body is None:
        raise SystemExit("ticker map failed: %s" % note)
    j = json.loads(body)
    t = ticker.upper()
    for v in j.values():
        if (v.get("ticker") or "").upper() == t:
            return v.get("cik_str"), v.get("title")
    return None, None


def pick_auto(rows, lo, hi, max_docs):
    wanted = []
    by_form = {}
    for r in sorted([_norm(x) for x in rows], key=lambda r: r["filingDate"] or "9999"):
        d = r["filingDate"]
        if not d or not (lo <= d <= hi) or not r["accession"] or not r["primaryDocument"]:
            continue
        fam = re.sub(r"[\d/]+$", "", r["form"]).strip()
        if r["form"] not in EARLY_FORMS and fam not in EARLY_FORMS:
            continue
        # every amendment of an S-1 is kept: version differences are findings, not duplicates
        key = r["form"] if fam in ("S-1", "S-4", "10-K") else r["form"].split("/")[0] + ":" + r["primaryDocument"][:12]
        if key in by_form and r["form"] not in ("S-1/A", "10-K/A", "S-4/A", "S-1", "10-K", "10-K405"):
            continue
        by_form[key] = r
        wanted.append(r)
        if len(wanted) >= max_docs:
            break
    return wanted


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("index", "facts", "grab", "auto"):
        p = sub.add_parser(name)
        p.add_argument("--cik")
        p.add_argument("--company-dir")
        p.add_argument("--ticker")
        p.add_argument("--from", dest="lo", default="1900-01-01")
        p.add_argument("--to", dest="hi", default="2030-12-31")
        p.add_argument("--accession")
        p.add_argument("--file")
        p.add_argument("--max-docs", type=int, default=40)
    p = sub.add_parser("resolve")
    p.add_argument("--ticker", required=True)
    a = ap.parse_args()

    if a.cmd == "resolve":
        cik, title = resolve_ticker(a.ticker)
        print(json.dumps({"ticker": a.ticker.upper(), "cik": cik, "name": title}))
        return 0 if cik else 2

    if not a.cik and a.ticker:
        a.cik, _ = resolve_ticker(a.ticker)
    if not a.cik:
        raise SystemExit("need --cik or --ticker")
    if not a.company_dir:
        raise SystemExit("need --company-dir")

    rc = 0
    if a.cmd in ("index", "auto"):
        name, tick, rows = submissions_index(a.cik)
        n, earliest = write_index(a.company_dir, a.cik, name, tick, rows)
        print("index: %d filings from %s (%s); earliest forms: %s"
              % (n, name, tick, ", ".join(sorted(earliest)[:14])))
        if any("UNANSWERED" in str(r.get("status", "")) for r in rows):
            rc = 1
    if a.cmd == "facts":
        cnt, path = xbrl_facts(a.company_dir, a.cik, a.lo, a.hi, KEY_TAGS)
        print("facts: %s" % ("wrote %d rows -> %s" % (cnt, path) if cnt else path))
        rc = 1 if cnt is None else rc
    if a.cmd == "grab":
        print(json.dumps(grab(a.company_dir, a.cik, a.accession, a.file or "index-headers.txt")))
    if a.cmd == "auto":
        _, _, rows = submissions_index(a.cik)
        picked = pick_auto(rows, a.lo, a.hi, a.max_docs)
        manifest, skipped = [], []
        for r in picked:
            items, note = doc_listing(a.cik, r["accession"])
            docs = [i["name"] for i in (items or [])
                    if i["name"].lower().endswith((".txt", ".htm", ".html"))][:6]
            if not docs:
                docs = [r["primaryDocument"]]
            for dn in docs:
                res = grab(a.company_dir, a.cik, r["accession"], dn)
                (manifest if res["status"] == "ok" else skipped).append(res)
            time.sleep(POLITE_SECONDS)
        d = os.path.join(a.company_dir, "sources", "sec")
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "_MANIFEST.csv"), "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["accession", "file", "path", "bytes", "words", "status"],
                               extrasaction="ignore")
            w.writeheader()
            w.writerows(manifest)
        print("auto: %d documents stored, %d skipped/unanswered" % (len(manifest), len(skipped)))
        for s in skipped[:12]:
            print("   UNANSWERED %s %s: %s" % (s["accession"], s["file"], s["status"]))
        rc = 1 if skipped else 0
    return rc


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main())
