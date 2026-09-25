# walmart_s1_repairs.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T20:46:34Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## HDR-1 and HDR-2

**Status: both repaired; the propagation path is closed and gate-checked (`corrections` now PASSes 2/2).**

**Verified against held documents before anything was written** (re-run on this pass, not taken from the
audit): `grep -ci delaware sources/periodicals/WALMART_AR_1972…1980.txt` → **0 in every one of the nine**;
`grep -ciE "wal-mart,[[:space:]]*inc"` over the same nine → **0 in every one** (the pattern excludes
"Wal-Mart Stores, Inc."); `grep -c 1962` → **0** in AR_1972, **0** in AR_1973, **1** in AR_1974 (body sentence
at `WALMART_AR_1974.txt` "first Wal-Mart Discount City store opened in Rogers. Arkansas in 1962"). So neither
HDR clause had any documentary carrier, and the header was the only place in the corpus still teaching them.

**The header now states, with the carrier named for each element** (`stage_1.md`, the `**Company:**` block):

| Element in the corrected identity line | Carrier named in the header |
|---|---|
| Registrant at the close: **Wal-Mart Stores, Inc.** | **S0101** (`WALMART_AR_1972.txt`) audited capital note → §B.0, §R |
| **State of incorporation: UNKNOWN** | the nine-file verified negative → §B.0 row 2, conflict **U.014** |
| **1969 year-only, company-asserted; day UNKNOWN** | the registrant's curated history page **S0141** (`sources/EXTRACT_corporate_walmart_history_timeline.md`) + the negative → §Q 1969 row, **U.013** CLAIM A |
| **Consolidated registrant begins 1970-02-01** by pooling out of **Walton Enterprises, Inc.** | **S0101 Note 1** → §B.0 row 5, **U.013** CLAIM C |
| **1962 operating start is registrant-retrospective** | **S0103**, printed 1974-03-21 → §B-1a, §C.0, **U.001** |
| **"Wal-Mart, Inc., an Arkansas corporation" withdrawn** | 0 occurrences on disk; Tier-4 folklore at §B.0, **U.013** CLAIM B, **COR-302** |
| No legal person named for 1945–1962 | §B.0 row 6, documented null **U.108** |

**Withdrawal recorded as new corrections, superseding not erasing.** `CORRECTIONS.md` did not exist at this
company, so it was created (it is also why the `corrections` gate reported "gate DID NOT RUN" before this
pass). Two ids: **COR-301** (Delaware + 1969-10-01) and **COR-302** (the Arkansas operating entity). Block
3xx chosen because no `COR-3nn` exists anywhere in the repo (checked repo-wide), so no cross-company id
collision is possible. Each entry names the withdrawn text, the file that carried it, the re-run document
evidence, the replacement reading with its carrier, what is deliberately **not** erased, and the open FETCH
routes. Propagation: both ids reach `conflicts.csv` **U.013**/**U.014** in a HEADER PROPAGATION note, the
volume's identity line and assembly note, and `_MANIFEST.md`'s defect list — the gate's invariant
(retraction reaches registers **and** a volume) is satisfied mechanically, not by assertion.

**What was left visible on purpose.** `_parts/s1_p1.md`'s header (4 Delaware / 4 date hits), `stage_1.md`
§D record **D-R03** and its correction **D-R03c**, §U.0's mapping row, §U.1's **U.014** CLAIM A, and part 3's
register-handoff rows inside `stage_1_part_2.md`: the correction-beside-the-row pattern is the audit trail
and the auditor instructed that D-R03/D-R03c not be touched. **No claim was back-solved and no gap filled by
inference:** state of incorporation remains **UNKNOWN**, not "Arkansas", and the 1962 entity remains unnamed.

## Sibling sweeps

Whole-corpus sweep over the three assertions, per-file line counts (`grep -ic`), **after** the repair.
Every hit was opened and classified; the only bucket that matters is **stale**, which is now **zero**
everywhere outside the protected audit trail.

| Assertion | stage_1.md | part_2 | registers | _MANIFEST | CORRECTIONS.md | `_parts/` (protected) | research dossiers (read-only) |
|---|---|---|---|---|---|---|---|
| "Delaware" | 13 | 3 | 3 (conflicts U.014, timeline 1969 row, data_gaps) | 2 | 6 | 15 (s1_p1 4, s1_p3 11) | 0 |
| "1969-10-01" | 8 | 2 | 1 (conflicts U.014) | 2 | 3 | 9 (s1_p1 4, s1_p3 5) | 0 |
| "Wal-Mart, Inc." (non-Stores) | 6 | 2 | 1 (conflicts U.013) | 2 | 6 | 7 (s1_p1 4, s1_p3 3) | 12 (A2 3, A 5, B 4) |

**Classification of the 27 volume hits + 5 register + 4 manifest hits:**

- **Correct (states the finding):** §B.0 state-of-incorporation row (UNKNOWN + verified negative), §B.0
  1969-year row, §B.0 folklore row, §R legal-person row, §Q 1969 row, `conflicts.csv` U.014
  `best_supported_interpretation`, `timeline.csv` 1969 row, `data_gaps.csv` predecessor-entity gap,
  part_2 §U.211 (names "Wal-Mart, Inc." as the **target** of an untried registry search, not as a fact).
- **Quoted source text:** §U.1 U.014 CLAIM A and §U.0's mapping row quote part 1's header verbatim; the two
  `>>> REGISTER ROWS FOR MERGE <<<` rows in `stage_1_part_2.md` (and the same rows in `_parts/s1_p3.md`)
  quote the drafted conflict text. Left byte-for-byte — they are the merge's audit trail.
- **Retraction marker:** the new identity line ("**0 times**", "**withdrawn**", COR-301/COR-302), the
  rewritten assembly note, §D-R03c, §U.4's protected list, `_MANIFEST.md` items 1 and 5, all of
  `CORRECTIONS.md`.
- **Carried original kept beside its correction (disclosed, not stale):** §D-R03 in `stage_1.md`, and
  `_parts/s1_p1.md`'s header — both named in `CORRECTIONS.md` as deliberately unretracted.
- **STALE: 0.** Before the pass the count was **2** (both in the identity line: the Delaware clause and the
  Arkansas-operating-entity clause; the second was disclosed nowhere in the instruction layer).

**Sweep hazard found and reported, not edited (I do not own `tools/`):** a hit-count sweep over
`Wal-Mart, Inc` also matches inside `Wal-Mart, Inc. Stores`-style prose and over-counts
"Delaware" in retraction sentences, so raw counts cannot classify themselves. The per-hit classification
above is why the totals should not be lifted as a metric.

## MERGE-1 correction

**Appended, not rewritten.** `03_quality_control/walmart_s1_merge.md` now carries a dated section
*"Correction appended 2026-09-26 by the Stage-1 repair pass (append-only; nothing above is rewritten)"*.
Its six sections were **found written** on this pass (substantive row-accounting, `STATUS: WRITTEN`
markers), so AUDIT 1's factual premise — a 476-byte unwritten scaffold, hence a dangling pointer — is
**superseded in fact**: the merge does have an application account on paper, and §11's provenance clause is
now falsifiable. The appended section states what the sheet got wrong and why:

1. **"Registers cite 80 anchors; volume 1 declares 82"** was never an anchor-to-anchor comparison. The 82 is
   **77 minted anchors + 5 §U subsection headings**; the 80 is **77 anchors + 3 headings echoed as register
   prose**. Parity was accidental **on both sides**, not just on the narrative side the sheet names.
2. The sheet's parenthetical discloses the incidental clearing of **U.2/U.3** but omits **U.0**, which clears
   for a third reason: it matches **inside the sub-number `U.0.1`**, because `.` is a word boundary in the
   gate's `\bU\.(\d+[a-z]?)\b`.
3. The volume front matter the same merge wrote said the gate "reports U.1–U.4". It reported **U.1 and U.4
   only**. Both texts are corrected in `stage_1.md`, and the correction is cross-referenced from the sheet.
4. **"Gate after: Findings 1" is no longer reproducible** — the same command returned **2** on this pass
   because the gate gained a `citation resolution` check after the merge was written. The merge is not wrong
   about its own observation; the instrument moved. That is stated plainly rather than read as a merge error.
5. The sheet's own UNTRIED remedy (retitle §U's subsections) is marked **superseded** by the explicit
   declaration route, and the 4 register rows this pass touched are listed for the merge owner's census.

No history in the sheet was deleted, no claim of the merge's was quietly overwritten, and the sheet's row
arithmetic (99 requested / 95 applied / 4 refused) was not re-adjudicated — it is outside this pass's scope
and untouched.

## Anchor grammar

**Route chosen: the explicit declaration, not the rename.** Derived from evidence by replicating the gate's
own set functions over the live corpus (`gates.py` read-only, imported and called in a throwaway script —
`tools/` not edited), rather than by pattern-matching the ids:

| Set | Members | Note |
|---|---|---|
| `_anchors_declared(stage_1.md)` | **82** | 77 three-digit anchors + `U.0`,`U.1`,`U.2`,`U.3`,`U.4` headings |
| `_anchors_declared(stage_1_part_2.md)` | **21** | a strict subset of the 77 (claim-record citations, no heading labels) |
| `_reg_anchor_tokens` (nine registers) | **80** | the same **77** + `U.0`,`U.2`,`U.3` from `data_gaps.csv` transcription prose |
| `cited_reg − declared − reserved` | **U.1n, U.2n, U.2x** | the merge's own placeholder notation `U.1nn`/`U.2nn`/`U.2xx`, **not** ids |

**Declared set = the 77 anchors that actually have register rows** (`U.001`, `U.011`–`U.048` with
`U.002`–`U.010` reserved and uncited, `U.101`–`U.116`, `U.201`–`U.222`) **plus `U.0`, `U.2`, `U.3`** —
the three section labels the registers do cite, which must stay declared or every one of those register
cells becomes "a row citing an absent anchor". `U.1` and `U.4` are deliberately excluded: they are headings
no register cites, and declaring them would have re-created the exact finding. Written as
`<!-- ANCHORS: U.001, U.011-U.048, U.101-U.116, U.201-U.222, U.0, U.2, U.3 -->` at §U.0, with the rationale
as **prose outside the comment** — the parser tokenises everything between `ANCHORS:` and the first `-->`
and would silently add any `U.<digit>` written inside it (observed hazard, reported to the gate owner).
The expansion was checked to yield exactly **80 unique ids** before editing, and the anchor **headings were
not renamed**: §9.3's spine is intact and the declaration makes the collision inert.

**Guard tests required by the brief, both evaluated:**
- *Does the declared count go down?* **82 → 80**, and the two dropped members are **precisely the two
  heading labels the auditor proved were not anchors** (`U.1`, `U.4`). No three-digit anchor left the set:
  77 in, 77 out, plus the three echoed labels on both sides. So the decrease is the defect being removed,
  not coverage being lost — the list was **not** reverted.
- *Any "register row citing an anchor absent from the narrative"?* **No — zero, before and after**
  (`anchors | parity` now PASSes at **80 narrative ↔ 80 register**, and `citation resolution` PASSes at 85
  distinct ids resolving). Had I omitted `U.0`/`U.2`/`U.3`, this is exactly the over-narrow-allowlist failure
  mode that manufactured the 5×-larger defect an hour before this pass; it was pre-empted by deriving the set
  from the register scan instead of from the §U headings.
- *Findings:* `anchors` **2 → 0**. The residual one (`U.1n/U.2n/U.2x`) was cleared by **notation only**: the
  three placeholder patterns backticked in `data_gaps.csv` (46 tokens across 3 forms), the convention the
  gate already documents for ids being *discussed*. No value, id, row count (52×8 asserted) or word count
  (6,553 unchanged) moved.

**Residual, for the gate owner (tools/ untouched per brief):** `_reg_anchor_tokens` still scans **whole
register text**, so parity can still be held by an unrelated prose echo — a future `data_gaps.csv` edit that
drops the words "U.2" or "U.3" would manufacture findings here again, and the `--self-test` suite still has
no **must-stay-clean** control for a `### U.1` heading beside a genuine `U.011`. The auditor's tool-side fix
(scope `_anchors_declared` to the declared minting shape + plant that control) is the permanent one; this
pass made the volume honest to the gate, not the gate honest to the volume.

## CHR items

All three settled against held documents; no figure, no register value and no basis flag was altered, and
nothing was back-solved to make a total foot.

- **CHR-1 (Medium) — settled.** `## STAGE BOUNDARY JUSTIFICATION` row 1 no longer reads "1962
  *(documented)*": it reads "printed by the registrant from 1974-03-21; no in-period document carries it".
  §D **D-R02**'s Source cell was re-pointed — it credited "FY1972+ store/branch lists (A3/A4)", but
  `1962` prints **0 times** in `WALMART_AR_1972.txt` and `WALMART_AR_1973.txt` (re-grepped here) and **once**
  in `WALMART_AR_1974.txt`, so no FY1972 list can carry the event; the cell now names **S0103** with its
  printed date and splits confidence into **Medium (the print) / Low (the 1962 event)**. The auditor's
  instruction to leave D-R02's *existence* and the correction-beside-the-row pattern intact was followed.
- **CHR-2 (Medium) — settled, and the error was in the safe direction as the audit said.** §B.2 now reads
  **six** documents, earliest **S0103, printed 1974-03-21**, with S0103's founding sentence quoted
  ("…who opened his first Ben Franklin variety store in Newport, Arkansas in 1945.", verified in the
  `WALMART_AR_1974.txt` body, not in an intake header), the confidence cell moved from "from 1975 onward" to
  "**from 1974-03-21 onward**", and the source cell names the S0105 exclusion (Newport appears in
  `WALMART_AR_1976.txt` only inside a store list, and `1945` prints **0 times** there — the exclusion is
  right and was kept). §B-1a's arithmetic was repaired in place with the original wording visible:
  "then five more dated printings S0103→S0109" is annotated **corrected to six**, with the per-file `1945`
  counts (S0103/S0104/S0106/S0107/S0108/S0109 carry it; S0105 and S0102 do not — S0102 attests 1945 only by
  the "twenty-eight year history" back-cast). `conflicts.csv` **U.011** was normalised to agree:
  `claim_a_source`, `evidence_weight` and `why_they_differ` all said five / FY1975-onward and now say six /
  FY1974-onward. Independence remains **0** either way; the one-lineage finding is strengthened, not
  weakened.
- **CHR-3 (Low) — settled.** §A.1's FY1978 total-assets row now prints **both** S0108 clause forms and names
  which carries the perimeter: the short form (with the document's own `[sic] ot`, verified) and
  "**All financial information prior to 1979 has been restated…**" (verified in the `WALMART_AR_1979.txt`
  body; the file also prints a third occurrence of the same clause), and the row states that the restatement
  reaches **up to but not including FY1979**. The 206,691 / 251,865,000 two-live-bases values, the
  capital-lease move and the §P.0 forbidden-operation rule are unchanged.
- **Audit-sheet Low residue settled where documents allow:** §U.4's protected item **U.026** — the refuted
  FY1980 dividend row — **stays dead in the register**: `grep -i dividend quantitative.csv` returns only the
  contemporaneous FY1977 `0.085` (S0106) and FY1979 `0.22` (S0108) rows, and the refuted `$.09/$.11/$.19/$.25`
  set occurs **only inside retraction notes**. **CLOSED, no change.**
- **NOT settleable on held documents → UNKNOWN + named FETCH REQUEST:** **S0105's printed date**. The
  register carries publication `1976-03-26`, but no body line in `WALMART_AR_1976.txt` yields a March 1976
  day-month under any of the greps run here (only fiscal-year references), and the OCR of that file is
  degraded ("January 3 ]"). The value is therefore **kept as-is and labelled unverified** rather than
  adjusted: **FETCH REQUEST — `WALMART_AR_1976.txt` signature/auditor block, source page images (the auditor's
  report page and the President's message page) for `sources/periodicals/WALMART_AR_1976.txt`, to settle
  whether 1976-03-26 is printed or taken from an IA metadata sidecar.** Zero web budget on this pass, so the
  fetch is returned rather than attempted.
- **Partially settled, carried on:** the `.hocr` independence risk — **0** cells in `sources.csv` name an
  `_hocr` file, but **3** rows name the 1975/1976 annual-report artifacts at all, so whether any row treats
  the second OCR layer as a separate `source_id` is **UNRESOLVED** (see UNTRIED).

## Gate before and after

Command (identical both runs): `python tools/gates.py --company-dir founders_playbook/01_companies/company_002_walmart --checks csv,keys,anchors,budget,corrections`

**BEFORE** (first act of this pass, after claiming):

```
Findings: **2** | Passes: 19
| anchors | citation resolution | 3 REGISTER row(s) cite a §U entry that is never declared: U.1n, U.2n, U.2x |
| anchors | narrative | anchor with no register row: U.1, U.4 |
- coverage 9 registers, 3 stage volumes, 20 source documents
- anchors  stage_1.md declares 82 anchors
- anchors  stage_1_part_2.md declares 21 anchors
- anchors  21 id(s) read as backticked references or range endpoints, not citations (U.0, U.001, U.011, ...)
- anchors  2 prose mention(s) match no declared entry, ADVISORY only: U.002, U.010
- corrections no CORRECTIONS.md -- gate DID NOT RUN (not a pass)
csv/keys/budget passes: timeline 59x11, quantitative 114x12, conflicts 39x15, sources 47x18, data_gaps 52x8,
  validation 0x11, failures 13x11, decisions 9x15, channels 0x11; keys 36 + 4 tokens resolve;
  budget stage_1.md 57991 / stage_1_index.md 501 / stage_1_part_2.md 7132 (cap 60000)
```

**AFTER** (all repairs applied):

```
Findings: **0** | Passes: 22
- coverage 9 registers, 3 stage volumes, 20 source documents
- anchors  stage_1.md declares an explicit ANCHORS set (80 ids)
- anchors  stage_1.md declares 80 anchors
- anchors  stage_1_part_2.md declares 21 anchors
- anchors  32 id(s) read as backticked references or range endpoints, not citations (...)
- corrections 2 retraction ids; register layer reaches 2, volumes 2
anchors  citation resolution   every register-cited anchor resolves (85 distinct ids across registers and volumes)
anchors  parity                80 narrative anchors <-> 80 register anchors
corrections propagation        all 2 retraction(s) reach registers and volumes
csv  all nine registers unchanged in shape: 59x11, 114x12, 39x15, 47x18, 52x8, 0x11, 13x11, 9x15, 0x11,
     source_id tokens all resolving
keys stage_1.md 36 / stage_1_part_2.md 4 source tokens all resolve
budget stage_1.md 58841 words (cap 60000, amber) / stage_1_index.md 591 / stage_1_part_2.md 7132
```

Net: **findings 2 → 0, passes 19 → 22** (the two `anchors` failures cleared and `corrections` converted from
"did not run" to a pass). Nothing reached the 60,000 hard cap, so no split was triggered; the volume is amber
by design and no evidence was cut to stay under it (§9.6).

## Residue

**Files written by this pass** (nothing else touched; no delete, move or rename; no git):
`stage_1.md` (identity line, assembly note, §U.0 declaration + rationale, §A.1 SFAS row, §B-1a arithmetic,
§B.2 Newport row, §D-R02 row), `conflicts.csv` (3 cells of U.011, U.013 note, U.014 note), `data_gaps.csv`
(46 placeholder tokens backticked), `CORRECTIONS.md` (created: COR-301, COR-302 + propagation table),
`_MANIFEST.md` (counts re-raised; items 1, 3, 5 dispositioned; CORRECTIONS.md row added), `stage_1_index.md`
(word counts, non-destruction arithmetic, declared-anchor-set bullet), `03_quality_control/walmart_s1_merge.md`
(append-only dated correction), and this sheet.
**Rows/cells changed: 10 register cells across 2 CSVs** (5 conflicts, 46 placeholder tokens in data_gaps =
1 cell-pattern group), **0 rows added, 0 removed, 0 re-keyed, 0 values altered**; column and row counts
asserted by the applying script.

**Not fixed, deliberately:** `_parts/` (protected audit trail — no `SUPERSEDED` line was applicable, because
no part text was contradicted *in situ*; the contradiction lives in the merged volume's header and in
`CORRECTIONS.md`, which `_parts/s1_p1.md`'s status banner does not carry. If the certifier wants the parts to
speak, the line to add is `SUPERSEDED 2026-09-26: identity-line claims withdrawn per COR-301/COR-302` —
**not applied by me**, since `_parts/` is outside my write set for content edits).

**UNTRIED at budget stop** (nothing skipped for convenience; every one named, none silently dropped):
1. `sources.csv` — whether any row treats the AR_1975/AR_1976 `.hocr` second OCR layer as its own `source_id`
   (0 filename hits, 3 artifact-name hits; needs the url/path cell read).
2. **S0105 `1976-03-26`** — FETCH REQUEST above; unverifiable from the text layer on disk.
3. The `first SEC-visible registration` label's continued death in the registers (§U.4's other protected item).
4. `budget` at tier-exemplar vs the tier actually assigned to this company (§15.2), and whether this volume's
   **amber 58,841 words** leaves enough headroom for the next repair pass — it is within ~1,150 words of the
   hard cap, so a future header expansion must split, not trim.
5. Row-for-row equivalence of `stage_1_part_2.md`'s kept handoff blocks against the live registers (the merge
   sheet's own UNTRIED item, still open).
6. Any re-key of inbound pointers **into** `stage_1.md` from other companies' files (§14 rule 12) — none
   attempted; no other company directory was opened.

**Observations for the gate/tool owner (reported, `tools/` not edited):**
(a) confirmed hazard in `declared_anchors`: any `U.<digit>` written inside the declaration comment — including
in explanatory prose — is silently **added** to the authoritative set; the rationale text must stay outside
the comment. (b) `_reg_anchor_tokens` still scans whole register text, so parity can be held by an unrelated
prose echo, and `--self-test` still has **no must-stay-clean control** for a `### U.1` heading beside a real
`U.011` (§15.5: a gate that cannot catch its own historical defect). (c) **`scaffold.py section` is broken in two live ways, and the second corrupted this sheet before I
repaired it.** `cmd_section` stamps a block only if the block still contains the tool's own unwritten-section
placeholder, so once an agent has written the section's content the §15.3 WRITE-line marking is
**impossible**: six of this sheet's seven `section` calls returned "NOT STAMPED: no section heading equals …
exactly / Existing headings that merely start with it: none", although all seven headings exist verbatim (see
the file's own `## ` lines). The heading comparison is exact and correct; the **silent extra condition
`and placeholder in block`** is what refuses, and the message never says so. Second: the stamp is a
**whole-block string replace**, so the one call that reported success (`Residue`) had not marked a section —
it had rewritten a placeholder string I was **quoting as evidence** inside my description of that very
defect, converting a quotation into a false `WRITTEN` stamp and then reporting a word count. This sheet
therefore carries **no trustworthy per-section markers**; the ledger record and this paragraph are the status
evidence, and the ledger `done` line is the only thing a reader should rely on. Tool fixes needed: locate by
heading and insert the stamp under it when no placeholder remains; anchor any placeholder replacement to the
line (`(?m)^STATUS: PENDING$`); name the real refusal reason. The auditor's interim guidance ("never put the
literal placeholder string in quoted evidence") is confirmed necessary but is **not** a fix — the trap stays
armed for the next agent, and I only caught it by diffing the word count before and after.
(d) the `quotes` gate remains **ADVISORY** at this company and was not run on this pass.

**For the certifier:** HDR-1/HDR-2 are repaired with carriers named and mechanically propagated; the anchor
namespace is now declared rather than guessed, with the over-narrow-allowlist guard tested explicitly;
CHR-1/2/3 and the two settleable Low items are closed; one Low item is UNKNOWN with a named FETCH REQUEST.
What this pass could **not** certify is unchanged from AUDIT 1's own boundary: HND-1's unread §§E–L, N–R prose
(line-by-line hindsight coverage), and independence judgment on the newly quoted S0103 sentence — which is one
more printing inside the **same** lineage, so the independent count stays **0** and must not be read as
corroboration.

