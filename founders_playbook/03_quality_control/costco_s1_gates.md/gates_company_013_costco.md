# Mechanical gate report -- company_013_costco

Findings: **2** | Passes: 18

| gate | subject | finding |
|---|---|---|
| quotes | verbatim | 16 of 74 quoted spans not found in local sources |
| advisory | stage_1.md | 46992 words over the core density target 22000 -- NOT a split mandate and NOT a defect; recorded so the tier is measurable |

- coverage 9 registers, 1 stage volumes, 21 source documents
- anchors  stage_1.md declares an explicit ANCHORS set (32 ids)
- anchors  stage_1.md declares 32 anchors
- anchors  3 id(s) read as backticked references or range endpoints, not citations (U.101, U.120, U.125)
- quotes   corpus: 3025386 chars of squashed local source text indexed
- quotes   candidates 340, attributed+checked 74, skipped 213, unmatched 16 (22%)
- quotes   unattributed spans unmatched: 53 (advisory, e.g. stage_1.md::it writes two separately argued predecessor legs inside one registrant s own memory of them the price company ; stage_1.md::do not occur in this volume the registrant s own retrospective genealogy the sentence)
- corrections 5 retraction ids; register layer reaches 5, volumes 5

## Passing checks

```
csv      timeline.csv                       35 rows x 11 cols
csv      timeline.csv.source_id             all S#### tokens resolve
csv      quantitative.csv                   46 rows x 12 cols
csv      conflicts.csv                      22 rows x 15 cols
csv      sources.csv                        14 rows x 18 cols
csv      data_gaps.csv                      26 rows x 8 cols
csv      validation.csv                     8 rows x 11 cols
csv      validation.csv.source_id           all S#### tokens resolve
csv      failures.csv                       11 rows x 11 cols
csv      failures.csv.source_id             all S#### tokens resolve
csv      decisions.csv                      13 rows x 15 cols
csv      decisions.csv.source_id            all S#### tokens resolve
csv      channels.csv                       16 rows x 11 cols
csv      channels.csv.source_id             all S#### tokens resolve
keys     stage_1.md                         14 source tokens all resolve
anchors  citation resolution                every register-cited anchor resolves (32 distinct ids across registers and volumes)
anchors  parity                             32 narrative anchors <-> 32 register anchors
corrections propagation                        all 5 retraction(s) reach registers and volumes
```

## Evidence lines for findings

```
stage_1.md :: part 1 s k01 k08 remain the addresses for everything minted there no anchor below re mints a k or p1g id
stage_1.md :: p1s01 s own words the fy1993 filing attributes the fall to cannibalisation by the company s own new units in e
stage_1.md :: draft eir publication date december 12 1991 final eir certification date april 16 1992
stage_1.md :: warehouses in operation end of year 221 200 170 140 119 104
stage_1.md :: price club warehouse was opened in san diego in 1975 by sol price robert price sol s son rick libenson and
stage_1.md :: he was chief executive officer and a director of price since 1976 mr price was president of price from 1976 un
stage_1.md :: an application for environmental evaluation for a development proposal on the site was filed on august 25 1989
stage_1.md :: the proposed warehouse type retail use would provide entry level employment opportunities for unskilled and se
stage_1.md :: an application for a site permit for the project has not been filed to date
stage_1.md :: price club and costco wholesale merged the price club facility in white marsh maryland did not have a full and
stage_1.md :: the estate closed 4 2 1 7 and 8 units in five of these years
stage_1.md :: price costco inc the registrant and price enterprises inc a newly formed delaware corporation newco have enter
stage_1.md :: 500 000 to 600 000 in the united states and canada for real estate construction remodeling and equipment and a
stage_1.md :: conf medium corroboration 1 lineage conflicts u 104 arithmetic 37 7 30 and 31 1 30 printed nowhere i02 claim c
stage_1.md :: an application for a site permit for the project has not been filed to date
stage_1.md :: 48 in window index filings are silently dropped so 0 unanswered still does not mean 0 remain
```
