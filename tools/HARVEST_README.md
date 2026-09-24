# HARVEST README — periodical_harvest.py

Batch harvester for the **digitised pre-1994 periodical corpus family** required by
`00_METHOD_AND_STYLE.md` §14 rule 6 (four-corpus-family rule). Built after the Walmart
(reopened) and UnitedHealth (provisional; Google Books HTTP 429) depth verdicts failed to
*see* this family, and modelled on the Apple probe (`company_004_apple/research/
A_chronology_feasibility.md`) which proved its value: Byte 1976 and the Homebrew newsletters
recovered as in-window Tier-1 text.

Stdlib-only Python 3 (urllib/json/csv/argparse/time). No installs, no third-party deps,
no keys. **Read-only public search APIs only — no paywall bypass, no login-gated content,
nothing a public API declines to return.**

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

## What the 2026-09-24 run returned (numbers from bodies on disk)

29 network requests / cap 60. 49 candidate rows: 1 TIER1_CANDIDATE, 28 LEAD_ONLY, 5 NULL, 15 UNANSWERED.

- **(a) Walmart 1945–1965:** IA `"Walton's" store` YEAR 1945–1965, `walton (retailing|variety store|five and dime)` 1945–1965, and `"$1.25 store"` → **proven nulls (numFound=0)**. `walton "five-and-dime"` → 2 hits, both **out of window** (1990 biography; 1998 DTIC discount-retail study incl. Wal-Mart — Tier-2 retrospective, LEAD_ONLY). **No in-window newspaper text was retrievable this run — CA blocked (UNANSWERED), which is exactly the gap the tool exists to close on the next network.**
- **(b) UnitedHealth 1971–1980:** IA `"charter med"` YEAR 1971–1985 and `"metropolitan health plans"` → **proven nulls (metadata-index level only)**. `"unitedhealthcare"/"united health care"` → 20 hits, all modern court-docket texts (LEAD_ONLY, post-window). `"burdic"` → 12 hits: one in-window date (1971 VA pension-cards microform, surname match only — the TIER1_CANDIDATE flag here is a date heuristic, treat as LEAD on inspection).

## Consuming results

1. Filter `candidates.csv` on `classification=TIER1_CANDIDATE|LEAD_ONLY`.
2. Open the URL (or the raw body in `<source_family>/`), read the item's own text — a search hit is a pointer, not evidence; per §14 rule 3 record documents in the company's `research/_EVIDENCE_CACHE.md`.
3. For CA hits worth mining: the `ocr_eng` field already carries page text (saved in the raw JSON), or queue a `chronicling_america_ocr` task.
4. Company `sources/` and `research/` directories are **protected archives** (§14 rule 4): this tool only ever writes under `00_universe/harvest/` — never into them, never deletes, never tidies.

## Adding a company

Edit `queries.json`: append tasks `{company, source_family, kind, query_label, params, window}` (+ raise `per_source_caps`). Dry-run, then run with a cap. Nothing in `.py` changes.
