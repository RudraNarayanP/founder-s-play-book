# Cigna Stage 1 — repair close-out

**Agent:** `repair-cigna-finish` (2026-10-14). Not the author, not the merger, not the auditor, and not a
certifier. Web calls: 0. No id was minted. S4529 and S4530 were already in `00_universe/_ID_BLOCKS.tsv`
under `repair-cigna`.

## What was already done, and what was not

`CORRECTIONS.md` COR-04…COR-12 and most of the volume's prose were written on 2026-10-06. The live
registers were not. Before this pass:

- `timeline.csv` still dated Halfmoon Parent's birth `UNKNOWN` and said "no held byte prints it".
- `data_gaps.csv` row 1 still said "No held byte".
- `conflicts.csv` U.1 still said the incorporation date "is printed nowhere".
- `sources.csv` had 16 rows, S4407–S4422. S4529 and S4530 were cited in the volume and unresolved.
- `failures.csv` had 6 rows. The annuity row named in COR-07 was not there.
- `gates.py --checks corrections` reported COR-04…COR-12 in the prose and in no register.
- `cigna_s1_repairs.md` was the scaffold stub.

The held byte was re-read before any edit. `sources/sec/0001140361-18-024107_s002268x1_s4.htm` line 48371
prints `(Originally incorporated on March 6, 2018 under the name Halfmoon Parent, Inc.)`. Line 5011 prints
`New Cigna was incorporated on March 6, 2018`. The CIA lines COR-08 cites are on disk (rdp90g l.1431 and
l.1436; rdp91 l.1071). The annuity sentence is `INAC2115_1979_djvu.txt` l.1754.

`_parts/s1_p1.md` still carries the withdrawn sentences. It is the author's emission and was not edited.

## What this pass wrote

- Timeline birth row: `2018-03-06`, FACT, source S4407, COR-04. The 1979 report row's notes record that the
  Healthplan sentence completes at l.2012–2019 (COR-06).
- `data_gaps.csv` incorporation row: answered from the held form; FR-2 narrowed. The trade-press row now
  separates the `PPO` archive null from the out-of-window `managed care` hits (COR-05) and names the
  96−12≠81 non-closure (COR-10).
- `conflicts.csv` U.1 interpretation and residual updated. The "printed nowhere" form is withdrawn in the cell.
- `failures.csv` row 7: annuity revenues −5% to $195.8 million, S4410, COR-07.
- `sources.csv` S4529 (naming, l.1436) and S4530 (surname decoy, l.1071). S4407's note records 20 files, not
  23, and the five `managed care` lines. S4417's passage is labelled a two-locator composite (COR-09). S4421
  names the census non-closure.
- `decisions.csv` has no `notes` column. COR-11 is on row 1's `claim_ref`. The estimate row and the 1792
  census row in `quantitative.csv` carry COR-11 and COR-10.
- Three live sentences the prose repair had missed: §R's "date-unknown", §U.1's "no held byte gives", and
  claim record A02. Each is withdrawn in place, not deleted. `stage_1_index.md` U.1 matches.
- The volume's own "79 rows" did not add. 18+15+14+12+6+7+4+3+2 = **81**. That sentence now says 81.
- `_MANIFEST.md`: NOTES word count 1,003 → measured **1,111** (7,830 bytes unchanged). Sources and failures
  rows republished at the post-repair measurement (sources 1,068 words / 10,953 bytes / 18 rows; failures
  298 words / 2,709 bytes / 7 rows).

## Gate

`python tools/gates.py --company-dir founders_playbook/01_companies/company_014_cigna --tier auto --out founders_playbook/03_quality_control/cigna_s1_gates_repair2.md --fail-on substantive`

Exit **0**. Findings **0**. Corrections: 12 ids, registers 12, volumes 12. Keys: 18 source tokens resolve.
Anchors 6↔6. Quotes: 6 checked, 0 unmatched. `stage_1.md` is **16,948 words**, under the T2 target and under
the 60,000-word cap.

This is not a certification. A certifier has to be someone who did not repair it.
