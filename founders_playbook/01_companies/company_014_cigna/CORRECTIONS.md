# CORRECTIONS.md — company_014_cigna (Stage 1)

Append-only provenance-correction register for the Cigna Stage-1 dossier. Established **at the Stage-1 merge
pass, 2026-10-06** (agent `merge-cigna`), each item verified against the author emission `_parts/s1_p1.md`
and against the held bytes under `sources/` and `research/`. **Nothing here re-tiers, re-dates, re-values or
deletes a claim.** These are key, propagation and schema corrections — the three classes a merge is allowed
to make. A later pass adds a dated entry above this one; it does not delete one.

**Reading rule.** Every `COR-nn` below is printed in the register layer *and* in `stage_1.md`, because a
correction that reaches only the prose leaves the registers teaching the withdrawn form (method §14.10). The
propagation is measured by `tools/gates.py --checks corrections`, and the cell each entry touched is named in
the merge record `03_quality_control/cigna_s1_merge.md`. Where an entry names an annotation, the annotation
was **appended to the end of an existing `notes` / `residual_uncertainty` cell**: no value, date, source key
or confidence on any of the 78 applied rows was altered, and no row was folded.

---

## COR-01 — the dossier-local source tags `CG01–CG16` are superseded by minted ids `S4407–S4422` (2026-10-06)

**What the author emitted.** 16 `sources.csv` rows keyed `CG01`…`CG16`, with the same tags carried in the
`source_id` cells of `quantitative`, `timeline`, `decisions`, `validation`, `failures`, `channels` and inside
notes text (`_parts/s1_p1.md` l.490, merge instruction (1) and (4): "the merge mints global ids … blank them
at merge into the minted ids").

**Correction applied.** `python tools/id_mint.py --count 16 --company company_014_cigna --claim --agent
merge-cigna` allocated **S4407 … S4422** contiguously, above the highest live id (`--audit`: range
S0001–S4406, `next assignable: S4407`). Every register row now carries the minted id; **no register row and no
cell retains a `CG` tag** (verified by regex over all nine files: zero matches). The narrative volume keeps the
author's local tags — they are the reading keys of §B, §K, §T and the claim records — and is bound to the
global space by the mapping table in `stage_1.md` (the merge record, "Provisional-to-global id map").

**Why this is a correction and not a rename.** Ids minted by authors have collided in this project:
`tools/id_mint.py --audit` reports `S4222–S4229` cited by both `company_011_microsoft` and
`company_042_target`, which is why Target's next mint is held (task #31). A local key may not survive into a
global register. **This entry is the authority for treating any `CG01–CG16` row found in a live register from
now on as stale.**

**Propagated to.** `sources.csv` S4407 `notes` cell · `stage_1.md` merge record.

---

## COR-02 — the 4-row and 6-row emissions are bound to `validation.csv` and `failures.csv` respectively (2026-10-06)

**The ambiguity.** `validation.csv` and `failures.csv` share a byte-identical 11-column header, so
`tools/merge_census.py` prints both blocks as `AMBIGUOUS:validation.csv,failures.csv` and cannot attribute
them (it did so before this merge and does so after — a schema property, not a defect in the emission).

**Correction applied — decided by reading, not by position.** (i) the part's own block headings name the
targets (`### \`validation.csv\` — 4 rows` at l.576, `### \`failures.csv\` — 6 rows` at l.589); (ii) the
author's stated counts agree (4 and 6, `_parts/NOTES_cigna_p1.md`); (iii) the rows' semantics agree with the
registers' control meaning — the 4-row block's `what_it_demonstrated` cells are all positive validation claims
(health pre-tax +48%; the buy-a-plan pattern repeated; three independent court records; the 2018 indenture
designation), the 6-row block's are all adverse signals (101.8 combined ratio; $84.8M 1978 losses; reserves
96→111% of earned; the 5%-of-income parent-and-other loss; goodwill write-downs; three respondent appearances).
4 + 6 = 10 = the census's unattributed total, with no row in both groups.

**Propagated to.** `validation.csv` first row `notes` · `failures.csv` first row `notes` · `stage_1.md` merge
record. **The census's `AMBIGUOUS` line is expected to persist after this correction** — it is the tool's
schema blindness, now adjudicated on the record rather than left to a future pass.

---

## COR-03 — the probe's 17:20 header claim ("both ancestor dates occur 0 times in every held byte", Stage 1 = **T3 register**) is withdrawn at the instruction layer (2026-10-06)

**The withdrawn form.** The first version of `research/A_chronology_feasibility.md`'s verdict line, written
against the 17:20 corpus (4 non-SEC documents), asserted that the two ancestor dates "occur **0** times in
every held byte" and graded Stage 1 **T3 register, PROVISIONAL**.

**What the bytes print now.** At 17:22-17:23 the fleet mine landed six layers; `1792` occurs **2** times, both
inside `sources/periodicals/INAC2115_1979_djvu.txt` (l.5, l.371) — re-measured by the author and re-measured
again for this merge; `1872` remains **0**, and the lone `1850` is an ERIC sentence about New Haven. The probe
regraded itself to **T2 core, PROVISIONAL** on the lineage frame, keeping the T3 reading for the
strict-registrant frame (§7 row 2). The retraction stayed **inside the probe file** and had never reached the
instruction layer until this entry.

**Correction applied, and its limit.** This entry registers the withdrawal so no downstream pass resurrects
either half. It **does not** re-tier anything: Stage 1 stays T2 core PROVISIONAL (lineage frame) **and** T3
register (strict-registrant frame), both carried as states in `stage_1.md` §boundary, §A, §B.2, §R and §U.4,
never averaged. `1872`/1850s for the second ancestor remains **UNTRIED** — a query-scope silence, explicitly
not a null (FR-7).

**Propagated to.** `conflicts.csv` U.2 `residual_uncertainty` cell · `quantitative.csv` census row `notes`
cell · `stage_1.md` §U.2, §U.4 and the merge record.

---

## Not corrected, and why (recorded so the absence is a decision, not an oversight)

1. **No fold, no dedup, no row withheld.** 78 rows requested, 78 applied. No `sources.csv` row was minted for
   the four S-4 amendments or the exhibits of acc. 0001140361-18-024107 (one lineage), for CG03's two exhibits
   (one accession), or for CG07's md5-identical pair on two shelves (one document).
2. **The 1982 combination stays a hypothesis** (U.3): 0 held bytes pair `1982` with a merger verb; it lives in
   `conflicts.csv` and `timeline.csv` as an unattested assertion, never as a fact. Nothing here "corrects" it
   toward fact or toward null.
3. **FR-8** (pre-1979 outside witnesses to the 1792 claim) has **no `data_gaps.csv` row**, because the author
   emitted none and the merge does not invent register rows; its home is UNTRIED item 8 in `stage_1.md` and the
   `residual_uncertainty` cell of `conflicts.csv` U.2. Named here so it is not lost.
4. **`research/_EVIDENCE_CACHE.md`** is still absent. `data_gaps.csv` row 11 asks for it "at merge", but the
   cache is not among the deliverables this merge claimed (`stage_1.md`, the nine registers, `_MANIFEST.md`,
   `stage_1_index.md`, `CORRECTIONS.md`). The row stays open and is reported as an uncarried follow-up in
   `03_quality_control/cigna_s1_merge.md`, not silently closed.
