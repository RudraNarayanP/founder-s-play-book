# AUDIT 6 REPAIRS — work log for the closure of the six AUDIT-6 DEFECTs

Authority: `03_quality_control/audit6_stage1_independent_qa.md` (verdict REOPEN, CONFIRMED 7 / DEFECT 6).
Scope rule: close the 6 DEFECT items + the 3 named small residuals, touch nothing the verifier CONFIRMED,
preserve the four invariants (43 U blocks ↔ 43 `conflicts.csv` rows; 428 register data rows; 29/29 DERIVED
arithmetic coverage; 32/32 §P.2 figures).

Zero web requests made or needed (item 12 resolved from local evidence — see IR-19).

## Defect checklist

- [ ] **Item 4** — dead bridge prints live at `_parts/s1_p4.md:102–103` (+ pre-repair d4/d5/d7 values at `:96–98`)
- [ ] **Item 6** — retracted denominators live at `context_appendices.md:596` (Value column) and `:639`
- [ ] **Item 8** — COR-12 supersession unmarked at `CORRECTIONS.md:57–69`, `CORRECTIONS.md:194`, `_parts/s1_p3b_H_addendum.md:131`
- [ ] **Item 9** — filing-lineage demotion incomplete: `stage_1.md:16–17`, `:1139`, `:870`; `quantitative.csv:74`;
      `context_appendices.md:595`; `CORRECTIONS.md:241–242`; §T `stage_1.md:1204/1205/1206`; claim records
      `stage_1_claim_records.md:383`, `:397`, `:454`
- [ ] **Item 12** — adversarial attack A-B1 still lands (`amazon_s1_audit4_audit5_final.md:409`, `:431`)
- [ ] **Item 13** — fix-introduced false closure claims, incl. `stage_1.md:36` "four sites … corrected"
- [ ] **Residuals** — `stage_1.md:1251` stale U-preamble count; `quantitative.csv:34` 1-cent addend label;
      `timeline.csv:33` / `:55` mis-keyed to U.16

## Repair rows (file, line-as-received, before → after, why)

Lines are the AUDIT-6 numbers, re-located by grep before every edit.

| id | item | file | line (received) | before | after | why |
|---|---|---|---|---|---|---|
| IR-01 | 4 | `_parts/s1_p4.md` | 102–103 | d14 prints `52 − 232 − 52 + 1,228 = +944; 52 + 944 = $996` live, unannotated | filed two-line bridge `−232 − 52 + 1,228 = +944; 52 + 944 = $996`, with the false single-line form named and retracted in place | the false form is arithmetically wrong (LHS=996≠944); the filed terms are at `sources/S-1_original…txt:3636,3641,3649,3652,3653,3655`; a false equation must not read as live |
| IR-02 | 4 | `_parts/s1_p4.md` | 62 | d/P36-line bridge form `52 − 232 − 52 + 1,228` unannotated (the `=996` reading of the brief) | annotated as the opening-cash-inclusive form, or retracted if it is the false form | same rule: no unannotated false/false-labelled equation live in a report volume |
| IR-03 | 4 | `_parts/s1_p4.md` | 96–98 | pre-repair d4 `$100,019.06`, d5 `$145,552.83`, d7 `$295,567` | superseded-value annotation at each | sheet item 4 names them as surviving pre-repair figures in the same fragment |
| IR-04 | 6 | `context_appendices.md` | 596 | Value column runs `$871,000` / `2,613,000` / `$976,408` as live composition | RETRACTION in place: residual composition → UNKNOWN, reason = denominator unfiled (`2,613,000` absent from all `sources/` text) | figure was retracted because its denominator is unfiled; correct move is retraction not substitution |
| IR-05 | 6 | `context_appendices.md` | 639 | "only ~$871,000 of it is anonymous share money …" runs the retracted leg | retracted; residual identity UNKNOWN | same |
| IR-06 | 8 | `CORRECTIONS.md` | 57–69 | COR-03 section carries no supersession marker; `:66` action still commands the reversed rule | `[SUPERSEDED BY COR-12]` banner at the heading + in-place marker on the action line | a corrections register must mark its own retracted entry in place (file rule at `:8–11`) |
| IR-07 | 8 | `CORRECTIONS.md` | 194 | COR-11.2 routes "see COR-03" with no mention of COR-12 | routes to COR-03 **as superseded by COR-12** | every reference to a superseded correction must point at its superseder |
| IR-08 | 8 | `_parts/s1_p3b_H_addendum.md` | 131 | "already in §B/§J/§R **with COR-03's phrasing**" describes retracted phrasing as current | marked as COR-03's phrasing *as superseded by COR-12*, current phrasing stated | parts are volumes of one document (`00_METHOD_AND_STYLE.md:187`) |
| IR-09 | 9 | `stage_1.md` | 16–17 | "the original S-1's 1996-01-01 phrasing as **independent corroboration**" | demoted to version/lineage evidence within one registration statement (method §3) | header contradicts the ruling at `:35–47`; S-1 original + its amendments = one source |
| IR-10 | 9 | `stage_1.md` | 1139 | §R: "is **independent corroboration** of the same population" + source cell "corroboration" | demoted to same-lineage restatement | same, in the most re-read cell |
| IR-11 | 9 | `stage_1.md` | 870 | §P42 "which **corroborates** the count" | re-worded to same-lineage restatement that adds no corroboration | same rule |
| IR-12 | 9 | `quantitative.csv` | 74 | source "(**corroborated by** S-1 (orig.), Risk Factors)" | "(same lineage as S0801; restatement, not corroboration)" | register must not credit the ancestor with corroborating its own amendments |
| IR-13 | 9 | `context_appendices.md` | 595 | "**corroboration of the same population** at the 1995/96 turn" | demoted to same-lineage restatement | appendix is what downstream passes mine |
| IR-14 | 9 | `CORRECTIONS.md` | 241–242 | COR-12 rule instructs "added as **corroboration**" | rule restated: added as same-lineage version evidence, never a corroboration count | this instruction generated sites 9-13; unfixed it regenerates |
| IR-15 | 9 | `stage_1.md` | 1204 | §T row S-1/A No. 3: no lineage note | add `same lineage as S0801` demotion | §T preamble exists to stop double-counting |
| IR-16 | 9 | `stage_1.md` | 1205 | §T row 10-K405: "Largely repeats" only | add explicit same-lineage demotion | same |
| IR-17 | 9 | `stage_1.md` | 1206 | §T row 424B1: no lineage note; stale "restoration pending" | add same-lineage demotion; status updated to the on-disk file | 424B1 is on disk (`sources/424B1_final-prospectus…txt`) |
| IR-18 | 9 | `stage_1_claim_records.md` | 383 (K04), 397 (L01), 454 (P01) | `Corroboration: 3 / 4 / 3` — escaped the `count == 2` re-key | re-keyed to defensible counts with lineage members excluded and reason recorded | §3: exhibits to the same accession, 424B1, 10-K405 are one lineage |
| IR-19 | 12 | `CORRECTIONS.md` (+ report) | A-B1 sites | A-B1 still lands | closed from local evidence where closed-able (the A-B1 site list is exactly items 9/13's sites → IR-09…IR-18); any limb not closable locally named as UNKNOWN | no softened wording; if a retrieval were needed I report rather than fetch |
| IR-20 | 13 | `stage_1.md` | 36 | "four sites that contradicted it are corrected below" | states what was actually done, enumerating the now-completed sites | false closure assertion introduced by the repair |
| IR-21 | 13 | `stage_1.md` | 2218–2231 | pointer census omits `timeline.csv` while asserting completeness | census restated to include `timeline.csv` after IR-24/25 | same failure class: sweep scoped to the file open |
| IR-22 | 13 | `conflicts.csv` | 9 | "the canonical spine is fixed at **U.1–U.42**" | U.1–U.43 | stale claim created when U.43 was appended |
| IR-23 | 13 | `stage_1.md` | 1526 | same stale "U.1–U.42" | U.1–U.43 | same |
| IR-24 | residual | `stage_1.md` | 1251 | "**42 canonical conflicts, U.1–U.42.**" | 43, U.1–U.43 | §U preamble count is stale against 43 blocks |
| IR-25 | residual | `quantitative.csv` | 34 | printed addends sum to 295,567.90 but string shows =295,567.89 | string shows unrounded addends alongside printed ones so it is re-runnable | `derived_arithmetic` must be re-runnable from what is printed |
| IR-26 | residual | `stage_1.md` | 925 | same 1-cent string at §P.2 d7 | same fix, mirrored | item 10's single mismatch |
| IR-27 | residual | `timeline.csv` | 33 | `conflict_ref` U.16 on the NCSA-listing row (U.43's subject) | U.43 | mis-keyed; row restates U.43 CLAIM B verbatim |
| IR-28 | residual | `timeline.csv` | 55 | `conflict_ref` U.16 on the Associates row (U.41's subject) | U.41 | mis-keyed; note is U.41's subject verbatim |

## Out-of-scope findings recorded here for the sheet owner (paths I may not edit)

- `03_quality_control/amazon_s1_numeric_closure_final.md:29` — "Sweep … **0**" is false; `_parts/s1_p4.md:102–103`
  is a live instance (its own R-4 at `:42` already says so). Needs correction by addition.
- `03_quality_control/amazon_s1_numeric_closure_final.md:17` — "no live value cell carries either" is false;
  `context_appendices.md:596` carried one. Needs correction by addition.
- `03_quality_control/amazon_s1_causal_lineage_closure.md:37` / `:86` — marker census reported as a site audit
  ("all 31 named sites demoted"). Needs correction by addition.
- `03_quality_control/amazon_s1_audit4_audit5_final.md:409` / `:431` — A-B1 status line.

## Log

(empty until edits begin)
