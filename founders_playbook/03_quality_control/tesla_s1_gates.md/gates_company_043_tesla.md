# Mechanical gate report -- company_043_tesla

Findings: **2** | Passes: 20

| gate | subject | finding |
|---|---|---|
| quotes | ADVISORY | 16 of 58 checked spans unmatched (28%) -- gate precision is not established, treat as a triage list, NOT as defects |
| advisory | stage_1.md | 53553 words over the register density target 8000 -- NOT a split mandate and NOT a defect; recorded so the tier is measurable |

- coverage 9 registers, 2 stage volumes, 81 source documents
- keys     stage_1.md mentions 3 retired keys inside collision/re-key/range text -- protected history, not re-pointed: S0001, S0012, S435
- keys     stage_1_index.md mentions 2 retired keys inside collision/re-key/range text -- protected history, not re-pointed: S4222, S4225
- anchors  stage_1.md declares an explicit ANCHORS set (23 ids)
- anchors  stage_1.md declares 23 anchors
- anchors  15 id(s) read as backticked references or range endpoints, not citations (U.1, U.10, U.13, U.18, U.19, U.2, U.22, U.23)
- quotes   corpus: 20216162 chars of squashed local source text indexed
- quotes   candidates 360, attributed+checked 58, skipped 184, unmatched 16 (28%)
- quotes   unattributed spans unmatched: 118 (advisory, e.g. stage_1.md::do not occur in this volume the company s own 2009 2011 marketing sentences; stage_1.md::in may 2004 we entered into a license agreement with ac propulsion inc acp and obtained a nonexclusive nontran)
- corrections 6 retraction ids; register layer reaches 6, volumes 6

## Passing checks

```
csv      timeline.csv                       46 rows x 11 cols
csv      timeline.csv.source_id             all S#### tokens resolve
csv      quantitative.csv                   61 rows x 12 cols
csv      conflicts.csv                      23 rows x 15 cols
csv      sources.csv                        24 rows x 18 cols
csv      data_gaps.csv                      15 rows x 8 cols
csv      validation.csv                     9 rows x 11 cols
csv      validation.csv.source_id           all S#### tokens resolve
csv      failures.csv                       11 rows x 11 cols
csv      failures.csv.source_id             all S#### tokens resolve
csv      decisions.csv                      9 rows x 15 cols
csv      decisions.csv.source_id            all S#### tokens resolve
csv      channels.csv                       10 rows x 11 cols
csv      channels.csv.source_id             all S#### tokens resolve
keys     stage_1.md                         8 source tokens all resolve
keys     stage_1_index.md                   2 source tokens all resolve
anchors  citation resolution                every register-cited anchor resolves (23 distinct ids across registers and volumes)
anchors  parity                             23 narrative anchors <-> 23 register anchors
budget   stage_1_index.md                   1564 words (target 8000, hard cap 60000)
corrections propagation                        all 6 retraction(s) reach registers and volumes
```

## Evidence lines for findings

```
stage_1.md :: until that edit happens a green anchors result means the six live rows are declared not that the conflict set 
stage_1.md :: tesla motors inc was incorporated in the state of delaware on july 1 2003
stage_1.md :: the term tesla store means tesla retail locations as well as tesla galleries where we show potential customers
stage_1.md :: competition from other luxury performance automobile brands in our target market including audi bmw lexus and 
stage_1.md :: virtually all of our competitors have more extensive customer bases and broader customer and industry relation
stage_1.md :: we note your rule 83 letter requesting confidentiality for your response to comment of our last letter we will
stage_1.md :: 236 miles on a single charge as determined using the united states environmental protection agency s combined 
stage_1.md :: it has not entered into any agreements with daimler or freightliner with respect to these transactions however
stage_1.md :: we note your rule 83 letter requesting confidentiality for your response to comment of our last letter we will
stage_1.md :: in 2009 s fourth quarter the company s stock based compensation expense was understated by 2 7 million due to 
stage_1.md :: we will correct the error in the three months ending june 30 2010
stage_1.md :: event subsequent to the date of independent registered accountant s report unaudited
stage_1.md :: your traditional practices of collecting refundable reservation deposits and receiving full upfront payment ha
stage_1.md :: we cannot access all of these funds at once
stage_1.md :: three held exhibits and only three are contemporaneous documents
stage_1.md :: pages 31 and 108 109 of amendment no 2
```
