# Mechanical gate report -- company_012_jpmorgan

Findings: **2** | Passes: 17

| gate | subject | finding |
|---|---|---|
| quotes | verbatim | 4 of 24 quoted spans not found in local sources |
| advisory | stage_1.md | 34641 words over the T2 (this volume's issued tier) density target 22000 -- NOT a split mandate and NOT a defect; recorded so the tier is measurable |

- coverage 9 registers, 1 stage volumes, 78 source documents
- keys     stage_1.md mentions 6 retired keys inside collision/re-key/range text -- protected history, not re-pointed: S0001, S4222, S4229, S4528, S4529, S4530
- anchors  stage_1.md declares an explicit ANCHORS set (13 ids)
- anchors  stage_1.md declares 13 anchors
- anchors  5 id(s) read as backticked references or range endpoints, not citations (U.001, U.003, U.005, U.010, U.013)
- quotes   corpus: 9198170 chars of squashed local source text indexed (+ 131483 chars of project-internal text from 8 research/method/brief files, second-class)
- quotes   candidates 417, attributed+checked 24, skipped 327, unmatched 4 (17%), matched-in-project-text-only 6
- quotes   unattributed spans unmatched: 66 (advisory, e.g. stage_1.md::petition for a water charter carrying a surplus capital clause; stage_1.md::no corrections md gate did not run)
- corrections no CORRECTIONS.md -- gate DID NOT RUN (not a pass)

## Passing checks

```
csv      timeline.csv                       61 rows x 11 cols
csv      timeline.csv.source_id             all S#### tokens resolve
csv      quantitative.csv                   52 rows x 12 cols
csv      conflicts.csv                      13 rows x 15 cols
csv      sources.csv                        23 rows x 18 cols
csv      data_gaps.csv                      15 rows x 8 cols
csv      validation.csv                     14 rows x 11 cols
csv      validation.csv.source_id           all S#### tokens resolve
csv      failures.csv                       10 rows x 11 cols
csv      failures.csv.source_id             all S#### tokens resolve
csv      decisions.csv                      17 rows x 15 cols
csv      decisions.csv.source_id            all S#### tokens resolve
csv      channels.csv                       9 rows x 11 cols
csv      channels.csv.source_id             all S#### tokens resolve
keys     stage_1.md                         9 source tokens all resolve
anchors  citation resolution                every register-cited anchor resolves (13 distinct ids across registers and volumes)
anchors  parity                             13 narrative anchors <-> 13 register anchors
```

## Evidence lines for findings

```
stage_1.md :: supply the double quote pairs around the bracketed phrases on merge never backslash escapes
stage_1.md :: an american bank offering complete foreign banking service in the principal markets of the world
stage_1.md :: there are nine banks now in existence whose history reaches back into the eighteenth century two are in massac
stage_1.md :: john pierpoint morgan the american financial magnate who left flushing in belgium has arrived in gdynia
```
