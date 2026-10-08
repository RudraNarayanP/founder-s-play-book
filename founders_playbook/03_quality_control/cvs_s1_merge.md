# CVS Health (company_006_cvs) Stage 1 — MERGE RECORD (live, written incrementally)

Agent `merge-cvs`. Operation: merge `_parts/s1_p1.md` (the only part; 22,951 words as emitted, §A–§U complete,
20 claim records CVS-A01…CVS-A20, nine fenced register append blocks totalling **126 rows**) into
`founders_playbook/01_companies/company_006_cvs/stage_1.md` + the nine registers at that directory root +
`_MANIFEST.md` + `CORRECTIONS.md` + `stage_1_index.md`. `_parts/` is **read-only** to this pass: nothing under
it was edited, moved, renamed or renumbered, and it stays the emission of record.

**I am the merger. I did not audit and I do not certify.** Everything below is arithmetic, geometry and the
application of what the part emitted. The five-family table is a restatement of the probe's verdict as carried
by the part, not a new verdict; the probe's tier and family verdicts are **not re-tiered here**.

Status legend per register: **PENDING** = not yet on disk, **APPLIED n rows** = verified on disk at the stated
width. If this file is read mid-operation, the `requested` column is the emission of record and the CSVs are
the ground truth — re-measure, do not trust this tally.

## Rows requested (from the part)

126 rows, from nine fenced blocks in `_parts/s1_p1.md`, each preceded by a `>>> REGISTER ROWS FOR MERGE <<<`
marker naming its target and its own row count: quantitative **29** · timeline **24** · sources **18** ·
conflicts **10** · data_gaps **10** · decisions **14** · validation **8** · failures **7** · channels **6** =
**126**. The marker counts and the parsed row counts agree row-for-row (measured per register below).

## Register application account

| register | requested | applied | cols | status |
|---|---|---|---|---|
| `quantitative.csv` | 29 | **29** | 12 | APPLIED 29 rows (0 off-width; 27 valued/UNKNOWN + counterparty + 3 trade-box rows) |
| `timeline.csv` | 24 | **24** | 11 | APPLIED 24 rows (0 off-width; `source_id` = S4431–S4448) |
| `sources.csv` | 18 | **18** | 18 | APPLIED 18 rows (keys **S4431–S4448**, 0 duplicate keys) |
| `conflicts.csv` | 10 | **10** | 15 | APPLIED 10 rows (keys **U.01–U.10**, 0 duplicates, 1:1 with §U anchors) |
| `data_gaps.csv` | 10 | **10** | 8 | APPLIED 10 rows (S.1–S.10) |
| `decisions.csv` | 14 | **14** | 15 | APPLIED 14 rows (1 geometry fix — see below; 0 off-width after fix) |
| `validation.csv` | 8 | **8** | 11 | APPLIED 8 rows (adjudicated block, §validation/failures above) |
| `failures.csv` | 7 | **7** | 11 | APPLIED 7 rows (adjudicated block, §validation/failures above) |
| `channels.csv` | 6 | **6** | 11 | APPLIED 6 rows |
| **TOTAL** | **126** | **126** | — | **0 unapplied, 0 added by the merge** |

STATUS: APPLIED — 126 requested, 126 on disk. Register integrity checks (run across every block of this one
operation together, not per block): **0** rows off-header-width (after the one geometry fix below); **0** empty
source_id cells; **0** exact duplicate rows across the nine registers; **0** duplicate keys in the two keyed
registers (`sources.csv` 18 unique, `conflicts.csv` 10 unique). `stage` is the literal `stage1` on all 126 rows.
Headers are byte-identical to the corresponding Amazon conformant register headers.

## Geometry fix (content-preserving, schema-only) — decisions.csv row 1

The part emitted `decisions.csv` row 1 (the standing non-claim, `claim_ref = CVS-A20`, "Founding act of the
chain") at **16** fields against a **15**-column header — a stray duplicate `"UNKNOWN"` sitting between
`actual_result` and `source_id`, which shifted `source_id / confidence / claim_ref` one column right. This is
the exact width-shift the wave plan warns about (here a spurious field, not an unquoted comma — every field was
quoted). The merge applied the **minimal** correction: it dropped exactly **one** `"UNKNOWN"` so the row lands
at 15 fields with `source_id = S4432` (the term-census carrier, correct for a "no byte" row), `confidence =
UNKNOWN`, `claim_ref = CVS-A20` in their header columns. **No value was changed, added, or moved; only the one
redundant `UNKNOWN` token was removed.** Re-validated: all 14 decisions rows now 15-wide, 0 off-width. Logged in
`CORRECTIONS.md` as **COR-02**.

Unapplied rows: **none — 126 requested, 126 applied.** No row was dropped, merged away, deduplicated, or
withheld by the merge; nothing was added beyond the emission. The only editorial act on the data was the
PROV→global id remap and the single-field geometry fix above.

## Census BEFORE any write (run first, per the wave plan)

`python tools/merge_census.py --company-dir founders_playbook/01_companies/company_006_cvs --verbose`
(2026-10-07, before the first byte of this merge was written): **9 structured blocks parsed; 2 block-groups
could not be attributed.** Per register — channels requested 6 / unkeyed 6; conflicts 10 / **missing keyed 10**
(`s1_p1.md:U.01 … U.10`); data_gaps 10 / unkeyed 10; decisions 14 / unkeyed 14; quantitative 29 / unkeyed 29;
sources 18 / **missing keyed 18** (`s1_p1.md:PROV-CVS-01 … PROV-CVS-18`); timeline 24 / unkeyed 24.
`TOTAL missing keyed rows: 28`. `present` = 0 everywhere because no register CSV existed at the root before
this pass (`ls` showed only `_parts/`, `research/`, `sources/`).

The 28 keyed-missing rows are exactly the two registers with a primary key (`conflict_id`, `source_id`); the
other seven are censused by count and appear as `unkeyed`, so they can only be checked by counting the written
file — done per register below.

## The validation / failures adjudication (the census cannot decide; I did, by reading)

`validation.csv` and `failures.csv` have a **byte-identical 11-column header**, so the census printed both the
8-row and the 7-row groups as `AMBIGUOUS:validation.csv,failures.csv`. (The content hints the census printed
for those groups are a **tool artifact**, not evidence: `merge_census.py` calls `hint_validation_or_failures`
with the `data` variable from the *previous* loop iteration — the decisions block — so the digests shown were
decisions rows, not the validation/failures rows. I did not rely on them; the plan says to adjudicate by
content, so I read the part directly.) Order the rules bind me to:

1. **Declared target in the part.** `_parts/s1_p1.md` names the 8-row block `targets validation.csv — rows
   emitted: 8` and the 7-row block `targets failures.csv — rows emitted: 7`, each marker immediately preceding
   its fenced block. `_parts/NOTES_cvs_p1.md` §9 states the same widths ("validation 8, failures 7").
2. **Counts close.** 8 + 7 = 15 = the two rows the census listed as unattributed; no row appears in both
   groups, so nothing needed splitting or duplicating to balance.
3. **Content, row by row, against the two registers' semantics** (Amazon's conformant usage: `validation` = a
   signal that validated something; `failures` = an incurred negative):
   - 8-row block: named in national press as RI-based (1980); own 150k sq ft warehouse planned (1983); 789
     stores / 582 pharmacies (1989); second chain bought 490/325m (1990); filed estate 1,284/1,081/38% (1993);
     Marshalls sold (1995); Delaware holding organised, brand becomes registrant (1996); 1,408 stores / $2.4bn
     pharmacy / $573 psf productivity filed (1996). Each `what_it_demonstrated` cell is a positive validation →
     **validation.csv**.
   - 7-row block: strategic review because the parent shape needed answering; $585m + $195m + $230m charges
     (1995); Q4 earnings reduced by the Marshalls timing; footwear discontinued / Kay-Bee / Wilsons / This End
     Up in exit; Peoples name erased across 400 stores; the origin-failure absence-row; the `_FLEET_INTAKE.tsv`
     disclosure-side failure. Each is an adverse or negative-signal row → **failures.csv**.
   - Cross-check: the two sets are non-overlapping in sense as well as in source; the block heading and the
     content agree; **no row was moved between registers.**

## Id allocation (minted centrally, above every live id, never into a gap)

`python tools/id_mint.py --audit` before minting: 351 distinct issued ids, range `S0001–S4430`, highest live
block `company_023_gm S4423..S4430`, tool's own **`next assignable: S4431`**. The audit also prints 17
collisions, of which the one named in my brief is live: **`S4222–S4229` cited by both `company_011_microsoft`
and `company_042_target`** — a range I therefore did **not** allocate into, and did not attempt to repair.

Minted: `python tools/id_mint.py --count 18 --company company_006_cvs --claim --agent merge-cvs` →
**S4431 … S4448** (18 ids, contiguous, allocated above the highest live id, written to
`00_universe/_ID_BLOCKS.tsv` as `company_006_cvs / merge-cvs`).

| provisional (part) | minted (global) | carrier |
|---|---|---|
| `PROV-CVS-01` | **S4431** | Form 8-B12B, `CVS Corporation (Successor to Melville Corporation)`, filed 1996-11-04 — the succession instrument; 0000950103-96-001174 |
| `PROV-CVS-02` | **S4432** | term census over `sources/sec/*.txt` (36 files) — derived measurement, not a witness |
| `PROV-CVS-03` | **S4433** | Form S-4 (Revco merger), 0000950103-97-000191 — the only 1963 carrier; one lineage with its S-4/A + DEF 14A |
| `PROV-CVS-04` | **S4434** | Form 10-K405 FY1996, 0000950135-97-001475 — first annual report of the renamed registrant; prints 1963 zero times |
| `PROV-CVS-05` | **S4435** | Drug Store News layer 1979-10-29→1980-10-13 (micro_IA40706901_0405) — earliest held naming row (1980-01-21) |
| `PROV-CVS-06` | **S4436** | Drug Store News layer 1983-10-31→1984-10-29 (micro_IA40706915_0203) — 1983 warehouse / `Con-sumer` hyphen-healed row |
| `PROV-CVS-07` | **S4437** | Drug Store News layer 1989-11-06→1990-10-22 (micro_IA40706934_0338) — at-a-glance + Peoples; md5-duplicate on corporate_print |
| `PROV-CVS-08` | **S4438** | Drug Store News layer 1990-11-05→1991-10-28 (micro_IA40706938_0038) — 1991 box; carries the Civic Drugs 1963 decoy |
| `PROV-CVS-09` | **S4439** | Drug Store News layer 1994-11-07→1995-10-23 (micro_IA40706951_0247) — Peoples-name-erased row |
| `PROV-CVS-10` | **S4440** | DEF 14A (Melville proxy 1994-03-14), 0000950110-94-000065 — the compensation peer set |
| `PROV-CVS-11` | **S4441** | Form 10-K FY1993, 0000950110-94-000133 — the 1,284 / 1,081 filed segment estate |
| `PROV-CVS-12` | **S4442** | Form 10-K FY1994, 0000891092-95-000026 — `CVS, Inc.` RI + Pharmacare DE; SGML header absent in the stored copy |
| `PROV-CVS-13` | **S4443** | Form 10-K FY1995, 0000891092-96-000050 — ~97,000 associates; Rye NY principal office |
| `PROV-CVS-14` | **S4444** | Form 8-K Item 5 (Marshalls→TJX), 0000950103-95-000374 — the $585m/$195m charge |
| `PROV-CVS-15` | **S4445** | SC 13D by Melville, subject TJX /DE/, 0000950103-96-000813 — third-party filing naming CVS-bearing persons |
| `PROV-CVS-16` | **S4446** | DEF 14A (proxy) 2001-03-15, 0000927016-01-001365 — the director-employment-history 1963 decoy |
| `PROV-CVS-17` | **S4447** | EDGAR submissions index for CIK 64803 (2,968 rows) — index metadata; the S-1/SB-2/10-A 0 / 8-B12B 1 census |
| `PROV-CVS-18` | **S4448** | six annual index volumes (JAPHA / Pharmacy Times) — NULL by construction; 2 md5-duplicates |

Re-minting is mechanical and complete: every `PROV-CVS-nn` token in every applied register row is replaced by
its minted id, including inside compound cells. The part's **narrative** carries no `PROV-CVS-nn` tokens and no
`S\d{4}` source ids (checked), so the mint created no collision with prose; the mapping survives only in this
table and in `stage_1.md`'s merge record. `PROV-CVS-nn` continues to appear verbatim in the read-only part.

## Anchor ↔ conflict parity (measured, not asserted)

The part declared `<!-- ANCHORS: U.01-U.10 -->` (10 anchors), wrote 10 §U subsections (`### U.01 … ### U.10`),
and emitted 10 `conflicts.csv` rows keyed `U.01 … U.10`. The merge proved parity three ways: (i) the
`conflicts.csv` keys on disk are exactly `['U.01','U.02','U.03','U.04','U.05','U.06','U.07','U.08','U.09','U.10']`
(0 duplicates); (ii) after-write `merge_census.py` reads `conflicts.csv | requested 10 | present 10 | missing 0`;
(iii) `gates.py anchors` cross-check (below). **10 narrative anchors ↔ 10 register conflict rows ↔ 10 declared
anchors, 0 orphans in either direction.** No anchor was renumbered; U.01–U.10 are the author's ids.

## CVS-specific carries (kept, not smoothed over — these three are the dossier's spine)

1. **1996 is a reincorporation-by-succession, not an IPO** (conflict **U.03**, claim CVS-A01/A02/A03): the 8-B12B
   filed **1996-11-04** names "CVS CORPORATION (Successor to Melville Corporation)", organised **1996-08-22** under
   Delaware law, with the triangular merger renaming the survivor "CVS New York, Inc."; and **0 rows of
   S-1/S-1/A/SB-2/10-A in 2,968** is the measurement that proves it. Carried verbatim; the merge did not soften
   "successor registration" into "offering".
2. **The corporate-print shelf is not family (d)** (conflict **U.08**): its four files are Internet Archive serial
   layers, two md5-duplicates of the periodicals shelf, so two families do not count and the whole window stays
   **T2** while **S1a/S1b/S1c stay T3 register**. Carried exactly as the probe put it; **not re-tiered.**
3. **U.10 supersedes the probe on the third-party naming lineage**: **6** *Drug Store News* rows
   **1980-01-21→1994-04-25** rather than the probe's 4 rows 1990-1994, with **OCR line-break-hyphen healing** stated
   as the method. "Founded in 1963" remains **COMPANY CLAIM, retrospective, Medium, one lineage** (S-4 + S-4/A +
   merger DEF 14A), with the shoe-store / Jacksonville / Consumer-Value-as-1963-entity folklore **UNKNOWN** and its
   route named. The merge applied the 6 naming rows to `timeline.csv`/`sources.csv` and did not re-import the
   probe's 4-row figure.

## Five-family table as carried (restated from the part/probe; states kept distinct — (b) and (e) UNTRIED)

| family | state as carried | measured basis (part) | in-window Tier-1 text? |
|---|---|---|---|
| (a) SEC / EDGAR | **TRIED–ANSWERED** (identity/S1d; S1a by recital only) | 36 `.txt` + 36 sidecars; 2,968 indexed rows, floor 1994-02-10, 0 before 1994-01-01; `Founded in 1963` in one lineage; FY1996 10-K405 prints `1963` 0 times | **YES** (S1d filings; S1a one recital) |
| (b) Web archives | **UNTRIED — 0 calls** | no `sources/web_archive/` shelf, no CDX artefact; `tools/cdx_intake.py` exists but was never run for CIK 64803 | NO — a route never attempted (S.8) |
| (c) Periodical corpora | **TRIED–ANSWERED** in part; **TRIED–UNANSWERED** for Chronicling America; **57 candidates UNTRIED** at the limit | 16 unique docs; naming 1980→1994; `1963` decoys measured; 2 index-shelf `NULL`s structural | **YES** (S1c/S1d trade press) |
| (d) Digitised corporate print | **TRIED–UNANSWERED (year-faceted)** and **ZERO BYTES** | the 4-file shelf is IA serial layers (2 md5-duplicates of (c)); **not counted as a family** — **U.08** | NO — zero bytes of this family |
| (e) Auction / museum / manuscript | **UNTRIED — 0 calls, and no query block exists for `cvs`** | no shelf, no `tools/queries.json` task; recorded as the missing ask, not a null | NO — never queried (S.6) |

**Families that counted: 2 — (a) and (c) — for the dispatched window ⇒ T2 core carried; S1a/S1b/S1c remain T3
register.** (b) and (e) are stated UNTRIED as such; neither was reported as an answered null.

## Not applied and why — NONE

Every one of the 126 emitted rows is applied to its target register; **no row was dropped, merged away,
deduplicated, or withheld.** The part held two things out of registers **by design** (author's choice, not a merge
drop): the §T.5 manifest-drift prose and the §U.10 measurement-supersession narrative are kept as prose, not forced
into a schema — those are not "rows withheld from a register this part owns." The data edits this merge made were:
(1) the mechanical `PROV-CVS-nn`→`S4431–S4448` remap in every `source_id`-bearing cell (**COR-01**); (2) the
single spurious-`UNKNOWN` width fix on `decisions.csv` row 1 (**COR-02**); (3) the validation/failures block
binding recorded, no row moved (**COR-03**); and (4) the `timeline.csv` foreign-key repair below (**COR-04**).
Nothing else changed.

## Post-write repair — timeline.csv foreign key (COR-04)

`gates.py` found `timeline.csv | source_id token not a key in sources.csv: S4449, S4450, S4451, S4452, S4453,
S4454`. Diagnosis: the author emitted `timeline.csv` `source_id` as a **per-row running counter**
(`PROV-CVS-01…24`) instead of as a foreign key into the 18-row `sources.csv`. Cells 1–18 coincidentally resolve to
real keys; cells 19–24 mapped past the minted block to ids never allocated. The merge repointed **only the six
non-resolving cells** to the carrier each row's own note already names — `S4445` (1996-03-15 TJX-preferred
transfer, the SC 13D) and `S4431` (the four 8-B12B succession rows) — inventing no source. The residual is named
and NOT silently fixed: because the whole column is a counter, several of cells 1–18 resolve as keys but are
semantically mis-pointed (e.g. timeline row 7's true carrier, the 1987 DSN-88 layer, is not among the 18 emitted
sources), so full re-keying would require sources the author did not emit — audit work, which the merger does not
do. Logged as COR-04 in `CORRECTIONS.md`; after the repair `gates.py` reads `timeline.csv.source_id — all S####
tokens resolve`.

## Corrections propagation into the register layer

Because `gate_corrections` treats every `COR-nn` in `CORRECTIONS.md` as needing to reach the register layer
(Cigna and GM do exactly this), each correction is echoed into the register it concerns: **COR-01** in
`sources.csv` S4431 notes; **COR-02** in `decisions.csv` row 1; **COR-03** in `validation.csv` + `failures.csv`
row-1 notes; **COR-04** in `timeline.csv` row-23 notes. These are provenance tags appended inside free-text cells
— no substantive value changed — and the gate now reports `corrections propagation — all 4 reach registers and
volumes`.

## Gate — run after all writes

`python tools/gates.py --company-dir founders_playbook/01_companies/company_006_cvs --tier core --out 03_quality_control/cvs_s1_gates_merge.md`
(`--tier core` passed explicitly because `gates.py --tier auto` cannot read a tier written only as a table row —
the wave plan's stale-belief #3; this is stated, not worked around by editing prose).

**Result: 19 passes, 2 findings.** Passing: `csv` widths for all nine registers (12/11/18/15/8/15/11/11/11);
`source_id` resolution `all S#### tokens resolve` on `timeline/decisions/validation/failures/channels`; `keys`
18 source tokens resolve; `anchors` every register-cited anchor resolves; **`anchors parity — 10 narrative
anchors ↔ 10 register anchors`**; `budget stage_1.md 19,520 words (target 22,000, hard cap 60,000)`; `corrections
propagation — all 4 reach registers and volumes`. The `--tier auto` warning is honoured: budget checked at
`--tier core` = T2's 22,000, not by editing prose.

**The 2 findings are accepted residuals, deliberately NOT reshaped away (method: never reshape data to silence a
gate — name it instead), and are logged in `CORRECTIONS.md` "Not corrected, and why":**

1. `csv quantitative.csv — source_date carries no four-digit year: ['-']`. This is the origin-window UNKNOWN row
   (`date 1963-1979`), whose `source_date = "-"` is the author's honest marker for a metric with **no dated
   carrier** (0 carriers across 36 SEC files + 16 unique press/print docs). Inventing a year would be fabrication.
2. `quotes verbatim — 1 of 11 quoted spans not found`: the §D.2 sentence "…CVS increased distribution capacity by
   [~]a 400,000-square-foot DC in New Jersey…". `[~]` is the author's in-quotation **OCR-corruption marker**
   (CVS-A14, §D "OCR corruption in the 1990 sentence"), so the squashed index cannot match it. A verbatim-check
   question for the citation auditor against the held DSN bytes; the merger did not edit the quotation.

**STATUS: MERGE COMPLETE.** registers APPLIED 126/126; `stage_1.md` (19,520 words), `_MANIFEST.md`,
`CORRECTIONS.md` (COR-01…COR-04), `stage_1_index.md`, and `cvs_s1_gates_merge.md` all written; id block
S4431–S4448 minted and claimed; anchors ↔ conflicts 1:1 (10/10); gate 19 passes / 2 named residuals. The merger
did not audit and does not certify — 2 audits (numbers+hindsight; citation+verbatim) and a certifier (none of whom
is author, merger, auditor, or repairer) are the next passes.
