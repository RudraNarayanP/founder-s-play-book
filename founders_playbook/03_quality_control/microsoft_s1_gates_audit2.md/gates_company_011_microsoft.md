# Mechanical gate report -- company_011_microsoft

Findings: **1** | Passes: 21

| gate | subject | finding |
|---|---|---|
| quotes | ADVISORY | 11 of 13 checked spans unmatched (85%) -- gate precision is not established, treat as a triage list, NOT as defects |

- coverage 9 registers, 2 stage volumes, 31 source documents
- keys     stage_1.md mentions 2 retired keys inside collision/re-key/range text -- protected history, not re-pointed: S4221, S435
- keys     stage_1_index.md mentions 4 retired keys inside collision/re-key/range text -- protected history, not re-pointed: S4201, S4221, S4301, S4331
- anchors  stage_1.md declares an explicit ANCHORS set (14 ids)
- anchors  stage_1.md declares 14 anchors
- anchors  11 id(s) read as backticked references or range endpoints, not citations (U.1, U.11, U.12, U.13, U.14, U.15, U.2, U.3)
- quotes   corpus: 11579621 chars of squashed local source text indexed
- quotes   candidates 168, attributed+checked 13, skipped 109, unmatched 11 (85%)
- quotes   unattributed spans unmatched: 46 (advisory, e.g. stage_1.md::almost a year ago paul allen and myself expecting the hobby market to expand hired monte davidoff and develope; stage_1.md::microsoft consumer products a sibling company to the microsoft that has written so many versions of basic has )
- corrections 5 retraction ids; register layer reaches 5, volumes 5

## Passing checks

```
csv      timeline.csv                       28 rows x 11 cols
csv      timeline.csv.source_id             all S#### tokens resolve
csv      quantitative.csv                   26 rows x 12 cols
csv      conflicts.csv                      14 rows x 15 cols
csv      sources.csv                        22 rows x 18 cols
csv      data_gaps.csv                      13 rows x 8 cols
csv      validation.csv                     7 rows x 11 cols
csv      validation.csv.source_id           all S#### tokens resolve
csv      failures.csv                       5 rows x 11 cols
csv      failures.csv.source_id             all S#### tokens resolve
csv      decisions.csv                      5 rows x 15 cols
csv      decisions.csv.source_id            all S#### tokens resolve
csv      channels.csv                       7 rows x 11 cols
csv      channels.csv.source_id             all S#### tokens resolve
keys     stage_1.md                         22 source tokens all resolve
keys     stage_1_index.md                   22 source tokens all resolve
anchors  citation resolution                every register-cited anchor resolves (15 distinct ids across registers and volumes)
anchors  parity                             14 narrative anchors <-> 14 register anchors
budget   stage_1.md                         34707 words (cap 60000)
budget   stage_1_index.md                   1085 words (cap 60000)
corrections propagation                        all 5 retraction(s) reach registers and volumes
```

## Evidence lines for findings

```
stage_1.md :: unverified tls re check before citing at high confidence
stage_1.md :: hobby computer is wasted will q iality software be written for the hobby market
stage_1.md :: the only mits software we have ever reproduced
stage_1.md :: 2 hr is what they re worth on the free market
stage_1.md :: unverified tls re check before citing at high confidence
stage_1.md :: a letter arrived from bill gates via mits
stage_1.md :: now we have 4k 8k extended rom and disk basic
stage_1.md :: we have written 6800 basic and are writing 8080 apl and 6800 apl
stage_1.md :: all you need is an apple ii or apple ii plus with 48k ram 2 drives the microsoft z 80 softcard dos 3 3 and a 1
stage_1.md :: i am one of the 10 minority who paid for altair 8k basic
stage_1.md :: at this price software is sold as is without support
```
