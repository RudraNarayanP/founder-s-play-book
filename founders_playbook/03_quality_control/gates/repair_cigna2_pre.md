# Mechanical gate report -- company_014_cigna

Findings: **2** | Passes: 18

| gate | subject | finding |
|---|---|---|
| keys | stage_1.md | unresolvable source tokens: S4529, S4530 |
| corrections | registers | 9 retraction(s) reach the prose but NOT any register, so the register layer still teaches the withdrawn claim: COR-04, COR-05, COR-06, COR-07, COR-08, COR-09, COR-10, COR-11, COR-12 |

- coverage 9 registers, 1 stage volumes, 43 source documents
- keys     stage_1.md mentions 5 retired keys inside collision/re-key/range text -- protected history, not re-pointed: S0001, S4222, S4229, S4393, S4406
- anchors  stage_1.md declares an explicit ANCHORS set (6 ids)
- anchors  stage_1.md declares 6 anchors
- anchors  2 id(s) read as backticked references or range endpoints, not citations (U.1, U.2)
- quotes   corpus: 9956365 chars of squashed local source text indexed (+ 122375 chars of project-internal text from 8 research/method/brief files, second-class)
- quotes   candidates 101, attributed+checked 5, skipped 77, unmatched 0 (0%), matched-in-project-text-only 1
- quotes   unattributed spans unmatched: 19 (advisory, e.g. stage_1.md::product families property casualty life and group health care investment management headquarters; stage_1.md::halfmoon parent inc exact name of registrant as specified in its certificate of incorporation delaware 82 4991)
- corrections 12 retraction ids; register layer reaches 3, volumes 12

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
anchors  citation resolution                every register-cited anchor resolves (6 distinct ids across registers and volumes)
anchors  parity                             6 narrative anchors <-> 6 register anchors
quotes   verbatim                           5 quoted spans all present in local sources
budget   stage_1.md                         16812 words (tier T2 target 22000, hard cap 60000)
```
