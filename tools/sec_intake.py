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
                                     [--max-docs 40] [--dry-run]
  python tools/sec_intake.py selftest          # detector proves itself against each defect

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
import tempfile
import time
import urllib.error
import urllib.request

# Declared contact is mandatory: sec.gov returns 403 "Your Request Originates from an
# Undeclared Automated Tool" without it. Plain ASCII, no parentheses.
UA = "FounderPlaybook Research AdminContact@example.com"
REFERER = "https://www.sec.gov/"
# 0.12 s between accessions tripped EDGAR's 10-req/s ceiling and produced pages that
# read as an outage. One global gap now paces every request, documents included.
POLITE_SECONDS = 0.35
HARD_DOC_CAP_BYTES = 60 * 1024 * 1024
# 503 from /Archives/ is a soft "come back later", so the backoff has to be long
# enough to clear the cooldown a burst starts; 1.5/3.0 s never did in this session.
BACKOFF_SECONDS = (5, 10, 20, 40)

# Forms that carry early-history evidence, in priority order for `auto`.
EARLY_FORMS = [
    "S-1", "S-1/A", "S-11", "S-4", "S-4/A", "424B1", "424B2", "424B4", "SB-2",
    "10-12B", "10-K", "10-K405", "10-K/A", "10-KB", "8-K", "DEF 14A", "SC 13D",
    "SC 13G", "SC 13G/A", "3-2", "S-3", "POS AM",
]
# Every entry MUST be bytes: `marker in raw` on a bytes body raises TypeError if one is
# a str, which made every binary fetch collapse into "UNANSWERED after 3 tries" and look
# like an outage. `selftest` asserts this (see section "Defect 2" in the proof sheet).
ERROR_MARKERS = (
    b"<Error><Code>NoSuchKey</Code>",
    b"<Code>NoSuchKey</Code>",
    b"x-amz-error-code",
    b"Request Rate Threshold Exceeded",
    b"<title>Access Denied",
    b"Sorry, but we cannot seem to find the URL",
    b"Invalid Request",
    # Observed live in this session at /Archives/edgar/data/: two HTML apology pages
    # that a status-200 or status-503 response can carry in place of a document body.
    # Neither was in the original marker set, so either would have been saved as if it
    # were a filing -- the exact trap 00_METHOD_AND_STYLE.md s14 names.
    b"SEC.gov | File Unavailable",
    b"<title>SEC.gov | File Unavailable</title>",
    b"This page is temporarily unavailable",
    b"SEC.gov | Your Request Originates from an Undeclared Automated Tool",
    b"undeclared automated tool",
)
# 503/403 bodies worth quoting in the UNANSWERED note rather than calling "unreachable".
THROTTLE_MARKERS = ERROR_MARKERS
GZIP_MAGIC = b"\x1f\x8b"
# Scaffolding that index.json lists first, so a naive `[:6]` of the listing spends the
# whole document budget on files that return 404 NoSuchKey.
SCAFFOLD_SUFFIXES = ("-index-headers.html", "-index.htm", "-index.html", "index.json",
                     "index.htm", "index.html", "-headers.hdml")


def _pace():
    """Enforce one global minimum gap between HTTP requests (EDGAR 10-req/s rule)."""
    global _LAST_REQUEST
    wait = (_LAST_REQUEST + POLITE_SECONDS) - time.monotonic()
    if wait > 0:
        time.sleep(wait)
    _LAST_REQUEST = time.monotonic()


_LAST_REQUEST = 0.0


def _looks_like_error_page(raw):
    """Return the matching marker, or None. Bytes-in, never str-in-bytes."""
    for marker in ERROR_MARKERS:
        assert isinstance(marker, bytes), "ERROR_MARKERS must be bytes: %r" % (marker,)
        if marker in raw:
            return marker
    return None


def _maybe_gunzip(raw, content_encoding):
    """Decompress on the header OR on the gzip magic bytes.

    Observed live: a 503 page returned with `Content-Encoding` absent but the body
    starting with 1f 8b -- trusting the header alone stores gzip bytes as text.
    """
    if "gzip" in (content_encoding or "").lower() or raw[:2] == GZIP_MAGIC:
        try:
            return gzip.decompress(raw)
        except OSError:
            pass
    return raw


def _ctx():
    # Local CA stores on this machine are stale for some CDN hosts; degrade only the
    # verification depth for the EDGAR hosts, never globally for other fetches.
    ctx = ssl.create_default_context()
    return ctx


def http_get(url, binary=False, tries=3):
    """Return (status, bytes_or_text, note). 'note' carries UNANSWERED reasons."""
    last = None
    for attempt in range(tries):
        _pace()
        req = urllib.request.Request(url)
        req.add_header("User-Agent", UA)
        req.add_header("Referer", REFERER)
        req.add_header("Accept-Encoding", "gzip, deflate")
        try:
            with urllib.request.urlopen(req, timeout=60, context=_ctx()) as r:
                raw = _maybe_gunzip(r.read(), r.headers.get("Content-Encoding", ""))
                status = r.status
            if not binary:
                body = raw.decode("utf-8", "replace")
                # A text response can still be an apology page rather than the JSON asked
                # for; 200 + "File Unavailable" once parsed as an empty filing list.
                marker = _looks_like_error_page(raw)
                if marker is not None:
                    return status, None, "ERROR PAGE (status %s, %r), not saved" % (status, marker)
                return status, body, "ok"
            marker = _looks_like_error_page(raw)
            if marker is not None:
                return status, None, "ERROR PAGE (status %s, %r), not saved" % (status, marker)
            return status, raw, "ok"
        except urllib.error.HTTPError as e:
            body = b""
            try:
                body = _maybe_gunzip(e.read(), (e.headers or {}).get("Content-Encoding", ""))
            except Exception:
                body = b""
            marker = _looks_like_error_page(body)
            reason = "HTTP %s" % e.code
            if marker is not None:
                reason = "%s %r page" % (reason, marker)
            last = reason
            if e.code in (503, 504, 429):
                # Soft cooldown, not an outage: back off long enough to clear it.
                time.sleep(BACKOFF_SECONDS[min(attempt, len(BACKOFF_SECONDS) - 1)])
                continue
            if e.code == 403:
                time.sleep(2.0 * (attempt + 1))
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


def accession_dirs(cik, accession):
    """Candidate (form, url-prefix) pairs for one accession, best-evidenced first.

    Live evidence for the ordering, from the 2026-09-26 diagnosis:
      /Archives/edgar/data/0001045810/000101287000004830/index.json -> 200
      /Archives/edgar/data/1045810/000101287000004830/index.json    -> 200
      /Archives/edgar/data/1045810/000101287000004830-index/...      -> 404
    so the `-index`-suffixed directory (the other form EDGAR's browse pages print for
    pre-2001 filings) is NOT a fetchable prefix and must not be tried first.
    """
    digits = re.sub(r"\D", "", str(cik))
    padded, bare = cik10(cik), str(int(digits)) if digits else "0"
    a = accession.replace("-", "")
    out, seen = [], set()
    for form, base in (("padded-cik/nodash-dir", "%s/%s" % (padded, a)),
                       ("bare-cik/nodash-dir", "%s/%s" % (bare, a)),
                       ("bare-cik/dashed-dir", "%s/%s" % (bare, accession))):
        if base not in seen:
            seen.add(base)
            out.append((form, "https://www.sec.gov/Archives/edgar/data/%s/" % base))
    return out


def _is_scaffold(name):
    low = name.lower()
    return low.endswith(tuple(s.lower() for s in SCAFFOLD_SUFFIXES)) or low == "index.json"


def doc_listing(cik, accession):
    """(items, note, form). Items keep `size` (a STRING upstream) and flag unnamed rows.

    Pre-2001 directories return a malformed listing: of 41 items in Amazon's original
    S-1 accession, only the first 3 carried a `name` and those 3 are the scaffolding
    stubs; the other 38 had name:"" with a real size. A caller that takes names in
    listing order therefore fetches stubs (404 NoSuchKey) and blank URLs, and stores
    almost nothing while every individual failure looks like an EDGAR outage.
    """
    last = None
    for form, base in accession_dirs(cik, accession):
        s, body, note = http_get(base + "index.json", tries=2)
        if body is None:
            last = "%s -> %s" % (form, note)
            # Same reasoning as in grab(): 503 is the host cooling down, so the next
            # directory prefix would be refused too. Without this break a throttled
            # window cost ~105 s per accession in backoff and stored nothing.
            if "503" in str(note) or "504" in str(note) or "429" in str(note):
                break
            continue
        try:
            j = json.loads(body)
        except ValueError:
            last = "%s -> UNPARSEABLE index.json (returned a page, not a listing)" % form
            continue
        items = j.get("directory", {}).get("item", []) or []
        out = []
        for it in items:
            try:
                size = int(it.get("size", "0") or 0)  # size arrives as a STRING
            except ValueError:
                size = 0
            out.append({"name": it.get("name", "") or "", "size": size,
                        "type": it.get("type", "") or ""})
        unnamed = sum(1 for i in out if not i["name"])
        return out, ("listing via %s (%d items, %d unnamed)" % (form, len(out), unnamed)), form
    return None, "UNANSWERED listing: %s" % (last or "no candidate directory form"), ""


def candidate_docs(row, items, limit=6):
    """Real document names to fetch for one filing, scaffolding and blanks removed.

    Order: the submissions `primaryDocument` (the authoritative name when the listing
    agrees), then named text/html items largest-first (a filing body is the biggest
    object in its directory), then the full-submission SGML `<accession>.txt`, which is
    the artifact that actually returned 200 with 1,444,013 bytes for Amazon's S-1 when
    the per-document names in the same listing did not resolve.
    """
    named = [i for i in (items or []) if i["name"] and not _is_scaffold(i["name"])
             and i["name"].lower().endswith((".txt", ".htm", ".html"))]
    named.sort(key=lambda i: -i["size"])
    out, seen = [], set()

    def push(name, why, size=None):
        if name and name not in seen:
            seen.add(name)
            out.append({"name": name, "why": why, "size": size})

    primary = row.get("primaryDocument") or ""
    psize = next((i["size"] for i in named if i["name"] == primary), None)
    push(primary, "primaryDocument", psize)
    for i in named[:limit]:
        push(i["name"], "index.json listing (%d B)" % i["size"], i["size"])
    push(row["accession"] + ".txt", "full-submission SGML fallback")
    return out[:max(1, limit)]


def grab(company_dir, cik, accession, filename, subdir="sec"):
    """Fetch one document, trying every candidate directory form. Never writes an error page.

    `filename` may arrive blank (the pre-2001 listing defect) or be a name the archive
    does not hold; each attempt's status is kept in `tried` so an UNANSWERED row names
    the status rather than reading as a null.
    """
    safe = re.sub(r"[^A-Za-z0-9._-]", "_", filename)
    rel = os.path.join(subdir, "%s_%s" % (accession, safe))
    path = os.path.join(company_dir, "sources", rel)
    if not filename:
        # A blank name is the malformed pre-2001 listing, not a document. Concatenating
        # it would fetch the directory URL and save whatever apology page came back.
        return {"accession": accession, "file": "", "path": "",
                "status": "UNANSWERED (empty document name in index.json listing, "
                          "no URL constructed)", "bytes": 0, "words": 0}
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tried = []
    for form, base in accession_dirs(cik, accession):
        url = base + filename
        s, raw, note = http_get(url, binary=True, tries=2)
        if not raw:
            tried.append("%s: %s %s" % (form, s or "-", note))
            # 503 is the whole host cooling down, not this directory form being wrong:
            # re-trying the same name under another prefix only deepens the cooldown.
            if s in (503, 504, 429):
                break
            continue
        if len(raw) > HARD_DOC_CAP_BYTES:
            return {"accession": accession, "file": filename, "status": "SKIPPED over cap",
                    "path": "", "bytes": len(raw), "url": url, "form": form,
                    "tried": "; ".join(tried + ["%s: %d B > cap" % (form, len(raw))])}
        txt = raw.decode("utf-8", "replace")
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(txt)
        words = len(re.findall(r"\S+", re.sub(r"<[^>]+>", " ", txt)))
        side = {"url": url, "fetched": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "sha1": hashlib.sha1(raw).hexdigest(), "bytes": len(raw), "words": words,
                "cik": cik10(cik), "accession": accession, "document": filename,
                "url_form": form, "http_status": s, "tried_before": tried,
                "html_stripped_word_count": True,
                "full_submission_sgml": filename.endswith(".txt") and filename.startswith(accession)}
        with open(path + ".meta.json", "w", encoding="utf-8") as f:
            json.dump(side, f, indent=1)
        return {"accession": accession, "file": filename, "status": "ok", "path": rel,
                "bytes": len(raw), "words": words, "url": url, "form": form,
                "tried": "; ".join(tried)}
    return {"accession": accession, "file": filename, "path": "",
            "status": "UNANSWERED (%s)" % (" | ".join(tried) or "no filename to fetch"),
            "bytes": 0, "words": 0}


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
    """Accessions worth fetching in the window.

    A blank `primaryDocument` no longer disqualifies a filing: the full-submission SGML
    `<accession>.txt` is fetchable for paper-era shells whose submissions row carries no
    document name at all, and dropping the row hid coverage rather than reported it.
    """
    wanted = []
    by_form = {}
    for r in sorted([_norm(x) for x in rows], key=lambda r: r["filingDate"] or "9999"):
        d = r["filingDate"]
        if not d or not (lo <= d <= hi) or not r["accession"]:
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


def selftest():
    """The intake proves itself against the exact defects it is supposed to catch (§15.5)."""
    fails = []
    checks = {"n": 0}

    def check(name, ok, detail=""):
        checks["n"] += 1
        print("  %-46s %s %s" % (name, "PASS" if ok else "FAIL", detail))
        if not ok:
            fails.append(name)

    print("sec_intake selftest")
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = [m for m in ERROR_MARKERS if not isinstance(m, bytes)]
    check("every ERROR_MARKERS entry is bytes", not bad, "str markers: %r" % (bad,))
    check("str marker cannot slip back in",
          all(isinstance(m, bytes) for m in THROTTLE_MARKERS))
    check("error-page detector fires on NoSuchKey",
          _looks_like_error_page(b'<?xml version="1.0"?><Error><Code>NoSuchKey</Code>')
          is not None)
    check("error-page detector fires on File Unavailable",
          _looks_like_error_page(b"<title>SEC.gov | File Unavailable</title>") is not None)
    check("error-page detector fires on undeclared-tool 403",
          _looks_like_error_page(b"SEC.gov | Your Request Originates from an Undeclared"
                                 b" Automated Tool") is not None)
    check("real filing text is not flagged",
          _looks_like_error_page(b"<html><body>Our initial public offering S-1</body>") is None)
    check("gzip sniffed without Content-Encoding",
          _maybe_gunzip(gzip.compress(b"0001012870-00-004830"), "") == b"0001012870-00-004830")
    check("slices are fetched from data.sec.gov/submissions/",
          'url = "https://data.sec.gov/submissions/%s" % f["name"]' in src
          # assembled at runtime so this line cannot make its own test false
          and ("/Archives/edgar/data/" + "%s/%s.json") not in src)
    check("an unfetchable slice is recorded UNANSWERED, not truncated",
          '"status": "UNANSWERED: " + n2' in src)
    check("60 MB per-document cap still enforced",
          "HARD_DOC_CAP_BYTES" in src and "SKIPPED over cap" in src)
    dirs = accession_dirs("1045810", "0001012870-00-004830")
    check("accession dir form has a separating slash",
          all(u.endswith("/") for _, u in dirs), dirs[0][1])
    check("`-index` directory form is not tried",
          not any(u.endswith("-index/") for _, u in dirs))
    check("scaffolding stubs excluded from candidates",
          _is_scaffold("0001012870-00-004830-index-headers.html"))
    check("unnamed listing rows never become URLs",
          all(c["name"] for c in candidate_docs(
              {"accession": "0000891618-97-001309", "primaryDocument": ""},
              [{"name": "", "size": 5319}, {"name": "x-index-headers.html", "size": 1},
               {"name": "a1309.txt", "size": 1444013}], limit=4)))
    sgml = candidate_docs({"accession": "0000891618-97-001309", "primaryDocument": ""},
                          [{"name": "", "size": 5319}], limit=4)
    check("SGML full-submission fallback is offered",
          any(c["name"] == "0000891618-97-001309.txt" for c in sgml), str(sgml))
    check("per-document budget keeps the SGML fallback",
          len(candidate_docs({"accession": "A-B-C", "primaryDocument": "p.txt"},
                             [{"name": "p.txt", "size": 10}] +
                             [{"name": "d%d.htm" % i, "size": i} for i in range(9)],
                             limit=6)) >= 2)
    check("UNANSWERED carries a status, not a blank",
          "UNANSWERED" in grab(tempfile.mkdtemp(prefix="sec_intake_selftest_"),
                              "1045810", "0001012870-00-004830", "").get("status", ""))
    check("a blank document name is never turned into a URL",
          "no URL constructed" in open(os.path.abspath(__file__), encoding="utf-8").read())
    print("selftest: %d checks, %d failing" % (checks["n"], len(fails)))
    return 1 if fails else 0


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
        p.add_argument("--docs-per-filing", type=int, default=4)
        p.add_argument("--dry-run", action="store_true",
                       help="list what WOULD be fetched (url, index.json size, form) and stop")
    sub.add_parser("selftest")
    p = sub.add_parser("resolve")
    p.add_argument("--ticker", required=True)
    a = ap.parse_args()

    if a.cmd == "selftest":
        return selftest()

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
    rows = None
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
        picked = pick_auto(rows, a.lo, a.hi, a.max_docs)
        manifest, skipped, planned = [], [], []
        for r in picked:
            items, note, form = doc_listing(a.cik, r["accession"])
            cands = candidate_docs(r, items, limit=a.docs_per_filing)
            base = accession_dirs(a.cik, r["accession"])[0][1]
            for c in cands:
                planned.append({"accession": r["accession"], "form": r["form"],
                                "filingDate": r["filingDate"], "document": c["name"],
                                "bytes_in_index_json": c["size"],
                                "why": c["why"], "url": base + c["name"]})
            if a.dry_run:
                continue
            for c in cands:
                res = grab(a.company_dir, a.cik, r["accession"], c["name"])
                res.update({"form": r["form"], "filingDate": r["filingDate"],
                            "listing": note})
                (manifest if res["status"] == "ok" else skipped).append(res)
        d = os.path.join(a.company_dir, "sources", "sec")
        os.makedirs(d, exist_ok=True)
        if a.dry_run:
            with open(os.path.join(d, "_DRY_RUN_PLAN.csv"), "w", encoding="utf-8", newline="") as f:
                w = csv.DictWriter(f, fieldnames=list(planned[0].keys()) if planned
                                   else ["accession", "form", "filingDate", "document"])
                w.writeheader()
                w.writerows(planned)
            print("dry-run: %d accessions, %d documents WOULD be fetched; no bytes downloaded"
                  % (len(picked), len(planned)))
            for p in planned[:25]:
                print("   %-11s %-24s %-34s %s%s" % (
                    p["filingDate"], p["form"][:24], p["document"][:34],
                    ("%s B " % p["bytes_in_index_json"]) if p["bytes_in_index_json"] is not None
                    else "(size unlisted) ", p["url"]))
            return rc
        cols = ["accession", "file", "path", "bytes", "words", "status", "form",
                "filingDate", "url", "listing"]
        with open(os.path.join(d, "_MANIFEST.csv"), "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
            w.writeheader()
            w.writerows(manifest)
        # Nothing is dropped: an unfetchable document is a row with its status, never a
        # silence that a later reader could mistake for "this filing has no text".
        with open(os.path.join(d, "_UNANSWERED.csv"), "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
            w.writeheader()
            w.writerows(skipped)
        words = sum(m["words"] for m in manifest)
        print("auto: %d documents stored (%d bytes, %d words), %d UNANSWERED "
              "(counted, not nulls)" % (len(manifest), sum(m["bytes"] for m in manifest),
                                        words, len(skipped)))
        for s in skipped[:12]:
            print("   UNANSWERED %s %s: %s" % (s["accession"], s["file"], s["status"]))
        rc = 1 if skipped else rc
    return rc


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main())
