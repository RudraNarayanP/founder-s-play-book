# Provenance Corrections Register — APPLE Stage 1

Standing list of retractions and labelling corrections established **after** the stage volumes were
merged, each verified against the held documents under `sources/` and the register rows under
`research/`. Minted 2026-09-26 by the apple-s1-repair pass on the finding of
`03_quality_control/apple_s1_audit1_chronology_hindsight.md`. Until this file existed the
`corrections` gate **did not run** for Apple (§14 rule 10: an instruction layer a cold reader trusts);
it now does, and every entry below is checked for propagation into both the registers and the volumes.

**Rule.** A retraction is not finished until it reaches every layer: the claim record, the §U conflict
that owns the subject, the narrative section that leans on it, and the register rows that carry it.
Superseded readings are marked where they stand and are **not** deleted; a corrected cell keeps its id.

---

## COR-01 — the §Q boundary inversion, and the row count it propped (was G1-A, G1-B: HIGH)

**Withdrawn.** The §Q micro-timeline row printed `1977-01-19 | In-window (last document before the edge)`.
Both halves are false: 1977-01-19 is **sixteen days past** the adopted 1977-01-03 edge, and the
parenthetical asserts an ordering its own date contradicts. **Replaced** by the straddle form used by every
other carrier of the same fact (§A, §D, S1P1-29, §P row P32, the U.021 register rows):
`1976-12-10 → 1977-01-19 | Straddles the edge (1976-12-10 in-window; 1977-01-19 far side)`, with the event
cell now stating that `hcc0213` is the **first document past** the boundary, not the last before it.

**Also withdrawn, on the same measurement:** S1P3-10's "twenty dated rows inside the window". Re-measured
two independent ways — §Q read cell by cell (25 rows: **17** wholly in-window + the boundary event + **1**
straddle + 5 far side + 1 out of window) and `research/timeline.csv` parsed by date (**19** `stage1` rows
starting on or before the edge, of which one is the boundary event and one straddles → **17**) — the two
layers agree. The record's `Date:` span is closed at 1977-01-03. The audit's note that the column printed
"19 rows marked In-window" is itself one high: as printed it offered 18 in-window labels + 1 window-end =
**19**, so the "twenty" was unreachable even before this mislabel is removed. The substantive half of the
claim is untouched and still printed: **no in-window row is an Apple-side document**.

**Carriers touched.** `stage_1.md` §Q row, §Q preamble, record S1P3-10; `research/timeline.csv`,
`research/quantitative.csv`, `research/failures.csv` (the three U.021-keyed rows); the same three rows
quoted into `stage_1_part_2.md`'s register blocks. No register date cell needed repair — the range form was
already correct there — so the fix is the label and the count, not the evidence.

## COR-02 — BYTE was tiered Tier 1 volume-wide (was G1-D: MEDIUM)

**Withdrawn.** `§5` ranks industry and trade publications **Tier 3**; the register and the narrative ranked
every BYTE row **Tier 1**, including the two carriers that most need the distinction: the unsigned February
1981 column "Apple Stock Goes On Sale", used to corroborate the end edge, and the magazine's own April 1977
column prose. **Replaced** by a per-item rule, stated in `research/sources.csv`:

* **Tier 1 retained** where the item *is* first-party or documentary matter: Apple's own June/July 1977
  advertisements (A2S-07, A2S-08's ad pages), Wozniak's bylined May 1977 system description (A2S-06), a
  named dealer's own advertisement (A2S-04), the **April 1977 store-directory page as a printed commercial
  artifact** (A2S-05), and documented-absence censuses, whose rank is the rank of the corpus searched
  (A2S-01, S1M-08).
* **Tier 3** where the item is the magazine's own prose about the period: A2S-09 outright (one unsigned 1981
  column), and Helmers' April 1977 column prose inside A2S-05.
* **Mixed rows carry `1 (printed commercial artifacts) / 3 (the magazine's own prose)`** rather than being
  flattened to one number: A2S-02, A2S-03, A2S-05, A2S-08, A2S-13.

**What this does not change.** Independence, lineage and confidence are **not** re-opened: the 1981 column is
still an origin of unrelated author, publisher and decade to the FY1994 10-K, the end edge's **year** still
stands on the filing with a genuine second origin, and **U.023** still caps the FY1978–FY1980 series at one
witness. What changes is the **rank** claimed for that carrier, which is what the confidence scale is built
from. The §Boundary adopted row now reads "a **Tier-1 registrant filing** and an **independent Tier-3 trade
column**", U.001's `EVIDENCE WEIGHT` says the same, and the records resting on the 1981 column
(S1P1-13, S1P1-21, S1P1-24, S1P2-14, S1P2-15) carry Tier 3.

**Not over-corrected.** BYTE April 1977's ~35-store directory and Apple's June 1977 direct-mail order form
remain documentary commercial artifacts and remain load-bearing in **U.008**: the tension between them and
Wozniak's word-of-mouth memoir is this volume's **finding**, and the demotion of magazine prose is not
evidence that the channel was thinner than the memoir says.

## COR-03 — S1P1-05 and S1P1-06 placed post-edge artifacts "inside the window" (was G1-C: MEDIUM)

**Withdrawn.** "A national retailer directory published in a technical monthly **inside the window**" and "A
company advertisement **inside the window**", with `Source date: UNKNOWN` on both. Under the adopted boundary
these artifacts (April 1977; June–July 1977) are three to six months **past** the edge, and their cover dates
are precisely known, so the `UNKNOWN` was suppressing the very contradiction that makes the conflict legible.
**Replaced**: both records now state post-edge status, carry `Source date: 1977-04` and `1977-06 / 1977-07`,
name their carriers (A2S-05; A2S-07/A2S-08), and point at the conflict that owns the subject.

**The conflict stays two-sided and is not resolved away.** **U.019** CLAIM A continues to print the in-window
reading exactly as the interrupted pass wrote it; CLAIM B is the defended boundary; the adjudication is a
merge decision, and the residual sentence says in terms that adopting a later Stage-1 end would make the
older records correct as written. The §Boundary rejection row, §M.4 item 5 and the S1P1-01…11 hand-off note
were updated to match, because all three instruct later readers.

## COR-04 — post-boundary rows were unmarked in the register layer (was G1-E: LOW)

Seven `timeline.csv` rows dated past 1977-01-03 (`1977-02-16`, `1977-04`, `1977-04-15/17`, two `1977-05`,
`1977-06`, `1977-07`) carried no out-of-window marker, while only three of the ten had one; the `1977-04`
row even read "the most granular channel evidence recovered **for Stage 1**". Each now opens
`POST-EDGE (window closes 1977-01-03)`, that row's note says "for the Stage-1 product, printed three months
after the edge and never used as Stage-1 state", and the straddling Homebrew pair opens
`STRADDLES THE EDGE` instead of a post-edge tag because both halves are load-bearing. **No fifth stage
literal was invented**: §13's four literals are untouched and every row remains `stage1`.

## COR-05 — §H leaned on post-window carriers without §6's tag (was G2-A: LOW)

§H is titled "MARKET (AS KNOWABLE IN-PERIOD)" for a window ending 1977-01-03, and its definitional
evidence — Carl Helmers' April 1977 "appliance computer" column, the only carrier of the 1976-11-20
demonstration — post-dates the edge. `RETROSPECTIVE SOURCE (1977-04)` is added at first use, with the reason
printed. No class reclassification: CONTEMPORARY OBSERVATION is correct as to the column's own moment, and
every claim built on it is a **negative** knowability claim, which gets safer as the carrier post-dates. The
same tag now appears in the two `timeline.csv` rows for the 1976-11-20 sighting.

---

## Standing positions this pass does not move

* **`$666.66` returns 0 hits across all 61 files under `sources/`** and stays FOUNDER CLAIM / UNKNOWN, never
  FACT; the corpus's only dollar-shaped 666 is IMSAI's December 1976 decoy (U.004).
* **No in-window document gives 1976 price, order, units, revenue, supplier, or a founder officer title**
  (U.014, U.026, U.030). Absence is scoped to this corpus, not asserted as a fact about the world.
* **Wayne's 10% vs 12%, Markkula's terms and arrival date, the 50 boards at $500, and $77,000 vs $770,000
  remain live, two-sided and unaveraged** (U.005, U.007, U.003, U.009); U.005's bar on printing an average of
  10 and 12 is unchanged.
* **Apple's earliest EDGAR text is 1994-01-26 (FY1994 10-K lineage)**, so all earlier evidence is print and
  **one lineage is one source** (§3 filing-lineage rule; S1M-01, S1M-02, U.023).
* **`conflicts.csv` rows `S1P2-CF-01…05` stay unmerged into the register** as the merge sheet records: they
  parse to 14 fields against a 15-column header, and their subjects are already carried by U.003, U.005,
  U.007, U.008, U.009.

## Untouched on this pass, and why

`_parts/s1_p1.md`, `_parts/s1_p2.md`, `_parts/s1_p3.md` are append-only: they carry a `SUPERSEDED` marker for
the readings corrected here and are not rewritten (§14 rule 4). `research/*.md` dossiers, `sources/`, and
`tools/` are outside this pass's write set. `sources/test_direct.txt` (G1-F) is **not** deleted and no census
denominator was recomputed: whether it inflates the "twelve cached BYTE 1976 issues" figure is scripted work,
and it is handed to the certifier as residue with the reason.
