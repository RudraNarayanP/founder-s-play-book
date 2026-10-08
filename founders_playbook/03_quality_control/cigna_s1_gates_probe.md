# Mechanical gate report -- company_014_cigna

Findings: **1** | Passes: 18

| gate | subject | finding |
|---|---|---|
| quotes | verbatim | 1 of 5 quoted spans not found in local sources |

- coverage 9 registers, 1 stage volumes, 43 source documents
- keys     stage_1.md mentions 5 retired keys inside collision/re-key/range text -- protected history, not re-pointed: S0001, S4222, S4229, S4393, S4406
- anchors  stage_1.md declares an explicit ANCHORS set (6 ids)
- anchors  stage_1.md declares 6 anchors
- anchors  2 id(s) read as backticked references or range endpoints, not citations (U.1, U.2)
- quotes   corpus: 9956365 chars of squashed local source text indexed
- quotes   candidates 91, attributed+checked 5, skipped 66, unmatched 1 (20%)
- quotes   unattributed spans unmatched: 20 (advisory, e.g. stage_1.md::product families property casualty life and group health care investment management headquarters; stage_1.md::at a 23 annual compound rate compared with 9 growth for the overall field)
- corrections CORRECTIONS.md exists but names no COR-nn ids -- UNANSWERED

## Passing checks

```
csv      timeline.csv                       14 rows x 11 cols
csv      timeline.csv.source_id             all S#### tokens resolve
csv      quantitative.csv                   15 rows x 12 cols
csv      conflicts.csv                      6 rows x 15 cols
csv      sources.csv                        16 rows x 18 cols
csv      data_gaps.csv                      12 rows x 8 cols
csv      validation.csv                     4 rows x 11 cols
csv      validation.csv.source_id           all S#### tokens resolve
csv      failures.csv                       6 rows x 11 cols
csv      failures.csv.source_id             all S#### tokens resolve
csv      decisions.csv                      3 rows x 15 cols
csv      decisions.csv.source_id            all S#### tokens resolve
csv      channels.csv                       2 rows x 11 cols
csv      channels.csv.source_id             all S#### tokens resolve
keys     stage_1.md                         16 source tokens all resolve
anchors  citation resolution                every register-cited anchor resolves (6 distinct ids across registers and volumes)
anchors  parity                             6 narrative anchors <-> 6 register anchors
budget   stage_1.md                         14168 words (target 22000, hard cap 60000)
```

## Evidence lines for findings

```
stage_1.md :: 96 candidate rows in the harvest index 12 items mined 81 left untried at the limit
```
