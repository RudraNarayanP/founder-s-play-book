#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
periodical_harvest.py — THE FOUNDER'S PLAYBOOK batch harvester for digitised
pre-1994 periodicals (method file 00_METHOD_AND_STYLE.md §14 rule 6: the
periodical corpus family that EDGAR and web archives cannot see).

Stdlib only. Read-only public search APIs only. Polite by construction:
  * per-host delay (default 2 s), honest User-Agent with contact placeholder
  * exponential backoff on 429/503 honouring Retry-After
  * hard stop after 5 consecutive failures per host
  * --max-requests cost cap (default 300), --dry-run planner
  * URL-hash cache: re-running is cheap and idempotent
  * raw evidence bytes saved verbatim beside a .meta.json sidecar
  * EMPTY (proven null) is NEVER conflated with UNANSWERED (blocked /
    rate-limited / not-implemented) — §14 failure-honesty rule

Sources implemented (endpoint shapes verified by live calls or, where the
host is Cloudflare-blocked from this network, by archived REAL response
bytes — see HARVEST_README.md for the verification record of each):
  chronicling_america   LoC page search  (OpenSearch params per official docs)
  chronicling_america_ocr  per-page ocr.txt text (documented link pattern)
  internet_archive      advancedsearch.php JSON + metadata/{id} + item text
  corporate_print       digitised BOUND CORPORATE PRINT (annual / shareholder
                        reports, 10-Ks, prospectuses, corporate research
                        print) over the same Internet Archive metadata index:
                        company terms + report-type terms + YEAR range, then
                        identifier -> metadata -> *_djvu.txt availability ->
                        direct-server text URL
  hathitrust            babel /cgi/ls/one q1 search (params read off the
                        site's own archived search form; HTML response)
  google_books          volumes query v1 (expected to rate-limit; handled)

  The fifth family exists because it is the one that REVERSED a depth verdict:
  the complete printed Wal-Mart Stores annual-report run FY1972-FY1997 sits
  text-searchable on Internet Archive
  (company_002_walmart/research/B_periodical_retest.md), and the probe that
  rated Walmart forensic-core had never queried digitised books or bound
  corporate print at all.  An unqueried family is UNANSWERED, never NULL.

Run:  python periodical_harvest.py --config queries.json [--dry-run]
Output: founders_playbook/00_universe/harvest/<source_family>/<sha1>.<ext>
        + <sha1>.meta.json sidecars, candidates.csv, _MANIFEST.md
"""

import argparse
import csv
import hashlib
import json
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

USER_AGENT = ("FoundersPlaybook-harvest/1.0 "
              "(research tool for THE FOUNDER'S PLAYBOOK; "
              "contact: research@example.org)")
CSV_FIELDS = ["company", "source_family", "query", "item_id", "title",
              "date_or_issue", "url", "snippet_or_hitcount", "http_status",
              "classification", "retrieved_at"]
CONSEC_FAIL_LIMIT = 5
MAX_RETRIES = 4            # attempts on 429/503 (incl. first try)
MAX_RETRY_AFTER_HONOUR = 60   # seconds; beyond this we stop and record UNANSWERED

def now_utc():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

def url_hash(url):
    return hashlib.sha1(url.encode("utf-8")).hexdigest()[:16]

def log(msg):
    print("[%s] %s" % (now_utc(), msg), flush=True)

# --------------------------------------------------------------------------
# HTTP machinery — polite by construction
# --------------------------------------------------------------------------

class Http:
    def __init__(self, delay, insecure=False):
        self.delay = delay
        self.insecure = insecure
        self.last_seen = {}      # host -> monotonic of last request
        self.consec_fail = {}    # host -> consecutive failure count
        self.halted = {}         # host -> reason string
        self.requests_made = 0   # network requests actually performed
        self.ctx = None

    def _ssl_ctx(self):
        if self.ctx is None:
            self.ctx = ssl.create_default_context()
            if self.insecure:
                self.ctx.check_hostname = False
                self.ctx.verify_mode = ssl.CERT_NONE
        return self.ctx

    @staticmethod
    def host_of(url):
        return urllib.parse.urlsplit(url).netloc

    def halted_reason(self, url):
        return self.halted.get(self.host_of(url))

    def fetch(self, url, budget_left):
        """Return (status, headers_dict, body_bytes, note). Never raises.
        status==0 -> network-level failure (UNANSWERED)."""
        host = self.host_of(url)
        if self.requests_made >= budget_left:
            return -1, {}, b"", "global max-requests cap reached"
        # per-host politeness delay
        wait = self.delay - (time.monotonic() - self.last_seen.get(host, 0.0))
        if wait > 0:
            time.sleep(wait)
        status, body, headers, note = 0, b"", {}, ""
        for attempt in range(MAX_RETRIES):
            self.requests_made += 1
            self.last_seen[host] = time.monotonic()
            req = urllib.request.Request(url, headers={
                "User-Agent": USER_AGENT, "Accept": "*/*"})
            try:
                with urllib.request.urlopen(req, timeout=45,
                                            context=self._ssl_ctx()) as r:
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
                if status in (429, 503):
                    ra = headers.get("Retry-After", "")
                    try:
                        ra_s = int(float(ra))
                    except (TypeError, ValueError):
                        ra_s = 0
                    if ra_s > MAX_RETRY_AFTER_HONOUR:
                        note = "Retry-After %ss exceeds honour cap; stopped" % ra_s
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
                ename = type(e).__name__
                if "CERTIFICATE_VERIFY_FAILED" in str(e):
                    ename += " (TLS cert verify failed in this environment)"
                note = "network error: %s" % ename
                time.sleep(2 ** attempt)
                continue
        # classify for consecutive-failure / hard stop
        blocked = (status == 403 and b"Just a moment" in body) or \
                  (status == 403 and b"cf-challenge" in body)
        failure = status == 0 or status in (429, 503) or status >= 500 or blocked
        cf = self.consec_fail.get(host, 0)
        self.consec_fail[host] = 0 if not failure else cf + 1
        if blocked and not note:
            note = "HTTP 403 Cloudflare challenge (blocked, not null)"
        if self.consec_fail[host] >= CONSEC_FAIL_LIMIT and host not in self.halted:
            self.halted[host] = "hard stop: %d consecutive failures" % CONSEC_FAIL_LIMIT
            log("  HOST HALTED: %s — %s" % (host, self.halted[host]))
        return status, headers, body, note

# --------------------------------------------------------------------------
# Raw-evidence persistence + cache
# --------------------------------------------------------------------------

class Archive:
    def __init__(self, out_root, source_family):
        self.dir = os.path.join(out_root, source_family)
        os.makedirs(self.dir, exist_ok=True)

    def cached(self, url):
        h = url_hash(url)
        meta_p = os.path.join(self.dir, h + ".meta.json")
        if os.path.exists(meta_p):
            try:
                with open(meta_p, "r", encoding="utf-8") as f:
                    meta = json.load(f)
                body_p = os.path.join(self.dir, h + meta.get("ext", ".bin"))
                if os.path.exists(body_p):
                    with open(body_p, "rb") as f:
                        return meta, f.read()
            except Exception:
                return None, None
        return None, None

    def save(self, url, body, status, headers, meta_ctx, ext):
        h = url_hash(url)
        body_p = os.path.join(self.dir, h + ext)
        with open(body_p, "wb") as f:
            f.write(body)          # verbatim — never normalised
        meta = {
            "url": url,
            "http_status": status,
            "content_type": headers.get("Content-Type", ""),
            "bytes": len(body),
            "retrieved_at": now_utc(),
            "ext": ext,
        }
        meta.update(meta_ctx)
        with open(os.path.join(self.dir, h + ".meta.json"), "w",
                  encoding="utf-8") as f:
            json.dump(meta, f, indent=1, ensure_ascii=False)
        return h + ext

# --------------------------------------------------------------------------
# Source adapters. Each: build_urls(cfg) + parse(source_family, body,
# status, note) -> list of candidate row dicts.
# Verified-parameter endpoints only; see HARVEST_README.md verification log.
# --------------------------------------------------------------------------

CA_BASE = "https://chroniclingamerica.loc.gov"

def ca_search_url(params):
    # Official documented params: andtext, date1, date2, dateFilterType,
    # state, sort, page, format. (Values confirmed against archived real
    # request URLs; response shape confirmed from archived 2021 response.)
    q = {"format": "json"}
    q.update(params)
    return CA_BASE + "/search/pages/results/?" + urllib.parse.urlencode(q)

def ca_ocr_url(page_path):
    # Documented link pattern /lccn/<sn>/<date>/ed-<e>/seq-<s>/ + ocr.txt
    return CA_BASE + page_path.rstrip("/") + "/ocr.txt"

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

def ht_search_url(term):
    # q1 / searchtype / target / ft read from the site's own GET search form
    # (archived 2019 /cgi/ls page). Response is HTML; parsed only by a
    # conservative result-count regex — anything else is recorded UNANSWERED.
    return ("https://babel.hathitrust.org/cgi/ls/one?" +
            urllib.parse.urlencode({"q1": term, "searchtype": "all",
                                    "target": "ls", "ft": "ft"}))

def gb_search_url(qstr, max_results):
    return ("https://www.googleapis.com/books/v1/volumes?" +
            urllib.parse.urlencode({"q": qstr, "maxResults": max_results}))

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

def unanswered_or_error(company, family, query, status, note):
    cls = "ERROR" if (400 <= (status or 0) < 500 and status not in (403, 429)) \
        else "UNANSWERED"
    return row(company, family, query,
               snippet="UNANSWERED: %s" % (note or "no answer from endpoint"),
               status=status, cls=cls)

# --------------------------------------------------------------------------
# Parsers
# --------------------------------------------------------------------------

def parse_ca_search(company, query_label, body, status, note):
    if status != 200:
        return [unanswered_or_error(company, "chronicling_america",
                                    query_label, status, note)]
    try:
        j = json.loads(body.decode("utf-8", "replace"))
    except Exception as e:
        return [unanswered_or_error(company, "chronicling_america",
                                    query_label, status, "unparseable JSON: %s" % e)]
    items = j.get("items") or []
    total = j.get("totalItems")
    if total is None and not items:
        return [unanswered_or_error(company, "chronicling_america",
                                    query_label, status,
                                    "response shape unrecognised (blocked/legacy?)")]
    if total == 0:
        return [row(company, "chronicling_america", query_label,
                    snippet="EMPTY (proven null): 0 pages for these params",
                    status=200, cls="NULL")]
    rows = []
    for it in items[:50]:
        d = str(it.get("date") or "")
        iso = "%s-%s-%s" % (d[0:4], d[4:6], d[6:8]) if len(d) >= 8 else d
        rows.append(row(
            company, "chronicling_america", query_label,
            item_id="%s %s seq-%s" % (it.get("lccn", ""), iso, it.get("sequence", "")),
            title=_clean(it.get("title"), 120),
            date=iso,
            url=CA_BASE + (it.get("id") or ""),
            snippet=_clean(it.get("ocr_eng") or it.get("snippet") or ""),
            status=200, cls="TIER1_CANDIDATE"))
    return rows

def parse_ca_ocr(company, query_label, body, status, note):
    if status != 200:
        return [unanswered_or_error(company, "chronicling_america_ocr",
                                    query_label, status, note)]
    text = body.decode("utf-8", "replace")
    return [row(company, "chronicling_america_ocr", query_label,
                snippet="OCR %d bytes: %s" % (len(body), _clean(text, 150)),
                status=200, cls="TIER1_CANDIDATE")]

def parse_ia_search(company, query_label, body, status, note, window=None,
                    family="internet_archive", gate=None):
    if status != 200:
        return [unanswered_or_error(company, family, query_label, status, note)]
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

def parse_ht(company, query_label, body, status, note):
    # HathiTrust /cgi/ls returns HTML; response schema was NOT confirmable
    # from this network (Cloudflare 403). We record the challenge honestly.
    if status == 403 or (status == 200 and b"Just a moment" in body):
        return [row(company, "hathitrust", query_label,
                    snippet="UNANSWERED: HTTP 403 Cloudflare challenge "
                            "(blocked from this network; not a null)",
                    status=status or 403, cls="UNANSWERED")]
    if status != 200:
        return [unanswered_or_error(company, "hathitrust", query_label,
                                    status, note)]
    html = body.decode("utf-8", "replace")
    m = re.search(r"([\d,]+)\s+(?:results|items)", html, re.I)
    if not m:
        return [row(company, "hathitrust", query_label,
                    snippet="UNANSWERED: 200 but result count unparseable "
                            "(HTML schema unverified — body saved verbatim)",
                    status=200, cls="UNANSWERED")]
    n = int(m.group(1).replace(",", ""))
    if n == 0:
        return [row(company, "hathitrust", query_label,
                    snippet="EMPTY (proven null): 0 results", status=200,
                    cls="NULL")]
    return [row(company, "hathitrust", query_label,
                snippet="hitcount %d (item list not parsed: schema unverified)"
                        % n, status=200, cls="LEAD_ONLY")]

def parse_gb(company, query_label, body, status, note):
    if status == 200:
        try:
            j = json.loads(body.decode("utf-8", "replace"))
        except Exception as e:
            return [unanswered_or_error(company, "google_books",
                                        query_label, status, "unparseable: %s" % e)]
        items = j.get("items") or []
        if j.get("totalItems") == 0:
            return [row(company, "google_books", query_label,
                        snippet="EMPTY (proven null): totalItems=0",
                        status=200, cls="NULL")]
        rows = []
        for it in items[:20]:
            vi = it.get("volumeInfo") or {}
            rows.append(row(company, "google_books", query_label,
                            item_id=it.get("id", ""),
                            title=_clean(vi.get("title"), 120),
                            date=str(vi.get("publishedDate", "")),
                            url=vi.get("canonicalVolumeLink", ""),
                            snippet=" ".join(_clean(x, 90) for x in
                                             [vi.get("publisher", ""),
                                              vi.get("preview", "")]),
                            status=200, cls="LEAD_ONLY"))
        return rows
    if status == 429:
        return [row(company, "google_books", query_label,
                    snippet="UNANSWERED: HTTP 429 rate-limited — "
                            "not a null (see body: quota message)",
                    status=429, cls="UNANSWERED")]
    return [unanswered_or_error(company, "google_books", query_label,
                                status, note)]

PARSERS = {
    "chronicling_america.search": parse_ca_search,
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

def planned_url(task):
    k = task["kind"]
    if k == "search" and task["source_family"] == "chronicling_america":
        return ca_search_url(task["params"])
    if k == "ocr" and task["source_family"] == "chronicling_america":
        return ca_ocr_url(task["params"]["page_path"])
    if k == "search" and task["source_family"] == "internet_archive":
        return ia_search_url(task["params"]["q"], task["params"].get("rows", 10))
    if k == "metadata" and task["source_family"] == "internet_archive":
        return ia_meta_url(task["params"]["identifier"])
    if task["source_family"] == "corporate_print":
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
    if task["source_family"] == "hathitrust":
        return ht_search_url(task["params"]["q1"])
    if task["source_family"] == "google_books":
        return gb_search_url(task["params"]["q"], task["params"].get("max_results", 10))
    raise ValueError("no endpoint mapping for task %s (refusing to invent one)"
                     % task.get("query_label"))

EXT_BY_SOURCE = {"chronicling_america": ".json", "chronicling_america_ocr": ".txt",
                 "internet_archive": ".json", "corporate_print": ".json",
                 "hathitrust": ".html", "google_books": ".json"}

def run(config_path, out_root, max_requests, dry_run, delay, insecure,
        only_company=None):
    with open(config_path, "r", encoding="utf-8") as f:
        cfg = json.load(f)
    tasks = cfg["tasks"]
    if only_company:
        tasks = [t for t in tasks if t["company"] == only_company]
    caps = cfg.get("per_source_caps", {})
    used_by_source = {}
    http = Http(delay=delay, insecure=insecure)

    if dry_run:
        print("PLANNED REQUESTS (%d tasks):" % len(tasks))
        for t in tasks:
            print("  [%s/%s] %s -> %s" % (t["company"], t["source_family"],
                                          t["query_label"], planned_url(t)))
        by_fam, by_co = {}, {}
        for t in tasks:
            by_fam[t["source_family"]] = by_fam.get(t["source_family"], 0) + 1
            by_co[t["company"]] = by_co.get(t["company"], 0) + 1
        print("\nFamilies: %s" % by_fam)
        print("Companies: %s" % by_co)
        print("Caps: max_requests=%d per_source=%s" % (max_requests, caps))
        return 0

    os.makedirs(out_root, exist_ok=True)
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
        if http.halted_reason(planned_url(t)):
            results.append(row(company, fam, label,
                               snippet="SKIPPED: %s (host halted)"
                                       % http.halted_reason(planned_url(t)),
                               cls="UNANSWERED"))
            s["skipped"] += 1
            s["halted"] += 1
            s["rows"]["UNANSWERED"] = s["rows"].get("UNANSWERED", 0) + 1
            continue
        url = planned_url(t)
        if fam not in archives:
            archives[fam] = Archive(out_root, fam)
        ar = archives[fam]
        cached_meta, cached_body = ar.cached(url)
        if cached_meta is not None:
            log("CACHE  %s / %s" % (fam, label))
            status = cached_meta["http_status"]
            body = cached_body
            note = ""
            used = 0
            s["cached"] += 1
        else:
            log("FETCH  %s / %s" % (fam, label))
            status, headers, body, note = http.fetch(url, max_requests -
                                                     http.requests_made)
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
            saved = ar.save(url, body, status, headers,
                            {"source": fam, "query_label": label,
                             "company": company, "kind": t["kind"]}, ext)
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
    print("\nDONE. network requests: %d / cap %d" % (http.requests_made,
                                                     max_requests))
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
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--insecure", action="store_true",
                    help="skip TLS verification (some archive CDN certs are "
                         "broken in some environments; use knowingly)")
    args = ap.parse_args()
    sys.exit(run(args.config, args.out, args.max_requests, args.dry_run,
                 args.delay, args.insecure, args.company))

if __name__ == "__main__":
    main()
