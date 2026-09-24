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
  hathitrust            babel /cgi/ls/one q1 search (params read off the
                        site's own archived search form; HTML response)
  google_books          volumes query v1 (expected to rate-limit; handled)

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

def parse_ia_search(company, query_label, body, status, note, window=None):
    if status != 200:
        return [unanswered_or_error(company, "internet_archive",
                                    query_label, status, note)]
    try:
        j = json.loads(body.decode("utf-8", "replace"))
        resp = j["response"]
    except Exception as e:
        return [unanswered_or_error(company, "internet_archive",
                                    query_label, status, "unparseable: %s" % e)]
    docs = resp.get("docs") or []
    if resp.get("numFound") == 0:
        return [row(company, "internet_archive", query_label,
                    snippet="EMPTY (proven null): numFound=0",
                    status=200, cls="NULL")]
    rows = []
    for d in docs:
        date = (d.get("date") or str(d.get("year") or ""))[:10]
        cls = "LEAD_ONLY"   # metadata pointer, text not yet opened
        if window and date[:4].isdigit():
            y = int(date[:4])
            if window[0] <= y <= window[1] and d.get("mediatype") == "texts":
                cls = "TIER1_CANDIDATE"
        rows.append(row(company, "internet_archive", query_label,
                        item_id=d.get("identifier", ""),
                        title=_clean(d.get("title"), 120), date=date,
                        url="https://archive.org/details/" + d.get("identifier", ""),
                        snippet=_clean(", ".join(map(str,
                              [d.get("mediatype"), d.get("collection")])), 120),
                        status=200, cls=cls))
    return rows

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
    if task["source_family"] == "hathitrust":
        return ht_search_url(task["params"]["q1"])
    if task["source_family"] == "google_books":
        return gb_search_url(task["params"]["q"], task["params"].get("max_results", 10))
    raise ValueError("no endpoint mapping for task %s (refusing to invent one)"
                     % task.get("query_label"))

EXT_BY_SOURCE = {"chronicling_america": ".json", "chronicling_america_ocr": ".txt",
                 "internet_archive": ".json", "hathitrust": ".html",
                 "google_books": ".json"}

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
        print("Caps: max_requests=%d per_source=%s" % (max_requests, caps))
        return 0

    os.makedirs(out_root, exist_ok=True)
    archives = {}
    results = []
    for t in tasks:
        fam = t["source_family"]
        label = t["query_label"]
        company = t["company"]
        cap = caps.get(fam, max_requests)
        if used_by_source.get(fam, 0) >= cap:
            results.append(row(company, fam, label,
                               snippet="SKIPPED: per-source cap %d reached" % cap,
                               cls="UNANSWERED"))
            continue
        if http.halted_reason(planned_url(t)):
            results.append(row(company, fam, label,
                               snippet="SKIPPED: %s (host halted)"
                                       % http.halted_reason(planned_url(t)),
                               cls="UNANSWERED"))
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
        else:
            log("FETCH  %s / %s" % (fam, label))
            status, headers, body, note = http.fetch(url, max_requests -
                                                     http.requests_made)
            if status == -1:
                results.append(row(company, fam, label,
                                   snippet="SKIPPED: global max-requests cap "
                                           "%d reached" % max_requests,
                                   cls="UNANSWERED"))
                continue
            ext = EXT_BY_SOURCE.get(fam, ".bin")
            saved = ar.save(url, body, status, headers,
                            {"source": fam, "query_label": label,
                             "company": company, "kind": t["kind"]}, ext)
            note = (note + " " if note else "") + "saved:%s/%s" % (fam, saved)
            used = 1
        used_by_source[fam] = used_by_source.get(fam, 0) + used
        parser = PARSERS["%s.%s" % (fam, t["kind"])]
        kw = {}
        if t["kind"] == "search" and fam == "internet_archive":
            kw["window"] = t.get("window")
        if parser is parse_ia_search:
            rows = parse_ia_search(company, label, body, status, note, **kw)
        else:
            rows = parser(company, label, body, status, note)
        results.extend(rows)

    write_candidates(out_root, results)
    write_manifest(out_root)
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
