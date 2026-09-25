# amazon_s2_recertification_audit6.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T19:05:41Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## Verdict

**NOT-CERTIFIED.** Stage 2 is **not** fit to be cited by Stage 3 as it stands. This is the sixth pass and it fails in
the expected shape — the narrative body is sound and the defects are concentrated in (i) the newest §U block and the
register rows minted for it, (ii) registers that every repair pass declared out of its own scope, and (iii) the index.
Five of the eight blockers are single-line fixes; none requires re-research. Nothing here re-opens the stage's
argument: §D's verdict, the boundary, the `(PB)` firewall and the price-walk *sequence* all survived this audit.

**Gate criteria, as a whole.**
1. **Chronology** — CONDITIONAL PASS. The 1997-05-09/13/14/15 re-key holds at every narrative site (all now
   retraction-marked), and §Q's dates and the `(POST-BOUNDARY)` tags survived; but `quantitative.csv` **L186** still
   states the *retracted* chronology ("within five days", "the previous day") in a stage-2 row Stage 3 reads (B1/B6 class).
2. **Sources / citation** — **FAIL.** B1 presents a document that prints blank price fields as evidence that it "states
   a range"; three of the four new block's line cites in the keyed file miss the quoted text (−17 on the S-1 original,
   −60 on No. 3), while two other cites are exact. Verbatim discipline is not uniform in the repaired text.
3. **Numbers** — **FAIL.** B2: the false FY1997 margin quotient is live in Stage 2 at §P.2 s4 and a claim record after
   the repair certified zero; B3: a no-disk numerator is still called "filed" in the U.67 record. Classes swept 1–6 and
   14 (rent 122→257, 30.813→30.81409, 0.2548, 14.0500007, ≈39.5, restatement set, U.114/U.115 re-key) are genuinely
   clean — the repair worked where it was checked and stopped where the sheet said "out of scope".
4. **Hindsight / class integrity** — **FAIL (narrow).** B5: one unbounded whole-life superlative survives verbatim in
   a claim record; B4: a `local_copy: NO` witness carries `FACT (audited counterparty)` + **High** in `sources.csv`
   while the same witness is `UNKNOWN` in `quantitative.csv` — class and confidence exceeding evidence, and a
   single-lineage witness labelled audited. The other C-1…C-16 sites are bounded and marked.
5. **Internal consistency** — **FAIL.** 72 §U blocks ↔ 72 `stage2` conflict rows (parity restored) but 70 conflict
   **records** (U.113a/U.113b have none); the index still says the rows are unapplied and prints 411/72/481 against a
   measured 304+105/70/479; volume 1b is unlisted; volume 1 breaches the 60,000-word hard cap.

**The two known open items.**
* **The 1997-04-18 authorised-capital record: DOES NOT CLOSE.** Still no claim record (B8), and the brief's id is
  wrong — that item is **RD-049**; **RD-072** is the Stage-3 "spouse and brother" 13G supersession (`MASTER_RESEARCH_LOG.md`
  l.586), whose **register** side is now corrected — `timeline.csv` L132 (`stage3`, S30006, FACT) reads "the founder's
  parents and spouses of each other", actors "Jacklyn Gise Bezos; Miguel A. Bezos". Whether `research/ST3_B_*` itself
  carries the supersession marker was **not verified** (Stage-3 path, outside this brief); the log row still says OPEN.
* **The U.168 wording: CLOSES ONLY FOR STAGE 2.** Stage 2's own leg (U.107) is correctly CLOSED — the strings appear in
  `context_appendices.md` l.598/l.641 only inside withdrawal sentences, re-measured. Stage 3's U.168 row states the
  same thing accurately. The residual is the instruction layer: `MASTER_RESEARCH_LOG.md` l.961 still asserts the pair
  "still run live" at l.596/l.639 — stale wording *and* off-by-2 pointers (T11). Stage 2 cannot close that line.

**Blockers:** 8 — B1 §U.113a CLAIM B + `conflicts.csv` U.113a (blank range presented as a stated range);
B2 `0.194995` live at `stage_2_part_2.md` §P.2 s4 and `stage_2_claim_records.md` l.622 (+3 inherited Stage-3 sites);
B3 "the filed figures give 2,448,000 …" at `stage_2_claim_records_part_2.md` U.67;
B4 `sources.csv` S2009 `FACT (audited counterparty)` @ High with no local copy;
B5 "the cheapest capital the firm ever raised" at `stage_2_claim_records.md` l.475;
B6 `conflicts.csv` rows 135/170/171 off-width (16/18/17 vs 15) incl. both new Stage-2 rows;
B7 index claim-count/parity/manifest contradictions + `stage_2_claim_records.md` over the hard cap + volume 1b unlisted;
B8 the 1997-04-18 authorised-capital record still missing from the appendix (RD-049).

## Repair-residue sweeps

Gates run first, once, as instructed: `python tools/gates.py --company-dir
"founders_playbook/01_companies/company_001_amazon" --checks csv,keys,anchors,budget` →
**Findings: 17 | Passes: 30**. Findings quoted in full in `## Blockers` / `## Tolerable` below:
csv width drift (timeline 1 row; quantitative 13; conflicts 3 at lines 135/170/171; sources 26; data_gaps 1);
`sources.csv` access_date without a year ("NOT ACCESSED IN THIS PASS (zero-web budget)"); `failures.csv` date cell
"Stage 2"; unresolvable source tokens S3001/S3007/S3012/S3013/S3020/S3022/S3024/S3081 in six **Stage-3** files;
anchors: `U.220` anchor with no register row, `U.201–U.211` register rows citing anchors absent from the narrative;
budget: `stage_2_claim_records.md` **60,718 words > 60,000 cap** and `stage_3_claim_records.md` 84,337.

Method: every repaired figure and construction from the five repair sheets was swept across the WHOLE company
corpus (narrative, claim records, nine registers, `_parts/`, `research/`, Stage 1, Stage 3) by literal digits and by
phrasing, each hit classified live / quoted-source / retraction / stale. Line numbers below are locators only;
addresses are by label (§14.12).

| # | Repaired class (source sheet) | Patterns swept | Hits in editable scope | Live-correct | Quoted source | Retraction | **STALE** |
|---|---|---|---|---|---|---|---|
| 1 | FY1996 rent 122 → **257**; multipliers 12.6/35.4/6.4× (A3 D-01/D-02) | `122k`, `$122`, `÷ /122`, `6.4×`, `6.4x`, `122 … rent` | 11 | 4 (quantitative L168/L169 value 257, channels L24, validation L40) | 3 (`1,122,000`, `$122.8440` S-8, `2852/12287` substring) | 4 (`stage_2_part_2` §P.2 l.418, §P150 l.607, `stage_2_part_3` §Q l.79) | **0** — class holds |
| 2 | `30.813`→`30.81409`; `2,980.6`/`3,081%`/`29.8×` inversion (D-03/D-04) | same | 6 | 3 | 0 | 3 (§P76 l.525, §P.2 s2 l.704, §U.47 l.406–408) | **0** in Stage 2; `_parts/s2_p4.md` ×4 under SUPERSEDED banners (draft copy, correctly fenced) |
| 3 | `0.2548`→`0.2549989` (D-05) | same | 2 | 1 (§P.2 s1 l.754) | 0 | 1 | **0** |
| 4 | `14.0500007`→`14.0500004` (D-14) | same | 2 | 1 (§P.2 s1 l.694) | 0 | 1 | **0** in Stage 2; `_parts` ×2 stale |
| 5 | `19.4995`/`0.194995`→`0.1950013` (D-06) | same | 9 | 0 | 0 | 4 (quantitative L124, §P80a l.530, §U.52 l.515, U.52 record l.66) | **2 LIVE IN STAGE 2** + 3 downstream — see Blocker 2 |
| 6 | `≈39.5`→`39.5690`/`39.6` days band (D-07) | `≈39\.5` | 3 | 1 (quantitative L166 `39.5690 -> 39.6`) | 0 | 0 | **0**; `_parts` ×2 fenced SUPERSEDED |
| 7 | `147,758` as-filed vs `147,787` pooling-restated (D-08; A4 B-5) | both spellings | 12+ | labelled at L124/L207, §P80a, §U.113b, §A | — | — | not individually classified — **UNTRIED** (see below) |
| 8 | `(0.31)` = PRO FORMA not as-filed (D-09) | `0.31` | 1 sample read | §P147 header + record l.660 "(0.31 **PRO FORMA**, 10-K405 l.1194/l.1197" | — | — | 0 in the sampled site; full sweep **UNTRIED** |
| 9 | B&N witness reclassed UNKNOWN (D-11) | `2,448`, `155.5`, `16.6×`, `431 superstores`, `FACT (audited counterparty)` | 22 | 15 carry the NO-LOCAL-COPY / RECLASSED gloss | `sources.csv` S0410/S0607 (Stage-1 rows) | quantitative L181/L182 `NOT-ON-DISK`, validation L38, conflicts U.67/U.68, §P164/§P165, part_3 §Q l.99/§R l.143 | **2** — `stage_2_claim_records_part_2.md` U.67 record ("**the filed figures** give 2,448,000 ÷ 147,758") and `sources.csv` **S2009 (`stage2`)** still `FACT (audited counterparty)` @ **High**. Blockers 3 and 4 |
| 10 | 365/366 basis named per row (D-12) | `365`, `366` | not swept individually | — | — | — | **UNTRIED** |
| 11 | §Q rows ↔ timeline.csv twins, 8 rows added (D-13) | row count | timeline 266 rows / 11 wide per the owner sheet; gates now reports **1 row width-drift** and one `date` cell reading "Stage 2" in `failures.csv` | — | — | — | partial, **UNTRIED** |
| 12 | Stale appendix-residue conflict U.107 CLOSED (D-10) | `2,613,000`, `871,000`, `871,024`, `976,408` | 30+ | 0 live values | `context_appendices.md` l.598/l.641 = withdrawal sentences ✓ (matches the repair) | stage_1.md ×6, CORRECTIONS.md ×4, RESUME_HANDOFF.md ×4 (all WITHDRAWN-marked) | **1 instruction-layer**: `MASTER_RESEARCH_LOG.md` l.961 still says the pair "still **run live** in `context_appendices.md:596` and `:639`" — wrong assertion and off-by-2 pointers. Tolerable-2 |
| 13 | Price walk re-keyed to 8 accessions / 7 dated states; "same morning", "that morning", "14 May morning", "five days", "first stated price range", "four dated states", "obsolete on its own filing date", "thirteen days", "one day after B&N" struck at every site (A4/A5 A-1…A-18) | all nine strings | 44 (incl. `_parts`, `research/`, Stage 3) | 0 | `timeline.csv` l.107 keeps struck wording verbatim inside a retraction note ✓ | narrative all retraction-marked: `stage_2_part_1` l.27/l.56/l.82, `part_2` l.305/l.383/l.420/l.613, `part_3` l.99–l.104/l.291/U.113a l.1759–1781, index l.130 | **1 in a register**: `quantitative.csv` **L186** (`stage2`) prints "within **five days**", "**obsolete on its own filing date**" and names the metric "range ceiling filed **the previous day**". Blocker 1 |
| 14 | FY1996/FY1997 restatement pair (A4/A5 B-1…B-9) | `numerator unchanged`, "Three FY1996 EPS bases", `6,246`, `9,902`, `31,020`, `469` | 8 | pair printed at §P147, §P106, §A, §U.113b, conflicts U.55/U.113b | "numerator unchanged" and "Three FY1996 EPS bases" **0 live** | retraction-marked | **0** |
| 15 | Hindsight strikes (A4/A5 C-1…C-15) | `cheapest capital`, `demonstrably scaled`, `negligible marginal cost`, `was right within one quarter`, `storefronts live`, `first held its Delaware`, `by accident` | 17 | 0 | `by accident` survives as Fortune-relay quote + `(NO LOCAL COPY — S2007)` tag ✓ (timeline L78, `_parts` L2227) | `part_1` l.31/74/200/258, `part_2` l.416, record l.563 all carry "AUDIT-4 C-x: this cell read …" retractions | **1 LIVE**: `stage_2_claim_records.md` **l.475** still asserts "the cheapest capital **the firm ever raised**, paid for with a board seat" — the exact unbounded superlative C-9 struck at three sites. Blocker 5 |
| 16 | `U.114`/`U.115` → `U.113a`/`U.113b` re-key (RD-079, dangling-refs sheet) | `U\.114|U\.115` in every `stage_2*` file | 0 | — | — | — | **0 — this repair verified clean**: all 39 sites re-pointed; Stage 3 keeps U.114/U.115 (`conflicts.csv` rows 115/116 = `P-U.114`/`P-U.115`) |

## Sampled citations

Spot-checks run **against the documents on disk**, weighted to the repair sites (the brief's instruction: ~1 in 8
paraphrases were previously found presented as quotes). Note §15.6: the scripted verbatim gate was **not** in the
mandated command set (`csv,keys,anchors,budget`), so quote existence here is judgment, and §15.6's standing advisory —
Stage-1/2 secondary print (magazine, newspaper) was never saved under `sources/` — means a `local_copy: NO` witness
cannot be verified at the citation; Stage 2 handles that by tagging it, which the samples below confirm is done.

| Site (label) | Quoted / asserted | Document read | Result |
|---|---|---|---|
| `stage_2_part_3.md` **§U.113a** CLAIM B | S-1 (orig.) "states **a range** and an assumption in one breath — 'is currently estimated that the initial public offering price will be between …' (l.191)" | `sources/S-1_original_acc-0000891618-97-001309_filed-1997-03-24.txt` l.207–209 | **FAIL.** The document prints "…will be between **$   and $** per share" (l.209): the range is **blank**. The quotation is real up to the ellipsis; the *proposition built on it* is false, and the ellipsis conceals exactly the two blank fields that refute it. → **B1** |
| §U.113a | cover table "2,875,000 shares **$13.00** $37,375,000" (l.149) | same file **l.166** "value per share....... 2,875,000 shares $13.00 $37,375,000 $11,326" | **QUOTE VERIFIED / POINTER INVERTED.** Text is byte-present, but at keyed l.166; l.149 is the twin numbering. The volume's own keying declaration (`stage_2_index.md` l.58–64: `l.NNNN` = keyed headered file) makes this a −17 mis-cite → **T12** |
| §U.113a | pro-forma "Assumed initial public offering price per share … **$13.00**" (l.1204) | same file **l.1221** | VERIFIED text; pointer −17 (1204+17=1221) → T12 |
| §U.113a | No. 3 (9 May) "initial public offering price will be between **$12.00 and $14.00** per share" (l.222–223) | `sources/S-1A-No3_acc-0000891020-97-000755_filed-1997-05-09.txt` **l.223** | **VERIFIED, pointer correct** (No. 3 has no bare twin) |
| §U.113a | "its own cover prints the assumption raised to **$14.00** on the same 2,875,000 shares ($40,250,000, l.173)" | No. 3 **l.173** "2,875,000 shares $14.00 $40,250,000 $12,197(3)" | **VERIFIED, pointer correct.** Note this line also *re-labels* audit-4 §0's "No. 4 l.186: 3,450,000 shares $16.00" family as fee-table totals, consistent with `audit4_repairs` §4 item 4 |
| §U.113a | "its pro-forma section is still running on '$13.00 per share' **(l.1230)**" | No. 3: the phrase sits at **l.1290** (and l.408) | **POINTER WRONG BY 60** — no −17 rule explains it (No. 3 is not a twin file). Third pointer defect in one block; new finding, travels with **B1** |
| `stage_2_part_2.md` **§P147**, `stage_2_claim_records.md` **l.660** | "$(0.31) **PRO FORMA**, 10-K405 l.1194/l.1197" on 18,544 shares | `sources/10-K_FY1997_acc-0000891020-98-000448_filed-1998-03-30.txt` **l.1194** "Pro forma basic and diluted loss per share(1)… $ (1.27) $ (0.31) $ (0.02)"; **l.1197** "…21,651 18,544 14,394 13,191" | **VERIFIED, pointers exact.** D-09's pro-forma re-labelling is correctly founded |
| `quantitative.csv` **L121**, §P76, §U.47 | "the company prints '2,981%' at 10-K405 l.1380" | 10-K405 **l.1380** "Net sales … $147,758 838% $15,746 **2,981%** $511" | **VERIFIED, pointer exact** — supports the D-03 inversion retraction |
| `quantitative.csv` **L124**, §P80a | "`28,813 ÷ 147,758 = 0.1950013`; 147,758 = AS FILED (K97 l.1177/l.1380/l.1861)" | 10-K405 **l.1177** "$147,758 $15,746 $511"; **l.1861** same | **VERIFIED** — and it proves **B2** is a *residue*, not a sourcing dispute |
| `conflicts.csv` **U.113b** | "opex 58,022 / **9,438** / 406 / 52 (l.1186)"; FY1996 "$(5,777) (l.1192)" | not re-read this pass; consistent with `audit4_repairs` §0's line table (l.1186 9,438; l.1192 (5,777)) | **UNTRIED at document level** (row is width-broken → B6) |
| `sources.csv` **S0810** | No. 6 hedge "still in the process of evaluating … not in a position at this time to estimate possible outcomes" (l.4412–4414) | matches `audit4_repairs` §0's read of No. 6 l.4412–4414 and its attribution of the hedge to No. 6, not 424B1 | **CONSISTENT**; direct line read **UNTRIED** |

**One integrity question raised by the sampling, not previously in any sheet.** 10-K405 **l.1721** prints "revised
from 23,602,000, **22,655,000** and 18,933,000 to 21,651,000, **18,544,000** and …" — i.e. the very denominator
`quantitative.csv` L154 / §P.2 s1 use for the as-filed `5,777 ÷ 22,655 = 0.2549989 → (0.25)` is labelled
*revised* by the same document that files it. If §P147/§P.2 s1 do not name that revision, the $(0.25) basis is one
as-filed state of a pair, not a settled line. Flagged for the repair pass; **not** asserted as a defect here.

## Blockers

Eight. Each is file + stable label + the document line that contradicts it. All are in Stage-2-owned paths.

**B1 — the newest §U block's central proposition is contradicted by the line it cites.**
`stage_2_part_3.md` **§U.113a** (minted 2026-09-26, RD-079) CLAIM B: "S-1 (orig.), filed **1997-03-24**, states a range
and an assumption in one breath — 'is currently estimated that the initial public offering price will be between …'
(l.191)". The cited document, `sources/S-1_original_acc-0000891618-97-001309_filed-1997-03-24.txt` **l.208–209**
(= l.191 under the `stage_2_index.md` −17 twin rule the block itself is keyed by), prints "**between / $  and $  per
share**" — the digits are **blank on the face of the document**. The original states no range. The ellipsis is doing
the work of a quotation (criterion 3), and the block then argues from it ("A document whose range sentence is still
printed on its own filing date is not obsolete on it"). This *contradicts the narrative it was written to correct*:
`stage_2_part_1.md` §A.3/the boundary row "blank (24 Mar, S-1 orig.) → $12.00–$14.00 … (No. 1, 21 Apr)" is the true
state, and `audit4_repairs` §4 item 2 ("the original left the range blank, so No. 1 is the first statement") is right.
The same false proposition is now a register row: `conflicts.csv` **U.113a** (`stage2`). This is a repair adding a
defect while removing one, in the direction that matters: Stage 3 cites the register.

**B2 — `0.194995` / `19.4995` still live in Stage 2 after AUDIT-3 D-06 certified "4 → 0 live".**
`stage_2_part_2.md` **§P.2 s4** l.715: "margin, `28,813 ÷ 147,758 = 0.194995 → 19.5%`, printed at 10-K405 l.1403"
and `stage_2_claim_records.md` **§L validation record at l.622**: "the FY1997 audited annual margin,
28,813 ÷ 147,758 = 0.194995". Both print the false quotient as arithmetic, with no retraction marker, while
`quantitative.csv` L124, §P80a (l.530), §U.52 (l.515) and the U.52 record (l.66) all state the correct
`0.1950013` (28,813 ÷ 147,758 = 0.19500129). The volume contradicts itself inside one section family. Downstream
already inherited it: `quantitative.csv` **L339** (`stage3`, `derived_arithmetic` = "28813/147758=0.194995"),
`stage_3_part_3.md` **§P188** (l.93) and **§P.2 t1** (l.227) — i.e. the propagation the recertification exists to catch.

**B3 — B&N numerator still called "filed" in the U.67 claim record.**
`stage_2_claim_records_part_2.md` **U.67 record**, l.96: "CLAIM B: **the filed figures** give `2,448,000 ÷ 147,758 =
16.6×` and `2,448,000 ÷ 15,746 = 155.5×`". Contradicted by the same repair's own sites: `conflicts.csv` **U.67**
now reads "the **transcribed** B&N figure … over the filed Amazon denominators", `quantitative.csv` **L181** opens
`NOT-ON-DISK:` with "the NUMERATOR is printed in NO document on disk (0 grep hits for 2,448 …)", and §U.67
`stage_2_part_3.md` l.811 says "the transcribed B&N figures over the **filed** Amazon denominators". D-11 moved the
register and stopped at the claim record — one-place-fixed/one-place-stale, the named failure class.

**B4 — class and confidence exceed the evidence in `sources.csv`.**
`sources.csv` **S2009** (`stage2`, the B&N FY1996 Form 10-K) still carries `evidence_class: FACT (audited
counterparty)` and `confidence: High` on the same line as `not held locally`, and `stage_2_index.md` l.69–72 records
S2009 as one of the five `local_copy: NO` witnesses. `amazon_s2_audit3_repairs` D-11 certified "`FACT (audited
counterparty)` as a class string: 6 occurrences before → **0 live**", exempting "the two in `sources.csv`/`_parts`"
as a *Stage-1/Stage-3* row — but S2009 is a **stage2** row. Under §3 (one filing lineage, no local bytes) a
dossier transcription cannot carry High, and it flatly contradicts `quantitative.csv` L181/L182 and §P164, which
reclassed the identical witness to UNKNOWN. Stage 3 reading `sources.csv` gets a High-confidence "audited
counterparty" label for a document the corpus cannot open.

**B5 — the struck whole-life superlative survives in a claim record.**
`stage_2_claim_records.md` **l.475** (§N Series-A record, sibling of the repaired N13 at l.563): "… and no row in
this stage may treat the IPO's size as free choice; **it is also the cheapest capital the firm ever raised**, paid
for with a board seat." That is verbatim the wording AUDIT-4 C-9/C-1c struck at three sites and `audit4_repairs`
§7 counted "**3 sites → 0**". `stage_2_part_1.md` l.74 keeps the retraction ("this cell read 'the cheapest capital
the firm EVER RAISED'. That is a whole-life ranking…"). A retrospective, whole-life superlative is presented as the
claim itself, with no bound to 1997-05-15 and no `INFERENCE (bounded)` class — criterion 4.

**B6 — the two appended Stage-2 conflict rows do not parse.**
gates csv: `conflicts.csv` "**width drift: 3 rows off ([(135, 16), (170, 18), (171, 17)]**)" against 15 uniform.
Lines 170/171 are `U.113a`/`U.113b`, the rows just minted to restore parity; line 135 is the D-10/U.107 row the
audit-3 log already admits it broke and "repaired twice" — it is still off-width. Field-aligned consequences: the
`confidence` and `residual_uncertainty` cells of the two new rows are not reliably addressable, and §13's
date columns are being used as prose (`U.113a`'s `claim_a_date` = "struck 2026-09-25; wording had been current in
Stage 2 from 2026-09-24"). The rows also carry `stage_2_part_3.md §T l.97-104` — line numbers as addresses, which
§14.12 forbids and which this pass's own edits shift.

**B7 — instruction layer and claim-record counts disagree with the disk.**
`stage_2_index.md` l.37 and l.84 still state that `conflicts.csv` "**holds 70 Stage-2 rows and stays there until the
register owner appends U.113a/U.113b**" — the rows **are** appended (file now 170 data rows = 43 stage1 / **72**
stage2 / 55 stage3). Measured claim records: `stage_2_claim_records.md` **304**, `stage_2_claim_records_part_1b.md`
**105**, `stage_2_claim_records_part_2.md` **70** = **479**, and **0** records for U.113a/U.113b against **72** §U
blocks (measured `^\*\*U\.[0-9]+[a-z]? —` = 72; U.113a l.1754, U.113b l.1790). The index asserts "volume 1 carries
**411** lettered records", "volume 2 carries **72** conflict records", "**481** in all" (l.44–46) and "**479**
records" (l.122) in the same file. Volume 1b is not in the index's volume table at all. And
`stage_2_claim_records.md` is **60,718 words**, over the §9.2 hard cap — §9.6: "Any file above the hard cap is a
defect: split it".

**B8 — the authorised-capital record is still missing (and the brief's RD id is wrong).**
Narrative `stage_2_part_1.md` **§B.0 "Legal form" row** (l.94) asserts "authorised 5,000,000 preferred / 25,000,000
common at $0.01, **raised 1997-04-18 to 10,000,000 / 100,000,000**" as FACT/High, and `quantitative.csv` L187 carries
the two *splits* but not the authorisation figures. No claim record exists for it:
`stage_2_claim_records_part_2.md` l.209 item 6 and `stage_2_claim_records_part_1b.md` l.277 both still declare it a
gap. **Open item 1 therefore does NOT close.** Note also that the brief's id is mis-keyed: `MASTER_RESEARCH_LOG.md`
l.586 **RD-072** is the ST3B-14 "spouse and brother" 13G supersession; the missing authorised-capital record is
**RD-049** (log l.554, still `OPEN`). Certifying against the wrong register id is itself a residue risk for the next pass.

## Tolerable

Stated as required: which gate findings and audit observations this certifier does **not** treat as Stage-2
certification blockers, and why.

**T1 — gate `budget`: `stage_2_claim_records.md` 60,718 > 60,000.** *Is* a §9.2/§9.6 defect, but it is a file-geometry
defect, not an evidence defect, and it does not corrupt a citation. Listed under B7 only because the same index lines
that fail to record the overage also mis-state the counts. Fix by splitting volume 3; do not trim (
§9.6: "Cutting evidence to fit a file limit is forbidden").
**T2 — gate `keys`: unresolvable `S3001/S3007/S3012/S3013/S3020/S3022/S3024/S3081` in six files.** All six are
**Stage-3** volumes (`stage_3_claim_records.md`, `_part_2`, `stage_3_index`, `stage_3_part_2/3`,
`stage_3_pending_registers`). Every Stage-2 volume resolves: gates passes `stage_2_part_1/2/3`, both claim-record
volumes and the index (16 tokens). Not a Stage-2 blocker; it *is* a warning that Stage 3's source keys are not yet
bound, which is exactly the surface B1–B4 will land on.
**T3 — gate `anchors`: `U.220` with no register row; `U.201–U.211` register rows with no narrative anchor.**
Measured to be **Stage-3 dossier-local keys written into global columns**: `stage_3_part_1.md` l.22–23 declares
"`ST3_A` at U.201–U.211 … `ST3_E` at U.220–U.228 — which are **dossier-local keys, not register IDs**", yet they sit
in `conflicts.csv` `section` cells (rows 115/116/123/125 "[dossier id U.201/U.202/U.209/U.211]"), `timeline.csv`
`conflict_ref` (L134, L153) and `sources.csv` `claim_supported` (L120/122/123/133). A §13 grammar breach owned by the
Stage-3 binding pass, not Stage 2. Stage 2's own parity is intact: 72 §U blocks ↔ 72 `stage2` conflict rows.
**T4 — gate `csv` width drift outside the two new rows** (quantitative 13 rows e.g. 7/8/25, sources 26, timeline 1,
data_gaps 1). These are dominated by Stage-1/Stage-3 legacy rows and prose commas in free-text cells; the ones that
touch this certification are named individually (B6 for conflicts 135/170/171). Row-ownership of the other 41 was not
classified within budget → **UNTRIED**, not asserted clean.
**T5 — gate `csv`: `sources.csv` access_date "NOT ACCESSED IN THIS PASS (zero-web budget)".** An honest null on rows
whose `local_copy: NO` is already declared (S2005–S2009, S2012). Tolerable, and it is the *right* answer under a
zero-web brief.
**T6 — gate `csv`: `failures.csv` `date` cell = "Stage 2".** One §13 ISO-date defect; pointer-class, one-line fix.
**T7 — gate `budget`: `stage_3_claim_records.md` 84,337 > cap.** Stage 3's file, Stage 3's gate.
**T8 — `_parts/` and `research/` still hold every pre-repair value.** Measured: `_parts/s2_p4.md` carries 122-as-rent,
`30.813`, `0.2548`, `14.0500007`, `19.4995`, `≈39.5`, "filed that morning", "obsolete on its own filing date";
`_parts/s2_p1.md` carries "the same morning", "14 May morning", "one source, four dated states", "first held its
Delaware form", "demonstrably scaled", "was right within one quarter", "negligible marginal cost". **Tolerable
because they are fenced**: `_parts/s2_p4.md` prints inline `⟪SUPERSEDED 2026-09-25 · R-4 … repaired at
stage_2_part_2.md … ⟫` banners at the `30.813`/`39.5`/`19.4995` sites, and `stage_2_index.md` l.4–6 declares the parts
the drafting audit trail, not a citable volume. It is nonetheless the re-import mechanism the audit-3 log predicted,
and B1 is the proof that a later pass reading a non-canonical copy can re-write canon wrongly.
**T9 — `stage_2_index.md` l.10–13 word columns stop at Audit 2** (part_1 19,289 / part_2 25,524 / part_3 40,385
against gates' measured 22,903 / 28,347 / 45,173). The column is self-labelled "(post-repair, 2026-09-25 Audit 2)",
so it is stale rather than false — but l.20's "no volume approaches the 60,000-word cap" is now contradicted by volume
1 of the claim records (T1).
**T10 — `by accident` / Fortune relay.** The struck phrase survives only inside a properly gated relay
(`timeline.csv` L78, `_parts` L2227) carrying "NO LOCAL COPY and the full text is UNTRIED; nothing is quoted beyond
what a dossier carries" — correct §5/§14 discipline, not a residue.
**T11 — U.107's CLOSED status holds.** `context_appendices.md` l.598/l.641 carry `2,613,000`/`$871,000` only inside
withdrawal sentences (measured), matching D-10. What is stale is the *log*, not Stage 2: `MASTER_RESEARCH_LOG.md`
l.961 still says they "still **run live** in `context_appendices.md:596` and `:639`" — wrong assertion plus off-by-2
pointers, in the highest-severity location §14 rule 10 names. Not owned by Stage 2; routed to the orchestrator.
**T12 — the twin/keyed line convention.** `stage_2_index.md` l.58–64 declares `l.NNNN` = a line of the *headered keyed*
file, with `twin line = keyed line − 17`. The new `U.113a` block and `conflicts.csv` U.113a name the **keyed** paths
but print **twin** numbers (l.191/149/1204 where the keyed file has the text at 208/166/1221). The quotations are real
— this is a pointer inversion, one line of convention text away from correct. Tolerable for Stage-2 text, but it makes
B1's citations un-followable, so it travels with B1 rather than standing alone.

## Untried

Named as a deliverable (§15.2), not a disclaimer. Everything below was **reachable on disk** and was not reached
inside 55 calls; zero web calls were made, and no Stage-2 file, register or source was edited by this pass.

1. **`(PB)` firewall census.** `audit4_repairs` measures 161 occurrences before / 187 after and claims the three
   untagged FY1997 margin sites in `stage_2_part_1.md` went 3 → 0. Not re-counted, and the margin pair was not
   re-swept for untagged live uses in the claim records (`part_1b`'s §Q–§T block was never opened).
2. **Sweep rows 7, 8, 10, 11 of the residue table are partial**: `147,787` vs `147,758` per-row basis labelling,
   `(0.31)`-without-pro-forma-word across all sites, the 365/366 day-basis per row, and D-13's eight new
   `timeline.csv` rows (were they written **inside** the stage-2 block with no row moved? only the row count 266 was
   observable). Each needs one sweep, not one judgment.
3. **`stage_2_claim_records.md` l.602 / l.616 / l.652** matched the false-tails class but were not read individually;
   l.620 and l.622 were, and l.622 is a live stale site (B2). If the other three are live, B2 grows.
4. **41 of the 44 `csv` width-drift rows** (`quantitative.csv` 13, `sources.csv` 26, `timeline.csv` 1, `data_gaps.csv`
   1) were not attributed to a stage. Only the three `conflicts.csv` rows this pass needed (B6) are owned.
5. **Stage 3's inheritance from Stage 2.** Found by accident, not by design: three Stage-3 sites carry the B2 false
   quotient (`quantitative.csv` L339, `stage_3_part_3.md` §P188, §P.2 t1). A directed sweep of Stage 3 for every
   Stage-2 repaired class (rent 257, 30.81409, 0.2549989, 14.0500004, 39.5690, B&N reclass, price walk, restatement
   pair) was **not** run. That sweep is the highest-value next call after B1–B6, because Stage 3 is already assembled.
6. **audit-3's own NOT-FIXED list**: R-01 (Stage-3 split chain), R-02 (`_parts/NUMBER_DEFECTS.md` retired bridge),
   **R-03 (§P145 still has no `quantitative.csv` twin)**, R-04 (FY1996 percentage rows cite A5 l.1703 instead of
   K97 l.1435/1464/1495). Still open on the sheets; R-03/R-04 were not re-tested.
7. **Register hygiene hazards raised by the owner sheet but not re-measured**: `conflicts.csv` is CRLF while the other
   eight are LF (§6.4 of `amazon_s2_register_owner.md`); the two B6 rows are the first thing a terminator-blind
   re-write will touch. Also the 15-field §13 header equality of the appended rows was not re-derived by hand.
8. **`_MANIFEST.md`** was not opened: whether `stage_2_claim_records_part_1b.md` is registered, and whether the word
   counts, conflicts 70→72 and records 479 deltas the index demands (l.138–140) were ever picked up, is unknown. B7
   asserts only what the index and the claim-record files say about themselves.
9. **`data_gaps.csv` completeness** (§13: a High-importance gap with no `follow_up_task` is an open research-debt
   violation) — not tested.
10. **gates' other checks** — verbatim-quote existence and `--self-test` (§15.5/§15.6) — were not run, because the
    mandated command was `csv,keys,anchors,budget`. The scripted verbatim gate would probably fire on §U.113a's
    ellipsis; that is a judgment call this sheet makes by hand instead.
11. **RD-072's dossier side** (`research/ST3_B_*` supersession marker) — Stage-3 path, not opened.
12. **Whether the two lettered addenda need claim records at all** under §7 ("one record per claim") was treated as
    yes (72 blocks ↔ 70 records = B7); a different reading would make B7 a labeling dispute rather than a defect.

