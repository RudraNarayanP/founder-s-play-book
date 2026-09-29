# Stage 1 index -- company_003_unitedhealth (United HealthCare Corporation)

Built by the Stage-1 merge pass on 2026-09-26 (agent `uhc-s1-merge`). This is the volume list for a stage
that **merged as one file**: method §9.2 puts the soft target at 40,000 words and defines 40,000-60,000 as
the amber band in which finishing as one file is explicitly allowed, and §9.3 splits only at the 60,000
hard cap and only at a section boundary. The merged volume is **44,921 words**, inside the cap with 15,079 words of
headroom, so there is no `stage_1_part_1.md` / `stage_1_part_2.md` geometry and no §A-§U renumbering;
numbering is continuous because the part was never renumbered. If a later pass pushes this stage past
60,000 words, the split point §9.3 allows is between §T and §U -- and both the part file and the volume
index stay citable, because §U's anchors are register keys, not line numbers.

## Volumes

| # | File | Words | Bytes | Sections contained | Status |
|---|---|---|---|---|---|
| 1 | `stage_1.md` | 44,921 | 312,292 | merge header and merge note, then the whole Stage-1 part verbatim: Header, Boundary, §A-§T, §U (anchors U.001-U.018), the nine register-emission blocks, Untried | WRITTEN, one volume |
| 2 | `stage_1_index.md` | measured in `_MANIFEST.md` | (this index reports its own size there) | this index | WRITTEN |
| 3 | `CORRECTIONS.md` | 1,223 | 8,179 | COR-01 - COR-08 and the four outbound corrections | WRITTEN |
| -- | `_parts/s1_p1.md` | 42,703 | 298,482 | the same 25 sections as written by the author -- **superseded, retained as the audit trail, DO NOT RE-APPLY its blocks** | SUPERSEDED 2026-09-26 |

Section letters physically present in `stage_1.md`: **A B C D E F G H I J K L M N O P Q R S T U** -- 21 §A-§U letters, plus `Header`, `Boundary`,
`Register rows for merge` and `Untried` = **25 sections**, each carrying `STATUS: WRITTEN` and none PENDING.

## Where the §U anchors live

All 18 anchors are declared in one range and each is covered by at least one register row -- 18 declared,
18 cited, 0 undeclared, 0 uncovered, measured by `gates.py` after the merge and not before.

| range | what it holds | register rows |
|---|---|---|
| `U.001`-`U.018` | every Stage-1 live conflict: the 1974-vs-January-1977 origin (U.001), the Charter Med predecessor and its two-name problem (U.002, U.005), the Minnetonka-vs-Eden-Prairie locality (U.003), the Burke 1987/1988 split (U.004), the FY1990 figure floor (U.006, U.007), the two file numbers (U.008), the GenCare day (U.009), the 4,330-row index delta (U.010), the enrollment denominators (U.011), the Delaware-registered-name leg (U.012), the naming history (U.013), the **stage boundary** (U.014), the 21-vs-16+9 plan count (U.015), and the two defects inside held primaries (U.016 Schedule F's 241,000; U.017 the +990,400 / 64 percent pair) | `conflicts.csv` -- one row each, plus three of the five `data_gaps.csv` rows this pass opened from their own residual cells |
| (no `U.019`+) | not minted. The declared set is U.001-U.018; a merge that minted an anchor would break the declared set. The two cross-emission discrepancies this pass found are therefore keyed **M-01** (the Second Restated Articles' execution date, 1988-02-19 vs 1994-05-13) and **M-02** (the "no dated event of any kind" null vs research/B's dated environment rows), and research/B's own three unresolved conflicts keep their dossier-local keys **C-02, C-03, C-04** |

## Registers (company root; canonical)

| register | rows | cols | what is in it |
|---|---|---|---|
| `sources.csv` | 31 | 18 | global **`S4301`-`S4331`**; 24 p1 carriers + 7 research/B carriers; four same-document folds and the P1S24 bundle split into one id per document |
| `quantitative.csv` | 83 | 12 | 80 p1 money rows + 3 research/B rows; 21 same-fact folds; every DERIVED/ESTIMATE row carries its arithmetic, every FACT row carries the corpus `not applicable` marker, and **all 83 rows state CONTEMPORANEOUS or RESTATED** |
| `timeline.csv` | 39 | 11 | 26 p1 + 13 research/B events; 4 folds; the null row re-perimetered under COR-02 |
| `decisions.csv` | 10 | 15 | p1 only -- research/B proposed none and says why (a Stage-1 decision for this company in 1974-1990 needs an interior record; none exists in any family tried, and inventing one from the 1995 disclosures would breach §2) |
| `validation.csv` | 8 | 11 | p1 only; includes the U.017 pair recorded as a validation signal, not a metric |
| `failures.csv` | 8 | 11 | p1 only; no research/B rows |
| `channels.csv` | 6 | 11 | p1 only; research/B's §G-equivalent is a knowability argument, not a channel record |
| `conflicts.csv` | 23 | 15 | 18 §U anchors + C-02/C-03/C-04 + the two merge-minted M-01/M-02 |
| `data_gaps.csv` | 22 | 8 | 15 p1 + 4 research/B + 3 residue rows opened from U.009/U.016/U.017; every High row carries a follow-up route |
| **total** | **230** | | 259 emissions requested, 34 folded, 0 refused, 5 rows added by the merge |

## The merge's decisions, in one place

1. **One volume, no split**, on §9.2's amber rule and §9.3's boundary rule; nothing trimmed to fit (§9.6).
2. **Both emissions applied**, including the one the census tool cannot see (`research/B_
   chronology_finance_from_print.md`, 64 rows) -- RD-122's failure mode, and the part's own preamble names it.
3. **Folding, never dropping**: 34 aliased emissions live on verbatim inside the kept rows behind printed
   `MERGE[...]` markers, and each kept row lists the ids it swallowed.
4. **Ids minted centrally once**: `S4301`-`S4331`, chosen past every id issued anywhere; `S43nn` cannot
   collide with Amazon's five-digit Stage-3 series and is not the `S3001`+ range that Target's idiom would
   have handed this company, because that range is already issued. Full map, superseded-local ids included:
   **S4301**<-BS-01+P1S01 **S4302**<-P1S02 **S4303**<-P1S03 **S4304**<-P1S04 **S4305**<-BS-02+P1S05 **S4306**<-BS-03+P1S06 **S4307**<-P1S07 **S4308**<-P1S08 **S4309**<-P1S09 **S4310**<-P1S10 **S4311**<-P1S11 **S4312**<-P1S12 **S4313**<-P1S13 **S4314**<-P1S14 **S4315**<-P1S15 **S4316**<-P1S16 **S4317**<-P1S17 **S4318**<-BS-05+P1S18 **S4319**<-P1S19 **S4320**<-P1S20 **S4321**<-P1S21 **S4322**<-P1S22 **S4323**<-P1S23 **S4324**<-P1S24 **S4325**<-BS-04 **S4326**<-BS-06 **S4327**<-BS-07 **S4328**<-BS-08 **S4329**<-BS-09 **S4330**<-BS-10 **S4331**<-BS-11
5. **Nothing adjudicated that the evidence does not adjudicate**: U.009, U.016 and U.017 stay open with
   their printed values, and the two cross-emission discrepancies this pass found (M-01, M-02) are recorded
   as conflicts, not resolved into one date or one null.
6. **Re-apply hazard named where a reader will hit it**: the nine emission blocks live in both the volume
   and the superseded part; the part's tail now says DO NOT RE-APPLY THESE BLOCKS.
