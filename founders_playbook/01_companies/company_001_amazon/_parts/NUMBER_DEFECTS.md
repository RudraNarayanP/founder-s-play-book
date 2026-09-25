# NUMBER_DEFECTS — Amazon Stage 1 · AUDIT 3 (Numbers) register
Produced 2026-09-23 by the Level-3 Numbers Auditor. **Repair pass owns every edit** — this file is the only
output of that audit besides the audit sheet. Severity: **HIGH** = wrong figure, wrong version attribution, or
post-boundary value presented as Stage 1 · **MEDIUM** = missing basis or unshown/unrecoverable-when-recoverable
derivation · **LOW** = style/wording. `line_or_row` = file line number (header = line 1) and, for `stage_1.md`,
the §P/§R/§K row ID as well; §P and §R line numbers are as read 2026-09-23 and may shift while other agents edit — **`stage_1.md` did move
under this audit** (the §P table shifted twice), so anchor repairs on the row ID (`P32`, `d7`, `§R "Capital"`) and
re-locate the line at repair time.
Evidence lines are `sources/S-1_original_acc-0000891618-97-001309_filed-1997-03-24.txt` (= "orig."),
`sources/S-1A-No3_…-1997-05-09.txt` ("A3"), `sources/S-1A-No5_…-1997-05-14.txt` ("A5"),
`sources/10-K_FY1997_acc-0000891020-98-000448_filed-1998-03-30.txt` ("10-K405").

| file | line_or_row | field | current_value | should_be | evidence (document + line) | severity |
|---|---|---|---|---|---|---|
| `quantitative.csv` | r93 (line 93) | value + derived_arithmetic | `1006999` / "3,021,000 × $0.3333 ≈ $1,006,999" | `1006899.30`, and re-express the check as division: $1,007,000 ÷ 3,021,000 = $0.3333̄ (the filed `$.3333` is the rounded display; 3,021,000 ÷ 3 = 1,007,000 exactly, so the aggregate governs and multiplying the rounded price undershoots by ≈$100.70) | orig. l.4301–4302 "aggregate of 3,021,000 shares … approximately $.3333 per share, or an aggregate of $1,007,000"; A5 l.4663–4664 | **HIGH** |
| `quantitative.csv` | r22 (line 22) | value + derived_arithmetic | `100019` / "582,528 × 0.1717 = $100,019.06" | `100020` / "$100,020.06" (582,528 × 0.1717 = 100,020.0576) | orig. l.2863–2864 "the Company sold 582,528 shares … to Miguel A. Bezos at a price per share of $0.1717"; A5 l.3094; §P14, `timeline.csv` r21 and `validation.csv` r13 already print ≈$100,020 | **HIGH** |
| `stage_1.md` | §P.2 d4 (line 855) | derived arithmetic | `582,528 × 0.1717 = $100,019.06` | `$100,020.06`; also fix d5's cent ($145,552.84) | same as above; recomputation | **HIGH** |
| `stage_1.md` | §K row "FY1995 result" (line 545) | cumulative loss figure | `cumulative $(355,000) DERIVED` | `accumulated deficit $(248,000) (FACT, audited)`; keep $355 only as "the two loss years, $52 + $303, before the $107,000 reclassified to common on ending the S-election" (52 + 303 − 107 = 248) | orig. balance sheet l.3461 "Accumulated deficit … (248)"; equity statement l.3560–3571 "(107) … 107"; Note 1 l.3713–3716 "$107,000 … reclassified to common" | **HIGH** |
| `stage_1.md` | §M bullet (line 628) | cumulative loss figure | `cumulative $(355,000) DERIVED` | `accumulated deficit $(248,000) as filed` (same reconciliation) | as above | **HIGH** |
| `quantitative.csv` | r52 (line 52) | value + metric + derived_arithmetic | `355000` / "Cumulative losses since inception" / "52 (1994 stub) + 303 (1995) = 355" | split into two rows: **`248000` "Accumulated deficit at 1995-12-31 (audited)" FACT**; and, if kept, relabel 355,000 as "sum of the two filed loss years, not the filed deficit", arithmetic `52 + 303 − 107 = 248` | orig. l.3461, l.3571, l.3713–3716 | **HIGH** |
| `failures.csv` | r7 (line 7) | notes | "cumulative deficit by 1995-12-31 was $355,000 (DERIVED 52 + 303)" | "the audited accumulated deficit at 1995-12-31 is **$248,000**; the $107,000 reclassified to common is why the two loss years (355) do not sum to it" | orig. l.3461 / l.3571 | **HIGH** |
| `quantitative.csv` | r83 (line 83) | notes (and the missing metric it denies) | "Two private price points exist …; **no share count** and no valuation" | share count **is** filed: delete the null, and add a row `1995-12-31 / Common shares issued and outstanding / 14,555,244 / shares (restated basis) / orig. balance sheet / FACT (audited) / High`; the whole-company *valuation* may remain UNKNOWN (also on file: 17,008,158 shares at 1997-02-28 — post-boundary) | orig. l.3455–3457 "Issued and outstanding shares -- 14,555,244 and 15,900,237 at December 31, 1995 and 1996"; l.2978 | **HIGH** |
| `quantitative.csv` | r28 (line 28) | notes + missing row | "Two private sales at two prices inside one year" | "Three priced common-stock issuances to outsiders in CY1995 at **three** prices: $0.1717 (Feb 9), **$0.1287 (Aug 7, 42,000 sh, aggregate $5,408)**, $0.3333 (Dec)"; add the missing August 1995 row (date 1995-08-07) | orig. Item 5 ¶3 l.4293–4295; A5 l.4656–4658 adds "who is an employee" | **HIGH** |
| `stage_1.md` | §K "The 23-purchaser program, as filed" (line 549) | in-window split | "the filings do not disaggregate it by date, so the in-window amount is **UNKNOWN**" | **DERIVED, arithmetic shown: ≈$921,000 in-window / ≈$86,000 post-boundary.** 4,235,244 (1995 shares sold, equity statement) − 582,528 − 847,716 − 42,000 = **2,763,000** program shares subscribed in 1995 → × $1,007,000/3,021,000 (= ⅓) = **$921,000**; 3,021,000 − 2,763,000 = 258,000 → **$86,000**; consideration tie: 245,573 + 5,408 + 921,000 = $1,171,978 → filed **$1,172** | orig. equity statement l.3555–3571 (sale of common stock 4,235,244 sh / 1,172 / (50) / 1,122); l.2863–2873 (582,528 / 847,716 / 150,000); l.4293–4302 | **MEDIUM** (recoverable figure left UNKNOWN; AUDIT 3 fail-rule → re-derive) |
| `stage_1.md` | §P51 (line 833) and §R "Capital" (line 958) | boundary-straddle qualifier | "only an undated part closed in 1995" / "its in-window portion is **UNKNOWN**" | keep "straddles the boundary", but replace UNKNOWN with the DERIVED ≈$921,000 (2,763,000 sh) above and add that Alberg's 150,000 shares ($49,995–$50,000) are the only *individually dated* in-window slice | as above; A5 l.4665–4668 | **MEDIUM** |
| `quantitative.csv` | r91 (line 91) and r92 | missing evidenced decomposition | roster/amount fields carry only "3,021,000 to 23 investors ≈$0.3333" | add the S-1/A No. 5-only decomposition as its own row: **Alberg 150,000 + two founder-related investors 60,000 + 20 unaffiliated 2,811,000 = 3,021,000; 1 + 2 + 20 = 23** (cross-foots both ways; the original lacks it, so cite No. 5 and mark it post-original-only) | A5 l.4663–4668; orig. l.4300–4302 (no breakdown) | **MEDIUM** |
| `quantitative.csv` | r33 (line 33) | value + notes | `976432` / "IDENTITY UNKNOWN. Upper bound … because it absorbs commingled option-exercise proceeds" | value **≈976,000 (±$1,000)** — the input $1,272 is filed in thousands; notes: 1995 option exercises are recorded at **$0** in the audited equity statement, so the residual is **not** explained by option cash; it comprises the disclosed $5,408 (Aug-1995 employee purchase), **$150,000 of advances received for shares not yet issued at 1995-12-31**, and ≈$871,000 (2,613,000 shares) of unaffiliated program purchases **[THAT FOURTH LEG IS WITHDRAWN 2026-09-25 — `2,613,000` is unfiled (0 occurrences in all four restored documents) and `≈$871,000` is not a canonical figure; the composition of the residual is UNKNOWN and only $5,408 + $150,000 − $50,000 = $105,408 is filed. See the AUDIT-7 ADDENDUM at the foot of this file, item 1.]** | orig. l.3555–3573 (Sale 4,235,244 → 1,122; Advances 150; Exercise of options 120,000 → `--`); l.3458; cash flow l.3645; Item 5 ¶3 l.4293–4295 | **MEDIUM** |
| `stage_1.md` | §P20 (line 802) + §P.2 d8 (line 857) | value + composition claim | `≈976,432` / "includes commingled option-exercise proceeds and is an upper bound" | `≈$976,000 (±$1,000)`; keep "identity UNKNOWN"; replace the option-cash clause with the $150,000-advances + $5,408 + ≈$871,000-unaffiliated decomposition **[THE THIRD TERM OF THAT INSTRUCTION IS WITHDRAWN 2026-09-25 — do NOT substitute ≈$871,000: the option-cash clause is rightly struck, but the replacement leg rests on the unfiled `2,613,000`. Execute the instruction as $150,000 + $5,408 − $50,000 = $105,408 filed, fourth leg UNKNOWN. See the AUDIT-7 ADDENDUM at the foot of this file, item 1.]** | as above | **MEDIUM** |
| `quantitative.csv` | r67 (line 67) (and `validation.csv` r20 line 20; §S/§K echoes) | evidence_class + value + derived_arithmetic | `17000` / `DERIVED` / "opening $0 + increase 17" | **`17000` as FACT (audited)** — the balance sheet files *Inventories … 17* at 1995-12-31; the cash-flow movement becomes corroboration, and the `≈` is unnecessary (only the 1994 $0 opening is inferred) | orig. balance sheet l.3429 "Inventories… 17"; cash flow l.3629 "(17)"; §P39 (line 821) carries the same fix | **MEDIUM** |
| `quantitative.csv` | r7 (line 7) (also `timeline.csv` r11 line 11; `stage_1.md` §Q line 903) | date/basis + notes | `1994-09-15 … 4800000 shares … "Floor strike $0.1717"` | state that **4,800,000 is the 1997 split-restated reserve** (it foots to the 1997-02-28 population 3,052,974 + 110,640 + 1,636,386 = 4,800,000; the 1994 as-adopted figure on the instrument basis would be ÷6); re-word "floor strike" as "the lowest exercise price outstanding at 1997-02-28", and label the date as adoption (1994-09-15) vs reserve-as-stated (1997 basis) | orig. l.2701–2711 "reserved an aggregate of 4,800,000 shares … approved by the Board of Directors and the sole stockholder on September 15, 1994 … As of February 28, 1997, options to purchase 3,052,974 shares … exercise prices ranging from $0.1717 to $4.00 per share"; director grants must be "not less than the fair market value" l.3874 | **MEDIUM** (1997-basis figure + 1997 observation sitting in a 1994-dated Stage-1 row) |
| `quantitative.csv` | r66 (line 66) vs r64 | unit/basis + cross-foot | "Cumulative Stage-1 capital expenditure `80000` = 28 + 52" against "Gross equipment at cost `81000`" | label r66 **cash-paid** capex (Purchases of equipment, 1994 + 1995) and reconcile the **$1,000** gap to the accrual gross-cost note (rounding in thousands and/or unpaid additions), or drop r66 and cite the filed 81,000 | orig. cash flow l.3639 "(28) (52) (1,214)"; Note 2 l.3797–3803 (73 + 8 + 0 = 81) | **MEDIUM** |
| `quantitative.csv` | r36 (line 36) + `stage_1.md` §P22 (line 804) + `decisions.csv` r12 | value vs its own span | `5.5` months for the stated span `1995-07-01 → 1995-12-31`, while `decisions.csv` r12 says "**~26-week** trading year" and §R says "≈5.5 months" in five places | one stated convention with a range: the filed month is "July 1995", so the trading period is **5.5–6.0 months (184 days = 6.0 months from 07-01; ≈5.5 from mid-July)**; show the arithmetic and fix `decisions.csv` to the same band | orig. l.343–346 / l.1377 caption "FOR THE PERIOD FROM JULY 5, 1994 (INCEPTION) TO DECEMBER 31, 1994"; MD&A "opened … July 1995"; A5 l.482 | **MEDIUM** |
| `stage_1.md` | §R "Weaknesses" (line 965) | value + derivation | "~$21,000 average net sales per trading week (DERIVED)" | either delete or carry it into §P.2 + `quantitative.csv` with the arithmetic: 511,000 ÷ (5.5 × 4.345) = **$21,383**, or 511,000 ÷ (184/7 = 26.3 weeks) = **$19,440** — state which convention | orig. Selected Financial Data l.355 (511); the two period readings above | **MEDIUM** (unshown derivation in a snapshot row that must cross-foot to §P.2) |
| `stage_1.md` + `quantitative.csv` + `validation.csv` | §P33 (line 815); r55 (line 55); r6 (line 6) | value | `38.75%` (MD&A says "approximately 39%") | **≈38.7%** — with both inputs filed in thousands the ratio's own band is 38.61–38.88%; 38.7476% is arithmetically right but one decimal is the ceiling the source supports | orig. Note 1 l.3722 "International sales were $198,000 and $5.1 million"; MD&A l.1437–1439 "approximately 39% and 33% … in 1995 and 1996, respectively"; 1996 check 5.1 ÷ 15.746 = 32.4% → "≈33%" ✓ | **MEDIUM** (false precision) |
| `validation.csv` | r26–r28 (lines 26–28) | stage | `stage1` while `date` = 1996-12-31 / 1997-03 / 1996 and `magnitude` = 180,000 accounts / 40 percent of orders / 15,746,000 USD | `stage2-consequence` — prose already says POST-BOUNDARY, but the field must carry the fence a query reads (the convention `quantitative.csv` r91–r105 follows) | orig. l.447–450 (Dec-1996 trio, original-only); A3 l.334–337 / A5 l.336–339 (Mar-1997 trio); 10-K405 Item 6 l.1186 | **MEDIUM** |
| `timeline.csv` | r39 (line 39) | notes | "the second and third internal price points of Stage 1" | "the third and fourth priced points of Stage 1 (Feb $0.1717, Aug **$0.1287**, Dec $0.3333)" once the 1995-08-07 issuance is entered | orig. Item 5 ¶2–¶4 l.4287–4302 | **MEDIUM** |
| `stage_1.md` | §P.2 d7 (line 857) | derived arithmetic | "100,019 + 145,553 + 49,995 = $295,567 **(dossier rounding: $295,568)**" | "= **$295,568** (100,020.06 + 145,552.84 + 49,995 = 295,567.89)" — the note is inverted: $295,568 is the accurate sum and $295,567 was the artifact of the bad d4 product; add that on the filing's exact ⅓ price for Alberg the total is $295,573, so ±$5 is the only honest precision | orig. l.2863–2873; recomputation | **MEDIUM** |
| `sources.csv` | S0804 row (line 54) | url / numeric claims | cites accession **0000891020-97-000868** (not in the restored primary set) for the $32 million / 340,000 accounts / 80,000 visits / Time figures | re-key those figures to A3 l.334–337 / A5 l.336–339 (on disk), or restore 0000891020-97-000868 with a retrieval header; no Stage-1 row depends on it | A3/A5 lines cited | **MEDIUM** (unverifiable citation for filed numbers) |
| `quantitative.csv` | r81 (line 81) | date | `1995-07-01` for "Web purchases of goods and services in 1995 (IDC) `318000000`" | `1995` (whole year) — r80 already uses `1995 (whole year)` for the same base; a July date invites a mid-year comparison | orig. l.1772–1774 "total value of goods and services purchased over the Web grew from $318 million in 1995" | LOW |
| `quantitative.csv` | r70 (line 70) | metric + notes | "Increase in accounts payable and accrued **liabilities** … Exact filed line label not re-verified in this register; carried at Medium" | "… accrued **expenses**" and close the hedge: the line is verified in both versions, 1995 = 83; confidence may stay Medium on the register's own convention | orig. cash flow l.3632–3633; A5 l.3919–3920 | LOW |
| `stage_1.md` | row **P32** ("Advertising expense (Note 1) 30,000"; line 815 as read 2026-09-23) | metric wording | "Advertising expense" | "Advertising expense **incurred**" — the filing's word is incurred, which is not the same assertion as expensed | orig. Note 1 l.3734–3736 "the Company incurred advertising expense of $30,000" | LOW |
| `stage_1.md` | §P.2 d3 (line 855) | derived arithmetic wording | "5 Jul → 31 Dec 1994 = 26+31+30+31+30+31 = 179 days" | keep 179 but state the convention (excludes 5 July; inclusive count = 180); immaterial to the no-annualisation point, which stands either way | orig. l.343–346 caption; "incorporated on July 5, 1994" l.3672 | LOW |
| `stage_1.md` | §P.2 d6/d9/d11/d17/d18/d19 (lines 856–865) | rendered precision | `+94.1%`, `19.96%`, `$0.595`, `3.33%`, `$46,455`, `0.161%` | one decimal / rounded where inputs are filed in thousands (19.96 → ≈20.0 and quote the MD&A's "approximately 20%"; 3.33 → ≈3.3; $46,455 → ≈$46,000/person; note that on the filing's exact ⅓ price the Feb→Dec step-up is +95.2%, not +94.1%) — **SUPERSEDED 2026-09-24 by number_repairs2: value corrected to +94.1%.** This clause is the origin of the false +95.2%: the step-up computes to 94.118 on the displayed prices and 94.137 on the filing's exact ⅓ (0.02 points apart, not 1.1), and +95.2% requires a February price of $0.1708, which is filed nowhere (orig. l.2864 files $0.1717). The clause is kept verbatim above because this register is the audit trail of how the number arrived; do not import it | orig. MD&A l.1435, l.1445–1446; Note 1 l.3722; Note 2 l.3803 | LOW |
| `stage_1.md` | §R "Founders" (line 947) | citation for a date | "Bezos, President and Chairman (**not CEO until May 1996**) … S-1 (orig.), Ex. 10.12 + Certain Transactions" | the title sequence must be cited to the **10-K405 Item 10 officer table** (10-K405 l.967 area; `sources.csv` S0805 already says "CEO only from May 1996"), because the S-1's own Certain Transactions sentence calls him "the President, Chief Executive Officer and Chairman" while describing the July 1994 purchase (orig. l.2847–2849) — the present-tense style is not a 1994 title claim | as above | LOW |
| `quantitative.csv` | r4 (line 4) vs §P03 (line 785) | source / source_date asymmetry | CSV cites only "S-1/A No. 5 … 1997-05-14"; §P cites "S-1 (orig.)/S-1/A No. 5 … 1997-03-24" | both versions carry 10,200,000 (orig. l.2848 Certain Transactions and l.4280 Item 5; A5 l.3078, l.4642): cite both, and note that the original states it on a **giving-effect** basis for a 3-for-2 split "to be effected" (l.4276–4277), so the restated count is a 1997 presentation, not a 1994 one | as above | LOW |

**Not defects — verified correct this pass (recorded so the repair pass does not "fix" them):** the 15
`stage2-consequence` rows are all properly fenced and dated; the 11 / 151 / 158 / 256 employee rows are kept on
their own dates and never reconciled (COR-12); P60/P61 are correctly re-keyed to the original S-1 (COR-14.1) and
`151` genuinely occurs zero times in A3/A5; the `158` is real (10-K405 l.729 — **Item 1, Management of Potential
Growth**, not Item 6); `$8,000,140` appears nowhere (the appendices' transposition did not propagate); the
`$245,572` claim is absent as a figure and correctly rejected (COR-14.2); COR-09's barred figures appear only as
retired/legend; every §P money row is nominal, thousands-correct, and net-sales-not-GMV; `511 + …` all P&L ties
(409 + 102 = 511; 200 + 171 + 35 = 406; 511 − 409 − 406 = −304; −304 + 1 = −303), the cash bridge
52 − 232 − 52 + 1,228 = 996, the depreciation tie 5 + 19 = 24, the 1995 balance-sheet cross-foot
(996 + 17 + 14 = 1,027; 1,027 + 57 = 1,084; 1,027 − 107 = 920; 1,075 + 150 − 248 = 977), the quarterly foot
875 + 2,230 + 4,173 + 8,468 = 15,746, 3,021,000 × ⅓ = 1,007,000, 569,396 × $14.05 = $8,000,013.80 → $8,000,014,
150,000 + 60,000 + 2,811,000 = 3,021,000, and 1,007,000 ÷ 23 = $43,782.61 → $43,783 all **PASS**.

---

**SUPERSESSION MARKERS — Level-3 register sweep, appended 2026-09-24. Nothing above this line was rewritten; this
register is the audit trail of how the numbers got here and stays as found.**

- **Row 43 (D29 rendered precision)** — the `+95.2%` clause in its `should_be` is the origin of the false step-up the
  first repair pass imported. **SUPERSEDED 2026-09-24 by number_repairs2: value corrected to +94.1%** (94.118 on the
  displayed prices / 94.137 on the filing's exact ⅓ — 0.02 points apart, not 1.1). Marker appended in the row itself.
- **Rows 27–28 (D19/D15 family, the residual and its composition)** — the instructions remain valid and their
  `should_be` leg reads **≈$871,000**, which is the canonical figure. **SUPERSEDED 2026-09-24 by number_repairs2 for
  the executed output only:** the first repair pass rendered that leg as a six-figure balancing plug
  (`1,272,000 − 295,568 − 5,408 − 150,000 + 50,000`), which was retracted — `2,613,000 × ($1,007,000 ÷ 3,021,000) =
  2,613,000 ÷ 3 = $871,000` exactly, so the composition foots to **$976,408**, not to the $976,432 residual arithmetic,
  and the $24 difference is accounted for (≈$19 filed-thousands rounding of the equity line + the ±$5 Alberg
  convention at d7), not plugged. **[AUDIT-7 MARKER, 2026-09-25 — the text above is left standing; this bullet's two
  operative claims are WITHDRAWN. Neither "≈$871,000 … the canonical figure" nor "the composition foots to
  $976,408" is true, the "$24 accounted for" explanation goes with the leg, and the citation
  `orig. l.4301–4302` does not carry the denominator. See the AUDIT-7 ADDENDUM at the foot of this file, row R4,
  and `stage_1.md` §P.2 d8a / §U.8.]**
- **Rows naming 43% / 41%** — this register carries none; the 43%/41% pair is a **version discrepancy** (43% = original
  S-1 acc. 0000891618-97-001309, l.985–988 / l.2919; 41% = S-1/A No. 5 acc. 0000891020-97-000839, l.1055–1062 /
  l.3149), to be kept visible per number_repairs2 item 6, never averaged or merged.
- Sweep log: `03_quality_control/amazon_s1_residual_sweep.md`.

**SUPERSESSION MARKERS — Level-3 register sweep ROUND 2, appended 2026-09-24. Again, nothing above was rewritten.**

- **Rows 27–28 and 43 — status: propagated beyond `quantitative.csv`/`stage_1.md` §P.** The copies the first two
  passes could not reach are now closed: `stage_1.md` **§K "Reconciliation of the two totals"** prints the composition
  at **$976,408** (band-level, retraction of the $871,024 leg shown in the row) instead of "= $976,432"; and
  `stage_1_claim_records.md` **P09** renders the residual as **≈$976,000 (±$1,000)** with a correction marker carrying
  the $976,432 arithmetic, the $976,408 composition and the retraction. **[AUDIT-7 MARKER, 2026-09-25 — text above
  left standing; both of its descriptions of the canonical sites are now FALSE and were the sibling this pass found
  by sweeping the folder instead of the named list. `stage_1.md` §K "Reconciliation of the two totals" (l.610) does
  **not** print a $976,408 composition — it states that no $976,408 total and no "$24 accounted for" claim survives;
  and P09 (`stage_1_claim_records.md` l.466) carries the **withdrawal** of the "cross-foot to $976,408", not the
  cross-foot itself. What is still true in this bullet: the residual is rendered **≈$976,000 (±$1,000)** at both
  sites, the $976,432 raw arithmetic is retained inside the retraction, and the $871,024 retraction stands. See the
  AUDIT-7 ADDENDUM at the foot of this file, row R4b.]**
- **Row 28's §B/§A sibling** — `stage_1.md` **l.184 §B.1 "Personal capital and ownership"** no longer prints the
  unattributed **"post-IPO ~41–43%"**: 43% is now attributed to the original S-1 (l.985–988) and 41% to S-1/A No. 5
  (l.1055–1062) in the row itself, per row 28's version rule and `conflicts.csv` r30. `stage_1_claim_records.md` **K14**
  carries the equivalent accession marker; its quoted 41% passage stands verbatim as the source's words.
- **Historical volumes marked, not rewritten** — `_parts/s1_p1.md` (l.52 range, l.70 composition), `_parts/s1_p3.md`
  (l.24), `_parts/s1_p4.md` (l.46, l.98, l.176, l.203) and `research/E_supply_ops_finance.md` (l.25 E-59 accession
  label; l.75, l.261, l.324 composition and the withdrawn option-cash clause) each received an appended
  `SUPERSEDED 2026-09-24` footer naming the site, the corrected value and where it lives. Their text above the footer
  is unchanged.
- **Still open, outside this sweep's write scope** — `_parts/s1_claims_KU.md` l.37 and `_parts/U_CONCORDANCE.md` l.60
  (the 41% without its accession) and `MASTER_RESEARCH_LOG.md` l.247. Reported for their owners; not edited here. The
  `stage_1_claim_records.md` coverage-note tally was raised in place to **77** with its sub-counts left un-rederived.
- Sweep log: `03_quality_control/amazon_s1_residual_sweep2.md`.

**AUDIT-7 ADDENDUM — appended 2026-09-25 (repair pass, rows R4 / R4b). Nothing above this line was rewritten,
including the two supersession bullets, which stay standing with their markers attached.**

This register is the audit trail of how the numbers got here, but it is also read as an instruction source: its
rows carry a `should_be` column and its bullets were written in the present indicative. Three of those statements
are now false and are withdrawn here, in place, with no substitute value offered:

1. **Rows 27–28's `should_be` leg "≈$871,000 (2,613,000 shares) of unaffiliated program purchases" (register row
   l.27) and the same decomposition at row l.28, restated as "the canonical figure" in the ROUND-1 bullet
   (l.68–69) — WITHDRAWN.** `2,613,000` occurs **0 times** in each of the original S-1, S-1/A
   No. 3, S-1/A No. 5 and the FY1997 10-K405 (`grep -c` over `sources/*.txt`); it is reachable only through the
   §P.2 d25 chain this project holds at UNKNOWN, "CANDIDATE DERIVATION, RECORDED BUT NOT ADOPTED"
   (`quantitative.csv` L99). Its only entry point into the dossier was `2,763,000 − Alberg's 150,000 = 2,613,000`
   (`stage_1.md` l.1066–1067).
2. **"the composition foots to $976,408 … the $24 difference is accounted for … not plugged" (l.71–73) —
   WITHDRAWN with the leg.** `2,613,000 ÷ 3 = $871,000` is arithmetically true and rests on an unfiled
   denominator; it differs from the retired `$871,024` back-solve by $24 and **not by evidence**, and the account's
   $19 term was itself computed from d25's non-adopted ≈$921,000.
3. **"§K … prints the composition at $976,408" (l.87–88) and "P09 … carr[ies] … the $976,408 composition"
   (l.89–90) — FALSE AS DESCRIPTIONS**, marked at R4b above; both canonical sites now withdraw the total.

**A wrong citation, separately retracted:** every "orig. l.4301–4302" attached to `2,613,000` in this file is
mis-cited. The filing at l.4300–4302 reads: "*Between December 6, 1995 and May 16, 1996, the registrant issued an
aggregate of **3,021,000** shares of Common Stock to **23 investors** for a consideration of approximately
**$.3333** per share, or an aggregate of **$1,007,000.***" That line supports the **filed** program figures —
3,021,000 / 23 / $.3333 / $1,007,000 — and is cited correctly in that service elsewhere in this register (rows at
l.15, l.26); it supports **no** `2,613,000`, and a citation is not repaired by the arithmetic that follows it.

**What this register's rows 27–28 still instruct correctly:** state the residual as **≈$976,000 (±$1,000)** rather
than `= $976,432`; keep the residual's identity **UNKNOWN**; and strike the option-cash / upper-bound clause — 1995
option exercises are filed at **$—** (orig. l.3560–3562). **The composition of the residual's fourth leg is
UNKNOWN**, and the only filed legs are `$5,408 + $150,000 − $50,000 = $105,408`.

**Line numbers in the items above are as read 2026-09-25, after the two AUDIT-7 markers were inserted; the two
bullets they point into began at l.68 and l.82 before this pass, so anchor on the bullet headings ("Rows 27–28
(D19/D15 family…)", "Rows 27–28 and 43 — status: propagated…") rather than on the numbers.**

**Canonical text:** `stage_1.md` §K "Reconciliation of the two totals" (l.610), §P.2 d8a (l.961) and §U.8 (l.1487);
`quantitative.csv` L35; `conflicts.csv` U.8; `context_appendices.md` §I "Capital raised inside Stage 1" and §J gap
row 12; `stage_1_claim_records.md` P09 (l.466). Line numbers are as read 2026-09-25; anchor on the row id.
Sweep commands re-run for this addendum are recorded at
`03_quality_control/audit7_repairs.md` (rows R4, R4b, S1–S3).
