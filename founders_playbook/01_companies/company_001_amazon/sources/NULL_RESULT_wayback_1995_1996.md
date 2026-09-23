# NULL RESULT — Wayback Machine, pre-1999 amazon.com page (research debt RD-006)

**Query date / access date:** 2026-09-23
**Retrieved by:** Level-3 Evidence Registrar
**Deliverable requested:** any pre-1999 archived amazon.com page the Wayback Machine will *actually serve*.
**Outcome:** **NONE FOUND. Documented null.** Gap **G-ARCHIVE-1 stays open**; RD-006 is now closed as a
negative result for the root URL and for the queries listed below, and stays open for arbitrary deep paths.

Request header used on every call: `User-Agent: FounderPlaybook Research AdminContact@example.com`
(compressed responses negotiated with `--compressed`).

## Queries run and what each returned

| # | Query | Result |
|---|---|---|
| 1 | CDX `url=amazon.com&matchType=prefix&filter=statuscode:200&from=1995&to=1998` | **HTTP 504** nginx `Gateway Time-out`. The prefix keyspace for this domain is too large to sweep in one call. |
| 2 | CDX `url=amazon.com/&matchType=exact&from=1994&to=1999` (all status codes) | **HTTP 200**, 64 rows / 22 distinct timestamps. **Every** 1994–1998 row is a **302**. Earliest capture of any kind: **1998-12-12 01:25:32**, `http://amazon.com:80/`, **status 302**, 330 bytes — a redirect, not a page. |
| 3 | CDX `url=www.amazon.com&matchType=exact&filter=statuscode:200&from=1995&to=1998` | **HTTP 200, 0 bytes of output — a true empty result set.** This is the decisive query: there is no 200 capture of the `www.amazon.com` root anywhere in 1995–1998. (One attempt returned HTTP 503, Internet Archive "Temporarily Offline"; the retry succeeded and is the row cited here.) |
| 4 | CDX `url=amazon.com&matchType=prefix&filter=statuscode:200` restricted to single years 1995, 1996, 1997 | **HTTP 504** on all three. |
| 5 | CDX `url=amazon.com&matchType=prefix&filter=statuscode:200&from=199610&to=199611` (one month only) | **curl exit 28**, 60 s timeout, 0 bytes. |
| 6 | CDX `url=amazon.com/exec&matchType=prefix&filter=statuscode:200&from=1995&to=1998` (early deep path) | **curl exit 28**, 60 s timeout, 0 bytes. |
| 7 | Availability API `https://archive.org/wayback/available?url=amazon.com&timestamp=` for 1995, 1996, 1997, 1998 | HTTP 200 all four, body `{"archived_snapshots": {}}` every time — no snapshot at or near any of those dates. |

## Where the first servable page actually is

The 1994–1999 root index contains exactly six `statuscode:200` rows, and both timestamps fall in the
second half of **1999**, i.e. outside the Stage-1 window and outside "pre-1999":

```
19990828014913  http://www.amazon.com:80/?   200  text/html  6544
19991013091817  http://amazon.com:80/        200  text/html  6801
```

Between them and 1998-12-12 sit only 302 redirects (1999-01-25, 1999-02-08, 1999-02-09, 1999-02-18,
1999-04-22 ×3, 1999-04-23, 1999-04-29, …). So the earliest homepage the archive will serve as an actual
page is **1999-08-28**, roughly four years after the July 1995 launch.

## What this means for the dossiers

1. **There is no archival screenshot of the 1995 or 1996 Amazon.com site.** Any description of the
   launch-era pages, the "Earth's Biggest Bookstore" front door, the order bell, or the first page layout
   must be sourced to the S-1 text, to the 1997 10-K, to the 1997 newspaper files, or to the 1999-conducted
   Sheff interview — and labelled as *textual/recalled*, never as artifact.
2. **Do not fill this gap with the cached 2006 capture.** `wb_amazon.html` (timestamp 2006-05-22) was in
   the destroyed cache and was already rated worthless for Stage 1; it is not restored here and must not be
   used as a stand-in.
3. **Do not misread the Mosaic artifact as an Amazon capture.** `ncsa-mosaic-whats-new_1995-08` is a real
   August-1995 web document and the closest thing to a launch-window page we hold, but it does not contain
   Amazon.com (its single "Amazon" string is the Amazon River).
4. The 504s and connection timeouts are **upstream capacity failures at the Internet Archive**, not evidence
   about Amazon. They are recorded so a later agent does not report "no captures exist" on the strength of a
   timeout, and does not re-run the same doomed broad-prefix sweep. If RD-006 is ever chased again, the only
   viable route is per-URL `matchType=exact` probes against specific guessed deep paths, one call each.

## Status of the file itself

Complete as written; this is a primary-adjacent negative finding, not a truncated retrieval.
