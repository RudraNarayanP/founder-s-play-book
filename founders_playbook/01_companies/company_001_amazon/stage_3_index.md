# Amazon.com Stage 3 — volume index

One forensic document, split at section boundaries (§9.3). Assembly parts under `_parts/` remain the audit
trail of who wrote which section, including the double-dispatch and turn-ceiling history.

| Volume | Sections | Words |
|---|---|---|
| `stage_3_part_1.md` | Header, STAGE BOUNDARY JUSTIFICATION, §A–§J | 45,120 |
| `stage_3_part_2.md` | §K–§O | 23,781 |
| `stage_3_part_3.md` | §P–§U | 42,888 |
| **Narrative total** | §A–§U | **111,789** |

Comparison: Stage 1 = 49,545 narrative words; Stage 2 = 81,129. **Stage 3 is 1.38× Stage 2**, the expected
shape for a window with 75 filings, a nine-site estate, three stock splits and 55 registered conflicts.

## What is NOT yet done

1. **Registers.** `stage_3_pending_registers.md` holds §P–§U's 134 rows, unapplied behind `RD-075`: three
   colliding `S3001–S3022` source-id sequences from the earlier merge, and two Stage-3 stage grammars
   (`3` vs `stage3`) across four registers. Both are orchestrator-created and must be fixed before applying,
   or `source_id` joins silently resolve to the wrong document.
2. **No claim-record appendix.** Stage 1 has 432 records, Stage 2 has 479. Stage 3's `stage_3_claim_records.md`
   does not exist yet.
3. **No audits.** All five Stage-3 gates remain unrun, and the boundary is contested on the page rather than
   decided — which is the correct state for an un-audited stage.
4. **Known open defects carried in:** `RD-076` (four falsified or re-based figures, including a filed 1996
   working-capital line of 1,698 that two stages believed was never printed), `RD-077` (instruction-layer
   retraction residue, registered as U.168), and `RD-073`/`RD-074` (a closed dossier's re-printed comparative
   and a margin trend that inverts on the filed line).
