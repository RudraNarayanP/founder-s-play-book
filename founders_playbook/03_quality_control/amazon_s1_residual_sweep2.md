# Amazon Stage 1 — LEVEL-3 REGISTER SWEEP, ROUND 2 (final register pass)
Level-3 Register Sweeper · run **2026-09-24**. Owns **exactly seven files**: `stage_1.md`,
`stage_1_claim_records.md`, `quantitative.csv`, `conflicts.csv`, `_parts/NUMBER_DEFECTS.md`,
`founders_playbook/RESUME_HANDOFF.md`, and this log — plus the appended-marker exception granted for four
**historical working volumes** (`_parts/s1_p1.md`, `_parts/s1_p3.md`, `_parts/s1_p4.md`,
`research/E_supply_ops_finance.md`), which were **marked at their ends, never rewritten**. **No file was deleted,
moved, renamed or tidied; no directory pruned.** This pass adds **no fact, no figure and no citation** that
`amazon_s1_number_repairs2.md` did not establish: it propagates them to the copies that pass could not open, and
proves the register is now internally consistent on those four numbers.

## 1. Canonical values swept to (original S-1, acc. 0000891618-97-001309, filed 1997-03-24)

| Register | Canonical | Filed lines | Must not survive |
|---|---|---|---|
| Feb→Dec 1995 step-up | **+94.1%** (94.118 displayed / 94.137 exact ⅓ — 0.02 points apart) | l.2864, l.4301–4302 | `+95.2%` as a live value (needs an unfiled $0.1708) |
| One-third leg | **$871,000** (`2,613,000 × ($1,007,000 ÷ 3,021,000) = 2,613,000 ÷ 3` exactly) | l.4301–4302 | `$871,024` anywhere outside a retraction sentence |
| Purchaser composition | **$976,408**, band-level (±$1,000); $24 gap accounted for (≈$19 filed-thousands + $5 Alberg), **not plugged** | l.3535, l.3546, l.3645, l.4296 | `= $976,432` as a composition tie (the arithmetic itself, `1,272,000 − 295,568`, stands) |
| Bezos post-IPO stake | **43% = original** (l.985–988, l.2919); **41% = S-1/A No. 5** (acc. 0000891020-97-000839, l.1055–1062, l.3149) | as listed | An unattributed 41–43% range; 41% under an unversioned "Form S-1"; any average |

## 2. Named survivors closed, and what the wider sweep added

**The named list under-counted for the fourth pass running.** Of the five numbered survivors, one site
(`_parts/s1_p1.md` l.52, an unattributed "~41–43%") had not been named by anyone, and one (`quantitative.csv` r98's
`1,006,999`) turned out to be a retraction already inside its correction sentence.

| # | Site | Before | After |
|---|---|---|---|
| 1 | `stage_1.md` **l.556 §K** "Reconciliation of the two totals" | "+ $871,000 − $50,000 **= $976,432**" — right leg, retired tie | "= **$976,408** — a band-level composition inside the ±$1,000, **not** an exact tie to the $976,432 residual arithmetic of §P.2 d8; the $24 difference is accounted for at §P.2 d8a, not plugged, and the $871,024 leg this row formerly printed is **retracted** as a back-solved plug". 5 pipes / 4 cells, geometry unchanged |
| 2 | `stage_1.md` **l.184 §B.1** "Personal capital and ownership" | "post-IPO **~41–43%**" under a Source cell naming only the original | both figures attributed to their accession in the row (**43%** orig. l.985–988 / **41%** No. 5 l.1055–1062), flagged as a version discrepancy never averaged; the Source cell now names the No. 5 leg and notes that dossier tag **E-59 cites the No. 5 accession, not the original's** |
| 3 | `stage_1_claim_records.md` **K14** (l.376) | 41% quoted under a "Form S-1" Source label | `Passage:` **verbatim, untouched**; correction marker appended after the field, naming the No. 5 accession + lines, the original's 43%/48.3%/43.1%, and the rule (never averaged/merged) |
| 4 | `stage_1_claim_records.md` **P09** (l.445) | Value cell "≈976,432 unnamed" at six significant figures | Value cell → "**≈$976,000 (±$1,000)** unnamed"; marker appended carrying the $976,432 arithmetic as still-correct, the $976,408 composition, and the $871,024 retraction. `Passage:` verbatim |
| 5 | `stage_1_claim_records.md` **coverage note** (l.572) | "Records carrying a visible correction: 75" | "75 as merged, **77 after 2026-09-24**" with the delta named and the per-family sub-counts explicitly **left un-re-derived** rather than silently recomputed |
| 6 | `_parts/s1_p1.md`, `s1_p3.md`, `s1_p4.md`, `research/E_supply_ops_finance.md` | live stale copies in frozen working volumes | each got an appended **`SUPERSEDED 2026-09-24`** footer naming its own sites (s1_p1 l.52 + l.70; s1_p3 l.24; s1_p4 l.46/98/176/203; E l.25/75/261/324), what changed, and where the corrected value now lives. **No existing line was rewritten** |
| 7 | `_parts/NUMBER_DEFECTS.md` | round-1 footer only | round-2 footer appended: propagation status of rows 27–28/43, the §B.1 attribution, the four marked volumes, and the still-open out-of-scope list |
| 8 | `RESUME_HANDOFF.md` | "repair in flight"; stale instruction list | Audit-3 rows state **all repairs landed**; the canonical four values printed; actions 1–2 marked DONE with the corrected figures; the §2 table row updated |

## 3. `quantitative.csv` / `conflicts.csv` — confirmed, not assumed

Parsed with Python `csv`, every cell scanned for the seven strings, and each hit located to its **column**:

* `quantitative.csv` — r30 `notes` (the sentence that deletes `+95.2%`), r35 `derived_arithmetic`
  (`1,272,000 − 295,568 = $976,432`, rendered ≈$976,000 (±$1,000)) and `notes` (both retraction sentences), r98
  `notes` (`1,006,999` inside "CORRECTED per AUDIT 3 … the register printed"). **No `value` or
  `derived_arithmetic` cell holds a superseded figure**: r30 value `94.1`, r35 value `976000`, r98 value
  `1006899.30`. The L30/L35 markers are the only `95.2` / `871,024` occurrences in the file and both sit inside
  retraction sentences.
* `conflicts.csv` — 12 occurrences, **all in r30**, all correctly attributed per accession (claim_a = original 43% /
  48.3% / 43.1%; No. 5's 41% confined to `why_they_differ` and `best_supported_interpretation` with its accession and
  date; claim_b = retrospective tellings). No averaging anywhere in the row.
* Neither file was written by this pass — nothing in them needed closing.

## 4. Final sweep (company directory + `founders_playbook/`, all `*.md`/`*.csv`, plus the Amazon `sources/*.txt` primaries)

Grep patterns: `976,432`, `871,024`, `95.2`, `41%`, `43%`, `~41`, `1,006,999` (+ the no-separator variants
`976432`, `871024`, `1006999`). Classified **per occurrence** by rule, then reviewed line by line: a `Passage:` span
→ quoted; an explicit retraction/correction verb, or a line in a file now carrying an appended footer → marker; a
figure printed with its accession → correct. **335 occurrences on 184 lines.**

| Class | Occ / lines | Representative sites |
|---|---|---|
| **correct value / attributed** | 35 / 23 | `stage_1.md` l.184 (43% orig / 41% No. 5, both named), l.892 (d8 arithmetic rendered ≈$976,000 ±$1,000), l.1876–1897 (§U.29 per accession), `research/H_legal_organization.md` l.141/318/319/320, `_EVIDENCE_CACHE.md` l.350, `s1_claims_AJ.md` l.325, `RESUME_HANDOFF.md` l.29/71, `MASTER_RESEARCH_LOG.md` l.537 |
| **quoted source text** — register `Passage:` quotes | 3 / 3 | `stage_1_claim_records.md` l.376 (K14), `E_supply_ops_finance.md` l.25, `H_legal_organization.md` l.141 — verbatim, untouched |
| **quoted source text** — the filings themselves | 6 / 6 | orig. `.txt` l.986 = **43%**; No. 5 `.txt` l.1055/1062 = **41%** (+ the two duplicate archival copies). This is the evidence the canonical split rests on |
| **retraction / supersession marker** | 95 / 37 | `stage_1.md` l.556/883/886/901/902/905/1100/1409, `quantitative.csv` r30/r35/r98, `data_gaps.csv` r11, `context_appendices.md` l.596, `CORRECTIONS.md` l.176, `stage_1_claim_records.md` l.376/445/573, `_parts/NUMBER_DEFECTS.md` (the defect register itself), `RESUME_HANDOFF.md` l.14/24/27/32, `MASTER_LOG` l.536, **`conflicts.csv` r30 ×12** (per-accession correction record) |
| **stale copy now under an appended SUPERSEDED footer** (marked, not rewritten) | 13 / 11 | `_parts/s1_p1.md` l.52/70, `s1_p3.md` l.24, `s1_p4.md` l.46/98/176/203, `research/E_supply_ops_finance.md` l.25/75/261/324 + the four footers themselves |
| **not this figure** (grep artifact) | 6 / 6 | `_MANIFEST.md` l.6/84 (43% **of the word ceiling**), `stage_1.md` l.312 + `_parts/s1_p2.md` l.19 ("~41 **months** post-launch"), orig. `.txt` `$5,995.20` ×2 |
| **frozen audit record** (`03_quality_control/`, unedited by design) | 172 / 97 | audit3_numbers 8 · audit3_recheck 15 · number_repairs 7 · number_repairs2 16 · residual_sweep 27 · this log |
| **OPEN — outside this pass's write scope** | 5 / 4 | see §5 |

**No occurrence of `+95.2%`, `$871,024` or a `= $976,432` composition tie survives as a live value anywhere in the
corpus**, and no `1,006,999` survives outside its own correction sentence. ~4 lines (e.g. `stage_1.md` l.905,
`quantitative.csv` r35 `derived_arithmetic`) sit on the boundary between "correct value" and "marker": they print
$976,432 *as* the retired residual arithmetic while labelling it as such. They are reported here rather than smoothed.

## 5. What this pass could not close (reported, not repaired)

| Site | Defect | Owner |
|---|---|---|
| `_parts/s1_claims_KU.md` **l.37** | K14's pre-merge twin: 41% under a "Form S-1" label. The merged `stage_1_claim_records.md` record is now marked; this working volume is not in this pass's scope and is not the clean copy | `_parts/` / claim-appendix owner (a footer marker of the §2.6 kind is the route) |
| `_parts/s1_claims_KU.md` **l.153** | P09's pre-merge twin: Value cell "≈976,432 unnamed" | same |
| `_parts/U_CONCORDANCE.md` **l.60** | "The ~41%/~10% post-IPO figures" with no accession named | concordance owner |
| `MASTER_RESEARCH_LOG.md` **l.247** | "the identity of the residual ~$976,432" without the ±$1,000 band | orchestrator's log (l.536–537 already carries the canonical values, so the log contradicts itself) |
| `_MANIFEST.md` | counts stale — its own regeneration is already queued as handoff action 5 | orchestrator |

## 6. Validation actually run

* **Geometry:** `stage_1.md` l.184 and l.556 re-checked at **5 pipes / 4 cells**, identical to their neighbours; the
  file is still uniformly **CRLF (2,139 lines, 0 lone CR, 0 mixed)** — no ending was converted by the edits. All
  six other written files verified **LF-only, no BOM, trailing newline present**.
* **CSV parse** (this pass wrote none, parsed all): `quantitative` 111 data rows × 12 cols, `conflicts` 42 × 15,
  `validation` 29 × 11, `data_gaps` 23 × 8, `sources` 102 × 18, `timeline` 57 × 11, `failures` 33 × 11,
  `decisions` 15 × 15, `channels` 15 × 11 — **uniform widths, 0 field-count mismatches, 0 empties anywhere except
  the 74 legitimately empty `derived_arithmetic` cells in `quantitative.csv`**, and `QUOTE_MINIMAL` round-trip
  byte-identical **True** for `quantitative.csv` and `conflicts.csv`.
* **Column-aware check:** every stale string in every CSV was located by header name, so no superseded value hides in
  a `value`/`derived_arithmetic` cell — the only cells carrying them are prose notes and retraction sentences.

## 7. What this pass is not

**Verification must not diff against `HEAD` for two of the eight files.** A sibling agent's commit `98aa933` ("Apple
rated exemplar-capable…") landed **mid-sweep** and swept up this pass's `stage_1.md` (l.184, l.556) and
`RESUME_HANDOFF.md` edits, so both read clean in `git status` while carrying this sweep's text — confirmed by
`git show HEAD:…` containing "retracted** as a back-solved balancing plug" in `stage_1.md` and "ALL NOW CLOSED
(2026-09-24)" in `RESUME_HANDOFF.md`. The other six files still show as modified. This is the third pass in a row to
disclose the same hazard (`number_repairs2` caveat (a), `residual_sweep` §6).

A sweep is a propagation, not a verification: every figure here is `number_repairs2`'s, carried to files its author
could not open. The three arithmetic claims (§K's $976,408 tie, the $871,000 third, the ±$1,000 band) still need an
independent read of orig. l.4301–4302, l.3535, l.3546, l.3645, l.4296. **No `UNKNOWN` was upgraded**: the identities
behind ≈$871,000, the date split of the $1,007,000 program and any 1995 ownership percentage stay UNKNOWN. If the
next auditor wants the last four lines in §5, they belong to owners this pass may not write — a fifth register pass
with a `_parts/` marker mandate would close them.
