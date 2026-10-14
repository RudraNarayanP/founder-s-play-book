# Mechanical gate report -- company_014_cigna

Findings: **0** | Passes: 20

- coverage 9 registers, 1 stage volumes, 43 source documents
- keys     stage_1.md mentions 5 retired keys inside collision/re-key/range text -- protected history, not re-pointed: S0001, S4222, S4229, S4393, S4406
- anchors  stage_1.md declares an explicit ANCHORS set (6 ids)
- anchors  stage_1.md declares 6 anchors
- anchors  2 id(s) read as backticked references or range endpoints, not citations (U.1, U.2)
- quotes   corpus: 10403673 chars of squashed local source text indexed (+ 123640 chars of project-internal text from 8 research/method/brief files, second-class)
- quotes   candidates 102, attributed+checked 6, skipped 78, unmatched 0 (0%), matched-in-project-text-only 1
- quotes   unattributed spans unmatched: 18 (advisory, e.g. stage_1.md::product families property casualty life and group health care investment management headquarters; stage_1.md::halfmoon parent inc exact name of registrant as specified in its certificate of incorporation delaware 82 4991)
- corrections 12 retraction ids; register layer reaches 12, volumes 12

## Passing checks

```
csv      timeline.csv                       14 rows x 11 cols
csv      timeline.csv.source_id             all S#### tokens resolve
csv      quantitative.csv                   15 rows x 12 cols
csv      conflicts.csv                      6 rows x 15 cols
csv      sources.csv                        18 rows x 18 cols
csv      data_gaps.csv                      12 rows x 8 cols
csv      validation.csv                     4 rows x 11 cols
csv      validation.csv.source_id           all S#### tokens resolve
csv      failures.csv                       7 rows x 11 cols
csv      failures.csv.source_id             all S#### tokens resolve
csv      decisions.csv                      3 rows x 15 cols
csv      decisions.csv.source_id            all S#### tokens resolve
csv      channels.csv                       2 rows x 11 cols
csv      channels.csv.source_id             all S#### tokens resolve
keys     stage_1.md                         18 source tokens all resolve
anchors  citation resolution                every register-cited anchor resolves (6 distinct ids across registers and volumes)
anchors  parity                             6 narrative anchors <-> 6 register anchors
quotes   verbatim                           6 quoted spans all present in local sources
budget   stage_1.md                         16948 words (tier T2 target 22000, hard cap 60000)
corrections propagation                        all 12 retraction(s) reach registers and volumes
```
