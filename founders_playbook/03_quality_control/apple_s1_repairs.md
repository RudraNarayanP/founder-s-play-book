# apple_s1_repairs.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T20:50:45Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## Q boundary drift

STATUS: WRITTEN 2026-09-25

**G1-A settled (High).** §Q's Homebrew row read `1977-01-19 | In-window (last document before the edge)`. Replaced with the straddle form used by every other carrier of the same fact (§A, §D, S1P1-29, §P row P32, the U.021 register rows): date cell now `1976-12-10 → 1977-01-19`, window status now **Straddles the edge (1976-12-10 in-window; 1977-01-19 far side)**, and the event cell states the ordering the old label inverted — `hcc0213` is the **first document past** the adopted 1977-01-03 edge, not the last before it, and the row now says so and names the superseded label. The "last document before the edge" parenthetical is deleted. Row count of the table is unchanged (25 rows), anchor `U.021` unchanged, so §U anchor parity is untouched.

**Register layer (rule 10).** The defect was merge-presentation only — `research/timeline.csv` already held `1976-12-10/1977-01-19` — so no date cell needed repair, but the register carried no marker either. Now tagged:
- `timeline.csv` U.021 row: notes open `STRADDLES THE EDGE (1976-12-10 in-window; 1977-01-19 far side)` and name **COR-01**.
- `quantitative.csv` U.021 row: notes carry the same COR-01 pointer.
- `failures.csv` U.021 row: same.
Volume layer: the §Q row itself, the §Q preamble, and record **S1P3-10** all carry COR-01, so the retraction reaches prose and registers together.

**G1-E settled at the same time (was Low; register-only).** Seven `stage1` `timeline.csv` rows dated past the edge carried no out-of-window marker (`1977-02-16`, `1977-04`, `1977-04-15/17`, two rows at `1977-05`, `1977-06`, `1977-07`); each now opens `POST-EDGE (window closes 1977-01-03)` (**COR-04**). The `1977-04` row's note also stopped saying the store directory is channel evidence "for Stage 1": it now reads "…for the Stage-1 product, printed three months after the edge and never used as Stage-1 state". No fifth stage literal was invented — §13's four literals are untouched and every row is still `stage1`.

## Row count re-measure

STATUS: WRITTEN 2026-09-25

**G1-B settled, and the audit's own arithmetic was one out.** S1P3-10's "twenty dated rows inside the window" is **retracted** (COR-01) and restated as: **17 dated rows wholly inside the window + the boundary event of 1977-01-03 = 18 in-window dates, plus 1 row straddling the edge.** The `Date:` span is closed at **1977-01-03** (it previously ended on the post-edge 1977-01-19). The substantive half of the claim survives untouched and is still printed: **no in-window row is an Apple-side document.**

**What I counted, and how.** Two independent measures, recorded inside the record so a reader can re-run them without me:
1. **§Q table cells.** All 25 data rows of the spine read one by one by their Window-status column: 17 labelled in-window (incl. the qualified "milieu", "start edge", "null", "contested"), 1 window-end, 1 straddle after the fix, 5 far side, 1 out of window. **The "twenty" was unreachable even as printed:** the printed column offered 18 in-window labels (the 17 plus the mislabelled `1977-01-19`) + 1 window-end = **19**. The audit's note that removing G1-A leaves "18, or 19 counting the boundary event" is right on the second form and one high on the first — removing the mislabel leaves **17** in-window labels, because the corrected row is a straddle row, not an in-window row; its in-window half (1976-12-10) already has its own row.
2. **`research/timeline.csv` parsed cell by cell.** **19** rows carry `stage1` with a first date ≤ 1977-01-03; one of those is the boundary event and one straddles the edge → **17 wholly in-window**, exactly the number measure 1 returns. The two layers agree, which is why the restated figure is High and not Medium.

**Census caveat, applied rather than recited.** Counting by record-id pattern is the trap here: the §P metric ids run **P1–P32** and a two-digit pattern `[A-T]\d{2}` returns only **23** of them, silently dropping the nine single-digit ids, where `[A-T]\d{1,3}` returns **32**. Appendix keys run past two digits too (S1P1-05 … S1P3-15). The restated count therefore counts table cells and register date fields, never id-pattern hits, and S1P3-10 prints that instruction so the next pass does not re-derive "twenty" from a regex.

## BYTE re-tiering

STATUS: WRITTEN 2026-09-25

**G1-D settled per item, not globally.** The volume-wide claim was that every BYTE row is Tier 1; §5 ranks trade publications Tier 3. The rule I minted and printed in `research/sources.csv` + `CORRECTIONS.md` (COR-02) separates **what the item is** from **who printed it**:

* **Tier 3** — A2S-09 outright (the unsigned February 1981 column "Apple Stock Goes On Sale"), and the magazine's own column prose inside A2S-05 (Helmers' April 1977 piece, the sole carrier of the 1976-11-20 demonstration).
* **Tier 1 retained** — first-party and documentary matter regardless of carrier: Apple's June/July 1977 advertisements (A2S-07, A2S-08's ad pages), Wozniak's bylined May 1977 description (A2S-06), named dealers' own advertisements (A2S-04), the **April 1977 store-directory page**, and documented-absence censuses, whose rank is the rank of the corpus searched (A2S-01, S1M-08).
* **Mixed rows now carry a split value** rather than a flattened number: `1 (printed commercial artifacts) / 3 (the magazine's own prose)` on A2S-02, A2S-03, A2S-05, A2S-08, A2S-13. A2S-05's row spells out both halves and repeats §H.3's warning that the directory is the magazine's own advertising inventory, not somebody's sales channel.

**Narrative layer.** The §Boundary adopted row now reads "a **Tier-1 registrant filing** and an **independent Tier-3 trade column**" instead of "Two Tier-1 documents"; U.001's `EVIDENCE WEIGHT` says the same in §U; the five records resting on the 1981 column (S1P1-13, S1P1-21, S1P1-24, S1P2-14, S1P2-15) print Tier 3, each with the reason in-cell; S1P3-10's tier cell now distinguishes the spine's in-window carriers from its far-side magazine prose. `independence_note` text updated on A2S-01, A2S-05, A2S-09; `conflicts.csv` U.001 `evidence_weight` rewritten, and its verbatim echo in `stage_1_part_2.md`'s register block carried along so the volume and the register cannot disagree.

**What I did not do.** No confidence, lineage or independence value moved: independence was already satisfied (different author, publisher, decade), the end edge's **year** still stands on the filing with a genuine second origin, **U.023** still caps the FY1978–FY1980 series at one witness, and the day remains Medium on a single document. No global demotion of periodical print: on this corpus the demotion of magazine prose is not evidence that the channel was thinner than the memoir says, and **U.008 keeps the directory / order-form vs word-of-mouth tension as a live two-sided finding** — S1P1-06 now says in terms that the tension is the finding, not an error to smooth away. The 46 `Tier: 1` narrative tokens were swept by carrier, not by count: only rows whose load-bearing item is the magazine's own prose changed, and the absence-census rows stayed because their rank is the rank of what was searched.

## S1P1-05 and 06

STATUS: WRITTEN 2026-09-25

**G1-C settled as a narrow correction of the citable atom, as the audit scoped it.** Both records said "inside the window" with `Source date: UNKNOWN`:

* **S1P1-05** → the April 1977 directory is "three months past the adopted stage edge … a **post-window witness to the channel the window's product entered**, not Stage-1 state"; `Source date: 1977-04`; carrier named (A2S-05, byte April 1977 directory page); Tier cell states the per-item rule; `Conflicts:` now points at the keys that actually own the subjects — **U.008** for channel character, **U.019** for labelling.
* **S1P1-06** → the June/July 1977 order form is "five to six months past the adopted stage edge … the maker's own printed commercial voice, the first such artifact in the corpus"; `Source date: 1977-06 / 1977-07`; carrier named (A2S-07/A2S-08) and kept **Tier 1**, because Apple's own advertisement is first-party matter whatever magazine carried it.
* Left alone deliberately: both records' `Conf: Low (pending line read)`, their `Class`, and the other nine S1P1 records awaiting the merge's Source/Tier/Conf upgrade. Scope discipline, not oversight — the audit's remedy was window status plus source date, and upgrading confidence cells is the merge's stated job.

**Two-sidedness preserved, not smoothed.** U.019's CLAIM A still prints the interrupted pass's in-window reading as written, CLAIM B the defended boundary, and the residual sentence still says a later adopted Stage-1 end would make the old records correct. Reach: `conflicts.csv` U.019 (`best_supported_interpretation`, + the part_2 echo) carries **COR-03**, and the three instruction-layer spots that told readers the defect was *unrepaired* were updated in the same pass — §Boundary cost, §M.4 item 5, and the S1P1-01…11 hand-off note.

## Sibling sweeps

STATUS: WRITTEN 2026-09-25

**Settled from held documents.** G1-E (Low) → **COR-04**: seven post-edge `stage1` timeline rows marked, the "for Stage 1" phrase on the April 1977 directory row rewritten, the straddle row marked as straddling, no fifth stage literal invented. G2-A (Low) → **COR-05**: `RETROSPECTIVE SOURCE (1977-04)` added at §H.2's first use of the Helmers column, with the reason ("the only carrier of the 1976-11-20 demonstration"), plus the same tag in both timeline rows for that sighting; no class reclassification, because the claims built on it are negative-knowability claims that get safer as the carrier post-dates.

**Checked and deliberately left.** `(PB)` stays 0 occurrences — I did not introduce the token, prose `post-window` / `far side` / the §Q column remain the convention. **No new §U anchor was minted**, so the 55 ↔ 55 parity was never at risk; U.019 and U.021 absorbed every correction into existing entries. S1P1-29, §A, §D, §P row P32 and the `1976-04-01 → 1976-04-12` = eleven-day / "nine months after" durations were re-read against the corrected row and needed nothing. U.024's "a production ledger, which almost certainly never existed" hedge — the one place the audit found the volume's own vocabulary rule bend — is left for the certifier: it is a judgment about a three-person hobby partnership, not a retraction I can measure. S1P1-10's re-keyed `Conflicts:` cell (U.011) was already done by the merge and is unchanged.

**Not settled, with the reason.** G1-F (`sources/test_direct.txt` duplicating the byte-1976-09 ad and possibly inflating the "twelve cached BYTE 1976 issues" denominator): deciding it means re-running the token censuses, which is scripted work (§15.1), and `sources/` is a protected archive this pass may not prune. Reported upward, untouched. The five live conflicts, the unread auction carriers, `byte-1976-07` page-sequence dating and the uncached Kilobaud/Creative Computing layers are **not** mine to trade for a better-looking figure: they stay UNKNOWN with reason, already anchored at U.003/005/007/008/009, U.018, U.037–U.054. **No new FETCH REQUEST is opened** — every route that could settle anything is already registered as untried, and nothing I found needed a document the scripts cannot reach.

## Corrections

STATUS: WRITTEN 2026-09-25

`CORRECTIONS.md` did not exist for this company, so the corrections gate **DID NOT RUN** and Apple's retraction propagation was uncertified. Minted at `01_companies/company_004_apple/CORRECTIONS.md` (1,449 words) with **five** ids, each reaching the register layer *and* a stage volume, per §14 rule 10 / RD-110:

| id | retracts | registers | volumes |
|---|---|---|---|
| COR-01 | §Q's `In-window (last document before the edge)` label; S1P3-10's "twenty dated rows" | `timeline.csv`, `quantitative.csv`, `failures.csv` (the three U.021 rows) | `stage_1.md` §Q row + preamble + S1P3-10; `stage_1_part_2.md` register echoes; `_parts/s1_p3.md` marker |
| COR-02 | BYTE Tier-1 rank (volume- and register-wide) | `sources.csv` A2S-01/02/03/05/08/09/13 tier + `independence_note`; two `timeline.csv` stage2 rows | `stage_1.md` §Boundary adopted row, U.001, S1P1-13/21/24, S1P2-14/15, S1P3-10; `_parts/s1_p2.md` marker |
| COR-03 | "inside the window" + `Source date: UNKNOWN` on S1P1-05/06 | `conflicts.csv` U.019 | `stage_1.md` S1P1-05/06, §Boundary cost, §M.4 item 5, S1P1-01…11 note; `stage_1_part_2.md` U.019 echo; `_parts/s1_p1.md` marker |
| COR-04 | unmarked post-edge register rows | 7 `timeline.csv` rows | `stage_1.md` §Q preamble |
| COR-05 | untagged later carrier at §H.2 | 2 `timeline.csv` rows (1976-11-20) | `stage_1.md` §H.2 |

No register carrier was invented to satisfy the gate: each COR rides rows whose subject **is** the corrected fact. `_parts/` files were appended to only (three `SUPERSEDED 2026-09-26` markers, +247 words total), never rewritten; `research/*.md` dossiers, `sources/` and `tools/` untouched. `_MANIFEST.md` and `stage_1_index.md` were re-measured and carry the repair note, because an instruction file that a cold reader trusts is where a stale figure survives longest.

## Gate before and after

STATUS: WRITTEN 2026-09-25

**BEFORE** (`gates.py --checks csv,keys,anchors,budget,corrections`): **Findings 0 | Passes 19**; `corrections  no CORRECTIONS.md -- gate DID NOT RUN (not a pass)`; `anchors  55 narrative anchors <-> 55 register anchors`; `budget  stage_1.md 56537 | stage_1_index.md 1472 | stage_1_part_2.md 8713`; register widths `timeline 30x11, quantitative 44x12, conflicts 38x15, sources 23x18, data_gaps 35x8, validation 6x11, failures 6x11, decisions 4x15, channels 0x11`; advisory `2 prose mention(s) match no declared entry: U.112, U.113`.

**AFTER** (same command): **Findings 0 | Passes 20**; `corrections  5 retraction ids; register layer reaches 5, volumes 5`; `anchors  parity  55 narrative anchors <-> 55 register anchors`; `budget  stage_1.md 57502 words (cap 60000)` · `stage_1_index.md` · `stage_1_part_2.md` all under cap; every CSV width identical to the BEFORE run (row and column counts unchanged — notes and tier cells edited in place, files rewritten by the CSV parser, not by hand); `citation resolution  57 distinct ids`; same two U.112/U.113 advisories and the same "no hyphenated key" notes. One benign shift: the anchor list read as backticked references rather than citations went from 8 ids to 7, because `U.021` in the rewritten §Q row now parses as a citation — no action.

No parity regression, no retraction left half-propagated, no citation deleted to keep a gate green. Volume 1 sits at **96%** of the 60k cap (amber, legal, §9.2); the ~1,086 added words are corrections and measurement text, and **nothing was cut to fit**.

## Residue

STATUS: WRITTEN 2026-09-25

1. **Volume 2 is still invisible to the `anchors`/`keys` narrative sweep** (`NARR_GLOBS["stage1"]` reads only `stage_1.md`), so the 55 ↔ 55 parity covers ~87% of the volume. That is a `tools/gates.py` defect, not a content defect — reported, not edited, per my write set.
2. **G1-F unresolved by design:** whether `sources/test_direct.txt` inflates any stated census (the "twelve cached BYTE 1976 issues" denominator, S1P1-18/22/25, S1M-08) needs the censuses re-run by script. Nothing I wrote depends on that denominator, and no count was padded to hide it.
3. **A2S-05 still carries two items in one row** (`event_date 1976-11-20; 1977-04`) with now a split tier cell. The clean fix is a second `source_id`, which is a §9.4 append-only register restructure and a central-id assignment — above a repair pass; flagged for the certifier with the reason.
4. **Nine S1P1 records still await the merge's `Source`/`Tier`/`Conf` upgrade** (S1P1-01…04, 07…12, 30 etc.). When that upgrade runs, its Tier cells must follow COR-02's per-item rule, not the old volume-wide Tier 1.
5. **The `stage` semantic mismatch is left as recorded** by the manifest: part 3's 1980-12 cap-table row is `stage1`, `timeline.csv`'s is `stage2`; both rows now carry the COR-02 tier note. A decision, not a repair.
6. **`Tier: 1` residual count not re-censused** after the edits (46 before, by carrier rather than by number); a certifier wanting an exact post-repair figure must re-run the sweep.
7. **UNTRIED at my stop line:** §B.1–B.5, §C.1–C.3, §E.1/E.3/E.6, §F.2–F.4, §G.1–G.3/G.5/G.6, §I.1–I.5, §J.1–J.4, §K.2–K.6, §L.1/L.2, §O.1–O.3 line-by-line reading; `derived_arithmetic` recomputation across the 44 `quantitative.csv` rows; `what_it_did_not_demonstrate` smuggling tests in `validation.csv`; High-gap `follow_up_task` completeness beyond U.044; byte-identity of the five new register headers against Amazon's. Zero web requests made; no `sources/` file read beyond the registers' own claims.

