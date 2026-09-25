# amazon_s3_hindsight_repairs.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T19:18:29Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## H-1

STATUS: WRITTEN — repaired (mechanism corrected, false claim retracted as COR-16)

Verified against the documents before touching the prose: FY1999 10-K `sources/10-K_FY1999_acc-0000891020-00-000622_filed-2000-03-23.txt`
l.1672-1690 prints the quarterly range table on the final 12× vintage — 1999 highs **$99.56 / $110.63 / $85.00 /
$113.00**, whole-1999 range $41.00–$113.00. The conversion price restated to that vintage is **$78.0275** (§K.4,
DERIVED `156.055 ÷ 2`; `1,250,000,000 ÷ 78.0275 = 16,019,993`), and 150% of it is **$117.04**. So the strike was
exceeded by all four 1999 highs and the redemption gate by none. The audit's reading of §M.13 is correct, and the
sheet's H-1 text ("never entered the money on any filed 1999 range … so the equity option they sold never
relieved the debt") was false in both halves.

**Edit made** (`stage_3_part_2.md` §O.1, *For* leg): deleted both asserted sentences; restated the mechanism as
filed — the **$78.0275 strike in the money at every filed 1999 high**, the **$117.04 optional-redemption gate
above every filed 1998/1999 high**, therefore "the issuer could not compel conversion and the notes remained debt
**at the holders' option, not at the company's**". The economic point the counterfactual needs survives without
the inversion: the priced cost is the **4¾% cash coupon plus the absence of an issuer-side escape**. Added an
in-place `RETRACTION, COR-16` marker quoting the withdrawn words, and pointed to the `N-5 vs M.13` conflict note
already at the foot of §N (part_2 l.721).

**Not done on purpose:** no number was substituted or back-solved. Whether holders *did* convert is post-window
and is not imported (§2, §6); the sentence says so rather than inferring it.

## H-2

STATUS: WRITTEN — downgraded (motive claim relabelled RETROSPECTIVE INTERPRETATION/Low, mechanism UNKNOWN; retraction COR-17)

Verified locally: Q3-1999 10-Q l.1626-1635 (filed 1999-11-15) prints "we have **no previous experience** with
automated distribution centers, as the two distribution centers in operation prior to 1999 … **were manually
operated**", and in the *same sentence* records that during the nine months to 1999-09-30 the company "**opened
distribution centers in Nevada, Georgia, Kentucky, Kansas and North Dakota**" — five openings. FY1999 10-K
l.1026-1027 (filed 2000-03-23) prints "we have had **limited experience**". No drafting history, counsel file or
board record exists in `sources/`, so the protective motive is un(document)able; the accuracy-update alternative
is carried by the filed text itself.

**Edits made:**
1. §M.5 heading (part_2 l.452): "the admission was then softened, in the same corpus, **before it could be read
   against the charge**" → "admitted in writing — twice, in two wordings, and the change of wording is dated but
   not documented as to motive".
2. §M.5 item 2: split into **FACT** (both wordings, both dates, no stated change of fact printed) and
   **`RETROSPECTIVE INTERPRETATION`, Confidence Low** (the protective reading), with the five-plants alternative
   stated and sourced to item 1 / §G.1 G3–G8 / §D.0, plus an in-place `RETRACTION, COR-17` marker quoting the
   withdrawn clause. §D.1's own discipline line is cited as the model.
3. §M.5 closing confidence line: was "High on all three strings **and on the softening**" → High on the wordings,
   dates, tense change and contract dating; **Low / RETROSPECTIVE on the reason for the wording change**.
4. `stage_3_part_1.md` §G.5 row **G31**: "printed **weaker each time**" → "printed **differently, as the automated
   estate opened**" with the filed fact that makes "limited" true, and an explicit `mechanism UNKNOWN` + Low
   retrospective tag pointing at §M.5/COR-17. The row's *Finding* cell also said "relaxes **six weeks later**":
   the 10-K's filing date is 2000-03-23, eighteen weeks after 1999-11-15, so the cell now states both dates
   (event 1999-12-31, filed 2000-03-23) instead of an interval.

## H-3

STATUS: WRITTEN — repaired (per-order basis removed, unsupported "quarterly-comparable" label cut, §6 basis note added)

Verified: the 3.24 points are `11.49% − 8.25%`, both computed on **net sales** (`188,400 ÷ 1,639,839`,
`50,300 ÷ 609,819`); §K.6 prints fulfilment cost per order as **UNKNOWN** because "no order count exists in
**any** filing in the window". Grep of the Stage-3 sources for a quarterly fulfilment figure returns nothing
beyond the FY1999 annual note (three points: 1997/1998/1999) — the series is annual, not quarterly.

**Edits made:**
1. §M.1 (part_2 l.376): "the cost of **delivering an order** rose 3.24 percentage points of revenue" →
   "**fulfilment cost per dollar of net sales** rose 3.24 percentage points", with the arithmetic printed in the
   sentence and a **§6 basis note**: per-order cost stays UNKNOWN and the 3.24 points may not be read as one.
2. §L row "1998-06-11 / 1998-11-17 → FY1999 MD&A" (part_2 l.341): struck "quarterly-comparable"; now "a filed,
   audited-adjacent **annual** dollar series at three points (1997 / 1998 / 1999) … **not** a quarterly series",
   pointing to `quantitative.csv` rows 325-327. The row's own "It is still **not per order**" caveat is kept.

## H-4 register rows

STATUS: WRITTEN — register gaps closed (11 `quantitative.csv` rows + 1 `failures.csv` row added; two audit items found already registered)

**Verified before adding, and one method correction to the audit's own instrument:** the auditor string-checked
comma-formatted digits (`1,308,292`), but this register stores values unseparated (`1308292`), so several "zero
hits" were counting artefacts. Re-run on both forms against all nine CSVs:

| item | true state before this pass | action |
|---|---|---|
| FY1999 segment note (1308292 / 167743 / 163804 / 262871 / 7801 / 242148 / 31000 / 79223 / 352371) | **absent** — 0 hits in every register | 3 rows added (revenues, gross profit (loss), segment loss) + 1 comparative-year row + 1 DERIVED share row |
| Q4-1999 inventory charge ($39m) | **absent** — 0 hits for `39000`, `39 million` | 2 rows added (the charge; the 13.4%/2.4% ratios with arithmetic) + **1 `failures.csv` row** |
| Inventories 220646 | **absent** | 1 row added (l.2545) |
| Days payable 1999 = 125.2 | **absent** (86.8 present at row 250; 101.3 in that row's notes) | 1 row added, `derived_arithmetic` = `463026 / (1349194 / 365) = 125.2` |
| Q4-1999 D&A 13871 | **already in `quantitative.csv` (line 372) and `timeline.csv`** — with its arithmetic | no row added; duplicating would create a false second record |
| 1999 debt proceeds 1263639 | **already registered** (proceeds/repayments row) | no row added |
| Note repurchases: 126.0m face / 83.9m accreted | **already registered** (line 263) | no row added |
| FY1999 repurchases 178.4 / 266 principal / 190.7 remaining | **absent** | 1 row added — **and it surfaced a document conflict**: l.2282 prints $178.4m as *cash paid*, l.3686 prints the same $178.4m as *accreted value* on $266m principal. Registered with both printings, `which is the cash figure = UNKNOWN`, no back-solve; the `530000 − 266000 = 264000` vs `190700` residue left to §U (COR-26) |
| Note receivable (1099) | **absent** | 1 row added — with the correction that **1099 is the 1998 column** (1999 is (1171), l.2580) and that **no counterparty is named at the cited line**, so the "officer's" attribution is UNKNOWN, not filed |
| L-1: run-rate row's empty `derived_arithmetic` | propagation miss | `252.9 x 4 = 1011.6` copied into the row, source cell extended to the 8-K event 1999-01-26 l.193 that prints $252.9m, and the row labelled a propagation fix, not a new number |

All rows carry `stage3`, a `source_id` that exists in `sources.csv` (**S30075** for every FY1999 10-K figure; the
S30075/S30011 pair for the derived Q4 D&A already on file), the document **and line** in the `source` cell, and
`derived_arithmetic` on every DERIVED value (§13). `gates.py` confirms widths held: **quantitative.csv 392 rows ×
12 cols, failures.csv 62 rows × 11 cols, all `S####` tokens resolve**.

## H-5

STATUS: WRITTEN — repaired (relabelled + alternative added + mind-state downgraded; retraction COR-18)

§C.2's closing sentence read filed safe-harbour risk factors as the company's mental state ("**unsure of the
machine**") and justified doing so by their being "legally exposed" — which cuts the other way, since
worst-case enumeration is what the class is *for*. Verified locally that §D.1 carries the opposite rule ("the
enumerated failure modes are **enumerated, not evidenced as experienced**, and this file does not upgrade them")
and that no in-window document contains a "broken through" benchmark.

**Edit made:** the sentence is withdrawn in place (COR-18 marker printed) and replaced by a CONTEMPORANEOUS
OBSERVATION confined to "the registrant disclosed X on date Y" across seven dated disclosures; the
disclosure-incentive alternative explanation is added; the state of mind is **UNKNOWN**; the filed list and its
citations are untouched (the audit's remedy said to keep them, and they are sound). **Confidence split printed:**
High on each disclosure and its date, UNKNOWN behind them.

**Done in the same §C.2 coda (M-5):** the §16 quartet is now complete — the missing **Confidence** grade is
appended (High on capital-financed capacity against audited capex; **Medium-High**, borrowed from §C.1's own
grading, on the absence of an internally generated means of continuation, capped there because the corpus is the
issuer's own filings); "Stage 3's **outcome**" → "Stage 3's **state at the recommended boundary (1999-09-30)**";
and the corpus-total negative is scoped — "**across the 99 files in `sources/`, no independent witness to demand
exists at any date** — a record-selection null inside this corpus, not a claim about documents this project did
not retrieve".

## Sibling sweeps

STATUS: WRITTEN — every hit classified; four same-construction siblings found and fixed, five left as named residue

Swept across `stage_1.md`, `stage_2_part_1/2/3.md`, `stage_3_part_1/2/3.md`, `context_appendices.md` and the
claim-record files (counts are **post-repair**, so a non-zero count is either a correct usage, a quoted source
string, or a dated retraction marker — the three-ways the audit's own rule demands).

| construction | sites and classification |
|---|---|
| `never entered the money` / `never relieved the debt` | **0 / 0** across all nine volumes — single instance, repaired. Literal digits `117.04` (4 hits) and `78.0275` (8) all in `stage_3_part_2.md`: §K.4/§K.8/§L/§M.13/§O.1, **all correct as strike-or-gate** on inspection; `in the money` (2) both correct |
| `softened` | post-edit: part_2 ×**4** (2 = my COR-17/COR-20 retraction quotes; **2 were siblings — §N row and §O.3 — now restated**, see COR-17); part_1 ×1 (l.538 "quantifier softened from 'any' to 'most'" = **documented diff between two filed reports, correct**); stage_1 ×1 (l.690 "not to soften the signal" = **correct, non-motive**); stage_2_part_2 ×1 and stage_2_part_3 ×4 (Amendment No. 5 vs No. 6 / 10-K clause diffs, both documents on disk = **correct**); `stage_2_claim_records.md` l.441 "it was **softened out of the record** by the annual report" = **borderline motive wording, not mine → residue**; `stage_3_claim_records_part_1b.md` l.40 = **the full H-2 claim, standing → residue** |
| `weaker each time` | part_1 0 (repaired); `stage_3_claim_records.md` l.592 (record G93) = **residue**, and it also carries the stale "**relaxes six weeks later**" interval against a 2000-03-23 filing date |
| `read against the charge` | part_2 ×2 — **both are my dated retraction markers** (COR-17); `stage_3_claim_records_part_1b.md` l.40 = **residue** |
| `relaxes` / `relaxed to` | part_1 ×3: **2 fixed under COR-17** (estate table l.359; claim record A08 l.786) and **1 correct** (G44/U.135 quantifier diff between two annual reports); part_3 ×2 (same quantifier diff, **correct**); claim records G93 = residue |
| `cost of delivering an order` / `delivering an order` | **0 in all three Stage-3 volumes**; `stage_3_claim_records_part_1b.md` l.30 = **residue** (H-3 construction) |
| `quarterly-comparable` | **0 corpus-wide** after the §L fix |
| `moved out of advertising` | part_2 ×1 = my COR-19 retraction quote; no siblings |
| `from bondholders` / `bid for convertibles` | part_2 ×1 = my COR-20 retraction quote; `bid for convertibles` **0** |
| `demand-side signal` | part_1 ×1 = my COR-22 retraction quote; **0 elsewhere** in Stage 1/2 and the claim records |
| `cost of capital` | part_1 ×2, **both inside the new labelled coda** (the withdrawn sentence + "UNKNOWN as a measured quantity"); **0 in every other volume**, so M-1 was a single site |
| `only scale produces` | part_1 ×1 = the sentence now marked as **declined**, mechanism UNKNOWN (COR/M-9) |
| `no day, no amount` | **0** — the §D.0 cell is now confined and cites l.1890-1892 (COR-21); `no independent witness` **0** unscoped |
| `unsure of the machine` / `legally exposed` | 1 / 0 — the single hit is my COR-18 retraction quote |
| `cheapest available` | part_2 ×1 = the COR-24 marker |

**H-2 and H-3 are therefore not three-instance and one-instance defects: H-2 had four live siblings in the
volumes I own (all fixed) and H-3 none; the remaining live copies all sit in the claim-record files.**

## MEDIUM and LOW items settled from local documents

STATUS: WRITTEN (folded in here rather than one section each, to stay inside budget; each is a single site unless noted)

| item | disposition | what changed |
|---|---|---|
| M-1 §D.3 cost-of-capital | **downgraded** (COR-23) | conclusion withdrawn in place; `INFERENCE` Low; effective yields **not computed** — no comparable price observation exists in `sources/` and none is derivable from filed numbers without an option-value assumption, so "cost of capital" is **UNKNOWN as a measured quantity**; alternative (1999 tech-paper demand) named from §N's own "window open for US high-yield convertibles" cell |
| M-2 §L 1998-04-24→05-05 | **re-sourced** (COR-20) | covenant's end re-sourced to the repayment (10-Q Q1-1998 l.988-989; 424B2 l.1355-1357) as FACT/High; motive reading returned to §N's Medium-inferred wording; "convertibles" deleted (non-convertible notes) |
| M-3 §M.3 | **replaced by the arithmetic the table supports** (COR-19) | transfer verb cut; relative growth (advertising 2.34×, fulfilment 3.75×, sales 2.7×) at High; per-customer basis removed |
| M-4 §D.0 Q4 row | **corrected** (COR-21) | "no day, no amount **in that sentence**" + the l.1890-1892 amount; Conf High (incurred, amount, quarter), UNKNOWN only for split/day |
| M-5 §C.2 assessment coda | **completed** | §16 quartet now has its missing Confidence grades; "outcome" → "state at the recommended boundary (1999-09-30)"; the corpus-total negative scoped to the 99 local files |
| M-6 §R current-objective row (part_3 l.551) | **relabelled** | `INFERENCE`, Medium, with the constraint-vs-objective alternative ("were and are **dependent on** expansion of our infrastructure", §N) and §N's evidentiary limit pointed to; the filed sequence stays High, internal number/authorship stay UNKNOWN |
| M-7 §D.0 converts row | **relabelled** (COR-22) | "capital-supply signal", with §L's "clearest external **price** signal" named as the form to propagate |
| M-8 §C.1 refuted column | **settled as an attribution note, not a citation** | a header note declares the column **RECONSTRUCTED BY THIS PROJECT**, authorship UNKNOWN, quotation marks typographic not attributive, dossier keys identified as project keys, and records that a sourced version would need a FETCH REQUEST this zero-web pass did not issue. No published source was invented |
| M-9 §A.2/A.3 float row | **generalisation dropped** | "only scale produces" declined as a cross-firm claim with no comparator in `sources/` (§I, §H.0); filed movement kept, **mechanism UNKNOWN** |
| L-1 run-rate row | **propagated** | `252.9 x 4 = 1011.6` into `derived_arithmetic`, source cell extended to 8-K event 1999-01-26 l.193 |
| L-2 §L splits row | **relabelled** (COR-24) | "cheapest available" adjective cut, marked `INFERENCE`, pointing at the row's own Low grading and §N's limit |

**Residue not mine to write:** the claim-record copies of H-2/H-3 (see above) and `context_appendices.md`, which
this audit already recommended for a sibling sheet.

## Residue for the certifier

STATUS: WRITTEN

1. **Claim records need the same four edits, and I could not touch them** (`stage_3_claim_records*.md` is another
   agent's path): `stage_3_claim_records_part_1b.md` **l.40** (full H-2 softened-admission claim), **l.30** (H-3
   per-order sentence), `stage_3_claim_records.md` **l.592** (G93, "printed weaker each time" + "relaxes six
   weeks later"), **l.162** (A08 "relaxed to"), and the §O.1/§M.13 strike-vs-gate line if any H-1 wording is
   mirrored there. Point them at COR-16/17/25; the claim-record Class/Conf lines should carry
   `RETROSPECTIVE INTERPRETATION, Low` on the motive.
2. **Stage-2 volume wording, adjacent to COR-17:** `stage_2_claim_records.md` l.441 "softened out of the record"
   — a documented diff, but the phrase attributes a effect on the record; classify or leave with a reason.
3. **A genuine document conflict I did not resolve (COR-26):** $178.4m printed as *cash paid* (10-K FY1999
   l.2282) and as *accreted value* on $266m principal (l.3686); and `530,000 − 266,000 = 264,000` against the
   "$190.7 million remaining" at l.3688. Registered as filed with **UNKNOWN** on which is cash; the reconciling
   items (conversions/exchanges) are not at the lines read. **Needs a §U row** — §U is part_3, and adding a U
   block means the §U parity the anchors gate already tracks, so I recorded it rather than opening it.
4. **M-1 was settled by downgrade, not by arithmetic:** effective yields are **not derivable** from filed numbers
   without an option-value assumption the record does not supply (§I confirms no peer document exists). If the
   certifier wants the number, it needs a fetch, not a repair.
5. **Two audit items in H-4 were already registered** (Q4 D&A 13871 at `quantitative.csv` l.372 with its
   arithmetic; 1263639 proceeds; 126.0 face) — the comma-vs-no-comma counting artefact. No rows added for them;
   re-adding would create duplicate records. Please read the gate widths rather than the digit grep.
6. **Not re-opened:** RD-073/076/077 carried in from `stage_3_index.md`; the 4 files with `[RETIRED-KEY REFERENCE]`
   `S3xxx` tokens (the gate reports stage_3_part_2, stage_3_part_3, `stage_3_claim_records_part_1b`,
   `stage_3_pending_registers` — **unedited on purpose**, per brief); `U.201–U.211`/`U.220` anchor parity, which
   predates this pass.
7. **Left PENDING on my own sheet: nothing.** H-1…H-5, M-1…M-9 (M-8 settled as an attribution note, not a
   citation, since no published source exists in `sources/` to cite) and L-1/L-2 are each settled above, downgraded
   above, or named as residue above. Zero web calls, zero git, nothing deleted or moved.

