# PepsiCo Stage 1 — MERGE RECORD (final, re-measured after the last write)

Agent `merge-pepsico`. Operation: merge `_parts/s1_p1.md` (the only part; author `s1-pepsico-p1`, 25,400 words
as emitted, Header + boundary + §A–§U + claim records `P1-01…P1-42` + nine fenced register blocks, every section
marked `STATUS: WRITTEN`, no PENDING section) into
`founders_playbook/01_companies/company_046_pepsico/stage_1.md` + the nine registers at that directory root +
`_MANIFEST.md` + `CORRECTIONS.md` + `03_quality_control/pepsico_s1_gates_merge.md`.

**I am the merger. I did not audit and I do not certify.** Everything below is arithmetic, geometry and
application of what the part emitted; the five-family table restates the probe's verdict as the part carried it,
it is not a new verdict. An audit by a different agent must re-measure every number here.

Status legend: **APPLIED n rows** = verified on disk at the stated width, counted from the written file, not from
this tally.

## Tier: T3 register — the probe's measurement governs, not the dispatch label

The wave plan dispatched `s1-pepsico-p1 … T2 22k`; the same plan's standing correction is that **the probe's
measured tier governs, not the dispatch label**. Probe §A.7 measured **T3 register** for 1A, 1B, 1C and for the
stage (1B/1C PROVISIONAL); the author wrote to T3 and logged the disagreement rather than silently re-tiering,
and registered it at **U.15**. This merge applied the T3 frame and ran the gate with **`--tier register` passed
explicitly** (wave-plan correction 3: `--tier auto` cannot read a table-row verdict; it printed
`tier: exemplar …` for this company's probe and the author recorded that as a tool default, not a finding, at
§A.11 of the probe and in U.15). The budget line the gate then prints is an **advisory** overage against the
8,000-word density target — §15.2 and RD-122 — and **nothing was trimmed, split or re-tiered to silence it**.
The volume is 22,958 words, under the §9.2 soft target of 40,000 and far under the 60,000 hard cap.
Registered as **COR-02**.

## Rows requested — 106

Nine fenced `csv` blocks at `_parts/s1_p1.md` l.999–l.1175, each under a `### <register>.csv — <header>` heading
and its own `>>> REGISTER ROWS FOR MERGE <<<` marker, each stating its own count; the part's closing paragraph
(l.1177–l.1182) totals them — `sources 16, quantitative 25, timeline 16, conflicts 15, data_gaps 15, decisions 4,
validation 4, failures 8, channels 3 = 106` — and `_parts/NOTES_pepsico_p1.md` states the same nine numbers. The
parsed blocks agree with the stated counts row for row: no register over- or under-emitted, and the author's own
line "**Rows withheld: none**" is confirmed on the bytes.

## Register application (requested ↔ applied, measured on the written files)

| register | requested | **applied** | cols | key / integrity check |
|---|---|---|---|---|
| `sources.csv` | 16 | **APPLIED 16 rows** | 18 | keys S4479–S4494, 0 duplicate keys, 0 empty cells |
| `quantitative.csv` | 25 | **APPLIED 25 rows** | 12 | no row key; 0 duplicate row texts, 0 empty cells |
| `timeline.csv` | 16 | **APPLIED 16 rows** | 11 | no row key; `source_id` repeats as a carrier reference (3 repeats are citations, not duplicate rows); **2 empty cells in the nullable `conflict_ref`** (named below) |
| `conflicts.csv` | 15 | **APPLIED 15 rows** | 15 | keys U.1–U.15, 0 duplicate keys, 0 empty cells |
| `data_gaps.csv` | 15 | **APPLIED 15 rows** | 8 | no row key; 0 duplicate row texts, 0 empty cells |
| `decisions.csv` | 4 | **APPLIED 4 rows** | 15 | no row key; 0 duplicates, 0 empty cells |
| `validation.csv` | 4 | **APPLIED 4 rows** | 11 | adjudicated block — see the validation/failures section |
| `failures.csv` | 8 | **APPLIED 8 rows** | 11 | adjudicated block — see the validation/failures section |
| `channels.csv` | 3 | **APPLIED 3 rows** | 11 | no row key; 0 duplicates, 0 empty cells |
| **TOTAL** | **106** | **APPLIED 106 rows** | — | **0 unapplied · 0 added by the merge · 0 folded · 0 refused** |

Whole-operation integrity, run across all nine files together: **0** rows off-header-width; all nine headers
**byte-identical** to `company_001_amazon/<name>.csv` line 1 (read as raw bytes and written back, never retyped);
`stage` = the literal **`stage1` on 106/106 rows** (a per-file distinct-value scan returned `['stage1']` nine
times — **0 numeric stage values, so there is no §13 normalisation count to report**); **0** duplicate keys in the
two keyed registers; **0** exact duplicate rows; UTF-8, LF line endings, no CR anywhere, RFC-4180 quoting.

### Every unapplied row, named

**There are none.** No emitted row was dropped, folded into another, deduplicated, refused, or left in prose; no
row was added to a register that the part did not emit. Two things are nevertheless named rather than smoothed:

1. **2 empty cells** — `timeline.csv` `conflict_ref` on the 1973 DERIVED row and on the 1995-01-06 EDGAR-floor
   row. `conflict_ref` is a nullable column: those two rows register no conflict, and inventing an anchor
   reference to make the column look full would be authoring, not applying. Left exactly as emitted.
2. **16 provisional tags** — `P1S01…P1S16` survive in the volume's narrative as the author's local labels and as
   alias text inside `sources.csv`; they are **superseded as keys**, which is the residual `sources.csv` "missing"
   count in the census-after table below.

## Id allocation (minted centrally, above every live id, never into a gap)

`python tools/id_mint.py --count 16 --company company_046_pepsico --claim --agent merge-pepsico` →
**S4479, S4480, S4481, S4482, S4483, S4484, S4485, S4486, S4487, S4488, S4489, S4490, S4491, S4492, S4493,
S4494** — contiguous, 16 ids, allocated above the highest live id.

`--audit` before the mint reported `next assignable: S4463` and 17 collisions; the mint landed at S4479 because a
concurrent merge in the same queue took S4463–S4478 between my audit and my mint. That is the intended behaviour
of central monotonic allocation: nothing was reused, no gap was re-entered, and no other company's held number
was touched. The audit's named live collision — **`S4222–S4229` cited by both `company_011_microsoft` and
`company_042_target`** — sits below this block; I did not allocate into it and did not attempt to repair it.
`sources.csv` is global-append-only (§9.4).

Map (full carrier descriptions live in `stage_1.md`):
`P1S01→S4479` K94 FY1994 10-K · `P1S02→S4480` REG95 S-3 · `P1S03→S4481` K99 FY1999 10-K · `P1S04→S4482` EX21
subsidiaries · `P1S05→S4483` S4Q+S4QA · `P1S06→S4484` OP5 counsel opinion · `P1S07→S4485` AR17 (the only merger
sentence) · `P1S08→S4486` CAT48 (the only in-window dated document) · `P1S09→S4487` PR74 · `P1S10→S4488` PX20 (the
`1893` trademark) · `P1S11→S4489` AR20/PX22/PX23/PX24 · `P1S12→S4490` YUM08 (A&W) · `P1S13→S4491` ERIC ·
`P1S14→S4492` LAY layer census · `P1S15→S4493` IDX submissions index · `P1S16→S4494` RUN/UNA/HMX/A4 ledgers.

Every `P1Sxx` token in a register cell was re-pointed to its minted id (token-level, inside cells the author
said the merge would re-key); the superseded tag is kept as an alias in the `notes` cell of the row that replaces
it — nothing deleted. Gate confirmation: `csv … .source_id all S#### tokens resolve` for `timeline`,
`validation`, `failures`, `decisions`, `channels`; **0 dangling source tokens** measured directly across all eight
non-`sources` registers.

## The validation/failures adjudication (COR-06) — and how I decided

`validation.csv` and `failures.csv` are byte-identical in their 11 columns, so `merge_census.py` printed the 4-row
and the 8-row groups as `AMBIGUOUS:validation.csv,failures.csv`, and **its content hints scored all 12 rows as
`either`** — the hints carried no signal whatever, so the pair had to be adjudicated by reading, and the decision
is on the record:

1. **Emit headings** — `_parts/s1_p1.md` l.1138 `### validation.csv — <header>` sits over the 4-row block and
   l.1150 `### failures.csv — <header>` over the 8-row block; each marker names its target exactly as the other
   seven blocks do.
2. **The author's stated counts** — both the part's closing paragraph and `NOTES_pepsico_p1.md` say
   "validation 4, failures 8"; the blocks parse to 4 and 8. No count tension, so nothing hung on the reading.
3. **Content, row by row** — the 4-row block's `what_it_demonstrated` cells each state **what a carrier
   established**: S4486's in-window programme spend and national reach, S4479's asserted dividend-increase streak
   inside a legal disclosure, S4480/S4481's disclosed licensing scale; its first row is the *measured absence* of
   any validation signal, which belongs to this register because its subject is validation, reported as nothing.
   The 8-row block's cells each state **a failure of retrieval or of the toolchain**: the empty pass-1 against the
   harvester's 1898→1965 window, the three 404 NoSuchKey documents, the `--max-docs 30` cap that left 88 in-window
   filings unlisted, the `drop_year_facet` artefact that reports corporate print as 0 B, the two layers filed
   under the wrong person or year, the unledgered `ERIC_ED337649` arrival, the probe's unparseable CLI form. That
   is §M.2's subject, which is `failures.csv`'s subject.
   Cross-check: no row text appears in both groups; 4 + 8 = 12 = the census's entire unattributed total.
4. **What was *not* used**: the keyword hints themselves (all `either`), and the census's ordering. A schema
   property is not evidence.

After this pass the two registers are no longer unattributable **on disk** — they carry their rows under their own
names — but `merge_census` will keep printing the pair as `AMBIGUOUS` for this company, because it reads the
_read-only part file_. That residual is a tool property, recorded here and at COR-06, not a missing row.

## Census BEFORE the first write

`python tools/merge_census.py --company-dir founders_playbook/01_companies/company_046_pepsico --verbose`
(run before the first byte of this merge was written): 9 blocks parsed, **2 block-groups unattributed**,
**TOTAL missing keyed rows: 31** = `conflicts.csv` 15 (`s1_p1.md:U.1 … U.15`) + `sources.csv` 16
(`s1_p1.md:P1S01 … P1S16`). Requested: channels 3 · conflicts 15 · data_gaps 15 · decisions 4 · quantitative 25 ·
sources 16 · timeline 16 (+ the ambiguous 4 and 8) = **106**. `present` = 0 in every register: no CSV at the
company root and none under `research/`.

## Third-emission check (the census is blind to `research/*.csv`)

Before any write, `*.csv` inside the company directory existed **only** as intake inventories under `sources/`
(`sources/_index/submissions_CIK0000077476.csv`; `sources/sec/_MANIFEST.csv`, `_PLAN.csv`, `_SKIPPED.csv`,
`_UNANSWERED.csv`) — inventories of bytes fetched, not register rows. `research/` held **0 CSV** and neither
dossier (`A_chronology_feasibility.md`, `A4_harvest_mine.md`) emits a register block. **106 is the whole
request**; there is no hidden 65-row or 25-row third emission here of the Tesla kind. Re-checked after the final
write: the nine live registers are the only CSVs at the root and `research/` still holds none.

## Census AFTER the final write (same command, on the finished bytes)

| reading | before | after |
|---|---|---|
| structured blocks parsed | 9 | 9 |
| rows requested | 106 | **106** |
| `conflicts.csv` present / missing | 0 / 15 | **15 / 0** ← anchor parity proven by the tool |
| `sources.csv` present / missing | 0 / 16 | 0 / **16** — the 16 are the superseded `P1S01…P1S16` tags read out of the read-only part; the live keys are S4479–S4494 (COR-01) |
| TOTAL missing keyed rows | 31 | **16**, fully accounted by the row above |
| unattributed block-groups | 2 | 2 — a schema property of the two registers, adjudicated on the record (COR-06) |
| unkeyed rows | channels 3 · data_gaps 15 · decisions 4 · quantitative 25 · timeline 16 | unchanged, all on disk, counted by row |
| third emissions | 0 | **0** |

**Requested 106 ↔ applied 106.** Nothing is unaccounted for.

## Anchors ↔ conflicts parity — 15 declared, 15 registered, 1:1

Declared by the part and preserved verbatim at the head of the carried body (the anchor declaration line):
**U.1–U.15, 15 ids.** Narrative entries on disk: `### U.1 … ### U.15` — **15 §U subsection headings**, each
counted in the volume. Register rows: `conflicts.csv` keys `U.1 … U.15`, **15 rows, 0 duplicates**.
Proof from the tools, not from my arithmetic: `merge_census` → `conflicts.csv requested 15 / present 15 /
missing 0`; `gates.py` → `anchors | parity | 15 narrative anchors <-> 15 register anchors` and
`anchors | citation resolution | every register-cited anchor resolves (15 distinct ids …)`. No orphan in either
direction, no seventh-style mismatch, no renumbering, no §U text moved to make a count agree. The other eight
registers cite those same 15 ids (`timeline.conflict_ref`, `data_gaps` gap text, `quantitative`/`failures` notes)
and every cited id resolves.

## The four load-bearing results carried by this merge

1. **The origin is refused, not chosen.** `1893`, `1898`, `1902` = **0 occurrences**, and the census was extended
   from the probe's 27 SEC documents to **all 38 held items** (27 filings + 11 print layers). The corpus's single
   `1893` is a **trademark name** in the 2020 marks list (S4488, U.8), not a date. The registrant's own recital —
   "incorporated in Delaware in 1919 and reincorporated in North Carolina in 1986" — accounts for **13
   attributable occurrences of the 14** (the 14th is A&W's founding in S4490), so **1919 is a charter recital,
   not a founding** (U.2, U.7). The harvester's `1898-01-01 → 1965-12-31` window stays **rejected**: its start has
   0 occurrences, it silently adopted both contested dates, and it is the measured cause of the fleet's empty
   pass-1 (`pass1_docs=0`). Stage 1 is carried as **1B 1919–1964**, **1C 1965–1986**, plus **1A** as a named,
   explicitly **undated** claim-slot. Carried in: `timeline.csv` rows 1893/1898/1902 (all `UNKNOWN - no carrier`),
   the `quantitative.csv` zero-occurrence rows, `conflicts.csv` U.1/U.2/U.7/U.8.
2. **The author superseded its own probe, and this merge preserved that** (COR-03). The probe's A.3 "the merger
   story itself: UNKNOWN — no carrier in this corpus" is refuted by `01-pepsi-co` **l.122** — the PepsiCo **2017**
   shareholder letter signed Indra K. Nooyi, "Two years later, in 1965, Frito-Lay and Pepsi-Cola merged to form
   PepsiCo." → **one carrier, one lineage, 52 years late → Low / RESTATED**, registered at **U.10** and not
   written as if the probe had been wrong about everything (everything else stands: the folklore zeros, the two
   origin lines, the ex-21 subsidiary finding, the single-lineage verdict, the five-family states, T3).
   **"Five filings corroborate 1965" stays refused**: they are one lineage (§3), and the clause's second half —
   "increased for 22 consecutive years" in the FY1994 10-K — arithmetically dates **1973** (`1994 − 22 + 1`),
   which is a **DERIVED row, not corroboration** (U.11; the `quantitative.csv` 1973 row; the `timeline.csv` 1973
   row; `decisions.csv` 1965 row keeps `UNKNOWN` for who decided, the day and month, the consideration and the
   survivor).
3. **`CAT48` stays the stage's single contemporaneous witness, not a founding record.** The only in-window dated
   document naming an origin-line person: Pepsi-Cola Company, Fourth Annual Exhibition, venues 1947-10-01 →
   1948-04-18, foreword signed "Walter S. Mack, Jr., President", $15,250 of awards, ~650,000 calendars. Carried at
   S4486, the two 1947–48 timeline rows, the two quantitative rows, the channels/validation rows, and U.14 — each
   stating that it witnesses **existence and activity of the subsidiary-line person** and dates nothing about the
   origin.
4. **Family (d) was enumerated, not fetched** — **TRIED as to existence / UNFETCHED as to text**, never a null and
   never counted as a second witness: `ia_text.py list-files --id 01-pepsi-co` → **102 layers, 17,860,942 B**, of
   which **27 pre-1965 (917,852 B)** and **21 in 1965–1986 (1,994,223 B)**, 7 tagged `(Frito-Lay)` 1958–1964, 1984
   missing (S4492, `data_gaps.csv` S-10/S-11, the three archive-layer quantitative rows, U.4/U.5/U.15). The two
   decoys are carried as decoys: `YUM08`'s only 1919 founding is **A&W** (U.7) and `PR74` names
   **Pepsi Cola Canada Ltd.**, a different person (U.12).

## The five families, as carried (TRIED / UNANSWERED / UNTRIED kept distinct)

| family | state carried into the registers | register / volume home |
|---|---|---|
| **(a) SEC / EDGAR** | **TRIED–ANSWERED, post-window only** — 27 documents / 17 accessions, md5-unique, 5,645,960 B; perimeter 1995-01-06 → 2026-09-17 over 3,058 index rows; **0** rows in 1965-01-01…1986-12-31; the floor is a measured archive perimeter, not a silence | S4479–S4484, S4493; `timeline.csv` 1919 / 1995-01-06 / 2000-12-30; `data_gaps.csv` S-06, S-12, S-13; `failures.csv` rows 2–4; §boundary 3 |
| **(b) web archives** | **UNTRIED — 0 calls**, no `sources/web_archive/` path; never reported as empty | `data_gaps.csv` S-14; §Untried item 1 |
| **(c) periodical corpora** | **TRIED–UNANSWERED** for the queries (CA/HT/GB cap- or host-blocked; the IA wide set sampled to row 20 of numFound 747) **and TRIED–ANSWERED** for the 11 layers already delivered (4,130,659 B; one in-window dated, one belonging to another registrant) | S4485–S4491; `conflicts.csv` U.10, U.14; `failures.csv` rows 6–7; §Untried items 3–4; FETCH 2, FETCH 3 |
| **(d) digitised corporate print** | **TRIED as to existence, UNFETCHED as to text**; `sources/corporate_print/` is 0 B because of the `drop_year_facet` artefact — an artefact, not a null; 48 in-window layers named and costed | S4486, S4492; `data_gaps.csv` S-10, S-11; `conflicts.csv` U.4, U.5, U.14, U.15; `failures.csv` row 5; FETCH 1 |
| **(e) auction / museum / manuscript** | **UNTRIED**, and no query block for the family exists corpus-wide — a structural hole, not a PepsiCo miss | `data_gaps.csv` S-14; §Untried item 2; FETCH 5 |

Family count for §15.2: **one** family returns in-window Tier-1 text held on disk (S4486). ≤1 → **T3**. No state
was averaged, upgraded, or reported as a null by this merge.

## Tool facts recorded so a later agent does not refuse a script

- `sec_intake auto` **works** — `version_aside()` keeps the previous run record beside the new one (RD-139) and
  `grab`'s enumeration is fixed (RD-138). Neither was needed here (a merge does no intake); recorded so the stale
  belief does not turn a runnable script into a fetch request (§15.1).
- `ia_text.py` requires **`list-files --id <identifier>`** — `mode` is positional, the identifier is a flag; the
  form printed in the probe's FETCH REQUEST 1 does not parse. The author's measurement, carried at U.15 and
  `failures.csv` row 8 (S4492).
- `gates.py --tier auto` cannot read a table-row verdict: pass `--tier register` and say so. Done, stated above.
- **The scratch enumeration was moved.** The author left `list-files`' stdout at the repository root as
  `_tmp_pepsico_layers.json`; this merge moved it, **byte-for-byte unchanged** (9,794 B), to
  `founders_playbook/01_companies/company_046_pepsico/_parts/_tmp_pepsico_layers.json`, cited it from
  `sources.csv` S4492 and `data_gaps.csv` S-10, and annotated the three places in the volume that pointed at the
  root path (§T.1 row, claim record P1-33, the closing coverage paragraph). The repo root now carries no company
  scratch; nothing was re-run and no count changed. Registered as **COR-04**.

## Volume, index and claim records

`stage_1.md`: **22,958 words / 150,036 bytes**, `wc`-class word count re-measured after the last write. Build =
MERGE RECORD header (3,169 words) + the author's body **verbatim** (19,789 words): Header, boundary, §A–§U,
§T.2's claim records, `## Untried`, `## Fetch requests`, the closing paragraph. **No section letter, claim id,
anchor id or metric id was renumbered; no narrative was rewritten, reordered, trimmed or summarised.**

Non-destruction proof, line by line: 25,400 (part as emitted) −21 (the part's filename H1, replaced by the
volume H1) −6,245 (the nine fenced blocks with their headings and markers, moved into the CSVs per §9.1(2),
COR-05) +557 (nine printed pointers naming each register, its applied row and column counts, its `_parts/` line
range and **DO NOT RE-APPLY**) +98 (the §registers scope note, 54 words, plus three COR-04 path annotations, net
44) = **19,789** body; +3,169 header = **22,958**. Verified two ways on the bytes: exactly **13** body lines are
not verbatim in the part (the 9 pointers, the scope note, the 3 annotated lines), and exactly **13** part lines
are absent from the volume (the same 4 lines in annotated form, the H1, and the 9 lines of the footer this pass
appended to the part itself). **No author line is lost.** Counts held after the merge: 42 claim records
(`P1-01 … P1-42`, all present), 15 §U headings, 12 `## Untried` items, 5 FETCH REQUESTS, 1 anchor declaration.

**No `stage_1_index.md`** (one volume; §9.3 lists an index under the split procedure) and **no
`stage_1_claim_records.md`** (the 42 records are §T.2 of the narrative; cutting them out would split a section at
a non-appendix boundary). Both refusals are stated in the volume's header rather than left silent, because GM and
Cigna did the opposite on dossiers whose shape differed. `_parts/s1_p1.md` is untouched above its last line; a
dated `MERGED / SUPERSEDED` footer was appended below it, and its wording limits its reach to **placement and
key-space**.

## Corrections propagation (COR-01 … COR-06)

`CORRECTIONS.md` carries six entries and each id reaches **both** the register layer and the volume — the check
the `corrections` gate runs. Gate line: `corrections | propagation | all 6 retraction(s) reach registers and
volumes`; measured note: "6 retraction ids; register layer reaches 6, volumes 6".

| id | what it records | register rows tagged |
|---|---|---|
| COR-01 | provisional `P1S01–P1S16` → minted `S4479–S4494`, aliases kept | `sources.csv` 16 |
| COR-02 | dispatch label T2 superseded by the probe's measured T3; `--tier register` stated | `conflicts.csv` U.15 |
| COR-03 | probe A.3 "no carrier" superseded on the merger point by AR17 l.122 → Low/RESTATED, U.10 | `conflicts.csv` U.10, `quantitative.csv` 1 row, `timeline.csv` 1 row |
| COR-04 | layer census relocated from the repo root into `_parts/` | `sources.csv` S4492, `data_gaps.csv` S-10 |
| COR-05 | the nine blocks moved out of prose into the CSVs (§9.1(2)) | `sources.csv` S4479 |
| COR-06 | the validation/failures pair adjudicated by content, method recorded | `validation.csv` row 1, `failures.csv` row 1 |

## Gate (final, run after every write, on the finished bytes)

```
python tools/gates.py --company-dir founders_playbook/01_companies/company_046_pepsico \
  --tier register --out founders_playbook/03_quality_control/pepsico_s1_gates_merge.md
```

Result: **Findings 2 | Passes 18** (`pepsico_s1_gates_merge.md` / `.json`). Passing: `csv` on all nine registers
at width (16×18, 25×12, 16×11, 15×15, 15×8, 4×15, 4×11, 8×11, 3×11), `source_id` tokens resolve in `timeline`,
`validation`, `failures`, `decisions`, `channels`; `anchors` citation resolution and **parity 15 ↔ 15**;
`corrections` propagation all 6. The two findings:

1. **`advisory | stage_1.md | 22,958 words over the register density target 8,000`** — advisory by design
   (§15.2: a density target is not a file limit; RD-122), the reason `--tier register` was passed explicitly.
   Not repaired: no evidence was cut, no section deleted, no split performed, no tier changed.
2. **`quotes | verbatim | 3 of 12 quoted spans not found in local sources`** — the gate's corpus is
   `sources/**/*.txt|htm*` only, and all three spans quote **project-internal text it does not index**, each
   verbatim in a held file:
   - `supporting data lives in CSV never inside prose files` — `00_METHOD_AND_STYLE.md` §9.1(2), quoted in my own
     merge header;
   - `the merger story itself unknown no carrier in this corpus` — `research/A_chronology_feasibility.md` A.3
     (also quoted by the author at §U.10): `grep -c` on that dossier = 1;
   - `unverified tls re check before citing at high confidence` — the `transport` field of
     `sources/periodicals/*.meta.json` (`.json` is outside the gate's index): `grep` finds it verbatim in the
     `01-pepsi-co`, `1974-12-press-release` and `ERIC_ED337649` sidecars.
   Per the dispatch rule the data was left alone and the evidence recorded; **no quote was deleted, rewritten or
   reshaped to silence a detector.** The pre-merge run (`pepsico_s1_gates_p1.md`) had no quote check at all
   (`--checks csv,keys,anchors,corrections`), so this finding is a scope property newly exposed, not a regression.

**A finding I caused and fixed:** the first gate run also printed
`keys | stage_1.md | unresolvable source tokens: S4463` — my own merge header cited the audit's
`next assignable` number as if it were a key. That is neither author data nor register data, so I rephrased my
sentence to state that S4463 **was taken by a concurrent merge**; the second run reads it as protected history
(`keys … mentions 3 retired keys inside collision/re-key/range text`). Nothing in the author's text was touched
to clear it.

## Residue, named not dropped

1. **Five FETCH REQUESTS stay open**, unexecuted by this pass: FETCH 1 (the 48 in-window corporate-print layers,
   2,912,075 B — the single route that could lift 1B/1C to T2), FETCH 2 (CA/HT past the 600-cap and the CP
   `year_range` fix), FETCH 3 (the 747-hit IA set filtered `date<=1965`), FETCH 4 (the 1962 candidate, the 404
   corn item, and the 1965 registration statement, which needs SEC legacy paper), FETCH 5 (the Delaware registry —
   the only route to a **first independent lineage** for this registrant). None is a null; each has a register
   row.
2. **Five pipeline defects recorded, not repaired** (§M.2): the `drop_year_facet` CP artefact, the two mislabelled
   layers, the unledgered `ERIC` arrival, the `--max-docs 30` cap, the probe's CLI form. They live in `tools/` and
   in intake, outside a merge's WRITE scope; I touched no tool.
3. **The tier-vs-cap tension is the orchestrator's, not mine**: a T3 dossier emitted 106 rows and 15 conflicts,
   which is exemplar-shaped output measured against a register cap. I did not re-tier it in either direction.
4. **Re-apply hazard, mitigated not removed**: the 106 rows exist once in the CSVs and once as text in
   `_parts/s1_p1.md`; the volume no longer prints them, and both the volume and the part say **DO NOT RE-APPLY**.
5. **Outbound, not mine to edit**: `_parts/NOTES_pepsico_p1.md` still names the repo-root scratch path, and
   `00_universe/_AUTHOR_WAVE_PLAN.md` still carries the `T2 22k` dispatch label. Both are handed to their owners;
   `MASTER_RESEARCH_LOG.md` and `RESUME_HANDOFF.md` were not opened by this pass.

## Claims released

`stage_1.md`, `_MANIFEST.md`, `CORRECTIONS.md`, the nine register CSVs, `_parts/s1_p1.md` (footer append only) and
`_parts/_tmp_pepsico_layers.json` (the relocation) — 14 paths, each claimed with
`python tools/scaffold.py claim --path … --agent merge-pepsico`, none forced, each released `--done` at the close
of this pass. `03_quality_control/pepsico_s1_merge.md` and `pepsico_s1_gates_merge.md` are this operation's QC
outputs.

**Merger's limit on this report:** I assembled, applied, verified and published. I did **not** audit and I do
**not** certify; the numbers above are measurements of my own writes and of the part's emission, and an audit by
a different agent must re-measure them.

STATUS: COMPLETE — 106 requested / 106 applied · 22,958-word volume · anchors 15 ↔ conflicts 15 · gate 2 findings
(1 advisory, 1 quotes-scope) · 0 unapplied rows
