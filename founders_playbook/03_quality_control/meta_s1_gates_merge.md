# Mechanical gate report -- company_017_meta

Findings: **2** | Passes: 18

| gate | subject | finding |
|---|---|---|
| quotes | ADVISORY | 10 of 35 checked spans unmatched (29%) -- gate precision is not established, treat as a triage list, NOT as defects |
| advisory | stage_1.md | 30212 words over the core (this volume's issued tier) density target 22000 -- NOT a split mandate and NOT a defect; recorded so the tier is measurable |

- coverage 9 registers, 1 stage volumes, 43 source documents
- keys     stage_1.md mentions 5 retired keys inside collision/re-key/range text -- protected history, not re-pointed: S0001, S4222, S4229, S4449, S4462
- anchors  stage_1.md declares an explicit ANCHORS set (8 ids)
- anchors  stage_1.md declares 8 anchors
- anchors  6 id(s) read as backticked references or range endpoints, not citations (U.1, U.4, U.5, U.6, U.7, U.8)
- quotes   corpus: 15233162 chars of squashed local source text indexed
- quotes   candidates 211, attributed+checked 35, skipped 123, unmatched 10 (29%)
- quotes   unattributed spans unmatched: 53 (advisory, e.g. stage_1.md::no edgar document can ever fix the founding day; stage_1.md::in the mail ru dst conversion amendment never described not a founder not a litigant and the probe s blanket)
- corrections 9 retraction ids; register layer reaches 9, volumes 9

## Passing checks

```
csv      timeline.csv                       23 rows x 11 cols
csv      timeline.csv.source_id             all S#### tokens resolve
csv      quantitative.csv                   36 rows x 12 cols
csv      conflicts.csv                      8 rows x 15 cols
csv      sources.csv                        15 rows x 18 cols
csv      data_gaps.csv                      13 rows x 8 cols
csv      validation.csv                     8 rows x 11 cols
csv      validation.csv.source_id           all S#### tokens resolve
csv      failures.csv                       8 rows x 11 cols
csv      failures.csv.source_id             all S#### tokens resolve
csv      decisions.csv                      5 rows x 15 cols
csv      decisions.csv.source_id            all S#### tokens resolve
csv      channels.csv                       4 rows x 11 cols
csv      channels.csv.source_id             all S#### tokens resolve
keys     stage_1.md                         15 source tokens all resolve
anchors  citation resolution                every register-cited anchor resolves (8 distinct ids across registers and volumes)
anchors  parity                             8 narrative anchors <-> 8 register anchors
corrections propagation                        all 9 retraction(s) reach registers and volumes
```

## Evidence lines for findings

```
stage_1.md :: deliberately wide where the founding date is itself unestablished
stage_1.md :: facebook inc 2005 stock plan as amended april 2006 as amended july 2006 as amended january 200
stage_1.md :: no edgar document can ever fix the founding day for this company
stage_1.md :: in 2004 and 2005 mr zuckerberg s father provided us with initial working capital
stage_1.md :: walmart u s purchased advertising on facebook targeting users in the united states between the ages of 18 and 
stage_1.md :: this prospectus contains estimates and information concerning our industry based on industry publications and 
stage_1.md :: we estimate that false or duplicate accounts may have represented approximately 5 6 of our maus as of december
stage_1.md :: twitter google s social media properties including orkut buzz google me or other properties with similar funct
stage_1.md :: no edgar document can ever fix the founding day
stage_1.md :: a row you cannot attribute to a register is worse than a paragraph
```
