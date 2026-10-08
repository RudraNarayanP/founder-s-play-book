# NVIDIA Stage 1 — CORRECTIONS.md

Open by the Stage-1 merge pass (`nvidia-s1-merge`) on 2026-09-30. A retraction is not finished until it reaches
the register layer **and** the volume (RD-059/RD-090/RD-105, §14 rule 10), so every id below is propagated to
both and is checked by `gates.py --checks corrections`. Nothing here erases an emitted row: a superseded value
keeps its row id, its text stays legible, and the correction is printed inside the kept row.

**Scope limit of this pass, stated up front.** The merge read the two `_parts/` emissions, the three `research/`
dossiers and the four shared tools. It did **not** open any document under `sources/` and made **0** web calls
(READ list for this brief). Every carrier sentence quoted below was quoted by the emitting pass at a named line,
and is reproduced here with that line so a later reader can re-open it; the merge did not independently verify
the line against the accession bytes, and that verification is the auditor's first task where a correction below
changes a basis.

---

### COR-01 — part 1 §Boundary 4: "no column" for the one month ended January 26, 1997 is REFUTED

**Withdrawn:** that the January 26, 1997 period "appears nowhere else in the document and corresponds to no
column in its own summary table", and therefore that the period must be recorded as UNKNOWN and used for nothing
(`_parts/s1_p1.md` L135–137; conflict `P1K05`; the same reading in the probe dossier §Conflicts X5).
**What replaces it:** the prospectus summary table prints **nine** columns, two of them one-month columns, and
the January-1997 column carries values — revenue 190, net loss (522), operating loss (516), gross profit 63
(USD thousands). Carrier, as read and line-cited by the part-2 pass: `S4355` (424B4, accession
0001012870-99-000192) Selected Financial Data header row **l.1941–1985**, and the same period at F-4. Part 2's
own words for why part 1 was wrong: "A column count taken by reading part of a wrapped table rather than
listing its header cells — RD-124 and RD-127's assumed-column failure mode, arriving here in an inherited
premise" (`P1K16` / anchor `U.110`).
**A basis note, per RD-125:** part 1 §Boundary 4 also states the audited transition month is the one month ended
January 31, 1998; part 2 confirms that label and adds that the same period is captioned January 26, 1998 in one
note table while the statements print January 31, 1998 (`P1K10` / `U.102`). The transition month used by every
register row is **January 31, 1998**, established by the statements and by the FY1999 10-K405 (`S4356`), not by
a note caption.
**Propagated to:** `conflicts.csv` `P1K05` (supersession printed inside `residual_uncertainty`), `conflicts.csv`
`P1K16` (the refuting row, kept as emitted), `quantitative.csv` rows `1997-01-26/one_month_total_revenue` and
`1998-01-31/one_month_total_revenue`, `timeline.csv` rows dated 1997-01-31 and 1998-01-31, `stage_1.md` merge
note contradiction 1 and the inline marker inserted after §Boundary 4's sentence.
**Residual:** which calendar convention each caption intended is UNKNOWN; the figures are not in doubt. Part 1
conservative handling ("use it for nothing") was safe; only its stated reason was wrong, and the merge records
the difference rather than smoothing it.

### COR-02 — part 1 §Boundary 5: the FY1997 movement is no longer an unexplained change with a candidate mechanism

**Withdrawn (as a statement of the corpus limit, not of the value):** "no note in any held draft explains the
change", and "a mechanism candidate exists inside the same lineage … but it is an INFERENCE, not a finding: no
held text links the two, and the $4.3M gross figure does not equal the $898K net movement" (`_parts/s1_p1.md`
L158–163; conflict `P1K01`). Also withdrawn: the part-1 `validation.csv` and `quantitative.csv` statements that
the first profitable quarter amount "was not read by this pass".
**What replaces it:** the movement is an arithmetic identity inside one lineage. Deferred compensation granted
in 1997 moves 2,100 → 4,277 and amortisation 62 → 961 across the March 1998 and final printings, and
**961 − 62 = 899**, allocated 18 to cost of revenue, 471 to research and development and 410 to selling, general
and administrative — which sums exactly to the operating-loss movement (`P1K08` / anchor `U.101`; carrier
`S4355` Statement of Stockholders Equity and the quarterly table, line-cited by the part-2 pass). The quarter
ended 1997-12-31 earned **1,424** (the March draft printed 2,163 for the same quarter; the quarter ended
1997-09-28 moved from (2,413) to (2,572)), so the restatement is localised to two quarters. Canonical 1997 net
loss remains **(3,589)**; the March printing (2,691) travels on as a SUPERSEDED-DRAFT row, as part 1 required.
**Confidence discipline kept:** the *composition* is DERIVED-High (it foots); the *reason* the grants were
re-measured is still UNKNOWN, and the allocation to three expense lines rests on the printed FASB Interpretation
No. 28 policy, not on a narrative sentence. Part 1's caution that the $4.3M gross grant figure does not equal
the $899K net movement is **still true and still printed**; what changed is that the amortisation half of the
same ledger closes the gap.
**Propagated to:** `conflicts.csv` `P1K01` (narrowing printed inside `residual_uncertainty`), `conflicts.csv`
`P1K08` (kept as emitted), `validation.csv` row dated 1997-12-31 (part 1) and row dated 1997-12-31 (part 2),
`quantitative.csv` rows `1997-12-31/net_income_first_profitable_quarter`, `1997/rd_expense_reported`,
`1997/sga_expense`, `1997/deferred_comp_grant`, `1997/deferred_comp_amortization`, `stage_1.md` merge note
contradiction 2 and the inline marker inserted after §Boundary 5's sentence.

### COR-03 — part 1 is truncated: the `## Untried` block it promised was never written

**What is missing, as found:** `_parts/s1_p1.md` ends after its own register row-count footer with a horizontal
rule and a single stray `#` — the first keystroke of a heading never written. Sections Header, Boundary 1–7,
§A–§F and all eight register blocks are present and complete; no table and no prose paragraph is cut mid-way.
**What it presupposed:** part 1 cites its own `## Untried` at L123 (§Boundary 3, family verdicts), L459 (§C.3),
L523 (§D.4, "items 3–6"), L590 (§E.3, "3, 5, 6") and L639 (§F.2). Eight emitted `data_gaps.csv` follow-up cells
name `UNTRIED-1`, `UNTRIED-3/4/5/6`, `UNTRIED-7` and item 10, and emitted conflict `P1K07` says the untested
probe readings are "named in Untried". Part 1's header also planned a third volume (`p3 = Q–U + appendix`) that
was never dispatched; part 2 took §G–§U, so no narrative section is missing from the volume and no separate
claim-record appendix exists (records are inline per section in both parts).
**What replaces it (and what does not):** this merge **did not reconstruct** the block — writing a section a
part left unwritten is not a merge decision. Part 2 eleven-route `## Untried` is carried forward as the volume
register of untried routes, re-numbered with part-1 item numbers in parentheses, and the probe dossier
`research/A_chronology_feasibility.md` carries its own eight-route list. A `data_gaps.csv` row was minted to hold
the coverage limit with a named follow-up.
**Consequence for claims resting on it:** no factual claim in part 1 rests on the missing block. What is weakened
is part 1 **route inventory and its item numbering**: any later reader who takes `UNTRIED-7` as an address will
not find part 1 definition of it, and must read it through part 2 cross-references or the probe list. The
seven part-1 conflict rows `P1K01`–`P1K07` likewise have no §U anchor, because the part-1 anchor block is what
the truncation removed; none was minted for them (see `stage_1_index.md`).
**Propagated to:** `data_gaps.csv` minted coverage row, `stage_1.md` merge note (coverage-limit paragraph, the
inline marker after §Boundary 3, and the END-OF-VOLUME-1 notice at the end of part 1 slice), `stage_1_index.md`,
`_MANIFEST.md`, `03_quality_control/nvidia_s1_merge_notes.md`.

### COR-04 — one prose value sat in a date column (register normalisation on touch)

**What was emitted:** `channels.csv` (part 2) row for the distributor channel carried
`date_tested = never tested within the stage` — a true statement, and a sentence, not a date (§13: a date cell
must carry a year-bearing value; `UNKNOWN` is the complete value, prose is a field-shift hazard).
**What replaces it:** `date_tested = UNKNOWN`, with the emitted wording preserved verbatim inside the same row
`notes` cell. The channel row is **not** deleted: it is the register carrier for the contemporaneous negative
("While the Company has not yet sold products through distributors", printed in every held draft), which is
evidence in itself. RD-122 precedent (Target rows B1S12/B1S13, `NOT ACCESSED` → `UNKNOWN`).
**Count of normalised date cells on this pass: 1. Count of numeric `stage` values normalised: 0** (all 194 rows
carry the literal `stage1`).
**Propagated to:** `channels.csv` (the row itself, with the original wording printed inside it), `stage_1.md`
merge note, this file. `gates.py --checks csv` now passes the `date_tested` test on this register.

---

## Residue handed to the Stage-1 auditor (not corrected here)

1. **`P1-38` is cited but declared nowhere.** Part 2 cites claim record `P1-38` in `decisions.csv` (the
   1999-01-22 row, giving up contract funding) and in §K/§T prose, and both parts together declare
   `P1-01`–`P1-37` and `P1-39`–`P1-60` with **0 duplicate declarations**. A merge may not invent a claim record
   to fill a citation, so the reference is left exactly as emitted and named here.
2. **`P1G06` and `P1G08` are cited in part 1 prose** while the ten emitted `data_gaps.csv` rows from part 1 carry
   no such labels (part 1 gaps are uncited by number, part 2 gaps are cited by `U.1nn` anchor). The two series
   are addressable by text but not by key. Left as emitted.
3. **The line citations behind COR-01 and COR-02 were not re-opened by this merge** (0 web calls, no `sources/`
   reads in the brief READ list). `S4355` l.1941–1985, the Statement of Stockholders Equity rows and the
   quarterly table are the lines to re-read first; if any of them fails, COR-01 and COR-02 revert and the part-1
   readings stand — this file is the place that revert must be written.
4. **Two intake families are still empty directories** (`sources/wayback/`, `sources/financials/`) and family (e)
   documentary has no scripted route, so the tier ceiling is unmeasured. The T2 upgrade needs one browser-egress
   Wayback CDX answer **and** one in-window periodical body read; both are `FETCH REQUEST` items in
   `03_quality_control/nvidia_s1_merge_notes.md`, not defects of this volume.
