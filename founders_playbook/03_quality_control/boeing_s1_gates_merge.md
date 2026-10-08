# Mechanical gate report -- company_047_boeing

Findings: **2** | Passes: 17

| gate | subject | finding |
|---|---|---|
| quotes | ADVISORY | 16 of 33 checked spans unmatched (48%) -- gate precision is not established, treat as a triage list, NOT as defects |
| advisory | stage_1.md | 34817 words over the core (this volume's issued tier) density target 22000 -- NOT a split mandate and NOT a defect; recorded so the tier is measurable |

- coverage 9 registers, 1 stage volumes, 62 source documents
- keys     stage_1.md mentions 7 retired keys inside collision/re-key/range text -- protected history, not re-pointed: S4222, S4229, S4407, S4422, S4479, S4494, S4509
- anchors  stage_1.md declares an explicit ANCHORS set (17 ids)
- anchors  stage_1.md declares 17 anchors
- anchors  5 id(s) read as backticked references or range endpoints, not citations (U.001, U.004, U.009, U.010, U.017)
- anchors  1 prose mention(s) match no declared entry, ADVISORY only: U.001b
- quotes   corpus: 10403191 chars of squashed local source text indexed
- quotes   candidates 399, attributed+checked 33, skipped 226, unmatched 16 (48%)
- quotes   unattributed spans unmatched: 140 (advisory, e.g. stage_1.md::to boeing aircraft company a washington corporation owned 100 by the addressee ii the federal record s4517 cal; stage_1.md::an in window name collision not a retrospective recital iii fy1938 prints)
- corrections no CORRECTIONS.md -- gate DID NOT RUN (not a pass)

## Passing checks

```
csv      timeline.csv                       42 rows x 11 cols
csv      timeline.csv.source_id             all S#### tokens resolve
csv      quantitative.csv                   75 rows x 12 cols
csv      conflicts.csv                      17 rows x 15 cols
csv      sources.csv                        19 rows x 18 cols
csv      data_gaps.csv                      18 rows x 8 cols
csv      validation.csv                     13 rows x 11 cols
csv      validation.csv.source_id           all S#### tokens resolve
csv      failures.csv                       9 rows x 11 cols
csv      failures.csv.source_id             all S#### tokens resolve
csv      decisions.csv                      11 rows x 15 cols
csv      decisions.csv.source_id            all S#### tokens resolve
csv      channels.csv                       7 rows x 11 cols
csv      channels.csv.source_id             all S#### tokens resolve
keys     stage_1.md                         19 source tokens all resolve
anchors  citation resolution                every register-cited anchor resolves (18 distinct ids across registers and volumes)
anchors  parity                             17 narrative anchors <-> 17 register anchors
```

## Evidence lines for findings

```
stage_1.md :: your company was formed for the purpose of acquiring these assets upon the dissolution of united aircraft tran
stage_1.md :: a boeing airplane company and edward hubbard georgetown station seattle washington at the rate of 1 50 per pou
stage_1.md :: i am transfer clerk on behalf of the united states government at the air field at cheyenne and know what mail 
stage_1.md :: i deliver the mail to the employee of the boeing company
stage_1.md :: flying boat six built in 1938 first flight
stage_1.md :: the university of washington in seattle now has under construction a large high speed wind tunnel the boeing a
stage_1.md :: j a greenwood attorney general of the state of wyoming
stage_1.md :: the fact is that united aircraft did not own varney air lines in august 1929 it was not until june 28 1930 alm
stage_1.md :: its enthusiastic acceptance in every field of air transportation has been a splendid tribute to its advanced d
stage_1.md :: contemplated expansion in engineering research and aerodynamics has been effected in 1940
stage_1.md :: by reason of the large development cost of new model aircraft it is necessary in order to meet competitive pri
stage_1.md :: an increase in the estimated cost to complete the stratoliners in the amount of 368 580 58 this additional los
stage_1.md :: on july 1 1937 however it became necessary to increase wages materially in excess of any wage rates previously
stage_1.md :: wage rate increases approximating eighteen per cent resulted from the new union agreement this increased labor
stage_1.md :: on or about february 1 1927 the then postmaster general awarded the contract
stage_1.md :: against the held fy1934 bytes the quotation changes
```
