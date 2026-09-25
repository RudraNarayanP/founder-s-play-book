# A3 — Walmart Audited Financial Series, FY1962–FY1980 (contemporaneous vs restated register)

**Dataset:** THE FOUNDER'S PLAYBOOK — forensic longitudinal reconstruction
**Company:** Walmart (Ben Franklin era through the first public years) — `company_002_walmart`
**Stage:** 1
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

**To be completed from the documents; the write-first skeleton record is here.**

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

**Append-after-each-year register.** Records A3-008 onward.

### Table S1 — Net sales

| FY | Value as printed | Unit / basis | Status | Document that states it | A3 record |
|---|---|---|---|---|---|
|---|---|---|---|---|---|

### Table S2 — Stores, square footage, DC capacity, headcount

### Table S3 — Operating profit, pre-tax income, net income, EPS, dividends

### Table S4 — Balance sheet: shares outstanding, equity, total assets, inventories, debt

---

## 4. Delta table against A2

## 5. Derived metrics (arithmetic shown; every row DERIVED)

## 6. Auditor and attestation note

## 7. Evidence-family verdict, re-derived + Stage-1 depth verdict

## Contradictions

## Data gaps

## Outbound corrections

## CSV append rows
