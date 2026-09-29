# target_s1_certification.md — CERTIFIER, company_042_target Stage 1

Agent `target-s1-certify`. Independent pass over `founders_playbook/01_companies/company_042_target/`
after `03_quality_control/target_s1_merge.md` (RD-122), `target_s1_audit1_chronology_hindsight.md`,
`target_s1_audit2_sources_independence.md`, `target_s1_audit3_numbers.md`, RD-125, RD-127 and
`target_s1_repairs.md`. I wrote none of the volume, none of the registers, none of `CORRECTIONS.md`, and
performed no merge and no repair (§15.6: certifier ≠ author ≠ merge ≠ repair). Method read before writing:
`00_METHOD_AND_STYLE.md` §13, §14 rules 4/8/10/11/12, §15.2, §15.5, §15.6. **This file writes no corpus
file: it is a verdict with evidence and nothing else.**

## VERDICT: **NOT-CERTIFIED**

Five blockers, numbered below. The volume's mechanical state is clean and the repair report is, with two
exceptions, honest and accurate about what it did — **but the certifier found a held printed figure that
the register and four places in the volume affirmatively declare unprinted, in a carrier this volume
already cites for the adjacent year.** That is the §14 rule-8 defect class, and it is blocking.

The gate at `--tier core --fail-on substantive` exited **0** while carrying only the budget finding, and
it did not see any of the five blockers below. Recording that, not hiding it, is §15.5's point: a gate
that cannot catch its own historical defect is a bug in the gate. The `corrections` gate tests whether a
COR **id** appears in both layers; it cannot see that four repair-pass findings exist only in the
registers, nor that nine withdrawn-date rows still sit unmarked inside the canonical volume.

## GATE, quoted verbatim

Command run exactly as briefed:

```
python tools/gates.py --company-dir founders_playbook/01_companies/company_042_target --checks csv,keys,anchors,budget,corrections --tier core --fail-on substantive
```

```
# Mechanical gate report -- company_042_target

Findings: **1** | Passes: 20

| gate | subject | finding |
|---|---|---|
| budget | stage_1.md | 38489 words > core cap 22000 (split required) |

- coverage 9 registers, 2 stage volumes, 17 source documents
- anchors  stage_1.md declares an explicit ANCHORS set (37 ids)
- anchors  stage_1.md declares 37 anchors
- anchors  41 id(s) read as backticked references or range endpoints, not citations (U.0, U.001, U.002, U.003, U.004, U.005, U.006, U.007)
- anchors  3 prose mention(s) match no declared entry, ADVISORY only: U.2, U.3, U.4
- corrections 14 retraction ids; register layer reaches 14, volumes 14

## Passing checks

csv      timeline.csv 24 rows x 11 cols · quantitative.csv 68 rows x 12 cols · conflicts.csv 18 x 15 ·
sources.csv 21 x 18 · data_gaps.csv 22 x 8 · validation.csv 4 x 11 · failures.csv 1 x 11 ·
decisions.csv 3 x 15 · channels.csv 3 x 11 (all `S####` tokens resolve in the five files that carry them)
keys     stage_1.md 5 source tokens all resolve · stage_1_index.md 21 source tokens all resolve
anchors  citation resolution — every register-cited anchor resolves (44 distinct ids)
anchors  parity 37 narrative anchors <-> 37 register anchors
budget   stage_1_index.md 1243 words (cap 22000)
corrections propagation — all 14 retraction(s) reach registers and volumes
```

**Register arithmetic I re-measured, not inherited:** 24+68+18+21+22+4+1+3+3 = **164 rows across 9
registers** ✓ (matches the brief and the repair report's 157→164, +7 all in `quantitative.csv`).
**Anchors 37↔37** ✓. The single finding is `budget`, which RD-122 already ruled a dispatch budget: I do
not re-litigate it (see Check 5).

---

## Check 1 — DID THE REPAIRS ACTUALLY LAND? Measured: 6 of 6 landed; 1 landed partially; and the repair report's own claims check out.

Every measurement below was taken on the repaired bytes by parsing columns, not by grepping the file.

| defect the repair claimed | my independent measurement | verdict |
|---|---|---|
| seven December year-ends re-dated to carrier year-ends | `quantitative.csv.date` cells matching `-12-31`: **0**; `source_date`: **0**; `timeline.csv.date_or_range`: **0**. Live re-datings: r54-r57 → `1974-02-02`, r58 → `1970-01-31`, r59 → `1973-02-03`, r60 → `1975-02-01`; `timeline.csv` row 23 → `1974-02-02`. Superseded strings survive only inside `notes` retraction sentences: `1973-12-31` ×4, `1969-12-31`, `1972-12-31`, `1962-12-31` in `quantitative.csv` (7) + 1 in `timeline.csv` = **8**, exactly as reported | **LANDED** |
| the FY1973 layer prints the dates it was re-dated to | `sources/corporate_print/1973_dayton_hudson_djvu.txt` **L172-174**: `1973 1972 / : 52 Weeks Ended 53 Weeks Ended / Consolidated February 2, 1974 February 3, 1973` — opened, verbatim. r58's day from `1969_…` **L1488** `…at January 31, 1970, and $6,951,217 at February 1, 1969` ✓; r60's from `1974_…` **L147-148** `52 Weeks Ended … February 1, 1975 February 2, 1974` ✓ | **LANDED** |
| CH-1 basis-migration retraction quoting **L3246-3250** | `1975_dayton_hudson_djvu.txt` L3246-3251 prints the Fiscal Year note (`ends on the Saturday closest to January 31. Fiscal year 1975 ended on January 31, 1976; fiscal year 1974 ended on February 1, 1975. Each of these years consisted of 52 weeks.`). `timeline.csv` row 17 now reads date `1976-01-31`, `source_id` **S4211** (the FY1975 layer, `archived_url` confirmed), class `FACT (verbatim carrier note)`, Conf High, `conflict_ref` U.011, with the withdrawn migration wording retained in `notes` | **LANDED** (locator off by one at the tail — see B-5) |
| six dropped Q20 components now present | All six present in `quantitative.csv` **and** in `stage_1.md`. Carriers opened and confirmed: `217,961,635` 1966 L49/L323/L434 ✓; `260,173,514` 1967 L765/L819 ✓; **`434,132,744`** 1968 **L1251, L1349, L1363** ✓ (L1363 prints `$434,132,744 100% $369,984,044 100% 17.3%`); `945,306` 1970 L829 ✓; `1,086.4` 1971 L309 header/L312 ✓; `1,262,759,000` 1972 L10/L325/L939 ✓ | **LANDED** |
| r18's denominator named, not assumed | r18 (`1968 low_margin_group_revenue 189515025`) carries in its cell `189,515,025 / 434,132,744 = 43.65 percent` and the 23.83 percent pooled comparison; the new row r64 carries `THIS IS THE DENOMINATOR OF THE 44 PERCENT CLAIM IN r18`. §E.2 (stage_1.md:623) prints the same arithmetic as a new paragraph. 23.84 percent appears **0** times corpus-side — the recomputation to 23.83 was applied, and COR-09 keeps the superseded figure visible | **LANDED** |
| DERIVED classes where arithmetic produces the value | `evidence_class` census on the live file: **7 DERIVED**, **7/7 carry non-empty `derived_arithmetic`** (r4, r11, r12, r15, r57, r58, r59 as reported). The two deliberate `FACT` retentions verified: r2 (`7,128,981 / 5,435,205 = 1.3116 … foots`, prints its own value) and r30 (`class = FACT as printed; DERIVED as a check`). The seventh arithmetic-bearing FACT, r64, prints its own value at L1363 and its sum only foots the table — consistent with the stated rule, not a miss | **LANDED** |
| 21 bare-year rows re-tagged `PERIOD BASIS` (COR-01's un-applied leg) | bare-year rows (`date` = 4 digits): **38**, rows carrying a literal `PERIOD BASIS` tag: **38/38**. All rows: 65 of 68 tagged; the three without are r1, r2, r39 — each carries an exact period-end date and states its basis in prose. The repair report's 21/13/14 three-definition reconciliation reproduced on the bytes; its r6 `year-end counts printed nowhere held` stem-collision is real | **LANDED** |
| §K.3 prose-follows-register, §T.2 id collision, U.024/U.019 re-scope, E02 fidelity | §K.3 now says **two register rows, not one**, class DERIVED, confidence **Low**, with a COR-12 self-citation (stage_1.md:1272-1276); §T.2 names **S4215** by global id and keeps the withdrawn `P2S01` sentence struck (1696, 1708); U.024/U.019 gap cells re-scoped to EMPTY-within-perimeter with the never-run families named; E02 marks `[L769|L770]` and the carrier possessive | **LANDED** |
| the 989,225 / restatement-delta findings | Present in `quantitative.csv` only. `stage_1.md` occurrences of `989,225`, `171,932,690`, `220,511,038`, `1,088,338,000`, `868,336`: **0, 0, 0, 0, 0** | **LANDED IN ONE LAYER ONLY** → B-3 |

Also verified in the carriers, as the repair report described: 1965 **L837** prints `$171,932,690 $153,156,825`
and **L944/L945** print `139,686,954`/`31,256,511` (so the 989,225 short-fall is real arithmetic); 1967 **L819**
prints `$260,173,514 $220,511,038` and 1972 **L10** prints `$1,262,759,000 $1,088,338,000 16.0%` — both
restatement deltas are carrier facts, not inventions; 1966 **L214** (`more than $7.50 per visit`), **L806-807**
(`approximate amount of $2,200,000`), **L808-809** (`approximately $225,000`) confirm r32/r37/r38; 1974
**L4633-4641** confirms r60's roster and its 1962 cohort labels.

**The repair report's refusals are honest.** §5.b's correction of the brief (`FOR THE YEAR ENDED DECEMBER 31,
1975` occurs **1** time in a file of **5,458** lines — measured: `wc -l` 5458, count 1, at L3583; L3604 prints
the balance-sheet date `DECEMBER 31, 1975`) is right, and it corrected upward instead of inheriting "twice".
§5.f's re-description of the r27 claim (868,336 is a component sum, printed nowhere — measured: `868,336`
grep = 0 hits in the register and 0 in the volume; 1969 L951/L1001-1004 print `868,335`, `607,697`, `233,532`,
`27,107`) is right. §5.g's recomputation (23.8311 percent, not 23.84) is right.

## Check 2 — IS EVERY RETRACTION PROPAGATED? The gate passes; substance does not follow the id in four places.

`corrections`: **14 retraction ids; register layer reaches 14, volumes 14** ✓ (gate, quoted above). I also
confirmed `CORRECTIONS.md` carries all 14 as both a table row and a dated section (lines 14-28 table; sections
at 32/56/69/77/83/97/124/151/162/173/184/203/214), with COR-07…COR-14 opened by the repair pass and the
withdrawn wording kept struck rather than erased (§14 rule 4). **RD-122's outbound leg to the instruction
layer is now closed:** `MASTER_RESEARCH_LOG.md:1291` reads `~~No held byte names the company before
1972-03-22~~` — struck, which was the merge's residue item 2.

One step past the gate, three failures:

1. **No prose sentence asserts a withdrawn value as live** — the volume's live prose is clean. `60,770,000`
   and `60770000` appear 0 times; `23.84` 0 times; the `basis migration` sentence survives only struck inside
   §Boundary 4 (228) and inside the emission slices.
2. **Nine withdrawn-date rows sit unmarked inside the canonical volume** → B-2.
3. **Five repair findings exist only in `quantitative.csv`** → B-3.

## Check 3 — DO CITATIONS RESOLVE TO REAL BYTES? 16 claim records opened across all six blocks: 16/16 resolve; zero fabrications; 3 quote-fidelity defects; and one earlier FINDING is refuted outright.

Records sampled: **A01, A02, A03, A04, B01, B02, B03, B04, B05, F01, E02, P2-02, P2-03, P2-07, P2-09, P2-10,
P2-12** (volume 1 §A/§B/§F blocks, the §C-§H inline records, and the §I-§U P2 appendix). Every quoted passage
was opened at the named line of the named carrier:

- A01 1965 **L159-166** ✓ · A02 **L124-126** ✓ · A03 **L725-738** incl. `KNOLLWOOD, ST.LOUIS PARK / MINNESOTA
1962` ✓ · A04 `sources/ia_search/meta_01-target-archive.json` **259,567 B** on disk, matching the cell ✓ ·
B01 **L1417-1421** (`BRUCE B. DAYTON, President`), **L1436**, **L1452-1459** (`DOUGLAS J. DAYTON, President,
Target Stores, Inc.` / `JOHN GEISSE, Vice President`) ✓ · B03 **L388-394** ✓ · B04 **L110-115** ✓ · B05 1965
**L159-166** + 1970 **L209-212** (`first public stock offering in late 1967, it had 23 stores in five states`)
✓ · F01 **L404-410** (`51 percent of women customers in Hennepin County`) ✓ · P2-03 **L179-181** (44/100
percent) ✓ · P2-05 **L1038** (`$1,564,220, of which $626,683`) ✓ · P2-06 **L1051** (`$3,750,000`) ✓ · P2-09
1974 **L4633-4641** ✓ · P2-10 1973 **L3987-3995** — every digit real at **L3988** (`$ 470.3 $ 440.4 $ 345.8 $
289.0 $ 233.5`) ✓ · P2-12 CSA layer, `CHAIN STORE AGE, APRIL 1962` at **L121** ✓.
- **B02's count claim re-run by census, not by reading:** `Geisse` hits per layer = 1965:1, 1966:1, 1967:1,
  and **0 in each of the other 11** held layers → "exactly three of the eleven founding-era layers, zero from
  FY1968 onward" is a measured fact ✓.

**The audit-2 "fabricated quote" charge is WRONG and I confirm it on the bytes.** `target_s1_audit2…md:40`
rules S4203 **MISMATCH**: "**NEITHER quote is in the carrier as printed**", and at 305-307 "`(L1952)` has no
origin I can locate … absent from all 14 held layers". Measured: `1967_dayton_hudson_djvu.txt` **L1952 is
`JOHN F. GEISSE`**, **L1955-1956** print `Senior Vice President and General Merchandise / Manager`, and
**L769-770** print `1967. Target’s sales were $86,901,007, an in-` / `crease of 43 percent` — the quoted
sentence exists across an OCR line-break hyphen. The auditor then cited `Sales of $86,901,007 in 1967 were 43
percent ahead of 1966 volume of $60,731,468` as the carrier's *actual* wording; that sentence is also real
(**L410-411**), so the auditor found one printing and concluded the other did not exist. A line locator is not
carrier text (§14 rule 12) — "the token `L1952` occurs in zero bytes" is a measurement taken with the wrong
key. **COR-13's refutation stands and the citation is not retractable.** I did not "fix" the charge; there was
nothing to fix.

Three genuine fidelity defects remain, none of them a fabrication → B-5: **P2-07** quotes `The Company (which
commenced operations on January 15, 1966)` across 1965 **L1354-1355**, where the bytes print `January 15, SS
ey` (OCR) and `1966)` on the next line — a silent repair, unmarked, and no line locator is given; **P2-10**
renders 1973 **L3988**'s row label as `Sales (millions)` when the layer prints `SOLS AMIS)` (§K.3's own table
does show the corruption, so the register and the prose disagree about what the passage promised: the P2
preamble at stage_1.md:2148 says `Passage:` is "verbatim from held bytes … as printed"); **sources.csv S4203**
`relevant_passage` still prints `(L1952)` inside the quoted span and drops the carrier's possessive `Target’s`.

## Check 4 — ARE THE EMPTY ZONES LABELLED HONESTLY? Yes on all five; one expectation cell is not honest → B-4.

`data_gaps.csv` read cell-by-cell; the volume carries all six ids (U.028 ×15, U.030 ×20, U.031 ×7, U.032 ×20,
U.036 ×8, U.037 ×16; vocabulary census in the volume: UNTRIED 37, UNANSWERED 26, NOT HELD 6, EMPTY-within-
perimeter 1, "never searched/never run/never tried" 10).

- **U.030, 17 unopened PDF image legs** — `the 17 PDF image legs … were never fetched` / `not attempted inside
  this pass's zero web budget` = **UNTRIED**, correctly, and it carries the repair pass's FETCH REQUEST for
  the FY1970/FY1971 Statement-of-Income headers. The two year-end days stay `UNKNOWN` in 6 bare-year rows
  (r12, r13, r21, r22, r65, r66) with **no December placeholder substituted** — measured 0 `-12-31` in any
  date column. Honest.
- **U.031, the two unheld founder-credit obituaries** — `S4213` (2013-07-06 Twin Cities/Pioneer Press, tier 2,
  `access_date UNKNOWN`, `archived none`, `NOT HELD so it cannot be evidence`) and `S4214` (Geisse biography,
  **tier 4**, `publication_date UNKNOWN`, `NOT HELD; a Tier-4 lead that must be chased to a Tier 1/2 carrier`).
  Kept as rows rather than dropped, and they do not decide K1 either way. **One labelling nit:** U.031's gap
  cell never names which of the three states applies to the *route* (the obituaries were requested, not
  tried), unlike U.030/U.032/U.036 which say so → folded into B-5.
- **U.032, HathiTrust for the pre-FY1965 leg** — `book corpora never searched` = **UNTRIED** ✓ correctly, but
  its expectation cell is not honest → B-4.
- **U.036, predecessor-CIK retries** — `predecessor-CIK index routes never run … blocked by the 503s recorded
  at U.025` = UNTRIED resting on an UNANSWERED parent ✓, with the route named (`browse-edgar getcompany` for
  four terms, then `sec_intake index --from 1930-01-01 --to 1985-12-31`).
- **U.028 / U.037, the five UNVERIFIED-TLS layers** — UNANSWERED (route ran, transport failed:
  `CERTIFICATE_VERIFY_FAILED … --insecure was used`) with U.037 carrying the re-verification task and the
  citation cap (`before any of Q3-Q8 Q16-Q19 or section K.3 is cited at High`). Confirmed applied downward,
  not upward: P2-08/P2-09/P2-10 sit at Conf **Medium**, r57-r59 at **Low**, and I found **no** row raised to
  High on a TLS-unverified layer.

## Check 5 — TIER: **T2 core is right for the window; the volume's length is not a tier error, and U.032 must not be counted on to change it.**

Measured against §15.2's family rule (T1 needs ≥3 families returning **in-window Tier-1 text**):

| family | what Target's Stage-1 actually returned | in-window Tier-1? |
|---|---|---|
| filings (EDGAR) | nothing before 1994: CIK 27419 submissions floor 1994-02-10, FTS zeros are an **index floor (corpus begins 2001)**, name-to-CIK 503 on all four terms (U.025) | **0** |
| web archives | CDX 503 ×2 (U.026); nothing pre-mid-1990s held | **0** |
| periodical / corporate-print corpora | **11 in-window layers FY1965-FY1975** (48,050-130,295 B, sidecar-matched), carrying the whole register | **1 family, rich** |
| trade periodicals (independent) | **one** held leg, `Chain Store Age` April 1963 (170,260 B, verified TLS) — and S4215's own note: `it does not name the company once` | **1 family, thin** |
| auction / museum documentary sale | **UNTRIED** | 0 |

Two families returned in-window Tier-1 text → **T2 core, correctly derived, and it is not re-litigable upward
until a third family actually delivers.** The volume being 38,489 words at exemplar density (164 register rows,
37 anchors, 28 claim records) is RD-122's dispatch-budget matter, and §15.4 makes a missed length target
legitimate: **no evidence may be trimmed to silence the `budget` finding, and the certifier does not ask for
it.** What the tier record *does* need is B-4: RD-127 measured the HathiTrust route on a comparable company
phrase — **every dated result on the returned page is 1990 or later**, while the rich pool is the 1950s
**sector** records (`"five and dime" variety store`: 97 in-window, 1950-1959 — documents about the trade, not
namings of the registrant). Target's cells assert U.032 "is the route most likely to lift the tier from T2 to
T1" (data_gaps U.032; stage_1.md:2090, :2277) with **RD-127 cited 0 times anywhere in this company directory**
(measured). The route stays **open and UNTRIED** — the 6 undated rows, the 4 unparsed facet records and every
page past the first are unexamined, so this is not disproven — but "most likely to lift the tier" is an
expectation the corpus's only measurement does not support, and it must be re-scoped rather than repeated.

---

## BLOCKERS

**B-1 — BLOCKING. A held printed figure is declared unprinted in five places, in a carrier this volume already cites.**
*Claim:* `quantitative.csv` r15 (`1966 target_unit_sales 60800000`, class DERIVED, Conf Low) — `notes`:
**"DERIVED and printed nowhere in any held layer"**; r16 — "the **only** Target-unit sales figure printed
anywhere in FY1962-FY1968"; `data_gaps.csv` **U.021** "Target-unit revenue for 1962-1966 1968 and 1970-1972 …
named Target dollars **only for 1967**"; `stage_1.md:310` (§A.1) "Target's own dollars in FY1962–FY1968 |
printed **once**, at **$86,901,007 for fiscal 1967**"; `stage_1.md:1570` (§P) "— the only Target-unit revenue
printed in FY1962-FY1968"; `stage_1.md:790` (§H.4 **N4**) "No held layer prints Target-unit sales for
**1962-1966**, 1968 or 1970-1972".
*Carrier that fails to support it:* `sources/corporate_print/1967_dayton_hudson_djvu.txt` **L409-412**, i.e.
**S4203 / B1S03**, the same layer the §A.1 row cites for 1967 (L769-771) and the same layer COR-13 just
defended: `Target has enjoyed substantial growth. Sales` / `of $86,901,007 in 1967 were 43 percent ahead` /
`of 1966 volume of $60,731,468. Profits in-` / `creased by 161 percent.` A full-corpus grep of all 14 layers
under `sources/` returns exactly one hit, at that line; `60,731,468` occurs **0 times** in `stage_1.md`,
`quantitative.csv`, `conflicts.csv` and `data_gaps.csv`.
*What a repair pass must do:* (i) add the FY1966 Target-unit sales row at the **printed** `60,731,468`
(FACT as printed, `PERIOD BASIS: RESTATED` — the layer labelled 1967 prints fiscal 1966 — Conf capped at
Medium by U.028, carrier `S4203 L409-412`, with the §B1S03 lineage note); (ii) re-word r15 so the printed base
governs and `86,901,007 / 1.43 = 60,769,935 → 60,800,000` survives as a **footing check against a printed
figure**, keeping the superseded value visible (rule 4) and correcting the sentence "printed nowhere"; (iii)
correct r16's "only … printed anywhere", §A.1:310, §P:1570 and §H.4 **N4** to "printed for fiscal **1966 and
1967**, unprinted for 1962-1965, 1968 and 1970-1972"; (iv) re-scope **U.021** to the years actually unprinted
and say the FY1966 leg closed on 2026-09-29; (v) record the two further printed quantities in the same
paragraph, currently absent corpus-wide (0 hits each): the FY1967 Target **profit growth of 161 percent** and
the FY1967 Target estate — **1,184,900 square feet** after **298,600 added** (L412, L415-416), the latter
bearing directly on the 889,000 sq ft series (r?/U.012) whose five-store footing the register already flags;
(vi) open **COR-15** and propagate to both layers so the gate sees it. **U.013/r3's FY1964 leg is NOT refuted
by this finding** — no FY1964 Target base appears in any held layer and the repair must not touch it; that leg
stays as written.

**B-2 — BLOCKING. Nine withdrawn-date rows sit inside the canonical volume with no in-file supersession marker.**
*Claim:* `stage_1.md:893` still prints `Target,stage1,1975-12-31,"The FY1975 report prints a 31-December
year-end against late-January or early-February year-ends in FY1965-FY1974",…,P1S01,FACT,Medium,P1K10,"basis
migration inside the stage window…"` — the sentence COR-08 retracts, as an unmarked register row. And
`stage_1.md:2213-2216` (`1973-12-31` ×4), `:2217` (`1969-12-31`), `:2218` (`1972-12-31`), `:2219`
(`1962-12-31`), `:2233` (timeline `1973-12-31`) print the dates COR-07 withdrew — measured **9** rows matching
`stage1,19[0-9][0-9]-12-31` in the volume: eight December-dated rows (`:2213-2219` = 7, `:2233` = 1) plus
line 893's withdrawn `1975-12-31` basis-migration row.
*Carrier that fails to support them:* `1973_…` **L172-174** (February 2, 1974 / February 3, 1973), `1969_…`
**L1488** (January 31, 1970), `1974_…` **L147-148** (February 1, 1975), `1975_…` **L3246-3251** (no
31-December corpora basis; the December prints sit in the joint-venture block at L3583/L3604).
*What a repair pass must do:* `grep -ci superseded stage_1.md` = **0**, `grep -ci 'do not re-apply'` = **0** —
the warning exists only in `_parts/s1_p1.md` and `_parts/s1_p2.md` (both verified present, one dated line each)
and in `stage_1_index.md:12-13`, while the same emission slices were carried **into** the volume the index
calls canonical. Append a dated supersession line at each of the two emission banners (`stage_1.md:845-851`
volume-1 "Emit-only" preamble and `:2168` `>>> REGISTER ROWS FOR MERGE <<<`) stating that the nine root CSVs
are canonical, that the slices below are pre-repair emissions, and that **the dates in them are withdrawn by
COR-07/COR-08 — do not read or copy these rows**; then mark the nine affected rows themselves (`# WITHDRAWN BY
COR-07 — see quantitative.csv r54-r60`). Do **not** delete or revalue the slices (they are the merge's
byte-identical audit trail, RD-122), and do not re-apply them.

**B-3 — SUBSTANTIVE. Five repair-pass findings reach the registers and not the prose (the RD-105/106 direction, reversed).**
*Claim:* `CORRECTIONS.md` COR-12/COR-09 tables, and the repair report §4's propagation matrix, assert these
reach `stage_1.md` §K.3/§E.2. *Measured:* `989,225`, `171,932,690`, `220,511,038`, `1,088,338,000`, `868,336`
→ **0 occurrences each in `stage_1.md`**; all five live only in `quantitative.csv`. *Carriers:* `1965_…` **L837** vs **L944/L945** (170,943,465 against the printed
171,932,690 = **989,225 short**); `1967_…` **L819** (260,173,514 / 220,511,038); `1972_…` **L10**
(1,262,759,000 / 1,088,338,000); `1969_…` **L951** vs **L1001-1004** (868,335 against 607,697+233,532+27,107 =
868,336). *Exact live keys (measured):* `989,225` and `171,932,690` → **r68**
(`parent_total_cost_of_sales_and_expenses_printed` @1966-01-29); `220,511,038` → **r63**; `1,088,338,000` →
**r66 and r67**; `868,336` → **r27**. *What a repair pass must do:* state each figure in the section that uses it — the unexplained
989,225 deduction-total residual in **§K.2/§K.3**; the two restatement deltas plus the rule in **§E.2**
("no growth rate may cross FY1966→FY1967 or FY1971→FY1972 without naming which restatement it used") — and
name the 1-thousand retail-leg residual at r27 in §P.1, where COR-07/09/11 already sit. Keep the numbers in
the register cells; the prose is the missing leg. No plug, no new arithmetic, no value changes.

**B-4 — SUBSTANTIVE. U.032's expectation cell asserts a tier lift the corpus's only measurement does not support, and cites nothing.**
*Claim:* `data_gaps.csv` U.032 `best_available_evidence` — "HathiTrust reaches 1950s-1960s print and is **the
route most likely to lift the tier from T2 to T1**"; `stage_1.md:2277` (the emitted row) repeats it verbatim;
`stage_1.md:2090` (§U) — "**could lift the tier from T2 to T1**". *What fails to support it:* not a carrier
but a measurement — `MASTER_RESEARCH_LOG.md` **RD-127**, which mined the held HathiTrust bodies: on the
company phrase every dated result on the returned page is **1990-2014**; the 1950s depth is the **sector** pool
(97 records 1950-1959 under `"five and dime" variety store`, 23 under `"Walton's" "five-and-dime"`), i.e.
documents about the trade rather than namings of the registrant. `RD-127` appears **0 times** in
`stage_1.md`, `data_gaps.csv` and `conflicts.csv`. *What a repair pass must do:* keep U.032 **open and
UNTRIED** — this is not a disproof, and the 6 undated rows, the 4 facet records whose Published field the
parser did not extract, and every page past the first remain unexamined — but replace the expectation cell
with the measured statement, cite RD-127, and say plainly that a T1 re-derivation requires an **in-window
company-naming** result, that the sector pool would not qualify under §15.2, and that the `periodical_harvest`
task set must be added by the orchestrator (`tools/` is outside every agent's write scope, per stage_1.md:2091).

**B-5 — MINOR, fixable in one pass; listed in full so no later agent re-derives it.**
(a) `CORRECTIONS.md:20` COR-07 says the withdrawal covered "**six** `date` cells"; measured **seven**
`quantitative.csv` rows (r54-r60) + one `timeline.csv` row = eight, which `stage_1.md:1493` states correctly
as `1973-12-31` ×4 + three singles — the correction record and the prose disagree by one. (b) COR-08/`timeline.csv`
row 17 quote **six** physical lines under the locator **L3246-3250**; `consisted of 52 weeks.` is **L3251**.
(c) **P2-07** quotes a repaired OCR join (1965 L1354-1355, `January 15, SS ey` → `1966)`) with no line locator
and no `[L1354|L1355]` mark, while the P2 preamble (stage_1.md:2148) promises passages "verbatim … as
printed"; **P2-10** normalises 1973 **L3988**'s corrupt label `SOLS AMIS)` to `Sales (millions)` — §K.3's table
prints the corruption, so the appendix record and the section disagree about the same line. Mark the joins, or
re-label the P2 preamble as "verbatim digits, normalized labels". (d) **U.031** names no state for its *route*
where U.030/U.032/U.036 do. (e) `_parts/s1_p2.md`'s appended merge line calls §I–§U "**volume 1**".
(f) Outbound and **not mine to fix**: `sources.csv` **S4203** `relevant_passage` still holds `(L1952)` inside
the quoted span and drops `Target’s` (COR-13's unapplied leg); **S4209**'s `independence_note` is circular
("same lineage as S4208/**S4209** — one source") and its `source_title` opens with a stray `U `; **S4211**
claims independence as "digitised by a third-party backfile service not by the company" while §T.2 and U.031
rest the whole-lineage finding on **one uploader's item**, and S4211's `claim_supported` still reads `context
only` although timeline row 17 now rests its Fiscal Year fact on it. Hand all four to the sources agent as an
explicit outbound correction — **I did not edit `sources.csv`, and its mtime was unchanged at
2026-09-26 15:26:12 throughout this pass; no parallel writer touched it, or any Target file, under me.**

## WHAT I DID NOT TEST — stated with the same weight as what I did

1. **No retrieval.** Zero web calls; I did not verify any URL, HTTP status or archive.org route, so every
   UNANSWERED cell (U.025, U.026, U.027, U.028) is judged only on whether the bytes on disk support what the
   cell says about them.
2. **The 17 PDF image legs (U.030) do not exist on disk**, so I could not test the FY1970/FY1971 year-end days
   from any source. Those two days stay UNKNOWN and I confirm no placeholder; I did not test whether the
   FETCH REQUEST would settle U.008/U.009.
3. **I opened 16 of the 28 claim records** (A01-A04, B01-B05, E02, F01, P2-02, P2-03, P2-07, P2-09, P2-10,
   P2-12) and the §I–§U inline records **C01, D01, G01, H01, H02 are unopened**; **B1-01…B1-12 were not tested
   at all** (they live only in `research/B1_dayton_print_records.md`, declared superseded). The 12 volume-2
   rows P2-04, P2-05 (passage verified, entity check not), P2-06, P2-08, P2-11 were sampled only where the
   table above names them.
4. **Sidecars**: I byte-matched three layers' claimed sizes (1965 48,050 · 1967 45,200 · 1970 53,023) and the
   CSA file (170,260 B); the other eleven layers' `bytes` claims and every `publication_date`/`access_date`
   cell are untested, as is U.023's provenance leg beyond the disk value.
5. **Post-boundary `(PB)` legs** (FY1972-FY1974 recap rows, the 1998/1999/2000 layers) — I read them only far
   enough to run the Geisse census and the five-year header checks; I did not audit their money.
6. **Not re-derived by me:** the 28-vs-28 claim-record census and the byte-identical-slice non-destruction
   proof (RD-122), the 157→164 fold arithmetic, and the 34-folded/28-group collision ledger. I measured the
   end state (164 rows, 9 registers, 37↔37 anchors, 14 ids), not the merge's history.
7. **`_MANIFEST.md` and `stage_1_index.md` word/byte claims**: I confirmed 38,489 / 261,590 and 1,243 against
   the gate and the filesystem, but did not audit the manifest's per-file batch table or its non-destruction
   table line by line.
8. **I did not test the four `tools/` defects at U.029** (they are handed to the orchestrator), and did not
   verify `periodical_harvest.py`'s ability to run a `target` task set — so B-4's remedy is unproven as
   executable, only named.
9. **I did not test the FY1964 Target-unit base either way** (U.013's leg), and did not search the 14 layers for
   a printed FY1962-FY1965 or FY1968 Target-unit dollar, so B-1's corrected year list is stated from the one
   line I found, not from an exhaustive absence hunt.

## WHAT IS SOUND, AND SHOULD NOT BE REOPENED

Repairs 1-7 landed as measured in Check 1. The gate's 20 passes are real and re-measured. COR-13's refutation
of the S4203 charge is correct and must not be retried by a later pass. The independence ledger's downward
corrections (P2-02 `Corroboration: 1` → `0 independent`, B05 `1 lineage` → `0 independent`, §T.2 → S4215) are
in both layers. Confidence moved **down** and never up for the TLS-unverified layers. No plugged figure was
invented for the 989,225 residual. `budget` at `--tier core` is expected, adjudicated by RD-122, and must not
be "cured" by trimming: **a repair pass that shortens the volume to 22,000 words to satisfy the gate destroys
evidence and would itself be a blocker.**

STATUS: WRITTEN 2026-09-29, agent `target-s1-certify`. Verdict **NOT-CERTIFIED**, blockers **B-1…B-5**
(B-1, B-2 blocking; B-3, B-4 substantive; B-5 minor). Nothing in the company directory was edited by this pass.
