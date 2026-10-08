# Mechanical gate report -- company_046_pepsico

Findings: **2** | Passes: 18

| gate | subject | finding |
|---|---|---|
| quotes | verbatim | 3 of 12 quoted spans not found in local sources |
| advisory | stage_1.md | 22958 words over the register density target 8000 -- NOT a split mandate and NOT a defect; recorded so the tier is measurable |

- coverage 9 registers, 1 stage volumes, 38 source documents
- keys     stage_1.md mentions 3 retired keys inside collision/re-key/range text -- protected history, not re-pointed: S4222, S4229, S4463
- anchors  stage_1.md declares an explicit ANCHORS set (15 ids)
- anchors  stage_1.md declares 15 anchors
- anchors  5 id(s) read as backticked references or range endpoints, not citations (U.1, U.10, U.14, U.15, U.4)
- quotes   corpus: 7968716 chars of squashed local source text indexed
- quotes   candidates 117, attributed+checked 12, skipped 89, unmatched 3 (25%)
- quotes   unattributed spans unmatched: 16 (advisory, e.g. stage_1.md::a company s own reprinted history pages and its filings are one source; stage_1.md::for years in which on the registrant s own word pepsico inc did not exist and the uploader s own)
- corrections 6 retraction ids; register layer reaches 6, volumes 6

## Passing checks

```
csv      timeline.csv                       16 rows x 11 cols
csv      timeline.csv.source_id             all S#### tokens resolve
csv      quantitative.csv                   25 rows x 12 cols
csv      conflicts.csv                      15 rows x 15 cols
csv      sources.csv                        16 rows x 18 cols
csv      data_gaps.csv                      15 rows x 8 cols
csv      validation.csv                     4 rows x 11 cols
csv      validation.csv.source_id           all S#### tokens resolve
csv      failures.csv                       8 rows x 11 cols
csv      failures.csv.source_id             all S#### tokens resolve
csv      decisions.csv                      4 rows x 15 cols
csv      decisions.csv.source_id            all S#### tokens resolve
csv      channels.csv                       3 rows x 11 cols
csv      channels.csv.source_id             all S#### tokens resolve
keys     stage_1.md                         16 source tokens all resolve
anchors  citation resolution                every register-cited anchor resolves (15 distinct ids across registers and volumes)
anchors  parity                             15 narrative anchors <-> 15 register anchors
corrections propagation                        all 6 retraction(s) reach registers and volumes
```

## Evidence lines for findings

```
stage_1.md :: supporting data lives in csv never inside prose files
stage_1.md :: the merger story itself unknown no carrier in this corpus
stage_1.md :: unverified tls re check before citing at high confidence
```
