# Audit Sheet — Amazon.com (company_001_amazon) · Stage 1 · Run 2026-09-23
Auditor: Level-3 Hindsight Auditor (independent of producer: **yes** — no part of this volume, its dossiers, or the
merge was written by this auditor)
Audit: **AUDIT 4 — HINDSIGHT** (would this reconstruction still read as plausible if the company had failed five
years after the stage ended?)
Target: `01_companies/company_001_amazon/stage_1.md` (38,403 w; 1,921 ll.) + `context_appendices.md` (8,527 w; 537
ll.), boundary **1994 idea formation → 1995-12-31** as re-based by AUDIT 1.
Binding read first: `00_METHOD_AND_STYLE.md` §2 (hindsight firewall), §3 (claim classes), §5–§6 (tiers, time audit),
§7 (fixed line formats incl. the Knowability triple), §11 (a failed audit means researching again), §13/§14
(schemas, retrieval discipline); `AUDIT_PROTOCOLS.md` AUDIT 4 steps 1–5 + template; `CORRECTIONS.md` COR-09,
COR-04, COR-10, COR-11, COR-06, COR-03; `adversarial_review.md` (30 graded elements; §4 mechanisms/alternatives;
§5 survivorship hazards; §6 nulls); `amazon_s1_audit1_chronology.md`; `amazon_s1_audit2_citation_check.md`.
Negative controls independently re-run this pass against `sources/`: "2,300" = **0 hits** in the restored original
S-1; "Cadabra" = **1** occurrence in the original, **0** in S-1/A No. 5 (COR-02 holds); "8,000,014" present,
"8,000,140" **absent from every filing** (see D-11).

| Audit | Result | Items checked | Failures found | Actions taken | Residual risk |
|---|---|---|---|---|---|
| 1 Chronology | not run here — sibling sheet exists (**CONDITIONAL FAIL** on the 1993 start, re-based by RD-020/021) | — | — | — | — |
| 2 Sources | not run here — sibling sheet exists (**PASS WITH CORRECTIONS**) | — | — | — | — |
| 3 Numbers | not run here; **one numeric defect found in passing** at `context_appendices.md` ll. 54, 476 (`$8,000,140`) | 1 arithmetic check against the restored Item 5 text | 1 | logged to D-11 / RD-033, not corrected by this auditor (out of scope) | none — figure is post-boundary either way |
| **4 Hindsight** | **FAIL** (7 outcome-dependent sentences survive; 7 causal assertions lack the §16 mechanism-plus-alternative set; 1 named survivorship control never reaches the deliverable) | step 1: 100% of §A, §D.2, §L, §N, §R narrative cells + every "this showed/demonstrated/learned" construction; step 2: all causal verbs in both files (63 candidate sentences read, 14 adjudicated); step 3: knowability split §H ll. 433–439, §C.1 l. 198, §N ll. 639–646, §S, §B/§D/§E/§F/§G/§J/§K/§R cells; step 4: 24 trait/inevitability search terms across both files + the reverse-error test; step 5: §M entry count and content, §O entry count and content, survivorship framing; step 6: all 14 named post-boundary figures traced through both files; step 7: §A read standalone | 7 + 7 + 1, plus 4 editorial/wording defects and 3 `context_appendices.md` boundary-leakage items | 14 rewrites specified in `Claims cut or downgraded` with replacement text; 6 debts opened RD-029…RD-034 | low if the rewrites are applied — **no cut removes evidence**, every one restores a tag the file already carries elsewhere |
| 5 Adversarial | ran 2026-09-23, **PASS (partial protocol)** | — | — | this sheet re-tests it behaviourally — see §7 below | 1 unpropagated verdict (hazard (i)) |

**Headline.** This is, on the whole, the least hindsight-contaminated Stage-1 text in the project so far, and the
verdict has to be said in both directions. The firewall is not decorative: the file repeatedly chooses the
sentence that hurts (`§A` l. 118–123 lists what was still broken; `§M.2` ll. 590–594 proves from the audited ratios
that **no** order size made a Stage-1 order profitable; `§D.2` l. 272 ends the experiment section on the fact that
the first sale "cannot be substantiated from any document made while it was happening"). COR-09's do-not-launder
list is honoured at all fourteen items it bars. But the audit fails on the pass
condition as written — **zero outcome-dependent sentences** — because seven survive, concentrated in exactly two
places: the *assessment* voice (`§D.1` "What was learned", `§D.2`'s opening sentence) and the one bullet where the
file states what was knowable (`§H` l. 435). Six of the seven are sentences that quietly drop a tag the same file
puts on the same fact two rows away, which makes them fixable without new evidence and also makes them the most
dangerous kind: the reader meets the untagged version first. The causality failure is worse in
`context_appendices.md` than in the stage file — five of the seven unmechanised claims sit in those "So what"
paragraphs, which are the interpretive payload a reader actually carries, and which the method never required to
carry the §16 set.

---

## 1. Outcome-dependent sentences (procedure step 1)

Test applied per sentence: *would this read as plausible if the firm had died in 2000?* Where a sentence passes
only because a later fact supplies its force, it is a finding. Fourteen candidates were adjudicated; **seven
fail**. The seven surviving clean (i.e. not counted) are listed at §7 so the positive result is on the record.

| # | Line | Sentence as written | Why it fails | Disposition |
|---|---|---|---|---|
| OD-1 | `§H` l. 435 | "**KNOWABLE in-period:** … that directory placement, not advertising, **drove** discovery" | A bare causal verb inside the file's own knowability ruling. Nothing in the record shows placement drove anything: `§D.1` l. 247 grades the effect of each channel **UNKNOWN**; `§F.2` l. 349 says no independent dated listing survives; `§M.9` l. 620 lists "traffic came from search engines — not evidenced"; adversarial §4 l. 134 states the alternative outright ("placement explains discoverability, not purchase, and for 1995 is asserted rather than evidenced"). It also fails the 2000 test: for a dead company this sentence would be retitled "the channel that failed". | **DOWNGRADE** — see C-01 |
| OD-2 | `§D.1` l. 255 | "Strangers outside the local area transacted in small dollars **across 50 states and 45+ countries** with almost no paid media" | States as *what was learned* the company's own unverified self-report. `§L` l. 576 grades this "High as claim; **Low as fact**"; `§U.1` l. 1036 "High that it was claimed, Low that it was verified"; `§R` l. 897 re-adds the tag ("**as claimed by the company**"); `§P50` l. 781 "Low that verified". Six tagged sites, one untagged — and the untagged one is in the learning row. | **RESTORE TAG** — C-02 |
| OD-3 | `§D.1` l. 255 | "the directory-era route **worked**" | "Worked" is an efficacy verdict, and efficacy is the one thing Stage 1 cannot measure: conversion, orders and repeat are all UNKNOWN (`§L` l. 577; `§M.8` ll. 615–617; `§S` l. 932). The route demonstrably *placed* the store; that it *converted* is unknowable inside the boundary. Force depends on the later curve. | **DOWNGRADE** — C-03 |
| OD-4 | `§D.2` ll. 260–262 | "The test showed a narrow, real thing: … **take payment from strangers in all fifty states and 45-plus countries**" | Same laundering as OD-2, in the paragraph that is the section's takeaway. `§D.2`'s own later sentence (ll. 266–267) concedes "visits, countries and repeat share all originate with the seller" — the correction exists two sentences downstream and does not repair the topic sentence. | **RESTORE TAG** — C-04 |
| OD-5 | `§N` l. 654, *Expected result* | "A name that **survived the telephone**" | No source in the corpus or in `stage_1_claim_records.md` attaches this expectation to anyone in 1994. Only the outcome (a company that kept a phone channel and became enormous) makes it legible as an aim, and the row's own rationale cell for the adjacent motive — the A-initial directory story — is COR-09-barred and `§U.4` l. 1118 fixes its first retrievability at 1999. The cell reads as the dataset supplying a 1994 motive the record refuses to give. | **STRIKE / replace** — C-05 |
| OD-6 | `§N` l. 656, *Expected result* | "An order system live **before rivals**" | Presupposes a race and implies it was won; `§U.11` l. 1308 and `§I` ll. 462–466 establish Amazon **was not first**, and l. 82/l. 919 show `relentless.com`/`amazon.com` were registered ~8 months before any sale — timing evidence the row already carries. The competitive framing adds nothing the cited "first mover advantages" disclosure does not already supply, and would only be selected as an aim by someone who knew the field was winnable. | **REWORD** — C-06 |
| OD-7 | `context_appendices.md` `§H` ll. 445–452 | "… makes early favorable coverage a scarce asset worth modeling and **borrowed credibility (Yahoo's and Netscape's editors, then the WSJ front page and a *Time* year-end list) a real part of the demand story**" | Asserts a demand causation the stage file keeps open (`§D.1` l. 247; `§F.2` l. 349), and does it by importing **1996-05-16** (WSJ) and **1996/1997** (*Time* "Best Websites of 1996", known only as restated in the 1997 filing) into a Stage-1 conclusion — the WSJ front page post-dates the boundary and the only 1995 channel datum is the company's own claim of 1995-10-04, unverified (adversarial §4 l. 133, N-7). | **REWRITE** — C-07 |

**Count: 7 outcome-dependent sentences surviving (6 in `stage_1.md`, 1 in `context_appendices.md`).** Pass
condition is zero. **Condition 1 = FAIL.**

## 2. Causality audit (procedure step 2)

Required per §16: evidence → mechanism → alternative explanation → confidence. Twelve assertions were traced;
**seven lack the set**. Eleven others were checked and pass, including three the brief named as priority sites.

**Named tests from the brief.**
- **Did directory placement *cause* traffic, or coincide?** The file gets this right five times and wrong once.
  Right: `§D.1` l. 247 "High (existence); **UNKNOWN (effect of each)** → U.41"; `§R` l. 907 repeats it; `§F.2`
  l. 349 caps borrowed credibility at Medium with "no independent dated listing survives"; `§I` l. 456 records the
  *filed risk* that gatekeepers "could promote the Company's competitors"; `§M.9` l. 620 lists the search-engine
  attribution as an unverifiable experiment. Wrong: OD-1 (`§H` l. 435). The error is not that the file believes
  it — it is that the file's knowability section asserts as in-period knowledge a proposition its evidence
  sections grade UNKNOWN.
- **Did the 1995-10-04 coverage drive demand or follow it?** `stage_1.md` handles this correctly and does not
  need repair: the release *reports* the preceding four weeks, so the direction of fit is stated by construction
  (`§Q` l. 871 "FACT as made"; `§L` l. 576 "a company self-report, not verified demand"; `§U.1` l. 1030 notes the
  tension is "between two statements by the same author, not between a claim and a measurement"). The failure is
  in the appendix (OD-7), where the reverse question — that the release's own circulation generated later
  traffic — is never raised.
- **Did long-tail selection produce purchases when there is no 1995 repeat evidence (a 1996 figure)?** Clean, and
  demonstrably so: `§M.8` ll. 8/615–617 "Stage-1 demand demonstrates *first purchase only*: retention, cohorts and
  acquisition cost are absent → U.12"; `§I` l. 464 "The 'infinite shelf' was a **listing** asset: the fillable tail
  was ~400,000 titles, about 3× the best superstore, not 20×"; `§P.2` d20 ll. 816–817 flags the 1995-claim ÷
  1997-disclosure ratio as "illustrative of the mechanism, **not a 1995 measurement**"; `§U.3` l. 1095 carries
  Kaphan's "we did have a million titles. We didn't have a million books". **No finding.**

**Causal claims lacking mechanism and/or alternative (7).**

| # | Line | Claim | Missing element | Disposition |
|---|---|---|---|---|
| CA-1 | `§H` l. 435 | placement "drove discovery" | mechanism, alternative, and contradicts the file's own channel ruling | C-01 |
| CA-2 | `§E.2` l. 298 | "Seafirst merchant account, personally guaranteed by Bezos — **a two-person firm could not get acceptance unsecured**" | The counterfactual is the mechanism, and `§U.24` ll. 1589–1594 adjudicates it **UNKNOWN**: "the filing evidences that a guarantee was **used**, never that a company-only account was **sought and refused**." `§K.5` l. 549 has it right ("The only observed mechanism… whether a company-only account was sought is UNKNOWN"). | C-08 |
| CA-3 | `§M.5` l. 604 | "**Card acceptance was obtainable only on a personal guarantee**" | Same barred counterfactual, in the negatives section, where an unargued assertion reads hardest. `§U.24` l. 1596 additionally leaves open whether this was credit rationing, founder convenience, "**or ordinary small-merchant practice in 1994**". | C-09 |
| CA-4 | `context_appendices.md` `§A` ll. 21–23 | "a two-person Seattle internet firm was financed by named individuals **because the institutional plumbing did not yet exist**" | Mechanism is elsewhere in the same file and better (S-election confined shareholders to eligible individuals, ll. 52–53), the causal verb is unsupported, and the alternative the appendix's own `§G` ll. 389–391 supplies — "the same silence bars the opposite counter-claim that 'no investor would touch it' — neither proposition is evidence" — is not carried at the claim site. | C-10 |
| CA-5 | `context_appendices.md` `§B` l. 124 | "The transaction was fragile: … **which is why the operator's own filing calls that step the barrier** to the whole category" | Evidentiary inversion. The filing is the *evidence* for the fragility, not its downstream reporter; stated this way the company's risk factor becomes independent confirmation of a condition the company asserted. Mechanism is present; the direction of proof is not. | C-11 |
| CA-6 | `context_appendices.md` `§C` l. 167 | "That made the Stage-1 pitch **legible and cheap to explain**, because an American consumer already knew how to buy something untouchable by post" | Unmeasured efficacy claim; `§C`'s own preceding bullet concedes "no in-window measure of catalogs mailed, catalog dollar sales or the return norm", and acquisition cost is a `§S`/`§M.9` null. Alternative (the pitch was legible because it was a discount catalogue in plain retail language, or because the press cycle needed a novelty) not offered. | C-12 |
| CA-7 | `context_appendices.md` `§D` l. 211 (heading) | "**The distributors who made it possible**" | Enabling causation asserted; the non-exclusivity alternative that `stage_1.md` `§G.1` l. 366 and `§M.7` l. 613 carry — Ingram is disclosed "help[ing] others establish and operate online sites for booksellers", so the same file armed every entrant and explains the category, not Amazon's share of it — is absent from this bullet. | C-13 |

**Count: 7 causal claims lacking the §16 set (2 in `stage_1.md` across 3 sites, 5 in `context_appendices.md`).**
**Condition 2 = FAIL.**

## 3. Knowability split (procedure step 3) — **PASS**

The triple is present and, unusually, load-bearing rather than decorative. `§H` ll. 433–439 runs KNOWABLE / NOT
KNOWABLE / UNKNOWN as a labelled block; the UNKNOWN list is populated with things a hagiographic file would leave
out (1993-95 host and user counts, access cost and speed, the returns rate, the Bowker in-print count). Per-element
splitting is consistent: `§C.1` l. 198 "Facts knowable in 1994" is a discrete row; `§A` l. 133 is an "Unknown:"
row and l. 125 an "Evidence that existed:" row; `§D.1` splits "What was learned" from "What was NOT learned" (ll.
255–256); `§R` l. 912 has a Start→End **Unknowns** cell; `§S` is 1,318 words of gaps with importance and
follow-up. `§P52–P54` print UNKNOWN as a value with High confidence *of the null*, which is the correct move.

`§N`'s rationale fields were checked individually against the test "does this describe what a person in 1994 could
observe?" and pass. The section opens with the COR-06 limit stated as an evidentiary ceiling (ll. 639–646: Sheff is
"Tier 1 as an artifact of 1999/2000, **Tier 4 as evidence for 1994**"; the 1995-10-04 quotation is "company-issued
publicity about the firm's own performance, not independent reporting of his reasoning"), and the cells obey it:
l. 651 books row lists what was observable ("two distributors … millions in print vs ~170,000 a superstore
stocks; catalogue un-mailable"); l. 652 refuses the inference and says so ("The 1997/1999/2013 retellings trace to
one speaker = **one source, not three**"); l. 653's *Unknowns* cell poses the causal question rather than answering
it ("**Whether incorporation drove or followed the site choice**"); l. 655 concedes that Tier 1 corroborates only
the *condition* (no sales tax collected outside Washington), not the motive; l. 656 keeps "*Whether* Bezos wrote
any of the site software" UNKNOWN. The only cells that fail the test are the two *Expected result* cells already
counted as OD-5 and OD-6. Because there is no contemporaneous founder-state document, the correct standard is
"reasoning tagged as recovered later" — and ll. 650, 651, 655 do exactly that with explicit `RETRO` in the Actual
result column.

## 4. Inevitability and trait language (procedure step 4) — **PASS**

Twenty-four search terms run across both files. "Visionary", "prescient", "clearly", "always intended",
"obviously", "doomed", "inevitable", "bold", "shrewd", "genius", "brilliant", "vindicated", "landmark",
"watershed", "destined", "testament", "paid off", "proved right", "with hindsight", "turned out" return **zero
dataset-voice hits** in `stage_1.md`. The only three near-hits are innocuous and each is cited: l. 285/l. 1519
"Proved, not assumed" refers to the 38-document byte arithmetic, not to a virtue; ll. 1597/1693 "proves" is bounded
to "*that* he said it in 1999/2000"; l. 200's "a lot, lot smaller than it turned out to be" is inside a quotation
attributed to Kaphan 2011 and tagged [T3 · RETRO]. In the appendices, "near-inevitable" (`§A` l. 52) predicts the
*shape of the financing* from two named period constraints (Subchapter S; the absent institutional plumbing), not
the fate of the firm — accepted, not a finding.

No adjective does work evidence should do: every evaluative noun is attached to a number at first mention
("thin" carries 2,200 visits; "almost no paid media" carries advertising of $30,000 against $200,000 of marketing,
l. 351; "minimal inventory" is refused as a marketing claim and replaced by ≈$17,000 at `§U.10` l. 1281). The
file's deflationary vocabulary is consistently applied *against* the subject, which is the opposite of
hagiography.

The reverse error was tested for specifically, and the file actively forbids it in three places: `§U.30` l. 1696
regret minimisation "explains a **choice**, not an outcome, and must not be recast as foresight or as evidence that
success was discounted"; `§U.33` l. 1748 the consent narrative "must not be used to argue the money was 'smart' —
**nor, conversely, to frame the investors as fools**"; and the firewall at l. 56 naming "financiers were fools" as
the thing being excluded. `context_appendices.md` `§G` ll. 389–391 does the same job for the banks. **No investor-
fool framing survives anywhere. Condition 4 = PASS.**

## 5. Survivorship control (procedure step 5) — **PASS on the two testable halves; one control never propagated**

- **No "successful companies did X" is smuggled in as "X tends to succeed."** Searched for the construction and its
  cousins ("tends to", "most firms", "companies that", "lessons", "generalizable"): no dataset-voice instance in
  either file. The closest approach — `§C.1` l. 198's "facts knowable in 1994: two wholesalers; millions in print
  vs ~130,000–175,000 stocked" — is disarmed in the same volume by `§G.1` l. 366 and `§M.7` l. 613, which record
  that the same distributor access was sold to rivals, so the shared condition can explain the category's
  existence without explaining the survivor's share of it. That is the correct handling of the long-tail
  argument.
- **§M is present and substantive, not decorative: 11 numbered entries, 699 words** (ll. 584–633). Each carries
  evidence, and several carry arithmetic rather than sentiment: entry 2 (ll. 590–594) derives a $(0.19) per-dollar
  contribution and states that "no average order value makes a Stage-1 order profitable (margin would have needed
  ≥ ~79%)"; entry 8 (ll. 615–617) removes the retention signal entirely; entry 9 (ll. 618–623) lists seven
  rejected, failed or unverifiable experiments including the search-engine attribution and the Slate test thrown
  out on Stephen Glass's fabrication record; entry 10 (ll. 624–629) spends 100 words on the file's own most
  quotable artifacts being untraceable. **§O carries 6 counterfactuals plus a boundary note** (ll. 663–715), each
  with *Visible / For / Against / Considered / Others*, and O.2 (ll. 674–678) refuses to manufacture a rejected
  alternative where none is evidenced ("Recorded as **UNKNOWN, not as a rejected alternative**, and must not be
  written as one") — that is the anti-decorative move.
- **Emotional centre: the fragility, not the success.** §M (699 w) exceeds §A (591 w); §A's final paragraph
  (ll. 137–144) is the negative case and opens "Failure remained entirely plausible."; §D.2's last sentence is the
  unsubstability of the first sale; `§R`'s Weaknesses row is captioned "(evidenced, not hindsight)" (l. 911). A
  reader finishing this file remembers a firm that no arithmetic could make profitable, not one that was going to
  win.
- **Finding (propagation failure, not a framing failure).** Adversarial §5 hazard (i) — "**Evidence
  survivorship:** the load-bearing documents exist because the company registered an offering in 1997; failed
  contemporaries left no S-1, so a filing-centred Stage 1 over-represents the survivor's side of the record,
  including risk factors drafted for liability rather than history" — **appears nowhere in `stage_1.md` or
  `context_appendices.md`** (searched: "survivor", "failed contemporar", "no filing of its own", "selection
  effect", "liability rather"). Two adjacent fragments exist (`§C.2` l. 226 "written under securities-law liability
  by an issuer describing its own origins"; `§U.19` l. 1490–1492 the S-1 "was filed two years after Stage 1 and
  after a successful IPO, so even it is a post-outcome document"), but they control *document* bias and never
  reach the *population* bias — which is the one that matters for a dataset whose entire purpose is comparison
  across companies. This is the single instance where the file does **not** behave as if an adversarial verdict had
  been made, and it is the most consequential one. Mandatory insertion C-14 / RD-032.

## 6. Endpoint discipline (procedure step 6) — `stage_1.md` **PASS**, `context_appendices.md` **3 leaks**

All fourteen named post-boundary items were traced through every occurrence, not just their first mention.

| 1996–97 figure | Sites in `stage_1.md` | Rhetorical status |
|---|---|---|
| $15.7M FY1996 net sales | header l. 62; `§P59` in the explicit "context only, NOT Stage-1 metrics" block (l. 789) | fenced |
| 151 / 158 employees | l. 62; `§P61` (post-boundary block, "neither enters a Stage-1 cell"); `§U.17` ll. 1446–1447 | fenced |
| 11 employees | 11 sites, every one carrying "(per the filing: at 1996-01-01)" per COR-03 — ll. 80, 104, 174, 243, 490, 518, 773, 880, 894 | **fenced; exemplary** |
| ~180,000 accounts | `§L` l. 580 (*POST-STAGE-1* row, "Nothing about 1995"); `§R` l. 897; `§P60` | fenced |
| >40% repeat | `§L` l. 580; `§F.2` l. 350 ("**All post-boundary**… not comparable"); `§M.8` l. 616; `§U.12` l. 1336 | fenced |
| Ingram 59% | `§A` l. 119; `§G.1` l. 363; `§G.4` l. 397; `§P55`; `§R` l. 899; `§U.40` — each with "1995 share UNKNOWN" | fenced |
| Series A $8,000,014 | `§K(j)` ll. 564–567 ("**1996, post-boundary**, and appear here only to warn against collapsing them"); `§P62` | fenced |
| March-1997 discounting | `§E.3` ll. 317–319; `§U.18` ll. 1456–1458; `context_appendices.md` `§D` ll. 208–210 "Sequence correction" | fenced |
| 2.5M titles | 8 sites, each barred at the point of use ("**1997 marketing numbers** and may not be back-projected", l. 286; `§U.3` ll. 1091–1093; `§P57`) | fenced |
| $1,007,000 program | `§B.2` l. 176 ("**most of it is post-boundary**"); `§K` l. 514; `§P51`; `§P.2` d22; `§R` l. 904; `§U.8` ll. 1231–1233 | fenced, incl. the 1996 leg |

**No sentence in `stage_1.md` frames a 1995 decision as wise because of what a 1996 number did.** The reverse
pressure is systematic instead: `§N`'s pricing row (l. 658) answers its own 1995 decision with the two
unfavourable facts available ("marketing exceeded gross profit and a rival undercut the typical discount"), and
`§L`'s post-stage row is headed "*POST-STAGE-1*" before it is headed "Signal". **Condition 6 = PASS for the
target file.**

Three leaks in `context_appendices.md`, of the kind correct tagging does not catch:
- **CL-1 l. 475.** The quantitative-context row is **labelled "Stage-1 capital raised"** and its value cell lists
  "§4(2) 3,021,000 sh to 23 purchasers = **$1,007,000**" and "incl. **20 unaffiliated investors**". The date cell
  is honest ("1995-12-06→1996-05-16"), but the *row title* performs the laundering COR-10 action 3 was written to
  prevent: a reader taking numbers from the table gets a Stage-1 raise inflated by a program that ran to
  1996-05-16 and whose in-window portion the filings never disaggregate.
- **CL-2 l. 49.** The same program is described in the financing narrative as part of "**the money that
  arrived**" with no counterpart to `stage_1.md`'s repeated "**most of it is post-boundary**".
- **CL-3 l. 1.** Header still reads "STAGE 1 (**1993** → 1995-12-31)" and every section preamble says "As knowable
  in **1993**–1995", after AUDIT 1 established that no document dates any Amazon-relevant act to 1993 and
  re-based the start. `stage_1.md` `§H` l. 405 licenses its own 1993–95 range with an explicit note ("a market-data
  knowability window, wider than the stage boundary"); `context_appendices.md` carries the range in its **title**,
  with no such note, which is precisely how a barred dating returns as a boundary.

## 7. §A read alone — anti-hagiography sanity check (procedure step 5 / §2 test) — **PASS**

Read in isolation, ll. 98–144: a company with five and a half months of trading; audited loss $(304,000); a third
of sales from abroad; card acceptance existing "on his personal guarantee, not the company's standing" (ll.
115–116); four things "Still broken" including the concession that "some titles may not be available at all" (l.
118) and "no order size was profitable" (ll. 122–123); nine named UNKNOWNs (ll. 133–135); and the paragraph
opening "**Failure remained entirely plausible.**" (l. 137), which supports itself with the 24.1% PC-ownership
ceiling, the registrant's own named payment-trust barrier, a rival's "we haven't sold many books", a printed 1995
skeptic's case, and a 1997 paper's "next light bulb or another Edsel" — with the dating of that last item policed
in the same breath ("a 1997 judgment on 1996, recorded as evidence about the climate, not about Stage 1", ll.
143–144). A reader of §A alone cannot form the impression this was going to work. **Condition 7 = PASS**, and
l. 137 is the line that proves it.

## Where the file is genuinely clean (positive findings, so the next auditor does not re-litigate them)

1. **The firewall statement is operational, not declaratory.** l. 62 names every post-boundary figure it binds
   itself to, and each is held at all downstream sites.
2. **`§L` passes the 2000 test row by row.** Every in-window signal's "Did NOT demonstrate" cell is stronger than
   its "Demonstrated" cell (ll. 575–579): July 1995 shows "a live paying outside channel", not a settled
   transaction; 2,200 visits show "the only 1995 traffic figure ever filed", not conversion; 11 employees show
   "an organisation existed", not capacity.
3. **`§D.2` ll. 268–271** measures the launch against what a contemporary could see — "buyers were a minority of
   households, payment trust a named industry barrier, a rival direct-book operation reported selling almost
   nothing, a general-purpose Web mall had already been shut down, and the largest physical chains had announced
   online programs" — every clause period-evidenced, none outcome-referencing. That is the §15 test met in prose.
4. **`§U.19` l. 1490–1492** treats the company's own best document as a post-outcome artifact and tags it `RETRO`
   where it explains earlier events. Rare and correct.
5. **`§U.24` ll. 1589–1599** refuses the tempting "banks wouldn't lend" story by name, applies COR-01's
   downgrade-not-quietly-keep rule to it, and records what the guarantee does and does not evidence. The
   counter-claim at `context_appendices.md` `§E` l. 249 ("Best-dated refutation of 'no one could take cards online
   then'… the barrier was **credit and account approval**, not technology") is the same discipline done well — and
   is what makes CA-2/CA-3 regressions so visible.
6. **`§M.2` (ll. 590–594)** is the anti-hagiography centre of gravity: derived contribution margin of $(0.19) per
   revenue dollar, closing "Evidenced arithmetic, not hindsight."
7. **All 30 adversarial verdicts behave as if made**, bar hazard (i). Spot-checked by construction: E-02 → the
   re-base and `§Q` l. 842's **UNKNOWN** row; E-04/E-21/E-12/E-14/E-06 → `§C.2` rung table, `§U.4`, `§F.1`,
   `§U.11`, `§H` ll. 424–431; E-17/E-18 → `§K` and `§U.8`; E-26 → `§B.1` l. 154's President-and-Chairman cell;
   E-30 → `§A` "Still broken" and `§G.4`; E-16's "investors laughed" → `§O.6`/`§U.33`, never as mockery.

---

## Claims cut or downgraded

No cut removes evidence. Where a value cell is rewritten, the replacement carries strictly more of the file's own
tagging than the original did.

| Ref | Claim (line) | Was | **Now — replacement wording** | Why | Evidence applied |
|---|---|---|---|---|---|
| **C-01** | `§H` KNOWABLE list, l. 435 | "that directory placement, not advertising, drove discovery" | "that discovery in 1995 ran through editorial directories rather than paid media — 3,084 curated listings at launch, free nomination, no retrievable paid 1995 placement (`§H`; `§M.9`) — **and that whether placement converted into purchases is NOT KNOWABLE for 1995**: the only 1995 channel datum is the company's own 1995-10-04 listing claim, no independent dated listing survives, and the effect of each channel is UNKNOWN (`§D.1`; `§F.2`; → U.41)". Move the causal half of the bullet to **NOT KNOWABLE**. | outcome-dependent **and** causal claim with no mechanism or alternative; contradicts four in-file rulings | `stage_1.md` ll. 247, 349, 620, 907; `adversarial_review.md` ll. 131–135, 207 (N-7) |
| **C-02** | `§D.1` "What was learned", l. 255 | "Strangers outside the local area transacted in small dollars across 50 states and 45+ countries with almost no paid media" | "**The company reported** shipments to customers in all 50 states and 45+ countries in its first four weeks; the audited year independently shows $198,000 (38.75%) of $511,000 arriving from outside the U.S., so foreign strangers did pay — the geographic spread itself is unverified (`§L`; → U.1)". | company self-report used as a finding; the audited international line is the independent substitute | ll. 576, 781, 1036; `§P33` |
| **C-03** | `§D.1` l. 255 | "the directory-era route worked" | "the directory-era route **placed the store in the period's principal discovery channels; that it converted there is not knowable inside the boundary** (`§D.1` channel row: effect of each UNKNOWN)". | "worked" is an efficacy verdict on unmeasurable conversion | ll. 247, 577, 615–617, 907; `§S` l. 932 |
| **C-04** | `§D.2` ll. 260–262 | "…and take payment from strangers in all fifty states and 45-plus countries, on a buy-per-order chain" | "…and take payment from strangers — **with the company itself reporting** all fifty states and 45-plus countries, and the audited statements independently establishing 38.75% of sales from outside the United States — on a buy-per-order chain". | same laundering, in the section's topic sentence | ll. 576, 897, 1036–1038 |
| **C-05** | `§N` l. 654 *Expected result* | "A name that survived the telephone" | "**None evidenced** — no 1994 source states an expected result for the rename; the directory-alphabetisation and 'signalling size' motives are retrospective/folklore claims first retrievable 1999 (COR-09; → U.4)". Apply the same fix to the *Rationale* cell: "**motive UNKNOWN in-window**; what is documented is only the registration sequence". | unsourced 1994 expectation whose content presupposes the outcome; collides with the file's own COR-09 ruling | `sources.csv`/ll. 478, 1116–1120; COR-09 |
| **C-06** | `§N` l. 656 *Expected result* | "An order system live before rivals" | "An order system live **before a first sale was possible** — the filing's own later words for the competitive aim are 'first mover advantages and momentum', asserted without priority claim (→ U.11)". | presupposes a race the record says Amazon did not win | ll. 462–466, 913, 1308–1310; `adversarial_review.md` E-14, G-12 |
| **C-07** | `context_appendices.md` `§H` ll. 445–452 | "…and borrowed credibility (Yahoo's and Netscape's editors, then the WSJ front page and a *Time* year-end list) a real part of the demand story" | "…which makes a directory nomination the scarcest acquisition asset a 1995 entrant could hold. **Whether borrowed credibility moved demand is UNKNOWN inside Stage 1**: the only 1995 listing datum is the company's own claim of 1995-10-04 with no independent dated record, the WSJ front page is **1996-05-16** and the *Time* list is a 1996 year-end item known only as restated in the 1997 filing — both post-boundary, and both consequences rather than Stage-1 demand evidence." | causal assertion the stage file keeps open; two post-boundary items used in a Stage-1 conclusion | `stage_1.md` ll. 247, 349; `adversarial_review.md` ll. 131–152, 191–206 (N-7) |
| **C-08** | `§E.2` l. 298 | "— a two-person firm could not get acceptance unsecured" | "— the rails are evidenced only **as opened on his signature**; whether a company-only account was available or sought is **UNKNOWN** (`§K.5`; → U.24)" | asserts a counterfactual `§U.24` adjudicates UNKNOWN | ll. 549, 1589–1594 |
| **C-09** | `§M.5` l. 604 | "**Card acceptance was obtainable only on a personal guarantee**" | "**Card acceptance is evidenced only in personally guaranteed form** (Seafirst Nov 1994, Wells Fargo Jul 1995, company cards Apr 1995; amounts UNKNOWN). Whether it was obtainable otherwise — or whether a personal guarantee was simply routine small-merchant practice in 1994 — is **UNKNOWN** (→ U.24)." | same; and this site is in the negatives section where an unargued claim reads hardest | ll. 549, 1591–1597 |
| **C-10** | `context_appendices.md` `§A` ll. 21–23, 58–66 | "was financed by named individuals **because the institutional plumbing did not yet exist**" | "was financed by named individuals, a family trust and a §4(2) placement to 23 purchasers. Two constraints on that shape are documented — **Subchapter S confined shareholders to eligible individuals and one class until 1995-03-31**, and no in-window institutional seed market is retrievable — and whether the plumbing's absence *caused* the individual-money shape is **not established**; `§G` bars the counter-claim too ('no investor would touch it' is not evidence either way)." | causal verb with the mechanism elsewhere and the alternative unspoken at the claim site | ll. 52–53, 43–44; `§G` ll. 389–391; `stage_1.md` `§U.24` |
| **C-11** | `context_appendices.md` `§B` l. 124 | "The transaction was fragile: … **which is why the operator's own filing calls that step the barrier** to the whole category" | "The transaction was fragile on the evidence available: card details by e-mail and telephone, a toll-free line kept open *specifically* for buyers unwilling to type a number, nine published mailboxes (`§E`). **The registrant's own risk language names secure transmission as the category barrier** — company-issued, and here counted as the filing's assessment of its market, not as independent confirmation of a condition we know only from it." | evidentiary direction inverted: the source of the evidence is presented as its downstream reporter | `stage_1.md` l. 348; `adversarial_review.md` N-1 |
| **C-12** | `context_appendices.md` `§C` l. 167 | "That made the Stage-1 pitch **legible and cheap to explain**, because an American consumer already knew how to buy something untouchable by post" | "The launch language adopted the catalogue form ('a catalogue of more than 1 million titles'), which is **consistent with** an audience already accustomed to buying sight-unseen by post — B&N self-described as the world's largest direct-mail book supplier. **Whether it lowered explanation or acquisition cost is not evidenced**: no in-window catalogue measure was retrieved and 1995 acquisition cost is UNKNOWN (`stage_1.md` `§D.1`, `§M.9`). Alternatives the record does not exclude: the pitch was legible because it was a discount catalogue in ordinary retail language, or because the 1995 press cycle needed a novelty regardless of the analogy used." | unmeasured efficacy claim, alternative absent, and its own bullet concedes the missing denominator | ll. 156–162; `stage_1.md` ll. 247, 351, 618–623 |
| **C-13** | `context_appendices.md` `§D` l. 211 heading | "**The distributors who made it possible**" | "**The distributors the offer ran on — non-exclusively**", with the closing clause added: "the same access was on sale to everyone: Ingram is separately disclosed **helping other booksellers 'establish and operate online sites'** (`stage_1.md` `§G.1`, `§M.7`; → U.40), so distributor access explains the category's emergence, not this entrant's share of it." | enabling causation without the non-exclusivity alternative the stage file already carries | `stage_1.md` ll. 366, 612–614; `adversarial_review.md` ll. 146–147 |
| **C-14** | `stage_1.md` — new cell, `§A` after l. 131 or a `§S` row | *(absent)* | "**Survivorship of the record.** Every load-bearing Stage-1 document is a 1997 registration filing, and it exists because this company went public: failed 1995 contemporaries filed no S-1, so a filing-centred Stage 1 over-represents the survivor's side of the record — including risk factors drafted for liability rather than history, which are candid here because the securities laws made candour cheap. Nothing in this volume may be read as the average 1995 internet retailer's documentary condition, because the average one left no audited statements to read." | adversarial §5 hazard (i) was adjudicated and never propagated to the deliverable | `adversarial_review.md` ll. 166–169 |
| **C-15** | `context_appendices.md` `§I` l. 475 | Row titled "**Stage-1 capital raised**" listing the $1,007,000 program and "20 unaffiliated investors" | Retitle "**Capital raised inside Stage 1, and the program that straddles it**": keep $10,000 founder / $44,000 notes / **$1,272,000 CY1995 equity cash (of which $295,568 named)** as the Stage-1 line, and move "§4(2) … = $1,007,000" to a separate **boundary-straddling** row reading "**subscriptions 1995-12-06 → 1996-05-16; the filings do not disaggregate by date; in-window amount UNKNOWN**", exactly as `stage_1.md` `§K` l. 514 has it. | correct date tagging, wrong row title — the rhetorical leak AUDIT 1's tagging pass cannot catch | COR-10 action 3 |
| **C-16** | `context_appendices.md` l. 1 (and the eight "As knowable in 1993–1995" preambles) | "AMAZON.COM — STAGE 1 (**1993** → 1995-12-31)" | Retitle "STAGE 1 (1994 idea formation → 1995-12-31)", and where a 1992–93 baseline is genuinely used (CERN 1992, Mosaic 1993, Matrix News Feb-1994), add the one sentence `stage_1.md` `§H` l. 405–407 already supplies: a market-data knowability window wider than the boundary, not a claim that the stage opens in 1993. | AUDIT 1 re-based the start on a documented null; the companion file still carries the barred dating in its **title** | AUDIT 1 verdict + RD-020/021; `stage_1.md` ll. 47–53, 842 |
| **C-17** | `context_appendices.md` ll. 54, 476 | "$8,000,140 at $14.05/share" | "**$8,000,014**" — the Item 5 aggregate in the restored text; 569,396 × $14.05 = $8,000,013.80. | transposition, re-verified against all four filings this pass; "8,000,140" occurs in **zero** on-disk documents | `sources/` S-1 (orig.), A3, A5; COR-10 |
| **C-18** *(editorial)* | `§L` l. 580 *Did NOT demonstrate* cell | "Nothing about 1995." under the header "What It Did **NOT** Demonstrate" | "**No implication about 1995.**" | header-plus-cell reads as a double negative in the one column whose job is to close off inference | — |
| **C-19** *(editorial)* | `§N` l. 657 *Actual result* | "Releases still unperformed post-IPO in 1997 [H-09]" | add "`(RETROSPECTIVE)`" | method §13 requires post-stage outcomes in `actual_result` to carry the label; every other row in `§N` does | method §13 |

## Research debt opened by this audit

> **Id-collision warning for the Company Lead.** AUDIT 1 took **RD-020–RD-023**, AUDIT 2 took **RD-024–RD-028**.
> This sheet's debts are numbered from **RD-029**; nothing below belongs in an earlier slot. **None of these
> re-dates anything**, so per AUDIT 4's closing rule no AUDIT 1 re-run is triggered by the rewrites above — with
> one exception noted at RD-033 (the `context_appendices.md` title, which is AUDIT 1's own finding re-asserted).

| RD id | Section | Debt | Assigned | Status |
|---|---|---|---|---|
| **RD-029** | `§H`, `§D.1`, `§F.2`, `§R` Distribution cell | **Directory-placement efficacy is unresolved, and C-01 must not be "restored" without it.** Chase any dated *independent* record of the Netscape "What's New" / Yahoo "What's Cool" listings (the directories' own 1995 archives, a dated third-party citation, or period correspondence) — N-7 records none surviving. Second line of attack: any 1995 order-source data at all, since "effect of each channel" is UNKNOWN by absence of measurement, not absence of measurement instrument. | Distribution + Archives | **OPEN — High**; C-01's downgrade stands until closed |
| **RD-030** | `§E.2`, `§K.5`, `§M.5`, `§U.24` | **Was a company-only merchant account obtainable by a two-person Washington firm in November 1994?** This is the file's single most load-bearing unasked counterfactual: it decides whether the personal guarantee was credit rationing, founder convenience or routine practice, and three sections currently assert the first. Period acquirer criteria for card-not-present micro-merchants, plus the service-bureau path the August-1995 Mosaic archive names ("Net Trust", Convergence Inc.; "Sun Microsystems Internet Commerce Group") — the latter is the documented *alternative* the file lists at l. 657 but never prices. | Finance / payments | **OPEN — High**; blocks any "capital constrained" framing of Stage 1 |
| **RD-031** | `context_appendices.md` `§H`; `stage_1.md` `§F.2` | **Press-and-coverage efficacy, separated by year.** Establish what (if anything) is observable about *1995* coverage effects: the two dated 1995 outside items (Tallahassee Democrat 1995-10-22, Knight Ridder Nov 1995) are Tier-4-quoting-T1 with print originals unheld (RD-011), and the WSJ/Time items are 1996–97. RD-027's re-save of the two 1995 releases plus the print originals is the precondition for C-07 being closable rather than merely downgraded. | Distribution (with RD-011, RD-027) | **OPEN — High**; carried, not newly discovered |
| **RD-032** | `stage_1.md` `§A`/`§S`; `context_appendices.md` preamble | **Propagate the survivorship control.** Adversarial §5 hazard (i) exists only in the review; insert C-14 into the deliverable, and specify in `00_METHOD_AND_STYLE.md` §2 that the record-selection null is a required element of every stage's firewall statement, not an auditor's private note. This is the one place where a made verdict did not reach the text. | Method owner + Company Lead | **OPEN — High**; blocks AUDIT 4 re-pass independently of every other item |
| **RD-033** | `context_appendices.md` ll. 1, 49, 54, 476 | **Companion-file boundary and figure drift.** Regenerate the appendices against the re-based boundary (C-16), fix the "Stage-1 capital raised" row label (C-15), and correct $8,000,140 → **$8,000,014** at both sites (C-17). The label fix is the substantive one: an appendix row title is the most-copied text in the whole dataset. Note the title item is AUDIT 1's finding re-asserted, so it may be closed under RD-020/021 rather than counted twice. | Evidence Registrar + Consolidation lead | **OPEN — High** (label, title); **trivial** (typo) |
| **RD-034** | `00_METHOD_AND_STYLE.md` §7 line formats | **The "So what" paragraph has no §16 obligation, and five of this run's seven causal failures live inside it.** The template mandates evidence–mechanism–confidence sets for tables but not for the interpretive codas, which are the sentences readers actually quote. Add a fourth element to the "So what" format — *mechanism plus the alternative the record cannot exclude* — or require those paragraphs to reuse the table's tags verbatim. | Method owner | **OPEN — Medium**; affects every subsequent company, not this one |

## Sign-off

Stage status: **RECONSTRUCTION → ADVERSARIAL REVIEW → QA → COMPLETE** — currently at **QA, and AUDIT 4 is not
passable as delivered.**

**AUDIT 4 result: FAIL.** Per pass condition, item by item:

| Pass condition | Result | Basis |
|---|---|---|
| Zero outcome-dependent sentences surviving in the text | **FAIL — 7 survive** | OD-1…OD-7; §1 table |
| Every causal claim with mechanism plus alternative | **FAIL — 7 lack the set** | CA-1…CA-7; §2 table. Named tests: directory placement **fails** at `§H` l. 435; the 1995-10-04 coverage **passes** in `stage_1.md` and fails in the appendix; long-tail selection **passes** (`§M.8`, `§U.3`, `§P.2` d20) |
| Knowability split present, with `§N` rationales describing 1994-observable states | **PASS** | `§H` ll. 433–439; `§C.1` l. 198; `§N` ll. 639–646 and per-cell `RETRO`; only the two *Expected result* cells fail |
| §M non-empty and substantive | **PASS — 11 entries / 699 words**, several with arithmetic rather than sentiment; §O carries 6 counterfactuals plus a boundary note, and O.2 refuses to invent a rejected alternative | `§M` ll. 584–633; `§O` ll. 663–715 |

Plus the two items this brief added: **endpoint discipline PASSES** in `stage_1.md` on all fourteen 1996–97 figures
at every occurrence, with three rhetorical leaks surviving in `context_appendices.md` (C-15/C-16 and one typo);
and **§A read standalone PASSES** the anti-hagiography check, on l. 137.

**Why the verdict is not softened.** Six of the seven outcome-dependent sentences are regressions against the
file's *own* rulings — the tag exists two rows away and is dropped where the prose is most quotable — and the
seventh (OD-1) is worse still, sitting inside the knowability block where it acquires the status of period
knowledge. A hindsight audit that passed this text because its tagging is otherwise excellent would be grading
geometry instead of argument. `context_appendices.md`'s failure is the more instructive one: five of seven
unmechanised causal claims are in its "So what" codas, which the method never required to hold §16 discipline and
which are, for any reader who opens one file rather than three, the actual conclusion of this stage.

**Why it is not harder.** I looked for objections and did not find enough to make more. The trait-language sweep
returns nothing; the reverse error is explicitly fenced three times over; the do-not-launder list is honoured at
every one of the fourteen items it bars (2,300% ll. 424–431; 16 July ll. 337, 626; $12,000/$14,000 ll. 334, 627;
"shipped our first book in August" ll. 628, 1060; the Wainwright/Hofstadter order ll. 331, 863; $1.1M-22-$50,000
ll. 176, 551; the ~$5M/20% valuation ll. 556, 783; $150,000/$250,000 ll. 159, 557–560; the Bulgarian order l. 622;
the A-for-directory motive ll. 478, 1118; the *Post* stake l. 621; a 1995 security guarantee ll. 315, 1465;
"Cadamia" ll. 169, 1110; the roadmap/91 pages ll. 214, 624), and the four negative controls that the whole
mythology test rests on were re-run against the bytes this pass and held ("2,300" = 0, "Cadabra" = 1/0 across
versions, "8,000,140" = 0 where "8,000,014" is in all three filings). The fix is 19 edits and 6 debts, none of
which removes evidence, and after C-01 through C-14 this file would pass. The work is not to re-research Amazon; it is to make the volume say about
the directory channel and the personal guarantee what it already says in its own evidence tables, and to ship the
one adversarial finding — that the record survives because the company did — that never left the review room.
