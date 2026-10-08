# Mechanical gate report -- company_023_gm

Findings: **1** | Passes: 19

| gate | subject | finding |
|---|---|---|
| quotes | ADVISORY | 10 of 24 checked spans unmatched (42%) -- gate precision is not established, treat as a triage list, NOT as defects |

- coverage 9 registers, 1 stage volumes, 49 source documents
- keys     stage_1.md mentions 4 retired keys inside collision/re-key/range text -- protected history, not re-pointed: S0001, S4222, S4229, S4422
- anchors  stage_1.md declares an explicit ANCHORS set (10 ids)
- anchors  stage_1.md declares 10 anchors
- anchors  2 id(s) read as backticked references or range endpoints, not citations (U.01, U.09)
- quotes   corpus: 23152587 chars of squashed local source text indexed
- quotes   candidates 254, attributed+checked 24, skipped 165, unmatched 10 (42%)
- quotes   unattributed spans unmatched: 65 (advisory, e.g. stage_1.md::the stringent terms exacted by the banking syndicate offer abundant testimony of the uncertain speculative cha; stage_1.md::note general motors corporation of delaware was incorporated october 13 1916 succeeding general motors company)
- corrections 9 retraction ids; register layer reaches 9, volumes 9

## Passing checks

```
csv      timeline.csv                       30 rows x 11 cols
csv      timeline.csv.source_id             all S#### tokens resolve
csv      quantitative.csv                   26 rows x 12 cols
csv      conflicts.csv                      10 rows x 15 cols
csv      sources.csv                        8 rows x 18 cols
csv      data_gaps.csv                      13 rows x 8 cols
csv      validation.csv                     6 rows x 11 cols
csv      validation.csv.source_id           all S#### tokens resolve
csv      failures.csv                       8 rows x 11 cols
csv      failures.csv.source_id             all S#### tokens resolve
csv      decisions.csv                      8 rows x 15 cols
csv      decisions.csv.source_id            all S#### tokens resolve
csv      channels.csv                       5 rows x 11 cols
csv      channels.csv.source_id             all S#### tokens resolve
keys     stage_1.md                         8 source tokens all resolve
anchors  citation resolution                every register-cited anchor resolves (10 distinct ids across registers and volumes)
anchors  parity                             10 narrative anchors <-> 10 register anchors
budget   stage_1.md                         20192 words (target 22000, hard cap 60000)
corrections propagation                        all 9 retraction(s) reach registers and volumes
```

## Evidence lines for findings

```
stage_1.md :: deliberately wide where the founding date is itself unestablished
stage_1.md :: the ambitious merger and combination projects that marked the history of the general motors enterprise up to 1
stage_1.md :: the naming wall for gm is therefore 1920 for a document that names and 1908 for a date asserted and those are 
stage_1.md :: late in november last william c durant then president of the general motors corporation requested that we take
stage_1.md :: for 1 827 694 of general motors preferred stock 1 195 880 of common and 17 279 in cash
stage_1.md :: the general motors corporation purchased 300 000 newly issued shares of no par value of the fisher body corpor
stage_1.md :: the corporation organized a subsidiary the general motors building corporation which sold to s w strauss co an
stage_1.md :: i picked him to be head of general motors in five years he turned a wreck into a concern having 25 000 000 in 
stage_1.md :: on 96 and interest with a 20 per cent stock bonus
stage_1.md :: the present general motors corporation was incorporated under the laws of delaware on october 13 1916
```
