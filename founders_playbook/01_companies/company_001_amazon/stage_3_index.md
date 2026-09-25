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
   colliding `S3001–S3022` source-id sequences from the earlier merge, and two Stage-3 stage grammars [RETIRED-KEY REFERENCE — names the pre-re-key id space; not a citation]
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

## Citation key convention (read this before writing a Stage-3 citation)

Stage-3 source citations take the canonical key **`S300nn`** — `S3` followed by a four-digit zero-padded
sequence number, `S30001` through `S30083`, the 83 rows of `sources.csv`. Do not write the retired
dossier-local form (three digits after `S3`, numbered from 1 to 81): it was never unique — the same string
named three different documents across the four dossiers — and it resolves to nothing now. The pairing
`(dossier, retired id) -> canonical id` is the authority and lives in
`03_quality_control/stage3_sourceid_rekey_map.md`; how those pairs were pushed into the texts, site by site,
is in `03_quality_control/stage3_citation_propagation.md`. A citation that cannot be paired with exactly one
document is left in place and marked `[UNRESOLVED — candidates …; missing fact: …]`; a retired id that prose
is *talking about* — the retired key space itself — is left in place and marked
`[RETIRED-KEY REFERENCE — …]`. Neither is ever silently re-pointed, and neither is ever deleted.

**Two register rows are still held, not applied** (§14 rule 4: a held row is a task, not a loss):
`failures.csv` block row 8 — the never-filed unit-metrics null, whose bare citation had three candidate
documents and which asserts a corpus-wide null no single filing can carry; and `decisions.csv` block row 3 —
the 1998-06-01 "pay a stock dividend for the 2-for-1" row, which cites `S30083` (provisionally `S3P-002`), a
row registering only the 8-Ks of 1998-11-19 and 1999-07-21, so its date and its citation cannot both stand.
Both are reproduced in full at `03_quality_control/stage3_register_merge_held_rows.md` and named in the
per-block status lines of `stage_3_pending_registers.md`.


---

**PART LIST OF THE CLAIM-RECORD APPENDIX as at 2026-09-26** (mechanical §9.2/§9.3 budget split; sheet `03_quality_control/amz_claim_record_split.md`). The appendix is **three** volumes of one document with continuous ids — nothing re-based, renumbered or reused:

1. `stage_3_claim_records.md` — volume 1a: front matter + §A–§L; records **A09 → L35**, 347 records, 44,228 words.
1. `stage_3_claim_records_part_1b.md` — volume 1b: §M–§T and the closing “VOLUME 1 ENDS HERE” statement; records **M27 → T58**, 280 records, 40,764 words.
1. `stage_3_claim_records_part_2.md` — volume 2: §U conflict spine + coverage note + defects; records **U.114 → U.168**, 55 records, 15,036 words.

Stage-3 total: **682 records**, unchanged by the split. The two-volume statements earlier in this index are superseded by this register, not rewritten (method §14 rule 4).
