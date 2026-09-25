# amazon_s2_blocker_repairs.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T19:28:34Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## B1 retraction

STATUS: WRITTEN (repair pass, 2026-09-26)

**What was asserted, and what the document prints.** `stage_2_part_3.md` **§U.113a** CLAIM B (as minted 2026-09-26,
RD-079) read: "S-1 (orig.), filed **1997-03-24**, states a range and an assumption in one breath — 'is currently
estimated that the initial public offering price will be between …' (l.191)". Re-read byte-for-byte at the primary
layer, `sources/S-1_original_acc-0000891618-97-001309_filed-1997-03-24.txt` l.208–209 prints: "It / is currently
estimated that the initial public offering price will be between / **$     and $     per share.**" — **two blank price
fields**. The original states no range. The quotation was real up to the ellipsis and false across it: the elided bytes
were the refutation.

**Repair executed (Stage-2 text, my paths).**
1. `stage_2_part_3.md` §U.113a now opens with a visible **`⟪COR-16 SUPERSEDES THIS BLOCK'S CLAIM B AND ITS
   CITATIONS — 2026-09-26⟫`** marker that prints the withdrawn sentence verbatim (supersede, do not erase, §14 rule 4).
   Block id, lettering and CLAIM A are unchanged; nothing renumbered (§9.3).
2. CLAIM B **re-stated from the documents**, not softened: (i) original 1997-03-24 = blank range field (l.208–209)
   standing next to a filled registration-fee/dilution assumption of $13.00 (fee table l.166; pro-forma l.1221), with
   the DERIVED check 2,875,000 × $13.00 = $37,375,000 printed as exact and the 2,500,000 + 375,000 option reconciled at
   l.170–171; (ii) **No. 1, 1997-04-21 = first accession to print a range** ($12.00–$14.00, l.247–248) on the same face
   as the raised $14.00 fee-table assumption (l.192) while its pro-forma still runs $13.00 (l.1365); No. 2 repeats the
   state (l.234–235 / l.183 / l.1330); (iii) No. 3, 1997-05-09 unchanged range (l.222–223) / $14.00 cover (l.173) /
   $13.00 pro-forma at five sites.
3. **Pointers re-keyed twin → keyed** per `stage_2_index.md`'s declared `twin = keyed − 17`: l.191 → **l.208**,
   l.149 → **l.166**, l.1204 → **l.1221**.
4. **Correction TO the certifier, not just of the text:** audit6 l.102 asserts the No. 3 cite "(l.1230)" is "POINTER
   WRONG BY 60". It is **not**: grep of No. 3 puts "$13.00 per share" at l.408, l.1188, **l.1230**, l.1290, l.1300, and
   l.1230 is inside the CAPITALIZATION pro-forma description, which is what the block said it was. So **three** pointer
   defects, not four — matching `MASTER_RESEARCH_LOG.md` RD-094 ("three of its line cites miss the quoted text by
   −17"). l.1230 stays cited. The audit sheet is not mine to edit; handed off below.
5. The block's own over-claim "no accession between No. 3 and the 424B1 was read for this block" is corrected in
   RESIDUAL UNCERTAINTY — Nos. 4/5/6 are read at §Q l.101–104 of the same volume.
6. **What the blank field is recorded as establishing** (the finding, per brief): as filed 1997-03-24 the registrant had
   not set a range; the $13.00 on the same page is a fee/pro-forma computation, not a stated price. **Why the field was
   left blank while the fee table was filled is UNKNOWN** — no document in `sources/` states a reason; no market
   practice is substituted for it (§6, repair rule 1).
7. **The narrative my predecessor "corrected" was right and is confirmed, not re-touched:** `stage_2_part_1.md` l.56
   ("blank (24 Mar, S-1 orig.) → $12.00–$14.00 on 2,500,000 (No. 1, 21 Apr l.247–248 …)") and l.82 ("range left BLANK
   (S-1 original, 1997-03-24)"), plus `stage_2_part_3.md` §Q l.97 and `amazon_s2_audit4_repairs.md` §4 item 2. All
   re-verified against No. 1's bytes: range at l.247–248, fee table $14.00 at l.192. No edit made to any of them.

**Register side (B1, not applied by me):** `conflicts.csv` row 170 (`stage2`, U.113a) carries the same false proposition
and the same twin pointers → rewritten 15-field row in `## Register handoff`.

## B2-B4 residue

STATUS: WRITTEN (B2, B3, B5, B7, B8 repaired in owned text; B4 handed off; B6 reclassified)

* **B2 — `0.194995`/`19.4995` (D-06 residue). FIXED, 2 sites.** `stage_2_part_2.md` **§P.2 s4** and
  `stage_2_claim_records.md` record **P26** now print `28,813 ÷ 147,758 = 0.1950013`, with the superseded value kept
  visible in the same cell as a residue note. Re-derived at the primary layer, not copied from the audit: 10-K405
  **l.1402** prints gross profit `$28,813`, **l.1403** prints `Gross margin ...... 19.5%`, **l.1177** prints net sales
  `$147,758`; 28,813 ÷ 147,758 = 0.19500129. Both the false and the true quotient round to 19.5%, which is why the error
  survived five passes — it never broke a total. **Nothing was substituted or back-solved** (repair rule 1).
* **B2 did not grow.** The audit's Untried-3 sites were read: records **P16** (`3,459 ÷ 15,746 = 0.219674 → 22.0%`) and
  **P23** carry no false quotient — the regex caught correct quotients with similar tails. Line numbers moved under my
  edits; these are addressed by record id (§14.12), which is why I did not re-cite them by line.
* **B3 — U.67 "the filed figures give 2,448,000 …". FIXED.** `stage_2_claim_records_part_2.md` record **U.67** now reads
  "**the transcribed, not-on-disk B&N numerator over the filed Amazon denominators**" with the reason inside the record
  (D-11: zero grep hits for 2,448 under `sources/`; S2009 `local_copy: NO`) and the two ratios kept arithmetically
  correct / epistemically UNKNOWN. Denominators re-verified filed at 10-K405 l.1177.
* **B4 — `sources.csv` S2009. NOT EDITED (live register owner); full replacement row in `## Register handoff`.**
  `FACT (audited counterparty)` + `High` on a row that also says `not held locally` → **FACT (the filing exists) /
  UNKNOWN (its contents)** + **Low / UNKNOWN** split, and its `relevant_passage` (`'stocking over 400,000 titles'`)
  marked **NOT VERIFIABLE AT THE CITATION** — the same family as B1: a quotation offered as evidence from a document the
  corpus cannot open. Independence of origin kept; independence of verifiability never existed.
* **B5 — unbounded superlative. FIXED.** Record **K19** now carries the bounded form its sibling **N13** already used
  ("on the filed record and bounded to this stage's own boundary (1997-05-15)"), names what the unbounded claim would
  require (post-boundary converts; the 1997-12-23 $75,000,000 facility this volume itself carries), and moves that
  clause's class to **INFERENCE (bounded superlative)**. No act, term, price or date changed.
* **B6 — RECLASSIFIED: a gate artifact, not a row defect.** All **170** `conflicts.csv` rows parse at **15 fields**
  under RFC-4180 (`csv.excel`, `doublequote=True`) and the current `csv` gate reports **Findings: 0 | Passes: 14**.
  Reading rows 135/170/171 with `doublequote=False` reproduces **exactly 16/18/17** — the behaviour
  `tools/gates.py::read_rows`' own docstring records as having invented "43 width-drift findings that did not exist".
  **No width repair is handed off: applying one would corrupt valid rows.** What does travel with B6 is content —
  row 170's `claim_a_date` holding prose (§13 wants ISO) and its `*_source` cells carrying `§T l.97-104` (line numbers as
  addresses, §14.12) — both fixed in the rewritten row. Also corrected: the audit attributes line 135 to "the
  D-10/U.107 row"; **U.107 is at physical line 108** and line 135 is `P-U.134`, a **stage3** row.
* **B7 — index and counts. FIXED in `stage_2_index.md` + volume 2's own coverage note.** Measured: **72** §U blocks;
  `conflicts.csv` **170** data rows = 43 `stage1` / **72 `stage2`** / 55 `stage3` (the index's "70 rows and stays there
  until the register owner appends" is superseded in place with the old wording kept visible); claim records
  **305 + 105 + 72 = 482** (the "411 in volume 1 / 481 in all" and "479 on disk" self-counts were both wrong after the
  §9.3 split); the two minted §U records close the 72-blocks-against-70-records gap. **The §9.2 hard-cap breach (T1,
  `stage_2_claim_records.md` 60,718 words) no longer exists on disk**: measured **44,766** post-edit, and every Stage-2
  volume passes `budget` (max `stage_2_part_3.md` 46,016). Nothing was trimmed to fit (§9.6 forbids it) — the split pass
  did the geometry work; the index's stale word columns are replaced with measured ones.
* **Pointer defect found by this pass, not by the audit:** §U.113b cited FY1998 10-K **l.1243** for the restated
  per-share line; **l.1243 is the totals rule `========`** and the digits are at **l.1244**. Fixed in the narrative and
  in the handed-off U.113b row. Conversely the audit's "pointer wrong by 60" challenge to §U.113a's **No. 3 l.1230** is
  **rejected**: grep of No. 3 puts "$13.00 per share" at l.408, l.1188, **l.1230**, l.1290, l.1300 — the cite is exact,
  so three pointers were inverted, not four (matching `MASTER_RESEARCH_LOG.md` RD-094).
* **B8 — the authorised-capital record. CLOSED.** Minted **B125** after reading the documents: pre-increase authorisation
  is filed in S-1 (orig.) Note "Reincorporation" **l.3813–3816** and Exhibit 3.1 Art. 4 **l.5192–5194** (5,000,000
  preferred / 25,000,000 common, $0.01 par); the increase is filed as board-approved "In March 1997", **subject to
  stockholder approval**, "to be effected prior to the closing" (**l.4075–4080**, summary l.280–283); the **1997-04-18
  effecting date exists only in No. 1** (**l.4590–4593**, in the same sentence as the three-for-two split) with the new
  totals at l.3306–3307 and l.1313. `stage_2_part_1.md` §B.0's legal-form cell now points at B125 and says which
  accession files which half; the two gap declarations (`part_2` item 6, `part_1b` §S.9 list) are marked CLOSED with the
  old wording kept. Id corrected per the certifier: **RD-049, not RD-072**. **UNKNOWN and deliberately not filled:** the
  stockholder-approval date and the purpose of the increase.

## Sibling sweeps

STATUS: WRITTEN. Whole-corpus sweeps (all stages, both indexes, appendices, the nine registers, `_parts/`, `research/`,
QC sheets) run **after** each fix, by literal digits and by construction; `sources/` excluded (evidence layer, not
corpus). Every hit classified: **correct / quoted-source / retraction / stale**.

| # | Class | Patterns | Corpus hits | In Stage-2 owned text | Retraction / superseded print | Correct-or-quoted elsewhere | **LIVE STALE** |
|---|---|---|---|---|---|---|---|
| B1 | false "states a range" + twin cites | `states a range`, `one breath`, `l.191`, `(l.149)`, `(l.1204)`, `range sentence` | 32 | 12 — every one a COR-16 marker, a re-key note, or the superseded wording printed inside a withdrawal | 11 | 9 — `conflicts.csv` row 170 (**handed off**), audit6 sheet, `MASTER_RESEARCH_LOG.md` RD-094 (already honest) | **0 in Stage-2 text**; 1 register row handed off |
| B2 | false margin quotient | `0.194995`, `19.4995` | 22 | 6 — `quantitative.csv` L124, §P80a l.530, §U.52 l.515, U.52 record, §P.2 s4, record P26: all now `0.1950013` or residue-marked | 10 | `_parts/s2_p4.md` ×5 + `_parts/s3_p4.md` ×3 fenced SUPERSEDED (T8, untouched); QC sheets ×12 | **0 Stage-2**; **6 downstream → `## Stage-3 handoff debt`** |
| B3 | B&N numerator called filed | `filed figures`, `2,448,000`, `2.448` | 17 | 2 (rewritten U.67 + COR-16 list) | 5 | `stage_1.md` l.2044/l.2058 use "the filed figures" for **other genuinely filed** arithmetic — correct, not siblings; `conflicts.csv` U.67 already "transcribed"; dossier layer | **0** |
| B4 | non-local witness @ audited+High | `FACT (audited counterparty)`, `local_copy: NO` | 12 | 0 in prose | — | `sources.csv` **S2009** (handed off); Stage-1 rows S0410/S0607 (other stage's owner) | **1 register row → handoff** |
| B5 | whole-life superlative | `cheapest capital`, `ever raised`/`EVER RAISED` | 8 | 4 — K19, N13, `part_1` §H.1, `part_2` decisions row, all bounded to 1997-05-15 | 6 | `_parts` ×2 fenced; `research/ST2_B_finance.md` (dossier layer) | **0** |
| B6 | row parse / width | field count under two dialects | 170 rows | n/a | n/a | 170/170 rows at 15 fields (fixed reader); 16/18/17 only under the retired `doublequote=False` reader | **0 — reclassified, no repair applied or requested** |
| B7 | §U blocks vs records vs rows | `^\*\*U\.[0-9]+[a-z]? —`, `^[A-T]{1,2}[0-9]{2,3} Claim:`, stage tallies | 72 / 482 / 170 | index, coverage note, part list all re-measured | — | Stage-1/3 tallies untouched | **0** |
| B8 | authorisation assertion | `25,000,000→100,000,000`, `5,000,000→10,000,000`, `1997-04-18`, `authorised capital` | — | 1 record minted, 1 cell re-pointed, 2 gap lines closed | 2 | S-1 orig. l.280–283/l.4075–4080/l.5192–5194; No. 1 l.4590–4593 are source lines; `quantitative.csv` L187 carries splits only | **0** |
| untouchables (instruction 5) | `257`, `30.81409`, `0.2549989`, `14.0500004`, `39.5690`/`≈39.5`, restatement set, U.114/U.115 re-key | re-measured only | — | all sites still in the auditor-certified form | — | — | **0 — no churn applied** |

## Register handoff

STATUS: WRITTEN. **Nothing here was applied by this pass** - the nine registers are held by the live register owner
(`amazon_s2_register_owner.md`), and repair rule 4 / method 14 rule 6 forbid editing through a live owner. Three **full
replacement rows**, generated with `csv.writer` in each target file's exact column order (`conflicts.csv` 15 fields,
`sources.csv` 18), one line per row, and every emitted line re-parsed back to the header width before it was pasted
here. Apply as **replacements** at physical lines **170** and **171** of `conflicts.csv` and at the **S2009** row of
`sources.csv` - do not append: both U.113 rows already exist, and duplicating `conflict_id` / `source_id` is exactly the
defect 13 keys on. **No width repair is requested for rows 135/170/171** (see B6: they parse at 15 fields and the
audit's 16/18/17 came from the retired dialect-sniffing gate; re-quoting them would break valid rows). In the U.113a row
`claim_a_date` moves from prose to two ISO dates (13), and the line-number-as-address cites in its `*_source` cells
become label addresses carrying the keyed line numbers beside them (14.12). **No figure in the S2009 row changes** - only
class, confidence, and a verifiability annotation on a passage that cannot be checked.

### conflicts.csv - replacement for row 170 (15 fields, header order)

```
"Amazon.com, Inc.",stage2,U.113a,T; P; A.3; D.6,"Earlier draft: the range was stated once as the ""first stated range""; the price settled ""the same morning"" / over ""five days""; the range-carrying accession was ""obsolete on its own filing date""",stage_2_part_3.md U.113a CLAIM A; the Q rows dated 1997-04-21 / 1997-05-09 / 1997-05-13 / 1997-05-14; stage_2_part_1.md A.3 deal row and price-walk paragraph; claim records U.45 / U.98 (struck wording; no document under sources/ carries any of the four phrases),1997-03-24; 1997-05-15,"Re-stated by COR-16 (2026-09-26) after this row's first form was contradicted by its own cited line. The S-1 original (1997-03-24) states NO range: its range sentence prints two BLANK price fields (between $   and $   per share, l.208-209) while the same document's registration-fee table prints 2,875,000 shares at a $13.00 assumption for $37,375,000 (l.166; 2,875,000 x 13.00 = 37,375,000 exact; the count is the offering's 2,500,000 plus the underwriters' 375,000 option, l.170-171) and its dilution table repeats Assumed initial public offering price per share ... $13.00 (l.1221). S-1/A No. 1 (1997-04-21) is the FIRST accession to print a range, between $12.00 and $14.00 per share (l.247-248), in the same document whose fee table already raises the assumption to $14.00 on 2,875,000 shares for $40,250,000 (l.192) while its pro-forma still runs $13.00 (l.1365). No. 2 (1997-04-29) repeats the state (l.234-235 / l.183 / l.1330). No. 3 (1997-05-09) re-prints the range unchanged (l.222-223) with the $14.00 cover (l.173) and $13.00 per share still running through its pro-forma and capitalization sections (l.408, l.1188, l.1230, l.1290, l.1300). Superseded wording kept visible: S-1 orig. (1997-03-24) states an estimated range at l.191 while its cover prints $13.00 ... (l.149) and pro-forma repeats $13.00 (l.1204) - WITHDRAWN.",sources/S-1_original_acc-0000891618-97-001309_filed-1997-03-24.txt l.208-209 / l.166 / l.1221 / l.170-171; sources/S-1A-No1_acc-0000891020-97-000603_filed-1997-04-21.txt l.247-248 / l.192 / l.1365; sources/S-1A-No2_acc-0000891020-97-000659_filed-1997-04-29.txt l.234-235 / l.183 / l.1330; sources/S-1A-No3_acc-0000891020-97-000755_filed-1997-05-09.txt l.222-223 / l.173 / l.1230 - keyed headered line numbers re-read at the line 2026-09-26 (twin = keyed - 17 per stage_2_index.md),1997-03-24; 1997-04-21; 1997-04-29; 1997-05-09,"Two failures, one per pass. The earlier draft compressed a documentary process: the lineage is ONE source family, each amendment re-prints its predecessor's sentence while re-striking the cover numbers, so taking the cover figure from one accession and the range sentence from another yields two states at once, and that draft resolved it by declaring one obsolete and collapsing six weeks into a morning. The minted row read the sentence FRAME (will be between) as evidence of its CONTENT, quoted across an ellipsis whose elided bytes are the two blank fields, and cited twin line numbers against keyed paths. The wording policed here was current in Stage 2 from 2026-09-24 and struck 2026-09-25; the correcting row was minted 2026-09-26 and superseded the same day by COR-16","B (re-stated) - eleven filed lines across FOUR accessions, each read at the keyed line, plus the filing dates on their faces. A carries no document at all. All four accessions are one registration lineage (File 333-23795), so the method's filing-lineage rule caps this at what one instrument supports","A walk with stated intermediate states, each keyed to its accession and date: blank range field plus $13.00 fee assumption (24 Mar) -> first stated range $12.00-$14.00 with the cover already at $14.00 (No. 1, 21 Apr) -> re-printed unchanged (Nos. 2, 3) -> range and size raised (No. 4, 13 May) -> $18.00 (424B1, 15 May). $13.00 and $14.00 are ASSUMPTIONS, never prices. No same morning, no five days, no first-stated-range at No. 3, no obsolete-on-its-own-filing-date. The narrative stage_2_part_1.md A.3 carries (blank 24 Mar -> $12.00-$14.00 at No. 1, 21 Apr) is CONFIRMED correct; the block that contradicted it is withdrawn","UNKNOWN: why the range field was blank while the fee table was filled (no document in sources/ states a reason and none is inferred); the day-part of the price fix (no document states an hour for any 13-15 May 1997 event); who directed each change (stays at U.98). NO LONGER uncertain: which accession first printed a range - No. 1, 1997-04-21 - and Nos. 4/5/6 were read, correcting this row's claim that nothing between No. 3 and the 424B1 was read","High (the eleven re-keyed filed lines); High (that the 1997-03-24 original states no range - the blanks are on its face, l.208-209); High (the four struck phrases have no document); Medium (that the $14.00 assumption moving to the range ceiling was deliberate - no document states intent); UNKNOWN (reason for the blank field; price-fixing day-part)"
```

### conflicts.csv - replacement for row 171 (15 fields)

```
"Amazon.com, Inc.",stage2,U.113b,P; A; L; M; R; K,"FY1997 10-K405 (filed 1998-03-30) reports FY1997 net loss $(27,590)k and FY1996 $(5,777)k (l.1192), opex 58,022/9,438/406/52 (l.1186), restating the pair under ""Net loss - as reported ... $(27,590) $(5,777) $(303)"" (l.2586). Every FY1996 figure Stage 2 argues from is this as-filed set",sources/10-K_FY1997_acc-0000891020-98-000448_filed-1998-03-30.txt l.1192/l.1186/l.2586,1998-03-30,"The issuer next reprints both years at larger losses: FY1998 10-K (1999-03-05) prints net loss $(124,546) $(31,020) $(6,246) (l.1242) with basic/diluted LPS (0.84)(0.24)(0.06) (l.1244 - re-keyed 2026-09-26 by COR-16: l.1243 is the totals rule and prints no digits); FY1999 10-K (2000-03-23) repeats the identical re-based pair (l.1761, l.1765-1766) on 260,682k/222,542k shares","sources/10-K_FY1998_acc-0000891020-99-000375_filed-1999-03-05.txt l.1242 (net loss row) and l.1244 (basic and diluted loss per share); sources/10-K_FY1999_acc-0000891020-00-000622_filed-2000-03-23.txt l.1761, l.1765-1766. Every line re-read at the keyed file 2026-09-26; the claim_a lines 10-K405 l.1186 / l.1192 / l.2586 likewise re-read and byte-present, closing this certifier's UNTRIED-at-document-level note on this row",1999-03-05; 2000-03-23,"A restatement, not a contradiction: the later annual reports re-base comparatives (PlanetAll pooling and the pre-IPO option/S-1 reconciliation). Net sales, cost of sales and gross profit are identical across all four instruments, so the movement is below the gross-profit line; FY1996 delta +$469k foots as +$464k inside total operating expense and +$5k interest, FY1997 delta +$3,430k","Both sides are Tier-1 issuer documents of one lineage. A is the as-filed state Stage 2 must argue from; B is the issuer own later re-basing of that same audited year, printed twice more","Print both witnesses side by side, label as-filed vs re-based, never average, never call either ""the figure"". The stage claim stands on the as-filed set; the re-based pair is disclosed because it changes every per-share and margin comparison drawn across the boundary","The reconciling note and the cause of the movement are not in sources/ (recorded as unreconciled locally); audit-5 L-2 claim that the delta is entirely below the operating line is wrong and total operating expense moves 9,438 -> 9,902",High (both states printed and line-cited); UNKNOWN (the reconciling disclosure)
```

### sources.csv - replacement for the S2009 row (18 fields)

```
S2009,stage2,"Barnes and Noble's own audited account of the same universe Amazon counted: 431 superstores in 47 states plus DC (91 opened, 18 closed) and 577 mall stores down from 781 in FY1993; revenues 2.448bn (+23.8%) and net earnings 51.2m for the 53 weeks ended 1997-02-01 after a prior-year net loss of 52.976m; comps +7.3%; about 9% of the consumer market; store stock about 130000 titles with special order from more than 1.2 million books in print; and a 344000 sq ft South Brunswick NJ distribution centre opened September 1996 stocking over 400000 titles for overnight delivery at very deep discounts","Barnes & Noble, Inc. Form 10-K for the 52/53 weeks ended February 1, 1997, accession 0000889812-97-001072","Barnes & Noble, Inc. (SEC)",SEC annual report of a competitor,Primary,FY1997 (weeks ended 1997-02-01),1997-05-02,UNTRIED at first hand (read through research/ST2_C_market_competition.md S2C-17 to S2C-21),https://www.sec.gov/Archives/edgar/data/890491/000088981297001072/0000889812-97-001072.txt,not held locally,1,"FACT (the filing exists, accession 0000889812-97-001072) / UNKNOWN (its CONTENTS - no byte under sources/; every figure here is a dossier transcription of a temporary read, S2C-17 to S2C-21). Reclassed from FACT (audited counterparty) by COR-16, 2026-09-26, to match quantitative.csv L181/L182 and stage_2 P164, which already carry this witness as UNKNOWN (AUDIT-3 D-11)","Low (that a B&N Form 10-K for the 53 weeks ended 1997-02-01 exists); UNKNOWN (the store counts, the 2.448bn revenue, the 51.2m earnings, the 52.976m prior-year loss - none verifiable at the citation). This row formerly read FACT (audited counterparty) + High on the same line as not held locally, which is AUDIT-6 B4: a transcription with no bytes cannot carry High under the method's independence rule","High | INDEPENDENCE IS OF ORIGIN ONLY, NOT OF VERIFIABILITY - different registrant, different auditor, no common drafter, but no local copy, so it corroborates nothing a Stage-2 row may raise a confidence on (D-11, COR-16)","NOT VERIFIABLE AT THE CITATION - the string stocking over 400,000 titles comes from the dossier transcription and is not quoted from any document on disk; it may not be used as filed wording. Same failure family as U.113a's ellipsis: a quotation offered as evidence from a text the corpus cannot open","Basis warning carried in every dependent row: the 53-week period ending 1997-02-01 is NOT coterminous with Amazon's calendar FY1996, so no like-for-like pairing is printed (S2P4 U.66 U.67 U.80). | local_copy: NO (no byte in sources/ - the witness is read only through a dossier transcription) | B4 RESIDUE CLOSED 2026-09-26 (COR-16): class and confidence lowered to match quantitative.csv L181/L182 and stage_2 P164; no value, date, accession or URL changed and no figure deleted or substituted"
```


## Stage-3 handoff debt

STATUS: WRITTEN. Nothing below was edited by this pass — every path is the other agent's.

1. **`quantitative.csv` L339** (`stage3`, `derived_arithmetic` = `28813/147758=0.194995`): correct value **0.1950013**.
2. **`stage_3_part_3.md` §P188 and §P.2 t1** carry the same false quotient (the audit's three sites). This pass's sweep
   found **two more matching literals** in Stage-3 files — `stage_3_claim_records_part_1b.md` l.177 and l.484 — plus
   `stage_3_pending_registers.md` l.61. Those four were **counted but not read individually** at the ceiling: each may
   already sit in retraction language, in which case it is not debt. **Not asserted as live.**
3. **`conflicts.csv` row 135 is `P-U.134`, a `stage3` row** — audit6 attributes it to Stage 2's U.107, which is at
   physical line **108**. Stage 3's register owner should read it as its own object.
4. **What Stage 3 inherits until the merge happens:** `conflicts.csv` U.113a still states the blank field as "a stated
   range", and `sources.csv` S2009 still calls a no-byte transcription `FACT (audited counterparty)` @ High. Stage 3
   cites the register, not the narrative — so the register rows below are the load-bearing handoff.
5. **RD-072** (`research/ST3_B_*` "spouse and brother" 13G supersession): register side corrected upstream, dossier side
   verified by nobody in this chain. Left open, untried here.
6. **Instruction layer, not mine:** `MASTER_RESEARCH_LOG.md` l.961 (U.107 "still run live" + off-by-2 pointers, audit6
   T11) and `_MANIFEST.md` (deltas re-measured by this pass: §U **72** blocks, `conflicts.csv` **170** data rows / 72
   `stage2`, claim records **482**). RD-094 already records B1 truthfully, so no instruction line asserts the false
   range today — the remaining stale instruction text is the U.107/`context_appendices` pair, routed to the orchestrator.

## Residue

STATUS: WRITTEN.

**Gate before** (`gates.py --checks keys,anchors,budget`): `Findings: 6 | Passes: 28` — four `keys` findings naming
S30xx tokens **in Stage-3 volumes only**, and two `anchors` findings (U.220 with no register row; U.201–U.211 register
rows citing anchors absent from the narrative). All six are the other agent's surface (audit6's own T2/T3). Every
Stage-2 volume passed `keys` and `budget` before this pass and passes after; `anchors` still counts **72** Stage-2
anchors, unchanged by the repairs. **After** run is pasted below this sheet.

**Blocker ledger.** B1 repaired in text + register row handed off · B2 repaired (2 sites) + 6 downstream sites handed off ·
B3 repaired · B4 handed off (row supplied) · B5 repaired · **B6 reclassified — should not be repaired** (rows are valid
CSV) · B7 repaired (counts re-measured, keying discipline declared, cap status corrected) · B8 closed (record B125;
id RD-049). The verified-clean set was **not** touched: 257 rent, 30.81409, 0.2549989, 14.0500004, 39.5690/39.6, the
restatement values, the U.114/U.115 re-key.

**UNTRIED at the ceiling (≈50 tool calls; named as a deliverable, §15.2).**
1. Directed Stage-3 sweep for the other Stage-2 repaired classes (rent, 30.81409, 0.2549989, 14.0500004, 39.5690, the B&N
   reclass, the price walk, the restatement pair) — audit6 Untried-5 called this the highest-value next call. Not run.
2. `(PB)` firewall census and `part_1b`'s §Q–§T margin sites (audit6 Untried-1). Not re-counted.
3. Audit residue-sweep rows 7, 8, 10, 11: `147,787` vs `147,758` per-row basis labelling, `(0.31)` without the words
   "PRO FORMA", the 365/366 day basis, D-13's eight new `timeline.csv` rows. Not individually classified.
4. The 41 non-conflicts register width/date findings: re-measured as **0** gate findings under the fixed reader, but no
   row-by-row stage attribution was made.
5. `data_gaps.csv` completeness (High-importance gap without `follow_up_task`). Not tested.
6. Whether other §T/§P cells still describe No. 2/No. 3's five assumption sites as one pro-forma section (the block now
   cites all five; the narrative cells were not re-audited).
7. The 10-K405 **l.1721** integrity question the certifier raised (the $(0.25) denominator `22,655` being labelled
   *revised* by the same document that files it). **Not asserted, not repaired** — it is a real question about a Stage-2
   basis, and the next pass should decide whether §P.2 s1 must name the revision.

**For the re-certifier.** Read §U.113a's `⟪COR-16 …⟫` marker against l.208–209 of the original yourself; check the three
re-keyed cites land; rule on my **rejection** of your "pointer wrong by 60" finding (No. 3 l.1230 is byte-present); check
the two minted §U records and new **B125** against the §7 line format; and treat **B6 as withdrawn** unless you can
produce a reader other than `csv.excel` that the pipeline actually uses — applying the width "fix" would break three
valid rows.

