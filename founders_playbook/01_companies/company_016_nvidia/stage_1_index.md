# NVIDIA Stage 1 — volume index

Written by the Stage-1 merge pass on 2026-09-30 (`nvidia-s1-merge`). **One volume**, sections A–U continuous,
carried in part order at section boundaries. No §9.3 split was triggered: the merged volume measures **46,691
words / 323,547 bytes** against the 40,000-word soft target and the **60,000-word hard cap**, which puts it in
the §9.2 amber band that is explicitly allowed to finish the stage as one file. Company tier is **T3 register**
(the probe verdict in `research/A_chronology_feasibility.md`, re-confirmed without re-issue in
`research/A3_intake_regrade.md`), whose 8,000-word figure is a dispatch budget and not a limit on written
evidence (RD-122): nothing was trimmed, nothing was re-tiered on word count, and `gates.py --tier register`
therefore reports one budget finding on this volume, which is the adjudicated non-defect.

## Volumes in order

| # | File | Words | Bytes | Sections contained | Status |
|---|---|---|---|---|---|
| 1 | `stage_1.md` | 46,691 | 323,547 | merge header + Stage-1 merge note, then **Volume 1** (`_parts/s1_p1.md`: Header, Boundary 1–7, §A–§F, 27 claim records, 8 register emission blocks) and **Volume 2** (`_parts/s1_p2.md`: §G–§U, 32 claim records, 9 register emission blocks, the §U anchor block, the eleven-route `## Untried`) | merged 2026-09-30 |
| — | `_parts/s1_p1.md` | 16,233 as emitted (incl. footer) | 115,586 | superseded: carried verbatim into `stage_1.md` as Volume 1; **truncated at the end of its own emission footer with a stray `#`**, the promised `## Untried` absent | SUPERSEDED, DO NOT RE-APPLY notice present |
| — | `_parts/s1_p2.md` | 29,155 as emitted (incl. footer) | 199,359 | superseded: carried verbatim into `stage_1.md` as Volume 2 | SUPERSEDED, DO NOT RE-APPLY notice present |

**Carry-forward.** Volume 2 `## Untried` (eleven routes, each re-numbered with part 1 item numbers in
parentheses) is the volume register of untried routes and is the last section of `stage_1.md`. Volume 1 owed an
`## Untried` of its own and never wrote one; that block was **not** reconstructed by this merge (a merge may not
write a section a part left unwritten) — see the truncation inventory in `_MANIFEST.md` and in
`03_quality_control/nvidia_s1_merge_notes.md`, COR-03 in `CORRECTIONS.md`, and the coverage row minted into
`data_gaps.csv`.

## Anchors: eighteen declared, all eighteen covered

§U declares **18 anchors** — `U.101`–`U.118` — with a single declaration comment in Volume 2, which is the only
such declaration anywhere in the merged volume, so the whole set resolves across both parts. Parity: **18
narrative anchors ↔ 18 register anchors, 0 undeclared, 0 uncovered.**

| range | what it holds | register home |
|---|---|---|
| `U.101`–`U.110` | the FY1997 restatement identity, the four captions for two January months, Sunday-vs-calendar quarter labels, the July 26-vs-28 quarter end, the two-step fiscal-year change, the ST→TSMC foundry migration, the 63/31 denominator, the 28,565,226-vs-28,595,976 share identity, the conversion condition the assumed price does not satisfy, and the refutation of part 1 §Boundary 4 | `conflicts.csv` rows `P1K08`–`P1K16`; echoed in `quantitative.csv` notes, `timeline.csv` `conflict_ref`, `validation.csv` and `failures.csv` notes |
| `U.111`–`U.118` | the largest customer being acquired by a patent plaintiff, the NV2 sponsor and the 2,500 advance, notification-vs-filing dates of three suits, the one-US-segment statement against the operating geography, the uncarried rescue recollection, the first-customer perimeter, the two instruments never filed, the six blank-`primaryDocument` accessions | `data_gaps.csv` (7 rows), `timeline.csv` `conflict_ref`, `sources.csv` `claim_supported`, `channels.csv` notes |
| **part 1 conflicts without anchors** | `P1K01`–`P1K07` (the 1997 restatement as first filed, the Delaware sequence, the causal-ordering anomaly, the headcount mis-citation trap, the January-1997 footnote, the award-count escalation, the dossier-premise corrections) | `conflicts.csv` only. Their addresses live in part 1 §Boundary and §A–§F prose; the part-1 §U block is the section the truncation removed, so no anchor was minted for them — inventing one would be writing text part 1 never wrote |

## Registers (row counts measured on disk after the final write)

| register | rows | cols | provenance of the rows |
|---|---|---|---|
| `sources.csv` | 16 | 18 | global ids `S4353`–`S4368` (7 from part 1, 9 from part 2), each carrying its dossier-local alias in `notes` |
| `quantitative.csv` | 65 | 12 | 30 from part 1, 35 from part 2 |
| `timeline.csv` | 37 | 11 | 21 from part 1, 16 from part 2 |
| `conflicts.csv` | 17 | 15 | 7 from part 1, 9 from part 2, 1 minted here (`P1K17`) |
| `data_gaps.csv` | 21 | 8 | 10 from part 1, 10 from part 2, 1 minted here (the part-1 truncation coverage row) |
| `decisions.csv` | 7 | 15 | 3 from part 1, 4 from part 2 |
| `validation.csv` | 11 | 11 | 5 from part 1 + 6 from part 2, attributed by content from an AMBIGUOUS census group |
| `failures.csv` | 11 | 11 | 5 from part 1 + 6 from part 2, same attribution |
| `channels.csv` | 9 | 11 | 3 from part 1, 6 from part 2 |
| **total** | **194** | | **192 emitted + 2 minted; 0 dropped, 0 folded, 0 refused** |

## Six decisions this merge took, each reversible by a reader

1. **Nothing dropped from the AMBIGUOUS census group.** 22 of 192 rows could not be attributed by column
   overlap because `validation.csv` and `failures.csv` share all 11 names. Attribution was made by content, on
   the parts' own declarations, and the evidence for each of the four blocks is tabled in
   `03_quality_control/nvidia_s1_merge_notes.md`. Result: 11 + 11.
2. **Collision pairs kept, not folded.** Twelve groups (G-01…G-12 in `_MANIFEST.md`). Folding would have
   produced composite values neither pass emitted, and RD-131's one-measurement-recorded-twice case does not
   arise: in every pair the later row *adds* a fact. Where the later row refutes an earlier premise the earlier
   row is kept with the supersession printed inside it (G-01, G-03).
3. **Ids minted centrally, prose left alone.** `S4353`–`S4368` via `tools/id_mint.py --claim`; every register
   citation cell re-pointed; part prose keeps `P1Snn` and resolves through the alias table in the merge note. A
   four-digit token in the parts was *not* treated as an id (RD-131's OCR price).
4. **Truncation recorded, not repaired.** The missing part-1 route block is listed in four places and none of
   its items was invented here; the volume is not presented as a complete two-part merge but as a complete
   part-2 plus an incomplete part-1.
5. **Contradictions kept on both sides.** `P1K05` vs `P1K16`, `P1K01` vs `P1K08`, and part 2 against itself on
   the first-profitable-period claim (`P1K17` minted). Marked in-site at the two part-1 sentences affected.
6. **Residue named instead of patched.** `P1-38` is cited by part 2 and declared by neither part; part 1 cites
   `P1G06`/`P1G08` which match no emitted gap label. Both left as emitted and handed to the Stage-1 auditor
   (see `CORRECTIONS.md`, Residue section).
