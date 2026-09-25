# Audit Sheet — Amazon.com (company_001) · Stage 2 · AUDIT 2 (Citation) · Run 2026-09-25

Auditor: Citation Auditor. **Independent of the producer: yes** — no line of `stage_2_part_1.md`,
`stage_2_part_2.md`, `stage_2_part_3.md`, `stage_2_claim_records.md` or `stage_2_claim_records_part_2.md` was
written by this agent. The five dossiers under `research/` were read **only after** the target sentence had been
quoted out of the assembled volumes, so that the dossier could never supply a passage the narrative lacks.
This agent also wrote none of `CORRECTIONS.md` and did not author the Audit-1 repair pass whose §Q re-anchoring is
part of what is under audit here.

**Web requests made in this run: zero.** Every document cited was tested against a byte on disk. Where the cited
document is not on disk, that is reported as an unavailable witness (DEFECT-7), never resolved by a fetch.

The question this sheet answers is the one the protocol actually poses — *does the cited document, at the cited
place, say this?* — not whether the citation is well-formatted. Format was 100% regular and told me nothing.

---

## Verdict

# **FAIL — 2 substantive mis-citations + 1 fabricated composite + 4 structural defects**

**Nothing in the four dangerous strata the tasking over-weighted is wrong about the facts.** The stage boundary
carrier, the IPO-week pricing sequence, every §P.2 arithmetic input I re-ran, and every post-boundary line anchor
I opened are all **at the cited place, saying what is claimed**. The 961 filing line references in the spine
contain **zero out-of-range pointers** and, in the ~40 I opened blind, landed on the right passage every time.

The failure is on the other side of the same question. **The volumes' quotation marks are not trustworthy even
where their line numbers are.** Of 479 claim records, **96 carry a `Passage:` in quotation marks of which not one
four-word run appears in any document on disk**, while the document they cite *is* on disk. Two of those 96 and
three adjacent narrative cells are not paraphrase-at-all but **assert something the filing reverses or never
states** — including one that inverts who holds a founder's-shares repurchase right, and one that dates a
key executive's tenure at the competitor to a range **no document in this repository contains**, which happens to
contradict the report's own reading of that hire.

Per method §11 this gate cannot pass on a repair by this auditor. Per §14 rule 4 the disagreement is reported,
not merged, and per §11 the fix is a separate pass by a different agent.

| # | Class | Items | Checked | Confirmed defects | Severity |
|---|---|---|---|---|---|
| 1 | Citation population | 242 `[T#·CLASS]`, 961 line refs, 479 records, 314 record-ID tokens, 94 exhibit refs, 113 register rows | — | 2 grammar/join | low |
| 2 | Line-reference integrity | 961 | 961 machine + 41 opened | **0 out-of-range** | — (pass) |
| 3 | Stratum A: boundary | 9 carriers | 9 | 1 (pricing-date carrier) | **high** |
| 4 | Stratum B: IPO week | 11 carriers | 11 | 0 | — (pass) |
| 5 | Stratum C: §P / §P.2 | s1–s11 + 6 §P rows | 17 | 0 factual; 2 quotation | pass / medium |
| 6 | Stratum D: post-boundary | 6 `(PB)` anchors | 6 | 1 (New Castle composite) | medium |
| 7 | Verbatim integrity | 403 testable records | 403 machine, 22 opened | **96 + 18** | **systemic** |
| 8 | Evidence on disk | 11 register rows, 88 source files | all | 5 witnesses absent | **high** |
| 9 | Local-copy identity | 2 duplicate accessions | both | 1 (17-line offset) | medium |
| 10 | Exhibit integrity | 94 refs / 12 exhibits | all | 1 conflation | low-med |

---

## 1. Procedure step 1 — the citation population as actually built

Counts are from machine extraction over the five files, not from the volumes' own self-description.

| Token class | Count | Where | Notes |
|---|---|---|---|
| `[T# · CLASS]` | **242** | part_1 141 (135×T1, 6×T2) · part_2 68 (67×T1, 1×T2) · part_3 33 (23×T1, 9×T2, 1×T3) | **0 in the claim-record spine** — the appendix carries `Tier:`/`Class:` fields instead, so the two halves of the spine tag evidence in incompatible grammars (see §7) |
| filing line refs `l.NNNN` / `ll.NNNN–NNNN` / `LNNNN` | **961** | part_1 114 · part_2 264 · part_3 154 · records 320 · records_pt2 109 | 762 resolve to a canonical accession from the nearest preceding alias on the same line; 199 sit in compound cells where the document is named in an earlier column — re-read by hand, **all 199 are resolvable**, none is orphaned |
| claim records | **479** | 409 + 70, as indexed | **0 duplicate ids, 0 missing ids** in A01→T40 and U.44→U.113 — the id-continuity claim in `stage_2_index.md` verifies |
| record-ID tokens cited (`S2A-*`…`S2E-*`) | **314 distinct** | all five files | **310 resolve** into the five dossiers. 4 do not: `S2B-X-2/-4/-5/-10` — these are the ST2_B cross-check table rows keyed locally as `X-2`…`X-10`, so an exact id join fails while the referent exists. Grammar, not phantom |
| exhibit references | **94** (12 distinct) | 2.1×22, 10.28×14, 10.2×11, 10.29×11, 10.31×9, 10.32×9, 10.30×4, 10.6×4, 10.12×4, 10.22×2, 10.13×2, 23.1×2 | tested for existence in `S-1_original_acc-…` — see §8 |
| `sources.csv` rows | 113 total, **11** Stage-2 | register | **only `S2001` is ever keyed by source_id anywhere in the Stage-2 text.** The other ten are reachable only by matching a title string, so the appendix→register join is nominal (§7) |

Two files carry **two byte-different local copies of the same accession** and both are in the population:
`S-1_original_acc-…1309_filed-1997-03-24.txt` (27,476 l / 1,445,709 B) vs `s1_original_0000891618-97-001309.txt`
(27,459 l / 1,444,013 B); `S-1A-No5_acc-…839_filed-1997-05-14.txt` (5,120 l / 303,069 B) vs
`s1_0000891020-97-000839.txt` (5,103 l / 301,685 B). This is DEFECT-6, and it is the one that will silently
mislead the next auditor.

---

## 2. Sampling plan (executed)

Random sampling would have been worthless here: the format is uniformly excellent. Strata were chosen by which
claims the stage cannot survive losing.

- **S-A · The boundary (9 citations).** part_1 l.12-13 (three-date cluster), l.22, l.36 (stage definition), the
  boundary table rows at l.46-53, and the 10-K405 `l.1126` effectiveness pointer.
- **S-B · IPO-week pricing sequence (11).** The four dated states: blank range → $12–14/2,500,000 (No. 3) →
  $14–16/3,000,000 (No. 5) → $18.00 (424B1), plus the all-primary claim and the discount/proceeds table.
- **S-C · §P / §P.2 (17).** Every `s1`–`s11` arithmetic input, plus §P rows P91, P153, P157, P170, P181.
- **S-D · Post-boundary (6).** Each `(PB)` anchor in the 10-K405 and the firewall's barred-value list.
- **S-E · Whole-spine sweep.** All 403 records carrying a testable `Passage:`, machine-tested for verbatim
  presence across all 88 local documents — reported at §5 with its honest denominator and its false-positive rate
  measured by hand, because a citation audit that manufactures phantom defects is as damaging as one that misses
  real ones.

---

## 3. STRATUM A — the stage boundary. Verdict: **one leg exact, one leg unbacked**

**PASS, cited to the line.** The header asserts the effectiveness leg and names its carrier
(part_1 l.12-13: *"the three-date cluster is disclosed at part_1 l.18 and the 10-K405 (l.1126) governs the
effectiveness day"*). Opening `10-K_FY1997_acc-0000891020-98-000448_filed-1998-03-30.txt` at l.1124-1126:

> "The Company's registration statement under the Securities Act of 1933, as amended, for its initial public
> offering (the "Registration Statement") became **effective on May 14, 1997.**"

Exact, and `grep` confirms l.1126 is the **only** line in that document containing "May 14, 1997". The
effectiveness date is correctly placed, correctly attributed to the only independent Tier-1 witness, and the
header's instinct to route the effectiveness day through the 10-K rather than through the lineage is right.

**DEFECT-3 (high) — the pricing leg of the boundary has no carrier on disk and no register row.**

The same header prints the boundary as *"1997-05-14/15 … 05-14 registration effective **and priced at $18.00 on
3,000,000 all-primary shares**"*. The effectiveness half is carried. The **pricing-on-14-May** half is not:

- `grep` for `May 14, 1997` across the five canonical accessions returns it in **No. 5 only at l.5114 and No. 6 at
  l.5093 — the signature date of the amendment**, not a pricing statement. No. 5's own cover (l.225) still says
  the price is *estimated* "between $14.00 and $16.00".
- The 424B1 carries $18.00 (l.124) but is dated/filed **15 May** — l.153: *"The date of this Prospectus is
  May 15, 1997."*
- `press.aboutamazon.com/1997/5/amazon-com-inc-announces-initial-public-offering-of-3-000-000-shares…` — the
  witness `S2A-53` reaches for — **has no local copy and is not registered: `sources.csv` has 6
  `press.aboutamazon.com` rows, all Stage-1 (S0606, S0609, S1701, S1703, S1711) or the June-1996 release (S2006).
  There is no Stage-2 row for the pricing announcement at all.**

So: **no document in this corpus states that the offering was priced at $18.00 on 1997-05-14**, and the one
document that would is not registered. This is the same species as the defect Audit 1 found at §Q ("attributed to
a Tier-1 instrument a date it demonstrably lacks"), in a more consequential cell — it is the boundary itself.

Two mitigations are real and should be said plainly: (i) the corpus **does** disclaim the adjacent trap — the
header's "What the boundary does NOT claim (ii)" correctly refuses the first trading day, and `S2A-53` in the
dossier says in bold *"the first trading day (1997-05-15) is NOT established by any Tier-1 document in this
corpus… Do not assert 'Amazon began trading on 14 May.'"* The specialist was careful; the header was not. (ii) The
repair is cheap: split the boundary label into "effective 05-14 [10-K405 l.1126, T1]" and "priced at $18.00,
announced 05-14 [company release, **no local copy — UNVERIFIED**]; price first printed in the 424B1 of 05-15
[T1, l.124]".

**Minor, same cell:** the header's self-pointer `part_1 l.18` lands on the volume H1
(`# FORENSIC LONGITUDINAL DATASET — AMAZON.COM, STAGE 2 (1 JANUARY 1996 – 15 MAY 1997)`), which carries **one** of
the three dates. The cluster is on **l.22**. A self-citation that misses by four lines is the only kind of
line-reference error this spine contains, so it is worth naming.

The rejected-boundary rows and the substantive-1996-12-31 row were also opened. The three figures they rest on
verify: `>4,800` Associates at **ORIG l.2148** ("which included over 4,800 registered members as of December
31, 1996"); the five rising quarters at **No. 5 l.1666** (`875 / 2,230 / 4,173 / 8,468 / 16,005`); and the
unaudited flag on that quarterly path at **No. 5 l.3729** `(UNAUDITED)`. The boundary row's compound citation
*"S-1 l.2147-2152; No. 5 l.2335-2344"* for the **degrading** Associates metric is *correct on both halves* —
No. 5 l.2336 says "several thousand enrolled members", which is the degradation the cell is describing. I
initially scored that as a mis-anchor and it is not.

---

## 4. STRATUM B — the IPO-week pricing sequence. Verdict: **PASS, entirely. Cleanest cell in the stage.**

Every one of the eleven carriers was opened at the cited line and every one is right.

| Claim as printed | Cited place | What is actually there | Verdict |
|---|---|---|---|
| "$18.00 … $1.26 … $16.74 / $54,000,000 … $50,220,000 … before $850,000" | 424B1 cover l.124 | l.124 `Per Share $18.00 $1.26 $16.74`; l.125 `Total(3) $54,000,000 $3,780,000 $50,220,000`; l.131 `Before deducting expenses estimated at $850,000` | **EXACT** |
| "3,000,000 shares all primary, 'sold by Amazon.com, Inc.'" | 424B1 l.102-103, l.227 | l.102-103 *"All of the 3,000,000 shares of Common Stock, par value $0.01 per share ("Common Stock"), are being sold by Amazon.com, Inc."*; l.227 `Common Stock offered … 3,000,000 shares` | **EXACT** (the ellipsis in the record is legitimate) |
| "$12.00–$14.00 / 2,500,000 (9 May)" | S-1/A No. 3 | l.215 `2,500,000 SHARES`; l.219-223 *"the initial public offering price will be between $12.00 and $14.00 per share"* | **EXACT** |
| "$14.00–$16.00 / 3,000,000 (14 May)" | S-1/A No. 5 | l.217 `3,000,000 SHARES`; l.221-225 *"between $14.00 and $16.00 per share"* | **EXACT** |
| "one source in four dated states; the differential is the evidence" | header rule | `2,500,000` occurs in **No. 3 and not in No. 5**; `3,000,000` in **No. 5 and not in No. 3** | **EXACT** — the four states are genuinely four different documents, which is what makes the lineage rule true rather than decorative |
| "$18.00 = +12.5% over the last filed ceiling; 20% upsize" | [S2A-38/39/53, S2B-31/33/36] | 18.00÷16.00−1 = 12.5% ✓; 3,000,000÷2,500,000 = 1.20 ✓, both inputs from the four lines above | **PASS** |
| "no selling stockholder was monetised" | P91 / K23 | no `Selling Stockholders` line exists in the 424B1 | **PASS** |
| "450,000-share option … whether exercised UNKNOWN" | 424B1 l.132-136, K28 | l.133 `450,000 additional shares`; l.135-136 gives the if-exercised-in-full totals | **PASS**, and the null is honest |
| "market cap 23,858,702 × $18.00 ≈ $429m" | 424B1 l.228 | l.228 `Common Stock to be outstanding after this offering … 23,858,702 shares` | **PASS** |
| "the 10-K405 states no price" | B118 | `18.00` is **absent** from the 10-K405 | **PASS** |
| "7.00% gross spread" | 424B1 l.124 | 1.26 ÷ 18.00 = 0.0700 ✓ | **PASS** |

The filing-lineage discipline the header preaches is, in this cell, actually practised: the volumes never present
the four states as four witnesses. That is the single most important methodological claim Stage 2 makes about
itself, and it holds.

---

## 5. STRATUM C — §P and §P.2. Verdict: **every number survives; two quotation classes need labelling**

I re-ran the arithmetic and opened the cited line for s1–s11 and six §P rows. **No §P or §P.2 figure is wrong,
mis-based, or carried from a line that does not contain it.** Specifics, all verified:

- **s1** — `NO5 l.4687` *"On June 21, 1996, the registrant issued 569,396 shares of Series A Preferred Stock"*;
  `l.4151-4152` (Note 3, month-only "In June 1996"); `l.3061` (Certain Transactions, 555,161 + 14,235 at $14.05);
  `l.3686` (balance-sheet caption 569,396 / 574,396). All four anchors exact. **Bonus:** the record's
  "conversion above a split-adjusted $3.33" and the two conversion totals reconcile — Item 5 ¶6 at l.4688 says
  569,396 → **3,416,376** while Certain Transactions at l.3071 says all Series A → **3,446,376**; the difference is
  exactly 30,000 = the 5,000 January/February-1997 director shares × 6, and 3,416,376 ÷ 569,396 = 6.0001. Both are
  right, and neither is presented as corroborating the other.
- **s2/s3** — `10-K405 l.1380` prints `Net sales … $147,758 838% $15,746 2,981% $511` (the "2,981%" is **the
  company's own rendering**, so the retraction of the received "≈3,081%" is correctly argued, not asserted);
  `l.1402-1403` prints gross profit `28,813 / 3,459 / 102` and margin `19.5% / 22.0% / 20.0%`.
- **s4** — `NO5 l.1702` prints the quarterly margin path **20.6 / 21.4 / 21.8 / 22.3 / 22.0** exactly as s4
  claims, and `l.1666-1669` the sales/gross-profit inputs (16,005 / 3,521). The correction that 19.5% is
  FY1997-annual and *not in this stage* is right and is the kind of finding this gate exists to keep.
- **s11** — `NO5 l.3729-3752`: 3,459 − 9,438 = (5,979) ✓ l.3744; (5,979) + 202 = (5,777) ✓ l.3747;
  (5,777) ÷ 22,655 = (0.2548) → $(0.25) ✓ l.3749 with the share count at l.3752. The rejected received set
  (3,462 − 6,498 = (3,036), $(0.18)) is indeed unreachable — the denominator it needs, 16,867k, is printed nowhere.
- **§A's resource discontinuity** — `NO5 l.396-399`: `Working capital … 79 / 41,079`; `424B1 l.276-279`:
  `79 / 49,449`. The header's warning that "No. 5's $41,079k runs on its assumed $15.00" is borne out at
  `NO5 l.173`, which sizes the table at `$16.00`. **This is a two-document, two-assumed-price cell rendered
  correctly.**

**DEFECT-4 (quotation class) — §P.2's own prose carries non-filed quotation.** R16 and G36 both print
*"The Company records revenue when the order is shipped."* / *"revenue is recognized when the order is shipped"*.
The filed sentence, at **`NO5 l.4038-4039`** and again at `10-K405 l.2175-2176`, is:

> "The Company recognizes revenue from product sales, net of any discounts, **when the products are shipped to
> customers.**"

"The order is shipped" appears in no document. Same at R18/K21, which print *"we have received $2.0 million and
$8.2 million…"* — first-person plural, a voice the registrant never uses about itself — where `NO5 l.1797-1799`
reads *"the Company has financed its operations primarily through private sales of Common Stock and Preferred
Stock which, through March 31, 1997, totaled $2.0 million and $8.2 million, respectively."* **U.92** prints
*"approximately 50,000 square feet"*; `NO5 l.2599` says *"an approximately 50,000-square-foot **facility**"*.
**A01** prints `"Net sales… $511 $15,746 $147,758"` as a `Passage:` — the three figures are all filed, but in that
ascending order in no single document, and the third term is post-boundary.

None of these five changes a number or a conclusion. All five are quoted as if verbatim. That is the defect.

---

## 6. STRATUM D — post-boundary `(PB)`. Verdict: **5 of 6 exact; 1 fabricated composite**

Every `(PB)` anchor resolves: `10-K405 l.323` *"Gift Center. In November 1997, Amazon.com launched its Gift
Center"* ✓ · `l.243` *"Repeat customers currently account for over 58% of orders"* ✓ (with l.242's 1.5m accounts) ·
`l.235-236` *"intends over time to expand its catalog into other information-based products, such as music"* ✓ ·
`l.1414-1416` *"20% and 30% discounts on more than 400,000 titles, with featured titles discounted at 40% and
certain 'special value' editions discounted up to 89%"* ✓ · `l.1646-1647` *"In November 1997 the Company opened a
200,000-square-foot distribution center in Delaware and expanded its Seattle distribution center to 85,000 square
feet"* ✓. The firewall's *barred list* is also honestly applied — I found no `(PB)` value standing in a Stage-2
state cell in the six I opened, consistent with Audit 1's finding that exactly one such breach existed and was
repaired.

**DEFECT-5 (medium) — "New Castle" is quoted into existence.** `D32` prints, in quotation marks,
*"In November 1997, the Company opened a distribution center in New Castle, Delaware."* **No such sentence exists
in any document on disk.** It is a splice of two passages: the event, from `10-K405 l.1646-1647` (which says
"Delaware" and *not* "New Castle"), and the place-name, from `l.1073-1075` in Properties —
*"...and in a 200,000-square-foot facility located in **New Castle, Delaware** under a lease that expires in
October 2002."* The splice happens to be true; the quotation mark is a lie about it.

The same over-reach appears un-quoted in two narrative cells that cite only the event line for the place-name:
`part_1 l.242` (`| New Castle, Delaware DC | … | 10-K405 L1647 |`) and `part_1 l.409`
(`… 200,000 sq ft DC at New Castle, Delaware … | 10-K405 l.1646-1653 |`).
**`10-K405 l.1075` is the only local carrier of "New Castle" and not one Stage-2 citation points to it.** Fix: cite
`l.1646-1647 + l.1075` jointly, and re-render D32's `Passage:` as two quotes or as `NO_VERBATIM_PASSAGE_RECORDED`.

---

## 7. The systemic finding: **quotation marks outrun the record in 96 of 479 records**

Method. For each of the 403 records carrying a testable `Passage:`, I split the quote at its own ellipses and
dashes, normalised both sides (EDGAR dot-leaders, `<PAGE>` junk, `<TABLE>`/`<C>` markup, curly quotes, hyphenated
compounds) and required every resulting ≥4-word run to appear in the concatenated text of **all 88 local source
documents**. Then I opened 22 of the hits by hand.

| Class | Records | Meaning |
|---|---|---|
| **A — verbatim, contiguous** | **148** | the quote is the document's own words in one run |
| **B — elided composite, every run verbatim** | **40** | legitimate: `…` marks a real elision and each side checks out |
| **C — mixed** | **18** | some runs verbatim, at least one not |
| **D — no ≥4-word run found in any local document, cited document IS on disk** | **96** | **the quotation marks assert something no document says** |
| **E — untestable: cited document not on disk** | **38** | see DEFECT-7 |
| no quote field / short-meta | 139 | `NO_VERBATIM_PASSAGE_RECORDED`, or a non-document string |

**Honest false-positive rate for class D, measured not assumed.** Of the 22 class-D records I opened by hand,
**8 were my harness's fault, not the text's**: long quotations crossing a `<PAGE>` break (B97 — whose `l.986`,
`l.1055`, `l.1062-1064` anchors are all *exact*), table-row composites whose numbers are filed but not contiguous
(A01, Q42, G34), and hyphenated-compound singular/plural drift (U.92's "50,000 square feet" vs filed
"50,000-square-foot facility"). **14 of 22 were genuine non-verbatim quotations**: re-worded prose printed inside
quotation marks (R16, G36, R18, K21, B99, B103, B104, B108, B109, B110, D32, U.79, C37, B100).

So the true class-D rate is somewhere between **~60% and 100% of those 96**, and the honest statement is:
**roughly one record in eight presents a paraphrase as a quotation.** The facts behind essentially every one I
tested survived; the *evidentiary form* did not.

Why this matters more than it sounds. The appendix's front matter declares: *"Nothing in the narrative was
upgraded, rounded, merged or re-classed here: every … Passage field is the specialist's or the filing's own
string."* That sentence is **not accurate for the `Passage:` column**, and it is the one sentence in the file that
tells a downstream reader they may trust a quotation mark without opening the document. Stage 1's AUDIT 2 opened
**RD-024** on the same column for missing *fields*; this is the same column failing on *content*, and it is the
more serious of the two.

**The repair I would not make, stated so the next agent does not over-correct.** Do not rewrite 96 quotations from
memory. Re-derive each from the line its own record cites — in 14 of 14 hand-tested cases the correct verbatim was
reachable in one `grep` — and where the narrative needs a paraphrase, tag it `PARAPHRASE (not the filing's
words)`, which the corpus already has a grammar for (`NO_VERBATIM_PASSAGE_RECORDED`).

---

## 8. Two defects that change a reading, not just a wording

### DEFECT-1 (HIGH) — `B110` dates a competitor's tenure to a range that exists in no document, and the range contradicts the report's own argument

`stage_2_claim_records.md` l.131, `B110`, `Passage:`:

> "Scott E. Lipsky has been Vice President, Business Expansion of the Company since July 1996 and was Chief
> Information Officer of the superstore division of Barnes & Noble **from 1993 to 1995**."

The filed biographies say, in both accessions, **March 1994 to July 1996**:

- `NO5 l.2727-2731`: *"Mr. Lipsky joined the Company in July 1996 as Vice President of Business Expansion.
  **From March 1994 to July 1996**, Mr. Lipsky served as Chief Information Officer of Barnes & Noble, Inc., a
  national trade bookstore chain, and Chief Technology Officer of Barnes & Noble College Bookstores, Inc."*
- `ORIG l.2509-2512`: same dates, different divisional language — *"**From March 1994 to July 1996**, Mr. Lipsky
  served as Chief Information Officer of **the superstore division**, and Chief Technology Officer of the college
  division, of B&N."*

Three separate errors in one field:

1. **`"from 1993 to 1995"` is in no document.** `grep` across all 88 sources returns zero hits for
   `1993 to 1995` in any Lipsky context; repo-wide, **the only occurrence of that string in this corpus is
   `B110` itself.**
2. **Wrong accession.** The phrase "superstore division" is in the **original of 1997-03-24** and **not in
   No. 5**, whose bio names the corporate entity instead. B110 cites `S-1/A No. 5 … Source date: 1997-05-14`.
   (The *dossier* `S2D-61` cites `NO5 l.2727-2731` with No. 5's correct words — the accession error entered at
   assembly, not in research.)
3. **The invented range destroys the claim it supports.** `part_3 l.55` argues *"The incumbent's
   fulfilment-systems chief crossed over **in the month the Series A money landed**"* — filed dates (B&N until
   July 1996, Amazon from July 1996) are precisely what make that sentence true. "1993 to 1995" would have him
   gone a year before the crossover. A defect that is also self-defeating is the easiest kind to fix and the worst
   kind to leave.

Also implicated: `U.79`'s `Passage:` *"Scott E. Lipsky … previously Chief Information Officer of the superstore
division of Barnes & Noble."* — the words are the **original's** (l.2510-2511) but the record cites
`S-1/A No. 5 / 1997-05-14`. And `part_1 l.443`, `part_2 l.97`, `part_2 l.627`, `part_3 l.55`, `Q29` all assert
"B&N superstore division" against a No. 5 anchor. **Recommendation:** re-key all six to
`S-1 (orig.) l.2509-2512` **and** `S-1/A No. 5 l.2727-2731`, present the two phrasings as the accession
*differential* the header already promises (Nos. 1/2/4/6 unread aside), and delete "from 1993 to 1995".

### DEFECT-2 (HIGH) — `B100` inverts who holds the repurchase right over Bezos's 612,000 shares

`stage_2_claim_records.md`, `B100`: *"A conditional control term bound 612,000 of Bezos's own shares to the
Series A, **repurchaseable by the investor** at one-tenth of a cent until 1999-06-21"*, `Passage:`
*"612,000 shares of Common Stock held by Mr. Bezos are subject to repurchase at $.001 per share through June 21,
1999."*

Filed, at `424B1 l.2969-2973` and `NO5 l.4176-4181`:

> "In June 1996, in connection with the Company's Series A Preferred Stock financing, **Mr. Bezos granted the
> Company a right to repurchase 612,000 shares of Common Stock held by him at $0.0010 per share if his employment
> terminates under certain circumstances.** The Company's right of repurchase lapses ratably over the 36-month
> period ending June 21, 1999."

The holder is **the Company**, not the investor; the trigger is **termination of employment**; the lapse is
**ratable over 36 months**, not a cliff "until 1999-06-21". The quoted string is in no document
(`subject to repurchase at $.001` → 0 hits; `through June 21, 1999` → 0 hits). This is an unvested-founder-stock
retention device — the opposite polarity from an investor claw-back.

The condition is what makes it *founder-control* evidence, and the drop of the condition is what lets §A.1 read
it the wrong way. `part_1` §A.1 lists *"conditional control (612,000 of Bezos's own shares repurchaseable at
$0.0010 to 1999-06-21)"* among the costs Bezos paid for KPCB's money. On the filed text the Company holds the
right, so this term **bound Bezos to stay**, and it is evidence about his commitment, not about KPCB's leverage
over him. `510,000 shares … subject to repurchase` at 1996-12-31 is also filed and also unclaimed.

**Both source dossiers are right, and `part_1` §A.1 is weaker than `B100`, not wrong in the same way.**
`S2B-54` writes *"granted **the Company** a repurchase right over 612,000 of his own shares at $0.0010"*, and
`S2E-47` quotes `NO5 l.4176-4181` **verbatim including the termination condition and the 510,000 figure**.
`part_1` §A.1 **omits the holder**; only `B100` **reverses** it. Repo-wide, the string `by the investor` occurs in
exactly one file — `stage_2_claim_records.md` — so the reversal is a claim-record transcription failure, in the
one direction that flatters the argument being made — which is the exact failure mode the hindsight firewall is there to catch, and
`S2E-47` had already caught. **Recommendation:** B100's `Passage:` ← `S2E-47`'s verbatim; holder = Company; add
"if his employment terminates"; re-word §A.1's "conditional control" to "unvested founder stock: the **Company**
could repurchase 612,000 of Bezos's shares at $0.0010 on termination, lapsing ratably to 1999-06-21". The Series
A's *control* price remains a board seat, which is the header's actual point and does not need this leg.

---

## 9. DEFECT-7 (structural, HIGH) — **the non-SEC evidence base has no bytes on disk**

`sources/` holds **88 `.txt` files, of which 86 are SEC documents** and two are HistoryLink and Sheff/Playboy
(both Stage-1). **Amazon's periodical set is empty.** Compare `company_002_walmart/sources/periodicals/`, which
exists. The harvest machinery is in the repo (`tools/periodical_harvest.py`); it was never run to disk for
company_001's Stage 2.

Five of the eleven Stage-2 register rows have no local copy, and each is honest about it — `S2006` *"restoration
pending - not held locally"*, `S2007` `NOT HELD`, `S2008` *"restoration pending"*, `S2009` *"not held locally"*,
`S2005` a documented null. **The register is more honest than the narrative.** The volumes cite these as
`[T2]`, `[T1 · FACT]` and `Conf: High` with no in-cell indication that the witness is absent:

- **Fortune 1996-12-09** carries `§A`'s single most quotable line — *"If we are profitable within the next two
  years, it will be by accident"* (`A06`, `U.44`, `U.77`, `U.81`, `U.83`) — plus "employs 110", "declined to
  disclose revenue", "well over $10 million". **None is on disk.** §A's "Failure stayed arithmetically live"
  paragraph rests entirely on it.
- **WIRED 1996-12-16** (`E46`, `F30`, `U.85`) — "425,000 titles", "1.6% of the online shopping market".
- **B&N Form 10-K, filed 1997-05-02** (`S2009`) — `U.80` is built on it and calls that pairing
  *"**genuinely independent issuers — the only such pairing in this stage**"*. The stage's one true
  two-issuer corroboration therefore **rests on a document with no byte on disk and no way to check the
  53-week basis warning that `S2009` itself flags**. That is the highest-value row in §P outside the
  financials (the volume's words) and the least verifiable.
- **LA Times 1996-12-11**, **Seattle Times**, **WSJ via Stage 1** (`F28`), **CSM 1996-09-18** (`F31`).
- Plus, from §3: **the 1997-05-14 pricing release**, which is not even registered.

This is why **38 records are untestable (class E)**: not a defect in those records, but a wall in front of them.
**Recommendation:** open as **research debt, not a repair** (method §11 — findings requiring retrieval are debt):
intake the four periodicals + the B&N 10-K + the 1997-05-14 release into `sources/periodicals/`, add the missing
`sources.csv` row for the pricing release, and add a `local_copy: yes|no` flag to every register row so the
narrative can inherit it. **Until then, `U.80`, `§A`'s Fortune paragraph and `P164` should print a visible
`(NO LOCAL COPY — unverifiable at the citation)` tag**, exactly as they already print `(PB)`. The corpus has the
tagging discipline; it just isn't applied to this axis.

## 10. DEFECT-6 (structural, MEDIUM) — two local copies of one accession, 17 lines apart, and the spine never says which

`l.NNNN` across this stage is keyed to the `_acc-…_filed-…` copies. The bare-named twins differ by exactly the
provenance header (303,069 − 301,685 = 1,384 B = 17 lines), and every reference is then off by 17 in the other:

| Probe text | canonical (`_acc-`) | twin (`s1_…`) |
|---|---|---|
| `expanded from 11 to 151` (ORIG) | **l.667** | l.650 |
| `Per Share` (ORIG) | l.228 | l.211 |
| `Mr. Lipsky served` (ORIG) | **l.2510** | l.2493 |
| `expanded from 11 to 256` (No. 5) | **l.796** | l.779 |
| `Mr. Lipsky served` (No. 5) | **l.2728** | l.2711 |

The twins are not referenced by any register row and appear to be pre-header restorations. **Recommendation:**
either delete them, or state once in `stage_2_index.md`/`_MANIFEST.md` that *all `l.NNNN` in the Stage-2 spine are
lines of `sources/<FORM>_acc-<ACCN>_filed-<DATE>.txt`*. Left as they are, the next auditor greps the twin,
finds the sentence 17 lines early, and reports 900 phantom citation failures.

## 11. DEFECT-9 (LOW, ×3) — grammar and join

1. **`S2B-X-2/-4/-5/-10`** — cited with a dossier prefix the dossier does not use (ST2_B keys those rows `X-2`
   … `X-10` in a table). All four resolve by hand; none resolves by id join.
2. **Register join unused** — 10 of 11 Stage-2 `sources.csv` rows are never keyed by `source_id` in Stage-2 text
   (only `S2001`). This repeats Stage 1's AUDIT 2 finding on **RD-024** (URLs only in §T, keyed by name). It was
   not carried forward and is now a two-stage defect.
3. **`T#` tokens exist only in the narrative** — the claim-record spine tags tier as a `Tier:` field, so
   `[T1 · FACT]` in part_1 cannot be joined to the record that evidences it without a manual name match. Two
   grammars for one load-bearing tag.


---

## 12. Passes that must be recorded, with the line that proves each

The protocol forbids softening a verdict, and forbids manufacturing one. These are the clean results, each cited.

| # | Pass | The line that proves it |
|---|---|---|
| **P-1** | **961 filing line references, zero out-of-range pointers.** The single machine-flagged candidate (`l.18509` in `U.82`) is valid: `ORIG l.18509` reads *"to Wells Fargo Bank and Seafirst Bank (along with any successors in"* — my resolver had mis-paired it to No. 5 from an earlier alias in the cell | `S-1_original_acc-…1309…txt` l.18509; every other ref ≤ its file length (27,476 / 5,187 / 5,120 / 4,404 / 10,815) |
| **P-2** | **~41 references opened blind all landed on the cited passage.** Selection was by adversarial value, not convenience | e.g. `NO5 l.796`, `l.1055`, `l.1666`, `l.1702`, `l.2336`, `l.2599`, `l.2695-2704`, `l.2719-2721`, `l.2727-2731`, `l.3061`, `l.3627-3631`, `l.3686`, `l.3729-3752`, `l.396-399`, `l.4151-4152`, `l.4687`; `424B1 l.124-131`, `l.153`, `l.227`, `l.276-279`, `l.1073` region, `l.2259-2261`, `l.2969-2973`; `ORIG l.666-667`, `l.986`, `l.2148`, `l.2509-2512`; `10-K405 l.243`, `l.323`, `l.1126`, `l.1380`, `l.1402-1403`, `l.1414-1416`, `l.1646-1647`, `l.2057`, `l.2175-2176` |
| **P-3** | **The filed exhibits are inside the saved primary and their numbers verify** — 38 `<TEXT>` parts and 38 `<TYPE>` markers, 37 of them `EX-` (the S-1 original); `EX-10.28`@l.18623, `EX-10.29`@l.21165, `EX-10.30`@l.22870, `EX-10.31`@l.23348, `EX-10.32`@l.26014 | 12,686 @l.18767 · 11,809 @l.20649 · 11,814 @l.20650 · 6,091 @l.20905 · 50,420 @l.21191 · 93,020 @l.21192 · $18,152/mo @l.21205 · commencement "November 1, 1996" @l.21203 |
| **P-4** | **`B111`'s 42,400 sq ft is honestly DERIVED, not a quotation from a lease** — the four addends are exhibit lines, the total appears only in the Facilities prose. Sum re-run: 12,686+11,809+11,814+6,091 = **42,400** ✓ | total at `ORIG l.2379`; addends at P-3 |
| **P-5** | **Stage-2 id continuity claim is true**: 479 records, 0 duplicates, 0 gaps, A01→T40 + U.44→U.113 + U.111a | machine parse of both appendix files |
| **P-6** | **The four dated IPO states are four different documents** — the lineage rule is load-bearing here, not decorative | `3,000,000` absent from No. 3; `2,500,000` absent from No. 5 |
| **P-7** | **`U.75`'s chronology-repair claim verifies exactly**: the 11→151 sentence is anchored to **January 1, 1996** in the original and the 11→256 sentence to **December 31, 1995** in No. 3/No. 5; the four/five-month variance is likewise real | `ORIG l.666-667` · `NO3 l.796-799` · `NO5 l.795-798` |
| **P-8** | **`U.110` is correct against the register**: S0804 really does bar a document now on disk | `sources.csv` S0804 `claim_supported`: *"The 424B1 itself is NOT in the restored primary set, so nothing in this register may rest on it…"* vs the 266,755 B 424B1 in `sources/` |
| **P-9** | **The E&Y opinion is verbatim and the going-concern null is safe** | `NO5 l.3627-3631` *"In our opinion, the financial statements referred to above present fairly, in all material respects…"* |
| **P-10** | **The one Tier-3 token in the whole stage is correctly placed and correctly labelled a retrospective recollection**, not filed evidence | `part_3 l.127` `Kaphan 2011 [T3 · RETRO]` |
| **P-11** | **`D19`'s ">4,800 registered members" is verbatim in the original** and `part_1 l.269`'s compound citation (No. 5 "several thousand") correctly shows metric degradation rather than mis-anchoring | `ORIG l.2148` · `NO5 l.2335-2336` |
| **P-12** | **The post-boundary firewall holds in the cells opened**: every `(PB)` value in the barred list I checked is tagged, and the two §F.3/§C FY1997 legs Audit 1 flagged are now tagged | `part_1 l.273`, `l.282`, `l.295` each carry `(PB)` / "post-boundary" / "consequence only" |

---

## 13. DEFECT-8 (LOW-MEDIUM) — exhibit quotations conflate two leases and drop a material tail

`B112` and `Q18` print, against **Exhibit 10.31 (Coast Wide)** *and* **10.30 (Filson)**:
*"Sublease … 2250 First Avenue South … **the permitted use is general offices, sale and distribution of books**."*

Two different exhibits, two different clauses, merged into one quotation:

- **Ex-10.31 (Coast Wide), `ORIG l.23387-23388`**: *"The **"Allowed Use"** of the Premises is for general offices,
  sale and distribution of books **& other products**."*
- **Ex-10.30 (Filson), `ORIG l.22988-22991`**: heading **"8. PERMITTED USE"** — *"Filson shall use the Premises
  for general office, storage, manufacturing and distribution and for no other purpose…"* — no mention of books.

The phrase "permitted use" is 10.30's heading; the "sale and distribution of books" is 10.31's "Allowed Use"; and
**the quote drops "& other products."** That tail is not decorative for this stage: §Rejected (iii) turns on
"Amazon never stopped being a bookseller" inside the window, and the stage's own sublease says *books & other
products* in 1996. The truncation removes the one non-prospectus, in-window hint at multi-product distribution —
the exact category the boundary argument is about.

`B114`/`U.89` are the same species one level down: quoted *"Each schedule delivered under this Master Lease is a
'Finance Lease.'"* vs filed **`ORIG l.26077-26078`** *"Lessor and Lessee agree that **each Lease** is a 'Finance
Lease' as defined by Section 103 of Article 2A of the Uniform Commercial Code."* Different subject; the substance
(leases are finance leases) holds.

---

## 14. Register of defects for the repair pass

Severity is about what breaks if it is left, not about how loud it is.

| ID | Locus | Printed | Filed / actual | Class | Action for the repair agent |
|---|---|---|---|---|---|
| **DEFECT-1** | `stage_2_claim_records.md` l.131 `B110`; also `U.79`, `part_1 l.443`, `part_2 l.97`, `part_2 l.627`, `part_3 l.55`, `Q29` | Lipsky "was CIO of the superstore division of Barnes & Noble **from 1993 to 1995**", cited to No. 5 / 1997-05-14 | both accessions: **"From March 1994 to July 1996"** (`NO5 l.2727-2731`, `ORIG l.2509-2512`); "superstore division" is the **original's** phrase only; "1993 to 1995" in **no document in the repository** | **HIGH — substantive + phantom date range** | delete the range; re-key to `S-1 (orig.) l.2509-2512` **and** `No. 5 l.2727-2731`; present as accession differential |
| **DEFECT-2** | `B100`; `part_1` §A.1 | 612,000 shares "**repurchaseable by the investor**", quoted *"subject to repurchase at $.001 per share through June 21, 1999"* | **`424B1 l.2969-2973` / `NO5 l.4176-4181`**: *Bezos granted **the Company** a right to repurchase … **if his employment terminates**… lapses ratably over the 36-month period ending June 21, 1999*; 510,000 still subject at 1996-12-31 | **HIGH — polarity reversed; supports an inference it shouldn't** | holder = Company; restore the termination condition; re-word §A.1; lift the passage from `S2E-47`, which already has it right |
| **DEFECT-3** | `part_1` l.12-13, l.22 | boundary = "05-14 registration effective **and priced at $18.00**" | effectiveness ✓ `10-K405 l.1126`; **pricing on 05-14 has no on-disk carrier**; the release carrying it is **not registered in `sources.csv`** | **HIGH — the boundary's own date label** | split the label; tag the pricing leg `UNVERIFIED (no local copy)`; register the release |
| **DEFECT-4** | 96 records class D + 18 class C (confirmed rate ≥ ~60/96) | `Passage:` strings in quotation marks that are re-wordings ("records revenue when the order is shipped", "we have received $2.0 million…", "Mr. Bezos will beneficially own…", "In June 1996, the Company effected a four-for-one stock split", etc.) | filed wording differs in every case checked, facts usually do not | **SYSTEMIC — evidentiary form** | re-derive from the line each record already cites; else tag `PARAPHRASE (not the filing's words)`. **Also correct the appendix front-matter sentence "every … Passage field is the specialist's or the filing's own string"** |
| **DEFECT-5** | `D32`; `part_1 l.242`, `l.409` | *"In November 1997, the Company opened a distribution center in New Castle, Delaware."* quoted | no such sentence; event at `10-K405 l.1646-1647` (says "Delaware" only); place-name at **`l.1075` only**, which **no Stage-2 citation points to** | **MEDIUM** | cite `l.1646-1647 + l.1075`; de-quote or split `D32` |
| **DEFECT-6** | `sources/` | two local copies of the S-1 original and of No. 5, **constant 17-line offset** (= the 1,384 B provenance header) | `ORIG l.667` = twin `l.650`; `NO5 l.796` = twin `l.779`; `ORIG l.2510` = twin `l.2493` | **MEDIUM — will generate ~900 phantom failures for the next auditor** | delete the twins or state the keying rule once in `stage_2_index.md` |
| **DEFECT-7** | `sources/`, `sources.csv` | Fortune, WIRED, LA Times, CSM, WSJ, B&N 10-K, both press releases cited with tiers and `Conf: High` | **zero periodicals on disk for company_001** (company_002 has `sources/periodicals/`); 38 records untestable; `U.80`'s "only genuinely independent Tier-1 pairing" rests on an absent document | **HIGH — structural** | **research debt, not repair**: intake + add `local_copy:` flag + print `(NO LOCAL COPY)` in-cell as `(PB)` is printed |
| **DEFECT-8** | `B112`, `Q18`, `B114`, `U.89` | 10.30's "PERMITTED USE" heading fused with 10.31's "Allowed Use" clause; **"& other products" dropped**; "each schedule delivered" for "each Lease" | `ORIG l.23387-23388`, `l.22988-22991`, `l.26077-26078` | **LOW-MEDIUM**, but the dropped tail touches the books-vs-category boundary argument | re-quote per exhibit; restore "& other products" |
| **DEFECT-9** | header self-pointer; `S2B-X-2/4/5/10`; `Tier:` vs `[T#]`; 10/11 register rows unkeyed | `part_1 l.18` → actually l.22; four ids unresolvable by join; two tier grammars | — | **LOW ×3** | re-point; normalise id grammar; key records by `source_id` |

---

## 15. Limits, and one claim I tested further than the volumes did

- **38 records** whose cited witness is not on disk (DEFECT-7) — untestable at zero web budget, by design.
- **The "unread accessions" limit does not reach the price.** The header calls the 424B1 *"the sole price
  carrier"*, which is asserted from four documents and not from Nos. 1/2/4/6. I machine-tested all of them.
  **`$18.00` occurs 0 times in each of: the S-1 original, and Amendments No. 1, 2, 3, 4, 5 and 6 — and 8 times in
  the 424B1.** Same for both duplicate local copies. The "sole price carrier" claim is therefore **established
  across the whole saved 1997 set, not merely consistent with the four read** (P-6a). It also sharpens DEFECT-3:
  No. 5 was filed on 14 May and **does not contain $18.00**, so nothing filed that day carries the price.
- **Origin of the two substantive defects, traced by string rather than assumed.** `"from 1993 to 1995"` and
  `"by the investor"` each occur in **exactly one file in the repository — `stage_2_claim_records.md`**. They are in
  no dossier, no `_parts/s2_p*.md` assembly part, and no narrative volume. Both were therefore introduced by the
  **claim-record appendix build itself**, which is the file whose front matter promises *"every … Passage field is
  the specialist's or the filing's own string"*. `S2D-61`, `S2B-54` and `S2E-47` all have the facts and the
  accessions right, and `_parts/s2_p1.md` §A.1 only **omits** the holder of the repurchase right rather than
  reversing it — so DEFECT-2's outright reversal is confined to `B100`, and the narrative needs a weaker fix than
  the record does. This is the most reassuring finding in the sheet and the least comfortable: the failure is not
  in research, or in retrieval, or in the specialists. It is in the transcription layer that exists to preserve
  them, and it is a quotation-mark failure, which is the kind no arithmetic check can see.
- **199 line references** whose document pairing I could not resolve mechanically; I hand-read enough to be
  confident none is orphaned, but the pairing was not machine-proved end to end.
- Amendment No. 6 (acc. …847, also filed 1997-05-14) is on disk and is still declared unread by the volumes. It
  contains no price, so nothing in this sheet turns on it, but the header's "Nos. 1/2/4/6 unread" line and the
  "four dated states" framing should be reconciled with the fact that **No. 6 is a fifth same-day state of the
  same instrument** — the register already notices this in S2004's title ("424B1 / S-1/A No. 6").


## 16. Gate result

**AUDIT 2 (Citation) — FAIL.** Not a formatting failure, not a coverage failure: **242 tier tokens, 961 line
references and 479 records, with zero out-of-range pointers and no phantom documents among the SEC set.** It is a
failure of the specific thing this audit is for — *the cited document, at the cited place, saying this* — and it
concentrates exactly where the previous audit found its two worst defects: in the assembled prose and registers,
downstream of correct specialist reading.

**Minimum to re-run clean:** DEFECT-1, -2, -3 (three sentences, all repairable from lines already named here);
the front-matter verbatimcy claim inside DEFECT-4; a `local_copy` decision on DEFECT-7 (repair or research debt —
but not silence); and DEFECT-6, because leaving it guarantees the next auditor's numbers are garbage.

Per method §11 Stage 2 remains **`RECONSTRUCTION`, not audited clean**, and per §14 rule 4 no finding above is
merged or quietly harmonised: where the volumes and the filings disagree, the disagreement is reported and the
volumes stand unedited, because I wrote none of it and change none of it.
