# target_s1_merge.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-26T09:32:57Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## Row application

**Which emissions were used — the brief asked.** `company_status` showed 0 register rows, and the check
confirmed no CSV at the company root. Rows exist in **three** places, not two: `_parts/s1_p1.md` (47),
`_parts/s1_p2.md` (79) and the probe dossier `research/B1_dayton_print_records.md` (**65 rows**, its
`## Register rows` block, 2026-09-26 STATUS line: "no register CSV was opened"). Both parts *presuppose*
B1's rows — p1: "B1's 65 rows are **not** duplicated here; the merge applies both sets and aliases the five
shared carriers"; p2: "new rows only, IDs continue B1's Q-series"; p1's timeline block: "B1's thirteen
timeline rows already carry the estate and offering sequences". Applying only the 126 would have dropped
B1's Q1–Q26 store-and-group series and 13 timeline rows, which is a silent drop, so **all three emissions
were applied: 191 requested → 157 register rows, 34 folded into 28 collision groups, 0 refused.**

Column parity was validated against Amazon's headers **before writing** (headers copied byte-identical from
`company_001_amazon/<name>.csv`). 8 rows arrived with width drift, all with one principled cause — unquoted
thousands/place commas inside a single cell. Repaired by re-joining at the printed split point, no value
altered, and tagged **COR-06**:

| emission row | cols got | repaired cell |
|---|---|---|
| p2 `sources.csv` l1179 (P2S01) | 19/18 | relevant_passage `…889,000 square feet.` |
| p2 `sources.csv` l1185 (P2S07) | 19/18 | relevant_passage `0 documents stored,0 skipped/unanswered` |
| p2 `sources.csv` l1186 (P2S08) | 23/18 | relevant_passage `Number of stores …5,563 5,518 4,220 3,516 2,390` |
| p2 `quantitative.csv` l1211 | 14/12 | derived_arithmetic `889,000 / 7 = 127,000` |
| p2 `timeline.csv` l1226 | 13/11 | event `…Roseville, Crystal, Duluth and Knollwood St.Louis Park` |
| p2 `timeline.csv` l1229 | 13/11 | notes `transfer of 1,535,500 from retained earnings…` |
| p2 `timeline.csv` l1231 | 12/11 | event `…total retail area of 889,000 square feet` |
| p2 `timeline.csv` l1233 | 12/11 | notes `…do not foot to the FY1966 total of 889,000` |

Other refusals-of-application: **none** — every row parsed to the target width, so nothing had to be refused.
Three further normalisations, each recorded inside the affected cell (never silently):
1. p1's shared `validation.csv`/`failures.csv` block (5 rows, one column list per §13) was split by the
   row's own content: 4 signals → `validation.csv`, the fifth (`ABSENCE OF ANY PRINTED FAILURE`) →
   `failures.csv`, exactly as p1's row-count paragraph instructs.
2. B1S12/B1S13 (the two unheld founder-credit leads) carried the prose `NOT ACCESSED` in `access_date`, a
   year-bearing date column; the cell is now `UNKNOWN` and the fact "never accessed, web lead only" moved
   into `notes` verbatim. The rows are kept, not dropped — they are the register's evidence that K1 has no
   held carrier.
3. 16 register cells cited §U's *subsection numbers* (`section U.1`) which are not anchors and resolve to
   nothing in the declared set; rewritten to block names ("the section-U live-conflict block"). Anchor ids
   themselves untouched.

Empty cells after application: **0** across all 157 rows. `derived_arithmetic`: every DERIVED/ESTIMATE row
carries its arithmetic; FACT rows that arrived with an empty cell were filled with the corpus's own
`not_derived` marker (p1's documented convention) so no cell is blank — 0 DERIVED rows lack arithmetic.
`stage` is the controlled literal `stage1` on every row of all nine registers; no numeric stage values were
found, so nothing needed normalising under §13.

STATUS: WRITTEN 2026-09-26

## Collisions and id resolution

**34 emissions folded into 28 visible collision groups. No row was dropped: in every group the kept row
carries the aliased emission's distinct wording verbatim** (union rule: a cell is appended when it holds
words absent from the kept row; passages union in place, other prose routes to `notes` / `section` /
`why_missing` / `follow_up_task` with a printed `MERGE[tag <- emission col: value]` marker).

| register | requested | rows kept | folded | groups |
|---|---|---|---|---|
| `sources.csv` | 30 (B1 14 + p1 8 + p2 8) | 21 | 9 | 8 |
| `quantitative.csv` | 65 (25 + 13 + 27) | 61 | 4 | 4 |
| `timeline.csv` | 25 (13 + 4 + 8) | 24 | 1 | 1 |
| `conflicts.csv` | 25 (6 + 3 + 16) | 18 | 7 | 7 |
| `data_gaps.csv` | 35 (7 + 8 + 20) | 22 | 13 | 8 |
| `decisions.csv` / `validation.csv` / `failures.csv` / `channels.csv` | 3 / 5 / 0 / 3 | 3 / 4 / 1 / 3 | 0 | 0 (the p1 validation block was **split**, not folded) |

Same-fact collisions worth naming: **P1K10 ≡ p2's K8** ("fiscal = calendar" refuted / the layer labelled
1965 ends 1966-01-29) → one row, **U.011**; p1's `parent_net_income 7,128,981` @bare-1965 ≡ p2's same digits
@1966-01-29 → p2's re-based row kept, p1's foot-check (`7,128,981 / 5,435,205 = 1.3116`) unioned into
`derived_arithmetic`; p1's `target_sales_growth_printed 44 percent` ≡ p2's `target_unit_sales_growth_rate`;
p1's `target_store_average_retail_area 127,000` ≡ p2's `target_avg_retail_area_per_store`; B1's Q20
(`parent_net_retail_sales`, 186,166,671 labelled 1965) ≡ p2's re-based row → kept with a **superseding note
inside the same cell**, per §14 rule 8, never a deletion. p1's bundled negative-artifact row **P1S08**
(EDGAR 503s + FTS zeros + CDX 503s) was folded into p2's three per-route rows so anchors U.025/U.026/U.027
each resolve to a carrier; P1S08's full text is retained at S4218 and cross-named at S4219/S4220.

**Ids resolved centrally, one pass.** p1 and p2 never literally collided (disjoint prefixes `B1S`/`P1S`/`P2S`,
`P1K`/`K`), but all three blocks were dossier-local claims, so 21 global ids were minted in `S42nn` form
(company-scoped, 4-digit so `gates.py` resolution applies) and every register citation was re-pointed to
them: **200 source-token re-pointings, 63 conflict-key re-pointings.** Superseded local ids are **kept as
aliases in the `notes` cell of the row that replaces them** — nothing deleted:
`S4201←P1S01+B1S01 · S4202←P1S02+B1S02+P2S01 · S4203←P1S03+B1S03 · S4204←B1S04 · S4205←B1S05 ·
S4206←P1S04+B1S06 · S4207←B1S07 · S4208←B1S08 · S4209←P2S08+B1S09 · S4210←B1S10 · S4211←B1S11 ·
S4212←B1S14 · S4213←B1S12 · S4214←B1S13 · S4215←P1S05 · S4216←P2S05+P1S06 · S4217←P2S06+P1S07 ·
S4218←P2S02+P1S08 · S4219←P2S03 · S4220←P2S04 · S4221←P2S07`. Conflict keys: p2's K-series renumbered onto
the §U anchors they document (`K1→U.001 … K15→U.017`, `K4b→U.007`, `K8/P1K10→U.011`), B1's six K-rows
folded into the same keys; p1's two orphan conflicts keep a non-anchor key space (`P1K11→K16`, `P1K12→K17`)
because volume 1 minted **no** §U anchors and minting one at merge would break the declared set.

**Anchor parity, verified not assumed.** p1 minted none (0 `U.n` tokens anywhere in `_parts/s1_p1.md`), so
p2's declared `<!-- ANCHORS: U.001-U.037 -->` is the whole set. Scan result: the registers cite exactly 37
distinct anchor tokens, `UNDECLARED = []` and `UNCOVERED = []` — every declared anchor has a register row
(U.001–U.017 in `conflicts.csv`, U.018–U.037 in `data_gaps.csv`) and no register row cites an undeclared one.
The 16 `section U.1`-style subsection references rewritten to block names were necessary for this: they are
not anchors and would otherwise have read as register rows citing entries the narrative never declared.
STATUS: WRITTEN 2026-09-26

## Registers created

**All nine created at the company root** (`founders_playbook/01_companies/company_042_target/`), 157 rows.
Headers are **byte-identical to Amazon's**: each was read as raw bytes from `company_001_amazon/<name>.csv`
and written back verbatim as line 1, not retyped — so column drift cannot originate at the merge. UTF-8, `\n`
line endings, `csv.QUOTE_MINIMAL`; every row asserted to the target width before writing.

| register | cols | rows | note |
|---|---|---|---|
| `sources.csv` | 18 | 21 | global `S4201`–`S4221`; `independence_note` carries the one-lineage finding on every corporate-print row; unheld leads S4213/S4214 are kept as **NOT HELD**, not as evidence |
| `quantitative.csv` | 12 | 61 | 37 `PERIOD BASIS` designations added at merge; `derived_arithmetic` non-empty on every DERIVED/ESTIMATE row, 42 FACT rows filled with the corpus `not_derived` marker so no cell is blank |
| `timeline.csv` | 11 | 24 | 8 from volume 2, 4 from volume 1, 13 from B1, 1 collision folded |
| `decisions.csv` | 15 | 3 | volume 1 only — volumes 2 and B1 emitted **no** decision rows (§N is narrative: "no memo, no study, no dissent survives"); creating it header-only was not needed |
| `validation.csv` | 11 | 4 | the four signals in p1's shared block (§L is narrative in volume 2, which emitted no rows) |
| `failures.csv` | 11 | 1 | the one printed negative in the founding decade (FY1972 group pretax fall) plus the record-selection absence row routed here by p1's own instruction |
| `channels.csv` | 11 | 3 | volume 1's three tested channels (§I in volume 2 is a knowability argument, not a channel record) |
| `conflicts.csv` | 15 | 18 | 16 keyed to §U anchors + K16/K17 for volume 1's two orphan conflicts; every row opens with a printed collision note naming its pre-merge local keys |
| `data_gaps.csv` | 8 | 22 | U.018–U.037 plus B1's 1963–64 openings gap and volume 1's cost/land-price/vendor gap; every High-importance row carries a follow-up route |

**No register ended header-only.** The brief asked for the reason where a register has no rows: the four
"thin" registers (`decisions` 3, `failures` 1, `channels` 3, `validation` 4) are thin because the dossiers
emitted that many rows and no more — inventing rows to even them out would be padding, and the register
counts now mirror the sections' actual evidence. Volume 2 emitted nothing for those four because §L, §M, §N
and §I are written as knowability arguments about the archive, not as new records.

Controlled `stage` vocabulary: **`stage1` on all 157 rows of all nine files** — a per-file distinct-value scan
returned `['stage1']` each time, so no numeric `1/2/3` values and no `stageN` drift existed to normalise, and
nothing needed the §13 "record the count in the manifest" treatment. Post-boundary `(PB)` rows (the FY1972–74
recap legs) stay `stage1` because the dossiers labelled them so and they are used only as consequences; that
choice is stated here rather than silently applied. Empty cells: **0**. Dangling `source_id` tokens: **0**.
Duplicate primary keys: **0** (18 distinct conflict ids, 21 distinct source ids).
STATUS: WRITTEN 2026-09-26

## Corrections propagation

Six items opened on this pass, each written into `CORRECTIONS.md` and tagged into the register rows the
withdrawn text actually sat in. **47 register rows carry a COR tag**; a per-id scan confirms each id reaches
**both** the register layer and the merged volume, which is the check the `corrections` gate runs and the
failure this project repeats most.

| id | what was withdrawn | register rows tagged |
|---|---|---|
| **COR-01** | the inherited claim that "fiscal year equals calendar year in these reports" (volume 1's P1K10, volume 2's K8 → the single conflict row **U.011**). The FY1965-labelled layer reports the year **ended 1966-01-29**; a bare year in a date cell is a fiscal year | **32**: `conflicts.csv` U.011; 29 `quantitative.csv` rows (incl. the re-based 186,166,671 / 162,773,739 pair and every bare-1965 leg); 2 `timeline.csv` rows |
| **COR-02** | the dispatch's floor date **1972-03-22**, which greps to **zero** across this company directory in all three written forms | **1**: `conflicts.csv` K16 — the value was never written into any row, which is the point of §14 rule 8; it survives only as a conflict |
| **COR-03** | the mis-citation trap: FY1965 **L122-123 Brookdale** (the development arm's centre) sitting one line above the Target entry sentence, quotable as a Target opening | **2**: `conflicts.csv` K17 + the `timeline.csv` Brookdale row, each marked so no later pass quotes it as an opening |
| **COR-04** | volume 1's §G claim that **site tenure was UNKNOWN** — retracted in the same pass that read the FY1966 notes, which print a land sale-and-leaseback with the buildings mortgaged | **2**: `data_gaps.csv` (the cost / land-price / vendor gap, whose `why_missing` now says tenure is *partially established*) + the `quantitative.csv` 225,000 annual-rentals row that carries the evidence |
| **COR-05** | the probe table's FY1970 layer byte count **52,736**; disk and sidecar both print **53,023** (volume 1's N6) | **2**: `sources.csv` S4206 + `data_gaps.csv` U.023 |
| **COR-06** | nothing was withdrawn — eight rows arrived with unquoted thousands/place commas (column drift) and were re-joined at the printed split point, no value altered | **8**: 3 `sources.csv` + 4 `timeline.csv` + 1 `quantitative.csv`, one tag per repaired row |

**B1's Q20 re-basing** is applied as the parts demanded: superseding text inside the same cell
("this row SUPERSEDES the aliased emission's label for the same digits"), the aliased row's wording unioned
in, the row ID kept, and COR-01 named — a deletion would have destroyed the record of the error.

**Outbound, not mine to fix (§14 rule 4: I may write only the files named in my brief).** The instruction
layer still carries a retracted value: `MASTER_RESEARCH_LOG.md` line 1291 states "No held byte names the
company before **1972-03-22**" as a finding, which is COR-02's withdrawn date. The merge did **not** edit that
log. `RESUME_HANDOFF.md` was grepped for the company, the date and the year-basis claim and returned **no
hits**, so no stale value lives there. The log line is handed to the log's owner as an explicit outbound
correction.
STATUS: WRITTEN 2026-09-26

## Volume and index

**`stage_1.md` written: one volume, 37,507 words / 255,104 bytes.** §9.2 test: 36,954 across the parts, so the
merged file sits under the 40,000 soft target and nowhere near the 60,000 hard cap — **no §9.3 split was
triggered and none performed**, and §A–§U numbering stays continuous because the parts were never renumbered.
Build is mechanical concatenation under one new header: merge header → merge note → Volume 1 body (Header,
Boundary, §A–§H) → divider → Volume 2 body (§I–§U, the P2 claim records, all three register-emission blocks).
**No part content was rewritten, reordered, trimmed or summarised.** The only things removed are each part's
filename H1 and its stale `SCAFFOLDED … STATUS: nothing written yet` marker, kept out because a header telling
a cold reader the file is empty is exactly the §14-rule-10 defect class; their 70 words are accounted line by
line below.

`<!-- ANCHORS: U.001-U.037 -->` is preserved verbatim inside the carried volume-2 assembly note, and §U's 37
anchor entries are physically intact in the merged file (gate-verified, not asserted). The merge note in front
carries: the split decision, the row/ collision counts, the global id decision with the retired-id policy, the
anchor-parity statement, and all six COR ids so that the retractions reach the volume as well as the registers
(`COR-01 … COR-06` appear in the register layer and in this volume — the propagation the `corrections` gate
requires).

**`stage_1_index.md` written (850 words / 5,834 bytes):** ordered volume list with words/bytes/sections, the four anchor
ranges (U.001–U.017 conflicts · U.018–U.024 documented nulls · U.025–U.029 UNANSWERED · U.030–U.037 UNTRIED)
with where each register row lives, the nine register counts, and the six merge decisions including the complete
retired-id map. **`_MANIFEST.md` regenerated (§9.6)** with live word/byte counts for all 14 files, upload batch
5 (companies 041–050), the stage-vocabulary report (**0 numeric stage values found, so no normalisation count
to give**), the coverage note naming what does not yet exist for this company, and the non-destruction table.

`_parts/` was **not** rewritten: one dated `MERGED 2026-09-26 / SUPERSEDED` line appended to each part, saying
where the text now lives, that the registers are canonical, and **DO NOT RE-APPLY THESE BLOCKS** — the emitted
CSV blocks still sit inside the volume and inside the parts as text, so the re-application hazard is named where
a future reader will hit it.
STATUS: WRITTEN 2026-09-26

## Non-destruction proof

**Word delta, line by line, not asserted.** 36,954 (parts as emitted: 15,396 + 21,558) → **37,507** merged.

| line | words | running |
|---|---|---|
| `_parts/s1_p1.md` as emitted | 15,396 | 15,396 |
| `_parts/s1_p2.md` as emitted | 21,558 | 36,954 |
| − each part's filename H1 + its stale `SCAFFOLDED … nothing written yet` marker | −35 −35 | 36,884 |
| + merged header (title, dataset line, §9.2 split test) | +102 | 36,986 |
| + `## Stage 1 merge note` (registers, ids, anchors, the six COR entries) | +505 | 37,491 |
| + the volume divider | +16 | **37,507** |

The build asserted `merged == body1 + body2 + header + divider` by word count before writing (37,507 =
37,507), and the stronger test passes after: **each part body is a byte-identical contiguous slice of
`stage_1.md`** (105,033 B and 145,812 B substring tests both true) — nothing between them was rewritten.

**Record counts before / after, equal.** Claim records 16 (volume 1) + 12 (`P2-nn`, volume 2) = **28 before,
28 after**. Emission blocks in `` ```csv `` fences 8 + 5 = **13 before, 13 after**. `ANCHORS:` declaration 1 → 1.
**Anchor counts equal: 37 distinct `U.nnn` anchor entries in volume 2 = 37 in the merged volume**, and
`gates.py` reports **parity 37 narrative ↔ 37 register**, 0 undeclared, 0 uncovered. The occurrence count of
bold anchor entries moved 45 → 47; the +2 is two mentions in my own merge note (COR-01 / U.011), not new
anchors — the reserved `U.101`-up block stayed unused.

**Register counts before / after: 0 rows on disk → 157 rows**, from 191 emitted (47 + 79 + B1's 65), with
**34 folded into 28 listed collision groups and 0 refused**; the per-register arithmetic is in
`_MANIFEST.md` and §Row application above, and every fold names its aliased emission inside the kept cell.

**Census caveat honoured.** The id census used `[A-T]\d{1,3}`: **143 distinct ids in the two parts → 145 in the
merged volume, `lost = []`**. The two additions are `K16` and `K17`, minted at merge for volume 1's two
anchor-less orphan conflicts (P1K11, P1K12) — an addition, not a renumbering; no pre-existing id was retired from
the census view. A two-digit pattern would have counted **57** and silently missed the three-digit legs the
corpus actually uses (`L110`, `L122`, `L397`, `U.011`-era line locators and the `Q`-series past Q9), which is
why the wider class was used.

**Gate.** Before: 1 finding (`coverage/registers` — no CSVs; `csv`/`anchors` **DID NOT RUN**; `corrections`
**DID NOT RUN**, "not a pass"). After: **0 findings, 19 passes** — `csv` 9 registers width-clean with all
`S####` tokens resolving, `keys` `stage_1.md` tokens resolve, `anchors` citation resolution + parity 37↔37,
`budget` 37,507 < 60,000, `corrections` "all 6 retraction(s) reach registers and volumes". Advisory, not
defect: `U.1`–`U.5` and the reserved `U.101` are prose mentions. No check I required still reports DID NOT RUN.
STATUS: WRITTEN 2026-09-26

## Residue

**UNTRIED / not done by this pass, named rather than papered over:**
1. **A tier-vs-cap finding the orchestrator must adjudicate.** Probe A returned **T2 core**, whose §15.2 cap is
   22,000 words per stage; the merged volume is 37,507 and `gates.py` budget-passed it only because its
   `--tier` default is `exemplar` (60,000). I did not trim, split or re-tier anything: §9.6 forbids cutting
   evidence to fit a file limit and §15.4 makes a missed length target legitimate, not a failure. The two parts
   are written at exemplar density (9 registers, 157 rows, 37 anchors), which argues the tier — not the volume —
   is what should be revisited.
2. **Outbound correction to a file I do not own:** `MASTER_RESEARCH_LOG.md` line 1291 still states COR-02's
   withdrawn `1972-03-22` floor as a finding. §14 rule 10 says that is the highest-severity home for a stale
   claim; rule 4 says I may not edit it. Handed to the log's owner. `RESUME_HANDOFF.md`: grepped, no hits, nothing stale.
3. **Re-apply hazard, mitigated not removed.** The 13 emission blocks still sit as text inside `stage_1.md`
   and the two `_parts/` files while the canonical data is the nine CSVs. Each part now carries `DO NOT RE-APPLY
   THESE BLOCKS`; a future pass that does would double-count 191 rows over 157.
4. **Pre-merge copies retained:** `research/B1_dayton_print_records.md` still holds its 65 emitted rows.
   `gates.py` resolves a register name at the company root first, so the root CSVs are canonical and the dossier
   is provenance, not a second register.
5. **Tool defects recorded, not fixed** (U.029): `ia_text.py` search returns field-less docs and `fetch` 404s on
   spaced filenames; `sec_intake.py index` discards `formerNames`; `periodical_harvest.py` has no `target` task
   set. Other agents are in `tools/sec_intake.py` right now; I touched nothing under `tools/`.
6. **Still-open evidence routes, unchanged by a merge:** the 17 PDF image legs (would settle K6/U.008, K7/U.009,
   N5), the two unheld K1 obituaries (U.031 — S4213/S4214 stay Tier-2/Tier-4 leads with `access_date` UNKNOWN),
   HathiTrust for the pre-FY1965 leg (U.032, the route that could lift the tier), the predecessor-CIK retries
   (U.036), and the five UNVERIFIED-TLS layers whose rows stay Medium (U.028/U.037).
7. **Four registers rest on one emission** (`decisions` 3, `validation` 4, `failure` 1, `channels` 3 — all
   volume 1). Volume 2 and B1 emitted nothing for them, so their thinness is the sections' actual evidence, not
   an omission I repaired by invention.
8. The merged volume's prose still cites dossier-local carriers (`B1S01`, `P1S01`, `P2S08`) by design; global
   uniqueness lives only in the registers plus this pass's id map.
STATUS: WRITTEN 2026-09-26

