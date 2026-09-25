#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
periodical_harvest.py — THE FOUNDER'S PLAYBOOK batch harvester for digitised
pre-1994 periodicals (method file 00_METHOD_AND_STYLE.md §14 rule 6: the
periodical corpus family that EDGAR and web archives cannot see).

Stdlib only. Read-only public search APIs only. Polite by construction:
  * sequential requests, per-host delay (default 2 s), honest User-Agent with
    contact placeholder, and a per-family Accept that matches what the family
    actually returns
  * exponential backoff on 429/503 honouring Retry-After
  * hard stop after 5 consecutive failures per host
  * --max-requests cost cap, --dry-run planner
  * raw evidence bytes saved verbatim beside a .meta.json sidecar; an existing
    evidence file is NEVER overwritten — a changed response is written beside
    it as <hash>-r<UTC stamp>.<ext> so the before-picture survives
  * NO response cache by default (2026-09-25 fix, see "What was wrong" in
    HARVEST_README.md): the cache used to BE the committed evidence folder, so
    a scheduled run on a fresh checkout replayed the previous machine's
    failures and issued zero network requests while still printing 403/429/0.
    Opt in with --cache-dir <path outside the repo's committed folders>.
  * HTTP 3xx is reported, not silently followed (2026-09-25 fix): following a
    redirect recorded the pre-redirect URL next to bytes produced by the
    post-redirect URL, which is how a moved host was mis-read as a blocked one
  * EMPTY (proven null) is NEVER conflated with UNANSWERED (blocked /
    rate-limited / TLS-trust failure / not-implemented) — §14 failure-honesty
    rule. A client-side certificate-trust failure is recorded as its own class
    (`tls_trust` in the sidecar), never as an empty catalogue.

Sources implemented (endpoint shapes verified by LIVE calls on 2026-09-25 from
this machine — the verification record, including what each fix was, is in
HARVEST_README.md and the raw evidence in
00_universe/harvest/_probe_fixed_20260925/):
  chronicling_america   LoC page search  (documented OpenSearch params
                      andtext/format/page; canonical host is now
                      www.loc.gov/chroniclingamerica — see README; responses
                      are Cloudflare-challenged to scripted clients, so this
                      family reports UNANSWERED, never NULL, from here)
  chronicling_america_titles  NDNP title-directory search (terms/format/page)
  chronicling_america_ocr  per-page ocr.txt text (documented link pattern)
  internet_archive      advancedsearch.php JSON + metadata/{id} + item text
  corporate_print       digitised BOUND CORPORATE PRINT (annual / shareholder
                        reports, 10-Ks, prospectuses, corporate research
                        print) over the same Internet Archive metadata index:
                        company terms + report-type terms + YEAR range, then
                        identifier -> metadata -> *_djvu.txt availability ->
                        direct-server text URL
  hathitrust            babel /cgi/ls full-text search with the site's own
                        SFX-style SEMICOLON parameter grammar
                        (field1/q1/a=srchls/lmt[/facet=bothPublishDateRange])
                        -> VERIFIED LIVE 2026-09-25, HTTP 200 + real records
  google_books          legacy Data API Atom feed
                        books.google.com/books/feeds/volumes -> VERIFIED LIVE
                        2026-09-25 without a key; the books.googleapis.com v1
                        JSON route is dead keyless (anonymous-project quota is
                        0 queries/day) and is kept only as an opt-in endpoint

  The fifth family exists because it is the one that REVERSED a depth verdict:
  the complete printed Wal-Mart Stores annual-report run FY1972-FY1997 sits
  text-searchable on Internet Archive
  (company_002_walmart/research/B_periodical_retest.md), and the probe that
  rated Walmart forensic-core had never queried digitised books or bound
  corporate print at all.  An unqueried family is UNANSWERED, never NULL.

Run:  python periodical_harvest.py --config queries.json [--dry-run]
      [--max-requests N] [--delay S] [--company walmart]
      [--cache-dir DIR] [--insecure-hosts h1,h2] [--follow-redirects]
      [--gb-key KEY | env GOOGLE_BOOKS_API_KEY]
Output: founders_playbook/00_universe/harvest/<source_family>/<sha1>.<ext>
        + <sha1>.meta.json sidecars (changed responses are written beside the
        old evidence as <sha1>-r<UTC>.<ext>, never over it),
        candidates.csv, _MANIFEST.md
"""

import argparse
import csv
import hashlib
import json
import os
import re
import shutil
import socket
import ssl
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request

USER_AGENT = ("FoundersPlaybook-harvest/1.0 "
              "(research tool for THE FOUNDER'S PLAYBOOK; "
              "contact: research@example.org)")
# Per-family Accept, 2026-09-25. The old code sent `Accept: */*` to every host,
# which is the single loudest "I am a script" signal a client can send to a
# CDN-fronted host and is what the brief asked to correct. Note that a
# browser-like Accept did NOT by itself unlock www.loc.gov (see README): the
# honest record is the pairing of header set and outcome, saved per response.
FAMILY_ACCEPT = {
    "chronicling_america": "application/json, text/plain, */*",
    "chronicling_america_titles": "application/json, text/plain, */*",
    "chronicling_america_ocr": "text/plain, application/json;q=0.8, */*;q=0.7",
    "internet_archive": "application/json, text/plain, */*",
    "corporate_print": "application/json, text/plain, */*",
    "hathitrust": ("text/html,application/xhtml+xml,application/json;q=0.8,"
                   "*/*;q=0.7"),
    "google_books": ("application/atom+xml,application/xml;q=0.9,"
                     "application/json;q=0.8,*/*;q=0.7"),
}
CSV_FIELDS = ["company", "source_family", "query", "item_id", "title",
              "date_or_issue", "url", "snippet_or_hitcount", "http_status",
              "classification", "retrieved_at"]
CONSEC_FAIL_LIMIT = 5
MAX_RETRIES = 4            # attempts on 429/503 (incl. first try)
MAX_RETRY_AFTER_HONOUR = 60   # seconds; beyond this we stop and record UNANSWERED

def now_utc():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

def run_stamp():
    return time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())

def url_hash(url):
    return hashlib.sha1(url.encode("utf-8")).hexdigest()[:16]

def log(msg):
    print("[%s] %s" % (now_utc(), msg), flush=True)

# --------------------------------------------------------------------------
# HTTP machinery — polite by construction
# --------------------------------------------------------------------------

class _NoRedirect(urllib.request.HTTPRedirectHandler):
    """Do not silently follow 3xx. Following a redirect and then saving the
    PRE-redirect url beside the POST-redirect bytes is what made Chronicling
    America look "bot-blocked as requested": the recorded request was not the
    request that produced the response (2026-09-25 finding: every
    chroniclingamerica.loc.gov path answers 308 -> www.loc.gov/chroniclingamerica
    and the harvester stored the old URL beside the new host's 403 body).
    A 3xx is now its own answer, with its Location recorded."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


class Http:
    def __init__(self, delay, insecure=False, insecure_hosts=None,
                 follow_redirects=False, use_curl=False, curl_bin="curl"):
        self.delay = delay
        self.insecure = insecure
        self.insecure_hosts = [h.lower() for h in (insecure_hosts or [])]
        self.follow_redirects = follow_redirects
        self.use_curl = use_curl
        self.curl_bin = curl_bin
        # a host that refuses the curl client too gets asked ONCE, not per task
        self.curl_refused = set()
        self.last_seen = {}      # host -> monotonic of last request
        self.consec_fail = {}    # host -> consecutive failure count
        self.halted = {}         # host -> reason string
        self.requests_made = 0   # network requests actually performed
        self._ctx_verify = None
        self._ctx_skip = None

    def _ssl_ctx(self, host):
        """Verification is ON. It is skipped only where the operator says so on
        the command line, and the sidecar records tls_verify='skipped ...' so a
        skipped-verification response can never be mistaken for a verified one.
        (A stale CA bundle / a machine clock ahead of the leaf certificate's
        notAfter produces 'certificate has expired' here — see the HathiTrust
        entry in HARVEST_README.md: that is a client condition, not a host
        answer, and it used to be logged as a bare status 0.)"""
        skip = self.insecure or host.lower() in self.insecure_hosts
        if skip:
            if self._ctx_skip is None:
                self._ctx_skip = ssl.create_default_context()
                self._ctx_skip.check_hostname = False
                self._ctx_skip.verify_mode = ssl.CERT_NONE
            return self._ctx_skip, "skipped (--insecure/--insecure-hosts)"
        if self._ctx_verify is None:
            self._ctx_verify = ssl.create_default_context()
        return self._ctx_verify, "on"


    @staticmethod
    def host_of(url):
        return urllib.parse.urlsplit(url).netloc

    def halted_reason(self, url):
        return self.halted.get(self.host_of(url))

    def _fetch_curl(self, url, family):
        """Opt-in second client (--use-curl); returns (status, headers, body,
        error_class) or None when curl is unavailable.

        WHY THIS EXISTS, and why it is not a fingerprint spoof. On 2026-09-25
        HathiTrust's /cgi/ls answered 403 'Cf-Mitigated: challenge' to this
        machine's Python client for EVERY header combination tried (declared
        tool UA; Chrome UA with sec-ch-ua / sec-fetch-* / Accept-Language; a
        browser cipher list; ALPN h2) while curl FROM THE SAME IP sending the
        same declared UA to the same URL answered 200 with the real result page
        (All Items 11,850 / Full View 2,638 for 'Wal-Mart' Bentonville). The
        rule is keyed on the client's TLS/HTTP stack, not on the request line.
        Mimicking a browser fingerprint to get past bot management would be
        circumvention and this tool will not do that; using a second ordinary
        command-line client and LABELLING the response client='curl' in the
        sidecar is not. TLS verification stays ON (no -k): curl uses its own
        trust store, which on this box is current where Python's is not."""
        fd, hp = tempfile.mkstemp(prefix="ph_h_")
        os.close(fd)
        fd, bp = tempfile.mkstemp(prefix="ph_b_")
        os.close(fd)
        try:
            # Resolve a bare name through PATH first. Windows' CreateProcess
            # looks in System32 BEFORE PATH, so argv "curl" silently picks
            # C:\Windows\System32\curl.exe while a shell picks Git's
            # curl.exe — and on 2026-09-25 that decided the outcome: the two
            # builds differ in their TLS ClientHello, HathiTrust's Cloudflare
            # rule scores the fingerprint, and only one of the two curl builds
            # on this box was served (Git's curl 8.7.1: HTTP 200 / 391,768 B /
            # 100 records; System32's: 403 Cf-Mitigated: challenge, same URL,
            # same UA, same flags, same IP). Recorded, not exploited.
            exe = shutil.which(self.curl_bin) or self.curl_bin
            cmd = [exe, "-s", "-S", "--max-time", "60",
                   "-A", USER_AGENT, "-H",
                   "Accept: " + FAMILY_ACCEPT.get(family or "", "*/*"),
                   "-D", hp, "-o", bp, "-w", "%{http_code}"]
            if not self.follow_redirects:
                cmd.append("--no-location")
            cmd.append(url)
            self.requests_made += 1
            self.last_seen[self.host_of(url)] = time.monotonic()
            r = subprocess.run(cmd, capture_output=True, timeout=120)
            code = (r.stdout or b"").decode("ascii", "replace").strip()
            if not code.isdigit():
                return None
            status = int(code)
            with open(hp, "r", encoding="latin-1") as f:
                raw = f.read()
            last = raw.rsplit("HTTP/", 1)
            head = ("HTTP/" + last[1]) if len(last) > 1 else ""
            headers = {}
            for line in head.splitlines()[1:]:
                if ":" in line:
                    k, v = line.split(":", 1)
                    headers[k.strip()] = v.strip()
            with open(bp, "rb") as f:
                body = f.read()
            ec = "" if status == 200 else (
                "rate_limited" if status == 429 else "http_error")
            return status, headers, body, ec
        except Exception:
            return None
        finally:
            for p in (hp, bp):
                try:
                    os.remove(p)
                except Exception:
                    pass

    def fetch(self, url, budget_left, family=None):
        """Return (status, headers_dict, body_bytes, note, extra). Never raises.
        status==0 -> network-level failure (UNANSWERED) and extra['error_class']
        says WHICH kind: tls_trust, dns, timeout and network are four different
        facts, and none of them is an empty catalogue.
        300<=status<400 -> extra['redirect_location'], not followed."""
        host = self.host_of(url)
        accept = FAMILY_ACCEPT.get(family or "", "*/*")
        extra = {"error_class": "", "redirect_location": "", "tls_verify": "on",
                 "client": "python-urllib",
                 "request_headers": {"User-Agent": USER_AGENT, "Accept": accept}}
        if self.requests_made >= budget_left:
            extra["error_class"] = "cost_cap"
            return -1, {}, b"", "global max-requests cap reached", extra
        # per-host politeness delay
        wait = self.delay - (time.monotonic() - self.last_seen.get(host, 0.0))
        if wait > 0:
            time.sleep(wait)
        status, body, headers, note = 0, b"", {}, ""
        for attempt in range(MAX_RETRIES):
            self.requests_made += 1
            self.last_seen[host] = time.monotonic()
            ctx, extra["tls_verify"] = self._ssl_ctx(host)
            req = urllib.request.Request(url, headers={
                "User-Agent": USER_AGENT, "Accept": accept})
            opener = urllib.request.build_opener(
                urllib.request.HTTPSHandler(context=ctx))
            if not self.follow_redirects:
                opener.add_handler(_NoRedirect())
            try:
                with opener.open(req, timeout=45) as r:
                    status = r.status
                    headers = dict(r.headers)
                    body = r.read()
                    break
            except urllib.error.HTTPError as e:
                status = e.code
                headers = dict(e.headers or {})
                try:
                    body = e.read() or b""
                except Exception:
                    body = b""
                if 300 <= status < 400:
                    extra["error_class"] = "redirect"
                    extra["redirect_location"] = headers.get("Location", "")
                    note = ("HTTP %d not followed; Location: %s"
                            % (status, extra["redirect_location"] or "(absent)"))
                    break
                if status in (429, 503):
                    ra = headers.get("Retry-After", "")
                    try:
                        ra_s = int(float(ra))
                    except (TypeError, ValueError):
                        ra_s = 0
                    if ra_s > MAX_RETRY_AFTER_HONOUR:
                        note = "Retry-After %ss exceeds honour cap; stopped" % ra_s
                        extra["error_class"] = "rate_limited"
                        break
                    backoff = ra_s if ra_s > 0 else (2 ** (attempt + 1))
                    log("  %s %s -> backoff %ss (attempt %d/%d)"
                        % (status, host, backoff, attempt + 1, MAX_RETRIES))
                    time.sleep(backoff)
                    continue
                break   # 403/404/other 4xx: definitive answer, no retry
            except Exception as e:
                status = 0
                body = b""
                es = "%s: %s" % (type(e).__name__, e)
                if "CERTIFICATE_VERIFY_FAILED" in es or "certificate" in es.lower():
                    extra["error_class"] = "tls_trust"
                    note = ("CLIENT-SIDE TLS TRUST FAILURE (%s). The endpoint was "
                            "never answered: NOT an empty catalogue and NOT a "
                            "bot-block. Re-run with --insecure-hosts %s to prove "
                            "the route, or from a box whose CA bundle matches "
                            "this clock" % (es[:150], host))
                elif "getaddrinfo" in es or isinstance(e, socket.gaierror) or \
                        "Name or service not known" in es:
                    extra["error_class"] = "dns"
                    note = ("NAME DOES NOT RESOLVE from this network (%s): the "
                            "host is not on the public internet for us; not a "
                            "null on content" % es[:150])
                elif "timed out" in es.lower():
                    extra["error_class"] = "timeout"
                    note = "network error: %s" % es[:200]
                else:
                    extra["error_class"] = "network"
                    note = "network error: %s" % es[:200]
                time.sleep(2 ** attempt)
                continue
        if (status == 0 or status == 403 or status >= 500) and self.use_curl \
                and host not in self.curl_refused \
                and self.requests_made < budget_left:
            refused = "%s/%s" % (status, extra["error_class"] or "?")
            alt = self._fetch_curl(url, family)
            if alt and alt[0] == 200:
                status, headers, body, ecls = alt
                extra["error_class"] = ecls
                extra["client"] = "curl (--use-curl fallback)"
                note = ("Python's own client was refused (%s); this response "
                        "came from the curl fallback client, which this host "
                        "answers. The sidecar records client=curl so the "
                        "evidence never hides which client got in." % refused)
            elif alt:
                status, headers, body, ecls = alt
                extra["error_class"] = ecls or "http_error"
                extra["client"] = "curl (--use-curl fallback)"
                note = ("both clients refused: python=%s, curl=HTTP %d"
                        % (refused, status))
            if status != 200:
                self.curl_refused.add(host)
        if status == 429 and not extra["error_class"]:
            extra["error_class"] = "rate_limited"
        # classify for consecutive-failure / hard stop
        cf_hdr = (headers.get("Cf-Mitigated") or headers.get("cf-mitigated")
                  or "")
        blocked = (status == 403 and (b"Just a moment" in body
                                       or b"cf-challenge" in body
                                       or str(cf_hdr).lower() == "challenge"))
        failure = status == 0 or status in (429, 503) or status >= 500 or blocked
        cf = self.consec_fail.get(host, 0)
        self.consec_fail[host] = 0 if not failure else cf + 1
        if blocked:
            extra["error_class"] = "bot_challenge"
            note = ("HTTP 403 Cloudflare bot-management challenge "
                    "(Cf-Mitigated: %s, Cf-Ray: %s). The host answered 'prove "
                    "you are a browser' and never searched anything: UNANSWERED, "
                    "not a null, and no parameter change will fix it"
                    % (cf_hdr or "challenge page", headers.get("CF-RAY", "?")))
        if self.consec_fail[host] >= CONSEC_FAIL_LIMIT and host not in self.halted:
            self.halted[host] = "hard stop: %d consecutive failures" % CONSEC_FAIL_LIMIT
            log("  HOST HALTED: %s (%s)" % (host, self.halted[host]))
        return status, headers, body, note, extra

# --------------------------------------------------------------------------
# Raw-evidence persistence + cache
# --------------------------------------------------------------------------

class Archive:
    """Raw-evidence writer + (opt-in) response cache.

    2026-09-25, two structural fixes:

    1. THE CACHE IS NO LONGER THE EVIDENCE FOLDER. It used to be, and evidence
       is committed to git, so a scheduled run on a fresh checkout found
       <url-hash>.meta.json already on disk, replayed the previous machine's
       403/429/0 bytes and printed 'network requests: 0' next to a table of
       'failures'. That is how a cache replay came to be read as a second
       egress confirming a block. Cache is now a separate --cache-dir (off by
       default), so every run asks the host unless an operator opts in.
    2. EVIDENCE IS NEVER OVERWRITTEN. An identical re-fetch is left alone; a
       response that CHANGED is written beside the old one as
       <hash>-r<UTCstamp><ext>, so a 403 -> 200 flip keeps both halves.
    """

    def __init__(self, out_root, source_family, cache_dir=None, stamp=""):
        self.dir = os.path.join(out_root, source_family)
        self.cache = os.path.join(cache_dir, source_family) if cache_dir else None
        self.stamp = stamp
        self.written = 0
        self.unchanged = 0
        self.versioned = 0
        os.makedirs(self.dir, exist_ok=True)
        if self.cache:
            os.makedirs(self.cache, exist_ok=True)

    @staticmethod
    def _read_pair(meta_dir, h):
        meta_p = os.path.join(meta_dir, h + ".meta.json")
        if not os.path.exists(meta_p):
            return None, None
        try:
            with open(meta_p, "r", encoding="utf-8") as f:
                meta = json.load(f)
            body_p = os.path.join(meta_dir, h + meta.get("ext", ".bin"))
            if not os.path.exists(body_p):
                base = meta.get("evidence_file") or ""
                body_p = os.path.join(meta_dir, base) if base else body_p
            if os.path.exists(body_p):
                with open(body_p, "rb") as f:
                    return meta, f.read()
        except Exception:
            return None, None
        return None, None

    def cached(self, url):
        """Cache lookup happens ONLY in --cache-dir. Never in the evidence
        tree: the evidence tree is history, and history is not a response."""
        if not self.cache:
            return None, None
        return self._read_pair(self.cache, url_hash(url))

    def save(self, url, body, status, headers, meta_ctx, ext, note="",
             extra=None):
        h = url_hash(url)
        base = os.path.join(self.dir, h + ext)
        base_meta = os.path.join(self.dir, h + ".meta.json")
        target, target_meta = base, base_meta
        if os.path.exists(base_meta) or os.path.exists(base):
            try:
                with open(base, "rb") as f:
                    same_bytes = f.read() == body
            except Exception:
                same_bytes = False
            prior_status = None
            try:
                with open(base_meta, encoding="utf-8") as f:
                    prior_status = json.load(f).get("http_status")
            except Exception:
                pass
            if same_bytes and prior_status == status:
                # identical re-fetch: touch NOTHING. Rewriting the sidecar
                # would restate retrieved_at for bytes we captured earlier,
                # and the note that explains them is not re-derivable.
                self.unchanged += 1
                return os.path.basename(base)
            else:
                # the response CHANGED (a 403 -> 200 flip, a new challenge, a
                # different hit count): write beside it, never over it
                self.versioned += 1
                stem = "%s-r%s" % (h, self.stamp or now_utc().replace(":", ""))
                target = os.path.join(self.dir, stem + ext)
                target_meta = os.path.join(self.dir, stem + ".meta.json")
        with open(target, "wb") as f:
            f.write(body)          # verbatim — never normalised
        self.written += 1
        meta = {
            "url": url,
            "evidence_file": os.path.basename(target),
            "http_status": status,
            "content_type": headers.get("Content-Type", ""),
            "bytes": len(body),
            "retrieved_at": now_utc(),
            "ext": ext,
            "client": (extra or {}).get("client", "python-urllib"),
            "request_headers": (extra or {}).get("request_headers", {}),
            "tls_verify": (extra or {}).get("tls_verify", "on"),
            "error_class": (extra or {}).get("error_class", ""),
            "redirect_location": (extra or {}).get("redirect_location", ""),
            "cf_mitigated": headers.get("Cf-Mitigated", "") or headers.get("cf-mitigated", ""),
            "cf_ray": headers.get("CF-RAY", ""),
            "retry_after": headers.get("Retry-After", ""),
            "note": note,
        }
        meta.update(meta_ctx)
        with open(target_meta, "w", encoding="utf-8") as f:
            json.dump(meta, f, indent=1, ensure_ascii=False)
        if self.cache:
            with open(os.path.join(self.cache, h + ext), "wb") as f:
                f.write(body)
            with open(os.path.join(self.cache, h + ".meta.json"), "w",
                      encoding="utf-8") as f:
                json.dump(meta, f, indent=1, ensure_ascii=False)
        return os.path.basename(target)


# --------------------------------------------------------------------------
# Source adapters. Each: build_urls(cfg) + parse(source_family, body,
# status, note) -> list of candidate row dicts.
# Verified-parameter endpoints only; see HARVEST_README.md verification log.
# --------------------------------------------------------------------------

# Chronicling America MOVED and nobody told the harvester. Verified 2026-09-25:
# EVERY path on the legacy host answers "HTTP 308 Permanent Redirect" to
# www.loc.gov/chroniclingamerica/<same path> (tested: /search/pages/results/,
# /search/titles/, /bulk/, /newspapers.json). The old code called urllib without
# a redirect handler, so it silently fetched the new host while writing the OLD
# url into the sidecar next to the NEW host's 403 body — and the 403 was a
# Cloudflare bot-management challenge on the whole www.loc.gov zone (even
# /robots.txt answers it), not a bad parameter. Both facts are now recorded
# separately: request shape fixed, block class named.
CA_BASE = "https://www.loc.gov/chroniclingamerica"
CA_LEGACY_BASE = "https://chroniclingamerica.loc.gov"

# Documented page-search parameters (official /about/api/ page, snapshot
# 2025-01-02): andtext, format, page. Everything else below is a LEGACY
# parameter carried over from the pre-relocation API: it is passed through
# because the old clients used it, but a zero from a legacy parameter is a
# statement about the parameter, not about the corpus — verify one live
# (README "What is still unproven") before treating any CA count as a null.
CA_DOCUMENTED_PARAMS = ("andtext", "format", "page")
CA_LEGACY_PARAMS = ("ortext", "nottext", "proxtext", "exactphrase", "date1",
                    "date2", "dateFilterType", "county", "state", "lccn",
                    "ed", "seq", "rows", "sort", "withText")

def ca_base(params):
    return params.get("base") or CA_BASE

def ca_search_url(params):
    q = {"format": "json"}
    q.update({k: v for k, v in params.items() if k != "base"})
    unknown = [k for k in params
               if k not in CA_DOCUMENTED_PARAMS + CA_LEGACY_PARAMS + ("base",)]
    if unknown:
        raise ValueError("unpublished Chronicling America parameter(s) %s; "
                         "refusing to invent one" % unknown)
    return ca_base(params) + "/search/pages/results/?" + urllib.parse.urlencode(q)

def ca_titles_url(params):
    """NDNP title-directory search: /search/titles/results/?terms=&format=
    [&page=] — documented, and a CATALOGUE route: it answers with title
    records, no full text. Kept separate from page search so a catalogue 200
    is never read as a text hit (the failure this project keeps meeting)."""
    q = {"format": "json"}
    q.update({k: v for k, v in params.items() if k != "base"})
    return ca_base(params) + "/search/titles/results/?" + urllib.parse.urlencode(q)

def ca_bulk_url(params):
    q = {"format": "json"}
    q.update({k: v for k, v in params.items() if k != "base"})
    return ca_base(params) + "/bulk/?" + urllib.parse.urlencode(q)

def ca_ocr_url(page_path, base=None):
    # Documented link pattern /lccn/<sn>/<date>/ed-<e>/seq-<s>/ + ocr.txt.
    # UNVERIFIED since the relocation: the new site's own URLs carry the bare
    # LCCN (e.g. /chroniclingamerica/lccn/2010270510/issues) rather than the
    # sn-prefixed form, so this pattern may itself 308. Recorded, not assumed.
    return (base or CA_BASE) + page_path.rstrip("/") + "/ocr.txt"


def ia_search_url(qstr, rows):
    return ("https://archive.org/advancedsearch.php?q=" +
            urllib.parse.quote(qstr) +
            "&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=date"
            "&fl%5B%5D=year&fl%5B%5D=mediatype&fl%5B%5D=collection"
            "&rows=" + str(int(rows)) + "&page=1&output=json")

def ia_meta_url(identifier):
    return "https://archive.org/metadata/%s" % urllib.parse.quote(identifier)

# --- family 5: digitised corporate print / annual reports (IA metadata index)
# Every clause field below was confirmed by a LIVE advancedsearch call on
# 2026-09-24 returning 200 + response.numFound + docs[] carrying exactly
# identifier/title/date/year/mediatype/collection/creator
# (creator and collection are LIST-valued).  Verified working example:
#   (title:(walmart) OR title:("wal-mart stores")) AND (title:(annual) OR
#   title:(reports) OR title:(yearbook)) AND mediatype:(texts)
#   AND YEAR:[1970 TO 1998]        -> numFound 27, the FY1972-FY1997 AR run
# NOT usable (tested live, returns token noise): the unscoped conjunction
#   walmart AND "annual report" AND YEAR:[..]  -> hits are CIA reading-room
#   documents and Compute! magazine.  Kept out of the shipped queries.
CP_FL_FIELDS = ["identifier", "title", "date", "year", "mediatype",
                "collection", "creator"]

def cp_clause(terms, field):
    return "(" + " OR ".join("%s:(%s)" % (field, t) for t in terms) + ")"

def cp_search_url(params):
    """Compose an Internet Archive metadata-search query from DATA.

    scope_field / report_field are restricted to the two clause fields proven
    live (title, creator); anything else raises rather than shipping an
    invented parameter."""
    for f in (params.get("scope_field", "title"),
              params.get("report_field", "title")):
        if f not in ("title", "creator"):
            raise ValueError("unverified query field %r in task params; "
                             "refusing to invent a parameter" % f)
    parts = [cp_clause(params["company_terms"],
                       params.get("scope_field", "title"))]
    if params.get("report_terms"):
        parts.append(cp_clause(params["report_terms"],
                               params.get("report_field", "title")))
    if params.get("mediatype"):
        parts.append("mediatype:(%s)" % params["mediatype"])
    yr = params.get("year_range")
    if yr:
        parts.append("YEAR:[%d TO %d]" % (int(yr[0]), int(yr[1])))
    q = " AND ".join(parts)
    return ("https://archive.org/advancedsearch.php?q=" +
            urllib.parse.quote(q) +
            "".join("&fl%5B%5D=" + f for f in CP_FL_FIELDS) +
            "&rows=" + str(int(params.get("rows", 20))) +
            "&page=1&output=json")

def cp_text_url(server, directory, filename):
    """Direct-server item text.  VERIFIED LIVE 2026-09-24: server+dir come
    from archive.org/metadata/<id>; the built URL
    https://ia601404.us.archive.org/11/items/<id>/<id>_djvu.txt returned
    HTTP 200 / 23,989 B of the FY1972 Wal-Mart report.  The friendlier
    archive.org/download/<id>/<file> route 302s to a CDN whose TLS cert is
    expired in this environment (recorded as UNANSWERED, not a null)."""
    return "https://%s%s/%s" % (server, directory.rstrip("/"), filename)

HT_LS = "https://babel.hathitrust.org/cgi/ls"
HT_CATALOG = "https://catalog.hathitrust.org"
# HathiTrust's /cgi/ls grammar is SFX-style: parameters are separated by
# SEMICOLONS, not ampersands, and the search action is `a=srchls`. The old
# builder called the legacy `/cgi/ls/one` alias with `&`-separated
# searchtype/target/ft, which answers 302 -> `.../cgi/ls?field1=ocr;q1=...;
# a=srchls;lmt=ft`. It also never got that far from this machine, because
# urllib died on a certificate-trust error and reported a bare status 0.
# VERIFIED LIVE 2026-09-25 (with --insecure-hosts babel.hathitrust.org):
#   /cgi/ls?field1=ocr;q1="Wal-Mart" Bentonville;a=srchls;lmt=ft -> 200,
#     facet counts All Items 11,850 / Full View 2,638, 100 record blocks
#   same + ;facet=bothPublishDateRange:"1960-1969" -> 45 / 4 full-view records
#   q1="five and dime" variety store ;facet=...:"1950-1959" -> 2,284 / 187
# DATE FACETS: the facet FIELD is `bothPublishDateRange` (a decade string such
# as "1960-1969", or a single year such as "2002"), copied out of the site's
# own result-page hrefs. `facet=DateRange:"1960-1969"` — the plausible guess —
# is ACCEPTED, echoed back as an active filter, and returns
# "No results match your search" for a control query that has 2,284 hits.
# That is a fake negative produced by a parameter name, which is the failure
# mode this file exists to prevent; ht_search_url therefore refuses any facet
# field outside HT_PUBLISH_DATE_FACETS below.
HT_PUBLISH_DATE_FACETS = ("bothPublishDateRange", "pubDateRange")
HT_DATE_FACET_RX = re.compile(r'^(\w+):"(\d{4})(?:-(\d{4}))?"$')

def ht_search_url(params):
    q1 = params["q1"]
    parts = [("field1", params.get("field1", "ocr")), ("q1", q1),
             ("a", "srchls"), ("lmt", params.get("lmt", "ft"))]
    for f in params.get("facets") or []:
        m = HT_DATE_FACET_RX.match(f)
        if not m or m.group(1) not in HT_PUBLISH_DATE_FACETS:
            raise ValueError(
                "refusing HathiTrust facet %r: a facet field that does not "
                "exist is silently accepted and returns zero rows, which reads "
                "as an empty catalogue. Use %s with a decade or year, e.g. "
                'bothPublishDateRange:"1960-1969". Copy the exact string out '
                "of a live result page." % (f, list(HT_PUBLISH_DATE_FACETS)))
        parts.append(("facet", f))
    if params.get("sort"):
        parts.append(("sort", params["sort"]))
    return HT_LS + "?" + ";".join(
        "%s=%s" % (k, urllib.parse.quote(str(v), safe=":,-"))
        for k, v in parts)

def ht_brief_url(id_type, value):
    """Catalog 'brief record' API — bibliographic metadata for one item, JSON.
    CATALOGUE ONLY: it never returns page text. Kept so a run can resolve an
    HT id to a title/date without pretending it searched full text."""
    return "%s/api/volumes/brief/%s/%s.json" % (
        HT_CATALOG, id_type, urllib.parse.quote(str(value), safe="."))

# Google Books: TWO different services wear the same name.
#   www.googleapis.com/books/v1/volumes  — the JSON API, GCP-quota'd. Keyless it
#     is answered 429 with quota_limit_value "0" on Google's SHARED ANONYMOUS
#     project (project_number:624717413613): "Queries per day = 0". That is not
#     a rate limit to back off from and not a delay to widen — every keyless
#     call from every network is refused, which is why the 2026-09-24/25 runs
#     saw 429 twice from one machine and 'again' from a cache replay. It needs a
#     key: --gb-key / GOOGLE_BOOKS_API_KEY.
#   books.google.com/books/feeds/volumes  — the legacy Atom Data API, no key, no
#     GCP quota. VERIFIED LIVE 2026-09-25: 200, application/atom+xml, real
#     volumeIds, viewability, and a `pg=` page pointer per hit. It carries NO
#     snippet text keyless (zero <gbs:snippet> in the response), so it is a
#     finding aid, not a text source; and books.google.com/<browsing html> for
#     the page itself answers 403 "your computer or network may be sending
#     automated queries". totalResults is capped at 300 and is not a count.
GB_FEEDS = "https://books.google.com/books/feeds/volumes"
GB_V1 = "https://www.googleapis.com/books/v1/volumes"

def gb_search_url(params, api_key=""):
    ep = (params.get("endpoint") or "feeds").lower()
    q = {"q": params["q"], "maxResults": int(params.get("max_results", 10))}
    if params.get("printType"):
        q["printType"] = params["printType"]
    key = params.get("api_key") or api_key
    if key:
        q["key"] = key
    if ep == "v1":
        return GB_V1 + "?" + urllib.parse.urlencode(q)
    return GB_FEEDS + "?" + urllib.parse.urlencode(q)


def _clean(s, n=180):
    s = re.sub(r"\s+", " ", (s or "")).strip()
    return s[:n]

# --------------------------------------------------------------------------
# Row classification helpers — the EMPTY vs UNANSWERED firewall
# --------------------------------------------------------------------------

def row(company, family, query, item_id="", title="", date="", url="",
        snippet="", status="", cls="", when=""):
    return {"company": company, "source_family": family, "query": query,
            "item_id": item_id, "title": title, "date_or_issue": date,
            "url": url, "snippet_or_hitcount": snippet,
            "http_status": status, "classification": cls,
            "retrieved_at": when or now_utc()}

def unanswered_or_error(company, family, query, status, note, extra=None):
    cls = "ERROR" if (400 <= (status or 0) < 500 and status not in (403, 429)
                      and not (300 <= (status or 0) < 400)) \
        else "UNANSWERED"
    ec = (extra or {}).get("error_class") or ""
    return row(company, family, query,
               snippet="UNANSWERED%s: %s" % ("[%s]" % ec if ec else "",
                                             note or "no answer from endpoint"),
               status=status, cls=cls)

# --------------------------------------------------------------------------
# Parsers
# --------------------------------------------------------------------------

def _ca_items(j):
    """The relocated app has no published changelog we can trust, so accept the
    legacy OpenSearch keys (items/totalItems) and the newer itemList/totalItems,
    and SAY WHICH one answered — a shape we have never seen is reported, not
    quietly parsed to zero rows."""
    for k in ("items", "itemList", "docs"):
        if isinstance(j.get(k), list):
            return j[k], k
    return [], ""

def parse_ca_search(company, query_label, body, status, note, extra=None,
                    family="chronicling_america", text_bearing=True):
    if status != 200:
        return [unanswered_or_error(company, family, query_label, status,
                                    note, extra)]
    try:
        j = json.loads(body.decode("utf-8", "replace"))
    except Exception as e:
        return [unanswered_or_error(company, family, query_label, status,
                                    "200 but not JSON (%s) — an HTML challenge "
                                    "page served with a 200 is a block, not a "
                                    "result: %s" % (
                                        _clean(body.decode("utf-8", "replace"), 60), e),
                                    extra)]
    items, key = _ca_items(j)
    total = j.get("totalItems")
    if total is None and not items:
        return [unanswered_or_error(company, family, query_label, status,
                                    "JSON 200 but no items/itemList/totalItems key "
                                    "(keys present: %s) — shape unrecognised, "
                                    "recorded UNANSWERED rather than as 0 hits"
                                    % ",".join(sorted(j)[:12]), extra)]
    if not items and not total:
        return [row(company, family, query_label,
                    snippet="EMPTY (proven null) FOR THESE PARAMS ONLY: 0 pages "
                            "(totalItems=%s, list key '%s'). Legacy date/state "
                            "params are unverified against the relocated app, so "
                            "a 0 here indicts the parameters too." % (total, key),
                    status=200, cls="NULL")]
    rows = []
    for it in items[:50]:
        d = str(it.get("date") or "")
        iso = "%s-%s-%s" % (d[0:4], d[4:6], d[6:8]) if len(d) >= 8 else d
        ocr = it.get("ocr_eng") or it.get("snippet") or ""
        rows.append(row(
            company, family, query_label,
            item_id="%s %s seq-%s" % (it.get("lccn", ""), iso, it.get("sequence", "")),
            title=_clean(it.get("title"), 120),
            date=iso,
            url=(it.get("id") or "").startswith("http") and (it.get("id") or "")
                or CA_BASE + (it.get("id") or ""),
            snippet=_clean(ocr) or "metadata only, no text field in this item",
            status=200, cls="TIER1_CANDIDATE" if (ocr and text_bearing)
            else "LEAD_ONLY"))
    if not any(r["classification"] == "TIER1_CANDIDATE" for r in rows):
        rows.insert(0, row(company, family, query_label,
                           snippet="200 with %d item(s) but NO text field on any "
                                   "of them: this is a catalogue response, not "
                                   "contemporaneous text. Pull /ocr.txt per page "
                                   "before citing (family stays UNANSWERED for "
                                   "text)." % len(rows), status=200,
                           cls="LEAD_ONLY"))
    return rows

def parse_ca_titles(company, query_label, body, status, note, extra=None):
    """Title-directory / bulk-listing searches: newspaper MARC records and
    batch inventories. They live in the SAME corpus family as the page search
    but can never be TIER1_CANDIDATE — a title record proves the paper exists,
    never that a story was printed. text_bearing=False enforces that in the
    classification, not just in the prose."""
    return parse_ca_search(company, query_label, body, status, note,
                           extra=extra, family="chronicling_america",
                           text_bearing=False)

def parse_ca_ocr(company, query_label, body, status, note, extra=None):
    if status != 200:
        return [unanswered_or_error(company, "chronicling_america_ocr",
                                    query_label, status, note, extra)]
    text = body.decode("utf-8", "replace")
    if len(body) < 200:
        return [row(company, "chronicling_america_ocr", query_label,
                    snippet="UNANSWERED: 200 but %d B — too short to be a page's "
                            "OCR text layer (could be a stub or an error page)"
                            % len(body), status=200, cls="UNANSWERED")]
    return [row(company, "chronicling_america_ocr", query_label,
                snippet="OCR TEXT %d bytes: %s" % (len(body), _clean(text, 150)),
                status=200, cls="TIER1_CANDIDATE")]

def parse_ia_search(company, query_label, body, status, note, window=None,
                    family="internet_archive", gate=None, extra=None):
    if status != 200:
        return [unanswered_or_error(company, family, query_label, status, note,
                                    extra)]
    try:
        j = json.loads(body.decode("utf-8", "replace"))
        resp = j["response"]
    except Exception as e:
        return [unanswered_or_error(company, family, query_label, status,
                                    "unparseable: %s" % e)]
    docs = resp.get("docs") or []
    if resp.get("numFound") == 0:
        return [row(company, family, query_label,
                    snippet=("EMPTY (proven null): numFound=0"
                             if family == "internet_archive" else
                             "EMPTY (proven null): numFound=0 FOR THESE EXACT "
                             "PARAMS ONLY — per-param, never per-corpus; the "
                             "family stays open until digitised corporate "
                             "print is searched on other indexes too"),
                    status=200, cls="NULL")]
    rows = []
    for d in docs:
        date = (d.get("date") or str(d.get("year") or ""))[:10]
        cls = "LEAD_ONLY"   # metadata pointer, text not yet opened
        gate_rejected = False
        if window and date[:4].isdigit():
            y = int(date[:4])
            if window[0] <= y <= window[1] and d.get("mediatype") == "texts":
                # gate: a numFound>0 is not evidence (Walmart retest WR-17 —
                # title:(fortune) returned 213 books, zero magazines). Corporate
                # print requires the item's own metadata to corroborate.
                if gate is None or gate(d):
                    cls = "TIER1_CANDIDATE"
                else:
                    gate_rejected = True
        fields = [d.get("mediatype"), d.get("collection")]
        if family == "corporate_print":
            fields.append(d.get("creator"))
        snip = _clean(", ".join(map(str, fields)), 120)
        if gate_rejected:
            snip += (" | GATE-REJECTED from Tier-1: in-window text item, but "
                     "its own title/creator do not carry a configured "
                     "corporate name + report-type term (WR-17 "
                     "false-positive rule). Chase as a lead only.")
        rows.append(row(company, family, query_label,
                        item_id=d.get("identifier", ""),
                        title=_clean(d.get("title"), 120), date=date,
                        url="https://archive.org/details/" + d.get("identifier", ""),
                        snippet=snip, status=200, cls=cls))
    return rows

CP_IDENTITY_TOKENS = ["inc", "inc.", "incorporated", "corporation", "corp",
                      "company", "co.", "ltd", "plc", "holdings", "group"]

def _cp_word_rx(term):
    """Whole-word match.  A plain substring match cost this tool 20 false
    TIER1_CANDIDATE rows on the first Apple run: 'Appleton', 'pineapple' and
    the surname 'Loyal E. Apple' all contain the substring 'apple'."""
    return re.compile(r"(?<![\w&])" + re.escape(term) + r"(?![\w&])")

def _cp_norm(t):
    return re.sub(r"[\"']", "", str(t)).lower().strip()

def _cp_gate(company_terms, report_terms, identity_terms=None,
             name_patterns=None):
    """Anti-false-positive gate for family 5 (the Walmart retest's WR-17 trap:
    title:(fortune) returned 213 books and zero magazines).  A mediatype=texts
    item dated in window is promoted to TIER1_CANDIDATE only when its OWN
    title/creator metadata corroborates that it IS the company's print.

    Two strengths, chosen by what the task configures:
      * name_patterns given -> the metadata must contain one whole corporate
        NAME (e.g. 'apple computer, inc') AND a report-type term.  Preferred:
        precise, and it is what keeps a 1990 DTIC 'Ada Compiler Validation
        Summary Report' mentioning an 'Apple Macintosh II' and produced by
        'Meridian Software Systems, Inc.' out of the Tier-1 column.
      * only company_terms given -> require company term + report term + a
        corporate-identity token somewhere (looser backstop).
    Either way a metadata hit is still only a CANDIDATE: the text has to be
    opened before anything is cited.
    """
    if name_patterns:
        comp = [_cp_word_rx(_cp_norm(t)) for t in name_patterns if _cp_norm(t)]
        identity_terms = []
    else:
        comp = [_cp_word_rx(_cp_norm(t)) for t in company_terms if _cp_norm(t)]
        if identity_terms is None:
            identity_terms = CP_IDENTITY_TOKENS
    reps = [_cp_word_rx(_cp_norm(t)) for t in (report_terms or []) if _cp_norm(t)]
    ident = [_cp_word_rx(_cp_norm(t)) for t in identity_terms if _cp_norm(t)]
    def gate(doc):
        hay = " ".join(_flat(doc.get("title")) + _flat(doc.get("creator")))
        if not any(r.search(hay) for r in comp):
            return False
        if reps and not any(r.search(hay) for r in reps):
            return False
        if ident and not any(r.search(hay) for r in ident):
            return False
        return True
    return gate

def _flat(v):
    """IA returns single strings or lists for the same field (collection and
    creator observed list-valued live); normalise to a list of lowercase text."""
    if v is None:
        return []
    if isinstance(v, (list, tuple)):
        out = []
        for x in v:
            out.extend(_flat(x))
        return out
    if isinstance(v, dict):
        out = []
        for x in v.values():
            out.extend(_flat(x))
        return out
    return [str(v).lower()]

def parse_cp_search(company, query_label, body, status, note, window=None,
                    task_params=None):
    p = task_params or {}
    return parse_ia_search(company, query_label, body, status, note,
                           window=window, family="corporate_print",
                           gate=_cp_gate(p.get("company_terms", []),
                                         p.get("report_terms"),
                                         p.get("identity_terms"),
                                         p.get("name_patterns")))

def parse_cp_meta(company, query_label, body, status, note, window=None):
    """identifier -> text availability.  Fields read: identifier, server, dir,
    files[].name, metadata.{title,date,year} — all confirmed present in a live
    200 response on 2026-09-24.  Absent text layer is a scan-only LEAD, never
    a null on the item's content."""
    if status != 200:
        return [unanswered_or_error(company, "corporate_print", query_label,
                                    status, note)]
    try:
        j = json.loads(body.decode("utf-8", "replace"))
    except Exception as e:
        return [unanswered_or_error(company, "corporate_print", query_label,
                                    status, "unparseable: %s" % e)]
    md = j.get("metadata") or {}
    ident = j.get("identifier") or md.get("identifier") or ""
    server, directory = j.get("server") or "", j.get("dir") or ""
    texts = [f.get("name", "") for f in (j.get("files") or [])
             if str(f.get("name", "")).endswith(("_djvu.txt", ".ocr.txt",
                                                 "_hocr.searchtext"))]
    date = str(md.get("date") or md.get("year") or "")[:10]
    in_window = bool(window and date[:4].isdigit()
                     and window[0] <= int(date[:4]) <= window[1])
    text_url = cp_text_url(server, directory, texts[0]) if (texts and server
                                                            and directory) else ""
    if texts and in_window:
        cls = "TIER1_CANDIDATE"
    else:
        cls = "LEAD_ONLY"
    return [row(company, "corporate_print", query_label, item_id=ident,
                title=_clean(md.get("title"), 120), date=date,
                url=text_url or "https://archive.org/details/" + ident,
                snippet="%s | server=%s dir=%s | %s" % (
                    "TEXT LAYER PRESENT" if texts else
                    "NO TEXT LAYER (scan-only, NOT a null on content)",
                    server or "?", directory or "?",
                    ", ".join(texts) or "-"),
                status=200, cls=cls)]

def parse_cp_text(company, query_label, body, status, note, window=None,
                  identifier=""):
    """Raw item text pulled from the IA content server."""
    if status != 200:
        return [unanswered_or_error(company, "corporate_print", query_label,
                                    status, note)]
    if len(body) < 200:
        return [row(company, "corporate_print", query_label,
                    item_id=identifier,
                    snippet="UNANSWERED: 200 but body only %d B (not a "
                            "readable text layer)" % len(body),
                    status=200, cls="UNANSWERED")]
    head = _clean(body.decode("utf-8", "replace"), 150)
    return [row(company, "corporate_print", query_label, item_id=identifier,
                snippet="TIER-1 TEXT RETRIEVED %d B: %s" % (len(body), head),
                status=200, cls="TIER1_CANDIDATE")]

def parse_ia_meta(company, query_label, body, status, note):
    if status != 200:
        return [unanswered_or_error(company, "internet_archive",
                                    query_label, status, note)]
    try:
        j = json.loads(body.decode("utf-8", "replace"))
    except Exception as e:
        return [unanswered_or_error(company, "internet_archive",
                                    query_label, status, "unparseable: %s" % e)]
    texts = [f["name"] for f in j.get("files", [])
             if f.get("name", "").endswith(("_djvu.txt", ".ocr.txt"))]
    ident = j.get("identifier", "")
    return [row(company, "internet_archive", query_label, item_id=ident,
                title=_clean((j.get("metadata") or {}).get("title", ""), 120),
                date=str((j.get("metadata") or {}).get("date", ""))[:10],
                url="https://archive.org/details/" + ident,
                snippet="text-layer files: %s" % (texts or "NONE (scan-only, "
                        "NOT a null on content)"),
                status=200, cls="LEAD_ONLY")]

def parse_ht_brief(company, query_label, body, status, note, extra=None):
    """Catalog 'brief record' API: JSON, and it is the ONE HathiTrust route a
    scripted client is not challenged on (verified 2026-09-25: this endpoint
    answers 200 to the tool's own urllib request while /cgi/ls answers
    Cf-Mitigated: challenge to the same client, and the browsable
    /Record/<id> page 403s too). Catalogue + rights only: rightsCode 'pd' and
    usRightsString 'Full view' tell you the text exists to be fetched, which
    is not the same as having fetched it, so nothing here is TIER1_CANDIDATE."""
    if status != 200:
        return [unanswered_or_error(company, "hathitrust", query_label, status,
                                    note, extra)]
    try:
        j = json.loads(body.decode("utf-8", "replace"))
    except Exception as e:
        return [unanswered_or_error(company, "hathitrust", query_label, status,
                                    "200 but not JSON: %s" % e, extra)]
    recs = j.get("records") or {}
    items = j.get("items") or []
    if not recs and not items:
        return [row(company, "hathitrust", query_label,
                    snippet="EMPTY (proven null) FOR THIS IDENTIFIER ONLY: the "
                            "brief-record endpoint answered 200 with no records "
                            "and no items — the id or its type is not in the "
                            "catalog; says nothing about the full-text search "
                            "index", status=200, cls="NULL")]
    rows = []
    for rid, r in list(recs.items())[:10]:
        rows.append(row(company, "hathitrust", query_label, item_id=rid,
                        title=_clean((r.get("titles") or [""])[0], 140),
                        date=", ".join(r.get("publishDates") or [])[:20],
                        url=r.get("recordURL", ""),
                        snippet="CATALOGUE (brief record API): isbn=%s issn=%s "
                                "oclc=%s lccn=%s | bibliographic metadata only, "
                                "no text in this response" % (
                                    (r.get("isbns") or ["-"])[:1],
                                    (r.get("issns") or ["-"])[:1],
                                    (r.get("oclcs") or ["-"])[:1],
                                    (r.get("lccns") or ["-"])[:1]),
                        status=200, cls="LEAD_ONLY"))
    for it in items[:10]:
        rows.append(row(company, "hathitrust", query_label,
                        item_id=it.get("htid", ""),
                        url=it.get("itemURL", ""),
                        date="", title="",
                        snippet="ITEM RIGHTS: %s (rightsCode=%s, holder=%s) — "
                                "the text is fetchable at the itemURL; this "
                                "call did not fetch it" % (
                                    it.get("usRightsString", "?"),
                                    it.get("rightsCode", "?"),
                                    _clean(it.get("orig"), 60)),
                        status=200, cls="LEAD_ONLY"))
    return rows

HT_BLOCK_RX = re.compile(r'<article class="record.*?</article>', re.S)


HT_NO_RESULT_RX = re.compile(r"No results\s+match your search", re.I)
HT_BLOCK_RX = re.compile(r'<article class="record.*?</article>', re.S)


def parse_ht(company, query_label, body, status, note, extra=None,
             family="hathitrust"):
    """HathiTrust /cgi/ls answers HTML — format=json is accepted and IGNORED
    (verified 2026-09-25), so this parses the page it actually sends. Two
    independent numbers are recorded: the sidebar facet badges (All Items /
    Full View, the corpus counts) and the <article class="record"> blocks on
    THIS page (the items themselves, each with its HT handle)."""
    if status != 200:
        return [unanswered_or_error(company, family, query_label, status,
                                    note, extra)]
    if b"Just a moment" in body:
        return [unanswered_or_error(company, family, query_label, status,
                                    "200 but the body is a Cloudflare challenge "
                                    "page — a block, not a result", extra)]
    html = body.decode("utf-8", "replace")
    plain = re.sub(r"<[^>]+>", " ", html)     # the 'no results' sentence can
    facets = re.findall(r'lmt=(all|ft)"[^>]*>([^<]{2,40})'
                        r'<span class="badge bg-dark rounded-pill">([\d,]+)</span>',
                        html)
    if not facets:
        facets = [(i % 2 and "ft" or "all", "?", n) for i, n in
                  enumerate(re.findall(r'rounded-pill">([\d,]+)<', html)[:2])]
    counts = {k: v for k, _, v in facets}
    blocks = HT_BLOCK_RX.findall(html)
    if not blocks and HT_NO_RESULT_RX.search(plain):
        return [row(company, family, query_label,
                    snippet="EMPTY (proven null) FOR THESE PARAMS ONLY: the page "
                            "says 'No results match your search' (facet counts "
                            "%s). Date facets with an unknown FIELD name are "
                            "silently accepted and produce exactly this — see "
                            "ht_search_url before trusting a 0." % counts,
                    status=200, cls="NULL")]
    if not blocks and not counts:
        return [row(company, family, query_label,
                    snippet="UNANSWERED: 200 but no record blocks and no facet "
                            "badges — markup changed, body saved verbatim",
                    status=200, cls="UNANSWERED")]
    rows = [row(company, family, query_label,
                snippet="FACET COUNTS: All Items=%s, Full View=%s; %d record "
                        "block(s) on this page. HathiTrust full-text search "
                        "returns RECORDS, not snippet text (0 <mark>/snippet "
                        "nodes in the live response), so nothing here is "
                        "readable text until the item itself is opened."
                % (counts.get("all", "?"), counts.get("ft", "?"), len(blocks)),
                status=200, cls="LEAD_ONLY")]
    for x in blocks[:50]:
        def g(p, j=1):
            m = re.search(p, x, re.S)
            return _clean(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ",
                                                     m.group(j))).strip(), 140) if m else ""
        hdl = (re.findall(r'data-hdl="([^"]+)"', x) or [""])[0]
        rec = (re.findall(r'href="https?://catalog\.hathitrust\.org/Record/(\d+)"', x) or [""])[0]
        access = (re.findall(r'data-key="([^"]+)"', x) or [""])[0]
        view = "Full View" if "Full View" in x else (
            "Limited View" if "Limited View" in x else "?")
        rows.append(row(company, family, query_label, item_id=hdl or rec,
                        title=g(r'<h3 class="record-title"[^>]*>(.*?)</h3>'),
                        date=g(r'Published</dt>\s*<dd[^>]*>(.*?)</dd>'),
                        url=("https://babel.hathitrust.org/cgi/pt?id=%s" % hdl
                             if hdl else
                             "https://catalog.hathitrust.org/Record/%s" % rec),
                        snippet="access=%s view=%s | record=%s | author=%s" % (
                            access, view, rec,
                            g(r'Author</dt>\s*<dd[^>]*>(.*?)</dd>') or "-"),
                        status=200, cls="TIER1_CANDIDATE" if view == "Full View"
                        else "LEAD_ONLY"))
    return rows


def _gb_atom_rows(company, query_label, xml, status):
    """Legacy Data API (books.google.com/books/feeds/volumes), Atom.
    What it DOES give: volumeId, title, date, creator, publisher, a
    `gbs:viewability` value (all_pages / partial / no_pages) and, when a
    preview link is present, the PAGE the query matched (`pg=PA138`).
    What it does NOT give keyless: the FULL TEXT of a page. It DOES give
    snippet-level text — corrected 2026-09-25 by re-reading the saved bodies:
    there is no <gbs:snippet>/<gbs:searchResult> node (so an earlier note here
    said "no snippet"), but 44 of the 50 entries in the five verified 200
    responses carry a <dc:description> of 178-283 chars, which is Google's
    matched-page snippet (ellipsis-bounded, e.g. InfoWorld 1983-02-28: "...
    CUPERTINO, CA At its recent shareholders' meeting, Apple Computer used ...
    the Lisa ..."). Snippet != full text: it is a pointer to a page, quotable
    only as what it is. totalResults is Google's display cap (it read 300 for
    three unrelated queries), never a count."""
    entries = re.findall(r"<entry>(.*?)</entry>", xml, re.S)
    total = (re.findall(r"<openSearch:totalResults>(\d+)<", xml) or [""])[0]
    gbs_snips = xml.count("<gbs:snippet") + xml.count("gbs:searchResult")
    snips = sum(1 for x in entries
                if re.search(r"<dc:description>\s*\S", x))

    def g(p, x):
        m = re.search(p, x, re.S)
        return _clean(m.group(1), 140) if m else ""

    if not entries:
        if "<error" in xml or "totalResults" not in xml:
            return [row(company, "google_books", query_label,
                        snippet="UNANSWERED: 200 but the Atom feed carries no "
                                "entries and no totalResults (body saved "
                                "verbatim)", status=status, cls="UNANSWERED")]
        return [row(company, "google_books", query_label,
                    snippet="EMPTY (proven null) FOR THIS QUERY ONLY: feed "
                            "well-formed, 0 volumes (totalResults=%s)" % total,
                    status=status, cls="NULL")]
    rows = [row(company, "google_books", query_label,
                snippet="FEED SUMMARY: %d volume(s) returned, totalResults=%s "
                        "(Google's display cap, NOT a corpus count), "
                        "entries carrying <dc:description> matched-page text=%d, "
                        "gbs:snippet nodes=%d -> keyless Google Books gives "
                        "SNIPPET-LEVEL text only (a ~250-char window on the "
                        "matched page): cite the volume and page, then obtain "
                        "the text elsewhere (IA / HathiTrust / a Books API "
                        "key)." % (len(entries), total or "?", snips, gbs_snips),
                status=status, cls="LEAD_ONLY")]
    for x in entries[:20]:
        # the feed uses BOTH quote styles in attributes (dc:* unquoted text,
        # gbs:* with single quotes) — accept either, or viewability silently
        # reads as '?' and every row demotes itself to a lead.
        vid = g(r"<dc:identifier>([0-9A-Za-z_-]{8,})</dc:identifier>", x)
        pg = (re.findall(r"pg=([A-Za-z0-9]+)", x) or [""])[0]
        # Google's matched-page text for a keyless feed row lives in
        # <dc:description>, NOT in a gbs:snippet node — dropping it (as the
        # first version of this parser did) threw away the only periodical
        # TEXT keyless Books returns and made a snippet read as bare metadata.
        desc = (re.findall(r"<dc:description>(.*?)</dc:description>", x, re.S)
                or [""])[0]
        desc = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", desc)).strip()[:300]
        view = (re.findall(
            r'''gbs:viewability[^>]*value=['"]([^'"]*)#view_(\w+)['"]''', x)
            or [("", "")])[0][1]
        rows.append(row(company, "google_books", query_label, item_id=vid,
                        title=g(r"<dc:title>(.*?)</dc:title>", x)
                        or g(r"<title[^>]*>(.*?)</title>", x),
                        date=g(r"<dc:date>(.*?)</dc:date>", x),
                        url=("https://books.google.com/books?id=%s%s"
                             % (vid, "&pg=%s" % pg if pg else "")),
                        snippet="viewability=%s | matched page=%s | %s | %s%s" % (
                            view or "?", pg or "-",
                            g(r"<dc:publisher>(.*?)</dc:publisher>", x) or "-",
                            g(r"<dc:creator>(.*?)</dc:creator>", x) or "-",
                            (" | snippet=" + _clean(desc, 300)) if desc else ""),
                        status=status, cls="TIER1_CANDIDATE"
                        if view in ("all_pages", "partial") else "LEAD_ONLY"))
    return rows

def parse_gb(company, query_label, body, status, note, extra=None):
    if status == 200 and (b"<feed" in body[:400] or b"openSearch" in body[:600]):
        return _gb_atom_rows(company, query_label,
                             body.decode("utf-8", "replace"), status)
    if status == 200:
        try:
            j = json.loads(body.decode("utf-8", "replace"))
        except Exception as e:
            return [unanswered_or_error(company, "google_books",
                                        query_label, status,
                                        "200 but neither Atom nor JSON: %s" % e,
                                        extra)]
        items = j.get("items") or []
        if j.get("totalItems") == 0:
            return [row(company, "google_books", query_label,
                        snippet="EMPTY (proven null) FOR THIS QUERY ONLY: "
                                "totalItems=0", status=200, cls="NULL")]
        rows = []
        for it in items[:20]:
            vi = it.get("volumeInfo") or {}
            ai = it.get("accessInfo") or {}
            rows.append(row(company, "google_books", query_label,
                            item_id=it.get("id", ""),
                            title=_clean(vi.get("title"), 120),
                            date=str(vi.get("publishedDate", "")),
                            url=vi.get("canonicalVolumeLink", ""),
                            snippet=" ".join(_clean(x, 90) for x in
                                             [vi.get("publisher", ""),
                                              ai.get("previewLink", "")])
                            + " | snippet=%s" % (
                                "yes" if (it.get("searchInfo") or {}).get("textSnippet")
                                else "none"),
                            status=200, cls="LEAD_ONLY"))
        return rows
    if status == 429:
        txt = body.decode("utf-8", "replace")
        compact = re.sub(r"\s+", "", txt)
        quota0 = '"quota_limit_value":"0"' in compact
        return [row(company, "google_books", query_label,
                    snippet="UNANSWERED (NOT a rate limit to back off from): "
                            "HTTP 429 with reason=rateLimitExceeded on the "
                            "quota limit 'Queries per day' whose "
                            "quota_limit_value is 0 for Google's SHARED "
                            "ANONYMOUS project. Keyless books.googleapis.com "
                            "is switched off for everyone, from every egress; "
                            "throttling and retries change nothing. Either "
                            "pass --gb-key / GOOGLE_BOOKS_API_KEY or use the "
                            "verified keyless endpoint "
                            "books.google.com/books/feeds/volumes%s | body: %s"
                            % ("" if quota0 else " (quota detail not parsed)",
                               _clean(txt, 260)),
                    status=429, cls="UNANSWERED")]
    if status == 403:
        return [row(company, "google_books", query_label,
                    snippet="UNANSWERED: HTTP 403 from a books.google.com "
                            "BROWSING (HTML) url — Google's own words are "
                            "'your computer or network may be sending automated "
                            "queries'. Use the feeds endpoint instead; page "
                            "text is not obtainable without a key. %s" % note,
                    status=403, cls="UNANSWERED")]
    return [unanswered_or_error(company, "google_books", query_label,
                                status, note, extra)]

PARSERS = {
    "chronicling_america.search": parse_ca_search,
    "chronicling_america.titles": parse_ca_titles,
    "chronicling_america.bulk": parse_ca_titles,
    "chronicling_america.ocr": parse_ca_ocr,
    "internet_archive.search": parse_ia_search,
    "internet_archive.metadata": parse_ia_meta,
    "corporate_print.search": parse_cp_search,
    "corporate_print.metadata": parse_cp_meta,
    "corporate_print.text": parse_cp_text,
    "hathitrust.search": parse_ht,
    "google_books.search": parse_gb,
}

# --------------------------------------------------------------------------
# Task planning + execution
# --------------------------------------------------------------------------

def planned_url(task, gb_api_key=""):
    k = task["kind"]
    fam = task["source_family"]
    if fam == "chronicling_america":
        p = task["params"]
        if k == "search":
            return ca_search_url(p)
        if k == "titles":
            return ca_titles_url(p)
        if k == "bulk":
            return ca_bulk_url(p)
        if k == "ocr":
            return ca_ocr_url(p["page_path"], p.get("base"))
        raise ValueError("no endpoint mapping for chronicling_america kind %r"
                         % k)
    if k == "search" and fam == "internet_archive":
        return ia_search_url(task["params"]["q"], task["params"].get("rows", 10))
    if k == "metadata" and fam == "internet_archive":
        return ia_meta_url(task["params"]["identifier"])
    if fam == "corporate_print":
        if k == "search":
            return cp_search_url(task["params"])
        if k == "metadata":
            return ia_meta_url(task["params"]["identifier"])
        if k == "text":
            p = task["params"]
            for f in ("server", "dir", "file"):
                if not p.get(f):
                    raise ValueError(
                        "corporate_print text task %s needs %s (copy it "
                        "verbatim from a live archive.org/metadata/<id> "
                        "response; refusing to guess)"
                        % (task.get("query_label"), f))
            return cp_text_url(p["server"], p["dir"], p["file"])
        raise ValueError("no endpoint mapping for corporate_print kind %r" % k)
    if fam == "hathitrust":
        if k == "catalog":
            return ht_brief_url(task["params"]["id_type"],
                                task["params"]["value"])
        return ht_search_url(task["params"])
    if fam == "google_books":
        return gb_search_url(task["params"], api_key=gb_api_key)
    raise ValueError("no endpoint mapping for task %s (refusing to invent one)"
                     % task.get("query_label"))

EXT_BY_SOURCE = {"chronicling_america": ".json", "chronicling_america_ocr": ".txt",
                 "internet_archive": ".json", "corporate_print": ".json",
                 "hathitrust": ".html", "google_books": ".xml"}

PARSERS["hathitrust.catalog"] = parse_ht_brief

def run(config_path, out_root, max_requests, dry_run, delay, insecure,
        only_company=None, cache_dir=None, insecure_hosts=None,
        follow_redirects=False, gb_api_key="", use_curl=False,
        curl_bin="curl", only_families=None):
    with open(config_path, "r", encoding="utf-8") as f:
        cfg = json.load(f)
    tasks = cfg["tasks"]
    if only_company:
        tasks = [t for t in tasks if t["company"] == only_company]
    if only_families:
        want = set(only_families)
        tasks = [t for t in tasks if t["source_family"] in want]
    caps = cfg.get("per_source_caps", {})
    used_by_source = {}
    http = Http(delay=delay, insecure=insecure, insecure_hosts=insecure_hosts,
                follow_redirects=follow_redirects, use_curl=use_curl,
                curl_bin=curl_bin)

    if dry_run:
        print("PLANNED REQUESTS (%d tasks):" % len(tasks))
        for t in tasks:
            print("  [%s/%s] %s -> %s" % (t["company"], t["source_family"],
                                          t["query_label"],
                                          planned_url(t, gb_api_key)))
        by_fam, by_co = {}, {}
        for t in tasks:
            by_fam[t["source_family"]] = by_fam.get(t["source_family"], 0) + 1
            by_co[t["company"]] = by_co.get(t["company"], 0) + 1
        print("\nFamilies: %s" % by_fam)
        print("Companies: %s" % by_co)
        print("Caps: max_requests=%d per_source=%s" % (max_requests, caps))
        return 0

    os.makedirs(out_root, exist_ok=True)
    stamp = run_stamp()
    archives = {}
    results = []
    fam_stats = {}
    def stat(fam):
        return fam_stats.setdefault(fam, {"tasks": 0, "fetched": 0,
                                          "cached": 0, "skipped": 0,
                                          "statuses": {}, "rows": {},
                                          "halted": 0})
    for t in tasks:
        fam = t["source_family"]
        label = t["query_label"]
        company = t["company"]
        s = stat(fam)
        s["tasks"] += 1
        cap = caps.get(fam, max_requests)
        if used_by_source.get(fam, 0) >= cap:
            results.append(row(company, fam, label,
                               snippet="SKIPPED: per-source cap %d reached" % cap,
                               cls="UNANSWERED"))
            s["skipped"] += 1
            s["rows"]["UNANSWERED"] = s["rows"].get("UNANSWERED", 0) + 1
            continue
        if http.halted_reason(planned_url(t, gb_api_key)):
            results.append(row(company, fam, label,
                               snippet="SKIPPED: %s (host halted)"
                                       % http.halted_reason(planned_url(t,
                                                                       gb_api_key)),
                               cls="UNANSWERED"))
            s["skipped"] += 1
            s["halted"] += 1
            s["rows"]["UNANSWERED"] = s["rows"].get("UNANSWERED", 0) + 1
            continue
        url = planned_url(t, gb_api_key)
        if fam not in archives:
            archives[fam] = Archive(out_root, fam, cache_dir=cache_dir,
                                    stamp=stamp)
        ar = archives[fam]
        cached_meta, cached_body = ar.cached(url)
        if cached_meta is not None:
            log("CACHE  %s / %s" % (fam, label))
            status = cached_meta["http_status"]
            body = cached_body
            # the sidecar's note/error_class travel WITH the bytes; an earlier
            # run dropped them, which is how a TLS-trust failure got replayed
            # as a bare status 0 with no explanation.
            note = cached_meta.get("note", "")
            extra = {"error_class": cached_meta.get("error_class", ""),
                     "redirect_location": cached_meta.get("redirect_location", ""),
                     "tls_verify": cached_meta.get("tls_verify", "on"),
                     "client": cached_meta.get("client", "python-urllib"),
                     "request_headers": cached_meta.get("request_headers", {}),
                     "from_cache": True}
            used = 0
            s["cached"] += 1
        else:
            log("FETCH  %s / %s" % (fam, label))
            status, headers, body, note, extra = http.fetch(
                url, max_requests - http.requests_made, family=fam)
            if status == -1:
                results.append(row(company, fam, label,
                                   snippet="SKIPPED: global max-requests cap "
                                           "%d reached" % max_requests,
                                   cls="UNANSWERED"))
                s["skipped"] += 1
                s["rows"]["UNANSWERED"] = s["rows"].get("UNANSWERED", 0) + 1
                continue
            s["fetched"] += 1
            ext = EXT_BY_SOURCE.get(fam, ".bin")
            if t["kind"] == "text":
                ext = ".txt"      # item full text, saved verbatim
            if t["kind"] == "catalog":
                ext = ".json"     # HathiTrust Catalog API answers JSON, not HTML
            saved = ar.save(url, body, status, headers,
                            {"source": fam, "query_label": label,
                             "company": company, "kind": t["kind"]}, ext,
                            note=note, extra=extra)
            note = (note + " " if note else "") + "saved:%s/%s" % (fam, saved)
            used = 1
        s["statuses"][str(status)] = s["statuses"].get(str(status), 0) + 1
        used_by_source[fam] = used_by_source.get(fam, 0) + used
        parser = PARSERS["%s.%s" % (fam, t["kind"])]
        kw = {}
        if fam == "corporate_print":
            kw["window"] = t.get("window")
            if t["kind"] == "search":
                kw["task_params"] = t["params"]
            if t["kind"] == "text":
                kw["identifier"] = t["params"].get("identifier", "")
        elif t["kind"] == "search" and fam == "internet_archive":
            kw["window"] = t.get("window")
        if fam in ("chronicling_america", "hathitrust", "google_books"):
            kw["extra"] = extra
        if parser is parse_ia_search:
            rows = parse_ia_search(company, label, body, status, note, **kw)
        else:
            rows = parser(company, label, body, status, note, **kw)
        for r in rows:
            s["rows"][r["classification"]] = s["rows"].get(
                r["classification"], 0) + 1
        results.extend(rows)

    write_candidates(out_root, results)
    write_manifest(out_root)
    print("\nPER-FAMILY OUTCOMES (this run):")
    for fam in sorted(fam_stats):
        s = fam_stats[fam]
        print("  %-22s tasks=%-3d fetched=%-3d cached=%-3d skipped=%-3d "
              "http=%s rows=%s"
              % (fam, s["tasks"], s["fetched"], s["cached"], s["skipped"],
                 s["statuses"] or "-", s["rows"] or "-"))
        if s["halted"]:
            print("  %-22s ^ %d task(s) never attempted: HOST HALTED"
                  % ("", s["halted"]))
    not_queried = [f for f in fam_stats
                   if fam_stats[f]["fetched"] == 0 and fam_stats[f]["cached"] == 0]
    if not_queried:
        print("  UNQUERIED THIS RUN (recorded UNANSWERED, NOT null): %s"
              % ", ".join(sorted(not_queried)))
    print("\nDONE. network requests: %d / cap %d   (cache: %s)"
          % (http.requests_made, max_requests,
             ("--cache-dir %s: %d replayed" % (cache_dir, sum(
                 s["cached"] for s in fam_stats.values())))
             if cache_dir else
             "OFF, so every row below is a live answer from this egress"))
    print("  evidence written: %d file(s), unchanged: %d, versioned-beside-existing: %d"
          % (sum(a.written for a in archives.values()),
             sum(a.unchanged for a in archives.values()),
             sum(a.versioned for a in archives.values())))
    if http.halted:
        print("  hosts halted: %s" % ", ".join(sorted(http.halted)))
    by_cls = {}
    for r in results:
        by_cls[r["classification"]] = by_cls.get(r["classification"], 0) + 1
    print("candidate rows: %d  %s" % (len(results), by_cls))
    return 0

def write_candidates(out_root, new_rows):
    path = os.path.join(out_root, "candidates.csv")
    old = []
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8", newline="") as f:
            old = list(csv.DictReader(f))
    seen = set()
    merged = []
    for r in new_rows + old:
        key = (r.get("company"), r.get("source_family"), r.get("query"),
               r.get("item_id"), r.get("classification"))
        if key in seen:
            continue
        seen.add(key)
        merged.append(r)
    merged.sort(key=lambda r: (r.get("company", ""), r.get("source_family", ""),
                               r.get("retrieved_at", "")))
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        w.writeheader()
        for r in merged:
            w.writerow({k: r.get(k, "") for k in CSV_FIELDS})
    log("wrote %s (%d rows)" % (path, len(merged)))

def write_manifest(out_root):
    rows = []
    for dirpath, dirnames, filenames in os.walk(out_root):
        dirnames.sort()
        for name in sorted(filenames):
            if not name.endswith(".meta.json"):
                continue
            with open(os.path.join(dirpath, name), "r", encoding="utf-8") as f:
                meta = json.load(f)
            rel = os.path.relpath(os.path.join(dirpath, name
                                               [:-len(".meta.json")]), out_root)
            rows.append((rel.replace("\\", "/"), meta.get("source", ""),
                         meta.get("query_label", ""), meta.get("company", ""),
                         meta.get("http_status", ""), meta.get("bytes", 0),
                         meta.get("content_type", ""), meta.get("retrieved_at", "")))
    lines = ["# HARVEST MANIFEST — 00_universe/harvest",
             "",
             "Regenerated by periodical_harvest.py at %s. Every raw response"
             % now_utc(),
             "body saved verbatim; .meta.json sidecars are not listed.",
             "",
             "| File | Source | Query | Company | HTTP status | Bytes | Content-Type | Retrieved (UTC) |",
             "|---|---|---|---|---|---|---|---|"]
    for r in rows:
        lines.append("| " + " | ".join(str(x) for x in r) + " |")
    lines.append("")
    lines.append("_MANIFEST.md itself: %d evidence files listed." % len(rows))
    with open(os.path.join(out_root, "_MANIFEST.md"), "w",
              encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")
    log("wrote manifest (%d files)" % len(rows))

def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    here = os.path.dirname(os.path.abspath(__file__))
    ap.add_argument("--config", default=os.path.join(here, "queries.json"))
    ap.add_argument("--out", default=os.path.normpath(
        os.path.join(here, "..", "founders_playbook", "00_universe", "harvest")))
    ap.add_argument("--max-requests", type=int, default=300)
    ap.add_argument("--delay", type=float, default=2.0,
                    help="per-host delay seconds (politeness)")
    ap.add_argument("--company", default=None)
    ap.add_argument("--source-family", action="append", default=None,
                    metavar="FAMILY",
                    help="run only these source families (repeatable), e.g. "
                         "--source-family hathitrust --source-family "
                         "google_books — so one route can be re-proved without "
                         "spending requests on the others")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--cache-dir", default=None,
                    help="opt-in response cache. OFF by default since 2026-09-25: "
                         "the cache used to be the committed evidence folder, so a "
                         "scheduled run on a fresh checkout replayed the previous "
                         "machine's failures and reported them as its own results. "
                         "Point it OUTSIDE the repo if you must use it.")
    ap.add_argument("--insecure", action="store_true",
                    help="skip TLS verification for every host (last resort; the "
                         "sidecars record tls_verify=skipped so the evidence says "
                         "so too). Prefer --insecure-hosts.")
    ap.add_argument("--insecure-hosts", default="",
                    help="comma-separated hosts to skip TLS verification for, e.g. "
                         "babel.hathitrust.org — for boxes whose CA bundle or clock "
                         "makes a valid chain look expired. Never silent: each "
                         "response is saved with tls_verify=skipped.")
    ap.add_argument("--follow-redirects", action="store_true",
                    help="restore the old silent-redirect behaviour (off by "
                         "default: a 3xx is now reported with its Location)")
    ap.add_argument("--gb-key", default=os.environ.get("GOOGLE_BOOKS_API_KEY", ""),
                    help="Google Books API key (or env GOOGLE_BOOKS_API_KEY) for "
                         "the books.googleapis.com v1 endpoint; keyless v1 is "
                         "quota-0 and answers 429")
    ap.add_argument("--use-curl", action="store_true",
                    help="when this host refuses the Python client with a "
                         "Cloudflare challenge, ask again through the curl "
                         "binary (a second ordinary client, not a spoofed "
                         "browser fingerprint) and record client=curl in the "
                         "sidecar. Needed for babel.hathitrust.org /cgi/ls "
                         "from this machine; see HARVEST_README.md.")
    ap.add_argument("--curl-bin", default="curl")
    args = ap.parse_args()
    try:
        sys.stdout.reconfigure(errors="replace")   # cp1252 consoles
    except Exception:
        pass
    hosts = [h.strip() for h in args.insecure_hosts.split(",") if h.strip()]
    sys.exit(run(args.config, args.out, args.max_requests, args.dry_run,
                 args.delay, args.insecure, args.company,
                 cache_dir=args.cache_dir, insecure_hosts=hosts,
                 follow_redirects=args.follow_redirects,
                 gb_api_key=args.gb_key, use_curl=args.use_curl,
                 curl_bin=args.curl_bin, only_families=args.source_family))

if __name__ == "__main__":
    main()
