#!/usr/bin/env python3
"""
ia_text.py -- reach the OCR text layer of an Internet Archive item, locally.

Why this exists: the Microsoft probe (2026-09-26) established that Internet Archive
`advancedsearch` `text:` queries match an item's **annotations**, not its scanned pages.
A `text:microsoft` hit returned 261 KB of a 1976 magazine whose OCR contained zero
occurrences of the word -- the match was an uploader's description. Reporting that as
"periodical evidence found" would have been a fabricated corpus, and reporting the
following local grep's zero as "no coverage" would have been a false null.

So: search for the item, DOWNLOAD the OCR text layer, and grep bytes you actually hold.
Stdlib only.

  python tools/ia_text.py search  --q 'title:("Popular Electronics") AND year:1975' --rows 20
  python tools/ia_text.py fetch   --id popular-electronics-v02n04 --company-dir <dir> [--max-mb 12]
  python tools/ia_text.py grep    --id <identifier> --pattern MITS --company-dir <dir> [--ctx 1]
  python tools/ia_text.py mine    --q '<advancedsearch query>' --pattern '<regex>' --company-dir <dir>
                                  [--rows 8] [--max-mb 12]        # search -> fetch -> grep, one call

Every result is classified TIER1_CANDIDATE / LEAD_ONLY / NULL / UNANSWERED / ERROR.
An HTTP error is UNANSWERED and is never reported as an absent record.
"""

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

UA = "FounderPlaybook Research AdminContact@example.com"
# This machine's trust store is stale for the archive.org CDN (the same expired-CA artefact
# that blocks HathiTrust), so a verified fetch can fail on a route that is genuinely there.
# Insecure transport is therefore OPT-IN, per host, and is stamped into every sidecar --
# bytes pulled unverified must not carry High confidence until re-checked.
INSECURE_HOSTS = {"archive.org", "ia800000.us.archive.org", "raw.githubusercontent.com"}
_CTX_INSECURE = None
ADV = "https://archive.org/advancedsearch.php"
CAP_DEFAULT = 12 * 1024 * 1024


def _insecure_ctx():
    global _CTX_INSECURE
    if _CTX_INSECURE is None:
        import ssl
        _CTX_INSECURE = ssl.create_default_context()
        _CTX_INSECURE.check_hostname = False
        _CTX_INSECURE.verify_mode = ssl.CERT_NONE
    return _CTX_INSECURE


def get(url, tries=3, timeout=90, allow_insecure=False):
    last = None
    host = urllib.parse.urlparse(url).hostname or ""
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            kw = {}
            if allow_insecure and host in INSECURE_HOSTS:
                kw["context"] = _insecure_ctx()
            with urllib.request.urlopen(req, timeout=timeout, **kw) as r:
                return r.status, r.read(), ("ok" if not kw
                                            else "ok-INSECURE (unverified TLS: re-check before High)")
        except urllib.error.HTTPError as e:
            last = "HTTP %s" % e.code
            if e.code in (401, 403, 429, 500, 502, 503, 504):
                time.sleep(1.2 * (attempt + 1))
                continue
            return e.code, b"", last
        except Exception as e:
            last = "%s: %s" % (type(e).__name__, e)
            time.sleep(1.0 * (attempt + 1))
    return 0, b"", "UNANSWERED after %d tries (%s)" % (tries, last)


def search(q, rows=20, fl=None, allow_insecure=False):
    fl = fl or ["identifier", "title", "year", "collection", "downloads", "mediatype"]
    url = "%s?%s" % (ADV, urllib.parse.urlencode(
        {"q": q, "rows[]": rows, "fl[]": fl, "output": "json", "sort[]": "downloads desc"}))
    s, body, note = get(url, allow_insecure=allow_insecure)
    if not body:
        return None, note
    try:
        j = json.loads(body)
    except ValueError:
        return None, "UNPARSEABLE (advancedsearch returned a page, not JSON)"
    docs = (j.get("response", {}) or {}).get("docs", []) or []
    return docs, "ok (%s rows matched of %s)" % (len(docs),
                                                 j.get("response", {}).get("numFound"))


def ocr_url(identifier):
    return "https://archive.org/download/%s/%s_djvu.txt" % (identifier, identifier)


def fetch(company_dir, identifier, max_mb=12, allow_insecure=False):
    out_dir = os.path.join(company_dir, "sources", "periodicals")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "%s_djvu.txt" % identifier)
    if os.path.exists(path) and os.path.getsize(path) > 200:  # cached bytes keep their route stamp
        return path, "cached", os.path.getsize(path)
    s, body, note = get(ocr_url(identifier), allow_insecure=allow_insecure)
    if not body:
        return None, note, 0
    if len(body) > max_mb * 1024 * 1024:
        body = body[: int(max_mb * 1024 * 1024)] + b"\n[TRUNCATED BY --max-mb]\n"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(body.decode("utf-8", "replace"))
    side = {"identifier": identifier, "url": ocr_url(identifier),
            "fetched": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "bytes": len(body), "route": "download/<id>/<id>_djvu.txt (OCR text layer)",
            "note": "the `text:` field in advancedsearch matches ANNOTATIONS, not this layer",
            "transport": "UNVERIFIED TLS -- re-check before citing at High confidence"
            if allow_insecure else "verified TLS"}
    with open(path + ".meta.json", "w", encoding="utf-8") as f:
        json.dump(side, f, indent=1)
    return path, "ok", len(body)


def grep_local(path, pattern, ctx=1):
    rx = re.compile(pattern, re.I)
    hits = []
    lines = open(path, encoding="utf-8", errors="replace").read().splitlines()
    for i, ln in enumerate(lines):
        if rx.search(ln):
            hits.append({"line": i + 1, "text": ln.strip()[:300],
                         "context": [l.strip()[:300] for l in
                                     lines[max(0, i - ctx):i] + lines[i + 1:i + 1 + ctx]]})
            if len(hits) >= 40:
                break
    return hits


def classify(hits, bytes_fetched):
    if bytes_fetched == 0:
        return "UNANSWERED/ERROR -- no text layer reached"
    if hits:
        return "TIER1_CANDIDATE -- %d in-page hits in held bytes" % len(hits)
    if bytes_fetched < 400:
        return "UNANSWERED -- text layer too thin to call this a null (%d B)" % bytes_fetched
    return "NULL -- %d KB of OCR held, zero hits" % (bytes_fetched // 1024)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["search", "fetch", "grep", "mine"])
    ap.add_argument("--q"); ap.add_argument("--id"); ap.add_argument("--pattern")
    ap.add_argument("--company-dir", default=".")
    ap.add_argument("--rows", type=int, default=20)
    ap.add_argument("--max-mb", type=float, default=12)
    ap.add_argument("--ctx", type=int, default=1)
    ap.add_argument("--insecure", action="store_true",
                    help="allow unverified TLS for archive.org hosts (stale local CA store)")
    a = ap.parse_args()
    out = {"mode": a.mode}

    if a.mode == "search" or a.mode == "mine":
        if not a.q:
            raise SystemExit("--q required")
        docs, note = search(a.q, a.rows, a.insecure)
        out["search"] = note if docs is None else {"num": len(docs),
                                                   "items": docs[: a.rows]}
        if docs is None:
            out["verdict"] = "UNANSWERED -- " + note
            print(json.dumps(out, indent=1)[:4000]); return 1
        if a.mode == "search":
            print(json.dumps(out, indent=1)[:6000])
            return 0
    if a.mode == "fetch":
        p, st, n = fetch(a.company_dir, a.id, a.max_mb, a.insecure)
        out["fetch"] = {"path": p, "status": st, "bytes": n}
        print(json.dumps(out, indent=1))
        return 0 if p else 1
    if a.mode == "grep":
        p = os.path.join(a.company_dir, "sources", "periodicals", "%s_djvu.txt" % a.id)
        if not os.path.exists(p):
            print(json.dumps({"error": "not fetched yet -- run fetch", "path": p}, indent=1))
            return 1
        hits = grep_local(p, a.pattern or ".", a.ctx)
        print(json.dumps({"path": p, "verdict": classify(hits, os.path.getsize(p)),
                          "hits": hits[:12]}, indent=1))
        return 0
    if a.mode == "mine":
        results = []
        for d in (search(a.q, min(a.rows, 8))[0] or []):
            ident = d.get("identifier")
            if not ident:
                continue
            p, st, n = fetch(a.company_dir, ident, a.max_mb, a.insecure)
            hits = grep_local(p, a.pattern, a.ctx) if p else []
            results.append({"identifier": ident, "title": (d.get("title") or "")[:120],
                            "year": d.get("year"), "fetch": st, "bytes": n,
                            "verdict": classify(hits, n), "hits": hits[:5]})
            time.sleep(0.3)
        out["mined"] = results
        print(json.dumps(out, indent=1)[:12000])
        tier1 = [r for r in results if r["verdict"].startswith("TIER1")]
        unanswered = [r for r in results if r["verdict"].startswith("UNANSWERED")]
        print("\n%d items: %d TIER1_CANDIDATE, %d NULL/LEAD, %d UNANSWERED "
              "-- UNANSWERED items are NOT evidence of absence"
              % (len(results), len(tier1), len(results) - len(tier1) - len(unanswered),
                 len(unanswered)), file=sys.stderr)
        return 0
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main())
