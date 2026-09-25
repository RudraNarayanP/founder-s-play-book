# rd078_stale_token_repairs.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T19:05:39Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## Method

STATUS: WRITTEN 2026-09-25

Pass `rd078-stale-keys`, 2026-09-26. Write scope: the six Stage-3 narrative volumes named in the gate
output — `stage_3_claim_records.md`, `stage_3_claim_records_part_2.md`, `stage_3_index.md`,
`stage_3_part_2.md`, `stage_3_part_3.md`, `stage_3_pending_registers.md`. Web requests: **zero**. No
id was renumbered, allocated, deleted or moved by this pass.

Procedure, in order:

1. **Enumerate, do not trust the finding list.** `gates.py` reports a *set* of unresolvable tokens per
   file, capped at 15, and skips fenced blocks; the finding list is therefore not a site list. All
   occurrences were enumerated directly with `S3[0-9]{3}\b` (word-boundary-anchored, so `S30012` and
   `S3D-004` cannot match) and printed with their surrounding sentence. Result: **34 token occurrences
   on 20 lines** across the six files.
2. **Establish the arbiter.** `sources.csv` was read row-wise: 203 rows, `source_id` column holds
   **no** 4-digit `S3nnn` key, and the canonical block **S30001–S30083** is present, with `S30082`
   = "Amazon.com Form 10-K/A for the fiscal year ended December 31 1999" and `S30083` = "Amazon.com
   Forms 8-K events 1998-11-19 … and 1999-07-21". So every bare 4-digit token in a scanned narrative
   file resolves to nothing by construction, and any re-point must be justified document-by-document
   from `03_quality_control/stage3_sourceid_rekey_map.md` plus that row's content.
3. **Classify each site, never the token.** The three classes fixed by
   `03_quality_control/stage3_citation_propagation.md` §"Three classes of site" were applied per site:
   **1 citation** (token stands for a document — re-point it), **2 retired-scheme meta** (token names
   the pre-re-key key space itself — re-pointing makes the sentence false; leave verbatim),
   **3 held** (two or more documents still fit, or the cited row was never written — leave verbatim
   under a visible marker).
4. **Verify, then write.** Each occurrence's class was checked against the line's own words plus the
   map/`sources.csv` content, and this sheet records every site with its file, line, token, class and
   the evidence line it was judged from.

**Outcome: 0 re-pointed, all 34 occurrences left in place** — **22 occurrences on 15 lines** as
class-2 historical/meta references (retractions, supersession notes and range statements naming the
retired id space itself), and **12 occurrences on 5 lines** as class-3 holds. No site was found where
the token functions as a live citation of a determinable document; the 329 citation sites this task
descends from were re-pointed by the earlier propagation pass.
Every one of the 34 occurrences already carries a visible in-line disposition marker
(`[RETIRED-KEY REFERENCE — …]` or `[UNRESOLVED — …]`) — measured: **0 occurrences on an unmarked
line** — so this pass's contribution is the independent re-verification below, not new edits.

## Per-file resolutions

STATUS: WRITTEN 2026-09-25

**Class-1 (live citation of a determinable document) sites found: NONE — so 0 tokens re-pointed.**
What the gate flags in these six volumes is, site by site, a retired-scheme reference whose sentence
is *about* the old key space, or an already-held row. Re-pointing any line below would make the
sentence assert something that was never true. Each entry: file : line : tokens : class : judgment.

**`stage_3_claim_records.md`** (4 occurrences, 2 lines)
- L1533 `S3001`, `S3081` — class 2. The §T lead-in reads "`sources.csv` is global-append-only per
  company; 81 Stage-3 rows already exist, S3001…S3081" — a *range* naming the register's id space as
  it stood when §T was written. `sources.csv` now carries 83 canonical rows, `S30001`–`S30083`
  (measured this session; no 4-digit `S3nnn` key survives in it). Pointing the two endpoints at single
  documents would assert that two documents "already exist" instead of a block of rows. Left verbatim.
- L1524 `S3007` — class 3, see *Held-as-unresolved*.

**`stage_3_claim_records_part_2.md`** (4, 2 lines) — all class 2, no holds.
- L244 `S3001`, `S3022` — "four dossiers' `S3001…S3022` blocks over each other, so 22 ids each named
  three different documents; re-keyed to …" — restates the collision note at the head of
  `03_quality_control/stage3_sourceid_rekey_map.md`.
- L248 `S3001`, `S3081` — a *quotation* of another volume: "`stage_3_part_3.md` §T's '81 Stage-3 rows
  already exist, `S3001…S3081`' uses the [retired space]". Editing the quote would misquote §T.

**`stage_3_index.md`** (2, 1 line)
- L19 `S3001`, `S3022` — class 2: "colliding `S3001–S3022` source-id sequences from the earlier merge",
  listed as the defect the re-key closed. Index-level history, not a source pointer.

**`stage_3_part_2.md`** (4, 1 line) — class 3 hold, see *Held-as-unresolved*; no class-1 site.

**`stage_3_part_3.md`** (6, 2 lines)
- L631 `S3001`, `S3081` — class 2: §T's copy of the same 81-row range statement as claim_records L1533.
- L613 `S3007` ×4 — class 3, the §S.9 table row reproducing ST3_C's unwritten `sources.csv` row.

**`stage_3_pending_registers.md`** (14, 9 lines) — the volume with the most residual tokens and the
fewest possible repairs, because it is the *pending-block* volume: it prints both the pre-repair
diagnosis and the binding pass's application records.
- L8 `S3001`, `S3022` — class 2, and already carries the repair in the same breath: "Provisional
  `S3P-001`/`S3P-002` are re-keyed to canonical **S30082**/**S30083**; the S3001-S3022 collision …".
  `S30082` and `S30083` were confirmed present in `sources.csv` this session.
- L10 `S3001` — class 2: "`S3001`-style ids that no longer resolve" — the sentence's whole subject is
  that these keys are dead.
- L15 `S3001`, `S3022` — class 2, superseded diagnosis: "Applying them is blocked behind `RD-075` —
  `sources.csv` carries three colliding `S3001–S3022` sequences … Fix those first or every join on
  `source_id` resolves to the wrong document." The fix it demanded has since happened; the block is a
  historical record of the request, not an open instruction.
- L32 `S3001`, `S3022` — class 2: "three colliding `S3001…S3022` sequences — the same id meaning a
  different document in each dossier's block", the reason a fresh `S3P-` prefix was used.
- L148 `S3001`, `S3024` — class 2, application record: "Bare citations S3001-S3024 resolved by content,
  never by position; row 33 … bound to TWO ids (S30011; S30075) … S3P-001/S3P-002 re-keyed to
  S30082/S30083." The range names the tokens the binding pass consumed.
- L151 `S3001`, `S3022` — class 2, inside the pending `S3P-001` row's own note field: "ID PREFIX S3P IS
  THIS PART'S OWN AND IS A DEFECT WORKAROUND: sources.csv already holds THREE colliding S3001-S3022
  sequences … so no further S3xxx id is safe". Rewriting it destroys the justification for the
  provisional id that the same line says became `S30082`.
- L185 `S3001` — class 2, hold explanation: "<failures.csv> APPLIED … HELD: row 8 … its cited bare
  S3001 has three candidates and the row asserts a corpus-wide null no single filing can carry".
  This is the *note about* the hold at L182; it must name the dead token to be intelligible.
- L143, L182 — class 3, see *Held-as-unresolved*.

## Held-as-unresolved

STATUS: WRITTEN 2026-09-25

**5 lines, 12 token occurrences.** Each was left verbatim with its visible marker in place; none was
written by this pass, none was silently dropped. For each: the candidates, the missing fact, and what
a later pass must supply to close it.

1. **`stage_3_claim_records.md` L1524 — `S3007` (2 occurrences, HELD).** Claim record S52 reproduces
   the merge note "`S3007` exists in `sources.csv` already and must not be re-defined (§13: reuse ids)".
   Measured this session: `sources.csv` has **no** `S3007` row, and the re-key map's ST3_C block has no
   `S3007` pair at all (it runs `S3006 → S30058`, then `S3008 → S30059`). So the sentence names the
   *primary key of a row that was never written*, not a document. The document itself **is** recoverable
   and is already recorded in the marker: ST3_C's `S3007` payload at `stage_3_part_3.md` L613 reads
   "8-K event 1998-10-28 (Q3-1998 results release), SEC EDGAR acc 0000891020-98-001498", and that
   event/accession occurs under exactly one canonical row, `S30051` = "Forms 8-K, events 1998-10-28 and
   1999-01-05". Re-pointing the **key** to `S30051` is nonetheless forbidden: `S30051` is ST3_B's row
   (map: `ST3_B S3021 → S30051`) with 18 fields and different claim text, so the rewrite would assert
   that C's unwritten row exists. *To close:* a register pass must decide whether ST3_C's held row is
   written under a new canonical id — after which the narrative note can name that id — or is dropped
   as a duplicate of `S30051`.
2. **`stage_3_part_3.md` L613 — `S3007` (4 occurrences, HELD).** The §S.9 held-row table row carrying
   the same unwritten ST3_C `sources.csv` row verbatim (payload key, two prose mentions, and the
   marker's restatement). Same disposition, same closing condition; the width defect it records
   (19 fields because the `url` cell contains a comma) is a register task, not a citation task.
3. **`stage_3_part_2.md` L907 — `S3001`, `S3012`, `S3013`, `S3020` (4 occurrences, HELD).** "this part
   cites those IDs (ST3A-…, ST3B-…, ST3C-…, ST3D-…, ST3E-…, and source_ids S3001, S3012, S3013, S3020)
   and redefines none of them". Checked independently this session: those 4 tokens are the volume's
   **entire** `S3` inventory (918 lines scanned, no canonical id and no other bare id), and the volume
   names no authoring dossier — its headers show §K–§O as one merged span (K money, L validation,
   M failures, N decisions, O counterfactuals) and L903–905 attributes the claim refs to all five
   Stage-3 dossiers. All three map triples are internally consistent with the token pattern — A
   `S30001/S30012/S30013/S30020`, B `S30031/S30042/S30043/S30050`, C `S30053/S30063/S30064/S30071` —
   and no line ties an exemplar id to a block. The inference "§K is money, therefore ST3_B" was
   considered and **rejected**: the same sentence credits five dossiers' record sets, so it is style
   guessing, i.e. exactly the invented mapping this task forbids. *To close:* the merge record (or the
   `_parts/s3_p3.md` provenance note, which carries the identical sentence and is outside this pass's
   write scope) must state which dossier's exemplar list §K–§O drew from.
4. **`stage_3_pending_registers.md` L143 — `S3004` (1 occurrence, HELD).** The pending `timeline.csv`
   payload row for the 1999-11 launches event, whose own section refs are "§P248 §P250". The applied
   row binds **two** ids (`S30011` = Form 10-Q quarter ended September 30 1999; `S30075` = Form 10-K
   FY1999 — both verified in `sources.csv` this session), so no single canonical token can carry the
   cell; choosing one drops the other document out of the citation. *To close:* the register must
   allow a two-id cell (or split the row), which is a schema decision, not a citation repair.
5. **`stage_3_pending_registers.md` L182 — `S3001` (1 occurrence, HELD).** The held `failures.csv`
   row 8, the never-filed-unit-metrics null. Three candidate documents fit the bare token, one per
   dossier block: `S30001` (ST3_A, Form S-8 File No. 333-28763), `S30031` (ST3_B, Form 10-K FY1998),
   `S30053` (ST3_C, FY1997 Form 10-K405). Beyond the ambiguity the row asserts a **corpus-wide null**
   ("no order count, average order value, fill rate or returns rate in any accession 1997-1999"), which
   no single filing can carry — the binding pass refused to write it for that reason (L185), and the
   same reasoning holds here. *To close:* bind the row to the whole FY1997-FY1999 accession set as a
   list, or re-file it as a data-gap row with a multi-source field.

No other token in the six files was left unresolved: the remaining 22 occurrences are class-2
historical references listed in *Per-file resolutions*, and both this pass and the earlier
propagation pass measured **zero** retired tokens on a line that carries no visible marker.

## Proof

STATUS: WRITTEN 2026-09-25

**Machine measurements (this pass, local files only).**
- `sources.csv`: 203 data rows; `source_id` column contains **zero** 4-digit `S3nnn` keys; canonical
  block runs `S30001`–`S30083` (tail observed: `S30078 S30079 S30080 S30081 S30082 S30083`).
- Retired-token census over the six gate-flagged volumes, pattern `S3[0-9]{3}\b`: **34 occurrences on
  20 lines**; lines carrying no visible marker: **0**; class-1 citation sites: **0**; class-2: 22
  occurrences / 15 lines; class-3: 12 occurrences / 5 lines.
- `stage_3_part_2.md` full-file `S3` inventory = the 4 tokens at L907 (918 lines scanned) — the
  fingerprint that would have been needed to resolve that hold does not exist in the file.
- Re-key map ST3_C block: `S3006 → S30058`, then `S3008 → S30059` — no `S3007` row, which is why the
  two `S3007` sites are holds rather than re-points.

**Gate `--checks keys`, BEFORE (first run of this pass).**

```
Findings: 6 | Passes: 8
| keys | stage_3_claim_records.md           | unresolvable source tokens: S3001, S3007, S3081 |
| keys | stage_3_claim_records_part_2.md    | unresolvable source tokens: S3001, S3022, S3081 |
| keys | stage_3_index.md                   | unresolvable source tokens: S3001, S3022 |
| keys | stage_3_part_2.md                  | unresolvable source tokens: S3001, S3012, S3013, S3020 |
| keys | stage_3_part_3.md                  | unresolvable source tokens: S3001, S3007, S3081 |
| keys | stage_3_pending_registers.md       | unresolvable source tokens: S3001, S3004, S3022, S3024 |
```

**Gate `--checks keys`, AFTER (this pass wrote no token into or out of those files).**

```
Findings: 6 | Passes: 9
| keys | stage_3_claim_records.md           | unresolvable source tokens: S3001, S3007, S3081 |
| keys | stage_3_claim_records_part_2.md    | unresolvable source tokens: S3001, S3022, S3081 |
| keys | stage_3_index.md                   | unresolvable source tokens: S3001, S3022 |
| keys | stage_3_part_2.md                  | unresolvable source tokens: S3001, S3012, S3013, S3020 |
| keys | stage_3_part_3.md                  | unresolvable source tokens: S3001, S3007, S3081 |
| keys | stage_3_pending_registers.md       | unresolvable source tokens: S3001, S3004, S3022, S3024 |
```

**Why the finding set is unchanged, and what each residual line means.** `gate_keys` tests only
`re.findall(r"\bS\d{3,6}[a-z]?\b")` against the `sources.csv` key set; it has no marker awareness, so
a *correctly dispositioned* hold or a *correctly preserved* historical reference fails the gate
exactly like an undiscovered one. Zeroing the gate therefore requires either re-pointing these tokens
(22 of them name the retired space, not a document) or deleting text this brief forbids deleting.
Neither is available; the honest end state is the six lines above, one per file, each explicable:
- `stage_3_claim_records.md` — `S3007` = held unwritten ST3_C row key; `S3001`, `S3081` = the 81-row
  range at §T. Both marked in place.
- `stage_3_claim_records_part_2.md` — `S3001`, `S3022`, `S3081` = collision note + quotation of §T.
- `stage_3_index.md` — `S3001`, `S3022` = "colliding `S3001–S3022` source-id sequences", defect history.
- `stage_3_part_2.md` — `S3001`, `S3012`, `S3013`, `S3020` = the 4 held exemplar source_ids, all three
  candidate triples listed in the marker.
- `stage_3_part_3.md` — `S3007` = same unwritten ST3_C row reproduced in the §S.9 table; `S3001`,
  `S3081` = §T range.
- `stage_3_pending_registers.md` — `S3004` = two-id pending row; `S3001` = pending `failures.csv`
  row 8 plus 8 meta mentions; `S3022`, `S3024` = retired-scheme range endpoints only.

**Coverage / integrity notes.**
- Write scope honoured: this sheet plus nothing. **No byte of the six narrative volumes was modified**
  by this pass, so no line count moved and no pointer *into* those files was invalidated (method §14
  rule 12 obligation discharged trivially). All sites in this sheet are addressed by file + token +
  stable anchor (§T, §S.9, claim record S52, pending block row), with the line number carried as a
  locator only.
- Concurrent writer observed, not touched: between my two gate runs `Passes` moved 8 → 9 and a new
  Stage-2 volume `stage_2_claim_records_part_1b.md` entered coverage (15 → 16 stage volumes). That is
  another owner's path; no collision with this pass's target.
- Budget: **31 tool calls of the 55 allowed** (the 45-call stop never approached); the `release` call
  is the last of them. Web requests: 0. Git: none. No file deleted, moved, renamed or
  renumbered; no id allocated; no document title, date or accession written here except strings read
  off `sources.csv`, the re-key map, or the six volumes during this session.
- What RD-078 still needs to reach zero: (i) the two `S3007` register decisions (write ST3_C's row
  under a canonical id, or drop it as a duplicate of `S30051`), (ii) provenance for the §K–§O exemplar
  id block, (iii) a two-id `source_id` cell in `timeline.csv`, (iv) a multi-source or data-gap home for
  `failures.csv` row 8, and (v) either a marker-aware `keys` gate or a documented exemption list for
  class-2 historical references — otherwise every future `--checks keys` run re-reports this same
  residue as if it were undiscovered.

