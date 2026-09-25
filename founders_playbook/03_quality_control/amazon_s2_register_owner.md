# AMAZON.COM STAGE 2 — REGISTER-OWNER REPORT (run 6 hand-off items)

Sheet: `03_quality_control/amazon_s2_register_owner.md` · Executor: **register owner** (holds the nine
`company_001_amazon/*.csv`) · Date 2026-09-25 · **Web requests: 0.**

Authority read in order: `amazon_s2_audit4_repairs.md` §6/§7 ("For the register owner"), then the two audits it
repaired from (`amazon_s2_audit4_hindsight.md`, `amazon_s2_audit5_adversarial.md`) for wording, then
`stage3_register_binding.md` for the current register conventions, then `00_METHOD_AND_STYLE.md` §13 (schemas,
append-only, "source_id … is never redefined"). Register-side evidence for every row below was read off
`stage_2_part_3.md` §T/§U and the source files themselves, not from an audit sheet's paraphrase.

**Log discipline:** written in full **before the first register edit**; outcomes appended as work completes.
Status tokens: `APPLIED` / `PARTIAL` / `HELD`.

## 0. Baselines measured at open (all nine registers)

| Register | header width | data rows | uniform width |
|---|---|---|---|
| channels.csv | 11 | 25 | yes |
| conflicts.csv | 15 | **168** (stage1 43 · stage2 70 · stage3 55) | yes |
| data_gaps.csv | 8 | 100 (stage1 23 · stage2 23 · stage3 54) | yes |
| decisions.csv | 15 | 29 | yes |
| failures.csv | 11 | 61 | yes |
| quantitative.csv | 12 | 381 | yes |
| sources.csv | 18 | 197 (stage1 102 · stage2 12 · stage3 83) | yes |
| timeline.csv | 11 | 263 (stage1 49 · stage2 67 · stage3 139 · stage2-consequence 8) | yes |
| validation.csv | 11 | 59 | yes |

`conflicts.csv` duplicate-key test on `conflict_id`: **0 duplicates**, ids `U.1 … U.168` contiguous.

## 1. ITEM 1 — U.114 / U.115: **HELD, twice over. Do not apply as written.**

Two independent blockers, both measured from disk:

1. **The ids are occupied by Stage 3, bound and cited.** `conflicts.csv` rows `U.114` and `U.115` already exist
   with `stage = stage3`: `U.114` = "The five 1999-03-11 'Sales Agreements' are not the marketplace's contractual
   trace" (`stage_3_part_3.md` l.683) and `U.115` = "The 1998 proxy officer roster: five names, four dates, and a
   cache that paired them one-to-one" (l.704). `stage_3_claim_records.md` l.27/l.34/l.136 declare the Stage-3
   conflict spine **U.114 → U.168 (55 blocks)**, and `stage3_register_binding.md` §2 bound 16 Stage-3 conflicts
   rows onto those ids. Writing a Stage-2 row at `U.114`/`U.115` would either create a duplicate key or overwrite a
   bound Stage-3 row — the §9.3 failure this brief forbids.
2. **The rows the log says to apply are not on disk.** `stage_2_part_3.md` §U ends at **U.113** (l.1725):
   `grep -c '^\*\*U\.[0-9]*'` = **70**, ids U.44–U.113, and the file contains **no `>>> CSV APPEND BLOCK`
   section and no `RESERVED` marker**. So the repair log's §7 invariant claim ("Spine now emits **72** … U.114 and
   U.115 appended with their `>>> CSV APPEND BLOCK: conflicts.csv` rows at the foot of §T→§U, marked RESERVED")
   is **not reproducible on disk**. `stage_2_index.md` l.41 repeats it ("volume 2 carries **72** conflict records
   (**U.44–U.115**)"). There is therefore **no row text to apply**: composing it would mean inventing claim_a/claim_b
   fields the Stage-2 volume never emitted, against ids Stage 3 owns.

**Consequence for the parity claim.** The spine's §U block count as measured is **70**, against **70** Stage-2
`conflicts.csv` rows: **the 70↔70 invariant is intact and there is no 72↔72 state to restore.** The declared
"excess … in three places" is a claim about the narrative, and the narrative on disk contradicts it.

**Proposed resolution (orchestrator's call; I have no authority over `stage_2_part_3.md`):**
- (a) *Preferred* — the Stage-2 volume re-labels its two reserved blocks to ids that are free and unambiguous
  (**U.113a / U.113b**, keeping the letter-suffix precedent already used by the **U.111a** addendum in
  `stage_2_claim_records_part_2.md` l.190), then the register owner appends rows with those ids and
  `stage = stage2`. Nothing existing is renumbered; 70↔70 becomes 72↔72 on both sides.
- (b) Alternatively, next free canonical ids **U.169 / U.170** — but that puts Stage-2 rows *behind* Stage 3 in
  the spine and invites a later pass to "reconcile" them, so it is worse than (a).
- (c) Either way `stage_2_index.md` l.39–41 and the part_3 preamble must be corrected to the ids actually used,
  and the Stage-2 block text must be emitted before any register row exists. **I did not write U.114/U.115.**

## 2. ITEM 2 — `sources.csv` S0807–S0812 + S0804's stale bar: **APPLIED** (S0804 with the reservation in 2.1)

Ids re-verified free before writing: `sources.csv` holds **S0801–S0806** only in that family; S0807–S0812 absent
(measured, §0 dump). Six new rows, `stage = stage2` (registered by Stage 2's §T; the stage literal matches the 12
existing `stage2` source rows). All fields populated from `stage_2_part_3.md` §T rows l.287–l.296 and the provenance
headers of the six files, measured this pass: No. 1 `…603` 438,685 B / body 436,103 B, access 2026-09-25; No. 2
`…659` 405,557 B / 403,334 B; No. 4 `…822` 312,174 B / 309,865 B; No. 6 `…847` 303,840 B / 301,661 B; FY1998 10-K
`…99-000375` 321,454 B / 319,591 B; FY1999 10-K `…00-000622` 307,278 B, **no provenance header** (raw SEC header,
`FILED AS OF DATE 20000329`), so its access date is recorded as the read date with the retrieval-date question
flagged for the orchestrator (repair log §7.1 item 10). `independence_note` carries the lineage per method §13 /
§T's Lineage column — the four amendments are states of **L-97/333-23795** (S0801) and are NOT independent; the two
later 10-Ks are separate reporting instruments of the same issuer, independent of the registration statement but
derivative of S0805's audited content, and neither is independent corroboration of the other's FY1996 column.

### 2.1 S0804 re-key — mechanism is genuinely ambiguous; I took the conservative branch
U.110 says the re-key goes into "**a new Stage-2 row rather than editing Stage 1's row**"; the repair log §7.1
item 4 says "**re-key S0804's stale bar**" and names no id for a new row. Minting `S0813` would invent a key the
log does not authorise, and `source_id` "is never redefined" (method §13), so a new row could not remove the bar
that Stage-2 rows citing **S0804** inherit. Applied instead: an **additive annotation inside S0804's own `notes`
field** — the 2026-09-23 bar wording is retained verbatim in `source_title`, `evidence_class`, `confidence` and
`claim_supported` (nothing rewritten, so a retraction can still quote it), and the annotation records the
2026-09-24 retrieval (acc. `0000891020-97-000868`, 266,755 B file / 263,820 B body, header on disk) as
superseding, plus the held `S0813` option. Reported as PARTIAL, not silent.

## 3. ITEM 3 — annotate eight `conflicts.csv` rows: **APPLIED**

U.52, U.56, U.51, U.65, U.55, U.95, U.97, U.68. Each edit appends one clause to the row's own
`residual_uncertainty` field, prefixed `AUDIT-4/5 REPAIR 2026-09-25 (register owner):`, and rewrites nothing:
`claim_a`, `claim_b`, `why_they_differ`, `best_supported_interpretation`, `evidence_weight`, `confidence` and
`section` are byte-identical after the pass (asserted in the apply script). The log names **nine** rows
("annotate nine existing conflict rows", adding U.99/U.102 "no change sought" and U.112 "unchanged") — the eight
listed in my brief are the eight whose text the repair actually moves; U.99/U.102/U.112 get no edit because none is
sought. U.55's intended cross-list to **U.115** is recorded in the annotation as **HELD**, per §1, so the register
does not point at a Stage-3 row.

## 4. ITEM 4 — timeline / data gaps / quantitative / decisions / validation-failures

- **`timeline.csv`: APPLIED.** Three new `stage2` rows at the log's dates — 1997-04-21 (No. 1, first stated range),
  1997-05-13 (No. 4, upsize + $14–16 ceiling + competitor rewrite), 1997-05-14 (No. 6, the hedge) — keyed
  `source_id` S0807/S0809/S0810 and `conflict_ref` U.95 / U.97 / U.68 as each row's own subject. Rows 100, 101, 104,
  106, 107, 108 carry **additive `notes` corrections** (the "UNTRIED." contents flags, row 104's "FIRST STATED
  RANGE", row 107's upsize/range/rewrite attribution and its "obsolete on its own filing date" note, row 108's
  "filed that morning"), because the log item 6 says "correct any 1997-05-09 'first range' wording" and the same
  stale class is live at those rows. `event` text untouched everywhere.
- **`data_gaps.csv`: APPLIED, 2 rows, `stage2`.** (i) the FY1996 (+$469k) / FY1997 (+$3,430k) restatement
  reconciliation null; (ii) the "FY1998 10-K notes not read past Selected Financial Data → OPEN, not closed" null.
  The repair log's own correction (§7.2 item 1 / §4 item 1) is honoured **in the gap's text**: the $469k **foots**
  (+$464k inside total operating expense, $9,438k → $9,902k, +$5k interest expense; loss from operations moves
  $(5,979) → $(6,443), and L-2's "byte-identical" premise covers only net sales, cost of sales and gross profit),
  so the movement is **explained in composition but unreconciled as to authority**. `amazon_s2_audit5_adversarial.md`
  L-2 (l.109–116) still says "the $469k sits entirely below the operating line" and mis-sources 2,401 / 1,411 to
  "the FY1997 10-K405 (l.1182–1184)"; **the audit sheet was not edited** — the discrepancy is recorded in
  `follow_up_task`, with the line numbers measured this pass. Also cross-referenced: Stage 3's own gap row
  (`data_gaps.csv` l.93) already carries the FY1997 (27590)→(31020) pair and closes it with "**None available**";
  the new rows say that closure is premature on the same evidence (§4 item 6 of the repair log).
- **`quantitative.csv`: HELD, no rows added.** The log's own instruction (item 5) is that the restatement pairs are
  "alternate bases on existing metrics, **not new rows**", and §7's invariant holds `derived_arithmetic` untouched
  on every DERIVED row. The decomposition therefore lives in the annotated U.55 row, the new sources rows and the
  new gap rows, not in a new §P value. No as-filed row altered. Delta 0.
- **`decisions.csv`: APPLIED as two additive `notes` annotations** on row 20 (1997-03 price-aggressive) and row 21
  (syndicate/deal shape), mirroring §N's two changes — the availability inversion (a March decision cannot be
  informed by a May filing; C-16) and the `RETROSPECTIVE` label on the price-floor `actual_result` (C-10).
  `information_available` and `actual_result` cells are **not rewritten**, because they are the wording the repair
  struck and retractions quote. Row count delta 0.
- **`validation.csv` / `failures.csv` / `channels.csv`: no change sought** (log item 9). Delta 0.

## 5. Invariants I will measure after each write

Re-parse each file: data rows before → after, uniform width, zero duplicate keys (conflicts `conflict_id`,
sources `source_id`, and the natural composite for `timeline`/`data_gaps`). Then re-measure the three §U parities
(Stage 1 43↔43, Stage 2 70↔70, Stage 3 55↔55) against the narrative block counts on disk, as measured, loudly.

## 6. Outcomes (appended as work completed — register-owner pass closed)

### 6.1 Item dispositions
| Item | Status | What was written |
|---|---|---|
| 1 · reserved §U conflicts U.114 / U.115 | **HELD** (§1 above: ids bound to Stage 3 **and** the promised rows are not on disk) | nothing |
| 2 · `sources.csv` S0807–S0812 | **APPLIED** | 6 rows appended, `stage = stage2`, all 18 fields populated, ids re-verified free against the register before writing (only S0801–S0806 existed) |
| 2b · S0804 stale bar (U.110) | **PARTIAL** (§2.1) | additive annotation inside S0804's own `notes`; the 2026-09-23 bar wording retained verbatim in `source_title`, `claim_supported`, `evidence_class`, `confidence`; the "new Stage-2 row" mechanism HELD for want of an authorised id |
| 3 · eight `conflicts.csv` annotations | **APPLIED** | U.52, U.56, U.51, U.65, U.55, U.95, U.97, U.68 — one clause each, appended inside `residual_uncertainty` only |
| 4 · timeline | **APPLIED** | 3 new `stage2` rows (1997-04-21 / S0807, 1997-05-13 / S0809, 1997-05-14 / S0810) + 6 additive `notes` corrections (1997-04-21, 04-29, 05-09, 05-13, 05-14 No. 5, 05-14 IPO); no `event` text rewritten |
| 5 · data gaps | **APPLIED** | 2 new `stage2` rows: the FY1996 +$469k / FY1997 +$3,430k reconciliation null, and the "notes unread → OPEN, not closed" reading debt |
| 6 · quantitative | **HELD, by the log's own instruction** | 0 rows; the pairs are alternate bases on existing metrics, not new §P values, and no `derived_arithmetic` field was touched |
| 7 · decisions | **APPLIED** | the 1996-06-21 Series A row annotated in `information_available` (Q1 + PARTIAL Q2: Q2 closed 1996-06-30, nine days after the closing) and in `actual_result` (price floor labelled `RETROSPECTIVE`); 0 rows added |
| 8 · validation / failures / channels | **NO CHANGE SOUGHT** | 0 rows |

### 6.2 Measured proof, after writing
*Row counts (data rows) and width, re-parsed from disk:*

| Register | before → after | width | duplicate keys | newlines in fields |
|---|---|---|---|---|
| sources.csv | 197 → **203** (+6) | 18 uniform | 0 on `source_id` | 0 |
| conflicts.csv | 168 → **168** (+0, 8 annotated) | 15 uniform | 0 on `conflict_id` | 0 |
| timeline.csv | 263 → **266** (+3, 6 annotated) | 11 uniform | 0 on (date, event) | 0 |
| data_gaps.csv | 100 → **102** (+2) | 8 uniform | 0 on (stage, gap) | 0 |
| decisions.csv | 29 → **29** (+0, 1 row annotated in 2 fields) | 15 uniform | 0 on (date, decision) | 0 |
| quantitative.csv · channels.csv · failures.csv · validation.csv | **381 · 25 · 61 · 59, all unchanged** | uniform | byte-identical to HEAD | 0 |

*Append-only, proved mechanically:* every one of the nine registers was diffed field-by-field against `git HEAD`
(commit `08cacf6`). **Original rows compared: 1,283 across the nine files; reordered 0, deleted 0, rewritten 0** — each
touched field is the old string with a note appended after it (` - REPAIR-PASS NOTE (AUDIT-4/5 register owner,
2026-09-25…): …`), so the pre-repair wording is quotable by every retraction that depends on it. In
`conflicts.csv` the only field that moved on any row is `residual_uncertainty`, on exactly the eight named ids.
`quantitative.csv` re-checked independently: 91 DERIVED rows, **0** missing `derived_arithmetic`.

*§U parities, as measured on disk (count **and** id-set identity, not just totals):*

| Stage | narrative §U blocks | register rows | id sets identical |
|---|---|---|---|
| Stage 1 (`stage_1.md`) | **43** (U.1–U.43) | **43** | **yes** |
| Stage 2 (`stage_2_part_3.md`) | **70** (U.44–U.113) | **70** | **yes** |
| Stage 3 (`stage_3_part_3.md`) | **55** (U.114–U.168) | **55** | **yes** |

**My changes moved none of them** — because the repairs that would have moved them (item 1) are held, and every
edit else is inside existing rows or in registers the spine does not count.

### 6.3 Two things the next pass must not inherit silently
1. **The 72↔72 parity the repair log declares does not exist and is not needed.** `stage_2_part_3.md` emits **70**
   §U blocks ending at U.113; there is no `>>> CSV APPEND BLOCK: conflicts.csv`, no `RESERVED` marker, no U.114 or
   U.115 block anywhere in the Stage-2 volume. But the *claim* of 72 is now printed in `stage_2_index.md` l.39–41
   ("volume 2 carries **72** conflict records (**U.44–U.115**)", "U.114 and U.115 records appended 2026-09-25") and
   in the part_1 preamble. Those statements are false against the disk and are the kind of instruction-layer defect
   that a later agent "repairs" by inventing rows.
2. **Four live Stage-2 cross-references now point at a key that resolves to a different stage's finding:**
   `stage_2_part_2.md` l.759, `stage_2_part_3.md` l.202 and l.275 all cite **→ U.115** for the five-basis
   restatement, and `stage_2_index.md` cites U.114/U.115 as appended. In this register **U.115 is Stage 3's "1998
   proxy officer roster"** and **U.114 is the 1999-03-11 Sales Agreements**. A reader following the Stage-2 pointer
   lands on the wrong conflict. The finding itself is safe — it is carried in the annotated U.55 row and in
   S0811/S0812 — but the pointers must be re-keyed (proposal: **U.113a** for the price-walk re-key, **U.113b** for
   the restatement pair, on the precedent of the existing U.111a addendum) by whoever owns `stage_2_part_3.md`,
   after which the register owner appends the two rows with those ids and 70↔70 becomes 72↔72 on both sides.

### 6.4 Post-script, recorded because a repair can be the next defect
**One defect created by this pass and caught by re-parsing.** The register files do not share one line terminator:
`conflicts.csv` is **CRLF** throughout (169 lines) while the other eight registers are **LF**. Re-serialising the
eight annotated `conflicts.csv` rows emitted LF for those rows plus the header, so the file briefly carried 160
CRLF lines and 9 LF lines — invisible to any CSV parser (all counts, widths and keys still measured clean) but a
spurious whole-file diff for the next line-based sweep. Repaired by normalising the file back to uniform CRLF:
**the other 160 rows are byte-for-byte what they were**, and the HEAD comparison re-run after the fix still reports
**8 rows differing, every difference a pure append, moved fields: none**. `sources.csv`, `timeline.csv`,
`data_gaps.csv` and `decisions.csv` are LF before and after, so nothing was mixed there. **Method note for the next
pass: check the target register's existing terminator before re-writing any line; `csv.writer`'s default is
`\r\n` and `lineterminator='\n'` silently changes convention on whatever lines it touches.**

### 6.5 Files written by this pass
Five registers: `sources.csv`, `conflicts.csv`, `timeline.csv`, `data_gaps.csv`, `decisions.csv`; plus this sheet.
**Untouched:** `quantitative.csv`, `channels.csv`, `failures.csv`, `validation.csv` (verified byte-identical to
HEAD), and every non-CSV file — `stage_1.md`, `stage_2_part_*.md`, `stage_2_claim_records*.md`, `stage_2_index.md`,
`context_appendices.md`, `CORRECTIONS.md`, the Stage-3 volumes, `_parts/`, `research/`, `MASTER_RESEARCH_LOG.md`,
`RESUME_HANDOFF.md`, other companies. `amazon_s2_audit5_adversarial.md` was **not** edited although L-2's
"entirely below the operating line" is measured false; the discrepancy is recorded in the new gap's
`follow_up_task`. **Web requests: 0.** Helper scripts ran outside the repo and were deleted.

