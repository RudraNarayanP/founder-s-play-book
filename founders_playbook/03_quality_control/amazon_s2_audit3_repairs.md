# AMAZON S2 — AUDIT 3 (NUMBERS) — REPAIR LOG

**Repair agent:** numbers-repair-3. **Work order:** `amazon_s2_audit3_numbers.md` (CONDITIONAL FAIL).
**Repo scope:** `stage_2_part_1/2/3.md`, `stage_2_claim_records.md` + `_part_2.md`, `stage_2_index.md`,
the nine registers, this sheet. **Untouched:** Stage 1, `_parts/s1_*`, `_parts/s3_*`, `research/ST2_*`,
`research/ST3_*`, `MASTER_RESEARCH_LOG.md`, `CORRECTIONS.md`, other companies. **Zero web requests.**
**Log written before the first edit, and appended as work proceeds.**

## Method rules adopted
1. Read every source line before editing it. No substitution of one unsourced number for another.
2. If a correct value is not printed on disk → UNKNOWN with the reason, not a back-solve.
3. Sweep the CLASS: for every corrected figure, grep the whole company folder for the old digits AND
   the construction; classify each hit live value / cited source text / retraction; report counts.
4. Preserve invariants: §U.44–U.113 ↔ Stage-2 `conflicts.csv` 70↔70; nine registers uniform width,
   no renumber/reorder of held Stage-3 rows; `derived_arithmetic` on every DERIVED row; the false bridge
   `52 − 232 − 52 + 1,228` and the fabricated FY1996 set at zero live copies.

## Repair table (status: PENDING → DONE / RECLASSIFIED-UNKNOWN / NOT FIXED)

| ID | Site | Before → After | Evidence line to read | Sweep command | Status |
|---|---|---|---|---|---|
| D-01 | `quantitative.csv` L169 | `1540 / 122 = 12.6x; 4323 / 122 = 35.4` → `1540 / 257 = 5.99; 4323 / 257 = 16.8` + RETRACTION of 122 | A5 l.4383; S-1o l.4047; 424B1 l.4257; K97 l.2392 | `grep -rn "122" company_001_amazon` filtered to rent construction; `/ 122`, `÷ 122`, `$122` | OUTCOME LOG BELOW |
| D-02 | `stage_2_part_2.md` §P150 (l.607) | `6.4× the $122k` → `6.0× the $257k`, 6.4 headline deleted, 16.8 second term | same four lines | `grep -rn "6.4×\|6.4x\|122k" stage_2_part_*.md claim records` | OUTCOME LOG BELOW |
| D-03 | `stage_2_part_2.md` §P76 (l.525) | `2,980.6 → ≈3,081% increase / ≈29.8×` → `30.814 → 30.8× prior year, +2,981.4% (company prints 2,981%)`, retraction kept visible | A5 l.3731/l.379; K97 l.1380 | `grep -rn "3,081\|2,980.6\|29.8×" stage_2_part_*.md` + claim records | OUTCOME LOG BELOW |
| D-04 | `quantitative.csv` L121, `stage_2_part_2.md` §P.2 s2 | `30.813` → `30.814` | direct division | `grep -rn "30.813"` | OUTCOME LOG BELOW |
| D-05 | `quantitative.csv` L154 | `0.2548` → `0.2550` (exact 0.2549989) | A5 l.3747/3752 | `grep -rn "0.2548"` | OUTCOME LOG BELOW |
| D-06 | `quantitative.csv` L124 + §P80a l.530 | `0.194995`/"exact 19.4995" → `0.1950013`/"19.5001%" | K97 l.1177/1180 | `grep -rn "19.4995\|0.194995"` | OUTCOME LOG BELOW |
| D-07 | `quantitative.csv` L166 + §P120 | `39.5` → `39.6` (exact 39.5690), run-rate gloss kept | A5 l.3675, l.1378/1667 | `grep -rn "39.5"` whole folder | OUTCOME LOG BELOW |
| D-08 | `quantitative.csv` L207 vs L124/L181 | add basis labels: 147,787 = pooling-restated (K98 l.1222 fn(1)); 147,758 = as filed (K97 l.1177) | K97 l.1177/1380/1861; K98 l.1222/1309/1269 | `grep -rn "147,787\|147787\|147,758\|147758"` | OUTCOME LOG BELOW |
| D-09 | `stage_2_part_2.md` §P147 (l.604) | `$(0.31)` → labelled PRO FORMA (preferred converted), K97 l.1194 + share line l.1197 18,544 | K97 l.1194/1197 | `grep -rn "0.31"` | OUTCOME LOG BELOW |
| D-10 | `conflicts.csv` row 108 (U.107) + §R `stage_2_part_3.md`:215 | "appendices still print 2,613,000/871,000" → CLOSED: pair survives only inside withdrawal prose at l.598/l.641 | context_appendices l.598, l.641 | `grep -rn "2,613,000\|871,000\|871,024\|976,408"` | OUTCOME LOG BELOW |
| D-11 | `quantitative.csv` L181 + §P164/§P165 | class `FACT (audited counterparty)` → `UNKNOWN (no local copy)`; both multipliers marked UNKNOWN; state 53-week-ended-1997-02-01 vs Amazon 52-week FY1996 / post-boundary FY1997 | §P164's own NO LOCAL COPY; grep 2,448 / "431 superstores" in filings | `grep -rn "2,448\|2448\|155.5\|16.6×" whole folder + sources` | OUTCOME LOG BELOW |
| D-12 | `quantitative.csv` L166, L171 + §P120, §P166 | state per-row day basis (FY1996 = 53-week leap year, 366 days; 365 a convention) | A5 l.3900-3947 | `grep -rn "365\|366" register + §P120/166` | OUTCOME LOG BELOW |
| D-13 | `stage_2_part_3.md` §Q ↔ `timeline.csv` | 7 dated §Q events with no timeline twin + 22 granularity rows: add stage2 rows at the §Q dates, or record precision; no renumbering | direct test of §Q date cells vs `timeline.csv` | `grep -n "1996-02-01\|1996-08-01\|1996-11-01\|1997-01-09\|1997-02-27\|1997-02-28\|1997-03-01" timeline.csv` | OUTCOME LOG BELOW |
| D-14 | `quantitative.csv` L115 | `14.0500007` → `14.0500004` | direct division | `grep -rn "14.050000"` | OUTCOME LOG BELOW |
| X-1 | §P↔register disagreement 3 (§P164/L181) | folded into D-11 | — | — | OUTCOME LOG BELOW |
| X-2 | §P145 no register twin (R-03) | route or add row; decide after register-width check | S-1o l.5307/5312 | `grep -rn "7,500,000\|20.00"` | OUTCOME LOG BELOW |

## Outcome log
(Sections are appended in the order the work finished, not in defect order.)

### D-03 / D-04 — §P76's inverted growth pair, and the 30.813 tail — **FIXED (narrative now agrees with the register; retraction kept visible)**
Inputs re-read: A5 l.3731 prints `511` (FY1995) and `15,746` (FY1996); 10-K405 l.1380 prints `$147,758 838% $15,746 2,981% $511`.
Re-divided by hand: `15,746 ÷ 511 = 30.81409` and `(15,746 − 511) ÷ 511 = 15,235 ÷ 511 = 29.81409 → +2,981.4%`.
§P76 now prints exactly that pair, with the received "2,980.6 → ≈3,081% increase / ≈29.8× the prior year" quoted
inside a RETRACTED-IN-FULL sentence that names the inversion and points at §P.2 s2 and register L121.
**Sweep, class = "the 3,081%-as-increase inversion printed as a live value":** BEFORE 1 live site (§P76) + 30.813 at
6 sites (register L121, §P.2 s2 ×2, claim record P24, §U.47 CLAIM B, U.47 claim record). AFTER 0 live; the string
`30.813` returns **0** hits in editable files; 5 retraction/claim-quotation occurrences of "3,081%" and "2,980.6"
remain, all inside sentences that retract them (§P76, §P.2 s2, §U.47 CLAIM A, U.47 claim record, conflicts.csv U.47,
register L121 note). `_parts/s2_p4.md` still carries the old pair (out of scope; reported).

### D-05 / D-06 / D-07 / D-14 — false-precision tails — **FIXED (9 sites)**
Re-computed each: `5,777 ÷ 22,655 = 0.2549989` (was 0.2548); `28,813 ÷ 147,758 = 0.1950013 → 19.50013%`
(was 0.194995 / "exact 19.4995"); `2,852 ÷ (6,577 × 4) × 365 = 39.5690 → 39.6` (was 39.5, a rounding step that
understated the band's foot); `8,000,014 ÷ 569,396 = 14.05000035 → 14.0500004` (was 14.0500007). Filed terms used
were re-read at A5 l.3731/l.3747-3752, 10-K405 l.1177/l.1180/l.1403, 424B1/A5 Item 5.
Sites: `quantitative.csv` L154, L124, L166, L115; `stage_2_part_2.md` §P80a (l.530), §P120 (l.575), §P.2 s1 (694),
s11 (754), s16 (785-789); `stage_2_part_3.md` l.130, 486, 561, 565, 570-575; `stage_2_claim_records.md` l.499, 602,
652, 662, 874; `stage_2_claim_records_part_2.md` U.52 (l.64) and U.56 (l.72, three occurrences); `conflicts.csv`
U.56 (l.57, three occurrences). **Sweep before → after:** `19.4995` 4 → 0 live / 2 retraction; `0.2548` 2 → 0 live /
2 retraction; `14.0500007` 2 → 0 live / 2 retraction; `≈39.5` as a live band term 11 → 0 (all remaining `39.5` hits
are either the retraction sentence or the substring of the correct `39.5690`).

### D-08 — the two FY1997 bases in one register — **FIXED (labels added; no row moved)**
Lines re-read: 10-K FY1997 l.1177 / l.1380 / l.1861 = **147,758** with FY1997 growth **838%**; 10-K FY1998
l.1222 / l.1309 = **147,787** with growth **839%**, under the footnote at l.1269 *"(1) Reflects restatement for
pooling of interests."* Labels added: L207 (Stage-3 row — **notes cell only, no renumber/reorder**) states the
pooling-restated basis, the as-filed alternative `609,996 / 147,758 = 4.12830`, and that the rendered 4.13 is
basis-independent; L124 and §P80a state `147,758 = AS FILED (K97 l.1177/l.1380/l.1861)` and that 147,787 is not used
there. **Sweep before → after:** `147,787`/`147787` live-unlabelled in the shared register = 1 (L207) → 0; Stage-3
narrative copies in `_parts/s3_*` and `research/ST3_*` left to their own gate (R-01).

### D-11 — the B&N pair — **RECLASSIFIED-UNKNOWN (12 sites, class + period + numerator provenance)**
Verified first, on disk: `grep` of `sources/` returns **0** hits for `2,448` and **0** for `431 superstores`; the only
B&N witness is `sources.csv` **S2009**, whose notes read *`local_copy: NO (no byte in sources/ — the witness is read
only through a dossier transcription)`* — re-read directly, so the reclassification rests on a disk fact, not on
§P164's self-declaration alone. Amazon-side denominators confirmed filed (A5 l.3731 = 15,746; K97 l.1177 = 147,758).
Re-divided: `2,448,000 ÷ 15,746 = 155.47`, `÷ 147,758 = 16.57`.
Changes: `quantitative.csv` L181 evidence_class → **UNKNOWN (no local copy; transcription of a temporary read at
S2C-20)** with both ratios labelled UNKNOWN + the 53-week/52-week/post-boundary mismatch in `derived_arithmetic`, and
its `value` cell now opens **`NOT-ON-DISK:`** so the numerator cannot be read as a filed figure; L182 (the 344,000 sq
ft DC row, same provenance) reclassed the same way; `timeline.csv` two B&N rows reclassed (High → Medium);
`validation.csv` L38 reclassed with its `155.5x`; §P164's class cell → UNKNOWN; §P165 rewritten (ratios printed as
UNKNOWN, 53-week mismatch stated, "restated in absolute **filed** terms" removed); §U.66/§U.67 evidence-weight lines,
`conflicts.csv` U.66 + U.67 (including "the **filed** figures give" → "the **transcribed** B&N figure"), claim records
I17, P90, U.67 heading; §Q 1997-05-02 row, §R Competitors row, §C competition table and the §M/§I lines now carry the
NO-LOCAL-COPY gloss. **Sweep before → after, class = "a B&N figure presented as filed":** 19 sites carrying
`2,448 / 2.448 / 2448 / 155.5 / 16.6× / 431 superstores / FACT (audited counterparty)`; of those 12 carried no
local-copy caveat before → **0 now carry none** except `sources.csv` S0409 (Stage-1 row, already states "not on
disk"; not editable here) and `stage_2_part_1.md` l.162/477 (narrative C-flag rows that point at the §U conflict
which now carries the class). `FACT (audited counterparty)` as a class string: 6 occurrences before → 0 live (the two
in `sources.csv`/`_parts` are provenance notes for the Stage-1/Stage-3 row).

### D-12 — 365 vs 366 for the same fiscal year — **FIXED (basis stated on every affected row)**
L166 (365, band restated on 366 as 39.7–85.0), L171 (366, restated on 365 as 16.62 / 9.78), §P120, §P.2 s16,
§U.56 and its claim record, `conflicts.csv` U.56 — each now names its convention and the leap-year reason, and
records that the difference is convention, not error.

### D-09 — the unlabelled pro-forma $(0.31) — **FIXED (11 sites)**
Read the filing: 10-K405 **l.1194** caption `Pro forma basic and diluted loss per share(1)` = `(0.31)` for 1996;
**l.1197** pro-forma share line = `21,651 / 18,544 / 14,394 / 13,191`; footnote at **l.2242–2245**: "to calculate pro
forma loss per share, all outstanding shares of convertible preferred stock are assumed to have been converted to
common stock for all periods presented." `5,777 ÷ 18,544 = 0.31153 → (0.31)` ✓ ties. §P147's header changed from
"three bases" to **"two as-filed bases and one PRO FORMA basis"**, and §U.55's RESIDUAL UNCERTAINTY ("which convention
produced $(0.31)") is **CLOSED at the line**. Class cell now splits: FACT (audited) for (0.26)/(0.25), **FACT (pro
forma, as captioned)** for (0.31). **Sweep before → after, class = "(0.31) without its pro-forma label":** 14 live
unlabelled sites → **4** remaining, all legitimate (the `(0.18)` retraction lists and the §S retraction line at
`stage_2_part_3.md`:179, which enumerates the filed set); glosses added at register L154, §P147, §I table l.255,
§R l.134, §S l.179, §T l.266, §U.55 CLAIM B/C + interpretation + uncertainty, claim records l.183/658/948,
U.55 record l.70, `conflicts.csv` U.55.


### D-01 / D-02 — FY1996 rental denominator 122 → 257 — **FIXED (13 live sites, not the 2 the sheet named)**
Source lines read in full before editing: A5 l.4383 ("… for 1994, 1995, and 1996 was $2,000, $12,000, and
**$257,000**, respectively, and $18,000 and $242,000 for the first quarter of 1996 and 1997"); S-1 original
l.4047; 424B1 l.4257; 10-K405 l.2392 ("for 1997, 1996 and 1995 was $2 million, **$257,000** and $12,000").
Commitment table re-read at A5 l.4396 (`1997 … $1,540`) and l.4402 (`$4,323`). No "122" anywhere in
`sources/` as rent (only as $122.5m FY1997 financing cash, 10-K405 l.1571, and $122.4m 1999 — unrelated).
**Site the auditor missed: `quantitative.csv` L168** — the register row whose `value` cell IS the FY1996
rent, printed `122` as FACT (audited). L169 was only the multiplier built on it.
Corrected quotients now printed: `1540 / 257 = 5.9922 → 6.0x`; `4323 / 257 = 16.8210 → 16.8x` (both
re-divided by hand; the old 12.6 / 35.4 were 2.1× too large). §P150's "6.4×" headline deleted outright —
it is the quotient of no pair. Derived claims that rested on 122 also rewritten: "Q1-1997 rent $242k =
**twice** the whole of FY1996" → **94% of** FY1996 (242 ÷ 257 = 0.9416), which agrees with the already-
correct sibling at `stage_2_part_1.md`:439 and `stage_2_part_2.md`:262.
**Sweep (before → after), class = "122 rendered as FY1996 rent":**
BEFORE: 13 live-value sites in editable scope — `quantitative.csv` L168, L169; `stage_2_part_2.md` §P122
(l.578), §P150 (l.607); `stage_2_part_3.md` l.73 (§Q 1996-12-31), l.88 (§Q 1997-Q1), l.142 (§R weaknesses);
`stage_2_claim_records.md` l.565, l.664 (P48), l.666 (P49), l.824 (Q52); `channels.csv` L24;
`validation.csv` L40. Zero retraction-labelled occurrences (the number was always carried as truth).
AFTER: 0 live; 13 retraction sentences (each carries the filed 257 and the four line cites); 0 cited-source
hits in `sources/`. **Out of scope and still stale: `_parts/s2_p4.md`** (l.91, 120, 499, 514, 567, 2151,
2153, 2154, 2253, 2294, 2298) — the drafting copy of §P/§Q that the brief excludes from my paths; reported,
not edited. `stage_1.md` l.1614 and `context_appendices.md` l.480 print the rent correctly (257) and were
not touched.

### D-10 — the stale appendix-residue conflict — **CLOSED (6 sites)**
Re-read `context_appendices.md` l.598 and l.641 in full: the value cells print `≈$976,000 (±$1,000) un-named` and
"**NO COMPOSITION TOTAL IS PRINTED ON THIS ROW**"; the digits survive only inside withdrawal sentences — counted
**2,613,000 ×4, 871,000 ×3, 871,024 ×2**, live values **0**. The conflict as worded ("still print[s] …" as an open
residue) is stale, and its own cites (l.596/l.639) are off by the rewrite. Restated as CLOSED in `conflicts.csv`
U.107, §U.107 (heading, CLAIM A marked superseded, re-read paragraph added, CONFIDENCE), §S row l.177,
`data_gaps.csv` l.43, claim records l.96 and the U.107 record — **the row is kept, not deleted**: the grep-and-lift
risk CLAIM C raised is real, and the propagation question stays UNKNOWN.

### D-13 — §Q rows with no `timeline.csv` twin — **FIXED for the 7 dated rows (8 register rows added); the 22 month/quarter rows left at source precision, deliberately**
Verified the absence first: all seven §Q dates returned **0** hits in `timeline.csv:date_or_range` before the repair.
Added as `stage2` rows inside the stage-2 block, immediately before the register's `UNKNOWN` catch-all row, with no
existing row moved or renumbered: 1996-02-01, 1996-08-01, 1996-11-01, **1997-01-01 -> 1997-01-31** (the B&N letter is
dated only to the month by the source, so its twin is a range row rather than an invented day), 1997-01-09 and
1997-02-27 (the two Trident amendments, which the §Q row carried together, split into one row each), 1997-02-28,
1997-03-01 = **8 rows**. The 22 month/quarter-granularity rows were **not** given day-level twins: that would
substitute dates the sources do not print. Recorded instead as a new `data_gaps.csv` row that splits the finding in
two. `timeline.csv`: 220 → **228** data rows, width uniform at **11**; no column was added to any register.

## Invariants, recomputed after every edit (measured, not assumed)
| Invariant | Before (auditor) | After (this pass) |
|---|---|---|
| §U blocks U.44–U.113 in `stage_2_part_3.md` | 70, none missing or duplicated | **70**, missing [], range 44–113 |
| Stage-2 rows in `conflicts.csv` | 70, 70 unique | **70**, unique U.44–U.113, **exact set match with the §U blocks** |
| `conflicts.csv` field width | 15 | **15 on all 153 lines** — after this pass's own first D-10 edit introduced a comma-in-unquoted-field 16-field row (caught by the width check, then repaired twice) |
| Nine registers uniform width | 12/11/15/15/11/11/8/18/11 | unchanged: quantitative 334×12, timeline 228×11, conflicts 152×15, decisions 25×15, failures 54×11, channels 23×11, data_gaps 88×8, sources 195×18, validation 52×11 |
| Total register data rows | ~1,142 | **1,151** = 1,142 + 8 timeline rows + 1 data_gaps row |
| `derived_arithmetic` on every DERIVED row | 83 DERIVED, 0 exceptions | **83 DERIVED, 0 missing**; arithmetic present on **104** rows |
| Fabricated FY1996 set live in a `value` cell | 0 | **0** — no `value` cell equals 12284 / 3462 / 4322 / 1326 / 2398 / 3268 / 8839 / 5804 / 10093; the strings persist only inside `CORRECTED from` notes |
| False bridge `52 − 232 − 52 + 1,228 = 996` live | 0 | **0** |
| 871,000 / 871,024 / 976,408 / 2,613,000 live in registers | 0 | **0** (every occurrence is retraction prose; the only rent `value` cell in the register is now **257**) |
| §P table | "121 rows" | **no row added or removed**: the §P ID set in `stage_2_part_2.md` is identical to the pristine draft `_parts/s2_p4.md` (136 P-labelled rows counting the correction sub-tables; 120 in the main table) — the 121 vs 120 gap is a parse-boundary difference, not a lost row |

## Every figure this pass printed, re-divided (the repair's own arithmetic audit)
`1540/257 = 5.99222 → 6.0` · `4323/257 = 16.82101 → 16.8` · `15746/511 = 30.81409` · `15235/511 = 29.81409 → +2,981.4%` ·
`28813/147758 = 0.1950013` · `5777/22655 = 0.2549989` · `8000014/569396 = 14.0500004` · `5777/18544 = 0.3115293 → (0.31)` ·
`2852/12287×365 = 84.7221` · `2852/26308×365 = 39.5690` · on 366: `84.9542 / 39.6774` · `79/(1735/366) = 16.6651` ·
`79/(2949/366) = 9.8047` · on 365: `16.6196 / 9.7779` · `2448000/15746 = 155.4681` · `2448000/147758 = 16.5676` ·
`609996/147787 = 4.12753` · `609996/147758 = 4.12835` · `242/257 = 0.94163 → 94%`.
**Four tails this pass first printed wrongly and then corrected against a calculator:** 84.7337 → **84.7221**;
16.6650 → **16.6651**; 4.12754 → **4.12753**; 4.12830 → **4.12835**. Reported because a repair pass that introduces
false "exact" digits is committing the very defect it is fixing.

## Where the auditor itself was wrong
1. **D-01/D-02 named 2 sites; the class has 14.** The register row **`quantitative.csv` L168**, whose `value` cell *is*
   the FY1996 rent and read `122` under `FACT (audited)`, appears nowhere in the sheet — L169 is only the multiplier
   built on it. §P122, the origin of the 122, was filed as a precision-laundering item (§3.2.3) and not as a D-01 site.
   The same 122 also lived at §Q l.73, §Q l.88, §R l.142, the §N decision table `stage_2_part_2.md`:418 (a second live
   **6.4×**), claim records l.565 / 664 / 666 / 824, `channels.csv` L24 and `validation.csv` L40. Repairing only the
   two named sites would have left 12 live copies of an unfiled denominator.
2. **Self-contradiction on L124.** §1.1 lists `28,813 ÷ 147,758 = 0.194995 → 19.5%` among the rows that "tie"; §1.2 and
   D-06 list the same cell as a defect. It is a defect: the quotient is 0.1950013.
3. **The register layer was worse than the narrative layer on B&N, and the sheet only half-said so.** It quoted §P164's
   NO-LOCAL-COPY language but did not flag that `conflicts.csv` U.67 asserts "**The filed figures** give 2,448,000 …"
   and that §U.67's EVIDENCE WEIGHT calls it "two audited numbers divided". Both had to be rewritten to close the class.
4. **D-04's target list under-counts the `30.813` tail** (6 sites: register L121, §P.2 s2 twice, claim record P24,
   §U.47 CLAIM B, U.47 claim record), and the inversion's × forms also sit in `conflicts.csv` U.47.
5. **§5.1's "§P 121 rows" does not reproduce** under a parser that stops at the first sub-heading (120), or one that
   counts the correction sub-tables (136) — the sheet should say which population it means.
6. **Siblings outside the editable paths still hold the old numbers**: `_parts/s2_p4.md` (pre-repair copies of §P/§Q and
   of the L168/L169 register rows, including `122` as rent and `30.813`) and `_parts/NUMBER_DEFECTS.md`:55 (the retired
   bridge form the sheet routes as R-02). Not touched here, but any later rebuild from `_parts` would re-import them.

## Final status line
D-01 FIXED · D-02 FIXED · D-03 FIXED · D-04 FIXED · D-05 FIXED · D-06 FIXED · D-07 FIXED · D-08 FIXED (labelled) ·
D-09 FIXED (labelled; §U.55 residual uncertainty closed at the line) · D-10 CLOSED · **D-11 RECLASSIFIED-UNKNOWN** ·
D-12 FIXED (basis named per row) · D-13 FIXED for the 7 dated rows / 22 left at source precision by design ·
D-14 FIXED. NOT FIXED: R-01 (Stage-3 split chain), R-02 (`_parts/NUMBER_DEFECTS.md`), R-03 (§P145 still has no
`quantitative.csv` twin — both terms are filed at S-1 orig. l.5307 and l.5312, and adding the row is a one-line job
for the next pass), R-04 (the FY1996 annual percentage rows still cite the quarterly ratio table at A5 l.1703 instead
of K97 l.1435/1464/1495 — pointer, not number).


## End-of-pass sweep (whole `company_001_amazon/`, sources/ and research/ excluded, `_parts/` reported separately)
| Class swept | Live copies BEFORE | Live copies AFTER | Labelled retraction/cited-source occurrences AFTER |
|---|---|---|---|
| `122` rendered as FY1996 rent | 13 (+1 second live `6.4x` headline at `stage_2_part_2.md`:418) | **0** | 3 (`quantitative.csv` L169 note + L168, §P122/§P150, §Q, §R, claim records, `channels.csv`, `validation.csv` — each quoting 122 as retracted) |
| `6.4×` as the rent multiplier | 2 | **0** | 0 (deleted, with the reason printed in §P150) |
| `30.813` | 6 | **0** | 0 (all rewritten to 30.81409) |
| the `3,081%`-as-increase inversion as a live value | 1 (§P76) | **0** | 5 (§P76, §P.2 s2, §U.47, U.47 claim record, `conflicts.csv` U.47) |
| `19.4995` / `0.194995` | 6 | **0** | 6 (all inside "the cell printed …, it is 0.1950013" sentences; Stage-3 files keep their own copies, out of scope) |
| `0.2548` | 2 | **0** | 2 |
| `14.0500007` | 2 | **0** | 2 |
| a live `≈39.5` days term | 11 | **0** | 0 (39.5690 printed instead; 39.5 survives only inside the D-07 sentences) |
| B&N `FACT (audited counterparty)` class | 16 across the folder (7 in editable Stage-2 paths + 9 in `_parts/s2_p4.md`) | **0 live** — 4 remaining mentions all read "RECLASSED from FACT (audited, counterparty)" | — |
| `(0.31)` with no pro-forma word on its line | 14 | **0** (the 4 that looked unlabelled are the §S retraction list and the `(0.18)` rejection prose) | — |
| **`_parts/s2_p4.md` (NOT an editable path here)** | — | still carries 122-as-rent x8, `6.4×` x1, `30.813` x4, `19.4995` x4, `39.5` x3, the old counterparty class x9 | **flagged for the next pass: a rebuild from `_parts` re-imports every defect closed today** |
