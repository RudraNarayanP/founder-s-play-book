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

**Recommendation: forensic-core (~6,000 words) for Walmart Stage 1 — not exemplar depth.**
The Tier-1 floor for 1962–1970 is nearly bare: EDGAR holds nothing filed before 1994-02-14,
the 1970 registration statement exists only as SEC paper, no corporate web artifact predates
1990 (first capture 1996-12-29), and open-web search surfaced **zero** contemporaneous
1950–62 press items quoting prices, sales, or store descriptions. The genuinely dated
fact-stock recovered so far is ~15–20 items, and almost all route through **two uncited
retrospective lineages** (the company's own timeline page, and Tier-2/3 retellings like PBS
2004 and SCDigest 2012) or Sam Walton's 1992 memoir. Exemplar density (~22,500 words × 11
dossiers) would therefore be filled by re-cutting the same lore six ways — precisely the
padding the method forbids. A forensic-core stage built on §§A–U with rigorous
UNKNOWN/classification discipline is achievable and honest now; **escalate toward exemplar
only if** the fleet's newspaper-archive probes (newspapers.com Arkansas/Rogers items
1962–70, the 1962 opening flyer, Arkansas SoS entity records, a 1970 prospectus facsimile)
land primary text — those four targets are the whole upside, and each is bounded-cheap to
test. Record count on this probe: 22 W-records.

## Recommended stage boundaries

| Stage | Start | End | Why This Boundary | Confidence |
|---|---|---|---|---|
| 1 — Founder state + first experiment | 1950 (documented only at Tier-2/3 + memoir: Walton operating the Bentonville Ben Franklin five-and-dime; 1945 Newport is even weaker) | 1970-10-01 (IPO; company/PBS-dated; the first moment public documentary machinery begins) | Everything before the IPO is one archival world: no SEC text, no filings-era financials, supply by wholesalers, entity history contested. The IPO is the only end boundary the record itself creates. | Start: Low · End: Medium |
| 2 — Listed but provincial | 1970-10-01 | 1979/80 fiscal boundary (FY ended 1980-01-31) — PROVISIONAL, needs its own feasibility pass; candidates: 1972 NYSE listing (documented) or first >$1bn sales year (checkable in paper 10-K/hoover-type sources) | Post-IPO decade is covered by annual-report text (paper, not EDGAR) and trade press; the 1970s end at the point where national-scale formats and national media coverage begin | Medium at start, Low at end |
| 3 — National formation | 1980 | 1992-04 (Sam Walton's death, heavily contemporaneous-press documented) or first international store (provisional; unverified here) | End-of-era marker is externally documented at Tier 1/2 and closes the founder-state period | Low — outside this probe's scope; flag for Stage 2/3 feasibility pass |

**Fit against spec §6 (origin → first real-world experiment → repeatable validation →
scalable formation):** Walmart breaks the template because its "first experiment" (1962)
predates the legal entity used in the SEC record (1969 incorporation; contested 1962 entity)
by seven years and predates any retrievable filing by 32 years (EDGAR floor 1994). The
evidence **can** support Stage 1 = "founder operating state + first format experiment →
going public," anchored on the IPO as the first hard documentary boundary. It **cannot**
support a §6-style Stage 1 of "origin with dated micro-chronology": 1945–61 has no
Tier-1 trace online at all, and even 1962–69 store-by-store chronology (openings, leases,
terms) is only reconstructable from behind paywalled newspaper archives, if at all. The
run must therefore accept a Stage 1 that is *boundary-strong, interior-quiet* — or fund the
newspaper-archive probe before promising interior detail.

## Source availability by document class

| Class | Earliest reachable | What it yields | Retrieval status | Notes |
|---|---|---|---|---|
| SEC filings (EDGAR) | **1994-02-14** (SC 13G/A); first 10-K 1995-04-27 (acc 0000104169-95-000004) | Post-1994 business narrative; 1990s 10-K Item 1 carries a one-line founding story only | DONE — full submissions history on disk | 1970 registration statement, 1970s 10-Ks = SEC paper only (Reference Room / National Archives Region Fort Worth); not scanned |
| Trade press 1950–62 (DNR/WWD, Discount Store News, Saturday Evening Post, Arkansas Gazette, Southwest Record) | UNKNOWN — nothing surfaced on open web | Would be the only contemporaneous price/crowd/sales evidence | NOT DONE — outside budget; requires newspapers.com / Gale / ArCat (UALR Arkansas newspaper archive, holds Arkansas Gazette) | Highest-value untested class; probe's 4 searches returned only post-2000 echoes |
| General newspapers | same as above | Rogers/Madison/Bentonville weeklies 1962 opening ads | NOT DONE | 1962 items may be microfilmed at state library |
| Archived corporate artifacts (web) | **1996-12-29** (walmart.com root, ~789 B) | Nothing pre-1990; null established by CDX exact queries | DONE (+ documented null; prefix sweeps 504 — upstream failure, do not re-run) | Corporate *physical* artifacts pre-1990 exist only at Walmart Museum (1950 bill of sale claimed on hand) |
| Public records (county/state) | Untested | Arkansas SoS corporation filings (1962/1969 entity dates); Benton County deed/lease records; Missouri SoS for any MO entities | NOT DONE | Arkansas SoS business search (arcbiz.arkansas.com) likely paywalled/registration-gated; Benton County Circuit Clerk offline — request routes needed |
| Memoir (Walton & Huey, *Made in America*, 1992) and secondary books | 1992 | The dominant source of nearly every famous founding detail | Known-exists; not quoted here | All memoir-sourced claims = FOUNDER CLAIM (retrospective), per §3; single lineage |
| Company self-narrative | corporate.walmart.com (undated page, retrieved 2026-09-23) | Canonical dated timeline with zero citations | DONE — extracted | T1 as artifact; T2-equivalent as evidence |

## Evidence cache (what is saved in ../sources/)

See `../sources/_RETRIEVAL_LOG.md` (authoritative table). On disk now: 2 EDGAR submissions
JSONs (CIK 0000104169 current + 1994–2012 block), SEC tickers map, 3 Wayback CDX probe
outputs (incl. the 504 artifact), 3 curated EXTRACT_*.md files (corporate timeline, PBS
2004, SCDigest 2012), and 3 retained SEC error pages proving the wrong-CIK dead end.
Nothing was deleted or moved at any point in this run.

## Data gaps

| Gap | Why missing | Importance | Best available evidence | Confidence |
|---|---|---|---|---|
| 1970 IPO terms in filing text (date, shares, price, proceeds) | Pre-EDGAR paper; never located online | HIGH — stage endpoint | Company page "$16.50 per share" + PBS $44.2M/38 stores | Low-Med |
| Original entity name/date(s): "Wal-Mart, Inc." 1962 vs 1969 incorporation | No digitized Arkansas corporate record tested | HIGH — chronology spine | W-11 + U-1 | Low |
| 1962 opening-day prices, crowd, sales from contemporaneous print | Trade/newspaper archives paywalled, untested | HIGH — the section-D exemplar moment | Flyer artifact lead (W-20) | UNKNOWN |
| Sam's pre-1962 operations: Newport dates, Bentonville purchase price/rent, lease-loss terms and date | Memoir-only lineage; no county records tested | HIGH for founder state | Museum bill-of-sale claim (W-21) | Low |
| Ben Franklin franchise relationship: start, terms, what ended it | Single-source (memoir) | MED-HIGH | none Tier-1 | UNKNOWN |
| Bud Walton / Plaza store date + first hires (employee #1 folklore) | No digitized payroll; lore | MED | none found | UNKNOWN |
| First DC: exact year/location/size (1970 vs 1971; Bentonville vs Springfield MO) | Conflicting uncited retrospectives (U-2) | MED | SCDigest pre-1970 supply mode (W-18) | Low |
| How many stores existed 1962–66 and where (Rogers, Bentonville Plaza, Jonesboro…) | Only aggregated counts at 1967 | MED | company 24-store/$12.7M datapoint | Low |

## Queries that returned null

| Query | Endpoint | Result | Interpretation |
|---|---|---|---|
| `url=walmart.com&matchType=exact&from=1990&to=1999` | Wayback CDX | earliest 1996-12-29 | No pre-1990 web artifact — established for exact-root queries |
| `url=walmart.com&matchType=exact&from=1994&to=1999` | Wayback CDX | identical (host-normalised) | walmart.com vs www are not two tests |
| `matchType=prefix&from=1994&to=1994` | Wayback CDX | HTTP 504 | Upstream capacity failure, NOT absence; do not re-run fat sweeps (Amazon-run lesson) |
| `CIK0001041694*.json` (7-digit guess) | data.sec.gov | S3 NoSuchKey ×3 | CIK is 104169 — recorded so no agent re-burns this |
| "1962 Wal-Mart opening advertisement…", "earliest trade coverage…" etc. (4 WebSearches) | general web | social/commemoration only | Contemporary print exists only inside paywalled/untested archives — fleet brief D1 targets it |

## Fleet briefs if parallelization proceeds

**D1 FOUNDER FORENSICS (pre-1962).** Targets: Newport-era store dates/ownership (Ben Franklin
franchise 1945–50; search "Newport Merchant" Nebraska newspaper archive — the Newport
*Merchant* paper ran Walton-era ads); Bentonville 1950 store purchase price and lease terms
from the *Benton Courier* / *Northwest Arkansas Times* (both partially digitized on
newspapers.com — try 1950–62 items naming "Walton's Store", "Ben Franklin"); the lease-loss
event date (was it 1960? was the non-renewal reported or only remembered in 1992?). Chase the
Walmart Museum bill of sale (W-21) for a published image or accession. Every output from
*Made in America* must be labeled FOUNDER CLAIM (retrospective memory) — the memoir is the
*only* witness for most of this period; finding any 1950s–62 print item that independently
names Sam's store is the brief's win condition.

**D2 STORE FORMAT & PRICING (1962).** Fetch the reddit r/vintageads grand-opening flyer
(W-20; use old.reddit.com or the i.reddit image endpoints; if blocked, search "Wal-Mart 1962
opening flyer" images via the Walmart Museum). Extract advertised items and prices verbatim;
compare with the 1962 "Wal-Mart Discount City" signage and the 6,000-sq-ft / warehouse-building
claims. Test the opening-day sales figure's first print appearance (memoir? 1980 HBS case?
*Fortune* 1980s?). Deliverable: which opening-day numbers have a pre-1992 source at all.

**D3 SUPPLY & DISTRIBUTION (1962–1971).** Resolve U-2: search "Wal-Mart" "Springfield"
Missouri warehouse 1970 (Springfield *News & Leader* / Greene County records; the
Missouri State Digital Newspaper Center is free and covers 1970s MO titles). Confirm SCDigest's
"vendor direct + wholesalers" pre-1970 mode against the 1962–69 franchise-warehouse pickup
story (Ben Franklin's Kansas City warehouse). Check the 1996 10-K / FY1996-97 annual reports
for any "History" paragraph dating the first DC — cheap EDGAR text, accession indices already
on disk here.

**D4 COMPETITION & CONTEMPORANEOUS PRESS (1955–1970).** Map the 1962 discount landscape as
knowable then: Woolworth's/Kresge/S.H. Kress variety stores, FedMart (1963), Two Guys/Gibson,
and the 1962 "discount house" trade controversy (DNR/WWD coverage of the NY discount-store
injunction fights — real, dated trade coverage that frames Walmart's format in-period).
Then newspapers.com: Arkansas Gazette + Southwest Record (St. Louis) for "Wal-Mart" 1962–70;
target any item quoting store counts/sales contemporaneously — those, if found, are the ONLY
Tier-1 interior evidence possible.

**D5 FINANCE & FILINGS.** EDGAR text 1994→back is empty for the founding period (established);
so: (a) find any digitized 1970 prospectus or 1970s annual report (HathiTrust/Hoover's
Business Press archives; Arkansasiana); (b) pin the IPO: "$16.50" — confirm against a 1970–72
newspaper quote (NYT archive has 1970-wire obituary-adjacent mentions; *Fortune* 1972 profile
attempted?); (c) FY-ends-01-31 convention: derive FY1970 sales $44.2M basis (12 months to
1970-01-31) and show arithmetic; (d) chase Arkansas SoS incorporation records for both entities.

**D6 ADVERSARIAL.** Attack the spine this probe built: (1) every "fact" here traces to an
uncited company page or a 2004/2012 retrospective — demand a pre-1992 witness for each;
(2) the 1967 "24 stores/$12.7M" vs PBS 1970 "38 stores/$44.2M" vs the 1969 "50 stores" lore —
find the store-count series' real source (1970 prospectus quoted in press?); (3) hindsight
check the framing of 1962 as "the beginning of retail's future" — in 1962 dozens of discount
formats launched and failed; document the failures around Walmart (the many Arkansas-area
discount ventures that died, Kmart's 1962-scale dominance: Kmart opened its first store
Mar 1962, S.S. Kresge — already 130+ stores by 1962; verify with dated sources); (4) test
whether "Walmart lost #1 to Amazon in 2026" framing (universe CSV) is leaking backward into
stage selection — it must not.


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

W-09 Claim: Walmart's own official corporate-history timeline (corporate.walmart.com/about/history) states: "On July 2, 1962, Sam Walton opens the first Walmart store in Rogers, Arkansas" — Date: 1962-07-02 — Source: Walmart Corporate, "Walmart History" — Source date: retrieved 2026-09-23; page undated — URL: https://corporate.walmart.com/about/history — Archived: sources/EXTRACT_corporate_walmart_history_timeline.md — Tier: 1 artifact / Class: RETROSPECTIVE INTERPRETATION (company self-narrative, zero primary citations on the page) — Passage: "On July 2, 1962, Sam Walton opens the first Walmart store in Rogers, Arkansas." — Conf: Medium (universally repeated single lineage; no 1962 document yet retrieved) — Corroboration: PBS 2004 (W-16) repeats it — but both may trace to the same company lore — Conflicts: None on the date itself.

W-10 Claim: The company timeline gives 1967 as "The Walton family owns 24 stores, ringing up $12.7 million in sales" — an unsourced pre-IPO financial datapoint — Date: 1967 — Source: corporate.walmart.com/about/history — Source date: retrieved 2026-09-23 — URL: https://corporate.walmart.com/about/history — Archived: sources/EXTRACT_corporate_walmart_history_timeline.md — Tier: 1 artifact, company narrative — Class: ESTIMATE/RETROSPECTIVE INTERPRETATION, basis unstated (stores owned vs operated? fiscal year? sales basis?) — Passage: "The Walton family owns 24 stores, ringing up $12.7 million in sales." — Conf: Low — Corroboration: 0 independent — Conflicts: Open — compare W-18 (PBS: 38 stores at 1970).

W-11 Claim: Official timeline: "The company officially incorporates as Wal-Mart Stores, Inc." in 1969 — year only, no month/day, no state, no citation; the frequently repeated "Wal-Mart, Inc., March 15, 1962" earlier-entity claim appears nowhere on the official page and remains undocumented — Date: 1969 — Source: corporate.walmart.com/about/history — Source date: retrieved 2026-09-23 — URL: https://corporate.walmart.com/about/history — Archived: sources/EXTRACT_corporate_walmart_history_timeline.md — Tier: 1 artifact — Class: FACT (that the company says this) / UNKNOWN (exact incorporation date, original entity name 1962?) — Passage: "The company officially incorporates as Wal-Mart Stores, Inc." — Conf: Medium — Corroboration: Walmart Museum Facebook post (2020-10-31, title fragment "…wal-mart-inc-was-not-incorporated-…") suggests the museum distinguishes a separate "Wal-Mart, Inc." from the store opening — text not retrievable at budget — Conflicts: U-1 (see below).

W-12 Claim: Official timeline: 1970 "Walmart becomes a publicly traded company. The first stock is sold at $16.50 per share." The page gives no date-of-IPO precision, no share count, no proceeds, no underwriter — and no filing citation; the oft-repeated "October 1, 1970" is corroborated only by Tier-4 aggregators so far (W-08) — Date: 1970 — Source: corporate.walmart.com/about/history — Source date: retrieved 2026-09-23 — URL: https://corporate.walmart.com/about/history — Archived: sources/EXTRACT_corporate_walmart_history_timeline.md — Tier: 1 artifact, company narrative — Class: RETROSPECTIVE INTERPRETATION — Passage: "The first stock is sold at $16.50 per share." — Conf: Medium ($16.50 price; two independent lines of transmission incl. PBS-era retellings) — Corroboration: 1 (company) — Conflicts: IPO exact date = UNKNOWN at Tier 1; 1970 registration text not on EDGAR (W-02).

W-13 Claim: Official timeline: 1971 "The first distribution center and Home Office open in Bentonville, Arkansas." — Date: 1971 — Source: corporate.walmart.com/about/history — Source date: retrieved 2026-09-23 — URL: https://corporate.walmart.com/about/history — Archived: sources/EXTRACT_corporate_walmart_history_timeline.md — Tier: 1 artifact — Class: RETROSPECTIVE INTERPRETATION — Passage: "The first distribution center and Home Office open in Bentonville, Arkansas." — Conf: Medium — Corroboration: 0 independent — Conflicts: U-2 (PBS says 1970 Bentonville DC; SCDigest says 1970; lore says Springfield, Missouri).

W-14 Claim: Official timeline: 1972 "Walmart is listed on the New York Stock Exchange (WMT). With 51 stores, Walmart records sales of $78 million." — Date: 1972 — Source: corporate.walmart.com/about/history — Source date: retrieved 2026-09-23 — URL: https://corporate.walmart.com/about/history — Archived: sources/EXTRACT_corporate_walmart_history_timeline.md — Tier: 1 artifact, no citations — Class: RETROSPECTIVE INTERPRETATION — Passage: "Walmart is listed on the New York Stock Exchange (WMT). With 51 stores, Walmart records sales of $78 million." — Conf: Medium — Corroboration: PBS 2004 confirms NYSE listing year (W-19) — Conflicts: None.

W-15 Claim: The official corporate history contains **nothing** about pre-1962 operations: no Newport Nebraska/Ben Franklin years, no Bentonville 1950 store, no lease-loss story, no Bud Walton Plaza store — the company's own curated narrative starts cold at 1962, which means the founding-period detail circulating everywhere is sourced to the memoir and secondary books, not to the firm's records — Date: n/a — Source: corporate.walmart.com/about/history — Source date: retrieved 2026-09-23 — URL: https://corporate.walmart.com/about/history — Archived: sources/EXTRACT_corporate_walmart_history_timeline.md — Tier: 1 (documented absence) — Class: FACT (absence observed) — Passage: NO_VERBATIM_PASSAGE_RECORDED (negative finding) — Conf: High — Corroboration: 1 — Conflicts: None.

W-16 Claim: PBS NewsHour's August 2004 retrospective timeline states the first store date and the 1968 out-of-state expansion — Date: 2004-08-20 — Source: "Timeline: An Overview of Wal-Mart," PBS NewsHour — Source date: 2004-08-20 — URL: https://www.pbs.org/newshour/economy/business-july-dec04-timeline_08-20 — Archived: sources/EXTRACT_pbs_2004_timeline.md — Tier: 2 (reported retrospective) — Class: RETROSPECTIVE INTERPRETATION — Passage: "The first Wal-Mart store opens in Rogers, Ark."; "Wal-Mart expands outside of Arkansas, opening stores in Sikekton, Mo., and Claremore, Okla." [sic — Sikeston] — Conf: Medium — Corroboration: company page for 1962 — Conflicts: first-out-of-state town names need press corroboration (1968).

W-17 Claim: PBS 2004 gives the key end-of-stage financials: "With 38 stores open, Wal-Mart enjoys $44.2 million in sales" for 1970, and places the first distribution center in Bentonville in 1970 — Date: 1970 — Source: PBS NewsHour timeline — Source date: 2004-08-20 — URL: https://www.pbs.org/newshour/economy/business-july-dec04-timeline_08-20 — Archived: sources/EXTRACT_pbs_2004_timeline.md — Tier: 2 — Class: RETROSPECTIVE INTERPRETATION / ESTIMATE — Passage: "With 38 stores open, Wal-Mart enjoys $44.2 million in sales."; "The company also opened its first distribution center in 1970 in Bentonville, Ark." — Conf: Medium ($44.2M is the figure most secondary accounts use for FY ending 1970-01-31; no filing text seen) — Corroboration: 1 (no second independent source yet) — Conflicts: U-2 on the DC (1970 vs 1971; Bentonville vs Springfield MO lore); store count 38 vs company's own 1967=24 trajectory.

W-18 Claim: SCDigest's "50 Years of Supply Chain at Walmart" (2012) states that before the first DC, "stores were stocked by vendor direct shipments and wholesalers," and dates the first DC to 1970 — the supply-side null for 1962–69: no owned logistics existed, a fact consistent with a single-wholesaler franchise model — Date: 2012-07-27 — Source: SCDigest On Target — Source date: 2012-07-27 — URL: https://www.scdigest.com/ASSETS/ON_TARGET/12-07-27-1.php — Archived: sources/EXTRACT_scdigest_2012_timeline.md — Tier: 3 (trade publication, retrospective) — Class: RETROSPECTIVE INTERPRETATION — Passage: "Before then, stores were stocked by vendor direct shipments and wholesalers." — Conf: Medium — Corroboration: consistent with absence of DC in pre-1970 record — Conflicts: none on substance; year conflict as U-2.

W-19 Claim: Vintage Bentonville (a cited-locally project, 2018) says Walton "managed a Ben Franklin variety outlet in Newport, **Arkansas**" — the state is wrong (Newport is in Nebraska; the company never states otherwise; this is how folklore corrupts) — and calls the Bentonville store "Walton's 5&10 near the Bentonville town square," giving no dates, prices, or lease terms; no source list on the page — Date: 2018? — Source: vintagebentonville.com "Walton, Sam" — Source date: retrieved 2026-09-23 — URL: https://www.vintagebentonville.com/walton-sam.html — Archived: NO — Tier: 3/4 local-history lead — Class: RETROSPECTIVE INTERPRETATION, with observed error — Passage: NO_VERBATIM_PASSAGE_RECORDED (summary returned by retrieval) — Conf: Low — Corroboration: 0 — Conflicts: Newport NB vs "Arkansas" — fleet must resolve the Newport item from a Tier-2 biography or press.

W-20 Claim: A physical 1962 grand-opening **flyer invitation** for the first Wal-Mart store exists and circulates as an image (Reddit r/vintageads thread, 2024-11-30) — this is the single best lead to genuine in-period advertising prices for 1962; it was NOT retrieved within this probe's budget — Date: 1962 (artifact) — Source: reddit.com/r/vintageads — Source date: 2024-11-30 — URL: https://www.reddit.com/r/vintageads/comments/1h3nx3t/flyer_invitation_to_the_grand_opening_of_the/ — Archived: NO — Tier: 4 host, but the flyer itself would be a Tier-1 artifact if photographed legibly — Class: UNKNOWN (contents unread here) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: Medium (existence), UNKNOWN (text) — Corroboration: 0 — Conflicts: None.

W-21 Claim: The Walmart Museum (Bentonville) publicly states its archivist holds the **bill of sale for Sam Walton's first (1950 Bentonville) store** — a primary 1950 document that exists but is not digitized on the open web — Date: 2019-06-14 (post) — Source: facebook.com/walmartmuseum — Source date: 2019-06-14 — URL: https://www.facebook.com/walmartmuseum/posts/2343625289030653/ — Archived: NO (Facebook, fetch-unfriendly) — Tier: 4 lead to a Tier-1 artifact — Class: FACT (that the museum claims to hold it) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: Medium — Corroboration: 0 — Conflicts: None. Fleet action: contact museum / look for digitized image in press.

W-22 Claim: As of this probe, NO contemporaneous 1950–1962 newspaper or trade-press item (Arkansas Gazette, Daily News Record/Women's Wear Daily, Discount Store News, Saturday Evening Post) was found in open-web search results that quotes 1962 prices, sales, or store descriptions; searches returned only social-media commemorations and retrospective TV recaps — Date: n/a — Source: WebSearch ×4 (this probe) — Source date: 2026-09-23 — URL: see null table — Archived: N/A — Tier: N/A — Class: documented absence for these queries — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High for these endpoints (general web search); NOT established for newspaper databases (newspapers.com, Arkansas Gazette archive at UALR/ArCat, Chronicling America beyond 1963, Fold3) which were not tested — Corroboration: none — Conflicts: None.

## Conflicts register (for section U of the dossier)

U-1 **Original legal entity.** (a) Company timeline: incorporated 1969 as "Wal-Mart Stores, Inc." (b) ubiquitous lore: "Wal-Mart, Inc." incorporated 15 March 1962 (c) museum post (uncaptured) distinguishing the two. / WHY THEY DIFFER: likely two incorporations (1962 operating entity, 1969 holding reorganization) collapsed into one lore date. / EVIDENCE WEIGHT: (a) Tier-1 artifact but uncited; (b) Tier-4; Arkansas Secretary of State and Benton County records untested. / BEST-SUPPORTED: two-step formation, unproven. / RESIDUAL: exact dates and names UNKNOWN. / CONFIDENCE: Low.

U-2 **First distribution center.** (a) corporate.walmart.com: 1971, Bentonville ("first distribution center and Home Office"); (b) PBS: 1970, Bentonville; (c) SCDigest: 1970, location unspecified; (d) widespread lore: a leased Springfield, Missouri warehouse c.1970. / WHY THEY DIFFER: none of the four sources cites a lease or filing; anniversary-marketing rounding. / EVIDENCE WEIGHT: all retrospective. / BEST-SUPPORTED: "first owned DC at the very start of the 1970s; 1962–69 supplied by vendor direct + wholesalers (W-18)." / RESIDUAL: year 1970-vs-1971 and Bentonville-vs-Springfield unresolved; lease records would settle it. / CONFIDENCE: Low-Medium.

U-3 **Newport store location state**: vintagebentonville says "Newport, Arkansas"; all book lore says Newport, Nebraska. Untested here. / Low.

## Famous claims pre-flagged as likely untraceable

| Claim | Where it circulates | Any earlier source found | Expected verdict |
|---|---|---|---|
| Opening-day sales/crowd at Rogers, 2 July 1962 (variously "$1,402", "packed parking lot", "half the town came") | Walton/Huey *Made in America* (1992); every listicle | NONE — no 1962 press item retrieved; flyer (W-20) may carry advertised prices but not sales | FOUNDER CLAIM (retrospective memory), Conf Low; sales figure likely UNTRACEABLE unless museum holds register records |
| "Wal-Mart, Inc. incorporated March 15, 1962" | countless summaries; not on corporate timeline | No Tier-1 record; museum post disputes timing (W-11) | UNTRACEABLE pending Arkansas SoS record |
| Sam "discovered" discounting at a 1962 trade show / copied the Ben Franklin "strip" plan only after seeing a Manhattan Ben Franklin discounter | memoir + biographies | None contemporaneous | FOUNDER CLAIM (retrospective), single-source memoir |
| Pre-1962 Bentonville lease "lost because landlord wanted the site for his son-in-law" (motive clause) | memoir; every secondary retelling | Lease document untested (Benton County records) | Event plausible-attested only by memoir; motive = UNTRACEABLE |
| "I never took my eye off the ball"/sunrise chants etc. as founding-period practice | memoir, corporate lore | No in-period evidence | RETROSPECTIVE — exclude from Stage 1 as evidence |
| 1962 store "stocked 45,000 items / was 6,000 sq ft" | aggregator articles | None retrieved | UNTRACEABLE pending lease/deed or flyer |
| IPO "October 1, 1970, 300,000 shares at $16.50 (net $15.x)" | Brainly/TikTok-tier + paywalled press | $16.50 from company timeline (uncited); date+share count Tier-4 only | Price Medium, date Low, shares UNKNOWN; 1970 prospectus exists only on SEC paper — chase via reference room scan or contemporaneous newspaper (NYT archive has paid-obituaries echo) |

— end of probe —

