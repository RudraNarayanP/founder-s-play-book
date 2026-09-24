# Audit Sheet — Amazon.com (company_001_amazon) · Stage 1 · Run 2026-09-24
**AUDIT 3 (Numbers) — THIRD VERIFICATION.** Auditor: Level-3 Numbers Auditor (third pass).
Independent of the producers of the material audited: **yes** — this run wrote nothing in the corpus.
Files opened read-only: `stage_1.md` §P/§P.2/§R (plus §A/§B.1/§K/§S/§U for cross-references), the nine CSV
registers, `CORRECTIONS.md`, and the four repaired-stage logs
(`amazon_s1_number_repairs.md`, `amazon_s1_number_repairs2.md`, `amazon_s1_residual_sweep.md`,
`amazon_s1_residual_sweep2.md`).
**Authority used:** the restored filings only — original S-1 `acc. 0000891618-97-001309` (1997-03-24),
S-1/A No. 3 `…-000755` (1997-05-09), S-1/A No. 5 `…-000839` (1997-05-14), 10-K405 FY1997
`acc. 0000891020-98-000448` (1998-03-30). Every line quoted below was read out of the `.txt`, not out of a
repair log. Line numbers are the `grep -n` numbers of the restored files.

**Verdict: AUDIT 3 FAILS — 9 surviving defects, of which 1 is a false equation, 1 is a NEW transcription
drift created by the round-2 repair, 1 is an unfiled/underived input used as a live component, and 3 are
retired rulings still printed as live text in registers the audit depends on.** Every one of the nine
canonical values is nevertheless confirmed at a filing line, and none of the retired figures
(`+95.2%`, `$871,024`, `= $976,432` as a composition tie, `1,006,999`, `$0.1708`, unattributed
`~41–43%`, `$355,000` as the deficit, `~$21,000`) survives anywhere as a live value.

---

## 1. Results table

| Audit | Result | Items checked | Failures found | Actions taken | Residual risk |
|---|---|---|---|---|---|
| 1 Chronology | not run by this auditor (see §8) | — | — | — | — |
| 2 Sources | not run by this auditor (see §8) | — | — | — | — |
| **3 Numbers** | **FAIL** | 111 `quantitative.csv` rows + 70 §P rows + 22 §R rows; 6 protocol checks; 30 DERIVED/ESTIMATE/INFERENCE rows re-computed; d1–d30 re-run; 9 canonical values traced to filing lines; 9 registers parsed | **9** (§3, §4, §5, §6 below) | **None.** No corpus file edited; defects reported here only | `_parts/`, `research/`, `context_appendices.md`, `stage_1_claim_records.md`, `_MANIFEST.md` were read only where they cross-reference §P/§R; a fifth register pass has no mandate to touch them either |
| 4 Hindsight | not run by this auditor | — | — | — | — |
| 5 Adversarial | not run by this auditor | — | — | — | — |

### AUDIT 3 by check (protocol `AUDIT_PROTOCOLS.md` §AUDIT 3, checks 1–6)

| Check | Result | Basis of the verdict |
|---|---|---|
| 1 Basis (fiscal/calendar, net sales/GMV, audited/estimate, thousands/millions, as-of date) | **FAIL** | The calendar-year and ship-basis labels are **correct and provable** (§2.1–2.2); but a derived share count is labelled "unaffiliated", colliding with the filed unaffiliated count (§4 C-1), and one row's accession stamp contradicts its own cited lines (§4 C-4) |
| 2 Provenance / re-run the arithmetic | **FAIL** | 27 of 30 arithmetic claims re-ran clean (§2.3, §2.4); three did not: the false bridge (§3 F-1), the cent-digit drift (§3 F-2), the underived 2,613,000 (§3 F-3) |
| 3 Units | **PASS** | All money nominal USD, no inflation adjustment claimed; `P59` marks the quarterly series "(thousands)" against a dollar-total; per-share figures carry the 1997 split-restated basis and are kept off the pre-split 1,700,000 instrument basis |
| 4 Cross-foot | **FAIL** | §R agrees with §P and `quantitative.csv` on all 22 rows (§5.1); §P36 and §P.2 d14/CSV L66 disagree with each other (§5.2) |
| 5 Precision | **PASS** | No manufactured exactness survives: residual rendered ≈$976,000 (±$1,000), margin 38.7% with its 38.61–38.88% band, period 5.5–6.0 months, per-week a band not a point, both step-up conventions rendering +94.1%; the $24 gap is accounted for, not plugged (§2.4 proves the account) |
| 6 Contradiction register | **FAIL** | 42 conflict rows exist and U.29 is correctly split by accession, but U.8 and U.17 still carry superseded rulings as live text (§3 F-4, F-5) |

---

## 2. Canonical values — every one confirmed at a filing line

### 2.1 Net sales and the 1996 quarterly series
```
orig. l.3489   Net sales.................................  $    --          $    511       $ 15,746
orig. l.1435   Net sales grew from $511,000 in 1995 to $15.7 million in 1996
A5   l.1666    Net sales.........................  $   875     $ 2,230    $ 4,173    $ 8,468    $ 16,005
```
CONFIRMED. 1994 stub `$0` (filed `--`), FY1995 `$511,000`, FY1996 `$15,746,000`; 875 + 2,230 + 4,173 +
8,468 = **15,746** ✓. §P59 carries the series and labels it post-boundary. Cost of sales 409/12,287,
gross profit 102/3,459, opex 200/171/35 → 406, loss from operations (304) all read off l.3489–3500 ✓.
The 1994 column of the SFD prints Product development 38 / G&A 14 / total 52 / loss (52) ✓ (P08/P09 cite
the 10-K405, which repeats them: K405 Item 6 table, net loss 1994 `$(52)`).

### 2.2 Basis labels (protocol Check 1)
* **Calendar, not fiscal-shifted:** every audited period is captioned "YEAR ENDED DECEMBER 31" and the first
  is "JULY 5, 1994 (DATE OF INCEPTION) TO DECEMBER 31, 1994" (orig. l.3483–3486, l.343–346); K405 carries
  fiscal year 1997 ended December 31, 1997 (l.250). **No November–October year end appears in any of the
  four documents**, so the protocol's generic "Amazon's Nov–Oct fiscal year pre-1996" caution is *not*
  applicable here and §P's "FY = calendar year … except the 1994 stub of 179 days" is the right label.
* **Net sales, not GMV:** orig. l.1433–1435 "net of returns, as well as outbound shipping and handling
  charges" — the register's "ship-basis, incl. outbound S&H" tag is the filing's own basis; §R's GMV row
  is UNKNOWN with a reason.
* **Audited vs estimate vs company claim vs self-measured** kept separate: E&Y-audited lines, the IDC
  third-party estimate (`quantitative.csv` L84, orig. l.1774 "IDC … from $318 million in 1995"), the
  company's own press claims (P46/P47/P50), and its self-measured visits (orig. l.317 "approximately
  2,200 in December 1995 … (not 'hits')").
* **Filed in thousands:** `orig. l.3411 "(IN THOUSANDS, EXCEPT SHARE AND PER SHARE DATA)"`, balance sheet
  l.3469 `(IN THOUSANDS)`; §P's precision rule at l.867–870 states it, and L35's ±$1,000 band implements it.
* **Per-date headcounts, never averaged:** no cell in §P, §R or any register averages or reconciles 11,
  151, 158 or 256 (grep for averaged-headcount phrasings returns nothing but the explicit "not reconciled"
  instructions).

### 2.3 Accumulated deficit, share count, headcount
```
orig. l.3461   Accumulated deficit...................................     (248)     (6,025)       (6,025)
orig. l.3540   Net loss … 1994 .... (52)      l.3567 … 1995 .... (303)
orig. l.3555   Reclassification of accumulated deficit due to termination of S Corporation status .... (107) / 107
orig. l.3571   Balance at December 31, 1995 ... 14,555,244  1,075  150  -  -  (248)  977
orig. l.3455–3457  Issued and outstanding shares -- 14,555,244 and 15,900,237 at December 31, 1995 and 1996
orig. l.1340–1342  Total assets 76 / 1,084 / 8,271 ; Long-term obligations -- / -- / -- ; equity 8 / 977 / 3,401
A3   l.797    From December 31, 1995 to March 31, 1997, the Company expanded from 11 to 256 employees
A5   l.796    (identical sentence, No. 5)
orig. l.667    from January 1, 1996 to December 31, 1996, the Company expanded from 11 to 151 employees
orig. l.2364   As of December 31, 1996, the Company employed 151 full-time employees
K405 l.729     158 employees as of December 31, 1996 to 614 employees as of December 31, 1997
```
CONFIRMED. **52 + 303 − 107 = 248** ✓ and it is the filed line, not a reconstruction. Equity cross-foot
**1,075 + 150 − 248 = 977** ✓ against l.3457/l.3458/l.3461/l.3463. Share-count cross-foot
10,200,000 + 4,235,244 + 120,000 = **14,555,244** ✓ and 14,555,244 + 840,534 + 504,459 = 15,900,237 ✓.
The retired `$355,000` survives in exactly three forms, all correct: the relabelled `quantitative.csv` L55
("Sum of the two filed loss years (**NOT** the filed accumulated deficit…)", DERIVED), and the sentences
that retract it (`stage_1.md` l.551, l.635, l.1048, l.1071; `timeline.csv` r43; `validation.csv`; L54
notes). **No percentage is invented from 14,555,244** anywhere: P67, L86 and §R Capital each print the
prohibition, and no cell divides anything by it. **11 is filed at 1995-12-31** by both amendments and the
original's 1996-01-01 anchor is corroboration — COR-12's ruling is right and P42/L74/§R state it.
**`151` occurs 0 times in No. 3 and No. 5** (`grep -c "151 "` → 0, 0), so §P61's "151 occurs nowhere in
S-1/A No. 3 or No. 5" is true, and 151 vs 158 is a real same-date conflict correctly kept side by side.

### 2.4 The money round and the step-up
```
orig. l.2863–2864  In February 1995, the Company sold 582,528 shares … to Miguel A. Bezos at a price per share of $0.1717
orig. l.2864–2865  In July 1995, the Company sold 847,716 shares … to the Gise Family Trust at … $0.1717
orig. l.2872–2873  In December 1995, the Company sold 150,000 shares … to Tom A. Alberg
orig. l.4294–4296  On August 7, 1995, the registrant issued 42,000 shares … approximately $.1287 … or an aggregate of $5,408
orig. l.4300–4302  Between December 6, 1995 and May 16, 1996 … an aggregate of 3,021,000 shares … to 23 investors
                   for a consideration of approximately $.3333 per share, or an aggregate of $1,007,000
orig. l.3645       Proceeds from exercise of stock options, sale of stock, and advances … 60 | 1,272 | 231
orig. l.3535 / l.3546 / l.3556–3559 / l.3560–3562   advances 50 (1994) | 4,235,244 sh, 1,172, (50), 1,122 | 150 | options 120,000 sh at $—
orig. l.4280 / l.2848  10,200,000 founder shares, $10,000                orig. l.11452  "subscribes for 1,700,000 shares … Cadabra, Inc."
orig. l.3848            On November 23, 1996, the Company effected a 4-for-1 common stock split   (+ 3-for-2, l.4078)
orig. l.3797–3803       Computers 73 / software 8 / leaseholds 0 → 81; accum. dep. 24 → 57       orig. l.3734–3735 incurred advertising expense of $30,000
orig. l.3722            International sales were $198,000 and $5.1 million          orig. l.1438 "approximately 39%"
orig. l.4045–4046       Rental expense … for 1994, 1995, and 1996 was $2,000, $12,000, and $257,000
orig. l.2849–2851       interest-free loans … $15,000, $29,000 and $40,000 … fully repaid in August 1995, April 1995 and November 1995
A5   l.4665–4668        one director Alberg 150,000 + two founder-related 60,000 + 20 unaffiliated 2,811,000; "23 purchasers"
orig. l.985–988 / l.2919   ~43% Bezos + 10% family (42%/10% with over-allotment) ; 9,885,000 — 48.3% / 43.1%
A5   l.1055–1062 / l.3149  ~41% Bezos + 10% family (41%/10%) ; 9,885,000 — 47.4% / 41.4%
```
CONFIRMED, all nine:
* **+94.1%, not +95.2%:** `(0.3333 − 0.1717)/0.1717 = 0.9411765` → 94.12;
  `(1,007,000/3,021,000 = 0.333333… − 0.1717)/0.1717 = 0.9413706` → 94.14. Conventions differ by
  **0.0194 points**, so there is no ±1.1-point band. +95.2% requires a February price of **$0.170765**
  (≈$0.1708), filed nowhere; the filed February price is **$0.1717** (l.2864). P17, d6 and L30 all now
  read +94.1, and `95.2`/`0.1708` appear only inside the sentences that delete them.
* **The one-third leg:** 3,021,000 ÷ 3 = 1,007,000 exactly, so the ⅓ is the filing's own; and
  2,613,000 ÷ 3 = **871,000** exactly. **But 2,613,000 is not a filed number and no cell derives it** —
  see §4 C-1. `$871,024` survives only as the retracted back-solve (l.901–903, L35, l.556).
* **Composition ≈$976,000 band:** d8's `1,272,000 − 295,568 = 976,432` is correct and rendered
  ≈$976,000 (±$1,000) ✓. The composition 5,408 + 150,000 + 871,000 − 50,000 = **976,408** ✓, and the
  $24 gap really does decompose as claimed: exact CY1995 equity cash
  `245,572.8948 + 5,408 + 921,000 − 50,000 + 150,000 = 1,271,980.8948` (filed `1,272`, gap **$19.11**),
  named insiders on the exact ⅓ `245,572.8948 + 50,000 = 295,572.8948`, and
  `1,271,980.8948 − 295,572.8948 = 976,408.00` — **so "the two meet at $976,408 on exact prices" is
  arithmetically true**, and the residual $5 of the gap is the Alberg displayed-price convention.
  $976,432 appears now only as d8's own arithmetic or inside a "not an exact tie to" disclaimer; no target
  file presents it as the composition total.
* **The disclosed round** — 3,021,000 shares, 23 (original "investors" / No. 5 "purchasers"), $1,007,000,
  ≈$0.3333, window 1995-12-06 → 1996-05-16, decomposition 150,000 + 60,000 + 2,811,000 with
  1 + 2 + 20 = 23 ✓✓. **The aggregate governs and the filing says so on its face:** "approximately"
  qualifies *$.3333*, not $1,007,000 — so 3,021,000 × $0.3333 = $1,006,899.30 is an artifact of the
  display (undershoot $100.70), and L98's `1006899.30` with the division as the valid cross-check is
  right; `1,006,999` exists only inside its own correction sentence.
* **43% vs 41%** is a version discrepancy, both quoted above at their own accession; the unattributed
  `~41–43%` is gone from every live file (l.184 now names both accessions and notes E-59 cites No. 5).

---

## 3. Surviving drift — exact list, file + line

| # | Class | Site (absolute path + line) | What survives | Why it is a defect |
|---|---|---|---|---|
| **F-1** | Check 2 — false equation (**pre-existing, recheck F-2, never repaired by any of the three sweeps**) | `E:\founder's playbook\founders_playbook\01_companies\company_001_amazon\stage_1.md` **l.917** (§P.2 d14) | `52 − 232 − 52 + 1,228 = +944; 52 + 944 = $996` | The LHS is **996**, not 944; the filed statement (orig. l.3633–3649) prints net increase **944** = −232 − 52 + 1,228 and then 52 + 944 = 996. As written the bridge double-counts the opening 52 |
| **F-2** | Check 2/5 — **NEW drift introduced by the round-2 repair** | `…\company_001_amazon\quantitative.csv` **line 112** (`derived_arithmetic`) | `511,000 ÷ (5.5 × 4.345 = 23.90 weeks) = 21,382.98 → $21,383` | 511,000 ÷ 23.8975 = **21,382.9899**, i.e. 21,382.9**9**. The log that created the row (`amazon_s1_number_repairs2.md` item 2) prints `21,382.99`; the copy into the register lost the last digit. Truncated instead of rounded, in a field whose whole purpose is to be re-runnable |
| **F-3** | Check 1/2 — **unfiled, underived input presented as a disclosed component** | `…\stage_1.md` **l.899–900** (d8a), **l.811** (P20), **l.556** (§K), **l.1100** (§S), **l.1406–1407** (§U.8), **l.1072** (§R Capital); `…\quantitative.csv` **line 35** (notes); also `data_gaps.csv` r11, `context_appendices.md` l.596 | `2,613,000` shares, cited to `orig. l.4301–4302`, called "unaffiliated program shares" | l.4301–4302 contains 3,021,000 / $1,007,000 / $.3333 — **not 2,613,000**. The figure is nowhere derived in the corpus; it is `2,763,000 − 150,000` from the d25 chain that `quantitative.csv` **line 99** holds at **UNKNOWN, "RECORDED BUT NOT ADOPTED"** for three stated reasons (issuance ≠ subscription; assumes no 1995 sale outside the four Item 5 items; COR-10). And "unaffiliated" collides with the filed unaffiliated count **2,811,000** (A5 l.4665–4668, quoted at §S l.1099). $871,000 is a true third of 2,613,000 — but its input silently adopts what the register elsewhere refuses to adopt |
| **F-4** | Check 6 — withdrawn explanation live in the conflict register | `…\conflicts.csv` **line 9** (row U.8, `residual_uncertainty`) | "The identity and count of the residual roughly **$0.9 million** of purchasers, **option-exercise proceeds being commingled with issuance proceeds and inseparable**" | The commingling explanation was withdrawn after the audited equity statement proved 1995 option exercises at **$—** (orig. l.3560–3562) — §P.2 d8a l.894–896, §S l.1100, `data_gaps.csv` r11, `quantitative.csv` L35 all say so. `residual_sweep2.md` §3 certified that `conflicts.csv` "needed no closing"; that certification is false for this cell. "roughly $0.9 million" is also not the canonical ≈$976,000 (±$1,000) |
| **F-5** | Check 1/6 — superseded headcount ruling live in the conflict register | `…\conflicts.csv` **line 18** (row U.17, `best_supported_interpretation` + `residual_uncertainty`) | "Print **'11 employees (per the filing: at 1996-01-01)' in sections P and R**"; "**no filing gives any 1994 or 1995 headcount at all**, so the Stage-1 end-state number is genuinely UNKNOWN" | Both were superseded by **COR-12** and are refuted by the documents (A3 l.797 / A5 l.796 file the 11 **at 1995-12-31**). §P42 (l.833) and §P61 (l.861) send the reader to U.17, which contradicts them; §R Employees (l.1062) prints the opposite of what U.17 instructs. No sweep touched r18 |
| **F-6** | Check 1 — accession stamp | `…\quantitative.csv` **line 30** (`source_date` = `1997-05-14`) | its own `derived_arithmetic` cites "orig. l.4301-4302" and `notes` cite "orig. l.2864" | The row's evidence is the original (1997-03-24); stamping the amendment's date on original-only line citations is the COR-01 error class run backwards. Every other repaired row (L22, L24, L25, L26, L74) carries both dates or the right one |
| **F-7** | Check 2 / §13 schema | `…\quantitative.csv` **lines 26, 54, 70, 73, 86, 96 (FACT), 99 (UNKNOWN)** | `derived_arithmetic` populated on 7 non-DERIVED/ESTIMATE/INFERENCE rows | The brief's rule "present **exactly** on DERIVED/ESTIMATE rows" fails: the field is not a reliable "this value is calculated" flag. Mitigation verified: each cell is a cross-foot of a filed line or an explicit anti-derivation note (L26 `42,000 × $0.1287 = $5,405.40; the FILED aggregate is $5,408`; L99 records the rejected chain), and no value in those 7 rows is derived-but-labelled-fact — L54 248,000, L70 17,000, L86 14,555,244, L96 3,021,000 are all filed |
| **F-8** | §13 schema | `…\quantitative.csv` **line 102** (`value` = `151 / 158 / 256`, `date` = `1996-12-31 (151/158) and 1997-03-31 (256)`) and **line 103** (`value` = `≈180,000 accounts; >$16,000,000`) | multiple metrics / three as-of dates packed into one `value` cell | Not a wrong-column error and not a Stage-1 breach (both `stage2-consequence`), but a query reading `value` gets two dates' incompatible restatements in one field; the 151-vs-158 conflict then has no machine-readable row |
| **F-9** | Out-of-target consistency witness | `…\stage_1_claim_records.md` **line 446** (record P10) | "Inventory is **DERIVED** from cumulative movements … **≈17,000**" | D15 was certified "CLOSED as a three-file item" (§P39 / L70 / `validation.csv` r20 all read **FACT (audited)**); the claim record still carries the retired class and the retired `≈`. Reported, not repaired — the claim appendix is not in this run's write scope and no auditor may repair what it audits |

**Also verified as NOT surviving (the retired-value hunt):** `+95.2` as a live value (0), `$871,024` outside
retractions (0), `= $976,432` as a composition tie (0), `1,006,999` outside its correction sentence (0),
`$0.1708` outside the deletion sentence (0), `~41–43%` unattributed (0), `~$21,000` as the figure (0),
`$355,000` as the deficit (0), averaged headcount (0), `256` or `151` inside a Stage-1 cell
(0 — they appear only inside dated verbatim quotes or the post-boundary block).

---

## 4. Programmatic CSV pass (nine registers) and the proof that the detector can fail

Parsed with Python `csv`, UTF-8, all nine files in
`E:\founder's playbook\founders_playbook\01_companies\company_001_amazon\`:

| Register | rows (data) | cols | field-count mismatches | unexpected empties | `QUOTE_MINIMAL` round-trip byte-identical | CRLF / BOM |
|---|---|---|---|---|---|---|
| `quantitative.csv` | 112 (111) | 12 | **0** (widths `{12}`) | **0** (74 legitimately empty `derived_arithmetic`) | **True** | 0 / none |
| `conflicts.csv` | 43 (42) | 15 | 0 | 0 | True | 0 |
| `validation.csv` | 30 (29) | 11 | 0 | 0 | True | 0 |
| `data_gaps.csv` | 24 (23) | 8 | 0 | 0 | True | 0 |
| `sources.csv` | 103 (102) | 18 | 0 | 0 | True | 0 |
| `timeline.csv` | 58 (57) | 11 | 0 | 0 | True | 0 |
| `failures.csv` | 34 (33) | 11 | 0 | 0 | True | 0 |
| `decisions.csv` | 16 (15) | 15 | 0 | 0 | True | 0 |
| `channels.csv` | 16 (15) | 11 | 0 | 0 | True | 0 |

* **`derived_arithmetic`:** all **30** DERIVED/ESTIMATE/INFERENCE rows populated (0 missing);
  **74** empty cells fall entirely on the 81 non-calculated rows; the 7 exceptions are F-7.
* **Wrong-column tests:** no money figure in any `confidence`/`importance` cell; every `evidence_class`
  parses as a class and every `confidence` as a confidence; no retired value in any `value` cell.
* **Boundary test:** `stage='stage1' AND date ∈ 1996/1997` → **0 rows**; the 6 rows dated `1995-12-06`
  all carry `stage='stage2-consequence'` (the straddling program); `quantitative.csv` post-boundary tokens
  appear only in stage2-consequence rows, and in §P/§R every 1996–97 token sits either in the
  "Post-boundary … NOT Stage-1 metrics" block (P55–P63) or inside an explicit "post-boundary"/"out of
  stage"/dated label. §P ID completeness: P01–P70 present, **0 duplicates, 0 gaps**.
* **Detector proof (plant test, in a throwaway copy — no corpus file was created, edited or moved):**
  `%TEMP%\quantitative_PLANT_badcopy.csv` was planted with a 5-field row, `871,024` in a `value` cell,
  `46,455` in `confidence`, an empty `metric`, and arithmetic stripped from a DERIVED row. The same
  script returns **FIELD-COUNT (5 fields at line 113), RETIRED-VALUE-IN-CELL L35, MONEY-IN-WRONG-COL L76,
  UNEXPECTED-EMPTY L88, DERIV-MISSING** on the copy, and **0 findings of those classes on the real file**
  (only the 7 F-7 flags). A second plant on `L30` proved the `DERIV-MISSING` branch fires. The copy was
  deleted afterwards; the real file's size and mtime are unchanged. **A test that cannot fail is not a
  test — this one failed on command.**
* Detector calibration noted for honesty: a generic severity/class regex flags `Very High` in
  `data_gaps.csv` (r12/13/17) and source-class vocabulary in `sources.csv`/`timeline.csv`/`failures.csv`
  (`FOUNDER-ADJACENT CLAIM`, `COMPANY SELF-REPORT`, `RECOLLECTION`). Those are the detector's vocabulary,
  not corpus defects, and are **not** counted among F-1…F-9.

---

## 5. §R cross-foot against §P and `quantitative.csv`

**5.1 Where it agrees (all 22 §R variables checked, none silently contradicted).** Employees 11 = P42 =
L74 = `validation.csv` r7; Revenue $511,000 + 5.5–6.0 band = P23/P22 = L39/L38; Users ≈2,200 = P43 = L75;
Margins 19.96/20.0% · (304,000) · 39.1% · (248,000) = P25/P29/P28/P68 = L42/L49/L44/L54; Capital
$1,272,000 = P18 = L33 with the audited decomposition 1,122 + 150 + 0 ✓; $295,568 (±$5) = P19 = L34;
≈$976,000 (±$1,000) = P20 = L35; 14,555,244 = P67 = L86; $44,000 repaid = P11 = L19; $0 long-term =
P41 = L72; $996,000 = P35 = L62; $1,007,000 / 23 = P51/P69 = L95–L100, all as stage2-consequence;
Valuation's three price points = P13/P16/P66; Weaknesses' ≈$19,400–$21,400 = d30 = **L112, which now
exists** (so the row-112 citation is true, closing the F-3/RD-025 half-application); Geography's $0
leaseholds and Technology's $73,000 + $8,000 = P37 = L67; Supply's 59% flagged FY1996 = L104; Customers'
≈180,000 flagged 1996-12-31 = L103.

**5.2 Where it fails.** `§R`/`§P36` vs `§P.2 d14` + `quantitative.csv` L66 — **two different values for the
same bridge** (996,000 vs the false "= +944"), which is exactly the protocol's "a snapshot that disagrees
with the last metric in the same section is a defect" (F-1).

---

## 6. Context tested, not accepted (the three repair logs and COR-01…COR-14)

| Claim in the logs | Independent result |
|---|---|
| "All six recheck items landed; F-2/F-5/F-6/F-7 left as found" | **F-2 is still open** (F-1 above) and was never scheduled by any later pass — `residual_sweep` and `residual_sweep2` enumerate only the 871,024/976,432/95.2/41% families |
| `residual_sweep2` §3: "Neither [`quantitative.csv`, `conflicts.csv`] was written by this pass — **nothing in them needed closing**" | **False for `conflicts.csv`**: r9 (U.8) carries the withdrawn option-cash explanation and a $0.9M residual; r18 (U.17) carries the superseded 1996-01-01 instruction |
| `residual_sweep2` §1: canonical step-up "94.118 displayed / 94.137 exact ⅓" | Confirmed to 4 dp: 0.9411765 / 0.9413706. P17's "94.12 / 94.14" are those numbers rounded to 2 dp ✓ |
| `residual_sweep2` §1: "$24 gap accounted for (≈$19 filed-thousands + $5 Alberg), not plugged" | Confirmed by exact recomputation: 1,271,980.8948 − 295,572.8948 = 976,408.00 exactly; 1,272,000 − 1,271,980.89 = 19.11 ✓ |
| `residual_sweep2` §2 row 4 / `NUMBER_DEFECTS` claim "$976,432 arithmetic itself (1,272,000 − 295,568) stands" | Stands ✓ |
| `residual_sweep2` §5 open list (`_parts/s1_claims_KU.md` l.37/l.153, `U_CONCORDANCE.md` l.60, `MASTER_RESEARCH_LOG.md` l.247, `_MANIFEST.md`) | All four now sit under appended `SUPERSEDED 2026-09-24` markers or per-accession text (commit `fdb1095`); they remain working volumes, not clean copies, and F-9 is a fifth such site nobody named |
| COR-02 (Cadabra / sole stockholder / 1,700,000 in the original only) | Confirmed by count: 1 / 2 / 3 occurrences in the original, **0 / 0 / 0** in S-1/A No. 5 |
| COR-10 (aggregate governs; program must not be shown as a Stage-1-only raise) | Confirmed at l.4300–4302; honored at P51/P70/L99/§R Capital — **except** via F-3, which imports the not-adopted in-window share split into a Stage-1 money composition |
| COR-12 (11 filed at 1995-12-31) | Confirmed at A3 l.797 / A5 l.796 — but contradicted inside `conflicts.csv` r18 (F-5) |

---

## 7. Claims cut or downgraded
**None.** An auditor never edits what it audits. Every finding above is a report to its owner; no
`UNKNOWN` was upgraded and no figure was altered by this run.

## 8. Research debt opened by this audit
| RD id | Section | Debt | Assigned | Status |
|---|---|---|---|---|
| RD-029 | §P.2 d14 / `quantitative.csv` L66 | Re-write the 1995 cash bridge in the filed form (−232 − 52 + 1,228 = +944; 52 + 944 = 996). Recheck **F-2**, unscheduled through three sweeps | numbers-repair pass (never §P/§R author) | OPEN — High for a derived-arithmetic field |
| RD-030 | `quantitative.csv` L112 | Correct `21,382.98` → `21,382.99`; re-render d30's band the same way | round-2 author's successor | OPEN — the new drift this pass was hunting for |
| RD-031 | d8a / P20 / §K / §S / §U.8 / §R Capital / L35 / `data_gaps.csv` r11 | Print 2,613,000's derivation and its dependency on the non-adopted d25, or restate the leg against the **filed** 2,811,000 and mark the composition UNKNOWN-by-date; stop calling 2,613,000 "unaffiliated" while §S l.1099 calls 2,811,000 that | numbers + money-family owner | OPEN — High: it is the only canonical value whose input is not filed |
| RD-032 | `conflicts.csv` r9 (U.8), r18 (U.17) | Strike the withdrawn commingled-option-proceeds explanation and the superseded "print 11 at 1996-01-01" instruction; restate the residual as ≈$976,000 (±$1,000); register the 151-vs-158 conflict as its own machine-readable row | conflict-register owner | OPEN — Check 6 |
| RD-033 | `quantitative.csv` schema (L26/54/70/73/86/96/99; L102/L103) | Decide and document whether `derived_arithmetic` may hold corroboration, and split multi-value `value` cells | schema owner (method §13) | OPEN — Low |
| RD-034 | `quantitative.csv` L30 | Add `1997-03-24` to `source_date`, or re-cite the No. 5 lines | numbers-repair pass | OPEN — Low |
| RD-035 | `stage_1_claim_records.md` P10 | Carry D15's FACT (audited) reclassification into the claim record | claim-appendix owner | OPEN — Low, out of this file's scope |

## 9. Sign-off
Stage status: RECONSTRUCTION → ADVERSARIAL REVIEW → QA → **COMPLETE (BLOCKED)**.
AUDIT 3 = **FAIL** on checks 1, 2, 4 and 6; PASS on 3 and 5. Nine defects (F-1…F-9), three of them
material to a number a reader would take away (the false bridge, the underived 2,613,000, and the two
registers still printing retired rulings). **All nine canonical values are confirmed at a filing line of
the four restored documents**, and every value the three sweeps retired stays retired — so the repairs
landed; they were just not finished, and two of the three passes' self-certifications
(`residual_sweep2` §3 on `conflicts.csv`; the "all repairs landed" handoff line) do not survive an
independent read of the registers they declared clean. Per spec §11 this failure is answered by
re-deriving from the filings (RD-029…RD-032), not by a disclaimer. This auditor edited nothing.
