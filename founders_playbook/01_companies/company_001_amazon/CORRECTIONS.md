# Provenance Corrections Register — Amazon Stage 1

Standing list of citation and attribution corrections established **after** the dossiers were
written, each verified directly against primary documents rather than accepted from a summary.
The consolidation leads were briefed before several of these landed, so their output may still
carry the pre-correction form.

**Rule: `stage_1.md`, `stage_1_claim_records.md`, `context_appendices.md` and every CSV must be
emitted with these corrections applied. Reverting one is a defect, and a claim whose only support
is a document that must be relabeled to a version that does not contain it is downgraded to
`UNKNOWN` until re-verified — not quietly kept.**

**Superseded entries are marked where they stand, not only where they were retired.** One correction in
this register has been fully superseded: **COR-03 is superseded by COR-12** (2026-09-23), and its Action
line is withdrawn; a top-down reader must not apply it. Any other cross-reference in this file that says
"see COR-03" is routed through that marker.

---

## COR-01 — the accession everyone cited is an amendment, not the S-1

Verified from the restored filings' own headers (`sources/`):

| Document | Accession | Filed | Bytes |
|---|---|---|---|
| **Form S-1 (original)** | **0000891618-97-001309** | 1997-03-24 | 1,445,709 |
| **S-1/A No. 3** | 0000891020-97-000755 | 1997-05-09 | 306,425 |
| **S-1/A No. 5** | **0000891020-97-000839** | **1997-05-14** | 303,069 |
| FY1997 annual report, form **10-K405** | 0000891020-98-000448 | 1998-03-30 | 607,959 |

Most briefs and several dossiers cite **0000891020-97-000839** as "the S-1". It is **S-1/A No. 5**.
The adversarial dossier's "Amendment No. 4, 9 May 1997" is **No. 3** by the restored file's own
label (same date, wrong ordinal). Independently confirmed twice — by the graphics agent's
document-count arithmetic and by the Evidence Registrar's read-back on 2026-09-23, which also
restored all four filings to `sources/` with retrieval headers.

The FY1997 annual report is filed as form **10-K405** (a 10-K with a late-filing delinquency
cover), not a plain 10-K; cite the form as filed.

**Action:** relabel to `S-1/A No. 5 (acc. 0000891020-97-000839, filed 1997-05-14)` wherever that
accession was cited, and to the original where the original is meant. Where a dossier cites
No. 5 for a fact that exists **only** in the original, the citation becomes the original and the
date "1997-03-24".

## COR-02 — three founding-instrument facts exist in the **original S-1 only**

Cross-checked string-by-string across all four filings:

| Fact | Original S-1 | A3 | A5 | FY1997 10-K |
|---|---|---|---|---|
| "Cadabra, Inc., a Washington corporation" — *"subscribes for 1,700,000 shares of the common stock of Cadabra, Inc."* | **present** | absent | absent | absent |
| "approved by the Board of Directors and **the sole stockholder on September 15, 1994**" | **present** | absent | absent | absent |
| "1,700,000 shares" (founder-holding and investor-purchase passages) | present | absent | absent | absent |

The documents that establish the founding itself are therefore **only in the original**, and any
record citing the amendment for them is corrected to `S-1 (original), acc. 0000891618-97-001309,
filed 1997-03-24`. Everything else in the spine is version-safe: `$511`, "commenced offering
products", `0.1717`, `2,200`, Seafirst, Wells Fargo, Ingram, `400,000`, `15,746`, `107,000`,
"interest-free" all appear in **every** version tested, so relabeling them changes nothing
substantive.

## COR-03 [SUPERSEDED BY COR-12, 2026-09-23] — the employee count is a January figure, not a December one

> **[SUPERSEDED IN FULL BY COR-12, 2026-09-23 — do not apply this correction.]** COR-12 re-read the
> employee sentences in all three filing versions and established that "11 employees at 1995-12-31" **is**
> filed, at that date, in S-1/A No. 3 and No. 5. Everything below is retained as the record of what was
> believed when this entry was written; its Action line is withdrawn. Read COR-12 instead. Text below is
> left standing because this register appends and never rewrites history — but a reader working the file
> top-down meets this entry first, so the marker is here, in place, and not only 150 lines later.

Verified wording (original S-1): *"…from January 1, 1996 to December 31, 1996, the Company
expanded from **11 to 151 employees**"* and *"As of December 31, 1996, the Company employed 151
full-time employees."*

So "11 employees" is the filing's **1996-01-01** figure, and it is not styled "full-time" at that
point. Dossiers render it as "11 employees at 1995-12-31".

**Action [WITHDRAWN BY COR-12 — the rule below is inverted and must not be applied]:** section R and P state `11 employees (per the filing: at 1996-01-01)` and note the
one-day difference is immaterial to the boundary but the phrasing is the filing's, not ours. The
`151` figure is **post-Stage-1** and belongs only in the consequence column, never in the Stage-1
snapshot.

**Action as it now stands (COR-12):** §R and §P state **11 employees at 1995-12-31**, cited to S-1/A No. 3
and No. 5; the original S-1's 1996-01-01 phrasing is the same instrument's first state and is recorded as
version evidence on that count, never as a second confirmation (method §3 filing-lineage rule).

## COR-04 — the "lost screenshots" were never images; and their captions are 1997

The S-1 figure caption `[PICTURES OF THE COMPANY'S WELCOME, SEARCH, REVIEW AND ORDERING WEB PAGES]`
is **a printer's art-direction instruction printed in square brackets in the text itself**. Proved,
not assumed: the original's `PUBLIC DOCUMENT COUNT: 38` accounts exactly for the 38 `index.json`
rows and 38 `<DOCUMENT>` blocks, totalling 1,438,356 B against the 1,444,013 B file; zero
`<TYPE>GRAPHIC`, zero `<img>`, zero `.gif`/`.jpg`, zero base64. The same arithmetic closes all
eight 1997 accessions. **0 images exist; there is nothing to recover.** `sources/s1_graphics/INVENTORY.md`.

**Two consequences for section E:**
1. It may **not** claim surviving images of the 1995-96 site. What survives is the *plan* to show
   welcome, search and ordering pages (with "review" named only collectively in the original and
   dropped from the amendments), plus the S-1/A cover and p.66 art plan naming seven pages with
   quoted captions — **"2.5 million titles", "40% discount", warehouse/barcode shots, an email
   confirmation specimen**.
2. Those captions sit in **1997** filings, so `2.5 million` and `40%` are **1997 marketing
   numbers and must not be back-projected into Stage 1**. The in-window figure is ~1M titles
   (press release 1995-10-04). This is the same time-trap as COR-05 and belongs in section U.

## COR-05 — the circulating "1996 Amazon homepage" is 2006 content

`wb_amazon.html` was a **2006-05-22** capture; Wayback holds **no amazon.com root capture before
1998-12-12**, and that one is a bare 302. Earliest *rendered* homepage: **1999-08-28**. Any
"Amazon in 1996" screenshot online is silently served from a much later capture. Honest limit:
deep-path 1996 absence is **unanswered, not proven** — those CDX `matchType=prefix` queries
**504'd**, they did not return empty.

## COR-06 — `sheff.txt` is a Playboy interview conducted 1999, published 2000

Its own header states this, confirmed on re-retrieval by the Evidence Registrar. Every Stage-1
statement inside it is a **retrospective founder account**.

**Consequence, stated plainly because it shapes sections B, C and N: no contemporaneous
founder-state interview has been located for Stage 1.** Sheff's genuinely 1994 Wired profile of
Bezos remains unfound, and the widely-quoted Bezos origin quotations all post-date the window by
five years or more. The one in-window exception is the **press release of 1995-10-04, which carries
a Bezos quotation** — contemporaneous in date but **company-issued**, so it is a founder statement
made for publicity about the firm's own performance, not independent reporting of his reasoning.
Section N must therefore say that the founders' *reasoning* in 1994-95 is largely unrecoverable,
and that what exists is (a) a public relations quotation from 1995, and (b) retrospective
interviews from 1999 onward. That is a data gap about the record, not a gap in the history.

Zero dossier records carried my bad "1994" label (audit 2026-09-23); the error was mine, introduced
in the evidence cache, and caught by the agents reading the document.

## COR-07 — other cached documents reclassified as retrospective

`lat.txt` = LA Times, Littman, **1997-07-20**. `hl.txt` = HistoryLink essay 23230, published
**2025-04-07**. `amztimeline.html` = capture stamp **2007-10-27** (company self-narrative as of
2007). `wiki.txt` = Tier-4 lead. `ncsa.html` = NCSA Mosaic "What's New", **August 1995** — one of
the few genuinely in-window technology artifacts, and it stays Tier 1.

## COR-08 — destroyed evidence, re-verified

The adversarial agent's cleanup deleted the shared `_scratch` folder on 2026-09-23.
**Restored to `sources/` the same day by the Evidence Registrar, each with URL / access-date /
size / completeness headers and verified by read-back:** original S-1 (1,445,709 B), S-1/A No. 3
(306,425 B), S-1/A No. 5 (303,069 B), 10-K405 FY1997 (607,959 B), the Sheff interview (52,098 B
text / 133,811 B html), HistoryLink 23230 (21,399 B / 54,616 B), the NCSA Mosaic August-1995 page
(985,639 B), and `NULL_RESULT_wayback_1995_1996.md` (4,427 B). **Four load-bearing dossier
quotations were re-verified verbatim against the restored text.** Retrieval friction recorded: the
SEC first returned a genuine transient `503 File Unavailable` before the declared User-Agent
resolved the earlier 403, and bodies arrived gzipped; legacy EDGAR leaves document names blank, so
complete-submission `.txt` files were used.

**Still missing, and low-consequence:** `lat.txt`, `stone.txt`, `wiki.txt`, `p.html`,
`amztimeline.html`, `wb_amazon.html` — all retrospective or Tier-4 by our own classification, and
none carrying a Stage-1 fact that is not duplicated in a filing or a press release. Records citing
them are marked `restoration pending` in section T until re-verified.

One further trap the Mosaic retrieval exposed: the **only "Amazon" in the August-1995 Mosaic "What's
New" archive is the river.** The page is a legitimate in-window technology artifact, but it is not
evidence about the company, and no dossier may cite it as such.

## COR-10 — the first money round IS in the filings; dossier E was wrong

A consolidation lead flagged a direct contradiction: dossier **E** reported that the filings record
*no round total or participant count*, while dossier **H** found a disclosed figure in S-1/A Item 5.
Verified against the restored text of **both** the original S-1 and S-1/A No. 5, where the passages
appear identically:

- *"…aggregate of 3,021,000 shares of Common Stock **to 23 investors** for a consideration of
  approximately **$.3333 per share, or an aggregate of $1,007,000**."* (original S-1 reads "23
  investors"; S-1/A No. 5 reads "23 purchasers" — same transaction, wording differs between versions.)
- An earlier priced tranche: *"…consideration of approximately **$.1717 per share, or an aggregate
  of $345,525**."*
- Later preferred rounds, **outside Stage 1**: *"…or an aggregate of **$8,000,014**"* and a further
  Series A passage of *"an aggregate of $200,000"*.

**Actions:**
1. **Delete E's "no round total disclosed" claim** from section K and from the conflict register;
   the disclosure exists and is now cited to the original S-1 (acc. 0000891618-97-001309,
   1997-03-24).
2. **Section K states the audited facts, not the legend.** The popular *"$1.1M from 22 friends and
   family at $50,000 each"* is **near but not equal** to the disclosure: **23 purchasers,
   $1,007,000, at $0.3333/share**. Per-investor amounts are not disclosed; do not assert $50,000
   each. The identity of the 23 is not disclosed either — the four in-window Shareholder's
   Agreements (H) name father, mother's trust, Kaphan and Alberg, which is *evidence of some*
   participants, not the roster.
3. **Time-basis trap:** H dates the $1,007,000 subscriptions **1995-12-06 → 1996-05-16**, so most
   of that round is **after the Stage-1 endpoint of 1995-12-31**. Section K must split
   in-window cash (E's audited **$1,272,000 common-equity cash in CY1995**, plus the $345,525
   $0.1717 tranche) from the multi-month $1,007,000 program, and must not present $1,007,000 as a
   Stage-1-only raise. Reconcile the two totals explicitly in a `DERIVED` row; do not average them.
   **Arithmetic in my own example here was wrong and is corrected by AUDIT 3 (2026-09-23):**
   3,021,000 × $0.3333 = **$1,006,899.30**, not "≈$1,006,999" as first written. The direction of the
   rounding is also the other way round: $1,007,000 ÷ 3,021,000 = **$0.3333 repeating exactly**, so
   **the aggregate is the precise figure and the printed per-share price is the rounded one.**
   A row that derives $1,007,000 *from* $0.3333 is backwards; cite the aggregate as filed.
4. **$8,000,014 and $200,000 are Series A (1996) and post-boundary** — usable only as consequences.

## COR-11 — merge-time directives from lead-to-lead conflicts

The consolidation leads cross-read each other and raised issues the dossier authors did not. Each is
resolved here so the merge applies it once. (Numbered last but placed here in file order; both this
and COR-10 were appended in the same session.)

1. **`$511K must not be sourced to Sheff.** Dossier F carries the FY1995 net-sales figure with a
   magazine citation. Audited revenue is cited to the original S-1 selected financial data and MD&A
   (and confirmed in S-1/A No. 5). Retier it from 2 to 1 and fix the class from FOUNDER CLAIM to FACT.
2. **151 vs 158 employees** — two figures circulate for 1996-12-31. The original S-1 reads "from 11
   to 151 employees" and "151 full-time employees"; any 158 is from a different document or date and
   must carry its own citation or be dropped from the Stage-1 report entirely (both are
   post-boundary anyway; see COR-03 — **which is SUPERSEDED BY COR-12: apply COR-12, which keeps the
   post-boundary ruling on 151/158/256 but files the "11" at 1995-12-31**).
3. **HistoryLink essay 23230 is tiered and dated inconsistently** across dossiers C, D, F and J.
   It is a **2025-04-07 secondary essay** citing its own sources: tier 2 at best, and any Stage-1
   fact resting on it alone is Medium confidence at most, or is chased to its footnote.
4. **The 1995-10-04 press release has two dates** — indexed 1995-10-03, datelined 10-04. Cite as
   "press release, dated 1995-10-04 (indexed 1995-10-03)" and put the discrepancy in U's minor
   dating list rather than picking silently.
5. **The launch-date triangle is one conflict, not three:** "first four weeks" (PR, 1995-10-04),
   "commenced offering products for sale… in July 1995" with "no sales through July 1995" (S-1),
   and the folkloric "16 July 1995". Section U carries all three with their evidence weights; the
   third has **no primary support** and is listed in COR-09.
6. **The four S-1 page images are not "recovery pending" — they never existed.** Dossier p2's
   section E says images are pending recovery; apply COR-04 and rewrite that clause to state the
   null, with the art-plan captions as the surviving (1997) evidence.
7. **"2,300%" is verified absent from the on-disk S-1** (p2 checked the restored file). Keep it in
   COR-09 and in section H as a founder claim with unestablished provenance.

## COR-09 — figures that must never appear as Stage-1 fact

Carried here so no section accidentally launders them back in:
"2,300%" web growth (absent from the filings; untraced); "July 16, 1995" first sale; the
"$12,000/$14,000 first weeks"; "shipped our first book in August 1995" (absent from all five SEC
documents searched); Wainwright/Hofstadter first-order details (Tier 2, one interview cycle,
contradicts every company statement); "$1.1M from 22 friends and family at $50,000 each"; the
~$5M / 20% valuation; $150,000–$250,000 parental money (the $250,000 traces to a **2018 LA Times
inference**); the Bulgaria floppy-disk order; the "A-for-directory-order" naming story; any
Washington Post stake; any 1995 money-back or security guarantee; "Cadamia" (zero occurrences in
the original S-1, while "Cadabra" is documented by signature); and the 1994 "roadmap"/notebook,
which tops out at **evidence rung 3 — founder description only**, earliest description LA Times
1997-07-20.

## COR-12 — SUPERSEDES COR-03. "11 employees at 1995-12-31" IS filed; my correction over-claimed

AUDIT 2 re-read the employee sentences across all three filing versions and the orchestrator confirmed
it verbatim against `sources/` on 2026-09-23:

| Document | Sentence | Anchor date for "11" |
|---|---|---|
| S-1 (original), 1997-03-24 | *"…from January 1, 1996 to December 31, 1996, the Company expanded from **11 to 151 employees**"* | 1996-01-01 |
| S-1/A No. 5, 1997-05-14 | *"…from **December 31, 1995** to March 31, 1997, the Company expanded from **11 to 256 employees**"* | **1995-12-31** |
| S-1/A No. 3, 1997-05-09 | same construction as No. 5 | 1995-12-31 |

**COR-03's error:** it treated the original S-1's phrasing as the only filed wording and therefore
declared the stage report's "11 employees at 1995-12-31" insufficiently precise. The amendments anchor
that exact count at 1995-12-31, and both statements are consistent — 11 is the headcount at the
1995/1996 turn in every version.

**Corrected rule:** the Stage-1 end snapshot may state **11 employees at 1995-12-31**, cited to S-1/A
No. 3/No. 5. The original S-1's 1996-01-01 phrasing is *added*, not substituted.
The endpoint argument gets stronger, not weaker: the year-end count is now filed on its own date.
**151** (Dec 31, 1996, original) and **256** (Mar 31, 1997, amendments) remain post-boundary and are
different dates — they are not in conflict with each other and must not be reconciled to one number.

> **[ADDED 2026-09-24 — this entry's own wording is corrected, its ruling is not.]** The sentence this
> entry originally carried read: "The original S-1's 1996-01-01 phrasing should be *added* **as
> corroboration**, not substituted." **That instruction is withdrawn and replaced.** It is the standing
> cause of the same-lineage double count that AUDIT 5 raised as A-B1 and that AUDIT 6 confirmed still
> landing: five downstream sites counted the original S-1 as corroborating its own amendments because this
> register instructed them to (`stage_1.md` header and §R Employees; `stage_1.md` §P42; `quantitative.csv`
> L74; `context_appendices.md` §I) — all five demoted on 2026-09-24 by the AUDIT-6 pass.
> Under `00_METHOD_AND_STYLE.md` §3 (filing-lineage rule), the original S-1, S-1/A No. 3, S-1/A No. 5, the
> 424B1 and the exhibits to those accessions are **one instrument** (`sources.csv` S0801–S0804): the
> original's 1996-01-01 phrasing is therefore added as **VERSION EVIDENCE — the first state of the same
> registration statement — and counts as neither a second corroboration nor a second source.** What the
> count rests on is unchanged: S-1/A No. 3 and No. 5 file the 11 at 1995-12-31, and the independence that
> does exist for the population is elsewhere (a release, a periodical, or a differently-originated
> document), never inside this lineage.

> **[A-B1 CLOSURE, 2026-09-24 — AUDIT 6 item 12; limb (a): closed from evidence already on disk, no retrieval
> required.]** A-B1 asserted that copies of one 1997 filing family were being counted as independent
> corroboration, and the ruling was "strike the phrasing, re-key the records". The premise behind the ruling —
> that the original S-1, S-1/A No. 3, S-1/A No. 5, the 424B1 and the FY1997 10-K405 are **one instrument** — is
> now **proved from the cached filings rather than stipulated by project convention**, and the proof is what a
> fresh verifier can re-check: **SEC File No. 333-23795 appears on all five**, and each says in its own words
> that it amends or incorporates that same registration statement.
>
> | Document (under `sources/`) | Its own lineage statement |
> |---|---|
> | S-1 (original), acc. 0000891618-97-001309 | header `SEC FILE NUMBER: 333-23795` l.49; cover "REGISTRATION NO. 333-" l.77 |
> | S-1/A No. 3, acc. 0000891020-97-000755 | `SEC FILE NUMBER: 333-23795` l.49, "REGISTRATION 333-23795" l.79; signature page l.5112 "Amendment No. 3 to the Registration Statement (Form S-1 No. 333-23795)" |
> | S-1/A No. 5, acc. 0000891020-97-000839 | same at l.49 and l.79; `<DESCRIPTION>AMENDMENT NO. 5 TO FORM S-1` l.70; signature page l.5106 in the same form; E&Y consent is its own exhibit EX-23.1 |
> | 424B1 final prospectus, acc. 0000891020-97-000868 | `SEC FILE NUMBER: 333-23795` l.66; cover "Registration Statement No. 333-23795" l.92; retrieval lineage note l.28–32 |
> | FY1997 10-K405, acc. 0000891020-98-000448 | exhibit index, twice: "Incorporated by reference to the Company's Registration Statement on Form S-1 (Registration No. 333-23795)" at l.2913 and l.3105 |
>
> One file number, one registrant, one auditor. **A-B1's execution is complete at the sites AUDIT 6 named plus
> five found by re-running its own phrase sweep** *(the word here read "four" until the AUDIT-7 repair pass of
> 2026-09-25 re-counted the list this sentence itself prints, which holds five items — the five are unchanged, only
> the tally was wrong; correction logged at `03_quality_control/audit7_repairs.md` row R11)*
> (`sources.csv` S0801 and S0803 carried the struck wording
> "gain independence" / "independent corroboration"; the boundary-state row at `stage_1.md` §Stage-boundary,
> and the §B.2 and §D.1 people rows counted the original as corroborating its own amendments). **No claim in
> this corpus is reopened or moved to UNKNOWN by A-B1**, because the ruling changes counts and wording, not
> evidence: confidence levels were verified unmoved. What the attack genuinely needed and did not have until
> now is this citation; `stage_1.md`'s header ruling carries the same proof.

## COR-13 — what the 1995-10-04 press release actually says

AUDIT 2 verified the release line by line. **Present in it:** 50 states, 45+ countries, "first four
weeks", >1M titles, 10–40% discounts, Netscape "What's New", Yahoo "What's Cool", UPS/Airborne,
"Eyes & Editors", the (206) 622-2335 number, the motto, and a Bezos quotation. **Not in it:** nine
mailboxes, toll-free ordering, fax ordering, e-mail ordering — the release says customers order online.

**Attribution rule for §D/§F/§I/§Q:** "nine addresses" and the toll-free line cite the original S-1
(l.2174 and l.2179–2180); fax ordering stays with Knight Ridder, Nov 1995, at Medium. Do not credit the
press release with content it does not contain, including where dossiers D and E already did.

## COR-14 — open items AUDIT 2 raised that are NOT yet adopted

1. **P60/P61 citation error.** Two rows in §P (and their `quantitative.csv` twins) cite S-1/A No. 5 for
   the 151 figure, which belongs to the original S-1. Fix the citation to the original S-1.
2. **Parental money: the "$245,572" claim is unverified.** AUDIT 2 asserted the folk "$250,000 from the
   parents" equals a filings figure of $245,572. A direct search for `245,572` across the original S-1,
   S-1/A No. 5 and the 10-K405 returns **nothing**. Until the document and line are produced, COR-09
   stands as written: $150,000/$250,000 remain untraced and the $250,000 traces to a 2018 LA Times
   inference. **Do not launder the audit's own unsourced number into the report** — the auditor is not
   exempt from the rule it enforces.
3. **One new false-corroboration instance was found inside the appendix** and must be collapsed to a
   single lineage.

## COR-15 — AUDIT 8 residue sweep: the appendix pair was already retracted; the Stage-2 draft was not (2026-09-25)

AUDIT 8 (Stage 1 certification) and `_parts/s3_p4.md` U.168 reported that the retraction of the
`$871,000` / `2,613,000` leg "never reached" `context_appendices.md`. **Read in full, that premise is
stale.** Both appearances — now at l.598 and l.641, not the l.596 / l.639 cited — sit **inside their own
withdrawal sentences**, with the composition of the residual already printed as **UNKNOWN** and the
`$976,408` total already withdrawn along with the leg. Nothing was substituted and no digit was deleted;
the pass **dated and tagged** the appearances instead, so a grep- or copy-out register can no longer read a
withdrawal as an assertion. Corpus test re-run: `2,613,000` and `871,0` occur in **zero** files under
`sources/` (99 entries), while `3,021,000` occurs in 14. The correct value stays **UNKNOWN**, reason: no
document on disk prints that denominator, and the citation offered for it (original S-1 l.4301–4302) prints
`3,021,000 / 23 investors / $.3333 / $1,007,000`.

**The residue that was real is the Stage-2 draft volume** `_parts/s2_p4.md`, which the numbers repair pass
had already logged as "out of scope; reported, not edited" (`amazon_s2_audit3_repairs.md` D-01/D-02, D-06,
D-07, and its sweep table warning that "a rebuild from `_parts` re-imports every defect closed today"). It
now carries a `## SUPERSEDED 2026-09-25` banner plus in-place tags on every copy of: **`$122k` printed as
FY1996 rent** (filed: **$257k**, S-1/A No. 5 l.4383), **`6.4×`** (repaired **6.0×** = 1540 ÷ 257),
**`30.813`** (**30.81409**), **`19.4995`** (**19.50013%**), **`≈39.5`** days (**39.6**, from 39.5690), and
the stale B&N class label `FACT (audited counterparty)`. **No value was rewritten:** per §14 an
intermediate volume is the merge's audit trail and takes a dated supersession marker, never a silent edit.
Sites, before→after counts, sweep commands and the invariant checks (§U 43↔43 Stage 1, 70↔70 Stage 2,
uniform register widths) are in `03_quality_control/audit8_residue_repairs.md`.

**Standing rule from this pass:** an audit reporting a stale figure must say whether the bytes are
*asserted* or *quoted inside a retraction* — a grep cannot tell them apart, and only the first is a defect.
Conversely, a retraction is not finished until it is dated and greppable as a retraction.

---

# Stage 3 hindsight repairs (AUDIT 4) — COR-16 … COR-26, added 2026-09-26

Repairs executed by `s3-hindsight-repair` against `03_quality_control/amazon_s3_audit4_hindsight.md`; the
work log with sweep counts is `03_quality_control/amazon_s3_hindsight_repairs.md`. **These entries supersede;
they do not erase.** The withdrawn words are quoted from the volumes as they stood, and every replacement rests
on the printed document lines given.

## COR-16 — SUPERSEDES the §O.1 "never entered the money" mechanism (Stage 3, H-1)

**Withdrawn (`stage_3_part_2.md` §O.1, *For* leg):** "they were struck at a conversion price that **never
entered the money on any filed 1999 range** (§M.13), so the equity option they sold **never relieved the
debt**." **Relying on:** Form 10-K FY1999 l.1672-1690 (1999 quarterly highs $99.56 / $110.63 / $85.00 /
$113.00, final 12× vintage) against the conversion price **$78.0275** (§K.4, DERIVED `156.055 ÷ 2`) and the
optional-redemption gate **$117.04** (DERIVED `78.0275 × 1.5`, l.1683-1690 terms as filed in §K.4). The strike
was in the money in every 1999 quarter; the **gate** was never reached — the sentence collapsed the two and
inverted the sign, then drew an economic conclusion from the inverted premise. **Replacement:** the issuer could
not compel conversion (the gate governs), while conversion stood at the **holders'** option; the cost the
counterfactual prices is the cash coupon plus the absence of an issuer-side escape. Cross-reference the
`N-5 vs M.13` conflict note at the foot of §N. **No number was substituted or back-solved.**

## COR-17 — SUPERSEDES the "softened admission … before it could be read against the charge" reading (Stage 3, H-2)

**Withdrawn (`stage_3_part_2.md` §M.5 heading and item 2):** "the admission was then **softened**, in the same
corpus, **before it could be read against the charge**"; "a **softened admission**, not a withdrawn one"; and
`stage_3_part_1.md` §G.5 G31 "Two statements of inexperience, **printed weaker each time**".
**Relying on:** Q3-1999 10-Q l.1626-1635, which prints **both** the warning ("we have no previous experience
with automated distribution centers") **and** the fact that in the same nine months the company "**opened
distribution centers in Nevada, Georgia, Kentucky, Kansas and North Dakota**"; against FY1999 10-K l.1026-1027
("we have had **limited experience**"). At the 1999-12-31 count date the November sentence had become literally
false. No counsel file, drafting history or board record exists in `sources/`, so motive is untestable
(audit's own "Untestable" item 5). **Replacement:** both wordings and both dates kept as FACT; the protective
reading carried as **`RETROSPECTIVE INTERPRETATION`, Confidence Low**, with the accuracy-update alternative
stated and `mechanism UNKNOWN`; §G.5 G31 now reads "printed **differently, as the automated estate opened**",
and its stale interval ("relaxes **six weeks later**" — the 10-K was filed 2000-03-23, eighteen weeks after
1999-11-15) now gives both dates. **Siblings carried under this entry, not left standing:** §N row
"December 1998 lease → 1999-03-11" and §O.3 each said "softened to 'limited experience'"; §B estate table
(l.359) and claim record A08 each said "relax[es]/relaxed to 'limited experience'". All four now read
"restated as …" with the motive marked UNKNOWN. **Untouched, and correctly:** G44/U.135's "the dependence
sentence **relaxes its quantifier**" ("any of our vendors" → "most"), §C.1 l.538's "quantifier softened from
'any' to 'most'", and the Stage-2 amendment diffs (`stage_2_part_2.md` l.107, `stage_2_part_3.md` l.104/287/292/1350)
— each of those describes a textual difference between **two filed documents on disk** and asserts no motive.

## COR-18 — SUPERSEDES the mental-state reading of filed risk factors (Stage 3, H-5)

**Withdrawn (`stage_3_part_1.md` §C.2 closing sentence):** "**Read together these are the self-description of a
company mid-build and unsure of the machine, not of a company that had broken through**", and the supporting
claim that risk language is a proxy for "the questions it thought it was facing, because it is dated, filed and
**legally exposed**". **Relying on:** the disclosure class itself — safe-harbour risk factors enumerate worst
cases whether or not they are experienced, so their bias runs **toward** over-stating trouble; the volume's own
rule at §D.1 ("enumerated, not evidenced as experienced, and this file does not upgrade them") and §M.5. **No
in-window document contains a "broken through" benchmark.** **Replacement:** CONTEMPORANEOUS OBSERVATION
confined to "the registrant disclosed X on date Y"; `UNKNOWN` on whether any disclosed risk was experienced;
the filed list itself retained unchanged.

## COR-19 — SUPERSEDES the advertising-to-fulfilment transfer mechanism (Stage 3, M-3)

**Withdrawn (`stage_3_part_2.md` §M.3):** "The ratio fell because the **denominator was pulled up by the
first-party merchandise base while the money actually spent to serve each customer moved out of advertising and
into fulfilment**". **Relying on:** §M.3's own audited series — advertising $3.4m / $21.2m / $60.2m / **$140.9m**
(`140.9 ÷ 60.2 = 2.34×` in 1999) — nothing left the advertising line; fulfilment rose `188.4 ÷ 50.3 = 3.75×`
against net sales 2.7×, so **all three grew at different rates**. "Per each customer" also reintroduced the
per-order basis §K.6 registers as UNKNOWN. **Replacement:** the relative-growth statement, at High, movement
verb deleted.

## COR-20 — SUPERSEDES "the covenant's removal came from bondholders" and the "convertibles" label (Stage 3, M-2)

**Withdrawn (`stage_3_part_2.md` §L row 1998-04-24 → 1998-05-05):** "the removal of that covenant was itself the
validation, **and it came from bondholders**" and "the upsizing happened in a **1998 bull bid for
convertibles**". **Relying on:** 10-Q Q1-1998 l.988-989 — "The Company has **repaid the Senior Loan in full with
a portion of the net proceeds** of the Senior Discount Notes" — and 424B2 l.1355-1357, "the Company used
approximately $75.0 million of such proceeds to retire the Senior Loan". The covenant ended by **repayment**, not
at bondholders' hands; and the 1998 notes were **non-convertible** senior discount notes. **Retained as
inference at §N row 1's grade (Medium):** that the facility was retired to escape the covenant — "inferred from
the ordering of the company's own use-of-proceeds sentence rather than stated".

## COR-21 — SUPERSEDES the §D.0 "no amount" cell (Stage 3, M-4)

**Withdrawn (`stage_3_part_1.md` §D.0, Q4-1999 inventory-charges row):** magnitude cell "**no day, no amount in
that sentence**" with Conf "High (incurred); **UNKNOWN** (size)", where the section contradicted §G.0 row 6,
§M.4, §N-5 and §O.1, all of which use the figure. **Relying on:** Form 10-K FY1999 l.1890-1892 — "inventory-related
charges of approximately **$39 million** incurred in the fourth quarter of 1999". **Replacement:** the sentence is
confined to what it says ("no day and no amount **in that sentence**"), the MD&A amount is cited, and the register
now carries both the charge and its two ratios (`39000 ÷ 290645 = 13.4%`, `39000 ÷ 1639839 = 2.4%`). UNKNOWN
remains — correctly — for the day, the category split, and any causal link to the automated DCs.

## COR-22 — SUPERSEDES the "demand-side" label on a financing row (Stage 3, M-7)

**Withdrawn (`stage_3_part_1.md` §D.0, $1.25bn converts row):** "the **hardest external demand-side signal in
the stage**". Note-buying is a **supply of capital**; "demand" in this stage's own vocabulary is customer demand
(§D.2, §H.3's "NOT KNOWABLE as demand"). **Replacement:** "the hardest external **capital-supply** signal", with
§L's "clearest external **price** signal" named as the form to propagate, so a financing row cannot do the work of
a sales row in the signal ledger.

## COR-23 — SUPERSEDES the cost-of-capital conclusion (Stage 3, M-1)

**Withdrawn (`stage_3_part_1.md` §D.3 closing sentence):** "**The largest signal in this window is that the cost
of capital fell, not that the cost of doing business did.**" **Relying on:** the instruments themselves — 10%
Senior Discount Notes (1998) with **no cash coupon before 2003-11-01**, accreting to $530m face on ~$326m gross
(424B2/8-K, §K.4), against 4¾% **convertible subordinated** notes (1999) whose low cash coupon pays for an
embedded equity option that §M.13/§L say was in the money from the first quarter after closing. Different
ranking, different consideration; no effective yield, secondary price or peer issue of the same week exists in
`sources/`, and §I's provenance boundary confirms no non-Amazon registrant document is present. **Replacement:**
`INFERENCE`, **Confidence Low**, with the market-demand alternative taken from §N's own "window open for US
high-yield convertibles" cell, and **the cost of capital marked UNKNOWN as a measured quantity in this stage**. No
yield was computed, because none is derivable from filed numbers without an option-value assumption the record
does not supply.

## COR-24 — SUPERSEDES the "cheapest available signal" motive wording on the splits (Stage 3, L-2)

**Withdrawn (`stage_3_part_2.md` §L row 1999-02-03, splits):** "**the cheapest available** signal of expected
continued appreciation". No minute or board record survives (§N's evidentiary limit), so the superlative
attributed a choice-motive to an act whose alternatives were never costed. **Replacement:** `INFERENCE`, with the
adjective dropped and the row's own "Low as a validation signal" grading pointed to.

## COR-25 — SUPERSEDES the per-order basis and the "quarterly-comparable" label (Stage 3, H-3)

**Withdrawn:** `stage_3_part_2.md` §M.1 — "i.e. **the cost of delivering an order rose 3.24 percentage points of
revenue** in the single year the network doubled"; and §L row "1998-06-11 / 1998-11-17 → FY1999 MD&A" — "the cost
of serving customers is now an audited-adjacent, **quarterly-comparable** dollar series". **Relying on:** §K.6,
which registers fulfilment cost **per order** as UNKNOWN because "no order count exists in **any** filing in the
window"; the 3.24 points are `11.49 − 8.25`, both computed on **net sales** (`188,400 ÷ 1,639,839`;
`50,300 ÷ 609,819`); and the fulfilment series is printed at three **annual** points out of the FY1999 note
(10-K FY1999 l.1969-1972; `quantitative.csv` rows 325-327), never in a filed 10-Q. **Replacement:** "fulfilment
cost **per dollar of net sales** rose 3.24 percentage points", with a §6 basis note forbidding the per-order
reading, and "a filed annual dollar series at three points … **not** a quarterly series".

## COR-26 — the $178.4m dual printing: which figure is cash is UNKNOWN (Stage 3, H-4 residue)

Form 10-K FY1999 prints **$178.4 million twice, in two different senses**: MD&A l.2282 — "including $178.4
million of **cash paid** to repurchase a portion of our outstanding Senior Discount Notes" — and the debt note
l.3686-3688 — "the Company repurchased **$266 million (principal amount)** of the Senior Discount Notes,
representing **accreted value of $178.4 million**", with "the remaining principal amount outstanding … **$190.7
million**". Both cannot be exact, and the filing does not reconcile them. The narrative's existing phrasing
("$178.4m of **cash** paid") is the MD&A's own words and is **not** withdrawn, but it is now registered with its
alternative printing, and **which figure is the cash outlay is recorded as UNKNOWN**. Not back-solved. Separately
registered: `530,000 − 266,000 = 264,000` against the $190.7m the note says remains, unexplained at the cited
lines → **left as a §U candidate for the certifier**, since the reconciling items (conversions, exchanges) are
not in the lines read.


## COR-16 — SUPERSEDES §U.113a's CLAIM B AS MINTED (2026-09-26, Stage-2 blocker-repair pass, AUDIT 6 B1–B8)

**The instruction this register gives every later pass: the 1997-03-24 S-1 original states NO IPO price range. Do not
"correct" any narrative that says the range field was blank.** `stage_2_part_3.md` §U.113a (minted 2026-09-26, RD-079)
asserted the original "states a range and an assumption in one breath", quoting "…will be between …" with an ellipsis.
The document (`sources/S-1_original_acc-0000891618-97-001309_filed-1997-03-24.txt` **l.208–209**) prints "**between /
$     and $     per share**" — the two price fields are **unfilled on the face of the filing**. The elided bytes were the
refutation, so the quotation failed the test it was offered to satisfy (method §14 rule 8). `conflicts.csv` **U.113a**
carried the same false proposition, and **a repair added the defect while removing one**.

**What is true, each line re-read at the keyed file:** original 1997-03-24 = blank range field (l.208–209) beside a
$13.00 registration-fee assumption (l.166; 2,875,000 × 13.00 = $37,375,000 exact) and a $13.00 pro-forma dilution
assumption (l.1221) → **No. 1, 1997-04-21 = first accession to state a range**, "$12.00 and $14.00 per share" (l.247–248),
in the same document whose fee table already prints $14.00 (l.192) while its pro-forma still runs $13.00 (l.1365) → No. 2
(1997-04-29) repeats it → No. 3 (1997-05-09) re-prints it unchanged (l.222–223) with the $14.00 cover (l.173) and
"$13.00 per share" still in its pro-forma/capitalization sections (l.408, l.1188, l.1230, l.1290, l.1300) → No. 4
(1997-05-13) raises range and size → 424B1 (1997-05-15) prints $18.00. **$13.00 and $14.00 are assumptions, never
prices.** `stage_2_part_1.md` §A.3's "blank (24 Mar, S-1 orig.) → $12.00–$14.00 … (No. 1, 21 Apr)" and
`amazon_s2_audit4_repairs.md` §4 item 2 are **correct and stand unamended**.

**Action for every later pass.**
1. **Re-keyed pointers.** Cite keyed lines: **l.208 / l.166 / l.1221** for the original (the minted l.191 / l.149 / l.1204
   are **twin** numbers of the unheadered duplicate — `twin = keyed − 17`, declared in `stage_2_index.md`). AUDIT 6's
   fourth pointer challenge is **not** adopted: No. 3's "$13.00 per share" **is** at **l.1230**, so three cites were
   inverted, not four.
2. **New pointer defect found by this pass and fixed in the narrative:** FY1998 10-K's restated loss-per-share line is
   **l.1244**, not the l.1243 that §U.113b and `conflicts.csv` U.113b cited — l.1243 is the totals rule and prints no
   digits. Rewritten U.113b row handed to the register owner.
3. **Residues closed in Stage-2 text:** `0.194995` → **0.1950013** at `stage_2_part_2.md` §P.2 s4 and record P26 (B2);
   "the filed figures give 2,448,000 …" → "**transcribed** numerator over **filed** denominators" in the U.67 record
   (B3); the unbounded "cheapest capital the firm ever raised" bounded to 1997-05-15 in record K19 (B5); the missing
   authorised-capital record minted as **B125** (B8 / RD-049 — **not** RD-072, which is the Stage-3 13G supersession).
4. **B6 is a gate artifact, not a row defect.** `conflicts.csv` rows 135/170/171 parse at **15 fields** under RFC-4180;
   the reported 16/18/17 reproduce exactly under the retired `doublequote=False` dialect-sniffing reader, which
   `tools/gates.py` has since removed. Do not "repair" the widths; the U.113a row is rewritten for its **content** (the
   false claim, its twin pointers, and a §13 date column holding prose), which is handed off un-applied.
5. **Register rows this pass does not touch** (live owner): `conflicts.csv` U.113a, U.113b; `sources.csv` **S2009**
   (`FACT (audited counterparty)` + `High` on a line that also says `local_copy: NO` → lowered to
   FACT (existence) / UNKNOWN (contents) + Low, and its `relevant_passage` marked not-verifiable — the same
   quote-without-a-document family as B1). Exact replacement rows: `03_quality_control/amazon_s2_blocker_repairs.md`.
6. **Handed off, not fixed here** (Stage 3's files, live owner): the false quotient is inherited at `quantitative.csv`
   L339 and `stage_3_part_3.md` §P188 / §P.2 t1.

**Standing rule from this pass:** a quotation is not evidence until the bytes behind any ellipsis have been read, and a
correction authored by an agent is a claim by that agent — it gets tested against the document before it is written into
the narrative, the register, or a log line that the next agent will read as an instruction (§14 rules 8 and 10).
