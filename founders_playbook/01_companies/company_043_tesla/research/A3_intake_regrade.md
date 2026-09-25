# A3_intake_regrade.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T20:49:21Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## Dry run

STATUS: WRITTEN 2026-09-27 (regrade pass, agent `regrade-t3-batch`; all figures observed in this session)

`resolve --ticker TSLA` → `{"ticker": "TSLA", "cik": 1318605, "name": "Tesla, Inc."}`. Entity question **not
re-resolved** — the probe settled it; window used throughout: **2003-01-01 → 2012-12-31**.

`python tools/sec_intake.py index --cik 1318605 --company-dir founders_playbook/01_companies/company_043_tesla --from 2003-01-01 --to 2012-12-31 --dry-run`
→ `index: 1750 filings from Tesla, Inc. (TSLA); earliest forms: 10-K, 10-K/A, 10-Q, 144, 3, 3/A, 4, 4/A, 424B3, 424B4, 424B5, 425, 5, 5/A` — identical to the live run, so no download was needed to see coverage.
Pre-state of `sources/_index/_INDEX.md` was already the same registrant ("Tesla, Inc. (CIK 0001318605, TSLA),
1750 filings enumerated", built 2026-09-25 19:42 UTC), so unlike Dell this pass overwrote only its own kind —
no sibling-CIK artifact was displaced.

**Tesla is the one company in this batch where the broken build under-called the archive the least and the
probe's own index was already right — and where the re-grade still found the probe wrong on one structural
claim** (see §Index: the 2005–2009 REGDEX band, and §Stored bytes: 76 documents where the probe held 4).

## Index

STATUS: WRITTEN 2026-09-27 (regrade pass)

Parsed `sources/_index/submissions.csv` after the live run (`filingDate,form,accession,reportDate,primaryDocument,source`):

- total rows **1,750**; rows inside **2003-01-01 → 2012-12-31** = **269**; **blank `primaryDocument` = 0 of 269.**
  The nameless-listing defect is a pre-2001 phenomenon and does not bite here; this is why Tesla's index was
  never the problem, and why its ceiling is limited by *other* families, not by EDGAR enumeration.
- **Earliest in-window row in the index: Form REGDEX, accession `9999999997-05-006484`, filed 2005-02-17**
  (primaryDocument `9999999997-05-006484.paper`). Then REGDEX/A 2005-05-31, REGDEX/A 2005-06-16, REGDEX
  2005-12-01, REGDEX 2006-04-13, REGDEX 2006-05-25, REGDEX 2006-06-08, REGDEX/A 2006-06-28, REGDEX 2007-05-24,
  REGDEX 2008-03-05, REGDEX/A 2008-06-13, REGDEX 2009-01-12 — **12 rows in the 2005-02-17 → 2009-01-12 band,
  every one a SEC-generated `9999999997-*` paper accession with a `.paper` primary document.**
- **Correction to the probe's §Verdict/§D6 claim** "Nothing EDGAR-dated 2003–2008: earliest submission … is
  Form D **2009-04-09**". Measured now: the slice's first Form **D** is indeed 2009-04-09, but the slice is
  **not empty before it** — it holds those 12 REGDEX/REGDEX/A rows from **2005-02-17**. The correction narrows,
  it does not demolish, the probe's point: **2003 and 2004 are genuinely empty on this CIK**, and REGDEX items
  carry **no company-authored narrative** (they are paper registration/exemption index entries). Earliest
  *substantive registrant document* remains the **S-1 of 2010-01-29**. But "EDGAR is empty for the first five
  and a half years of the company's existence" must be re-worded to **"empty of company documents 2003–2004,
  then SEC paper REGDEX entries 2005–2009"** — a null about *content*, not about *rows*.
- Earliest per form in-window: REGDEX 2005-02-17 · REGDEX/A 2005-05-31 · D 2009-04-09 · S-1 2010-01-29 ·
  UPLOAD 2010-02-25 · S-1/A 2010-03-29 · 8-A12B 2010-05-27 · CORRESP 2010-06-08 · CERTNAS 2010-06-21 ·
  3 2010-06-25 · EFFECT 2010-06-28 · FWP 2010-06-28 (+ 424B4 2010-06-29, 10-K 2011-03-03, DEF 14A 2011-04-08).
- **`facts` worked here, unlike the other three companies in this batch**:
  `facts: wrote 336 rows -> founders_playbook\01_companies\company_043_tesla\sources\financials\xbrl_early_series.csv`
  and the file is on disk: **336 rows**, columns `tag,unit,start,end,value,fy,fp,form`, **`end` range
  2008-12-31 → 2012-12-31, all 336 rows in-window**. The 2008-12-31 and 2009 comparatives are **pre-IPO money
  carried in the registrant's own XBRL** — a new §K-bearing asset this batch produced nowhere else.

## Stored bytes

STATUS: WRITTEN 2026-09-27 (regrade pass)

`auto --cik 1318605 --from 2003-01-01 --to 2012-12-31 --max-docs 25` →
**`auto: 76 documents stored (59479299 bytes, 3059480 words), 0 UNANSWERED (counted, not nulls)`**, exit code 0;
`sources/sec/_UNANSWERED.csv` parses to **0 rows**.
Probe comparison: **4 documents (≈5.9 MB)** → **76 documents, 59,479,299 bytes (59.5 MB), 3,059,480 words**
across **28 accessions**, i.e. ~10× the bytes and the *entire* registration lineage rather than one branch of it.

From `sources/sec/_MANIFEST.csv` (76 rows, all `status ok`, header `accession,file,path,bytes,words,status,form,filingDate,url,listing`):
- **Earliest held: S-1 2010-01-29, accession 0001193125-10-017054, `ds1.htm` 2,362,163 B** — the probe's D1,
  re-fetched at the identical byte count, plus 3 exhibits the probe did not hold (`dex1023.htm` 568,385 ·
  `dex1022.htm` 470,947 · `dex1019.htm` 333,067).
- **Latest held: SC 13G/A 2012-02-14, 0000950155-12-000015, 260,500 + 262,178 B.**
- Complete S-1 lineage now held (the probe had 3 of these accessions): S-1/A 2010-03-29 (0001193125-10-068933,
  4 docs), S-1/A 2010-04-29 (…-10-099603, `ds1a.htm` 2,189,012 B — same as probe D2), S-1/A 2010-05-27
  (…-10-129878, incl. `dex1037.htm` 1,571,717 B), S-1/A 20010-06-02 (0000950130-10-002906, incl. full
  submission txt 4,637,571 B), 2010-06-15 (…-10-139143), 2010-06-28 ×3 (…-10-148468, -10-147850, -10-147655),
  424B4 2010-06-29 (…-10-149105, `d424b4.htm` 2,677,451 B + submission txt 4,731,793 B), 8-K 2010-08-04,
  SC 13G ×4 2011-02 (+ 2011-04-08, 2012-02-09), 10-K 2011-03-03 (`d10k.htm` 1,669,538 B = probe D4),
  DEF 14A 2011-04-08 (`ddef14a.htm` 588,431 B = probe D5), S-1 2011-05-25 + S-1/A 2011-06-02, 8-K 2011-10-11 and
  2011-11-02 (`d249698dex991.htm` 200,152 B), SC 13G/A 2012-02-08.
- **Not held:** the 12 2005–2009 REGDEX `.paper` rows, all `3/4/5/144` beneficial-ownership forms, `10-Q`s,
  `CORRESP`, `424B3/424B5`, `425`, `UPLOAD`. `auto` reported **0 UNANSWERED while leaving 269 in-window index
  rows at 28 fetched accessions** — the same silent-drop defect seen at Costco and Dell. **UNTRIED, not null.**

Filings, not apology pages: `grep -l -i "File Unavailable\|Temporarily Offline\|NoSuchKey" sources/sec/*.txt`
→ **0 files matched**. Substantive phrase counts read out of stored bytes this session (`grep -o -i`, per file):

| phrase | S-1 2010-01-29 | S-1/A 2010-04-29 | 424B4 2010-06-29 | 10-K 2011-03-03 |
|---|---|---|---|---|
| "Tesla Motors" | 52 | 58 | 64 | 20 |
| "formed in July 2003" | **1** | 1 | 1 | 1 |
| "one of our founders" | **0** | **1** | **1** | 0 |

This **reproduces the probe's central dating finding on script-stored bytes**: the founder adjective enters the
filing record between 2010-01-29 and 2010-04-29 and the July 2003 entity statement is present from the first
S-1. (The probe's quoted "incorporated … on July 1, 2003" as one string returned **0** in the raw HTML of all
four files — markup splits the run — so only the counts above are claimed here.)

## Family a verdict

STATUS: WRITTEN 2026-09-27 (regrade pass) — verdict **in-window Tier-1 text (YES), unchanged in kind; +10× bytes; one structural null corrected.**

- Probe verdict: **(a) ANSWERED, held — YES, 4 documents ≈5.9 MB.** Re-measured: **76 documents, 59.5 MB,
  3.06 M words, 0 UNANSWERED.** Same verdict, so **the family count does not move**.
- **Earliest form and date actually held: S-1, 2010-01-29** (0001193125-10-017054, `ds1.htm` 2,362,163 B) —
  now the tool's own output, byte-identical to the probe's hand fetch.
- **Earliest form and date merely existing in the index: REGDEX, 2005-02-17** (9999999997-05-006484, `.paper`)
  — never held by either pass. Earliest **company-authored** index row: **S-1 2010-01-29**, which *is* held.
  The gap between the two is **paper SEC index entries, 2005-02-17 → 2009-01-12**, and the next real row after
  them is Form **D 2009-04-09** (also unfetched).
- The probe's "EDGAR empty 2003–2008" line **is superseded in wording** (12 REGDEX rows 2005→2009 exist) and
  **sustained in substance** (2003–2004 truly empty; no company text before the 2009-04-09 Form D / 2010-01-29
  S-1). No 2003–2008 *narrative* was produced by this pass, so §Founder-attribution-question's "one voice, two
  datable layers" conclusion is untouched and now better documented.
- New to family (a) this pass: the **XBRL series, 336 rows with `end` 2008-12-31 → 2012-12-31** — for the first
  time in this batch, `facts` wrote a file. Pre-IPO comparatives (FY2008/FY2009) are now available to §K with
  registrant-authority provenance, which the probe said did not exist.

## Tier

STATUS: WRITTEN 2026-09-27 (regrade pass) — **T3, unchanged, and NOT provisional on missing-query-block grounds.**

Families with in-window Tier-1 text:
- (a) filings — **YES** (76 docs / 59.5 MB, held bytes verified as filings; + the 336-row XBRL series).
- (b) web archives — **UNANSWERED/partial** (probe: one CDX answer with tesla.com captures 2002-11-25 →
  2006-02-09 kept as transcript only; later CDX attempts 504 / "Internet Archive temporarily offline"; **no page
  bytes**). Not re-probed here — this brief is family (a).
- (c) periodical corpora — **metadata-layer answers only, no in-window text read** (probe: IA advancedsearch ×3 →
  6 items all 2015–2018; HathiTrust Cloudflare interstitial; Chronicling America **HTTP 403**; Google Books feed
  post-window). **Not blocked by a missing query block** — `research/_harvest_queries_tesla.json` and
  `..._ca2.json` exist and `tools/queries.json` now parses to **427 tasks across 50 companies with `tesla`
  present**, so my brief's PROVISIONAL condition (a family untried *because of* a missing harvester block)
  **does not apply to this company**.
- (d) corporate print — **metadata only**: title-scoped numFound **2** (`tesla-logo` AR run; `teslaroadster0000maur`
  2008), creator-scoped numFound **0**; **identified, never opened**. One `ia_text.py`/harvest task away from YES.
- (e) documentary — **UNTRIED** (no scripted route in `tools/`; fleet-wide gap, not company-specific).

§15.2 count: **1 family (a)** → **T3 (register tier), 8k words/stage, 3–4 runs — re-issued unchanged**, because
family (a) movement did not add a family. Tesla keeps its §K/§N/§U-analogue obligations, and the probe's
promotion paths are all still open and all one intake task each: (i) tesla.com page bytes when the Archive
answers, (ii) any in-window newspaper text from a non-blocked route, (iii) **opening the two family-(d) items**
— the cheapest, since they are already identified. (iv) New this pass: the 336-row XBRL series means §K can now
be written from **registrant-filed quantitative data** for 2008–2012 instead of prose-only figures.

**Tool notes from this pass (`tools/` not edited):** `auto` fetched 28 accessions out of 269 in-window rows and
reported **0 UNANSWERED**, so "0 UNANSWERED" is not coverage (it is also not a null for the rest); `--max-docs 25`
is not honoured as a document ceiling (76 stored); `facts` succeeds where it wrote nothing for Costco/Nvidia/Dell,
so the `facts` failure on those three is not an absence-of-data result and deserves its own ticket.

