# FORENSIC LONGITUDINAL DATASET — PEPSICO, INC., STAGE 1 (PROPOSED 1919-01-01 → 1986-12-31, IN THREE SUB-STAGES, PLUS ONE UNDATED SLOT) — T3 REGISTER DOSSIER

## MERGE RECORD (assembly, application, id map, adjudications, anchor parity, carry-forward)

Merged 2026-10-07 by `merge-pepsico` from the single part `_parts/s1_p1.md` (author `s1-pepsico-p1`; Header,
boundary, §A–§U, the 42 claim records in §T.2, and nine fenced register blocks; 25,400 words as emitted, every
section marked `STATUS: WRITTEN`, no PENDING section). Deliverables of this operation: this volume, the nine
register CSVs at this directory root, `_MANIFEST.md`, `CORRECTIONS.md`, and
`03_quality_control/pepsico_s1_merge.md` + `pepsico_s1_gates_merge.md`.

**Section letters, claim ids and anchor ids are the author's and were not renumbered** (method §9.3 — numbering
continues, it is never re-based). Nothing in the narrative was rewritten, trimmed, re-tiered or merged away;
`_parts/s1_p1.md` stays read-only as the emission of record and carries a dated `MERGED / SUPERSEDED` footer
appended by this pass, below the author's last line.

**What moved out of the prose.** The nine `>>> REGISTER ROWS FOR MERGE <<<` blocks (6,245 words of the part) are
register data, not narrative (§9.1(2): "supporting data lives in CSV, never inside prose files"). They were
**applied** to the nine CSVs, and in the volume each block is replaced at its own heading by a printed pointer
naming the register, its row count, its column count and the `_parts/` line range where the verbatim emission
survives, with **DO NOT RE-APPLY** (COR-05).

**What did not move.** The claim records `P1-01 … P1-42` stay in §T.2 of this volume: they are narrative in the
§7 line format, and §T.2 is a subsection of §T, so pulling it out would cut a section at a non-appendix
boundary. No `stage_1_index.md` was written: this company has exactly one volume, and §9.3 lists an index under
the **split** procedure — an index of one file would be a stub. Both choices are recorded here rather than left
silent, because GM and Cigna (which had a standalone appendix and parts respectively) did the opposite.

### Register application (requested ↔ applied, measured on the bytes written)

| register | rows requested | rows applied | cols | key / integrity |
|---|---|---|---|---|
| `sources.csv` | 16 | **16** | 18 | keys S4479–S4494, 0 duplicate keys |
| `quantitative.csv` | 25 | **25** | 12 | no key column; 0 duplicate row texts |
| `timeline.csv` | 16 | **16** | 11 | no key column; `source_id` repeats as a carrier reference |
| `conflicts.csv` | 15 | **15** | 15 | keys U.1–U.15, 0 duplicate keys |
| `data_gaps.csv` | 15 | **15** | 8 | no key column; 0 duplicate row texts |
| `decisions.csv` | 4 | **4** | 15 | no key column; 0 duplicate row texts |
| `validation.csv` | 4 | **4** | 11 | adjudicated block — see COR-06 |
| `failures.csv` | 8 | **8** | 11 | adjudicated block — see COR-06 |
| `channels.csv` | 3 | **3** | 11 | no key column; 0 duplicate row texts |
| **TOTAL** | **106** | **106** | — | **0 unapplied, 0 added by the merge, 0 folded, 0 refused** |

Every header is byte-identical to the corresponding `company_001_amazon/<name>.csv` line 1 (read as raw bytes
and written back, not retyped); `stage` is the literal `stage1` on all 106 rows of all nine files; a width scan
across the whole operation at once gives **0** rows off-header-width; UTF-8, LF endings, RFC-4180 quoting.
**Unapplied rows: none.** No row was dropped, deduplicated, folded or withheld, and no row was invented to even
out a thin register.

### Id allocation and the provisional-to-global map

Minted centrally, never into a gap: `python tools/id_mint.py --count 16 --company company_046_pepsico --claim
--agent merge-pepsico` → **S4479 … S4494** (contiguous, 16 ids, allocated **above the highest live id**).
`--audit` before the mint printed a next-assignable value of **S4463**, but that number was taken by a
concurrent merge in the same queue between my audit and my mint, so this block landed at S4479 — which is
exactly why allocation is central and monotonic, and why no id here was reused or redefined. The audit's live
collision set,
**`S4222–S4229` cited by both `company_011_microsoft` and `company_042_target`**, sits below this range: it was
not allocated into and not touched. `sources.csv` is global-append-only (§9.4).

| provisional | minted | carrier |
|---|---|---|
| P1S01 | **S4479** | 10-K FY1994 (`K94`, acc. 0000077476-95-000017) — both origin sentences, the floor figures, the director-tenure decoy |
| P1S02 | **S4480** | Form S-3 1995-01-06 (`REG95`) — earliest document held for the CIK; equals the EDGAR floor |
| P1S03 | **S4481** | 10-K FY1999 (`K99`) — the 440/240 territory disclosure; recital spaced so a tight grep misses it |
| P1S04 | **S4482** | Exhibit 21, subsidiaries as of 12/30/2000 (`EX21`) — 91 countable jurisdiction rows; `Pepsi-Cola Company` and `Frito-Lay, Inc.` both Delaware, both undated |
| P1S05 | **S4483** | S-4 + S-4/A Quaker (`S4Q`, `S4QA`) — the corpus's only worked merger instrument, (PB) for Stage 1 |
| P1S06 | **S4484** | Exhibit 5.1 counsel opinion 2001-02-28 (`OP5`) — "a North Carolina corporation", no date printed |
| P1S07 | **S4485** | `AR17` — IA item `01-pepsi-co`, the 2017 layer; l.122 is the corpus's **only merger sentence** |
| P1S08 | **S4486** | `CAT48` — Pepsi-Cola Company's Fourth Annual Exhibition, venues 1947-10-01 → 1948-04-18, foreword signed Walter S. Mack, Jr., President |
| P1S09 | **S4487** | `PR74` — Concordia University release, Dec 1974, naming `Pepsi Cola Canada Ltd.` (a different person) |
| P1S10 | **S4488** | `PX20` — DEF 14A 2020 layer: the corpus's single `1893`, a **trademark name** |
| P1S11 | **S4489** | `AR20`/`PX22`/`PX23`/`PX24` — post-window reprints of the same dividend clause |
| P1S12 | **S4490** | `YUM08` — another registrant's 2008 annual report filed under this company's item name; its `1919` is A&W's |
| P1S13 | **S4491** | `ERIC` ED 337 649 — the only third-party naming of Frito-Lay outside the registrant's filings; absent from both harvest ledgers |
| P1S14 | **S4492** | `LAY` — the `ia_text.py list-files --id 01-pepsi-co` census: 102 layers, 17,860,942 B |
| P1S15 | **S4493** | `IDX` — EDGAR submissions index for CIK 0000077476, 3,058 rows, floor 1995-01-06 |
| P1S16 | **S4494** | `RUN`/`UNA`/`HMX`/`A4` — intake and harvest tool ledgers, LEAD ONLY, never counted in a tier verdict |

Every `P1Sxx` token inside a register cell was re-pointed to its minted id; the superseded local tag is kept as
an alias inside the `notes` cell of the row that replaces it (nothing deleted). The narrative below keeps the
author's local tags — this table is the only place the two key spaces meet.

### The validation/failures adjudication (COR-06) — how this merge decided

`validation.csv` and `failures.csv` share a byte-identical 11-column header, so `merge_census.py` printed the
4-row and the 8-row groups as `AMBIGUOUS:validation.csv,failures.csv`, and its content hints scored **every one
of those 12 rows as `either`** — the hints carried no signal, so the decision was mine and is recorded here.

1. **Emit headings.** `_parts/s1_p1.md` l.1138 is `### validation.csv — <its header>` and l.1150 is
   `### failures.csv — <its header>`; each `>>> REGISTER ROWS FOR MERGE <<<` marker sits under its own target
   heading, exactly as the other seven blocks do.
2. **The author's stated counts.** The volume's closing paragraph (l.1180–l.1182) and
   `_parts/NOTES_pepsico_p1.md` both state "validation 4, failures 8"; the blocks parse to 4 and 8. There is no
   count tension, so nothing turns on a guess.
3. **Register semantics, row by row.** The 4-row block populates `what_it_demonstrated` with something a carrier
   **established**: the beverage-line person's in-window programme spend and national reach (S4486), management's
   asserted dividend-increase streak inside a legal disclosure (S4479), the disclosed scale of the licensing
   apparatus (S4480/S4481); its first row is an explicit *measured absence* of any validation signal, which
   belongs to this register because its subject is what validated nothing. The 8-row block populates the same
   column with **defects**: the empty pass-1 run against the harvester's window, the three 404 NoSuchKey
   documents, the `--max-docs 30` cap, the `drop_year_facet` artefact that reports corporate print as empty, the
   two layers filed under the wrong person or year, the unledgered `ERIC` arrival, the probe's unparseable CLI
   form. Each is a failure *of the retrieval or of the toolchain* — §M.2's subject and this register's.
   Cross-check: no row text appears in both groups, and 4 + 8 = 12 = the census's whole unattributed total.

### Anchors ↔ conflicts parity (proved by census and by gate, not asserted)

Declared by the part and preserved verbatim at the head of the carried body (the anchor declaration line,
`U.1-U.15`): **15 ids, U.1 to U.15**, each with its own §U narrative entry (`### U.1` … `### U.15`). On disk:
`conflicts.csv` keys = `U.1 … U.15`, **15 rows, 0 duplicate keys** — one row per anchor, 1:1.
`merge_census.py` after the write reports `conflicts.csv requested 15 / present 15 / missing 0`, and the gate
reports parity **15 narrative anchors ↔ 15 register anchors** with no orphan in either direction. No anchor was
renumbered, and no §U text was moved to make a count agree.

### Census before and after the same bytes

| reading | before | after |
|---|---|---|
| structured blocks parsed | 9 | 9 |
| rows requested | 106 | **106** |
| `conflicts.csv` present / missing | 0 / 15 | **15 / 0** ← parity proven |
| `sources.csv` present / missing | 0 / 16 | **0 / 16** — the 16 are the superseded `P1S01–P1S16` tags the census reads out of the read-only part file; the live keys are S4479–S4494 (COR-01) |
| TOTAL missing keyed rows | 31 | **16**, fully accounted by the row above |
| unattributed block-groups | 2 (the 4-row and the 8-row group) | 2 — a schema property of the two registers, now adjudicated on the record (COR-06), not a missing row |
| unkeyed rows | channels 3 · data_gaps 15 · decisions 4 · quantitative 25 · timeline 16 | unchanged, all on disk and counted by row |
| third emissions under `research/` | 0 | **0** |

### The four load-bearing results this merge carried unchanged

1. **The origin is refused, not chosen.** `1893`, `1898` and `1902` have **0 occurrences**, and the census was
   extended from the probe's 27 SEC documents to **all 38 held items** (27 filings + 11 print layers); the single
   `1893` in the corpus is a **trademark name** in a 2020 marks list (S4488), not a date. The registrant's own
   recital — "incorporated in Delaware in 1919 and reincorporated in North Carolina in 1986" — accounts for
   **13 attributable occurrences of the 14** (the 14th is A&W's founding, in S4490), so **1919 is a charter
   recital, not a founding** (U.2, U.7). The harvester's `1898-01-01 → 1965-12-31` window stays **rejected**: its
   start has 0 occurrences, and it is the measured cause of the fleet's empty pass-1 (`pass1_docs=0`). Stage 1 is
   carried as **1B 1919–1964** and **1C 1965–1986**, with **1A** kept as a named, explicitly **undated**
   claim-slot.
2. **The author superseded its own probe, and this merge preserved that.** The probe's A.3 verdict — "the merger
   story itself: UNKNOWN — no carrier in this corpus" — is refuted by `01-pepsi-co` **l.122**, a 2017
   shareholder letter signed Indra K. Nooyi printing "Two years later, in 1965, Frito-Lay and Pepsi-Cola merged
   to form PepsiCo." That is **one carrier, one lineage, 52 years late → Low / RESTATED**, and the supersession
   is registered as **U.10** rather than written as though the probe had been wrong about everything (COR-03).
   What stays refused, and is in the registers as refused: that "five filings corroborate 1965" — they are
   **one lineage** (§3), and their second clause ("increased for 22 consecutive years", FY1994) arithmetically
   dates **1973** (`1994 − 22 + 1 = 1973`), which is a **DERIVED row, not corroboration** (U.11; the
   `quantitative.csv` 1973 row; the `timeline.csv` 1973 row).
3. **`CAT48` is kept as the stage's single contemporaneous witness, not as a founding record.** It is the only
   in-window dated document in the corpus naming an origin-line person — Pepsi-Cola Company, 1947–48, President
   Walter S. Mack Jr., $15,250 of awards, ~650,000 calendars — and every row that uses it says what it witnesses
   (S4486, the two 1947–48 `timeline.csv` rows, the two `quantitative.csv` rows, the `channels.csv` and
   `validation.csv` rows, U.14). It establishes **existence and activity of the subsidiary-line person**; it
   dates nothing about the origin.
4. **Family (d) was enumerated, not fetched** — a **TRIED as to existence / UNFETCHED as to text** state, never a
   null and never a second witness: `ia_text.py list-files --id 01-pepsi-co` → 102 text layers, 17,860,942 B, of
   which **27 pre-1965 (917,852 B)** and **21 in 1965–1986 (1,994,223 B)**, 7 of them tagged `(Frito-Lay)` for
   1958–1964, with 1984 missing (S4492; `data_gaps.csv` S-10 and S-11; the three archive-layer
   `quantitative.csv` rows; U.4, U.5). The two decoys are carried as decoys: `YUM08`'s only 1919 founding is
   **A&W** (U.7), and `PR74` names a **Canadian** person, not the US constituent (U.12).

### The five families, as the probe issued them and as this merge carried them

| family | state carried into the registers | register / volume home |
|---|---|---|
| **(a) SEC / EDGAR** | **TRIED–ANSWERED, post-window only** — 27 documents / 17 accessions, md5-unique, perimeter 1995-01-06 → 2026-09-17 over 3,058 index rows, **0** rows inside 1965–1986 | S4479–S4484, S4493; `timeline.csv` 1919 / 1995-01-06 / 2000-12-30 rows; `data_gaps.csv` S-06, S-12, S-13; `failures.csv` rows 2–4; §boundary 3 |
| **(b) web archives** | **UNTRIED — 0 calls**, no `sources/web_archive/` path at all (a route never attempted, never a null) | `data_gaps.csv` S-14; §Untried item 1 |
| **(c) periodical corpora** | **TRIED–UNANSWERED for the queries** (CA/HT/GB capped or host-halted; the IA wide set sampled to row 20 of numFound 747) and **TRIED–ANSWERED for the 11 layers those queries already delivered** | S4485–S4491; `conflicts.csv` U.10, U.14; `failures.csv` rows 6–7; §Untried items 3–4; FETCH 2, FETCH 3 |
| **(d) digitised corporate print** | **TRIED as to existence, UNFETCHED as to text**; the YEAR-faceted zero is a tool artefact, not an empty shelf (`sources/corporate_print/` is still 0 B while CP-classified items sit in `sources/periodicals/`) | S4486, S4492; `data_gaps.csv` S-10, S-11; `conflicts.csv` U.4, U.5, U.14, U.15; `failures.csv` row 5; FETCH 1 |
| **(e) auction / museum / manuscript** | **UNTRIED** — no path, no sidecars, and no query block for the family corpus-wide (a structural hole, not a PepsiCo miss) | `data_gaps.csv` S-14; §Untried item 2; FETCH 5 (the Delaware registry is the only route to a first independent lineage) |

Family count for the tier rule (§15.2): **one** family returns in-window Tier-1 text held on disk — S4486, the
subsidiary-line person — so ≤1 → T3. No family state was averaged, upgraded or reported as empty by this merge.

### Tier: the probe's measured T3 governs, not the dispatch label

The wave plan dispatched this company at **T2 22k**; its own standing correction is that **the probe's measured
tier governs, not the dispatch label**. Probe §A.7 measured **T3 register** for 1A, 1B, 1C and for the stage
(1B/1C PROVISIONAL); the author wrote to T3 and logged the disagreement instead of silently re-tiering (U.15);
this merge applied the same frame and ran `gates.py` with **`--tier register` passed explicitly**, because
`--tier auto` cannot read a table-row verdict (wave-plan correction 3) and the word-cap check must be measured
against the T3 target of 8,000 rather than against a label. The resulting budget line is an **advisory** overage
(§15.2: a density target, not a file limit) and the volume sits far under the §9.2 hard cap — **nothing was
trimmed, split or re-tiered to silence a gate** (RD-122, §9.6).

### Tool facts this merge recorded so a later agent does not refuse a script

- `sec_intake auto` **works**: `version_aside()` keeps the previous run record beside the new one (RD-139), and
  `grab`'s enumeration branch is fixed (RD-138). Neither was needed by this pass — a merge does no intake — and
  both are recorded so the stale belief does not turn a runnable script into a fetch request (§15.1).
- `ia_text.py` needs the **`list-files --id <identifier>`** form: `mode` is positional and the identifier is a
  flag. The form printed in the probe's own FETCH REQUEST 1 (`list-files 01-pepsi-co`) does not parse — the
  author's measurement, carried at U.15 and in `failures.csv` row 8 (S4492).
- `gates.py --tier auto` cannot read a table-row verdict: pass `--tier core|register` and say so. Done above.
- **The layer enumeration now lives inside this company's directory.** The author left its `list-files` stdout at
  the repo root as `_tmp_pepsico_layers.json`; this merge moved it, unchanged byte-for-byte, to
  `founders_playbook/01_companies/company_046_pepsico/_parts/_tmp_pepsico_layers.json`, cited it in two register
  cells and annotated the three volume places that pointed at the repo root (COR-04), so the repo root carries
  no company scratch.

### Corrections opened by this merge (all six reach the registers and this volume)

| id | what changed | where it lands |
|---|---|---|
| **COR-01** | the author's provisional `P1S01–P1S16` are superseded by minted `S4479–S4494`; register cells re-pointed, local tags kept as aliases in `notes` | `sources.csv` all 16 rows + the re-pointed cells of the other eight registers |
| **COR-02** | the dispatch label **T2 22k** is not this company's tier: the probe's measured **T3 register** governs, and the gate was run with `--tier register` stated on the record | `conflicts.csv` U.15 residual cell; the tier section above |
| **COR-03** | the probe's A.3 "merger: UNKNOWN — no carrier" is **superseded on that one point** by `AR17` l.122; the merger is now **Low / RESTATED**, one carrier, one lineage; everything else the probe measured stands | `conflicts.csv` U.10, `quantitative.csv` merger row, `timeline.csv` 2017 row |
| **COR-04** | the layer census `_tmp_pepsico_layers.json` was **relocated** from the repo root into `_parts/`; three path references in the volume annotated in place | `sources.csv` S4492, `data_gaps.csv` S-10, §T.1, claim record P1-33, the volume's closing paragraph |
| **COR-05** | the nine register blocks were **moved out of the prose** into the CSVs (§9.1(2)); placement only, no claim withdrawn; the verbatim emission stays in `_parts/` | `sources.csv` S4479 notes cell; the nine printed pointers in §registers |
| **COR-06** | the census's `AMBIGUOUS:validation.csv,failures.csv` pair was **adjudicated by content** (the hints scored all 12 rows `either`); the decision is recorded, not silently applied | `validation.csv` row 1, `failures.csv` row 1, the adjudication section above |

**Nothing outside this company's directory was edited.** The wave plan's two corrected tool beliefs are recorded,
not repaired; `tools/` and `00_universe/` were not touched. The five pipeline defects the author listed in §M.2
(the CP YEAR-facet artefact, the two mislabelled layers, the unledgered `ERIC` arrival, the `--max-docs 30` cap,
the probe's CLI form) stay **recorded, not repaired** — they are tool and intake matters outside a merge's WRITE
scope, each already carries a register row, and each has a FETCH REQUEST. The five FETCH REQUESTS are **not**
executed by this pass: a merge applies emissions, it does not retrieve bytes.

<!-- ANCHORS: U.1-U.15 -->

## Header

STATUS: WRITTEN 2026-10-06

**Dataset:** The Founder's Playbook — forensic reconstruction of what each company in the frozen universe
(`00_universe/`) looked like while its outcome was still unknown.

**Company (rank 46):** today's registrant **PEPSICO, INC.**, CIK **0000077476** (`sources/sec/_RUN.json`
`registrant`/`cik`, read this pass). Fortune rank 46.

**File:** Stage 1, **part 1 of 1** — Header, boundary, **§A–§U** and the nine register append blocks, all in
this volume. Section letters, claim IDs (`P1-xx`) and register row keys (`P1Sxx`/`P1Qxx`/`P1Txx`/`P1Dxx`/
`P1Vxx`/`P1Fxx`/`P1Cxx`/`P1Gxx`) are dossier-local and run continuously into whatever volume the merge
assembles. Cross-references use the form `(PepsiCo S1 §K, part_1)`.

**Dossiers consolidated (read in full this pass, in this order):** `03_quality_control/STAGE1_AUTHOR_BRIEF_SHARED.md`;
`00_METHOD_AND_STYLE.md` §3–§9, §13–§15; `company_046_pepsico/research/A_chronology_feasibility.md`
(probe `probe-pepsico`, **T3**, five-family verdict, A.1–A.12); `company_046_pepsico/research/A4_harvest_mine.md`
(a **later** dossier, mtime 2026-10-06 18:14, which **post-dates the probe** and reports mined periodical bytes
the probe's A.1 measured as zero). Format exemplar: `company_001_amazon/_parts/s1_p1.md` read **for format
only**; no Amazon value, date or phrasing is imported.

**Tier: T3 REGISTER** (probe A.7; RD-112 tier-per-stage). The later dossier `A4_harvest_mine.md` **does not
regrade it**, and this pass says why in §A.4 after measuring A4's bytes: no family yields **in-window
Tier-1 text held on disk about an event inside 1919–1964 except one document** (§D.2), and no family yields
**any** in-window text about the 1893–1918 slot. §K, §N and §U are therefore still mandatory, and the
`UNKNOWN`s are the deliverable. Per RD-122 the 8k-word T3 planning cap is a dispatch budget, not a limit on
written evidence; nothing is trimmed to fit it and no section is deleted for being unpopulated (§7 "adapt,
never delete").

**Carrier labels used throughout** (a line number is a locator, not an address — §14 r12):

| label | file (all paths under `company_046_pepsico/sources/`) | form, filed | lineage |
|---|---|---|---|
| `REG95` | `sec/0000077476-95-000002_0000077476-95-000002.txt` | S-3, 1995-01-06 | registrant |
| `K94` | `sec/0000077476-95-000017_0000077476-95-000017.txt` | 10-K FY1994, 1995-03-28 | registrant |
| `K95`…`K99` | `sec/0000077476-96-000023…`, `-97-000007…`, `-98-000014…`, `-99-000013…`, `-00-000006…` | 10-K FY1995–FY1999 | registrant |
| `K2000` | `sec/0000077476-01-500016_k2000.htm` | 10-K FY2000, 2001-03-15 | registrant |
| `EX21` | `sec/0000077476-01-500016_ex21.htm` | ex-21 to FY2000 10-K, as of 12/30/2000 | registrant |
| `S4Q` / `S4QA` | `sec/0000912057-01-000830_a2034530zs-4.txt` / `sec/0000912057-01-007577_a2039895zs-4a.txt` | S-4 + S-4/A, 2001-01-09 / 2001 (Quaker) | registrant, second registration |
| `OP5` | `sec/0000950103-01-500049_ex5-1.txt` | ex-5.1 legal opinion, dated **February 28, 2001** | registrant's own counsel |
| `REG01` | `sec/0000950103-01-500049_s3.txt` | S-3, 2001 | registrant |
| `AR17` | `periodicals/01-pepsi-co_djvu.txt` | IA item `01-pepsi-co`; **the held layer is `PepsiCo, Inc. (PEP) Annual Report 2017_djvu.txt`** (sidecar `url`) | registrant, corporate print |
| `CAT48` | `periodicals/cor5_0_s06_ss01_boxrg5_0_2008_006_f61_djvu.txt` | "PEPSI-COLA COMPANY'S Fourth Annual Exhibition Paintings of the Year", venues 1947-01 … 1948-04 | **Pepsi-Cola Company print** |
| `PR74` | `periodicals/1974-12-press-release_djvu.txt` | Concordia University (Montreal) release, Dec 1974 | **third party** |
| `YUM08` | `periodicals/pepsicofritolayannualreports_djvu.txt` | IA item mislabelled to PepsiCo; held layer is `yum2008_djvu.txt` = **YUM! Brands, Inc. 2008** AR | **another registrant** |
| `AR20`,`PX20`,`PX22`,`PX23`,`PX24` | `periodicals/pepsi-co-inc.-pep-*_djvu.txt` | PEP annual report 2020 + proxies 2020–2024 | registrant, corporate print |
| `ERIC` | `periodicals/ERIC_ED337649_djvu.txt` | ERIC/CE doc. ED 337 649, names **Frito-Lay** workplace-literacy program | federal education report |
| `NPTG` | `periodicals/NPTG19060630_djvu.txt` | Hongkong Telegraph, 1906-06-30 | third party, **0 Pepsi naming** |
| `IDX` | `_index/submissions_CIK0000077476.csv` | EDGAR submissions index | regulator index |
| `RUN`,`UNA` | `sec/_RUN.json`, `sec/_UNANSWERED.csv` | intake sidecars | tool ledger |
| `HMX`,`A4`,`LAY` | `harvest_mine/_index.json`; `research/A4_harvest_mine.md`; this pass's `ia_text.py list-files --id 01-pepsi-co` census | harvest ledgers | tool ledger |

**Cell convention:** *carrier label*, *tier*, *class* — "verbatim" [claim ID]. `FACT-about-the-corpus` = a
measurement of what this repository holds; it proves reach, never a company fact.

**Label form.** Every carrier label above is dossier-local and carries **no hyphen on purpose**: a
hyphen-with-year token reads to a machine as a global record key — `gates.py`'s keys check flagged exactly
that form for the two S-3 carriers in this volume's first draft, which is why they are printed as `REG95`
(1995) and `REG01` (2001). Global `source_id`s are minted centrally at merge; none is asserted here.

**Independence accounting (§3, stated once and enforced on every row).** This corpus holds **38 documents**
(27 SEC + 11 periodical layers), **0 byte-identical duplicates** (`md5sum` over all 38 → no duplicate digest,
measured this pass) — and **zero second independent witnesses to any origin date**. The 27 SEC documents are
one registrant across 17 accessions; the `AR17`/`AR20`/`PX20`/`PX22`/`PX23`/`PX24` print layers re-print the
same corporate record the filings recite ("a company's own reprinted history pages and its filings … are one
source", §3), so **13 of the 14 occurrences of `1919` in this whole corpus are the registrant's own sentence in
two media**. The remaining `1919` is another company's founding (`YUM08` l.9009, A&W). Only three carriers in
the entire corpus are **not** the registrant talking about itself: `CAT48` (Pepsi-Cola Company's own 1947–48
art-exhibition catalogue — the *subsidiary's* print, not the registrant's), `PR74` (a Canadian university's
1974 release naming `Pepsi Cola Canada Ltd.`) and `IDX` (the regulator's own index). **Not one of them prints
a founding date.** `CAT48` is nevertheless the only in-window self-naming corporate person in the corpus and is
carried as such in §D.2.

**Confidence (§3):** **High** = primary document for its own year or 2+ independent origins; **Medium** = one
reliable source, or a retrospective-only primary; **Low** = conflicting, vague, or retrospective-only with no
primary carrier; **UNKNOWN** = a finding, not a gap to fill or smooth.

**Hindsight firewall (§2).** Nothing here treats the registrant's later scale as evidence about the origin
period. The FY1994 figures quoted in §K/§P are **corpus-floor data** — the earliest numbers the archive
reaches — labelled `(floor)`; they are never used as Stage-1 performance, and the 1995–99 franchise geography
in §G is described as *what the filing printed about 1995*, not as what the franchise system "was" in 1920.
The words "visionary", "prescient", "legendary" and "iconic" appear **zero** times in this volume. No coda in
§C/§D/§L asserts a consequence without naming evidence, mechanism and an alternative, or writing
`mechanism UNKNOWN`.

**ID scheme (§13).** `source_id` is left **provisional/dossier-local on every row** and is minted centrally at
merge by `tools/id_mint.py`; nothing here assumes a global key. `stage` is the controlled literal `stage1` on
every row of all nine registers. CONTEMPORANEOUS vs RESTATED is labelled per row.

STATUS: WRITTEN

---

## boundary

STATUS: WRITTEN 2026-10-06

**Geometry note.** This section enumerates the candidate Stage-1 subjects and windows, names the held carrier
behind each, and says why each rival **fails**. It does not assert a boundary and then defend it rhetorically.

### 1. The harvester's window is rejected, and why

`tools/harvest_mine.py:71` sets this company's Stage-1 window verbatim as
`"pepsico": ("1898-01-01", "1965-12-31")`, and `research/A4_harvest_mine.md` l.3 restates it and defends it as
"deliberately WIDE where the founding date is itself unestablished". **Rejected.** That window is a search
parameter, not evidence (RD-112), and its two endpoints silently adopt the two most contested dates in this
company's folklore — **1898** as the origin and **1965** as the terminal event — while this corpus prints
`1898` **0 times in 38 documents** and prints `1965` 22 times of which **exactly one** states a merger (§P.2,
`P1-06`/`P1-09`). A window whose start date has 0 occurrences and whose end date's meaning is asserted rather
than carried is not a boundary; it is a guess that then selects which bytes get mined. `tools/fleet_intake.py`
read the same table for pass 1 and stored **0 documents** against it (`_FLEET_INTAKE.tsv` `pass1_docs=0`,
probe A.1) — the parameter also caused a wasted intake pass, which is the practical cost of the same error.

### 2. Candidate windows, each bounded by a printed carrier or refused

| # | candidate | endpoints printed by | verdict |
|---|---|---|---|
| 1 | **1893 / 1898 / 1902 → 1918** (the syrup, the pharmacist, the brand before a charter) | nothing held. `1893: 1` (a **brand name**, §U.8), `1898: 0`, `1902: 0`, `pharmacist: 0`, `Bradham: 0`, `Caleb: 0`, `since 18: 0` across all 38 documents | **REFUSED as a window; kept as an explicitly UNDATED slot (stage 1A).** No endpoint may be adopted from a 0-occurrence term. The slot's upper bound is the first carrier-printed date above it (1919); its lower bound is `UNKNOWN`. |
| 2 | **1919-01-01 → 1964-12-31** (the beverage charter line) | open: the registrant's own oldest self-date, 13 occurrences in 13 documents (`REG95` l.462; `K94` l.125–126; …; `AR17` l.1364). close: `AR17` l.122 "Two years later, in 1965, Frito-Lay and Pepsi-Cola merged" | **ADOPTED (stage 1B).** Both ends are printed by held bytes; the open is the registrant's own record (Medium, single lineage), the close is a 2017 retrospective sentence (Low). |
| 3 | **1965-01-01 → 1986-12-31** (the merged registrant) | open: `K94` l.557–559 "since PepsiCo was formed in 1965" and `AR17` l.122; close: 8 filings print "reincorporated in North Carolina in 1986" | **ADOPTED (stage 1C).** This is the only sub-stage whose **both** endpoints are printed in held bytes; the day and month of the 1965 act remain `UNKNOWN`. |
| 4 | 1919-01-01 → 1965-12-31 (one merged stage, close at the merger) | carriers as above | **REJECTED as the whole of Stage 1.** It would silently make the registrant's reincorporation (1986) — a second change of the same legal person printed in the same sentence as its 1919 charter — a Stage-2 event, and it would drop the only in-window corporate-print route the corpus can name (21 archive layers, 1965–1986, §A.4). |
| 5 | "as far back as the brand goes" (1893 → today) | importer's folklore | **REJECTED — hard rule 4.** Importing a *brand* lineage into a *registrant* chronology is the Morgan Stanley / AT&T / Ford / Kroger defect class this project has already paid for. On its own word the registrant begins in 1919 (§U.2). |

**Proposed Stage-1 window, from carriers: 1919-01-01 → 1986-12-31**, carried as sub-stages **1B** and **1C**,
with **1A** retained as a named, **undated** claim-slot so the origin folklore stays visible and stays
`UNKNOWN` instead of disappearing. The whole span is 68 years and the corpus holds **0 documents dated inside
it** as documents (§boundary 3): every Stage-1 statement below is therefore registrant-retrospective or
third-party-peripheral, and that is the finding, not a shortfall of this pass.

### 3. Where the record physically stops — re-measured this pass, not inherited

`IDX` = **3,058 rows**, `min filingDate 1995-01-06`, `max 2026-09-17`; **rows before 1995-01-06 = 0**;
**rows with filingDate in 1965-01-01..1986-12-31 = 0** (all four numbers computed this pass over the CSV after
enumerating its header). So the 1995-01-06 floor is a measured perimeter of EDGAR's own archive for this CIK,
**not** "PepsiCo filed nothing"; the 1965 registration statement or merger proxy for the merged person is
simply not in the family-（a）reach of this toolchain (§S, §U.10). `RUN` (read this pass): `attempted 106 =
stored 27 + unanswered 4 + skipped 75`, `identity_ok: true`, `bytes 5,645,960`, `words 703,025`, intake window
`1965-12-31..2006-12-31`. `UNA`: three `UNANSWERED` rows are the **same accession**, 8-K `0000077476-00-000047`
(2000-12-04) documents `0001.txt/0002.txt/0003.txt`, 404 NoSuchKey on all three path forms, plus a fourth row
recording that **88 in-window filings were never listed** because `--max-docs 30` was reached — a capped
enumeration, and therefore not a census (§14.14, RD-134).

**What the boundary does NOT claim.** (i) Not that 1919 is the founding of the drink, the brand, or the snack
line — it is the registrant's recital of a Delaware **charter** (§U.1, §U.2). (ii) Not that the 1965 sentence
proves a merger happened on a proven date: it proves the registrant **says in 2017** that two named persons
merged in 1965, and separately that it has paid quarterly dividends since 1965 (§U.6, §U.11). (iii) Not that
"Pepsi-Cola Company" or "Frito-Lay, Inc." is the registrant: `EX21` lists both, with jurisdiction
`Delaware`, **as subsidiaries** of PepsiCo, Inc. as of 12/30/2000 — so each is a separate legal person inside
the group, and **neither is given an incorporation date anywhere in the corpus** (§U.13). (iv) Not that the
1A slot is empty because it is empty: families (b) and (e) are **UNTRIED** and (c)/(d) are partly
TRIED–UNANSWERED (§S, `## Untried`). (v) Not that the archive's silence about 1938–1964 is a corporate silence:
27 in-window corporate-print layers exist in the archive and are **unfetched** (§A.4).

STATUS: WRITTEN

---

## A

STATUS: WRITTEN 2026-10-06

### A.1 The state of the origin question at the end of Stage 1, as far as this corpus can state it

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Who the registrant says it is | "PepsiCo, Inc. (the 'Company') was incorporated in Delaware in 1919 and was reincorporated in North Carolina in 1986." | `K94` l.125–126, T1, RESTATED [P1-01] — printed in 8 filings and reprinted in 5 print layers | **Medium** — the registrant's own corporate record, one lineage, never independently witnessed |
| What it says the merged person is | "Quarterly cash dividends have been paid since PepsiCo was formed in 1965" | `K94` l.557–559, T1, RESTATED, **inside the dividend-policy paragraph** [P1-02] | Medium as to the printing; **Low** as to what 1965 did |
| What the 1965 act was | "Two years later, in 1965, Frito-Lay and Pepsi-Cola merged to form PepsiCo." | `AR17` l.122 (shareholder letter, Indra K. Nooyi, Chairman and CEO), T1 corporate print, RESTATED [P1-03] | **Low** — the only merger sentence in 38 documents; written 52 years after the event by a CEO who did not perform it; one lineage |
| The two origin-name persons | `Pepsi-Cola Company \| Delaware` and `Frito-Lay, Inc. \| Delaware` appear in the subsidiary exhibit, undated | `EX21`, parsed rows l.677–678 and l.313–314 (raw l.1366), T1, FACT (of the listing) [P1-04] | High that they are listed; **UNKNOWN** when either was incorporated |
| The creator of the drink | **Absent from the corpus entirely.** `pharmacist 0`, `Bradham 0`, `Caleb 0`, `1893` only as a brand name, `1898 0`, `1902 0` | whole-corpus census, §P.2 [P1-05] | **UNKNOWN** — not a null: families (b)/(e) UNTRIED, (c)/(d) TRIED–UNANSWERED |
| The snack line's founder | **Absent.** `Herman Lay 0`; the 4 `Herman` hits are "EGEA Hermanos S.A.", "Sherman Act" ×2 and an artist named "SARAI SHERMAN" | `K98`, `S4Q`, `S4QA`, `CAT48` [P1-06] | **UNKNOWN** — keyword decoy, rule 6 |
| Stage-1 events dated inside the window by a document | **None.** 0 filings in 1965-01-01..1986-12-31; 1 in-window **document** of any kind held: `CAT48` (1947–48) | `IDX`, §boundary 3 [P1-07] | High (FACT-about-the-corpus) |

**The finding, stated plainly.** Two origin lines and a merger are three different acts, by different persons,
and the corpus can date none of them from outside the company's own voice. (a) The act that would create the
syrup has **no** named agent, date or place in any of the 38 documents. (b) The act the registrant does claim
— a Delaware incorporation in 1919 — is a **charter** statement about a legal person, reprinted 13 times in
two media and witnessed by nobody. (c) The 1965 act is a merger of two named persons stated once, in 2017, in
a shareholder letter — and it is the **merged** person, a third legal person, that the 1919 recital belongs
to. Because Exhibit 21 keeps both origin-name persons alive **inside** the group as subsidiaries, neither can
be collapsed into "the registrant" to make the chronology tidy (hard rule 4).

### A.2 What is knowable and what is not, in one list

**Knowable from held bytes:** the registrant's self-recital (1919 / 1965 / 1986); the existence and Delaware
situs of `Pepsi-Cola Company` and `Frito-Lay, Inc.` as subsidiaries at 12/30/2000; the corporate-print fact
that `Pepsi-Cola Company` was an operating named person with a President in 1947–48 (`CAT48`); the
franchise-appointment structure as printed in 1995–2000; the corpus-floor financial and territorial state
1994–2000 (§K, §P).
**Not knowable from held bytes:** who created the drink; when; under what name; when either origin-name person
was incorporated; what the 1965 merger certificate said; whether 1965 was a merger of the two named persons
or a re-naming; the day and month of every Stage-1 act; any in-window price, output, capitalisation,
headcount, or first-customer datum; and whether the 1893/1898/1902 rivalry can be settled at all (§S).

### A.3 Coda (with its three duties)

**Evidence:** the origin chronology of rank-46 rests on exactly two sentences in the registrant's own voice
and one in its own 2017 print. **Mechanism:** a registrant's Item 1 sentence is a *legal-person* statement
(the charter and the reincorporation are what the instrument needs for its own identification), while a
shareholder letter's merger sentence is a *brand-continuity* statement; neither genre was ever intended to
date the product, so neither is weak on the origin for reasons internal to the record and not because this
pass searched badly. **Alternative explanation:** the corpus could be silent because the origin documents were
never digitised (EDGAR's floor for this CIK is 1995-01-06 — `IDX` measured), *not* because the company has no
earlier history; the 27 unfetched in-window corporate-print layers (§A.4) are direct evidence that
in-window print exists and this repository simply has not pulled it. Confidence in the two recitals as
statements-of-the-record: **Medium**; in the events they describe: **Low**.

### A.4 The one route that could change this dossier's tier — measured, still unfetched

This pass ran a script that already exists, `python tools/ia_text.py list-files --id 01-pepsi-co` (the probe's
route, named there in the wrong CLI form — `list-files 01-pepsi-co` is rejected as a positional; `--id` is
required; measured error quoted in §M.3), and got the decisive census of the compilation item `01-pepsi-co`,
"PepsiCo Annual Reports: 1938-":

| measure (LAY) | value |
|---|---|
| text layers in the item | **102**, **17,860,942 B** of OCR text |
| layers whose name prints **"PepsiCo, Inc. (PEP) Annual Report <year>"** | **86**, years **1938–2024**, one gap at **1984** |
| of those, layers dated **1938–1964** (inside stage 1B) | **27 layers, 917,852 B** — **none fetched** |
| of those, layers dated **1965–1986** (inside stage 1C) | **21 layers, 1,994,223 B** — **none fetched** |
| layers carrying the parenthetical **"(Frito-Lay)"** | **7** — exactly **1958, 1959, 1960, 1961, 1962, 1963, 1964** |
| layers named for other registrants | `Pepsi Bottling Group (PBG)` ×9 (1999–2008), `PepsiAmericas, Inc. (PAS)` ×5 + 1 ×1999 "(Whitman Corporation-WH)" |
| bytes of this item actually held | **only the 2017 layer** (`AR17`, 520,419 B), per its own sidecar `url` |

Two consequences, both register-grade. **(1) The label is anachronistic on its face:** 27 layers print
"PepsiCo, Inc." for years in which, on the registrant's own word, PepsiCo, Inc. did not exist, and the
uploader's own "(Frito-Lay)" tag on 1958–1964 concedes that at least those seven are a **different person's**
annual reports (§U.4, U.5). **(2) The tier hinge is now measurable rather than hopeful:** 48 in-window layers
(27 + 21), 2,912,075 B, are the second family the probe said would be needed to lift 1B/1C from T3 to T2.
**This pass did not fetch them** (fetching writes bytes into `sources/periodicals/`, outside my WRITE scope;
§15.1 routes script-reachable retrieval to the orchestrator), so family (d) stays **bytes-held = 0 in-window**
for the registrant's own pre-1965 print, and the tier stays **T3** — but with a named, costed FETCH REQUEST
(`## FETCH REQUEST 1`) instead of a hope.

### A.5 The five corpus families as this pass found them (three states only; an untried family is never a null)

| family | state as found by this pass | measurement | remedy / route |
|---|---|---|---|
| **(a) SEC / EDGAR filings** | **TRIED–ANSWERED, post-window only** | 27 documents / 17 accessions, md5-unique, 5,645,960 B (`RUN` re-read); perimeter re-measured from `IDX`: 3,058 rows, 1995-01-06 → 2026-09-17, 0 rows before the floor, **0 rows in 1965-01-01..1986-12-31** | nothing fetchable: the 1965 instrument is outside this family's reach (paper era). FETCH REQUEST 4 names the human route |
| **(b) web archives** | **UNTRIED — 0 calls by this pass, 0 by the probe** | still no `sources/web_archive/` path (re-enumerated this pass) | CDX pass in Microsoft's `cdx_microsoft_com_earliest_200.json` shape, for PepsiCola.com / fritolay.com, 1996–2005 |
| **(c) periodical corpora** | **TRIED–UNANSWERED for the queries; TRIED–ANSWERED for the bytes those queries already delivered** | CA/HT/GB rows remain cap- and host-blocked (inherited, not re-run by this pass); the IA wide set is still sampled only to row 20 of numFound 747; but 11 layers totalling 4,130,659 B are now on disk and were read here, of which **one is dated inside the window** (`CAT48`) and one belongs to another registrant (`YUM08`) | FETCH 2 and FETCH 3; page the 747-hit set filtered `date<=1965` |
| **(d) digitised corporate print** | **the probe's YEAR-faceted zero is an artefact, not a null — this pass converted the family from UNTRIED-by-order to TRIED as to existence and UNFETCHED as to text** | `sources/corporate_print/` is still 0 B while CP-classified items sit in `sources/periodicals/`; `LAY` measured the compilation: 102 layers, **27 in 1938–1964 (917,852 B)** and **21 in 1965–1986 (1,994,223 B)**, 7 tagged "(Frito-Lay)", one year missing (1984) | **FETCH 1** — layer-by-layer fetch plus title-page reading; and fix `drop_year_facet` so CP tasks lose `year_range` under `--facet-free` |
| **(e) auction / museum / manuscript** | **UNTRIED**, and no query block exists for the family corpus-wide | no path, no sidecars; families present in `tools/queries.json`: chronicling_america, internet_archive, corporate_print, hathitrust, google_books | new family plus query block; and the Delaware registry route, which is not a family but is the only **independent lineage** available (FETCH 5) |

**Family count for the tier rule (§15.2).** Families returning **in-window Tier-1 text held on disk: one** —
(c)/(d) through `CAT48` (1947–48, the subsidiary-line person), while (a) returns **zero** in-window documents
and only retrospective recital. ≤1 family, so **T3 stands for 1A, 1B and 1C**, 1B/1C marked PROVISIONAL
pending FETCH 1 (§U.15). Family (d) is **not** reported empty: its zero is a tool artefact with a named fix.

STATUS: WRITTEN

---

## B

STATUS: WRITTEN 2026-10-06

### B.1 The founder: absent from the record, not merely unstated

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Any founder of the beverage line | **Not in the corpus.** `pharmacist` 0, `Bradham` 0, `Caleb` 0, `1893` (as a date) 0, `1898` 0, `1902` 0, `since 18` 0, `Loth's` 0, `Texana` 0, `Bibbole` 0 | whole-corpus census over 38 docs, §P.2 [P1-08] | **UNKNOWN** — no carrier in any family held |
| Any founder of the snack line | **Not in the corpus.** `Herman Lay` 0; the 4 `Herman` hits are decoys (§A.1) | `K98` l.5366, `S4Q` l.10275, `S4QA` l.10462, `CAT48` l.1485 [P1-06] | **UNKNOWN** |
| The word "founder" in the registrant's filings | **0 occurrences in all 27 SEC documents.** So does "founded": **0**. The 6 print-family `founder` hits are a director's *co-founded* venture (`PX24` l.1636), Yum's directors' side-businesses (`YUM08`) and an education-report author | census [P1-09] | High (FACT-about-the-corpus). **The registrant's own EDGAR voice has no founder narrative at all** — only a charter recital |
| Whose signature carries the 1965 merger sentence | "Indra K. Nooyi / PepsiCo Chairman of the Board of Directors and Chief Executive Officer" | `AR17` l.95–97, l.122, T1, CONTEMPORANEOUS (for 2017), RESTATED (for 1965) [P1-03] | High that she wrote it in 2017; it is **not** a founder's claim |
| Who signed for the person in the only in-window print | "Walter S. Mack, Jr., President" — of Pepsi-Cola Company | `CAT48` l.141ff., T1 (Pepsi-Cola Company's own print), CONTEMPORANEOUS [P1-10] | **Medium-High** — the only named officer of an origin-line legal person inside 1919–1964 held anywhere |

### B.2 The company's state, as the corpus can print it

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Legal origin recited | Delaware 1919 → North Carolina 1986, one sentence, 8 filings | `REG95` l.462–463; `K94`–`K99`; `K2000` l.79, T1, RESTATED [P1-01] | Medium; **single lineage** |
| Counsel's independent-ish statement of situs | "PepsiCo, Inc., a North Carolina corporation (the 'Company')" — opinion dated **February 28, 2001**, by the company's own General Counsel and Secretary, "limited to the laws of the State of North Carolina" | `OP5` l.21, l.53–54, T1, FACT (of the opinion) [P1-11] | High that the opinion says this; **it prints no origin date and does not opine on the Delaware leg** |
| Persons inside the group at 12/30/2000 | `EX21` prints 91 rows whose jurisdiction this pass could count: **Delaware 81, California 4, New York 3, Texas 2, Nevada 1** | `EX21`, tag-stripped parse [P1-12] | High (FACT-about-the-carrier) |
| The two origin-name lines | `Pepsi-Cola Company` \| `Delaware`; `Frito-Lay, Inc.` \| `Delaware`; and `S.W. Frito-Lay, Ltd` \| `Texas` — all three **undated** | `EX21` parsed l.677/678, 313/314, 826/827 [P1-04], [P1-13] | High (listed) / **UNKNOWN** (chartered) |
| The beverage person's trading name in the 1990s | `Pepsi-Cola North America ("PCNA")` and `Pepsi-Cola International ("PCI")` — divisions, not the subsidiary | `REG95` l.470–471, T1, FACT [P1-14] | High (as printed) |
| Employees | "At December 31, 1994, PepsiCo employed … approximately **471,000 persons** (including 228,000 part-time), of whom approximately **340,000** … within the United States" — a **system** figure inclusive of bottlers | `K94` l.338–341, T1, FACT (floor datum, not Stage 1) [P1-15] | High (as filed); basis named: persons, part-time inclusive, US vs total |
| Registered name of the issuer on the 1995 shelf | "PEPSICO, INC." | `REG01` l.23/l.39; `REG95` cover block, T1 | High |

**Reading of §B.** The corpus contains a company, a recital, and a subsidiary list — and no person who made
anything. The founder question is therefore not answered "no" here: it is answered `UNKNOWN`, with the route
named (families (b)/(e) untried; the 27 unfetched pre-1965 print layers; the Delaware charter file). The one
person the record does let us name inside the window is a **President of the beverage subsidiary in 1947–48**,
in that subsidiary's own print — which is the closest this corpus comes to an in-window founder-state section,
and it is an officer, not a founder (rule 4).

STATUS: WRITTEN

---

## C

STATUS: WRITTEN 2026-10-06

### C.1 The problem as the record states it — and the honest statement that the record states none

| Variable | Value | Source | Confidence |
|---|---|---|---|
| The origin-period business problem | **UNKNOWN.** No held document describes a problem, a plan, a pricing decision or an entry decision for 1893–1964. `founder/founded` 0 in filings; no prospectus, charter, merger certificate, or trade-press naming inside 1B except `CAT48`, which is an art-exhibition catalogue and states an **art** problem | census; `CAT48` passim [P1-16] | **UNKNOWN** — deliverable, not a gap to smooth |
| The economic mechanism the registrant prints for itself, 1995 | Concentrate-and-bottle: "Under appointments from PepsiCo, bottlers manufacture, sell, and distribute, **within defined territories**, carbonated soft drinks and syrups bearing trademarks owned by PepsiCo" | `REG95` l.472–477, T1, CONTEMPORANEOUS (for 1995) [P1-17] | High as to 1995; **the structure's inception date is UNKNOWN** (§U.9) |
| Same mechanism, 1999 | "PCNA's bottlers are licensed to manufacture, market, sell and distribute beverages and syrups bearing the Pepsi-Cola Beverage trademarks in **approximately 440 licensed territories** in the United States and Canada. We have a minority interest in 8 of these bottlers, comprising approximately **240** licensed territories." | `K99` l.238–241, T1, CONTEMPORANEOUS [P1-18] | High (as filed) |
| What the mechanism is NOT evidenced to be | Not evidenced as a 1919 or 1965 design choice; not evidenced as a franchise system "invented" at any date; the corpus never uses the word "franchise" of its own beverage system before 1995 because it prints nothing before 1995 | `REG95`, `K99` [P1-19] | High (of the silence) |
| The snack side's problem | **UNKNOWN.** `Frito` occurs 455 times in the SEC corpus and 130 in the print corpus, **never with a founding date, a founder, or a start-up account**; `1961` (the folklore year of the Frito Company / H.W. Lay merge) occurs **0** times | census [P1-20] | **UNKNOWN** — 1961 unproven by this corpus |

### C.2 Genealogy of the origin claim — this replaces the legend

| Rung | What exists in this corpus | Date | Carrier | Confidence |
|---|---|---|---|---|
| 1 — artifact of the origin act | **Nothing held**: no charter, no merger certificate, no incorporation filing, no bottle, no ledger | — | 0 documents in 1919–1964 (`IDX`); EDGAR floor 1995-01-06 | High (none reachable by this toolchain) |
| 2 — in-window third-party text naming a person | `CAT48` names **Pepsi-Cola Company** as the sponsoring corporate person, with a President's signed foreword, venues 1947-01→1948-04; `PR74` names `Pepsi Cola Canada Ltd.` as a 1974 sponsor | 1947–48; 1974 | `CAT48` l.5, l.121, l.141; `PR74` l.25, l.34 | **High** that the name operated as a corporate person then. **Medium**: `CAT48` is self-published corporate print of the *subsidiary*, and is about an art prize |
| 3 — registrant's own retrospective statement | The 1919/1986 recital (13 occurrences, 2 media) and the 1965 merger sentence (1 occurrence, 2017 print) | 1995–2001 filings; 2017 print | `REG95`, `K94`–`K2000`, `AR17` | Medium (recital); **Low** (merger) |
| 4 — importer's folklore | 1893 / 1898 / 1902 / the pharmacist / the bottle cap — carried into this project's own **search parameter** (`harvest_mine.py:71`) | — | §boundary 1 | Not evidence. Recorded so the next agent sees the folklore entered the pipeline as a **window**, not as a source |

**Problem vs narrative.** The documented problem in this corpus is a *1995* problem printed by a *1995*
registrant: how to sell concentrate to independent bottlers under territorial appointments and how to keep a
trademark portfolio distinct from its bottlers' operations. Everything usually meant by "PepsiCo's original
problem" — a pharmacist's cola syrup as an answer to a drugstore beverage trade, a snack company's route-to-
store, a 1965 combination's rationale — is **absent**: no carrier, no agent, no date. `INFERENCE, held
narrowly:` the 1965 dividend sentence and the 2017 merger sentence are two tellings of one corporate-
continuity claim by the same institution, 52 years apart, in two genres (a legal Item 5 disclosure and a CEO's
letter); their agreement is **lineage, not corroboration** (§3). Conflicts registered at §U.6, §U.11.

STATUS: WRITTEN

---

## D

STATUS: WRITTEN 2026-10-06

### D.1 The first experiment, 1893–1918 or 1919–1965: UNKNOWN, with the route named

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Date | **UNKNOWN.** No held document dates any commercial act of either origin line before 1995 | `IDX` (0 rows ≤ 1994); census | High (that nothing is held); **UNKNOWN** (the event) |
| Product at the origin | **UNKNOWN.** `syrup` appears only in 1995–99 structure sentences; no first product, formula, price or package is dated in-window | `REG95` l.477; `K99` l.239 | **UNKNOWN** |
| "Bottle cap / crown cap" folklore | **Rejected as uncarried.** `bottle cap` = 4 occurrences, all in 2020–2023 environmental-regulation boilerplate ("requirements for **bottle caps** to be tethered to bottles"); `crown cap` = 0; the 2 `crown` hits are a 1906 Chinese-newspaper auction line and "forfeited to the Crown" | `AR20` l.2336, `PX20` l.2046, `PX22` l.2434, `PX23` l.2439; `NPTG` l.2986, l.5009 | **UNKNOWN**, and the apparent hits are keyword decoys (§U.9, rule 6) |
| First customer, first sale, first bottler | **UNKNOWN** — no in-window document exists to contain one | — | **UNKNOWN** |
| What the corpus does hold as an in-window act | A **sponsorship**, not a product test: Pepsi-Cola Company's "Fourth Annual Exhibition Paintings of the Year", toured National Academy of Design (Oct 1–Nov 2 **1947**), Rochester Memorial Art Gallery (Nov 21–Dec 21 1947), Corcoran Gallery of Art (Jan 15–Feb 22 **1948**), Toledo Museum of Art (Mar 14–Apr 18 1948) | `CAT48` l.1–30, T1 corporate print, CONTEMPORANEOUS [P1-21] | **High** that this act happened, in the window, under that name — the only such item in the corpus |
| Magnitudes of that act | "twenty cash awards totaling **$15,250**", fellowships "**$1500** each, one to each region", "purchased outright … **eleven paintings valued at $14,700** for reproduction in full color on its **1948 calendar**", "distribution throughout the country of approximately **650,000 calendars**" | `CAT48` l.125–137 [P1-22] | **High** (as printed by the sponsor); basis: programme spend and calendar circulation, **not** sales |

### D.2 Assessment (three duties discharged)

**Evidence:** the single in-window, dated, non-registrant-authored set of bytes this company holds about its
own origin line is an **art competition**, and it is enough to prove three things security filings cannot: that
`Pepsi-Cola Company` was an operating corporate person with a President and a published foreword in 1947–48;
that it spent real money on brand-goodwill channels rather than only on product; and that its distribution
apparatus reached a national calendar circulation of ~650,000. **Mechanism:** corporate sponsorship of a jury
art prize is a reputation channel — the catalogue is signed by the company's President and addresses "the
Company", so the print itself is the artefact of the marketing. **Alternative explanation (held as live):**
the catalogue may be a *Pepsi-Cola Company* publication that an art institution physically printed; its bytes
prove the company's name and money, not who manufactured the document, and the IA item it arrived in is
classified `corporate_print` by the harvest ledger while the probe classified the same item as an art catalogue
(§U.14). What §D cannot say, on any held byte, is anything at all about a **product** in the origin window;
that is the deliverable of this section, and the reason D is not padded with the 1893 story. **Confidence:**
High on the sponsorship act; **UNKNOWN** on every product question.

STATUS: WRITTEN

---

## E

STATUS: WRITTEN

**§7 adaptation note.** The standard "product reconstruction" frame presumes a datable first product. For this
stage no product can be dated, so §E reconstructs (i) the product *system* the registrant prints for itself
once the record starts, and (ii) the empty set for 1893–1964, which is the finding.

| Variable | Value | Source | Confidence |
|---|---|---|---|
| First product of the beverage line | **UNKNOWN** — no held document names a product with a date inside 1893–1964 | census; 0 documents in-window | **UNKNOWN**, route named (§S G-04) |
| First product of the snack line | **UNKNOWN** — `Frito` 455 occurrences in the SEC corpus, **130** in the print corpus, none with an origin date, founder, or first-product account | census [P1-20] | **UNKNOWN** |
| The product system as printed in 1995 | PCNA "manufactures and sells beverages, primarily soft drinks and soft drink concentrates"; it "sells its concentrates to licensed independent and company-owned bottlers and to joint ventures in which PepsiCo participates" | `REG95` l.472–475, T1, CONTEMPORANEOUS (1995) [P1-23] | High (as printed) |
| The marks the system moved, 1995 | "carbonated soft drinks and syrups bearing trademarks owned by PepsiCo, including **PEPSI-COLA, DIET PEPSI, MOUNTAIN DEW, SLICE, CRYSTAL, MUG, and, within Canada, 7UP and DIET 7UP**" | `REG95` l.477–480, T1, FACT [P1-24] | High. **No first-use or registration year is printed for any mark** — `trademark` occurs 94 times in the SEC corpus, none paired with an inception date |
| Portfolio as printed 2020 (property schedule) | "We own numerous valuable trademarks which are essential to our worldwide businesses, including **1893**, Agusha, Amp Energy, Aquafina, … Cheetos, … Doritos, … Frito-Lay, Fritos, … Gatorade…" | `PX20` l.1606–1609, T1 corporate print, FACT (of the list) [P1-25] | High — and this is the corpus's **only** `1893`: a **Mexican cola brand name in a marks list**, not a date (§U.8) |
| Package / dispensing at the origin | **UNKNOWN.** No held document describes a bottle, cap, crate, fountain, or vending apparatus before 1995. The `bottle cap` hits are 2020–23 plastics-regulation text (§D.1); `crown cap` 0 | census | **UNKNOWN** (§U.9) |
| Concentrate chemistry | **UNKNOWN** — the word `caramel` occurs **0** times in the whole corpus | census | **UNKNOWN** |

STATUS: WRITTEN

---

## F

STATUS: WRITTEN 2026-10-06

**§7 adaptation note.** "Customer" for a concentrate licensor splits into the licensees (who buy) and the
consumers (who drink); both are answered, and the origin-period answer is the empty set.

| Variable | Value | Source | Confidence |
|---|---|---|---|
| First customer | **UNKNOWN**; no in-window document exists that could contain one | `IDX` | **UNKNOWN** |
| Who bought from the registrant, as printed 1995 | "licensed independent and company-owned bottlers and … joint ventures in which PepsiCo participates" | `REG95` l.474–475 [P1-23] | High (1995) |
| Who was licensed, as printed 1999 | "sale to **franchised bottlers** in the United States and Canada"; "approximately **440 licensed territories**"; minority interest in **8** bottlers covering approximately **240** territories | `K99` l.237–241, T1, FACT [P1-18] | High (as filed) |
| Bottlers as separate legal persons | `EX21` lists among the registrant's subsidiaries `Pepsi-Cola Bottling International Inc.` \| `Nevada`, `Pepsi-Cola Canada Ltd.` \| `Canada`, `Pepsi-Cola Equipment Corp.` \| `New York` | `EX21` parsed l.669–686 [P1-26] | High (listed); all **undated** |
| Consumer-side demand data, origin period | **UNKNOWN** — no unit-volume, price or consumption series exists in the corpus for any year before 1995 | census | **UNKNOWN** |

STATUS: WRITTEN

---

## G

STATUS: WRITTEN 2026-10-06

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Host / distribution side | The franchise-bottler apparatus: appointments, "within defined territories", marks owned by the licensor | `REG95` l.472–480 [P1-17] | High for 1995; **inception date UNKNOWN** (§U.9) |
| Territory count, first printed | ~440 licensed territories (US + Canada), 1999 basis | `K99` l.239–240 [P1-18] | High (as filed) |
| Owned bottling inside the group | yes — `EX21` lists bottling and equipment subsidiaries in 5 counted jurisdictions (Delaware 81 / California 4 / New York 3 / Texas 2 / Nevada 1 of 91 countable rows) | `EX21` [P1-12], [P1-26] | High (of the listing) |
| Non-production distribution the record prints, in-window | Pepsi-Cola Company's 1947–48 exhibition sponsorship reached "approximately **650,000 calendars**" distributed nationally, and 4 named museum venues across 4 states | `CAT48` l.1–30, l.137 [P1-22] | Medium-High — the only in-window distribution datum in the corpus, and it is a **goodwill channel**, not a product route |
| What G cannot say | No route, warehouse, truck, vending, or shelf-space datum exists for 1919–1964 | — | **UNKNOWN** |

STATUS: WRITTEN

---

## H

STATUS: WRITTEN 2026-10-06

**§7 adaptation note.** "Market as knowable in-period" is answered here as an epistemic question, because the
corpus holds no in-window market text at all: stating a 1920 or 1955 market size would be invention.

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Market size at the open of 1B or 1C | **UNKNOWN** — no held document prints a soft-drink or snack market size for any year before 1995 | census | **UNKNOWN** |
| Knowable to a 1919 observer | **NOT KNOWABLE from this corpus.** The corpus's earliest market-bearing text is dated 1995-01-06 (`REG95`, the EDGAR floor for this CIK) | `IDX`, `RUN` | High (of the boundary) |
| What the corpus does print about the demand side | The registrant's 1994 dividend-payout policy and its 1995–99 bottler geography (§K, §F); the 1947–48 cultural-sponsorship programme; a 1974 Canadian university tournament sponsored by `Pepsi Cola Canada Ltd.` | `K94` l.562–565; `CAT48`; `PR74` l.25 | High (as printed); none of it is a market size |
| Periphery naming the brand in-window, third-party | `PR74` (Concordia University, Montreal, Dec 1974): "OTH ANNUAL CENTENNIAL BASKETBALL TOURNAMENT SET. **SPONSORED BY PEPSI COLA CANADA LTD.**" | `PR74` l.25, l.34, T3-of-T1, CONTEMPORANEOUS [P1-27] | High that a Pepsi-Cola-titled corporation sponsored Canadian university sport in 1974. **This is a different legal person from the US constituent** (rule 5), and it is 1C-window not 1B |
| Decoy class | `NPTG` (Hongkong Telegraph, 1906-06-30) holds 196,947 B of in-window-period newspaper and returns **0** hits for `pepsi`, `cola`, `Bradham`, `1898` | `NPTG` sidecar + census | **NULL** over held bytes (the honest class for this item; A4 graded it `NULL`) |

STATUS: WRITTEN

---

## I

STATUS: WRITTEN 2026-10-06

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Competitors named inside 1B/1C | **None.** No held document names a competitor for any year before 1995 | census, `IDX` | **UNKNOWN** |
| Competitor naming that does exist | `Coca-Cola` occurs **148 times in exactly 2** of the 27 SEC documents — `S4Q` and `S4QA` (the 2001 Quaker registration) — and never inside a Stage-1 window | census [P1-28] | High (FACT-about-the-corpus); (PB) for Stage 1 |
| The corpus's one *founding-date* sentence about a rival brand | "**A&W was founded in Lodi, California by Roy Allen in 1919** and the first A&W franchise unit opened in 1925" — inside `YUM08`, the **YUM! Brands 2008** annual report stored under this company's harvest item name | `YUM08` l.9009, T1-of-another-registrant, RESTATED (for 1919) [P1-29] | High that the sentence exists; **it is not evidence about PepsiCo**. It is the only non-recital `1919` in the corpus (§U.7) |
| Adjacent founding folklore in the same file | "KFC was founded in Corbin, Kentucky by Colonel Harland D. Sanders … perfected his secret blend … in 1939 and signed up his first franchisee in 1952" | `YUM08` l.8920–8922 [P1-30] | Same class: another registrant's origin story, arriving inside this company's harvest ledger |
| Third-party naming of the snack person, post-window | `ERIC` (federal education report ED 337 649) carries "**What Frito-Lay Has Done in Workplace Literacy**" by "Kelly Mossberg, Frito-Lay" and names "Frito-Lay South" | `ERIC` l.73, l.376–377, l.546, T1 (third-party report), CONTEMPORANEOUS (for its own year) [P1-31] | High that Frito-Lay operated a named US regional organisation; **no origin date**, and outside Stage 1 (1991/92) |

**Reading of §I.** Every competitor or sibling founding story the corpus appears to supply is somebody else's.
The temptation this section exists to resist is the *one-1919-is-as-good-as-another* error: a naive full-text
hit count for `1919` across the print family returns 6 rows, of which 5 are the registrant's own recital and 1
is A&W's.

STATUS: WRITTEN

---

## J

STATUS: WRITTEN 2026-10-06

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Origin-period technology | **UNKNOWN** — no formula, process, plant, or equipment reference dated inside 1893–1964 exists in the corpus | census | **UNKNOWN** |
| Technology as printed for 1995 | concentrate manufacture + independent bottling under appointment; the registrant's own 1995 description contains no process detail beyond "manufactures and sells … soft drinks and soft drink concentrates" | `REG95` l.472–477 [P1-23] | High (as printed) |
| In-window apparatus naming | `EX21` lists `Pepsi-Cola Equipment Corp.` \| `New York` as a subsidiary at 12/30/2000 — an equipment person, undated | `EX21` parsed l.685–686 [P1-26] | High (listed); **UNKNOWN** (when constituted) |
| OCR/keyword decoy class in this family | the corpus's single `1900` is Y2K boilerplate: "date-sensitive software may recognize a date using '00' as the year **1900** rather…" | `K97` l.636 [P1-32] | High (FACT-about-the-corpus); never citable as history (rule 6) |
| Measurement decoy this pass caught | a `\b(1[89]\d\d|20\d\d)\b` year regex returns **0** matches on IA layer filenames, because `_djvu.txt` glues a word character to the year so `\b` fails; the corrected pattern `(1[89]\d\d|20\d\d)` recovers the whole 1938–2024 run | `LAY`, §A.4 [P1-33] | High. **Any earlier "no dated layers" reading of this item was an artefact of the regex, not of the archive** |

STATUS: WRITTEN

---

## K

STATUS: WRITTEN

**§K is mandatory at T3 (method §15.2), and for this company it is the section where the emptiness is the
result.** There is no founder in the corpus whose personal finances could be reconstructed, no 1919
capitalisation, no 1965 consideration, and no in-window money of any kind. What the corpus can carry is
printed and labelled `(floor)` — the earliest money the archive reaches (1994–95), which is *after* Stage 1
closed and is quoted only to establish what the registrant's own accounting voice looks like.

### K.1 Origin-period money: the register of what is missing

| Variable | Value | Source | Confidence |
|---|---|---|---|
| The creator's capital, personal or otherwise | **UNKNOWN** — no person is named in the origin act (§B.1) | census | **UNKNOWN**; route = families (b)/(e) + Delaware registry (FETCH 5) |
| 1919 charter capitalisation, share structure, franchise fee | **UNKNOWN** — 0 occurrences of any capitalisation figure attached to 1919 in 38 documents | census | **UNKNOWN**; the Delaware Division of Corporations charter file is the only known route |
| 1965 merger consideration, exchange ratio, constituent balance sheets | **UNKNOWN** — the merger is asserted in one 2017 sentence with no figures at all | `AR17` l.122 [P1-03] | **UNKNOWN**; the 1965 registration statement / merger certificate is unreachable: 0 index rows before 1995-01-06 (`IDX`) |
| Snack constituent's capital before 1965 | **UNKNOWN** — `Frito` never appears with a figure that is dated in-window; `1961` 0 | census | **UNKNOWN** |
| Dividends before 1994 | **UNKNOWN** as amounts. The only pre-1994 money statement is the *policy* sentence "paid since 1965" | `K94` l.557–559 [P1-02] | **UNKNOWN** (amounts) |

### K.2 What the record does print about money (all of it `(floor)`, none of it Stage-1 performance)

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Dividends declared per share | **1994: 70 cents** (Q1 16, Q2 18, Q3 18, Q4 18); **1993: 61 cents** (13/16/16/16) | `K94` l.568–575, T1, FACT (floor datum) [P1-34] | High |
| Payout policy as stated | "Consistent with PepsiCo's current payout target of approximately **one-third** of the prior year's income from ongoing operations, the 1994 dividends declared represented **34%** of 1993 income from ongoing operations" | `K94` l.562–565, T1, FACT [P1-35] | High |
| Continuity claim as stated | "Quarterly cash dividends have been paid since **PepsiCo was formed in 1965**, and dividends per share have increased for **22 consecutive years**" | `K94` l.557–559 [P1-02]; restated `K95` l.557, `K96` l.554, `K97` l.455, `K98` l.542, `K99` l.487, `K2000` l.346 | Medium (one lineage, 7 printings) |
| The same claim in 2017–23 print | "Dividends — We have paid **consecutive quarterly cash dividends since 1965**" | `AR17` l.3348, `AR20` l.2693, `PX22` l.2838, `PX23` l.2848 [P1-36] | Medium — same corporate record, different genre |
| DERIVED: what "22 consecutive years" implies | 1994 − 22 + 1 = **1973** as the first year of the increase streak; the *payment* streak is claimed from **1965**. The two clauses in one sentence therefore date **two different things** | arithmetic on `K94` l.557–559, DERIVED [P1-37] | High (arithmetic); the streak's start year is the registrant's assertion, not a charter fact |
| Share price basis (1994) | NYSE quarterly high/low/close for a share of PepsiCo Capital Stock, e.g. Q4 1994 high 37 3/8, low 32 1/4, close 36 1/4 | `K94` l.577–583, T1, FACT (floor) [P1-38] | High; basis = **PepsiCo Capital Stock** (not common), NYSE, quarterly |
| Employees at the floor | ~471,000 persons (282,000 part-time) at 1994-12-31; ~340,000 in the US | `K94` l.338–341 [P1-15] | High; basis = persons, inclusive of part-time and of the bottler system |

**Reading of §K.** The single most useful sentence in this section is the DERIVED one: the registrant's own
1994 text puts "paid since 1965" and "increased for 22 consecutive years" in the same breath, and the two
date-spans they imply differ by eight years. That is internal evidence that the 1965 in that paragraph is
doing **dividend-continuity** work, not founding work — which is precisely why this dossier refuses to promote
the dividend sentence into a charter (§U.6, §U.11).

STATUS: WRITTEN

---

## L

STATUS: WRITTEN

**§7 adaptation note.** Validation signals for an origin stage would normally be first sales, repeat purchases
or a licence granted. The corpus holds none, so §L records the *absence* and then lists what the earliest
record does demonstrate, each with its "did NOT demonstrate" cell filled.

| Date | Signal | Magnitude | What it demonstrated | What it did NOT demonstrate | Source | Confidence |
|---|---|---|---|---|---|---|
| inside 1893–1964 | **none held** | — | nothing | — | 0 documents (`IDX`) | **UNKNOWN** (no signal exists in this corpus) |
| 1947–48 | Pepsi-Cola Company's own print: a national art prize with cash awards and a 650,000-calendar run-up | $15,250 awards; $1,500 regional fellowships; 11 paintings bought for $14,700 | that the beverage person was spending discretionary brand money at scale, and had a national distribution reach for its calendar | product demand, sales, or the corporate chronology | `CAT48` [P1-22] | Medium-High (self-reported programme) |
| 1994-12-31 (floor) | "dividends per share have increased for 22 consecutive years" | 70 cents declared in 1994 vs 61 in 1993 | that management asserted an unbroken increase streak to 1994, inside a legal disclosure | formation, and even the payment start it names is one lineage's word | `K94` [P1-02], [P1-34] | Medium (as an assertion) |
| 1995–99 (floor) | franchise geography | ~440 licensed territories; 8 minority-held bottlers ≈ 240 territories | the scale of the licensing apparatus as of 1995–99 | when the apparatus began (§U.9) | `REG95`, `K99` [P1-17], [P1-18] | High (as filed) |

STATUS: WRITTEN

---

## M

STATUS: WRITTEN

**§7 adaptation note.** No operating failure inside 1893–1986 can be cited from this corpus, because no
document inside it exists. The failures this section can honestly register are **retrieval and record-keeping
failures** — they are what stands between this dossier and a founding date, and they are fixable, so they are
recorded as defects with remedies rather than as bad luck.

### M.1 In-window operating failures

| Item | Value | Source | Confidence |
|---|---|---|---|
| Any failure dated inside 1B or 1C | **UNKNOWN — 0 documents.** No product failure, litigation, recall, plant, contract loss or labour event is recorded for any year before 1995 | `IDX`; census | **UNKNOWN**; the 27 + 21 in-window print layers (§A.4) and the paper-era EDGAR record are the only routes |

### M.2 What the corpus itself failed to do, measured

| Date | Failure | Magnitude | What it demonstrated | What it did NOT demonstrate | Source | Confidence |
|---|---|---|---|---|---|---|
| 2026-09-29/30 | pass-1 intake against the harvester's 1898→1965 window returned **rc0 / inwindow0 / pass1_docs=0** | 0 documents | that a window built from contested dates wastes an intake pass and then *silently* re-imports the contested dates as if settled | that no in-window record exists | `HMX` l.3; `harvest_mine.py:71`; probe A.1 | High |
| 2026-09-29 | 8-K `0000077476-00-000047` (2000-12-04) documents `0001/0002/0003.txt` all **404 NoSuchKey** on all three path forms | 3 of 4 UNANSWERED rows | an archive-side gap on one accession | anything about the company | `UNA` | High (of the 404s) |
| 2026-09-29 | **88 in-window filings never listed** because `--max-docs 30` was reached | capped enumeration | that the stored 27 is a *sample*, not a census | completeness of the recital set | `UNA` row 4 | High (FACT-about-the-corpus) |
| 2026-10-06 | the corporate_print family's **YEAR-facet zero is an artefact, not a null**: `periodical_harvest.py:1401–1427` `drop_year_facet` rewrites only `params["q"]`, while CP tasks carry `year_range` and no `q`, so `if not q: continue` skips the whole family; the stored CP sidecar URL still ends `…AND%20YEAR%3A%5B1900%20TO%201980%5D` | family (d) returned 0 bytes on a faceted query | a tool defect (RD-130 class) | that corporate print is empty for this brand line | probe A.6(d); this pass re-read the sidecars and confirms `sources/corporate_print/` is still **0 B** while CP-classified items sit in `sources/periodicals/` | High |
| 2026-10-06 | two harvest items are **mislabelled as to person**: `01-pepsi-co` (IA metadata date 1938) yields the **2017** layer as its held bytes; `pepsicofritolayannualreports` yields **`yum2008_djvu.txt`**, the **YUM! Brands 2008** annual report | 2 of 11 print layers belong to other persons/years | that an item title and an uploader's `creator`/`date` field are not the document | — | sidecars (`url`, `route`) [P1-39] | High |
| 2026-10-06 | `research/A4_harvest_mine.md` and `sources/harvest_mine/_index.json` both ledger **12 mined items**, while **11 text layers sit on disk including `ERIC_ED337649` (130,917 B), which appears in neither ledger** — `grep -c ERIC research/A4_harvest_mine.md` → **0** | 1 unledgered arrival | §14 r11 risk in the wild: bytes arrive after the dossier that describes them | that ERIC is irrelevant — it names **Frito-Lay** and is cited here (§I) | `HMX` vs directory listing [P1-40] | High |
| 2026-10-07 | the probe's named highest-value route, `ia_text.py list-files 01-pepsi-co`, **fails as written** — argparse: `error: unrecognized arguments: 01-pepsi-co` (`mode` is positional; the identifier must be passed as `--id`). This pass ran the corrected form and it answered | route was live but its CLI form was wrong | that a "cheapest route" named in a dossier can be unrunnable as stated and still be worth re-deriving | that the route was empty — it is the richest one in the corpus | `LAY` [P1-41] | High |

**Reading of §M.** The dominant failure in this dossier is not that the origin is unknowable; it is that the
pipeline adopted contested dates as parameters, capped its own enumeration, mislabelled two items, skipped a
whole family on a facet bug, missed one downloaded file in its own ledger, and stated its best route in a CLI
form that does not parse. Every one of those is a tool-side defect with a named remedy, and §A.4 shows what
the corrected route yields on the first try.

STATUS: WRITTEN

---

## N

STATUS: WRITTEN

**§N is mandatory at T3.** There is no founder in this corpus, so a founder-decision section is answered by
(n) the decisions the record prints for the legal persons it does name, and (n′) an explicit statement that no
decision of the origin period is documented. Each decision row below is carrier-anchored; the ones the corpus
cannot support are `UNKNOWN` rows with a route, not omissions.

### N.1 Decisions the record prints

| Date | Decision | State before | Information available | Unknowns | Alternatives | Constraints | Rationale | Expected result | Actual result | Evidence | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1965 (year only) | the combination that formed PepsiCo, Inc. | two separate persons, `Pepsi-Cola Company` (Delaware) and the snack line's person | one 2017 sentence: "Two years later, in 1965, Frito-Lay and Pepsi-Cola merged to form PepsiCo" | who decided; day and month; consideration; whether "Frito-Lay" then meant Frito-Lay, Inc.; which entity survived | a re-naming, a holding-company formation, or an acquisition — none excluded by any held byte | Delaware/NC corporate law of the period, unexamined by this corpus | **UNKNOWN** | **UNKNOWN** | `RESTATED (2017)` — registrant's own word, 52 years late | `AR17` l.122 [P1-03] | **Low** |
| 1986 | reincorporation in North Carolina | "incorporated in Delaware in 1919" | the two legs printed in one sentence in 8 filings | why NC; the mechanics; the vote | — | — | **UNKNOWN** | — | — | RESTATED (registrant's own record) | `K94` l.125–126 … `K2000` l.79 [P1-01] | **Medium** |
| 1994 (policy) | dividend payout target ≈ one-third of prior-year income from ongoing operations | 1993 declared 61 cents | the stated target and the achieved 34% | board deliberations | a different payout | earnings | **stated in the filing** | 1994 declared 70 cents | — | CONTEMPORANEOUS disclosure | `K94` l.562–575 [P1-35] | **High (as printed)** |
| 2001-01-09 | use a **merger of BeverageCo, Inc. with and into Quaker**, surviving as a wholly-owned PepsiCo subsidiary, with a certificate of merger filed in New Jersey | Quaker as target | the structure and the filing office | why this form | a stock purchase, a direct merger into PepsiCo | antitrust conditions named in the instrument | disclosed purpose | effective on DE/NJ filing | — | CONTEMPORANEOUS instrument (post-stage) | `S4Q` l.2044–2048, l.5704–5712 [P1-42] | **High** |

### N.2 Why N.2 belongs in a mandatory §N

The 2001 row is carried because it is the corpus's only **worked example** of how this registrant documents a
combination: named constituent persons, a surviving entity, and a filing office (`New Jersey`). It is the
documentary *class* of instrument that a 1965 merger would have required, and its absence from the corpus is
exactly the shape of the gap — an EDGAR floor at 1995-01-06, 0 index rows inside Stage 1. It is **not**
evidence about 1965; the inference it supports is about the record, not the event. **No founder decision of
the origin period is documented anywhere in these 38 documents: `founder` 0 and `founded` 0 in all 27 SEC
documents.**

STATUS: WRITTEN

---

## O

STATUS: WRITTEN

**§7 adaptation note.** "Counterfactual opportunities" normally asks what the founder chose not to do. With no
founder and no decision text in-window, the honest counterfactuals here are of **two kinds**, and the second
kind is the one this dossier can actually discharge.

| # | Counterfactual | Kind | Can the corpus support it? |
|---|---|---|---|
| 1 | that the 1919 Delaware corporation might have been chartered for a different business, or that the 1965 combination might have taken another form | business-history | **No.** No in-window document exists to make an alternative plausible; asserting one would be invention, and the hindsight firewall (§2) forbids reasoning backwards from the registrant's later portfolio (sodas + salty snacks + hydration + 2001 Quaker) to claim the 1965 design was "chosen over" anything |
| 2 | that the **record** might have carried the origin, and the pipeline chose routes that could not | record-formation | **Yes, and this is §O's deliverable.** Four forks, each measured: (i) the harvester windowed on 1898–1965 instead of on the carrier-printed 1919–1986, and got 0 documents; (ii) the corporate_print family was skipped whole by a facet bug while its items were being stored under another family's directory; (iii) the intake stopped at `--max-docs 30`, leaving 88 in-window filings unlisted and the recital set a sample; (iv) 48 in-window corporate-print layers named by `list-files` (§A.4) were never fetched, because only one layer per item was pulled and it happened to be the 2017 one |
| 3 | whether a *deliberate* origin-narrative choice exists — i.e. did the registrant select 1919 over an earlier brand date | narrative | **Supported as an observation, not as a motive.** On its own word the registrant begins in 1919 and the merged firm in 1965; `since 18` occurs 0 times and no 1890s date is attached to the registrant anywhere. That the recital *silently excludes* the brand's pre-corporate period is a fact about the corporate record (§U.2). Attributing a motive is beyond the corpus |
| 4 | whether the 1965 "merger" and the 1965 "formed" are the same institutional claim | source-genre | Yes, as an inference: the dividend sentence and the 2017 letter are the same institution's continuity assertion in two genres 52 years apart; their agreement is lineage, not corroboration (§3) |

**Coda.** Evidence: the four forks above are all measured. Mechanism: a corpus is shaped by the parameters its
tools were given, and a parameter set from folklore reproduces the folklore as a search window and then reports
its own silence as history. Alternative explanation: the origin documents may be genuinely lost rather than
merely unfetched — this cannot be excluded, because nothing in this corpus proves or disproves the survival of
the 1965 instrument, and the paper-era EDGAR/legacy-microfilm leg is `UNTRIED` and unreachable by these tools
(`## Untried` item 9). Confidence: High (forks i–iv); **UNKNOWN** (survival).

STATUS: WRITTEN

---

## P

STATUS: WRITTEN 2026-10-06

### P.1 Filed figures the corpus carries (all `(floor)` — earliest reach of the archive, **not** Stage-1 performance)

| ID | Date | Metric | Value | Unit | Source | Source date | Confidence |
|---|---|---|---|---|---|---|---|
| P140 | 1994 | dividends_declared_per_share | 70 | US cents | `K94` l.568–575 | 1995-03-28 | High |
| P141 | 1993 | dividends_declared_per_share | 61 | US cents | `K94` l.568–575 | 1995-03-28 | High |
| P142 | 1994 | payout_ratio_vs_prior_year_ongoing_income | 34 | percent | `K94` l.562–565 | 1995-03-28 | High |
| P143 | 1994 | consecutive_annual_dividend_increases_claimed | 22 | years | `K94` l.557–559 | 1995-03-28 | Medium (registrant's own count) |
| P144 | 1994-12-31 | persons_employed_system_wide | 471000 | persons (282,000 part-time) | `K94` l.338–341 | 1995-03-28 | High |
| P145 | 1994-12-31 | persons_employed_in_US | 340000 | persons (228,000 part-time) | `K94` l.338–341 | 1995-03-28 | High |
| P146 | 1995–1999 | licensed_bottling_territories_US_and_Canada | 440 | territories (approx.) | `K99` l.238–241 | 2000-03-21 | High (as filed) |
| P147 | 1995–1999 | territories_via_8_minority_held_bottlers | 240 | territories (approx.) | `K99` l.240–241 | 2000-03-21 | High (as filed) |
| P148 | 1947–1948 | exhibition_cash_awards_total | 15250 | USD | `CAT48` l.131 | 1947/48 programme | Medium-High (sponsor's own print) |
| P149 | 1947–1948 | regional_fellowship_each | 1500 | USD | `CAT48` l.131–132 | 1947/48 | Medium-High |
| P150 | 1947–1948 | paintings_purchased_value | 14700 | USD (11 works) | `CAT48` l.134–135 | 1947/48 | Medium-High |
| P151 | 1948 | calendar_distribution | 650000 | copies (approx.) | `CAT48` l.137 | 1947/48 | Medium-High |

### P.2 Corpus measurements that *are* Stage-1 findings (measured this pass; every row reproducible from `sources/`)

| ID | Date | Metric | Value | Unit | Source | Source date | Confidence |
|---|---|---|---|---|---|---|---|
| P152 | 1893–1964 | documents_held_dated_inside_the_slot | 0 | documents | `IDX` | 2026-10-07 | High |
| P153 | 1965–1986 | index_rows_in_stage_1C | 0 | accessions | `IDX` | 2026-10-07 | High |
| P154 | 1995-01-06 | edgar_floor_for_this_CIK | 1995-01-06 | filingDate | `IDX` (min of 3,058 rows) | 2026-10-07 | High |
| P155 | whole | index_rows_before_the_floor | 0 | rows | `IDX` | 2026-10-07 | High |
| P156 | whole | documents_held (27 SEC + 11 print layers) | 38 | documents | directory enumeration | 2026-10-07 | High |
| P157 | whole | byte_identical_duplicate_documents | 0 | documents | md5 over all 38 | 2026-10-07 | High |
| P158 | whole | occurrences_of `1898` / `1902` / `1904` | 0 / 0 / 0 | occurrences | grep over 38 docs | 2026-10-07 | High |
| P159 | whole | occurrences_of `pharmacist`/`Bradham`/`Caleb`/`Herman Lay`/`since 18`/`Loth's`/`crown cap` | 0 each | occurrences | grep over 38 docs | 2026-10-07 | High |
| P160 | whole | occurrences_of `1919` | 14 (13 = registrant's own recital in 2 media; 1 = A&W in `YUM08`) | occurrences | grep | 2026-10-07 | High |
| P161 | whole | occurrences_of `1965` | 22 in 14 files; **exactly 1 states a merger** | occurrences | grep | 2026-10-07 | High |
| P162 | whole | occurrences_of `1893` | 1 — a **trademark name** in a marks list (`PX20` l.1606) | occurrences | grep | 2026-10-07 | High |
| P163 | whole | occurrences_of `founder` / `founded` in the 27 SEC documents | 0 / 0 | occurrences | grep | 2026-10-07 | High |
| P164 | whole | occurrences_of `bottle cap` | 4, all 2020–23 tethered-cap regulation text | occurrences | grep | 2026-10-07 | High |
| P165 | 12/30/2000 | `EX21` countable jurisdiction rows | 91 (DE 81, CA 4, NY 3, TX 2, NV 1) | rows | `EX21` parse | 2026-10-07 | High |
| P166 | whole | occurrences_of `Pepsi-Cola Company` | 40 in 10 files (18 in SEC, 22 in `CAT48`), **0 with an incorporation date** | occurrences | grep | 2026-10-07 | High |
| P167 | whole | occurrences_of `Frito` | 455 in the SEC corpus + 130 in the print corpus, 0 with a founding date | occurrences | grep | 2026-10-07 | High |
| P168 | 2017 | merger sentences in the whole corpus | 1 (`AR17` l.122) | sentences | grep `merged` | 2026-10-07 | High |
| P169 | 1938–1964 | **unfetched** in-window print layers in item `01-pepsi-co` | 27 layers / 917,852 B | layers / bytes | `LAY` | 2026-10-07 | High (existence); bytes unfetched |
| P170 | 1965–1986 | **unfetched** in-window print layers in the same item | 21 layers / 1,994,223 B | layers / bytes | `LAY` | 2026-10-07 | High (existence) |
| P171 | 1958–1964 | layers tagged "(Frito-Lay)" under a "PepsiCo, Inc." filename | 7 | layers | `LAY` | 2026-10-07 | High |
| P172 | 1938–2024 | year gap in the PepsiCo-named layer run | 1984 absent (85 of 86 run-years present) | year | `LAY` | 2026-10-07 | High |

STATUS: WRITTEN

---

## Q

STATUS: WRITTEN 2026-10-06

### Q.1 Micro-timeline of everything this corpus dates

| Date | Event | Actors | Location | source_id (provisional) | Class | Conf |
|---|---|---|---|---|---|---|
| **1893 / 1898 / 1902** | the rival origin dates of the folklore | no person named in the corpus | `UNKNOWN` | P1T01 | **UNKNOWN — no carrier** (0 occurrences; `1893` exists only as a brand name) | — |
| 1919 | registrant "incorporated in Delaware" | PepsiCo, Inc. (its own recital) | Delaware | P1T02 | FOUNDER-CLASS claim → **RESTATED self-narrative**; the registrant's own corporate record | Medium |
| 1947-10-01 → 1947-11-02 | Pepsi-Cola Company's Fourth Annual Exhibition opens at the National Academy of Design | Pepsi-Cola Company; President Walter S. Mack, Jr. | New York City | P1T03 | **CONTEMPORANEOUS** (in-window, self-published print) | Medium-High |
| 1948-01-15 → 1948-02-22 | the same exhibition at the Corcoran Gallery of Art | Pepsi-Cola Company | Washington, D.C. | P1T04 | CONTEMPORANEOUS | Medium-High |
| **1965** | (a) "PepsiCo was formed" per the dividend sentence; (b) "Frito-Lay and Pepsi-Cola merged to form PepsiCo" per 2017 print | the merged registrant; the two constituent persons | `UNKNOWN` (day/month UNKNOWN) | P1T05 | RESTATED, single lineage; **(b) is the corpus's only merger statement** | Low |
| 1974-12-06/07 | 9th Annual Centennial Basketball Tournament "SPONSORED BY PEPSI COLA CANADA LTD." | Concordia University / Loyola; Pepsi Cola Canada Ltd. | Montreal, Quebec | P1T06 | **CONTEMPORANEOUS third-party** — different legal person from the US constituent | High (of the release) |
| 1986 | "reincorporated in North Carolina" | the registrant | North Carolina | P1T07 | registrant's own record (same sentence, same lineage as P1T02) | Medium |
| 1995-01-06 | **earliest document of any kind held for this CIK** (Form S-3) | registrant | — | P1T08 | FACT-about-the-corpus | High |
| 1995-03-28 | FY1994 10-K prints both the 1919/1986 recital and the 1965 dividend sentence | registrant | — | P1T09 | FACT (of the printing) | High |
| 12/30/2000 | `EX21` lists `Pepsi-Cola Company \| Delaware` and `Frito-Lay, Inc. \| Delaware` as **subsidiaries** | registrant | — | P1T10 | FACT (of the listing); both **undated** | High |
| 2001-02-28 | counsel's opinion: "PepsiCo, Inc., a North Carolina corporation", limited to NC law | PepsiCo GC & Secretary | Purchase, NY (address block) | P1T11 | CONTEMPORANEOUS instrument; prints no origin date | High |
| 2017 | CEO's shareholder letter prints the merger sentence | Indra K. Nooyi | — | P1T12 | RESTATED (52 years after the event) | High (of the printing) |
| 2020-05-06 | marks list includes the brand named **"1893"** | registrant | — | P1T13 | FACT (of the list); the corpus's only `1893` | High |
| **silence rows, stated as rows** | 0 documents for 1919-01-01→1994-12-31; 0 filings for 1965-01-01→1986-12-31; 0 occurrences of the whole origin vocabulary (§P.2) | — | — | P1T14 | FACT-about-the-corpus, **not** a corporate null | High |

STATUS: WRITTEN

---

## R

STATUS: WRITTEN 2026-10-06

### R.1 End-of-stage snapshot at 1986-12-31 (the day after Stage 1 closes, as far as this corpus can speak)

| Field | State at 1986-12-31 | Basis | Class |
|---|---|---|---|
| The registrant | "PepsiCo, Inc., … reincorporated in North Carolina in 1986" — i.e. the same legal person, two charters, per its own later word | `K94` l.125–126 (printed 1995) | RESTATED, one lineage, Medium |
| Documents dated inside 1965–1986 | **0** | `IDX` (0 rows) | FACT-about-the-corpus, High |
| Legal persons inside the group | `UNKNOWN` — the only subsidiary census held is dated 12/30/2000, 14 years after the stage closed | `EX21` | FACT (of the census) |
| Product portfolio at the close | **UNKNOWN** | — | — |
| Money at the close | **UNKNOWN** (no in-window figure of any kind) | — | — |
| People at the close | **UNKNOWN**; the earliest employment figure held is 1994-12-31 | `K94` l.338 | FACT (of the floor) |
| Distribution | **UNKNOWN** for 1986; ~440 licensed territories is a 1999 statement | `K99` | FACT (as filed, wrong year for R) |
| Name / brand line | `Pepsi-Cola Company` and `Frito-Lay, Inc.` are the two origin-name persons; **the corpus dates neither of them** and lists both as subsidiaries in 2000 | `EX21` | High (listing) / **UNKNOWN** (charter) |

**What R refuses.** R does not fill 1986 from 1994. Every `(floor)` figure in §K/§P belongs to a year *after*
the stage, and the table above leaves those cells `UNKNOWN` instead of back-dating the earliest available
number — which is the exact defect (§2, §6) this project's hindsight audits keep finding.

STATUS: WRITTEN

---

## S

STATUS: WRITTEN 2026-10-06

| Gap | Why missing | Importance | Best available evidence | Confidence | Follow-up task |
|---|---|---|---|---|---|
| S-01 who created the drink, when, where | 0 occurrences of every agent-name and date term in 38 documents | **High** | none in-corpus | **UNKNOWN** | FETCH 2 (CA/HT re-run past the cap) + FETCH 3 (IA 747-hit set, `date<=1965`) |
| S-02 1893 vs 1898 vs 1902 — which, if any | three rival folklore dates, no carrier for any | **High** | §U.1 (unresolved) | **UNKNOWN** | FETCH 2/3; then re-open U.1 with a carrier |
| S-03 when `Pepsi-Cola Company` was incorporated, and its early name changes | ex-21 lists it undated; no charter held | **High** | `EX21` (Delaware); `CAT48` (operating 1947–48) | **UNKNOWN** (date) | FETCH 5 (Delaware Division of Corporations) — the only independent-lineage route |
| S-04 when `Frito-Lay, Inc.` (and the prior Frito Co. / Lay's companies) were incorporated | ex-21 lists it undated; `1961` 0 occurrences | **High** | `EX21`; `ERIC` (1991/92 "Frito-Lay South") | **UNKNOWN** | FETCH 5 + FETCH 2 with bottler/manufacturer name sets |
| S-05 what the 1965 transaction legally was (merger / holding co / rename), its date and consideration | the merger is stated once, in a 2017 CEO letter, with no mechanics | **High** | `AR17` l.122 [P1-03] | Low (existence) / **UNKNOWN** (mechanics) | FETCH 4 (1965 registration statement / merger certificate via SEC legacy paper & microfilm) — **unreachable by these tools** |
| S-06 any in-window financial or operating datum (1919–1964) | EDGAR floor 1995-01-06 (`IDX`, 0 rows before) | **High** | none | **UNKNOWN** | FETCH 1 (the 27 + 21 print layers, §A.4) |
| S-07 inception date of the franchise-bottler system | 1995–99 filings describe the system, never its start | Medium | `REG95` l.472–477; `K99` l.238–241 | **UNKNOWN** | FETCH 2 (trade press: *Beverage World*, *Progressive Grocer*, *Food Engineering*) |
| S-08 first use / registration date of the PEPSI-COLA mark | `trademark` 94 occurrences, 0 with an inception year | Medium | `REG95` l.477–480 marks list | **UNKNOWN** | trademark-register retrieval (no script reaches it; human task) |
| S-09 founder personal finances / origin capital | no founder exists in the corpus to have finances | Medium | — | **UNKNOWN** | families (b)/(e), UNTRIED |
| S-10 the 27 pre-1965 corporate-print layers | they exist (`LAY`) but **no bytes held**; fetching them is outside this pass's WRITE scope | **High** | layer names + sizes | High (existence) | **FETCH 1 — the single highest-value call remaining for this company** |
| S-11 whether `01-pepsi-co` holds any 1938-layer naming Pepsi-Cola Company (as opposed to a label) | the held layer is 2017; the item date is uploader metadata | **High** | sidecar `url` vs metadata | **UNKNOWN** | FETCH 1, and read each title page before crediting a person |
| S-12 88 in-window filings never listed (`--max-docs 30`) | capped enumeration; a sample is not a census (§14.14) | Medium | `UNA` row 4 | High (of the cap) | re-run intake with a raised cap for forms in-window (10-K, S-1, S-4, DEF 14A) |
| S-13 the 3 documents of 8-K 0000077476-00-000047 | 404 NoSuchKey on all path forms | Low | `UNA` | **UNANSWERED** (network-side, named) | re-fetch via the dashed-dir form / the full submission ZIP |
| S-14 auction / museum / manuscript family, and web archives | **no path, no sidecars, and no query block exists corpus-wide** (probe A.6(e)) | Medium–High | — | **UNTRIED**, never a null | new family + query block; CDX pass for `pepsiacola.com`/`fritolay.com` |
| S-15 whether `ERIC_ED337649` is dated 1991 or 1992 | the item's own year was not read past its title page; it is also missing from both harvest ledgers | Low | `ERIC` l.1–10 header | **UNKNOWN** | next intake should stamp its date and ledger it (§14 r11) |

STATUS: WRITTEN

---

## T

STATUS: WRITTEN 2026-10-06

### T.1 Provenance table

`URL` gives the **local held path**; each document's remote URL is printed in its own `.meta.json` sidecar
written by the intake and was read by this pass for the print family (and for `OP5` in the SEC family) —
remote URLs are not re-verified here, and every print sidecar carries `"transport": "UNVERIFIED TLS — re-check
before citing at High confidence"`, which is why no print-family row below is graded High on the strength of a
transport this project did not validate.

| Source | Type | Primary/Secondary | Event date | Publication date | URL | Tier | Confidence |
|---|---|---|---|---|---|---|---|
| `REG95` Form S-3 | SEC filing | primary (registrant) | 1995-01-06 | 1995-01-06 | `sources/sec/0000077476-95-000002_0000077476-95-000002.txt` | 1 | High (of the printing); Medium (recital) |
| `K94` 10-K FY1994 | SEC filing | primary | 1994 FY | 1995-03-28 | `sources/sec/0000077476-95-000017_0000077476-95-000017.txt` | 1 | High / Medium (recital) |
| `K95`–`K99`, `K2000` | SEC filings | primary | FY1995–FY2000 | 1996-03-26…2001-03-15 | `sources/sec/0000077476-9{6,7,8,9}-…`, `…-00-000006…`, `…-01-500016_k2000.htm` | 1 | High (printing) |
| `EX21` subsidiary exhibit | SEC exhibit, same accession as `K2000` | primary | as of 12/30/2000 | 2001-03-15 | `sources/sec/0000077476-01-500016_ex21.htm` | 1 | High (of the listing) |
| `S4Q` / `S4QA` Form S-4 + amendment | SEC filings (Quaker acquisition) | primary | 2001-01-09 / 2001 | same | `sources/sec/0000912057-01-000830_a2034530zs-4.txt`, `…-01-007577_a2039895zs-4a.txt` | 1 | High; second registration, same registrant |
| `OP5` legal opinion | SEC exhibit | primary (counsel) | 2001-02-28 | 2001 | `sources/sec/0000950103-01-500049_ex5-1.txt` | 1 | High (of the opinion) |
| `REG01`, `K94`'s sibling `0000077476-95-000005/000016`, `…-96-000003`, `…-99-000018`, `…-00-000010` | SEC filings/exhibits | primary | 1995–2000 | same | `sources/sec/…` | 1 | High (of existence); content not re-read where unused |
| `AR17` PepsiCo Annual Report 2017 text layer | corporate print (IA) | primary (registrant) | 2017 | 2017 (item metadata says 1938) | `sources/periodicals/01-pepsi-co_djvu.txt` (item `01-pepsi-co`) | 1 | Medium-High (TLS unverified; label conflict §U.4) |
| `CAT48` Pepsi-Cola Company exhibition catalogue | corporate print (IA, Corcoran box) | **primary of the *subsidiary* person** | 1947–48 | item date 1948 | `sources/periodicals/cor5_0_s06_ss01_boxrg5_0_2008_006_f61_djvu.txt` | 1 | Medium-High — the only in-window self-naming print |
| `PR74` Concordia University release | third-party print | secondary of the sponsor | 1974-12 | 1974-12 | `sources/periodicals/1974-12-press-release_djvu.txt` | 3 | Medium (a naming, not a chronology) |
| `YUM08` YUM! Brands 2008 AR | another registrant's print | primary (of YUM) | 2008 | stored under a PepsiCo item name | `sources/periodicals/pepsicofritolayannualreports_djvu.txt` | 1 (for YUM) | High that it is YUM's; **0 value for PepsiCo's origin** (§U.7) |
| `AR20`, `PX20`, `PX22`, `PX23`, `PX24` | corporate print (IA) | primary (registrant) | 2020–2024 | same | `sources/periodicals/pepsi-co-inc.-pep-*.txt` | 1 | Medium-High; (PB) for Stage 1 |
| `ERIC` ED 337 649 | federal education report | third-party | 1991/92 (**year not established**, S-15) | — | `sources/periodicals/ERIC_ED337649_djvu.txt` | 1 | Medium; **absent from both harvest ledgers** (§M.2) |
| `NPTG` Hongkong Telegraph 1906-06-30 | periodical | third-party | 1906-06-30 | same | `sources/periodicals/NPTG19060630_djvu.txt` | 3 | **NULL** — 0 hits over 196,947 B held |
| `IDX` EDGAR submissions index | regulator index | n/a | 1995-01-06→2026-09-17 | retrieved 2026-09 | `sources/_index/submissions_CIK0000077476.csv` | 1 | High (FACT-about-the-index; a search index is not a fact about the company) |
| `RUN`, `UNA`, `HMX`, `A4`, `LAY` | tool ledgers / dossiers | n/a | 2026-09-29 / 2026-10-06 / 2026-10-07 | same | `sources/sec/_RUN.json`, `_UNANSWERED.csv`, `sources/harvest_mine/_index.json`, `research/A4_harvest_mine.md`, `_tmp_pepsico_layers.json` (this pass's scratch from `ia_text.py list-files`; **[merge, COR-04] relocated 2026-10-07 to `company_046_pepsico/_parts/_tmp_pepsico_layers.json`, which is the path that now resolves**) | 4 | LEAD ONLY — never counts in a tier verdict (§3) |

### T.2 Claim records for this volume (§Header–§T)

P1-01 Claim: The registrant recites that it was incorporated in Delaware in 1919 and reincorporated in North Carolina in 1986. — Date: 1995-03-28 (first held printing) — Source: 10-K FY1994 `K94` l.125-126; `REG95` l.462-463 — Source date: 1995-03-28 — URL: `sources/sec/0000077476-95-000017_0000077476-95-000017.txt` — Archived: — — Tier: 1 — Class: RESTATED (registrant's own corporate record; FOUNDER-claim class but no founder utters it) — Passage: "The Company was incorporated in Delaware in 1919 and was reincorporated in North Carolina in 1986." — Conf: Medium — Corroboration: 1 lineage (8 filings + 5 print reprints) — Conflicts: U.1, U.2
P1-02 Claim: The only 1965 sentence in the SEC corpus is inside the dividend-policy paragraph. — Date: 1995-03-28 — Source: `K94` l.557-559 (restated `K95` l.557, `K96` l.554, `K97` l.455, `K98` l.542, `K99` l.487, `K2000` l.346) — Source date: 1995-03-28 — URL: `sources/sec/0000077476-95-000017_0000077476-95-000017.txt` — Archived: — — Tier: 1 — Class: RESTATED — Passage: "Quarterly cash dividends have been paid since PepsiCo was formed in 1965, and dividends per share have increased for 22 consecutive years." — Conf: Medium — Corroboration: 1 lineage — Conflicts: U.6, U.11
P1-03 Claim: The corpus's only statement of the 1965 merger is a 2017 shareholder letter naming the two constituent persons. — Date: 2017 — Source: `AR17` l.122 (+ "to form PepsiCo." l.126) — Source date: 2017 — URL: `sources/periodicals/01-pepsi-co_djvu.txt` — Archived: — — Tier: 1 (TLS unverified per sidecar) — Class: RESTATED / RETROSPECTIVE INTERPRETATION, uttered by a CEO 52 years after the event — Passage: "Two years later, in 1965, Frito-Lay and Pepsi-Cola merged to form PepsiCo." — Conf: Low — Corroboration: 0 independent — Conflicts: U.6, U.10
P1-04 Claim: `Pepsi-Cola Company` and `Frito-Lay, Inc.` are listed as **subsidiaries** of PepsiCo, Inc., each with Delaware jurisdiction and neither with a date. — Date: as of 12/30/2000 — Source: `EX21` parsed l.677-678, l.313-314 — Source date: 2001-03-15 — URL: `sources/sec/0000077476-01-500016_ex21.htm` — Archived: — — Tier: 1 — Class: FACT (of the listing) — Passage: "SUBSIDIARIES OF PEPSICO, INC. AS OF 12/30/2000 … Pepsi-Cola Company | Delaware" — Conf: High — Corroboration: 1 — Conflicts: U.13
P1-05 Claim: No origin vocabulary occurs anywhere in the held corpus. — Date: whole corpus — Source: grep census over 38 documents — Source date: 2026-10-07 — URL: `sources/sec/*`, `sources/periodicals/*` — Archived: — — Tier: 1 — Class: FACT-about-the-corpus — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High — Corroboration: n/a — Conflicts: None
P1-06 Claim: The four `Herman` occurrences are decoys ("EGEA Hermanos S.A.", "Sherman Act" ×2, an artist "SARAI SHERMAN"), not the snack founder. — Date: whole corpus — Source: `K98` l.5366; `S4Q` l.10275; `S4QA` l.10462; `CAT48` l.1485 — Source date: 2026-10-07 — URL: as listed — Archived: — — Tier: 1 — Class: FACT-about-the-corpus — Passage: "Agreement, \"Regulatory Law\" means the Sherman Act, as amended" — Conf: High — Corroboration: n/a — Conflicts: None
P1-07 Claim: Zero documents of any kind are held dated inside 1919-01-01→1994-12-31, and zero index rows fall in 1965-01-01→1986-12-31. — Date: 2026-10-07 — Source: `IDX` computed over 3,058 rows — Source date: 2026-10-07 — URL: `sources/_index/submissions_CIK0000077476.csv` — Archived: — — Tier: 1 — Class: FACT-about-the-corpus — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High — Corroboration: 1 (regulator's own index) — Conflicts: None
P1-08 Claim: The creator of the drink is absent from the record (pharmacist/Bradham/Caleb/1893/1898/1902 all zero). — Date: whole corpus — Source: census — Source date: 2026-10-07 — URL: `sources/` — Archived: — — Tier: — — Class: **UNKNOWN** — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: UNKNOWN — Corroboration: 0 — Conflicts: U.1
P1-09 Claim: The registrant's 27 SEC documents contain the words `founder` 0 times and `founded` 0 times; all 6 print-family `founder` hits belong to other people's ventures. — Date: whole corpus — Source: census; `PX24` l.1636 — Source date: 2026-10-07 — URL: `sources/sec/`, `sources/periodicals/` — Archived: — — Tier: 1 — Class: FACT-about-the-corpus — Passage: "Ms. Cooper co-founded Medley, a membership-" — Conf: High — Corroboration: n/a — Conflicts: None
P1-10 Claim: The only officer of an origin-line legal person named inside Stage 1 is Walter S. Mack, Jr., President of Pepsi-Cola Company, in that company's own 1947-48 print. — Date: 1947-48 — Source: `CAT48` foreword — Source date: 1948 (item year) — URL: `sources/periodicals/cor5_0_s06_ss01_boxrg5_0_2008_006_f61_djvu.txt` — Archived: — — Tier: 1 — Class: CONTEMPORANEOUS (self-published) — Passage: "Walter S. Mack, Jr., President" — Conf: Medium-High — Corroboration: 1 — Conflicts: U.14
P1-11 Claim: The only counsel-signed statement of situs in the corpus prints no origin date and is limited to North Carolina law. — Date: 2001-02-28 — Source: `OP5` l.21, l.53-54 — Source date: 2001-02-28 — URL: `sources/sec/0000950103-01-500049_ex5-1.txt` — Archived: — — Tier: 1 — Class: CONTEMPORANEOUS instrument — Passage: "PepsiCo, Inc., a North Carolina corporation (the \"Company\")" — Conf: High — Corroboration: same registrant (not independent) — Conflicts: U.2
P1-12 Claim: Exhibit 21 carries 91 rows whose jurisdiction this pass could count: Delaware 81, California 4, New York 3, Texas 2, Nevada 1. — Date: as of 12/30/2000 — Source: `EX21` tag-stripped parse — Source date: 2026-10-07 — URL: `sources/sec/0000077476-01-500016_ex21.htm` — Archived: — — Tier: 1 — Class: FACT-about-the-carrier (parse method stated in §Header) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High — Corroboration: n/a — Conflicts: None
P1-13 Claim: A third origin-name person, `S.W. Frito-Lay, Ltd` of Texas, sits in the same exhibit, also undated. — Date: 12/30/2000 — Source: `EX21` parsed l.826-827 — Source date: 2001-03-15 — URL: as P1-04 — Archived: — — Tier: 1 — Class: FACT (of the listing) — Passage: "S.W. Frito-Lay, Ltd | Texas" — Conf: High — Corroboration: 1 — Conflicts: U.13
P1-14 Claim: In 1995 the beverage business ran through divisions named PCNA and PCI, which are not the subsidiary `Pepsi-Cola Company`. — Date: 1995-01-06 — Source: `REG95` l.470-471 — Source date: 1995-01-06 — URL: `sources/sec/0000077476-95-000002_0000077476-95-000002.txt` — Archived: — — Tier: 1 — Class: FACT — Passage: "PepsiCo's beverage business consists of Pepsi-Cola North America (\"PCNA\") and Pepsi-Cola International (\"PCI\")." — Conf: High — Corroboration: 1 — Conflicts: U.2
P1-15 Claim: At 1994-12-31 the registrant printed ~471,000 persons employed, 340,000 in the US, part-time included. — Date: 1994-12-31 — Source: `K94` l.338-341 — Source date: 1995-03-28 — URL: as P1-01 — Archived: — — Tier: 1 — Class: FACT (floor datum, not Stage 1) — Passage: "approximately 471,000 persons (including 282,000 part-time employees)" — Conf: High — Corroboration: 1 — Conflicts: None
P1-16 Claim: No held document states an origin-period business problem for either line. — Date: whole corpus — Source: census; `CAT48` states an art-prize problem — Source date: 2026-10-07 — URL: `sources/` — Archived: — — Tier: — — Class: **UNKNOWN** — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: UNKNOWN — Corroboration: 0 — Conflicts: U.3
P1-17 Claim: The registrant's 1995 self-description of its beverage channel is appointment-based territorial bottling of its own marks. — Date: 1995-01-06 — Source: `REG95` l.472-477 — Source date: 1995-01-06 — URL: as P1-14 — Archived: — — Tier: 1 — Class: CONTEMPORANEOUS (for 1995) — Passage: "Under appointments from PepsiCo, bottlers manufacture, sell, and distribute, within defined territories, carbonated soft drinks and syrups bearing trademarks owned by PepsiCo" — Conf: High — Corroboration: 1 — Conflicts: U.9
P1-18 Claim: By 1999 the same apparatus was quantified at ~440 licensed territories, with 8 minority-held bottlers covering ~240. — Date: FY1999 — Source: `K99` l.237-241 — Source date: 2000-03-21 — URL: `sources/sec/0000077476-00-000006_0000077476-00-000006.txt` — Archived: — — Tier: 1 — Class: FACT as disclosed — Passage: "licensed to manufacture, market, sell and distribute beverages and syrups bearing the Pepsi-Cola Beverage trademarks in approximately 440 licensed territories" — Conf: High — Corroboration: 1 — Conflicts: U.9
P1-19 Claim: Nothing in the corpus dates the franchise system's inception, and no pre-1995 text uses "franchise" of the beverage system because no pre-1995 text exists. — Date: whole corpus — Source: census — Source date: 2026-10-07 — URL: `sources/` — Archived: — — Tier: — — Class: **UNKNOWN** — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: UNKNOWN — Corroboration: 0 — Conflicts: U.9
P1-20 Claim: The snack line's origin is equally uncarried, and the folklore year 1961 occurs 0 times. — Date: whole corpus — Source: census (`Frito` 455 SEC + 130 print, 0 dated) — Source date: 2026-10-07 — URL: `sources/` — Archived: — — Tier: — — Class: **UNKNOWN** — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: UNKNOWN — Corroboration: 0 — Conflicts: U.13
P1-21 Claim: Pepsi-Cola Company ran a Fourth Annual national art exhibition with venues in four states across 1947-48. — Date: 1947-10-01→1948-04-18 — Source: `CAT48` l.1-30 — Source date: 1948 (item year; venue dates printed in the title pages) — URL: as P1-10 — Archived: — — Tier: 1 — Class: CONTEMPORANEOUS — Passage: "PEPSI-COLA COMPANY'S FOURTH ANNUAL EXHIBITION PAINTINGS OF THE YEAR" — Conf: Medium-High — Corroboration: 1 — Conflicts: U.14
P1-22 Claim: That programme's own print states its money and circulation. — Date: 1947-48 — Source: `CAT48` l.125-137 — Source date: 1948 — URL: as P1-10 — Archived: — — Tier: 1 — Class: CONTEMPORANEOUS, self-reported magnitude — Passage: "twenty cash awards totaling $15,250" / "approximately 650,000 calendars" — Conf: Medium-High — Corroboration: 1 — Conflicts: None
P1-23 Claim: Concentrate was sold to licensed independent and company-owned bottlers and to PepsiCo joint ventures. — Date: 1995-01-06 — Source: `REG95` l.474-475 — Source date: 1995-01-06 — URL: as P1-14 — Archived: — — Tier: 1 — Class: FACT — Passage: "sells its concentrates to licensed independent and company-owned bottlers and to joint ventures in which PepsiCo participates" — Conf: High — Corroboration: 1 — Conflicts: None
P1-24 Claim: The 1995 marks carried by that system are listed without any first-use or registration date. — Date: 1995-01-06 — Source: `REG95` l.478-480 — Source date: 1995-01-06 — URL: as P1-14 — Archived: — — Tier: 1 — Class: FACT — Passage: "PEPSI-COLA, DIET PEPSI, MOUNTAIN DEW, SLICE, CRYSTAL, MUG, and, within Canada, 7UP and DIET 7UP" — Conf: High — Corroboration: 1 — Conflicts: U.8
P1-25 Claim: The string `1893` in this corpus is a trademark name in a marks list. — Date: 2020-05-06 — Source: `PX20` l.1606-1609 — Source date: 2020-05-06 — URL: `sources/periodicals/pepsi-co-inc.-pep-proxy-statement-2020-05-06_djvu.txt` — Archived: — — Tier: 1 — Class: FACT (of the list) — Passage: "We own numerous valuable trademarks which are essential to our worldwide businesses, including 1893," — Conf: High — Corroboration: n/a — Conflicts: U.8
P1-26 Claim: Bottling and equipment persons appear in the same exhibit, e.g. `Pepsi-Cola Bottling International Inc.` (Nevada) and `Pepsi-Cola Equipment Corp.` (New York). — Date: 12/30/2000 — Source: `EX21` parsed l.669-686 — Source date: 2001-03-15 — URL: as P1-04 — Archived: — — Tier: 1 — Class: FACT (of the listing) — Passage: "Pepsi-Cola Equipment Corp. | New York" — Conf: High — Corroboration: 1 — Conflicts: U.13
P1-27 Claim: A third party named a Pepsi-Cola-titled corporation as a sports sponsor in 1974. — Date: 1974-12 — Source: `PR74` l.25, l.34 — Source date: 1974-12 — URL: `sources/periodicals/1974-12-press-release_djvu.txt` — Archived: — — Tier: 3 (third-party institutional release, IA print) — Class: CONTEMPORANEOUS OBSERVATION — Passage: "SPONSORED BY PEPSI COLA CANADA LTD." — Conf: High — Corroboration: 1 independent of the registrant — Conflicts: U.12
P1-28 Claim: Competitor naming in the SEC corpus is confined to the 2001 Quaker registration: `Coca-Cola` 148 times in exactly 2 of 27 documents. — Date: whole corpus — Source: census — Source date: 2026-10-07 — URL: `sources/sec/0000912057-01-000830…`, `…-01-007577…` — Archived: — — Tier: 1 — Class: FACT-about-the-corpus — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High — Corroboration: n/a — Conflicts: None
P1-29 Claim: The corpus's one non-recital `1919` is a competitor brand's founding, printed in another registrant's annual report. — Date: 2008 (for 1919) — Source: `YUM08` l.9009 — Source date: 2008 — URL: `sources/periodicals/pepsicofritolayannualreports_djvu.txt` — Archived: — — Tier: 1 (of YUM! Brands) — Class: RESTATED, and **VARIANT_TERM_HIT class for this company** — Passage: "A&W was founded in Lodi, California by Roy Allen in 1919" — Conf: High (of the sentence); 0 (as PepsiCo evidence) — Corroboration: n/a — Conflicts: U.7
P1-30 Claim: The same file carries other companies' founder stories (KFC/Sanders 1939, first franchise 1952; Langone; Cardinal Health). — Date: 2008 — Source: `YUM08` l.8920-8922, l.1566-1702 — Source date: 2008 — URL: as P1-29 — Archived: — — Tier: 1 (of YUM) — Class: RESTATED — Passage: "KFC was founded in Corbin, Kentucky by Colonel Harland D. Sanders" — Conf: High (of the sentence) — Corroboration: n/a — Conflicts: U.7
P1-31 Claim: A federal education report names Frito-Lay's workplace-literacy programme and a "Frito-Lay South" region. — Date: 1991/92 (year not established, S-15) — Source: `ERIC` l.73, l.376-377, l.546 — Source date: — — URL: `sources/periodicals/ERIC_ED337649_djvu.txt` — Archived: — — Tier: 1 — Class: CONTEMPORANEOUS (third party) — Passage: "\"What Frito-Lay Has Done in Workplace Literacy\"" — Conf: Medium — Corroboration: 1 (outside the registrant) — Conflicts: U.14
P1-32 Claim: The corpus's single `1900` is Y2K boilerplate. — Date: 1998-03-24 — Source: `K97` l.636 — Source date: 1998-03-24 — URL: `sources/sec/0000077476-98-000014_0000077476-98-000014.txt` — Archived: — — Tier: 1 — Class: FACT-about-the-corpus; decoy per rule 6 — Passage: "date-sensitive software may recognize a date using \"00\" as the year 1900 rather" — Conf: High — Corroboration: n/a — Conflicts: None
P1-33 Claim: A word-boundary year regex returns zero on IA layer filenames because `_djvu.txt` fuses a word character to the year. — Date: 2026-10-07 — Source: `LAY`, this pass's own two measurements — Source date: 2026-10-07 — URL: `_tmp_pepsico_layers.json` (**[merge, COR-04] now at `company_046_pepsico/_parts/_tmp_pepsico_layers.json`**; the repo-root path is empty) — Archived: — — Tier: — — Class: FACT-about-the-method — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High — Corroboration: n/a — Conflicts: U.15
P1-34 Claim: 1994 dividends declared were 70 cents per share against 61 cents in 1993. — Date: 1994 — Source: `K94` l.568-575 — Source date: 1995-03-28 — URL: as P1-01 — Archived: — — Tier: 1 — Class: FACT (floor datum) — Passage: "Dividends Declared Per Share (in cents)" — Conf: High — Corroboration: 1 — Conflicts: None
P1-35 Claim: The stated payout target was about one-third of the prior year's income from ongoing operations; 1994 declared came in at 34% of 1993. — Date: 1994 — Source: `K94` l.562-565 — Source date: 1995-03-28 — URL: as P1-01 — Archived: — — Tier: 1 — Class: FACT — Passage: "the 1994 dividends declared represented 34% of 1993 income from ongoing operations" — Conf: High — Corroboration: 1 — Conflicts: None
P1-36 Claim: The 1965 continuity claim survives in 2017-23 corporate print in the same words. — Date: 2017-2023 — Source: `AR17` l.3348; `AR20` l.2693; `PX22` l.2838; `PX23` l.2848 — Source date: 2017-2023 — URL: `sources/periodicals/` — Archived: — — Tier: 1 — Class: RESTATED — Passage: "Dividends — We have paid consecutive quarterly cash dividends since 1965." — Conf: Medium — Corroboration: 1 lineage — Conflicts: U.6
P1-37 Claim: The 22-year increase streak implies 1973 as its first year, eight years later than the 1965 payment claim in the same sentence. — Date: 1994 — Source: DERIVED from `K94` l.557-559 — Source date: 1995-03-28 — URL: as P1-01 — Archived: — — Tier: 1 — Class: ESTIMATE/DERIVED (1994 − 22 + 1 = 1973) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High (arithmetic); the streak's start remains the registrant's assertion — Corroboration: internal only — Conflicts: U.11
P1-38 Claim: The price series printed for 1994 is PepsiCo **Capital Stock** on the NYSE, quarterly. — Date: 1994 — Source: `K94` l.577-583 — Source date: 1995-03-28 — URL: as P1-01 — Archived: — — Tier: 1 — Class: FACT (basis named) — Passage: "a share of PepsiCo Capital Stock on the New York Stock Exchange" — Conf: High — Corroboration: 1 — Conflicts: None
P1-39 Claim: Two of the eleven held print layers belong to the wrong person or year relative to their item labels. — Date: 2026-10-06 — Source: sidecars `01-pepsi-co`, `pepsicofritolayannualreports` — Source date: 2026-10-06 — URL: `sources/periodicals/*.meta.json` — Archived: — — Tier: — — Class: FACT-about-the-corpus — Passage: "route": "download/<id>/PepsiCo, Inc. (PEP) Annual Report 2017_djvu.txt (OCR text layer)" — Conf: High — Corroboration: n/a — Conflicts: U.4, U.5, U.7
P1-40 Claim: `ERIC_ED337649` holds 130,917 B on disk but appears in neither harvest ledger. — Date: 2026-10-07 — Source: directory listing vs `HMX` (12 items) vs `A4` (12 rows); `grep -c ERIC research/A4_harvest_mine.md` = 0 — Source date: 2026-10-07 — URL: `sources/periodicals/` — Archived: — — Tier: — — Class: FACT-about-the-corpus — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High — Corroboration: n/a — Conflicts: U.14
P1-41 Claim: The probe's highest-value route failed in the CLI form it was given in and answered in the correct form. — Date: 2026-10-07 — Source: `ia_text.py list-files 01-pepsi-co` → "error: unrecognized arguments: 01-pepsi-co"; `--id 01-pepsi-co` → 102 layers — Source date: 2026-10-07 — URL: — — Archived: — — Tier: — — Class: FACT-about-the-toolchain — Passage: "error: unrecognized arguments: 01-pepsi-co" — Conf: High — Corroboration: n/a — Conflicts: U.15
P1-42 Claim: Where the registrant does document a combination it names the constituent persons, the survivor and the filing office. — Date: 2001-01-09 — Source: `S4Q` l.2044-2048, l.5704-5712 — Source date: 2001-01-09 — URL: `sources/sec/0000912057-01-000830_a2034530zs-4.txt` — Archived: — — Tier: 1 — Class: CONTEMPORANEOUS instrument; (PB) for Stage 1 — Passage: "the merger of BeverageCo, Inc. with and into Quaker, with Quaker surviving the merger as a wholly-owned subsidiary of PepsiCo" — Conf: High — Corroboration: 1 — Conflicts: U.10

STATUS: WRITTEN

---

## U

STATUS: WRITTEN 2026-10-06

### U.1 1893 vs 1898 vs 1902 for the creation of the drink
CLAIM A: the drink was created in 1893. CLAIM B: it was created in 1898 (and a third telling says a corporation
was "incorporated in 1902"). WHY THEY DIFFER: three oral/printed tellings of one brand story, none of them
sourced to a document this corpus holds. EVIDENCE WEIGHT: `1893` = 1 occurrence and it is a **trademark name**
(P1-25); `1898` = 0; `1902` = 0; `1904` = 0 across 38 documents. BEST-SUPPORTED INTERPRETATION: all three are
**UNKNOWN**; the corpus cannot rank them. RESIDUAL UNCERTAINTY: total — nothing in this repository names any
of them, and families (b)/(e) are UNTRIED. CONFIDENCE: High (in the zero), **UNKNOWN** (in the event).

### U.2 The registrant's 1919 charter vs the brand's pre-1919 past
CLAIM A: "incorporated in Delaware in 1919" (8 filings, 5 print reprints). CLAIM B: the brand line begins in
the 1890s. WHY THEY DIFFER: A is a **legal-person** statement made for identification purposes; B is a
**product** statement made in later marketing and never in these documents. EVIDENCE WEIGHT: A is carried in
one lineage; B is carried nowhere (0 occurrences of `since 18`). BEST-SUPPORTED INTERPRETATION: on its own word
the registrant begins in 1919; importing an earlier brand date into the registrant's chronology is hard-rule-4
error (the Morgan Stanley / AT&T / Ford class). RESIDUAL UNCERTAINTY: whether 1919 is even the beverage
person's own date rather than a later reading of it — unresolvable without the charter file. CONFIDENCE:
Medium (A as a printed claim); **UNKNOWN** (A as the founding of anything).

### U.3 Is `Pepsi-Cola Company` the registrant, its subsidiary, or its predecessor?
CLAIM A: the recital makes 1919 the registrant's own charter. CLAIM B: `EX21` lists `Pepsi-Cola Company` as a
**subsidiary** in 2000, so it is a different legal person inside the group. WHY THEY DIFFER: the recital
speaks of the parent, the exhibit of a child; both can be true. EVIDENCE WEIGHT: A = 13 occurrences, one
lineage; B = one table, 91 countable rows (P1-04, P1-12). BEST-SUPPORTED INTERPRETATION: they are **two
persons**; the parent's 1919 date cannot be transferred to the subsidiary, and the subsidiary's charter date is
not in the corpus. RESIDUAL UNCERTAINTY: whether the 1919 Delaware corporation is the same body later renamed
`Pepsi-Cola Company`, or its parent — the corpus contains no name-change instrument. CONFIDENCE: High (that
both are listed) / **UNKNOWN** (identity relation).

### U.4 The item metadata year 1938 vs the held layer 2017
CLAIM A: IA metadata for `01-pepsi-co` = "PepsiCo Annual Reports: 1938-", `date 1938-01-01`, `creator "PepsiCo
Inc."`. CLAIM B: the bytes actually held are the **2017** layer (sidecar `url`, `route`). WHY THEY DIFFER: an
uploader's item-level label versus a specific file inside the bound run. EVIDENCE WEIGHT: B is bytes; A is a
catalogue row (§3: an index row is not a fact). BEST-SUPPORTED INTERPRETATION: the metadata is an RD-130
item-date artefact; only the 2017 layer is in evidence. RESIDUAL UNCERTAINTY: whether a 1938 layer exists at
all — `LAY` says a layer **named** 1938 does exist (16,075 B) and is unfetched. CONFIDENCE: High.

### U.5 "PepsiCo, Inc." filenames over years the person did not exist
CLAIM A: 86 layers are named "PepsiCo, Inc. (PEP) Annual Report 1938…1964…". CLAIM B: the registrant's own word
is that PepsiCo, Inc. was formed in **1965**. WHY THEY DIFFER: uploader renaming versus the issuer's own
history. EVIDENCE WEIGHT: both statements are in the corpus; the 7 layers tagged "(Frito-Lay)" for 1958-1964
show the uploader knew some of them belonged to another person. BEST-SUPPORTED INTERPRETATION: the pre-1965
layers belong to **predecessor persons** (rule 4) and must be read title-page by title-page before any
attribution. RESIDUAL UNCERTAINTY: which person each of the 27 pre-1965 layers actually carries. CONFIDENCE:
High (that the conflict exists); **UNKNOWN** (per-layer attribution).

### U.6 1965 as a dividend fact vs 1965 as a merger fact
CLAIM A: "Quarterly cash dividends have been paid since PepsiCo was formed in 1965" (7 filings, 4 print
reprints, always in a dividends paragraph). CLAIM B: "in 1965, Frito-Lay and Pepsi-Cola merged to form PepsiCo"
(1 sentence, 2017 CEO letter). WHY THEY DIFFER: A proves continuity of payment; only B asserts a transaction.
EVIDENCE WEIGHT: A is one lineage in a legal disclosure; B is one lineage in marketing-adjacent print, 52
years later, with **no mechanics**. BEST-SUPPORTED INTERPRETATION: keep them separate — A supports "the
registrant claims an unbroken dividend record from 1965"; B is the corpus's sole carrier of the merger story
and is **Low**. RESIDUAL UNCERTAINTY: the whole of the transaction (parties' exact persons, date, terms,
survivor). CONFIDENCE: Medium (A) / Low (B).

### U.7 Whose `1919`, whose founder story
CLAIM A: 1919 is the registrant's charter year. CLAIM B: `YUM08` prints "A&W was founded … in 1919". WHY THEY
DIFFER: B is another registrant's origin sentence inside a file catalogued under this company's harvest item.
EVIDENCE WEIGHT: neither corroborates the other; B is 100% irrelevant to PepsiCo. BEST-SUPPORTED
INTERPRETATION: any count of `1919` that mixes the two is a **VARIANT_TERM_HIT inflation**; this dossier
reports 14 occurrences and attributes 13 / 1. RESIDUAL UNCERTAINTY: none — the classification is the point.
CONFIDENCE: High.

### U.8 The `1893` hit
CLAIM A: `1893` appears in the corpus, so a carrier for 1893 exists. CLAIM B: the occurrence is the string
"1893," inside a list of owned trademarks (`PX20` l.1606: "including 1893, Agusha, Amp Energy, Aquafina…").
WHY THEY DIFFER: a brand name (a Mexican cola) versus a calendar year. EVIDENCE WEIGHT: B, decisively.
BEST-SUPPORTED INTERPRETATION: the origin date 1893 remains **0-occurrence**; this hit is a keyword decoy of
exactly the class rule 6 names. RESIDUAL UNCERTAINTY: none. CONFIDENCE: High.

### U.9 The franchise system's existence vs its inception
CLAIM A: the franchise-bottler system is FACT — "Under appointments from PepsiCo, bottlers … within defined
territories" (1995), ~440 licensed territories (1999). CLAIM B: the system's origin is unknown. WHY THEY
DIFFER: A is a description of a structure at the archive floor; B is the history nobody printed. EVIDENCE
WEIGHT: A carries; B carries nothing in-corpus. BEST-SUPPORTED INTERPRETATION: existence High for 1995-99,
**UNKNOWN** for inception; a §7-adapted dossier must not let the former leak into the latter. RESIDUAL
UNCERTAINTY: the entire pre-1995 franchise history. CONFIDENCE: as stated.

### U.10 Probe A.3 ("the merger story itself: UNKNOWN — no carrier in this corpus") vs this pass
CLAIM A (probe, 2026-10-06 17:28): no carrier states the 1965 merger. CLAIM B (this pass, after `sources/
periodicals/` arrived at 18:03-18:14): `AR17` l.122 states it, once. WHY THEY DIFFER: the corpus grew under
the probe; §14 r11. EVIDENCE WEIGHT: B is bytes on disk now. BEST-SUPPORTED INTERPRETATION: **the probe's
conclusion is superseded on this point and carried forward unchanged on the rest** — the merger has a carrier,
but it is a single 2017 self-narrative line, so the date's confidence stays Low. RESIDUAL UNCERTAINTY: whether
any stronger carrier exists (FETCH 1, FETCH 4). CONFIDENCE: High (of the supersession).

### U.11 The `1965` count
CLAIM A: 1965 appears 22 times, so 1965 is well corroborated. CLAIM B: of 22 occurrences, 15 are dividend
sentences, 2 are a director's tenure ("ROBERT H. STEWART, III, a director since 1965"), 2 are an unrelated
facility built in 1965 (`ERIC`), 1 is the merger sentence, and the remainder are restatements of the same
dividend clause. WHY THEY DIFFER: raw hit count versus function of each sentence. EVIDENCE WEIGHT: B.
BEST-SUPPORTED INTERPRETATION: **a term frequency is not a corroboration count**; the merger has one carrier
and the tenure rows must never be quoted as founding evidence. RESIDUAL UNCERTAINTY: none. CONFIDENCE: High
(the per-file split measured this pass: `K94` l.296, `K95` l.526 for the director).

### U.12 The 1974 Canadian sponsor
CLAIM A: `PR74` is in-window (1974) naming of a Pepsi-Cola corporation. CLAIM B: it names `Pepsi Cola Canada
Ltd.`, a different person from the US constituent, in a third-party university release. WHY THEY DIFFER: brand
identity versus legal identity. EVIDENCE WEIGHT: both — the release is genuine and contemporaneous, and
genuine about a *different* person. BEST-SUPPORTED INTERPRETATION: cite as (b)-family peripheral evidence of
the brand's sponsorship activity in Canada, never as an event of the registrant or of its US constituent.
RESIDUAL UNCERTAINTY: the relation between the Canadian and Delaware persons. CONFIDENCE: High.

### U.13 Undated subsidiaries versus dated folklore
CLAIM A: `Pepsi-Cola Company` \| Delaware and `Frito-Lay, Inc.` \| Delaware (PepsiCo exhibit, undated). CLAIM B:
the folklore dates each constituent (1902; 1961; 1938; 1898). WHY THEY DIFFER: an exhibit lists situs, not
charter dates, and the corpus prints `1902` 0, `1961` 0, `1938` 0 times. EVIDENCE WEIGHT: A only.
BEST-SUPPORTED INTERPRETATION: the constituent dates are **UNKNOWN**; the exhibit is the strongest statement
about those persons available here. RESIDUAL UNCERTAINTY: everything the folklore asserts. CONFIDENCE: High.

### U.14 Family classification of the in-window print
CLAIM A (probe): `cor5_…f61` is a Corcoran Gallery **art catalogue**, "not corporate print", and should be
expected to yield only a sponsor naming. CLAIM B (`HMX`, `A4`): the same item is classed `corporate_print` and
graded `TIER1_CANDIDATE_TEXT`. CLAIM C (this pass): the bytes are a Pepsi-Cola Company publication about an art
prize — a **sponsor naming that the sponsor itself printed**, in-window. WHY THEY DIFFER: three different
questions — what family the tool files it under, what the classifier promotes, and what the document *is*.
EVIDENCE WEIGHT: C. BEST-SUPPORTED INTERPRETATION: it is corporate print **of a subsidiary-line person**, and
its Tier-1-ness is about the person's existence, not about a chronology; the probe's caution and the ledger's
promotion are both half-right. RESIDUAL UNCERTAINTY: whether the Corcoran series contains further Pepsi-Cola
Company layers (the item sits in a `boxrg5_0_…` gallery box). CONFIDENCE: Medium-High.

### U.15 What the tier stamp and the tooling said, and what the bytes say
CLAIM A: `gates.py` printed `tier: exemplar (no tier stated in this company's research/ dossiers — exemplar
assumed)` (probe A.11). CLAIM B: the stated tier is **T3 register** (probe A.7). CLAIM C (this pass): the
corpus grew (11 print layers, 4,130,659 B) and the decisive route was run, so the evidence for the tier
changed shape but not the verdict. WHY THEY DIFFER: a tool default versus a dossier finding versus a
re-measurement. EVIDENCE WEIGHT: B/C; A is a tool default and must never be read as a finding.
BEST-SUPPORTED INTERPRETATION: **Stage 1 remains T3** — 1B and 1C stay PROVISIONAL because 48 in-window
corporate-print layers (917,852 B + 1,994,223 B) are named but unfetched, and one fetched in-window document
exists (`CAT48`). RESIDUAL UNCERTAINTY: whether FETCH 1 delivers in-window naming of either constituent, which
would regrade 1B/1C to T2 in a single pass. CONFIDENCE: High (the T3 call as measured today).

STATUS: WRITTEN

---

## registers

STATUS: WRITTEN 2026-10-06

**[merge, 2026-10-07]** The sentence above is the author's scope statement and was true of the writing pass. The nine registers **were** created by the merge, at this company root, from the blocks that sat here: `sources.csv` S4479-S4494 replace the provisional `P1S01-P1S16` (COR-01) and the blocks themselves are no longer printed in this volume (COR-05).

*Emit-only. **No register CSV on this company was opened, created or edited by this pass** — the company root
and `research/` hold none, so coverage findings of the form "no registers yet" are the expected pre-merge
state and are not defects. `stage` is the controlled literal `stage1` on every row. Every `P1x` id is
dossier-local; `source_id` values are **provisional and will be re-minted centrally at merge** by
`tools/id_mint.py` (RD-123). `independence_note` carries the §3 lineage finding on every registrant row: the
27 SEC documents across 17 accessions, and the corporate-print layers that reprint the same Item 1 sentence,
are **one corporate record** and are never counted as corroboration of one another. Fields that can contain a
comma are quoted; every row is emitted at its header's width. `derived_arithmetic` is filled on every
DERIVED row and reads `not_derived` where a cell is intentionally non-empty.*

**[merge]** `sources.csv` - **APPLIED 16 rows** at the company root (18 cols; keys S4479-S4494, 0 duplicate keys); header byte-identical to `company_001_amazon/sources.csv`. Per §9.1(2) register data lives in CSV, not in prose (COR-05), so the fenced block is not reprinted in this volume; its verbatim emission of record stays at `_parts/s1_p1.md` l.999-l.1021. **DO NOT RE-APPLY - these rows are already on disk.**


**[merge]** `quantitative.csv` - **APPLIED 25 rows** at the company root (12 cols; no key column; 0 duplicate row texts); header byte-identical to `company_001_amazon/quantitative.csv`. Per §9.1(2) register data lives in CSV, not in prose (COR-05), so the fenced block is not reprinted in this volume; its verbatim emission of record stays at `_parts/s1_p1.md` l.1023-l.1054. **DO NOT RE-APPLY - these rows are already on disk.**


**[merge]** `timeline.csv` - **APPLIED 16 rows** at the company root (11 cols; no key column; source_id repeats as a carrier reference); header byte-identical to `company_001_amazon/timeline.csv`. Per §9.1(2) register data lives in CSV, not in prose (COR-05), so the fenced block is not reprinted in this volume; its verbatim emission of record stays at `_parts/s1_p1.md` l.1056-l.1078. **DO NOT RE-APPLY - these rows are already on disk.**


**[merge]** `conflicts.csv` - **APPLIED 15 rows** at the company root (15 cols; keys U.1-U.15, 0 duplicate keys); header byte-identical to `company_001_amazon/conflicts.csv`. Per §9.1(2) register data lives in CSV, not in prose (COR-05), so the fenced block is not reprinted in this volume; its verbatim emission of record stays at `_parts/s1_p1.md` l.1080-l.1101. **DO NOT RE-APPLY - these rows are already on disk.**


**[merge]** `data_gaps.csv` - **APPLIED 15 rows** at the company root (8 cols; no key column; 0 duplicate row texts); header byte-identical to `company_001_amazon/data_gaps.csv`. Per §9.1(2) register data lives in CSV, not in prose (COR-05), so the fenced block is not reprinted in this volume; its verbatim emission of record stays at `_parts/s1_p1.md` l.1103-l.1124. **DO NOT RE-APPLY - these rows are already on disk.**


**[merge]** `decisions.csv` - **APPLIED 4 rows** at the company root (15 cols; no key column; 0 duplicate row texts); header byte-identical to `company_001_amazon/decisions.csv`. Per §9.1(2) register data lives in CSV, not in prose (COR-05), so the fenced block is not reprinted in this volume; its verbatim emission of record stays at `_parts/s1_p1.md` l.1126-l.1136. **DO NOT RE-APPLY - these rows are already on disk.**


**[merge]** `validation.csv` - **APPLIED 4 rows** at the company root (11 cols; adjudicated block, COR-06); header byte-identical to `company_001_amazon/validation.csv`. Per §9.1(2) register data lives in CSV, not in prose (COR-05), so the fenced block is not reprinted in this volume; its verbatim emission of record stays at `_parts/s1_p1.md` l.1138-l.1148. **DO NOT RE-APPLY - these rows are already on disk.**


**[merge]** `failures.csv` - **APPLIED 8 rows** at the company root (11 cols; adjudicated block, COR-06); header byte-identical to `company_001_amazon/failures.csv`. Per §9.1(2) register data lives in CSV, not in prose (COR-05), so the fenced block is not reprinted in this volume; its verbatim emission of record stays at `_parts/s1_p1.md` l.1150-l.1164. **DO NOT RE-APPLY - these rows are already on disk.**


**[merge]** `channels.csv` - **APPLIED 3 rows** at the company root (11 cols; no key column; 0 duplicate row texts); header byte-identical to `company_001_amazon/channels.csv`. Per §9.1(2) register data lives in CSV, not in prose (COR-05), so the fenced block is not reprinted in this volume; its verbatim emission of record stays at `_parts/s1_p1.md` l.1166-l.1175. **DO NOT RE-APPLY - these rows are already on disk.**


*Rows withheld: none. Every row emitted above is attributable to a named register, and no row was left in
prose because it could not be keyed. Claim records P1-01 … P1-42 are all in §T.2, and register rows cite them
so the merge can check 1:1 parity between the 15 §U anchors declared at the head of this volume
(`ANCHORS: U.1-U.15`) and the 15 conflicts.csv rows. **Rows emitted per register: sources 16,
quantitative 25, timeline 16, conflicts 15, data_gaps 15, decisions 4, validation 4, failures 8, channels 3 =
106 rows across all nine registers.***

STATUS: WRITTEN

---

## Untried

STATUS: WRITTEN

**Three states only, and an untried family is never a null (§14 r5, rule 5 of the author brief).** Everything
below was *not attempted by this pass*, in most cases because attempting it means writing bytes into
`sources/` — outside this dossier's WRITE scope — and the pipeline rule is that an agent returns a
`FETCH REQUEST:` rather than running a retrieval a script can reach (§15.1).

1. **Family (b) web archives — UNTRIED, 0 calls by this pass and 0 by the probe.** Still no
   `sources/web_archive/` path for this company (re-enumerated this pass: `sources/` holds `_index`, `sec`,
   `periodicals`, `corporate_print` (empty), `harvest_mine`). The probe's remedy stands: a CDX pass in the
   shape Microsoft's `cdx_microsoft_com_earliest_200.json` uses, for `PepsiCola.com` / `fritolay.com`,
   1996–2005.
2. **Family (e) auction / museum / manuscript — UNTRIED, and no query block for it exists corpus-wide**
   (families present in `tools/queries.json`: chronicling_america, internet_archive, corporate_print,
   hathitrust, google_books). This is a corpus-level hole, not a PepsiCo miss.
3. **Family (c) Chronicling America and HathiTrust — UNTRIED as queries** (both harvest rows are
   `SKIPPED: global max-requests cap 600 reached` / `hard stop: 5 consecutive failures (host halted)`). A
   cap is a tool limit, not archive emptiness.
4. **Family (c/d) the Internet Archive 747-hit wide set beyond row 20, filtered `date<=1965` — UNTRIED.**
   Only the first 20 rows were ever sampled, and those are court dockets naming franchisees (rule-5 decoys).
5. **Family (d) the 48 in-window corporate-print layers inside item `01-pepsi-co` — UNTRIED (bytes), now
   NAMED and COSTED.** This is the one route this pass advanced: it ran the script's file-layer listing
   (§A.4) and found 27 layers 1938–1964 (917,852 B) and 21 layers 1965–1986 (1,994,223 B). Reading their
   text is still untried — that is FETCH 1.
6. **`research/A4_harvest_mine.md`'s own 21 items left untried at the `--limit`** — the pass stopped
   mid-candidate-list (43 candidates, 12 mined), so 21 candidate identifiers were never opened, and this
   dossier cannot say whether any of them holds in-window text.
7. **`sources/sec/_SKIPPED.csv` (75 skipped slots) — UNTRIED.** The stored 27 of 106 attempted is a sample.
8. **The 88 in-window filings never listed** (`--max-docs 30`) — UNTRIED by listing, not by emptiness.
9. **EDGAR pre-1994 paper era / SEC legacy microfilm — UNTRIED and unreachable by this toolchain.** Named so
   no later agent reads the 1995-01-06 floor as the company's filing history.
10. **The Delaware Division of Corporations charter file** for the 1919 line and for the 1965 merger
    certificate — UNTRIED; no script in `tools/` reaches a state registry. This is the only route to a first
    **independent** lineage for this registrant (§3).
11. **Trademark register** (first use / registration of PEPSI-COLA) — UNTRIED, no script.
12. **The Corcoran gallery box series** (`cor5_0_s06_ss01_boxrg5_0_…`) beyond the one catalogue held —
    UNTRIED; the naming pattern suggests sibling items that may name Pepsi-Cola Company again in-window.

**UNTRIED-by-order, stated exactly.** Family (d) carries a **YEAR-faceted zero that is an artefact, not a
null**: `drop_year_facet` rewrites `params["q"]` only, corporate-print tasks have no `q`, so the whole family
is skipped and reports empty (probe A.6(d); re-confirmed this pass — `sources/corporate_print/` is still
0 bytes while CP-classified items sit in `sources/periodicals/`). The probe named
`ia_text.py list-files 01-pepsi-co` as the cheapest route to break that artefact. **This pass did not leave it
UNTRIED-by-order: it ran a script that already exists** and reported the result in §A.4 — including that the
probe's CLI form does not parse (`error: unrecognized arguments: 01-pepsi-co`; `mode` is positional and the
identifier must be passed with `--id`). What remains UNTRIED is the *contents* of those layers, not their
existence.

---

## Fetch requests

STATUS: WRITTEN

```
FETCH REQUEST 1  (highest value; regrades 1B and 1C if it delivers)
  route:   python tools/ia_text.py fetch --id 01-pepsi-co --company-dir <dir> --file "<layer>"
           layers to pull, in this order:
             "PepsiCo, Inc. (PEP) Annual Report 1938_djvu.txt"        (16,075 B)
             "PepsiCo, Inc. (PEP) Annual Report 1958 (Frito-Lay)_djvu.txt" (31,338 B)
             "PepsiCo, Inc. (PEP) Annual Report 1964 (Frito-Lay)_djvu.txt" (31,240 B)
             "PepsiCo, Inc. (PEP) Annual Report 1965_djvu.txt"        (70,338 B)
             "PepsiCo, Inc. (PEP) Annual Report 1966_djvu.txt", then 1970, 1975, 1980, 1985, 1986
             then all remaining 1938-1964 layers (27 layers, 917,852 B total)
  item:    https://archive.org/details/01-pepsi-co   (102 text layers, 17,860,942 B; measured by this pass)
  settles: whether in-window corporate print names either origin-line legal person with a date, and which
           person each pre-1965 layer actually carries. One fetched in-window annual report that prints its
           own incorporation history converts 1B/1C from T3 to T2 and converts §U.1/§U.13 from UNKNOWN.
  caution: the FILENAME is an uploader's anachronism (U.4, U.5): 27 layers print "PepsiCo, Inc." for years in
           which, on the registrant's own word, the person did not exist, and 7 of them (1958-1964) are tagged
           "(Frito-Lay)". Read the title page of each layer and record WHICH legal person's name is printed
           before crediting the layer with anything. Do not cite a layer as PepsiCo print until its own
           inside title says so.
```
```
FETCH REQUEST 2
  route:   python tools/periodical_harvest.py --company pepsico --only-family chronicling_america
           and, after fixing drop_year_facet (periodical_harvest.py:1401-1427) to strip year_range under
           --facet-free, the whole corporate_print task set
  items:   CA 'Pepsi-Cola' beverage 1890-1975; CA 'Pepsi' Purchase / Harrison NY 1950-1995;
           HT 'Pepsi-Cola' bottling company
  why:     every one of these rows is UNANSWERED because of a tool cap or a host halt, not because the
           archive is empty. The trade press is where a franchise-bottler naming (S-07) would live.
```
```
FETCH REQUEST 3
  route:   advancedsearch paging past rows=20 on
           ("Pepsi-Cola" OR "Pepsi Co" OR "Frito" OR "Lay's") AND mediatype:texts   [numFound 747]
           filtered to date <= 1965
  settles: whether any pre-1966 periodical names the beverage company outside a federal court docket. The
           sampled rows are usfederalcourts decisions naming bottling franchisees - same brand, different
           legal person (rule 5 decoys).
```
```
FETCH REQUEST 4  (low cost; also closes S-05)
  identifiers already in the harvest index whose bytes were never reached:
    twelvefullounces0000mart   (1962, printdisabled, HTTP 401 after 3 tries) - in-window by title year and
                               the only other candidate the ledger promotes; verify WHICH string matched
                               before citing, and expect a pepsin/Pepsi advertisement, not a naming.
    report-100-of-corn-in-frito-lay-sun-chips-completely-gmo  (404) - a modern corn/GMO item, not print.
  also:    the 1965 registration statement or merger proxy for PepsiCo, Inc. - EDGAR has nothing before
           1995-01-06 for this CIK (measured), so this needs SEC legacy paper / microfilm: a human task.
```
```
FETCH REQUEST 5  (the first INDEPENDENT lineage, and the only thing that can lift §U.1 above UNKNOWN)
  Delaware Division of Corporations: charter file for the 1919 Delaware corporation; the 1965 certificate of
  merger naming the constituent corporations of "PepsiCo, Inc."; certificates of incorporation for
  "Pepsi-Cola Company" and "Frito-Lay, Inc." as listed undated in Exhibit 21.
  No script in tools/ reaches a state registry - dispatch only if the orchestrator can order a retrieval.
  Until then every origin date in this dossier rests on the company's own word, which is the finding.
```

---

**What this pass did NOT examine (coverage, reported as §REPORT requires).** I did not open: the 15 unused SEC
accessions' bodies (of the 27 stored documents this pass read in full or in relevant part those carrying the
recitals, `EX21`, `OP5`, `S4Q` and `S4QA` — the remainder (`0000077476-95-000005`, `-95-000016`, `-96-000003`,
`-99-000018`, `-00-000010`, the ex-23 f/g/h consents, `-01-007577` ex-4_a and ex-99 d/e, `-00-000047`) were
enumerated and greped but not read for content; `ERIC_ED337649` and `NPTG19060630` were tested for naming and
not otherwise read; the `AR20`/`PX22`/`PX23`/`PX24` layers were searched, not read; **none of the 48
in-window archive layers, and no bytes outside `company_046_pepsico/sources/`**, no other company's dossier,
no XBRL series (none exists for this company), and no web resource — **0 web calls beyond the single archive
file-listing run named in §A.4, whose stdout is the repo-root scratch file
`E:\founder's playbook\_tmp_pepsico_layers.json` (mine, this pass; no one else's data lives there). **[merge, COR-04 2026-10-07: moved out of the repo root to `founders_playbook/01_companies/company_046_pepsico/_parts/_tmp_pepsico_layers.json`; cited by `sources.csv` S4492 and `data_gaps.csv` S-10. The repo root carries no company scratch now.]****
Registers at the company root were not created, opened or edited (§15: the merge applies the blocks above).
The probe's and A4's ledgers were used as leads only, never as evidence, and every family verdict this pass
did not re-measure is labelled as inherited in §T.1.
