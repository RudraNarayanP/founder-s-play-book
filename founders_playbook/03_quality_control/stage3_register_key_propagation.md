# Stage-3 register key propagation — log and dispositions

Owner: the register-key propagation pass (Stage 3, `company_001_amazon`). Date: 2026-09-25.
Exclusive write access to the nine `*.csv` registers (confirmed by brief); no other agent edits them.
Web requests made by this pass: **zero**.

## What this pass fixes

The Stage-3 register merge applied four dossiers' source blocks under ids that collided (`S3001` naming
three documents). They were re-keyed to canonical **S30001–S30083** in `sources.csv` (83 canonical rows), and
the *narrative* was propagated (329 re-pointed, 28 held by `03_quality_control/stage3_citation_propagation.md`).
The **reference columns inside the registers still carry the retired keys**: 157 rows resolve to nothing, plus
14 `sources.csv` rows whose `independence_note`/`notes` cross-references name a retired id.

## Authorities used (row by row, never a file-wide alias)

1. `03_quality_control/stage3_sourceid_rekey_map.md` — `(dossier, old id) -> canonical id -> title`.
2. `03_quality_control/stage3_register_binding.md` — the binding pass's per-row decisions (§4 decision tables).
3. `03_quality_control/stage3_citation_propagation.md` — 329 resolved narrative sites **and its held list, which
   this pass mirrors exactly** (where it held, this pass holds).
4. `sources.csv` itself — the arbiter: every bound canonical id is machine-checked against its `source_id` column.

**Why no file-wide alias:** the same retired token resolves to a *different* canonical per dossier block —
in `timeline.csv` `S3001` -> `S30001` (ST3_A rows 126-168), -> `S30031` (ST3_B 169-191), -> `S30053` (ST3_C
192-214). The binding/propagation passes recorded `S3010` -> `S30020` and `S3010` -> `S30010` in one file. A
blanket substitution would falsify the record; every row is bound from its own dossier block + text + date.

## Measurement command (run before and after)

```
cd "E:\founder's playbook/founders_playbook/01_companies/company_001_amazon"
python - <<'PY'
import csv,re,glob
CANON=re.compile(r'^S3\d{4}$')          # canonical S300nn
OLD  =re.compile(r'^S3\d{3}$')          # retired bare  S30nn
D    =re.compile(r'^S3D-\d{3}$')        # retired family S3D-nnn
P    =re.compile(r'^S3P-\d{3}$')        # retired family S3P-nnn
keys={r[0] for r in csv.reader(open('sources.csv',newline='',encoding='utf-8')) if r and OLD.match(r[0]) is None}
tok=re.compile(r'\b(S3[A-Za-z0-9-]*\d)\b')
for f in sorted(glob.glob('*.csv')):
    for i,row in enumerate(csv.reader(open(f,newline='',encoding='utf-8')),1):
        if i==1: continue
        bad=[t for cell in row for t in tok.findall(cell) if (OLD.match(t) or D.match(t) or P.match(t))]
        if bad: print(f,'row',i,bad)
PY
```

Rows already wrapped in `UNRESOLVED(...)` markers are *dispositioned*, not dangling: they are tasks. The
before/after check separates "a retired token that resolves to nothing" (a defect) from "a retired token inside
an `UNRESOLVED(cand=...)` marker or inside a documented `[RETIRED-KEY REFERENCE]` sentence" (a recorded hold).

## Pre-edit snapshot (from disk, this pass)

Line counts (physical lines): timeline 267, quantitative 382, sources 204, validation 60, failures 62,
conflicts 171, data_gaps 103, decisions 30, channels 26. Header widths: timeline 11, quantitative 12,
validation 11, failures 11, sources 18, conflicts 15, data_gaps 8, decisions 15, channels 11.

## Planned disposition

### `timeline.csv` — 88 rows in the legacy dossier blocks (rows 126-214)

- **Rows 126-158 (ST3_A block, `source_id` col 7):** each retired `S300n` -> `S3000n` by the rekey map's
  ST3_A pairing (un-collided within the block). 33 rows.
- **Row 159 (ST3_A, `S3031`):** RESOLVED -> **`S30045`**. Outside ST3_A's own 1-30 source block (allocation
  error, not drift); resolved by content — File No. 333-78797 is unique to `S30045` in `sources.csv`, and the
  binding pass wrote the same 1999-05-19 $2bn shelf event to `S30045`.
- **Rows 160-167 (ST3_A, `S3032`-`S3037`): HELD — 8 rows.** Mirrors the propagation pass's 8 held ST3_A tokens.
  These ids are outside ST3_A's mapped block and each still fits two or more candidate documents:
  - 160 `S3032` — `UNRESOLVED(cand=S30024|S30079; missing=cited-for-completion-dates-vs-S-8-plan-registration)`
  - 161-165 `S3033`-`S3035` — Q2-1999 10-Q registered twice: `UNRESOLVED(cand=S30010|S30064; missing=which-duplicate-is-canonical)`
  - 166-167 `S3036`-`S3037` — Q3-1999 10-Q registered four times: `UNRESOLVED(cand=S30011|S30043|S30065|S30076; missing=which-duplicate-is-canonical)`
- **Row 168:** `source_id` = UNKNOWN, no retired token. Untouched.
- **Rows 169-191 (ST3_B block):** retired `S300n` -> `S300(30+n)` by the map's ST3_B pairing (S3001->S30031 ...
  S3019->S30049). 23 rows. (Proof the token is not file-wide: `S3010` here -> `S30040`, but `S3010` in the
  ST3_A pending row 257 -> `S30010`.)
- **Rows 192-214 (ST3_C block):** retired `S300n` -> the map's ST3_C pairing (S3001->S30053 ... S3016->S30067),
  with one documented content resolution: **`S3007` -> `S30051`** (the map skips ST3_C S3007; its accession
  0000891020-98-001498 / event 1998-10-28 occurs under exactly one canonical row, `S30051`, and the binding
  pass resolved the same 1998-10-28 event to `S30051`). 23 rows.

Totals: **80 resolved, 8 held.**

### `quantitative.csv` — 59 rows, `source` col 7, all in the ST3_B block (rows 226-288)

Retired `S300n` -> `S300(30+n)` by the map's ST3_B pairing; pair cells (`S3002;S3001`) bind both tokens. Rows
284-287 carry `UNKNOWN` (no token) and rows before 226 carry free-text citations already bound — untouched.
**59 resolved, 0 held.**

### `validation.csv` — 6 rows, `source_id` col 7, ST3_C block (rows 42-47)

S3007->S30051, S3017->S30068, S3004->S30056, S3009->S30060, S3014->S30065. **6 resolved, 0 held.**

### `failures.csv` — 4 rows, `source_id` col 8, ST3_C block (rows 48-51)

S3009->S30060, S3014->S30065, S3017->S30068, S3011->S30062. **4 resolved, 0 held.** (The corpus-wide-null row
the binding pass held — 3 candidates, asserts a null no single filing carries — was never written here; it
remains a task in the pending block, nothing to mirror.)

### `sources.csv` — 14 note-field cross-references (key column itself is already clean)

- **11 retired bare-id notes** (rows 118, 123, 125, 126, 128, 130, 136, 144, 147, 148, 153): re-point the bare
  token to its canonical **for that row's own dossier** (the row's canonical id tells the block: S30001-S30030 =
  ST3_A, S30031-S30052 = ST3_B). e.g. `S30003` note "Same accession as S3004" -> `S30004`; `S30032` note
  "same registrant as S3001" -> `S30031`. Additive: only the id token changes, the explanatory sentence is kept.
- **3 `S3D-nnn` notes** (rows 196, 197, 198): `see S3D-004` -> `S30075`; "SAME INSTRUMENT AS S3D-004" -> `S30075`;
  "registered as S3D-006" -> `S30077`.
- `sources.csv` row 197's "S3001-S3022" history and the `S3P-001`/`S3P-002` in the binding annotations are
  **class-2 retired-scheme references — left verbatim**, exactly as the propagation pass left them.

### `stage_3_pending_registers.md` — dated correction only

Lines ~107 and ~196 claim `quantitative.csv`/`validation.csv` were applied "every `source` reference bound to
canonical ids," which the two files contradict (59 and 6 retired references). Append a dated correction to each;
**do not erase the original claim, do not touch any other line.**

### Adjacent retired families (`S3D-nnn`, `S3P-nnn`) — budget permitting

The 3 register-internal `S3D` note refs are folded into the `sources.csv` cleanup above. Any remaining
`S3D-`/`S3P-` in a register reference column will be measured and, if present, propagated by the same map
(`S3D-004`->`S30075`, `S3D-006`->`S30077`, `S3P-001`->`S30082`, `S3P-002`->`S30083`); otherwise logged as the
next pass with exact counts. Narrative occurrences are out of scope (this pass may not edit narrative files).

## RESULT — rows resolved per register (row by row; canonical verified present in `sources.csv`)

**`timeline.csv` — 88 rows touched: 80 resolved, 8 held.**
- ST3_A block 126-158 (`S300n`->`S3000n`): 33 rows, e.g. L126 S3001->S30001 … L158 S3030->S30030.
- L159 S3031 -> **S30045** (content: File No. 333-78797 unique; matches the shelf event).
- **HELD L160-167 (S3032-S3037)** — see marker table below (mirror the propagation pass's 8 ST3_A holds).
- ST3_B block 169-191 (`S300n`->`S300(30+n)`): 23 rows, e.g. L169 S3001->S30031, **L170 S3010->S30040** (contrast
  the pending ST3_A row 257 `S3010`->`S30010`: same token, different dossier, different canonical — proof of no
  file-wide alias). L187 S3015->S30045.
- ST3_C block 192-214 (map pairing): 23 rows; **L200/L201 S3007 -> S30051** (map skips ST3_C S3007; accession
  0000891020-98-001498 / event 1998-10-28 has one canonical row, `S30051`, as the binding pass resolved it).

**`quantitative.csv` — 59 rows (62 token sites incl. pair cells), 0 held.** All ST3_B `source` col -> `S300(30+n)`.
Pairs: L238 `S3002;S3001`->`S30032;S30031`; L258 `S3009;S3001`->`S30039;S30031`; L273 `S3007;S3005`->`S30037;S30035`.
Rows 284-287 (`UNKNOWN`) untouched.

**`validation.csv` — 6 rows (col 8), 0 held.** L42/L43 S3007->S30051; L44 S3017->S30068; L45 S3004->S30056;
L46 S3009->S30060; L47 S3014->S30065. (The binding pass's own re-emitted rows 54-60 were already canonical.)

**`failures.csv` — 4 rows (col 8), 0 held.** L48 S3009->S30060; L49 S3014->S30065; L50 S3017->S30068;
L51 S3011->S30062. The corpus-wide-null row the binding pass held was never written into this register.

**`sources.csv` — 14 note-field cross-references, key column already clean.** 11 bare-id notes (dossier = the
row's own canonical block): L118 `S3004`->`S30004`; L123 `S3007`->`S30007`; L125 `S3011`->`S30011`;
L126 `S3010`->`S30010`; L128 `S3012`->`S30012`; L130 `S3014`->`S30014`; L136 `S3022`->`S30022`;
L144 `S3009`+`S3010`->`S30009`/`S30010`; L147 `S3001`->`S30031`; L148 `S3001`->`S30031`; L153 `S3007`->`S30037`.
3 `S3D-nnn` notes: L196 `see S3D-004`->`see S30075`; L197 `S3D-004`->`S30075`; L198 `S3D-006`->`S30077`.
**Preserved verbatim (class-2 history):** L197 `S3001-S3022` collision narrative and `S3P-001` re-key note;
L198 `S3P-002` re-key note. Only the token changed; every sentence that explains the history is intact.

## Held rows (8) — the task each one opens

| Row | token | UNRESOLVED marker (candidates all exist in `sources.csv`) | the missing fact |
|---|---|---|---|
| timeline 160 | S3032 | `UNRESOLVED(cand=S30024|S30079;missing=cited-for-completion-dates-vs-S-8-plan-registration)` | is the row cited for the merger completion dates or for the equity-plan registrations? |
| timeline 161-162 | S3033 | `UNRESOLVED(cand=S30010|S30064;missing=which-duplicate-is-canonical)` | which Q2-1999 10-Q duplicate (A `S30010` / C `S30064`) is canonical for acc. 0000891020-99-001426? |
| timeline 163-164 | S3034 | `UNRESOLVED(cand=S30010|S30064;missing=which-duplicate-is-canonical)` | same duplicate question |
| timeline 165 | S3035 | `UNRESOLVED(cand=S30010|S30064;missing=which-duplicate-is-canonical)` | same duplicate question |
| timeline 166 | S3036 | `UNRESOLVED(cand=S30011|S30043|S30065|S30076;missing=which-Q3-1999-10-Q-duplicate-is-canonical)` | which Q3-1999 10-Q duplicate is canonical (acc. 0000891020-99-001938)? |
| timeline 167 | S3037 | `UNRESOLVED(cand=S30011|S30043|S30065|S30076|S30075;missing=which-duplicate-vs-FY1999-10-K-S30075-carrier)` | which duplicate, and is the FY1999 10-K `S30075` the carrier rather than the 10-Q? |

## Verification block (pasted, after)

Definitive reference-column re-check (retired = `S3\d{3}`/`S3D-`/`S3P-`; canonical `S3\d{4}` unaffected), UNRESOLVED cells excluded:
```
sources.csv      col0: retired-token reference cells = 0
timeline.csv     col6: retired-token reference cells = 0
quantitative.csv col6: retired-token reference cells = 0
validation.csv   col7: retired-token reference cells = 0
failures.csv     col7: retired-token reference cells = 0
TOTAL retired reference values outside UNRESOLVED markers across registers: 0
```

Invariants re-measured from disk (uniform width via csv field-count == header):
```
sources.csv        lines= 204 width=18 ragged=0  source_id 203/203 distinct (dup=0)
timeline.csv       lines= 267 width=11 ragged=0
quantitative.csv   lines= 382 width=12 ragged=0  DERIVED rows=91  missing derived_arithmetic=0
validation.csv     lines=  60 width=11 ragged=0
failures.csv       lines=  62 width=11 ragged=0
conflicts.csv      lines= 171 width=15 ragged=0  conflict_id 170/170 distinct (dup=0)  [stage3 = 55]
decisions.csv      lines=  30 width=15 ragged=0
channels.csv       lines=  26 width=11 ragged=0
data_gaps.csv      lines= 103 width= 8 ragged=0
stage values inside the four literals only (stage1|stage2|stage2-consequence|stage3) — 0 out-of-set.
§U parity: Stage-1 U.1-U.43    <-> conflicts stage1 = 43  ✓ 43<->43
          Stage-2 U.44-U.113b  <-> conflicts stage2 = 72  ✓ 72<->72
          Stage-3 U.114-U.168  <-> conflicts stage3 = 55  ✓ 55<->55
```

Row-count deltas (git HEAD vs disk), all zero:
```
sources.csv 204->204  timeline.csv 267->267  quantitative.csv 382->382
validation.csv 60->60 failures.csv 62->62  conflicts.csv 171->171
decisions/channels/data_gaps unchanged.
```

Append-only / no-loss vs git HEAD (read-only; `git diff --numstat`):
```
4   4   failures.csv         (added==deleted -> no line gained or lost)
59  59  quantitative.csv
14  14  sources.csv
2   0   stage_3_pending_registers.md   (the two dated corrections, appended; no line removed)
88  88  timeline.csv
6   6   validation.csv
```
Per changed row, csv-parsed column count is preserved and the edit is confined to the reference cells
(`tok`-classified diff); every new id tested against `sources.csv`. `conflicts.csv`, `decisions.csv`,
`channels.csv`, `data_gaps.csv` show empty `git diff` -> untouched. **Line terminators from disk: `conflicts.csv`
171 CRLF / 0 bare-LF; all other eight 0 CR / all bare-LF — each file uniform, no mixing introduced.**

## Next pass — adjacent retired families

- `S3D-nnn`: all 3 register-internal cross-references (`sources.csv` 196/197/198) folded into this pass. The
  remaining `S3D-` tokens live in the **narrative** (`research/ST3_D_tech_ops.md` 11, `stage_3_pending_registers.md`
  9, `_parts/s3_p4.md` 9 = **29** by the propagation pass's measure) and **class-2** note history in `sources.csv`
  rows 197/198 which is preserved. Propagate the 29 by `S3D-001->S30072 … S3D-004->S30075, S3D-006->S30077 …`
  (map rows 82-91) in a narrative pass — out of scope here (this pass may not edit narrative files).
- `S3P-nnn`: the register reference columns carry **zero** `S3P-` values (the binding pass already bound every
  `S3P-*` row to `S30082`/`S30083`); the only `S3P-` left are the class-2 re-key annotations in `sources.csv`
  197/198, intentionally preserved. The 27 narrative `S3P-nnn` (`stage_3_pending_registers.md` 17, `_parts/s3_p4.md`
  10) belong to the same next narrative pass (`S3P-001->S30082`, `S3P-002->S30083`).

