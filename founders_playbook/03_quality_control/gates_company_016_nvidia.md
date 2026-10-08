# Mechanical gate report -- company_016_nvidia

Findings: **2** | Passes: 20

| gate | subject | finding |
|---|---|---|
| quotes | ADVISORY | 18 of 66 checked spans unmatched (27%) -- gate precision is not established, treat as a triage list, NOT as defects |
| advisory | stage_1.md | 46691 words over the register density target 8000 -- NOT a split mandate and NOT a defect; recorded so the tier is measurable |

- coverage 9 registers, 2 stage volumes, 33 source documents
- anchors  stage_1.md declares an explicit ANCHORS set (18 ids)
- anchors  stage_1.md declares 18 anchors
- anchors  6 id(s) read as backticked references or range endpoints, not citations (U.101, U.102, U.110, U.111, U.113, U.118)
- quotes   corpus: 7063901 chars of squashed local source text indexed
- quotes   candidates 276, attributed+checked 66, skipped 105, unmatched 18 (27%)
- quotes   unattributed spans unmatched: 105 (advisory, e.g. stage_1.md::do not occur in this volume the registrant s own marketing sentence; stage_1.md::certificate of incorporation of nvidia delaware corporation in witness whereof this certificate has been subsc)
- corrections 4 retraction ids; register layer reaches 4, volumes 4

## Passing checks

```
csv      timeline.csv                       37 rows x 11 cols
csv      timeline.csv.source_id             all S#### tokens resolve
csv      quantitative.csv                   65 rows x 12 cols
csv      conflicts.csv                      17 rows x 15 cols
csv      sources.csv                        16 rows x 18 cols
csv      data_gaps.csv                      21 rows x 8 cols
csv      validation.csv                     11 rows x 11 cols
csv      validation.csv.source_id           all S#### tokens resolve
csv      failures.csv                       11 rows x 11 cols
csv      failures.csv.source_id             all S#### tokens resolve
csv      decisions.csv                      7 rows x 15 cols
csv      decisions.csv.source_id            all S#### tokens resolve
csv      channels.csv                       9 rows x 11 cols
csv      channels.csv.source_id             all S#### tokens resolve
keys     stage_1.md                         16 source tokens all resolve
keys     stage_1_index.md                   2 source tokens all resolve
anchors  citation resolution                every register-cited anchor resolves (18 distinct ids across registers and volumes)
anchors  parity                             18 narrative anchors <-> 18 register anchors
budget   stage_1_index.md                   1125 words (target 8000, hard cap 60000)
corrections propagation                        all 4 retraction(s) reach registers and volumes
```

## Evidence lines for findings

```
stage_1.md :: nvidia corporation exact name of registrant as specified in its charter california prior to reincorporation de
stage_1.md :: a 2 the company as it stood at the open of the stage this is the honest version and it is almost entirely nega
stage_1.md :: no officer or employee is bound by an employment agreement and the relationships of such officers and employee
stage_1.md :: the company typically pays for wafers which may or may not have any functional products accordingly the compan
stage_1.md :: nvidia s primary source of competition is from companies that provide or intend to provide 3d graphics solutio
stage_1.md :: creative recently disclosed that it has acquired in excess of 5 of the outstanding stock of 3dfx a competitor 
stage_1.md :: on april 9 1998 the company was notified that sgi had filed a patent infringement lawsuit against the company 
stage_1.md :: pay substantial damages permanently cease the manufacture use and sale of any infringing products expend signi
stage_1.md :: the company has a fabless manufacturing strategy whereby the company employs world class suppliers for all pha
stage_1.md :: tsmc fabricates wafers for other companies including certain competitors of the company and could choose to pr
stage_1.md :: the company does not have long term agreements with either of these subcontractors amkor siliconware due to th
stage_1.md :: st is entitled to manufacture the riva128zx graphics processor and to sell the riva128 and riva128zx graphics 
stage_1.md :: c the 1993 1997 warrants are a second instrument class
stage_1.md :: note 3 the december 1998 amendment s pro forma footnote carried by the 424b4 assumes an initial price of 8 00 
stage_1.md :: the one 1997 line that does not move across the lineage
stage_1.md :: product revenue from stb and diamond accounted for 63 and 31 respectively of the company s 1997 revenue
stage_1.md :: as of january 26 1997 and september 28 1997
stage_1.md :: yield problems during the quarter ended july 28 1998
```
