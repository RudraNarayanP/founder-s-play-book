# Amazon Stage 1 — AUDIT 3 (Numbers) REPAIR LOG
Level-2 Company Lead (numbers repair) · run 2026-09-23 · register: `_parts/NUMBER_DEFECTS.md` (31 rows:
9 HIGH · 15 MEDIUM · 7 LOW) · audit sheet: `03_quality_control/amazon_s1_audit3_numbers.md`

Every `should_be` was verified against the filing line in `sources/` **before** it was written. Where the register's
proposed value or arithmetic disagreed with the document, **the document won** and the disagreement is recorded in
§C. No row was deleted; nothing in `_parts/` was written; `stage_1_claim_records.md`, `adversarial_review.md`,
`_MANIFEST.md`, `CORRECTIONS.md` and `sources/` were not touched.

Primaries used: S-1 (original) acc. 0000891618-97-001309, 1997-03-24 ("orig."); S-1/A No. 3 acc.
0000891020-97-000755 ("A3"); S-1/A No. 5 acc. 0000891020-97-000839, 1997-05-14 ("A5"); 10-K405 FY1997 acc.
0000891020-98-000448, 1998-03-30.

Line numbers in `stage_1.md` are as read at repair time; the register's own warning held — §P/§P.2/§R shifted
under this edit, so every repair was anchored on the row ID (`P32`, `d7`, `§R "Capital"`), not the line.

---

## A. Row-by-row disposition (register order, D01–D31)

| # | Sev | Register target | Disposition | What was written / refused |
|---|---|---|---|---|
| D01 | HIGH | `quantitative.csv` r93 (now r97) `1006999` | **FIXED** | Value → `1006899.30`. `derived_arithmetic` re-expressed as **division**: `3,021,000 × $0.3333 = $1,006,899.30`, and the valid check is `$1,007,000 ÷ 3,021,000 = $0.33333…`. Notes state that the $100.70 shortfall is an artifact of the four-decimal display, that the filed aggregate governs, and that a row deriving $1,007,000 *from* $0.3333 runs the rounding backwards (COR-10 as corrected). The register's alternative ("or delete the row") was **not** taken — the row is kept because it is now the place the rounding direction is explained. Cited orig. l.4300–4302. |
| D02 | HIGH | `quantitative.csv` r22 (now r21) `100019` | **FIXED** | Value → `100020`; arithmetic → `582,528 × $0.1717 = $100,020.0576 → $100,020.06`. Source re-keyed to **both** versions (orig. l.2863–2864 **and** A5 l.3093–3094), source_date `1997-03-24 / 1997-05-14`. |
| D03 | HIGH | `stage_1.md` §P.2 d4 (+ d5 cent) | **FIXED** | d4 → `$100,020.0576 → $100,020.06`, flagged as wrong by exactly $1.00 before. d5 → `$145,552.8372 → $145,552.84` (the old `.83` was a truncation). CSV Gise row (r23) and §P15 updated to match so the §P ↔ CSV cross-foot holds. |
| D04 | HIGH | `stage_1.md` §K "FY1995 result" | **FIXED** | `cumulative $(355,000) DERIVED` → **accumulated deficit $(248,000), FACT (audited)**, cited to the balance sheet line itself (orig. l.3461) plus the equity-statement roll-forward. The $355,000 survives in the same cell **only** as "the sum of the two loss years, before the $107,000 reclass", with `52 + 303 − 107 = 248` printed and pointed at d26. |
| D05 | HIGH | `stage_1.md` §M bullet 2 | **FIXED** | Same substitution. §M's **narrative was re-read at the smaller number and still holds**, and was rewritten so it does not depend on $355,000 being the deficit: the signal is "the residue of a $304,000 operating loss and $303,000 of net loss inside a single trading year", and the note adds that $248,000 is not the cash burned either, because $107,000 passed through to the founder personally. |
| D06 | HIGH | `quantitative.csv` r52 | **FIXED (split into two rows)** | New row `248000 / Accumulated deficit at 1995-12-31 (audited) / FACT (audited)` with the roll-forward visible; the old row retained but **relabelled** `Sum of the two filed loss years (NOT the filed accumulated deficit, NOT cumulative losses since inception)`, evidence_class `DERIVED`, arithmetic `52 + 303 = 355; 355 − 107 = 248`. Also propagated to every other site that carried the wrong figure: `stage_1.md` §A, §K Year-end, §L, §M, §P68 (new), §Q endpoint, §R Margins/Risks/Capital, `failures.csv` r7, `timeline.csv` r42. |
| D07 | HIGH | `failures.csv` r7 notes | **FIXED** | Now states the audited $248,000 with its lines, explains the $107,000 reclass as the reason the loss years do not sum to it, and keeps the row's failure signal intact. |
| D08 | HIGH | `quantitative.csv` r83 | **FIXED (null deleted + new row)** | The false assertion "no share count" is **deleted**. New row: `1995-12-31 / Common shares issued and outstanding / 14555244 / shares (restated basis) / S-1 (original) BALANCE SHEET l.3455–3457 (and equity-statement balance l.3571) / FACT (audited) / High`, with the cross-foot `10,200,000 + 4,235,244 + 120,000 = 14,555,244`. Notes state explicitly **what it permits** (a boundary share count; a per-share basis for the $(0.02) loss per share) and **what it does not** (no ownership percentage for any 1995 holder — it is the total and no per-holder 1995-12-31 table is filed; not to be mixed with the pre-split 1,700,000 instrument basis). 15,900,237 and 17,008,158 named as post-boundary. The valuation row is retained with `UNKNOWN` and its premise corrected: the null is now a conclusion, not a missing input. Mirrored at §P67 (new) and §P52. |
| D09 | HIGH | `quantitative.csv` r28 + missing August row | **FIXED** | Notes replaced with the three-price statement (`$0.1717 Feb 9 / $0.1287 Aug 7 / $0.3333 Dec`). **Two rows entered**: 42,000 shares (FACT) and the **filed aggregate $5,408** — with the warning that `42,000 × $0.1287 = $5,405.40` and the aggregate governs (d27). Cited orig. Item 5 ¶3 l.4294–4296; A5 l.4656–4658 ("who is an employee"). Mirrored at §P66, §K "First priced tranche", §Q (new 1995-08-07 row), `timeline.csv` (new row), §U.8. The Alberg option row and the step-up row were re-worded so "$0.6666 = the second internal price point" and "two private sales at two prices" no longer survive anywhere. |
| D10 | MEDIUM | `stage_1.md` §K "The 23-purchaser program, as filed" in-window split | **REFUSED — held UNKNOWN (register proposed DERIVED ≈$921,000)** | Per the Company Lead's ruling for this repair the split **stays `UNKNOWN`**. The full derivation is nonetheless recorded and labelled, in three places, as a **candidate that was considered and not adopted**: new §P.2 **d25**, a new fenced `stage2-consequence` row in `quantitative.csv` whose value cell is `UNKNOWN`, and §K itself. Reasons written into d25: (i) the equity statement counts shares **issued in a cash year**, Item 5 dates the program by **subscription** — different objects, and the `Advances 150 / (50)` lines prove consideration and issuance did not coincide; (ii) the subtraction assumes no 1995 sale outside the four Item 5 items, a negative the filing never states; (iii) COR-10 forbids presenting the program as a Stage-1-only raise, and ≈$921,000 in a Stage-1 money cell is that presentation. **Checked that no file states it as a Stage-1 raise**: §K, §P51, §P70, §R Capital, `timeline.csv`, `data_gaps.csv`, `quantitative.csv` all fence it and none carries $921,000 in a value cell. |
| D11 | MEDIUM | `stage_1.md` §P51 and §R "Capital" boundary qualifier | **PARTLY REFUSED** | "straddles the boundary" kept and strengthened; the UNKNOWN is kept (see D10) and now points at d25. The one substantive item **adopted** is the register's other half: Alberg's 150,000 shares ($49,995–$50,000) are named as the **only individually dated in-window slice** of the program, in §P51, §K, d25 and the CSV. |
| D12 | MEDIUM | `quantitative.csv` r91/r92 decomposition | **FIXED** | New `stage2-consequence` row: **Alberg 150,000 + two founder-related 60,000 + 20 unaffiliated 2,811,000 = 3,021,000; 1 + 2 + 20 = 23**, cross-footing both ways (d29), cited to **A5 l.4663–4668 only** and explicitly marked *post-original-only / amendment-stage addition, not corroboration*, with source_date `1997-05-14 (No. 5 only)`. Mirrored at §P69 (new). |
| D13 | MEDIUM | `quantitative.csv` r33 residual | **FIXED, WITH THE REGISTER'S OWN ARITHMETIC CORRECTED** | Value → `976000`, rendered **≈$976,000 (±$1,000)**. "Upper bound … absorbs commingled option-exercise proceeds" deleted: the audited equity statement prices 1995 option exercises at **$—** (orig. l.3560–3562). The register's replacement decomposition **did not foot** — see §C(2). Corrected to include the −$50,000 term. |
| D14 | MEDIUM | `stage_1.md` §P20 + §P.2 d8 | **FIXED** | Same precision and composition, with the new **d8a** arithmetic line; `quantitative.csv` $1,272,000 row, §A, §K Reconciliation, §K Equity-cash row, §S, §U.8, `data_gaps.csv` r11 and `validation.csv` wording all brought to the same decomposition so the withdrawn "option cash" excuse does not survive in any file. |
| D15 | MEDIUM | `quantitative.csv` r67 (+ validation r20, §P39) inventory | **FIXED** | **`17000` as FACT (audited)**, source = the balance-sheet line itself (orig. l.3429 "Inventories … 17"), `≈` removed, cash-flow movement demoted to corroboration, and only the 1994 $0 opening left as an inference from that column's "—". Added the balance-sheet cross-foot (996 + 17 + 14 = 1,027; + 57 = 1,084). Echoes cleared at §A, §G.1, §G.4, §K Year-end, §Q endpoint, §R, §P.2 d16, `timeline.csv` r42, **and §U.10's "RESIDUAL UNCERTAINTY"**, which asserted the opposite ("not lifted from a balance-sheet line") and is now corrected in place. |
| D16 | MEDIUM | `quantitative.csv` r7 / `timeline.csv` r11 / §Q option plan | **FIXED** | Adoption date vs reserve-as-stated separated: the 4,800,000 is labelled **1997 split-restated**, with the foot `3,052,974 + 110,640 + 1,636,386 = 4,800,000` (orig. l.2707–2711) and the 1994 equivalent (÷6 = 800,000) flagged as **never printed**. "Floor strike" withdrawn in all three carriers plus `quantitative.csv` r20 and `validation.csv` r13: the filing gives only the **observed** 1997-02-28 range $0.1717–$4.00, and director grants are separately "not less than the fair market value" (l.3874). |
| D17 | MEDIUM | `quantitative.csv` r66 capex | **FIXED (labelled, not deleted)** | Metric now `Cumulative Stage-1 capital expenditure, CASH-PAID basis`; the $1,000 gap to the accrual $81,000 is explained as a **basis difference** (unpaid additions and/or rounding in thousands) that is **not reconcilable on the filed record**, with no invented plug. Register's alternative (drop r66) rejected: the cash-paid number is the one the burn narrative uses. Added as §P.2 d15a and echoed in §K Year-end, §Q endpoint, §R Unknowns. |
| D18 | MEDIUM | r36 + §P22 + `decisions.csv` r12 trading period | **FIXED with ONE stated convention** | New **§P.2 d24** is the single source of truth: filed month "July 1995", day UNKNOWN, therefore **5.5–6.0 months (184 days = 6.0 months / 26.3 weeks at the early end; ≈5.5 / ≈23.9 weeks at the mid-July end)** with the arithmetic shown. CSV value → `5.5-6.0`; §P22 → the band; `decisions.csv` r12 → the band (its "~26-week" is now the band's other end); the five §R/§A/§D/§K/§N/§U "≈5.5 months" and "~26 weeks" mentions converted to the band with a pointer to d24. |
| D19 | MEDIUM | §R "Weaknesses" ~$21,000 per trading week | **FIXED as a band, not a point** | Register offered `21,383` **or** `19,440` and said "state which convention"; neither single figure was adopted, because choosing one silently would repeat the D18 error. New **§P.2 d30** shows both and the row now reads **≈$19,400–$21,400 per trading week**; §U.9's "about $21,000 per week" and the "twenty-six weeks" phrase updated to match. |
| D20 | MEDIUM | 38.75% → ≈38.7% (§P33, r55, `validation.csv` r6) | **FIXED** | All three carriers → `38.7` / `≈38.7%`, with exact `38.7476%`, the ±500-per-thousand band `38.61–38.88%`, the MD&A's "approximately 39%" as the source's own precision, and the independent 1996 check (5.1 ÷ 15.746 = 32.4% → "≈33%"). Also cleared at §D.2 (two sites) and §L. |
| D21 | MEDIUM | `validation.csv` r26–r28 stage | **FIXED** | `stage1` → `stage2-consequence` for all three (180,000 accounts at 1996-12-31; >40% of orders at 1997-03; $15,746,000 for 1996), with a note that the **field** is the fence a query reads and prose was not one. This was the only place a post-boundary value sat in a Stage-1 field; the 15 `stage2-consequence` rows of `quantitative.csv` were re-tested and are correctly fenced. |
| D22 | MEDIUM | `timeline.csv` r39 price-point count | **FIXED** | "the second and third internal price points" → "the THIRD and FOURTH priced points of Stage 1 (Feb $0.1717, Aug $0.1287, Dec $0.3333, $0.6666 for the grants)", with the reason the count changed. |
| D23 | MEDIUM | §P.2 d7 inverted rounding note | **FIXED** | `100,020.06 + 145,552.84 + 49,995 = $295,567.89 → $295,568`, and the note now says plainly that $295,568 is the accurate total and $295,567 was the artifact of the bad d4 product. Added the convention sentence: on the filing's exact ⅓ for Alberg the total is $295,572.89, so **±$5 is the only honest precision**. Carried into `quantitative.csv` r32 (now r33), §K Insider money, §P19. |
| D24 | MEDIUM | `sources.csv` S0804 | **FIXED by the register's first option** | The $32m / 340,000 accounts / 80,000 visits / Time figures are **re-keyed to A3 l.334–341 and A5 l.336–341**, both on disk, quoted verbatim and dated to March-1997 with the supersession of the December-1996 trio stated. The row is **not deleted** (lineage stays visible) and the 424B1 remains "restoration pending"; evidence_class and confidence downgraded for the unverifiable accession. Verified by search that **no** Stage-1 row in any CSV cites S0804. |
| D25 | LOW | `quantitative.csv` r81 IDC date | **FIXED** | `1995-07-01` → `1995 (whole year)`, matching r80's own base label, source_date corrected to `1997-03-24`, and the numerator/denominator basis mismatch (ship-basis revenue incl. S&H over IDC's undefined Web total) recorded so this is read as scale, not market share. Same warning added at §H and §P49. |
| D26 | LOW | `quantitative.csv` r70 AP line | **FIXED** | "accrued **liabilities**" → "accrued **expenses**" (verified at orig. l.3633–3634 **and** A5 l.3919–3920, 1995 = 83 in both); the hedge "not re-verified in this register" is closed; confidence stays Medium on the register's own convention; the balance-sheet 99 + 8 = 107 → 920 working-capital tie added. |
| D27 | LOW | §P32 advertising | **FIXED** | "Advertising expense **incurred**", quoting Note 1 l.3734–3736 and stating that incurred ≠ expensed is a real basis word. §A's list updated to match. |
| D28 | LOW | §P.2 d3 day count | **FIXED** | 179 kept, convention stated: the sum **excludes** 5 July; the inclusive count is 180; immaterial to the no-annualisation point, which holds either way. |
| D29 | LOW | §P.2 d6/d9/d11/d17/d18/d19 rendered precision | **FIXED** | A precision rule is now printed at the head of §P.2: with inputs filed in thousands a ratio renders to one decimal, and the exact product stays visible so the d-chain still cross-foots. Applied: d9 **≈20.0%** + the MD&A's own "approximately 20%"; d11 **≈$0.59 (one decimal $0.6)**; d17 **≈3.3%**; d18 **≈$46,000/person**; d19 **≈0.16%**; d6 retains +94.1% **with the +95.2% sensitivity on the exact ⅓** stated. §P25/P31/P40/P44/P49 and §R Margins carry the same rendering. `quantitative.csv` value cells keep the two-decimal exacts, since the register named only `stage_1.md` here and changing both would have broken nothing but added churn. |
| D30 | LOW | §R "Founders" CEO-date citation | **FIXED** | The title sequence is now cited to the **10-K405 FY1997 Item 10 officer table** (bios at l.960–972; S0805 already carries "CEO only from May 1996"), with an explicit note that the S-1's Certain Transactions sentence calling him "the President, Chief Executive Officer and Chairman" while describing the July 1994 purchase (orig. l.2847–2849) is the filing's **present-tense style as of 1997, not a 1994 title claim** — so the two are not a conflict. |
| D31 | LOW | `quantitative.csv` r4 vs §P03 | **FIXED** | CSV now cites **both** versions for the 10,200,000 (orig. Certain Transactions l.2848 **and** Item 5 ¶1 l.4280; A5 l.3078/l.4642), source_date `1997-03-24 / 1997-05-14`, with the giving-effect caveat: the original states it for a three-for-two split "**to be effected** prior to the closing of the offering" (l.4276–4277), so the restated count is a 1997 presentation, not a 1994 one. |

**In passing (not a register row, briefed separately):** `context_appendices.md` carried the **stale `[COR-03]`
employee note** — "headcount per the filing is the **1996-01-01** figure [COR-03]". Replaced with **COR-12's
supersession wording**: the 11 is **filed at 1995-12-31** in S-1/A No. 3 (l.797) and No. 5 (l.796), the original
S-1's 1996-01-01 phrasing (l.667) is corroboration of the same population rather than a competing date, and
151 (1996-12-31) and 256 (1997-03-31) are different dates and not a conflict. The same row's "~5.5 months" was
converted to the d24 band. Three further `context_appendices.md` cells that still carried the superseded
$976,432, the uncaveated $295,568, and the straddling-program UNKNOWN were brought into line.

---

## B. Sites cleared per defect (grep-verified after editing)

`cumulative $(355,000)` / `Cumulative losses since inception` — 0 live assertions (only the relabelled
sum-of-loss-years rows and the correction notes); `100,019` / `100019` — 0; `1,006,999` / `1006999` — 0;
`38.75` — 0; `no share count` — 0; `floor strike` — 0 (only its withdrawal is mentioned); `≈976,432` as an
asserted value — 0; `~$21,000 per` as a point figure — 0; `$295,567` as a total — 0; `second and third internal
price points` — 0; `Advertising expense` without "incurred" — 0. Every remaining occurrence of a retired string is
inside a "was X, now Y" correction note, which is deliberate: the trail must stay visible.

---

## C. Where the register's proposed value or arithmetic disagreed with the document

1. **D10 / D11 — the ≈$921,000 in-window split (the material disagreement).** The register and the audit sheet
   both propose replacing `UNKNOWN` with `DERIVED ≈$921,000 / ≈$86,000`. **Refused on this repair, on the Company
   Lead's explicit instruction, and the figure is held `UNKNOWN`** with the derivation recorded as a candidate and
   the refusal reasons on the face of the record (d25, the CSV UNKNOWN row, §K, §P51, §P70, §R Capital,
   `data_gaps.csv`, `timeline.csv`). The arithmetic itself was verified and does tie — but see (2) and (3).
2. **D13 — the register's own residual decomposition does not foot.** It proposes
   `$5,408 + $150,000 + ≈$871,000` as the composition of a **$976,432** residual, which sums to **$1,026,408** —
   over by exactly **$50,000**, the 1994 advances applied against 1995 share sales (orig. l.3535 shows the 1994
   `Advances received for common stock … 50`; l.3546 shows `(50)` released against the 1995 sale). The written
   version carries the `− $50,000` term, and then it foots exactly:
   `5,408 + 150,000 + 871,024 − 50,000 = 976,432` ✓. **The document won.**
3. **The audit's consideration tie for the program split is off by $3.** The sheet and register print
   `245,573 + 5,408 + 921,000 = $1,171,978`; the sum of those three terms is **$1,171,981**. Either way it rounds
   to the filed `$1,172` thousand, so nothing substantive turns on it — but the number on the page is wrong, and
   the corrected sum is what is recorded in d25 and in `quantitative.csv`.
4. **D19 — the register's two candidate values were both rejected as single points.** Asked to "state which
   convention", the answer is that naming one of $21,383 / $19,440 would repeat the very error D18 corrected; the
   row now carries the band **≈$19,400–$21,400** with both computations visible at d30.
5. **D01/D24 — the register's offered *alternatives* were declined where the primary option preserved more.** The
   audit's "claims cut" table proposed *deleting* r93, and the register allowed either `1006899.30` **or** the
   division re-expression; both the row and the division are kept, because the row is where the rounding direction
   is now taught. For S0804 the register offered re-key **or** restoring accession 0000891020-97-000868; only the
   re-key is possible from `sources/`, so that is what was done and the gap is stated rather than papered over.
6. **`quantitative.csv` row-count premise.** The audit sheet describes "all 105 data rows"; the file held **104**
   data rows (lines 2–105). Not a defect and nothing was changed for it, but the repair added 6 rows, so the file
   now holds **110** and every r-number in the register maps **two to six lines lower** past the insertions
   (r93 → r97, r52 → r53/54, r83 → r85/86, r91 → r94/95). Mapping given above per row.
7. **Audit CHECK 1 item 9 (two EPS denominators: 10-K405 pro forma 14,394 vs S-1 18,780, both $(0.02)) and
   CHECK 1's P49 numerator/denominator mismatch were NOT registered as defect rows.** The 1995 EPS row was left
   alone — the S-1's own basis is cited and correct — but the denominator-pair risk is flagged as open in §D
   because it is real and the 31-row register does not own it. The IDC mismatch, which was folded into D25, is
   registered.

---

## D. Left open (deliberately)

| Item | Status | Why it stays open |
|---|---|---|
| In-window portion of the $1,007,000 program | **UNKNOWN** | Ruled here; candidate derivation preserved at d25 for a later pass with subscription-dated evidence. RD-020 stays open. |
| Identity of the 1995-08-07 employee purchaser; the 20 unaffiliated; the 2 founder-related; all 23 | **UNKNOWN** | Never named in any version. RD-019 open. The 1995-08-08 Kaphan adjacency is recorded as a coincidence, not an identification. |
| Whole-company valuation for 1995 | **UNKNOWN** | Now a conclusion, not a missing input: the count exists (P67) and three prices exist, but no document multiplies them into a value. COR-09 bars the ~$5M/20% pairing. |
| $1,000 gap between cash-paid ($80,000) and accrual ($81,000) capex | **UNRECONCILABLE on the record** | Basis difference and/or rounding in thousands; no figure was invented to close it. Recorded in §R Unknowns. |
| `sources.csv` S0804 accession 0000891020-97-000868 and S0806 (FY1996 annual report, no accession/URL) | **restoration pending** | Text not on disk; the numeric claims are re-keyed to what is on disk, but the documents themselves still cannot be verified. RD-023 partially closed. |
| 151 vs 158 employees at 1996-12-31 | **kept side by side, unreconciled** | COR-11.2 / COR-12; both post-boundary; different documents, undisclosed restatement basis. Not a numbers-repair call. |
| 10-K405 pro forma EPS denominator (14,394) vs S-1 (18,780) for the same $(0.02) | **flagged, not entered** | Audit Check 1 item 9, outside the 31-row register. Needs its own defect row before it is touched. |
| `AUDIT_PROTOCOLS.md` AUDIT 3.1's Nov–Oct fiscal-year premise | **not dataset work** | The audit proved the premise false (EDGAR `FISCAL YEAR END: 1231` in all four filings). RD-022 belongs to the Master Orchestrator. Protocol text was not edited here. |
| The 7 `quantitative.csv` rows with no §P twin, and the one-directional §P ↔ CSV set relation | **noted** | Structural (Check 4). New §P rows P66–P70 close the three most load-bearing gaps; the remaining unpaired rows (r7 reserve, stub components, r34 loan, r70 AP) are now mirrored in §K/§Q prose but not as §P IDs. |

---

## E. Files written this pass

`stage_1.md` · `context_appendices.md` · `quantitative.csv` · `timeline.csv` · `validation.csv` ·
`failures.csv` · `decisions.csv` · `data_gaps.csv` · `sources.csv` · this log.
**Not written:** `channels.csv` (no defect touched it), `conflicts.csv` (out of the numbers brief; its U.8/U.9/U.10
prose was checked against the corrections above and no figure in it contradicts them — U.8's numbers are the ones
this pass corrected, and §U.8/§U.9/§U.10 *inside `stage_1.md`* were corrected), `_parts/` (read-only), `sources/`,
`stage_1_claim_records.md`, `adversarial_review.md`, `_MANIFEST.md`, `CORRECTIONS.md`.

## F. Post-edit CSV validation (Python `csv` parser, re-run after all edits)

| File | lines | data rows | cols | field-count mismatches | empty cells (excl. `derived_arithmetic` on FACT/UNKNOWN rows) |
|---|---|---|---|---|---|
| `quantitative.csv` | 111 | 110 | 12 | **0** | **0** (74 legitimately empty `derived_arithmetic` cells) |
| `timeline.csv` | 58 | 57 | 11 | 0 | 0 |
| `validation.csv` | 30 | 29 | 11 | 0 | 0 |
| `failures.csv` | 34 | 33 | 11 | 0 | 0 |
| `decisions.csv` | 16 | 15 | 15 | 0 | 0 |
| `data_gaps.csv` | 24 | 23 | 8 | 0 | 0 |
| `channels.csv` (untouched) | 16 | 15 | 11 | 0 | 0 |
| `sources.csv` | 103 | 102 | 18 | 0 | 0 |
| `conflicts.csv` (untouched) | 43 | 42 | 15 | 0 | 0 |

Checks actually run, not assumed: (a) every row's field count equals the header's; (b) **content alignment** was
pattern-tested column by column — `company` is `Amazon.com` in every row, `stage` is one of `stage1` /
`stage2-consequence`, `date` begins with a digit — because the register warns that an unquoted comma previously
shifted a whole row **silently while keeping the column count correct**, and a count check alone cannot see that;
(c) no empty cell anywhere except `quantitative.csv`'s optional `derived_arithmetic` on FACT/UNKNOWN rows;
(d) §13 quoting normalised with `QUOTE_MINIMAL`, so every field containing a comma is quoted;
(e) **boundary fence re-tested**: zero `stage1` rows carry a 1996/1997 date in `quantitative.csv` or
`validation.csv`, and `validation.csv` rows 26–28 are now the `stage2-consequence` rows they describe.
