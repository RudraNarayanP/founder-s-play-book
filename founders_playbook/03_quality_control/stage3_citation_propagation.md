# Stage-3 citation-key propagation — log and dispositions

Owner: the citation-propagation pass (Stage 3, `company_001_amazon`). Date: 2026-09-25.
Authority used: `03_quality_control/stage3_sourceid_rekey_map.md` (dossier + old id -> canonical id), read
against `sources.csv` (83 canonical rows, `S30001`-`S30083`) and against the **already-applied register rows**
the binding pass wrote on 2026-09-25 (`timeline.csv` rows 230-264, `validation.csv` 54-60, `failures.csv`
61-62, `decisions.csv` 27-30, `channels.csv` 25-26), which carry the canonical id the binding pass chose for
each re-emitted row **by content**. Registers were read, never written.

## Measurement command (run before and after)

```
cd "E:\founder's playbook/founders_playbook/01_companies/company_001_amazon"
grep -rInoP '\bS3[0-9]{3}\b' --include='*.md' . | cut -d: -f1 | sort | uniq -c | sort -rn
```

`\b...\b` is load-bearing: without it the pattern also matches the first four characters of every canonical
`S300nn` id (`S30001` -> `S3000`) and the count is meaningless. The brief's no-boundary measurement returned
153/124/113/105... for the CSVs; bounded, it returns the numbers below.

## Measured sites (differ from the brief — the brief's counts are DISTINCT old ids per file, mine are occurrences)

| File | brief (distinct ids) | measured lines | measured tokens |
|---|---|---|---|
| `research/ST3_A_chronology_org.md` | 37 | 72 | 81 |
| `research/ST3_B_finance.md` | 22 | 106 | 113 |
| `research/ST3_C_product_market.md` | 20 | 62 | 63 |
| `research/ST3_D_tech_ops.md` | 2 | 1 | 2 |
| `stage_3_pending_registers.md` | 18 | 51 | 57 |
| `stage_3_claim_records.md` | 3 | 2 | 3 |
| `stage_3_claim_records_part_2.md` | 3 | 2 | 4 |
| `stage_3_part_1.md` | (not listed) | 0 | 0 |
| `stage_3_part_2.md` | 4 | 1 | 4 |
| `stage_3_part_3.md` | 3 | 2 | 5 |
| `_parts/s3_p3.md` | 4 | 1 | 4 |
| `_parts/s3_p4.md` | 20 | 48 | 54 |
| `stage_3_index.md` | 2 | 1 | 2 |
| **in scope** | **138** | **349** | **392** |

Distinct-id counts reproduce the brief exactly (A S3001-S3037 = 37; B S3001-S3022 = 22; C S3001-S3020 = 20;
D S3001+S3020 = 2; pending = 18; s3_p4 = 20; etc.), so the 138 and the 392 describe the same defect at two
different resolutions. All 392 occurrences are dispositioned below.

## Three classes of site, not two

1. **Citation** — the token stands for a document. Re-pointed to canonical.
2. **Retired-scheme reference (meta)** — the token names the *pre-re-key key space itself* ("the colliding
   `S3001-S3022` sequences", "81 Stage-3 rows already exist, `S3001-S3081`", "ST3_C reserves S3001-S3020",
   "`source_id` values `S3001`+ continue the register"). Re-pointing any of these makes the sentence false.
   Left verbatim, marked `[RETIRED-KEY REFERENCE — ...]`.
3. **Held** — two or more candidate documents still fit, or the cited row was never written. Left verbatim,
   marked `[UNRESOLVED — candidates ...; missing fact: ...]`.

Classes 2 and 3 are the fourth and fifth exclusions the brief's list did not anticipate; both are *marked*
in place, so the final measurement is still a clean zero-unmarked claim. No token is silently left behind.

## Dispositions

### `research/ST3_A_chronology_org.md` — dossier ST3_A, 81 tokens
- 72 tokens RESOLVED. Map pairing `(ST3_A, S300n) -> S3000n` for n = 1..30, applied to every occurrence in
  the file: narrative citations, `sources.csv` append-block row keys (lines 946-975, whose field 1 is the
  row's own key) and `timeline.csv` append-block `source_id` cells (lines 830-862). Cross-checked: each
  re-keyed row key matches the `sources.csv` row that carries its own claim field.
- `S3031` (line 863, $2bn universal shelf, Form S-3 File No. 333-78797) RESOLVED -> **`S30045`**. No map row
  pairs dossier A with S3031; resolution is by content and the file number is unique in `sources.csv`
  (only `S30045` carries 333-78797), and the binding pass wrote the same event to `timeline.csv` row 253 as
  `S30045`. A's timeline block ran past its own 30-row source block; these are allocation errors, not drift.
- 8 tokens HELD (lines 864-871, `S3032` x1, `S3033` x2, `S3034` x2, `S3035` x1, `S3036` x1, `S3037` x1), all
  likewise outside A's map block:
  - `S3032` (Accept.com/Alexa mergers + both equity plans registered on Form S-8 1999-06-11) — candidates
    `S30024` (A's 8-K set 1999-06-08/09) / `S30079` (the S-8 set 333-78651...). Missing fact: whether the row
    is cited for the completion dates or for the plan registrations.
  - `S3033`-`S3035` (Galli offer letter EX-10.1; Nevada "opened" sentence; Q2-1999 net sales) — the Q2-1999
    10-Q accession 0000891020-99-001426 is registered **twice**, at `S30010` (A) and `S30064` (C). Missing
    fact: which duplicate the register treats as canonical for that accession.
  - `S3036`-`S3037` (zShops/Payments/Jenson; five DCs YTD) — the Q3-1999 10-Q accession 0000891020-99-001938
    is registered **four times** (`S30011`, `S30043`, `S30065`, `S30076`). Missing fact: same, and for S3037
    whether the FY1999 10-K (`S30075`) is the carrier rather than the 10-Q.

### `research/ST3_B_finance.md` — dossier ST3_B, 113 tokens
- 110 RESOLVED. Map pairing `(ST3_B, S300n) -> S300(30+n)`: S3001->S30031 ... S3022->S30052. Verified against
  the file's own `sources.csv` append block (line 1344 onward) row by row.
- Line 1335 (`source_id` values `S3001`+ continue the register ... ) and line 1515
  (`sources.csv` append rows proposed (S3001-S3022) | **22**) are class 2 — they describe the retired
  allocation. Excluded from the re-key, marked. **This is why no file-wide blanket alias was used.**

### `research/ST3_C_product_market.md` — dossier ST3_C, 63 tokens
- 60 RESOLVED. Map pairing `(ST3_C, ...)`: S3001->S30053, S3002->S30054, S3003->S30055, S3004->S30056,
  S3005->S30057, S3006->S30058, S3008->S30059, S3009->S30060, S3010->S30061, S3011->S30062, S3012->S30063,
  S3013->S30064, S3014->S30065, S3015->S30066, S3016->S30067, S3017->S30068, S3018->S30069, S3019->S30070,
  S3020->S30071; plus **`S3007` -> `S30051`** on the five citing lines (541, 542, 561, 628, 629).
  `S3007` has no map row: the map's ST3_C block skips it, and `sources.csv` holds 19 C rows (30+22+19+10+2=83),
  so C's S3007 row was the **held** sources.csv row (19 fields, comma in the `url` cell - see
  `stage3_register_merge_held_rows.md` row 8 and `stage_3_claim_records.md` S52). Resolution is by content:
  the accession C named for S3007, 0000891020-98-001498 / event 1998-10-28 (Q3-1998 results release), occurs
  under **exactly one** canonical row - `S30051` - and the binding pass resolved the same 1998-10-28 event to
  `S30051` independently (`timeline.csv` 241).
- Line 609 HELD (1 token): C's own `sources.csv` append row, keyed `S3007`. Re-keying the *row's own key*
  would assert that a row `S30051` with C's fields exists; it does not (that row is B's, 18 fields, different
  claim text). Marked.
- Line 496 (class 2, "This file reserves **S3001-S3020** for its own source rows") marked, not re-pointed.

### `research/ST3_D_tech_ops.md` — 2 tokens, both class 1? No - class 2
- Line 464 only: "ST3_C OC-10 reserves S3001-S3020 for itself". D claimed **no** `S30xx` block (it used
  `S3D-nnn`, which the map pairs to `S30072`-`S30081`); the sentence is about C's retired reservation. Marked
  class 2. D's `S3D-nnn` keys are **not** in this defect class (3-digit-after-`S3`) and are not touched; see
  the register-side note on them below.

### `stage_3_pending_registers.md` (57) and `_parts/s3_p4.md` (54) — the same blocks
`stage_3_pending_registers.md` line 15: the register blocks were "cut out of `_parts/s3_p4.md` at merge".
Every register row here is a **re-emission** whose `source_id` was a bare old id resolved *by the row's own
subject, date and named document* — and for these rows the binding pass recorded its resolution in the
register on 2026-09-25. Where the applied register carries the row, the canonical id in that applied row is
used (identical date + identical event string). Where it does not, the row is held.
Line numbers: pending 110-142 == s3_p4 1814-1846; pending 150 == s3_p4 1852; pending 179-181 == s3_p4
1877-1879; pending 187-191 == s3_p4 1883-1887; pending 199-203 == s3_p4 1893-1897; pending 209-210 == s3_p4
1901-1902. s3_p4 additionally carries 599, 617, 1740.

timeline block, per line (pending -> s3_p4 -> canonical, `timeline.csv` anchor row):
110/1814 S3004->`S30004`(230) · 111/1815 S3001->`S30005`(231) · 112/1816 S3002->`S30005`(232) ·
113/1817 S3018->`S30006`(233) · 114/1818 S3021->`S30021`(234) · 115/1819 S3001->`S30009`(235) ·
116/1820 S3005->`S30057`(236) · 117/1821 S3022->`S30022`(237) · 118/1822 S3023->`S30023`(238) ·
119/1823 S3009->`S30039`(239) · 120/1824 S3002->`S30009`(240) · 121/1825 S3021->`S30051`(241) ·
123/1827 S3003->`S30033`(243) · 124/1828 S3002->`S30009`(244) · 125/1829 S3002->`S30009`(245) ·
126/1830 S3021->`S30051`(246) · 127/1831 S3003->`S30033`(247) · 128/1832 S3019->`S30019`(248) ·
129/1833 S3010->`S30020`(249) · 130/1834 S3016->`S30016`(250) · 132/1836 S3018->`S30018`(252) ·
133/1837 S3015->`S30045`(253) · 134/1838 S3024->`S30024`(254) · 135/1839 S3013->`S30011`(255) ·
137/1841 S3010->`S30010`(257) · 138/1842 S3016->`S30016`(258) · 139/1843 S3013->`S30011`(259) ·
140/1844 S3013->`S30011`(260) · 141/1845 S3013->`S30011`(261) ·
142/1846 S3004 **HELD** — the applied row 262 binds TWO ids (`S30011; S30075`, per pending line 147); one
token cannot carry two citations and inventing the second would be adding a citation, not re-keying one.
Note lines 114, 129, 137, 141 etc. prove the same old token resolves differently line by line inside one file
(`S3010` -> `S30020` at 129 but -> `S30010` at 137; `S3021` -> `S30021` at 114 but -> `S30051` at 121), which
is why every one of these is a line-addressed substitution.

failures block: 179/1877 S3023->`S30023` (`failures.csv` 61) · 180/1878 S3020->`S30020` (`failures.csv` 62) ·
181/1879 S3001 **HELD** — this is `failures.csv` block row 8, the row the binding pass refused to write
(three candidates; a corpus-wide null no single filing carries).

validation block (anchor `validation.csv` 54-58 by subject): 187/1883 S3001->`S30005` · 188/1884 S3009->
`S30039` · 189/1885 S3003->`S30033` · 190/1886 S3011->`S30019` · 191/1887 S3013->`S30011`.

decisions block (anchor `decisions.csv` 27-30 by `D-n` and subject): 199/1893 S3004->`S30004` ·
200/1894 S3018->`S30006` · 202/1896 S3020->`S30020` · 203/1897 S3013->`S30011`. (201/1895 = D-3, held row 3,
cites `S3P-002` not a bare id - untouched.)

channels block (anchor `channels.csv` 25-26, whose cells the binding pass re-bound and whose row names
10-K405/97, 10-K/98, 10-K/99): 209/1901 S3001->`S30005`, S3002->`S30009` · 210/1902 S3011->`S30011`.
The `S3D-004` cell in both rows is a different key family; left, reported below.

class-2 lines: pending 8, 10, 15, 32, 147, 150 (inside the S3P-001 row's own note), 184; s3_p4 617, 1740,
1852. class-3 line: s3_p4 599 (= `stage_3_part_3.md` 613) - the §S.9 table row reproducing C's unwritten
`S3007` sources row; same disposition as ST3_C line 609.

### `stage_3_claim_records.md` (3), `stage_3_claim_records_part_2.md` (4), `stage_3_part_3.md` (5),
`stage_3_part_2.md` (4), `_parts/s3_p3.md` (4), `stage_3_index.md` (2)
- claim_records 1524 (`S3007 exists in sources.csv already`) **HELD** as C's unwritten row, same as above;
  1533 (`81 Stage-3 rows already exist, S3001…S3081`) class 2.
- claim_records_part_2 244, 248 class 2 (both quote the retired collision and §T's retired range).
- stage_3_part_3 613 **HELD** (held sources-row table); 631 class 2.
- stage_3_part_2 907 and `_parts/s3_p3` 894 (same sentence, both files) **HELD**: "this part cites those IDs
  (... and source_ids S3001, S3012, S3013, S3020) and redefines none of them". The four exemplars sit in a
  list that names no document, date or line anchor, and both volumes contain **no other** `S3` id anywhere
  (measured: these 4 tokens are their entire S3 inventory), so the writing dossier cannot be recovered from
  the file. Candidate blocks: `(ST3_A, ...)` -> `S30001/S30012/S30013/S30020`; `(ST3_B, ...)` ->
  `S30031/S30042/S30043/S30050`; `(ST3_C, ...)` -> `S30053/S30063/S30064/S30071`. Missing fact: which
  dossier's block §K-§O drew its exemplar ids from.
- stage_3_index 19 class 2.

Totals, and they foot to the 392 measured occurrences: **329 re-pointed** (A 73, B 110, C 60, pending 43,
s3_p4 43), **28 held class-3** (A 8, C 1, pending 2, s3_p4 5, claim_records 1, part_3 3, part_2 4, s3_p3 4),
**35 class-2** (B 3, C 2, D 2, pending 12, s3_p4 6, claim_records 2, claim_records_part_2 4, part_3 2,
index 2). `stage_3_part_1.md` carried zero sites. 349 physical lines changed, no line added or removed, no
field width disturbed, no invented id (proof below).

## Register-side check — read-only, reported, NOT fixed

Every `*.csv` was opened for reading only; `git status` confirms no register is modified.

| Register | rows with a retired id in a **reference field** | where |
|---|---|---|
| `sources.csv` | **0** | all 83 `source_id` keys are canonical — the key column is clean |
| `timeline.csv` | **88** | rows 126-214: ST3_A's block (126-168, incl. the never-allocated `S3031`-`S3037`), ST3_B's (169-191), ST3_C's (192-214). The binding pass's own re-emitted block, rows 230-264, is canonical |
| `quantitative.csv` | **59** | rows 226-288, ST3_B's block, `source` column |
| `validation.csv` | **6** | rows 42-47, ST3_C's block, `source_id` column |
| `failures.csv` | **4** | rows 48-51 |
| `conflicts.csv` / `decisions.csv` / `channels.csv` / `data_gaps.csv` | **0** | clean |

**157 register rows carry a reference field that resolves to nothing.** Two further kinds of retired-key
residue sit in reference/note text rather than in a key column: 11 `sources.csv` rows name a retired id in
their `independence_note`/`notes` cross-reference (rows 118, 123, 125, 126, 128, 130, 136, 144, 147, 148,
153 — e.g. `S30003`: "Same accession as S3004"), and 3 rows still cross-reference the `S3D-nnn` family
(`S30081`: "see S3D-004"). `sources.csv` row 197 (`S30082`) mentions `S3001-S3022` deliberately, as history.

**Integrity finding reported, not repaired:** `stage_3_pending_registers.md` line 107 asserts that
`quantitative.csv` was applied with "every `source` reference bound to canonical ids", and line 196 makes the
same claim for `validation.csv`; the two files carry 59 and 6 retired-form references respectively. The
sentences are prose, not citation tokens, so this pass leaves them verbatim and reports them.

**Out of this defect class but adjacent to it:** the editable texts still carry the *other* two retired
families — `S3D-nnn` (ST3_D 11, pending 9, s3_p4 9) and `S3P-nnn` (pending 17, s3_p4 10). Neither is a
3-digit-after-`S3` token, and the binding table pairs them (`S3D-004`->`S30075`, `S3D-006`->`S30077`,
`S3P-001`->`S30082`, `S3P-002`->`S30083`), so a follow-up pass can propagate them by the same method.

**Bare retired tokens left in files this pass may not edit** (read-only): `03_quality_control/stage3_register_binding.md`
46 (its own `retired -> canonical` decision table — class (a) by nature), `MASTER_RESEARCH_LOG.md` 2
(RD-066/RD-075/RD-083, the records of this defect), `00_METHOD_AND_STYLE.md` 1,
`03_quality_control/stage3_register_merge_held_rows.md` 1 (the held row quoted verbatim). Excluded as
always: the re-key map's old-id column, `03_quality_control/abandoned/`, and this sheet.

## Independent confirmation of the 43 register-row resolutions

Two checks, both from records this pass did not write: (i) each of the 30 timeline rows re-points to the
canonical id already present in `timeline.csv` rows 230-261 for the identical date + identical event string;
(ii) every resolution agrees row-for-row with `03_quality_control/stage3_register_binding.md`'s decision
table — including row 33 (1999-11 launches), which that table itself records as `S30011; S30075` with the
note "two ids, citation falsified as written", which is exactly why this pass held it rather than picking
one, and the two held rows (`failures.csv` 8, `decisions.csv` 3).

## FINAL MEASUREMENT (after)

```
$ grep -rInoP '\bS3[0-9]{3}\b' --include='*.md' . | cut -d: -f1 | sort | uniq -c | sort -rn
    118 ./founders_playbook/03_quality_control/stage3_citation_propagation.md   <- this sheet (documents both sides of every pair)
     76 ./founders_playbook/03_quality_control/stage3_sourceid_rekey_map.md     <- exclusion (a): old-id column
     52 ./founders_playbook/03_quality_control/stage3_register_binding.md       <- read-only: binding decision table
     14 ./founders_playbook/01_companies/company_001_amazon/stage_3_pending_registers.md   <- all on marked lines
     12 .../company_001_amazon/_parts/s3_p4.md                                  <- all on marked lines
      8 .../company_001_amazon/research/ST3_A_chronology_org.md                  <- all on marked lines
      6 .../company_001_amazon/stage_3_part_3.md                                 <- all on marked lines
      5 ./founders_playbook/MASTER_RESEARCH_LOG.md                               <- read-only defect records
      4 .../stage_3_part_2.md, stage_3_claim_records.md, …_part_2.md,
          research/ST3_C_product_market.md, _parts/s3_p3.md                     <- all on marked lines
      3 .../research/ST3_B_finance.md                                            <- all on marked lines
      2 .../stage_3_index.md, research/ST3_D_tech_ops.md                         <- all on marked lines
      1 ./founders_playbook/03_quality_control/stage3_register_merge_held_rows.md
      1 ./founders_playbook/00_METHOD_AND_STYLE.md

$ grep -rIP '\bS3[0-9]{3}\b' --include='*.md' company_001_amazon | grep -vcP 'UNRESOLVED|RETIRED-KEY'
0
```

**Zero unmarked bare tokens in every file this pass owns** (349 lines changed; `stage_3_part_1.md` needed
nothing). The 61 tokens remaining in *editable* files all sit on a line carrying either
`[UNRESOLVED — candidates …; missing fact: …]` or `[RETIRED-KEY REFERENCE — …]`, and a marked line may
legitimately restate the retired id inside its own marker text.

Machine proof that nothing but keys moved (git baseline vs disk): 349 changed lines, **0** line-count
changes, **0** field-width (comma-count) changes, **0** non-token text changes, **0** invented ids — every
new id tested against the 83 `source_id` values in `sources.csv`.

**Marker placement.** On the three sites that are markdown **table rows** (`stage_3_part_3.md` 613,
`_parts/s3_p4.md` 599, `research/ST3_B_finance.md` 1515) the marker was first appended after the row's
closing pipe, which would have added a phantom column; it was moved inside the last cell, so each row still
ends `… [marker] |`. Verified against the git baseline: on those three lines the only difference beyond the
marker itself is one space before the trailing pipe. Every other marked site is a CSV append row or a prose
line, where the marker sits at end of line and adds no comma, so no register width moves.

**Register-row resolutions are not this pass's opinion.** All 43 per-line resolutions in
`stage_3_pending_registers.md` / `_parts/s3_p4.md` were taken from the documents named in the citing row and
then cross-checked twice: against the canonical id already sitting in the applied register row for the
identical date + identical event string, and against the binding pass's own decision table in
`03_quality_control/stage3_register_binding.md`. Both agree row for row, including the two rows that pass
refused (its row 33 = "S30011; S30075 — two ids, citation falsified as written", its row 8 = HELD) — which
are the two this pass holds.

