# FORENSIC LONGITUDINAL DATASET — WAL-MART STORES, INC., STAGE 1 (1945 → 1970-10-08)

## MERGED VOLUME 1 — Header, STAGE BOUNDARY JUSTIFICATION, §A–§L, and §M–§U

**Assembly note (written by the merge pass, 2026-09-26; no line below it is rewritten, renumbered or
re-ordered).** This file is the merged Stage-1 narrative for company_002, assembled from `_parts/s1_p1.md`,
`_parts/s1_p2.md` and `_parts/s1_p3.md` exactly in that order. The parts' own file-level headers and status
preambles are **retained verbatim where they fell in the sequence**, so the words below them read as written by
their authors; where a preamble says "Volume 2" or "Volume 3" it names the *part*, not this volume — the live
geometry is this: **stage_1.md** carries Header + boundary + §A–§U, and **stage_1_part_2.md** carries
`UNTRIED ROUTES, CARRIED FORWARD`, the claim-record appendix and part 3's register-row handoff block.
Numbering (A–U, claim ids, metric ids, conflict ids) continues across the two volumes and is not renumbered
(§9.3).

**Register handoff blocks.** The `>>> REGISTER ROWS FOR MERGE <<<` blocks emitted by parts 2 and 3 are kept
in place inside the narrative as the audit trail of what was requested; they are **not** live register content.
Every row in them was applied, refused-with-a-reason, or re-pointed at merge, and the account is in
`03_quality_control/walmart_s1_merge.md`.

**Two defects carried visibly, not fixed.** (1) §U's own subsection labels (`### U.0`…`### U.4`) collide with
the `U.nnn` anchor grammar the `anchors` gate reads, so the gate reports U.1–U.4 as narrative anchors with no
register row; they are section numbers, not conflicts, and the merge does not retitle a part (§9.3). (2) Part 1's
header and §D-R03 carried "a Delaware corporation; incorporated 1969-10-01", which no document in `sources/`
supports; the corrected reading (state UNKNOWN, day UNKNOWN, 1969 year-only and company-asserted) is what the
registers carry, as conflict **U.014**, and the original wording stays visible in the part's own text so the
audit pass can adjudicate the pointer, not just the value.

---

# FORENSIC LONGITUDINAL DATASET — WAL-MART STORES, INC., STAGE 1 (1945 → 1970-10-08)
## Volume 1 — sections Header, STAGE BOUNDARY JUSTIFICATION, A–D

*This is one document split for the 60,000-word file cap (method §9.3). Section letters, claim IDs,
metric IDs and conflict numbering run continuously across volumes: **§A–§D live in this volume
(`_parts/s1_p1.md`); §E–§P in `s1_p2.md`; §Q–§U and the claim-record appendix in `s1_p3.md`.**
Cross-references of the form `(Walmart S1 §D.2, part_1)` name the volume. No id anywhere in the
spine is renumbered to make a part look self-contained.*

**Company:** Wal-Mart Stores, Inc. — a **Delaware corporation**; incorporated **1969-10-01**; the
operating entity from **1962** was **Wal-Mart, Inc., an Arkansas corporation** (register lineage and
the two-issuer question are handled at §B.0 and §boundary; `company_002_walmart`).
**Stage:** 1 of 3. **Span:** **1945 → 1970-10-08**, **contested at both ends and argued, not
asserted, at `## STAGE BOUNDARY JUSTIFICATION` below.** The **open** end is a
**registrant-retrospective date** (1945 = the Ben Franklin franchise working arrangement; the
earliest attestation anywhere in the corpus is the FY1973 annual report's "twenty-eight year
history") and is therefore labelled a **CLAIMED ORIGIN, not a documented one**. The **close**
**1970-10-08** is the **200,000-share public offering**, a date carried **inside an audited
FY1972 note** — i.e. by a document one year after the event, in the registrant's own lineage.
**File:** part 1 — Header, boundary, **§A–§D**; §E–§P part 2; §Q–§U and claim records part 3.
**Hindsight firewall (method §2).** Nothing in this volume treats later scale — the 1991
revenue-ranking future, the discount-department-store category, the eventual supplier apparatus —
as evidence that a 1945–1970 decision was rational, that contemporaneous competitors were fools,
or that any outcome was foreseeable. **SIC/sector context, competitor fates and post-1980 rankings
are NOT ADMITTED AS EVIDENCE ABOUT 1962–1970 in this file** and appear, where they appear at all,
only as `(PB)` consequences. The word "visionary" does not occur here; the founder's later memoir is
**FOUNDER CLAIM / RETROSPECTIVE INTERPRETATION** even where it is the only source.
**Record-selection null (§2).** Unrecoverable because the survivor's archive is the one that was
kept: no 1945–1962 internal deliberation, no rejected option, no contemporaneous price or sales
record from inside the first store, no independent count behind any company self-report, and **no
document dated inside the 1945–1968 span at all** except what the registrant later wrote down about
itself. See §A.2 and §S (part_2).
**Confidence (§3):** **High** = 2+ independent sources or a primary document; **Medium** = one
reliable source; **Low** = conflicting, vague, or retrospective-only; **UNKNOWN** = a finding, never
a gap to fill or smooth.
**Tier discipline (§5) and the single-lineage finding (§3 filing-lineage rule).** **Every positive
statement about this company inside the window traces to ONE lineage: the registrant's own annual
reports plus its auditor's opinion on them.** The independent route that should have existed — the
Commission's own statistical registers — was **closed by a page-level negative** (A5): the
*Securities Traded on exchanges, as of December 31, 1970* issuer register prints
**WALGREEN … WALWORTH and ZERO occurrences of Wal-Mart**, so the 941 KB on-disk register **cannot
witness 1962–1971**. Corroboration therefore does not exist for company-state claims in this stage,
and confidence is capped accordingly. Repeated prints of one figure across FY1972–FY1980 are
**version evidence, never corroboration.**

---

## STAGE BOUNDARY JUSTIFICATION

**Geometry note.** This section is written as the Amazon Stage-2 volume writes its contested
boundary: **candidates enumerated, the evidence for each named, and the reason each rival FAILS
stated against a document** — not a boundary asserted and then defended rhetorically.

| Stage | Start | End | Why This Boundary | Confidence |
|---|---|---|---|---|
| **1 (this file)** | **1945** *(claimed)* / **1962** *(documented)* — see the two-row split below | **1970-10-08** | Opens where the registrant itself says its history opens and closes where the first **outside** capital event is dated inside an audited note | **Medium** (see the ranked-candidate table) |
| 2 (proposed opening) | **1970-10-09** | — | First day after a public offering is on the record; FY1971 is the first year-end **named in the same note**, and FY1968–FY1971 are the four year-ends the company itself labels **pro forma**, outside every opinion | Medium |
| Rejected (i) | — | 1970-08-27 / 1970-09-03 | The NASDAQ listing / first-trade cluster as the close | **High (that it fails)** — UNKNOWN (dates not on disk; recorded as UNTRIED, not resolved) |
| Rejected (ii) | — | 1972-02-29 | FY1972 report as the earliest surviving document, so the stage would be what the archive can prove | High — this is an **archive** boundary, not a business boundary; it would delete the stage |
| Rejected (iii) | 1950 | — | Any date anchored to the later Ben Franklin **wholesale** relationship rather than the first retail store | Low; rejected on single-lineage grounds |

### B-1 The start: two dates that are not the same kind of date

The **1945** start is **registrant-retrospective**: the earliest attestation in the corpus is
**FY1973's "twenty-eight year history"**, which is an arithmetic back-cast (1973 − 28 = 1945) made
**28 years after the event by the entity whose history it is**. Under §3's filing-lineage rule that
is **one source**, and it is a *claimed* origin. **1962** — Walton's first Wal-Mart store — is the
rival, and it must be defeated or accepted **on the evidence**, not on common knowledge. The full
argument, with the document and line for each candidate, is at `## STAGE BOUNDARY JUSTIFICATION`
detail table below (§B.1a) and at §C.0.

### B-2 The end: what the FY1972 note actually dates

**1970-10-08** is preferred because it is **the only end-of-window candidate that is dated inside an
audited financial statement note**, in a form whose words are the registrant's and whose opinion is
the auditor's: the **200,000-share public offer**. Its weakness is disclosed, not hidden: it is the
same lineage as everything else positive on the company, and it is a **1972 document reporting a
1970 event** — `RETROSPECTIVE SOURCE` under §6 in the weak sense (two years, audited comparative)
and in the strong sense for the pre-1968 years.

### B-1a The start candidates, by attestation geometry (the detail table promised at §B-1)

**Why a separate table.** A boundary argued as "the oldest date anyone repeats" is not argued at all. What
follows is the distance between each event and the earliest document on disk that carries it, so the reader
can see the shape of the evidence rather than the size of the claim. Ranked narrative and the loser
recorded as a live conflict are at §C.0; this table is the arithmetic behind them.

| Variable | Value | Source | Confidence |
|---|---|---|---|
| 1945 (claimed origin) | Attested first by **S0102, 1973-03-20** ("twenty-eight year history") — **28 years after the event**, by the entity whose history it is; then five more dated printings S0103→S0109 (FY1974's "twenty-nine year history" → FY1980's "Beginning in 1945, with a Ben Franklin franchised store in Newport, Arkansas"). **Independent origins: 0.** Distance grows from 28 to 35 years as the series runs, which is the wrong direction for evidence | `WALMART_AR_1973.txt` … `_1980.txt`; A3-028/A3-029, COR-A3-10 | High (that the geometry is this); **Low** that the event is documented |
| 1955 (first named premises) | **S0105, 1976-03-26** — 21 years, one lineage, and the sentence describes an **office above a store**, not a venture | `WALMART_AR_1976.txt` (A2 W-49) | Medium (as a 1976 assertion) |
| 1962 (first Discount City) | **S0103, 1974-03-21** is the earliest document on disk that dates it at all ("opened in Rogers, Arkansas in 1962"); **12 years**; the *month* waits until **S0104, 1975-03-28**. Verified negatives: `WALMART_AR_1972.txt` and `WALMART_AR_1973.txt` each print **"1962" 0 times and "Ben Franklin" 0 times** | S0103, S0104; the two greps re-run on this pass | High (geometry); **Low** (the event) |
| 1970-02-01 (pooling) | **S0101, 1972-03-22** — 2 years, audited note, names **Walton Enterprises, Inc.** and "the various subsidiaries" | S0101 Note 1 | High |
| **1970-10-08 (adopted close)** | **S0101, 1972-03-22** — 17 months, inside the audited notes: "200,000 shares sold in public offering October 8, 1970". The **only** day-precision public-capital date in the corpus. Its corroborators are **same-lineage** (S0103's "In October 1970 … became traded in the over-the-counter market"; S0108's "publicly-owned since October, 1970") and one is **structurally independent but negative**: the SEC's 31-Dec-1970 exchange-issuer register omits the company (A5-04) | S0101 note; S0103; S0108; A5-04 | High (the note prints it); **Medium** (as a boundary) |
| The losing candidate, kept live | **1970-02-01** — earlier, better documented, and *not* a public-capital event. Recorded here so Stage 2's opening does not silently re-adjudicate it | S0101 Note 1 | High |

**STATUS: WRITTEN 2026-09-25**

---

## A. EXECUTIVE STATE SUMMARY

STATUS: WRITTEN 2026-09-25

### A.1 What the registrant's own nine reports state

**The attested series.** Nine printed Wal-Mart Stores, Inc. annual reports are on disk, **FY1972 →
FY1980 continuously with no missing year** (A3-001), each signed by **Arthur Young & Company, Tulsa,
Oklahoma**. Register source ids **S0101–S0109** = `sources/periodicals/WALMART_AR_1972.txt` …
`_1980.txt` (publication dates 1972-03-22 → 1980-04-01). Earliest year carrying ANY figure anywhere in
the corpus: **FY1968**. FY1962–FY1967 are **EMPTY** — no sales, no store count, no earnings, no balance
sheet, no square footage, no headcount in any of the nine documents (A3-039).

**Reading rule before any row below.** A value printed in the report *for that fiscal year* is
**CONTEMP**; a value printed in a *later* report's summary or comparative column is **RESTAT (in
`document`)**. Nine printings of FY1974 in FY1975/76/77/78/79 remain **one lineage** (§3 filing-lineage
rule); they are version evidence, not corroboration, and the independent-lineage count for every number
here is **1** (A3 §7.2(c), re-tested and unchanged by A5).

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Net sales, FY1968 | **$12,618,754** — RESTAT (in S0101, 1972-03-22); only printing anywhere; earnings row of the same table is captioned *pro forma* by the company | `WALMART_AR_1972.txt` "5 YEAR FINANCIAL SUMMARY / YEARS ENDED JANUARY 31" (S0101) | Medium (one printing, 1972-dated about 1968) |
| Net sales, FY1969 | **$21,365,081** — RESTAT (in S0101); only printing anywhere | S0101, same table | Medium |
| Net sales, FY1970 | **$30,862,659** — RESTAT (in S0101); later printed in S0103 (1974) and S0107 (1978, in thousands) | S0101; A3 Table S1 | Medium |
| Net sales, FY1971 | **$44,286,012** — RESTAT (in S0101); **no FY1971 report exists** | S0101 | Medium |
| Net sales, FY1972 | **$78,014,164** — **CONTEMP** | S0101 | High (as-filed) |
| Net sales, FY1973 | **$124,889,141** — **CONTEMP** | `WALMART_AR_1973.txt` (S0102) | High (as-filed) |
| Net sales, FY1974 | **$167,560,892** — **CONTEMP**, read from the Five Year Progress Report and NOT from the audited statement pages, whose FY1974 own-column is missing and which misprint FY1973 as "$124,059,141" (A3-002) | `WALMART_AR_1974.txt` (S0103) | High (as-filed) |
| Net sales, FY1975 | **$236,209 thousand** — **NOT PRINTED on the FY1975 text layer**; the FY1975 Five Year Summary carries four values against five column heads and drops FY1975's own column everywhere (A3-003). Printed 236,209 in S0105/S0106/S0107 and as $236,209,000 in S0108 | `WALMART_AR_1975.txt` (S0104) + later prints | **Medium, and open conflict U-A3/1**: the 2-vs-3 digit ambiguity **$226,209 / $236,209** is recorded in the file's own header and is NOT resolved here |
| Net sales, FY1976 / FY1977 / FY1978 / FY1979 / FY1980 | **$340,331k / $478,807k / $678,456k / $900,298,000 / $1,248,176k** — each **CONTEMP** in its own report | S0105, S0106, S0107, S0108, S0109 | High (as-filed) |
| Stores at year end | FY1968 **24**, FY1969 **27**, FY1970 **32**, FY1971 **38** — all RESTAT (FY1968/69 in S0102's "Six Years at a Glance"; FY1970 in S0101). FY1972 **51**, FY1973 **64**, FY1974 **78**, FY1975 **104**, FY1976 **125**, FY1977 **153**, FY1978 **195**, FY1979 **229**, FY1980 **276** — each **CONTEMP** | S0101–S0109; A3 Table S2 | High (as-filed years), Medium (FY1968–FY1971) |
| **Composition of the fleet at the closing boundary** | **"On January 1, 1970, eight years after the opening of the first Wal-Mart Discount City store in Rogers, Arkansas, the Company owned and operated 18 Wal-Marts and 14 Ben Franklin variety stores in a four-state area, with sales totaling $31 million"** — a 1980-dated statement of a 1970 state. Independently printed, same lineage, in the FY1972 President's letter: "our eighteen Wal-Mart stores that already existed as of February 1, 1970 and were not expanded had a 17% increase in sales over 1971" | S0109 (`WALMART_AR_1980.txt`, "Wal-Mart's Past — Foundation for the Future"); S0101 (President's message, 1972-03-22) | High that both documents say it; Medium that 1970-01-01 state is right (32-store FY1970 count and 18+14=32 **agree**, which is an internal check, not a second source) |
| Earnings basis FY1968–FY1972 as printed | The FY1972 table's rows are captioned **"Pro forma net income"** and **"Pro forma net income per share"**: $.09 / $.12 / $.23 / $.30 / $.47 for FY1968→FY1972. **The word "pro forma" is the registrant's own label** and means the registrant group did not exist for those years — it begins at the **1970-02-01** pooling (A3-020, W-04) | S0101, S0102 (`WALMART_AR_1973.txt`), S0103 | High (as printed) |
| Total assets, FY1978 — **THE SERIES BREAKS HERE** | **$206,691 thousand AS PUBLISHED** in S0107; **$251,865,000 AS RESTATED** in S0108 (+45,174,000), because SFAS-13 capitalised leases: long-term capital-lease obligations **10,904 → 59,003 thousand**, equity **98,943 → 96,482 thousand**, retained-earnings restatement **(2,461,000)**. S0108 prints: "All financial information has been restated to reflect the retroactive application ot [sic] Statement of Financial Accounting Standards No. 13" | S0107, S0108; A3-033/A3-036, U-A3/6 | High. **Register rule inherited: any asset-turn, debt/assets or total-asset growth figure computed across 1978-01-31/1979-01-31 is invalid** |
| **Dividend claim, REFUTED on the page** | The FY1980 ten-year summary's dividend row (**1976 $.09 / 1977 $.11 / 1978 $.19 / 1979 $.25**) is refuted for 1976–1979 by each year's own document: **$.065 (S0105), $.085 (S0106), $.16 (S0107, and quarterly .025/.045/.045/.045), $.22 (S0108, four quarters at $.055)**. No split factor reconciles the two series ($.09/$.065 = 1.38 is not a split) — COR-A3-04. First evidenced dividend row at all: **FY1974 $.025**, printed only in S0107's nine-year table, i.e. **RESTAT** | S0109 (refuted row) vs S0105/S0106/S0107/S0108 | High that the four-year row is refuted; the FY1980 row is **kept on the record as printed**, not deleted |
| Stock splits | Three two-for-one events are printed in this corpus, **not one**: **1971-06-11** (1,500,000 shares issued, par charge 150,000), **1972-04-05** (3,000,000 shares to be issued, par charge 300,000) — both inside S0101's own capital note; and **1975-08-19** (6,687,789 shares, per S0105 Note 4, the only one falling in the restatement dispute of A3 Table S3) | S0101 note "Capital in excess of par value at January 31, 1972 includes the following transactions"; S0105 | High. See §D correction note **D-R09c** — this contradicts this volume's earlier single-split row |
| The closing-boundary event, verbatim | **"Excess of net proceeds over par value of 200,000 shares sold in public offering October 8, 1970 — 3,010,467"** — the only day-precision public-capital date any Tier-1 document on disk puts inside the window, and it sits **inside the audited notes** | S0101 (`WALMART_AR_1972.txt`) | High that the note says it; Medium that the note is a 1972 document reporting a 1970 event |
| Net proceeds per share, FY1972 note (DERIVED) | **$15.15** = (3,010,467 excess over par + 20,000 par at $.10 × 200,000) ÷ 200,000. Par of $.10 is itself evidenced in the same note (1,500,000 shares → 150,000; 3,000,000 → 300,000) — **arithmetic shown, DERIVED, not observed** | DERIVED from S0101 | High as arithmetic. **UNKNOWN as gross offer price**: no local document prints a gross price or an underwriting spread, so $15.15 is **not** reconcilable here with the company page's "$16.50 per share". The gap is recorded, not back-solved |
| Market status | S0103 (1974-03-21): "In October 1970, Wal-Mart Stores, Inc. became a publicly-held corporation and became traded in the **over-the-counter** market. August 25, 1972, the Company's stock was listed and began trading on the New York Stock Exchange" (A3-019) | S0103 | High. Any 1972-08-25 price break is a **venue change, not a stock event** |
| Square footage | Total store/retail space is **not printed before FY1976**: 5,295,000 (S0105), ≈6,500,000 (S0106's own words), 8,500,000 (S0107), 10,200,000 (S0108), 12,600,000 (S0109). FY1972–FY1975 print **additions only** (e.g. 604,000 sq ft FY1972; 1,083,326 sq ft FY1975 "a record for new store space in a single year"). S0109's "less than a million square feet" at 1970-01-01 is a **1980 sentence about 1970**, and the addition series must not be cumulated backwards | S0105–S0109; A3 Table S2 | High (FY1976+); **UNKNOWN** for any pre-FY1976 total |
| Headcount | FY1972 "some 2,300 who today make up our Wal-Mart world" (S0101, President's letter, 1972-03-22); FY1974 4,500 (chart, S0103); FY1975 "approximately 5800 associates" (S0104); FY1977 "10,000 associates" (S0106, stated twice); FY1979 "over 17,500 associates" (S0108); FY1980 "more than 21,000 associates" (S0109). **FY1973, FY1976 (chart OCR-damaged) and FY1978 = UNKNOWN** — recorded as a gap, not as zero | S0101–S0109 | Medium (company-stated, basis of "associates"/"employees" never defined in any document) |
| Fiscal-year convention | All nine reports state a **fixed 31 January** year end; **no report anywhere states a 52/53-week convention** (A3-018). Consequence: calendar-fixed years, so no growth rate in this stage is distorted by a shifted year end; the only length effect is the leap day inside FY1969, FY1973 and FY1977 (+0.27%) | nine files, heading lines | High |
| Auditor qualifications inside the window | FY1974 unqualified (1974-03-21); FY1975 **qualified by exception for the change in the method of determining inventories (LIFO adoption)**; FY1977 and FY1978 unqualified; FY1979 **qualified by the retroactive SFAS-13 lease-restatement clause** | S0103, S0104, S0106, S0107, S0108 | High |
| Company-page figures, calendar-year trap | The company's own undated page: "1967 — The Walton family owns 24 stores, ringing up $12.7 million in sales" = **FY1968** as filed, mislabelled by calendar year; "1972 — 51 stores, sales of $78 million" = FY1972 as filed. The page's numbers are the reports' numbers with a one-year labelling shift on the earlier entry | `sources/EXTRACT_corporate_walmart_history_timeline.md`; A3 §0 fiscal-basis note | High that the shift exists; the page itself is **company self-narrative** and adds no lineage |

**What this table cannot say.** It says nothing about FY1962–FY1967, nothing about the 1945 or 1946
events, and nothing about any price, customer, town reaction or rejected option anywhere in the window.
Those silences are the subject of §A.2 and §S (part_2); they are not smoothed by the density of the
FY1968–FY1980 rows.

### A.2 What evidence existed, and what stayed UNKNOWN

**The four families, named, with what each returned.** Per §14 rule 6 a depth verdict may not rest on
two families. All four were reached for this company:

| Family | What is on disk | What it returned for 1945–1970 |
|---|---|---|
| (a) Filings | `sources/EDGAR_submissions_CIK0000104169_002_1994-2012.json` (1,409 filings) | **Nothing before 1994-02-14** (an SC 13G/A); first electronic 10-K 1995-04-27 (W-02). The 1970 registration statement is **paper at the SEC Reference Room / National Archives, not on disk** — so the stage's closing date cannot be read from the filing that created it |
| (b) Web archives | `probe_wayback_walmart*_exact.txt` | Earliest root capture **1996-12-29**; no pre-1990 artifact (W-04). The `matchType=prefix` sweep returned **HTTP 504 — an upstream capacity failure, NOT a null**, and is recorded UNTRIED, not as absence |
| (c) Periodical corpora | Business Week annual indexes 1962–1971 (`sim_business-week_*`), *Stores* (NRDGA/NRMA) monthly 1945–1961 + annual indexes 1971/1972/1974/1975; extracts at `sources/periodicals/BUSINESSWEEK_INDEX_1962-1971_EXTRACT_walmart_and_sector_hits.txt`, `STORES_NRDGA_1946-1972_EXTRACT_walton_and_discount.txt` | **Sector evidence exists; company evidence does not.** Ten BW index years and five *Stores* apparatuses print **0 occurrences of "Wal-Mart"** while carrying dated sector stories — "Discount store dropouts" p.101 Oct.6 1962; "Shake-out among discounters seen as chain files in bankruptcy" p.83 Oct.27 1962; "Discounters strive to ride out storm: fast-growing $6-billion industry is facing a major shakeout" p.78 Dec.1 1962 (A4-01…A4-15, S0112–S0126). The **decisive empty row** in A4's own comparison table: "Wal-Mart named in ANY press figure, 1962–1980 — **UNKNOWN, no figure recovered**" |
| (d) Government statistical / register | `sources/gov_docs/SEC_SecuritiesTradedOnExchanges_asof-1970-12-31_IA-securitiestraded1970unit.txt` (941,197 B, 153,481 words read whole) + the SEC *Statistical bulletin* Nov 1970 (47,206 B, whole) | **Both print the company zero times.** The register's W-block legibly reads WALGREEN … WALWORTH, so OCR loss is excluded (A5-04). The Bulletin's only issuer-naming table is a fixed sample of "100 SELECTED COMMON STOCKS" on the NYSE, in which an unlisted Arkansas retailer could not appear (A5-03) |
| (e) Documentary / auction | `sources/periodicals/STUB_LEAD_samwaltoninsides00vanc.md`, `STUB_LEAD_DTIC_ADA345567.md`, `walmart_museum_page.html` | No founding document reached. The 1950 bill of sale the museum claims to hold (W-21) and the 1962 grand-opening flyer (W-20) are **leads whose bytes are not in this repository** |

**Where the independence rule bites, and one place it does not.** Every positive statement about this
company inside the window traces to **one lineage** (S0101–S0109 + Arthur Young's opinions on them), and
A5 was the test of whether a third-party publisher could move the count. It could not, and the reason is
structural, not unlucky: **even a positive naming inside the SEC Bulletin would have been evidence of
registration, not of the company**, because that series republishes registrant filings as aggregates
(A5-03's own `independence_note` reasoning). The single datum that DOES now have a genuinely independent origin is a
**negative**: "not exchange-listed as of 31 December 1970" (A5-04). It corroborates the registrant's own
"traded in the over-the-counter market" (S0103) and it corroborates **no dollar, no store and no rate**.
A4's *Stores* 1971 annual index zero is separately weak and is reported as weak: that volume is a
subject-only apparatus (`wal-mart` 0 · `walton` 0 · `ben franklin` 0 · `variety` 0 · `discount` 0), which
proves the index did not carry the subject, not that the trade ignored the firm (A4-18).

**Precision note on the header's "no document dated inside the 1945–1968 span at all".** Read narrowly,
and corrected here rather than left to mislead: dated third-party documents inside 1945–1968 **do** exist
on disk — the *Stores* monthly run 1945–1961 (205 digitised items with text layers, A4-16) and the BW
indexes for 1962–1968. What does not exist on disk is **any document dated inside 1945–1968 that names
this company**, and **any company document of any kind before 1972-03-22**. That is the finding; the
stronger wording would overstate it.

**What stayed UNKNOWN, item by item.**
1. **Every FY1962–FY1967 metric.** EMPTY in all nine reports; not restated later, because S0103's
   five-year table starts at FY1970 and S0107's nine-year table starts at FY1970 (A3-039).
2. **The 1970 offering's terms as filed.** No gross price, no proceeds line, no underwriter, no
   registration statement text. $16.50 exists only on an undated company page; **$16.50 and the derived
   $15.15 net are not reconciled and no local document licenses a bridge between them.**
3. **The 1962 opening's observable facts.** Opening-day takings, prices, crowd and stock are
   **UNTRACEABLE**: no 1962 press item in hand names the firm, and the flyer was never retrieved. The
   claim "opening-day sales $1,402" is a **memoir-lineage item** classified FOUNDER CLAIM (retrospective)
   and there is **no pre-1992 source for it anywhere in this corpus**.
4. **The 1945 and 1946 events themselves.** Six dated company restatements (FY1973→FY1980) attest *the
   telling*; nothing attests *the told*. No franchise agreement, lease, deed, partnership instrument or
   register entry from 1945–1946 is in this evidence set.
5. **Which legal person did what.** See §B.0: the names, dates and states of the predecessor
   subsidiaries "appear nowhere" in the reports (A2 §Data gaps); "Wal-Mart, Inc., 15 March 1962" is
   **unattested**; the 1969 incorporation is **undated and uncited** on the page that asserts it.
6. **Whether the trade press's silence is informative.** 6 of ~200 *Stores* monthly issues have been
   read. The remaining ~194 are **UNTRIED**, so the only licensed sentence is "the issues sampled do not
   name it", never "the trade ignored it" (A4-23 perimeter).

**Record-selection null, stated for this stage (§2).** What is unrecoverable *because the survivor's
archive is the one that was kept*: no 1945–1962 internal deliberation; no rejected option (nothing in the
corpus records a declined alternative to the 1962 format, a failed site, or a lost lease as a dated
document — the lost-lease story exists only in a 1992 memoir); no contemporaneous price or sales record
from inside any store before FY1968; no independent count behind any company self-report; and no
contemporaneous third-party witness to the founder's decision-making at all. The asymmetry is the point:
the corpus is **dense from 1972 and mute before it**, and density after the float must not be read as
evidence that the pre-float years were legible to anyone in them.

---

## B. FOUNDER / COMPANY STATE

STATUS: WRITTEN 2026-09-25

### B.0 The same entity at the two ends of the window

**The question this section has to answer honestly is not "which company was it" but "how many legal
persons does the record actually name, and at which end does the naming fail."** It fails at the open end.

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Registrant at the close of the window | **Wal-Mart Stores, Inc.**, issuer of the stock of which 200,000 shares were sold in the 1970-10-08 public offering | S0101 note ("Capital in excess of par value at January 31, 1972 includes the following transactions") | High (single lineage, audited note) |
| **State of incorporation** | **UNKNOWN — not stated in any of the nine reports.** A string-search for "Delaware" across `WALMART_AR_1972…1980.txt` returns **zero** hits; the only "Delaware" occurrences anywhere in `sources/` are a navigation list of U.S. states inside `walmart_museum_page.html` and an unrelated SEC ticker file. **This volume's header line asserts "a Delaware corporation; incorporated 1969-10-01"; no local document supports either the state or the day**, and the claim is flagged at §D note **D-R03c** and in the assembler's report rather than silently repeated here | nine files, negative search; `sources/periodicals/walmart_museum_page.html` | **UNKNOWN** |
| 1969 incorporation | The company's own page states only "**1969** — The company officially incorporates as Wal-Mart Stores, Inc." — **year only, no month, no day, no state, no citation**. A2's data-gap row records the claim as "undated and uncited" | `sources/EXTRACT_corporate_walmart_history_timeline.md`; A probe W-11; A2 §Data gaps "Entity names and dates" | Medium that the page says it; **Low/UNKNOWN for the event** |
| "Wal-Mart, Inc., incorporated 15 March 1962" | **UNATTESTED in this corpus.** It is Tier-4 folklore; the Arkansas Secretary of State and Benton County records that could settle it are **UNTRIED** | A probe W-07, U-1; A2 §Data gaps; `B_periodical_retest.md` §Paywalled/on-paper leads | **UNKNOWN** — the date is not adopted anywhere in this volume |
| The registrant group's consolidated beginning | **1970-02-01**: an exchange of common stock accounted for as a **pooling of interests**, in which the principal shareholder **Walton Enterprises, Inc.** transferred shares in "**the various subsidiaries**" plus the assets of certain related businesses, subject to liabilities including an assumed **$968,876** bank note | S0101 Note 1 (W-04); also printed in the same note's capital breakdown as "Excess of paid-in capital of pooled companies … at February 1, 1970 $1,470,139" | High (as-filed, audited note) |
| Names of the predecessor subsidiaries | **None is named.** The reports say "the various subsidiaries" and never enumerate them. A2's register: the names, dates and state of the predecessor subsidiaries "appear nowhere in these four reports" | A2 §Data gaps; S0101 | High (that the record is silent) |
| Was the group ONE operating company at the close? | **No, on the tax evidence.** Through FY1972 "The Company and its subsidiaries file separate income tax returns", the provision being "the approximate combined amounts of the taxes currently payable by the individual corporations"; a **consolidated** federal return was filed only for the year ended 1973-01-31. The IRS had extended proposed assessments to the years ended 1969-01-31 and 1970-01-31 | S0101 Note 6 (W-21); S0102 Note 6 (W-40) | High. **INFERENCE, Medium:** separate returns prove multiple legal persons in 1972, three years after the pooling; they do not prove which of them ran the 1962 store |
| The entity operating in 1945–1962 | **No legal person is identified at all.** The FY1978 report is the only document that names a form of organisation for the pre-1962 business, and it does so retrospectively: brothers "who had formed [a] partnership in 1946" | S0107 (narrative); S0104, S0106, S0108, S0109 for the 1945/1946 sequence | **Low; FOUNDER CLAIM / retrospective, one lineage.** No partnership deed, firm name, or acquisition date exists in this corpus |

**Finding: the window's two ends are not joined by any document.** At the close there is a named issuer
with an audited capital account; at the open there is a franchise relationship described decades later by
the entity that grew out of it. The entity-identity claim that the Stage-1 span is one company's history
is therefore **carried by the registrant's own retrospective narrative — and by nothing else** (§3
independence rule). What is *not* inference: the 1970-02-01 pooling and the 1970-10-08 offer are printed
in the same set of notes, in the same document, twelve months after the offer, and the notes agree that
the group as consolidated begins at the pooling. What must not be asserted: that the 1945 Newport
operator and the 1970 registrant are the same firm in any legal sense, or that the reports say they are —
the reports say "the Company's origin … predates the opening of the first Wal-Mart store … by 17 years"
(S0109), which is a **narrative** claim of continuity made in 1980, not a corporate-record one.

### B.1 The founder at the boundary, on the record that survives

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Founder, as named by the registrant | "The Company's founder and present Chairman of the Executive Committee of the Board of Directors, **Sam M. Walton**" | S0104 (`WALMART_AR_1975.txt`, company profile) | High (as a company statement, FY1975) |
| Offices actually attested in-window | **Sam M. Walton — Chairman of the Board and President**; **J. L. Walton — Senior Vice President**; **S. Robson Walton — Secretary**; with Ferold G. Arend and Ronald Mayer among directors | S0103 "Directors and Officers" page | High. **The family is attested inside the audited document, not only in the lore** |
| The only founder-signed document in the corpus | The FY1972 President's message, **signed Sam M. Walton, 1972-03-22** | S0101 | High (the signature block is on disk) |
| **Newport is in ARKANSAS — and the project's own "correction" was the error** | Five documents place the 1945 start in **Newport, Arkansas**: S0104 "opened his first Ben Franklin variety store in Newport, Arkansas in 1945"; S0106 "opened in 1945, in Newport, Arkansas by Sam M. Walton"; S0107 "1945, when Sam Walton opened his first Ben Franklin franchise operation in Newport, Arkansas"; S0108 "In 1945, Sam Walton opened his first variety store, under the Ben Franklin franchise, in Newport, Arkansas"; S0109 "Beginning in 1945, with a Ben Franklin franchised store in **Newport, Arkansas**, the Walton brothers assembled a group of fifteen variety stores" | S0104–S0109; A probe's own supersession note | **High that the registrant placed it in Arkansas from 1975 onward; Low that any 1945 event is documented.** The 1945–50 Newport years sit in **Mississippi County, Arkansas**, which is the county A2 names for the untested public-records route |
| Two internal project errors about this place-name, recorded so they are not re-imported | (i) the 2026-09-23 probe asserted vintagebentonville's "Newport, Arkansas" was wrong and "Newport is in Nebraska" (W-19) — **that fix is itself the error** and the probe's own supersession note retracts it; (ii) **A4's dossier prose repeatedly writes "Newport, Kentucky" / "the year Sam Walton's Newport, Kentucky experiment ended"** (A4-16, A4-18, A4-23) — a third wrong state, uncorrected in A4, contradicted by S0104–S0109. Neither dossier wording is adopted here | `A_chronology_feasibility.md` W-19 + its SUPERSEDED note; `A4_independent_periodicals.md` L278, L332-334, L424 | High (both errors are on the page and locatable). **Reported as a named finding to the register owner** |
| The decoy that makes the geography trap worse, not better | Business Week's 1962 index does carry a town entry "**NEWPORT, Ky. — Boycott of Communist-made goods … p38, Dec.15**" — a Kentucky municipality, unrelated to the company. Its presence proves the index carried Newport entries when it had a story to carry, which is what makes the zero for Wal-Mart an **informed** silence (§A.2) | S0112 (A4-17, offset @1,067,884) | High |
| **Co-operator at the 1962 opening, named by the company** | S0109: "The first Wal-Mart Discount City store was opened in 1962 in Rogers, Arkansas **by Sam M. Walton and his brother James L. Walton**", and its caption calls them "**Wal-Mart's co-founders**". The same person appears in S0106/S0108 as "his brother, **J. L. 'Bud' Walton**", and as Senior Vice President in S0103's officer list | S0109; S0106; S0108; S0103 | High that the FY1980 report says it; **Low for the 1962 event** (1980-dated, one lineage). **This directly contradicts the single-founder form of the company's own web page** ("Sam Walton opens the first Walmart store"), and the contradiction is recorded as a live conflict at §U (part_2), not resolved by preference |
| The founder's later memoir | *Made in America* (Walton & Huey, 1992) is the dominant source of nearly every famous founding detail — prices, the lease loss and its motive, the 1962 "discovery" of discounting, the employee-first anecdotes | `A_chronology_feasibility.md` §Source availability, §Famous claims | **NOT ADMITTED as evidence in §§A–D.** It is **FOUNDER CLAIM (retrospective memory)**, single lineage, and its bytes are not in this repository; where it is the only witness, this volume writes **UNKNOWN** instead |

**What the founder's record cannot tell us.** Not one document in this corpus records the founder
*choosing* anything in 1945, 1950, 1955 or 1962. The earliest first-person-ish act on disk is a signed
stockholder letter of March 1972 about a fiscal year that ended eleven weeks earlier. Everything between
1945 and 1970 that is attributed to him arrives as **institutional prose in the registrant's own annual
reports, 1974–1980**, or as **memoir**. The consequence for §N (part_2) is that the decisions table will
be built from *observable states* (store counts, square footage, DC capacity, banners carried) rather
than from stated intent, and the absence of stated intent is itself recorded, not paraphrased.

### B.2 The firm at the boundary

**Open end (1945 → 1962): a franchised variety business, described but never inventoried.**

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Stated composition | "Between 1945 and 1962, they assembled a group of **fifteen successful Ben Franklin stores** which served as the base for what was to become Wal-Mart Stores, Inc." — S0104. S0108 says "**15 Ben Franklin stores between 1946 and 1962**"; S0109 says "a group of fifteen variety stores, most of them in small towns in **Arkansas, Missouri and Kansas**" | S0104, S0108, S0109 | High (stable across four reports); **Low for the underlying facts.** Note the **internal one-year disagreement on the start of the count** (1945 vs 1946) and the label drift "Ben Franklin stores" → "variety stores" |
| Which fifteen, where, when acquired | **UNKNOWN — no document in this corpus lists them.** Nothing states which of the fifteen entered the registrant group, on what date, on what terms, or whether all fifteen did | nine-file negative search | **UNKNOWN**, recorded as a gap in §S (part_2) |
| Stated character of the business | "Until 1962, the Company's business was devoted to the operation of **variety stores**" (S0106) | S0106 | High (as a 1977 statement) |
| Earliest pre-1962 date carrying a **named business premises** | 1955 — "The first office was established above **Walton's Family Store** in Bentonville, Arkansas, in 1955" (S0105, W-49). 1976-dated, not 1955-dated | S0105 | Medium as a company assertion made in 1976; **no 1955 document exists** |
| 1950 / the Bentonville lease loss | **No document in this evidence set mentions 1950, a 1950 Bentonville store, a purchase price, a rent, or a lease loss.** The museum's claimed holding of a 1950 bill of sale is a lead with no bytes on disk; the motive clause ("landlord wanted the site for his son-in-law") is memoir-only and **UNTRACEABLE** | A2 §"Where the boundary is NOT defensible"; A probe W-21, §Famous claims | **UNKNOWN / EMPTY within the stated perimeter** — not a corpus null, because county records are UNTRIED |

**Closing end (FY1968 → 1970-10-08): the firm the reports actually let us count.**

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Fleet at the boundary, by banner | **18 Wal-Mart Discount Cities + 14 Ben Franklin variety stores**, four-state area, at 1970-01-01, "with sales totaling $31 million" | S0109; the 18-store figure corroborated **within the same lineage** by S0101's "eighteen Wal-Mart stores that already existed as of February 1, 1970" | Medium-High as company state; **one lineage** |
| Total store count | **32** at FY1970-01-31 and **38** at FY1971-01-31 (RESTAT prints in S0101/S0102/S0103/S0107) | A3 Table S2 | Medium |
| Sales | FY1970 **$30,862,659**, FY1971 **$44,286,012** — both RESTAT (in S0101); no FY1970 or FY1971 report exists | S0101 | Medium |
| Capital structure at the boundary | **6,000,000 shares outstanding** at both 1971-01-31 and 1972-01-31; stockholders' equity **$7,840,701** → **$10,748,055**; current ratio 1.87 → 1.65. Par value **$.10** is evidenced inside the same FY1972 note (1,500,000 shares → $150,000; 3,000,000 → $300,000) | S0101 "FINANCIAL HIGHLIGHTS" and Note (capital in excess of par) | High (as-filed FY1972); the 1971 column is a 1972-dated comparative |
| Share of the issuer sold publicly | **200,000 of approximately 3,000,000 pre-split shares ≈ 6.7%** — **DERIVED**: 6,000,000 post-1971-split shares ÷ 2 = 3,000,000 pre-split; 200,000 ÷ 3,000,000 = 6.7%. Arithmetic shown because the documents never state a float percentage | DERIVED from S0101's own rows | Medium (**INFERENCE on the pre-split share base**; the FY1972 report prints post-split shares only) |
| Logistics at the boundary | Distribution Center "more than doubled from 60,000 square feet to 124,800 square feet. This addition was completed **August 15, 1971**" | S0101 President's message | High (as-filed) |
| Organisational acts dated inside the window | FY1971: **14 new stores, 604,000 sq ft**; "A new profit sharing program was adopted by our Board of Directors for all regular Wal-Mart employees"; FY1972 "some **2,300**" employees | S0101 | High (as stated) |
| Format experimentation *after* the boundary, to show the boundary is not a format line | FY1975 fleet = **100 Discount Cities + 2 Family Centers + 2 Sav-Co**; FY1974 "Two Ben Franklin variety stores were sold and four were closed during the year"; FY1978 a **16-store group acquired**, 4 stores closed; FY1979 the remaining Sav-Co closed; the Ben Franklin units "completely phased out" only across the 1970s | S0103, S0104, S0107, S0108, S0109 | High. **This is why 1970-10-08 closes a *capital* stage and not a *business-model* stage** — see §C.0 |
| Trading-area rule the firm stated about itself | FY1975: towns "within a **350 mile radius** of the General Office and Distribution Centers in Bentonville", average community population served **10,000–15,000**, average store ~42,000 sq ft (range 30,000–60,000); FY1980: "towns having populations from **5,000 to 25,000**", average store ~45,000 sq ft, "over 35,000 items" | S0104, S0109 | Medium (company characterisations; the FY1975 and FY1980 population bands **disagree at the low end** and both are kept) |
| Ownership | **No local document states the family's or any holder's percentage.** The only ownership sentence in the corpus is the uncited company page, "The Walton family owns 24 stores" (its "1967" = **FY1968**). Walton Enterprises, Inc. is named as **principal shareholder** and never sized | S0101 Note 1; `EXTRACT_corporate_walmart_history_timeline.md` | **UNKNOWN (percentage)**, High (that a principal shareholder existed and was the Walton-side vehicle) |

**Independence note for the whole of §B (mandatory, §3).** Every row above whose subject is the company's
own state traces to **the same registrant-and-auditor lineage**, and repeating a 1945 sentence in FY1975,
FY1977, FY1978, FY1979 and FY1980 is **five printings of one source**. The one datum in §B with an
independent origin is negative and is recorded as such: the SEC's 31 December 1970 register of
exchange-traded issuers does **not** list the company (A5-04), which is consistent with S0103's
over-the-counter statement and with nothing else in this section.

---

## C. ORIGINAL PROBLEM

STATUS: WRITTEN 2026-09-25

### C.0 The claimed origin versus the documented origin, ranked

**The ranking rule, stated before the ranking.** A candidate is ranked by **(i)** whether any document
*dated in or near the event* carries it, and **(ii)** whether it is a **business** boundary or an
**archive** boundary. It is NOT ranked by how famous it is, and the two rival starts are **not the same
kind of date** — which is precisely why they cannot be averaged or silently merged.

| Variable | Value | Source | Confidence |
|---|---|---|---|
| **RANK 1 — ADOPTED as the stage's open marker: 1945** | **CLAIMED ORIGIN.** Chosen not because it is documented but because it is **the limit of what the registrant itself ever claimed for its origin**, and a stage that opens later would silently delete the company's own asserted beginning. Its documentary basis: FY1973 "twenty-eight year history" (`WALMART_AR_1973.txt` body — the earliest attestation anywhere in the corpus, a 1973−28 back-cast), then five further dated restatements FY1974 ("twenty-nine year history"), FY1975, FY1977, FY1978, FY1979, FY1980 ("Beginning in 1945, with a Ben Franklin franchised store in Newport, Arkansas"). Under §3 this is **one source printed six times** | S0102–S0109; A3-028, A3-029, COR-A3-10; A2 §Boundary proposal row 1 | **High** that the company dated itself to 1945 by 1973 · **Low** that any 1945 event is documented · overall boundary **Medium** |
| RANK 2 — the rival that must be defeated on evidence: **1962 (November, Rogers)** | It is NOT better documented than 1945 — it is only **less retrospectively distant**. The reports date it to **November 1962** (S0104, S0107) while the company's own page dates it to **2 July 1962**; the timeline register carries it as **FOUNDER CLAIM / Low**. It also fails the *boundary* test for a different reason: 1962 is **inside** the founder-state period the stage exists to reconstruct, so adopting it would cut off the 1945 and 1955 anchors the record does contain (A2: "A Stage 1 beginning in 1962 cannot be used") | S0104, S0107; `EXTRACT_corporate_walmart_history_timeline.md`; `timeline.csv` rows 1945 and 1962-11; A2 §Boundary proposal | **Low** for the event; **High** that it is the wrong *kind* of boundary. **The July-vs-November 1962 disagreement is recorded as live conflict U-C0/1 below, not adjudicated** |
| RANK 3: **1955** (Bentonville office above Walton's Family Store) | Earliest pre-1962 date with a **named business premises**, but the sentence is **1976-dated** and the premises is an office, not a venture. Rejected: it is a detail inside the period, not an origin of it | S0105 (W-49) | Medium as a company assertion made in 1976 |
| RANK 4: **1950** (the memoir's Bentonville purchase year) | **REJECTED ON A NULL.** "No document in this evidence set mentions 1950, Bentonville's 1950 store, a purchase price, a rent, or a lease." A boundary can be argued from an absent record only when the absence is *within a stated perimeter*; here county and local print are **UNTRIED**, so the rejection is provisional | A2 §"Where the boundary is NOT defensible"; §A.2 UNTRIED list | **UNKNOWN** — this candidate is **alive on evidence that has never been fetched**, and is listed as such, not as dead |
| RANK 5: **1946** (the brothers' partnership) | S0107 says "partnership in 1946"; S0108 counts the fifteen stores "between 1946 and 1962"; S0106 puts Bud's Versailles, Missouri store in 1946. Rejected: **no instrument, firm name or date is documented**, and adopting 1946 would privilege the second brother's entry over the first | S0106, S0107, S0108 | Low |
| **RANK 1 — ADOPTED as the stage's close: 1970-10-08** | **The 200,000-share public offering**, dated to the day **inside the audited FY1972 notes**: "200,000 shares sold in public offering October 8, 1970". Preferred because it is the only end-of-window candidate with day-precision in a Tier-1 audited document, and because it is a **capital** event that creates its own documentary world (FY1968–FY1971 are labelled **pro forma** by the company; FY1972 is the first year with a report of its own) | S0101 note; A2 §Boundary proposal; A3 Table S1 | High that the note says it; **Medium as a boundary** (a 1972 document reporting a 1970 event, same lineage as everything else positive) |
| RIVAL CLOSE, recorded as the LOSER of this contest and NOT deleted: **1970-02-01** | The pooling-of-interests exchange — the registrant group as a **consolidated entity** begins here, and it is the *earliest* date at which "the company" in the audited sense exists. It loses only on the ground that it is not a **public-capital** event. It stays live: any Stage-2 opening that ignores it will re-open this contest | S0101 Note 1 (W-04); A2 §Boundary proposal "Stage 1 secondary marker" | **High** as a fact; **Medium** as a rival boundary |
| RIVAL CLOSE: **1970-08-27 / 1970-09-03** (pre-offer trade cluster) and **1970-10-24 / 1972-08-25** | The first two are **NOT ON DISK AT ALL** — they remain **UNTRIED**, and this volume declines to assert them. **1972-08-25 IS on disk** and is dated to the day by the registrant (S0103: the NYSE listing) but it is 22 months after the float and belongs to Stage 2. **1970-10-24** is a Business Week cover date, not a company event (S0123) | S0103; S0123; §A.2 | High (that the dates named are not in-window boundaries); **UNKNOWN** for the August/September 1970 cluster |
| **REJECTED LABEL, corrected on this pass: "the first SEC-visible registration"** | The brief for this stage describes 1970-10-08 as "the first SEC-visible registration". **No local document makes it SEC-visible.** A5 read the SEC's *complete* alphabetical register of exchange-traded issuers at 31 Dec 1970 (153,481 words, 941,197 B, whole) and the November 1970 *Statistical Bulletin* whole: **zero occurrences** of the name. And the register's own front matter bounds its universe — "all securities admitted to trading on stock exchanges … except securities exempted under Section 3" — so it **cannot witness Securities Act registration or over-the-counter status at all**. The label is therefore replaced throughout this volume by **"the first public-capital event dated inside an audited registrant note"** | A5-03, A5-04 (dossier-local; their register rows are pending merge, §D.4.6); A5 §Verdict rungs 1–3 | **High** — this is a documented negative, not a stylistic preference |
| Archive boundary (not a business boundary): **1972-03-22** | The date of the earliest surviving document. Adopting it would make Stage 1 = "what the archive can prove", deleting 27 of the 28 years. Recorded so the geometry is visible | S0101 | High that it fails as a business boundary |

**U-C0/1 — the live conflict this section hands to §U (part_2), named here so it is not lost.**
*CLAIM A:* the first Wal-Mart Discount City opened in **November 1962** (S0104, `WALMART_AR_1975.txt`;
S0107, `WALMART_AR_1978.txt`). *CLAIM B:* it opened **2 July 1962**
(`sources/EXTRACT_corporate_walmart_history_timeline.md`, undated company page). *WHY THEY DIFFER:* the
reports' month is the company's own retrospective prose inside an audited document; the page's date is
anniversary curation, and no register, deed, photograph or press item on disk carries either.
*EVIDENCE WEIGHT:* A is Tier 1 but retrospective and one-lineage; B is Tier 1 as artifact, Tier-4-equivalent
as evidence, and uncited. *BEST-SUPPORTED INTERPRETATION:* **neither** — the month is attested by the
registrant, the day is not attested by anyone, and this volume uses "**1962**" unqualified wherever a date
would do work. *RESIDUAL UNCERTAINTY:* total. *CONFIDENCE:* Low on both; **the conflict is NOT resolved
and no average is taken.** (A third variant — Rogers' population "approximately 4700" in S0104 vs
"approximately 5,000" in S0107 — is already registered as **U-A3/8**.)

### C.1 The problem as the registrant states it, in its own words

**Framing rule.** Everything in this subsection is **company self-narrative transmitted 13–35 years after
the events** (S0104 → S0109). It is quoted because the registrant's stated rationale is itself an
in-period *document* about the 1970s firm, even where it is not evidence about 1945–1962. Class per §3.

| Variable | Value | Source | Confidence |
|---|---|---|---|
| The stated end of the pre-1962 business | "Until 1962, the Company's business was devoted to the operation of variety stores." | S0106 (`WALMART_AR_1977.txt`) | High (as a 1977 statement) — **Class: RETROSPECTIVE INTERPRETATION** |
| The stated *lateness* of the change | "the Company did not open its first discount department store until November 1962" | S0107 (`WALMART_AR_1978.txt`) | High (as printed) — **Class: RETROSPECTIVE INTERPRETATION.** Note the construction: the company's own narrative frames 1962 as a *delay*, which is the opposite of the hagiographic reading, and it is kept for that reason |
| What the variety-store base was said to be *for* | "they assembled a group of fifteen successful Ben Franklin stores which served as the base for what was to become Wal-Mart Stores, Inc." | S0104 | High (as printed) — **Class: RETROSPECTIVE INTERPRETATION**, and the only stated continuity mechanism in the corpus |
| The stated *problem* the format answered | **NONE IS PRINTED.** No document in this corpus states a market gap, an unmet customer need, a supply condition or a competitive threat that the 1962 format was built to answer. The reports state what the company *did* and what it *believed*, never what problem it diagnosed | nine-file search; A probe §Famous claims; §A.2 record-selection null | **UNKNOWN — this is a finding, not a gap to fill.** The absence of a stated problem in the only contemporaneous documents is the single most consequential silence in Stage 1 |
| The nearest thing to a stated operating doctrine, as the company gives it for the pre-1962 business | "The Waltons' guiding business principle was threefold: (1) A clean, well-managed store; (2) A cheerful guarantee of complete satisfaction to every customer; and (3) The lowest everyday prices on a wide selection of quality merchandise." — 25 words, quoted as printed in 1980 | S0109 ("Wal-Mart's Past — Foundation for the Future") | High that FY1980 prints it; **Low as an account of 1945–1962 practice** — **Class: FOUNDER CLAIM / retrospective, one lineage** |
| The stated founding purpose of the franchise stores | "The Walton-owned Ben Franklin stores had a unique philosophical base: service to the community by participation in civic projects beneficial to its citizens." | S0109 | High (printed); **Class: RETROSPECTIVE INTERPRETATION** |
| The stated "co-founder" operating principles, 1980 | "All associates shall be considered equal in importance to the Company's successful operation; every customer shall be treated fairly and courteously; each goal set by the Company shall be predicated on its responsibility to offer the highest quality of merchandise at the lowest possible price." | S0109 | High (printed) — **Class: RETROSPECTIVE INTERPRETATION.** "Their founding Operating Principles remain unchanged" is a 1980 claim about an unbounded prior period and is not admitted as evidence of 1945–1962 practice |
| The founder's own contemporaneous framing, 1972 — the only one available | "Our fiscal year ending January 31, 1972 must be considered Wal-Mart's best ever… Full credit must go to our dedicated and loyal employees — some 2,300 who today make up our Wal-Mart world." | S0101 (President's message, signed 1972-03-22) | High (as-filed, signed) — **Class: FOUNDER CLAIM, CONTEMPORANEOUS**, and note what it is *about*: a year, a headcount and a result — not an origin |
| The registrant's own statement of its market position, 1980 | "undisputed claim to the title, 'Fastest-Growing Regional Discount Chain in America.'" | S0109 | High (printed) — self-award, no external validation anywhere in the corpus; **the phrase is quoted as a claim about the 1970s and is NOT imported backwards into 1962–1970** (§2) |
| Whether anything *outside* the registrant stated the company's problem | **NO.** Business Week's indexes for 1962–1971 and the *Stores* apparatuses carry **zero** Wal-Mart entries while printing dated sector distress stories ("Discount store dropouts" p.101; "Shake-out among discounters … bankruptcy" p.83; "$6-billion industry … facing a major shakeout" p.78, Dec.1 1962). Those are **market-state facts for §H (part_2)** and are **NOT admitted here as evidence of what the founder faced or knew** (§2 firewall) | S0112; A4-01…A4-05; registered as **U-A4/3** | High (independent publisher, dated printed indexes) |
| The company's curated page on its own before-1962 past | **Silent.** `corporate.walmart.com/about/history` begins cold at July 1962 with "no Newport … no 1950 Bentonville store, no lease-loss story, no Bud Walton, no Plaza store"; and A4's *Stores* 1961-12 issue shows the affiliated trade body's own journal describing *other* members' discount ventures ("Nichols Discount Cities since 1958") while never naming Walton's. **The self-narrative's omission of the very years the annual reports narrate is a finding about curation, and it means the two company artifacts cannot be counted twice** | `EXTRACT_corporate_walmart_history_timeline.md` §Documented absences; A probe W-15; S0133 | High (documented absence on a document on disk). **Independence: the page and the reports share one corporate record — one source (§3)** |

**So what — and what it does not show (interpretive coda, §16 duty).** The registrant's own words give a
*sequence* (variety stores → 1962 discount city → 1970 public offer) and a *doctrine* (price, service,
associates), and they never give a *mechanism*: no document states why a variety-store operator in a
four-state area converted a 1962 experiment into a repeatable format, and no document states what would
have falsified it. Mechanism therefore is **UNKNOWN**, and the honest shape of §C is that the "original
problem" of this stage is **reconstructed from observable states (§B.2, and the store/space/DC series in
§P, part_2) and not from intent** — a company that described its own beginnings as a set of principles
held, in its telling, "unchanged", is a company whose archive supplies continuity of language but not
continuity of reasoning. Alternative explanation retained: the absence may reflect only that the
1972–1980 report genre had no place for a founding *rationale*, which would make the silence a property of
the form rather than of the firm — **that alternative cannot be tested on this corpus, and is recorded as
UNTRIED at §S (part_2)** rather than dismissed.

---

## D. FIRST EXPERIMENT

STATUS: WRITTEN 2026-09-25

**Dated record set (this volume's load-bearing evidence).** Each record is
`Date · Event · Document · Line · Class · Confidence`. Records **D-R01…D-R10** are established from
the local corpus below; **UNTRIED** records name the exact query that was not run against a local
file and are complete answers, not gaps to be smoothed.

| Rec | Date | Event / statement carried | Document (local) | Class | Conf |
|---|---|---|---|---|---|
| D-R01 | 1945 | Claimed origin: post-war franchise working arrangement in Newport, **Arkansas** — earliest attestation is a 1973 back-cast, so this is a claimed date not a documented one | FY1973 annual report (via A4/A3 marker set) | RETROSPECTIVE INTERPRETATION | Low |
| D-R02 | 1962 | First **Wal-Mart** store opening — the documented rival start | FY1972+ store/branch lists (A3/A4) | FACT (single lineage) | Medium |
| D-R03 | 1969-10-01 | Wal-Mart Stores, Inc., a Delaware corporation, incorporated | annual-report corporate note | FACT | Medium |
| D-R04 | FY1968 | First year-end carried **pro forma by the company itself**, outside every opinion | FY1972 report comparative table | FACT (of labelling) | High |
| D-R05 | FY1969 | Second pro forma year-end; **outside every audit opinion in the corpus** | FY1972/FY1973 comparatives | FACT | High |
| D-R06 | FY1970 | Third pro forma year-end; the stage's **closing year** | FY1972 report | FACT | High |
| D-R07 | FY1971 | Fourth pro forma year-end; the first year-end **after** the boundary | FY1972 report | FACT | High |
| D-R08 | 1970-10-08 | **200,000-share public offering** — the boundary date, carried **inside the audited FY1972 note** | FY1972 annual report, notes | FACT (single lineage) | Medium |
| D-R09 | 1975-08-19 | The **one and only** 2-for-1 stock split in the attested series; no second split exists in the corpus | FY1976 report onward, comparative share data | FACT | High |
| D-R10 | 1970-12-31 | The SEC issuer register *Securities Traded on exchanges* prints **WALGREEN … WALWORTH and ZERO Wal-Mart**, so the register **cannot witness 1962–1971** | `sources/gov_docs/SEC_SecuritiesTradedOnExchanges_asof-1970-12-31…txt` | FACT (of absence) | High |

**STATUS: WRITTEN (record set) by the first pass; the four correction notes and §§D.1–D.4 below are added
by the completing pass, 2026-09-26. No row above is renumbered or deleted; every correction is printed
beside the row it corrects, per §14 rule 8.**

### D.0 Corrections taken on this pass against the table above

| Note | Row | What the row said | What the local documents say | Class of act |
|---|---|---|---|---|
| **D-R01c** | D-R01 | Source column: "FY1973 annual report (via A4/A3 marker set)" | The attestation is verified **directly in the report's own body**: `WALMART_AR_1973.txt` (S0102) prints "…pany's **twenty-eight year history**. Let's…". A4 is the Business Week / *Stores* corpus and **contains no Wal-Mart text at all**, so it cannot be a marker set for this phrase; the dossier sources are S0102–S0109 and A3-028/A3-029 | Citation pointer corrected; claim itself stands |
| **D-R02c** | D-R02 | "FY1972+ store/branch lists (A3/A4) · FACT (single lineage) · Medium" | **Downgraded and re-pointed.** A string-search of `WALMART_AR_1972.txt` returns **0 occurrences of "1962" and 0 of "Ben Franklin"**; `WALMART_AR_1973.txt` returns **0 of either**. The earliest document on disk that dates the first store is **S0103 (FY1974, 1974-03-21)**: "assemble a group of fifteen Ben Franklin stores and subsequently developed the concept of larger discount department stores. The Company's first Wal-Mart Discount City store opened in Rogers, Arkansas in 1962." The **month** appears first in S0104 ("November 1962"). Register status in `timeline.csv`: **FOUNDER CLAIM, Low, S0104, conflict U-A3/8** — the row's FACT/Medium grading is not supportable and the correct class is **FOUNDER CLAIM (retrospective) · Low** | Class and confidence corrected against the corpus and the register; row kept |
| **D-R03c** | D-R03 | "1969-10-01 · Wal-Mart Stores, Inc., a Delaware corporation, incorporated · annual-report corporate note · FACT · Medium" | **UNSUPPORTED — flagged, not deleted.** No document in `sources/` states a **state of incorporation** or a **1969 date at all**: "Delaware" occurs **0 times** across the nine annual reports, and the only "Delaware" strings in the corpus are a U.S.-state navigation list inside `walmart_museum_page.html` and an unrelated SEC ticker file. The company's own page gives **1969, year only, no month/day/state/citation** (W-11); A2's data-gap row records the predecessor subsidiaries' "names, dates and state" as appearing "nowhere". The correct entry is **Date: 1969 (year, company-asserted) · State: UNKNOWN · Day: UNKNOWN · Class: UNKNOWN · Conf: Low**, and "Wal-Mart, Inc. / 15 March 1962" is **unattested folklore**, not a documented alternative | **Open evidentiary defect handed to the register owner** — see report to orchestrator |
| **D-R09c** | D-R09 | "The **one and only** 2-for-1 stock split in the attested series; no second split exists in the corpus · 1975-08-19" | **Refuted on its own column, and by two documents.** The corpus carries **three** two-for-one events: **1971-06-11** (1,500,000 shares issued, par charge $150,000) and **1972-04-05** (3,000,000 shares to be issued, par charge $300,000), both printed **inside the audited FY1972 note in S0101**, plus the **1975-08-19** split disclosed in S0105's Note 4 (6,687,789 shares; $668,779 at $.10 par — A3 Table S3). Also: 1975-08-19 falls **outside** Stage 1 as bounded here (the window closes 1970-10-08), so its presence in a Stage-1 record set is a boundary violation as well as a count error. What survives the row: exactly **one** split falls inside the FY1972–FY1979 EPS-restatement dispute, and A3's proof is the halving pattern (FY1974 printed $.93 then $.47), i.e. **one adjustment, not two** | Claim corrected in place; superseded wording retained above |

### D.1 The first experiment, as the record is actually able to carry it

What the corpus permits is a **three-sentence reconstruction and a wall of silence**. The sentences: a
franchised variety-store operator opened a larger-format store in **Rogers, Arkansas in 1962**, named it a
**Wal-Mart Discount City**, and by **1970-01-01** operated **18 of them alongside 14 Ben Franklin variety
stores** in a four-state area on **$31 million** (S0109; S0101's "eighteen … as of February 1, 1970").
Everything a "first experiment" section conventionally holds is **absent**: no opening-day takings, no
advertised price, no floor area for the 1962 store, no customer count, no lease, no photograph, no
contemporaneous press item. Specifically **not on disk and not to be inferred**: the folklore 6,000-sq-ft
former warehouse, "45,000 items", and "$1,402" of first-day sales — each returns **zero** hits across the
nine reports, and the nearest printed numbers belong to **other years and other stores** (FY1980 prints
"over 35,000 items" for a 1980 store; FY1974 prints Rogers at **35,000 → 56,000 sq ft** on relocation,
which is a 1974 fact about a 1974 building, not a 1962 one). The store's own **town size** is printed
twice and disagrees: "then a town of approximately 4700" (S0104) vs "approximately 5,000" (S0107) —
**U-A3/8**, kept unadjudicated.

### D.2 Why 1962 cannot be written as a validated experiment in this volume

The hindsight firewall (§2) forbids reading the later fleet as proof the 1962 format worked *then*, and the
independence rule (§3) forbids counting six annual reports as six witnesses. Against those two rules the
1962 event has: **one attester, writing 12–18 years later** (S0103 is the first to date it), **no
independent publisher** (A4's ten Business Week index years, 1962–1971, print **zero** Wal-Mart entries
while printing dated discount-sector distress — S0112…S0124), and **no measurement of the store itself**.
The sector facts are admitted **only as market-state for §H (part_2)**: Business Week's own December 1962
characterisation of "a fast-growing $6-billion industry … facing a major shakeout" (p.78) describes the
environment a 15,000-store-era reader could observe, and **is not evidence that the founder observed a
gap, nor that the format was a good answer to anything**. The anti-hagiography test applied: every record
in §D.1 would still read as plausible had the chain been liquidated in 1975 — the store count at 1969 was
**27** and the registrant group was still majority-Ben-Franklin by banner at the close of the window.

### D.3 The earliest signal that *could* carry "repeatable validation", and its limits

| Variable | Value | Source | Confidence |
|---|---|---|---|
| The only same-store statement inside the audited window that reaches back to the boundary cohort | "for this year our eighteen Wal-Mart stores that already existed as of February 1, 1970 and were not expanded had a **17% increase in sales over 1971**" | S0101, President's message signed **1972-03-22** | High that the document prints it; **Medium as a validation signal** |
| Total-chain growth in the same letter, for context | "total sales were $78,000,000, a 77% increase over $44,000,000" — **DERIVED check**: 78,014,164 ÷ 44,286,012 − 1 = **+76.2%**; the letter's "77%" is its own rounding of the same two audited numbers | S0101 | High |
| What that pairing demonstrates | A **cohort** of pre-1970 stores grew without new square footage, at a rate **below** the chain's — i.e. growth was simultaneously coming from new units. That is the arithmetic shape of *repeatability* (new units being added to a base that keeps growing) | INFERENCE from S0101's two printed rows; the store-count series 32 → 38 → 51 (A3 Table S2) | Medium |
| What it does **NOT** demonstrate | **Nothing about profitability of the cohort** (no cohort sales or margin is printed, so the cohort's share of FY1972 sales is **UNKNOWN and deliberately not back-solved**); nothing about customer retention, price position, or supplier terms; nothing about 1962–1967 (EMPTY, A3-039); and it is a **company's own characterisation of its own best year, signed by its founder** — one lineage, self-interested, and labelled **CONTEMPORANEOUS** but not independent | S0101 | **High that the limits are limits** |
| The only explicit stop-rule anywhere in the corpus | FY1974, on the Family Center / Home Improvement division: "This is a new division for our Company, and we feel it has great potential … **Further expansion of this division will depend on the results obtained from these first two units.**" — an experiment with a stated gate | S0103 (`WALMART_AR_1974.txt`) | High (as printed). **OUTSIDE the window** (FY1974 > 1970-10-08): it is recorded here only to establish that the registrant *was capable of stating a gate* in its report prose, and that **no such statement exists for 1945–1970** — the silence inside the window is therefore a property of the record, not of the genre |
| The next comparable-store figure the registrant prints | FY1978: "Comparable stores sales (excluding the effect of new stores) increased **17 percent**" (S0107). Two different documents, two different years, the same 17%. **Not merged**; the coincidence is logged so no later pass reads one as the other | S0107 | High (printed); **UNKNOWN** whether the two 17% figures are related |

### D.4 UNTRIED — exact queries not run against local files on this pass, and what each would settle

These are complete answers, not gaps to be smoothed, and each names the file it was not run against.

1. **`WALMART_AR_1976.txt` for the FY1976 restatement of the 1945 origin** — A2's W-50 quotes a
   partially OCR'd "Company's first unit … a franchise Ben Franklin … in 1945, his brother …"; the full
   FY1976 wording is not re-walked here and would fix the *earliest* statement of the fifteen-store count.
2. **A page-image re-walk of the FY1975 Five Year Summary** (`_text.pdf`, 3.2 MB declared in the file's
   own provenance header) against **U-A3/1** — the $226,209 / $236,209 digit ambiguity is *decidable on the
   printed page and undecidable in this text layer*; not attempted because no page image is on disk.
3. **`sources/periodicals/ia_arkgaz.json`, `ia_satpost.json`, `ia_supermerch.json`,
   `ca_01_waltons_five.json`, `gb_01_waltons_five_and_dime.json`** — enumerated but never mined for a
   company-naming item; these are the only on-disk routes to a **1945–1962 named witness**.
4. **`sources/probe_SEC_tickers.json` and the two EDGAR submission blocks** for any *stated* former name
   or state of incorporation beyond `"former": ["Walmart Inc.", "WAL MART STORES INC"]` — the shortest
   remaining path to settling **D-R03c**, and it is a **local** path.
5. **`sources/gov_docs/` for the 1972–1979 SEC issuer registers** — the class that *should* name the
   company after the 1972-08-25 NYSE listing; absent from `sources/`, so this is a **FETCH REQUEST** for the
   orchestrator, not a null (U-A5/1 residual).
6. **`conflicts.csv` / `timeline.csv` / `sources.csv` re-read after this pass** (all four registers read at
   mtime **2026-09-25 19:37**, i.e. mid-repair by another agent): this volume cites their ids but writes
   none of them. A5's **three drafted `sources.csv`** rows (its own ids, not yet issued centrally), its three quantitative rows and its U-A5/1 conflict are
   **present in `research/A5_sec_statistical_lineage_probe.md` §CSV append rows and NOT yet in the
   registers** — cited here as dossier-local until the register owner merges them.

---

*End of part 1. §E–§P continue in `s1_p2.md`; §Q–§U and the claim-record appendix in `s1_p3.md`. Section
letters, claim IDs, metric IDs and conflict numbering continue across volumes and are not renumbered here
(§9.3).*

---

# s1_p2.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T19:18:51Z. NOW WRITTEN: sections E, F, G, H, I, J,
K and L were authored by agent walmart-s1-p2 on 2026-09-26; no PENDING block remains in this file. The
scaffold's original "nothing written yet" warning is superseded by this line. -->

# s1_p2.md — Volume 2, sections §E–§L

*One document split for the file cap (method §9.3); section letters, conflict numbering and metric
numbering continue across volumes. **Part 1 carries Header, `STAGE BOUNDARY JUSTIFICATION`, §A–§D**;
**this volume carries §E–§L**; §M–§U and the claim-record appendix are a later pass in `s1_p3.md`.
Cross-references name the volume: `(Walmart S1 §B.0, part_1)`.*

> **GEOMETRY CORRECTION, emitted for the manifest owner (this pass does not edit `s1_p1.md`).**
> Part 1's header states "§E–§P in `s1_p2.md`; §Q–§U and the claim-record appendix in `s1_p3.md`".
> The dispatch this volume was written under assigns **§E–§L to part 2 and §M–§U to part 3**. Both
> statements cannot be true of one file plan. Recorded here as an instruction-layer discrepancy, not
> silently obeyed: a later reader who trusts the part-1 header will look for §M–§P here and find them
> absent (they are absent, and that is the correct state of this file).

**Hindsight firewall (§2), restated for this volume.** Nothing in §§E–§L treats Wal-Mart's later scale
as evidence that the 1962 format choice, the small-town site rule, the leasing practice, the LIFO
switch or the 1970 offer were rational, prescient, or foreseeable. Sector conditions in §H and §I are
used **only** to state what was publicly knowable in-period, never to argue that the company read them
correctly. Where the corpus holds a company statement and no outside witness, the confidence ceiling
stated in part 1's header applies to every row below.

**Reading rule inherited from §A.1 and enforced in every table below.** **CONTEMP** = the value is
printed in the report *for that fiscal year*; **RESTAT (in S01xx)** = the value is printed in a later
report's comparative or summary table. A restated figure is **not** corroboration of a contemporary
one, and several printings of one registrant figure across FY1974→FY1980 are **one lineage** (§3
filing-lineage rule). Source labels are `S01xx` plus the document path; no citation in this volume is
to a line number.

---

## E. PRODUCT RECONSTRUCTION

STATUS: WRITTEN 2026-09-26

**Frame adaptation (§7).** Wal-Mart is a retailer, so the standard §E frame ("what was the product,
what did it do, how did it change") is answered by the retail equivalent: **the store as the unit of
product, and its specification — size, assortment, departments, price policy, service terms — as the
product description.** There was no artifact, code, or device sold under a Wal-Mart brand in this
window; what was "shipped" to a customer was a physical trading floor and a merchandise mix. The
adaptation is licensed by §7's retail row (stores / supply chain / same-store sales) and it is
declared rather than left implicit, because the frame's absence is the reason §E can say so much about
FY1975–FY1980 and so little about FY1962–FY1967.

### E.0 What the record can and cannot describe

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Earliest fiscal year in which ANY document on disk describes the merchandise offer | **FY1972** — leased-department rentals and lessee-reported department sales are printed for FY1972 and FY1971, and the FY1972 report carries the format language | `sources/periodicals/WALMART_AR_1972.txt` (S0101) | High (as-filed) that the print describes it; the described **year** is FY1972 |
| Earliest fiscal year with a printed **store count** | **FY1968** (24 stores) — and it is a 1972-dated restatement, not a 1968 document | S0101 "5 YEAR FINANCIAL SUMMARY"; A3-039 | Medium, RESTAT (in S0101) |
| The product in FY1962–FY1967 | **UNKNOWN.** No sales, no store count, no square footage, no assortment statement, no price list, no department count for any year FY1962–FY1967 appears in any of the nine printed reports (A3-039: **EMPTY, not thin**) | negative search across S0101–S0109; `research/A3_audited_series_1962_1980.md` A3-039 | **UNKNOWN**, with the gap named: the FY1970 report (the likeliest carrier of a "History" paragraph) does not exist in this corpus (S0101 is the earliest document on disk) |
| The product in 1945–1961 (Ben Franklin years) | **UNKNOWN as a Wal-Mart product.** What is documented is a **franchised third-party banner**, described retrospectively | S0104, S0106, S0107, S0108, S0109 (the 1945/1946 narrative) | **UNKNOWN** for the goods sold; Low for the franchise relationship itself, and the 1945 material stays in pre-history per part 1 §B.1 |

**independence_note (§3).** Everything in §E whose subject is Wal-Mart's own offer traces to
**S0101–S0109 plus Arthur Young & Company's opinions on them** — one registrant lineage. No trade or
general periodical in this corpus describes a Wal-Mart store, assortment, price, or banner (A4's
independent-figures table: "Wal-Mart named in ANY press figure, 1962–1980 — **UNKNOWN, no figure
recovered**", `research/A4_independent_periodicals.md`, S0112–S0133). The one non-registrant item §E
uses is the **December 1961 NRMA Discount Seminar** in *Stores* (S0133), which describes the **trade's**
conception of a discount store three months before the first opening, not Wal-Mart's.

### E.1 The formats the registrant actually ran — a multi-format operator from its first audited year

This is the single most under-used fact in the corpus and it is a **counter-hagiography** fact: the
company's own print documents formats it tried, formats it ran beside the famous one, and formats it
**stopped**.

| Format / unit | What the print states | Dates evidenced | Source | Class · Conf |
|---|---|---|---|---|
| **Wal-Mart Discount City** | the flagship unit; "a regional discount department store chain … operates 276 Discount Cities in eleven states" | 1962 (claimed opening) → FY1980; counts 32/38/51/64/78/104/125/153/195/229/276 at FY-ends FY1970–FY1980 | S0109 company profile; series in S0101–S0109 (A3 Table S2) | FACT (as filed) · High FY1972+, Medium FY1968–FY1971 (RESTAT) |
| **Ben Franklin franchised variety store** | "Until 1962, the Company's business was devoted to the operation of variety stores"; 14 such stores still trading at 1970-01-01; "nine variety and family center stores" in the FY1973 stated goal (55 Wal-Mart + 9 = 64 ✓ the FY1973 count); "Two Ben Franklin variety stores were sold and four were closed during the year" in FY1974; a Ben Franklin variety store at **Rogers, Arkansas "was closed in January. 1976"**; a "Ben Franklin Stores, Supervisor" on the FY1973 operations staff | 1945 (claimed) → January 1976 (last dated trace) | S0106 (FY1977); S0109 (FY1980); S0102 (FY1973); S0103 (FY1974); S0105 (FY1976) | FACT (that the reports say it) · High; **Low** for 1945, single lineage, retrospective |
| **Family Center store** | a distinct, smaller format that was **converted** — the Berryville, Arkansas Family Center, damaged and "being expanded to 30,000 sq ft for reopening as a Wal-Mart Discount City" (FY1973); Marshfield, Missouri "Ben Franklin Family Center converted to a 29,100 sq ft Wal-Mart" (FY1974); 2 Family Centers still open at FY1975 year-end | FY1973 → FY1975 | S0102; S0103; S0104 | FACT · High |
| **Sav-Co Home Improvement Center** | two opened and were counted in the FY1975 fleet (100 Discount Cities + 2 Family Centers + 2 Sav-Co = 104 ✓); FY1976: "Our two Sav-Co Home Improvement Centers have shown improvements during the current year; however, they are still not operating at our expected profitability level. We will continue to critically evaluate this operation"; FY1979: "closed our remaining Sav-Co Home Improvement Center" | FY1975 → FY1979 (opened, under-performed, shut inside five years) | S0104; S0105; S0108 | FACT · High. **This is the corpus's clearest documented format failure** |
| **Project '79, Pine Bluff, Arkansas** | a 62,400 sq ft store "planned, not as a prototype, but to be an experiment in physical plant design, fixture composition and merchandise presentation", opened 1979 | FY1979 | S0108; corroborated only by S0109's letter | FACT · High that the report says it; the **result** of the experiment is not stated in any document on disk ⇒ UNKNOWN |
| **Leased / licensed departments (shoes, jewelry, pharmacy)** | rental income $655,219 FY1972 against $261,246 FY1971, while **the lessees' own reported department sales were $7,297,956 and $3,715,333**; FY1974 leased departments comprised "shoes, jewelry and twenty-six pharmacies"; FY1973 lessee-reported sales $9,678,573; **total store sales including leased departments $182,634,000 in FY1974** against net sales of $167,560,892 | FY1971 → FY1980 | S0101 Note 5; S0103; S0102; S0109 | FACT · High; the **ESTIMATE** that leased volume was ≈9.4% of FY1972 store sales is arithmetic on the company's own two rows ($7,297,956 ÷ $78,014,164), basis = period-end, and it is labelled derived |
| **Automotive Service Centers** | named among the trading entities/units in the FY1973–FY1976 estate descriptions | FY1973 → FY1976 | S0102; S0105 (A2 §"Formats the company itself ran beside Discount Cities") | FACT (as a printed name) · Medium; no specification, count or economics are printed ⇒ UNKNOWN beyond existence |

**E.1 finding (INFERENCE, Medium).** The registrant's earliest audited years do not show a single-format
company executing a proven idea; they show a **four-banner operator liquidating one banner
(14 → 9 → last trace closed January 1976) while experimenting with two others (Family Center
conversions, Sav-Co) and protecting a concession business whose sales it did not own.** The
inference rests on the counts in the rows above, all printed, and it does **not** rest on any claim
about intent; no document in this corpus states why any banner was kept or dropped.

### E.2 The store as specified — the closest thing in this corpus to a product specification sheet

| Specification | As printed | Source (fiscal year of the print) | Conf · basis flag |
|---|---|---|---|
| Size range and average | "30,000–60,000 square feet … average store size approximately 42,000 square feet" (range 30,000–60,000), "the twenty-four newest average 42,900" | S0104 (FY1975 report) | High (as-filed, CONTEMP) |
| Size range, later print | sizes "from 30,000 to 60,000 square feet … with the average size being approximately 45,000" | S0109 (FY1980) | High; **the average moves 42,000 → 45,000 across five reports and both are kept** |
| Size range, widest | "The stores vary in size from 30,000 to 83,000 square feet" | S0108 (FY1979) | High; the upper bound escapes the 60,000 figure — a range statement, not a spec |
| Assortment depth | "over 35,000 items" | S0109 (FY1980) | High (company statement) · **the basis of "item" (SKU? style? vendor pack?) is not defined in any document** ⇒ denominator UNKNOWN |
| Department structure | "Each store features 36 departments"; "36 full-line departments" | S0108 (FY1979); S0109 (FY1980) | High (as stated) |
| Merchandise mix | "Softline products account for 30 percent of sales and hardline goods 70 percent" | S0108 (FY1979) | Medium — **management's own characterisation with no stated basis and no supporting dollar row**; no document prints a softline/hardline sales split |
| Total fleet space | **5,295,000 sq ft (FY1976, CONTEMP)** → ≈6,500,000 (FY1977, company's own word "approximately") → 8,500,000 (FY1978) → **10,200,000 "Total retail space occupied at January 31, 1979"** (FY1979) → 12,600,000 (FY1980) | S0105–S0109; A3 Table S2 | High (FY1976+); **three different labels across four years** ("total space" / "floor space in operation" / "retail space occupied") with no definition in any document ⇒ the series is *not* established to be one quantity |
| Pre-FY1976 total space | **UNKNOWN for every year FY1962–FY1975.** FY1972–FY1975 print **additions only** (FY1972 +604,000 sq ft; FY1973 +781,940; FY1974 +881,630; FY1975 +1,083,326, "a record for new store space in a single year"). The addition series **must not be cumulated backwards into a total** | S0101, S0102, S0103, S0104; A3 Table S2 note | High (that totals are absent); the FY1980 phrase "less than a million square feet" at 1970-01-01 is a **1980 sentence about 1970** (S0109) |
| Price policy | price set below manufacturer's suggested retail and at "meet or undersell local competition", **except items covered by Fair Trade Laws**, said to be a negligible portion of sales by FY1976 | S0105 (FY1976) | High (as printed); "negligible" is the company's word, unverified |
| Customer-facing terms | "unconditional money-back guarantee"; "Satisfaction Guaranteed"; "WE SELL FOR LESS"; "Guaranteed Quality at Discount Prices"; "Price Busters" signing; "Grand Opening"; "Big Little Sale" with "inflation stoppers" | S0105 (FY1976); S0109 (FY1980); S0101 cover | High that the print carries them; they are **advertising language, not terms of sale evidenced anywhere else** |
| The one surviving 1962 wording | the museum page's own transcription of its catalogued 1962 advertisement: **"Wal-Mart Lowers Living Cost"** | `sources/periodicals/walmart_museum_page.html`, company asset entry "First Walmart Advertisement", asset year 1962, page `dc:modifyDate` **2026-04-24** (A2 W-77; S0134 register family) | **Low–Medium.** This is the *only* 1962 artifact catalogued in the evidence set, and the slogan survives **as company transcription on a 2026-modified page**, not as a document anyone read in 1962; the advert's remaining contents are paraphrased, not transcribed |
| 1962 store size / stock / prices | **UNKNOWN.** The commonly cited "6,000 sq ft", "45,000 items" and opening-day price claims have **no witness of any kind in this corpus** (probe §"Famous claims pre-flagged as likely untraceable"; the flyer lead at W-20 was never retrieved and its bytes are not in `sources/`) | — | **UNKNOWN**, gap named |

### E.3 Product *change* evidenced inside the window, with each change on its own document

1. **FY1972 → FY1976: build-out of the standard box.** Additions of 604,000 (FY1972, 14 new stores),
   781,940 (FY1973, 18 new), 881,630 (FY1974, 20 new + 6 closed), 1,083,326 (FY1975, 26 new + 2
   enlarged), 993,436 (FY1976) square feet, each printed in its own report (S0101–S0105; A3 Table S2).
   Every one is **CONTEMP**; the fleet goes 51 → 125 stores. FACT, High (as-filed).
2. **FY1973–FY1976: the variety estate is wound down**, evidenced by arithmetic inside the company's own
   sentences, not by a company essay: 14 Ben Franklin units trading at 1970-01-01 (S0109), 9 "variety and
   family center stores" at FY1973 (S0102, 55 + 9 = 64), 2 sold and 4 closed in FY1974 alone (S0103), the
   last dated trace closing at Rogers in January 1976 (S0105), and "completely phased out" across the
   decade in the FY1980 telling. FACT (each print) · High; **the reason is not stated in any document**
   ⇒ mechanism UNKNOWN.
3. **FY1975 → FY1979: a second format opened, judged and shut.** Two Sav-Co Home Improvement Centers
   counted at FY1975 (S0104), still below expected profitability at FY1976 (S0105), remaining unit
   closed in FY1979 (S0108). FACT · High. This is §L's most important negative and it is developed at
   §L.4; §M (part_3) owns the failures register.
4. **FY1977–FY1980: the concession business is bought back.** Hutcheson Wholesale Shoe Company,
   "previously a licensee, was acquired on October 1, 1978", with its sales moving from
   $18,579,000 in licensed-department sales (1 February–30 September 1978) to $11,773,000 inside the
   company's own figures from 1 October 1978; licensed-department sales reported by licensees then fell
   to $46,097,000 in FY1980 from $60,560,000 in FY1979; and the FY1980 objectives carried "the previously
   announced plan to acquire 159 licensed jewelry department units, presently operated by Cohen-Hatfield"
   (S0109, Note 5 and profile). FACT · High. **Cohen-Hatfield is the only named external retail operator
   anywhere in these reports, and it appears as a counterparty, not a competitor** (see §I.2).
5. **FY1978: an acquired store group enters the fleet.** "we acquired a group of 16 stores. Four stores
   were closed during the year" alongside 30 new stores and 10 expansions/relocations (S0107). FACT ·
   High; **the acquired group's banner, location and price are not stated** ⇒ UNKNOWN.

**E.3 methodological point (INFERENCE, Medium, mechanism named).** The product's in-window trajectory is
visible **only** through quantities the auditors were asked to attest (store counts, square footage
additions, licensed-department dollars) and through one-off narrative sentences. There is no printed
assortment evolution, no category sales series before the FY1979 softline/hardline characterisation, and
no price index. A §E written as a product *story* would therefore be smuggling in the 1992 memoir; a §E
written as this table of quantities is the most the corpus licenses.

### E.4 The date of the first store: two company sources, two months

**U-E/1 (new conflict opened by this volume; merge row requested below).**

- **CLAIM A** — the first Wal-Mart Discount City opened at Rogers, Arkansas **in November 1962**, in
  "Rogers, Arkansas (then a town of approximately 4700)" (S0104, FY1975 company profile); the FY1978
  report repeats it: "the Company did not open its first discount department store until **November 1962.**
  The first Wal-Mart Discount City store was opened in Rogers, Arkansas" (S0107).
- **CLAIM B** — the company's own curated page states "On **July 2, 1962**, Sam Walton opens the first
  Walmart store in Rogers, Arkansas" (`sources/EXTRACT_corporate_walmart_history_timeline.md`; A2 W-118;
  probe W-09).
- **WHY THEY DIFFER** — different instruments and different purposes: A is dated corporate print inside
  audited documents (1975 and 1978), repeated in FY1979/FY1980 in year-only form; B is an undated
  marketing page with zero citations, retrieved 2026-09-23, whose detail traces to a lineage this
  repository has never seen. Neither is a 1962 document.
- **EVIDENCE WEIGHT** — A carries four separate printings inside the registrant's own signed reports and
  is the only version anchored to audited documents; B carries no citation and is contradicted on the
  *same page family* by the museum asset entry, which is catalogued by year only. Both are **one
  lineage**; the count of independent origins for either month is **zero**.
- **BEST-SUPPORTED INTERPRETATION** — **1962 is attested; the month is not.** Where a month must appear
  (timeline rows, §Q micro-chronology in part_3) the corporate-print month is used **with U-E/1 cited
  beside it**, and the July date is never presented as the documented one.
- **RESIDUAL UNCERTAINTY** — no 1962 newspaper item, lease, permit, register tape or photograph exists in
  this corpus; the Arkansas Gazette / Southwest Record / Rogers and Bentonville weekly routes are
  **UNTRIED** (paywalled or bot-blocked in earlier passes), as is the Arkansas Secretary of State entity
  file. `research/A_chronology_feasibility.md` W-05, W-22.
- **CONFIDENCE** — High (that the two company sources disagree); **UNKNOWN** (the opening date).

### E.5 Knowability, §E

| State | Content |
|---|---|
| **KNOWABLE in-window** | the formats the company ran and counted (E.1); the store specifications it published (E.2); additions and closures; the leased-department economics; the price-policy sentence and the Fair Trade carve-out |
| **NOT KNOWABLE in-window** | whether any of it was unusual — no independent publication in this corpus describes a Wal-Mart store at any date, so an operator inside 1962–1971 could not have read a third-party account of this firm (S0112–S0133, all zero) |
| **UNKNOWN, with the gap named** | FY1962–FY1967 assortment, prices, store size, item counts, sales; the 1945–1961 Ben Franklin merchandise offer; the definition behind "over 35,000 items" and behind each square-footage label; the outcome of Project '79; the banner and terms of the FY1978 sixteen-store group; whether the 1962 store and the 1976-closed Rogers Ben Franklin unit shared premises (S0105 does **not** say they did) |

---

## F. CUSTOMER

STATUS: WRITTEN 2026-09-26

**Frame adaptation (§7).** For a discount department store the customer section is answered by
**who the store was sited to serve, what the trading-area rule was, and what demand evidence the
documents print** — not by user counts, cohorts or retention, none of which existed as reported
quantities. **No document in this corpus prints a customer count, a transaction count, an average
basket, a per-visit spend, a demographic profile, or a repeat-purchase measure for any year** — the
absence is not a search failure but a property of the reporting regime, and it is the first thing §F
must say.

### F.1 The customer as the company described it

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Site rule, stated FY1975 | stores "within a **350 mile radius** of the General Office and Distribution Centers in Bentonville"; **average community population served 10,000–15,000**; average store ≈42,000 sq ft | S0104 (`WALMART_AR_1975.txt`) | High (CONTEMP as-filed) that the company stated the rule |
| Site rule, stated FY1978 | towns "having populations from **5,000 to 25,000**" | S0107 | High (as-filed) |
| Site rule, stated FY1980 | "located primarily in towns having populations from 5,000 to 25,000"; stores "located primarily in small communities like Bentonville" | S0109; S0108 (FY1979 profile) | High (as-filed) |
| **The two bands disagree and both are kept** | FY1975's *average* of 10,000–15,000 and FY1978/FY1980's *range* of 5,000–25,000 are different statements (an average is not a bound); the FY1975 sentence describes communities served, the later ones describe where stores "are located" | S0104 vs S0107/S0109 | **U-F/1 (merge row requested).** High that both are printed; **UNKNOWN which rule governed which openings** — no document lists a town's population against a store |
| First-store town population | "Rogers, Arkansas (then a town of approximately 4700)" (FY1975) vs "approximately 5,000 people" (FY1978) | S0104; S0107 | **A3 U-A3/8, live conflict, not resolved here.** No census record is in this corpus |
| Geographic reach | FY1972 five states inside a "magic circle" within 300 miles of the DC; FY1973 list adds Kansas, Louisiana, Missouri, Oklahoma, Tennessee; FY1975 eight states (AR 37 / MO 36 / OK 15 / KS 6 / TN 6 / LA 2 / MS 1 / KY 1 = 104 ✓) with entry into **Kentucky and Mississippi** in FY1975 (Corinth MS 50,150 sq ft August; Fulton KY 32,000 sq ft October); FY1977 "nine-state marketing area"; FY1979 "ten central and southern states"; FY1980 eleven states, Missouri 64 / Arkansas 57 / Oklahoma 46 / Texas 36 / Mississippi 18 / Tennessee 17 / Illinois 16 / Kansas 10 / Louisiana 7 / Kentucky 4 / Alabama 1 | S0101; S0102; S0104; S0106; S0108; S0109; A2 §"Geography as filed" | High (as-filed counts). **The Texas entry is dated 1975-11-11 and the FY1977 "nine-state" language post-dates it**; Illinois and Alabama appear **only** in the FY1980 list with no entry dates ⇒ their opening dates UNKNOWN |
| Four-state starting position | "the Company owned and operated 18 Wal-Marts and 14 Ben Franklin variety stores in a **four-state area**" at 1970-01-01 | S0109 (FY1980 report, retrospective) | Medium-High as company state; **one lineage**; the four states are not named in that sentence ⇒ UNKNOWN |

### F.2 What the customers bought, and at what frequency — the honest null

| Question | Answer on this corpus | Why |
|---|---|---|
| How many customers, or transactions? | **UNKNOWN for every year FY1962–FY1980** | no report prints a customer or transaction count; the closest printed quantity is **space**, not traffic |
| Average sale / basket | **UNKNOWN** | derivable only from a transaction count, which does not exist; a sales-per-**store** figure is not a per-customer figure (see §L.2 basis warning) |
| What proof is there that demand was broad rather than company-supplied? | **UNKNOWN, and the strongest available signal runs the other way**: FY1978's own comparable-store arithmetic implies a new store opened at roughly **77% of a mature store's volume** ($2,815,519 per net new store against $3,661,466 per comparable store, DERIVED from S0107's two stated figures) | `research/A3_audited_series_1962_1980.md` §5.2; **mechanism UNKNOWN** — the document offers none, and the 42 is a *net* count (30 openings, 10 expansions/relocations, 16 acquired, 4 closed) |
| Seasonality of demand | fourth-quarter FY1980 sales $417,175 thousand of $1,248,176 thousand = **33% of the year** (S0109 quarterly series) | High (as-filed). **This is FY1980 only; no earlier quarterly series is printed**, so demand shape FY1962–FY1979 is UNKNOWN |
| Did customers come for the merchandise or the concession? | partly measurable: lessees reported department sales of $3,715,333 (FY1971) and $7,297,956 (FY1972) inside stores the company did not own, ≈9.4% of FY1972 volume — a **DERIVED** ratio of one company row to another | S0101 Note 5; A2 W-16 | Medium (arithmetic on printed rows; the "volume" denominator is company net sales, and lessee-reported sales are unaudited third-party figures inside an audited note) |
| Who were they demographically? | **UNKNOWN**; no document characterises customers at all. The only customer-facing economic characterisation is the price policy in §E.2 and the slogan evidence | — | not asserted |
| Employee-as-customer? | **no evidence.** Profit sharing and stock purchase plans are documented (§K.3) but no document states a customer-facing effect | S0101, S0105 | **UNKNOWN**; treating a benefit plan as a demand mechanism would be hindsight (§2) |

### F.3 How the firm reached customers — the only customer-side quantities on disk

- **Newspaper advertising as the primary channel.** "Management estimates that the local Wal-Mart store
  is the largest newspaper advertiser of non-food items in most of the communities in which its stores
  are located"; circulars distributed about **twelve times a year**; television used for area promotions;
  the company "has a plant for printing advertising circulars and newspaper inserts" (S0105, FY1976).
  **Class: FACT that the company stated it; the claim itself is labelled by the company as an
  *estimate* and is unaudited** — Medium at best, and it is §F's single most useful research pointer: it
  tells a future pass exactly which Arkansas, Missouri and Oklahoma weekly files should contain
  Wal-Mart advertising 1962–1976. Those files are **UNTRIED** (probe W-22; A4's newspaper routes 403-blocked).
- **Price-sign and event apparatus** ("Price Busters", "Grand Opening", "Big Little Sale", "Satisfaction
  Guaranteed", "unconditional money-back guarantee") — S0105, S0109, S0101 cover (A2 §"Advertising posture").
  FACT (as printed) · High; their effect on demand is **UNKNOWN**.
- **The FY1975 "350 mile radius" and FY1972 "magic circle" statements are supply-side rules presented as
  market definition** (§G.4) — the customer geography they imply is an *inference from a logistics
  constraint*, not a demand study. INFERENCE · Medium, and §7's interpretive-coda duty requires the
  alternative be kept live: the radius may simply describe where trucks could turn around, and the
  corpus does not say.

### F.4 Coda (§7 interpretive-duty check)

**Evidence:** the site-rule sentences in S0104/S0107/S0109, the state-by-state counts, the FY1978
new-versus-mature store arithmetic, the FY1980 quarterly split, the FY1976 advertising estimate.
**Mechanism:** a small-town siting rule, executed inside a road radius of one distribution complex, and
paid for with local newspaper space — every element of that is a printed company statement.
**Alternative explanations retained:** (i) the town-size bands may be *ex-post descriptions of where
stores happened to be*, not rules anyone followed — no document records a site-selection procedure;
(ii) the 77% new-store figure may reflect ramp timing rather than weaker markets; (iii) the advertising
"largest advertiser" claim is management's estimate and may be wrong. **Confidence:** High for each
printed quantity as printed; **Medium for the siting rule as a rule; UNKNOWN for who the customers were.**
**independence_note:** every row in §F with the company as subject is registrant print (S0101–S0109),
one lineage; the only independent periodical evidence touching §F is trade material about the
*sector's* view of store-size-to-trading-area sizing (S0133, December 1961), and it does not name this
company (see §H.4 and A4 U-A4/7).

### F.5 Knowability, §F

| State | Content |
|---|---|
| **KNOWABLE** | the published town-size and radius language; state-by-state fleet counts; the existence and cadence of local newspaper advertising; the leased-department share of FY1972 volume |
| **NOT KNOWABLE to a contemporaneous observer** | whether this retailer's small-town thesis was working: no press or trade item in this corpus reports a Wal-Mart customer or sales figure at any date FY1962–FY1980, so the industry could not see what the company later reported |
| **UNKNOWN, with the gap named** | customers, traffic, basket, demographics, repeat behaviour, prices paid, and the population of every town where a store opened (no store-level town table is printed before the FY1973 list, and even that list carries populations for none of its entries) |

## G. SUPPLY / HOST SIDE

STATUS: WRITTEN 2026-09-26

**Frame adaptation (§7).** The retail equivalent of "supply / host side" is **merchandise flow** —
who the goods came from, how much of them moved through company-owned plant, what that plant was — plus
the **real-estate estate** on which the whole model sat, since a leased store is simultaneously the
product (§E), the fixed capital (§K) and the supply node. This section is the first place in this
volume where a quantity can be *measured* rather than asserted, because the registrant printed a
distribution-penetration percentage in four consecutive reports.

### G.1 The 1962–1969 supply question: what the corporate print says is **nothing**

| Proposition | Status on this corpus | Source |
|---|---|---|
| How the first stores were stocked (1962–1969) | **UNKNOWN from any registrant document.** A2's pre-1962 ledger records the franchise terms, the franchisor's warehouse, and any pickup arrangement as **NOTHING in the corporate print**: "no date of taking the franchise, no franchisor named beyond 'Ben Franklin', no termination, no warehouse-pickup arrangement" | `research/A2_chronology_finance.md` §Pre-1962 evidence ledger; S0101–S0109 negative search |
| "Before then, stores were stocked by vendor direct shipments and wholesalers" | **Tier-3 trade retrospective, 2012-dated, uncited** — SCDigest, "50 Years of Supply Chain at Walmart", 2012-07-27 (A2 W-78; probe W-18) | `sources/EXTRACT_scdigest_2012_timeline.md` |
| A Ben Franklin **Kansas City** warehouse serving franchisees | **LEAD ONLY, UNTRIED.** Named as a retrieval target in the probe's D3 brief; no document in `sources/` carries it | `research/A_chronology_feasibility.md` §Fleet briefs D3 |
| Date of the first company distribution centre | **CONTESTED, four sources, none cited** — corporate page 1971 Bentonville; PBS 2004 1970 Bentonville; SCDigest 1970 no location; "leased Springfield, Missouri warehouse" lore. Probe U-2 | `EXTRACT_corporate_walmart_history_timeline.md`; `EXTRACT_pbs_2004_timeline.md`; `EXTRACT_scdigest_2012_timeline.md` |
| What the registrant *does* date | a distribution centre **already standing** at 60,000 sq ft before **1971-08-15**, when it was doubled to 124,800 sq ft: "more than doubled from 60,000 square feet to 124,800 square feet. This addition was completed August 15, 1971" | S0101 President's message (1972-03-22) · **High (as-filed)** |

**The licensed sentence for G.1 (INFERENCE, Medium).** A distribution facility existed and was being
enlarged in FY1971 — i.e. **before** the 1970-10-08 offer, and inside the pool of "the various
subsidiaries" that Walton Enterprises, Inc. transferred at the 1970-02-01 pooling (S0101 Note 1). What
supplied stores in 1962–1969 is **not** in evidence at Tier 1, and the 2012 trade line about wholesalers
is a **retrospective characterisation of a period no retrieved document describes**. It must not be
promoted to FACT, and its absence must not be read as proof that company distribution began earlier or
later than it did.

### G.2 Company distribution penetration, as the company itself printed it

This is the only quantified supply-side series in Stage 1 and it is the reason the "wholesaler model"
accounts cannot be used unbounded.

| FY | Penetration as stated | Basis and caveat | Source | Conf |
|---|---|---|---|---|
| FY1973 | the DC "shipped over **$42,786,831 at cost**, largely by our Wal-Mart truck fleet" — against net sales of **$124,889,141** | **ESTIMATE / DERIVED**: $42.8m **at cost** against a **sales** figure is a mismatched comparison in the company's own terms; it nevertheless bounds the claim, because cost-of-goods-through-DC cannot exceed the merchandise the stores sold. A3/A2 read: a **majority of goods did not yet flow through the DC**, and the balance's routing is not disclosed | S0102 (CONTEMP); sales row from S0102/A3 Table S1 | High (both printed rows); Medium (the inference) |
| FY1974 | forward statement only: "A new 150,000 square foot addition … hopefully to be completed by September 1974. At that time, our total Distribution Center and General Office space will exceed 400,000 square feet" | **a plan stated contemporaneously, not a state achieved** — no FY1974 print of the achieved percentage exists | S0103 | High (that it was planned); **UNKNOWN** (what FY1974's actual penetration was) |
| FY1975 | "approximately **60 percent** of the merchandise shipped to our stores came through our Warehouse and Distribution Center as compared to **55 percent** in the previous year" | both percentages in one CONTEMP document, so the FY1974 figure arrives **second-hand inside the FY1975 print** — it is a restated prior-year value, not a contemporaneous one | S0104 | High (as-filed) |
| FY1976 | "approximately **80 percent** of the Wal-Mart store purchases were shipped from the Company's Warehouse and Distribution Center located in Bentonville, Arkansas. **The balance was shipped directly to the stores from suppliers**" | the earliest quantified penetration measurement in the corpus, and the sentence names the residual channel — vendor direct — in the company's own words | S0105 | High (as-filed) |
| FY1977 | "increased from 60% to 80% **within the past two years**" | internally consistent with FY1975→FY1976; a restatement of the prior two years in a later document, same lineage | S0106 | High (as-filed) |

**Series reading (INFERENCE, Medium).** Penetration moved 55% → 60% → 80% across FY1974–FY1976 with the
balance explicitly going direct from suppliers. **What the series does not do** is reach back past
FY1974: the FY1973 dollar row and the FY1974 percentage come from different documents with different
denominators, and **no printed penetration figure exists for FY1962–FY1972 at all**. Any sentence of the
form "Wal-Mart replaced the wholesaler model in year X" is unsupported by this corpus.

### G.3 The distribution estate, with every conflicting print kept side by side

| Date / FY | Facility, as printed | Source and basis | Conf · conflict |
|---|---|---|---|
| ≤1971-08-15 | DC 60,000 → **124,800 sq ft** | S0101, CONTEMP (1971-08-15 completion stated 1972-03-22) | High |
| FY1972 | General Office + DC "increased during 1972 to **261,800 sq ft** 'all under one roof'" (≈25,000 office; 24,000 labelling/sorting/quality control of wearables; balance hardware) | S0102 | High (FY1973-dated statement about FY1972 work) · **U-A2/5: the FY1976 report prints 263,800 sq ft for the same building**, and its open-house note dates the event 1972-12-03 with >1,500 associates attending |
| FY1974 | "+18,000 sq ft GO/DC addition" | printed later in S0105's retrospective account of FY1974 | Medium, RESTAT-in-a-later-report |
| FY1975 | a second **150,000 sq ft DC**, described three ways in the corpus: "began operation in January 1975" (S0104) / "completed in 1975" and "on January 6, 1975, another distribution center was completed" (S0105) — **same facility, three phrasings, one lineage**; loading capacity **8 rail-car and 37 truck doors vs the original DC's 6 and 28** | S0104; S0105 | High that all three sentences exist · **U-A2/3 (A2's own conflict, still open as to which verb is the record)** |
| FY1976 | **238,800 sq ft warehouse** for staples, inspection and price-ticketing + the **150,000 sq ft DC** used as a redistribution point; +31,000 sq ft General Office addition April 1976 | S0105, CONTEMP | High |
| FY1977 | a new **150,000 sq ft Bentonville DC completed November 1976**, taking that site to "**300,000 square feet**" described as a "pure distribution center" on a **2½-day cycle**; all Bentonville distribution facilities ≈**550,000 sq ft**; General Office complex doubled early 1976 to "in excess of 50,000 sq ft" | S0106, CONTEMP | High |
| FY1978 | "construction began during 1977 on a new **390,000 square foot distribution center in Searcy, Arkansas**", completion "tentatively June 1978", "capability of servicing **one-half of the existing Wal-Mart stores**", conveyor at ≈**200 ft/min**, combining "DC I" warehousing with "DC II" distribution | S0107, CONTEMP | High |
| FY1979 | a **"Fashion Distribution Center"** and a **"Claims Center"** listed as divisions in the report's own contents | S0108, CONTEMP | High; **square footage of the Fashion DC is not printed** ⇒ UNKNOWN |
| FY1980 | "the Company operates four … warehouses and distribution centers, **three in Bentonville and one in Searcy, Arkansas**"; Searcy ≈400,000 sq ft on a **93-acre** site, "capability to supply **175 stores**", loading **50–60 trucks daily** into "a **300 mile radius** of Searcy"; stores receiving "**two to three deliveries per week** by the Company's own fleet of **118 trucks** manned by **146 drivers**"; a mechanised **390,000 sq ft** facility "was opened in Bentonville in January, 1980"; a fifth centre of **510,000 sq ft at Palestine, Texas** "scheduled for completion in late 1980" | S0109, CONTEMP | High (as-filed) · **live internal tension: the same report's Chairman's letter says the company "constructed and opened three new distribution facilities" during the 1970s while the profile counts four in operation plus one under construction; reconcilable only by excluding the pre-existing Bentonville warehouse, and the reconciliation is not disclosed** (A2 W-66) |

### G.4 The radius rule is a logistics statement, not a market study

The FY1972 "magic circle" within 300 miles of the DC, the FY1975 "350 mile radius of the General Office
and Distribution Centers in Bentonville" and the FY1980 "300 mile radius of Searcy" (S0101, S0104, S0109)
are **the same constraint expressed as a delivery envelope**, and the FY1980 sentence shows the envelope
moving when a second node opened. **independence_note:** all three are registrant sentences. The
inference — that trading geography was *derivative of* distribution geography in this window — is
**INFERENCE, Medium**, and its alternative is kept live: the company may have chosen towns first and
served them second; no document in this corpus describes the order of either decision.

### G.5 Buying, and a supplier-concentration figure that is **not recoverable**

FY1976 states centralised buying from the General Offices and then prints the sentence
**"no supplier to the Wal-Mart stores accounted for more than [N]%"** in which the percentage itself is
**OCR-illegible** (the layer renders it "29c"; A2 W-57 records the figure as **not recoverable**).
**Class: FACT that the disclosure existed; UNKNOWN what it said.** The apparent "29" is **not** adopted
anywhere in this volume and is **not** to be entered in `quantitative.csv`: a cleaner number substituted
for an illegible one is exactly the defect class §14 rule 8 exists to stop. The one licensed use of the
row is negative — the company **had** a supplier-concentration disclosure by FY1976, which means the
question was being asked of it inside the window.

### G.6 The lease estate: growth contracted **ahead of** opening, in four dated prints

| FY | Future-store leases in hand | Terms attached | Source |
|---|---|---|---|
| FY1972 | **6** | aggregate minimum annual rentals **$285,238**, with inventory, fixtures and working capital for those six estimated at **$3,370,000**; store leases running to **$2,016,723** minimum for the year ending 1973-01-31; renewal options five to fifteen years at the same minimums; percentage-of-sales additional rentals **$54,876** | S0101 Note 7 (CONTEMP) |
| FY1973 | **8** | **$233,247** aggregate minimum annual rentals, estimated **$4,300,000** of inventory, fixtures and working capital still to come; percentage rentals **$62,644**; minimum rentals scheduled "in diminishing annual amounts through 1995" | S0102 Note 7 (CONTEMP) |
| FY1976 | **24** | **$2,029,000** aggregate | S0105 (CONTEMP) |
| FY1980 | **38**, "including 15 under sale and leaseback arrangements" | 20- to 25-year minimum terms approximating **$5,800,000 a year**; total minimum rentals **$85,420,000 (operating)** and **$228,319,000 (capital)**; present value of capital-lease payments **$99,916,000** after imputed interest "at rates ranging from 8.5% to 13.5%"; contingent percentage rentals **$2,027,000** (FY1980) and **$1,149,000** (FY1979) | S0109 Notes 6/3/7 (CONTEMP) |

Supporting facts, each as-filed: a named real-estate vehicle, **Wal-Mart Properties, Inc.**, described as
"our Real Estate and Construction Division", conducting **sale-and-lease-back**, with subsidiary mortgage
notes guaranteed by the parent (S0101, S0102); and the pre-SFAS-13 off-balance-sheet position stated by
the company itself — FY1976 disclosed **$38,416,000** of "noncapitalised financing leases of stores",
whose capitalisation "would cut FY1976 net income ~$515,000" (S0105, and A3-036 for the mechanism).

**G.6 finding (FACT + INFERENCE).** The estate grew by **contract before it grew by construction** at
every date the register can see (6 → 8 → 24 → 38 future stores, FY1972 → FY1980), and the **obligations
the leases created overtook recorded debt by roughly four-to-one by FY1980** (§K.2). INFERENCE, Medium:
the site-before-building practice is documented as a *state*, four times, in four different reports; it
is **not** documented anywhere as a *decision*, and no rationale for it exists in this corpus.

### G.7 People on the supply side

| FY | Headcount as stated | Basis caveat | Source |
|---|---|---|---|
| FY1972 | "some **2,300** who today make up our Wal-Mart world" | President's letter, not a statement page | S0101 · Medium |
| FY1974 | **4,500** | from a chart; OCR renders "4.500" | S0103 · Medium |
| FY1975 | "approximately **5800** associates" | company's own approximation | S0104 · Medium |
| FY1976 | "over **7,500** full-time and part-time associates", up about 1,700 | the only print that defines the basis (full-time **and** part-time) | S0105 · Medium-High |
| FY1977 | "**10,000** associates", stated twice | round number; basis undefined in this document | S0106 · Medium |
| FY1978 | **UNKNOWN — no figure found in this pass; recorded as a gap, not as zero** | — | S0107 |
| FY1979 | "over **17,500** associates" (stated in a data-processing context: company-wide payroll) | — | S0108 · Medium |
| FY1980 | "more than **21,000** associates"; separately **118 trucks manned by 146 drivers** | — | S0109 · Medium |

**Trap recorded once, applies to every headcount row.** The documents never define "associate": no
report states whether leased/licensed-department staff, or the employees of the concessionaires whose
sales the company reports (§E.1), are counted. **All eight figures are company assertions, one lineage.**

### G.8 Coda (§7 interpretive-duty check) and knowability

**Evidence:** the penetration percentages (S0104/S0105/S0106), the DC dollar row (S0102), the facility
sizes and door counts (S0101–S0109), the future-store lease series (S0101/S0102/S0105/S0109), the
sale-and-leaseback vehicle (S0101), the headcount prints. **Mechanism, as far as the documents license:**
buying was centralised at the General Offices, goods moved increasingly through one then two then four
distribution complexes, and the store estate was contracted forward under lease and sale-and-leaseback
financing. **Alternative explanations retained:** (i) the rising penetration percentage may reflect the
**reclassification** of goods already moving, not new capability — nothing separates the two in these
documents; (ii) "largely by our Wal-Mart truck fleet" may overstate ownership, since the same report
family says **tractors and trailers were leased** (S0105); (iii) the Searcy and Palestine sites are
consistent with congestion at Bentonville but **no document states why either was built**. Where the
mechanism is not in the documents this section says **mechanism UNKNOWN** rather than implying one.
**Confidence:** High for each printed quantity; **Medium for the series as a trajectory; Low for any
causal claim about why it moved.**

| State | Content |
|---|---|
| **KNOWABLE in-window** | that company distribution was a live and measurable programme from FY1971 at the earliest; that leases were signed ahead of openings; that buying was centralised |
| **NOT KNOWABLE in-window** | how this firm's supply apparatus compared with any other's: no competitor's distribution data exists in this corpus, and the company named no rival (§I.1) |
| **UNKNOWN, with the gap named** | 1962–1969 sourcing; the franchisor's warehouse arrangement; the first DC's year and town (four sources, probe U-2); FY1974 achieved penetration; supplier-concentration percentage; the Fashion DC's size; wage, benefit-cost and payroll dollar amounts for any year (§K, §J) |

---

## H. MARKET (AS KNOWABLE IN-PERIOD)

STATUS: WRITTEN 2026-09-26

**Evidentiary rule for this section, stated before any row.** §H is the one place in Stage 1 where
**non-registrant print does real work**, and it may use that print for exactly one purpose: to establish
**what a contemporaneous observer could have read**. Business Week's annual indexes and *Stores* (the
journal of the National Retail Dry Goods Association, later NRMA — the same trade body whose franchise
members ran Ben Franklin stores) are **Tier-1 for knowability** because they are dated, paginated
statements of attention published by a periodical about its own output. They remain **Tier-2/3 for any
company fact**, and no row below converts a sector figure into a Wal-Mart figure. Per part 1 §A.2,
**ten Business Week index years and five *Stores* apparatuses print zero occurrences of "Wal-Mart"**
while carrying dated sector stories (S0112–S0133): *the sector was newsworthy; the participant was not.*

### H.1 The condition of the discount trade in the year of entry, 1962

All rows: *Business Week* 1962 annual index, item `sim_business-week_1962_index` (S0112; A4-01…A4-07),
indexed by printed page and issue date. **Class for every row: CONTEMPORARY OBSERVATION at index level
only — the article text is not reachable on this route and nothing from it is quoted or implied.**

| Date | Indexed entry | Page | Register |
|---|---|---|---|
| Feb. 3 | "Discounters invade food field" (block entry) | p. 62 | S0112 |
| Feb. 10 | Korvette moving upmarket | p. 72 | S0112 |
| Mar. 24 | **Walgreen buying three Houston discount stores** — a drug chain entering the trade | p. 36 | S0112 |
| Apr. | **Parke Davis** switching to sell directly to discounters — the supplier channel, in dispute | p. 54 | S0112 |
| Jul. 14 | (decoy row) "WALTON, William — Motel chain finds profits in owning: Holiday Inns is acquiring franchised units" — **not the Arkansas family** | p. 47 | S0112 · A4-07 |
| Aug. 18 | "Discounter caught in cash bind: Grayson-Robinson's plight may presage a discount house shakeout" | p. 109 (layer also prints `pl169` → **A4 U-A4/1**) | S0112 · A4-05 |
| Sep. 22 | "Another discounter enters bankruptcy court as Grayson-Robinson case worries lenders" | p. 146 | S0112 · A4-05 |
| Oct. 6 | **"Discount store dropouts"** | p. 101 | S0112 · A4-02 |
| Oct. 27 | **"Shake-out among discounters seen as chain files in bankruptcy"** | p. 83 | S0112 · A4-03 |
| Dec. 1 | **"Discounters strive to ride out storm: Fast-growing $6-billion industry is facing a major shakeout"** (with illus) | p. 78 | S0112 · A4-04 |

**Market-state effect, phrased to survive the firewall (§2).** A 1962 entrant into discounting entered a
sector the trade press was actively writing down **in the same twelve months as its founding**. That is a
fact about the sector's condition; it tells us **nothing** about whether this entrant was well or ill
run, in either direction. The dataset forbids the hindsight reading (Walmart's troubles were everyone
else's opportunity) and equally forbids its mirror (the sector was doomed and the company beat it).
**Whether anyone at Wal-Mart read any of this coverage is UNKNOWN and no inference is offered** — A4's
own adjudication of this exact pair (U-A4/3) records the two claims as being of different kinds.

### H.2 The size of the market — two published figures, and a prohibition

| Figure | Citation | Status |
|---|---|---|
| **$6 billion**, "fast-growing … facing a major shakeout" | Business Week p. 78, Dec. 1 1962 (S0112, A4-04) | contemporaneous characterisation, published *during* the year, **no stated universe** |
| **$6.9 billion** in discount-store sales for calendar **1962** | Business Week p. 132, Jul. 13 1963, indexed short item (S0114, A4-19/A4-30 family) | specific figure for the completed year, published seven months later; the layer's column reflow **loses the subject noun and the source attribution** |
| **A4's own adjudication (U-A4/5)** | both are Business Week, both index-level, and **neither can be checked against article text, which does not exist on this route** | **Best supported: print both, choose neither.** Residual: the industry definition behind each (establishments? lines of merchandise? including food discounters?) is **UNKNOWN**. The gap between them is **15% of the figure** |

> **REGISTER DISCIPLINE, inherited verbatim from A4 U-A4/5 and binding on §P (part_3):** neither $6bn nor
> $6.9bn may be used as a denominator for any "Wal-Mart's share of the industry" metric, and no
> penetration ratio against either is computed anywhere in this volume.

### H.3 1963–1971: consolidation, counting, and the incumbents moving in

All rows are Business Week index entries; register ids in the last column; **Class: CONTEMPORARY
OBSERVATION (index level)**.

| Year | What was publicly printed | Source |
|---|---|---|
| 1963 | **"Fewer stores to share the pie: They get bigger but decrease in number as discounters, chains squeeze 'little guys'"**, p. 182, Nov. 16 — a *shrinking unit count* for the trade, one year after Wal-Mart's founding | S0114 (A4-30 family) |
| 1963 | A **Dun & Bradstreet survey** of discount-store department profitability, p. 79, Nov. 9 (one department name lost to OCR) — the survey volume itself is **UNTRIED** | S0114 |
| 1962 | the index also points at **AUDITS & Surveys Co.** ("Data on discount stores offers … progress they have been making") and a truncated "**Dun & Bradstreet reports on number of disc…**" — i.e. third-party counting of this trade demonstrably existed | S0112 · A4-06, recorded as a **LEAD, not evidence** |
| 1964 | **"Nielsen survey shows an increase in the number of mass merchandisers"**, p. 100, May 16 — an independent counting operation addressing the population two years after founding | S0115 · A4-08 |
| 1964 | **"The old five-and-ten spreads new wings: Woolworth branches out into mass merchandising in varied lines"** (with cover) p. 58, Nov. 14, plus "…is setting up **Worth Marts**, discount mass-volume stores", p. 24, Dec. 26 | S0115 · A4-09 |
| 1964 | "Bus line adds a destination: Houston transit company opens a discount house to lure riders", p. 78 | S0115 |
| 1965 | **"Is success spoiling discount stores? Moves to carry more costly merchandise worry industry leaders"**, p. 97, Jun. 2 — self-doubt *inside* the sector | S0117 |
| 1965 | a **Supreme Court franchise-law question**, p. 66, Apr. 3 — indexed matter that touches the **Ben Franklin form** directly, in the year before the first Discount City's fifth anniversary | S0117 |
| 1966 | **Kresge** cover story on "upgrading, discounting, and experimenting", Jan. 29 — the variety-to-discount conversion thesis was **public print, not a later historian's frame** (page contested: p. 26 / p. 126, **A4 U-A4/2**, so the entry is cited by headline, date and cover status only) | S0118 |
| 1969 | "Discount stores getting tryout" p. 98, Aug. 2; "A discounter is a Washington department store" p. 108, Sept. 20 | S0122 · A4-10 |
| 1970 | **"How Kresge became top discounter"** (with cover, chart and illus) p. 62, Oct. 24, indexed under **three** blocks — `DISCOUNT Houses`, `KRESGE (S. S.) Co.` **and `VARIETY Stores`** — third-party evidence that the discount and variety trades had publicly fused, in the same year as Wal-Mart's public offering | S0123 |

**H.3 finding (FACT about the press; INFERENCE about the market).** By 1970 the *category* this company
entered was a named subject with its own rankings, its own counting firms, and its own literature about
failure. **The company's own unit count was rising (51 FY1971 → 64 FY1973 → 78 FY1974) while the trade's
published unit count was falling.** A4 records that pair as **U-A4/6** and refuses the causal reading:
the two are different universes measured by different instruments, whether Wal-Mart sat inside or outside
the "chains squeezing little guys" class is undeterminable from this corpus, and **whether any
contemporaneous observer — including Sam Walton — could have read that headline as an opportunity or as
a warning is UNKNOWN.**

### H.4 The channel the company's own trade body ran: *Stores* (NRDGA → NRMA)

This is the most valuable §H material in the corpus, because it is **the published market state of the
exact transition the registrant later narrated as its own venture** — carried in the journal of the
association its franchise banner belonged to.

| Date | Item | What it printed | Source · Class |
|---|---|---|---|
| June 1958 | *Stores* member survey | **"the spread of discount houses over the country is slowing down"** — **28%** of member stores saw *more* discount houses in their communities, **6%** fewer, **66%** no change. Respondent universe **not disclosed** and **UNTRIED** | S0131 · FACT (that the survey was published); UNKNOWN (its sampling frame) |
| Jan. 1960 | NRDGA presidential editorial | the **mandatory functional-discount bills** — the legislative fight over the wholesale discounts that financed variety stores | **S0134** (the bounded *Stores* extract; the intake read this issue and **no per-issue row exists in `sources.csv` for 1960-01**, so the extract document is the citable unit) · CONTEMPORARY OBSERVATION |
| Mar. 1961 | *Stores* | no company name; the sector's **willingness to try new ways** indexed | S0132 |
| **Dec. 1961** | **NRMA's first Discount Seminar, "The Discount Business — Is It for You?"** — held **three months before the first Wal-Mart Discount City opened** | ≈**800 attendees, half of them conventional department-store representatives**; published **hard-goods discount markup of 26 to 28 per cent**; a consultant's warning of **"a serious 'over-concentration' of discount stores"**; a **store-size-to-trading-area table** (30,000 sq ft against a trading area "Under 100,000" rising to "Over 150,000 … Multi-million"); NRMA **membership "covers over 11,500 retail establishments with a combined annual sales of over $19 billion"**; **S. E. Nichols Company described as "operator of Nichols Discount Cities since 1958, and with a long previous history in variety stores"**; and American Dixie Shops (Richard Tumpowsky) describing **"more than 40 departments in discount stores"**, volume that "will hit $30 million next year", and **$100,000–$150,000 of inventory per 8,000–10,000 sq ft leased department aiming at $1–1.5 million sales** | **S0133** · FACT (that it was published, dated, paginated); **Tier-1 for knowability, Tier-3 for any company fact** |
| 1971 | *Stores* Vol. 53 annual index | subject-only apparatus: `wal-mart` 0 · `walton` 0 · `ben franklin` 0 · `variety` 0 · `discount` 0 — **this proves the index did not carry the subject, not that the trade ignored the firm** | S0125 (part 1 §A.2) |
| 1972 | *Stores* Vol. 54 annual index | the test at the company's first full year as a public issuer — still no name | S0126 |

**Three prohibitions that follow from this table, each stated so a later pass does not cross it.**
1. **The $19 billion NRMA aggregate is a *membership* total, not the discount industry and not a market
   denominator** (A4's own label discipline). Wal-Mart's share of it is deliberately **not computed**.
2. **The 26–28% trade markup and Wal-Mart's filed gross margins (24.90%–26.57%, §L.3) are not the same
   measure** — one is a *leased-department operator's markup on a store-within-a-store*, the other a
   *whole-store* gross margin. They must never be subtracted (A4, U-A4/7 mechanism note).
3. **The December 1961 sizing table cannot be used to say the founders were wrong, right, or
   influenced.** A4's U-A4/7 lays out the pair honestly: if the smallest bracket means a 30,000 sq ft
   store belongs where the trading area is *up to* 100,000, a 4,700-person Rogers sits **inside** the
   rule; if it means *at least*, Rogers **violates** it. The layer's column pairing is OCR-damaged, the
   seminar's own text is unreachable, and **whether any Walton attended or read NRMA material at all is
   UNKNOWN**. A4 logs this as **RESEARCH DEBT under §10** — it is the closest this dossier comes to an
   independent check on the founding decision, and it cannot be closed from index-and-OCR evidence.

### H.5 The market as the registrant itself framed it (for contrast with H.1–H.4)

| Claim | As printed | Source | Conf · caveat |
|---|---|---|---|
| Category label | "a **regional** discount department store chain"; "Discount City"; "**leading** regional discount chain"; "mid-South region" | S0101 cover; S0105; S0102; S0109 | High. **The company never calls itself a national chain in these documents** — the category claim is deliberately bounded |
| Margin position | "one of the **lowest gross margins of any chain in the United States**" | S0101 | Medium as a company assertion; **unbenchmarkable — no comparator is named and no comparator data exists in this corpus** |
| Sales-per-foot vs a named study | sales per square foot of selling area were "well above the national average for discount store chains **surveyed for the Cornell study**" | S0102 | **The only comparator SET the company names.** The study itself is **not in this evidence set** ⇒ contents, sample and the company's rank are **UNKNOWN** (A2 W-38). Also a **denominator trap**: FY1973's is *selling area*, FY1980's is *gross space* (§L.3) |
| External ranking | Forbes' "Annual Report on American Industry" according Wal-Mart **First Place** in its annual ranking of "major discount, variety and department store chains", first in return on equity, return on capital, sales growth and EPS growth "based on the previous five-year average", for the **fourth consecutive year** | S0109 | High (that the company reported it); **the Forbes volumes are not in this corpus** ⇒ UNKNOWN (the ranking's contents). **Names the peer set, not the peers** |
| Self-awarded title | "undisputed claim to the title, '**Fastest-Growing Regional Discount Chain in America**'", and "the youngest general merchandise retailer in the United States to attain the milestone of over a billion dollars in sales in one year, and the only regional discount chain ever to achieve this landmark" | S0109 | High (as a printed statement); **Medium as a measurement — the superlative is the company's, the population it ranks within is undefined** |

### H.6 The null, its perimeter, and what remains UNTRIED

**The decisive empty row (carried from A4's independent-figures table):** *Wal-Mart named in ANY press
figure, 1962–1980 —* ***UNKNOWN, no figure recovered*** *in ten Business Week index years, five* Stores
*annual indexes and nine* Stores *monthly items* (S0112–S0133). **Class: FACT (of absence inside a stated
perimeter).** Consequences for this section, stated as boundaries not as findings:

- **EMPTY (searched, silent, inside a perimeter).** The eight *Stores* monthly issues sampled
  (1946-06, 1950-06, 1951-06, 1955-06, 1958-06, 1961-03, 1961-12, plus the intake's 1960-01): `walton` 0,
  `wal-mart` 0, `ben franklin` 0, `bentonville` 0, `springdale` 0 — **and 193 issues of the same run are
  UNTRIED**, so the only licensed sentence is "the issues sampled do not name it", never "the trade
  ignored it" (A4 §Data gaps; A4-23 perimeter).
- **UNTRIED, and not to be reported as a null.** Arkansas, Missouri and Oklahoma daily/weekly files
  (Arkansas Gazette at UALR/ArCat, *Southwest Record*, Rogers and Bentonville weeklies, newspapers.com /
  Gale / Chronicling America beyond 1963); *Chain Store Age*, *Discount Store News*,
  *Discount Merchandising* **at any archive other than Internet Archive** (IA proved EMPTY for them five
  ways, A4-41, which is a route null not a genre null); the **NRMA/NRDGA directory-yearbook family**,
  which is the document class that would carry a membership roster — **absent from this corpus, no roster
  found** (A4-41); the **Dun & Bradstreet / AUDITS & Surveys / Nielsen** volumes themselves; the
  **Cornell study**; the **Forbes** annual reports; HathiTrust's **573 full-view records matching
  "Wal-Mart"** in the 1970s facet (S0137, A4-43) — reachable, **candidate set only, no text read**.
- **Decoys already documented, listed so no later pass promotes them.** "WALTON, William / Holiday
  Inns" (p. 47, Jul. 14 1962, S0112); "G. H. Dreyfus, H. C. Walton" (p. 4, Aug. 29 1970, S0123);
  **NEWPORT, Ky. — Boycott of Communist-made goods** (p. 38, Dec. 15 1962, S0112); Arkansas appearing in
  the 1967 indexes **only as river infrastructure** (S0119, S0120); and a steel town's "small town" story
  (S0120). Citing any of them as a Wal-Mart witness would be a fabrication.

### H.7 Coda (§7 interpretive-duty check) and knowability

**Evidence:** thirteen Business Week index/half-index layers (~1.06 M words read whole, every byte count
matched to the item's declared size, per A4's own re-walk R1–R7) and nine *Stores* items, all with
offsets recorded in `sources/periodicals/BUSINESSWEEK_INDEX_1962-1971_EXTRACT_walmart_and_sector_hits.txt`
and `STORES_NRDGA_1946-1972_EXTRACT_walton_and_discount.txt` (S0134). **Mechanism:** indexes and trade
journals are published instruments of attention; what they carry is a dated statement of what was
discussable, which is precisely the evidence class §H is allowed. **Alternative explanations kept live:**
(a) the company may have been covered by titles no reachable host indexes; (b) Business Week's silence
may be editorial selection and *Stores*' silence an artefact of its subject-only index apparatus plus
microfilm OCR loss; (c) an unindexed column or brief may have carried the name and never entered a
finding aid. **Confidence (A4's own numbers, adopted here):** High that BW covered the sector as
described across ten years; High that BW's indexes do not name the company 1962–1971; **Medium** that
this is a fair picture of *total* press attention; **Medium** that the sampled *Stores* issues represent
the run — which, on 7 of ~200 issues, they are not.

| State | Content |
|---|---|
| **KNOWABLE in-period** | everything in H.1–H.4: that discounting was in a public shake-out in 1962; that third parties were counting the trade; that the largest variety incumbents were converting; that the trade's own association had formalised the discount transition by December 1961 and published its markup norms, its sizing table and an over-concentration warning |
| **NOT KNOWABLE in-period** | where this company stood inside any of it — it was not in the published counts, not in the indexes, and not ranked by anyone whose work is on disk. **The company's own growth was invisible to the market record until 1980's Forbes citation, which itself is not on disk** |
| **UNKNOWN, with the gap named** | the definition behind $6bn/$6.9bn; the contents of the Nielsen, D&B, AUDITS, Cornell and Forbes instruments; whether the founders read any of the above; and whether local Arkansas print carried the store at all (193+ issues and every newspaper route UNTRIED) |

## I. COMPETITION

STATUS: WRITTEN 2026-09-26

**Two frames, kept apart, because they answer different questions.** (a) **Competition as the registrant
filed it** — what the company said it was competing with, which is a fact about the company's own
category thinking. (b) **Competition as the independent press named it** — which firms the trade press
treated as the discount players in-period, which is a fact about the market's visible structure. On the
evidence in `sources/`, frame (a) is nearly empty and frame (b) is rich — and **the asymmetry is the
finding**: the company that would later be ranked against everyone named almost none of them, and the
paper that named them almost never saw this one.

### I.1 Competition as filed: category-level, never firm-level

| Frame | As filed | Source | Conf |
|---|---|---|---|
| Self-label | "a **regional** discount department store chain"; "Discount City"; "WE SELL FOR LESS"; "Guaranteed Quality at Discount Prices"; "leading regional discount chain"; "mid-South region" | S0101 cover; S0105; S0102; S0109 | High that the print says it |
| The one comparative claim about rivals | "one of the lowest gross margins of **any chain in the United States**" | S0101 | Medium; **no comparator named, no comparator data anywhere in the corpus — unbenchmarkable** |
| The one comparator **set** named | "discount store chains surveyed for the **Cornell study**" | S0102 | Medium; study **not in this evidence set** (§H.5) |
| The one external **ranking** cited | Forbes "Annual Report on American Industry", First Place among "**major discount, variety and department store chains**", four years running on a five-year average | S0109 | High (that it was cited); the Forbes volumes are **not on disk** |
| **Named non-company firms, and their actual roles** | White, Weld & Co. Incorporated (New York) and Stephens Inc. (Little Rock) — **underwriters**; Hutcheson Wholesale Shoe Company — shoe-department **licensee**, then acquired 1978-10-01; Cohen-Hatfield — operator of **159 licensed jewelry units** to be acquired; Singer and NCR — **register suppliers**; IBM — **leased-system vendor**; Arthur Young & Company (Tulsa) — auditors; Conner, Winters, Ballaine, Barry & McGowen (Tulsa) — counsel; Registrar & Transfer Company (Jersey City, then Cranford NJ) — transfer agent; Malone & Hyde, Inc. and Montgomery Ward & Co. — **via director affiliations only** | A2 §"Competitors as filed and advertised"; S0101–S0109 as cited there | High |

> **THE LOAD-BEARING NEGATIVE FOR §I.** Across all nine printed reports (FY1972–FY1980) **no discount
> rival is named — not Kmart, not Woolworth's, not S. S. Kresge, not FedMart, not Two Guys, not Gibson,
> not any Arkansas-area competitor** (A2 §"Competitors as filed and advertised 1962–1980", "NOT
> ESTABLISHED" row). The competitive frame in the filing is **category-level, not firm-level**, and
> Cohen-Hatfield is the only external retail operator named at all — as a **counterparty** in a
> licensed-department transaction (S0109). Class: **FACT (of absence within a stated perimeter)**, High.

### I.2 The rivals the company counted inside its own walls

| Rival | Evidence | Source | Conf |
|---|---|---|---|
| **Its own other banners** | the FY1973 stated goal — "a profitable operation of the existing **fifty-five Wal-Mart and nine variety and family center stores**" (55 + 9 = 64, exactly the FY1973 count) — puts a non-Wal-Mart banner inside the reported estate; two Sav-Co centres and two Family Centers in the FY1975 fleet (104 ✓); a Marshfield, Missouri "Ben Franklin Family Center converted to a 29,100 sq ft Wal-Mart" (FY1974); Berryville Family Center → Discount City (FY1973) | S0102; S0104; S0103 | High (each CONTEMP). **Walmart's earliest documented competitors were partly its own other formats** |
| **Itself, cannibalised** | FY1973: "our old stores, same size, had a healthy **11% increase in sales (excluding one store near a new Wal-Mart store)**" — the company's own comparable-store metric removes a unit the company had cannibalised | S0102 | High. Two findings in one sentence: an **in-period admission of self-competition**, and — because it speaks of stores "in existence as long as **eight to ten years**" — the closest the corporate print comes to a **1963–1965 opening cohort**, which is a dating remark and **not a count** |
| **Concessionaires inside the box** | lessee-reported department sales $3,715,333 (FY1971) → $7,297,956 (FY1972) → $9,678,573 (FY1973) → licensee-reported $60,560,000 (FY1979) → $46,097,000 (FY1980), with the FY1980 fall partly explained by the FY1978 Hutcheson acquisition moving shoe volume inside the company's own numbers | S0101; S0102; S0109 | High (as reported by the company); the lessees' figures are **third-party numbers transmitted through an audited note**, which is a basis caveat, not a corroboration |

### I.3 Competition as the independent press named it, 1962–1970

Dated, paginated, third-party (Business Week indexes S0112/S0115/S0118/S0122/S0123; *Stores* S0133).
**Class: CONTEMPORARY OBSERVATION at index level.**

| Firm | What was printed, and when | Why it matters here |
|---|---|---|
| **S. S. Kresge Co.** | cover story on "upgrading, discounting, and experimenting" (Jan. 29 1966); **"How Kresge became top discounter"** with cover, chart and illus, p. 62, Oct. 24 1970, cross-indexed under `DISCOUNT Houses`, `KRESGE Co.` **and `VARIETY Stores`** | the press's own "top discounter" title in the very year of Wal-Mart's public offer — and the cross-index under VARIETY Stores is third-party evidence that the trade Wal-Mart came out of and the trade it entered were publicly the same trade |
| **F. W. Woolworth Co.** | "The old five-and-ten spreads new wings", cover, p. 58, Nov. 14 1964; "…is setting up **Worth Marts**, discount mass-volume stores", p. 24, Dec. 26 1964 | the largest variety incumbent moving into discount mass merchandising, two years after Wal-Mart's first store |
| **Korvette** | move upmarket, p. 72, Feb. 10 1962 | the existing national discount benchmark, in distress |
| **Grayson-Robinson** | cash bind p. 109 (page contested, A4 U-A4/1), Aug. 18 1962; bankruptcy court p. 146, Sep. 22 1962 | a named **failure** inside the founding year |
| **Parke Davis** | switching to sell directly to discounters, p. 54, Apr. 1962 | supplier-side competition for the discount channel |
| **Walgreen** | buying three Houston discount stores, p. 36, Mar. 24 1962 | a drug chain entering the trade in the founding year |
| **Aldens, Inc. / Gamble-Skogmo Inc.** | **"Small town greets the discounters"**, p. 90, Oct. 3 1964, indexed under `ALDENS, Inc.`, with the `DISCOUNT Houses` cross-entry continuing "**Gamble-Skogmo is opening franchised …**" | **THE DOSSIER'S MOST DANGEROUS FALSE POSITIVE (A4-20 / A4-30, registered as U-A4/8).** A headline that reads, to any modern reader, exactly like this company's story — a small town meeting discounters — attaches to two **Minnesota-based** chains. It is **not** a Wal-Mart item, and no pass may borrow its sentiment. The value of the row is that it proves **small-town discounting was a named, multi-firm, publicly reported programme in 1964**, and that this
corpus contains no Wal-Mart item that can be mistaken for it |
| **S. E. Nichols Company** | *Stores*, Dec. 1961: "operator of **Nichols Discount Cities since 1958**, and with a long previous history in variety stores" | a **variety-to-discount precedent printed in the company's own trade journal, before the company existed, and using the words "Discount Cities"** — the registrant's later narrative presents the conversion as its own venture; this row is §I's anti-hagiography instrument |
| **American Dixie Shops** (Richard Tumpowsky) | *Stores*, Dec. 1961: "more than 40 departments in discount stores"; volume "will hit $30 million next year"; $100,000–$150,000 of inventory per 8,000–10,000 sq ft leased department | a dated comparator that **disagrees in kind** — a leased-department operator's economics against Wal-Mart's whole-store margins (§H.4 prohibition 2) |
| **A Houston transit company** | "Bus line adds a destination: … opens a discount house to lure riders", p. 78, 1964 | the category's low entry barriers, as reported |
| **The unnamed chain that filed** | "Shake-out among discounters seen as chain files in bankruptcy", p. 83, Oct. 27 1962 | exit, in the founding year |

**I.3 finding (FACT about the press; INFERENCE Medium about structure).** The discount trade of 1962–1970
was **populated, ranked, counted and written about by third parties, and included national chains,
variety-store incumbents converting to discount, wholesale-affiliated operators already using the phrase
"Discount Cities", and demonstrable failures.** Wal-Mart entered that field as an unlisted participant
that none of this coverage noticed. **What the row does NOT support:** any statement that Wal-Mart's
format was derivative of Nichols's, Kresge's or Woolworth's — no document connects the founder to any of
them — and any statement that the rivals were weak.

### I.4 The 1962 competitive frame at Rogers, and two claims that stay OUT of this file

- **What else was open in Rogers, Arkansas in 1962: UNKNOWN.** No document in this corpus — registrant,
  index, or trade — enumerates the competitive set in any Wal-Mart town. The probe's **D4 brief**
  (newspapers.com Arkansas Gazette / *Southwest Record* 1962–70, local weeklies, the New York
  discount-injunction fights) **was never executed and its sources stayed blocked** (A2 §"NOT
  ESTABLISHED"; probe §Fleet briefs D4). **Record as a gap, not as an absence of competition.**
- **Two widely repeated competitor facts are NOT ADMITTED here, because they are not in this corpus:**
  (i) that Kmart's first store opened in **March 1962** under S. S. Kresge; (ii) that Kresge already
  operated **130+** variety stores in 1962. Both appear in the probe only as **instructions to verify**
  ("verify with dated sources", D4/§Fleet briefs), and **no dated source for either is on disk.**
  Neither number is written into §I, §P or §Q. **Status: UNTRIED**, and the fetch request for them is in
  this volume's hand-back list.
- **"Discount house" as a legal category was itself contested in-window:** resale-price maintenance was a
  live boundary — the company priced below suggested retail and promised to "meet or undersell local
  competition" **except for items covered by Fair Trade Laws** (S0105), the variety trade's journal
  editorialised on **mandatory functional-discount bills** (Jan. 1960), and a **Supreme Court
  franchise-law question** was indexed in April 1965 (S0117). Competition here is evidenced as a
  **regulatory and channel structure**, not as a market share contest.

### I.5 People in the room: interlocks, and what they are worth

Board composition is the one place competitor firms appear by name — **as affiliations of outside
directors, never as rivals** (A2 §Ownership and governance): FY1972–FY1973 — James H. Jones (President,
First National Bank of Commerce, New Orleans), H. L. Remmel (Senior VP, White, Weld & Co.), Jackson T.
Stephens (President, Stephens Inc.), i.e. **the two underwriters of the April 1972 offering sat on the
board**, and the same three outside directors were charged with the audit-committee review function;
FY1976 — "an active Audit Committee of the Board of Directors … In these days of loss of credibility by
corporate citizens"; FY1980 — J. R. Hyde III (Chairman and President, **Malone & Hyde, Inc.**, Memphis)
and Sidney A. McKnight ("President, Retired, **Montgomery Ward & Co., Incorporated**") — **two
retail-industry interlocks by 1980, and neither is discussed in any founding account in this corpus.**
Class: FACT (as printed in the officers' pages) · High. **Inference explicitly withheld:** no document
states that either director changed any competitive decision, and the Malone & Hyde connection must not
be read as evidence about grocery-adjacent strategy.

### I.6 Coda (§7 interpretive-duty check) and knowability

**Evidence:** the nine reports' competitor silence (I.1); the FY1973 exclusion clause and the 55 + 9
arithmetic (I.2); dated third-party index entries with pages and issues (I.3). **Mechanism, named only
where the documents name it:** the company competed on price inside a legal regime (Fair Trade), on
site terms secured by leases signed ahead of opening (§G.6), and with concessionaires whose sales it
reported but did not own (§E.1). **Alternative explanations retained:** the absence of named rivals may
be a **disclosure convention** of 1970s printed annual reports rather than an absence of competitive
awareness — no document licenses either reading; and the press's naming of Kresge and Woolworth may
reflect their **capital-markets salience** rather than their commercial relevance to an Arkansas chain.
**Confidence:** High (each printed row); **Medium** for I.3's structural inference; **UNKNOWN** for
competitive position, market share, and win/loss against any named firm — **no market-share figure for
this company exists in this corpus in any year.**

| State | Content |
|---|---|
| **KNOWABLE in-period** | the sector's named firms and named failures, from third-party print dated in-window; the company's own category language; the legal price regime |
| **NOT KNOWABLE in-period** | where this company stood in that structure: it is absent from every in-window count, index and ranking reached, so no contemporaneous observer could have placed it |
| **UNKNOWN, with the gap named** | the local competitive set at Rogers / Bentonville / Jonesboro in 1962–66; Kmart's 1962 scale (UNTRIED, not asserted); any share, traffic or price-comparison datum; whether any director's retail affiliation affected any decision |

---

## J. TECHNOLOGY

STATUS: WRITTEN 2026-09-26

**Frame adaptation (§7), declared because the standard frame does not fit.** §J's software/platform form
— stack, architecture, deployment, dependence on a third-party platform — **does not apply to a
1962–1970 discount retailer**, and pretending otherwise would import later categories into an earlier
period. The adapted equivalent, licensed by §7's hardware/infrastructure row (**prototypes, component
sourcing, yield**), is: **the data-processing apparatus, the physical plant of distribution and store
design, and the operating instruments that made a 40,000-square-foot self-service box controllable.**
Every row below is a quantity or a sentence printed in a document on disk, with its fiscal-year basis.

### J.1 Data processing, as filed

| Component | As printed | FY / source | Conf · basis |
|---|---|---|---|
| Central computer | the company **leases** an **IBM 370/135** | FY1976 · S0105 | High (CONTEMP). **Leased, not owned** — a vendor-dependence fact, and the only computing asset any report names before 1980 |
| What it maintained | **item-level** inventory for the Warehouse and Distribution Center; **classification-level** inventory per store; **all payroll and accounts payable**; **departmental sales analysis**; **store-by-store income statements** | FY1976 · S0105 | High. Note the **asymmetry the company itself documents: item-level at the DC, classification-level in the store** — the store did not carry item-level stock records |
| Point-of-sale capture | "**Singer electronic cash registers in 64 Wal-Mart stores and NCR mechanical and electronic registers in 61 Wal-Mart stores** record point of sale data" | FY1976 · S0105 | High (the sentence). **64 + 61 = 125 against a 125-store fleet is the company's own arithmetic**; "mechanical **and** electronic" is a mixed basis, so **how many stores captured sales electronically is UNKNOWN** — the document does not split the 61 |
| Merchandise-control innovation | a new **fashion-goods unit-control** system using "**computer prepared magnetic tickets**" | FY1976 · S0105 | High; **no throughput, error-rate or cost figure is printed** ⇒ effect UNKNOWN |
| Payroll scale through the system | "company-wide payroll for over 17,500 associates" in the data-processing account | FY1979 · S0108 | High (as stated). **The document says the payroll ran through the computer, not what it cost** — no payroll dollar figure exists for any year (§K.4) |
| Divisional structure | a **Fashion Distribution Center** and a **Claims Center** listed as divisions in the report contents | FY1979 · S0108 | High (as a name); each one's function is **not described** ⇒ UNKNOWN |

### J.2 The retrospective computing claim, and what the print will not support

The company's museum page carries, in its own curation prose, **"starting back in 1968 when Sam Walton
attended an IBM class for executives and installed Walmart's first computer—an IBM System/360 Model 20—
the next year. By 1977, Walmart had built a computer system designed for ordering merchandise directly
from suppliers"** (`sources/periodicals/walmart_museum_page.html`, a 1992-anniversary item; page
`dc:modifyDate` **2026-04-24**; A2 W-77).

- **Class: RETROSPECTIVE INTERPRETATION / company self-narrative**, made on a page last modified
  **57 years** after the first claimed event, with **no citation**.
- **Corroboration: 0.** No document dated 1968 or 1969 exists in this corpus that mentions a computer;
  **the earliest computing witness anywhere on disk is the FY1976 leased IBM 370/135** (S0105), and no
  report on disk describes a supplier-ordering system built by 1977.
- **What may be written:** "the company later asserted that its first computer was installed for fiscal
  1969". **What may not be written:** any Stage-1 sentence in which a computer existed at Wal-Mart before
  FY1976 as a matter of record. **Confidence: Low (assertion), UNKNOWN (event).**

### J.3 Plant and process technology — the physical operating apparatus

| Item | As printed | FY · source | Conf |
|---|---|---|---|
| Throughput design at Searcy | conveyor operating at approximately **200 ft/min**; a design **combining "DC I" warehousing with "DC II" distribution**; "capability of servicing one-half of the existing Wal-Mart stores" | FY1978 · S0107 | High |
| Dock capacity as a technology statement | the 1975 DC: **eight railroad-car and 37 truck doors**, "as compared with six railroad car and 28 truck doors in the original Distribution Center" | FY1975 · S0104 | High — the company chose to measure its own capacity in doors |
| Cycle time | a "**2½-day cycle**" at the Bentonville "pure distribution center" | FY1977 · S0106 | High (as stated); **the definition of the cycle is not printed** ⇒ basis UNKNOWN |
| Receiving cadence | stores receiving "two to three deliveries per week by the Company's own fleet of **118 trucks** manned by **146 drivers**" | FY1980 · S0109 | High; tractors and trailers were **leased** (S0105), so "own fleet" describes operation not ownership |
| Mechanisation | a mechanised **390,000 sq ft** facility "opened in Bentonville in January, 1980" | FY1980 · S0109 | High |
| In-house services technology | "plant for printing advertising circulars and newspaper inserts"; a 24,000 sq ft area for **labelling, sorting and quality control of wearables** inside the 261,800 sq ft GO/DC | FY1976 · S0105; FY1973 · S0102 | High; **U-A2/5 flags the 261,800 / 263,800 building-size disagreement** |
| Store design as experiment | Pine Bluff "Project '79", 62,400 sq ft, "planned, **not as a prototype, but to be an experiment in physical plant design, fixture composition and merchandise presentation**" | FY1979/FY1980 · S0108/S0109 | High that it was stated; **the experiment's result is not in any document** ⇒ UNKNOWN |
| Inventory-costing technology | the move **FIFO → LIFO effective January 31, 1975**, which "reduced net income for the year ended January 31, 1975 by **$2,347,000** or **$.18** per share" and which the auditor **approved** in a **qualified** opinion ("except for the change, which we approve, in the method of determining inventory cost as described in Note 2") | FY1975 · S0104; FY1976 · S0105; A3-025; A2 W-51; A3 §6.1 | High. **An accounting technique is technology in this frame**: it is the instrument by which the company measured its own cost of goods under inflation, and it breaks every margin comparison crossing 1975-01-31 (§L.3) |
| Shrinkage control | a **Security and Loss Prevention Division** running "programs in shoplifter apprehension, checker and **checkout supervisor training**, lay-away and gun control, and employee awareness", including "the investigation, interrogation and prosecution of persons apprehended for robbery, break-ins and thefts", with "Regular contact … maintained with the news media to publicize Wal-Mart's security policies"; by FY1980 a **Vice President-Loss Prevention** on the officers' list and an "aggressive campaign against shrinkage" in the margin discussion | FY1976 · S0105; FY1980 · S0109 | High (as filed). **No shrinkage percentage is printed for any year before FY1980's qualitative mention** ⇒ UNKNOWN |

### J.4 What is NOT attested in-window (recorded so a later pass does not fill it)

No barcode, no electronic data interchange with suppliers, no in-store terminal, no satellite or
network link, no warehouse management system, no e-commerce, and **no dollar figure for any technology
line — capital, lease payments on the IBM, or data-processing headcount — appears in any of the nine
reports.** Absence here is a property of what annual reports of this era disclosed and of what has since
survived; it is **not** evidence that the trade lacked these things, and it is **not** a claim about the
company's sophistication. Each is recorded **UNKNOWN**, and the four families that could still produce an
in-window witness (local print, trade titles off-IA, the NRMA roster genre, the SEC paper file) are
**UNTRIED** (§H.6, part 1 §A.2).

### J.5 Coda (§7 interpretive-duty check) and knowability

**Evidence:** the FY1976 data-processing and distribution pages (S0105), the FY1975/FY1977/FY1978/FY1980
plant sentences (S0104/S0106/S0107/S0109), the FY1975 LIFO note and the qualified opinion that covers it,
and the museum page's retrospective computer claim. **Mechanism (named, and only this far):** a leased
central computer took over work that had to be done anyway — payroll, accounts payable, DC inventory,
departmental and store profit — and the same reports show **rising distribution penetration, rising
throughput per node and a lengthening lease pipeline** in the adjacent fiscal years. **The causal claim
that computing *caused* the penetration rise cannot be made:** the percentages and the computer share one
document (FY1976) and no mechanism is printed in it, so **the relationship is CORRELATION ONLY, and
mechanism UNKNOWN.** **Alternative explanations retained:** the penetration rise may be the arithmetic
result of opening stores in DC-served towns; the LIFO change may be a tax-and-inflation response rather
than a systems change; the conveyor and door counts may be descriptions, not differentiators.
**Confidence:** High for each printed component; **Low** for any claim that the technology was unusual for
its period — **no comparator's data-processing or plant specification exists in this corpus** — and
**UNKNOWN** for its cost.

| State | Content |
|---|---|
| **KNOWABLE in-window** | that a leased IBM served the DC, payroll, payables and store reporting by FY1976; that point-of-sale data was captured from mixed Singer/NCR registers; that the company measured its own capacity in doors, conveyor speed, cycle days and deliveries per week; that inventory costing changed in FY1975 and the auditor flagged it |
| **NOT KNOWABLE in-window** | whether any of this distinguished the firm — no comparator's apparatus is in this corpus |
| **UNKNOWN, with the gap named** | the date of the first computer (asserted 1969/1970 on a 2026-dated page, unattested in-window); the split between electronic and mechanical registers; all technology costs; the outcome of Project '79; the function of the Fashion DC and Claims Center; shrinkage rates before FY1980 |

## K. MONEY / PERSONAL FINANCES

STATUS: WRITTEN 2026-09-26

**Scope, and the split that this section must not blur.** §K.1–§K.6 are **company money**, and almost
every row is audited registrant print with a contemporaneous/restated flag. §K.7 is **the founders'
personal finances**, and it is the emptiest subsection in Stage 1: **EDGAR's electronic history for this
issuer begins 1994-02-14, so no proxy, no statement of beneficial ownership, no Schedule 13D and no
registration statement from inside this window exists on disk** (part 1 §A.2 family (a); probe W-02).
Every number in §K.1–§K.6 is therefore a printed report's figure, and every statement in §K.7 is a gap.

### K.1 Equity events

| Date | Event, as the document states it | Money | Source | Conf · basis |
|---|---|---|---|---|
| **1970-02-01** | exchange of common stock accounted for as a **pooling of interests**; the principal shareholder **Walton Enterprises, Inc.** transferred shares in "the various subsidiaries" plus assets of certain related businesses, **subject to liabilities including an assumed $968,876 bank note**; "Excess of paid-in capital of pooled companies … at February 1, 1970 — $1,470,139" | group's consolidated capital beginning | S0101 Note 1 | High (CONTEMP as-filed). **This is the date the registrant group starts, and it is inside the audited notes** |
| **1970-10-08** | "**Excess of net proceeds over par value of 200,000 shares sold in public offering October 8, 1970 — 3,010,467**" | **net $3,030,467** ( = $3,010,467 excess + $20,000 par at $.10 × 200,000) | S0101 capital note; A2 W-03 | High (the note) · Medium that a 1972 document reporting a 1970 event is day-accurate. **DERIVED $15.15 net per share** = $3,030,467 ÷ 200,000, arithmetic shown; **gross offer price UNKNOWN** |
| October 1970 | "became a publicly-held corporation and became traded in the **over-the-counter** market" | — | S0103 | High. Independently consistent with the only non-registrant witness in Stage 1: the SEC's 31 Dec 1970 exchange-issuer register prints **WALGREEN … WALWORTH and zero Wal-Mart** (`S0139`) — a **negative**, corroborating venue only |
| **1972-04** | White, Weld & Co. and Stephens Inc. underwrote a further public offering; the sale of **400,000 common shares at $23.75 per share before expenses**; paid-in capital rose **$8,913,504**, plus **$464,300** from exercise of options and warrants for 112,950 shares, less **$15,000** "an initial stock exchange filing fee"; stock placed with **over 3,400 holders**, "which made us eligible for NYSE listing" | three coexisting totals: **$9,500,000** gross arithmetic, "**approximately $9,250,000**" in the letter, **$8,913,504** posted to paid-in | S0102 (letter + Note 4) | High (event, underwriters, purpose); **U-A2/4 open — the bridge between the three figures is not disclosed and no one of them is "the" raise** |
| **1972-08-25** | "the Company's stock was listed and began trading on the New York Stock Exchange" | venue change, **not a stock event** | S0103 | High (CONTEMP) |
| **1971-06-11 / 1972-04-05 / 1975-08-19** | three two-for-one splits are printed in this corpus, **not one**: 1,500,000 shares issued (par charge 150,000); 3,000,000 shares to be issued (par charge 300,000) — both inside S0101's own capital note; and "Common stock outstanding was increased **6,687,789 shares** by a two-for-one stock split effective **August 19. 1975**" (S0105 Note 4, with **$668,779** charged to capital in excess — 6,687,789 × $.10 par ✓) | par value **$.10** evidenced throughout | S0101; S0105 | High. **Only the 1975 split falls inside the restatement dispute**; A2's "in 1976" wording mislocates it and invites a double adjustment (COR-A3-07) |
| 1976 | authorised preferred raised **500,000 → 1,000,000** shares; authorised common **11,000,000 → 20,000,000** | — | S0105 | High |
| Share count at each FY-end | FY1971 **6,000,000** · FY1972 **6,000,000** · FY1973 **6,512,950** (FY1974 report) / **6,512,550** (FY1973 report) · FY1974 **6,542,250** · FY1975 **6,659,650** (RESTAT in FY1976) · FY1976 **13,418,063** · FY1977 **13,649,829** · FY1978 **14,867,711** (**stated only in the FY1979 report's comparative column: RESTAT**) · FY1979 **15,079,383** | — | S0101–S0109; A3 Table S3 | High, except **U-A3/3** on the FY1973 last digit, and the FY1978 figure is restated-only |
| Float sold publicly | **200,000 of ≈3,000,000 pre-split shares ≈ 6.7%** — **DERIVED** (6,000,000 ÷ 2 = 3,000,000; 200,000 ÷ 3,000,000) | no document states a float percentage | DERIVED from S0101 rows | Medium; **INFERENCE on the pre-split base** |

### K.2 Debt, leases, and how growth was actually funded

| Item | As printed | FY · source | Conf · flag |
|---|---|---|---|
| The funding sentence | "the financing of new store inventories and fixtures was **primarily through the reinvestment of earnings, combined with bank borrowings, until May, 1975**, at which time, the Company issued **$15 million of convertible subordinated debentures**" | FY1976 · S0105 | **High — this is §K's central fact.** Expansion was internally funded plus bank credit until a single convertible issue, **five years after the public offering** |
| Bank credit | a revolving bank loan of **$5,056,000 at FY1975** stood **nil at FY1976** | FY1976 · S0105 | High |
| Note structure | **9¾% notes** agreement carrying the retained-earnings restriction; scheduled maturities $842,713 (1974), $441,614 (1975), $387,813 (1976), $324,765 (1977), $304,219 (1978); 8¼% and 9% mortgage notes running to December 1989 **paid off out of new 8¼% notes to January 1988** | FY1973 · S0102 Note 3 | High |
| Conversion | **$630,000** of debentures converted during FY1976; **1,336,744** shares reserved for debenture conversion at 1976-01-31 | FY1976 · S0105 Notes 3/4 | High |
| **Covenant-restricted earnings** | **$5,660,237** (FY1973) → **$22,235,000** (FY1976) → **$50,021,000** (FY1980) | S0102; S0105; S0109 | High. **The dividend record in K.3 is the residue of a restricted-capital business, on the company's own filing** |
| Debt, as carried | long-term debt **$4,659k** (FY1972) · $5,066k (FY1973) · $10,578k (FY1974) · $11,132k (FY1975, RESTAT in FY1976) · $17,531k (FY1976) · **$23,245k** (FY1977 as its own report prints) **or $19,158k + $4,087k capital leases** (FY1978's split) · $21,489k (FY1978) · $25,965k (FY1979) · $24,862k (FY1980) | A3 Table S4; S0106/S0107 (A3-012) | High; **U-A3/9 records the FY1977 one-line vs two-line presentation. Debt/equity for the same date is 0.351 or 0.289 depending on which print is used** |
| **The off-balance-sheet estate** | FY1976 disclosed **$38,416,000** of "noncapitalised financing leases of stores", whose capitalisation "would cut FY1976 net income ~**$515,000**"; and **total lease commitments of $106,501,000 against $17,531,000 of recorded long-term debt** in the same year. By FY1980: **capital-lease obligations $97,212,000 long-term + $2,704,000 current against long-term debt of $24,862,000**; total minimum rentals $85,420,000 operating / $228,319,000 capital; present value $99,916,000 at imputed **8.5%–13.5%** | S0105; S0109 (A2 W-52, W-73); A3-036 | High. **Leases, not debt, were the balance sheet** |
| **The basis break that invalidates cross-year asset ratios** | FY1978 total assets **$206,691 thousand as published** (S0107) vs **$251,865,000 as restated** (S0108) — **+45,174,000**, from capitalising leases under SFAS-13 (long-term capital-lease obligations 10,904 → 59,003; equity 98,943 → 96,482; retained-earnings restatement **(2,461,000)**); S0108 prints "All financial information has been restated to reflect the retroactive application ot [sic] Statement of Financial Accounting Standards No. 13" | S0107 / S0108 | High. **U-A3/6 + COR-A3-05. Register rule inherited: any asset-turn, debt/assets or total-asset growth figure computed across 1978-01-31 / 1979-01-31 is invalid, and 0.327 → 0.771 is a presentation change, not a leverage event** |
| Equity carried | stockholders' equity **$3,159k** (FY1970, RESTAT in FY1978) · $7,841k (FY1971) · $10,748k (FY1972) · $24,754k/$24,753,623 (FY1973) · **$30,734,128 (FY1974, exact, CONTEMP)** · $36,935k (FY1975, RESTAT) · $48,454k (FY1976) · $66,183k (FY1977) · **$98,943k as published / $96,482k as restated (FY1978)** · $127,476,000 (FY1979) · $164,844k (FY1980) | A3 Table S4 | High (CONTEMP years), Medium (FY1970–FY1975, restated-only) |
| Return on capital, **as printed** | return on assets 20.7 (FY1970, **not checkable** — the denominator is FY1969 assets, which no document states) → 19.5 (FY1971) → 19.0 → 16.1 → 13.3 → 10.6 → 15.3 → 16.5 → 16.4; return on equity 49.4 → 52.3 → … → 31.2 → 34.1, all "**On beginning of year balances**" per the table's own footnote, and A3 verified each ratio against the table's own rows | S0107/S0108 nine- and eight-year tables | High **as printed**, with the FY1970/FY1969 dependency stated (A3 §5.7). **Not re-derived here** |

### K.3 Distributions to shareholders, and one refuted row

| FY | Dividend per share | Basis | Source |
|---|---|---|---|
| FY1968–FY1973 | **—** (the nine-year table's own cell prints an em-dash: not reported) | — | S0107 |
| **FY1974 / calendar 1974** | **$.025 paid 5 April 1974 and $.025 paid 7 August 1974**, semi-annual — the **earliest evidenced dividend payment anywhere in this corpus**, falling inside **fiscal 1975** (FYE 1975-01-31) | RESTAT (printed in the FY1978 nine-year table and in the FY1976 report's prior-year column) | S0105; S0107 · A3 Table S3; A2 W-54 |
| FY1975 | **$.015** (4 Apr 1975) + **$.015** (1 Jul 1975) + **$.015** (3 Oct 1975) + **$.02** (2 Jan 1976) | CONTEMP quarterly table | S0105 · High |
| FY1976 | **$.065**, "dividends were increased in the third quarter from an annual rate of 6 cents to 8 cents a share" | CONTEMP (reprinted FY1977, FY1978) | S0105 |
| FY1977 | **$.085** | CONTEMP | S0106 |
| FY1978 | **$.16** — quarterly **$.025 / $.045 / $.045 / $.045** ✓ | CONTEMP; also restated as "$.16 per share" in S0108's Note | S0107; S0108 |
| FY1979 | **$.22** — four quarters at **$.055** ✓ (income-statement parenthetical) | CONTEMP | S0108 |
| FY1980 | **$.30**, raised to **$.40** after year end | CONTEMP | S0109 |
| **REFUTED ROW** | the FY1980 ten-year summary's dividend row prints **1976 $.09 / 1977 $.11 / 1978 $.19 / 1979 $.25**, which each year's own document refutes (**.065 / .085 / .16 / .22**). **No split factor reconciles them** ($.09 ÷ $.065 = 1.38 is not a split ratio) — COR-A3-04 | **the row is kept on the record as printed, not deleted**; the contemporaneous values govern | S0109 vs S0105/S0106/S0107/S0108 · **High that the four-year row is wrong** |

> **PROHIBITION.** No row in §P or in `quantitative.csv` may carry the FY1980 table's 1976–1979 dividend
> values, and no "dividend growth" series may be built by mixing the two sets. The company's own
> nine-year dividend row and its own contemporaneous quarterly table are **the same lineage disagreeing
> with itself**, which is a disclosure defect to report, not a second source to choose between.

### K.4 Employee capital, and the labour cost that is not printed

Profit-sharing plan **adopted by the Board in FY1972** ("A new profit sharing program was adopted by our
Board of Directors for all regular Wal-Mart employees"), contribution **$275,000 in FY1973** ("largest
sum ever"); **eligibility shortened from two years to one effective 1976-02-01, 824 associates added**; a
qualified option plan (grants at **$4.12** in FY1971) and warrants for **180,000 (1972) / 90,000 (1973)**
shares at **$4.12 expiring 1 April 1985**; an employee stock purchase plan (**60,000 shares reserved
1973**); a **nonqualified** option plan (**985,587 shares, 1976**, expiring in ten years in nine annual
instalments); **2,537,281 shares reserved** at 1976-01-31 in total; **831,237 shares under option at
grant prices $2.06–$14.25** (S0101, S0102, S0105 — A2 §"Employee ownership"). Class: **FACT**, High.

**What is NOT there:** no document on disk prints a **payroll total, wage bill, average wage, hourly
rate, or headcount-cost ratio for any year FY1962–FY1980** (A3 §5.7: "no document on disk prints capex,
payroll, or wage totals for any year in this window"; FY1979's "company-wide payroll for over 17,500
associates" says the payroll ran through the computer, **not what it was**). **Capital expenditure per
store, selling cost per store and payroll per associate are therefore UNKNOWN**, and no §L productivity
claim may be costed.

### K.5 Tax, and profit the state capped

- Effective income-tax rate, computed only where both inputs are printed: **43.7% (FY1970) · 47.9%
  (FY1971) · 47.8% (FY1972) · 48.5% (FY1973) · 48.2% (FY1974) · 48.0% (FY1975) · 49.5% (FY1976) · 48.0%
  (FY1977) · 48.1% (FY1978) · 48.1% (FY1979) · 44.6% (FY1980)** — **DERIVED** (`taxes ÷ income before
  income taxes`), arithmetic at A3 §5.5, and the company's own statement that the rate "has consistently
  approximated 48%" checks (S0105). **The single-step FY1980 break to 44.6% is a tax story, not an
  operating one.** High as arithmetic; the FY1970 ratio rests on a row pair that does not close to the
  printed pre-tax figure (**U-A3/2**), so **FY1970's tax rate is printed-with-caveat, not trusted.**
- **Price policy constrained reported earnings directly:** FY1973 "we were tightly controlled this past
  year by the guidelines of the **Wage and Price Control programs Phase II and Phase III**. **Our earnings
  are close to the maximum allowed by these regulations**" (S0102). Class: FACT (as management disclosed,
  inside audited statements) · High. **Anti-hagiography value: early-1970s margins were not unconstrained
  pricing power.**
- **IRS reassessment of the pre-IPO group:** proposed assessments for the years ended **1969-01-31 and
  1970-01-31**, on surtax-exemption disallowance and inter-subsidiary reallocation, contested (S0101 Note
  6; S0102 Note 6) · High. **The tax authority was, in other words, already auditing the years this stage
  ends in — and its outcome is not in this corpus** ⇒ UNKNOWN.
- **Separate returns prove multiple legal persons:** through FY1972 "The Company and its subsidiaries file
  separate income tax returns"; a **consolidated** federal return was filed first for the year ended
  1973-01-31 (S0101; S0102) · High (see part 1 §B.0).

### K.6 The founder's personal finances — the gap, named

| Question | Answer | Why, and what would settle it |
|---|---|---|
| What did Sam Walton hold in 1962 / 1970? | **UNKNOWN** | no shareholder register, minute book, proxy or beneficial-ownership filing exists on disk for any pre-1994 date (probe W-02); **Walton Enterprises, Inc.** is named as "**the principal shareholder**" and is **never sized** (S0101 Note 1) |
| What was it? | **UNKNOWN** | no document states what Walton Enterprises, Inc. **was** (partnership, corporation or trust), who held it, or when it was formed (A2 §Ownership and governance) |
| Source of the 1945 and 1950 capital; purchase price; rent; the lease and its terms | **UNKNOWN / EMPTY within the stated perimeter** | no corporate statement at any date mentions 1950, a 1950 Bentonville store, a purchase price, a rent or a lease loss; the museum's claimed holding of a **1950 bill of sale** is a lead whose **bytes are not in this repository** (probe W-21; part 1 §B.2). **County deed records (Benton County Circuit Clerk; Mississippi County for Newport) are UNTRIED** |
| The founder's salary, dividends received, or personal borrowing | **UNKNOWN for every year** | no compensation disclosure of any kind is printed in the nine reports; the only personal-side corporate trace is **"Amounts due from stockholder (113,955)"** in the **FY1971** column — a related-party **receivable** from a stockholder, with the **counterparty unidentified** (S0101) · High (line), **UNKNOWN** (person and meaning) |
| Family ownership percentage | **UNKNOWN** | the only ownership sentence in the corpus is the uncited company page, "**The Walton family owns 24 stores**", whose "1967" label corresponds to **FY1968** as filed (part 1 §A.1, trap row) |
| "He financed the first store with a $X loan from Y" | **NOT ADMITTED** | memoir lineage; its bytes are not in this repository and no pre-1992 witness exists in it. **UNTRACEABLE** (probe §Famous claims) |

**independence_note for §K.** The **only** datum in this section with a genuinely independent origin is the
SEC's 31-Dec-1970 register negative (`S0139`), which speaks to listing venue and to nothing else. Every
dollar, share and covenant in K.1–K.6 traces to **S0101–S0109 plus Arthur Young's nine opinions** — one
lineage, and repetition across reports is version evidence.

### K.7 Money measured on three different rulers (basis breaks in one place)

1. **FIFO → LIFO, effective 1975-01-31**, cutting FY1975 net income by **$2,347,000 / $.18** (restated
   basis) or **$2.3 million / $.36** (the company's pre-split contemporaneous statement — the two
   reconcile, A3-025) · the FY1975 opinion is **qualified** for it.
2. **Pre-SFAS-13 → post-SFAS-13, FY1979**, grossing FY1978 total assets from **206,691** to **251,865**
   thousand and cutting FY1978 net income **21,886 → 21,191**; the FY1979 opinion carries the
   retroactive-restatement clause. **A3's own prose-vs-lines disagreement survives inside one document:**
   the FY1979 Chairman says the restatement "reduced net earnings **$769,000**, or 5 cents per share"
   while the statement lines give **695** — **the $74,000 gap is not reconciled anywhere on disk, and the
   "5 cents" fits 695 better than 769** (A3-035, U-A3/5).
3. **Historical cost → constant dollars, disclosed once (FY1980, SFAS-33, unaudited by definition):**
   FY1980 constant-dollar net income **$27,146 thousand against $41,151 thousand reported**, with a "Gain
   from decline in purchasing power of net amounts owed" of **$28,422 thousand** and a **55%** effective
   tax rate on the adjusted earnings; revenues restated at **$1,015,738 / $826,476 / $621,654 / $466,630**
   thousand for FY1979/78/77/76 against CPI averages **219.8 / 196.9 / 182.5 / 171.2 / 162.1**; year-end
   market price per share **$33.58 / $24.30 / $22.31 / $17.40 / $17.97**; and replacement cost of
   inventories exceeding LIFO carrying cost by **$38,899,000** (FY1980) and **$22,271,000** (FY1979)
   (S0109 Notes 9 and 2). Class: FACT (the disclosure) / **ESTIMATE** (the constant-dollar figures).
   **Anti-hagiography value, in the company's own words: by 1980 it was publishing that roughly a third
   of its nominal profit was an artefact of measuring cost in unadjusted dollars.**

**Market price coverage:** **no price exists before fiscal 1975.** The first price table anywhere in the
corpus is the FY1976 report's quarterly high/low grid (FY1976 $10.3125/$7.00 … $15.75/$12.625; FY1975
$9.375/$7.25 … $7.6875/**$3.6875**), restated for the split (S0105; A2 W-54) · High. The **$16.50** on the
company's own timeline page and the **derived $15.15 net** from the FY1972 note are **not reconciled and
no local document licenses a bridge between them** — U-A2/2 stays open, and §K does not close it.

---

## L. VALIDATION SIGNALS

STATUS: WRITTEN 2026-09-26

**What §L may and may not do.** A validation signal is evidence that **repeatability** had been
demonstrated **to someone at the time**. Two constraints bind here harder than anywhere else in this
volume: (1) **every quantitative signal is a registrant self-report** — no independent count exists (§H.6,
U-A4/4: "press vs filed figures: still none, and that is the finding"); and (2) **the company chose which
signals to publish, and the corpus preserves that choice.** So §L lists both: the signals the company
selected (§L.1–§L.3) and the ones it printed anyway (§L.4). **§M (part_3) owns the failures register;
§L records only the validation-side consequence of each.**

| Date | Signal | Magnitude | What it demonstrated | What it did NOT demonstrate | Source | Confidence |
|---|---|---|---|---|---|---|
| FY1968 | first counted year anywhere in the corpus | 24 stores, **$12,618,754** | that a countable business existed | that the model was validated — **FY1962–FY1967 are EMPTY**, so the six founding years are uncounted; and the row is a **1972-dated restatement** labelled **pro forma** by the company | S0101 (RESTAT) | Medium |
| FY1972 (a 1972 sentence about 1970–71) | eighteen unexpanded stores grew sales | **+17%** | that stores **already built, in their original size, in towns already chosen** grew without new capital — the single most direct repeatability claim inside the window | anything about **which** eighteen stores, their towns, or their sales; and it **excludes** expanded units, so it is a selected population | S0101 President's message (W-07) | High that it was stated · Medium as a measurement |
| FY1973 | "our old stores, same size, had a healthy **11%** increase" | +11%, **excluding one store near a new Wal-Mart store** | continued same-store growth **and**, inadvertently, self-cannibalisation | that growth was sector-wide: the exclusion is an admission that a new store took volume from an old one | S0102 (W-32) | High (printed with its own exclusion) |
| FY1975 | distribution penetration | **55% → 60%** of merchandise through the DC | that the company was capturing its own goods flow measurably | that the model depended on it; and **no earlier penetration figure exists at all** | S0104 | High |
| FY1975 | new store space in one year | **1,083,326 sq ft**, "a record for new store space in a single year"; 26 new + 2 enlarged; fleet **104** with the state table summing to 104 ✓ | that the unit could be reproduced ~26 times in a year inside a self-imposed radius | profitability of the new units; the record's comparability (no prior total square footage is printed) | S0104 | High (CONTEMP) |
| FY1975 | LIFO charge | net income **$6,353k** reported vs **$8.7m** "had we not made the decision to change" | that the reported growth curve is **after** a deliberate $2.3m / $.36 charge | that operating performance was stronger than reported — the counterfactual is the company's own | S0104; S0105 | High; **a discount to the signal, not a bonus** |
| FY1976 | "the best year in the company's history to that date" | sales **$340.3m (+44%)**; incl. leased departments **$368.7m** vs $255.8m; net income **$11.5m / $.80** diluted (**+81%** over FY1975's $6.4m / 48c); stores **125**; space **5,295,000 sq ft (+23%)**; stores open a full year **+15%**; expense ratio improved **21.1% → 20.5%** | simultaneous growth in revenue, units, space, per-store volume and expense efficiency — the fullest multi-metric validation print in the stage | that any of it was externally verifiable; **the "+81%" partly reflects the prior-year LIFO charge**; the "best ever" frame is unfalsifiable within a company's own history | S0105 | High (CONTEMP) |
| FY1976 | distribution penetration | **80%** of store purchases through Bentonville, "the balance … shipped directly to the stores from suppliers" | that company distribution had become the majority channel — **the earliest quantified penetration measurement in this record** | when the crossover happened; and it bounds, but does not date, the pre-1970 wholesaler accounts | S0105 (W-57) | High |
| FY1977 | penetration restated in the company's own words | "increased from **60% to 80%** within the past two years" | internal consistency of the two-year move | nothing new; a later restatement of an adjacent claim | S0106 | High |
| FY1978 | the only same-store figure printed anywhere in the nine documents | "**Comparable stores sales (excluding the effect of new stores) increased 17 percent**"; total sales +42% ("an increase of 42 percent", matching the derived **+41.7%**) | that mature-unit growth and total growth were both strong in the same year | **what "comparable" meant — the population and dollar base are not defined in the document, so the metric's denominator is UNKNOWN** | S0107 | High that stated · Medium as economics |
| FY1978 (DERIVED from the two rows above) | new-store vs mature-store volume | new stores ≈ **$2,815,519** each against comparable stores ≈ **$3,661,466** ⇒ **a new store opened at roughly 77% of a mature store's volume** | that the two company numbers are mutually consistent | that the format "worked": a 23% opening gap is a **validation-side caution**, and its mechanism is **UNKNOWN — the document offers none**. 42 is a **net** count (30 openings, 10 expansions/relocations, 16 acquired, 4 closed) | DERIVED, A3 §5.2 | Medium (arithmetic) · Low (any interpretation) |
| FY1979 | scale milestone, contemporaneous | net sales **$900,298,000** (+32.7% derived; company "up 33 percent"); **229** stores; **10,200,000 sq ft**; "over 17,500 associates"; equity **$127,476,000** | that the model scaled to nine figures on its own print | that anyone outside the company had noticed: **no press or trade figure for Wal-Mart exists in this corpus for any year through 1980** | S0108 | High (CONTEMP) |
| FY1979 | expense discipline, company's own delta | "Expenses increased **.4 percent** of sales in 1979 from 1978" — which **only closes against the RESTATED FY1978 expense ratio (20.53%)**, i.e. 20.95 − 20.53 = 0.42 | that FY1979's own comparison was made on restated figures — **independent confirmation of the restatement's reality inside one document** | that expense control held: the ratio **rose**, and it rose again to 20.2% (FY1980, stated as a ratio only) | S0108; A3 §5.5 | High |
| FY1980 | comparable stores | **+15.3%**; productivity "approximately **$110 per square foot, excluding licensed departments**", with the report specifying that "Sales per square foot are calculated using **gross space as opposed to selling area**" | that mature-unit growth persisted | comparability with FY1973's selling-area-based Cornell benchmark — **different denominators, must never be trended** | S0109 (W-70) | High |
| FY1972 → 1975 | capital-markets validation | "over **3,400** holders", "**which made us eligible for NYSE listing**"; listing 1972-08-25 | that dispersed ownership was achieved — **and the company states the causal order itself: the equity distribution was the *condition* for the listing, not its consequence** | investor quality, hold rates, or price stability; **no price exists before fiscal 1975** | S0102; S0103 | High |
| FY1973 / FY1975 / FY1976 | employee-capital validation | profit sharing adopted FY1972, **$275,000** FY1973 ("largest sum ever"); eligibility 2 years → 1 year effective 1976-02-01 with **824 added** | that the company was spreading ownership claims internally as a stated programme | any effect on sales, turnover or service — **no document measures it**, and reading it as a demand or productivity driver would be hindsight | S0101; S0102; S0105 | High (as stated) · **UNKNOWN (effect)** |
| FY1973 | external benchmark cited | sales per square foot of selling area "well above the national average for discount store chains **surveyed for the Cornell study**" | that the company positioned against a named peer set | **anything at all about the benchmark** — the study is not in this evidence set; contents, sample and rank UNKNOWN | S0102 (W-38) | Medium (statement) · UNKNOWN (substance) |
| FY1980 | external ranking reported | Forbes "Annual Report on American Industry" **First Place** among major discount, variety and department store chains, four years running on a five-year average | that a third party had by 1980 ranked the company first — **the only external ranking in the corpus** | the ranking's method or peer list (**the Forbes volumes are not on disk**), and it post-dates the window's interior years it is used to characterise | S0109 (W-76) | High (that it was reported) · UNKNOWN (the ranking) |

### L.1 Growth, with every step's basis visible

**DERIVED** from §5.1 of `research/A3_audited_series_1962_1980.md`; the inputs' basis flag is what makes
the row usable. FY1968→69 **+69.3%** · →70 **+44.5%** · →71 **+43.5%** (all RESTAT in S0101/S0103) ·
→72 **+76.2%** (RESTAT→CONTEMP) · →73 **+60.1%** · →74 **+34.2%** · →75 **+41.0%** (CONTEMP→**DERIVED top
line**) · →76 **+44.1%** · →77 **+40.7%** · →78 **+41.7%** (company states "42 percent" ✓) · →79 **+32.7%**
(company states "up 33 percent" ✓) · →80 **+38.6%**.

**The consistency result and its limit (INFERENCE, High as arithmetic).** Two company-stated round numbers
and two independent derivations agree to **0.3 points** in both overlapping cases, which is the strongest
internal-consistency evidence in the whole stage: **the growth curve is a real ~33–44% plateau from FY1975,
not a construction of a later report's table.** What it is *not* is evidence of a market: **a company that
did not exist in any count before FY1968, and in any press figure before 1980, grew only in its own
documents for the first six years of this stage.**

### L.2 Per-store validation, and the denominator that cannot be fixed

**Sales per store (DERIVED; year-end count as denominator)**: FY1968 $525,781 · FY1969 $791,299 ·
FY1970 $964,458 · FY1971 $1,165,421 · FY1972 $1,529,690 · FY1973 $1,951,393 · FY1974 $2,148,217 ·
FY1975 $2,271,240 · FY1976 $2,722,648 · FY1977 $3,129,458 · FY1978 $3,479,262 · FY1979 $3,931,432
(A3 §5.3; FY1980 $4,522,377).

**Basis warning, binding on every row:** the denominator is a **period-end** store count while the
numerator is a **whole-year** revenue, so years with heavy back-half openings are penalised and **an
average-store count is not stated for any year** — the correct version of this metric has an **UNKNOWN
denominator**. Note the **FY1974→FY1975 flattening (+6.1% against +11.3% before and +19.9% after)**:
FY1975 is the year of both the record 26-store build and the LIFO charge, and **the two effects are not
separable from the documents on disk** — recorded as a shape, not an explanation.

**Sales per square foot (DERIVED; series cannot start before FY1976)**: FY1976 **$64.27** · FY1977
**$73.66** · FY1978 **$79.82** · FY1979 **$88.26** · FY1980 **$99.06**. **Three different labels across
four years** ("total space" / "floor space in operation" / "retail space occupied") with no definition in
any of them ⇒ **the series is comparable only if the labels name the same quantity, which the documents do
not establish**; FY1977 inherits the company's own word "approximately"; and FY1980's $110 figure is on
**gross space excluding licensed departments**, a fourth basis. For **FY1962–FY1975 the answer is UNKNOWN
because the denominator is never stated**, not because the arithmetic was refused.

### L.3 Unit-economics validation

- **Gross margin (DERIVED, `(sales − cost of sales) ÷ sales`)**: FY1970 25.91% · FY1971 25.88% ·
  FY1972 24.90% · FY1973 25.46% · FY1974 **26.39%** · FY1975 **25.24%** · FY1976 26.11% · FY1977 26.34% ·
  FY1978 25.74% · FY1979 26.57%; FY1968–FY1969 **UNKNOWN (cost of sales is not printed for either year in
  any document)**. The company's own stated ratios match the derivations to 0.1 point in **five** cases
  (26.4 / 25.2 / 26.1 / 26.3 / 25.7), which is the cleanest cross-check in the corpus. **But every
  comparison crossing 1975-01-31 straddles the FIFO→LIFO break and must say so** (A3-025, §5.5).
- **Expense ratio (DERIVED)**: 19.16% → 19.06% → 18.31% → 19.10% → 19.72% → 20.36% → 20.01% → 20.43% →
  20.33% (published) / 20.53% (restated) → 20.95%. **Direction: rising.** The company's FY1976 letter
  states 20.5% of sales while its own analysis states 20.0% — **unresolved in A3 §5.5 and kept
  unresolved here.** A rising expense ratio alongside rising sales and rising space productivity is the
  **least flattering consistent series in §L**, and it is contemporaneous.
- **Inventory-based ratios**: **not computed** for FY1974/FY1975 (cost of sales and inventories never
  coexist in one document for those years) and **not comparable across the FY1975 LIFO line** for any year
  (A3 §5.7). LIFO reserves that *are* printed: **$7,081,000** (FY1976), **$10,590,000** (FY1977),
  replacement cost **$14,148,000** higher (FY1978) and **$22,271,000** higher (FY1979), **$38,899,000**
  (FY1980) — the reserve roughly **quintupling in four years**, which is inflation living on the balance
  sheet rather than in the income statement. **INFERENCE, Medium:** under-LIFO reported margins were being
  held flat while the understatement of inventory grew; **the documents do not say this and no such
  sentence may be attributed to management.**

### L.4 Signals the company did not select, and printed anyway

These are §L's most load-bearing rows for the firewall, because they show the registrant's own documents
carrying evidence **against** its narrative. **§M (part_3) owns each as a failure; here each is recorded
as the limit it places on a validation claim.**

1. **A format opened, judged and shut.** Two Sav-Co Home Improvement Centers counted at FY1975, still
   below "our expected profitability level" at FY1976, remaining unit closed in FY1979 → **the
   repeatability claim is banner-specific, not company-wide** (S0104, S0105, S0108).
2. **A banner liquidated.** Ben Franklin variety units 14 (1970-01-01) → 9 (FY1973) → 2 sold and 4 closed
   in FY1974 → last dated trace closed January 1976 → "completely phased out" → **the base the company
   says it grew from was itself run down over the decade of validation** (S0109, S0102, S0103, S0105).
3. **Self-cannibalisation inside the metric.** FY1973's +11% excludes "one store near a new Wal-Mart
   store" → **growth was partly internal reallocation** (S0102).
4. **Physical loss.** "three of our older and most profitable stores were totally destroyed or damaged —
   two by fire, and one by tornado" in FY1973 (Dexter MO, Morrilton AR, Berryville AR), with Berryville
   reopened as a Discount City → **a record-breaking year was recorded despite losing three of its best
   units** (S0102; A3-017 for the FY1974 rebuilds at Jonesboro and Berryville).
5. **A regulatory cap on the profit line.** FY1973 "Our earnings are close to the maximum allowed by these
   regulations" (Wage and Price Control Phases II and III) → **the growth series is policy-truncated**
   (S0102).
6. **An accounting choice that reduced reported earnings by 41%.** The LIFO switch (S0104; S0105).
7. **A restatement the company published against itself.** FY1978 as published vs as restated under
   SFAS-13; and the FY1980 ten-year table's dividend row, refuted by four earlier documents (§K.3).
8. **Inflation accounting that cut the profit by a third** (FY1980 constant-dollar **$27,146k** vs
   **$41,151k**, unaudited by definition) (S0109).
9. **A new store opening at ~77% of a mature store's volume**, mechanism UNKNOWN (§L.1).
10. **A supplier-concentration disclosure the corpus cannot read** (§G.5) — evidence that the question was
    asked, and a permanent gap in §L's ability to describe buying power.

### L.5 Coda (§7 interpretive-duty check) and knowability

**Evidence:** the rows above, all printed in the nine reports or derived from two rows of one report with
the arithmetic shown. **Mechanism, where the documents give one:** capital was restricted, so growth was
paid for from earnings and bank credit until May 1975, and the store count and square footage are the
visible trace of that (§K.2, §G.3). **Where they do not:** the mechanism connecting any published signal
to a cause — why FY1975 per-store volume flattened, why a new store opened 23% below a mature one, why
comparable-store growth fell from 17% (FY1978) to 15.3% (FY1980) while totals grew 38.6% — is
**UNKNOWN**, and no document in this corpus offers an explanation for any of the three.
**Alternative explanations kept live:** growth may reflect **town selection, price controls, inflation
accounting conventions and acquisition** rather than any operating innovation; the four overlapping
company/derived consistency checks prove **honesty of the tables**, not **success of the model**.
**Confidence:** High for each printed quantity and each labelled derivation; **Medium for the growth curve
as a trajectory**; **Low for every claim that these signals validated the format rather than the fiscal
year.**

| State | Content |
|---|---|
| **KNOWABLE in-window** | the growth curve from FY1968 (as restated) and FY1972 (as filed); same-store figures the company chose to publish; sales per store; margins and expense ratios; DC penetration; per-year unit additions; the covenant and cap constraints on retained profit |
| **NOT KNOWABLE in-window** | that any of it was externally visible: **the only witness to every signal in §L is the company's own print plus one auditor.** No press figure for Wal-Mart exists in this corpus for FY1962–FY1980 (U-A4/4) |
| **UNKNOWN, with the gap named** | FY1962–FY1967 in its entirety; the definition of every comparable-store population; total square footage before FY1976; payroll, capex and every cost-per-unit; the outcome of Project '79; whether the four-state estate of 1970 was profitable store-by-store |

**RECORD-SELECTION NULL, applied to §L (§2).** That the validation record is **dense from FY1972 and mute
before FY1968** is an artefact of which archive survived, not of when the business became measurable: the
FY1970 report — the first audited public-company year, and the likeliest carrier of a "History" paragraph
and of the offering's terms — **does not exist in this corpus**, and the Internet Archive run starts at
FY1972 (probe W-80: `title:("wal-mart") AND year:[1962 TO 1971]` → **numFound 0**, an admissible empty
because the same query style returns known-good hits in the same index). The six founding years are not
quiet in the record; **the record that could describe them was never printed, or never kept.**

---

>>> REGISTER ROWS FOR MERGE <<<

*Emitted, not written: this pass does not own the register CSVs (`research/sources.csv`,
`quantitative.csv`, `timeline.csv`, `conflicts.csv`). Column order is exactly the header order fixed in
method §13. `stage` uses the literal `stage1`. Ids already registered are **not** re-emitted; every
`source_id` cited below already resolves in `sources.csv` except **`S0139` and `S0140`**, whose rows are
requested first because §K.1, part 1 §A.1/§A.2 and the SEC-register negative all point at them.*

### `sources.csv` — 4 rows (three documents §§E–L and part 1 cite by path but which carry no register id; one government register row)

```
source_id,stage,claim_supported,source_title,author_or_publication,source_type,primary_or_secondary,event_date,publication_date,access_date,url,archived_url,tier,evidence_class,confidence,independence_note,relevant_passage,notes
S0139,stage1,"The company was NOT exchange-listed as of 31 December 1970: the issuer register prints WALGREEN ... WALWORTH and zero occurrences of Wal-Mart",Securities Traded on Exchanges as of December 31 1970,U.S. Securities and Exchange Commission,government statistical register,primary,1970-12-31,1971,2026-09-25,https://archive.org/details/IA-securitiestraded1970unit,sources/gov_docs/SEC_SecuritiesTradedOnExchanges_asof-1970-12-31_IA-securitiestraded1970unit.txt,1,FACT (of absence),High,"THE ONLY NON-REGISTRANT ORIGIN IN STAGE 1, and it is a negative: an SEC compilation independent of the issuer, but it registers listing status only and corroborates no dollar, store or rate",WALGREEN ... WALWORTH; Wal-Mart 0 occurrences of 153481 words read whole,"W-block legible, so OCR loss is excluded (A5-04); corroborates S0103's 'over-the-counter market' statement and nothing else"
S0140,stage1,"The SEC Statistical bulletin (Nov 1970) does not name the company; its only issuer-naming table is a fixed sample of 100 selected common stocks on the NYSE",Statistical bulletin November 1970,U.S. Securities and Exchange Commission,government statistical publication,primary,1970-11-01,1970-11,2026-09-25,UNKNOWN,UNKNOWN,1,FACT (of absence),High,"NOT independent in the useful sense: this series republishes registrant filings as aggregates, so even a positive naming would have been evidence of registration rather than of the company",NO_VERBATIM_PASSAGE_RECORDED,"A5-03; an unlisted Arkansas retailer could not appear in the sample by construction (A5 page-level negative)"
S0141,stage1,"The company's curated dated timeline: the 1962 Rogers opening, the 1967 '24 stores / $12.7 million' datapoint, the 1969 incorporation, the 1970 '$16.50 per share' first stock, the 1971 'first distribution center and Home Office', the 1972 NYSE listing with '51 stores ... $78 million'; and the documented ABSENCE of everything before July 1962","Walmart History",Corporate Affairs (Wal-Mart Stores Inc. / Walmart Inc.),company self-narrative web page,secondary,1962-07-02/1972,undated page retrieved 2026-09-23,2026-09-23,https://corporate.walmart.com/about/history,sources/EXTRACT_corporate_walmart_history_timeline.md,1,RETROSPECTIVE INTERPRETATION,Medium,"ONE lineage with the annual reports for every number it repeats, and NO independent basis for any of them; the page carries zero primary citations, so it is evidence of what the company asserts, never of what happened. Its silence about pre-1962 is itself a finding (probe W-15)","On July 2, 1962, Sam Walton opens the first Walmart store in Rogers, Arkansas.","cited by part 1 (trap row, §B.0, §B.2) and by §E.4/§H.5/§I.4 of this volume; the FY1967/FY1968 one-year labelling shift is recorded at part 1 §A.1"
S0142,stage1,"The only 1962 artifact catalogued in this evidence set ('First Walmart Advertisement', asset year 1962, slogan 'Wal-Mart Lowers Living Cost'), plus the 1992-anniversary item carrying the company's first-computer claim (IBM System/360 Model 20, 1968/69) and the 1977 supplier-ordering-system claim","Walmart Museum",Walmart Museum (Bentonville),company museum catalogue web page,secondary,1962,2026-04-24 (page dc:modifyDate),2026-09-24,https://corporate.walmart.com/about/walmart-museum,sources/periodicals/walmart_museum_page.html,1,FACT (existence of the catalogue entry) / RETROSPECTIVE INTERPRETATION (its prose),Low,"TIER SPLIT ON ONE DOCUMENT: the catalogued artifact is Tier 1 as an artifact, the curation text describing it is Tier 3, and the 1968-77 computing narrative printed on it is uncited, 2026-dated and has NO in-window witness anywhere in this corpus (A2 W-77)","In the bottom right corner, a stack of quarters proudly proclaims: 'Wal-Mart Lowers Living Cost.'","cited by §E.2 (the only surviving 1962 wording) and §J.2 (the retrospective computer claim); the 1950 bill of sale the museum claims to hold (probe W-21) is a lead whose bytes are NOT in this repository"
```

### `conflicts.csv` — 9 rows (2 opened by this volume; 7 already argued in the A2 dossier but never emitted as register rows)

```
company,stage,conflict_id,section,claim_a,claim_a_source,claim_a_date,claim_b,claim_b_source,claim_b_date,why_they_differ,evidence_weight,best_supported_interpretation,residual_uncertainty,confidence
Walmart,stage1,U-E/1,E; D; Q,"The first Wal-Mart Discount City opened in November 1962","Wal-Mart Stores Inc. annual reports FY1975 and FY1978 (company profile and founding narrative), S0104/S0107",1978-04-14,"The first Walmart store opened on July 2, 1962","corporate.walmart.com/about/history (extract), EXTRACT_corporate_walmart_history_timeline.md; A2 W-118",2026-09-23,"Different instruments and purposes: A is dated narrative inside four audited registrant documents; B is an undated marketing page carrying zero citations whose provenance chain this repository has never seen","four printings of A inside signed annual reports against one uncited page; both are the same registrant lineage, so the independent-origin count for either month is zero","1962 is attested; the MONTH is not. Where a month must appear the corporate-print month is used with U-E/1 cited beside it, and July 2 is never presented as documented","no 1962 newspaper item, lease, permit, register tape or photograph exists in this corpus; the 1962 grand-opening flyer lead (W-20) was never retrieved; Arkansas and Missouri newspaper archives and the Arkansas SoS file are UNTRIED","High (that the two company sources disagree); UNKNOWN (the opening date)"
Walmart,stage1,U-F/1,F,"Stores served communities with an average population of 10,000-15,000, within a 350 mile radius of Bentonville","Wal-Mart Stores Inc. FY1975 report, S0104",1975-03-28,"Stores are 'located primarily in towns having populations from 5,000 to 25,000'","Wal-Mart Stores Inc. FY1978 and FY1980 reports, S0107 and S0109",1980-04-01,"An average is not a bound, and 'communities served' is not 'towns where stores are located'; the two sentences describe different quantities, printed three and five years apart","both contemporaneous to their own fiscal year and both as-filed; neither is corroborated by any outside source","both statements are kept and neither supersedes the other; the FY1975 band may describe the settled fleet while the later band describes the whole site policy","no document in the corpus pairs any store with its town's population, so which rule governed which openings is unknowable from this evidence","High (both printed); UNKNOWN (which rule governed site selection)"
Walmart,stage1,U-A2/2,K; boundary; A,"The 1970 public offering was 200,000 shares sold 8 October 1970 for net proceeds of $3,030,467 ($3,010,467 over par)","Wal-Mart Stores Inc. FY1972 report, capital note and statement of changes in financial position, S0101",1972-03-22,"The first stock was sold at $16.50 per share","corporate.walmart.com/about/history (extract), W-12/W-118",2026-09-23,"A states net proceeds and share count but no gross price; B states a price but no date, count, proceeds, underwriter or citation","A is auditor-attested registrant print; B is uncited company self-narrative. Both are one lineage","the offering is dated and sized at Tier 1; the gross offer price is not evidenced. Implied NET per share $15.15 is DERIVED and is not reconciled with $16.50","no 1970 registration statement, prospectus or underwriting agreement is on disk; the $16.50 and $15.15 pair has no licensed bridge","High (the note's contents); UNKNOWN (gross price)"
Walmart,stage1,U-A2/3,G; Q,"A distribution centre of 60,000 sq ft was doubled to 124,800 sq ft, the addition completed 15 August 1971","Wal-Mart Stores Inc. FY1972 report, President's message, S0101",1972-03-22,"The first distribution centre opened in 1970 (PBS) / 1971 (company page) / 1970 location unspecified (SCDigest) / a leased Springfield Missouri warehouse (lore)","EXTRACT_corporate_walmart_history_timeline.md; EXTRACT_pbs_2004_timeline.md; EXTRACT_scdigest_2012_timeline.md",2004-08-20,"Four retrospective accounts, none citing a lease or a filing; the registrant print describes an EXPANSION of a facility that already existed, which none of the four narratives does","the registrant sentence is contemporaneous and inside an audited document; all four alternatives are retrospective and uncited","a distribution facility stood before 1971-08-15 and was enlarged then; the 'first DC' year and town in the secondary accounts are not evidence","no lease, deed or DC-opening document exists in this corpus; Benton County and Greene County (MO) records are UNTRIED","High (the 1971 enlargement); Low (any 'first DC' date)"
Walmart,stage1,U-A2/4,K,"The April 1972 offering added approximately $9,250,000 of equity capital and placed stock with over 3,400 holders","Wal-Mart Stores Inc. FY1973 report, President's letter, S0102",1973-03,"Paid-in capital rose $8,913,504 on the sale of 400,000 shares at $23.75 before expenses, i.e. $9,500,000 gross","Wal-Mart Stores Inc. FY1973 report Note 4, S0102",1973-03,"three totals coexist in one document (gross arithmetic, letter rounding, amount posted to paid-in) and the bridge between them is not disclosed","all three are the same document and the same lineage; none is independent of the others","no single figure is 'the raise'; register rows must carry the basis label of whichever figure they print","underwriting expense, over-allotment and option/warrant proceeds are not separately disclosed for the month of April 1972","High (that the three figures coexist); Medium (any total used alone)"
Walmart,stage1,U-A2/5,G,"The General Office and Distribution Center at Bentonville was increased during 1972 to 261,800 sq ft all under one roof","Wal-Mart Stores Inc. FY1973 report, S0102",1973-03,"the same building is printed at 263,800 sq ft with an open house dated 3 December 1972","Wal-Mart Stores Inc. FY1976 report, growth note, S0105",1976-03-26,"two registrant prints of the same facility two fiscal years apart, 2,000 sq ft apart","each is contemporaneous to its own report; the later print is retrospective about the earlier year","both prints are carried in §G.3 rather than averaged; no document reconciles them","the square footage may measure different envelopes (office included/excluded); the documents do not say","Medium (the discrepancy is real and small); UNKNOWN (its cause)"
Walmart,stage1,U-A2/6,B; E; L,"The Walton brothers assembled a group of fifteen Ben Franklin variety stores between 1945/1946 and 1962","Wal-Mart Stores Inc. FY1975, FY1978, FY1979 and FY1980 reports, S0104/S0107/S0108/S0109",1980-04-01,"fourteen Ben Franklin variety stores were still trading at 1 January 1970 and nine 'variety and family center stores' existed in FY1973","Wal-Mart Stores Inc. FY1980 report and FY1973 report, S0109 and S0102",1980-04-01,"a cumulative assembly total against period-end trading counts, plus a label drift from 'Ben Franklin stores' to 'variety stores' and a one-year disagreement on the start of the count (1945 vs 1946)","all prints are the same registrant lineage; the trading counts are arithmetically consistent with run-down of an assembled group, which is an internal check not a second source","both are kept: fifteen assembled and fourteen/nine trading at those dates are compatible only if closures are admitted, and the FY1974 report does print two sold and four closed","no document lists which stores, where, when acquired, or how many entered the 1970-02-01 pooling; no partnership deed exists in this corpus","Low (the count); High (that each report says it)"
Walmart,stage1,U-A2/7,B; D,"The 1945 Ben Franklin franchised start was in Newport, Arkansas","Wal-Mart Stores Inc. FY1975-FY1980 reports, five documents, S0104-S0109",1980-04-01,"Newport is in Nebraska (an internal 2026-09-23 project 'correction' against vintagebentonville) / Newport, Kentucky (A4 dossier prose)","A_chronology_feasibility.md W-19 and its own supersession note; A4_independent_periodicals.md A4-16/A4-18/A4-23",2026-09-24,"the registrant placed it in Arkansas from 1975 onward; the project's own correction asserted Nebraska and A4's prose asserted Kentucky - two wrong states introduced after the fact, neither sourced","five registrant documents naming Newport, Arkansas, plus FY1973/FY1976 store lists placing Newport among Arkansas towns; the rival readings have no document at all","Newport, ARKANSAS is the only reading any document in this corpus supports; the 'correction' is itself the refuted error and 1945-50 Newport sits in Mississippi County, Arkansas","the 1945 event itself remains independently undocumented; the state is settled by the print, the year is not","High (Arkansas); Low (that any 1945 event is documented)"
Walmart,stage1,U-K/1,L; P,"FY1976 total expense ratio was 20.5% of sales","Wal-Mart Stores Inc. FY1976 report, shareholder letter, S0105",1976-03-26,"FY1976 total expense ratio was 20.0% of sales","Wal-Mart Stores Inc. FY1976 report, Management's Analysis, S0105",1976-03-26,"two stated ratios for the same fiscal year inside the same document; the derived value from the summary rows is 20.01%, which supports the analysis figure","both are the company's own; the arithmetic of the same table's rows breaks the tie in favour of 20.0%, but the letter is the more widely quoted number","print both; §L uses the DERIVED 20.01% and states the pair rather than choosing","the letter's 20.5% may be a different expense definition (e.g. including interest) - no document states it","Medium (that the pair disagrees); High (the derived ratio)"
```

### `quantitative.csv` — 18 rows (§G penetration and lease estate; §E specification; §K capital events; §L derived validations)

```
company,stage,date,metric,value,unit,source,source_date,evidence_class,confidence,derived_arithmetic,notes
Walmart,stage1,FY1973,Distribution centre shipments at cost,42786831,USD,S0102,1973-03-22,FACT,High,,"CONTEMPORANEOUS: FY1973 report; stated 'largely by our Wal-Mart truck fleet'; a cost-basis figure against a sales-basis top line, so no share-of-goods ratio is computed from it"
Walmart,stage1,FY1974,Share of merchandise shipped through company distribution,55,percent-of-merchandise,S0104,1975-03-28,FACT,Medium,,"printed as the PRIOR YEAR inside the FY1975 report: a restated prior-year value, not a contemporaneous FY1974 statement"
Walmart,stage1,FY1975,Share of merchandise shipped through company distribution,60,percent-of-merchandise,S0104,1975-03-28,FACT,High,,"CONTEMPORANEOUS: 'approximately 60 percent ... as compared to 55 percent in the previous year'"
Walmart,stage1,FY1976,Share of store purchases shipped from the Bentonville warehouse and DC,80,percent-of-purchases,S0105,1976-03-26,FACT,High,,"CONTEMPORANEOUS, and the sentence names the residual channel: 'The balance was shipped directly to the stores from suppliers'. Earliest quantified penetration measurement in the corpus"
Walmart,stage1,1972-01-31,Future-store leases in hand,6,leases,S0101,1972-03-22,FACT,High,,"aggregate minimum annual rentals $285,238; inventory, fixtures and working capital for the six estimated at $3,370,000; the earliest dated evidence of contracting the estate ahead of opening"
Walmart,stage1,1973-01-31,Future-store leases in hand,8,leases,S0102,1973-03-22,FACT,High,,"$233,247 aggregate minimum annual rentals; estimated $4,300,000 of inventory, fixtures and working capital still to come"
Walmart,stage1,1976-01-31,Future-store leases in hand,24,leases,S0105,1976-03-26,FACT,High,,"$2,029,000 aggregate minimum annual rentals"
Walmart,stage1,1980-01-31,Future-store leases in hand,38,leases,S0109,1980-04-01,FACT,High,,"including 15 under sale-and-leaseback arrangements; 20- to 25-year minimum terms approximating $5,800,000 a year"
Walmart,stage1,1976-01-31,Total lease commitments (operating and capital / pre-SFAS-13 presentation),106501000,USD,S0105,1976-03-26,FACT,High,,"against recorded long-term debt of $17,531,000 in the same year; FY1976 also disclosed $38,416,000 of noncapitalised financing leases of stores whose capitalisation would have cut FY1976 net income by about $515,000"
Walmart,stage1,1970-02-01,Bank note assumed at the pooling of interests,968876,USD,S0101,1972-03-22,FACT,High,,"liability assumed by the registrant group from Walton Enterprises, Inc. at the exchange effective 1970-02-01"
Walmart,stage1,1970-10-08,Net proceeds of the 200,000-share public offering,3030467,USD,S0101,1972-03-22,FACT,High,,"printed component: excess of net proceeds over par value $3,010,467; par $20,000 at $.10 x 200,000. GROSS OFFER PRICE UNKNOWN"
Walmart,stage1,1970-10-08,Net proceeds per share sold,15.15,USD-per-share,S0101,1972-03-22,ESTIMATE,Medium,3010467 + 20000 = 3030467; 3030467 / 200000 = 15.15,DERIVED from the FY1972 capital note only; NOT reconciled with the $16.50 on the company page and no local document licenses a bridge (U-A2/2)
Walmart,stage1,1972-04,Public offering shares placed,400000,shares,S0102,1973-03-22,FACT,High,,"$23.75 per share before expenses; paid-in capital rose $8,913,504; placed with over 3,400 holders, which the company states made it eligible for NYSE listing; three coexisting totals (U-A2/4)"
Walmart,stage1,1975-05,Convertible subordinated debentures issued,15000000,USD,S0105,1976-03-26,FACT,High,,"the single external issue that replaced bank borrowing for new-store inventory and fixtures 'until May, 1975'; $630,000 converted during FY1976"
Walmart,stage1,FY1978,New-store volume as a share of comparable-store volume,77,percent,S0107,1978-04-14,ESTIMATE,Medium,"153 x (478807000/153) x 1.17 = 560204190; 678456000 - 560204190 = 118251810; 118251810/42 = 2815519 vs 3661466 per comparable store; 2815519/3661466 = 77%",DERIVED from the two company-stated FY1978 figures; 42 is a NET store count (30 openings, 10 expansions/relocations, 16 acquired, 4 closures); mechanism UNKNOWN and offered by no document
Walmart,stage1,FY1979,Merchandise mix softline / hardline,30 / 70,percent-of-sales,S0108,1979-04-06,FACT,Low,,"management's own characterisation; NO document prints a softline or hardline dollar row, so the basis is unstated and the split is not auditable"
Walmart,stage1,FY1979,Departments per store,36,departments,S0108,1979-04-06,FACT,High,,"'Each store features 36 departments'; FY1980 restates it as '36 full-line departments' alongside 'over 35,000 items', whose unit basis (SKU/style/vendor pack) is never defined"
Walmart,stage1,FY1980,Fourth-quarter share of fiscal-year sales,33,percent,S0109,1980-04-01,DERIVED,High,"417175 / 1248176 = 33.4%","from the FY1980 quarterly series 238569 / 291685 / 300747 / 417175 thousand; NO earlier quarterly series is printed in any report, so demand shape FY1962-FY1979 stays UNKNOWN"
```

### `timeline.csv` — 9 rows

```
company,stage,date_or_range,event,actors,location,source_id,evidence_class,confidence,conflict_ref,notes
Walmart,stage1,1962-07,"Claimed opening date on the company's own curated page: 'On July 2, 1962, Sam Walton opens the first Walmart store in Rogers, Arkansas'","Sam M. Walton","Rogers, AR",S0141,RETROSPECTIVE INTERPRETATION,Low,U-E/1,"uncited company self-narrative, retrieved 2026-09-23; carried in the register so the July date is never mistaken for the audited-print date, and the 1962-11 registrant row remains the documented one"
Walmart,stage1,1970-02-01,"Exchange of common stock accounted for as a pooling of interests: Walton Enterprises, Inc. transfers shares in the various subsidiaries plus assets of related businesses, subject to an assumed $968,876 bank note; the registrant group's consolidated life begins","Wal-Mart Stores Inc.; Walton Enterprises Inc.","Bentonville, AR",S0101,FACT,High,none,"Note 1; the FY1968-FY1971 rows the company itself labels pro forma sit OUTSIDE this date and outside every audit opinion on disk"
Walmart,stage1,1970-10-08,"200,000 shares sold in the public offering that closes Stage 1","Wal-Mart Stores Inc.; underwriters not named for this event in any document on disk","Bentonville, AR",S0101,FACT,Medium,U-A2/2,"day precision comes from inside the audited FY1972 capital note, a 1972 document reporting a 1970 event; no 1970 registration statement is on disk (EDGAR floor 1994-02-14)"
Walmart,stage1,1971-06-11,"Two-for-one stock split: 1,500,000 shares issued with a $150,000 par charge","Wal-Mart Stores Inc.","Bentonville, AR",S0101,FACT,High,none,"first of THREE two-for-one splits printed in this corpus (with 1972-04-05 and 1975-08-19); corrects the register's earlier single-split framing (part 1 §D note D-R09c)"
Walmart,stage1,1972-04-05,"Two-for-one stock split: 3,000,000 shares to be issued with a $300,000 par charge","Wal-Mart Stores Inc.","Bentonville, AR",S0101,FACT,High,none,"both 1971 and 1972 splits are evidenced inside the FY1972 report's own capital note, which is also where the $.10 par value is established"
Walmart,stage1,1975-08-19,"Two-for-one stock split increasing common stock outstanding by 6,687,789 shares","Wal-Mart Stores Inc.","Bentonville, AR",S0105,FACT,High,U-A3/7,"the only split falling inside the restatement dispute; 6,687,789 x $.10 par = $668,779 matches the $669,000 charged to capital in excess"
Walmart,stage1,1976-01,"The last dated trace of the Ben Franklin variety banner: a Ben Franklin variety store at Rogers, Arkansas was closed","Wal-Mart Stores Inc.","Rogers, AR",S0105,FACT,Medium,U-A2/6,"the report does NOT state that this unit shared premises with the 1962 Discount City; the absence of that statement is recorded, not inferred"
Walmart,stage1,1978-10-01,"Hutcheson Wholesale Shoe Company, previously a licensee, was acquired","Wal-Mart Stores Inc.; Hutcheson Wholesale Shoe Co.",UNKNOWN (not stated in the report),S0109,FACT,High,none,"backward integration of a leased department; FY1980 then carries the plan to acquire 159 licensed jewelry units presently operated by Cohen-Hatfield"
Walmart,stage1,1966-01-29,"Business Week cover story on S. S. Kresge mixing upgrading, discounting and experimenting","S. S. Kresge Co.","Detroit, MI",S0118,CONTEMPORARY OBSERVATION,High,U-A4/2,"index-level only: page contested p.26 / p.126 and the article text is unreachable, so the entry is cited by headline, issue date and cover status"
```

**Two notes for the register owner.** (1) **Append order matters:** the four `sources.csv` rows must land
before the `timeline.csv` rows are merged, because those rows carry `source_id` values (`S0139`, `S0141`)
that do not yet resolve in `sources.csv`, which currently ends at `S0138`. (2) The seven `U-A2/*`
conflicts merged from the `conflicts.csv` block **already exist as argued prose in
`research/A2_chronology_finance.md` §Contradictions and were never emitted as register rows**; `U-A2/1`,
`U-A2/9` and `U-A2/10` are not requested here because §§E–§L do not rely on them.


# s1_p3.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T19:36:02Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

# s1_p3.md — Volume 3, sections §M–§U, the §U canonical anchor set, and the part-3 register rows

*One document split for the §9.2 cap. **§M–§U and the §§M–§U claim records live here.** Numbering runs
continuously from `s1_p1.md` (§Header, boundary, §A–§D) and `s1_p2.md` (§E–§L); nothing in this volume is
renumbered to make a part look self-contained (§9.3).*

**Geometry drift, declared not repaired.** `s1_p1.md`'s header says "§E–§P in `s1_p2.md`", and part 1's
prose forwards several of its own items to "§S (part_2)" and "§U (part_2)". The dispatch this volume was
written under assigns **§E–§L to part 2 and §M–§U to part 3**; part 2 states the same resolution at its own
head and does not obey the part-1 header either. **Every part-1 forward reference to "§S (part_2)" or
"§U (part_2)" therefore resolves HERE, in part 3**, and is collected by anchor in §U.0. Nothing part 1
promised was dropped: §A.2 items 1–6, §B.0, §B.1, §B.2, §C.0 (U-C0/1), §C.1, §D.1, §D.3 and §D.4's six
UNTRIED queries all land in §S, §T, §U and the final section of this volume.

**Confidence scale, classes, and the two firewalls are inherited verbatim from part 1's header block**
(method §2, §3, §5, §6). Standing constraints re-stated because this volume owns the registers they bite on:
**pre-1994 here is digitised print, not EDGAR**; every financial row states **as-filed (CONTEMP)** or
**RESTATED (RESTAT)**; **one printed annual report plus its own later reprints is ONE lineage** (so the
independent-origin count for every company figure in Stage 1 is **1**, A3 §7.2(c), unchanged by A5);
"**not establishable in the Stage-1 record**" is written where a claim cannot be carried, never "never
happened"; and a 403/429/500/504 or an unattempted retrieval is **UNANSWERED or UNTRIED, never a null**.

---

## M. NEGATIVE SIGNALS AND FAILURES

STATUS: WRITTEN 2026-09-26

### M.0 Why the standard frame is adapted here, and what the adaptation costs

Method §7 allows a section to be answered by its model-appropriate equivalent but never by deletion. For a
retail chain the equivalents are store closures, format write-offs, same-store declines, lease exposure and
margin compression (spec §19). **Inside Stage 1's window (1945 → 1970-10-08) the corpus supplies almost none
of them, and the reason is evidentiary rather than favourable: the register's negative evidence begins where
the archive begins.** The nine printed Wal-Mart Stores, Inc. annual reports run FY1972→FY1980
(`sources/periodicals/WALMART_AR_1972.txt` … `_1980.txt`; S0101–S0109), and **no document of any kind in
this corpus names the company before 1972-03-22** (part 1 §A.2; U.101). A year-with-a-failure column for
FY1945–FY1967 cannot be written, because FY1962–FY1967 is **EMPTY of every financial and physical variable**
(A3-039; U.102). This section therefore does three things instead: it registers **every dated negative signal
the record actually carries**, it marks each one **in-window or out-of-window** against the 1970-10-08
boundary, and it states the **in-window silence as a finding about the record**, not as a claim about the
firm. The anti-hagiography test (§2) is applied to each row: none asserts that a failure was overcome,
because none has an outcome column inside the window.

### M.1 Failure and negative-signal register (rows keyed to `failures.csv`, which does not yet exist for this company — see §U.0 note R-3)

Format per §13's `failures.csv` fields: `Date | Signal or failure | Magnitude | What it demonstrated | What
it did NOT demonstrate | Source | Class | Confidence | Anchor`.

| Date | Signal / failure | Magnitude | What it demonstrated | What it did NOT demonstrate | Source (path + label) | Class | Conf | Anchor |
|---|---|---|---|---|---|---|---|---|
| **in-window** — FY1969 and FY1970 tax years; disclosed 1972-03-22, extended 1973-03-20 | **IRS proposed additional assessments** on surtax exemptions and inter-subsidiary reallocation for the years ended 1969-01-31 and 1970-01-31 | Amount: **not stated in either document**; the disclosure is qualitative | The group's **pre-pooling multi-entity structure was itself under challenge**: the tax authority disputed how the separate corporations had allocated income among themselves | That the assessment was sustained, or material, or about the retail business rather than the holding form | `WALMART_AR_1972.txt` Note 6 (S0101); `WALMART_AR_1973.txt` Note 6 (S0102); A2 W-06, W-40 | FACT (that the assessment was proposed and extended) | High | U.108 |
| **in-window** — 1970-02-01 | The pooled group came in **indebted at birth**: an assumed **bank note of $968,876** transferred with the "various subsidiaries" | $968,876 against FY1970 total assets **$8,493 thousand** = **11.4%** — DERIVED: 968,876 ÷ 8,493,000 = 0.1141 | The registrant's opening consolidated position was levered against a small asset base, and the leverage was **inherited, not raised** | Any judgement about whether 11.4% was high for a 1970 regional retailer — **no peer asset/debt figure exists in this corpus** (U.113) | `WALMART_AR_1972.txt` Note 1 (S0101, W-04); FY1970 total assets RESTAT in `WALMART_AR_1978.txt` nine-year table (S0107, A3 Table S4) | FACT + DERIVED | High (rows); Medium (ratio) | — |
| **in-window** — FY1971 | A **stockholder receivable was cleared** during the fiscal year (part of the same capital note) | printed in the FY1972 capital breakdown | Related-party balances sat inside the capital account up to the year of the float | Who owed what, and when the balance arose — the document does not say | `WALMART_AR_1972.txt` capital note (S0101) | FACT | High | — |
| **in-window** — 1970-01-01 | **The conversion was incomplete at the boundary: the fleet was still 14 Ben Franklin variety stores out of 32 units** (18 Discount Cities + 14 variety) | 43.8% of units under the franchised banner — DERIVED: 14 ÷ 32 = 0.4375 | At the moment the company sold stock to the public, **nearly half its stores carried another firm's banner and buying arrangement**; the discount format was 8 years old and not yet the whole business | That the variety units were failing (no per-banner sales, margin or count is printed for any year) — and it does **not** show the format choice was vindicated by the following decade, which is Stage 2's record not this one | `WALMART_AR_1980.txt` "Wal-Mart's Past — Foundation for the Future" (S0109); the 18-store figure inside `WALMART_AR_1972.txt` President's message (S0101) | FACT (as company state, one lineage) | Medium-High | U.029 |
| **in-window** — FY1970→FY1972 (comparatives printed 1972-03-22) | **Liquidity fell while the chain grew**: current ratio 1.87 → 1.65 across the two columns the FY1972 report prints; long-term debt appears at 809 → 4,659 (thousands) between FY1971 and FY1972 | printed rows (A3 Table S4) | The FY1972 report itself carries the shape of a company funding growth with debt and working capital in the same two years it sold 200,000 shares | Causality — the report does not link the offer to the ratio, and no use-of-proceeds statement is on disk (U.210) | `WALMART_AR_1972.txt` FINANCIAL HIGHLIGHTS + A3 Table S4 (S0101) | FACT (rows); INFERENCE (the pairing) | High (rows); Medium (reading) | — |
| **in-window** — the company's own label, FY1968–FY1972 | **Four of the five pre-float years are captioned "Pro forma net income" by the registrant**, i.e. the group it reports earnings for did not exist in those years | $.09 / $.12 / $.23 / $.30 / $.47 per share, FY1968→FY1972 | The **earliest financial series in the corpus is a self-declared construction**: it begins only at the 1970-02-01 pooling and is arithmetic backwards for FY1968–FY1969 | That the underlying stores did not trade — pro forma is a statement about the **reporting entity**, not about activity. **No opinion of any kind attaches to FY1968–FY1971** (A3 §6.1) | `WALMART_AR_1972.txt` five-year table (S0101); A3-020 | FACT (of labelling) | High | U.102 |
| **in-window, structural** | **No failure of any kind is dated inside 1945–1962 in any document.** No lost lease, rejected site, closed unit, failed venture, price war or write-off appears in the corporate print for those years | zero rows | Nothing about the firm. It measures the record: the corporate print's entire pre-1962 economic content is one office sentence (1955) and one move (1957) | That nothing went wrong — the county, newspaper and franchisor routes that would carry such a record are **UNTRIED or UNANSWERED** (U.206, U.211, U.212) | part 1 §A.2 items 4–6; A2 §Pre-1962 evidence ledger; nine-file negative search | **EMPTY within a stated perimeter** | High (that the print is silent) | U.101, U.110 |
| **out-of-window, control set** — FY1974 | Two Ben Franklin variety stores **sold**, four **closed** | 6 units | The registrant **was capable of printing a contraction** in its report prose as it happened | Anything about FY1945–FY1970 — except by this negative: the silence inside the window is **not** a genre that never reports losses | `WALMART_AR_1974.txt` (S0103) | FACT | High | — |
| **out-of-window, control set** — FY1975 → FY1979 | The **second format failed on the company's own accounting**: two Sav-Co Home Improvement Centers opened FY1975 (54,000 sq ft) under the stated gate "will not be expanded until [they are] operating at our expected profitability level"; the **remaining Sav-Co was closed in FY1979** | 2 units in, 1 closure ending a 9-year experiment | A printed stop-rule and a printed write-off, in the same banner. **This is what an in-window failure would have looked like in this archive if the archive began earlier** | Any transfer of this pattern backwards to 1945–1970 (that would be hindsight: the genre is documented as capable, nothing more) | `WALMART_AR_1975.txt` (S0104); `WALMART_AR_1979.txt` (S0108); `timeline.csv` 1979 row | FACT | High | — |
| **out-of-window, control set** — FY1973 | **Three stores lost or damaged by fire/tornado** in one fiscal year; and the FY1973 store count reconciles only if **≥5 units left the base unlisted** (51 + 16 new + 2 relocated ≠ 64) | 3 casualty events; ≥5 unexplained exits | Even in its own best-dated year the company's store arithmetic does not close — the register's counts are **net**, its narratives **gross** | Which units, where, or under which banner — "UNKNOWN on the exits" (U-A2/10 → U.030) | `WALMART_AR_1973.txt` (S0102); A2 W-34 | FACT + INFERENCE | High (arithmetic); UNKNOWN (exits) | U.030 |
| **out-of-window, accounting** — 1975-01-31 | **LIFO adoption** reduced FY1975 net income by **$2,347,000 ($.36 pre-split / $.18 post-split)** and the auditor flagged it **in the opinion, by exception** | $2,347,000 | A company-acknowledged, auditor-flagged break in the cost-of-sales/margin series at exactly the year the register would need for a clean FY1974→FY1976 comparison | That LIFO signalled deterioration — it signalled inflation, and the direction of the effect is arithmetic not judgement | `WALMART_AR_1975.txt` opinion + S0104 quoted passage (S0104); A3 §6.1 | FACT | High | — |
| **out-of-window, register hygiene** — FY1980 table | The FY1980 ten-year summary's **dividend row is refuted for 1976–1979** by each year's own report ($.09/$.11/$.19/$.25 printed against $.065/$.085/$.16/$.22), and no split factor reconciles them ($.09 ÷ $.065 = 1.38 is not a split) | 4 of 4 cells | A late retrospective table can be **wrong against its own earlier prints**, and the later print is the one that got into secondary lore | That the company underpaid or overpaid anything — the contemporaneous rows govern | `WALMART_AR_1980.txt` ten-year table vs `WALMART_AR_1976/77/78/1979.txt`; A3 COR-A3-04 | FACT (of refutation) | High | U.026 |
| **research-side, this stage** | **Every "small town greets the discounters"-style story the corpus reaches belongs to somebody else** — five documented decoy families (Aldens/Gamble-Skogmo 1964; Hennepin Illinois steel town 1967; three "Walton" person entries 1968; Newport, Kentucky municipal item 1962; Arkansas-as-river-infrastructure 1967) | 5 families, ~12 index entries | The **most probable false positive in this dossier is a headline that reads like Wal-Mart's own positioning** and is a competitor's or a person's | That the company was or was not covered elsewhere — the reachable corpus is silent, the unreachable is UNTRIED (U.202, U.207, U.213) | S0112, S0114, S0115, S0119, S0120, S0121; A4-17…A4-22; `timeline.csv` 1964-10-03 row | FACT | High | U.042 |

**Reading rule for the table.** Seven rows are inside the window, four are out-of-window controls recorded
*because* the window cannot supply them, and two are register-hygiene rows. **The register is not thin
because this company did not fail; it is thin because no one was writing before 1972-03-22.**

### M.2 The one contemporaneous negative that exists at the moment of entry — and its firewall

The single dated negative in the corpus that is **independent of the registrant** sits in the founding year
and is about the industry, not the firm: Business Week's 1962 index carries "Discount store dropouts" p.101
(Oct.6 1962), "Shake-out among discounters seen as chain files in bankruptcy" p.83 (Oct.27 1962),
"Discounter caught in cash bind: Grayson-Robinson's plight may presage a discount house shakeout" p.109
(Aug.18 1962, page contested p.169 — U.035), and "Discounters strive to ride out storm: fast-growing
$6-billion industry is facing a major shakeout" p.78 (Dec.1 1962) — all in
`sources/periodicals/BUSINESSWEEK_INDEX_1962-1971_EXTRACT_walmart_and_sector_hits.txt` (S0112; A4-01…A4-05).
**Class: CONTEMPORARY OBSERVATION, Tier 2, index-level only — no article text is reachable, so no content of
any of these items is asserted anywhere in this volume** (§6 date/precision discipline).

**Firewall (§2), stated as a prohibition.** This material is admissible as *market state* for §H (part 2) and
as the counterfactual context for §O. It is **NOT** admissible as (i) evidence that the founder knew the
sector was consolidating, (ii) evidence that the Rogers format was a response to anything, or (iii) evidence
that surviving the shake-out validated the 1962 decision. U-A4/3 (→ **U.037**) keeps the registrant's
untroubled retrospective founding narrative and this distress coverage side by side **without a bridge**, and
the `independence_note` is that the two are of different kinds: one is a third party's real-time industry
diagnosis, the other is the company's own later account of its own intent.

### M.3 Negative signals about the record itself, which are the stage's actual failures

1. **Zero independent lineages for every company number** (A3 §7.2(c); unchanged by A5's two whole-document
   reads). Confidence **High**; this is measured, not asserted.
2. **The one genuinely independent document in Stage 1 is a negative** — the SEC's complete 31 December 1970
   register of exchange-traded issuers prints WALGREEN … WALWORTH and **zero** occurrences of the name in
   153,481 words (`sources/gov_docs/SEC_SecuritiesTradedOnExchanges_asof-1970-12-31_…txt`; A5-04; the row is
   pending in the register as `S0139`). It corroborates *over-the-counter status* and **no figure**.
3. **The register's own supersession load**: A2's 133 records carry **39 SUPERSEDED sites**, and every
   supersession note wins over the row it supersedes (§U.0 mapping; part 1 §D.0's four correction notes are
   the in-volume application).
4. **Two internal project errors became evidence hazards**: the "Newport is in Nebraska" *correction* (which
   was the error, and whose D1 fleet brief pointed agents at the wrong state's newspapers) and A4's repeated
   "Newport, **Kentucky**" dossier prose. Both are U-A2/7 → **U.011**.
5. **A live `source_id` collision is in flight between two volumes of this same part-set** — see **U.048**
   and §T.3. It is a defect of *this* reconstruction, and it is registered rather than quietly harmonised.

### M.4 Coda (§7/§16 interpretive duty) and knowability

The honest negative finding of Stage 1 is **double**: the company's failures before 1970 are unrecoverable
because the archive is a post-float artifact, **and** the one place where the archive is deep is exactly where
a later reader expects the story to be, which is why the FY1972–FY1980 density must not be read backwards as
legibility. Mechanism for the in-window silence: **UNKNOWN** — the corpus cannot distinguish "nothing was
written" from "something was written and is not in this repository", because the routes that would
discriminate (U.202, U.206, U.207, U.211, U.212, U.213) are UNTRIED or UNANSWERED. Alternative explanation
retained, and not dismissible: local Arkansas print 1945–1962 may carry closures, leases and franchise
notices naming Walton's, in which case §M's shape changes and §S's gap list shrinks; **that is a fetch, not an
inference** (`ca_01_waltons_five.json`, `ia_arkgaz.json` are on disk and unmined — U.202, in flight with the
mining agent).

| Kind | Item |
|---|---|
| **KNOWABLE in-period** | That the discount sector was consolidating by failure during 1962 (a dated third-party index a reader could have held); the company's own as-filed sales, store count and capital structure from FY1968 forward (pro forma FY1968–FY1971, audited FY1972+); that 14 of 32 units still carried the Ben Franklin banner at the boundary |
| **NOT KNOWABLE in-period** | Whether the 1962 format would scale; the sector's true universe behind "$6-billion"; any per-banner economics; whether the IRS proposals would be sustained; the terms of the 1945 franchise |
| **UNKNOWN (and the gap is named)** | Every FY1962–FY1967 variable (U.102); every in-window failure (U.101, U.110); the FY1973 exits (U.030); the outcome of the IRS proposals (U.108); the contents of all four 1962–1971 Business Week items (index-only); the 1962 opening's observable facts (U.110) |

---

## N. FOUNDER DECISIONS

STATUS: WRITTEN 2026-09-26

### N.0 What this table is allowed to rest on

Line format per §7: `| Date | Decision | State before | Information available | Unknowns | Alternatives |
Constraints | Rationale | Expected result | Actual result | Evidence | Confidence |`. **Three structural
limits govern every row.** (i) **No document in this corpus records the founder choosing anything before
March 1972** — part 1 §B.1's finding, and §N is where it costs the most, because a decisions table is
normally built from stated intent. Rows below are therefore reconstructed from **observable states** (fleet
composition, premises, capital events) and each row prints the absence of rationale rather than filling it.
(ii) `decisions.csv` **does not exist** for this company (the register set on disk is four files: `timeline`,
`quantitative`, `sources`, `conflicts`); §N.1 is drafted in its column order so the merge can create the
file without re-deriving the content, and the request is logged at §U.0 note R-3. (iii) **`actual_result` may
reference post-stage outcomes only when labelled RETROSPECTIVE**, and where the outcome is simply outside
this stage's evidence the cell reads **UNKNOWN AT THIS BOUNDARY**.

### N.1 Decision rows

| Date | Decision | State before | Information available | Unknowns | Alternatives | Constraints | Rationale | Expected result | Actual result | Evidence | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **1945 (claimed)** | Take a **Ben Franklin franchised variety store at Newport, Arkansas** as the post-war working arrangement | UNKNOWN — nothing in the corpus states the founder's position, capital or employment before this claim, and no legal person is identified for 1945–1950 | Only what the registrant later wrote: FY1973's "twenty-eight year history" back-cast, then FY1975/77/78/79/80 restatements; the trade body's franchise form was the ordinary route for a small-town dry-goods operator (S0133 shows NRMA's own membership covered "over 11,500 retail establishments") | Whether a franchise agreement, lease or partnership instrument exists; which person contracted; the terms, the wholesale arrangement, the capital source | The alternative actually on the trade's agenda in 1945 is **not documented as an option anyone considered** — that is a finding, and it is why this row's Alternatives cell cannot be filled | Post-war capital scarcity is **assumed by no document here**; nothing in the corpus states any constraint | **NOT STATED in any document** | UNKNOWN | UNKNOWN at this boundary; only the *telling* is dated (1973) | `WALMART_AR_1973.txt` (S0102) → `WALMART_AR_1980.txt` (S0109); part 1 §B.0, §B.2; A2 W-27/W-50/W-63; U.101, U.110 | **Low** (Class: FOUNDER CLAIM / RETROSPECTIVE INTERPRETATION, one lineage; independence: **0**) |
| **1946 (rival label)** | Enter the **brothers' partnership** | the 1945 claim | S0107: "brothers who had formed [a] partnership in 1946"; S0108 counts fifteen stores "between 1946 and 1962"; S0106 places Bud's Versailles, Missouri store in 1946 | Firm name, deed, partners, capital | staying sole; partnering later | UNKNOWN | **NOT STATED** | UNKNOWN | UNKNOWN | S0106, S0107, S0108; part 1 §C.0 RANK 5 | Low; the **1945-vs-1946 drift inside one lineage** is U.045 |
| **c. 1950 (memoir-only)** | Purchase / lose the **Bentonville store site** | UNKNOWN | **NO DOCUMENT.** "No document in this evidence set mentions 1950, Bentonville's 1950 store, a purchase price, a rent, or a lease" (part 1 §B.2) | Whether any 1950 transaction occurred; the museum's claimed 1950 **bill of sale has no bytes in this repository** | — | — | motive clause ("landlord wanted the site for his son-in-law") is **memoir-only, UNTRACEABLE**, and *Made in America* (1992) is **not admitted as evidence** (§3, part 1 §B.1) | UNKNOWN | UNKNOWN | A2 §"Where the boundary is NOT defensible"; probe W-21; U.110, U.211, U.214, U.219 | **UNKNOWN** — recorded as a live candidate for county-deed evidence that has never been fetched, **not as a refuted event** |
| **1955 / 1957** | Put the **first office above Walton's Family Store, Bentonville** (1955), then move it to a small building on Southeast A Street (1957) | a store-level operation with no stated central office | one 1976 sentence carrying both dates | what the "office" was, its staff, its function | staying in-store | UNKNOWN | **NOT STATED** | UNKNOWN | A later report prints that by November 1969 an office facility was completed (same 1976 sentence), so the office line is continuous to the boundary | `WALMART_AR_1976.txt` (S0105), A2 W-49 | Medium **as a 1976 assertion**; **no 1955 or 1957 document exists** |
| **1962** | Convert the operating model: **open a larger-format "Wal-Mart Discount City" at Rogers, Arkansas** | 15 (claimed) franchised variety stores assembled over 17 (claimed) years | The trade's own journal had, three months earlier, run NRMA's first Discount Seminar — "**The Discount Business — Is It for You?**", ~800 attendees, "about one half" conventional department stores — and printed a member ("Nichols Discount Cities since 1958") that had already made the same variety-to-discount move, plus a size-to-trading-area rule and a warning of "serious over-concentration of discount stores" (`STORES_NRDGA_1946-1972_EXTRACT_walton_and_discount.txt`, S0133, offsets 61,464 / 84,160 / 84,355 / 91,292) | Whether the founder attended, read or owned NRMA material — **UNKNOWN, and no inference is offered** | **Documented and live**: stay franchised (the base was profitable by the company's own word, "fifteen *successful* Ben Franklin stores"); convert as S. E. Nichols had; convert as Woolworth (Worth Marts, 1964) and Kresge (1970) later did at scale | The format's capital and buying terms are **undocumented** — no lease, plan or cost for the 1962 store exists on disk | **NOT STATED. No document in this corpus states the problem the 1962 format answered** (part 1 §C.1: "the single most consequential silence in Stage 1") | UNKNOWN — and **no contemporaneous measure of the experiment survives**: no opening-day takings, price, floor area or customer count (U.110) | 18 Discount Cities trading at 1970-01-01 beside 14 variety units (S0109) — the only in-window evidence that the format spread; **one lineage** | `WALMART_AR_1974.txt` (S0103, first document to date 1962), S0104, S0107, S0109; S0133; `timeline.csv` 1961-11/1961-12 rows; **U.001, U.011, U.041** | **Low** for the decision (retrospective, one attester writing 12 years later); **High** that the 1961 trade alternative is documented and contemporaneous |
| **1969-11** | Complete the **initial portion of the present Bentonville general-office facility** | the 1955/1957 office line | one FY1976 sentence | cost, size of that first portion, who decided | UNKNOWN | UNKNOWN | **NOT STATED** | UNKNOWN | by 1972-12-03 the enlarged GO+DC is printed at **261,800 sq ft** (FY1973) / **263,800 sq ft** (FY1976) — two registrant prints of one building, U.028 | `WALMART_AR_1976.txt` (S0105) W-49; `WALMART_AR_1973.txt` W-33; **U.028** | High (as company statements); **Medium** as a decision attribution — no document names a decision-maker |
| **1970-02-01** | **Pool the "various subsidiaries" and related-business assets into one registrant**, by an exchange of common stock contributed by **Walton Enterprises, Inc.**, subject to liabilities including the assumed $968,876 bank note | multiple separate corporations filing **separate** income-tax returns through FY1972; a principal shareholder whose form of organisation **no document states** | what the audited note prints; that separate returns continued, that a consolidated federal return was filed only for the year ended 1973-01-31, and that the IRS had extended proposals for 1969-01-31 and 1970-01-31 | **Names, dates and states of every predecessor subsidiary** ("appear nowhere in these reports" — part 1 §B.0); what Walton Enterprises, Inc. *was*; which of the fifteen stores entered the pool | staying separate; a merger purchase-accounting route instead of a pooling | the pooling had to be executed before the FY1972 report's consolidated columns could exist | **NOT STATED.** The note gives the accounting treatment, not a business reason | The group's consolidated life begins here, and **FY1968–FY1971 are labelled pro forma because of it** — the company's own admission that the reporting entity is an artifact | the registrant's first audited year-end is FY1972 with **$78,014,164** sales and 51 stores; **8 years of claimed history sit outside the consolidated entity** | `WALMART_AR_1972.txt` Notes 1 and 6 (S0101); `WALMART_AR_1973.txt` Note 6 (S0102); A2 W-04, W-21; **U.102, U.108** | **High** as a fact (audited note); **Medium as a boundary** (part 1 §C.0 keeps 1970-02-01 as the **live losing rival** to the adopted close) |
| **1970-10-08** | **Sell 200,000 shares to the public** — float the registrant | 6,000,000 shares outstanding, wholly family/Enterprise-side; **no float percentage is stated in any document** | the note's own line: "Excess of net proceeds over par value of 200,000 shares sold in public offering October 8, 1970 — 3,010,467"; par value $.10 established in the same note; the derived net per share **$15.15** = (3,010,467 + 20,000) ÷ 200,000 | gross offer price (**$16.50 exists only on an uncited company page, and no document licenses a bridge between $16.50 and $15.15** — U.031); underwriter; whether 200,000 shares is the whole offer or the newly-issued portion; who bought | staying private; a bank-debt route (the group already carried a bank note at the pooling); a larger float | **~6.7% of the pre-split share base sold — DERIVED** (6,000,000 ÷ 2 = 3,000,000; 200,000 ÷ 3,000,000 = 6.7%), arithmetic shown because the documents never state a float percentage | **NOT STATED** | **UNKNOWN as stated by anyone.** What is documented is the accounting effect | family control is consistent with a 6.7% float, but **no local document states an ownership percentage** (part 1 §B.2) | `WALMART_AR_1972.txt` capital note (S0101); the same-lineage FY1974/FY1980 OTC sentences; **the one structurally independent datum in the cluster is a negative**: the SEC's 31-Dec-1970 exchange-issuer register omits the company (`S0139`, pending) — **it corroborates OTC status and no figure**; **U.031, U.210** | **High** (the note prints it) / **Medium** (a 1972 document reporting a 1970 event, same lineage) |
| **post-boundary control rows** | NOT DECIDED IN STAGE 1 — recorded so no later pass re-imports them into this window | — | LIFO adoption effective 1975-01-31 (−$2,347,000, auditor-flagged); the FY1974 Family Center stop-rule ("Further expansion of this division will depend on the results obtained from these first two units"); SFAS-13 restatement FY1979; the 1972-08-25 NYSE listing (**a venue change, not a stock event**) | — | — | — | — | — | — | `WALMART_AR_1975.txt` (S0104); `WALMART_AR_1974.txt` (S0103); `WALMART_AR_1979.txt` (S0108); **part 1 §D.0 D-R09c** (the "one and only split" claim is refuted: 1971-06-11, 1972-04-05, 1975-08-19 — U.015) | High, **out of window** |

### N.2 The absence is the finding, and it has a shape

Eight rows are writable inside the window and **not one carries a rationale**: the corpus's decisions are
visible only as **states that changed** — a fleet mix, an office line, a pooling note, a capital-account line.
The four post-boundary controls at the end of §N.1 prove the registrant *could* state a gate and a reason in
its report prose (FY1974's expansion sentence is an explicit stop-rule), **so the in-window silence is a
property of the surviving record and not of the genre** — which is the strongest statement this volume is
licensed to make about §N. Confidence in that statement: **High**, because both its legs are printed (the
FY1974 gate exists; no in-window gate exists in nine files).

### N.3 Knowability

| Kind | Item |
|---|---|
| **KNOWABLE in-period** | The pooling and the float, as accounting and capital events (the company's own audited note); the fleet mix at the boundary; that the trade was publicly debating the discount conversion in 1961 (S0133, third party, dated) |
| **NOT KNOWABLE in-period** | Whether the 1962 format would scale; what the float would do to the business; whether the IRS proposals would be sustained |
| **UNKNOWN (named)** | Every rationale in §N.1 (eight rows, zero stated); the identity and terms of the 1945/1946 arrangement; the 1950 cluster; what Walton Enterprises, Inc. was; which subsidiaries entered the pool; the 1970 gross price (U.031); the buyer list; **whether any decision document exists at all** — county and SoS routes UNTRIED (U.211), on-disk local-newspaper JSONs UNMINED (U.202, in flight) |

## O. COUNTERFACTUAL OPPORTUNITIES

STATUS: WRITTEN 2026-09-26

### O.0 The rule this section writes under

A counterfactual is admissible here **only if a document dated in-period shows the alternative existed and was
visible**. Method §2 forbids the reverse construction — inventing a road not taken from the shape of the road
taken. That test is satisfiable for this company, and satisfiable **without the registrant**: the trade body
of the founder's own franchise form put the question on its programme three months before the Rogers opening
— NRMA's first Discount Seminar, titled "**The Discount Business — Is It for You?**", ~800 attendees, "about
one half" of them conventional department stores (`sources/periodicals/STORES_NRDGA_1946-1972_EXTRACT_walton_and_discount.txt`,
S0133, raw offset 61,464, reported December 1961). **Class: CONTEMPORARY OBSERVATION; Tier 3; independence:
an unrelated publisher, so this is the one in-period counterfactual that is not the company talking about
itself.** Note what it does *not* establish: it does not show that anyone at Walton's attended, read or owned
NRMA material — that is **UNKNOWN**, and no inference is offered.

### O.1 The alternatives the record shows were on the table

| Counterfactual | Visible in-period, on what document | What taking it would have required | What the record can say about why it was not taken | Class | Conf |
|---|---|---|---|---|---|
| **Stay in the franchised variety form** | The base is described by the registrant as profitable — "fifteen **successful** Ben Franklin stores" (S0104) — and **14 of 32 units were still Ben Franklin at the boundary** (S0109), so the alternative was not abandoned even in the account that describes the conversion | Nothing: it was the incumbent arrangement, with its wholesale and buying terms intact | **NOT STATED anywhere.** No document gives up a reason for leaving a form the company itself called successful; and the franchise terms themselves are **absent from the corporate print** (A2 §Pre-1962 evidence ledger; part 1 §B.2) | RETROSPECTIVE INTERPRETATION (the state) / **UNKNOWN** (the choice) | High (that the banner survived the boundary); **Low** (that the choice was argued at all) |
| **Convert as a large chain's subsidiary format did** — Woolworth's "Worth Marts" (Dec.26 1964 short item; and "The old five-and-ten spreads new wings", cover, Nov.14 1964) and S. S. Kresge ("How Kresge became top discounter", cover, Oct.24 1970 — **cross-indexed by Business Week under VARIETY Stores as well as DISCOUNT Houses**) | S0115, S0123, dated index entries | Scale capital, an existing buying organisation, and a name to protect | **Nothing in this corpus states whether the company's principals saw these as the model or as the threat.** The Kresge cross-index is, however, **independent evidence that the variety and discount trades were publicly treated as one competitive field in the company's first public year** — which is what makes the counterfactual visible rather than invented | CONTEMPORARY OBSERVATION (the entries) / **UNKNOWN** (the observation by the firm) | High (the entries exist); **UNKNOWN** (any causal reading) |
| **Follow the sector's own consolidation logic: fewer, larger units** — "Fewer stores to share the pie: They get bigger but decrease in number as discounters, chains squeeze little guys" (p.182, Nov.16 1963) against "Nielsen survey shows an increase in the number of mass merchandisers" (p.100, May 16 1964) | S0114, S0115 — index-level only; **no article text is reachable, so no numeric content is asserted** (U.039, U.040) | A slower unit count and a bigger average unit | **The company did the opposite of the first headline and neither confirmed nor denied knowing it existed.** U-A4/6 (→ **U.040**) keeps the sector's contraction beside the registrant's rising unit series (51→78, FY1971→FY1974) and **refuses to explain the gap** — the sector's contraction is *not* converted into the company's good fortune | CONTEMPORARY OBSERVATION; the pair are counterevidence to each other, with different counted classes | Medium (the direction claims); **UNKNOWN** (the universes behind them) |
| **Do not float in 1970, or float more** | 200,000 shares ≈ **6.7% of the pre-split base** — DERIVED in part 1 §B.2 and at §P.5 row P37; the group carried a bank note at its birth and long-term debt appears at **809 → 4,659 (thousands)** FY1971→FY1972 | Either debt (documented as present) or a larger public sale (the FY1972 report prints an April 1972 follow-on: 400,000 shares at $23.75, **$8,913,504** credited to paid-in — U.032) | **NOT STATED.** No document in this corpus discusses the size of the offer as a choice; the FY1972 note records the accounting effect of a completed transaction | FACT (the rows) / **UNKNOWN** (the decision variable) | High (the capital rows); **Low** for any claim about intent |
| **Locate distribution away from Bentonville** | The FY1975 rule is printed: stores served "within a **350 mile radius** of the General Office and Distribution Centers in Bentonville", average community 10,000–15,000 (S0104); the A2 register's only competing DC-location story is a **leased Springfield, Missouri warehouse**, which has **no support anywhere in this corpus** (U.027) | A second property and buying estate outside the home county | **The radius rule is a constraint stated by the company, and it is the closest thing in Stage 1 to a self-imposed boundary on growth.** Whether it was chosen or discovered is not stated; the FY1975 and FY1978/FY1980 population bands **disagree at the low end and both are kept** (U.034) | FACT (the printed rule); INFERENCE (that it bounded site selection) | Medium |
| **Sell the variety estate earlier** | FY1974: "Two Ben Franklin variety stores were sold and four were closed during the year"; FY1976-01: the last dated trace of the banner, a Rogers Ben Franklin closure; the FY1980 retrospective says 14 variety stores "closed" across the 1970s (S0103, S0105, S0109; `timeline.csv` 1976-01 row) | Nothing beyond a transaction | **All four prints sit OUTSIDE the 1970-10-08 boundary** and are listed here only to show the phase-out was a *sequence with an end*, not a 1962 decision; the register must not read them as the founder rejecting the variety form at the founding | FACT | High (printed); **out of window** |

### O.2 What no counterfactual in this section can be given — a falsification test

A stage file may ask "what would have told the founder the experiment had failed?". **No document in this
corpus states a stop-rule, a threshold or a falsifier for the 1962 format.** One explicit stop-rule exists
anywhere in the nine reports, and it is FY1974 and about a different division: "Further expansion of this
division will depend on the results obtained from these first two units" (S0103). Part 1 §D.3 records that
pairing, and §N.1 uses it as the control: the genre **could** state a gate. **Mechanism for the 1962
continuation is therefore UNKNOWN, and the honest counterfactual of §O is not "they could have done X instead"
but "no document shows that X, Y or Z were options anyone ranked."** Alternative explanation retained: the
absence may be a property of the annual-report genre and of a survivor's archive, not of the decision-making —
**untestable on this corpus, and recorded as UNTRIED at U.222** rather than dismissed.

### O.3 Record-selection null and knowability for §O (§2)

Rejected options are precisely what a winner's archive does not keep: nothing in this corpus records a
declined alternative, a lost site, a rejected lease or a failed format **as a dated document inside the
window**. The asymmetry is stated once and applies to the whole section — **the density of the FY1972–FY1980
print is evidence about a company that had already succeeded at being legible**, and §O borrows none of that
density as evidence about 1945–1970 choice architecture.

| Kind | Item |
|---|---|
| **KNOWABLE in-period** | That the discount question was being publicly debated by the founder's own trade body in 1961; that the largest variety chains were entering discount (1964, 1970); that the sector's unit count was reported as falling in 1963 and rising in 1964; the company's own printed trading-area rule (FY1975) |
| **NOT KNOWABLE in-period** | Which of these, if any, anyone at the firm observed; whether the format would scale; whether the float would be repeated (it was, in April 1972 — outside the window) |
| **UNKNOWN (named)** | Why the variety form was kept at the boundary; who set the 350-mile radius; the Springfield-MO DC lore (unsupported, U.027); every falsification test; whether any local Arkansas paper reported the 1962 opening at all (**U.202 / U.206 / U.212–U.213, in flight or untried**) |

---

## P. QUANTITATIVE METRICS TABLE

STATUS: WRITTEN 2026-09-26

### P.0 Reading rules, stated before any row

1. **Basis flag is part of the value.** `CONTEMP` = printed in that fiscal year's own report;
   `RESTAT(in S01xx)` = printed later, in another document's comparative or summary column. Nine printings of
   FY1974 across FY1975/76/77/78/79 are **version evidence, not corroboration** (§3 filing-lineage rule).
   **The independent-lineage count for every row in §P is 1** (A3 §7.2(c), re-tested and unchanged by A5).
2. **Units are not uniform across the break at FY1974/FY1975.** FY1968–FY1974 print in exact dollars; FY1975
   onward in thousands. Rows carry the unit as printed.
3. **Audited status is not uniform.** FY1972–FY1980 sit behind eight dated Arthur Young opinions (Tulsa,
   Oklahoma). **No opinion of any kind attaches to FY1968–FY1971** (A3 §6.1); FY1968–FY1971 earnings rows are
   captioned **"pro forma" by the registrant**, and the multi-year summary tables are outside the wording of
   every opinion on disk. FY1962–FY1967 is **EMPTY** (U.102).
4. **Forbidden operations, printed here so the table cannot be mis-used** — (i) any asset-turn, debt/assets or
   total-asset growth figure computed **across 1978-01-31 / 1979-01-31** (SFAS-13 lease capitalisation;
   U.022); (ii) **cumulating the FY1972–FY1975 square-footage *additions* backwards into a total** — the
   total series begins at FY1976 (U.105); (iii) quoting **any FY1976–FY1979 dividend from the FY1980 ten-year
   table** (refuted; U.026); (iv) quoting a **single FY1973 share count at High** (U.018); (v) using either
   $6-billion or $6.9-billion 1962 sector figure as a **denominator for a company share** (U.039; the
   prohibition is inherited from §H/part 2 and binds §P and `quantitative.csv`); (vi) reading a margin or
   expense step **across 1975-01-31** without the LIFO qualification (U.027-adjacent, A3 §6.1); (vii) using
   the FY1977 report's stated expense ratios **21.1 / 20.5 / 20.8** as data (stated-but-not-reconcilable;
   U.024).

### P.1 Income series, FY1962–FY1980 (`| ID | Date | Metric | Value | Unit | Source | Source date | Confidence |`)

| ID | Date | Metric | Value | Unit | Source | Source date | Confidence |
|---|---|---|---|---|---|---|---|
| P01 | FY1962–FY1967 | Net sales, stores, earnings, balance sheet, square footage, headcount — **every variable** | **EMPTY — no figure in any document** | — | all nine `sources/periodicals/WALMART_AR_197*.txt`/`_1980.txt`; A3-039 | 1972-03-22→1980-04-01 | **UNKNOWN**, recorded as EMPTY within the stated perimeter (U.102) |
| P02 | FY1968 | Net sales | **$12,618,754** — RESTAT(in S0101), only printing anywhere; **outside every opinion** | USD | `WALMART_AR_1972.txt` five-year table (S0101) | 1972-03-22 | Medium (one 1972-dated printing of a 1968 year) |
| P03 | FY1968 | Income before income taxes | $779,754 — RESTAT(in S0101) | USD | S0101; A3 Table S1 | 1972-03-22 | Medium |
| P04 | FY1968 | Net income — *pro forma* | $481,754; **$.09** per share | USD / USD/share | S0101 | 1972-03-22 | Medium; **company's own "pro forma" label kept** |
| P05 | FY1968 | Stores at year end | **24** — RESTAT(in S0102 "Six Years at a Glance") | stores | `WALMART_AR_1973.txt` (S0102); A3 Table S2 | 1973-03-20 | Medium |
| P06 | FY1969 | Net sales / pre-tax / net income *pro forma* / EPS | $21,365,081 / $1,056,211 / $605,211 / $.12 — all RESTAT(in S0101) | USD; USD/share | S0101 | 1972-03-22 | Medium |
| P07 | FY1969 | Stores at year end | **27** — RESTAT(in S0102) | stores | S0102 | 1973-03-20 | Medium |
| P08 | FY1970 | Net sales | **$30,862,659** — RESTAT(in S0101; reprinted S0103 1974, S0107 1978) | USD | S0101; S0103; S0107 | 1972-03-22→1978-04-14 | Medium (**one lineage, three printings**) |
| P09 | FY1970 | Income before income taxes | $2,198,764 — RESTAT(in S0101); **independently consistent** with the FY1978 nine-year table's own rows (2,199 thousand) | USD | S0101; S0107 | 1972-03-22 / 1978-04-14 | Medium-High |
| P10 | FY1970 | Net income *pro forma* | **$1,187,764** register value; the FY1978 table prints "1,011" thousand **and its own rows require 1,239** — that cell is **SUSPECT, not corrected** | USD | S0101/S0103/S0102 vs S0107 | 1972-03-22 / 1978-04-14 | Medium for $1,187,764, **Low** for the alternative — **U.017 open** |
| P11 | FY1970 | Balance sheet — first statement anywhere | current assets 6,703 / net PP&E 1,678 / **total assets 8,493** / current liabilities 3,872 / LTD 1,328 / equity **3,159** (thousands), current ratio 1.7 — **RESTAT(in S0107); no FY1970 report exists** | USD thousands | `WALMART_AR_1978.txt` nine-year table (S0107); A3 Table S4 | 1978-04-14 | High (as printed) / **Medium as FY1970 state** |
| P12 | FY1970 | Stores / EPS *pro forma* | 32 / $.23 (FY1978 table prints $.11 — split-adjusted once for 1975-08-19) | stores; USD/share | S0101; S0107 | 1972-03-22 / 1978-04-14 | Medium |
| P13 | FY1971 | Net sales / pre-tax / net income *pro forma* / EPS | $44,286,012 / $3,170,599 / $1,651,599 / $.30 — RESTAT(in S0101; reprinted S0103, S0104, S0107) | USD; USD/share | S0101 and later prints | 1972-03-22→1978-04-14 | Medium; **no FY1971 report exists** |
| P14 | FY1971 | Balance sheet | 12,150 / 3,080 / **15,331** / 6,513 / 809 / equity **7,841**; current ratio 1.9; **shares outstanding 6,000,000**; inventories $10,654,640 (CONTEMP in S0101) | USD thousands | S0107 (position); S0101 (inventory, shares) | 1978-04-14 / 1972-03-22 | High (as printed) / Medium (basis) |
| P15 | FY1971 | Stores at year end | **38** — RESTAT | stores | S0102, S0103, S0107 | 1973→1978 | Medium |
| P16 | FY1972 | Net sales | **$78,014,164** — **CONTEMP** | USD | `WALMART_AR_1972.txt` (S0101) | 1972-03-22 | **High (as-filed)** |
| P17 | FY1972 | Pre-tax / net income / EPS *pro forma* | $5,569,027 / $2,907,354 / $.47 (later prints $.24) — CONTEMP | USD; USD/share | S0101 | 1972-03-22 | High |
| P18 | FY1972 | Balance sheet | 21,069 / 7,080 / **28,463** / 12,806 / 4,659 / equity **10,748**; current ratio 1.7; inventories $18,452,663; **shares 6,000,000** | USD thousands; USD; shares | S0101 | 1972-03-22 | High |
| P19 | FY1972 | Stores / new store space / headcount | 51 / +604,000 sq ft on 14 new stores / "some 2,300" employees | stores; sq ft; people | S0101 (President's message, signed 1972-03-22) | 1972-03-22 | High (printed) / Medium (headcount basis undefined: "employees" vs "associates" is never defined in any document) |
| P20 | FY1973 | Net sales / pre-tax / net income / EPS | $124,889,141 / $8,917,188 / $4,591,469 / $.70 — **CONTEMP**. **The FY1974 audited statement pages misprint FY1973 as "$124,059,141"; the five-year table governs** (A3-002) | USD; USD/share | `WALMART_AR_1973.txt` (S0102) | 1973-03-20 | High (as-filed) |
| P21 | FY1973 | Balance sheet | 32,787 / 13,233 / **46,241** / 15,990 / 5,066 / equity **24,754**; current ratio 2.1; inventories $29,427,119 | USD thousands; USD | S0102; reprinted exact in S0103 Note 2 | 1973-03-20 / 1974-03-21 | High |
| P22 | FY1973 | Shares outstanding | **6,512,950** per the FY1974 report / **6,512,550** per the FY1973 report (and that report's own two rows print both) — **no single count is quotable at High**; 400 shares in 6.5m, immaterial to every ratio here | shares | S0103 balance-sheet block vs S0102 L103-108 | 1974-03-21 / 1973-03-20 | Medium — **U.018** |
| P23 | FY1973 | Stores; composition; losses | 64 = **55 Wal-Mart + 9 variety/family centre**; three stores lost or damaged by fire/tornado; **first consolidated federal return filed**; the +13 net against 16 openings + 2 relocations implies **≥5 unlisted exits** | stores; events | S0102; A2 W-34, W-37 | 1973-03-20 | High (printed) / **UNKNOWN (the exits)** — U.030 |
| P24 | FY1974 | Net sales / pre-tax / net income / EPS *pro forma* | **$167,560,892 / $11,883,754 / $6,158,520 / $.93 (pre-split)** — **CONTEMP from the Five Year Progress Report, NOT the audited statement pages** (FY1974's own column is missing there) | USD; USD/share | `WALMART_AR_1974.txt` (S0103); A3-002 | 1974-03-21 | High |
| P25 | FY1974 | Balance sheet | 45,254 / 14,657 / **$60,105,646** / 18,121,532 / 10,578 / equity **$30,734,128**; current ratio 2.5; **inventories $41,470,471** (stores $33,713,932 + DC $7,756,539), **FIFO/retail-method basis — pre-LIFO** | USD thousands; USD | S0103 | 1974-03-21 | High |
| P26 | FY1974 | Stores / additions / headcount / dividend | 78 / +881,630 sq ft, 20 new + 4 expanded or rebuilt, 6 closed / **4,500 employees (chart, round)** / **$.025 first evidenced dividend payment, 1974-04-05, RESTAT in S0107's nine-year table — the FY1974 report's own table has no dividend row** | stores; sq ft; people; USD/share | S0103; S0107; A2 W-54 | 1974-03-21 / 1978-04-14 | High (stores, sq ft) / Medium (headcount, dividend basis) |
| P27 | FY1975 | Net sales | **$236,209 thousand — NOT PRINTED on the FY1975 text layer**; recovered by inverting the same table's five printed rows (5,855 + 6,353 + 1,800 + 48,088 + 176,591 − 2,478 = 236,209); later prints 236,209 (S0106, S0107, S0108) and $236,209,000 (S0109). **The FY1976 text layer reads 226,209** | USD thousands | `WALMART_AR_1975.txt` (S0104) + later prints | 1975-03-28→1979-04-06 | **Medium-High, open — U.016.** The 2-vs-3-digit ambiguity is recorded **in the file's own header**; the page image that decides it is UNTRIED (`S0111` lead; **U.205, in flight**) |
| P28 | FY1975 | Pre-tax / net income | 12,208 / **6,353\*** — CONTEMP (asterisked in the original for the LIFO year); SFAS-13 restated **11,521 / 5,995** in S0108 | USD thousands | S0104; restated S0108 | 1975-03-28 / 1979-04-06 | High — **two live bases, both kept: U.019/U.020** |
| P29 | FY1975 | Cost of sales / operating+S&G+admin | 176,591 / 48,088 — CONTEMP (first witness of FY1975's expense rows from its own year) | USD thousands | S0104 | 1975-03-28 | High |
| P30 | FY1975 | Balance sheet | 55,860 / 19,157 / **75,221** / 26,190 / 11,132 / equity **36,935**; current ratio 2.1 — **RESTAT(in S0106, then S0107, S0108)**: FY1975's own text layer drops its balance sheet | USD thousands | S0106; S0107; S0108 | 1976-03-26→1979-04-06 | High (as printed) / **Medium (a restated FY1975 position)** |
| P31 | FY1975 | Stores; fleet composition; additions; DC; headcount | **104** = 100 Discount Cities + 2 Family Centers + 2 Sav-Co (the state table sums to 104 ✓) / **+1,083,326 sq ft — "a record for new store space in a single year"** / new 150,000 sq ft DC in operation January 1975 (8 rail + 37 truck doors vs the original DC's 6 + 28) / **"approximately 5800 associates"** | stores; sq ft; people | S0104 | 1975-03-28 | High (as-filed) |
| P32 | FY1976 | Net sales / pre-tax / net income / EPS | $340,331k / 22,798 CONTEMP (restated **22,057**) / 11,506 CONTEMP (restated **11,132**) / $.83 primary, $.80 diluted | USD thousands; USD/share | `WALMART_AR_1976.txt` (S0105) | 1976-03-26 | High / restated pair kept beside it (U.019) |
| P33 | FY1976 | Stores / total space / DC space / shares / dividend | 125 / **5,295,000 sq ft — the FIRST total square footage printed anywhere** / 238,800 sq ft warehouse + 150,000 sq ft DC + 31,000 sq ft GO addition April 1976 / 13,418,063 shares / **$.065** (refutes the FY1980 table's $.09) | stores; sq ft; shares; USD/share | S0105; S0107 (nine-year table) | 1976-03-26 / 1978-04-14 | High — **headcount FY1976 = UNKNOWN: the report's employee chart is OCR-damaged and the values are not guessed** (U.114) |
| P34 | FY1977 | Net sales / pre-tax / net income / EPS | **$478,807k CONTEMP** / 31,833 DERIVED from the FY1977 report's own rows (15,287 + 16,546) — restated **30,857** / **16,546 CONTEMP** — restated **16,039** / $1.19 primary (restated $1.15), $1.12 diluted (restated 1.08) | USD thousands; USD/share | `WALMART_AR_1977.txt` (S0106); restated in S0108 | 1977-04-01 / 1979-04-06 | High; **U-A3/4 → U.020 is the FY1977–FY1978 two-live-bases conflict and neither value is primary** |
| P35 | FY1977 | Balance sheet / stores / space / DC / headcount / dividend | 99,493 / 33,091 / **133,158** / 41,929 / **23,245 as one line, or 19,158 + 4,087 capital leases as S0107 splits it** / equity 66,183; inventories **$88,815,000** (gross $99,405,000 less LIFO reserve $10,590,000) / 153 stores / ≈6,500,000 sq ft / ≈550,000 sq ft Bentonville distribution, ~80% of merchandise through it / "10,000 associates" / **$.085** | USD thousands; USD; stores; sq ft; people; USD/share | S0106; S0107 | 1977-04-01 / 1978-04-14 | High — **U.023** on the two debt presentations (leverage 0.351 or 0.289 for one date depending on print) |
| P36 | FY1978 | Net sales / pre-tax / net income / EPS | $678,456k / 42,186 DERIVED (20,300 + 21,886) — restated **40,847,000** / **21,886 CONTEMP** — restated **21,191,000** / $1.53 (restated $1.48), 1.46 diluted (restated 1.41) | USD thousands; USD/share | `WALMART_AR_1978.txt` (S0107, the cleanest layer and A3's reference copy); restated in S0108 | 1978-04-14 / 1979-04-06 | High; **U.020, U.021** (the restatement's own size is stated $769,000 and computed $695,000 inside one document) |
| P37 | FY1978 | Balance sheet — **THE SERIES BREAKS HERE** | 150,986 / 55,402 / **206,691 as published** → **251,865 as restated** / 73,083 → 74,891 restated / LTD 21,489 / **capital-lease obligations 10,904 → 59,003** / equity **98,943 → 96,482**; current ratio 2.1 → 2.02; inventories $135,845,000 (LIFO; replacement cost $14,148,000 higher) | USD thousands | S0107 vs S0108 comparative | 1978-04-14 / 1979-04-06 | **High — U.022. Any asset growth or turn across this date is invalid** |
| P38 | FY1978 | Stores / space / comparable sales / DC / gross margin | **195** = 30 new + 10 expanded or relocated + **16 acquired** − 4 closed / 8,500,000 sq ft / **comparable-store sales +17%** — *the only same-store figure printed in the nine reports*, and **its store population and dollar base are undefined, so the denominator is UNKNOWN** / Searcy AR 390,000 sq ft DC under construction from 1977, "capability of servicing one-half of the existing Wal-Mart stores" / gross margin **25.7%** (from 26.3%) | stores; sq ft; percent; USD/share | S0107 | 1978-04-14 | High (rows) / **Medium** (the 17%: self-reported, undefined base). **FY1978 headcount UNKNOWN** (U.114) |
| P39 | FY1979 | Net sales / pre-tax / net income / EPS | **$900,298,000 / $56,772,000 / $29,447,000 / $1.93 primary and diluted** — CONTEMP; check: 909,913,000 − 853,141,000 = 56,772,000 ✓; implied taxes 27,325,000 = 48.1% effective | USD | `WALMART_AR_1979.txt` (S0108) | 1979-04-06 | High |
| P40 | FY1979 | Balance sheet (post-SFAS-13) / shares / dividend / headcount / space | **$324,666,000** (98,868,000 + 25,965,000 + 72,357,000 + 127,476,000 ✓) / current liabilities 98,868,000 / LTD 25,965,000 / **capital leases 72,357,000** / equity **127,476,000**; current ratio 1.94; inventories $172,640,000 (replacement cost $22,271,000 higher) / **15,079,383 shares** / **$.22** (four quarters at $.055) / "over 17,500 associates" / 10,200,000 sq ft / 229 stores | USD; shares; USD/share; people; sq ft; stores | S0108 | 1979-04-06 | High — **NOT comparable with any pre-FY1979 asset figure** (U.022) |
| P41 | FY1980 | Net sales / pre-tax / net income / EPS / balance sheet / stores / space / headcount | $1,248,176k / 74,288k / 41,151k / $2.68 both bases / **$457,879k assets, $164,844k equity, capital leases $97,212k**, inventories $235,315k (replacement cost $38,899k higher) / 276 stores / 12,600,000 sq ft / "more than 21,000 associates" | USD; USD/share; stores; sq ft; people | `WALMART_AR_1980.txt` (S0109) | 1980-04-01 | High (as-filed); **FY1980 operating profit left UNKNOWN rather than reconstructed from a rounded 20.2% expense ratio** (A3 Table S1) |
| P42 | FY1968–FY1972 | Earnings basis as captioned | **"Pro forma net income" / "Pro forma net income per share"**: $.09 / $.12 / $.23 / $.30 / $.47 — the registrant's own label for years in which the reporting group did not exist | USD/share | S0101 (and S0102, S0103 prints) | 1972-03-22→1974-03-21 | High (as printed) — **the label is the finding: U.102** |

### P.2 Capital, splits and the boundary event

| ID | Date | Metric | Value | Unit | Source | Source date | Confidence |
|---|---|---|---|---|---|---|---|
| P43 | 1970-10-08 | Shares sold in the public offering | **200,000** | shares | S0101 capital note ("…200,000 shares sold in public offering October 8, 1970") | 1972-03-22 | High (the note prints it) / **Medium as a 1970 fact** — a 1972 document reporting a 1970 event, one lineage |
| P44 | 1970-10-08 | Excess of net proceeds over par value | **$3,010,467** (the FY1972 note line). Total net proceeds **$3,030,467** = 3,010,467 + 20,000 par — DERIVED, arithmetic shown | USD | S0101 | 1972-03-22 | High (row) / Medium (the addition) |
| P45 | 1970-10-08 | Implied **net** per share | **$15.15** = (3,010,467 + 20,000) ÷ 200,000 — **DERIVED, not observed**; par $.10 evidenced in the same note (1,500,000 → 150,000; 3,000,000 → 300,000) | USD/share | DERIVED from S0101 | 1972-03-22 | **High as arithmetic; UNKNOWN as the gross offer price.** $16.50 exists only on the uncited company page and **no local document licenses a bridge between $16.50 and $15.15** — **U.031** |
| P46 | 1970-10-08 | Share of the issuer sold publicly | **≈6.7%** = 200,000 ÷ 3,000,000 pre-split shares; the pre-split base is itself DERIVED (6,000,000 post-split ÷ 2, for the 1971-06-11 two-for-one) | percent | DERIVED from S0101's own rows | 1972-03-22 | **Medium — INFERENCE on the pre-split base**; no document states a float percentage or an ownership percentage |
| P47 | 1971-06-11 / 1972-04-05 / 1975-08-19 | Two-for-one stock splits | **THREE events**: 1971-06-11 (1,500,000 shares, $150,000 par charge) and 1972-04-05 (3,000,000 shares, $300,000 par charge), both inside S0101's own capital note; 1975-08-19 (6,687,789 shares, $668,779 at $.10 par, S0105 Note 4) | shares; USD | S0101; S0105 | 1972-03-22 / 1976-03-26 | High — **the "one and only split" claim in part 1 §D-R09 is REFUTED on the page and the refutation is U.015; only the 1975-08-19 event falls inside the EPS-restatement dispute, and the halving pattern (FY1974 $.93 then $.47) proves one adjustment, not two** |
| P48 | FY1971/FY1972 → FY1979 | Shares outstanding | 6,000,000 / 6,000,000 / 6,512,950-or-6,512,550 (FY1973, **U.018**) / 6,542,250 (FY1974) / 6,659,650 (FY1975, RESTAT in S0105) / 13,418,063 (FY1976) / 13,649,829 (FY1977) / 14,867,711 (FY1978, RESTAT in S0108) / **15,079,383 (FY1979, CONTEMP)** | shares | S0101, S0103, S0105, S0106, S0108 | 1972→1979 | High (each print), **Medium as a series** (basis changes across splits and restatements) |
| P49 | FY1974→FY1980 | Dividends per share, **contemporaneous rows only** | $.025 (1974, first evidenced, **RESTAT in S0107**) / $.05 (1975, RESTAT in S0107) / **.065** / **.085** / **.16** (quarterly .025/.045/.045/.045 ✓) / **.22** (four at $.055 ✓) / $.30 raised to $.40 after year end | USD/share | S0105, S0106, S0107, S0108, S0109 | 1976-03-26→1980-04-01 | High — **the FY1980 ten-year row (1976 $.09 / 1977 $.11 / 1978 $.19 / 1979 $.25) is REFUTED for all four years and is barred from `quantitative.csv`; $.09 ÷ $.065 = 1.38 is not a split factor. U.026; COR-A3-04** |
| P50 | 1970-02-01 / FY1971 / FY1972 | Pooling-date capital lines | "Excess of paid-in capital of pooled companies … at February 1, 1970 **$1,470,139**"; assumed bank note **$968,876**; stockholders' equity **$7,840,701 → $10,748,055**; current ratio **1.87 → 1.65** | USD; USD thousands | S0101 Note 1 and FINANCIAL HIGHLIGHTS; A3 Table S4 | 1972-03-22 | High (as-filed FY1972; the FY1971 column is a 1972-dated comparative) |
| P51 | 1972-04 | April 1972 follow-on offering (out-of-window control) | 400,000 shares at **$23.75** before expenses ⇒ **$9,500,000** gross arithmetic; paid-in capital **+$8,913,504**; the President's letter says "approximately **$9,250,000**" (OCR prints the leading figure as "59,250,000.00"); >3,400 holders; a $15,000 stock-exchange filing fee charged against capital | USD | `WALMART_AR_1973.txt` letter + Note 4 (S0102), A2 W-29/W-30 | 1973-03-20 | High (that the three totals coexist); **Medium for any single "amount raised"** — **U.032** |
| P52 | 1972-08-25 | Venue change | Stock **listed on the NYSE**; OTC since October 1970. **Any 1972-08-25 price break is a venue move, not a stock event** | — | S0103 (its own year's print, A3-019); S0108 | 1974-03-21 | High |
| P53 | FY1975→FY1980 | Market price series | **No market price exists before FY1975 anywhere in the corpus**; the earliest price table is the FY1976 report's quarterly highs/lows reaching back only to fiscal 1975 | — | A2 W-54; A3 §Data gaps | 1976-03-26 | **EMPTY within perimeter — U.106** |

### P.3 Physical and organisational series (retail frame: stores / space / supply chain / people)

| ID | Date | Metric | Value | Unit | Source | Source date | Confidence |
|---|---|---|---|---|---|---|---|
| P54 | 1970-01-01 | Fleet at the boundary | **18 Wal-Mart Discount Cities + 14 Ben Franklin variety stores**, four-state area, "with sales totaling $31 million", "less than a million square feet" — **a 1980-dated statement of a 1970 state** | stores; USD; sq ft | S0109; the 18 corroborated **within the same lineage** by S0101's "eighteen Wal-Mart stores that already existed as of February 1, 1970" | 1980-04-01 / 1972-03-22 | High (both documents say it) / **Medium** (the state). **The 18+14 = 32 agreement with the audited FY1970 count is an internal check, not a second source** |
| P55 | FY1968–FY1980 | Store count, year end | 24 · 27 · 32 · 38 · 51 · 64 · 78 · 104 · 125 · 153 · 195 · 229 · 276 — FY1968–FY1971 RESTAT, FY1972 onward **CONTEMP** | stores | S0101–S0109; A3 Table S2 | 1972-03-22→1980-04-01 | High (CONTEMP years) / Medium (FY1968–FY1971) |
| P56 | FY1972–FY1975 | Total store square footage | **UNKNOWN for every year** — the reports print **additions only** (604,000 FY1972; 781,940 FY1973; 881,630 FY1974; 1,083,326 FY1975). **The addition series must not be cumulated backwards into a total** | sq ft | S0101–S0104 | 1972→1975 | High (additions) / **EMPTY (totals) — U.105** |
| P57 | FY1976–FY1980 | Total store/retail square footage | 5,295,000 · ≈6,500,000 · 8,500,000 · 10,200,000 · 12,600,000 | sq ft | S0105–S0109 | 1976-03-26→1980-04-01 | High (FY1976, FY1978, FY1979, FY1980) / Medium (FY1977 "approximately") |
| P58 | FY1975–FY1979 | Headcount | 5,800 (FY1975) · **UNKNOWN (FY1976, chart OCR-damaged)** · 10,000 (FY1977) · **UNKNOWN (FY1978, not found this pass)** · 17,500+ (FY1979); plus 2,300 (FY1972) and 4,500 (FY1974) | people | S0101, S0103, S0104, S0106, S0108 | 1972→1979 | Medium — **company-stated, round, and the basis ("employees" vs "associates") is never defined in any of the nine documents. FY1973, FY1976 and FY1978 are gaps, not zeros: U.114** |
| P59 | 1971-08-15 → 1980 | Distribution estate | 60,000 → **124,800** sq ft completed 1971-08-15 (S0101) · new 150,000 sq ft DC in operation **1975-01** (8 rail + 37 truck doors) · second 150,000 sq ft DC completed **1976-11** → 300,000 sq ft "pure distribution center" on a two-and-one-half-day cycle, ≈550,000 sq ft all-Bentonville · **Searcy AR 390,000 sq ft** under construction from 1977 · Bentonville 390,000 sq ft opened **1980-01**; Palestine TX 510,000 planned | sq ft | S0101, S0104, S0106, S0107, S0109 | 1972-03-22→1980-04-01 | High (as-filed) / **the *first* DC's start date, tenure and site are UNKNOWN — U.027** |
| P60 | FY1972–FY1980 | Share of merchandise flowing through the company's own DC | 55% (FY1974) → **~60%** (FY1975) → **~80%** (FY1977); FY1976 print "80% of purchases through Bentonville" | percent | S0104, S0105, S0106 | 1975→1977 | Medium (company-stated, denominators unstated) |
| P61 | FY1975 / FY1979 / FY1980 | Store-size and town-size rules as the company stated them | FY1975: 350-mile radius of Bentonville, average community **10,000–15,000**, average store ~42,000 sq ft (range 30,000–60,000) · FY1979: size range now **30,000–83,000 sq ft**, 36 departments · FY1980: towns of **5,000–25,000**, average ~45,000 sq ft, "over 35,000 items" | sq ft; people | S0104, S0108, S0109 | 1975-03-28→1980-04-01 | Medium (self-characterisation) — **the FY1975 average and the FY1978/FY1980 range are different quantities and both are kept: U.034** |
| P62 | FY1971 / FY1976-02-01 | Benefit and governance acts | "A new **profit sharing program** was adopted by our Board of Directors for all regular Wal-Mart employees" (FY1971); eligibility cut from two years to one year effective 1976-02-01; an **Audit Committee** was constituted in FY1976; Ronald Mayer signs as Chairman and CEO in FY1976 | — | S0101; S0105 | 1972-03-22 / 1976-03-26 | High (as stated) — **the FY1971 act is the only organisational decision dated inside the window by a signed document** |

### P.4 Derived metrics (all **DERIVED**; arithmetic shown per §8 and §13)

| ID | Date | Metric | Value | Unit | Source | Source date | Confidence |
|---|---|---|---|---|---|---|---|
| P63 | FY1971→FY1972 | Net sales growth | **+76.2%** = 78,014,164 ÷ 44,286,012 − 1. The President's letter prints "77% increase over $44,000,000" against rounded figures: **the letter's own rounding of the same two audited numbers** | percent | DERIVED from S0101 | 1972-03-22 | High |
| P64 | FY1968→FY1971 | Sales growth per year of the pro-forma run | FY1968→FY1969 +69.3% (21,365,081 ÷ 12,618,754 − 1); FY1969→FY1970 +44.5%; FY1970→FY1971 +43.5% — **each on a RESTAT, unaudited, pro-forma-labelled base** | percent | DERIVED from S0101 | 1972-03-22 | **Low-Medium: the arithmetic is exact, the basis is the weakest in the register** |
| P65 | FY1972 | Cohort vs chain growth | The 18 pre-1970 unexpanded stores grew **17%**; the chain grew **76.2%** — **the arithmetic shape of repeatability: growth came from new units added to a base that kept growing** | percent | S0101 President's message; DERIVED check as P63 | 1972-03-22 | High (printed pair) / **Medium as a validation signal** (part 1 §D.3: **nothing about cohort profitability is printed**, and the cohort's share of FY1972 sales is UNKNOWN and deliberately not back-solved) |
| P66 | FY1978 | Sales per store (period-end count) | **$3,479,262** = 678,456,000 ÷ 195 | USD/store | DERIVED from S0107 | 1978-04-14 | Medium — **the denominator is a period-end count against a full-year numerator; the average-store count is not printed for any year, so the correct version of this metric is UNKNOWN** |
| P67 | FY1976 / FY1980 | Sales per square foot | **$64.27** = 340,331,000 ÷ 5,295,000 (earliest computable year) → **$99.06** = 1,248,176,000 ÷ 12,600,000 | USD/sq ft | DERIVED from S0105, S0109 | 1976-03-26 / 1980-04-01 | Medium — **no total square footage exists before FY1976, so no earlier value is computable (U.105); the space label ("store/retail") is undefined** |
| P68 | FY1978→FY1979 | Return-on-assets and debt/equity across the SFAS-13 line | **NOT COMPUTED — INVALID.** FY1978 total assets exist at 206,691 *and* 251,865 thousand for one date; FY1979's 324,666,000 is post-SFAS-13. FY1979 debt/equity **within** the new basis: (25,965,000 + 72,357,000) ÷ 127,476,000 = **0.771**, or **0.204** excluding capital leases — **both reported because "debt" has two definitions in these documents** | ratio | DERIVED from S0108 | 1979-04-06 | High (each within-basis ratio); **the cross-year ratio is refused: U.022** |
| P69 | FY1970–FY1978 | Return on assets / equity | **Taken as printed, not re-derived.** The FY1978 table's own footnote gives the basis — "**On beginning of year balances**" — and A3 verified eight cells to the dollar (FY1976 11,506 ÷ 75,221 = 15.3 ✓ … FY1971 1,652 ÷ 3,159 = **52.3** ✓ on equity). **FY1970's printed 20.7 / 49.4 depend on FY1969 assets and equity, which no document states ⇒ those two cells are not checkable and are printed as stated only** | percent | S0107 nine-year table + A3 §5.7 verification | 1978-04-14 | High (the verified cells) / **Medium (FY1970, unchecked)** |
| P70 | FY1973, FY1969, FY1977 | Leap-day effect on growth | Fixed **31 January** year ends in all nine reports; **no report states a 52/53-week convention** (A3-018). Calendar-fixed years ⇒ no growth rate here is distorted by a shifted year end; the only length effect is the **leap day inside FY1969, FY1973 and FY1977 (+0.27%)** | percent | nine files' heading lines; DERIVED 1 ÷ 365 | 1972→1980 | High (convention); High (arithmetic) |
| P71 | FY1975 | Expense ratio, as computed from the year's own printed rows | **20.36%** = 48,088 ÷ 236,209 — **and the computation is only as good as P27**, whose top line is DERIVED | percent | DERIVED from S0104 | 1975-03-28 | Medium — **carries U.016's uncertainty forward; the FY1977 letter's stated 20.5% series is NOT reconcilable with these rows (U.024)** |

### P.5 Sector comparators kept OUT of company denominators (rows exist in `quantitative.csv`; restated here as a prohibition)

| ID | Date | Metric | Value | Unit | Source | Source date | Confidence |
|---|---|---|---|---|---|---|---|
| P72 | 1962 | SECTOR — Business Week's characterisation on entry | "$6-billion industry … facing a major shakeout" (p.78, Dec.1 1962) — **index-level only** | USD/year | S0112 | 1962-12-01 | Medium (that it was published); **UNKNOWN what it measured** |
| P73 | 1962 | SECTOR — the same publisher's later figure for the same calendar year | **$6.9 billion** (p.132, Jul.13 1963, short item, subject noun lost to OCR reflow) | USD/year | S0114 | 1963-07-13 | Low; **both values stand; the 15% gap is material to any share calculation and no share is calculated — U.039** |
| P74 | 1958-06 | SECTOR — NRDGA member survey of discount penetration | **28% more / 6% fewer / 66% no change** (sums to 100 ✓, single-response survey) | percent-of-respondents | S0131, raw offsets 32,746 / 32,858 | 1958-06 | Medium — **respondent universe UNTRIED; a sector penetration measure, not a company measure** |
| P75 | 1961-12 | ASSOCIATION — NRMA membership scale | "over 11,500 retail establishments … combined annual sales of over $19 billion"; **DERIVED average $1,652,174 per establishment = 19,000,000,000 ÷ 11,500** (A4's arithmetic, printed to keep the derivation visible) | establishments; USD/year; USD/establishment | S0133, offset 13,749 | 1961-12 | Medium (inputs, both floor values from an association describing itself); **Low (the quotient — an undefined mix). NEVER a denominator for a Wal-Mart share of industry** |
| P76 | 1961-12 | SECTOR — discount markup on hard goods as stated at NRMA's Discount Seminar | **26 to 28 percent**, qualified in the print (stores with large small-electricals volume ran lower) | percent | S0133, offset 74,633 | 1961-12 | Medium — **NOT comparable with the registrant's whole-store gross margins (25.7% FY1978, 26.3% FY1977): different measures, different bases; U.041** |
| P77 | 1962–1971 | COMPANY — occurrences of the name in the Business Week index apparatus | **0 named-index-entries across ten index years / 13 half-and-full volumes, ~1.06 million words, every layer byte-exact against its own metadata** | count | S0112–S0124 | 1962→1971 | **High — the headline null of the dossier, and it is a statement about the reachable corpus, not about the world: U.101** |
| P78 | 1970-12-31 | COMPANY — occurrences in the SEC's complete exchange-issuer register | **0 in 153,481 words / 941,197 bytes read whole**, while the same W-block legibly prints WALGREEN, WALWORTH, WALTHAM, WALLACE-MURRAY, WALCO (so OCR loss is excluded) | count | `sources/gov_docs/SEC_SecuritiesTradedOnExchanges_asof-1970-12-31_IA-securitiestraded1970unit.txt`; the row is pending in the register as `S0139` | 1971 | **High — a DENOMINATED NEGATIVE: it witnesses the ABSENCE OF EXCHANGE LISTING at that date and nothing else; it does NOT move the lineage count** |
| P79 | 1946–1961 / 1970–1975 | COMPANY — named mentions in *Stores* (NRDGA/NRMA) | **0** in the 7 monthly issues read whole of ~200 (1946-06, 1950-06, 1951-06, 1955-06, 1958-06, 1961-03, 1961-12) and **0** in all five annual indexes that exist on this route — **the 1971 index is subject-only (`wal-mart` 0 · `walton` 0 · `ben franklin` 0 · `variety` 0 · `discount` 0), which proves the index did not carry the subject, not that the trade ignored the firm** | count | S0125–S0133 | 1946→1975 | Medium (monthly, worst OCR 1946); **the 193 unread issues are UNTRIED — U.212 — so the licensed sentence is "the issues sampled do not name it"** |
| P80 | 1970–1979 | ROUTE-STATE, not a company metric | HathiTrust full-view records whose OCR matches "Wal-Mart" with the 1970s decade facet: **573**; of the first 100, **52 are SEC serials** | records | `S0137` (A4-43) and the A5 re-walk (`S0141`-pending); `quantitative.csv` already carries the 573 row | 2026-09-25 | High (as counts of an index) — **no item text has been read, so no naming is established and the lineage count is UNCHANGED: U.044, U.207, U.208** |

**Coda (§16 duty).** §P is deep in exactly one direction. FY1972–FY1980 has a contemporaneous witness for
every primary income-statement line of every year, eight dated opinions, and cross-year identities that close
to the dollar — **A3 §7.2(a) calls that `DEPTH-CORE (single-lineage)`, and this table adopts the label.** The
same table's left-hand end, FY1962–FY1971, is **pro forma, restated, unaudited, and silent for six of its ten
years**; A3 §7.2(b) calls it `PROVISIONAL — NOT CORE` and so does §P. The two halves are not averaged. Where a
mechanism would normally be read out of a table like this one — why margins moved, what a capital raise bought,
what the fleet mix did to returns — **the mechanism is UNKNOWN**, because the documents that would carry it
(the FY1970/FY1971 reports, the 1970 registration statement, county and trade records) are absent or untried.

## Q. CHRONOLOGICAL MICRO-TIMELINE

STATUS: WRITTEN 2026-09-26

**Column discipline, because this is the table a later pass will copy.** The first column is the **event**
date; the second block names the **earliest document on disk that carries the event**, with that document's own
date; the third is the **distance** between them, which is the quantity that decides how much weight the row
can bear. Every pre-1972 row is therefore self-indicating: the distance column *is* the evidentiary finding.
Rows marked **[RESEARCH-STATE]** are events in this project's retrieval history, not in the company's history,
and are included because they change what a later pass can reach (method §14 rule 3, §15.1).

### Q.1 The claimed opening and the pre-1962 layer — all distances ≥ 18 years

| Event date | Event | Earliest document carrying it (own date) | Distance | Class | Conf | Anchor |
|---|---|---|---|---|---|---|
| 1945 | **Claimed origin**: Ben Franklin franchised variety store, Newport, **Arkansas** | `WALMART_AR_1973.txt` (S0102) — "twenty-eight year history", a 1973−28 back-cast | **28 years** | FOUNDER CLAIM / RETROSPECTIVE INTERPRETATION | **Low** (event) / High (that the company dated itself thus by 1973) | U.101, U.110 |
| 1945→1980 | The same sentence re-prints: FY1974 "twenty-nine year history", FY1975, FY1977, FY1978, FY1979, FY1980 "Beginning in 1945, with a Ben Franklin franchised store in Newport, Arkansas" | S0103…S0109 (1974-03-21 → 1980-04-01) | distance **grows 28 → 35 years** | one source printed six times | High (the telling) / Low (the told) | U.045 |
| 1946 | The brothers' **partnership** (S0107); Bud Walton's Versailles, Missouri store (S0106); the fifteen-store count "between 1946 and 1962" (S0108) | 1977–1980 prints | ≥31 years | RETROSPECTIVE INTERPRETATION | Low | U.045 |
| c. 1950 | Bentonville store purchase / lease loss (**memoir-only cluster**) | **NO DOCUMENT.** Museum's claimed 1950 bill of sale has no bytes in this repository | — | **UNKNOWN** | UNKNOWN | U.110, U.211, U.214 |
| 1955 | **First named premises**: "The first office was established above Walton's Family Store in Bentonville, Arkansas, in 1955" | `WALMART_AR_1976.txt` (S0105), 1976-03-26 | 21 years | FACT (as a 1976 company assertion) | Medium | — |
| 1957 | Office moved to a small building on Southeast A Street, Bentonville | S0105 | 19 years | company assertion | Medium | — |
| 1958-06 | **[SECTOR]** *Stores* member survey: discount spread "slowing down" — 28% more / 6% fewer / 66% no change | S0131, June 1958 issue | contemporaneous, third party | CONTEMPORARY OBSERVATION | Medium | §P row P74 |
| 1961-11 | **[SECTOR]** NRMA's first Discount Seminar, "The Discount Business — Is It for You?", ~800 attendees, half conventional department stores | S0133 (Dec 1961 issue) | contemporaneous | CONTEMPORARY OBSERVATION | High | U.041 |
| 1961-12 | **[SECTOR]** "Nichols Discount Cities since 1958, and with a long previous history in variety stores" — a variety-to-discount precedent printed in the founder's own trade journal **before the company existed** | S0133, offset 91,292 | contemporaneous | FACT | High | U.041 |
| 1962 (month contested) | **First Wal-Mart Discount City opens, Rogers, Arkansas** — "in Rogers, Arkansas in 1962" (S0103); "November 1962" (S0104, S0107); company page: **2 July 1962**; FY1980 names **J. L. Walton as co-operator** | **S0103, 1974-03-21** is the first document anywhere to date it | **12 years** to the year, **12.4** to the month | FOUNDER CLAIM (retrospective), **Low** — **`timeline.csv` already carries it as FOUNDER CLAIM / Low** | Low | **U.001**, U.011, U.033 |
| 1962-08-18 → 1962-12-01 | **[SECTOR]** four Business Week items: cash-bind/shakeout forecast (Aug.18), "Discount store dropouts" (Oct.6), bankruptcy shake-out (Oct.27), "$6-billion industry … facing a major shakeout" (Dec.1) | S0112 index | contemporaneous | CONTEMPORARY OBSERVATION, index-level only | High (existence) / Medium (content) | U.035, U.037, U.039 |
| 1963-11-16 / 1964-05-16 | **[SECTOR]** "Fewer stores to share the pie" vs Nielsen "increase in the number of mass merchandisers" | S0114, S0115 | contemporaneous | CONTEMPORARY OBSERVATION | Medium | U.040 |
| 1964-11-14 / 1964-12-26 | **[SECTOR]** Woolworth into mass merchandising; "Worth Marts" named | S0115 | contemporaneous | CONTEMPORARY OBSERVATION | High | — |
| 1967-09-23 / 1968 | **[DECOY]** Business Week's "small town" and "Walton" entries resolve to a J.&L. Steel mill town (Hennepin, Illinois) and to three unrelated people named Walton | S0120, S0121 | contemporaneous | FACT (of the decoys) | High | U.042 |
| 1968-01-31 | **FY1968 year end** — the earliest year any document counts: 24 stores, $12,618,754, pre-tax $779,754, pro-forma net $481,754 | S0101, 1972-03-22 | 4 years, **no opinion** | FACT (rows) / pro-forma (basis) | Medium | U.102 |
| 1969-01-31 | FY1969 year end: 27 stores, $21,365,081; **tax year later targeted by the IRS proposals** | S0101 | 3 years | FACT + pro-forma | Medium | U.108 |
| **1969** | Company page: "The company officially incorporates as Wal-Mart Stores, Inc." — **year only; no month, no day, no state, no citation** | `sources/EXTRACT_corporate_walmart_history_timeline.md` (undated page, retrieved 2026-09-23); **the nine reports state no incorporation date and no state at all: "Delaware" occurs 0 times** | — | **UNKNOWN** for the event; Medium that the page says it | **Low/UNKNOWN** | **U.013, U.014** |
| 1969-10-01 | The date and state part 1's own header carried ("a Delaware corporation; incorporated 1969-10-01"), **retracted on the page** by §B.0 and §D-R03c | part 1 §B.0, §D.0 note D-R03c (`_parts/s1_p1.md`) | — | **REFUTED / UNSUPPORTED — not resurrected anywhere in this volume** | High (that no document supports it) | **U.014** |
| 1969-11 | "Present Bentonville general-office facility's initial portion … completed in November. 1969" | S0105 (1976) | 7 years | company assertion | High (as a 1976 statement) / Medium (the event) | — |
| 1970-01-01 | Fleet state at the boundary's edge: **18 Discount Cities + 14 Ben Franklin variety stores**, four states, "sales totaling $31 million", "less than a million square feet" | S0109 (1980-04-01); the 18-store figure inside S0101 (1972-03-22) | 2 years (S0101) / 10 years (S0109) | FACT (single lineage) | Medium-High | U.029 |
| **1970-02-01** | **Pooling of interests**: Walton Enterprises, Inc. transfers shares in "the various subsidiaries" plus related-business assets, subject to liabilities including the assumed **$968,876** bank note; paid-in capital of pooled companies at this date **$1,470,139** | S0101 Note 1, **1972-03-22** | 2 years, **audited note** | FACT | **High** | U.108; boundary: §C.0 RIVAL CLOSE |
| 1970-08-27 / 1970-09-03 | The NASDAQ-listing / first-trade cluster some secondary accounts use as the opening date | **NOT ON DISK AT ALL** | — | **UNTRIED — not asserted, not denied** | UNKNOWN | **U.216** |
| **1970-10-08** | **STAGE-1 CLOSE. 200,000 shares sold in the public offering**; excess of net proceeds over par **$3,010,467**; derived net **$15.15**/share; ≈**6.7%** of the pre-split base | S0101 capital note, 1972-03-22 — **the only day-precision public-capital date in the corpus** | 17 months | FACT (the note) / DERIVED (the per-share and float figures) | High (printed) / **Medium as a boundary** | **U.031**, U.210 |
| 1970-10 | Company page: "The first stock is sold at **$16.50 per share**" — no date, no size, no citation | corporate page extract, undated | — | RETROSPECTIVE company self-narrative | **Low**; **UNKNOWN at Tier 1** | **U.031** |
| 1970-12-31 | **[INDEPENDENT, NEGATIVE]** The SEC's complete register of exchange-traded issuers contains **no Wal-Mart entry** (WALGREEN … WALWORTH legible; 0 of 153,481 words) | `sources/gov_docs/SEC_SecuritiesTradedOnExchanges_asof-1970-12-31_…txt`, published 1971 | **contemporaneous** | FACT (of absence) / INFERENCE (that it witnesses listing status only) | **High** | U.112, U.044; `S0139` pending |
| 1971-01-31 | FY1971 year end: 38 stores, $44,286,012, pre-tax $3,170,599, pro-forma net $1,651,599, shares 6,000,000, equity $7,840,701 | S0101 (1972-03-22) | 1 year, **opinion names "the year then ended" = FY1972 only** | FACT (rows) | Medium-High | U.104 |
| 1971-06-11 | **Two-for-one split**, 1,500,000 shares, $150,000 par charge | S0101 capital note | 9 months | FACT | High | **U.015** |
| 1971-08-15 | DC doubled 60,000 → **124,800 sq ft** — *first organisational act dated after the boundary* | S0101 President's message | 7 months | FACT | High | out of window; U.027 |
| FY1971 | **Profit-sharing program adopted by the Board** for all regular employees | S0101 | ≤1 year | FACT | High | P62 |
| **1972-03-22** | **ATTESTATION FLOOR: the earliest document of any kind in this corpus that names the company.** President's message signed Sam M. Walton; stockholders approve authorised common of 11,000,000 | `WALMART_AR_1972.txt` (S0101) | 0 | FACT | **High** | **U.101** |

### Q.2 Post-boundary spine, compressed (Stage-2 material; listed so the boundary is visible, not so it is argued)

1972-04-05 second two-for-one · 1972-04 follow-on offering (400,000 at $23.75; +$8,913,504 paid-in) ·
**1972-08-25 NYSE listing (venue change, not a stock event)** · 1972-12-03 open house on the 261,800 / 263,800
sq ft GO+DC (U.028) · FY1973 64 stores, three units lost to fire/tornado, first consolidated federal return ·
1974-04-05 first evidenced dividend payment $.025 · FY1974 78 stores, two Ben Franklins sold and four closed ·
**1975-01-06 second DC in operation** · **1975-01-31 LIFO adopted, −$2,347,000, auditor-flagged by exception** ·
1975-05 $15,000,000 convertible subordinated debentures · **1975-08-19 third two-for-one (+6,687,789 shares)** ·
1975-11-11 Mount Pleasant, Texas → "nine-state region" · FY1976 125 stores, first total square footage
5,295,000, IBM 370/135 leased, Singer registers in 64 stores / NCR in 61, Audit Committee constituted ·
1976-11 third DC → 300,000 sq ft pure DC · FY1977 153 stores, ≈550,000 sq ft distribution, ~80% penetration ·
1977 Searcy DC begun · **1977-10-01 a sixteen-store group acquired, four stores closed** · 1978-10-01 Hutcheson
Wholesale Shoe acquired · FY1979 229 stores, SFAS-13 restatement of FY1975–FY1978 (−$769,000 stated /
−$695,000 computed, U.021), remaining Sav-Co closed · 1979 Pine Bluff "Project '79 … planned, not as a
prototype, but to be an experiment" · 1980-01 mechanised 390,000 sq ft Bentonville warehouse · FY1980 276
stores, $1,248,176k, 12,600,000 sq ft, >21,000 associates.

### Q.3 [RESEARCH-STATE] rows — the retrieval events that made this timeline possible

| Date | Event | Evidence | Class | Anchor |
|---|---|---|---|---|
| 2026-09-23 | The chronology probe reads the EDGAR submission JSONs and the corporate pages; concludes the Tier-1 floor for 1962–1970 is "nearly bare" — a verdict later **falsified** by a document class it never queried | `research/A_chronology_feasibility.md` §Verdict + its own SUPERSEDED note (2026-09-24) | LEAD / superseded | U.101 |
| 2026-09-24 | **The five interior-year reports (FY1974, FY1975, FY1977, FY1978, FY1979) are fetched**; each carries a provenance header with byte-match and SHA-256 | `sources/periodicals/IA_A2_interior_years_fetch_evidence_20260924.json` (S0110) | METHOD ARTEFACT — the CONTEMPORANEOUS / NOT-RECOVERABLE claims about text layers rest **on these headers, not on the registrant** | — |
| 2026-09-25 | A4 re-walks 13 Business Week index volumes and 8 *Stores* apparatuses whole; 0 company namings; **10 of 10 requests spent** re-probing HathiTrust and Google Books after the harvester's repair | S0112–S0138; `REQUEST_LEDGER.tsv` (S0136) | FACT (route state) | **U.043** |
| 2026-09-25/26 | **A5 reads two SEC documents whole** (47,206 B and 941,197 B): both print the company **zero** times; HathiTrust's page text proves script-unreachable (403 twice) while its search answers 200 | A5-03, A5-04; pending `S0139`/`S0140`/`S0141` | FACT (negative) + route state | **U.044**, U.201, U.207 |
| 2026-09-25 → present | Mining agent works the **held-but-unread** corpus: the on-disk IA/LOC/GB JSONs, the Chronicling America 403 round, the FY1972 direct-server text layer, and the corporate_print pre-1972 naming nulls | `research/A6_held_corpus_mine.md` (live, growing during this pass) | IN FLIGHT | **U.202, U.206** |
| 2026-09-26 | This volume mints the **canonical §U anchor set** and maps every dossier-local and part-local key onto it | `_parts/s1_p3.md` §U.0 | METHOD — single addressable set for the merge | §U.0 |

---

## R. END-OF-STAGE STRUCTURED SNAPSHOT (at 1970-10-08)

STATUS: WRITTEN 2026-09-26

| Variable | Value | Source | Confidence |
|---|---|---|---|
| **The date itself** | **1970-10-08** — the only end-of-window candidate dated to the day inside an audited note. Adopted as a **capital** boundary, and the row states the weakness: a 1972 document reporting a 1970 event, in the same lineage as everything else positive about the company | S0101 capital note; part 1 §B-2, §C.0 | High / **Medium as a boundary** |
| **Legal person** | **Wal-Mart Stores, Inc.**, issuer of the stock sold; consolidated group **20 months old** (from the 1970-02-01 pooling). **State of incorporation: UNKNOWN — stated by no document; "Delaware" occurs 0 times across the nine reports.** Predecessor subsidiaries: **not named** ("the various subsidiaries"). Principal shareholder: **Walton Enterprises, Inc.**, form of organisation and stake **unstated** | S0101 Notes 1 and 6; part 1 §B.0; **U.013, U.014, U.108** | High (registrant) / **UNKNOWN (state, subsidiaries, sizes)** |
| **Number of legal persons actually doing business** | **More than one, on the tax evidence**: through FY1972 "The Company and its subsidiaries file separate income tax returns", the provision being the combined amounts payable by **the individual corporations**; a consolidated federal return was filed only for the year ended 1973-01-31 | S0101 Note 6; S0102 Note 6 | High. **INFERENCE, Medium:** this proves multiple persons in 1972; it does **not** identify which ran the 1962 store |
| **Fleet** | **32 stores at FY1970-01-31** (RESTAT in S0101); composition at 1970-01-01 = **18 Wal-Mart Discount Cities + 14 Ben Franklin variety stores**; **38 by FY1971-01-31**. Banner mix: **43.8% of units still carried another firm's name at the boundary** — DERIVED 14 ÷ 32 | S0101; S0102; S0107; S0109; §P rows P12, P54, P55 | Medium-High; **one lineage** |
| **Sales** | **FY1970 $30,862,659** (RESTAT in S0101; the FY1980 narrative rounds it to "$31 million"); FY1969 $21,365,081; FY1968 $12,618,754; **FY1962–FY1967 EMPTY** | §P rows P02, P06, P08 | Medium; **U.102** |
| **Earnings basis at the boundary** | **Pro forma, and un-audited.** FY1968–FY1971 net income is captioned "Pro forma net income" by the registrant; **no opinion on disk attaches to any year before FY1972**; FY1970 net income carries a live second value in the FY1978 table (1,011 / implied 1,239 vs register $1,187,764) | S0101; S0107; A3 §6.1; **U.017** | High (the labels) / Low (the FY1970 cell) |
| **Balance sheet at the boundary** | FY1970: total assets **$8,493 thousand**, equity **$3,159 thousand**, current ratio 1.7, LTD 1,328 — **first stated anywhere in a 1978 document** (nine-year table); FY1971: 15,331 / 7,841 / 1.9. **Pre-SFAS-13 basis: leases largely off balance sheet** | S0107 (RESTAT); S0101; A3 Table S4 | High (as printed) / **Medium as 1970 state** |
| **Capital structure** | **6,000,000 shares outstanding**, par **$.10**; 200,000 (≈6.7% of the pre-split base, DERIVED) sold publicly; net proceeds **$3,030,467** (derived total) / **$3,010,467** over par; **no gross price on any Tier-1 document** | S0101; §P rows P43–P46 | High (rows) / Medium (derived shares of the total) |
| **Market status** | **Over-the-counter from October 1970**; not NYSE until 1972-08-25. **Independently corroborated — once, and only as a negative**: the SEC's 31-Dec-1970 exchange-issuer register omits the company | S0103; S0108; `sources/gov_docs/…1970-12-31…txt` (`S0139` pending) | High; **the only datum in §R with a non-registrant origin, and it corroborates no figure** |
| **Premises and logistics** | General office at Bentonville (initial portion of the present facility completed **1969-11**); distribution capacity **60,000 sq ft → 124,800 sq ft on 1971-08-15 (7 months after the boundary, already planned)**; ~55% of merchandise moving through the company's own DC/warehouse in FY1974 | S0105 (1976 statement of 1969); S0101; S0104 | High (S0101 rows) / Medium (1969, from a 1976 sentence) |
| **People** | FY1968–FY1971 headcount **UNKNOWN** (never printed); the earliest headcount anywhere in the corpus is FY1972's "some 2,300" in a signed letter | S0101; **U.114** | **EMPTY within perimeter**, not zero |
| **Ownership concentration** | **No document states any holder's percentage.** The only ownership sentence in the corpus is the uncited page's "The Walton family owns 24 stores" — whose "1967" label is **FY1968** as filed | `EXTRACT_corporate_walmart_history_timeline.md`; part 1 §B.2 | **UNKNOWN (percentages)**; High (that a Walton-side vehicle was principal shareholder) |
| **Trading-area rule in force** | Post-boundary statements describe the policy that governed this fleet: a **350-mile radius of Bentonville**, towns averaging 10,000–15,000 (FY1975) / 5,000–25,000 (FY1978, FY1980). **Neither rule is stated in any document dated 1970** | S0104; S0107; S0109 | Medium (self-characterisation, later-dated); **U.034** |
| **Competition as the company filed it** | **No firm-level rival is named in any of the nine reports**; competition appears as category-level statements. Independent 1970 evidence places the boundary between two publicly-linked trades: Business Week indexes S. S. Kresge under **VARIETY Stores** as well as DISCOUNT Houses in the company's float year | S0101–S0109 negative search; S0123; part 2 §I | High (that the print is silent on rivals); High (the Kresge taxonomy datum) |
| **Regulatory / tax exposure** | IRS proposed additional assessments for the years ended **1969-01-31** and **1970-01-31** (surtax exemptions, inter-subsidiary reallocation), extended in the FY1973 report; **outcome UNKNOWN** | S0101 Note 6; S0102 Note 6; **U.108** | High |
| **Technology at the boundary** | **UNKNOWN from any in-window document.** The corpus's earliest computer statement is FY1976's leased **IBM 370/135**, and the retrospective "first computer 1968/69" claim rests on a **museum page modified in 2026 with no in-window witness** | S0105; `sources/periodicals/walmart_museum_page.html` (`S0142` pending); part 2 §J | **UNKNOWN** for 1970; High (that the retrospective claim is uncited) |
| **What the company said about itself on that date** | **Nothing in this corpus.** There is no 1970-dated company document of any kind on disk; the first is 1972-03-22 | nine-file enumeration; **U.101** | High — **this is the load-bearing limitation of Stage 1** |
| **State of the archive at the boundary** | Documents on disk **dated on or before 1970-10-08 that name the company: 0**. Dated third-party documents inside 1945–1968 that do **not** name it: the *Stores* monthly run 1945–1961 (205 items with text layers) and the Business Week indexes 1962–1968 | part 1 §A.2 precision note; S0112–S0133 | **High** |
| **Stage boundary as it must be read** | **A capital boundary, not a business-model boundary.** The fleet still carried two banners at the close, the second format (Family Center / Sav-Co) was still 5 years away, and the variety units were phased out only across the 1970s | S0103, S0104, S0108, S0109; part 1 §B.2 last row | High |

## S. DATA GAPS

STATUS: WRITTEN 2026-09-26

### S.0 The three states, and what this section may not do

**EMPTY** = searched, the record is silent, **within a stated perimeter**. **UNANSWERED** = a route exists, it
was reached, and it refused an application-layer reply (403 / 429 / 500 / 504 / TLS failure) — a statement
about **this environment**, never about Walmart. **UNTRIED** = the retrieval was never attempted, recorded so
the next pass neither re-burns it nor mistakes it for a null (§14 rule 6). Three prohibitions bind every row:
**no UNANSWERED or UNTRIED row may be written as a null**; **no gap may be closed by a plausible substitute**
(a sector figure is not a company figure; a memoir is not a witness); and **every High-importance gap carries
a `follow_up_task`, because a High gap without one is an open research-debt violation (§13), not a finished
section.**

**Register-set note (R-3).** `data_gaps.csv`, `decisions.csv`, `failures.csv`, `validation.csv` and
`channels.csv` **do not exist** for this company; the register set on disk is four files
(`conflicts.csv`, `quantitative.csv`, `sources.csv`, `timeline.csv`). §15.2 requires `data_gaps.csv` at every
tier, so §S.1 below is drafted in its exact column order for file creation by the merge — **and it is a
request, not an edit**: this volume writes no CSV.

### S.1 Gap register (columns exactly as `data_gaps.csv`)

| gap | why_missing | importance | best_available_evidence | confidence | follow_up_task | Anchor |
|---|---|---|---|---|---|---|
| **Any document naming the company before 1972-03-22** | The corpus contains **none**. Nine printed reports start FY1972; EDGAR's electronic history starts 1994-02-14; web archives start 1996-12-29; the whole periodical family returned **zero** namings across 13 BW index volumes, 8 *Stores* apparatuses and 2 SEC government documents | **High** | The absence is itself the evidence, and it is measured: S0112–S0136, A5-03/A5-04, nine-file enumeration | **High** (that the corpus is silent) — **NOT** a null about the world | **RUN THE HELD-BUT-UNREAD ROUTES** (mining agent in flight): the on-disk `sources/periodicals/ia_arkgaz.json`, `ia_satpost.json`, `ia_supermerch.json`, `ca_01_waltons_five.json`, `gb_01_waltons_five_and_dime.json` have never been mined; the HathiTrust 573-record 1970s pool and the NLRB/FAA registers are identified but unread | **U.101**, U.202, U.207, U.208 |
| **FY1962–FY1967: sales, stores, earnings, balance sheet, square footage, headcount — every variable** | Empty in all nine reports, and **not restatable from them**: S0103's five-year table starts FY1970 and S0107's nine-year table starts FY1970 | **High** | FY1968 is the floor ($12,618,754, 24 stores, pro forma) | **High** (EMPTY within the nine-report perimeter) | the FY1970/FY1971 reports (proven absent from IA by `ia_q_92a4542e.json`, numFound 0, but **that host is not the corpus**): try Hoover's, WorldCat/LOC holdings, SEC Reference Room paper; and a **non-company contemporaneous count** (Chain Store Age directory 1963–1970) | **U.102**, U.210, U.213 |
| **FY1968–FY1969 cost of sales, expense rows, balance sheet, shares, headcount, square footage** | The FY1972 five-year table carries only sales / pre-tax / pro-forma income / EPS / stores | Medium-High | §P rows P02–P07, P05, P07 | High (EMPTY in perimeter) | FY1969/FY1970 reports; county assessor and chain directories | U.102 |
| **The 1970 offering's terms as filed** — gross price, proceeds line, underwriter, registration-statement text | The note gives the accounting effect only. **$16.50 exists solely on an uncited company page; the derived net $15.15 has no licensed bridge to it** | **High** | S0101 capital note; §P rows P43–P46 | High (the note) / **UNKNOWN** (the price) | **FETCH REQUEST:** the 1970 registration statement — EDGAR full-text and the SEC Reference Room / National Archives (never queried by any pass of this project) | **U.031**, U.210 |
| **Which legal persons did what, 1945–1970** — predecessor subsidiaries' names, dates, states; what Walton Enterprises, Inc. was; which of the fifteen stores entered the pool | The reports say "the various subsidiaries" and never enumerate them; the 1969 claim is year-only and uncited; **"Delaware" occurs 0 times in all nine reports** | **High** | S0101 Note 1 and Note 6 (separate returns ⇒ multiple persons); part 1 §B.0 | High (that the record is silent); **UNKNOWN** (the entities) | **LOCAL FIRST:** `sources/probe_SEC_tickers.json` + the two EDGAR submission JSONs carry a `formerNames` field — an EDGAR **former-name / state-of-incorporation** search is the shortest remaining path and is **in flight with the mining agent**; then Arkansas SoS and Benton / Mississippi County records | **U.013, U.014, U.108**, U.203, U.211 |
| **The 1945 and 1946 events themselves** — franchise agreement, lease, deed, partnership instrument, firm name | Six dated company restatements (FY1973→FY1980) attest *the telling*; nothing attests *the told* | **High** | S0102–S0109; `timeline.csv` 1945 row (FOUNDER CLAIM/Low) | **Low** | Mississippi County, **Arkansas** records and Newport *Daily Sun* — note the fleet brief aimed at Nebraska was an artefact of an internal error (**U.011**); Chronicling America queries to date have searched "waltons newport **mo**", the wrong state | **U.110**, U.206, U.211 |
| **The 1962 opening's observable facts** — opening day, takings, prices, floor area, crowd, stock | No 1962 press item in hand names the firm; the flyer image has never been read; the "6,000 sq ft / 45,000 items / $1,402" folklore returns **zero** hits across the nine reports | **High** | S0103 (first to date 1962, 1974-03-21); S0109 names J. L. Walton as co-operator | **Low / UNTRACEABLE**; the "$1,402" claim has **no pre-1992 source anywhere in this corpus** | read the catalogued 1962 "First Walmart Advertisement" image (the museum entry is on disk; **A2 W-77 records the image path but says it has never been read**); Arkansas/Missouri local print | **U.001, U.110, U.033**, U.214 |
| **Total store square footage before FY1976; headcount for FY1973, FY1976, FY1978; any market price before FY1975; any comparable-store figure except FY1978** | The reports print additions only, one employee chart is OCR-damaged, FY1978's figure was not found this pass, price tables begin in the FY1976 report, and only one same-store sentence exists | Medium | §P rows P56–P59, P53, P38 | High (EMPTY within the nine files) | **page-image re-walk** of the FY1976 employee chart and the FY1978 profile pages (`_text.pdf` leads are declared in each file's own metadata; `S0111`); Management's Analysis pages of FY1979/FY1980 | **U.105, U.106, U.107, U.114**, U.205, U.206, U.217 |
| **FY1975's printed top line** ($226,209 vs $236,209) and the FY1970 net-income cell and the FY1973 share count | All three are **machine failures on the text layer, not company errors**: the FY1975 own-column numerals dropped everywhere in that file; the FY1978 table's cell is internally inconsistent; the FY1973 count differs by 400 shares between two prints and one document prints both | Medium-High (each is a live conflict, none is immaterial to a register row) | §P rows P27, P10, P22; A3-023's inversion arithmetic | Medium-High / Medium / Medium | **one cheap fetch settles all three**: the declared page-image PDFs (`_text.pdf`, 3,243,815 B / 3,706,555 B for FY1974-FY1975) — **FETCH REQUEST, in flight** | **U.016, U.017, U.018**, U.205, U.206 |
| **Whether the trade press's silence is informative** | Only 7 of ~200 *Stores* monthly issues and 5 subject-only annual indexes have been read; the genre that would actually name a member store — an **NRDGA/NRMA membership roster or chain directory** — is absent from this corpus | **High** | S0125–S0133; A4-18, A4-29, A4-40; §P rows P79 | Medium | a **designed sample of ~10** roster-bearing issues (convention and membership numbers), not a sweep; plus the roster question itself | **U.111, U.113**, U.212 |
| **Whether any competitor or third party ever counted Wal-Mart's stores before 1972** — A3 §7.2(d)'s named missing witness | *Chain Store Age*'s annual "Directory of Chain Stores" is the exact instrument and sits behind the blocked Google Books route; D&B / Hoover's firm reports were never reached | **High** | A3 §7.2(d); A2/A4 route logs | **UNKNOWN** | **FETCH REQUEST** (off-environment or keyed): Chain Store Age 1963–1970; *Discount Store News* / *Discount Merchandising* 1962–1970; D&B discount volumes; AUDITS & Surveys; the Cornell discount-chain study the company itself cites in FY1973 (S0102 W-38, never located) | **U.113**, U.213 |
| **What the founder decided and why** — every rationale in §N | No document before March 1972 records a choice; the 1992 memoir's bytes are not in this repository and it is **not admitted as evidence** | **High** | part 1 §B.1; §N.1's eight rows, all with `Rationale: NOT STATED` | **UNKNOWN** — **and this is a finding, not a failure of search**: it is the record-selection null (§2) | memoir as a text (library interprint, not this machine); internal-corporate papers at a repository; U.219 | **U.109, U.110**, U.219 |
| **The 1970-08-27 / 1970-09-03 first-trade cluster** used by some accounts as the opening of Stage 2 | **Not on disk at all**; part 1 §C.0 records the rejected candidate as UNKNOWN | Medium | part 1 boundary table | **UNKNOWN**, and **not asserted** | an exchange- or quotation-record fetch (outside Stage 1's evidence classes so far); the 1972/1978 SEC issuer registers would at least date the *listing* leg | U.201, U.216 |
| **Whether the annual-report genre simply had no place for a founding rationale** — the one alternative explanation for §C's central silence | Untestable on a corpus whose only company documents **are** annual reports | Medium | part 1 §C.1 coda | **UNKNOWN** | read a **different company's** 1950s–60s printed reports as a control (genre test, non-Walmart); or the company's own non-report print (stockholder letters, newsletters, meeting transcripts) | **U.222** |

### S.2 The untried lists are carried forward, in full, as named routes

Every UNTRIED and UNANSWERED item named anywhere in this company's research files is carried into **§U's
U.2xx block** and detailed in the final section of this volume, with its owning agent marked. Nothing is
dropped silently: **A §D.4.1–§D.4.6 (part 1, six queries) · B §Queries-that-returned-null-or-errored and
§Paywalled/on-paper leads · A2 §Evidence-family status · A3 §UNTRIED table · A4 §UNTRIED (7 bullets) ·
A5 X-A5/1…X-A5/6 · A6 (in flight)**. The mapped route ids are **U.201–U.222**.

### S.3 Record-selection null, stated for §S (§2)

Unrecoverable *because the survivor's archive is the one that was kept*: no 1945–1962 internal deliberation;
no rejected option; no contemporaneous price or sales record from inside any store before FY1968; no
independent count behind any company self-report; no contemporaneous third-party witness to any decision; and
**no document of any kind — company, trade, government or press — that names this company before 1972-03-22**.
What the archive *is* rich in is the post-float decade, which is why §A–§R read as they do, and why the depth
verdict is bifurcated (A3 §7.2) rather than averaged: **`DEPTH-CORE (single-lineage)` for FY1972–FY1980,
`PROVISIONAL — NOT CORE` for FY1962–FY1971 and the whole origin layer, and company-level `PROVISIONAL`**
because §14 rule 6's four families return one positive (corporate print), one partial (a museum catalogue
entry), one UNANSWERED (the periodical family, now partly re-opened and still unread) and one never properly
tried (auction/documentary).

### S.4 What §S does NOT claim

It does not claim the company was unmentioned in print before 1972, that the trade ignored it, that no 1970
prospectus exists, that the FY1975 top line is finally settled at $236,209, that no 1945 document survives, or
that the missing FY1970/FY1971 reports are lost. **Each of those would convert a perimeter-bound EMPTY, an
UNANSWERED route or an UNTRIED act into a null about the past, and the volume's central finding does not need
the help.**

---

## T. SOURCE / PROVENANCE TABLE

STATUS: WRITTEN 2026-09-26

### T.1 Provenance of every document class §§M–§U rest on

Line format per §7: `| Source | Type | Primary/Secondary | Event date | Publication date | URL | Tier | Confidence |`. Register ids are the issued ones; **ids not yet in `sources.csv` are written backticked** so the `keys` gate measures citation fidelity rather than merge order.

| Source | Type | Primary/Secondary | Event date | Publication date | URL | Tier | Confidence |
|---|---|---|---|---|---|---|---|
| `sources/periodicals/WALMART_AR_1972.txt` — **S0101** (FY1972 report: the pooling note, the capital note dating 1970-10-08, the five-year table, the signed President's message) | printed registrant annual report | Primary | 1972-01-31 | **1972-03-22 — the attestation floor of this corpus** | https://archive.org/details/1972-annual-report-for-walmart-stores-inc | 1 | High (as-filed); **Medium** for the 1970 event it reports |
| `WALMART_AR_1973.txt`–`WALMART_AR_1980.txt` — **S0102–S0109** (eight further reports; eight dated Arthur Young opinions; the FY1975 qualification; the FY1979 SFAS-13 clause; the FY1980 retrospective essay and its refuted dividend row) | printed registrant annual reports | Primary | 1973-01-31 … 1980-01-31 | 1973-03-20 … 1980-04-01 | same detail pattern, `_1973` … `_1980` | 1 | High (as-filed years) |
| `sources/periodicals/IA_A2_interior_years_fetch_evidence_20260924.json` + the PROVENANCE HEADER atop each report file — **S0110** | retrieval provenance register (this project's own) | Secondary | 2026-09-24 | 2026-09-24 | local | n/a (METHOD ARTEFACT) | High — **every CONTEMPORANEOUS / NOT-RECOVERABLE claim about a text layer rests on these headers, not on the registrant** |
| Declared **page images** of FY1974/FY1975/FY1977/FY1978/FY1979 (`_djvu.xml` page map 448,062 B; `_text.pdf` 3,243,815 B and 3,706,555 B) — **S0111**, metadata-declared, **bytes NOT retrieved** | page-image lead | Primary if fetched | 1975-03-28 etc. | 1974–1979 | https://archive.org/details/1975-annual-report-for-walmart-stores-inc | 1 | **LEAD / UNTRIED — the highest-value untried act in the dossier, and cheap: U.205, U.206** |
| Business Week annual indexes 1962–1971 (13 half-and-full volumes) — **S0112–S0124**, with the bounded extract `sources/periodicals/BUSINESSWEEK_INDEX_1962-1971_EXTRACT_walmart_and_sector_hits.txt` | printed periodical index / finding aid | Primary (as to what the index carried) | 1962-01-01 … 1971-12-31 | 1963 … 1972 | `https://ia802906.us.archive.org/14/items/sim_business-week_1962_index/…_djvu.txt` etc. | 2 | High (existence, byte-exactness, zeros); **Medium/UNKNOWN as to article content — no issue text is reachable** |
| *Stores* (NRDGA→NRMA) monthlies 1946–1961 and annual indexes 1970–1975 — **S0125–S0133**, extract `STORES_NRDGA_1946-1972_EXTRACT_walton_and_discount.txt` | printed trade journal / index | Primary | 1946-06 … 1975 | 1946 … 1975 | `https://archive.org/metadata/sim_stores_1958-06_40_6` → server+dir route | 3 | High (the December 1961 seminar issue, in-window and closest dated document to the founding moment); **Medium (1946 layer is the worst OCR in the run)**; the annual indexes are **subject-only — a weak instrument and reported as weak** |
| A4's two bounded extracts and its request ledger — **S0134, S0136** (47-row ledger: 46 HTTP 200, 1 read-timeout at 0 B, 10,035,277 B across 18 hosts) | derived extract + retrieval log | Secondary | 1945–1975 / 2026-09-25 | 2026-09-25 | in-repo `sources/periodicals/` | — (TRANSCRIPT / PROVENANCE) | High — **derived, not an independent lineage** |
| `sources/gov_docs/SEC_SecuritiesTradedOnExchanges_asof-1970-12-31_IA-securitiestraded1970unit.txt` (941,197 B, 153,481 words read whole) — **`S0139` (pending)** | government publication, complete issuer register | Primary **as to listing status only** | 1970-12-31 | 1971 | https://archive.org/download/securitiestraded1970unit/securitiestraded1970unit_djvu.txt | 1 | **High — the only non-registrant origin in Stage 1, and it is a negative**; its front matter bounds its universe to exchange-admitted securities, so it **cannot witness Securities Act registration or OTC status** |
| SEC *Statistical bulletin* November 1970 (47,206 B, whole) — **`S0140` (pending)** | government statistical series | Primary as to that publication's structure | 1970-11 | 1970-11 | `https://dn760102.eu.archive.org/0/items/sim_sec-monthly-statistical-review_1970-11_29_11/…` | 1 | High — **and structurally unable to name the company: its only issuer-naming table is a fixed sample of "100 SELECTED COMMON STOCKS" on the NYSE. Even a positive would have evidenced registration, not the firm** |
| HathiTrust / Google Books route probes — **`S0137`, `S0138` (issued), `S0141`-as-HathiTrust-probe (pending, see U.048)** | search-index and catalogue metadata | Secondary | 1970–1979 / 2026-09-25 | 2026-09-25 | `https://babel.hathitrust.org/cgi/ls?field1=ocr;q1=%22Wal-Mart%22;…` | n/a | High (route state) / **zero evidentiary value about the company: NO item text read** |
| `sources/EXTRACT_corporate_walmart_history_timeline.md` — the company's own undated curated page (**`S0141`-as-timeline in p2's block; see U.048**) | company self-narrative web page | Secondary | 1962-07-02 … 1972 | undated page, retrieved 2026-09-23 | https://corporate.walmart.com/about/history | 1 as artifact / **Tier-4-equivalent as evidence** | Medium (that the page says it); **Low/UNKNOWN for every event it asserts** — **zero citations on the page; the same corporate record as the reports, so ONE source; its silence about pre-1962 is itself a finding (U.115)** |
| `sources/EXTRACT_pbs_2004_timeline.md` (2004-08-20) and `sources/EXTRACT_scdigest_2012_timeline.md` | third-party retrospective summaries | Secondary | 1945–1970s | 2004-08-20 / 2012 | as held | 3–4 | Low — **retrospective only; used solely to show that the 1970-DC folklore is unsupported (U.027), never as a fact about 1970** |
| `sources/periodicals/walmart_museum_page.html` (**`S0142` pending**) | museum catalogue page | Secondary; the catalogued artifact is Tier 1 | 1962; 1950 (claimed) | page `dc:modifyDate` 2026-04-24 | https://corporate.walmart.com/about/walmart-museum | **tier split on one document**: artifact 1 / curation prose 3 | High (that a 1962 advertisement is catalogued); **Low (the computing and lease sentences)**; the 1950 bill of sale has **no bytes in this repository** |
| `sources/periodicals/STUB_LEAD_samwaltoninsides00vanc.md`, `STUB_LEAD_DTIC_ADA345567.md`, `sources/periodicals/ia_anywalmart.json`, `ia_chain_store_age.json`, `ca_01_probe.json`, the five `*.bin` probes | **enumerated, not mined** | — | — | — | local | — | **UNTRIED / UNANSWERED as the case may be — see U.202 and the final section. Three of the JSONs are error or challenge bodies and are therefore UNANSWERED, never nulls** |
| `sources/EDGAR_submissions_CIK0000104169.json`, `…_002_1994-2012.json`, `probe_EDGAR_submissions_001/002/current.json`, `probe_SEC_tickers.json` | regulatory metadata (1,409 filings) | Primary (as to what EDGAR holds) | 1994-02-14 → 2012 | — | EDGAR | 1 | High — **proves the EDGAR floor, not the 1970 filing**; the three `probe_EDGAR_*` files are **S3 `NoSuchKey` XML error bodies = UNANSWERED**, and `formerNames` is present in the tickers file → **U.203** |
| `research/A6_held_corpus_mine.md` (live during this pass) | holdings census by the mining agent | Secondary (this project) | 2026-09-25/26 | 2026-09-26 | local | — | High (as a census) — **cited here as in-flight; its §§"Pre-1972 name evidence", "A5 re-test" and "Records for merge" were still PENDING when this volume was written, and its census table was growing between two reads 20 minutes apart** |

### T.2 The lineage ledger — the arithmetic behind "one voice"

| Lineage | Documents in it | Independent origins it can supply | Effect |
|---|---|---|---|
| **L1 — the registrant and its auditor** | S0101–S0109 + Arthur Young's eight dated opinions + the corporate page + the museum page (same corporate record) | **1** | **Every positive statement about this company inside Stage 1 traces here.** Nine prints of FY1974 = one witness. Confidence caps at what a single document supports |
| **L2 — Business Week indexes** | S0112–S0124 | **1 (independent publisher, contemporaneous)** — but it names no one | Corroborates **no company figure**; supplies the sector and decoy record (§H part 2, §M.2) |
| **L3 — *Stores* / NRMA** | S0125–S0133 | **1** | Same: market-state and the 1961 counterfactual; **no company datum** |
| **L4 — SEC publications** | `S0139` register, `S0140` bulletin | **1, negative only** (A5-04). The bulletin is **NOT independent in the useful sense** — it republishes registrant aggregates | Supplies exactly one corroborated company fact: **not exchange-listed at 1970-12-31** |
| **L5 — this project's retrieval artifacts** | S0110, S0134, S0136, `S0141`, the `.bin`/`.json` probes | method evidence only | Governs what "read", "byte-exact", "UNANSWERED" mean in §§M–§U |

### T.3 Register-hygiene findings this volume must report rather than fix (R-1, R-2, R-3)

* **R-1 — a live `source_id` collision between two volumes of this same part-set (U.048).** `s1_p2.md`'s merge
  block issues **`S0139` = the SEC register, `S0140` = the November 1970 bulletin, `S0141` = the corporate
  timeline page, `S0142` = the museum page**. A5's pending block issues **`S0139` = the SEC register, `S0140` =
  the bulletin, `S0141` = the HathiTrust route probe**. `S0139` and `S0140` agree; **`S0141` names two different
  documents.** Per
  §13 ("`source_id` blocks are assigned centrally at merge, never per dossier"), this volume **does not
  renumber**; it reports that the merge must treat **one id per document** and re-issue the HathiTrust probe
  and any colliding page row under fresh central ids, then re-point both volumes' prose. The §14 rule-7
  recovery applies: **declare one register canonical, alias the duplicates, keep both passes' genuine content,
  hand the de-duplication to the merge as an explicit outbound correction.**
* **R-2 — A3's and A4's U-A3/n and U-A4/n keys are already IN `conflicts.csv`, A5's is not.** §U.0 therefore
  maps them to canonical `U.nnn` anchors **for renumbering only**, and does not re-issue their content, so the
  merge cannot create duplicates. A5's U-A5/1, A2's ten U-A2/n, the probe's U-1/U-2/U-3, B's U-W-4/U-W-5 and
  this part-set's U-C0/1, U-E/1, U-F/1, U-K/1 receive new rows.
* **R-3 — five of the eight §13 registers do not exist** for this company (see §S.0).

## U. CONFLICTING EVIDENCE, DOCUMENTED NULLS AND UNTRIED ROUTES — THE CANONICAL ANCHOR SET

STATUS: WRITTEN 2026-09-26

### U.0 How these anchors are minted, and why this volume has to mint them

**The problem §U solves.** Walmart's Stage-1 dossiers and its two earlier volumes keyed conflicts to
*dossier-local* and *part-local* ids — `U-A2/1`…`U-A2/10`, `U-A3/1`…`U-A3/9`, `U-A4/1`…`U-A4/9`,
`U-A5/1`, the probe's `U-1`/`U-2`/`U-3`, the retest's `U-W-4`/`U-W-5`, part 1's `U-C0/1`, and part 2's
`U-E/1`/`U-F/1`/`U-K/1` — and `conflicts.csv` already carries **eighteen** rows under the `U-A3/n` and
`U-A4/n` spellings. Method §13 is explicit that local ids are dossier-local and that **the register is the
only place global uniqueness lives**, because applying two dossiers' id-blocks in sequence produced 22 ids
each naming three different documents on another company. So this volume does three things and nothing else:
(1) it mints a **continuous canonical set `U.nnn`**; (2) it **maps every local key ever used** onto it, so the
merge has a single addressable set; (3) it **does not re-adjudicate** what a dossier already adjudicated — the
`U-A3/n` and `U-A4/n` rows in the register keep their own reasoning and are renumbered, not rewritten.

**Minting rules.** `U.001`–`U.099` live conflicts (two incompatible claims about one variable).
`U.100`–`U.199` **documented nulls** (EMPTY within a stated perimeter — a finding, not a search failure).
`U.200`–`U.299` **UNANSWERED and UNTRIED routes** (a route refused, or a route nobody walked). Numbers are
**never re-used, never re-ordered to look tidy**, and gaps inside a block are reserved for the merge's own
additions. An anchor is minted **only** where a conflict, null or route exists in a document on disk: nothing
here is speculative, so nothing here can be silently dropped later.

**U.0.1 The mapping table — every local key, its canonical anchor, and its register state**

| Local key (as used) | Where it was minted | Canonical anchor | Subject | Register state at merge time |
|---|---|---|---|---|
| `U-C0/1` | `s1_p1.md` §C.0 | **U.001** | 1962 opening month: November (registrant print) vs 2 July (company page) | **duplicate of part 2's `U-E/1` — the merge issues ONE row, at U.001** |
| `U-E/1` | `s1_p2.md` §E.4, drafted row in its merge block | **U.001** | same | row drafted by part 2 → renumber to U.001, **do not add a second row** |
| (A2's 1962 row) | `timeline.csv` 1962-11 row, conflict_ref `U-A3/8` | **U.001 / U.012** | mis-pointed: U-A3/8 is the **population** conflict, not the month | **outbound correction: the timeline row's `conflict_ref` must become `U.001` (month) and `U.012` where population is meant** |
| `U-A3/8` | `A3` §Contradictions; in `conflicts.csv` | **U.012** | Rogers population "approximately 4700" (FY1975) vs "approximately 5,000" (FY1978) | **row exists — renumber only** |
| `U-3` (probe), `U-W-4` (retest), `U-A2/7` (A2) | `A_chronology_feasibility.md` §Conflicts; `B_periodical_retest.md`; `A2` §Contradictions | **U.011** | Newport = **Arkansas** vs Nebraska (an internal "correction") vs Kentucky (A4 prose) vs Missouri (a brief) | part 2 drafted `U-A2/7` → **one row at U.011**; the probe's `U-3` and the retest's `U-W-4` are **aliases, not separate conflicts** |
| `U-1` (probe), `U-A2/8` (A2) | probe §Conflicts; A2 §Contradictions | **U.013** | which founding the records support: 1962 lore / 1969 page / 1970-02-01 pooling | **no register row from either dossier → REQUESTED in §U.1 and in the merge block** |
| (part 1 §B.0, §D-R03c) | `s1_p1.md` header, §B.0, §D.0 | **U.014** | "Delaware corporation, incorporated 1969-10-01" vs **zero** occurrences of "Delaware" in all nine reports and a year-only, uncited 1969 | **NEW — requested. The claim is retracted, not resurrected** |
| `D-R09` + correction `D-R09c` | `s1_p1.md` §D, §D.0, §A.1 | **U.015** | "one and only 2-for-1 split (1975-08-19)" vs **three** two-for-ones (1971-06-11, 1972-04-05, 1975-08-19) | **NEW — requested. 1975-08-19 is also outside Stage 1's window, so the original row was a boundary violation as well as a count error** |
| `U-A3/1` | A3; in `conflicts.csv` | **U.016** | FY1975 net sales 236,209 vs 226,209 thousand | row exists — renumber |
| `U-A3/2` | A3; in `conflicts.csv` | **U.017** | FY1970 net income $1,187,764 vs "1,011" vs implied 1,239 | row exists — renumber |
| `U-A3/3`, `U-A2/9` | A3 (row exists); A2 (no row) | **U.018** | FY1973 shares 6,512,950 vs 6,512,550 — **across two documents and inside one document** | row exists for the cross-document leg; **merge AMENDS its text to carry the intra-document leg rather than adding U-A2/9 as a duplicate** |
| `U-A2/1` | A2 §Contradictions (no row; p2 explicitly did not request it) | **U.019** | FY1972–FY1976 net income as published vs the FY1980 restated set | **NEW — requested** |
| `U-A3/4` | A3; in `conflicts.csv` | **U.020** | FY1977/FY1978 pre-tax and net income: as published vs SFAS-13 restated — **two live bases** | row exists — renumber |
| `U-A3/5` | A3; in `conflicts.csv` | **U.021** | the FY1978 restatement's size: −$769,000 (prose) vs −$695,000 (two arithmetic paths), **inside one audited document** | row exists — renumber |
| `U-A3/6` | A3; in `conflicts.csv` | **U.022** | FY1978 total assets 206,691 vs 251,865, same balance-sheet date | row exists — renumber |
| `U-A3/9` | A3; in `conflicts.csv` | **U.023** | FY1977 long-term debt: one line 23,245 or 19,158 + 4,087 | row exists — renumber |
| `U-A3/7` | A3; in `conflicts.csv` | **U.024** | the FY1977 letter's expense ratios 21.1 / 20.5 / 20.8 vs the same document's table (19.72 / 20.36 / 20.01 / 20.43) | row exists — renumber |
| `U-K/1` | `s1_p2.md` §K, drafted row | **U.025** | FY1976 expense ratio 20.5% (letter) vs 20.0% (Management's Analysis) — same report | row drafted by part 2 → renumber |
| `COR-A3-04` | A3 §Outbound corrections; part 1 §A.1 | **U.026** | FY1980 ten-year dividend row 1976–1979 ($.09/.11/.19/.25) vs each year's own print ($.065/.085/.16/.22) — **refuted** | **NEW as a conflict row (the correction exists in prose only) — requested** |
| `U-2` (probe), `U-W-5` (retest), `U-A2/3` (A2) | probe; retest; A2 | **U.027** | when and where the **first distribution centre** opened (1970 / 1971 / Springfield MO lore / a facility already existing before 1971-08-15) | part 2 drafted `U-A2/3` → **one row at U.027**; `U-2` and `U-W-5` are aliases |
| `U-A2/5` | A2; drafted by part 2 | **U.028** | the 1972 General Office + DC at **261,800** vs **263,800** sq ft | row drafted — renumber |
| `U-A2/6` | A2; drafted by part 2; part 1 §B.2 | **U.029** | **fifteen** assembled vs **fourteen** trading at 1970-01-01 vs **nine** variety/family-centre at FY1973 vs **fourteen closed** across the 1970s | row drafted — renumber |
| `U-A2/10` | A2 (no row; p2 did not request it) | **U.030** | FY1973 store arithmetic: 16 openings + 2 relocations against a net +13 ⇒ **≥5 unlisted exits** | **NEW — requested** |
| `U-A2/2` | A2; drafted by part 2 | **U.031** | the 1970 offering's terms: 200,000 shares / $3,030,467 net / no price vs "$16.50 per share" | row drafted — renumber |
| `U-A2/4` | A2; drafted by part 2 | **U.032** | April 1972 raise: "approximately $9,250,000" vs $8,913,504 credited vs $9,500,000 gross | row drafted — renumber |
| (part 1 §B.1 last row — "recorded as a live conflict at §U") | `s1_p1.md` §B.1 | **U.033** | **single founder** ("Sam Walton opens the first Walmart store", company page) vs **co-founders** ("Sam M. Walton and his brother James L. Walton", "Wal-Mart's co-founders", FY1980) | **part 1 forwarded it to "§U (part_2)"; part 2 did not mint it → REQUESTED HERE, at U.033** |
| `U-F/1` | `s1_p2.md` §F.1, drafted row | **U.034** | towns served: **average** 10,000–15,000 (FY1975) vs **range** 5,000–25,000 (FY1978/FY1980) | row drafted — renumber |
| `U-A4/1` | A4; in `conflicts.csv` | **U.035** | Grayson-Robinson cash-bind story at p.109 vs p.169 | row exists — renumber |
| `U-A4/2` | A4; in `conflicts.csv` | **U.036** | Kresge 1966 cover at p.26 vs p.126 | row exists — renumber |
| `U-A4/3` | A4; in `conflicts.csv` | **U.037** | 1962 sector distress by failure vs the registrant's untroubled planned-founding narrative | row exists — renumber |
| `U-A4/4` | A4; in `conflicts.csv` | **U.038** | A3 §7.2(c)'s requirement of an independent lineage vs the total absence of any press figure to disagree with — **a conflict of expectation against absence** | row exists — renumber |
| `U-A4/5` | A4; in `conflicts.csv`; inherited as a §P prohibition | **U.039** | $6 billion (Dec.1 1962) vs $6.9 billion (Jul.13 1963, for calendar 1962) | row exists — renumber |
| `U-A4/6` | A4; in `conflicts.csv` | **U.040** | "fewer stores … chains squeeze little guys" (1963) vs the registrant's rising unit series | row exists — renumber |
| `U-A4/7` | A4; in `conflicts.csv`; `timeline.csv` carries `U-A4/7-adjacent` | **U.041** | NRMA's Dec.1961 size-to-trading-area rule + over-concentration warning vs the Rogers opening actually built | row exists — renumber; **the `timeline.csv` cell reading "U-A4/7-adjacent" is not an id: the merge must resolve it to U.041 or clear it** |
| `U-A4/8` | A4; in `conflicts.csv` | **U.042** | "Small town greets the discounters": ALDENS vs Gamble-Skogmo attribution | row exists — renumber |
| `U-A4/9` | A4; in `conflicts.csv` | **U.043** | A4/B's blocked-host rows (HathiTrust TLS, Google Books 429) vs the repaired route state (200s, and 403 on page text) | row exists — renumber |
| `U-A5/1` | A5 §Data gaps (row drafted in the A5 file, **not merged**) | **U.044** | the 573-record SEC-pool inference vs the two SEC documents whose text reads zero | **row pending merge → renumber** |
| (part 1 §B.2 "label drift", §C.0 RANK 5) | `s1_p1.md` | **U.045** | origin year **1945** vs **1946** inside one lineage ("fifteen stores between 1945 and 1962" vs "between 1946 and 1962") | **NEW — requested** |
| (part 1 §A.1 last row) | `s1_p1.md`; A3 §0 fiscal-basis note | **U.046** | the company page's "1967 — 24 stores, $12.7 million" vs the audited **FY1968** basis: a one-year calendar mislabel that has propagated into secondary counts | **NEW — requested** |
| `A3-002` | A3 §3.3; part 1 §A.1 FY1974 row | **U.047** | FY1973 net sales "$124,889,141" (five-year table) vs **"$124,059,141"** on the same report's audited statement pages — **one document, two values** | **NEW — requested** |
| (this volume §T.3 R-1) | `s1_p2.md` merge block vs `A5` §CSV append rows | **U.048** | **`S0141` names two different documents** (corporate timeline page vs HathiTrust route probe); `S0139`/`S0140` agree | **NEW — requested; a register-hygiene conflict, registered so it cannot be resolved by silent overwriting** |

**Local keys that are NOT conflicts and are not given U. anchors:** the correction codes `COR-A3-01`…`COR-A3-11`,
`COR-A2-10`, `COR-A4-06`, `COR-A4-08` (outbound corrections, each of which either generated a U. anchor above or
is a supersession note with no live dispute); the A3/A4/A5 record ids `A3-0nn`, `A4-nn`, `A5-nn`; the probe's
`W-nn` and the retest's `WR-nn`/`R-nn`; `D-R01`…`D-R10` (part 1's dated record set, whose four `c` notes are
corrections except **D-R03c → U.014** and **D-R09c → U.015**, which are live conflicts and are mapped).

### U.1 The conflicts no register row covers, in full (§7 line format)

**U.013 — which founding the records support.** *CLAIM A:* the company was incorporated as **Wal-Mart Stores,
Inc. in 1969** (`sources/EXTRACT_corporate_walmart_history_timeline.md`, undated page, year only). *CLAIM B:*
**folklore** — "Wal-Mart, Inc., incorporated 15 March 1962" (Tier-4; **unattested anywhere on disk**).
*CLAIM C (the documented event):* the consolidated registrant was created by an **exchange accounted for as a
pooling, effective 1970-02-01**, out of "the various subsidiaries" held by **Walton Enterprises, Inc.**
(`WALMART_AR_1972.txt` Note 1, S0101). *WHY THEY DIFFER:* a corporate-history page compresses a multi-entity
reorganisation into one anniversary date, and a separate piece of lore supplies the missing operating entity
with a day and a month; the audited note never claims to be a founding story. *EVIDENCE WEIGHT:* C is Tier-1,
audited and dated to the day; A is Tier-1 as an artifact and Tier-4-equivalent as evidence (uncited,
current-state page); B has no document at all. *BEST-SUPPORTED INTERPRETATION:* **the 1962-vs-1969 argument is
the wrong frame.** The documented event is 1970-02-01 (part 1 §C.0 keeps it as the live losing rival for the
stage's close); the 1962 operating entity is a **separate, still-undated question**; A and B are recorded, not
adopted. *RESIDUAL UNCERTAINTY:* names, dates and states of every predecessor entity; what Walton Enterprises,
Inc. was; whether any 1962 or 1969 charter exists. *CONFIDENCE:* **High on 1970-02-01; UNKNOWN on 1962 and
1969.** (Probe `U-1` is an alias of this row. The shortest remaining route to narrowing it is **local** —
EDGAR `formerNames` — **U.203**, in flight.)

**U.014 — the state and day of incorporation, i.e. this volume's own header.** *CLAIM A:* part 1's header
states "**a Delaware corporation; incorporated 1969-10-01**", and §D-R03 carried it as FACT/Medium.
*CLAIM B:* **no document in `sources/` states a state of incorporation or any 1969 date at day precision** —
"Delaware" occurs **0 times** across the nine annual reports, and the only "Delaware" strings in the whole
corpus are a U.S.-state navigation list inside `walmart_museum_page.html` and an unrelated SEC ticker file; the
company page gives **1969, year only, no month, no day, no state, no citation**. *WHY THEY DIFFER:* an
upstream probe asserted a date and a state it had not read, and the header inherited them (method §14 rule 8 —
an inherited figure never grepped against the corpus). *EVIDENCE WEIGHT:* B is a verified negative across nine
files plus a positive reading of the only page that discusses the event. *BEST-SUPPORTED INTERPRETATION:*
**Date: 1969 (company-asserted, year only) · State: UNKNOWN · Day: UNKNOWN · Class: UNKNOWN · Conf: Low.** The
claim is **retracted, not restated**, and this volume repeats the retraction in its own geometry note so a
cold reader cannot re-import it. *RESIDUAL UNCERTAINTY:* whether any charter exists in the Arkansas SoS or
Benton County files (**U.211**, UNTRIED) or whether EDGAR's `formerNames` field states a state
(**U.203**, in flight). *CONFIDENCE:* **High** (that no local document supports either element).

**U.015 — the number of stock splits.** *CLAIM A:* part 1 §D-R09 — "**the one and only** 2-for-1 stock split in
the attested series; no second split exists in the corpus", dated 1975-08-19. *CLAIM B:* the corpus prints
**three** two-for-one events: **1971-06-11** (1,500,000 shares, $150,000 par charge) and **1972-04-05**
(3,000,000 shares, $300,000 par charge), **both inside the audited FY1972 capital note (S0101)**, plus
**1975-08-19** (+6,687,789 shares, S0105 Note 4; 6,687,789 × $.10 = $668,779, matching the ~$669,000 charged to
capital in excess). *WHY THEY DIFFER:* a count taken from one comparative table rather than from the capital
note that authorises the events. *EVIDENCE WEIGHT:* B is two audited documents; A rests on none.
*BEST-SUPPORTED INTERPRETATION:* **three splits printed, of which exactly one (1975-08-19) falls inside the
EPS-restatement dispute**, proven by the halving pattern FY1974 $.93 → $.47 — **one adjustment, not two**;
and 1975-08-19 is **outside Stage 1's window**, so its presence in a Stage-1 record set was a boundary
violation as well as a count error. *RESIDUAL UNCERTAINTY:* none on the count; the only open question is
whether further splits sit in the FY1981–FY1998 reports, which are **UNTRIED and outside the stage (U.220)**.
*CONFIDENCE:* **High** (that the "one and only" claim is refuted). **Do not resurrect it.**

**U.019 — which net income is "the" FY1972–FY1976 figure.** *CLAIM A (as published):* FY1972 $2,907k · FY1973
$4,591k · FY1974 $6,159k · FY1975 $6,353k · FY1976 $11,506k. *CLAIM B (FY1980 ten-year table):* $2,806k ·
$4,439k · $5,954k · $5,995k · $11,132k, with FY1976 pre-tax 22,057 not 22,798. *WHY THEY DIFFER:* retroactive
application of **SFAS-13** to store capital leases, over a base already broken by the **LIFO change effective
1975-01-31**. *EVIDENCE WEIGHT:* both Tier-1, same lineage, same auditors; A is what investors were told, B is
the series' final audited shape. *BEST-SUPPORTED INTERPRETATION:* **quote A for any statement about what was
known when, B for comparison with FY1979/FY1980, and label every figure as-filed or restated** — there is no
third figure that is "the real" number (the same rule A3 states at U-A3/4 → U.020). *RESIDUAL UNCERTAINTY:*
the FY1971–FY1974 restated values are read from the **OCR-scrambled FY1980 middle rows**, and whether pre-tax
income was restated for those years is not shown; the FY1979 report discharges FY1975–FY1978 cleanly
(COR-A3-03) but not FY1971–FY1974. *CONFIDENCE:* **High** (that a restatement occurred); **Low** (on the
individual pre-1976 restated values).

**U.026 — the refuted dividend row.** *CLAIM A:* the FY1980 ten-year summary's dividend row — 1976 **$.09**,
1977 **$.11**, 1978 **$.19**, 1979 **$.25**. *CLAIM B:* each year's own report — **$.065** (S0105), **$.085**
(S0106), **$.16** (S0107, with quarterly .025/.045/.045/.045 summing ✓), **$.22** (S0108, four quarters at
$.055 ✓). *WHY THEY DIFFER:* no split factor reconciles them ($.09 ÷ $.065 = 1.38 is not a split), so the
candidates are a typesetting/OCR failure in the ten-year block or an unstated alternative basis; the document
supplies no bridge. *EVIDENCE WEIGHT:* **four contemporaneous prints against one retrospective table, and the
retrospective table's middle rows are separately known to be OCR-damaged (A2 W-69).**
*BEST-SUPPORTED INTERPRETATION:* **the contemporaneous rows govern; the FY1980 row is kept on the record as
printed and is BARRED from `quantitative.csv` and from any per-share dividend series** (COR-A3-04).
*RESIDUAL UNCERTAINTY:* why the FY1980 table prints what it does — **page image UNTRIED (U.206)**.
*CONFIDENCE:* **High** (that the four-year row is refuted).

**U.030 — store arithmetic that closes only if unlisted exits are admitted.** *CLAIM A:* FY1973 prints 16 new
stores plus 2 enlarged relocations. *CLAIM B:* stores at year end **64** against **51** a year earlier — net
**+13**. *CLAIM C (the comparison):* FY1976 prints "twenty-two new units were opened" against a net +21, which
**closes exactly** if the January 1976 Rogers Ben Franklin closure is counted. *WHY THEY DIFFER:* openings are
gross and the tables are net; the FY1973 report simply does not list the exits. *EVIDENCE WEIGHT:* one lineage,
but the arithmetic is internal and checkable, and FY1976 demonstrates the mechanism. *BEST-SUPPORTED
INTERPRETATION:* **FY1976 reconciles; FY1973 does not — at least five units left the base unlisted**, and the
register states the exits as **UNKNOWN**, not as variety-store conversions (which is an inference about banner
run-down that no document licenses). *RESIDUAL UNCERTAINTY:* which stores, where, under which banner, sold or
closed. *CONFIDENCE:* **High** (the arithmetic); **UNKNOWN** (the exits).

**U.033 — one founder or two.** *CLAIM A:* the company's own curated page — "**Sam Walton** opens the first
Walmart store" (single founder, no co-operator). *CLAIM B:* FY1980 — "The first Wal-Mart Discount City store was
opened in 1962 in Rogers, Arkansas **by Sam M. Walton and his brother James L. Walton**", captioned
"**Wal-Mart's co-founders**"; the same man appears as **J. L. 'Bud' Walton** in S0106/S0108 and as **Senior
Vice President** in S0103's officer list. *WHY THEY DIFFER:* an anniversary page compresses the story to one
name; the audited-era report names two operators and a board page attests the second as an officer.
*EVIDENCE WEIGHT:* B is Tier-1 registrant print **attested inside the audited document set** and corroborated
within the same lineage three times; A is Tier-1 as artifact, uncited as evidence. Both are **one lineage**, so
the independent-origin count is **1 either way** — the disagreement is between two company artifacts, not
between the company and the record. *BEST-SUPPORTED INTERPRETATION:* **the co-operator is in the company's own
documents and the single-founder form is a curation choice; neither reading is independently evidenced for
1962.** *RESIDUAL UNCERTAINTY:* what either man did, and who decided. *CONFIDENCE:* **High** (that the two
company artifacts disagree); **Low** (the 1962 event). *This row also services §2:* it is the registrant's own
evidence against the single-genius framing.

**U.045 — 1945 or 1946 as the beginning of the count.** *CLAIM A:* "Between **1945** and 1962, they assembled a
group of fifteen successful Ben Franklin stores" (S0104); FY1980 "Beginning in 1945…". *CLAIM B:* "15 Ben
Franklin stores between **1946** and 1962" (S0108); the partnership formed "in 1946" (S0107); Bud's Versailles
store in 1946 (S0106). *WHY THEY DIFFER:* the second date marks the brothers' partnership, the first Sam's
individual franchise; the reports use both without reconciling them, and the labels drift from "Ben Franklin
stores" to "variety stores". *EVIDENCE WEIGHT:* equal — one lineage, several reports. *BEST-SUPPORTED
INTERPRETATION:* **the stage opens on the claimed 1945 individual franchise and the count's start is printed
both ways; the volume uses "1945 → 1962" for the span and flags 1946 as the partnership year, and neither is
documented.** *RESIDUAL UNCERTAINTY:* total — no deed, agreement or register entry for either year.
*CONFIDENCE:* **Low** on both, **High** that the registrant prints both.

**U.046 — the calendar-year mislabel on the company's own page.** *CLAIM A:* the page's "1967 — The Walton
family owns 24 stores, ringing up **$12.7 million** in sales". *CLAIM B:* the audited series — **FY1968**
(ended 1968-01-31) is the year with **24 stores and $12,618,754**; FY1967 prints nothing anywhere (U.102).
*WHY THEY DIFFER:* a fiscal year ending 31 January is labelled by its **starting** calendar year. *EVIDENCE
WEIGHT:* B is Tier-1 audited and internally consistent; A is the same number with the wrong label.
*BEST-SUPPORTED INTERPRETATION:* **the page's "1967" is FY1968.** Every register row must carry the fiscal
basis, and **no FY1967 value may be created out of this label** — the year is EMPTY, not $12.7 million.
*RESIDUAL UNCERTAINTY:* none about the mechanism; the page's other labels are checked the same way (its "1972 —
51 stores, sales of $78 million" happens to be correct). *CONFIDENCE:* **High.**

**U.047 — one report, two FY1973 sales figures.** *CLAIM A:* **$124,889,141** in FY1973's own Five-Year/
Highlights presentation and in every later comparative print. *CLAIM B:* **"$124,059,141"** printed for FY1973
on the FY1974 report's audited statement pages. *WHY THEY DIFFER:* a typewriter or OCR transposition in the
statement block of a document whose FY1974 own-column is separately missing (A3-002) — which is why A3 takes
FY1974's money from the Five Year Progress Report rather than the statement pages. *EVIDENCE WEIGHT:* A has
many printings (one lineage) and is consistent with the FY1973 report's own totals; B is a single cell in a
block with two known defects. *BEST-SUPPORTED INTERPRETATION:* **$124,889,141 governs; the misprint is
recorded, not deleted.** *RESIDUAL UNCERTAINTY:* which physical page erred — FY1974 page image UNTRIED
(U.206). *CONFIDENCE:* **High** (A) / **Low** (B).

**U.048 — `S0141` names two documents.** *CLAIM A:* `s1_p2.md`'s merge block issues **`S0141` = the company's
curated history page** (`EXTRACT_corporate_walmart_history_timeline.md`). *CLAIM B:* A5's pending block issues
**`S0141` = the HathiTrust search/catalogue route probe**, and `s1_p2.md` separately issues `S0142` = the museum
page while A5's `S0139`/`S0140` match p2's. *WHY THEY DIFFER:* two writers extended the same append-only id
block without the central assignment §13 requires. *EVIDENCE WEIGHT:* both rows are genuine; the ids are not
unique. *BEST-SUPPORTED INTERPRETATION:* **the merge re-issues one id per document** — recommended: keep
`S0139`/`S0140` as agreed by both, take the next free central ids (`S0143` onward) for whichever of the
corporate page, museum page and HathiTrust probe does not already hold one, and **re-point both volumes'
prose**; the `keys` gate will then resolve. *RESIDUAL UNCERTAINTY:* the final numbering, which the register
owner owns.
*CONFIDENCE:* **High** (that the collision exists; it is verifiable by reading the two blocks).
**No prose in this volume depends on who wins: every not-yet-issued id is written backticked.**

### U.2 Documented nulls (EMPTY within a stated perimeter) — anchors U.101–U.116

| Anchor | Null | Perimeter of the silence (stated, because a null without a perimeter is a claim about the world) | Conf |
|---|---|---|---|
| **U.101** | **No document of any kind in this corpus names the company before 1972-03-22** | the nine reports; 13 BW index volumes (S0112–S0124); 8 *Stores* apparatuses (S0125–S0133); 2 SEC government documents (`S0139`, `S0140`); EDGAR (floor 1994-02-14); web archives (floor 1996-12-29). **NOT** the whole of print | **High** |
| **U.102** | FY1962–FY1967 — **every** financial and physical variable EMPTY; earliest counted year FY1968 | nine reports, all summary tables and narrative pages; the FY1974 five-year table starts FY1970 and the FY1978 nine-year table starts FY1970, so later restatement cannot reach it either | High |
| **U.103** | FY1968–FY1969 cost of sales, expense, balance sheet, shares, headcount, square footage | same perimeter | High |
| **U.104** | **No FY1970 or FY1971 annual report exists on this route** | IA `title:("wal-mart") AND year:[1962 TO 1971]` → numFound **0**; admissible because the same query style returns known-good hits in the same index. **Hoover's / LOC-WorldCat / SEC Reference Room UNTRIED** | High (as an IA-holdings null; **not** a loss null) |
| **U.105** | No total store square footage before FY1976 | FY1972–FY1975 print additions only | High |
| **U.106** | No market price before FY1975 anywhere in the corpus | earliest price table is in the FY1976 report, reaching back only to fiscal 1975 | High |
| **U.107** | No comparable-store figure for any year except FY1978 (plus the FY1972 cohort sentence) | nine reports; FY1979/FY1980 Management's Analysis not re-walked (**U.217**) | High |
| **U.108** | No legal person named for 1945–1962; the predecessor subsidiaries are never enumerated; the outcome of the IRS proposals is not stated | nine reports; the reports say "the various subsidiaries" | High |
| **U.109** | **No document states the problem the 1962 format answered, or any rationale for any in-window decision** | nine reports + all company/press/agency documents read. §C's "single most consequential silence" | High |
| **U.110** | No 1945, 1946, 1950 or 1962 primary document (agreement, lease, deed, permit, register tape, photograph, press item) | whole corpus; the museum's 1950 bill of sale and the 1962 advertisement image are **leads, not bytes** | High |
| **U.111** | 7 of ~200 *Stores* monthly issues 1945–1961 name nobody relevant (1946-06, 1950-06, 1951-06, 1955-06, 1958-06, 1961-03, 1961-12); all five *Stores* annual indexes that exist on this route carry zero Wal-Mart entries | **193 issues UNTRIED (U.212)**; the annual index is **subject-only**, so a zero means "not indexed under that word" | Medium; **the licensed sentence is "the issues sampled do not name it"** |
| **U.112** | The SEC's complete register of exchange-traded issuers at 1970-12-31 prints the company **0** times in 153,481 words | **exchange-listed securities only**: not Securities Act registrants, not §12(g)/OTC registrants, §3(a)-exempted issues excepted. W-block legible (WALGREEN…WALWORTH), so OCR loss excluded | **High — informative, and the only independent datum in Stage 1** |
| **U.113** | **No press figure for this company in any year 1962–1980** has been recovered | every item read in A4; the row is recorded as EMPTY-within-the-corpus and the **independent-lineage count stays at 1** — a sector number is never substituted for a company number | High |
| **U.114** | FY1973, FY1976 and FY1978 headcount UNKNOWN; FY1976's employee chart is OCR-damaged | nine reports; page images UNTRIED (U.206) | High (that the numbers are absent) |
| **U.115** | **The company's own curated timeline is silent about everything before July 1962** — no Newport, no 1950 Bentonville store, no lease-loss story, no Bud Walton, no Plaza store | one document, but a *finding about curation*: the self-narrative omits the very years the annual reports narrate, so page and reports **cannot be counted twice** | High (documented absence on a document on disk) |
| **U.116** | No dividend row exists before FY1974 in any print, and FY1974's own table has none | the first evidenced payment is $.025 on 1974-04-05, RESTAT in S0107's nine-year table | High |

### U.3 UNANSWERED and UNTRIED routes — anchors U.201–U.222 (detail in the final section)

| Anchor | Route | State | Owner at release time |
|---|---|---|---|
| U.201 | 1972–1979 SEC issuer registers (1978 *Securities traded*; 1979NO1 §13(f) list) | **FETCH REQUEST — in flight** | mining agent |
| U.202 | On-disk but unmined `ia_arkgaz.json`, `ia_satpost.json`, `ia_supermerch.json`, `ca_01_waltons_five.json`, `gb_01_waltons_five_and_dime.json` | **FETCH/FILE REQUEST — in flight** | mining agent |
| U.203 | EDGAR `formerNames` / former-name + state-of-incorporation search (**local**) | **in flight** | mining agent |
| U.204 | FY1976 origin-wording re-walk (`WALMART_AR_1976.txt`, A2's partially-OCR'd W-50) | **FETCH REQUEST — in flight** | mining agent |
| U.205 | FY1975 page-image digit test (`_text.pdf`) → settles U.016 | **FETCH REQUEST — in flight; declared `S0111` lead** | mining agent |
| U.206 | Page images FY1974/77/78/79 → U.017, U.018, U.026, U.047, FY1975 balance sheet, FY1976 chart | **UNTRIED** | — |
| U.207 | HathiTrust full-view **page text** (the 573-record pool; 52 SEC serials) | **UNANSWERED** (403 on `/cgi/pt` and `/cgi/imgsrv/html`; search and catalog answer) | — |
| U.208 | NLRB *Court decisions* v.26 (1973–74), *Decisions and orders* v.201 (1973); FAA *civil aircraft register* 1971–78 | **UNTRIED** (`X-A5/1`) — the most probable positive-naming class ever located here | — |
| U.209 | SEC *Directory of companies filing annual reports* 1970/1971/1972 | **UNTRIED** (`X-A5/4`) | — |
| U.210 | 1970 registration statement: EDGAR full-text + SEC Reference Room / National Archives | **UNTRIED** (`X-A5/3`) — the only accession-numbered route to the IPO years | — |
| U.211 | Arkansas SoS; Benton County and Mississippi County deed/incorporation files | **UNTRIED** | — |
| U.212 | remaining ~193 *Stores* monthlies + the NRDGA/NRMA **membership roster / chain directory** | **UNTRIED** | — |
| U.213 | *Chain Store Age* "Directory of Chain Stores" 1963–1970; *Discount Store News*; *Discount Merchandising*; D&B discount volumes; AUDITS & Surveys; the Cornell study; Hoover's | **UNTRIED / route-blocked** — A3 §7.2(d)'s named missing witness | — |
| U.214 | the catalogued 1962 "First Walmart Advertisement" image | **UNTRIED read** | — |
| U.215 | the FY1972 report's direct-server text layer (23,989 B) and the 27-item FY1972–FY1998 run list held in `00_universe/harvest/corporate_print/`, unread by every Stage-1 dossier | **ARRIVED DURING THE RUN — being read now** (§14 rule 11) | mining agent |
| U.216 | Wayback `matchType=prefix` (HTTP 504); December 1970 SEC bulletin (HTTP 500, one attempt); Google Books keyed v1 `dateRestrict`; Federal Register pre-1994 via govinfo; the **1970-08-27/09-03 first-trade cluster** | **UNANSWERED / UNTRIED** (`X-A5/2`, `X-A5/5`, `U-A5/2…5`) | — |
| U.217 | FY1979/FY1980 Management's Analysis comparable-store sentences; FY1974/75/77/78 **lease-commitment notes**; FY1977–79 market-price and dividend tables | **UNTRIED (local)** | — |
| U.218 | Census of Business 1963/1967 for AR/MO/OK/KS/TX (extract-only, never dumped); the Greensboro chamber trade-area study (`hf-5465.-u-55-g-7`); duplicate BW index bindings as an OCR control; BW/*Stores* page images | **UNTRIED** | — |
| U.219 | the 1992 memoir **as a text** (bytes not in this repository) | **UNTRIED** — and it would remain a FOUNDER CLAIM even when read | — |
| U.220 | FY1981–FY1998 corporate print (rest of the IA run) | **UNTRIED, out of stage** — recorded so the run's remaining gap stays visible | — |
| U.221 | **auction / museum documentary family** — §14 rule 6's fourth family, never properly tried for this company | **UNTRIED** (the reason the company-level verdict stays `PROVISIONAL`) | — |
| U.222 | the **genre control**: do other 1950s–60s printed annual reports state a founding rationale? — the only test available for §C's silence | **UNTRIED** (non-Walmart documents) | — |

### U.4 The finding §U exists to protect

Strip every row above to one sentence and Stage 1 says: **the company's own audited print is deep from FY1972
and mute before it; the one independent document in the entire stage is a register that does not contain the
company; and every date earlier than 1970-02-01 arrives as a retrospective sentence in the registrant's own
voice.** No anchor in §U closes that gap by preference, by averaging, or by importing an outcome. Six of the
mappings above exist solely so that a claim already refuted on the page — **Delaware (U.014)**, the **single
split (U.015)**, the **FY1980 dividend row (U.026)**, the **"first SEC-visible registration" label** (part 1
§C.0), **Newport-as-Nebraska (U.011)** and the **FY1967 sales label (U.046)** — cannot re-enter through a
later volume, because each now has an address the registers carry.

