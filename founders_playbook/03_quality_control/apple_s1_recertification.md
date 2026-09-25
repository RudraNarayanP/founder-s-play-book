# apple_s1_recertification.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T21:06:18Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## Verdict

**CERTIFIED.** No blockers. The repair pass is verified against the document, not against its own
sheet: I am a fresh certifier, I wrote no part of the volume, the audit, or the repairs, and every
claim below was re-checked against bytes on disk.

1. The G1-A boundary repair is a real repair, not a rewording (§Retraction integrity, item COR-01):
   the §Q row now carries the straddle range, the inverted parenthetical is deleted from both
   volumes (0 occurrences of `last document before the edge` in `stage_1.md` and
   `stage_1_part_2.md`), and the withdrawn label survives only where it should — quoted inside its
   own retraction and verbatim in `_parts/s1_p3.md` under an appended SUPERSEDED marker.
2. The restated count **reproduces from the cells it summarises, by two independent methods I
   re-ran myself** (§Count reproduced): 17 wholly in-window + 1 boundary event + 1 straddle.
3. All five COR-01…05 retractions reach narrative, index, registers, volume-2 echoes and marked
   `_parts/` trails (§Retraction integrity).
4. The BYTE tier split is per-item, confidence untouched, and the reasoning holds against the
   actual records (§BYTE tiering).
5. All mandated open items are still open and labelled; `$666.66` literal-string returns **0 hits
   across the 61 files under `sources/`** (§Open items held).
6. Gates re-run today: 0 findings / 20 passes, `corrections` demonstrably ran; `--self-test` PASS.
   The old "volume 2 is invisible to the gates" claim is **false under the current build**, proven
   against `tools/gates.py` source, not against a prior agent's report (§Gate gaps).

Both handed-over residues were tested: G1-F is **partly closable by inspection, open in the part
that matters**; the S1P1 upgrade queue is **genuinely open and correctly parked** in the index
hand-off (§Tolerable).

STATUS: WRITTEN 2026-09-25

## Retraction integrity

The `corrections` gate now enforces prose-vs-register reach. **It ran, and I confirmed running
rather than assumed:** today's live output prints `corrections 5 retraction ids; register layer
reaches 5, volumes 5` and the pass line `corrections propagation  all 5 retraction(s) reach
registers and volumes`; `--self-test` catches the planted "retraction never reaches the registers"
defect and holds the "propagated retraction must stay clean" negative control. Given the project's
two silent-non-run incidents (RD-114's own history of a gate wired only into the harness), the
printed line is the evidence, not the sheet's claim. Layer-by-layer verification, each id:

- **COR-01** — narrative: §Q row now `1976-12-10 → 1977-01-19 | Straddles the edge (1976-12-10
  in-window; 1977-01-19 far side)`, event cell names the superseded label and says `hcc0213` is the
  **first document past** the edge; the §Q preamble carries COR-04+COR-01 vocabulary; record
  S1P3-10 prints the withdrawal of "twenty dated rows" with the re-measurement. Registers: the
  `timeline.csv`, `quantitative.csv` and `failures.csv` U.021 rows all open `STRADDLES THE EDGE`
  and name COR-01 (verified in `stage_1_part_2.md`'s quoted register echoes and in
  `research/timeline.csv` cell `1976-12-10/1977-01-19`). Trail: `_parts/s1_p3.md` carries an
  appended SUPERSEDED marker (line ~718) and keeps the withdrawn label **un-erased** (2 occurrences)
  — marked, not rewritten. This is a repair that matches the document, not the prose.
- **COR-02** — registers: `sources.csv` A2S-02/03/05/08/13 carry the split cell
  `1 (printed commercial artifacts) / 3 (the magazine's own prose)`; A2S-09 is outright `tier: 3`;
  A2S-01/04/06/07/10/11/12 and S1M-07/08 stay Tier 1. Volumes: §Boundary adopted row reads
  "a **Tier-1 registrant filing** and an **independent Tier-3 trade column**"; `Tier: 3` occurs 15×
  in vol 1; vol 2's U.001 `evidence_weight` echo carries the same wording (verified verbatim).
  Trail: `_parts/s1_p2.md` marker for S1P2-14/15; S1P1-13 record checked directly.
- **COR-03** — records S1P1-05/06 now read "three months past the adopted stage edge" / "five to
  six months past", with `Source date: 1977-04` and `1977-06` present; `conflicts.csv` U.019 carries
  the COR-03 merge-action note, its vol-2 echo too; instruction layer reached — §Boundary, §M.4 and
  the `stage_1_index.md` hand-off note all updated; `_parts/s1_p1.md` carries an appended marker and
  CLAIM A survives **unchanged** in the part. U.019 remains two-sided (verified in the register row).
- **COR-04** — exactly **7** `timeline.csv` rows open `POST-EDGE (window closes 1977-01-03)`
  (counted, not asserted); the §Q preamble prints the convention; no fifth stage literal exists
  (every row still `stage1` — the csv gate's stage-vocabulary check passes over all 9 registers).
- **COR-05** — `RETROSPECTIVE SOURCE (1977-04)` at §H.2 (stage_1.md line 579 region) and in
  **2** `timeline.csv` rows for the 1976-11-20 sighting; class deliberately not reclassified, with
  the negative-knowability reason printed in CORRECTIONS.md.

Index reach: `stage_1_index.md` carries the repair note naming COR-01…COR-05 and the post-repair
word counts — the RD-110 failure mode (header/instruction files still teaching withdrawn text) is
closed here: no header, manifest or index line re-teaches any struck reading.

STATUS: WRITTEN 2026-09-25

## Count reproduced

**It reproduces — 17 + 1 + 1 — and I re-derived it myself, twice, without using the repair pass's
arithmetic.** Method and numbers:

1. **§Q Window-status column.** I extracted the date and status cells of every `|`-row between
   `## Q.` and `## R.` myself: 25 data rows. Labels as printed: **17** `In-window` (including the
   qualified milieu / start-edge / null / contested variants), **1** `Window end` (1977-01-03),
   **1** `Straddles the edge` (1976-12-10 → 1977-01-19), **5** `Far side`, **1** `Out of window`
   (1980-12 → 1981-02). That is S1P3-10's restated form exactly: seventeen wholly in-window plus
   the boundary event (eighteen in-window dates) plus one straddle.
2. **`research/timeline.csv` parsed with the csv module** (not by hand-splitting on commas, per the
   mechanical-discipline warning). 28 rows carry `stage1` of 30 total; **19** have a first date
   ≤ 1977-01-03; removing the 1977-01-03 boundary row and the `1976-12-10/1977-01-19` straddle row
   leaves **17 wholly in-window**. The two layers agree, and S1P3-10 prints both recipes plus the
   census caveat (id-pattern counting silently drops single-digit §P ids: 23-of-32 on `[A-T]\d{2}`
   versus 32 on `[A-T]\d{1,3}`), which I confirmed is the right warning since the §P ids run P1–P32.

One honest wobble, recorded so nobody "repairs" it: the §Q rows and the timeline rows are not a
one-to-one mapping (the timeline holds two 1976-11-20 rows and no row for §Q's 1975-11 → 1977-01
null row, which is in-window). The totals coincide at 17, which is what the claim asserts; the
claim is a count of rows-by-status in each layer, and that is reproducible in both.

The retracted "twenty" was unreachable even as printed pre-repair (18 in-window labels + 1
window-end = 19) — the repair sheet says so, the record prints so, and the audit sheet's own
"18, or 19 counting the boundary event" correction is reproduced in S1P3-10's measurement cell.
Whichever total had been right, the defect was un-reproducibility; it is gone.

STATUS: WRITTEN 2026-09-25

## BYTE tiering

I tested the tiering against the actual records, in both failure directions.

**Register cells, read directly from `research/sources.csv`:** A2S-09 = `tier: 3` outright;
A2S-02, A2S-03, A2S-05, A2S-08, A2S-13 carry the split `1 (printed commercial artifacts) / 3 (the
magazine's own prose)` with the per-item rule and COR-02 named in-cell; A2S-01, A2S-04, A2S-06,
A2S-07, A2S-10, A2S-11, A2S-12, S1M-07, S1M-08 stay Tier 1.

**Not applied too widely.** No confidence cell moved with the tier: A2S-09 is `tier: 3 / conf: High`
and A2S-08 stays `Medium` — correct, because under §3 confidence scales on witnesses and lineage,
not rank: the end-edge **year** has two unrelated origins (the FY1994 10-K plus the 1981 column),
the **day** rests on the filing alone and is still printed Medium, and U.023 still caps the
FY1978–FY1980 series at one witness. A tier change that also cut confidence would have been the
quiet evidence-deletion the brief warns about; it was not done. The April 1977 store-directory page
retains Tier 1 *as a printed commercial artifact* while the same row states in-cell that the
directory "is NOT a sales channel" and repeats §H.3's warning — rank and reading are separated, and
U.008 keeps the directory/order-form vs word-of-mouth tension fully two-sided (`best_supported`:
"The tension is the finding"). First-party matter (Apple's own June/July 1977 ads, Wozniak's bylined
May 1977 description, named dealers' ads) staying Tier 1 regardless of carrier is exactly the audit's
own concession, and absence censuses taking the rank of the corpus searched is defensible under §5's
"contemporaneous statistics" clause.

**Not applied too narrowly.** The unsigned retrospective column that did the most documentary work —
the February 1981 "Apple Stock Goes On Sale" — is Tier 3 both in the register and in every narrative
record that rests on it (S1P1-13, S1P1-21, S1P1-24, S1P2-14, S1P2-15; `Tier: 3` appears 15× in
volume 1), and the §Boundary adopted row — the sentence the audit quoted as "Two Tier-1 documents" —
now reads "a Tier-1 registrant filing and an independent Tier-3 trade column". Retrospective print no
longer carries documentary rank anywhere I looked.

**Residual, honestly declared:** the volume-wide `Tier: 1` token count (46 pre-repair) was swept by
carrier and never re-censused as a number; a straggler Tier-1 token on a magazine-prose carrier could
survive outside the ten records named. I spot-checked the named carriers and the §Boundary/§T/§Q
rows and found none, but the census is the scripted job, and the repair sheet says so itself.

STATUS: WRITTEN 2026-09-25

## Open items held

**Nothing was resolved by preference.** Verified against the records today:

- **The five live conflicts are live and two-sided.** `research/conflicts.csv` U.003 (50 boards at
  $500), U.005 (Wayne 10%-vs-12%), U.007 (Markkula's terms), U.008 (word-of-mouth vs the April 1977
  BYTE directory and June-July 1977 order form), U.009 ($77,000-vs-$770,000) each carry a non-empty
  `residual_uncertainty` naming the document that could close it, and a `best_supported_interpretation`
  that adjudicates by scoping, not by choosing ("10% and eleven days are the best-supported figures,
  **not veri**fied"; "Terms UNKNOWN and entry date UNKNOWN"; "First order UNKNOWN"; revenue UNKNOWN
  with reason). The bar on averaging — "no average of 10 and 12 may be printed" — survives ("no
  average" x3 in volume 1); no averaging occurs anywhere I checked.
- **The 1994-01-26 EDGAR floor** is intact and load-bearing (13 occurrences in volume 1; restated in
  CORRECTIONS.md standing positions and the index's preserved-positions block).
- **`$666.66` stays a verified zero.** `find sources -type f | wc -l` = **61**; a **fixed-string**
  grep for `666.66` returns **0 files**. (A plain-regex grep returns one file —
  `byte-1976-04.txt` line 5229, OCR noise `666666` — which is a dot-matches-anywhere artifact, not a
  hit, and worth recording so a later pass does not "discover" a contradiction.) The only
  dollar-shaped 666 remains the IMSAI decoy, and the position remains FOUNDER CLAIM / UNKNOWN, never
  FACT, exactly as the audit left it.
- **Retraction-shaped temptations were declined.** U.019 still prints CLAIM A (the interrupted
  pass's in-window reading) verbatim with a residual sentence saying a later adopted edge would make
  it correct; U.021's silence is still "report the silences, price them, and draw nothing from them";
  the `S1P2-CF-01…05` rows stay refused-and-re-pointed, not force-merged.

**The two handed-over residues, adjudicated as instructed:**

1. **G1-F (`sources/test_direct.txt` vs the "twelve cached BYTE 1976 issues" denominator): partly
   closed by inspection, genuinely open where it matters.** The denominator itself is clean:
   `sources/ia_byte_1976/` contains exactly **12** files, `byte-1976-01.txt` … `byte-1976-12.txt`,
   and `test_direct.txt` sits at the `sources/` root, outside the run directory — the printed
   "twelve cached 1976 BYTE issues" (stage_1.md §T preamble) is reproducible and is not thirteen.
   What remains open is the *hit-count scope*: `sources.csv` S1M-08's note cell records only
   "Anchor U.030; the pivotal negative of sections M and N" and does not say whether its exhaustive
   token census globbed the run directory or all of `sources/` recursively (a recursive census would
   double-count the duplicated 1976-09 ad block). Only a scripted re-run settles that, per §15.1;
   the pass correctly did not prune the protected archive. **Open, Low, correctly labelled.**
2. **The nine S1P1 records awaiting the merge-side `Source`/`Tier`/`Conf` upgrade: genuinely open,
   not closed.** S1P1-01/02/03 still print `Source: UNKNOWN (carrier not…)`-era cells, and the
   upgrade is parked where a cold reader will find it: the `stage_1_index.md` NOT-APPLIED hand-off
   names it "for the audit pass" and points at `apple_s1_merge.md`; the repair pass states it left
   them deliberately (scope discipline) and that when run, its Tier cells must follow COR-02's
   per-item rule. **Open, correctly registered.** Nit: the repair sheet's own label "nine" enumerates
   `S1P1-01…04, 07…12, 30 etc.` — eleven-plus labels — a count in a QC sheet that does not reproduce
   from its own enumeration; the index's authoritative set is `S1P1-01…11`. Cosmetic, in a file this
   certifier does not own; recorded, not repaired.

STATUS: WRITTEN 2026-09-25

## Blockers

**None. Zero.** No file + stable-label citation can be offered against the repaired volume at the
blocker threshold. Gates quoted as run today, per the mechanical-discipline instruction, both
executed by me and neither re-derived by hand:

`python tools/gates.py --company-dir founders_playbook/01_companies/company_004_apple --checks csv,keys,anchors,budget,corrections`

```
Findings: **0** | Passes: 20
coverage     9 registers, 3 stage volumes, 41 source documents
keys         stage_1.md cites 2 hyphenated record keys: S1M-01, S1M-10
keys         stage_1_index.md cites 4 hyphenated record keys: S1M-01, S1M-02, S1M-09, S1M-10
anchors      stage_1.md declares 55 anchors
anchors      7 id(s) read as backticked references or range endpoints, not citations (U.005, U.009, U.012, U.013, U.025, U.037, U.054)
anchors      2 prose mention(s) match no declared entry, ADVISORY only: U.112, U.113
corrections  5 retraction ids; register layer reaches 5, volumes 5
csv      timeline 30x11 · quantitative 44x12 · conflicts 38x15 · sources 23x18 · data_gaps 35x8
         validation 6x11 · failures 6x11 · decisions 4x15 · channels 0x11 (header only)
anchors  citation resolution  every register-cited anchor resolves (57 distinct ids across registers and volumes)
anchors  parity  55 narrative anchors <-> 55 register anchors
budget   stage_1.md 57502 (cap 60000) · stage_1_index.md 1517 · stage_1_part_2.md 8834
corrections propagation  all 5 retraction(s) reach registers and volumes
```

`python tools/gates.py --self-test`

```
anchor with no register row                  [anchors]     CAUGHT
backticked anchor id stays clean             [neg]         STAYS CLEAN
cited anchor matches no declaration          [anchors]     CAUGHT
correctly escaped doublequote must stay clean [neg]        STAYS CLEAN
dangling source_id                           [csv]         CAUGHT
duplicate record id                          [csv]         CAUGHT
numeric stage vocabulary                     [csv]         CAUGHT
paraphrase presented as quote                [quotes]      CAUGHT
propagated retraction must stay clean        [neg]         STAYS CLEAN
retraction never reaches the registers       [corrections] CAUGHT
row with wrong column count                  [csv]         CAUGHT
unquoted comma shifts fields                 [csv]         CAUGHT
unresolvable source token in narrative       [keys]        CAUGHT
clean fixture                                CLEAN
self-test: PASS
```

Word counts in the brief (57,502 + 8,834) and the index's post-repair note match the gate output
exactly; widths match the repair sheet's AFTER run row for row. Volume 1 at 95.8% of the 60k cap is
amber (§9.2), not a defect, and §9.6 geometry holds.

STATUS: WRITTEN 2026-09-25

## Tolerable

Recorded, below blocker weight, none requiring another repair pass before certification:

1. **`Tier: 1` residual count not re-censused** after COR-02 (46 pre-repair, swept by carrier). A
   straggler token on a magazine-prose carrier outside the ten named records would be cosmetic; the
   census is §15.1 scripted work. `stage_1.md` §T, S1P1/S1P2 records checked where load-bearing.
2. **A2S-05 still carries two items in one row** (`event_date 1976-11-20; 1977-04`) with a split tier
   cell. The clean fix is a second `source_id` — a §9.4 append-only restructure with central id
   assignment, above a repair pass. Genuinely open, correctly parked (repair sheet residue 3).
3. **The repair sheet's "nine" S1P1 records enumerates eleven-plus labels** (`01…04, 07…12, 30
   etc.`); the index's authoritative hand-off set is `S1P1-01…11`. A QC-sheet count that does not
   reproduce its own enumeration is the RD-110 shape in miniature — but it is in a sheet its author
   owns, not in a volume, register, or instruction file, so it is a nit for that owner, not a
   defect of the document under certification.
4. **The 1980-12 cap-table row's `stage1`-vs-`stage2` semantic split** is left as a recorded decision
   in the manifest, both halves now tier-noted. A decision, not drift.
5. **Advisories, not defects:** `U.112/U.113` prose mentions match no declared entry (advisory-only
   line, correctly labelled); the 7 ids read as backticked references rather than citations are the
   protected-history class the anchors gate deliberately exempts.
6. **`_parts/s1_p3.md` keeps the withdrawn `last document before the edge` label verbatim (2
   occurrences)** — that is the audit trail doing its job under §14 rule 4: marked, never rewritten.
   Not residue; design.
7. **`sources/test_direct.txt` still sits in the protected archive** (G1-F). §14 rule 4 forbids this
   certifier — and the repairer — from pruning it; its disposition is an intake decision for the
   scripted census re-run.

STATUS: WRITTEN 2026-09-25

## Gate gaps

**First, the gate myth, retired against code, not against a report.** "Volume 2 is invisible to the
`anchors`/`keys` gates" was true of an earlier build and is **false today**: `tools/gates.py` line
44 lists `stage_1_part_*.md` under `NARR_GLOBS["stage1"]`; `narr_files()` (line 105) globs those
across the company dir, `research/` and `_parts/`; `gate_anchors()` iterates `narr_files()` and
`gate_keys()` iterates `stage_docs()` (line 191), whose `stage_*.md` glob matches
`stage_1_part_2.md`. The run confirms it: `coverage 3 stage volumes`, budget lines for all three,
and `citation resolution 57 distinct ids across registers and volumes`. Volume 2 showing no declared
anchors and no keys line is **correct behaviour for the appendix volume** — it legitimately declares
zero §U entries, and its register echoes' citations are the 57 that resolve. The repair sheet's
residue 1 restates the superseded claim; it should be struck from any future brief.

What the gates structurally cannot see, and where I covered it by hand:

1. **Values inside well-formed cells.** G1-A was a wrong label in a correct column; no csv check can
   see a misclassified Window-status. The count reproduction is likewise semantic — done by me,
   twice, outside the gates.
2. **Two-sidedness.** All 38 `conflicts.csv` rows pass width while nothing checks that `claim_a` and
   `claim_b` genuinely oppose or that `residual_uncertainty` is a residual; I read the five live
   rows.
3. **Tier and independence semantics.** The tier cells pass as strings; per-item correctness was my
   read, and the `keys`/`csv` layers only resolve ids.
4. **Volumes vs `sources/` bytes.** No check compares a quotation to the held file in a scripted
   run; the `quotes` gate exists (and self-catches paraphrase-as-quote) but was not among the five
   directed checks, so verbatim existence for the repair pass's new quotes is unmechanised — the
   audit's eleven hand-verifications still stand as the last full pass.
5. **`_parts/` trail reach.** `corrections` enforces registers+volumes only; the three SUPERSEDED
   markers and the two instruction-layer spots (§Boundary cost, §M.4) were verified by me, not by
   the gate.
6. **Denominators and durations.** "Twelve cached issues", the 17/1/1 totals, "eleven days", "nine
   months" — pure prose to a script; the 61-file census was my `find`/`grep -F`.
7. **UNTRIED at my stop line** (chosen scope, zero web): I did not read §B.1–B.5, §C.1–C.3,
   §E.1/E.3/E.6, §F.2–F.4, §G.1–G.3/G.5/G.6, §I.1–I.5, §J.1–J.4, §K.2–K.6, §L.1/L.2, §O.1–O.3
   line-by-line; did not recompute `derived_arithmetic` across the 44 quantitative rows or test
   `what_it_did_not_demonstrate` smuggling in `validation.csv`. Those were the audit's and the
   repairer's UNTRIED list too; a full-coverage read pass remains unclaimed by any check.

STATUS: WRITTEN 2026-09-25

