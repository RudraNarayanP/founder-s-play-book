# Amazon Stage 1 — NUMERIC CLOSURE, FINAL (Level-3 Register Finisher)

Run **2026-09-24**. Successor to the closure round that died at its turn limit with the arithmetic finished and the
sheets unwritten. Owns **four items and three writes**: `stage_1.md`, `quantitative.csv`, and this sheet plus
`amazon_s1_causal_lineage_closure.md`. **0 web requests** — every figure below was read from files already on disk
against the restored primaries in `sources/`. **No file was deleted, moved, renamed or tidied.** Where a wrong
string was removed, it survives only inside a sentence that says it is wrong.

Line numbers are post-edit for the two files this pass touched.

---

## 1. Closed by earlier rounds (verified on disk this pass, not carried forward on assertion)

| # | Item | Canonical now | Where it lives | Status of the wrong value |
|---|---|---|---|---|
| N-1 | **The one-third equity leg.** `2,613,000` shares was cited to orig. l.4301–4302, which contains `3,021,000 / $1,007,000 / $.3333` and **not** `2,613,000`. The number is reachable only by back-solving the d25 chain that `quantitative.csv` L99 itself holds at **UNKNOWN, "RECORDED BUT NOT ADOPTED"**, and "unaffiliated" collides with the filed unaffiliated count `2,811,000` (A5 l.4667–4668) | **UNKNOWN** — the denominator is neither filed nor derivable, so the leg gets no figure | `stage_1.md` §P.2 **d8a** (ll. 931–970), §K l.584, §P20 l.848, §S l.1177, §U.8 l.1488; `quantitative.csv` **L35** (value `976000`, composition UNKNOWN), **L99** (`UNKNOWN`, held there by ruling) | **`$871,024`** (a back-solved balancing plug) and **`$871,000`** (its re-doctored successor, `2,613,000 ÷ 3`) both survive **only as retractions** — stage_1.md ll. 939–941, 1037, 1488, 1157; no live value cell carries either |
| N-2 | **The residual's precision.** `1,272,000 − 295,568 = $976,432` printed six significant figures off inputs filed to the nearest thousand | **≈$976,000 (±$1,000)**; on rounding alone the residual spans ≈$974,900–$977,900 | `stage_1.md` §P.2 **d8** l.929, §P20 l.848, §R Capital l.1149; `quantitative.csv` **L35** | `$976,432` retained **as the exact subtraction of two audited lines**, banded, never as a point |
| N-3 | **The price step-up.** `+95.2% ("exact ⅓")` was a sensitivity invented by the first repair pass; the two conventions differ by 0.02 points (94.118 displayed / 94.137 exact), not 1.1 | **+94.1%** on both conventions | `stage_1.md` §P.2 **d6** ll. 918–924; `quantitative.csv` **L30** (value `94.1`) | `+95.2%` survives only where it is deleted and explained (l. 920, l. 923 — to yield it the February price would have to be $0.1708 against the filed $0.1717) |
| N-4 | **The Miguel Bezos product.** `582,528 × $0.1717` printed as `$100,019` / `$100,019.06`, wrong by exactly **$1.00** | **100,020.06** → register value `100020`; the `≈` is stated because the price itself may be a rounded display | `stage_1.md` §P.2 **d4** ll. 914–915, §P16; `quantitative.csv` **L22** | `$100,019` appears only inside the correction sentence |
| N-5 | **The deficit.** The register carried "Cumulative losses since inception **$355,000**" as the accumulated deficit; $355,000 is the **sum of the two loss years**, not the filed deficit | **(248,000)** as filed (orig. l.3461), with the roll-forward shown: `52 + 303 − 107 = 248` | `stage_1.md` §P.2 **d26** ll. 1040–1045, §P68 l.888, §M l.663, §A l.128; `quantitative.csv` **L54** (`248000`, `FACT (audited)`) | `$355,000` survives only as the loss-years sum and as the named retired value; equity cross-foots `1,075 + 150 − 248 = 977` |
| N-6 | **The register's own three errors** (verify-3 F-6, F-7, F-8) | — | — | **F-6 CLOSED**: L30's `source_date` now `1997-03-24 / 1997-05-14`, matching its original-only line citations. **F-7 CLOSED**: `derived_arithmetic` cleared off non-calculated rows (7 → 0; the last one, L38 `INFERENCE`, was closed by **this** pass — see §2). **F-8 OPEN**: packed `value` cells L102/L103 — see the residual list |

## 2. Changed by this pass

| Item | Finding | Action |
|---|---|---|
| **1 — the duplicate rounding** | `21,382.98` occurs in `quantitative.csv` **exactly once**, at **L112**, and that occurrence is **not** in the `derived_arithmetic` field. The field reads `511,000 ÷ (5.5 × 4.345 = 23.8975 weeks) = 21,382.99 → $21,383`; the `21,382.98` sits in the `notes` column inside the sentence "**this cell carried 21,382.98 — a truncation introduced when §P.2 d30 was copied into the register**" (verify-3 F-2 / RD-030). A third match, `21,382.9899`, is the exact quotient quoted by the same sentence | **Left alone — it is a retraction that intentionally quotes the wrong value, and this sheet records that.** No edit was possible or needed: the register carries **one** live rendering (`21,382.99`, plus the correct `$21,383` / band `19440-21383`), and `stage_1.md` ll. 1055–1058 mirrors it exactly. Census across the company directory: `21,382.99` × 3 in L112 + 2 in `stage_1.md` + 1 in `conflicts.csv` r10; `21,382.98` × 1 (retraction) in each of L112 and `stage_1.md` |
| **2 — the bridge arithmetic** | Located at `stage_1.md` §P.2 **d14** (ll. 978–987; the brief's "around line 917" is its pre-merge position) and its twin `quantitative.csv` **L66**. Both had already been rewritten to the **filed** two-line form by verify-3 F-1 / RD-029: `−232 (l.3636) − 52 (l.3641) + 1,228 (l.3649) = +944` (the filed net-increase line, l.3652), then `52 (l.3653) + 944 = 996` (the filed closing line, l.3655). §P36 l.864 keeps the single-line form `52,000 − 232,000 − 52,000 + 1,228,000 = 996,000`, whose left-hand side **does** sum to 996, and now says so | **No edit required, and no term adjusted.** The false form `52 − 232 − 52 + 1,228 = 944` survives in exactly three places, all of them retractions (`stage_1.md` l.982, `quantitative.csv` L66 notes, `validation.csv` r17). **Nothing in the bridge is UNKNOWN**: 944 and 996 are both filed lines, so the gap never needed inventing. Sweep for a surviving live instance of the false equation across all registers, parts and claim records: **0** |
| **3 — six `U.41` pointers** | See `amazon_s1_causal_lineage_closure.md` §3 for the full reconciliation. Result: 1 live pointer (resolves here), 1 pointer already retargeted to **U.43**, 3 intentional id-quotations, 1 block | **Appended** a `POINTER/BLOCK RECONCILIATION` note inside the U.41 block (`stage_1.md` ll. 2218–2231) and an append-only spine note at l. 2315 (`conflicts.csv` must be generated one row per canonical id, now **U.1–U.43**, 43 rows for 43 ids verified by parse). No pointer deleted |
| **Schema completion of F-7** | After the earlier rounds, **one** row still carried `derived_arithmetic` off-class: `quantitative.csv` **L38**, class `INFERENCE` (the 5.5–6.0-month trading band) | **String relocated verbatim into `notes`** with an explicit `RELOCATED FROM derived_arithmetic per verify-3 F-7 / RD-033` marker. Nothing deleted, no value touched, row count and line positions unchanged. Field is now populated on **29/29** `DERIVED` rows and **0** others |

## 3. Residual-defect list — **9 items** (R-1 … R-9)

Ranked by the harm a future pass would do with them. None is a wrong number in a Stage-1 cell.

| ID | Defect | Where | Class |
|---|---|---|---|
| **R-1** | `2,613,000`'s one-third leg is **permanently UNKNOWN**; the residual ≈$976,000 has only **three filed legs ($105,408)** and its balance is unattributed **both as to identity and as to figure** | stage_1.md d8a ll. 931–970; `quantitative.csv` L35, L99; `data_gaps.csv` r11 | Standing UNKNOWN — correct, not repairable |
| **R-2** | `derived_arithmetic` rule **cannot be satisfied by `ESTIMATE`** anywhere: the register's class census has **0** `ESTIMATE` rows (12 classes, 29 DERIVED, 82 non-calculated), so "mandatory on DERIVED/ESTIMATE" reads as "mandatory on DERIVED" in practice | `quantitative.csv` column `evidence_class` | Schema wording for the method owner |
| **R-3** | **F-8 open** — packed `value` cells: **L102** `151 / 158 / 256` (three as-of dates in one field, and the 151-vs-158 conflict therefore has no machine-readable row) and **L103** `≈180,000 accounts; >$16,000,000` (two measures, `unit` = "accounts and USD"). Same family: **L79** and **L105** carry a count inside `unit` ("distinct titles (advertised as more than 1,000,000)") | `quantitative.csv` L79, L102, L103, L105 — all `stage2-consequence`, all outside the Stage-1 boundary | Register geometry; no Stage-1 number at risk |
| **R-4** | The deleted false bridge **still prints live** in `_parts/s1_p4.md` **ll. 102–103** (`52 − 232 − 52 + 1,228 = +944`), alongside pre-repair d4 `100,019.06`, d5 `145,552.83`, d7 `295,567` and the withdrawn "upper bound / commingled option cash" wording | `_parts/s1_p4.md` (frozen staging fragment, retained as the merge's audit trail per RD-038) | Re-import hazard for a future consolidation |
| **R-5** | `_parts/U_CONCORDANCE.md` still states "**Final count: 42 canonical conflicts**", has **no row for canonical U.43**, and its l.71 cites "U.41 boundary discipline" inside the vendor-agreement (U.40) row | `_parts/U_CONCORDANCE.md` ll. 14, 71 | Mapping volume predates the append-only additions |
| **R-6** | Part-local `Conflicts: U.41` keys for the **artifact** rows (canonical **U.21**) survive in `_parts/s1_claims_AJ.md` ll. 157–162, 325 — correctly re-keyed in the merged `stage_1_claim_records.md` (E01–E06 → U.21), wrongly keyed in the part | `_parts/s1_claims_AJ.md` | Same hazard as R-4 |
| **R-7** | **RD-id collision, unresolved and escalated**: this numeric family cites **RD-027, RD-029, RD-030, RD-031, RD-033**, which `MASTER_RESEARCH_LOG.md` ll. 490–495 assigns to *other* debts (RD-029 = directory-placement efficacy, RD-030 = the company-only merchant-account counterfactual, RD-031 = 1995 press-coverage effect); `data_gaps.csv` uses RD-027/RD-031 in the numeric sense | `MASTER_RESEARCH_LOG.md` l. 490 (records the RD-025…RD-028 collision, "recorded rather than tidied"); RD-042 **OPEN — High**, assigned to the Orchestrator | Traceability, not accuracy |
| **R-8** | Mirror not closed: `stage_1.md` **§T l.1206** still grades the **424B1 final prospectus** `restoration pending` although `sources/424B1_final-prospectus_acc-0000891020-97-000868_filed-1997-05-15.txt` landed on disk at 17:00 during the closure pass (`_MANIFEST.md` l.94); and §T/`_MANIFEST` record that four non-SEC items from COR-08 remain pending | stage_1.md §T ll. 1185–1209 | Provenance bookkeeping (out of this pass's four items) |
| **R-9** | Three count/range claims in the file's self-description do not verify: (i) **"`stage_1_claim_records.md` — 432 records"** — on-disk census is **418** dossier claim records (prefixes A1…T22) plus **13** condensed `U.n Claim:` spine records = **431** `Claim:` lines; (ii) `stage_1.md` l. 2315's generation instruction still says `conflicts.csv` is one row per canonical id **U.1–U.42** (now annotated as **U.1–U.43**, which parses); (iii) `stage_1_claim_records.md` **l.15** carries the same stale `U.1–U.42` range | stage_1.md ll. 2292, 2315–2317; `stage_1_claim_records.md` ll. 15, 555–567 | Arithmetic of the file's own self-description. The record count was **not** repaired: settling 432 vs 431 needs a merge-time recount of the appendix, which is the re-audit this pass was told not to run |

## 4. Final CSV parse — all nine registers in `company_001_amazon/`

Parsed with Python `csv`, UTF-8, `newline=''`; both edited files verified **LF-only, no BOM, trailing newline, 0 stray CR**.

| Register | Data rows | Fields/row | Off-grid rows | Empty cells | Wrong-column values |
|---|---|---|---|---|---|
| `channels.csv` | 15 | 11 | **0** | 0 / 165 | 0 |
| `conflicts.csv` | **43** | 15 | **0** | 0 / 645 | 0 |
| `data_gaps.csv` | 23 | 8 | **0** | 0 / 184 | 0 |
| `decisions.csv` | 15 | 15 | **0** | 0 / 225 | 0 |
| `failures.csv` | 33 | 11 | **0** | 0 / 363 | 0 |
| `quantitative.csv` | 111 | 12 | **0** | 82 / 1,332 | 0 (4 shape exceptions = R-3) |
| `sources.csv` | 102 | 18 | **0** | 0 / 1,836 | 0 |
| `timeline.csv` | 57 | 11 | **0** | 0 / 627 | 0 |
| `validation.csv` | 29 | 11 | **0** | 0 / 319 | 0 |
| **Total** | **428** | — | **0** | **82** | **0** |

* **Uniform field counts: 9/9 files, 428 data rows, 0 off-grid rows.**
* **The 82 empty cells are 100% the `derived_arithmetic` column of the 82 non-calculated `quantitative.csv` rows.**
  No other register has an empty cell.
* **`derived_arithmetic` populated only on DERIVED rows: 29 populated / 29 `DERIVED`-class rows; 0 populated on
  `FACT (audited)` (40), `FACT` (18), `UNKNOWN` (9), `FACT (company claim)` (3), `FACT (company self-measured)` (2),
  `FACT (as disclosed)` (3), and 1 each of `FOUNDER CLAIM`, `INFERENCE`, `CONTEMPORARY OBSERVATION`,
  `FACT (1997 claim)`, `FACT (third-party estimate quoted in a filing)`, `FACT (audited-period filing; basis
  labelled)`, `FACT (per date; 151 vs 158 conflicting basis)`.** Before this pass: 30 populated / 7 violations
  (verify-3 F-7 counted 7); after: 29 / 0. No DERIVED row is missing the field.
* **Date columns:** every value in `decisions.date`, `failures.date`, `validation.date`, `quantitative.date`,
  `quantitative.source_date`, `sources.event_date / publication_date / access_date`, `conflicts.claim_a_date /
  claim_b_date`, `timeline.date_or_range`, `channels.date_tested` is either ISO-shaped or a declared qualifier
  (`UNKNOWN`, `bounded 1994-11 to 1995-07`, `by 1995-12-31`, `spring 1994`, `undated: …`, `earliest independently
  evidenced 1997-01-28`, `advertised live by 1995-10-04`). **Misplaced values found: 0.**
* **`company` column:** constant in every register (`Amazon.com` in `quantitative.csv` 111/111;
  `"Amazon.com, Inc."` in `conflicts.csv` 43/43).
* **`stage` fence:** `quantitative.csv` 94 `stage1` + 17 `stage2-consequence`; `timeline.csv` 49 + 8;
  `validation.csv` 26 + 3; `channels.csv` 12 + 3; `data_gaps.csv` 23 `stage1`.
* **`conflicts.csv` id spine:** 43 rows = **U.1 … U.43**, no gaps, no duplicates — 1:1 with the 43 canonical
  `**U.n —` blocks in `stage_1.md` §U.

## 5. Verdict

**Stage 1's numeric layer is internally consistent.** Every live number in `stage_1.md` §P/§R/§M/§K and in
`quantitative.csv` is either a filed line, a re-runnable derivation on filed inputs with its precision capped to
what those inputs support, or an explicit UNKNOWN; every superseded figure that remains on disk remains only inside
a sentence that marks it superseded; the register's geometry, its fence columns and its arithmetic field are now
clean on parse. **No value in this Stage-1 set is now wrong-and-uncorrected.** What is left is nine named
residuals — three standing UNKNOWNs by construction, four register-geometry or provenance-bookkeeping items, and
two cross-file hazards in `_parts/` — none of which changes a Stage-1 number, and all of which are written down
rather than smoothed over.
