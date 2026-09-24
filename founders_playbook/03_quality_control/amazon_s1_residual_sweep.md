# Amazon Stage 1 — LEVEL-3 REGISTER SWEEP (residual stale copies)
Level-3 Register Sweeper · run **2026-09-24**. Owns **exactly five files**: `stage_1.md` **§S and §U.8 regions only**,
`data_gaps.csv`, `context_appendices.md`, `_parts/NUMBER_DEFECTS.md`, and this log. **No file was deleted, moved,
renamed or tidied; no directory was pruned** (method §14.4). Authority: `03_quality_control/amazon_s1_number_repairs2.md`
(which established the values and named four survivors it could not write), `company_001_amazon/CORRECTIONS.md`
(COR-01, COR-02, COR-10, COR-14.2), `00_METHOD_AND_STYLE.md` §8 (metric basis; no value without source and confidence
cells; `UNKNOWN` is a complete value) and §13 (schemas; every field containing a comma, quote or newline is
double-quoted; an empty cell is a defect). **This pass adds no fact, no figure and no citation that number_repairs2
did not already establish; it only propagates them and proves nothing stale remains in its own scope.**

## 1. The canonical values being swept to (from the original S-1, acc. 0000891618-97-001309, filed 1997-03-24)

| Register | Canonical value | Filed lines | What must not survive |
|---|---|---|---|
| Feb→Dec 1995 price step-up | **+94.1%** under both conventions — `94.118` displayed / `94.137` exact ⅓, **0.02 points apart** | l.2864 `$0.1717`; l.4301–4302 `3,021,000 shares … $.3333 per share, or an aggregate of $1,007,000` | **`+95.2%` anywhere as a live value** (it requires an unfiled February price of $0.1708) |
| One-third composition leg | **$871,000** — `2,613,000 × ($1,007,000 ÷ 3,021,000) = 2,613,000 ÷ 3` exactly | l.4301–4302 | **`$871,024` as if it were a filed figure** (it was a back-solved plug: `1,272,000 − 295,568 − 5,408 − 150,000 + 50,000`) |
| Purchaser composition total | **$976,408**, $24 gap to the $976,432 residual arithmetic **accounted for, not plugged** (≈$19 filed-thousands rounding of the equity line + the ±$5 Alberg convention at d7) | l.3535, l.3546, l.3645 (+ l.3556–3559, l.3458, l.4296) | Restating the composition as **$976,432** |
| Bezos post-IPO stake | **43% = original S-1** (l.985–988, l.2919); **41% = S-1/A No. 5** (acc. 0000891020-97-000839, l.1055–1062, l.3149) — a **version discrepancy kept visible**, never averaged or merged | as listed | An unattributed 41%/43% pair, or 41% under a "Form S-1 (original)" label |

## 2. Sweep method and the sites actually found

Greps run with `-n` over `01_companies/company_001_amazon/` (all `*.md`, `*.csv`; `sources/` excluded as the primary
archive) plus a corpus-wide pass over `founders_playbook/`, for `871,024`, `95.2`, `976,432`, `41%`, `43%`, and for the
inconsistent-shape variants the named list did **not** predict: `871024`, `976432`, `+95 `, `95 percent`, `$0.1708`,
`2,613,000`, `one-third`, `⅓`, `upper bound`, `step-up`, `94.1`, `871,000`, `976,408`. **The named list of four
survivors under-counted, as expected: the sweep found six sites needing action inside scope and two inside-scope
consistency defects nobody had named, plus nine out-of-scope survivors.**

### 2.1 Sites aligned (written by this pass)

| # | Site | Before (stale) | After (aligned) |
|---|---|---|---|
| 1 | `stage_1.md` **§S l.1100** (row "Identity of the residual ≈$976,000") | components itemised as "+ ≈$871,024 of unaffiliated program shares", no composition total | leg reads **$871,000** with the arithmetic shown (`2,613,000 ÷ 3` exactly, l.4301–4302) and the composition totalled at **$976,408**, marked a band-level tie inside ±$1,000 rather than an exact tie to the d8 residual arithmetic; the plug is recorded as **retracted** (F-4 / RD-027). 4 cells, geometry unchanged |
| 2 | `stage_1.md` **§U.8 l.1406–1412** (BEST-SUPPORTED INTERPRETATION) | "and ≈$871,024 of unaffiliated program shares, less the $50,000 …" | "$871,000 … = **$976,408**. Those legs are the filing's own lines; the composition is a band-level tie … the $24 difference is accounted for at §P.2 d8a, not plugged", the plug **retracted**, and the entry states plainly that retracting it **buys no knowledge**: who bought the ≈$871,000 and when inside 1995-12-06 → 1996-05-16 remain **UNKNOWN** (U.8's RESIDUAL UNCERTAINTY / CONFIDENCE cells unchanged) |
| 3 | `data_gaps.csv` **r11 `best_available_evidence`** | "~$871,024 … − $50,000 … = $976,432" (a composition presented as footing to the residual) | "$871,000 (2,613,000 unaffiliated programme shares on the filing's exact one-third … = 871,000 exactly, orig. l.4301-4302) − $50,000 … = **$976,408** — a band-level composition …, not an exact tie to the 976,432 residual arithmetic", with the $24 explanation and the retraction named |
| 4 | `data_gaps.csv` **r11 `importance`** — *un-named defect found by the sweep* | "**it is the upper bound** on un-named share purchases", contradicting r11's own `why_missing` and `confidence` cells, which already withdrew the upper-bound framing | "the un-named share money inside the audited CY1995 equity line (not an upper bound: part of it is the advance for shares not yet issued at 1995-12-31, which bought no 1995 shares)" — no figure placed in a prose column; field double-quoted per §13 because it contains commas |
| 5 | `context_appendices.md` **l.596** ("Capital raised inside Stage 1", the block-I quantitative row) | "≈$871,024 unaffiliated program shares − $50,000 …" with no tie | "**$871,000** unaffiliated program shares (2,613,000 × the filing's exact ⅓ = 2,613,000 ÷ 3 = $871,000 exactly) − $50,000 … = **$976,408**, a band-level composition … rather than an exact tie to the $976,432 residual arithmetic"; plug **retracted**; "identities behind the ≈$871,000 remain UNKNOWN". 8 cells, geometry unchanged; `confidence` cell still cites the row's own source (S-1/A No. 5, version-safe per COR-02) — **no citation was added or changed** |
| 6 | `_parts/NUMBER_DEFECTS.md` **row 43** (register row for D29) — *history kept, not rewritten* | `should_be` still instructs "note that on the filing's exact ⅓ price the Feb→Dec step-up is **+95.2%**, not +94.1%" | clause kept **verbatim** and followed by the appended marker: "**SUPERSEDED 2026-09-24 by number_repairs2: value corrected to +94.1%**", with the two computations, the 0.02-point separation, and the $0.1708 requirement, and an instruction not to import the clause |
| 7 | `_parts/NUMBER_DEFECTS.md` **appended supersession footer** (new content below the register's own "Not defects" paragraph; the table above it untouched) | — | markers for row 43 and for rows **27–28**: the instructions stand and their `should_be` leg already read **≈$871,000**, but the first repair pass rendered it as a plug, so the **executed output only** is superseded ($871,000 → composition $976,408, $24 accounted for). Records 43%/41% as a **version discrepancy**, and states this register carries no 41%-to-the-original row |

## 3. Re-grep after the sweep (company directory, `sources/` excluded)

| String | Occurrences after sweep | Disposition |
|---|---|---|
| `871,024` | **0 live values.** 3 quotations: `stage_1.md` l.901–902 (§P.2 d8a — the retraction itself quotes the figure it retracts) and `quantitative.csv` L35 `notes` (same, F-4 record) | **Deliberately kept.** A retraction that does not name what it retracted cannot be audited; both are deletion records, not values |
| `95.2` | **0 live values.** 5 quotations: `stage_1.md` l.883/886 (§P.2 d6 "THE +95.2% SENSITIVITY IS DELETED HERE"), `quantitative.csv` L30 `notes` (correction record), `_parts/NUMBER_DEFECTS.md` l.43 (the origin, now marked) and l.65 (this pass's appended marker) | **Deliberately kept** — every one is the sentence that deletes it. `_parts/` is an audit trail and was marked, not rewritten |
| `976,432` | 21 lines, **all of them the d8 residual arithmetic (`1,272,000 − 295,568`), a "not an exact tie to …" disclaimer, or out-of-scope volumes** — except one (below) | Composition now foots to $976,408 in every file this pass owns |
| `41%` / `43%` in scope | `stage_1.md` §S and §U.8: **no mis-attributed instance** (`§U.29` and `conflicts.csv` r30 were already split by accession by number_repairs2 and were not touched) | Version discrepancy intact and visible |

**Zero stale occurrences remain in the four files this pass owns.**

## 4. Survivors this pass could NOT write (reported, not repaired) — the sweep's real yield

These are outside the named list. Each carries the same defect class just corrected in scope and needs its owner.

| Site | Defect | Owner / route |
|---|---|---|
| `stage_1.md` **l.556 (§K, "Reconciliation of the two totals")** | prints the composition as "$5,408 + $150,000 + ≈$871,000 − $50,000 **= $976,432**" — the leg is right but the **tie is the retired one**; should read **$976,408**, band-level | §K owner / number-repair pass (`stage_1.md` §K is not in this pass's scope) |
| `stage_1.md` **l.184 (§A, "Personal capital and ownership")** | "post-IPO **~41–43%**" as an **unattributed pair**, under a Source cell that names only the original S-1 — exactly the COR-01 / F-8 class | §A owner; the split belongs to §U.29's per-accession form |
| `stage_1_claim_records.md` **l.445 (P09)** | "≈976,432 unnamed" carried as the value cell without the ±$1,000 rendering (already flagged by the recheck, never actioned) | claim-record appendix owner |
| `stage_1_claim_records.md` **l.376 (K14)**, `_parts/s1_claims_KU.md` **l.37**, `research/E_supply_ops_finance.md` **l.25 (E-59)** | **41% under a "Form S-1" label** with a No. 5 date / No. 5 accession cited *as* the S-1 (COR-01) | claim-record and dossier owners |
| `research/E_supply_ops_finance.md` **l.75, l.261, l.324** | residual stated as **$976,432** and as "includes option exercises which are commingled in the same line" — the withdrawn option-cash explanation | dossier E (frozen research volume) |
| `_parts/s1_p4.md` **l.46, l.98, l.176, l.203**; `_parts/s1_p1.md` **l.70**; `_parts/s1_p3.md` **l.24** | intermediate volumes: **≈$976,432** live, and l.203 still says "the residual also absorbs option-exercise proceeds" (the wording §S withdrew) | `_parts/` is an audit trail: **mark, do not rewrite** (this pass may only write `NUMBER_DEFECTS.md`) |
| `MASTER_RESEARCH_LOG.md` **l.247**; `RESUME_HANDOFF.md` **l.14, l.24, l.27** | log/handoff still say "fix the +95.2% step-up" and "delete the $871,024 plug", and the log quotes "~$976,432" as the residual identity gap | orchestrator's files; **stale instructions, not stale values** — the handoff should be closed by whoever owns it |
| `03_quality_control/amazon_s1_audit3_numbers.md` **l.137**; `amazon_s1_audit3_recheck.md` **l.161, l.216, l.219, l.240, l.243**; `amazon_s1_number_repairs.md` **l.88** | the wrong `+95.2%` / `$871,024` appear inside **audit findings and the first repair's own log** | **Frozen by design** — these are the records of what was found; not edited, not to be edited |
| `_MANIFEST.md` l.6, l.84 — "**43%** of the word ceiling" | **not a hit**: a byte/word-ceiling percentage, not the ownership figure. Listed only to show the grep saw it and rejected it on cause | n/a |

## 5. CSV validation actually run (not assumed)

`data_gaps.csv` parsed with Python `csv` (the only CSV this pass wrote); all company CSVs parsed for geometry.

| Test | `data_gaps.csv` |
|---|---|
| Rows / data rows / columns | 24 / **23** / **8** — widths `{8}` for every row, **0 field-count mismatches** |
| Empty cells (§13: an empty cell is a defect) | **0** |
| `company` == `Amazon.com`, `stage` ∈ {stage1, stage2-consequence, stage3-consequence} | **True** in every row |
| `importance` opens with a severity word; `confidence` opens with a confidence word (class-value-in-wrong-column test) | **True** in every row; no money figure sits in `importance` or `confidence` |
| `follow_up_task` non-empty wherever `importance` is High (§13) | **True** — 0 violations |
| Quoting / serialization | UTF-8, **LF only, no CRLF, no BOM**; `QUOTE_MINIMAL` **round-trip byte-identical: True** (r11's two comma-bearing prose fields are double-quoted; the re-serialization did not have to add or strip a single quote) |
| Cross-file geometry (read-only) | `channels` 16×11, `conflicts` 43×15, `decisions` 16×15, `failures` 34×11, `quantitative` 112×12, `sources` 103×18, `timeline` 58×11, `validation` 30×11 — **uniform widths, 0 empty cells anywhere except the 74 legitimately empty `derived_arithmetic` cells on FACT/UNKNOWN rows in `quantitative.csv`**, matching `number_repairs2`'s own count exactly |

**The detector was proved to be able to fail, not merely to pass.** A throwaway **copy** of `data_gaps.csv` in the OS
temp directory (`%TEMP%\data_gaps_PLANTED_badcopy.csv` — the real file was never touched and nothing in the workspace
was created or removed for the test) was planted with a 9-field row and a row carrying `871,024` in the wrong column
with two empty fields. The same script flags the planted copy **6 times** (field-count mismatch at row 4, empty
`confidence` and `follow_up_task`, an empty follow-up on a High-importance row, a money figure in a prose column) and
reports `QUOTE_MINIMAL round-trip identical: False`, while reporting **0 problems** on the real file. A test that
cannot fail is not a test.

## 6. What this pass is not

**Verification of this pass must not diff against `HEAD`.** A sibling agent's commit `afb7aac` ("Number repairs round 2
landed…") landed **mid-sweep** and swept up this pass's `stage_1.md` and `context_appendices.md` edits, so those two
files show clean in `git status` while carrying this sweep's text; only `_parts/NUMBER_DEFECTS.md` and `data_gaps.csv`
still read as modified. Confirmed by reading the committed blobs directly (`git show HEAD:…` contains
"back-solved balancing plug and is" in `stage_1.md` and "back-solved balancing plug" in `context_appendices.md`). This
is the same hazard `number_repairs2` disclosed at its own caveat (a).

A sweep is a propagation, not a verification: every value written here is number_repairs2's, carried to files its own
author could not open, and the two §S/§U.8 arithmetic claims ($871,000 as a true third; $976,408 as the composition
total) still need an independent read of orig. l.4301–4302, l.3535, l.3546, l.3645 by the next auditor. **No `UNKNOWN`
was upgraded to make a row read well** — the identities behind ≈$871,000, the date split of the $1,007,000 program and
the 1995 ownership percentage all stay UNKNOWN. Until §K l.556, §A l.184 and the `_parts/` and `research/` volumes in
§4 are acted on by their owners, the corpus is **not internally consistent** on the composition tie and the
41%-attribution family, and a re-auditor will (correctly) find those cells disagreeing with §P.2 d8a/d6 and §U.29.
