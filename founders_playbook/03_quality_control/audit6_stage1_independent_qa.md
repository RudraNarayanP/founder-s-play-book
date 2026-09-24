# AUDIT 6 — INDEPENDENT QA OF THE STAGE-1 CLOSURE (Amazon, company_001)

**Verifier status.** This sheet was written by an INDEPENDENT verifier who did not perform the repairs
under review and who has an interest in not repeating the AUDIT-3/4 failure mode in which the closer
graded its own work. I operated under a hard read-only constraint.

**I edited nothing.** The only file created anywhere in this run is this one:
`founders_playbook/03_quality_control/audit6_stage1_independent_qa.md`. All other files were opened for
reading only. Parser/recomputation scripts were written OUTSIDE the repository (to `E:\tmp\qoder_audit6\`)
precisely so that the "exactly one new file" constraint held; their paths and outputs are quoted inline
below so every verdict is re-runnable.

**Zero web requests were made.** No WebSearch or WebFetch call was issued in this session. Every artifact
cited is local. Two checklist sub-items would have required the web; they are marked UNTRIED and named.

**Standard applied.** No assertion below is offered without a `file:line`. Where I could not localize a
claim to a line I say so rather than assert it. Where the closure agent was right, I say that too —
but only after trying the break.

Repo root: `E:\founder's playbook`. All paths below are relative to
`E:\founder's playbook\founders_playbook\` unless written absolute.

---

## Verdict table

| # | Item | Verdict | Primary evidence |
|---|---|---|---|
| 1 | U-block ↔ register parity | **CONFIRMED** (1 named residual: stale U-preamble count) | `company_001_amazon/stage_1.md:1258, 2251`; `conflicts.csv:2–44`; stale count at `stage_1.md:1251` |
| 2 | Register parse (9 CSVs, schema, quoting, 428 rows) | **CONFIRMED** | `00_METHOD_AND_STYLE.md:263–318`; script output §2 below |
| 3 | derived_arithmetic coverage + recompute | **CONFIRMED 29/29** (1 named residual: 1-cent addend label, `quantitative.csv:34`) | script output §3 below |
| 4 | The dead bridge | **DEFECT** | `_parts/s1_p4.md:102–103` prints the false form live, unannotated; contradicts `03_quality_control/amazon_s1_numeric_closure_final.md:29` (own R-4 at `:42`). Replacement matches filed terms — verified at `sources/S-1_original…txt:3636–3655` |
| 5 | `21,382.98` retraction-only | **CONFIRMED** | 6 occurrences repo-wide, all retraction chains — §5 below |
| 6 | Retracted denominators `2,613,000` / `$871,024` / `$871,000` | **DEFECT** | `context_appendices.md:596` (Value column) and `:639` still run the `$871,000` / `2,613,000` leg live; falsifies `amazon_s1_numeric_closure_final.md:17`. Pre-flagged as S2E-28, `research/ST2_E_adversarial.md:895–922` |
| 7 | U.41 single-pointer | **CONFIRMED** (1 adjacent register defect) | `stage_1.md:347` sole live pointer, `:2203` sole block; `timeline.csv:33`/`:55` mis-keyed to U.16 |
| 8 | COR-10 / COR-12 coherence | **DEFECT** (arithmetic limb CONFIRMED) | `1,006,899.30` ✓ from `sources/S-1_original…txt:4300–4302`; COR-03 block `CORRECTIONS.md:57–69` carries no supersession marker; `:194`; `_parts/s1_p3b_H_addendum.md:131` |
| 9 | Filing-lineage demotions | **DEFECT** | `stage_1.md:16–17` and `:1139` still say "independent corroboration"; `quantitative.csv:74`; `stage_1.md:870`; `context_appendices.md:595`; `CORRECTIONS.md:241–242`; §T `:1204`/`:1205`/`:1206` undemoted; claim records `:383`, `:397`, `:454` escaped the re-key |
| 10 | §P.2 total recomputation | **CONFIRMED 32/32 figures** (1 mismatch reported: `stage_1.md:925`) | every d-entry recomputed, §10 table |
| 11 | §R ↔ §P cross-reference | **CONFIRMED** | `stage_1.md:1136–1159`: all d-refs / U-refs resolve; `quantitative.csv:112` exists as §R:1156 describes |
| 12 | AUDIT 5 re-run on repaired text | **DEFECT** | A-B2 (`amazon_s1_audit4_audit5_final.md:410`) **closed**; A-B1 (`:409`, `:431`) **still lands** |
| 13 | Fix-introduced-defect sweep | **DEFECT** | 4 new false closure assertions, incl. `stage_1.md:36` "four sites … corrected"; no new unfounded number |

**Tallies: CONFIRMED 7 · DEFECT 6 · UNTRIED 0** at item level, plus **3 named UNTRIED sub-probes** (§ "Sub-probes
I did not run") that would each have required a web request.

---

## Item 1 — U-block ↔ register parity — **CONFIRMED**

### Convention actually used (inspected, not assumed)

Stage 1 does NOT use `### U.n`. `## U. CONFLICTING EVIDENCE` opens at `stage_1.md:1249`; each conflict is
a bold-runin paragraph of the form `**U.<n> — <title>**`. A grep for `^### U` returns zero hits
(`grep -n "^### U" stage_1.md` → empty). Any parity count keyed to `### U.n` would have returned 0 and
been silently wrong; this is why I inspected first.

### Count of blocks

```
$ grep -cE "^\*\*U\.[0-9]+ — " stage_1.md
43
```

The 43 matches are at `stage_1.md:` **1258, 1297, 1331, 1351, 1373, 1395, 1422, 1453, 1546, 1568, 1599,
1626, 1648, 1673, 1697, 1722, 1736, 1769, 1792, 1814, 1829, 1859, 1877, 1898, 1921, 1937, 1956, 1973,
1990, 2021, 2036, 2052, 2070, 2088, 2106, 2122, 2138, 2149, 2167, 2185, 2203, 2233, 2251**.
Two other lines begin with `U.` but are cross-references inside prose, not blocks
(`stage_1.md:796` relative-to-U, i.e. `2044` `U.7**.` inside U.31; `stage_1.md:2226` inside U.41) — both
correctly excluded by the `^\*\*U\.[0-9]+ — ` anchor, and I checked them by eye.

### Set parity against `conflicts.csv`, parsed with quoting

Script `E:\tmp\qoder_audit6\parse_registers.py` (csv module, `utf-8-sig`, strict):

```
stage1 U ids: [1 … 43]            contiguous 1-43: True
csv  U ids == stage1 U ids: True
orphans in csv only: set()   in md only: set()
conflicts.csv data rows: 43, field counts Counter({15: 44})  # header + 43 rows, all 15 cells
dupes: []
```

`conflicts.csv` records run from file line 2 (U.1) to file line 44 (U.43). IDs match one-for-one, in
order, with no gaps, no duplicates, and no orphans in either direction. **43 = 43.** The count the
closure agent asserted is right.

### Named residual (does not break parity, but is a live stale statement)

`stage_1.md:1251`, the §U preamble, still reads:

> `**42 canonical conflicts, U.1–U.42.**`

against a section that now holds 43 blocks (U.1 at `:1258` … U.43 at `:2251`). The same file carries the
correction 1,068 lines later at `stage_1.md:2317–2319` ("the spine now runs **U.1–U.43** and
`conflicts.csv` carries exactly 43 rows … verified by parse, not by assertion"), and
`stage_1.md:2307–2308` appends the U.43 spine note — so the discrepancy is disclosed, not concealed, and
the append-only-id rule at `00_METHOD_AND_STYLE.md:188` ("Never renumber") explains why the merge-time
wording was left standing. But the closure agent annotated the *tail* and not the *head*: a reader who
stops at the §U header is told 42 before seeing 43. **Reported as a residual, not a parity defect** —
the object of item 1 (block↔row parity) holds exactly.

---

## Item 2 — Register parse — **CONFIRMED**

Nine CSVs live under `company_001_amazon/`. Schemas taken from
`00_METHOD_AND_STYLE.md:253–318` verbatim: `sources.csv` at `:264–267`, `quantitative.csv` at `:273–276`,
`timeline.csv` at `:281–284`, `decisions.csv` at `:287–290`, `validation.csv`/`failures.csv` at
`:294–297`, `channels.csv` at `:300–303`, `conflicts.csv` at `:306–310`, `data_gaps.csv` at `:313–316`.

### The parser was proven before it was trusted

I did not eyeball anything. Two independent proofs, script
`E:\tmp\qoder_audit6\prove_parser.py`:

```
SYNTHETIC [embedded comma in quoted field]              -> PASS
SYNTHETIC [doubled quote escape ""]                     -> PASS
SYNTHETIC [embedded newline inside quoted field]        -> PASS
SYNTHETIC [control: no quoting needed]                  -> PASS
ALL SYNTHETIC PARSER TESTS PASS: True
```

and, on the real data, a deliberately naive comma-split is compared against the quoting-aware parse, to
show that quoting is load-bearing rather than decorative in these files:

```
conflicts.csv:    strict ncols=[15]  naive split ncols=[15,23,25,…,158]  -> load-bearing: True
quantitative.csv: strict ncols=[12]  naive split ncols=[12,13,…,105]      -> load-bearing: True
sources.csv:      strict ncols=[18]  naive split ncols=[18,19,…,96]       -> load-bearing: True
timeline.csv:     strict ncols=[11]  naive split ncols=[11,12,…,45]       -> load-bearing: True
decisions.csv:    strict ncols=[15]  naive split ncols=[15,16,…,28]       -> load-bearing: True
validation.csv:   strict ncols=[11]  naive split ncols=[11,12,…,27]       -> load-bearing: True
failures.csv:     strict ncols=[11]  naive split ncols=[11,12,…,25]       -> load-bearing: True
channels.csv:     strict ncols=[11]  naive split ncols=[11,12,…,20]       -> load-bearing: True
data_gaps.csv:    strict ncols=[8]   naive split ncols=[8,9,…,67]         -> load-bearing: True
```

A field-level spot check on a row I knew to be quoted — `conflicts.csv` record for **U.8** (file line 9),
which carries commas, an apostrophe-quoted phrase and a `""`-escaped quote — re-parses to exactly 15
named cells, e.g. `claim_b` = `The filings DO disclose the round: 3,021,000 shares to 23 purchasers at
approximately $.3333 per share or an aggregate of $1,007,000, …` (single cell, embedded commas intact).
The naive split of that line yields 51 pseudo-cells. Eyeballing this register would have produced a
different and wrong answer, which is the point of the test.

### Result — header, arity, row count

```
file             | rows | field counts as parsed | header matches §13 schema
sources.csv      | 102  | [18]                   | OK
quantitative.csv | 111  | [12]                   | OK
timeline.csv     |  57  | [11]                   | OK
decisions.csv    |  15  | [15]                   | OK
validation.csv   |  29  | [11]                   | OK
failures.csv     |  33  | [11]                   | OK
channels.csv     |  15  | [11]                   | OK
conflicts.csv    |  43  | [15]                   | OK
data_gaps.csv    |  23  |  [8]                   | OK
TOTAL DATA ROWS: 428
```

Every one of the nine headers is a field-for-field, case-insensitive match to its §13 schema. No ragged
rows in any file (zero output from the ragged-row check in `parse_registers.py`). **Total = 428, which is
the number the closure agent claimed.** CONFIRMED.

*Scope note, stated so it is not mistaken for a defect:* `00_METHOD_AND_STYLE.md:257` says "an empty cell
is a defect", but `:277–278` explicitly carves out `derived_arithmetic`, which "is mandatory whenever
`evidence_class` is `ESTIMATE`/`DERIVED` … empty otherwise". I checked the carve-out is honoured in both
directions — see item 3, where exactly 0 non-DERIVED rows carry arithmetic and 0 DERIVED rows lack it.

---

## Item 3 — derived_arithmetic coverage — **CONFIRMED 29/29**, one 1-cent label residual

### Coverage

Script `E:\tmp\qoder_audit6\derived_check.py`:

```
DERIVED rows: 29
DERIVED rows with EMPTY derived_arithmetic: []
non-DERIVED rows carrying arithmetic: []
```

29/29 coverage confirmed — the closure agent's number is right. `quantitative.csv` evidence_class census
(`Counter` over all 111 rows) is `FACT (audited)` 40, `DERIVED` 29, `FACT` 18, `UNKNOWN` 9,
`FACT (company claim)` 3, `FACT (as disclosed)` 3, `FACT (company self-measured)` 2, and nine singletons.

*A trap I checked rather than fell into:* filtering on the substring `ESTIMATE` as well as `DERIVED`
returns **30** rows, because `quantitative.csv:84` has evidence_class
`FACT (third-party estimate quoted in a filing)` and a legitimately empty `derived_arithmetic`. That row
is an observed IDC figure quoted inside the S-1, not a calculation of ours, so an empty arithmetic cell is
correct per `00_METHOD_AND_STYLE.md:277–278`. A verifier who counted "29 expected, 30 found" and reported
a coverage defect would be wrong; exact-match on `DERIVED` gives 29.

### Recomputation of all 29, independently

Every arithmetic string was re-run from its own stated inputs (no reuse of the register's intermediates):

| CSV record (file line) | Metric | Arithmetic as filed | My recomputation | Result |
|---|---|---|---|---|
| L5 | founder price/share, instrument basis | 10,000 / 1,700,000 | 0.00588235 | ✓ = 0.005882 |
| L6 | founder price/share, restated basis | 10,000 / 10,200,000 | 0.000980392 | ✓ = 0.00098 |
| L9 | first reporting period length | 26+31+30+31+30+31 | 179; `date(1994,12,31)-date(1994,7,5)` = 179 days | ✓ |
| L22 | Miguel A. Bezos purchase | 582,528 × 0.1717 | 100,020.0576 | ✓ = $100,020.06 |
| L24 | Gise Family Trust purchase | 847,716 × 0.1717 | 145,552.8372 | ✓ = $145,552.84 |
| L28 | Alberg purchase (both conventions) | 150,000 × 0.3333; 150,000 × 1,007,000/3,021,000 | 49,995.0; 50,000.0 | ✓ both |
| L30 | Feb→Dec 1995 price step-up | (0.3333−0.1717)/0.1717; (0.33333−0.1717)/0.1717 | 0.9411765; 0.9413706 | ✓ both → +94.1%; the stated "differ by 0.02 pp" is right (0.0194 pp) |
| L32 | in-window $0.1717 tranche | 582,528+847,716 = 1,430,244 × 0.1717 | 1,430,244 ✓; product **245,572.8948** → $245,573 | ✓ (and see the note below on $245,572) |
| L34 | named related-party CY1995 total | "100,020.06 + 145,552.84 + 49,995 = $295,567.89" | unrounded sum 295,567.8948 → $295,567.89 ✓; **sum of the three DISPLAYED addends = 295,567.90** | value ✓; see residual |
| L35 | residual unnamed-purchaser cash | 1,272,000 − 295,568 | 976,432 | ✓ |
| L42 | gross margin FY1995 | 102/511 | 19.96086% | ✓ = 19.96% |
| L44 | marketing/share of sales | 200/511 | 39.13894% | ✓ = 39.14% → 39.1% |
| L47 | total opex FY1995 | 200+171+35 | 406 | ✓ |
| L52 | loss per $1 of net sales | 304/511 | 0.594912 | ✓ = $0.595 |
| L53 | contribution per $1 | 0.1996 − 0.3914 | −0.1918 | ✓ |
| L55 | two filed loss years + tie to deficit | 52+303 = 355; 355−107 | 355; 248 | ✓ both |
| L58 | international share | 198/511 | 38.74755% | ✓ = 38.7476% → ≈38.7% |
| L61 | total cash consumed FY1995 | 232+52 | 284 | ✓ |
| L66 | cash bridge | −232 − 52 + 1,228 = +944; 52 + 944 | 944; 996 | ✓ (filed terms verified against the filing — item 4) |
| L68 | net equipment book value | 81 − 24 | 57 | ✓ |
| L69 | cumulative cash-paid capex | 28 + 52 | 80 | ✓ |
| L71 | inventory as share of sales | 17/511 | 3.32681% | ✓ = 3.33% |
| L76 | net sales per year-end employee | 511,000/11 | 46,454.545 | ✓ → $46,455 |
| L83 | Amazon share of 1995 Web purchases | 511,000/318,000,000 | 0.16069% | ✓ = 0.161% |
| L85 | implied runway | 996/284 | 3.50704 | ✓ = 3.51 years |
| L98 | price × share cross-check | 3,021,000 × 0.3333; 1,007,000 ÷ 3,021,000 | 1,006,899.30; 0.3333333 | ✓ both (see item 8) |
| L100 | average per purchaser | 1,007,000/23 | 43,782.609 | ✓ ≈ $43,783 |
| L108 | advertised-minus-sourceable gap | 2,500,000 − 400,000 | 2,100,000 | ✓ |
| L112 | net sales per trading week (band) | 511,000 ÷ (5.5 × 4.345 = 23.8975); 511,000 ÷ (184/7 = 26.2857) | 21,382.98985 → 21,382.99 ✓; 19,440.2174 → 19,440.22 ✓ | ✓ both ends, band `19440-21383` correct |

**Zero mismatches between a stored `value` and its recomputed arithmetic.** All 29 values are right.

### On $245,572 — the fabricated figure this brief warned about

`quantitative.csv:32` stores `245573`, and its arithmetic string gives the product as `$245,573`. My
independent product is 1,430,244 × 0.1717 = **245,572.8948**, i.e. $245,572.89 ≈ **$245,573**. The register
rounds correctly; a repo-wide grep for `$245,572` as a *live value* is handled in item 13 — the surviving
hits are all in the rejection record (`_parts/NUMBER_DEFECTS.md:52` "the `$245,572` claim is absent as a
figure and correctly rejected (COR-14.2)"). The repair is real.

### Residual (named, low severity) — `quantitative.csv:34`

The `derived_arithmetic` cell reads verbatim:

> `$100,020.06 + $145,552.84 + $49,995 = $295,567.89 → $295,568`

The three displayed addends sum to **$295,567.90**, not $295,567.89. The stated total is the sum of the
*unrounded* products (100,020.0576 + 145,552.8372 + 49,995 = 295,567.8948), so the total is right but the
string shows rounded addends and then a total that those addends do not produce. `quantitative.csv:22` and
`:24` display the cent values (`$100,020.0576 → $100,020.06`, `$145,552.8372 → $145,552.84`) while `:34`
sums at a different precision than it prints. The stored value `295568` is unaffected and no live claim
breaks; the defect is that the field exists so the arithmetic is re-runnable from what is printed
(`00_METHOD_AND_STYLE.md:42`, "the arithmetic must be shown"), and this string is not. One-cent cosmetic;
reporting, not fixing. The identical string is repeated at `stage_1.md:925` (§P.2 d7), so the residual covers
two sites, not one.

---

## Item 4 — the dead bridge — **DEFECT**

The brief writes the dead bridge as `52 − 232 − 52 + 1,228 = 996`. That string is **arithmetically true**
(LHS = 996; checked in Python: `52-232-52+1228 == 996`). The equation that was actually false, and which the
repair record identifies as the defect (verify-3 F-1 / RD-029), is the same left-hand side set equal to
**944**. I tested **both** readings so the verdict does not depend on which one the brief meant.

### The replacement matches the filed terms — verified line by line against the local filing

`company_001_amazon/sources/S-1_original_acc-0000891618-97-001309_filed-1997-03-24.txt`, read directly:

| Cited line | Filed text (columns: 1994 stub / FY1995 / cumulative) | Matches replacement? |
|---|---|---|
| l.3636 | `Net cash used in operating activities........... (24) (232) (1,735)` | ✓ −232 |
| l.3641 | `Net cash used in investing activities........... (28) (52) (1,214)` | ✓ −52 |
| l.3649 | `Net cash provided by financing activities....... 104 1,228 8,201` | ✓ +1,228 |
| l.3652 | `Net increase in cash................................... 52 944 5,252` | ✓ filed net-increase is 944 |
| l.3653 | `Cash and cash equivalents at beginning of year.. -- 52 996` | ✓ opening 52 |
| l.3655 | `Cash and cash equivalents at end of year....... $ 52 $ 996 $ 6,248` | ✓ closing 996 |

S-1/A No. 5, cited as the second accession at l.3923/3928/3940/3942–3947, prints the identical bridge (I read
it: `(232)` at l.3923, `(52)` at l.3928, `1,228` at l.3940, `944` at l.3942, beginning `52` at l.3944, end
`$ 996` at l.3947). **This half is CONFIRMED**: `−232 − 52 + 1,228 = +944`, then `52 + 944 = 996` is the
filing's own two-line statement, both endpoints filed, nothing invented, and the closure's insistence that
"Nothing in the bridge is UNKNOWN and no figure needed inventing to close it" (`stage_1.md:984–985`) is right.

### Where it fails

A whole-repo multi-line grep for the bridge (pattern `52 ?[−-] ?232 … 1,?228 … = … 944`) returns, among the
legitimate retraction sites, this **live, unannotated** instance. It is invisible to a single-line grep
because it wraps across the line break — which is why I ran it multiline:

```
founders_playbook\01_companies\company_001_amazon\_parts\s1_p4.md:102
    39%" — an internal cross-check, not a new source. d13 `232 + 52 = $284,000 consumed`. d14 `52 − 232 − 52 +
founders_playbook\01_companies\company_001_amazon\_parts\s1_p4.md:103
    1,228 = +944; 52 + 944 = $996` (ties to the audited closing cash to the dollar). d15 `81 − 24
```

`_parts/` is not scratch. `00_METHOD_AND_STYLE.md:187–188` makes parts "volumes of one document, not separate
documents", with numbering continuing across them. The false equation therefore still prints inside the
report, in §P.2 d14 of volume 4, with no retraction marker on it — and the same fragment still carries the
pre-repair d4 `$100,019.06`, d5 `$145,552.83` and d7 `$295,567` at `_parts/s1_p4.md:96–98`.

**And the closure's summary claim is contradicted by its own next table row.**
`03_quality_control/amazon_s1_numeric_closure_final.md:29`: "The false form `52 − 232 − 52 + 1,228 = 944`
survives in exactly three places, all of them retractions … Sweep for a surviving live instance of the false
equation across all registers, **parts** and claim records: **0**". Thirteen lines later the same sheet's
residual R-4 (`:42`) states the deleted false bridge "**still prints live** in `_parts/s1_p4.md`
ll. 102–103". Both cannot be true. The "0" is what was signed; R-4 is what is on disk. This is precisely the
pattern the brief warned about — the closer's own sweep statement being wrong in the direction of closure.

Under the literal reading of the brief (the `= 996` form) the answer has the same shape: that form appears
live in a §P table row at `stage_1.md:864` (P36) — where it is correct and is now explicitly annotated
("this row's left-hand side already includes the 52,000 opening, so its sum is 996,000", and re-explained at
`stage_1.md:985–986`) — but appears **unannotated** at `_parts/s1_p4.md:62`. `quantitative.csv:66` and
`validation.csv:17` hold theirs inside correction prose, which is compliant.

Compliant retraction sites, for the record: `stage_1.md:978–987`; `quantitative.csv:66` (`derived_arithmetic`
carries the filed form; the false form appears only in `notes` as "this cell read … and the equation is
false"); `validation.csv:17`. Historical QC sheets (`03_quality_control/amazon_s1_audit2_citation_check.md:560`
and `:622`; `amazon_s1_audit3_numbers.md:145`) print the false form as a *passing* check — those are the
superseded audit trail, not live claims, and retro-editing them would itself breach audit integrity;
`amazon_s1_audit3_recheck.md:217` and `amazon_s1_audit3_verify3.md:157` are their retractions, and I note
`amazon_s1_audit3_numbers.md:145` as the original sin ("**PASS + tie confirmed**" on a false equation).

**Verdict: DEFECT** — narrow but real: one live unannotated copy at `_parts/s1_p4.md:102–103`, and one false
zero-count asserted at `amazon_s1_numeric_closure_final.md:29`.

---

## Item 5 — `21,382.98` is retraction-only — **CONFIRMED**

`grep -rnF "21,382.98"` over the whole repo, `*.md` and `*.csv`, returns exactly 6 hits. Every one sits inside
a sentence that identifies it as the wrong value:

| File:line | Context |
|---|---|
| `company_001_amazon/quantitative.csv:112` | in the `notes` column only: "**this cell carried 21,382.98 — a truncation introduced when §P.2 d30 was copied into the register**". The `derived_arithmetic` column of the same row reads `= 21,382.99 → $21,383` |
| `company_001_amazon/stage_1.md:1058` | "…and was truncated to 21,382.98 when d30 was copied into `quantitative.csv` L112" |
| `03_quality_control/amazon_s1_audit3_verify3.md:158` | finding F-2, quoting the defective cell |
| `03_quality_control/amazon_s1_audit3_verify3.md:259` | RD-030: "Correct `21,382.98` → `21,382.99`" |
| `03_quality_control/amazon_s1_numeric_closure_final.md:28` | the closure record of the retraction |
| `founders_playbook/MASTER_RESEARCH_LOG.md:539` | "`21,382.98` proved to be inside a retraction sentence rather than a live value" |

Zero hits in `conflicts.csv`, `_parts/`, `context_appendices.md`, `stage_1_claim_records.md`, `sources/`. The
live renderings elsewhere are all the correct `21,382.99` / `$21,383` (`conflicts.csv:10`,
`stage_1.md:1055`, `stage_1.md:1156`), and I re-derived the quotient independently:
`511,000 ÷ 23.8975 = 21,382.98985` → rounds to 21,382.9**9**. The repair is right and so is the closure's
"exactly one occurrence, and it is a retraction". **CONFIRMED.**

---

## Item 6 — retracted denominators `2,613,000` / `$871,024` / `$871,000` — **DEFECT**

### The premise first: is `2,613,000` really unfiled? Yes — independently checked

`grep -c` for `2,613,000`, and for the no-separator form `2613000`, across every text file in `sources/`:

```
10-K_FY1997…1998-03-30.txt           : 0     S-1A-No3…1997-05-09.txt     : 0
424B1_final-prospectus…868.txt       : 0     S-1A-No5…1997-05-14.txt     : 0
S-1_original…1309.txt                : 0     historylink-essay….txt      : 0
s1_0000891020-97-000839.txt          : 0     sheff-playboy-interview….txt: 0
s1_original_0000891618-97-001309.txt : 0
```

Controls on the same method: `3,021,000`, `2,811,000`, `4,235,244` and `1,007,000` are all present in those
files. So the register's assertion is true and the retraction is grounded. `2,763,000` is likewise absent
(0 hits) and is reachable only as `4,235,244 − 582,528 − 847,716 − 42,000` (my own arithmetic returns exactly
2,763,000), i.e. the d25 chain the register itself refuses to adopt.

### Where the retraction WAS applied — checked site by site

`stage_1.md:216, 584, 848, 1149, 1157, 1177, 1486–1506, 1525–1536` (U.8 RETRACTED-FIGURE RECORD);
`quantitative.csv:35` (value `976000`, composition leg UNKNOWN) and `:99` (`UNKNOWN`, "RECORDED BUT NOT
ADOPTED"); `data_gaps.csv:11`; `conflicts.csv:9` ("THIS ROUND RETRACTS THE CHAIN AND SUBSTITUTES NO THIRD
NUMBER"); `stage_1_claim_records.md:462` (P09) and `:562`. Each carries both spellings inside explicit
retraction language and states the filed alternative. The new positive claims in that family also compute —
`5,408 + 150,000 − 50,000 = 105,408` ✓; `2,811,000 ÷ 3 = 937,000` ✓;
`5,408 + 150,000 + 937,000 − 50,000 = 1,042,408` ✓; overshoot over the audited residual `1,042,408 − 976,432 =
65,976`, i.e. the stated "≈$66,000" ✓; `150,000 + 60,000 + 2,811,000 = 3,021,000` and `1 + 2 + 20 = 23` ✓
against `sources/S-1A-No5…1997-05-14.txt:4662–4668` (read verbatim); `3,021,000 ÷ 3 = 1,007,000` ✓; and orig.
l.4300–4302 contains `3,021,000 / 23 investors / $.3333 / $1,007,000` and **not** `2,613,000` ✓. The
"two figures differ by $24" line is right too: `871,024 − 871,000 = 24` ✓.

### Where it fails: `context_appendices.md` still runs the leg live

`context_appendices.md:596` is a row of the §I quantitative context table whose header is at `:583`,
`| Metric | Value | Unit | Date | Publisher of figure | Source date | What it measured | Confidence |`. The
offending text therefore sits in the **Value column** (column 2):

> `| Capital raised inside Stage 1 | … CY1995 common-equity cash $1,272,000, of which **$295,568 named (±$5)**
> and **≈$976,000 un-named** = $5,408 (1995-08-07 employee purchase) + $150,000 advances for unissued shares +
> **$871,000** unaffiliated program shares (2,613,000 × the filing's exact ⅓ = 2,613,000 ÷ 3 = $871,000
> exactly) − $50,000 of 1994 advances applied = **$976,408** … the six-figure one-third leg printed here earlier
> was a back-solved balancing plug and is **retracted** …`

The row retracts `$871,024` while keeping `$871,000`, `2,613,000` and the withdrawn `$976,408` composition as
live arithmetic. **`context_appendices.md:639`** is live on the same leg: "identity of the residual ~$976,000
(±$1,000) of 1995 purchasers — **only ~$871,000 of it is anonymous share money**, the rest being a disclosed
$5,408 purchase, $150,000 of advances for unissued shares and a $50,000 1994 carry-over".

That falsifies `03_quality_control/amazon_s1_numeric_closure_final.md:17` (N-1): "**`$871,024`** … and
**`$871,000`** … both survive **only as retractions** … **no live value cell carries either**". A value cell
does.

**The aggravating fact:** this is not new. It was written up with these same two line numbers as attack
**S2E-28** in `company_001_amazon/research/ST2_E_adversarial.md:895–922`, graded "**Certain**", concluding
"**Stage 2 must draw no capital figures from context_appendices.md**" until it is fixed. A Stage-2 dossier had
to tell the Stage-1 closer that its own appendix still launders a retracted figure. Severity: this is the
third instance of the pattern this project has now been caught in twice before (the `$245,572` fabrication,
the `+95.2%` invented sensitivity) — a retracted number surviving in the file a downstream miner reads, while
the closing sheet certifies the sweep.

**Verdict: DEFECT.** Two live sites, one of them in a Value column.

---

## Item 7 — U.41 single-pointer — **CONFIRMED** (one adjacent register defect, named)

**Convention check first.** `U.41` is a `**U.41 — …**` block at `stage_1.md:2203`; the anchored grep
`grep -nE "^\*\*U\.41 — "` returns exactly 1. Total `U.41` strings in the file: 15 lines / 17 occurrences.
Every one classified:

| Line | Kind | Basis |
|---|---|---|
| `stage_1.md:347` (§E version table; `## E.` opens at `:318`) | **the one live pointer** — confidence cell `Medium-High → U.41` | same object as the block: Associates Program, 1996-07, 4,800+ at 1996-12-31 |
| `stage_1.md:497` (§H) | id quotation, not a pointer | the pointer in the same sentence at `:496` reads `→ **U.43**` |
| `stage_1.md:1830` (inside U.21) | id quotation | "absorbs claims_AJ's U.41", a superseded part-local key |
| `stage_1.md:2243` (inside U.42) | range statement | "the same treatment in U.1–U.41", fenced by the spine note at `:2244–2245` |
| `stage_1.md:2253` (inside U.43) | history sentence | names the three routes that "now read → U.43" |
| `stage_1.md:2203` | the block header | — |
| `stage_1.md:2218–2231` | the reconciliation note itself | adds mentions of the id, adds no pointer |

**1 live pointer, 1 block — they match.** The three former misroutes are demonstrably re-pointed: `:288`
(§D.1), `:496` (§H), `:809` (§O.7) and `:1152` (§R Distribution) all carry `→ U.43`, and none of them still
carries `→ U.41` — §D.1 and §R contain no `U.41` string at all (confirmed by the 17-occurrence table).
Register mirrors hold: `conflicts.csv` U.41 at file line 42, U.43 at file line 44;
`stage_1_claim_records.md:260` (F17) and `:367` (J12) key `Conflicts: U.41` and both are Associates rows;
`sources.csv:45` (S0608) keys the Associates start date to U.41.

**No duplicate live claim.** U.41's CLAIM A ("…making it a shipped, scaled **Stage-1** system") was the
mislabelling under adjudication. Repo-wide greps for `shipped, scaled` and `scaled Stage-1` return only
quotation sites: `stage_1.md:2204` and `conflicts.csv:42` (both inside CLAIM A itself), plus the origin
dossiers `research/F_technology.md:167` and `_parts/s1_claims_AJ.md:312` (working volumes, not the report).
Every surviving in-report mention of the program is fenced: `stage_1.md:347` labelled
`1996-07 *(post-boundary)*`; `stage_1.md:1152` "the Associates Program (4,800+ members) is 1996 —
post-boundary"; `channels.csv:16` stage `stage2-consequence`; `timeline.csv:55` stage `stage2-consequence`;
`context_appendices.md:416` "the Associates Program (1996; …)".

**Named adjacent defect, found while walking the pointer graph.** `timeline.csv:55` is the Associates row —
`event = Associates Program begins; more than 4,800 registered members by 1996-12-31`,
`notes = stage2-consequence: hyperlink syndication is NOT a Stage-1 channel and must not be imported
backwards` — and its `conflict_ref` is **U.16**, which is "The launch release carries two dates"
(`stage_1.md:1722`). That note is U.41's subject verbatim. The same mis-key hits `timeline.csv:33`
(directory listing; "no independent dated listing for amazon.com survives"; the NCSA null) — U.43's subject —
also keyed **U.16**. A `conflict_ref` census over all 57 `timeline.csv` rows:
`{None 15, U.8 7, U.4 5, U.1 4, U.27 3, U.9 3, U.16 3, U.7 2, U.18 2, U.15 2, U.21 2, U.3 2, U.31 1, U.6 1,
U.2 1, U.23 1, U.13 1, U.17 1, U.11 1}` — **zero** references to U.41 and **zero** to U.43. The reconciliation
note at `stage_1.md:2228–2231` enumerated `conflicts.csv`, `stage_1_claim_records.md` and `sources.csv` but
never `timeline.csv`, so "Live pointers to U.41: 1" is true of the prose volume and incomplete across the
register set. Reported; item 7 as literally stated is still **CONFIRMED**.

---

## Item 8 — COR-10 / COR-12 coherence — **DEFECT**

### (a) $1,006,899.30 recomputes from the filed share count and price — CONFIRMED

Filed, `sources/S-1_original_acc-0000891618-97-001309_filed-1997-03-24.txt:4300–4302`, verbatim:
*"Between December 6, 1995 and May 16, 1996, the registrant issued an aggregate of **3,021,000** shares of
Common Stock to **23 investors** for a consideration of approximately **$.3333 per share**, or an aggregate of
**$1,007,000**."*

`3,021,000 × 0.3333 = 1,006,899.30` (Python: `1006899.2999999999`, i.e. exactly 1,006,899.30). Reverse check:
`1,007,000 ÷ 3,021,000 = 0.33333333…`, so the aggregate is the precise figure and the printed price the rounded
one — which is what `CORRECTIONS.md:176–179` now says and what `quantitative.csv:98` states in both directions.
The related cross-references hold: `amazon_s1_audit3_recheck.md:160` and `_parts/NUMBER_DEFECTS.md:57`
(`3,021,000 × ⅓ = 1,007,000`) ✓. COR-10's other directives are honoured: the DERIVED reconciliation row exists
(`stage_1.md:584`, "deliberately not averaged"), `$8,000,014`/`$200,000` are fenced post-boundary
(`stage_1.md:1516`; `_parts/NUMBER_DEFECTS.md:51` records that the transposed `$8,000,140` appears nowhere),
and the program is not presented as a Stage-1-only raise (`stage_1.md:1149`, `:1506–1509`).

### (b) COR-12's supersession of COR-03 — NOT stated consistently

Where the supersession **is** stated (each site read, not counted): `stage_1.md:15–18`; `stage_1.md:870` (P42);
`stage_1.md:1125` (§Q); `stage_1.md:1139` (§R); `stage_1.md:1738` (U.17);
`stage_1_claim_records.md:26–28` and `:615`; `context_appendices.md:595`; `timeline.csv:49`;
`quantitative.csv:74`. That part is genuinely thorough.

Where it is not:

1. **`CORRECTIONS.md:57–69` — COR-03's own section carries no supersession marker.** The heading is still
   `## COR-03 — the employee count is a January figure, not a December one`, and its action still commands the
   reversed rule verbatim: "**Action:** section R and P state `11 employees (per the filing: at 1996-01-01)`"
   (`:66`). There is no `[SUPERSEDED BY COR-12]` line anywhere in the block. The file has no global supersession
   table — I read `:1–20`; the header carries only the rule at `:8–11` that "**Reverting one is a defect**".
   The supersession appears only at `:225`, 156 lines later, and `CORRECTIONS.md:185–186` warns that COR-11 and
   COR-10 were "placed here in file order", so a reader working the register top-down meets the retracted
   instruction first. A corrections register that leaves its own retracted entry unmarked in place fails the
   standard it sets at its own line 8.
2. **`CORRECTIONS.md:194`** — COR-11.2 still routes the reader onward with "(both are post-boundary anyway;
   **see COR-03**)", pointing at the superseded entry with no mention of COR-12.
3. **`company_001_amazon/_parts/s1_p3b_H_addendum.md:131`** — "Not folded in: H-21/H-48, H-22/H-49 (headcount,
   people register) — already in §B/§J/§R **with COR-03's phrasing**". Parts are volumes of one document
   (`00_METHOD_AND_STYLE.md:187`); this one still describes the retracted phrasing as current.

### (c) The seam item 8 was really a hook for

COR-12's own rule text, `CORRECTIONS.md:241–242`, says the original S-1's 1996-01-01 phrasing "should be
*added* as **corroboration**, not substituted", and `stage_1.md:16–17` renders that as "with the original S-1's
1996-01-01 phrasing as **independent corroboration** of the same population". That wording predates the
2026-09-24 restatement of method §3 and is the exact error §3 names
(`00_METHOD_AND_STYLE.md:53–55`: "Two agents counted a figure as 'corroborated in the original S-1 and in
S-1/A No. 5' when the second is the same instrument refiled"). Item 9 carries it; I do not double-count it.

**Verdict: DEFECT** on limb (b). Limb (a) — the arithmetic the brief asked me to recompute — is CONFIRMED.

---

## Item 9 — filing-lineage demotions — **DEFECT (substantial)**

The rule under test is `00_METHOD_AND_STYLE.md:51–59`, as restated for this finding: an S-1, its amendments,
"exhibits to the same accession" and "a prospectus and the filing that superseded it" are **one source**, and
`independence_note` must say `same lineage as S00xx`. RD-041's own site list is
`MASTER_RESEARCH_LOG.md:512`: "`stage_1.md` header, §G.3, §J, §T, §U.1; 22 claim records; `conflicts.csv`
U.1/U.8/U.9", with status "**PARTLY CLOSED (2026-09-24)** — the header ruling is written, both narrative sites
and the §T doctrine row are capped".

### What was actually done — and it is not trivial

`sources.csv` is fully demoted, all five lineage members, and I read each `independence_note`:
`S0801` "THE SINGLE LARGEST ANCESTOR IN THE CORPUS … S0802-S0805 largely restate it, so those are ONE
corroborating instrument"; `S0802` "Second state of the same registration statement as S0801: repetition here
is NOT corroboration, and where the two differ only in rounding that is not corroboration either";
`S0803` "Third state … therefore NOT an independent source for anything already in S0801"; `S0804` (424B1)
"Fourth state of the same registration statement, so no independence at all for content shared with S0801";
`S0805` (10-K405) "Restates S0801 material and is therefore not independent of it". ✓
The claim-record re-key is real: `stage_1_claim_records.md:46–60` and `:580–585` record 22 records moved to
`Corroboration: 1 (same lineage as S0801)` with **2 deliberately left at 2** on stated grounds (**L05**
filing-vs-*LA Times*; **P13** release-vs-filing), and I confirmed both survivors are genuinely two origins.
`stage_1.md:431` (§G.3), `:560` (§J), `:1203` (§T S-1/A No. 5) and `:1280` (U.1) all carry the demotion in the
right words — e.g. `:431`: "they are **two states of one registration statement** … one instrument restated,
not corroboration (method §3 filing-lineage rule; A-B1)".

### Places that still count agreement between those filings as independent corroboration

I grepped for the phrasings the volume itself withdrew (`independent corroboration`, `genuinely corroborat`,
`gain independence`, `corroborat` near a second accession). Five live sites:

| # | Site | Text | Why it is the prohibited count |
|---|---|---|---|
| 1 | **`stage_1.md:16–17`** — inside the header block that `MASTER_RESEARCH_LOG.md:512` marks capped | "the original S-1's 1996-01-01 phrasing as **independent corroboration** of the same population" | The words "independent corroboration", between the S-1 original and its own amendments. It sits **19 lines above** the new ruling paragraph at `stage_1.md:35–47` which says the opposite: "Repetition across accessions is therefore **version evidence** … and never a second corroboration" (`:39–40`) and "Where this volume previously wrote that a disclosure 'gained independence' or was 'genuinely corroborated' by appearing in two accessions, **that phrasing is withdrawn**" (`:40–41`). The volume contradicts itself inside one header block. |
| 2 | **`stage_1.md:1139`** — §R Employees | "the original S-1's 'from January 1, 1996 …' is **independent corroboration** of the same population at the 1995/96 turn", plus the Source cell "S-1 (orig.), Risk Factors [T1 · FACT — **corroboration**]" | Same error, in the end-of-stage snapshot — the most re-read cell in the file. |
| 3 | **`quantitative.csv:74`** | `source` = "S-1/A No. 3 Risk Factors; S-1/A No. 5 Risk Factors (**corroborated by** S-1 (orig.), Risk Factors)" | A register row crediting the accession ancestor with corroboration of its own amendments. |
| 4 | **`stage_1.md:870`** (§P42) | "which **corroborates** the count rather than displacing the date" | Milder (it denies displacement) but still uses the counted word for a same-lineage document. |
| 5 | **`context_appendices.md:595`** | "**corroboration of the same population** at the 1995/96 turn, not a competing date" | Same, in the appendix volume a downstream pass mines. |
| 6 | **`CORRECTIONS.md:241–242`** (COR-12's rule) | "The original S-1's 1996-01-01 phrasing should be *added* as **corroboration**, not substituted" | This is the *instruction* that generated sites 1–5, and it is still the standing rule. Fixing the downstream sentences without fixing COR-12 guarantees regeneration. |

### §T: three of the five lineage rows were never demoted

`§T` opens at `stage_1.md:1189` and its own preamble at `:1197–1198` says the abridged independence column
"exists only to stop a reader double-counting corroboration". Reading `:1202–1206` in full:

| Row | Line | Independence note present? |
|---|---|---|
| S-1 (original) | `:1202` | ✓ "Ancestor of nearly everything below; one instrument, not many" |
| S-1/A No. 5 | `:1203` | ✓ the fullest treatment in the file |
| **S-1/A No. 3** | `:1204` | ✗ **none.** "High — **restored**, 306,425 B. The adversarial dossier's 'Amendment No. 4, 9 May 1997' is No. 3 by the file's own label" — no lineage note at all, though `sources.csv` S0802 has one |
| **10-K405** | `:1205` | ✗ only "Largely repeats the S-1 text" — descriptive, not a demotion, and no `same lineage as S0801` |
| **424B1** | `:1206` | ✗ **no lineage note at all** — and its status cell still reads "Medium — **restoration pending**" while `sources/424B1_final-prospectus_acc-0000891020-97-000868_filed-1997-05-15.txt` is on disk at 266,755 B. (The stale status is self-declared as residual R-8 at `amazon_s1_numeric_closure_final.md:46`; the missing demotion is not on any residual list.) |

The item-9 brief asks specifically about "the S-1 original, its amendments **and the 424B1**" — the 424B1 row
is the one §T row that received neither the demotion nor a current restoration status.

### Claim records: the re-key used a `count == 2` rule, so records at 3 and 4 escaped

`stage_1_claim_records.md:46–50` describes exactly that trigger ("Twenty-two records … carried
`Corroboration: 2`"). I extracted every `Corroboration:` value in the appendix: 52 populated fields, 9 at ≥2,
of which **5 are at 3 or 4** and none of the five was touched:

| Record | Line | Field | Assessment |
|---|---|---|---|
| **L01** | `:397` | `Corroboration: 4 (424B1; Amazon PR 1996-06-13 "less than a year ago"; Amazon PR 1999-06-07; Seattle Times 1997-05-13)`, Source line already including "10-K FY1997 repeats (T01, T02, T03)" | **Clear violation.** 424B1 *and* the 10-K405 are lineage members named by §3 itself; two of the four are Amazon's own later releases repeating the same corporate record. A defensible count is 1 lineage + *Seattle Times* = 2. |
| **P01** ($511,000 net sales) | `:454` | `Corroboration: 3`, Source = "Amazon.com Form S-1, Selected Financial Data (T02)" only | **Clear violation.** No non-lineage origin is named anywhere in the record, and `conflicts.csv:10` (U.9) states for this same figure that "the identical figure recurs in S0803, which is the SAME registration lineage as S0801 and so is version evidence, not a second confirmation". The register row and the conflict row contradict each other about the same number. |
| **K04** (Cadabra subscription) | `:383` | `Corroboration: 3`, Source = "Form S-1 Exhibit 10.12 …; Management — Certain Transactions (T01, T02)" | **Violation on §3's own "exhibits to the same accession" limb.** The record's own bracketed COR-02 note says the fact is "in the ORIGINAL S-1 only — absent from S-1/A No. 3, No. 5 and the FY1997 10-K405", so no second instrument exists to corroborate anything; the three are exhibit + body + dossier restatements. |
| M05 (repeat-purchase %) | `:412` | `Corroboration: 3` | Questionable but arguable — the WSJ and Seattle Times legs are independent; the S-1 leg is not. Flagged for review, not asserted as a defect. |
| L06 (1M titles / 10–40%) | `:402` | `Corroboration: 3 (June 1996 release; LA Times 1996-12-11; Wired 1996-12-16)` | Two genuinely independent papers; but the second company release is the same origin story under `00_METHOD_AND_STYLE.md:49`. Flagged, not asserted. |

The closure never claims to have looked at records above 2 — `causal_lineage_closure.md:51` reports "22 records
re-keyed … **2 records were left at 2**", a census with no row for 3 or 4. That is the mechanism of the miss.

### Why the closer could not see it

`amazon_s1_causal_lineage_closure.md:35–40` counts demotion **markers**: "`stage_1.md` | **4** | ll. 431, 560,
1203, 1280". A marker census finds text that was fixed; it cannot find text that was never rewritten. The
contradicting phrases at `stage_1.md:17` and `:1139` contain no marker, so the count of 4 was arithmetically
correct and evidentially useless, and `:86` then upgrades it to "the same-registration-lineage double count is
demoted at **all 31 named sites**". "All named sites" is the tell: the site list came from the census, not
from the attack.

**Verdict: DEFECT.** The demotion is real in `sources.csv`, in the 22 re-keyed records, and at three of the
four prose sites; it is incomplete at §T (No. 3 / 10-K405 / 424B1), at six live "corroboration" sites including
the header that RD-041 marks capped and the §R snapshot, in `quantitative.csv:74`, in at least three claim
records at `Corroboration: 3–4`, and its standing cause — COR-12's instruction — is unrevised.

---

## Item 10 — §P.2 recomputed in full — **CONFIRMED**, one shared 1-cent label defect

I read §P.2 end to end (`stage_1.md:899–1067`) and re-ran every figure in the d-chain independently. §P.2
carries d1–d30 plus the interpolated **d8a**, **d15a** and **d23a**-class sub-notes; all 32 are below.

| d | line | stated arithmetic | my recomputation | verdict |
|---|---|---|---|---|
| d1 | 909 | 10,000 ÷ 1,700,000 = $0.005882 | 0.00588235 | ✓ |
| d2 | 910 | 10,000 ÷ 10,200,000 = $0.00098; "the counts differ by a factor of exactly 6 = 4:1 × 3:2" | 0.000980392; 10,200,000/1,700,000 = 6.000; 4 × 1.5 = 6 | ✓ both |
| d3 | 911–912 | 26+31+30+31+30+31 = 179; "the inclusive count … is 180" | 179 (and `date(1994,12,31)-date(1994,7,5)` = 179); 180 | ✓ |
| d4 | 914–915 | 582,528 × 0.1717 = $100,020.0576 → $100,020.06; "the earlier product was wrong by exactly $1.00" | 100,020.0576; 100,020.06 − 100,019.06 = 1.00 | ✓ |
| d5 | 917 | 847,716 × 0.1717 = $145,552.8372 → $145,552.84 | 145,552.8372 | ✓ |
| d6 | 918–924 | (0.3333−0.1717)/0.1717 = 0.94118; exact-⅓ form 0.94137; "differ by 0.02 pp (94.12 vs 94.14)"; "+95.2% would need $0.1708" | 0.9411765; 0.9413706; 0.0194 pp; 0.33333/1.952 = 0.170763 | ✓ all four |
| d7 | 925–928 | "100,020.06 + 145,552.84 + 49,995 = $295,567.89 → $295,568"; "±$5 is the only honest precision"; exact-⅓ variant $295,572.89 | **displayed addends sum to 295,567.90**; unrounded sum 295,567.8948 → $295,567.89 ✓; 295,567.89 + 5 = 295,572.89 ✓ | **mismatch in the printed addends only** — see below |
| d8 | 929 | 1,272,000 − 295,568 = $976,432, rendered ≈$976,000 (±$1,000), spans ≈$974,900–$977,900 | 976,432 ✓; band arithmetic ✓ (±500 on each of two inputs) | ✓ |
| d8a | 934–971 | 5,408 + 150,000 − 50,000 = 105,408; 2,811,000 ÷ 3 = 937,000; 5,408+150,000+937,000−50,000 = 1,042,408, "overshoots … by ≈$66,000"; 245,572.89 + 5,408 + 921,000 − 50,000 + 150,000 = 1,271,980.89 (the "$19 term"); 3,021,000 ÷ 3 = 1,007,000 | 105,408 ✓; 937,000 ✓; 1,042,408 ✓; 1,042,408 − 976,432 = **65,976** ≈ 66,000 ✓; 1,271,980.89 ✓ and 1,272,000 − 1,271,980.89 = 19.11 ≈ $19 ✓; 1,007,000 ✓ | ✓ all six |
| d9 | 971 | 102 ÷ 511 = 19.961% | 19.960861 | ✓ |
| d10 | 972 | 200 + 171 + 35 = 406 | 406 | ✓ |
| d11 | 973 | 304 ÷ 511 = 0.5949 | 0.594912 | ✓ |
| d12 | 974–977 | 198 ÷ 511 = 38.7476%; band "38.61–38.88%" from ±$500 inputs; 5.1 ÷ 15.746 = 32.4% | 38.74755; 197.5/511.5 = 38.612% and 198.5/510.5 = 38.884% ✓; 32.389% | ✓ all three |
| d13 | 977 | 232 + 52 = 284 | 284 | ✓ |
| d14 | 978–987 | −232 − 52 + 1,228 = +944; 52 + 944 = 996 | 944; 996; every term re-read from orig. l.3636/3641/3649/3652/3653/3655 | ✓ (see item 4 for the `_parts/` copy) |
| d15 | 988 | 81 − 24 = 57; 5 + 19 = 24 | 57; 24; both re-read at orig. l.3798–3803 and l.3628 | ✓ |
| d15a | 989–993 | 28 + 52 = $80,000 cash-paid vs 73 + 8 + 0 = $81,000 accrual; "$1,000 gap … not reconcilable" | 80,000; 81,000; gap = 1,000 ✓ (orig. l.3639 and Note 2 l.3798–3800 read) | ✓ and correctly *not* closed |
| d16 | 993–999 | 0 + 17 = 17; 996 + 17 + 14 = 1,027; +57 = 1,084 | 17 ✓ (orig. l.3429); 1,027 ✓ (l.3432); 1,084 | ✓ |
| d17 | 999 | 17 ÷ 511 = 3.33% | 3.32681 | ✓ |
| d18 | 1000 | 511,000 ÷ 11 = $46,454.5 → $46,455 | 46,454.545 | ✓ |
| d19 | 1002 | 511,000 ÷ 318,000,000 = 0.1607% | 0.16069 | ✓ |
| d20 | 1005 | 2,500,000 − 400,000 = 2,100,000; 1,000,000 ÷ 400,000 = 2.5× | 2,100,000; 2.5 | ✓, and the cross-year warning is attached |
| d21 | 1008 | 996 ÷ 284 = 3.51 years | 3.50704 | ✓ |
| d22 | 1008 | 1,007,000 ÷ 23 = $43,782.61 → $43,783 | 43,782.609 | ✓ |
| d23 | 1010 | 100,020.06 + 145,552.84 ≈ $245,573 | 245,572.90 → ≈245,573 ✓ (rendered with ≈) | ✓ — and it is the honest form of the number the last auditor fabricated |
| d24 | 1016–1022 | 1995-07-01 → 1995-12-31 = 184 days = 6.0 months = 26.3 weeks; mid-July ≈5.5 months ≈23.9 weeks | 184 days inclusive ✓; 184/7 = 26.2857 ✓; 5.5 × 4.345 = 23.8975 ✓ | ✓ |
| d25 | 1025–1029 | 4,235,244 − 582,528 − 847,716 − 42,000 = 2,763,000; ×⅓ = 921,000; 3,021,000 − 2,763,000 = 258,000 → $86,000; 245,573 + 5,408 + 921,000 = 1,171,981 → filed 1,172 | 2,763,000 ✓; 921,000 ✓; 258,000 ✓ and 258,000/3 = 86,000 ✓; 1,171,981 ✓; the filed `1,172` is real (orig. l.3546) | ✓ — and correctly **not adopted** |
| d26 | 1041–1045 | (52) + (303) + 107 = (248); 1,075 + 150 − 248 = 977 | 248 ✓ (orig. l.3540, l.3567, l.3555, l.3461, l.3571 all read); 977 ✓ (l.3463) | ✓ |
| d27 | 1046 | 42,000 × $0.1287 = $5,405.40 vs filed aggregate $5,408 | 5,405.40 ✓; $5,408 is filed at orig. l.4296 | ✓ and the direction of rounding is right |
| d28 | 1049–1050 | 10,200,000 + 4,235,244 + 120,000 = 14,555,244; 14,555,244 + 840,534 + 504,459 = 15,900,237 | 14,555,244 ✓ (and filed: orig. l.3455, l.3571); 15,900,237 ✓ (filed at l.3456) | ✓ both cross-foots |
| d29 | 1052 | 150,000 + 60,000 + 2,811,000 = 3,021,000; 1 + 2 + 20 = 23 | ✓ read at A5 l.4665–4668 | ✓ |
| d30 | 1055–1059 | 511,000 ÷ 23.8975 = 21,382.99 → $21,383; 511,000 ÷ 26.2857 = 19,440.22 → $19,440 | 21,382.98985; 19,440.2174 | ✓ both ends |

**Result: 32/32 d-entries recompute; zero stored figures are wrong.**

**The single mismatch, with its line:** `stage_1.md:925` prints
`100,020.06 + 145,552.84 + 49,995 = $295,567.89`, but those three printed addends sum to **$295,567.90**. The
total quoted is the sum of the *unrounded* products (295,567.8948). The same string is mirrored at
`quantitative.csv:34`. Both stored values (`$295,568`) are correct; the field is not re-runnable from its own
printed terms. One cent, two sites, cosmetic.

**Two judgement calls I made in the repair's favour rather than against it.** (i) d30's late end mixes a
5.5-month count with a 365/84 = 4.345 weeks-per-month convention, giving 23.90 weeks ≈ 167 days, whereas
15 July → 31 December is 170 days inclusive; the row is labelled "BAND, not a point", the launch day is
UNKNOWN per U.1, and the stored rendering is a band, so I record this as basis wobble inside a declared band,
not a defect. (ii) d25's parenthetical at `stage_1.md:1028–1029` concedes a $3 slip in the *audit sheet's*
tie and shows the correct sum; that is a retraction of someone else's number, correctly handled.

---

## Item 11 — §R ↔ §P cross-reference — **CONFIRMED**

§R occupies `stage_1.md:1130–1159`. I extracted every cross-reference token from the 22 table rows and tested
each against the defined target sets in the same file.

```
§R d-refs:  ['8a','15a','24','25','26','30']   missing: []
§R U-refs:  ['1','7','8','9','10','11','17','20','22','23','25','26','27','28','39','40','43']   missing: []
§R P-refs:  []                                  missing: []
defined d-ids in §P.2: 1..30 plus 8a, 15a      §U blocks: 43, contiguous U.1–U.43
```

Every §R reference resolves to a target that exists. The **prior defect is closed and I checked it directly
rather than trusting the note**: `stage_1.md:1156` (§R Weaknesses) promises the weekly-sales figure is
"DERIVED at §P.2 d30 and carried in `quantitative.csv` as its own row — stage1, date 1995-12-31, metric
'Average net sales per trading week, FY1995 (BAND, not a point)', value `19440-21383`, unit USD/week, class
DERIVED". Every element of that self-description matches the actual row at `quantitative.csv:112` — company
`Amazon.com`, stage `stage1`, date `1995-12-31`, metric string, value, unit, class `DERIVED` — so the promise
that was false when received is now true, and §P.2 records the history at `:1060–1062`. d30 exists at
`stage_1.md:1053`. The band §R cites matches d24's band at `:1016–1022`.

The two register-side citations in §R also resolve: `:1146` "the stated convention, §P.2 d24 — the same band
§N and `decisions.csv` carry" → §N does carry it at `stage_1.md:742` ("5.5–6.0 months of trading (§P.2 d24
band)") and `decisions.csv` at file line 12, where the band is written `5.5-6.0` with a hyphen rather than the
en-dash used in the prose — a style variance, not a broken reference. `:1152` routes Distribution to `→ U.43`,
which exists at `:2251`.

**Verdict: CONFIRMED.** No §R row points at anything that is not there. (The mirror-image problem — a register
row pointing at the *wrong* §R-adjacent conflict — is item 7's `timeline.csv:33`/`:55`, reported there and not
double-counted here.)

---

## Item 12 — AUDIT 5 re-run on the repaired text — **DEFECT**

**Which two attacks.** `03_quality_control/amazon_s1_audit4_audit5_final.md:407–418` is the adjudication table
with an explicit "Lands?" column. Of the ten attacks, exactly two are recorded **YES**: **A-B1** (`:409`) and
**A-B2** (`:410`). A-B8 is "**NO** on the end; yes on the label" and A-B3/A-B4 "Partly", so they are not the
two. (`adversarial_review.md:65` "## 2. Challenges that landed" is a different object — 13 narrative
downgrades, G-series, already applied at merge — and I read it at `:65–96` to be sure I was re-testing the
right thing.)

### A-B2 — directory/credibility efficacy had no canonical U block — **CLOSED**

Re-test: U.43 exists at `stage_1.md:2251–2293` and carries all six required elements of the
`00_METHOD_AND_STYLE.md:127–128` conflicting-evidence format (CLAIM A `:2256`, CLAIM B `:2260`, WHY THEY DIFFER,
EVIDENCE WEIGHT, BEST-SUPPORTED INTERPRETATION, RESIDUAL UNCERTAINTY, CONFIDENCE). The three stale pointers
named at `amazon_s1_audit4_audit5_final.md:430` (ll. 274, 469, 1075) now read → U.43 at `:288`, `:496`,
`:1152` (§O.7's fourth route at `:809`), and §D.1/§H/§R contain no live `→ U.41`. The register mirror exists:
`conflicts.csv` file line 44, `section` = "D.1; H; L; O.7; R". `validation.csv:9` (F-3's register twin) now
reads "the company **CLAIMED** editorial placement … that it earned it is not established".
I also verified U.43's two load-bearing empirical claims from disk, because a new block is exactly where an
unsupported number would hide:
* the "3,084 entries" census — `sources/ncsa-mosaic-whats-new_1995-08_kitchencloset.html` contains **exactly
  3,084** `<!-- key=` entry markers (Python count);
* "does not contain the company" — the file has 6 case-insensitive "amazon" hits; 5 are inside the project's
  own appended NEGATIVE FINDING banner (chars 1538–1962) and the 6th, at char 649,561, is the Nissan Pathfinder
  entry "the Amazon, and the Yukon" — the river. `_MANIFEST.md:98` is right;
* "no amazon.com root capture before 1998-12-12" — `sources/NULL_RESULT_wayback_1995_1996.md:17` records
  "Earliest capture of any kind: **1998-12-12 01:25:32** … status 302 … a redirect, not a page".

**Residual, named, not a reopening:** the re-point stopped at the prose volume. `timeline.csv` has **no** row
referencing U.43, and `timeline.csv:33` — whose `notes` restate U.43's CLAIM B verbatim ("no independent dated
listing for amazon.com survives … (NCSA Mosaic 'What's New', August 1995) contains the river, not the
company") — still carries `conflict_ref = U.16`. The attack's substance ("pointers route to an unrelated
conflict") survives in one register row.

### A-B1 — one filing family counted as independent corroboration — **STILL LANDS**

The decision recorded at `:409` was: "**strike the 'gain independence / genuinely corroborated' phrasing**,
re-key those records to `Corroboration: 1 (same-instrument duplicate)`". Re-test of each site:

| Site named by AUDIT 5 / RD-041 | Now | Status |
|---|---|---|
| §G.3 (pre-merge l. 417) | `stage_1.md:431` — "two states of one registration statement … one instrument restated, not corroboration (method §3 filing-lineage rule; A-B1)" | **CLOSED** |
| §J (pre-merge l. 532) | `stage_1.md:560` — "in **two** accessions of **one** registration statement (same lineage as S0801 — restatement, not corroboration; A-B1)" | **CLOSED** |
| §U.1 (pre-merge l. 1202) | `stage_1.md:1280` — "two accessions of **one** registration statement (S-1 original and S-1/A No. 5 — same lineage as S0801, so a restatement and **not** a second confirmation …)" | **CLOSED** |
| §T (pre-merge l. 1202 region) | `stage_1.md:1203` demoted; `:1204`, `:1205`, `:1206` **not** | **PARTLY CLOSED** |
| "`stage_1.md` header" (RD-041's own site list, `MASTER_RESEARCH_LOG.md:512`, marked capped) | a **new** ruling paragraph was added at `:35–47`, and the contradicting sentence it exists to cure was left standing 19 lines above at `:16–17`: "the original S-1's 1996-01-01 phrasing as **independent corroboration**" | **OPEN — the header now contradicts itself** |
| 22 claim records at `Corroboration: 2` | re-keyed | **CLOSED** |
| sites *not* in the named list | `stage_1.md:1139` §R, `quantitative.csv:74`, `stage_1.md:870`, `context_appendices.md:595`, `CORRECTIONS.md:242`, and claim records `:383`/`:397`/`:454` at counts 3–4 | **OPEN** |

So the answer to "still lands / closed / closed-but-overcorrected" for A-B1 is **still lands** — not because
the repair over-reached (it did not; no confidence moved, which I verified: `quantitative.csv:74` is still
`High`, and the 22 re-keyed records keep their ratings), but because the demotion is **incomplete and its
completeness was asserted on a marker census**
(`amazon_s1_causal_lineage_closure.md:35–40`, `:86`; `MASTER_RESEARCH_LOG.md:512` "the header ruling is
written"). The strongest single piece of evidence that this is a live contradiction rather than a wording
preference: `stage_1.md:40–41`, in the same header block, says the phrase "genuinely corroborated" is
withdrawn, and `stage_1.md:16` uses "**independent corroboration**" — the volume executing A-B1 against itself.

**Verdict: DEFECT.** A-B2 closed (one register-row residual); A-B1 still lands at six-plus sites including
the one the log marks capped.

---

## Item 13 — fix-introduced-defect sweep — **DEFECT**

Read-only git: `git log --oneline`, `git show --stat`, `git show <sha> -- <paths>`, `git grep`-equivalent
greps over the diffs. No ref was moved, no working tree touched.

The Stage-1 corpus was last written by two commits:
**`3ef318a`** (2026-09-24 17:46) — 4 changed files, +218/−2, touching `quantitative.csv` (2 records),
`stage_1.md` (+19 lines in two places) and creating the two closure sheets; and
**`f86306f`** (2026-09-24 17:19) — `stage_1.md` (+261 lines across 22 hunks), `conflicts.csv`, `data_gaps.csv`,
`quantitative.csv` (22 records), `stage_1_claim_records.md` (93 lines), `validation.csv`, `_MANIFEST.md`.

**The 10 most recently touched passages, and what I found in each:**

| # | Passage (current line) | Touched by | New numbers/dates/claims introduced | Provenance check |
|---|---|---|---|---|
| 1 | `stage_1.md:2218–2231` U.41 POINTER/BLOCK RECONCILIATION | 3ef318a | "six `U.41` strings", "live pointers … 1", `conflicts.csv` r42/r44, F17/J2 keys, S0608 key | **all verified** (item 7). Caveat: the census omits `timeline.csv`, so the claim is complete for the file it describes and not for the register set |
| 2 | `stage_1.md:2313–2319` spine note | 3ef318a | "43 rows, one per id, no gaps and no duplicates — verified by parse" | **verified by my own parse** (item 1/2). But the note fixes the tail and leaves `stage_1.md:1251` ("**42 canonical conflicts, U.1–U.42**") unannotated |
| 3 | `quantitative.csv:35` notes rewrite | 3ef318a | $105,408; 2,811,000; $937,000; $1,042,408; ≈$66,000; "0 occurrences"; $24 difference | **all verified** against the filings and by recomputation (items 6, 10). This is a good repair |
| 4 | `quantitative.csv:38` field relocation | 3ef318a | moves the INFERENCE band string to `notes`, `derived_arithmetic` emptied | **correct** per `00_METHOD_AND_STYLE.md:277`; my census: 0 non-DERIVED rows carry arithmetic, 82 empty cells all in that one column |
| 5 | `stage_1.md:35–47` new filing-lineage header ruling | f86306f | **"four sites that contradicted it are corrected below"** | **FALSE AS STATED.** `stage_1.md:16–17`, 19 lines above in the same header block, still reads "independent corroboration"; `:1139` §R likewise; §T `:1204`/`:1205`/`:1206` carry no demotion. A new assertion of completeness is itself the new defect |
| 6 | `stage_1.md:476–494` §H card-incidence regrade | f86306f | KNOWABLE narrowed to "two period documents *described*…"; rival remark dated 1996-09-18; withdrawal logged at `:493` | **verified**: `grep frightened` finds it only on the NOT-KNOWABLE/withdrawn side; the 1996-09-18 date matches `stage_1.md:1219` (CSM 1996-12-11 row cites the same "we haven't sold many books" line) |
| 7 | `stage_1.md:800–812` §O.7 rewrite | f86306f | "~400,000 sourceable titles against a superstore shelf of **~130,000**"; the (206) 622-2335 number | **verified**: `~130,000` is an S-1 estimate at orig. l.1793–1794 ("such superstores carry an average of approximately 130,000 titles", also l.1856); phone number filed at orig. l.2174–2180 per COR-13 |
| 8 | `stage_1.md:931–970` d8a rewrite | f86306f | $105,408; $937,000; $1,042,408; ≈$66,000; $1,271,980.89; the "$19"; the ⅓ | **all six recomputed, all six right** (item 10). This is the most number-dense new passage in the repair and it holds |
| 9 | `stage_1.md:1052–1063` d29/d30 | f86306f | `21,382.99`, `19,440.22`, "432 … [src:] traces resolving to 548" | 21,382.99 ✓ and 19,440.22 ✓ recomputed. **The self-description does not hold**: `stage_1_claim_records.md:574` still claims "**432** records" while `amazon_s1_numeric_closure_final.md:47` (R-9) puts the on-disk census at **431** `Claim:` lines; the closure recorded the discrepancy and did not settle it |
| 10 | `conflicts.csv:44` + `stage_1.md:2251–2293` new U.43 row/block | f86306f | 3,084; 1998-12-12; "no independent dated listing" | **verified from disk** (see A-B2 above). Clean |

**Newly introduced defects attributable to the repair rounds (as distinct from pre-existing ones):**

1. **`stage_1.md:36`** — "four sites that contradicted it are corrected below": false. This is a *new*
   assertion, created by the repair, that is not true.
2. **`03_quality_control/amazon_s1_numeric_closure_final.md:29`** — "Sweep for a surviving live instance of
   the false equation across all registers, parts and claim records: **0**", contradicted thirteen lines
   later in the same sheet at `:42` (R-4) and by `_parts/s1_p4.md:102–103`.
3. **`amazon_s1_numeric_closure_final.md:17`** — "**no live value cell carries either**", contradicted by
   `context_appendices.md:596` (Value column) and `:639`.
4. **`amazon_s1_causal_lineage_closure.md:37/86`** — a marker-count reported as a site audit ("all 31 named
   sites … demoted"), which is how `stage_1.md:17` and `:1139` escaped.
5. **`stage_1.md:2218–2231`** — a pointer census scoped to `stage_1.md`/`conflicts.csv`/claim records/
   `sources.csv` but not `timeline.csv`, which is where the mis-keyed rows are (item 7).
6. **`conflicts.csv:9`** and **`stage_1.md:1526`** both assert "the canonical spine is fixed at **U.1–U.42**"
   while U.43 exists — a *new* staleness created when U.43 was appended, annotated at the tail
   (`stage_1.md:2244–2245`, `:2313–2319`) but not in either of those two sentences.

**Repairs that introduced NO defect, recorded because the brief says a false positive is as costly as a miss:**
the whole $871,024/$871,000 retraction in the Stage-1 spine, the d7–d8a family, the d24 band, the d25
non-adoption, the 21,382.99 cent restoration, the $100,020.06 and $145,552.84 cent corrections, the $355,000 →
$248,000 deficit fix, the d15a $1,000 capex gap (correctly left open rather than plugged), the U.41
pointer/block reconciliation, and the 428-row parse. I recomputed or re-read every one against
`sources/` and none of them is a fabrication. There is no new "$245,572" in this round — `$245,572` appears in
the corpus only inside COR-14.2's rejection (`CORRECTIONS.md:261–266`),
`_parts/NUMBER_DEFECTS.md:52` and `stage_1.md:1512` ("**AUDIT 2's equation of it with the folk parental
figure is rejected, not adopted (COR-14.2)**"), and the live value everywhere is the correctly-rounded
`$245,573` (`quantitative.csv:32`, my product 245,572.8948).

**Verdict: DEFECT** — the repairs are numerically sound but the closure **assertions** written about them are
not, and one false assertion of completeness (`stage_1.md:36`) was introduced into the report itself.

---

## Sub-probes I did not run (would have required the web)

The brief allows me to declare these rather than fake them. None of the 13 items above depends on them; they
are listed so a later pass knows the boundary of this sheet.

| Probe | Why it needs the network | Query I would have run |
|---|---|---|
| U-a: whether the four non-SEC items still marked `restoration pending` in §T (`stage_1.md:1221–1231`) can be re-saved | existence of the live page today | WebFetch against each URL as cited in the §T row, recording HTTP status; `stone.txt`, `wiki.txt`, `p.html` per COR-08 |
| U-b: whether 1998-12-12 is still the earliest amazon.com root capture | live CDX | `https://web.archive.org/cdx/search/cdx?url=amazon.com/&matchType=exact&from=1994&to=1999&output=json` (note `stage_1.md:1215` records that prefix-match queries return HTTP 504 for this corpus — an unanswered, not a null) |
| U-c: completeness of the 3,084-entry Mosaic mirror, the one clause A-B3 (`amazon_s1_audit4_audit5_final.md:411`) asked to add to §T | requires the original August-1995 archive, not this third-party mirror | locate a second in-window copy of the NCSA "What's New" August 1995 listing and diff entry keys |

---

## Gate recommendation

**REOPEN.**

The closure agent's numbers hold. I could not break a single stored figure in `stage_1.md` §P/§P.2/§R or in
`quantitative.csv`: 29/29 DERIVED rows carry arithmetic and recompute, 32/32 §P.2 d-entries recompute, the cash
bridge reproduces the filed lines at orig. l.3636/3641/3649/3652/3653/3655 exactly, the register set parses to
43 U rows and 428 records with uniform arity, U.41 resolves to one live pointer and one block with no
duplicate live claim, §R's every cross-reference resolves, `21,382.98` is retraction-only, and `2,613,000` is
genuinely absent from all nine local documents. What I could break is the closure's account of its own work,
in four places, and one retracted figure is genuinely still live.

**Blocking defects:**

- **B-1 (item 6) — a retracted figure is live in a Value column.** `context_appendices.md:596` and `:639`
  still carry `$871,000`, `2,613,000` and the withdrawn `$976,408` composition as live capital arithmetic, while
  `amazon_s1_numeric_closure_final.md:17` certifies "no live value cell carries either". Already written up as
  S2E-28 (`research/ST2_E_adversarial.md:895–922`, confidence "Certain") and not acted on. This is the same
  failure class as the retracted `$245,572`, in the file a Stage-2 miner reads.
- **B-2 (items 9 and 12) — A-B1 still lands, and the header contradicts itself.** `stage_1.md:16–17` and
  `:1139` still count the original S-1 as "independent corroboration" of its own amendments;
  `quantitative.csv:74`, `stage_1.md:870` and `context_appendices.md:595` do the same in weaker words;
  `CORRECTIONS.md:241–242` still instructs it; §T rows `:1204`/`:1205`/`:1206` carry no demotion; claim records
  `:383` (3), `:397` (4, counting 424B1), `:454` (3) escaped a re-key that only looked for `Corroboration: 2`.
  `MASTER_RESEARCH_LOG.md:512` marks the header site capped and `stage_1.md:36` asserts "four sites …
  corrected" — both false as stated.
- **B-3 (item 4) — a false equation is still live in a volume of the report.** `_parts/s1_p4.md:102–103`
  prints `52 − 232 − 52 + 1,228 = +944`, unannotated, alongside the pre-repair d4/d5/d7 values;
  `amazon_s1_numeric_closure_final.md:29` says the surviving count across "all registers, **parts** and claim
  records" is **0**, contradicted by its own R-4 at `:42`.
- **B-4 — closure assertions must be re-derived, not re-argued.** B-1, B-2 and B-3 all share one shape: the
  underlying repair was largely done, and the *sweep statement about it* was produced by counting markers or
  scoping to the file the agent happened to have open. Both closure sheets
  (`amazon_s1_numeric_closure_final.md`, `amazon_s1_causal_lineage_closure.md`) should be corrected by
  addition, not rewriting, and re-run with a site list rather than a marker count.

**Non-blocking residuals to carry into the sign-off note:** the stale "42 canonical conflicts, U.1–U.42" at
`stage_1.md:1251` (and the two "spine is fixed at U.1–U.42" sentences at `conflicts.csv:9` and
`stage_1.md:1526`); COR-03's own section carrying no supersession banner (`CORRECTIONS.md:57–69`) and COR-11.2
still routing to it at `:194`; `timeline.csv:33`/`:55` keyed `U.16` where U.43/U.41 are the canonical homes and
no `timeline.csv` row referencing U.41 or U.43 existing; the 1-cent printed-addend mismatch at
`stage_1.md:925` / `quantitative.csv:34`; the unsettled 432-vs-431 record census
(`stage_1_claim_records.md:574` vs `amazon_s1_numeric_closure_final.md:47`); §T `:1206`'s stale
`restoration pending` on the 424B1 (already R-8); and RD-042's unresolved RD-id collision, which is
traceability, not accuracy.

**Fair statement of what the closure got right**, since an audit that only reports damage is not an audit:
the numeric layer is clean on my re-computation, the retraction discipline was honoured at every one of the
~40 sites I spot-checked in the spine, no new figure in the repair rounds lacks provenance, and the hardest
judgement call in the round — holding d25 at UNKNOWN rather than adopting ≈$921,000, and refusing to substitute
a third number for the $871k leg — was made in the right direction twice. The gate is reopening on sweep
integrity and on one live figure, not on invented arithmetic.
