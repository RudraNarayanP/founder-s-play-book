# amazon_s3_gate_residue.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T20:09:32Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## Parity measurement

Re-measured against the gate's own detector (`_anchors_declared` / `_reg_anchor_tokens`), not against the count quoted in the brief.

**Narrative declarations (173 distinct anchors):** `stage_1.md` 43 (U.1–U.43) · `stage_2_part_1.md` 1 (U.44) · `stage_2_part_3.md` 72 (U.44–U.113 + U.113a/U.113b) · `stage_3_part_1.md` 1 (**U.220 only**) · `stage_3_part_3.md` 57 (U.114–U.170, incl. U.169/U.170 from the last repair pass).

**Direction 1 — declared, no register row: 1 (`U.220`).** `U.220` was never a narrative §U entry: the `>>> CONFLICT FOR §U` label in `stage_3_part_1.md` soft-wrapped so that the line began with the literal text `U.220, U.221, U.222`, and the detector reads a line-initial anchor as a declaration. Those three keys are `ST3_E` dossier-local — the same file's collision note says so in its own words ("dossier-local keys, **not** register IDs"). Fix applied: backticked the three keys in that heading, which keeps the folding instruction readable and stops the accidental label. I did **not** add a register row citing a dossier-local key (that launders the dossier spine into the register, against method §13) and did **not** write an empty §U heading.

**Direction 2 — register-cited, no declaration: 11 (`U.201`–`U.211`).** Registers citing them: `conflicts.csv` 11 rows (one each, carried in the `section` column as "[dossier id U.20n; from ST3_A_chronology_org.md]"), `sources.csv` 14 occurrences, `timeline.csv` 12 occurrences. These are the `ST3_A` dossier spine folded into register keys U.114–U.124; the re-key map's own preamble states the dossier id "is echoed here for the parity check" — but in `stage_3_part_3.md`'s `>>> CONFLICT RE-KEY MAP` table the `Dossier original` cells were backticked, so the echo was invisible to the detector (the `Final` column, printed un-backticked, is exactly how U.114–U.170 declare themselves). Fix applied: removed the backticks from the 11 `Dossier original` cells only. No new §U entries were invented: writing 11 fresh §U blocks would create a second conflict series duplicating U.114–U.124, which is worse than the finding.

**After both fixes: 0 in each direction** — the `anchors` gate now reports parity.

## Rows added or relabelled

**Zero register rows added, zero relabelled, zero values changed in the nine CSVs by this pass.** Register layer is untouched apart from verification: all nine still pass the `csv` gate (row/col counts unchanged at measurement: timeline 267×11, quantitative 395×12, conflicts 172×15, sources 204×18, data_gaps 102×8, validation 59×11, failures 62×11, decisions 29×15, channels 25×11), the controlled `stage` vocabulary is unchanged (`stage1 | stage2 | stage3`; the residual numeric `3` grammar in the seven Stage-3 registers is a pre-existing finding recorded in `stage_3_pending_registers.md` and is **not** mine to normalise under §13 "normalise on touch" — I touched no row of it), and no `DERIVED` row was edited so no `derived_arithmetic` obligation arose.

The only cell re-pointed by this pass sits in an **un-applied append block** in `stage_3_pending_registers.md` (see *Re-pointed tokens*), not in a register.

## RD-090 register retraction

**Already closed by another pass; verified, deliberately not re-edited** (concurrency note in the brief; re-editing a landed repair is how two passes destroy each other's work).

`timeline.csv`, row dated `1999-h1` (line 164 at measurement) now prints: event = "Nevada (Fernley) distribution centre reported OPENED in the half-year - the company's first such statement for THIS site, **NOT** the first 'opened' verb in the corpus (retracted per RD-090)"; confidence = "High (that Nevada was leased-and-opened by Q1-1999) / RETRACTED as to 'first'"; conflict_ref = "U.153 / U.204"; evidence_class = `FACT` (defensible — the surviving assertion is what a filing prints about this site, and the row states what survives and what does not); source_id = `UNRESOLVED(cand=S30010|S30064;missing=which-duplicate-is-canonical)`; notes = "RD-090 repair 2026-09-26. SUPERSEDED TEXT, kept readable as withdrawn: event='First distribution centre the company states it opened (Nevada)', confidence=High, note='The verb, not the lease, is the event.'" followed by the three falsifiers (row 1997-11 / S30005 / U.153 Delaware FY1997 10-K405 l.1646-1648; row 1997-12-31; 10-Q Q1-1999 l.592).

So the class/confidence/note the brief asked me to set are set, and the superseded value survives only inside retraction language (the §14 rule 8 test). **Adjudication still owed by someone else:** that row's `source_id` is a held `UNRESOLVED` — duplicate 10-Q accessions S30010/S30064 — which needs the duplicate-resolution decision, not a citation hunt. Not invented here.

## Sibling sweeps

Counts at measurement (a read-only numbers auditor is working the same files, so cite these as labels, not as figures that must hold):

* Exact phrase **"verb, not the lease"**: `timeline.csv` 1, `research/ST3_A_chronology_org.md` 1, every other register 0, every stage volume 0. The register hit is inside RD-090's "SUPERSEDED TEXT, kept readable as withdrawn" quote — i.e. retraction language, which is where a superseded value belongs.
* **"states it opened"**: `timeline.csv` 1 (same quoted note); all other registers and all stage volumes 0.
* **"first … opened" / "opened … first|verb"**: `timeline.csv` 4 — of which 1 is RD-090's own retraction, 1 is the Delaware falsifier row (1997-11, a filed fact, not a dating criterion), 1 is the 1994-11 Seafirst Bank merchant account (regex false positive), 1 is the 1999-11 launches row (no dating force). `validation.csv` 2 (Seafirst 1994-11; music store 1998-06 — both unrelated). `conflicts.csv` 3 (U.24 Seafirst; P-U.151 the seven-DC count; **U.153 = the voiding entry itself**, which must quote the criterion it voids). `quantitative.csv` 1 (music store). `sources.csv` 3 (S0610 first-order account; S30011 note "first filed statement of five DCs opened"; S30072 note "first filed 'opened' for a second DC" — both falsifier records). `decisions.csv`, `channels.csv`, `data_gaps.csv`, `failures.csv` 0.
* Narrative: `stage_3_part_3.md` 1 (the falsification record, "first use of 'opened'… The falsification is total, and it is checkable in three greps"); the `ST3_E` A06 record in `stage_3_claim_records_part_1b.md` carries the same retraction.

**UNTRIED / out of ownership:** the instruction layer (`RESUME_HANDOFF.md`, `MASTER_RESEARCH_LOG.md`, `_MANIFEST.md`, `CORRECTIONS.md`, `stage_2*`) was **not** swept by this pass — those paths are held by the re-certification pass, and §14 rule 10 says that is exactly where a stale claim survives. **Flagged for that pass, not fixed here.**

## Re-pointed tokens

**1 genuine citation re-pointed.** `stage_3_pending_registers.md`, `>>> CSV APPEND BLOCK: timeline.csv`, row 33 (1999-11 launches): the `source_id` cell's bare `S3004` → `S30011; S30075`, with the provenance written into the same row's notes cell. The mapping is **not invented**: the status line the binding pass printed directly under that block says "row 33 (1999-11 launches) bound to TWO ids (S30011; S30075) because its own section refs P248/P250 name two documents", and `timeline.csv` at date 1999-11 actually carries `S30011; S30075`. The pending cell now matches the register the binding pass wrote; the row's pre-existing `[UNRESOLVED — candidates S30011/S30075 …]` tail is left in place because it names the same pair.

**5 mention-class tokens labelled, not re-pointed** (protected history: collision notes and id-space ranges, which the gate separates from citations): `stage_3_pending_registers.md` line at "blocked behind `RD-075`" (`S3001`–`S3022`), the same file's "three colliding `S3001`…`S3022` sequences" — where a prior pass had dropped its `[RETIRED-KEY REFERENCE …]` marker 110 characters away from its own tokens and mid-sentence, so the marker was relocated to sit adjacent to the range it describes (sentence restored, nothing deleted) — the `>>> timeline.csv APPLIED` status line ("Bare citations `S3001`-`S3024` resolved by content"), and the `sources.csv` block's in-cell collision note (`S3001`-`S3022`). All use the marker this corpus already established (`stage_3_index.md`, `stage_3_part_3.md`, and the top of `stage_3_pending_registers.md` carry it verbatim).

**Self-inflicted defect found and fixed on this pass:** my first adjacency marker for `S3007` in `stage_3_part_3.md` named the surrounding ids as bare tokens (`S3006 → S3008`), which created two new dangling citations. Corrected: explanation ids are backticked, and only the id under discussion is printed bare inside a `UNRESOLVED` window. This is the §14 rule "repairs create defects" case — recorded rather than hidden.

## Held as UNRESOLVED

Three sites where the intended canonical document cannot be determined from the re-key map plus `sources.csv`. Held visibly; no mapping invented.

1. **`stage_3_part_2.md`, "NOTE ON §Q–§U AND THE CLAIM RECORDS"** — cited bare `S3001, S3012, S3013, S3020`. The re-key map gives each **three** candidate documents (ST3_A `S30001/S30012/S30013/S30020`; ST3_B `S30031/S30042/S30043/S30050`; ST3_C `S30053/S30063/S30064/S30071`), and resolution is by content — but no other bare four-digit id occurs in this volume, so nothing fingerprints which dossier block the §K–§O exemplar list was drawn from. Wrapped in a visible `UNRESOLVED ×4` marker at the tokens, keeping the three candidate sets and the missing fact legible at the citation (the paragraph's pre-existing tail marker, too far from the tokens to protect them, was left untouched).
2. **`stage_3_part_3.md`, §T row-8 collision table** — cited `S3007` (ST3_C). `03_quality_control/stage3_sourceid_rekey_map.md` carries **no ST3_C/S3007 row at all**: that block runs `S3006` → `S3008`, skipping the id. There is therefore no canonical 5-digit document to point at, and the pre-existing `[UNRESOLVED — held row …]` note on the same line says the same thing. Marker moved adjacent to the token.
3. **`stage_3_pending_registers.md`, `failures.csv` append block, row 8** (the never-filed-unit-metrics null, HELD and never applied — the block's status line reads "rows 1-7 of 8 written") — its `source_id` cell `S3001` → `UNRESOLVED(bare S3001: candidates S30001/S30031/S30053 …; the row asserts a corpus-wide null no single accession carries; HELD for adjudication per 03_quality_control/stage3_register_binding.md)`, and the status line under the block now reads "its cited bare S3001 is UNRESOLVED — … adjudication owed". The row is `UNKNOWN` on evidence class already, and I did not choose among the three candidates.

**Deliberately left broken (named, not silent):** `stage_3_claim_records_part_1b.md` still yields the file's `S3007` finding — the same undeterminable ST3_C id — because every `stage_3_claim_records*` path belongs to the claim-record split pass. Editing it would put two writers on one file (§14 rule 7).

## Gate before and after

**Before** (`python tools/gates.py --company-dir "founders_playbook/01_companies/company_001_amazon" --checks csv,keys,anchors,budget`): **Findings 6 | Passes 42**

```
| keys    | stage_3_claim_records_part_1b.md | unresolvable source tokens: S3007 |
| keys    | stage_3_part_2.md                | unresolvable source tokens: S3001, S3012, S3013, S3020 |
| keys    | stage_3_part_3.md                | unresolvable source tokens: S3007 |
| keys    | stage_3_pending_registers.md     | unresolvable source tokens: S3001, S3004, S3022, S3024 |
| anchors | narrative                        | anchor with no register row: U.220 |
| anchors | registers                        | register row citing an anchor absent from the narrative: U.201 … U.211 |
```

**After** (same command): **Findings 1 | Passes 46**

```
| keys | stage_3_claim_records_part_1b.md | unresolvable source tokens: S3007 |
- coverage 9 registers, 17 stage volumes, 101 source documents
```

Both `anchors` findings closed (parity now passes in both directions); three of four `keys` findings closed; `csv` 9 registers + 4 source_id resolution checks pass; `budget` clean on the five files this pass wrote to — measured after: `stage_3_part_1.md` 49,374 · `stage_3_part_3.md` 43,659 · `stage_3_part_2.md` 25,288 · `stage_3_pending_registers.md` 10,722 · `stage_3_index.md` 661 (cap 60,000 each). This pass added roughly 240 words to those four volumes and moved none toward the cap; `stage_3_index.md` was measured and needed no edit.

**The one residue is irreducible without touching another owner's file or inventing a mapping**: ST3_C `S3007` has no row in the re-key map, so no agent can name its document; the token sits in a claim-record path owned by the split pass. Target stated honestly — zero findings is the goal, and this residue is named, reasoned and owned elsewhere.

**Tooling incident to report:** during this pass `tools/gates.py` was left unparseable by a concurrent edit (SyntaxError at line 629, literal newlines inside the new `plant_unpropagated_retraction` self-test case), so `gates.py` could not run for part of the work; I verified my fixes with a faithful local replica of the `keys`/`anchors` detectors instead and re-ran the real gate once that pass restored the file. `tools/` is in my DO-NOT-TOUCH set, so it was reported, not repaired. The new self-test case it was adding ("retraction never reaches the registers", RD-105's shape) is exactly the gate RD-090 needed — worth telling whoever owns `gates.py` that the register layer for RD-090 already passes it.

