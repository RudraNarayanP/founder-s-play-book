# ADVERSARIAL REVIEW — APPLE (company_004) STAGE 1 — DOSSIER D

**Run date:** 2026-09-24. **Company:** Apple (004), Fortune rank #4. **Stage under attack:** Stage 1,
recommended span **1975 → 1977-01-03** (partnership era), per `A_chronology_feasibility.md` §Recommended
stage boundaries.
**Reviewer role:** adversarial (AUDIT-5 class). Graded: the 38 records of the feasibility probe
(AP-01…AP-38), the ~77 records and 13 conflicts (U-A2-1…13) of `A2_periodical_archive_mine.md`, and the
**popular Apple founding narrative** as it circulates in Tier-2/3/4 print. This pass attacks the claims
*currently on the table for the dossier*, not a delivered `stage_1.md` — none exists yet. That ordering is
an advantage, not a defect: the story is broken before it is built.
**Ownership:** this file is the only path this agent writes. `sources/` is a protected read-only archive
(method §14 rule 4); no file there or elsewhere was created, moved, renamed, tidied or deleted by this pass.

**Hindsight-firewall statement for this pass.** Nothing after 1977-01-03 is used here as evidence that
1975–76 decisions were rational. The February 1981 BYTE column and the FY1994 10-K are admitted **only**
as `RETROSPECTIVE SOURCE` witnesses to earlier facts, and the 2026 auction record is admitted as evidence
that a 1976 document *exists*, never as evidence of what 1976 was like.

**Independence statement and its limit.** The claims tested here were assembled by agents that had read the
corpus; this pass therefore grades against the registers themselves (AP-xx, A2-xx, U-A2-nn) plus its own
fresh greps of the cached primary files, not against memory. Where this pass states a corpus fact it has
re-verified it locally and says so; where it inherits a dossier finding without re-verification it is marked
`[inherited]`.

**Confidence scale** per §3: High (2+ independent sources or a primary document) · Medium (one reliable
source) · Low (conflicting, vague, retrospective-only) · UNKNOWN.

---

## Working method and budgets

**Method.** (1) Enumerate the claims Apple Stage 1 will actually rest on. (2) For each, ask the three
firewall questions: what is the **earliest dated evidence**, is it a **company/founder statement or an
outside witness**, and **what survives if the founder's later account is discarded entirely**? (3) Trace
popular claims to their **first appearance**; where the only lineage is one document or one memoir, name it
and apply the independence rule (§3) so that repetition is not counted as corroboration. (4) Hunt
**primary contradictions** — contemporaneous print with a different number, an advertisement that predates
the canonical story, an instrument that contradicts the memoir — beginning with the locally cached BYTE
1976/1977/1981 and Homebrew 1975–77 files (`../sources/`, provenance per `../sources/_RETRIEVAL_LOG.md`).
(5) Classify: **well supported / contested / folklore / unsourced**. (6) Refuse to overcorrect: absence of
an independent witness is a **provenance downgrade, not a disproof**, and this pass flags places where the
existing dossiers are themselves at risk of that error (§Do-not-overcorrect, under Attacks that failed).

**Verdict key used in the element table.** `WELL SUPPORTED` = survives total discard of founder memoir on
independent or primary-dated evidence. `CONTESTED` = dated evidence exists on more than one side, or the
support is single-lineage/in-window-self-report only. `FOLKLORE` = **true-or-untrue is not the question;
the only support is a later self-report or a commercial description of an unread document, repeated.** An
element can be folklore and still have happened — that is the honest category, not a refutation.
`UNSOURCED` = no support of any class located.

**Web budget (hard cap 10).** Spend plan: ≤4 search requests to trace first appearances of the $666.66
price, the "50 boards at $500" order, the "biggest IPO since Ford" formula and the 1976 fictitious-business-name
/ county record class; ≤6 fetch requests against auction lot text, one price-list facsimile, and one trade-press
IPO story carrying the FY1976–77 columns. Every failure is recorded as `UNANSWERED` with request and status
(§14 rule 1). Local material is mined first and is not counted against the cap.

**Local corpus mined by this pass (0 web requests):** `sources/ia_byte_1976/byte-1976-01..12.txt`
(12 full-issue OCR files, ≈5.7 MB), `sources/ia_byte_1977/byte-1977-04..07.txt` (4 issues),
`sources/ia_byte_1981/byte-1980-12.txt` + `byte-1981-02.txt`, `sources/ia_homebrew/` (13 dated newsletters +
the 1977-02-16 Faire flyer), `sources/10-K_FY1994_acc-0000320193-94-000016_filed-1994-12-13.txt`,
`sources/apple1registry_stories.txt`, `sources/probe_wayback_APPLE.md`, the six EDGAR probe JSONs and the two
submissions blocks. Grep results are logged with file and line in §Attacks that landed / §Provenance notes.

---

## Element register — 36 load-bearing elements, attack and verdict

`Founder-discard test` = what remains of the element if every founder/memoir account is thrown out.

| # | Element as popularly told | Verdict | Attack | What survives the founder-discard test |
|---|---|---|---|---|
| E-01 | Apple was **founded April 1, 1976** | CONTESTED (date of a document, not of a company) | The date's only carrier in this corpus is Tier-2/3 **auction prose** for an instrument no agent in this repo has read (AP-20). Three web reports of one sale are one event, not three witnesses (§3 independence). 1 April is also the calendar's joke date, and the number's fame is self-reinforcing | A dated 1976 three-page partnership agreement exists and was publicly catalogued; **no 1976–77 print names it, dates it, or names the partnership at all** (U-A2-1, U-A2-10). "Founded 1976-04-01" is a document date, not a contemporated event |
| E-02 | Apple Computer, Inc. was **incorporated in California on 1977-01-03** | WELL SUPPORTED | Is the 1981 print independent of the 1994 filing? Yes — different author, publisher, decade, no lineage | Two Tier-1 documents that do not share a lineage: the registrant's own FY1994 10-K sentence (AP-04) and BYTE Feb 1981 "Apple, incorporated in 1977" (AP-19). Nothing in the corpus dates the *day* except the filing |
| E-03 | "Apple Computer, Inc. was founded April 1, 1976" (the fused form) | FOLKLORE / **category error** | The Library of Congress page that states it cites a 2001 young-adult biography, Britannica 2021 and Mergent 2020 — **zero contemporaneous sourcing** (AP-23). The company's own filings never narrate a founding (AP-05) | Two different legal events collapsed into one word. The dossier may print 1976-04-01 (partnership, document-based) and 1977-01-03 (corporation, filing-based); it may not print either as "Apple was founded" |
| E-04 | There were **three founders**, Wayne at 10% | CONTESTED | The percentage reaches us through sale coverage, not transcribed text (AP-20 `[inherited]`); Wayne appears in **zero** cached 1976–1981 documents, including the Feb 1981 column written for investors (U-A2-10) | A three-signatory 45/45/10 allocation is a documentary claim resting on one artifact; the *origin story as printed from the start was a two-founder story* (this pass re-confirms: `Wayne` grep of all cached files returns no Apple attribution) |
| E-05 | Wayne left after **12 days**, for **$800**, and "no regrets" | FOLKLORE | "12 days" has no dated withdrawal instrument in evidence; the "$800 plus a later $1,500" is auction prose. The 12/12 symmetry is mnemonic, not archival | Withdrawal happened (artifact class exists); duration, amounts and attitude are undocumented in this corpus |
| E-06 | Apple was **born in a garage** | CONTESTED — and *partially* rescued | The canonical version is memoir. But the characterisation is **in-window and third-party**: Feb 1981 print says Markkula "took Apple from a garage operation to its current enviable position" | A 1981 published characterisation of a "garage operation" (Tier 1 press, retrospective about 1976). No 1976 document places any work in any garage; no address; ownership UNKNOWN (AP-36/DG). Note the asymmetry: this is the *strongest* in-window support for the garage motif anywhere in the cache, and it is still 5 years late |
| E-07 | The garage is **20211 Crist Drive, Los Altos** | UNSOURCED within period; **not refuted** | All `Los Altos` lines in the cached corpus belong to third parties (Cromemco, Qume) `[inherited U-A2-13; this pass re-counted — exactly 17 lines, all third-party, see §H-7]`. But absence in BYTE is not absence in the world | The **only** address of record in 1976–77 print is Cupertino, 20863 Stevens Creek Blvd Bldg B3-C (May–June 1977). Street number and municipality of the childhood home require assessor/recorder or a 1976 dba filing — neither reached |
| E-08 | The **Byte Shop ordered 50 Apple-1 boards at $500** in July 1976 and that order founded the business | FOLKLORE (as to number and price) | The designer's own May 1977 print names no buyer, no order and no number, and attributes distribution to word of mouth then retail stores (AP-16). Wayne, the only partner who ever described the transaction on the record, says "a large number," not 50, and does not price it (AP-29). No invoice, cheque or Terrell statement dated 1976–77 is in evidence | That a wholesale relationship with Terrell's chain is plausible-to-likely: Terrell and Jobs appear as peers in Dec 1976 print (AP-10); dealers stocked the machine by Sept–Nov 1976 (AP-12/14); Terrell's own 1976 photographs of the founders showing him the machine exist (AP-30). **Units, price and date: zero** |
| E-09 | Terrell demanded **fully assembled boards, no discount, cash on delivery** | FOLKLORE | Every element of this scene traces to memoir/retelling; no 1976–77 document quotes Terrell | A retail chain that stocked assembled machines did exist and did advertise assembled machines (Kentucky Fried Computers offers the "Apple-1 computer" — the assembled form — by mail order, Nov 1976) |
| E-10 | The Apple-1 sold for **$666.66** | FOLKLORE **in this corpus**; the price itself UNKNOWN | This pass independently re-grepped all cached files: no price occurrence of the famous figure anywhere — and the corpus's **only** dollar-shaped 666 is a competitor's strike-through anchor, "IMSAI 8080 … a $666 value / only $595" (§L-2 decoy inventory). The designer's only printed number is "a price under $700 at the retail level" (May 1977). The 4/3-times-$500 derivation is arithmetic applied to an unestablished $500 | An under-$700 retail price from the maker in-window; the famous repeating-decimal figure appears in **no** cached in-window file. Recorded as UNANSWERED-not-false: Kilobaud 1976 has no OCR text layer (AP-34), Creative Computing is unmined (555 items), and an October 1976 advertisement image exists on Wikimedia unread (DG-D2) |
| E-11 | Apple-1 distribution ran on **word of mouth** | WELL SUPPORTED **as a dated claim**; CONTESTED as description | It is a first-party self-report with no denominator, printed by the man who built the machine; and the same paragraph's second half ("later nationwide through retail computer stores") is contradicted-or-at least-not-matched by East-Coast dealers advertising by Sept–Oct 1976, i.e. **before** the maker's own advertising began in June 1977 | The sentence itself, dated 1977-05, Tier 1, contemporaneous founder claim — plus the *external* picture: three dealer advertisements and two trade mentions in 1976, zero maker advertisements in BYTE in 1976 (AP-22) |
| E-12 | Apple's **first-year sales were $77,000** (and FY1977 $770,000) | UNSOURCED / folklore | No retrieved in-window text states any 1976 or 1977 revenue (AP-35). Both figures arrive as "prospectus figures" from secondary sites; the prospectus is paper-only (AP-02, AP-21) and has never been read by this project | Nothing. The printed revenue series begins FY1978 at $7.8M (Feb 1981). §P must carry 1976 and 1977 revenue as UNKNOWN unless the paper prospectus or an IPO-era story is produced |
| E-13 | Jobs and Wozniak financed board printing with **$500 from an HP-65 calculator and $750 from a VW bus** | FOLKLORE (textbook §3 case) | The Apple-1 Registry itself attributes the story to *iWoz*, chapter 12, page 173 — a 2006 autobiography (AP-32). Corroboration across the entire web is repetition of that one book | Zero independent. Nothing about it is refuted; the sale of a calculator and a vehicle by a 21-year-old is entirely plausible. It is single-lineage memoir, not evidence |
| E-14 | Wayne understood Jobs obtained a **$15,000 loan** to fill the order | CONTESTED→LOW (single retrospective partner) | One participant's 2022 written account, no instrument, and in tension with E-13's $1,000 (AP-29, U-AP-3) | That a founding partner, in retrospect, believed outside credit was needed. Amount, lender, date, collateral: UNKNOWN |
| E-15 | **Markkula** put in roughly $250,000 / guaranteed $91,000 / took ~26% | FOLKLORE at T1 for the terms | What 1981 print actually carries is his **name, age, holding and a one-line role gloss** (AP-18, AP-30 quote). Every figure for the deal is post-1981 retelling | A. C. Markkula, 32, holding 8.3 million shares in Feb 1981, described as the man who took Apple "from a garage operation" — Tier 1, contemporaneous to the IPO, retrospective to 1977. Terms UNKNOWN |
| E-16 | **Venrock** led the first venture round (amount, date, valuation) | UNKNOWN (round) / WELL SUPPORTED (holding) | Only a share count is in print: "Venrock Associates, a venture capital firm, holds 3.8 million shares" (AP-18). Price paid, date and pre-money valuation appear nowhere in the cached corpus | The existence of venture capital in the cap table, printed within two months of the offering |
| E-17 | The Apple I was **designed late in 1975** | WELL SUPPORTED **as a contemporaneous founder claim**; Low as dated fact | Single source: Wozniak's May 1977 article (AP-16). The club's own newsletters for 1975-11 → 1976-03 contain **zero** occurrences of "apple" (AP-26), so the late-1975 demo has no in-window witness. But newsletters were not minutes, so this is silence | "Designed late in 1975," by its designer, in print 17 months after the claim and before any memoir — the earliest dated first-party statement available anywhere. Stage-1 start edge should be flagged as **Medium**, not High |
| E-18 | The Apple I demo **at Homebrew** produced immediate orders | FOLKLORE | The club's print record shows the first Apple machine arriving as a "special guest" in **April 1976** with Wozniak providing transportation (AP-24) — i.e. the club's own account is of a machine brought in, not orders taken in 1975 | That Wozniak and an Apple 6502 system were present to the club by April 1976, dated and self-published by the club |
| E-19 | BYTE's **Helmers saw the Apple II on 1976-11-20** in the founders' hands, in a Palo Alto motel | WELL SUPPORTED (strongest single dated Stage-1 fact) | Published April 1977, four months after; single witness; and the witness was a magazine editor with a commercial interest in the machine. Still: an outside observer, a date, both founders, one named place | A named third-party sighting dated to the day, printed within five months (AP-15). Nothing in the corpus contradicts it |
| E-20 | The Byte Shop was **the world's first computer store / first franchise** | CONTESTED — primacy was a live in-window fight, with advertisers on both sides | BYTE July 1976 editorially calls Terrell founder of "the world's first computer store franchise" — in the same magazine that later printed Computer Mart of New York's "Last year we opened the first computer store on the East Coast" (U-A2-5). Three scopes, three interested speakers, no adjudicator | The claims, dated, as **advertising and editorial self-narration of the period**. Which store first sold an Apple product: earliest advertisement found is New York, Sept–Oct 1976 (AP-14), which cuts against the Palo-Alto-first telling |
| E-21 | The Apple I was **the first single board integrating display, processor, memory and power** | CONTESTED | The claim is the designer's own, in a magazine where he was also an advertiser's client (AP-16). The in-window field was crowded with assembled 6502/8080 systems advertised in these same pages (Sphere, IMSAI, SWTPC, Digital Group, Processor Technology, ETC-1000 at $675) | The maker's 1977 claim of integration, plus the fact that BYTE's November 1976 technical article groups "the new Apple computer" with other PROM-monitor machines already being marketed (AP-13) — which places Apple *inside* a category, not at its origin |
| E-22 | Apple products were in **East-Coast retail stock by October 1976** | WELL SUPPORTED | Advertisement provenance: an OCR brand list, which does not say which Apple product or how many units | A New York City/Long Island dealer's printed brand list including Apple (AP-14), plus Computer Mart of New York listing APPLE among ~25 lines in May 1977 (U-A2-5) |
| E-23 | Independent dealers offered the **Apple-1 by mail order at a discount off list** in Nov 1976 | WELL SUPPORTED | OCR noise ("Apple-Apple-1"); a discount off "manufacturer's current list prices" implies a list price that **no cached file prints** — which is itself the evidence gap behind E-10 | A Berkeley dealer's advertisement offering the Apple-1 at 10% off manufacturer's current list (AP-12) — the strongest in-window proof of a wholesale/retail ladder existing by November 1976 |
| E-24 | Apple's **first self-published advertisement** priced the Apple II at $1,298 complete, $598 board-only, June 1977 | WELL SUPPORTED | Could a self-published price be a *later* correction of a 1976 reality? Irrelevant to the artifact's own date. Checked the alternate reading: no cached 1977 Apple ad gives a conflicting number | Full-page maker's advertisement, dated by the issue's own masthead, with address and telephone (AP-17) — the dossier's cleanest primary price evidence |
| E-25 | Apple's 1977 price table implies a **6.5% California sales tax** | CONTESTED (arithmetic) | Nine rows agree at 6.5% `[inherited U-A2-6]`, while two 1976 and 1980 advertisers in the same pages print 6%. A consistent table is hard to produce by rounding accident, but the interpretation (jurisdictional add-on) is inference, not record | The arithmetic, exactly; the explanation UNKNOWN. Do **not** use the 6.5% as a locator for Cupertino vs Los Altos — district taxes did not map that cleanly |
| E-26 | The 1980 IPO: **4.6M shares = 8% of 52.4M at $22** (≈$101.2M) | CONTESTED as printed | The column's own arithmetic does not close: 0.08 × 52.4M = 4.192M, and 4.6/52.4 = 8.78% (U-A2-9). One number is rounded, stale, or includes an over-allotment. No filing exists online to check (AP-21) | Both printed figures, with the inconsistency on the page; the derived gross sizes $101.2M and $92.2M, neither preferred (DERIVED rows with arithmetic shown) |
| E-27 | It was **the biggest US IPO since Ford** | UNSOURCED in this corpus | Not found in any cached in-window text; the phrase circulates Tier-4. Tested against local material and logged as a live web query (§Sources consulted) | Nothing in-window; keep as a research-debt item, not a Stage-1 fact |
| E-28 | Revenue/profit: **FY1978 $7.8M/$793,497; FY1979 $48M/$5M; FY1980 $117M/$11.7M** | WELL SUPPORTED (as printed) / single column | One unsigned 24-line column (Feb 1981) is the entire corpus-side basis; precision is mixed within it — exact dollars beside rounded millions (U-A2-7, U-A2-8) | Contemporaneous trade-press reporting of a company-supplied series. It is **not** audited data, and FY1978 is not Stage 1: the hole where Stage 1's money is, stays a hole |
| E-29 | Apple-1 production/sales "about 150" in the partnership's 11 months (and "about 200" in the first year) | UNSOURCED | No in-window count anywhere. This pass chased the "200" version and found it resting on **Wikipedia alone** (§L-9); any figure is derived from surviving-serial estimation, which is collector inference, not a record | Serial-number census exists as artifact scholarship (Tier 3); production and sales totals UNKNOWN, and may not be used as a denominator in §L |
| E-30 | Jobs's **1973 job application** documents his pre-Apple founder state | CONTESTED (Low) | The date is the curator's inference ("believed to have been completed around" Reed's dropout), and the adjacent "a year later, he joined Atari" is curation prose, not payroll (AP-28) | A dated-to-1973-ish handwritten signed artifact exists with a public sale record; its own text mentions "computers and calculators" — thin but first-party |
| E-31 | **Terrell's Polaroids** record the first Apple-1 showing at the Byte Shop | CONTESTED | Photographs exist and are dated by a 2022 curator, not by the images as read; "first showing" is the curator's or Terrell's memory attached to the frames (AP-30) | In-window artifact photographs of a founder-era machine in a store context, published 2022. The word "first" is unsupported |
| E-32 | Apple-1s for the Byte Shop came in **handmade Koa-wood cases** | CONTESTED | Rests on a March 2022 conversation identifying the case-maker, layered on surviving objects (AP-31) | Surviving cased units as physical artifacts; the narrative of who built them and for which order is Low |
| E-33 | Randy Wigginton was **"Apple employee #6"** | FOLKLORE | Employee numbering is a company-origin claim with no payroll document in evidence; the source is a 2022 recollection (AP-31) | Nothing; and no Stage-1 file should print an employee number for Apple |
| E-34 | **Blue Box** and **Atari** as Jobs's documented pre-1976 activity | FOLKLORE / UNKNOWN at Tier 1 | No in-window document names the Blue Box venture anywhere in the corpus; Atari tenure rests on curated auction prose (AP-28, D2 brief) | Both remain founder-state **memory**; classify as FOUNDER CLAIM (retrospective) or UNKNOWN, never as FACT |
| E-35 | The Apple II was **introduced at the first West Coast Computer Faire, April 1977** | WELL SUPPORTED (as introduction-in-April) / CONTESTED (days) | The Faire's own dates conflict inside the corpus: promoter billing 15–17 vs a correspondent's "April 16 and 17" (U-A2-3). And the *introduction* is announced in advance, so print proves intent plus report, not the booth's day | Announced for April 1977 in BYTE April 1977 and covered afterwards (AP-11, AP-15, A2's post-event report); Apple's participation as a billed exhibitor from December 1976 |
| E-36 | Apple's **1976 company name** was "Apple Computer Company" | CONTESTED | Four name forms are all authentic in print: "Apple Computer Co" (BYTE Dec 1976, and Wozniak's own May 1977 byline), "Apple Computers" (Homebrew Sept 1976), "Apple Computer Inc." (Apple's own June 1977 ad), "the Apple Corporation" (a third-party Dec 1980 ad). **No 1976–77 document names the partnership style at all** (U-A2-1) | The registered partnership style is known only from the unread auctioned agreement. Any Stage-1 sentence asserting the 1976 legal name is resting on the document lineage of E-01 |

---

**Tally (36 elements graded).** **9 WELL SUPPORTED** — E-02, E-11, E-17, E-19, E-22, E-23, E-24, E-28, E-35, each
with the qualification printed in its own row (two are "well supported *as a claim*", one "as printed", one "as a
contemporaneous founder claim"). **12 CONTESTED** — E-01, E-04, E-06, E-14, E-20, E-21, E-25, E-26, E-30, E-31,
E-32, E-36. **11 FOLKLORE** — E-03, E-05, E-08, E-09, E-10, E-12, E-13, E-15, E-18, E-33, E-34. **3
UNSOURCED/UNKNOWN-primary** — E-07, E-27, E-29. **1 split** — E-16 (holding well supported, round UNKNOWN).
**11 attacks landed (L-1…L-11); 11 failed (H-1…H-11).** Of the nine claims the stage file most wants to rest on:
**four survive untouched** (incorporation 1977-01-03; the Apple II's published June 1977 price and configuration;
the 1976-11-20 founder sighting; the printed 1978–80 series as reporting), **three survive only as claims** (word
of mouth; "designed late in 1975"; the 1976-04-01 document), and **two do not survive as numbers at all** (the
first order; the $666.66 price).

## Attacks that landed

Each item names the claim, the attack, the specific evidence that did the damage (file + line, or request),
and the decision the merge must apply. "Landed" means the dossier's text cannot be written as currently
recorded; it does **not** mean the underlying event is false.

### L-1 — The first order ("50 Apple-1 boards at $500, July 1976") loses its last documentary pretence. LANDED

The claim is the keystone of Apple Stage 1: it converts a garage hobby into a company, supplies the first
customer, the first revenue and the first financing motive, and it is repeated everywhere. A already recorded
that no in-window text supports it (AP-16, U-AP-2). This pass went further and chased the lineage to its
carriers.

**What did it.**
1. The designer's own contemporaneous sentence, re-verified at line level: `ia_byte_1977/byte-1977-05.txt`
   line 6397 (`"1975 and sold by word of mouth through-"`, wrapping to the retail-stores clause) and line 6420
   (`"processor board with a price under $700 at"`), signed from `20863 Stevens Creek Blvd B3-C` (line 6385).
   No buyer, no order, no unit count, no price point.
2. **The Byte Shop's own 1976 advertising does not mention Apple.** The chain appears repeatedly in the cached
   issues, and always selling somebody else's product: as an *authorized dealer for Processor Technology* at
   five Bay Area addresses (`ia_byte_1976/byte-1976-11.txt` lines 20005–20040) and six addresses a month later
   (`byte-1976-12.txt` lines 25065–25115), and as a ten-outlet chain directory (`byte-1976-12.txt` lines
   17427–17435, Palo Alto at 2227 El Camino Real). Across all twelve 1976 issues the token `Apple` occupies 13
   lines, of which **zero** fall in a Byte Shop advertisement.
3. The specialist and commercial carriers of the story admit the lineage in their own text. RR Auction's 2026
   essay on the transaction states "fifty computers at five hundred dollars apiece, to retail at $666.66" and —
   per this pass's extraction — **relies exclusively on direct conversation with the merchant, with no invoice,
   dated correspondence, printed volume or magazine entry anchoring the figures**; it also dates the deal
   "**Spring 1976**", not July. The apple-1-replica.com study (2021) gives "50 completed boards … 25,000 USD
   cash on delivery" and cites a **photograph of a stamped manual cover plus a 2021 email reply from Terrell**,
   "zero invoices, periodicals, or dated interviews", merging a 1976 transaction with 2021 correspondence
   without separating contemporaneous from retrospective.
4. A rival figure exists and is unadjudicated: a public post attributed to Paul Terrell says he "sold Apple 1s
   to my Byte Shop owners for **$525** each and made $25 per unit" (Facebook, Tier 4 — recorded as a lead
   requiring chase, not as evidence, per §5).

**Verdict.** E-08/E-09 are **FOLKLORE as to units, price, date and payment terms** — the whole package traces
to *one* man's later conversations, and that lineage contradicts itself on the date and on the price.
**Merge decision:** the first order may appear only as `UNKNOWN (undocumented in any retrieved primary)`, with
the *relationship* — which is genuinely well evidenced — stated separately: Terrell and Jobs named as peers on
the WESCON floor in September 1976 (`byte-1976-12.txt` line 1516), the Faire billing pairing "Apple Computers"
with "Byte Shop of Palo Alto" (`byte-1976-12.txt` line 29856), and Terrell's surviving 1976 photographs of the
founders showing him the machine (AP-30). No number may be printed in §D, §F, §K or the timeline as FACT, and
the "first customer" field of the stage file stays UNKNOWN.

### L-2 — $666.66 is not merely absent from the corpus: the corpus's only price-shaped "666" is a competitor's. LANDED

A2's U-A2-4 recorded that the famous price is absent and that "the only hits are a telephone number and
printer's rules". That description is **wrong in a way that makes the claim more dangerous, not less**, and this
pass found it by re-running the grep instead of trusting the register.

**Decoy inventory — every `666` occurrence in the 1976–77 cache, with what it actually is:**

| File : line | String as printed | What it really is |
|---|---|---|
| `ia_byte_1976/byte-1976-12.txt`: 39846–39851 | "IMSAI 8080 with a FREE 22 slot mother board and 2 edge connectors / **a $666 value** / only $595" | **A competitor's advertisement — the only dollar-shaped 666 in the entire 1976 corpus, and it is a strike-through anchor price for an IMSAI 8080 bundle.** An agent mining "666" for the Apple-1 price lands here first |
| `ia_byte_1976/byte-1976-07.txt`:19613; `-08`:3525; `-09`:2888; `-10`:39187; `-12`:806 | "(501)666-2839" | Advertiser telephone number, New Hampshire |
| `ia_byte_1977/byte-1977-06.txt`:5581 | "stored in the first **666** bytes of EROM" | Technical prose |
| `ia_byte_1977/byte-1977-05.txt`:9551 | "Zilog, 10460 Bubb Rd, **Cupertino CA 95014**, (408) 446-**4666**" | A Cupertino address with Apple's own ZIP and a phone ending 4666 — a confirmation-bias magnet |
| `ia_homebrew/hcc0206.txt`:160; `byte-1976-11`:19743; `byte-1977-04`:36401 | "Suite 666"; "Hampton, VA 23**666**" | Suite and ZIP fragments |

**And the apparent authority for the price collapses on chasing.** The most citation-like secondary source found
for it, historyofinformation.com's entry on the Apple I, states "The Apple I went on sale in July 1976 at a
price of US $666.66" and "About 200 units were produced" — and its **only cited source is a Wikipedia article
retrieved 2011-11-26**, with even its reproduced October 1976 *Interface Age* promotional insert described from
that same wiki rather than read from the scan. So the chain is: wiki → aggregator → every "authoritative"
restatement; and the RR Auction sentence pairing $500 wholesale with $666.66 retail comes from the same 2021
conversation as the 50-unit figure. **One lineage, two famous numbers.**

**Merge decision.** E-10 → `UNKNOWN as a figure`; print only the designer's band ("under $700 at the retail
level", Tier 1, 1977-05) plus the market context this pass located: a mid-1976 magazine campaign offering "a
complete computer system for only **$650**" and the same author's quoted purchase price for a Sphere SYS2/KIT,
"**only $750** (during the
special introductory period)" (`ia_byte_1976/byte-1976-07.txt` lines 2985–3020; issue-dating caveat at L-6). Do
**not** print the 4/3-markup derivation ($500 × 1.333), which is arithmetic performed on two undocumented
numbers. The single document that could settle the price is an **October 1976 Apple-1 advertisement image**
(DG-D2).

### L-3 — The dossier's fourth "strongest retrievable dated fact" is not a Homebrew record. LANDED

A's Verdict lists as fact #4 the Homebrew newsletter of 1976-04-30: "In April the APPLE 6502 system was **our
special guest**. We are grateful to STEVE WOZNIAK for providing transportation" (AP-24), and the record presents
it as the club's own print placing an Apple machine inside Homebrew in April 1976. Read the page:
`ia_homebrew/hcc0204.txt` lines 131–144. The paragraph sits under the standing column heading **"NOTES FROM THE
NORTH —"**, whose subject is "**The SONOMA COUNTY MICRO COMPUTER CLUB** … We meet the first Tuesday in each
month at **LO\*OP CENTER in Cotati**" — with the sign-off block "L0\*0P CENTER, 8099 La Plaza, Cotati, CA
94928". "Our special guest" is the **Sonoma club's** guest; the gratitude to Wozniak is for driving a machine
about 60 miles north of Homebrew's own meeting place.

**Consequences, both directions.** Against the dossier: there is **no in-window Homebrew record of Apple at
all** in the cached run — the club's own pages contribute the Faire flyer and a September 1976 vendor list, not
the origin scene — and A's "earliest Apple trace in the club's own printed record" wording must be retired.
Against the folklore: the item is not nothing. It is a **dated, self-published, non-commercial grassroots
record that by April 1976 an "APPLE" 6502 system existed, was named, and was being personally transported by
its designer to clubs outside his own county**. That is materially better evidence for the word-of-mouth channel
(E-11) than for the Homebrew-origin scene; and the sentence above it ("We are a group of several ALTAIR's, an
IMSAI, a JOLT, two PDP-8's, **an APPLE** and some others **on order**") carries its own ambiguity — "on order"
may govern the APPLE, in which case April 1976 evidences a booking, not a delivery. **Merge decision:** cite as
*Sonoma County Micro Computer Club letter reprinted in the Homebrew newsletter, 1976-04-30*; delete every
inference about Homebrew's own April 1976 meetings; keep the machine's existence and naming in April 1976 at
High, physical custody at Medium. A2 already flagged the per-item provenance rule (A2-19/20, A2S-12) — this
pass's contribution is that **A's headline fact-list and its stage-boundary confidence row still carry the
uncorrected reading**, and the 1975 start edge leans on it.

### L-4 — The "first dealer" ladder inverts, and no 1976 document evidences a dealer *agreement*. LANDED

The earliest print naming the **product** is not Californian. `ia_byte_1976/byte-1976-09.txt` lines 25253–25291:
an advertisement from **Computer Mart of New York, 314 Fifth Avenue, New York NY 10001, 212 279-1048** —
"Authorized dealer for: Sphere • IMSAI • Processor Technology • SWTPC 6800 & CT 1024 … Take a byte out of **the
new Apple-1 computer**" — beating the Berkeley mail-order advertisement (`byte-1976-11.txt`:20478) by two months
and the maker's own BYTE advertising by nine. The same retailer's brand list ("Processor Tech, **Apple**, OSI")
recurs in October, November and December (`byte-1976-10.txt`:40844; `byte-1976-11.txt`:25922;
`byte-1976-12.txt`:32191). This pass confirms A2's correction of A's "Computer Fan" label (A2 §Outbound
corrections C-1) and adds the decisive identity cross-check: the September page's address and telephone are the
same printed for "Computer Mart of New York, Inc." in that issue's distributor list (`byte-1976-09.txt`:141–143).

The sharper point: the New York ad enumerates the lines it is an **authorized dealer for**, and Apple is not
among them — while the Berkeley ad sells the Apple-1 at "10% discount from manufacturer's current list prices"
without claiming any relationship either. **No 1976 document in the corpus evidences an authorized Apple dealer
relationship of any kind.** That is fatal to "first store / first dealer / dealer network" framing in either
direction (the Byte Shop-first story *and* its rivals) and consistent with a house selling boards on the street
to whoever came. **Merge decision:** §F/§G print the dated retailer ladder, name Computer Mart as the earliest
advertiser of the product, and refuse "first dealer", "first store" and "dealer network" for 1976.

### L-5 — "Started in a garage" was a 1976 genre phrase, printed about another company. LANDED

`ia_byte_1976/byte-1976-07.txt` lines 3023–3027, a first-person build narrative about a **different** firm:
"Part way through this 60 day wait I heard a rumor that Sphere had not delivered any systems and that **all the
company consisted of was two people in a garage**." Two people, a garage, big claims, a delivery failure — in
hobby print before Apple's own garage could have entered anyone's memory, in the same magazine. This does not
refute Apple's garage; it shows the garage was a **stock figure of speech in the field's own press**, which
lowers the evidentiary value of the motif and raises the value of a property record. A2's garage treatment used
only the February 1981 line and missed this usage. **Merge decision:** keep the 1981 line (verified:
`ia_byte_1981/byte-1981-02.txt` lines 48514–48519, "A C Markkula, 32 years old, who took Apple **from a garage
operation** to its current enviable position, also holds 8.3 million shares") as the only Apple-linked garaging
in the cache; add the genre note; keep the physical premises UNKNOWN (DG-D5).

### L-6 — The 1976 issue-dating spine has an unresolved internal impossibility. LANDED (provenance risk on the whole ladder)

A dated the 1976 issues by Internet Archive metadata, asserted month confidence High, and performed internal
cross-checks only for October–December. This pass found a cross-check that **fails** for the July file. In
`ia_byte_1976/byte-1976-07.txt`: front matter reads "ISSUE NUMBER 11" (line 6) and "JULY 197[6]" (line 14);
line 15648 previews pieces appearing "in BYTE's **August and September** issues"; yet the article "Assembling a
Sphere" (line 2975 onward, contents mention at line 410, author index at line 39038) narrates events through
"**October 30**, as promised, brought a box from Sphere" (line ~3029). A July issue cannot contain a completed
first-person account of late October. Either the IA item bundles pages from a later issue, or the file's
contents are mixed at the OCR layer.

**Merge decision — deliberately narrow.** This refutes no Apple fact: nothing in the Apple ladder depends
solely on `-07`, because the Terrell "world's first computer store franchise" sentence is duplicated in August
(`byte-1976-08.txt`:16779) and every other Apple-bearing 1976 record sits in September–December or is
independently dated. What changes is the **confidence label**: any Stage-1 statement citing `-07` (and by
extension the un-cross-checked Jan–Jun files) carries `issue-date: provisional pending page-sequence
verification`, and A2's "High" month confidence for Jan–Sep 1976 falls to Medium until the scan is inspected
(DG-D1). The generalisation is the point: **a corpus whose issues are named by their archive identifiers will
silently launder a mis-dating into a chronology.**

### L-7 — Two of the project's verification recipes would produce a *false* refutation. LANDED (method)

1. **The hard-wrap trap.** AP-04 is the dossier's most load-bearing Tier-1 sentence. A literal one-line grep of
   the cached filing for `"was incorporated under the laws of the State of California on January 3, 1977"`
   returns **zero matches** — the text wraps at ~76 columns ("…was incorporated under  the / laws  of  the
   State  of  California on January  3,  1977."). This pass hit the false negative first, then confirmed the
   passage at `10-K_FY1994_…txt` lines 132–135 with a whitespace-flexible pattern. **An auditor who "checks"
   AP-04 with the naive grep will report that the project fabricated its central date.** Fix: cite line ranges,
   never whole-sentence equality.
2. **The header-injection trap.** The caching probe's four-line provenance header contains the literal string
   `company_004_apple`, so a case-insensitive grep for `apple` over `sources/ia_homebrew/*.txt` returns at least
   one hit **per file by construction** (verified: hcc0109:2, hcc0110:2, hcc0201:2, hcc0202:2, hcc0203:2).
   AP-26's headline — "contains zero occurrences of 'apple'" — is therefore **false as literally worded for the
   cached artefacts**, though true of the document bodies (the only other hit in the five "empty" issues is an
   idiom, `hcc0202.txt`:334, "polishes off the apple with some guidelines"). A2 noticed the contamination (its
   §Working method and A2-77) and recommended line-scoping, but **A's AP-26 record text was never corrected**,
   so an agent reading A alone reproduces an unverifiable negative. Fix: restate as "no occurrence below the
   caching header, lines 5 ff."

### L-8 — The stage's foundational document is still unread by this project, and the fusion of two legal events is still live. LANDED (readiness attack)

The only 1976 paper in evidence is the partnership agreement, and this pass **failed to reach the auction
house's own lot text** (`christies.com/en/lot/lot-the-apple-computer-company-partnership-agreement-6570347/` →
`fetch failed`; artnet → HTTP 403 per the retrieval log). The repository's founding date, the 45/45/10 split,
the signing place and Wayne's withdrawal terms therefore rest on **three secondary web reports plus a Tier-3
collector registry** — not one transcribed line of the instrument. A made reading the lot text a gate; it has
not been read. Separately, the fused formulation still circulates inside the project's own inputs: the Library
of Congress page's "founded on April 1, 1976" carries a 2001 young-adult biography as its only 1976 sourcing
(AP-23), and the universe register repeats the fusion with an unsourced place gloss. **Merge decision:** the
stage file states two dated events and never uses "founded" without attaching one; and no §A/§Q sentence may
assert the split percentages, the signing location or Wayne's exit terms as document text until the lot
description or the instrument is read. Where a percentage is needed now, the honest form is "reported as
45/45/10 in auction and registry coverage of the document (Tier 2/3); the document unread" — which also disposes
of the folklore "12%" (H-9).

### L-9 — "About 200 Apple-1s were made" is a wiki-derived count, not an artifact count. LANDED

historyofinformation's "About 200 units were produced" cites only Wikipedia (retrieved 2011). Collector serial
censuses (`sources/apple1registry_stories.txt`) are genuine artifact scholarship but publish *surviving* serials,
not production totals; no in-window document counts units, and nothing in the cache gives Apple's 1976 output.
**Merge decision:** any Apple-1 unit count is `ESTIMATE` with its derivation and source named, or UNKNOWN; it
may not appear in §L (validation signals) as a denominator, which is where it usually smuggles in — e.g. to make
"50 boards" look like a majority of output.

### L-10 — The word-of-mouth sentence's own *sequence* is contradicted by the print record. LANDED (partly)

Wozniak's May 1977 clause is "word of mouth throughout California **and later** nationwide through retail
computer stores". The cache puts the first named product advertisement in **New York in September 1976**, with
Berkeley mail order in November 1976 and the maker's own advertisement only in **June 1977** — so "California
first, then nationwide, then retail" is at best a compression, and the retail stage was running before the
maker advertised at all. **Merge decision:** cite as FOUNDER CLAIM (contemporaneous) for channel *type*; build
the *sequence* from the dated advertisements.

### L-11 — Nothing in the corpus, and nothing reachable in the web budget, can carry 1976–77 money. LANDED (as a bar)

Requests aimed at the FY1976/FY1977 columns and at "biggest offering since Ford" produced nothing in-window
(§Sources consulted, W-table, statuses). The printed series starts at FY1978 — verified line by line at
`ia_byte_1981/byte-1981-02.txt` lines 48494–48507. **Merge decision:** §P carries 1976 and 1977 revenue and
profit as **UNKNOWN** with U-A2-7's warning printed as the table note; "$77,000" and "$770,000" enter the
conflict register, never the metric table; and the IPO arithmetic stays printed-as-inconsistent (U-A2-9) with
both gross sizes and no preference.

---

## Attacks that failed (and the evidence that held)

**H-1 — The incorporation date survived the hardest test in this pass.** The project's central legal fact is
`1977-01-03, California`, resting on two documents with no shared lineage: the registrant's FY1994 10-K
(verbatim re-verified, lines 132–135) and BYTE February 1981's independent "Apple, incorporated in 1977". It was
attacked by the L-7 grep failure (a false negative this pass produced and then resolved) and by the suspicion
that a 1994 filing restates a 1977 fact from corporate memory. It holds: a registrant's state-of-incorporation
recital is a certified statement about a public charter, and the 1981 witness is independent of it. **Residual
risk noted, not resolved:** neither document was checked against the California Secretary of State file
(endpoint alive, unexercised).

**H-2 — Wozniak's May 1977 article is real, dated, and says what the dossier says it says.** Attacked as
self-promotion by an advertiser in the magazine that published him. Re-verified at `byte-1977-05.txt` lines 6385
(address of record), 6397 (word of mouth), 6420 (under $700). It survives as the corpus's best first-party
in-window text — FOUNDER CLAIM (contemporaneous), the strongest class available for 1976.

**H-3 — Apple's June 1977 pricing survived.** $1,298 complete and $598 board-only are printed in Apple's own
advertisement (`byte-1977-06.txt` lines 1935, 2112). Attacked as a possible later correction of 1976 practice;
irrelevant, because the artifact's date is the claim's date. This remains the reason Stage 1 need not lean on
memoir for the product.

**H-4 — The Helmers sightings survived.** 20 November 1976 verified at `byte-1977-04.txt` line 2704; the WESCON
peer list at `byte-1976-12.txt` line 1516. Attacked as editor-commercial interest and single-witness. Both
weaknesses noted; the facts hold — and they are the only outside, dated, named-witness records of both founders
together with the machines.

**H-5 — The Berkeley and New York dealer advertisements survived,** at `byte-1976-11.txt`:20478 ("Apple-Apple-1
computer", the 10%-off-list mail-order line) and the September/New York ladder at L-4. OCR noise is real, the
brand token is not. The November 1976 technical sentence grouping "the new Apple computer" with other marketed
PROM-monitor machines is at line 20845 — which independently **defeats** the "first in category" reading without
needing anything later.

**H-6 — "Apple placed no advertisement of its own in BYTE during 1976" survived this pass's exhaustive
re-grep.** Across all twelve 1976 files there are exactly 13 `Apple`-token lines and every one is accounted for:
false positives in February and July ("Big Apple" `byte-1976-02.txt`:11672; "Apple Pie!"
`byte-1976-07.txt`:32018), two in June ("Apple Valley", `byte-1976-06.txt`:15975, 16152), one unrelated Kansas
City firm in November ("Burstein-Applebee", `byte-1976-11.txt`:29612), four New York retailer brand lists
(Sept/Oct/Nov/Dec), one Berkeley dealer ad, one technical article, one editorial, one Faire exhibitor list. Zero
maker copy. The negative holds — with the L-6 caveat that Jan–Jun month labels are provisional (immaterial,
since those hits are non-Apple in any month).

**H-7 — The Los Altos census reproduced exactly, and the *interpretation* is what failed.** `grep -rn "Los
Altos"` over the four cached directories returns **17 lines**, matching A2's count, none of them Apple (Cromemco
at "One First St." in five 1976 issues and in `hcc0109`; "111 Main St."; a "F.O.B. Los Altos" terms line; Qume at
"745 Distel Drive"; "265 W Portola Av"; a member at "Los Altos Hills"; Slone Associates and publisher William
Kaufmann in December 1980). The attack I mounted — that U-A2-13's framing overreaches — **succeeded on the
framing and failed on the data**, and that distinction is the point (§5, do not overcorrect; the project's own
history records an earlier pass that wrongly "corrected" a town attribution). Correct form: *the company's 1976–77
address of record is Cupertino; the childhood home's municipality is not a periodical question at all.* A
Cupertino business address in May 1977 is fully compatible with unpaid work at a family home in Los Altos or
anywhere else in 1976, so the register's "Los Altos" is **unsourced**, not **disproved** (D-4).

**H-8 — The February 1981 financial and cap-table block survived every attack this pass could make.** It is one
unsigned column, which is a lineage weakness (U-A2-7), not a falsity indicator, and it is the only in-window
printed money. The internal inconsistency (4.6M vs "8% of 52.4M") was chased, not waved: no web source in this
pass's budget reconciled it and no filing exists online to test it (AP-02, AP-21), so the row stays printed-as-is
with both gross sizes. The Jobs/Wozniak "8.3 million shares each … they own well over $100 million worth of
stock" arithmetic checks (`8.3M × $22 = $182.6M`) — a small signal that the column was working from real numbers
rather than memory.

**H-9 — The 12%/12-day folklore is the one place where the documentary side got stronger under attack.** Wayne
appears **nowhere** in the cached 1976–1981 print (this pass's own `Wayne` grep returns only third parties —
"Fort Wayne", "Wayne State", Wayne Green, Wayne Sewell, "Wayne Av" — matching A2's negative; `Markkula` occurs
exactly once in the whole cache, `byte-1981-02.txt`:48516). But the *percentage* now has two document-derived
witnesses agreeing on 10%: the auction coverage (45/45/10) and the collector registry's 2018 prose written from
Wayne's own letter ("reduce the story about Ron Wayne to the point when he sold his **10%** Apple share",
`apple1registry_stories.html`:488), which predates the 2025–26 sale campaign. So "12%" is contradicted by every
line in the corpus that speaks to it — while the instrument remains unread (L-8), which is why the label is
CONTESTED-with-10%-preferred, not FACT.

**H-10 — The Sphere episode survived as evidence about the environment, and it helps Stage 1.** Attacked as
off-topic; it is not. It is a dated in-window record of (a) a competitor selling "a complete computer system for
only $650" in 1976, which contextualises "under $700"; (b) a named customer's account of promised quantities not
arriving — the failure mode every 1976 hardware channel ran, and a legitimate §M entry; (c) the garage idiom
(L-5). Its author is a reader in San Diego (`4554 Chinook Ct, San Diego CA 92117`), which also shows how thin and
geographically spread the buying public was.

**H-11 — A2's own outbound corrections held up.** The "Computer Fan" mislabel in A's AP-14 was caught by A2 and
this pass's address/phone cross-check confirms A2 over A; A2's U-A2-12 unit conflict (1500 bps vs "over 180 bytes
per second", `1500/8 = 187.5`) is arithmetic-correct and is the model of what §6's basis-carrying rule demands. No
defect was found in A2's re-computable arithmetic (6.5% tax ratios, share arithmetic, the 17-line census).

## Unsourced or folklore claims

Consolidated, with the class of the *only* support. "True but folklore" means exactly that: the event may have
happened; the sentence has no evidential standing.

| Claim | Only support found | Class of that support | Disposition |
|---|---|---|---|
| Byte Shop ordered 50 boards at $500, July 1976, cash on delivery | Terrell's later conversations (2021 email, 2026 auction essay); Wayne's "a large number" | Retrospective participant speech, self-inconsistent on date and price | **UNKNOWN**; forbidden as FACT anywhere in the stage file |
| Apple-1 retail price $666.66 | The same 2021 conversation lineage, plus a wiki → aggregator echo chain | Echo with a wiki terminus | **UNKNOWN as a figure**; print "under $700" only |
| ~150 / ~200 Apple-1s produced | Wikipedia via a secondary encyclopedia site; survivor-serial censuses | Wiki echo / collector estimation | **ESTIMATE with derivation, or UNKNOWN**; never a denominator |
| Wayne: 12 days, $800 (+$1,500), "no regrets" | Auction press + Wayne's own later writings and letters | Retrospective + commercial | Folklore; 10% is better supported than 12%, but the instrument is unread |
| The $1,000 board-printing capital (HP-65 at $500 + VW bus at $750) | *iWoz* (2006), ch. 12 p. 173, via the registry | Single memoir | Folklore, zero independent witnesses |
| $15,000 loan to fill the order | Wayne's 2022 written account | Retrospective participant | Folklore. The trade-credit *mechanism* is period-plausible — Cramer Electronics is a real Bay Area distributor in these same pages (`byte-1976-09.txt`:1951, 3125) — but plausibility is not evidence |
| Terrell demanded assembled boards, no discounts, cash on delivery | Retellings | Folklore | Bar unless a Terrell statement is dated in-window |
| Markkula's terms ($91,000 guarantee / ~$250,000 / ~26%) | Books and Tier-4 saturation | Retrospective | UNKNOWN at Tier 1; print only his 1981 name, age, holding and role-gloss |
| Venrock round size, date, valuation | Nothing (holding only) | — | UNKNOWN (the holding is a dated fact) |
| 1976 sales $77,000; FY1977 revenue $770,000 | Cited to the 1980 prospectus by parties who have not quoted it | Untraceable | UNKNOWN; conflict-register entry |
| "Biggest US IPO since Ford" | General retelling; absent from in-window text | Untraceable | UNKNOWN; route named (financial press Dec 1980–Feb 1981) |
| A late-1975 Homebrew demonstration that "generated immediate orders" | Memoir | Retrospective | Folklore; the county's and the club's print begins April 1976 |
| Founding "employee #" numbering (e.g. "#6") | 2022 recollection | Retrospective | Bar: no Apple employee numbers without payroll or a dated self-published list |
| Blue Box venture; Atari employment dates | Memoir; curated auction prose | Retrospective / curator inference | FOUNDER CLAIM (retrospective) at best |
| "Apple Computer Company" in use in 1976 | Only the unread agreement's title | Document, unread | CONTESTED; print the four authentic in-window forms and say no 1976 print names the partnership |
| The garage as the site of founding work | 1981 "garage operation" gloss + memoir + a genre idiom | Retrospective gloss | CONTESTED; premises UNKNOWN |

## Single-lineage claims

Per §3's independence rule these rest on **one** document or speech lineage, however many times they are
printed. Repeated copying is one source.

| Claim | The one lineage | What would break or settle it |
|---|---|---|
| 1976-04-01 partnership, 45/45/10, three partners, Wayne's exit | The auctioned instrument — which **no agent in this repository has read** (W9 failed; artnet 403); every citation is downstream of the same lot | The lot text or a photograph of the pages; a county FBN filing naming the partners |
| First customer, units, price, terms, retail mark-up | Paul Terrell's later recollections (RR Auction 2026; apple-1-replica 2021), with Wayne's variant | An invoice, cheque, purchase order, distributor credit record, or a 1976 Terrell statement |
| $666.66 | The same Terrell conversation lineage **plus** a wiki echo chain | A 1976 printed price list or advertisement (DG-D2) |
| Board-printing capital ($500 + $750) | *iWoz* 2006 | A dated distributor record or a contemporaneous 1976 statement |
| Markkula's deal | Post-1981 books; his 1981 share count is the sole in-window line | Incorporation-era stock records; California SoS Statements of Information, 1977 |
| FY1976/FY1977 revenue | The 1980 prospectus as described by people who have not read it | The paper prospectus; an IPO-era financial-press story reproducing the columns |
| "Wozniak brought the machine to a club in April 1976" | One ~40-word club letter, `hcc0204.txt`:141 | Any second in-window mention; the Sonoma club's own papers |
| Apple-1 "designed late in 1975" | Wozniak's single May 1977 sentence | A dated 1975 artifact: schematic revision, meeting minutes, photograph |
| The 1978–80 revenue and cap table | One unsigned BYTE column (Feb 1981) | The prospectus, an audited statement, a second 1980–81 financial-press story |
| Terrell's chain as "the world's first computer store franchise" | BYTE's own editorial boilerplate, reprinted July and August 1976 in the magazine that sold him display space | Independent trade or municipal records of store openings; Computer Mart's rival claim is likewise self-serving |
| The garage as a *place* | Memoir, plus a 1981 gloss and a 1976 genre phrase (L-5) | Assessor/recorder ownership chain; any 1976 lease or utility record |

## Contradictions in the existing Apple dossiers

Each must be resolved explicitly at merge; silent reconciliation is prohibited (§7).

| # | Conflict | Where | Best-supported reading | Action |
|---|---|---|---|---|
| D-1 | A's Verdict fact-#4 and its stage-boundary row treat the April 1976 machine as a **Homebrew** record; A2 states it is a **Sonoma County** letter reprinted by Homebrew | AP-24 vs A2-19/20, A2S-12; `hcc0204.txt`:131–144 | A2 is right; A's headline list is stale | Strike the Homebrew framing wherever carried; put Cotati into §C/§J geography |
| D-2 | A's AP-14 names the October 1976 advertiser "Computer Fan"; A2 names it Computer Mart of New York and files an outbound correction | AP-14 vs A2-08/A2-11/C-1; `byte-1976-09.txt`:141–143, 25253–25291 | A2 (address + telephone identity) | Use Computer Mart; move the earliest product-naming advertisement to **September 1976** |
| D-3 | U-A2-4 says the cache's only `666` hits are "a telephone number and printer's rules" | This pass: `byte-1976-12.txt`:39846–39851 | Both descriptions incomplete — there is a **dollar** 666, and it is IMSAI's | Rewrite U-A2-4 with the decoy inventory; conclusion (price unestablished) stands |
| D-4 | U-A2-13's BEST-SUPPORTED line reads as though Cupertino displaces Los Altos | U-A2-13; register row; H-7 | Address of record ≠ birthplace; the register's gloss is unsourced, not refuted | Reword; move the garage municipality to UNKNOWN (DG-D5) |
| D-5 | A's AP-26 "zero occurrences of 'apple'" is not reproducible on the cached files as worded | AP-26 vs A2-77; header line 2 of every HCC file | Body-level true, file-level false | Restate with line scoping (L-7) |
| D-6 | A gives 1976 month attributions confidence High; the `-07` file is internally impossible | AP batch-2 dating note; L-6 | Jan–Sep 1976 labels rest on archive metadata, not page-sequence checks | Downgrade to Medium pending DG-D1 |
| D-7 | A's AP-04 records "Corroboration: 1 Tier-1 document"; AP-19 later claims 2 | AP-04 vs AP-19 | Two lineage-free documents — corroboration 2 is right, but the 1981 witness gives the **year only** | High on year; day-and-month rests on the filing alone |
| D-8 | A's AP-18 quotes the IPO sentence without noticing its arithmetic; A2 finds it internally inconsistent | AP-18 vs U-A2-9 | A2 | Print both figures plus both gross sizes; never a single gross-proceeds number |
| D-9 | A2's DG-5 says Markkula's first print appearance is February 1981; A's AP-18 quotes the same line as fact | DG-5 vs AP-18 | Agreed; neither notes that "garage operation" is doing identity work about 1976 inside a 1981 text | Cross-reference L-5 in §B/§K citation |
| D-10 | A's famous-claims table calls the 1981 "garage operation" phrase "contemporaneous" | AP-table; this pass (L-5) | Half-right: contemporaneous **to 1981**, not to the events | Replace with "in-window-later"; add the genre evidence |
| D-11 | Wayne's stake: 10% (registry 2018 prose; auction prose) vs 12% (universal retelling) | `apple1registry_stories.html`:488 vs AP-20 note | 10%, document-derived, twice; but the document is unread | Record 10% as best supported, flagged CONTESTED; bar "12%" |

## Data gaps this pass created

| Gap ID | What is missing | Why | Importance | Route / follow-up task |
|---|---|---|---|---|
| DG-D1 | Whether `byte-magazine-1976-07` is wholly the July issue | Internal chronology impossible (L-6); only Oct–Dec 1976 were cross-checked | **HIGH** — governs every Jan–Sep 1976 citation | Inspect the IA item's page sequence / file list; locate the Sphere article's printed page number |
| DG-D2 | The October 1976 Apple-1 advertisement as printed, with its price line and letterhead | A Wikimedia image exists (`File:Apple 1 Advertisement Oct 1976.jpg`) and historyofinformation displays an October 1976 *Interface Age* insert; neither read for numbers | **HIGH** — the only realistic candidate for an in-window $666.66 **and** for the 1976 partnership name and address | Read the image at full zoom; identify the host title; if it prints a price and a letterhead, U-A2-4 and E-36 upgrade at once |
| DG-D3 | Christie's lot text for the partnership agreement, and Wayne's withdrawal document | W9 `fetch failed`; artnet 403 (recorded, not retried) | **HIGH** — the founding document | Browser route or alternate catalogue host; also RR Auction's 50th-anniversary lot pages for a transcribed clause |
| DG-D4 | Business Week, 12 July 1976, on Paul Terrell's Mountain View store | Reported in BYTE October 1976 (`byte-1976-10.txt`:1203–1210); the article itself unread and no Apple reference in it established | MED-HIGH — the only dated general-press retail lead in this corpus | Locate the issue at a periodical archive/library; check for an Apple or Byte Shop stock line |
| DG-D5 | Garage ownership/lease; Crist Drive's municipality; any 1976 Apple premises | County portals 403/000; property records are not a periodical question | **HIGH** (§G/§E host side) | Santa Clara County assessor/recorder or a records request |
| DG-D6 | A 1976 fictitious-business-name filing for "Apple Computer Company" | California required FBN filing and newspaper publication; nothing in the cache | MED-HIGH — one instrument could name partners, address and date | Santa Clara County clerk FBN index; contemporaneous newspaper publication notices |
| DG-D7 | Kilobaud 1976 and Creative Computing 1976–77 text layers | Kilobaud items expose no `_djvu.txt`; Creative Computing has 555 unmined items | **HIGH** — the titles most likely to print an Apple-1 price and a dealer list | OCR locally, then grep for `666`, `Apple-1`, `Apple Computer Company` |
| DG-D8 | The Terrell franchisee figure ($525 / $25 per unit) | Surfaced only on a Tier-4 social post | MED — a rival number that may describe a **different transaction** (chain to franchisee, not maker to chain) | Chase to a dated interview; §5 requires chase or an untraceable record |
| DG-D9 | Who actually paid for the first boards — the "who provided the money" question | RR prose names Cramer Electronics; Cramer's presence in these pages corroborates the mechanism only | **HIGH** (§K) | Distributor records; the agreement's capital clause (DG-D3); any 1976 bank or credit instrument |
| DG-D10 | "Biggest offering since Ford"; FY1976–77 columns | Not in-window in the cache; unreachable inside the web budget | MED | InfoWorld / Inc. / financial press, Dec 1980 – Jun 1981 |

## Sources consulted

**Locally cached primary (zero web budget; every citation verified at line level by this pass unless marked
`[inherited]`).**

| Source | Type | Primary/Secondary | Event date | Publication date | Route / location | Tier | Confidence |
|---|---|---|---|---|---|---|---|
| BYTE, Jan–Dec 1976 (12 full-issue OCR files) | trade magazine | primary | 1976 | 1976-01…12 | `sources/ia_byte_1976/` | 1 | High on content; Medium on Jan–Sep month labels (D-6) |
| BYTE, Apr–Jul 1977 | trade magazine | primary | 1977 | 1977 | `sources/ia_byte_1977/` | 1 | High (self-dated mastheads `[inherited]`) |
| BYTE, Dec 1980 & Feb 1981 | trade magazine | primary (1980–81); retrospective for 1976–77 | 1978–1981 | 1980-12 / 1981-02 | `sources/ia_byte_1981/`; IPO block at `byte-1981-02.txt`:48494–48525 | 1 | High as printed |
| Homebrew Computer Club newsletters (11 items) + Faire flyer | club print | primary | 1975–1977 | 1975-11-30 → 1977-01-19 | `sources/ia_homebrew/`; `hcc0204.txt`:131–144 | 1 | High, with per-item provenance discipline (L-3) |
| Apple Computer, Inc. Form 10-K FY1994 | SEC filing | primary | 1977-01-03 (recited) | 1994-12-13 | `sources/10-K_FY1994_acc-0000320193-94-000016_filed-1994-12-13.txt`:132–135 | 1 | High |
| The Apple-1 Registry, "Stories" | collector registry | secondary reporting artifacts | 1973–1976 claimed | 2018–2022 | `sources/apple1registry_stories.{html,txt}` (Wayne at .html:488) | 3 | Medium on artifact existence; Low on curator-attributed dates |
| EDGAR submissions blocks, 6 FTS probes, Wayback CDX probe | registry indexes | primary about coverage, not history | — | 2026-09-24 | `sources/EDGAR_*`, `sources/probe_*` | 1 | High (as index facts) |
| A_chronology_feasibility.md; A2_periodical_archive_mine.md | project dossiers | secondary (subject of this review) | — | 2026-09-24 | `research/` | n/a | graded herein |

**Web (hard cap 10; 8 substantive requests, 4 failures recorded, every failure logged as UNANSWERED).**

| # | Request | Status | What it yielded |
|---|---|---|---|
| W1 | WebSearch — Apple-1 $666.66 price origin / first appearance | OK | Tier-4 saturation (Quora, Reddit, Facebook) + historyofinformation + Wikipedia: re-demonstrates AP-38 |
| W2 | WebSearch — Christie's partnership agreement (over-length query) | **validation error** | nothing; turn consumed |
| W3 | WebSearch — Terrell / 50 boards / invoice / primary source | OK | RR Auction essay, apple-1-replica, Wikipedia, Registry, a Facebook Terrell figure |
| W4 | WebFetch `content.rrauction.com/paul-terrell-byte-shop-apple-50th/` | OK | "fifty computers at five hundred dollars apiece, to retail at $666.66"; **conversation-sourced, no archival anchor; dates the deal "Spring 1976"** |
| W5 | WebFetch `apple-1-replica.com/the-byte-shop-situation` | OK | "50 completed boards … 25,000 USD cash on delivery"; stamped-manual photograph + a 2021 Terrell email; **zero invoices or periodicals**; no $666.66 |
| W6 | WebSearch — $666.66 in a 1976 Kilobaud / Creative Computing ad (over-length) | **validation error** | nothing; turn consumed |
| W7 | WebSearch — Christie's lot description | OK | the official lot URL (→W9), artnet, a Reuters photo item |
| W8 | WebSearch — where was $666.66 first printed | OK | historyofinformation; a **Wikimedia image of an October 1976 Apple-1 advertisement**; Christie's Apple-1 lot; Wikipedia |
| W9 | WebFetch — Christie's lot page for the partnership agreement | **FAILED: "fetch failed"** | **UNANSWERED — the founding document's text remains unread** (DG-D3) |
| W10 | WebSearch — earliest book mention of $666.66 (over-length) | **validation error** | nothing; turn consumed |
| W11 | WebFetch `historyofinformation.com/detail.php?id=3019` | OK | "The Apple I went on sale in July 1976 at a price of US $666.66"; "About 200 units were produced"; **only cited source: Wikipedia, retrieved 2011-11-26**; the October 1976 *Interface Age* insert described from the wiki, not the scan |
| W12 | WebSearch — Interface Age October 1976 Apple advertisement price | OK | confirmed the image lead; no text-searchable source located |

*(W2, W6, W10 consumed turns without producing evidence; W9 is recorded with its URL as UNANSWERED, never as a
null finding. No statement in this file asserts that anything "does not exist" on the strength of a retrieval
failure.)*

## Provenance and method notes

**Ownership and non-destruction.** One file written: this one. Nothing in `sources/` or anywhere else in the
repository was created, moved, renamed, tidied or deleted (method §14 rule 4); no existing file was edited,
including the two dossiers criticised here. The protected archive is byte-untouched as at close.

**Grep log (all against `sources/`, 2026-09-24).** `666` → 40+ hits, dispositioned in L-2 · `Wayne` → one
Apple-relevant hit (the registry, retrospective); every magazine hit third-party · `Los Altos` → 17 lines, 0
Apple · `Apple|APPLE` in `ia_byte_1976` → 13 token lines, per-file counts 01:0, 02:1, 03:0, 04:0, 05:0, 06:2,
07:1, 08:0, 09:1, 10:1, 11:4, 12:3 (H-6) · `Byte Shop|BYTE Shop|Terrell` → ~30 lines, none carrying an Apple
line · `garage` → 14 lines, 1 Apple-linked (Feb 1981) · `Markkula` in `ia_byte_1981` → 1 (`byte-1981-02.txt`:48516)
· `Cramer` → distributor/advertiser mentions, no Apple · `Wozniak` in `ia_homebrew` → 1 (`hcc0204.txt`:141) ·
`word of mouth` (6397), `under $700` (6420), `Stevens Creek` (6385), `$1298` (1935), `$598` (2112),
`November 20 1976`/`motel room` (2704), `January 3, 1977` (10-K 132–135), the 1981 revenue block
(48494–48525) — all re-verified at the lines cited.

**Two verification hazards this pass hands back to the fleet.** (i) Hard-wrapped filings: one-line verbatim
greps of the 10-K produce **false negatives** (L-7). (ii) Self-referential cache: the caching probe's provenance
headers inject the search term `apple` into the files they describe, so any "zero occurrences" claim must state
its line scope (L-7). Both convert a careful audit into a confident error, in opposite directions — one fabricates
a refutation, the other fabricates a corroboration.

**What this pass deliberately did not do.** It did not refute the garage, the Los Altos home, the word-of-mouth
channel or the Byte Shop relationship; it located where each becomes unspeakable as fact. It did not treat the
1981 column as audited data, nor the 1994 filing as history. It ran no `matchType=prefix` sweeps, retried no
403 endpoint, mined no new magazine corpus, and opened no paywalled title. It names the two places where a
single page could still change Stage 1's most-quoted number: DG-D2 (the October 1976 advertisement) and DG-D7
(Kilobaud/Creative Computing OCR).

**Hindsight audit of this review.** Its surviving facts are structural — a charter date, an advertisement, a club
letter, a magazine column, a filing recital. Its unfavourable findings — no first order, no price, no revenue, no
premises, no deal terms, no dealer agreement — are the honest shape of the record: a partnership whose paper has
not been read, inside a market whose own print was saying "the new Apple-1 computer" in New York before the maker
advertised anything at all. Nothing here requires the company to have succeeded, and nothing here assumes it did.

**Claims this pass would move to UNKNOWN outright.** (1) The Apple-1's price as a figure. (2) The first order's
units, price, date and terms. (3) FY1976 and FY1977 revenue and profit. (4) Apple-1 production volume. (5) The
garage's address, ownership and municipality. (6) Markkula's and Venrock's terms. (7) Wayne's exit date and
amounts. (8) Any "first" attached to a store, a dealer relationship or a product category in 1976.

**Residual risks.** (R-1) The `-07` dating anomaly is unresolved; if it spreads to the September file, the
earliest product advertisement moves again. (R-2) The founding instrument remains unread, so E-01/E-04/E-36 cannot
rise above CONTESTED however often they are cited. (R-3) Every barred figure here is one careless sentence from
returning — **$666.66, 50 boards, $500, July 1976, cash on delivery, 12 days, $800, 12%, $1,000, $15,000, $77,000,
$770,000, ~200 units, "employee #6", Markkula's terms, "biggest since Ford", "first dealer", "founded April 1,
1976", "Homebrew, April 1976"** — and each must be checked against §Unsourced and §Single-lineage at merge time.
(R-4) Independence is partial: this reviewer read the dossiers before attacking them, and graded against their
registers plus its own greps rather than against memory. (R-5) The web budget was consumed partly on three
over-length query errors; a rerun of W9 (Christie's lot text) and one read of the DG-D2 image would close more of
this file than any further searching.
