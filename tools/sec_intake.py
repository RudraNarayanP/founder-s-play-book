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
    formers = [f.get("name") if isinstance(f, dict) else f
               for f in (j.get("formerNames") or [])]
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
    return name, (ticks[0] if ticks else ""), rows, ticks, [f for f in formers if f]


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


NAME_STOP_WORDS = {"inc", "incorporated", "corp", "corporation", "co", "company", "ltd",
                   "llc", "plc", "lp", "l.p", "plc", "the", "and", "group", "holdings",
                   "holding", "sa", "nv", "bv", "gmbh", "ag", "corp.", "new", "delaware"}


def slug_tokens(company_dir):
    """`company_041_dell` -> ['dell']; `company_016_nvidia` -> ['nvidia']
    """
    base = os.path.basename(os.path.normpath(str(company_dir))).lower()
    base = re.sub(r"^company[_\-\.]?\d*[_\-\.]", "", base)
    return [t for t in re.findall(r"[a-z0-9]+", base)
            if t and t not in NAME_STOP_WORDS and not t.isdigit()]


def _norm_name(text):
    return set(re.findall(r"[a-z0-9]+", (text or "").lower())) - NAME_STOP_WORDS


def registrant_guard(company_dir, cik, name, tickers, former_names):
    """(ok, verdict, reasons) -- defect D-5.

    Two independent signals, because neither alone catches the incident that produced
    this rule. Resolving the 2013 Dell merger shell (CIK 1571996, registrant name
    "Dell Inc.") against Dell's directory (legacy registrant 826083) passes any
    name/token test you care to write -- the shell really is called Dell. What gives it
    away is that the *directory already holds an index for a different CIK*. So:

      A. identity plausibility: a slug token must occur as a whole word in the
         registrant name, a former name, or a ticker (no substring matching -- "dell"
         inside "Dellor" would pass, and a wrong CIK whose name shares three letters
         would too);
      B. no-clobber: if `sources/_index` already carries artefacts for another CIK, a
         second CIK may not overwrite them, however well its name reads.

    Failing either one sends every artefact to `sources/_index/quarantine/CIK.../` and
    says so loudly rather than writing the wrong registrant's history into the right
    company's directory.
    """
    reasons = []
    slug = slug_tokens(company_dir)
    toks = _norm_name(name)
    for f in (former_names or [])[:40]:
        toks |= _norm_name(f if isinstance(f, str) else (f or {}).get("name"))
    tk = {str(t).lower() for t in (tickers or [])}
    if not slug:
        return True, "unchecked", ["directory slug yields no name token to test"]
    hits = [t for t in slug if t in toks or t in tk]
    if not hits:
        reasons.append("no slug token %s appears in registrant name %r / tickers %s / former names"
                       % (slug, name, sorted(tk)))
    own = cik10(cik)
    d = os.path.join(company_dir, "sources", "_index")
    if os.path.isdir(d):
        for fn in sorted(os.listdir(d)):
            m = re.match(r"^submissions_CIK(\d{10})\.csv$", fn) or \
                re.match(r"^submissions_CIK(\d{10})\.json$", fn)
            if m and m.group(1) != own:
                reasons.append("directory already holds an index for CIK %s; refusing to let "
                               "CIK %s share these artefacts" % (m.group(1), own))
                break
    legacy = os.path.join(d, "submissions.json")
    if os.path.exists(legacy) and not reasons:
        try:
            prev = cik10(json.load(open(legacy, encoding="utf-8")).get("cik") or 0)
            if prev.strip("0") and prev != own:
                reasons.append("legacy submissions.json belongs to CIK %s, not %s" % (prev, own))
        except (ValueError, OSError, re.error):
            pass
    if reasons:
        return False, "quarantine", reasons
    return True, "ok", ["slug token(s) %s match registrant %r (CIK %s)" % (hits, name, own)]


def _csv_text(fieldnames, rows):
    """Deterministic CSV text (LF endings) so a byte compare is a real compare."""
    buf = io.StringIO(newline="")
    w = csv.DictWriter(buf, fieldnames=list(fieldnames), extrasaction="ignore",
                       lineterminator="\n")
    w.writeheader()
    for r in rows:
        w.writerow({k: r.get(k, "") for k in fieldnames})
    return buf.getvalue()


def write_index(company_dir, cik, name, ticker, rows, tickers=None, former_names=None):
    """Index artefacts keyed by CIK, never by directory alone (D-5), with every row
    accounted for (D-2): rows that could not be acted on are written with a reason
    instead of being filtered out of existence."""
    guard_ok, verdict, reasons = registrant_guard(company_dir, cik, name,
                                                 tickers or ([ticker] if ticker else []),
                                                 former_names)
    c = cik10(cik)
    base = os.path.join(company_dir, "sources", "_index")
    d = base if guard_ok else os.path.join(base, "quarantine", "CIK%s" % c)
    os.makedirs(d, exist_ok=True)
    norm = [_norm(r) for r in rows if (r.get("accession") or r.get("accessionNumber"))]
    dropped = [{"source": r.get("source", ""), "status": r.get("status", "") or "no accession",
                "form": r.get("form", ""), "filingDate": r.get("filingDate", "")}
               for r in rows if not (r.get("accession") or r.get("accessionNumber"))]
    no_doc = [r for r in norm if not r["primaryDocument"]]
    norm.sort(key=lambda r: (r["filingDate"] or "9999", r["form"]))
    meta = {"cik": c, "requested_cik": str(cik), "registrant": name, "ticker": ticker,
            "tickers": list(tickers or ([ticker] if ticker else [])),
            "former_names": list(former_names or [])[:20],
            "company_dir": os.path.basename(os.path.normpath(str(company_dir))),
            "guard": verdict, "guard_reasons": reasons,
            "built": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "count": len(norm), "rows_dropped_no_accession": len(dropped),
            "rows_without_primaryDocument": len(no_doc)}
    payload = dict(meta, filings=norm)
    csv_text = _csv_text(["filingDate", "form", "accession", "reportDate", "primaryDocument",
                          "source"], norm)
    paths = {}
    paths["json"] = os.path.join(d, "submissions_CIK%s.json" % c)
    _write_verified(paths["json"], json.dumps(payload, indent=1))
    paths["csv"] = os.path.join(d, "submissions_CIK%s.csv" % c)
    meta["csv_sha1"] = hashlib.sha1(csv_text.encode("utf-8")).hexdigest()
    meta["csv_bytes"] = len(csv_text.encode("utf-8"))
    _write_verified(paths["csv"], csv_text)
    earliest = {}
    for r in norm:
        if r["form"] and r["form"] not in earliest and r["filingDate"]:
            earliest[r["form"]] = r
    lines = ["# SEC submissions index -- %s (CIK %s, %s)" % (name, c, ticker), "",
             "Built by `tools/sec_intake.py` at %s. **Registrant name for this index: `%s` "
             "(CIK %s)** -- artefacts are keyed by CIK, so a wrong `--cik` cannot overwrite "
             "another registrant's index." % (time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime()),
                                              name, c),
             "%d filings enumerated; %d submissions rows dropped for carrying no accession; "
             "%d rows carry no `primaryDocument` (paper-era shells -- fetchable as "
             "`<accession>.txt`)." % (len(norm), len(dropped), len(no_doc)), "",
             "Registrant guard: **%s** -- %s" % (verdict, "; ".join(reasons)), "",
             "**This file is the source of truth for what exists.** Do not re-search EDGAR for",
             "coverage; grep `submissions.csv` and report a form as absent only from this list.",
             "",
             "## Earliest filing per form", "",
             "| form | filed | accession | primary document |", "|---|---|---|---|"]
    for form in sorted(earliest, key=lambda x: earliest[x]["filingDate"]):
        r = earliest[form]
        lines.append("| %s | %s | %s | %s |" % (form, r["filingDate"], r["accession"],
                                                r["primaryDocument"]))
    lines += ["", "## UNANSWERED slices (never report these as absent)", ""]
    unanswered = [r for r in rows if "UNANSWERED" in str(r.get("status", ""))]
    lines.append("(none)" if not unanswered else "")
    for r in unanswered:
        lines.append("- `%s` -- %s" % (r.get("source"), r.get("status")))
    if dropped:
        lines += ["", "## Rows dropped for carrying no accession (counted, not discarded)", ""]
        for r in dropped[:50]:
            lines.append("- source `%s` -- %s" % (r.get("source"), r.get("status")))
        if len(dropped) > 50:
            lines.append("- ... %d more in `dropped_rows_CIK%s.csv`" % (len(dropped) - 50, c))
    paths["md"] = os.path.join(d, "_INDEX_CIK%s.md" % c)
    _write_verified(paths["md"], "\n".join(lines) + "\n")
    if dropped:
        _write_verified(os.path.join(d, "dropped_rows_CIK%s.csv" % c),
                        _csv_text(["source", "status", "form", "filingDate"], dropped))
    _write_verified(os.path.join(d, "_registrant_CIK%s.json" % c), json.dumps(meta, indent=1))
    # Back-compat copy for the rest of the corpus, which greps `submissions.csv`. Written
    # only under a passing guard, and never over another registrant's copy.
    legacy_written, legacy_note = False, ""
    if guard_ok:
        legacy = os.path.join(base, "submissions.json")
        if os.path.exists(legacy):
            try:
                prev = (json.load(open(legacy, encoding="utf-8")).get("cik") or "").strip()
                if prev and cik10(prev) != c:
                    legacy_note = ("legacy submissions.json is CIK %s -- left untouched" % cik10(prev))
            except (ValueError, OSError):
                legacy_note = "legacy submissions.json unreadable -- left untouched"
        if not legacy_note:
            _write_verified(legacy, json.dumps(payload, indent=1))
            _write_verified(os.path.join(base, "submissions.csv"), csv_text)
            _write_verified(os.path.join(base, "_INDEX.md"), "\n".join(lines) + "\n")
            legacy_written = True
    meta.update({"paths": paths, "legacy_copy_written": legacy_written,
                 "legacy_note": legacy_note})
    _write_verified(os.path.join(d, "_registrant_CIK%s.json" % c), json.dumps(meta, indent=1))
    meta["rows"] = norm
    return len(norm), earliest, meta


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


def grab(company_dir, cik, accession, filename, subdir="sec", registrant=""):
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
                "cik": cik10(cik), "registrant": registrant or "(not resolved this run)",
                "accession": accession, "document": filename,
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
    """XBRL money series for one window: ALWAYS bytes on disk, or a named NULL.

    Root cause of defect D-1, verified live on 2026-09-26 (see
    03_quality_control/intake_hardening_2.md): `companyfacts` carries no observation
    before ~2007 for these registrants (MSFT min_end 2007-06-30, TSLA 2008-12-31,
    COST 2007-09-02), so a 1994-1999 window yields zero rows -- and the old function
    returned `(0, path)` while `main` printed the path and exited 0 without creating
    the file. It also could not tell the two opposite causes apart:
      (a) nothing in the window at all  -> the window predates XBRL; widen nothing,
          go read the filings;
      (b) facts in the window, none under the allow-list -> KEY_TAGS is too narrow
          for this company, and the run is fixable with --tags/--all-tags.
    Confusing (b) for (a) silently discards evidence; confusing (a) for (b) sends an
    agent chasing a tag list. So both counts are computed and both are printed.
    """
    out = {"status": "NULL", "cik": cik10(cik), "registrant": "", "window": "%s..%s" % (lo, hi),
           "rows": 0, "path": "", "bytes": 0, "report": "", "reason": "", "corpus": {}}
    d = os.path.join(company_dir, "sources", "financials")
    cols = ["tag", "unit", "start", "end", "value", "fy", "fp", "form", "fyEnd", "frame", "accn"]
    url = "https://data.sec.gov/api/xbrl/companyfacts/CIK%s.json" % cik10(cik)
    s, body, note = http_get(url)
    if body is None:
        out["status"] = "UNANSWERED"
        out["reason"] = ("companyfacts fetch failed (HTTP %s): %s -- the window was NOT tested, "
                         "which is not the same as empty" % (s or "-", note))
        out["report"] = _write_facts_report(d, out, cols, [])
        return out
    try:
        j = json.loads(body)
    except ValueError:
        out["status"] = "UNANSWERED"
        out["reason"] = "companyfacts JSON unparseable (status %s): a page came back, not data" % s
        out["report"] = _write_facts_report(d, out, cols, [])
        return out
    out["registrant"] = j.get("entityName") or ""
    facts = j.get("facts", {}) or {}
    rows, ends, tag_total, in_window = [], [], 0, 0
    win_tags = {}
    for taxonomy in ("us-gaap", "dei"):
        for tag, spec in (facts.get(taxonomy) or {}).items():
            tag_total += 1
            for unit, us in (spec.get("units", {}) or {}).items():
                for u in us or []:
                    end = u.get("end", "") or ""
                    if end:
                        ends.append(end)
                    if not end or end < lo or end > hi:
                        continue
                    in_window += 1
                    win_tags[tag] = win_tags.get(tag, 0) + 1
                    rows.append({"tag": tag, "unit": unit, "start": u.get("start", ""),
                                 "end": end, "value": u.get("val"), "fy": u.get("fy"),
                                 "fp": u.get("fp") or "", "form": u.get("form", ""),
                                 "fyEnd": u.get("fyEnd", ""), "frame": u.get("frame", ""),
                                 "accn": u.get("accn", "")})
    top = sorted(win_tags.items(), key=lambda kv: -kv[1])[:12]
    out["corpus"] = {"tags_present": tag_total, "observations": len(ends),
                     "min_end": min(ends) if ends else "", "max_end": max(ends) if ends else "",
                     "in_window_any_tag": in_window, "tags_in_window": len(win_tags)}
    kept = [r for r in rows if not tags or r["tag"] in tags] if tags else rows
    rows_sorted = sorted(kept or rows, key=lambda r: (r["tag"], r["end"], r["start"]))
    p = os.path.join(d, "xbrl_early_series.csv")

    if kept:
        buf = io.StringIO(newline="")
        w = csv.DictWriter(buf, fieldnames=cols, lineterminator="\n")
        w.writeheader()
        w.writerows(rows_sorted)
        try:
            out["bytes"] = _write_verified(p, buf.getvalue())
        except OSError as e:
            out["status"] = "UNANSWERED"
            out["reason"] = "CSV writer failed at %s: %s" % (p, e)
            out["report"] = _write_facts_report(d, out, cols, rows_sorted)
            return out
        out.update({"status": "OK", "rows": len(rows_sorted), "path": p})
        _write_verified(p + ".meta.json", json.dumps(
            {"cik": out["cik"], "registrant": out["registrant"], "window": out["window"],
             "rows": len(rows_sorted), "bytes": out["bytes"], "allow_list_applied": bool(tags),
             "corpus": out["corpus"],
             "built": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}, indent=1))
        if len(kept) < in_window:
            out["note"] = ("%d of %d in-window observations kept under the allow-list; "
                           "%d tags present in the window were not asked for"
                           % (len(kept), in_window, len(win_tags)))
        return out

    # Zero kept rows: name the reason, write it down, and keep the untagged evidence.
    if in_window:
        out["reason"] = ("ALLOW-LIST: %d observations fall in %s..%s across %d tags, but none is "
                         "in the %d-tag KEY_TAGS set. In-window tags by volume: %s. Re-run with "
                         "--tags a,b,c or --all-tags; this is a fixable intake gap, not an absence."
                         % (in_window, lo, hi, len(win_tags), len(tags or ()),
                            ", ".join("%s(%d)" % (k, v) for k, v in top)))
        ub = io.StringIO(newline="")
        uw = csv.DictWriter(ub, fieldnames=cols, lineterminator="\n")
        uw.writeheader()
        uw.writerows(sorted(rows, key=lambda r: (r["tag"], r["end"], r["start"]))[:20000])
        up = os.path.join(d, "xbrl_early_series_CIK%s_untagged.csv" % out["cik"])
        try:
            out["untagged_bytes"] = _write_verified(up, ub.getvalue())
            out["untagged_path"] = up
            out["untagged_rows"] = min(in_window, 20000)
        except OSError as e:
            out["reason"] += " (untagged dump failed: %s)" % e
    else:
        out["reason"] = ("WINDOW: 0 of %s observations in this registrant's companyfacts fall in "
                         "%s..%s. Observed XBRL coverage runs %s..%s, and %d tags are present, so "
                         "the absence is EDGAR's XBRL start date (~2007 for this filer), not a "
                         "fetch failure and not the allow-list. Early-window money figures must "
                         "come from the filings themselves."
                         % ("{:,}".format(len(ends)), lo, hi, min(ends) if ends else "n/a",
                            max(ends) if ends else "n/a", tag_total))
    out["report"] = _write_facts_report(d, out, cols, [])
    return out


def _write_verified(path, text):
    """Write, then stat it. A function that returns success without producing bytes is
    the defect class this whole pass exists to remove (§15.5 applied to retrieval)."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    size = os.stat(path).st_size
    if size <= 0:
        raise OSError("wrote %s but the file is 0 bytes" % path)
    return size


def _write_facts_report(d, out, cols, rows):
    """The NULL/UNANSWERED artefact: keyed by CIK and window, so two runs cannot mute
    each other, and stale bytes are called out instead of being trusted."""
    name = "xbrl_early_series_CIK%s_%s_%s.NULL.md" % (out["cik"], out["window"].replace("..", "_"),
                                                      out["status"])
    p = os.path.join(d, name)
    stale = ""
    canon = os.path.join(d, "xbrl_early_series.csv")
    if os.path.exists(canon):
        st = os.stat(canon)
        prev = ""
        if os.path.exists(canon + ".meta.json"):
            try:
                meta = json.load(open(canon + ".meta.json", encoding="utf-8"))
                prev = " (built for CIK %s window %s, %s rows)" % (meta.get("cik"),
                                                                   meta.get("window"),
                                                                   meta.get("rows"))
            except (ValueError, OSError):
                prev = " (sidecar unreadable)"
        stale = ("\n> **STALE BYTES ON DISK**: `%s` exists (%d B, %s%s) and was **not** written by "
                 "this run. Do not read it as evidence for window %s.\n"
                 % (canon, st.st_size,
                    time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime(st.st_mtime)), prev,
                    out["window"]))
    lines = ["# XBRL facts: %s -- %s" % (out["status"], out["cik"]), "",
             "- registrant: `%s`" % (out["registrant"] or "(unknown)"),
             "- CIK: `%s`" % out["cik"],
             "- window requested: `%s`" % out["window"],
             "- rows written: %d" % out["rows"],
             "- reason named: %s" % (out["reason"] or "(none)"),
             "- corpus census: %s" % json.dumps(out["corpus"]),
             "- this run wrote NO data file; the canonical `xbrl_early_series.csv` was left "
             "untouched on purpose", ""]
    if out.get("untagged_path"):
        lines.append("- untagged in-window evidence kept at `%s` (%d rows, %d B)"
                     % (out["untagged_path"], out.get("untagged_rows", 0),
                        out.get("untagged_bytes", 0)))
    if stale:
        lines.append(stale)
    lines += ["", "A NULL here is a *named* absence, not a silent one: an empty result that",
              "reports success is what lets an absence get absorbed into the corpus.", ""]
    out["report_bytes"] = _write_verified(p, "\n".join(lines))
    return p



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


SELECTION_ORDER = (
    "1. filings whose filingDate falls in --from/--to, sorted filingDate ASCENDING "
    "(earliest evidence first); 2. one filing per form key -- S-1/S-4/10-K families keep "
    "every filing because version differences are findings, other forms keep the first "
    "per (base-form, primaryDocument[:12]); 3. inside a filing, documents in candidate "
    "order: the submissions primaryDocument, then named text/html items largest-first, "
    "then the full-submission SGML <accession>.txt; 4. --max-docs caps DOCUMENTS, so the "
    "stream built by 1-3 is cut at N and every slot past the cut is written to "
    "_SKIPPED.csv as 'SKIPPED beyond --max-docs N' -- never dropped."
)


def _form_family(form):
    return re.sub(r"[\d/]+$", "", form).strip()


def pick_filings(rows, lo, hi):
    """Filings worth fetching in the window, in SELECTION_ORDER. No document cap here.

    The cap used to be applied to THIS list (`if len(wanted) >= max_docs`), which is why
    D-4 read as "--max-docs is ignored": asking for 25 documents got 25 *filings* and up
    to 25 x --docs-per-filing documents, and nothing in the output said which.
    """
    wanted, by_form = [], {}
    for r in sorted([_norm(x) for x in rows], key=lambda r: r["filingDate"] or "9999"):
        d = r["filingDate"]
        if not d or not (lo <= d <= hi) or not r["accession"]:
            continue
        fam = _form_family(r["form"])
        if r["form"] not in EARLY_FORMS and fam not in EARLY_FORMS:
            continue
        key = (r["form"] if fam in ("S-1", "S-4", "10-K")
               else r["form"].split("/")[0] + ":" + r["primaryDocument"][:12])
        if key in by_form and r["form"] not in ("S-1/A", "10-K/A", "S-4/A", "S-1", "10-K",
                                                "10-K405"):
            continue
        by_form[key] = r
        wanted.append(r)
    return wanted


def nameless_row(accession, form, filing_date, item, listing_note, cik):
    """One pre-2001 listing row that carries a size but no name (D-2).

    These used to vanish: `candidate_docs` filters unnamed items, and the run then
    reported "0 UNANSWERED" while a third of the directory was unaccounted for. A row
    that cannot be acted on is still a row, and it is counted.
    """
    return {"accession": accession, "file": "", "path": "", "bytes": 0, "words": 0,
            "status": "UNANSWERED NAMELESS-ROW: index.json listed a %s B item with an empty "
                      "name (pre-2001 malformed directory); no URL can be built, content is "
                      "reachable only through the full-submission <accession>.txt"
                      % (item.get("size", "?")),
            "form": form, "filingDate": filing_date, "url": "", "listing": listing_note,
            "cik": cik10(cik), "slot": "nameless:%s:%s" % (accession, item.get("size"))}


def build_plan(cik, rows, lo, hi, docs_per_filing, max_docs):
    """(plan, unanswered, listing_notes, visited, unvisited) -- enumerate document slots.

    Stops opening new directories once `max_docs` slots exist: the cap has to bound the
    HTTP cost, not only the output. Anything past the cut is still reported.
    """
    picked = pick_filings(rows, lo, hi)
    plan, unanswered, notes, visited = [], [], {}, 0
    seen = set()
    for r in picked:
        if len(plan) >= max_docs:
            break
        visited += 1
        items, note, _form = doc_listing(cik, r["accession"])
        notes[r["accession"]] = note
        if items is None:
            unanswered.append({"accession": r["accession"], "file": "", "path": "", "bytes": 0,
                               "words": 0, "status": "UNANSWERED LISTING: %s" % note,
                               "form": r["form"], "filingDate": r["filingDate"], "url": "",
                               "listing": note, "cik": cik10(cik),
                               "slot": "listing:%s" % r["accession"]})
            continue
        for it in items:
            if not it["name"]:
                unanswered.append(nameless_row(r["accession"], r["form"], r["filingDate"],
                                               it, note, cik))
        for c in candidate_docs(r, items, limit=docs_per_filing):
            key = (r["accession"], c["name"])
            if key in seen:
                continue
            seen.add(key)
            base = accession_dirs(cik, r["accession"])[0][1]
            plan.append({"rank": len(plan) + 1, "accession": r["accession"], "form": r["form"],
                         "filingDate": r["filingDate"], "document": c["name"],
                         "bytes_in_index_json": c["size"], "why": c["why"],
                         "url": base + c["name"], "cik": cik10(cik),
                         "slot": "doc:%s:%s" % (r["accession"], c["name"])})
    return plan, unanswered, notes, visited, max(0, len(picked) - visited)


def tally(stored, unanswered, skipped, attempted):
    """The D-3 accounting identity, as a detector rather than a print.

    Nvidia's run stored 31 documents behind an inflated UNANSWERED tally: a row could
    reach the summary twice (the old build also counted 'SKIPPED over cap' as
    UNANSWERED). So the buckets are keyed by slot and proved disjoint as well as total.
    """
    all_rows = [("stored", r) for r in stored] + [("unanswered", r) for r in unanswered] \
        + [("skipped", r) for r in skipped]
    by_slot = {}
    dups = []
    for bucket, r in all_rows:
        slot = r.get("slot") or "doc:%s:%s" % (r.get("accession"), r.get("file"))
        if slot in by_slot:
            dups.append("%s in %s and %s" % (slot, by_slot[slot], bucket))
        else:
            by_slot[slot] = bucket
    total = len(stored) + len(unanswered) + len(skipped)
    msg = ("stored(%d) + unanswered(%d) + skipped(%d) = %d vs attempted(%d) -> %s"
           % (len(stored), len(unanswered), len(skipped), total, attempted,
              "OK" if total == attempted and not dups else "BROKEN"))
    ok = (total == attempted and not dups)
    return ok, msg, dups


def fetch_plan(company_dir, cik, keep, over, pre_unanswered, notes, unvisited, max_docs,
               registrant=""):
    """Fetch the kept slots and put EVERY row in exactly one bucket (D-2, D-3, D-4).

    Factored out of `main` so `selftest` can exercise the accounting against fakes: the
    D-3 tally was never provable while it lived inline, which is how it got inflated.
    """
    cols = ["rank", "slot", "cik", "accession", "file", "path", "bytes", "words", "status",
            "form", "filingDate", "url", "why", "listing"]
    stored, unanswered, skipped = [], [], list(pre_unanswered)
    for s in keep:
        res = grab(company_dir, cik, s["accession"], s["document"], registrant=registrant)
        res.update({"form": s["form"], "filingDate": s["filingDate"], "slot": s["slot"],
                    "rank": s["rank"], "why": s["why"], "cik": s["cik"],
                    "listing": notes.get(s["accession"], "")})
        if res["status"] == "ok":
            stored.append(res)
        elif str(res["status"]).startswith("SKIPPED"):
            skipped.append(res)
        else:
            unanswered.append(res)
    for s in over:
        skipped.append({"slot": s["slot"], "rank": s["rank"], "cik": s["cik"],
                        "accession": s["accession"], "file": s["document"], "path": "",
                        "bytes": 0, "words": 0, "url": s["url"], "why": s["why"],
                        "form": s["form"], "filingDate": s["filingDate"],
                        "listing": notes.get(s["accession"], ""),
                        "status": "SKIPPED beyond --max-docs %d (selection order is documented "
                                  "in the run summary and in _PLAN.csv)" % max_docs})
    if unvisited:
        unanswered.append({"slot": "listing:not-enumerated", "rank": "", "cik": cik10(cik),
                           "accession": "(%d filings)" % unvisited, "file": "", "path": "",
                           "bytes": 0, "words": 0, "url": "", "why": "", "form": "",
                           "filingDate": "", "listing": "",
                           "status": "UNANSWERED NOT-ENUMERATED: %d in-window filings were "
                                     "never listed because --max-docs %d was reached; their "
                                     "documents exist but are unknown to this run"
                                     % (unvisited, max_docs)})
    attempted = len(keep) + len(over) + len(pre_unanswered) + (1 if unvisited else 0)
    return stored, unanswered, skipped, attempted, cols


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
          "no URL constructed" in src)
    check("a document sidecar names the registrant it was filed by",
          '"registrant": registrant' in src)

    # ---- 2026-09-26 pass (intake_hardening_2): each of the five reported intake defects
    # is planted here in the shape the reporter saw, offline, with no network. §15.5: a
    # retrieval script that cannot reproduce its own historical defect is a bug in the
    # script, because the corpus silently absorbs whatever it fails to report.
    real_http, real_listing, real_grab = http_get, doc_listing, grab
    tmp = tempfile.mkdtemp(prefix="sec_intake_selftest_")

    def fake_http(body):
        def _f(url, binary=False, tries=3):
            return 200, body, "ok"
        return _f

    def obs(tag, end, val=7):
        return json.dumps({"entityName": "SELFTEST CORP", "facts": {"us-gaap": {
            tag: {"units": {"USD": [{"end": end, "val": val, "start": "1995-01-01",
                                    "fy": 1996, "fp": "FY", "form": "10-K", "accn": "x-1"}]}}}}})
    try:
        # D-1: window matches nothing -- the exact MSFT/TSLA/COST shape (no observation
        # before ~2007), which the old build reported as "wrote a path" with exit 0.
        globals()["http_get"] = fake_http(obs("Revenues", "2009-06-30"))
        r1 = xbrl_facts(os.path.join(tmp, "d1a"), "789019", "1994-01-01", "1999-12-31", KEY_TAGS)
        canon = os.path.join(tmp, "d1a", "sources", "financials", "xbrl_early_series.csv")
        check("D-1 empty window returns NULL, never a success path", r1["status"] == "NULL")
        check("D-1 empty window writes NO data file it could be read as",
              not os.path.exists(canon))
        check("D-1 the NULL is a named report with bytes on disk",
              bool(r1.get("report")) and os.path.exists(r1["report"])
              and os.stat(r1["report"]).st_size > 200, r1.get("report", ""))
        check("D-1 the report names the coverage floor, not just 'empty'",
              "WINDOW" in r1["reason"] and "2009-06-30" in r1["reason"])
        # D-1 opposite cause: facts IN the window, none under the allow-list.
        globals()["http_get"] = fake_http(obs("EntitySomeObscureTag", "1996-06-30"))
        r2 = xbrl_facts(os.path.join(tmp, "d1b"), "789019", "1994-01-01", "1999-12-31", KEY_TAGS)
        check("D-1 allow-list miss is told apart from absence",
              r2["status"] == "NULL" and r2["reason"].startswith("ALLOW-LIST"))
        check("D-1 untagged in-window evidence survives the miss",
              os.path.exists(r2.get("untagged_path", "")) and r2.get("untagged_bytes", 0) > 0)
        # D-1 positive control + the write-is-verified rule.
        globals()["http_get"] = fake_http(obs("Revenues", "1996-06-30"))
        r3 = xbrl_facts(os.path.join(tmp, "d1c"), "789019", "1994-01-01", "1999-12-31", KEY_TAGS)
        on_disk = len(open(r3["path"], encoding="utf-8").read().strip().splitlines()) - 1
        check("D-1 a written file has the bytes and rows it claims",
              r3["status"] == "OK" and os.stat(r3["path"]).st_size == r3["bytes"] > 0
              and on_disk == r3["rows"] == 1)
        globals()["http_get"] = lambda url, binary=False, tries=3: (0, None, "boom")
        r4 = xbrl_facts(os.path.join(tmp, "d1d"), "789019", "1994-01-01", "1999-12-31", KEY_TAGS)
        check("D-1 a failed fetch is UNANSWERED, not an empty success",
              r4["status"] == "UNANSWERED" and os.path.exists(r4["report"]))
    finally:
        globals()["http_get"] = real_http
    fake_items = [{"name": "", "size": 5000, "type": "text"},
                  {"name": "", "size": 900, "type": "text"},
                  {"name": "a.htm", "size": 900000, "type": "text"},
                  {"name": "z-index-headers.html", "size": 10, "type": "text"},
                  {"name": "", "size": 100, "type": "text"}]
    srows = [{"accessionNumber": "0000912057-95-%06d" % i, "form": "10-K",
              "filingDate": "1995-06-0%d" % i, "primaryDocument": "", "source": "selftest"}
             for i in (1, 2, 3)]
    try:
        globals()["doc_listing"] = lambda cik, acc: (
            fake_items, "listing via selftest (5 items, 3 unnamed)", "selftest")
        plan, una, notes, visited, unvisited = build_plan(
            "909832", srows, "1994-01-01", "1997-12-31", 4, 99)
        nl = [u for u in una if "NAMELESS-ROW" in str(u.get("status", ""))]
        check("D-2 every nameless listing row is emitted and counted",
              len(nl) == 9 and len(plan) > 0, "%d nameless of 15 items" % len(nl))
        check("D-2 a nameless row is never turned into a URL",
              all(not u["url"] and not u["file"] for u in nl))
        globals()["doc_listing"] = lambda cik, acc: (None, "UNANSWERED listing: 503", "")
        plan_n, una_n, _n, _v, _u = build_plan("909832", srows, "1994-01-01", "1997-12-31", 4, 99)
        check("D-2 an unopenable directory is a row, not a lost note",
              len(plan_n) == 0 and len(una_n) == 3 and "UNANSWERED LISTING" in una_n[0]["status"])
        globals()["doc_listing"] = lambda cik, acc: (
            fake_items, "listing via selftest (5 items, 3 unnamed)", "selftest")
        globals()["grab"] = lambda cd, cik, acc, fn, registrant="": {
            "accession": acc, "file": fn, "path": "sec/x", "status": "ok", "bytes": 10,
            "words": 2}
        stored, unanswered, skipped, attempted, _c = fetch_plan(
            tmp, "909832", plan[:2], plan[2:], una, notes, 0, 2)
        ok_id, msg, dups = tally(stored, unanswered, skipped, attempted)
        check("D-4 --max-docs cuts DOCUMENTS and names every slot past the cut",
              len(stored) == 2 and len(skipped) > 0
              and all("beyond --max-docs 2" in s["status"] for s in skipped
                      if s["slot"].startswith("doc:")))
        check("D-3 identity holds on the fixed accounting", ok_id, msg)
        check("D-3 a SKIPPED row is never tallied as UNANSWERED",
              all(not str(u.get("status", "")).startswith("SKIPPED") for u in unanswered))
        ok2, msg2, dups2 = tally(stored, unanswered + [dict(stored[0], status="UNANSWERED x")],
                                 skipped, attempted)
        check("D-3 the identity FIRES on the historical double-count",
              (not ok2) and bool(dups2), msg2)
        ok3, msg3, _d3 = tally(stored, unanswered, skipped, attempted + 1)
        check("D-3 the identity FIRES when a row goes missing", not ok3, msg3)
    finally:
        globals()["doc_listing"], globals()["grab"] = real_listing, real_grab
    try:
        grow = [{"accessionNumber": "0001012870-00-004830", "form": "S-1",
                 "filingDate": "1999-01-14", "primaryDocument": "nvda.txt", "source": "selftest"}]
        ndir = os.path.join(tmp, "company_016_nvidia")
        _n, _e, m1 = write_index(ndir, "1045810", "NVIDIA CORP", "NVDA", grow,
                                 tickers=["NVDA"])
        csv1 = m1["paths"]["csv"]
        sha_before = hashlib.sha1(open(csv1, "rb").read()).hexdigest()
        _n, _e, m2 = write_index(ndir, "1571996", "Dell Inc.", "", grow)
        check("D-5 a foreign registrant is quarantined, never written in place",
              m2["guard"] != "ok" and "quarantine" in m2["paths"]["csv"]
              and m2["paths"]["csv"].startswith(os.path.join(ndir, "sources", "_index",
                                                             "quarantine")))
        check("D-5 the right CIK's index is byte-identical afterwards",
              sha_before == hashlib.sha1(open(csv1, "rb").read()).hexdigest())
        check("D-5 index artefacts are keyed by CIK, not by directory",
              os.path.basename(csv1) == "submissions_CIK0001045810.csv"
              and os.path.exists(m1["paths"]["json"]))
        side = json.load(open(os.path.join(ndir, "sources", "_index",
                                          "_registrant_CIK0001045810.json"), encoding="utf-8"))
        check("D-5 registrant name is logged in the sidecar for audit",
              side["registrant"] == "NVIDIA CORP" and side["guard"] == "ok")
        ddir = os.path.join(tmp, "company_041_dell")
        write_index(ddir, "826083", "Dell Technologies Inc.", "DEL", grow, tickers=["DEL"])
        _n, _e, m3 = write_index(ddir, "1571996", "Dell Inc.", "", grow)
        check("D-5 the Dell shell passes the name test and is caught by no-clobber",
              m3["guard"] != "ok" and any("already holds" in r for r in m3["guard_reasons"]),
              "; ".join(m3["guard_reasons"])[:60])
        _n, _e, m4 = write_index(os.path.join(tmp, "company_099_acme"), "424242",
                                 "WIDGET HOLDINGS", "", grow)
        check("D-5 an unrelated registrant name is refused on identity alone",
              m4["guard"] != "ok", "; ".join(m4["guard_reasons"])[:60])
        _n, _e, m5 = write_index(os.path.join(tmp, "company_042_target"), "1571996",
                                 "Dell Inc.", "", grow)
        check("D-5 no substring accident: 'dell' does not match 'target'",
              m5["guard"] != "ok")
    finally:
        pass
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
        p.add_argument("--max-docs", type=int, default=40,
                       help="hard cap on DOCUMENTS fetched (not filings); selection order is "
                            "printed in the run summary and written to _PLAN.csv")
        p.add_argument("--docs-per-filing", type=int, default=4)
        p.add_argument("--tags", default="",
                       help="facts: comma-separated XBRL tag allow-list (default KEY_TAGS)")
        p.add_argument("--all-tags", action="store_true",
                       help="facts: ignore the allow-list and keep every in-window observation")
        p.add_argument("--allow-mismatch", action="store_true",
                       help="index/auto: write canonical artefacts even when the registrant "
                            "name/ticker does not match the directory slug (NOT recommended)")
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
        name, tick, rows, ticks, formers = submissions_index(a.cik)
        n, earliest, meta = write_index(a.company_dir, a.cik, name, tick, rows,
                                        tickers=ticks, former_names=formers)
        print("index: %d filings from registrant %r (CIK %s, tickers %s)"
              % (n, name, meta["cik"], meta["tickers"]))
        print("index: registrant guard = %s -- %s" % (meta["guard"],
                                                      "; ".join(meta["guard_reasons"])))
        print("index: artefacts keyed by CIK -> %s"
              % ", ".join(os.path.basename(p) for p in meta["paths"].values()))
        print("index: %d rows dropped for no accession, %d without primaryDocument (both "
              "counted in the artefacts)" % (meta["rows_dropped_no_accession"],
                                             meta["rows_without_primaryDocument"]))
        if meta["guard"] != "ok":
            print("*** REFUSED-WRONG-REGISTRANT: EDGAR answered %r for CIK %s but this "
                  "directory is %r. Everything went to %s; no canonical index was touched."
                  % (name, meta["cik"], meta["company_dir"], os.path.dirname(
                      meta["paths"]["csv"])))
            print("*** Re-run with the legacy registrant's CIK, or --allow-mismatch if you "
                  "are certain. This is the 2026-09-26 Dell/1571996 clobber, D-5.")
            if not a.allow_mismatch:
                return 2
        if any("UNANSWERED" in str(r.get("status", "")) for r in rows):
            rc = 1
    if a.cmd == "facts":
        tags = KEY_TAGS
        if a.tags:
            tags = {t.strip() for t in a.tags.split(",") if t.strip()}
        if a.all_tags:
            tags = set()
        r = xbrl_facts(a.company_dir, a.cik, a.lo, a.hi, tags)
        if r["status"] == "OK":
            print("facts: wrote %d rows, %d bytes -> %s" % (r["rows"], r["bytes"], r["path"]))
            if r.get("note"):
                print("facts: %s" % r["note"])
            rc = 0
        else:
            print("facts: %s -- NO DATA FILE WRITTEN. %s" % (r["status"], r["reason"]))
            print("facts: report -> %s" % r["report"])
            if r.get("untagged_path"):
                print("facts: untagged in-window evidence -> %s (%d rows, %d bytes)"
                      % (r["untagged_path"], r.get("untagged_rows", 0),
                         r.get("untagged_bytes", 0)))
            rc = 1
    if a.cmd == "grab":
        print(json.dumps(grab(a.company_dir, a.cik, a.accession, a.file or "index-headers.txt")))
    if a.cmd == "auto":
        if rows is None:
            raise SystemExit("auto needs the submissions index")
        plan, pre_unanswered, notes, visited, unvisited = build_plan(
            a.cik, rows, a.lo, a.hi, a.docs_per_filing, a.max_docs)
        d = os.path.join(a.company_dir, "sources", "sec")
        os.makedirs(d, exist_ok=True)
        keep, over = plan[:a.max_docs], plan[a.max_docs:]
        plan_cols = ["rank", "cik", "accession", "form", "filingDate", "document",
                     "bytes_in_index_json", "why", "url", "disposition"]
        prow = []
        for s in keep:
            prow.append(dict(s, disposition="fetched this run"))
        for s in over:
            prow.append(dict(s, disposition="SKIPPED beyond --max-docs %d" % a.max_docs))
        _write_verified(os.path.join(d, "_PLAN.csv"), _csv_text(plan_cols, prow))
        print("auto: %d accessions in window, %d directories opened, %d document slots "
              "planned, %d kept under --max-docs %d, %d skipped past the cut"
              % (visited + unvisited, visited, len(plan), len(keep), a.max_docs, len(over)))
        print("auto: selection order -- %s" % SELECTION_ORDER)
        if a.dry_run:
            print("dry-run: no bytes downloaded. First %d planned slots:" % min(len(keep), 25))
            for s in keep[:25]:
                print("   %2d %-11s %-24s %-34s %s%s" % (
                    s["rank"], s["filingDate"], s["form"][:24], s["document"][:34],
                    ("%s B " % s["bytes_in_index_json"])
                    if s["bytes_in_index_json"] is not None else "(size unlisted) ", s["url"]))
            return rc
        stored, unanswered, skipped, attempted, cols = fetch_plan(
            a.company_dir, a.cik, keep, over, pre_unanswered, notes, unvisited, a.max_docs,
            registrant=name)
        ok, msg, dups = tally(stored, unanswered, skipped, attempted)
        nameless = sum(1 for u in unanswered if "NAMELESS-ROW" in str(u.get("status", "")))
        _write_verified(os.path.join(d, "_MANIFEST.csv"), _csv_text(cols, stored))
        _write_verified(os.path.join(d, "_UNANSWERED.csv"), _csv_text(cols, unanswered))
        _write_verified(os.path.join(d, "_SKIPPED.csv"), _csv_text(cols, skipped))
        run = {"cik": cik10(a.cik), "registrant": name, "tickers": ticks,
               "company_dir": os.path.basename(os.path.normpath(a.company_dir)),
               "window": "%s..%s" % (a.lo, a.hi), "max_docs": a.max_docs,
               "docs_per_filing": a.docs_per_filing, "guard": meta["guard"],
               "attempted": attempted, "stored": len(stored), "unanswered": len(unanswered),
               "skipped": len(skipped), "nameless_rows": nameless,
               "identity": msg, "identity_ok": ok, "duplicate_slots": dups,
               "bytes": sum(m["bytes"] for m in stored),
               "words": sum(m["words"] for m in stored),
               "selection_order": SELECTION_ORDER,
               "built": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
        _write_verified(os.path.join(d, "_RUN.json"), json.dumps(run, indent=1))
        words = sum(m["words"] for m in stored)
        print("auto: %d documents stored (%d bytes, %d words); %d UNANSWERED (of which %d "
              "nameless pre-2001 listing rows); %d SKIPPED"
              % (len(stored), run["bytes"], words, len(unanswered), nameless, len(skipped)))
        print("auto: IDENTITY stored + unanswered + skipped == attempted -> %s" % msg)
        if dups:
            print("auto: DOUBLE-COUNTED SLOTS (this is defect D-3, do not trust the tally): %s"
                  % "; ".join(dups[:5]))
        for s in unanswered[:10]:
            print("   UNANSWERED %s %s: %s" % (s["accession"], s["file"], s["status"]))
        if not ok:
            return 2
        rc = 1 if unanswered else rc
    return rc


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main())
