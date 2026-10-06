#!/usr/bin/env python3
"""
cdx_intake.py -- deterministic Internet Archive CDX intake for corpus family (b), the
Founder's Playbook.

Why this exists. Method s15.2 sets a company's density tier from how many of FIVE corpus
families return in-window Tier-1 text, and family (b) -- web archives -- had no scripted
route whatsoever: `tools/queries.json` carries 427 tasks across chronicling_america /
internet_archive / corporate_print / hathitrust / google_books and NOTHING for web
archives. So for every company in the fleet the verdict has been structurally four-family,
and five probes named exactly this as the route most likely to change a tier (Centene
FR-1, Cencora S-4 l.839/850, Elevance l.262 + FR-6, Verizon FR-2/FR-6, Comcast family (b)
UNTRIED with 0 calls). Microsoft holds family-(b) artefacts only because an agent wrote an
ad-hoc curl; the bytes on disk are two identical 11,832-byte "Internet Archive: Temporarily
Offline" banners whose sidecars read `"http_status": 503, "verdict": "UNANSWERED (service
503, not an empty result)"`. That is the class Microsoft's audit NR-1 caught: a dead route
reported as if it had been tested and found empty. This script makes that unrepresentable.

What it does. For a slug + domain list, it (1) enumerates captures over a year window via
the CDX API, (2) ranks the most promising captures (status 200, text/html, a real body,
spread across the window so an in-window tier question can be answered), (3) fetches a
bounded number of snapshot bytes into `<company>/sources/web_archive/` with `.meta.json`
sidecars, and (4) records EVERY slot in exactly one of four states:

  ANSWERED    snapshot bytes stored, sidecar written, sha256 verified
  NULL        CDX answered 200 with ZERO rows for that domain/window -- a real emptiness
  UNANSWERED  4xx / 5xx / timeout / challenge / apology-page-under-200 -- the endpoint
              refused, so the window was NEVER TESTED. A remedy is named in the sidecar.
  UNTRIED     no domain supplied for the slug, or the request budget was not spent on it.

NULL and UNANSWERED are opposite findings and the corpus has been absorbing the difference.
A refusal can never print as "0 captures": the capture count field is not even emitted for
an UNANSWERED slot (see `classify_cdx` and `_verify_slot`).

Stdlib only.  Usage:
  python tools/cdx_intake.py enumerate --domain centene.com --from 1996 --to 2002 [--limit 500]
  python tools/cdx_intake.py run --slug centene,cencora [--per-domain 8] [--max-requests 60]
                                 [--company-root founders_playbook/01_companies] [--dry-run]
  python tools/cdx_intake.py audit --company-dir <dir>      # re-verify bytes vs sidecars
  python tools/cdx_intake.py selftest                       # or: --self-test  (no network)

Domains come from `tools/web_domains.json` (slug -> [{domain, window, why, source_line}]).
They are NOT in `tools/queries.json`: that file belongs to the harvest lanes. A domain with
no citation is a lead with no provenance, so every entry must carry `source_line`.

Exit codes: 0 all slots clean, 1 partial (some UNANSWERED/NULL), 2 hard failure.
A non-200 is recorded as UNANSWERED, never as a null. See 00_METHOD_AND_STYLE.md s15.2, s15.5.
"""

import argparse
import hashlib
import json
import os
import re
import ssl
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAINS_FILE = os.path.join(REPO, "tools", "web_domains.json")
COMPANY_ROOT = os.path.join(REPO, "founders_playbook", "01_companies")

# Declared contact, same as every other lane: an undeclared tool gets a 403 that reads
# like an empty archive if you do not check the body.
UA = "FounderPlaybook Research AdminContact@example.com"
CDX_BASE = "https://web.archive.org/cdx/search/cdx"
SNAP_BASE = "https://web.archive.org/web/"

# >=1 s between requests to a HOST (method s15.1 politeness; the fleet is also running the
# periodical and mine lanes tonight, so the gap is per-host rather than global and the whole
# run is additionally capped by --max-requests).
POLITE_SECONDS = 1.0
# 503/504 from web.archive.org is a soft cooldown, not an outage: a 1.5 s retry just deepens it.
BACKOFF_SECONDS = (10, 20, 40)
# CDX field list. `original` is stored as `url` in every row so the sidecar key matches the
# brief's schema. `digest` is kept: it is how a re-run proves the bytes are the same capture.
DEFAULT_FL = ["timestamp", "original", "mimetype", "statuscode", "length", "digest"]
REQUIRED_ROW_KEYS = ("url", "timestamp", "mimetype", "statuscode", "length")

# Bodies that a CDX endpoint returns IN PLACE OF an answer. Every one of these arriving under
# a status 200 must land as UNANSWERED: a 200 whose payload is an HTML apology page is not an
# empty result, and the Microsoft fixture on disk proves the endpoint serves exactly this body.
# Bytes-in, never str-in-bytes (sec_intake ERROR_MARKERS defect: a str marker made every
# binary fetch collapse into "UNANSWERED" and look like an outage).
CDX_LIE_MARKERS = (
    b"<html", b"<!DOCTYPE", b"<title>", b"Internet Archive: Temporarily Offline",
    b"Temporarily Offline", b"Rate Limited", b"Too Many Requests", b"Server Busy",
    b"Maximum CDX", b"Blocked", b"Access Denied", b"Unauthorized", b"Guru Meditation",
    b"Are you a robot", b"captcha", b"challenge", b"robots.txt", b"We're sorry",
)
# IA's own interstitials under a fetch status 200 -- an IA page ABOUT the archive, not the
# archived bytes.
SNAPSHOT_LIE_MARKERS = (
    b"Wayback Machine has not archived that URL",
    b"Internet Archive: Temporarily Offline",
    b"is not in the Wayback Machine",
    b"Got an HTTP 302 response at crawl time",
    b"Got an HTTP 301 response at crawl time",
    b"To browse the Internet Archive's collection",
)
# This machine's trust store is stale for some archive.org hosts (same expired-CA artefact
# that blocks HathiTrust), so unverified TLS is OPT-IN per host and stamped into the sidecar.
INSECURE_HOSTS = {"archive.org", "web.archive.org", "ia800000.us.archive.org"}

ANSWERED, NULL, UNANSWERED, UNTRIED = "ANSWERED", "NULL", "UNANSWERED", "UNTRIED"
STATES = (ANSWERED, NULL, UNANSWERED, UNTRIED)

_last_by_host = {}
_budget = {"left": 0, "cap": 0, "used": 0}
_allow_insecure = False
_ctx_insecure = None


# ---------------------------------------------------------------- transport

def _insecure_ctx():
    global _ctx_insecure
    if _ctx_insecure is None:
        _ctx_insecure = ssl.create_default_context()
        _ctx_insecure.check_hostname = False
        _ctx_insecure.verify_mode = ssl.CERT_NONE
    return _ctx_insecure


def _pace(host):
    """Enforce >=POLITE_SECONDS between requests to the SAME host."""
    wait = (_last_by_host.get(host, 0.0) + POLITE_SECONDS) - time.monotonic()
    if wait > 0:
        time.sleep(wait)
    _last_by_host[host] = time.monotonic()


def _markers_hit(raw, markers):
    """Return the matching marker or None. Asserts bytes so a str marker cannot slip in."""
    for m in markers:
        assert isinstance(m, bytes), "markers must be bytes: %r" % (m,)
        if m in raw:
            return m
    return None


def http_get(url, tries=3, timeout=60):
    """Return (status, raw_bytes_or_None, note, transport). 'note' carries the remedy reason.

    `transport` is `ok`, or `ok-INSECURE (unverified TLS: re-check before High)` when the
    stale-CA fallback was used -- bytes pulled unverified must not carry High confidence.
    A budget exhaustion is returned as status 0 with a note that names the remedy; it must
    never be written as an empty result.
    """
    host = urllib.parse.urlparse(url).hostname or ""
    last = None
    for attempt in range(tries):
        if _budget["left"] <= 0:
            return 0, None, ("request budget exhausted (--max-requests %d reached): the "
                             "window was NOT tested -- raise --max-requests or re-run"
                             % _budget["cap"]), ""
        _pace(host)
        _budget["left"] -= 1
        _budget["used"] += 1
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
        kw = {}
        if _allow_insecure and host in INSECURE_HOSTS:
            kw["context"] = _insecure_ctx()
        transport = "ok"
        try:
            with urllib.request.urlopen(req, timeout=timeout, **kw) as r:
                raw = r.read()
                status = r.status
            if kw:
                transport = "ok-INSECURE (unverified TLS: re-check before High)"
            return status, raw, "ok", transport
        except urllib.error.HTTPError as e:
            body = b""
            try:
                body = e.read() or b""
            except Exception:
                body = b""
            reason = "HTTP %s" % e.code
            if body:
                reason += " with %d-byte body" % len(body)
            last = reason
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(BACKOFF_SECONDS[min(attempt, len(BACKOFF_SECONDS) - 1)])
                continue
            if e.code in (401, 403):
                time.sleep(2.0 * (attempt + 1))
                continue
            return e.code, b"", last, transport
        except Exception as e:                      # timeout / DNS / TLS: unanswered, not null
            last = "%s: %s" % (type(e).__name__, e)
            time.sleep(1.0 * (attempt + 1))
    return 0, None, "no answer after %d tries (%s)" % (tries, last), transport


# ---------------------------------------------------------------- s15.5 remedy naming

def remedy_for(state, http_status, note):
    """Name the remedy so a dead route cannot be filed as a finding about the past."""
    if state == ANSWERED:
        return ""
    if state == NULL:
        return ("window is genuinely unpopulated in the archive for this domain: try the "
                "predecessor/alias domains in tools/web_domains.json, do not re-run this one")
    if state == UNTRIED:
        return ("supply a cited domain in tools/web_domains.json (slug -> domain) or re-run "
                "with --max-requests raised")
    if http_status == 503 or note.startswith("HTTP 50") or "Temporarily Offline" in note:
        return ("service refused with %s -- an IA cooldown, NOT an empty archive: retry after "
                ">=60 s, lower --max-requests, or run from CI egress" % (http_status or note))
    if http_status in (401, 403):
        return ("endpoint refused at %s (bot challenge / undeclared tool): raise the delay, "
                "declare the UA already set, or run from CI egress -- the window was not tested")
    if "challenge" in note or "robot" in note:
        return "challenge page returned instead of CDX rows: slow the rate or change egress"
    if "budget" in note or "--max-requests" in note:
        return ("the run spent its request cap before this window was reached: raise "
                "--max-requests or re-run this domain alone -- the window was NOT tested")
    if http_status == 200:
        return ("status 200 carried a non-CDX body (apology/HTML): the endpoint refused while "
                "looking like an answer -- re-check the URL shape, the window was NOT tested")
    return ("transport failed (%s): re-run; if the host is archive.org try --allow-insecure "
            "for this machine's stale CA store -- the window was NOT tested" % note)


# ---------------------------------------------------------------- enumerate

def cdx_url(domain, frm, to, limit=500, collapse="timestamp:6", fl=None):
    fl = fl or DEFAULT_FL
    return (CDX_BASE + "?url=" + urllib.parse.quote(domain) + "&matchType=domain"
            + "&from=%d&to=%d&output=text" % (int(frm), int(to))
            + "&fl=" + ",".join(fl)
            + "&collapse=" + urllib.parse.quote(collapse)
            + "&limit=%d" % int(limit))


def parse_cdx_rows(body, fl=None):
    """Text CDX -> (rows, malformed). Each row records url/timestamp/mimetype/statuscode/length.

    `fl` is positional, so a row whose field count differs from the field list is MALFORMED,
    not silently truncated: a URL containing a space shifts every later column, and reading
    a shifted `statuscode` as a length is how a capture gets mis-ranked. Malformed rows are
    counted and reported rather than dropped quietly.
    """
    fl = fl or DEFAULT_FL
    text = body.decode("utf-8", "replace") if isinstance(body, bytes) else body
    rows, malformed = [], []
    for line in (text or "").splitlines():
        line = line.strip()
        if not line:
            continue
        parts = line.split(None, len(fl) - 1)
        if len(parts) != len(fl):
            malformed.append(line[:160])
            continue
        rec = dict(zip(fl, parts))
        # A positional field list shifts every later column when one archived URL contains a
        # literal space, and a shifted `statuscode` read as a length mis-ranks the capture --
        # the same failure the CA lane hit by trusting a sniffed delimiter. Validate the
        # columns that MUST be shape-true and count the row as malformed rather than drop it.
        if (not re.fullmatch(r"\d{14}", rec.get("timestamp", ""))
                or not re.fullmatch(r"\d{3}|-", rec.get("statuscode", ""))
                or not re.fullmatch(r"\d+|-", rec.get("length", ""))):
            malformed.append(line[:160])
            continue
        rows.append({"url": rec.get("original", ""),
                     "timestamp": rec.get("timestamp", ""),
                     "mimetype": rec.get("mimetype", ""),
                     "statuscode": rec.get("statuscode", ""),
                     "length": rec.get("length", "0"),
                     "digest": rec.get("digest", "")})
    return rows, malformed


def classify_cdx(domain, frm, to, status, body, note, transport, limit=0):
    """The four-state verdict for an ENUMERATION. The defect this whole function exists to kill
    is Microsoft's NR-1 class: a refused endpoint written up as an empty result (NULL), or a
    dead route left as UNTRIED. Order matters -- a 200 is parsed structurally BEFORE its
    emptiness is read, because that is exactly the case that was misfiled."""
    slot = {"domain": domain, "window": "%s-%s" % (frm, to), "http_status": status,
            "transport": transport, "note": note, "captures": None, "rows": [],
            "malformed_rows": 0, "capped": False, "verdict": UNANSWERED,
            "cdx_url": cdx_url(domain, frm, to)}
    if not domain:
        slot["verdict"] = UNTRIED
        slot["note"] = "no domain supplied for this slug"
        return slot
    if status == 200 and body is not None:
        # ORDER MATTERS AND IT IS SUBSTRUCTURAL, not cosmetic: parse first. A marker search
        # over the whole body before parsing misfires on real answers -- a first live run
        # classified centene.com 1996-2002 as UNANSWERED because 500 genuine CDX rows contain
        # archived URLs with `robots.txt` and `challenge` in them. Rows are the evidence that
        # the endpoint answered; the apology-page test applies only to a body that yielded none.
        rows, malformed = parse_cdx_rows(body)
        slot["malformed_rows"] = len(malformed)
        if rows:
            slot["verdict"] = ANSWERED
            slot["captures"] = len(rows)
            slot["rows"] = rows
            if limit and len(rows) >= limit:
                # A truncated listing is not a census (the slice-cap defect that reported
                # "0 filings in any stage window" for Citigroup). Here the risk is the softer
                # one: an agent reading `captures=500` as the whole archive for the domain.
                slot["capped"] = True
                slot["note"] = ("%d captures, enumeration hit --limit %d: this is a FLOOR, not "
                                "a census -- raise --limit before concluding anything about "
                                "coverage" % (len(rows), limit))
            return slot
        marker = _markers_hit(body[:8192], CDX_LIE_MARKERS)
        if marker is not None:
            # The Microsoft fixture body is 11,832 bytes of "Internet Archive: Temporarily
            # Offline" HTML; under a 200 it would have parsed as zero rows -> NULL.
            slot["note"] = "status 200 body is an endpoint page, not CDX rows (%r)" % (marker,)
            slot["captures"] = None          # explicitly NOT zero
            return slot
        if not (body or b"").strip():
            slot["verdict"] = NULL       # 200 + empty body: the window WAS tested
            slot["captures"] = 0
            slot["note"] = "CDX answered 200 with zero captures"
            return slot
        slot["verdict"] = UNANSWERED
        slot["note"] = ("CDX returned %d bytes that parsed to zero usable rows and %d "
                        "malformed rows -- unparseable is not empty"
                        % (len(body), len(malformed)))
        return slot
    if status == 0:
        slot["note"] = note or "no HTTP answer"
        return slot
    slot["note"] = note or ("CDX returned status %s with no usable body" % status)
    return slot


# ---------------------------------------------------------------- ranking

def capture_exists(outdir, domain, timestamp):
    """True if this exact capture is already on disk (stem `<domain>_<timestamp>`).

    A re-run that stores the same capture twice creates two 'sources' for one document, which
    is a duplicate-key defect downstream, and it spends rate budget the fleet needs for other
    lanes. Versioning on collision is still the default (no-clobber); `--skip-stored` is the
    idempotent re-pass.
    """
    stem = "%s_%s" % (re.sub(r"[^A-Za-z0-9.-]", "_", domain), timestamp)
    if not os.path.isdir(outdir):
        return ""
    for name in os.listdir(outdir):
        if name.startswith(stem) and not name.endswith((".meta.json", ".md")):
            return name
    return ""


def rank_captures(rows, want, max_bytes=1_500_000):
    """Pick the most promising captures: 200 + text/html + a real body, spread over the window.

    Spread is the point. A density tier asks whether the family returns IN-WINDOW text, so
    eight captures of one 2002 month answer less than one capture per year does. Sorting by
    timestamp and taking one per year first also reproduces the "earliest capture" question
    the probes asked (Centene FR-1, Cencora l.839).
    """
    def keepable(r):
        if r["statuscode"] != "200":
            return False
        if not r["mimetype"].startswith("text/"):
            return False
        try:
            ln = int(r["length"] or 0)
        except ValueError:
            return False
        return 300 <= ln <= max_bytes

    def score(r):
        s = 0
        path = (urllib.parse.urlparse(r["url"]).path or "/").rstrip("/") or "/"
        if path in ("/", "/index", "/index.html", "/index.htm", "/home", "/home.htm",
                    "/default.htm", "/welcome.html"):
            s += 40                      # the company's own front page: highest Tier-1 value
        if r["url"].lower().endswith((".htm", ".html", "/")):
            s += 10
        try:
            if int(r["length"] or 0) >= 2000:
                s += 10
        except ValueError:
            pass
        return s

    good = [r for r in rows if keepable(r)]
    good.sort(key=lambda r: (r["timestamp"], -score(r)))
    by_year, order = {}, []
    for r in good:
        by_year.setdefault(r["timestamp"][:4], []).append(r)
    for year in sorted(by_year):                       # one per year, earliest first
        order.append(by_year[year][0])
    picked = list(order)
    if len(picked) < want:                             # fill from the rest, best score first
        rest = sorted([r for r in good if r not in picked],
                      key=lambda r: (-score(r), r["timestamp"]))
        picked += rest[:want - len(picked)]
    return picked[:want], {"fetchable": len(good), "non200": len(rows) - len(good)}


def snapshot_url(timestamp, original):
    # `id_` asks for the archived bytes as captured, without IA's injected toolbar; the
    # toolbar would be stored as if it were the company's page.
    return SNAP_BASE + timestamp + "id_/" + original


def ext_for(mimetype):
    return {"text/html": ".html", "text/plain": ".txt", "text/css": ".css",
            "application/xml": ".xml", "text/xml": ".xml"}.get(mimetype, ".bin")


# ---------------------------------------------------------------- provenance

def version_aside(path):
    """Keep the previous run record instead of silently overwriting it (sec_intake house rule)."""
    if not os.path.exists(path) or os.path.getsize(path) <= 0:
        return None
    stamp = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    prev = "%s.prev-%s%s" % (os.path.splitext(path)[0], stamp, os.path.splitext(path)[1])
    os.replace(path, prev)
    return prev


def no_clobber_path(path):
    """Never overwrite an existing body/sidecar: version a NEW name beside it instead.

    Renaming the old bytes (as version_aside does for run records) would move evidence that
    another agent may already cite, so for corpus bodies the new capture takes `_v2`, `_v3`.
    """
    if not os.path.exists(path):
        return path, None
    root, ext = os.path.splitext(path)
    n = 2
    while os.path.exists("%s_v%d%s" % (root, n, ext)):
        n += 1
    new = "%s_v%d%s" % (root, n, ext)
    return new, path


def _write_verified(path, data):
    """Write, then stat and re-hash it. A function that returns success without producing
    the bytes it claims is the defect class s15.5 applies to retrieval."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    size = os.stat(path).st_size
    if size <= 0:
        raise OSError("wrote %s but the file is 0 bytes" % path)
    return size


def write_pair(outdir, base, body, sidecar):
    """Sidecar BEFORE body: an interrupted run then leaves a sidecar with no body (which
    `audit` reports) rather than orphan bytes with no provenance (which reads as evidence)."""
    path = os.path.join(outdir, base)
    path, clobbered = no_clobber_path(path)
    side = dict(sidecar)
    side["path"] = os.path.basename(path)
    if clobbered:
        side["no_clobber"] = "existing %s left untouched, wrote %s" % (
            os.path.basename(clobbered), os.path.basename(path))
    side["sha256"] = hashlib.sha256(body).hexdigest()
    side["bytes"] = len(body)
    spath = path + ".meta.json"
    spath, sclob = no_clobber_path(spath)
    _write_verified(spath, (json.dumps(side, indent=1) + "\n").encode("utf-8"))
    _write_verified(path, body)
    return path, spath, side


# ---------------------------------------------------------------- fetch

def fetch_snapshot(row, outdir, meta, max_bytes=1_500_000, tries=2):
    """Fetch one archived capture. Returns a disposition dict; never writes a refusal as a body."""
    url = snapshot_url(row["timestamp"], row["url"])
    s, raw, note, transport = http_get(url, tries=tries)
    rec = {"url": row["url"], "timestamp": row["timestamp"], "requested_url": url,
           "http_status": s, "mimetype": row["mimetype"], "cdx_length": row["length"],
           "transport": transport, "note": note, "bytes": 0, "path": "", "sha256": "",
           "verdict": UNANSWERED}
    if s == 200 and raw:
        marker = _markers_hit(raw, SNAPSHOT_LIE_MARKERS)
        if marker is not None:
            rec["note"] = "IA interstitial instead of archived bytes (%r)" % (marker,)
            rec["verdict"] = UNANSWERED
        elif len(raw) > max_bytes:
            rec["note"] = "%d bytes over --max-bytes %d, not stored" % (len(raw), max_bytes)
            rec["verdict"] = UNANSWERED
        else:
            base = "%s_%s%s" % (re.sub(r"[^A-Za-z0-9.-]", "_", meta["domain"]),
                                row["timestamp"], ext_for(row["mimetype"]))
            side = {"url": row["url"], "timestamp": row["timestamp"], "requested_url": url,
                    "http_status": s, "bytes": len(raw), "sha256": "", "transport": transport,
                    "verdict": ANSWERED, "mimetype": row["mimetype"],
                    "cdx_length": row["length"], "cdx_digest": row["digest"],
                    "family": "(b) web archives", "fetched_utc":
                    time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
            side.update({k: meta.get(k) for k in ("domain", "window", "slug", "company_dir",
                                                  "why", "source_line", "cdx_url")})
            path, spath, written = write_pair(outdir, base, raw, side)
            rec.update({"verdict": ANSWERED, "bytes": written["bytes"], "path": path,
                        "sha256": written["sha256"], "sidecar": spath})
            return rec
    if s == 200 and not raw:
        rec["note"] = "status 200 with a zero-byte body: refused, not empty-by-finding"
    rec["verdict"] = UNANSWERED
    return rec


# ---------------------------------------------------------------- accounting

def tally(rows, attempted=None):
    """The accounting identity as a detector, not a print (sec_intake `tally` shape).

    `attempted` is the number of slots the PLAN said to process, passed in by the caller: a
    row that never reached a bucket must break the identity, which is impossible if the
    divisor is derived from the rows themselves.
    """
    counts = {st: 0 for st in STATES}
    by_slot, dups = {}, []
    for r in rows:
        counts[r["verdict"]] += 1
        slot = "%s|%s|%s" % (r.get("slug", ""), r.get("domain", ""), r.get("window", ""))
        if slot in by_slot:
            dups.append("%s in %s and %s" % (slot, by_slot[slot], r["verdict"]))
        else:
            by_slot[slot] = r["verdict"]
    raw = sum(counts.values())
    unique = len(by_slot)
    attempted = len(rows) if attempted is None else attempted
    msg = ("answered(%d) + null(%d) + unanswered(%d) + untried(%d) = %d raw / %d unique slots "
           "vs attempted(%d) -> %s%s"
           % (counts[ANSWERED], counts[NULL], counts[UNANSWERED], counts[UNTRIED], raw,
              unique, attempted, "OK" if unique == attempted and not dups else "BROKEN",
              "" if raw == unique else " (raw inflated by repeated slots, see DOUBLE-COUNTED)"))
    return unique == attempted and not dups, msg, counts, dups


def _verify_slot(r):
    """The refusal-cannot-say-zero guard. An UNANSWERED slot that carries a capture count --
    including 0 -- is a defect, because the window was never tested."""
    bad = []
    if r["verdict"] == UNANSWERED and r.get("captures") is not None:
        bad.append("UNANSWERED slot %s carries captures=%r" % (r.get("domain"), r["captures"]))
    if r["verdict"] == ANSWERED and r.get("bytes", 0) <= 0:
        bad.append("ANSWERED slot has no bytes")
    if r["verdict"] == UNANSWERED and not r.get("remedy"):
        bad.append("UNANSWERED slot %s names no remedy" % r.get("domain"))
    if r["verdict"] == ANSWERED:
        p = r.get("path")
        if not p or not os.path.exists(p):
            bad.append("ANSWERED slot %s points at a missing body %r" % (r.get("domain"), p))
        elif not os.path.exists(p + ".meta.json"):
            bad.append("ANSWERED slot %s has a body with no sidecar" % r.get("domain"))
    return bad


def print_slots(rows):
    """Four states, kept distinct. The guard below is the point: an UNANSWERED slot that
    arrived with a capture count (including 0) is the Microsoft NR-1 defect, and this refuses
    to print it rather than letting "0 captures" reach a dossier."""
    header = ("  %-13s %-21s %-10s %-6s %-9s %-6s %-9s %s"
              % ("slug", "domain", "window", "http", "captures", "bytes", "state",
                 "note/remedy"))
    lines = []
    for r in sorted(rows, key=lambda x: (x.get("slug", ""), x.get("domain", ""),
                                         x.get("window", ""))):
        if r["verdict"] == UNANSWERED:
            assert r.get("captures") is None, (
                "refused route carries a capture count: %r" % r)
            cap = "-"
        elif r["verdict"] == UNTRIED:
            cap = "untried"
        else:
            cap = str(r.get("captures"))
        lines.append("  %-13s %-21s %-10s %-6s %-9s %-6s %-9s %s" % (
            r.get("slug", ""), r.get("domain", ""), r.get("window", ""),
            r.get("http_status") or "-", cap, r.get("bytes", 0) or 0, r["verdict"],
            (r.get("remedy") or r.get("note") or "")[:80]))
    print(header)
    for ln in lines:
        print(ln)


# ---------------------------------------------------------------- intake

def resolve_company_dir(company_root, slug):
    hits = sorted(d for d in os.listdir(company_root)
                  if d.lower() == ("company_%s" % slug) or d.lower().endswith("_" + slug))
    if not hits:
        return None
    return os.path.join(company_root, hits[0])


def load_domains(path=DOMAINS_FILE):
    j = json.load(open(path, encoding="utf-8"))
    return j.get("slugs", j), j.get("_provenance_note", "")


def run_slug(slug, cdir, entries, per_domain, max_bytes, dry_run, notes, limit=500,
             skip_stored=False):
    """One slug: enumerate every cited domain, fetch a bounded set, return dispositions.

    EVERY entry lands in exactly one state, including the ones this function refuses to call
    (no domain, dry run, budget spent) -- an entry that returns nothing is how a family goes
    silently UNTRIED.
    """
    rows = []
    if not entries:
        rows.append({"slug": slug, "domain": "", "window": "", "http_status": 0,
                     "captures": None, "bytes": 0, "path": "", "verdict": UNTRIED,
                     "note": "no cited domain in tools/web_domains.json for this slug",
                     "remedy": remedy_for(UNTRIED, 0, "")})
        return rows
    outdir = os.path.join(cdir, "sources", "web_archive") if cdir else None
    if cdir is None:
        for e in entries:
            rows.append({"slug": slug, "domain": e.get("domain", ""),
                         "window": e.get("window", ""), "http_status": 0, "captures": None,
                         "bytes": 0, "path": "", "verdict": UNTRIED,
                         "note": "no company dir resolved for slug %r" % slug,
                         "remedy": remedy_for(UNTRIED, 0, "")})
        return rows
    for e in entries:
        dom = (e.get("domain") or "").strip()
        win = (e.get("window") or "").strip()
        m = re.match(r"^(\d{4})\s*[-.]\s*(\d{4})$", win)
        base = {"slug": slug, "domain": dom, "window": win, "http_status": 0,
                "captures": None, "bytes": 0, "path": "", "verdict": UNTRIED,
                "note": "", "remedy": "", "why": e.get("why", ""),
                "source_line": e.get("source_line", "")}
        if not dom or not m:
            base["verdict"] = UNTRIED
            base["note"] = ("no domain supplied" if not dom else
                            "window %r is not YYYY-YYYY, so nothing was tested" % win)
            base["remedy"] = remedy_for(UNTRIED, 0, "")
            rows.append(base)
            continue
        frm, to = int(m.group(1)), int(m.group(2))
        if dry_run:
            base["verdict"] = UNTRIED
            base["note"] = "dry run: no request was made, so the window is untested"
            base["remedy"] = "re-run without --dry-run"
            rows.append(base)
            continue
        s, body, note, transport = http_get(cdx_url(dom, frm, to, limit))
        slot = classify_cdx(dom, frm, to, s, body, note, transport, limit)
        base.update({"http_status": slot["http_status"], "transport": slot["transport"],
                     "cdx_url": slot["cdx_url"], "note": slot["note"],
                     "captures": slot["captures"], "malformed_rows": slot["malformed_rows"],
                     "capped": slot["capped"]})
        if slot["verdict"] == NULL:
            base["verdict"] = NULL
            base["remedy"] = remedy_for(NULL, s, note)
            rows.append(base)
            _write_state_artifact(outdir, base)
            continue
        if slot["verdict"] != ANSWERED:
            base["verdict"] = UNANSWERED
            base["captures"] = None
            base["remedy"] = remedy_for(UNANSWERED, s, note)
            rows.append(base)
            _write_state_artifact(outdir, base)
            continue
        picked, why = rank_captures(slot["rows"], per_domain, max_bytes)
        base["enumerated"] = slot["captures"]
        base["fetch_attempted"] = len(picked)
        base["fetch_ranking"] = "%d of %d captures keptable (non-200 dropped: %d)" % (
            why["fetchable"], slot["captures"], why["non200"])
        meta = {"domain": dom, "window": win, "slug": slug, "company_dir": cdir,
                "why": e.get("why", ""), "source_line": e.get("source_line", ""),
                "cdx_url": slot["cdx_url"]}
        stored, failed, first, already = 0, 0, None, 0
        for r in picked:
            if skip_stored:
                ex = capture_exists(outdir, dom, r["timestamp"])
                if ex:
                    already += 1
                    notes.append("%s %s %s SKIPPED-ALREADY-ON-DISK (%s)" % (slug, dom,
                                                                            r["timestamp"], ex))
                    continue
            d = fetch_snapshot(r, outdir, meta, max_bytes)
            if d["verdict"] == ANSWERED:
                stored += 1
                if first is None:
                    first = d
            else:
                failed += 1
            notes.append("%s %s %s %s" % (slug, dom, r["timestamp"], d["verdict"]))
        base["stored"] = stored
        base["already_on_disk"] = already
        base["fetch_failed"] = failed
        if first:
            base.update({"bytes": first["bytes"], "path": first["path"],
                         "sha256": first["sha256"], "example_timestamp": first["timestamp"],
                         "example_status": first["http_status"], "url": first["url"]})
        elif already:
            # The family returned, the bytes were already filed by an earlier pass: still
            # ANSWERED for tier purposes, and the sidecar on disk carries the provenance.
            ex = os.path.join(outdir, capture_exists(outdir, dom, picked[0]["timestamp"]))
            base["path"] = ex
            base["bytes"] = os.stat(ex).st_size
            base["example_timestamp"] = picked[0]["timestamp"]
            base["example_status"] = 200
            base["url"] = picked[0]["url"]
        # A family counts toward a tier only if bytes are ON DISK: enumeration that answered
        # but yielded no stored body is UNANSWERED, never a tier-able ANSWERED.
        # BUT: an endpoint that ANSWERED and holds no fetchable capture in the window is a
        # TESTED null (NULL), not a refusal -- filing it UNANSWERED would be the mirror image
        # of the defect this tool exists to remove (it would send a re-grade agent to retry a
        # route that already gave its answer).
        if not (stored or already):
            if not picked:
                base["verdict"] = NULL
                base["captures"] = base["enumerated"]
                base["note"] = ("CDX answered 200: %s captures in the window, 0 fetchable as "
                                "200 text (non-200 status or non-text mimetype) -- the window "
                                "WAS tested and holds no Tier-1 web-archive bytes"
                                % base["enumerated"])
                base["remedy"] = ("no retry will change this: read the CDX rows in _RUN.json "
                                  "for the status codes, or try the alias domains")
            else:
                base["verdict"] = UNANSWERED
                base["captures"] = None
                base["note"] = ("CDX enumerated %s captures but 0 bodies were stored: all %d "
                                "fetch attempts were refused" % (base["enumerated"], failed))
                base["remedy"] = remedy_for(UNANSWERED, 200, base["note"])
        else:
            base["verdict"] = ANSWERED
            base["remedy"] = ""
        rows.append(base)
        if base["verdict"] != ANSWERED:
            _write_state_artifact(outdir, base)
    return rows


def _write_state_artifact(outdir, r):
    """A NULL/UNANSWERED artefact on disk, so a dead route is a FILED FINDING with a date
    rather than an absence an agent reads as 'the archive is empty'."""
    if r["verdict"] not in (NULL, UNANSWERED, UNTRIED) or r["verdict"] == ANSWERED:
        return ""
    os.makedirs(outdir, exist_ok=True)
    name = "%s_%s.%s.md" % (re.sub(r"[^A-Za-z0-9.-]", "_", r.get("domain") or "no-domain"),
                            (r.get("window") or "nowindow").replace("-", "_"), r["verdict"])
    path = os.path.join(outdir, name)
    body = ("# family (b) web archives: %s -- %s %s\n\n"
            "- verdict: %s\n- CDX/fetch status: %s\n- captures: %s\n- note: %s\n"
            "- remedy: %s\n- cdx_url: %s\n- source_line: %s\n- recorded_utc: %s\n"
            % (r["verdict"], r.get("domain") or "(no domain)", r.get("window") or "",
               r["verdict"], r.get("http_status") or "-",
               "NOT TESTED (refused)" if r["verdict"] == UNANSWERED else r.get("captures"),
               r.get("note", ""), r.get("remedy", ""), r.get("cdx_url", ""),
               r.get("source_line", ""), time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())))
    path, _ = no_clobber_path(path)
    _write_verified(path, body.encode("utf-8"))
    return path


def write_run(cdir, slug, rows, max_requests, attempted=None):
    """`_RUN.json` with the accounting identity, versioned aside if a run already landed."""
    ok, msg, counts, dups = tally(rows, attempted)
    d = os.path.join(cdir, "sources", "web_archive")
    os.makedirs(d, exist_ok=True)
    path = os.path.join(d, "_RUN.json")
    prev = version_aside(path)
    slim = []
    for r in rows:
        s = {k: v for k, v in r.items() if k not in ("rows",)}
        s.pop("path", None)
        s["path"] = r.get("path", "")
        slim.append(s)
    run = {"tool": "cdx_intake.py", "family": "(b) web archives", "slug": slug,
           "company_dir": cdir, "generated_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
           "attempted": len(rows) if attempted is None else attempted,
           "ANSWERED": counts[ANSWERED], "NULL": counts[NULL],
           "UNANSWERED": counts[UNANSWERED], "UNTRIED": counts[UNTRIED],
           "identity": msg, "identity_ok": ok, "double_counted": dups,
           "requests_used": _budget["used"], "max_requests": max_requests,
           "policy": {"polite_seconds_per_host": POLITE_SECONDS,
                      "transport": "ok / ok-INSECURE stamped per sidecar",
                      "never_write_empty_as_null": True,
                      "UNANSWERED_emits_no_capture_count": True},
           "rows": slim}
    for r in rows:
        bad = _verify_slot(r)
        if bad:
            run.setdefault("verify_defects", []).extend(bad)
    _write_verified(path, (json.dumps(run, indent=1) + "\n").encode("utf-8"))
    if prev:
        run["previous_run_versioned_aside"] = prev
    return path, ok, msg, counts


# ---------------------------------------------------------------- audit

def audit_dir(d):
    """Re-verify on-disk bytes against their sidecars: orphan body, missing sidecar, sha
    mismatch, size mismatch, and a sidecar whose verdict is ANSWERED but has no bytes."""
    findings = []
    if not os.path.isdir(d):
        return ["no such dir: %s" % d]
    for name in sorted(os.listdir(d)):
        p = os.path.join(d, name)
        if not os.path.isfile(p) or name.startswith("_") or name.endswith(".meta.json") \
                or name.endswith(".sidecar.json") \
                or name.endswith(".md") or ".prev-" in name:
            continue
        sp = p + ".meta.json"
        legacy = p + ".sidecar.json"
        if not os.path.exists(sp):
            # Microsoft's two family-(b) artefacts were written by an ad-hoc curl pass and use
            # the `.sidecar.json` suffix. They are someone else's files: report the shape, do
            # not call a documented sibling an orphan.
            if os.path.exists(legacy):
                findings.append("LEGACY-SIDECAR-SHAPE (not a defect): %s carries %s, not "
                                ".meta.json" % (name, os.path.basename(legacy)))
                continue
            findings.append("orphan body, no sidecar: %s" % name)
            continue
        try:
            side = json.load(open(sp, encoding="utf-8"))
        except ValueError:
            findings.append("unreadable sidecar: %s" % name)
            continue
        raw = open(p, "rb").read()
        h = hashlib.sha256(raw).hexdigest()
        if side.get("sha256") != h:
            findings.append("sha256 mismatch: %s sidecar=%s... disk=%s..." %
                            (name, str(side.get("sha256"))[:10], h[:10]))
        if side.get("bytes") != len(raw):
            findings.append("bytes mismatch: %s sidecar=%s disk=%d" %
                            (name, side.get("bytes"), len(raw)))
        for k in ("url", "timestamp", "requested_url", "http_status", "transport", "verdict"):
            if k not in side:
                findings.append("sidecar missing required key %r: %s" % (k, name))
    return findings


# ---------------------------------------------------------------- selftest

def selftest():
    """s15.5: the intake proves itself against the exact defects this project previously
    missed, offline, with no network. Status at build is printed as a defect -> fired table."""
    global http_get
    fails = []
    checks = {"n": 0}
    print("cdx_intake selftest (no network)")

    def check(defect, fired, detail=""):
        """fired=True means the planted defect WAS caught by the tool."""
        checks["n"] += 1
        print("  %-58s %-14s %s" % (defect, "FIRED" if fired else "STAYS CLEAN", detail))
        if not fired:
            fails.append(defect)

    def control(name, clean, detail=""):
        """A negative control must STAY CLEAN; a finding here is a false positive, which is
        the defect §15.5's control exists to catch (gates.py invented 43 width-drift
        findings on Amazon by sniffing a dialect from a truncated sample)."""
        checks["n"] += 1
        print("  %-58s %-14s %s" % (name, "STAYS CLEAN" if clean else "FALSE POSITIVE", detail))
        if not clean:
            fails.append(name)

    real_get = http_get
    tmp = tempfile.mkdtemp(prefix="cdx_intake_selftest_")
    cdir = os.path.join(tmp, "company_900_selftest")
    outdir = os.path.join(cdir, "sources", "web_archive")
    os.makedirs(outdir)

    def fake(responses):
        calls = {"n": 0}

        def _f(url, tries=3, timeout=60):
            i = min(calls["n"], len(responses) - 1)
            calls["n"] += 1
            return responses[i]
        return _f

    GOOD_CDX = (200, b"19991105102101 http://www.centene.com:80/ text/html 200 1701 AAAA\n"
                     b"20000307064106 http://www.centene.com:80/ text/html 200 1690 BBBB\n",
                "ok", "ok")
    GOOD_BODY = (200, b"<html><body>Centene Home Page 1999</body></html>", "ok", "ok")

    try:
        # (a) a 503 -- and the Microsoft fixture body under a 200 -- must land as UNANSWERED.
        slot = classify_cdx("centene.com", 1996, 2002, 503, b"", "HTTP 503", "ok")
        check("(a) CDX 503 -> UNANSWERED, never NULL", slot["verdict"] == UNANSWERED
              and slot["captures"] is None, slot["note"][:60])
        ms = os.path.join(REPO, "founders_playbook", "01_companies", "company_011_microsoft",
                          "sources", "web_archive", "cdx_microsoft_com_earliest_200.json")
        fixture = open(ms, "rb").read() if os.path.exists(ms) else None
        check("(a) Microsoft 503 fixture found on disk", fixture is not None,
              "" if fixture else ms)
        if fixture is not None:
            s200 = classify_cdx("microsoft.com", 1994, 2001, 200, fixture, "ok", "ok")
            check("(a) IA 'Temporarily Offline' under status 200 -> UNANSWERED",
                  s200["verdict"] == UNANSWERED and s200["captures"] is None,
                  "the NR-1 defect: HTML banner would parse as 0 rows -> NULL")
            s503 = classify_cdx("microsoft.com", 1994, 2001, 503, fixture, "HTTP 503", "ok")
            check("(a) same fixture at its recorded status 503 -> UNANSWERED",
                  s503["verdict"] == UNANSWERED)
        check("(a) UNANSWERED names a remedy", bool(remedy_for(UNANSWERED, 503, "HTTP 503")),
              remedy_for(UNANSWERED, 503, "HTTP 503")[:60])

        # (b) empty-but-successful CDX -> NULL, and NOT UNANSWERED.
        slot = classify_cdx("coordinatedcare.com", 1996, 2002, 200, b"", "ok", "ok")
        check("(b) CDX 200 + zero bytes -> NULL", slot["verdict"] == NULL, slot["note"][:60])
        slot = classify_cdx("coordinatedcare.com", 1996, 2002, 200, b"   \n\n", "ok", "ok")
        check("(b) CDX 200 + whitespace only -> NULL", slot["verdict"] == NULL)
        slot = classify_cdx("x.com", 1996, 2002, 200, b"garbage line with no fields\n",
                            "ok", "ok")
        check("(b) unparseable-but-nonempty -> UNANSWERED, not NULL",
              slot["verdict"] == UNANSWERED)
        # bcbskc.org 1996-2014 measured live: CDX answered ONE capture, a 410 robots.txt.
        # The window was tested and holds nothing fetchable -- a null about the archive, not
        # a refusal by it.
        ONLY_NON200 = (200, b"20080827071737 http://bcbskc.org:80/robots.txt text/html 410 267"
                        b" D\n", "ok", "ok")
        http_get = fake([ONLY_NON200])
        rows_n = run_slug("selftest", cdir, [{"domain": "bcbskc.org", "window": "1996-2014",
                                              "why": "w", "source_line": "l"}],
                          per_domain=3, max_bytes=1_500_000, dry_run=False, notes=[])
        check("(b) answered-but-nothing-fetchable -> NULL, not UNANSWERED",
              rows_n[0]["verdict"] == NULL and rows_n[0]["captures"] == 1,
              rows_n[0]["note"][:60])
        capped = classify_cdx("x.com", 1996, 2002, 200, GOOD_CDX[1], "ok", "ok", limit=2)
        check("(b) an enumeration that hits --limit is labelled a FLOOR, not a census",
              capped["verdict"] == ANSWERED and capped["capped"] and "FLOOR" in capped["note"],
              capped["note"][:60])
        control("(b) the same answer under a generous --limit is not called capped",
                not classify_cdx("x.com", 1996, 2002, 200, GOOD_CDX[1], "ok", "ok",
                                 limit=500)["capped"])

        # (c) a stored body must have a sidecar and a matching sha256.
        http_get = fake([GOOD_CDX, GOOD_BODY, GOOD_BODY, GOOD_BODY])
        _budget.update({"left": 50, "cap": 50, "used": 0})
        rows = run_slug("selftest", cdir, [{"domain": "centene.com", "window": "1996-2002",
                                            "why": "fixture", "source_line": "fixture l.1"}],
                        per_domain=2, max_bytes=1_500_000, dry_run=False, notes=[])
        check("(c) fixture run stores bytes", rows[0]["verdict"] == ANSWERED
              and rows[0]["bytes"] > 0, str(rows[0].get("path", ""))[-40:])
        f = audit_dir(outdir)
        control("(c) clean pair passes audit", not f, "; ".join(f)[:80])
        planted = [p for p in os.listdir(outdir) if not p.endswith((".meta.json", ".md"))
                   and not p.startswith("_")][0]
        with open(os.path.join(outdir, planted), "wb") as fh:
            fh.write(b"tampered bytes after the fact")
        f = audit_dir(outdir)
        check("(c) planted sha256 mismatch IS caught", any("sha256" in x for x in f),
              "; ".join(f)[:80])
        with open(os.path.join(outdir, planted), "wb") as fh:
            fh.write(open(os.path.join(outdir, planted + ".meta.json"),
                          encoding="utf-8").read().encode("utf-8"))
        os.replace(os.path.join(outdir, planted), os.path.join(outdir, "orphan_no_sidecar.html"))
        f = audit_dir(outdir)
        check("(c) planted orphan body IS caught", any("orphan" in x for x in f),
              "; ".join(f)[:80])

        # (d) an existing file must not be overwritten.
        for p in list(os.listdir(outdir)):
            os.remove(os.path.join(outdir, p))
        sentinel = b"CANONICAL EARLIER RUN -- DO NOT OVERWRITE"
        first_body = os.path.join(outdir, "centene-com_19991105102101.html")
        _write_verified(first_body, sentinel)
        http_get = fake([GOOD_CDX, GOOD_BODY, GOOD_BODY])
        _budget.update({"left": 50, "cap": 50, "used": 0})
        rows = run_slug("selftest", cdir, [{"domain": "centene.com", "window": "1996-2002",
                                            "why": "fixture", "source_line": "fixture l.1"}],
                        per_domain=2, max_bytes=1_500_000, dry_run=False, notes=[])
        check("(d) pre-existing bytes untouched",
              open(first_body, "rb").read() == sentinel,
              os.path.basename(rows[0].get("path", "")))
        check("(d) new capture versioned beside it", rows[0].get("path", "") != first_body
              and os.path.exists(rows[0].get("path", "")),
              "wrote %s" % os.path.basename(rows[0].get("path", "")))
        calls_seen = {"n": 0}

        def counting(url, tries=3, timeout=60):
            # `fake` bypasses the transport, so it never moves _budget; this step counts the
            # HTTP-level calls themselves, which is the unit the claim is about.
            calls_seen["n"] += 1
            return GOOD_CDX if "/cdx/search/cdx" in url else GOOD_BODY
        http_get = counting
        rows = run_slug("selftest", cdir, [{"domain": "centene.com", "window": "1996-2002",
                                             "why": "fixture", "source_line": "fixture l.1"}],
                        per_domain=2, max_bytes=1_500_000, dry_run=False, notes=[],
                        skip_stored=True)
        check("(d) --skip-stored fetches nothing already on disk, slot stays ANSWERED",
              rows[0]["verdict"] == ANSWERED and rows[0]["already_on_disk"] == 2
              and rows[0]["stored"] == 0 and calls_seen["n"] == 1,
              "%d HTTP call (the CDX enumeration), %d stored, %d already on disk"
              % (calls_seen["n"], rows[0]["stored"], rows[0]["already_on_disk"]))

        # (e) identity: stored+null+unanswered+untried == attempted, and it FIRES when broken.
        for p in list(os.listdir(outdir)):
            os.remove(os.path.join(outdir, p))
        seq = [GOOD_CDX, GOOD_BODY, GOOD_BODY, (200, b"", "ok", "ok"),
               (503, b"", "HTTP 503", "ok"), (0, None, "timed out", "ok")]
        entries = [{"domain": "centene.com", "window": "1996-2002", "why": "w",
                    "source_line": "l"},
                   {"domain": "coordinatedcare.com", "window": "1996-2002", "why": "w",
                    "source_line": "l"},
                   {"domain": "anthem.com", "window": "1996-2002", "why": "w",
                    "source_line": "l"},
                   {"domain": "wellpoint.com", "window": "1996-2002", "why": "w",
                    "source_line": "l"},
                   {"domain": "", "window": "1996-2002", "why": "no domain",
                    "source_line": "l"}]

        def scripted(url, tries=3, timeout=60):
            if "/cdx/search/cdx" in url:
                i = {"centene.com": 0, "coordinatedcare.com": 3, "anthem.com": 4,
                     "wellpoint.com": 5}[url.split("url=")[1].split("&")[0]]
                return seq[i]
            return GOOD_BODY
        http_get = scripted
        _budget.update({"left": 60, "cap": 60, "used": 0})
        rows = run_slug("selftest", cdir, entries, per_domain=2, max_bytes=1_500_000,
                        dry_run=False, notes=[])
        ok, msg, counts, dups = tally(rows)
        check("(e) identity holds on a four-state run", ok, msg)
        check("(e) all four states present and distinct",
              counts[ANSWERED] == 1 and counts[NULL] == 1 and counts[UNANSWERED] == 2
              and counts[UNTRIED] == 1, str(counts))
        check("(e) NULL is not UNANSWERED and vice versa", counts[NULL] == 1
              and all(r["captures"] is None for r in rows if r["verdict"] == UNANSWERED))
        dropped = rows[:-1]
        ok2, msg2, _, _ = tally(dropped, attempted=len(rows))
        check("(e) identity FIRES when a row goes missing", not ok2, msg2[:70])
        dupped = rows + [dict(rows[0])]
        ok3, msg3, _, d3 = tally(dupped)
        check("(e) identity FIRES on a double-counted slot", not ok3 and bool(d3), msg3[:70])
        bad_slot = dict(rows[2])
        bad_slot["captures"] = 0
        check("(e) refusal carrying captures=0 is caught", bool(_verify_slot(bad_slot)),
              str(_verify_slot(bad_slot))[:70])
        buf = _Capture()
        with buf:
            print_slots(rows)
        printed = buf.getvalue()
        un_lines = [ln for ln in printed.splitlines() if " UNANSWERED " in ln]
        check("(e) UNANSWERED lines print no capture count", bool(un_lines)
              and all(ln.split()[4] == "-" for ln in un_lines),
              "cols=" + ",".join(ln.split()[4] for ln in un_lines[:3]))
        check("(e) the printer RAISES on a refusal carrying captures=0",
              _raises(lambda: print_slots([dict(rows[2], captures=0)])))
        run_path, ok4, _, _ = write_run(cdir, "selftest", rows, 60)
        j = json.load(open(run_path, encoding="utf-8"))
        check("(e) _RUN.json written with the identity", ok4 and j["identity_ok"],
              j["identity"][:70])
        check("(e) _RUN.json carries no UNANSWERED-with-count",
              not j.get("verify_defects"), str(j.get("verify_defects", ""))[:80])

        # NEGATIVE CONTROL: the clean fixture must stay clean.
        for p in list(os.listdir(outdir)):
            os.remove(os.path.join(outdir, p))
        http_get = fake([GOOD_CDX, GOOD_BODY, GOOD_BODY])
        _budget.update({"left": 50, "cap": 50, "used": 0})
        rows = run_slug("selftest", cdir, [{"domain": "clean.com", "window": "1996-2002",
                                            "why": "control", "source_line": "l"}],
                        per_domain=2, max_bytes=1_500_000, dry_run=False, notes=[])
        control("NEGATIVE CONTROL: clean run produces zero findings",
                not audit_dir(outdir) and all(not _verify_slot(r) for r in rows)
                and rows[0]["verdict"] == ANSWERED,
                "; ".join(audit_dir(outdir))[:70])

        # extra planted defects this project has hit before
        ldir = os.path.join(tmp, "legacy_shape")
        os.makedirs(ldir, exist_ok=True)
        open(os.path.join(ldir, "cdx_probe.json"), "wb").write(b"{}")
        open(os.path.join(ldir, "cdx_probe.json.sidecar.json"), "wb").write(b"{}")
        f = audit_dir(ldir)
        control("(c) a legacy `.sidecar.json` sibling is a shape note, not an orphan finding",
                any(x.startswith("LEGACY-SIDECAR-SHAPE") for x in f)
                and not [x for x in f if not x.startswith("LEGACY-SIDECAR-SHAPE")],
                "; ".join(f)[:70])
        check("(a) str marker cannot enter CDX_LIE_MARKERS",
              all(isinstance(m, bytes) for m in CDX_LIE_MARKERS + SNAPSHOT_LIE_MARKERS))
        r = classify_cdx("x.com", 1996, 2002, 200, b"19960101 http://a b c d e f g h i\n",
                         "ok", "ok")
        check("(a) malformed row counted, never silently dropped",
              r["malformed_rows"] == 1, "malformed=%d" % r["malformed_rows"])
        http_get = fake([(0, None, "request budget exhausted (--max-requests 60 reached)",
                          "")])
        slot = classify_cdx("x.com", 1996, 2002, *http_get("u"))
        check("(a) budget exhaustion -> UNANSWERED, not NULL",
              slot["verdict"] == UNANSWERED and slot["captures"] is None,
              slot["note"][:60])
        check("(a) budget remedy names --max-requests",
              "max-requests" in remedy_for(UNANSWERED, 0, "budget exhausted"))
        rows_dry = run_slug("selftest", cdir, [{"domain": "centene.com",
                                                "window": "1996-2002", "why": "w",
                                                "source_line": "l"}],
                            per_domain=1, max_bytes=10, dry_run=True, notes=[])
        check("(e) dry run -> UNTRIED, no bytes claimed",
              rows_dry[0]["verdict"] == UNTRIED and rows_dry[0]["bytes"] == 0)
        picked, _ = rank_captures([{"timestamp": t + "0101", "url": "http://a/%s" % t,
                                    "mimetype": "text/html", "statuscode": "200",
                                    "length": "5000", "digest": ""} for t in
                                   ("1996", "1997", "1998", "1999", "2000")], want=3)
        check("(b) ranking spreads across the window, not one year",
              len({p["timestamp"][:4] for p in picked}) == 3,
              " ".join(p["timestamp"][:4] for p in picked))
        check("(b) non-200 and tiny captures are not fetched",
              not [p for p in rank_captures([{"timestamp": "19960101", "url": "http://a",
                                               "mimetype": "text/html", "statuscode": "302",
                                               "length": "5000", "digest": ""}], want=3)[0]])
    finally:
        http_get = real_get

    print("\nselftest: %d check(s), %d defect(s) did not fire" % (checks["n"], len(fails)))
    print("SELFTEST %s%s" % ("PASS" if not fails else "FAIL",
                             "" if not fails else " -- failed: " + ", ".join(fails[:8])))
    return 0 if not fails else 1


def _raises(fn):
    """True if fn() raises -- used to prove the refusal-cannot-say-zero guard is live."""
    try:
        fn()
    except (AssertionError, Exception):
        return True
    return False


class _Capture:
    """contextlib-free stdout capture for the print guard."""

    def __init__(self):
        self.buf, self.old = [], None

    def __enter__(self):
        self.old = sys.stdout
        sys.stdout = self

    def __exit__(self, *a):
        sys.stdout = self.old

    def write(self, s):
        self.buf.append(s)

    def flush(self):
        pass

    def getvalue(self):
        return "".join(self.buf)


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(prog="cdx_intake.py", description=__doc__.split("\n")[1])
    ap.add_argument("cmd", nargs="?", default="run",
                    choices=["run", "enumerate", "audit", "selftest"])
    ap.add_argument("--self-test", "--selftest", dest="self_test", action="store_true")
    ap.add_argument("--slug", default="", help="comma-separated company slugs, e.g. centene,cencora")
    ap.add_argument("--domains-file", default=DOMAINS_FILE)
    ap.add_argument("--company-root", default=COMPANY_ROOT)
    ap.add_argument("--company-dir", default="", help="override dir resolution for a single slug")
    ap.add_argument("--domain", default="")
    ap.add_argument("--frm", "--from", dest="frm", type=int, default=1994)
    ap.add_argument("--to", dest="to", type=int, default=2002)
    ap.add_argument("--limit", type=int, default=500)
    ap.add_argument("--per-domain", type=int, default=8, help="bodies to store per domain")
    ap.add_argument("--max-bytes", type=int, default=1_500_000)
    ap.add_argument("--max-requests", type=int, default=60)
    ap.add_argument("--allow-insecure", action="store_true",
                    help="allow the stale-CA fallback, and only for INSECURE_HOSTS "
                         "(every such fetch is stamped ok-INSECURE in its sidecar)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--skip-stored", action="store_true",
                    help="do not re-fetch a capture already on disk (idempotent re-pass; "
                         "spends no request on it, and never versions a duplicate beside it)")
    a = ap.parse_args()

    global _allow_insecure
    _allow_insecure = a.allow_insecure
    # The cap is armed BEFORE any command can reach the network, so `enumerate` cannot run
    # against an unarmed budget and report every window as "budget exhausted".
    _budget.update({"left": a.max_requests, "cap": a.max_requests, "used": 0})
    if a.self_test or a.cmd == "selftest":
        return selftest()

    if a.cmd == "enumerate":
        s, body, note, transport = http_get(cdx_url(a.domain, a.frm, a.to, a.limit))
        r = classify_cdx(a.domain, a.frm, a.to, s, body, note, transport, a.limit)
        print(json.dumps({k: v for k, v in r.items() if k != "rows"}, indent=1))
        for row in r["rows"][:12]:
            print("  %s" % " ".join(str(row[k]) for k in REQUIRED_ROW_KEYS))
        return 0 if r["verdict"] == ANSWERED else 1

    if a.cmd == "audit":
        d = a.company_dir or os.path.join(a.company_root, a.slug)
        f = audit_dir(os.path.join(d, "sources", "web_archive") if not d.endswith("web_archive")
                      else d)
        hard = [x for x in f if not x.startswith("LEGACY-SIDECAR-SHAPE")]
        shape = [x for x in f if x.startswith("LEGACY-SIDECAR-SHAPE")]
        print("audit %s: %d finding(s), %d sidecar-shape note(s)" % (d, len(hard), len(shape)))
        for x in f:
            print("  " + x)
        return 1 if hard else 0

    map_, note = load_domains(a.domains_file)
    slugs = [s.strip() for s in a.slug.split(",") if s.strip()]
    if not slugs:
        raise SystemExit("run needs --slug <a,b,c>")
    all_rows, rc, planned_total = [], 0, 0
    for slug in slugs:
        cdir = a.company_dir or resolve_company_dir(a.company_root, slug)
        entries = map_.get(slug, [])
        planned = len(entries) if entries else 1     # no cited domain is still ONE slot
        planned_total += planned
        notes = []
        rows = run_slug(slug, cdir, entries, a.per_domain, a.max_bytes, a.dry_run, notes,
                        a.limit, a.skip_stored)
        for r in rows:
            r.setdefault("slug", slug)
        all_rows += rows
        print("\n%s -> %s" % (slug, cdir or "(no company dir)"))
        print_slots(rows)
        if cdir:
            p, ok, msg, counts = write_run(cdir, slug, rows, a.max_requests, planned)
            print("  identity: %s" % msg)
            print("  wrote %s" % p)
            if not ok:
                rc = 2
        else:
            print("  UNTRIED: no company dir for slug %r, nothing written" % slug)
    ok, msg, counts, dups = tally(all_rows, planned_total)
    print("\nfleet total: %s" % msg)
    print("per-state: " + "  ".join("%s=%d" % (s, counts[s]) for s in STATES))
    print("requests used %d of --max-requests %d" % (_budget["used"], a.max_requests))
    if counts[UNANSWERED] or counts[NULL] or counts[UNTRIED]:
        rc = rc or 1
    return rc


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main())
