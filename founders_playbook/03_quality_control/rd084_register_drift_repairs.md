# rd084_register_drift_repairs.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T19:05:40Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## Method

STATUS: WRITTEN 2026-09-26

Scope: the eight register CSVs named in the RD-084 brief (nine under `company_001_amazon/`, plus the
four registers under each of `company_002_walmart/research/`, `company_003_unitedhealth/research/`,
`company_004_apple/research/`). Zero web access; every judgment below is made from the file's own
bytes and the schema in spec §13.

Repair procedure, applied to every finding rather than trusting the gate's own parser:

1. Re-read each flagged file with a strict RFC-4180 reader (`csv.reader`, `doublequote=True`), which
   is what spec §13 prescribes: "any field containing a comma, quote, or newline is double-quoted
   with `"` escaped as `""`". Field counts per record were compared with the header.
2. Run an independent drift detector that does not depend on quoting at all, because a
   comma-inside-a-field defect can preserve the field count: per-column value-domain histograms
   (`stage` against the §13 controlled vocabulary; `confidence`, `evidence_class`, `importance`
   distinct-value census; `quantitative.value` numeric-ness; `sources.url` / `source_id` shape), plus
   an empty-cell census (spec: an empty cell is a defect).
3. Repair only what step 1-2 confirms is genuinely wrong, editing the raw line in place with a
   prefix/whole-cell guard assertion so that no other byte of the file changes. No file was
   re-serialized wholesale; untouched rows are byte-identical to before.
4. Never write a value that changes a row's meaning to satisfy a check, and never invent a figure.

**Headline result: the Amazon "width drift" is not a CSV defect.** Under strict RFC-4180 parsing
every record in `sources.csv`, `quantitative.csv`, `conflicts.csv`, `timeline.csv` and
`data_gaps.csv` has exactly the header width (drift = 0 rows in all five), and the value-domain
census shows no count-preserving shift either: `stage` is in-vocabulary in all 1,296 Amazon register
rows, `company`, `confidence`, `evidence_class` and `importance` all land in their own columns, and
the 102 non-numeric `quantitative.value` cells are legitimate multi-value or qualified metrics
(`5.5-6.0`, `$3.00 per order + $0.95 per book`, `151 / 158 / 256`), not displaced text.

The findings are produced by `tools/gates.py:read_rows`, which sniffs the dialect from only the
**first 4,000 bytes** of a file (`sample = f.read(4000)`). In that window `csv.Sniffer` returns
`doublequote=False`, so a correctly escaped `""` inside a quoted field is read as a field
terminator, the rest of the record re-opens, and every subsequent in-field comma is counted as a
separator. Feeding the same bytes as one full sample returns `doublequote=True` and the drift
disappears. Measured on the flagged files (`Sniffer().sniff(text, delimiters=",;")`):

| file | sniffed on first 4000 bytes | sniffed on whole file |
|---|---|---|
| amazon/timeline.csv | dq=False | dq=True |
| amazon/quantitative.csv | dq=False | dq=True |
| amazon/conflicts.csv | dq=False | dq=True |
| amazon/sources.csv | dq=False | dq=True |
| amazon/data_gaps.csv | dq=False | dq=True |
| amazon/failures.csv | dq=False | dq=False (file contains no `""`; no drift reported either way) |

Consequence for the record, stated plainly: `--self-test` passes on this corpus only because its
fixture is small and contains no `""`, so the clean-fixture control never exercises the truncated
sniff window. **The gate's width-drift finding on a large quoted register is currently
unreliable, and its `--csv` result on Amazon must not be read as evidence that these five files are
malformed.** The one-line fix belongs in the tool, not in the data: pass
`dialect=csv.excel` (or call `sniff` on the whole file and honour `doublequote`) in
`tools/gates.py:read_rows`. I did **not** edit `tools/gates.py` — it is not in the file set this
brief assigns me, and repairing a checker to silence a finding it raised on correct data is the
move this project's rules forbid. It is logged in Residue for the tooling owner.

## Amazon repairs

STATUS: WRITTEN 2026-09-25

`founders_playbook/01_companies/company_001_amazon/` — nine registers, 1,296 rows. Two rows repaired;
43 flagged width-drift rows deliberately left unchanged; one briefed defect not reproduced.

| file | rows repaired | finding disposition |
|---|---|---|
| `sources.csv` | 1 | 26 width-drift rows: **not a defect** (see below). 1 real: `access_date` prose on S2012 |
| `quantitative.csv` | 0 | 13 width rows: not a defect |
| `conflicts.csv` | 0 | 3 width rows: not a defect |
| `timeline.csv` | 0 | 1 width row (rec 118): not a defect |
| `data_gaps.csv` | 0 | 1 width row (rec 37): not a defect |
| `failures.csv` | 1 | `date` = `Stage 2` on rec 47 → repaired |
| `validation.csv`, `decisions.csv`, `channels.csv` | 0 | no findings |

### Repaired

**`failures.csv` rec 47** — `date` held the literal string `Stage 2`. Read against its own columns,
nothing had shifted: `company`=Amazon.com, `stage`=stage2, `signal_or_failure`="Failed experiments
actually dated inside the window", `magnitude`=EMPTY, `evidence_class`=UNKNOWN,
`what_it_demonstrated`="Nothing: no dated failed test … appears in any accession", `confidence`=
"High (that none is retrievable)". All eleven fields are at header width, so this is a stage label
that wandered into the date column, not a comma defect. The row's own assertion is that **no date
exists to record**, so the cell was set to the spec-§13 literal `UNKNOWN`. No date was invented and
no other value was touched; the row still says the same thing it said before.

**`sources.csv` rec 115 (S2012)** — `access_date` held `NOT ACCESSED IN THIS PASS (zero-web budget)`,
prose with no year and outside the gate's sentinel list. Set to
`UNKNOWN - not accessed in this pass (zero-web budget)`: the sentinel plus the original reason kept
verbatim in the same cell, matching the vocabulary the register already uses for this state (S2007
carries `UNTRIED (Stage-1 retrieval returned 404; no local copy; not re-requested under the
zero-web budget)`; 19 further rows carry plain `UNKNOWN`). Post-repair, `sources.csv` has **zero**
`access_date` cells lacking a year or a sanctioned sentinel.

### Not repaired, and why

The 43 width-drift rows are correctly quoted RFC-4180 data. Representative receipts, from the raw
bytes rather than from a parser's opinion:

- `timeline.csv` rec 118 — one 11-field record; the `event` field is quoted and contains
  `…trademark rights in ""Earth's biggest bookstore"" and demanding…`. Under `doublequote=True` this
  is one field holding a quoted phrase; under the sniffed `doublequote=False` it terminates the
  field and the phrase's two in-field commas become separators (hence "13 fields").
- `quantitative.csv` rec 7 — 12 fields as parsed strictly. Its `notes` field opens
  `Adopted ""by the Board of Directors and the sole stockholder on September 15, 1994"" …` and runs
  to ~1,200 characters containing ~20 commas; the gate counted 32.
- `conflicts.csv` recs 170/171 — both carry a legitimately quoted `company` field
  (`"Amazon.com, Inc."`) plus several `""`-escaped phrases each; strict parse = 15 fields = header.
- `data_gaps.csv` rec 37 — `follow_up_task` is quoted because it contains
  `…history for ""Cadabra, Inc."" (RETRY: …)`; the comma inside the organisation name is inside a
  doubled-quote escape, which is exactly what §13 prescribes. Strict parse = 8 fields = header.

Rewriting any of these to satisfy the gate would mean either deleting quotation marks from verbatim
quoted evidence — which the verbatim-quote gate and the citations themselves depend on — or
un-quoting fields that contain commas, which would create real drift where none exists. Both were
refused on the "never change a value's meaning to make a check pass" rule.

**`channels.csv` `date_tested`: the briefed defect is NOT REPRODUCED.** All 25 rows were read. Every
non-empty `date_tested` cell carries a four-digit year, e.g. `1995 (start date UNKNOWN; claimed in
the 1995-10-04 release)`, `~1995-05 (six-week closed beta, per retrospective accounts); claimed
first outside order 1995-04-03`, `1995-10-22 (Tallahassee Democrat search test); 1995-11 (Knight
Ridder feature)`. The column is verbose — it carries qualification prose that would sit better in
`notes` — but it is year-bearing and the gate reports no finding on it. Nothing changed; a
year-stripping "repair" would have deleted the dates' own confidence qualifiers.

Also observed, not repaired (outside the brief, and each would need a judgment or a document, not a
mechanical fix): 337 empty cells in the nine Amazon registers. The large majorities are
schema-mandated blanks — `quantitative.derived_arithmetic` is empty in 246 rows precisely because
spec §13 requires it empty unless `evidence_class` is ESTIMATE/DERIVED — and `timeline.conflict_ref`
(41), `decisions.claim_ref` (10) and `notes` columns are optional back-references. Read against the
strict §13 sentence "an empty cell is a defect" they are all defects; read against the same schema's
own mandatory/empty-otherwise rule they are correct. That contradiction is left for the adjudication
pass rather than "fixed" by writing filler into 337 cells.

## Walmart+other stage sweep

STATUS: WRITTEN 2026-09-25

The numeric-`stage` defect was swept across **all four company dirs and all nine register names in
each**, not only the row that was named in the brief. Detection used the strict reader with the
column position resolved from the header, so a shifted row could not masquerade as a stage value.

| file | numeric rows found | mapping applied |
|---|---|---|
| `company_002_walmart/research/sources.csv` | 27 rows `1` | → `stage1` |
| `company_004_apple/research/timeline.csv` | 21 rows `1`, 2 rows `2` | → `stage1` / `stage2` |
| `company_004_apple/research/quantitative.csv` | 30 rows `1` | → `stage1` |
| `company_004_apple/research/conflicts.csv` | 13 rows `1` | → `stage1` |
| `company_004_apple/research/sources.csv` | 13 rows `1` | → `stage1` |
| `company_003_unitedhealth/research/*` | **no register CSVs exist** | nothing to sweep |
| `company_001_amazon/*.csv` (all nine) | 0 — already in vocabulary | 0 |
| `company_002_walmart/research/{timeline,quantitative,conflicts}.csv` | 0 | 0 |

**106 rows normalized in total** (27 Walmart + 79 Apple). Each edit changed only the `stage` cell of
the raw line: the script asserted that every field preceding `stage` in that row is comma-free and
quote-free, then replaced the exact prefix `field0,field1,…,` + old cell with the same prefix + new
cell, so no other byte of any line moved. The three remaining Apple `stage` values that were not
numeric were already in vocabulary and were not touched. Post-sweep, the whole-corpus stage census is
`{stage1, stage2, stage2-consequence, stage3}` with no illegal literal in any of the 17 registers
that exist (Amazon 9, Walmart 4, Apple 4, UnitedHealth 0).

Spot-check of the two Apple `2 → stage2` rows, since a numeric cannot express `stage2-consequence`:
rec 23 is `1980-12 · Apple shares go on sale; 4.6M shares at $22 printed …` and rec 24 is
`1981-02 · BYTE prints the FY1978-FY1980 revenue series …`. Both are post-IPO and read as Stage-2
events in their own right rather than consequences of a Stage-2 fact, so `stage2` is the defensible
normalization. Residual risk, for the re-certification pass rather than me: the 104 `1`-valued rows
were recorded as bare `1` before the vocabulary was fixed on 2026-09-25, so nothing in the file can
now tell us whether any of them was *intended* as `stage2-consequence` and got flattened to `2`/`1`
at write time. The literal `stage2-consequence` appears only in the Amazon registers (17
`quantitative` + 8 `timeline` + 3 `channels` rows) and nowhere in Apple, Walmart or UnitedHealth.

**company_003_unitedhealth: reported honestly as un-sweepable.** `research/` contains two dossiers
(`A_chronology_feasibility.md`, `B_chronology_finance_from_print.md`) and no `timeline.csv` /
`quantitative.csv` / `conflicts.csv` /
`sources.csv`. The gate's two findings there are `coverage` findings
("no register CSVs at root or research/ -- csv/anchors gates DID NOT RUN", "no stage_*.md volumes
found"), which are intake gaps, not CSV defects, and are not mine to create — inventing four empty
registers would turn a loud coverage failure into a silent pass. Left exactly as found.

## Proof

STATUS: WRITTEN 2026-09-25

Command run per company, identical before and after:
`python tools/gates.py --company-dir "founders_playbook/01_companies/<dir>" --checks csv`

Findings, before → after: **Amazon 7 → 5 · Walmart 1 → 0 · UnitedHealth 2 → 2 · Apple 4 → 0.
Corpus 14 → 7.** Every one of the 7 remaining findings is either a width-drift false positive whose
data was verified correct under RFC-4180 (5, Amazon) or a UnitedHealth coverage finding that
predates this brief and cannot be closed by editing CSVs (2).

After — `company_001_amazon`:

```
Findings: **5** | Passes: 9
| csv | timeline.csv     | width drift: 1 rows off ([(118, 13)]...) |
| csv | quantitative.csv | width drift: 13 rows off ([(7, 32), (8, 15), (25, 19)]...) |
| csv | conflicts.csv    | width drift: 3 rows off ([(135, 16), (170, 18), (171, 17)]...) |
| csv | sources.csv      | width drift: 26 rows off ([(54, 24), (115, 19), (117, 21)]...) |
| csv | data_gaps.csv    | width drift: 1 rows off ([(37, 10)]...) |
- coverage 9 registers, 15 stage volumes, 101 source documents
csv      timeline.csv.source_id    all S#### tokens resolve
csv      validation.csv            59 rows x 11 cols
csv      validation.csv.source_id  all S#### tokens resolve
csv      failures.csv              61 rows x 11 cols
csv      failures.csv.source_id    all S#### tokens resolve
csv      decisions.csv             29 rows x 15 cols
csv      decisions.csv.source_id   all S#### tokens resolve
csv      channels.csv              25 rows x 11 cols
csv      channels.csv.source_id    all S#### tokens resolve
```

The two date-column findings that were real — `sources.csv | access_date carries no four-digit year:
['NOT ACCESSED IN THIS PASS (zero-web budget)']` and `failures.csv | date carries no four-digit year:
['Stage 2']` — are gone from the table above.

After — `company_002_walmart` and `company_004_apple`, both clean:

```
# company_002_walmart    Findings: 0 | Passes: 5
csv      timeline.csv      37 rows x 11 cols      csv      timeline.csv.source_id  all S#### tokens resolve
csv      quantitative.csv  71 rows x 12 cols      csv      conflicts.csv           18 rows x 15 cols
csv      sources.csv       38 rows x 18 cols      (stage vocabulary: no finding)

# company_004_apple      Findings: 0 | Passes: 5
csv      timeline.csv      23 rows x 11 cols      csv      timeline.csv.source_id  all S#### tokens resolve
csv      quantitative.csv  30 rows x 12 cols      csv      conflicts.csv           13 rows x 15 cols
csv      sources.csv       13 rows x 18 cols      (was: 4 stage-vocabulary findings, values 1 and 2)
```

Before, for the record: Walmart `stage vocabulary illegal: 1`; Apple `stage vocabulary illegal: 1, 2`
on `timeline.csv` plus `1` on each of `quantitative.csv`, `conflicts.csv`, `sources.csv`;
UnitedHealth `coverage | registers | no register CSVs at root or research/ -- csv/anchors gates DID
NOT RUN` and `coverage | narrative | no stage_*.md volumes found` — unchanged after, 2 findings, 0
passes, 0 registers / 0 stage volumes / 37 source documents.

`python tools/gates.py --self-test`:

```
anchor with no register row              [anchors] CAUGHT
dangling source_id                       [csv]    CAUGHT
duplicate record id                      [csv]    CAUGHT
numeric stage vocabulary                 [csv]    CAUGHT
paraphrase presented as quote            [quotes] CAUGHT
row with wrong column count              [csv]    CAUGHT
unquoted comma shifts fields             [csv]    CAUGHT
unresolvable source token in narrative   [keys]   CAUGHT
clean fixture                            CLEAN

self-test: PASS
```

8/8 defects caught, clean fixture clean — so the detector fires on the defects it was written for.
But read together with the table in Method, `--self-test` **does not** establish that the width-drift
gate is sound: its fixture is 4 lines and contains no `""` escape, so it never presents the gate with
a large quoted register, which is the only condition under which the truncated 4,000-byte sniff
window misfires. Green self-test plus 43 unverifiable-looking rows on Amazon is exactly the pattern
§15.5 warns about, inverted: the gate catches its historical defect while generating a new class of
false positive on real data.

Independent verification of the 7 repairs, since the gate cannot be the arbiter here: strict
`csv.reader` re-parse of all 17 registers that exist confirms record counts unchanged
(Amazon 266/381/170/203/102/59/61/29/25, Walmart 37/71/18/38, Apple 23/30/13/13), field widths equal
to header in every record of every file, stage vocabulary legal in every file, and zero `access_date`
or `date` cells without a year or a sanctioned sentinel.

## Residue

STATUS: WRITTEN 2026-09-25

### NEEDS-ADJUDICATION

1. **5 Amazon width-drift findings (43 rows) — data verified correct, gate left red.** Nothing here
   was repaired, so nothing here was changed under me. A judgment pass must decide between: (a)
   `tools/gates.py:read_rows` passing `csv.excel` (or sniffing the full file and honouring
   `doublequote`) — after which these 5 findings should disappear with no data edit; or (b) a ruling
   that the §13 `""`-escaping convention is not what these registers should use, which would be a
   data-format decision affecting 1,296 Amazon rows and would have to be made by whoever owns the
   method, not by a repair agent. I am reporting (a) as the evidence-backed reading: strict RFC-4180
   parsing yields header width on every row, and the affected rows' content is internally consistent.
   No row's meaning was altered to move a check from red to green.
2. **Amazon `stage2-consequence` cannot be re-derived for the 104 normalized numeric rows** (Apple +
   Walmart). See the risk note in the sweep section: `1`/`2` could not express "usable only as a
   consequence", so the flattening is irreversible from the file alone and needs a reader of the
   Apple/Walmart dossiers, not a script.
3. **`tools/gates.py` was not edited** — outside the file set this brief assigns. The bug is recorded
   with its reproduction (Method table) and its one-line fix, above.

### Repaired (7 rows, 7 files) — restated for the ledger

`company_001_amazon/failures.csv` 1 row · `company_001_amazon/sources.csv` 1 row ·
`company_002_walmart/research/sources.csv` 27 rows · `company_004_apple/research/timeline.csv` 23 rows ·
`company_004_apple/research/quantitative.csv` 30 rows · `company_004_apple/research/conflicts.csv`
13 rows · `company_004_apple/research/sources.csv` 13 rows. **106 rows in 7 files**; every other
register byte-identical to how it was received.

### UNTRIED

- **Spec §13 "record the count in the company manifest" for the normalized numeric stages.** The
  `_MANIFEST.md` files are not in this brief's owned set, so the 27 Walmart / 79 Apple counts live
  only in this sheet. Someone with manifest ownership must copy them across.
- **UnitedHealth registers and stage volumes do not exist.** Its 2 coverage findings are an intake
  gap; the fix is dispatching register construction, and the brief's assumption that four registers
  sat in `company_003_unitedhealth/research/` is simply wrong. Not attempted.
- **The 337 Amazon / 65 Walmart / 25 Apple empty cells**, including Walmart `sources.csv` recs 3 and
  10 with an empty `relevant_passage` (S0102 FY1973 annual report, S0109 FY1980 annual report).
  Filling those needs the cited annual-report text; under zero web and no local copy of those two
  documents, writing anything would be inventing a passage. Left empty, as found. The
  mandatory-vs-optional reading of "an empty cell is a defect" is flagged above for adjudication.
- **The non-csv gates were not run** (`--checks csv` only, per the brief): `keys`, `anchors`,
  `quotes`, `budget` are untested by me on all four companies, so this sheet's "clean" claims are
  scoped strictly to the csv gate.
- **Apple/Walmart `sources.csv` id-block collision** was not examined. The `source_id` resolution
  gate passes on both (`all S#### tokens resolve` on their `timeline.csv`), but those registers use
  dossier-local `A2S-nn`-style keys per §13's central-mapping rule, and I did not verify whether that
  mapping has happened.
- **No other company dirs exist** in `01_companies/`, so "all four" is the whole sweep scope; the
  remaining 46 of the Fortune-50 top 50 have no registers here to sweep.

### Files touched

Seven CSVs, listed above. Not touched: any file under `sources/`,
`01_companies/company_001_amazon/research/_EVIDENCE_CACHE.md`, `00_universe/harvest/`, any narrative
`.md`, any `_MANIFEST.md`, `tools/`, and the five Amazon registers whose flagged rows proved correct.

