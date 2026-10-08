# Mechanical gate report -- company_006_cvs

Findings: **2** | Passes: 19

| gate | subject | finding |
|---|---|---|
| csv | quantitative.csv | source_date carries no four-digit year: ['-'] |
| quotes | verbatim | 1 of 11 quoted spans not found in local sources |

- coverage 9 registers, 1 stage volumes, 54 source documents
- keys     stage_1.md cites 1 hyphenated record keys: S3-97
- keys     stage_1.md mentions 4 retired keys inside collision/re-key/range text -- protected history, not re-pointed: S4222, S4229, S4423, S4430
- anchors  stage_1.md declares an explicit ANCHORS set (10 ids)
- anchors  stage_1.md declares 10 anchors
- anchors  3 id(s) read as backticked references or range endpoints, not citations (U.01, U.04, U.10)
- quotes   corpus: 16820546 chars of squashed local source text indexed
- quotes   candidates 103, attributed+checked 11, skipped 64, unmatched 1 (9%)
- quotes   unattributed spans unmatched: 28 (advisory, e.g. stage_1.md::0 rows of s 1 s 1 a sb 2 10 a in 2 968 is the proof 2 corporate print shelf is not family d u 08 four files ar; stage_1.md::stays company claim retrospective medium one lineage the shoe store jacksonville consumer value as 1963 entity)
- corrections 4 retraction ids; register layer reaches 4, volumes 4

## Passing checks

```
csv      timeline.csv                       24 rows x 11 cols
csv      timeline.csv.source_id             all S#### tokens resolve
csv      quantitative.csv                   29 rows x 12 cols
csv      conflicts.csv                      10 rows x 15 cols
csv      sources.csv                        18 rows x 18 cols
csv      data_gaps.csv                      10 rows x 8 cols
csv      validation.csv                     8 rows x 11 cols
csv      validation.csv.source_id           all S#### tokens resolve
csv      failures.csv                       7 rows x 11 cols
csv      failures.csv.source_id             all S#### tokens resolve
csv      decisions.csv                      14 rows x 15 cols
csv      decisions.csv.source_id            all S#### tokens resolve
csv      channels.csv                       6 rows x 11 cols
csv      channels.csv.source_id             all S#### tokens resolve
keys     stage_1.md                         18 source tokens all resolve
anchors  citation resolution                every register-cited anchor resolves (10 distinct ids across registers and volumes)
anchors  parity                             10 narrative anchors <-> 10 register anchors
budget   stage_1.md                         19520 words (target 22000, hard cap 60000)
corrections propagation                        all 4 retraction(s) reach registers and volumes
```

## Evidence lines for findings

```
stage_1.md :: to support this growth cvs increased distribution capacity by a 400 000 square foot dc in new jersey that rais
```
