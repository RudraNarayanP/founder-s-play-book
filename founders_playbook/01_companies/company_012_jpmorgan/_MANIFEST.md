# _MANIFEST — company_012_jpmorgan (Stage 1)

**Counts regenerated 2026-10-14** by `merge-jpmorgan-finish` after the last write to `stage_1.md` (word =
whitespace-delimited tokens, the same count `gates.py` printed; byte = file size; register rows counted with
`csv.reader`, not by line). Re-measure before quoting any of these again. This manifest is bookkeeping for a
merge that was already on disk. It is **not an audit and not a certification**.

## Which ceiling governs which file

- §9.2's **60,000-word hard cap** is the only word count that is a defect. `stage_1.md` is **34,641 words**,
  under that cap. No split was performed.
- The probe issues Stage 1 as **T2 core, 22,000 words**. 34,641 is over that density target. `gates.py --tier
  auto` read T2 and recorded the overage as **advisory**, not a defect. Nothing was trimmed to meet it.
- The nine registers are not stage volumes. None is near a cap.

## Deliverables

| File | Words | Bytes | Contents | Status |
|---|---|---|---|---|
| `stage_1.md` | **34,641** | 219,012 | Merger's MERGE RECORD, then the author's Header through §U, applied-register pointer, UNTRIED / fetch appendix. **13 anchors U.001–U.013** declared at the HTML comment on line 174 | MERGED 2026-10-07; preamble corrected 2026-10-14 |
| `stage_1_claim_records.md` | 3,507 | 22,487 | Claim records J01–J32, moved at the §U boundary | Applied with the merge; not edited this pass |
| `CORRECTIONS.md` | — | — | **Not seeded.** The 2026-10-07 merger recorded why: no `data_gaps` row asks for the file, and the probe-transcription notes already live in §T.2 and in register note cells. `gates.py` therefore reports `no CORRECTIONS.md -- gate DID NOT RUN (not a pass)`. Creating an empty file would change that coverage note into an unanswered register. | Intentionally absent |

`_parts/s1_p1.md` is **read-only** (47,463 words, 327,197 bytes) and remains the emission of record for the 214
provisional rows. `_parts/NOTES_jpmorgan_p1.md` is 2,954 words.

## Registers (nine CSVs at this directory root — 214 data rows)

| register | cols | data rows | rows the part requested | key / integrity | words | bytes |
|---|---|---|---|---|---|---|
| `sources.csv` | 18 | **23** | 23 | S4531–S4553, 0 duplicate keys, 0 `PROV-*` | 2,011 | 20,855 |
| `quantitative.csv` | 12 | **52** | 52 | 0 duplicate `(date, metric)` in the merger's own check | 1,407 | 13,167 |
| `timeline.csv` | 11 | **61** | 61 | — | 2,155 | 18,138 |
| `conflicts.csv` | 15 | **13** | 13 | U.001–U.013 | 1,918 | 13,850 |
| `data_gaps.csv` | 8 | **15** | 15 | — | 1,032 | 7,811 |
| `decisions.csv` | 15 | **17** | 17 | — | 1,324 | 10,262 |
| `validation.csv` | 11 | **14** | 14 | adjudicated by block heading; census cannot attribute | 811 | 6,286 |
| `failures.csv` | 11 | **10** | 10 | adjudicated by block heading; 0 rows shared with validation | 533 | 4,109 |
| `channels.csv` | 11 | **9** | 9 | — | 491 | 3,968 |
| **TOTAL** | — | **214** | **214** | **0 withheld, 0 added this pass** | — | — |

Headers match `company_001_amazon/` (the 2026-10-07 merger compared them column for column). Every `stage`
cell is the literal `stage1`. Line endings on these nine files are LF. **S4551 and S4552 still have empty
`tier` cells**, as the merger left them: both rows are instrument indexes the author refused to tier.

## Id block — already minted, not minted again

`founders_playbook/00_universe/_ID_BLOCKS.tsv` already held **S4531–S4553** for `company_012_jpmorgan` /
`merge-jpmorgan`, and `sources.csv` already used those keys. This pass did **not** call `id_mint.py --claim`.
The part's `PROV-JP1-01`…`PROV-JP1-23` stay in `_parts/s1_p1.md` on purpose. `merge_census.py` still prints
`sources.csv requested 23 / missing 23` on those provisional keys. That reading is the re-mint, not 23 lost
rows. Binding, as the volume's id map states: `PROV-JP1-nn` → `S(4530+nn)`.

## Five families

The volume's own `## UNTRIED (this pass) AND FETCH REQUESTS` table is the statement. This manifest does not
re-tier it. In short, as that table has it: (a) filings are a **perimeter** (EDGAR floor 1994, nothing in
1799–1955); (c) periodicals and (d) digitised corporate print are the two families the probe counted for T2;
(b) web archives are **UNTRIED** (no `jpmorgan` slug in `tools/web_domains.json`); (e) auction/museum is
**UNTRIED and has no tool**.

## Gates

`founders_playbook/03_quality_control/jpmorgan_s1_gates_merge.md`, re-run 2026-10-14 with `--tier auto`.
Anchors 13↔13 and keys pass. One substantive finding remains: `quotes` / `verbatim`, 4 of 24 spans. Named in
the merge report. Not rewritten.
