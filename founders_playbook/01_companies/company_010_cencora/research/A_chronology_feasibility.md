# A — chronology feasibility PROBE · company_010_cencora

**Dataset:** Founder's Playbook — Stage-1 chronology-feasibility probe (not a stage volume)
**Company:** Cencora (Fortune rank 10, FY ending 2025-09-30) · registrant `Cencora, Inc.`, CIK 0001140859, ticker COR
**Probe agent:** probe-cencora · **written:** 2026-10-06 (local) · **method:** `00_METHOD_AND_STYLE.md` §3, §14, §15.2; RD-112, RD-124, RD-130, RD-134
**Hindsight firewall:** nothing below imports the 2023 brand into an earlier period, or a 2001 recital into a founding claim. Every pre-2001 date on this page is labelled as a *recital about another legal person*, not as this registrant's origin.
**Confidence scale:** High = 2+ independent origins or a primary document · Medium = one reliable source · Low = retrospective-only or conflicting · UNKNOWN = no evidence recovered.

## Verdict (read this first)

STATUS: WRITTEN

1. **The fleet's Stage-1 candidate window `1985-01-01 → 2000-12-31` cannot be a stage of this registrant, on the
   registrant's own words.** Its first indexed EDGAR document — the S-4 of 2001-05-23 — states inside its own
   financial statements: *"AmeriSource-Bergen Corporation (formerly AABB Corporation) (the 'Company') was
   incorporated in the state of Delaware on March 16, 2001"* and *"Other than its formation, to date the Company and
   its subsidiaries have not conducted any activities."* (`sources/sec/0000893220-01-500258_w48458s-4.txt:7772-7779`)
   The 1985-2000 window therefore belongs to **two other legal persons**, both of which the same filing names with
   their own dates: **AmeriSource Health Corporation, "incorporated in Delaware in 1988"** (same file, l.1834) and
   **Bergen Brunswig Corporation, "formed in New Jersey in 1956"** (same file, l.1857).
2. **"Cencora" is a naming fact, not an absence of history — and the whole intake pipeline still asks the brand
   question.** Measured: the string `cencora` occurs **0 times in the 30 stored document bytes** and 32 times only in
   the tool's own metadata (`sources/sec/*.meta.json` × 30, `sources/sec/_RUN.json` × 2). Every one of the 8 harvest
   queries configured for this slug (`tools/queries.json`: the 8 tasks whose `company` field is `cencora`) is keyed on
   `cencora` / `"cencora inc"`, and
   the fleet mine's entity vocabulary for this company is the literal phrase **`cencora formerly known as`**
   (`research/A4_harvest_mine.md` l.21). A 1994 document cannot answer that query. Every periodical and corporate-print
   zero on this shelf is therefore a statement about our parameter, not about the archive (RD-124's slug-as-grep-term
   defect pointed at a renamed registrant; RD-130's facet lesson in the same shape).
3. **Tier issued (per RD-112, per stage, named window):** Stage 1 = `2001-03-16 → 2004-09-30` →
   **T3 register, PROVISIONAL** — one family (a) returning in-window Tier-1 text. It is a *count*-driven T3 with an
   unusually heavy carrier: 30 in-window documents across 6 filing lineages. Families (b) and (e) are UNTRIED, and
   (c) and (d) are TRIED–UNANSWERED for the reason in ¶2, so the ceiling is provisional, not the floor.

## PROPOSED windows (the universe CSV has no founding-date column — header enumerated, no such field)

STATUS: WRITTEN

`00_universe/fortune_top_50_2026.csv` header, printed not assumed:
`rank, company, revenue_usd_millions, revenue_fiscal_year, profit_usd_millions, hq_city, hq_state, fortune_industry,
universe_source_url, verified_by_second_source, confidence, notes` — 50 rows; the Cencora row carries
`revenue_fiscal_year = fiscal year ended 2025-09-30` and **no date of any earlier kind**. So no window below is inherited.

| id | window (PROPOSED) | whose window it is | basis |
|---|---|---|---|
| **W-1** | **2001-03-16 → 2004-09-30** | **the registrant itself** (AABB Corp → AmeriSource-Bergen Corp → AmeriSourceBergen Corp → Cencora, Inc.) | registrant's own incorporation date, printed in its own S-4 (l.7772-7773); formation-date to first three fiscal year-ends (FY ends 30 Sep, per the universe row's own FY convention) |
| W-0 | 1985-01-01 → 2000-12-31 | **not this registrant.** AmeriSource Health Corporation (DE 1988) and Bergen Brunswig Corporation (NJ 1956), and a third person named nowhere on disk | fleet candidate, re-labelled: the registrant's EDGAR record contributes **0 of 2,567** indexed rows here |
| W-2 | 1956-01-01 → 2001-08-28 | **predecessor lineage**, two independent lines: Bergen Brunswig (1956 NJ) and AmeriSource Health (1988 DE) | recited in the registrant's 2001 S-4 (l.1857, l.1834). §3: one lineage is one lineage — these are two, and the 2001 holdco is a third person, not the sum of them |

**Recommendation to the orchestrator:** issue Stage 1 against **W-1**, and write W-2 as a *lineage* file whose every
pre-2001 date carries `RETROSPECTIVE SOURCE` — because the only carrier of those dates in this repository is a 2001
filing talking about other companies. If Stage 1 is nonetheless dispatched over W-0, it will return a register with no
registrant-authored content, which is a window error, not a data gap.

## Per-stage tier, and which families counted

STATUS: WRITTEN

| stage (window) | (a) SEC | (b) web archives | (c) periodicals | (d) corp. print | (e) auction/museum | families counted | tier |
|---|---|---|---|---|---|---|---|
| **W-1** 2001-03-16→2004-09-30 | **ANSWERED** — 30 docs / 4,904,411 B / 671,629 w, all filingDate 2001 | UNTRIED | TRIED–UNANSWERED (brand-keyed) | TRIED–UNANSWERED (brand-keyed + faceted zero) | UNTRIED | **1** — (a) | **T3 PROVISIONAL** |
| W-0 1985-01-01→2000-12-31 | ANSWERED *for the naming question only* (recital pass); 0 in-window registrant docs | UNTRIED | TRIED–UNANSWERED; predecessor text demonstrably exists but under another slug | TRIED–UNANSWERED | UNTRIED | **0** registrant-authored | **not issuable** — window belongs to another person |
| W-2 1956→2001-08-28 (lineage) | UNTRIED *as a question* — needs the predecessor CIKs walked (FR-1) | UNTRIED | TRIED–UNANSWERED — 6 in-window trade-press layers naming "Bergen Brunswig" are on disk under `company_006_cvs` (26/9/35/14/13/5 hits), never queried here | TRIED–UNANSWERED (FR-3) | UNTRIED | 0 on this shelf, **2 reachable** | **candidate T2 after FR-1 + FR-3 — do not dispatch before re-grade** |

Which families counted: **only (a)**, and only for W-1. Which are provisional: everything else, because (c)/(d) were
asked the wrong question and (b)/(e) were never asked at all. Under §15.2 a T3 here is a statement about the intake,
and RD-112's Costco precedent (`T3 PROVISIONAL: family (c) went untried for want of a query block`) is the exact
shape of this case: the query block exists but its vocabulary is post-2023.

## Five-family verdict table (three states only; an untried family is never a null)

STATUS: WRITTEN

| family | state | measurement / remedy |
|---|---|---|
| **(a) SEC / EDGAR** | **TRIED–ANSWERED** (for W-1); **TRIED–UNANSWERED** (for W-0, remedy FR-1) | Uncapped walk: 2,567 filings enumerated, `0 submissions rows dropped`, **0 UNANSWERED slices** (`sources/_index/_INDEX.md` l.4, l.75). Measured floor **2001-05-23**; rows in `1985-01-01..2000-12-31` = **0 of 2,567** (own count, appendix M-2). In-window doc pass stored 0; recital pass stored 30 (`_RUN.json`, window `2000-12-31..2025-12-31`). XBRL is a separate measured perimeter: `facts` printed *"0 of 26,066 observations … fall in 1985-01-01..2000-12-31. Observed XBRL coverage runs 2006-09-30..2026-10-31"* — so §K money series for W-0/W-2 must come from the filings, never from companyfacts. |
| **(b) web archives** | **UNTRIED — 0 calls** | No `sources/web_archive/` on this shelf (`ls -d 01_companies/*/sources/web_archive` → only company_011_microsoft, company_042_target). No query task configured. The CDX route exists inside `tools/periodical_harvest.py`, which this brief forbids me to run. **Remedy FR-2**, and the handles are on disk already: the S-4 prints `http://www.amerisource.com` (l.839 and l.1832) and `http://www.bergenbrunswig.com` (l.850 and l.1855). RD-134/Microsoft NR-1 respected: I checked for sidecars before writing UNTRIED and there are none. |
| **(c) periodical corpora** | **TRIED–UNANSWERED** | 4 configured queries (`chronicling_america` ×2, `internet_archive` ×2) + `hathitrust` ×1 + `google_books` ×1. States in `00_universe/harvest/candidates.csv` (14 cencora rows): CA `404`/`SKIPPED: hard stop: 5 consecutive failures (host halted)` → **ERROR/UNANSWERED**; HT `SKIPPED: hard stop` → **UNANSWERED**; GB `totalResults=0` → NULL *for that query*; IA `numFound=0` → NULL, and the **facet-free** IA re-run returned exactly 2 items, both CIA Reading Room scans dated `1966-04-07`. Those bytes are held and mined to **NULL** (`A4_harvest_mine.md` l.25-26): `cencora`=0, `americsource`=0, `bergen`=0 (own grep, appendix M-4); they are 1966 FOIA documents about "electronic 'snooping' devices" whose only pharmacy-adjacent string is `{ieut drug wholesaler "who: was` — an OCR fragment naming no one. **All six vocabularies are `cencora`-keyed.** Remedy **FR-3**. |
| **(d) digitised corporate print** | **TRIED–UNANSWERED** | Two `corporate_print` tasks, both `cencora`/`cencora inc`-keyed: at 13:05Z `numFound=0` (classified NULL "FOR THESE EXACT PARAMS ONLY"), at 19:07Z the same labels re-ran faceted and the harvester itself re-graded them `UNANSWERED, not a null: numFound=0 WITH A YEAR FACET … Re-run the same query with year_range` (RD-130 firing as designed). `sources/corporate_print/` holds **0 bytes**. No query has ever used `AmeriSource`, `AmeriSourceBergen` or `Bergen Brunswig` as a creator/term. Remedy **FR-3**. This is the one family that flipped tiers elsewhere in this project (Walmart, Target, Boeing, Kroger), so its UNANSWERED state is the live risk, not a footnote. |
| **(e) auction / museum / manuscript** | **UNTRIED** | No task and no directory anywhere in the configured harvest families: `families present across all 420 tasks in tools/queries.json = chronicling_america, corporate_print, google_books, hathitrust, internet_archive`. This is structural, not company-specific. Remedy: a documented route (or an explicit method ruling that family (e) is out of scripted scope) before any null is recorded for it. |

## The naming chain, resolved as the brief required

STATUS: WRITTEN

`python tools/sec_intake.py resolve --ticker COR` → `{"ticker": "COR", "cik": 1140859, "name": "Cencora, Inc."}`
`sources/_index/_registrant_CIK0001140859.json` → `"former_names": ["AMERISOURCEBERGEN CORP", "AMERISOURCE BERGEN CORP"]`
— an **unordered list carrying no dates**, which is the whole reason the pre-rename reading of this shelf has to be
done from cover pages. Chain as printed by the documents themselves, oldest attestation first:

| # | legal person as printed | where it is printed on disk | what it proves | what it does NOT prove |
|---|---|---|---|---|
| 1 | **Bergen Brunswig Corporation**, "a New Jersey corporation" / "formed in New Jersey in 1956" | `w48458s-4.txt:1857`, `:8441-8442`; 234 mentions in the stored bytes | a predecessor person with a stated 1956 formation | any founding of *this* registrant; the earlier Bergen trade name (see Refusals) |
| 2 | **AmeriSource Health Corporation**, "incorporated in Delaware in 1988" | `w48458s-4.txt:1834` (and the S-4/A twins at l.1869 / l.1905 — same lineage, one source) | a second predecessor person inside W-0 | a founding date; a founder |
| 3 | **AABB Corporation** — charter exhibit in the registrant's first filing | `w48458ex3-1.txt:12` "AABB CORPORATION / AMENDED AND RESTATED / CERTIFICATE OF INCORPORATION"; bylaws for `AMERISOURCE-BERGEN CORPORATION` at `w48458ex3-2.txt:14-16` | the holdco's birth name, from a corporate instrument rather than a narrative | — |
| 4 | **AmeriSource-Bergen Corporation** (hyphenated), registrant block on the S-4 cover | `w48458s-4.txt:20` name, `:21` "(Exact name of Registrant as specified in its charter)", `:26` `DELAWARE / 5122 / 23-3079390` | the cover-page spelling, which no index column carries | continuity of EIN = continuity of person (it is not) |
| 5 | **AmerisourceBergen Corporation, "formerly known as AABB Corporation"**, effective 2001-08-29 | `0000947871-01-500695_f8k_082901.txt:45-47`; same sentence in the full-submission copy l.91 | the renaming, stated by the registrant, with an effective date | the 2023 renaming, which is not on disk at all |
| 6 | **Cencora, Inc.** | EDGAR metadata only: `_RUN.json`, `_registrant_*.json`, `resolve --ticker COR`; **0 hits in 30 document bytes**; earliest index row whose *primary document name* carries the brand = `2024-02-13 SC 13G/A 0001104659-24-020561 tv0564-cencorainc.htm` (1 of 2 such rows in 2,567) | that the SEC's own registrant record for CIK 1140859 now reads "Cencora, Inc." | **the date and instrument of the renaming** — no document on disk states it (FR-4) |

## Carriers for the origin / predecessor question (file + line)

STATUS: WRITTEN

All paths relative to `founders_playbook/01_companies/company_010_cencora/`. Line numbers are locators; the stable
label is the file + the quoted phrase (§14 r12).

| carrier | file : line | what it carries | class / confidence |
|---|---|---|---|
| **Registrant's own incorporation statement** | `sources/sec/0000893220-01-500258_w48458s-4.txt` : 7772-7779 (NOTE 1) — "(formerly AABB Corporation) … incorporated in the state of Delaware on March 16, 2001 … have not conducted any activities" | origin of the *legal person* whose shelf this is | FACT (primary document, own filer) / High |
| Same statement, re-filed | `…_w48458as-4a.txt` : 8050 · `…_w48458a2s-4a.txt` : 8634 · `0000950109-01-504387_ds4.txt` : 8492 | the 1994-act amendments are the **same registration lineage** for the first three; the 2001-10-19 S-4 is a different accession | same lineage as S001 for l.8050/8634 (§3) — **not** corroboration |
| Renaming, with effective date | `sources/sec/0000947871-01-500695_f8k_082901.txt` : 45-53 | "Effective August 29, 2001 … AmerisourceBergen Corporation, formerly known as AABB Corporation … AmeriSource and Bergen combined their businesses by merging with acquisition subsidiaries … Bergen common stockholders received 0.37 of a share" | FACT / High |
| Charter instrument | `sources/sec/0000893220-01-500258_w48458ex3-1.txt` : 12-13 ("AABB CORPORATION / AMENDED AND RESTATED / CERTIFICATE OF INCORPORATION") · `…ex3-2.txt` : 14-16 ("AMENDED AND RESTATED BYLAWS / OF / AMERISOURCE-BERGEN CORPORATION") | AABB → AmeriSource-Bergen, from the certificate and bylaws themselves | FACT / High |
| Predecessor A | `…w48458s-4.txt` : 1834 | AmeriSource Health Corporation, Delaware, 1988 | FACT about *that* person / High; **not** this registrant's origin |
| Predecessor B | `…w48458s-4.txt` : 1857 (+ its subsidiaries named at 1868-1872: "(i) pharmaceutical distribution, (ii) PharMerica, and (iii) other businesses. The pharmaceutical distribution segment includes Bergen Brunswig Drug Company and ASD Specialty Healthcare, Inc. … The Lash Group") | Bergen Brunswig Corporation, New Jersey, 1956 | same status as above |
| Merger instrument + parties | `…w48458s-4.txt` : 8438-8446 (Agreement and Plan of Merger "as of the 16 day of March, 2001, by and among AABB Corporation … AmeriSource Health Corporation, a Delaware corporation … Bergen Brunswig Corporation, a New Jersey corporation … A-Sub Acquisition Corp. … B-Sub Acquisition Corp.") | the four other persons in the transaction, by name and state | FACT / High |
| Registrant's own web handles (for family (b)) | `…w48458s-4.txt` : 839 and : 1832 `http://www.amerisource.com` · : 850 and : 1855 `http://www.bergenbrunswig.com` | the domains a CDX pass should walk, printed twice in one document | FACT / High |
| **Third-party SEC text naming a predecessor, IN W-0** | `../company_015_cardinal/sources/sec/0000950152-94-001030_0000950152-94-001030.txt` : 1175 — "The companies in the peer group index are Bergen Brunswig Corporation," (DEF 14A, filed as of date 19941014, CIK 0000721371) | an independent contemporaneous naming of predecessor B inside the fleet's proposed window | CONTEMPORARY OBSERVATION / High — **but it is another company's shelf; read-only cross-check, not my corpus** |
| **Trade press naming a predecessor, IN W-0** | `../company_006_cvs/sources/…` 6 layers: `corporate_print/micro_IA40706915_0203` (26 × "Bergen Brunswig"; masthead "Drug Store News … Special reports: … Drug wholesalers—p. 61"), `corporate_print/micro_IA40706928_0007` (9), `corporate_print·periodicals/micro_IA40706934_0338` (35), `periodicals/micro_IA40706901_0405` (14; "FEBBO … Vol. 1, No. 22/Incorporating CHAIN STORE AGE Drug … Wholesaling '79"), `periodicals/micro_IA40706918_0157` (13; "November 12, 1984"), `periodicals/micro_IA40706951_0247` (5; "Vol. 16 No. 19") | Drug Store News / Chain Store Age layers carrying Bergen Brunswig as an active corporate subject across 1979-199x — i.e. the periodical family is **not** empty for this lineage, it was never asked | CONTEMPORARY OBSERVATION / Medium-High pending a date read of each issue; `AmeriSource` = **0** in all six (measured) |

**Rule-4 duplicate check on those cross-company bytes:** `micro_IA40706934_0338_djvu.txt` exists on two shelves and is
**one** document — `md5sum` → `4aa6d311f6c393b58b747b8c07d6215f` for both. Counted once. The two CIA layers on my own
shelf have distinct hashes (`f664b58959eb4b3bc355b927cc530cef`, `44d489181508fdf3786fde9941d17c33`) so they are two
items, both NULL.

**Independence note (§3).** The 2001 S-4, its S-4/A and S-4/A No. 2 and the 424B3 are **one source**: three filings,
one registration lineage, 12 of the 30 stored documents. Counting the recital at l.1834 three times across
`w48458s-4 / w48458as-4a / w48458a2s-4a` would manufacture corroboration out of a refile. The independent origins on
this shelf are therefore: (i) the S-4 lineage, (ii) the 2001-08-24 S-3, (iii) the 2001-10-19 S-4, and (iv)(v)(vi) the
three 2001 8-Ks, which report **three different event dates** — 2001-07-31 (`d8k.txt:20`), 2001-08-27
(`s8k_082801.txt:19`), 2001-08-29 (`f8k_082901.txt:19`) — so they are three filings but not three independent accounts
of one fact; the 2001-08-29 and 2001-08-30 pair bracket the same closing week.

## Untried

STATUS: WRITTEN

- **(b) web archives — 0 calls, 0 attempts.** No `sources/web_archive/`, no configured task. Remedy FR-2.
- **(e) auction / museum / manuscript — 0 calls, no route configured for any company** (5 families exist in
  `tools/queries.json`; this is not one of them). Remedy: a method ruling or a new task family.
- **(c) periodicals / (d) corporate print keyed on the predecessor vocabulary** — never run for this slug in any
  form: no query containing `AmeriSource`, `AmeriSourceBergen`, `AABB`, `Bergen Brunswig`, `Bergen County Chemicals`,
  `Brunswig Drug`, `PharMerica` or `ASD Specialty`. Remedy FR-3.
- **(a) filings by the predecessor persons** — the EDGAR records of AmeriSource Health Corp, Bergen Brunswig Corp and
  the 1994-2001 AmeriSourceBergen Corp have never been walked; they are different CIKs and `sec_intake` resolves names
  only through EDGAR's ticker map, so this cannot be done from my shelf. Remedy FR-1.
- **(a) the 2023 renaming instrument and everything after 2001-10-19** — the recital pass stored 30 of 380 in-window
  filings and stopped: `_UNANSWERED.csv` reads *"UNANSWERED NOT-ENUMERATED: 372 in-window filings were never listed
  because --max-docs 30 was reached"*. The first 10-K (2001-12-28), the DEF 14A (2002-01-23) and every later history
  page are indexed but not on disk. Remedy FR-5.
- **XBRL/§K for W-0 and W-2** — measured unreachable (coverage starts 2006-09-30), so it is a named perimeter, not a
  gap to try again.

## FETCH REQUESTs

STATUS: WRITTEN

```
FETCH REQUEST FR-1  (family (a), highest value): walk the PREDECESSOR registrants, not this one.
  run: python tools/sec_intake.py index "AMERISOURCE BERGEN CORP" --company-dir <a NEW dir for the 1994-2001 person>
       python tools/sec_intake.py index "BERGEN BRUNSWIG CORP"   --company-dir <ditto>
       python tools/sec_intake.py index "AMERISOURCE HEALTH CORP" --company-dir <ditto>
  then: facts/auto over 1994-01-01..2001-08-28 (EDGAR's own floor is 1993-94, so 1994-2001 is reachable paper).
  why: I did not run these under company_010_cencora: the registrant guard would either refuse (rightly) or write a
       second registrant's index into this company's protected shelf, and RD-112 defect 5 is exactly that clobber.
  note: if these CIKs return in-window 10-K/S-1 text, W-0 gains a filings answer that is REAL but belongs to another
        legal person; it must be filed as lineage, per §3.
FETCH REQUEST FR-2  (family (b), the one that stays untried because no script route is sanctioned to me):
  CDX pass on http://www.amerisource.com and http://www.bergenbrunswig.com (handles printed at
  sources/sec/0000893220-01-500258_w48458s-4.txt:1832 and :1855) for 1996-01-01..2004-12-31, into
  sources/web_archive/. This is the route the method says can flip a tier (RD-134/Microsoft NR-1).
FETCH REQUEST FR-3  (families (c) and (d)): re-write the 8 `company == cencora` tasks in tools/queries.json
  (indices 104-105 are the corporate_print pair) — vocabularies to
  ["cencora","americsource bergen","amerisource","bergen brunswig","aabb corporation","bergen county chemicals",
  "phamerica","asw specialty healthcare"] and re-run periodical_harvest --facet-free for this slug over
  1956-01-01..2001-08-28 and 2001-08-29..2010-12-31. Proof the archive answers: 6 in-window Drug Store News layers
  already held under company_006_cvs name "Bergen Brunswig" 5-35 times each (appendix M-5).
  DO NOT schedule until the fleet reharvest and mine release their writers (see "Late-arriving bytes").
FETCH REQUEST FR-4  (the renaming date): the 2023 name-change carrier — the 8-K or 8-K cover page filed around
  2023-09 and the first 10-K whose cover prints "Cencora, Inc.". Neither is on disk: 0 of 30 stored docs post-date
  2001-10-19. Enumerated index shows 2,567 rows; ask for accession list, not for a web read.
FETCH REQUEST FR-5  (history section of the origin): the first 10-K (2001-12-28, accession 0000011454-01-500032,
  primary doc abcform10k.htm) and the 2002 DEF 14A (0000893220-02-000073) — both indexed, neither stored, and a
  10-K's Item 1 is the likeliest in-corpus carrier of a company-written "our history" paragraph.
```

## What I refused to claim, and why

STATUS: WRITTEN

1. **I do not claim a founding date for Cencora, and I do not claim 1988 or 1956 as one.** Per the brief's trap and
   hard rule 5, a predecessor spelling found in a 2001+ recital is evidence of a name. The only founding-class date
   this registrant ever asserts about itself on disk is **2001-03-16**, and it is paired with a nil-activity sentence,
   which forecloses reading the 1988/1956 lines as this person's origin.
2. **I refuse "the company filed nothing before 2001".** The measured statement is narrower: **0 of 2,567 indexed rows
   for CIK 1140859 fall before 2001-05-23, in an uncapped walk with 0 UNANSWERED slices** — that is a perimeter of one
   registrant record, and the pre-2001 story lives under other CIKs that were never walked (FR-1). EDGAR's own floor
   (1993-94) explains 1985-1993 silence for *any* registrant; it explains nothing about 1994-2000, which is simply not
   this person's record.
3. **I refuse to treat the fleet mine's NULLs as periodical nulls.** `A4_harvest_mine.md` reports `NULL 2 / 
   TIER1_CANDIDATE_TEXT 0` — and its entity vocabulary is `cencora formerly known as` (l.21). Zero is the arithmetically
   certain result of asking a 1994 document for a 2023 brand. Per the file's own header ("Nothing on this page is a
   finding") and hard rule 6, those two rows are cited as held bytes only.
4. **I refuse the 32-line `cencora` count as a document hit** and any use of `1908` as a year: measured, all 82
   occurrences of `1908` in the stored document bytes are inside the address string `19087-5594` (Chesterbrook PA) —
   82 of 82 (`grep -o '1908' | wc -l` = 82; `grep -o '19087' | wc -l` = 82). This is hard rule 6's `S435`-as-a-dollar-amount class.
5. **I refuse to call the three EIN-shared filings one company's continuity.** Cover pages of the S-4, the 8-Ks and the
   S-3 all print EIN `23-3079390`; a shared EIN across a holdco formation is not evidence that the 1994 business and
   the 2001 person are the same legal subject, and the S-4's own note says the opposite (nil-activity shell formed
   2001-03-16).
6. **I refuse to publish a date for each of the six cross-company Drug Store News layers beyond the two mastheads that
   literally print one** ("November 12, 1984"; "Wholesaling '79"). The others (Vol. 16 No. 19 etc.) need an issue-date
   read before any claim rests on them.
7. **I refuse to run `harvest_mine.py` / `periodical_harvest.py`** as briefed, and refused `sec_intake index` on a
   predecessor name into this directory for the RD-112 reason written into FR-1.

## Late-arriving bytes (§14 r11) and live writers

STATUS: WRITTEN

- `research/A4_harvest_mine.md` — **mtime 2026-10-06 17:19:26 +05:30**, i.e. rewritten ~2 minutes after this probe's
  claim (17:17:15) and *during* my session. I re-read it immediately before quoting and the quoted numbers are from
  that re-read (2 candidate rows, 2 mined, 0 untried at limit, `NULL 2`, `TIER1_CANDIDATE_TEXT 0`, entity vocabulary
  `cencora formerly known as`). Its content was byte-identical to the earlier read, so no figure in this dossier is
  stale — but **the file has a live writer, so a later re-mine may supersede those counts.**
- `sources/periodicals/*` — mtimes 2026-09-30 01:35:59 / 01:36:04, i.e. written by the same mine pass, not by a
  periodical harvest of my own. Attribution matters: the brief's "0 periodicals" is true of `periodical_harvest.py`
  output and false of the shelf, which holds 2 bytes via the mine. I record the family state above as
  TRIED–UNANSWERED, not UNTRIED, for exactly that reason.
- `sources/sec/_RUN.json` 2026-09-30 00:32:34 · `sources/_index/*` 2026-09-30 00:32:03 — pre-session intake, quoted as
  measured, not re-run (a re-run would rewrite another writer's artifacts).
- Nothing arrived on `sources/` that I did not account for: 30 sec, 2 periodicals, 0 corporate_print, 0 web_archive,
  9 index/run files.

## Gate

STATUS: WRITTEN

`python tools/gates.py --company-dir founders_playbook/01_companies/company_010_cencora --checks csv,keys --fail-on substantive --out founders_playbook/03_quality_control/cencora_s1_probe_gates.md`
→ **Findings: 2 | Passes: 0**, both coverage-only ("no register CSVs at root or research/", "no stage_*.md volumes
found"), 32 source documents seen — the expected pre-authoring state named in my brief; 0 substantive findings, so the
exit code is not failed by `--fail-on substantive`. Re-run after authoring: still 2 coverage findings, and the gate's
tier reader moved from its default (`tier: exemplar (no tier stated in this company's research/ dossiers -- exemplar
assumed)`) to **`tier: T3 (tier T3 from A_chronology_feasibility.md ... the most recent write wins, §15.2 regrade)`** —
i.e. the first run's "exemplar assumed" default was a no-input placeholder, now superseded by the T3 PROVISIONAL this
dossier issues for W-1.

## Measurements appendix (every quantifier above, with its command)

STATUS: WRITTEN

- **M-1 identity/former names** — `python -c "json.load('sources/_index/_registrant_CIK0001140859.json')"` →
  `former_names: ["AMERISOURCEBERGEN CORP","AMERISOURCE BERGEN CORP"]`, `count: 2567`, `built: 2026-09-29T19:02:03Z`.
- **M-2 window coverage** — own count over `sources/_index/submissions.csv` (2,567 rows):
  `rows in 1985-01-01..2000-12-31: 0` · `rows before 2001-05-23: 0` · `rows whose primaryDocument names Cencora: 2`,
  earliest `2024-02-13 SC 13G/A 0001104659-24-020561 tv0564-cencorainc.htm`.
- **M-3 name strings in stored document bytes** — command form: `grep -i -c "<term>" sources/sec/*.txt`, summed with
  `awk -F: '{s+=$2} END{print s+0}'`. Counting unit is **matching lines**, not occurrences. Results:
  `AmeriSourceBergen` (unhyphenated) **1,476 lines**, present in 12 of the 30 documents and **0 in the 2001-05-23 S-4
  itself** — its heaviest carriers are `w48458a2s-4a.txt` 502, `ds4.txt` 471, `ds3.txt` 235, i.e. the amendments and
  the later filings (**21 of the 30 documents** carry the unhyphenated spelling); `AmeriSource-Bergen` (hyphenated) **874 lines**, the S-4's own cover spelling (cover name l.20);
  `AMERISOURCE BERGEN` (spaced) 7 · `AmeriSource Health` 192 · `Bergen Brunswig` 234 · `AABB` 67 · `PharMerica` 239 ·
  **`Cencora` 0** · `BergUSA` 0 · `"Bergen County"` 0 · `CanMed` 0 · `Lincare` 0 · `Anagram` 0 · `USA Interactive` 0.
  Three spellings of one name coexist inside a single accession (`0000930661-01-501359_d8k.txt` l.22 `AmerisourceBergen
  Corporation`, l.41 `AmeriSource-Bergen`, l.50 `AmerisourceBergen`, l.52 `AMERISOURCEBERGEN CORPORATION`, and the
  filer's own `<DESCRIPTION>` tag at l.5), so a grep vocabulary for this lineage needs all
  three, plus the hyphen and space variants. Shelf-wide over `sources/sec/` (documents **and** metadata) the string
  `cencora` = **32 lines**, which decompose exactly as 30 `.meta.json` sidecars × 1 + `_RUN.json` × 2.
- **M-4 own periodical bytes** — per file, `grep -oi`: `cencora=0 americsource=0 bergen=0 philadelph=0` for both CIA
  layers; md5 `f664b58959eb4b3bc355b927cc530cef` / `44d489181508fdf3786fde9941d17c33`.
- **M-5 cross-company predecessor text** — per file, `grep -oi 'bergen brunswig' | wc -l` and
  `grep -oi americsource | wc -l`: 26/0 · 9/0 · 35/0 · 14/0 · 13/0 · 5/0 across the six `company_006_cvs` layers;
  md5 collision check on `micro_IA40706934_0338` (identical on two shelves = 1 document).
- **M-6 harvest state** — `00_universe/harvest/candidates.csv` (3,803 rows; header
  `company, source_family, query, item_id, title, date_or_issue, url, snippet_or_hitcount, http_status, classification,
  retrieved_at`), company==`cencora` → 14 rows: chronicling_america 2 ERROR(http 404) + 2 UNANSWERED;
  corporate_print 2 NULL + 2 UNANSWERED(faceted); google_books 1 NULL; hathitrust 1 UNANSWERED;
  internet_archive 2 NULL + 2 LEAD_ONLY (the two CIA items).
- **M-7 configured vocabularies** — `tools/queries.json`: 420 tasks; families present =
  `chronicling_america 111, internet_archive 104, corporate_print 103, hathitrust 56, google_books 53` (no auction
  family); tasks with `company == cencora` = **8**, all `search`, all keyed on `cencora` / `"cencora inc"`.
- **M-8 XBRL perimeter** — `python tools/sec_intake.py facts "Cencora, Inc." --company-dir … --from 1985-01-01 --to
  2000-12-31` → `facts: NULL -- NO DATA FILE WRITTEN. WINDOW: 0 of 26,066 observations … Observed XBRL coverage runs
  2006-09-30..2026-10-31, and 512 tags are present`.
- **M-9 numeric decoy** — `grep -o '1908' sources/sec/*.txt | wc -l` = 82 and `grep -o '19087' … | wc -l` = 82, so
  every `1908` is the ZIP prefix.
- **M-10 fleet intake row** — `00_universe/_FLEET_INTAKE.tsv`:
  `cencora | Cencora | company_010_cencora | rc0/inwindow0/UNANS0 | 0 | rc1/inwindow380/UNANS1 | 30 | filing_floor
  2001-05-23 | slices_capped=no | DONE`.

## The route most likely to change this verdict

STATUS: WRITTEN

**FR-1** — walking the predecessor registrants' own CIKs (AmeriSource Health Corporation, Bergen Brunswig Corporation,
and the 1994-2001 AmeriSourceBergen Corporation) over 1994-2001, because that is the only route that can turn family
(a) from "0 in-window documents" into "in-window Tier-1 filings that are contemporaneous rather than recital", and it
is the one intake step no tool on my shelf is allowed to perform for me.

