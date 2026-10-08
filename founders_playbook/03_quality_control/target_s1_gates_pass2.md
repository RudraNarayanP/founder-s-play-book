# Mechanical gate report -- company_042_target

Findings: **1** | Passes: 21

| gate | subject | finding |
|---|---|---|
| quotes | ADVISORY | 2 of 2 checked spans unmatched (100%) -- gate precision is not established, treat as a triage list, NOT as defects |

- coverage 9 registers, 2 stage volumes, 17 source documents
- anchors  stage_1.md declares an explicit ANCHORS set (37 ids)
- anchors  stage_1.md declares 37 anchors
- anchors  42 id(s) read as backticked references or range endpoints, not citations (U.0, U.001, U.002, U.003, U.004, U.005, U.006, U.007)
- anchors  2 prose mention(s) match no declared entry, ADVISORY only: U.3, U.4
- quotes   corpus: 943215 chars of squashed local source text indexed
- quotes   candidates 41, attributed+checked 2, skipped 24, unmatched 2 (100%)
- quotes   unattributed spans unmatched: 15 (advisory, e.g. stage_1.md::premise is refuted the layer labelled fy1965 reports the year ended 1966 01 29 b1 s q20 is re based by superse; stage_1.md::route most likely to lift the tier from t2 to t1)
- corrections 20 retraction ids; register layer reaches 20, volumes 20

## Passing checks

```
csv      timeline.csv                       24 rows x 11 cols
csv      timeline.csv.source_id             all S#### tokens resolve
csv      quantitative.csv                   72 rows x 12 cols
csv      conflicts.csv                      18 rows x 15 cols
csv      sources.csv                        25 rows x 18 cols
csv      data_gaps.csv                      22 rows x 8 cols
csv      validation.csv                     4 rows x 11 cols
csv      validation.csv.source_id           all S#### tokens resolve
csv      failures.csv                       1 rows x 11 cols
csv      failures.csv.source_id             all S#### tokens resolve
csv      decisions.csv                      3 rows x 15 cols
csv      decisions.csv.source_id            all S#### tokens resolve
csv      channels.csv                       3 rows x 11 cols
csv      channels.csv.source_id             all S#### tokens resolve
keys     stage_1.md                         10 source tokens all resolve
keys     stage_1_index.md                   21 source tokens all resolve
anchors  citation resolution                every register-cited anchor resolves (44 distinct ids across registers and volumes)
anchors  parity                             37 narrative anchors <-> 37 register anchors
budget   stage_1.md                         41534 words (cap 60000)
budget   stage_1_index.md                   1243 words (cap 60000)
corrections propagation                        all 20 retraction(s) reach registers and volumes
```

## Evidence lines for findings

```
stage_1.md :: source id blocks are assigned centrally at merge never per dossier
stage_1.md :: fiscal year calendar year in these reports
```

