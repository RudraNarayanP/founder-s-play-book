# WALMART — PERIODICAL / DOCUMENTARY RETEST: PROVENANCE REGISTER

Append-only. Created by `../../research/B_periodical_retest.md` (Level-3 Fast-tier Corpus Retester)
on **2026-09-24**. **Create files only** — nothing in `company_002_walmart/sources/` (this directory
included) may be deleted, moved, renamed or "tidied" by any agent. Nothing was removed or renamed
during this run; the pre-existing probe files one level up (`EDGAR_*`, `probe_*`, `EXTRACT_*`,
`_RETRIEVAL_LOG.md`) were opened read-only and never written.

Header convention used here (per `00_METHOD_AND_STYLE.md` §14 rule 6 and the Apple probe's practice):
a 5-line `# [PROVENANCE HEADER …]` block **prepended** to each retrieved primary file, with **not one
byte of the retrieved body altered, added to or removed beneath it**.

## A. Primary documents retrieved (Tier 1) — full text on disk

| File | Bytes on disk | Retrieved from (URL) | Access date | What it is / what it settles |
|---|---|---|---|---|
| `WALMART_AR_1972.txt` | 26,029 | https://archive.org/details/1972-annual-report-for-walmart-stores-inc → `metadata` → `https://ia…us.archive.org/11/items/…/1972-annual-report-for-walmart-stores-inc_djvu.txt` | 2026-09-24 | **Wal-Mart Stores, Inc. printed Annual Report, FY ended 1972-01-31** (President's message signed Sam M. Walton 1972-03-22). Carries: "5 Year Financial Summary" FY1968→FY1972 (sales $12,618,754 / $21,365,081 / $30,862,659 / $44,286,012 / $78,014,164); the **1970-02-01 exchange of common stock accounted for as a pooling of interests, transferred by "the principal shareholder (Walton Enterprises, Inc.)"** with a $968,876 bank note assumed; eighteen pre-1970-02-01 Wal-Mart stores with 17 % same-store growth; DC 60,000→124,800 sq ft completed 1971-08-15; 6,000,000 shares $.10 par; **IRS proposed assessments for the year ended 1969-01-31**. → WR-01, WR-04…WR-07, WR-12 |
| `WALMART_AR_1973.txt` | 31,727 | https://archive.org/details/1973-annual-report-for-walmart-stores-inc (same route) | 2026-09-24 | **FY ended 1973-01-31.** "Six Years at a Glance" store series **24 · 27 · 32 · 38 · 51 · 64** and pro-forma income/EPS series; "twenty-eight year history" (1973 ⇒ origin 1945); General Office + DC enlarged to 261,800 sq ft in 1972; same-store +11 % "excluding one store near a new Wal-Mart store"; warrants at $4.12 expiring 1985-04-01; **Arthur Young & Company** as Independent Accountants; store-locations list by state (Arkansas incl. **Newport** and **Rogers**). → WR-02, WR-08, WR-11, WR-12, WR-15 |
| `WALMART_AR_1976.txt` | 66,477 | https://archive.org/details/1976-annual-report-for-walmart-stores-inc (same route) | 2026-09-24 | **FY ended 1976-01-31.** 125 stores (+21); 5,295,000 sq ft (+23 %); **leases for 24 future stores, aggregate minimum annual rentals $2,029,000**; financing "reinvestment of earnings … bank borrowings, until May, 1975, at which time the Company issued $15 million of co[nvertible]"; Ben Franklin variety store at Rogers closed January 1976; Security and Loss Prevention Division (shoplifter apprehension, interrogation, prosecution); expanded Arkansas store list. → WR-13, WR-14, WR-15 |
| `WALMART_AR_1980.txt` | 71,918 | https://archive.org/details/1980-annual-report-for-walmart-stores-inc (same route) | 2026-09-24 | **FY ended 1980-01-31.** The single most valuable document recovered: **"Wal-Mart's Past — Foundation for the Future"** — "The first Wal-Mart Discount City store was opened in 1962 in Rogers, Arkansas by Sam M. Walton and his brother James L, Walton"; origin "predates … by 17 years"; "Beginning in 1945, with a Ben Franklin franchised store in **Newport, Arkansas**, the Walton brothers assembled a group of fifteen variety stores, most of them in small towns in Arkansas, Missouri and Kansas"; **"On January 1, 1970 … the Company owned and operated 18 Wal-Marts and 14 Ben Franklin variety stores in a four-state area, with sales totaling $31 million"**; first store of the 1970s decade at St. Robert, Missouri; Ten-Year Financial Summary FY1971–FY1980 and five-year table 125/153/195/229/276 stores. **This is a pre-memoir (1980 vs 1992) corporate account of the founding.** → WR-09, WR-10, WR-20, WR-25 |

**Route note for the fleet:** `https://archive.org/download/<id>/<file>` 302-redirects to a CDN that
fails from this environment. Use `https://archive.org/metadata/<id>` → `server` + `dir` →
`https://<server><dir>/<name>_djvu.txt`. The whole printed run is
`1972-…` through `1997-annual-report-for-walmart-stores-inc` (26 items), plus `walmart199000harv`.

## A-2. Interior years FY1974 · FY1975 · FY1977 · FY1978 · FY1979 — retrieved (Tier 1), second pass 2026-09-24

**Why this section exists.** The five reports below were **not** a corpus absence: they are the
interior years of the same printed run that produced §A's four files, and they were sitting on the
host the whole time. Outbound correction `COR-A2-10` (in `../../research/A2_chronology_finance.md`)
read the nightly harvest (`00_universe/harvest/candidates.csv`, query
`CP walmart annual-report run 1970-1998 (EXEMPLAR)`, HTTP 200, `retrieved_at 2026-09-24T10:33:13Z`)
and found the run enumerated **contiguous FY1972 → FY1998 — 27 `TIER1_CANDIDATE` rows, one per
fiscal year**, i.e. **FY1998 also exists**, which understates this register's own §A route note
above ("…through 1997…(26 items)"); that line is left in place unedited and is corrected forward
here. **This pass therefore converted a download gap into primary text: FY1974, FY1975, FY1977,
FY1978 and FY1979 are now on disk, each carrying its own year's audited table.** All five retrieved
at **HTTP 200 with an exact byte match against the size declared in the item's own metadata**; the
reusable route is unchanged (identifier → `metadata/<id>` → `server`+`dir` → `_djvu.txt`).
Machine-readable proof of every request (URLs as issued, timestamps, `Content-Length`, SHA-256 of
each body, full lead metadata) is preserved in **`IA_A2_interior_years_fetch_evidence_20260924.json`**
(26,952 B) in this directory. Reading the "Bytes on disk" column: the figure is the file's total size,
the first parenthetical number is the prepended provenance header and the second is the **retrieved
text-layer body as delivered** (LF); on disk that body carries CRLF, so it occupies a few thousand
bytes more — the header + body figures are therefore *content* measures, not a sum to the total.

| File | Bytes on disk | Retrieved from (URL) | Access date | What it is / what it settles |
|---|---|---|---|---|
| `WALMART_AR_1974.txt` | 47,166 (header 5,487 + body 39,954) | https://archive.org/details/1974-annual-report-for-walmart-stores-inc → `metadata` → `https://ia801507.us.archive.org/5/items/1974-annual-report-for-walmart-stores-inc/…_djvu.txt` (HTTP 200, 13:43:15Z, 39,954 B = metadata-declared) | 2026-09-24 | **FY ended 1974-01-31. The cleanest FY1970–FY1974 series in the corpus**: p.1 "Five Year Progress Report" gives, on one legible page, Net Sales $30,862,659 / $44,286,012 / $78,014,164 / $124,889,141 / $167,560,892; income before taxes $2,198,764 → $11,883,754; **pro forma** net income $1,187,764 → $6,158,520; pro forma EPS $.23/$.30/$.47/$.70/$.93; **stores 32 · 38 · 51 · 64 · 78\*** with the footnote **"Two Ben Franklin variety stores were sold and four were closed during the year."** Also: **"twenty-nine year history"** (1974 ⇒ origin 1945); 20 opened / 6 closed FY1974 vs 16 / 3 FY1973; **Marshfield MO Ben Franklin Family Center converted to a 29,100 sq ft Wal-Mart**; **Rogers AR relocated 35,000→56,000 sq ft**; Jonesboro AR (tornado V. 1973) and Berryville AR (fire XII. 1972) rebuilt; 881,630 sq ft added; **twenty-six pharmacies** in leased departments; total store sales incl. leased depts $182,634,000; **Arthur Young opinion, Tulsa, 1974-03-21, unqualified**. ⚠ Text layer is **partial-with-gaps on the statement pages only** (row/column interleaving; the "Net sales" row prints FY1973's figure and prints it as "$124,059, 141") — header in the file lists exactly which rows are affected. |
| `WALMART_AR_1975.txt` | 66,591 (header 5,680 + body 58,278) | …/details/1975-annual-report-for-walmart-stores-inc → `https://ia800408.us.archive.org/13/items/1975-annual-report-for-walmart-stores-inc/…_djvu.txt` (HTTP 200, 13:43:19Z, 58,278 B = declared) | 2026-09-24 | **FY ended 1975-01-31. Retrieved, and the one year whose own current-year numbers the OCR will not give up.** What IS on the contemporaneous text layer: "Five Year Summary" rows FY1975→FY1971 — **net income 6,353\* / 6,159 / 4,591 / 2,907 / 1,652; EPS .95\* / .93 / .70 / .47 / .30**; cost of sales 176,591/123,339/93,090/58,592/32,825; opex 48,088/33,044/23,848/14,285/8,441; interest 1,800/1,099/592/415/195; taxes 5,855/5,725/4,326/2,662/1,519; current assets 55,860/45,254/32,787/21,069/12,150 — plus Management's Analysis percentages (gross margin **25.2 % vs 26.4 %**, SG&A 20.4 % vs 19.7 %, advertising 1.4 % vs 1.2 %, rent 2.4 % vs 2.2 %) and the quarterly net-income-before-LIFO table. Founding narrative in the company's own words: **Newport, Arkansas 1945** first Ben Franklin; Bud Walton joins "one year later"; **fifteen Ben Franklin stores 1945–1962**; **"Wal-Mart's first Discount City store opened in Rogers, Arkansas (then a town of approximately 4700), in November 1962"**; fleet **100 Wal-Marts + 2 Family Centers + 2 Sav-Co**, AR 37 / MO 36 / OK 15 / KS 6 / TN 6 / LA 2 / MS 1 / KY 1; 26 new stores, 1,083,326 sq ft. **Arthur Young opinion 1975-03-28 carries the LIFO-change exception** ("except for the change, which we approve, in the method of determining inventory cost as described in Note 2"). ⚠ **GAPS: the FY1975 own-column numerals are dropped from every audited statement page** (column head prints "WTjJM 1974"; only FY1974 comparatives survive; balance-sheet 1975 cells render as "KlHHWil", "F^ffftEffjfcjJ"), and the Five Year Summary's **Net sales row carries 4 values against 5 column heads — FY1975's top line is absent** (cf. $226,209 in FY1976's table vs $236,209 in FY1977/FY1978's). FY1975 net sales / total assets / equity ⇒ **page image `_text.pdf`, still UNANSWERED by this pass.** |
| `WALMART_AR_1977.txt` | 71,075 (header 5,239 + body 62,803) | …/details/1977-annual-report-for-walmart-stores-inc → `https://ia800501.us.archive.org/1/items/1977-annual-report-for-walmart-stores-inc/…_djvu.txt` (HTTP 200, 13:43:24Z, 62,803 B = declared) | 2026-09-24 | **FY ended 1977-01-31.** Cover "Annual Report January 31, 1977". **"Eight-Year Summary" = FY1970→FY1977 in one contemporaneous table**: net sales $30,863 · $44,286 · $78,015 · $124,889 · $167,561 · $236,209 · $340,331 · **$478,807** (thousands); net income … 1,011 · 1,652 · 2,907 · 4,591 · 6,159 · 6,353\* · 11,506 · **16,546**; **stores 32 · 38 · 51 · 64 · 78 · 104 · 125 · 153** (FY1970→FY1977; the **104** for FY1975 — also present in `WALMART_AR_1976.txt` at body lines 1144 / 1580 — cross-checks FY1975's own narrative "100 Wal-Mart Discount City stores, two Family Center stores and two Sav-Co Home Improvement Centers"); EPS primary $1.19 / fully diluted 1.12; dividends .085; total assets 133,158; equity 66,183; ROA 16.5 / ROE 34.1. Founding paragraph: **"first unit was a franchised Ben Franklin variety store, opened in 1945, in Newport, Arkansas by Sam M. Walton. In 1946, his brother, J. L. 'Bud' Walton, opened a similar store in Versailles, Missouri"** … first Discount City **Rogers, Arkansas, 1962**; store sizes 30,000–60,000 sq ft, **average ≈42,000**; thirty-six full-line departments; "Research and Development Committee Formed"; **Arthur Young, Tulsa, 1977-04-01, unqualified**. ⚠ Complete scan, no page missing, but the layer is **column-major reflowed** (labels first, then each year's values as a stacked block) so row↔value pairing is positional, and FY1975's net sales reads **"$236,209"** here against "$2?6,209" in FY1976 — a live 2/3 digit ambiguity for the page image. |
| `WALMART_AR_1978.txt` | 81,039 (header 5,625 + body 72,300) | …/details/1978-annual-report-for-walmart-stores-inc → `https://ia802902.us.archive.org/14/items/1978-annual-report-for-walmart-stores-inc/…_djvu.txt` (HTTP 200, 13:43:28Z, 72,300 B = declared) | 2026-09-24 | **FY ended 1978-01-31 — and the best OCR of the five, so treat it as the reference copy for FY1970→FY1978.** **"Nine-Year Summary"** inline pair + stacked older columns: net sales **$678,456** / $478,807 / $340,331 / $236,209 / $167,561 / $124,889 / $78,015 / $44,286 / $30,863; net income **21,886** / 16,546 … ; EPS $1.53 / $1.19; dividends .16; **stores 195 / 153**; current assets 150,986/99,493; **long-term obligations under capital leases 10,904 / 4,087** (pre-SFAS 13 presentation); equity 98,943/66,183; RmA 16.4 / RoE 33.1. Two-year comparison and income statement print **both columns on the same line**. Narrative: **390,000 sq ft Searcy, Arkansas DC begun 1977, completion "tentatively set for June 1978"**; 30 new stores + 10 expanded/relocated; the independent survey ranking Wal-Mart **first in all four of Return on Equity, Return on Capital, Sales Growth, Earnings Growth** against discount/department/variety chains over five preceding years; founding paragraph (**Newport 1945**, **partnership in 1946**, fifteen Ben Franklins, **first discount store November 1962 in Rogers, "then a small, primarily agricultural community of approximately 5,000 people"**, average community 5,000–25,000, largest cities Little Rock and Springfield MO); **LIFO footnote "$2,347,000 or $.18 per share"**; **Arthur Young, Tulsa, 1978-04-14, unqualified**. Minor gaps are typographic only (right-margin letter loss on narrow narrative columns; decimal-comma confusions). |
| `WALMART_AR_1979.txt` | 77,773 (header 6,343 + body 67,946) | …/details/1979-annual-report-for-walmart-stores-inc → `https://ia801507.us.archive.org/25/items/1979-annual-report-for-walmart-stores-inc/…_djvu.txt` (HTTP 200, 13:43:33Z, 67,946 B = declared) | 2026-09-24 | **FY ended 1979-01-31 — closes the window at the top of the decade.** Audited two-year pages are clean and print **FY1979 net sales $900,298,000**, leased-dept rentals 6,344,000, other income 3,271,000, total revenues 909,913,000, cost of sales 661,062,000, opex 188,592,000, interest 3,487,000, income before taxes **56,772,000**, against FY1978's $678,456,000 … 40,847,000; **stores 229 / 195**; highlights block: current assets $191,860,000, equity $127,476,000, **shares outstanding 15,079,383**. Prose: net income **$29.4 m, +39 %**, **EPS $1.93 vs $1.41**; **"Earnings for 1978 have been restated to reflect the retroactive application of SFAS 13 … reduced net earnings $769,000, or 5 cents per share"**; the report's own declaration that **"All financial information prior to 1979 has been restated…"** (so this file is itself a restating document for its history column — see the depth note below). Narrative: **"first discount store opened 17 years ago"**; **1945 Newport Ben Franklin**; **Bud Walton, Versailles, Missouri**; **15 Ben Franklin stores between 1946 and 1962**; **first Wal-Mart Discount City, Rogers, 1962**; **"publicly-owned since October, 1970"**; NYSE: WMT; 35 new stores and the **closure of the remaining Sav-Co Home Improvement Center**; quarter-by-quarter market price on both fiscal and calendar bases; **Arthur Young, Tulsa, 1979-04-06** with the SFAS-13 restatement clause. ⚠ **The "TEN-YEAR SUMMARY" numeric cells are the one unreadable block in the five files** ("5900,298", "3>678.456", "GOl,UbZ", "5uo,o25", "■ oo<oy^", "$340 3T1", "U7R R07") — use FY1978's nine-year table plus FY1979's own statements instead. |

### Depth consequence of A-2 (stated once, for the merge, not asserted in §A)

FY1972→FY1980 is now **one unbroken run of printed reports, each year's money on that year's own
page**: FY1972 · FY1973 · **FY1974** · FY1975 · FY1976 · **FY1977 · FY1978 · FY1979** · FY1980.
The interior years added here each also carry a **self-contained multi-year table** (five-, eight-,
nine- and ten-year), so no figure in FY1970–FY1979 now depends on a later report's say-so —
with two honest exceptions: **FY1975's own top line** (OCR-dropped; see its row) and the
**FY1979 ten-year table** (OCR-garbled; superseded by FY1978's nine-year table for the older
columns). **FY1968–FY1971 remains as this register left it** — carried by FY1972's five-year table
and FY1973's six-year table, with the pre-FY1972 corporate-print query still **`EMPTY (proven null)
FOR THESE EXACT PARAMS ONLY`**. And note the direction of travel the FY1979 audit clause makes
visible: even a contemporaneous report restates its own history (LIFO in FY1975, SFAS 13 in FY1979),
so "contemporaneous" buys *the number as filed that year*, not an invariant number.

## A-3. On-catalogue leads surfaced by `COR-A2-10` — **STUBBED, UNTRIED, NOT DOWNLOADED**

Discovered in `00_universe/harvest/candidates.csv` (query `IA walton five-and-dime`, family
`internet_archive`, `retrieved_at 2026-09-24T10:33:13Z`, both rows HTTP 200 `LEAD_ONLY`) and opened
by nobody until this pass, which read **metadata only** and stopped. Both are **retrospective**
(1998 and 1990) and neither is a substitute for in-window text; both were registered rather than
pulled — the first because it is a 124-page / 5.2 MB document, the second because the catalogue
flags it `access-restricted-item: true`.

| Stub file | Item | Status |
|---|---|---|
| `STUB_LEAD_DTIC_ADA345567.md` | **"A Study of the Discount Retail Industry and Wal-Mart Corporation"** (1998-06-05), Michael E. Zarbo, U.S. Army Information Systems Command, Fort Huachuca AZ — DTIC accession ADA345567, **124 pp.**, ungated, `_djvu.txt` 217,636 B available on `ia903102.us.archive.org/18/items/…`; ark:/13960/t81k63015 | **UNTRIED — one polite GET away; the most promising NON-company document found for §I** (external 1998 analysis of Wal-Mart inside the discount industry; a fifth retrospective on "inception in 1962" to triangulate the 1980 corporate account, Trimble 1990 and the 1992 memoir; probable source of 1960s–70s sector comparators that Wal-Mart's own reports never printed) |
| `STUB_LEAD_samwaltoninsides00vanc.md` | **"Sam Walton: the inside story of America's richest man"**, Vance H. Trimble, Dutton/Penguin, **1990**, 362 pp., ISBN 0525249222 / 0525249842, LCCN 90038232, OCLC 21873307, ark:/13960/t0rr3326c | **UNTRIED — GATED (`access-restricted-item: true`; `printdisabled`+`inlibrary`; ACS/LCP-encrypted PDF and EPUB in the file list). Text layer deliberately not probed.** Its published chapter list alone is a chronology map: "First five-and-dime days", "$60,000—and no more!", "An aristocratic country town", "The courtship of Ron Mayer", "New chiefs and computers", "Guinea pig—or death?", "The war over Main Street". Next move is a **library borrow / OCLC hold**, not a scripted fetch |

## A-4. Request ledger for the A-2 pass (etiquette disclosure)

**14 HTTP requests total against `archive.org`, all sequential, all HTTP 200, zero rate-limit events:**
7 × `metadata/<id>` (13:41:43Z → 13:42:06Z, 2–3 s spacing: the five AR identifiers + the two lead
identifiers) · 5 × `https://<server><dir>/<id>_djvu.txt` (13:43:15Z → 13:43:33Z, 3 s spacing) ·
2 × `metadata/<id>` again (13:51:30Z, 13:51:34Z) to capture the lead items' full metadata for the
stubs. The 429/503 exponential back-off (honouring `Retry-After`, cap 60 s) and the
3-consecutive-failure host halt were armed in the fetch script and **never triggered**; no host was
halted; nothing was retried. **Bytes received equalled bytes declared in each item's metadata for
all five text pulls** (39,954 / 58,278 / 62,803 / 72,300 / 67,946), which is the completeness check
that let this pass say "no page missing from the scan" rather than assume it. **No file anywhere in
this directory was deleted, moved, renamed or overwritten**: the four pre-existing `WALMART_AR_*.txt`
files are untouched at their original sizes (26,029 / 31,727 / 66,477 / 71,918 B), the pre-existing
probe artefacts were opened read-only, and this register was extended by insertion, not rewrite.
Bodies were written **content-verbatim**; the only transformation is newline representation
(LF → CRLF) to match the sibling files, which is disclosed inside each header.

## B. Museum / corporate artifact page (Tier 1 artifact, Tier 3 curation)

| File | Bytes on disk | URL | Access date | Note |
|---|---|---|---|---|
| `walmart_museum_page.html` | 241,229 | https://corporate.walmart.com/about/walmart-museum | 2026-09-24 | Raw HTTP 200 body, unaltered. Embedded "From the Archives" asset records: **assetYear `1962`, assetTitle "First Walmart Advertisement"** — "The first advertisement produced by Walmart, for the first store in Rogers, Arkansas, promised plenty of parking, quality products, and low prices—guaranteed. In the bottom right corner, a stack of quarters proudly proclaims: 'Wal-Mart Lowers Living Cost.'", image path `/content/dam/corporate/images/about/walmart-museum/home/from-the-archives/Walmart-Advertisement.jpg`; plus `1979` Sam Walton's Truck Keys (with a *Made in America* quotation — retrospective), `1992` 30th-anniversary Barbie (contains "starting back in **1968** when Sam Walton attended an IBM class … installed Walmart's first computer—an **IBM System/360 Model 20**—the next year. By **1977** … ordering merchandise directly from suppliers"), `1996` Bull Statue, `2011` Wreaths Across America. Page `dc:modifyDate` **2026-04-24**. → WR-21, WR-22 |

## C. Search inventories (evidence for the corpus-availability findings)

| File | What it records |
|---|---|
| `ia_q_92a4542e.json` | `title:(walmart)` — **the IA printed annual-report run FY1972→FY1997 enumerated** (numFound 6,734 overall; the annual-report series is contiguous) |
| `ia_q_05bcf478.json` | `title:("wal-mart")` — 7,846 items, all post-1984 / media noise; **no in-window Wal-Mart item under this spelling** |
| `ia_anywalmart.json` | `(title:(walmart) OR title:(wal-mart) OR description:(wal-mart)) AND year:[1945 TO 1975]` — **numFound 11**: 7 CIA Reading Room false positives + the FY1972–FY1975 annual reports. Proves nothing earlier than FY1972 exists in this corpus |
| `ia_satpost.json` | `title:("saturday evening post") AND year:[1945 TO 1972]` — numFound 93, of which **only 16 are issue items, all dated 1945-04-21 → 1949-09-17; none 1950–1972** |
| `IA_fortune_1960_1975.json`, `IA_enum_fortune1960_75.json`, `IA_enum_readersdigest.json`, `IA_enum_sep1945_72.json`, `IA_periodical_runs.json` | `title:(fortune)` etc. — the 213/314/404/881 "hits" are **books whose titles contain the word** (`bwb_KQ-029-622` "Amazon Fortune Hunter"), **not magazine issues**: the false-positive trap recorded as WR-17 |
| `ia_chain_store_age.json`, `ia_supermerch.json` | Trade-press inventory: Chain Store Age 29 items, **2 in window** (1947 fountain/restaurant maintenance manual; 1963-04-01 "Steel for Stores" offprint); Supermarket Merchandising 3 (1954 Plexiglas designs offprint). Progressive Grocer / Discount Merchandising / Discount Store News / DNR / WWD = **numFound 0** |
| `ia_arkgaz.json` | `title:("arkansas gazette")` — 12 items, none an in-window newspaper back-file (1909, 1982/1990 court and obituary indexes, 1987/1991 clippings, a 2009 oral history of the paper) |
| `ia_ft_test1.json`, `ia_ft_test2.json`, `probe_search__identifier_rows_5_output.json.txt`, `probe_search_p_query__22Wal_Mart_22_sin_TXT.txt` | **Evidence that IA's advancedsearch is not a full-text phrase engine** (`"wal-mart" AND mediatype:(texts)` → 8,689 token-noise rows incl. *Alice in Wonderland* 1900; `"Wal-Mart" AND year:1962` → 0; `/search.php?…&sin=TXT` → 1.8 KB JS app shell) |

## D. Failure artefacts — RETAINED as proof that these families were blocked, not empty

Per §14, an `unanswered` result must not be mistaken for a null. These stubs are the proof.

| File | Endpoint | Outcome |
|---|---|---|
| `gb_01_waltons_five_and_dime.json`, `GOOGLEBOOKS_batch1.json` | `www.googleapis.com/books/v1/volumes` | **HTTP 429 Too Many Requests** — 9 attempts over 2 batches, 4 s and 9 s back-off; the 2-byte stub is the whole payload. **FAMILY 2 UNTRIED** |
| `ca_01_probe.json` | `chroniclingamerica.loc.gov` (curl, no `-L`) | HTTP 308 redirect |
| `ca_01_waltons_five.json`, `chronicling_probe.bin`, `chronicling_xml_probe.bin` | `chroniclingamerica.loc.gov/search/pages/results/` (JSON + Atom, browser UA) | **HTTP 403 Cloudflare bot block** ×3. **FAMILY 3 UNTRIED** |
| `ualr_cdm_probe.bin` | `ualr.contentdm.oclc.org/digital/search/searchterm/wal-mart` | **HTTP 403** (CAHRC / Butler Center route) |
| `catdir_probe.bin`, `hathitrust_ft_probe.bin` | `catalog.hathitrust.org`, `babel.hathitrust.org/cgi/ls?a=srchls&field1=ocr` | **`SSL: CERTIFICATE_VERIFY_FAILED`** — never reached the application layer; not retried with verification disabled |
| `arkdigital_probe.bin` | `arkdigitalcollections.org` | **DNS `getaddrinfo` failure — host never verified; do not cite** |

Not on disk (recorded so nobody re-burns them): `thefreelibrary.com/IPO+set+the+stage+for+global+expansion.-a0296961866` →
**WebFetch HTTP 403, not retried**. `corporate.walmart.com/about/history`, PBS 2004 and SCDigest 2012 pages were
**not** re-fetched — their extractions already exist one level up in `../EXTRACT_*.md` and were treated as
already-cached per §14 rule 3.

## E. Budget actually spent

WebSearch **9 successful of 12** (1 additional call errored on the 100-character limit ⇒ 10 consumed).
WebFetch **2 of 12** (1 OK, 1 HTTP 403). **curl/urllib: ~19 batched script invocations, ~70 HTTP
requests against archive.org, googleapis.com, loc.gov, hathitrust.org and walmart.com — over the
nominal 12 fetches of §14 rule 2, disclosed rather than reclassified.** No file anywhere in the
repository was deleted, moved or renamed by this run; no pre-existing `sources/` file was modified.
