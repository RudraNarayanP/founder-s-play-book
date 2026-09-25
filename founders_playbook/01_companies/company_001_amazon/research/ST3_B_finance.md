# ST3_B — Amazon.com Stage-3 FINANCIAL EVIDENCE DOSSIER (post-IPO, from 1997-05-16)

**Dataset:** THE FOUNDER'S PLAYBOOK — forensic longitudinal reconstruction
**Company:** Amazon.com, Inc. — CIK 1018724 — `company_001_amazon`
**Stage:** 3. **Stage 3 opens 1997-05-16** — the day after the IPO priced (1997-05-15). Stage 2's boundary is
frozen and is **not** re-litigated here; nothing in this file re-argues a pre-1997-05-16 claim.
**Closing boundary:** the intake ran generously through 1999-12-31. This dossier reports the evidence that
exists, and where the year-end 1999 record is thin it says so rather than smoothing it.
**File role:** register of record for Stage-3 **financial** evidence — the audited annual series, the
quarterly path, the financing events, founder compensation, and the unit-economics knowability audit.
**Hindsight firewall (§2):** no row here states or implies that the later outcome was foreseeable at the
date of its own filing. A 1999 figure is not evidence of a 1997 decision. The record-selection null (§2) is
stated at the head of `## Unit economics` and again in `## Data gaps`: what is unrecoverable here is not
"the truth about Amazon's unit economics" but *what anyone inside the building could see*, and the honest
answer for most of it is that they could see very little, because the company printed almost none of it.
**Confidence scale (§3):** High = 2+ independent lineages or a primary document; Medium = one reliable
source; Low = conflicting, vague, or retrospective-only; UNKNOWN = no evidence recovered.

---

## 0. The two basis labels on every row (convention copied from the sister-company Stage-2 register)

Two labels are used on **every** financial figure in this file, and they are not interchangeable:

| Label | Meaning | Evidential status |
|---|---|---|
| **CONTEMPORANEOUS** | The value is printed in the filing **for that period** — the document whose own fiscal period the number describes (the FY1998 10-K for FY1998; the Q2 1998 10-Q for Q2 1998) | registrant self-report, auditor-attested where it sits inside audited statements, made at the time. Still ONE lineage, but the earliest possible witness for that number |
| **RESTATED (in `<document>`)** | The value appears in a **later** document — a Selected Financial Data column, a prior-year comparative, a Q4/3-month column inside a later 10-K, a pro forma, or an acquisition restatement | retrospective within the same lineage. It may differ from what the period itself reported. **A restated value never reads as filed** and is never used as the primary witness for its own period |

Where both exist, both rows are kept and any disagreement is surfaced in `## Contradictions`, not
reconciled away. **Filing-lineage rule (§3) applies throughout:** the FY1997 10-K405, its ARS, the 1998
proxy, the S-4/S-3 prospectuses that incorporate them by reference, and the 424B3 supplements that only
re-print them are **one source**. A figure found in a 424B3 and in a 10-Q is not corroborated twice.

**Derived rows.** Every computed value is tagged **DERIVED** and prints its arithmetic in-cell. Where the
denominator is not itself filed, the row retracts to **UNKNOWN** — the project rule that killed the
Stage-1 `$871,000`/`2,613,000` pair (`ST2_E`/`_EVIDENCE_CACHE` C-series) binds here: an unfiled denominator
is not a denominator. **Precision is never manufactured**: where a filing prints "$5.1 million" and
"approximately 33%", this dossier writes `$5.1 million` and `~33%`, and does not reconstruct `5,112` or
`32.5%`.

**Line anchors.** Citations are to the saved file's own line numbers (e.g.
`10-K_FY1998_…txt L1234`) so any figure can be re-walked byte-for-byte in `../sources/`.

**Write-first log (§14 rule 1).** This file was created on the first write call after reading
`00_METHOD_AND_STYLE.md` and the Stage-3 intake sections, carrying its full section skeleton plus 14 dated
records, before any further document mining. Records are appended after each document is mined, never
accumulated in scratch.

**Web budget consumed so far: 0 WebSearch, 0 WebFetch.** Ceiling for this dossier is 8, spendable only
after local mining is written down. Every failure is recorded as UNANSWERED with its status.

**Surgical scope (§14 rule 4).** This dossier may create/modify exactly one file: itself. Nothing in
`../sources/` has been or will be opened for writing, moved, renamed, emptied, pruned or "tidied".

---

## Findings

Claim records. `ST3B-nn`. Each carries its own basis label, class, and lineage note.

### A. The audited annual spine

**ST3B-01** — Net sales by fiscal year as printed in the FY1998 Form 10-K's Selected Financial Data:
**FY1998 $609,996k; FY1997 $147,787k; FY1996 $15,746k; FY1995 $511k.** — Date: 1998-12-31 (FY) — Source:
Form 10-K FY1998, acc. `0000891020-99-000375`, filed 1999-03-05, Item 6 Selected Financial Data — Source
date: 1999-03-05 — URL: `../sources/10-K_FY1998_acc-0000891020-99-000375_filed-1999-03-05.txt` — Tier: 1 —
Class: FACT — **Basis: CONTEMPORANEOUS for FY1998; RESTATED for FY1997-FY1995** (they appear here only as
the earlier columns of a later report's summary table) — Passage: verbatim line anchor recorded in
`## Audited series` — Conf: High — Corroboration: **1 lineage** (registrant; FY1996/FY1997 also printed in
the FY1997 10-K405, which is the contemporaneous witness for those two years, not an independent one) —
Conflicts: none on the numerals; vintage conflict handled at `## Contradictions`.

**ST3B-02** — FY1997 net sales as **filed in FY1997's own annual report** — the contemporaneous witness for
1997 — is the number the Stage-3 series must use for 1997, and the FY1998 10-K's comparative column is
carried only as a restatement check. — Date: 1997-12-31 — Source: Form 10-K405 FY1997, acc.
`0000891020-98-000448`, filed 1998-03-30 — Tier: 1 — Class: FACT — **Basis: CONTEMPORANEOUS for FY1997** —
Conf: High — Corroboration: 1 lineage — Note: the ARS shareholder letter states the same year as "838%
revenue growth to $147.8 million"; the ARS and the 10-K405 are **one corporate record in two wrappers**, so
the rounded "$147.8 million" adds no independence (§3).

**ST3B-03** — Accumulated deficit **$162.1 million** at 1998-12-31 and roughly **$349 million** of
outstanding senior indebtedness at the same date, both printed in the FY1998 10-K and re-printed in the
March 1999 S-3. — Date: 1998-12-31 — Source: 10-K FY1998; S-3 File No. 333-74435 filed 1999-03-16 —
Tier: 1 — Class: FACT — **Basis: CONTEMPORANEOUS for FY1998; RESTATED (in the 1999-03-16 S-3)** —
Conf: High — Corroboration: 1 lineage — Conflicts: none.

**ST3B-04** — The accumulated-deficit path mid-year, as printed at the time: **$42.9 million at
1998-03-31** (Q1 1998 10-Q and the June 1998 S-4) → **$64.1 million at 1998-06-30** (424B2 of 1998-08-13) →
**$162.1 million at 1998-12-31** (10-K). — Date: 1998-03-31 / 1998-06-30 / 1998-12-31 — Tier: 1 —
Class: FACT — **Basis: CONTEMPORANEOUS for each stated date in its own document** — Conf: High —
Corroboration: 1 lineage each; the S-4 and 424B2 re-print the 10-Q figure and do not corroborate it.

### B. The quarterly path (what anyone inside the building could see)

**ST3B-05** — The first post-IPO reported quarter: **net sales $27,855 thousand for the three months ended
1997-06-30** against **$2,230 thousand** for the three months ended 1997-06-30, 1996; and **$43,860
thousand / $3,105 thousand** for the six months. — Date: 1997-06-30 — Source: Form 10-Q Q2 1997, acc.
`0000891020-97-001148`, filed 1997-08-14 — Source date: 1997-08-14 — Tier: 1 — Class: FACT —
**Basis: CONTEMPORANEOUS for Q2 1997; the prior-year three-month figure is CONTEMPORANEOUS-AS-COMPARATIVE
only in this document and RESTATED for 1996's own quarterly record (which does not exist — Amazon had no
quarterly filing before the IPO)** — Passage: "Net sales 27,855 … 2,230 … 43,860 … 3,105" — Conf: High —
Corroboration: 1 lineage.

**ST3B-06** — Q3 1998 as filed with the company's own category claim attached: **online music sales of
$14.4 million** in the quarter and a "#1 online music retailer" assertion, in the 8-K release of
1998-10-28 — a **company statement**, not an audited line. — Date: 1998-09-30 — Source: Form 8-K, acc.
`0000891020-98-001498`, filed 1998-10-28 — Tier: 1 — Class: FOUNDER CLAIM / company self-report —
**Basis: CONTEMPORANEOUS for Q3 1998** — Conf: Medium on the $14.4M (single unreconciled company figure;
the audited Q3 10-Q does not break out music) — Corroboration: 1 lineage — Note: an 8-K press release is a
**dated filing** but not audited evidence; the class distinction is the finding.

### C. Financing events

**ST3B-07** — First post-IPO debt instrument: **$75,000,000 three-year senior secured term credit
facility**, commitment letter dated **1997-11-07**, Deutsche Bank AG New York Branch as administrative
agent and Deutsche Morgan Grenfell Inc. as arranger, **increasable to $100,000,000**, "to finance working
capital, capital add[itions]…" — Date: 1997-11-07 — Source: Form 8-K acc. `0000950151-97-000357` filed
1997-11-10, Item 5; corroborated in text by Q3 1997 10-Q filed 1997-11-14 — Tier: 1 — Class: FACT —
**Basis: CONTEMPORANEOUS** — Conf: High — Corroboration: 1 lineage (8-K and 10-Q are the same corporate
record) — Conflicts: none.

**ST3B-08** — **10% Senior Discount Notes due 2008**: announced as a **$275 million** offering (8-K event
1998-04-24), upsized (8-K event 1998-05-05), indenture and form of note filed as Q1 1998 10-Q exhibits
EX-4.1/4.2/4.3, exchange offer registered on Form S-4 File No. 333-56723 described as **"approximately
$326 million gross proceeds"**, priced prospectus 424B2 filed 1998-08-13. The 424B2 also states that
**excluding** these notes the company would have carried only "approximately $2.4 million of
indebtedness" — the before-picture, in the company's own words. — Date: 1998-04-24 → 1998-08-13 —
Tier: 1 — Class: FACT — **Basis: CONTEMPORANEOUS for the instrument; the "$326 million gross" is a
registration-document statement of a range settled in that lineage** — Conf: High on the instrument,
Medium on the exact gross until the closing figure is walked from the S-4/424B2 text — Corroboration:
1 lineage.

**ST3B-09** — **$1,250,000,000 aggregate principal amount of 4¾% Convertible Subordinated Notes due 2009**
sold in a private offering **completed 1999-02-03**, indented as EX-4.1 with a Registration Rights
Agreement as EX-4.2 to the 8-K of event date 1999-02-03. The sequence on the dated record: **$500 million
announced 1999-01-28** (two 8-Ks carry that event date) → priced/upsize release the next day → **$1.25
billion closed six days later**. — Date: 1999-02-03 — Tier: 1 — Class: FACT — **Basis: CONTEMPORANEOUS** —
Conf: High — Corroboration: 1 lineage.

**ST3B-10** — **$2,000,000,000 universal shelf** registered on Form S-3 File No. 333-78797, filed
1999-05-19, amended 1999-06-08 to add the restated certificate of incorporation: common, preferred,
depositary shares, debt, warrants, **stock purchase units and stock purchase contracts**, third-party
warrants. — Date: 1999-05-19 — Tier: 1 — Class: FACT — **Basis: CONTEMPORANEOUS** — Conf: High —
Corroboration: 1 lineage — Note: this is a **capacity** document, not a financing. No proceeds arose from
filing it; the dossier does not treat it as money raised.

### D. Founder money and the documented null

**ST3B-11** — **Jeffrey Bezos's filed compensation: salary $64,333 (1996), $79,197 (1997), $81,840
(1998); bonus nil; securities underlying options nil; all other compensation nil in all three years.** By
1998 his salary was exceeded by four of his own VPs — Dalzell $201,512, Aposporos $142,083, Spiegel
$116,352, Risher $105,168. — Date: 1998-12-31 (table covers 1996-1998) — Source: DEF 14A filed 1999-04-07
acc. `0000891020-99-000635`; 1997/1996 figures also in DEF 14A filed 1998-04-17 acc.
`0000891020-98-000601` — Tier: 1 — Class: FACT — **Basis: CONTEMPORANEOUS for 1998 (in the 1999 proxy) and
for 1997 (in the 1998 proxy); the 1996 salary is RESTATED inside both later tables** — Conf: High —
Corroboration: 1 lineage per year — Note: reported, not re-hunted; already resolved by the Stage-3 intake.

**ST3B-12** — The two proxies' option counts differ **only by split vintage** and are not comparable:
Dalzell's 1997 grant appears as **125,000** in the 1998 proxy and **750,000** in the 1999 proxy, the
difference being the 3-for-1 split effected 1999-01-04. — Date: 1998-04-17 / 1999-04-07 — Tier: 1 —
Class: FACT (about the documents) — Conf: High — Corroboration: 1 lineage — Conflicts: `## Contradictions`
entry; this is a vintage difference, not a data error.

**ST3B-13** — **DOCUMENTED NULL.** The personal guarantees on the card-processing arrangements (Seafirst
merchant account; Wells Fargo bankcard merchant account; company-card guarantee) are **never mentioned in
any filing dated after 1997-05-15**. A corpus scan of the whole archived set for `Seafirst`, `Wells Fargo`,
`Bezos … guarantee`, `release … guarantee` returns hits **only in the 1997 registration lineage**, plus one
post-IPO lease clause that merely quotes Seafirst's prime rate to compute a late rent charge — not
related-party disclosure. The only in-filing statement of any release remains the S-1's forward-looking
undertaking: *"The Company intends to secure releases of all of Mr. Bezos' guarantees as soon as possible
following the closing of this offering."* — Date: window 1997-05-16 → 1999-12-31 — Tier: 1 —
Class: **UNKNOWN, now UNKNOWN-with-the-searches-recorded** — Conf: High in the null itself (the silence is
verified), UNKNOWN as to the guarantees — Corroboration: n/a — **This is a finding about the filing
record, not a fact about the guarantees. The release status stays UNKNOWN; the EDGAR route is exhausted.**

### E. Ownership

**ST3B-14** — Schedule 13G filed **1998-02-17** by **Jeffrey Bezos** reports his post-IPO beneficial
ownership as **9,885,000 shares**. A second 13G, filed **1998-02-13**, is by **Jacklyn Gise Bezos and
Miguel Bezos** (spouse and brother). A Schedule 13G is a **filing by a holder, not a company narrative**:
each number in it is the holder's own statement, under the holder's own signature, about the holder's own
position. — Date: 1998-02-17 / 1998-02-13 — Tier: 1 — Class: FACT (that it was stated) —
**Basis: CONTEMPORANEOUS** — Conf: High — Corroboration: 1 lineage — Note: the family-side row must **not**
be aggregated with the Bezos row without checking each form's own Item 3/4 attribution for shared
beneficial ownership.

---

## Audited series

### S0. What "audited" means here, and the one restatement that moves every 1995-1997 number

Two auditors' reports exist in the Stage-3 window. **Ernst & Young LLP**, dated **1999-01-22** ("except for
Note 11, as to which the date is February 10, 1999"), signs the FY1998 consolidated statements including
"each of the three years in the period ended December 31, 1998" (`10-K_FY1998_…` L1931-1935). The FY1997
`10-K405` carries its own E&Y opinion for 1997/1996/1995. Everything in tables S1-S2 below therefore sits
inside an **audited** set of statements — with two exceptions the reader must not miss:

1. **The Selected Financial Data of the FY1998 10-K is footnoted "Reflects restatement for pooling of
   interests. See Notes 1 and 2" (L1269-1270).** PlanetAll was merged under **pooling-of-interests**
   accounting in August 1998, and under GAAP at the time that required **retrospective restatement of all
   periods presented**. So the 1997/1996/1995 columns of the FY1998 report are *not* what those years
   reported; they are PlanetAll-plus-Amazon recast backwards. Each such number is labelled **RESTATED**
   here, and the **as-filed** version is kept beside it.
2. **The pro-forma block in the FY1998 10-K (L1603-1605) is expressly "not prepared in accordance with
   generally accepted accounting principles"** (L1610-1612). Those three numbers are labelled
   **PRO FORMA (company-stated, unaudited basis)** and never enter the audited series.

**Fiscal basis, stated once.** Amazon.com reported a **calendar fiscal year ending December 31**. FYnn =
the year ending 12-31 of that number. No 52/53-week complication arises, so calendar and fiscal labels
coincide — unlike the sister-company Walmart register. The four-1998-weeks/quarters issue is handled
separately in `## Quarterly path`.

### S1. Statement-of-operations series, FY1995-FY1998 (in $ thousands unless noted)

Every row shows **both witnesses** where both exist. `AF` = as filed in that year's own annual report
(CONTEMPORANEOUS). `RST` = as re-printed in the FY1998 10-K's Selected Financial Data / audited
comparatives (RESTATED for that year).

| Line | FY1995 | FY1996 AF (10-K405, filed 1998-03-30) | FY1997 AF (10-K405) | FY1996 RST (10-K FY1998) | FY1997 RST (10-K FY1998) | **FY1998 CONTEMPORANEOUS** |
|---|---|---|---|---|---|---|
| Net sales | 511 | 15,746 | **147,758** | 15,746 | **147,787** | **609,996** |
| Cost of sales | 409 | 12,287 | 118,945 | 12,287 | 118,969 | 476,155 |
| Gross profit | 102 | 3,459 | 28,813 | 3,459 | 28,818 | 133,841 |
| Marketing and sales | 200 | 6,090 | 38,964 | 6,090 | 40,486 | 133,023 |
| Product development | 171 | 2,313 | 12,485 | 2,401 | 13,916 | 46,807 |
| General and administrative | 35 | 1,035 | 6,573 | 1,411 | 7,011 | 15,799 |
| Merger & acquisition related costs (incl. goodwill amortisation) | — | — | **not a line** | — | — | 50,172 |
| Total operating expenses | 406 | 9,438 | 58,022 | 9,902 | 61,413 | 245,801 |
| **Loss from operations** | (304) | (5,979) | **(29,209)** | (6,443) | **(32,595)** | **(111,960)** |
| Interest income | 1 | 202 | 1,898 | 202 | 1,901 | 14,053 |
| Interest expense | — | — | (279) | (5) | (326) | (26,639) |
| **Net loss** | (303) | (5,777) | **(27,590)** | (6,246) | **(31,020)** | **(124,546)** |
| Loss per share, basic and diluted | (0.00) | (0.31) *pro forma* | **(1.27) *pro forma*** | (0.06) | (0.24) | **(0.84)** |
| Shares used in that EPS | 86,364 * | 18,544 *pro forma* | **21,651 *pro forma*** | 111,271 | 130,341 | **148,172** |

`*` FY1995 column and share count are from the FY1998 10-K Selected Financial Data (RESTATED for 1995).
Line anchors: FY1998/97/96/95 RST = `10-K_FY1998_acc-0000891020-99-000375_filed-1999-03-05.txt`
**L1222-1247** (Selected Financial Data) and **L2016-2039** (audited statements of operations); FY1997/FY1996
AF = `10-K_FY1997_acc-0000891020-98-000448_filed-1998-03-30.txt` **L1177-1197** and **L1861-1881**.

### S2. Balance-sheet and cash series (in $ thousands)

| Line | FY1996 AF | FY1997 AF | FY1997 RST (in FY1998 10-K) | **FY1998 CONTEMPORANEOUS** |
|---|---|---|---|---|
| Cash | 6,248 *(cash & equivalents)* | 109,810 *(cash & equivalents)* | 1,876 *(cash only; securities shown separately)* | **25,561** |
| Short-term investments / marketable securities | — | 15,256 | 123,499 | 347,884 |
| **Cash + securities** | 6,248 | 125,066 | 125,375 | **373,445** |
| Inventories | 571 | 8,971 | 8,971 | **29,501** |
| Prepaid expenses and other | 321 | 3,298 | 3,363 | 21,308 |
| Total current assets | 7,140 | 137,335 | 137,709 | 424,254 |
| Fixed assets, net | 985 | 9,265 | 9,726 | 29,791 |
| Goodwill and other purchased intangibles, net | — | — | — *(not a line)* | **186,377** |
| Total assets | 8,271 | 149,006 | 149,844 | **648,460** |
| **Accounts payable** | 2,852 | 32,697 | 33,027 | **113,273** |
| Accrued advertising | 598 | 3,454 | 3,454 | 13,071 |
| Other liabilities and accrued expenses | 920 | 6,167 | 6,570 | 34,547 |
| Total current liabilities | 4,870 | 43,818 | 44,551 | 161,575 |
| **Working capital (deficiency)** | 2,270 | 93,517 | 93,158 | **262,679** |
| Long-term debt | — | 76,521 *(long-term portion of debt)* | 76,702 | **348,077** (+684 current) |
| **Accumulated deficit** | (6,025) | **(33,615)** | **(37,514)** | **(162,060)** |
| Stockholders' equity | 3,401 | 28,486 | 28,591 | **138,745** |
| Common shares issued & outstanding | 15,900,229 | 23,937,169 | *144,909 (thousands, split-vintage)* | **159,267 (thousands, split-vintage)** |
| Purchases of fixed assets (capex, cash flow) | 1,335 | 7,603 | — | **28,333** |
| Net cash from operating activities | (2,010) | 687 | — | **31,035** |
| Depreciation & amortization | 296 | 3,442 | — | **9,692** |
| Employees at year-end | *158 (recited in the FY1997 report — RESTATED witness)* | **614 full-time** | — | **~2,100** |

Line anchors: `10-K_FY1998_…` **L1955-1996** (balance sheet), **L2229-2270** (cash flows), **L527-528**
(employees), **L1260-1265** (Selected Financial Data balance-sheet block); `10-K_FY1997_…` **L1803-1841**
(balance sheet), **L1210-1214**, **L516-517** and **L729** (employees), **L1067-1080** (properties).

### S3. The restatement deltas — the pooling recast, quantified line by line (DERIVED)

The FY1997 year changed when it was re-witnessed. These are not transcription disagreements; they are the
PlanetAll pooling restatement working through the comparative columns. Arithmetic: `RST − AF`.

| FY1997 line | AF | RST | Delta | Reading |
|---|---|---|---|---|
| Net sales | 147,758 | 147,787 | **+29** | PlanetAll added $29k of sales to 1997 |
| Gross profit | 28,813 | 28,818 | +5 | |
| Marketing and sales | 38,964 | 40,486 | **+1,522** | |
| Product development | 12,485 | 13,916 | **+1,431** | |
| General and administrative | 6,573 | 7,011 | +438 | |
| Total operating expenses | 58,022 | 61,413 | **+3,391** | |
| Loss from operations | (29,209) | (32,595) | **(3,386)** | the 1997 operating loss grew 11.6% by restatement |
| Net loss | (27,590) | (31,020) | **(3,430)** | 1997's loss as remembered is 12.4% larger than 1997's loss as filed |
| Accumulated deficit | (33,615) | (37,514) | **(3,899)** | |
| Accounts payable | 32,697 | 33,027 | +330 | |
| Total assets | 149,006 | 149,844 | +838 | |
| Working capital | 93,517 | 93,158 | **(359)** | restatement made 1997's working capital *smaller* |
| Stockholders' equity | 28,486 | 28,591 | +105 | |

FY1996 moved the same way between its two witnesses: product development 2,313 → 2,401 (+88), G&A 1,035 →
1,411 (+376), total operating expenses 9,438 → 9,902 (+464), loss from operations (5,979) → (6,443)
(**(464)**), net loss (5,777) → (6,246) (**(469)**). FY1996 net sales did **not** move: 15,746 in both.

**The finding, stated plainly.** *The 1997 and 1996 loss figures every later source quotes are restated
numbers.* The FY1997 annual report — the document a 1998 reader would have opened — printed a **$27.6
million** net loss for 1997, not $31.0 million. Every Stage-3 row that uses $(31,020) for FY1997 is a
RESTATED row and is labelled as such. **No restated value in this file reads as filed.**

### S4. The share-count and EPS vintage problem (this is the reason two proxies disagree)

Two vintages are in play, and mixing them produces false contradictions:

- **Splits.** A **2-for-1** split was announced in the 8-K of event date 1998-04-27 and a **3-for-1** split
  was announced 1998-11-19 (8-K acc. `0000891020-98-001686`) effective January 1999 (the ARS/proxy record
  puts effect at **1999-01-04**). Any pre-1999 per-share or share-count figure is therefore **split-vintage
  dependent** and is **not** comparable with a post-1999 one.
- **Pooling.** Share counts for 1997 in the FY1998 10-K include PlanetAll shares retroactively.
- **The FY1997 10-K's own EPS was `pro forma`, on a 21,651-thousand share base, and printed $(1.27)** —
  whereas the FY1998 10-K recasts the same year as **$(0.24) on 130,341 thousand shares**. The difference
  is almost entirely the denominator's construction (the FY1997 report used a pre-IPO-style pro forma
  count; the FY1998 report used actual weighted-average post-IPO shares, restated for splits), **not** a
  change in the loss. This must be said wherever a 1997 EPS appears: **the "EPS" of FY1997 and the "EPS" of
  FY1998 are different instruments and the year-over-year "change" is not interpretable.**
- **Cross-check on the vintage (DERIVED, inputs filed):** `144,909 (FY1998 10-K's 1997 share count, in
  thousands) ÷ 2 ÷ 3 = 24,151.5 thousand`. Against the FY1997 10-K's as-filed `23,937,169`, the residual
  **214,331 shares** is the PlanetAll pooling addition. The identity closes, so the split-factor reading is
  confirmed rather than assumed.

### S5. The distribution-centre estate, as filed each year (physical, not money — but it is the capex story)

| Date of witness | Filed estate | Basis |
|---|---|---|
| 1997-12-31 (10-K405 filed 1998-03-30) | Seattle principal administrative/engineering/marketing/customer-service facilities **~88,000 sq ft**; warehousing & merchandising in a **~85,000 sq ft** Seattle facility (expanded to 85,000 in November 1997) and a **200,000 sq ft** New Castle, Delaware facility opened November 1997. **"The Company does not own any real estate."** | CONTEMPORANEOUS |
| 1998-12-31 (10-K filed 1999-03-05) | US principal offices **~150,000 sq ft** (Seattle, leases expiring June 1999 - April 2003) plus a recently leased **~184,000 sq ft** Seattle office building expiring 2009, to be occupied in 1999; warehousing/fulfillment **~93,000 sq ft** Seattle (expires October 1999) and **200,000 sq ft** New Castle, Delaware (expires October 2002); **December 1998 lease of a ~323,000 sq ft "highly mechanized distribution facility" in Fernley, Nevada, expiring 2009, expected to begin operations in 1999**; Germany: Regensburg HQ + DC **~32,000 sq ft**, Munich editorial/marketing **~9,000 sq ft**; UK: Slough HQ + DC **~41,000 sq ft** (lease to 2008). **"The Company does not own any real estate as of December 31, 1998."** | CONTEMPORANEOUS |

**Total filed fulfilment floor area.** US DCs at 1997-12-31: `85,000 + 200,000 = 285,000 sq ft`. US DCs at
1998-12-31: `93,000 + 200,000 + 323,000 (Fernley, not yet operating) = 616,000 sq ft`, of which
**323,000 sq ft — over half the estate — was leased but not yet in operation** at the balance-sheet date.
Tagged **DERIVED** (sum of filed components). The company's own words carry the caveat: bringing these
facilities to operational readiness "will require significant leasehold improvement and capital
expenditures, and require the Company to stock inventories, purchase fixed assets and hire and train
employees" (L1657-1659).

## Quarterly path and what it could not show

### Q0. A correction to the brief, on the face of the record

The dispatch asks for "the nine 10-Qs 1997-1999". **The EDGAR record holds eight.** There is no Q1 1997
Form 10-Q: Amazon's first periodic report of any kind after the IPO was the Q2 1997 10-Q filed 1997-08-14,
and the Q1 1997 quarter was **never separately filed**. It first appears in 1999, in Note 12 of the FY1998
10-K. The intake manifest says the same (`10-Q` x8, "all eight 1997-99 10-Qs"). This dossier works the
eight that exist and records the missing quarter as a structural feature of the record, not a retrieval
failure. **Q4 quarters, in any year, have no 10-Q by design** — the only Q4 witnesses are the annual
report's Note 12 and the Q4 press release filed on Form 8-K.

### Q1. The quarterly net-sales path, with every vintage kept separate

Amazon printed the **same quarter up to three times** in three documents, and the three do not agree. The
table below therefore refuses to pick one silently. `AF` = the figure as filed in that quarter's own 10-Q
(CONTEMPORANEOUS). `NK` = the figure as re-printed in Note 12 "Quarterly Results (Unaudited)" of the FY1998
10-K filed 1999-03-05 (L3288-3293, L3305-3310). `L` = the figure as a comparative column inside a **later**
10-Q (RESTATED). All in $ thousands.

| Quarter | Net sales AF (own 10-Q) | Net sales in Note 12 | Net sales as a later comparative | Net loss AF | Net loss Note 12 | Basis verdict for the quarter |
|---|---|---|---|---|---|---|
| Q1 1997 | **none exists** | 16,005 | — | none | (3,220) | **NO CONTEMPORANEOUS WITNESS.** First printed 1999-03-05 |
| Q2 1997 | 27,855 (L283) | 27,855 | 27,855 (Q2 1998 10-Q L270) | (6,705) | **(7,345)** | sales contemporaneous; **loss restated +640** |
| Q3 1997 | 37,887 (L269) | 37,887 | 37,887 (Q3 1998 10-Q L269) | **(8,510)** | **(9,647)** | sales contemporaneous; **loss restated +1,137** |
| Q4 1997 | **none exists** (no Q4 10-Q) | 66,040 | 66,040 (Q4-1998 8-K L439) | none | (10,808) | **NO CONTEMPORANEOUS QUARTERLY WITNESS** |
| Q1 1998 | 87,375 (L288) | **87,395** | **87,361** (Q1 1999 10-Q L268) | (9,259) | **(10,369)** | **three different printed values for one quarter** |
| Q2 1998 | 115,977 (L270) | **116,010** | **115,982** (Q2 1999 10-Q L247) | (21,226) | **(22,579)** | three printed values |
| Q3 1998 | 153,698 (L269) | 153,698 | **153,648** (Q3 1999 10-Q L258) | (45,171) | (45,171) | sales restated (50); loss unchanged |
| Q4 1998 | **none exists** | **252,893** | 252,893 (Q4-1998 8-K, filed 1999-01-27) | none | (46,427) | earliest witness = the 8-K release |
| Q1 1999 | 293,643 | n/a (no FY1999 10-K on disk) | — | (61,667) | — | CONTEMPORANEOUS |
| Q2 1999 | 314,377 | n/a | — | (138,008)* | — | CONTEMPORANEOUS |
| Q3 1999 | 355,777 | n/a | — | (197,080) | — | CONTEMPORANEOUS |
| Q4 1999 | **no filing on disk** | — | — | **UNKNOWN** | — | **EMPTY** (see `## Data gaps`) |

`*` Q2 1999 net loss is taken from the Q2 1999 10-Q's own loss-per-share computation block, "Net loss - as
reported … $138,008 / $22,579 / $199,675 / $32,948" (L671); the 3-month column is 138,008 and the six-month
1998 comparative is 32,948 — itself a fourth presentation of the 1998 loss path (`10,369 + 22,579 = 32,948`
**DERIVED: foots exactly**).

### Q2. The arithmetic that settles which quarterly basis is the right one (DERIVED, inputs all filed)

The Note 12 quarters are the **only** set that foots to the audited annual lines. Both years, four lines
each:

- **FY1998 net sales:** `87,395 + 116,010 + 153,698 + 252,893 = 609,996` = audited FY1998 net sales. **Foots.**
- **FY1998 gross profit:** `19,333 + 26,216 + 34,875 + 53,417 = 133,841` = audited. **Foots.**
- **FY1998 net loss:** `(10,369) + (22,579) + (45,171) + (46,427) = (124,546)` = audited. **Foots.**
- **FY1997 net sales (restated basis):** `16,005 + 27,855 + 37,887 + 66,040 = 147,787` = the FY1998 10-K's
  restated FY1997. **Foots — to the restated number, not to the 147,758 that 1997 filed.**
- **FY1997 net loss (restated basis):** `(3,220) + (7,345) + (9,647) + (10,808) = (31,020)` = restated FY1997
  net loss. **Foots — and note that the four quarters sum to the restated loss, not the $(27,590) filed.**

**Therefore:** the quarterly series a Stage-3 reader should treat as authoritative is **Note 12 of the
FY1998 10-K** — which means the authoritative quarterly path for 1997 and 1998 is itself a **restated**
presentation. The 10-Qs are contemporaneous but superseded. Both facts are recorded; neither is used to
erase the other.

**The one internal caveat the company itself printed** (L3314-3317): "The sum of quarterly per share amounts
may not equal per share amounts reported for year-to-date periods. This is due to changes in the number of
weighted average shares outstanding and the effects of rounding for each period." So quarterly EPS rows are
**not** additive, and any attempt to sum them is a defect, not a finding.

### Q3. The quarter-by-quarter balance-sheet path (cash, inventories, payables, working capital)

Working capital is **DERIVED as `Total current assets - Total current liabilities`**, both of which are
filed in every quarter, so the denominator rule is satisfied and the ratio stands. Where the 10-Q prints a
"Working capital" line itself, the filed word is used instead. ($ thousands)

| Quarter end | Cash | Marketable securities | Inventories | Total current assets | Total current liabilities | **Accounts payable** | **Working capital (DERIVED)** |
|---|---|---|---|---|---|---|---|
| 1997-06-30 | 47,700 | — | 1,652 | 59,206 | 17,357 | 10,327 | **41,849** |
| 1997-09-30 | 44,687 | — | 2,732 | 52,697 | 19,848 | 15,386 | **32,849** |
| 1997-12-31 | 1,876 *(per FY1998 10-K)* / 1,567 *(per Q2 1998 10-Q comparative)* | 123,499 | 8,971 | 137,709 / 137,335 | 44,551 / 43,818 | 33,027 / 32,697 | **93,158 / 93,517** |
| 1998-03-31 | 98,600 | (in "cash and equivalents") | 11,674 | 132,893 | 48,478 | 34,374 | **84,415** |
| 1998-06-30 | 2,523 | 337,396 | 17,035 | 369,441 | 71,924 | 47,556 | **297,517** |
| 1998-09-30 | 14,856 | 322,404 | 19,772 | 374,657 | 99,455 | 60,046 | **275,202** |
| 1998-12-31 | 25,561 | 347,884 | 29,501 | 424,254 | 161,575 | 113,273 | **262,679** *(this one is printed as "Working capital" in the 10-K)* |
| 1999-03-31 | 5,248 | 1,437,717 | 45,236 | 1,525,278 | 201,585 | 133,018 | **1,323,693** |
| 1999-06-30 | 42,539 | 1,101,698 | 59,387 | 1,256,958 | 277,944 | 165,983 | **979,014** |
| 1999-09-30 | 43,149 | 862,536 | 118,793 | 1,080,068 | 357,671 | 236,711 | **722,397** |
| 1999-12-31 | **UNKNOWN — no filing on disk** | — | — | — | — | — | **UNKNOWN** |

Two readings must be held apart. (a) **The presentation changes under the reader.** Through Q4 1997 the
company showed one line, "Cash and cash equivalents" (1997-06-30: $47,700; 12/31/97: $109,810); from Q1 1998
it split "Cash" from "Marketable securities", so the visible "cash" collapses from $98,600 (3/31/98) to
**$2,523** (6/30/98) — not a collapse in liquidity but a reclassification plus the arrival of the Notes
proceeds into securities. Any Stage-3 sentence beginning "cash fell…" across that boundary is a presentation
artefact and is not made here. (b) **The 1,876 / 1,567 pair is a real restatement, and it is provable:**
`1,567 + 123,499 = 125,066` = the FY1997 10-K's own `109,810 + 15,256 = 125,066`; and
`1,876 + 123,499 = 125,375 = 125,066 + 309`. **The $309k gap is the PlanetAll pooling addition**
(DERIVED; the identity closes in three different documents).

### Q4. Customer-account and mix disclosures — the closest thing to a unit metric anyone could see

These are **company-stated operating statistics printed inside filings**, not audited lines, and the
definition moves. `CA` = cumulative customer accounts as stated.

| Date | Cumulative customer accounts (as stated) | Where stated | Repeat-customer share / foreign-sales share stated |
|---|---|---|---|
| 1997-12-31 | 1.5 million | FY1998 10-K L1317; ARS 1997 | international ~25% of net sales (FY1997) |
| 1998-03-31 | "approximately 2.3 million" | Q1 1998 10-Q / S-4 of 1998-06-03 | — |
| 1998-06-30 | **3.1 million** | 424B2 of 1998-08-13 | — |
| 1998-06-30 | **3.3 million** | Q2 1999 10-Q L861 (retrospective) | 21.3% of Q2 1998 net sales (same document) |
| 1998-09-30 | **4.5 million** | Q3 1999 10-Q L870 (retrospective) | 20.1% of Q3 1998 net sales |
| 1998-12-31 | 6.2 million | FY1998 10-K L1317; ARS 1998; Q4 1998 8-K | repeat orders "over 60%" of FY1998 orders; "more than 64 percent" for Q4 1998; international ~20% |
| 1999-03-31 | 8.4 million | Q1 1999 10-Q L626 | repeat customers 66% of Q1 1999 orders |
| 1999-06-30 | 10.7 million | Q2 1999 10-Q; 8-K of 1999-07-22 | net foreign sales 23.9% of Q2 1999 |
| 1999-09-30 | 13.1 million | Q3 1999 10-Q; 8-K of 1999-10-28 | net foreign sales 24.5% of Q3 1999 |
| 1999-12-31 | **UNKNOWN** | — | — |

**The 3.1 vs 3.3 million collision at 1998-06-30 is a genuine contradiction inside one lineage** — see
`## Contradictions`. Note also the definitional drift the company itself flags: from 1999 the accounts are
"(inclusive of Accounts)" and later "(inclusive of accounts with Amazon.com Auctions)", so the 1999 series
is **not** on the same base as the 1998 series. Any growth rate run across that boundary is unsound and is
not presented as a fact.

### Q5. What the quarterly path could NOT show anyone inside the building

The quarterly filings gave a reader **net sales, gross profit, three expense lines, a loss and a share
count**. They did **not** give, in any quarter of 1997-1999: order counts, orders per customer, average
order value, contribution margin per order, cost of fulfilment per order (the filings state that
fulfilment cost sits *inside* "marketing and sales" — FY1998 10-K L1390-1392 — so it cannot be separated
from advertising even with the filed data), gross proceeds of third-party selling, unit shipping economics,
or cohort retention. Those are the subject of `## Unit economics: knowable and not knowable`.

**The single sharpest statement of the problem.** The company told investors that **period-to-period
comparison of its own numbers was not meaningful**: "the Company believes that period-to-period comparisons
of its operating results, including the Company's gross profit and operating expenses as a percentage of net
sales, are not necessarily meaningful and should not be relied upon as an indication of future performance"
(`10-K_FY1997_…` L1293-1297). That was the company's own contemporaneous answer to anyone building a
quarterly trend line. Stage 3 should report the trend, and report that the issuer disclaimed it in the same
period.

## Financing events

Every event: **amount, date, instrument, conversion/redemption terms, and use of proceeds as stated in the
document itself.** Where a document states only an intention, that is said. Basis labels as in §0.

### F1. Chronological register of capital events, 1997-05-16 → 1999-10-28

| # | Date (event) | Instrument / event | Amount as printed | Terms as filed | Use of proceeds **as stated in the document** | Document (and basis) |
|---|---|---|---|---|---|---|
| 1 | 1997 (FY) | **Initial public offering** — carried as a financing cash flow | **$49,103k net proceeds from IPO** (1997 column of the audited cash-flow statement) | — | not restated here; pricing and allocation belong to Stage 2's frozen boundary | `10-K_FY1998_…` L2257; `10-K_FY1997_…` — **CONTEMPORANEOUS to FY1997 as a cash-flow line; the IPO itself is Stage 2's record and is not re-litigated** |
| 2 | 1997-11-07 (commitment); drawn **December 1997** | **Three-year senior secured term credit facility** ("the Senior Loan") | **$75,000,000**, "may be increased to … $100 million" | Deutsche Bank AG, New York Branch as administrative agent; Deutsche Morgan Grenfell Inc. as arranger; secured | 8-K Item 5: "to finance working capital, capital add[itions]…" | `8-K_event-1997-11-07_…`; `10-Q_Q3-1997_…`; `10-K_FY1998_…` L1519-1521 — **CONTEMPORANEOUS** |
| 3 | 1997-11 (November 1997) | Vendor financing for fixed assets | ~**$3.0 million**, imputed rate **7.7%**, three-year term, four equal payments | asset-acquisition loan | purchase of fixed assets | `10-K_FY1997_…` L1641-1644; cash-flow supplemental "Fixed assets acquired under financing agreement … $3,021" — **CONTEMPORANEOUS** |
| 4 | 1998-04-17 / 1998-04-24 (settlements) | **Stock-funded acquisitions, Regulation S**: Bookpages Limited (England), Telebook, Inc. (Florida), Internet Movie Database Ltd | **540,066 shares** of common stock issued | off-shore issuance; Item 9 Reg S | consideration for the acquisitions | `8-K_event-1998-04-17_acc-0000891020-98-000694` — **CONTEMPORANEOUS**. The FY1998 10-K later states the **aggregate purchase price of the three acquisitions, plus related charges, was approximately $55 million**, funded with "common stock and cash", **approximately 3.2 million shares** issued (L1548-1555) — **RESTATED for April 1998** |
| 5 | 1998-04-24 (announced) → 1998-05 (completed) | **10% Senior Discount Notes due 2008** | announced **$275 million** → upsized 1998-05-05 → **approximately $326 million gross proceeds**; net proceeds **approximately $315.7 million** after selling commissions and transaction expenses; cash-flow line "Proceeds from long-term debt 325,987" | Sold at a substantial discount to a **principal amount at maturity of $530 million**; **no cash interest before 1 November 2003** (interest accretes to $530M); from and after 1 May 2003, 10% p.a. payable 1 May / 1 Nov; optional redemption on or after 1 May 2003; **Change of Control put at 101% of Accreted Value**; indenture with Bank of New York as trustee (EX-4.1, note form EX-4.2, registration rights EX-4.3 to the Q1 1998 10-Q); senior unsecured, `pari passu` with unsubordinated unsecured debt | 424B2 L1355-1360: "The Company used approximately **$75.0 million** of such proceeds to retire the Senior Loan and expects to use the remaining net proceeds for general corporate purposes, including working capital to fund anticipated [operating losses]" | `8-K_event-1998-04-24_…`; `8-K_event-1998-05-05_…`; `10-Q_Q1-1998_…` EX-4.1/4.2/4.3; `S-4_FileNo-333-56723_…`; `424B2_…` L1345-1360; `10-K_FY1998_…` Note 5 — **CONTEMPORANEOUS** |
| 6 | **May 1998** | **Prepayment/retirement of the Senior Loan** | ~$75.0 million retired; **$2.0 million of unamortized loan fees written off**; cash-flow "Repayment of long-term debt (78,108)" | — | — | `10-K_FY1998_…` L1526-1527, L1638-1639, L2261 — **CONTEMPORANEOUS (FY1998)** |
| 7 | 1998-06-01 (effected) | **Two-for-one stock split**, stockholders of record 1998-05-20, in the form of a stock dividend | share count ×2 | — | — | `10-Q_Q1-1999_…` L453-458 — **CONTEMPORANEOUS as an event; the recital "The accompanying consolidated financial statements have been restated to reflect the splits" is the reason every earlier per-share figure in the archive is a different vintage** |
| 8 | 1998-08-12 / 1998-08-27 | **Junglee Corp.** acquisition (purchase method) and **PlanetAll / Sage Enterprises** merger (**pooling of interests**) | Junglee: **approximately 4.7 million shares** issued, "substantially all of the **approximately $180 million** purchase price allocated to goodwill and other purchased intangibles"; PlanetAll: **approximately 2.4 million shares** | amortised straight-line over lives averaging ~3 years | — | `8-K_event-1998-08-03_…` (merger agreements), `8-K_event-1998-08-12_…` (Junglee audited financials + pro formas), `8-K_event-1998-08-27_…` (PlanetAll completed, seven EX-27 restated schedules), `8-K/A` of 1998-10-26 — **CONTEMPORANEOUS for the events; the FY1998 10-K's $180M/$55M/2.4M/4.7M figures are RESTATED summaries** |
| 9 | 1998-09-30 → 1998-10-22 | **Shelf registration and a selling-stockholder resale prospectus** | S-3 File No. 333-65091 filed 1998-09-30; 424B3 "FINAL PROSPECTUS" of 1998-10-22 offers **2,662,125 shares of Common Stock** by "certain stockholders … or by their pledgees, donees, distributees" | resale, no primary issuance | **424B3 / S-3: the company receives no proceeds from a secondary sale** | `S-3_FileNo-333-65091_…`, `424B3_final-prospectus_…`, supplement of 1998-10-27 — **CONTEMPORANEOUS. This is a dilution/liquidity event, not a financing event: no money entered the company.** Terminated by POS AM Amendment No. 2 of 1999-10-26 |
| 10 | 1998-11-19 (announced) → **1999-01-04** (effected) | **Three-for-one stock split**, stockholders of record 1998-12-18, stock dividend | share count ×3 | — | — | `8-K_event-1998-11-19_…`; `10-Q_Q1-1999_…` L456-457 — **CONTEMPORANEOUS** |
| 11 | **1999-02-03** | **4¾% Convertible Subordinated Notes due 2009** (private offering) | announced **$500 million** on 1999-01-28; priced and **increased from $500 million to approximately $1.25 billion** the same day; **$1,250,000,000 aggregate principal** completed 1999-02-03; cash-flow "Proceeds from long-term debt 1,250,000" (Q1 1999) | interest **4¾% p.a., cash, semi-annual 1 Feb / 1 Aug, first payment 1999-08-01**; **initial conversion price $156.055 per share**; "may be converted into, in the aggregate, **8,009,996 shares**"; unsecured, subordinated to senior debt; Provisional Redemption before 2002-02-06 at $1,000 + accrued, provided the stock exceeded **150% of the conversion price for 20 of 30 consecutive trading days** and the resale shelf is effective — with an **additional payment of $212.60 per $1,000 note** less interest paid; after 2002-02-06 redeemable on 30 days' notice; Fundamental Change put at **100% of principal + accrued**; indenture EX-4.1 and registration rights EX-4.2 to the 8-K | FY1998 10-K L1761-1766: "general corporate purposes, including working capital to fund anticipated operating losses, the expansion of the Company's core business, investments in new business segments and markets, capital expenditures, acquisitions or investments in complementary businesses, products and technologies and repurchases and retirement of debt" | `8-K_event-1999-01-28_…` x2, `8-K_event-1999-02-03_…`, `10-Q_Q1-1999_…` Note 2, `10-K_FY1998_…` — **CONTEMPORANEOUS** |
| 12 | 1999-Q1 | **Open-market/bought-back retirement of its own discount notes** | repurchased **$126.0 million face amount** of the 10% Senior Discount Notes, "representing accreted value of $83.9 million"; **remaining face outstanding $404 million** at 1999-03-31 (of $530M) | — | — | `10-Q_Q1-1999_…` L436-442 — **CONTEMPORANEOUS.** This is the only place in the window where the company retires its own debt at a discount, and it is the filed answer to "what did the converts buy?" partly: cash returned to bondholders, not to operations |
| 13 | 1999-03-16 | **Shelf for the converts' resale** — S-3 File No. 333-74435 | registers the notes and conversion shares for **selling holders**; "Amazon.com will not receive any proceeds from the sale of the notes and the common stock into which the notes are convertible by the selling holders" | — | none to the company | `S-3_FileNo-333-74435_…` L1698-1701; amended 1999-05-13; supplements run weekly to 1999-12-30 — **CONTEMPORANEOUS** |
| 14 | 1999-05-19 (amended 1999-06-08) | **$2,000,000,000 universal shelf** — S-3 File No. 333-78797 | **$2 billion** of capacity: common, preferred, depositary shares, debt, warrants, **stock purchase units and stock purchase contracts**, third-party warrants | — | none — **a capacity filing, not a raising** | `S-3_FileNo-333-78797_…`, `S-3A_…` — **CONTEMPORANEOUS** |
| 15 | 1999-04-24 → 1999-06-10 | **Stock-funded acquisitions (1999)**: Alexa Internet, e-Niche, Exchange.com, Accept.com | Alexa/e-Niche 8-K: consideration "**totaling approximately $250 million**"; Exchange.com merged **1999-05-14** via Amazon.com Auctions, Inc.; Accept.com merged **1999-06-09** via ADC Acquisitions, Inc.; Alexa merged **1999-06-10** via AI Acquisition, Inc. with Amazon options substituted at a stated **Exchange Ratio** | — | — | `8-K_event-1999-04-26_acc-…000805`, `8-K_event-1999-05-14_…`, `8-K_event-1999-06-09_…`, `8-K_event-1999-06-08_…` — **CONTEMPORANEOUS. Note the index event date 1999-06-08 on the Alexa 8-K precedes the completion date 1999-06-10 stated inside it; reported as filed, not "fixed"** |
| 16 | as of 1998-12-31 | **Equity-method investment** | "approximately 46%" of **drugstore.com, inc.** | equity method; basis classified within other purchased intangibles; share of investee loss runs into merger and acquisition related costs | — | `10-K_FY1998_…` L1574-1583 — **CONTEMPORANEOUS (FY1998)** |

### F2. The audited money-in picture for FY1998 (the cross-check on all of the above)

From the audited FY1998 consolidated statement of cash flows (`10-K_FY1998_…` L2256-2264, $ thousands),
**CONTEMPORANEOUS for FY1998**:

| Financing line | 1998 | 1997 | 1996 |
|---|---|---|---|
| Net proceeds from initial public offering | — | 49,103 | — |
| Proceeds from exercise of stock options | 5,983 | 509 | 195 |
| Proceeds from issuance of capital stock | 8,383 | 3,746 | 8,443 |
| **Proceeds from long-term debt** | **325,987** | **75,000** | — |
| Repayment of long-term debt | (78,108) | (47) | — |
| Financing costs | (7,783) | (2,309) | — |
| **Net cash provided by financing activities** | **254,462** | **126,002** | **8,638** |

Supplemental non-cash (same statement, L2273-2277): **Common stock issued in connection with acquisitions
$217,241** in 1998 (nil in 1997 and 1996); fixed assets acquired under capital lease $442 (1997); fixed
assets acquired under financing agreement $3,021 (1997).

**Two derived identities worth stating (DERIVED, inputs filed):**
- `325,987 + 8,383 + 5,983 - 78,108 - 7,783 = 254,462` — the financing section foots exactly. The FY1998
  capital story is therefore, in cash terms: **$326.0M of notes in, $78.1M of the Senior Loan repaid,
  $7.8M of financing costs, and $217.2M of stock handed to acquisition targets that never touched cash at
  all.**
- The **cash raised in the window by selling securities into the market ($326.0M + $1.25bn = $1.576bn
  gross) is dwarfed by the non-cash equity cost of acquisitions** only in the second year; in FY1998 the
  stock consideration ($217,241k) was **67% of the entire debt raise** (`217,241 ÷ 325,987 = 0.666…`).
  Tagged DERIVED; both inputs are audited statement lines.

### F3. What the leverage pivot actually did to the obligation, as filed

- FY1997: long-term debt **$76,702k** (restated) / $76,521k (as filed) — essentially the Senior Loan.
- FY1998: **long-term debt $348,077k** + current portion $684k = **$348,761k**; the 10-K's own Item 6 line
  reads **"Long-term debt 348,140"** (thousands), and the S-3 of 1999-03-16 recites "$349 million of
  outstanding senior indebtedness" as of 1998-12-31 (DERIVED check: `348,140 vs 348,077+684 = 348,761` — a
  **$621k** presentation difference between the Selected-Financial-Data line and the balance-sheet lines,
  inside one document; recorded, not reconciled away).
- Interest expense moved from **$(326)k (FY1997)** to **$(26,639)k (FY1998)** — but **$23,970k of that is
  non-cash** ("Non-cash interest expense", L2238). So the Notes' 1998 cost in cash was roughly
  `26,639 - 23,970 = 2,669` thousand (DERIVED; both inputs audited). **This is the single most
  mis-readable number in Stage 3**: the FY1998 interest expense line is ~90% accretion, not cash.
- The 424B2's own before-picture: excluding the Senior Discount Notes the company would carry only
  "**approximately $2.4 million of indebtedness**". One document, filed 1998-08-13, contains both the
  $2.4M-before and the $326M-raise. That pair is the leverage decision, sized.

## Unit economics: knowable and not knowable

_TO be populated._

## Ownership, dilution and the 13G testimony

_TO be populated._

## Founder compensation and personal money

_TO be populated (ST3B-11 … ST3B-13 expanded)._

## Metrics

_TO be populated: DERIVED rows with arithmetic, or UNKNOWN where no filed denominator exists._

## Timeline

_TO be populated._

## Data gaps

_TO be populated: EMPTY / UNANSWERED / UNTRIED kept distinct._

## Contradictions

_TO be populated._

## Sources consulted

_TO be populated._

## Provenance and method notes

_TO be populated._

## Outbound corrections

_TO be populated._

## CSV append rows

_TO be populated last, once record IDs are final._
