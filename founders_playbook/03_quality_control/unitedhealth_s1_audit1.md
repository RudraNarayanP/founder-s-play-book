# UnitedHealth Stage 1 audit 1

**Auditor:** `uhc-audit1` (independent first pass; not the author, merger, repairer or certifier).
**Subject:** `company_003_unitedhealth` Stage 1 — `stage_1.md` (merged volume), `stage_1_index.md`,
`_MANIFEST.md`, `CORRECTIONS.md`, the nine registers, four dossiers under `research/`, and the bytes
under `sources/`.
**Method:** `00_METHOD_AND_STYLE.md` §9–§15 (§14 defect catalogue, §15 binding pipeline). Log
context: RD-126…RD-132. The merge agent (`uhc-s1-merge`) reported out of turn-ceiling, so its
self-report was treated as a claim to be measured, not as evidence. Web calls used: **0**. Files
written by this pass: **this file only**.

## Verdict

**PASS-WITH-FINDINGS.**

Merge integrity is clean — every one of the 230 register rows traces to an emission block, the fold
arithmetic verifies to the row, and the known `validation.csv`/`failures.csv` schema ambiguity landed
correctly by content. The volume's central quantitative architecture (the restated FY1990–FY1994
series, the owned/managed enrollment splits, the three defects kept open inside held primaries) is
carried line-for-line by the four SEC accessions on disk. What is wrong is concentrated: **four
arithmetic or counting claims, two source-carrier defects (one with no bytes in the repository at
all), a mislabelled claim class, a coda that asserts a motive, and a set of self-measurements in the
instruction layer that do not match the bytes they describe.** 18 blockers below; none requires
deleting evidence, and one of them (the word count) is a claim that must be corrected **without**
trimming the volume.

## Blocker list for the repair agent

Each line: locator — the claim as written — what the carrier prints — minimal honest fix.
Register row numbers are 1-based **data** rows (header excluded). Money is USD as filed.

**BLK-01** `quantitative.csv` Q82 (`revenue_cagr_1990_1994`) — "35.9 | percent per year …
`3768882/1056019 = 3.569; 3.569^0.25 - 1 = 35.9%`" — the carrier (EX-13 l.7428) prints the two
endpoints 1,056,019 and 3,768,882; 3.569^0.25 = 1.3745, i.e. **37.4 %** per year over the four
compounding years 1990→1994 (1.359^4 = 3.411, not 3.569) — restate the value to 37.4 and print the
corrected root, or drop the row and rely on Q8 (3.57× multiple), which computes.

**BLK-02** `stage_1.md` §U.017 (l.2282), `conflicts.csv` U.017, `quantitative.csv` Q69 derived cell,
and the merge note (l.169) — "`990,400 ÷ 0.64` implies a base of **about 1,558,000**" — the printed
division gives **1,547,500** — replace 1,558,000 with 1,547,500 in all four places; the conclusion
("matches no January-1994 figure"; Schedule F's January-1994 owned total is 1,976,000) is unaffected.

**BLK-03** §U.017 / `conflicts.csv` U.017 — "GenCare (197,900-230,000) plus **Puerto Rico
(133,900-135,100)** together account for only ~330,000 of the gap" — the same 10-K405 prints that
Group Sales and Services of Puerto Rico was acquired **on February 28, 1995**, i.e. after the
"twelve months ended January 1995" window the figure describes — either remove Puerto Rico from the
window arithmetic or label it "acquired 1995-02-28, outside the window; excluded from the base".

**BLK-04** §L.2 (l.1444), §M.1 (l.1488), §O.1 (l.1615), `failures.csv` row 5 — footnote 12 is
"attached to **four named managed plans**", and §M.1 names "Physicians Plus, Physicians Health Plan of
Northern Indiana, **South Carolina, and related**" — the FY1994 10-K405 marks footnote **(12) on
exactly two plan rows** (l.274 Physicians Plus Insurance Company, Madison WI; l.277 Physicians Health
Plan of Northern Indiana, Fort Wayne IN); Physicians Health Plan of South Carolina (l.285) carries no
footnote; the footnote text itself is at l.347-348 — change "four" to **two**, delete "South Carolina,
and related", or set the count UNKNOWN.

**BLK-05** `timeline.csv` row `1981` ("Arthur Andersen begins auditing the Company's financial
statements", class FACT, conf High, `source_id` **S4301**) — S4301 (FY1994 10-K405) names Arthur
Andersen only in the auditor signature blocks (l.8786, 8806, 9013) and **states no start year**; the
date is printed by S4305, the 1995 DEF 14A: "Arthur Andersen & Co. has examined the Company's
financial statements **since 1981**" — re-point `source_id` to S4305 (S4301 may stay as co-carrier
for the Minneapolis signature); the date itself survives.

**BLK-06** `sources.csv` S4328 (Medical Economics vol 61 Index, 1984) — `archived_url` =
"`TEMP uhg_b/me1984.txt`", `independence_note` asserts "independent serial, second year; **76,685 B**",
`relevant_passage` is quoted from it, confidence High — **no such bytes exist in `sources/`**: the
company's own `sources/_PROMOTED_FROM_TEMP.md` lists the seven temp files promoted on 2026-09-25 and
`me1984.txt` is not among them, and a scan of all 117 held files returns zero hits for the 1984 index
text (only `fts_ipo1984*.json`, which are unrelated EDGAR full-text-search bodies) — run the row's own
named archive.org URL through scripted intake into `sources/periodicals/`, and until the bytes are
held set the row's archived state to NOT_HELD and downgrade `data_gaps.csv` row 20's
"best_available_evidence" (which cites S4328) accordingly. Do not delete the row (§14 rule 4).

**BLK-07** `sources.csv` S4327, S4329, S4325 — `archived_url` still addresses the deleted temp
directory ("`TEMP uhg_b/me1978.txt`", "`TEMP uhg_b/ab1978.txt`", "`TEMP uhg_b/burke.json`") while the
bytes are held and byte-consistent at `sources/periodicals/me1978.txt` (48,818 B — matches the row's
own claim), `sources/periodicals/ab1978.txt` (130,273 B), `sources/periodicals/burke.json` (60,243 B,
content verified as the EDGAR submissions body for CIK 0000905023 with 1997-09-24 present) — re-point
the three `archived_url` cells to the held paths; note in passing that `burke.json` sits under
`periodicals/` though it is SEC metadata, and that the promotion note describes it as "Internet
Archive metadata", which the bytes contradict.

**BLK-08** §A.3 (l.478-490) — "…then converted from a fee-for-management relationship into majority
ownership **when the risk was worth holding**" — no held document states a conversion criterion; the
volume's own `data_gaps.csv` row ("any internal record of deliberation 1974-1994 — none exists in any
of the five families") is the counter-evidence — per §14's coda duty, either print "mechanism
UNKNOWN" in place of the motive clause or recast the sentence as INFERENCE with a named alternative
(the conversions track licensure, capital and the pooling accounting, not an underwriting judgment).

**BLK-09** `_MANIFEST.md` (row 1), `stage_1_index.md` (¶2 and Volumes table) and the merge note
(l.13-15, l.25-35) — the volume is stated as "44,921 words / 312,292 B", "44,981 words / 44,994 /
312,765 bytes", "**44,99615,004 words** of headroom", and the part as "42,649 w / 300,613 B as
written" and "42,703 w / 298,482 B as carried here" — measured on disk: `stage_1.md` = **44,996 words
/ 312,780 bytes**; the carried body = 42,668 w / 298,251 B; `_parts/s1_p1.md` = 42,924 w / 300,106 B.
The merge note's own running column also does not foot (42,924 − 35 = 42,889; "+77" is shown as
landing on 42,745; the deltas sum to 45,218) because the 221-word superseded block is never
subtracted on its own line; the manifest states that block as "1,624-byte" where it measures 1,626 B,
and states the carried body as 298,253 B where it measures 298,251 B — restate these from disk and add
the missing −221 line; do **not** trim prose to make any stated number true (§9.6, §15.4).

**BLK-10** `_MANIFEST.md` "Defects and discrepancies" item 1 — "The gate reports `stage_1.md` at
44,921 words against the `core` cap of 22,000 … and against T3's 8,000" — the briefed gate run
(`--tier exemplar`) reports `budget stage_1.md 44996 words (cap 60000)` as a **PASS**; the single
finding is the verbatim-quote gate, not a length overage, and §9.2 makes 40,000–60,000 amber and
explicitly allowed as one file — correct the manifest's description of the gate, and record that
there is no overage to repair.

**BLK-11** `failures.csv` row 9 and `decisions.csv` row 11 — `source_id` = the literal `none` —
§13 makes `UNKNOWN` the valid value and an empty cell a defect; `none` is neither and is invisible to
the gate's `S####` resolver — write `UNKNOWN` and keep the search record in the notes cell.

**BLK-12** §P.2 identity 2 (l.1746-1749) — "Owned 3,358,546 + managed and specialty 456,109 +
corporate and eliminations (45,773) = 3,768,882 ✓ equals total revenue **at l.698**" — the three
components are the 10-K405 EX-13 segment row (l.7632 region); l.698 of the 10-K405 is unrelated
product prose, while l.698 of the **8-K** prints "TOTAL REVENUE $ 3,768,882 100.0% $ 3,115,202 100.0%
21.0%" — the identity is true; name the file for each address (or convert to stable §-labels per
§14 rule 12).

**BLK-13** `quantitative.csv` Q66 — "one-time merger costs … `35,940 pre-tax; 22.3 million after tax;
0.13 per share`", class **FACT**, `derived_arithmetic` = "not applicable" — the filings print the
pre-tax 35,940 (10-K income statement "Merger Costs (35,940)"; 8-K "MERGER COSTS (3)(4) (35,940)");
the after-tax amount and the per-share amount exist only as the difference between two printed pairs
in the release ("excluding merger costs … Earnings -$310,422 & EPS - $1.77" against 288,139 / $1.64):
310,422 − 288,139 = 22,283; 1.77 − 1.64 = 0.13 — either show the subtraction in the arithmetic cell
(§8 forbids a derived number labelled as observed) or cite a footnote if one prints them.

**BLK-14** `quantitative.csv` Q60 — `unit` = "USD (**face value** at a quoted price, point-in-time)"
and the folded `MERGE[…]` cell preserves research/B's `derived_arithmetic`: "172943352 x 43.25 =
7479799974; minus 5782458005 = 1697341969 **held by directors, officers and 13G filers**" — the cover
prints "the aggregate market value of voting stock held by non-affiliates of the registrant as of
March 13, 1995, was approximately $5,782,458,005* (based on the last reported sale price of $43.25
per share …)": it is a **market** value, not a face value, and the registrant never names who holds
the 1,697,341,969 residual — relabel the unit "market value, point-in-time" and mark the residual
attribution INFERENCE (both subtractions themselves compute correctly).

**BLK-15** §P.1 record **P1-22** — `Passage: "LONG-TERM OBLIGATIONS … 41,649 … 24,132 … 39,099 …
24,275"` — the carrier prints the row in the other direction: "Long-term Obligations $ 24,275
$ 39,099 $ 24,132 $ 41,649 $ 39,123" (1994→1990, l.7455) — the year-to-value assignments in the
volume are correct and §P's table discloses the direction ("period-end 12/31/1991 → 12/31/1994"), so
the only fix is to re-order the elided quote to the print's order, or mark it `NO_VERBATIM_PASSAGE_RECORDED`;
this is the one genuine span mismatch among the gate's five flags.

**BLK-16** `validation.csv` row 4 — `evidence_class` = "**FOUNDER CLAIM**, contemporaneous" for
"+384,000 / 18 percent" — the release states it in the company's own voice ("Internal enrollment
growth … rising by 384,000 enrollees, or 18 percent"), and §R.1 of this same volume records "a
chairman/CEO (McGuire) who is **not the founder**" — reclassify as FACT (disclosure) or
CONTEMPORARY OBSERVATION; the volume must not hand a corporate press release a founder's voice.

**BLK-17** `timeline.csv` `company` column — the register carries six distinct values:
`United HealthCare Corporation` (21), `unitedhealth` (13), `Charter Med` (2), `Richard T. Burke` (1),
`UnitedHealth Group Incorporated` (1), `Prudential` (1); `quantitative.csv` (80/3), `conflicts.csv`
(20/3) and `data_gaps.csv` (18/4) split the same way between the registrant's name and `unitedhealth`
— §13 puts actors in `actors`, and RD-127's lesson is that a filter keyed on one string silently
drops the rest — normalise `company` to one registrant value per stage, move the actor names to
`actors`, and record the alias counts in `_MANIFEST.md` the way the stage-vocabulary normalisation
was recorded.

**BLK-18** `quantitative.csv` Q27 and Q62/Q72/Q73 label precision — Q27 `unit` = "thousands
(average)" with no primary/diluted marker although the print distinguishes them for 1990 (Primary
124,898 / Fully Diluted 138,022, l.7448-7449; the basis survives only inside the folded
`weighted_average_primary_shares` marker); Q72's unit "USD per share (**face**)" describes a
**redemption price ceiling** ("up to a maximum of $39.00 per share"); Q73's date 1994-05-11 is the
shareholders' adoption date, and the exhibit also prints board adoption 1994-02-10 and its own
execution "this 13th day of May, 1994" (l.1782-1783, l.1790, l.1800) — add the basis markers; §6
requires numerals to carry theirs.

**Also for the repair agent, and for the log owner:** `merge_census.py` reported this company's
request side as 179 attributable rows + 16 UNATTRIBUTED and "24 sources.csv rows missing". Both
halves are tool artefacts, re-measured here: the 24 "missing" source rows are the pre-mint ids
`P1S01…P1S24`, which the merge legitimately re-minted to `S4301–S4331` (the full alias map is in the
merge note l.104-134), and the census is blind to all **64** rows in
`research/B_chronology_finance_from_print.md` because it globs `_parts/*.md` only and that emission
carries no `>>> … MERGE … <<<` marker. RD-127/RD-131's defect reproduces exactly; the merge did not
inherit it. Separately, `gates.py --out` created a **directory** named
`unitedhealth_s1_gates.md/` containing `gates_company_003_unitedhealth.md` (and the .json) — geometry
note for the tool owner, not a company defect.

## 1. Merge integrity — items checked

The merge never self-reported (turn ceiling), so this class was measured from disk against the two
emissions, not against the census.

* **Registers read:** 9 files, **230 rows** (quantitative 83, timeline 39, sources 31, conflicts 23,
  data_gaps 22, validation 8, failures 8, decisions 10, channels 6) — matches the briefed counts
  exactly. **0 column-width drift** (12/11/18/15/8/11/11/15/11 columns), **0 empty cells** across all
  230 rows.
* **Emission blocks parsed:** 14 — 9 in `_parts/s1_p1.md` (all nine behind their own markers, so the
  census attributes them) and 5 in `research/B_chronology_finance_from_print.md` (none behind a
  marker; invisible to the census). Requested rows: 195 (p1) + 64 (research/B) = **259**, which is
  what the merge note claims.
* **Rows present in a register with no block: 0 undeclared.** Content-traced 230/230 against the two
  emissions. The only rows not in any emission are the **5 the merge itself minted and named**
  (`conflicts.csv` M-01, M-02; `data_gaps.csv` rows 21-23 from the residual cells of U.009/U.016/
  U.017), each carrying an in-cell "[minted at merge…]" marker.
* **Blocks whose rows never landed: 0 undeclared.** All 29 net reductions are the merge's declared
  **34 folds**, and the per-register fold counts verify to the row against my own matcher:
  quantitative 21, timeline 4, sources 4, data_gaps 4, conflicts 1 = 34; per-register arithmetic
  closes (259 − 34 + 5 = 230). COR-04's stage claim verifies exactly the same way: of research/B's 64
  rows, **30 landed as their own rows** (quant 3, timeline 13, sources 7, gaps 4, conflicts 3) and
  **34 folded**.
* **Duplicate primary keys across the two emissions: 0.** 31 distinct `source_id`s, 23 distinct
  `conflict_id`s (18 §U + C-02/C-03/C-04 + M-01/M-02), 0 duplicate timeline (date, event), 0
  duplicate decisions/channels. The one composite collision in quantitative — (1994-12-31,
  "net earnings before extraordinary item…") — is **two different measures** (288,139 as reported at
  EX-13 l.7431 vs 310,422 excluding merger costs at 8-K Ex-99.1), not a duplicate.
* **`source_id` resolution:** every carrier column (`timeline`, `validation`, `failures`,
  `decisions`, `channels`, `quantitative.source`, `sources.source_id`) resolves to the global block
  `S4301–S4331`; 167 re-pointed citation cells claimed, and dossier-local ids (`P1Snn`, `BS-nn`,
  `UH-nn`, `B-nnn`) survive only inside prose/notes cells, which is what §13 permits, with the alias
  map published twice. Two `none` cells are BLK-11.
* **`stage` values:** 230/230 read `stage1`; **no numeric stage anywhere on disk**. The numeric `1`
  existed only in the research/B emission (64 rows), as COR-04 claims, and was normalised with a
  per-row marker.
* **`validation.csv` / `failures.csv` ambiguity (8 + 8):** resolved by content and **each row landed
  in the right register** — the 8 validation rows are all positive signals (3.57× revenue
  compounding, owned-plan margin 7.0→8.4→10.5, SG&A 17.3→14.7, +384,000/18 %, market access, the
  1992 equity raise, 23 M participant lives, +152,500 record month) and the 8 failure rows are all
  negative (Iowa disposal, DPS exit, −24.5 % management services, contract-expiry risk, loss of the
  home-market plans, the 1987-08/1988-02 founder structure, the one-off gain presented beside
  operating earnings, and the recorded null "no failure of any kind is recorded"). 0 misplaced.
* **Non-destruction claim tested:** the volume body is byte-for-byte the part minus its H1/scaffold
  banner (35 words) minus the trailing "MERGED / SUPERSEDED" block (221 words) — diff shows 28 lines
  changed, all in those two regions; **no prose word and no register row was altered at merge**, as
  claimed. The part's tail does carry the DO-NOT-RE-APPLY warning.

## 2. Numbers and dates — items checked

83/83 quantitative rows read. **Machine count:** every numeral appearing in the register's `value`
and `notes` cells was searched against the seven documents the register cites (the four 1995 SEC
accessions plus the FY1998 and FY1999 10-Ks and the 1998 S-4) — **126 distinct numerals tested: 120
found verbatim in the cited print; 6 not found, and all six are accounted for** (1,969,549 / 172,686,857
/ 43,808,704 are rows that print their own subtraction or division; 341,000 and 341,400 are the
audit's corrected figures held inside U.016's note, not claimed prints; 23,000,000 is the print's word
form "23 million"). **21 arithmetic identities recomputed: 19 confirm the volume, 2 contradict it
(BLK-01, BLK-02).** **19 date claims opened to the printed line: 17 carried, 1 carried by a different
document than the row cites (BLK-05), 1 with no carrier anywhere in the corpus but declared
UNKNOWN (the 1984 row).**

* **Cross-foots that hold:** 1,665,214 − 1,377,075 = 288,139 ✓ (l.7431-7435); 2,184,800 + 1,064,000 =
  3,248,800 ✓ (l.295); 2,730,900 + 332,300 + 185,600 = 3,248,800 ✓; 2,132,700 + 291,300 + 111,200 =
  2,535,200 ✓ (l.360-361); 3,358,546 + 456,109 − 45,773 = 3,768,882 ✓ (l.7632); 2,347,177 − 377,628 =
  1,969,549 ✓ against the quarterly summary balance sheet (12/31/93 400,870 · 03/31/94 377,628 ·
  06/30/94 2,347,177); 4,230,828 / 0.0245 = 172,686,857 ✓; 17,502,346 / 172,943,352 = 10.12 % ✓
  (proxy prints 10.12 %); 1,012,918 / 172,943,352 = 0.586 % ✓ (proxy marks it "*Less than 1%");
  55,822 vs 73,923 = −24.5 % ✓ (Schedule A, printed); 3.569 × ✓ for the 21 % growth row ✓ (10-K
  prints "21%", 8-K prints "21 percent" and Schedule A prints 21.0 %).
* **The five-year column alignment was tested because it is where a merge hides a one-column shift:**
  the print order is 1994→1990, so Long-term Obligations 24,275 (1994) / 39,099 (1993) / 24,132 (1992)
  / 41,649 (1991) / 39,123 (1990). The register's Q37 (1994 = 24,275) and Q38 (1991 = 41,649) are
  **both correct**; the 8-K's Schedule E corroborates 41,649 and 24,132 (l.901) and 39,099 and 24,275
  (l.930) "to the dollar", as P1-22 claims.
* **CONTEMPORANEOUS vs RESTATED:** 83/83 rows carry one of the two words (checked row by row); the
  pooling basis is stated where it matters ("restated for all periods presented … in accordance with
  pooling of interests … Complete Health and Ramsay were acquired on May 31, 1994"), the split basis
  is stated (February 23, 1994 two-for-one; an earlier September 1, 1992 split is carried by the
  proxy and the volume labels it "referenced only as a restatement event", Medium). Fiscal = calendar
  is declared on every money row.
* **Insurance-specific traps, tested explicitly rather than assumed:** (i) **gross vs net revenue** —
  the 1992 offering row says "net proceeds of approximately $196,000,000" and the register says net
  ✓; (ii) **a face amount vs a premium** — the MLR row is "owned-plan medical loss ratio, Q4 1994 =
  79.1 percent of premium revenue", and Schedule A's own line label is **PREMIUM** (877,317 / 736,647
  / 19.1 %), with the release defining "medical loss ratio (medical costs as a percent of premium
  revenues)" — the register also keeps the Q4 figure distinct from the full-year 79.3 % ✓; no
  earned-for-written or written-for-earned substitution was found; (iii) **an enrolled member vs a
  life covered under management** — the 23,000,000 row is labelled "participant lives
  (availability)" and the carrier prints "available to a total of approximately 23 million
  participant lives, 81 % of whom were not enrolled in one of the Company's …" ✓, and U.011 keeps the
  3,248,800 / 3,249,000 / 3,674,000 denominators apart ✓. The only label slips are BLK-14 and BLK-18.
* **Dates with a carrier that states them** (16 opened): 1977-01 ✓ l.168-169; 1974 ✓ as company
  self-dating (l.148-150 and 8-K l.290-292); 1988-02-19 ✓ carried **in full** at Ex-3(a) l.2522-2560
  (executed by Simmons 19th February 1988, sworn Hennepin County, "FILED FEB 19 1988 / Joan Anderson
  Growe, Secretary of State") — M-01's claim_a is not invented; 1994-05-11 ✓ l.1783/1790;
  1994-05-13 ✓ l.1800 ("has executed this document this 13th day of May, 1994"); 1994-05-27 ✓,
  1994-05-31 ✓, 1993-07-30 ✓, 1995-03-13 ✓ (cover and proxy), 1995-03-01 ✓ ("as of March 1, 1995"),
  1995-02-28 ✓, 1985-09 ✓ ("President from September 1985"), 1976-08 ✓ ("Health Planning Law
  (PL. 93-641). (August) 511"), 1978-11 ✓ ("Conversation with Dr. Richard K. Simmons … Physicians
  Health Plan, November, 665"), 1995-01-03 vs 1995-01-04 ✓ both printed (10-K l.201, l.325; 8-K
  l.1007-1008). **Two rows fail the test: the 1981 row (wrong carrier, BLK-05) and the 1984 row
  (no carrier — and it is labelled `UNKNOWN`/`UNKNOWN` with the null stated in its notes, so it is
  honest, though its carrier column should not point at the EDGAR index).**
* **The three held-primary defects behave as the volume says:** Schedule F's total-Medicaid cell for
  January 1995 prints **241,000** (l.986) while its own OWNED and MANAGED Medicaid cells print
  291,000 (l.974) and 50,000 (l.980), and the same row's printed change **+20.1 %** against a
  January-1994 base of 284,000 implies ≈341,000; the 10-K405 gives 291,300 + 50,100 = 341,400
  (l.360-364). U.016's description is right on the bytes (its "the same row's own … cells" phrasing
  means the Medicaid category across three rows; the line numbers it cites are the correct ones).
  U.017's +990,400 / 64 % pair is verbatim at l.275-278 against Schedule F's 1,976,000 → 2,535,000
  (+559,000, +28.3 %), so the conflict is real — only its implied-base arithmetic is wrong (BLK-02).

## 3. Citations — items checked

**31/31 `sources.csv` rows opened**, each `url`/`archived_url` resolved against the filesystem;
**22 line-number addresses** tested inside 5 documents; the gate's **23 attributed verbatim spans**
re-tested by hand.

* **Carriers that do not exist as addressed:** 1 — S4328 (BLK-06). 3 more address a deleted temp
  directory while the bytes are held elsewhere (BLK-07). 2 rows point outside the company directory
  but resolve in-repo: S4326 →
  `00_universe/harvest/periodicals_intake/unitedhealth_minnesota/MINNESOTA_MEDICINE_INDEX_1974-1980_EXTRACT_hmo_debate.txt`
  (12,274 B) and S4330 → `00_universe/harvest/candidates.csv` (1,031,151 B) — legal per §14 rule 9
  (in the repository), but a cold reader needs the repo root stated; note the promotion table
  describes `burke.json` as Internet Archive metadata when the bytes are EDGAR submissions.
* **Right document, wrong place / place that does not support:** §P.2 identity 2's `l.698` (BLK-12);
  the 1984 timeline row's carrier column (see above); the six Google Books rows S4307–S4312 all
  archive to **one** harvest body (`897cacbf3eb39aa4.xml`, 23,604 B) which does contain each quoted
  snippet, and the volume discloses that the 1978 and 1981 items are the same snippet text — a
  duplication the volume flags rather than doubles, and independence is capped at "one" accordingly.
* **Line addresses verified as landing:** 10-K405 l.66, l.148-150, l.168-169, l.171-172, l.201,
  l.274, l.277, l.285, l.295, l.325, l.347-348, l.360-364, l.1773, l.1782-1783, l.1790, l.1800,
  l.2498-2517, l.2522-2560, l.7410, l.7428-7456, l.7448-7449, l.7632; 8-K l.275-278, l.290-292,
  l.691, l.698, l.901, l.907, l.930, l.936, l.974, l.980, l.986, l.1007-1008; FY1998 l.156-160;
  FY1999 l.217. **All land on the quoted content except 10-K l.698.** This corpus's habit of citing
  by line rather than by stable label (§14 rule 12) is a re-keying hazard for the repair pass, not an
  accuracy failure today.
* **Span-level quote checks, with my own false-positive rate.** The gate flags 5 of 23 attributed
  spans (22 %). Re-testing each against the bytes: 4 are **gate false positives** — the volume quotes
  a Google Books snippet whose text is "coun- try" verbatim; two spans carry the volume's own `…`
  elision markers (the §12(b) covenant list and the GenCare press-release sentence); and P1-51's
  header span elides "PUBLIC DOCUMENT COUNT: 18" with an `…` while all four fields print adjacently
  in the `IMS-HEADER` block. **1 is a true mismatch** (P1-22's order-reversed five-year row,
  BLK-15). So my measured false-positive rate on this gate for this company is **4/5 = 80 %**, and
  the underlying quote discipline is **22/23 = 96 % verbatim-with-marked-elision**. The gate's own
  143 "skipped" and 72 "unattributed spans unmatched" are advisory and are the known Stage-1 intake
  shape §15.6 describes, not fabricated citations: every claim record in this volume cites bytes that
  are in `sources/` except BLK-06/BLK-07.
* **51 claim records** exist (P1-01…P1-51), each carrying Tier, Class, Passage, Conf, Corroboration
  and Conflicts; 47 use the fixed `Tier: n —` delimiter and 4 a variant — format drift only. The
  lineage discipline the method demands is present and correct: `independence_note` says "same
  lineage as P1S01", "one corporate record in four printings", "Wikipedia … adds ZERO weight", and
  corroboration is counted by origin, not by printing.

## 4. Hindsight and boundary — items checked

Read in full: `## Boundary` §1–§6, §A.3, §C.3 (7 knowability rows), §L.2, §M.1/§M.2, §N.1 (10
decision rows), §O.1/§O.2, §P.2, §R.1/§R.2 (6 rows), all 18 §U anchors (5 read in full text, 13 in
register form), and `## Untried`.

* **Is the claimed start the earliest defensible origin, and what anchors it?** Yes. The stage opens
  at **January 1977** and the anchor document is named and verified: **FY1994 Form 10-K405, Item 1,
  "United HealthCare Corporation is a Minnesota corporation, incorporated in January 1977" (l.168-169,
  filed 1995-03-28)** — the earliest printing of that sentence anywhere in `sources/` (a corpus-wide
  search found it only in this accession and in later restatements: FY1998 l.156, FY1999 l.217,
  FY2004, FY2005/06, FY2006/07). The volume caps it correctly ("High as to the 1995 statement;
  **Medium** as to January 1977 as the event; **day UNKNOWN**") and keeps 1974 as a **labelled
  preamble** rather than a dated act, which is the right treatment of a company self-dating its own
  service history. Four rival starts are each named with their document and rejected on evidence:
  1974-as-event, the 1975 lore (nothing held), 1984 (Tier-4 attribution whose underlying article is
  not held, EDGAR full-text-search zero with `_shards.failed: 0`, kept live as UNKNOWN), and the
  1993-12-31 close rejected as an availability artefact dressed as periodisation (`U.014`, kept live
  against the log's own RD-116 line). The record-selection null required by §2 is present in §A and
  §S, and the losers are kept live.
* **Evidence–mechanism–alternative–confidence applied to each causal coda:** §O.2 passes and is
  exemplary (it names the three propositions a hindsight reading would need and refuses all three);
  §L.2 passes (evidence in the restated series, mechanism = contract rollover and the disclosed
  UHC-Allina change, both carried; it does not claim the outcome was intended); §P.2 passes; §R.1/§R.2
  pass; §M.2's three internal-contradiction codas pass; §N.1/`decisions.csv` pass on the firewall —
  all 10 decision rows keep `unknowns` and `alternatives` non-empty (one says "UNKNOWN — no
  alternative is named in any held document"), `rationale` is "not stated" wherever nothing states
  it, and no `actual_result` reaches past 1994-12-31 (so the RETROSPECTIVE label is not required and
  its absence is not a defect). **One coda fails: §A.3's motive clause (BLK-08).**
* **Confidence inflation, checked class by class:** the only over-labelled rows I found are the 1981
  FACT/High date (BLK-05, whose carrier is a different document) and the two derived-as-observed
  labels (BLK-13/BLK-14). The volume's own instinct runs the other way — the +990,400 pair is Low,
  the Schedule F cell is Low, the founding self-dating is Medium, the 2022 newspaper's founder
  account is Low with "35-year lag" stated, and the boundary choice is Medium "because it is a
  decision and it is labelled as one."
* **UNTRIED/EMPTY/UNANSWERED discipline:** `## Untried` is present with routes, commands and what
  each could change; web budget spent **0**; the four corpus families are named and the two that
  returned nothing are separated from the ones never tried; the Chronicling America row S4331 is kept
  as a **negative artifact** ("FAILED: HTTP 308 Cloudflare redirect page, no JSON"), which matches
  RD-128/RD-129's measured cause and does not overstate a null.

## Gates

`python tools/gates.py --company-dir founders_playbook/01_companies/company_003_unitedhealth --tier
exemplar --out founders_playbook/03_quality_control/unitedhealth_s1_gates.md` → **1 finding, 21
passes** (the briefed "1 finding / 20 passes" is off by one pass, and the finding is **not** the word
count):

* Finding: `quotes verbatim — 5 of 23 quoted spans not found in local sources`; my re-check makes 4 of
  those 5 false positives and 1 real (BLK-15).
* `budget stage_1.md 44996 words (cap 60000)` — a **PASS**. The brief's premise that 44,996 exceeds a
  cap and is an "advisory overage" is wrong on the facts: §9.2 puts 40,000–60,000 in the amber band
  where finishing as one file is explicitly allowed, and §15.4 says a missed length target is never a
  failure. **Nothing may be cut to reach 40,000, and no evidence may be deleted to silence a gate.**
  The stale "over the core cap" story is itself a defect and is BLK-10.
* Passing and independently confirmed by this audit: 9 registers at declared widths, `S####` tokens
  resolve in five carrier columns, `keys stage_1.md 31 source tokens all resolve`, anchor parity
  **18 narrative ↔ 18 register**, `corrections propagation — all 8 retractations reach registers and
  volumes`, and the retired-key notes (S0001/S0155/S0812/S3000/S30001/S3001/S30084/S3029) are
  collision history quoted in the id-band argument, not live citations.
* Gate blind spots this audit found (for the tool queue, not for this company): it cannot see the
  64-row emission in `research/` (same RD-127 defect), it cannot resolve a carrier cell reading
  `none`, it does not test the `company` column's value set, and it cannot know that a
  `sources.csv` row's bytes are absent from the repository.

## Checks run that found nothing (with counts)

1. Register row counts vs the briefed census — **9/9** match; 230/230 rows.
2. Column-width drift and empty cells — **9/9** registers, 230 rows, **0** defects.
3. `stage` vocabulary — **230/230** `stage1`; **0** numeric values on disk; COR-04's 64/30/34 split
   reproduced exactly.
4. Duplicate primary keys — **4** key sets tested (source_id 31, conflict_id 23, timeline
   (date,event) 39, quantitative (date,metric) 83): **0** real duplicates (the 1 apparent collision is
   two different measures).
5. Register↔emission tracing — **14** blocks, **259** requested rows, **230** applied: **0** invented
   rows, **0** undeclared losses, 34 folds verified per register, 5 merge-minted rows declared.
6. `validation.csv`/`failures.csv` content attribution — **16** rows: **0** misplaced.
7. Non-destruction of the part — body diff: **0** prose changes, **0** row changes, 28 changed lines
   all in the banner/superseded-block regions.
8. Money figures re-grepped against the filings — **126** distinct numerals: **120** found verbatim
   in the cited print, **6** not found and all six accounted for (4 derived-with-shown-arithmetic, 1
   word form, 2 = the audit's own corrected figures inside U.016's note).
9. Arithmetic identities recomputed — **21**: 19 hold; 2 fail (BLK-01 CAGR, BLK-02 implied base).
10. Five-year column-year alignment — **6** rows (revenues, earnings from operations, cash and
    investments, total assets, long-term obligations, shareholders' equity, plus EPS/dividends/share
    counts): **0** column shifts.
11. CONTEMPORANEOUS/RESTATED and fiscal-year basis — **83/83** rows carry a basis; **0** missing.
12. Insurance traps (gross vs net; face vs premium; earned vs written; enrolled vs covered lives;
    Q4 vs full-year MLR) — **5** tests: **0** substitutions, 2 label slips (BLK-14, BLK-18).
13. Timeline date carriers — **19** dates opened: **17** carried by the cited document at the exact
    line; 1 carried by a different document (BLK-05); 1 undeclared-null but labelled UNKNOWN (1984).
14. Source carriers resolved to bytes — **31** rows: **27** resolve as addressed (BLK-06/07 are the 4).
15. Line-number addresses — **43** opened: **42** land on the cited content; 1 crosses files (BLK-12).
16. Attributed verbatim spans — **23**: **22** verbatim with marked elision (the 1 exception is
    BLK-15); my own FP rate on the quote gate is **80 %** (4/5).
17. Claim-record format — **51** records: all carry Class/Tier/Conf/Corroboration/Conflicts; **0**
    missing fields; independence-by-lineage applied in every SEC cluster.
18. Decisions firewall — **10/10** rows keep unknowns and alternatives; **0** post-stage leakage, so
    the RETROSPECTIVE label is correctly unused.
19. Data gaps — **22** rows; every High row carries a follow-up route: **0** open §13 violations.
20. Conflicts register — **23** rows, all with both sides, why-they-differ and residual uncertainty;
    **18** anchors declared = cited = covered, **0** undeclared, **0** uncovered.
21. Boundary defence — **6** candidates, **4** rejected with named documents, **1** kept live; the
    adopted opening date has a carrier and the adopted close is labelled a decision.

## Figures re-measured after this audit's last write

All of the following were measured again after the final edit to this file, and this file changed no
company byte (`WRITE` permission was one path only).

| item | value on disk |
|---|---|
| `stage_1.md` | 44,996 words / 312,780 bytes / 0 CR |
| `stage_1_index.md` | 1,068 words |
| `_parts/s1_p1.md` | 42,924 words / 300,106 bytes |
| volume body (from the FORENSIC header line) | 42,668 words / 298,251 bytes |
| merge header + merge note | 2,328 words (42,668 + 2,328 = 44,996) |
| register rows | 83 + 39 + 31 + 23 + 22 + 8 + 8 + 10 + 6 = **230** |
| `sources.csv` ids | S4301–S4331, 31 distinct |
| §U anchors | 18 declared, 18 cited, 18 register-covered |
| claim records | 51 (`P1-01`…`P1-51`); `Tier:` stamps 51, fixed-delimiter 47 |
| files under `sources/` | 117 (95 excluding `.meta.json` sidecars), 10 directories |
| `gates.py --tier exemplar` | 1 finding / 21 passes |
| `merge_census.py` | 9 blocks attributed, 2 AMBIGUOUS (16 rows), 24 false "missing" source ids, blind to 64 rows in `research/` |
| byte-slice proof asserted by the merge | **substance verified**: `stage_1.md[14529:]` is byte-identical to `s1_p1.md[229:]` for the full 298,251 B of carried body, and the 1,626-byte / 221-word superseded block is exactly what the part adds beyond it — the part offset 229 is right as stated, but the body length is stated as 298,253 B (measured 298,251) and the volume offset as 14,039 (measured 14,529), both inside BLK-09's measurement set |
