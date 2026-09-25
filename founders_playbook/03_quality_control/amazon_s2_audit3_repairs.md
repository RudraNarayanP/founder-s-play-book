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
Appended below as work completes.
