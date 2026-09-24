# Amazon Stage 1 — AUDIT 3 (Numbers) REPAIR LOG, ROUND 2
Level-2 Company Lead (numbers repair, round 2) · run 2026-09-23 · owns **exactly the six items** named by
`03_quality_control/amazon_s1_audit3_recheck.md` (failure rows **F-1, F-3, F-4, F-8, F-9** = research debts
**RD-024, RD-025, RD-026, RD-027, RD-028**, plus the D15 closure the recheck says is not complete).
Authority: the recheck sheet (which names each defect and its location), `CORRECTIONS.md` (COR-01, COR-02, COR-10 as
corrected, COR-12, COR-14.2), `00_METHOD_AND_STYLE.md` §8 (no value without source and confidence cells; `UNKNOWN` is
a complete value) and §13 (schemas; every field containing a comma, quote or newline is double-quoted).

**Files written by this pass — nothing else:** `stage_1.md` **§P (incl. §P.2), §R, §U.29 only**; `quantitative.csv`;
`validation.csv`; `conflicts.csv`; this log. **`context_appendices.md` and the Appendix prose were not opened for
writing** (sibling agent owns them). No file deleted, moved or renamed; `_parts/`, `sources/`, `data_gaps.csv`,
`decisions.csv`, `timeline.csv`, `failures.csv`, `sources.csv`, `channels.csv`, `stage_1_claim_records.md` untouched.

Primaries, greps run with `-n` against `company_001_amazon/sources/` ("orig." = S-1 original acc. 0000891618-97-001309,
1997-03-24; "A5" = S-1/A No. 5 acc. 0000891020-97-000839, 1997-05-14). Every line below was read out of the document,
not out of the recheck sheet; the line relied on is quoted in the cell.

| # | Defect (recheck id) | Disposition | Site(s) written | The filing line that settled it |
|---|---|---|---|---|
| 1 | **F-1 / RD-024** — false `+95.2%` step-up "on the filing's exact ⅓", 3 sites | **FIXED.** Recomputed: displayed `(0.3333 − 0.1717) ÷ 0.1717 = 0.94118 → +94.1%`; exact ⅓ `(0.33333… − 0.1717) ÷ 0.1717 = 0.94137 → +94.1%`. Conventions differ by **0.019 points**, not 1.1. The sensitivity is deleted and the deletion explained, since 95.2% requires a February price of **$0.170765 ≈ $0.1708**, filed nowhere | `stage_1.md` §P **P17**, §P.2 **d6**; `quantitative.csv` **L30** (`derived_arithmetic` + `notes`) | orig. **l.2864** `"…582,528 shares of Common Stock to Miguel / A. Bezos at a price per share of $0.1717…"`; orig. **l.4301–4302** `"aggregate of 3,021,000 shares of Common Stock to 23 investors for a / consideration of approximately $.3333 per share, or an aggregate of $1,007,000"` (3,021,000 ÷ 3 = 1,007,000 exactly, so the ⅓ is right and only the ratio computed with it was wrong) |
| 2 | **F-3 / RD-025 / D19 half-applied** — §R cited a `quantitative.csv` row that was never written | **ROW ADDED** (chosen over deleting §R's citation): the figure is recoverable from filed inputs, so the register's own `should_be` ("carry it into §P.2 **+ `quantitative.csv`**") is satisfiable and the cross-reference is worth more than the cut. New row: stage1 / 1995-12-31 / "Average net sales per trading week, FY1995 (BAND, not a point)" / `19440-21383` / `USD/week` / DERIVED / Medium, with provenance and the d24-band caveat in `notes`; appended at the file end so **no existing line reference (L30/L35/L70/L97–L99) shifts** — the `stage` field, not position, is the boundary fence. §R's cell now names the row it points at; §P.2 d30 records that the promise was false when received | `quantitative.csv` **line 112** (new); `stage_1.md` §R "Weaknesses"; §P.2 **d30** | orig. **l.3489** `Net sales................................. $ -- $ 511 $ 15,746`; orig. **l.1435** `"Net sales grew from $511,000 in 1995 to $15.7 million in 1996"`; orig. **l.1377–1378** `"For the period beginning with the / opening of the Amazon.com bookstore in July 1995 through December 31, 1995"` (day UNKNOWN ⇒ band). Arithmetic `511,000 ÷ (5.5 × 4.345) = 21,382.99`; `511,000 ÷ (184 ÷ 7 = 26.2857) = 19,440.22` |
| 3 | **F-9 / RD-026 / D15** — `validation.csv` r20: class written into `confidence`, `evidence_class` left stale at DERIVED | **FIXED, each value moved to its own column, row re-validated.** `evidence_class` → `FACT (audited) - balance-sheet line (S-1 (orig.) l.3429 'Inventories ... 17' at December 31, 1995)`; `confidence` → `High (the filed line) / Medium (the inferred 1994 zero opening)` (the destroyed pre-repair value was `Medium-High`; it is now split by component because only the 1994 opening is inferred). `notes` records the column slip and that the first pass's fix "existed in the file but not in the field a query reads" | `validation.csv` **r20** (only row changed in the file) | orig. **l.3429** `Inventories...........................................       17         571` (same figure in A5 l.3663). Three-way agreement now holds on the class of $17,000: §P39 `**FACT (audited)**` + High, `quantitative.csv` L70 `FACT (audited)` + High, `validation.csv` r20 `FACT (audited)` + High/Medium by component → **D15 CLOSED** |
| 4 | **F-4 / RD-027** — `≈$871,024` presented as "2,613,000 shares at the filing's exact ⅓" | **TRUE THIRD USED, AND THE PLUG NAMED.** Leg is now `$871,000` (`2,613,000 × ($1,007,000 ÷ 3,021,000) = 2,613,000 ÷ 3 = 871,000 exactly`); composition foots to **$976,408**, not $976,432; the $24 gap is **accounted for, not plugged**: ≈$19 from the filed-thousands rounding of the equity line (exact $1,271,980.89 vs filed `1,272`) plus the $5 Alberg convention (d7) — on exact prices throughout both sides meet at $976,408, i.e. a **band-level composition inside the row's ±$1,000**, not an exact tie. The deleted `871,024` is shown for what it was: `1,272,000 − 295,568 − 5,408 − 150,000 + 50,000`, back-solved from the displayed-price convention | `stage_1.md` §P.2 **d8a**; `quantitative.csv` **L35** (`notes`, incl. the cross-foot) | orig. **l.4301–4302** (the ⅓ source); **l.3546** `4,235,244 1,172 (50) … 1,122`; **l.3535** `Advances received for common stock … 50`; **l.3556–3559 / l.3458** `150` advances; **l.4296** `aggregate of $5,408`; **l.3645** `1,272`. Check: `5,408 + 150,000 + 871,000 − 50,000 = 976,408` ✓ |
| 5 | **D15 not closed** | **CLOSED as a three-file item**, not as one cell: the residual unclosed piece of register row 15 was exactly the `validation.csv` r20 field placement (item 3); §P39 and L70 were already FACT (audited). Verified by parsing all three carriers and reading the class out of each, and the row's `notes` now points at the other two so the tie is checkable by the next auditor | `validation.csv` r20 + its `notes`; nothing further written for §P39/L70 | orig. **l.3429** (above). Recheck CHECK 4 break "F-9 … the three files still disagree on the class of $17,000" no longer holds |
| 6 | **F-8 / RD-028** — `conflicts.csv` r30 and §U.29 attributed the **41%** to the original S-1 | **ATTRIBUTION SPLIT BY ACCESSION, DIFFERENCE KEPT VISIBLE.** §U.29 now carries CLAIM A (original: 43%/10% + table 48.3%/43.1%) and CLAIM A′ (S-1/A No. 5: 41%/10% + table 47.4%/41.4%), labelled a **version discrepancy between two accessions — not an error to average, reconcile or merge**; `conflicts.csv` r30 `claim_a`/`claim_a_source` = original only (date `1997-03-24` unchanged and now true), with the No. 5 pair in `why_they_differ` and its lines and date; **the false "confirmed in S0803" is deleted** (No. 5 does not confirm 43% — it replaces it) | `stage_1.md` **§U.29** (whole entry); `conflicts.csv` **r30** (7 fields) | orig. **l.985–988** `"…will be beneficially owned approximately 43% by Jeffrey / P. Bezos … and 10% by members of Mr. Bezos' family and trusts … (42% and 10%, respectively, if the over-allotment option is / exercised in full)"`; orig. **l.2919** `Jeffrey P. Bezos… 9,885,000 48.3% 43.1%`; **A5 l.1055–1062** `"approximately 41% by Jeffrey / P. Bezos … (41% and 10%, / respectively, if the over-allotment option is exercised in full)"`; **A5 l.3149** `9,885,000 47.4% 41.4%` |

## Why nothing else was "fixed while we were there"

The recheck's other failure rows are **not in this pass's six** and were left exactly as found, so they stay auditable
by whoever owns them: **F-2** (§P.2 d14 / `quantitative.csv` L66 cash-bridge notation — `52 − 232 − 52 + 1,228` written
as `= +944`; the LHS is 996; §P36 prints the bridge correctly), **F-5** (L81 `unit: counts`), **F-6** (>$16,000,000
cumulative-ship-basis label at §P60/L103), **F-7** (15,900,237 vs the amendments' 15,900,237-vs-15,900,229 variance at
§P67/d28). No new fact, figure or citation was introduced anywhere: each corrected number is carried by a document +
line printed above. `UNKNOWN` was not upgraded to make a row read well — the ~$921,000 in-window slice stays UNKNOWN
(RD-020), the identities behind ≈$871,000 stay UNKNOWN, the 1995 ownership percentage stays UNKNOWN.

## Self-verification actually run (not assumed)

Parsed with Python `csv`, all files UTF-8, LF, no CRLF introduced:

| File | parsed rows | data rows | cols | field-count mismatches | empty cells | class-word-in-`confidence` | QUOTE_MINIMAL round-trip identical |
|---|---|---|---|---|---|---|---|
| `quantitative.csv` | 112 | **111** (was 110; 1 row appended) | 12 | **0** | **0** outside the 74 legitimately empty `derived_arithmetic` cells on FACT/UNKNOWN rows | n/a | **True** |
| `validation.csv` | 30 | 29 | 11 | **0** | **0** | **0** (r20 was the only hit repo-wide and is cleared) | **True** |
| `conflicts.csv` | 43 | 42 | 15 | **0** | **0** | n/a | **True** |

* Content-shape (not just count) test: `company` is `Amazon.com` (validation/quantitative) or `Amazon.com, Inc.`
  (conflicts) in every row; `stage` ∈ {`stage1`, `stage2-consequence`}; r20's `evidence_class` now parses as an
  evidence class and its `confidence` as a confidence; every `DERIVED`/`ESTIMATE`/`INFERENCE` row in
  `quantitative.csv` has non-empty `derived_arithmetic` (**0 violations**, including the new row).
* **The column test was proved to be able to fail, not merely to pass:** re-running it against a planted copy of the
  old r20 state (`evidence_class` = DERIVED, class label in `confidence`) flags **row 20**; against the file as written
  it flags **nothing** — a test that cannot fail is not a test.
* Class of $17,000 read out of all three carriers after the edit: §P39 `FACT (audited)` / High · `quantitative.csv`
  L70 `FACT (audited)` / High · `validation.csv` r20 `FACT (audited) - balance-sheet line (l.3429)` /
  High + Medium by component → **D15 closed with the three in agreement**.
* Cell-level diff against the pre-repair commit `a52e978`: **`validation.csv` 3 changed cells, all in r20**
  (evidence_class, confidence, notes) on 1 physical line; **`conflicts.csv` 7 changed cells, all in r30** on 1 physical
  line; **`quantitative.csv` 3 changed cells in 2 content rows** — L30 (`derived_arithmetic`, `notes`) and L35 (`notes`)
  — **plus 1 appended row (line 112), and 0 changed cells among the other 109 data rows.** `quantitative.csv` differs
  from `a52e978` on 13 physical lines: 3 are content (L30, L35, the new L112) and **10 are pure quote normalisation**
  (lines 4, 7, 22, 24, 25, 26, 38, 74, 96, 102), because the file was re-serialised once with `QUOTE_MINIMAL` and
  twelve fields lost double-quotes they never needed; parsed content on those lines is byte-for-byte identical after
  normalisation.
* `stage_1.md` diff hunks fall only at l.805–811 (§P P17), 878–914 and 964–990 (§P.2 d6, d8a, d30), 1060–1083 (§R
  Weaknesses), 1849–1885 (§U.29) — **inside §P/§P.2/§R/§U.29 only**; table geometry re-checked: P17 = 9 cells,
  §R Weaknesses = 4 cells.
* Grep sweep of every retired string across the corpus (excluding `sources/`): `+95.2`, `871,024`,
  `976,432 ✓` as a composition tie, `DERIVED (cash-flow movement, $0 opening)` in `evidence_class`,
  `carried in quantitative.csv` (unbacked), `41%` attributed to the original.

## Surviving copies found OUTSIDE this pass's writable scope (reported, not repaired)

1. **`≈$871,024` still printed as a live value in four places this pass may not write:**
   `stage_1.md` **l.1100** (§S Data Gaps, "Its disclosed components are now itemised at §P.2 d8a: … + ≈$871,024"),
   `stage_1.md` **l.1406** (§U.8 best-supported interpretation), **`data_gaps.csv` r11** `best_available_evidence`
   ("+ ~$871,024 (2,613,000 unaffiliated programme shares at the filing's exact one-third)"), and
   **`context_appendices.md`** (the "Capital raised inside Stage 1" row, now at l.596; the sibling agent holds that
   file). Each repeats the item-4 defect. They are now **inconsistent with §P.2 d8a**, which they cite as their source.
2. **The false `+95.2%` survives at its origin:** `_parts/NUMBER_DEFECTS.md` **row 43** (register row for D29) still
   instructs "note that on the filing's exact ⅓ price the Feb→Dec step-up is **+95.2%**, not +94.1%" — that is where
   the first pass imported it from, and `_parts/` is read-only to repair passes. `03_quality_control/
   amazon_s1_audit3_numbers.md` **l.137** carries the same parenthetical, and `RESUME_HANDOFF.md` l.24 still tells the
   next agent to "fix the +95.2% step-up" (now done in the three owned sites). Both audit sheets are, by design,
   frozen records of what was found and were not edited.
3. **`41%` under a "Form S-1" label** (COR-01 class, same family as item 6) survives in files this pass may not write:
   `stage_1_claim_records.md` l.376 (K14, dated 1997-05-14 but titled "Form S-1, Risk Factors"),
   `research/E_supply_ops_finance.md` l.25 (E-59, accession 0000891020-97-000839 cited *as* the S-1),
   `_parts/s1_claims_KU.md` l.37, and `stage_1.md` **l.184** (§A, "post-IPO ~41–43%" — an unattributed pair, outside
   §P/§R/§U.29). The `_MANIFEST.md` hits on "43%" are a word-ceiling percentage, not this figure.

## Caveat this pass must state about itself

**A repair pass is a change to the corpus, not a verification of it.** Nothing above is correct because this file says
so: the three new numbers (+94.1% both ways, the $871,000 leg with its $24 explanation, the 19,440–21,383 band row) and
the re-placed `validation.csv` r20 fields are re-derivable from the printed filing lines, but they need an
**independent** re-audit, exactly as the first repair did — and four of the six items were created by a pass that
declared itself complete. Two further limits, disclosed rather than smoothed over: (a) `quantitative.csv` and
`validation.csv` were committed **mid-pass** by another agent's commit `bd3097c` ("Fast tier provisioned…"), so their
repair content sits inside a commit whose message does not describe it and a `git diff` against HEAD no longer shows
these two files — verification must diff against `a52e978`; (b) the four surviving `871,024` copies mean the corpus is
**not yet internally consistent** on that leg, and re-auditors will (correctly) find §S/§U.8/`data_gaps.csv`/the
appendix disagreeing with §P.2 d8a until their owners act.
