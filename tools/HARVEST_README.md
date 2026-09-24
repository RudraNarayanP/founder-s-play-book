# HARVEST README — periodical_harvest.py

Batch harvester for the **digitised pre-1994 periodical and corporate-print
corpus families**. Families 1–3 exist because `00_METHOD_AND_STYLE.md` §14 rule 6
requires a depth verdict to search **four** corpus families — filings, web
archives, **periodical corpora**, and **auction/museum documentary records** —
and the Walmart (reopened) and UnitedHealth (provisional; Google Books HTTP 429)
verdicts failed to *see* the periodical family at all. Family 5 exists because
the method file does not name it, and it is the family that decided the case
anyway: the Apple probe (`company_004_apple/research/A_chronology_feasibility.md`)
recovered Byte 1976 and the Homebrew newsletters as in-window Tier-1 text from
digitised print, and Walmart's verdict flipped on the same class of material.

> **OPERATIVE LESSON (why family 5 exists, stated as a rule):** **a depth verdict
> may not treat "paper-only" or "no digitised text exists" as established until
> digitised books and bound corporate print — the Internet Archive metadata
> index and its `_djvu.txt` text layers — have been queried.** This is the family
> that reversed the first verdict attempted on it: Walmart was rated
> *forensic-core* on a probe that asserted "1970 registration statement, 1970s
> 10-Ks = SEC paper only … not scanned" and "pre-IPO financials are UNDOCUMENTED
> at Tier 1", and that had never searched a digitised book or a printed annual
> report. The complete printed Wal-Mart Stores FY1972→FY1997 annual-report run
> was on Internet Archive, free and text-searchable, the whole time; audited
> in-window financials came back with it (see
> `founders_playbook/01_companies/company_002_walmart/research/B_periodical_retest.md`).
> **An unqueried family must never be reported as NULL — it is UNANSWERED.**

Stdlib-only Python 3 (urllib/json/csv/argparse/time). No installs, no third-party deps,
no keys. **Read-only public search APIs only — no paywall bypass, no login-gated content,
nothing a public API declines to return.**

## Corpus families covered

| # | `source_family` | What it queries | Live status at 2026-09-24 |
|---|---|---|---|
| 1a | `chronicling_america` (+ `_ocr`) | LoC digitised newspaper page search + per-page OCR | **UNANSWERED — HTTP 403 Cloudflare** (blocked, not null) |
| 1b | `internet_archive` | IA metadata search for periodicals/magazines + `metadata/{id}` | WORKING — 8 searches, 200; 5 proven per-param nulls, 28 LEAD_ONLY, 1 TIER1 |
| 2 | `hathitrust` | Babel `cgi/ls/one` full-text search | **UNANSWERED — TLS/403** |
| 3 | `google_books` | Books volumes v1 (the trade-press route) | **UNANSWERED — HTTP 429 anonymous daily quota** |
| 4 | *(not implemented)* | auction / museum / special-collections documentary records | **UNQUERIED — no API verified; remains UNANSWERED, never null** |
| 5 | `corporate_print` | **NEW: digitised bound corporate print — annual / shareholder reports, 10-Ks, prospectuses — via the IA metadata index, then identifier → `metadata/<id>` → `_djvu.txt` availability → direct-server text** | WORKING — 9/9 tasks HTTP 200; **35 TIER1_CANDIDATE rows** |

Family 4 is named here so that it is visibly **unqueried**, per the hard rule that a
family the tool never sends a request for may not be reported as a corpus null.

## Files

| File | Role |
|---|---|
| `tools/periodical_harvest.py` | the harvester |
| `tools/queries.json` | all queries as **data** — add future companies by editing this, never the code |
| `founders_playbook/00_universe/harvest/<source_family>/` | raw evidence, one `<sha1>.<ext>` body + `<sha1>.meta.json` sidecar per URL |
| `founders_playbook/00_universe/harvest/candidates.csv` | the index: `company,source_family,query,item_id,title,date_or_issue,url,snippet_or_hitcount,http_status,classification,retrieved_at` |
| `founders_playbook/00_universe/harvest/_MANIFEST.md` | regenerated every run: file, source, query, HTTP status, bytes, timestamp |

## Running

```bash
cd tools
python periodical_harvest.py --dry-run                 # print planned URLs, fetch nothing
python periodical_harvest.py --max-requests 60         # bounded run (cap default 300)
python periodical_harvest.py --company walmart         # one company only
python periodical_harvest.py --delay 2.0 --insecure    # per-host delay; TLS-verify bypass (see Gotchas)
```

Behaviour: per-host delay (default 2 s); User-Agent
`FoundersPlaybook-harvest/1.0 (…contact: research@example.org)`; exponential backoff on
429/503 honouring `Retry-After` (stops honouring above 60 s and records UNANSWERED);
**hard stop after 5 consecutive failures per host** (remaining tasks for that host are
written as UNANSWERED SKIPPED rows, never silently dropped); URL-hash cache — a cached URL
costs 0 network requests, so re-runs are idempotent and cheap.

## Classification discipline — the EMPTY / UNANSWERED firewall

This project has been misled twice by conflating them. In `candidates.csv`:

- `TIER1_CANDIDATE` — dated item whose text is (or plausibly is) in-window Tier-1 periodical evidence.
- `LEAD_ONLY` — pointer (metadata hit, snippet, scan without opened text); chase before citing.
- `NULL` = **EMPTY, proven null**: endpoint answered 200 with 0 results *for those exact params*. A null is per-endpoint, never per-corpus.
- `UNANSWERED`: 403-challenge / 429 / 503 / TLS / timeout / parse-schema-unverified / host-halted / cap-skipped. Says nothing about the corpus.
- `ERROR`: other 4xx (bad request — check your params).

## Sources: endpoint verification record (2026-09-24)

No parameter below is invented; each is marked with how it was confirmed. Live-run outcomes
are from the executed harvest (all bodies preserved in the subdirectories).

### 1. Chronicling America — `chronicling_america`, `chronicling_america_ocr`
- Search: `https://chroniclingamerica.loc.gov/search/pages/results/?format=json&andtext=…&date1=&date2=&dateFilterType=yearRange&state=&sort=&page=N`.
  Params confirmed from **archived real request URLs** (e.g. `state=Alaska&dateFilterType=yearRange&date1=1912&date2=1916&sort=date&andtext=suffrage&format=json`, Wayback 2020–21) and the **official API docs** (Wayback snapshot 2025-08-04 of `chroniclingamerica.loc.gov/about/api/`: page-search "OpenSearch" params `andtext/format/page`; link pattern `/lccn/<sn>/<date>/ed-<e>/seq-<s>/`; `ocr.txt` naming in the bulk-data section).
- Response shape confirmed from **archived real response bytes** (Wayback `id_` capture 2021-09-29): top-level `totalItems, startIndex, endIndex, itemsPerPage, items[]`; each item has `id, lccn, date (YYYYMMDD), title, sequence, city, state, ocr_eng` (full page OCR **inline** — so search hits are directly minable even before the ocr.txt route).
- Per-page text: `<item.id>ocr.txt` (`chronicling_america_ocr` kind `ocr`) — documented pattern, **not live-verifiable from this network**; add `ocr` tasks after real hits (template in `queries.json._deferred_examples`).
- **LIVE STATUS 2026-09-24: UNANSWERED (BLOCKED, NOT NULL).** Every request from this network returns HTTP 403 Cloudflare "Just a moment" challenge (urllib, curl, and the assistant fetch pipeline alike; legacy host 308-redirects to `www.loc.gov/chroniclingamerica/…`, also challenged). The tool fetched 5 queries, hit the 5-consecutive-failure hard stop, and recorded all 11 CA tasks as UNANSWERED; challenge bodies are preserved verbatim. **Re-run from a non-Challenge-blocked network (residential/regular egress) — no code change needed; that is the single highest-value follow-up, since CA is the proven route for both Walmart's and UnitedHealth's newspaper window.**

### 2. Internet Archive — `internet_archive`
- Metadata search (LIVE, working): `https://archive.org/advancedsearch.php?q=<solr-ish>&fl[]=identifier&fl[]=title&fl[]=date&fl[]=year&fl[]=mediatype&fl[]=collection&rows=N&page=1&output=json` → `response.numFound`, `response.docs[]`. `YEAR:[a TO b]` ranges verified live (200; syntax-valid, 0-result answers are true nulls).
- Item files: `https://archive.org/metadata/<id>` → `server`, `dir`, `files[]` (which `*_djvu.txt` text layers exist) — verified live.
- **NOT shipped (not confirmed): the in-item full-text `fulltext/inside.php` endpoint.** Live tests returned `{"error":"Invalid filename"}` / `"No hOCR or Abbyy file present"` on every parameter spelling tried (including the item's own home server) — the endpoint is deprecated/unverifiable from this environment. Recorded here rather than shipped as a fabricated integration. Workaround, proven in the Apple case: download the `_djvu.txt` and grep locally.
- Item text download: `https://archive.org/download/<id>/<file>` — **unreliable from this environment** (302 to CDN hosts with an expired TLS cert here; direct-server pattern 404'd). Run with `--insecure` only knowingly; failures are recorded as UNANSWERED, not nulls.

### 3. HathiTrust — `hathitrust`
- `https://babel.hathitrust.org/cgi/ls/one?q1=<term>&searchtype=all&target=ls&ft=ft` — param names and values read from **the site's own GET search form** (`<form action="/cgi/ls/one">`, inputs `q1`, `searchtype`, `target`, `ft`) in Wayback capture 2019-07-12 of `babel.hathitrust.org/cgi/ls`; endpoint existence confirmed by archived 200s.
- Response is HTML and its result-list schema **could not be verified live** → parser only stores the body and attempts one conservative result-count regex; everything else is UNANSWERED. **LIVE STATUS 2026-09-24: UNANSWERED** — this network receives the Cloudflare 403 challenge (TLS-verify failure also observed); 2 tasks recorded, both marked as such.

### 4. Google Books — `google_books`
- `https://www.googleapis.com/books/v1/volumes?q=<phrase>&maxResults=N` — endpoint LIVE and shape-confirmed: it answers JSON, currently **HTTP 429 `Quota exceeded … 'Queries per day' … for consumer 'project_number:…'`** (anonymous per-IP daily quota exhausted from this network). Both queries exhaust the full backoff ladder and are recorded **UNANSWERED (rate-limited)** — the identical failure that made UnitedHealth's verdict provisional; this time it is instrumented, honoured, and preserved, not mistaken for a null.

### 5. Digitised corporate print / annual reports — `corporate_print` (NEW)
Queries the **same Internet Archive metadata index** as family 1b, but scoped the way
bound corporate print is actually findable, then carries each identifier through to
text availability. Three task kinds:

| kind | Endpoint | Verified live 2026-09-24 |
|---|---|---|
| `search` | `https://archive.org/advancedsearch.php?q=…&fl[]=…&rows=N&page=1&output=json` | HTTP 200. Clause fields used are **only** `title:(…)`, `creator:(…)`, `mediatype:(texts)`, `YEAR:[a TO b]` — each returned 200 and non-zero results in a real call. `response.{numFound,start,docs}` confirmed; docs carry exactly `identifier, title, date, year, mediatype, collection, creator` (`collection` and `creator` are **list-valued**) |
| `metadata` | `https://archive.org/metadata/<identifier>` | HTTP 200. Fields read and confirmed present: `identifier`, `server`, `dir`, `files[].name`, `metadata.{title,date,year}`. Text layer = a file ending `_djvu.txt` / `.ocr.txt` / `_hocr.searchtext` |
| `text` | `https://<server><dir>/<file>` (content server) | HTTP 200, **23,989 B** of the FY1972 Wal-Mart report body, saved verbatim |

Reference exemplar of a hit (this is what the family is for):
```
(title:(walmart) OR title:("wal-mart stores")) AND (title:(annual) OR title:(reports)
  OR title:(yearbook)) AND mediatype:(texts) AND YEAR:[1970 TO 1998]
  -> HTTP 200, numFound=27 = the printed Wal-Mart Stores annual-report run FY1972-FY1998
```

Query traps found by live testing — **do not repeat them**:
- `title:("wal-mart")` does **not** match an item titled *"Walmart Stores"*: IA's
  hyphen/quote tokenisation is unreliable, so the hyphenless form must be OR-ed in.
  Strict `title:("wal-mart") AND title:("annual report")` returned **numFound 0** while
  the same corpus holds 27 annual reports.
- Unscoped conjunctions (`walmart AND "annual report" AND YEAR:[…] AND
  mediatype:(texts)`) return **token noise** — CIA reading-room cables, *Compute!*
  magazine, `united health care` → 315 rows of unrelated federal documents. Such a
  `numFound` is not evidence; these forms are deliberately **not** shipped.
- `archive.org/download/<id>/<file>` 302-redirects to a CDN whose **TLS certificate is
  expired** from this network (`CERTIFICATE_VERIFY_FAILED`) → UNANSWERED, not null. The
  `<server>+<dir>` route above works with verification on.
- **`creator:` is the productive clause for corporate print.** Title-scoping found 0
  Apple items; `creator:("apple computer") AND (title:(annual) OR title:(report))` →
  numFound 5, Apple Computer, Inc.-authored corporate research print (ACOT reports, 1989).

**Tier-1 promotion gate (the WR-17 rule, enforced in code).** In-window +
`mediatype=texts` alone is NOT enough: a task's `name_patterns` must appear, whole-word,
in the item's **own** title/creator alongside a `report_terms` hit. Without the gate the
first live run emitted **24 false `TIER1_CANDIDATE` rows for Apple** — DTIC "Ada Compiler
Validation Summary Report … Apple Macintosh II … Meridian Software Systems, **Inc.**",
NASA and ERIC records, a "concentrated apple" orchard study, and a *Reciprocal Evaluation
Tour* whose creator is a person surnamed **Loyal E. Apple**. Substring matching was also
dropped for whole-word matching ("Appleton", "pineapple"). Demoted rows are marked
`GATE-REJECTED from Tier-1` in `snippet_or_hitcount` and kept as `LEAD_ONLY`.
**Superseded rows:** the append-merge in `write_candidates` means `candidates.csv` still
carries those 24 rows from the 10:22–10:24Z generation. They were **not deleted**
(protected-evidence rule). Consumers must take the **newest `retrieved_at` per
`item_id`**; under that rule family 5 currently reads 35 `TIER1_CANDIDATE`, 24
`LEAD_ONLY`, 3 per-param `NULL`.

## What the 2026-09-24 run returned (numbers from bodies on disk)

29 network requests / cap 60. 49 candidate rows: 1 TIER1_CANDIDATE, 28 LEAD_ONLY, 5 NULL, 15 UNANSWERED.

- **(a) Walmart 1945–1965:** IA `"Walton's" store` YEAR 1945–1965, `walton (retailing|variety store|five and dime)` 1945–1965, and `"$1.25 store"` → **proven nulls (numFound=0)**. `walton "five-and-dime"` → 2 hits, both **out of window** (1990 biography; 1998 DTIC discount-retail study incl. Wal-Mart — Tier-2 retrospective, LEAD_ONLY). **No in-window newspaper text was retrievable this run — CA blocked (UNANSWERED), which is exactly the gap the tool exists to close on the next network.**
- **(b) UnitedHealth 1971–1980:** IA `"charter med"` YEAR 1971–1985 and `"metropolitan health plans"` → **proven nulls (metadata-index level only)**. `"unitedhealthcare"/"united health care"` → 20 hits, all modern court-docket texts (LEAD_ONLY, post-window). `"burdic"` → 12 hits: one in-window date (1971 VA pension-cards microform, surname match only — the TIER1_CANDIDATE flag here is a date heuristic, treat as LEAD on inspection).

## What the family-5 run returned (2026-09-24T10:22–10:33Z, numbers from bodies on disk)

`--max-requests 25`, `--delay 2.0`. **10 network requests on the live pass; 0 on the
re-run that verified the gate fix** (every URL was a cache hit — the family-5 params
added after the fact are gate-only and do not change a built URL, so cache keys held).
No host rate-limited this session, so the 5-consecutive-failure hard stop **did not
fire and was not extended past**; the single fresh Chronicling America 403 was one
failure, and the remaining CA tasks recorded their cached 403s as UNANSWERED.

Per-family HTTP outcomes actually received (32 tasks):

| Family | Tasks | Fetched | Cached | HTTP | Rows |
|---|---|---|---|---|---|
| `corporate_print` | 9 | 9 | 0 (then 9) | **200 × 9** | 35 TIER1_CANDIDATE, 24 LEAD_ONLY, 3 NULL |
| `chronicling_america` | 11 | 1 | 10 | 403 × 11 | 11 UNANSWERED |
| `internet_archive` | 8 | 0 | 8 | 200 × 8 | 28 LEAD_ONLY, 5 NULL, 1 TIER1 |
| `hathitrust` | 2 | 0 | 2 | 0 (TLS failure) × 2 | 2 UNANSWERED |
| `google_books` | 2 | 0 | 2 | 429 × 2 | 2 UNANSWERED |

- **(a) Walmart — the exemplar reproduces.** `CP walmart annual-report run 1970–1998`
  → HTTP 200, `numFound=27` → **27 `TIER1_CANDIDATE` rows**, one per printed report
  FY1972…FY1998 (`1972-annual-report-for-walmart-stores-inc` … `1998-…`). The
  FY1972 `metadata` task confirmed the `_djvu.txt` layer and its direct-server URL;
  the `text` task pulled **23,989 B of the audited report body** as a raw saved file —
  i.e. the FY1968–FY1972 five-year table that flipped the verdict is now in the
  harvest cache, not just in a company `sources/` tree.
- **(b) Walmart pre-FY1972** (`YEAR:[1962 TO 1971]`, annual/reports/prospectus terms)
  → HTTP 200 `numFound=0` → **NULL on those exact params**, consistent with the retest's
  WR-16 (the FY1970/FY1971 reports are not on IA). Not a corpus null: EDGAR paper,
  Hoover, LoC/WorldCat holdings and the SEC Reference Room remain unqueried.
- **(c) UnitedHealth** → HTTP 200, **`numFound=0` on both forms** (title-scoped
  1977–1995 and creator-scoped 1971–1995) → 2 per-param NULLs. **The family is NOT
  closed for UnitedHealth:** the 1984–1993 printed shareholder reports may exist under
  a scan identifier that carries no corporate name in `title`/`creator`, and the two
  corpora that hold them (Google Books 429, HathiTrust TLS-dead) are UNANSWERED here.
- **(d) Apple — the family pays for itself on the second company.** Title-scoping
  1976–1995 → HTTP 200, 20 docs, **0 survive the gate** (DTIC/NASA/ERIC/orchard/
  surname noise). Creator-scoping → HTTP 200, 9 docs, of which **5 are `TIER1_CANDIDATE`:
  Apple Computer, Inc.-authored ACOT corporate research reports dated 1989**
  (`micro_IA41155142_0546…0550`, creator field literally `"Apple Computer, Inc.,
  Cupertino, CA."`), and the Apple `metadata` task confirmed a **text layer exists**
  (`https://ia801804.us.archive.org/32/items/micro_IA41155142_0546/…_djvu.txt`).
  So Apple's early-era printed corporate material is present but **this is corporate
  research print, not financial print**: no Apple annual report surfaced, so the
  probe's "money and organisation" exclusion is *narrowed*, not answered.

## Consuming results

1. Filter `candidates.csv` on `classification=TIER1_CANDIDATE|LEAD_ONLY`.
2. Open the URL (or the raw body in `<source_family>/`), read the item's own text — a search hit is a pointer, not evidence; per §14 rule 3 record documents in the company's `research/_EVIDENCE_CACHE.md`.
3. For CA hits worth mining: the `ocr_eng` field already carries page text (saved in the raw JSON), or queue a `chronicling_america_ocr` task.
4. Company `sources/` and `research/` directories are **protected archives** (§14 rule 4): this tool only ever writes under `00_universe/harvest/` — never into them, never deletes, never tidies.

## Adding a company

Edit `queries.json`: append tasks `{company, source_family, kind, query_label, params, window}` (+ raise `per_source_caps`). Dry-run, then run with a cap. Nothing in `.py` changes.

For family 5 the params are **data**, and only these keys are accepted
(`cp_search_url` raises rather than inventing a parameter if a clause field
other than `title`/`creator` is requested, and a `text` task refuses to run
unless `server`/`dir`/`file` were copied verbatim from a real `metadata` response):

```json
{"company": "<co>", "source_family": "corporate_print", "kind": "search",
 "query_label": "CP <co> annual reports <yr>-<yr>", "window": [<from>, <to>],
 "params": {
   "company_terms": ["<name>", "\"<hyphenated name>\""],
   "scope_field": "creator",
   "report_terms": ["annual", "report", "reports", "shareholder", "stockholder", "prospectus"],
   "mediatype": "texts", "year_range": [<from>, <to>], "rows": 20,
   "identity_terms": ["inc", "corporation", "company"],
   "name_patterns": ["<company, inc>", "<company stores>"] }}
```

- `company_terms` / `report_terms` / `year_range` / `mediatype` build the query;
  `name_patterns` / `identity_terms` are **gate-only** — they change no URL, so
  adding them never costs a request and never invalidates a cache key.
- Always ship **both** a `title:`-scoped and a `creator:`-scoped search: the Apple
  seed proved they find disjoint material.
- Then queue `{"kind":"metadata","params":{"identifier":"…"}}` for any hit worth
  reading (identifier verbatim from the search body) — that is what proves a text
  layer exists before anyone writes "not digitised".
- Walmart's config block is the worked reference exemplar; copy its shape.

## Known gaps / next run

1. **Family 4 (auction / museum / special collections) is unqueried by this tool** —
   no read-only public API was verified for it. It stays UNANSWERED and must be
   reported as such, not as a null, in any depth verdict that cites this harvest.
2. Chronicling America and HathiTrust need a non-Challenge-blocked egress; Google
   Books needs a quota reset or a key — all three are UNANSWERED, not empty.
3. Family 5 could be extended to `prearchive.org`/`annualreports.com`-class corpora
   and to HathiTrust's corporate-print scans; none of those endpoints has been
   verified from this environment, so none is shipped.
