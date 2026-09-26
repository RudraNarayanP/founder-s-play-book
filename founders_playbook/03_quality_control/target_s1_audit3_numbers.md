# Target Stage 1 - Stage-1 numbers audit 3

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-26T11:19:48Z. owner=target-s1-audit3. Section skeleton replaced by the audit; nothing else on this path was written before it. -->

**Audit: `company_042_target` quantitative register + `stage_1.md` (37,507 w) + `research/B1_dayton_print_records.md`
store/sales series. Numbers only. Web budget 0; every carrier checked is a file under
`01_companies/company_042_target/sources/`.**

**Headline.** All 61 rows were put through two independent tests — the 9 rows carrying a formula were
recomputed, and all 61 value cells were searched against the held carrier bytes (60 of 61 found; the
single miss is a derived row, as expected). One arithmetic test fails (row 15: the value cell does not
equal the row's own computed result). The larger damage is not in the arithmetic: **7 rows still carry the
exact fiscal-vs-calendar error COR-01 was minted to retire**, and **B1's nine-value parent-sales series
reached the register as three rows — six components dropped silently, including the only denominator that
makes the register's own "44 percent" claim true.** 24 of 61 rows carry at least one number-level defect
(enumerated in §Rows re-derived). No defect was repaired here.

---

## Rows re-derived

Row key = CSV line order (1 = first data row). **`quantitative.csv` has no key column** — 12 columns, none
of them an id — so rows are addressed here by position + metric, which will not survive a re-sort.
Printed-vs-carrier check for all 61: 60 values occur verbatim (comma-formatted) in
`sources/**/**.txt`; the one miss is row 15, which is derived and says so.

### The 9 formula rows, recomputed

| Row key | Formula as given | Recomputed | Printed | Verdict |
|---|---|---|---|---|
| r02 `parent_net_income` 1966-01-29 | 7,128,981 / 5,435,205 | 1.311631 (= +31.163%) | "1.3116", "31 percent" | PASS — carrier L609/L173 print 31 percent and the base 5,435,205 ✓ |
| r04 `target_avg_retail_area_per_store` 1967-01-28 | 889,000 / 7 | 127,000.0 exact | 127000 | PASS arithmetically; basis defect (see D-16) |
| r10 `target_stores_in_operation` 1968 | "not_derived" | — | 11 | **FAIL on class**: 11 is obtained by reading "five years" back from the FY1973 report's sentence ("Target has grown from 11 stores to 46 stores in five years", L564-565). It is an inference from a rhetorical clause, carried as FACT/`not_derived`. Its companion term (46 = FY1973) was dropped (D-17). |
| r11 `target_stores_in_operation` 1969 | 11 + 6 (2 Dallas + 2 Houston + 1 Colorado Springs + 1 St. Louis) | 2+2+1+1 = 6; 11+6 = 17 | 17 | PASS arithmetic (openings independently confirmed: the FY1974 roster's 1969 rows are Bridgeton, North Dallas, Garland, Colorado Springs, Hedwig Village, South Loop = 6 ✓). Cross-check is circular (D-13). |
| r12 `target_stores_in_operation` 1970 | 30 at year-end 1971 − 6 opened in 1971 | 24 | 24 | PASS arithmetic; the "6 opened in 1971" is not shown as a formula input anywhere |
| r15 `target_unit_sales` 1966 | 86,901,007 / 1.43 = 60,769,935 | **60,769,935.0** | value cell **60770000** | **FAIL — printed ≠ computed (Δ 65), three values for one variable** (D-8). Also 2-s.f. input → 8-s.f. output (D-P1). |
| r30 `parent_net_retail_sales_growth_printed` 1965 | 186,166,671 / 162,773,739 = 1.1437 | 1.143714 (+14.371%) | "14.4 percent, consistent with the printed 14" | PASS; carrier L602 prints "14 percent larger than the $162,773,739" ✓ both columns read off the same statement (L822) |
| r57 `…sales_per_sqft_change_1969_to_1973` | 84.54 / 97.70 − 1 = −0.1347 | −0.134698 | −13.5 percent | PASS; both legs are in the same printed row of S4209 (L3988-3998: 97.70 … 84.54) ✓ one-row-one-basis claim verified. Date cell wrong (D-1). |
| r58 `…revenue_per_store_1969` | 233.5 / 19 = 12.29 | 12.28947 (with the more precise carrier 233,532k: 12.29116) | 12.29 | PASS rounding; denominator unstated as period-end (D-7). Numerator taken from S4209 (233.5) while r20 holds S4205's 233,532 — one carrier chosen silently. |
| r59 `…revenue_per_store_1972` | 440.4 / 50 = 8.81 | 8.808 (with r23's 440,441,000: 8.8088) | 8.81 | PASS rounding; same two defects. |

### Class-shape results on all 61

- **0 rows are classed `DERIVED`** (class counts: FACT 51, ESTIMATE 7, UNKNOWN 1, CONTEMPORARY 1,
  "company-printed" 1). Nine rows carry arithmetic anyway, so the DERIVED class is unused rather than
  clean: the arithmetic in r02/r30 is labelled a check on a FACT, and r10's true derivation is hidden in a
  note. **No DERIVED or ESTIMATE row has an empty arithmetic column** (all 7 ESTIMATE rows carry a formula
  — 0 failures of that test), but **r54, r55, r56 are FACT/`not_derived` while their own notes perform the
  foot** ("the block foots: 470.3m/5,563k = 84.5" in r55). The derivation is in the wrong column, so any
  mechanical arithmetic sweep of `derived_arithmetic` will never see it.
- Independent cross-foot of r55's claim: 470.3/5.563 = **84.5407** vs the printed 84.54 ✓ the block does foot.
- Rows carrying a numeric defect (enumerated, not grepped): r04, r10, r11, r15, r17, r18, r19, r25, r26,
  r27, r32, r37, r38, r42, r43, r45, r54, r55, r56, r57, r58, r59, r60, r61 = **24 of 61**.

STATUS: WRITTEN 2026-09-26

## Denominator and basis defects

**D-1 — the COR-01 error is still live in 7 date cells (r54-r60). This is the brief's item-2 answer.**
COR-01's own ruling is that "a report labelled N is a 52/53-week retail year ending in late January/early
February of N+1". Re-tested against the carriers (COR-01's residual note says the FY1968-onward pattern
"was not re-tested by this pass"):
- FY1973 ended **1974-02-02** — `1973_dayton_hudson_djvu.txt` L174 balance-sheet header "February 2, 1974 /
  February 3, 1973" and L4986 "filed … for Dayton Hudson's fiscal year ended February 2, 1974".
- FY1972 ended **1973-02-03** (same comparative header).
- FY1969 ended **1970-01-31** — `1969_…txt` "year ended January 31, 1970"; FY1968 "year ended February 1, 1969".
Yet r54, r55, r56, r57 are dated **1973-12-31**, r58 **1969-12-31**, r59 **1972-12-31**, r60 **1962-12-31**.
The Five Year Comparisons columns those rows come from are fiscal columns (header "1973 1972(1) 1971 1970
1969", L3973). Six of the seven do not even carry the COR-01 tag (rows tagged COR-01 = 29, and the set is
{1,2,3,4,29,30,…,53,60,61} — r54-r59 absent); **r60 carries the COR-01 tag and still has the wrong date**,
i.e. the merge stamped the correction note without applying it to that cell. 25 rows use ISO dates, 17 of
them correctly ending in January/February; the 12-31 set is the whole residue.
Consequence: r57's five-year window and r58/r59's per-store ratios are labelled with a period-end that no
carrier prints, and any later series joining these to the January-based rows (r01/r02/r39/r61) silently
crosses a year-end.

**D-2 — r18's "44 percent of net retail sales" has the wrong named denominator.** Carrier `1968_…txt`
L1361 prints `Goods Stores 189,515,025 44 141,824,116 38 33.6` under a table whose total is
**$434,132,744** (L1363, and it foots: 223,276,791 + 189,515,025 + 21,340,928 = 434,132,744). So the 44 is a
share of the three-group retail total, not of "net retail sales": the same company's next-year report
prints **Net Retail Sales 1968 = 795,243** thousand (`1969_…txt` L951, foots: 582,923 + 189,515 + 22,805 =
795,243). Against that base the share is **23.83%**, not 44. Both denominators are real and the register
names neither. 434,132,744 appears **zero** times in `quantitative.csv` and **zero** times in `stage_1.md`.

**D-3 — period-end vs average store count is never stated on the per-store rows.** r58 (233.5/19) and r59
(440.4/50) divide a full-year flow by a **period-end** count taken from the same five-year row. The fleet
moved 13 → 19 → 27 → 34 → 50 stores across 1968-1972, and the FY1972 report says 16 openings landed inside
seven months (L476-478). On an average-count basis r58 = 233.5/16 = 14.59 and r59 = 440.4/42 = 10.49.
The *direction* of the productivity fall survives (−28.1% vs −28.3% printed); the *level* does not, and a
reader cannot tell which was used. r55/r57 have the same silence on square footage (period-end space:
2,390 → 5,563 thousand sq ft).

**D-4 — r45 drops a related-party component of its own total.** Carrier L1037-1038: "aggregate minimum
annual rentals of approximately $1,564,220, **of which $626,683 is payable to unconsolidated
subsidiaries**". 40% of the registered total is affiliate-payable and appears nowhere in the row, the
volume, or a gap row.

**D-5 — r31's 11 percent is a share of a carved base.** Carrier L421-423: "Only 11 percent of sales in
Target stores are from leased departments. This does not include sales of the grocery departments,
operated by Applebaum's." The carve-out *is* preserved in the notes ✓, but the metric name
(`target_leased_department_share_of_sales`) states no denominator, and the same corpus defines the parent
line as "Net retail sales, **including** sales of leased departments" (r01) — the phrase means opposite
things at the two levels and no row says so.

**D-6 — r33's denominator is a surveyed subset, not a population.** Carrier L404-407: a Minneapolis Star
and Tribune survey of "shopping habits in the city's suburbs" found "51 percent of **women customers** in
Hennepin County shopped at a Target store in 1965". The row's metric name reads it as a share of Hennepin
County women. The base is the survey's respondent set; the sample size and frame are unprinted (class
"CONTEMPORARY OBSERVATION second-hand" ✓, but the denominator is not stated).

**D-7 — same-term-different-entity across r17-r26.** One metric name (`low_margin_group_revenue`) spans
three carrier labels — "Discount and Hard Goods Stores" (S4204, Dayton-only), "Low Margin" (S4205,
post-pooling), "LOW MARGIN STORES" (S4209) — and B1 records the perimeter itself ("also carried Lechmere
… and, from 1971, acquired Lechmere stores"). The lineage discipline in the notes is genuinely good
(r18 names all three reprints; r28 files the pooled 582,923 as `as_restated` and quotes the pre-pooling
223,276,791 in the same cell). What is missing is the corollary for the **series**: a reader can compute a
1968→1969 growth on `low_margin_group_revenue` from r18→r20 (141,824,116/189,515,025→233,532k = +23.2%)
without any flag that the 1969 column sits in a different reporting object than the 1968 one.

**D-8 — r19/r56 ignore the carrier's own footnote on the 1972 column.** The five-year block heads it
`1972(1)` and the footnote (L4031) reads "(All earnings data for 1972 are exclusive of extraordinary
items." r56 registers the earnings-ratio series `3.3 / 3.0 / 4.0 / 2.1 / 1.4` straight across that break,
and r19's note cites the same block's 1,577 ksqft / $120.16 without the footnote. The 1.4 vs 2.1
comparison is the row's own headline claim.

**D-9 — r13/r14 store basis vs r10.** r10's 11 and the 46 in r14 both trace to letters/recaps, and r13's
note records the roster conflict (29 vs 30, U.008) ✓ correctly. But r12's 24 is derived from r13's 30
while r13's own count is contradicted by the roster — the estimate inherits a contested base with no
forward reference in r12.

STATUS: WRITTEN 2026-09-26

## Sums that do not foot

**S-1 — B1's Q20 parent-sales series: 9 values in, 3 rows out. 6 components dropped silently.**
`research/B1_dayton_print_records.md` L102 carries Q20 "Parent net retail sales (whole company, NOT
Target)" dated "1964→1972" with nine values. Register coverage: 186,166,671 (r01), 162,773,739 (r39),
868,335 (r27). **Absent from every register file and from `stage_1.md` entirely** (grep count 1 = B1 only):
217,961,635; 260,173,514; **434,132,744**; 945,306; 1,086.4; 1,262,759,000. No data-gap row names the
drop. The dropped set is also the only place the FY1968-FY1972 parent sales exist at all, so the register
cannot test any group share after 1969 — which is exactly where the D-2 denominator confusion lives.
The cell also mixes four notations for one variable (dollars, `(000)`, `(m)`, bare dollars) across one
year-end migration, and its 1968 member (434,132,744, pre-pooling) sits directly beside its 1969 member
(868,335 thousand, pooled) — read as a series it prints a 100% one-year "increase" that is two-thirds
scope change.

**S-2 — r27's 868,335 is $1,000 less than the sum of the components in its own table.** `1969_…txt` L1001
-1004 print Department 607,697 + Low Margin 233,532 + Specialty 27,107 = **868,336**, against the printed
"Net Retail Sales … $868,335" (L951). r20's note asserts "the column foots: 607,697 + 233,532 + 27,107 +
20,021 = 888,357" — true of total revenues ✓, and it conceals the 1-thousand gap one line above. r27 is
FACT/**High** with no doubt recorded.

**S-3 — the 1966-01-29 money rows cannot be footed against each other.** The statement of income itself
foots: 186,166,671 − **171,932,690** = 14,233,981 ✓ (r01 − printed total deductions = r40). But the
register holds neither the 171,932,690 subtotal nor the 160,514,978 "cost of sales and expenses exclusive
of items listed below" line, and the two aggregates it does hold are from the **notes**, not the statement:
r42 (139,686,954) + r43 (31,256,511) = **170,943,465** = **989,225 short** of the statement's 171,932,690.
Add r44 (2,088,720) and r61 and the gap changes again — the six rows share one date cell and three
different bases with no basis label per row. Separately, the statement's own seven printed deduction
components sum to 171,810,830, i.e. **121,860 short of the printed 171,932,690** — an OCR digit somewhere
in the `1965_…txt` L825-838 block that no row or conflict names.

**S-4 — the maintenance-and-repairs pair is registered only on one side.** The current-year column prints
763,572 (L826); it has **no register row** — it survives only inside r61's notes and stage_1.md L1364. So
the register can state FY1965-01-30 maintenance (1,894,037) but not the year-over-year pair it is the base
of. r61's note also raises a doubt the arithmetic closes: 1,894,037 − 763,572 = **1,130,465** against the
carrier's "reduction … of approximately $1,130,000" (L616-618) — agreement to 0.04%, not "a fall larger
than the narrative explains". A false open conflict is left in the record.

**S-5 — the seven-unit space sums disagree by 167 thousand sq ft and the bases differ.** r60's note:
"sum for the seven units to 1966 = 722 against S4202's 889 (U.012)". Recomputed from the FY1974 roster
(L4636-4650): 68+96+96+106+118+119+119 = **722** ✓ (count of units matches "the seven Target stores").
But r60's own unit cell concedes the roster's column label is **OCR-corrupt**, while S4202's 889,000 is
explicitly "total **retail** area" — a net/retail vs gross/unknown comparison left to stand as a numeric
conflict, and r04 (127,000 = 889/7) carries no marker that the same seven units give 103,143 on the roster.

**S-6 — one value, three printings, one silently chosen (r15).** 60,769,935 (the row's own arithmetic
cell) / 60,770,000 (the row's value cell) / **~60,800,000** (B1 Q11, the emission the row came from) /
60,769,935 again in `stage_1.md` L625 prose. The register carries one, the volume another, and the
superseded B1 value appears in neither. Per §14 rule 8 and the brief's item 3, both must appear; neither
does.

STATUS: WRITTEN 2026-09-26

## CONTEMPORANEOUS-RESTATED mislabels

Sample re-checked against carriers: r01, r02, r03, r04, r05, r07-r15, r16-r28, r30, r31, r32, r33, r35-r46,
r47-r53, r54-r61 (well above the 15 required). Formal coverage is good — **60 of 61 rows carry a basis tag**
(only r06, the UNKNOWN row, does not). The failures are in the tags' content:

| Row | Tag as written | Defect |
|---|---|---|
| r17 (1967 group revenue) | "CONTEMPORANEOUS for 1967 as printed in the FY1968 report" | **Self-contradictory and wrong.** Its only carrier is S4204 (the FY1968 report), and the value sits in that report's *comparative* column (L1361, second pair: "141,824,116 38"). A figure printed in the FY1968 layer about 1967 is **RESTATED**. r18 — the current column of the same line — is correctly CONTEMPORANEOUS, so the pair shows the rule was understood and not applied. |
| r10 (1968 stores) | "RESTATED — a 1973 report reciting 1968" ✓ tag right | But `evidence_class` = **FACT / `not_derived`**: the number is not printed as a 1968 count anywhere; it is computed by subtracting five years from the report's own date. Class and basis tag disagree about whether anything was derived. |
| r26 (1972 group stores) | "CONTEMPORANEOUS group / RESTATED in the 1973 column" | The 50 is printed in **both** the 1972 and the 1973 columns (L3995: `50 50 34 27 19`); the tag names a column relationship that does not exist and leaves unclear which layer authorised CONTEMPORANEOUS. Source cell says source_date **1972** while the cited line is in S4209, a 1974 publication. |
| r10, r21, r22, r24, r25, r26 | RESTATED (where tagged) ✓ but their `source_date` cells read **1973** (r10, r21, r24, r25) and **1972** (r22, r26) | The `source_date` column is carrying the *row's* year, not the printing layer's year, on the six rows whose cited line is in **S4209** — and S4209 is dated 1974 in `sources.csv` (publication_date 1974), as r54-r59 correctly record. Six rows therefore assert a carrier a year or two older than the document that prints them; r22/r26 compound it by pairing S4209 with S4208 (1972), so one cell cannot name both layers' dates. (r19's 1972 is sound: its cited line is S4208 L2374.) The same defect RD-123 records for Walmart's register, arriving by a different route. |
| r61 (1,894,037) | "RESTATED (the layer labelled 1965 prints a figure for **fiscal year 1964**)" + date cell **1965-01-30** | The two fields name two different periods for one column. The value is the statement column headed "January 30, 1965". The register inherited the *letter's* prose label ("the 1964 earnings of $5,435,205", L609) for the same column the *notes* label "1965" (L944: "$123,584,592— 1965"). **One document labels the same column both 1965 and 1966** (L609/616/621 say 1965/1964 for the current/prior; L944-945 say 1966/1965). COR-01 fixed the date cells and did not record that the label conflict is internal to the carrier — which is why r52 and r61 can carry basis parentheticals that contradict their own dates. |
| r52 | "RESTATED (the layer labelled 1965 prints a figure for fiscal year 1964)", date cell bare `1964` | Same ambiguity; here the bare year is left bare, so the row cannot be resolved to a period-end at all. |
| r27 | "CONTEMPORANEOUS in both layers" | True for S4205 (current column) but S4206's 868,335 is a *comparative*, and the row's source_date prints **1970** (the later layer) for a 1969 figure. "in both layers" collapses the distinction the register elsewhere insists on. |
| r54-r56 | "CONTEMPORANEOUS (printed by the layer labelled 1973 for its own fiscal year 1973)" | Tag right (S4209 is the FY1973 layer) — but paired with date cells of **1973-12-31**, i.e. CONTEMPORANEOUS attached to a period-end the layer never printed (D-1). |
| r60 | "RESTATED (the layer labelled 1974 prints a figure for **fiscal year 1962**)" | Category error, and the worst one in the file. The FY1974/75 roster prints each store's area **beside** an "Opened" column (`Roseville, Minn. 68 1962`). The areas are attributes of the 1974 estate; 1962 is the opening year, not the year of the figure. The row's own note says "as printed in FY1965" while the source cell says S4210 — the two carriers disagree with each other inside the row. Read as written, r60 licenses "Target opened with 366k sq ft" (68+96+96+106), which no layer prints. |

**Also:** `stage_1.md` L1240-1241 says the group per-store division "is written **once**, as DERIVED" at
confidence **Medium**; the register mints **two** rows (r58, r59) at confidence **Low**. Same variable,
two layers, two counts, two confidences, no reconciliation note.

STATUS: WRITTEN 2026-09-26

## Precision laundering

**P-1 — r15 is a 2-significant-figure input rendered as an 8-significant-figure output.** The 43 percent
(S4203 L410/L769-770) is a rounded company figure; ±0.5 pp on it moves the implied 1966 base by ~±$700k.
The value cell reads `60770000` (nearest $10,000) and the arithmetic cell reads `60,769,935`. The row's own
note concedes "approximate to about 1 million" — a ±1,000,000 statement beside a $10,000-precision number.
B1's Q11 wrote the honest form: `~60,800,000`. The merge replaced the tilde-and-2-s.f. version with a
4-s.f. one, which is the laundering, and did it silently (D S-6).

**P-2 — a bound rendered as a point (r32).** Carrier `1966_…txt` L214-215: "Target statistics for **the
past two years** show that its customers spend an average of **more than $7.50** per visit, excluding
groceries. This compares with an industry average of $5.05." The row prints value `7.50`, unit "USD per
visit", date `1966`. The "more than" survives only in the notes; any consumer of the value column gets a
point estimate of a quantity the company only ever lower-bounded, assigned to a single year when the
carrier states a two-year window, and the comparator $5.05 is left unattributed (the volume's L638 table
does flag the comparator's missing carrier ✓; the register row does not carry the window at all). This is
the same failure class as the retracted "stated range" earlier in the run.

**P-3 — hedge stripped on two rows, kept on two others (r37, r38 vs r45, r46).** Carriers print "in the
**approximate amount of** $2,200,000" (1966 L807) and "annual rentals of **approximately** $225,000" (1966
L809). r37's unit is `USD`, r38's is `USD per year` — qualifiers gone — while r45 and r46 preserve
"approximately" in the unit cell. A `stage_1.md` table (L675, L1177, L1180, L2096) prints the
"approximately" form, so the hedge now exists in prose but not in the register for the same digits.

**P-4 — a rounded reprint chosen as the dividend (r58, r59).** r58 divides **233.5** (S4209's millions)
though r20 holds **233,532** (S4205's `(000)s`, 10× more precise, same year); r59 divides **440.4** though
r23 holds **440,441,000**. Both quotients happen to round the same way here (12.29, 8.81), so no printed
value moves — but the choice of the coarser numerator is a silent carrier selection that will not be
harmless the next time someone re-derives from the register.

**P-5 — printed ratios re-stated with more digits than the table.** r55 (84.54) and r57 (−13.5) are fine
(the company prints 84.54 and 97.70, and −13.469% → −13.5 is a *loss* of precision ✓). Flagged only to
record that the check was run: no row re-states a carrier ratio at extra digits apart from P-1/P-4.

**Blanks read as zeros — none found.** No value cell is empty or `0` in the 61 (the two non-numeric cells
are r06 `UNKNOWN` and r52 `magnitude UNKNOWN`, both correctly non-zero-valued); r06 keeps its source cell
as an explicit "no held layer prints …" with source_date `UNKNOWN` rather than a defaulted zero. OCR-blank
five-year blocks are described in B1 ("lose their numeric columns in OCR — a rendering null on held bytes,
not an absence of the data") and no row was fabricated from them ✓.

**Ranges read as points — one live (P-2), one historical and handled.** r32 is the live one. The register
does hold a multi-valued cell (r60, `68;96;96;106`) — not a range, but an array in a numeric column, which
no mechanical check can average or sum, and whose sum (366) is exactly the number that tempts the "1962
estate" reading named in the mislabel table.

STATUS: WRITTEN 2026-09-26

## Sweep counts

Each count with the command that produced it (run from `E:\founder's playbook`, Git Bash).

| # | Count | Value | Command |
|---|---|---|---|
| 1 | register rows / cols | **61 × 12** | `python tools/gates.py --company-dir founders_playbook/01_companies/company_042_target --checks csv,keys --fail-on substantive` → `csv quantitative.csv 61 rows x 12 cols` |
| 2 | class counts | FACT 51, ESTIMATE 7, UNKNOWN 1, CONTEMPORARY 1, company-printed 1, **DERIVED 0** | see S1 script below (`B_class_counts`) |
| 3 | rows with a real formula | **9** → 2,4,11,12,15,30,57,58,59 | S1 (`E_formula_rows`) |
| 4 | ESTIMATE/DERIVED rows with empty formula | **0** | S1 (`D_estimate_rows … empty_formula []`) |
| 5 | date cells: bare year / ISO / ISO-12-31 | **36 / 25 / 7** (12-31 set = r54-r60) | S1 (`F_`,`H_`) |
| 6 | rows ending Jan/Feb (correct retail year-end) | **17** | S1 (`I_janfeb_dates`) |
| 7 | rows without a CONTEMPORANEOUS/RESTATED tag | **1** (r06) | S1 (`J_rows_without_basis_tag`) |
| 8 | rows tagged COR-01 | **29** — matches `CORRECTIONS.md`'s "29 quantitative.csv rows"; set excludes r54-r59 | S1 (`K_rows_tagged_COR-01`) |
| 9 | value cells not found in held carriers | **1** (r15, derived) | S1 (`L_rows_value_absent_from_sources`) |
| 10 | B1 store/sales Q-rows | **20** (last = Q20) | `grep -c "^&#124; Q" .../research/B1_dayton_print_records.md` |
| 11 | B1 register emissions | **65** — reproduces RD-122's "65 rows of its own" | `awk '/^## Register rows/,0' .../B1_dayton_print_records.md &#124; grep -c "^Target,&#124;^S4&#124;^P1S&#124;^[A-Z][0-9]"` |
| 12 | Q20 series members: in register / dropped | **3 / 6** | `for v in "217,961,635" "260,173,514" "945,306" "1,086.4" "1,262,759,000" "434,132,744"; do grep -rc --include="*.csv" --include="*.md" "$v" .; done` → each returns `research/B1_dayton_print_records.md` only |
| 13 | `434,132,744` / `141,824,116` / `60,770,000` hits in `stage_1.md` | **0 / 0 / 0** (`60,769,935` → 1) | python `re.findall` over `stage_1.md`, 39 patterns |
| 14 | `223,276,791` / `582,923` hits | register 1 (notes only) / volume 3 | same loop |
| 15 | word count | `stage_1.md` **37,507** ✓ (matches RD-122), B1 7,860 | `wc -w founders_playbook/01_companies/company_042_target/stage_1.md .../B1_dayton_print_records.md` |

**S1** — the script that produced counts 1-9 (re-run from the repo root, heredoc form):
`python - <<'EOF' …csv.DictReader(quantitative.csv)… EOF` (class Counter, `derived_arithmetic` regex,
date-cell regex, basis-tag regex, then a comma-formatted search of every
`sources/**/*.txt` for each value cell). Full text was executed this pass; its stdout lines are quoted
verbatim in the table above.

### Gate

```
$ python tools/gates.py --company-dir founders_playbook/01_companies/company_042_target --checks csv,keys --fail-on substantive
# Mechanical gate report -- company_042_target

Findings: **0** | Passes: 16

- coverage 9 registers, 2 stage volumes, 17 source documents

## Passing checks
csv      timeline.csv                       24 rows x 11 cols
csv      quantitative.csv                   61 rows x 12 cols
csv      conflicts.csv                      18 rows x 15 cols
csv      sources.csv                        21 rows x 18 cols
csv      data_gaps.csv                      22 rows x 8 cols
csv      validation.csv                     4 rows x 11 cols
keys     stage_1.md                         2 source tokens all resolve
...
EXIT=0
```
**Gate green, and it is not evidence that the numbers are.** `csv,keys` checks column drift, row/col shape
and `S####` resolution; it does not open a single arithmetic cell, date basis or denominator. Two of this
audit's three worst defects are invisible to it by construction. Per RD-122 the `--tier` flag defaults to
`exemplar`; my brief's command names no tier, so the word-budget finding that `--tier core` produces is
outside this run's check set (and `budget` is not in `--checks csv,keys`).

STATUS: WRITTEN 2026-09-26

## Untried

1. **The S4209 `TOTAL RETAIL` row alignment.** That row prints only four values (`$1,262.8 $1,088.3 $946.9
   $868.8`) under five column heads, and FY1972's own report prints 1,262,759,000 — i.e. the row appears
   **column-shifted by one**, which would move every parent-sales value in the recap by a year. I did not
   resolve the alignment: it needs a re-OCR of the table image, and the register carries no `TOTAL RETAIL`
   row to test against. Left as UNKNOWN; `1,088.3` and `1,262,759,000` were grepped and appear in no
   register file.
2. **The 1973 Target store count.** No row; the FY1973 letter's endpoint 46 is the only candidate and it
   collides with r14's 46-for-1972 reading. Not adjudicated here.
3. **Rows 34-51 line-level re-read.** I verified each value's existence somewhere in `sources/` and read
   the carriers for r35, r36, r37, r38, r42, r43, r45, r46, r47, r48, r49, r50, r52; I did **not** confirm
   that each cited line number (e.g. `S4203 L189-192` for r34's 10,705,548, `S4201 L1170` for r36) is the
   line that prints it. Line-number drift is a known §14 rule 12 problem; the digits were found, the
   pointers were not audited.
4. **`conflicts.csv` / `data_gaps.csv` / `timeline.csv` numbers.** I counted anchor mentions (U.008 ×11,
   U.010 ×10, U.012 ×3) to check that the conflicts this audit cites exist; I did not audit their contents,
   nor whether the 24-defect row set maps onto conflict rows.
5. **The 34 folded collision groups (RD-122).** Only one folding loss was chased (Q20). Whether other
   multi-valued cells were folded the same way is untested — the `L_rows_value_absent_from_sources` sweep
   would not catch it, because a folded cell's members often also exist in a single-valued row.
6. **Post-1975 sources.** `sources.csv` carries S4211-S4221 (through the 1998-2000 annual reports) but
   **zero of the 61 quantitative rows post-date 1975**. Whether that is Stage 1's window boundary or an
   intake gap was not determined.
7. **Nothing was searched outside this directory.** Where a carrier is not on disk (the Minneapolis Star
   and Tribune survey behind r33; the "industry average of $5.05" behind r32; the XBRL leg of any of these
   series) the row stays UNKNOWN and I did not go looking.
8. **No repair performed.** Registers, volume, `_parts/`, `CORRECTIONS.md` and `tools/` untouched; this
   file is the only write on this pass.

STATUS: WRITTEN 2026-09-26
