# Mechanical gate report -- company_003_unitedhealth

Findings: **1** | Passes: 21

| gate | subject | finding |
|---|---|---|
| quotes | verbatim | 5 of 23 quoted spans not found in local sources |

- coverage 9 registers, 2 stage volumes, 44 source documents
- keys     stage_1.md mentions 10 retired keys inside collision/re-key/range text -- protected history, not re-pointed: S0001, S0155, S0812, S3000, S30001, S3001, S30084, S3029
- keys     stage_1_index.md mentions 1 retired keys inside collision/re-key/range text -- protected history, not re-pointed: S3001
- anchors  stage_1.md declares an explicit ANCHORS set (18 ids)
- anchors  stage_1.md declares 18 anchors
- anchors  20 id(s) read as backticked references or range endpoints, not citations (U.001, U.002, U.003, U.004, U.005, U.006, U.007, U.008)
- quotes   corpus: 5269736 chars of squashed local source text indexed
- quotes   candidates 238, attributed+checked 23, skipped 143, unmatched 5 (22%)
- quotes   unattributed spans unmatched: 72 (advisory, e.g. stage_1.md::allowed to finish the stage as one file; stage_1.md::only at a section boundary never renumber)
- corrections 8 retraction ids; register layer reaches 8, volumes 8

## Passing checks

```
csv      timeline.csv                       39 rows x 11 cols
csv      timeline.csv.source_id             all S#### tokens resolve
csv      quantitative.csv                   83 rows x 12 cols
csv      conflicts.csv                      23 rows x 15 cols
csv      sources.csv                        31 rows x 18 cols
csv      data_gaps.csv                      22 rows x 8 cols
csv      validation.csv                     8 rows x 11 cols
csv      validation.csv.source_id           all S#### tokens resolve
csv      failures.csv                       8 rows x 11 cols
csv      failures.csv.source_id             all S#### tokens resolve
csv      decisions.csv                      10 rows x 15 cols
csv      decisions.csv.source_id            all S#### tokens resolve
csv      channels.csv                       6 rows x 11 cols
csv      channels.csv.source_id             all S#### tokens resolve
keys     stage_1.md                         31 source tokens all resolve
keys     stage_1_index.md                   31 source tokens all resolve
anchors  citation resolution                every register-cited anchor resolves (18 distinct ids across registers and volumes)
anchors  parity                             18 narrative anchors <-> 18 register anchors
budget   stage_1.md                         44996 words (cap 60000)
budget   stage_1_index.md                   1068 words (cap 60000)
corrections propagation                        all 8 retraction(s) reach registers and volumes
```

## Evidence lines for findings

```
stage_1.md :: charter med minneapolis which manages ten ipas around the coun try
stage_1.md :: long term obligations 41 649 24 132 39 099 24 275
stage_1.md :: not make or incur any loan or capitalized lease obligation in excess of 10 000 000 not enter into business lin
stage_1.md :: accession number 0000950131 95 000748 conformed period of report 19941231 filed as of date 19950328
stage_1.md :: enrollment growth including acquisitions rose by 990 400 members or 64 percent during the 12 months ended janu
```
