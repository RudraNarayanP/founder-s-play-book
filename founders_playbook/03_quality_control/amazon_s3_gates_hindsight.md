# Mechanical gate report -- company_001_amazon

Findings: **1** | Passes: 32

| gate | subject | finding |
|---|---|---|
| quotes | ADVISORY | 66 of 157 checked spans unmatched (42%) -- gate precision is not established, treat as a triage list, NOT as defects |

- coverage 9 registers, 8 stage volumes, 103 source documents
- keys     stage_2_part_1.md cites 195 hyphenated record keys: S2A-03, S2A-04, S2A-06, S2A-10, S2A-11, S2A-17, S2A-18, S2A-20 ...
- keys     stage_2_part_2.md cites 152 hyphenated record keys: S2A-18, S2A-21, S2A-24, S2A-33, S2A-37, S2A-43, S2A-47, S2A-53 ...
- keys     stage_2_part_3.md cites 79 hyphenated record keys: S2A-05, S2A-17, S2A-21, S2A-23, S2A-24, S2A-29, S2A-30, S2A-31 ...
- keys     stage_3_part_1.md cites 4 hyphenated record keys: S2D-05, S2D-09, S2D-63, S2D-72
- keys     stage_3_part_2.md cites 2 hyphenated record keys: S2B-66, S3E-21
- keys     stage_3_part_2.md mentions 4 retired keys inside collision/re-key/range text -- protected history, not re-pointed: S3001, S3012, S3013, S3020
- keys     stage_3_part_3.md cites 1 hyphenated record keys: S2C-17
- keys     stage_3_part_3.md mentions 5 retired keys inside collision/re-key/range text -- protected history, not re-pointed: S3001, S3006, S3007, S3008, S3081
- keys     stage_3_pending_registers.md cites 4 hyphenated record keys: S3D-004, S3D-006, S3P-001, S3P-002
- keys     stage_3_pending_registers.md mentions 4 retired keys inside collision/re-key/range text -- protected history, not re-pointed: S3001, S3004, S3022, S3024
- anchors  stage_1.md declares 43 anchors
- anchors  stage_2_part_1.md declares 1 anchors
- anchors  stage_2_part_3.md declares 72 anchors
- anchors  stage_3_part_3.md declares 68 anchors
- anchors  74 id(s) read as backticked references or range endpoints, not citations (U.1, U.108, U.113, U.114, U.115, U.116, U.117, U.118)
- anchors  5 prose mention(s) match no declared entry, ADVISORY only: U.111a, U.223, U.224, U.225, U.228
- quotes   corpus: 14826080 chars of squashed local source text indexed
- quotes   candidates 3038, attributed+checked 157, skipped 1804, unmatched 66 (42%)
- quotes   unattributed spans unmatched: 1077 (advisory, e.g. stage_1.md::four sites that contradicted it are corrected below; stage_1.md::dated july 5 1994 jeffrey p bezos)
- corrections 26 retraction ids; register layer reaches 26, volumes 26

## Passing checks

```
csv      timeline.csv                       267 rows x 11 cols
csv      timeline.csv.source_id             all S#### tokens resolve
csv      quantitative.csv                   395 rows x 12 cols
csv      conflicts.csv                      172 rows x 15 cols
csv      sources.csv                        204 rows x 18 cols
csv      data_gaps.csv                      102 rows x 8 cols
csv      validation.csv                     59 rows x 11 cols
csv      validation.csv.source_id           all S#### tokens resolve
csv      failures.csv                       62 rows x 11 cols
csv      failures.csv.source_id             all S#### tokens resolve
csv      decisions.csv                      29 rows x 15 cols
csv      decisions.csv.source_id            all S#### tokens resolve
csv      channels.csv                       25 rows x 11 cols
csv      channels.csv.source_id             all S#### tokens resolve
keys     stage_1.md                         5 source tokens all resolve
keys     stage_2_part_1.md                  3 source tokens all resolve
keys     stage_2_part_2.md                  2 source tokens all resolve
keys     stage_2_part_3.md                  15 source tokens all resolve
keys     stage_3_part_2.md                  12 source tokens all resolve
keys     stage_3_part_3.md                  3 source tokens all resolve
keys     stage_3_pending_registers.md       33 source tokens all resolve
anchors  citation resolution                every register-cited anchor resolves (191 distinct ids across registers and volumes)
anchors  parity                             183 narrative anchors <-> 183 register anchors
budget   stage_1.md                         50814 words (target 60000, hard cap 60000)
budget   stage_2_part_1.md                  22967 words (target 60000, hard cap 60000)
budget   stage_2_part_2.md                  28399 words (target 60000, hard cap 60000)
budget   stage_2_part_3.md                  46016 words (target 60000, hard cap 60000)
budget   stage_3_part_1.md                  49545 words (target 60000, hard cap 60000)
budget   stage_3_part_2.md                  25615 words (target 60000, hard cap 60000)
budget   stage_3_part_3.md                  43689 words (target 60000, hard cap 60000)
budget   stage_3_pending_registers.md       10738 words (target 60000, hard cap 60000)
corrections propagation                        all 26 retraction(s) reach registers and volumes
```

## Evidence lines for findings

```
stage_1.md :: nobody really knows whether large numbers of consumers will take to shopping by computer
stage_1.md :: isn t the first or necessarily the cheapest online book merchant
stage_1.md :: in just its first four weeks of operation
stage_1.md :: we did have a million titles we didn t have a million books
stage_1.md :: is claimed by the company s own 1995 10 04 release to have placed the store
stage_2_part_1.md :: the leading online retailer of books also sells a smaller number
stage_2_part_1.md :: an under count of the instrument s own history the differential is the evidence the repetition is not audit 5 
stage_2_part_1.md :: on the deal under a disclaimer that the words were neither
stage_2_part_1.md :: u 112 dated instead over 4 800 registered members as of december 31 1996 and fortune s
stage_2_part_1.md :: orders in hand amazon requests books from a distributor or publisher which delivers them to the company s seat
stage_2_part_1.md :: the online commerce market is new rapidly evolving and intensely competitive in addition the retail book indus
stage_2_part_1.md :: the definitive answer to the stage 1 null on directory efficacy
stage_2_part_2.md :: might not be able to project the rate of growth in time
stage_2_part_2.md :: is not consistent with the figures in the record that states it
stage_2_part_2.md :: primarily attributable to increases of 29 8 million in accounts payable 5 1 million in other accrued expenses 
stage_2_part_2.md :: and the company s own factor warns it
stage_2_part_2.md :: of the more than 2 5 million titles offered by the company up to 400 000 are currently supplied by distributor
stage_2_part_3.md :: the company may choose to expand its product offerings
stage_2_part_3.md :: music and video were part of the business from 1996 97
stage_2_part_3.md :: no specific use of proceeds working capital to fund anticipated operating losses and capital expenditures
stage_2_part_3.md :: asserts that a registration statement carries a launch date string checked across all five local accessions th
stage_2_part_3.md :: the 4 2 window closes 1996 12 06 1996 05 16 the 1996 slice is unknown
stage_3_part_1.md :: this is the fy1997 md a paragraph reproduced inside an 8 k exhibit it is not a second observation of the delaw
stage_3_part_1.md :: the company operates in one principal business segment across domestic and international markets international
stage_3_part_1.md :: the international segment was 21 806k 3 6 of fy1998 net sales on 2 8m of foreign long lived assets derived 21 
stage_3_part_1.md :: net cash provided by changes in operating assets and liabilities 72 468
stage_3_part_1.md :: the intimate bookshop and wallace kuralt filed a lawsuit in the united states district court for the southern 
stage_3_part_1.md :: we expect that fulfillment costs will decline as a percentage of sales in the future as additional capacity of
stage_3_part_1.md :: the largest signal in this window is that the cost of capital fell not that the cost of doing business did
stage_3_part_1.md :: first day in which periodic filings not a registration statement govern
stage_3_part_1.md :: net sales for the three month period ended june 30 1997 were 27 855 000
stage_3_part_1.md :: this sales agreement made by and between amazon com inc a delaware corporation hereinafter called
stage_3_part_1.md :: string in the filing is an air handling spec l11150 register st3d 17 st3d 20 b06 claim amazon com ksdc inc a s
stage_3_part_1.md :: third party sellers can now reach amazon com s community nof 8 million pre registered experienced online buyer
stage_3_part_1.md :: word of mouth remains the most powerful customer acquisition ntool we have and we are grateful for the trust o
stage_3_part_1.md :: these eight nnew distribution centers comprised approximately four million square feet
stage_3_part_1.md :: eight distribution centers approximately 3 8 million square feet
stage_3_part_1.md :: string in the whole q1 1999 filing is an air handling specification
stage_3_part_1.md :: fulfillment costs will decline as a percentage of sales in the future as nadditional capacity of our existing 
stage_3_part_1.md :: we are not experienced in coordinating and nmanaging distribution operations in geographically distant locatio
```
