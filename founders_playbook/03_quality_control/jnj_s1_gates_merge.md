# Mechanical gate report -- company_045_jnj

Findings: **2** | Passes: 18

| gate | subject | finding |
|---|---|---|
| quotes | ADVISORY | 7 of 8 checked spans unmatched (88%) -- gate precision is not established, treat as a triage list, NOT as defects |
| advisory | stage_1.md | 27043 words over the core density target 22000 -- NOT a split mandate and NOT a defect; recorded so the tier is measurable |

- coverage 9 registers, 1 stage volumes, 41 source documents
- keys     stage_1.md mentions 2 retired keys inside collision/re-key/range text -- protected history, not re-pointed: S4222, S4229
- anchors  stage_1.md declares 12 anchors
- anchors  9 id(s) read as backticked references or range endpoints, not citations (U.001, U.002, U.003, U.004, U.005, U.006, U.007, U.012)
- quotes   corpus: 17547354 chars of squashed local source text indexed
- quotes   candidates 261, attributed+checked 8, skipped 184, unmatched 7 (88%)
- quotes   unattributed spans unmatched: 69 (advisory, e.g. stage_1.md::no band aid u 005 ii the three self supersessions survive the merge unchanged a; stage_1.md::0 lines naming the company a canadian volume dominion of canada statistics l108 date leg)
- corrections 4 retraction ids; register layer reaches 4, volumes 4

## Passing checks

```
csv      timeline.csv                       18 rows x 11 cols
csv      timeline.csv.source_id             all S#### tokens resolve
csv      quantitative.csv                   21 rows x 12 cols
csv      conflicts.csv                      12 rows x 15 cols
csv      sources.csv                        16 rows x 18 cols
csv      data_gaps.csv                      11 rows x 8 cols
csv      validation.csv                     7 rows x 11 cols
csv      validation.csv.source_id           all S#### tokens resolve
csv      failures.csv                       5 rows x 11 cols
csv      failures.csv.source_id             all S#### tokens resolve
csv      decisions.csv                      8 rows x 15 cols
csv      decisions.csv.source_id            all S#### tokens resolve
csv      channels.csv                       4 rows x 11 cols
csv      channels.csv.source_id             all S#### tokens resolve
keys     stage_1.md                         16 source tokens all resolve
anchors  citation resolution                every register-cited anchor resolves (12 distinct ids across registers and volumes)
anchors  parity                             12 narrative anchors <-> 12 register anchors
corrections propagation                        all 4 retraction(s) reach registers and volumes
```

## Evidence lines for findings

```
stage_1.md :: unverified tls re check before citing at high confidence
stage_1.md :: the incorporation question stays open and no nj charter is in the corpus
stage_1.md :: in the cuban campaign 370 000 w ere supplied by order of the united states government to the army and navy
stage_1.md :: was incorporated into the 16th edition of the united states dispensatory
stage_1.md :: mr johnson was the first to lift the veil of secrecy that covered the making of india rubber plasters
stage_1.md :: unverified tls re check before citing at high confidence
stage_1.md :: sec document bytes held 0 only the index exists no accession body was fetched
```
