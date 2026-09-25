# A3 — Walmart Audited Financial Series, FY1962–FY1980 (contemporaneous vs restated register)

**Dataset:** THE FOUNDER'S PLAYBOOK — forensic longitudinal reconstruction
**Company:** Walmart (Ben Franklin era through the first public years) — `company_002_walmart`
**Stage:** 1
**STATUS — SECOND PASS COMPLETE: 39 claim records on disk (A3-001…A3-039), verified by read-back, no
duplicate record IDs.** Write-first gate observed (§14 rule 1): the file was created with its full section
skeleton plus 7 real records on the first write call, before any mining of the five new documents; records
were then appended after each fiscal year was mined (FY1978 → FY1977 → FY1974 → FY1975 → FY1979 → the
FY1972/73/76 re-witness → the pre-FY1972 null), never accumulated in scratch. Web budget consumed:
**0 WebSearch, 0 WebFetch.** Nothing in `../sources/` was opened for writing, moved, renamed, pruned or
tidied; A2 and every other dossier untouched (§14 rule 4). **Register totals for FY1962-FY1980: 9 years
(FY1972-FY1980) now have a contemporaneous witness for their earnings line, of which FY1975 does NOT for
its net-sales top line (derived from its own table's other rows, A3-023); 5 years gained contemporaneity
for the first time in this pass (FY1974, FY1975, FY1977, FY1978, FY1979); 4 years remain restated-only
(FY1968, FY1969, FY1970, FY1971 — no report for any of them exists in the corpus); 6 years are EMPTY
(FY1962-FY1967).**
**File role:** register of record for the audited series, FY1968–FY1980 (earlier years as far as
evidence allows). **A3 supersedes parts of `A2_chronology_finance.md` §"Audited series" by being a
later, better-evidenced pass. A2's 133 records stay intact as the audit trail; nothing in A2 was
edited, deleted or tidied** (method §14 rule 4).
**Hindsight firewall (§2):** no record in this file states or implies that the later chain was
foreseeable at any earlier date. Post-1972 documents are never presented as witnesses to 1962.
**Confidence scale (§3):** High = 2+ independent lineages or a primary document; Medium = one
reliable source; Low = conflicting, vague, or retrospective-only; UNKNOWN = no evidence recovered.

---

## 0. Working method for this dossier, and the write-first log

Rule obeyed: this file was created on the first write call, containing its full section skeleton plus
real records, **before** any further mining of the five new documents. Records are appended after each
fiscal year is mined, never accumulated in scratch.

- **Surgical scope.** This dossier may create/modify exactly one file: itself. Nothing under
  `../sources/` was opened for writing, moved, renamed, pruned or "tidied". All nine
  `WALMART_AR_*.txt` files were read read-only.
- **Web budget: 0 WebSearch, 0 WebFetch so far.** Every document needed for FY1968–FY1980 is already
  on disk. Any gap that needs the network is recorded `UNTRIED` instead of fetched (see §Data gaps).
- **What changed underneath A2.** A2 built its series from four printed reports on disk
  (FY1972, FY1973, FY1976, FY1980) and discovered at COR-A2-10 that the Internet Archive
  corporate-print run is contiguous **FY1972→FY1998**. Five more reports have now been downloaded —
  FY1974, FY1975, FY1977, FY1978, FY1979. The consequence is exactly the one A2 predicted: fiscal years
  it could only state from a **later report's** summary table now have a **contemporaneous** witness,
  and some of A2's "High" rows must be re-labelled as **value-changing** rather than merely
  basis-changing.

### The point of this file (read before using any row)

Two labels are used on **every** figure, and they are not interchangeable:

| Label | Meaning | Evidential status |
|---|---|---|
| **CONTEMPORANEOUS** | The value is printed in the report **for that fiscal year** — the document whose own fiscal year the number describes, signed within weeks of the year end | registrant self-report, auditor-attested, made at the time. Still ONE lineage, but the earliest possible witness for the number |
| **RESTATED (in `<document>`)** | The value is printed in a **later** report, in a summary column or comparative column looking backwards | retrospective within the same lineage. It may differ from what the year itself reported, and when it does the difference is itself evidence |

A restatement is **never** presented here as a primary. Where both exist, both rows are kept and any
disagreement is surfaced in `## Contradictions`, not reconciled away.

**Fiscal basis, stated once.** Wal-Mart Stores, Inc. reported a **fiscal year ending 31 January**,
labelled here FYnn by its end date: FY1972 = 1971-02-01 → 1972-01-31. Company timelines and popular
accounts that label the same numbers by **calendar** year are off by one: the corporate page's
"1967 — 24 stores, $12.7 million" is **FY1968**; "1972 — 51 stores, $78 million" is FY1972 as printed.
A2 establishes this mapping (its §"Audited series" preamble) and A3 keeps it. §2 below records what
each report itself says about the 31-January / 52-53-week question, because that convention matters to
every year-over-year growth rate in §4.

**Line anchors.** Citations are to the saved file's own line numbers (e.g.
`WALMART_AR_1978.txt L1869-1910`) so any figure can be re-walked byte-for-byte. Passages are quoted
**verbatim as OCR'd** — including garble — with runs of whitespace collapsed. Where a printed line is
too damaged to support a reading, the record says so and confidence drops; garble is not laundered
into a fact.

---

## 1. Evidence base on disk (nine printed reports + the surrounding corpus)

| Document on disk | Own fiscal year | Dated / signed | Machine-readable completeness (per its own provenance header) | What it can witness |
|---|---|---|---|---|
| `WALMART_AR_1972.txt` | FY1972 (FYE 1972-01-31) | presidential letter 1972-03-22 | in corpus since A2 | FY1972 contemporaneous; FY1968–FY1971 via its own 5-Year Summary (same-document, 1972-dated) |
| `WALMART_AR_1973.txt` | FY1973 | report date 20 March 1973 | in corpus since A2 | FY1973 contemporaneous; FY1969–FY1972 retrospective |
| `WALMART_AR_1974.txt` | FY1974 | new to A3 | complete scan; five-year table fully legible; **audited statement pages interleave and drop cells** | FY1974 money from its Five Year Progress Report, NOT from statement-page row order |
| `WALMART_AR_1975.txt` | FY1975 | new to A3 | complete scan (21 pp) but **worst of the five for current-year money**: FY1975 own-column numerals dropped on every audited statement page; Five Year Summary Net sales row carries **four values against five column heads** | FY1975 net income/EPS/opex/taxes contemporaneous; **FY1975 net sales, total assets, stockholders' equity NOT recoverable from this text layer** |
| `WALMART_AR_1976.txt` | FY1976 | report date 26 March 1976 | in corpus since A2 | FY1976 contemporaneous; FY1972–FY1975 retrospective |
| `WALMART_AR_1977.txt` | FY1977 | new to A3 | complete scan; text layer complete but **COLUMN-MAJOR REFLOW** — labels print first, values follow as stacked year blocks | FY1977 contemporaneous if pairing is done by position, never by adjacency |
| `WALMART_AR_1978.txt` | FY1978 | new to A3 | **cleanest layer of the five — treat as the reference copy for FY1970–FY1978** (nine-year table, statement columns side by side) | FY1978 contemporaneous; FY1970–FY1977 nine-year-table witness |
| `WALMART_AR_1979.txt` | FY1979 | new to A3 | complete scan (24 pp); **ten-year summary numeric cells are the one genuinely unreadable block**; two-year comparison, income statement, balance sheet, notes, market-price tables all render | FY1979 (and FY1978 comparative) contemporaneous **from its own audited statements**; NOT from its ten-year table |
| `WALMART_AR_1980.txt` | FY1980 | report date 1 April 1980 | in corpus since A2 | FY1980 contemporaneous; the SFAS-13 restatement source for FY1971–FY1978 |

Non-report material carried forward from A2 and the retest, unchanged: the museum/press page
`walmart_museum_page.html`, the corporate-history extract, the probe/IA enumeration JSONs, the two
stub leads (`STUB_LEAD_DTIC_ADA345567.md`, `STUB_LEAD_samwaltoninsides00vanc.md`) and the failed-probe
`.bin` artefacts. A3 does not re-mine those; it mines the reports.

---

## 2. Fiscal-year-end convention as each document states it

A3-018 Claim: **All nine reports on disk state a fixed 31-January year end, and NOT ONE of them states a
52/53-week convention.** Headings read "Years ended January 31," (`WALMART_AR_1979.txt` L1893 region),
"Year Ended January 31, 1978" (`WALMART_AR_1978.txt` L1748), "January 31, 1974 and 1973" (notes heading,
`WALMART_AR_1974.txt`), "Nine-Year Summary … 1978 1977 / 1976 1975 1974 1973 1972 1971 1970" with the
income-statement head "Years ended January 31," — Date: FY1972–FY1980 — Source: nine files, heading
lines as cited; a targeted search of all nine files for `52 weeks|53 weeks|52/53|weeks ended|fiscal year
ends|additional week` returns **no matches** — Source date: 1972-03-22 → 1980-04-01 — URL: see each
file's header — Archived: on disk — Tier: 1 — Class: FACT (that no such language is present) —
Passage: "Year Ended January 31, 1978" — Conf: High — Corroboration: 1 lineage, 9 documents —
Conflicts: none. **Consequence for every comparison in §5: Wal-Mart's years in this window are
calendar-fixed, not retail-4-5-4, so no year is 52 vs 53 weeks and no growth rate is distorted by a
shifted year end. The only length effect is the leap day: FY1969, FY1973 and FY1977 each contain 29
February and so run 366 days against 365 in every other year of the series — a +0.27% tailwind on those
three growth rates and on sales-per-square-foot for those years. That is the whole size of the effect
and it is stated rather than ignored.**

A3-019 Claim: **The FY1974 report dates the NYSE listing contemporaneously**: "In October 1970, Wal-Mart
Stores, Inc. became a publicly-held corporation and became traded in the over-the-counter market.
August 25, 1972, the Company's stock was listed and began trading on the New York Stock Exchange" —
Date: 1972-08-25 — Source: `WALMART_AR_1974.txt` L441-445 — Source date: 1974-03-21 — URL: as A3-014 —
Archived: on disk — Tier: 1 — Class: FACT — Passage: "August 25. 1972, the Com- pany's stock was listed
and began trading on the New York Stock Exchange." — Conf: High — Corroboration: 1 lineage; the FY1979
report repeats the market status in the present tense ("the Company's stock (WMT) is traded on the New
York Stock Exchange") — Conflicts: none. **A2 dated only the 1970-10-08 offering (W-03) and recorded "no
pre-1976 price data exists in this corpus" (W-54). Both stand; but A2 carried no listing date at all,
and the exchange-transition fact — OTC from October 1970, NYSE from 1972-08-25 — is now on disk in the
registrant's own words with the market it names. This matters for any later price series: a 1972-08-25
break is a venue change, not a stock event.**

A3-020 Claim: The word **"pro forma"** in the FY1972/FY1973/FY1974 five-year tables is the registrant's
own label for its pre-1972 earnings rows, and the FY1974 report's Note 1 states an earnings-per-share
basis that is not the later reports' basis: "Per share amounts are based on average outstanding shares,
stock options and warrants. The average stock options and warrants outstanding have been reduced by
shares assumed to have been purchased with proceeds from such options and warrants under the treasury
stock method." — Date: FY1974 — Source: `WALMART_AR_1974.txt` L1305-1315 (Note 1) and L110-174 (table
heads "Pro forma net income", "Pro forma net income per share") — Source date: 1974-03-21 — URL: as
A3-014 — Archived: on disk — Tier: 1 — Class: FACT — Passage: "Pro forma net income per share $.23 $.30
$.47 $.70 $.93" — Conf: High — Corroboration: 1 lineage — Conflicts: none, but **the label is the point:
FY1968–FY1971 income was never an audited registrant result — the registrant group did not exist until
the 1970-02-01 pooling (W-04) — and A2's §"Audited series" table describes those rows as
"registrant reports; amounts as printed" without carrying the "pro forma" qualifier into the row label.
See `## Outbound corrections` COR-A3-06 and the attestation note (§6).**

A3-001 Claim: Nine Wal-Mart Stores, Inc. printed annual reports are now physically present on disk,
covering **FY1972 through FY1980 continuously with no missing year** — Date: 1972-03-22 → 1980-04-01
(document dates) — Source: `../sources/periodicals/WALMART_AR_1972.txt`, `_1973`, `_1974`, `_1975`,
`_1976`, `_1977`, `_1978`, `_1979`, `_1980` — Source date: retrieved 2026-09-24 (five interior years),
2026-09-24 15:20 (four originals) — URL: see each file's own `SOURCE URL` header line —
Archived: yes, on disk — Tier: 1 — Class: FACT (about the corpus) —
Passage: "COMPLETENESS: **complete scan, no page absent, but PARTIAL-WITH-GAPS as machine-readable
text.**" (FY1974 header) — Conf: High — Corroboration: 1 corpus, 9 artefacts; each byte-matched to the
metadata-declared size at retrieval — Conflicts: none. **This is the structural change relative to A2:
the printed-run hole inside FY1972–FY1980 is closed as a download gap.**

A3-002 Claim: The FY1974 report's text layer is **complete as a scan but partial as machine-readable
text**, and its own registrar header forbids reading FY1974 money from the audited statement pages —
Date: 1974 — Source: `WALMART_AR_1974.txt` L1-30 (provenance header) — Source date: 2026-09-24 —
URL: https://archive.org/details/1974-annual-report-for-walmart-stores-inc — Archived: on disk,
SHA-256 e0781cac…90a06 — Tier: 1 (document) / provenance note is this project's own — Class: FACT —
Passage: "the income-statement "Net sales" row prints only the comparative figure and prints it wrong
("$124,059, 141" for FY1973's $124,889,141) with FY1974's own top line missing from that row" —
Conf: High — Corroboration: 1 (this project's retrieval log) — Conflicts: none; **operational rule
adopted: FY1974 money comes from the Five Year Progress Report or FY1975's comparative column.**

A3-003 Claim: The FY1975 report is the **worst of the five for current-year money**: FY1975's own
column numerals are dropped on every audited statement page, and its Five Year Summary prints four
Net sales values against five column heads — Date: 1975 — Source: `WALMART_AR_1975.txt` L1-30 —
Source date: 2026-09-24 — URL: https://archive.org/details/1975-annual-report-for-walmart-stores-inc —
Archived: on disk, SHA-256 79b8603b…31189c — Tier: 1 — Class: FACT — Passage: "**FY1975's net sales,
total assets and stockholders' equity are NOT recoverable from this text layer**" — Conf: High —
Corroboration: 1 — Conflicts: **raises a live digit ambiguity it also records**: "the FY1976/FY1977
reports print that year as $226,209 vs $236,209 elsewhere, a 2/3 digit ambiguity" → U-A3/1.

A3-004 Claim: The FY1977 report's text layer is complete but reflowed **column-major**, so label→value
pairing must be reconstructed by position within a year block — Date: 1977 — Source:
`WALMART_AR_1977.txt` L1-30 — Source date: 2026-09-24 — URL:
https://archive.org/details/1977-annual-report-for-walmart-stores-inc — Archived: on disk, SHA-256
f398a40d…ba500 — Tier: 1 — Class: FACT — Passage: "income statement: labels 1831-1885, then the FY1977
block 1887-1928, then the FY1976 block 1931-1969" — Conf: High — Corroboration: 1 — Conflicts: none,
but every FY1977 figure in §3 is read with this rule applied and is marked accordingly.

A3-005 Claim: The FY1978 report is the **cleanest layer of the five and is used here as the reference
copy for FY1970–FY1978**; its gaps are typographic, not structural — Date: 1978 — Source:
`WALMART_AR_1978.txt` L1-30 — Source date: 2026-09-24 — URL:
https://archive.org/details/1978-annual-report-for-walmart-stores-inc — Archived: on disk, SHA-256
10a30c39…62978f — Tier: 1 — Class: FACT — Passage: "No audited-statement page and no column of the
nine-year table is missing." — Conf: High — Corroboration: 1 — Conflicts: none. **Consequence: the
nine-year table in this one document is the single best contemporaneous-window witness for FY1972–FY1977
that A2 did not have.**

A3-006 Claim: The FY1979 report is complete (24 numbered pages) but its **ten-year summary numeric
cells are unreadable**, and its own header directs series work to FY1978's nine-year table and to
FY1979's own audited statements — Date: 1979 — Source: `WALMART_AR_1979.txt` L1-30 — Source date:
2026-09-24 — URL: https://archive.org/details/1979-annual-report-for-walmart-stores-inc — Archived:
on disk, SHA-256 ad6958cf…c7095c — Tier: 1 — Class: FACT — Passage: "**Do not read multi-year series
out of this file's ten-year table**" — Conf: High — Corroboration: 1 — Conflicts: none. The header
also notes "the file's own 1978 restatement disclosures are legible and are themselves the evidence
that the FY1979 report is a restating document for prior years" → §5 auditor note.

A3-007 Claim: Every figure in A2's audited series is for a fiscal year ended 31 January and A3
inherits that basis; A3's remaining task is to record whether each report itself states a 52/53-week
convention — Date: 1968-01-31 → 1980-01-31 — Source: A2 §"Audited series" preamble + the reports' own
table heads ("YEARS ENDED JANUARY 31", `WALMART_AR_1972.txt` L48-64) — Source date: 1972-03-22 /
2026-09-24 — URL: as cited — Archived: on disk — Tier: 1 — Class: FACT (basis) + UNKNOWN (whether any
report states a 52/53-week rule) — Passage: "5 YEAR FINANCIAL SUMMARY OPERATING RESULTS .._ YEARS
ENDED JANUARY 31" — Conf: High (31-January year end), UNKNOWN (52/53-week language) pending the §2
mine recorded in A3-011.

---

## 3. The year-by-year series, FY1962–FY1980, with the contemporaneous/restated flag per figure

**Append-after-each-year register.** Records A3-008 onward. Section 3.1 = FY1978 mine (reference copy);
3.2 = FY1977; 3.3 = FY1974; 3.4 = FY1975; 3.5 = FY1979; 3.6 = FY1972/73/76 re-witness;
3.7 = pre-FY1972.

### 3.1 FY1978 mine — `WALMART_AR_1978.txt`, Nine-Year Summary (p.13, file L1364-1743)

The table head reads **"(Dollar amounts in thousands except lor [sic] per share data)"** — that is the
stated unit for every row below unless a row says otherwise. Current-year pair FY1978/FY1977 prints
inline (L1368-1420); FY1976→FY1970 print as a stacked run under column heads at L1434-1446
(`1976 1975 1974 1973 *972 "971 1970` — two column heads are OCR-damaged, resolved by position).

**Row→column pairing was verified arithmetically, not assumed.** Every FY1970–FY1977 column satisfies
`net sales + leased-dept rentals − cost of sales − operating expense − interest = taxes + net income`,
and every FY1971–FY1976 return row satisfies the table's own footnote `**On beginning of year balances`
against the table's own prior-year totals. Eighteen independent checks close, which is why A3 treats
this table as the reference copy rather than as a garble risk.

A3-008 Claim: **FY1978 (FYE 1978-01-31) as printed in its own report** — net sales $678,456 thousand;
leased department rentals and other income — net 7,767; cost of sales 503,825; operating, selling and
general and administrative expenses 137,939; interest and debt expense 2,273; taxes on income 20,300;
net income 21,886; primary EPS $1.53; fully diluted 1.46; dividends .16; **stores in operation at the
end of the period 195** — Date: 1977-02-01→1978-01-31 — Source: `WALMART_AR_1978.txt` L1368-1394 —
Source date: report of 14 April 1978 (auditor's report date, per the file's own provenance block) —
URL: https://archive.org/details/1978-annual-report-for-walmart-stores-inc — Archived:
sources/periodicals/WALMART_AR_1978.txt — Tier: 1 — Class: FACT — Passage: "Net sales $678,456 $478,807
… Net income 21,886 16.546 … Stores in operation at the end of the period 195 153" — Conf: High —
Corroboration: **1 lineage (registrant+Arthur Young); basis = CONTEMPORANEOUS for FY1978**, re-printed
FY1979/FY1980 — Conflicts: FY1980's SFAS-13 restated net income for the same year is $21,191k →
U-A3/4. **NEW WITNESS: A2 had FY1978 net sales and net income only from `WALMART_AR_1980.txt` L89/L94
(restated basis, 1980-dated); FY1978's own report now states them.**

A3-009 Claim: FY1978 financial position as printed in the FY1978 report — current assets $150,986k;
net property, plant and equipment 55,402; total assets 206,691; current liabilities 73,083; long-term
debt 21,489; **long-term obligations under capital leases 10,904**; stockholders' equity 98,943 —
Date: 1978-01-31 — Source: `WALMART_AR_1978.txt` L1396-1410 — Source date: 1978-04-14 — URL: as A3-008 —
Archived: on disk — Tier: 1 — Class: FACT — Passage: "Long-term obligations under capital leases 10,904
4,087 … Stockholders' equity 98,943 66,183" — Conf: High — Corroboration: 1 lineage; CONTEMPORANEOUS —
Conflicts: none. Note the capital-lease line does not exist for FY1970–FY1976 in this table (those cells
print `—`), so the FY1977 reclassification in A3-011 is the earliest split-out of that obligation.

A3-010 Claim: **FY1978's own management text states a same-store (comparable-store) growth figure and a
gross margin, both as printed rather than derived**: "During 1977 [i.e. the fiscal year ended 1978-01-31],
Wal-Mart continued its sales growth with an increase of 42 percent … Comparable stores sales (excluding
the effect of new stores) increased 17 percent compared to the same period a year ago"; and "Gross margin
decreased for the year to 25.7 percent from 26.3 percent in 1977" — Date: FY1978 — Source:
`WALMART_AR_1978.txt` L1748-1778 ("Management's Analysis of Summary of Earnings / Year Ended January 31,
1978") — Source date: 1978-04-14 — URL: as A3-008 — Archived: on disk — Tier: 1 — Class: FACT (company's
own stated ratios) — Passage: "Comparable stores sales (excluding the effect of new stores) increased 17
percent" — Conf: High that the company stated it; **the comparable-store population and its dollar base
are not defined in the document ⇒ the metric's denominator is UNKNOWN (§5 rule)** — Conflicts: none.
The same passage states store space: "giving us 195 stores and 8,500.000 [sic, = 8,500,000] square feet
of floor space in operation at year end in comparison with 153 and 6.500,000, respectively, at the same
time a year ago" — i.e. **FY1978 = 8,500,000 sq ft and FY1977 = 6,500,000 sq ft, CONTEMPORANEOUS**, plus
"30 new Wal-Mart stores and the expansion and/or relocation of 10 others … we acquired a group ot [sic]
16 stores. Four stores were closed during the year".

### 3.2 FY1977 mine — `WALMART_AR_1977.txt`, Eight-Year Summary (file L1400-1460) and Chairman's Message

A3-011 Claim: **FY1977 (FYE 1977-01-31) as printed in its own report**, Eight-Year Summary — net sales
$478,807k; leased-department rentals 5,393; cost of sales 352,669; operating/S&G/administrative expense
97,807; interest and debt expense 1,891; taxes on income 15,287; net income 16,546; primary EPS $1.19;
fully diluted 1.12; dividends .085; stores 153; current assets $99,493k; net PP&E 33,091; total assets
133,158; current liabilities 41,929; **long-term debt 23,245**; stockholders' equity 66,183; current
ratio 2.4; inventories/net working capital 1.5; return on assets 16.5; return on equity 34.1 — Date:
1976-02-01→1977-01-31 — Source: `WALMART_AR_1977.txt` L1400-1460 (file lines; column-major reflow per
A3-004, pairing verified by the FY1978 report's independent reprint) — Source date: auditor's report
dated 1 April 1977 — URL: https://archive.org/details/1977-annual-report-for-walmart-stores-inc —
Archived: sources/periodicals/WALMART_AR_1977.txt — Tier: 1 — Class: FACT — Passage: "Net sales $478,807
$340,331 … Long-term debt 23,245 17,531 … Return on Stockholders1 [sic] Equity** 34.1 31.2" —
Conf: High — Corroboration: 1 lineage; CONTEMPORANEOUS for FY1977; the same values re-print verbatim in
the FY1978 nine-year table (A3-008 source) — **same lineage, second printing, not a second source.** —
Conflicts: A2's FY1977 rows (`WALMART_AR_1980.txt` L89/L92/L94) give net sales 478,807 ✓ but **pre-tax
income 30,857 and net income 16,039, which the FY1977 report's own columns do not support** → U-A3/4.

A3-012 Claim: **The FY1978 report reclassified FY1977's long-term debt, and the two prints reconcile
exactly**: FY1977 long-term debt = **23,245** as printed in the FY1977 report, vs **19,158 plus 10,904**
for FY1978 and **4,087** for FY1977 in the FY1978 report's split-out capital-lease line —
19,158 + 4,087 = 23,245 — Date: 1977-01-31 — Source: `WALMART_AR_1977.txt` L1400-1460 and
`WALMART_AR_1978.txt` L1406-1408 — Source date: 1977-04-01 / 1978-04-14 — URL: as cited — Archived: on
disk — Tier: 1 — Class: FACT (arithmetic self-check) + ESTIMATE/DERIVED for the sum
(`19,158 + 4,087 = 23,245`) — Passage: "Long-term obligations under capital leases 10,904 4,087" —
Conf: High — Corroboration: 1 lineage — Conflicts: none; **recorded as a BASIS CHANGE, not a value
change**: any debt/equity ratio for FY1977 must state which print it uses, because 23,245/66,183 = 0.351
and 19,158/66,183 = 0.289 are different leverage pictures for the same balance-sheet date.

A3-013 Claim: **The FY1977 report states headcount**: "Wal-Mart cares deeply about its 10,000 associates
who serve its customers throughout its nine-state marketing area", and the Chairman's message "the
complete dedication and loyalty of our 1 0,000 associates throughout our Company" — Date: FY1977
(document; the "nine-state" footprint dates the statement to after the 1975-11-11 Texas entry) — Source:
`WALMART_AR_1977.txt` L780 and L397 (file lines) — Source date: 1977-04-01 — URL: as A3-011 —
Archived: on disk — Tier: 1 — Class: FACT (that the company stated 10,000) — Passage: "its 10,000
associates who serve its cus- tomer throughout its nine-state marketing area" — Conf: Medium —
**the number is round, is a company assertion, and the document does not say whether "associates"
counts full-time only or includes leased-department staff ⇒ basis UNKNOWN** — Corroboration: 1 lineage —
Conflicts: none. A2 carried **no headcount row at all**; this is the first in this corpus.

### 3.3 FY1974 mine — `WALMART_AR_1974.txt`, Five Year Progress Report (file L110-174)

A3-014 Claim: **FY1974 (FYE 1974-01-31) as printed in its own report**, "FIVE YEAR PROGRESS REPORT"
(exact dollars, not thousands) — Net Sales **$167,560,892**; Income before income taxes **$11,883,754**;
Pro forma net income **$6,158,520**; Pro forma net income per share **$.93**; Number of stores in
operation at the end of the period **78** — Date: 1973-02-01→1974-01-31 — Source:
`WALMART_AR_1974.txt` L110-174 (file lines) — Source date: auditor's report dated **21 March 1974**
(Arthur Young & Company, Tulsa OK, unqualified) — URL:
https://archive.org/details/1974-annual-report-for-walmart-stores-inc — Archived:
sources/periodicals/WALMART_AR_1974.txt — Tier: 1 — Class: FACT — Passage: "Net Sales $30,862,659
$44,286,012 $78,014,164 $124,889,141 $167,560,892 … Income before income taxes $ 2,198,764 $ 3,170,599
$ 5,569,027 $ 8,917,188 $ 11,883,754" — Conf: High — Corroboration: 1 lineage; CONTEMPORANEOUS for
FY1974 — Conflicts: none. **Value upgrade: A2 carried FY1974 net sales as "$167,561,000" and pre-tax
as "$11,884k" (thousands, from FY1976's summary); the contemporaneous print gives exact dollars and the
thousands-rounding is now seen to be the later document's rounding, not the company's FY1974 figure.**

A3-015 Claim: The FY1974 report's balance-sheet block prints **stockholders' equity $30,734,128
(FY1974) and $24,753,623 (FY1973)** and **number of shares outstanding 6,542,250 (FY1974) and 6,512,950
(FY1973)**, with total current liabilities 18,121,532 and total 60,105,646 — Date: 1974-01-31 /
1973-01-31 — Source: `WALMART_AR_1974.txt` L110-174 and balance sheet at file L995-1077 — Source date:
1974-03-21 — URL: as A3-014 — Archived: on disk — Tier: 1 — Class: FACT — Passage: "Number of Shares
Outstanding 6,542,250 6,512,950" — Conf: High (FY1974 6,542,250); **Low-Medium on the FY1973 figure
6,512,950, which disagrees with the 6,512,550 A2 read from the FY1973 report** → U-A3/5 —
Corroboration: 1 lineage; CONTEMPORANEOUS for FY1974 — Conflicts: U-A3/5. Also note the FY1974 total
assets print **60,105,646** where the FY1978 nine-year table prints 60,106 (thousands) — consistent.

A3-016 Claim: The FY1974 report's own five-year table is **the cleanest contemporaneous witness to
FY1970-FY1973 that exists**, because it prints exact dollars and a full row set for all five years:
Net Sales $30,862,659 / $44,286,012 / $78,014,164 / $124,889,141 / $167,560,892; Income before income
taxes $2,198,764 / $3,170,599 / $5,569,027 / $8,917,188 / $11,883,754; Pro forma net income
$1,187,764 / $1,651,599 / $2,907,354 / $4,591,469 / $6,158,520; Pro forma EPS $.23 / $.30 / $.47 / $.70 /
$.93; Stores 32 / 38 / 51 / 64 / 78 — Date: FY1970→FY1974, all printed in 1974 — Source:
`WALMART_AR_1974.txt` L110-174 — Source date: 1974-03-21 — URL: as A3-014 — Archived: on disk — Tier: 1 —
Class: FACT (as printed) — Passage: "Pro forma net income per share $.23 $.30 $.47 $.70 $.93" —
Conf: High — Corroboration: 1 lineage. **Basis flag, and it is the crux of this dossier's method: for
FY1974 this is CONTEMPORANEOUS; for FY1970-FY1973 this same block is RESTATED (in the FY1974 report) —
a 1974 document restating years whose own reports are not on disk. It is a better witness than A2's
1972-dated table for FY1970-FY1973 (closer in time, and it adds FY1974), but it is not primary for
those three years.** The label "pro forma" is the company's own and is retained: see A3-020.

A3-017 Claim: The FY1974 report supplies contemporaneous store-grossing detail for FY1974 that no A2
document carried: **20 new stores opened and 6 closed in FY1974** (vs 16 opened / 3 closed in FY1973),
**881,630 sq ft of new store space**, total store sales including leased departments **$182,634,000**,
leased departments comprising shoes, jewelry and **twenty-six pharmacies**, and the note under the
five-year store series that **"Two Ben Franklin variety stores were sold and four were closed during the
year"** — Date: FY1974 — Source: `WALMART_AR_1974.txt` provenance `DOCUMENT:` line, verified against the
body — Source date: 1974-03-21 — URL: as A3-014 — Archived: on disk — Tier: 1 — Class: FACT — Passage:
"Two Ben Franklin variety stores were sold and four were closed during the year" — Conf: High —
Corroboration: 1 lineage; CONTEMPORANEOUS — Conflicts: none. **Significance for Stage 1: this is a
dated, contemporaneous record of the Ben Franklin franchise estate still being liquidated in FY1974 —
twelve years after the first Discount City — which no A2 record on disk established.** Expansions
listed with square footage: Salem MO 25,000→37,000; Mountain Home AR 22,000→51,000; **Marshfield MO Ben
Franklin Family Center converted to a 29,100 sq ft Wal-Mart**; **Rogers AR relocated 35,000→56,000**;
Jonesboro AR rebuilt to 65,000 (tornado May 1973); Berryville AR 30,000 (fire December 1972).

### 3.4 FY1975 mine — `WALMART_AR_1975.txt`

A3-021 Claim: **FY1975 (FYE 1975-01-31) as printed in its own report**, "FIVE YEAR SUMMARY (Dollar
amounts in thousands except for per share data)" — net income **6,353\*** (asterisked); net income per
share **$.95\***; leased department rentals and other income — net **2,478**; cost of sales **176,591**;
operating, selling and general and administrative expenses **48,088**; interest and debt expense
**1,800**; taxes on income **5,855** — Date: 1974-02-01→1975-01-31 — Source: `WALMART_AR_1975.txt`
L1070-1180 — Source date: auditor's report 28 March 1975 — URL:
https://archive.org/details/1975-annual-report-for-walmart-stores-inc — Archived:
sources/periodicals/WALMART_AR_1975.txt — Tier: 1 — Class: FACT — Passage: "Net income 6,353* 6,159
4,591 2,907 1.652" — Conf: High — Corroboration: 1 lineage; **CONTEMPORANEOUS** — Conflicts: none.
**This is the whole value of the FY1975 download and it is a partial one: the earnings, expense and tax
rows are contemporaneous, the top line is not.**

A3-022 Claim: **FY1975 net sales is NOT printed on this document's machine-readable text layer.** The
Five Year Summary's Net sales row carries **four** values ($167,561 / $124,889 / $78,015 / $44,286)
against **five** column heads (1975 1974 1973 1972 1971): FY1975's own cell is absent, and the row label
itself OCRs as "IN el odlcS" — Date: FY1975 — Source: `WALMART_AR_1975.txt` L1070-1180 — Source date:
1975-03-28 — URL: as A3-021 — Archived: on disk — Tier: 1 — Class: FACT (about the absence) — Passage:
"IN el odlcS S 167,561 $124,889 $ 78,015 $ 44,286" — Conf: High — Corroboration: 1 —
**Conflicts: U-A3/1 (the $226,209 / $236,209 2-vs-3 digit ambiguity which the file's own header records)
and the derivation in A3-023. FY1975 net sales is recorded in this dossier as NOT CONTEMPORANEOUSLY
READABLE, not as unknown — the deficit is in the text layer, not in the company.**

A3-023 Claim: FY1975 net sales can be **recovered from the FY1975 report's own five rows by inverting
the table's arithmetic identity**, which the file verifies for every other column: net sales =
(taxes + net income) + interest + operating expense + cost of sales − leased-department rentals =
(5,855 + 6,353) + 1,800 + 48,088 + 176,591 − 2,478 = 12,208 + 223,501… = **$236,209 thousand** — Date:
FY1975 — Source: `WALMART_AR_1975.txt` L1070-1180 (all five input rows are on the same page of the same
1975 document) — Source date: 1975-03-28 — URL: as A3-021 — Archived: on disk — Tier: 1 —
Class: **ESTIMATE / DERIVED**, arithmetic shown — Passage: NO_VERBATIM_PASSAGE_RECORDED (derived) —
Conf: **Medium-High** — Corroboration: the same identity closes exactly for FY1974, FY1976, FY1977 and
FY1978 in the FY1977/FY1978 reports, and the FY1979 report's own Five-Year Financial Review prints
FY1975 net sales as $236,209,000 and pre-tax as 11,521,000 (restated) — so the derivation is not
speculative, but **it is a derivation, and the value that resolves it is stated by later documents.
Therefore FY1975 net sales is entered in Table S1 as DERIVED-ON-CONTEMPORANEOUS-INPUTS, and it is NOT
promoted to CONTEMPORANEOUS.** The page image (`_text.pdf`, 3.2 MB, declared in the FY1975 metadata)
would settle it directly: **UNTRIED**, deliberately, since a re-walk is a retrieval task not a writing
task and §14 rule 1 makes the unwritten dossier the more expensive failure.

A3-024 Claim: **FY1975's total assets and stockholders' equity are likewise unrecoverable from its own
text layer** (the balance sheet shows the 1974 column with 1975 cells as noise "KlHHWil",
"F^ffftEffjfcjJ", "^S^SIBm"), while FY1974's are printed — Date: FY1975 — Source:
`WALMART_AR_1975.txt` L1-30 (header) and the balance-sheet region at L1753-1800 — Source date:
1975-03-28 — URL: as A3-021 — Archived: on disk — Tier: 1 — Class: FACT (about the deficit) — Passage:
"the balance sheet shows the 1974 column with 1975 cells as noise" — Conf: High — Corroboration: 1 —
Conflicts: none. FY1975 equity $36,935k and total assets $75,221k therefore remain **RESTATED (in the
FY1976 report)** and re-printed in the FY1977 and FY1978 tables; A3 does not let three later printings
become a contemporaneous one.

A3-025 Claim: **FY1975's own report states the LIFO break in the company's own words and its exact
size**: "Net income would have increased 4! [41] percent to $8.7 million, or $1.31 per share, compared to
last year's net income of $6.2 million, or $.93 per share, had we not made the decision to change from
the first-in, first-out … to the last-in, first-out … method of costing inventory … The change resulted
in a decrease in earnings of $2.3 million, or $.36 per share, for fiscal 1975, to $6.4 million, or $.95
per share." — Date: FY1975 — Source: `WALMART_AR_1975.txt` L225-240 — Source date: 1975-03-28 — URL: as
A3-021 — Archived: on disk — Tier: 1 — Class: FACT — Passage: "The change resulted in a decrease in
earnings of $2.3 million, or $.36 per share, for fiscal 1975" — Conf: High — Corroboration: 1 lineage;
CONTEMPORANEOUS — Conflicts: none, and it **reconciles across the split**: the FY1978 nine-year footnote
states the same event as "$2,347,000 or $.18 per share"; $2,347,000 ÷ 6,542,250 FY1974 shares = $.359
= $.36 (pre-split) and ÷ ~13.1m post-split shares = $.18 (U-A3/9). **The FY1975/FY1974 inventory series
is therefore on two different cost bases, and any inventory-turn or gross-margin comparison that crosses
January 1975 must say so.**

A3-026 Claim: **FY1975's own report states gross margin and expense ratios as printed, not derived**:
gross margin **25.2%** vs **26.4%**; SG&A **20.4%** vs **19.7%**; advertising **1.4%** vs **1.2%**; rent
**2.4%** vs **2.2%** (FY1975 vs FY1974) — Date: FY1975 — Source: `WALMART_AR_1975.txt`, Management's
Analysis of Summary of Earnings (body line 1280 region) — Source date: 1975-03-28 — URL: as A3-021 —
Archived: on disk — Tier: 1 — Class: FACT (as stated by management) — Passage: NO_VERBATIM_PASSAGE_RECORDED
(quoted from this project's retrieval note; the underlying page lines should be re-walked before CSV
entry) — Conf: Medium-High — Corroboration: 1 lineage — Conflicts: none; §5 reproduces the same ratios
as DERIVED from the table rows and they agree to 0.1 pt.

A3-027 Claim: **FY1975 headcount and physical footprint, contemporaneous**: "its 5800 associates" and
"the over-all quality of its approximately 5800 associates"; 26 new stores opened and 2 existing
enlarged, "giving an additional **1,083,326 square feet, a record for new store space in a single
year**"; entry into Kentucky and Mississippi (Corinth MS 50,150 sq ft, August; Fulton KY 32,000 sq ft,
October); two Sav-Co Home Improvement Centers totalling 54,000 sq ft, already under review — "It will
not be expanded until it is operating at our expected profitability level"; fleet at FY-end = **100
Wal-Mart Discount Cities + 2 Family Centers + 2 Sav-Co = 104 stores**; state counts AR 37 / MO 36 /
OK 15 / KS 6 / TN 6 / LA 2 / MS 1 / KY 1 (= 104 ✓); "A new **150,000 square foot Distribution Center**
began operation in January 1975 … eight railroad car and 37 truck doors, as compared with six railroad
car and 28 truck doors in the original Distribution Center"; "approximately 60 percent of the
merchandise shipped to our stores came through our Warehouse and Distribution Center as compared to
55 percent in the previous year"; average store size ~42,000 sq ft, range 30,000-60,000, twenty-four
newest average 42,900; towns "within a 350 mile radius of the General Office and Distribution Centers in
Bentonville"; average community population served 10,000-15,000 — Date: FY1975 — Source:
`WALMART_AR_1975.txt` L225-290, L700-715, L767, L912 — Source date: 1975-03-28 — URL: as A3-021 —
Archived: on disk — Tier: 1 — Class: FACT — Passage: "giving an additional 1,083,326 square feet, a
record for new store space in a single year" — Conf: High — Corroboration: 1 lineage; CONTEMPORANEOUS —
Conflicts: none. **A2 carried NO headcount and NO FY1975 square footage; its store count of 104 for
FY1975 was a FY1976-dated restatement. And no document on disk states FY1975's TOTAL square footage, so
sales-per-square-foot for FY1975 is UNKNOWN (§5), and cannot be back-filled from the addition series.**

A3-028 Claim: **The origin narrative, stated contemporaneously in FY1975**: "The Company's founder and
present Chairman of the Executive Committee of the Board of Directors, Sam M. Walton, wrote the first
chapter in Wal-Mart's success story when he opened his first Ben Franklin variety store in **Newport,
Arkansas in 1945**. One year later, joined by his brother, J. L. 'Bud' Walton, now Senior Vice
President … **Between 1945 and 1962, they assembled a group of fifteen successful Ben Franklin stores**
which served as the base for what was to become Wal-Mart Stores, Inc."; "**Wal-Mart's first Discount
City store opened in Rogers, Arkansas (then a town of approximately 4700), in November 1962**" — Date:
events 1945, 1946, 1945-1962, 1962-11 — Source: `WALMART_AR_1975.txt` (company-profile narrative) —
Source date: 1975-03-28 — URL: as A3-021 — Archived: on disk — Tier: 1 — Class: **FOUNDER CLAIM /
RETROSPECTIVE INTERPRETATION, transmitted by the registrant 13 and 30 years after the events** —
Passage: "opened his first Ben Franklin variety store in Newport, Arkansas in 1945" — Conf: **High that
the company said this in 1975; Low that any 1945 or 1962 event is independently documented** —
Corroboration: **1 lineage repeated (see A3-029) — repetition inside the same report series is NOT a
second source (§3 filing-lineage rule)** — Conflicts: U-A3/8 (Rogers' population 4700 here vs
"approximately 5,000" in FY1978).

A3-029 Claim: **Every year FY1974→FY1979 now carries its own printed restatement of the 1945/1962
origin, and the run is internally stable while the underlying events stay single-lineage**: FY1974
"Fiscal year 1974 was the most significant in the **twenty-nine year history** of your Company"
(1974 − 29 ⇒ 1945); FY1977 "The Company's first unit was a franchised Ben Franklin variety store, opened
in **1945, in Newport, Arkansas by Sam M. Walton**. In 1946, his brother, J. L. 'Bud' Walton, opened a
similar store in **Versailles, Missouri**. **Until 1962, the Company's business was devoted to the
operation of variety stores.** In that year, the first Wal-Mart Discount City store was opened in
**Rogers, Arkansas**"; FY1978 "…**1945, when Sam Walton opened his first Ben Franklin franchise
operation in Newport, Arkansas** … the Company did not open its first discount department store until
**November 1962. The first Wal-Mart Discount City store was opened in Rogers, Arkansas** … who had formed
[a] **partnership in 1946** … a group of fifteen successful Ben Franklin variety stores"; FY1979 "since
its **first discount store opened 17 years ago** … In **1945, Sam Walton opened his first variety store,
under the Ben Franklin franchise, in Newport, Arkansas** … a similar store in **Versailles, Missouri** …
**15 Ben Franklin stores between 1946 and 1962** … the first Wal-Mart Discount City in **Rogers,
Arkansas, in 1962**. Wal-Mart Stores, Inc. has been **publicly-owned since October, 1970**" — Date:
1945-1962 as narrated — Source: `WALMART_AR_1974.txt`, `_1975.txt`, `_1977.txt`, `_1978.txt`,
`_1979.txt` narrative pages (FY1978 body L361-385; FY1977 body L648-658 per the file's own pointer) —
Source date: 1974-03-21 → 1979-04-06 — URL: as cited — Archived: on disk — Tier: 1 — Class: FACT (that
each report says it) / **FOUNDER CLAIM, retrospective, for the events themselves** — Passage: "Until
1962, the Company's business was devoted to the operation of variety stores." — Conf: High (stability of
the self-report across six consecutive reports); **unchanged-Low (independent documentation of 1945 or
1962)** — Corroboration: 1 lineage — Conflicts: **the FY1975 report dates the brothers' association to
"One year later" (1946) and FY1979 to "between 1946 and 1962"; FY1978 calls it a "partnership in 1946".
No document states a partnership deed, a date for the firm name, or which of the fifteen stores the
registrant group acquired and when.** **This is the honest shape of the pre-1972 record: better
attestation of the *telling*, no new attestation of the *told*.**

### 3.5 FY1979 mine — `WALMART_AR_1979.txt`

A3-030 Claim: **FY1979 (FYE 1979-01-31) as printed in its own audited statement of income, exact
dollars** — Net sales **$900,298,000**; Rentals from leased departments 6,344,000; Other income — net
3,271,000; **total revenues 909,913,000**; Cost of sales 661,062,000; Operating, selling and general and
administrative expenses 188,592,000; Interest and debt expense 3,487,000; **total costs and expenses
853,141,000**; **Income before income taxes 56,772,000**; **Net income 29,447,000**; primary EPS
**$1.93**, fully diluted **1.93**; **Number of stores in operation at the end of the year 229**;
dividends paid **$.22 per share** — Date: 1978-02-01→1979-01-31 — Source: `WALMART_AR_1979.txt`
L1882-1960 (income statement), L2017 (dividends parenthetical), L17-130 (two-year comparison and
Five-Year Financial Review) — Source date: auditor's report 6 April 1979 — URL:
https://archive.org/details/1979-annual-report-for-walmart-stores-inc — Archived:
sources/periodicals/WALMART_AR_1979.txt — Tier: 1 — Class: FACT — Passage: "$900,298,000 6,344,000
3,271,000 909,913,000 … 661,062,000 188,592,000 3,487,000 853,141,000" — Conf: High — Corroboration: 1
lineage; **CONTEMPORANEOUS** — Conflicts: none. Identity checks close: 909,913 − 853,141 = 56,772 ✓;
56,772 − 29,447 = 27,325 (taxes) ✓; $.055 × 4 quarterly payments = $.22 ✓. **A2 held all of FY1979's
income-line figures from `WALMART_AR_1980.txt` L89/L92/L94/L95-99 — an FY1980-dated restatement. FY1979's
own audited statement is the primary and is now on disk.**

A3-031 Claim: **FY1979 balance sheet, contemporaneous, and it reconciles to the penny**: total assets
**$324,666,000** = total current liabilities **98,868,000** (notes payable 550,000 + accounts payable
65,001,000 + accrued salaries 7,759,000 + taxes other than income 4,719,000 + other 6,933,000 + accrued
federal and state income taxes 9,729,000 + long-term debt due within one year 1,700,000 + obligations
under capital leases due within one year 2,477,000) + long-term debt **25,965,000** + long-term
obligations under capital leases **72,357,000** + total stockholders' equity **127,476,000**; current
assets 191,860,000; working capital 92,992,000; current ratio 1.94; **shares outstanding 15,079,383**;
inventories (Note 2) **$172,640,000**, with "Replacement cost (FIFO vs LIFO) would be $22,271,000
greater in 1979 and $14,148,000 greater in 1978" — Date: 1979-01-31 — Source: `WALMART_AR_1979.txt`
L2042-2260, L21-130, L2593-2597 — Source date: 1979-04-06 — URL: as A3-030 — Archived: on disk —
Tier: 1 — Class: FACT + ESTIMATE/DERIVED for the sum — Passage: "Inventories at January 31. 1979, and
January 31 , 1978, were $172,640,000 and $135,845,000 respectively." — Conf: High — Corroboration: 1
lineage; CONTEMPORANEOUS — Conflicts: **the printed current-liability total reads "96,868,000" but its
own eight components sum to 98,868,000, which is also what the two-year comparison prints; the OCR digit
is wrong, not the company. Also: total assets and the capital-lease line are on the POST-SFAS-13 basis —
see U-A3/6 — so FY1979's $324,666,000 is not comparable with any pre-FY1979 asset figure.**

A3-032 Claim: **FY1979's physical footprint and headcount, contemporaneous**: "During the year, we added
thirty-five new Wal-Mart stores and closed our remaining Sav-Co Home Improvement Center, which created a
net addition of over **1,600,000 square feet** of floor space. **Total retail space occupied at January
31, 1979, was 10,200,000 square feet**"; company profile: "a progressive chain of discount department
stores operating regionally in **ten central and southern states** … the **229 stores** are located
primarily in small communities like Bentonville … **The stores vary in size from 30,000 to 83,000 square
feet** … Each store features **36 departments** … **Softline products account for 30 percent of sales and
hardline goods 70 percent**"; data processing: "company-wide payroll for over **17,500 associates**";
Contents lists a **"Fashion Distribution Center"** and a **"Claims Center"** as divisions — Date: FY1979
— Source: `WALMART_AR_1979.txt` L1791-1810, L140-175, L1230-1245 — Source date: 1979-04-06 — URL: as
A3-030 — Archived: on disk — Tier: 1 — Class: FACT — Passage: "Total retail space occupied at January
31. 1979. was 10,200,000 square feet." — Conf: High (space, store count, department count, headcount as
company-stated; the 30/70 softline/hardline split is management's own characterisation with no stated
basis) — Corroboration: 1 lineage — Conflicts: none. **A2's 10,200,000 sq ft for FY1979 came from the
FY1980 report; FY1979's own statement now supersedes it. Note the 8,500,000 (FY1978) → 10,200,000 step is
+1,700,000 against a stated "over 1,600,000" net addition — consistent — and that FY1978's own report
calls the same measure "square feet of floor space in operation" while FY1979 calls it "retail space
occupied": two labels, one series, basis not defined in either document.**

A3-033 Claim: **FY1978's restated comparatives as printed in the FY1979 report** — net sales
$678,456,000 (unchanged); rentals from leased departments 4,957,000 and other income 2,810,000 (re-split
out of what FY1978 had shown as a single "leased department rentals and other income — net 7,767");
cost of sales 503,825,000 (unchanged); **operating/S&G/administrative 139,278,000** (was 137,939,000);
interest and debt expense 2,273,000 (unchanged); total costs 645,376,000; **income before income taxes
40,847,000** (was, on FY1978's own rows, 42,186); **net income 21,191,000** (was 21,886); primary EPS
**$1.48** (was 1.53), fully diluted **1.41** (was 1.46); stores 195; **total assets $251,865,000** (was
206,691,000); current liabilities 74,891,000 (was 73,083,000); long-term debt 21,489,000 (unchanged);
**long-term obligations under capital leases 59,003,000** (was 10,904,000); capital in excess of par
29,520,000; **retained earnings restated 65,475,000** (previously reported 67,936,000, restatement
(2,461,000)); **stockholders' equity $96,482,000** (was 98,943,000); shares outstanding 14,867,711;
current ratio 2.02 — Date: FY1978 as restated — Source: `WALMART_AR_1979.txt` L1882-1960, L2042-2260,
L17-130, L1997-2020 — Source date: 1979-04-06 — URL: as A3-030 — Tier: 1 — Class: FACT — Passage:
"'All financial information has been restated to reflect the retroactive application ot [sic] Statement
of Financial Accounting Standards No. 13.'" — Conf: High — Corroboration: 1 lineage;
**RESTATED (in the FY1979 report)** — Conflicts: U-A3/4, U-A3/5, U-A3/6. **This single document is the
reason A3 exists: for FY1978 there are now two complete, internally consistent, auditor-attached
statements of the same year, differing on purpose. Neither is wrong. A register that prints one of them
without the other destroys the evidence.**

A3-034 Claim: **The FY1979 report's "FIVE-YEAR FINANCIAL REVIEW" is a clean restated series for
FY1975-FY1979 and it closes A2's column-alignment inference.** Printed rows: Net sales $900,298,000 /
$678,456,000 / $478,807,000 / $340,331,000 / $236,209,000; Income before income taxes 56,772,000 /
40,847,000 / 30,857,000 / 22,057,000 / 11,521,000; Net income 29,447,000 / 21,191,000 / 16,039,000 /
11,132,000 / 5,995,000; Net income per share, primary $1.93 / $1.48 / $1.15 / $.80 / $.45; fully diluted
1.93 / 1.41 / 1.08 / .77 / .45; Stores 229 / 195 / 153 / 125 / 104 — Date: FY1975→FY1979 as restated —
Source: `WALMART_AR_1979.txt` L17-160 — Source date: 1979-04-06 — URL: as A3-030 — Archived: on disk —
Tier: 1 — Class: FACT — Passage: "30.857,000 16,039,000 $1.15 1.08 153" — Conf: High — Corroboration:
1 lineage; **RESTATED (in the FY1979 report)**, and the same values re-printed in the FY1980 ten-year
table — Conflicts: none. **Merge consequence: A2's W-69 row carried A2's own flag — "Medium; INFERENCE
on column alignment … the row is OCR-scrambled and is cross-checked only where taxes + net income =
pre-tax income". That caveat is now discharged: the FY1979 five-year review prints FY1975 5,995 /
FY1976 11,132 / FY1977 16,039 / FY1978 21,191 cleanly, in a table whose neighbours are legible, and
every one of those values satisfies pre-tax − net income = the implied tax. The FY1980 inference can be
withdrawn and the values kept, on the correct RESTATED label.**

A3-035 Claim: **The SFAS-13 restatement effect per year is now computable and monotone**, by pairing
each year's own as-published pre-tax and net income with the restated pair in A3-034 — FY1975: pre-tax
12,208 → 11,521 (**−687**), net 6,353 → 5,995 (**−358**); FY1976: 22,798 → 22,057 (**−741**), 11,506 →
11,132 (**−374**); FY1977: 31,833 → 30,857 (**−976**), 16,546 → 16,039 (**−507**); FY1978: 42,186 →
40,847 (**−1,339**), 21,886 → 21,191 (**−695**). Independent check: the FY1979 report's own
retained-earnings bridge gives cumulative effect at 1978-02-01 of 2,461,000 and at 1977-02-01 of
1,766,000, difference **695,000 = the FY1978 net-income effect computed above** — Date: FY1975-FY1978 —
Source: `WALMART_AR_1975.txt` / `_1976.txt` / `_1977.txt` / `_1978.txt` (as published) and
`WALMART_AR_1979.txt` (as restated) — Source date: 1975-03-28 → 1979-04-06 — URL: as cited —
Archived: on disk — Tier: 1 — Class: **ESTIMATE / DERIVED**, arithmetic shown — Passage: "Restatement of
1978 for Statement of Financial Accounting Standards No. 13 (Note 7) (2,461,000)" — Conf: High for the
differences as arithmetic, Medium for reading them as the whole accounting effect (a tax-efffect and
reclassification element may sit inside) — Corroboration: 1 lineage — **Conflicts: U-A3/5, because the
FY1979 Chairman's prose says the FY1978 restatement "reduced net earnings $769,000, or 5 cents per
share" while the same document's own statement lines give 695; the $74,000 gap is not reconciled
anywhere on disk, and the "5 cents" fits 695 better than 769 on the 1.46→1.41 diluted move.**

A3-036 Claim: **The SFAS-13 retroactive application grossed up the balance sheet without touching the
income statement's top lines: FY1978 total assets 206,691,000 as published → 251,865,000 restated
(+45,174,000), while long-term obligations under capital leases 10,904,000 → 59,003,000 (+48,099,000)
and equity fell only 98,943,000 → 96,482,000 (−2,461,000).** The mechanism is named in the documents
themselves: FY1976's report had disclosed "noncapitalised financing leases of stores $38,416,000" whose
capitalisation "would cut FY1976 net income ~$515,000", and FY1979's Note 7 is the lease note — Date:
FY1978 — Source: `WALMART_AR_1978.txt` L1396-1410 (as published) and `WALMART_AR_1979.txt` L2042-2260
(restated); mechanism from `WALMART_AR_1976.txt` (A2 W-cite: 1976 L2151-2272) — Source date: 1978-04-14
/ 1979-04-06 — URL: as cited — Archived: on disk — Tier: 1 — Class: FACT + DERIVED for the deltas —
Passage: "Long-term obligations under capital leases 10,904 4,087" (FY1978 print) vs "59.003.000" (FY1979
print of the same date) — Conf: High — Corroboration: 1 lineage — Conflicts: U-A3/6.
**Register rule adopted: the asset series in this dossier is broken at 1979-01-31/1978-01-31. Any
asset-turn, debt/assets or total-assets growth figure computed across that line is invalid, and A2's
`Total assets` row — which placed FY1973-76 thousands and FY1979-80 thousands in one row at "High" —
mixed the two bases silently.**

### 3.6 FY1972 / FY1973 / FY1976 — what the five new documents add to years A2 already had

A3-037 Claim: **FY1974, FY1975, FY1977 and FY1978's own reports independently reprint FY1972 and FY1973
in full**, converting those two years from "two printings, one 1972 and one 1973 document" to "four
printings 1972-1978" and, importantly, **adding a cost-of-sales and expense row for FY1972/FY1973 in
each of FY1975, FY1977 and FY1978's tables**: FY1972 cost of sales 58,592 / operating expense 14,285 /
interest 415 / taxes 2,662 / net income 2,907; FY1973 93,090 / 23,848 / 592 / 4,326 / 4,591 (thousands) —
Date: FY1972, FY1973 — Source: `WALMART_AR_1974.txt` L110-174 (exact dollars, top-line and pre-tax and
pro-forma only); `WALMART_AR_1975.txt` L1070-1180; `WALMART_AR_1977.txt` L1400-1460;
`WALMART_AR_1978.txt` L1424-1544 — Source date: 1974-03-21 → 1978-04-14 — URL: as cited — Archived: on
disk — Tier: 1 — Class: FACT — Passage: "58,592" / "14,285" — Conf: High — Corroboration: **1 lineage
only — four printings of one registrant remain one lineage (§3)**; status stays **CONTEMPORANEOUS** for
FY1972/FY1973 (their own reports were already on disk in A2) — Conflicts: none. **Net effect on A2: the
FY1972 gross margin A2 had to derive by reading the FY1973 report's comparative column ($58,591,379) is
now printed as a summary-table row in three further documents, so the derivation no longer depends on
crossing two documents.**

A3-038 Claim: **FY1976 loses nothing and gains three later witnesses.** FY1976's own report remains the
contemporary: net sales $340,331k, pre-tax $22,798k as published, net income $11,506k, primary EPS $.83 /
diluted $.80, stores 125, shares 13,418,063, equity $48,454k, total assets $100,249k, inventories
$64,371k net of a $7,081k LIFO reserve, 5,295,000 sq ft total store space (+23%). New: the FY1977
eight-year summary and FY1978 nine-year summary print the same values in thousands
(340,331 / 251,473 / 68,105 / 1,758 / 11,292 / 11,506 / $.83 / .80 / .065 / 125 / 76,070 / 23,646 /
100,249 / 32,945 / 17,531 / 48,454), the FY1977 report's balance sheet prints FY1976 inventories
**$64,371,000** in exact dollars, and the FY1977 report's stock line prints FY1976 shares **13,418,063**
— Date: FY1976 — Source: `WALMART_AR_1976.txt` (as A2 cited) plus `WALMART_AR_1977.txt` L1400-1460,
L2010-2020, L2160-2172; `WALMART_AR_1978.txt` L1424-1544 — Source date: 1976-03-26 → 1978-04-14 — URL: as
cited — Archived: on disk — Tier: 1 — Class: FACT — Passage: "Inventories (Note 2) 88,815,000 64,371,000"
— Conf: High — Corroboration: 1 lineage — **CONTEMPORANEOUS for FY1976, unchanged** — Conflicts: none.

### 3.7 Pre-FY1972 — the part of the brief the downloads could not fix

A3-039 Claim: **FY1962–FY1967 remain EMPTY, not thin: no net sales, no store count, no earnings, no
balance sheet, no square footage, no headcount for any year FY1962 through FY1967 appears in ANY of the
nine reports, and the earliest counted year in the whole corpus is still FY1968.** FY1968 $12,618,754 and
FY1969 $21,365,081 remain **RESTATED (in the FY1972 report, 1972-03-22)** — and the five new documents
**cannot** restate them, because the FY1974 five-year table starts at FY1970 and the FY1978 nine-year
table starts at FY1970. FY1970 and FY1971 gain a second and third later printing (FY1974's table;
FY1975's table for FY1971; FY1978's nine-year table for both) and their **first-ever balance-sheet and
expense-row statement** (FY1970: current assets $6,703k, net PP&E $1,678k, total assets $8,493k, current
liabilities $3,872k, long-term debt $1,328k, capital leases —, equity $3,159k, cost of sales $22,866k,
operating expense $5,912k, interest $108k, taxes $960k, net income "1,011", EPS $.11, stores 32;
FY1971: 12,150 / 3,080 / 15,331 / 6,513 / 809 / — / 7,841 / 32,825 / 8,441 / 195 / 1,519 / 1,652 / $.15 /
38) — but **no FY1970 or FY1971 annual report exists in this corpus**, so those years stay
restated-only — Date: FY1962–FY1971 — Source: negative search across all nine files; positive rows from
`WALMART_AR_1972.txt` L48-106 and `WALMART_AR_1978.txt` L1424-1743 — Source date: 1972-03-22 / 1978-04-14
— URL: as cited — Archived: on disk — Tier: 1 — Class: FACT (rows) / **EMPTY** (FY1962-FY1967) —
Passage: "Stores in operation at the end of the period … 32" (FY1970, the earliest store count in the
nine-year run) — Conf: High for what is printed; **the FY1970 net income cell is Low, see U-A3/2** —
Corroboration: 1 lineage — Conflicts: U-A3/2.
**The corpus floor has moved, but only inside FY1972-FY1980. A2's structural finding survives intact:
there is still no witness dated before 1972-03-22 anywhere in this evidence set, and every statement
about 1945-1971 is still a later document talking about an earlier one.**

#### Table S1 — Net sales, income before income taxes, operating profit, net income

**No document on disk prints an "operating profit" line.** The nearest printed measure is *Income before
income taxes*; operating profit below is DERIVED as `net sales + leased-department rentals − cost of
sales − operating/S&G/admin expense` (i.e. before interest and debt expense), and each row's check
`operating profit − interest = income before income taxes` is shown. Amounts FY1968-FY1974 exact dollars;
FY1975 onward thousands.

| FY | Net sales (as printed) | Income before income taxes | Operating profit (DERIVED) | Net income | Basis flag |
|---|---|---|---|---|---|
| FY1962–FY1967 | **EMPTY — no figure in any document** | EMPTY | EMPTY | EMPTY | no witness exists |
| FY1968 | $12,618,754 | $779,754 | **UNKNOWN** (no cost-of-sales row printed) | $481,754 *pro forma* | **RESTAT (in FY1972 report, 1972-03-22)** — only printing anywhere |
| FY1969 | $21,365,081 | $1,056,211 | **UNKNOWN** | $605,211 *pro forma* | **RESTAT (in FY1972 report)** — only printing anywhere |
| FY1970 | $30,862,659 | $2,198,764 | **UNKNOWN** (rows exist only in the FY1978 table, in thousands, and that table's own identity gives 2,307−108 = 2,199 ≠ 2,198,764 only in the FY1968-69 sense: it AGREES — see note) | $1,187,764 *pro forma* / **"1,011"** in the FY1978 table | **RESTAT (in FY1972 report)**; **RESTAT (in FY1974 report, 1974-03-21)**; **RESTAT (in FY1978 report)** for the expense rows. **No FY1970 report exists.** U-A3/2 |
| FY1971 | $44,286,012 | $3,170,599 | 3,366 (thousands, DERIVED) | $1,651,599 *pro forma* = 1,652 (thousands) | **RESTAT (in FY1972 report)**; **RESTAT (in FY1974, FY1975, FY1978 reports)**. **No FY1971 report exists** |
| FY1972 | $78,014,164 | $5,569,027 | 5,984 (DERIVED; 5,984 − 415 = 5,569 ✓) | $2,907,354 = 2,907 (thousands) | **CONTEMP (FY1972 report)** + RESTAT in FY1973/74/75/77/78 prints |
| FY1973 | $124,889,141 | $8,917,188 | 9,509 (DERIVED; −592 = 8,917 ✓) | $4,591,469 = 4,591 | **CONTEMP (FY1973 report)** + RESTAT in FY1974/75/77/78 prints |
| FY1974 | $167,560,892 | $11,883,754 | 12,983 (DERIVED; −1,099 = 11,884 ✓) | $6,158,520 = 6,159 | **CONTEMP (FY1974 report, 1974-03-21)** ← NEW; was RESTAT-in-FY1976 in A2 |
| FY1975 | **NOT PRINTED on the FY1975 text layer**; 236,209 DERIVED from the same table's five rows; later prints $236,209k (FY1976/77/78) and $236,209,000 (FY1979 review) | 12,208 (DERIVED from contemporaneous 5,855 + 6,353); restated **11,521** | 14,008 (DERIVED; −1,800 = 12,208 ✓) | **6,353\* CONTEMP** ; restated **5,995** | **mixed**: earnings CONTEMP, top line DERIVED-on-contemporaneous-inputs, assets/equity RESTAT-in-FY1976 |
| FY1976 | $340,331k | 22,798 CONTEMP (FY1976); restated **22,057** | 24,556 (DERIVED; −1,758 = 22,798 ✓) | 11,506 CONTEMP; restated **11,132** | CONTEMP + RESTAT in FY1977/78/79 |
| FY1977 | **$478,807k CONTEMP (FY1977 report)** | **31,833 DERIVED from the FY1977 report's own contemporaneous rows** (15,287 + 16,546); restated **30,857** | 33,724 (DERIVED; −1,891 = 31,833 ✓) | **16,546 CONTEMP**; restated **16,039** | ← **NEW: A2 had FY1977 only from the FY1980 table (restated, 1980-dated, alignment-inferred)** |
| FY1978 | **$678,456k CONTEMP (FY1978 report)** | **42,186 DERIVED from the FY1978 report's own rows** (20,300 + 21,886); restated **40,847,000 printed** in FY1979 | 44,459 (DERIVED; −2,273 = 42,186 ✓) | **21,886 CONTEMP**; restated **21,191,000** | ← **NEW: contemporaneous print + a 1979-dated restatement, one year earlier than A2's only source** |
| FY1979 | **$900,298,000 CONTEMP (FY1979 income statement)** | **56,772,000 CONTEMP (printed line)** | 60,259 (DERIVED; −3,487 = 56,772 ✓) | **29,447,000 CONTEMP** | ← **NEW: A2 held all of FY1979 from the FY1980 report** |
| FY1980 | $1,248,176k CONTEMP (FY1980 report) | 74,288k CONTEMP | **UNKNOWN — cost of sales and interest for FY1980 were not extracted by A2 and are not re-minted here**; opex stated only as a 20.2% ratio | 41,151k CONTEMP | unchanged by the five downloads; operating profit deliberately left UNKNOWN rather than reconstructed from a rounded ratio |

**Note on FY1970, stated so the reader does not smooth it.** The FY1978 nine-year table's own rows for
FY1970 (30,863 + 222 − 22,866 − 5,912 − 108) give pre-tax **2,199 thousand**, which matches the
FY1972/FY1973/FY1974 reports' printed **$2,198,764** to the dollar. Its taxes row (960) plus its net
income row ("1,011") give 1,971, which does not. One of the two cells is wrong, and the dossier does not
decide which: see U-A3/2.

#### Table S2 — Stores, square footage, distribution capacity, headcount

| FY | Stores at FY-end | New store space added | Total store/retail square footage | Distribution capacity as stated | Headcount as stated |
|---|---|---|---|---|---|
| FY1962–FY1967 | **EMPTY** | EMPTY | EMPTY | EMPTY | EMPTY |
| FY1968 | 24 RESTAT (in FY1973 report) | — | UNKNOWN | UNKNOWN | UNKNOWN |
| FY1969 | 27 RESTAT (in FY1973 report) | — | UNKNOWN | UNKNOWN | UNKNOWN |
| FY1970 | 32 RESTAT (in FY1972, FY1973, FY1974, FY1978 reports) | — | UNKNOWN (FY1980 report says only "less than a million square feet" at 1970-01-01 — a 1980 sentence about 1970) | DC 60,000 → 124,800 sq ft 1971-08-15 (RESTAT in FY1972/73) | UNKNOWN |
| FY1971 | 38 RESTAT (in FY1973, FY1974, FY1978 reports) | — | UNKNOWN | GO+DC 261,800 sq ft (FY1973 report) — **U-A2/3 stands: FY1976's retrospective print says 263,800** | UNKNOWN |
| FY1972 | 51 CONTEMP (FY1972) | +604,000, 14 new (CONTEMP) | UNKNOWN | as FY1971 | UNKNOWN |
| FY1973 | 64 CONTEMP (FY1973) | +781,940, 18 new (CONTEMP) | UNKNOWN | as FY1971 | UNKNOWN |
| FY1974 | **78 CONTEMP (FY1974 report)** ← NEW | **+881,630, 20 new + 4 expanded/rebuilt (CONTEMP)** ← NEW | **UNKNOWN — no total is printed** | +18,000 GO/DC addition (A2, FY1976 print); FY1974's own forward plan: "A new 150,000 square foot addition … hopefully to be completed by September 1974. At that time, our total Distribution Center and General Office space will exceed 400,000 square feet" (**a plan stated contemporaneously, not a state**) | **4,500 employees (chart, CONTEMP)** ← NEW; Medium (chart label, OCR "4.500") |
| FY1975 | **104 CONTEMP (FY1975: "100 Discount Cities + 2 Family Centers + 2 Sav-Co"; state table sums to 104 ✓)** ← NEW | **+1,083,326, 26 new + 2 enlarged, "a record for new store space in a single year" (CONTEMP)** ← NEW | **UNKNOWN — no total printed** | **new 150,000 sq ft DC in operation January 1975; 8 rail + 37 truck doors vs the original DC's 6 + 28; ~60% of merchandise through warehouse/DC vs 55% prior year (CONTEMP)** ← NEW | **"approximately 5800 associates" (CONTEMP)** ← NEW |
| FY1976 | 125 CONTEMP (FY1976) | 993,436 sq ft of FY1976 openings (CONTEMP) | **5,295,000 (+23%) CONTEMP (FY1976)** | 238,800 sq ft warehouse + 150,000 sq ft DC; +31,000 sq ft GO addition April 1976 (CONTEMP) | **UNKNOWN — the FY1976 report has a "NUMBER OF EMPLOYEES" chart whose year labels and values are OCR-damaged; not readable, and NOT guessed** |
| FY1977 | **153 CONTEMP (FY1977 report)** ← NEW | **+1,300,000, 28 new stores, +24% store space (CONTEMP)** ← NEW | **≈6,500,000 CONTEMP (FY1977 report's own words)** ← NEW; also printed as the prior-year column in FY1978 | **new 150,000 sq ft Bentonville DC completed November 1976 → 300,000 sq ft "pure distribution center", 2½-day cycle; all distribution facilities in Bentonville ≈550,000 sq ft total; ~80% of merchandise flowing through them, "increased from 60% to 80% within the past two years"; GO complex doubled early 1976 (+~31,000 → in excess of 50,000 sq ft) (CONTEMP)** ← NEW | **"10,000 associates" (CONTEMP, stated twice)** ← NEW |
| FY1978 | **195 CONTEMP (FY1978 report)** ← NEW | 30 new stores + 10 expansions/relocations + a 16-store group acquired + 4 closed (CONTEMP) | **8,500,000 CONTEMP (FY1978 report)** ← NEW | **"construction began during 1977 on a new 390,000 square foot distribution center in Searcy, Arkansas", completion tentatively June 1978, "capability of servicing one-half of the existing Wal-Mart stores", conveyor at ~200 ft/min, combining DC I warehousing with DC II distribution (CONTEMP)** ← NEW | **UNKNOWN for FY1978 — no figure found this pass; recorded as a gap, not as zero** |
| FY1979 | **229 CONTEMP (FY1979 report)** ← NEW | **net addition "over 1,600,000 square feet"; 35 new stores; remaining Sav-Co closed (CONTEMP)** ← NEW | **10,200,000 CONTEMP (FY1979 report)** ← NEW | Fashion Distribution Center and Claims Center listed as divisions (CONTEMP); store size range now "30,000 to 83,000 square feet", 36 departments (CONTEMP) | **"over 17,500 associates" (CONTEMP)** ← NEW |
| FY1980 | 276 CONTEMP (FY1980) | +2,400,000 (CONTEMP) | 12,600,000 CONTEMP (FY1980) | Searcy ~400,000 on 93 acres; Bentonville 390,000 opened January 1980; Palestine TX 510,000 planned (CONTEMP) | **"more than 21,000 associates" (CONTEMP, `WALMART_AR_1980.txt` L522)** — not in A2's series table |

**Two things this table says that A2's could not.** (1) FY1974, FY1975, FY1977 and FY1978 square-footage
totals and store counts, which A2 reached only through later reports, are now on their own year's page;
(2) **the total-square-footage series still begins at FY1976** — the FY1974 and FY1975 reports print
*additions* only, so no document on disk supports a sales-per-square-foot figure for any year before
FY1976, and the addition series must not be cumulated backwards into a "total" (the FY1980 report's
"less than a million square feet" at 1970-01-01 is a 1980 sentence, not a 1970 one).

#### Table S3 — Per share: earnings, dividends, shares outstanding

| FY | Primary EPS | Fully diluted EPS | Dividends per share | Shares outstanding at FY-end | Basis flag |
|---|---|---|---|---|---|
| FY1968 | $.09 *pro forma* | — | — | UNKNOWN | RESTAT (in FY1972 report); the only printing |
| FY1969 | $.12 *pro forma* | — | — | UNKNOWN | RESTAT (in FY1972 report); the only printing |
| FY1970 | $.23 *pro forma* (RESTAT in FY1972 + FY1974 reports) / **$.11** in the FY1978 nine-year table | — | — (nine-year table prints `—`) | UNKNOWN | split-adjusted once for 1975-08-19 between the two prints; **no FY1970 report exists** |
| FY1971 | $.30 *pro forma* (FY1972/FY1974) / **$.15** (FY1975, FY1978 tables) | — | — | 6,000,000 (RESTAT in FY1972 report) | same adjustment |
| FY1972 | $.47 *pro forma* CONTEMP / **$.24** in FY1975/FY1977/FY1978 prints | — | — | 6,000,000 (FY1972 report) | CONTEMP |
| FY1973 | $.70 CONTEMP / **.35** later prints | — | — | 6,512,950 per the FY1974 report; A2 read **6,512,550** from the FY1973 report → **U-A3/3** | CONTEMP (value), contested last digits |
| FY1974 | **$.93 CONTEMP (FY1974 report)** | — | **$.025 (first evidenced payment 5 April 1974)** — printed as the FY1974 dividend row cell in the FY1978 nine-year table, **RESTAT**; the FY1974 report's own five-year table has **no dividend row** | **6,542,250 CONTEMP (FY1974 report)** ← NEW | CONTEMP for EPS and shares |
| FY1975 | **$.95\* CONTEMP (FY1975 report)** / restated $.45 primary and .45 diluted (FY1979 review) | .45 (restated) | $.05 (RESTAT in FY1978 table) | 6,659,650 (RESTAT in FY1976 report) | earnings CONTEMP, per-share series restated twice over |
| FY1976 | $.83 CONTEMP | $.80 CONTEMP | $.065 CONTEMP (FY1976 report; reprinted FY1977, FY1978) | 13,418,063 CONTEMP | unchanged, plus new reprints |
| FY1977 | **$1.19 CONTEMP (FY1977 report)** / restated **$1.15** primary, **1.08** diluted (FY1979) | 1.12 CONTEMP | **.085 CONTEMP (FY1977 report)** ← NEW | **13,649,829 CONTEMP (FY1977 report)** ← NEW | ← A2 had FY1977 EPS only from the FY1980 table |
| FY1978 | **$1.53 CONTEMP (FY1978 report)** / restated **$1.48**, **1.41** diluted | 1.46 CONTEMP | **.16 CONTEMP (FY1978 report; restated in FY1979's Note as "$.16 per share")** ← NEW, and it **refutes** A2's alternative $.19 | **14,867,711 — stated only in the FY1979 report's comparative column: RESTAT (in FY1979 report)** | quarterly dividends FY1978 $.025/.045/.045/.045 = $.16 ✓ |
| FY1979 | **$1.93 CONTEMP** | **1.93 CONTEMP** | **$.22 CONTEMP (FY1979 income-statement parenthetical; four quarters at $.055)** ← NEW | **15,079,383 CONTEMP (FY1979 report)** ← NEW | |
| FY1980 | $2.68 CONTEMP (FY1980) | $2.68 | $.30, raised to $.40 after year end (CONTEMP) | 15,121,261 CONTEMP | unchanged |

**Split basis, corrected against A2.** Exactly **one** two-for-one split falls inside this window:
**effective 19 August 1975**, disclosed in the FY1976 report's Note 4 — "Common stock outstanding was
increased 6,687,789 shares by a two-for-one stock split effective August 19. 1975" and "$685.OO0
including S669.000 relating to the two-for-one stock split" charged to capital in excess (6,687,789 ×
$.10 par = $668,779 ✓, confirming the $.10 par stated in the FY1977 report). Proof it is the only one:
the FY1975 report prints FY1974 EPS $.93 and the FY1977/FY1978 tables print FY1974 $.47 — one halving,
not two. A2's preamble wording ("restates earlier EPS 'for the two-for-one stock split in 1976'")
mislocates the event into a year in which no such split is disclosed on disk and invites a double
adjustment. The earlier 11 June 1971 and 5 April 1972 two-for-ones are outside this dispute and are
carried from A2 unchanged.

#### Table S4 — Balance sheet

All thousands unless stated. `—` = the row itself prints an em-dash (i.e. not reported by the company for
that year). Long-term debt for FY1977 exists in two prints on purpose (see A3-012).

| FY | Current assets | Net PP&E | Total assets | Current liabilities | Long-term debt | Capital-lease obligations | Stockholders' equity | Current ratio | Inventories (exact $) | Stating document / basis |
|---|---|---|---|---|---|---|---|---|---|---|
| FY1968, FY1969 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | **no balance sheet for either year exists in any document on disk** |
| FY1970 | 6,703 | 1,678 | 8,493 | 3,872 | 1,328 | — | 3,159 | 1.7 | UNKNOWN | RESTAT (in FY1978 report, nine-year table) — **first statement of FY1970's balance sheet anywhere in this corpus** |
| FY1971 | 12,150 | 3,080 | 15,331 | 6,513 | 809 | — | 7,841 | 1.9 | $10,654,640 (FY1972 report) | RESTAT (in FY1978) for the position; CONTEMP (FY1972 report) for inventory |
| FY1972 | 21,069 | 7,080 | 28,463 | 12,806 | 4,659 | — | 10,748 | 1.7 | $18,452,663 (FY1972 report) | CONTEMP for inventory/equity/assets (FY1972 report); rows reprinted FY1978 |
| FY1973 | 32,787 | 13,233 | 46,241 | 15,990 | 5,066 | — | 24,754 | 2.1 | $29,427,119 (FY1973 report; reprinted exact in the FY1974 report's Note 2) | CONTEMP + a second CONTEMP-adjacent printing in the FY1974 report's comparative column |
| FY1974 | 45,254 | 14,657 | **$60,105,646** | **18,121,532** | 10,578 | — | **$30,734,128** | 2.5 | **$41,470,471** (stores $33,713,932 + distribution centre $7,756,539) | **CONTEMP (FY1974 report)** ← NEW; closes the inventory gap A2 had between FY1973 and FY1975 |
| FY1975 | 55,860 | 19,157 | 75,221 | 26,190 | 11,132 | — | 36,935 | 2.1 | $50,582k (FY1976 report) | **RESTAT (in FY1976, then FY1977 and FY1978 reports)** — FY1975's own text layer drops the balance sheet |
| FY1976 | 76,070 | 23,646 | 100,249 | 32,945 | 17,531 | — | 48,454 | 2.3 | **$64,371,000** (gross $71,452,000 less LIFO reserve $7,081,000; composition stores 57,371 + DCs 12,080 + new stores not opened 2,001) | CONTEMP (FY1976; composition reprinted in the FY1977 report's comparative column) |
| FY1977 | 99,493 | 33,091 | **133,158** | 41,929 | **23,245 (as the FY1977 report prints it)** / 19,158 + 4,087 (as FY1978 splits it) | 4,087 (per FY1978) | **66,183** | 2.4 | **$88,815,000** (gross $99,405,000 less LIFO reserve $10,590,000; stores 79,230 + DCs 18,708 + new stores not opened 1,467) | **CONTEMP (FY1977 report)** ← NEW, including the exact inventory composition |
| FY1978 | **150,986** | **55,402** | **206,691 as published** / **251,865 as restated** | **73,083** / 74,891 restated | **21,489** | **10,904** / **59,003** restated | **98,943** / **96,482** restated | **2.1** / 2.02 restated | **$135,845,000** (LIFO; replacement cost $14,148,000 higher per FY1979 Note 2) | **CONTEMP (FY1978 report)** ← NEW **and** RESTAT (in FY1979 report) — two live bases |
| FY1979 | 191,860 | not extracted | **$324,666,000 (POST-SFAS-13 basis)** | **98,868,000** | **25,965,000** | **72,357,000** | **$127,476,000** | **1.94** | **$172,640,000** (replacement cost $22,271,000 higher) | **CONTEMP (FY1979 report)** ← NEW |
| FY1980 | not extracted | not extracted | $457,879k | not extracted | not extracted | capital-lease obligations $97,212,000 long-term (FY1980) | $164,844k | — | $235,315k (replacement cost $38,899k higher) | CONTEMP (FY1980 report); unchanged by this pass |

**Balance-sheet basis break, stated where it will be tripped over.** Rows FY1970-FY1978 above the
FY1979 line are on the *pre*-SFAS-13 presentation (leases largely off balance sheet — FY1976's own
report disclosed $38,416,000 of noncapitalised financing leases of stores). FY1979 is on the
*post*-SFAS-13 presentation. **Total assets, debt/equity and asset-turn are therefore NOT a single
series across this table**, and any ratio computed across the FY1978/FY1979 line is reported below as
invalid rather than as a finding.


---

## 4. Delta table against A2

A2's §"Audited series" Table 1 has 24 rows. Every row is dispositioned here. **A2 was not edited**; the
merge takes A3's rows and A2 keeps its own as the trail. "Value changes" means the printed digits move;
"basis changes" means the digits survive but the witness type changes, which in a forensic register is
the more common and more dangerous error.

| A2 row (as written) | A2 value | A2's cited source | Disposition in A3 | Type of change |
|---|---|---|---|---|
| Net sales FY1968 | $12,618,754 | FY1972 L64, FY1973 | **unchanged value; still RESTAT-only, and now demonstrably so** — the FY1974 table starts at FY1970 and the FY1978 table starts at FY1970, so no new document can witness it | none |
| Net sales FY1969 | $21,365,081 | FY1972 L62 | unchanged; still RESTAT-only | none |
| Net sales FY1970 | $30,862,659 | FY1972 L60 | **unchanged value; gains a third printing (FY1974 report, exact dollars) and a thousands reprint (FY1978)** | basis (still RESTAT) |
| Net sales FY1971 | $44,286,012 | FY1972 L58; FY1980 restated | unchanged value; gains FY1974 + FY1975 + FY1978 printings | basis (still RESTAT) |
| Net sales FY1972 | $78,014,164 | FY1972, FY1973 | unchanged; CONTEMP; gains FY1974/75/77/78 printings | none |
| Net sales FY1973 | $124,889,141 | FY1973, FY1976, FY1980 | unchanged; CONTEMP; gains FY1974 (exact) + FY1975 + FY1978 | none |
| **Net sales FY1974** | **$167,561,000** | **FY1976 L37, L1032; FY1980** | **$167,560,892 CONTEMP (FY1974 report)** | **VALUE (rounding was presented as the printed figure) AND BASIS** |
| **Net sales FY1975** | **$236,209,000, Conf "High"** | **FY1976 L1030; FY1980** | **NOT printed on FY1975's own text layer; 236,209 DERIVED from FY1975's own five rows; the 2-vs-3 digit ambiguity is logged (U-A3/1); page image UNTRIED** | **BASIS DOWNGRADE — A2's "High" rested on later documents; the contemporaneous cell is missing** |
| Net sales FY1976 | $340,331,000 | FY1976, FY1980 | unchanged; CONTEMP; gains FY1977/78/79 | none |
| **Net sales FY1977** | **$478,807 thousand** | **FY1980 L89 (alone)** | **$478,807k CONTEMP (FY1977 report) + FY1978 nine-year** | **BASIS — a 1980-dated restatement becomes a 1977-dated primary** |
| **Net sales FY1978** | **$678,456 thousand** | **FY1980 L89 (alone)** | **$678,456k CONTEMP (FY1978 report) + $678,456,000 printed in FY1979's comparative column** | **BASIS** |
| **Net sales FY1979** | **$900,298 thousand** | **FY1980 L89, L1029** | **$900,298,000 CONTEMP (FY1979 audited income statement)** | **BASIS** |
| Net sales FY1980 | $1,248,176 thousand | FY1980 | unchanged | none |
| Stores FY1968→FY1973 (24·27·32·38·51·64) | as listed | FY1973 L162-175 | FY1972/FY1973 unchanged CONTEMP; FY1970/FY1971 gain FY1974 printings; **FY1968/FY1969 remain a single FY1973-dated printing** | basis for FY1970-71 |
| Stores FY1972→FY1976 (51·64·78·104·125) | as listed | FY1976 L1138-1150 | **FY1974's 78 and FY1975's 104 become CONTEMP** (FY1974 five-year table; FY1975 fleet count 100+2+2 with a state table summing to 104) | **BASIS ×2** |
| Stores FY1976→FY1980 (125·153·195·229·276) | as listed | FY1980 L104, L1056 | **FY1977's 153, FY1978's 195, FY1979's 229 all become CONTEMP** | **BASIS ×3** |
| Income before taxes FY1968→FY1972 | $779,754 · $1,056,211 · $2,198,764 · $3,170,599 · $5,569,027 | FY1972 L66-79 | unchanged; FY1970/71/72 gain the FY1974 exact-dollar printing; **label "pro forma" now carried explicitly** | basis + label |
| Income before taxes FY1973 | $8,917,188 | FY1973 L677 | unchanged CONTEMP; +FY1974 printing | none |
| **Income before taxes FY1974/75/76 "$11,884k / $12,208k / $22,798k as published"** | as listed | **FY1976 L39** | **FY1974 $11,883,754 CONTEMP; FY1975 12,208 DERIVED from FY1975's own contemporaneous tax + net-income rows; FY1976 unchanged CONTEMP; all three restated values (11,521 / 22,057) now printed in FY1979's clean five-year review** | **VALUE (FY1974) + BASIS (FY1975)** |
| **Income before taxes FY1977/78/79/80 "$30,857k / $40,847k / $56,772k / $74,288k"** | as listed | **FY1980 L92** | **The row is NOT "as printed" for FY1977/FY1978 — those are SFAS-13 restated. As-published: 31,833 (FY1977 rows) and 42,186 (FY1978 rows). FY1979's 56,772,000 becomes CONTEMP. FY1977/FY1978 restated values confirmed a year earlier in FY1979's review** | **BASIS MISLABEL — the single most consequential A2 row. Two live bases were presented as one** |
| Pro-forma/net income FY1968→FY1973 | $481,754 · $605,211 · $1,187,764 · $1,651,599 · $2,907,354 · $4,591,469 | FY1972, FY1973 | unchanged for FY1968/69 (sole printings); FY1970 **contested** (U-A3/2: the FY1978 table prints "1,011" and its own rows imply 1,239); FY1971-73 gain printings | basis + 1 contradiction |
| Net income FY1974/75/76 as published | $6,159k / $6,353k / $11,506k | FY1976 L1092-1112 | **FY1974 $6,158,520 CONTEMP; FY1975 6,353 CONTEMP** ← the FY1975 download's one clean win; FY1976 unchanged | **BASIS ×2, VALUE ×1** |
| **Net income FY1971→FY1978 restated (SFAS 13), Conf "Medium; INFERENCE on column alignment"** | 1971 $1,619k · 1972 $2,806k · 1973 $4,439k · 1974 $5,954k · 1975 $5,995k · 1976 $11,132k · 1977 $16,039k · 1978 $21,191k | FY1980 L1220-1234 | **The alignment inference is DISCHARGED: FY1975 5,995 / FY1976 11,132 / FY1977 16,039 / FY1978 21,191 are printed cleanly in FY1979's Five-Year Financial Review, and FY1978's 21,191,000 is a line of FY1979's audited statement. Confidence for those four rises Medium→High; FY1971-FY1974 restated values remain in the FY1980 garbled block only** | **CONFIDENCE + BASIS, on an A2 row that flagged itself** |
| Net income FY1979 / FY1980 | $29,447k / $41,151k | FY1980 L94, L1044 | **FY1979 $29,447,000 CONTEMP** | **BASIS** |
| EPS row (as printed and split-adjusted) | FY1968-73 pro-forma $.09 .12 .23 .30 .47 .70; FY1972-76 $.24 .35 .47 .48 .80; FY1976-80 primary $.80→$2.68 | FY1972/73/76/80 | **FY1974 $.93 CONTEMP; FY1975 $.95* CONTEMP; FY1977 $1.19/1.12 CONTEMP; FY1978 $1.53/1.46 CONTEMP; FY1979 $1.93/1.93 CONTEMP; and the split statement is corrected to a single 1975-08-19 two-for-one (COR-A3-07)** | **BASIS ×5 + a correction to the adjustment rule itself** |
| **Dividends per share** | FY1974 $.025 · FY1975 $.05 · FY1976 $.065 · FY1979 $.22 · FY1980 $.30; "constant-dollar row 1976 $.09 / 1977 $.11 / 1978 $.19 / 1979 $.25 / 1980 $.30", Conf Medium, "the ten-year dividend row is OCR-shifted" | FY1976, FY1980 | **FY1977 $.085 and FY1978 $.16 added CONTEMP; FY1979 $.22 now CONTEMP from FY1979's own income-statement parenthetical and its quarterly table ($.055 × 4); the ten-year alternative row is REFUTED for 1976-1979 — no split factor reconciles .09/.11/.19/.25 to .065/.085/.16/.22, and .16 and .22 are each printed twice in their own year's document** | **BASIS + A2's own suspicion resolved against A2's alternative row** |
| Stock price record ("no pre-1976 price data exists") | earliest FY1976/FY1975 quarterly H/L | FY1976, FY1980 | **stands**; but FY1974 adds the venue history (OTC from October 1970; **NYSE from 1972-08-25**) and FY1979's quarterly table adds FY1978/FY1979 prices | new fact, not a change |
| Shares outstanding | 6,000,000 · 6,512,550 · 6,659,650 · 13,418,063 · 15,079,383 · 15,121,261 | FY1972/73/76/80 | **6,542,250 CONTEMP (FY1974); 13,649,829 CONTEMP (FY1977); 15,079,383 CONTEMP (FY1979, was FY1980-dated); 14,867,711 RESTAT-in-FY1979 for FY1978; and FY1973's count is contested 6,512,950 vs 6,512,550 (U-A3/3)** | **BASIS ×3 + one new contradiction** |
| Stockholders' equity | $7,840,701 · $10,748,055 · $24,753,623 · $30,734k/$36,935k/$48,454k · $127,476k · $164,844k | FY1972/73/76/80 | **$30,734,128 CONTEMP (FY1974) ← exact dollars replace a thousands rounding; $66,183k CONTEMP (FY1977); $98,943k CONTEMP (FY1978); $127,476k CONTEMP (FY1979, was FY1980-dated); FY1970 $3,159k appears for the first time (RESTAT-in-FY1978); FY1978 restated to $96,482k** | **BASIS ×4, VALUE (precision) ×1** |
| Total assets | $15,331,433 · $28,462,538 · $46,241k/$60,106k/$75,221k/$100,249k · $324,666k/$457,879k | FY1972/76/80 | **$60,105,646 CONTEMP (FY1974); 133,158 CONTEMP (FY1977); 206,691 CONTEMP (FY1978) AND 251,865 RESTAT-in-FY1979; $324,666,000 CONTEMP (FY1979); FY1970 8,493 first appearance.** **And a basis warning A2 did not carry: the row straddles the SFAS-13 gross-up and is not one series (COR-A3-05)** | **BASIS + a newly-flagged invalid comparison** |
| Inventories | $10,654,640 · $18,452,663 · $29,427,119 · $50,582k · $64,371k · $172,640k · $235,315k | FY1972/73/76/80 | **$41,470,471 added CONTEMP (FY1974, with stores/DC split); $88,815,000 CONTEMP (FY1977, with the full gross-to-LIFO bridge); $135,845,000 CONTEMP (FY1978) plus its $14,148,000 FIFO differential; $172,640,000 now CONTEMP (FY1979) not FY1980-dated; and the FY1974 Note 1 statement that pre-FY1975 inventories were retail-method/FIFO gives the series a documented basis break at FY1975 that A2's row did not mark** | **BASIS ×4 + new composition + basis break** |
| Store square footage (mixed bases, Conf Medium) | FY1970 "<1m" · FY1972 +604,000 · FY1973 +781,940 · FY1976 5,295,000 · FY1979 10,200,000 · FY1980 12,600,000 | FY1980/72/73/76 | **+881,630 CONTEMP (FY1974); +1,083,326 CONTEMP (FY1975); +1,300,000 and total ≈6,500,000 CONTEMP (FY1977); total 8,500,000 CONTEMP (FY1978); net addition >1,600,000 and total 10,200,000 CONTEMP (FY1979, was FY1980-dated).** **The mixed-basis problem is NOT resolved: no document defines "store space" vs "retail space occupied" vs "floor space in operation", and FY1974/FY1975 totals remain UNKNOWN** | **BASIS ×5; the Medium stays Medium** |
| Distribution/property | DC 60,000→124,800 → 261,800/263,800 → +18,000 → 150,000 DC 1975-01-06 → 238,800 + 150,000 → +31,000 → Searcy ~400,000, Bentonville 390,000 Jan 1980, Palestine 510,000 planned | FY1972/73/76/80 | **FY1975's 150,000 sq ft DC becomes CONTEMP with door counts and the 60%/55% flow split; FY1977 gains CONTEMP Bentonville 300,000 pure-DC / ~550,000 all-distribution / 80% flow; FY1978 gains CONTEMP Searcy 390,000 with its stated "one-half of the existing stores" capability and 200 ft/min conveyor. U-A2/3 (261,800 vs 263,800) is untouched — neither number appears in the five new documents** | **BASIS ×3; one A2 contradiction unaffected** |
| Leases (the recurring exposure) | FY1972 / FY1973 / FY1976 / FY1980 detail | FY1972/73/76/80 | **A2's four years unchanged; the five new reports show FY1977 capital-lease obligations of 4,087 (thousands, per FY1978) and FY1978 of 10,904 — i.e. the on-balance-sheet lease liability begins its printed series in FY1977, and the SFAS-13 jump to 59,003/72,357 is now measurable. **The FY1974/FY1975/FY1977/FY1978 lease-commitment notes were NOT mined this pass — recorded as UNTRIED, not as absent**** | **partial: new series start point; commitment notes UNTRIED** |
| Margin and expense ratios ("only from FY1974 onward") | 26.4 / 25.2 / 26.1 / 19.7→20.4→20.5(20.0) →20.3→20.2; tax ~48%→44.6%; FY1972 24.9% and FY1971 25.9% and FY1973 25.5% derived | FY1976/80/72/73 | **Extended backwards to FY1970 from a printed cost-of-sales row (FY1978 table) — gross margin 25.9% FY1970, 25.9% FY1971, expense ratio 19.2%/19.1%; and forwards: FY1977 26.3% and FY1978 25.7% are now **stated by the company** not derived; FY1979 derived 26.6% with the company saying only "improved". FY1974/FY1975 ratios become CONTEMP. **FY1968/FY1969 remain UNKNOWN — no cost of sales exists for them anywhere on disk**, and the FY1977 letter's 21.1/20.5/20.8 expense series is added as an unreconciled basis (U-A3/7)** | **EXTENSION + BASIS ×4; the "only from FY1974" limit is lifted** |

**A2 rows that remain restated-only after all of this, listed so nobody re-reads A3 as having fixed them:**
FY1968 net sales/pre-tax/net income/EPS/stores · FY1969 same · FY1970 and FY1971 net sales, pre-tax, net
income, EPS, stores, and the *whole* FY1970 balance sheet · FY1975 net sales (top line) and total assets
and stockholders' equity · FY1978 shares outstanding · FY1974 and FY1975 dividends · every number for
FY1962-FY1967 · every 1945-1962 origin statement. **Twelve fiscal years FY1968-FY1979 now have at least
one contemporaneous witness for their net sales or earnings line; FY1970 and FY1971 are the two years in
the FY1968-FY1979 span that still have none, and FY1975 has one for earnings but not for its top line.**

---

## 5. Derived metrics — arithmetic shown, every row DERIVED

**Denominator rule applied throughout:** a ratio is computed only where **both** its numerator and its
denominator are printed in a document on disk. Otherwise the cell reads UNKNOWN and says what is missing.
Nothing below is an observation.

### 5.1 Net sales growth, year over year

| Step | Arithmetic | Result | Inputs' basis |
|---|---|---|---|
| FY1968→FY1969 | 21,365,081 ÷ 12,618,754 − 1 | **+69.3%** | both RESTAT (in FY1972) |
| FY1969→FY1970 | 30,862,659 ÷ 21,365,081 − 1 | **+44.5%** | both RESTAT (in FY1972) |
| FY1970→FY1971 | 44,286,012 ÷ 30,862,659 − 1 | **+43.5%** | both RESTAT (in FY1972/74) |
| FY1971→FY1972 | 78,014,164 ÷ 44,286,012 − 1 | **+76.2%** | RESTAT → CONTEMP |
| FY1972→FY1973 | 124,889,141 ÷ 78,014,164 − 1 | **+60.1%** | CONTEMP → CONTEMP |
| FY1973→FY1974 | 167,560,892 ÷ 124,889,141 − 1 | **+34.2%** | CONTEMP → CONTEMP |
| FY1974→FY1975 | 236,209 ÷ 167,561 − 1 | **+41.0%** | CONTEMP → **DERIVED top line** (A3-023) |
| FY1975→FY1976 | 340,331 ÷ 236,209 − 1 | **+44.1%** | DERIVED → CONTEMP |
| FY1976→FY1977 | 478,807 ÷ 340,331 − 1 | **+40.7%** | CONTEMP → CONTEMP |
| FY1977→FY1978 | 678,456 ÷ 478,807 − 1 | **+41.7%** — company states "an increase of 42 percent" ✓ | CONTEMP → CONTEMP |
| FY1978→FY1979 | 900,298 ÷ 678,456 − 1 | **+32.7%** — company states "up 33 percent" ✓ | CONTEMP → CONTEMP |
| FY1979→FY1980 | 1,248,176 ÷ 900,298 − 1 | **+38.6%** | CONTEMP → CONTEMP |

The two company-stated round numbers and the two derivations agree to 0.3 pt in both overlapping cases,
which is the strongest internal-consistency evidence in the file: **the growth curve is a real ~33-44%
plateau from FY1975, not a construction of a later report's table.**

### 5.2 Same-store (comparable-store) growth

| FY | As stated by the company | Arithmetic / basis | Confidence |
|---|---|---|---|
| FY1978 | **"Comparable stores sales (excluding the effect of new stores) increased 17 percent compared to the same period a year ago"** | **The only same-store figure printed anywhere in the nine documents.** Its denominator — which stores qualify as "comparable", and the dollar base they are comparable on — **is not stated in the document ⇒ the metric's population is UNKNOWN** | High that it was stated; Medium as an economic measure |
| FY1968-FY1977, FY1979-FY1980 | **NOT STATED** | — | **EMPTY, not zero.** The FY1976 and FY1977 reports carry Management's Analysis prose but no comparable-store line was read in them; the FY1980 report's analysis was not re-mined this pass (**UNTRIED** for those pages) |

**Consistency test of the one figure that exists (DERIVED, shown because it is checkable and not because
it is a measurement):** if the 153 stores open at FY1977 year-end each grew 17%, they carry
153 × (478,807,000 ÷ 153) × 1.17 = 153 × 3,129,458 × 1.17 = **$560,204,190**; FY1978 sales were
$678,456,000; the residual **$118,251,810 ÷ 42** net store additions = **$2,815,519 per new store**,
against $3,661,466 per comparable store. **The two company numbers are therefore mutually consistent, and
they say something no founding account on disk says: a new Wal-Mart store in FY1978 opened at roughly 77%
of a mature store's volume.** Caveats that bound the inference: 42 is a *net* count (195 − 153) while the
company also reports 30 openings, 10 expansions/relocations, 16 acquired stores and 4 closures; and part
of the FY1978 step-up comes from the acquired group rather than from new space. Mechanism for the gap:
UNKNOWN — the document offers none.

### 5.3 Sales per store (year-end count as denominator)

**Basis warning printed once, applies to every row: the denominator is a *period-end* store count, while
the numerator is a *whole-year* revenue. New stores opened through the year therefore depress this ratio,
and years with heavy back-half openings are penalised. This is not a productivity measure; it is what the
documents on disk permit.** An average-store count is not stated for any year → **UNKNOWN denominator
for the correct version of this metric.**

| FY | Arithmetic | Sales per store | Store-count basis |
|---|---|---|---|
| FY1968 | 12,618,754 ÷ 24 | $525,781 | RESTAT |
| FY1969 | 21,365,081 ÷ 27 | $791,299 | RESTAT |
| FY1970 | 30,862,659 ÷ 32 | $964,458 | RESTAT |
| FY1971 | 44,286,012 ÷ 38 | $1,165,421 | RESTAT |
| FY1972 | 78,014,164 ÷ 51 | $1,529,690 | CONTEMP |
| FY1973 | 124,889,141 ÷ 64 | $1,951,393 | CONTEMP |
| FY1974 | 167,560,892 ÷ 78 | $2,148,217 | CONTEMP |
| FY1975 | 236,209,000 ÷ 104 | $2,271,240 | DERIVED sales, CONTEMP stores |
| FY1976 | 340,331,000 ÷ 125 | $2,722,648 | CONTEMP |
| FY1977 | 478,807,000 ÷ 153 | $3,129,458 | CONTEMP |
| FY1978 | 678,456,000 ÷ 195 | $3,479,262 | CONTEMP |
| FY1979 | 900,298,000 ÷ 229 | $3,931,432 | CONTEMP |
| FY1980 | 1,248,176,000 ÷ 276 | $4,522,377 | CONTEMP |

Note the FY1974→FY1975 flattening (+6.1% against +11.3% the year before and +19.9% after) — FY1975 is the
year of the 26-store record build and of the LIFO charge, so the two effects run together; **mechanism
NOT separable from the documents on disk, and this is recorded as a shape, not as an explanation.**

### 5.4 Sales per square foot

**Series starts at FY1976 and cannot start earlier: no document on disk prints a total square footage for
FY1968-FY1975.** For FY1962-FY1975 the answer is **UNKNOWN because the denominator is not stated**, not
because the arithmetic was refused.

| FY | Arithmetic | Sales per sq ft | Basis of the denominator |
|---|---|---|---|
| FY1976 | 340,331,000 ÷ 5,295,000 | **$64.27** | "5,295,000 total", FY1976 report — definition not given |
| FY1977 | 478,807,000 ÷ 6,500,000 | **$73.66** | "approximately 6,500,000 square feet as of year-end", FY1977 report (approximate by the company's own word) |
| FY1978 | 678,456,000 ÷ 8,500,000 | **$79.82** | "8,500.000 square feet of floor space in operation at year end", FY1978 report |
| FY1979 | 900,298,000 ÷ 10,200,000 | **$88.26** | "Total retail space occupied at January 31, 1979, was 10,200,000 square feet", FY1979 report |
| FY1980 | 1,248,176,000 ÷ 12,600,000 | **$99.06** | FY1980 report |

Three labels across four years ("total space", "floor space in operation", "retail space occupied") and
no definition in any of them ⇒ **the +14%/+8%/+11%/+12% step series is comparable only if the labels
name the same quantity, which the documents do not establish.** FY1977's $73.66 also inherits the
company's own "approximately".

### 5.5 Margin and expense steps

| FY | Gross margin (DERIVED, `(sales − cost of sales) ÷ sales`) | Company's own stated gross margin | Operating/S&G expense ÷ sales (DERIVED) | Company's stated | Effective tax rate (`taxes ÷ pre-tax`) |
|---|---|---|---|---|---|
| FY1968, FY1969 | **UNKNOWN — cost of sales is not printed for either year in any document on disk** | — | **UNKNOWN** | — | **UNKNOWN** |
| FY1970 | (30,863 − 22,866) ÷ 30,863 = **25.91%** | — | 5,912 ÷ 30,863 = **19.16%** | — | 960 ÷ 2,199 = **43.7%** *(on the FY1978 table's own rows; the table's taxes/net-income pair does not close to its printed pre-tax — U-A3/2)* |
| FY1971 | (44,286 − 32,825) ÷ 44,286 = **25.88%** | — | 8,441 ÷ 44,286 = **19.06%** | — | 1,519 ÷ 3,171 = **47.9%** |
| FY1972 | (78,015 − 58,592) ÷ 78,015 = **24.90%** | — | 14,285 ÷ 78,015 = **18.31%** | — | 2,662 ÷ 5,569 = **47.8%** |
| FY1973 | (124,889 − 93,090) ÷ 124,889 = **25.46%** | — | 23,848 ÷ 124,889 = **19.10%** | — | 4,326 ÷ 8,917 = **48.5%** |
| FY1974 | (167,561 − 123,339) ÷ 167,561 = **26.39%** | **26.4% stated (FY1975 report) ✓** | 33,044 ÷ 167,561 = **19.72%** | **19.7% stated ✓** | 5,725 ÷ 11,884 = **48.2%** |
| FY1975 | (236,209 − 176,591) ÷ 236,209 = **25.24%** | **25.2% stated, CONTEMP (FY1975 report)** | 48,088 ÷ 236,209 = **20.36%** | **20.4% stated ✓** | 5,855 ÷ 12,208 = **48.0%** |
| FY1976 | (340,331 − 251,473) ÷ 340,331 = **26.11%** | 26.1% (FY1976) | 68,105 ÷ 340,331 = **20.01%** | 20.5% letter / 20.0% analysis (A2) — **unresolved** | 11,292 ÷ 22,798 = **49.5%** |
| FY1977 | (478,807 − 352,669) ÷ 478,807 = **26.34%** | **26.3% stated (FY1978 report)** | 97,807 ÷ 478,807 = **20.43%** | — | 15,287 ÷ 31,833 = **48.0%** |
| FY1978 | (678,456 − 503,825) ÷ 678,456 = **25.74%** | **25.7% stated, CONTEMP (FY1978 report)** | 137,939 ÷ 678,456 = **20.33%** as published; 139,278 ÷ 678,456 = **20.53%** restated | — | 20,300 ÷ 42,186 = **48.1%** |
| FY1979 | (900,298 − 661,062) ÷ 900,298 = **26.57%** | "Gross margins improved in 1979 over 1978" (no number) | 188,592 ÷ 900,298 = **20.95%** | **"Expenses increased .4 percent of sales in 1979 from 1978" → 20.95 − 20.53 = 0.42 ✓ the company's own delta only closes against the RESTATED FY1978 expense ratio, which is independent confirmation that FY1979's comparison was made on restated figures** | 27,325 ÷ 56,772 = **48.1%** ("increased slightly over those from 1977" ✓ 48.1 vs 48.0) |
| FY1980 | **UNKNOWN — cost of sales not extracted this pass** | — | ~20.2% (A2, stated as a ratio) | 20.2% | (74,288 − 41,151) ÷ 74,288 = **44.6%** ✓ A2's figure |

The tax rate is **flat at 48-49% from FY1972 through FY1979 and then drops to 44.6%** — that single-step
break, visible only now because FY1979's own statement supplies the missing tax line, is the cleanest
margin story in the series and it is a *tax* story, not an operating one.

### 5.6 Debt to equity

**Computed only where a document prints both a debt figure and an equity figure for the same date.**
Where the two coexist they are given separately, because "debt" has two definitions in these documents.

| FY | `(long-term debt) ÷ equity` | `(long-term debt + capital-lease obligations) ÷ equity` | Source of both inputs |
|---|---|---|---|
| FY1968, FY1969 | **UNKNOWN — no debt or equity figure for either year exists on disk** | UNKNOWN | — |
| FY1970 | 1,328 ÷ 3,159 = **0.420** | same (leases `—`) | FY1978 nine-year table (both inputs, one document) |
| FY1971 | 809 ÷ 7,841 = **0.103** | same | FY1978 table; equity also in FY1972 report |
| FY1972 | 4,659 ÷ 10,748 = **0.433** | same | FY1972 report + FY1978 table |
| FY1973 | 5,066 ÷ 24,754 = **0.205** | same | FY1973/FY1978 |
| FY1974 | 10,578 ÷ 30,734 = **0.344** | same | FY1978 table (equity also exact in the FY1974 report) |
| FY1975 | 11,132 ÷ 36,935 = **0.301** | same | FY1977/FY1978 tables (both RESTAT-in-a-later-report) |
| FY1976 | 17,531 ÷ 48,454 = **0.362** | same | FY1976/FY1977/FY1978 |
| FY1977 | **0.351** on the FY1977 report's single line (23,245 ÷ 66,183) **or 0.289** on the FY1978 report's split line (19,158 ÷ 66,183) | 23,245 ÷ 66,183 = **0.351** (= 19,158 + 4,087 ÷ 66,183 = 0.289 + 0.062) | two documents, same date, two presentations (A3-012) |
| FY1978 | 21,489 ÷ 98,943 = **0.217** as published | 32,393 ÷ 98,943 = **0.327** as published; on FY1978 **restated** figures (21,489 + 59,003) ÷ 96,482 = **0.834** | FY1978 report vs FY1979 report |
| FY1979 | 25,965 ÷ 127,476 = **0.204** | 98,322 ÷ 127,476 = **0.771** | FY1979 report, both inputs CONTEMP |
| FY1980 | **UNKNOWN — FY1980 long-term debt was not extracted by A2 or by this pass, and the denominator-only figure is not a ratio** | capital-lease obligations 97,212 ÷ 164,844 = **0.590** on the lease line alone | FY1980 report; **the full FY1980 ratio is reported UNKNOWN rather than assembled from a partial row** |

**Read the FY1978/FY1979 pair with the break in mind: 0.327 → 0.771 is not a leverage event.** It is the
SFAS-13 capitalisation of leases that already existed (A3-036). The genuine FY1978→FY1979 change in
*rental* debt, excluding lease presentation, is 21,489 → 25,965 = **+20.8%** against equity
98,943 → 127,476 = **+28.8%**, i.e. **conventional debt lightened relative to equity while total
recognised obligations roughly tripled on paper.** Any Stage-1 claim about how Wal-Mart financed its
growth has to say which of those two it means.

### 5.7 What cannot be derived at all, and why

- **Inventory turns / sales-to-inventory for FY1968, FY1969, FY1974-FY1978 partial**: cost of sales and
  inventories coexist for FY1970-FY1973 and FY1976-FY1979 but **not for FY1974/FY1975** (inventory is
  printed for FY1974 by the FY1974 report and for FY1975 by the FY1976 report, cost of sales for both by
  the FY1978 table) — ratios across the FY1975 LIFO break are reported as **not computed**; the basis
  change alone invalidates the comparison (A3-025).
- **Capital expenditure per store, selling cost per store, payroll per associate**: **UNKNOWN — no
  document on disk prints capex, payroll, or wage totals for any year in this window**; FY1979's
  "company-wide payroll for over 17,500 associates" says the payroll ran through the computer, not what
  it was.
- **Return on assets / return on equity**: **taken as printed, not re-derived** — the FY1978 table states
  its own basis in a footnote ("**On beginning of year balances") and A3 verified it: FY1976
  11,506 ÷ 75,221 = 15.3 ✓, FY1975 6,353 ÷ 60,106 = 10.6 ✓, FY1974 6,159 ÷ 46,241 = 13.3 ✓, FY1973
  4,591 ÷ 28,463 = 16.1 ✓, FY1972 2,907 ÷ 15,331 = 19.0 ✓, FY1971 1,652 ÷ 8,493 = 19.5 ✓, FY1977
  16,546 ÷ 100,249 = 16.5 ✓, FY1978 21,886 ÷ 133,158 = 16.4 ✓; equity likewise (FY1976 11,506 ÷ 36,935 =
  31.2 ✓ … FY1971 1,652 ÷ 3,159 = 52.3 ✓). **Because the denominators are prior-year balances, the
  printed returns for FY1970 (20.7 / 49.4) depend on FY1969 assets and equity, which no document states
  ⇒ those two cells are not checkable and are marked as printed only.**

## 6. Auditor and attestation note — how much weight the label "audited series" can carry

### 6.1 Who attested which year

| Fiscal year (ended 31 Jan) | Attesting firm | Opinion date on the document | Opinion wording as it reads on disk | Effect on the series |
|---|---|---|---|---|
| FY1968, FY1969, FY1970, FY1971 | **NONE — no opinion in any document on disk attaches to these years** | — | — | **not audited; the FY1968-FY1971 earnings rows are labelled *pro forma* by the registrant itself (A3-020)** |
| FY1972 | Arthur Young & Company, Tulsa OK | A2 records the FY1972 report's date as 1972; the presidential letter is signed 1972-03-22 | "Our examination was made in accordance with generally accepted auditing standards … In our opinion, the statements mentioned above present fairly the consolidated financial position of Wal-Mart Stores, Inc. and subsidiaries **at January 31, 1972**, the consolidated results of their operations and changes in their consolidated financial position **for the year then ended** … applied on a basis consistent with that of the preceding year." (`WALMART_AR_1972.txt` L368-390) | **the opinion names ONE year.** FY1971's comparatives are not inside it |
| FY1973 | Arthur Young & Company | 1973-03-20 | (per A2) | — |
| FY1974 | **Arthur Young & Company, Tulsa Oklahoma** | **1974-03-21, unqualified** | per the file's provenance block: "**Report of Independent Certified Public Accountants (Arthur Young & Company), Tulsa Oklahoma, dated March 21, 1974, unqualified**" | first year whose opinion A3 adds |
| FY1975 | **Arthur Young & Company** | **1975-03-28 — QUALIFIED by exception** | "**except for the change, which we approve, in the method of determining inventory cost as described in Note 2**" | **the comparability break the company itself flagged: FY1975 vs FY1974 is not an apples-to-apples year, and the auditor said so in the opinion, not in a footnote** |
| FY1976 | Arthur Young & Company | 1976-03-26 | (per A2) | — |
| FY1977 | **Arthur Young & Company** | **1977-04-01, unqualified** | "…at January 31, 1977 and 1976 and the related consolidated statements of income and retained earnings and changes in financial position **for the years then ended** … in conformity with generally accepted accounting principles applied **on a consistent basis during the period**." (`WALMART_AR_1977.txt` L2755-2772) | **two years now inside the opinion; the wording has moved from "consistent with that of the preceding year" (FY1972) to "on a consistent basis during the period" (FY1977)** |
| FY1978 | **Arthur Young & Company** | **1978-04-14, unqualified** | per the file's provenance block | — |
| FY1979 | **Arthur Young & Company** | **1979-04-06 — carries the retroactive-restatement clause** | "…applied on a consistent basis during the period **after restatement of the consolidated financial statements to give retroactive effect to the change, with which we concur, in the method of accounting for leases as described in Note 7**" | **this is the document that authorises the SFAS-13 restatement of FY1975-FY1978 — the auditor concurred in re-writing prior years** |
| FY1980 | Arthur Young & Company | 1980-04-01 | (per A2) | — |

### 6.2 What the label can and cannot bear

1. **Eight consecutive audited year-ends (FY1972-FY1979) now sit behind dated Arthur Young opinions,
   up from four in A2.** That is a real strengthening of the register, and it is the honest headline of
   this dossier.
2. **The multi-year summary tables are not, on their face, inside any opinion.** Every opinion on disk is
   addressed to "the consolidated balance sheet … and the related consolidated statements of income and
   retained earnings and changes in financial position". The 5-Year / Eight-Year / Nine-Year / Ten-Year
   summaries are supplementary pages outside that naming. **Consequence: FY1968-FY1971 — which appear
   ONLY in summary tables and in a comparative column of the FY1972 statement — are the part of the
   "audited series" that the word "audited" least applies to, and the company's own "pro forma" label
   already says so.** FY1971 is the single exception: it is inside the FY1972 report's comparative
   balance-sheet column, but the FY1972 opinion names only "the year then ended".
3. **Two of the eight opinions are not clean passes.** FY1975 is qualified for an accounting change the
   auditor "approve[s]" (LIFO), and FY1979 carries the clause endorsing a retroactive restatement of
   leases. Both are comparability events, and both were invisible to A2 because it had neither report.
   **A founder's-playbook register that reported a smooth FY1974→FY1976 margin step without the LIFO
   qualification inside it would be reporting an artefact of an accounting change as if it were an
   operating result.**
4. **The auditor is one party, engaged by the registrant, and attests statements — not history.**
   Arthur Young's signature adds assurance over the FY1972-FY1979 numbers. It adds **nothing** to the
   1945 or 1962 origin claims, which appear in narrative pages no opinion covers. The independence note
   in A2's §Findings preamble stays exactly true and A3 has not diluted it: "the only genuine second
   party in this evidence set is Arthur Young & Company's signature, which attests the statements, not
   the 1945-1962 events."
5. **Neither firm was local.** Tulsa, Oklahoma for the auditor; Conner, Winters, Ballaine, Barry &
   McGowen, Tulsa, for counsel (A2). A3's nine documents add no counter-example and make the pattern
   more conspicuous, since all eight new-region years are signed in Tulsa too.

**Verdict on the label.** "Audited series" is defensible for **FY1972-FY1980** and must be printed as
**"auditor-attested registrant self-report, one lineage"** for FY1968-FY1971, where it is a *pro forma*
company table restated by later company tables. A3 uses the label only in the first sense.

---

## 7. Evidence-family verdict, re-derived, and the Stage-1 depth verdict

### 7.1 Collapsed to the four families §14 rule 6 requires

| Family | Status before the five downloads (A2) | Status now | What changed |
|---|---|---|---|
| **1. Filings (EDGAR / SEC)** | **EMPTY (proven null)** for electronic filings pre-1994 — oldest submission row 1994-02-14, first 10-K 1995-04-27. Paper 1970 registration statement and 1970s 10-Ks **UNTRIED** | **UNCHANGED.** The nine printed reports are shareholder annual reports, not EDGAR accessions; they belong to family 4 | nothing |
| **2. Web archives** | **EMPTY (proven null)** for pre-1990 exact-root captures (first capture 1996-12-29); `matchType=prefix` sweeps **UNANSWERED** (HTTP 504) | **UNCHANGED** | nothing |
| **3. Periodical corpora** (trade press, newspapers, magazines, chain directories) | **UNANSWERED, never a null**: Google Books HTTP 429, HathiTrust TLS failure with no HTTP status, Chronicling America 403/Cloudflare, loc.gov 403, UALR CONTENTdm 403, arkdigital DNS failure, thefreelibrary 403; the *IA* magazine and trade runs are **EMPTY as to IA's holdings only**, which is not a null as to the content | **UNCHANGED — and this is the decisive line in this dossier. The five new files are corporate print, not periodicals. Not one word of third-party contemporaneous text entered the corpus.** | **nothing** |
| **4. Auction / museum documentary records** | Museum page POSITIVE for one 1962 artifact ("First Walmart Advertisement", `assetYear 1962`), **its image UNTRIED**; auction family EMPTY-for-the-queries-run and **UNTRIED as a family** | **UNCHANGED** | nothing |
| *(5th family A2 tracked separately)* **Digitised corporate print** | POSITIVE but **4 documents**; A2's own COR-A2-10 flagged the FY1972→FY1998 run as a **download gap, not a corpus absence** | **POSITIVE and now FY1972→FY1980 continuous: 9 documents, 8 dated audit opinions, and the pre-FY1972 registrant print remains a proven null (A2's 3a row)** | **the whole of this dossier** |

**Family tally: POSITIVE = 1 whole (corporate print) + 1 partial (museum, single artifact). EMPTY as a
proven null within a stated perimeter = EDGAR pre-1994, web pre-1990, IA pre-FY1972 registrant print,
IA's own magazine/trade/Gazette holdings. UNANSWERED = the entire third-party periodical family. UNTRIED
= paper SEC records, county/SoS records, paywalled newspapers, finding-aid portals, the 1962 image, the
1992 memoir as a text, and now the page images of the five new reports.**

### 7.2 Stage-1 depth verdict — bifurcated, and deliberately so

**(a) FY1972-FY1980 financial interior: `DEPTH-CORE (single-lineage)`.** Reason: nine consecutive printed
reports, no missing year, eight dated opinions, a contemporaneous witness for every primary income-statement
line of every year in the span, cross-year internal identities that close to the dollar, and two named
accounting breaks documented by the auditor. Nothing in this dossier's corpus is deeper.

**(b) FY1962-FY1971 interior and the whole origin layer: `PROVISIONAL — NOT CORE`.** Reason: FY1962-FY1967
is EMPTY; FY1968-FY1971 is pro-forma-and-restated with no opinion attached; FY1970-FY1971 have no report;
and every 1945/1946/1962 statement is the registrant's retrospective self-report — now repeated in six
consecutive reports, which strengthens the **telling** and not the **told**.

**(c) Company-level Stage-1 verdict: `PROVISIONAL`. §14 rule 6 is not satisfied and A3 does not pretend
otherwise.** A lean/core verdict requires four families; only one is positive, one is partial, one is
UNANSWERED, and the fourth has never been properly tried. **The count of independent lineages in the
Walmart Stage-1 financial record is 1, and downloading five more documents from the same corporate
lineage left it at 1.** No number of further years of Wal-Mart's own annual reports can move this
verdict; only a different publisher can.

**(d) The specific witness that would move it, named so the next pass is not left guessing.** A
**non-company contemporaneous count** of Wal-Mart's stores or sales for FY1964-FY1970 — the *Chain Store
Age* annual "Directory of Chain Stores" (Google Books, blocked at 429, family 3), a Dun & Bradstreet /
Hoover's firm report, or an Arkansas/Missouri/Oklahoma local daily reached through a route that is not
Cloudflare-blocked (Chronicling America was searched against "waltons newport **mo**" — the wrong state —
so that family is untested twice, per A2's own note). **Until one exists, the depth verdict for the
1962-1970 stage stays provisional, and the correct one-line statement of it is: "the register is deep and
the record is one voice."**

## Contradictions

Format per §7. **Both sides are kept; none is reconciled by choosing one.** A3 IDs run U-A3/n and do not
renumber A2's U-A2/n.

**U-A3/1 — FY1975 net sales: $236,209 vs $226,209.**
CLAIM A: FY1975 net sales $236,209 thousand. CLAIM B: the same year printed as $226,209 in the FY1976
report's five-year table (the digit 2/3 is the ambiguity; the FY1975 report's own cell is absent
altogether). WHY THEY DIFFER: OCR of a low-resolution "2"/"3" in a stacked numeric column — a machine
failure, not a company one. EVIDENCE WEIGHT: the FY1975 report's own five printed rows, inverted, give
236,209 exactly (A3-023); the FY1977 eight-year summary, the FY1978 nine-year summary and the FY1979
five-year review each print 236,209; only the FY1976 text layer reads 226,209. BEST-SUPPORTED
INTERPRETATION: $236,209 thousand. RESIDUAL UNCERTAINTY: **the contemporaneous printed top line for
FY1975 has still not been read from a printed page** — four later documents agreeing is one lineage
agreeing with itself; the FY1975 page image (`_text.pdf`) is UNTRIED, so this stays open at Medium-High,
not High. CONFIDENCE: Medium-High.

**U-A3/2 — FY1970 net income: $1,187,764 vs "1,011" thousand vs an implied 1,239.**
CLAIM A: pro forma net income FY1970 = $1,187,764, printed identically in the FY1972, FY1973 and FY1974
reports' five-year tables. CLAIM B: net income FY1970 = 1,011 (thousands), printed in the FY1978 nine-year
table's FY1970 column. WHY THEY DIFFER: unknown, and this is the point — the FY1978 table is **internally
inconsistent**, because its own FY1970 rows give pre-tax 30,863 + 222 − 22,866 − 5,912 − 108 = 2,199
(which matches Claim A's $2,198,764 exactly) while its taxes 960 plus its net income 1,011 give 1,971. A
third value, 1,239 (= 2,199 − 960), is what the table's own arithmetic requires. EVIDENCE WEIGHT: three
documents for A, one for B, and B disagrees with itself. BEST-SUPPORTED INTERPRETATION: $1,187,764 pro
forma remains the register value, **and the FY1978 table's FY1970 column is marked suspect in its
net-income cell**. RESIDUAL UNCERTAINTY: an OCR mis-read cannot be separated from a genuine second basis
(an *actual* rather than *pro forma* FY1970 result) without the FY1978 page image, which is UNTRIED.
Nothing here is treated as resolved. CONFIDENCE: Medium for A, Low for B.

**U-A3/3 — FY1973 shares outstanding: 6,512,950 vs 6,512,550.**
CLAIM A: 6,512,950, printed in the FY1974 report's own balance-sheet block ("Number of Shares Outstanding
6,542,250 / 6,512,950"). CLAIM B: 6,512,550, read by A2 from the FY1973 report (`WALMART_AR_1973.txt`
L103-108) and carried into A2's series table at High. WHY THEY DIFFER: a single digit (9 vs 5) in a
typewritten balance sheet, or a genuine restatement of a year-end count between the two documents.
EVIDENCE WEIGHT: each figure has one printing. BEST-SUPPORTED INTERPRETATION: **neither; the difference
is 400 shares out of 6.5 million and is immaterial to every ratio in §5, so it is recorded rather than
adjudicated.** RESIDUAL UNCERTAINTY: the FY1973 and FY1974 page images would settle it in one look; both
UNTRIED. **Register effect: A3 prints "6,512,950 per FY1974 / 6,512,550 per FY1973" and forbids quoting a
single FY1973 count at High.** CONFIDENCE: Medium (that the discrepancy is real), Low (as to which).

**U-A3/4 — FY1977 and FY1978 earnings: as published vs SFAS-13 restated.**
CLAIM A: FY1977 pre-tax 31,833 / net 16,546; FY1978 pre-tax 42,186 / net 21,886 — printed in those years'
own reports, with the auditor's clean signature. CLAIM B: FY1977 pre-tax 30,857 / net 16,039; FY1978
pre-tax 40,847 / net 21,191 — printed in the FY1979 five-year review and again in the FY1980 ten-year
table, under the declaration "All financial information prior to 1979 has been restated to reflect the
retroactive application of Statement of Financial Accounting Standards No. 13". WHY THEY DIFFER: a
documented, auditor-concurred accounting change (lease capitalisation), not an error. EVIDENCE WEIGHT:
both sides are Tier-1, dated, and complete. BEST-SUPPORTED INTERPRETATION: **A for anything that claims
to be "what the company reported at the time"; B for anything that claims to be comparable to FY1979 or
FY1980. There is no third figure that is "the real" FY1978 net income.** RESIDUAL UNCERTAINTY: A2
presented B's numbers inside a row titled "as printed" at High confidence and separately carried B as a
restatement with an alignment INFERENCE — so the register cannot say which basis its own EPS and margin
steps used. **A3's §5.5 and §5.6 recompute on both and the FY1979 expense-delta check (20.95 − 20.53 =
0.42 against the company's stated ".4") shows the company itself was comparing against B.** CONFIDENCE:
High (both readings), High (that A2's row was mislabelled).

**U-A3/5 — the size of the FY1978 restatement, inside one document.**
CLAIM A: "The restatement reduced net earnings $769,000, or 5 cents per share" (FY1979 Chairman's
message / Management's Analysis, `WALMART_AR_1979.txt` L1804-1808). CLAIM B: 21,886 → 21,191 = **$695,000**
(the same document's audited statement lines), independently corroborated by its own retained-earnings
bridge (cumulative effect 2,461,000 at 1978-02-01 less 1,766,000 at 1977-02-01 = 695,000). WHY THEY
DIFFER: unknown; a pre-publication figure surviving in prose, or a difference between net income and some
other measure (e.g. before a minority or extraordinary item, which no FY1979 line discloses). EVIDENCE
WEIGHT: two internal arithmetic paths give 695; the prose gives 769; and the "5 cents" the same sentence
quotes fits either at the rounding of ~15m shares, so the prose is not independently checkable.
BEST-SUPPORTED INTERPRETATION: **695 for the income-statement effect; 769 recorded as the company's own
stated number, unretracted.** RESIDUAL UNCERTAINTY: $74,000 — 0.3% of FY1978 net income, immaterial to
§5, but it sits inside a single audited document and A3 does not smooth it. CONFIDENCE: High (both
figures exist), Medium (that 695 is the statement-line figure).

**U-A3/6 — FY1978 total assets: 206,691 vs 251,865 thousand, same balance-sheet date.**
CLAIM A: 206,691, printed in the FY1978 report signed 1978-04-14. CLAIM B: 251,865, printed as FY1978's
comparative in the FY1979 report signed 1979-04-06. WHY THEY DIFFER: SFAS-13 brought capitalised lease
assets onto the balance sheet — the matching liability is visible as long-term capital-lease obligations
moving 10,904 → 59,003 (+48,099) against the asset move (+45,174), with equity falling only 2,461.
EVIDENCE WEIGHT: both are Tier-1 statements of the same date by the same firm; B has the later and more
extensive recognition rule behind it. BEST-SUPPORTED INTERPRETATION: **B is the correct figure to compare
with FY1979/FY1980; A is the correct figure to compare with FY1970-FY1977. The asset series is broken and
must be printed broken.** RESIDUAL UNCERTAINTY: A2's `Total assets` row placed FY1973-76 thousands and
FY1979-80 thousands in the same row at "High" with no flag, so any growth or turn figure a reader derived
from A2 silently mixed bases. CONFIDENCE: High.

**U-A3/7 — FY1977 report's expense ratios vs the eight-year table's own rows.**
CLAIM A: "We controlled tightly our expense structure in 1976, though it increased slightly from 20,5% of
sales in 1975 to 20.8% last year … Two years ago, for 1974, our total expense structure was 21.1% of
sales" (`WALMART_AR_1977.txt` L373-384). CLAIM B: operating + selling + general and administrative
expense ÷ net sales from the same report's Eight-Year Summary = 19.72% (FY1974), 20.36% (FY1975), 20.01%
(FY1976), 20.43% (FY1977). WHY THEY DIFFER: the letter's denominator is not stated and its year labels
are ambiguous — its gross-margin sentence ("improved our gross profits by a .2% increase") matches
FY1976→FY1977 (26.11→26.34), which implies the letter names fiscal years by their **starting calendar
year**, i.e. "1976" = FY1977; under that mapping 20.8% still exceeds the computed 20.43%. EVIDENCE
WEIGHT: the table is auditable arithmetic on printed rows; the letter is management prose with an
unstated base. BEST-SUPPORTED INTERPRETATION: **none. The ratio's denominator is not stated in a document
on disk, so per §5 the FY1977 letter's 21.1 / 20.5 / 20.8 series is recorded as STATED-BUT-NOT-RECONCILABLE
and is excluded from §5.5.** RESIDUAL UNCERTAINTY: whether "total expense structure" includes interest,
pre-opening costs, or leases — none of which the document says. CONFIDENCE: High (that it does not
reconcile), UNKNOWN (as to what it measures).

**U-A3/8 — Rogers, Arkansas, population at the first Discount City.**
CLAIM A: "(then a town of approximately 4700)" — FY1975 report. CLAIM B: "then a small, primarily
agricultural community of approximately 5,000 people" — FY1978 report. WHY THEY DIFFER: rounding of the
same 1960-census figure, or reliance on a different source. EVIDENCE WEIGHT: equal; one lineage, three
years apart. BEST-SUPPORTED INTERPRETATION: "approximately 4,700-5,000, per the company's own two
statements, and the town's actual 1960 population was not independently sought." RESIDUAL UNCERTAINTY:
**no census record is in this corpus; the 1962 opening itself still has no witness outside the
registrant.** CONFIDENCE: Medium (as a range), Low (as a fact about 1962).

**U-A3/9 — FY1977 long-term debt: one line (23,245) or two (19,158 + 4,087).** Recorded in full at A3-012;
kept here because the two presentations give materially different leverage for the same date (0.351 vs
0.289 before leases). RESIDUAL UNCERTAINTY: whether FY1977's single line was a presentation shortcut or a
different classification standard; no document says. CONFIDENCE: High (that both were printed).

**Unchanged from A2 and explicitly NOT resolved by these downloads:** U-A2/2 (the 1970 offer *price* —
$16.50 remains a company-page claim; the FY1972 note still gives no price and the five new reports add
none), U-A2/3 (the 261,800 vs 263,800 General-Office/DC pair — neither number occurs in FY1974, FY1975,
FY1977, FY1978 or FY1979), U-A2/7 (the harvest's Chronicling queries still search "waltons newport **mo**",
the wrong state).

## Data gaps

**The three states are kept distinct throughout: EMPTY = searched and the record is silent; UNANSWERED =
an endpoint was reached and failed to reply; UNTRIED = the retrieval was never attempted.**

### Empty (proven, inside a stated perimeter)

| Gap | Where the silence is | What would fill it |
|---|---|---|
| **FY1962-FY1967: every financial and physical variable** | nine reports, all summary tables, all narrative pages. Earliest counted year is FY1968; earliest table row in any nine-year/twelve-year print is FY1970 | the FY1970/FY1971 reports (proven absent from IA per A2's 3a row), the 1970 prospectus, a chain directory |
| **FY1968-FY1969 cost of sales, expense, balance sheet, headcount, square footage** | the FY1972 five-year table carries only sales / pre-tax / pro-forma income / EPS / stores; the FY1978 nine-year table starts at FY1970 | the FY1969/FY1970 reports; **not retrievable from anything on disk** |
| **FY1968-FY1969 shares outstanding** | nowhere | the FY1972/FY1973 balance sheets give FY1971 forward |
| **Total square footage before FY1976** | only *additions* are printed for FY1972-FY1975 | FY1976's "5,295,000" is the first total; FY1974/FY1975 totals are absent, so sales/sq ft for those years is not computable |
| **FY1978 headcount** | not found in the FY1978 report this pass | the FY1978 company-profile pages |
| **No comparable-store figure for any year except FY1978** | FY1972-FY1977 and FY1979-FY1980 print none | Management's Analysis pages of FY1979/FY1980 (UNTRIED, below) |
| **No market price before FY1975** | A2's W-54 stands; the five new reports contain no price tables for FY1972-FY1974 | the FY1976 report's earliest quarterly table; a newspaper quote sheet |
| **No witness of any kind dated before 1972-03-22** | the whole corpus | family 3 (periodicals), family 1 paper records |

### UNANSWERED (endpoint reached, no application-layer reply) — unchanged by this pass

Google Books volume API (HTTP 429, quota) · HathiTrust (TLS failure, **no HTTP status exists**) ·
Chronicling America and loc.gov (HTTP 403 / Cloudflare) · UALR CONTENTdm (HTTP 403) ·
arkdigitalcollections.org (DNS `getaddrinfo failed` — the host may not exist; **never cite it**) ·
thefreelibrary (HTTP 403) · Wayback `matchType=prefix` sweeps (HTTP 504). **None of these is a null about
Walmart; each is a statement about this environment.**

### UNTRIED (deliberately not attempted; this dossier's budget went to writing)

| Untried item | Cost | What it would settle |
|---|---|---|
| **Page images (`_text.pdf`) of FY1974, FY1975, FY1977, FY1978, FY1979** — declared in each file's IA metadata (FY1974: 3,243,815 B + `_text.pdf` 3,706,555 B; DJVU text 39,954 B byte-matched at retrieval) | local-route re-walk, no web budget needed beyond one fetch | **U-A3/1 (FY1975 net sales top line), U-A3/2 (the FY1970 net-income cell), U-A3/3 (the FY1973 share count), the FY1975 balance sheet, the FY1976 employee-chart values, and A2's W-69 middle rows.** **This is the single highest-value untried act in the whole dossier now, and it is cheap** |
| FY1974 / FY1975 / FY1977 / FY1978 **lease-commitment notes** | local | whether A2's "leases as the recurring exposure" series has interior holes or continues unbroken |
| FY1977 / FY1978 / FY1979 **market-price and dividends tables** in full | local | FY1977-79 price range; FY1975/FY1974 dividend confirmation from their own years |
| FY1979 / FY1980 **Management's Analysis** comparable-store sentences | local | a second same-store data point, the thinnest row in §5.2 |
| FY1981-FY1998 corporate print (the rest of the IA run) | download | outside Stage 1; recorded so the run's remaining gap is visible |
| Paper SEC copy: the 1970 registration statement, 1970s 10-Ks | external, reference-room request | **the only route to an accession-numbered, dated filing for the IPO years** |
| County / Arkansas SoS / Benton & Mississippi County deeds and incorporations | external | Walton Enterprises, Inc. (what it was, when formed), the subsidiaries' names — which A2 records as **not disclosed anywhere in the four reports it had**, and the five new ones do not name them either |
| The 1962 museum advertisement image; the 1992 memoir as a text; the Cornell study; the Forbes volumes | external | 1962 prices; memoir provenance; the one comparator set the company itself cites |

**What the five downloads did NOT create: any new family, any new lineage, or any pre-1972 witness.**
Every item above that was UNTRIED before is UNTRIED now, except the IA report run, which A2's 3b row
correctly called a download gap and which is now closed for FY1974-FY1979.

## Outbound corrections

Written in the form of `../../company_001_amazon/CORRECTIONS.md`: stated against a named prior record,
verified against the saved primary, with the action the merge must apply. **No prior file was edited by
this run. A2's 133 records and its 24 series rows stand as written; A3 supersedes by being later and
better-evidenced, not by deletion.**

**COR-A3-01 — A2's `## Audited series` rows for FY1974 and FY1975 are mislabelled as to source, and
FY1974's figures are wrong in the last three digits.** A2 prints "Net sales FY1974 | $167,561,000 |
WALMART_AR_1976.txt L37, L1032" and "Net sales FY1975 | $236,209,000 | WALMART_AR_1976.txt L1030". The
FY1974 report's own Five Year Progress Report (`WALMART_AR_1974.txt` L110-174, opinion dated 21 March
1974) prints **$167,560,892 / $11,883,754 / $6,158,520 / $.93 / 78 stores**, and the FY1975 report's own
Five Year Summary prints **net income 6,353\* / EPS $.95\* / cost of sales 176,591 / operating expense
48,088 / interest 1,800 / taxes 5,855**. **Action:** merge takes A3's Table S1/S3/S4 for FY1974 and
FY1975; FY1974 becomes CONTEMPORANEOUS with exact dollars; **FY1975's net sales must be entered as
DERIVED-on-contemporaneous-inputs, not as a printed contemporaneous figure, and its total assets and
equity remain RESTATED (in FY1976)** — the FY1975 text layer drops them (A3-022, A3-024).

**COR-A3-02 — A2's FY1977/FY1978/FY1979 income rows were sourced only to the FY1980 report and are now
contemporaneous, with two exceptions that are corrections rather than upgrades.** A2: "Net sales FY1977 |
$478,807 thousand | WALMART_AR_1980.txt L89 | High". **Action:** FY1977 → `WALMART_AR_1977.txt`; FY1978 →
`WALMART_AR_1978.txt`; FY1979 → `WALMART_AR_1979.txt` income statement; and **A2's row
"Income before income taxes FY1977/FY1978/FY1979/FY1980 = $30,857k / $40,847k / $56,772k / $74,288k |
WALMART_AR_1980.txt L92 | High" must be split**, because the first two are SFAS-13 restated and the last
two are as-published. As-published FY1977 = **31,833** and FY1978 = **42,186** thousand (U-A3/4).

**COR-A3-03 — A2's W-69 self-flag ("Medium; INFERENCE on column alignment … the row is OCR-scrambled")
is discharged and its restated values confirmed.** `WALMART_AR_1979.txt` L17-160 prints a clean Five-Year
Financial Review: FY1975 5,995 / FY1976 11,132 / FY1977 16,039 / FY1978 21,191 thousand net income, with
pre-tax 11,521 / 22,057 / 30,857 / 40,847 and EPS $1.48/$1.41 for FY1978 and $1.15/$1.08 for FY1977, under
the declaration "All financial information has been restated to reflect the retroactive application of
Statement of Financial Accounting Standards No. 13." **Action:** raise those four years to High, **remove
the alignment caveat, keep the RESTATED label**, and note that FY1971-FY1974 restated values remain in the
FY1980 garbled block alone.

**COR-A3-04 — A2's dividend row: its alternative "constant-dollar row 1976 $.09 / 1977 $.11 / 1978 $.19 /
1979 $.25 / 1980 $.30" is refuted for four of its five years.** Contemporaneous: FY1976 **$.065**
(FY1976 report, reprinted in FY1977 and FY1978 tables), FY1977 **$.085** (`WALMART_AR_1977.txt`
L1392 region), FY1978 **$.16** (`WALMART_AR_1978.txt` L1392, and FY1979's income statement: "Dividends
paid (1979 — $.22 per share; 1978— $.16 per share)"), FY1979 **$.22** (also four quarters at $.055 in
FY1979's dividends table). No split factor reconciles the two series: the ratio .09/.065 = 1.38 is not
.11/.085 = 1.29 nor .19/.16 = 1.19, and there was no split in the interval. **Action:** drop the
ten-year-table dividend row or mark it OCR-SHIFTED-AS-A2-SUSPECTED; A2's own FY1979 $.22 and FY1980 $.30
stand; add FY1977 $.085 and FY1978 $.16 as CONTEMPORANEOUS.

**COR-A3-05 — A2's `Total assets` row mixes two incompatible bases without a flag.** The row places
FY1973-76 thousands (46,241 / 60,106 / 75,221 / 100,249) and FY1979-80 thousands (324,666 / 457,879) in
one High-confidence line. **`WALMART_AR_1979.txt` proves the discontinuity: FY1978's total assets are
206,691,000 as published and 251,865,000 as restated — +45,174,000 on one year-end from SFAS-13 lease
capitalisation, against long-term capital-lease obligations moving 10,904 → 59,003.** **Action:** mark the
asset series broken at the FY1978/FY1979 line; forbid any asset-turn or debt/assets figure computed across
it; keep both FY1978 values.

**COR-A3-06 — A2's auditor row is superseded and the "audited series" label needs narrowing.** A2:
"Arthur Young & Company, Tulsa OK (report dates 1972, 20 March 1973, 26 March 1976, 1 April 1980)".
Now eight dated opinions, of which **FY1975 (28 March 1975) is qualified by exception "except for the
change, which we approve, in the method of determining inventory cost as described in Note 2"** and
**FY1979 (6 April 1979) carries the retroactive-restatement clause for leases (Note 7)**. And the FY1972
opinion covers **"the year then ended"** only — so A2's rows for FY1968-FY1971, which live in summary
tables and a comparative column, are outside every opinion on disk, and the company itself labelled the
FY1968-FY1971 earnings **"pro forma"**. **Action:** apply A3 §6; relabel A2's table title from
"registrant reports; amounts as printed" to "registrant reports; FY1972-FY1980 auditor-attested,
FY1968-FY1971 unaudited pro forma".

**COR-A3-07 — A2's stock-split preamble invites a double adjustment.** A2 lists two-for-ones at
"11 June 1971, 5 April 1972, 19 August 1975" and separately says "the FY1976 report restates earlier EPS
'for the two-for-one stock split in 1976'". `WALMART_AR_1976.txt` L2056-2057 reads: "Common stock
outstanding was increased 6,687,789 shares by a two-for-one stock split effective **August 19, 1975**" —
one event, disclosed in the FY1976 report, dated 1975. **Proof it is the only one in the FY1974→FY1978
window:** the FY1975 report prints FY1974 EPS $.93 and the FY1977/FY1978 tables print FY1974 $.47 —
exactly one halving. **Action:** correct the preamble; any series adjusted for "a 1976 split" in addition
to the 1975-08-19 one is over-adjusted by a factor of two from FY1972 onward.

**COR-A3-08 — A2's paragraph "Where the audited series gives way to gaps" is now partly false as
written and must be annotated, not deleted.** It states: "FY1974 and FY1975 reports were not retrieved",
"**FY1977-FY1979 are known only from summary tables, not from their own reports**". Both were correct on
2026-09-24 and both are superseded. **Still true and to be kept:** "no FY1970 or FY1971 report exists in
the source corpus at all" (A2's W-80), "FY1962-FY1967 have no store count, no sales figure and no margin
anywhere in this corpus", "The earliest document physically present in this evidence set is dated
1972-03-22". **Action:** merge adds a one-line supersession note; the paragraph stays in place.

**COR-A3-09 — A2's evidence-family row 3b changes status.** "UNTRIED (download gap)" for FY1974/FY1975
and FY1977-FY1998 becomes **POSITIVE for FY1972-FY1980; UNTRIED only for FY1981-FY1998.** **Do not let
this change the family count**: rows 7-13 (Google Books, HathiTrust, Chronicling America, loc.gov, UALR,
arkdigital, thefreelibrary) are all still UNANSWERED, rows 17-20 still UNTRIED, and §14 rule 6 therefore
remains unsatisfied. A2's own summary line — "Untried = … the IA report run beyond these four documents"
— is the only clause in it that is now stale.

**COR-A3-10 — A2's boundary-proposal evidence for a 1945 origin gains four dated restatements and no
independence.** Add: FY1974 report "the twenty-nine year history of your Company" (21 March 1974);
FY1975 report "opened his first Ben Franklin variety store in Newport, Arkansas in 1945 … Between 1945 and
1962, they assembled a group of fifteen successful Ben Franklin stores" (28 March 1975); FY1977 report
"The Company's first unit was a franchised Ben Franklin variety store, opened in 1945, in Newport,
Arkansas by Sam M. Walton. In 1946, his brother … Versailles, Missouri. Until 1962, the Company's business
was devoted to the operation of variety stores" (1 April 1977); FY1978 report (14 April 1978); FY1979
report "first discount store opened 17 years ago … publicly-owned since October, 1970" (6 April 1979).
**Action:** confidence in *"the company dated itself to 1945 by 1973"* rises toward High; confidence in
*"a 1945 event is independently documented"* **stays Low and unchanged.** Report it as
`same lineage as the FY1972 report` in `independence_note` every time.

**COR-A3-11 — a new dated market-structure fact for the master log and for Stage 1's end boundary.** The
FY1974 report: "In October 1970, Wal-Mart Stores, Inc. became a publicly-held corporation and became
traded in the over-the-counter market. **August 25, 1972, the Company's stock was listed and began
trading on the New York Stock Exchange.**" FY1979: "the Company's stock (WMT) is traded on the New York
Stock Exchange." **Action:** add the 1972-08-25 NYSE listing to the timeline; where A2's `Stock price
record` row says "No pre-1976 price data exists in this corpus", add "but a venue history does, and any
1972-08-25 price break is a listing move, not a stock event".

**COR-A3-12 — headcount enters the Walmart register for the first time, and it was never in A2.**
FY1974 4,500 (chart) · FY1975 "approximately 5800 associates" · FY1976 **UNKNOWN (chart unreadable, not
guessed)** · FY1977 10,000 · FY1978 **UNKNOWN** · FY1979 "over 17,500 associates" · FY1980 "more than
21,000 associates". **Action:** add a headcount row to the master quantitative register with basis
"company-stated, round, full/part-time composition undefined"; **do not compute sales per associate for
FY1974-FY1980** — the numerator is audited and the denominator is a rounded public-relations figure.

**COR-A3-13 — for `MASTER_RESEARCH_LOG.md`: Walmart Stage 1's depth verdict is bifurcated, not upgraded.**
`FY1972-FY1980 financial interior = DEPTH-CORE (single-lineage)`; `FY1962-FY1971 interior and origin =
PROVISIONAL, NOT CORE`; `company-level Stage 1 = PROVISIONAL`, families positive 1 whole + 1 partial,
periodicals UNANSWERED, §14 rule 6 unsatisfied. Retrieval cost of this pass: **0 WebSearch, 0 WebFetch**;
records on disk: **A3-001 … A3-039 plus 4 register sections**; nothing in `sources/` altered.

## CSV append rows

Schemas copied verbatim from `../../company_001_amazon/*.csv` headers (§13). Walmart has no CSVs yet, so
**source IDs are opened at S0101** for the nine printed reports, leaving S0001-S0099 to whoever builds the
museum/press/probe register; **`sources.csv` is append-only and no ID below is ever redefined.** Every
field containing a comma is double-quoted. `stage` = `1` in `sources.csv` (matching Amazon's usage) and
`stage1` in the company-prefixed files (matching `quantitative.csv`/`timeline.csv`/`conflicts.csv`).
**These rows are emitted, not written.**

### `quantitative.csv` — header
```
company,stage,date,metric,value,unit,source,source_date,evidence_class,confidence,derived_arithmetic,notes
```
### `quantitative.csv` — rows
```csv
Walmart,stage1,FY1974,Net sales,167560892,USD,S0103,1974-03-21,FACT,High,,"CONTEMPORANEOUS: FY1974 report Five Year Progress Report; supersedes A2's rounded $167,561,000 taken from the FY1976 report"
Walmart,stage1,FY1974,Income before income taxes,11883754,USD,S0103,1974-03-21,FACT,High,,"CONTEMPORANEOUS; A2 carried 11,884k from the FY1976 report"
Walmart,stage1,FY1974,Net income (pro forma),6158520,USD,S0103,1974-03-21,FACT,High,,"CONTEMPORANEOUS; company's own label is 'pro forma' and A3 keeps it"
Walmart,stage1,FY1974,Net income per share,0.93,USD/share,S0103,1974-03-21,FACT,High,,"pre-split basis; divide by 2 for the FY1977/FY1978 print (split effective 1975-08-19)"
Walmart,stage1,FY1974,Stores in operation at end of period,78,stores,S0103,1974-03-21,FACT,High,,"CONTEMPORANEOUS"
Walmart,stage1,FY1974,Inventories,41470471,USD,S0103,1974-03-21,FACT,High,,"Note 2: stores 33,713,932 + distribution centre 7,756,539; FIFO/retail-method basis — pre-dates the FY1975 LIFO change"
Walmart,stage1,FY1974,Stockholders' equity,30734128,USD,S0103,1974-03-21,FACT,High,,"CONTEMPORANEOUS exact dollars; replaces A2's 30,734k from FY1976"
Walmart,stage1,FY1974,Number of shares outstanding,6542250,shares,S0103,1974-03-21,FACT,High,,"CONTEMPORANEOUS"
Walmart,stage1,FY1974,New store space added,881630,square feet,S0103,1974-03-21,FACT,High,,"20 new stores opened and 6 closed in FY1974; no total square footage is printed for FY1974"
Walmart,stage1,FY1974,Employees,4500,people,S0103,1974-03-21,FACT,Medium,,"chart label in the 'NUMBER OF EMPLOYEES' block; round figure; full/part-time composition UNKNOWN"
Walmart,stage1,FY1975,Net sales,236209,USD thousands,S0104,1975-03-28,ESTIMATE/DERIVED,Medium-High,"(5855+6353)+1800+48088+176591-2478 = 236209","FY1975's own printed top line is ABSENT from the text layer; derived by inverting the same table's five printed rows; U-A3/1 records the 226,209 vs 236,209 ambiguity; page image UNTRIED"
Walmart,stage1,FY1975,Net income,6353,USD thousands,S0104,1975-03-28,FACT,High,,"CONTEMPORANEOUS, asterisked in the original for the LIFO year; SFAS-13 restated value 5995 (S0108)"
Walmart,stage1,FY1975,Net income per share,0.95,USD/share,S0104,1975-03-28,FACT,High,,"CONTEMPORANEOUS, pre-split; restated basis prints $.45 primary / $.45 diluted in FY1979"
Walmart,stage1,FY1975,Income before income taxes,12208,USD thousands,S0104,1975-03-28,ESTIMATE/DERIVED,High,"5855+6353=12208","both components CONTEMPORANEOUS on FY1975's own page; restated basis 11,521 (S0108)"
Walmart,stage1,FY1975,Cost of sales,176591,USD thousands,S0104,1975-03-28,FACT,High,,"CONTEMPORANEOUS; first time FY1975's expense rows have their own witness"
Walmart,stage1,FY1975,Operating and selling and general and administrative expense,48088,USD thousands,S0104,1975-03-28,FACT,High,,"CONTEMPORANEOUS"
Walmart,stage1,FY1975,Store space added,1083326,square feet,S0104,1975-03-28,FACT,High,,"'a record for new store space in a single year'; FY1975 TOTAL square footage is UNKNOWN — no document prints it"
Walmart,stage1,FY1975,Associates,5800,people,S0104,1975-03-28,FACT,Medium,,"'its 5800 associates' / 'approximately 5800 associates'; company-stated"
Walmart,stage1,FY1977,Net sales,478807,USD thousands,S0106,1977-04-01,FACT,High,,"CONTEMPORANEOUS (FY1977 Eight-Year Summary); A2 held this only from the FY1980 ten-year table"
Walmart,stage1,FY1977,Income before income taxes,31833,USD thousands,S0106,1977-04-01,ESTIMATE/DERIVED,High,"15287+16546=31833","as-PUBLISHED; the SFAS-13 restated figure is 30,857 — U-A3/4 keeps both and forbids reading either as primary"
Walmart,stage1,FY1977,Net income,16546,USD thousands,S0106,1977-04-01,FACT,High,,"CONTEMPORANEOUS; restated 16,039"
Walmart,stage1,FY1977,Total assets,133158,USD thousands,S0106,1977-04-01,FACT,High,,"pre-SFAS-13 basis"
Walmart,stage1,FY1977,Long-term debt,23245,USD thousands,S0106,1977-04-01,FACT,High,,"single line in FY1977's own report; the FY1978 report splits the same date into 19,158 + 4,087 capital leases = 23,245 (A3-012)"
Walmart,stage1,FY1977,Total store space,6500000,square feet,S0106,1977-04-01,FACT,Medium,,"'approximately 6,500,000 square feet as of year-end', +24% on 1,300,000 of new space; approximate by the company's own word"
Walmart,stage1,FY1977,Distribution capacity,550000,square feet,S0106,1977-04-01,FACT,Medium,,"'some 550,000 square feet totally' of Bentonville distribution, incl. a new 150,000 sq ft DC completed November 1976 → 300,000 sq ft pure DC; ~80% of merchandise flowed through it (60% two years earlier)"
Walmart,stage1,FY1977,Associates,10000,people,S0106,1977-04-01,FACT,Medium,,"stated twice; round number; composition UNKNOWN"
Walmart,stage1,FY1977,Dividends per share,0.085,USD/share,S0106,1977-04-01,FACT,High,,"CONTEMPORANEOUS; refutes the FY1980 ten-year table's 1977 $.11 (COR-A3-04)"
Walmart,stage1,FY1978,Net sales,678456,USD thousands,S0107,1978-04-14,FACT,High,,"CONTEMPORANEOUS (Nine-Year Summary, the cleanest of the five layers); also printed as $678,456,000 in the FY1979 comparative column"
Walmart,stage1,FY1978,Income before income taxes,42186,USD thousands,S0107,1978-04-14,ESTIMATE/DERIVED,High,"20300+21886=42186","as-PUBLISHED; restated in FY1979 to 40,847"
Walmart,stage1,FY1978,Net income,21886,USD thousands,S0107,1978-04-14,FACT,High,,"CONTEMPORANEOUS; restated 21,191"
Walmart,stage1,FY1978,Total assets,206691,USD thousands,S0107,1978-04-14,FACT,High,,"as published; the SAME DATE is restated to 251,865 in the FY1979 report — see conflict U-A3/6 and metric note in §5.4/5.6"
Walmart,stage1,FY1978,Stockholders' equity,98943,USD thousands,S0107,1978-04-14,FACT,High,,"as published; 96,482 restated (206,691→251,865 assets; 10,904→59,003 capital leases)"
Walmart,stage1,FY1978,Stores in operation,195,stores,S0107,1978-04-14,FACT,High,,"30 new + 10 expanded/relocated + 16 acquired − 4 closed"
Walmart,stage1,FY1978,Total floor space in operation,8500000,square feet,S0107,1978-04-14,FACT,High,,"vs 6,500,000 'at the same time a year ago'"
Walmart,stage1,FY1978,Comparable-store sales growth,17,percent,S0107,1978-04-14,FACT,Medium,,"the ONLY same-store figure printed anywhere in the nine reports; the comparable-store population and dollar base are not defined ⇒ denominator UNKNOWN; §5.2 reconstructs and confirms internal consistency"
Walmart,stage1,FY1978,Gross margin,25.7,percent,S0107,1978-04-14,FACT,High,,"stated by management 'from 26.3 percent in 1977'; §5.5 derives 25.74%/26.34% independently and both agree"
Walmart,stage1,FY1978,Inventories,135845000,USD,S0107,1978-04-14,FACT,High,,"CONTEMPORANEOUS; LIFO basis, replacement cost $14,148,000 higher per FY1979 Note 2"
Walmart,stage1,FY1979,Net sales,900298000,USD,S0108,1979-04-06,FACT,High,,"CONTEMPORANEOUS from the audited income statement; A2 held FY1979 only from the FY1980 report"
Walmart,stage1,FY1979,Income before income taxes,56772000,USD,S0108,1979-04-06,FACT,High,,"printed line; 909,913,000 total revenues − 853,141,000 total costs = 56,772,000 ✓"
Walmart,stage1,FY1979,Net income,29447000,USD,S0108,1979-04-06,FACT,High,,"implies taxes of 27,325,000 = 48.1% effective"
Walmart,stage1,FY1979,Total assets,324666000,USD,S0108,1979-04-06,FACT,High,,"POST-SFAS-13 basis; 98,868,000 + 25,965,000 + 72,357,000 + 127,476,000 = 324,666,000 ✓ — NOT comparable with any pre-FY1979 asset figure"
Walmart,stage1,FY1979,Long-term obligations under capital leases,72357000,USD,S0108,1979-04-06,FACT,High,,"vs 10,904,000 for FY1978 as published — the lease capitalisation made visible"
Walmart,stage1,FY1979,Inventories,172640000,USD,S0108,1979-04-06,FACT,High,,"replacement cost (FIFO vs LIFO) $22,271,000 greater"
Walmart,stage1,FY1979,Distribution centre under construction,390000,square feet,S0107,1978-04-14,FACT,High,,"Searcy Arkansas, construction began during FY1978, completion tentatively June 1978, 'capability of servicing one-half of the existing Wal-Mart stores'"
Walmart,stage1,FY1979,Dividends per share,0.22,USD/share,S0108,1979-04-06,FACT,High,,"stated in the income statement parenthetical and as four quarterly payments of $.055"
Walmart,stage1,FY1979,Number of shares outstanding,15079383,shares,S0108,1979-04-06,FACT,High,,"CONTEMPORANEOUS (was FY1980-dated in A2)"
Walmart,stage1,FY1970,Total assets,8493,USD thousands,S0107,1978-04-14,FACT,High,,"RESTATED (in the FY1978 nine-year table) — the first statement of FY1970's balance sheet anywhere in this corpus; no FY1970 report exists"
Walmart,stage1,FY1970,Stockholders' equity,3159,USD thousands,S0107,1978-04-14,FACT,High,,"RESTATED (in FY1978); independently confirmed by the table's own return-on-equity row: 1,652 / 3,159 = 52.3 = printed FY1971 ROE"
Walmart,stage1,FY1970,Net income,1187764,USD,S0101,1972-03-22,FACT,Medium,,"'pro forma'; RESTATED (in FY1972, FY1973, FY1974 reports); the FY1978 table prints 1,011 thousand and its own rows imply 1,239 — see U-A3/2"
Walmart,stage1,FY1968,Net sales,12618754,USD,S0101,1972-03-22,FACT,High,,"RESTATED (in FY1972 report) and UNAUDITED — outside every opinion on disk; the earliest year any document counts"
Walmart,stage1,FY1962,Net sales,UNKNOWN,UNKNOWN,no document on disk states any FY1962-FY1967 financial figure,UNKNOWN,UNKNOWN,UNKNOWN,,"EMPTY, not thin: nine reports, all summary tables searched. Earliest counted year is FY1968"
Walmart,stage1,FY1976,Sales per square foot,64.27,USD per square foot,S0105,1976-03-26,ESTIMATE/DERIVED,Medium,"340331000 / 5295000 = 64.27","earliest computable year — no total square footage exists for FY1968-FY1975; denominator label undefined"
Walmart,stage1,FY1980,Sales per square foot,99.06,USD per square foot,S0109,1980-04-01,ESTIMATE/DERIVED,Medium,"1248176000 / 12600000 = 99.06",""
Walmart,stage1,FY1978,Sales per store (period-end count),3479262,USD per store,S0107,1978-04-14,ESTIMATE/DERIVED,Medium,"678456000 / 195 = 3479262","denominator is a PERIOD-END store count against a full-year numerator; average-store count is not printed for any year ⇒ the correct version of this metric is UNKNOWN"
Walmart,stage1,FY1979,Debt to equity,0.771,ratio,S0108,1979-04-06,ESTIMATE/DERIVED,High,"(25965000+72357000)/127476000 = 0.771","excluding capital leases 25,965/127,476 = 0.204; both figures reported because 'debt' has two definitions in these documents"
Walmart,stage1,FY1962-FY1967,Every financial and physical variable,EMPTY,UNKNOWN,all nine reports searched,1972-03-22 to 1980-04-01,UNKNOWN,UNKNOWN,,"EMPTY — a stated perimeter: the nine printed reports and every summary table in them"
```

### `timeline.csv` — header
```
company,stage,date_or_range,event,actors,location,source_id,evidence_class,confidence,conflict_ref,notes
```
### `timeline.csv` — rows
```csv
Walmart,stage1,1972-08-25,"Wal-Mart Stores, Inc. common stock listed for trading on the New York Stock Exchange",Wal-Mart Stores Inc.; NYSE,"New York, NY",S0103,FACT,High,none,"verbatim: 'August 25, 1972, the Company's stock was listed and began trading on the New York Stock Exchange'; OTC since October 1970. NEW contemporaneous fact the five downloads produced"
Walmart,stage1,1974-03-21,"Arthur Young & Company signs the unqualified report on the consolidated statements for the year ended January 31, 1974",Arthur Young & Company (Tulsa OK),"Tulsa, OK",S0103,FACT,High,none,"first of five newly-witnessed opinions"
Walmart,stage1,1975-01,"A new 150,000 square foot Distribution Center begins operation in Bentonville, consolidating case-pack merchandise previously shipped direct to stores",Wal-Mart Stores Inc.,"Bentonville, AR",S0104,FACT,High,none,"8 rail-car and 37 truck doors against the original DC's 6 and 28; ~60% of merchandise shipped through warehouse/DC in FY1975 vs 55% the prior year"
Walmart,stage1,1975-03-28,"Arthur Young qualifies its FY1975 opinion by exception for the change in the method of determining inventory cost (FIFO to LIFO), an change the auditor states it approves",Arthur Young & Company,"Tulsa, OK",S0104,FACT,High,U-A3/1,"the comparability break in the margin series is auditor-flagged, not footnoted: FY1975 earnings fall $2,347,000 ($.36 pre-split, $.18 post-split)"
Walmart,stage1,1976-11,"A second 150,000 square foot Bentonville distribution centre is completed, making 300,000 sq ft of 'pure distribution center' on a two-and-one-half-day cycle",Wal-Mart Stores Inc.,"Bentonville, AR",S0106,FACT,High,none,"total Bentonville distribution ≈550,000 sq ft through which ~80% of merchandise flows, up from 60% two years earlier"
Walmart,stage1,1977-04-01,"Arthur Young & Company signs the unqualified FY1977 report; wording has moved from 'consistent with that of the preceding year' to 'applied on a consistent basis during the period'",Arthur Young & Company,"Tulsa, OK",S0106,FACT,High,none,"the opinion now covers two years"
Walmart,stage1,1977,"Construction begins on a 390,000 square foot distribution center at Searcy, Arkansas, designed to service one-half of the existing stores",Wal-Mart Stores Inc.,"Searcy, AR",S0107,FACT,High,none,"automated conveyor at ~200 ft/min; combines DC I warehousing with DC II distribution; completion then tentative for June 1978"
Walmart,stage1,1977-10-01,"A group of sixteen stores is acquired in late summer, four stores closed during FY1978 including two of the acquired units",Wal-Mart Stores Inc.,multiple,S0107,FACT,Medium,none,"the only store-group acquisition in the window stated in its own year's report; identity of the seller is not given in the FY1978 report"
Walmart,stage1,1978-04-14,"Arthur Young & Company signs the unqualified FY1978 report",Arthur Young & Company,"Tulsa, OK",S0107,FACT,High,none,"the FY1978 report is the cleanest text layer of the five new documents and A3's reference copy for FY1970-FY1978"
Walmart,stage1,1979,"The remaining Sav-Co Home Improvement Center is closed, ending the nine-year second-format experiment begun in FY1975",Wal-Mart Stores Inc.,"Bentonville, AR",S0108,FACT,High,none,"FY1975 opened two Sav-Co centres totalling 54,000 sq ft and already conceded they 'will not be expanded until [they are] operating at our expected profitability level'"
Walmart,stage1,1979-04-06,"Arthur Young signs the FY1979 report carrying the clause that prior-year statements were restated retroactively for the change in the method of accounting for leases (SFAS 13), a change the auditor concurs in",Arthur Young & Company,"Tulsa, OK",S0108,FACT,High,"U-A3/4, U-A3/5, U-A3/6","the authorising document for the restatement of FY1975-FY1978 — a second restating document one year earlier than A2's only one"
Walmart,stage1,1945,"Sam M. Walton opens his first Ben Franklin franchise variety store in Newport, Arkansas — as narrated by the registrant in 1974, 1975, 1977, 1978 and 1979",Sam M. Walton; Ben Franklin,"Newport, AR",S0104,FOUNDER CLAIM,Low,"see COR-A3-10","NO 1945 document exists in this corpus; five dated repeatings inside ONE lineage do not make a second source (§3 filing-lineage rule)"
Walmart,stage1,1962-11,"The first Wal-Mart Discount City opens in Rogers, Arkansas, a town of 'approximately 4700' (FY1975) / 'approximately 5,000 people' (FY1978)",Sam M. Walton; J. L. 'Bud' Walton,"Rogers, AR",S0104,FOUNDER CLAIM,Low,U-A3/8,"the month is stated in the FY1975 and FY1978 reports; no 1962 price, no opening-day takings, and no witness outside the registrant"
```

### `sources.csv` — header
```
source_id,stage,claim_supported,source_title,author_or_publication,source_type,primary_or_secondary,event_date,publication_date,access_date,url,archived_url,tier,evidence_class,confidence,independence_note,relevant_passage,notes
```
### `sources.csv` — rows
```csv
S0101,1,FY1972 statements and the FY1968-FY1972 five-year summary,"Wal-Mart Stores, Inc. Annual Report, fiscal year ended January 31, 1972",Wal-Mart Stores Inc.; Arthur Young & Company,printed registrant annual report,primary,1972-01-31,1972-03-22,2026-09-24,https://archive.org/details/1972-annual-report-for-walmart-stores-inc,sources/periodicals/WALMART_AR_1972.txt,1,FACT,High,one of nine documents in the same registrant lineage,"5 YEAR FINANCIAL SUMMARY OPERATING RESULTS .._ YEARS ENDED JANUARY 31 Sales $78,014,164 $44,286,012 $30,862,659 $21,365,081 $12,618,754","earliest document physically present in the corpus; its opinion names 'the year then ended' only"
S0102,1,FY1973 statements and comparatives,"Wal-Mart Stores, Inc. Annual Report, fiscal year ended January 31, 1973",Wal-Mart Stores Inc.; Arthur Young & Company,printed registrant annual report,primary,1973-01-31,1973-03-20,2026-09-24,https://archive.org/details/1973-annual-report-for-walmart-stores-inc,sources/periodicals/WALMART_AR_1973.txt,1,FACT,High,same lineage as S0101,"","carries FY1972's legible cost of sales $58,591,379 which A2 needed to derive the FY1972 margin"
S0103,1,"FY1974 contemporaneous money, shares, equity, inventories, store additions, NYSE listing","Wal-Mart Stores, Inc. Annual Report, fiscal year ended January 31, 1974",Wal-Mart Stores Inc.; Arthur Young & Company,printed registrant annual report,primary,1974-01-31,1974-03-21,2026-09-24,https://archive.org/details/1974-annual-report-for-walmart-stores-inc,sources/periodicals/WALMART_AR_1974.txt,1,FACT,High,same lineage as S0101,"Net Sales $30,862,659 $44,286,012 $78,014,164 $124,889,141 $167,560,892","NEW to A3; complete scan; five-year table fully legible; AUDITED STATEMENT PAGES interleave and drop cells — take FY1974 money from the five-year table, not the statement rows; SHA-256 e0781cac…90a06"
S0104,1,"FY1975 earnings, expense rows, headcount, store fleet, DC capacity, LIFO break, 1945/1962 narrative","Wal-Mart Stores, Inc. Annual Report, fiscal year ended January 31, 1975",Wal-Mart Stores Inc.; Arthur Young & Company,printed registrant annual report,primary,1975-01-31,1975-03-28,2026-09-24,https://archive.org/details/1975-annual-report-for-walmart-stores-inc,sources/periodicals/WALMART_AR_1975.txt,1,FACT,Medium-High,same lineage as S0101,"The change resulted in a decrease in earnings of $2.3 million, or $.36 per share, for fiscal 1975","NEW to A3; WORST of the five for current-year money: FY1975's own column numerals dropped on every audited statement page; net sales, total assets and equity NOT recoverable from the text layer; SHA-256 79b8603b…31189c"
S0105,1,FY1976 statements and the ten-year/summary comparatives,"Wal-Mart Stores, Inc. Annual Report, fiscal year ended January 31, 1976",Wal-Mart Stores Inc.; Arthur Young & Company,printed registrant annual report,primary,1976-01-31,1976-03-26,2026-09-24,https://archive.org/details/1976-annual-report-for-walmart-stores-inc,sources/periodicals/WALMART_AR_1976.txt,1,FACT,High,same lineage as S0101,"Common stock outstanding was increased 6,687,789 shares by a two-for-one stock split effective August 19. 1975","source of the corrected split date (COR-A3-07); its employee and square-footage charts are OCR-damaged"
S0106,1,"FY1977 contemporaneous income, balance sheet, dividends, stores, total and DC square footage, headcount, 1945/1946/1962 narrative","Wal-Mart Stores, Inc. Annual Report, fiscal year ended January 31, 1977",Wal-Mart Stores Inc.; Arthur Young & Company,printed registrant annual report,primary,1977-01-31,1977-04-01,2026-09-24,https://archive.org/details/1977-annual-report-for-walmart-stores-inc,sources/periodicals/WALMART_AR_1977.txt,1,FACT,High,same lineage as S0101,"Until 1962, the Company's business was devoted to the operation of variety stores.","NEW to A3; complete scan; text layer complete but COLUMN-MAJOR REFLOW — pair labels to values by position within the year block, never by adjacency; SHA-256 f398a40d…ba500"
S0107,1,"FY1978 contemporaneous income, balance sheet, dividends, stores, square footage, comparable-store growth; and the nine-year restatement of FY1970-FY1977","Wal-Mart Stores, Inc. Annual Report, fiscal year ended January 31, 1978",Wal-Mart Stores Inc.; Arthur Young & Company,printed registrant annual report,primary,1978-01-31,1978-04-14,2026-09-24,https://archive.org/details/1978-annual-report-for-walmart-stores-inc,sources/periodicals/WALMART_AR_1978.txt,1,FACT,High,same lineage as S0101,"Comparable stores sales (excluding the effect of new stores) increased 17 percent","NEW to A3; CLEANEST layer of the five — designated reference copy for FY1970-FY1978; no audited-statement page and no nine-year-table column missing; 18 row/column identities verified arithmetically; SHA-256 10a30c39…62978f"
S0108,1,"FY1979 contemporaneous income, balance sheet, dividends, headcount, retail space; and the SFAS-13 restatement of FY1975-FY1978","Wal-Mart Stores, Inc. Annual Report, fiscal year ended January 31, 1979",Wal-Mart Stores Inc.; Arthur Young & Company,printed registrant annual report,primary,1979-01-31,1979-04-06,2026-09-24,https://archive.org/details/1979-annual-report-for-walmart-stores-inc,sources/periodicals/WALMART_AR_1979.txt,1,FACT,High,same lineage as S0101; it is ALSO a restating document for FY1975-FY1978,"All financial information prior to 1979 has been restated to reflect the retroactive application of Statement of Financial Accounting Standards No. 13","NEW to A3; complete scan (24 pp); TEN-YEAR SUMMARY numeric cells unreadable — do NOT read a multi-year series out of this file; income statement, balance sheet, two-year comparison, Five-Year Financial Review, notes and market-price tables all render; SHA-256 ad6958cf…c7095c"
S0109,1,FY1980 statements and the ten-year restated summary,"Wal-Mart Stores, Inc. Annual Report, fiscal year ended January 31, 1980",Wal-Mart Stores Inc.; Arthur Young & Company,printed registrant annual report,primary,1980-01-31,1980-04-01,2026-09-24,https://archive.org/details/1980-annual-report-for-walmart-stores-inc,sources/periodicals/WALMART_AR_1980.txt,1,FACT,High,same lineage as S0101,"","its ten-year table's dividend row is refuted by S0106/S0107/S0108 (COR-A3-04); its middle rows are OCR-damaged (A2 W-69, caveat now discharged by S0108)"
S0110,1,"Provenance and byte-level completeness of the five interior-year reports: URLs, item identifiers, retrieval timestamps, SHA-256, page inventories","IA_A2_interior_years_fetch_evidence_20260924.json + the PROVENANCE HEADER block at the head of each WALMART_AR_197x.txt",THE FOUNDER'S PLAYBOOK evidence-registrar (this project),retrieval provenance register,secondary,2026-09-24,2026-09-24,2026-09-24,local,sources/periodicals/IA_A2_interior_years_fetch_evidence_20260924.json and _PROVENANCE_PERIODICALS.md,n/a,METHOD ARTEFACT,High,self-record,"COMPLETENESS: **complete scan, no page absent, but PARTIAL-WITH-GAPS as machine-readable text.**","every CONTEMPORANEOUS / NOT-RECOVERABLE claim in this dossier about a text layer rests on these headers, not on the registrant"
S0111,1,"The unresolved digit ambiguity in FY1975's top line and the unreadable FY1970 net-income cell: both are recorded, neither is settled","WALMART_AR_1975.txt and WALMART_AR_1974 and WALMART_AR_1978 page-image leads (_djvu.xml page map; _text.pdf 3.7 MB)",Internet Archive hosting of the Wal-Mart report collection,page-image lead,primary,1975-03-28,1974,2026-09-24,https://archive.org/details/1975-annual-report-for-walmart-stores-inc,metadata declared in each item — bytes NOT retrieved,1,LEAD / UNTRIED,UNKNOWN,one of nine documents in the same registrant lineage,"text layer '…_djvu.txt' (DjVuTXT, 39,954 B) declared, plus _djvu.xml page map (448,062 B) and page-image PDFs (3,243,815 B / _text.pdf 3,706,555 B) for anyone re-walking a figure to the printed page","THE HIGHEST-VALUE UNTRIED ITEM IN THE DOSSIER; it is cheap and needs one fetch; deliberately not spent this pass so the register got written instead"
```

### `conflicts.csv` — header
```
company,stage,conflict_id,section,claim_a,claim_a_source,claim_a_date,claim_b,claim_b_source,claim_b_date,why_they_differ,evidence_weight,best_supported_interpretation,residual_uncertainty,confidence
```
### `conflicts.csv` — rows
```csv
Walmart,stage1,U-A3/1,"P; A3 §3.4","FY1975 net sales = $236,209 thousand",WALMART_AR_1977/1978/1979 reports and the inversion of WALMART_AR_1975.txt's own five rows,1977-04-01,"FY1975 net sales = $226,209 thousand",WALMART_AR_1976.txt five-year table text layer,1976-03-26,"OCR of a 2/3 digit in a stacked numeric column, plus the FY1975 top-line cell being absent from its own text layer — a machine failure, not a company one","four printings for A against one for B, and B disagrees with a fifth witness (the FY1975 report's own row identity)","$236,209 thousand","the contemporaneous PRINTED top line has never been read off a printed page; the FY1975 _text.pdf is UNTRIED",Medium-High
Walmart,stage1,U-A3/2,"P; A3 §3.8","FY1970 net income = $1,187,764 (pro forma)",WALMART_AR_1972/1973/1974 reports,1974-03-21,"FY1970 net income = 1,011 thousand",WALMART_AR_1978.txt Nine-Year Summary FY1970 column,1978-04-14,"unknown — and the FY1978 table is internally inconsistent: its own rows give pre-tax 2,199 (matching claim A's $2,198,764) and taxes 960, which require net income 1,239","three documents for A, one for B, and B disagrees with itself","$1,187,764 stays the register value; the FY1978 FY1970 net-income cell is marked SUSPECT, not corrected","whether 1,011 is an OCR mis-read or a genuine second (actual vs pro forma) basis cannot be told without the FY1978 page image, UNTRIED",Medium for A / Low for B
Walmart,stage1,U-A3/3,"P; A3 Table S3","FY1973 shares outstanding = 6,512,950",WALMART_AR_1974.txt balance-sheet block,1974-03-21,"FY1973 shares outstanding = 6,512,550",WALMART_AR_1973.txt L103-108 as read by A2,1973-03-20,"one digit (9 vs 5) in a typewritten statement, or a genuine restatement of a year-end count between the two documents","one printing each","neither; record both and forbid quoting a single FY1973 count at High","immaterial to every ratio in §5.6 (400 shares in 6.5m); page images of both reports UNTRIED",Medium
Walmart,stage1,U-A3/4,"P; A3 Tables S1/S3; §5.5","FY1977 pre-tax 31,833 and net income 16,546; FY1978 42,186 and 21,886",WALMART_AR_1977.txt and WALMART_AR_1978.txt own tables,1978-04-14,"FY1977 pre-tax 30,857 and net income 16,039; FY1978 40,847 and 21,191",WALMART_AR_1979.txt Five-Year Financial Review; repeated in WALMART_AR_1980.txt ten-year table,1979-04-06,"SFAS 13 (Accounting for Leases) applied retroactively with the auditor's concurrence — a documented accounting change, not an error","both Tier-1, both dated, both complete","both, for different purposes: A for 'what the company reported at the time', B for comparison with FY1979/FY1980","A2 printed B's values inside a row titled 'as printed' at High, so A2's own EPS and margin steps cannot be attributed to a basis",High
Walmart,stage1,U-A3/5,"P; A3 §5.5","The FY1978 SFAS-13 restatement 'reduced net earnings $769,000, or 5 cents per share'",WALMART_AR_1979.txt Management's Analysis,1979-04-06,"The FY1978 restatement reduced net earnings by $695,000","WALMART_AR_1979.txt income statement and retained-earnings bridge (2,461,000 minus 1,766,000; 21,886 minus 21,191)",1979-04-06,"unknown — a pre-publication figure surviving in prose, or a different measure than net income; no reconciling line exists","two independent arithmetic paths inside the same document give 695; the prose gives 769; the '5 cents' fits either at ~15m shares","695 for the income-statement effect; 769 recorded as the company's own stated number and not retracted","$74,000, i.e. 0.3% of FY1978 net income, unreconciled INSIDE one audited document",High
Walmart,stage1,U-A3/6,"P; A3 Table S4","FY1978 total assets = $206,691 thousand",WALMART_AR_1978.txt Nine-Year Summary,1978-04-14,"FY1978 total assets = $251,865 thousand",WALMART_AR_1979.txt comparative balance sheet,1979-04-06,"SFAS-13 lease capitalisation brought lease assets and liabilities on to the balance sheet: +45,174 assets against +48,099 of capital-lease obligations, with equity falling only 2,461","both are Tier-1 statements of the same date by the same firm; B has the later recognition rule behind it","B for comparison with FY1979/FY1980, A for comparison with FY1970-FY1977; THE ASSET SERIES IS BROKEN AND IS PRINTED BROKEN","A2's Total assets row mixed the bases silently, so any A2-derived asset growth or turn across 1978/1979 is invalid",High
Walmart,stage1,U-A3/7,"P; §5.5",FY1974/FY1975/FY1976 expense structure 21.1% / 20.5% / 20.8% of sales,WALMART_AR_1977.txt Chairman's Message,1977-04-01,operating + S&G + administrative expense ÷ net sales = 19.72% / 20.36% / 20.01% / 20.43% for FY1974-FY1977,WALMART_AR_1977.txt Eight-Year Summary (same document),1977-04-01,"the letter's denominator is unstated and its fiscal-year labels appear to run by STARTING calendar year (its gross-margin '+.2%' matches FY1976→FY1977); even remapped, 20.8% exceeds the computed 20.43%","the table is auditable arithmetic on printed rows; the letter is management prose with an unstated base","none — the letter's series is recorded as STATED-BUT-NOT-RECONCILABLE and EXCLUDED from §5.5","whether 'total expense structure' includes interest, pre-opening costs or leases; the document does not say. DENOMINATOR NOT STATED ⇒ UNKNOWN",High (that it does not reconcile) / UNKNOWN (what it measures)
Walmart,stage1,U-A3/8,"C; D",Rogers Arkansas population at the November 1962 opening was 'approximately 4700',WALMART_AR_1975.txt company profile,1975-03-28,"… 'approximately 5,000 people'",WALMART_AR_1978.txt founding narrative,1978-04-14,"rounding of the same census figure, or a different informal source","equal; one lineage, three years apart","'approximately 4,700-5,000 per the company's own two statements'","no census record in this corpus; the 1962 opening still has no witness outside the registrant",Medium (as a range) / Low (as a fact)
Walmart,stage1,U-A3/9,"P; A3-012","FY1977 long-term debt = 23,245 thousand (one line)",WALMART_AR_1977.txt Eight-Year Summary,1977-04-01,"FY1977 long-term debt = 19,158 plus capital-lease obligations 4,087 (two lines)",WALMART_AR_1978.txt Nine-Year Summary,1978-04-14,"presentation change: the FY1978 report split out the capital-lease component of the same total (19,158 + 4,087 = 23,245, exact)","both Tier-1 and self-consistent","both, labelled; leverage for one date is 0.351 or 0.289 depending on which print is used","whether FY1977's single line was a presentation shortcut or a different classification standard; no document says",High
```

