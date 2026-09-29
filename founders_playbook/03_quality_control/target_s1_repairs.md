# target_s1_repairs.md — REPAIR pass, company_042_target Stage 1

Agent `target-s1-repair`. Run 2026-09-29, against the three Stage-1 audits and the orchestrator's own
re-verification in `MASTER_RESEARCH_LOG.md` RD-122 and RD-125. **This is a repair record, not a certification:
the writer is not the certifier (§15.6), and nothing here is a claim that the corpus is sound.** A separate agent
certifies after this pass, and the residual uncertainties this pass created or left open are listed at the end.

Method read before writing: `00_METHOD_AND_STYLE.md` §13 (schemas), §14 rules 1–12 (4 supersede-don't-erase,
8 grep-before-you-assert, 10 the instruction layer, 12 line numbers are locators), §15.1/§15.6.

**Files written (all claimed first with `python tools/scaffold.py claim --path … --agent target-s1-repair`):**
`quantitative.csv`, `timeline.csv`, `conflicts.csv`, `data_gaps.csv`, `stage_1.md`, `stage_1_index.md`,
`CORRECTIONS.md`, `_MANIFEST.md`, this file.
**Files NOT written:** `sources.csv` and `sources/_index/_INDEX.md` (parallel agent), everything under `sources/`
(protected archive, read-only: §14 rule 4), `MASTER_RESEARCH_LOG.md`, anything under `tools/`, `_parts/`,
`research/`. `validation.csv`, `failures.csv`, `decisions.csv`, `channels.csv` were read and **needed no change** —
they hold no December year-end, no mislabelled class the defect list named, and no corpus-wide null
(their `-12-31` grep hits are zero; `data_gaps.csv`'s two are the command parameter `--to 1985-12-31`).

---

## 1. Gate record — every run, tier flag visible

Required gate: `python tools/gates.py --company-dir founders_playbook/01_companies/company_042_target --checks csv,keys,anchors,corrections --tier core --fail-on substantive`

| # | point in the pass | result |
|---|---|---|
| 0 | baseline, before any write | `--tier core` → **Findings: 0 \| Passes: 19**; `corrections 6 retraction ids; register layer reaches 6, volumes 6` |
| 1 | after defect 1a (`quantitative.csv` re-dating + the 21 missing basis tags) | `--tier core` → **Findings: 0 \| Passes: 19**; `csv quantitative.csv 61 rows x 12 cols`; still `6 retraction ids … 6, 6` |
| 2 | after defect 1 complete (COR-07…COR-14 opened in `CORRECTIONS.md`, `timeline.csv`, `conflicts.csv`, §Boundary 4) | `--tier core` → **Findings: 2 \| Passes: 18**; `corrections 14 retraction ids; register layer reaches 9, volumes 8`; `corrections \| registers \| 5 retraction(s) reach the prose but NOT any register …: COR-09, COR-10, COR-12, COR-13, COR-14`; `corrections \| volumes \| 6 retraction(s) name no stage volume …: COR-09, COR-10, COR-11, COR-12, COR-13, COR-14` |
| 3 | after defects 2–3 | `--tier core` → **Findings: 2 \| Passes: 18**; registers missing `COR-10, COR-13, COR-14`; volumes missing `COR-10, COR-11, COR-12, COR-13, COR-14` |
| 4 | after defect 7 (data_gaps re-scope) | `--tier core` → **Findings: 1 \| Passes: 18**; `anchors \| narrative \| anchor with no register row: U.019` — **a defect this pass introduced**, see §5.e |
| 5 | after restoring the anchor keys | `--tier core` → **Findings: 0 \| Passes: 19** |
| 6 | final, after the FETCH REQUEST and the manifest/index updates | `--tier core` → **Findings: 0 \| Passes: 19**, exit 0; `corrections 14 retraction ids; register layer reaches 14, volumes 14`; `csv quantitative.csv 68 rows x 12 cols`; `keys stage_1.md 5 source tokens all resolve`; `anchors parity 37 narrative anchors <-> 37 register anchors` |

Gate runs 2 and 3 are the failure the corrections gate exists to produce — a retraction that stops at the prose —
and they are quoted rather than hidden. Run 4 is a repair-introduced regression caught by the anchors gate.

**Not in the required check set, and it matters:** `budget` was not run here. RD-122 records that at
`--tier core` the volume of 37,507 words already breached the 22,000 core planning cap; this pass grew the volume
to **38,489 words**, still under the §9.2 40,000 soft cap and the 60,000 hard cap, and further past the core
planning figure. Under RD-122's ruling the cap is a dispatch budget, not a limit on written evidence, so no
evidence was trimmed. The certifier should expect `budget` to fire at `--tier core`.

---

## 2. Defect by defect

### Defect 1 — the fiscal-basis defect, and the correction that carried it

**1a. The December year-ends.** Every affected row was re-dated to the year-end its own carrier prints, and the
withdrawn date is kept inside the same cell (rule 4). Carriers read this pass:

| row | withdrawn | now | carrier line that prints it |
|---|---|---|---|
| r54 r55 r56 r57 | `1973-12-31` | **1974-02-02** | `sources/corporate_print/1973_dayton_hudson_djvu.txt` **L172-174**: `1973 1972 / : 52 Weeks Ended 53 Weeks Ended / Consolidated February 2, 1974 February 3, 1973` |
| r59 | `1972-12-31` | **1973-02-03** | same L172-174, second column (`53 Weeks Ended February 3, 1973`) |
| r58 | `1969-12-31` | **1970-01-31** | the five-year header L3975 prints only the bare label `1969`, so the day came from fiscal 1969's own report: `1969_dayton_hudson_djvu.txt` **L1488** `…at January 31, 1970, and $6,951,217 at February 1, 1969` |
| r60 | `1962-12-31` | **1975-02-01** | `1974_dayton_hudson_djvu.txt` **L147-148** `52 Weeks Ended … Consolidated February 1, 1975 February 2, 1974`; and see defect 4 — the areas are the FY1974 roster's, not 1962's |
| `timeline.csv` row 23 | `1973-12-31` | **1974-02-02** | L172-174 of the same report that carries the five-year row |

**No held carrier prints a fiscal-1970 or fiscal-1971 year-end day.** Those two days are recorded as `UNKNOWN`
(the date cells carry the fiscal-year label alone: `1970`, `1971`) and a **FETCH REQUEST** was raised on
`data_gaps.csv` U.030 for the two PDF legs whose Statement of Income headers would print them. No December
placeholder was substituted anywhere. Measured on the repaired bytes: **the `date` / `date_or_range` columns of
`quantitative.csv` and `timeline.csv` contain zero `-12-31` values** (verified by parsing the columns, not by
grepping the file). The literal strings `1973-12-31`, `1969-12-31`, `1972-12-31`, `1962-12-31` do still occur
**8 times** in those two files — 7 in `quantitative.csv` and 1 in `timeline.csv` — and every one of those sits
inside a `SUPERSEDES date …` retraction sentence in a `notes` cell, which is what rule 4 requires. A grep that
does not parse columns would report "8 December dates remain" and be wrong; the check that means anything is the
one on the date field.

**1b. COR-01's un-applied re-tag.** The merge paragraph said every bare-year row had been re-tagged. Measured on
the bytes it had not: the 21 bare-year rows lacking a literal `PERIOD BASIS` tag were tagged this pass, derived
from each row's own printing layer (`source_date` vs `date`: same year → CONTEMPORANEOUS, later layer → RESTATED).
COR-01's own paragraph in `CORRECTIONS.md` now carries that sentence struck through and dated, not erased.

**1c. CH-1 — the "basis migration by FY1975" was a misread carrier, and it was inside a correction.** Retracted
in four places. The carrier that settles it is quoted verbatim inside the new correction record (COR-08), which is
the rule this defect teaches:

> `Fiscal Year. The Corporation's fiscal year ends on the Saturday closest to January 31. Fiscal year 1975 ended on
> January 31, 1976; fiscal year 1974 ended on February 1, 1975. Each of these years consisted of 52 weeks.`
> — `sources/corporate_print/1975_dayton_hudson_djvu.txt` L3246-3250 (read this pass, 6 lines, verbatim)

Everything 31-December in that layer is inside `F. INVESTMENT iN JOINT VENTURES` (L3570), under `Condensed combined
financial statements of the joint ventures follow:` (L3578-3579): L3583 `FOR THE YEAR ENDED DECEMBER 31, 1975` and
L3604 `DECEMBER 31, 1975`, and the same block states its position `at January 31, 1976` (L3575).
`grep -c "Saturday closest to" stage_1.md` was **0** before this pass — now the sentence is in §Boundary 4, in
`conflicts.csv` U.011 and in `CORRECTIONS.md` COR-08.

**1d. `timeline.csv` row 17.** It asserted an FY1975 fact while carrying `source_id` **S4201**, the FY1965 report.
Re-pointed to **S4211** (the FY1975 layer) and re-classed from `FACT` about a migration to `FACT (verbatim carrier
note)` about the printed Fiscal Year note, dated `1976-01-31`, confidence High, `conflict_ref` U.011, with the
withdrawn wording retained in its `notes` cell. No row added or deleted.

### Defect 2 — dropped components, and a denominator that was assumed

All six values were grepped in the held bytes before being written (rule 8), and each new row names the lines that
print it:

| value | fiscal year | carrier |
|---|---|---|
| 217,961,635 | FY1966 (ended 1967-01-28) | `1966_…` L49, L323, L434 |
| 260,173,514 | FY1967 (ended 1968-02-03) | `1967_…` L765, L819 |
| **434,132,744** | FY1968 (ended 1969-02-01) | `1968_…` L1251, L1349, **L1363** (`$434,132,744 100%`) |
| 945,306 (thousands) | FY1970 (day UNKNOWN) | `1970_…` L828-829 (`Net Retail Sales $945,306 \| $868,335`) |
| 1,086.4 (millions) | FY1971 (day UNKNOWN) | `1971_…` L309 header, L312 |
| 1,262,759,000 | FY1972 (ended 1973-02-03) | `1972_…` L10, L325, L939 |

`434,132,744` was confirmed present in the held FY1968 carrier and **absent from `stage_1.md` and
`quantitative.csv`** before this pass, exactly as reported. r18's denominator is now named rather than assumed:
`189,515,025 / 434,132,744 = 43.65%`, so the printed "44" is true against the **Dayton Corporation** total; against
the pooled Dayton Hudson FY1968 restatement of `795,243` thousand (`1969_…` L951) the same numerator is
**23.83%** — see §5.g on that figure. Recorded in r18's cell, `CORRECTIONS.md` COR-09 and a new paragraph in
`stage_1.md` §E.2 (the section whose whole subject is the denominator that must travel with a figure).

Two residuals surfaced while adding them and are recorded, not resolved: the FY1967 report prints **220,511,038**
as its fiscal-1966 column where the FY1966 report printed **217,961,635** (Δ 2,549,403), and the FY1972 report
prints **1,088,338,000** for fiscal 1971 where the FY1971 report printed **1,086.4m** (Δ ≈1.9m). Same object, two
amounts, one lineage: no growth rate may cross those documents without naming which restatement it used.

### Defect 3 — r15's precision, the silent choice, and the DERIVED classes

r15: `60770000` → **`60800000`**, class `ESTIMATE` → **`DERIVED`**, with all three printings named in the cell and
the merge's silent choice recorded: computed `60,769,935`, B1's dossier `~60,800,000`, register `60,770,000`; a
quotient of a two-significant-figure printed percent cannot be rendered at eight. Accuracy ± ≈1,000,000 from the
rounding of the percent alone.

Classes: **0 rows were `DERIVED` although 9 carry arithmetic.** **7 are now `DERIVED`** — r4, r11, r12, r15, r57,
r58, r59 — because their values are computed and printed in no held layer. **r2 and r30 deliberately keep `FACT`**
and their cells say why: they print their own values and their arithmetic only *checks* a printed percentage, which
is a footing, not a derivation. That distinction is the finding; a sweep that made all 9 DERIVED would have
mislabelled two printed figures to satisfy a count.

### Defect 4 — labels that read a print for something it does not print

Each was re-read in its carrier before it was moved, as required.

* **r17** — `CONTEMPORANEOUS` withdrawn for a comparative column. `1968_…` L1355-1356 heads the table
  `RETAIL SALES. Retail sales by operating groups for 1968 and 1967 were as follows:` and L1361 prints
  `Goods Stores 189,515,025 44 141,824,116 38 33.6`: 141,824,116 is the prior-year column of a 1968 document.
* **r60** — a FY1974 roster's *current* areas were labelled fiscal 1962. `1974_…` L4633-4641 prints
  `LOW MARGIN STORES … Stephen L. Pistner, President (000) Opened / Roseville, Minn. 68 1962 / Crystal, Minn. 96 1962
  / Duluth, Minn. 96 1962 / Knollwood, St. Louis Park, Minn. 106 1962`. The areas are observations of the estate at
  the FY1974 year-end; `1962` is a cohort label. Date, basis sentence and metric reading all corrected; the metric
  name (`…_1962_openings`) kept, because it names the cohort, not the observation year.
* **r11 / r25** — circular. r11's 17 Target stores is derived from the group's 19 less 2 hard-goods units, and
  r25's 19 is then glossed as "the derived Target 17 plus 2". Both cells now state the dependency and disclaim the
  cross-check; neither corroborates the other. Confirmed real, confirmed as the pair (not r11/r20).
* **r42 + r43** — 139,686,954 + 31,256,511 = 170,943,465 against the printed deduction total **171,932,690**
  (`1965_…` L837) = **989,225 short**, and no subtotal row existed to reveal it. The printed total is now a row
  (`parent_total_cost_of_sales_and_expenses_printed`), the seven component lines and their line numbers are named
  in its cell, and the residual is stated as unexplained. **No plugged figure was invented.**
* **r27** — printed 868,335 (`1969_…` L951) against the same report's segment legs
  607,697 + 233,532 + 27,107 = **868,336** (L1001-1004); the four-segment column does foot to Total Revenues
  888,357 (L957 with 20,021 real estate), so the 1-thousand residual sits inside the retail legs. Value unchanged
  (it is what the named line prints); the residual is recorded. See §5.f on the wording of this claim.
* **r32, r37, r38** — precision laundering, all three confirmed in the carrier: `1966_…` L214
  `an average of more than $7.50 per visit, excluding groceries` (value now `>7.50`, unit says it is a floor);
  L806-807 `a first mortgage note in the approximate amount of $2,200,000`; L808-809 `annual rentals of
  approximately $225,000`. The two qualifiers moved to the `unit` cells using the convention r45/r46 already use.
* **`stage_1.md` §K.3** — the volume said the per-store divisions were "written once … confidence **Medium**" while
  the register carried **two** rows at **Low**. The prose now matches the register (two rows, `DERIVED`, Low) rather
  than the register being raised to the prose, because the carriers — one UNVERIFIED-TLS layer restating four of its
  five columns, a group numerator over a group denominator — support Low.

### Defect 5 — §T.2's inverted independence ledger

Confirmed, and it is worse than a wrong name: `P2S01` resolves **two ways inside the same volume**. §T.1's table row
(L1634 pre-repair) reads `P2S01` as *Chain Store Age*, April 1963; the register-emission block (L2119 pre-repair)
reads `P2S01` as *The Dayton Company Annual Report 1966*, which the merge folded into **S4202** under the note
`same lineage as B1S01`. §T.2 used the bare local id, so on the harder reading it nominated a parent self-account as
the corpus's only independent origin and directly contradicted §H.2, which had it right. §T.2 now names **S4215**
by global id, states the collision, and keeps the withdrawn sentence struck through.

The two corroboration cells: **P2-02** (`Corroboration: 1`, no second source named — the other print is the same
opening letter of the same report) and **B05** (`Corroboration: 1 lineage` at Conf High — FY1965 L159-166 and the
FY1970 report L209-212, one series restating itself) are both restated `0 independent` with the reason inside the
cell; a lineage count is not a corroboration count. Registered in `data_gaps.csv` U.031 so the id reaches the
register layer as well as the volume.

### Defect 6 — S4203 quote fidelity: the fabrication charge is REFUTED, and the citation stands

Checked in the bytes before touching anything, per the instruction not to "fix" a wrong defect claim.
`1967_dayton_hudson_djvu.txt` **L1952 is `JOHN F. GEISSE`** and **L769-770** print
`1967. Target’s sales were $86,901,007, an in-` / `crease of 43 percent`. So `(L1952)` is a line locator on real
text, and the quoted sentence exists; the auditor found one carrier sentence and missed the other. **No de-fabrication
was performed** — COR-13 records the refutation so a later pass does not retry it.

What did move: in `stage_1.md` claim record E02 the possessive is the carrier's typographic apostrophe
(`Target’s`, U+2019, which `sources.csv` renders as `Target sales`), the locator sits **outside** the quoted span, and
the line-break join is marked `[L769|L770]` instead of silently repaired (rule 12). r15 and r16 carry the COR-13
note. **The `sources.csv` S4203 `relevant_passage` cell was NOT edited** — that file belongs to the parallel agent;
the fix is recorded as an **outbound correction** at COR-13, the way COR-02 records its outbound leg to the log.

### Defect 7 — nulls stated over families that never ran

`data_gaps.csv` U.024 ("no family returned an earlier document") and U.019 ("no contemporaneous periodical mention")
are re-scoped into the §7 vocabulary: **EMPTY-within-perimeter** where a search ran and returned nothing,
**UNANSWERED** where a route failed, **UNTRIED** where work was not done — with U.032/U.033 named as the families
that were never searched. U.024's gap cell now reads "no document before FY1965 exists IN THIS ITEM … not a
statement that none exists elsewhere". The volume's §U.2 U.019 entry was already properly scoped and carries a
COR-14 sentence; §U.2 is where a cold reader looks, so it is quoted there too.

---

## 3. The 21 / 13 reconciliation (and a third number, which is mine)

Three counts were measured of the same 36 bare-year rows in `quantitative.csv` before this pass. **They are three
definitions, not three facts, and none is wrong.** I did not inherit either; I measured all three on the bytes:

| definition | with a basis statement | without |
|---|---|---|
| **(B) audit 1 — "21 of 36"**: bare-year rows lacking a **literal `PERIOD BASIS` tag** | 15 | **21** — reproduced exactly |
| **(A) RD-125 — "23 of 36 … so 13 carry no basis note"**: `notes` containing `FY` \| `fiscal` \| `end` | 23 | **13** — reproduced, but see below |
| **(C) this pass**: `notes` containing `FY` \| `fiscal` \| `ended`, word-true | 22 | **14** |

The 13/14 difference is one row and it is the stem. Matching `end` rather than `ended` catches **r6**, whose note
reads `year-end counts printed nowhere held` — a sentence about an absence, containing the letters `end` inside
`year-end`. That row states no period basis, so the honest count of rows with no basis note is **14**, not 13, and
the same failure mode RD-124 and RD-125 log (reading a field or a stem for something it is not) is what produced
the 13. **Definition (B) is the one I repaired against** — a literal tag is checkable by a later gate, a fuzzy
keyword match is not — and its 21 rows are now tagged, so both 21 and 14 are 0 on the repaired bytes:
`quantitative.csv` now has **38** bare-year rows (the 36 plus the two new `1970`/`1971` component rows, whose day
is UNKNOWN), **all 38 carry a literal `PERIOD BASIS` tag**, and 65 of 68 rows carry one overall. The three that do
not are r1, r2 and r39: they carry exact period-end dates and state their basis in prose
(`CONTEMPORANEOUS for the fiscal year ENDED 1966-01-29`). `_MANIFEST.md`'s "all 61 rows carry a … period basis" is
correct as a statement about CONTEMPORANEOUS/RESTATED words being present (0 rows lack them) and misleading about
tags; it is rewritten with both numbers and their definitions.

---

## 4. Corrections opened, and every place each reaches

`CORRECTIONS.md` now carries 14 ids: COR-01…COR-06 (merge, untouched but for the superseded sentences inside
COR-01) and **COR-07…COR-14** opened here. Each has a table row *and* a dated section; each withdrawn wording is
kept visible and struck through where it lived; each reaches the register layer and a volume, which is what the
`corrections` gate measured at run 6: `14 retraction ids; register layer reaches 14, volumes 14`.

| id | reaches the registers | reaches the volumes |
|---|---|---|
| COR-07 | `quantitative.csv` r54-r60 + the 21 tagged rows + the two new UNKNOWN-day rows; `timeline.csv` rows 17, 23; `conflicts.csv` U.011 | `stage_1.md` §Boundary 4, §P.1; `stage_1_index.md`; `_MANIFEST.md` |
| COR-08 | `timeline.csv` row 17 (notes carry the quoted L3246-3250); `conflicts.csv` U.011; `quantitative.csv` r54-r57 tags | `stage_1.md` §Boundary 4 (carrier quoted verbatim), §P.1 |
| COR-09 | `quantitative.csv` 6 new rows + r18 | `stage_1.md` §E.2 (new paragraph), §P.1 |
| COR-10 | `data_gaps.csv` U.031 | `stage_1.md` §T.2, claim records P2-02 and B05 |
| COR-11 | `quantitative.csv` r15 + the 6 re-classed DERIVED rows | `stage_1.md` §P.1 |
| COR-12 | `quantitative.csv` r11, r17, r25, r27, r32, r37, r38, r60 + the new 171,932,690 row | `stage_1.md` §K.3 |
| COR-13 | `quantitative.csv` r15, r16 | `stage_1.md` claim record E02 |
| COR-14 | `data_gaps.csv` U.019, U.024 | `stage_1.md` §U.2 (U.019 entry) |

**Known limit of that propagation, stated rather than glossed (rule 10):** inside `stage_1.md` the merge preserved
the pre-merge emission blocks (its §Appendix CSV slices, e.g. the emitted timeline row still reading
`1975-12-31` and the emitted source row still reading `JOHN F. GEISSE (L1952)`), and `_parts/s1_p1.md`,
`_parts/s1_p2.md`, `research/B1_dayton_print_records.md` are all declared SUPERSEDED audit trail (RD-122's
byte-identical-slice proof, `stage_1_index.md` decision 6). Those blocks are historical records of what a dossier
emitted, not live registers; the live carriers are the nine root CSVs, and the withdrawn readings are retracted
there and in the prose. This pass did not rewrite the emission slices, and says so: a reader who takes a line from
an emission block is reading a superseded emission, and the COR id is the thing to follow.

---

## 5. What this pass refused to fix, and why

* **(a) The S4203 "reconstruction" charge — REFUTED, not repaired.** As instructed and as verified in the bytes
  (L1952 and L769-770). The citation stands; only fidelity and format moved. Recorded at COR-13 so the charge is
  not re-raised by a later pass.
* **(b) The brief's own count for the 1975 layer.** "the string `FOR THE YEAR ENDED DECEMBER 31, 1975` occurs
  **twice in 5,458 lines**" — `grep -o … | wc -l` returns **1** occurrence, at L3583, in a file of 5,458 lines. The
  second December-31 print is L3604, `DECEMBER 31, 1975`, a joint-venture **balance-sheet** date in the same block.
  The material claim is unaffected (both are inside the joint-venture statements, and the corporation's own year-end
  is January 31, 1976), so COR-08, `conflicts.csv` U.011 and `timeline.csv` row 17 all state **1 occurrence of the
  full string** rather than inheriting "twice". This is rule 8 applied to the brief.
* **(c) `sources.csv` S4203 `relevant_passage`** (the dropped possessive, the locator inside the quoted span) — not
  in this pass's file set. Outbound correction at COR-13 and in this report, per the ownership rule; the parallel
  agent owns the edit.
* **(d) `MASTER_RESEARCH_LOG.md`, `tools/`, `_parts/`, `research/`, `sources/`.** Not touched, not "tidied"
  (rule 4). RD-125's own text still says "twice"; the log's owner is the orchestrator.
* **(e) Nothing in this pass's own output was spared either.** The gate at run 4 caught that my re-scope of
  `data_gaps.csv` had **deleted the leading `U.019` from the gap cell**, orphaning the anchor; the anchors gate
  fired and the keys were restored (both U.019 and U.024 keep their anchor prefix). Earlier in the pass a
  `recs = rows[1:]` aliasing bug meant the first attempt to append rows wrote the file back **without** them —
  silent, since the printed count came from the in-memory list. The seven rows were re-applied with a readback that
  counts records on disk after the write. Both are recorded because a repair pass that hides its own near-misses
  teaches nothing.
* **(f) The wording of the r27 claim.** "868,335 vs its own component sum 868,336" is real but not literally
  r27's: 868,336 is not printed anywhere in the held carriers (`grep -r "868,336" corporate_print/` → 0 hits); it is
  the **sum of three segment rows in the same report** against the printed Net Retail Sales line. The residual is
  recorded with that description, and the row's value was **not** changed to the component sum.
* **(g) The pooled percentage.** The brief gives **23.84%** for 189,515,025 / 795,243,000. Computed to four places
  it is **23.8311%**, i.e. 23.83%. The register and §E.2 carry 23.83%; COR-09 keeps 23.84% visible as the superseded
  figure with the recomputation named, so the arithmetic trail survives.
* **(h) No year-end was inferred.** FY1970 and FY1971 days stay UNKNOWN with a FETCH REQUEST rather than being
  filled by the Saturday-closest-to-January-31 rule (which is printed only from FY1974 back to… precisely: the rule
  is printed in the FY1975 layer and cannot be retro-applied to FY1970 without a carrier).
* **(i) Confidence was moved down, not up.** r58/r59 stayed `Low` and §K.3's `Medium` was corrected to match, and
  the six new component rows are capped at `Medium` where their layer is UNVERIFIED-TLS (FY1966, FY1967, FY1971 —
  U.028). No row was raised to a level the carriers do not support merely to agree with prose.
* **(j) `budget` was not "fixed".** The volume is 38,489 words against a 22,000-word core planning figure. RD-122
  ruled the cap a dispatch budget and forbids trimming evidence; adding evidence was the job here. Named so the
  certifier is not surprised by a finding this pass deliberately did not cure.

---

## 6. Register row counts, before and after

| register | before | after | change |
|---|---|---|---|
| `sources.csv` | 21 × 18 | 21 × 18 | **not owned by this pass**; 1 outbound correction queued (COR-13) |
| `quantitative.csv` | 61 × 12 | **68 × 12** | +7: six COR-09 components + one COR-12 printed total. 0 rows deleted; 1 value re-precisioned (r15), 7 classes moved to DERIVED, 7 dates re-dated, 21 rows newly tagged |
| `timeline.csv` | 24 × 11 | 24 × 11 | ±0; row 17 re-pointed S4201→S4211 and re-classed, row 23 re-dated |
| `conflicts.csv` | 18 × 15 | 18 × 15 | ±0; U.011 carries the COR-07/COR-08 retraction and its residual is partly closed |
| `data_gaps.csv` | 22 × 8 | 22 × 8 | ±0; U.019/U.024 re-scoped, U.031 tagged, U.030 carries the FETCH REQUEST |
| `decisions.csv` / `validation.csv` / `failures.csv` / `channels.csv` | 3 / 4 / 1 / 3 | unchanged | read; no named defect lived there |
| **nine registers** | **157** | **164** | +7, all in `quantitative.csv` |

`stage_1.md` 37,507 → 38,489 words (255,104 → 261,590 B); `stage_1_index.md` 850 → 1,243;
`CORRECTIONS.md` 1,246 → 4,131; `_MANIFEST.md` 1,145 → updated with this pass. **`_MANIFEST.md` and
`stage_1_index.md` both state the +7 and where each added row came from**, as required.

---

## 7. Residual, for the certifier

1. Two `UNKNOWN` year-end days (FY1970, FY1971) with a FETCH REQUEST on U.030 — closable by script, not by reading.
2. The `989,225` residual between the two notes-page expense categories and the printed deduction total: named, not
   explained. No held carrier accounts for it.
3. Two restatement deltas newly visible in the register (FY1966 217,961,635 vs 220,511,038; FY1971 1,086.4m vs
   1,088,338,000) with no mechanism in print.
4. The `P2S01` id collision is now *described* in §T.2 and §T.1, but the emission blocks still contain both
   readings; only the sources agent's `sources.csv` and a re-census can retire the local id outright.
5. `budget` at `--tier core` will fire on `stage_1.md` (38,489 > 22,000), by the reasoning in §5.j.
6. The independence ledger's deeper problem is untouched by this pass and unchanged: one uploader's item supplies
   every corporate layer, so S4215 remains the only independent in-window carrier, and it does not name the company.
