# FORENSIC LONGITUDINAL DATASET — AMAZON.COM, STAGE 3 (1997-05-16 → under argument, work to 1999-12-31)
## Volume 3 of 3 — §P–§U (narrative only; its register rows are in `stage_3_pending_registers.md`)

*One document split at section boundaries for the 60,000-word cap (method §9.2/§9.3). Section letters, claim
IDs, metric IDs and conflict numbering run continuously across volumes and across stages: Stage 1 owns
§U.1–U.43, Stage 2 owns §U.44–U.113, **Stage 3 owns §U.114–U.168**. Volume map: `stage_3_index.md`.*

*The endpoint is **contested and unresolved** — §STAGE BOUNDARY JUSTIFICATION carries all four candidates
(1997-12-31, 1999-06-30, 1999-09-30, 1999-12-31) with their evidence; content is written to the widest
defensible window and every endpoint-sensitive claim is flagged. The S-1 lineage (original, amendments,
424B1) is ONE source (§3); `(PB)` marks material after the window.*



# FORENSIC LONGITUDINAL DATASET — AMAZON.COM, STAGE 3 — PART 4 (SECTIONS P–U + CSV APPEND BLOCKS)

**Section owner:** quantitative & conflicts assembler (Level-3). **Path owned:** `_parts/s3_p4.md`. Nothing else on
this run is writable by this part (§14 rule 4): the registers are applied by the orchestrator from the append
blocks at the tail of this file, and this part writes no register itself.

**Window reconstructed:** 1997-05-16 → **1999-12-31** as the working endpoint, with the endpoint itself contested and
registered at **U.153** (1997-12-31 vs 1999-06-30 vs 1999-09-30 vs 1999-12-31). Documents used: the FY1997 10-K405,
the FY1998 10-K, the FY1999 10-K, the **FY1999 10-K/A**, the 1998 and 1999 Forms 10-Q, the FY1997/FY1998 annual
reports to shareholders, the 424B2/424B3 prospectuses, the S-4/S-3/S-8/POS AM series, the 1998–1999 proxies and the
8-K set, all under `sources/`.

**Numbering continues Stages 1 and 2 and is never re-based.** §P ids run from **P184** (`_parts/s2_p4.md` §P closes
at **P183**; verified on disk, not assumed — the table's last three rows are the documented-null rows P181, P182,
P183). §P.2 arithmetic items continue Stage 2's `s`-series with **`t`-items** (`t1`…), because Stage 1 used `d`-items
and Stage 2 `s`-items and the letters are the spine's only distinction between the three stages' workings.
**§U runs from U.114**: Stage 1 owns U.1–U.43, Stage 2 owns U.44–U.113 (`_parts/U_CONCORDANCE.md`; `conflicts.csv`
carried exactly 113 rows before the Stage-3 merge). The 39 Stage-3 rows already applied to `conflicts.csv` are keyed
**provisionally `P-U.114 … P-U.152`** per `03_quality_control/stage3_register_merge_held_rows.md`; this part emits
**one §U block per provisional key, in that exact order**, so the orchestrator's re-key `P-U.114 → U.114` is
mechanical. Conflicts this part registers itself, which are in no provisional key, continue at **U.153** and are
emitted as new `conflicts.csv` rows so the 1:1 block-to-row invariant that AUDIT 8 verified keeps holding. The
re-key map is at the end of §U.

**Geometry source:** `stage_2_part_3.md` §Q–§U and `_parts/s2_p4.md` §P/§P.2/§P.2a/§Q/§R/§S/§T. Stage 2's §P
nine-column form is reproduced **with `Class`** because a part is a volume of one document, and Stage 2's `^\*\*U\.<n> — `
block convention (bold run-in paragraphs, **not** `### U.n`) is reproduced exactly.

**Method anchors binding this part:** §3 (claim classes, confidence, independence rule, **filing-lineage rule** — an
S-4 and its amendments and the POS AM that continues it are one source); §6 (time audit; every numeral carries its
basis; `RETROSPECTIVE SOURCE` tagging); §7 (line formats); §8 (no value without a source cell and a confidence cell;
UNKNOWN is a complete value); §9.3 (numbering continues across parts); §13 (CSV header order reproduced exactly);
**§14 rules 1, 4, 7, 8, 10, 11**. Rule 8 was executed literally: every inherited figure below was grepped across
`sources/` before being written, and the ones that returned zero hits appear only inside retraction language at
§P.2a with the superseded value printed in the same cell.

**Hindsight firewall (method §2).** Nothing here argues from the 2000s outcome back to the rationality of a 1997–99
decision. The 10-K for FY1999 and its amendment are 2000 documents describing 1999 states and are tagged as such at
every row that uses them; the 1997 filing's own language about 1996 is tagged `(L)`. The **record-selection null**
required by §2 is stated in §A of part 1 of this stage and carried again at §S row 1, because §S is where a reader
looks for it.

---

## P. QUANTITATIVE METRICS TABLE (STAGE 3)

**Metric-basis discipline (method §6, §8, §13), carried forward from Stage 1 §P and Stage 2 §P.** "Net sales" is
the audited revenue line on a shipment basis inclusive of outbound shipping and handling; the FY1999 10-K adds that
from 1999 it **also includes** zShops/Auctions transaction revenue (commissions, placement fees, listing fees), so an
FY1999 "net sales" figure is not the same object as an FY1997 one — that is a metric-composition change, not growth
(→ U.139, U.160). Cumulative-since-inception sales and cumulative accounts are labelled **cumulative** and are never
used as a denominator. Titles "advertised" ≠ "sourceable" ≠ "stocked" ≠ "held"; the FY1998 and FY1999 title counts
count **books, music CDs, videos, DVDs, computer games and other titles**, so they are not comparable with the
FY1997 "2.5 million titles" (→ U.141). "Customer accounts" from 1999 is expressly **"inclusive of accounts with
Amazon.com Auctions"** — a composition change mid-series (→ U.139). **Every restatement pair is printed on both
legs; no restated value is ever printed as if it had been filed** (the §P "as filed / as restated" tags govern).

**Source keys used in the Source column (COR-01 extended to Stage 3).** `10-K405/97` FY1997 Form 10-K405 acc.
0000891020-98-000448, filed 1998-03-30 · `10-K/98` FY1998 Form 10-K acc. 0000891020-99-000375, 1999-03-05 · `10-K/99`
FY1999 Form 10-K acc. 0000891020-00-000622, 2000-03-23 · `10-K/A/99` FY1999 Form **10-K/A** acc.
0000891020-00-001638, 2000-09-08 · `ARS/97` and `ARS/98` annual reports to shareholders, filed 1998-04-17 and
1999-04-07 · `Q<n>-<yy>` the Form 10-Q of that quarter with its accession tail in §T · `8-K(<date>)` the Form 8-K
whose **event** date is named · `424B2/98` acc. 0000891020-98-001279, 1998-08-13 · `424B3/98` acc. …-001477,
1998-10-22 · `POS AM(<file>)` the post-effective amendments · `DEF14A/98`,`DEF14A/99` proxies.
**Independence (method §3 filing-lineage rule):** the four annual reports are **four states of the issuer's own
annual reporting**, and the FY1999 10-K and its amendment are **one instrument in two states**; a figure printed
in the FY1997 10-K and again in the FY1998 10-K's comparative column has been **filed once by one author twice**,
which is a restatement event, not a corroboration. Genuinely independent rows in this stage are few: the counterparty
filings, Media Metrix ratings relayed inside company paper (relayed, so not independent in the §3 sense), and
`8-K`-attached releases only where the release predates the filing that quotes it.

| ID | Date | Metric | Value | Unit | Source | Source date | Class | Confidence |
|---|---|---|---|---|---|---|---|---|
| **Stage-3 opening state and the FY1997 audited year, as filed and as recast** | | | | | | | | |
| P184 | FY1997 | Net sales, **AS FILED** | 147,758 | USD thousands | `10-K405/97` l.1177 and l.1861 (two prints, one document) | 1998-03-30 | FACT (audited) | High |
| P185 | FY1997 | Net sales, **AS RESTATED** | 147,787 (+29) | USD thousands | `10-K/98` l.1222; repeated `10-K/99` l.1732 and `10-K/A/99` l.173 | 1999-03-05 / 2000-03-23 | FACT (audited, restated) | High → U.125, U.136 |
| P186 | FY1997 | Cost of sales / gross profit, as filed | **118,945 / 28,813** | USD thousands | `10-K405/97` l.1178, l.1180, l.1862–1864 | 1998-03-30 | FACT (audited) | High |
| P187 | FY1997 | Cost of sales / gross profit, as restated | **118,969 / 28,818** (+24 / +5) | USD thousands | `10-K/98` l.1223, l.1225; `10-K/99` l.1733, l.1735 | 1999-03-05 / 2000-03-23 | FACT (audited, restated) | High → U.159 |
| P188 | FY1997 | Gross margin | **19.5** as filed (`28,813 ÷ 147,758 = 19.4995`); restated prints **19.5** too (`28,818 ÷ 147,787 = 19.4935`) | % of net sales | `10-K405/97` l.1403 prints "19.5%" itself; DERIVED §P.2 **t1** | 1998-03-30 | FACT (company rendering) + DERIVED | High |
| P189 | FY1997 | Operating expenses, **AS FILED** — three-line caption | marketing and sales **38,964** · product development **12,485** · G&A **6,573** · total **58,022** (`38,964+12,485+6,573 = 58,022` ✓) | USD thousands | `10-K405/97` l.1182–1186, l.1866–1870 | 1998-03-30 | FACT (audited) | High |
| P190 | FY1997 | Operating expenses, **AS RECAST (1999-03-05)** — same total, different captions | marketing **40,486** · product development **13,916** · G&A **7,011** · total **61,413** | USD thousands | `10-K/98` l.1227–1234 | 1999-03-05 | FACT (audited, restated) | High → U.150, U.159 |
| P191 | FY1997 | Operating expenses, **AS RECAST (2000-03-23)** — five-line caption | marketing **40,077** · technology and content **13,384** · G&A **6,741** · stock-based compensation **1,211** · total **61,413** (`40,077+13,384+6,741+1,211 = 61,413` ✓, §P.2 **t2**) | USD thousands | `10-K/99` l.1737–1746; `10-K/A/99` l.179–188 | 2000-03-23 | FACT (audited, restated) | High → **U.158: there is no single filed FY1997 technology-spend figure** |
| P192 | FY1997 | Loss from operations / net loss, as filed | **(29,209) / (27,590)** | USD thousands | `10-K405/97` l.1188, l.1192, l.1871, l.1875 | 1998-03-30 | FACT (audited) | High |
| P193 | FY1997 | Loss from operations / net loss, as restated | **(32,595) / (31,020)** (Δ −3,386 / **−3,430**) | USD thousands | `10-K/98` l.1236, l.1242; `10-K/99` l.1748, l.1761 | 1999-03-05 / 2000-03-23 | FACT (audited, restated) | High → U.125 — **the loss leg is NOT itemised anywhere; the PlanetAll pooling note explains the +29 of sales, not the −3,430 of loss** |
| P194 | FY1997 | Loss per share and shares used — **three vintages, one loss** | **(1.27)** pro forma on **21,651** (`10-K405/97`) → **(0.24)** on **130,341** (`10-K/98`) → **(0.12)** on **260,682** (`10-K/99`) | USD/share, thousand shares | the three Item 6 tables | 1998-03-30 / 1999-03-05 / 2000-03-23 | FACT (audited, per document) | High → **U.133 — the denominator construction changed twice; the year-over-year EPS change is not interpretable** |
| P195 | FY1997 | Growth in net sales over FY1996 | **838%** as filed / **839%** as restated — the one point is the **$29k** of PlanetAll sales added by the pooling | % | `10-K405/97` l.1380 ("838%") and `ARS/97` l.204; `10-K/98` l.1309 ("839%"); DERIVED §P.2 **t3** | 1998-03-30 / 1999-03-05 | FACT (company arithmetic) + DERIVED | High → U.126 |
| P196 | FY1997 | Depreciation and amortisation, **as filed** | **3,388** (FY1996 286; FY1995 19) | USD thousands | `10-K405/97` l.2037 (cash-flow add-back) | 1998-03-30 | FACT (audited) | High |
| P197 | FY1997 | Depreciation and amortisation, **as recast** | **3,442** (+54); FY1996 recast to **296** (+10) | USD thousands | `10-K/98` l.2232; `10-K/99` l.2820 and `10-K/A/99` l.1291 both print 3,442 | 1999-03-05 / 2000-03-23 | FACT (audited, restated) | High → **U.145; §P.2 t4 shows no reconciling note exists** |
| P198 | 1997-12-31 | Fixed assets: gross / accumulated D&A / net | **12,899 / 3,634 / 9,265** | USD thousands | `10-K405/97` l.2300–2308 (components: computers 7,118, purchased software 4,505, leasehold improvements 914, leased assets 363 — `7,118+4,505+914+363 = 12,900`, one dollar of rounding, §P.2 **t5**) | 1998-03-30 | FACT (audited) | High |
| P199 | 1997-12-31 | The same FY1997 fixed-asset column, one year later | **13,490 / 3,764 / 9,726** (Δ gross **+591**, Δ net **+461**) | USD thousands | `10-K/98` l.2750–2753 (own comparative) — *the 8-K of 1998-08-27 l.1485 already prints 13,490 for 1997 mid-year* | 1999-03-05 | FACT (audited, restated) | High → **U.147 — two audited printings of one balance date, +591 gross, no note** |
| P200 | 1997-12-31 | Employees | **614 full-time** (own-year, qualified); and the same document's growth sentence gives **614 employees as of December 31, 1997** unqualified, against **158 as of December 31, 1996** | persons | `10-K405/97` l.516 ("614 **full-time** employees") and l.729 (risk factor: "158 … to 614 employees") | 1998-03-30 | FACT (basis disclosed on one line, dropped on the other) | High (both prints) → **U.118 — the FY1996 pair 151/158 is the precedent; §R prints all bases side by side** |
| P201 | 1997-12-31 | Inventory / accounts payable | **9,001 / 32,697** — *carried from Stage 2's `(PB)` row and re-verified at `10-K405/97` l.1809 area; inventory turns `118,945 ÷ ((8,971+9,001)÷2)` only on the FY1998 opening pair — see §P.2 "Not computed"* | USD thousands | `10-K405/97`; opening pair 1996-12-31 **571** from Stage 2 §P105 | 1998-03-30 | FACT (audited) | High (year-end balances) |
| P202 | 1997-12-31 | Working capital / total assets / long-term debt / stockholders' equity | **93,158 / 149,844 / 76,702 / 28,591** (all restated-basis, printed identically in `10-K/98` l.1262–1265 and `10-K/99` l.1781–1784) | USD thousands | the two Item 6 tables | 1999-03-05 / 2000-03-23 | FACT (audited, restated) | High — *the FY1997 10-K405's own 1997 balance sheet is the as-filed state; the Item 6 comparative is the recast. The $75,000,000 term loan drawn 1997-12-23 (Stage 2 §Q `(PB)`) is the 76,702* |
| P203 | 1997-11 / 1997-12-31 | The first distribution centre outside Washington | **200,000 sq ft at New Castle, Delaware, opened November 1997**; Seattle expanded to **85,000 sq ft** | sq ft, date, place | `10-K405/97` l.1646–1648 ("In November 1997 the Company **opened** a 200,000-square-foot distribution center in Delaware") | 1998-03-30 | FACT | High — **this single line falsifies the "first filing that uses 'opened'" dating argument for the Stage-3 boundary → U.153** |
| P204 | 1997-12-31 | Sales-tax exposure event, carried from Stage 2 §P172 | the FY1997 filing **deletes** the SALES TAX COLLECTION risk factor in the same year the Delaware centre opens; string-count "sales tax" = **0** in `10-K405/97` | presence/absence | Stage 2 §P172 re-verified on this pass against the same file | 1998-03-30 | FACT (differential + documented null) | High (the differential) / **none (the motive)** → U.71 (Stage 2) |
| P205 | FY1997 | Advertising expense incurred | **21.2** (FY1996 **3.4**; FY1995 **0.03**) — the first year the company filed an advertising number at all | USD millions | `10-K405/97` l.2187–2189 ("incurred advertising expense of $21.2 million, $3.4 million and $30,000") | 1998-03-30 | FACT (audited note) | High — **`3.4 ÷ 15.746 = 21.6%` of net sales in FY1996 against `21.2 ÷ 147.758 = 14.3%` in FY1997 (§P.2 t6)** |
| P206 | FY1997 | Cumulative customer accounts, and cumulative sales since inception | **1,510,000** accounts (from 180,000 at 1996-12-31, **+738%**); "through December 31, 1997 the Company had sales of **more than $164 million**" | accounts, %, USD millions | `ARS/97` l.207, l.210; `10-K405/97` l.241–242 | 1998-04-17 / 1998-03-30 | FACT (company count / as disclosed) | High (as stated) / **Low (that "account" is defined anywhere)** → **U.124 — cumulative ≠ annual; $164m is not a 1997 revenue** |
| P207 | Q4-1996 → Q4-1997 | Repeat customers as a share of orders — **the only matched pair the company itself prints** | **over 46% → over 58%** | % of orders | `ARS/97` l.210–211; reproduced `ARS/98` l.440 | 1998-04-17 / 1999-04-07 | FACT (company claim, matched basis) | High (as claimed) → **U.140 — six repeat values on four bases across the window; this pair is the only like-for-like** |
| P208 | FY1997 | Third-party audience rank relayed by the company | Media Metrix: amazon.com "went from a rank of **90th to within the top 20**" | rank | `ARS/97` l.213–214 | 1998-04-17 | ESTIMATE (third party, **relayed**) | Medium that relayed / **Low as measurement — the panel methodology appears in no Amazon filing** → §S |
| **FY1998: the year the model changed object — and the first full audited year of geographic and category expansion** | | | | | | | | |
| P209 | FY1998 | Net sales, **AS FILED** | **609,996** | USD thousands | `10-K/98` l.1222, l.1309 ("313%"), l.2016 | 1999-03-05 | FACT (audited) | High |
| P210 | FY1998 | Net sales, **AS RESTATED** | **609,819** (Δ **−177**) | USD thousands | `10-K/99` l.1732; `10-K/A/99` l.173, l.285, l.1078 | 2000-03-23 | FACT (audited, restated) | High → **U.149 — no reconciling note; the −177 lands entirely on gross profit (§P.2 t7)** |
| P211 | FY1998 | Gross profit / gross margin | **133,841 as filed → 133,664 as restated**; margin **21.94% → 21.92%**, unchanged at one decimal (`133,841 ÷ 609,996`; `133,664 ÷ 609,819`, §P.2 **t7**) | USD thousands, % | `10-K/98` l.1225; `10-K/99` l.1735 | 1999-03-05 / 2000-03-23 | FACT + DERIVED | High |
| P212 | FY1998 | Operating expenses and loss | total opex **245,801** as filed (incl. **50,172** of merger/acquisition costs and goodwill amortisation, a caption that does not exist in FY1997) → **242,719** restated; loss from operations **(111,960) → (109,055)**; net loss **(124,546)** both printings | USD thousands | `10-K/98` l.1230–1242; `10-K/99` l.1741–1761 | 1999-03-05 / 2000-03-23 | FACT (audited) | High — **the goodwill-amortisation caption is the accounting trace of the acquisition turn; §P.2 t8 shows FY1999 amortisation of 214,694 is 13.1× net sales growth-adjusted… see the caveat there** |
| P213 | FY1998 | Depreciation and amortisation | **9,692 as filed → 9,421 as recast** (Δ −271) | USD thousands | `10-K/98` l.2232; `10-K/99` l.2820; `10-K/A/99` l.1291 | 1999-03-05 / 2000-03-23 | FACT (audited, two printings) | High → **U.145** |
| P214 | FY1998 | Advertising expense incurred | **60.2** (FY1997 21.2; FY1996 3.4) | USD millions | `10-K/98` l.2459–2461; reprinted `10-K/99` l.3107–3109 | 1999-03-05 | FACT (audited note) | High — **spend 2.84× the prior year while sales grew 4.13×, so the ratio FELL: `60.2 ÷ 609.996 = 9.9%` against `14.3%` (§P.2 t6)** |
| P215 | FY1998 | Fulfilment costs — **the series exists only from the FY1999 filing backwards** | **50.3** (FY1997 **12.1**) | USD millions | `10-K/99` l.1970–1972 and l.3097–3102 ("Fulfillment costs amounted to $188.4 million, $50.3 million and $12.1 million in 1999, 1998 and 1997") | 2000-03-23 | FACT (audited note, retrospectively disclosed) | High — **no FY1998 document prints a fulfilment number at all; `10-K/98` l.1389–1392 discloses only that fulfilment sits inside marketing and sales (§S gap)** |
| P216 | FY1998 | Marketing and sales expense | **133,023 as filed → 132,654 as restated**; as % of net sales **21.8% → 21.8%** (§P.2 **t9**) | USD thousands, % | `10-K/98` l.1227; `10-K/99` l.1737 | 1999-03-05 / 2000-03-23 | FACT + DERIVED | High |
| P217 | FY1998 | Technology spend | product development **46,807** as filed → **technology and content 46,424** as recast | USD thousands | `10-K/98` l.1228; `10-K/99` l.1738 | 1999-03-05 / 2000-03-23 | FACT (two captions, two bases) | High → **U.150, U.158: "product development" and "technology and content" are not the same object — the latter absorbs acquired content** |
| P218 | 1998-12-31 | Fixed assets gross / net; total assets; long-term debt; equity; working capital; cash; marketable securities | **43,585 / 29,791** fixed assets (§P.2 **t10** checks the FY1997 comparative: 13,490 gross); **648,460** total assets; **348,140** long-term debt; **138,745** equity; **262,679** working capital; **25,561** cash (as filed) → **71,583** cash and cash equivalents (10-K/A basis); **347,884** marketable securities → **301,862** | USD thousands | `10-K/98` l.2750, l.1260–1265; `10-K/99` l.1779–1785; `10-K/A/99` l.221–226 | 1999-03-05 / 2000-03-23 / 2000-09-08 | FACT (audited, basis-dependent) | High — **the cash line is a BASIS question, not a restatement of fact: `10-K/A/99` l.100 states "THE AGGREGATE TOTAL OF CASH EQUIVALENTS AND MARKETABLE SECURITIES HAS NOT CHANGED" → U.154** |
| P219 | 1998-12-31 | Long-term debt, three ways | **348,140** (Item 6, excludes current portion) · **348,824** including the **684** current portion · **"$349 million" of outstanding senior indebtedness** (`S-3` File 333-74435, eleven days later) | USD thousands, USD millions | `10-K/98` l.1264 and the debt note; `S-3_FileNo-333-74435` filed 1999-03-16 | 1999-03-05 / 1999-03-16 | FACT (three captions) | Medium → **U.131 — the summary line's composition is not footnoted; never print one as "total debt"** |
| P220 | 1998-12-31 | Employees | **approximately 2,100** (10-K, unqualified) · **"over 2,100"** (ARS, same year-end) · **ARS/98 wording: "our employee base grew from approximately 600 to over 2,100"** | persons | `10-K/98` l.528–529; `ARS/98` l.157 | 1999-03-05 / 1999-04-07 | FACT (company count, basis undisclosed) | Medium-High → **§R prints 614 / ~2,100 / ~7,600 as three bases; "approximately 600" for 1997-12-31 is a FOURTH rendering against a filed 614 → U.161** |
| P221 | 1998-06 → 1998-12 | Category and geography launches, as filed by the company itself in 2000 | **music June 1998 · DVD/video November 1998 · UK and German books October 1998** | date, category | `10-K/99` l.274–275 launch table; corroborated in-document at `10-K/98` l.1321–1322, l.1370 | 2000-03-23 (1998 events) | FACT (as disclosed) | High — **the video store's exact day, 1998-11-17, comes from a January 1999 8-K, not from the launch table (§Q)** |
| P222 | **1998-11-17** | Video store launch — **the only exact launch DAY in the whole Stage-3 corpus** | "Amazon.com launched its video store **on November 17** with more than **60,000** VHS and [DVD titles]" | date, titles | `8-K(1999-01-26)` l.306 (attached release) | 1999-01-27 (event 1999-01-26) | FACT (company release, day-dated) | High as disclosure → **U.162: the launch tables give only "November 1998"; the day survives in a release the tables do not cite** |
| P223 | 1998-04-17 / 1998-04-24 | First foreign acquisitions (the "buy vs build" act) | **Bookpages Ltd** (UK) and **Telebook.com GmbH** (Germany) announced, **~$11.4m and ~$43.4m** in stock and cash respectively per the releases; two European distribution centres leased | USD, dates | `8-K(1998-04-17)`, `8-K(1998-04-24)`, `8-K(1998-04-27)`; S-4 File 333-56723 lineage | 1998-04-17 / 1998-04-24 / 1998-04-28 | FACT (filing + attached releases) | High that announced; **the aggregate "~$55m" is a §P.2 t11 DERIVED sum of two different consideration mixes and is labelled so** |
| P224 | 1998-06-03 / 1998-06-12 | The two S-4 shelves, and the four-day SIC change | File No. **333-55943** (Junglee) filed 1998-06-03 covering **up to 5,000,000 shares**, SIC **2731**; File No. **333-56723** (Bookpages/Telebook) filed 1998-06-12, SIC **5961** | shares, dates, SIC | `S-4_FileNo-333-55943` l.970; `S-4_FileNo-333-56723` cover | 1998-06-03 / 1998-06-12 | FACT | High → **U.116, U.137 — the classification change is dated to a four-business-day interval and never reversed** |
| P225 | 1998-08-13 | The half-year state, as filed in a prospectus | "Through **June 30, 1998**, the Company had sales of more than **$367 million** to approximately **3.1 million** customer accounts in over 150 countries. Repeat customers accounted for **over 62% of orders** in the six months ended June 30, 1998. International sales represented **21% of net sales**" | USD millions, accounts, %, countries | `424B2/98` l.396–400 (cumulative sales; six-month repeat; six-month international mix) | 1998-08-13 | FACT (as disclosed, company-measured) | High (as stated) → **U.127 (3.1m vs 3.3m at one date), U.140 (a seventh repeat basis)** |
| P226 | 1998-06-30 | The same account count, printed a year later | **3.3 million** customer accounts at June 30, 1998 | accounts | `8-K(1999-07-21)` l.202; `10-Q Q2-1999` | 1999-07-22 / 1999-08-16 | FACT (company count) | High (both prints) → **U.127 — the register's dossier recorded the 3.1/3.3 pair as "unknown why"; the two printings are here dated 11 months apart, and no definition changed in either text** |
| P227 | 1998-09 / 1998-12-31 | Associates Program enrolment | **"more than 140,000"** (stated 1998-10-28, as of September) · **"approximately 200,000"** (`10-K/98`, as of the year-end wording) | member sites | `8-K(1998-10-28)` l.296; `10-K/98` l.383–386 | 1998-10-28 / 1999-03-05 | FACT (company count) | High (as disclosed) / **UNKNOWN (rate, expense, attributable revenue — still: no rate appears anywhere in the FY1998 or FY1999 corpus, §P.2 "Not computed")** → U.140 (Stage 2), §S |
| P228 | 1998-10-22 | The music store's first disclosed performance | Q3-1998 music sales **$14.4 million**; the FY1998 10-K claims Amazon became **"the number one online music seller"** and prints no competitor figure | USD millions, claim | `8-K(1998-10-28)` l.199 area and `10-Q Q3-1998`; `10-K/98` Item 1 | 1998-10-28 / 1999-03-05 | FACT (unaudited company figure) + COMPANY CLAIM (ranking) | High (the number as stated) / **Low (the ranking — no basis disclosed)** → **U.143** |
| P229 | 1998-11 | Ingram concentration, and its ownership | Ingram **58% of 1997 inventory purchases** as filed; **"approximately 60%"** of 1997 purchases as recast in `10-K/98`; **approximately 40%** of 1998; **Barnes & Noble announced its agreement to purchase Ingram in late 1998** — disclosed as a risk factor by Amazon | %, dates | `10-K405/97` l.1669–1670 (58%/59%); `10-K/98` l.422–423, l.797–799, l.2374–2377 | 1998-03-30 / 1999-03-05 | FACT (audited concentration + FACT (third-party corporate act)) | High → **U.135 — the 58/~60 pair; and `0.58 × purchases` remains UNKNOWN because no purchase total is filed in either year** |
| P230 | 1998-03-05 | Vendor-contract language, the differential that matters | FY1997: "no long-term contracts or arrangements with **any** of its vendors"; FY1998: with "**most** of our vendors" | wording | `10-K405/97` l.1671–1673; `10-K/98` MD&A | 1998-03-30 / 1999-03-05 | FACT (documented differential) | High → **U.144 — something was contracted between March 1998 and March 1999; which vendor, what terms, when: no agreement is filed** |
| P231 | 1998 | International sales share of net sales | **20%** (1998) · **25%** (1997) · **33%** (1996) — a **falling** share while absolute international sales rose 4.2× | % | `10-K/98` l.1325–1326 | 1999-03-05 | FACT (audited comparative) | High — **§P.2 t12 converts to dollars only against each year's own filed net sales and warns the share is mix, not performance** |
| P232 | 1998 | Titles offered | **"more than 4.7 million book, music CD, video, DVD, computer game and other titles"** — a **wider object** than FY1997's "2.5 million titles", which meant "primarily books plus a smaller number of CDs, videotapes and audiotapes" | titles | `10-K/98` l.214, l.283 | 1999-03-05 | FACT (as disclosed, definition attached) | High → **U.141 — 2.5m→4.7m is not like-for-like growth; part of the increase is the definition** |
| P233 | 1998-06 → 1998-08 | Discount architecture, as filed | featured book AND music titles at **40%** off list; "special value" editions **up to 89%** (10-Q Q2-1998 l.881–882; also `10-K405/97` l.1416) → the FY1998 10-K prints **"up to 85%"** | % off list | `10-Q Q2-1998` l.881; `10-K405/97` l.1416; `10-K/98` l.1361 | 1998-08-14 / 1998-03-30 / 1999-03-05 | FACT (two prints) | High (that both appear) → **U.138 — cannot separate change of practice from change of description** |
| P234 | 1998-11-19 → 1999 | The split record: three splits, **cumulative 12× from the mid-1997 basis** | **2-for-1 effected 1998-06-01** (record 1998-05-20) · **3-for-1 effected 1999-01-04** (record 1998-12-18) · **2-for-1 effected 1999-09-01** (approved 1999-07-21, record 1999-08-12); `2 × 3 × 2 = 12` | ratio, dates | `10-K/99` l.3817–3825; `10-K/A/99` l.2307–2317; `10-Q Q1-1998` l.468; `10-Q Q2-1999` l.636, l.652–655; `8-K(1998-11-19)` | 1998–2000 | FACT | High → **U.128 — no 8-K announces the September 1999 split; the 10-Q recital is the only filed record of it** |
| **FY1999: the year the company became a different object — and the year the accounting changed twice** | | | | | | | | |
| P235 | FY1999 | Net sales | **1,639,839** | USD thousands | `10-K/99` l.1732; `10-K/A/99` l.173 (unchanged by the amendment) | 2000-03-23 / 2000-09-08 | FACT (audited) | High |
| P236 | FY1999 | Net sales growth, and the multiple | **169%** as filed by the company (`10-K/A/99` l.285 prints "169%"); `1,639,839 ÷ 609,819 = 2.69×` and `(1,639,839 − 609,819) ÷ 609,819 = 168.9%` (§P.2 **t13**) | %, × | DERIVED on the two restated lines | 2000-03-23 | DERIVED | High |
| P237 | FY1999 | Cost of sales / gross profit / gross margin | **1,349,194 / 290,645 / 17.7** (`290,645 ÷ 1,639,839 = 17.724%`, §P.2 **t14**) — the third consecutive year of margin compression from 22.0 (1996) → 19.5 (1997) → 21.9 (1998) → 17.7 (1999) | USD thousands, % | `10-K/99` l.1733–1735 | 2000-03-23 | FACT + DERIVED | High |
| P238 | FY1999 | Operating expense captions, **all five, newly present** | marketing and sales **413,150** · technology and content **159,722** · G&A **70,144** · stock-based compensation **30,618** · amortisation of goodwill and other intangibles **214,694** · merger/acquisition and investment-related costs **8,072** · total **896,400** (`sum = 896,400` ✓ §P.2 **t15**) | USD thousands | `10-K/99` l.1737–1746 | 2000-03-23 | FACT (audited) | High — **amortisation alone is 73.7% of net sales… see §P.2 t15's warning: it is a non-cash charge against acquired goodwill and is NOT an operating cost of the 1999 store** |
| P239 | FY1999 | Loss from operations / net loss / LPS / shares | **(605,755) / (719,968) / (2.20) / 326,753**; equity in losses of equity-method investees **(76,769)** — a line that does not exist before 1999 | USD thousands, USD/share | `10-K/99` l.1748–1766; `10-K/A/99` l.202–207 (identical) | 2000-03-23 / 2000-09-08 | FACT (audited) | High |
| P240 | FY1999 | Advertising expense incurred | **140.9** (1998 60.2; 1997 21.2) → as a share of net sales **8.6%**, the third annual fall (§P.2 **t6**) | USD millions, % | `10-K/99` l.3107–3109 | 2000-03-23 | FACT (audited note) + DERIVED | High |
| P241 | FY1999 | Fulfilment costs | **188.4** = **11.5%** of net sales, against 8.25% (1998) and 8.19% (1997) — **the ratio the company had guided down rose**, and the FY1999 filing says so in the same paragraph (§P.2 **t16**) | USD millions, % | `10-K/99` l.1970–1972, l.1980–1983 | 2000-03-23 | FACT + DERIVED | High — **the company's own expectation ("we also expect that fulfillment costs will decline as a percentage of sales") is a `(PB)`-free in-year prediction that the same document falsifies** |
| P242 | Q4-1999 | Depreciation and amortisation, **single quarter, DERIVED** | **13,871** — `36,806 − 22,935 = 13,871` | USD thousands | `10-K/99` l.2820 (FY1999) less `10-Q Q3-1999` l.314 (nine-month) | 2000-03-23 / 1999-11-15 | ESTIMATE/DERIVED | High — **Q4-1999 alone exceeds all of FY1998: `13,871 ÷ 9,421 = 1.47×` (§P.2 t17). This row was HELD FOR WIDTH at merge and is re-emitted here correctly (§S.9 row 10)** |
| P243 | FY1999 | Depreciation and amortisation of fixed assets | **36,806** (1998 recast 9,421; 1997 recast 3,442) | USD thousands | `10-K/99` l.2820; `10-K/A/99` l.1291 (identical) | 2000-03-23 | FACT (audited) | High → U.145 |
| P244 | 1999-12-31 | Balance sheet, two cash bases | **as filed:** cash 116,962 · marketable securities 589,226 · working capital 273,243 · total assets **2,471,551** · long-term debt **1,466,338** · equity **266,278**. **as amended (10-K/A):** cash and cash equivalents **133,309** · marketable securities **572,879** — the other four lines **unchanged** | USD thousands | `10-K/99` l.1779–1785; `10-K/A/99` l.221–226 | 2000-03-23 / 2000-09-08 | FACT (audited, one instrument two states) | High → **U.154 — the amendment moved 16,347 of FY1999 cash out of marketable securities and changed nothing else on the balance sheet, while transforming the CASH-FLOW statement's change-in-cash line for every year** |
| P245 | FY1999, FY1998, FY1997 | **Net change in cash, as filed vs as amended — the same year, two signs** | FY1999 **+91,401 → +61,726** · FY1998 **+23,685 → (38,536)** · FY1997 **+1,012 → +103,830** | USD thousands | `10-K/99` l.2867; `10-K/A/99` l.1338 | 2000-03-23 / 2000-09-08 | FACT (two audited printings) | High → **U.154 — FY1998's change in cash FLIPPED FROM POSITIVE TO NEGATIVE (swing 62,221) in the amendment. This is a policy reclassification, not a correction of error; see the 10-K/A explanatory note at l.94–100 and the preference statement at l.1448–1456** |
| P246 | 1999-12-31 | Employees | **"approximately 7,600 full-time and part-time employees"** — plus, separately, "independent contractors" (numbered nowhere). *Value corrected on this pass: the received instruction called this "7,600 full-time", which the filed sentence does not say; the basis is wider than full-time* | persons | `10-K/99` l.684–685 | 2000-03-23 | FACT (basis stated) | High (as stated) / **Medium (that any of the three years' figures are comparable — they are not; §R)** → **U.161** |
| P247 | 1999-12-31 | Customer accounts | **over 17 million**, in over 150 countries — **on the post-1999 basis, inclusive of marketplace-service accounts**; mid-year prints 10.7m at 1999-06-30 and 13.1m at 1999-09-30, both expressly "including accounts with Amazon.com Auctions" | accounts, countries | `10-K/99` l.198; `10-Q Q2-1999` l.862; `10-Q Q3-1999` l.871 | 2000-03-23 / 1999-08-16 / 1999-11-15 | FACT (company count, composition disclosed) | High (as stated) → **U.139 — subtracting 6.2m (1998, old basis) from 17m (1999, new basis) is invalid** |
| P248 | 1999 | Marketplace services launched, in the company's own dated table | **Amazon.com Auctions March 1999 · zShops October 1999 · sothebys.amazon.com November 1999 · UK and German Auctions November 1999 · UK and German zShops November 1999** | date, service | `10-K/99` l.277–278, l.284 | 2000-03-23 | FACT (as disclosed) | High → **U.155 — the same company's Q3-1999 10-Q says zShops was introduced "in late September 1999" and its October 1999 8-K repeats "in late September"; the FY1999 table then dates the UK/German zShops to November while the Q3-1999 10-Q says the expansion happened "in October"** |
| P249 | 1999-03-30 | Amazon.com Auctions launch, as filed | Form 8-K event 1999-03-30 announcing the launch; **the company later filed that the service's revenue was minimal in the launch quarter** and that auctions/zShops transaction revenue was folded into net sales | date, revenue treatment | `8-K(1999-03-30)`; `10-Q Q2-1999`, `10-Q Q3-1999` net-sales definition; `10-K/A/99` l.292 | 1999-03-30 → 2000-09-08 | FACT (filing) + FACT (as disclosed) | High — **no take rate, no GMV, no listing count: the marketplace's own economics are undisclosed at every date (§P.2 "Not computed")** |
| P250 | 1999-04 / 1999-06 / 1999-11 | Other named launches in-window | **Amazon.com Cards** (free electronic greeting cards) **April 1999** · **toys and electronics July 1999** · **Amazon.com Payments and All Products Search late September 1999** · **Amazon.com Anywhere (wireless) October 1999** · **home improvement incl. a tool store, software, video games November 1999** | date, service | `10-Q Q3-1999` l.795–816 | 1999-11-15 | FACT (as disclosed, undated to the day) | High — **Cards is the conflict leg at U.142: the Q1-1999 10-Q already describes a free electronic greeting-card service that the Q3-1999 10-Q dates to April** |
| P251 | 1999 (nine months to 1999-09-30) | Acquisitions the company **names** | **Exchange.com, Alexa Internet, Accept.com** (10-Q Q3-1999, nine-month recital); FY1999 full list in the 10-K/A: **Exchange.com, Alexa Internet, Accept.com, LiveBid.com, the catalog and online-commerce assets of Acme Electric Motor Co. (Tool Crib of the North), Back to Basics Toys, "and other acquisitions"** | names | `10-Q Q3-1999` l.820–822; `10-K/A/99` l.550–554 | 1999-11-15 / 2000-09-08 | FACT (as disclosed) | High → **U.156 — WarehouseDirect, Internet Mail and Allaire return ZERO occurrences in every file in `sources/`; the named list is the only filed acquisition record** |
| P252 | 1999-06-10 / 1999-06-08 | Alexa Internet merger **completed** date vs the 8-K's index event date | completion **1999-06-10** (Item 2 text) reported under event date **1999-06-08** (EDGAR `reportDate`), filed 1999-06-11 | date | `8-K acc. 0000891020-99-000993` face and Item 2 | 1999-06-11 | FACT (two keys, one form) | High → U.120 |
| P253 | 1999-05-14 / 1999-05-19 / 1999-06 | The universal shelf, dated | the FY1999 10-K/A note: IPO of **18 million shares** completed "May 15, 1997", net proceeds **$49.1 million**; the company filed a **universal shelf on Form S-3 1999-05-19** (File No. 333-78797 line) and announced the **$1.25 billion convertible note** raise in the same window (Q2-1999 shows **1,250,000** proceeds from long-term debt) | shares, USD millions, dates | `10-K/A/99` l.2307–2310; `10-Q Q3-1999` l.839–840; `10-Q Q2-1999` l.332 | 1999–2000 | FACT | High (each cell) → **U.157 — the 10-K/A's "18 million shares" is restated only through January 1999 and contradicts the same paragraph's list of three post-IPO splits; see §P.2 t18** |
| P254 | 1999-06-29 / 1999-09 | The operating leadership change | **Joseph Galli, Jr. named President and COO in late June 1999** (elected to the Board); **Warren C. Jenson named Senior VP and CFO in September 1999** | dates, offices | `10-Q Q3-1999` l.824–828 | 1999-11-15 | FACT (as disclosed) | High — **Covey, CFO since December 1996 (Stage 2 §P170), is superseded inside this window; the exact handover day is UNKNOWN** |
| P255 | 1999-07-21 → 1999 holiday season | The distribution-centre claim, and the filed count beside it | 8-K release: "nearly **4 million square feet** of space at **seven distribution centers nationwide**—**more than 10 times** the distribution center floor space the company had in 1998" (forward-looking, "by the busy 1999 holiday shopping season"). Filed: five new DCs opened in the nine months to 1999-09-30 (Nevada, Georgia, Kentucky, Kansas, North Dakota) with **Kentucky also in the announced list** (`10-Q Q3-1999` l.830–833); the FY1999 10-K then lists **eight new DCs ≈ four million sq ft** (l.568–573) and **eight US DCs ≈ 3.8 million sq ft** (l.1602–1605) | sq ft, counts, states | `8-K(1999-07-21)` l.311–317; `10-Q Q3-1999` l.830–833; `10-K/99` l.568–573, l.1602–1605 | 1999-07-22 / 1999-11-15 / 2000-03-23 | FACT (claim) + FACT (as filed) | High (each text) → **U.148 (two different "eights"), U.151 (seven claimed vs five certified), U.117 (Kentucky in both lists)** |
| P256 | 1999-01-04 / 1999-08-12 | Share and per-share basis | every FY1999 per-share and share figure is on the **12× -restated** basis; the FY1999 10-K's own weighted-average shares **332,409** (1998 304,938; 1997 253,118) against the Item 6 basic/diluted **326,753 / 296,344 / 260,682** | thousand shares | `10-K/99` l.4049 (EPS note) and l.1766 (Item 6) | 2000-03-23 | FACT (two share series, one year) | High (each cell) / **Low (that they describe one population — they do not; §P.2 t19)** |
| P257 | 1999-12-31 | Stock options outstanding, **the ×2 question resolved** | **54,664 thousand** at 1997-12-31 on the FY1999 basis, weighted-average exercise price **$0.751** — against **27,332 thousand** and **$1.502** in the FY1998 10-K for the same date | thousand options, USD/share | `10-K/98` l.2991 vs `10-K/99` l.3886 and `10-K/A/99` l.2377 | 1999-03-05 / 2000-03-23 | FACT (audited, two vintages) | High → **U.146 — resolved by instrument: `27,332 × 2 = 54,664` and `1.502 ÷ 2 = 0.751` exactly (§P.2 t20). The doubling is the undocumented 1999-09-01 2-for-1, not double counting** |
| P258 | 1999-09-08 | Note-9 typographical correction, and what it proves | the 10-K/A exists partly to correct Note 9: the weighted-average exercise price of options **cancelled** and of options **exercised** in 1999 were **"inadvertently transposed"**, and the 1999 exercised price was incorrect | wording | `10-K/A/99` l.104–110 | 2000-09-08 | FACT (company's own statement of its error) | High — **the register's option-table rows must therefore not be built from the original 10-K's Note 9 figures for 1999** |
| **Cross-cutting, negative and structural rows** | | | | | | | | |
| P259 | Stage 3 | FY1996 income-statement lines **as recast in the Stage-3 documents** | net sales 15,746 and gross profit 3,459 **unchanged**; but product development **2,313 → 2,401**, G&A **1,035 → 1,411**, total opex **9,438 → 9,902**, loss from operations **(5,979) → (6,443)**, net loss **(5,777) → (6,246)**, LPS **(0.25) → (0.06)** on 111,271 | USD thousands | `10-K/98` l.1222–1247; `10-K/99` l.1732–1766 | 1999-03-05 / 2000-03-23 | FACT (audited, restated) | High → **§P.2 t21 proves the +464 of expense and −5 of interest income foot to the +469 net-loss change exactly; and U.159 records that Stage 2's hard-won FY1996 set is itself one of three printings** |
| P260 | 1996-12-31 | Working capital, **now filed** | **1,698** — the FY1998 and FY1999 Item 6 tables both print a 1996 working-capital line, which Stage 2 recorded as "the filing prints no 1996 working-capital line" and derived as 2,270 | USD thousands | `10-K/98` l.1262; `10-K/99` l.1781 | 1999-03-05 / 2000-03-23 | FACT (audited, restated basis) | High — **value corrected against Stage 2 §P81a on the point of the derived cell's necessity; the derived 2,270 remains valid ON ITS OWN AS-FILED BASIS (§P.2 t22) and the two are never averaged** |
| P261 | 1996-12-31 / 1995-12-31 | Total assets and stockholders' equity, restated | total assets **8,434** (1996) and **1,084** (1995); equity **2,943** and **977**; both against the as-filed **8,271 / 3,401** for 1996 (Stage 2 §P121) | USD thousands | `10-K/98` l.1263–1265; `10-K/99` same lines | 1999-03-05 | FACT (audited, restated) | High → **U.159 — the 1996 equity restatement is −458; the identity still holds on each basis (§P.2 t23), so neither pair is an error** |
| P262 | 1995-12-31 | Cash, and the two bases that finally reconcile it | **996** ("cash and cash equivalents", 10-K/A basis) vs **804** ("cash", the original FY1999 Item 6) — Stage 1 and Stage 2 carry **996** from the audited 1995 balance sheet | USD thousands | `10-K/A/99` l.221 (1995 = 996) vs `10-K/99` l.1779 (1995 = 804) | 2000-03-23 / 2000-09-08 | FACT (two captions) | High — **the amendment's restated basis restores the Stage-1/Stage-2 figure; the original 10-K's 804 is a narrower caption, not a different balance → §P.2 t24** |
| P263 | Stage 3 | **Revenue per employee, per-order ratios, average order value, take rate, GMV, order count, units per order, fill and returns rates, Associates commission rate, marketing spend separable from fulfilment** | **UNKNOWN — not computed, on purpose.** No denominator for any of them exists in any Stage-3 accession: no order count is filed in any year 1997–1999; no GMV line exists; no Associates rate, expense or attributable revenue appears anywhere in the FY1997–FY1999 corpus; fulfilment was inside marketing and sales until FY1999 disclosed the dollars separately | — | documented null across all Stage-3 filings; §P.2 "Not computed" list | — | UNKNOWN | **High (of the null)** — §S rows 3–5 |
| P264 | Stage 3 | Cost of being known, per customer | **UNKNOWN / refused**: `advertising ÷ net-new accounts` is not computable — net-new accounts are a cumulative-registration series whose composition CHANGED in 1999 (→ U.139), and advertising is a disclosed number with no channel split | USD | §P205, §P214, §P240, §P247 | — | UNKNOWN | High (that the ratio is not computable) |
| P265 | Stage 3 | **Gross margin path, in the company's own renderings** | **20.0% (FY1995) → 22.0% (FY1996) → 19.5% (FY1997) → 21.9% (FY1998, our DERIVED) → 17.7% (FY1999, our DERIVED)** — the first three are printed by the company (`10-K405/97` l.1403), the last two are arithmetic on its audited lines (§P.2 **t25**) | % | the Item 6 and MD&A tables | 1998-03-30 → 2000-03-23 | FACT + DERIVED | High — **the FY1999 fall is the year the mix moved to low-margin categories and marketplace revenue; the filing's own explanation is §P238's amortisation caption plus "relatively low product gross margins" (`10-K/99` l.730)** |
| P266 | Stage 3 | Loss per dollar of gross profit, the ratio that measures the burn | FY1997 **113.1%** (restated basis) · FY1998 **81.6%** · FY1999 **208.4%** — and FY1999 falls to **134.5%** if the non-cash goodwill/intangible amortisation is removed (`(605,755 − 214,694) ÷ 290,645 = 134.5%`, §P.2 **t26**). *A first draft of this cell printed "108.3%", which was a net-loss-basis subtraction that does not foot (t26 prints the check); the corrected figure is on the operating-loss basis and both renderings are shown* | % of gross profit | DERIVED on the restated pairs | 2000-03-23 | DERIVED | High (arithmetic) / **Medium (that either rendering is the useful one; both are printed for that reason)** |
| P267 | Stage 3 | Cumulative accounts, filed endpoints | 180,000 (1996-12-31, Stage 2) → **1,510,000** (1997-12-31, `ARS/97`) → **6.2 million** (1998-12-31, `10-K/98` l.1317) → **8.4m** (1999-03-31) → **10.7m** (1999-06-30) → **13.1m** (1999-09-30) → **over 17 million** (1999-12-31) | accounts | the named lines above | 1998-04-17 → 2000-03-23 | FACT (company counts, mixed basis) | High (each as stated) / **Low across the 1998/1999 boundary** → U.139 |
| P268 | Stage 3 | The window's stock-consideration volume | stock issued in connection with business acquisitions **774,409** (1999), **217,241** (1998), **--** (1997) — the acquisitions were paid for in paper, and the cash-flow statement proves it in a line the income statement does not have | USD thousands | `10-K/99` l.2875 | 2000-03-23 | FACT (audited, supplemental disclosure) | High — **`774,409 ÷ 609,819 = 1.27×` the prior year's entire net sales of stock consideration (§P.2 t27); it is not a revenue figure and is not used as one** |
| P269 | Stage 3 | Debt raised, in cash-flow terms | proceeds from long-term debt **75,000 (1997) → 325,987 (1998) → 1,263,639 (1999)**; repayments **(47) → (78,108) → (188,886)**; financing costs **(2,309) → (7,783) → (35,151)** | USD thousands | `10-K/99` l.2860–2864; `10-K/98` l.2260–2264 | 2000-03-23 | FACT (audited) | High |
| P270 | Stage 3 | The one in-window operational failure the corpus carries | Q3-1999 discloses that the company's **auction and zShops services do not take possession of goods**, that Amazon **"does not act as an agent"** and that it **"disclaims responsibility for delivery of goods"**; the FY1999 10-K's risk factors carry the failure mode **users of auction and zShops services may not complete transactions** | wording | `10-K/99` l.1307–1317; `10-Q Q3-1999` | 2000-03-23 / 1999-11-15 | FACT (as disclosed) | High — **this is a disclosed negative attached to the marketplace turn, and it is the only one in the corpus that is not a boilerplate risk factor** |
| P271 | Stage 3 | Segment reporting, first year | FY1999 reports **three segments**: US Books, Music and DVD/video; Early-Stage Businesses and Other; International (all Germany and UK) | count | `10-K/99` l.220–226, Note 14 | 2000-03-23 | FACT (audited) | High — **the segment frame is the first filed admission that the "Early-Stage Businesses" are a distinct object; no segment revenue is quoted in this part without its own cell** |

**Precision rule applied throughout (carried from Stage 1 §P.2 and Stage 2 §P.2).** Every audited money input is
filed **in thousands**, so a ratio of two such inputs is rendered to one decimal and the exact quotient is printed
beside it in §P.2. Where the filing gives its own rounded wording ("approximately 40%", "more than 4.7 million",
"over 17 million"), that wording is quoted and its line located, and no false precision is reconstructed from it.
**Every `t`-item below was run against the local text of the accession named**, not against a dossier's paraphrase
(method §3 lineage rule; task order; §14 rule 8).

### P.2a Corrections taken on this pass, and the rows they touch

**Method, stated once.** Each figure below arrived from an upstream dossier, a register row or an instruction file.
Each was searched across the local filings in `sources/` before being written. Where the string or the arithmetic was
absent, the row was reset to the filed value and the superseded value is printed **inside the same cell as a
retraction**, in the form Stage 2 established at `_parts/s2_p4.md` §P.2a. Nothing here deletes a row, an id or a
register entry (§14 rule 4); the retracted values are not evidence and are reused nowhere in this file as values.

| Row | Value / statement as received | Filed value | Where the filed value sits | What the received value or wording would have broken |
|---|---|---|---|---|
| P246 | "approximately **7,600 full-time** employees at 1999-12-31" | "approximately **7,600 full-time and part-time** employees" — and independent contractors are mentioned in the next sentence, unnumbered | `10-K/99` l.684–685 | the received label would have made the FY1999 basis **narrower** than FY1997's "614 full-time", so a 12.4× headcount multiple would have looked like a like-for-like full-time comparison. It is the opposite: FY1999 is the **widest** basis of the three |
| P260 | "the filing prints no 1996 working-capital line" (Stage 2 §P81a), derived 2,270 | a 1996 working-capital line **is** printed in the FY1998 and FY1999 Item 6 tables: **1,698** | `10-K/98` l.1262; `10-K/99` l.1781 | the derived 2,270 is not wrong — it is the as-filed balance-sheet arithmetic (`7,140 − 4,870`, §P.2 t22). But the **claim of necessity** was wrong, and a Stage-3 reader using 2,270 as "the filed 1996 working capital" would have contradicted the later audited comparative without noting it |
| P245 | "FY1998 net increase in cash **+23,685**", sourced to the FY1999 10-K/A | **+23,685 is the FY1998 10-K and FY1999 10-K figure; the FY1999 10-K/A prints FY1998 as (38,536)** | `10-K/98` l.2267 and `10-K/99` l.2867 = 23,685; `10-K/A/99` l.1338 = (38,536) | a row citing the amendment for the number the amendment removed. Both are printed here, each against its own document, and the swing is named (62,221) rather than averaged |
| P253 | "the IPO was **18 million shares**" (read out of the FY1999 10-K/A note without basis) | the IPO sold **3,000,000** shares at $18.00 (424B1, Stage 2 §P91–P92); the note's 18 million is the 3,000,000 restated through the **June 1998 and January 1999** splits only | `10-K/A/99` l.2307–2310; `10-K/99` l.3817–3820; 424B1 cover l.124 | 3,000,000 × 2 × 3 = 18,000,000 ✓, but × 2 again (September 1999) = 36,000,000, which the note does **not** say — so the note is internally stale against its own split list (§P.2 t18). Registering the number unqualified would have imported a 6× share-count error into any per-share use |
| P257 | option balances "27,332 **and** 54,664 thousand" treated as a possible double count | not a double count: two vintages of one balance date, separated by the September 1999 2-for-1; exercise price moves exactly inversely (1.502 → 0.751) | `10-K/98` l.2991; `10-K/99` l.3886 | `27,332 × 2 = 54,664` ✓ exactly (§P.2 t20). Summing them, or averaging, would have manufactured 81,996 thousand options that never existed |
| P210 / P211 | "FY1998 net sales 609,996" used in Stage-3 ratios **and** "609,819" used in others, unlabelled | both are filed; the Δ **−177** falls wholly on gross profit because cost of sales is unchanged at 476,155 | `10-K/98` l.1222–1225; `10-K/99` l.1732–1735 | `133,841 − 177 = 133,664` ✓ (§P.2 t7) — a cross-foot that proves the 177 is a revenue-line movement, not a reclassification of cost. Any FY1998 margin printed without naming the printing is ambiguous to ±0.02 pt, which is harmless once named and misleading when not |
| P236 | "FY1999 growth **169%**" sourced to the FY1999 10-K | the 169% is printed in the **10-K/A** l.285 comparative table; and the multiple is **2.69×** — the two renderings of one quotient (§P.2 t13) | `10-K/A/99` l.285 | the Stage-2 lesson at §P.2 s2 repeats: 2.69 read as 269% and 168.9 rendered as 169 are different objects. The received sourcing cited a document for a number it prints only in a re-keyed place |
| P239 | FY1999 "operating loss (605,755)" quoted alongside FY1998 "(111,960)" as a growth comparison | the FY1998 pair is **(111,960) as filed / (109,055) as restated**; the like-for-like ratio to 605,755 is **5.4×** (filed basis) or **5.6×** (restated basis) | `10-K/98` l.1236; `10-K/99` l.1748 | mixing the two FY1998 printings against the FY1999 restatement silently changes the multiple; §P.2 t26 prints both |
| P205 / P214 / P240 | "advertising $3.4m / $21.2m / $60.2m (1996–1998)" (held register row, `channels.csv`, width-defect) | **verified correct**, and extended: FY1995 $30,000 and FY1999 **$140.9m**, so the series is five points not three | `10-K405/97` l.2187–2189; `10-K/98` l.2459–2461; `10-K/99` l.3107–3109 | the held row is re-emitted with correct width (§S.9). The extension matters: 1996→1998 alone shows spend rising and ratio falling; adding 1999 shows the spend at **2.34× the 1998 figure** with the ratio still falling, which is the actual mechanism the stage's growth ran on |
| P215 | "fulfilment cost series" quoted from the FY1999 10-K as if FY1998 disclosed it | **no FY1998 document prints fulfilment dollars.** FY1998 discloses only that fulfilment sits inside marketing and sales | `10-K/98` l.1389–1392 vs `10-K/99` l.3097–3102 | a §P row of the form "FY1998 fulfilment 50.3, source FY1998 10-K" would cite a document that does not print the number; the retrospective note is the only source and is labelled as such |
| P229 | "Ingram 58% in FY1997 and **60%** in FY1998" | the pair is **58% (as filed) / approximately 60% (as recast for FY1997)** and **approximately 40% for FY1998** | `10-K405/97` l.1669–1670; `10-K/98` l.422–423, l.2374–2377 | the received pairing put 60% on FY1998, i.e. it read the FY1998 10-K's *comparative* FY1997 figure as the *own-year* FY1998 figure. That reverses the finding: concentration **fell** by roughly a third while the company grew 4.1× |
| P231 | "international sales 20% / 25% / 33%" read as three years of declining performance | a declining **share**, on rising absolutes: `609,996 × 20% = 121,999` vs `147,758 × 25% = 36,940` vs `15,746 × 33% = 5,196` (§P.2 t12) | `10-K/98` l.1325–1326 | a mix percentage is not a growth rate; used as one it would say the international business shrank in 1998 when it tripled |
| P234 | cumulative split across the stage "**6×**" | **12×** — three splits, not two: 2-for-1 (1998-06-01), 3-for-1 (1999-01-04), 2-for-1 (1999-09-01); `2 × 3 × 2 = 12` | `10-K/99` l.3817–3825; `10-Q Q2-1999` l.636, l.652–655; `10-Q Q1-1998` l.468 | **the single highest-consequence defect in this part.** A 6× factor halves every per-share figure produced from the mid-1997 basis; it would have put FY1999 EPS at (1.10) instead of (2.20) and made the option pair at §P257 look like a double count |
| P247 | "10.7m / 13.1m accounts" used as a continuation of the 6.2m series | both are expressly **inclusive of accounts with Amazon.com Auctions**; 6.2m (FY1998) is not | `10-Q Q2-1999` l.862; `10-Q Q3-1999` l.871; `10-K/98` l.1317 | subtracting 6.2m from 10.7m to show "growth" hides that the **population was redefined in the same year it was reported**; → U.139 |
| P223 | "Ingram 58% vs ~60%" (duplicate detection of one defect by two dossiers) | both detections retained as separate rows (U.135 from ST3_C and this row) rather than merged | — | method §14 rule 7's recovery rule: two independent finds of one defect are **both** kept, so a later reader can see the defect was reached twice and not once by copy |
| §P.2 t11 | "aggregate ~$55m" for the two European acquisitions (held `channels.csv` row) | the two releases state **~$11.4m** and **~$43.4m**; `11.4 + 43.4 = 54.8 ≈ 55`, but the two consideration **mixes differ** (stock vs cash) and neither is an audited total | `8-K(1998-04-17)`, `8-K(1998-04-24)`; S-4 File 333-56723 lineage | printed as DERIVED with the two terms named; it is a sum of two differently-composed company-stated figures and must never be cited as "the price of Germany and the UK" |
| §P.2 t5 | FY1997 gross fixed assets components "sum to 12,899" | the four filed components sum to **12,900**, one dollar above the filed total 12,899 | `10-K405/97` l.2300–2305 | rounding in the filed table. Recorded rather than "fixed": a §P row that re-derives the total from the components silently corrects the filing and then cites the filing |

**Defects reported, not fixed (outside this part's ownership).** (i) `sources.csv` **S0806** still registers a
non-existent "FY1996 annual report"; the 158-employee figure's real filed source is the FY1997 10-K405 l.729
(→ **U.118**). (ii) `conflicts.csv`'s 39 Stage-3 rows are keyed `P-U.114…P-U.152`; they must be re-keyed, not
re-emitted (map at the end of §U). (iii) The retracted **`$871,000` / `2,613,000`** leg still lives in the
instruction layer; **`context_appendices.md` still prints `2,613,000` and `$871,000`, twice each** — I re-checked and
both strings still occur there, and they occur **zero** times in `sources/` (§14 rule 10; → **U.168**). (iv)
`stage3_register_merge_held_rows.md` lists **ten held rows**; they are reproduced in full at **§S.9** and the two that
belong to this part's registers are re-emitted in the append blocks with canonical width.

### P.2 ARITHMETIC FOR EVERY DERIVED FIGURE (STAGE 3)

**t1 — FY1997 gross margin, both bases.** As filed: `28,813 ÷ 147,758 = 0.194995 → **19.5%**`, and the filing prints
"19.5%" itself at `10-K405/97` l.1403. As restated: `28,818 ÷ 147,787 = 0.194935 → 19.5%`. **The rendering survives
the restatement; the exact quotient does not**, which is why §P188 prints both and why no FY1997 margin may be quoted
to two decimals from a filing that rounds it.

**t2 — FY1997 operating expenses, the cross-foot that proves the recaption.** `40,077 + 13,384 + 6,741 + 1,211 =
61,413` ✓ against `10-K/99` l.1746, and `40,486 + 13,916 + 7,011 = 61,413` ✓ against `10-K/98` l.1234. **Two different
three- and four-line decompositions of the identical total**, published eleven months apart. The FY1999 carve-out of
stock-based compensation (1,211) is therefore funded by reductions in the other three lines (−409 marketing, −532
technology, −270 G&A; `−409 −532 −270 = −1,211` ✓ exactly, §P.2 **t2b**). This is the arithmetic behind **U.158**: the
FY1997 *total* is stable across printings, while the FY1997 *technology* figure is not a fact that can be quoted
without naming the document.

**t2b — the carve-out foot.** `40,486 − 40,077 = 409`; `13,916 − 13,384 = 532`; `7,011 − 6,741 = 270`;
`409 + 532 + 270 = 1,211` = the stock-based-compensation line exactly. The reallocation is closed, so no residual is
left to explain; **what is NOT disclosed is which compensation was moved out of which function**, and no note
says (→ §S).

**t3 — FY1997 growth, as the company computed it.** Filed "838%" (ARS/97 l.204) on the as-filed pair:
`(147,758 − 15,746) ÷ 15,746 = 132,012 ÷ 15,746 = 8.3835 → **838.4%**`. Restated "839%" (`10-K/98` l.1309) on the
restated pair: `(147,787 − 15,746) ÷ 15,746 = 132,041 ÷ 15,746 = 8.3857 → **838.6% → 839%**` at zero decimals.
**The one-point difference is the $29k of PlanetAll sales divided by a $15,746k base: `29 ÷ 15,746 = 0.184%`**, which
straddles the rounding boundary — that is the whole of the 838/839 pair (§P195 → U.126). The **multiple** is
`147,758 ÷ 15,746 = 9.38×`, never "938%", and never 838× (the Stage-2 s2 lesson repeats at a different magnitude).

**t4 — FY1997 depreciation, two audited values, no note.** `10-K405/97` l.2037 prints 3,388 in its own-year cash-flow
add-back; `10-K/98` l.2232 prints 3,442 for the same year in the comparative column (Δ **+54**), and FY1996 moves
286 → 296 (Δ **+10**). **Neither the FY1997 loss nor the FY1998 loss is changed by these amounts** (`(29,209)` →
`(32,595)` is driven by expense reclassification, not by +54 of depreciation), so the D&A difference is a
comparative-column reclassification with **no reconciling note anywhere in the corpus**. Consequence stated for §S:
the only honest FY1997 D&A cell names a document. Also note the printed depreciation is a **cash-flow add-back**, not
the income-statement charge; a reader who pairs 3,442 with gross fixed assets to compute an average life is pairing a
cash-flow line with a balance-sheet line.

**t5 — FY1997 gross fixed assets, components against total.** `7,118 + 4,505 + 914 + 363 = 12,900` against the filed
total **12,899** (`10-K405/97` l.2300–2305): a one-dollar rounding in the filing's own table. Net:
`12,899 − 3,634 = 9,265` ✓. **Received and re-set on this pass:** the FY1998 comparative prints `13,490 − 3,764 =
9,726` ✓, so **both** printings are internally consistent and both disagree with the other on 1997 by **+591 gross /
+461 net** (→ U.147). Accumulated depreciation rises by only 130 while gross rises by 591, which is the arithmetic
signature of additions reclassified **in**, not of depreciation reclassified **out**.

**t6 — Advertising as a share of net sales, five years.** `0.03 ÷ 0.511 = 5.9%` (FY1995); `3.4 ÷ 15.746 = **21.6%**`
(FY1996); `21.2 ÷ 147.758 = **14.3%**` (FY1997); `60.2 ÷ 609.996 = **9.9%**` (FY1998, filed basis);
`140.9 ÷ 1,639,839 = **8.6%**` (FY1999). **Spend rose 41.5× in dollars while the ratio fell from 21.6% to 8.6%**, a
13.0-point fall (all five inputs filed; the ratios are ours). On the restated FY1998 denominator the ratio is
`60.2 ÷ 609.819 = 9.87%` — the same rendering, which is why §P214 does not flag a basis problem here. **The held
register row's "21.6% to 9.x%" is therefore correct and is re-emitted, extended by FY1995 and FY1999.**

**t7 — The FY1998 −177 restatement, cross-footed.** `609,996 − 609,819 = 177`. Cost of sales is **identical** in both
printings (476,155), so `133,841 − 177 = 133,664` ✓ exactly matches the restated gross profit at `10-K/99` l.1735.
Margin: `133,841 ÷ 609,996 = 21.941%`; `133,664 ÷ 609,819 = 21.918%`; both render **21.9%**. **The Δ is therefore
confined to the revenue line** — which is the strongest local evidence available on the 177, and it is arithmetic, not
a note (→ U.149). It is not explicable by the PlanetAll pooling ($29k, which moved FY1997 **up**), because FY1998
moved **down**.

**t8 — FY1999 goodwill amortisation in proportion.** `214,694 ÷ 1,639,839 = 13.1%` of net sales, and
`214,694 ÷ 290,645 = 73.9%` of gross profit. **Warning attached to both numbers:** this is a **non-cash** charge
against acquired goodwill and intangibles, and §P.2 t26 shows what the operating-loss ratio looks like with it
removed. Nothing in this part uses it as a cost of operating the 1999 stores.

**t9 — FY1998 marketing and sales as a share.** `133,023 ÷ 609,996 = 21.807%` (filed) and `132,654 ÷ 609,819 =
21.753%` (restated) — **21.8% on both bases**, so the caption's ratio is basis-insensitive while its dollars are not.
FY1999: `413,150 ÷ 1,639,839 = 25.195% → **25.2%**`, a 3.4-point rise, and the FY1999 10-K attributes it to
fulfilment (`10-K/99` l.1980–1983) — the first year the company could support that sentence with a number (t16).

**t10 — FY1998 fixed assets.** `43,585` gross − accumulated = `29,791` net, so accumulated D&A at 1998-12-31 is
`43,585 − 29,791 = 13,794` (§P.2 **t10b**), against `13,490 − 9,726 = 3,764` at 1997-12-31 on the FY1998 basis; the
difference `13,794 − 3,764 = 10,030` is **more than the 9,421 restated FY1998 D&A charge by 609**, which is the
arithmetic trace of disposals, accumulated-amortisation of intangibles booked to other captions, or an addition-set
change — **and the composition is not disclosed** (§S). t10b therefore exists to stop the naive claim that gross
fixed assets and the D&A line foot.

**t11 — The two European acquisitions, summed.** `~11.4 + ~43.4 = 54.8 ≈ 55` USD millions of stated consideration for
Bookpages and Telebook, **with different consideration mixes**, both company-stated in the April 1998 8-K releases and
re-presented in the S-4 File No. 333-56723 lineage (one lineage, so one source). It is DERIVED, is labelled so, and is
never called "the price of the international launch" — the two European distribution centres were leased, not bought,
and their cost appears only inside the lease and marketing commitments table.

**t12 — International sales: share to dollars, and back.** FY1996 `15,746 × 33% = 5,196`; FY1997 `147,758 × 25% =
36,940`; FY1998 `609,996 × 20% = 121,999` — **dollars 23.5× in two years while the share fell 13 points**
(`121,999 ÷ 5,196 = 23.48`). The percentages are filed to whole numbers, so every dollar figure derived from them
carries **two significant figures at best** and is rendered to the nearest thousand only for the ratio, never quoted
as a filed balance. **This is also why Stage 2's §P111 retraction of "5,112" holds**: the Note prints "$5.1 million",
and a reconstruction to the dollar is false precision from a rounded input.

**t13 — FY1999 growth, both renderings.** `(1,639,839 − 609,819) ÷ 609,819 = 1,030,020 ÷ 609,819 = 1.68898 →
**168.9% → 169%**` (the 10-K/A prints "169%" at l.285 ✓); multiple `1,639,839 ÷ 609,819 = **2.69×**`. On the
**filed** FY1998 denominator: `1,639,839 ÷ 609,996 = 2.688×`, `+168.8%` — **the basis does not move the rendering**,
which is stated so a reader stops treating the FY1998 pair as consequential for growth.

**t14 — FY1999 gross margin.** `290,645 ÷ 1,639,839 = 0.177240 → **17.7%**`, and the identity
`1,639,839 − 1,349,194 = 290,645` ✓ foots. The **fall** from 21.9% is 4.2 points; over the whole stage, from FY1996's
22.0%, the fall is **4.3 points**.

**t15 — FY1999 total operating expenses.** `413,150 + 159,722 + 70,144 + 30,618 + 214,694 + 8,072 = 896,400` ✓
against `10-K/99` l.1746. Loss from operations: `290,645 − 896,400 = (605,755)` ✓. Net loss:
`(605,755) − 37,444 = (643,199)`; `(643,199) − 76,769 = (719,968)` ✓ (l.1748–1761). **Three cross-foots, all closing,
on the restated series** — which is what licenses the §P238–P239 rows as arithmetic rather than as an unverified
table lift.

**t16 — Fulfilment costs as a share of net sales, the guided-down ratio that rose.**
`12.1 ÷ 147.758 = **8.19%**` (FY1997); `50.3 ÷ 609.996 = **8.25%**` (FY1998); `188.4 ÷ 1,639,839 = **11.49%**`
(FY1999). Dollars grew **15.6×** in two years against sales growth of **11.1×**, so cost per dollar of sales rose.
**Denominator warning printed in-cell:** FY1997 and FY1998 fulfilment are disclosed **only** in the FY1999 note and on
the FY1999 restated basis, while §P237's FY1999 net sales is the FY1999 own-year figure — so all three ratios are on
the FY1999 restated revenue basis, and no mix of the filed FY1998 denominator with the note's FY1998 numerator is
valid. (Using 609,819 gives 8.25% unchanged.)

**t17 — Q4-1999 depreciation, the held row's arithmetic re-run.** `36,806 − 22,935 = 13,871` ✓ where 36,806 is the
FY1999 annual add-back (`10-K/99` l.2820) and 22,935 the nine-month figure (`10-Q Q3-1999` l.314). Against the FY1998
restated annual charge: `13,871 ÷ 9,421 = **1.47×**` — **a single quarter's depreciation exceeded the whole of the
prior year**, which is the clearest filed trace of the 1999 build-out's timing. Basis: nine-month-to-annual
subtraction of two unaudited/audited prints of the same caption; the Q3 figure is unaudited, so the residual Q4 figure
inherits that status and is labelled ESTIMATE/DERIVED, not FACT.

**t18 — The 10-K/A's "18 million shares" IPO, resolved.** Filed at the 424B1: **3,000,000** shares (Stage 2 §P91).
Restatements after the offering: × 2 (1998-06-01) = 6,000,000; × 3 (1999-01-04) = **18,000,000**; × 2 (1999-09-01) =
**36,000,000**. The note at `10-K/A/99` l.2307–2317 **lists all three splits and then prints 18 million**, i.e. it is
restated through January 1999 only, and it does the same for the preferred conversion: "an effective rate of **36
shares of common stock for one share of preferred**" with "**20,678,256**" converted shares —
`574,396 × 36 = 20,678,256` ✓ exactly, and `3,446,376 × 6 = 20,678,256` ✓, so 36 = the Stage-2 IPO-date ratio of 6
(§P.2 s27) × 2 × 3, again missing the September doubling. **On the FY1999 basis the IPO is 36 million shares and the
conversion ratio is 72:1.** Nothing in this part restates either to a "correct" single figure: the note is quoted, the
arithmetic is shown, the discrepancy is registered (**U.157**), and no per-holder percentage is built on any of them.

**t19 — Two share series for one year.** Item 6 basic-and-diluted FY1999 **326,753** vs the EPS note's weighted
average **332,409**; 1998 **296,344** vs **304,938**; 1997 **260,682** vs **253,118** (`10-K/99` l.1766 vs l.4049).
**These are not one population**: the note's figure is a weighted-average share count net of shares subject to
repurchase and including different equivalents, and the Item 6 figure is the EPS denominator the company reported.
The three differences run **both ways** (+5,656 / +8,594 / −7,564), which is the proof that no arithmetic reconciliation
exists and that no reader may treat them as a rounding pair. No ratio in this part divides anything by a share count
without naming which one.

**t20 — The options pair, and the test that settles it.** `27,332 × 2 = 54,664` ✓ and `1.502 ÷ 2 = 0.751` ✓ (both
exact). **The exercise price moving down by exactly the factor the count moved up is the signature of a split
restatement, not of a change in the grant population** — a real doubling of options outstanding would not have halved
the weighted-average exercise price. This is the arithmetic that resolves U.146 by instrument.

**t21 — The FY1996 restatement, footed.** Opex: `9,902 − 9,438 = **+464**`; loss from operations
`(6,443) − (5,979) = −464` ✓ — **the same 464**. Net loss: `(6,246) − (5,777) = −469`, of which `−464` is operating
and `−5` is interest income (`202 → 197` ✓). **The FY1996 restatement is therefore fully explicable in its own
arithmetic even though no note itemises it** — which is why §P259 prints it as FACT (restated) rather than as a
discrepancy, and why U.159 registers the *existence of three printings* rather than an error.

**t22 — FY1996 working capital, two legitimate answers.** As-filed basis: `7,140 − 4,870 = **2,270**` (Stage 2 §P81a,
derived because the FY1997/A5 filings print no 1996 working-capital line). Restated basis as filed by the company:
**1,698** (`10-K/98` l.1262, `10-K/99` l.1781). `2,270 − 1,698 = 572`, and the FY1996 balance-sheet restatements move
total assets from 8,271 to **8,434** (+163) and equity from 3,401 to **2,943** (−458): `+163 − (−458) = 621`, which is
**not** 572 — so the working-capital change is not fully explained by the two headline restatements either, and the
residual 49 is undisclosed. **Neither figure is printed alone; the pair is the row** (§P260 → U.159).

**t23 — The balance-sheet identity on each 1996 basis.** As filed: `4,870 + 3,401 = 8,271` ✓. Restated: liabilities
and equity must still foot to **8,434**; with working capital 1,698 and the filed current-liability figures the
restated pair is internally consistent **on its own basis only**, and no cell in this part mixes a 1996 as-filed
liability with a 1996 restated asset. **The identity holds twice and the numbers differ — that is the finding.**

**t24 — The 1995 cash line, 804 vs 996.** `10-K/99` l.1779 prints 1995 **cash 804**; `10-K/A/99` l.221 prints 1995
**cash and cash equivalents 996**; Stage 1/Stage 2 carry **996** from the audited 1995 balance sheet (§P262). The
amendment's restated caption therefore **restores** the earlier figure, and the original FY1999 Item 6's 804 is a
narrower caption, not a different balance. **`1,639,839`-scale consequences:** none for any Stage-3 ratio; but a row
that printed 804 as "1995 cash, restated" would have contradicted Stage 1's audited balance sheet on a caption change.

**t25 — The margin path, with each rendering sourced.** 20.0 / 22.0 / 19.5 are **the company's own renderings**
printed together at `10-K405/97` l.1403 ("19.5% / 22.0% / 20.0%"). 21.9 (FY1998) and 17.7 (FY1999) are **ours**, from
t7 and t14. The sequence is printed once, with a note that the first three are audited-year company renderings and the
last two are derived from audited lines — never as five equally-status figures.

**t26 — Loss per dollar of gross profit, with and without the non-cash charge.** FY1997 `32,595 ÷ 28,818 = 113.1%`
(restated basis) / `29,209 ÷ 28,813 = 101.4%` (as filed). FY1998 `109,055 ÷ 133,664 = 81.6%` / `111,960 ÷ 133,841 =
83.7%`. FY1999 `605,755 ÷ 290,645 = **208.4%**`; **excluding goodwill/intangible amortisation** `(605,755 − 214,694)
÷ 290,645 = 391,061 ÷ 290,645 = **134.5%**`. §P266's "108.3%" was the *net-loss*-basis rendering
`(719,968 − 214,694) ÷ 290,645` **which does not foot** — `505,274 ÷ 290,645 = 173.8%` — **so §P266 is corrected on
this pass to the operating-loss basis, 134.5%, and both the with- and without-amortisation renderings are printed.
Printed here as a self-correction because §P.2 must foot before §P does.**

**t27 — Stock consideration against revenue.** `774,409 ÷ 609,819 = 1.27×`: the FY1999 value of stock issued for
business acquisitions exceeded **127% of the prior year's entire net sales** — stated as a ratio of two filed lines
and **not** as a return, a valuation or a cost. The FY1999 net-sales figure is used because the acquisitions were
priced against a market value, not against FY1999 sales; the sentence exists to scale the paper, nothing else.

### NOT COMPUTED, and why (the §P.2 negative list, Stage 3)

Carried in this form from Stage 1 §P.2 and Stage 2 §P.2. **Each item below has a filed numerator or a filed
denominator, but never both** — which is a different statement from "we did not bother".

(i) **Revenue per employee.** Not computed. Three bases at three year-ends (614 full-time / ~2,100 unqualified /
~7,600 full-time **and part-time**), each with an unnumbered contractor pool behind it, and the FY1999 basis wider
than the FY1997 one. Any productivity figure would be a **band with a moving definition**, and §R's job is to show
the three bases side by side rather than to launder them into one quotient.
(ii) **Revenue per account, orders, average order value, units per order, fill/back-order/returns rates,
chargebacks.** Not computed. **No order count exists in any accession in any year of the stage** (the Stage-2 §P181
null persists through FY1999), so there is no denominator at any date.
(iii) **GMV / bookings / take rate / marketplace commission revenue separately.** Not computed. From 1999 the
company's net sales **include** auctions and zShops transaction revenue "which include sales commissions, placement
fees and fees" (`10-K/A/99` l.292) **inside one line**; no accession splits it, so a take rate would be invented.
(iv) **Associates Program: commission rate, total paid out, attributable revenue or orders.** Not computed.
Enrolment counts are filed at four dates (4,800+ 1996-12-31 → >140,000 1998-09 → ~200,000 1998-12-31 → ~430,000
2000-02-29); **no rate, expense, payout total or attributable revenue appears anywhere in the FY1997–FY1999 corpus** —
the whole programme is disclosed as a count and a mechanism.
(v) **Advertising separated from fulfilment and customer-service payroll in FY1997–FY1998.** Not computed. The
marketing-and-sales caption bundles them (`10-K/98` l.1389–1392) and only **fulfilment** is later carved out in a
note (§P215); **no accession gives an advertising-plus-media number and a channel split**.
(vi) **Ingram dollar purchase volume.** Not computed. `58%` / `~60%` / `~40%` are filed **percentages of purchases**
and **no purchase total is filed** in any year; `0.58 × (unknown)` is unknown.
(vii) **Series valuation, market-cap-to-sales multiples, or any per-holder percentage.** Not computed. The share
basis is contested (t18, t19), the 10-K/A itself prints an internally stale figure, and §2 forbids reading the outcome
back into the earlier round.
(viii) **Any CAC or LTV figure.** Not computed: no order count (ii), no separable advertising (v), no
gross-margin-per-order, and an account population whose composition changed mid-series (U.139).
(ix) **Average distribution-centre lease cost, or cost per square foot of the 1999 build-out.** Not computed. Square
footage is filed in two mutually exclusive "eights" (U.148) and lease commitments are bundled with marketing
(`10-K/98` l.2853's $134,829 total minimum lease payments line is a **single undifferentiated column**).
(x) **Customer-support cost per contact, or web-site uptime.** Not computed; nothing is filed on either at any date.

## Q. CHRONOLOGICAL MICRO-TIMELINE, 1997-05-16 → 1999-12-31

**Endpoint choice, stated before the first row, because the endpoint is contested (→ U.153).** This §Q runs to
**1999-12-31**: it is the last date the window can be run to without importing a document the stage itself does not
need, it is the date the Stage-3 intake was executed to, and it is the only candidate that the FY1999 10-K can
describe from inside. **It is not asserted as the correct stage boundary.** The competing candidates — 1997-12-31 (the
Delaware centre and the first term loan), 1999-06-30 (the shelf and the conversion pivot), 1999-09-30 (the nine-month
distribution and marketplace state) — are registered with their evidence at U.153, and the argument ST3_A made for
one of them ("the first filing that uses the verb *opened* for a distribution centre") is **falsified there** by three
earlier filings. Rows are ordered by date. `(PB)` marks a post-boundary row printed only to date an absence; `(L)`
marks the same registration lineage as another cited document, so it adds no independence. **Two date keys are
periods by convention:** `1999-Qn` rows are the filed quarterly tables, whose register twin is keyed to the
quarter-**end** day, and a `1998-11`-style key means the filing goes no finer than the month. **A row whose date cell
is a span does not bind the point-dated rows after it.**

**Failures, retractions and abandoned experiments are rows here, not footnotes** (method §2's record-selection null;
§10's trigger list). Where the only in-window negative is a **company admission in a risk factor or a note**, the row
says so; where the negative is the falsification of the company's own guidance, the row carries both sentences.

| Date | Event | Source | Class | Confidence |
|---|---|---|---|---|
| 1997-05-16 | **Stage 3 opens.** The day after the 424B1 was filed: 3,000,000 shares all primary at $18.00, $49.4m estimated net, 256 employees, one Seattle warehouse of ~92,400 sq ft through which "the Company processes all sales", no second site, no non-book store, no CFO with a day-dated start, no marketplace, no foreign entity. **The opening state is Stage 2's closing state and is not re-derived here** | Stage 2 §P91–P98, §P102, §P149, §R; 424B1 `(L)` | FACT (carried) | High |
| 1997-06-06 | **S-8 File No. 333-28763 filed** — the 1994 Stock Option Plan registered for the first time post-IPO; the dilution engine is put on paper eight weeks after the offering | `S-8_FileNo-333-28763` acc. 0000950151-97-000177 | FACT (filing) | High |
| 1997-08-14 | **First post-IPO Form 10-Q** (Q2-1997, acc. 0000891020-97-001148) — the first quarterly report Amazon ever filed as a public company, and the first in-window document that could revise anything Stage 2 asserted | `10-Q_Q2-1997` | FACT (filing) | High |
| 1997-09-11 | **S-8 POS Amendment No. 1** to the 1994 plan; **the Q3-1997 10-Q follows on 1997-11-14** | `S-8POS_FileNo-333-28763_AmdtNo1`; `10-Q_Q3-1997` | FACT | High |
| **1997-11-07 → 11-10** | **The debt pivot begins: a $75,000,000 senior secured term facility with Deutsche Bank**, reported on Form 8-K Item 5 and filed again inside the Q3-1997 10-Q. **The company that four months earlier had $79k of working capital now takes secured bank debt** | `8-K(1997-11-07)` acc. 0000950151-97-000357 (filed 1997-11-10); `10-Q_Q3-1997` | FACT (filing + Item 5) | High — §P202's 76,702 at 1997-12-31 is this facility net of a $47 repayment |
| **1997-11** | **The first distribution centre outside Washington OPENS: 200,000 sq ft at New Castle, Delaware**, with the Seattle centre expanded to 85,000 sq ft — disclosed in the FY1997 10-K405 with the verb **"opened"** (`10-K405/97` l.1646–1648). **This row is the falsification, in the corpus, of the argument that a later filing is "the first that uses 'opened'" → U.153** | `10-K405/97` l.1643–1652 | FACT (audited, in-period) | High |
| **1997-12-23** | **The $75,000,000 term loan drawn** (Stage 2's `(PB)` row becomes in-window here); long-term debt at 1997-12-31 **76,702** | `10-K405/97` Note 3 l.2312 area; `10-K/98` l.1264 | FACT (audited) | High |
| 1997-12-31 | **STAGE-3 YEAR ONE CLOSES.** Net sales **147,758** as filed (147,787 restated); gross margin **19.5%**; marketing and sales 38,964; product development 12,485; G&A 6,573; total opex 58,022; loss from operations (29,209); **net loss (27,590) as filed** (31,020 restated); pro forma LPS (1.27) on 21,651; D&A 3,388; gross fixed assets 12,899 / net 9,265; inventory 9,001; working capital 93,158; total assets 149,844; equity 28,591; **614 full-time employees**; **1,510,000 cumulative accounts**; advertising **$21.2m**; fulfilment **$12.1m** (disclosed only retrospectively, in the FY1999 note); Ingram **58%** of purchases; international **25%** of net sales; Media Metrix rank 90th → top 20 | `10-K405/97` l.1177–1194, l.1403, l.1643–1670, l.1861–1881, l.2037, l.2300–2308, l.2187–2189; `ARS/97` l.204–218; `10-K/99` l.1970–1972 | FACT (audited) + FACT (as disclosed) | High (each cell) / **U.125, U.145, U.147, U.159 on the restated legs** |
| **1998-02-13 / 02-17** | **Two Schedule 13G filings by the founder's family and by Bezos personally** — the first post-IPO statement of who holds the company, filed as the FY1997 report was being prepared | `SC13G (1998-02-13)` acc. 0000891020-98-000174 (Bezos, Migual Bezos, Jacklyn Gise Bezos); `SC13G (1998-02-17)` acc. …-000175 (Jeffrey Bezos) | FACT (filing) | High |
| 1998-03-05 | **FY1997 Form 10-K405 filed** — Amazon's **first annual report ever filed**, a delinquency form: it prints the 158-employee comparative, the deleted sales-tax and security risk factors, the Delaware "opened" sentence, and the first advertising-expense note in the company's history | `10-K405/97` | FACT (audited) | High → U.118, U.204(→U.118), U.153, U.159 |
| **1998-04-17** | **First foreign acquisitions announced: Bookpages Ltd (UK) and Telebook.com (Germany), plus Internet Movie Database Limited**, for **540,066 restricted shares** — the company buys three small sites rather than build export operations, and pays entirely in paper | `8-K(1998-04-17)` acc. 0000891020-98-000694; `10-Q Q1-1998` l.483; `10-Q Q2-1998` l.478 | FACT (filing + attached release) | High → **U.163 — the register's "~$55m aggregate, mostly stock" is a §P.2 t11 sum of differently-composed stated figures; the filed instrument for the three sites is 540,066 shares** |
| 1998-04-17 | **ARS for FY1997 filed** (with the DEF 14A the same day) — "But this is Day 1 for the Internet…"; the only **contemporaneous** founder-state document in the first half of the stage, outranking any retrospective interview for what Bezos believed while Stage 3 was running | `ARS_1997`; `DEF14A/98` | FOUNDER CLAIM (contemporaneous) | High (as a 1998 document) |
| **1998-04-24 → 05-05** | **$275,000,000 of 10% Senior Discount Notes announced (04-24), then upsized (05-05)**; the indenture and form of note are filed as Q1-1998 exhibits 4.1/4.2/4.3 with the Bank of New York, and the notes are ultimately registered on the 424B2 of 1998-08-13 and S-4 File No. 333-56723 (**~$326m gross**). **The stage's funding mechanism changes from bank debt to capital-markets paper in eleven days** | `8-K(1998-04-24)`; `8-K(1998-05-05)`; `10-Q Q1-1998` EX-4.1–4.3; `424B2/98`; `S-4_FileNo-333-56723` | FACT (filings) | High |
| **1998-06-03 / 06-12** | **Two Form S-4 registration statements, nine days apart, and the SIC classification changes between them.** 333-55943 (Junglee) covers **up to 5,000,000** shares and carries SIC **2731 BOOKS: PUBLISHING**; 333-56723 (Bookpages/Telebox — the European set) carries SIC **5961 RETAIL-CATALOG & MAIL-ORDER HOUSES**. **A four-business-day interval is as precisely as the "what are we?" question is answered on the cover of a filing anywhere in the corpus** | `S-4_FileNo-333-55943` l.970; `S-4_FileNo-333-56723` cover | FACT (filings) | High → U.116, U.137, **U.123 (why the SIC change must not carry a boundary)** |
| **1998-06-01** | **2-for-1 stock split effected**, in the form of a stock dividend to holders of record **1998-05-20** — the first of the stage's three splits and the one most often missed when a cumulative factor is computed | `10-Q Q1-1998` l.468; `10-K/99` l.3820 | FACT | High → **U.128, §P.2 t18 (the 12× factor)** |
| 1998-06-18 | **Music-store launch decision, then the store.** The 424B2 of 1998-08-13 and the FY1999 launch table date music to **June 1998**; **no day survives in the corpus** — the one exact launch day in the whole stage belongs to video, not music | `424B2/98`; `10-K/99` l.274 | FACT (month only) | Medium (month) / **UNKNOWN (day)** |
| **1998-08-03** | **Merger agreements with Junglee.com and PlanetAll signed** (the 8-K carries a plan of merger with "AJ Acquisitions"); the FY1999 comparative restatement of **all** periods for PlanetAll's pooling of interests is the accounting event behind most of this part's as-filed/as-restated pairs | `8-K(1998-08-03)` acc. 0000891020-98-001210; `10-K/98` l.1269; `10-K/99` l.1788 | FACT | High → **U.125, U.126, U.159** |
| **1998-08-12 → 10-26** | **A Form 8-K/A amends the 8-K of 1998-08-12.** An amended current report inside the window is a filing-correction event; **the amendment's substance is the record's own evidence that the original was wrong or incomplete**, and its reason is not stated in the body | `8-KA_event-1998-08-12` acc. 0000891020-98-001491 (filed 1998-10-26) | FACT (documented correction) | High (that it exists) / **UNKNOWN (what was corrected)** → §S |
| 1998-08-13 | **424B2 final prospectus** for the senior discount notes; it files the half-year state: cumulative sales "more than **$367 million**" to "approximately **3.1 million** customer accounts" through 1998-06-30, **over 62% of orders** from repeat customers in the six months, **21%** international in the six months | `424B2/98` l.396–400 | FACT (as disclosed) | High → U.127, U.140 |
| **1998-08-27** | **A third 8-K in August** attaches Ernst & Young's consent and financial statements — the acquired companies' audited history arrives in the registrant's own current report; the FY1997 gross-fixed-asset figure **13,490** appears here (l.1485, l.2327) **before** the FY1998 10-K prints it as a comparative | `8-K(1998-08-27)` acc. 0000891020-98-001370 | FACT | High → **U.147 — the recast 1997 balance appears mid-1998, so the "own-year vs comparative" ordering is not the whole story** |
| **1998-09-11 / 09-30 / 10-01 / 10-15** | **The shelf architecture is built in five filings over five weeks**: S-8 for an acquired plan (09-11), **S-3 File No. 333-65091 filed 1998-09-30**, its S-8 POS (10-01), S-3/A (10-15). **Registration infrastructure, not a product, is the densest activity of the autumn** | `S-8_FileNo-333-63311`; `S-3_FileNo-333-65091`; `S-8POS_FileNo-333-63311`; `S-3A_FileNo-333-65091` | FACT | High |
| **1998-10** | **UK and German stores open** (October 1998) — the company's own launch table, dated by month; **the first foreign-selling sites, thirteen months after the company first discussed expanding and four years after it began shipping abroad from one Seattle address** | `10-K/99` l.274; `10-K/98` l.1321 | FACT | High (month) / **UNKNOWN (day)** |
| 1998-10-22 / 10-27 | **424B3 "FINAL PROSPECTUS" for 2,662,125 shares** and a supplement: a **resale** registration — "certain stockholders … or their pledgees, donees, distributees". **The first time the corpus shows insiders' paper being registered for sale rather than the company's** | `424B3/98`; `424B3 supplement` | FACT | High → **§S: 33 further 424B3 supplements were filed in 1999 and deliberately not fetched (intake §5a); the resale cadence is itself a fact about market activity** |
| **1998-10-28** | **Q3-1998 results release.** Music sales **$14.4 million** in the quarter; Associates **"more than 140,000"** member sites. The FY1998 10-K will claim Amazon became "the number one online music seller" and print **no competitor figure at all** | `8-K(1998-10-28)` l.199, l.296; `10-K/98` Item 1 | FACT (unaudited company figure) + COMPANY CLAIM (ranking) | High (the number as stated) / **Low (the ranking)** → U.143 |
| **1998-11-19** | **The board announces a 3-for-1 stock split** (press release: "ANNOUNCES 3-FOR-1 STOCK SPLIT"). **This is the last split announcement on Form 8-K in the corpus** — the January 1999 split is here, the September 1999 split is **not** announced on any 8-K, and its only filed record is a recital inside a 10-Q | `8-K(1998-11-19)` acc. 0000891020-98-001686, EX-99 headline | FACT (filing + release) | High → **U.128** |
| **1998-11-17** | **THE VIDEO STORE LAUNCHES — the only exact launch DAY in the entire Stage-3 corpus.** "Amazon.com launched its video store **on November 17** with more than **60,000** VHS and [DVD titles]". The FY1999 launch table dates the same event to **"November 1998"** and never names the day; the day survives only in a January 1999 8-K release the tables do not cite | `8-K(1999-01-26)` l.306; `10-K/99` l.276; `10-K/98` l.1322, l.1370 | FACT (company release, day-dated) | High as disclosure → **U.162** |
| 1998-11-30 | **A Schedule 13D is filed** — a 13D asserts control intent where a 13G disclaims it. **Not retrieved** (intake §5b), so who filed it and what they intended is UNTRIED, not null | EDGAR catalogue row `0000891020-98-001712` | FACT (that the row exists) / **UNKNOWN (contents)** | High (existence) → §S UNTRIED |
| **1998-12-31** | **STAGE-3 YEAR TWO CLOSES.** Net sales **609,996** as filed (609,819 restated); gross profit **133,841 → 133,664**; margin **21.9%** on both bases; total opex **245,801** including a **new 50,172 caption** for merger/acquisition costs and goodwill amortisation; loss from operations (111,960) → (109,055); **net loss (124,546)**; LPS (0.84) on 148,172; D&A **9,692 → 9,421**; gross fixed assets **43,585** / net **29,791**; working capital **262,679**; total assets **648,460**; long-term debt **348,140** (+ 684 current); equity **138,745**; **~2,100 employees**; **6.2 million** cumulative accounts; **over 60%** of FY1998 orders from repeat customers; advertising **$60.2m**; **fulfilment $50.3m — disclosed nowhere in 1998**; Ingram **~40%**; **~200,000** Associates sites; **4.7 million titles** (wider definition); international **20%**; B&N announces it will **buy Ingram** — Amazon's 58%-of-purchases supplier is being acquired by its largest competitor, and Amazon discloses it as a risk factor | `10-K/98` l.422–423, l.528, l.1222–1265, l.1317–1326, l.2374–2377, l.2459–2461, l.2750; `ARS/98` l.157, l.160; `10-K/99` l.1970–1972 | FACT (audited) + FACT (as disclosed) | High / **U.144, U.145, U.149, U.159 on the recast legs** |
| **1999-01-04 / 01-05** | **3-for-1 split effected** (record 1998-12-18), and an 8-K for period ended **1999-01-05** reports it. **Every prior per-share figure in the corpus moves by ×3 on this date**, and the FY1998 10-K's own F2 footnote says the selected financial data "HAVE NOT BEEN RESTATED FOR THE STOCK SPLIT" (`10-K/98` l.5708–5710) — **the same document therefore carries two share bases in two places** | `10-K/99` l.3821–1323; `8-K(1999-01-05)`; `10-K/98` l.5708 | FACT | High → **§P.2 t18, U.164** |
| **1999-01-26** | **FY1998 and Q4 results release** ("RECORD HOLIDAY SEASON PUSHES CUSTOMER [SATISFACTION…]"). **The record holiday is the event that makes the Delaware/Nevada capacity question urgent**, and the same release carries the video store's exact November 17 day | `8-K(1999-01-26)` acc. 0000891020-99-000103 | FACT | High |
| **1999-01-28 → 02-03** | **"$500 million ask" (two 8-Ks on 1999-01-28) → the $1.25 billion 4¾% convertible note offering CLOSED 1999-02-03.** **The raise came in at 2.5× the announced ask.** Q2-1999's cash-flow statement prints **1,250,000** of proceeds from long-term debt against a full-year 1,263,639 | `8-K(1999-01-28)` ×2; `8-K(1999-02-03)` acc. …-000125; `10-Q Q2-1999` l.332; `10-K/99` l.2860 | FACT (filings + cash-flow line) | High |
| **1999-03-15 / 03-16 / 03-23** | **Two more S-8 plan registrations, the S-3 File No. 333-74435 shelf, and the PRE 14A** — governance and shelf infrastructure advance in the same fortnight in which the FY1998 annual report is filed | `S-8_FileNo-333-74419/74435`(03-15/03-16 area); `S-3_FileNo-333-74435` 1999-03-16; `PRE14A/99` 1999-03-15; `DEF14A/99` 1999-04-07 | FACT | High |
| 1999-03-28 / **1999-03-30** | **Amazon.com Auctions LAUNCHES**, announced on Form 8-K dated 1999-03-30 (a press release 03-28 precedes it). **The company that had always bought inventory and sold it now opens a venue where it does neither** — and its Q3-1999 and FY1999 filings expressly **disclaim responsibility for delivery of goods** and state it does not take possession | `8-K(1999-03-30)` acc. 0000891020-99-000568; `10-K/99` l.1307–1317; `10-Q Q3-1999` | FACT (filing) + FACT (as disclosed) | High → §P249, §P270 |
| 1999-04-07 | **ARS for FY1998 and DEF 14A 1999 filed** — "We predict the next 3 1/2 years will be even more exciting"; the proxy pays Aposporos **$142,083** for 1998 under a title the 10-K had given Shriram five weeks earlier, and restates Dalzell's 1997 option grant from **125,000 to 750,000** on the split alone | `ARS_1998`; `DEF14A/99` l.617–627 | FACT (filing) + FOUNDER CLAIM (contemporaneous) | High → U.119, U.130 |
| **1999-04 (month)** | **Amazon.com Cards launches** — "a free electronic greeting card service" — per the Q3-1999 10-Q; **yet the Q1-1999 10-Q already describes such a service in the quarter it covers** | `10-Q Q3-1999` l.795; `10-Q Q1-1999` | FACT (two incompatible company statements) | **Medium → U.142** — something greeting-card-like preceded the named April launch |
| 1999-04-26 | **POS AM to S-4 File No. 333-55943 raises the shelf from 5,000,000 to 15,000,000 shares**; the same day two 8-Ks are filed (one a press release, one later carrying a PwC consent for an acquired company's financials) | `POSAM_FileNo-333-55943_AmdtNo1`; `8-K(1999-04-26)` acc. …-000717 and …-000805 | FACT | High → U.116 |
| **1999-05-14 / 05-19** | **Two acquisitions COMPLETE the same day as, or days after, an 8-K for period ended 1999-05-14: Exchange.com (legal name e-Niche Incorporated) and LiveBid.com** — ~**$145m** and ~**$40m** purchase prices, **1,893,944** and **553,770** shares issued, substantially all allocated to goodwill amortised over ~3 years, **and an earn-out of up to $27.5m of additional shares for Exchange.com contingent on performance goals**. **The universal shelf on Form S-3 is filed 1999-05-19** | `10-K/A/99` l.1729–1750; `10-Q Q3-1999` l.839; `8-K(1999-05-14)`; `S-3_FileNo-333-78797` | FACT (audited note + filings) | High → **U.156 — this is the filed Exchange.com record, and the same note names no WarehouseDirect, Internet Mail or Allaire** |
| **1999-05-17** | **Q1-1999 10-Q filed** — it carries (i) the five 1999-03-11 "Sales Agreements" with **The Buschman Company**, which the intake manifest mislabelled as the marketplace's merchant contracts; (ii) **"A new distribution center was leased and opened in Nevada during the quarter"** (l.592) and the same in MD&A (l.915); (iii) accounts **3.1m → 8.4m** (+265%) in a year; (iv) cumulative accounts 8.4 million. **Both legs of U.114/U.152 and the boundary falsification at U.153 live in this one document** | `10-Q_Q1-1999` l.592, l.915, l.1660–1669, l.626 | FACT | High |
| **1999-06-08 → 06-11** | **Alexa Internet merger: 8-K event date 1999-06-08, Item 2 completion 1999-06-10, filed 1999-06-11**; **Accept.com completes 1999-06-09** for ~**$189m** (1,755,356 shares). **~$2.8m of the Accept.com and Alexa purchase price is written off as in-process R&D because "technological feasibility had not been established and no alternative future uses existed"** — the company's own filed statement that some of what it bought did not yet work | `8-K(1999-06-08)`; `8-K(1999-06-09)`; `10-K/A/99` l.1719–1760 | FACT (audited note) | High → U.120, **U.165 (the IPR&D write-off as an in-window failure record)** |
| **1999-Q2** | **The convertible proceeds land**: Q2-1999 cash-flow prints **1,250,000** of long-term-debt proceeds and **617,007** of stock issued for business acquisitions in six months, against 217,241 for all of 1998. Cash rises to **42,539** at 1999-06-30 from 25,561 at year-end — **and the FY1999 10-K/A will later restate this same six months' cash movement onto a different definition of "cash"** | `10-Q Q2-1999` l.332, l.339–347 | FACT (unaudited interim) | High → U.154 |
| **1999-06-24 / late June** | **Joseph Galli, Jr. named President and Chief Operating Officer** and elected to the Board; **an S-3/A amendment (1999-05-13) and an S-3A (1999-06-08) precede it**. **The company installs a second-in-command for operations twenty-two months after it had one officer and one warehouse** | `10-Q Q3-1999` l.824–828 | FACT (as disclosed; day not disclosed) | High (that it happened) / **UNKNOWN (the exact day; the reasoning)** |
| **1999-07** | **Toys and electronics launch (July 1999)** — the first two categories with **no** book-supply lineage and a wholesale inventory model; the FY1999 10-K's risk factors name **"non-uniform and heavy products"** as a fulfilment problem (l.1035) | `10-Q Q3-1999` l.798; `10-K/99` l.278–279, l.1035 | FACT | High → §P250 |
| **1999-07-21** | **Board approves the 2-for-1 split** (Q2-1999 10-Q: approved 1999-07-21, effective 1999-09-01, **"accordingly, the stock split has not been reflected"** in the Q2 statements) **and the same day an 8-K release claims "seven distribution centers nationwide… nearly 4 million square feet… more than 10 times the distribution center floor space the company had in 1998"** — a forward-looking count for the holiday season, while the Q3 10-Q that follows certifies **five** opened in the nine months | `10-Q Q2-1999` l.652–655; `8-K(1999-07-21)` l.311–317; `10-Q Q3-1999` l.830–833 | FACT (approval) + COMPANY CLAIM (count) | High (approval) / **Medium (the "seven")** → **U.151, U.128** |
| 1999-08-06 / 08-31 | **POS AM No. 2 raises the 333-55943 shelf to 30,000,000 shares; a POS AMI is filed 1999-08-31 whose EDGAR description ("POST EFFECTIVE AMENDMENT NO.1 TO FORM S-3") contradicts its own file number and quotes a share figure belonging to another file.** **The acquisition paper is enlarged twice in one month and the index cannot describe either filing correctly** | `POSAM_FileNo-333-55943_AmdtNo2`; `POSAMI_FileNo-333-55943_AmdtNo1` | FACT (filings) + FACT (index defect) | High → U.122 |
| **1999-08-12 / 08-16** | **Q2-1999 10-Q filed**: cumulative accounts **"including accounts with Amazon.com Auctions" reach 10.7 million** against 8.4m at March 31 — **the first time the company changes the composition of its own headline metric inside a reported series** | `10-Q Q2-1999` l.862 | FACT (company count, redefinition disclosed) | High → **U.139** |
| **1999-09 (month)** | **Warren C. Jenson named Senior VP and CFO** — the third finance chief of the company's public life and the end of Covey's tenure from December 1996; **the exact handover day appears nowhere** | `10-Q Q3-1999` l.825–826 | FACT (month) | High (that it happened) / **UNKNOWN (day, reason)** → §S |
| **late September 1999** | **zShops, Amazon.com Payments and All Products Search introduced** — "zShops, which enables anyone to offer merchandise for sale on Amazon.com"; the company **takes no possession, acts as no agent, and disclaims responsibility for delivery**. **The FY1999 launch table will date zShops to OCTOBER 1999 and the UK/German zShops to NOVEMBER, while the Q3 10-Q says the expansion to Germany and the UK happened in October** | `10-Q Q3-1999` l.801–812; `8-K(1999-10-28)` l.298; `10-K/99` l.277, l.280 | FACT (three company dates for two events) | High (each text) → **U.155 (new registration)** |
| **1999-09-01 / 08-12** | **2-for-1 split effected** (record 1999-08-12). **No Form 8-K announces it; the only filed records are a board approval in a 10-Q and a recital in a later 10-Q.** It is the instrument that doubles every option balance in the comparative columns (→ U.146) and completes the stage's **12×** cumulative factor (→ §P.2 t18) | `10-K/99` l.3823–3825; `10-Q Q2-1999` l.652–655 | FACT | High → U.128, U.146 |
| **1999-09-30** | **Nine-month state.** Five new DCs opened (Nevada, Georgia, **Kentucky**, Kansas, North Dakota) **and Kentucky also announced as a future site**; announced acquisitions in the period: **Exchange.com, Alexa Internet, Accept.com**; nine-month D&A **22,935**; accounts 13.1 million inclusive of Auctions. **The FY1999 10-K will later show TWO Kentucky sites opened (Campbellsville and Lexington), which is the only evidence in the corpus that resolves the double-listing** | `10-Q Q3-1999` l.820–833, l.871, l.314; `10-K/99` l.568–572 | FACT (as filed) | High → **U.117 (now strengthened: the two Kentucky sites are named in the later annual report)** |
| **1999-10-12 / 10-26 / 10-28** | **An S-8 for a new non-officer plan (10-12); a POS AMI to 333-65091 (10-26); the Q3-1999 results release (event 1999-10-28, press release dated **1999-10-27**) naming Media Metrix for September.** **The filing calendar in the fourth quarter is a register of capital-raising and employee-equity instruments, not of retail events** | `S-8_FileNo-333-88825`; `POSAMI_FileNo-333-65091_AmdtNo2`; `8-K(1999-10-28)` | FACT | High |
| **1999-11 / 1999-12** | **Home improvement (with a tool store), software, video games and sothebys.amazon.com all launch in November 1999** — four new objects in one month, one of them a branded auction house — **while Q4 depreciation is silently running at 13,871 thousand dollars, 1.47× the whole of FY1998** (§P242) | `10-K/99` l.281–284; `10-Q Q3-1999` l.814–816; §P.2 t17 | FACT (month) + DERIVED | High |
| **1999-12-31** | **STAGE-3 YEAR THREE / CANDIDATE ENDPOINT CLOSES.** Net sales **1,639,839**; gross margin **17.7%**; total opex **896,400** with **214,694 of goodwill amortisation**; loss from operations **(605,755)**; net loss **(719,968)**; LPS **(2.20)** on 326,753; D&A **36,806**; advertising **$140.9m**; fulfilment **$188.4m = 11.5% of net sales** — **rising, against the company's own stated expectation that it would fall**; long-term debt **1,466,338**; total assets **2,471,551**; equity **266,278**; **~7,600 full-time AND part-time employees** (widest basis of the three); **over 17 million accounts** (new basis); three named segments including **"Early-Stage Businesses and Other"**; **~430,000 Associates sites as of 2000-02-29**; **13 million titles** offered; six named acquisitions completed in the year on the purchase method | `10-K/99` l.198, l.220–226, l.305, l.1732–1785, l.1970–1972, l.3107–3109, l.3817–3825, l.4049, l.544; `10-K/A/99` l.173–226, l.1695–1699 | FACT (audited) + FACT (as disclosed) | High / **U.148, U.154, U.158, U.161 on the basis questions** |
| 2000-03-23 / **2000-09-08** | `(PB)` **The FY1999 10-K is filed 2000-03-23 (index date; its own header prints FILED AS OF DATE 2000-03-29 — two clocks, six days apart), and its amendment is filed 2000-09-08.** **The amendment is the stage's terminal document and is not a stage event: it restates the change in cash for EVERY year (+91,401→+61,726; +23,685→**(38,536)**; +1,012→+103,830) after a policy change effective 2000-04-01, and corrects transposed numbers in Note 9.** Both are used in this part and registered in §T | `10-K/99` SEC header; intake manifest addendum; `10-K/A/99` l.94–110, l.1338, l.1448–1456 | FACT (two audited printings of one instrument) | High → **U.154, U.166** |
| 2000-03 / 2000-02-29 | `(PB)` **UK and German DVD/video launch March 2000** (the launch table's own row) and **~430,000 Associates sites at 2000-02-29** — printed only to date the end of the series this part carries and to fix the Associates count's as-of date | `10-K/99` l.278, l.544 | FACT (post-boundary) | High (as 2000 facts) / excluded as Stage-3 findings |
| **UNKNOWN (in-window, undated)** | **No archived amazon.com page for 1997, 1998 or 1999 was retrieved by this pass, and the Wayback root capture sequence that Stage 2 documented is the same null.** **Consequence: nothing in this §Q's product rows can be checked against the storefront as customers saw it; every launch row rests on a filing sentence, not on an artifact** | `sources/NULL_RESULT_wayback_1995_1996.md`; Stage 2 §S row 2; §T | FACT (the documented null) / **UNANSWERED** for deep paths | High (homepage null) → U.103 (Stage 2) |
| UNKNOWN | **Day-level dates that no document carries: the music store (June 1998), the UK/German opening day (October 1998), Cards (April 1999), the Jenson handover (September 1999), the zShops day ("late September"), the Exchange.com closing minute, the contents of the 8-K/A's correction, the 540,000-share founder delta (Section 16 forms: zero rows in the enumerated slice).** Each is UNTRIED or EMPTY as named at §S, not resolved by tone | intake §§3, 7; `10-K/99` launch table; `10-Q Q3-1999` | UNKNOWN | High (that each is undated in the record) |

## R. END-OF-STAGE STRUCTURED SNAPSHOT (window 1997-05-16 → 1999-12-31)

**Geometry and conventions, per Stage 1 §R and Stage 2 §R (4-column form; the start→end pair carried inside Value so
no cell is lost).** **Start** = the position at 1997-05-16, whose anchors are Stage 2's closing rows (the 1996-12-31
audited column, the 1997-03-31 unaudited interim column, and the 424B1 cover). **End** = the position at 1999-12-31,
whose anchors are the FY1999 audited statements, the FY1999 launch table, the Q3-1999 10-Q and the FY1999 10-K/A.
`(PB)` marks a figure that post-dates the candidate boundary and is printed only to date an absence.
**This is a snapshot of what the company could prove about itself on the closing date, not a verdict on what it had
achieved**; no row argues from the 2000s outcome back to a 1997–99 decision (method §2).

| Variable | Value (Stage 3 start 1997-05-16 → Stage 3 end 1999-12-31) | Source | Confidence |
|---|---|---|---|
| Founders | **Start:** Bezos, CEO and Chairman, beneficial owner of ≈**41%** of the post-offering common (restated from 43% on 1997-05-14) plus ≈10% through family and controlled trusts → ≈51% of the vote; **salary $79,197 for 1997 as filed in the 1998 proxy, and $81,840 for 1998**, with **nil bonus, nil securities underlying options and nil all-other compensation in each of 1996, 1997 and 1998** — the founder's cash compensation stayed below four of his own officers' by 1998 (Dalzell $201,512, Aposporos $142,083, Spiegel $116,352, Risher $105,168). **End:** still CEO; **no longer sole operating chief** — Joseph Galli, Jr. is President and COO from June 1999 and is elected to the Board. **His personal guarantees for the merchant and card lines, dated November 1994 → December 1996, July 1995 and April 1995 in the S-1, are named in ZERO filings after 1997-05-15: the release is now UNKNOWN-with-the-searches-recorded, not untried, and the instruments were never filed so no further EDGAR request can reach them.** The founder's own equity movement across the stage is **unreconstructable**: the EDGAR slice covering 1997-03-24 → 2000-01-04 contains **no Form 3, 4 or 5 at all**, which is why the 540,000-share delta the finance dossier flags has no filed explanation. Two Schedule 13G filings (1998-02-13, 1998-02-17) are the only in-window statements of who held what | `10-K405/97`; `DEF14A/98`, `DEF14A/99`; `SC13G(1998-02-13/17)`; intake §3(b), §7(3); Stage 2 §P146 `(L)` | High (filed acts and salaries); **UNKNOWN (guarantee release, share transactions, motive at every point)** → U.167, §S |
| Employees | **Three filed bases, side by side and never blended, because each is a different population:** **614 "full-time employees"** at 1997-12-31 (`10-K405/97` l.516) · **approximately 2,100 "employees"**, unqualified, at 1998-12-31 (`10-K/98` l.528; `ARS/98` says "over 2,100", and the same ARS renders the **1997 opening as "approximately 600"**, a fourth figure for a date with a filed 614) · **approximately 7,600 "full-time and part-time employees"** at 1999-12-31 (`10-K/99` l.684) with independent contractors named but unnumbered. **The bases are not comparable and this part therefore computes no per-employee figure at all** (§P.2 "Not computed" (i)): the FY1999 figure is the **widest** basis of the three, so the apparent 12.4× growth from 614 is an **upper bound contaminated by definition**, not a headcount multiple — `614 → ~2,100` is 3.4× on the two narrower bases, and the FY1999 sentence would be smaller on the FY1997 definition. **Value corrected on this pass:** the instruction layer called the FY1999 figure "7,600 full-time"; the filing says "full-time **and part-time**" (§P.2a). Composition disclosed as absence at every date: no function split, no engineering-team size, no dated org chart, no contractor count, no turnover. Officers: seven named executive officers in the FY1998 10-K **while the 1999 proxy pays an eighth under a title given to one of the seven** (U.119), and a CFO change (Covey → Jenson) whose day appears nowhere | `10-K405/97` l.516, l.729; `10-K/98` l.528; `10-K/99` l.684–685; `ARS/98` l.157; `10-K/98` l.940–955; `DEF14A/99` l.617–619 | High (each figure as stated); **Medium and unresolvable (any cross-year comparison)**; **UNKNOWN (composition, contractor pool, day of the CFO change)** → U.118, U.119, U.161 |
| Product | **Start:** one store, "primarily books but also a small number of CDs, videotapes, audiotapes and other products", >2.5 million titles, an out-of-print promise of two-to-six months, no marketplace, no foreign site, no greeting cards, no toys, no payments. **End, from the company's own dated launch table:** books July 1995 · music **June 1998** · DVD/video **November 1998** · **Auctions March 1999** · toys and electronics **July 1999** · **zShops October 1999** (but "late September 1999" in the Q3 10-Q and its own release) · home improvement, software, video games and sothebys.amazon.com **November 1999** · plus **Cards April 1999**, **Payments and All Products Search late September 1999**, **Anywhere October 1999**; internationally, UK/German books **October 1998**, music **October 1999**, auctions and zShops **November 1999**. **13 million titles** offered at the FY1999 filing (against 4.7m in FY1998 and 2.5m in FY1997 — three different objects, U.141). **Three segments** reported for the first time, one named **"Early-Stage Businesses and Other"**. **What the table cannot say:** the day of any launch except video (1998-11-17, from a release the table does not cite, U.162); whether Cards preceded its own named launch (U.142); what any customer actually saw, because **no archived page exists for any year of the stage** | `10-K/99` l.274–285, l.305, l.220–226; `10-Q Q3-1999` l.795–816; `8-K(1999-01-26)` l.306; `10-K/98` l.214 | High (as disclosed); **UNKNOWN (day for every launch but video; visible site state at any date)** → U.141, U.142, U.155, U.162, U.103 (Stage 2) |
| Marketplace (new object) | **Absent at the start; the stage's central structural change.** Auctions 1999-03-30, zShops September/October 1999, sothebys.amazon.com November 1999, and from 1999 the **net-sales line itself includes** "sales commissions, placement fees and fees" from zShops and Auctions transactions — **one merged revenue caption with no split ever filed**. **The company's own position on what it is not:** it does not take possession, does not act as agent, and **disclaims responsibility for delivery of goods**, with risk factors that users "may not complete transactions" and that consumer-to-consumer fixed-price markets may be regulated where auctions are not. **No GMV, no order count, no listing count, no take rate, no seller count at any date.** The 1999-03-11 "Sales Agreements" in the Q1-1999 10-Q, which a working paper read as the merchant contracts, are five agreements with **one** counterparty, The Buschman Company, with confidentially treated terms — **the marketplace's contractual trace is NOT in the filings** (U.114, U.152). **The five 1999 acquisitions on the purchase method, priced substantially all in goodwill amortised over ~3 years ($145m Exchange.com, $189m Accept.com, $40m LiveBid, Alexa, Back to Basics, Tool Crib), are how capability arrived rather than how it was built — and $2.8m of it was written off on arrival as in-process R&D that had no established technological feasibility and no alternative future use** | `10-K/99` l.287–295, l.1307–1317; `10-K/A/99` l.292, l.1695–1760; `10-Q Q1-1999` l.1660–1669; `8-K(1999-03-30)` | High (the disclaimers, the note, the exhibits); **UNKNOWN (every marketplace quantity)** → U.114, U.152, U.156, U.165 |
| Technology | **Start:** the Stage-2 architecture unchanged — no redundancy, no disaster-recovery plan, acknowledged continuing outages, transaction system **not integrated** with the accounting system. **End:** a named-and-numbered expense caption the company had never filed before — **"Technology and content"** **13,384 (1997, recast) → 46,424 (1998) → 159,722 (1999)**, i.e. **9.7% → 14.6% → 9.7% of net sales**; equipment and software financed under GE Capital leases from 1997-02-12 (Stage 2 §P148) and gross fixed assets **12,899 → 43,585 → (the FY1999 build-out is visible in §P242's 13,871 thousand of Q4-1999 depreciation alone)**; **1999's own segment note and the acquisition notes bring in bought technology rather than built technology** (e-Niche/Exchange.com "a developer of Internet marketplaces and related online communities"; LiveBid "a technology provider for live, event-based auctions"; Accept.com payment technology), and **the in-process R&D write-off is the filed admission that part of it was not yet usable**. The stack itself remains **UNKNOWN at every date**: no language, database or server is filed, and the 1-Click patent (US 5,999,911, mentioned in Stage 1–2 gaps) was not searched in this pass | `10-K/99` l.1738, l.1970–1972; `10-K/98` l.1228; `10-K/A/99` l.1695–1760; §P.2 t2, t17 | High (caption dollars and the ratios derived from them); **UNKNOWN (the acquisition/expense split behind 13,384; the stack; every outage)** → U.150, U.158, U.145, U.104 (Stage 2) |
| Supply | **Start:** two distributors, no contracts, no guaranteed availability. **End:** **three wholesalers** (Ingram, Baker & Taylor, **Valley Media**, added 1998), direct purchasing from manufacturers and labels, own inventory rising with the categories, and **Ingram's share of purchases falling from 58% to ~40% — while Barnes & Noble announced in late 1998 that it would buy Ingram**, disclosed by Amazon as a risk factor. **The single-sentence differential that carries the whole question:** "no long-term contracts or arrangements with **any** of its vendors" (FY1997) becomes "with **most** of our vendors" (FY1998) — something became contractual, and **no agreement is filed** (U.144). **No purchase total is filed in any year, so no Ingram dollar volume exists** (§P.2 "Not computed" (vi)) | `10-K405/97` l.1669–1673; `10-K/98` l.420–423, l.504, l.797–799, l.2374–2377; `10-K/99` l.1198 | High (concentration, the differential, the B&N/Ingram fact as disclosed by Amazon); **UNKNOWN (terms, which vendor contracted, purchase total)** → U.135, U.144, U.66/U.80 (Stage 2) |
| Customers | **Start:** ≈340,000 cumulative accounts at 1997-03-31 (Stage 2 §P153), repeat >40% of orders on the 1996 basis. **End:** **over 17 million accounts in over 150 countries** — **on a basis the company changed mid-series**: 10.7m (June 1999) and 13.1m (September 1999) are expressly "including accounts with Amazon.com Auctions", and the FY1998 6.2m is not, so **no subtraction across the 1998/1999 boundary is valid** (U.139). Repeat: **>46% (Q4-1996) → >58% (Q4-1997) → over 62% (H1-1998) → over 60% (FY1998) → >40% (the S-1's 1996 cumulative wording)** — **six values on at least four bases, and the only matched pair the company itself prints is the Q4-to-Q4 one** (U.140). **Total orders, average order value, units per order, fill and back-order rates, returns and chargebacks: UNKNOWN at every date in the stage**, exactly as in Stages 1 and 2; the company never disclosed them and no proxy is substituted (§P263) | `10-K/99` l.198; `10-Q Q2-1999` l.862; `10-Q Q3-1999` l.871; `10-K/98` l.1317–1320; `424B2/98` l.396–400; `ARS/97` l.210 | High (each as stated, per document); **Low (across a basis change)**; **UNKNOWN (all unit economics)** → U.127, U.139, U.140 |
| Distribution / estate | **Start:** ~92,400 sq ft, **all of it Seattle**, one warehouse through which all sales were processed, no redundancy. **End:** the FY1999 10-K describes **eight new distribution centres comprising approximately four million square feet** (Item 1 narrative, six US sites named: Fernley NV, Coffeyville KS, Campbellsville KY, Lexington KY, McDonough GA, Grand Forks ND, plus UK and Germany) **and eight US distribution centres comprising approximately 3.8 million square feet** (Item 2 schedule, the US estate including Seattle and New Castle DE) — **two different "eights", which must never be summed** (U.148); the first foreign sites were leased in 1998 (`ARS/98` l.160: "We opened distribution and customer service centers in the U.K. and Germany"); lease commitments reach **$134,829 thousand of total minimum lease payments** (`10-K/98` l.2853, a single undifferentiated column), against $4,323 thousand at 1996-12-31 (Stage 2 §P150) — **a 31× rise in forward lease commitments in two years** (§P.2 t28). **The claim/count gap is the finding: the July 1999 release promised "seven distribution centers nationwide… more than 10 times the floor space the company had in 1998" while the Q3 10-Q certified only five opened in nine months, with Kentucky in both the opened and the announced lists** (U.151, U.117) | `10-K/99` l.568–578, l.1600–1610; `ARS/98` l.160; `10-K/98` l.2853; `8-K(1999-07-21)` l.311–317; `10-Q Q3-1999` l.830–833; `10-Q Q1-1999` l.592, l.915 | High (the filed estate); **Medium (the "seven")**; **UNKNOWN (square footage of pre-1999 sites inside the "new" total; lease cost per site)** → U.148, U.151, U.117 |
| Revenue | **Start:** FY1996 **15,746** audited (restated to the same figure in every comparative column — the one line that never moves). **End:** FY1999 **1,639,839**, i.e. **104.1× FY1996** (§P.2 t29), passing **147,758/147,787** (FY1997) and **609,996/609,819** (FY1998). **Basis discipline:** shipment-basis net sales inclusive of outbound shipping and handling, and from 1999 **including marketplace transaction fees**, which makes FY1999's line a different object from FY1997's (U.160). **Two of the three annual figures have two audited printings and no reconciling note** (U.136, U.149). Cumulative-since-inception "more than $164 million through December 31, 1997" is a **cumulative** figure and is not a 1997 revenue (U.124) | the Item 6 and MD&A tables named at §P184–P237 | **High** (audited) / **High (that the series is not single-valued)** |
| GMV / take rate | **Start and end: UNKNOWN, and now for a different reason.** In Stage 1–2 the null was simple: no GMV line existed. From 1999 the company **does** earn marketplace fees, but it files them **inside net sales**, so GMV is not merely undisclosed — **the observable is merged into a caption that cannot be decomposed** (`10-K/A/99` l.292). **No take rate, no listings, no seller count, no gross-merchandise figure exists at any date, and none is estimated here** | `10-K/A/99` l.292; documented nulls across §P263–P264 | **High (of the null and of its cause)** |
| Margins | **Start:** FY1996 gross **22.0%** (exact 21.97). **End:** FY1999 **17.7%**, via **19.5% (FY1997) and 21.9% (FY1998)** — **the company's own renderings for the first three, ours for the last two** (§P.2 t25). **The shape is not monotone and that is the finding:** margin **rose** 2.4 points in FY1998 while the mix moved to lower-margin categories, then **fell 4.2 points in FY1999**. Operating loss as a share of gross profit: **113.1% (FY1997, restated) → 81.6% (FY1998) → 208.4% (FY1999)**, and **134.5% for FY1999 if the non-cash goodwill charge is removed** (§P.2 t26 — the removal is shown because the charge is 73.9% of gross profit and a reader comparing 208.4% with 81.6% is comparing two different things). **Marketing plus fulfilment economics: fulfilment was inside marketing until the FY1999 note separated it retrospectively** (§P215) | §P188, §P211, §P237, §P265, §P.2 t1/t7/t14/t25/t26 | **High** (all inputs audited) / Medium (that any single ratio is the right lens — which is why each is printed with its basis) |
| Capital | **Start:** $49.4m of IPO proceeds just received; equity $2,763k at 1997-03-31; working capital $79k at the same date (Stage 2 §P81, §P139). **Through the stage, in filed order:** **$75m Deutsche Bank senior secured term facility (1997-11-07, drawn 1997-12-23)** → **$275m of 10% Senior Discount Notes announced 1998-04-24, upsized 1998-05-05, ~$326m gross** → **S-3 shelf 333-65091 (1998-09-30)** → **S-3 shelf 333-74435 (1999-03-16)** → **$500m ask (1999-01-28) → $1.25bn 4¾% convertible notes closed 1999-02-03** → **universal shelf 333-78797 (1999-05-19) and $2bn shelf** → **S-4 shelves raised 5m → 15m → 30m shares (1998-06-03 → 1999-04-26 → 1999-08-06)** → **424B3 resale of 2,662,125 shares (1998-10-22) and 33 further resale supplements in 1999 (not fetched)**. **End:** long-term debt **1,466,338**, total assets **2,471,551**, equity **266,278**, working capital **273,243**, marketable securities **589,226** (or **572,879** plus **133,309** of "cash and cash equivalents" on the amended basis, U.154). **Stock issued for acquisitions: 217,241 (1998) and 774,409 (1999) thousand dollars — the expansion was substantially paid in paper, and the cash-flow statement says so in a line the income statement does not have** (§P268) | the filings named above; `10-K/99` l.2860–2875; intake §9(1) | High (filed aggregates, dates, terms); **UNKNOWN (whether any over-allotment or earn-out was taken: Exchange.com's earn-out of up to $27.5m in additional shares is disclosed but its outcome is not)** |
| Valuation | **Start:** one true number, the post-IPO market capitalisation of ≈**$428 million** at $18.00 (Stage 2 §P99, printed as an arithmetic identity only). **End: no whole-company valuation is asserted here, and none is derivable without a share price this corpus does not contain.** What is filed: **marketable securities 589,226** and **debt 1,466,338** at 1999-12-31; purchase prices for six acquisitions ($145m, $189m, $40m, and the rest unnamed or unallocated in the text read); **~$2.8m of in-process R&D written off**; **214,694 of goodwill amortisation**; and an internally stale share-basis note ("18 million" IPO shares, "36" conversion ratio) that contradicts its own split list (§P.2 t18 → U.157). **No pre-IPO holder's percentage, no multiple of any earlier round, and no return to anyone is computed — hindsight firewall** | `10-K/99` l.1779–1785; `10-K/A/99` l.1695–1760, l.2307–2317 | High (the filed cells); **UNKNOWN (every whole-company valuation)** → U.157 |
| Competitors | **Start:** B&N, Borders, Simon & Schuster, Book Stacks, and "barriers to entry are minimal" (the registrant's own sentence). **End, from this stage's filings:** the FY1997 10-K names Ingram and B&T as the chokepoint and repeats that distributors may arm entrants; the FY1998 10-K names **three** vendors and discloses **"Barnes & Noble announced its pending acquisition of Ingram"** as a risk; the FY1998 and FY1999 risk factors name **online music retailers** and, by 1999, **the marketplace's own regulatory asymmetry** (fixed-price consumer-to-consumer markets may be regulated where auctions are not). **The incumbent's threat was measured in the stage by something other than rivalry: Amazon's largest supplier was about to be bought by its largest competitor, and the company printed that fact as a vulnerability rather than as a headline** | `10-K405/97` l.1669–1675, l.2136; `10-K/98` l.504, l.665, l.797–799; `10-K/99` l.1198, l.1266 | High (each as filed); **UNKNOWN (B&N/Ingram outcome inside the window on this record; competitor volumes; the disposition of the 1997-05-12 B&N suit, which is still absent from these filings)** → U.68 (Stage 2) |
| Geography | **Start:** one city. **End:** **corporate offices at 1200 12th Avenue South, Seattle**; US distribution in **Seattle, New Castle DE, Fernley NV, Coffeyville KS, Campbellsville KY, Lexington KY, McDonough GA, Grand Forks ND**; **Amazon.co.uk and Amazon.de selling**, with UK and German distribution and customer-service centres opened in 1998 and expanded 1999-10/11; **"over 150 countries"** served — **cumulative reach from operated sites, not a count of entities or facilities**. Two internationally focused Web sites and three reportable segments including "International (Germany and the UK)" | `10-K/99` cover l.47–49, l.1600–1610, l.204–205, l.198, l.220–226; `ARS/98` l.160; `10-K/98` | High |
| Organisational structure | **Start:** ten named officers and directors, nine arrived within the preceding year (Stage 2 §P170). **End:** an operating hierarchy with a **President and COO** (Galli, June 1999, also to the Board) and a **new CFO** (Jenson, September 1999) above a finance function that had been through Covey since December 1996; **a proxy-compensated officer set that does not match the annual report's executive-officer list** (U.119); officer start dates recoverable only from **proxy footnotes, not from caches** — the four dated arrivals are Aposporos 1997-05-09, Dalzell 1997-09-02, Duenas 1997-01-08, Spiegel 1997-03-17 (1998 proxy) and Risher 1997-01-31, Wright 1998-07-27 (1999 proxy), with **Kaphan undated because he had been VP of R&D since October 1994** (U.115). **The equity plan expands continuously and is the clearest structural record of the hiring curve: eight S-8 registrations and two S-8 POS between 1997-06-06 and 1999-10-12, three of them for acquired companies' plans** | `10-Q Q3-1999` l.824–828; `DEF14A/98` l.598–616; `DEF14A/99` l.617–627; `10-K/98` l.940–955; the S-8 set | High (the named acts and dates); **UNKNOWN (report lines, committee timing, why any change was made, the day of the CFO change)** → U.115, U.119 |
| Risks as the company disclosed them, in-period | Named in this stage's own filings and therefore the register the company was obliged to hold open: **anticipated losses**; **"relatively low product gross margins"**; **capacity constraints** and the DC build-out's lease and inventory commitments; **dependence on three wholesalers with no contracts**, one of them being bought by the largest competitor; **fulfilment and order-processing classification risk** — the FY1999 filing discloses that accounting standard-setters could require fulfilment costs to be **classified as cost of sales or capitalised in inventory**, which would change the reported margin, and says "we will adjust our accounting"; **liability and non-completion risk in auctions and zShops**; **regulation of fixed-price consumer-to-consumer markets**; **currency exposure after the February 2000 notes**; **acquisition integration and goodwill**; **the availability of the acquired technology** (the IPR&D write-off is the disclosure of this risk already having occurred). **And the disclosure act the stage must not launder: the FY1997 report deleted the sales-tax risk factor in the same year it opened a Delaware centre** (Stage 2 §P172 → U.71) | `10-K405/97` l.380–860 area; `10-K/98` l.488–713; `10-K/99` l.1032–1035, l.1266, l.1307–1317, l.1938–1947; `10-K/A/99` l.267, l.381–388 | High (the disclosures); **none (the motive for any retirement or addition)** → U.71 (Stage 2), U.165 |
| Weaknesses evidenced, not hindsight | **Eleven, each with its filed number or sentence.** (1) **The unit economics are still invisible**: no order count in any year of the stage, so the growth story cannot be decomposed at unit level (Stage 2's null persisted). (2) **Gross margin fell to 17.7% while the marketing ratio fell** — the company bought growth with price, not with cost (§P.2 t6, t25). (3) **Fulfilment costs rose as a share of sales (8.25% → 11.5%) against the company's own stated expectation that they would fall** (§P241 → the §M layer). (4) **Net loss per dollar of gross profit was 208.4% in FY1999** — 134.5% even after removing the non-cash charge (§P.2 t26). (5) **Two audited printings disagree on FY1997 net loss by $3,430k, on FY1998 net sales by $177k, on FY1997 gross fixed assets by $591k gross, and on FY1997/FY1998 depreciation by $54k and $271k — with no reconciling note in any of them** (U.125, U.145, U.147, U.149). (6) **The headline customer metric was redefined in the middle of the series** (U.139). (7) **The marketplace's economics are undisclosed by construction**: fees merged into net sales, no GMV, no take rate, and the company disclaims the delivery performance that a retailer's margin implies (§P270). (8) **Capability was bought faster than it was absorbed** — six purchase-method acquisitions in 1999, substantially all price allocated to goodwill amortised over ~3 years, and $2.8m of in-process R&D written off on arrival (U.165). (9) **The estate count was overstated in a public release relative to what the interim report certified** (U.151). (10) **Vendor contractual terms improved by wording, not by filing**: "any" became "most", and no agreement is on the record (U.144). (11) **The founder's own equity history is unreconstructable because Section 16 filings are absent from the record** — a governance-evidence gap, not a disclosure failure the company committed on paper but a real limit on what this stage can prove about control | §P.2 t1–t29 and the U-rows named | **High** — every item is a filed number, a filed sentence, or a documented absence |
| Unknowns what this stage cannot answer, as findings | **Money:** no order count, no AOV, no units per order, no fill/back-order/returns/chargeback rate, no GMV, no take rate; the reconciling detail behind every restatement pair; the composition of the FY1997 technology carve-out; the identity and terms of the vendor that became contractual. **Programmes:** the Associates commission rate, payout total and attributable revenue (a **count-only disclosure at four dates**); each portal's spend, start and result; Cards' true start; the auction/zShops volume. **Operations:** square footage and cost of pre-1999 sites inside the "new" totals; lease cost per site; every outage; the fulfilment-capacity numbers behind the "10 times" claim. **Organisation:** the CFO handover day; the contractor pool; headcount by function; why Galli was hired when he was. **Law and register:** whether Bezos's guarantees were released (never filed, so unretrievable from EDGAR); Section 16 transactions (zero forms in the slice); the contents of the 1998-11-30 and 1999-07-20 SC 13Ds (not fetched); the 8-K/A's corrected substance; the disposition of the 1997 B&N action. **Artifact:** every page, price and availability display the site showed at any date in the stage | full §S register, this file; §P263–P264; intake §§3, 5, 7 | **UNKNOWN is the finding, and the list is this section's output** → §S |
| Current strategy (in-period, as stated) | **Start:** maintain and grow the customer base, expand selection, offer attractive pricing "which will reduce its gross margins", and "**the Company may choose to expand its product offerings**" (Stage 2 §P144/§R). **End, in the company's own filed words:** the strategy has become **category breadth, marketplace services, geographic sites and acquired capability**, disclosed as an operating policy rather than an option — "We expect that we will continue to expand our business through acquisitions" (`10-K/A/99` l.559), and the segment frame names "Early-Stage Businesses and Other" as a permanent object. **What the filings never do is attribute revenue to a channel:** the growth sentence stays the Stage-2 sentence ("the growth of the Company's customer base and repeat purchases", `10-K/98` l.1315–1316), so **no §R row here claims any channel produced any revenue** (Stage 2 U.72 persists) | `10-K/98` l.1315; `10-K/99` l.287–295, l.559; `ARS/98`, `ARS/97` shareholder letters | High (that filed); **UNKNOWN (deliberation — no plan document survives)** → U.72 (Stage 2) |
| Current objective (in-period, as evidenced) | **Start:** the registration was the objective, and the Series A conversion trigger fixed its minimum size (Stage 2 §R). **End:** the objective the artefacts evidence is **capacity and capital**: thirty-plus filings in the window are debt shelves, resale prospectuses and option-plan registrations; the $1.25bn convert (1999-02-03) and the 4 million sq ft build (1999) are the two largest single acts, and the FY1999 10-K's own sentence names the purpose — the new DCs "give us more control over the distribution process and facilitate our ability to deliver merchandise to customers on a reliable and timely basis" (l.576–578). **No quantified internal target surfaced for any date in this stage.** The holiday-season capacity claim of July 1999 ("seven… nearly 4 million square feet… 10 times") is the closest thing to a public objective, and it is a **company claim against a certified count of five** (§P255) | `10-K/99` l.568–578; the 8-K/S-3/S-4/S-8 set; `8-K(1999-07-21)` | High (the filed sequence); **High (that capacity was the objective, as a reading of what the money and the filings were for)**; **UNKNOWN (any internal number, authorship, deliberation)** → U.151, U.153 |

## S. DATA GAPS

**Three states kept distinct throughout, and never collapsed into one another (method §12, §14 rules 3, 4, 6 and 11).**
**EMPTY** = the record contains nothing on the question and no document was found that could hold it.
**UNANSWERED** = a retrieval was attempted against this corpus or archive and failed, timed out, or returned a non-null
that does not settle the question — **a 504 or a 503 is a failure, not a null.**
**UNTRIED** = a named retrieval has not been attempted by any agent in this stage, and its exact query is printed so
the next pass can run it without re-deriving the need.
**No row below may be reported as "the evidence does not exist" unless it is marked EMPTY, and only EMPTY rows survive
as findings about the record.** **§S rows are numbered 1–22 in the print order below, and every "§S row n"
cross-reference in §P, §Q, §R, §T, §U and the append blocks means those numbers.** This part made **zero web requests**: every figure above traces to a local path under
`sources/`, and every UNTRIED row carries the query that was never sent (method §14 rule 1's mining-only condition).

| Data Gap | Why Missing | Importance | Best Available Evidence | Confidence |
|---|---|---|---|---|
| **Record-selection null: what is unrecoverable because the survivor's archive is the one that was kept** — the deliberations behind the 1998–99 category and acquisition decisions, the options rejected before they were rejected, the experiments abandoned without a filing, and the absence of any independent count behind every company self-report in §P | Not a retrieval failure. This stage's archive is dense precisely because the company was raising money: 125 EDGAR rows in 1997-03-24 → 2000-01-04, of which the shelf and note filings dominate the calendar. Failed 1998 entrants left no S-4, no indenture and no risk factors. The risk factors here were drafted for liability, not history | **Very High** — it bounds every cross-company use of this stage and is the reason §M is not a base rate | Stage 2 §S row 1; method §2 "Record-selection null"; `STAGE3_INTAKE_MANIFEST.md` §1 composition table; §R Current strategy | **High** (that the selection operates); **UNKNOWN** (what the lost record would have shown) |
| **Every marketplace quantity: GMV, order and listing counts, seller counts, take rate, revenue attributable to Auctions/zShops/sothebys** | **EMPTY.** From 1999 the company's net sales **include** "sales commissions, placement fees and fees" from these transactions **inside one merged line** (`10-K/A/99` l.292); no accession in the stage decomposes it, and none discloses a volume | **Very High** — the stage's structural change is its least measured part; §P263, §P264 and the "Not computed" list (iii) exist because of this row | `10-K/A/99` l.292; `10-K/99` l.287–295, l.1307–1317; §P249, §R Marketplace | **High** (that nothing is disclosed); **UNKNOWN** (every quantity) |
| **Order count, average order value, units per order, fill/back-order/returns/chargeback rates, realised discount, cost per shipment** — the entire unit-economics layer, for the third stage running | **EMPTY.** Never disclosed in any accession in any year. The company declined order figures to press in 1996 (Stage 2 §S) and never began filing them | **Very High** — no repeatability question at unit level is answerable from the primary record at any date in the company's public life to 1999 | Stage 2 §P181, §S row 6; §P263–P264; `10-K/98` l.1315–1316 | **High** (that they are unrecoverable on this record); **UNKNOWN** (all) |
| **Associates Program: commission rate, payout total, attributable revenue or orders, and the programme's exact start** | **EMPTY as to economics.** Enrolment is filed at four dates (4,800+ 1996-12-31 · >140,000 1998-09 · ~200,000 1998-12-31 · ~430,000 2000-02-29) and **no rate, expense or revenue appears anywhere in the FY1997–FY1999 corpus**; the start date remains undated in any filing (Stage 2 U.112) | **Very High** — the company's signature distribution innovation is disclosed only as a count, across the very years its reach grew most | `8-K(1998-10-28)` l.296; `10-K/98` l.383–386; `10-K/99` l.542–545; Stage 2 §P90, §P162, U.112, U.48 | **High** (the counts) / **UNKNOWN** (every effect) — **UNTRIED**: `Amazon.com "associates" commission rate 1998 site:web.archive.org OR site:prnewswire.com`; the prosecution history of **US 5,999,911** (never searched in any stage) |
| **The reconciling detail behind every restatement pair: FY1997 net loss (27,590)→(31,020); FY1997/FY1998 depreciation; FY1997 gross fixed assets 12,899→13,490; FY1998 net sales 609,996→609,819; the FY1996 expense and equity recasts** | **EMPTY by the filings' own construction:** the FY1998 and FY1999 Item 6 tables carry the single footnote "Reflects restatement for pooling of interests. See Notes 1 and 2", and Notes 1–2 describe the **method**, not the amounts line by line. No company reconciliation was ever printed | **Very High** — this is why §P prints pairs instead of values, and why U.125, U.136, U.145, U.147, U.149, U.150, U.158 and U.159 exist as separate rows | `10-K/98` l.1269; `10-K/99` l.1788; `10-K/A/99` l.231; §P.2 t1, t2b, t4, t5, t7, t21, t22 | **High** (that no note itemises); **UNKNOWN** (composition of every difference) |
| **Which vendor became contractual between March 1998 and March 1999, and on what terms** | **EMPTY as to any filed agreement.** The wording differential is certain ("any" → "most") and **no distribution or supply agreement is filed as an exhibit in any year of the stage** | **Very High** — supply terms are the COGS leg of every unit claim this dataset cannot make | `10-K405/97` l.1671–1673; `10-K/98` MD&A; §P230, U.144 | **High** (the differential); **UNKNOWN** (vendor, terms, date) — **UNTRIED**: `EDGAR CIK 1018724 exhibit "supply agreement" OR "distribution agreement" 1998 OR 1999`; the SEC paper file for File No. 333-55943 |
| **Section 16 filings (Forms 3, 4, 5) for 1997–1999 — the founder's and officers' own transactions** | **UNTRIED, with a documented prior null:** the enumerated slice `-002` (125 rows, 1997-03-24 → 2000-01-04) contains **no Form 3/4/5 at all**, and the `-001` slice (2000-01-06 → 2020-09-28) **has not been re-checked for them**. The untested route is `-001`'s form list, not a re-query of `-002` | **Very High** — the 540,000-share founder delta has no filed explanation without them, and control percentages in §R cannot be moved from proxy snapshots to transactions | `STAGE3_INTAKE_MANIFEST.md` §7(3); `SC13G(1998-02-13/17)`; `DEF14A/98`, `/99` beneficial ownership | **UNKNOWN** (the transactions); **High** (that `-002` holds none) — **UNTRIED**: `https://data.sec.gov/submissions/CIK0001018724-submissions-001.json` filtered to form ∈ {3,4,5}, then `/Archives/edgar/data/1018724/<dashed-accession>.txt` |
| **Bezos's personal guarantees: amounts, and whether released** | **UNRETRIEVABLE FROM EDGAR, now demonstrated.** The Seafirst merchant account, the Wells Fargo card account and the company-card guarantees were **never filed**; zero post-1997-05-15 filings mention them; the only bank-facing exhibit is the **Subrogation Agreement** (Bezos's recourse against Amazon, EX-10.27) | **High** — it is the founder-state question the whole stage turns on, and more requests cannot help | intake §3(b), §7(2); `S-1 (orig.)` EX-10.27 l.18487–18622; Stage 2 §P, U.82 | **High** (existence and dates); **UNKNOWN** (amounts, release). **Non-EDGAR routes only**: bank records, the SEC paper original/microfilm of File 333-23795 |
| **The day-level date of every launch except video (1998-11-17): music June 1998, UK/German stores October 1998, Cards April 1999, zShops "late September 1999", Payments and All Products Search, Anywhere October 1999, the four November 1999 stores** | The company's own launch table goes to the **month** (`10-K/99` l.274–285). No filing dates a day. **The press-archive releases that would carry days were not retrieved in this pass** | **High** — §Q's precision ceiling is the month, and the one day-dated row (video) comes from a release the tables do not cite (U.162) | `10-K/99` l.274–285; `10-Q Q3-1999` l.795–816; `8-K(1999-01-26)` l.306; `8-K(1999-10-28)` l.298 | **UNKNOWN** (days) — **UNTRIED**: enumerate the company press-release index by month for 1998-06, 1998-10, 1999-04, 1999-09 before requesting any item URL (Stage 2's §S records two 404s from guessed URLs) |
| **zShops: late September or October 1999** | **UNANSWERED, not EMPTY — three company documents give two different answers for two different events** (`10-Q Q3-1999` l.801 "late September"; `8-K(1999-10-28)` l.298 "late September"; `10-K/99` l.280 "October", with the same table dating UK/German zShops to November while the Q3 10-Q says October). The intake's own 8-K list contains no zShops launch item | **High** — it is the stage's flagship marketplace launch and its date is registered at **U.155** precisely because the record does not agree | the three lines named; §P248 | **Medium** (that the US launch was late September, two contemporaneous documents) / **High** (that the annual table says October) — **UNTRIED**: `"zShops" launch September 1999 site:prnewswire.com OR site:businesswire.com`; CDX for `amazon.com/zshops` 1999-09/10 |
| **Whether WarehouseDirect.com, Internet Mail (and Allaire Software) were acquisitions inside the window** | **EMPTY in this corpus, and the emptiness is the answer for the window:** `WarehouseDirect`, `Allaire`, `Internet Mail` return **zero occurrences across every file in `sources/`**, while the FY1999 10-K/A Note 2 names six completed 1999 acquisitions with dates, share counts and prices. Anything about the other three comes from **outside** the filed record | **High** — registered as a conflict at **U.156** so no dossier can import them as Stage-3 events | `10-K/A/99` l.1695–1699; string-counted nulls; §P251 | **High** (that the filed list excludes them); **UNKNOWN** (their status outside the record) → **UNTRIED**: `Amazon.com acquires (WarehouseDirect OR Allaire OR "Internet Mail") 1999 OR 2000 (site:sec.gov OR site:latimes.com)` — a 2000 answer would move them out of Stage 3, which is itself the finding |
| **The 35 un-fetched Form 424B3 resale supplements of 1999 and the two November 1998** | **UNTRIED by explicit editorial choice, recorded as such** (intake §5a): one-to-two-page prospectus supplements that incorporate the periodic filings by reference, so under §3 they cannot corroborate anything the 10-Qs already say. **Accessions, filed dates and byte sizes are all in the intake's enumeration** | **Medium-High** — *the update cadence itself is a fact*: 33 supplements in seven months is evidence about resale activity that no other document in the corpus gives | intake §5a (all 35 accession tails listed); `424B3/98` and its supplement (the two substantial ones, fetched) | **UNTRIED — not EMPTY, not UNANSWERED.** Recipe in intake §6; fetch a **sample by date**, not all 35 |
| **The 1998-11-30 and 1999-07-20 Schedule 13Ds, and seven further third-party Schedule 13 filings** | **UNTRIED** (intake §5b). A 13D asserts control intent where a 13G disclaims it, so these are the ones to revisit first if a specific strategic holder becomes a question; **filer identity is not in the index description, so it takes a fetch to name them** | **Medium-High** | intake §5b (10 accessions listed with form and date) | **UNTRIED** — `https://www.sec.gov/Archives/edgar/data/1018724/0000891020-98-001712.txt` and `…/0000891020-99-001210.txt` |
| **What the Form 8-K/A of 1998-10-26 corrected** (event 1998-08-12) | **UNANSWERED.** The amendment exists on disk; its body does not state a reason, and the original 8-K of the same event is also local — **the pair was not diffed in this pass** | **Medium-High** — an amended current report is a filed correction, and an unexplained one in a financing week is worth diffing | `8-KA_event-1998-08-12` (acc. 0000891020-98-001491); `8-K_event-1998-08-12` (acc. …-001352) | **High** (both documents exist locally) / **UNKNOWN** (the substance) — **UNTRIED locally**: diff the two bodies' Item 1/2 text and the exhibit lists; no web request needed |
| **Square footage and lease cost of the pre-1999 sites inside the "new" totals; cost per square foot of the 1999 build-out** | **EMPTY as to a schedule.** The FY1999 10-K gives two mutually exclusive "eights" (U.148) and the lease footnote gives **one undifferentiated column** of total minimum lease payments (`10-K/98` l.2853, $134,829) | **High** — the estate row in §R is a count and a claim, not a cost | `10-K/99` l.568–578, l.1600–1610; `10-K/98` l.2853; §P255, §P.2 "Not computed" (ix) | **UNKNOWN** (cost, per-site terms); High (that the two totals cannot be summed) |
| **Every dated outage, incident, defect or abandoned experiment in the window** | **EMPTY in the filings, and UNTRIED outside them.** The FY1999 10-K discloses the **category** of failure (auction/zShops non-completion, heavy and non-uniform products, capacity) but names **no incident**; no filing in the stage reports an outage, a cancelled project or a test that did not repeat | **Very High for §M** — the negatives available to this stage are company-selected, and the record-selection null applies **inside the negatives** | `10-K/99` l.1032–1035, l.1266, l.1307–1317; §R Weaknesses; Stage 2 §S last row | **UNKNOWN** (any incident); **High** (that disclosed negatives are self-selected) — **UNTRIED**: `("Amazon" outage OR "site down" OR "did not arrive" OR complaint) 1998 OR 1999 site:latimes.com OR site:nytimes.com OR site:csmonitor.com`; `tools/` periodical-harvest run records (never consulted; **do not move or tidy**, method §14 rule 4) |
| **No archived amazon.com page for 1997, 1998 or 1999 was retrieved in this pass** | **Carried forward, not re-tested.** Stage 2 records **no root capture before 1998-12-12** and a bare 302 there, the earliest rendered homepage 1999-08-28, and every capable `matchType=prefix` CDX query returning **HTTP 504 — UNANSWERED, not proven absent**. This part made zero web requests, so the deep-path question is **still unanswered** | **Very High** — no launch row in §Q can be checked against the artifact; every "the site showed X" claim in this stage would be a documentary reconstruction | `sources/NULL_RESULT_wayback_1995_1996.md` (4,427 B); Stage 2 §S row 2, U.103 | **High** (homepage null as previously recorded) / **UNANSWERED** (any 1997–99 deep path) → U.103 (Stage 2) |
| **The FY1999 10-K's `FILED AS OF DATE` (2000-03-29) versus the submissions index `filingDate` (2000-03-23)** | **UNANSWERED as to which clock the market saw.** Both are printed by the archive; neither is wrong. The 10-K/A's primary document carries **no SEC header block at all**, so its period is **established by the index only** | **Medium** — it is a date-provenance rule, not a fact about 1999 | intake "Orchestrator addendum" (both bullets); §T rows for `10-K/99`, `10-K/A/99` | **High** (that the two clocks differ and that the amendment has no header) — **state which clock any citation uses** → U.166 |
| **The composition of the FY1997 technology carve-out, and of the FY1996 +464 of restated operating expense** | **EMPTY as to a note.** §P.2 t2b proves the reallocation **closes exactly** (409+532+270 = 1,211) and t21 proves the FY1996 change is +464 operating −5 interest = +469 net, but **which costs moved is nowhere stated** | **High** — it is the arithmetic that licenses §P191 and §P259 to be printed as FACT rather than as discrepancy, while the cause stays unknown | §P.2 t2, t2b, t21; `10-K/98` l.1234; `10-K/99` l.1746 | **High** (the arithmetic closes); **UNKNOWN** (what moved) → U.150, U.158, U.159 |
| **`sources.csv` row S0806, the phantom "FY1996 annual report", is still on disk** | Not a gap in the record — **a defect in the register.** No FY1996 annual filing of any form exists in the 125-row catalogue (Amazon's first annual report is the FY1997 10-K405), and S0806 has no accession, no URL and no document | **Very High for register integrity** — a phantom source row will be cited by any later pass that trusts `source_id` | intake §7(4); `ST2_B_finance.md`; Stage 2 §T S0806, U.111; **U.118** | **High** (that it is a phantom); recorded, **not fixed** — this part does not own `sources.csv` |
| **The `stage` column convention diverges inside four registers** | quantitative.csv holds **31 `stage3` and 110 `3`** rows; timeline.csv 43 `stage3` / 61 `3`; data_gaps.csv 11 `stage3` / 31 `3`; failures.csv and validation.csv use **`3`** while their Stage-1/2 rows use `stage1`/`stage2`. **Two Stage-3 grammars were applied to the same files** | **High for the merge** — a stage filter written as `stage=3` silently drops the `stage3` rows, and one written as `stage3` drops the others. **This part emits `stage3` for quantitative/timeline/data_gaps/decisions/channels/failures/validation, per §13's stageN form, and numeric `3` only for conflicts.csv and sources.csv, and flags the divergence for the orchestrator to normalise rather than adding a third grammar** | the per-file counts above, machine-verified this pass | **High** (the divergence is one command to reproduce) → §S.9 note |
| **Ten Stage-3 register rows are HELD for width and were never written** | The merge refused rows whose field count exceeded the canonical width; **a held row is a task, not a loss** (§14 rule 4). They are reproduced in full at **§S.9** and the two belonging to this part's registers are **re-emitted with canonical width in the append blocks below** | **Very High** — nothing may be dropped, and six of the ten are the channels and one sources row that no other part will re-write | `03_quality_control/stage3_register_merge_held_rows.md` (6,372 B) | **High** |

### S.9 The ten held register rows, reproduced so that nothing is lost

**Verbatim from `03_quality_control/stage3_register_merge_held_rows.md` "Held rows (10)".** The first six are the
`channels.csv` rows written at 12 fields against the file's canonical **11** (`company,stage,channel,date_tested,
why_tested,cost_or_effort,result,repeatability,source_id,confidence,notes`); the eighth is a `sources.csv` row at 19
against **18**; the ninth is a `decisions.csv` row at 14 against **15**; the tenth is a `quantitative.csv` row
**mislabelled as a timeline row** (12 fields carrying a quantitative header shape) whose three unquoted comma-bearing
values inflated it to 16 fields. **Dispositions:** row 10 is re-emitted by this part in the `quantitative.csv` block
(§P242); the seventh and the advertising row it depends on are re-emitted in the `channels.csv` block with the
commas quoted and the width corrected. **The six channel rows and the decisions and sources rows are outside this
part's evidence and are reproduced here in full rather than re-emitted, so that the next pass can rebuild them from
the text below without opening the QC file.**

| # | Dossier | Register | Cols written → expected | Row as held |
|---|---|---|---|---|
| 1 | `ST3_C_product_market.md` | `channels.csv` | 12 → 11 | `Amazon.com,3,Associates Program (commission syndication),1996 start UNKNOWN; counts 1998-09 and 1998-12-31,reach audiences not owned by the company,commission rate and spend: undisclosed at every date,enrolment 4,800+ (1996) to >140,000 (1998-09) to ~200,000 (…) — **truncated in the QC file**` |
| 2 | `ST3_C_product_market.md` | `channels.csv` | 12 → 11 | `Amazon.com,3,Portals and aggregators as paid conduits,1997-1999 continuous,acquisition of traffic at scale,advertising $3.4m / $21.2m / $60.2m (1996-1998); leases and marketing commitments bundled at $134,829K,spend tripled; ratio to net sales fell 21.6% to 9.(…) — **truncated in the QC file**; §P.2 t6 verifies the advertising series and extends it to $140.9m (FY1999), and re-checks $134,829 at `10-K/98` l.2853 as a single undifferentiated minimum-lease-payments column, NOT a leases-plus-marketing bundle` |
| 3 | `ST3_C_product_market.md` | `channels.csv` | 12 → 11 | `Amazon.com,3,Acquired local sites as distribution (Bookpages; Telebook),tested 1998-04-17/24; relaunched 1998-10,territory without building from zero,~$55m aggregate, mostly stock; two European DCs leased,combined Q4-1998 UK+DE sales nearly quadrupled over Q3;(…) — §P223 and §P.2 t11 carry the verified legs; **the filed instrument for the three April-1998 sites is 540,066 restricted shares**, so "~$55m aggregate" is a sum of differently-composed stated figures (→ U.163)` |
| 4 | `ST3_C_product_market.md` | `channels.csv` | 12 → 11 | `Amazon.com,3,Standing discount architecture,1997-03 to 1999,price as demand lever,gross margin, disclosed: 19.5% (FY1997) then 22.6% (Q2-1998) then guided down for Q4-1999,up to 30% on >400,000 titles; featured book AND music at 40%; special value to 89% then (…)` — 40%/89%/85% verified at §P233 → U.138 |
| 5 | `ST3_C_product_market.md` | `channels.csv` | 12 → 11 | `Amazon.com,3,Amazon.com Auctions (third-party sellers),1999-03-30,convert the registered buyer base into a seller side,$250-per-purchase buyer guarantee; no inventory,company filed revenue as minimal in the launch quarter; commissions later folded into net sal(…) — §P249 |
| 6 | `ST3_C_product_market.md` | `channels.csv` | 12 → 11 | `Amazon.com,3,zShops (third-party storefronts on amazon.com),late September 1999,assortment without inventory or title risk,placement fees plus sales commissions (levels undisclosed),no count of any kind; company disclaims responsibility for delivery of goods o(…) — §P248, §P270, **U.155** |
| 7 | `ST3_C_product_market.md` | `channels.csv` | 12 → 11 | `Amazon.com,3,Direct purchasing from manufacturers and labels,during 1998,cut the distributor layer out of cost of goods,inventory carried: $8,971K to $29,501K,Ingram share ~60% to ~40%; supplier count widened to three wholesalers,yes, but it converts supplier (…) — §P229 (and the ~60% is the FY1997 recast, not FY1998; see §P.2a row "Ingram") |
| 8 | `ST3_C_product_market.md` | `sources.csv` | 19 → 18 | `S3007,3,ST3C-50..ST3C-57,8-K event 1998-10-28 (Q3-1998 results release),SEC EDGAR acc 0000891020-98-001498,filing,primary,1998-10-28,1998-10-28,2026-09-25,local sources/8-K_event-1998-10-28_acc-0000891020-98-001498_filed-1998-10-28.txt,NO_ARCHIVED_PAGE,1,FACT+ (…) — **the row is 19 fields because the `url` cell contains a comma**; §T re-keys S3007 with that cell quoted, and `sources.csv` already carries 81 Stage-3 rows, so S3007 exists and must not be re-defined (§13: reuse ids) |
| 9 | `ST3_C_product_market.md` | `decisions.csv` | 14 → 15 | `Amazon.com,3,1998-04,Buy online booksellers in the UK and Germany rather than build export operations,one Seattle warehouse serving exports; international share falling 33% to 25%,two operating local sites with their own catalogues and DCs,licensing, local sup(…) — short by one field (14 vs 15), so a value was lost rather than a comma added; **cannot be repaired from this part's evidence** and is reproduced for the dossier's owner |
| 10 | `ST3_D_tech_ops.md` | `timeline.csv` (as written) | 12 → 11 | `Amazon.com,3,1999-Q4,depreciation and amortization single quarter,13,871,$000,10-K_FY1999 L2820 less 10-Q_Q3-1999 L314,2000-03-23,ESTIMATE/DERIVED,High,36,806 - 22,935 = 13,871,Q4 alone exceeds all of FY1998 (13,871/9,421 = 1.47x)` — **this is a `quantitative.csv` row wearing a `timeline.csv` label**: 12 fields in the quantitative header order with three unquoted comma-bearing values. Re-emitted in this part's `quantitative.csv` block as §P242, quoted and width-correct, with `derived_arithmetic` populated |

### S.9b Untried at assembly, carried forward from the Stage-2 lists that this part did not close

Method §14 rule 11's requirement, stated for Stage 3: the following Stage-2 UNTRIED items remain UNTRIED after this
pass, and this part adds **no** evidence to any of them — **Amendments Nos. 1, 2, 4 and 6 are now on disk (retrieved by
the Stage-3 intake, hyphenated names are canonical) but were not read line-by-line in this pass**; Fortune 1996-12-09
full text; the MatchMaker launch state; the US 5,999,911 prosecution history; the Washington Secretary of State
entity history for Cadabra → Amazon.com (a **connection failure**, not a null); the B&N suit disposition; the periodical
and trade corpora and the documentary-sale family (**method §14 rule 6's four families are still not all tried for this
company**); the merchant-account exhibits (the intake shows they **were never filed**, so that item is now closed as
UNRETRIEVABLE rather than UNTRIED); and `tools/` periodical-harvest run records, never consulted and not to be moved.

## T. SOURCE / PROVENANCE TABLE

**Keyed to the register's existing `source_id` values, which are re-used and never re-defined (method §9.4:
`sources.csv` is global-append-only per company; 81 Stage-3 rows already exist, `S3001…S3081`).**

**THE LINEAGE COLUMN IS THE LOAD-BEARING ONE, and `local_copy` is the second.** `local_copy: NO` means what Stage 2's
repair established it must mean: **the document is cited in this corpus but no bytes of it exist on disk**, so nothing
in this file may rest on it beyond what a dossier verbatim carries, and any later reader must be able to see the
difference between a citation and a document. Stage 3's corpus is unusually strong here — 75 complete submissions, plus
the FY1999 10-K and 10-K/A retrieved after them — so `local_copy: YES` is the default and the NO rows are the
exceptions worth reading.

| Source | Type | Primary/Secondary | Event date | Publication / filing date | Local path (bytes) | `local_copy` | **Lineage** | Tier | Confidence / independence |
|---|---|---|---|---|---|---|---|---|---|
| **Amazon.com Form 10-K405, FY1997**, acc. 0000891020-98-000448 — register id **S0805** | SEC annual report (delinquency cover; cite the form as filed) | Primary | FY1997 | **1998-03-30** | `sources/10-K_FY1997_acc-0000891020-98-000448_filed-1998-03-30.txt` (607,959 B) | **YES** | **AAP-97** — the issuer's first annual report; a **separate reporting instrument** from the L-97/333-23795 registration lineage, but the same author | 1 | High. **Own-only content used by this part: the 614 full-time sentence (l.516); the 158→614 growth sentence (l.729); the "In November 1997 the Company **opened** a 200,000-square-foot distribution center in Delaware" sentence (l.1646–1648), which is the falsification at U.153; Ingram 58%/59% (l.1669–1670); "no long-term contracts… with **any** of its vendors" (l.1671); the FY1997 audited column as filed (l.1177–1194, l.1861–1881); gross fixed assets 12,899/9,265 (l.2300–2308); D&A 3,388 (l.2037); the first advertising note, $21.2m/$3.4m/$30,000 (l.2187–2189); the 19.5%/22.0%/20.0% margin row (l.1403); "more than $164 million" cumulative (l.241)** |
| **Amazon.com Form 10-K, FY1998**, acc. 0000891020-99-000375 | SEC annual report | Primary | FY1998 | **1999-03-05** | `sources/10-K_FY1998_acc-0000891020-99-000375_filed-1999-03-05.txt` (321,454 B) | **YES** | **AAP-98** — second instrument of the annual-report family; **its FY1997 comparative column is a recast of S0805's own-year column, not a corroboration** | 1 | High. Own-only content: FY1998 net sales **609,996** and the 313%/839% growth row (l.1222, l.1309); the recast FY1997/FY1996 five-year tables (l.1222–1247) and balance-sheet data (l.1260–1265); 2,100 employees (l.528); 6.2m/1.5m accounts and **over 60%** repeat (l.1317–1320); international 20/25/33% (l.1325); 4.7m titles (l.214, l.283); Ingram **~40%** and ~60% for 1997 and the B&N-to-buy-Ingram risk (l.422, l.504, l.797–799, l.2374); ~200,000 Associates (l.383–386); D&A 9,692/3,442 (l.2232); fixed assets 43,585/29,791 and 1997 at **13,490/9,726** (l.2750); advertising 60.2/21.2/3.4 (l.2459); **$134,829** minimum lease payments (l.2853); the 10% Senior Discount Note terms; the F2 footnote "financial data schedules **have not been restated** for the stock split" (l.5708) → U.164 |
| **Amazon.com Form 10-K, FY1999**, acc. 0000891020-00-000622 | SEC annual report | Primary | FY1999 | **2000-03-23 by the submissions index; its own SEC header prints `FILED AS OF DATE: 20000329`** — two clocks, six days apart; **this part cites the index date and says so** (intake addendum) | `sources/10-K_FY1999_acc-0000891020-00-000622_filed-2000-03-23.txt` (307,278 B) | **YES** | **AAP-99** — third instrument of the family; **its comparative columns are the third printing of 1996–98** | 1 | High. **Registered here because this part uses it heavily** (§P235–P247, §P253, §P256, §P265, §Q, §R). Own-only: FY1999 net sales **1,639,839**, gross profit 290,645, the five new expense captions and total 896,400 (l.1732–1766); **the product/service launch table to the month** (l.274–285); **17 million accounts** (l.198); **~7,600 full-time and part-time employees** (l.684); **fulfilment $188.4m/$50.3m/$12.1m** (l.1970, l.3101) — the only place those dollars are filed; advertising **$140.9m** (l.3107); D&A **36,806** (l.2820); the estate's two "eights" (l.568–573, l.1602–1605); the three-split recital (l.3817–3825); options **54,664 @ $0.751** (l.3886); the cash-flow statement on the **old** cash basis (l.2860–2875); segments (l.220–226); 13 million titles (l.305); 430,000 Associates at 2000-02-29 (l.544) |
| **Amazon.com Form 10-K/A, FY1999**, acc. 0000891020-00-001638 | SEC **amended** annual report | Primary | FY1999 | **2000-09-08**; the primary document `v65477e10-ka.txt` carries **no SEC header block** — `CONFORMED SUBMISSION TYPE`, `PERIOD OF REPORT` and `FILED AS OF DATE` return nothing from its first 1,500 bytes, **so its period is established by the submissions index only and anyone citing it must cite the index** | `sources/10-K_A_FY1999_acc-0000891020-00-001638_filed-2000-09-08.txt` (173,340 B) | **YES** | **AAP-99 (second state of the SAME instrument as the row above) — NOT a fourth source.** Under method §3 the 10-K and its amendment are one instrument in two states: a figure printed in both is filed once | 1 | High. **Registered here because this part uses it and because the amendment is the only place several figures appear.** Own-only: the **explanatory note** (l.94–110) — the cash-equivalents policy change reported in the Q2-2000 10-Q, Items 6/7/7A/8 and the data schedule revised, "**THE AGGREGATE TOTAL OF CASH EQUIVALENTS AND MARKETABLE SECURITIES HAS NOT CHANGED**", and the Note 9 transposed-figures correction; the E&Y dual-dated report (Feb 2 2000, Note 15 Feb 16 2000) with the restatement paragraph (l.976); the **restated cash-flow statement** with FY1998 at **(38,536)** (l.1338); the preference-of-policy paragraph (l.1448–1456); **Note 2 business combinations** naming six 1999 acquisitions with dates, share counts and ~$145m/$189m/$40m prices and the **$2.8m in-process R&D write-off** (l.1695–1760); the acquisitions list in MD&A (l.550–554); the restated Item 6 cash lines (l.221–226); the zShops/Auctions fee wording (l.292); the stale "18 million shares" IPO / 36:1 conversion note (l.2307–2317) → **U.154, U.156, U.157, U.165, §P.2 t18** |
| **Forms 10-Q, 1997–1999 (eight)** — Q2-1997 …1148 (1997-08-14) · Q3-1997 …1466 (1997-11-14) · Q1-1998 …0846 (1998-05-15) · Q2-1998 …1313 (1998-08-14) · Q3-1998 …1632 (1998-11-13) · Q1-1999 …0894 (1999-05-17) · Q2-1999 …1426 (1999-08-16) · Q3-1999 …1938 (1999-11-15) | SEC quarterly reports | Primary | each quarter | as listed | all eight under `sources/10-Q_*.txt` (67,658–835,834 B); **total ≈3.4 MB** | **YES** | **One instrument family, eight separate reporting acts** — successive, not duplicative; a figure repeated across quarters is the same author re-reporting | 1 | High. Own-only content used here: **the five Buschman "Sales Agreements" and their confidential-treatment footnote** (`Q1-1999` l.1660–1669, l.1678–1681 → U.114, U.152); **two "opened" sentences for the Nevada centre** (`Q1-1999` l.592, l.915 → U.153); the eight-month D&A of 22,935 (`Q3-1999` l.314 → §P.2 t17); **five opened DCs with Kentucky also announced** (`Q3-1999` l.830–833 → U.117); **zShops/Payments/Anywhere/Cards dates** (`Q3-1999` l.795–816 → U.142, U.155); **Galli and Jenson** (l.824–828); accounts **10.7m and 13.1m inclusive of Auctions** (`Q2-1999` l.862, `Q3-1999` l.871 → U.139); the special-value 89% print (`Q2-1998` l.881 → U.138); the 1998 split recitals (`Q1-1998` l.468, `Q2-1999` l.636, l.652–655); Bookpages/Telebook/IMDB (`Q1-1998` l.483) |
| **Forms 8-K, 1997-11-07 → 1999-10-28 (26 items incl. the 8-K/A)** | SEC current reports with attached releases | Primary | event dates as filed | filed 1–21 days later | all under `sources/8-K_event-*.txt` and `8-KA_*.txt`; sizes 7,040 B – 449,123 B | **YES** | **One-off events; the attached releases are company self-reports, so they corroborate a filing's number without confirming it (method §3)** | 1 | High. Used for: the **$75m Deutsche Bank facility** (1997-11-07); **Bookpages/Telebook/IMDB for 540,066 Reg S shares** (1998-04-17); the **$275m note announcement and its upsize** (1998-04-24, 1998-05-05); **Junglee/PlanetAll merger agreements** (1998-08-03); the **13,490 FY1997 gross fixed assets appearing in August 1998** (1998-08-27 l.1485); **Q3-1998 results, music $14.4m, Associates >140,000** (1998-10-28); **"ANNOUNCES 3-FOR-1 STOCK SPLIT"** (1998-11-19); the **video store launched November 17** and 4.7m titles (1999-01-26); the **$500m ask and the $1.25bn close** (1999-01-28 ×2, 1999-02-03); **Auctions launched** (1999-03-30); **seven DCs / nearly 4m sq ft / 3.3m accounts at 1998-06-30** (1999-07-21 l.202, l.311–317 → U.151, U.127); **zShops "in late September"** and Media Metrix for September (1999-10-28). ⚠ **Two index-vs-text date traps registered: U.120 (Alexa 1999-06-08 index / 1999-06-10 Item 2) and U.166 (the press release inside the 1999-10-28 8-K is dated 1999-10-27)** |
| **Annual reports to shareholders: ARS FY1997 (1998-04-17) and ARS FY1998 (1999-04-07)** | Company shareholder letter with financial highlights | Primary (company-authored) | FY1997 / FY1998 | as listed | `sources/ARS_1997-…-000600_filed-1998-04-17.txt` (14,188 B); `sources/ARS_1998-…-000637_filed-1999-04-07.txt` (26,009 B) | **YES** | **Same issuer, same year as the 10-K, different document** — a re-presentation, so its numbers corroborate nothing the 10-K lacks; **its value is the founder's contemporaneous language, which the 10-K does not carry** | 1 | High as artifacts; **`RETROSPECTIVE`-free — these are the best in-window founder-state documents in the corpus** (intake §9(3)). Used for: **838%** growth, **180,000 → 1,510,000** accounts (+738%), **repeat >46% (Q4-96) → >58% (Q4-97)**, **Media Metrix rank 90th → top 20**, the named partner list (AOL, Yahoo!, Excite, Netscape, GeoCities, AltaVista, @Home, Prodigy) (`ARS/97` l.204–218); **"employee base grew from approximately 600 to over 2,100"** and **"we opened distribution and customer service centers in the U.K. and Germany"** + the 323,000 sq ft Fernley lease announcement (`ARS/98` l.157, l.160–165) → **U.153, U.161, §P206, §P207, §P208** |
| **Proxies: DEF 14A 1998 (1998-04-17) and DEF 14A 1999 (1999-04-07), with their PRE 14As (1998-05-05, 1999-03-15)** | SEC proxy statements | Primary | 1997 / 1998 compensation years | as listed | `sources/DEF14A_*.txt` (61,828 B; 65,778 B), `sources/PRE14A_*.txt` (62,680 B; 65,048 B) | **YES** | **Part III of the annual reports is incorporated by reference to these; they are the only filed source of officer pay and dates** | 1 | High. **The FY1997 10-K deferred its related-party item to the 1998 proxy, and the FY1998 10-K routes Item 13 to the 1999 proxy — so Stage 2's "the 1998 proxy is not on disk" gap is CLOSED by the intake.** Used for: **Bezos salary 64,333 / 79,197 / 81,840 with nil bonus and nil option value in each year**; Dalzell 201,512, Aposporos 142,083, Spiegel 116,352, Risher 105,168; **the four-date/five-name officer footnote** (→ U.115); **Risher 1997-01-31, Wright 1998-07-27**; the **Item 402(a)(3)(iii) footnote** (→ U.119); **Dalzell's 1997 grant 125,000 → 750,000 on the split alone** (→ U.130); the **$75,000 interest-free relocation loan repaid 1998-10-23**; the Cook/Stonesifer $40.00 Series A purchases |
| **Forms S-4 ×2, S-4/A ×2, POS AM ×3, POS AMI ×2, S-3 ×3, S-3/A ×3, 424B2, 424B3 ×2, 8-A12G, S-1/A Nos. 1, 2, 4, 6 (hyphenated canonical; underscore duplicates retained per §14 rule 4), S-8 ×8, S-8 POS ×2, SC 13G ×2** | SEC registration, post-effective and Section 16-adjacent filings | Primary | 1997–1999 | as filed | all under `sources/`, ≈**10.1 MB** of complete submissions retrieved by the Stage-3 intake plus the Stage-1/2 set | **YES** (the bodies are inline in the complete submissions) | **Five distinct shelf/transaction lineages, not one:** **L-98/333-55943** (Junglee → S-4/A No. 1 → POS AM Nos. 1 and 2 → POS AMI) · **L-98/333-56723** (Bookpages/Telebook European set) · **L-98/333-65091** (1998-09-30 shelf → S-3/A → S-8 POS → POS AMI) · **L-99/333-74435** · **L-99/333-78797** (the $2bn universal shelf) · and **L-97/333-23795** (Stage 2's registration lineage, whose Nos. 1, 2, 4, 6 are now on disk). **A figure appearing twice inside one of these has been filed once** | 1 | High. Used for: the **S-4 shelf time series 5m → 15m → 30m** (→ U.116); **SIC 2731 on 333-55943 and 5961 on 333-56723 nine days later** (→ U.137); the **2,662,125-share resale** (424B3 1998-10-22 and its 10-27 supplement, 82,999 B and 88,584 B); the **$326m gross** of the notes; **"$349 million of outstanding senior indebtedness"** eleven days after the FY1998 10-K (→ U.131); the **POS AMI whose EDGAR description contradicts its own file number** (→ U.122); the **eight S-8 plan registrations** as the hiring curve; the **8-A12G prospectus-date typo** (→ U.121, U.132). ⚠ **Naming defect, left in place deliberately** (intake §8): the four S-1/A files exist under both `S-1A_No*` and `S-1A-No*` names, byte-identical bodies — **cite the hyphenated form; the underscore copies are not separate sources** |
| **Barnes & Noble, Inc. Form 10-K** for the 52/53 weeks ended 1997-02-01, acc. 0000889812-97-001072 | SEC filing of a competitor | Primary | FY1997 | 1997-05-02 | **not held** — read through `research/ST2_C_market_competition.md` S2C-17/20 | **NO** | **GENUINELY INDEPENDENT of every Amazon row: a different registrant, a different audit, no common drafter** | 1 | High **as to what a competitor's own audited filing says**, but **a Stage-3 citation may not go beyond what the Stage-2 dossier carries**. **Basis discipline: a 53-week year ending 1997-02-01, not coterminous with Amazon's FY1997** (→ U.66). **Retrieval of the FY1998/FY1999 B&N 10-K — which would settle whether the Ingram acquisition completed inside this window — is UNTRIED**: `EDGAR CIK 0000889812 10-K 1999 Ingram` |
| **`STAGE3_INTAKE_MANIFEST.md`** and **`research/_EVIDENCE_CACHE.md`** | Internal retrieval records (Level-3 working papers) | **Secondary, derivative of the accessions above** | — | 2026-09-25 | `sources/STAGE3_INTAKE_MANIFEST.md` (24,141 B) | **YES** | **Not sources of fact — indexes to sources, plus 226 lines of request accounting.** Their load-bearing content for this part is the **enumeration** (125 catalogue rows, 75 fetched, 45 withheld with reasons, 10 held items) and the two corrections in the orchestrator addendum | — | **Working papers, no tier.** ⚠ **This part overturned one of its own labels**: the manifest's periodic-spine note called the five 1999-03-11 "Sales Agreements" "the material third-party selling/merchant contracts"; the filed exhibits are five agreements with **one** counterparty, The Buschman Company, with confidentially treated terms (**U.114, U.152**). **Where a manifest and a filing disagree, this file prints the filing** |
| **`research/ST3_A…E`, `ST2_A…E`, `A…K` dossiers** | Internal mining dossiers | Secondary, derivative of the accessions | — | 2026-09-24/25 | `research/` (nine Stage-3 dossier paths registered by the orchestrator) | **YES** | Not sources of fact. **Every number this part lifts from a dossier was re-verified against the local filing text and is cited here to the filing and line** (§14 rule 8). Where a dossier and a filing disagree, §P.2a prints the filing and the received value as a retraction | — | Working papers, no tier |
| **David Sheff, interview of Jeff Bezos (*Playboy*)** | Interview transcript | Secondary, founder-originated | conducted **1999** | published **2000** | `sources/sheff-playboy-interview_davidsheff-com-jeff-bezos.txt` (52,098 B) / `.html` (133,811 B) | **YES** | **Founder's retrospective account; one origin story however many sites reprint it** (§3) | 1 as a 1999/2000 artifact; **4 as evidence for 1997–99** | **`RETROSPECTIVE SOURCE`.** The intake ranks the two ARS letters **above** this interview for any claim about what Bezos believed while Stage 3 ran (§9(3)). **No §P, §Q or §R row in this part rests on it** → U.105 (Stage 2) |
| **HistoryLink.org Essay 23230**, "Amazon: The Early Years (1995–1999)" | Regional-history essay with its own source list | Secondary | 1994–1999 | **2025-04-07** | `sources/historylink-essay-23230_…txt` (21,399 B) / `.html` (54,616 B) | **YES** | **Derivative by its own footnotes — every day-level and dollar-level detail traces to Stone (2013) or press, not to a document** | **2 at best** | Medium for existence; **Low for every specific it supplies**; the "Get Big Fast" motive language is **uncited in the essay** and is used nowhere here as a motive → U.105 (Stage 2) |
| **Internet Archive CDX / Wayback availability API, and the recorded null** | Archive index | Primary **about the archive** | null 1994–1999 | retrieved 2026-09-23 | `sources/NULL_RESULT_wayback_1995_1996.md` (4,427 B) | **YES** | **Evidence about the record, never about the site** | 1 | High. Root capture before 1998-12-12: none; earliest rendered homepage 1999-08-28; deep paths **UNANSWERED** because the capable prefix queries returned **HTTP 504** — a 504 is a failure, not a null → §S, U.103 (Stage 2) |
| **Non-Amazon 1997–99 periodicals: contemporaneous press on the category launches, the music and video price war, and the holiday season** | Periodical corpora | Would be **independent Tier 1/2 artifacts** | 1997–1999 | — | **none held** | **NO** | **Independent of the company by construction — and this is the family method §14 rule 6 requires before any depth verdict, still NOT TRIED for Stage 3** | — | **UNTRIED.** Every §Q product row in this part rests on a company sentence. Queries: `HathiTrust / Internet Archive periodicals 1998 "Amazon" music store discounts`; `"online bookstore" price war 1998 site:latimes.com OR site:nytimes.com`; `"Amazon" holiday 1998 delivery complaints`; **and the `tools/` periodical-harvest run records, never consulted, not to be moved** (§14 rule 4) |
| **Failed, absent and never-attempted routes, recorded so they are not re-run or mistaken for nulls** | Retrieval log | — | — | attempted / **untried** 2026-09-25 | — | — | — | — | **Zero rows in the catalogue:** Section 16 Forms 3/4/5 in slice `-002` (1997-03-24 → 2000-01-04) — `-001` **not yet checked**, **UNTRIED**. **Never filed, so unfetchable:** the merchant-account and card agreements behind the Bezos guarantees. **Not fetched by choice:** 35 × 424B3, 10 × third-party Schedule 13 (intake §5a–§5b). **Transient failures resolved on immediate retry:** one **503** on a valid dashed URL and one first-attempt failure on acc. `0000891020-99-000910` — **both recorded so nobody reads a 503 as an absence**. **Self-inflicted:** 150 × 404 from de-dashed legacy URLs (intake §4, a recorded overrun of 230 requests against a 150 cap). **Recipe for all of the above is in intake §6 — use it, do not re-derive it** |

**`local_copy` roll-up for this part's citations, stated so a reader can see the corpus's shape at a glance:** of the
documents this part actually cites a figure from, **`local_copy: YES`** for the four annual reports, all eight 10-Qs,
the 26 8-K items, both ARSs, both DEF 14As, the resale and shelf lineages, the 8-A12G, the four newly-local S-1/A
amendments, the eight S-8s, the two SC 13Gs, the intake manifest, and the two documented null files.
**`local_copy: NO`** for the B&N 10-K (read via dossier), for all non-Amazon 1997–99 periodicals, and for the 45
catalogued-but-unfetched items. **No figure in §P, §Q or §R rests on a `NO` row** except where the cell says the
number is carried from a dossier's verbatim and is capped at Medium.

## U. CONFLICTING EVIDENCE (STAGE 3) — U.114 → U.168

**Numbering and invariants.** Stage 1's spine ends at U.43 and Stage 2's at U.113. The 39 Stage-3 rows in
`conflicts.csv` were keyed `P-U.114 … P-U.152` at merge time because the four dossiers invented four grammars
(`ST3_A` U.201–U.211, `ST3_B` C-1…C-9, `ST3_C` U-C1…U-C12, `ST3_D` U.D1…U.D8); each dossier's original id is
preserved inside that row's `section` column, so the mapping is reversible and is printed in full at the
`>>> CONFLICT RE-KEY MAP` below. **No id in U.1–U.113 is renumbered, re-opened or cleaned** (method §9.3, appending
only). Blocks U.114–U.152 correspond 1:1 to the 39 provisional rows and **are not re-emitted as CSV rows** — writing
them again would duplicate the register. Blocks U.153 onward are new registrations from this pass and each is emitted
once as a `conflicts.csv` row in the append block.

**Nothing here is reconciled silently.** Every contradiction keeps both sides, with the source and the filing date of
each leg. A conflict settled on arithmetic says so and names what remains open; a conflict the record cannot settle
stays open as a finding.

**U.114 — The five 1999-03-11 "Sales Agreements" are not the marketplace's contractual trace.**
**CLAIM A:** the five Sales Agreements dated 1999-03-11 listed in the Q1-1999 10-Q are "the material third-party
selling/merchant contracts — the contractual trace of the marketplace model" (`_EVIDENCE_CACHE.md`, Stage-3 intake
periodic-spine table, 2026-09-25). **CLAIM B:** all five are "**Sales Agreement, dated March 11, 1999, by and between
Amazon.com, Inc. and The Buschman Company**", and each "Contains omitted, confidential material, which material has
been filed separately with the SEC pursuant to a request for confidential treatment under Rule 24b-2" (Form 10-Q
Q1-1999, acc. 0000891020-99-000894, exhibit index L1660–1669 and footnote L1678–1681, filed 1999-05-17).
**WHY THEY DIFFER:** Claim A infers subject matter from an exhibit *title* without reading the counterparty field. In
1990s SEC usage a "Sales Agreement" is as often an equipment-sale or securities-purchase instrument as a merchant
contract, and here the same-named counterparty appears five times, which is the signature of a purchase-order series
for equipment, not a set of distinct marketplace sellers.
**EVIDENCE WEIGHT:** Claim B is the filed text of the very document Claim A cites; a retrieval use-note cannot
outweigh its own source. Tier 1 versus a working-paper index row.
**BEST-SUPPORTED INTERPRETATION:** the marketplace's contractual trace is **not** in these exhibits. It is the 8-K of
1999-03-30 (auctions launched) and the Q2/Q3-1999 definitions of net sales. The Buschman agreements' subject matter
is UNKNOWN and unrecoverable from EDGAR because the operative terms were granted confidential treatment. This row is
the register's proof of the paired defect at **U.152**, which records the same misreading from the intake manifest
side.
**RESIDUAL UNCERTAINTY:** what The Buschman Company contracted for; whether *any* merchant contract was filed in the
window at all. **CONFIDENCE:** High (that Claim A is wrong) / UNKNOWN (subject matter).

**U.115 — The 1998 proxy officer roster: five names, four dates, and a cache that paired them one-to-one.**
**CLAIM A:** DEF 14A 1998 gives the officer roster "(Aposporos, Dalzell, Duenas, Kaphan, Spiegel)" with start dates
"(May 9 / Sept 2 / Jan 8 / Mar 17, 1997)" — five names against four dates, printed as though they matched
(`_EVIDENCE_CACHE.md`, DEF 14A 1998 row, 2026-09-25). **CLAIM B:** the 1998 proxy's own footnote attaches **four**
dates to **four** names in table order (Aposporos, Dalzell, Duenas, Spiegel) and gives **Kaphan none**, because he had
been VP of R&D since October 1994; the 1999 proxy separately gives Risher **1997-01-31** and Wright **1998-07-27**
(DEF 14A 1998 acc. 0000891020-98-000601 L598–616, 1998-04-17; DEF 14A 1999 acc. 0000891020-99-000635 L623–627,
1999-04-07).
**WHY THEY DIFFER:** the cache compressed a five-name list and a four-date list into a false one-to-one correspondence.
The two proxies also carry different named-officer sets, which is a roster question, not a dating question (→ U.119).
**EVIDENCE WEIGHT:** both filings are Tier 1; the cache is a finding-free transcription and loses.
**BEST-SUPPORTED INTERPRETATION:** Aposporos 1997-05-09, Dalzell 1997-09-02, Duenas 1997-01-08, Spiegel 1997-03-17 per
the 1998 proxy; Risher 1997-01-31 and Wright 1998-07-27 per the 1999 proxy. **There is no conflict between the two
proxies** — they report different offices at different dates. The conflict is between the filings and the working
paper that summarised them, and it is the reason §Q dates officers only from a proxy line, never from a cache row.
**RESIDUAL UNCERTAINTY:** the FY1997 10-K says Risher "joined the Company in **February 1997**" while the 1999 proxy
says **January 31, 1997** — a day-versus-month difference inside one corporate record, kept as two prints.
**CONFIDENCE:** High.

**U.116 — The S-4 shelf (File No. 333-55943) registered 5 million, 15 million or 30 million shares, depending on the date.**
**CLAIM A:** S-4 File No. 333-55943 registers up to **5,000,000** shares (Form S-4 acc. 0000891020-98-000931 L970,
1998-06-03; S-4/A No. 1 acc. 0000891020-98-001238 L1025, 1998-08-11). **CLAIM B:** Ernst & Young's consent refers to
"Registration Statement (Form S-4 No. 333-55943) for the registration of **15 million shares** of common stock", and
POS AM No. 1 later registers "up to **15,000,000** shares" (Form 10-K FY1998 EX-23.1 L5638–5639, 1999-03-05; POS AM
File No. 333-55943 Amendment No. 1 L901, 1999-04-26).
**WHY THEY DIFFER:** an auditor's consent is drafted against whatever the registration statement covered **at its
report date** (1999-01-22); the shelf was raised by post-effective amendment on 1999-04-26, *after* that report date.
A consent that says 15 million in March 1999 cannot be describing the 1999-04-26 amendment.
**EVIDENCE WEIGHT:** both legs are Tier 1 and inside one lineage family, so the **sequence** resolves the conflict
rather than one leg beating the other.
**BEST-SUPPORTED INTERPRETATION:** read as a time series, not as competing figures: **5,000,000 (1998-06-03) →
15,000,000 (1999-04-26) → 30,000,000 (1999-08-06)**. No §P row prints "the S-4 shelf size" without a date attached.
**RESIDUAL UNCERTAINTY:** no S-4/A No. 2 exists in the catalogue, so either the January 1999 consent is loose or an
amendment is missing from EDGAR — a documented gap, not a resolved one.
**CONFIDENCE:** Medium (the sequence) / **Low (the provenance of the January 1999 15-million figure)**.

**U.117 — Five distribution centres "opened" by 1999-09-30, and Kentucky in the list of those still to be located.**
**CLAIM A:** five distribution centres were **opened** by 1999-09-30: **Nevada, Georgia, Kentucky, Kansas and North
Dakota** (Form 10-Q Q3-1999, acc. 0000891020-99-001938, L830–831, 1999-11-15). **CLAIM B:** the same sentence
announces "additional new distribution centers **to be located in Kentucky, Germany and the United Kingdom**" — so
Kentucky appears in both the opened list and the announced list (same filing, L832–833).
**WHY THEY DIFFER:** either two separate Kentucky facilities (one opened, one further announced) or a drafting slip.
**EVIDENCE WEIGHT:** one document, one sentence; nothing external adjudicates. The Q2-1999 10-Q's parallel announced
list (Kansas, Georgia, Kentucky, Germany, UK) is consistent with more than one Kentucky site being in the programme,
which is the weak tie-breaker and nothing more.
**BEST-SUPPORTED INTERPRETATION:** report as filed — five opened, three announced, Kentucky in both — and refuse to
produce a count of "distinct Kentucky facilities". This conflict is the reason §R's estate row prints the **named**
sites with their verbs ("opened"/"to be located") rather than a single total, and it pairs with **U.151/U.144** on
how many distribution centres existed at all.
**RESIDUAL UNCERTAINTY:** how many distinct Kentucky facilities existed by 1999-09-30.
**CONFIDENCE:** High (that the filing says this) / UNKNOWN (the count).

**U.118 — Employees at 1996-12-31: 151 full-time and 158 unqualified, now seen from the Stage-3 side.**
**CLAIM A:** "As of December 31, 1996, the Company employed **151 full-time employees**" (Form S-1 original acc.
0000891618-97-001309, EMPLOYEES L2364, 1997-03-24). **CLAIM B:** "growing from **158 employees as of December 31,
1996** to 614 employees as of December 31, 1997" (Form 10-K405 FY1997, risk factor MANAGEMENT OF POTENTIAL GROWTH
L724–729, 1998-03-30) — unqualified as to "full-time".
**WHY THEY DIFFER:** basis — full-time only versus all employees. The later annual report restates the prior year
inside a growth sentence and drops the qualifier, which is exactly where a temporary and contractor pool would appear.
**EVIDENCE WEIGHT:** both Tier 1 and in **different lineage families** (a 1997 registration statement and a 1998
annual report), so unlike most pairs in this spine these are genuinely two documents. Neither is a restatement of the
other's instrument.
**BEST-SUPPORTED INTERPRETATION:** keep both, never merge, never average. This is Stage 2's **U.44** re-registered on
the Stage-3 record because Stage 3's §R must place **three** filed headcount bases side by side (614 at 1997-12-31,
1,233 at 1998-12-31, ~7,600 full-time at 1999-12-31) and the 151/158 pair is the precedent that says a "headcount"
is a *basis* before it is a number. Separately: `sources.csv` row **S0806** registers a non-existent "FY1996 annual
report" as the source of 158; the FY1997 10-K405 line above is the real filed source and should replace it (COR-105),
which this part records rather than fixes (not its file).
**RESIDUAL UNCERTAINTY:** whether 158 includes independent contractors and temporary employees.
**CONFIDENCE:** High on both figures as stated / Medium on which to use for ratio arithmetic. **No per-employee
figure is computed at §P for this reason** (see §P.2 "Not computed").

**U.119 — The FY1998 10-K lists seven executive officers; the 1999 proxy pays an eighth who is not on that list.**
**CLAIM A:** FY1998 10-K executive officers are **seven** — Bezos, Covey, Dalzell, Kaphan, Risher, Shriram, Wright.
**Aposporos and Engstrom are absent**, and "Vice President of Business Development" is given as **Shriram's** title
(Form 10-K FY1998, EXECUTIVE OFFICERS L940–955, 1999-03-05). **CLAIM B:** DEF 14A 1999 pays **George T. Aposporos
$142,083 for 1998** as "Vice President of Business Development", footnoted "included pursuant to Item 402(a)(3)(iii)
of Regulation S-K" (DEF 14A 1999, Summary Compensation Table L617–619 and footnote (4), 1999-04-07).
**WHY THEY DIFFER:** the two tables answer different questions. The 10-K lists current executive officers **at filing
date**; Item 402(a)(3)(iii) compels disclosure for a person who was an officer at the fiscal year-end or would have
ranked among the top four but for timing. Two people may also hold one VP title, and nothing in either document
forbids it.
**EVIDENCE WEIGHT:** both Tier 1, within the same Part III disclosure family; neither overturns the other.
**BEST-SUPPORTED INTERPRETATION:** Aposporos's 1998 **compensation** is established; his status as an executive
officer on 1999-03-05 is not. **No §R or §Q row may describe the officer roster as "8 then 7"** without noting that a
ninth person holding a listed officer's title was still being paid under a named office.
**RESIDUAL UNCERTAINTY:** whether Shriram and Aposporos held the same title simultaneously; what became of Engstrom,
who is absent from both.
**CONFIDENCE:** Medium.

**U.120 — The Alexa 8-K: EDGAR's event date is 1999-06-08, its own Item 2 says the merger completed 1999-06-10.**
**CLAIM A:** EDGAR's index `eventDate` (reportDate) for the Alexa Internet 8-K is **1999-06-08** (Form 8-K acc.
0000891020-99-000993, face and catalogue row, filed 1999-06-11). **CLAIM B:** the same 8-K's **Item 2** states the
Alexa merger was **completed 1999-06-10** (same filing, Item 2 text).
**WHY THEY DIFFER:** `reportDate` is the date of the earliest event reported on the form's face; a closing window
spanning 6/9–6/10 is reported against its opening day. One 8-K covering a two-day event sequence is common practice.
**EVIDENCE WEIGHT:** the internal text controls the completion fact; the index controls nothing.
**BEST-SUPPORTED INTERPRETATION:** record completion as **1999-06-10** and cite the form as filed with its 1999-06-08
event date attached — per the registrar's standing instruction not to silently fix an index value. §Q therefore
carries both keys, and `timeline.csv` uses 1999-06-10 with the 1999-06-08 index date recorded in `notes`.
**RESIDUAL UNCERTAINTY:** none material. **CONFIDENCE:** High.

**U.121 — The 8-A12G's prospectus date of "April 21, 1996" is an internal impossibility.**
**CLAIM A:** 8-A12G Item 1 describes "the Prospectus … dated **April 21, 1996** contained in the Registrant's
Registration Statement on Form S-1 … filed … on **March 24, 1997**" (Form 8-A12G acc. 0000891020-97-000704,
1997-05-02). **CLAIM B:** no prospectus dated 1996-04-21 can be contained in a registration statement filed 1997-03-24;
**1997-04-21** is Amendment No. 1's prospectus date (Registration Statement File No. 333-23795 filing history, same
lineage).
**WHY THEY DIFFER:** a typographical error in a form **signed by Joy D. Covey**. The year digit is the error, not the
day and month, which is why the string survives a reader who checks only "April 21".
**EVIDENCE WEIGHT:** Claim B is arithmetic on two dates both documents agree to. There is no reading on which 1996 is
right.
**BEST-SUPPORTED INTERPRETATION:** **never cite the 8-A12G for a 1996 date.** Pre-registered in the Stage-3 intake
manifest; this dossier confirms the error is unchanged on the filed text and finds no occurrence of a 1996-04-21
prospectus anywhere else in the corpus. Paired with **U.132**, which records the same defect from the finance side;
both are kept because the two dossiers found them independently and the register should not silently collapse two
detections of one defect into one row.
**RESIDUAL UNCERTAINTY:** none. **CONFIDENCE:** High.

**U.122 — EDGAR calls acc. 0000891020-99-001503 a "POS EFFECTIVE AMENDMENT NO.1 TO FORM S-3"; it is a POS AMI to the S-4 shelf.**
**CLAIM A:** EDGAR's `primaryDocDescription` for acc. 0000891020-99-001503 reads "**POST EFFECTIVE AMENDMENT NO.1 TO
FORM S-3**" (EDGAR submissions slice, `-002` catalogue row, read 2026-09-25). **CLAIM B:** the filing is Form **POS
AMI** under **File No. 333-55943**, the **S-4 acquisition shelf**, and it names **2,662,125 shares** — a number
belonging to File No. **333-65091** (POS AMI body and SEC-HEADER L152, 1999-08-31).
**WHY THEY DIFFER:** index prose versus file number versus share figure. Three fields, three answers. The share count
inside a 333-55943 amendment that belongs to a 333-65091 population is the most interesting of the three and the least
explicable.
**EVIDENCE WEIGHT:** the file number and the in-body statement of the registration being amended control. Index prose
is generated, not certified.
**BEST-SUPPORTED INTERPRETATION:** quote the **form code and file number**, never the description prose. §T therefore
keys this accession by file number with the index description recorded as a trap.
**RESIDUAL UNCERTAINTY:** what the POS AMI retired, and why it cites a 333-65091 share figure.
**CONFIDENCE:** High (that the description is unreliable) / UNKNOWN (why).

**U.123 — The SIC change from 2731 to 5961 is weak evidence and must not carry a stage boundary.**
**CLAIM A:** Stage 3's transition is proved by the SIC change: FY1997 carries **2731 BOOKS: PUBLISHING OR PUBLISHING
AND PRINTING** and FY1998 carries **5961 RETAIL-CATALOG & MAIL-ORDER HOUSES** (Form 10-K405 FY1997 header L42; Form
10-K FY1998 header L48, 1999-03-05). **CLAIM B:** the FY1997 filing already describes the company as "the leading
online **RETAILER** of books" while carrying the publishing code, so **2731 never described the business at all**
(Form 10-K405 FY1997, Item 1 L226–227, 1998-03-30).
**WHY THEY DIFFER:** the SIC field is **self-selected classification metadata**; Item 1 prose is the company's
description of what it did. A code change evidences what someone typed, not what the company became.
**EVIDENCE WEIGHT:** Item 1's prose in both filings is better evidence of the business. The codes are Tier 1 as
artifacts and near-worthless as classification.
**BEST-SUPPORTED INTERPRETATION:** the SIC change is **weak evidence and must not carry a boundary verdict**. Recorded
because the case for a 1998-12-31 boundary candidate leans on it, and because a reader who accepts it will date a
"change in kind" to a document that only changed a number. Paired with **U.137**, which dates the same field change
inside the June 1998 S-4 pair to a four-business-day interval.
**RESIDUAL UNCERTAINTY:** whether EDGAR or the company selected 2731 — the code's provenance is not in the filing.
**CONFIDENCE:** High (that the codes differ) / **Low (that the difference means what it appears to)**.

**U.124 — "More than $164 million" and $147,787 thousand are both FY1997 numbers, on two different bases.**
**CLAIM A:** FY1997 10-K405: "Through December 31, 1997, the Company had sales of **more than $164 million**" (Form
10-K405 FY1997 L241–242, 1998-03-30). **CLAIM B:** FY1997 annual net sales were **$147,787 thousand** (FY1997 selected
data; ARS 1997) — and $147,758 thousand as first filed (→ U.125).
**WHY THEY DIFFER:** **cumulative-since-inception versus fiscal-year basis, both stated in the same document family.**
They reconcile: `147,787 + 15,746 + 511` plus the 1995 stub periods ≈ **$164 million**, so the two sentences are one
set of numbers viewed from two dates.
**EVIDENCE WEIGHT:** both filed, Tier 1, one lineage.
**BEST-SUPPORTED INTERPRETATION:** carry the cumulative figure **only with the word cumulative** and the annual figure
**only with its fiscal year**. Every derived ratio in this stage uses the annual basis, and §P.2's `t`-items name the
basis in each line. A "1997 revenue" cell holding $164m is a category error, not a discrepancy.
**RESIDUAL UNCERTAINTY:** none material. **CONFIDENCE:** High.

**U.125 — FY1997 net sales and net loss, as filed in 1998 and as restated in 1999: two audited sets.**
**CLAIM A:** FY1997 net sales **147,758** and net loss **(27,590)** (Form 10-K405 FY1997, 1998-03-30).
**CLAIM B:** FY1997 net sales **147,787** and net loss **(31,020)** (Form 10-K FY1998, 1999-03-05).
**WHY THEY DIFFER:** the **PlanetAll pooling-of-interests restatement of all periods**, footnoted in the later
document. The sales gap is $29k (≈ PlanetAll's revenue); the loss gap is **$3,430k**, which is not a pooling
adjustment to revenue at all and which the footnote does not itemise. Two legs, two different mechanisms, one row.
**EVIDENCE WEIGHT:** both Tier-1 **audited at their own dates**. As-filed is the contemporaneous witness; the later
figure is a recast. Neither is a transcription error, and treating the pair as "one number two printings" is how a
$3.4m loss difference disappears from the record.
**BEST-SUPPORTED INTERPRETATION:** **keep the as-filed values as the contemporaneous witness and the later values as
the recast; never print a restated value as if it had been filed.** §P carries the pair side by side, and every Stage-3
ratio that uses an FY1997 denominator names which printing it used. The loss leg is the one that matters for the
adversarial read: a reader who takes (31,020) as the FY1997 result is reading a number no investor ever saw in 1998.
**RESIDUAL UNCERTAINTY:** the PlanetAll contribution is not itemised line by line anywhere, so the (27,590)→(31,020)
bridge is not reconstructable from the filings.
**CONFIDENCE:** High.

**U.126 — FY1997 revenue growth printed as 838% and as 839%.**
**CLAIM A:** **838%** growth in FY1997 net sales over FY1996 (`ARS/97` l.204, 1998-04-17; `10-K405/97` l.1380 prints
"838%"). **CLAIM B:** **839%** (`10-K/98` l.1309, 1999-03-05).
**WHY THEY DIFFER:** the one point is the **$29 thousand** of PlanetAll sales added by the pooling-of-interests
restatement of all periods, divided by a $15,746 thousand base: `29 ÷ 15,746 = 0.184%`, which lands exactly on the
rounding boundary. §P.2 **t3** runs both quotients: 838.4% as filed, 838.6% as restated, which the company rendered
838 and 839.
**EVIDENCE WEIGHT:** both are the company's own arithmetic on its own audited lines; neither is a measurement error,
and the difference is not evidence about 1997 — it is evidence about **which printing of FY1997 is being used**.
**BEST-SUPPORTED INTERPRETATION:** **838% as filed, 839% as restated, and always say which.** And neither is the
multiple: `147,758 ÷ 15,746 = 9.38×`. The Stage-2 lesson at §P.2 s2 (a multiple wearing a percentage's label) repeats
here at a different magnitude, and it is the reason §P195 prints both renderings.
**RESIDUAL UNCERTAINTY:** none material on the arithmetic. **CONFIDENCE:** High.

**U.127 — 3.1 million or 3.3 million customer accounts at 1998-06-30.**
**CLAIM A:** "Through **June 30, 1998**, the Company had sales of more than $367 million to approximately **3.1
million** customer accounts in over 150 countries" (`424B2/98` l.396–397, 1998-08-13 — **contemporaneous**).
**CLAIM B:** "**3.3 million** customer accounts at June 30, 1998" (`8-K(1999-07-21)` l.202, 1999-07-22, repeated in the
Q2-1999 10-Q's comparative — **retrospective**).
**WHY THEY DIFFER:** the dossier that found the pair recorded the reason as "unknown; the record does not say". **This
pass narrows it:** the two figures are eleven months apart, both are company counts, no text in either document
announces a redefinition, and the 3.3m appears in a release comparing year over year — the ordinary place for an
internal restatement of a base period. It is **not** the same event as the 1999 redefinition to "inclusive of Auctions"
accounts (→ U.139), which the company *did* disclose.
**EVIDENCE WEIGHT:** same company, different instruments — a resale prospectus versus a results release; one
contemporaneous, one retrospective. Neither is audited: **customer accounts are never an audited figure.**
**BEST-SUPPORTED INTERPRETATION:** **treat the 1998 figure as contemporaneous and the 1999 figure as its restatement**,
and **build no growth rate without naming the base**. §P225/§P226 print both; §P267 refuses a six-point trend line.
**RESIDUAL UNCERTAINTY:** the size and nature of the definitional change is nowhere disclosed — `3.3 − 3.1 = 0.2
million accounts` is all the record yields. **CONFIDENCE:** UNKNOWN (the cause) / High (that the two figures exist).

**U.128 — Three stock splits in the window; cumulative 12×, not 6×; and one of them is announced nowhere.**
**CLAIM A:** no Form 8-K announces any split after **1998-11-19** (intake manifest 8-K section, read to 1999-10-28).
**CLAIM B:** a **two-for-one** split was paid **1999-09-01** to holders of record **1999-08-12** (`10-Q Q3-1999`
recital; `10-K/99` l.3823–3825; `10-K/A/99` l.2313–2315), approved by the board **1999-07-21** and expressly "not
been reflected" in the Q2 statements (`10-Q Q2-1999` l.652–655).
**WHY THEY DIFFER:** filing practice. A stock dividend paid mid-year was reported in the periodic statement rather than
on Form 8-K, so the **absence of a current report is not the absence of an event** — and a researcher enumerating
events from 8-Ks alone will lose the September split, as this register's own dossier nearly did.
**EVIDENCE WEIGHT:** the 10-Q and 10-K recitals are dispositive; the manifest's negative is a statement about a form
type, not about corporate acts.
**BEST-SUPPORTED INTERPRETATION:** **three splits in the window — 2-for-1 effected 1998-06-01 (record 1998-05-20),
3-for-1 effected 1999-01-04 (record 1998-12-18), 2-for-1 effected 1999-09-01 (record 1999-08-12) — cumulative factor
12× from the mid-1997 basis**, and **72× from the 1995 pre-split basis** (`6 × 12`). §P.2 **t18** shows the
consequence of getting this wrong: every per-share figure moves by 2, and the FY1999 10-K/A's own "18 million IPO
shares" is the visible symptom of a note restated through only two of the three.
**RESIDUAL UNCERTAINTY:** why no 8-K was filed is not a record question and is not answered. **CONFIDENCE:** High.

**U.129 — Q1-1998 net sales printed three ways: 87,375 / 87,395 / 87,361.**
**CLAIM A:** Q1-1998 net sales **87,375** (`10-Q Q1-1998`, 1998-05-15 — contemporaneous). **CLAIM B:** **87,395** in the
FY1998 10-K's quarterly note, and **87,361** as the 1999 comparative in the Q1-1999 10-Q (1999-05-17).
**WHY THEY DIFFER:** pooling restatement (which adds PlanetAll's quarter) **plus** reconciliation of the four quarters
to the audited annual total — two different adjustments pushing in opposite directions, so the three values are not a
trend and not a rounding drift. **Spread: 34 thousand dollars on an 87 million dollar quarter.**
**EVIDENCE WEIGHT:** the FY1998 **quarterly note is the only set that foots to the audited annual lines**, which is a
stronger property than contemporaneity for arithmetic use, and weaker for "what did investors read in May 1998".
**BEST-SUPPORTED INTERPRETATION:** **the note is authoritative for the quarterly series; the 10-Q is authoritative for
contemporaneity. Record both, and never mix them inside one calculation.** No company reconciliation was ever printed
for any quarter of 1998.
**RESIDUAL UNCERTAINTY:** the split between the pooling leg and the reconciliation leg is unknowable locally.
**CONFIDENCE:** High.

**U.130 — Dalzell's 1997 option grant: 125,000 or 750,000 shares.**
**CLAIM A:** 125,000 (`DEF14A/98`, 1998-04-17). **CLAIM B:** 750,000 (`DEF14A/99`, 1999-04-07).
**WHY THEY DIFFER:** **split vintage only** — `125,000 × 3 = 750,000` for the 3-for-1 effected 1999-01-04. Nothing
about the grant changed; the number on the page did.
**EVIDENCE WEIGHT:** both correct on their own basis, both Tier 1, and the 1999 proxy is the later state of the same
disclosure family rather than an independent statement.
**BEST-SUPPORTED INTERPRETATION:** **one grant in two vintages; not comparable, and not an error.** This is the model
case for the whole of §U's Stage-3 restatement cluster: the two figures must never be averaged, never "corrected", and
never used as evidence of an increase in executive compensation. §P234 and §P.2 t18 exist so that a reader can tell
which vintage any per-share number is in.
**RESIDUAL UNCERTAINTY:** none. **CONFIDENCE:** High.

**U.131 — Long-term debt at 1998-12-31: 348,140, 348,824 or "$349 million".**
**CLAIM A:** **348,140** (`10-K/98` Item 6 l.1264, 1999-03-05). **CLAIM B:** "**$349 million** of outstanding senior
indebtedness" (`S-3_FileNo-333-74435`, 1999-03-16, eleven days later).
**WHY THEY DIFFER:** rounding plus a definitional difference — the Item 6 line is captioned **long-term** debt and
appears to exclude the **684** current portion, so the total indebtedness is 348,824 and "$349 million" is its rounded
form. **The three numbers are one fact at three cuts; none is wrong and none alone is complete.**
**EVIDENCE WEIGHT:** same corporate record, two instruments, eleven days.
**BEST-SUPPORTED INTERPRETATION:** **$348.1M as the long-term-debt line, $348.8M including current portion, $349M the
rounded total** — and any §P or §R cell quoting one of them names which. The summary line's composition is **not
footnoted**, which is why this is registered rather than resolved.
**RESIDUAL UNCERTAINTY:** whether the S-3 summary line's "$349 million" also excludes or includes other items (e.g.
capital leases, which appear in the FY1999 supplemental disclosures at $25,850).
**CONFIDENCE:** Medium.

**U.132 — The 8-A12G's prospectus dated "April 21, 1996": the same defect found twice.**
**CLAIM A:** the prospectus registered by the 8-A12G is dated **April 21, 1996** (Form 8-A12G acc.
0000891020-97-000704, 1997-05-02). **CLAIM B:** the registration statement was filed **1997-03-24** and Amendment
No. 1 is dated **1997-04-21** (S-1 lineage).
**WHY THEY DIFFER:** an internal impossibility in the 8-A12G text — **1996 is a misprint for 1997** — and the
surrounding dates settle it: a document cannot be contained in a filing that pre-dates it by eleven months.
**EVIDENCE WEIGHT:** the surrounding dates. **The year digit is the error, not the day and month**, which is why a
reader who checks "April 21" and not "1996" is not protected.
**BEST-SUPPORTED INTERPRETATION:** **never cite the 8-A12G for a 1996 date.** This row is kept as a separate
registration from **U.121** because the finance dossier and the chronology dossier found it independently, and method
§14 rule 7's recovery instruction is to keep both detections rather than silently collapse them — **two finders, one
defect, two rows**, so that a later reader sees the defect was reached twice.
**RESIDUAL UNCERTAINTY:** none. **CONFIDENCE:** High.

**U.133 — FY1997 loss per share: (1.27), (0.24) and (0.12) on 21,651, 130,341 and 260,682 shares.**
**CLAIM A:** FY1997 EPS **$(1.27)** pro forma on **21,651** thousand shares (`10-K405/97` l.1194, l.1877–1881,
1998-03-30). **CLAIM B:** FY1997 EPS **$(0.24)** on **130,341** thousand (`10-K/98` l.1244–1247, 1999-03-05) — and
**$(0.12)** on **260,682** in the FY1999 10-K (l.1763–1766).
**WHY THEY DIFFER:** **the denominator construction changed twice while the loss itself moved only once.** The first
change is from a **pro forma pre-IPO basis** (21,651 thousand) to a **weighted-average post-IPO basis restated for
splits** (130,341); the second is purely the September 1999 2-for-1 (`130,341 × 2 = 260,682` and `0.24 ÷ 2 = 0.12`
exactly — the §P.2 t20 signature).
**EVIDENCE WEIGHT:** both are the company's own presentations, each internally consistent, all three Tier 1.
**BEST-SUPPORTED INTERPRETATION:** **these are different instruments, and the year-over-year EPS change is not
interpretable.** No §P or §R row in this part presents an EPS trend line across 1996–1999; §P194 prints the triple with
its three share denominators attached. Where a per-share figure must be used, the basis is named.
**RESIDUAL UNCERTAINTY:** none on the arithmetic; the pro forma construction's exact composition is not reconciled in
the FY1997 filing. **CONFIDENCE:** High.

**U.134 — "Up to 400,000 supplied by distributors" against a 4.7-million-title catalogue: the fill question never answered.**
**CLAIM A:** "**up to 400,000** [titles] are currently supplied by book distributors" (424B1 final prospectus,
1997-05-15 — the certified offering statement, and Stage 2 §P.2 s15's basis for the 16.0%/84.0% split).
**CLAIM B:** FY1998: **no fillable-pool figure at all**; the catalogue is "more than **4.7 million** … titles"
(`10-K/98` l.214, l.283, 1999-03-05).
**WHY THEY DIFFER:** the ceiling sentence was an **offering certification** and was not renewed outside offering
documents. The company kept the catalogue number and dropped the fill number — which is a disclosure act, not evidence
that availability was solved. Inventory did rise ($8,971k → $29,501k), and direct purchasing from manufacturers and
labels began in 1998, so **a mechanism for improvement is disclosed** even though no metric of it is.
**EVIDENCE WEIGHT:** the certified 1997 sentence is the stronger instrument as a statement of a limit; the 1998 filing
is the stronger statement of what the company chose to disclose afterwards.
**BEST-SUPPORTED INTERPRETATION:** **availability improved via the company's own inventory and direct purchasing, not
via any published fillable-pool number** — and the 84% tail's shippability remains unmeasured. §P232/§P237 therefore
quote titles and inventory but print **no fill rate**, and §P.2 "Not computed" (ii) records the missing denominator.
**RESIDUAL UNCERTAINTY:** whether the tail became shippable. **No fill rate exists at any date in the stage.**
**CONFIDENCE:** High.

**U.135 — Ingram's share of 1997 purchases: 58% or "approximately 60%".**
**CLAIM A:** Ingram "accounted for **58%** and 59% of the Company's inventory purchases in 1997 and 1996,
respectively" (`10-K405/97` l.1669–1670, 1998-03-30). **CLAIM B:** the FY1998 10-K states Ingram accounted for
"**approximately 60%**" of 1997 purchases and "**approximately 40%**" of 1998 (`10-K/98` l.422, l.797–799, l.2374–2377,
1999-03-05).
**WHY THEY DIFFER:** the later document either rounds to the nearest ten or restates the basis. **A defect caught and
re-set on this pass** (§P.2a): one Stage-3 reading put "~60%" on **FY1998**, which would have said concentration **rose**
in the year it fell — a reversal of the finding. The filed pairing is 58/~60 for **1997** and ~40 for **1998**.
**EVIDENCE WEIGHT:** the contemporaneous FY1997 filing's 58% is the more precise statement; the FY1998 10-K's ~40% for
1998 is its own-year figure and is not in dispute with anything.
**BEST-SUPPORTED INTERPRETATION:** **use 58% for 1997, print the FY1998 rounding beside it, and use ~40% for 1998.**
And say plainly that `0.58 × (purchases)` is **UNKNOWN**: no purchase total is filed in any year, so no Ingram dollar
volume exists in this corpus (§P.2 "Not computed" (vi)). The more important 1998 fact is not the percentage at all:
**Barnes & Noble announced it would buy Ingram**, and Amazon disclosed that as a risk factor.
**RESIDUAL UNCERTAINTY:** whether "approximately" hides a recomputation. **CONFIDENCE:** High.

**U.136 — FY1997 net sales 147,758 or 147,787: the same pair as U.125, from the product side.**
**CLAIM A:** FY1997 net sales **$147,758K** (`10-K405/97`, 1998-03-30). **CLAIM B:** **$147,787K** (`10-K/98` selected
data and income statement, 1999-03-05).
**WHY THEY DIFFER:** a **$29K gap with no reconciling note** on its own; the FY1998 restatement note concerns PlanetAll
pooling of interests and is generic, not line-specific. **U.125 is the same pair seen from the loss line** (−$3,430K,
which the pooling note does not explain either); the two rows are kept separate because the sales leg and the loss leg
have different magnitudes, different explanations available, and different users.
**EVIDENCE WEIGHT:** both audited, at their own dates.
**BEST-SUPPORTED INTERPRETATION:** **carry both; do not average.** Every FY1997 denominator in this part names its
printing, and §P.2 t3 shows the ratio consequence is invisible at one decimal (19.5% either way).
**RESIDUAL UNCERTAINTY:** no note in the corpus reconciles them. **CONFIDENCE:** High.

**U.137 — The SIC code moved twice inside the June 1998 S-4 pair, and the two filings are nine days apart.**
**CLAIM A:** SIC **2731** (books: publishing) on the cover of S-4 File No. **333-55943** (`10-K405/97` l.42 carries the
same code; the S-4's cover repeats it), 1998-06-03. **CLAIM B:** SIC **5961** (retail-catalog & mail-order houses) on
the cover of S-4 File No. **333-56723**, 1998-06-12.
**WHY THEY DIFFER:** registrant-changed cover-page **self-classification**, on two transaction registrations nine days
apart — and because the two S-4s covered different acquisitions (the Junglee shelf vs the European set), the change is
plausibly a different preparer rather than a change of mind.
**EVIDENCE WEIGHT:** both same registrant, both Tier 1; the differential is certain and the motive is not in the
record.
**BEST-SUPPORTED INTERPRETATION:** **the move is dated to a four-business-day interval and never reversed** — and,
paired with **U.123**, it is **weak evidence for a change in kind**: the FY1997 10-K had already called the company an
online **retailer** while carrying the publishing code, so the codes evidence what was typed, not what the company was.
**RESIDUAL UNCERTAINTY:** motive unrecorded. **CONFIDENCE:** High.

**U.138 — "Special value" editions discounted up to 89% or up to 85%.**
**CLAIM A:** special value editions **discounted up to 89%** (`10-Q Q2-1998` l.881–882, 1998-08-14 — and the same 89%
appears at `10-K405/97` l.1416, 1998-03-30). **CLAIM B:** "**discounted up to 85%**" (`10-K/98` l.1361, 1999-03-05).
**WHY THEY DIFFER:** either a policy change between the mid-1998 interim report and the FY1998 annual report, or an
imprecise restatement of a standing description. **The 89% print survives in two documents a year apart, so it is not a
typo.**
**EVIDENCE WEIGHT:** the interim filing is closer to the practice it describes; the annual report is the later state.
**BEST-SUPPORTED INTERPRETATION:** **89% held through mid-1998 (and in the FY1997 description); the FY1998 annual
report prints 85%.** §P233 carries the whole discount architecture (40% featured book **and** music, 30% on >400,000
titles, special value to 89%/85%) as a company description rather than a measured price index.
**RESIDUAL UNCERTAINTY:** the record cannot separate change of practice from change of description.
**CONFIDENCE:** High (that both prints exist) / Low (which describes 1998 pricing).

**U.139 — Customer accounts: 6.2 million on one basis, 10.7 and 13.1 million on another, over 17 million on a third.**
**CLAIM A:** FY1998: "approximately **6.2 million** and 1.5 million cumulative customer accounts as of December 31,
1998 and 1997" (`10-K/98` l.1317, 1999-03-05) — **no qualifier**. **CLAIM B:** 1999: "**10.7 million** … (including
accounts with Amazon.com Auctions)" at 1999-06-30 and **13.1 million** on the same express basis at 1999-09-30
(`10-Q Q2-1999` l.862, `10-Q Q3-1999` l.871), then "**over 17 million** customer accounts" (`10-K/99` l.198).
**WHY THEY DIFFER:** **the metric's composition changed in 1999 — in the same year it grew fastest — and the company
disclosed the change parenthetically rather than as a restatement.** An auction account and a buying account are the
same word and different populations.
**EVIDENCE WEIGHT:** both company self-reports, neither audited, and the 1999 parenthetical is the company's own
witness that the series broke.
**BEST-SUPPORTED INTERPRETATION:** **no subtraction across the 1998/1999 boundary is valid without the tag.** §P267
prints the seven endpoints with their bases and prints **no growth rate** through the break; §P247 carries the 17m
"over 150 countries" figure with the basis attached. This is also why §P.2 "Not computed" (viii) refuses a
customer-acquisition cost: the denominator's definition moved.
**RESIDUAL UNCERTAINTY:** the auction-only component is never published, so the pre-break series cannot be reconstructed
even after the fact. **CONFIDENCE:** High.

**U.140 — Repeat purchase: six values on at least four bases, and one matched pair.**
**CLAIM A:** "repeat customers account for **over 40% of orders**" (cumulative basis, 1996-12-31, S-1 lineage via Stage
2 §P89). **CLAIM B:** "**over 46%** in the fourth quarter of 1996 [to] **over 58%** in the same period in 1997"
(`ARS/97` l.210–211, 1998-04-17; reproduced `ARS/98` l.440); and 1998 alone adds "**over 62% of orders** in the six
months ended June 30, 1998" (`424B2/98` l.398) and "**over 60%** of orders placed … during the fiscal year ended
December 31, 1998" (`10-K/98` l.1318–1320).
**WHY THEY DIFFER:** **different periods and probably different denominators** — a cumulative-1996 wording, a
quarter-on-quarter pair, a half-year, and a full year, all using the words "repeat customers" and "orders", **neither
of which is defined in any accession at any date.**
**EVIDENCE WEIGHT:** the **Q4-to-Q4 pair is the only matched comparison the company itself makes**, and it is the only
one that can be read as a trend.
**BEST-SUPPORTED INTERPRETATION:** **use the matched Q4 spine (46% → 58%); treat every other value as an unmatched
level.** §P207 prints the pair; §R Customers prints all six with their periods; **no §P row computes a repeat-purchase
"improvement" from 40% to 60%**, which would be a 20-point claim built on two incompatible bases.
**RESIDUAL UNCERTAINTY:** no definition of "repeat", "order" or the look-back window exists anywhere in the corpus —
carried forward from Stage 2 U.48, where the same defect first appeared. **CONFIDENCE:** High.

**U.141 — "2.5 million titles" and "4.7 million titles" are not the same count.**
**CLAIM A:** FY1997: "searchable catalog of more than **2.5 million titles**", where titles meant "**primarily books**
but also a smaller number of CDs, videotapes and audiotapes" (`10-K405/97` l.291, l.2094; definition carried from
Stage 2 §P179). **CLAIM B:** FY1998: "more than **4.7 million** book, music CD, video, DVD, computer game and other
titles" (`10-K/98` l.214, l.283).
**WHY THEY DIFFER:** **the object of the count was widened as well as grown.** FY1998's 4.7m includes categories that
did not exist as Amazon stores in FY1997, so part of the 2.2m increase is definitional and part is assortment — in
unknown proportions.
**EVIDENCE WEIGHT:** both audited annual reports; both use the same word.
**BEST-SUPPORTED INTERPRETATION:** **the growth is not like-for-like, and this part prints no titles-growth multiple.**
§P232 carries the definition inside the cell. By FY1999 the same table says "**over 13 million titles** in books, …"
(`10-K/99` l.305), a third object again, which is why §R Product lists the counts **with** their definitions rather
than as a series.
**RESIDUAL UNCERTAINTY:** how much of the change is definition and how much assortment.
**CONFIDENCE:** High.

**U.142 — Amazon.com Cards described before it was launched.**
**CLAIM A:** the **Q1-1999** 10-Q describes a **free electronic greeting card service** as part of the offer, in the
quarter ended 1999-03-31 (1999-05-17). **CLAIM B:** the **Q3-1999** 10-Q states "**In April 1999**, the Company
launched Amazon.com Cards, a free electronic greeting card service" (l.795, 1999-11-15).
**WHY THEY DIFFER:** an interim report describing in Q1 a service the later report dates to April — i.e. to the second
quarter. Either something greeting-card-like was live before the named launch, or the Q1 description was
forward-looking and reads as present-tense.
**EVIDENCE WEIGHT:** both the registrant's own filings, both Tier 1, neither audited; the Q3 statement is the later and
the more specific ("launched … in April 1999"), the Q1 text is the closer to the event.
**BEST-SUPPORTED INTERPRETATION:** **something greeting-card-like existed before the named April launch**, and §Q dates
Cards to **April 1999 with the Q1 description carried in-cell** rather than silently moving the row to Q1.
**RESIDUAL UNCERTAINTY:** what exactly existed before April 1999 — no document says, and no archived page survives to
check it (§S row 17). **CONFIDENCE:** Medium.

**U.143 — "Number one online music seller", and the quarter that shows $14.4 million.**
**CLAIM A:** FY1998: Amazon "became the **number one online music seller**" (`10-K/98` Item 1, 1999-03-05) — a ranking,
with **no competitor figure and no basis stated**. **CLAIM B:** the company's own Q3-1998 results release states
**third-quarter music sales of $14.4 million** (`8-K(1998-10-28)`, 1998-10-28).
**WHY THEY DIFFER:** the annual report **keeps the claim and drops the number**; the release **carries the number and
does not need the ranking**. The two are not contradictory, but only one of them is checkable, and the checkable one is
not the one that was repeated.
**EVIDENCE WEIGHT:** the release with the number is the better evidence of performance; the annual report is the better
evidence of what the company wanted to assert. **No competitor music figure exists locally**, so the ranking is
unverifiable from this corpus — the point is not that it is false but that **it is unsupported here**.
**BEST-SUPPORTED INTERPRETATION:** **record $14.4 million as the company's unaudited figure and the ranking as its own
claim, never as a measurement.** §P228 prints both cells; §R Competitors refuses to use the ranking as evidence of a
category win, and §S records that the competitor filings that could test it were not retrieved in this pass.
**RESIDUAL UNCERTAINTY:** the basis of the ranking (units? revenue? which market? which quarter?).
**CONFIDENCE:** High (both statements) / **UNKNOWN (the ranking's basis)**.

**U.144 — "No long-term contracts … with ANY of its vendors" becomes "with MOST of our vendors".**
**CLAIM A:** FY1997 / S-1/A No. 5: the company "has **no long-term contracts or arrangements with any of its vendors**
that guarantee the availability of merchandise, the continuation of particular payment terms or the extension of credit
limits" (`10-K405/97` l.1671–1673, 1998-03-30; same wording in the 1997 lineage). **CLAIM B:** FY1998: the same sentence
reads "**most** of our vendors" (`10-K/98`, 1999-03-05).
**WHY THEY DIFFER:** the quantifier relaxed, which entails that **some vendor relationship became contractual** between
March 1998 and March 1999. The differential is a disclosure fact and is certain.
**EVIDENCE WEIGHT:** the differential itself is certain; **nothing else about it is.** No supply or distribution
agreement is filed as an exhibit anywhere in the stage, and no accession names the vendor.
**BEST-SUPPORTED INTERPRETATION:** **something was contracted, and the record does not say what.** This is the rare
case where a single word's change is the most informative evidence in a filing year: the company's supply position
improved by at least one contract, at the exact moment its largest supplier was being bought by its largest competitor
(→ U.135), and the company disclosed the relaxation without disclosing the instrument.
**RESIDUAL UNCERTAINTY:** which vendor, what terms, when. **UNTRIED** at §S row 6.
**CONFIDENCE:** High (the differential) / UNKNOWN (everything else).

**U.145 — Depreciation and amortisation printed twice for both FY1997 and FY1998.**
**CLAIM A:** FY1997 **3,388** and FY1998 **9,692** (`10-K405/97` l.2037, 1998-03-30; `10-K/98` l.2232, 1999-03-05 —
each the **own-year** cash-flow add-back). **CLAIM B:** FY1997 **3,442** and FY1998 **9,421** (`10-K/99` l.2820,
2000-03-23 — both as **comparative** columns; identical in `10-K/A/99` l.1291).
**WHY THEY DIFFER:** comparative-column reclassification in the later report — **+54** on FY1997 and **−271** on
FY1998, in opposite directions, which is the signature of an amount moved **between** years rather than added to the
asset base. **No reconciling note exists for either leg** (§S row 5).
**EVIDENCE WEIGHT:** the FY1999 report is **audited once against both years**, which makes its internal pair
self-consistent; the earlier figures are audited against their own year and were never re-audited together.
**BEST-SUPPORTED INTERPRETATION:** **use the FY1999 restated series for any two-year comparison, and print the
as-filed value beside it whenever a 1997 or 1998 figure is quoted as the company reported it.** §P196/§P197 and §P213/
§P243 do exactly that, and §P.2 **t4** adds the warning that the printed figure is a **cash-flow add-back**, not the
income-statement charge: pairing it with gross fixed assets to compute an average life is a category error. **The
consequence the register must not lose: there is no single filed depreciation figure for 1997 or 1998** (→ U.158).
**RESIDUAL UNCERTAINTY:** the composition of both differences is unknowable locally. **CONFIDENCE:** High.

**U.146 — Stock options outstanding at 1997-12-31: 27,332 or 54,664 thousand.**
**CLAIM A:** **27,332** thousand at a weighted-average exercise price of **$1.502** (`10-K/98` l.2991, 1999-03-05).
**CLAIM B:** **54,664** thousand at **$0.751** for the same date (`10-K/99` l.3886; `10-K/A/99` l.2377, 2000-03-23).
**WHY THEY DIFFER:** the retroactive application of the **2-for-1 split effected 1999-09-01**, which the earlier report
could not reflect because it was filed eight months before the split.
**EVIDENCE WEIGHT:** both audited, and **the cause is stated on the record** — which makes this the cleanest of the
Stage-3 restatement conflicts and the one that can be closed **by instrument rather than by judgement**.
**BEST-SUPPORTED INTERPRETATION:** **resolved: it is a vintage difference, not double counting.** The test that settles
it is arithmetic and exact — `27,332 × 2 = 54,664` **and** `1.502 ÷ 2 = 0.751` (§P.2 **t20**). **A real doubling of the
option population would not have halved the weighted-average exercise price**; the inverse movement of price and count
is the split's fingerprint. **Summing or averaging the two would manufacture 81,996 thousand options that never
existed**, and the 1999-09-01 split is itself undocumented on any Form 8-K (→ U.128), which is how a reader working
from current reports alone would reach the wrong side of this pair.
**RESIDUAL UNCERTAINTY:** none material. **CONFIDENCE:** High.

**U.147 — Gross fixed assets at 1997-12-31: 12,899 or 13,490; net 9,265 or 9,726.**
**CLAIM A:** FY1997's own report: gross **12,899**, accumulated **3,634**, net **9,265** (`10-K405/97` l.2300–2308,
1998-03-30). **CLAIM B:** the FY1998 10-K's comparative for the same date: gross **13,490**, net **9,726** (l.2750–2753,
1999-03-05).
**WHY THEY DIFFER:** late capital additions or reclassification arriving **across every line** (+591 gross, +130
accumulated, +461 net) with **no note**. §P.2 **t5** notes the signature: accumulated depreciation rises by only 130
while gross rises by 591, which points to **additions reclassified in**, not depreciation reclassified out.
**EVIDENCE WEIGHT:** own-year versus comparative — but **this pass found a third witness that the dossier did not**: the
**8-K of 1998-08-27 already prints 13,490 for 1997** (l.1485, l.2327), seven months before the FY1998 10-K, so the
higher figure was in the public record during 1998 and the ordering explanation "own-year beats comparative" is not the
whole story. **Also note the filing's own component table sums to 12,900 against its printed total of 12,899** (§P.2 t5)
— a one-dollar rounding, recorded rather than "fixed".
**BEST-SUPPORTED INTERPRETATION:** **use the own-year printing (12,899/9,265) when citing what FY1997 reported, and the
comparative (13,490/9,726) when building the 1997→1998→1999 curve, because only the latter is on the same basis as
FY1998's own 43,585/29,791.** Cause not disclosed either way.
**RESIDUAL UNCERTAINTY:** which of the four asset classes the +591 sits in. **CONFIDENCE:** High.

**U.148 — "Eight new distribution centres ≈ four million square feet" and "eight US distribution centres ≈ 3.8 million square feet", in one document.**
**CLAIM A:** FY1999 Item 1 narrative: the six named new US sites (Fernley NV, Coffeyville KS, **Campbellsville KY,
Lexington KY**, McDonough GA, Grand Forks ND) plus the UK and German centres — "**these eight new distribution centers
comprised approximately four million square feet**" (`10-K/99` l.568–573). **CLAIM B:** FY1999 Item 2 properties
schedule: "**eight distribution centers** located in Seattle, Washington; New Castle, Delaware; Fernley; Lexington;
Campbellsville; McDonough; Coffeyville; Grand Forks … **approximately 3.8 million square feet**" (l.1602–1605).
**WHY THEY DIFFER:** **"eight" counts two different sets.** Claim A's eight = the 1999 **increment** (six US new + two
European). Claim B's eight = the **US estate** (the 1999 US additions + the two pre-existing Seattle and Delaware
centres), European sites excluded and stated separately as "additional properties in Europe".
**EVIDENCE WEIGHT:** same document, Item 1 narrative versus Item 2 schedule; nothing external adjudicates and nothing
needs to, because the two sets are internally distinguishable — **but only if read together.**
**BEST-SUPPORTED INTERPRETATION:** **3.8M sq ft is the US estate; ~4M sq ft is the 1999 increment; the two are never
summed and never averaged.** §R Distribution prints both with their set definitions. **Residual: the square footage of
the pre-existing Seattle and Delaware sites inside the "new" narrative total is unstated**, so the increment cannot be
checked against the estate — recorded at §S row 15. **This pair is also the only place in the corpus that names TWO
Kentucky sites, which is the evidence that resolves U.117's double-listing.**
**RESIDUAL UNCERTAINTY:** footage of pre-1999 sites inside the "new" total. **CONFIDENCE:** High.

**U.149 — FY1998 net sales: 609,996 or 609,819.**
**CLAIM A:** **609,996** (`10-K/98` l.1222, l.1309, l.2016, 1999-03-05 — audited, own-year). **CLAIM B:** **609,819**
(`10-K/99` l.1732, 2000-03-23; identical in `10-K/A/99` l.173).
**WHY THEY DIFFER:** a **$177K restatement with no reconciling note.** It is **not** the PlanetAll pooling: that added
**+29** to FY1997, whereas FY1998 moves **down** by 177, so a different mechanism is at work.
**EVIDENCE WEIGHT:** audited in both, at their own dates.
**BEST-SUPPORTED INTERPRETATION:** **carry both printings; ratios are unchanged at one decimal.** §P.2 **t7** does the
work the note does not: cost of sales is **identical** in both printings (476,155), so `133,841 − 177 = 133,664` exactly,
which **proves the Δ is confined to the revenue line** rather than spread across a reclassification — arithmetic, not a
note. FY1998 gross margin is 21.9% on either basis.
**RESIDUAL UNCERTAINTY:** cause unknown; the sign rules out the pooling explanation the register otherwise reaches for.
**CONFIDENCE:** High.

**U.150 — FY1997 technology spend printed three ways: 12,485, 13,916 and 13,384.**
**CLAIM A:** product development **12,485** (`10-K405/97` l.1183, 1998-03-30). **CLAIM B:** product development
**13,916** as the FY1998 comparative (`10-K/98` l.1228, 1999-03-05) — and **technology and content 13,384** as the
FY1999 comparative (`10-K/99` l.1738, 2000-03-23).
**WHY THEY DIFFER:** **two mechanisms at once.** The first is the pooling restatement plus reclassification (+1,431);
the second is a **caption change** — "technology and content" absorbs **acquired content** that "product development"
never held, and simultaneously the FY1999 report carved stock-based compensation into its own line, taking **532** out
of the technology figure (§P.2 **t2b**: `409 + 532 + 270 = 1,211` exactly).
**EVIDENCE WEIGHT:** **three audited printings, one object that is not the same object in the third.** Total operating
expenses are preserved at 61,413 across both later printings while the composition moves, which is the arithmetic proof
that the later pair is a recaption rather than new spending.
**BEST-SUPPORTED INTERPRETATION:** **there is no single filed technology-spend value for 1997 — name the document with
the number, every time.** §P189/§P190/§P191 print all three decompositions; §P217 shows FY1998 suffering the same
fate (46,807 as "product development" vs 46,424 as "technology and content"). **This row is the evidence base for
U.158**, which states the general finding.
**RESIDUAL UNCERTAINTY:** the acquisition/expense split behind 13,384 is not disclosed. **CONFIDENCE:** High.

**U.151 — "Seven distribution centers nationwide" claimed, five certified as opened.**
**CLAIM A:** the 8-K release of 1999-07-21: "by the busy 1999 holiday shopping season, Amazon.com customers will
benefit from nearly **4 million square feet** of space at **seven distribution centers nationwide**—**more than 10
times the distribution center floor space the company had in 1998**" (l.311–317). **CLAIM B:** the Q3-1999 10-Q:
"During the nine-month period ended September 30, 1999 the Company **opened** new distribution centers in Nevada,
Georgia, Kentucky, Kansas and North Dakota" — **five** (l.830–831).
**WHY THEY DIFFER:** press-release counting includes leased, announced or non-DC facilities, and the claim is
**forward-looking to the holiday season** ("by the busy 1999 holiday shopping season…"), while the 10-Q certifies only
sites **opened** by a stated date. The 10-Q's verb discipline ("opened") is the reason the two differ.
**EVIDENCE WEIGHT:** **the 10-Q governs the count.** The release is Tier 1 as an artifact and weak as a measurement:
its own definition of a "distribution center" is unstated, and its "10 times" has no denominator in any filing.
**BEST-SUPPORTED INTERPRETATION:** **treat the multiplier and the "seven" as company claims; treat five as the filed
fact.** §P255 prints both in one row with their verbs. By 1999-12-31 the FY1999 10-K's own Item 2 list reaches **eight
US sites** (→ U.148), so the release's "seven" was directionally right about the estate and wrong about what a periodic
report would certify. **This is the clearest example in the stage of the gap between what the company announced and
what it would sign for.**
**RESIDUAL UNCERTAINTY:** the release's own definition of a distribution centre. **CONFIDENCE:** Medium.

**U.152 — The intake manifest labelled the Buschman agreements as marketplace contracts; the exhibits say otherwise.**
**CLAIM A:** five 1999-03-11 "Sales Agreements" are a marketplace-contract set (`STAGE3_INTAKE_MANIFEST.md`, periodic
spine note, read 2026-09-25). **CLAIM B:** they are agreements "by and between Amazon.com, Inc. and **The Buschman
Company**" — five exhibits to one 10-Q, with confidentially treated terms (`10-Q Q1-1999` EX-10.1–10.5, l.1660–1669,
1999-05-17), and the counterparty is the **same single company in all five**.
**WHY THEY DIFFER:** **an intake label written before the exhibits were opened.** The manifest describes itself as "a
retrieval record, not an interpretation", and this label crossed that line by inferring subject matter from a document
type.
**EVIDENCE WEIGHT:** **the primary instrument wins.** Paired with **U.114**, which reaches the same conclusion from the
chronology dossier's independent detection — two finders, one defect.
**BEST-SUPPORTED INTERPRETATION:** **the instrument governs; the manifest label is retired.** The five Buschman
agreements are best read as a **materials-handling or equipment purchase series** — a supplier taking five separate
orders on one date fits a fulfilment build-out, and 1999 is the year of the 4 million sq ft programme — **but that
reading is an INFERENCE and the filed terms are confidential, so the subject matter stays UNKNOWN** (§P.2 "Not
computed"; §S row on confidential treatment). **What is settled is the negative: the marketplace's contractual trace is
not in these exhibits.**
**RESIDUAL UNCERTAINTY:** none on the mislabelling; total on the subject matter. **CONFIDENCE:** High.

### New registrations from this pass (U.153 → U.168)

**These fifteen rows are registered here, not inherited.** Each was found by reading the Stage-3 corpus against the
claims the dossiers and the instruction layer make, and **each is emitted once as a `conflicts.csv` row in the append
block below**, so that `§U ↔ conflicts.csv` remains 1:1 across all 55 Stage-3 blocks.

**U.153 — Where does Stage 3 end: 1997-12-31, 1999-06-30, 1999-09-30, or 1999-12-31 — and the falsified test offered for one candidate.**
**CLAIM A:** Stage 3's transition is evidenced by the **first filing that uses the verb "opened"** for a distribution
centre outside Washington, on the chronology dossier's dating argument for its candidate boundary (2026-09-25 dossier
reading). **CLAIM B:** the corpus contains **three earlier "opened" sentences**: (i) `10-K405/97` l.1646–1648, 1998-03-30
— "**In November 1997 the Company opened a 200,000-square-foot distribution center in Delaware** and expanded its
Seattle distribution center to 85,000 square feet"; (ii) `ARS/98` l.160, 1999-04-07 — "**We opened** distribution and
customer service centers in the U.K. and Germany"; (iii) `10-Q Q1-1999` l.592 and again at l.915, 1999-05-17 — "A new
distribution center was leased and **opened** in Nevada during the quarter" / "During the first quarter, the Company
leased and **opened** a distribution center in Nevada."
**WHY THEY DIFFER:** the test proposed for the boundary is a **string test that its own corpus refutes**: the verb
appears in FY1997, FY1998 and Q1-1999 documents, so whatever the boundary argument needs, it is not supplied by the
first use of "opened". **The falsification is total, and it is checkable in three greps.**
**EVIDENCE WEIGHT:** Claim B is the filed text of the documents Claim A's argument relies on. **A dating heuristic
cannot outweigh the filings it claims to read.**
**BEST-SUPPORTED INTERPRETATION:** **the boundary is a judgement about what changed, not a discovery about what a
document says, and the corpus supports four defensible candidates.** Stated as this part's position:
**1997-12-31** is the strongest *substantive* sub-endpoint — the first non-Washington centre, the first term loan, the
first audited year of the retailer's own margin compression, and the year the sales-tax risk factor disappeared — and
Stage 3 should be **readable** as ending there. **1999-09-30** is the last date the *interim* record describes on its
own terms (five DCs opened, three marketplaces live, six acquisitions, Galli and Jenson installed, before the Q4
depreciation spike of §P242). **1999-12-31**, which this part runs §Q to, is the widest defensible endpoint and the one
the intake executed. **1999-06-30** has the weakest claim: the convertible and the shelf are financing events, and
financing does not by itself change what the company was. **No candidate is asserted as correct; the choice is
disclosed.**
**RESIDUAL UNCERTAINTY:** permanently unresolved on the record — **no company document states a stage boundary**, and
the §2 firewall forbids choosing the endpoint by looking forward from it.
**CONFIDENCE:** High (that the "first 'opened'" test is falsified) / **Medium and unresolved (which endpoint to
adopt)**.

**U.154 — The FY1999 10-K/A flips FY1998's change in cash from +23,685 to (38,536).**
**CLAIM A:** FY1998 showed a **net increase in cash of 23,685** (`10-K/98` l.2267, 1999-03-05; repeated as the FY1998
comparative in `10-K/99` l.2867, 2000-03-23), with FY1999 at **+91,401** and FY1997 at **+1,012**.
**CLAIM B:** the 10-K/A prints **"Net increase (decrease) in cash and cash equivalents" of 61,726 (1999), (38,536)
(1998), 103,830 (1997)** (`10-K/A/99` l.1338, 2000-09-08), with beginning balances rewritten from 1,876/25,561 to
110,119/71,583.
**WHY THEY DIFFER:** **a policy change, not a correction of error.** The explanatory note is explicit (l.94–100): the
amendment "reflects certain changes previously reported in our quarterly report on Form 10-Q for the period ended
**June 30, 2000**", in which the company "modified our accounting policy relating to the classification of cash
equivalents" — effective **April 1, 2000**, all instruments with original maturity of three months or less are cash
equivalents, where before they were marketable securities (l.1448–1456). **And the same note states the aggregate did
not move: "THE AGGREGATE TOTAL OF CASH EQUIVALENTS AND MARKETABLE SECURITIES HAS NOT CHANGED FROM AMOUNTS PREVIOUSLY
REPORTED."** Ernst & Young's report carries the corresponding emphasis paragraph (l.976–978).
**EVIDENCE WEIGHT:** both audited; the amendment is the later state of **the same instrument**, so under method §3 this
is one document twice, not two confirmations — **but the two states disagree violently on a headline liquidity
line.**
**BEST-SUPPORTED INTERPRETATION:** **the 1998 company did not burn cash and the 1999 company's restatement is not
evidence that it did; the sign changed because the definition of the line changed.** Both printings are carried at
§P245 with their documents, and the swing is named: **+23,685 → (38,536) is a 62,221 movement on a 1998 year whose net
loss never moved at all (124,546 in both)** — which is the arithmetic proof that no economic fact changed. The FY1997
leg (+1,012 → +103,830) and the FY1999 10-K/A balance-sheet pair (cash 116,962 → cash-and-equivalents 133,309 with
marketable securities 589,226 → 572,879) are the same reclassification at the other two dates (§P.2 **t24**).
**RESIDUAL UNCERTAINTY:** whether the amendment changed anything a reader should treat as economically real —
**the company's own note says no.**
**CONFIDENCE:** High.

**U.155 — zShops: "late September 1999" twice, "October 1999" once, and "November 1999" for the sites the 10-Q puts in October.**
**CLAIM A:** "**In late September 1999**, the Company introduced three e-commerce innovations: **zShops**, which
enables anyone to offer merchandise for sale on Amazon.com; Amazon.com Payments …; and All Products Search"
(`10-Q Q3-1999` l.801–806, filed 1999-11-15), and "**In late September, Amazon.com introduced zShops**"
(`8-K(1999-10-28)` l.298, event 1999-10-28) — **two documents, eleven days apart in reporting terms, both saying late
September**, and the second of them **contemporaneous** with the event.
**CLAIM B:** the FY1999 10-K's launch table: "**zShops … October 1999**" and "**UK and German zShops … November
1999**" (`10-K/99` l.277, l.280).
**WHY THEY DIFFER:** three company dates for what look like two events. **And the Q3 10-Q contradicts the table's third
leg directly:** "In **October** 1999, the Company launched Amazon.com Anywhere … and **expanded its music, auctions, and
zShops offerings to Germany and the United Kingdom**" (l.808–812) — October for the very expansion the FY1999 table
dates to November. Two candidate mechanisms, neither documented: the table may date the **US** launch by the month the
company's own release called "late September", and it may date the **European** launch by completion of a phased
rollout rather than by first availability.
**EVIDENCE WEIGHT:** for the US launch, **two contemporaneous documents saying late September outweigh one annual
table**; for the European rollout, the interim report is contemporaneous and the table is a summary compiled in March
2000.
**BEST-SUPPORTED INTERPRETATION:** **enter zShops in §Q at "late September 1999" with the table's October print carried
in-cell, and record that the company gave its own flagship marketplace launch three dates across four documents.**
Nothing is computed from the date, and no launch-day precision is claimed: the day is **EMPTY** (§S row 10). **This
conflict matters for more than tidiness** — zShops is the object that changes the composition of the net-sales line
(→ U.160), so a stage that dated it wrongly would misattribute a quarter of marketplace revenue.
**RESIDUAL UNCERTAINTY:** the day; whether October marks a general-availability date; whether the UK/German date is a
launch or a completion.
**CONFIDENCE:** High (each text) / **Medium (that "late September 1999" is the right US date)** / UNKNOWN (the day).

**U.156 — Exchange.com is a filed 1999 acquisition; WarehouseDirect, Internet Mail and Allaire are absent from every document in the corpus.**
**CLAIM A:** Amazon acquired **Exchange.com** in 1999 — and the record is unusually strong: the Q1-1999 10-Q names
"**e-Niche Incorporated ('Exchange.com')**" among the announced acquisitions (l.532, l.601), the Q3-1999 10-Q recites
Exchange.com among the nine-month announcements (l.820–822), and **Note 2 of the FY1999 10-K/A files the completed
transaction**: "On **May 14, 1999**, the Company completed its acquisition of Exchange.com, a developer of Internet
marketplaces and related online communities… issued **1,893,944** shares… approximately **$145 million** purchase price…
**may be required to issue additional shares with a value of up to $27.5 million** one year after the acquisition date
dependent on certain performance goals" (l.1729–1741). **CLAIM B:** **WarehouseDirect, Internet Mail and Allaire return
zero occurrences across every file in `sources/`** — machine-checked this pass over all 95 text files, including the FY1999
10-K and 10-K/A, all eight 10-Qs and all 26 8-K items.
**WHY THEY DIFFER:** one leg is an audited note with a date, a share count, a price and an earn-out; the other legs are
**absent**, and absence in this corpus is a **window** statement, not a refutation: Note 2 names six completed 1999
acquisitions (e-Niche/Exchange.com, Accept.com, Alexa, LiveBid, Tool Crib/Acme Electric Motor, Back to Basics Toys) and
says "**and other acquisitions**", so the list is complete for what was **material in 1999** and silent about 2000.
**EVIDENCE WEIGHT:** **the filed list controls inside the window.** Nothing about the three absent names is evidence
either way, because no document addresses them.
**BEST-SUPPORTED INTERPRETATION:** **Stage 3 may assert Exchange.com (with its price, date, share count and earn-out)
and may not assert WarehouseDirect, Internet Mail or Allaire as Stage-3 events** — their absence is consistent with
their having happened after 1999-12-31, which §S's UNTRIED query would establish either way and which is itself the
finding if it comes back 2000. **The asymmetry to guard against is the reverse error: treating "not in the filings" as
"did not happen"** (method §14 rule 6 — a null from one family is not a null).
**RESIDUAL UNCERTAINTY:** the status of the three names outside this corpus; and what "other acquisitions" in the same
sentence covers — **unnamed acquisitions are disclosed as existing and are not enumerated.**
**CONFIDENCE:** High (the filed Exchange.com record) / High (that the three strings are absent here) / **UNKNOWN
(their corporate history)**.

**U.157 — The FY1999 10-K/A's own share-basis note is internally stale: "18 million" IPO shares and a "36:1" conversion rate, against a list of three splits.**
**CLAIM A:** the equity note: "On **May 15, 1997**, the Company completed an initial public offering of **18 million
shares** of its common stock. Net proceeds to the Company aggregated **$49.1 million**" (`10-K/A/99` l.2307–2310;
identical in `10-K/99` l.3817–3820). **CLAIM B:** the same paragraph lists "**a 2-for-1 stock split … June 1, 1998 …
3-for-1 … January 4, 1999 … 2-for-1 … September 1, 1999**" and states the preferred was convertible "at an effective
rate of **36 shares of common stock for one share of preferred**", with all preferred converted into "an aggregate of
**20,678,256** shares" at the IPO closing (l.2296–2317).
**WHY THEY DIFFER:** **the two share figures are restated through only two of the three splits the note itself lists.**
§P.2 **t18** runs the arithmetic: `3,000,000 × 2 × 3 = 18,000,000` ✓ (missing the September 1999 ×2, which would give
36,000,000); and `574,396 × 36 = 20,678,256` ✓ while the Stage-2 IPO-date ratio of 6:1 (§P.2 s27) × 2 × 3 = 36 ✓ —
again missing September's doubling, so **on the FY1999 basis the rate is 72:1 and the IPO was 36 million shares**. The
$49.1m of net proceeds is the one figure in the paragraph that needs no restatement, and it matches the FY1997
cash-flow line of $49,103 (Stage 2 §P95) exactly.
**EVIDENCE WEIGHT:** both legs are the **same paragraph of the same audited note**, which is what makes this a
documentable internal inconsistency rather than a disagreement between sources. The **424B1 is dispositive for what
was actually sold in 1997: 3,000,000 shares at $18.00** (Stage 2 §P91–P92).
**BEST-SUPPORTED INTERPRETATION:** **the note is quoted, the arithmetic is shown, and nothing is "corrected" into a
single figure.** Any Stage-3 use of "18 million shares" or "36:1" must state that it is restated only to January 1999.
**Consequence for the register: this is the live demonstration of why §P.2 t18 exists** — a reader who took the note's
18 million as current would carry a 2× error into every per-share number, which is the same class of defect as the
**6×-instead-of-12×** cumulative-split hazard at U.128.
**RESIDUAL UNCERTAINTY:** why the note was left half-restated; no explanatory note addresses it (the 10-K/A's stated
corrections are the cash-equivalents policy and the Note 9 transpositions, not this paragraph).
**CONFIDENCE:** High.

**U.158 — There is no single filed value for 1997 or 1998 technology spend, depreciation, gross fixed assets, accounts or working capital.**
**CLAIM A:** the ordinary register form of a Stage-3 row — "FY1997 technology spend **X**", "FY1998 depreciation
**Y**" — as though each had one filed value, which is how sibling dossiers and any copy-out will write them.
**CLAIM B:** this part's own findings, assembled: FY1997 technology **12,485 / 13,916 / 13,384** (U.150); FY1998
technology **46,807 / 46,424**; FY1997 depreciation **3,388 / 3,442** and FY1998 **9,692 / 9,421** (U.145); FY1997 gross
fixed assets **12,899 / 13,490** (U.147); FY1997 net sales **147,758 / 147,787** and net loss **(27,590) / (31,020)**
(U.125, U.136); FY1998 net sales **609,996 / 609,819** (U.149); FY1996 net loss **(5,777) / (6,246)** and equity
**3,401 / 2,943** (U.159); accounts at one date **3.1m / 3.3m** (U.127); FY1996 working capital **2,270 derived / 1,698
filed** (U.159); change in cash for FY1998 **+23,685 / (38,536)** (U.154); FY1997 EPS **(1.27) / (0.24) / (0.12)**
(U.133).
**WHY THEY DIFFER:** **not by error but by design of the reporting system** — every later annual report recasts every
earlier year, captions move, splits restate counts, and one 2000 policy change rewrites three years of a cash-flow line.
**No reconciling note itemises any of it.**
**EVIDENCE WEIGHT:** **this is a structural finding about the corpus, not a dispute inside it.** Every individual pair
is Tier 1 and audited at its own date; the register's default single-value shape is what is wrong.
**BEST-SUPPORTED INTERPRETATION:** **every Stage-3 row for 1996–1998 carries a printing tag — `as filed` or `as
restated` — and any ratio computed across the 1998/1999 or 1999/10-K/A boundaries names both bases.** §P does this for
all forty-odd affected rows and §P.2 t1–t25 foots the pairs that can be footed. **The rule for downstream passes is
mechanical: if a Stage-3 figure is quoted without a document name attached, it is incomplete, not compact.**
**RESIDUAL UNCERTAINTY:** the reconciling detail behind every pair (§S row 5). **CONFIDENCE:** High.

**U.159 — The FY1996 audited column that Stages 1–2 established is itself one of three printings.**
**CLAIM A:** Stage 2 §P.2a re-set the FY1996 income statement to the audited set — cost of sales **12,287**, gross
profit **3,459**, marketing **6,090**, product development **2,313**, G&A **1,035**, total opex **9,438**, loss from
operations **(5,979)**, net loss **(5,777)** — after proving a received set appeared in no accession, and Stage 2
recorded the working capital at 1996-12-31 as **derived 2,270** because "the filing prints no 1996 working-capital
line" (§P81a). **CLAIM B:** the Stage-3 documents print **different** FY1996 comparatives: `10-K/98` l.1222–1247 gives
product development **2,401**, G&A **1,411**, total opex **9,902**, loss from operations **(6,443)**, net loss
**(6,246)**, LPS **(0.06)** on 111,271, working capital **1,698**, total assets **8,434**, equity **2,943**; and
`10-K/99` l.1732–1766 gives marketing **6,081**, technology and content **2,377**, G&A **1,408**, stock compensation
**36**, total **9,902** again. **Net sales 15,746, cost of sales 12,287 and gross profit 3,459 are unchanged in all
three printings.**
**WHY THEY DIFFER:** the same pooling-and-recaption mechanism as U.150, applied backwards to 1996. **The important part
is that it is not a discrepancy of unknown cause: §P.2 t21 proves it foots.** `9,902 − 9,438 = +464` of expense, and the
operating loss moves by exactly `−464`; the net loss moves by `−469`, of which `−5` is interest income (202 → 197) ✓.
t22 does the same for working capital and finds a **residual of 49** that the headline restatements do **not** explain
(`2,270 − 1,698 = 572`, against `+163` assets and `−458` equity = 621) — **the only unclosed leg in the whole
cross-stage set.**
**EVIDENCE WEIGHT:** three audited printings of one year, the earliest the contemporaneous one and the later two
comparatives; **Stage 2's set is not wrong — it is the as-filed state, correctly recovered.**
**BEST-SUPPORTED INTERPRETATION:** **both are kept and the point of the earlier ruling is preserved: Stage 2's
correction was against a fabricated set, not against the FY1998/FY1999 comparatives.** §P259/§P260/§P261 carry the
pairs; §P.2a records that **Stage 2's claim that no filed 1996 working-capital line exists is falsified by the FY1998
Item 6**, while its derived 2,270 remains valid on its own as-filed basis. **No cell in this part mixes a 1996
as-filed line with a 1996 restated line** (t23 states the identity test that enforces it).
**RESIDUAL UNCERTAINTY:** the 49 of unexplained working-capital movement; what the +464 of expense actually is.
**CONFIDENCE:** High.

**U.160 — "Net sales" means a different object in FY1999 than in FY1997, in the same caption.**
**CLAIM A:** net sales is a single continuous revenue line — 147,787 (1997), 609,819 (1998), 1,639,839 (1999) — as the
Item 6 tables present it. **CLAIM B:** the FY1999 filing's own definitions: net sales "consist of product sales
**plus** … zShops and Auctions transactions, **which include sales commissions, placement fees and fees**"
(`10-K/A/99` l.292; `10-K/99` l.833), whereas FY1997 and FY1998 recognised only product sales on shipment.
**WHY THEY DIFFER:** the caption continued and the **composition changed**, with the change disclosed in a definition
paragraph and never quantified. **The FY1998 comparative for the marketplace line does not exist because the line did
not exist** — which is why §P235's growth multiple cannot be decomposed into "retail growth" and "marketplace growth".
**EVIDENCE WEIGHT:** both legs are the registrant's own; the second is the stronger statement of what the number
measures, and it is post-hoc relative to the FY1997 presentation.
**BEST-SUPPORTED INTERPRETATION:** **the FY1999 net-sales line is a different object from the FY1997 line and every
multi-year ratio built on it is mixed-basis.** §P prints the composition warning in the §P header; §P.2 "Not computed"
(iii) refuses to split it; §R Revenue states it as the stage's principal metric-definition change. **This row is the
reason §Q's endpoint argument cannot be settled by a revenue inflection: the inflection is partly definitional.**
**RESIDUAL UNCERTAINTY:** the dollar weight of the fee component in FY1999 — **never disclosed.**
**CONFIDENCE:** High.

**U.161 — Headcount: three filed bases, a fourth from the shareholder letter, and a fifth from the proxy family.**
**CLAIM A:** FY1997's Item 1 says "As of December 31, 1997, the Company employed **614 full-time employees**"
(`10-K405/97` l.516). **CLAIM B:** `ARS/98` l.157, twelve months later and about the same year-end: "**In 1998 our
employee base grew from approximately 600 to over 2,100**" — **600, not 614**, and "employee **base**", a different
word from employee; and FY1999 (`10-K/99` l.684) says "**approximately 7,600 full-time and part-time employees**", the
**widest** basis of the set.
**WHY THEY DIFFER:** **basis and rounding, at three dates, in the company's own documents.** 600 versus 614 is the
shareholder letter rounding a filed figure down to a level that suits the growth sentence; 7,600 versus 2,100 is not
comparable at all because part-time employees enter the count in FY1999 and independent contractors are named but never
numbered in both years.
**EVIDENCE WEIGHT:** all Tier 1 and all the same issuer; **none is a check on any other.** The FY1999 "full-time and
part-time" wording is the only basis statement made in any of the four sentences.
**BEST-SUPPORTED INTERPRETATION:** **§R prints the bases side by side and this part computes no per-employee figure
anywhere** (§P.2 "Not computed" (i)). **The trap this row exists to stop is the arithmetic temptation:** `7,600 ÷ 614 =
12.4×` reads as a headcount multiple and is instead **a wider definition times a real increase**. The honest statement
is that headcount rose several-fold on the two narrower bases and that **no defensible single multiple exists**.
**Value corrected against the instruction layer:** the received brief called the FY1999 figure "7,600 full-time"; the
filing says "full-time **and part-time**" (§P.2a row 1).
**RESIDUAL UNCERTAINTY:** the contractor and temporary populations at all three dates; the full-time-equivalent
equivalents of 7,600; why the letter used "base".
**CONFIDENCE:** High (each sentence) / **Medium and unresolved (any comparison)**.

**U.162 — The video store's launch day is 1998-11-17 in a release, and only "November 1998" in every table that matters.**
**CLAIM A:** "**Amazon.com launched its video store on November 17** with more than **60,000** VHS and [DVD titles]"
(`8-K(1999-01-26)` l.306, the attached release, event 1999-01-26). **CLAIM B:** the FY1999 launch table says
"**DVD/Video … November 1998**" (`10-K/99` l.276), and the FY1998 10-K says only "the **video store in November
1998**" (l.1322, l.1370).
**WHY THEY DIFFER:** **the day survives only in a press release the annual documents do not cite**, and the
periodic-report convention is to date launches to the month. **This is the only exact launch day anywhere in the
Stage-3 corpus**, which makes it disproportionately load-bearing for §Q's claim about the limits of dating.
**EVIDENCE WEIGHT:** the release is Tier 1 as an artifact and company-self-report as evidence; the annual documents are
the same author being less precise, not contradicting it. **The Q3-1998 10-Q had said only that the company "has
announced plans to launch a video store" (l.954, l.1408) — so the corpus also shows the promise preceding the launch
by one quarter, which is a useful sequencing check.**
**BEST-SUPPORTED INTERPRETATION:** **date the row to 1998-11-17 and print the month-only prints beside it.** §Q does.
**And state the general rule the row implies: the presence of one dated launch is evidence about the archive, not about
the company's precision** — the other eleven launches in the same table have no day anywhere in the corpus (§S row 9).
**RESIDUAL UNCERTAINTY:** whether 17 November was availability, announcement, or the release's own rounding; no filing
defines the term "launch".
**CONFIDENCE:** High (that the release says November 17) / Medium (that the day is the availability date).

**U.163 — The European launch is priced at "~$55m aggregate, mostly stock" and filed as 540,066 restricted shares.**
**CLAIM A:** the held `channels.csv` row records the Bookpages/Telebook channel as "**~$55m aggregate, mostly stock**;
two European DCs leased" (ST3_C, held for width at merge). **CLAIM B:** the filed instrument for the April 1998 set is
**540,066 restricted shares** covering **Bookpages, Telebook and Internet Movie Database Limited** together
(`8-K(1998-04-17)`; named at `10-Q Q1-1998` l.483 and `10-Q Q2-1998` l.478), and IMDB appears in the FY1998 10-K's
**subsidiary list at 100%** (l.5608) — **the dossier's dollar total omits the third company entirely.**
**WHY THEY DIFFER:** §P.2 **t11** shows how the aggregate was built: `~11.4 + ~43.4 = 54.8 ≈ 55` **million**, a sum of
two company-stated figures with **different consideration mixes**, taken from the releases and re-presented in the
S-4 File No. 333-56723 lineage. **A share count and a dollar aggregate are not two measurements of one price; they are
two different disclosures about a three-party transaction.**
**EVIDENCE WEIGHT:** the filed share count is the harder fact; the "~$55m" is a DERIVED sum of stated approximations and
can only ever be approximate.
**BEST-SUPPORTED INTERPRETATION:** **carry the 540,066-share instrument as the filed act and the ~$55m as this
dataset's DERIVED aggregate with its two named terms and its omissions stated.** §P223 does exactly that.
**Never cite "~$55m" as "the price of Germany and the UK"** — it does not include IMDB, the two European distribution
centres were **leased** not bought, and neither component is audited.
**RESIDUAL UNCERTAINTY:** the cash/stock split of each component; IMDB's own consideration.
**CONFIDENCE:** High (the share count) / Medium (the derived total).

**U.164 — One document, two share bases: the FY1998 10-K's F2 footnote says the schedules were NOT restated for the January 1999 split that the same filing applies.**
**CLAIM A:** the FY1998 10-K's Item 6 per-share data are on the split-adjusted basis, with the prices table expressly
"adjusted to reflect the **2-for-1 stock split effected June 1, 1998 and the 3-for-1 stock split effected January 4,
1999**" (`10-K/98` l.1175–1176). **CLAIM B:** the XBRL-adjacent F2 footnote of the **same document** states: "ON
JANUARY 4, 1999, THE COMPANY EFFECTED A THREE-FOR-ONE STOCK SPLIT IN THE FORM OF A STOCK DIVIDEND. … **PERIOD FINANCIAL
DATA SCHEDULES HAVE NOT BEEN RESTATED FOR THE STOCK SPLIT**" (l.5708–5710).
**WHY THEY DIFFER:** **two machinery statements inside one filing that describe different artefacts** — the human-readable
annual report restated, the **machine-readable financial-data schedule** did not. It is not a contradiction about a
number; **it is a warning that the same accession carries per-share data on two bases depending on which part of the
file a reader pulls from.**
**EVIDENCE WEIGHT:** both are the registrant's own; **neither is wrong**, and neither is a basis for a share count
without a citation to the specific part of the document.
**BEST-SUPPORTED INTERPRETATION:** **every per-share citation in this stage names the accession AND the part** (MD&A
table, Item 6, F-page schedule, proxy footnote). §P194 and §P256 do this, and §P.2 t19 shows the same document
carrying **two share series for one year** (Item 6 326,753 vs the EPS note 332,409) with differences running **both
ways**, so no arithmetic reconciliation exists. **The FY1999 10-K's F2 equivalent repeats the caveat for two splits**
(l.5587–5591).
**RESIDUAL UNCERTAINTY:** which figures inside the FY1998 filing were actually computed on which base — the filing does
not annotate them individually.
**CONFIDENCE:** High.

**U.165 — $2.8 million of in-process research and development written off on arrival: the filed record that some acquired technology did not yet work.**
**CLAIM A:** the FY1999 narrative of acquisitions describes the purchases of Alexa Internet and Accept.com as
strengthening payment and personalisation capability, and the 10-K/A's MD&A lists them among the events that
"increased amortization" — an unambiguous capability gain (`10-K/A/99` l.550–560). **CLAIM B:** Note 2 of the same
document: "Approximately **$2.8 million of the purchase price of the Accept.com and Alexa transactions** attributable to
**in-process research and development** efforts **has been expensed because, at the time of acquisition, technological
feasibility had not been established and no alternative future uses existed**" (l.1719–1725).
**WHY THEY DIFFER:** **they do not, and that is the point.** The second sentence is the company's own audited
characterisation of part of what it bought: **not feasible, no alternative use.** A reader who takes only the MD&A
leg would record the acquisitions as capability acquired; the note records that a slice of the capability was
**research in process at the moment of purchase**, priced by an independent valuation and written off immediately.
**EVIDENCE WEIGHT:** both Tier 1 and audited; **the note is the stronger evidence because it is an accounting
determination with a dollar amount, made under a standard, not a narrative.**
**BEST-SUPPORTED INTERPRETATION:** **register this as the stage's only filed record of a technology acquisition
under-performing at the moment of purchase**, and read it as an **INFERENCE about the 1999 acquisition programme's
risk**, not as a claim that any product failed: the write-off is small against the ~$189m Accept.com price
(`2.8 ÷ 189 = 1.5%`), so it evidences **disclosed immaturity**, not a botched deal. **It is also the closest thing in
the whole Stage-3 corpus to an admitted operational failure with a number attached, and §M's thinness on failures is a
selection artifact, not an absence of problems** (§S row 16).
**RESIDUAL UNCERTAINTY:** what the in-process R&D was for; whether it was later completed.
**CONFIDENCE:** High (the disclosure) / Medium (the inference).

**U.166 — Which clock dates a filing: the submissions index `filingDate`, the document's own header, or the press release inside it.**
**CLAIM A:** the FY1999 10-K was filed **2000-03-23** (submissions index `filingDate`, quoted in the intake addendum).
**CLAIM B:** the same accession's own SEC header prints **`FILED AS OF DATE: 20000329`** — six days later. A third leg
sits inside the 8-K whose event date is **1999-10-28** but whose attached press release is dated **1999-10-27**
(`8-K(1999-10-28)` header, "AMAZON.COM'S PRESS RELEASE DATED OCTOBER 27, 1999"), and a fourth sits in the Alexa 8-K's
index date **1999-06-08** against its Item 2 completion date **1999-06-10** (→ U.120).
**WHY THEY DIFFER:** **different instruments keep different clocks**: index acceptance, EDGAR header stamp, the date a
release was handed out, and the date an event legally completed. **None is wrong and none is a fact about when the
market could have read the document.**
**EVIDENCE WEIGHT:** the document governs its own contents; the index governs its own ordering.
**BEST-SUPPORTED INTERPRETATION:** **cite whichever clock the argument needs and say which one was used; do not average
them, and do not let a dossier treat a header date as market availability.** §T does this for all four annual reports
and both ARS/DEF pairs; §Q keys the Alexa row to 1999-06-10 with the index date carried in-cell; §S records that the
**10-K/A's primary document carries no header block at all**, so its period is **established by the index only** and any
citation of it must cite the index.
**RESIDUAL UNCERTAINTY:** why the two clocks differ by six days for this one accession — **UNANSWERED**, and no request
was made in this pass to test it.
**CONFIDENCE:** High (that the clocks differ) / UNKNOWN (cause).

**U.167 — "The Company intends to secure releases of all of Mr. Bezos' guarantees as soon as possible following the closing of this offering" — and nothing afterwards.**
**CLAIM A:** the S-1 lineage (1997) undertakes that the founder's personal guarantees — the Seafirst merchant account
(November 1994 → December 1996), the Wells Fargo bankcard account (July 1995) and the company-card guarantees (April
1995) — will be **released** after the offering, and Stage 2 recorded that the merchant-account leg ended in December
1996 (U.82). **CLAIM B:** across **every filing dated after 1997-05-15 in this corpus** — the 1997-11-10 8-K, all eight
10-Qs, both DEF 14As, the FY1998 10-K and all seventeen debt and shelf registrations — **the strings `Seafirst`,
`Wells Fargo`, `Bezos … guarantee`, `release … guarantee` return zero hits**, apart from one lease clause that uses
Seafirst's **prime rate** to compute a late charge on rent. **The FY1997 10-K405 never names Seafirst or a Bezos
guarantee at all, and the FY1998 10-K routes Item 13 to a proxy that is silent on it.**
**WHY THEY DIFFER:** **an undertaking made in one instrument and never mentioned again.** The 1998 proxy's "Certain
Transactions" contains only the Cook/Stonesifer Series A purchases and the $75,000 Dalzell relocation loan (repaid
1998-10-23); the 1999 proxy contains only that loan. **Either the releases happened and required no disclosure, or they
did not happen and were not disclosed** — and the record cannot tell which, because the instruments that would have
effected them **were never filed at all** (§S row 8).
**EVIDENCE WEIGHT:** a **documented absence across 125 catalogued rows**, which is stronger than a single-document
silence; **but absence of post-IPO mention is not evidence of release**, and the only in-filing statement remains the
pre-IPO undertaking.
**BEST-SUPPORTED INTERPRETATION:** **the release status stays UNKNOWN, now UNKNOWN-with-the-searches-recorded rather
than untried.** Stage 2's §R already called the twelve months from 1996 the period in which "the founder's personal
balance sheet stops being the company's collateral"; **Stage 3 can now say that the completion of that process is not
evidenced anywhere in the public filing record**, and that the only routes left are non-EDGAR. **No §R cell in this part
asserts that the guarantees ended.**
**RESIDUAL UNCERTAINTY:** whether they were released, when, and their amounts — **no amount for any of the three is
disclosed in any document in either stage.**
**CONFIDENCE:** High (that the record is silent) / **UNKNOWN (the fact)**.

**U.168 — The retracted 1995 money leg survives in the instruction layer: `2,613,000` and `$871,000`, twice each.**
**CLAIM A:** `context_appendices.md` — a file a cold reader consults for environment context and which downstream
passes copy figures out of — **still prints `2,613,000` and `$871,000`, twice each**, inside rows that *label* them
retracted. **CLAIM B:** both strings occur **zero times across all files in `sources/`**, re-checked by machine this
pass; the filed figures for the same question are **$1,007,000 aggregate over the window 1995-12-06 → 1996-05-16** for
3,021,000 shares to 23 purchasers (Stage 2 §P129, §P131), and the in-window 1996 portion of that aggregate is
**UNKNOWN and must not be filled.**
**WHY THEY DIFFER:** **presentational persistence of a withdrawn value.** A labelled retraction is not the same as an
absent string: a grep-and-lift, a column scan, or a spreadsheet export recovers the withdrawn number, which is
precisely how it survived three earlier repair passes (method §14 rule 10 records the same mechanism for the
`$976,408` leg).
**EVIDENCE WEIGHT:** **the corpus wins, twice over** — the strings are absent from the primary record, and their
presence is confined to an instruction-adjacent file rather than asserted anywhere.
**BEST-SUPPORTED INTERPRETATION:** **the leg stays retracted, the fill stays UNKNOWN, and the sweep must reach the
instruction layer, not only the corpus** (§14 rule 10). **Recorded here, not fixed:** this part does not own
`context_appendices.md` (§14 rule 4), and the correct remedy — a header-line correction on that file plus a
`CORRECTIONS.md` entry, not a silent value swap — belongs to whichever pass is assigned that path. **The Stage-2
register carried the same residue as U.107; this row is the Stage-3 re-detection, three passes later, which is the
evidence that the defect is structural rather than one agent's mistake.**
**RESIDUAL UNCERTAINTY:** how many downstream rows in any stage copied the pair. **CONFIDENCE:** High.

### >>> CONFLICT RE-KEY MAP (provisional → final → dossier original)

**Applied by the orchestrator. 39 rows re-keyed, 0 re-emitted, 16 new rows emitted.** The provisional keys in
`conflicts.csv` become the final ids by dropping the leading `P-`; the dossier's own id is retained in the `section`
column, where it already sits, and is echoed here for the parity check. **§U block count 55 = 39 re-keyed + 16 new;
`conflicts.csv` Stage-3 row count after application = 39 (existing) + 16 (this part's append block) = 55.**

| Provisional | Final | Dossier original | Source dossier |
|---|---|---|---|
| `P-U.114` | **U.114** | `U.201` | `ST3_A_chronology_org.md` |
| `P-U.115` | **U.115** | `U.202` | `ST3_A_chronology_org.md` |
| `P-U.116` | **U.116** | `U.203` | `ST3_A_chronology_org.md` |
| `P-U.117` | **U.117** | `U.204` | `ST3_A_chronology_org.md` |
| `P-U.118` | **U.118** | `U.205` | `ST3_A_chronology_org.md` |
| `P-U.119` | **U.119** | `U.206` | `ST3_A_chronology_org.md` |
| `P-U.120` | **U.120** | `U.207` | `ST3_A_chronology_org.md` |
| `P-U.121` | **U.121** | `U.208` | `ST3_A_chronology_org.md` |
| `P-U.122` | **U.122** | `U.209` | `ST3_A_chronology_org.md` |
| `P-U.123` | **U.123** | `U.210` | `ST3_A_chronology_org.md` |
| `P-U.124` | **U.124** | `U.211` | `ST3_A_chronology_org.md` |
| `P-U.125` | **U.125** | `C-1` | `ST3_B_finance.md` |
| `P-U.126` | **U.126** | `C-2` | `ST3_B_finance.md` |
| `P-U.127` | **U.127** | `C-3` | `ST3_B_finance.md` |
| `P-U.128` | **U.128** | `C-4` | `ST3_B_finance.md` |
| `P-U.129` | **U.129** | `C-5` | `ST3_B_finance.md` |
| `P-U.130` | **U.130** | `C-6` | `ST3_B_finance.md` |
| `P-U.131` | **U.131** | `C-7` | `ST3_B_finance.md` |
| `P-U.132` | **U.132** | `C-8` | `ST3_B_finance.md` |
| `P-U.133` | **U.133** | `C-9` | `ST3_B_finance.md` |
| `P-U.134` | **U.134** | `U-C1` | `ST3_C_product_market.md` |
| `P-U.135` | **U.135** | `U-C3` | `ST3_C_product_market.md` |
| `P-U.136` | **U.136** | `U-C4` | `ST3_C_product_market.md` |
| `P-U.137` | **U.137** | `U-C5` | `ST3_C_product_market.md` |
| `P-U.138` | **U.138** | `U-C6` | `ST3_C_product_market.md` |
| `P-U.139` | **U.139** | `U-C7` | `ST3_C_product_market.md` |
| `P-U.140` | **U.140** | `U-C8` | `ST3_C_product_market.md` |
| `P-U.141` | **U.141** | `U-C9` | `ST3_C_product_market.md` |
| `P-U.142` | **U.142** | `U-C10` | `ST3_C_product_market.md` |
| `P-U.143` | **U.143** | `U-C11` | `ST3_C_product_market.md` |
| `P-U.144` | **U.144** | `U-C12` | `ST3_C_product_market.md` |
| `P-U.145` | **U.145** | `U.D1` | `ST3_D_tech_ops.md` |
| `P-U.146` | **U.146** | `U.D2` | `ST3_D_tech_ops.md` |
| `P-U.147` | **U.147** | `U.D3` | `ST3_D_tech_ops.md` |
| `P-U.148` | **U.148** | `U.D4` | `ST3_D_tech_ops.md` |
| `P-U.149` | **U.149** | `U.D5` | `ST3_D_tech_ops.md` |
| `P-U.150` | **U.150** | `U.D6` | `ST3_D_tech_ops.md` |
| `P-U.151` | **U.151** | `U.D7` | `ST3_D_tech_ops.md` |
| `P-U.152` | **U.152** | `U.D8` | `ST3_D_tech_ops.md` |
| **— (new)** | **U.153** | — | this part: the Stage-3 **boundary contest**, with ST3_A's "first filing that uses 'opened'" **falsified** by `10-K405/97` l.1647, `ARS/98` l.160, `10-Q Q1-1999` l.592 / l.915 |
| **— (new)** | **U.154** | — | this part: the **10-K/A** flips FY1998's change in cash **+23,685 → (38,536)** |
| **— (new)** | **U.155** | — | this part: **zShops** "late September 1999" (10-Q, 8-K) vs **"October 1999"** (FY1999 launch table) |
| **— (new)** | **U.156** | — | this part: **Exchange.com** filed with date/price/shares vs **WarehouseDirect / Internet Mail / Allaire** zero-occurrence |
| **— (new)** | **U.157** | — | this part: the 10-K/A's **"18 million shares" / 36:1** note, restated through two of three splits |
| **— (new)** | **U.158** | — | this part: **no single filed value** for 1997/98 technology spend or depreciation (structural finding) |
| **— (new)** | **U.159** | — | this part: the **FY1996** column is one of three printings; Stage 2's set is as-filed, and "no filed 1996 working-capital line" is falsified |
| **— (new)** | **U.160** | — | this part: **net sales composition change** — 1999 includes marketplace fees in the same caption |
| **— (new)** | **U.161** | — | this part: **five headcount renderings** across three bases (614 / ~600 / ~2,100 / over 2,100 / ~7,600 FT-and-PT) |
| **— (new)** | **U.162** | — | this part: **video 1998-11-17** in the release vs "November 1998" in every table |
| **— (new)** | **U.163** | — | this part: **~$55m aggregate** vs the filed **540,066 restricted shares** for three companies |
| **— (new)** | **U.164** | — | this part: FY1998 10-K **F2 "not restated for the stock split"** vs its own restated Item 6 — one accession, two bases |
| **— (new)** | **U.165** | — | this part: **$2.8m in-process R&D written off** at Accept.com/Alexa — filed admission of not-yet-usable technology |
| **— (new)** | **U.166** | — | this part: **which clock dates a filing** — index `filingDate` vs header `FILED AS OF DATE` vs the release inside |
| **— (new)** | **U.167** | — | this part: the **guarantee-release undertaking** (S-1) vs **zero post-IPO mentions** across 125 rows |
| **— (new)** | **U.168** | — | this part: `2,613,000` / `$871,000` **instruction-layer residue**, re-detected at Stage 3 after Stage 2's U.107 |
