# Tesla Stage 1 — residuals closed (`tesla-residuals`, 2026-10-06)

Executes the six executable items B1\*–B6\* left by certifier `tesla-cert-1` in
`03_quality_control/tesla_s1_certification.md`. **Web calls: 0 made, 0 permitted.** **No adjudication was
re-opened**: no value, date, class, confidence or verdict changed; every edit is a count, a label, a
supersession marker or a route name. Nothing the certifier decided was re-decided — each item was first
re-measured from the bytes and then closed.

Gate after the last write: `03_quality_control/tesla_s1_gates_residuals.md` → **Findings 2 | Passes 18**,
tier **T3** (auto), **0 substantive**; `anchors | parity | 23 ↔ 23`; `corrections | 7 retraction ids; register
layer reaches 7, volumes 7`. The 2 findings are the same two advisories the certifier recorded (the T3 word
advisory, now 55,347 w against the 8,000 target, and `quotes | ADVISORY | 16 of 58 (28%)`).

## Item-by-item, before/after measured from disk

**B1\* — CLOSED.** `03_quality_control/tesla_s1_merge_notes.md` §7. Before (lines 161–162, no marker):
"**$2009-12-31 is UNKNOWN**, and the 'liability held flat across the deposit-policy inversion' reading is not
carried as a finding". After: **§7 untouched, one dated `> SUPERSEDED 2026-10-06` block appended after its last
line**, pointing at COR-01, `U.23`, the `quantitative.csv` $26.0m carrier row and the S4370 carrier sentence,
and stating that the route was a local read so the 0-call web budget never bore on it. Append-only — the note's
history is intact (sweep below: §7's old wording 1×, supersession marker 2× in that file). `_OWNER_LEDGER.json`
had **no entry** at this path, so nobody was displaced; claimed and released. The task's suggested date
("SUPERSEDED 2026-09-30") is the merge date; the certifier's own requested block text is dated 2026-10-06, so
this pass used **2026-10-06**, the date of the supersession.

**B2\* — CLOSED (7 cells, 5 files).** Before: "11 held bodies across 8 accessions" printed bare in
`conflicts.csv` `U.23` `claim_b_source` and `evidence_weight`, `quantitative.csv` 2009-12-31 note,
`CORRECTIONS.md` COR-01 (l.56) and the auditor-correction note (l.246), `stage_1.md` merge-header repair
paragraph (l.97), `stage_1_index.md` `U.23` row. **Independently re-measured by this pass**, tag-stripped
sentence-by-sentence across `sources/sec/`: a strict "December 31, 2009" + "$26.0 million" sentence test returns
**14 bodies / 10 accessions**; adding the FY2010 10-K `S4375` (`0001193125-11-054847_d10k.htm`, which prints the
*other* form — "As of December 31, 2010 and 2009, reservation payments in the amount of $30.8 million and $26.0
million, respectively, were recorded as current liabilities") gives **15 bodies / 11 accessions**, exactly the
certifier's figure. And 14 − the three 2011 printings (`-11-149963` txt+htm, `-11-157135`) = **11 bodies / 8
accessions**, confirming the old figure is the 2010 registration lineage rather than a mistake. After: every
cell restated to **15 / 11**, scoped as "the 11/8 pair is the 2010 lineage", with **S4375 added to the carrier
list** in `claim_b_source`, `quantitative.csv`, `stage_1.md`, the index and COR-01's recount bullet. Neither the
auditor's "eight held documents" nor the 11/8 pair is published bare anywhere now.

**B3\* — CLOSED.** `sources.csv` `S4390` `source_title`. Before: "Measured 2026-09-30: **8 files** in
sources/wayback/, 3 negative HTML bodies …, 1 zero-byte JSON, 1 transcript, **3 sidecars**". Measured this pass
(`ls --full-time`): **7 entries** — `cdx_tesla_com_2003_2005.json` 160 B, `cdx_tesla_com_root_exacts.json` 160 B,
`cdx_www_tesla_com_root_exacts.json` 11,832 B, `cdx_tesla_com_2008_2011_founderish.json` 0 B, **2** ×473 B
`.meta.json` sidecars, `README_retained_capture_evidence.md` 1,009 B. After: the false enumeration stays quoted
and a `[RESIDUALS 2026-10-06 … / B3*]` marker inside the same cell prints the measured 7 / 2 / 160 / 160 /
11,832 / 0, plus the point that **only 2 of the 4 CDX bodies carry a sidecar** — which is A8's `http_status` gap
itself. The 3 negative HTML bodies and the zero-byte-JSON-with-sidecar were re-checked and are correct as
printed.

**B4\* — CLOSED as a named requirement; the route was NOT run (correctly).** `tools/cdx_intake.py` exists
(63,450 B, `run|enumerate|audit|selftest`). `tools/web_domains.json` holds **5 slugs — centene, cencora,
elevance, marathon, microsoft — and no `tesla` entry**, so there is **no cited `source_line` to run against**.
Per the brief and per the ledger's own `_provenance_note` ("a domain invented by the tool is a lead with no
provenance"), **no domain was invented and `--force` was not used**; the command was therefore not executed and
no `sources/web_archive/` directory was created (still absent, re-measured). The citable provenance that a
future ledger pass can quote already exists on disk: both protected `sources/wayback/*.meta.json` sidecars print
`url_param: "tesla.com matchType=domain"` — those bytes are **superseded from the register, not edited**. The
requirement is now named in **all four instruction-layer locations plus the volume's own family line**:
`stage_1.md` §U `U-1 / FETCH REQUEST` and §U family (b); `data_gaps.csv` row 16 ("via the CDX route at FRA-1");
`_MANIFEST.md` "Open research debt … Web archives"; `tesla_s1_merge_notes.md` FR-3. Each names
`python tools/cdx_intake.py run --slug tesla --max-requests 20` **and** its blocker (a `tesla` entry in
`tools/web_domains.json` carrying a cited `source_line`), and each records that **(b) stays TRIED–UNANSWERED
and T3 stays T3 until that command has run and been graded** — no tier claim from an unexecuted route either
side.

**B5\* — CLOSED.** `decisions.csv` row 1 (`2010-06-08 | Correct the FY2009 stock-compensation error
prospectively …`) `actual_result`. Before: "…the uncorrected $(55740)k comparative later printed in the 10-K",
with `RETROSPECTIVE` occurring **0×** in that register (re-confirmed). After: the clause carries
`[RETROSPECTIVE - post-stage outcome per s13 register vocabulary …]`; the fact itself is untouched. Sweep: the
same clause also stands in `stage_1.md`'s re-emission of the row and in `_parts/s1_p2.md` — **the `_parts/` copy
was left alone**: that path is claimed `done=false` by `tesla-s1-p1`/`tesla-s1-p2` in `_OWNER_LEDGER.json`, so
per the brief it is skipped and reported, not forced. The volume's own copy was not edited either (B5's locator
is the register; the register is canonical and `_MANIFEST.md` says so).

**B6\* — CLOSED.** `stage_1.md` §U "Corpus-family status as this merge leaves it", family (a). Before:
"**76 held documents / 59,479,299 B / 3,059,480 words**" — the denominator COR-06 withdrew. Measured by this
pass over `sources/sec/`: **83 documents** (61 `.htm` + 19 `.txt` + 3 `.pdf`), **32 accessions**,
**59,881,144 B**. After: the line prints **83 documents across 32 accessions / 59,881,144 B**, with the withdrawn
76 / 59,479,299 / 3,059,480 kept visible inside a dated `*[…B6*]*` bracket as superseded, not deleted. The words
figure is re-measured and labelled as this pass's own method (tag-stripped whitespace tokens: **2,914,081**),
because COR-06's method does not reproduce the 3,059,480 it replaced; the mismatch is stated rather than hidden.
The T3 justification is explicitly unchanged — family (a) is the one family with in-window Tier-1 text under
either denominator, so this is a self-contradiction inside the tier line, not a re-tier. Two other "76" printings
in the volume (`stage_1.md` P1-22 claim record, P1S11 register emission) are **pre-repair emissions and were
left standing** — the certifier's own R-b class.

## Sweeps run, with hit counts (all measured after the last write)

| sweep | pattern | hits |
|---|---|---|
| B2 old 11/8 figure | `11 held bodies across 8 accessions` + variants | **8** (conflicts.csv 2, CORRECTIONS.md 2, quantitative.csv 1, stage_1.md 1, stage_1_index.md 1, certification sheet 1) — every corpus hit now sits beside a restatement |
| B2 new 15/11 figure | `15 held bodies (across) 11 accessions` | **7** (same five corpus files + certification sheet) |
| B1/B4 supersession markers | `SUPERSEDED 2026-10-06` | **3** (merge notes 2, certification sheet 1) |
| B4 scripted route named | `cdx_intake.py` | **13** (stage_1.md 4, data_gaps.csv 2, merge notes 2, _MANIFEST.md 1, certification sheet 4) |
| B4 blocker named | `web_domains.json` | **8** corpus+cert |
| B3 old / new enumeration | `8 files in sources/wayback` / `7 entries in sources/wayback` | **1 / 1**, both in `S4390` (old kept as the quoted false claim) |
| B5 label | `[RETROSPECTIVE` | **2** (decisions.csv 1, certification sheet 1); was 0 in `decisions.csv` |
| B6 old / new denominator | `76 held documents / 59,479,299` / `83 documents across 32 accessions / 59,881,144` | **1 / 1** in `stage_1.md` |
| wayback directory | `ls --full-time sources/wayback/` | **7 entries / 2 sidecars**; `sources/web_archive` **absent** |
| register row counts | per-file `csv.reader` | **210 data rows**, split 24/62/46/23/16/9/9/11/10 — **unchanged** |

**One defect this pass made and fixed, reported because a repair pass is itself a defect source (§14).** The
B5 edit added commas to `decisions.csv` `actual_result`, a field the register had left **unquoted**, and the
gate fired `csv | decisions.csv | width drift: 1 rows off (2, 17)` — findings went 2 → **3**. Rewritten
comma-free (no quoting change needed), the row is back to 15 columns and the gate is back to **2 / 18**
(`03_quality_control/tesla_s1_gates_residuals.md`, same command as the brief).

**Counts regenerated (§9.6), because the annotations move words.** `_MANIFEST.md` now carries a dated
re-measure block (its 2026-09-30 table cells left standing as published history): `stage_1.md` **55,347 w /
385,304 B** (was 54,903 / 382,275; still **under** the 60,000 hard cap → no §9.3 split), `CORRECTIONS.md`
**3,027 / 21,319**, `stage_1_index.md` **2,038 / 13,605**, and **registers 210 rows / 17,191 w / 131,294 B**
(was 16,837 / 128,812 — cell text grew, **no row added or removed**). `sources/sec` 83 / 32 / 59,881,144 and
`sources/wayback` 7 / 2 unchanged.

**Paths claimed and released** (`--agent tesla-residuals`, no `--force` used anywhere): `stage_1.md`,
`stage_1_index.md`, `CORRECTIONS.md`, `_MANIFEST.md`, `sources.csv`, `conflicts.csv`, `quantitative.csv`,
`decisions.csv`, `data_gaps.csv`, `03_quality_control/tesla_s1_merge_notes.md`, this log — all eleven released
`done=true`. **Touched nothing**: `_parts/s1_p1.md`, `_parts/s1_p2.md` (ledger `done=false`, `tesla-s1-p1` /
`tesla-s1-p2`) and `03_quality_control/tesla_s1_audit1.md` (`done=false`, `tesla-s1-audit1`, heartbeat
2026-10-06T11:48Z) — all three held by other agents and all three named by the certifier as protected or
not-yet-released, so their stale wording is **skipped and reported**, not overwritten. The named residuals R-a
(unregistered printings needing centrally minted rows), R-b, R-c, R-d, R-e (tool defects incl.
`scaffold.py ledger` PermissionError and `gates.py coverage`'s 81-vs-83) and R-f (FRA-2/3, FR-4/5/6) are
untouched by design and stay open.

## Was anything actually re-adjudicated? No — and the residual-ness is genuine

Every one of the six was a bookkeeping fix on a measurement the certifier had already taken, and each of this
pass's re-measures landed on the certifier's number: **15 / 11** (reconciled from 14 / 10 + S4375), **7 entries /
2 sidecars** at 160/160/11,832/0 B, **83 / 32 / 59,881,144 B**, `RETROSPECTIVE` 0× in `decisions.csv`, no ledger
entry at the merge-notes path, no `tesla` slug in `web_domains.json`. **The certification does not need to be
re-run: the residuals were genuinely residual, not the certifier being wrong.** Nothing flipped — tier stays T3,
anchors stay 23↔23, corrections stay 7/7 reaching both layers, register rows stay 210, and no value, date or
adjudication moved. One item is genuinely still open rather than closed: **B4\* is intake debt, not a defect** —
it cannot be executed by a repair pass at 0 web calls and no cited domain, and it is now named in five places so
the next pass is briefed to the script instead of to a hand curl. I am not the certifier and do not re-certify:
this sheet records the closures; the verdict remains `tesla-cert-1`'s
(**CERTIFIED-WITH-NAMED-RESIDUALS**), and whether B1\*–B6\* may be re-labelled closed is a call for that role.
