# Target (company_042) Stage 1 — AUDIT 1: chronology and hindsight

Auditor: `target-s1-audit1`. Date of pass: 2026-09-26. Target: `founders_playbook/01_companies/company_042_target/stage_1.md`
(37,507 w, merged single volume, 9 registers / 157 rows, 37 declared `U.nnn` anchors) plus `timeline.csv`,
`quantitative.csv`, `sources.csv`, `conflicts.csv`, `CORRECTIONS.md`, `_parts/s1_p1.md`, `_parts/s1_p2.md`,
`research/A_chronology_feasibility.md`, `research/B1_dayton_print_records.md` and the 17 held source documents
under `sources/`. Method basis: `00_METHOD_AND_STYLE.md` §2, §3 (incl. the filing-lineage rule), §6, §13, §14
(rules 8, 10, 12), §15.3, §15.5, §15.6.

**Nothing here was repaired.** No file outside this one was created, edited or deleted; no register, no
`stage_1.md`, no `CORRECTIONS.md`, nothing under `tools/`.

**Severity scale used below:** BLOCKING (a written statement that its own cited carrier refutes, sitting in the
instruction or corrections layer) · HIGH (false date/class that propagates into a register or a second file) ·
MEDIUM (internal contradiction between the volume's own stated rule and its registers/prose) · LOW (locator,
vocabulary or wording defect; no value moves).

**Locators.** Per §14 rule 12 every defect is addressed by a stable label (§-anchor, claim-record id, register
row key); the `file:line` figure beside it is a convenience locator only and will drift on the next edit.

---

## Gate result (run before writing anything)

```
python tools/gates.py --company-dir founders_playbook/01_companies/company_042_target \
  --checks csv,keys,anchors,budget,corrections --tier core --fail-on substantive
```

Reported: **Findings: 1 | Passes: 20**, exit 0. The single finding is
`budget | stage_1.md | 37507 words > core cap 22000 (split required)` — the KNOWN, ADJUDICATED non-defect
(RD-122: the T2 cap is a dispatch budget, not a limit on written evidence). Not re-reported here as a defect and
not touched. **Every one of the five requested checks ran** (`csv` 14 passes incl. all `source_id` resolutions,
`keys` 2, `anchors` 6 incl. 37↔37 parity, `budget` 2, `corrections` 1 pass with 6 retraction ids reaching
registers 6 / volumes 6); **no check reported DID NOT RUN**, so there is no gate failure to escalate.
Advisory lines, recorded not disputed: `41 id(s) read as backticked references or range endpoints, not
citations`; `3 prose mention(s) match no declared entry, ADVISORY only: U.2, U.3, U.4`.

**Gate blind spot this audit exploited:** `csv` polices column count, stage vocabulary, year-bearing date
columns and `source_id` resolution. It does not read the *content* of a `date` cell against the carrier, nor the
`evidence_class` / `PERIOD BASIS` cells. CH-1, CH-2, CH-3, CH-4 and HS-2 are all invisible to `gates.py` by
construction; each is a semantic check a script cannot make, which is what §15.1 assigns to an auditor.

---

## Chronology defects

### CH-1 — BLOCKING. A false "31-December year-end / basis migration" claim, built on a context-stripped line, sits in the boundary argument, the timeline register, `conflicts.csv` U.011 and `CORRECTIONS.md`

- **Where.** §Boundary 4 table, `stage_1.md:220` (row `FY1975 | FOR THE YEAR ENDED DECEMBER 31, 1975`, under the
  column head *"What it prints for its own year-end"*); the ruling drawn from it at `stage_1.md:226-227`
  ("(b) the FY1969 layer marks the **change to a December-terminating presentation by FY1975**, so a series that
  spans FY1974→FY1975 changes basis and must say so"); `timeline.csv:18` (row key `1975-12-31` / "The FY1975
  report prints a 31-December year-end against late-January or early-February year-ends in FY1965-FY1974",
  `evidence_class=FACT`, notes "basis migration inside the stage window") = the same row echoed in the volume at
  `stage_1.md:863`; the retained fold text of `conflicts.csv` U.011 ("…and the FY1974 to FY1975 leg changes
  basis"); and `CORRECTIONS.md:35` (COR-01's own consequences paragraph: "The FY1974→FY1975 leg migrates to a
  31-December year-end").
- **What is wrong.** No such migration exists anywhere in the held corpus, and the document that supposedly
  proves it refutes it. The string `FOR THE YEAR ENDED DECEMBER 31, 1975` is real — `sources/corporate_print/1975_dayton_hudson_djvu.txt:3583`
  — but its context, nine lines up, is `F. INVESTMENT iN JOINT VENTURES … Real Estate had partnership interests
  ranging from 25% to 75% in eleven joint ventures at January 31, 1976 … CONDENSED COMBINED RESULTS OF
  OPERATIONS` (L3571-3582): the calendar-year statements of **unconsolidated joint ventures**, not the
  Corporation's fiscal year. The same layer's accounting-policy note prints the opposite of the claim:
  `1975_dayton_hudson_djvu.txt:3246-3250` — "Fiscal Year. The Corporation's fiscal year ends on the Saturday
  closest to January 31. **Fiscal year 1975 ended on January 31, 1976; fiscal year 1974 ended on February 1,
  1975.**" The FY1974 layer repeats it: `1974_dayton_hudson_djvu.txt:2917-2922` ("fiscal year 1974 ended on
  February 1, 1975; fiscal year 1973 ended on February 2, 1974"), and the FY1975 layer's own five-year header
  block reads `1974 / 52 Weeks Ended Consolidated February 1, 1975` (L134-136). A `grep -c -i "december" `
  over the FY1975 layer returns 5, and the only `December 31, 1975` prints in the whole `sources/` tree are
  L3583 and L3604, both inside that joint-venture note (`grep -rn -i -E "december 31,? 1975" sources/`).
- **Second defect in the same row.** `timeline.csv:18`'s `source_id` is **S4201** — the FY1965 report — for a
  claim about the FY1974 and FY1975 layers. The FY1975 layer is S4211 (`sources.csv:12`). The row's own note
  admits the reading was only "at probe level", i.e. the row asserts a fact about a document it did not open at
  merge.
- **What the auditor found already on disk and unused.** The printed policy key that settles the whole question
  is cited **nowhere** in the volume (`grep -n -c "approximately January 31" stage_1.md` → **0**):
  `1967_dayton_hudson_djvu.txt:1525` "Fiscal years ended approximately January 31 of following year.";
  `1969_dayton_hudson_djvu.txt:1953` and `1970_dayton_hudson_djvu.txt:2462` "Fiscal years end on approximately
  January 31 of the year following."; plus the two FY1974/FY1975 notes above. Had §Boundary 4 used these, U.011's
  residual ("FY1968 onward was not tested for the same pattern by this pass") would have closed and CH-1 not
  arisen. COR-01's *other* dates check out and are not disputed: `FY1967 ends 1968-02-03` is printed at
  `1967_dayton_hudson_djvu.txt:1178` and `:1195`; `FY1965 ends 1966-01-29` at `1965_dayton_hudson_djvu.txt:170`.
- **Consequence.** COR-01 is the volume's flagship retraction and it is correct in one direction and wrong in the
  other: it retracts "fiscal = calendar" and then installs "FY1975 = calendar-year", which its carrier refutes.
  Per §14 rule 10 the instruction layer (`CORRECTIONS.md`, the merge note at `stage_1.md:36-39`) is the
  highest-severity home for a stale claim, and the register layer (`timeline.csv:18`, `conflicts.csv` U.011) is
  where a downstream Stage-2 agent will read it. Any Stage-2 series built on this row will insert a denominator
  break that does not exist.

### CH-2 — HIGH. Seven quantitative rows are dated to a 31-December period end that the carriers and §Boundary 4's own ruling refute — COR-01's defect class surviving COR-01

- **Where.** `quantitative.csv` row keys by metric: `low_margin_group_total_square_feet`,
  `low_margin_group_sales_per_square_foot`, `low_margin_group_pretax_margin_pct_of_sales`,
  `low_margin_group_sales_per_sqft_change_1969_to_1973` — all four `date=1973-12-31` (lines 55-58);
  `low_margin_group_revenue_per_store_1969` `date=1969-12-31` (line 59);
  `low_margin_group_revenue_per_store_1972` `date=1972-12-31` (line 60); `target_store_area_1962_openings`
  `date=1962-12-31` (line 61). Count produced by:
  `python -c "…re.fullmatch(r'19\d\d-12-31', r['date'])…" → rows dated NNYY-12-31: 7`.
- **What is wrong.** Every one is a fiscal-year value taken from the FY1973 five-year block
  (`1973_dayton_hudson_djvu.txt:3970-3997`, columns headed `1973 1972 1971 1970 1969`, balance-sheet heads at
  L174 `February 2, 1974 February 3, 1973`). The printed period ends are **1974-02-02** (FY1973), **1973-02-03**
  (FY1972) and **1970-01-31** (FY1969, per `1970_dayton_hudson_djvu.txt:1715` "January 30, 1971 and January 31,
  1970"). December 31 is a *Sunday* in 1973 and cannot be a "Saturday closest to January 31" year-end in any of
  these years. The `1962-12-31` row is refuted by the volume's own rule rather than by a line: §Boundary 4
  ruling (a) (`stage_1.md:225-226`) states in terms that year-end figures are "a count **at a late-January date
  in the following calendar year**, not a 31-December count".
- **Carrier that fails to support.** None of the seven rows' `source` cells prints a 31-December date; the rows
  inherit the date from the *label* on the column, which is exactly the inference COR-01 exists to forbid.
- **Secondary inconsistency.** The prose version of the same block (§P.2 rows Q38-Q42, `stage_1.md:1479-1483`)
  dates these rows `1969-01/1973`, `1969→1973` and `1962` — three further forms, and `1969-01/1973` is not an ISO
  partial date under §13 ("partial dates use `1995-07` or `1995`"). One printed table, six date formats across
  prose and register.

### CH-3 — HIGH. COR-01's propagation claim is false on its own register: 21 of the 36 bare-year quantitative rows carry no `PERIOD BASIS` designation

- **Where.** `CORRECTIONS.md:33` ("Every quantitative row whose `date` is a bare year was re-tagged
  `PERIOD BASIS: CONTEMPORANEOUS|RESTATED` against the printing layer") and the merge note `stage_1.md:38-39`
  ("37 quantitative rows gained an explicit PERIOD BASIS … designation").
- **What is wrong — the command and its output.**
  ```
  $ python -c "import csv,re; rows=list(csv.DictReader(open('quantitative.csv',encoding='utf-8')))
      bare=[r for r in rows if re.fullmatch(r'19\d\d',r['date'])]
      print(len(rows), len(bare), len([r for r in bare if 'PERIOD BASIS' not in r['notes']]))"
  61 36 21
  ```
  The 21 un-tagged bare-year rows are the whole `target_stores_in_operation` series (1962, 1965, 1966, 1967,
  1968, 1971, 1972), the whole `low_margin_group_revenue`/`_stores` series (1967, 1968, 1969, 1970, 1971, 1972,
  1973), `target_unit_sales` 1967, `parent_net_retail_sales` 1969,
  `department_store_group_revenue_as_restated` 1968 and `parent_net_retail_sales_growth_printed` 1965. (The 37
  in the merge note is the true count of `grep -c "PERIOD BASIS" quantitative.csv` — the note is accurate about
  how many rows were tagged and wrong about *which* rows.)
- **Why it matters.** The store-count series is the Stage-1 chronology. A bare `1966` in a register the volume
  has told readers to trust as re-based is exactly the "fiscal-year assumption asserted as a date" the brief
  asks me to hunt.
- **Also failing: §P.1's own universal.** `stage_1.md:1451-1453`: "every row below from a cover-labelled '1965'
  report carries the **fiscal period end** in its `Date` cell (`1966-01-29`)" — Q35 and Q36 (`stage_1.md:1480-
  1481`) carry `FY1965`, and their register twins `target_unit_sales_growth_rate` (`quantitative.csv:4`) and
  `target_unit_pretax_profit_growth_rate` (`:52`) carry bare `1965`. MEDIUM in itself; folded here because it is
  the same class of over-claimed propagation.

### CH-4 — MEDIUM. The CONTEMPORANEOUS/RESTATED tag is applied backwards for prior-year *comparative columns* (three instances), so the 61-row tag set is not internally consistent

- **Instance 1 (clearest).** `quantitative.csv:18` `1967 | low_margin_group_revenue | 141,824,116 | S4204 L1361`
  tagged `CONTEMPORANEOUS for 1967 as printed in the FY1968 report`. The carrier prints the figure in the
  **prior-year column** — `sources/corporate_print/1968_dayton_hudson_djvu.txt:1356-1361`: "Retail sales by
  operating groups for 1968 and 1967 were as follows: … `1968 1967 Over 1967` … `Discount and Hard Goods Stores
  189,515,025 44 141,824,116 38 33.6`". Line 19 of the register cites **the same table line** for the current-year
  column and calls it CONTEMPORANEOUS, which is right; one of the two must be RESTATED. The volume's own usage
  elsewhere settles which: `quantitative.csv:20` ("RESTATED (1968 inside a 1972 recap)"), `:22` ("RESTATED (1973
  recap of 1970)"), `:53` ("RESTATED (the layer labelled 1965 prints a figure for fiscal year 1964)"), `:62`
  (same). Contributing cause: `sources.csv:5` gives S4204 an unsplit `CONTEMPORANEOUS` evidence_class while
  S4205/S4208/S4209 (`sources.csv:6,9,10`) all split theirs.
- **Instance 2.** `quantitative.csv:23` `1971 | low_margin_group_revenue | 345.8 | S4208 L1040` —
  "CONTEMPORANEOUS-as-1971 via the FY1972 report". Same relationship (prior-year column of the next layer),
  same mis-tag.
- **Instance 3.** `quantitative.csv:40` vs `quantitative.csv:62` date and tag **one fiscal period** two ways: the
  FY1965 layer's comparative column (year ended 1965-01-30) is `date=1965-01-30 / CONTEMPORANEOUS` at line 40 and
  `date=1964 / RESTATED` at line 62.
- **Severity rationale.** These are the tags a Stage-2 agent will filter on; a row that says CONTEMPORANEOUS for
  a comparative column teaches the next pass to treat recap digits as observations, which is §3's cardinal
  prohibition.

### CH-5 — MEDIUM. One printed sentence is dated four different ways across the volume

- **The sentence.** `Total retail area of the seven Target stores now in operation is 889,000 square feet.` —
  carrier `sources/corporate_print/1966_dayton_hudson_djvu.txt:219`, inside a layer whose fiscal period ended
  **1967-01-28** (printed at `1966_dayton_hudson_djvu.txt:320` and `:1197` of the following layer; the volume
  itself quotes "during the fiscal year ended January 28, 1967" in U.011 at `stage_1.md:1820`).
- **The four dates.** §P.2 Q37 (`stage_1.md:1482`) `Date = 1966-01-29` while the same row's Source-date cell
  says `1967 (cover 1966)` — internally contradictory in one table row; `quantitative.csv:5` and `:54`
  `1967-01-28` (correct); `quantitative.csv:9` bare `1966` (the store-count row for the same seven units);
  §Q `stage_1.md:1520` `1966-10 +`. Two of the four are refuted by the carrier; the register disagrees with
  itself on whether this is 1966 or 1967-01-28.
- **Carrier that fails to support.** No held document dates the seven-store statement 1966-01-29; that is the
  FY1965 layer's period end, i.e. the previous report's closing date.

### CH-6 — MEDIUM. The `(PB)` post-boundary marker the volume says it applies "wherever it is used" is absent from 12 of 19 post-boundary register rows

- **The rule.** `stage_1.md:84`: "Post-boundary material is tagged `(PB)` wherever it is used"; restated at
  `stage_1.md:1501-1502` for §Q.
- **The counts (command shown).**
  ```
  $ python -c "csv.DictReader over timeline.csv and quantitative.csv, regex (19\d\d) on the date cell,
      rows with year > 1969, test for literal '(PB)' anywhere in the row"
  timeline.csv     rows dated >1969: 6   of which carry (PB): 2   → untagged: 1971, 1972, 1971-04-16, 1975-12-31
  quantitative.csv rows dated >1969: 13  of which carry (PB): 5   → untagged: 1970, 1971, 1972 (revenue),
                                                                    1970, 1971, 1972, 1973 (group revenue), 1972 (stores)
  ```
- **What is wrong.** The Stage-1 boundary is argued at `stage_1.md:270` as the 1969 name changeover. Twelve rows
  dated 1970-1975 sit in registers whose `stage` column reads `stage1` with no marker, while §Q tags the
  identical facts `(PB)` (`stage_1.md:1528-1531`). A register consumer (any `stage==stage1` filter, which is what
  §13's fixed stage vocabulary exists to enable) will read 1970-1975 evidence as in-window; the prose does not
  have this problem, so the divergence is register-side. `timeline.csv:12` (1969-09-08 NYSE) is correctly inside
  the window and is not counted here.

### CH-7 — LOW. `timeline.csv:2` and §Q disagree on the date of the disclosure decision, and the more precise of the two has no carrier

- **Where.** `timeline.csv:2` `date_or_range=1966`; §Q `stage_1.md:1517` `1966-02` for the same event, with the
  gloss "dated by the document that is itself that report".
- **Carrier that fails to support.** The FY1965 opening letter (`1965_dayton_hudson_djvu.txt:155-166`, source of
  `we are issuing our first public Annual Report`) prints no date line; the only `February 1966` prints in that
  layer are the annual meeting (`:1056`, `:1058`) and a receivables resale (`:1358`), neither of which dates the
  letter. The §Q column is headed "Date (as held)", so a derived month presented in it is a drift, and it drifts
  against the register. The register's `1966` is the defensible value; §Q's `1966-02` should be labelled inferred
  or dropped.
- **Note (not a defect).** The same row's `conflict_ref` moved from `U.011` (pre-merge, `_parts/s1_p1.md`) to
  `U.017` (merged); U.017 is the right key ("first public annual report while private" vs "first public stock
  offering late 1967"), so the re-key is an improvement and is recorded only because it is a silent register
  edit.

### CH-8 — LOW. §Boundary 4's FY1970 cell puts a prior-year date in a column headed "its own year-end", and the cited locator prints something else

- **Where.** `stage_1.md:219` row `FY1970 / FY1971 / FY1974 | For the year ended January 31, 1970; During the
  year ended January 29, 1972; the year ended February 1, 1975`; register locator list at `stage_1.md:902` and
  `conflicts.csv` U.011 fold text: "held layers … FY1970 **L1743** …".
- **What is wrong.** `January 31, 1970` is the FY1969 period end (the FY1970 layer's own year ended `January 30,
  1971`); the quote is genuine but sits at `1970_dayton_hudson_djvu.txt:1831`, not 1743 — L1743 reads "During the
  year ended **January 30, 1971** three", which supports the ruling and contradicts the cell. The FY1971 and
  FY1974 items are correct as printed (`1971_dayton_hudson_djvu.txt:1880`; `1974_dayton_hudson_djvu.txt:2921`).
  Knock-on: the confidence claim at `stage_1.md:230-231` ("five printed year-end dates in four layers") is
  inflated — one of the five is CH-1's joint-venture line and a second is a prior-year column.
- **No value moves**, but this is the table the whole year-basis ruling is sold on.

### CH-9 — LOW. Two superlative/anchor wordings need a perimeter tightened

- `stage_1.md:1120` (§J.1): "This is the earliest held date **in the entire corpus** attached to any operating
  act" for `1966-01-15` (Dayton Credit Company). The same fact's register row, `timeline.csv:21`, states the
  narrower and correct perimeter — "anywhere in the **held** corpus". "The entire corpus" is a claim about the
  archive, not about these 17 documents. Fix is a word.
- `stage_1.md:116-117`, `:335`, §A.1 and §H.2 say the one in-window independent carrier "does not name the
  company once". True of The Dayton Company and Target Stores, Inc. — the layer does print
  `J. L. HUDSON REAL ESTATE CO.` (`sources/periodicals_csa_1963/Chain_store_age_Steel_for_Stores_djvu.txt:5619`),
  the Detroit company that merges into the stage-window entity at 1969-09-08 (`timeline.csv:12`). Recommend
  "does not name The Dayton Company or Target Stores once" so the sentence is not re-read as a claim about the
  later corporation. I re-ran §H.2's own counts and every one holds exactly (see Sweep counts), so this is a
  wording precision issue, not a false null.

### Chronology checks that PASSED (named so the next reader knows they were tested)

Carrier-real and correctly dated in the volume: the 1962 Roseville sentence "Since the first Target store was
opened early in 1962 in Roseville, a suburb north of St. Paul" (`1965_dayton_hudson_djvu.txt:397-398`); the
entry sentence `The Company entered the discount merchandising field in 1962 with Target Stores, Inc., which now
has five stores…` (`:124-126`) — including COR-03's whole point: `Brookdale shopping center in 1962` is at
`:122-123`, one line above, and is Dayton Development Company's centre, so the mis-citation trap is real and the
timeline row that forbids it (`timeline.csv:16`) is right; the four 1962 rows of the chronology spread
(`:725-738`, incl. `KNOLLWOOD, ST.LOUIS PARK / MINNESOTA 1962` and `BLOOMINGTON, MINNESOTA 1965` at `:741`); the
five-store sentence `This brought the total number of Target stores to five` (`:189`); the subsidiary officers
(`:1453-1456`); the FY1966 store list with `St. Louis Park` spelled with a space (`1966_dayton_hudson_djvu.txt:216`),
which is the transcription claim §A.2 makes; `Target's sales were $86,901,007, an in-crease of 43 percent`
(`1967_dayton_hudson_djvu.txt:769-770`); `When the Corporation made its first public stock offering in late 1967,
it had 23 stores in five states` (`1970_dayton_hudson_djvu.txt:209-211`); the FY1974 roster `Roseville, Minn. 68
1962 … Knollwood, St. Louis Park, Minn. 106 1962` under the heading `Target (1967)*` (`1974_dayton_hudson_djvu.txt:4632-4641`,
which is U.009's both-sides carrier); and `Target has grown from 11 stores to 46 stores in five years`
(`1973_dayton_hudson_djvu.txt:565-566`). Stage-window placement inside 1962-1969 is otherwise clean, the FY1969
boundary is argued from mastheads and not from a calendar day, and no date anywhere in the volume is asserted
from an *unstated* fiscal assumption except those named in CH-1/CH-2.

STATUS: WRITTEN 2026-09-26 — 9 defects (CH-1…CH-9) + the tested-and-passed list.

---

## Hindsight leaks

The firewall itself is the strongest part of this volume and says so in its own header: the entity is written as
**"The Dayton Company at FY1965 narrating 1962"**, the volume explicitly refuses "Target (1962)"
(`stage_1.md:74-77`), the FY1999 genealogy spread is admitted only as evidence that the company told the story in
1999 (`:91-93`, and record B04), and §A.1's own table rule is "no value is 'Target's'". The 1972-03-22 date
inherited in the dispatch brief — a Walmart fact, per RD-123 — was grepped to zero and refused rather than
written (COR-02 / `conflicts.csv` K16), which is the correct handling of the corpus's worst cross-company leak
class. I found **no** instance of the modern brand, the later scale of the chain, or 1990s-2020s identity
knowledge inside contemporaneous narrative (sweep in the next section). The defects below are **class-label**
leaks, not narrative leaks: places where the volume's own hindsight machinery contradicts itself.

### HS-1 — MEDIUM-HIGH. The 1967 offering is carried as `FACT · High` off a 1971-dated restatement, against the rule the volume states for itself

- **Where.** §Q `stage_1.md:1524`: `| 1967-late | First public stock offering: it had 23 stores in five states
  (corporation level, printed in the FY1970 report; month UNKNOWN) | FACT · High · B1S06 |`; `timeline.csv:9`
  same event, `evidence_class=FACT`, `confidence=High`; claim record B05 `stage_1.md:479` `Class: FACT … Conf:
  High`.
- **The rule it breaks.** `stage_1.md:117-119`: "**no retrospective recap carries a FACT about a decision in this
  volume.** Recaps carry FACT-about-the-printing and RETROSPECTIVE INTERPRETATION-about-the-event, in two
  separate records, always." And the confidence scale at `stage_1.md:105-108`: High requires "2+ independent
  origins or a primary document **for its own year**"; "a retrospective-only primary" is the definition of Medium.
- **The carrier.** `1970_dayton_hudson_djvu.txt:209-211`, in a layer that prints its own date line **April 16,
  1971** (`:200`) — so it is a primary document for 1970/1971 and a recap for 1967. `sources.csv:7` says exactly
  this: S4206 is `RESTATED for 1967; CONTEMPORANEOUS for 1970`.
- **The internal contradiction that makes it a defect and not a judgment call:** the *same* document reciting the
  *same* offering is tagged `RESTATED` one row away (`timeline.csv:17`, "a 1971-dated carrier for a 1967 and a
  1970 fact; RESTATED, so it is version evidence and never corroboration"). One fact, two registers rows, two
  classes, no conflict entry joining them.

### HS-2 — MEDIUM. `evidence_class` cells in the registers carry compound prose where §3/§13 expect one controlled literal

- **Where.** `timeline.csv:19` `evidence_class = "RETROSPECTIVE INTERPRETATION at three years' remove"`;
  `:24` `"RESTATED 1969-1972 / CONTEMPORANEOUS 1973"`; `:25` `"RESTATED roster"`; `quantitative.csv:61`
  `"FACT as printed"`; `:34` `"CONTEMPORARY OBSERVATION second-hand"`; `:52` `"FACT that it was printed; base
  UNKNOWN"`; claim record P2-10 (`stage_1.md:2101`) `Class: RESTATED for 1969-1972, CONTEMPORANEOUS for 1973`.
- **What is wrong.** The words are defensible in prose and are exactly what §6 wants; the *cells* are the
  machine-read layer, and the `csv` gate that polices `stage` does not police `evidence_class`. Any downstream
  equality filter on `RESTATED` / `CONTEMPORANEOUS` / `FACT` silently drops these rows — the same silent-drop
  failure §13's register-vocabulary note was written for ("a stage filter silently dropped rows"). The volume's
  own convention (`PERIOD BASIS: …` inside `notes`, e.g. `quantitative.csv:30`) shows the right shape: keep the
  literal in the column, put the qualifier in `notes`.
- **Related, lower.** `timeline.csv:16` `conflict_ref=K17` and `conflicts.csv` rows `K16`/`K17` are legal keys
  that resolve (the gate counts them among the 44), but the merge note at `stage_1.md:28-30` asserts "The
  registers cite exactly those 37 ids **and nothing else**" — refuted by `timeline.csv:16` and by the two K-row
  ids in `conflicts.csv`. And **U.006 has no register row of its own**: it exists as a narrative block
  (`stage_1.md:1760`), is cited twice by `sources.csv:17` (S4216), and survives in `conflicts.csv` only as the
  folded header "U.003 and U.006" of K3's row (`:4`). The merge note's partition claim ("U.001-U.017 in
  conflicts.csv") is false for that one id. LOW.

### HS-3 — LOW. §K.4 states the loss-carry-forward sentence as `FACT / High` with no period-basis qualifier that its own register row carries

- **Where.** `stage_1.md:1243-1249` (§K.4) — "Class **FACT**; confidence **High**" for `a substantial loss
  carry-forward available to Target Stores, Inc., in 1964`.
- **The contradicting cell.** `quantitative.csv:53` (`target_unit_loss_carryforward_available`) — `PERIOD BASIS:
  RESTATED (the layer labelled 1965 prints a figure for fiscal year 1964)`. The FY1965 layer is contemporary for
  its own period and retrospective for 1964; the prose picks one and the register picks the other for the same
  sentence. Prose-side fix only. (For the record: the sentence's *class* is fine — §Boundary/§K.4 is careful to
  say "the unit's earliest profitability statement in the corpus is a tax statement about losses", and it does
  not read the loss forward into 1962.)

### HS-4 — what I tested for and did NOT find

No use of "Target" for the parent in contemporaneous voice; `would become` **0**, `later known` **0**;
`eventual` and `largest discount` occur exactly **1** time each, both inside the same firewall sentence that
refuses the inference (`stage_1.md:88-90`, "…or Target's eventual position as the country's largest discount
chain as evidence that a 1962 decision was rational"); *visionary*, *prescient*, *destined* appear only inside the
§2 statement that records their refusal (`:94`). `bullseye`, `superstore`, `supercenter`, `2020s` occur **0**
times; `1990s` occurs **2** times (`:722`, `:1979`) and both are archive provenance — the mid-1990s floor of the
web-archive family — never a claim about the company. Every post-1969 scale figure in §Q and §R is
either `(PB)`-marked or corporation-level-labelled. The record-selection null required by §2 is present three
times (§Header `:97-104`, §C.2, §S.3) and §A.3 states the anti-hagiography test in the first person ("a story
about a future chain" — what the volume is **not**). §S/§A pass the RD-032 requirement.

STATUS: WRITTEN 2026-09-26 — 3 defects (HS-1…HS-3) + HS-4 negative result.

---

## Independence audit

The volume's 28 claim records are 16 in volume 1 (`A01-A04`, `B01-B05`, `D01`, `E01-E02`, `F01`, `G01`, `H01-H02`)
and 12 in the P2 block (`stage_1.md:2092-2103`). I extracted **every** `Corroboration:` cell (`grep -oE
"Corroboration: [^—]{0,90}" stage_1.md` → **27 cells for 28 records**; record B02 fills the slot with the sentence
"extends inherited N3 from six layers to eleven" instead of a count, a LOW instance of HS-2). Of the 27: **22
record 0 independent, 2 record `n/a`, 1 is prose (B02), and only 2 assert a non-zero count — B05 `1 lineage` and
P2-02 `1`**, both below. So 24 of 27 cells honour the §3 filing-lineage rule (22 × `0 independent`, 2 × `n/a` at A04 `stage_1.md:350` and
H01 `:805`); the remaining 3 are B02's prose, B05's and P2-02's counts. This is better than the Amazon precedent
that produced RD-097/RD-123. The two non-zero cells fail.

### IN-1 — HIGH. The volume's own independence ledger names a company filing as its only independent source

- **Where.** §T.2, `stage_1.md:1644-1653`: "`P2S01` is the only held document of independent origin that touches
  the period, and its independent content about this company is empty (`U.019`)."
- **What `P2S01` is.** `stage_1.md:2119` (the emission block): `P2S01,stage1,P2-08 U.012,Q 'The Dayton Company'
  Annual Report 1966 (OCR text layer),The Dayton Company,corporate stockholder report,primary,…` — folded into
  global **S4202** at merge, whose `sources.csv:3` `independence_note` reads "same lineage as S4201 - one source
  however many report years". It is the parent's own next-year report.
- **The correct referent.** **P1S05 / S4215**, *Chain Store Age — Steel for Stores*, April 1963
  (`sources/periodicals_csa_1963/Chain_store_age_Steel_for_Stores_djvu.txt`), whose `sources.csv:16` note says
  "THE ONLY INDEPENDENT IN-WINDOW CARRIER HELD" — and §H.2 (`stage_1.md:724-740`) gets it right. So the volume
  states the correct fact in §H.2 and the wrong one in §T.2, and the wrong one is in the section whose entire
  function is the §3 filing-lineage rule. A Stage-2 agent reading §T.2 alone would count a company report as a
  second origin and could promote a Medium single-lineage claim to High.
- **Severity.** HIGH for a ledger entry: it is the file's independence authority, and it is inverted.

### IN-2 — MEDIUM. P2-02 asserts `Corroboration: 1` with no second source in evidence

- **Where.** `stage_1.md:2093`: claim "At the moment of the first public annual report the company described
  itself as privately owned and the report as its first public one" — `Source: The Dayton Company Annual Report
  1965, opening letter … Conf: High — Corroboration: 1`.
- **What is wrong.** The only carrier named is one document, and the claim is a self-description inside it. The
  only candidate for a second origin in the corpus is the FY1970 recap that U.017 sets against it — same lineage,
  and the volume says so itself (`sources.csv:7`: "a 1971-dated carrier reciting 1967 is one lineage"). The **same
  proposition** at record A01 (`stage_1.md:341`) records "Corroboration: **0** independent (company
  self-account)". Two records, one fact, contradictory corroboration — and the one that inflates it is the one in
  the §I-U appendix a reader trusts for §L/§N material. This is the RD-097 shape: an un-named second slot filled
  by a reiteration.

### IN-3 — MEDIUM. B05 fills the independence slot with a *lineage count* and keeps `Conf: High`

- **Where.** `stage_1.md:479`: "Corroboration: **1 lineage**"; the record's own Source cell lists two carriers,
  "FY1965 report L159-166; FY1970 report L209-212"; Class `FACT (corporation level)`; Conf `High`.
- **What is wrong.** §7 fixes the slot as `Corroboration: <n independent>`; "1 lineage" is not a count of
  independent origins, it is a statement that there is one. Combined with HS-1, half of this claim (the 1967
  offering leg) rests on the FY1970 restatement and the record is graded High on a scale that reserves High for a
  primary *of its own year*. Fix is mechanical: `Corroboration: 0 independent (two layers of one lineage)` +
  `Conf: Medium`, and split the record into FACT-about-printing / RETROSPECTIVE-interpretation-about-the-act per
  the volume's own rule at `stage_1.md:117-119`.

### IN-4 — LOW-MEDIUM. `sources.csv:18` (S4217) carries two opposite independence notes in one cell

- `independence_note = "independent of the company"` while the same cell's folded P1S07 text says "the
  registrant's **own** index; it cannot witness anything before its own floor". Both are true of different
  propositions (the SEC is a third-party carrier of the *index*; the filing dates and `formerNames` are the
  registrant's own acts). The row supports U.003/U.007 at `confidence: High`. Recommend the note be split by
  proposition, because as written a reader can take "independent of the company" as independent evidence *about*
  the company — which is the exact error RD-123 recorded when an index entry was read as a fact.

### IN-5 — independence work that held up (so the next auditor does not redo it)

- Single-lineage discipline is stated once and then, almost everywhere, kept: `stage_1.md:109-119` (eleven
  consecutive reports from one digitised item, one uploader, plus three later layers from the same item);
  `sources.csv:2` "FY1973, FY1974 and FY1999 re-narrate the same self-account, which is version evidence not
  corroboration"; `quantitative.csv:19` "reprinted unchanged … - same lineage restated, never corroboration";
  `:28` "the FY1970 re-print of the same 1969 figure is one source repeated, not corroboration"; `:29`, `:23`,
  `conflicts.csv` U.008 ("both are company print of one lineage so neither corroborates the other") and U.010
  ("RESTATED is never corroboration of CONTEMPORANEOUS"). A03's "the FY1974 roster repeats the same lineage",
  B01's "FY1966/FY1967 re-listings are the same lineage" and B04's "the FY1999 spread is the same lineage" are
  correct calls.
- **Verbatim re-reads (11 passages, all printed as quoted).** A01/B05/P2-01/P2-02 → `1965_…:159-173`, `:599-601`;
  B03 → `:388-394`; B01 → `:1453-1456`; P2-03 → `:178-181`; P2-08 → `1966_…:219`; §H.2's quotation →
  CSA `:4475-4479`; P2-09 → `1974_…:4636-4641`; P2-10 → `1973_…:3988-3997`; B05 side B → `1970_…:209-211`.
  One drift: B01/A.1 give `JOHN GEISSE` (FY1965) and P2/B.2 give `JOHN F. GEISSE` (FY1967) — both are as printed;
  no defect.
- The two not-held web leads (S4213 obituary, S4214 biography pages) are correctly ring-fenced: `sources.csv:14-15`
  mark them `NOT HELD so it cannot be evidence - a named assertion only`, and no record I opened counts either as
  corroboration; U.001 keeps both founder sides unscored with no averaging.
- **All §H.2 null counts re-ran exactly** (see Sweep counts), as did B02's Geisse count and U.002's
  month-with-1962 zero.

STATUS: WRITTEN 2026-09-26 — 4 defects (IN-1…IN-4) + IN-5 the independence checks that held; 20 of 28 records
read in full (A01-A03, B01-B05, P2-01…P2-12), all 27 corroboration cells extracted, 11 verbatim passages re-read
in the carriers.

---

## Sweep counts

**Files in scope.** `find . -type f` under `company_042_target/` → **68 files**, of which **17** are held source
documents under `sources/` (`corporate_print` 11 layers + 11 `.meta.json` sidecars not counted separately,
`periodicals_csa_1963` 1, `ia_search`, `name_search`, `web_archive`, `sec`, `_index`).

**Fully read (7):** `stage_1.md` (targeted reads of ~700 of 2,222 lines, plus whole-file greps), `CORRECTIONS.md`,
`timeline.csv`, `quantitative.csv`, `sources.csv`, `conflicts.csv`, `00_METHOD_AND_STYLE.md`.
**Partially read (6):** `data_gaps.csv` (ids + 2 rows via python), `stage_1_index.md` (headings only via grep),
`_parts/s1_p1.md` and `_parts/s1_p2.md` (only the lines my greps surfaced: p1 `:175, :812, :851`; p2
`:1212-1232`), `research/A_chronology_feasibility.md` and `research/B1_dayton_print_records.md` (targeted greps
only — see "did NOT test").
**Carriers opened (11 of 17):** all eleven `corporate_print` layers 1965-1975 + the CSA 1963 layer. Not opened:
`1998/1999/2000` print layers, `ia_search/meta_01-target-archive.json`, `name_search/*.atom` and `fts_*.json`,
`web_archive/cdx_*.txt`, `sec/_MANIFEST.csv`, `_index/raw_submissions_CIK0000027419.json` (all five negative
artifacts and the metadata JSON were read only **through** `sources.csv`, not at source).

**Commands run, with results (so every count above is reproducible).**

| Test | Command (run in `company_042_target/`) | Result |
|---|---|---|
| period-basis coverage | `python -c` over `quantitative.csv` (rows / bare-year / bare-year without tag) | `61 36 21` |
| `PERIOD BASIS` literal | `grep -c "PERIOD BASIS" quantitative.csv` | 37 |
| December year-ends in register | `re.fullmatch(r'19\d\d-12-31', date)` | 7 rows (listed CH-2) |
| post-boundary `(PB)` | python, year >1969, literal `(PB)` in row | timeline 6 rows/2 tagged; quantitative 13/5 |
| claim records | `grep -cE "^[A-Z][0-9]{2} Claim:\|^P2-[0-9]{2} Claim:" stage_1.md` | 28 |
| corroboration cells | `grep -c "Corroboration:" stage_1.md` | 27 |
| FY1975 "December" | `grep -c -i december …/1975_dayton_hudson_djvu.txt`; `grep -rn -i -E "december 31,? 1975" sources/` | 5; 2 hits, both in Note F (L3583, L3604) |
| printed fiscal-year keys | `grep -n -i -E "(fiscal )?year (ended|ending)|December 31|January 3[01]|February [12]"` per layer | 11 layers; year-ends 1966-01-29 / 1967-01-28 / 1968-02-03 / 1969-01-31 / 1970-01-30 / 1971-01-29 / 1974-02-01 / 1975-01-31 |
| policy key present, unused | `grep -rn "approximately January 31" sources/corporate_print/*.txt`; `grep -n -c "approximately January 31" stage_1.md` | 3 carriers (1967:1525, 1969:1953, 1970:2462); **0** citations |
| §H.2 null counts | `grep -o -i <term> | wc -l` over the CSA layer, per term | target 0, goodfellow 0, minnesota 0, dayton 2, hudson 3, discount 14 — **all six match `sources.csv:16` exactly**; file 170,260 B (`ls -l`) |
| Geisse distribution | `for y in 1965..1975; grep -o -i geisse | wc -l` | 1 1 1 0 0 0 0 0 0 0 0 — matches record B02 |
| month-with-1962 | `grep -l -iE "(january|…|december)[a-z]*,? 1962" *.txt` | 0 files — matches U.002 |
| hindsight vocabulary | `grep -niE "would become\|eventual\|later known\|superstore\|bullseye\|national ranking\|largest discount\|1990s\|2020s\|destined\|prescient\|visionary\|the chain\|became Target" stage_1.md` (7 hits) then per-term `grep -o -i -F "$t" \| wc -l` | bullseye 0, superstore 0, supercenter 0, 2020s 0, would become 0, later known 0, eventual 1, largest discount 1, 1990s 2 (archive floor, not the company) — **0** leaks into narrative; the 7 grep lines are firewall text, the §Boundary geometry table, §G.1's generic "a chain of this era", verbatim 1966 print (`nationally advertised`) and the `(PB)` heading U.007 |
| anchor/id sweep | python over `timeline.csv` `conflict_ref`; `grep -c U.006 conflicts.csv data_gaps.csv` | refs = {K17, None, U.001…U.017}; U.006 → 1 in conflicts (folded header), 0 in data_gaps |
| 11-layer volume | `cat 1965..1975 layers | wc -c` | 786,383 B (vs U.002's "781995 chars" — the gap is consistent with UTF-8 multibyte, **not** a defect) |

**What I did NOT test (named, not silently skipped).**
1. `research/A_chronology_feasibility.md` and `research/B1_dayton_print_records.md` were **not read end to end** —
   I grepped them for the fiscal/calendar premise (found at `B1:74`, so COR-01's attribution is accurate), the
   Q20 money set (`B1:102`, `B1:275` — the emitted `date=1965` row COR-01 re-bases, confirmed), `1972-03-22` (0
   hits) and `1962-07-01` (`A:277`, `B1:211`, `B1:335` — both say no carrier, consistent with the volume).
   B1's Q1-Q19 rows as emitted were therefore **not** individually compared with the merged register.
2. I did **not** test the *arithmetic* of any figure (footings, ratios, the 889,000/722 area conflict, the
   −13.5% derivation) — that is audit 3's numbers remit. Where a derived row's arithmetic is right but its
   **date** is wrong (CH-2's `low_margin_group_*` rows) I flagged only the date.
3. I did **not** re-open the pre-merge `_parts/` files row by row: only the grep-surfaced lines. So I cannot say
   whether the merged registers changed any *other* cell besides the ones reported (CH-7's `conflict_ref` re-key
   is the one drift I confirmed).
4. I did **not** test the 4 `(PB)`-tagged 1970s rows for **stage-window placement of the right stage label** —
   i.e. whether 1970-1975 material should have been emitted as `stage2-consequence` per §13 rather than
   `stage1`+`(PB)`. That is a register-schema question for the merge owner; I tested only the stated `(PB)` rule.
5. Not tested: the three later print layers (1998/1999/2000), the 17 unopened Image Container PDFs (the volume
   itself records them UNTRIED at U.030), `validation.csv`/`failures.csv`/`channels.csv` (11 rows total, none
   bearing a date I was asked to check beyond those already covered via timeline).
6. `EMPTY / UNANSWERED / UNTRIED` — I did not re-run any network route, so I cannot confirm or refute the volume's
   503/zero-hit classifications (`sources.csv:19-22`, U.025-U.029). I read them as declared and did not convert
   any of them into a null of my own.
7. Not run: `gates.py --self-test` (§15.5) and the `verbat`/`quotes` checks, which are outside my `--checks`
   list — so the 39%-unmatched-quote advisory recorded in §15.6 is **not** cleared or confirmed by this audit.

STATUS: WRITTEN 2026-09-26 — 15 commands and their outputs. Files touched by this audit: 13 of the 68 prose/register
files (7 fully, 6 partially) plus 11 of the 17 held source layers opened to verify carriers.

---

## Untried

Routes I did not attempt in this pass, each with the exact command that would settle it. These are **UNTRIED**,
not nulls and not unanswered.

1. **Whether the FY1975 December lines were read out of context by the author or by the dossier** — i.e. whether
   `research/B1_dayton_print_records.md` or `_parts/s1_p1.md` is the origin of CH-1. `grep -n -i "december 31"
   research/*.md _parts/s1_p1.md` (I read `_parts/s1_p1.md:175` = the same sentence as merged, but did not grep
   the dossiers for the December premise).
2. **Whether any other register cell asserts a 31-December fiscal date that I did not catch** — my regex covered
   `quantitative.csv` and `timeline.csv` date cells only. `grep -n "12-31" validation.csv failures.csv
   channels.csv decisions.csv quantitative.csv timeline.csv`.
3. **Whether the 5 negative-artifact rows and `ia_search/meta_01-target-archive.json` support the run-floor claim
   (U.024)** — the JSON is on disk, unopened by me. `python -c` over
   `sources/ia_search/meta_01-target-archive.json` counting `djvu.txt` files and min year.
4. **Whether the 17 Image Container PDFs settle the OCR-corrupt roster basis (U.012) and the Target (1961)/(1967)
   contradiction (U.009)** — the volume lists both as U.030-UNTRIED and I did not fetch. Route:
   `archive.org/download/01-target-archive` PDF legs.
5. **The second carrier for the same years (U.034, `fund-and-stock-reports`)** and **local newspaper back-files
   (U.033)** — named by the volume as the only routes to a 1962 day; not attempted, zero web calls made in this
   pass (my brief's web budget was 0).
6. **Whether the merged register changed any date cell that the pre-merge parts held differently**, other than
   CH-7: `diff <(grep "^Target,stage1" _parts/s1_p1.md | cut -d, -f3) <(… timeline.csv)` — I did not build this
   diff because the parts carry dossier-local ids and the merge re-pointed 200 of them.

STATUS: WRITTEN 2026-09-26

---

## Summary for the orchestrator (nothing below is a new claim)

| id | one-line defect | severity |
|---|---|---|
| CH-1 | "FY1975 prints a 31-December year-end / basis migration" taken from an unconsolidated **joint-venture** note; the same layer's Fiscal Year note prints `FY1975 ended January 31, 1976` — reaches §Boundary 4, `timeline.csv:18`, U.011, COR-01, and the row cites S4201 for an FY1975 fact | BLOCKING |
| CH-2 | 7 quantitative rows dated `1973-12-31`/`1969-12-31`/`1972-12-31`/`1962-12-31` assert the calendar year-ends COR-01 exists to ban and §Boundary 4 ruling (a) forbids | HIGH |
| CH-3 | COR-01's "every bare-year row was re-tagged" is false for **21 of 36** bare-year rows (incl. the entire store-count series) | HIGH |
| CH-4 | Prior-year comparative columns tagged CONTEMPORANEOUS (`quantitative.csv:18, :23`) while the identical relationship is RESTATED at `:20, :22, :53, :62`; `:40` vs `:62` date one period two ways | MEDIUM |
| CH-5 | One FY1966 sentence dated four ways (`1966-01-29` §P.2 Q37 / `1967-01-28` / bare `1966` / `1966-10+` §Q) | MEDIUM |
| CH-6 | `(PB)` rule applied "wherever it is used" fails in 12 of 19 post-boundary register rows | MEDIUM |
| CH-7 | `timeline.csv:2` = `1966` vs §Q = `1966-02` for the disclosure decision; the letter prints no date line | LOW |
| CH-8 | §Boundary 4's FY1970 cell puts FY1969's period end in an "own year-end" column; cited locator (L1743) prints a different date | LOW |
| CH-9 | "entire corpus" perimeter wording at §J.1; "does not name the company once" needs narrowing to the Stage-1 entity | LOW |
| HS-1 | 1967 offering carried `FACT · High` off the FY1970/1971 restatement against the volume's own no-recap-for-a-decision rule; same event tagged RESTATED one row away | MEDIUM-HIGH |
| HS-2 | Compound prose in `evidence_class`/`Class` cells (4 rows + 1 record) that a §13 equality filter silently drops; "registers cite only the 37 ids" refuted by `K17`; U.006 has no register row | MEDIUM |
| HS-3 | §K.4 grades the 1964 loss-carry-forward sentence FACT/High with no RESTATED qualifier its own register row carries | LOW |
| IN-1 | §T.2 independence ledger names **P2S01 = the FY1966 company annual report** as "the only held document of independent origin"; the independent carrier is S4215 (*Chain Store Age* Apr 1963) | HIGH |
| IN-2 | P2-02 `Corroboration: 1` with no second source; A01 records 0 for the same proposition | MEDIUM |
| IN-3 | B05 `Corroboration: 1 lineage` + `Conf: High` on a claim half-carried by a restatement | MEDIUM |
| IN-4 | S4217 carries "independent of the company" and "the registrant's own index" in one cell | LOW-MEDIUM |

**Counts — 16 findings:** 1 BLOCKING (CH-1) · 3 HIGH (CH-2, CH-3, IN-1) · 1 MEDIUM-HIGH (HS-1) · 6 MEDIUM
(CH-4, CH-5, CH-6, HS-2, IN-2, IN-3) · 1 LOW-MEDIUM (IN-4) · 4 LOW (CH-7, CH-8, CH-9, HS-3); the U.006 /
`K17` anchor-partition item is recorded as a sub-finding of HS-2, and §P.1's failed universal as a sub-finding of
CH-3. Plus 3 named classes that PASSED (single-lineage discipline, verbatim-passage integrity,
hindsight-vocabulary firewall) and the gate's 1 adjudicated budget non-finding, which is not counted and was not
touched.
