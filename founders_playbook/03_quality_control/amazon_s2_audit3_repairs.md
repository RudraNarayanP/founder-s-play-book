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
| D-01 | `quantitative.csv` L169 | `1540 / 122 = 12.6x; 4323 / 122 = 35.4` → `1540 / 257 = 5.99; 4323 / 257 = 16.8` + RETRACTION of 122 | A5 l.4383; S-1o l.4047; 424B1 l.4257; K97 l.2392 | `grep -rn "122" company_001_amazon` filtered to rent construction; `/ 122`, `÷ 122`, `$122` | PENDING |
| D-02 | `stage_2_part_2.md` §P150 (l.607) | `6.4× the $122k` → `6.0× the $257k`, 6.4 headline deleted, 16.8 second term | same four lines | `grep -rn "6.4×\|6.4x\|122k" stage_2_part_*.md claim records` | PENDING |
| D-03 | `stage_2_part_2.md` §P76 (l.525) | `2,980.6 → ≈3,081% increase / ≈29.8×` → `30.814 → 30.8× prior year, +2,981.4% (company prints 2,981%)`, retraction kept visible | A5 l.3731/l.379; K97 l.1380 | `grep -rn "3,081\|2,980.6\|29.8×" stage_2_part_*.md` + claim records | PENDING |
| D-04 | `quantitative.csv` L121, `stage_2_part_2.md` §P.2 s2 | `30.813` → `30.814` | direct division | `grep -rn "30.813"` | PENDING |
| D-05 | `quantitative.csv` L154 | `0.2548` → `0.2550` (exact 0.2549989) | A5 l.3747/3752 | `grep -rn "0.2548"` | PENDING |
| D-06 | `quantitative.csv` L124 + §P80a l.530 | `0.194995`/"exact 19.4995" → `0.1950013`/"19.5001%" | K97 l.1177/1180 | `grep -rn "19.4995\|0.194995"` | PENDING |
| D-07 | `quantitative.csv` L166 + §P120 | `39.5` → `39.6` (exact 39.5690), run-rate gloss kept | A5 l.3675, l.1378/1667 | `grep -rn "39.5"` whole folder | PENDING |
| D-08 | `quantitative.csv` L207 vs L124/L181 | add basis labels: 147,787 = pooling-restated (K98 l.1222 fn(1)); 147,758 = as filed (K97 l.1177) | K97 l.1177/1380/1861; K98 l.1222/1309/1269 | `grep -rn "147,787\|147787\|147,758\|147758"` | PENDING |
| D-09 | `stage_2_part_2.md` §P147 (l.604) | `$(0.31)` → labelled PRO FORMA (preferred converted), K97 l.1194 + share line l.1197 18,544 | K97 l.1194/1197 | `grep -rn "0.31"` | PENDING |
| D-10 | `conflicts.csv` row 108 (U.107) + §R `stage_2_part_3.md`:215 | "appendices still print 2,613,000/871,000" → CLOSED: pair survives only inside withdrawal prose at l.598/l.641 | context_appendices l.598, l.641 | `grep -rn "2,613,000\|871,000\|871,024\|976,408"` | PENDING |
| D-11 | `quantitative.csv` L181 + §P164/§P165 | class `FACT (audited counterparty)` → `UNKNOWN (no local copy)`; both multipliers marked UNKNOWN; state 53-week-ended-1997-02-01 vs Amazon 52-week FY1996 / post-boundary FY1997 | §P164's own NO LOCAL COPY; grep 2,448 / "431 superstores" in filings | `grep -rn "2,448\|2448\|155.5\|16.6×" whole folder + sources` | PENDING |
| D-12 | `quantitative.csv` L166, L171 + §P120, §P166 | state per-row day basis (FY1996 = 53-week leap year, 366 days; 365 a convention) | A5 l.3900-3947 | `grep -rn "365\|366" register + §P120/166` | PENDING |
| D-13 | `stage_2_part_3.md` §Q ↔ `timeline.csv` | 7 dated §Q events with no timeline twin + 22 granularity rows: add stage2 rows at the §Q dates, or record precision; no renumbering | direct test of §Q date cells vs `timeline.csv` | `grep -n "1996-02-01\|1996-08-01\|1996-11-01\|1997-01-09\|1997-02-27\|1997-02-28\|1997-03-01" timeline.csv` | PENDING |
| D-14 | `quantitative.csv` L115 | `14.0500007` → `14.0500004` | direct division | `grep -rn "14.050000"` | PENDING |
| X-1 | §P↔register disagreement 3 (§P164/L181) | folded into D-11 | — | — | PENDING |
| X-2 | §P145 no register twin (R-03) | route or add row; decide after register-width check | S-1o l.5307/5312 | `grep -rn "7,500,000\|20.00"` | PENDING |

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

