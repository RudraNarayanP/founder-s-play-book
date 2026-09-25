# AMAZON.COM — STAGE 2 — AUDIT 3 (NUMBERS) — INDEPENDENT RECOMPUTATION

**Auditor role:** NUMBERS AUDITOR, independent of all prior passes and of every agent that wrote the
material under audit. **Read-only audit**: this file is the only artefact created; no register, no
narrative, no dossier, no source document was modified. **Zero web requests**: every check below runs
against bytes already on disk under `founders_playbook/01_companies/company_001_amazon/` (99 items in
`sources/`, five Stage-2 dossiers in `research/`). Working scripts were kept outside the repo
(`%TEMP%\numaudit\`). **Turn budget respected:** the run completed inside the 90-call ceiling; anything
not measured here is marked UNTRIED in §UNTRIED below.

**Scope audited:** `stage_2_part_1.md` (§A–H, 594 l), `stage_2_part_2.md` (§I–P incl. §P, §P.2a, §P.2,
939 l), `stage_2_part_3.md` (§Q–U, 1,735 l), `stage_2_claim_records.md` + `_part_2.md`, the nine
registers, and the filing text they cite (`sources/S-1A-No5…`, `S-1_original…`, `424B1…`,
`10-K_FY1997…`, `S-1A-No3…`).

**Method.** (i) Every expression printed in `quantitative.csv:derived_arithmetic` was re-evaluated from
first principles by an independent parser (`recomp3.py`), then each Stage-2 row was re-checked by hand.
(ii) Every arithmetic INPUT was located in the cited filing line and the printed line was read.
(iii) Denominators were tested for existence, filedness and coterminousness, not just for tidiness.
(iv) Registers were diffed against the narrative (§P ↔ `quantitative.csv`, §Q ↔ `timeline.csv`,
§U ↔ `conflicts.csv`, held Stage-3 rows). (v) The validator itself was poisoned and re-run (§7).

## Verdict table

| # | Check | Verdict | Count | Defect ids |
|---|---|---|---|---|
| 1 | Recompute every DERIVED row from the cited document lines | **FAIL** (arithmetic mostly sound; 6 rows print a wrong quotient or a wrong input) | 334 rows read; 104 with `derived_arithmetic`; 83 tagged DERIVED; 116 expressions re-evaluated | D-01/02, D-03, D-04, D-05, D-06, D-07, D-14 |
| 2 | Denominators filed and coterminous | **FAIL** | 1 denominator filed nowhere, 1 unverifiable, 1 non-coterminous pair, 1 365/366 basis split | D-01/02, D-11, D-12 |
| 3 | Precision laundering | **CONDITIONAL PASS** | 3 live rendering defects; 0 survivors of the retracted 5,112/32.5 pair; 11 checked figures clean | D-06, D-07, D-14 (§3.2) |
| 4 | Cross-foot the statements (FY1996, FY1995 comparatives, Q1-1997) | **PASS** | 34 identities recomputed, 34 tie; the 79/2,270 working-capital trap is NOT sprung anywhere | — |
| 5 | Register ↔ narrative agreement (§P / §Q / §U / held rows) | **FAIL** | §P 121 rows ↔ 99 register rows: 3 disagreements; §Q 68 rows: 7 with no twin (+22 granularity); §U 70 ↔ 70 EXACT; held rows 0/10 leaked | D-03, D-02, D-11, D-13 |
| 6 | Basis labels (pooling-restated / pro forma / split basis) | **CONDITIONAL PASS** | Stage 2 uses 147,758 as-filed and the 6× split basis correctly; 2 label defects; 1 Stage-3 exposure routed | D-08, D-09, R-01 |
| 7 | Prove the validator | **PASS** — 2 of 2 planted defects caught (1 by the arithmetic/unfiled-input run, 1 only after column-integrity invariants were added; width-only validation provably insufficient) | poison run on a copy outside the repo, 2 defects | — |
| — | Ghost sweep: no survivor of the fabricated FY1996 set; no return of the retracted Stage-1 legs or the false cash bridge | **PASS with 1 stale conflict row + 1 routed caution** | 15 ghost strings × 26 files; live-value occurrences in the nine registers = **0** | D-10, R-02 |

**Overall: CONDITIONAL FAIL** — see §Overall verdict.

---

## 1. Recomputation of every DERIVED row

`quantitative.csv` = 334 rows, 12 columns, every line exactly 12 fields (so a naive field-count
validator would see nothing wrong — see §7). `derived_arithmetic` is populated on **104** rows, of
which 83 carry a DERIVED label somewhere in `evidence_class` (66 `DERIVED`, 6 `FACT + DERIVED`,
6 `ESTIMATE/DERIVED`, 4 `FACT (audited) + DERIVED`, 1 `FACT (as filed unaudited) + DERIVED`) and
**21 populate the arithmetic while labelling the row FACT/ESTIMATE** (e.g. L130 net sales, L143
post-offering share count, L148 share caption, L187 splits). That asymmetry is not itself a defect —
the cell is the audit trail — but it means "rows with arithmetic" (104) and "DERIVED rows" (83) are
different populations and the brief's "~334 rows with `derived_arithmetic` on every DERIVED one" holds:
**every** DERIVED-labelled row does carry its arithmetic (0 exceptions found).

Stage split of the 104: stage1 26, stage2 49, stage2-consequence 3, stage3 4, "3" 22.

### 1.1 What the machine said

`python recomp3.py` → 116 `EXPR = RESULT` pairs extracted and re-evaluated. Every pair was re-checked
by hand; the parser's own false positives are listed so this report does not launder them into findings.

**Ties (exact or correct to the printed precision) — Stage 2, all verified against the printed filing line:**

| Row | Re-computed | Filed input located |
|---|---|---|
| L115 | 569,396 × 14.05 = 8,000,013.80; 8,000,014 ÷ 569,396 = 14.0500007 | A5 l.3686 prints 569,396 |
| L118 | 40.00 ÷ 14.05 = 2.8470 | A5 l.2849-2850 prints $40.00, 2,500 shares |
| L123 | 3,459 ÷ 15,746 = 0.219674 → 22.0% | A5 l.3731-3734; 10-K405 l.1403 prints 22.0% |
| L124 | 28,813 ÷ 147,758 = 0.194995 → 19.5% | K97 l.1177/1180 |
| L125 | 3,521 ÷ 16,005 = 0.219994 → 22.0% | A5 l.3731/3734; ratio table l.1702 |
| L126 | 9,038 − 8,959 = 79 | A5 l.3666/3680, capitalization l.397 |
| L127 | 7,140 − 4,870 = 2,270 | A5 l.3666/3680 (1996 column) |
| L132 | 16,005 − 15,746 = 259 | A5 l.3731 |
| L133 | 875+2,230+4,173+8,468 = 15,746 | A5 l.379 (quarterly columns) |
| L134 | (16,005−8,468)/8,468 = 0.89004 | A5 l.379 |
| L139 | 3,000,000 × 18.00 = 54,000,000 | 424B1 l.125 prints $54,000,000 |
| L141 | 50,220 − 850 = 49,370; 49,449 − 79 = 49,370 | 424B1 l.21/125 ($50,220,000, $850,000), l.277 (49,449 / 79) |
| L142 | 54,000 − 3,780 − 1,117 = 49,103; 49,370 − 49,103 = 267 | K97 l.1997 (49,103), l.1935 (1,117) |
| L143 | 3,780 + 850 = 4,630 = 54,000 − 49,370 | 424B1 l.20/21/125 |
| L144 | 3,000,000 ÷ 23,798,782 = 0.12606 | 424B1 l.1205 prints 12.6 |
| L145 | 20,798,782 + 3,000,000 = 23,798,782 | 424B1 l.1204/1206 |
| L146 | 23,798,782 × 18.00 = 428,378,076 | derived on the filed count |
| L148 | 14,555,244+840,528+504,457 = 15,900,229; orig. variant = 15,900,237 | A5 l.3693-3694 |
| L149 | 574,396 × 6 = 3,446,376; +17,352,406 = 20,798,782 | A5 l.3687/3694/3696 |
| L152 | 256 ÷ 11 = 23.27; (256−11)/11 = 22.273 | A5 l.796 |
| L154 | (5,979)+202 = (5,777); 5,777 ÷ 22,655 = 0.25499 → (0.25) | A5 l.3744-3752 |
| L155 | 3,459 − 9,438 = (5,979); 9,438 ÷ 15,746 = 0.59939 | A5 l.3742/3741 |
| L156 | 6,090 ÷ 15,746 = 0.38676; 6,090 ÷ 3,459 = 1.7606 | A5 l.3736 |
| L157 | 2,313 ÷ 15,746 = 0.14689 | A5 l.3737 |
| L158 | 1,035 ÷ 15,746 = 0.06573 | A5 l.3739 |
| L160 | 4,870 + 3,401 = 8,271 | A5 l.3680/3703/3670 |
| L161 | (248)+(5,777) = (6,025); 6+159+9,873−612−6,025 = 3,401 | A5 l.3689-3703 |
| L162 | 9,063 ÷ 2,763 = 3.280 | A5 l.3701/3703 |
| L163 | 231+7,970 = 8,201; 996−1,735−1,214+8,201 = 6,248 | A5 l.3933/3935/3940/3947 |
| L164 | 1,214 ÷ 52 = 23.346 | A5 l.3925 |
| L166 | 2,852 ÷ 12,287 × 365 = 84.72; 2,852 ÷ (6,577×4) × 365 = **39.57** | A5 l.3675, l.1378/1667 (Q4-96 cost of sales 6,577) |
| L167 | (17+571) ÷ 2 = 294; 12,287 ÷ 294 = 41.79 | A5 l.3663, l.3732 |
| L169 | 1,540 ÷ 122 = 12.62; 4,323 ÷ 122 = 35.43 — **arithmetic right, input wrong, see 2.3** | A5 l.4396/4402 |
| L171 | 1,735 ÷ 366 = 4.7404, 79 ÷ 4.7404 = 16.67; 2,949 ÷ 366 = 8.0574, 79 ÷ 8.0574 = 9.80 | A5 l.3923/3925 |
| L172 | 3,021,000 ÷ 3 = 1,007,000 exactly | S-1o l.4300-4302 |
| L173 | 2,500,000 ÷ 1,100,000 = 2.2727 | press release relay, see 2.4 |
| L175 | 400,000 ÷ 2,500,000 = 0.16; 2,500,000−400,000 = 2,100,000; ÷ = 6.25 | A5/S-1o |
| L176 | 511 + 15,746 = 16,257 vs "more than $16 million" | S-1o l.315 |
| L178/179 | 50,000 ÷ 2,200 = 22.7; 80,000 ÷ 2,200 = 36.36 | S-1o l.316 / A5 l.337 |
| L181 | 2,448,000 ÷ 15,746 = 155.47; ÷ 147,758 = 16.57 | denominator has no local copy — see 2.4 |
| L184 | 17 ÷ 5 = 3.4 | WIRED relay |
| L185 | 726,000 × 3 = 2,178,000 ÷ 3,000,000 = 72.6% | 424B1 l.3324 |
| L186 | 18.00 ÷ 16.00 = 1.125 | A5 l.225 / 424B1 cover |
| L187 | 1 × 4 × 1.5 = 6 | A5 l.4172, l.4440-4443 |
| L188 | 18.00 ÷ 14.05 = 1.2811; 14.05 ÷ 6 = 2.3417; 18.00 ÷ 2.3417 = 7.6867 → 7.69 | filed pair |
| L190 | 15,746 ÷ 81 = 194.4; 15,746 ÷ 84.5 = 186.34 | filed counts 11/151/158 |

**Ties — Stage 1 and stage-2-consequence rows re-run as inputs to Stage 2 numbers:** L5 0.005882 ✓;
L6 0.00098 ✓ (but see 6.3 on the restatement basis); L9 26+31+30+31+30+31 = 179 ✓; L22 582,528 ×
0.1717 = 100,020.0576 ✓; L24 847,716 × 0.1717 = 145,552.8372 ✓; L28 150,000 × 0.3333 = 49,995 ✓;
L30 (0.3333−0.1717)/0.1717 = 0.941176 ✓ and (0.33333−0.1717)/0.1717 = 0.941351 (cell prints 0.94137,
**off by 0.00002** — immaterial, listed for completeness); L32 1,430,244 × 0.1717 = 245,572.9 ✓;
L34 100,020.0576+145,552.8372+49,995 = 295,567.8948 ✓; L35 1,272,000−295,568 = 976,432 ✓;
L42 102 ÷ 511 = 19.96% ✓; L44 200 ÷ 511 = 39.14% ✓; L47 200+171+35 = 406 ✓; L52 304 ÷ 511 = 0.5949 ✓;
L53 0.1996−0.3914 = (0.1918) ✓; L55 52+303 = 355, 355−107 = 248 ✓; L58 198 ÷ 511 = 38.75% ✓;
L61 232+52 = 284 ✓; L66 −232−52+1,228 = 944, 52+944 = 996 ✓ (**the retracted bridge form does not
survive here — see §8.2**); L68 81−24 = 57 ✓; L69 28+52 = 80 ✓; L71 17 ÷ 511 = 3.33% ✓;
L76 511,000 ÷ 11 = 46,454.5 ✓; L83 511,000 ÷ 318,000,000 = 0.1607% ✓; L85 996 ÷ 284 = 3.507 ✓;
L98 3,021,000 × 0.3333 = 1,006,899.30 ✓; L100 1,007,000 ÷ 23 = 43,782.6 ✓; L108 2,500,000−400,000 =
2,100,000 ✓; L112 5.5 × 4.345 = 23.8975, 511,000 ÷ 23.8975 = 21,382.99, 184 ÷ 7 = 26.2857,
511,000 ÷ 26.2857 = 19,440.22 ✓.

**Stage-3-tagged DERIVED rows (read, not adopted, listed because they sit in the same register):**
L206 2,100/614 = 3.4205 ✓; L207 609,996/147,787 = 4.1275 ✓ (**denominator printed as 147,787 while the
10-K prints 147,758 and every Stage-2 row uses 147,758** — a transposed digit inside the shared
register); L211 31,035−78,674 = −47,639 ✓; L221 8.5m/270k = 31.5 ✓; L241-L334 all re-run ✓ except
L250 113,273 ÷ (476,155 ÷ 365) = 86.8 ✓, L251 476,155 ÷ ((8,971+29,501)/2 = 19,236) = 24.75 ✓,
L254 38,005 ÷ 159,267 = 0.23862 ✓, L268 217,241 ÷ 325,987 = 0.66641 ✓, L273 9,885,000 × 2 × 3 =
59,310,000 − 58,770,000 = 540,000 ✓ (**split-factor basis: see 6.4**), L278 81,840 ÷ 201,512 = 0.4061 ✓,
L279 81,840 ÷ 64,333 = 1.2721 ✓, L291 14,400 ÷ 153,700 = 9.368% ✓, L298 60,200 ÷ 609,996 = 9.869% ✓,
L312 3,800,000+690,000 = 4,490,000 ✓, L321 83,290 ÷ 366,977 = 0.22696 ✓, L328 188.4 ÷ 1,639.839 =
0.11489 ✓, L329 188.4 ÷ 140.9 = 1.3372 ✓, L332 31,739,000 ÷ 7,600 = 4,176.2 ✓, L334 188.4 ÷ 16.9 =
11.15 ✓, L252 609,996 ÷ 2,100 = 290.5 ✓, L253 147,758 ÷ 614 = 240.6 ✓, L255/L256 ✓.

### 1.2 The six arithmetic defects

1. **L169 (register) + §P150 (`stage_2_part_2.md`:607) — the rent denominator is not the filed number.**
   Filed: A5 l.4383 "Rental expense under operating lease agreements for 1994, 1995, and 1996 was
   $2,000, $12,000, and **$257,000**" (identical at S-1o l.4047, 424B1 l.4257, and K97 l.2392:
   "1997, 1996 and 1995 was $2 million, **$257,000** and $12,000"). Nothing in the corpus prints 122
   as rent. Correct multipliers: 1,540 ÷ 257 = **5.99×**; 4,323 ÷ 257 = **16.8×**.
2. **§P150 headline "6.4×"** is reproducible from no pair of numbers in the row (1,540/122 = 12.6;
   4,323/122 = 35.4; 1,540/257 = 6.0; 4,323/257 = 16.8).
3. **L121 / §P.2 s2 print `15,746 ÷ 511 = 30.813`**; the exact quotient is **30.81409** (30.814 to 3 dp).
   The companion `(15,746 − 511) ÷ 511 = 29.8141` ✓ is right, so the two renderings in the same cell
   disagree with each other by 0.001 in the third decimal.
4. **§P76 prints the growth pair inverted** — see §5.1; the "≈3,081% increase / ≈29.8× the prior year"
   form is the exact confusion §P.2 s2 retracts in the paragraph below it.
5. **§P76's "2,980.6"** is not the quotient of the filed pair: 15,235 ÷ 511 = 29.81409 → +2,981.4%
   (the 10-K405 itself prints **2,981%** at l.1380 ✓ verified).
6. **L166 prints 39.5 for a computation of 39.5690** (2,852 ÷ 26,308 × 365). Rounding to one decimal is
   **39.6**; the band's upper term (84.7 from 84.7221) rounds correctly. Understating the low end of a
   days-payable band by a rounding step is immaterial to the argument, material to the register's claim
   that every derived figure prints its exact arithmetic.

**Verdict — check 1: FAIL.** The register's *identities* all hold (every cross-foot below ties); what
fails is the printed "exact quotient" tail and one input. Five rows print an "exact" decimal that is not
the exact quotient of the two numbers they name — L121 (30.813 for 30.8141), L124 with §P80a
(0.194995 / "exact 19.4995" for 28,813 ÷ 147,758 = **0.1950013** / 19.50013%), L134 (0.89004 for
0.8900567), L154 (0.2548 for 5,777 ÷ 22,655 = **0.2549989**), L115 (14.0500007 for 14.0500004) — and one
row (L169/§P150) carries an input (122) that no filing prints. Stage-1 rows re-run clean except
L30's 0.94137 for 0.941351 (immaterial, listed for completeness).

---

## 2. Denominators: filed? coterminous?

### 2.1 Test applied
Every ratio printed in a Stage-2 register row or §P row was resolved to (numerator, denominator, the
document line where each is printed, and the period each covers). A denominator that appears in no
document on disk makes the ratio UNKNOWN regardless of how tidy the quotient is.

### 2.2 Ratios whose denominators ARE filed and ARE coterminous (PASS)
L123, L124 (147,758 is the FY1997 audited year, and the row is labelled POST-BOUNDARY), L125, L133,
L134, L141, L143, L144, L146, L154, L155, L156, L157, L158, L162, L163, L164, L167, L185, L186, L188,
L190, and the §P.2 s1-s35 block that supports them. All inputs located at the cited lines
(A5 l.3663-3703, l.3731-3752, l.379, l.3905-3947, l.1378, l.1667, l.397; 424B1 l.20-21, l.125,
l.277, l.1204-1206, l.3324; K97 l.1177-1197, l.1380, l.1403, l.1935, l.1997).

### 2.3 Denominator defects (FAIL)
1. **Rent — L169, §P150 (`stage_2_part_2.md`:607).** 122 is filed nowhere; the filed FY1996 rental
   expense is **$257,000** (four documents, §1.2.1). Both multipliers change: 1,540 ÷ 257 = **6.0×**,
   4,323 ÷ 257 = **16.8×**. The row also heads itself with a third number, **6.4×**, which is
   reproducible from no pair in the row.
2. **Days payable, low term — L166, §P120.** The denominator `6,577 × 4` is an **annualised Q4-1996 run
   rate**, and Q4-1996 alone carries 6,577 ÷ 12,287 = 53.5% of the year's cost of sales. The row labels
   the result a BAND and says so; the register keeps the label. Accepted as disclosed, but the term
   "≈39.5" must be **39.6** and it must never be quoted without the run-rate gloss.
3. **§P140 / L162 — `9,063 ÷ 2,763`:** both filed (A5 l.3701, l.3703) and coterminous (both at
   1997-03-31) ✓ PASS — recorded here because the brief asked for the pairing to be tested, not assumed.
4. **L166's 365 / L171's 366.** FY1996 is a leap year, and the days-payable and runway rows use **365**
   while the runway row uses **366**. 365 is correct for a generic year but the two rows in the same
   register pair the same fiscal year with different denominators: on 366 the days-payable band becomes
   39.7/85.0 and the runway is unchanged. Flagged as a basis inconsistency, not as an arithmetic error.

### 2.4 Denominators that are NOT filed anywhere → the ratio is UNKNOWN
1. **L181 / §P164-§P165 — the Barnes & Noble pair.** `2,448,000 ÷ 15,746 = 155.5×` and
   `2,448,000 ÷ 147,758 = 16.6×`. The numerator comes from the B&N Form 10-K (acc.
   0000889812-97-001072), which §P164 itself declares **`(NO LOCAL COPY … every figure in this row is
   this project's transcription of a temporary read recorded at S2C-20, not a string a reader can open)`**.
   Grep of the five Amazon filings returns **0 hits** for `2,448` and `431 superstores`. Under the rule
   this brief sets, both multipliers are UNKNOWN, not FACT. The register row L181 classes the same
   figures **"FACT (audited counterparty)"** with no local-copy caveat — a direct class disagreement
   between register and narrative (→ §5.2).
   *Coterminousness, separately:* B&N's revenue is for the **53 weeks ended 1997-02-01** against
   Amazon's **52 weeks ended 1996-12-31** — a 53/52 and a period-mismatch pairing (the same shape as
   the S2C-52 flag), and the second ratio pairs a 1997-02-01-terminating B&N year with Amazon's
   **post-boundary** FY1997. Neither is disclosed in the register row.
2. **§P147's third leg, `$(0.31)`** — filed ✓ but as **"Pro forma basic and diluted loss per share"**
   (K97 l.1194, with its own pro-forma share line at l.1197: 21,651 / 18,544 / 14,394 / 13,191).
   5,777 ÷ 18,544 = 0.31153 → (0.31) ✓ arithmetic ties, so the figure is real — but it is *not* the
   10-K's reported FY1996 loss per share, and the §P row's own header calls the three entries
   "three bases across three documents" without naming pro-forma-ness. → §6.2.
3. **§P150's "6.4×"** — no denominator at all (see 2.3.1).
4. **The $345,525 founder-related block and 2,012,772 shares** — traced to S-1o Item 5 in Stage 1 and
   unchanged here; the retracted `2,613,000` denominator has **not** returned as a live value (§8.2).

### 2.5 The "1.4×" test (S2C-17)
Searched all three Stage-2 volumes for a live `1.4` multiplier claim: the only occurrences are the
conflict blocks that *refuse* it (U.17 family / §P.2 notes) — see §5.4. No register row in
`quantitative.csv` carries a 1.4× value. **PASS (nothing survived).**

**Verdict — check 2: FAIL** (4 defects: the unfiled rent denominator, the unfiled-and-mismatched B&N
pair presented as FACT in the register, §P150's unreproducible 6.4×, and the 365/366 basis split).

---

## 3. Precision laundering

### 3.1 The retracted false-precision pair stays dead
`5,112` / `32.5` (§P111's predecessors) were a reconstruction of a figure the Note prints as
**"$5.1 million"** (A5 l.4042, S-1o l.3722) and **"approximately … 33%"** (A5 l.1510, S-1o l.1438).
Grep of the four Stage-2-bearing files plus the nine registers: `5,112` occurs **only** inside the
retraction sentence at `stage_2_part_2.md`:566 and `stage_2_part_3.md`:645; `32.5` likewise. §P111 now
prints the filed forms and states the reason ("`5.1 ÷ 15.746 = 32.4%`, which is why the company's own
rounding is 'approximately 33%'") ✓ correct: 5.1/15.746 = 0.32389 → 32.4%.

### 3.2 Live defects
1. **`quantitative.csv` L169 "4323" vs the note's own precision.** No laundering — the note prints
   thousands ✓. The live precision problem is the **122** (§2.3.1), which is a *false* number dressed as
   a filed one, a stronger defect than laundering.
2. **L166 "approximately 39.5 to 84.7"** — printed to one decimal where the underlying computation is a
   run-rate annualisation (39.569). One-decimal precision on a run-rate band is laundering by rendering:
   **≈40 / ≈85** is the honest form, or keep one decimal and fix the rounding.
3. **§P122 "122 — carried as received and re-checked against the note in this pass; see §S if the note's
   own caption wording differs."** A three-significant-figure value carried on a hedge instead of a
   lookup. The lookup takes one grep (A5 l.4383): the note's caption does not merely "differ", it prints
   $257,000.
4. **L115's "14.0500007"** and **L124's "0.194995"** (§1.2 item list) print 6-7 significant digits of a
   quotient that is not, at the last digit, the quotient. False precision in the audit-trail column is
   still false precision.

### 3.3 Checked and CLEAN (no defect)
`22.0` (the company prints 22.0% at K97 l.1403 for FY1996 ✓); `19.5` (company prints 19.5% ✓); `38.7`,
`14.7`, `6.6`, `59.9` (all derived from filed thousands, and the ratio table A5 l.1703-1705 prints the
*quarterly* series — the annual 38.7/14.7/6.6 are ours, labelled DERIVED ✓; the citation to "ratio table
l.1703" for an ANNUAL percentage mis-points the reader at the quarterly row: noted, not a number
defect); `(0.25)` on `22,655` ✓; `≈180,000 accounts`, `> $16 million`, `≈340,000`, `> $32 million` ✓
filed verbatim (S-1o l.315-316; A5 l.336-337); `≈50,000` / `80,000` visits ✓ filed; `59%` / `58%`
Ingram ✓ filed (A5 l.948; K97); `2,981%` ✓ printed by the company (K97 l.1380);
`12.6%` / `87.4%` dilution ✓ printed by the company (424B1 l.1204-1205); `49,449` / `79` ✓ printed
(424B1 l.277).

**Verdict — check 3: CONDITIONAL PASS** — 3 live rendering defects (items 3.2.2, 3.2.3, 3.2.4); the
retracted pair stayed dead; 11 checked figures clean.

---

## 4. Cross-footing the statements (from the printed filing, not from the register)

Ground truth read directly from `sources/S-1A-No5…txt` at the lines cited: balance sheet l.3650-3708,
statements of operations l.3721-3754, cash flows l.3900-3948, selected data l.368-386, quarterly
percentage table l.1690-1715, capitalization l.388-400, lease note l.4377-4404.

### 4.1 FY1996 — 14 identities, all tie
| Identity | Filed terms | Result |
|---|---|---|
| Gross profit | 15,746 − 12,287 | **3,459** = filed l.3734 ✓ (the brief's exact test) |
| Operating expense foot | 6,090 + 2,313 + 1,035 | **9,438** = filed total l.3742 ✓ |
| Loss from operations | 3,459 − 9,438 | **(5,979)** ✓ l.3744 |
| Net loss | (5,979) + 202 | **(5,777)** ✓ l.3747 |
| LPS bridge | 5,777 ÷ 22,655 = 0.254999 | filed **(0.25)** ✓ l.3749/3752 |
| Current assets | 6,248 + 571 + 321 | **7,140** ✓ l.3666 |
| Current liabilities | 2,852 + 598 + 500 + 920 | **4,870** ✓ l.3680 |
| Balance-sheet identity | 4,870 + 3,401 | **8,271** = total assets ✓ l.3670/3707 |
| Assets side | 7,140 + 985 + 146 | **8,271** ✓ |
| Equity roll | 6 + 159 + 9,873 − 612 − 6,025 | **3,401** ✓ l.3689-3703 |
| Deficit roll | (248) + (5,777) | **(6,025)** ✓ |
| Cash bridge | 996 − 1,735 − 1,214 + 8,201 | **6,248** ✓ l.3947 |
| Financing foot | 231 + 7,970 + (−−) | **8,201** ✓ l.3940 |
| Quarterly sum | 875 + 2,230 + 4,173 + 8,468 | **15,746** ✓ (A5 l.379) |
| Quarterly loss sum | (331) + (767) + (2,380) + (2,299) | **(5,777)** ✓ (l.381) |
| Lease commitments | 1,540+1,534+1,133+107+9 | **4,323** ✓ l.4402 |

### 4.2 FY1995 comparatives — tie
511 − 409 = 102 ✓; 200 + 171 + 35 = 406 ✓; 102 − 406 = (304) ✓; (304) + 1 = (303) ✓;
(303) ÷ 18,933 = 0.0160 → filed **(0.02)** ✓; 996 + 17 + 14 = 1,027 ✓; 99 + 8 = 107 ✓;
1,027 + 57 = 1,084 ✓; 1,027 − 107 = **920** working capital ✓ (§P82 prints 920 ✓ — derived, not filed,
and correctly labelled); 996 − 232 − 52 + 1,228 = 996 ✓; 5 + 19 = 24 accumulated depreciation ✓.
1994 stub: 38 + 14 = 52 ✓; net loss (52) ✓; (52) ÷ 17,730 = 0.0029 → filed **(0.00)** ✓.

### 4.3 Q1-1997 unaudited column — tie
16,005 − 12,484 = 3,521 ✓ (3,521 ÷ 16,005 = 21.999% → the company's own quarterly table prints **22.0**
at l.1702 ✓); 3,906 + 1,575 + 1,142 = **6,623** ✓ l.3742; 3,521 − 6,623 = **(3,102)** ✓;
(3,102) + 64 = **(3,038)** ✓ l.3747; 3,038 ÷ 23,018 = 0.13198 → filed **(0.13)** ✓;
balance sheet 7,162 + 939 + 937 = 9,038 ✓; 5,650 + 1,254 + 2,055 = 8,959 ✓; 9,038 − 8,959 = **79** ✓;
9,038 + 2,491 + 193 = 11,722 ✓; 8,959 + 2,763 = 11,722 ✓; 6,025 + 3,038 = **9,063** ✓;
cash 6,248 + 914 = 7,162 ✓ (l.3942/3947).

### 4.4 The working-capital trap — NOT sprung
The filing prints **79 only at 1997-03-31** (l.397 capitalization; 424B1 l.277). `2,270` is the derived
1996-12-31 figure (7,140 − 4,870). Every occurrence of 79 in the registers and in all three volumes was
tested for a 1996-12-31 or "year-end" pairing: **zero** live mis-usages. L126 carries
`date = 1997-03-31, value = 79, "the boundary state"` ✓; L127 carries `date = 1996-12-31, value = 2,270,
"the filing prints no 1996 line"` ✓; §P81/§P81a the same ✓. The retracted form
"`$79k` as the 1996 year-end working capital" survives only inside the retraction list at
`stage_2_part_3.md`:179 and :644 ✓.

**Verdict — check 4: PASS. 34/34 identities tie; no year-end/boundary confusion survives.**

---

## 5. Register ↔ narrative agreement

### 5.1 §P ↔ `quantitative.csv`
§P (`stage_2_part_2.md`:505-640) parses to **121 metric rows** (P71…P183, incl. the a/b suffixed rows).
99 register rows carry `stage2`/`stage2-consequence`. Every numeric token in every Stage-2 register
`value` cell was matched against the §P token set: **5 rows surfaced, and all 5 are unit renderings, not
disagreements** — L101 prints net sales as `15746000` USD where §P74 prints `15,746` thousands; L181's
`51200` is §P164's `$51.2m`; L184's `17000000` is §P163's `$17m`; L98/L100 are the §P.2-level placement
cross-checks (`$1,006,899.30`, `$43,783`) which live in the arithmetic block rather than in a §P row.
Spot-agreement confirmed on the money rows: P77↔L122 (12,287/3,459), P105↔L153 (571), P106↔L154
((5,777)/(0.25)/22,655), P107↔L155, P108-P110↔L156-158, P120↔L166, P121↔L160, P121a↔L161, P81↔L126,
P81a↔L127, P98↔L144, P99↔L146, P144↔L149, P145↔(no register twin, see below), P159↔L187, P166↔L171.

**Three real disagreements:**
1. **§P76 vs L121 — the growth pair is inverted in the narrative.** L121: `30.8x the prior year and
   +2981%` ✓ correct. §P76: `2,980.6 → rendered ≈3,081% increase / ≈29.8× the prior year`. 3,081% is the
   *multiple×100*, not an increase; 29.8 is the *increase ratio*, not a multiple of the prior year; and
   2,980.6 is not the quotient of the filed pair (+2,981.4%). §P.2 s2, nine lines below, states the
   correct rule and retracts exactly this form ("the received '≈3,081%' is the *multiple* wearing the
   *percentage* label … and is retracted") — so §P76 disagrees with its own arithmetic block and with
   its register twin.
2. **§P150 vs L169 — three multipliers for two ratios.** §P150's headline says 1,540-in-1997 is
   "**6.4×** the $122k of rent actually paid"; its own parenthetical computes 12.6 and 35.4; L169's
   `derived_arithmetic` carries 12.6 and 35.4 and no 6.4. All three are wrong once the filed rent
   (257) replaces 122: 6.0 and 16.8.
3. **§P164 vs L181 — the class label disagrees across layers.** §P164 states its own row is
   "unverifiable at the citation … not a string a reader can open"; L181 classes the same figures
   "FACT (audited counterparty)" with no such caveat, and §P165 turns them into two multipliers printed
   as `155.5×` / `16.6×`. A register row may not outrank its own narrative's disclosure.

Coverage gap noted, not a defect: §P145 (the Series A automatic-conversion trigger, ≥$20.00/share AND
aggregate ≥$7,500,000) has **no `quantitative.csv` twin**, although both terms are filed
(S-1 original l.5307 and l.5312). It is the only §P money row without a register partner that this
audit found.

### 5.2 §Q ↔ `timeline.csv`
§Q (`stage_2_part_3.md`:18-111) carries **68 event rows**; `timeline.csv` carries 220 rows
(stage2 59, stage2-consequence 8, stage1 49, stage3 43, "3" 61). Date-twin test on the §Q date cell:
**39 of 68 have an ISO date that is present in `timeline.csv`; 29 do not resolve**, and the 29 split:
- **22 rows are month- or quarter-level** (`1996-Q1`, `**1996-09**`, `1997-02`, `1996-06`) and
  `timeline.csv` holds no month-level row for the same bucket. This is a *register-granularity* gap, not
  a value conflict — the §Q row is the more precise statement of an event the register records at
  quarter or year level, or not at all.
- **7 rows carry a real ISO date with no `timeline.csv` twin at all**: 1996-02-01 (Coast Wide sublease
  commencement), 1996-08-01 (Trident commencement), 1996-11-01 (Building U scheduled commencement),
  1997-01-01→01-31 (B&N letter month), 1997-01-09 / 1997-02-27 (Trident amendments 2 and 3),
  1997-02-28 (17,008,158 share count), 1997-03-01 (Building U/mezzanine possession).
  Confirmed below by direct search of `timeline.csv`.

### 5.3 §U ↔ `conflicts.csv` — EXACT
`conflicts.csv` = 152 rows: stage 1 → U.1-U.43 (43), **stage 2 → U.44-U.113 (70, no gaps, no
duplicates)**, stage 3 → U.114-U.152 (39, provisional keys). `stage_2_part_3.md` carries exactly
**70 `**U.nn` blocks, 44 through 113, none missing, none duplicated** (U.44-U.113; incidental in-text
cross-references to U.60/U.107/U.112/U.113 are references, not blocks). The Stage-2 claim of
"70 blocks ↔ 70 rows" is **verified 1:1**.

### 5.4 Stage-3 held rows
The 10 held rows in `03_quality_control/stage3_register_merge_held_rows.md` (all `ST3_C_*` → `channels
.csv`, 12 columns against an 11-column register) were each matched by their longest distinctive
fragments against all nine registers: **0 of 10 leaked into any register** ✓. The held rows' own numbers
(4,800+ enrolment 1996; >140,000 1998-09; ~200,000; advertising $3.4m/$21.2m/$60.2m) appear in no
Stage-2 row, and no Stage-2 value was rewritten by the merge: the Stage-2 rows re-checked against the
filings in §1.1/§4 all still print the filed term.
**One register-internal collision the merge did create** is reported at §6.3 (147,758 vs 147,787).

**Verdict — check 5: FAIL** — 3 §P↔register disagreements (one of them the retracted 3,081% form back
in print), 7 §Q rows with no timeline twin (22 more at granularity level), §U and held-rows clean.

---

## 6. Basis labels: restated vs as-filed vs pro forma

### 6.1 The pooling test, run on the documents
`10-K_FY1997` l.1177 / l.1380 / l.1861 print FY1997 net sales as **147,758** (as filed).
`10-K_FY1998` l.1222 / l.1309 / l.2016 print the same year as **147,787**, under the footnote at
l.1269: *"(1) Reflects restatement for pooling of interests."* The two prints of FY1997 growth differ
with it — 838% in the FY1997 10-K (l.1380) against 839% in the FY1998 10-K (l.1309).
**Every Stage-2 row and §P row uses 147,758 and never 147,787** (L124, L181, §P80a, §P165) ✓ so Stage 2
itself never presents the pooling-restated figure as as-filed. Gross margin 19.5% is printed identically
in both documents (K97 l.1403, K98 l.1340) ✓ basis-independent.

**But the merge has put both bases into one register with no label distinguishing them:**
`quantitative.csv` L124/L181 = 147,758 (as filed) and L207 = 147,787 (pooling-restated, per K98 l.1222),
L207's `source` column reading only `DERIVED` @ 1999-03-05. That is not a Stage-2 arithmetic error, it is
a Stage-2 register-integrity exposure created by the Stage-3 merge → defect D-08.

### 6.2 Pro-forma printed as a per-share "basis"
§P147 lists FY1996 loss per share "three bases across three documents": $(0.26) → $(0.25) → **$(0.31)**.
The first two are the as-reported lines (S-1o l.358; A5 l.382/3749 ✓ both located). The third is
**K97 l.1194, captioned "Pro forma basic and diluted loss per share"**, with its own pro-forma share
line at l.1197 (21,651 / 18,544 / 14,394 / 13,191). 5,777 ÷ 18,544 = 0.31153 → (0.31) ✓ the arithmetic
ties, so the number is real — but a preferred-converted pro-forma figure is a different kind of animal
from an as-filed LPS, and the row's own header word ("bases") does not carry the label. → defect D-09.

### 6.3 The 12× split factor — Stage 2 is CLEAN
A5 l.4172 ("On November 23, 1996, the Company effected a four-for-one common stock split") and
l.4440-4443 (three-for-two, 1997-04-18) are the only splits inside the Stage-2 window, so the operative
cumulative factor for this stage is **6×**, and Stage 2 uses exactly that: L187 `1 × 4 × 1.5 = 6`,
L149 `574,396 × 6 = 3,446,376`, L188 `14.05 ÷ 6 = 2.3417`, §P72's unit cell "shares (1997 split-restated
basis)", §P144, §P159, §U.59. Every Stage-2 per-share and option figure was re-tested for a silently
inherited 12× basis: **none**. Searching all three volumes for a 12-for-1 or cumulative-12 claim returns
zero live hits. The 1994 "restated basis" row L6 (`1,700,000 × 6 = 10,200,000`, A5 l.3775/3788 print
10,200,000 shares ✓) is on the same 6× basis ✓.
**Exposure is in Stage 3, not Stage 2:** `quantitative.csv` L273 restates the founder block as
`9,885,000 × 2 × 3 = 59,310,000`, a chain that carries two later splits and no 1999-09-01 2-for-1 term;
if the cumulative factor is 12× rather than 6× post-1999, that row (and the 13G comparison under it) is
short a factor of 2. Out of scope here, routed to the Stage-3 gate → routed item R-01.

**Verdict — check 6: CONDITIONAL PASS** — Stage-2 figures are on the correct 6× and as-filed bases;
two label defects (6.1 unlabelled second basis in the shared register; 6.2 pro-forma presented as a
per-share basis) and one routed Stage-3 exposure.

---

## 7. Proving the validator (the parser that missed a shifted row)

A copy of `quantitative.csv` was made outside the repo and two known defects were planted into it.

**Defect A — unquoted comma shifting a field, field count held at 12** (the historical failure):
row L158 rewritten so `value` carries a bare comma and the trailing `notes` field is dropped.
Result: `len(fields) = 12`, identical to every other row, while `unit` goes empty and every column from
6 onward shifts one place right — `evidence_class` now holds `1997-05-14`, `confidence` holds
`FACT + DERIVED`, `derived_arithmetic` holds `High`, and the real arithmetic sits unread in `notes`.
**Defect B — back-solved denominator:** L166's `2852 / (6577 x 4) x 365 = 39.5` rewritten as
`2852 / (6590.3 x 4) x 365 = 39.5`, i.e. the denominator solved backwards out of the wanted answer
(2,852 ÷ 26,361.2 × 365 = 39.500 exactly). 6,590.3 is printed nowhere.

Run 1 (width check + arithmetic recomputation, the shape of a "clean" validator):
`field-widths=[12]` on both files → the width check calls the poisoned file **CLEAN**; the recomputation
engine flags L166 (new catch) and **misses L158 entirely** — the historical bug reproduced.

Run 2 (three column-integrity invariants added: `evidence_class` ∈ a controlled vocabulary;
`source_date` matches a date grammar; every DERIVED-labelled row carries re-runnable arithmetic):

```
REAL   : width-set=[12] caught=11 -> [22,24,34,66,69,74,96,100,146,149,335]
POISON : width-set=[12] caught=12 -> [...,158,...]
NEW catches from the two planted defects: [158]     (plus [166] from Run 1)
```
**Both planted defects are caught, one per run** — L158 by `evidence_class off-vocabulary: '1997-05-14'`
and `source_date not a date: 'S-1/A No. 5 l.3739…'`; L166 by `UNFILED INPUTS ['6590.3']`.

**Honest reporting of the 11 pre-existing flags on the untouched register:** all 11 were traced and
**none is a register defect.** L22/24/34/66/69/100/146/149 fire only because the arithmetic grammar does
not tolerate a `$` between the operator and its operand (`582,528 × $0.1717 = …`) — false positives of my
regex, each row re-checked by hand in §1.1 and correct. L74/L96/L335 print compound `source_date` cells
(`1997-05-09 / 1997-05-14 (199…`, `1997-05-14 (No. 5 only)`, `1998-03-30 · 1999-03-05 · 20…`) — legal
annotations, not shifts. So the structural verdict on the live register is **clean at 12 columns, with
no evidence_class or source_date cell out of vocabulary**.

**Verdict — check 7: PASS** (validator proven against both planted defect classes; the naive
width-only form is proven insufficient, which is the point of the exercise).

---

## 8. Ghost sweep — no survivor of the fabricated FY1996 set, no return of the dead legs

### 8.1 The fabricated set (U.60)
Searched 15 strings (`12,284 3,462 4,322 850 1,326 3,036 (0.18 2,398 3,268 8,839 5,804 10,093 96.8 27.4
21.99`) across 26 files (3 Stage-2 volumes, 2 claim-record volumes, index, manifest, corrections,
adversarial review, all nine registers, the `_parts` drafts). **Live-value occurrences in the nine
registers: ZERO.** The 11 hits in `quantitative.csv` (L122, L153, L155-L158, L160, L161, L163, L166,
L172) each sit in a `CORRECTED from the received X` note with the filed term in the `value` column;
the 7 in `conflicts.csv` are inside the U.60-block prose; `timeline.csv`, `decisions.csv`,
`failures.csv`, `channels.csv`, `sources.csv`, `validation.csv`, `CORRECTIONS.md` return **0**.
Each fabricated term was separately confirmed dead against the filings themselves, and its filed
replacement confirmed live: cost of sales 12,287 (l.3732), gross profit 3,459, marketing 6,090,
product development 2,313, G&A 1,035, opex 9,438, net loss (5,777), LPS (0.25), inventory 571
(l.3663), AP 2,852 (l.3675), assets 8,271 (l.3670), equity 3,401 (l.3703). The received set's own
identity fails: 3,462 − 6,498 = (3,036) foots only against retracted terms, and (3,036) ÷ 22,655 =
$(0.134) ≠ $(0.18) ✓ (independently re-derived here).
Also dead: `74.6` as sales-per-employee (0 occurrences in A5; the band is 186-194), `$360,146,844`
(1 register hit, inside the retraction prose at §P99 only), `15.0%` as dilution, `5,112 / 32.5`.

### 8.2 The retracted Stage-1 legs
`871,000 / 871,024 / 976,408 / 2,613,000` — 15 hits in `quantitative.csv`, all in L35's and L172's
withdrawal prose ("**BOTH FIGURES … RETRACTED**", "the 871,000 / 2,613,000 leg stays RETRACTED (U.107)");
8 in `conflicts.csv` (U.107 and its cross-references); 4 in `data_gaps.csv`; 2 in
`context_appendices.md` (l.598, l.641) — and both appendix occurrences are now **inside explicit
retraction sentences** ("the fourth leg was printed here first as $871,024 … Both are withdrawn"),
with the row's value cell printing `≈$976,000 (±$1,000) un-named` and "NO COMPOSITION TOTAL IS PRINTED
ON THIS ROW". `2,613,000` remains at 0 occurrences in every filing ✓.
**Residue found:** `conflicts.csv` row 108 (U.107) still asserts as an *open* conflict that
"`context_appendices.md` still print[s] 2,613,000 and 871,000", and §R/§P route items repeat it
(`stage_2_part_3.md`:215, `_parts/s2_p1.md`:258, `stage_2_claim_records.md`:96). The appendix was since
rewritten, so the conflict as worded is stale → defect D-10.

### 8.3 The false cash bridge
`52 − 232 − 52 + 1,228 = 944` occurs 5 times in the repo's working files and **never as a live value**:
`quantitative.csv` L66 prints it inside "ROW REWRITTEN per verify-3 F-1 / RD-029: this cell read … for
three repair rounds, and the equation is false"; `validation.csv` row 17 and `stage_1.md` l.1012 do the
same. L66's live form is the correct one and it ties: −232 − 52 + 1,228 = **944** = filed l.3942, and
52 + 944 = **996** = filed l.3947 ✓. One caution: `_parts/NUMBER_DEFECTS.md`:55 lists
`52 − 232 − 52 + 1,228 = 996` in a `should_be`-shaped column — arithmetically true only because it
carries the opening balance on the left, which is what `validation.csv` row 17 says, but a repairer
reading only that line could re-adopt it → routed item R-02.

**Verdict — check 8 (sweep): PASS with 1 stale-register residue + 1 routed caution.**

---

## UNTRIED (budget)
- The 479 claim records were not each re-multiplied: I swept them for the ghost/retracted strings (§8)
  and spot-checked the money records behind §P. A per-record recomputation of the 112 §Q/§R records and
  of the Stage-1 records is UNTRIED.
- `research/ST2_*` dossier-level provenance (the layer beneath the registers) was used only to date the
  B&N read at S2C-20; the five Stage-2 dossiers were not recomputed line by line. UNTRIED.
- §F.3, §G.5, §H and §I-N narrative multipliers: I recomputed the ones that also sit in a register row
  or a §P row; the remainder of the prose-only ratios (e.g. §F.2's five repeat-customer measurements)
  were tested for register twins, not re-derived. PARTIALLY UNTRIED.
- The 1999-09-01 2-for-1 evidence (Q3-1999 10-Q footnote) is a Stage-3 document; I confirmed only that
  no Stage-2 figure inherits a 12× basis, and routed the Stage-3 L273 chain (R-01). The Stage-3 restated
  share arithmetic itself is UNTRIED.

## Defects for a separate repair pass

| # | File | Line | Current | Should be | Evidence |
|---|---|---|---|---|---|
| D-01 | `company_001_amazon/quantitative.csv` | L169 (row for 'Forward lease and service commitments') | `1540 / 122 = 12.6x FY1996 rent paid; 4323 / 122 = 35.4` | `1540 / 257 = 6.0x; 4323 / 257 = 16.8x` — FY1996 rental expense is $257,000 | A5 l.4383; S-1o l.4047; 424B1 l.4257; K97 l.2392 all print $257,000; 122 occurs nowhere as rent |
| D-02 | `stage_2_part_2.md` | 607 (§P150) | `**4,323**, of which **1,540** falls in 1997 = **6.4× the $122k of rent actually paid in FY1996** (1,540 ÷ 122 = 12.6; 4,323 ÷ 122 = 35.4)` | `= 6.0× the $257k of rent actually paid in FY1996 (1,540 ÷ 257 = 6.0; 4,323 ÷ 257 = 16.8)`; delete the 6.4 headline | same as D-01; 6.4 is not the quotient of any pair in the row |
| D-03 | `stage_2_part_2.md` | 525 (§P76) | `2,980.6 → rendered ≈3,081% increase / ≈29.8× the prior year` | `15,746 ÷ 511 = 30.814 → 30.8× the prior year; (15,746−511) ÷ 511 = +2,981.4% (the company prints "2,981%")` | A5 l.379/l.3731; K97 l.1380 prints 2,981%; §P.2 s2 (l.702-705) already retracts the 3,081% form; register L121 has it right |
| D-04 | `quantitative.csv` | L121 (and `stage_2_part_2.md`:702 §P.2 s2) | `15746 / 511 = 30.813` | `30.814` (exact 30.81409) | direct division |
| D-05 | `quantitative.csv` | L154 | `(5979) + 202 interest income = (5777); 5777 / 22655 = 0.2548` | `5777 / 22655 = 0.2550` (exact 0.2549989) | direct division; A5 l.3747/3752 |
| D-06 | `quantitative.csv` + `stage_2_part_2.md` | L124 / §P80a (l.530) | `28813 / 147758 = 0.194995` ; "exact 19.4995" | `0.1950013` / "19.5001%" | direct division; K97 l.1177/1180 |
| D-07 | `quantitative.csv` | L166 | `… x 365 = 39.5` (band "approximately 39.5 to 84.7") | `39.6` (exact 39.5690), or restate the band as ≈40 to ≈85 | 2,852 ÷ 26,308 × 365 = 39.5690 |
| D-08 | `quantitative.csv` | L207 vs L124/L181 | FY1997 net sales printed as 147,787 (L207) and 147,758 (L124/L181) with no basis label on either | label L207 `147,787 (pooling-restated per 10-K FY1998 l.1222 fn(1))` and L124/L181 `147,758 (as filed, FY1997 10-K l.1177)` | K97 l.1177/1380/1861 = 147,758, 838%; K98 l.1222/1309 = 147,787, 839%, footnote l.1269 "Reflects restatement for pooling of interests" |
| D-09 | `stage_2_part_2.md` | 604 (§P147) | `$(0.31)` listed as the FY1996 LPS "in the 10-K405" | `$(0.31) — PRO FORMA (preferred converted), K97 l.1194; the 10-K's pro-forma share line l.1197 = 18,544` | K97 l.1194 caption "Pro forma basic and diluted loss per share"; 5,777 ÷ 18,544 = 0.31153 |
| D-10 | `conflicts.csv` | row 108 (U.107) | asserts "Context appendices **still print** 2,613,000 and 871,000" as an open residue | re-state as CLOSED: `context_appendices.md` l.598/l.641 now carry the pair only inside withdrawal prose; no live value remains | read of l.598 and l.641 in full; §P value cells print `≈$976,000 (±$1,000) un-named` |
| D-11 | `quantitative.csv` + `stage_2_part_2.md` | L181 / §P164-§P165 | B&N figures classed `FACT (audited counterparty)`; ratios printed `155.5×`, `16.6×` | class `UNKNOWN (no local copy; transcription of a temporary read at S2C-20)` and mark both ratios UNKNOWN; state that the numerator covers the **53 weeks ended 1997-02-01** against Amazon's 52-week FY1996 and post-boundary FY1997 | §P164's own `(NO LOCAL COPY …)`; grep of the five Amazon filings: 0 hits for `2,448` and `431 superstores` |
| D-12 | `quantitative.csv` + `stage_2_part_2.md` | L166, L171 / §P120, §P166 | days-payable and runway rows use 365 and 366 for the same fiscal year without saying why | one basis stated per row (FY1996 is a 53-week leap year: 366 days; 365 is a convention) | A5 l.3900-3947 covers 1996 (leap); the rows' own denominators differ |
| D-13 | `stage_2_part_3.md` | §Q, 68 rows (l.18-111) | 7 dated events have no `timeline.csv` twin (1996-02-01, 1996-08-01, 1996-11-01, 1997-01-01→31, 1997-01-09/02-27, 1997-02-28, 1997-03-01) and 22 more sit at month/quarter granularity the register does not carry | add the seven `stage2` rows at the §Q dates and give `timeline.csv` month-level rows (or a `date_precision` column) for the 22 | direct test of every §Q date cell against `timeline.csv:date_or_range` |
| D-14 | `quantitative.csv` | L115 | `8000014 / 569396 = 14.0500007` | `= 14.0500004` | direct division (14.05000035) |

**Routed, not defects:** R-01 Stage-3 `quantitative.csv` L273 split chain `9,885,000 × 2 × 3` omits the
1999-09-01 2-for-1 → Stage-3 gate. R-02 `_parts/NUMBER_DEFECTS.md`:55 prints the retired bridge form in
a `should_be` column. R-03 §P145 (Series A conversion trigger ≥$20.00 AND ≥$7,500,000) has no
`quantitative.csv` twin despite both terms being filed (S-1o l.5307, l.5312). R-04 the annual FY1996
percentages (38.7 / 14.7 / 6.6 / 59.9) cite "A5 ratio table l.1703", which is the **quarterly** table;
the annual prints are K97 l.1435 / l.1464 / l.1495 — the numbers are right, the pointer mis-leads.

## Overall verdict

**CONDITIONAL FAIL.**

The spine holds. Every statement identity in the FY1996 audited set, the FY1995 comparatives and the
Q1-1997 unaudited column re-foots from the printed filing lines (34/34, §4); the working-capital
boundary is stated correctly at both dates and no row anywhere uses 79 as a year-end figure; no survivor
of the fabricated FY1996 money set is live in any register; the retracted `871,000 / 871,024 / 976,408 /
2,613,000` family and the false cash bridge survive only inside withdrawal prose; the §U ↔ `conflicts`
invariant is exact at 70 ↔ 70; no held Stage-3 row leaked; and Stage 2 is clean on the 6×/12× split
basis.

What fails is the layer the stage itself keeps promising — *every derived figure prints its exact
arithmetic*: **one input in the register is not the filed number at all** (the FY1996 rent of 122
against a filed $257,000, which silently re-scales two published multipliers and is the single most
serious defect here), **one §P row prints the retracted 3,081%-as-increase inversion that its own §P.2
note forbids** (and disagrees with its register twin), **two ratios rest on a denominator the corpus
declares unverifiable while the register classes the same figures FACT**, and six rows print an "exact"
quotient that is not exact. None of them changes a Stage-2 conclusion; all of them are things a founder
reading the sheet would be misled by, and D-01/D-03/D-11 are the three that must be repaired before this
stage's numbers are quoted anywhere else.
