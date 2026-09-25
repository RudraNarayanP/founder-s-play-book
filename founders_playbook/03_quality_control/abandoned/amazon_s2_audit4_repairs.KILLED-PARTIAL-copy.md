

---

## CORRECTION — appended 2026-09-26 by the Stage-2 dangling-reference repair pass (RD-079)

*This section is additive. Nothing above it is altered, re-labelled or deleted: it is the audit trail of what the
2026-09-25 pass believed it did, and the divergence between that belief and the disk is itself the finding.*

1. **The two §U blocks were never emitted.** This pass's report to the orchestrator stated that it had written two
   new conflict blocks and taken the spine to 72↔70. `stage_2_part_3.md` on disk emits **70 §U blocks, U.44–U.113**,
   with **no `>>> CSV APPEND BLOCK: conflicts.csv` section at the foot of §U and no `RESERVED` marker anywhere** in the
   file or in `stage_2_index.md`. This sheet never states 72 either: the claim lived **only** in the report to the
   orchestrator. The reservation described above was therefore never made, and the registers were correctly left at 70
   Stage-2 rows.
2. **The ids used for the two unwritten blocks belong to Stage 3.** §U.114 (the Buschman equipment-contract finding)
   and §U.115 (the 1998 proxy officer roster) are Stage-3 rows in `conflicts.csv`. Because the repaired prose keyed 24
   lines onto them — `stage_2_part_1.md` l.66/68, nine lines of `stage_2_part_2.md`, nine of `stage_2_part_3.md`,
   `stage_2_index.md` and both claim-record volumes — **a Stage-2 reader following a cross-reference was delivered into
   a different stage's conflict.** Recorded as RD-079 in `MASTER_RESEARCH_LOG.md`.
3. **Resolution (2026-09-26).** Every citing line was read in context and checked against all 70 existing §U titles:
   no existing block carries either claim, and each site already names the existing block for its *other* point
   (U.45/U.48/U.52/U.55/U.59/U.68/U.95/U.97/U.98). Both are therefore **genuine-but-unwritten (type (a))**: **0
   references were mis-points to be re-directed onto an existing block, and 24 were re-keys.** The two missing blocks
   are minted as the lettered addenda **§U.113a** (the IPO price walk across the S-1 lineage, against the four struck
   wordings) and **§U.113b** (the FY1996/FY1997 restated pair, cause UNKNOWN) at the foot of `stage_2_part_3.md` §U,
   following the **U.111a addendum precedent**; nothing was renumbered (§9.3) and Stage 3's ids were not taken. All 24
   lines are re-keyed by label (§14.12). `stage_2_index.md` l.28–33, l.39–41 and l.77 now state the true numbers,
   with the phantom append and the phantom RESERVATION **retracted in place, not rewritten**; the `stage_2_part_1.md`
   and `stage_2_part_3.md` preambles are likewise restated at 72 blocks / 70 rows.
4. **Invariant after the correction:** §U emits **72** Stage-2 blocks (U.44–U.113, U.113a, U.113b) with no gap and no
   duplicate; `conflicts.csv` holds **70** Stage-2 rows and stays there until the orchestrator appends U.113a/U.113b at
   `stage2`, after which the pair is 72↔72. Sheet: `03_quality_control/amazon_s2_dangling_refs_repair.md`.
5. **Method lesson for the next pass:** *a repair pass may not report a count it has not re-read from disk.* The
   72↔70 spine, the CSV append block and the RESERVED rows were all reported as done and none exists; the check that
   catches this is re-grepping the emitted ids and the emitted count in the edited file before the report is written.
