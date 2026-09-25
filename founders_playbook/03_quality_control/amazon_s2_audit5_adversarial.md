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
| **S-1/A No. 1**, acc. …603 | **1997-04-21** | 2,500,000 + 375,000 OA = 2,875,000 @ **$14.00** | **"between $12.00 and $14.00 per share"** | `sources/S-1A-No1_acc-0000891020-97-000603_filed-1997-04-21.txt` **l.247–248**, fee table **l.191** |
| S-1/A No. 2, acc. …659 | 1997-04-29 | 2,875,000 @ $14.00 | "between $12.00 and $14.00" | `…No2…filed-1997-04-29.txt` **l.234–235**, l.183 |
| S-1/A No. 3, acc. …755 | 1997-05-09 | 2,500,000 | "between $12.00 and $14.00"; assumed **$13.00** | `…No3…l.222–223`, l.408 |
| **S-1/A No. 4, acc. …822** | **1997-05-13** | **3,000,000** + 450,000 OA = 3,450,000 @ **$16.00** | **"between $14.00 and $16.00"**; assumed **$15.00** | `sources/S-1A-No4_acc-0000891020-97-000822_filed-1997-05-13.txt` **l.242–243**, l.187, **l.233, l.239, l.369**, l.438 |
| S-1/A No. 5, acc. …839 | 1997-05-14 | 3,450,000 @ $16.00 | "between $14.00 and $16.00" | `…No5…l.224–225`, l.173 |
| **S-1/A No. 6, acc. …847** | **1997-05-14** | 3,450,000 @ $16.00 | "between $14.00 and $16.00" | `sources/S-1A-No6_acc-0000891020-97-000847_filed-1997-05-14.txt` **l.225–226**, l.174 |
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
  are **identical in all four instruments** (`10-K_FY1998…l.1222–1227`; `10-K_FY1999…l.1733–1736`), and total
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
No. 5: *"The Company is evaluating Barnes & Noble, Inc.'s claims and intends to defend against them
vigorously"*; No. 6: *"The Company is **still in the process of evaluating** Barnes & Noble, Inc.'s claims, and
therefore **is not in a position at this time to estimate possible outcomes**. The Company intends to defend
against the lawsuit vigorously."* ST2_E **F-12** credits this wording to the 424B1 (l.4287–4289) and treats it
as one of the three points on which the amendments "differ on the points that matter"; the spine carries F-12's
attribution. **Correction:** the hedge is filed on **14 May**, in the last pre-pricing instrument, and reaches
the 424B1 unchanged. Consequence, and it is a strengthening one: on the day the deal priced above its own
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
