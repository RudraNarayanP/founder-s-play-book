# B1_dayton_print_records.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T20:24:29Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## Layers held

Stage 1 boundary carried forward **unchanged** from the probe: *The Dayton Company at FY1965
narrating 1962*. Every record below is quoted from bytes on disk in
`sources/corporate_print/`, read this session.

**Five layers fetched this session** (FY1966, 1967, 1971, 1973, 1974), which closes the probe's
U-5 gap and makes the founding-era run **FY1965→FY1975 gap-free, eleven consecutive years**.
New bytes: 371,992 B. Route: verified TLS was **attempted first and failed** on all five
(`SSL: CERTIFICATE_VERIFY_FAILED … certificate has expired` — the stale local CA store), so the
fetch used `--insecure`. All five sidecars stamp
`transport: UNVERIFIED TLS -- re-check before citing at High confidence`. **Those five layers
therefore cap every claim resting solely on them at Medium** until re-checked. The nine probe
layers keep `verified TLS`. `ia_text.py fetch` cannot address sub-files of a multi-report item,
so the per-year file names were taken from the held item listing
`sources/ia_search/meta_01-target-archive.json` and fetched through `ia_text.ocr_url()` +
`ia_text.get()` — same endpoints, same UA, same retry class; no WebFetch/WebSearch was used.

| FY | file (in `sources/corporate_print/`) | bytes | entity masthead read inside the layer | TLS |
|---|---|---|---|---|
| 1965 | `1965_dayton_hudson_djvu.txt` | 48,050 | `THE DAYTON COMPANY @ ANNUAL REPORT 1965` (re-read in bytes this session; the three lines above it are library-stamp OCR noise: `VEEVECAND PUSLIC LIBRARY`, `HOSIMESS INF. BUR.`, `GORPORATION FILE`) — balance-sheet head `THE DAYTON COMPANY AND RETALE SUBSIDIARIES` L757 | verified |
| 1966 | `1966_dayton_hudson_djvu.txt` | 43,364 | `The Dayton Company.` L184 (subsidiary-note head); first lines are stamp noise `Tld NOWWWYOdYOD | …` | **UNVERIFIED** |
| 1967 | `1967_dayton_hudson_djvu.txt` | 45,200 | `Dayton Corporation | Annual Report /1967` (L1-2) — parent name already changed | **UNVERIFIED** |
| 1968 | `1968_dayton_hudson_djvu.txt` | 52,479 | masthead not re-read (first lines are stamp noise); entity read from body text this session: `DISCOUNT AND HARD GOODS STORES` group table L684, notes L1355-1363 | verified |
| 1969 | `1969_dayton_hudson_djvu.txt` | 55,348 | Dayton Hudson (masthead lines read by probe only); body: `Low Margin Stores Group` L532 | verified |
| 1970 | `1970_dayton_hudson_djvu.txt` | 53,023 (sidecar agrees; the probe's table printed 52,736 — see N6) | `Dayton Hudson | Corporation | Annual Report` (L1-3) | verified |
| 1971 | `1971_dayton_hudson_djvu.txt` | 55,420 | `Dayton Hudson | Corporation | Annual Report | 1971` | **UNVERIFIED** |
| 1972 | `1972_dayton_hudson_djvu.txt` | 75,196 | `Cayton hudson corporation 1972 annual report` | verified |
| 1973 | `1973_dayton_hudson_djvu.txt` | 114,193 | Dayton Hudson Corporation (Contents head; `Five Year Comparisons` block L2360-analogue) | **UNVERIFIED** |
| 1974 | `1974_dayton_hudson_djvu.txt` | 113,815 | `ayton Hudson | Corporation` | **UNVERIFIED** |
| 1975 | `1975_dayton_hudson_djvu.txt` | 130,295 | `Dayton Hudson Corporation Annual Report -- 1975` + `ProQuest Historical Annual Reports` | verified |
| 1998/1999/2000 | 3 layers | 344,257 | Dayton-Hudson → Target name changeover (Stage 3 leg; unused here) | verified |

STATUS: WRITTEN 2026-09-26 (target-s1-records)

## Entity-lineage key

Every figure below is stamped with the masthead that printed it. A number printed under one
entity belongs to that entity's line and may not be carried onto "Target" without naming the
filer. The uploader's file names are **not** evidence: all 1965-1998 layers are labelled
`… Dayton Hudson Corp (DH) …` in item `01-target-archive`, which would misdate the merger by four
years (probe conflict K3, confirmed again this session: the FY1965 masthead in bytes reads
`THE DAYTON COMPANY @ ANNUAL REPORT 1965`, the FY1967 masthead reads `Dayton Corporation`).

| masthead as printed | layer(s) | what its numbers are | relation to today's registrant |
|---|---|---|---|
| **The Dayton Company** | FY1965, FY1966 | its own consolidated retail sales and the Target store estate it owned; Target Stores, Inc. named as its subsidiary | ancestor; **not** an EDGAR registrant on any held document |
| **Dayton Corporation** | FY1967, FY1968 | parent-level group sales by operating group (Department / Discount and Hard Goods / Specialty) | ancestor |
| **Dayton Hudson Corporation** | FY1969→FY1998 | corporation-level totals plus Low-Margin-Store group data | EDGAR `formerNames` for CIK 27419 = **one** entry, `DAYTON HUDSON CORP` 1994-12-09→1999-04-12 (probe-held raw JSON). No Dayton Co / Goodfellow / Dey Brothers former name exists in EDGAR, and EDGAR carries no paper-era filings at all |
| **Target Corporation** | FY1999→ | modern registrant | its own filings begin 1994-02-10 (SC 13G), first 10-K 1994-04-21 |

Two subsidiary levels matter for Stage 1 and must not be conflated with the parent:
1. **Target Stores, Inc.** — the operating company. FY1965 L125 `the discount merchandising field
   in 1962 with Target Stores, Inc.` and the subsidiary-officers page L1452-1456
   (`Principal Officers of Subsidiaries` → `DOUGLAS J. DAYTON, President, Target Stores, Inc.`).
2. **"Low margin stores" / "Discount and Hard Goods Stores"** — a *reporting group*, not a company.
   FY1968 prints the group as `Discount and Hard Goods Stores` (L1361: `Goods Stores 189,515,025 44
   141,824,116 38 33.6`), and the FY1972 `Five Year Comparisons` prints the same 1968 figure under
   the later group name `LOW MARGIN STORES` (L2374-2375 `Sales … $189.5`). Any series that mixes
   group revenue with Target-unit revenue must say which, or it silently changes the denominator.

STATUS: WRITTEN 2026-09-26 (target-s1-records)

## Store and sales series

The prize: a Target store-count and sales run for FY1962-FY1972 that **exists nowhere in EDGAR**
(the registrant's own filings begin 1994-02-10; probe null N2). It exists here, in eleven
consecutive years of the entity's own stockholder print. Two bases must never be merged:
**TARGET (unit)** = the discount chain; **LOW MARGIN GROUP** = the reporting group, which also
carried Lechmere (hard goods) and, from 1971, acquired Lechmere stores. Fiscal year = calendar
year in these reports (`ANNUAL REPORT 1965`, revenue tables headed `Group 1969 1968`).

**Row S-1 is the load-bearing discovery of this pass**: the FY1973 report's `Five Year Comparisons`
(L3975 columns `1973 1972(*) 1971 1970 1969`) prints the whole low-margin row, which no other layer
in the run renders complete.

| ID | Date | Metric | Value | Unit | Source | Source date | Confidence |
|---|---|---|---|---|---|---|---|
| Q1 | 1962 | Target stores opened in 1962 (Roseville, Crystal, Duluth, Knollwood/St. Louis Park) | 4 | stores | FY1965 chronology L725-738; recap in FY1974 roster L4636-4641 | 1965 / 1974 | Medium |
| Q2 | 1965 | Target stores in operation | 5 | stores | FY1965 L189 `This brought the total number of Target stores to five.` + L400 `There are now five Target stores, with four situated in the Minneapolis-St. Paul metropolitan area and one in Duluth.` | 1965 | High |
| Q3 | 1966 | Target stores in operation | 7 | stores | FY1966 L219 `Total retail area of the seven Target stores now in operation is 889,000 square feet.` | 1966 (UNVERIFIED TLS) | Medium |
| Q4 | 1967 | Target stores in operation (Fridley + West St. Paul opened October) | 9 | stores | FY1967 L180-182 + FY1966 L217-218 (`numbers eight and nine scheduled to open Fall, 1967`); FY1974 roster 1967 rows ×2 | 1967 | Medium |
| Q5 | 1968 | Target stores at year end | 11 | stores | FY1973 L564-565 `Target has grown from 11 stores to 46 stores in five years.` (retrospective) | 1973 (UNVERIFIED TLS) | Medium |
| Q6 | 1969 | Target stores at year end | 17 | stores | DERIVED: 11 (Q5) + 6 opened in 1969 (FY1969 L540-544 lists 2 Dallas + 2 Houston + 1 Colorado Springs + 1 St. Louis) | 1969/1973 | Low |
| Q7 | 1970 | Target stores at year end | 24 | stores | DERIVED from FY1971: 30 (Q8) − 6 opened (FY1971 L816); matches FY1969's plan `to raise its total to 24` (L550-551), which is a plan not an actual | 1971 | Low |
| Q8 | 1971 | Target stores at year end | 30 | stores in 11 markets | FY1971 L831 `At year's end, Target had 30 stores in 11 markets.` | 1971 (UNVERIFIED TLS) | Medium |
| Q9 | 1972 | Target stores at year end | 46 | stores in nine states | FY1972 L476-478 `Target opened 16 new stores within a seven-month period, increasing retail space by 38 percent and completing the year with 46 stores in nine states.` | 1972 | High |
| Q10 | 1967 | Target (unit) sales | 86,901,007 | $ | FY1967 L769-770 `Target's sales were $86,901,007, an in-crease of 43 percent.` | 1967 (UNVERIFIED TLS) | Medium |
| Q11 | 1966 | Target (unit) sales, implied base of the 43% | ~60,800,000 | $ | DERIVED: 86,901,007 ÷ 1.43 (Q10's own rounded percent) | 1967 | Low |
| Q12 | 1967 | Discount-and-Hard-Goods GROUP revenue | 141,824,116 | $ | FY1968 L1361 | 1968 | High |
| Q13 | 1968 | Discount-and-Hard-Goods GROUP revenue (44% of retail sales) | 189,515,025 | $ | FY1968 L1361 `Goods Stores 189,515,025 44 141,824,116 38 33.6`; total retail $434,132,744 L1363 (foots: 223,276,791+189,515,025+21,340,928) | 1968 | High |
| Q14 | 1968 | Low-margin GROUP stores | 13 | stores | FY1972 Five Year Comparisons L2382 (`LOW MARGIN STORES` L2374, `Sales … $189.5` L2375) | 1972 | High |
| Q15 | 1969 | Low-margin GROUP revenue | 233,532 | $000 | FY1969 L1003 `Low Margin............. 233,532 189,515` under `Revenues (00s)` L998-1000 (column foots to $888,357 total revenue) | 1969 | High |
| Q16 | 1970 | Low-margin GROUP revenue / stores | 289.0 / 27 | $m / stores | FY1973 L3988, L3995 (recap column) | 1973 (UNVERIFIED TLS) | Medium |
| Q17 | 1971 | Low-margin GROUP revenue / stores | 345.8 / 34 | $m / stores | FY1973 L3988/L3995; revenue independently printed FY1972 L1040 `Revenues ....... $440.4 $345.8 27.4%` | 1971-1973 | Medium |
| Q18 | 1972 | Low-margin GROUP revenue / stores | 440.4 / 50 | $m / stores | FY1972 L470 `Sales of the low-margin group increased 27.4 percent to $440,441,000.`; FY1973 L3988/L3995 | 1972 | High |
| Q19 | 1973 | Low-margin GROUP revenue / stores | 470.3 / 50 | $m / stores | FY1973 L3988/L3995 (contemporaneous column) | 1973 (UNVERIFIED TLS) | Medium |
| Q20 | 1964→1972 | Parent net retail sales (whole company, NOT Target) | 162,773,739 / 186,166,671 / 217,961,635 / 260,173,514 / 434,132,744 / 868,335(000) / 945,306(000) / 1,086.4(m) / 1,262,759,000 | $ | FY1965 L169-171, L822; FY1966 L49; FY1967 L765/L819; FY1968 L1349/L1363; FY1969 L951; FY1970 L829; FY1971 L312; FY1972 L325 | 1965-1972 | High (each in its own year) |

**Not printed anywhere in the eleven layers:** Target-unit (as opposed to group) sales for 1962,
1963, 1964, 1965, 1968, 1970, 1971 and 1972 — gap G-3. The FY1969/FY1970/FY1971 `Five Year
Comparisons` blocks print the row labels but **lose their numeric columns in OCR**
(e.g. FY1971 L2298-2307: `LOW MARGIN STORES / Number of stores … / Sales (millions) …` with no
figures) — a rendering null on held bytes, not an absence of the data in the original.

**Independence discipline for this whole table.** Every row is company stockholder print from one
reporting lineage. FY1973's recap of 1969/1971/1972 agrees with FY1969/FY1972's contemporary
printing, and FY1972's five-year table agrees with FY1968's group revenue — but a recap that repeats
a figure is **not** a second source; it is the same source in a later year, and the agreement only
proves the company carried its own number forward. Where a later report *restates* under a wider
scope (FY1969's 1968 department-store column reads `582,923` where FY1968's own report printed
`$223,276,791`, because the 1969 column is the merged Dayton Hudson scope), the later figure is
RESTATED and may not be used as corroboration of the contemporary one.

STATUS: WRITTEN 2026-09-25

## 1962 origin records

Claim records for Stage 1 (The Dayton Company at FY1965 narrating 1962). `B1-` ids are
dossier-local. Every `Passage:` field is a verbatim line read from held bytes this session;
`— Independence:` carries the §3 independence note the register expects.

```
B1-01 Claim: The Dayton Company, not any entity named Target, entered discount merchandising in 1962 through a subsidiary called Target Stores, Inc. — Date: 1962 — Source: The Dayton Company, Annual Report 1965 (stockholder report; IA item 01-target-archive, per-year OCR layer) — Source date: 1965 — URL: https://archive.org/download/01-target-archive/1965%20-%20Dayton%20Hudson%20Corp%20%28DH%29_djvu.txt (local bytes: sources/corporate_print/1965_dayton_hudson_djvu.txt L124-125) — Archived: held locally — Tier: 1 — Class: FACT — Passage: "The Company entered the discount merchandising field in 1962 with Target Stores, Inc., which now has five" — Conf: High — Corroboration: 1 independent origin (company self-account) — Conflicts: None — Independence: one source only; the same sentence is re-narrated in FY1973 and FY1999 print, which is the same lineage repeating itself, not corroboration.
```
```
B1-02 Claim: The first Target store opened in Roseville, a suburb north of St. Paul, "early in 1962"; no month or day is printed in any held layer. — Date: 1962 (month UNKNOWN) — Source: The Dayton Company, Annual Report 1965 — Source date: 1965 — URL: as B1-01, local L397-398 — Archived: held locally — Tier: 1 — Class: FACT as to year and place; UNKNOWN as to calendar day — Passage: "Since the first Target store was opened early in 1962 in Roseville, a suburb north of St. Paul, its identification as a quality discount operation has been firmly established." — Conf: High (year/place), UNKNOWN (day) — Corroboration: 1 — Conflicts: U.K2 (1962-07-01 widely asserted, no carrier held) — Independence: no independent carrier exists on disk; the company's own chronology page (L725-738) is the same document.
```
```
B1-03 Claim: Target Stores, Inc. existed in FY1965 as a subsidiary of The Dayton Company with named principal officers. — Date: 1965 — Source: FY1965 report, "Principal Officers of Subsidiaries" page — Source date: 1965 — URL: as B1-01, local L1452-1456 — Tier: 1 — Class: FACT — Passage: "DOUGLAS J. DAYTON, President, Target Stores, Inc." and "JOHN GEISSE, Vice President, Target Stores, Inc." — Conf: High — Corroboration: 1 primary (re-printed FY1966 L1449-1457, FY1967 L1947-1956) — Conflicts: None — Independence: same lineage across the three years; one officer-listing source repeated.
```
```
B1-04 Claim: The store count reached five during 1965 when a Bloomington, Minnesota store opened; four were in the Minneapolis-St. Paul area and one in Duluth. — Date: 1965 — Source: FY1965 report — Source date: 1965 — URL: as B1-01, local L187-189, L400-401 — Tier: 1 — Class: FACT — Passage: "This brought the total number of Target stores to five." / "There are now five Target stores, with four situated in the Minneapolis-St. Paul metropolitan area and one in Duluth." — Conf: High — Corroboration: 1 (FY1974 roster L4636-4642 lists exactly those five with opening years — same lineage) — Conflicts: None — Independence: single lineage; the roster is a later restatement of the same estate.
```
```
B1-05 Claim: Four Target stores carry opening year 1962 in the company's own FY1965 chronology page (Roseville, Crystal, Duluth, Knollwood/St. Louis Park). — Date: 1962 — Source: FY1965 report, subsidiary/store chronology spread — Source date: 1965 — URL: as B1-01, local L725-738 — Tier: 1 — Class: RETROSPECTIVE INTERPRETATION at three years' remove (printed 1965 about 1962), FACT as to the FY1965 estate — Passage: "TARGET STORES, INC. 1962 … ROSEVILLE, MINNESOTA 1962 … CRYSTAL, MINNESOTA 1962 … DULUTH, MINNESOTA 1962 … KNOLLWOOD, ST.LOUIS PARK … MINNESOTA 1962" — Conf: Medium — Corroboration: 0 independent; column interleaving in the OCR means the store↔year pairing must be read against the FY1974 roster (L4636-4641), which agrees — Conflicts: None — Independence: two report years, one lineage.
```
```
B1-06 Claim: The first Target venture outside the Upper Midwest was planned for Denver in Fall 1966 and the two Denver stores opened in October 1966. — Date: 1966-10 — Source: FY1965 report L190-192 (plan); FY1966 report L355 (actual) — Source date: 1965; 1966 — URL: archive.org/download/01-target-archive/ per-year layers; local L1965 L190-192, 1966 L355 — Tier: 1 — Class: FACT for the plan; FACT for the opening — Passage: "Two more Target units are scheduled to be opened in Denver, Colorado, in the Fall of 1966, marking our first venture outside the Upper Midwest." / "reflects the interim financing for two Target stores opened in Denver in October of 1966." — Conf: High (FY1965, verified TLS); Medium (FY1966, UNVERIFIED TLS) — Corroboration: 1 — Conflicts: None — Independence: FY1967 L177-179 ("In their first full year of operation, Target's two Denver stores…") is the same company repeating.
```
```
B1-07 Claim: The company printed third-party adoption evidence that 51% of Hennepin County women customers shopped a Target store in 1965. — Date: 1965 — Source: FY1965 report quoting a Minneapolis Star and Tribune "Retail Revolution 1955-1965" survey — Source date: 1965 — URL: as B1-01, local L404-410 — Tier: 1 for the report page; the survey itself is Tier-2 and NOT HELD — Class: CONTEMPORARY OBSERVATION (second-hand) — Passage: "discloses that 51 percent of women customers in Hennepin County shopped at a Target store in 1965." — Conf: Medium — Corroboration: 0 — Conflicts: None — Independence: this is the company's selection of a favourable survey printed inside its own shareholder report; the survey document is not held, so the figure is one carrier deep and cannot be audited.
```
```
B1-08 Claim: Company print attributes the 1962 decision to the institution and frames the concept as market logic, naming no person as decider. — Date: 1962 — Source: FY1965 report, Target Stores essay — Source date: 1965 — URL: as B1-01, local L388-394 — Tier: 1 — Class: RETROSPECTIVE INTERPRETATION — Passage: "Target Stores, Inc., was conceived with the knowledge that … there also will be people who wish to take advantage of low margins and convenience shopping through the economies of mass merchandising." — Conf: High (that the text reads this way) — Corroboration: 1 — Conflicts: U.K1 — Independence: the FY1999 genealogy spread ("The Dayton Company enters discount merchandising with the opening of its first Target stores") is the same self-account, later.
```
```
B1-09 Claim: John Geisse is printed in company print as an officer of Target Stores, Inc. in FY1965 (Vice President), FY1966 (Vice President and General Merchandise Manager) and FY1967 (Senior Vice President and General Merchandise Manager), and appears in no later founding-era layer. — Date: 1965-1967 — Source: FY1965/FY1966/FY1967 subsidiary-officer pages — Source date: 1965; 1966; 1967 — URL: archive.org/download/01-target-archive/ per-year layers; local 1965 L1456, 1966 L1449-1457, 1967 L1947-1956 — Tier: 1 — Class: FACT — Passage: "target stores, inc." / "JOHN GEISSE" / "Vice President and General Merchandise Manager" — Conf: High (FY1965, verified TLS); Medium (FY1966/67 rows, UNVERIFIED TLS) — Corroboration: 1 lineage — Conflicts: U.K1 (role is established; "founder" is not) — Independence: officer lists in three consecutive reports of one lineage are one source.
```
```
B1-10 Claim: The parent's own masthead moved from The Dayton Company (FY1965, FY1966 body text) to Dayton Corporation by the FY1967 report, i.e. one year earlier than the probe's table showed. — Date: 1967 — Source: FY1967 report masthead lines 1-2 — Source date: 1967 — URL: archive.org/download/01-target-archive/ per-year layer; local 1967 L1-2 — Tier: 1 — Class: FACT — Passage: "Dayton Corporation | Annual Report /1967" — Conf: Medium (UNVERIFIED TLS) — Corroboration: 1 — Conflicts: corrects the probe's `## Family d` table, which dates "Dayton Corporation" from FY1968 only — Independence: masthead evidence is documentary, not narrative.
```
```
B1-11 Claim: Target-unit sales for fiscal 1967 were printed at $86,901,007, up 43%, with the two Denver stores credited. — Date: 1967 — Source: FY1967 report, Financial Review — Source date: 1967 — URL: as B1-10 layer; local L769-771 — Tier: 1 — Class: FACT — Passage: "Target's sales were $86,901,007, an in- crease of 43 percent. Contributing to Target's increase were its two Denver stores, which" — Conf: Medium (UNVERIFIED TLS; also the only Target-unit sales figure printed anywhere in FY1962-FY1968) — Corroboration: 0 independent — Conflicts: None — Independence: the group total in FY1968 ($141,824,116, verified-TLS layer) is the same lineage with a different denominator, not a second source.
```
```
B1-12 Claim: The Corporation's first public stock offering came in late 1967, when it had 23 stores in five states; by the close of 1970 it had 125 stores in 20 states plus 58 franchised outlets. — Date: 1967-11 / 1970-12 — Source: FY1970 report, Operating Review — Source date: 1970 (layer prints the date "April 16, 1971" at L200) — URL: as B1-01 item; local 1970 L200, L209-212 — Tier: 1 — Class: FACT (corporation level; NOT a Target-unit count) — Passage: "When the Corporation made its first public stock offering in late 1967, it had 23 stores in five states. At the close of 1970 — just a little more than three years later — it had 125 stores in 20 states, along with 58 franchised outlets" — Conf: High — Corroboration: 1 — Conflicts: None — Independence: single source; the em-dash pair is OCR of a spaced dash, quoted here as printed.
```

STATUS: WRITTEN 2026-09-25

## Founder-credit conflict

**Status: unresolved, and now two-sided with one held carrier per side.** The probe recorded K1 as
"company print credits the institution and names no person; the two independent accounts (Douglas
Dayton / John F. Geisse) have no held document." This pass **partially refutes the first half** and
supplies held bytes for the second.

What the held bytes actually say:

* **Company print does name both men — as officers, never as founders.** FY1965 report, "Principal
  Officers of Subsidiaries": `DOUGLAS J. DAYTON, President, Target Stores, Inc.` (L1455) and
  `JOHN GEISSE, Vice President, Target Stores, Inc.` (L1456). FY1966 repeats both under the heading
  `target stores, inc.` (L1449-1457). FY1967 lists `DOUGLAS J. DAYTON / President` and
  `JOHN F. GEISSE / Senior Vice President and General Merchandise Manager` (L1950-1956). Across the
  eleven founding-era layers the string GEISSE appears **only** in FY1965, FY1966, FY1967 (1 hit
  each) and **zero times from FY1968 onward**.
* **Company print never credits any person with the decision.** The 1962 entry is narrated by the
  institution (`The Company entered the discount merchandising field in 1962 with Target Stores,
  Inc.`) and the concept is stated impersonally (`Target Stores, Inc., was conceived with the
  knowledge that…`). The FY1999 genealogy spread is likewise institutional.
* **Side A carrier (Douglas Dayton):** *Twin Cities*/Pioneer Press obituary, 2013-07-06, headline
  form "Target Stores founder Douglas Dayton, governor's uncle … dies". **Still not held** — web
  lead only (probe family e). Against it, in held bytes: FY1965-1967 print him as **President of the
  subsidiary** the parent had already created, i.e. a document that establishes office, not
  origination.
* **Side B carrier (John F. Geisse):** Geisse biography pages (1920-09-01→1992-02-21) presenting him
  as the Target concept's originator, hired from outside the Dayton chain. **Still not held.**
  Against it, in held bytes: FY1965 VP, FY1966 VP + General Merchandise Manager, FY1967 Senior VP +
  GMM — i.e. from the first printed year he runs merchandising, and he is gone from the officer
  pages by FY1968.

**Why the two sides can both be partly right and neither provable:** "founder" is not a category
these documents record. An officer list proves who held the unit in FY1965; an obituary headline
proves what a newspaper asserted in 2013; neither is an instrument of origination. The held
company-side evidence is *consistent with* either narrative and *sufficient for* neither.

**Best-supported reading recorded here (and nothing stronger):** the discount venture was launched in
1962 by **The Dayton Company** as **Target Stores, Inc.**, with **Douglas J. Dayton printed as its
President and John Geisse printed as its merchandising officer from the first year the company lists
them**. No founder is settled. **No averaging, no tie-break.** Confidence in the conflict record
itself: High; confidence in either founder attribution: **Low / UNKNOWN as to "founder."**
Residual uncertainty: neither independent obituary text has been fetched into `sources/`, so the
conflict cannot be adjudicated at Tier 2 from this corpus either.

Also still open, same shape: the **first-store date**. Held text says only `early in 1962` (FY1965
L397); the widely stated **1962-07-01** has **no carrier held anywhere in the eleven layers** —
`July` in a 1962 context appears in none of them. That stays **UNKNOWN until a document exists**.

New this pass, second founder-adjacent conflict: the FY1973 and FY1974 subsidiary rosters print
different parenthetical years for the same unit — `Target (1961)*` (FY1973 L4295) vs `Target (1967)*`
(FY1974 L4634). Neither is legible enough to carry a date claim; recorded as K7, resolved as
**UNKNOWN (OCR-corrupt)**, and explicitly *not* used to move the 1962 date either way.

STATUS: WRITTEN 2026-09-25

## Register rows

Emit-only: **no existing register CSV was opened for writing.** A merge pass applies these.
`stage` is the controlled literal `stage1` on every row. `B1S..` / `B1-..` ids are dossier-local and
must be remapped centrally at merge (§13). Every financial row carries
**CONTEMPORANEOUS** (printed by the report for its own year) or **RESTATED** (a later report's recap
column) in `notes`; a RESTATED row is never counted as corroboration of the CONTEMPORANEOUS one.

### sources.csv (columns: source_id, stage, claim_supported, source_title, author_or_publication, source_type, primary_or_secondary, event_date, publication_date, access_date, url, archived_url, tier, evidence_class, confidence, independence_note, relevant_passage, notes)

```csv
source_id,stage,claim_supported,source_title,author_or_publication,source_type,primary_or_secondary,event_date,publication_date,access_date,url,archived_url,tier,evidence_class,confidence,independence_note,relevant_passage,notes
B1S01,stage1,B1-01 B1-02 B1-03 B1-04 B1-05 B1-07 B1-08 / Q1 Q2 / K1 K2,The Dayton Company Annual Report 1965 (OCR text layer),The Dayton Company,corporate stockholder report,primary,1962;1965,1965,2026-09-25,https://archive.org/download/01-target-archive/1965%20-%20Dayton%20Hudson%20Corp%20%28DH%29_djvu.txt,held locally: sources/corporate_print/1965_dayton_hudson_djvu.txt,1,CONTEMPORANEOUS for 1965 / RETROSPECTIVE for 1962,High,"one lineage; the FY1973 and FY1999 layers repeat the same self-account, which is one source not several","The Company entered the discount merchandising field in 1962 with Target Stores, Inc., which now has five","masthead in bytes reads THE DAYTON COMPANY @ ANNUAL REPORT 1965; the uploader label Dayton Hudson Corp (DH) is wrong for this year (K3); 48050 B; verified TLS"
B1S02,stage1,B1-06 / Q3 / K1,Dayton Company Annual Report 1966 (OCR text layer),The Dayton Company,corporate stockholder report,primary,1966,1966,2026-09-25,archive.org item 01-target-archive per-year DjVuTXT layer (exact URL in file sidecar),held locally: sources/corporate_print/1966_dayton_hudson_djvu.txt,1,CONTEMPORANEOUS,Medium,officer list repeats B1S01 - same lineage,"Total retail area of the seven Target stores now in operation is 889,000 square feet.",TRANSPORT UNVERIFIED TLS so capped at Medium; 43364 B; body head at L184 reads The Dayton Company
B1S03,stage1,B1-10 B1-11 / Q4 Q10 / K1,Dayton Corporation Annual Report 1967 (OCR text layer),Dayton Corporation,corporate stockholder report,primary,1967,1967,2026-09-25,archive.org item 01-target-archive per-year DjVuTXT layer (exact URL in file sidecar),held locally: sources/corporate_print/1967_dayton_hudson_djvu.txt,1,CONTEMPORANEOUS,Medium,unit and group denominators come from two reports of one lineage,"Target sales were $86,901,007, an in-crease of 43 percent",TRANSPORT UNVERIFIED TLS; first layer whose masthead reads Dayton Corporation (L1-2); 45200 B
B1S04,stage1,Q12 Q13 / timeline-1968,Dayton Corporation Annual Report 1968 (OCR text layer),Dayton Corporation,corporate stockholder report,primary,1968,1968,2026-09-25,archive.org item 01-target-archive per-year DjVuTXT layer (exact URL in file sidecar),held locally: sources/corporate_print/1968_dayton_hudson_djvu.txt,1,CONTEMPORANEOUS,High,"group revenue reprinted in B1S05 and B1S08 recap columns - one source, not three","Goods Stores 189,515,025 44 141,824,116 38 33.6",verified TLS (probe-fetched); group heading DISCOUNT AND HARD GOODS STORES at L684
B1S05,stage1,Q6 Q15 / K9 / NYSE listing,Dayton Hudson Corporation Annual Report 1969 (OCR text layer),Dayton Hudson Corporation,corporate stockholder report,primary,1969,1969,2026-09-25,archive.org item 01-target-archive per-year DjVuTXT layer (exact URL in file sidecar),held locally: sources/corporate_print/1969_dayton_hudson_djvu.txt,1,CONTEMPORANEOUS for 1969 / RESTATED for its 1968 column,High,first layer printed under the Dayton Hudson masthead,"Low Margin............. 233,532 189,515",verified TLS; table heads Revenues (00s) and Group 1969 1968 at L998-1000; the 1969 column foots to total revenues 888
B1S06,stage1,B1-12 / Q7 Q20,Dayton Hudson Corporation Annual Report 1970 (OCR text layer),Dayton Hudson Corporation,corporate stockholder report,primary,1967;1970,1970,2026-09-25,https://archive.org/download/01-target-archive/1970%20-%20Dayton%20Hudson%20Corp%20%28DH%29_djvu.txt,held locally: sources/corporate_print/1970_dayton_hudson_djvu.txt,1,CONTEMPORANEOUS,High,corporation-level store counts are not Target-unit counts,When the Corporation made its first public stock offering in late 1967,"verified TLS; on-disk and sidecar both 53023 B while the probe table printed 52736 (see N6); the layer also prints the date April 16, 1971 at L200"
B1S07,stage1,Q7 Q8 / K6,Dayton Hudson Corporation Annual Report 1971 (OCR text layer),Dayton Hudson Corporation,corporate stockholder report,primary,1971,1971,2026-09-25,archive.org item 01-target-archive per-year DjVuTXT layer (exact URL in file sidecar),held locally: sources/corporate_print/1971_dayton_hudson_djvu.txt,1,CONTEMPORANEOUS,Medium,its Five Year Comparisons rows lost every numeric column in OCR,At year,TRANSPORT UNVERIFIED TLS; also prints six openings in 1971 and a plan for 16 in 1972
B1S08,stage1,Q9 Q14 Q18 / K6 K9,Dayton Hudson Corporation Annual Report 1972 (OCR text layer),Dayton Hudson Corporation,corporate stockholder report,primary,1972,1972,2026-09-25,archive.org item 01-target-archive per-year DjVuTXT layer (exact URL in file sidecar),held locally: sources/corporate_print/1972_dayton_hudson_djvu.txt,1,CONTEMPORANEOUS for 1972 / RESTATED for its 1968 five-year column,High,the recap column repeats the FY1968 group figure - same lineage,Target opened 16 new stores within a seven-month period,verified TLS; group revenues $440.4 and $345.8 at L1040
B1S09,stage1,Q5 Q16-Q19 / K6 K7,Dayton Hudson Corporation Annual Report 1973 (OCR text layer),Dayton Hudson Corporation,corporate stockholder report,primary,1969-1973,1973,2026-09-25,archive.org item 01-target-archive per-year DjVuTXT layer (exact URL in file sidecar),held locally: sources/corporate_print/1973_dayton_hudson_djvu.txt,1,RESTATED for 1969-1972 / CONTEMPORANEOUS for 1973,Medium,only layer in the run whose five-year low-margin row survives OCR intact,Target has grown from 11 stores to 46 stores in five years,TRANSPORT UNVERIFIED TLS; Five Year Comparisons at L3970-3997; the store roster prints Target (1961)*
B1S10,stage1,Q1-Q9 cross-check / K6 K7,Dayton Hudson Corporation Annual Report 1974 (OCR text layer),Dayton Hudson Corporation,corporate stockholder report,primary,1962-1973,1974,2026-09-25,archive.org item 01-target-archive per-year DjVuTXT layer (exact URL in file sidecar),held locally: sources/corporate_print/1974_dayton_hudson_djvu.txt,1,RESTATED (retrospective store roster),Medium,a roster of the estate still operating in 1974; one source however many later reports reprint it,Roseville,TRANSPORT UNVERIFIED TLS; the roster heading Target (1967)* contradicts B1S09 Target (1961)* (K7)
B1S11,stage1,context only,Dayton Hudson Corporation Annual Report 1975 (OCR text layer),Dayton Hudson Corporation,corporate stockholder report,primary,1975,1975,2026-09-25,archive.org item 01-target-archive per-year DjVuTXT layer (exact URL in file sidecar),held locally: sources/corporate_print/1975_dayton_hudson_djvu.txt,1,CONTEMPORANEOUS,Medium,digitised by a third-party backfile service not by the company,Dayton Hudson Corporation Annual Report -- 1975,verified TLS; a provenance line names ProQuest Historical Annual Reports
B1S12,stage1,K1 side A,Twin Cities / St Paul Pioneer Press obituary 2013-07-06,unknown - NOT HELD,newspaper,secondary,2013,2013-07-06,NOT ACCESSED,NOT HELD - web lead only from probe family e,none,2,RETROSPECTIVE SOURCE,Low,NOT HELD so it cannot be evidence - a named assertion only,Target Stores founder Douglas Dayton,LEAD ONLY; fetch into sources/documentary/ before any use (U-2)
B1S13,stage1,K1 side B,John Francis Geisse biography pages,unknown - NOT HELD,biographical web page,secondary,1992,UNKNOWN,NOT ACCESSED,NOT HELD - web lead only from probe family e,none,4,RETROSPECTIVE SOURCE,Low,NOT HELD; a Tier-4 lead that must be chased to a Tier 1/2 carrier,presents Geisse as the Target concept originator,LEAD ONLY; unheld (U-2)
B1S14,stage1,K1 and pre-history,Target Corporation Annual Report 1999 (OCR text layer),Target Corporation,corporate stockholder report,primary for 1999 and self-account for 1902-1962,1902-1999,1999,2026-09-25,archive.org item 01-target-archive per-year DjVuTXT layer (probe-fetched),held locally: sources/corporate_print/1999_annual_report_djvu.txt,1,RETROSPECTIVE INTERPRETATION,Low,same lineage as B1S01; a reprinted company history page is one source,George Dayton opens Goodfellows in down,tick-to-blurb pairing unresolved (probe G4); never load-bearing for Stage 1
```

### quantitative.csv (columns: company, stage, date, metric, value, unit, source, source_date, evidence_class, confidence, derived_arithmetic, notes)

```csv
company,stage,date,metric,value,unit,source,source_date,evidence_class,confidence,derived_arithmetic,notes
Target,stage1,1962,target_stores_opened_in_year,4,stores,B1S01 chronology L725-738 (cross-check B1S10 roster L4636-4641),1965,FACT,Medium,,"CONTEMPORANEOUS-as-1965 / RETROSPECTIVE-as-1962; the four are Roseville, Crystal, Duluth and Knollwood-St. Louis Park"
Target,stage1,1963,target_stores_in_operation,UNKNOWN,stores,no held layer prints a 1963 or 1964 Target opening,UNKNOWN,UNKNOWN,UNKNOWN,,"year-end counts printed nowhere held; both store lists jump 1962 to 1965, which is an absence in a list and not a statement"
Target,stage1,1965,target_stores_in_operation,5,stores,B1S01 L189 and L400-401,1965,FACT,High,,"CONTEMPORANEOUS; four in the Minneapolis-St. Paul area plus one in Duluth"
Target,stage1,1966,target_stores_in_operation,7,stores,B1S02 L219,1966,FACT,Medium,,"CONTEMPORANEOUS; the two Denver stores opened October 1966 (B1S02 L355); UNVERIFIED TLS"
Target,stage1,1967,target_stores_in_operation,9,stores,B1S03 L180-182 with B1S02 L217-218,1967,FACT,Medium,,"CONTEMPORANEOUS; Fridley and West St. Paul opened in October and were profitable in the year of opening; UNVERIFIED TLS"
Target,stage1,1968,target_stores_in_operation,11,stores,B1S09 L564-565,1973,FACT,Medium,,"RESTATED - a 1973 report reciting 1968, i.e. company self-narrative recap; UNVERIFIED TLS"
Target,stage1,1969,target_stores_in_operation,17,stores,B1S05 L540-544 added to the B1S09 1968 base,1969,ESTIMATE,Low,"11 (1968 recap base) + 6 opened in 1969 (2 Dallas + 2 Houston + 1 Colorado Springs + 1 St. Louis) = 17","DERIVED; cross-check: group stores 19 (B1S09 L3995) less 2 hard-goods units = 17"
Target,stage1,1970,target_stores_in_operation,24,stores,B1S07 L816 and L831,1971,ESTIMATE,Low,"30 at year-end 1971 minus 6 opened in 1971 = 24","DERIVED; the FY1969 plan to raise its total to 24 is a plan not an actual; the group count 27 (B1S09 L3995) is consistent"
Target,stage1,1971,target_stores_in_operation,30,stores in 11 markets,B1S07 L831,1971,FACT,Medium,,"CONTEMPORANEOUS; UNVERIFIED TLS; the FY1974 roster enumerates only 29 Target stores with opening year up to 1971 - see K6"
Target,stage1,1972,target_stores_in_operation,46,stores in nine states,B1S08 L476-478,1972,FACT,High,,"CONTEMPORANEOUS; 16 openings in a seven-month period, exactly the 16 planned in B1S07 L832"
Target,stage1,1966,target_unit_sales,60770000,USD,B1S03 L769-770 printed percent only,1967,ESTIMATE,Low,"86,901,007 / 1.43 = 60,769,935 - the percent is rounded so the base is approximate to about 1 million","DERIVED and printed nowhere in any held layer; UNVERIFIED TLS"
Target,stage1,1967,target_unit_sales,86901007,USD,B1S03 L769-770,1967,FACT,Medium,,"CONTEMPORANEOUS; the only Target-unit sales figure printed anywhere in FY1962-FY1968; UNVERIFIED TLS"
Target,stage1,1967,low_margin_group_revenue,141824116,USD,B1S04 L1361,1968,FACT,High,,"CONTEMPORANEOUS for 1967 as printed in the FY1968 report; the group is Discount and Hard Goods Stores, NOT Target alone"
Target,stage1,1968,low_margin_group_revenue,189515025,USD,B1S04 L1361 (44 percent of net retail sales),1968,FACT,High,,"CONTEMPORANEOUS; reprinted unchanged as 189,515 in B1S05 and as $189.5m in B1S08 - same lineage restated, never corroboration"
Target,stage1,1968,low_margin_group_stores,13,stores,B1S08 L2374-2384 Five Year Comparisons 1968,1972,FACT,High,,"RESTATED (1968 inside a 1972 recap); the same block prints 1,577 thousand square feet and $120.16 sales per square foot"
Target,stage1,1969,low_margin_group_revenue,233532,USD thousands,B1S05 L998-1003,1969,FACT,High,,"CONTEMPORANEOUS; the column foots: 607,697 + 233,532 + 27,107 + 20,021 = 888,357 total revenues"
Target,stage1,1970,low_margin_group_revenue,289.0,USD millions,B1S09 L3988,1973,FACT,Medium,,"RESTATED (1973 recap of 1970); the FY1970 layer prints no group row at all because its table lost the numeric columns; UNVERIFIED TLS"
Target,stage1,1971,low_margin_group_revenue,345.8,USD millions,B1S08 L1040 with B1S09 L3988,1972,FACT,Medium,,"CONTEMPORANEOUS-as-1971 via the FY1972 report; the FY1973 recap agrees, which is one source restated"
Target,stage1,1972,low_margin_group_revenue,440441000,USD,B1S08 L470 and L1040,1972,FACT,High,,"CONTEMPORANEOUS; group pretax earnings fell to $9,222,000 from $13,749,000, attributed in print to Target performance and start-up costs (L471-482)"
Target,stage1,1973,low_margin_group_revenue,470.3,USD millions,B1S09 L3988,1973,FACT,Medium,,"CONTEMPORANEOUS; UNVERIFIED TLS"
Target,stage1,1969,low_margin_group_stores,19,stores,B1S09 L3995,1973,FACT,Medium,,"RESTATED; equals the derived Target 17 plus 2 hard-goods units; UNVERIFIED TLS"
Target,stage1,1972,low_margin_group_stores,50,stores,B1S09 L3995 with B1S08,1972,FACT,Medium,,"CONTEMPORANEOUS group / RESTATED in the 1973 column; equals Target 46 plus 4"
Target,stage1,1965,parent_net_retail_sales,186166671,USD,B1S01 L169 and L822 with the 1964 comparative 162773739 printed in the same line,1965,FACT,High,,"CONTEMPORANEOUS; whole company NOT Target; the FY1966 figure 189,776,071 is net sales AND rentals, a different denominator"
Target,stage1,1969,parent_net_retail_sales,868335,USD thousands,B1S05 L951 and B1S06 L829,1970,FACT,High,,"CONTEMPORANEOUS in both layers; the FY1970 re-print of the same 1969 figure is one source repeated, not corroboration"
Target,stage1,1968,department_store_group_revenue_as_restated,582923,USD thousands,B1S05 L1004,1969,FACT,High,,"RESTATED for the merged Dayton Hudson scope; the FY1968 report printed 223,276,791 CONTEMPORANEOUS for Dayton Corporation alone (B1S04 L1359) - different entities, see K9"
```

### timeline.csv (columns: company, stage, date_or_range, event, actors, location, source_id, evidence_class, confidence, conflict_ref, notes)

```csv
company,stage,date_or_range,event,actors,location,source_id,evidence_class,confidence,conflict_ref,notes
Target,stage1,1962,"The Dayton Company enters discount merchandising through Target Stores, Inc.",The Dayton Company and Target Stores Inc,Minneapolis-St. Paul area,B1S01,FACT,High,None,stage-1 origin event; narrated in the first person plural by the entity that did it
Target,stage1,1962-early,First Target store opens,"Target Stores, Inc.","Roseville, Minnesota, a suburb north of St. Paul",B1S01,FACT,High,K2,phrase in bytes is early in 1962; month and day UNKNOWN in all eleven layers (N7)
Target,stage1,1965,"Bloomington store opens, bringing Target stores to five (four Twin Cities, one Duluth)","Target Stores, Inc.","Bloomington, Minnesota",B1S01,FACT,High,None,CONTEMPORANEOUS count
Target,stage1,1965,"Parent prints subsidiary officers: Douglas J. Dayton President and John Geisse Vice President of Target Stores, Inc.",The Dayton Company,Minneapolis,B1S01,FACT,High,K1,held Tier-1 carrier for both K1 sides but for ROLES only; neither line says founder
Target,stage1,1966-10,Two Denver stores open as the first Target units outside the Upper Midwest,"Target Stores, Inc.","Denver, Colorado",B1S02,FACT,Medium,None,scheduled for Fall 1966 in B1S01 L190-192; UNVERIFIED TLS
Target,stage1,1967-10,Fridley and West St. Paul open as Target stores numbers eight and nine,"Target Stores, Inc.","Twin Cities, Minnesota",B1S03,FACT,Medium,None,both operated at a profit in the year of opening after absorbing pre-opening expenses; UNVERIFIED TLS
Target,stage1,1967-late,Corporation first public stock offering with 23 stores in five states,Dayton Corporation,UNKNOWN,B1S06,FACT,High,None,month UNKNOWN; printed in the FY1970 Operating Review rather than in a 1967 layer
Target,stage1,1968,Two new Target stores open in St. Louis and Target ends the year with eleven stores,"Target Stores, Inc.","St. Louis, Missouri",B1S04,FACT,High,None,openings CONTEMPORANEOUS (B1S04 L688) but the eleven-store total is a 1973 recap (B1S09 L565)
Target,stage1,1969-07-15,First public DEBT offering of $25 million sinking fund debentures due 1994 priced to yield 7.80 percent,Dayton Hudson Corporation,UNKNOWN,B1S05,FACT,High,None,a different instrument from the 1967 stock offering; do not merge the two
Target,stage1,1969-09-08,Common stock listed on the New York Stock Exchange the same day a new corporate symbol is unveiled,Dayton Hudson Corporation,New York,B1S05,FACT,High,None,dates the Dayton-Hudson leg by document rather than by uploader filename; the merger with The J. L. Hudson Company of Detroit is the same year (B1S06 L228-229)
Target,stage1,1971,Six Target stores opened and Target closes 1971 with 30 stores in 11 markets,"Target Stores, Inc.","Dallas, St. Louis, Twin Cities, Des Moines, Fort Collins",B1S07,FACT,Medium,K6,UNVERIFIED TLS; the FY1974 roster enumerates only five 1971 openings (29 cumulative)
Target,stage1,1961-or-1967,Roster parenthetical year for the Target unit prints differently in consecutive reports,Dayton Hudson Corporation,UNKNOWN,B1S09 and B1S10,UNKNOWN,Medium,K7,not usable as a date for anything and explicitly not used to move 1962
Target,stage1,1972,"Sixteen Target stores opened in seven months; year ends with 46 stores in nine states while group pretax falls to $9,222,000 from $13,749,000",Target Stores Inc and Dayton Hudson Corporation,nine states,B1S08,FACT,High,None,the earnings decline is attributed in print to Target performance and start-up costs
```

### conflicts.csv (columns: company, stage, conflict_id, section, claim_a, claim_a_source, claim_a_date, claim_b, claim_b_source, claim_b_date, why_they_differ, evidence_weight, best_supported_interpretation, residual_uncertainty, confidence)

```csv
company,stage,conflict_id,section,claim_a,claim_a_source,claim_a_date,claim_b,claim_b_source,claim_b_date,why_they_differ,evidence_weight,best_supported_interpretation,residual_uncertainty,confidence
Target,stage1,K1,B1-03 B1-08 B1-09,Douglas Dayton is the founder of Target Stores,Twin Cities / Pioneer Press obituary (NOT HELD),2013-07-06,John F. Geisse originated and headed the Target concept,Geisse biography pages (NOT HELD),UNKNOWN,"company print names both as officers of Target Stores, Inc. from FY1965 and credits neither with the decision",held bytes settle ROLES only: Dayton President and Geisse Vice President in FY1965 and Geisse Senior Vice President and General Merchandise Manager by FY1967; GEISSE appears zero times from FY1968 on,both founder narratives rest on unheld Tier-2/Tier-4 carriers so neither is settled and no averaging is applied,neither independent obituary text is held so the conflict cannot be adjudicated even at Tier 2 from this corpus,Low
Target,stage1,K2,B1-02,The first Target store opened early in 1962 in Roseville,The Dayton Company Annual Report 1965 L397-398,1962,The first Target store opened 1962-07-01,commonly repeated secondary accounts with NO carrier held,UNKNOWN,side A is a held primary and side B has no held document at all,one held layer states the year and the place and refuses the month; a month-with-1962 search returns zero over all eleven layers (N7),keep 1962 with place Roseville and month and day UNKNOWN until a document exists,whether any 07-01 carrier was ever printed is UNKNOWN,High (that it is unresolved)
Target,stage1,K3,entity-lineage key,the 1965 file is a Dayton Hudson Corporation report (uploader file name 1965 - Dayton Hudson Corp (DH)),item 01-target-archive file labels,UNKNOWN,the 1965 masthead in bytes reads THE DAYTON COMPANY @ ANNUAL REPORT 1965,held layer opening lines,1965,the uploader label is applied to every year 1965-1998 regardless of the entity inside the document,text outranks filename and a register built on the file names would misdate the 1969 merger by four years,attribute every figure to the masthead that printed it,none material - the fix is procedural and is applied throughout this file,High
Target,stage1,K6,Q8 Q9,Target had 30 stores at year-end 1971 after six openings in 1971,Dayton Hudson Annual Report 1971 L816 L831,1971,the FY1974 roster enumerates five Target stores with stated opening year 1971 i.e. 29 cumulative,Dayton Hudson Annual Report 1974 L4636-4670,1974,the roster lists only units still operating in 1974 so a closed or renamed unit vanishes from it and one row may also be OCR loss,both are company print of one lineage so neither corroborates the other; CONTEMPORANEOUS outranks RESTATED as to priority but not as to arithmetic,report both: 30 as printed for 1971 and 29 as roster-countable with a one-unit difference whose mechanism is UNKNOWN,which store is missing and which document is at fault is UNKNOWN,Medium
Target,stage1,K7,B1 roster leg,the Target unit carries parenthetical year 1961,Dayton Hudson Annual Report 1973 L4295,1973,the same unit carries parenthetical year 1967,Dayton Hudson Annual Report 1974 L4634,1974,OCR corruption of a small parenthetical inside a dense two-column roster,two consecutive reports disagree and neither is legible enough to carry a date,UNKNOWN; explicitly not used to move the 1962 opening either way,only the original PDF page could settle it (17 Image Container PDFs for 1965-74 exist in the same item),Low
Target,stage1,K9,Q13 Q20,Department Stores revenue for 1968 was 223276791 USD as printed by Dayton Corporation,The Dayton Corporation Annual Report 1968 L1359,1968,the 1968 Department Stores column is 582923 USD thousands,Dayton Hudson Annual Report 1969 L1004,1969,the 1969 column is the merged Dayton Hudson scope including The J. L. Hudson Company of Detroit,RESTATED is never corroboration of CONTEMPORANEOUS; each set foots to its own scope (each restated 1968 set sums to 811981),print both each labelled with the entity whose report printed it,which consolidation date inside 1969 produced the wider column is not established by these layers,High
```

### data_gaps.csv (columns: company, stage, gap, why_missing, importance, best_available_evidence, confidence, follow_up_task)

```csv
company,stage,gap,why_missing,importance,best_available_evidence,confidence,follow_up_task
Target,stage1,"Target-unit (not group) sales for 1962-1965, 1968 and 1970-1972",the reports printed the discount-and-hard-goods GROUP for those years and named Target dollars only for 1967,High,FY1967 prints Target sales at 86901007 (B1S03) and FY1968 prints the group at 189515025 (B1S04),Medium,U-3 HathiTrust and Google Books for Dayton Corporation prospectus and divisional schedules; U-8 XBRL cannot reach this window
Target,stage1,month and day of the first Target store opening,held company text says only early in 1962 and a month-with-1962 search returns zero over eleven held layers,High,B1S01 L397-398,High,U-4 Minneapolis Star Tribune and St Paul Pioneer Press 1962 back-files; U-2 obituary fetches
Target,stage1,store openings in 1963 and 1964,no held layer enumerates a 1963 or 1964 Target opening,Medium,absence in two lists of one lineage (B1S01 chronology and B1S10 roster),Medium,re-read the 1965 chronology against the item 1965 PDF image leg; U-3 for 1963-64 print
Target,stage1,"numeric columns of the Five Year Comparisons tables in FY1969, FY1970 and FY1971",OCR dropped the figure columns leaving row labels only (FY1971 L2298-2307),Medium,the FY1973 five-year row survives intact and supplies 1969-1972 (B1S09 L3988 L3995),Medium,fetch the FY1971 or FY1973 PDF leg or a ProQuest copy of the report and re-OCR
Target,stage1,any document before FY1965 (the 1902-1961 pre-history),the item OCR run starts at FY1965 (probe N3 proven from held item metadata) and no family returned an earlier document,High,only the FY1999 retrospective genealogy spread (B1S14) which is company self-account,Low,U-3 HathiTrust for Dayton Company reports FY1955-FY1964; U-1 auction and museum ephemera
Target,stage1,held independent primary for K1,both founder-credit carriers are web leads not bytes,High,officer pages B1S01 L1455-1456 and B1S03 L1950-1956 which establish roles only,High,U-2 fetch the 2013-07-06 obituary and a Geisse obituary into sources/documentary/ with sidecars
Target,stage1,verified-TLS status of five layers (FY1966 FY1967 FY1971 FY1973 FY1974),verified TLS failed with CERTIFICATE_VERIFY_FAILED certificate expired so the fetch used --insecure,Medium,sidecars on all five stamp transport UNVERIFIED TLS,High,re-fetch the same five URLs after repairing the local CA store and re-stamp; until then every claim resting only on them stays Medium
```

STATUS: WRITTEN 2026-09-26 (target-s1-records) — all five register blocks emitted here, no register
CSV opened or edited; a merge pass applies them.

## Nulls and UNANSWERED

**NULLs (over bytes held on this machine and read this session; the eleven founding-era layers total
781,995 chars of OCR):**

- **N1 (NULL):** a month-name-with-1962 pattern (any month within 25 characters of `1962`, plus the
  `1962 + 1st/first` form) → **0 hits in all eleven layers**. `July` occurs 10 times across the run
  (FY1965 lease notes, FY1968 Hudson's Oakland Mall, FY1969 debt offering, FY1971 Toledo, FY1975) and
  **never with a 1962 Target opening**. The 1962-07-01 date therefore has no carrier here (K2).
- **N2 (NULL):** `Goodfellow` = **0** and `\bDey\b` = **0** across the eleven layers (the probe tested
  six; the count now covers eleven). `Dey Brothers` remains **unestablished**, and the EDGAR full-text
  zeros over 1940-1995 stay an **index floor (2001)**, never a null on the entity.
- **N3 (NULL, count not absence):** `GEISSE` = **3** hits in the whole run — FY1965, FY1966, FY1967 —
  and **0 from FY1968 onward**; `DOUGLAS J. DAYTON` = 18 hits across the eleven layers. These are
  name-presence counts in officer listings, not founder evidence either way.
- **N4 (NULL):** no held layer prints Target-**unit** sales for 1962-1966, 1968 or 1970-1972; the only
  unit figure in FY1962-FY1968 is 1967's `$86,901,007` (FY1967 L769). Everything else is group scope.
- **N5 (NULL, rendering):** the `Five Year Comparisons` blocks in FY1969 (L1895-1909), FY1970
  (L2316-2322) and FY1971 (L2298-2307) print row labels with **no numeric columns** — absent from the
  OCR, not proven absent from the report; FY1973's equivalent row survived intact.
- **N6 (provenance correction):** the probe's table lists the FY1970 layer at 52,736 B; the file on
  disk and its sidecar both say **53,023 B**. Logged so no later pass re-imports the wrong byte count.
- **N7 (catalog-level NULL, re-read from held metadata):** the item's text-layer listing read this
  session runs **1965→2024**; nothing before FY1965 exists in `01-target-archive`.

**UNANSWERED / not-null (never reportable as absence):**

- **Verified TLS on the five new layers FAILED** — `CERTIFICATE_VERIFY_FAILED … certificate has
  expired` for `archive.org` on FY1966/67/71/73/74, then succeeded with `--insecure`. The route is
  alive; the trust store is not. Bytes are held and readable, transport unverified → **Medium cap**.
- **`ia_text.py fetch --id 01-target-archive` cannot answer this brief**: `fetch()` writes
  `<item>_djvu.txt` into `sources/periodicals/` and, through `text_layer_names()`, would have returned
  the **largest** of the item's 62 text layers — a 2024 report — as one cached file. Per-year
  sub-files had to be addressed with the script's own `ocr_url()` + `get()` from the held metadata
  listing. **Tool limitation for the orchestrator, not an evidence finding**, and a live trap: an
  agent running the briefed command would hold the wrong year while believing it held FY1966.
- The FY1965 and FY1968 mastheads sit under library-stamp OCR noise in the first lines
  (`VEEVECAND PUSLIC LIBRARY`, `Tld NOWWWYOdYOD`), so an automated masthead read at L1 fails and the
  entity must be read from deeper lines (FY1965 L757; FY1966 L184). FY1968's masthead itself was **not
  re-read this session** — only its body group tables — so the FY1968 entity attribution rests on the
  probe's line plus the body text, and is flagged rather than reused as fresh.
- **Not attempted inside this budget:** the item's 17 PDF legs, `sec_intake.py facts`, HathiTrust /
  Google Books, local newspapers, the two obituary texts. All are in `## Untried`, none is a null.

STATUS: WRITTEN 2026-09-25

## Untried

- **U-1** The item's own **PDF legs** (`01-target-archive` holds 17 Image Container PDFs for
  1965-74/1976/1985-86/1990-91/1994): re-OCR the FY1971 and FY1973-74 roster pages to settle **K6**
  (the one-store 1971 difference) and **K7** (`Target (1961)*` vs `(1967)*`), and the FY1969-71
  five-year tables for **N5**. Highest value per call remaining on this company.
- **U-2** Fetch the two unheld K1 carriers into `sources/documentary/` with sidecars — the
  2013-07-06 *Twin Cities*/Pioneer Press Douglas Dayton obituary and a Geisse obituary (NYT
  1992-02) — so founder credit can be adjudicated rather than merely recorded.
- **U-3** HathiTrust / Google Books for `Target Stores, Inc.` 1962-66 and for Dayton Company reports
  FY1955-FY1964 (needs `--use-curl` plus a `target` task set in `tools/queries.json`, which does not
  exist); still the route most likely to lift the tier from T2 to T1.
- **U-4** Minneapolis *Star Tribune* / *St. Paul Pioneer Press* 1961-08→1962-12 for the Roseville
  opening: the only route to a **day**, and the only way K2 stops being UNKNOWN.
- **U-5** A **second carrier** for the same years: the probe's eleven layers are one uploader's item,
  so every Stage-1 record is one lineage. Search `fund-and-stock-reports` for independently digitised
  Dayton Company reports FY1962-FY1964.
- **U-6** `sec_intake.py facts` and the FY1993 10-K selected-data table (probe U-8): the Tier-1 bridge
  leg back toward the founding decade, still never fetched.
- **U-7** EDGAR name→CIK for predecessor registrants (`dayton dry goods`, `j.l. hudson`,
  `dayton company`), blocked by HTTP 503 in the probe: until it runs, "one registrant line only" is
  the EDGAR record's limit, not a proof that no predecessor filed.
- **U-8** Re-fetch the five UNVERIFIED-TLS layers after the local CA store is repaired, to lift the
  Medium cap on Q3-Q8, Q16-Q19 and the FY1974 roster cross-check.

STATUS: WRITTEN 2026-09-25

