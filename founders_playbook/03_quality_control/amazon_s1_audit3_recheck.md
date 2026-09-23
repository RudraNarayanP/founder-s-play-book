# Audit Sheet — Amazon (company_001_amazon) · Stage 1 · AUDIT 3 RECHECK (Numbers, Level-3) · Run 2026-09-23
Auditor: Level-3 Numbers Auditor (recheck) — independent of both producers: **yes** (wrote neither `stage_1.md`/CSVs nor
`amazon_s1_number_repairs.md`; edited nothing).
Object under test: the repair log's claim that **all 31 AUDIT 3 defects are fixed** (`03_quality_control/amazon_s1_number_repairs.md`).
Method: the AUDIT 3 section of `03_quality_control/AUDIT_PROTOCOLS.md`, re-run in full. **The repair log was not trusted;
every value below was read out of the filings.** Nothing was repaired here.

Target: `stage_1.md` §P (l.777–975, incl. §P.2), §R (l.1037–1067), `context_appendices.md`, and the nine CSVs.
Primaries (`company_001_amazon/sources/`, all greps run with `-n` against these): **orig.** = S-1 original
acc. 0000891618-97-001309 (1997-03-24); **A3** = S-1/A No. 3 acc. 0000891020-97-000755; **A5** = S-1/A No. 5
acc. 0000891020-97-000839; **10-K405** = acc. 0000891020-98-000448. Binding corrections: `CORRECTIONS.md`
COR-10 (round arithmetic + division direction), COR-12 (employee dates), COR-02, COR-09, COR-14.2.
Mechanical aid: `git diff 461299b → 8eb9f86` was used **read-only** to prove no cell of any CSV lost or shifted content
during re-serialization (every changed cell was matched by `(stage, date, metric)` key; 0 unexplained changes).

| Audit | Result | Items checked | Failures found | Actions taken | Residual risk |
|---|---|---|---|---|---|
| 3 Numbers (recheck) | **FAIL** — 3 of 6 checks pass; the repair's blanket claim is false | 70 §P rows + 30 §P.2 derivations + 24 §R rows + 110 `quantitative.csv` rows (17 fenced `stage2-consequence`) + 141 rows across the other eight CSVs, parsed with Python `csv` (field counts **and** per-column content shape) + 41 arithmetic re-computations + 27 filing-line verifications across four documents + a digit-level transposition hunt | **9 rows in the failure table below: 0 of the 9 HIGH defects wrong, 3 repair-introduced, 6 pre-existing/unregistered** | None (auditor does not edit what it audits). Findings → failure table; register stays as AUDIT 3 wrote it | The spine (deficit, share count, the round, the 1995 money chain) is now right at source; the residue is in derived *labels* and in one field-placement slip |

**Bottom line on the repair's claim:** **26 of 31 confirmed fixed at the filing line; 2 refused by ruling (D10, D11)
— both refusals adjudicated correct, not omissions; 2 not fully closed (D15, D19); 1 fixed but with a new false figure
(D29).** All **9 HIGH** rows are genuinely fixed and each was re-derived from the primary, not from the log.

---

## 1. The seven items I was told to verify specifically

### (1) Accumulated deficit $(248,000), 52 + 303 − 107 shown as DERIVED — **CONFIRMED**
Filing: orig. balance sheet **l.3461** `Accumulated deficit...................................     (248)     (6,025)       (6,025)`
and the same figure as the 1995 closing balance of the statement of stockholders' equity, **l.3571**
` 1995...........  --  --  14,555,244  1,075  150  --  --  (248)  977`. Inputs filed at **l.3540** (1994 net loss `(52)`),
**l.3567** (1995 `(303)`), **l.3555** (reclassification `(107) / 107`), Note 1 **l.3713–3716**
`cumulative net losses of $107,000 incurred by the Company as of that date have been reclassified to common stock`.
−52 − 303 + 107 = **−248** ✓; equity cross-foot 1,075 + 150 − 248 = **977** ✓ (l.3457/3458/3461/3463).
**All sites agree on $(248,000) and the arithmetic is carried as DERIVED while the filed line stays FACT** —
`stage_1.md` l.114 (§A), l.551 (§K FY1995 result), l.559 (§K Year end), l.634–637 (§M), **P68** l.851, **d26** l.953–957,
l.1032 (§Q endpoint), l.1055/1056/1062 (§R Margins/Capital/Risks), `quantitative.csv` **L54** (FACT) + **L55** (relabelled
355,000 as `Sum of the two filed loss years`, DERIVED), `failures.csv` r7, `timeline.csv` r43, `context_appendices.md` l.553.
No live `355,000`-as-deficit assertion survives anywhere: every remaining `355` is inside a "sum of the two loss years,
not the deficit" cell or a correction note. ✓ **HIGH D04/D05/D06/D07 fixed.**

### (2) Share count 14,555,244 — **CONFIRMED, and it is a balance-sheet figure**
orig. **l.3455–3457** `Issued and outstanding shares -- 14,555,244 and / 15,900,237 at December 31, 1995 and 1996,`
`respectively (19,316,613 pro forma)`; identical count filed at l.3571 and **in A3 l.3672 and A5 l.3693/3815**, so the
boundary number is version-safe. Roll-forward verified: 10,200,000 + 4,235,244 + 120,000 = **14,555,244** ✓ (l.3531,
l.3546, l.3562, l.3571). The false null is **gone**: `no share count` survives only as the quoted string being deleted,
in `quantitative.csv` L86 ("the register previously carried a row asserting there was 'no share count'; there is one")
and L87 ("only the second half of that is true"). **No percentage was computed on it**: L86, §K l.553, P67 l.850 and
§R l.1056 each state it is a total and **not** a denominator for any holder's percentage, and the only ownership
percentages in the corpus are the filing's own (orig. l.2919 `9,885,000 48.3% 43.1%`; l.985–988 ~43%/10%), which carry
the filing's denominator. ✓ **HIGH D08 fixed.** (One caution, failure-table F-7.)

### (3) 100,020.06 replacing 100,019 — **CONFIRMED to the cent**
Inputs filed: orig. **l.2863–2864** `the Company sold 582,528 shares of Common Stock to Miguel / A. Bezos at a price per
share of $0.1717` (same sentence A5 l.3093–3094). Recomputation: **582,528 × 0.1717 = 100,020.0576 → $100,020.06** ✓
(the old $100,019.06 was short by almost exactly $1.00). Companion: 847,716 × 0.1717 = **145,552.8372 →
$145,552.84** ✓ (old `.83` was a truncation). d7 = 100,020.0576 + 145,552.8372 + 49,995 = **295,567.8948 → 295,568** ✓,
and on the exact ⅓ for Alberg **295,572.89** ✓, so "±$5" is right. Sites: P14/P15 l.805–806, d4/d5 l.877–880, d7 l.884,
§K l.554/562, `quantitative.csv` L22 (100020) / L24 (145553) / L34, `timeline.csv` r21, `validation.csv` r13. `100019`
occurs nowhere; `100,019` only in the "was wrong by exactly $1.00" notes. ✓ **HIGH D01 (see 4), D02, D03 fixed.**

### (4) The round re-expressed as division — **CONFIRMED; no row derives an aggregate from a displayed price**
Filing: orig. **l.4301–4302** `aggregate of 3,021,000 shares of Common Stock to 23 investors for a / consideration of
approximately $.3333 per share, or an aggregate of $1,007,000` (A5 l.4663 reads "23 purchasers"; both wordings kept).
**3,021,000 ÷ 3 = 1,007,000 exactly**; 1,007,000 ÷ 3,021,000 = 0.3̄; the product 3,021,000 × 0.3333 =
**$1,006,899.30**, i.e. the multiplication undershoots by **$100.70** — exactly the display artifact. `quantitative.csv`
**L98** now carries `1006899.30` with the division as the valid check and the direction stated; **L97** holds
`1007000` as FACT with "the aggregate governs". Sweep of every other aggregate: L31 `345525` cited as filed (Item 5 ¶2,
orig. l.4287–4289) with no arithmetic; L26 `5408` filed with the warning that `42,000 × $0.1287 = $5,405.40` and the
aggregate governs (orig. l.4294–4296; A5 l.4656–4658 adds "who is an employee"); L109 `8000014` filed (orig. l.4325;
A5 l.4655) and the product $8,000,013.80 is itself filed at orig. **l.8318** `TOTAL: 569,396 $8,000,013.80`; d22 and
L100 run `1,007,000 ÷ 23` as division ✓. No surviving row multiplies a rounded price into a filed aggregate.
✓ **HIGH D01 fixed; COR-10's corrected direction is honoured.**

### (5) The two refused items — **~$921,000 is still UNKNOWN, marked NOT ADOPTED, and the refusal was right**
`UNKNOWN` at P51 (l.842), **P70** (l.853), §R Capital (l.1056) and `quantitative.csv` **L99** (value cell `UNKNOWN`,
evidence_class `UNKNOWN`), with the candidate derivation recorded — not hidden — at **d25** (l.940–953), L99's
derived_arithmetic, §K l.555, §Q l.1029, `timeline.csv` r42, `data_gaps.csv` r10, `context_appendices.md` l.554. No file
puts $921,000 in a Stage-1 value cell ✓. Adjudication of the refusal, on the filing: the equity statement measures
shares **issued** in a cash year (l.3546) while Item 5 dates the program by **subscription window** (l.4300), and the
`Advances received for common stock 150` / `(50)` lines (l.3559, l.3546) prove consideration and issuance did not
coincide, so the subtraction bridges two different objects; the derivation also assumes the four Item 5 paragraphs
exhaust 1995. Crucially, the audit's own tie was wrong: **245,573 + 5,408 + 921,000 = $1,171,981**, not the
$1,171,978 printed in `amazon_s1_audit3_numbers.md` (l.186) and in `_parts/NUMBER_DEFECTS.md` (row 10) — the sum of the
three terms named does not equal the sum stated, so the "it ties" evidence for the replacement was itself defective
(it still rounds to the filed `1,172` at l.3546, so nothing substantive moves). AUDIT 3's fail-rule
("re-derive … if unrecoverable, replace with UNKNOWN and record the loss in `data_gaps.csv`") is satisfied: the loss is
registered at `data_gaps.csv` r10 and RD-020 stays open. **A refusal with the arithmetic and the reasons on the face of
the record is not an omission.** D11's *adopted* half is done: Alberg's 150,000 shares ($49,995–$50,000) are named as
the only individually dated in-window slice at P51, §K l.555, L96, L99 and d25. ✓

### (6) The repair log's three "the register was wrong" claims — **all three confirmed against the filing**
* **(a) The $50,000 overstatement** (`amazon_s1_number_repairs.md` §C(2)) — **confirmed.** The register's proposed
composition $5,408 + $150,000 + ≈$871,000 = $1,026,408 exceeds the $976,432 residual by $49,976 ≈ $50,000. The filing
shows why: 1994 `Advances received for common stock … 50` (**l.3535**) released against the 1995 sale
(**l.3546** `4,235,244  1,172  (50) … 1,122`), so CY1995 cash = 1,172 − 50 + 150 = **1,272** ✓ (l.3645). With the
−$50,000 term the written version foots. The repair was right to override the register; **but see failure-table F-4 for
the mislabel the replacement text introduced.**
* **(b) The tie off by 3** (§C(3)) — **confirmed**, computed above; and the corrected sum is what is now printed
(d25 l.945, L99).
* **(c) Two point values that needed a band** (§C(4)) — **confirmed on the arithmetic**: 511,000 ÷ (5.5 × 4.345) =
**21,382.99** and 511,000 ÷ (184/7 = 26.2857) = **19,440.22** ✓, and the day of July 1995 really is undisclosed
(MD&A **l.1377–1378** gives only "the opening of the Amazon.com bookstore in July 1995"; the 1994 caption at l.343–346
is a different period), so naming one end would repeat D18's error. d24 (l.933–939) and d30 (l.966–970) are the single
stated convention and every carrier now reads the band: P22 l.813, §A l.108, §K l.549, §R l.1053, L38,
`decisions.csv` r12, `context_appendices.md` l.552. No "≈5.5 months" point-claim or "~26-week" survives outside the band
text. **The half of this item that fails is the phantom CSV twin — F-3.**

### (7) The six checks re-run on the whole §P table and all nine CSVs — see §2 and the failure table.

---

## 2. Check-by-check result

### CHECK 1 — BASIS: **FAIL** (0 registered basis rows unfixed · 3 residuals, of which 1 is a repair claim)
Verified correct at the filing: net sales definition (orig. **l.1433–1435** "net of returns, as well as outbound
shipping and handling charges") ✓; "visits (not 'hits')" (l.450, A3 l.336, A5 l.338) ✓; gross margin
"approximately 20%" (l.1445–1446) ✓; marketing "39% in each of 1995 and 1996" (l.1462–1463) ✓; company-wording pairings
kept in the right column ✓; FY = calendar with the 179-day 1994 stub, and the S→C election at 1995-03-31 (l.3712–3716)
handled ✓; 4,800,000 now labelled **1997 split-restated** with the foot 3,052,974 + 110,640 + 1,636,386 = 4,800,000
(l.2707–2711, all three numbers verified) and the ÷6 = 800,000 flagged as never printed ✓ (L7, `timeline.csv` r11, §Q
l.1000); "floor strike" withdrawn everywhere and replaced with the observed range + the director-grant rule (l.2709,
l.3874) ✓; capex split into **cash-paid 28 + 52 = 80** (l.3639) vs **accrual 73 + 8 + 0 = 81** (l.3798–3803) with the
$1,000 gap declared unreconcilable and no plug invented ✓ (d15a, L69); the IDC numerator/denominator mismatch is now
stated at P49 **and** L83 and L84 is dated `1995 (whole year)` ✓; trading period is one band (item (5c) above) ✓.
Residuals: **F-5** (`quantitative.csv` L81 unit still `counts` while §P50 says "markets served (states; countries)"),
**F-6** (>$16,000,000 cumulative still not labelled cumulative-ship-basis-through-date at §P60/L103 — the tie
0 + 511 + 15,746 = 16,257 vs filed "more than $16 million", l.447), **F-3** (§R's per-week row).

### CHECK 2 — PROVENANCE / VERSION ATTRIBUTION: **FAIL** (all 9 HIGH attribution items verified; 1 error elsewhere)
Every version claim tested against the four documents, string by string:
| Claim | Test | Result |
|---|---|---|
| "Cadabra, Inc." + 1,700,000 + "sole stockholder on September 15, 1994" = **original only** | `grep -c Cadabra` orig **1**, A3 **0**, A5 **0** | ✓ COR-02 held; "Cadabra" absent from A5 as §U.4 says |
| 11 employees **filed at 1995-12-31** | A3 **l.797** / A5 **l.796** `From December / 31, 1995 to March 31, 1997, the Company expanded from 11 to 256 employees`; orig **l.667** `1, 1996 to December 31, 1996, the Company expanded from 11 to 151 employees` | ✓ COR-12 applied at P42, §R l.1046, L74, `timeline.csv` r49, `context_appendices.md` l.552; the stale COR-03 note is gone and COR-03 now appears only as "superseded" |
| 151 is original-only | `\b151\b` in A3/A5 → only `1516 SECOND AVE` (6 hits), zero as a headcount | ✓ P61, L102 re-keyed to the original, 151/158/256 kept on their own dates and never reconciled (158 = 10-K405 **l.729**, Item 1 *Management of Potential Growth* ✓ correct location) |
| December-1996 trio original-only, superseded by the March-1997 trio | orig l.446–450 (`>$16 million … 180,000 … 50,000`); A3 l.334–340 / A5 l.336–342 (`>$32 million … 340,000 … 80,000 … Time … "Best Websites of 1996"`) | ✓ P60, L103 and the S0804 re-key quote the amendments **verbatim**; `sources.csv` S0804 downgraded for the off-disk accession and no Stage-1 row cites it |
| 3,021,000 / 23 investors vs purchasers; A5-only decomposition | orig l.4301–4302 (no breakdown); A5 **l.4663–4668** `The purchasers consisted of one director … Tom A. Alberg, who / purchased 150,000 shares … two investors who are related to the / founder … 60,000 … and 20 unaffiliated / investors who purchased 2,811,000 shares` | ✓ P69/L96 cite No. 5 only, source_date `1997-05-14 (No. 5 only)`, marked "amendment-stage addition, NOT corroboration"; 150,000 + 60,000 + 2,811,000 = 3,021,000 ✓ and 1 + 2 + 20 = 23 ✓ |
| 42,000 @ ≈$0.1287 = $5,408 in **every** version | orig l.4294–4296; A5 l.4656–4658 (`who is an employee`) | ✓ D09: entered at P66, §K l.554, §Q l.1018, `timeline.csv` r29, L25/L26, §U; "two prices inside one year" and "second and third internal price points" now survive only as quoted retired wording |
| 10,200,000 in both versions + giving-effect basis | orig l.2848 and l.4280; **l.4276–4278** `a three-for-two stock split … to be effected prior to the closing of the offering` | ✓ D31: L4 now cites both accessions with the restated-presentation caveat |
| $107,000 / $8,000,014 / $345,525 / $5,408 / 14,555,244 / (248) / 17 / 83 / 1,272 | orig l.3715, l.4325, l.4289, l.4296, l.3455, l.3461, l.3429, l.3634, l.3645 — and each present in A5 too (l.4033, l.4691, l.4652, l.4658, l.3693, l.3701, l.3663, l.3920, l.3790) | ✓ no version in the record is cited for a figure it lacks |
| CEO only from May 1996 | 10-K405 **l.965–966** `Chief Executive Officer since May / 1996`; orig l.2847–2849 present-tense "President, Chief Executive Officer and Chairman" for the July 1994 purchase | ✓ D30: §R l.1045 cites Item 10 and explains why the S-1 sentence is not a 1994 title claim |

**F-8 (new, outside the 31):** `conflicts.csv` r30 and `stage_1.md` l.1853–1854 attribute "approximately **41%**" for
Bezos to the **original** S-1's Risk Factors (`claim_a_source: S0801 Form S-1 (original) … Risk Factors`,
`claim_a_date: 1997-03-24`). The original says **43%**: l.985–988 `approximately 43% by Jeffrey / P. Bezos … and 10% by
members of Mr. Bezos' family and trusts … (42% and 10%, respectively, if the over-allotment option is / exercised)`;
`41%` is **A5 l.1055–1062**, whose Principal Stockholders table also differs from the original's (A5 l.3149
`47.4%  41.4%` vs orig l.2919 `48.3%  43.1%`). A version-attribution error of exactly the COR-01/COR-02 class,
pre-existing (conflicts.csv was outside both the AUDIT 3 brief and the repair's edits).

### CHECK 3 — ARITHMETIC: **FAIL** (3 originally-failing results recomputed clean; 3 new/pre-existing bad statements)
Re-ran all 30 §P.2 derivations and all 27 populated `quantitative.csv` `derived_arithmetic` cells. **Clean:** d1
0.0058824 ✓; d2 0.00098039 and 10,200,000 ÷ 1,700,000 = 6 ✓; d3 179 = 26+31+30+31+30+31 with the excludes-5-July
convention now stated ✓; d4 100,020.0576 ✓; d5 145,552.8372 ✓; d7 295,567.8948 ✓; d8 976,432 ✓; d9 19.961 ✓;
d10 406 = filed ✓; d11 0.5949 ✓; d12 38.7476 with the ±500 band 38.61–38.88 ✓; d13 284 ✓; **d14 996 ✓ but see F-2**;
d15 57 and 5 + 19 = 24 = filed accumulated depreciation ✓; d15a 80 vs 81 ✓; d16 17 = filed l.3429 ✓; d17 3.33 ✓;
d18 46,454.5 ✓; d19 0.1607% ✓; d20 2,100,000 / 2.5× ✓ mixed-year warning present; d21 3.507 ✓; d22 43,782.61 ✓;
d23 245,572.8948 ✓; d25 2,763,000 / 921,000 / 258,000 / 86,000 / 1,171,981 ✓; d27 5,405.40 ✓; d28 14,555,244 and
15,900,237 ✓; d29 both ways ✓; d30 21,383 / 19,440 ✓; L98 1,006,899.30 ✓; L108 2,100,000 ✓.
**Wrong:** **F-1** the +95.2% sensitivity; **F-4** the $871,024 "exact ⅓" label; **F-2** the cash-bridge line; and a
one-cent cosmetic slip (the printed addends 100,020.06 + 145,552.84 + 49,995 sum to 295,567.**90**, the exact products
to 295,567.89 — the → $295,568 rendering is unaffected).

### CHECK 4 — CROSS-FOOT §P ↔ §R ↔ `quantitative.csv`: **FAIL** (spine holds; 2 breaks)
Mechanical: all **70** §P rows carry a numeric value with a twin in `quantitative.csv` (0 orphans) ✓. §P ↔ §R spine
re-checked value by value: 511,000 / 102,000 / ≈20.0% / 406,000 / (304,000) / (303,000) / 39.1% / 996,000 / 920,000 /
1,084,000 / 977,000 / (248,000) / 14,555,244 / 11 at 1995-12-31 / 2,200 / >1,000,000 / 10–40 / $3.00 + $0.95 /
1,272,000 / 295,568 / ≈976,000 / 44,000 / 0 LT / 81,000 + 8,000 / 17,000 / 38.7% — **all three files agree** ✓.
Balance sheet foots end-to-end (996 + 17 + 14 = 1,027; + 57 = 1,084; 99 + 8 = 107; 1,027 − 107 = 920;
1,075 + 150 − 248 = 977; 107 + 977 = 1,084 ✓ l.3427–3467). P&L ties ✓ (409 + 102 = 511; 200 + 171 + 35 = 406;
511 − 409 − 406 = −304; −304 + 1 = −303; 10-K405 l.1176–1189 repeats 511/409/102/200/171/35/406/(304)/(303)/(52) ✓).
Quarterly 875 + 2,230 + 4,173 + 8,468 = 15,746 ✓. 1994 stub 60 + 44 − 24 − 28 = 52 ✓; 38 + 14 = 52 ✓; 10 + 50 − 52 = 8 ✓.
MD&A control total 60 + 1,272 + 231 = 1,563 → "totaled $1.6 million" (l.1663–1665) ✓.
**Breaks:** **F-3** (§R claims a `quantitative.csv` row that does not exist) and **F-9** (`validation.csv` r20 —
§P39/L70 say FACT (audited), the register's own class column says DERIVED).

### CHECK 5 — UNIT AND CURRENCY HYGIENE: **PASS**
Parsed all nine CSVs: field counts equal the header in every row (111/110 data rows in `quantitative.csv`, then
58/57, 30/29, 34/33, 16/15, 24/23, 16/15, 103/102, 43/42 — matching the repair's §F table exactly), and — the check the
count test cannot make — **column content** was pattern-tested: `company` = `Amazon.com` everywhere, `stage` ∈
{stage1, stage2-consequence}, `source_id` cells all match `S\d{4}` in `sources.csv` (102 rows, 0 non-canonical), no
empty `url` (absent values read `UNKNOWN`, so the §13 empty-cell defect is closed), money rows carry `USD`, and the
unit vocabulary is 24 controlled values with no prose leaking in. **The only content misplacement found is F-9.**
Thousands→dollars conversion is clean (filed `511`, `15,746`, `406`, `1,272`, `(248)` → 511,000 / 15,746,000 / 406,000 /
1,272,000 / 248,000; P59 keeps the filed "(thousands)"); a digit-level transposition hunt over all FACT-class value
cells found **zero** mismatch against the four filings (the only non-literal hits are `0.1717` filed as `$.1717`,
`318,000,000` filed as "$318 million" (l.1774), `>$16,000,000` filed as "more than $16 million" (l.447), and the
multi-value cells L102/L103/L81/L82) — `$8,000,140`, `1006999`, `976432`, `100019`, `355000`-as-deficit appear nowhere
as live values. Fence: **17** `stage2-consequence` rows in `quantitative.csv` (15 + the 2 new program rows), `validation.csv`
r26–r28 now `stage2-consequence` ✓ (D21 fixed), and **no** `stage1` row in any CSV carries a 1996/1997 *metric* date
(the only stage1 rows with later dates are 2026-09-23 archive-status records and one `REJECTED AS EVIDENCE` row — provenance
log, not metric). Nominal marking improved from 17 to **24** rows naming "nominal 1995/1994 dollars"; §P's basis block
still has no global nominal sentence (F-6b, cosmetic, never registered).

### CHECK 6 — PRECISION LAUNDERING: **PASS**
Both material items are fixed at source: the six-significant-figure residual is now `976000` rendered
"≈$976,000 (±$1,000)" with the honest span ≈$974,900–$977,900 stated (L35, P20, §R l.1056, §K l.556,
`data_gaps.csv` r11), and the inventory line is no longer laundered *down* — `17000` as **FACT (audited)** with the cash
movement demoted to corroboration (L70, P39; `validation.csv` r20's *notes* say the same, its class column does not —
F-9). §P.2 now prints an explicit precision rule (l.867–870) and applies it: ≈20.0 / ≈38.7 / ≈3.3 / ≈$0.59 /
≈$46,000 / ≈0.16 with the exact products kept visible so the d-chain still foots. Discipline that held: `$50,000 each`,
`$1.1M / 22 friends`, `2,300%`, `July 16`, `$12,000/$14,000`, `~$5M/20%`, `245,572`, parental `$150,000/almost $250,000`
appear only as retired/legend with their lineages; UNKNOWN is used rather than a false precise value at P52–P54,
P70, L87–L94, L99. Residual (disclosed by the repair, and the register named only `stage_1.md`): `quantitative.csv`
value cells keep two-decimal exacts (19.96 / 39.1 / 3.33 / 0.595 / 0.161 / 46455) where §P renders one decimal —
each carries its `derived_arithmetic`, so it is a rendering asymmetry, not manufactured exactness.

---

## 3. Failure table — exact file, line/row, current value, filing's value
No row below was repaired by this auditor. "orig./A3/A5/10-K405" = the primaries in `.../company_001_amazon/sources/`.

| # | file | line / row | current value (verbatim) | the filing's value / the correct statement | evidence | severity | in the 31? | origin |
|---|---|---|---|---|---|---|---|---|
| **F-1** | `stage_1.md`; `quantitative.csv` | l.808 (**P17**), l.881–883 (**d6**); L30 `derived_arithmetic` | "`+94.1 (displayed prices) / **+95.2 (exact ⅓)**`"; d6: "on the filing's exact ⅓ ($1,007,000 ÷ 3,021,000) the same Feb→Dec step-up is **+95.2%**"; L30: "`+95.2% on the filing's exact 1/3`" | **(⅓ − 0.1717) ÷ 0.1717 = 0.94137 → +94.1%**, not +95.2%. The two conventions differ by **0.02 points**, not 1.1. To yield 95.2% the February price would have to be $0.1708, which is in no filing. The ⅓ itself is right (3,021,000 ÷ 3 = 1,007,000) — the step-up computed with it is wrong | orig. l.2864, l.4301–4302 | **MEDIUM** (a stated derivation that does not compute, in 3 sites) | row 29 (LOW) — the *figure* is new | **introduced by the repair** (absent from `stage_1.md` before 8eb9f86; imported from `amazon_s1_audit3_numbers.md` l.137's parenthetical) |
| **F-2** | `stage_1.md`; `quantitative.csv` | l.904 (**d14**); L66 `derived_arithmetic` | "`52 − 232 − 52 + 1,228 = +944; 52 + 944 = $996`" / "`52 − 232 − 52 + 1,228 = 944; 52 + 944 = $996`" | The left-hand side equals **996**, not 944. The filed bridge is: net increase **944** = −232 − 52 + 1,228, then opening 52 + 944 = closing **996**. §P36 (l.827) already prints it correctly | orig. l.3636, l.3639, l.3645, l.3653–3657 (`Net increase in cash … 52 944 5,252`) | LOW (notation; every endpoint filed and the tie holds) | not registered | pre-existing; **AUDIT 3 passed it** ("PASS + tie confirmed") and the repair copied it |
| **F-3** | `stage_1.md` | l.1063 (§R "Weaknesses") | "`≈$19,400–$21,400 average net sales per trading week (DERIVED at §P.2 d30 and **carried in `quantitative.csv`**)`" | There is **no such row** in `quantitative.csv`: no metric or value cell in any of the 110 rows contains 19,400 / 21,400 / 19440 / 21383 / "trading week". The register's own should_be was "carry it into §P.2 **+ `quantitative.csv`**" — §P.2 d30 exists, the CSV row does not, and §R asserts it does | file scan of all 110 rows | **MEDIUM** (false cross-reference + D19 only half done) | row 19 (MEDIUM) | **introduced by the repair** |
| **F-4** | `stage_1.md`; `quantitative.csv`; `data_gaps.csv`; `context_appendices.md` | l.894 (**d8a**); L35 notes; r11 `best_available_evidence`; l.553 | "`+ ≈$871,024` (2,613,000 unaffiliated program shares **at the filing's exact ⅓**)"; L35 prints "**≈$871,000** (2,613,000 shares at the filing's exact 1/3)" and then "Cross-foot: $5,408 + $150,000 + **$871,024** − $50,000 = $976,432 ✓" | 2,613,000 × ($1,007,000 ÷ 3,021,000) = **$871,000 exactly**. $871,024 is a **plug** back-solved from the displayed-price convention (1,272,000 − 295,568 − 5,408 − 150,000 + 50,000), so labelling it "the filing's exact ⅓" is false; with the true exact-⅓ leg the composition sums to 976,408, not 976,432 | orig. l.3535, l.3545–3546, l.3556–3559, l.3645; l.4301–4302 | LOW (inside the row's own ±$1,000 band, but the stated derivation and the two printed values contradict each other) | row 13 (MEDIUM) — the *label* is new | **introduced by the repair** |
| **F-5** | `quantitative.csv` | L81 (line 81) `unit` | `counts`, for value "50 states / >45 countries" | §P50 was corrected to "`markets served (states; countries)`" plus "**MARKETS-SERVED COUNTS, not customers, orders or accounts**"; the CSV twin still invites the customer reading. Its `notes` also never state the markets-served basis | orig. l.1433–1435 (basis discipline); press release 1995-10-04 | LOW (basis label) | AUDIT 3 Check 1 item 8 — **never registered as a row**, so the repair never owned it | pre-existing, unfixed |
| **F-6** | `stage_1.md`; `quantitative.csv` | l.860 (**P60**); L103 (line 103) | "`>$16,000,000 cumulative`" / unit `USD` and `accounts and USD`, with no statement that this is **cumulative net sales on the same ship basis through 1996-12-31**, not a period's revenue and not GMV | Filed: "Through December 31, 1996, Amazon.com had sales of more than $16 million" (orig. l.447–448), and it ties to the audited series 0 + 511 + 15,746 = **16,257** thousands ✓ | orig. l.447–448, l.3489/3490 (511 / 15,746) | LOW (basis label; the number itself is right) | AUDIT 3 Check 1 item 6 — **never registered as a row** | pre-existing, unfixed |
| **F-7** | `stage_1.md` | l.850 (**P67**), l.963–964 (**d28**) | "`15,900,237 (1996-12-31)`"; "`14,555,244 + 840,534 + 504,459 = 15,900,237 … ✓`" | Correct **for the original** (l.3456) and the roll-forward does foot (14,555,244 + 840,534 + 504,459 = 15,900,237). But the amendments restate it: A5 l.3693 and l.3843, A3 l.3672 file **15,900,229** — an 8-share variance the record does not explain. The tie is therefore version-specific and the row does not say so | orig. l.3455–3457, l.3582/3585; A3 l.3672; A5 l.3693, 3843 | LOW (post-boundary figure only; the Stage-1 count 14,555,244 is identical in all three versions) | not registered; found by this recheck | pre-existing |
| **F-8** | `conflicts.csv`; `stage_1.md` | r30 (line 30) `claim_a` / `claim_a_source`; l.1853–1854 (U.29) | "…with Risk Factors stating approximately **41%** for Bezos and approximately 10% for family and trusts", sourced to "`S0801 Form S-1 (original) … Risk Factors`", dated `1997-03-24` | The original's Risk Factors say **43%**: "approximately 43% by Jeffrey P. Bezos … and 10% by members of Mr. Bezos' family and trusts (42% and 10%, respectively, if the over-allotment option is exercised in full)". 41% is **S-1/A No. 5** l.1055–1062 — and A5's own Principal Stockholders table is 47.4%/41.4% (l.3149), not 48.3%/43.1% (orig. l.2919). The two versions must not be merged in one cited cell | orig. l.985–988, l.2919; A5 l.1055–1062, l.3149 | **MEDIUM** (version attribution — COR-01/COR-02 class) | not registered (conflicts.csv was outside AUDIT 3's brief and the repair's edits) | pre-existing |
| **F-9** | `validation.csv` | r20 (line 20), fields `evidence_class` and `confidence` | `evidence_class: DERIVED (cash-flow movement, $0 opening)` **and** `confidence: FACT (audited) - balance-sheet line` | The correction was written into the wrong column. `evidence_class` still asserts **DERIVED** — the exact value register row 15 ordered changed — while the confidence field now holds an evidence-class label and the previous `Medium-High` is gone. §P39 and `quantitative.csv` L70 both read **FACT (audited)**, so the three files still disagree on the class of $17,000 | orig. **l.3429** `Inventories...........................................       17         571` | **MEDIUM** (targeted field unfixed + column-content misplacement: field count correct, semantics shifted — precisely the trap the brief names) | row 15 (MEDIUM) — **NOT closed** | **introduced by the repair** (verified against `git show 461299b:validation.csv`, where confidence read `Medium-High`) |

**Cosmetic, not counted above:** ten CSV cells contain unbalanced literal `"` characters inside prose (8 of them
pre-existing — e.g. `quantitative.csv` L12, L44, L75, L81, L103, L106); `failures.csv` r26 `source_id` reads
`SEE-SOURCES-PENDING` instead of an S-id; `decisions.csv` r12 carries its AUDIT 3 correction note inside `claim_ref`
(that file has no notes column); `stage_1_claim_records.md` l.445 still prints the retired "`≈976,432 unnamed`" —
outside this brief's target set and outside the repair's declared file list, but it is the one dossier file where the
withdrawn figure survives un-hedged.

## Claims cut or downgraded
**None.** An auditor of a repair does not edit the repaired. F-1 … F-9 are registered here for a second repair pass;
F-1, F-3, F-4, F-9 are that pass's own making and must be re-audited, not trusted.

## Research debt opened by this audit
| RD id | Section | Debt | Assigned | Status |
|---|---|---|---|---|
| RD-024 (new) | §P.2 d6 / P17 / `quantitative.csv` L30 | Replace the false "+95.2% (exact ⅓)" with **+94.1% (both conventions; they differ by 0.02 points)** — or delete the sensitivity and state that the displayed price and ⅓ give the same step-up | Numbers repair pass (2nd) | OPEN |
| RD-025 (new) | §R Weaknesses / `quantitative.csv` | Either enter the per-trading-week row the §R cell promises (value `19440-21383`, DERIVED, arithmetic = d30) or delete "carried in `quantitative.csv`" from §R. D19 is not closed until one of these happens | Numbers repair pass (2nd) | OPEN |
| RD-026 (new) | `validation.csv` r20 | Move `FACT (audited) - balance-sheet line` from `confidence` into `evidence_class` and restore a real confidence value; re-run the column-content test, not just the field-count test | Numbers repair pass (2nd) | OPEN |
| RD-027 (new) | d8a / L35 / `data_gaps.csv` r11 / appendices l.553 | Re-label the ≈$871,024 leg honestly: a balancing plug under the displayed-price convention, **not** "2,613,000 at the filing's exact ⅓" (= $871,000) | Numbers repair pass (2nd) | OPEN |
| RD-028 (new) | U.29 / `conflicts.csv` r30 | Split the 41%/43% and 47.4%/48.3% figures by accession (orig. l.985–988, l.2919 vs A5 l.1055–1062, l.3149); one cell may not carry both versions under a 1997-03-24 label | Evidence Registrar / AUDIT 2 owner | OPEN |
| RD-029 (new) | §P60 / L103 / L81 / §P basis block | Three unregistered basis labels: cumulative-ship-basis-through-date for >$16,000,000; markets-served unit in the CSV twin; a global "all money is nominal 1994–95 dollars" sentence in §P | Company Lead | OPEN |
| RD-020 (AUDIT 3) | K / P | Still **OPEN** by design: the in-window split is held UNKNOWN with the candidate at d25. If it is ever adopted, it must be re-derived with the tie printed as **$1,171,981**, and only against subscription-dated evidence | Company Lead (money) | OPEN — refusal verified as correct this pass |
| RD-021/022 (AUDIT 3) | P/R/S, protocol | RD-021's substance (share count, deficit, A5 decomposition) is **now closed** by this recheck; RD-022 (the false Nov–Oct fiscal-year premise in `AUDIT_PROTOCOLS.md` 3.1) is untouched — the repair was right that protocol text is not dataset work, and orig./A3/A5 l.44 and 10-K405 l.45 all read `FISCAL YEAR END: 1231` | Master Orchestrator | OPEN (protocol text) |
| RD-023 (AUDIT 3) | T | S0804 re-keyed to A3 l.334–341 / A5 l.336–342 (quotes verified verbatim this pass) and S0806's url now `UNKNOWN` not empty; the off-disk accessions remain unrestored | Evidence Registrar | PARTIALLY CLOSED |

## Sign-off
Stage status: RECONSTRUCTION → ADVERSARIAL REVIEW → **QA (AUDIT 3 recheck = FAIL: 26/31 confirmed fixed at source, 2
authorized refusals verified, 2 rows not fully closed (D15, D19), 1 row fixed with a new false figure (D29); all 9 HIGH
defects confirmed correct against the filings; 9 failure-table rows, 4 of them created by the repair)** → COMPLETE blocked.

The material spine is now right and provably so: **$(248,000)**, **14,555,244**, **$100,020.06 / $145,552.84 /
$295,568 (±$5)**, **$1,007,000 governing $0.33̄**, **$5,408 as a filed aggregate**, and the ~$921,000 slice held at
UNKNOWN with its arithmetic preserved. What failed this pass is the layer above it — one fabricated sensitivity, one
half-implemented fix that points at a register row that does not exist, one correction written into the wrong column,
and one plug presented as a filed product. Those are the four things a second repair pass owns; none of them is a reason
to doubt the 26 that were done properly, and none of the 9 HIGH items is in question.
