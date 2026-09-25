# AUDIT 5 — AMAZON.COM STAGE 2 · ADVERSARIAL (run 5, adversarial class)

**Sheet:** `03_quality_control/amazon_s2_audit5_adversarial.md` · **Auditor:** Level-3 Adversarial, independent of
the producer: **yes** (wrote no dossier, no merge, no repair pass; edited no file but this sheet).
**Target attacked:** `stage_2_part_1.md` (19,289 w) · `stage_2_part_2.md` (25,524 w) · `stage_2_part_3.md`
(40,385 w) · `stage_2_claim_records.md` + `_part_2.md` (479 records) · `stage_2_index.md`.
**Boundary under test:** 1996-01-01 → 1997-05-14/15.
**Web requests made: 0.** Every refutation below is a line of a file already in
`founders_playbook/01_companies/company_001_amazon/sources/` (99 files) or of a spine file, re-read this pass.

**Binding rules honoured.** COR-01 accession labels; COR-09 barred list (swept, not re-asserted); COR-12
headcount; COR-13 the 1995 release; method §3 one-lineage rule; the Stage-1 A-B1 closure (a restatement of one
registration statement is **one** source). `ST2_E_adversarial.md` is treated as a claim, not as evidence: five of
its fifty challenges are re-tested here and two of them are corrected (see L-7 and the F-list).

**Method note, and it is the reason this sheet finds anything.** The spine declares at
`stage_2_part_1.md` l.27 "**Nos. 1/2/4/6 unread**" and registers the non-reading as a conflict at **U.95**
(`stage_2_claim_records_part_2.md` l.150, confidence "**UNKNOWN** (what they hold)"). Those four documents, and
the FY1998 10-K, FY1999 10-K and FY1999 10-K/A, have been on disk the whole time. U.95 was therefore never an
UNKNOWN; it was an unopened envelope inside the project's own directory. This pass opened it. **Nothing about the
stage's argument collapsed. Everything about the volume's account of its own documentary spine changed**, and the
load-bearing sentence of the boundary — "priced above the ceiling it had itself filed **that morning**" — did not
survive it.

---

## Attacks that landed

Ranked by damage. Class in brackets. **CRITICAL** = a spine sentence is false on a local document; **MAJOR** = a
section's attribution apparatus is wrong; **MEDIUM** = wording/discipline.

### L-1 · CRITICAL — The IPO price walk is wrong in three of its four steps, and "the ceiling it filed that morning" is contradicted by the volume's own §Q

**The claim attacked.** `stage_2_part_1.md` l.24 (span header): "after the filed range moved $12–14 → $14–16
**the same morning**, a 20% upsize clearing above its own ceiling"; l.53 (§Boundary, "The deal and its
repricing"): "**Range: blank → $12.00–$14.00 / 2,500,000 (9 May) → $14.00–$16.00 / 3,000,000 (14 May morning) →
$18.00**"; l.79 (§A.3, the section that carries the stage's endpoint): "**Amendment No. 3 (1997-05-09): 2,500,000
shares at $12.00–$14.00. Amendment No. 5 (1997-05-14, the same day as pricing): 3,000,000 shares at
$14.00–$16.00** … **$2.00 above the ceiling the company had filed that morning** … inside one week";
`stage_2_part_2.md` l.305 (§L): "deal **+20% larger than five days earlier**"; `stage_2_part_3.md` l.94 (§Q
1997-05-09 row): "**the first stated price range in the whole lineage, $12.00–$14.00**"; l.98: "$2.00 above the
ceiling of the prospectus **filed that morning**"; `stage_2_claim_records.md` l.840 (**Q60**) repeats it.

**What is on disk.** The walk has **seven** dated states across **eight** accessions, not four, and its two
pivot dates are both earlier than the spine says:

| Accession | Filed | Shares | Range / assumed price | Line |
|---|---|---|---|---|
| S-1 (original) | 1997-03-24 | 2,500,000 | range **blank** | (spine correct) |
| **S-1/A No. 1**, acc. …603 | **1997-04-21** | 2,500,000 + 375,000 OA = 2,875,000 @ **$14.00** | **"between $12.00 and $14.00 per share"** | `sources/S-1A-No1_acc-0000891020-97-000603_filed-1997-04-21.txt` **l.247–248**, fee table **l.192** |
| S-1/A No. 2, acc. …659 | 1997-04-29 | 2,875,000 @ $14.00 | "between $12.00 and $14.00" | `…No2…filed-1997-04-29.txt` **l.234–235**, l.183 |
| S-1/A No. 3, acc. …755 | 1997-05-09 | 2,500,000 | "between $12.00 and $14.00"; assumed **$13.00** | `…No3…l.222–223`, l.408 |
| **S-1/A No. 4, acc. …822** | **1997-05-13** | **3,000,000** + 450,000 OA = 3,450,000 @ **$16.00** | **"between $14.00 and $16.00"**; assumed **$15.00** | `sources/S-1A-No4_acc-0000891020-97-000822_filed-1997-05-13.txt` **l.242–243**, l.186, **l.233, l.239, l.369**, l.438 |
| S-1/A No. 5, acc. …839 | 1997-05-14 | 3,450,000 @ $16.00 | "between $14.00 and $16.00" | `…No5…l.224–225`, l.173 |
| **S-1/A No. 6, acc. …847** | **1997-05-14** | 3,450,000 @ $16.00 | "between $14.00 and $16.00" | `sources/S-1A-No6_acc-0000891020-97-000847_filed-1997-05-14.txt` **l.225–226**, l.178 |
| 424B1, acc. …868 | 1997-05-15 | 3,000,000 | **$18.00** | `…424B1…l.124` |

**Damage, itemised.**
1. **"the same morning" / "filed that morning" is not a filed fact and is contradicted by inference from the
   spine's own rows.** No accession in the corpus states a time of day; the EDGAR headers for …822, …839 and
   …847 carry `FILED AS OF DATE` only (verified in the diff of No. 5 against No. 6, both `19970514`). And the
   $14–16 ceiling was first filed on **13 May** — a day and a half before the 424B1's date line, not the same
   morning. `stage_2_part_3.md` **l.95** already prints "1997-05-13 · Amendment No. 4 (acc. …822) filed". The
   volume therefore **contradicts itself between §Q l.95 and §A.3 l.79 / §Q l.98**: the ceiling was on file
   overnight.
2. **"$12.00–$14.00 on 2,500,000 (9 May)" is three weeks late and §T's own-only-content attribution is false.**
   `stage_2_part_3.md` **l.263** states that No. 3 earns its separate citation for "**the FIRST stated price
   range in the whole lineage**, $12.00–$14.00, on 2,500,000 shares". It was second or third printed; No. 1
   stated it on 1997-04-21 and No. 2 on 1997-04-29. Same defect at §Q l.94.
3. **"+20% larger than five days earlier" is wrong by three days.** The upsize was filed 13 May, the final
   prospectus 15 May: **two days**. (`stage_2_part_2.md` l.305.)
4. **"one source in four dated states" (l.53, l.79) under-counts the instrument's own history** — the sentence
   being defended ("the *differential* is the evidence, the repetition is not") is right in principle and wrong
   in its census. The differentials that carry information are **24 March → 21 April** (blank to $12–14),
   **9 May → 13 May** ($12–14/2.5m to $14–16/3.0m), and **13 May → 15 May** ($16 ceiling to $18 price). The
   volume names the third, misdates the second, and misses the first.

**What survives, and it matters.** $18.00 ÷ $16.00 − 1 = **+12.5%** above the last filed ceiling: **intact**.
All-primary, no selling stockholder, 20% upsize, ten-house firm commitment, 7.00% spread: **intact**. That the
company re-priced its own range upward twice in twenty-four days and then cleared it: **intact, and better
documented than the volume knew** — the range moved on 21 April, 13 May and the price cleared it on 15 May.
**The attack does not remove the endpoint. It removes the rhetorical device** (same-day compression) that §A.3
uses to make the price look like an event that happened *to* the company rather than a sequence the company
itself set in motion five weeks before. That distinction is the whole difference between a marketing signal and
a validation signal, and §A.3 currently claims the second with the rhetoric of the first.

### L-2 · CRITICAL — "Three FY1996 EPS bases exist in the corpus" is false: there are five, and the issuer itself **restated the FY1996 net loss upward** in two audited annual reports that are sitting in `sources/`

**The claim attacked.** `stage_2_part_2.md` **l.758** (§P.2 s11 area): "**Three FY1996 EPS bases exist in the
corpus** and …"; **l.604 (P147)**: "FY1996 | Net loss per share, **two as-filed bases and one PRO FORMA basis
across three documents, numerator unchanged at $(5,777)k** | $(0.26) (S-1 orig.) → $(0.25) (No. 5) → $(0.31)
(10-K405)"; **l.560 (P106)**: FY1996 "(5,777) / (0.25) / 22,655"; `stage_2_part_1.md` **l.63** (§A): "Audited
FY1996: … net loss **$(5,777)k**". The phrase "**numerator unchanged**" is the load-bearing half, and it is
false.

**What is on disk.** Two further **separate reporting instruments** — not amendments, not the same document —
print FY1996 again:

| Instrument (filed) | FY1996 net loss | FY1996 LPS | Shares used | Line |
|---|---|---|---|---|
| S-1 original, 1997-03-24 | $(5,777)k | **$(0.26)** | — | `stage_2_part_3.md` l.262 cites it; original Selected Financial Data |
| S-1/A No. 5, 1997-05-14 | $(5,777)k | **$(0.25)** | 22,655k | A5 l.3749 (volume cites correctly) |
| 10-K405 FY1997, 1998-03-30 | $(5,777)k | **$(0.31)** *pro forma* | 18,544k | `10-K_FY1997…l.1194, l.1197`, note l.1716–1726 |
| **10-K FY1998, filed 1999-03-05** | **$(6,246)k** | **$(0.06)** | **111,271k** | `sources/10-K_FY1998_acc-0000891020-99-000375_filed-1999-03-05.txt` **l.1242, l.1244, l.1247** |
| **10-K FY1999, filed 2000-03-23** | **$(6,246)k** | **$(0.03)** | **222,542k** | `sources/10-K_FY1999_acc-0000891020-00-000622_filed-2000-03-23.txt` **l.1761, l.1763, l.1765–1767** |

**Cross-checks run on this pass, all in `sources/`:**
- **The FY1996 loss is restated, not merely re-based.** $(6,246) − $(5,777) = **$(469)k, an 8.1% larger loss.**
  The movement is **not** in the operating lines: net sales $15,746, cost of sales $12,287, gross profit $3,459
  are **identical in all four instruments** (`10-K_FY1998…l.1222–1225`; `10-K_FY1999…l.1732–1735`), and total
  FY1996 operating expenses reconcile to the same **$9,902k** both ways — 6,090 + 2,401 + 1,411 in the FY1997
  10-K405 (l.1182–1184) against 6,081 + 2,377 + 1,408 + 36 (stock compensation carved out) in the FY1999 10-K
  (l.1738–1741). **So the $469k sits entirely below the operating line and the corpus contains no
  reconciliation of it.** The FY1999 10-K's own Selected-Financial-Data note reads "(1) Reflects **restatement
  for pooling of interests**" (l.231), and its l.1389/l.1456/l.1840 carry period-wide restatement language —
  offered as a candidate cause, **not adopted as one**.
- **FY1997 is restated the same way, in the same pair:** net sales **$147,758k → $147,787k** and net loss
  **$(27,590)k → $(31,020)k** (`10-K_FY1998…l.1222, l.1242`). Every `(PB)` consequence figure in the volume —
  §A l.65, §M.2, §M.6, §Q l.105, §P80a — is printed on the 1998 figure with no note that the issuer later
  printed another.
- **Even the failure ledger's own number moves.** FY1996 marketing and sales is **$6,090k** in the 10-K405
  (l.1182) and the FY1998 10-K, and **$6,081k** in the FY1999 10-K (l.1738). The §F.1 l.338 ratio "38.7% of net
  sales" therefore has two bases; the FY1997 "26.4% of net sales" at §M.6 l.360 has **three** ($38,964k /
  $40,486k / $40,077k, in that order across three audited annual reports).
- **The same year is presented with two different share counts two years apart** (111,271k vs 222,542k for
  FY1996), which means the cumulative-split factor applied to the 1996 column differs between the FY1998 and
  FY1999 10-Ks. **Any per-share ladder across 1996–99 in this corpus inherits that, and S2E-46's split warning
  does not reach it.**

**Damage.** P147's headline ("two as-filed bases and one pro forma basis **across three documents**, numerator
unchanged") must become **five bases across five documents with the numerator changed twice**, and §A's "Audited
FY1996 … net loss $(5,777)k" must carry its as-filed/restated pair. This is the project's own known trap
(**restated vs as-filed**) reproducing at the single most quoted number in the stage.
**It is a completeness failure, not a falsehood**: $(5,777) is what the registration statement and the FY1997
annual report both say, and the stage's argument never turns on the loss-per-share value. But §P.2's *claim to
have enumerated the bases* is what the volume leans on to bar a per-share ladder, and an enumeration that missed
two audited instruments cannot support a bar.

### L-3 · MAJOR — the counter-evidence hunt lands: local documents the report does not use, including a §S row that asserts the non-retrieval of a file that is on disk

- `stage_2_part_3.md` **l.227 (§S, row UG-4)** lists as still-missing: "**Q2 and Q3 1997 Forms 10-Q; the 1997
  8-K; the FY1998 10-K**; B&N's FY1995 10-K; Borders' own 10-K … **none retrieved**". **`sources/10-K_FY1998_…`
  and `sources/10-K_FY1999_…` and `sources/10-K_A_FY1999_…` are on disk.** Two of the five items are present.
  The row is a statement about the corpus that the corpus refutes. (Whether it arrived *during* or *beside*
  Stage-2 assembly is the orchestrator's fact to settle from `_MANIFEST.md`; what is not in doubt is that it is
  **now** local and that UG-4's remedy — "is a single fetch" — is no longer needed to close it.)
- Grep of the three narrative volumes for any use of the later annual reports or their figures
  (`147,787`, `40,486`, `6,081`, `10-K_FY1998`, `10-K_FY1999`): **0 substantive uses**. §T (`stage_2_part_3.md`
  l.260–281) has no row for them at all, so the source table is incomplete in the direction that flatters the
  attestation argument: **the FY1996 audited result now has four separate instruments standing behind it, which
  is the one place in this stage where the "one issuer, one document" objection genuinely weakens** — and the
  volume never collects it.
- The four unread S-1/A amendments are the second half of the same finding: they were **inventoried** (§Q l.91,
  l.95; part_1 l.27; U.95) and **not read**, and three of the five items at L-1/L-4/L-5 turn out to be sitting
  inside them.

### L-4 · MAJOR — the B&N competitor rewrite is mis-dated by one day, its "two-state" model is a three-state one, and §Q's date arithmetic is internally inconsistent

**Attacked.** `stage_2_part_2.md` **l.383 (§M.9)**: "Between A3 and A5 Amazon's own text changed to 'B&N …
**has launched** a Web site'"; `stage_2_part_3.md` **l.96 (§Q, 1997-05-14 row)**: "**the competitor paragraph
rewritten to 'B&N, specifically, HAS LAUNCHED a Web site to sell books online'** — the same sentence, **one day
after B&N's own filing** made it true and two days after B&N sued"; **l.93**: "Filed **thirteen days** before
Amazon's amendment".

**On disk.** "B&N, specifically, has launched a Web site to sell books online" first appears in
**`sources/S-1A-No4_acc-0000891020-97-000822_filed-1997-05-13.txt` l.673 and l.2535** — a day before the row
that claims it. No. 3 (1997-05-09) still reads "B&N, specifically, **has a relationship with AOL**" (l.641,
l.2484), and the **original S-1 (1997-03-24) reads "B&N, specifically, has entered into a …"** (l.2278), which
is a **third** state the volume does not model: §M.9 and U.97 analyse the competitor list as a two-step change
when it is a three-step one, and the step that matters — the shift from *relationship* to *launched* — happened
on 13 May.
**The arithmetic is self-refuting as written.** B&N's 10-K filed 1997-05-02; A5 filed 1997-05-14. That is
**twelve** days, so neither "thirteen days before Amazon's amendment" (l.93) nor "one day after B&N's own
filing" (l.96) is right; to No. 4 the interval is **eleven**. This is exactly the error class U.97 was opened to
 police (attributing a competitor-list change to the wrong accession), reproducing inside §Q — **the recurrence
 test the Stage-1 sheet says to run, and it failed.**

### L-5 · MAJOR — the last document filed before the price is the one that hedges the litigation hardest, and the volume assigns that hedge to the wrong file

`stage_2_part_3.md` **l.98** notes accession …847 only as "a further amendment body, UNTRIED". It is not
untested here: **No. 6 (acc. …847, filed 1997-05-14, a higher accession than No. 5) is No. 5 with the B&N
paragraph softened.** Diff of the two files, run this pass, isolates the body change to a single passage —
No. 5 **l.4414**: *"The Company is evaluating Barnes & Noble, Inc.'s claims and intends to defend against them
vigorously"*; No. 6 **l.4412**: *"The Company is **still in the process of evaluating** Barnes & Noble, Inc.'s
claims, and therefore **is not in a position at this time to estimate possible outcomes**. The Company intends to
defend against the lawsuit vigorously."* ST2_E **F-12** credits this wording to the 424B1 (l.4287–4289, verified)
and treats it as one of the three points on which the amendments "differ on the points that matter"; the spine
carries F-12's attribution. **Correction:** the hedge is filed on **14 May**, in the last pre-pricing instrument,
and reaches the 424B1 unchanged. Consequence, and it is a strengthening one: on the day the deal priced above its own
ceiling, the company's own final filed words about the suit attacking its central marketing claim were *"not in
a position at this time to estimate possible outcomes"*. §M.9 and U.68 should cite the …847 accession for that,
not the 424B1 alone.

### L-6 · MEDIUM — the Stage-1 discipline "**a claim is repaired everywhere it is made**" fails again, on the same quote and in the same shape as F-2/F-3

`stage_2_part_1.md` **l.67** carries the Fortune 1996-12-09 material with the full device: "`(NO LOCAL COPY —
Fortune 1996-12-09 is sources.csv S2007, local_copy: NO: the string 'If we are profitable within the next two
years, it will be by accident' … are all transcriptions, not checked bytes)`". **The same quote is restated at
two sites that carry no such tag:** `stage_2_part_1.md` **l.254** (§D.6, the section that closes the stage's
verdict) — "a founder predicting profit 'by accident' in December 1996" — and `stage_2_part_2.md` **l.301**
(§L, the *What it demonstrated* column of a row headed "Contemporaneous outside assessment"), which prints the
words as a filed observation. l.254 is worse than untagged: it converts a **journalist's relay of a founder**
into "a founder predicting", which is a motive claim about a person for whom the volume elsewhere holds
reasoning **UNKNOWN** (part_1 l.112, §N preamble). This is Stage-1's F-3 (`validation.csv` row 9, "could earn")
one stage later: the repaired site is right and its neighbour is not.

### L-7 · MEDIUM (an attack on the adversarial dossier itself) — S2E-27's version-safety census under-counts by a factor of eight, and the true count changes what the boundary document is

`research/ST2_E_adversarial.md` **l.883** records as a version-safety result:
"`repeat customers currently account for over 40% of orders` — **3 occurrences (one sentence, three
printings)**", and `stage_2_part_3.md` **l.262** carries the same figure into the spine ("all three 'over 40% of
orders' prints"). **Counted this pass, per accession:** the clause occurs **three times in each of the eight
1997 accessions** — original …1309 (3), No. 1 (3), No. 2 (3), No. 3 (3), No. 4 (3), No. 5 (3), No. 6 (3),
**424B1 …868 (3)** — and **0** times in the FY1997 10-K405 (which prints "over 58%"). **Twenty-four printings
in one instrument**, not three.
The direction of the correction is *in favour* of S2E-27's rule (still one source), so nothing inflates. But it
breaks §A.3's framing: **the document that printed the $18.00 cover price is the same document that restated the
undefined, denominator-free ">40%" three times.** The belief outside investors bought was not independent of the
self-measurement; it was priced off a page carrying that self-measurement three times over. That does not
disprove validation — "no independent witness" is a provenance downgrade — but §A.3's sentence "outside
investors priced a **belief that the model would repeat**" must now be read as belief priced off a document that
was arguing the repetition on its own page. **The dossier's own method (a string census run on four of eight
local accessions) is why the spine inherited a wrong count**: S2E-27's header says "I tested every load-bearing
fact in this review for version-safety" against a four-document set that the same dossier elsewhere concedes
omits four more.

---

## Attacks that failed (and the evidence that held)

Recorded because an adversarial sheet that reports only landings is itself a narrative — and because this project
has twice had an adversarial pass assert something untrue. Each entry names the probe and the text that stopped
it.

- **H-1 · "The stage's claim depends on the price."** Probed by deletion: remove §A.3, the §Boundary "deal and
  its repricing" row, the §L 1997-05-14/15 row and every $18.00 mention, and re-run the argument. What is left
  is §D.6's verdict — "**demand and revenue repeated; the economics were not shown to repeat; that test
  transfers to Stage 3 unperformed**" (`stage_2_part_1.md` l.254), §Boundary l.42's "**the substantive boundary,
  carried not discarded … 1996-12-31 … Substance and document are different events**", and §D.0's provisional
  verdict row (l.181). **No §D conclusion, no §P row and no §R cell changes.** The endpoint is documentary and
  the volume says so in the same sentence as the price. **FAILED — and this is the strongest part of the file.**
  L-1 damages the *rhetoric* of the price, not the *architecture* of the boundary.
- **H-2 · ">40% of orders is presented as measured retention."** It is not. `stage_2_part_1.md` l.177 grades it
  "High (as filed); **Low as measurement**"; §F.1 l.333 tags it `[T1 · SELF-MEASUREMENT]` with the derived
  complement ("**~60% of orders came from first-time buyers**"); §F.2 l.346–355 prints **five** measurements
  unreconciled across 22 months with the arithmetic of the spread shown; the §F coda l.374–383 names four
  alternative explanations including "a stable 40% of orders from repeaters is compatible with **falling**
  per-customer loyalty", and carries S2C-35's ban "Do not treat 58% as evidence of a retention flywheel".
  §L l.300 confidence: "High as claim; **Low as fact**". **FAILED** — the attack the brief asked me to run is
  already the section's own thesis. What does hold against it: nothing on this record supplies a denominator, so
  the phrase may appear only inside quotation marks around the company's words, which is how it appears.
- **H-3 · "The failure ledger §M is decorative."** Counted: **10 entries**, each with a *what it proved* and a
  *what it did not*, and an explicit *Alternative* clause at §M.1 and §M.2. Of the five failures the brief named:
  marketing ~39% is at §F.1 l.338 (38.7%, with the caption's payroll content and the split held UNKNOWN) and
  §M.6 l.360; **margin falling** at §M.6; **$79,000** at §M.3 l.337–341, §A l.63/65, §B.0, §C row 4, §D.6 l.254,
  §Q l.88; **single-site, no vendor contracts** at §M.7 and §M.8 with the exhibit-index null attached; **three
  EPS bases and the retracted runway** at §P147/§P.2 s11 and §M.3 ("The 'four days' form … **retracted**").
  §M's survivorship note (l.393–399) is concrete, not a hedge: it names three risk factors that **appear in
  March 1997 and are absent from the FY1997 annual report**, plus the suit's disappearance, and rules "a retired
  disclosure is not a resolved condition". **FAILED as decoration; SUCCEEDED as an enumeration defect** — see
  L-2 (the ratios inside §M.6 and §F.1 are as-filed values on instruments the ledger does not consult).
- **H-4 · "Was 1996 a squeeze, not a validation?"** Run as a straight swap of the section order: FY1996 net
  sales +2,983%, gross margin 20.0%→22.0%, 4,800 Associates, five rising quarters, against working capital
  $920k→$2,270k, cash $6,248k, payables $99k→$2,852k, marketing 38.7% of sales, $(5,777)k loss, 151→(158)
  employees, one uncontracted supplier, one building. **The record supports "both, in the same sentence", and the
  volume already writes it that way** — §L l.304: "a revenue record and a solvency record on one page". The
  attack's strongest form is seasonal, and it also fails: see H-5.
- **H-5 · "'Five rising quarters' is a seasonality artefact."** Tested and it holds *against* the attacker twice
  over. (i) §Boundary l.57(v) and S2E-34/F-9 already print the null: the quarterly table begins at **Q1 1996**,
  so **no two-Christmas comparison exists anywhere inside the window**. (ii) The company's own seasonality text is
  **future tense in every instrument** — "The Company **expects that it will experience** seasonality" (No. 5
  l.604 and l.1780; 424B1 l.484, l.1658; 10-K405 l.629, l.1350) — i.e. no seasonal datum existed to confound the
  series either way. (iii) §F.3 l.362 supplies the one real seasonal test available and states it as a *pair*:
  Q4 share 53.8% of FY1996 vs 44.7% of FY1997, **on a rising base, with the FY1997 leg tagged `(PB)`**.
  **FAILED.** Residual worth one clause, not an attack: the series contains **no same-quarter pair at all**, so
  the 8,468→16,005 step from the holiday quarter into the trough is the load-bearing "fifth quarter" and it is
  being read across a seasonal boundary the company had never yet measured. Say that, and the row is sound.
- **H-6 · "Filings are being read as contemporaneous 1996 observation; §T's lineage rule is applied loosely."**
  The apparatus is present and mostly enforced: §T l.246–254 ("**A figure that appears in three of them has been
  filed once**"; the 10-K405 counted as a second document "only where it prints something the lineage does not"),
  the `(PB)` convention, C-flag 8 at `stage_2_part_1.md` l.162 ("True of the documents that exist; **not evidence
  about 1996**"), the S0806 phantom FY1996 annual report caught and sent to **U.111**, and §A.2's inventory of
  non-local witnesses (`stage_2_index.md` l.47–53 counts **6 rows** at `local_copy: NO`, of which five are
  witnesses — June-1996 release S2006, Fortune S2007, WIRED S2008, the B&N 10-K S2009, the pricing release S2012
  — and the sixth, S2005, is a documented null). **FAILED as a general charge.** Two loose applications were found and are
  already booked: **L-4** (a change dated to the accession that reproduced it, not the one that printed it — the
  §T rule inverted) and **L-1.2** (§T crediting No. 3 with a first that belongs to No. 1).
- **H-7 · "The retracted 'four days of cash' runway came back."** Re-derived from the filed lines: FY1996 net
  cash used in operations $1,735k ÷ 365 = **$4.75k/day**, so $79k ≈ **16.6 → ≈17 days**; Q4-1996 loss $2,299k ÷
  92 = $25.0k/day, so ≈**3.2 days**. §M.3 l.338–340 prints both, on named bases, and retracts the third form.
  **FAILED — the retraction is correct and the arithmetic is right.** Same test on $79,000, 4,800, 6,090, 3.4m
  advertising, 22,655k shares and the $(0.25): all re-found at the cited lines (`sources/S-1_original…l.2148`;
  `10-K_FY1997…l.1182, l.2188–2189, l.1194`).
- **H-8 · "A barred figure is being laundered."** Swept the three volumes for `2,300%`, `8,000,140`, `16 July`,
  `Cadamia`, `22 investors`, `$1.1 million`, `$245`, `Get Big Fast`, `429`, `most prosperous`, `3,000%`, `first
  employee`, `co-founder`, `world's largest`. Every hit is inside a **retraction, a bar, a `(NO LOCAL COPY)` tag
  or the company's own disclaimer of it** (e.g. `stage_2_part_1.md` l.79 "~$429m (DERIVED) … **must not be run
  backwards into a June-1996 venture valuation**"; `stage_2_part_2.md` l.408 HistoryLink's "Get Big Fast" named
  as uncited; part_2 l.258 valuation "UNKNOWN — NOT TRACEABLE"). **FAILED — this is the cleanest sweep in the
  volume set.**
- **H-9 · S2E-19's original overreach ("$18 and $54,000,000 are not filed anywhere").** Re-tested: both are on
  the 424B1 cover, l.124–125, as ST2_E's own **F-10** already concedes. **The dossier's one self-reported denial
  of a filing statement that exists did not propagate into the spine** — §Q l.99 and §B.0 l.100 cite the 424B1
  correctly, and §B.0 is even careful that the 10-K405 derivation is "arithmetic, not independence" (l.102).
  **FAILED.** Recorded here because the brief asked me to attack the attacks, and this one was already attacked
  by its own author with evidence.

---

## Unsourced or folklore elements

Items in the Stage-2 text as written whose earliest support is an inference, a superlative about the corpus, or
no document.

| # | Element | Site | Status | What it may be re-written as |
|---|---|---|---|---|
| U-1 | The offering was **priced on 14 May**, "the same morning", the ceiling "filed that morning" | part_1 l.24, l.53, l.79; part_3 l.98; claim record Q60 | **UNSOURCED AS TO DAY-PART, AND CONTRADICTED AS TO SEQUENCE** by `S-1A-No4…filed-1997-05-13.txt` l.242–243 | "the last filed ceiling ($16.00) was set on **1997-05-13** and held in two further amendments filed **1997-05-14**; the final prospectus of **1997-05-15** states $18.00. No document states an hour for any of these" |
| U-2 | "deal +20% larger than **five days** earlier" | part_2 l.305 | **UNSOURCED ARITHMETIC**, contradicted by the spine's own §Q l.95 | "…than **two days** earlier (No. 4, 1997-05-13)" |
| U-3 | No. 3 carries "the **FIRST** stated price range in the whole lineage" | part_3 l.263 (§T), repeated l.94 (§Q) | **FALSE CORPUS-INTERNAL SUPERLATIVE** | "…the first range stated **in a document the corpus holds**; Nos. 1 and 2 state $12.00–$14.00 on 21 and 29 April" |
| U-4 | "thirteen days before Amazon's amendment" / "one day after B&N's own filing" | part_3 l.93, l.96 | **OFF BY ONE AND BY TWELVE** (both) | eleven days to No. 4; twelve to No. 5 |
| U-5 | "a **founder** predicting profit 'by accident'" | part_1 l.254 | **MIS-ATTRIBUTED SPEAKER** — a journalist's relay, no local copy | "a magazine article reports the founder as saying"; carry part_1 l.67's tag at this site |
| U-6 | The Fortune 110 headcount, "over 1,800 associates in three months", the WSJ 60% and the Seattle Times 44% | part_1 l.67, l.177–178, l.350–352; part_2 l.301; §T l.271, l.274–275 | **TAGGED, NOT SOURCED** — five witnesses, no byte on disk (`local_copy: NO`) | keep, but see S-7: two of the five repeat measurements are non-local, so the *shape* of the spread is carried by unlocalised text |
| U-7 | First trading day / day-one price | part_1 l.57(ii); part_3 l.100 → **U.99** | **CORRECTLY HELD AT UNKNOWN** | no change |
| U-8 | Associates launch "July 1996" | part_1 l.187; part_3 l.107 → **U.112** | **CORRECTLY `RETRO`**, dated to a 1998 release and a 2007 timeline | no change |

Swept and clean (nothing reintroduced): the whole COR-09 barred list, the "$8m for 13%" and "$429m" valuation
family, "world's most prosperous online bookstore", "3,000%", "Get Big Fast", the 22-investor form of the angel
round, "first employee"/"co-founder", and the W-1…W-16 table of ST2_E.

---

## Single-lineage claims

Claims whose whole evidential weight rests on one printing, one instrument, or one unlocalised witness. §T's
lineage column is honest and this section adds only what it does not yet flag.

| # | Claim | Sole carrier | Why it is load-bearing | Ruling |
|---|---|---|---|---|
| S-1 | **">4,800 Associates at 1996-12-31"** | **ONE printing**: original S-1 **l.2148 only** (`sources/S-1_original_acc-0000891618-97-001309_filed-1997-03-24.txt`); degraded to "several thousand" in No. 5 l.2335 and "thousands" in 10-K405 l.362 | the second pillar of the stage thesis (repeatability without headcount) | Correctly §T-flagged as original-only. **Sharpen:** it is a *membership* count, self-registered, undefined, in a marketing section, in the only document that ever printed it, **20 months after the date it reports**. It can carry "a mechanism existed at scale outside Amazon's premises"; it cannot carry "the mechanism produced orders" — which §D.1 l.195 already says. Hold at Medium-High, not High |
| S-2 | **"up to 400,000 of more than 2.5 million"** → the 16.0% fill ceiling | one sentence, four 1997 printings, **absent from the FY1997 10-K** | §M.1's "load-bearing number of the stage" | One source, four printings, correctly ruled. The *absence* in the 10-K is inference about disclosure, not about the world; §M.1's wording already holds that line |
| S-3 | The IPO terms: $18.00 / 3,000,000 / all-primary / ten houses / 726,000-share allocations / 180-day lock-up | **the 424B1 cover and Underwriting section alone** | the endpoint itself | No underwriter document, no exchange document and no aftermarket record exists locally; the 10-K405 gives effectiveness and net proceeds only. **The boundary rests on one document's cover page.** That is a provenance ceiling, not a disproof — the price is a fact — but no Stage-2 sentence may imply the market's judgment was independently recorded anywhere |
| S-4 | Bezos 43% (original) → ~41% (No. 5), ≈51% of the vote | two states of one lineage | control claims, and §M.8's "terms that qualify control" | Correctly differential-cited at §B.0 l.101. Keep |
| S-5 | "processes **all** sales through its warehouse in Seattle"; 42,400 sq ft + ≈50,000 sq ft; "does not own any real estate" | lineage Properties/Facilities text + five dated leases (Ex. 10.28–10.32) | single-site dependence, §M.8 | The **leases are separate executed instruments**, so this is the best-instrumented single-site claim in the corpus. Not single-lineage in the weak sense. Holds at High |
| S-6 | FY1996 audited result $15,746k / 22.0% / $(5,777)k | originally **one** lineage; **now four instruments** (10-K405, FY1998 10-K, FY1999 10-K) | §A, §L, §R, §P | **The volume's weakest link in this column is now its strongest, and it has not been collected.** Caveat: the two later instruments restate the loss to $(6,246)k (L-2), so the upgrade is on net sales and margin, **not** on the loss |
| S-7 | The five-measurement repeat spread (60 / >40 / 44 / >40 / 58) | two of five points from non-local press via dossiers | §F.2's whole point | If either press item fails re-verification the spread collapses to two filed values and one post-boundary value, and §F.2's "20 percentage points / 1.5× / 22 months" arithmetic falls with it. **Register as a single-lineage dependency of a DERIVED figure** |
| S-8 | The Q1-1997 interim column ($16,005k, $79k, 256, $(3,038)k) | one accession pair (No. 5 / No. 6, one lineage) + 424B1 republication; **expressly unaudited** | the last state before the boundary | Correctly classed `FACT (interim)`. Note: Nos. 5 and 6 are the **same date**, so "two accessions" here is one day of one document — worth saying since §A.2 counts "five documents" |

---

## What Stage 2 may not claim on this record

1. **Not** that the range moved on the morning of 1997-05-14, nor that the price cleared a ceiling filed "that
   morning". The ceiling was filed **1997-05-13** (No. 4 l.242–243) and re-filed **twice** on 1997-05-14
   (Nos. 5 and 6). No document states an hour. What **is** claimable: $18.00 cleared the last filed ceiling by
   **+12.5%**, on a size filed **two days** earlier, in a document dated the following day.
2. **Not** that $12.00–$14.00 first appeared on 1997-05-09, and not that Amendment No. 3 earns a citation for it.
   It is on file from **1997-04-21**.
3. **Not** that "three FY1996 EPS bases exist in the corpus", and not that the FY1996 numerator is unchanged
   across the record. **Five bases, five documents, numerator moved from $(5,777)k to $(6,246)k** by the issuer's
   own later audited reports; FY1997 net sales and net loss likewise restated ($147,758→$147,787;
   $(27,590)→$(31,020)); FY1996 marketing and sales printed as both $6,090k and $6,081k.
4. **Not** that the B&N competitor rewrite happened "between A3 and A5", nor "one day after" B&N's filing; it is
   in **No. 4 on 13 May**, the original S-1 already had a different state, and the intervals are eleven and
   twelve days.
5. **Not** that the "not in a position at this time to estimate possible outcomes" hedge is a 424B1 discovery. It
   is in **S-1/A No. 6, filed 1997-05-14** — the last pre-pricing document.
6. **Not** that ">40% of orders" appears three times in the record. It appears **three times in each of the eight
   1997 accessions**; and correspondingly not that the priced document is independent of the self-measurement —
   the 424B1's cover carries the price and its body carries the clause three times.
7. **Not** that the FY1998/FY1999 10-Ks "are not retrieved" or that Amendments 1/2/4/6 hold UNKNOWN contents.
   They are local, they are now read, and §S row UG-4's remedy is stale.
8. **Not** that the IPO certified repeatability. Already barred at part_1 l.57(i) and by S2E-38; L-1 and L-7
   strengthen the bar rather than weaken it.
9. **Not** the four-day runway, and not "$41,079k corroborated by the 424B1". Both already retracted
   (§M.3, §Boundary l.54); re-tested at H-7 and correct.
10. **Not** a retention curve, a conversion rate, an order count, an AOV, a fill rate, a per-customer figure, a
    cross-year per-share ladder, or any FY1996 valuation. The §A.2/§S null list is accurate as far as it goes —
    **but it must now add "and no reconciliation of the FY1996/FY1997 loss restatement".**
11. **Not** that the seasonality of the five-quarter path is measurable. No Q4-1995 column exists, and the
    company's own seasonality text is future tense in every instrument.
12. **Not** that 1996 was a validation, or that 1996 was a squeeze. On the record alone it is a **financing
    sequence with a demand signal inside it**: margin rose to 22.0%, the loss rose every quarter, payables grew
    $99k→$2,852k, working capital grew $920k→$2,270k and then fell to $79k, and the firm needed an IPO to buy
    four months of operations. §L l.304 already states it correctly; the mistake would be to let §A's headline
    order imply a verdict §D.6 refuses.

---

## Boundary stress test

**The boundary survives, but not where the volume thinks it survives.**

*Where it is stronger than claimed.* The window's anchor is no longer a single registration lineage. FY1996 net
sales, gross profit and gross margin are printed identically in **four** instruments — the S-1 family, the FY1997
10-K405, the FY1998 10-K and the FY1999 10-K — which is the strongest cross-instrument corroboration anywhere in
the stage, and it is currently uncollected. And the **1996-12-31 substantive date does not depend on the price
at all**: delete §A.3 entirely and §Boundary l.42, §D.0, §D.6 and §L still hold the same three repeatability
signals (>40%, 4,800, five quarters) at the same confidences. The stage claim is therefore **not** load-bearing
on the price, which is the answer to the brief's central question.

*Where it breaks.* The endpoint's rhetorical keystone — "priced above the ceiling it had itself filed that
morning" — is a **two-day** sequence the company set in motion on **13 May**, after having moved the range once
already on **21 April**, and the price cleared a ceiling that had been re-filed **twice on the 14th**. That
converts the event from "the market seized on the company and outran it" to "the company raised its range twice
in three weeks, upsized, and sold above the top of the last one, in a firm-commitment deal, two days later".
Both readings are real; **only the second is documented.** And a price cleared above a two-day-old ceiling in a
ten-house firm-commitment deal is **as much a rarity-and-marketing signal as a validation signal** — the
underwriters took the whole 3,000,000 and the company itself warned in the same document that its growth rates
were "not sustainable". §A.3's own list of limits (capital, "visibility and credibility", $15.85 of dilution, no
insider selling) already concedes this, so the repair is to the keystone sentence, not to the verdict.

*Where the 1996-12-31 alternative is stronger than the volume allows.* Three of the stage's best facts were on
file **before** FY1996 closed, not at it: the >40% clause as of 1996-12-31 appears in a document **filed 1997-03-24
and reprinted eight times**; the 4,800 count in one document only; and the Associates acceleration is dated by a
**magazine on 1996-12-09 that nobody in this corpus holds**. The substantive date is therefore not just
"unaudited and conflicted" (l.42's reason for rejecting it) — it is **observationally empty**, because everything
that would certify 1996-12-31 arrives in 1997 paper. That is a *better* argument for the IPO boundary than the one
the volume gives, and it costs nothing to add.

*What would actually break the boundary.* Four things, named so a later pass can look:
(i) **a dated first-trade record for 1997-05-15** with a day-one close — U.99 is right that none exists locally,
and one would move the endpoint from a document date to a market date and make "the outside certified it"
literally true; (ii) **an underwriter's or exchange document of 14–15 May 1997** — the deal's terms are currently
one issuer's cover page (S-3); (iii) **a 1996-dated, non-company witness to the Associates programme's order
flow**, which is the only artifact that would let 1996-12-31 carry the repeatability claim on its own;
(iv) **an FY1996 annual report**, which S0806/U.111 has already established is very likely a phantom. Absent
(i)–(iv) the boundary is documentary, which is exactly what part_1 l.28 says it is.
**Verdict on the boundary: HOLDS, relabelled.** 1997-05-15 as the closing document date; 1997-05-13 as the date
the last ceiling was filed; 1996-12-31 as the substantive date the volume already carries; and no claim at any of
the three that the model repeated.

---

## Overall verdict

**CONDITIONAL.** Stage 2's argument does not fall apart: its repeatability case is self-limited, its failure
ledger is substantive and not decorative, its self-measurement apparatus is the best in the volume set, its
boundary claim does not depend on the price, and it launders no barred figure. **What falls apart is the
volume's account of its own documents.** Five of the six load-bearing statements about the IPO sequence are
wrong or unsourced, and all five are wrong in the same direction: they describe a compressed same-day
capital-markets shock where the local record shows a five-week sequence the company ran itself. Every one of them
was refutable **without a single web request**, from files inside `sources/` that the spine itself inventoried as
unread.

The precedent this sheet is written against is A-B1: an attack that survived three passes because nobody opened
the envelope. Here the envelope was labelled, catalogued, registered as a conflict (U.95), dated in §Q — and not
opened, and the un-opened contents changed the story's best line. That is a process finding, not a scholarship
finding, and it is the one the method should absorb.

| Class | Count |
|---|---|
| Attacks **landed** | **7** (L-1 CRITICAL, L-2 CRITICAL, L-3/L-4/L-5 MAJOR, L-6/L-7 MEDIUM) |
| Attacks **failed, evidence held** | **9** (H-1 … H-9) |
| Unsourced / folklore elements | **8** (U-1 … U-8; **U-1 … U-5 are new defects in the spine**, U-7/U-8 correctly held) |
| Single-lineage claims | **8** (S-1 … S-8; S-6 upgraded, S-3 and S-7 are ceilings, S-1 needs a downgrade of tone) |
| Claims barred on this record | **12** |
| Elements of ST2_E's 50 challenges re-tested and corrected | **2** (S2E-19 census via L-1; S2E-27 print-count via L-7) + F-12's 424B1 attribution corrected at L-5 |
| Stage-1 failure modes recurring in Stage 2 | **2 of 2 found again** (F-2/F-3 "repaired everywhere": L-6; F-1/U.97 accession mis-attribution: L-4) |
| Web requests used | **0** |

---

## Repair instructions for a separate pass

**Executor: not this auditor. Nothing above was applied.** All six first-order repairs need **no retrieval**;
two are single-field substitutions and one requires re-opening an already-registered conflict.

1. **R-1 (blocks sign-off) — re-key the price walk at seven sites.** Replace, at `stage_2_part_1.md` l.24, l.53,
   l.79; `stage_2_part_2.md` l.305; `stage_2_part_3.md` l.94, l.98; and claim record **Q60**:
   *blank (24 Mar) → **$12.00–$14.00 on 2,500,000 (Nos. 1, 21 Apr l.247–248; No. 2, 29 Apr l.234–235; No. 3,
   9 May l.222–223)** → **$14.00–$16.00 on 3,000,000 (No. 4, 13 May l.242–243; re-filed by Nos. 5 and 6, both
   14 May)** → **$18.00 (424B1, 15 May, cover l.124)**. Delete "the same morning" and "that morning"; change
   "five days earlier" to **two days**; keep +12.5% and the 20% upsize. Add "no document in the corpus states an
   hour for any 13–15 May 1997 event". Register the correction as a new appended conflict, **U.114** — do not
   renumber.
2. **R-2 (blocks sign-off) — §T's own-only-content column and the U.95 closure.** At `stage_2_part_3.md` l.263
   strike "the FIRST stated price range in the whole lineage" from the S0802 row and re-attribute to **S0802 =
   Simon & Schuster addition**; add **S0807 (No. 1, …603, 1997-04-21), S0808 (No. 2, …659), S0809 (No. 4, …822),
   S0810 (No. 6, …847)** to §T with their own-only content: No. 1 = first stated range; No. 4 = **the upsize, the
   $14–16 range, the "B&N has launched" competitor rewrite, and the assumed $15.00 basis**; No. 6 = the B&N
   litigation hedge. Then **re-adjudicate U.95 from UNKNOWN to CLOSED** with the finding, and add a
   `conflicts.csv` row. Update `stage_2_index.md`'s "1997 accessions unread" language.
3. **R-3 — FY1996/FY1997 restatement.** At `stage_2_part_2.md` **P147 (l.604)** and **§P.2 s11 (l.758)** replace
   "three FY1996 EPS bases" with **five**, delete "**numerator unchanged**", and add the two rows for
   `10-K_FY1998…l.1242/l.1244/l.1247` ($(6,246)k / $(0.06) / 111,271k) and
   `10-K_FY1999…l.1761/l.1763/l.1765` ($(6,246)k / $(0.03) / 222,542k), with the below-the-operating-line proof
   (net sales, COGS, gross profit and total opex identical). Annotate §A l.63, §A l.65, §L l.306, §M.2, §M.6,
   §Q l.105 and **P80a** that FY1997 appears as both $147,758k/$(27,590)k and $147,787k/$(31,020)k, and that
   FY1996 marketing and sales appears as $6,090k and $6,081k. Open the $469k reconciliation as a research debt
   and add it to §A.2's UNKNOWN list. **Do not change any confidence**: the as-filed values stay, they just stop
   being the only values.
4. **R-4 — B&N dates.** `stage_2_part_2.md` l.383: "Between A3 and A5" → "**Between No. 3 (9 May) and No. 4
   (13 May)**, with the original S-1 (24 Mar, l.2278) carrying a third, earlier state ('has entered into …')".
   `stage_2_part_3.md` l.96: move the row to the **1997-05-13** line and fix "one day after" → eleven days to
   No. 4 / twelve to No. 5; l.93 "thirteen days" → twelve. Attach U.97.
5. **R-5 — the No. 6 litigation hedge.** Cite `sources/S-1A-No6_acc-0000891020-97-000847_filed-1997-05-14.txt`
   for "still in the process of evaluating … not in a position at this time to estimate possible outcomes" as
   **first filed 1997-05-14, the last pre-pricing instrument**, at §M.9, §Q l.98 and U.68; correct ST2_E F-12 in
   place by **addition** (the dossier's text stays; append a dated marker, the A-B1 precedent).
6. **R-6 — Fortune tag propagation.** Add the `(NO LOCAL COPY — S2007)` tag at `stage_2_part_1.md` **l.254** and
   `stage_2_part_2.md` **l.301**, and at l.254 change "a founder predicting" to "a magazine article reporting the
   founder as saying". This is the third recurrence of the Stage-1 F-2/F-3 defect and RD-040's discipline applies:
   **a claim is repaired everywhere it is made** — sweep the string `by accident` across all five Stage-2 files
   and the `_parts/s2_*.md` mirrors before signing off.
7. **R-7 — print counts.** §T l.262 and S2E-27 l.883: "three 'over 40% of orders' prints" → "**three prints in
   each of eight 1997 accessions; zero in the FY1997 10-K405**". Add one clause to §A.3: the priced document is
   also the eighth printing of the self-measurement, so the price and the claim share one page of one instrument
   (provenance only; no confidence change).
8. **R-8 — §S row UG-4.** Strike "the FY1998 10-K" and "the FY1999 10-K" from the not-retrieved list (both
   local); keep the 1997 10-Qs/8-K and the B&N and Borders filings. Record which of the seven newly-used local
   documents arrived during Stage 2 and which arrived beside it, by reading `_MANIFEST.md` and
   `sources/STAGE3_INTAKE_MANIFEST.md` — **the distinction is the orchestrator's fact, not this auditor's
   inference.**
9. **R-9 — boundary wording, one sentence each.** §D.0 "five consecutive rising quarters" → append "**no
   same-quarter comparison exists; the company's own seasonality text is future tense in every instrument**"
   (No. 5 l.604/1780; 424B1 l.484/1658; 10-K405 l.629/1350). §Boundary l.42's rejection of 1996-12-31 → append
   "**and observationally empty: every artifact that would certify 1996-12-31 is 1997 paper**". §A.3's keystone →
   the R-1 wording.
10. **R-10 — method, one line, for the whole project.** The gate that failed here is not citation discipline but
    **inventory discipline**: a document can be registered, dated, and declared unread in the same volume, and no
    gate catches it. Propose to the method owner: *"a conflict may not be held at UNKNOWN while the document that
    resolves it is present in `sources/`; either read it or say why the read is refused."* Recurs across 49
    companies; the A-B1 shape of it.
11. **Sign-off condition.** R-1, R-2 and R-3 are blocking; R-4…R-9 are one-pass wording and register work; R-10
    is a method debt. After R-1…R-3 are applied, **AUDIT 5 may be re-run as a confirmation pass in under a
    dozen calls**, because every finding above is a line address in a file already on disk. No confidence is
    raised anywhere by this sheet, no claim is restored, and **the stage's verdict — demand repeated, economics
    not shown to repeat, the test transferred to Stage 3 unperformed — stands unchanged.**
