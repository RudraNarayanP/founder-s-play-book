# WALMART STAGE 1 — CHRONOLOGY AND FEASIBILITY PROBE

Level-3 (Corporate Historian + Feasibility) probe for company_002, run **before** any
eleven-agent fleet is committed. Purpose: establish what is actually retrievable about
Walmart's founding period (1945/1950–1970), fix the three stage boundaries, audit source
availability, and render a depth verdict.

Method governance: `00_METHOD_AND_STYLE.md` §2 (hindsight firewall), §3 (classification),
§5 (tiers), §7 (formats), §9 (file splitting), §14 (retrieval discipline).
Company row: `00_universe/fortune_top_50_2026.csv` rank #2, Walmart, revenue $713,163M,
fiscal year ended 2026-01-31, profit $21,893M, Bentonville, Arkansas, General Merchandisers
(Tier-1 corroboration: SEC EDGAR 10-K XBRL exact match, per universe CSV notes).

## Verdict (depth recommendation, 4–8 sentences)

PENDING — to be filled after findings W-01…W-nn are on disk.

## Recommended stage boundaries

| Stage | Start | End | Why This Boundary | Confidence |
|---|---|---|---|---|
| PENDING | | | | |

## Findings

Format per record: `W-nn Claim: … — Date: … — Source: … — Source date: … — URL: … —
Archived: … — Tier: <1-4> — Class: <FACT|FOUNDER CLAIM|CONTEMPORARY OBSERVATION|
RETROSPECTIVE INTERPRETATION|INFERENCE|ESTIMATE|UNKNOWN> — Passage: "…" or
NO_VERBATIM_PASSAGE_RECORDED — Conf: … — Corroboration: … — Conflicts: …`

W-01 Claim: The SEC registrant for Walmart Inc. is EDGAR CIK 0000104169 (ticker WMT), currently named "Walmart Inc.", with formal former name "WAL MART STORES INC" — Date: ongoing — Source: SEC EDGAR company_tickers.json + submissions JSON — Source date: 2026-09-23 (retrieval) — URL: https://www.sec.gov/files/company_tickers.json ; https://data.sec.gov/submissions/CIK0000104169.json — Archived: sources/EDGAR_submissions_CIK0000104169.json — Tier: 1 — Class: FACT — Passage: `"cik_str": 104169, "ticker": "WMT", "title": "Walmart Inc."` and `"former": ["Walmart Inc.", "WAL MART STORES INC"]` — Conf: High — Corroboration: 1 authoritative registry — Conflicts: None. (Note for fleet: CIK 1041694 does NOT exist — the 7-digit guess returns S3 NoSuchKey; probe files retained in sources/.)

W-02 Claim: Walmart's complete EDGAR electronic filing history begins 1994-02-14 (an SC 13G/A); there is NO 1970 registration statement, prospectus, or any pre-1994 SEC document on EDGAR — the entire 1962–1993 SEC record exists only as paper at the SEC Public Reference Room / National Archives — Date: 1994-02-14 — Source: EDGAR submissions bulk file CIK0000104169-submissions-002.json (1,409 filings, 1994-02-14 → 2012-05-21) — Source date: 2026-09-23 (retrieval) — URL: https://data.sec.gov/submissions/CIK0000104169-submissions-002.json — Archived: sources/EDGAR_submissions_CIK0000104169_002_1994-2012.json — Tier: 1 — Class: FACT — Passage: oldest rows: `1994-02-14 0000950157-06-000672 SC 13G/A`; then `1995-02-13 … SC 13G/A`, `1995-04-27 0000104169-95-000004 10-K` — Conf: High — Corroboration: 2 (current + historical submissions blocks agree) — Conflicts: None.

W-03 Claim: The earliest Walmart annual report (Form 10-K) available digitally is accession 0000104169-95-000004 filed 1995-04-27 (fiscal year ended 1995-01-31); early 10-Ks may carry a brief company self-narrative of the founding but cannot be primary evidence for 1962–70 — Date: 1995-04-27 — Source: EDGAR submissions index — Source date: 2026-09-23 — URL: https://www.sec.gov/Archives/edgar/data/104169/000010416995000004/ — Archived: index row in sources/EDGAR_submissions_CIK0000104169_002_1994-2012.json — Tier: 1 — Class: FACT — Passage: NO_VERBATIM_PASSAGE_RECORDED (accession directory not yet opened) — Conf: High — Corroboration: 1 — Conflicts: None.

W-04 Claim: No archived walmart.com (or walmart.com) corporate web artifact predates 1990; the earliest Wayback root captures are 1996-12-29 (HTTP 200, ~789 bytes) — Date: 1996-12-29 — Source: Wayback CDX API, exact-url queries `url=walmart.com&matchType=exact&from=1990&to=1999` and `from=1994&to=1999` — Source date: 2026-09-23 — URL: http://web.archive.org/cdx/search/cdx?url=walmart.com&matchType=exact&from=1990&to=1999&fl=timestamp,original,statuscode,length&limit=30 — Archived: sources/probe_wayback_walmartcom_exact.txt, probe_wayback_walmart_exact.txt — Tier: 1 — Class: FACT (negative for pre-1990; index-confirmed) — Passage: first row `19961229070003 http://www.walmart.com:80/ 200 789` — Conf: High — Corroboration: 2 identical CDX runs — Conflicts: None. Caveat: `matchType=prefix` broad sweeps returned HTTP 504 (upstream capacity failure, NOT evidence of absence) — same trap recorded in the Amazon cache; do not re-run prefix sweeps.

W-05 Claim: The date "July 2, 1962" as the first Walmart store opening (Rogers, Arkansas) is asserted pervasively, but every web item surfaced by a targeted search is Tier-4 social/aggregator content (Instagram, Facebook, TikTok) or a 2025 regional-TV "this day in history" recap — no contemporaneous 1962 document appeared in results; the claim's provenance chain must be traced to the company timeline and/or 1962 press — Date: 1962-07-02 — Source: WebSearch results — Source date: 2026-09-23 — URL: e.g. https://www.5newsonline.com/article/news/history/this-day-history-first-walmart-opened-rogers/527-0e76ca72-23de-404c-a0e9-686f721d2ccb — Archived: NO_VERBATIM_PASSAGE_RECORDED — Tier: 4 (leads only) — Class: RETROSPECTIVE INTERPRETATION pending T1 — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: Medium (date), Low (any detail attached to it) — Corroboration: single lineage — Conflicts: None yet.

W-06 Claim: The official corporate history lives at corporate.walmart.com/about/history and is the presumptive source of the canonical timeline (store date, incorporation, IPO); Walmart Museum (Facebook, post 2019-06-14) states an archivist holds the actual 1950 bill of sale for Sam Walton's first store — a genuine primary artifact that exists but is not digitized publicly — Date: ongoing — Source: corporate.walmart.com; facebook.com/walmartmuseum — Source date: 2026-09-23 (search) — URL: https://corporate.walmart.com/about/history ; https://www.facebook.com/walmartmuseum/posts/2343625289030653/ — Archived: pending fetch — Tier: 1 artifact / company self-narrative; museum post Tier 4 lead — Class: RETROSPECTIVE INTERPRETATION (company telling its own history decades later) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: Medium — Corroboration: 0 independent — Conflicts: None yet.

W-07 Claim: A widely circulated incorporation story — "Wal-Mart, Inc." was incorporated 15 March 1962, and the Walmart Museum itself published (2020-10-31) a correction-style post noting the first store opened before the entity existed — needs the exact entity date, state, and original name pinned to a public record; no such record has surfaced in web results yet — Date: 1962-03-15 (claimed) — Source: WebSearch (Facebook/walmartmuseum post title fragment "while-the-first-walmart-opened-on-july-2-1962-wal-mart-inc-was-not-incorporated-…") — Source date: 2020-10-31 (post) — URL: https://www.facebook.com/walmartmuseum/posts/3524217377638099/ — Archived: NO — Tier: 4 lead — Class: UNKNOWN — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: Low — Corroboration: 0 — Conflicts: Open: "Wal-Mart Stores, Inc." incorporation (company timeline says Oct 1969) vs folklore "Wal-Mart, Inc. 1962".

W-08 Claim: The 1970 IPO is dated October 1, 1970 by all secondary sources, but the only share-count/price figures surfaced by search are Tier-4 (a PocketOption blog, a Brainly homework snippet claiming "300,000 shares" at an unstated price) — no filing text, no contemporaneous newspaper quotation recovered; IPO financials are currently UNDOCUMENTED at Tier 1 — Date: 1970-10-01 — Source: WebSearch — Source date: 2026-09-23 — URL: https://pocketoption.com/blog/en/news-events/data/walmart-stock-history/ ; https://brainly.com/question/37307087 — Archived: NO — Tier: 4 — Class: UNKNOWN (figures) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: Low (date), UNKNOWN (terms) — Corroboration: 0 independent — Conflicts: Possible: share count 300,000 (Brainly) vs later claims; unresolved.

(pending further records)

## Source availability by document class

| Class (filings / trade press / general newspapers / archived artifacts / public records / memoir) | Earliest reachable | What it yields | Retrieval status | Notes |
|---|---|---|---|---|
| PENDING | | | | |

## Famous claims pre-flagged as likely untraceable

| Claim | Where it circulates | Any earlier source found | Expected verdict |
|---|---|---|---|
| PENDING | | | | |

## Evidence cache (what is saved in ../sources/)

(pending)

## Data gaps

| Gap | Why missing | Importance | Best available evidence | Confidence |
|---|---|---|---|---|
| PENDING | | | | |

## Queries that returned null

| Query | Endpoint | Result | Interpretation |
|---|---|---|---|
| PENDING | | | | |

## Fleet briefs if parallelization proceeds

(pending: six specialist briefs — founder forensics; store-format and pricing;
supply/distribution; competition; finance/filings; adversarial)
