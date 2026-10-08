# A_chronology_feasibility.md — VALERO ENERGY CORP (company_040), Stage-1 PROBE

**Probe agent:** `probe-valero` (claimed with `python tools/scaffold.py claim --path
founders_playbook/01_companies/company_040_valero/research/A_chronology_feasibility.md --agent probe-valero`).
**Tier issued (stated here first so `gates.py --tier auto` can read it): T3 register** for both proposed
Stage-1 sub-windows — exactly **one** corpus family (a) returns in-window Tier-1 text. Full arithmetic in §5.
**Scope:** chronology feasibility only. No volume, no registers, no ids, no certification (§15.1; §13 rows
were not invented for anything below).
**Web budget used: 0 WebSearch / 0 WebFetch.** Every quantifier below is printed beside the command or the
byte that produced it.
**Scripts run:** `sec_intake.py facts` once (§2 F1). **Scripts NOT run, per brief:** `harvest_mine.py`,
`periodical_harvest.py` — the fleet lanes own them tonight. `research/A4_harvest_mine.md` was re-read
immediately before being quoted; its mtime is **2026-09-29 23:53:27 +0530** (`stat -c '%y %n'`), and it is
used only as a pointer to files, never as evidence, per its own banner.

## 0. Measured state at probe start (verified, not inherited)

The fleet record said this company **REFUSED / 0 stored**. That record is now wrong in both halves, and the
correction matters more than the intake numbers: the retry stored **two intakes' worth of bytes**, and the
ledgers describe only the second one.

| item | measured this pass | how |
|---|---|---|
| SEC shelf | **119 files** = 57 `.txt` + 57 `.meta.json` + 5 ledgers (`_RUN.json`, `_MANIFEST.csv`, `_PLAN.csv`, `_SKIPPED.csv`, `_UNANSWERED.csv`). **All 119 carry mtime 2026-10-06**; total `.txt` bytes **9,680,991** | `find … sources/sec -type f`
, python sum of `os.path.getsize` |
| `_RUN.json` | `cik 0001035002`, registrant `VALERO ENERGY CORP/TX`, **`window: "2001-12-31..2020-12-31"`**, max_docs 30, docs_per_filing 4, guard `ok`, attempted 34, stored 30, unanswered 1, skipped 3, identity_ok true, **bytes 2,872,260, words 384,391**, built 2026-10-06T11:45:41Z | `cat sources/sec/_RUN.json` |
| `_MANIFEST.csv` | 30 rows, **every one filingDate 2002-01-10 → 2002-04-15**; forms `SC 13D ×3, 8-K ×11 … 10-K405 ×4, S-3 ×4, DEF 14A ×2`; **0 rows inside the candidate window** | python over the CSV |
| **the discrepancy** | 57 fetched docs, 30 in the manifest ⇒ **27 documents are on disk and NOT in `_MANIFEST.csv`**. Joined to `submissions_CIK0001035002.csv` by accession, those 27 are **filingDate 1997-05-13 → 2001-05-25 — i.e. in-window** (27 docs / 16 accessions / **6,808,731 B / 941,450 words**); the 30 manifest docs (2,872,260 B / 384,391 w) are all **post-2001-12-31**. Both passes were fetched the same minute (meta `fetched` 11:44:28Z–11:45:32Z), so the forward pass **overwrote** `_RUN.json`/`_MANIFEST.csv` of the candidate-window pass | python join of `sec/*.meta.json` → `submissions_CIK0001035002.csv` |
| what the fleet line means now | "30 documents / 2,872,260 B / 384,391 words / 1 UNANSWERED / 3 SKIPPED" is **the forward (recital-route) strip only**. Total stored for this company is **57 docs / 27 accessions / 9,680,991 B / 1,325,841 words**, of which 27 docs are in the candidate window | same |
| `_UNANSWERED.csv` | 1 row: `UNANSWERED NOT-ENUMERATED: 342 in-window filings were never listed because --max-docs 30 was reached`. Its "in-window" is the **2001-12-31..2020-12-31** window; the candidate window has **291** filings indexed and **16 accessions** actually listed here | `cat sources/sec/_UNANSWERED.csv` |
| `_SKIPPED.csv` | 3 rows, all documents of accession `0000950129-02-001907` (8-K, 2002-04-15) `SKIPPED beyond --max-docs 30` | `cat sources/sec/_SKIPPED.csv` |
| EDGAR index | **2,272 filings enumerated**, 0 rows dropped for no accession, 159 rows without `primaryDocument`; `source` column = `CIK0001035002-submissions-001.json` ×1,271 + `recent` ×1,001 ⇒ the walk is **not slice-capped** (RD-134 fix confirmed live); `_INDEX.md` "UNANSWERED slices: (none)" | python over `submissions_CIK0001035002.csv` |
| **measured date perimeter** | **1997-05-13 → 2026-09-21**; 30 distinct filing years, earliest 1997; **filings dated 1979/1980/1981/1984/1993/1994/1995/1996 = 0 each** (measured per year, not inferred). This is the CIK's own perimeter, not EDGAR's floor | same |
| registrant identity | CIK `0001035002`, `VALERO ENERGY CORP/TX`, ticker `VLO`, **`former_names: ["VALERO REFINING & MARKETING CO"]`**, guard `ok` ("slug token ['valero'] match registrant") — the RD-135 guard fix is what let this run at all | `_index/_registrant_CIK0001035002.json` |
| other shelves | `sources/corporate_print/` = **0 files**; `sources/periodicals/` = 2 documents (+2 meta); `sources/harvest_mine/_index.json` window `["1979-01-01","2001-12-31"]`, candidates 2, mined 2, untried_by_limit 0; `_parts/` empty | `find … -type f` per dir |
| duplicate control (hard rule 4) | `submissions.csv` and `submissions_CIK0001035002.csv` are **byte-identical** (md5 `f98aebc6bd9dbc5e…`); `_INDEX.md` ≡ `_INDEX_CIK0001035002.md` (md5 `f651cf24340ec8c9…`) ⇒ **one document, two shelves, never two corroborations**. Among the 57 stored SEC texts: **0 byte-identical duplicate groups** | `md5sum`, python md5 over all |
| headers enumerated first (hard rule 3) | `sources/_index/submissions*.csv` = `filingDate, form, accession, reportDate, primaryDocument, source`. `sources/sec/_MANIFEST.csv` = `rank, slot, cik, accession, file, path, bytes, words, status, form, filingDate, url, why, listing`. `00_universe/harvest/candidates.csv` = `company, source_family, query, item_id, title, date_or_issue, url, snippet_or_hitcount, http_status, classification, retrieved_at`. `tools/queries.json` task keys = `company, source_family, kind, query_label, _note, params`. Universe header = `rank, company, revenue_usd_millions, revenue_fiscal_year, profit_usd_millions, hq_city, hq_state, fortune_industry, universe_source_url, verified_by_second_source, confidence, notes` — **no founding-date column**, so every window below is mine, and PROPOSED | python `csv.DictReader` keys |
| universe row | rank 40, `Valero Energy`, San Antonio TX; no date field to inherit | same |

STATUS: WRITTEN

## 1. The identity question first, because every tier below depends on it

The brief's trap is real, and the held bytes decide it — but the sequence in the brief is **not** what the
record supports, so I am recording the record. Five distinct legal persons are in play, and the name `Valero`
crosses four of them.

**C1 — the registrant's own incorporation recital, repeated in four of its own filings.**
`sources/sec/0000950134-00-001705_0000950134-00-001705.txt` (10-K405 for FY1999, filed 2000-03-08) **l.294-298**
and again **l.2904-2915**:

> "(1) Valero was incorporated in Delaware in 1981 under the name Valero Refining and Marketing Company as a
> wholly owned subsidiary of Valero Energy Corporation, referred to as Old Valero. … On July 31, 1997, Old Valero
> spun off Valero to Old Valero's stockholders … Upon completion of the Restructuring, the Company's name was
> changed from Valero Refining and Marketing Company to Valero Energy Corporation."

Same sentence, same lineage, in: FY2001 10-K405 `0001035704-02-000158_d94896e10-k405.txt` **l.222-232**
("…as a wholly owned subsidiary of a corporation then known as Valero Energy Corporation, and referred to in
this report as Old Valero"); FY2000 10-K405 `0000950134-01-001719_d84423e10-k405.txt` **l.222**, **l.2988**;
DEF 14A 2001-03-28 `0000950134-01-002726_d84423ddef14a.txt` **l.252**; S-3 2002-03-22
`0000950129-02-001437_h94967s-3.txt` **l.361-364** ("We were incorporated in Delaware in 1981 as Valero Refining
and Marketing Company, a wholly owned subsidiary of our predecessor company. On July 31, 1997, our stock was
distributed, or spun off, … and we changed our name to Valero Energy Corporation"); and, in the registrant's
own first filing, S-1 1997-05-13 `0000950130-97-002339_0000950130-97-002339.txt` **l.3452** ("New Valero was
incorporated in Delaware in 1981").

**C2 — an independent third party prints the same 1997 facts.** Salomon Inc's Schedule 13D, filed **1997-08-11**
under accession `0000903423-97-000135` (**not** a Valero lineage): **l.376-391** — distribution "to the holders
of record as of July 31, 1997 of common stock … of Valero Energy Corporation ('Old Valero')"; "the Issuer,
which had been a wholly owned subsidiary of Old Valero, became a publicly held corporation"; "the Merger closed
on July 31, 1997. The Issuer thereafter changed its name from Valero Refining and Marketing Company to Valero
Energy Corporation." This is the only non-corporate-record Tier-1 carrier on this disk, and it corroborates the
**1997** leg, not the 1981 leg.

**C3 — the acquisition that brought the refining scale (bought, not built).** S-3 2002 l.**334-341**: "Effective
December 31, 2001, we acquired Ultramar Diamond Shamrock Corporation, or UDS. … we issued 45.9 million shares …
paid $2.1 billion of cash … assumed approximately $2 billion of UDS debt." Agreement and Plan of Merger,
`0000898822-01-500188_mergeragreement.txt` **l.137-139**: "dated as of **May 6, 2001** … by and between VALERO
ENERGY CORPORATION, a Delaware corporation ('Valero') and ULTRAMAR DIAMOND SHAMROCK CORPORATION, a Delaware
corporation ('UDS')". Closing 8-K `0000898822-02-000035_form8k-jan11.txt` **l.51** ("Effective December 31,
2001, Ultramar Diamond Shamrock Corporation, a …") and its exhibit 99-2 **l.39**: "various brand names including
the Diamond Shamrock, Ultramar, **Valero**, Beacon and Total". The acquired company carried brands; the
registrant already carried the name.

**C4 — a second purchase inside the origin window.** The 1997 S-1 **l.542 / l.1409 / l.3659**: "On April 22,
1997, Valero entered into a stock purchase agreement with Salomon…" to acquire **Basis Petroleum, Inc.**, and
**l.8595-8597**: "Basis Petroleum, Inc. (the Company), with headquarters in Houston, Texas … changed its name
from **Phibro Energy USA, Inc.**". Basis's business was contributed to the registrant at the spin-off (S-1
l.391, l.22561). So even the registrant's 1997 "starting" asset base is an acquired one with its own predecessor
name and its own litigation history (S-1 l.3987 `Friends of the Earth, Inc. v. Phibro Energy USA, Inc.`).

**What the record does NOT carry, measured across all 57 stored SEC texts** (python regex
`(?<!\d)TERM(?!\d)` over `sources/sec/*.txt`):

| term | occurrences | what the hits actually are |
|---|---|---|
| `Dealey` | **0** (0 files) | — |
| `Murchison` | **0** (0 files) | — |
| `lobby` / `Lobbying` | **0** / **0** | — |
| `Shamrock Oil` | **0** | the ancestor of the Diamond Shamrock name is absent |
| `Spanish` | **1** — S-1, MTBE joint venture: "Dragados y Construcciones, S.A., a **Spanish** construction company" | a decoy, not an etymology |
| `Mission` (capitalised) | **0**; lower-case `mission` = 647, all of them substrings of `submission`/`commission`/`permission` | substring artefact, not evidence |
| `1979` | 43 across 12 files | officer/director tenure rows and statutes: S-1 l.22564-area "Mr. Greehey has served as Chief Executive Officer and as a director of Valero **since 1979**"; FY2000 10-K405 l.427-area "MR. GREEHEY served as Chief Executive Officer and a director of **Old Valero** from 1979"; "Natural Gas Pipeline Safety Act of 1979" |
| `1975` | 4 across 4 files | S-1: an officer "in various other capacities with Valero since 1975"; 8-K `0001035002-98-000016`: bonds "issued in 1975 and 1978" |
| `1984` | 11 across 4 files | **the plant, not the company**: S-1 **l.3410** and **l.3839** "The Refinery was completed in 1984 under more stringent environmental requirements…"; FY1997 10-K `0001035002-98-000002_0001035002-98-000002.txt` **l.873**; plus director-tenure columns |
| `1981` | 36 across 14 files | the incorporation recitals above, plus unrelated tenure/statute uses |
| `Deepwater` / `Horizon` / `RFCC` / `Resid Fluid Catalytic` | **0 / 0 / 0 / 0** | nothing post-boundary is on this disk to contaminate Stage 1 |

**Verdict on identity.** The registrant of record is **CIK 0001035002, incorporated in Delaware in 1981 as
Valero Refining and Marketing Company**. It carries I.R.S. Employer ID `74-1828067` in both the 1997 S-1 header
(`COMPANY CONFORMED NAME: VALERO REFINING & MARKETING CO`, `STATE OF INCORPORATION: DE`) and the FY2001 10-K
cover (`0001035704-02-000158_d94896e10-k405.txt` **l.29-37**: `VALERO ENERGY CORPORATION / DELAWARE /
74-1828067`) — one continuous taxpayer and CIK from 1997 to today, whose EDGAR conformed name is now
`VALERO ENERGY CORP/TX` with `VALERO REFINING & MARKETING CO` as its only listed former name. **"1979", "1980" and "1984" describe other things**: 1979 = a person's start year at the
*predecessor parent* (Old Valero); 1984 = the Corpus Christi refinery's **completion date**; and Old Valero
itself — the parent that merged into a PG&E subsidiary on 1997-07-31 — is **not this registrant and has no CIK
on this disk**. The brief's "holding/lobbying vehicle for a Texas oil family" leg has **zero carriers here**,
so I do not claim it (see §9).

STATUS: WRITTEN

## 2. Family (a) SEC/EDGAR — **TRIED–ANSWERED**, and it answers twice over: once in-window, once as recital

**What landed, stated as a measurement rather than as a summary.** 57 documents / 27 accessions on the shelf.
Split by `filingDate` joined from the registrant index:

| strip | accessions | documents | bytes | words | inside candidate window? |
|---|---|---|---|---|---|
| **1997-05-13 → 2001-05-25** (the candidate-window pass) | 16 | **27** | **6,808,731** | **941,450** | **YES — 27 of 27** |
| 2002-01-10 → 2002-04-15 (the forward/recital pass, = `_RUN.json`) | 11 | 30 | 2,872,260 | 384,391 | no, all post-2001-12-31 |

The in-window 16 accessions, by form (`filingDate` = filed date, from `submissions_CIK0001035002.csv`):
`S-1` 1997-05-13 · `SC 13D` 1997-08-11 (Salomon Inc, third party) · `10-K` 1998-03-02 · `DEF 14A` 1998-03-20 ·
`S-3` 1998-06-11 · `SC 13G/A` 1998-08-10 · `8-K` 1998-09-30 · `10-K` 1999-02-26 · `10-K405` 2000-03-08 ·
`8-K` 2000-05-30 · `8-K` 2000-06-30 (+3 exhibits) · `SC 13G/A` 2000-10-10 · `10-K405` 2001-02-23 (+3 exhibits) ·
`DEF 14A` 2001-03-28 · `8-K` 2001-05-10 (merger agreement +2) · `S-4` 2001-05-25 (+2 exhibits; `d87697s-4.txt`
is 640,443 B / 90,953 words).

**Lineage discipline (§3).** Those 16 accessions are **not 16 sources** for the origin question: the 1997 S-1,
the four annual-report recitals, the 2001 DEF 14A, the 2002 S-3 and the S-4 are **one corporate record
re-described** — the registrant repeating its own 1981 sentence filing after filing. Independence, measured on
this disk, exists only for (i) the **1997-07-31 spin-off/rename** leg, which the Salomon Inc 13D (C2) prints
from an unrelated holder's position, and (ii) nothing else: the merger counterparty's own filings are absent
(all 57 stored URLs are under `Archives/edgar/data/0001035002/…`, and no UDS or Old Valero accession was
enumerated at all). So the 1981 incorporation date rests on **one self-filing lineage** and is capped at Medium
under §3 until a Delaware charter file or an unrelated 1981-82 record repeats it.

**F1 — XBRL, run this pass.** `python tools/sec_intake.py facts "VALERO ENERGY CORP/TX" --company-dir
founders_playbook/01_companies/company_040_valero --from 1979-01-01 --to 2001-12-31` printed:

> `facts: NULL -- NO DATA FILE WRITTEN. WINDOW: 0 of 27,123 observations in this registrant's companyfacts fall
> in 1979-01-01..2001-12-31. Observed XBRL coverage runs 2006-12-31..2026-07-24, and 703 tags are present, so
> the absence is EDGAR's XBRL start date (~2007 for this filer), not a fetch failure and not the allow-list.
> Early-window money figures must come from the filings themselves.`

Report artefact added (nothing removed): `sources/financials/xbrl_early_series_CIK0001035002_1979-01-01_2001-12-31_NULL.NULL.md`.
**Consequence:** XBRL cannot arbitrate anything inside Stage 1 — this is a measured null, not a refusal, and the
2006-12-31 floor sits five years after my proposed stage boundary.

**What family (a) structurally cannot answer.** The CIK's own perimeter starts **1997-05-13** (§0), so the
1981→1996 leg of the registrant's own life is reachable **only as a recital inside a post-1997 filing** — which
is exactly what C1 is, and exactly the pattern RD-134 turned into a rule from Ford's 1919/1903 recital and
Citigroup's empty walk. It also cannot reach **Old Valero** at all: the parent's filings sit under another CIK
this disk never enumerated (FR-2), and nothing on this shelf prints Old Valero's incorporation year, its state,
or who controlled it.

STATUS: WRITTEN

## 3. Families (b), (c), (d), (e) — three states, and only one of them is a null

**(b) Web archives — UNTRIED.** 0 attempts, 0 calls. No `sources/web_archive/` shelf exists (the tree is `sec`,
`periodicals`, `corporate_print`, `harvest_mine`, `_index`, `financials` — the last created by my own `facts`
run). **Not a null.** The company's own "History" pages of the 2000s are exactly what an archived-web crawl
would hold, and they are a **different lineage** from the filings: a self-told origin story is where a "founded
1975/1979/1983" claim would appear, so this untried family is the one most likely to *contradict* the 1981
recital rather than repeat it. Remedy FR-4.

**(c) Periodical corpora — TRIED; split verdict.** I did not run `harvest_mine.py` or `periodical_harvest.py`
(brief). I read the artefacts they left, plus the fleet index.
- `research/A4_harvest_mine.md` (mtime **2026-09-29 23:53:27 +0530**): window 1979-01-01..2001-12-31, 2
  candidates, 2 mined, 0 untried at the limit; **`TIER1_CANDIDATE_TEXT` 0, `VARIANT_TERM_HIT` 0,
  `BARE_WORD_MATCH` 2, NULL 0, UNANSWERED 0**. Entity vocabulary it applied: name phrases `formerly known as
  valero`, `valero energy`, `valero energy corporation`; other quoted term `diamond shamrock`. Quoted as a
  pointer only, never as a finding, per its own banner.
- The 2 held periodicals — `sources/periodicals/ANA-DIG-THENEWSARUBA-D0046-01-20050903-DOC_djvu.txt` (3,175 B)
  and `…D0216-05-20051104-DOC_djvu.txt` (1,993 B); meta `fetched` 2026-09-29T18:23Z, route
  `download/<id>/<id>_djvu.txt (OCR text layer)`, **transport `UNVERIFIED TLS -- re-check before citing at High
  confidence`** — are *The News (Aruba)* items dated **2005-09-03** and **2005-11-04**, `in_window: false` in
  `sources/harvest_mine/_index.json`, both about "Valero Refinery Aruba", both **(PB)**. Charity-golf and hiring
  notices; no origin content.
- The fleet index `founders_playbook/00_universe/harvest/candidates.csv` now holds **28 rows** for
  `company == "valero"` (4,706 rows total — **the index has grown far past the 1,562 rows the mine saw**, so the
  mine's "2 candidates" is stale by design and not a census, per RD-135): 18 `internet_archive`, 4
  `chronicling_america`, 4 `corporate_print`, 1 `google_books`, 1 `hathitrust`; classifications `LEAD_ONLY` 11,
  `UNANSWERED` 8, `TIER1_CANDIDATE` 4, `NULL` 3, `ERROR` 2.
  - The 4 `TIER1_CANDIDATE` rows are the **same 2 Aruba documents counted twice** (the faceted query
    `IA Valero + predecessor periodical text 1960-2005` and its `[FACET-FREE per RD-130]` re-run): one document,
    not four, and the pass that actually read their bytes graded them `BARE_WORD_MATCH` with **0 entity hits**.
    The label is a query-text echo (hard rule 6 / RD-124), so I count **zero** periodical namings of this
    registrant.
  - `internet_archive` task "IA petroleum trade-journal sweep 1960-2010"
    (`title:("Oil & Gas Journal") OR title:("Petroleum Refiner") OR title:("Hydrocarbon Processing") AND Valero`)
    → **`EMPTY (proven null): numFound=0`**, measured twice (2026-09-29T13:09:40Z and T19:13:27Z). That is the
    single best trade-press route for a 1981-2001 refiner and it is a real zero **on those params**.
  - 7 `LEAD_ONLY` `internet_archive` rows are **federal court files, not periodicals**:
    `gov.uscourts.cacd.793552` *Ultramar, Inc. dba Valero Wilmington Refinery v. Old Republic Insurance*,
    `gov.uscourts.laed.135477` *Victorian v. Valero St. Charles Refinery*, `gov.uscourts.tnwd.97261`
    *Jones v. Valero Memphis Refinery*, `gov.uscourts.oked.17485` and `gov.uscourts.txnd.248740`
    *… v. Valero Ardmore Refinery*, `gov.uscourts.cand.173961` *Diaz v. Valero Oil Refinery, Brock Scaffolding*,
    `gov.uscourts.laed.144436` (untitled). **No bytes on this disk, no dates in the index rows, and every
    caption names a refinery of the acquired post-2001 footprint** — (PB) leads about the purchase, not the
    origin. They are also, note, the only place on this shelf where "Ultramar, Inc. dba Valero" appears as an
    entity: the brand was a *dba*, which is exactly the confusion trap 1 warns about.
  - `chronicling_america` (4 rows): 2 × `UNANSWERED` `SKIPPED: hard stop: 5 consecutive failures`
    (2026-09-26T09:45:25Z), 2 × `ERROR` (2026-09-29T13:09:36/38Z). `hathitrust` 1 × `UNANSWERED` (hard stop),
    `google_books` 1 × `UNANSWERED` (`SKIPPED: global max-requests cap 600 reached`). **Tool-level refusals all:
    no CA / HathiTrust / Google Books zero may be cited as a null for this company.**
  Verdict: **(c) TRIED** — it answered with one trade-journal param-null and two out-of-window 2005 items, and
  it left CA/Hathi/GB **UNANSWERED** (remedies: FR-3 and the fleet's own `00_universe/harvest/_CA_ENDPOINT_TEST.md`).
  A `valero` query block **exists** (8 tasks in `tools/queries.json`: CA 2, IA 2, Hathi 1, GB 1, corporate print
  2), so under RD-112's Costco/Nvidia distinction family (c) is **not provisional as a try** — only as an answer.

**(d) Digitised corporate print — TRIED–UNANSWERED; an empty shelf is not an empty archive.**
`sources/corporate_print/` holds **0 files**. The 4 `corporate_print` rows in the fleet index are: 2 ×
`UNANSWERED` `numFound=0 WITH the YEAR facet` (2026-09-29T19:13:28Z / T19:13:30Z — RD-130: a faceted zero is a
statement about our parameter); 1 × `NULL` `EMPTY (proven null): numFound=0 FOR THESE EXACT PARAMS ONLY —
per-param, never per-corpus; the family stays open…` (facet-free creator query, **2026-10-06T12:03:15Z**, the
one genuine zero); and 1 × `LEAD_ONLY` *Valero Benicia Exceedance Investigation Report* (2019-09-04,
DocumentCloud) = **(PB)**. Both `valero` corporate-print tasks in `tools/queries.json` carry
`year_range: [1960, 2005]`. **Verdict: TRIED–UNANSWERED at family level** — one param-proven null does not close
the family that has flipped tiers repeatedly in this project (RD-130: Walmart, Target, Boeing, Kroger), and a
1997-2001 Valero annual report or a Diamond Shamrock house organ is precisely what would live there.

STATUS: WRITTEN

## 4. The window I was handed, the window I propose, and what each bound rests on

**Where the candidate window comes from — measured, not assumed.** `tools/harvest_mine.py` **line 68** reads:
`"valero": ("1979-01-01", "2001-12-31")`. That is the whole of its provenance: a **harvester parameter**, echoed
into `sources/harvest_mine/_index.json` → `"window": ["1979-01-01", "2001-12-31"]` and into the header line of
`A4_harvest_mine.md`. `00_universe/fortune_top_50_2026.csv` has no founding-date column (§0). So the window is a
search setting, and RD-112 says it is evidence for nothing.

**What I did with it: I narrowed the START by 2 years on the registrant's own filing, kept the END, and split
the span in two.**

| window | bound | the carrier that fixes it |
|---|---|---|
| 1979-01-01 → 1980-12-31 | **DROPPED from Stage 1** | No carrier of any kind on this disk puts this registrant in existence before **1981** (C1: four filings print "incorporated in Delaware in 1981"; the term `1979` appears 43× and every hit is a tenure row, a statute or a bond year — §1). EDGAR cannot correct the silence: **0 filings dated 1979/1980 for CIK 1035002** (§0). Anything true of 1979-80 belongs to **Old Valero**, a different legal person with no CIK on this disk. |
| **1981-01-01 → 1997-07-31** | **PROPOSED Stage 1-A** "subsidiary years" | Start = C1's incorporation recital. End = the **1997-07-31** distribution date, printed by the registrant (C1) **and by an unrelated third party** (C2, Salomon 13D l.376-391: "holders of record as of July 31, 1997 … The Merger closed on July 31, 1997"). Inside it the registrant was a **wholly owned subsidiary that could not file at all** — its first own accession is the S-1 of 1997-05-13, 5 weeks before the boundary. |
| **1997-07-31 → 2001-12-30** | **PROPOSED Stage 1-B** "independent public company, before the purchase" | Start = the spin-off. End = the day before **UDS** closes (C3: "Effective December 31, 2001, we acquired Ultramar Diamond Shamrock Corporation"). This is the only stretch where the company in the filings is the company in the Fortune row **and** still owns its own history. 258 of the 291 in-window indexed filings fall here (§0). |
| 2001-12-31 | **STAGE BOUNDARY, not a stage of its own** | The UDS acquisition is a **purchase of an operating history** — 11 U.S. refineries + 1 Canadian, ~1.9 MBD, 4,500 retail sites, five brands (C3/S-3 l.334-350). A stage that begins with a bought asset base is Stage 2, and its evidence is UDS's lineage, not this registrant's 1981 recital. |
| 2002-01-01 → | **(PB)** post-boundary | Includes the whole forward intake strip, the `1.9 million barrels per day` figure, the Aruba items, and every court caption in §3. |
| *ancestor lineages — NOT stages of this company* | Old Valero (Texas parent, merged into a PG&E subsidiary 1997-07-31) · UDS / Diamond Shamrock / Ultramar (acquired 2001-12-31) · Basis Petroleum ← Phibro Energy USA (acquired 1997-04-22) | Each named so no later volume can drag one of their dates into this registrant's chronology. Their records are **not on this disk**; FR-2 and FR-5 are the only routes I found to them. |

**A claim I am not making:** that 1979-1980 is empty *in fact*. It is empty **in this corpus**; the family that
could speak for it (Old Valero's own EDGAR record, 1980s-1997, and Texas corporate-registry papers) is
**UNTRIED**, which is exactly why the narrowing above moves the start to the earliest date the *registrant's own
charter sentence* supports and leaves 1979-80 as a predecessor question, not a null.

STATUS: WRITTEN

## 5. Per-stage tiers (RD-112: a tier is measured against that stage's own window)

| stage | PROPOSED window | families returning in-window **Tier-1 text** | tier | §15.2 deliverable |
|---|---|---|---|---|
| **1-A subsidiary years** | 1981-01-01 → 1997-07-31 | **(a) only** — 1 accession in-window (S-1 1997-05-13, 1.90 MB, 262,752 words) plus the recital it carries. (b)(e) UNTRIED; (c) answered 0 in-window namings; (d) UNANSWERED | **T3 register** | short narrative + registers; §K, §N, §U still mandatory; 8k w/stage cap; 3-4 runs |
| **1-B independent, pre-purchase** | 1997-07-31 → 2001-12-30 | **(a) only** — 15 of the 16 in-window accessions, 6.81 MB / 941,450 words of filed text: annual reports 1998/1999/2000/2001, S-3 1998, S-4 2001, proxies, 8-Ks, the merger agreement, plus 1 third-party 13D | **T3 register** (not provisional: the answer is bytes, not a tool ceiling) | same cap; the *densest* T3 I could imagine, see the note below |
| *(stage 2, flagged only)* | 2001-12-31 → | (a) indexed + the 30-doc forward strip already on disk | **not graded** — out of this probe's contract | — |

**Tier arithmetic, stated plainly.** For each proposed Stage-1 window exactly **one** family returns in-window
Tier-1 text ⇒ ≤1 ⇒ **T3** by §15.2. No family is provisional-as-a-try (a `valero` query block exists, 8 tasks)
and none is counted that shouldn't be: the two 2005 Aruba items are out-of-window and only `BARE_WORD_MATCH`, and
the 4 `TIER1_CANDIDATE` index labels are two documents echoing their own query (§3).

**The uncomfortable half, which RD-112 told me to expect.** Stage 1-B is close to the best-documented origin in
the fleet — incorporation state and year, original name, parent, spin-off date and mechanics, rename, first
asset base, first refinery's completion year and nameplate, four years of filed throughput, and the terms of the
purchase that ended the stage — **and it is still T3**, because *tier measures family breadth, not doubt*. A
downgrade of tier here must not be read as a licence to write less: §15.2 keeps §K, §N and §U mandatory at T3,
and for this company those three sections are where the real difficulty sits (money in 1981-96 is a recital
question, the decision set belongs to Old Valero's board, and the conflicts are all name-vs-person conflicts).
**Provisional markers:** Stage 1-A's T3 is *provisional upward* only, never downward: if (d) or (b) returns
in-window text (FR-1, FR-4) it becomes T2 core with no new SEC work at all.

STATUS: WRITTEN

## 6. Petroleum-vocabulary audit (trap 3) — every capacity/throughput figure, classified

The screen I applied: a figure may be published only if (i) the **entity name or a defined term traceable to
this registrant** is adjacent in the same sentence, and (ii) I can say whether it is **nameplate**, an
**acquired** capacity, a **filed actual**, or somebody else's capacity appearing in a Valero risk factor.
Regex used for the sweep: `[^.]{0,120}(nameplate|throughput|capacity|barrels per day|bbls?/d)[^.]{0,120}`
across the five in-window texts listed below plus the 2002 S-3 (whose figures are all (PB)), then each hit read
in the bytes. Files swept: `0000950130-97-002339_…txt`, `0001035002-98-000002_…txt`,
`0000950134-00-001705_…txt`, `0000950134-01-001719_d84423e10-k405.txt`, `0000950134-01-502495_d87697s-4.txt`. Re-measured with the raw regex
(no adjacency filter) the S-4 gives **14 matches, of which exactly 1** carries `Valero` + a digit —
`0000950134-01-502495_d87697s-4.txt` **l.5404**: "Valero owns and operates six refineries in Texas, California,
Louisiana and New Jersey with a combined throughput capacity of approximately 1,000,000 barrels per day, or BPD
(723,000 BPD of crude capa…)" — the same sentence as C5, reprinted in the UDS prospectus. The other 13 hits are
UDS-side or contractual boilerplate. For scale, that prospectus prints `Valero` 1,561× and `UDS` 1,756×: it is
half one company and half the other, which is the whole reason trap 3 exists.

| figure | carrier (file + line) | entity adjacency | class | usable for Stage 1? |
|---|---|---|---|---|
| **171,500 barrels per day** | `0000950130-97-002339_…txt` **l.3482-3483** "The Refinery can produce approximately 171,500 barrels per day of refined products, with gasoline … approximately 85%" | "The Refinery" is defined two lines earlier as **the Corpus Christi refinery owned by New Valero** (l.3452-3453) | **nameplate / "can produce"** — not an actual | **YES, in-window**, labelled nameplate, and only for Stage 1-A's asset base |
| **Refinery completed in 1984** | S-1 **l.3410**, **l.3839**; FY1997 10-K `0001035002-98-000002_…txt` **l.873** "Because the Corpus Christi Refinery was completed in 1984" | same | plant date, not a corporate date | **YES** as an asset fact; **NO** as an origin (see U-1) |
| **392 / 170 / 160 MBD** | FY1997 10-K **l.562** "Refinery Throughput Volumes (MBD) 392 ⟨F2⟩ 170 160" | the registrant's own selected-data table | **filed actuals**, three years, but the column mapping needs the table header and the `<F2>` footnote (a mid-table line; do not cite a bare number) | **YES with care** — read the header row before publishing which year is which |
| **640 MBPD / 543 MBPD** | FY1999 10-K405 `0000950134-00-001705_…txt` **l.715**, **l.719** "…refinery throughput volumes and sales volumes were 640 MBPD and…" | registrant's MD&A | **filed actual** | **YES** (PB-adjacent: FY1999/FY1998 periods, inside Stage 1-B) |
| **+8,000 BPD, +20,000 BPD** | FY2000 10-K405 `0000950134-01-001719_d84423e10-k405.txt` **l.427-433** "In 2000, Valero increased net refinery throughput capacity by approximately 8,000 BPD by expanding the refinery's hydrotreating unit and FCC Unit… in early February 2001 … to increase net refinery throughput capacity by approximately 20,000 BPD" | "Valero", the named unit, the named refinery paragraph | **capacity increments** (net), i.e. derived from capital work, not nameplate | **YES**; the Feb-2001 increment is in-window, and note it is *net* |
| **~1,000,000 BPD combined, of which 723,000 BPD crude** | FY2000 10-K405 **l.208-210** "Valero owns and operates six refineries in Texas, California, Louisiana and New Jersey with a combined throughput capacity of approximately 1,000,000 barrels per day, or BPD (723,000 BPD of crude capacity)"; restated **l.343-346** "as of December 31, 2000"; **and in the 2001 UDS prospectus** `0000950134-01-502495_d87697s-4.txt` **l.5404** | "Valero owns and operates" | **nameplate aggregate, as of a date, gross AND net printed together** | **YES — this is the Stage 1-B ceiling figure**, and the crude-vs-total split is the gross/net trap (§6 of the method: numerals carry their basis): never publish 1,000,000 without the 723,000 |
| **up to 200,000 BPD, Good Hope, Louisiana** | FY1997 10-K **l.671-673** "The Company is **aware, for example, of** additional capacity of up to 200,000 BPD from a refinery in Good Hope, Louisiana which may become operational as early as late 1998" | the adjacency is to *industry economics*, not to Valero's assets | **a competitor's capacity inside Valero's risk factor** | **REFUSED** — this is the exact decoy the brief predicted; publishing it as Valero capacity would inflate the registrant's 1997 footprint by more than its own single refinery |
| **~1.9 million barrels per day, eleven U.S. + one Canadian refinery** | S-3 2002 `0000950129-02-001437_h94967s-3.txt` **l.337-341** "As of January 1, 2002, we owned and operated eleven refineries in the United States and one refinery in Canada with a combined throughput capacity of approximately 1.9 million barrels per day. **This excludes the Golden Eagle Refinery acquired from UDS**…" | "we", but the assets arrive with UDS | **acquired nameplate aggregate**, dated the day after the boundary, and explicitly excludes an asset sold to satisfy the FTC | **(PB)** — Stage 2 at best, and never a Stage 1-B figure |
| **4,500 retail sites; brands Diamond Shamrock, Ultramar, Valero, Beacon, Total** | S-3 2002 **l.349-350**; also 8-K exhibit `0000898822-02-000035_exhibit99-2.txt` **l.39** | registrant's own words about the **acquired** network | acquired footprint | **(PB)**, and it is the line that proves the name was already a brand of the acquired business — cite it only against U-2 |
| **"73 percent of Valero L.P. … crude oil pipelines"** | S-3 2002 **l.355-359** | registrant | post-boundary consolidation of a bought MLP | **(PB)** |

STATUS: WRITTEN

## 7. Post-boundary ledger — what must not enter Stage 1, and what is already absent

Named in the brief, measured on this disk (counts over all 57 stored SEC texts, §1's table):
`Deepwater` **0**, `Horizon` **0**, `RFCC` **0**, `Resid Fluid Catalytic` **0**, `British Petroleum` **0**.
So the 2010 Deepwater Horizon liability and the RFCC-unit fires have **no carrier here and are (PB) regardless**
— they belong to the acquired UDS/Gulf-of-Mexico lineage and to years after the boundary, and I record them as
**out of Stage 1 on date alone**, not as disproved. Two adjacent cautions for whoever writes Stage 2:
1. The captions in §3 (`Ultramar, Inc. dba Valero Wilmington Refinery`, `Valero St. Charles`, `Valero Memphis`,
   `Valero Ardmore`) are **all acquired-asset names**; a Stage-2 agent that mines them will be writing the
   history of other companies' workers and insurers under this slug.
2. `Benicia` occurs 195× and `Texas City` 150× in the **in-window** bytes (the registrant's own refineries from
   the 1999-2000 expansion era), so in-window incidents at those sites are findable — but a *Valero-era*
   incident there is not the same as an incident at a facility acquired in 2001, and each hit must be read for
   which entity owned it in which year.

STATUS: WRITTEN

## 8. Carriers index (file + line) for the origin / predecessor question

All paths are relative to `founders_playbook/01_companies/company_040_valero/sources/sec/`. Tier 1 throughout.

| # | carrier | file + line | what it settles | lineage |
|---|---|---|---|---|
| C1a | S-1, filed 1997-05-13 | `0000950130-97-002339_0000950130-97-002339.txt` **l.3452** | "New Valero was incorporated in Delaware in 1981" | registrant (first own accession) |
| C1b | 10-K405 FY1999, 2000-03-08 | `0000950134-00-001705_0000950134-00-001705.txt` **l.294-298**, **l.2904-2915** | 1981 incorporation + original name + parent + 1997-07-31 spin + rename | registrant |
| C1c | 10-K405 FY2000, 2001-02-23 | `0000950134-01-001719_d84423e10-k405.txt` **l.222**, **l.2988** | same recital, one year later | registrant |
| C1d | 10-K405 FY2001, 2002-03-14 | `0001035704-02-000158_d94896e10-k405.txt` **l.222-232**; cover **l.29-37** | same recital + `VALERO ENERGY CORPORATION / DELAWARE / 74-1828067` | registrant |
| C1e | DEF 14A 2001-03-28 | `0000950134-01-002726_d84423ddef14a.txt` **l.252** | same recital in a proxy | registrant |
| C1f | S-3 2002-03-22 | `0000950129-02-001437_h94967s-3.txt` **l.361-366** | 1981 + spin + rename + "spun off by our predecessor company" | registrant |
| C2 | Salomon Inc SC 13D, 1997-08-11 | `0000903423-97-000135_0000903423-97-000135.txt` **l.243**, **l.376-396** | spin-off record date, "wholly owned subsidiary … became a publicly held corporation", rename, 1-to-1 share exchange | **third party — the only independent origin carrier on disk** |
| C3a | Agreement and Plan of Merger, 8-K filed 2001-05-10 | `0000898822-01-500188_mergeragreement.txt` **l.137-139** | "dated as of May 6, 2001 … Valero … and ULTRAMAR DIAMOND SHAMROCK CORPORATION, a Delaware corporation" | registrant + UDS instrument |
| C3b | closing 8-K filed 2002-01-11 | `0000898822-02-000035_form8k-jan11.txt` **l.51**, **l.118**, **l.170** | "Effective December 31, 2001, Ultramar Diamond Shamrock Corporation…" | registrant |
| C3c | S-3 2002 business description | `…h94967s-3.txt` **l.334-350** | UDS acquired, consideration, 1.9 MBD (PB), brands (PB) | registrant |
| C4 | 1997 S-1, Basis/Phibro | `0000950130-97-002339_…txt` **l.542**, **l.1409**, **l.3659**, **l.8595-8597**, **l.3987** | April 22 1997 stock purchase agreement; Basis = renamed Phibro Energy USA; Phibro litigation | registrant (about a third party) |
| C5 | FY2000 10-K405 | `0000950134-01-001719_d84423e10-k405.txt` **l.206-213**, **l.343-346**, **l.427-433** | six refineries, 1,000,000 BPD total / 723,000 BPD crude, +8,000 / +20,000 BPD increments | registrant |
| C6 | FY1997 10-K | `0001035002-98-000002_0001035002-98-000002.txt` **l.562**, **l.671-673**, **l.3410** area | filed throughput actuals; the Good Hope competitor-capacity decoy | registrant |
| C7 | 1997 S-1 header | same file, l.1-40 region (`COMPANY CONFORMED NAME: VALERO REFINING & MARKETING CO`, `CENTRAL INDEX KEY: 0001035002`, `STATE OF INCORPORATION: DE`, `IRS NUMBER: 741828067`, address `530 MCCULLOUGH AVENUE, SAN ANTONIO`) | who the 1997 registrant was, in EDGAR's own header | registrant |

**Negative carriers (nothing found, measured):** `Dealey` 0 · `Murchison` 0 · `lobby`/`Lobbying` 0 ·
`Shamrock Oil` 0 · capitalised `Mission` 0 · `Deepwater`/`Horizon`/`RFCC` 0 — each over all 57 files (§1, §7).

STATUS: WRITTEN

## 9. What this probe refuses to claim, and why

**U-1 — "Valero was founded in 1979 / 1980 / 1984."** Refused. 1981 is the only year the registrant applies to
itself, in six of its own filings (C1a-C1f); 1984 is when the Corpus Christi **Refinery was completed** (S-1
l.3410, FY1997 10-K l.873); 1979 is when **William E. Greehey became CEO and a director of Old Valero**, the
*parent* (S-1 and FY2000 10-K405 recitals — "MR. GREEHEY served as Chief Executive Officer and a director of Old
Valero from 1979"). A plant-completion year and an officer's start year at a different legal person are not
foundings. Confidence in the 1981 date: **Medium**, capped by §3 because every carrier is one corporate record.

**U-2 — "the company began as a holding/lobbying vehicle for a Texas oil family."** Refused as a claim about
**this registrant**, and recorded as an **open predecessor question**. Measured support on this disk: `Dealey` 0,
`Murchison` 0, `lobby` 0, `Lobbying` 0 across all 57 stored SEC texts. What the disk does support is narrower and
different: the registrant was a **wholly owned subsidiary of Old Valero** (a company engaged in "the refining and
marketing business and the natural gas related services business", C1b l.296-297) that **merged into a wholly
owned subsidiary of PG&E Corporation on 1997-07-31** (C1b l.299-301, C2 l.382-383). If a family-holding story
exists, it is Old Valero's story, under a CIK this corpus never enumerated — FR-2. The brief's own framing was
not inherited; it was tested and it failed to produce a carrier here.

**U-3 — "the name comes from a Spanish mission / saint."** Refused: **0 carriers of any family on this disk.**
The single `Spanish` occurrence is a Mexican MTBE joint-venture partner, "Dragados y Construcciones, S.A., a
Spanish construction company" (S-1); capitalised `Mission` is 0 and the 647 lower-case hits are substrings of
`submission`/`commission`/`permission`; `Shamrock Oil` is 0. The nearest real fact is geographic, not etymological:
the 1997 registrant's own address is **530 McCullough Avenue, San Antonio** (S-1 header) and later **One Valero
Place, San Antonio** (C1b l.289) — the city that contains the Mission San Antonio de Valero. **That is a
coincidence of location and I am not upgrading it into an etymology.** Route: FR-4/FR-5 (web archive of the
company's own history pages, or the auction/manuscript family), which are the only places a name story is
actually told.

**U-4 — that the 2001 UDS deal, or any 2002+ figure, describes the company Stage 1 is about.** Refused. The
acquisition is a **purchase** (C3a/C3b: agreement dated 2001-05-06, effective 2001-12-31), so the 1.9 MBD, the
twelve refineries, the 4,500 sites and the five brands are **(PB)** and belong to Stage 2 with an acquired-lineage
caveat. **Conflict logged for the merge:** the 8-K narrative says "On May 7, 2001, Valero Energy Corporation and
Ultramar…" (`0000898822-01-500188_…txt` l.95, and `may10form8k.txt` l.46) while the instrument it attaches is
"dated as of **May 6, 2001**" (l.137). Best-supported reading: signed 6 May, announced 7 May; residual
uncertainty: none material, but a Stage-2 volume must not print both dates as one event.

**U-5 — that the 1979-01-01 → 1980-12-31 stretch is empty of evidence.** Refused. It is empty **in this corpus**;
family (a) cannot reach it for this CIK (perimeter 1997-05-13→, §0), and families (b)(d)(e) were never tried on
it. Reporting it as a null would be the §14 rule-6 error in reverse.

**U-6 — that 30 documents were "1 UNANSWERED / 3 SKIPPED" and nothing else.** Refused as a description of the
shelf. §0 measured 57 documents / 27 accessions, of which 27 are in-window and absent from `_MANIFEST.csv`. Any
downstream agent that trusts the ledger will conclude the SEC shelf holds no in-window text at all — the single
most damaging stale instruction I found this pass (RD-135 rule 10: a retraction must reach the instruction layer;
here the instruction layer is `_RUN.json` itself).

## 10. Five-family verdict table (the contract's table; three states only)

| family | state | what it answered | what it could not answer, and why |
|---|---|---|---|
| **(a) SEC/EDGAR** | **TRIED–ANSWERED** | The registrant's whole legal identity: incorporated **Delaware 1981** as **Valero Refining and Marketing Company**, wholly owned subsidiary of Old Valero; **spun off 1997-07-31** and renamed **Valero Energy Corporation**; CIK 1035002, IRS 74-1828067, DE on the cover, San Antonio HQ; first plant = Corpus Christi, **completed 1984**, nameplate **171,500 BPD**; 1997 **Basis Petroleum** (ex-Phibro Energy USA) purchase; **six refineries / 1,000,000 BPD total, 723,000 BPD crude** by 2000-12-31; **UDS acquired effective 2001-12-31** (agreement 2001-05-06). 27 in-window docs / 16 accessions / 6.81 MB / 941,450 words held; perimeter 1997-05-13→2026-09-21; XBRL 0 of 27,123 rows in window (2006 floor). | Anything before 1997-05-13 as a **filing** (the CIK's own perimeter), hence Old Valero's own origin, ownership and 1981-96 finances; who chose the name; anything the registrant would not say about itself. All C1 carriers are **one corporate record** → §3 cap. |
| **(b) web archives** | **UNTRIED** (0 attempts, 0 calls) | nothing | no shelf, no scripted route, web budget 0. **Not a null** — and it is the family that would hold the company's *self-told* history page, i.e. the strongest competitor to the 1981 recital. Remedy FR-4. |
| **(c) periodical corpora** | **TRIED** — **ANSWERED as a null on the two routes that ran clean**, **UNANSWERED on three** | 0 namings of this registrant in window, measured: `TIER1_CANDIDATE_TEXT` 0 / `VARIANT_TERM_HIT` 0 / `BARE_WORD_MATCH` 2 (A4, mtime 2026-09-29 23:53:27 +0530); the 2 held items are **2005** Aruba newsletters (out of window, `(PB)`, `UNVERIFIED TLS`); trade-journal sweep `Oil & Gas Journal`/`Petroleum Refiner`/`Hydrocarbon Processing` = **numFound 0, proven null on those params**, twice. | `chronicling_america` (2 UNANSWERED hard-stop + 2 ERROR), `hathitrust` (UNANSWERED hard stop), `google_books` (UNANSWERED, max-requests cap) — **tool failures, no zero from them may be cited**. The 4 `TIER1_CANDIDATE` index rows are 2 documents echoing their own query (RD-124). 7 court-file `LEAD_ONLY` rows are (PB) acquired-footprint captions with no bytes here. Remedy FR-3. |
| **(d) digitised corporate print** | **TRIED–UNANSWERED** | nothing — `sources/corporate_print/` = **0 files**. 4 fleet rows: 2 × faceted `numFound=0` (RD-130 ⇒ UNANSWERED), 1 × facet-free creator-query param-null (2026-10-06T12:03:15Z), 1 × `(PB)` 2019 Benicia report. | The registrant's own 1997-2001 annual reports and the **Ultramar Diamond Shamrock** shareholder print are exactly what is missing, and the query block (`valero`, `"valero energy"`, `"diamond shamrock"` × `annual/report/shareholder`, `year_range [1960,2005]`) is bounded by the facet RD-130 condemned. Remedy FR-1. |
| **(e) auction / museum / manuscript** | **UNTRIED** | nothing | no label in the harvester, no script, 0 web calls. Only meaningfully reachable for the two legs (a) cannot touch (Old Valero's Texas papers; the name story). |

**Counted toward each proposed Stage-1 window: family (a) alone → 1 → T3.** No counted family is provisional;
(d) and (b) are the two that could make it T2, and (c) could corroborate the name story.

STATUS: WRITTEN

## 11. `## Untried` — one command each, in the order I would spend them

```
# UNTRIED, ranked by expected verdict-change:
U-1  (d) corporate print, facet-free, this registrant's own 1997-2001 reports:
     python tools/periodical_harvest.py --company valero --family corporate_print     # FORBIDDEN this run
U-2  (b) web archives of the company's own history pages, 1997-2004 (no scripted route exists → FR-4)
U-3  (e) auction / museum / manuscript: nothing run, no tool
U-4  (c) Chronicling America + HathiTrust + Google Books live queries for 1981-2001 → FR-3
U-5  (a) OLD VALERO's own registrant record: `sec_intake.py index "Valero Energy Corporation"`
        is already bound to CIK 1035002; the parent needs its own CIK → FR-2
U-6  (a) UDS's side of the 2001 merger (its own CIK, its 10-Ks 1980s-2001) → FR-5
U-7  (a) EDGAR full-text for the 1981-96 Delaware subsidiary in other filers' exhibits
        (PG&E/NorthEnergy successor filings recite Old Valero; no script reaches a full-text search)
```
Not attempted at all this run, and therefore not reportable as anything: any family beyond `sec_intake.py facts`
(one call) and local reads. `harvest_mine.py` and `periodical_harvest.py` were **left unrun by instruction**, so
their outputs above are the fleet's, quoted with their own timestamps.

STATUS: WRITTEN

## 12. FETCH REQUESTs (0 web calls made; scripts own these routes)

**FR-1 — corporate print, facet-free, in-window.** Re-run the two `valero` corporate-print tasks with the year
facet removed (`periodical_harvest.py --company valero --family corporate_print`), and specifically try:
`Valero Energy Corporation` `annual report` 1997-2001; `Ultramar Diamond Shamrock` `annual report` 1980-2001;
`Valero Refining and Marketing` . Needed to give Stage 1-B a **second family** and to test whether print repeats
1981 or recites an earlier founding.

**FR-2 — the predecessor's registrant record.** Enumerate Old Valero (`Valero Energy Corporation`, Texas,
merged into a PG&E subsidiary 1997-07-31) as its own EDGAR CIK and index it: the 1997 S-1 defines the term
`"OLD VALERO FORM 10-K"` = "Old Valero's annual report on Form 10-K for [the year 1996]"
(`0000950130-97-002339_…txt` **l.23175**), so Old Valero's FY1996 10-K exists and is incorporable by reference.
This is the **only** route to the 1975/1979/1983 leg the brief asserts, and to the family-control question
(U-2). Command shape: `python tools/sec_intake.py index "<Old Valero conformed name>" --company-dir <its own
dir>` — **do not** point it at this company dir.

**FR-3 — periodical routes that failed as tools, not as archives.** `chronicling_america` (2 UNANSWERED hard-stop
2026-09-26T09:45:25Z, 2 ERROR 2026-09-29T13:09:36/38Z), `hathitrust` (UNANSWERED hard stop), `google_books`
(max-requests cap 600). Re-run after the fleet's CA endpoint work (`00_universe/harvest/_CA_ENDPOINT_TEST.md`),
with `andtext` carrying the industry noun as `tools/queries.json` already instructs ("a bare 'Valero' hit is a
lead, never the company").

**FR-4 — web archives.** No scripted CDX route exists in `tools/`. Request: archived `valero.com` history/about
pages 1997-2004, and the same for `dsci.com`/UDS. Needed because a company's own history page is where a
*founding* claim (as opposed to an incorporation recital) is made, and it is a separate lineage from C1.

**FR-5 — UDS's own filings.** Any accession from Ultramar Diamond Shamrock Corporation's CIK (1980s-2001),
especially its last 10-K and the S-4 joint document. Needed to date the acquired brands and to stop Stage 2
writing Diamond Shamrock's age as Valero's.

**FR-6 — the 27 in-window documents have no ledger.** Not a network fetch but the same remedy class: re-run
`python tools/sec_intake.py auto "VALERO ENERGY CORP/TX" --company-dir
founders_playbook/01_companies/company_040_valero --from 1979-01-01 --to 2001-12-31 --max-docs 30` so
`_RUN.json`/`_MANIFEST.csv` describe the candidate-window pass instead of the forward pass. The bytes are
already on disk; only the ledger is wrong.

STATUS: WRITTEN

## 13. Close-out

- **Path:** `founders_playbook/01_companies/company_040_valero/research/A_chronology_feasibility.md` —
  **7,868 words** (`wc -w`, measured after the final edit; §15.2's T3 cap of 8k w/stage is a *deliverable* cap
  for a stage volume, not a probe cap, but it is close enough to note).
- **Gate:** `python tools/gates.py --company-dir founders_playbook/01_companies/company_040_valero --checks
  csv,keys --fail-on substantive --out founders_playbook/03_quality_control/valero_s1_probe_gates.md` →
  **exit 0**, findings **2**, both **coverage-only** ("no register CSVs at root or research/", "no stage_*.md
  volumes found"), which is expected for a probe that writes no registers and no volumes (§15.1); coverage line
  `0 registers, 0 stage volumes, 59 source documents`. On the run made **before** this dossier existed the gate
  printed `tier: exemplar (no tier stated in this company's research/ dossiers — exemplar assumed)`; on the
  final run it printed `tier: T3 (tier T3 from A_chronology_feasibility.md …)` — so the tier is now read from
  this file rather than assumed. The gate's parenthetical warning ("13 mentions, 0 on a verdict line") is about
  its own reader, not about my finding: the verdict lines are the §5 table cells and the header block.
- **Tool calls used:** within the 85 budget; the last measurement calls were spent on §6's re-verification,
  which found and killed one of my own over-broad claims (the S-4 "0 hits" line).
- **Route most likely to change the verdict:** **FR-1 — a facet-free corporate-print run that returns the
  registrant's own 1997-2001 annual reports (or Ultramar Diamond Shamrock's)** — because it is the only
  in-window, non-SEC-lineage text the project can reach tonight; it would put a **second family** inside
  Stage 1-B and move this company from **T3 to T2 core without touching the SEC shelf**. The runner-up, with
  bigger historical stakes and less probability, is **FR-2**: Old Valero's own registrant record is the only
  thing that can either found or destroy the 1975-1983 "family holding vehicle" leg, and if it prints a
  founding date it prints it for a company that is **not this registrant**.

STATUS: WRITTEN
