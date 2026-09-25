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

| # | `source_family` | What it queries | Live status at 2026-09-24 → **after the 2026-09-25 repair** |
|---|---|---|---|
| 1a | `chronicling_america` (+ `_ocr`) | LoC digitised newspaper page search + per-page OCR | **UNANSWERED — HTTP 403, and now *proven* to be their policy, not our request** (`/robots.txt` 403s identically; see §1) |
| 1b | `internet_archive` | IA metadata search for periodicals/magazines + `metadata/{id}` | WORKING — 8 searches, 200; 5 proven per-param nulls, 28 LEAD_ONLY, 1 TIER1 |
| 2 | `hathitrust` | Babel `cgi/ls` full-text search + catalog brief-record API | **POSITIVE but INTERMITTENT** — 5/5 searches 200 with real records in the 13:12Z window, 5/5 403-challenged in the 13:44Z window, same URL bytes. The catalog API is **unconditionally open** (see §3) |
| 3 | `google_books` | Legacy Atom volumes feed (the trade-press route) | **POSITIVE (keyless) — 4 × HTTP 200 with real volumes.** Still 429 on the v1 JSON API, which is switched off for everyone (see §4) |
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
python periodical_harvest.py --source-family hathitrust --source-family google_books
python periodical_harvest.py --delay 2.0 --insecure    # per-host delay; TLS-verify bypass (see Gotchas)
# 2026-09-25 additions — each one exists because a real failure was mis-recorded:
python periodical_harvest.py --insecure-hosts babel.hathitrust.org   # host-scoped TLS bypass: HathiTrust
                                                                     # died on 'certificate has expired'
                                                                     # and logged a bare status 0
python periodical_harvest.py --cache-dir <dir> --gb-key <k>          # sidecar cache (notes/errors travel
                                                                     # with the bytes); keyed Books v1
python periodical_harvest.py --use-curl [--curl-bin curl] --follow-redirects
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

## Sources: endpoint verification record (2026-09-24, repaired 2026-09-25)

No parameter below is invented; each is marked with how it was confirmed. Live-run outcomes
are from the executed harvest (all bodies preserved in the subdirectories).

### 1. Chronicling America — `chronicling_america`, `chronicling_america_ocr`
- **Working call as corrected (2026-09-25):**
  `https://www.loc.gov/chroniclingamerica/search/pages/results/?andtext="<quoted phrase>"&format=json[&page=N]`
  — the relocated canonical host, not `chroniclingamerica.loc.gov`. Title directory:
  `/search/titles/results/?terms=<q>&format=json`; bulk inventory: `/bulk/?format=json`;
  per-page OCR: `<item.id>/ocr.txt` (`ca_ocr_url`). All four are built in code and dry-run
  clean; all four are unreachable scripted (below).
- **What the old code did wrong (three separate things, only two of them ours):**
  (1) it called the **retired host**, which 308-redirects every path to `www.loc.gov`, and
  because urllib followed the redirect silently the sidecar recorded the OLD url next to the
  NEW host's bytes — the evidence disagreed with itself; (2) it sent `Accept: */*`, which is
  what a bot looks like; (3) the **content** was wrong: token `waltons` (never a store name),
  no hyphenated `"Wal-Mart"` (the brand the full-text index must match), no Arkansas anchor,
  Newport mis-stated, `UnitedHealthCare` for a company founded as Charter Med, `"Burdic"` for
  a founder named Burke, and **no Apple periodical task at all**. Those are fake negatives
  manufactured by the query set, and they are why 17 CA tasks now exist where 11 did.
- **LIVE STATUS 2026-09-25 — UNANSWERED, and the block is CLASSIFIED, not assumed.** Three
  canaries re-run this session, 13:48Z, from `v2_reverify/`: titles canary → **403, 5,990 B,
  `Cf-Mitigated: challenge`, CF-RAY a40a7d1cc9554621-DEL** with a Chrome UA and full Chrome
  header set; page-search canary (`andtext="Wal-Mart" Bentonville&format=json`) → **403,
  5,980 B, challenge** with the declared tool UA; and the decisive one,
  `https://www.loc.gov/robots.txt` → **403, 5,457 B, `Cf-Mitigated: challenge`**, body text
  verbatim *"Just a moment… Enable JavaScript and cookies to continue"*.
  **The 403 is their policy, not our request** — robots.txt carries none of our parameters,
  none of our company names, none of our query grammar, and it is answered exactly like every
  CA search. Corroborating: `labs.loc.gov` (200), `data.labs.loc.gov` (200), `tile.loc.gov`
  (301) and `web.archive.org` (200) all answer normally **from this same machine**, so it is
  not an IP reputation problem either; and the legacy host 308s to the challenged zone, so
  there is no LoC path that a script can read. Unblocking needs a browser session or
  LOC-granted access. **17 CA tasks therefore stay UNANSWERED and none of them may be read as
  a corpus null** — this is the single largest known gap in the harvest, because CA is where
  Walmart's 1945–1962 Arkansas press and UnitedHealth's 1970s Minneapolis press would live.
- **Unverified and marked as such:** `date1/date2/dateFilterType/state/sort/withText` are
  LEGACY params, absent from the published docs and unverifiable while the zone challenges.
  The shipped CA searches carry them anyway (they are the only documented decade filter), and
  `parse_ca_search` records that a 0 from them indicts the parameter, not the corpus.

### 2. Internet Archive — `internet_archive`
- Metadata search (LIVE, working): `https://archive.org/advancedsearch.php?q=<solr-ish>&fl[]=identifier&fl[]=title&fl[]=date&fl[]=year&fl[]=mediatype&fl[]=collection&rows=N&page=1&output=json` → `response.numFound`, `response.docs[]`. `YEAR:[a TO b]` ranges verified live (200; syntax-valid, 0-result answers are true nulls).
- Item files: `https://archive.org/metadata/<id>` → `server`, `dir`, `files[]` (which `*_djvu.txt` text layers exist) — verified live.
- **NOT shipped (not confirmed): the in-item full-text `fulltext/inside.php` endpoint.** Live tests returned `{"error":"Invalid filename"}` / `"No hOCR or Abbyy file present"` on every parameter spelling tried (including the item's own home server) — the endpoint is deprecated/unverifiable from this environment. Recorded here rather than shipped as a fabricated integration. Workaround, proven in the Apple case: download the `_djvu.txt` and grep locally.
- Item text download: `https://archive.org/download/<id>/<file>` — **unreliable from this environment** (302 to CDN hosts with an expired TLS cert here; direct-server pattern 404'd). Run with `--insecure` only knowingly; failures are recorded as UNANSWERED, not nulls.

### 3. HathiTrust — `hathitrust`
- **Working call as corrected (2026-09-25):**
  `https://babel.hathitrust.org/cgi/ls?field1=ocr;q1="<phrase + place terms>";a=srchls;lmt=ft[;facet=bothPublishDateRange:%221960-1969%22]`
  — **semicolon**-separated SFX grammar, action `a=srchls`, `lmt=ft` for full view. The date
  facet field is `bothPublishDateRange`, value a decade or a single year, copied out of the
  site's own hrefs. `ht_search_url` refuses any other facet field (see the fake negative below).
  Record rights/metadata: `https://catalog.hathitrust.org/api/volumes/brief/htid/<hdl>.json`.
- **What the old code did wrong:** (1) it called the legacy `/cgi/ls/one` alias with
  `&`-separated `searchtype/target/ft`, which answers **302** to the shape above; (2) status
  `0` was a **client-side TLS trust failure** — "certificate has expired" from Python's own
  verifier while the environment clock reads 2026-09-25 — recorded as a bare 0 with no reason,
  so a trust problem masqueraded as a dead host and as an empty catalogue. Run with
  `--insecure-hosts babel.hathitrust.org` (host-scoped, logged in the sidecar as
  `tls_verify: off-for-this-host`); that is how every count below was obtained; (3)
  `format=json` is accepted and **ignored** — HTML comes back — so a result count must come
  from the record blocks and facet badges, never from a JSON key.
- **Fake negative found and guarded:** `facet=DateRange:"1960-1969"` (plausible, nonexistent)
  is silently accepted, echoed as an active filter, and returns *"No results match your
  search"* for a control query that really holds **2,284** hits. The shipped CONTROL task
  (`"five and dime" variety store` 1950–1959, verified 2,284 / 187) exists to catch exactly
  this: if it ever reads 0 while the host answers 200, the defect is ours.
- **LIVE STATUS 2026-09-25: POSITIVE but INTERMITTENT — the block is bot management with an
  open window, not a wall.** Five searches returned **HTTP 200** with real records in the
  13:12Z window (`"Wal-Mart" Bentonville` 391,767 B, All Items **11,850** / Full View
  **2,638**, 100 record blocks; same query + 1960–1969 facet 34,171 B → **45 / 4**;
  `"Walton's" "five-and-dime"` 238,566 B → **1,529 / 59**; `"Charter Med"` 380,833 B →
  **1,527 / 532**; CONTROL 370,909 B → 2,284 / 187). The **byte-identical URLs** re-run at
  13:44–13:52Z returned **403 `Cf-Mitigated: challenge` five times in a row**, including a
  Chrome UA with a full Chrome header set and two spaced retries. So: a `/cgi/ls` 403 is
  UNANSWERED-with-a-known-200-history — re-run in a later window, never report the corpus as
  empty. The 5-consecutive-failure hard stop is what to lean on here.
- **What is open to a script unconditionally:** the catalog brief-record API —
  `…/api/volumes/brief/htid/uiug.30112005545535.json` → **200, 29,445 B, no challenge** at
  13:47Z, i.e. in the same minute the search host was refusing. It returns records
  (titles/publishDates/oclcs/lccns) and **every holding with `rightsCode` and
  `usRightsString`** — that is how a 1960s Full-view right is proven without the search page.
- **What is NOT open to a script:** the text. `/cgi/pt?id=<hdl>&view=1up&seq=1` for a
  `pd` / "Full view" item answered **403 Cf-Mitigated: challenge**. "Full view" therefore
  means *a human can open it*, not *this tool can read it* — page text must come from a
  browser session or from the same item on Internet Archive.

### 4. Google Books — `google_books`
- **Working call (keyless, verified live four times this session):**
  `https://books.google.com/books/feeds/volumes?q="<quoted phrase>"&maxResults=10` — the
  **legacy Data API (Atom)**: no key, no GCP quota, real volumeIds, `dc:title`/`date`/
  `creator`/`publisher`, `gbs:viewability` (`all_pages` / `partial` / `no_pages`), the matched
  page as `pg=PA138`, and a 178–283-character matched-page snippet. Outcomes re-verified at
  13:48Z: Walmart `"Wal-Mart" Bentonville Rogers` 200 / 25,023 B / 10 volumes; Apple
  `"Apple Computer" Cupertino shareholder` 200 / 23,665 B / 10 volumes (four InfoWorld issues
  `all_pages`); UnitedHealth `"Charter Med" Minneapolis` 200 / 23,608 B / 10 volumes
  (three federal HMO documents `all_pages`, 1978/1981/1982-series); `"Metropolitan Health
  Plans"` 200 / 6,102 B / 2 volumes, **neither in-window** — a real-but-thin answer, not a null
  on the company.
- **What the old code did wrong:** the request shape was never the problem — it called
  `www.googleapis.com/books/v1/volumes`, which is a **different service wearing the same
  name** and is quota-gated. The shipped `GB v1 control` task exists to keep that diagnosis
  honest rather than folkloric: re-run 13:48Z it answers **429**, body verbatim
  *"Quota exceeded for quota metric 'Queries' and limit 'Queries per day' … for consumer
  'project_number:624717413613'"*, `reason=rateLimitExceeded`, `quota_limit_value: "0"` —
  Google's **shared anonymous** project has a daily quota of **zero**. No delay, no backoff
  and no second egress changes that; a key (`--gb-key` / `GOOGLE_BOOKS_API_KEY`) does.
- **The limit that must not be talked up or down:** keyless Books delivers **snippet-level
  text, not full text**. `openSearch:totalResults` read **300 for three unrelated queries** —
  a display cap, never a corpus count — and the `books.google.com` **browsing** HTML for a
  matched page answers 403 *"your computer or network may be sending automated queries"*.
  So Google Books is a finding aid with a quote attached: it can tell you which volume, which
  page, and whether it is viewable.
- **Corrected 2026-09-25 (second pass over the saved bodies):** an earlier note in this file
  and in `queries.json` claimed keyless returns *no* snippet, because there is no
  `<gbs:snippet>` node. That was wrong — the text is in `<dc:description>` (44 of the 50
  entries in the five verified 200 feeds). `_gb_atom_rows` now captures it (≤300 chars) per
  row, so the harvest keeps Google's own words instead of only a bare viewability flag.

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

## The 2026-09-25 repair runs, and the 14-request re-verification (numbers from bodies on disk)

| Run | Requests | Outcome |
|---|---|---|
| 13:00Z (urllib, TLS on) | ~18 | CA 403 ×5 · HT 403 ×5 (challenge) · GB feeds 200 ×4 + v1 429 · IA/CP 200 ×17 |
| 13:07Z replay | cached + few | CA 403 · HT 403 ×5 · GB 200 (cache) |
| 13:12Z replay | ~6 fresh | **HT 200 ×5 (34,171 / 238,566 / 370,909 / 380,833 / 391,767 B)** · HT catalog 200 JSON · CA 403 · GB 429 (control) |
| 13:44–13:52Z re-verification (this session, `v2_reverify/`) | **14** | GB feeds **200 ×3** (25,023 / 23,608 / 23,665 B, byte-identical to cache) · GB v1 **429 ×1** (1,306 B, quota 0) · HT `/cgi/ls` **403 ×5** (tool UA, Chrome UA+full header set, 2 spaced retries — same URLs that 200'd at 13:12Z) · HT catalog **200 ×1** (29,445 B, unchallenged) · HT `/cgi/pt` full-view page **403 ×1** · CA titles **403**, CA pages **403**, CA **`/robots.txt` 403** |

No probe body in `_probe_fixed_20260925/` was overwritten or deleted: the re-verification
wrote to the new `v2_reverify/` subdirectory alongside the earlier evidence, and the failing
Chronicling America bodies (including the `CA-CANARY` ones) remain exactly as received,
because they are the proof that the block is theirs.

## What each host can actually deliver for a pre-1994 company (2026-09-25)

This distinction is not pedantry: **whether a company's depth tier may move depends on which
rung of this ladder an item sits on.** A pointer cannot be cited; a snippet can be cited as
a snippet and no more.

| Rung | Host / call, scripted today | Object returned | Verdict effect |
|---|---|---|---|
| 1. Nothing | `chronicling_america` (all paths, incl. `/robots.txt`) | 403 challenge page | **UNANSWERED.** The contemporaneous local-newspaper record — Walmart's 1945–62 Arkansas, UnitedHealth's 1970s Minneapolis — remains unseen. No tier may move on it, up *or* down |
| 2. Bibliographic metadata | `catalog.hathitrust.org/api/volumes/brief/…` (open), `archive.org/advancedsearch.php`, `archive.org/metadata/<id>` | title/date/rights/text-layer existence, `numFound` | Establishes **that an item exists and whether its text is openable**; a `numFound=0` is a null on those params only |
| 3. Records + counts, no text | `babel.hathitrust.org/cgi/ls` (window-dependent: 200 five times at 13:12Z, 403 five times at 13:44Z) | facet counts + record blocks (htid, title, date, Full/Limited view) | Names **which** items to open, and how many exist in a decade. Not quotable content |
| 4. Snippet-level text | `books.google.com/books/feeds/volumes` (open keyless) | volumeId + `pg=` matched page + **~250 chars of the matched page** in `dc:description` + viewability | Quotable as a finding, and enough to *identify* a lead worth chasing ("Charter Med, Minneapolis, which manages ten IPAs…", *Focus on HMOs*, 1978, `udRwLIq-iMoC` RA7, all_pages). Cannot carry a financial or chronology claim alone |
| 5. **Full text, openable** | `corporate_print` → `<server><dir>/<id>_djvu.txt` (open); IA periodical scans; HathiTrust Full-view items **via a browser** | the page, byte-saved, greppable | **This is the rung that moves tiers.** FY1972 Wal-Mart AR (23,989 B) flipped Walmart; Apple's four `all_pages` InfoWorld issues and UnitedHealth's `pur1.32754075976369` *Physicians Health Plan of Minnesota* (1980, Full view) are the first rung-5 candidates the other two companies have |

Two traps this table exists to prevent: (a) **`all_pages`/Full view is a right, not a
retrieval** — the scripted fetch of the same HathiTrust page still 403s, so a rung-3 or rung-4
item only becomes rung-5 when someone opens it; (b) **a snippet can name the wrong company** —
`yqYVAQAAMAAJ` *Modern Healthcare* 1990 "Charter Medical Corporation is the nation's largest
… private psychiatric" firm is a different corporation, and would have entered UnitedHealth's
chronology as a founder-era fact if a snippet had been read as an identification.

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
2. **Chronicling America is their block, not our bug — and it needs a different egress, not
   a different request.** Proven by the `/robots.txt` 403 (13:48Z, `Cf-Mitigated: challenge`,
   5,457 B), which carries none of our parameters. The two CA canary tasks exist so a run on
   a browser-egress (or LOC-granted) connection settles it in **2 requests**: a 200 on
   `CA-CANARY titles Bentonville` makes all 15 remaining CA tasks live; a 403 keeps the whole
   family UNANSWERED for this corpus. Until then no Walmart or UnitedHealth newspaper claim
   may be written as absent.
3. **HathiTrust search must be re-run in an open window and its full-view text fetched by a
   browser.** The same URLs that returned five 200s at 13:12Z returned five 403s at 13:44Z:
   the route works, the host decides when. The catalog API and `/cgi/pt` rights/metadata do
   work scripted today, so the productive pattern is *search in a browser → htid → rights by
   script → text by browser or IA*. Two configured HT tasks have **no 200 body yet** and are
   UNTRIED, not empty: `HT 'Metropolitan Health Plans' 1970-1989` and both Apple HT tasks.
4. **Google Books keyless is settled: use the feeds endpoint; a v1 key buys the rest.** The
   v1 429 with `quota_limit_value: 0` is Google's shared anonymous project, unchanged since
   2026-09-24, and no amount of polite delay alters it. What a key would add is search-text
   and page retrieval, not existence: the feeds already return the volumes, the viewability
   and ~250-char snippets listed in `_probe_fixed_20260925/LEADS.md`.
5. Family 5 could be extended to `prearchive.org`/`annualreports.com`-class corpora
   and to HathiTrust's corporate-print scans; none of those endpoints has been
   verified from this environment, so none is shipped.
6. `chronicling_america_ocr` is wired end-to-end (`ca_ocr_url`, `parse_ca_ocr`,
   `PARSERS["chronicling_america.ocr"]`, cap 4) but has **zero tasks** — by design: the page
   pattern is pre-relocation and may itself 308, so an `ocr` task must be queued from a
   live CA hit's own `id`, never from the old template (see
   `queries.json._deferred_examples.chronicling_america_ocr`).
