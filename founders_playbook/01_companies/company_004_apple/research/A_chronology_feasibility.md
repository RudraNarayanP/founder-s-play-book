# APPLE STAGE 1 — CHRONOLOGY AND FEASIBILITY PROBE

Level-3 (Corporate Historian + Feasibility) probe for company_004, run **before** any
eleven-agent fleet is committed. Purpose: establish what is actually retrievable about
Apple's founding period (1975–1980), fix the three stage boundaries, audit source
availability by document class, and render a depth verdict.

Method governance: `00_METHOD_AND_STYLE.md` §2 (hindsight firewall), §3 (classification),
§5 (tiers), §6 (time audit), §7 (formats), §9 (file splitting), §14 (retrieval discipline).

Company row: `00_universe/fortune_top_50_2026.csv` rank **#4**, Apple Inc., revenue
$416,161M, fiscal year ended **2025-09-27**, profit $112,010M, Cupertino, California,
"Computers, Office Equipment" / Fortune sector Technology. Tier-1 corroboration: SEC EDGAR
10-K XBRL exact match on revenue and profit, confidence High. Feasibility register class A
(single founder-lineage, continuous entity): "1976-04-01, Los Altos, California; founders
Steve Jobs, Steve Wozniak, Ronald Wayne" — sourced there to Wikipedia `action=raw`, i.e. a
Tier-2/3 pointer, explicitly *not* chased to registries or founding-era documents.

Hindsight firewall statement for this probe: nothing after 1985 is used here as evidence
that 1975–76 decisions were rational. Later fame is not admitted as proof of earlier
quality, and the Apple II's market success is not used to retro-validate the Apple I.

Confidence scale per §3: High (2+ independent sources or primary document) · Medium (one
reliable source) · Low (conflicting, vague, retrospective-only) · UNKNOWN (no evidence).

## Verdict (depth recommendation)

PLACEHOLDER — to be filled after retrieval.

## Recommended stage boundaries

| Stage | Start | End | Why This Boundary | Confidence |
|---|---|---|---|---|
| 1 | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |
| 2 | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |
| 3 | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |

**Fit against spec §6:** PLACEHOLDER.

## Findings

Format per record: `AP-nn Claim: … — Date: … — Source: … — Source date: … — URL: … —
Archived: … — Tier: <1-4> — Class: <FACT|FOUNDER CLAIM|CONTEMPORARY OBSERVATION|
RETROSPECTIVE INTERPRETATION|INFERENCE|ESTIMATE|UNKNOWN> — Passage: "…" or
NO_VERBATIM_PASSAGE_RECORDED — Conf: … — Corroboration: … — Conflicts: …`

Batch 1 — EDGAR and Wayback index probes (curl, no WebSearch/WebFetch budget spent).
All source files carry provenance headers in `../sources/`.

AP-01 Claim: Apple Inc.'s SEC registrant identity is EDGAR CIK **0000320193** (ticker AAPL, title "Apple Inc."), and the filing history is served in two bulk blocks — a "recent" block (1,000 rows, 2015-07-27 → present) and `CIK0000320193-submissions-001.json` (1,249 rows) covering **1994-01-26 → 2015-07-25** — Date: ongoing — Source: SEC EDGAR `company_tickers.json` + `submissions/CIK0000320193.json` — Source date: 2026-09-24 (retrieval) — URL: https://www.sec.gov/files/company_tickers.json ; https://data.sec.gov/submissions/CIK0000320193.json — Archived: sources/EDGAR_company_tickers.json, sources/EDGAR_submissions_CIK0000320193.json — Tier: 1 — Class: FACT — Passage: `"cik_str": 320193, "ticker": "AAPL", "title": "Apple Inc."` ; bulk-file descriptor `"filingCount": 1249, "filingFrom": "1994-01-26", "filingTo": "2015-07-25"` — Conf: High — Corroboration: 1 authoritative registry + 2 agreeing blocks — Conflicts: None. Note for fleet: CIK 320193 carries **no** `-submissions-002.json`; a request for anything older than 1994-01-26 through this API will not resolve.

AP-02 Claim: Apple's complete electronic filing history on EDGAR begins **1994-01-26** (a `424B5` and a `10-Q` for the quarter ended 1993-12-31, accession 0000320193-94-000002); there is **no** 1980 registration statement, no prospectus, no S-1, and no 10-K of any year before 1994 in the index — the 1976–1993 SEC record for Apple is paper-only, exactly as the Walmart probe found for Walmart — Date: 1994-01-26 — Source: EDGAR bulk submissions file `CIK0000320193-submissions-001.json`, sorted ascending by filingDate — Source date: 2026-09-24 (retrieval) — URL: https://data.sec.gov/submissions/CIK0000320193-submissions-001.json — Archived: sources/EDGAR_submissions_CIK0000320193_001_1994-2015.json — Tier: 1 — Class: FACT (documented absence within this index) — Passage: three oldest rows `1994-01-26 424B5 0000891618-94-000021`; `1994-01-26 10-Q 0000320193-94-000002 1993-12-31`; `1994-02-10 SC 13G/A 0000950150-94-000252` — Conf: High — Corroboration: 2 (recent + historical blocks agree; `min(filingDate)` = 1994-01-26) — Conflicts: None.

AP-03 Claim: Apple's first digitally available annual report is Form **10-K for fiscal year ended 1994-09-30, filed 1994-12-13, accession 0000320193-94-000016** (complete submission 240,556 B on disk); the form-type set present in Apple's whole pre-2000 index contains no S-1 — Date: 1994-12-13 — Source: EDGAR submissions index + Archives directory listing — Source date: 2026-09-24 — URL: https://www.sec.gov/Archives/edgar/data/320193/000032019394000016/ — Archived: sources/EDGAR_10-K_FY1994_acc0000320193-94-000016_index.json, sources/10-K_FY1994_acc-0000320193-94-000016_filed-1994-12-13.txt — Tier: 1 — Class: FACT — Passage: `"name":"0000320193-94-000016.txt" … "size":"209340"` — Conf: High — Corroboration: 1 — Conflicts: None.

AP-04 Claim: **Apple's own signed SEC filing states the incorporation date and jurisdiction: "Apple Computer, Inc. ('Apple' or the 'Company') was incorporated under the laws of the State of California on January 3, 1977."** This is the single most important date-anchor recovered by this probe and it comes from a Tier-1 registrant document, not from a memoir — Date: 1977-01-03 (event); 1994-12-13 (document) — Source: Apple Computer, Inc., Form 10-K, Item 1 "Business — General" — Source date: filed 1994-12-13 — URL: https://www.sec.gov/Archives/edgar/data/320193/000032019394000016/0000320193-94-000016.txt — Archived: sources/10-K_FY1994_acc-0000320193-94-000016_filed-1994-12-13.txt (lines 130–135 of the .txt) — Tier: 1 — Class: FACT — Passage: "Apple Computer, Inc. ('Apple' or the 'Company') was incorporated under the laws of the State of California on January 3, 1977." — Conf: High — Corroboration: 1 Tier-1 document; needs a second independent witness (California SoS entity record) to be unassailable — Conflicts: Open against the ubiquitous "April 1, 1976" founding date (see AP-05, U-AP-1): the filing dates the *corporation*, the lore dates the *partnership/company*.

AP-05 Claim: The FY1994 10-K's Item 1 contains **no** mention of Jobs, Wozniak, Wayne, 1975, 1976 or the founding story beyond that incorporation sentence — a grep of the full 240 KB submission for `Jobs|Wozniak|Wayne|founded|1976|1977` returns the incorporation sentence and the state-of-incorporation header only; Apple's own filings do not narrate the founding — Date: n/a — Source: full-text grep of the filing — Source date: 2026-09-24 — URL: as AP-04 — Archived: as AP-04 — Tier: 1 — Class: FACT (documented absence) — Passage: NO_VERBATIM_PASSAGE_RECORDED (negative finding) — Conf: High — Corroboration: 1 — Conflicts: None. Consequence: any founding narrative in an Apple dossier is sourced *outside* EDGAR.

AP-06 Claim: Apple's own exhibit index proves a **paper SEC record older than the electronic floor**: the FY1994 10-K incorporates by reference "88-S3 — Restated Articles of Incorporation, filed with the Secretary of State of the State of California on January 27, 1988"; "89-8A"; "90-2Q"; "91-8K" — filings that exist in the company's filing history but are **absent from EDGAR's electronic index** (floor 1994-01-26), and which name the California SoS as the registry holding the charter record — Date: 1988-01-27 (event) — Source: Form 10-K FY1994, Exhibit Index — Source date: 1994-12-13 — URL: as AP-04 — Archived: as AP-04 (lines 3175–3190) — Tier: 1 — Class: FACT — Passage: "3.1 88-S3 Restated Articles of Incorporation, filed with the Secretary of State of the State of California on January 27, 1988." — Conf: High — Corroboration: 1 — Conflicts: None. Route value: the California SoS business-entity file for "Apple Computer, Inc." is the authority that could carry original 1977 charter text.

AP-07 Claim: EDGAR **full-text search** has zero coverage before 2001: with the same query string `"Apple Computer"`, the index returns 3,081 hits for 2001-01-01→2001-12-31 but **0 hits** for 1999-01-01→2000-12-31 and **0 hits** for 1994-01-01→1996-12-31; a pre-1994 query scoped to CIK 320193 likewise returns `hits.total.value: 0` — Date: 2001-01-01 (coverage floor) — Source: efts.sec.gov LATEST search-index API, 4 queries incl. a positive control (`q=test` → 10,000+ hits, proving the endpoint works) — Source date: 2026-09-24 — URL: https://efts.sec.gov/LATEST/search-index?q=%22Apple+Computer%22&dateRange=custom&startdt=1994-01-01&enddt=1996-12-31 — Archived: sources/probe_edgar_fts_*.json (5 files) — Tier: 1 — Class: FACT (about the index, not about Apple) — Passage: `"hits":{"total":{"value":0,"relation":"eq"}}` (1994–96) vs `"value":3081` (2001) — Conf: High — Corroboration: 2 (control queries) — Conflicts: None. **Do not** read the pre-1994 zeros as evidence no such document exists; they are an index-coverage null. Recorded so no fleet agent re-burns this.

AP-08 Claim: No archived corporate web artifact of Apple predates the mid-1990s: the earliest Wayback capture at the **apple.com / www.apple.com** root is **1996-10-22 10:54:58** (HTTP 200, 5,133 B), and an exact-root query restricted to **1990-01-01→1993-12-31 returns an empty result set** (HTTP 200, zero rows — not a 504) — Date: 1996-10-22 — Source: Wayback CDX API — Source date: 2026-09-24 — URL: http://web.archive.org/cdx/search/cdx?url=apple.com&matchType=exact&from=1993&to=1999&fl=timestamp,original,statuscode,length&limit=12 ; …&from=1990&to=1993… — Archived: sources/probe_wayback_APPLE.md — Tier: 1 — Class: FACT (negative for pre-1994 at the exact root) — Passage: first row `19961022105458 http://www.apple.com:80/ 200 5133` — Conf: High — Corroboration: 2 identical runs — Conflicts: None. Caveat as in the Amazon run: `url=apple.com` and `url=www.apple.com` are **not two tests** (host normalised out of the urlkey, byte-identical rows); `matchType=prefix` sweeps were deliberately not run because they return 504 (unanswered, not proven).

AP-09 Claim: Two secondary Apple-related domains with real founding-period content have known early captures — **applecomputer.com** earliest **1996-12-19 05:06:58** (200, 7,760 B) and **apple2.org** (the community/reference site carrying Apple I/II documentation) earliest **1998-04-29 14:26:00** (200, 2,742 B); **wozniak.com** (Wozniak's own site) earliest **1998-12-07 07:02:41** (200, 2,275 B) — Date: 1996-12-19 / 1998-04-29 / 1998-12-07 — Source: Wayback CDX exact queries — Source date: 2026-09-24 — URL: as AP-08 with `url=applecomputer.com`, `url=apple2.org`, `url=wozniak.com` — Archived: sources/probe_wayback_APPLE.md — Tier: 1 (index facts) — Class: FACT — Passage: `19961219050658 http://www.applecomputer.com:80/ 200 7760`; `19980429142600 http://www.apple2.org:80/ 200 2742` — Conf: High — Corroboration: 1 index per domain — Conflicts: None. Route value: `wozniak.com` and `apple2.org` deep paths are the best candidates for first-party, pre-memoir founding-era text; neither was opened within this probe's budget.

## Source availability by document class

| Class | Earliest reachable | What it yields | Retrieval status | Notes |
|---|---|---|---|---|
| SEC filings (EDGAR) | PLACEHOLDER | PLACEHOLDER | NOT STARTED | |
| General & trade press 1975–1980 | PLACEHOLDER | PLACEHOLDER | NOT STARTED | |
| Archived web artifacts (Wayback) | PLACEHOLDER | PLACEHOLDER | NOT STARTED | |
| Public records (county / SoS / court) | PLACEHOLDER | PLACEHOLDER | NOT STARTED | |
| Memoir & secondary accounts | PLACEHOLDER | PLACEHOLDER | NOT STARTED | |
| Museum & primary artifacts | PLACEHOLDER | PLACEHOLDER | NOT STARTED | |

## Famous claims pre-flagged as likely untraceable

| Claim | Where it circulates | Any earlier source found | Expected verdict |
|---|---|---|---|
| PLACEHOLDER | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |

## Evidence cache

PLACEHOLDER — inventory of `../sources/` with provenance headers.

## Data gaps

| Gap | Why missing | Importance | Best available evidence | Confidence |
|---|---|---|---|---|
| PLACEHOLDER | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |

## Queries that returned null

| Query | Endpoint | Result | Interpretation |
|---|---|---|---|
| PLACEHOLDER | PLACEHOLDER | PLACEHOLDER | PLACEHOLDER |

## Fleet briefs if the run proceeds

PLACEHOLDER — six short specialist briefs (D1–D6).

— end of probe —
