# CORRECTIONS.md — company_042_target, Stage 1

Provenance correction register for this company. Standing rule (method §14 rule 8 and rule 10): a withdrawal
**supersedes** the text it withdraws, it never erases it. The withdrawn wording stays visible where it was
written — in `_parts/`, in the part's own register-block preamble, in a register cell — and the correction
names the carrier that replaces it. Reverting one of these is a defect.

Opened 2026-09-26 by the Stage-1 merge pass (`03_quality_control/target_s1_merge.md`). The `corrections` gate
checks propagation mechanically: every id below must reach **both** the register layer and a stage volume. An
entry that reaches the prose but no register is the failure this file exists to stop.

| Id | Withdrawn text | Where it lived (carrier of the stale claim) | Replaced by | Reaches |
|---|---|---|---|---|
| **COR-01** | "fiscal year equals calendar year in these reports" (inherited premise; restated in `_parts/s1_p1.md` §Boundary 4 as P1K10 and refuted in `_parts/s1_p2.md` as K8) | `_parts/s1_p1.md` §Boundary 4 and its quantitative block's bare-year date cells; `research/B1_dayton_print_records.md` Q1–Q26 store-and-sales series, whose **Q20** dates 186,166,671 as "1965" | a report labelled **N** is a 52/53-week retail year ending in late January / early February of **N+1**: the FY1965 layer's period end is **1966-01-29**, its comparative column ends **1965-01-30**, FY1966 ends 1967-01-28, FY1967 ends 1968-02-03 pattern confirmed by the printed keys (year ended February 1 1969 = fiscal 1968) | `conflicts.csv` **U.011**; 29 `quantitative.csv` rows; 2 `timeline.csv` rows; `stage_1.md` merge note. **Superseded in part by COR-07:** the re-tag this row claims was measured at the 2026-09-26 repair pass as **37 of 61** rows carrying a literal `PERIOD BASIS` tag and **21 of the 36** bare-year rows carrying none |
| **COR-02** | the documented floor for naming the company in the retail sense is **1972-03-22** | the Stage-1 dispatch brief, repeated in `MASTER_RESEARCH_LOG.md` line 1291 as a finding | **three defensible floors, none of them 1972-03-22**: the FY1965 document floor, the 1962 event floor carried only by retrospective print, the 1994-02-10 registrant floor. The string and its two alternate forms occur in **zero** bytes under `company_042_target/` | `conflicts.csv` **K16**; `stage_1.md` merge note. **Outbound:** `MASTER_RESEARCH_LOG.md` line 1291 still states it — that file is not owned by this pass, see below |
| **COR-03** | the trap: `_parts/s1_p1.md` §G's site-tenure UNKNOWN claim, and the adjacency in the FY1965 layer where **Brookdale** (L122-123) sits one line above the Target entry sentence (L124) so that a careless citation quotes a Dayton Development centre as a Target opening | the §G retraction was carried in volume 1's prose and in the cost/vendor gap row | Brookdale is the development arm's 1962 centre; the 1962 Target entry is **Roseville** and its three chronology companions; site **tenure is partially established** — buildings mortgaged, land sold and leased back — so "UNKNOWN" is withdrawn, and what remains unknown is the sale price, the cost, and the vendors | `conflicts.csv` **K17** (mis-citation), `timeline.csv` Brookdale row, `data_gaps.csv` cost/vendor row (shared with COR-04), `stage_1.md` merge note |
| **COR-04** | "site tenure of the founding stores is UNKNOWN" (volume 1 §G, retracted in the same pass that read the FY1966 notes) | `_parts/s1_p1.md` §G and the data-gap row that carried it | the FY1966 notes print a **land sale-and-leaseback at 225,000 annual rentals** with the buildings mortgaged: tenure is partially established; the unknowns are the price, the per-store cost and the vendor terms | `quantitative.csv` `annual_rentals_under_the_land_sale_and_leaseback`; `data_gaps.csv` (the cost/land-price/vendor gap); `stage_1.md` merge note |
| **COR-05** | the FY1970 layer byte count **52,736** printed in the probe table | `research/B1_dayton_print_records.md` probe table (volume 1's N6) | disk and sidecar both print **53,023 B**; the filed artifact wins; the probe figure is withdrawn and the correction is logged rather than quietly retyped | `sources.csv` **S4206**; `data_gaps.csv` **U.023**; `stage_1.md` merge note |
| **COR-06** | nothing was withdrawn — eight emitted rows arrived with **column drift** (unquoted thousands/place commas inside one cell): `s1_p2.md` sources l1179, l1185, l1186; quantitative l1211; timeline l1226, l1229, l1231, l1233 | the emitted blocks in `_parts/s1_p2.md` (which claimed, for volume 1 only, "0 misaligned rows") | re-joined at the printed split point so the cell holds the intended text; **no value altered, no cell re-worded**; repaired cells are tagged in place | `sources.csv` S4202/S4209/S4221; `timeline.csv` 4 rows; `quantitative.csv` 1 row; `stage_1.md` merge note |
| **COR-07** | the **eight** re-dated `date` cells **(count re-measured 2026-10-06 under round-4/N-4b: 7 `quantitative.csv` rows r54-r60 + 1 `timeline.csv` row 23 = 8; this row opened "the six `date` cells" — six as first counted, kept visible here per §14 rule 4 — and COR-21's claim that the count was printed "where each stale `six` stood" had not in fact reached the row this correction is about; it does now)** of `1973-12-31` / `1969-12-31` / `1972-12-31` / `1962-12-31` that COR-01's re-tag wrote onto the FY1969-FY1973 rows, **and** COR-01's claim that the period-basis re-tag had been applied to every bare-year row | `quantitative.csv` r54-r60 (five-year and roster rows); `timeline.csv` row dated `1973-12-31`; the COR-01 paragraph above | every affected row re-dated to the year-end **its own carrier prints**, each with the printed line quoted in the cell: FY1973 = **1974-02-02** and FY1972 = **1973-02-03** (`1973_dayton_hudson_djvu.txt` L172-174), FY1974 = **1975-02-01** (`1974_…` L147-148), FY1969 = **1970-01-31** (`1969_…` L1488). Where no held carrier prints a day (FY1970, FY1971) the day is **UNKNOWN and was not guessed**. The 21 bare-year rows that carried no literal `PERIOD BASIS` tag now do. Census reconciled in `03_quality_control/target_s1_repairs.md` (21 / 13 / 14 are three definitions, not three facts) | `quantitative.csv` r54-r60 + 21 re-tagged rows; `timeline.csv` 2 rows; `conflicts.csv` **U.011**; `stage_1.md` §Boundary 4 and §P; `_MANIFEST.md` row counts |
| **COR-08** | "the FY1974→FY1975 leg migrates to a 31-December year-end, so any series crossing it changes denominator" | `stage_1.md` §Boundary 4 L226-227; `conflicts.csv` **U.011** (and its merged P1K10 predecessor wording); `timeline.csv` row 17, which also carried the mismatched `source_id` **S4201** (the FY1965 report) for an FY1975 fact; **COR-01** | the corporation's own Fiscal Year note, quoted at its line inside this correction: `Fiscal Year. The Corporation's fiscal year ends on the Saturday closest to January 31. Fiscal year 1975 ended on January 31, 1976; fiscal year 1974 ended on February 1, 1975. Each of these years consisted of 52 weeks.` (`1975_dayton_hudson_djvu.txt` **L3246-3251** — six printed lines, the tail `consisted of 52 weeks.` is **L3251**; the locator this row first printed, `L3246-3250`, truncated the quote it was citing and is kept visible here per §14 rule 4 exactly as in the four places COR-21 already reached (round-4/N-4a)). The December-31 prints in that layer are the **Real Estate joint ventures'** condensed statements (L3570, L3578-3579, L3582-3583, L3604). `timeline.csv` row 17 is re-pointed to **S4211** and re-classed as the printed note | `timeline.csv` row 17; `conflicts.csv` **U.011**; `stage_1.md` §Boundary 4; `quantitative.csv` r54-r60 tags |
| **COR-09** | nothing was withdrawn — B1's Q20 parent-sales series reached the register as **3 rows where the emission carried 9**, so six printed components were dropped and one ratio's denominator was left unnamed | `quantitative.csv` (the parent net retail sales series), r18's `44 percent of net retail sales` source cell, `stage_1.md` §P | the six missing component rows added with their carriers: **217,961,635** FY1966 (`1966_…` L49, L323, L434) · **260,173,514** FY1967 (`1967_…` L765, L819) · **434,132,744** FY1968 (`1968_…` L1251, L1349, L1363) · **945,306** FY1970 (`1970_…` L829) · **1,086.4** FY1971 (`1971_…` L312) · **1,262,759,000** FY1972 (`1972_…` L10, L325, L939). r18's denominator is now named: `189,515,025 / 434,132,744 = 43.65%`, so the volume's printed "44" is true **against the Dayton Corporation total**, while (the same numerator is **23.84%** against the pooled Dayton Hudson FY1968 net retail sales of **795,243** thousand (`1969_…` L951)
— **23.83%** as recomputed to four places on the repair pass, and the register cell now carries the recomputed figure) | `quantitative.csv` 6 new rows + r18; `conflicts.csv` **U.010**; `stage_1.md` §P, §K.3; `_MANIFEST.md`, `stage_1_index.md` row counts |
| **COR-10** | §T.2's "P2S01 is the only held document of independent origin that touches the period" | `stage_1.md` §T.2 L1647-1649 — while the T.1 table above it (L1634) resolves `P2S01` to *Chain Store Age* and the register-emission block at L2119 resolves the same id to **the Dayton Company FY1966 report**, i.e. **S4202, same lineage as S4201** | the lineage rule applied: the only held independent in-window carrier is **S4215**, *Chain Store Age* April 1963 (T.1 tier row; `sources.csv` S4215 `independence_note` = THE ONLY INDEPENDENT IN-WINDOW CARRIER HELD), as **§H.2 already states**. §T.2 now names S4215 and records the id collision. The two corroboration cells that claimed a non-zero count (**P2-02** `1`, **B05** `1 lineage`) are restated as `0 independent` because each is a reiteration of one self-account | `stage_1.md` §T.2, claim records **P2-02** and **B05**, §T.1; `conflicts.csv` U.001/U.031 leg unchanged; `data_gaps.csv` **U.034** |
| **COR-11** | `60770000` as the FY1966 Target-unit sales value, and the silent choice among three printings of one number | `quantitative.csv` r15 | the value carries the precision the evidence supports and the choice is recorded: computed `86,901,007 / 1.43 = 60,769,935`; B1's dossier prints `~60,800,000`; the register had `60,770,000`. A 2-significant-figure printed percent cannot yield an 8-significant-figure dollar, so the cell is `60800000` at 3 s.f. and the two superseded renderings are named inside it | `quantitative.csv` r15 + 7 rows re-classed **DERIVED**; `stage_1.md` claim record **E02** and §K.3 |
| **COR-12** | the evidence-class and precision labels that read a print for something it does not print: `CONTEMPORANEOUS` on a comparative column; a 1974 roster's current areas as "fiscal year 1962"; `171,932,690` left unfooted against its own components; `7.50` and two mortgage/rental figures stripped of their printed qualifiers; a 1-thousand footing residual unrecorded; one volume paragraph describing two register rows as one at a higher confidence | `quantitative.csv` r17, r60, r32, r37, r38, r27, r11/r25; `stage_1.md` §K.3 L1239-1241 | each restated against its carrier, with the withdrawn reading kept visible in the cell; a row for the printed statement total **171,932,690** added so the 1966-01-29 money rows can be seen to fall **989,225** short and that residual named; the volume now says **two rows at Low**, matching the register | `quantitative.csv` r17, r27, r32, r37, r38, r11, r25, new total row; `stage_1.md` §K.3; `conflicts.csv` **U.012**, **U.016** |
| **COR-13** | the audit charge that S4203's two quoted passages are **reconstructions** — **REFUTED, not repaired** | `03_quality_control/target_s1_audit2_sources_independence.md` finding 1 (this file's owner is the orchestrator, so the refutation is recorded here where a cold reader looks) | the bytes: `1967_dayton_hudson_djvu.txt` **L1952 is `JOHN F. GEISSE`**, so `(L1952)` is a line locator and not invented text; **L769-770** prints `1967. Target's sales were $86,901,007, an in-` / `crease of 43 percent`. The real residue is fidelity and format: the possessive was dropped in the `sources.csv` relevant_passage cell and a locator sat **inside** the quoted span | `sources.csv` **S4203** (outbound: that file belongs to the parallel sources agent), `quantitative.csv` r15/r16, `stage_1.md` claim record **E02**, §D table, §P and §T.1 |
| **COR-14** | "no family returned an earlier document" (U.024) and "no contemporaneous periodical mention" (U.019) stated as corpus-wide nulls | `data_gaps.csv` **U.019**, **U.024**; `stage_1.md` §U.2 | scoped to their actual perimeter in the §7 vocabulary: **EMPTY-within-perimeter** for the families that ran and returned nothing, **UNTRIED** for the families U.032/U.033 record as never run. A null over an unsearched family is not a null (§14 rule 6) | `data_gaps.csv` U.019, U.024; `stage_1.md` §U.2 and the N-table |
| **COR-15** | "the fiscal-1966 Target-unit dollar is DERIVED and printed nowhere in any held layer" (r15), "the **only** Target-unit sales figure printed anywhere in FY1962-FY1968" (r16, §A.1, §P, §H.4 **N4**, **U.021**), and the derived 1966 base standing as the only route to that year | `quantitative.csv` r15, r16; `data_gaps.csv` **U.021**; `stage_1.md` §A.1, claim record **E02**, §H.4 N4, §K.2, §K.5, §L.1, §P, §T/§U null table, §U.2 U.021 prose | the carrier this register already cites for 1967 prints 1966 as well: `1967_dayton_hudson_djvu.txt` **L409-412** `Sales / of $86,901,007 in 1967 were 43 percent ahead / of 1966 volume of $60,731,468. Profits in- / creased by 161 percent.` Printed for **fiscal 1966 and fiscal 1967**; unprinted for 1962-1965, 1968 and 1970-1972. New rows **r69** (60,731,468 as printed, FACT, RESTATED, Medium under U.028), **r70** (the 161 percent rate, base UNKNOWN), **r71/r72** (the estate line `added 298,600` / `1,184,900 square [feet]`, with the 2,700 sq ft residual against r53 named not absorbed). r15 keeps its value as a **footing check** against the printed base. **U.013's FY1964 leg is NOT touched — no FY1964 Target base appears in any held layer and this finding does not refute it** | `quantitative.csv` r15, r16, r69-r72; `data_gaps.csv` **U.021**; `sources.csv` **S4203**; `stage_1.md` §A.1, E02, §H.4 N4, §K.2, §K.5, §L.1, §P, §T null table, §U.2 |
| **COR-16** | the **silent presence** of nine withdrawn-date rows inside the canonical volume: `stage_1.md` printed the retracted `1975-12-31` basis-migration row and seven December year-ends in its two `REGISTER ROWS FOR MERGE` slices with **no in-file marker at all** (`grep -ci superseded` = 0, `grep -ci "do not re-apply"` = 0 before this entry), so the volume taught by presence what COR-07 and COR-08 had withdrawn by value | `stage_1.md` volume-1 timeline slice (the `1975-12-31` row) and the volume-2 quantitative/timeline slices (December rows); the warning lived only in `_parts/s1_p1.md`, `_parts/s1_p2.md` and `stage_1_index.md` | **marked, not erased and not revalued**: a dated **SUPERSEDED — DO NOT RE-APPLY** block appended at each of the two emission banners declaring the root CSVs canonical and the slices pre-repair audit trail, plus an in-cell withdrawal marker on each of the **nine** rows naming its carrier line (`1973_…` L172-174, `1969_…` L1488, `1974_…` L147-148, `1975_…` L3246-3251) and its canonical row. §14 rule 4 supersedes: the slices are RD-122's byte-identical merge audit trail and were left in place | `stage_1.md` (2 banners + 9 rows), `quantitative.csv` r54, `timeline.csv` row 23, `stage_1_index.md` |
| **COR-17** | the `Reaches` cells of **COR-09** and **COR-12** asserted that their findings reached `stage_1.md` §K.3/§E.2/§P. Measured on the volume before this entry: `989,225` `171,932,690` `220,511,038` `1,088,338,000` `868,336` → **0 occurrences each in `stage_1.md`**; five repair-pass findings lived in `quantitative.csv` alone | `CORRECTIONS.md` COR-09/COR-12 `Reaches` cells; `stage_1.md` §K.2, §K.3, §E.2, §P.1 | the five figures stated **in the section that uses them**: the deduction total `171,932,690` (L837) against `139,686,954 + 31,256,511 = 170,943,465` and the **`989,225`** residual in §K.2 (new table rows) and §K.3 (as the anti-foil to the self-footing FY1973 row); the deltas **`220,511,038`** (`1967_…` L819) and **`1,088,338,000`** (`1972_…` L10) in §E.2 **with the rule they write** — no growth rate crosses FY1966→FY1967 or FY1971→FY1972 without naming which restatement it used (`19.37` vs `17.99` percent; `16.23` vs `16.03`, the layers print `18` and `16.0%`); the `868,336` component sum against the printed `868,335`, and the 1-thousand residual, in §P.1 beside COR-07/09/11. **No value changed, no new arithmetic, no plug** — the sums were re-run against the carriers before writing (L951, L1001-1004, L837, L944/L945, L819, L10) | `quantitative.csv` r27, r63, r66, r67, r68; `stage_1.md` §K.2, §K.3, §E.2, §P.1 |
| **COR-18** | U.032's expectation cell and two volume sentences: `the route most likely to lift the tier from T2 to T1` / `could lift the tier from T2 to T1` / `the only route that can move the tier from T2 to T1` — asserted with **no citation at all** (`RD-127` occurred **0 times** anywhere in this company directory before this entry) | `data_gaps.csv` **U.032** (`best_available_evidence`, `follow_up_task`); `stage_1.md` §U.2 U.032 and §H.5 U-3 | the measured statement, cited: `MASTER_RESEARCH_LOG.md` **RD-127** mined the held HathiTrust bodies — on the **company** phrase every dated result on the returned first page is **1990-2014**, and the 1950s depth is the **sector** pool (97 records 1950-1959 under `"five and dime" variety store`, 23 under `"Walton's" "five-and-dime"`), which §15.2 would not count toward a tier because it names a trade and not a registrant. The route stays **OPEN and UNTRIED** — 6 undated rows, 4 unparsed facet records, every page past the first unexamined — so this is a **smaller door, not a disproof**; a T1 re-derivation requires an in-window **company-naming** Tier-1 text from a third family, and the `periodical_harvest` task set is named as orchestrator work (`tools/` is outside every agent's write scope) | `data_gaps.csv` U.032; `stage_1.md` §U.2, §H.5, §T; `stage_1_index.md` |
| **COR-21** | (i) four `timeline.csv` rows (2, 3, 8, 9) that graded recap-carried **events** as FACT/High against the volume's own §Boundary 3.2 rule and row 18's cohort filing (RB-3); (ii) the B-5(a)/(b)/(c) residuals: the "six date cells" undercount of COR-07's own leg (measured: **7** `quantitative.csv` rows r54-r60 + **1** `timeline.csv` row 23 = **8** re-dated cells), the truncated FY1975 Fiscal-Year-note locator `L3246-3250` (carrier tail `consisted of 52 weeks.` is **L3251**) surviving in **six** places — `timeline.csv` row 17, `conflicts.csv` 2 cells, `stage_1.md` §Boundary 4, `CORRECTIONS.md` COR-08 row and the COR-08 prose section — and the unmarked OCR join at P2-07 (1965 `L1354-1355`, corrupt print `SS ey`) against a P2 preamble that promised "as printed" | `timeline.csv` rows 2/3/8/9; `timeline.csv` row 17; `conflicts.csv` U.011 cells; `stage_1.md` §Boundary 3.2 (rule), §Boundary 4 (locator + six-dates sentence), P2 preamble and P2-07 | events re-graded in place (rows 2/3/8 → `RETROSPECTIVE INTERPRETATION`/Medium; row 9 → FACT for the FY1968 openings + `RESTATED`/Medium for the eleven-store total, S4209's UNVERIFIED-TLS cap named) — **no date changed, no event deleted**; locators corrected to `L3246-3251` in all six places with the old range kept visible inside the retraction sentences; the six/eight date count re-measured and printed where each stale "six" stood; P2-07 carries `[OCR JOIN L1354-1355: …]` and the preamble now states the convention | `timeline.csv` rows 2/3/8/9 + row 17; `conflicts.csv` U.011; `stage_1.md` §Boundary 3.2, §Boundary 4, P2 preamble, P2-07 |
| **COR-19** | `sources.csv` S4203/S4207/S4209/S4210/S4211/S4217/S4218/S4219/S4220/S4221; `data_gaps.csv` U.025, U.026 | **tiers 1 → 3** for the four artefact rows (a retrieval artefact is Tier 3 at most; a body that never arrived witnesses nothing) — provenance of the inflation is the merge: the pre-merge sibling `P1S08` stamped the identical bytes **tier 3** and that `3` still prints in the volume's emission slice. Status codes → **UNKNOWN**, and stricter than briefed: the bodies print no code at all (the single `500` token in each is CSS — a font-weight list and a `width:500px`). S4211/S4217/S4209 independence cells rewritten (a scanner is a conduit, not an origin; an index of filings is the registrant itself). Transport stamps added to S4207/S4209/S4210. S4203's quote restored **without** retracting it (COR-13's refutation stands: L1952 **is** `JOHN F. GEISSE`) | `sources.csv` (10 rows), `data_gaps.csv` U.025, U.026; `stage_1.md` merge note and §H.4; `stage_1_index.md` |
| **COR-20** | `sources/_index/_INDEX.md` L5-6: **"This file is the source of truth for what exists. Do not re-search EDGAR for coverage…"** — a registrant-floor statement (CIK 27419 begins 1994-02-10) written as a global existence claim, inside a Tier-1-stamped bundle, in the file a cold reader trusts (§14 rule 10); plus **19 held files that no `archived_url` path pointed at**, two of them used as evidence anyway | `sources/_index/_INDEX.md` L5-6; `sources.csv` (the register as written); `data_gaps.csv` U.026 (which cited the FY1998 and FY2000 layers as evidence with no rows) | the header reworded to say **what it enumerates** (this CIK, this build time, derived from the raw response), **what it cannot answer** (anything before 1994-02-10 and anything about a predecessor CIK — U.025/U.036 stay open) and **how it goes stale** (a point-in-time build whose tool discards `formerNames`; re-run to refresh, and the reword must also be made in `tools/sec_intake.py` or the next build overwrites it). Four new rows registered: **S4222** (the five `ia_search` bodies, one set, Tier 3), **S4223** (the derived EDGAR index trio, Tier 2), **S4224/S4225** (the FY1998 and FY2000 print layers, Tier 1 carriers, `(PB)` evidence, Low). Measured after the pass: files on disk minus exact paths in `archived_url` = **0** (was 19), `sources.csv` 21 → **25** rows | `sources.csv` S4222-S4225 (+ exact paths added to S4217/S4218/S4219/S4220), `data_gaps.csv` U.026, U.025; `stage_1.md` merge note; `stage_1_index.md`; `sources/_index/_INDEX.md` |
| **COR-22** | the volume printed *"Fiscal year = calendar year in these reports."* in quotation marks as though it were a verbatim single-line sentence of a held corporate-print carrier, and attributed it to `research/B1_dayton_print_records.md` (RB-5); the token-pair `calendar year` occurs **0 times in any held corporate-print layer** and **once** in the dossier, split across two lines (RB-5). **SUPERSEDED IN PART 2026-10-06 (round-4/N-3): the 0-times half of this claim is FALSE and is withdrawn by this row — the pair occurs in 4 of the 14 held `.txt` corporate-print layers, and the four occurrences STRENGTHEN this correction rather than weaken it (measurement and carriers in the Replaced-by column). The citation-form retraction above STANDS unchanged; COR-22's id and scope are unchanged; the refuted zero is kept visible here as this row's dated record (§14 rule 4), because a false null inside a retraction is worse than the defect the retraction corrects — the retraction is exactly the part later agents trust.** | `stage_1.md` §Boundary 4; `conflicts.csv` U.011 `claim_a` | re-attributed to **the dossier's own premise line**, printed at `research/B1_dayton_print_records.md` **L74-75** (`Fiscal year = calendar` / `year in these reports (…)`), and §Boundary 4 now prints that exact two-line source with its L74-75 locator; **claim_a and the conflict STAND** — the premise was carried and the bytes refute it — so only the citation form is corrected; COR-01 is unaffected. **N-3 MEASUREMENT 2026-10-06, which replaces the 0-times claim (every line opened in the bytes before being cited): `calendar year` occurs in 4 of the 14 held `.txt` layers under `sources/corporate_print/` (28 files in that directory), plus the one dossier line — not 0.** (i) **FY1998 L2483, FY1999 L2001, FY2000 L1997** each print `report relate to fiscal years rather than to calendar years`, under `Fiscal Year Our fiscal year ends on the Saturday nearest / January 31. Unless otherwise stated, references to years in this` (FY1998 L2481-2483; FY2000 L1995-1997) — a **second, explicit, documentary refutation** of the inherited fiscal=calendar premise, three layers saying so about themselves; all three are **post-boundary `(PB)`** carriers, citable as `(PB)` only and **never for 1962–1975**. (ii) **FY1975 L2978** prints `have adopted a calendar year as their`, inside the sentence running L2976-2981: `All the joint ventures of the Real Estate subsidiaries have adopted a calendar year as their fiscal year. See Note F for condensed financial statements of the combined joint ventures.` — the accounting-policy sentence **in the very layer** whose December-31 prints COR-08 traced to `F. INVESTMENT iN JOINT VENTURES` (L3570), `Condensed combined financial statements of the joint ventures / follow:` (L3578-3579), `CONDENSED COMBINED RESULTS OF OPERATIONS / FOR THE YEAR ENDED DECEMBER 31, 1975` (L3582-3583) and `DECEMBER 31, 1975` (L3604): the joint-venture calendar-year sentence COR-08's own story predicts, an uncited carrier already on the shelf, now named by the retraction it supports (§14 rule 11). The dossier's premise line stays the only occurrence in `research/`: `research/B1_dayton_print_records.md` L74-75, split across two lines | `stage_1.md` §Boundary 4; `conflicts.csv` U.011 |
| **COR-23** | the instruction layer — `_MANIFEST.md` and `stage_1_index.md`, the two files every agent reads first — printed the **pre-round-3** corpus as current: `stage_1.md` 38,489 w / 261,590 B, `sources.csv` 21 rows and block `S4201`–`S4221`, `quantitative.csv` 68 rows, `data_gaps.csv` 22 rows, 164 register rows, 14 COR ids (RB-1); §14 rule 10 — a retraction kept out of the instruction layer re-imports the superseded state downstream, and a stale id range read together with the `company_011_microsoft` `S4222`–`S4225` collision is exactly how a bad re-mint happens; the volume's own global-ids note also still printed `S4201`–`S4221` | `_MANIFEST.md` per-file table + stage-vocabulary line; `stage_1_index.md` per-file table + row fold + id-range line; `stage_1.md` global-ids note | re-measured to disk 2026-10-06: `stage_1.md` **42,833 w / 292,456 B**, `sources.csv` **25** rows with the block **`S4201`–`S4225`**, `quantitative.csv` **72**, `data_gaps.csv` **23**, **173** register rows, **24** COR ids; every superseded figure kept as a dated "at the merge / at the 2026-09-29 pass / at the 2026-09-30 recertification" string rather than deleted (rule 4), and one line added naming `S4222`–`S4225` as also held by `company_011_microsoft`, tracked cross-company as task #31. **PROVENANCE OF THIS NUMBER (round-4/N-4c): COR-23's number was assigned post hoc, as a reasoned judgement — it was NOT minted for RB-1 from the start, and no reader of this row should infer that it was.** The agent that opened the COR-21…COR-24 block (`target-repair-3`) died at the 150-turn ceiling leaving a 285-byte stub, so **what COR-23 was reserved for is unrecoverable from disk**; RB-1 was the only blocker carrying no id and the only one §14 rule 10 makes blocking, so round-3b attached COR-23 to it rather than leave a hole in the register that a later pass would fill with something else, and deliberately did **not** re-tag the dead agent's correct RB-2/RB-4 edits, which stand under the existing ids they complete (COR-19, COR-15). Full account: `target_s1_repair_round3b.md` §3 and the "COR-23 assignment" ruling in `target_s1_recertification3.md` | `stage_1.md` global-ids note; `sources.csv` S4225; `_MANIFEST.md`; `stage_1_index.md` |
| **COR-24** | id hygiene (RB-7): §S.1's payroll/wages/headcount null was anchored to `U.028`, which in `data_gaps.csv` is the **transport** gap — a mis-keyed pointer to a different question; and three `data_gaps.csv` rows carried **no `U.0xx` key at all**, so they could not be cited or anchored — the 1963-64 store openings, the 1962-65 store cost / land-sale / vendor gap, and the payroll/wages/headcount null | `stage_1.md` §S.1 null table and §U.2; `data_gaps.csv` (the three unkeyed rows) | the three rows minted keys **U.101** (1963-64 openings), **U.102** (1962-65 cost/land/vendor) and **U.103** (payroll/wages/headcount); §S.1 re-pointed off `U.028` to `U.103`; and RB-7iv's stale self-count corrected `37,507` → `41,534` with the superseded number kept as a dated string (rule 4). **Left open, deliberately:** RB-7iii — `sources/_index/_INDEX.md` L26-27 attributes its provenance block to "certifier blocker B-4," which the recertifier reads as U.032 while `target_s1_repair_pass2.md` §4 numbers the same work "blocker 4"; the referent is genuinely ambiguous, so it is left for the re-certifier rather than guessed at in the corpus | `stage_1.md` §S.1, §U.2; `data_gaps.csv` U.101, U.102, U.103 |

---

## COR-01 — the year basis: no report labelled N is a calendar year

Volume 1 inherited from the records dossier the premise that these reports equate fiscal and calendar years,
and used it to date money. Volume 2 read the statement headers. The layer labelled **1965** prints "the fiscal
year ended January 29, 1966" and calls the same column 1966 in its notes; FY1966 ends 1967-01-28; the FY1969
layer prints the key itself ("year ended February 1, 1969" for fiscal 1968). Five printed year-ends across four
layers, three of them verified-TLS.

Consequences applied at merge: **B1's Q20 is re-based, not re-typed** — the 186,166,671 row now carries
`date = 1966-01-29` with the superseded "1965" label kept inside the same cell, and the 162,773,739 comparative
carries `1965-01-30`. Every quantitative row whose `date` is a bare year was ~~re-tagged
`PERIOD BASIS: CONTEMPORANEOUS|RESTATED` against the printing layer~~ **— this sentence over-claimed: measured on
the bytes at the 2026-09-26 repair pass, only 37 of the 61 `quantitative.csv` rows carried a literal `PERIOD BASIS`
tag and 21 of the 36 bare-year rows carried none, so the re-tag was NOT applied everywhere (see COR-07; the tags
are now applied).** The two conflict emissions (P1K10 and K8) were folded into one row, **U.011**. ~~The
FY1974→FY1975 leg migrates to a 31-December year-end and any series crossing it changes denominator; that migration
is a `timeline.csv` row, not a footnote.~~ **WITHDRAWN 2026-09-29 — the migration never existed and the sentence was
read off a joint-venture block; see COR-08, which carries the carrier sentence COR-01 should have carried.**

Residual: whether the B1 store-count series silently compared a January count to a December market figure is
resolved per row in the `PERIOD BASIS` tags, not globally, and ~~the FY1968-onward pattern was not re-tested by
this pass.~~ **TESTED IN PART 2026-09-29 (COR-07): held carriers print FY1969→FY1975 year-ends; FY1970 and FY1971
print no day and remain UNKNOWN.**

## COR-02 — a received date that exists nowhere

§14 rule 8 applied to a date: the dispatch premise "1972-03-22" was grepped across the entire company
directory in three written forms and returned zero hits — no filing, no layer, no index, no negative artifact.
It is therefore **not evidence** and was not written as a value. It survives as conflict **K16** with its
provenance gap recorded ("where the date came from is UNKNOWN; if a carrier exists it is outside this company
directory and must be fetched before use").

**Outbound correction, not owned by this pass:** `MASTER_RESEARCH_LOG.md` line 1291 still states the withdrawn
date as a finding. This file is the instruction layer of a shared log and rule 10 says that is the
highest-severity home for a stale claim; the merge records it here and hands it to the log's owner rather than
editing a file outside its brief.

## COR-03 — the two 1962 openings that print one line apart

The FY1965 layer prints "Brookdale shopping center … 1962" at L122-123 and "early in 1962 … Roseville" at
L397-398 — two different subsidiaries, near-identical directional geography, one document. Both are true;
neither corroborates the other. Any later quotation that renders L122-123 as a Target opening is a mis-citation,
so the trap is registered as a conflict (K17) and as a timeline row whose note forbids the reading, rather than
by deleting the Brookdale fact.

## COR-04 — §G's site-tenure retraction reached the registers

Volume 1 retracted its own §G claim in the pass that read the notes pages. A retraction that stays in prose
leaves the register teaching the old answer, so the withdrawal is written into the gap row that carried it and
the 225,000-rental row that replaced it.

## COR-05 and COR-06 — transcription defects

A byte count that disagrees with the artifact is corrected by reading the artifact (53,023 B), and the eight
drifted rows were re-joined rather than dropped or re-worded. Both are recorded because a silent fix is
indistinguishable from a fabricated value.

---

# Entries opened by the 2026-09-29 repair pass (COR-07 … COR-14)

Opened by agent `target-s1-repair` against the three Stage-1 audits and the orchestrator's own re-verification
(`03_quality_control/target_s1_repairs.md`, `MASTER_RESEARCH_LOG.md` RD-125). Every date below is the day the
carrier was read, and every re-dating quotes the printed line rather than describing it.

## COR-07 — the December year-ends, and the re-tag COR-01 claimed but did not apply

COR-01 did the right thing to the FY1965 layer and then wrote December year-ends for the later ones. Rows
`r54`-`r57` carried `1973-12-31`, `r58` `1969-12-31`, `r59` `1972-12-31`, `r60` `1962-12-31` — and **no held
carrier prints a 31-December year-end for the registrant in any year of the run.** The FY1973 report prints its
own at L172-174: `1973 1972 / : 52 Weeks Ended 53 Weeks Ended / Consolidated February 2, 1974 February 3, 1973`.
Each row was therefore re-dated to the year-end printed by the carrier that supplies its value, and the superseded
December value is kept inside the same cell as a retraction:

| row | withdrawn date | now | carrier that prints it |
|---|---|---|---|
| r54, r55, r56, r57 | 1973-12-31 | **1974-02-02** | `1973_dayton_hudson_djvu.txt` L172-174 (the same document as the five-year row) |
| r59 | 1972-12-31 | **1973-02-03** | same L172-174, second column: `53 Weeks Ended February 3, 1973` |
| r58 | 1969-12-31 | **1970-01-31** | `1969_dayton_hudson_djvu.txt` L1488 — the five-year header itself (L3975) prints only the bare label `1969`, so the day was taken from fiscal 1969's own report |
| r60 | 1962-12-31 | **1975-02-01** | `1974_dayton_hudson_djvu.txt` L147-148, and see COR-12: the numbers are the FY1974 roster's **current** areas, not 1962 areas |

**FY1970 and FY1971 print no exact day in any held carrier; those two days are UNKNOWN and were not inferred.**
The 21 bare-year rows that COR-01's paragraph says were re-tagged but were not now carry a literal `PERIOD BASIS`
tag derived from each row's own printing layer.

The census of that failure is stated in three definitions rather than one number, because three were measured and
none is wrong: **21 of 36** bare-year rows lacked a literal `PERIOD BASIS` tag (audit 1's definition, reproduced
exactly); **13** lacked any of `FY`/`fiscal`/`end` in `notes` (the orchestrator's, whose stem `end` matches
`year-end counts` in r6 and so counts a row that states no basis); **14** lack `FY`/`fiscal`/`ended`, which is this
pass's definition, since a word that merely appears inside another word is not a basis statement. All three counts
are of the same 36 rows; see the repair report.

## COR-08 — the FY1975 "basis migration" was a joint-venture line read as accounting policy

This is the defect the pass exists to teach from. **A correction that changes a basis must carry, quoted at its
line inside the correction record, the carrier sentence that establishes that basis.** COR-01 asserted a migration
without ever quoting a document, and because the assertion sat inside a *retraction* it was trusted by
`conflicts.csv` U.011, by `timeline.csv` row 17 and by `stage_1.md` §Boundary 4 — three propagations, one of them
into the instruction layer, from a sentence nobody had read. The carrier says the opposite, verbatim
(`1975_dayton_hudson_djvu.txt` **L3246-3251** — six printed lines; the tail `consisted of 52 weeks.` is **L3251**, so the locator that stood here, `L3246-3250`, stopped one line short of the block quote printed immediately below it: the self-mis-pointing COR-21 declared fixed "in all six places" and did not reach here (round-4/N-4a; the old range is retained as its dated record, §14 rule 4)):

> `Fiscal Year. The Corporation's fiscal`
> `year ends on the Saturday closest to`
> `January 31. Fiscal year 1975 ended on`
> `January 31, 1976; fiscal year 1974 ended`
> `on February 1, 1975. Each of these years`
> `consisted of 52 weeks.`

What the December-31 strings in that layer actually are (all of them, counted this pass): L3570 heads
`F. INVESTMENT iN JOINT VENTURES`; L3578-3579 says `Condensed combined financial statements of the joint ventures
follow:`; L3582-3583 prints `CONDENSED COMBINED RESULTS OF OPERATIONS / FOR THE YEAR ENDED DECEMBER 31, 1975` —
**one** occurrence of that full string in 5,458 lines, not two — and L3604 prints `DECEMBER 31, 1975` as the
companion joint-venture balance-sheet date. Both are a **Real Estate** venture's year-end, and the venture block
itself states it reports `at January 31, 1976` (L3575). `grep -c "Saturday closest to" stage_1.md` was **0** before
this pass: the one sentence that settles the question was quoted nowhere in 37,507 words.

`timeline.csv` row 17 is re-pointed from **S4201** (the FY1965 report, which cannot carry an FY1975 fact) to
**S4211** and re-classed from a basis migration to the printed note.

## COR-09 — six dropped components, and a ratio whose denominator was assumed

B1's Q20 parent-sales series reached the register as three rows where the emission carried nine. Six printed
figures were dropped, all six of them present in held carriers, and `434,132,744` occurs **0 times** in
`stage_1.md` and occurred 0 times in `quantitative.csv` before this entry: it is the FY1968 denominator of the
"44 percent of net retail sales" claim in r18. With it, `189,515,025 / 434,132,744 = 43.65%`, so the printed 44 is
true against the **Dayton Corporation** total; without it, a reader divides by the pooled Dayton Hudson FY1968 net
retail sales of `795,243` thousand and gets **23.84%**. A dropped component is not a missing nicety, it is a second
answer to the same question. The six rows are added with the lines that print them, and r18 now names its
denominator instead of assuming the reader will pick one.

## COR-10 — §T.2 contradicted §H.2 about which document is independent

`P2S01` is a retired dossier-local id, and the volume resolves it two ways: §T.1's table row says *Chain Store
Age*, April 1963; the register-emission block at L2119 of the same file says *The Dayton Company Annual Report
1966*, which the merge folded into **S4202** under the note `same lineage as B1S01`. §T.2 used the bare local id,
so on the harder reading §T.2 named a **parent self-account** as the corpus's only independent origin — inverting
§H.2, which had it right. §T.2 now names **S4215** and states the collision. The same ledger then has to say what
its corroboration cells mean: of 27 cells, exactly two claim a non-zero count and neither has a second source —
**P2-02** `1` and **B05** `1 lineage` at Conf High, both reiterations of one self-account, both restated `0
independent`.

## COR-11 — a 2-significant-figure percent rendered at 8 significant figures, chosen silently

Three printings of one quantity existed at merge: the computed `60,769,935`, B1's `~60,800,000`, and the register's
`60,770,000`. The merge picked the third and said nothing. The value is a quotient of a **rounded** printed
percentage (`an in-crease of 43 percent`), so its honest precision is three significant figures at best; the cell
now reads `60800000` with both superseded renderings named inside it and the choice recorded. Separately: **0**
rows were classed `DERIVED` although **9** carry arithmetic in `derived_arithmetic`. Seven of the nine have been
re-classed `DERIVED` — r4, r11, r12, r15, r57, r58, r59, whose values are computed and printed nowhere. Two stay
`FACT`, deliberately: **r2** and **r30** print their own values and their arithmetic only *checks* a printed
percentage, and a check is not a derivation. Recording the classification rule matters more than the relabelling.

## COR-12 — labels that read a print for something it does not print

Six, each re-read in its carrier before it was moved. **r17**: `CONTEMPORANEOUS` on 1967's `141,824,116`, which is
the *comparative column* inside the FY1968 report (`1968_…` L1356-1363: `Retail sales by operating groups for 1968
and 1967`) — a prior-year column is RESTATED, never contemporaneous. **r60**: a FY1974 roster's `(000) Opened`
column read as "areas in fiscal 1962" (see COR-07). **r11/r25**: circular — 17 Target stores is *derived* from the
group's 19 less 2 hard-goods units, and the group's 19 is then "cross-checked" as the derived 17 plus 2; the
dependency is now stated in both cells and neither row corroborates the other. **r42+r43**: 139,686,954 +
31,256,511 = 170,943,465 against the statement's printed deduction total **171,932,690** (`1965_…` L837), i.e.
989,225 short with no subtotal row in the register; the total is now a row and the residual is named as
unexplained rather than absorbed. **r27**: 868,335 printed at `1969_…` L951 against the same report's segment legs
`607,697 + 233,532 + 27,107 = 868,336` (L1001-1004), a 1-thousand residual now recorded and not smoothed.
**r32, r37, r38**: precision laundering — the print says `an average of more than $7.50` (`1966_…` L214), `a first
mortgage note in the approximate amount of $2,200,000` (L806-807) and `annual rentals of approximately $225,000`
(L809); the qualifier is now in the cell, because a floor and an estimate are not measurements. And **§K.3**
described the per-store divisions as "written once … confidence Medium" while the register carried **two** rows at
**Low**; the prose now matches the register, not the other way round, because the register's Low is what the
carriers support.

## COR-13 — S4203's quote is faithful, and the charge against it is refuted

The audit called the two quoted passages reconstructions. The bytes refute it: `1967_dayton_hudson_djvu.txt`
L1952 is `JOHN F. GEISSE`, so `(L1952)` is a locator; L769-770 print `1967. Target's sales were $86,901,007, an
in-` / `crease of 43 percent`. The auditor found one of the two carrier sentences and missed the other. A repair
pass that "de-fabricated" this citation would have replaced a correct quote with a wrong one, so the quote stands.
What does move is fidelity and format (§14 rule 12): the possessive returns, the locator sits **outside** the
quoted span, and the OCR line-break join at `in-crease` is marked instead of silently repaired. The possessive is
dropped in `sources.csv`'s S4203 `relevant_passage` cell, which belongs to the parallel sources agent — recorded
here as an **outbound correction**, the way COR-02 records its outbound leg, and not edited by this pass.

## COR-14 — a null over a family that was never run is not a null

U.024 said "no family returned an earlier document" and U.019 "no contemporaneous periodical mention" while U.032
and U.033 on the same file record the book corpora and the newspaper back-files as **never searched**. Both rows
are now scoped to the perimeter that actually ran, in the §7 vocabulary: EMPTY-within-perimeter for what was
searched and returned nothing, UNANSWERED for a route that failed, UNTRIED for work not done. A reader who wants
the corpus-wide claim cannot get it from these rows, which is the point.

## COR-15 — a held printed figure the register declared unprinted (opened 2026-09-29 by the second repair pass)

The certifier's B-1. `sources/corporate_print/1967_dayton_hudson_djvu.txt` **L409-412** prints, verbatim:

> `Target has enjoyed substantial growth. Sales`
> `of $86,901,007 in 1967 were 43 percent ahead`
> `of 1966 volume of $60,731,468. Profits in-`
> `creased by 161 percent.`

`60,731,468` occurred **0 times** in `stage_1.md`, `quantitative.csv`, `conflicts.csv`, `data_gaps.csv` and
`timeline.csv` before this entry, while five places in the same two layers affirmatively declared it unprinted —
and the carrier is **S4203**, the layer the §A.1 row cites one line later for 1967 and that COR-13 defended two
days earlier. This is the §14 rule-8 defect class pointed at a number the corpus had already touched.

**What the bytes support, and what they do not.** Printed: fiscal 1966 `60,731,468` and fiscal 1967 `86,901,007`
(both unit-scope), the profit growth `161 percent`, and the estate line at L415-416 `In 1967, Target added
298,600 square feet, / bringing total retail area to 1,184,900 square` — L416 ends at `square` and L417 is blank,
so the unit word after the total is **not printed** and this entry records the truncation rather than repairing it.
Not printed anywhere: a Target **profit dollar** for 1966 or 1967 (so r70 is a rate over an unprinted base, the same
treatment r3/r51 already get), and any Target-unit dollar for 1962-1965, 1968 or 1970-1972. Both year-ends are
printed inside this same layer at L1195-1197 (`the years ended February 3, 1968 / and January 28, 1967 (restated)`),
so `r69` is PERIOD BASIS **RESTATED** and `r71`/`r72` **CONTEMPORANEOUS** without inference.

**Footing, stated rather than smoothed.** The carrier's own division reproduces its own rate: `86,901,007 /
60,731,468 = 1.4309`, i.e. `43 percent`. r15's derivation `86,901,007 / 1.43 = 60,769,935` sits **38,467** (0.06
percent) above the printed base, and the register's `60,800,000` sits **68,532** (0.11 percent) above it — which is
what dividing by a two-significant-figure printed percent costs, and is why r15 survives as a check and not as a
base. The estate pair does **not** foot: `889,000` (r53, fiscal 1966) `+ 298,600` (r72, added in fiscal 1967) `=
1,187,600` against the printed `1,184,900` — a **2,700 square foot** residual inside one basis label across two
consecutive periods, added to the U.012 footing question the register already carries for the FY1974 roster.

**Refusals on this pass.** (i) **U.013's FY1964 leg and `quantitative.csv` r4's "FY1964 Target dollar base is
printed nowhere" are NOT retracted** — no FY1964 Target base appears in any held layer, and finding a 1966 printing
says nothing about 1964. (ii) The correction record's own year list is stated from the lines found here, not from an
exhaustive absence hunt: the 17 PDF image legs of U.030 were never fetched, so "unprinted" means unprinted **in the
held OCR layers**. (iii) The two printings of `86,901,007` in one layer (L409-410 and L769-770) are **one lineage,
two printings** — they are not corroboration, and E02 says so. (iv) No register row was deleted and no value changed:
r15 keeps `60800000`, class `DERIVED`, confidence `Low`, with the withdrawn sentence kept visible in the cell (§14
rule 4).

## COR-16 — the canonical volume taught withdrawn dates by silent presence (opened 2026-09-29, blocker B-2)

COR-07 and COR-08 fixed the **values** in the root CSVs and the fix was real — measured on the repaired bytes, zero
`-12-31` strings survive in any date column of `quantitative.csv` or `timeline.csv`. What no earlier pass had done
was mark the copies of those rows that the merge carried **into** `stage_1.md` as pre-repair emission slices.
`grep -ci superseded stage_1.md` and `grep -ci "do not re-apply" stage_1.md` were both **0** before this entry: the
warning lived only in `_parts/s1_p1.md`, `_parts/s1_p2.md` and `stage_1_index.md`, while the volume the index calls
canonical printed nine rows asserting dates the corpus had already retracted — the `1975-12-31` basis-migration row
(COR-08) and seven December year-ends plus the December timeline recap row (COR-07). A register row is read as a
register; a row inside a *volume* is read as prose by whoever next opens the file, which is §14 rule 10's
highest-severity home for a stale claim.

**Fix = mark, not delete and not revalue.** §14 rule 4 says nothing is a cleanup target, and RD-122 makes these
slices the merge's byte-identical audit trail, so deleting or re-dating them would have destroyed the proof of the
merge and silently rewritten history. Two dated **SUPERSEDED — DO NOT RE-APPLY** blocks now sit at the two
`REGISTER ROWS FOR MERGE` banners (volume 1 and volume 2), declaring the nine root CSVs canonical, declaring the
slices pre-repair, and naming the carrier lines that print the real year-ends (`1973_…` L172-174, `1969_…` L1488,
`1974_…` L147-148, `1975_…` L3246-3251); each of the **nine** rows carries its withdrawal inside its own `notes`
cell, so a reader who copies one row copies the retraction with it. Measured after the pass: **9 of 9** December and
`1975-12-31` rows in the volume carry `DO NOT RE-APPLY`, and **2** banners carry `SUPERSEDED`.

Outbound and **not fixed here**: the same slices also pre-date **COR-15** (they still print "Target dollars only for
1967") and **COR-18** (they still print U.032's tier-lift expectation). Rather than revalue a slice, each banner
names those ids and states that the sentences below are withdrawn readings. The `_parts/` prose was not touched at
all (this pass's brief bars it); `MASTER_RESEARCH_LOG.md` was not touched; no date in a root CSV was changed by this
entry, because none needed changing.

## COR-17 — five register findings that never became prose (opened 2026-09-29, blocker B-3)

RD-105/106 taught the corpus one direction of this failure — a prose claim the registers refuse to carry. This is
the same failure **one layer down**: the repair pass that fixed COR-09 and COR-12 wrote `Reaches: … stage_1.md §K.3,
§E.2, §P` into this file, and the volume did not contain the findings. Measured before the present entry, each of
`989,225`, `171,932,690`, `220,511,038`, `1,088,338,000`, `868,336` occurred **0 times** in `stage_1.md`, and all
five occurred in `quantitative.csv`. The `corrections` gate could not see it: it tests whether an **id** appears in
both layers, and COR-09/COR-12's ids did appear. So the record here is a withdrawal of the *propagation claim*, not
of the findings, and a standing note that a `Reaches` cell is a promise to be measured, not a measurement.

**What was added, all of it already printed.** §K.2 now carries two rows: the deduction total **`171,932,690`**
(`1965_…` L837) and the residual it exposes — `139,686,954` (L944) + `31,256,511` (L945) = `170,943,465`, which is
**`989,225` short**, named as an unexplained reclassification with **no plugged figure invented**. §K.3 now contrasts
that with the FY1973 five-year row, which **does** foot to itself, so a later reader cannot confuse "internally
consistent" with "true". §E.2 now states both restatement deltas — `220,511,038` against the FY1966 report's
`217,961,635` (delta `2,549,403`, `1967_…` L819) and `1,088,338,000` against the FY1971 report's `1,086.4` million
(delta about `1,938,000`, `1972_…` L10) — and writes the rule they force: **no growth rate may cross
FY1966→FY1967 or FY1971→FY1972 without naming which restatement it used**, with both quotients shown
(`19.37` / `17.99` percent, and `16.23` / `16.03` percent) against the printed `18 percent` and `16.0%`, which chose
the restated bases. §P.1 names r27's `868,336` component sum (`607,697 + 233,532 + 27,107`, `1969_…` L1001-1004)
against the printed `868,335` (L951), the 1-thousand residual inside the retail legs only, and marks L1002's row
label as OCR-corrupt so the word `specialty` is not read off the bytes as a print.

**Refusals.** No value, class or confidence moved in any register on this entry; the prose is the missing leg, and
plugging `989,225` with a plausible component would have been a fabrication. The `_parts/` slices and the volume's
emission rows were left as emitted (COR-16's rule).

## COR-18 — a tier expectation the corpus's only measurement of the route does not support (opened 2026-09-29, blocker B-4)

An expectation cell is not a finding, but it *is* read as one: `data_gaps.csv` U.032 said HathiTrust "is the route
most likely to lift the tier from T2 to T1", the volume repeated it at §U.2 and (§H.5) called it "the only route that
can move the tier from T2 to T1", and **no source was cited** — `RD-127` appeared **0 times** anywhere in this company
directory, including in the two files that make tier claims. RD-127 exists and it measured this exact route: on the
**company** phrase, every dated result on the returned first page is **1990-2014**; the rich 1950s pool is the
**sector** query (`"five and dime" variety store` → 97 records 1950-1959), i.e. documents *about the trade* rather
than namings of a registrant — and §15.2 counts a family only when it returns **in-window Tier-1 text about the
company**, so the sector pool would not lift anything.

**What the entry does and does not say.** It does **not** close the route: the 6 undated rows on the company phrase,
the 4 facet records whose `Published` field the parser did not extract, and every result page past the first are
unexamined, so "the first page returned nothing pre-1990" is the honest limit of the measurement. The route stays
**UNTRIED** with its command named. It does say that a T1 re-derivation requires an **in-window company-naming**
Tier-1 text from a **third family**, that the corpus has no basis for calling HathiTrust the most likely source of
one, and that the `target` task set in `tools/queries.json` must be added by the **orchestrator** — `tools/` is
outside this pass's write scope and outside every agent's, exactly as §U already states. Written so a later agent
counts this row as an open route and **not** as a live tier ladder.

**T2 core itself is not re-derived here.** The certifier's Check 5 re-measured the family census (filings: nothing
before 1994; web archives: nothing before the mid-1990s; corporate print: 11 in-window layers; trade periodicals: one
held leg that does not name the company; auction/museum: UNTRIED) and Target stays **T2 on evidence**, which this
entry neither contradicts nor re-litigates.

## COR-19 — four Tier-1 stamps on retrieval artefacts, and the claims that hid behind them (opened 2026-09-30)

The queued sources work landed on this pass because no other agent owns it now. Everything below was verified against
the bytes at `archived_url` before a cell moved; the register has 18 columns and the pointer is `archived_url` — that
header was enumerated first, because four passes this run have been undone by an assumed column name.

**The tiers.** `S4218` (four 7,747 B SEC error pages), `S4219` (four 1,018-1,021 B full-text-search responses whose
only content is `"hits":{"total":{"value":0`), `S4220` (two 11,832 B Internet Archive "Temporarily Offline" bodies)
and `S4221` (the intake tool's own `sources/sec/_MANIFEST.csv`, 40 bytes, a header line and nothing else) all carried
**tier 1**. A retrieval artefact is Tier 3 at most, and a body that never arrived witnesses nothing about the world —
what it witnesses is that a route was run and failed. **The inflation is demonstrably merge-created:** the pre-merge
sibling that covered these identical bytes at the identical moment, `P1S08`, was stamped **tier 3**, and that `3`
still prints in the volume's own emission slice one screen above the register's `1`. All four are now **3**, and the
`evidence_class` cells (`UNANSWERED - dead route`, `INDEX FLOOR - not a null`) were already honest — the tier was the
lie, not the class.

**The status codes, stated stricter than the brief.** The brief said the bodies print `500`/`temporarily` where the
rows assert `503`. Measured: **the bodies print no status code at all.** The single `500` token in `dayton+hudson.atom`
is inside `Raleway:300,400,500,600:latin` — a CSS font-weight list in a script block — and the single `500` in
`cdx_targetcom.txt` is `width:500px` in a style attribute. What the pages actually say, in visible text, is
`SEC.gov | File Unavailable … This page is temporarily unavailable.` and `Internet Archive: Temporarily Offline`. No
HTTP response line was ever captured and **no provenance sidecar exists** for any `name_search/` or `web_archive/`
file, so the code is written **UNKNOWN** in the rows and in U.025/U.026, never a plausible number. This matters
downstream: a rate limit and a service-down carry different retry advice, and inventing either would have destroyed
that distinction rather than recording it.

**Independence (three cells).** `S4211` claimed independence for the FY1975 registrant report because *a third party
scanned it* — a digitisation vendor is a conduit, not an origin, and the layer is the same filer's self-account inside
the same item as `S4201`-`S4210`; the cell now says so and the row's `claim_supported` no longer reads `context only`
while `timeline.csv` row 17 rests its Fiscal Year fact on it. `S4217`'s merged note `independent of the company` was
restored to the pre-merge limit (the registrant's own index; cannot witness anything before its own floor).
`S4209`'s lineage cell said `same lineage as S4208/S4209` — naming itself — and its title opened with a stray `U `
merge seam; both rewritten.

**Bookkeeping, no evidentiary movement.** `S4207`/`S4209`/`S4210` now carry in `archived_url` the
`UNVERIFIED TLS` stamp their own sidecars print, which 2 of 5 rows had: a reader of `sources.csv` alone could not
apply U.037's cap. **No confidence moved on any of them** — re-measured, all 38 register rows citing those five
layers sit at Medium or Low and **zero** at High, so the cap already binds and this is registration, not revaluation.
`S4203`'s passage cell got COR-13's outbound leg applied (the possessive `Target’s` restored, `(L1952)` moved outside
the quoted span, the OCR join marked) **plus** the four L409-412/L415-416 passages COR-15 found; the refutation of the
fabrication charge stands untouched and nothing in the citation was "de-fabricated".

## COR-20 — an index file that claimed to be the source of truth, and 19 held files no row pointed at (opened 2026-09-30)

**The set difference, with the method quoted** because the number is the finding: every file under `sources/` that is
not a `.meta.json` sidecar (36 files), minus every file whose exact `sources/…` path appears in some row's
`archived_url` — measured with the header enumerated first and no basename, glob or fuzzy matching. **19 before, 0
after.** Of the 19: eleven were named only by an abbreviated fragment or a glob inside a compound cell
(`_INDEX.md`, `submissions.csv`, three of the four `name_search/*.atom`, all four `fts_*.json`, `cdx_dhc.txt`), so
they were findable by a human and invisible to a machine check; eight were named by nothing — the FY1998 and FY2000
print layers, `submissions.json`, `meta_chain-store-age.json`, `q_corp_title.json`, `q_corp_creator.json`,
`q_csa.json`, `q_dsn.json`. The exact four paths are now spelled out in S4217-S4220 as well.

**`_INDEX.md` L5-6** read `This file is the source of truth for what exists. Do not re-search EDGAR for coverage;
grep submissions.csv and report a form as absent only from this list.` It is true for CIK 27419 from 1994-02-10
forward (the arithmetic reproduces: 1,000 recent + 1,628 sliced = 2,628) and says nothing about any predecessor CIK,
which is not what it reads as — and it sits in the instruction layer, where §14 rule 10 puts the highest severity. It
is reworded to state what it enumerates, what it cannot answer, and how it goes stale. **Outbound:** the file is
generated by `tools/sec_intake.py`; `tools/` is outside this pass's write scope, so unless the orchestrator fixes the
template the next build overwrites this correction.

**Decisions on the artefacts, made as sets.** The five `ia_search` bodies became **one row S4222 at Tier 3**: they
are one search leg, none contains a word about the company, and they were kept rather than deleted because
`q_dsn.json` is the bytes behind §H.4 N7's `Discount Store News numFound 0`. The derived EDGAR trio became **S4223 at
Tier 2** — the SEC's own bytes are Tier 1 and are already registered as S4217; a rewrite by our own tool is not a
second source, and the tool discards `formerNames`, which is exactly why S4217 exists. The FY1998 and FY2000 layers
became **S4224/S4225: Tier 1 carriers, `(PB)` evidence, Low**, because §5 tiers are properties of carriers (they are
annual reports) while their evidentiary weight here is post-boundary name-change trace only; every string claimed was
opened first — `www.dhc.com` twice in 1998 (L4224, L4284) with `Target Corporation` zero times, `Target Corporation
Annual Report 2000` at 2000 L1 with `www.target.com` at L3743/L3827 and `1962` zero times.

**Refused.** Re-tiering `S4216` (Internet Archive catalogue metadata, High) and `S4217` itself, which audit 2 also
called inflated: not directed by this brief, and a tier change on a row the registers cite for three live gaps needs
its own evidentiary pass, not a repair by-product. Their class cells already limit them. `S4213`/`S4214` keep tiers
2 and 4 on documents never opened — audit 2 graded that low-severity and the rows refuse evidentiary use as written.
Handed to the next sources pass.
