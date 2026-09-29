#!/usr/bin/env python3
"""
ca_endpoint_probe.py -- decide, by measurement, which Chronicling America URL shape actually answers.

Why this exists. `periodical_harvest.py` builds
`https://www.loc.gov/chroniclingamerica/search/pages/results/?format=json&...` and for three consecutive
nightly runs (2026-09-27, -28, -29) that path returned `Page Not Found -- 404 -- Library of Congress`
HTML. 209 CA rows, 0 answers, 122 UNANSWERED. A 404 is not a bot block: it means the path we send does
not exist, so "LOC refuses this project" has been unsupported since the day it was first written down,
and every retry from any egress will keep returning the same 404 until the PATH changes (RD-128).

Why it runs on CI and not here. From this machine all four candidate shapes returned **403** (the LoC
zone sits behind Cloudflare bot management for datacentre/home IPs), so a local test cannot distinguish
a wrong path from a blocked client -- which is exactly the confusion that let the 404 masquerade as a
block for five days. GitHub Actions egress got far enough to return a real LoC 404 page, so it can read
a real 200 too. This script therefore ships a candidate list, tries each once, and prints which shape
answered, with the hit count it reported.

It changes nothing else: it does not touch `periodical_harvest.py`, does not write into the corpus
evidence trees, and its only output is a verdict file. Read the verdict, then fix one constant.
"""

import datetime
import gzip
import io
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(REPO, "founders_playbook", "00_universe", "harvest", "_CA_ENDPOINT_TEST.md")

UA = "FounderPlaybook Research AdminContact@example.com"
HEADERS = {"User-Agent": UA, "Accept": "application/json, text/plain, */*",
           "Accept-Encoding": "gzip", "Referer": "https://www.loc.gov/"}

# A query that MUST hit something if the route works: Chronicling America advertises open OCR full text
# of US newspapers 1777-2016, and "Walmart" plus "Bentonville" is a phrase the corpus is being mined for.
PROBE = {"andtext": '"Wal-Mart" Bentonville', "q": '"Wal-Mart" Bentonville'}
YEARS = ("1960", "1969")

# Each entry: (label, template). {andtext} / {q} are filled URL-encoded; the date params are appended
# where the shape supports them. Ordered: current site first, then legacy, then LoC's global search.
SHAPES = [
    ("loc-global-chronicling-america",
     "https://www.loc.gov/collections/chronicling-america/search/?fo=json&{q}&start=0"),
    ("loc-global-fa-collection",
     "https://www.loc.gov/search/?fo=json&fa=collection%3Achronicling-america&{q}"),
    ("ca-legacy-pages-results",
     "https://chroniclingamerica.loc.gov/search/pages/results/?format=json&{andtext}"
     "&date1=1960&date2=1969&dateFilterType=yearRange&rows=5"),
    ("ca-legacy-newspapers-api",
     "https://chroniclingamerica.loc.gov/newspapers/?fo=json&{q}"),
    ("cronidam-new-api",
     "https://chroniclingamerica.loc.gov/cronidam/?fo=json&{q}"),
    ("www-chroniclingamerica-path",
     "https://www.loc.gov/chroniclingamerica/search/pages/results/?format=json&{andtext}&rows=5"),
    ("www-collections-page-json",
     "https://www.loc.gov/collections/chronicling-america/search/?fo=json&page=1&q=wal-mart"),
]


def fill(tmpl):
    andtext = "andtext=" + urllib.parse.quote(PROBE["andtext"])
    q = "q=" + urllib.parse.quote(PROBE["q"])
    return tmpl.replace("{andtext}", andtext).replace("{q}", q)


def fetch(url, timeout=60):
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as f:
            body = f.read()
            if f.headers.get("Content-Encoding") == "gzip":
                try:
                    body = gzip.decompress(body)
                except Exception:
                    pass
            return f.status, f.geturl(), body
    except urllib.error.HTTPError as e:
        try:
            b = e.read()
            if e.headers.get("Content-Encoding") == "gzip":
                b = gzip.decompress(b)
        except Exception:
            b = b""
        return e.code, url, b
    except Exception as e:
        return None, url, ("%s: %s" % (type(e).__name__, e)).encode("utf-8", "replace")


def classify(status, body):
    t = (body or b"")[:4000].decode("utf-8", "replace")
    if status is None:
        return "ROUTE-FAILED", t[:120]
    if "Just a moment" in t or "Attention Required" in t or "cf-browser-verification" in t.lower():
        return "CHALLENGED", "Cloudflare bot challenge"
    if status == 404 or "Page Not Found" in t:
        return "NOT-FOUND", "404 -- the path does not exist (our own defect, not a block)"
    if status in (403,):
        return "FORBIDDEN", "403 -- refused at this egress"
    if status in (301, 302, 303, 307, 308):
        return "REDIRECT", t[:100]
    stripped = t.lstrip()
    if stripped[:1] in "{[":
        try:
            j = json.loads((body or b"").decode("utf-8", "replace"))
        except Exception:
            return "JSON-UNPARSED", t[:120]
        for key in ("totalRecords", "numFound", "count"):
            if isinstance(j, dict) and key in j:
                return "ANSWERED", "%s=%s" % (key, j[key])
        # LoC's global search nests the count under "api"/"pagination"; look for any integer that
        # clearly claims a result total rather than guessing a schema.
        m = re.search(r'"(?:total|pagination)"\s*:\s*\{[^{}]*?"(?:total|count)"\s*:\s*(\d+)',
                      json.dumps(j)[:4000], re.S)
        if m:
            return "ANSWERED", "total=%s" % m.group(1)
        n = len(j) if isinstance(j, (list, dict)) else 0
        return "ANSWERED", "json parsed, top-level size=%d (schema unknown -- read it before counting)" % n
    return "NOT-JSON", "status=%s, first bytes: %s" % (status, t[:100])


def main():
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    rows, best = [], []
    print("Chronicling America endpoint probe -- %s\n" % stamp)
    for label, tmpl in SHAPES:
        url = fill(tmpl)
        status, final, body = fetch(url)
        verdict, detail = classify(status, body)
        rows.append((label, verdict, status, len(body or b""), detail, url, final))
        print("  %-30s %-12s %s %8s B  %s" % (label, verdict, status or "-",
                                              format(len(body or b""), ","), detail[:88]))
        if verdict == "ANSWERED":
            best.append(label)

    lines = ["# Chronicling America endpoint test -- %s" % stamp, "",
             "Run from the GitHub Actions egress (or any host) to decide which URL shape answers, because",
             "from this project's development machine every shape 403s and a 403 cannot be told apart from",
             "a wrong path. `periodical_harvest.py` currently uses `www.loc.gov/chroniclingamerica` +",
             "`/search/pages/results/?format=json`, which has returned **404** on every nightly run so far",
             "(2026-09-27, -28, -29), so its 209 CA rows carry 0 answers and 122 UNANSWERED.", "",
             "| shape | verdict | status | bytes | detail |", "|---|---|---|---|---|"]
    for label, verdict, status, n, detail, url, final in rows:
        lines.append("| `%s` | %s | %s | %s | %s |" % (
            label, verdict, status or "-", format(n, ","), detail.replace("|", "/")[:120]))
    lines += ["", "**Probe query:** `%s` (%s-%s), chosen because the corpus is being mined for exactly "
              "this phrase and the collection advertises open OCR full text 1777-2016 -- so a working "
              "route should not return zero." % (PROBE["andtext"], *YEARS), "",
              "**Reading the verdict:**",
              "- `ANSWERED` -- this shape is the one to use. Open the body, find the total field, and "
              "point `CA_BASE` / `ca_search_url` at it; then re-run the CA tasks and re-classify.",
              "- `NOT-FOUND` -- path defect (ours). Not evidence about the corpus.",
              "- `FORBIDDEN`/`CHALLENGED` -- egress block. Still UNANSWERED, never a null, and it does "
              "not mean the path is wrong.",
              "- `NOT-JSON` -- right host, wrong format parameter.",
              "- A count from a shape whose schema you have not opened is NOT a null. Read the body first "
              "(RD-121/RD-124: three fleet verdicts came from trusting a number nobody had opened).", "",
              "**ANSWERED shapes:** %s" % (", ".join("`%s`" % b for b in best) if best
                                           else "**none** -- every candidate failed; the route is still "
                                           "UNTRIED and no CA zero may be cited as a null."), ""]
    with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")
    print("\nwrote %s" % os.path.relpath(OUT, REPO))
    return 0 if best else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main())
