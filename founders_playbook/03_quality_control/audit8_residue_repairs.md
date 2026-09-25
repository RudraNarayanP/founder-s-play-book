# AUDIT 8 — RESIDUE REPAIRS (Amazon Stage 1 appendix + Stage 2 draft volume)

Produced 2026-09-25 by the residue-repair pass. Scope: the two files AUDIT 8 (Stage 1) and the Stage-3
pass (`_parts/s3_p4.md`, U.168) reported as never having received the retraction. **Method: retract, never
substitute; supersede in place, never rewrite an intermediate volume silently.**
Files touched: `01_companies/company_001_amazon/context_appendices.md`,
`01_companies/company_001_amazon/_parts/s2_p4.md`, this sheet. No register, no `stage_1.md`, no Stage-2
deliverable volume, no `_parts/s3_*` was opened for writing. Zero web requests.

## 1. Headline finding — the AUDIT 8 premise is stale, and the fix is a tag not a retraction

AUDIT 8 says `context_appendices.md` "still runs `$871,000` and `2,613,000` live, twice each".
Read in full, the two rows are **not** asserting those figures: they print them **inside their own
withdrawal sentences**, with the correct value already carried as UNKNOWN.

- l.598 (row "Capital raised inside Stage 1"): `**RETRACTION, this row having carried the number twice:**` …
  `**Both are withdrawn, because the denominator` 2,613,000 `occurs in none of the restored documents** — zero
  occurrences in the original S-1, S-1/A No. 3, S-1/A No. 5 and the FY1997 10-K405` … `**NO COMPOSITION TOTAL IS
  PRINTED ON THIS ROW**` … confidence column closes `**UNKNOWN for the composition of the ≈$976,000 un-named
  residual, and for any fourth leg**`.
- l.641 (data-gap row 12): `**The leg that stood in for the rest is RETRACTED** — first **$871,024** … then
  **$871,000** (`2,613,000 ÷ 3`) — because the denominator `2,613,000` occurs in none of the restored documents
  and its only route in is the `stage_1.md` §P.2 d25 chain, which that register holds at UNKNOWN and NOT ADOPTED`.

This was already adjudicated once, in the file that reported it: `_parts/s2_p4.md` **U.107** ("CLAIM B: the
appearances are inside a row that labels them retracted … so the volume is not asserting the figures";
"Recorded, not fixed: `context_appendices.md` is not this part's file").

Corpus check (re-run of the AUDIT 8 test): `grep -rl "2,613,000" sources/` → **0 files**;
`grep -rl "871,0" sources/` → **0 files**; `grep -rl "3,021,000" sources/` → **14 files**.
The `sources/` directory holds 99 entries. So the denominator has no filed support anywhere on disk and the
correct in-window value is **UNKNOWN — reason: the figure occurs in zero of the restored filing texts, and its
only route into the dossier was a back-solved quotient of a number no document prints.**

**Therefore: nothing was substituted and nothing was deleted.** Each appearance keeps its digits (rule 4 — a
retracted figure held visible inside its own retraction is the correct forensic treatment) and gains a **dated,
machine-greppable** tag so a copy-out or grep register can no longer read a withdrawal as an assertion — which
is exactly how `$871,024 → $871,000` propagated the first time.

## 2. Site register — site / before → after / evidence line

| # | File · site | Value(s) | Before | After | Evidence line (as read on disk) |
|---|---|---|---|---|---|
| R-1 | `context_appendices.md` l.598 | `$871,000` ×1 · `2,613,000` ×2 · `$871,024` ×1 · `$976,408` ×1 | 0 live / 5 retraction-quoted, undated | 0 live / 5 retraction-quoted + **dated 2026-09-25 tag** → `CORRECTIONS.md`, `stage_1.md` §P.2 d8a, `audit8_stage1_certification.md` | "Both are withdrawn, because the denominator `2,613,000` occurs in none of the restored documents" |
| R-2 | `context_appendices.md` l.641 | `$871,000` ×2 · `2,613,000` ×2 · `$871,024` ×1 | 0 live / 5 retraction-quoted, undated | 0 live / 5 retraction-quoted + **dated tag**; composition stated UNKNOWN with reason | "which that register holds at UNKNOWN and NOT ADOPTED." |
| R-3 | `_parts/s2_p4.md` l.43 + l.859 | `19.4995` (2) | 2 stale (draft §P row + U.60 block) | 2 tagged SUPERSEDED — true quotient `28,813 ÷ 147,758 = 19.50013%` | `stage_2_part_2.md` l.530, `stage_2_part_3.md` l.486 |
| R-4 | `_parts/s2_p4.md` l.215, l.217, l.751, l.2106 | `30.813` (4) | 4 stale | 4 tagged SUPERSEDED — `15,746 ÷ 511 = 30.81409` | `stage_2_part_2.md` l.525, l.702; `stage_2_claim_records.md` l.616 |
| R-5 | `_parts/s2_p4.md` l.91?, 120, 499, 514, 567, 2151, 2153, 2154, 2253, 2294, 2298 | `$122k` as FY1996 rent (all `$122k` copies) | live-as-truth in the draft | each copy tagged — **filed FY1996 rent is $257k**, A5 l.4383 | `stage_2_part_2.md` l.418/l.578; `stage_2_part_3.md` l.73; `amazon_s2_audit3_repairs.md` D-01/D-02 |
| R-6 | `_parts/s2_p4.md` l.120 | `6.4×` | 1 stale quotient (of no pair; it is 1,540 ÷ 242, the Q1-1997 quarter) | tagged — repaired reading **6.0×** (`1,540 ÷ 257 = 5.9922`) | `stage_2_part_2.md` l.418, l.607 |
| R-7 | `_parts/s2_p4.md` l.88, l.298, l.555, l.943 | `≈39.5` days | 4 stale low-term copies | tagged — low term **39.6** (`2,852 ÷ (6,577 × 4) × 365 = 39.5690`), band 39.6–84.7 (366-day variant 39.7–85.0) | `stage_2_part_2.md` l.575; `amazon_s2_audit3_repairs.md` D-07/D-12 |
| R-8 | `_parts/s2_p4.md` l.2166, 2167, 2195, 2227, 2251, 2306 | class `FACT (audited counterparty)` | 6 stale labels in the CSV append block | tagged STALE CLASS LABEL — reclassified on the Stage-2 numbers pass | `amazon_s2_audit3_repairs.md` sweep table ("old counterparty class x9 … 0 live") |
| R-9 | `_parts/s2_p4.md` top of file | — | no supersession notice | `## SUPERSEDED 2026-09-25` banner → repaired deliverables + repair sheet; covers every remaining byte (incl. the CSV append block, which is deliberately **not** re-stated so widths and quote structure survive) | `_parts/s2_p4.md` l.1; `amazon_s2_audit3_repairs.md` l.197 "siblings outside the editable paths still hold the old numbers" |

## 3. Sweep the class, not the list — commands

From `founders_playbook/01_companies/company_001_amazon/` (excludes `_parts/s3_*`, read-only to two auditors):

    find . -name '*.md' -o -name '*.csv' | grep -v '/_parts/s3_' \
      | xargs grep -c -E '871,000|871,024|976,408|2,613,000'

Folder-wide line-level classification with the retraction-window heuristic
(`RETRACTION-QUOTED` = the same line also carries RETRACT / withdraw / UNKNOWN / not adopted / superseded /
stale / reclass / "occurs in none"):

    BEFORE (2026-09-25, pre-edit):
      871,000    LIVE 36 · RETRACTION-QUOTED 55
      871,024    LIVE  8 · RETRACTION-QUOTED 24
      976,408    LIVE 12 · RETRACTION-QUOTED 21
      2,613,000  LIVE 47 · RETRACTION-QUOTED 58
    AFTER (see audit trail line in this row's own footer; counts reported in the hand-back)

Targeted sweeps for the Stage-2 classes:

    grep -rn -E '6\.4×|30\.813|19\.4995|≈39\.5|\$122k|FACT \(audited counterparty\)' . | grep -v '/_parts/s3_'
    grep -rl '2,613,000' sources/ | wc -l      # -> 0 (no filed support anywhere)

### Live-count deltas attributable to this pass

| Class | Live before | Live after | Note |
|---|---|---|---|
| `$871,000` / `$871,024` / `$976,408` / `2,613,000` in `context_appendices.md` | 0 | 0 | already retracted; only dated tags added |
| `$122k`-as-rent / `6.4×` / `30.813` / `19.4995` / `≈39.5` in `_parts/s2_p4.md` | 15 tagged sites (1+3+4+2+4 ≈ 14 copies + the `6.4×` cell) | 15 dated SUPERSEDED tags | values never deleted; the volume's bytes are preserved |
| `FACT (audited counterparty)` in `_parts/s2_p4.md` | 6 | 6 tagged STALE | labels kept for the merge audit trail |
| Outside this pass's editable scope (`stage_1.md`, `stage_2_*`, `research/*`, `_parts/s1_*`, `_parts/NUMBER_DEFECTS.md`, `_parts/s2_p1/p3.md`, `stage_3_part_3.md`, `_MANIFEST.md`) | see BEFORE block | unchanged | reported, not edited |

## 4. Invariant check (run 2026-09-25, before and after)

- §U Stage 1: `stage_1.md` distinct `**U.n —**` blocks **43** ↔ `conflicts.csv` stage-1 rows **43**; ids U.1–U.43, **no gaps**.
- §U Stage 2: `stage_2_part_3.md` blocks **70** ↔ `conflicts.csv` stage-2 rows **70**; ids U.44–U.113, **no gaps**.
  (`_parts/s2_p4.md` still headers itself "U.44 → U.111", 68 blocks — the pre-merge draft subset; left as-is, covered by the banner.)
- Register widths uniform: conflicts 15 · quantitative 12 · sources 18 · data_gaps 8 · validation 11 · channels 11 ·
  timeline 11 · decisions 15 · failures 11 — one width per file, no ragged rows.

## 5. Not resolvable locally

1. **AUDIT 8's own wording is now the stale artifact.** It states the pair "still runs live" in
   `context_appendices.md`; the bytes on disk show retraction sentences. `audit8_stage1_certification.md` was
   not edited (not in this brief's paths) — the certification should be re-worded by its owner, or this sheet
   read beside it. The U.107 line references (`l.596, l.639`) have also shifted to l.598 / l.641.
2. **Whether the 36/47 "LIVE" folder-wide hits for the `$871,000` / `2,613,000` family are real** cannot be
   settled from a line-window heuristic: `stage_1.md` and the CSV registers carry very long rows where the
   withdrawal language sits in a different cell than the digits. Re-running the same sweep **after** the tag
   insertions is the next step; the definitive test is per-cell parsing of `quantitative.csv` / `conflicts.csv`,
   which is register work and outside this brief.
3. **The exact repaired spelling of the counterparty class** in each merged row: the Stage-2 repair sheet records
   the reclassification ("RECLASSED from FACT (audited, counterparty)"), so the draft label here is marked stale
   without asserting a replacement mapping.
4. `_parts/s3_p4.md` (U.168) reports the same residue; two auditors are reading `_parts/s3_*` now, so those
   copies were left untouched.
