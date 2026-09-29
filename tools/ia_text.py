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
    # Params are hand-built, not urlencoded. advancedsearch uses TWO different shapes:
    # `rows` is a plain scalar (rows[]= is ignored and you silently get 1 document), while
    # `fl[]` needs literal brackets -- urlencode() escapes them to %5B%5D, the field list is
    # ignored, and every doc comes back empty. Both failures look like "no results found".
    url = (ADV + "?q=" + urllib.parse.quote(q) + "&output=json&rows=%d" % rows
           + "".join("&fl[]=" + urllib.parse.quote(f) for f in fl)
           + "&sort[]=" + urllib.parse.quote("downloads desc"))
    s, body, note = get(url, allow_insecure=allow_insecure)
    if not body:
        return None, note, None
    try:
        j = json.loads(body)
    except ValueError:
        return None, "UNPARSEABLE (advancedsearch returned a page, not JSON)", None
    resp = j.get("response", {}) or {}
    docs = resp.get("docs", []) or []
    num_found = resp.get("numFound")
    # numFound is the archive's total and `rows` is the page we asked for; the two are different
    # numbers and printing only the second is how a caller comes to believe it counted the corpus.
    return docs, "ok (%d rows returned of numFound %s)" % (len(docs), num_found), num_found


def text_layer_names(identifier, allow_insecure=False):
    """Resolve the REAL text-layer filename. `<id>_djvu.txt` is the common convention, not a
    guarantee: many items name their OCR text after the item, the volume, or nothing at all,
    and assuming the convention 404s on exactly the items that matter. Ask the metadata API
    first, then fall back to the convention so a dead route is never mistaken for no text."""
    s, body, note = get("https://archive.org/metadata/%s" % identifier,
                        allow_insecure=allow_insecure)
    cands = []
    if body:
        try:
            j = json.loads(body)
        except ValueError:
            j = None
        if j:
            for f in j.get("files", []) or []:
                n = f.get("name", "")
                if n.endswith("_djvu.txt") or n.endswith("_text.txt") or n == "djvu.txt":
                    cands.append((0 if n.endswith("_djvu.txt") else 1,
                                  -int(f.get("size", 0) or 0), n))
            cands.sort()
    cands.append((9, 0, "%s_djvu.txt" % identifier))
    return [c[2] for c in cands], note


def ocr_url(identifier, fname=None):
    # IA filenames contain spaces constantly ("Byte Magazine v02"); without quoting, the
    # request 404s on a file that exists.
    return "https://archive.org/download/%s/%s" % (urllib.parse.quote(identifier),
                                                   urllib.parse.quote(fname or
                                                                      "%s_djvu.txt" % identifier))


def local_name(identifier, fname=None):
    """The on-disk filename for a text layer, and the reason it is not just `<id>_djvu.txt`.

    A bound run published as ONE item with a layer per year (Boeing's 46 reports 1934-1978, Kroger's
    104 layers 1925-2007) can only be addressed by filename. Two consequences, both fixed here: the
    requested volume must be selectable, and two volumes of one item must not land on one path --
    the old single-path rule meant a second fetch silently OVERWROTE the first item's bytes.
    """
    if not fname or fname == "%s_djvu.txt" % identifier:
        return "%s_djvu.txt" % identifier
    safe = re.sub(r"[^A-Za-z0-9._-]+", "_", fname)
    return "%s__%s" % (identifier, safe)


def text_layer_listing(identifier, allow_insecure=False):
    """(name, size) for every readable text layer on an item -- so a caller can CHOOSE a volume
    instead of accepting whichever layer the metadata happened to sort first."""
    s, body, note = get("https://archive.org/metadata/%s" % identifier,
                        allow_insecure=allow_insecure)
    if not body:
        return None, note
    try:
        j = json.loads(body)
    except ValueError:
        return None, "UNPARSEABLE metadata"
    out = []
    for f in j.get("files", []) or []:
        n = f.get("name", "")
        if n.endswith(("_djvu.txt", "_text.txt", ".txt")) and not n.endswith(".gz"):
            out.append((n, int(f.get("size", 0) or 0)))
    return sorted(out), "ok"


def fetch(company_dir, identifier, max_mb=12, allow_insecure=False, filename=None):
    out_dir = os.path.join(company_dir, "sources", "periodicals")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, local_name(identifier, filename))
    if os.path.exists(path) and os.path.getsize(path) > 200:  # cached bytes keep their route stamp
        return path, "cached", os.path.getsize(path)
    if filename:
        names = [filename]
        mnote = "explicit --file"
    else:
        names, mnote = text_layer_names(identifier, allow_insecure)
    body = None
    note = mnote
    used = None
    for nm in names:
        s, body, note = get(ocr_url(identifier, nm), allow_insecure=allow_insecure)
        if body and body[:200].lower().find(b"<html") < 0:
            used = nm
            break
        body = None
    if body is None:
        return None, "UNANSWERED -- no text layer resolved (%s); tried %s" % (
            note, ", ".join(names[:4])), 0
    note = "ok via %s" % used
    if len(body) > max_mb * 1024 * 1024:
        body = body[: int(max_mb * 1024 * 1024)] + b"\n[TRUNCATED BY --max-mb]\n"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(body.decode("utf-8", "replace"))
    side = {"identifier": identifier, "url": ocr_url(identifier, used),
            "fetched": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "bytes": len(body),
            "route": "download/<id>/%s (OCR text layer)" % (used or "?"),
            "note": "the `text:` field in advancedsearch matches ANNOTATIONS, not this layer",
            "transport": "UNVERIFIED TLS -- re-check before citing at High confidence"
            if allow_insecure else "verified TLS"}
    with open(path + ".meta.json", "w", encoding="utf-8") as f:
        json.dump(side, f, indent=1)
    return path, "ok", len(body)


GREP_CAP = 200


def grep_local(path, pattern, ctx=1, cap=GREP_CAP):
    rx = re.compile(pattern, re.I)
    hits = []
    lines = open(path, encoding="utf-8", errors="replace").read().splitlines()
    for i, ln in enumerate(lines):
        if rx.search(ln):
            hits.append({"line": i + 1, "text": ln.strip()[:300],
                         "context": [l.strip()[:300] for l in
                                     lines[max(0, i - ctx):i] + lines[i + 1:i + 1 + ctx]]})
            if len(hits) >= cap:
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
    ap.add_argument("mode", choices=["search", "fetch", "grep", "mine", "list-files"])
    ap.add_argument("--q"); ap.add_argument("--id"); ap.add_argument("--pattern")
    ap.add_argument("--company-dir", default=".")
    ap.add_argument("--rows", type=int, default=20)
    ap.add_argument("--max-mb", type=float, default=12)
    ap.add_argument("--file", help="fetch/grep one named text layer of a multi-file item "
                                   "(a bound run publishes a layer per year)")
    ap.add_argument("--ctx", type=int, default=1)
    ap.add_argument("--insecure", action="store_true",
                    help="allow unverified TLS for archive.org hosts (stale local CA store)")
    a = ap.parse_args()
    out = {"mode": a.mode}

    if a.mode == "search" or a.mode == "mine":
        if not a.q:
            raise SystemExit("--q required")
        docs, note, num_found = search(a.q, a.rows, allow_insecure=a.insecure)
        out["search"] = note if docs is None else {
            "numFound": num_found, "rows_returned": len(docs),
            "items": docs[: a.rows],
            "reading": "numFound is the archive total; rows_returned is this page. Never report "
                       "the second as the first (Chevron probe defect 2, RD-132)."}
        if docs is None:
            out["verdict"] = "UNANSWERED -- " + note
            print(json.dumps(out, indent=1)[:4000]); return 1
        if a.mode == "search":
            print(json.dumps(out, indent=1)[:6000])
            return 0
    if a.mode == "list-files":
        layers, lnote = text_layer_listing(a.id, a.insecure)
        if layers is None:
            print(json.dumps({"identifier": a.id, "status": "UNANSWERED", "note": lnote}, indent=1))
            return 1
        print(json.dumps({"identifier": a.id, "text_layers": len(layers),
                          "note": "a bound run may hold one layer per year; --file picks the "
                                  "volume, and each lands on its own path",
                          "files": [{"name": n, "size": s} for n, s in layers]}, indent=1)[:12000])
        return 0
    if a.mode == "fetch":
        p, st, n = fetch(a.company_dir, a.id, a.max_mb, a.insecure, a.file)
        out["fetch"] = {"path": p, "status": st, "bytes": n, "file_requested": a.file or ""}
        print(json.dumps(out, indent=1))
        return 0 if p else 1
    if a.mode == "grep":
        p = os.path.join(a.company_dir, "sources", "periodicals", local_name(a.id, a.file))
        if not os.path.exists(p):
            print(json.dumps({"error": "not fetched yet -- run fetch (with --file for a volume "
                                            "of a bound run)", "path": p}, indent=1))
            return 1
        hits = grep_local(p, a.pattern or ".", a.ctx)
        print(json.dumps({"path": p, "verdict": classify(hits, os.path.getsize(p)),
                          "hits": hits[:15]}, indent=1))
        return 0
    if a.mode == "mine":
        results = []
        for d in (search(a.q, min(a.rows, 8), allow_insecure=a.insecure)[0] or []):
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
