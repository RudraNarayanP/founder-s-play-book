# stage_1.md — company_017_meta — STAGE 1 (origin → first real-world experiment → repeatable validation → scalable company formation)

**MERGED 2026-10-07 by `merge-meta` from `_parts/s1_p1.md` (agent `s1-meta-p1`, 25,200 words, §Header–§J, 33 claim
records `P1-01…P1-33`, 99 register rows, declared anchors `U.1–U.7`) and `_parts/s1_p2.md` (agent `s1-meta-p2`,
9,721 words, §K–§U, 17 claim records, 43 register rows, declared anchors `U.1–U.8`).** Combined emission:
**34,921 words**. One volume, published below in full and in both parts' own section letters: nothing was split,
nothing was trimmed, and no anchor, section letter, claim id or register key was renumbered (merge wave rule,
`00_universe/_AUTHOR_WAVE_PLAN.md`: p2 adopted p1's taxonomy verbatim, so the merge takes the **union** `U.1–U.8`
and proves parity once).

**The nine registers are live at the company root** (`sources.csv` … `data_gaps.csv`, **120 applied rows**), and
the register blocks the parts emitted are **not reprinted here** — `_parts/` stays the emission of record and a
second copy would read to `tools/merge_census.py` as new rows. Each stripped block leaves a pointer line naming
its row count. The application account, the fold list, the local-tag→minted-id map and the census readings before
and after are at the foot of this file, and in `03_quality_control/meta_s1_merge.md`.

**Tier — written to T2, the probe's measured verdict, not to the dispatch's label.**
`research/A_chronology_feasibility.md` measures **T2 core: 2 of the 5 corpus families returned in-window Tier-1
text** — (a) filings yes, legal records yes at register level, (b) web archives **UNANSWERED** (CDX refused 504 /
503, "Internet Archive services are temporarily offline"), (c) periodicals no in-window text, (d) corporate print
**UNQUERIED** (consecutive-failure breaker), (e) auction/museum **UNTRIED**. The dispatch table labelled this
company **T1**, and `tools/gates.py --tier auto` read that label off the dossier and stamped **T1**; that is a
**dispatch-label error, recorded here and not smoothed** (the same correction the wave plan carries for Dell:
*the probe's measured tier governs, not the label*). Both authors wrote at T1 *section density* while reporting the
measured 2 of 5, and this merge did the same: **the register and the manifest are written to T2 and the dossier
remains the authority.** The volume's 34,921-word emission exceeds the T2 tier target (22,000 words) and sits well
under the §9.2 hard cap (60,000): the overage is logged as **advisory**, which is what §9.2 makes it, and it is
**not** evidence to delete. Two cheap re-runs (Wayback CDX once archive.org answers; RECAP/PACER docket text for
`1:04-cv-11923`) would make the tier genuinely T1 — the probe says so, and both are FETCH REQUESTs below.

**Window — two readings, both preserved, and the merge's staging call registered rather than silently made.** The
dispatched dossier window is **2003-01-01 → 2012-12-31** (`sources/sec/_RUN.json`,
`research/A4_harvest_mine.md` l.3: "deliberately WIDE where the founding date is itself unestablished"); the
probe proposes Stage 1 **closing at the July-2004 incorporation**. Part 1 wrote to the dispatched window, part 2
built §K–§R against the July-2004 close, and the divergence is a conflict, **U.7**, not a measurement error. This
merge keeps the dispatched window for this volume, keeps every part-2 section labelled with the close it was
written against, and records the re-homing of the 2005–2012 material between Stage 1 and Stage 2 as an open
staging decision for the cross-company pass — see U.7's `best_supported_interpretation`. **Both divergences (tier
label, window) are preserved on the record; neither was smoothed to make the volume read consistently.**

**What this dossier does not contain:** no certification (a merge may not certify), no audit, no new evidence
route attempted — this pass read only held bytes and the two part files, made **0 web calls**, and wrote nothing
into `sources/`.

## The seven findings the merge carried intact (each is a byte-level find, not a restatement)

1. **The founding day IS in EDGAR** — the probe's "no EDGAR document can ever fix the founding day" is **refuted**:
   Ex-3.3 of accession 0001193125-12-175673 (S-1/A, filed 2012-04-23, fetched 2026-09-29) recites *"The date of
   filing its original Certificate of Incorporation with the Secretary of State was July 29, 2004, under the name
   TheFacebook, Inc."* It is an **unexecuted form** (`Dated:` and signature block blank), so the day travels at
   **Medium** and **Delaware remains the upgrade route** (F-2). `S4497`, `U.1`, `P1-03`/`P1-18`.
2. **"A college dorm room in 2004" is in the filing text at year level only.** `February 2004` = **0 hits**; the
   place is in the Business section of 12 stored lineage documents in one unchanged sentence (`dorm` = 1 hit in
   each), and that is **version evidence, not corroboration**. Launch stays **UNKNOWN**, and withdrawing February
   licenses no substitute. `U.5`.
3. **`Saverin` appears exactly once in the whole SEC corpus** — in Ex-10.16A (`S4499`) as the defined title *"the
   Saverin Agreement"* in the Mail.ru/DST conversion amendment, never described. Not a founder, not a litigant,
   and the probe's blanket "Saverin 0" holds only for the S-1 and the 424B4. `U.4`.
4. **`thirty days` = 1 hit, and it is an option window** — the 2005 Stock Plan (`S4498`); `30 days` = 71 in raw
   bytes (73 after tag-and-entity stripping, 19 documents), all MAU definition, equity mechanics and boilerplate.
   **The growth claim therefore has no carrier and gets no substitute number.** `U.6`.
5. **`Meta Platforms, Inc.` exists in this corpus only in EDGAR's `former_names` field, undated here.** The 2021
   renaming is a different act of a differently named person and no stored document dates it; it stays UNKNOWN
   inside Stage 1 and no modern literal is allowed to date a 2004 instrument. `S4501`, `data_gaps.csv` row 9.
6. **Provenance drift, reported not repaired.** The stored S-1 body is **2,657,075 B / sha1 `d749855a…`** on disk
   (mtime 2026-10-07) while its own sidecar and `_MANIFEST.csv` record **2,627,682 B / sha1 `bf14d107…` / fetched
   2026-09-29T19:05:37Z**; the 424B4's sidecar does match (`f7fa2eb2…`). The merge re-measured both hashes,
   published the fact in `_MANIFEST.md` and in a `validation.csv` row, and **rewrote neither the sidecar nor the
   bytes** — choosing to preserve the mismatch is the point: reshaping either side to make the records agree would
   destroy the only evidence that the drift exists. What every quotation in this dossier rests on is the **current
   bytes at the path**, which is what §14 rule 11 requires.
7. **The `845 million` MAU row is verified at last.** Part 1 carried it "not re-read by this pass — the merge must
   re-verify"; part 2 declared it absent from the held S-1. Both were answerable only from the bytes: the S-1
   prints `845&nbsp;million` **eleven times** — *"We had 845 million MAUs as of December 31, 2011, an increase of
   39% as compared to 608 million MAUs as of December 31, 2010"* — so a literal grep returns 0 and part 2's
   correction is a rendering artifact of exactly the class part 1 flagged for `July&nbsp;29,&nbsp;2004`. Verified;
   confidence **stays Medium** (one company-internal count, one registration lineage, a 2011 restatement).

## `company` literal convention (register column; prose untouched)

Part 1 wrote `Facebook Inc.` on all 99 rows, part 2 wrote `Meta` on all 43. Normalised **carrier-faithfully, per
row, to the registrant as the cited document prints it**: `Facebook, Inc.` on every row whose carrier is the 2012
registration lineage, a filed exhibit of it, a 2004–2008 federal docket caption, or any event dated 2003–2012;
`Meta Platforms, Inc.` on the **one** row whose cited carrier is that record itself — `data_gaps.csv` row 9, the
undated renaming. Its carrier is `sources.csv` **S4501**, the EDGAR registrant record, which has no `company`
column at all. **Bare `Meta` is used on no row.** The 2005 `REGDEX` rows
keep `Facebook, Inc.` with attribution **UNKNOWN**, because labelling them `Meta Platforms, Inc.` would write into
a register the very attribution **U.3** forbids. The parts' prose is published as written.

## Anchor ↔ register parity (before and after de-duplication)

* **Before:** 15 `conflicts.csv` rows emitted against 8 declared anchor ids — p1's 7 (`U.1–U.7`) plus p2's 8
  (`U.1–U.8`) = **7 duplicate primary keys**, which the `csv` key gate fails.
* **After:** **8 rows, `U.1–U.8`, one row per subject**, against **8 narrative anchors** (`### U.1 … ### U.8` in
  §U, part 2's body, unrenumbered). Parity is 8 ↔ 8; every `§U.n` cross-reference inside part 1's §A–§J resolves.
* Part 1's rows are canonical for `U.1–U.7` (part 2 never opened Ex-3.3: 0 occurrences of `TheFacebook` or
  `July 29, 2004` in its reads); part 2's sentences are folded into them with attribution and part 2's
  superseded claims are printed inside the same cells as superseded, not deleted. `U.8` is part 2's alone.


---

# PART 1 BODY — `_parts/s1_p1.md`, applied to this volume verbatim (§Header, §boundary, §A–§J, registers pointer, `## Untried`, F-1…F-5). Section letters, claim ids and anchors are the author's and were not renumbered.


## Header

STATUS: WRITTEN 2026-10-06 (agent `s1-meta-p1`; every passage quoted in this volume was opened from bytes
under `company_017_meta/sources/` in this session, and every count was re-measured here rather than inherited)

<!-- ANCHORS: U.1-U.8 -->

### Dataset, stage, and how to read this volume

*One document split for the file cap (method §9.3). Section letters, claim IDs, metric IDs and conflict
numbering run continuously across volumes: **§Header, §Boundary and §A–§J live here (`_parts/s1_p1.md`);
§K–§U and the claim-record appendix are owed by `_parts/s1_p2.md`.** Cross-references of the form
`(Meta S1 §D.4, part_1)` name the volume. Nothing is renumbered to make a part look self-contained.*

**Dataset:** The Founder's Playbook — forensic reconstruction of what each company in the frozen universe
(`00_universe/`) looked like while its outcome was still unknown.

**Company (rank 17).** The registrant that carries this history today is **Meta Platforms, Inc.**, CIK
0001326801. EDGAR's own registrant record for that CIK prints `"registrant": "Meta Platforms, Inc."`,
`"ticker": ["META"]`, `"former_names": ["Facebook Inc"]` and indexes **4,194 filings** for it
(`sources/_index/_registrant_CIK0001326801.json`, built 2026-09-29). The Stage-1 subject is **not** that
name: it is the Delaware corporation whose original certificate of incorporation was filed **July 29, 2004
under the name TheFacebook, Inc.** (§Boundary 1). The 2021 renaming to Meta Platforms is a **different act of
a different-named person** and carries **no date inside this corpus** — every stored document in the
Stage-1 window is filed by or about Facebook, Inc. (§Boundary 1, table row 6; `## Untried` route 1).

**Stage:** 1 of 3.

**Span (the dossier window, re-stated with its carriers as the dispatch requires).**
**2003-01-01 → 2012-12-31**, with **2004-07-29 inside it as the only day-level Tier-1 date for the entity**
and **February 2004, the dorm launch, and the first customer outside it as UNKNOWN** (§Boundary 2). Two
scripted carriers fix the window, not the brief alone: `sources/sec/_RUN.json` prints
`"window": "2003-01-01..2012-12-31"` as the intake window actually applied, and
`research/A4_harvest_mine.md` line 3 prints the same window with its reason — "deliberately WIDE where the
founding date is itself unestablished — narrowing it here would silently discard the evidence that could
establish it". **The probe's proposed Stage-1 terminus is July 2004, not 2012**
(`research/A_chronology_feasibility.md`, "Boundaries": Stage 1 = *earliest attested point → July 2004*;
Stage 2 = July 2004 → 2012-02-01). This volume therefore works to **one window and two boundaries**: the
dossier window 2003→2012 as dispatched, and inside it the stage-defining act — the formation of the entity —
at 2004-07-29. Anything the merge reads as Stage-2 territory on the probe's architecture is labelled
`RESTATED` or dated, and the divergence itself is registered as a conflict (**U.7**) rather than smoothed.

**Stage definition:** origin → first real-world experiment → repeatable validation → scalable company
formation. For a consumer-technology network (§7 adaptation rule; the spec's frame is
adoption/retention/platform dependence) the four beats are *the founding instrument, the first working
product, the first measured adoption, and the first outside capital*. On this corpus only the first and the
last are documented, and both only at the company's own word: **the second beat has no carrier at all**
(§D), which is the single most important thing to say about Stage 1 for this company.

**File:** part 1 of 2 for Stage 1. p1 = Header / Boundary / §A–§J + the register append blocks emitted for
those sections; p2 = §K–§U + the claim-record appendix.

**Tier, stated as found.** The probe's measured verdict is **T2 core** — 2 of 5 corpus families returned
in-window Tier-1 text, and the shortfall is traceable to one archive.org outage plus one
consecutive-failure breaker, not to missing evidence. This pass re-checked all four non-filings families in
their held bytes and did not change that count (§Boundary 3). The dispatch calls this company a **T1
exemplar**. I have written at T1 section density (§A–§J in full, registers, claim records) because §15.2's
T1 deliverable is the shape the dispatch ordered, **but the family verdict is reported as the probe measured
it and is not upgraded by this volume.** The disagreement is recorded in
`_parts/NOTES_meta_p1.md`, not resolved silently.

**Hindsight firewall (§2).** Nothing here treats the 2012 listing, the 901 million MAUs, or the eventual
name change as evidence that the 2004 formation was rational, that the dorm story was the origin of a
company rather than of a product, or that the social-networking market was ever obviously huge. The
anti-hagiography test was applied to every coda in this volume: each is written so that it would still read
as plausible if the firm had failed in 2009. The words "visionary", "genius" and "inevitable" do not occur
here. The registrant's own origin sentence — "Facebook has grown from our beginnings in a college dorm room
in 2004…" — is quoted only as evidence of **what the company chose to print in February and May 2012**, and
is classified FOUNDER CLAIM about 2004 at every one of its appearances (§C, §D).

**Record-selection null (§2, RD-032).** Unrecoverable *because the survivor's archive is the one that was
kept*: for the founding year itself there is **no company document of any kind in this corpus** — not one
page of the product, not one screenshot, not one letter, not one count. What survives is (i) the company's
2012 recital of its own 2004 act, (ii) a federal docket register that dates other people's lawsuits against
Mr Zuckerberg, and (iii) exhibits that had to be filed to register an offering. Gone and unrecoverable at
this reach: any contemporaneous record of the launch, the first user counts, the first advertiser, the first
server, the rejected alternatives, and **any independent count behind any company self-report** — every
user figure in the window is "calculated using internal company data", the prospectus says so in its own
words (§H). The measured consequence is §Boundary 3: the earliest byte of EDGAR activity on this CIK is
2005-05-06, and even that is unattributed.

**Confidence scale (§3).** **High** = a primary document for its own year, or 2+ independent origins;
**Medium** = one reliable source, or a retrospective-only primary; **Low** = conflicting, vague, or
retrospective-only with no primary carrier; **UNKNOWN** = a finding, never a gap to be filled or smoothed.

**The single-lineage rule, stated once and enforced on every row (§3).** The whole in-window Tier-1 corpus
of this company is **one registration lineage**: S-1 of 2012-02-01 (accession 0001193125-12-034517), its
eight amendments of 2012-02-08 → 2012-05-15, the 424B4 of 2012-05-18 (which *is* that registration statement
printed final), the FY2012 10-K of 2013-02-01, and the exhibits filed inside those accessions. Thirty-one
documents are stored (50,285,422 B / 1,901,418 words per `_RUN.json`) and they are **one witness, not
thirty-one**. Counting the S-1, an S-1/A and the 424B4 as three corroborations is the error this rule exists
to stop. Repetition across drafts is **version evidence** — it shows what the company changed, or refused to
change, under staff comment; it proves nothing independently true. Measured version evidence used in this
volume: the word `dorm` occurs **exactly once in each of the 12 stored lineage documents that contain it**,
in one unchanged sentence, and `TheFacebook` occurs in **exactly one** of the 31 stored documents (§B.4,
§Boundary 5).

**ID scheme (§13, read before citing).** `P1-xx` claim records and `P1Sxx`/`P1Qxx`/`P1Txx`/`P1Dxx`/`P1Vxx`/
`P1Fx`/`P1Cx`/`P1Kxx`/`P1Gxx` register rows are **dossier-local**. Global `source_id` blocks are minted
centrally at merge (`tools/id_mint.py`); nothing here assumes one. `**U.1**–**U.7**` are the §U anchors
this volume declares for the seven conflicts it registers; §U itself is owed by part 2, which must fold or
renumber them and continue from `` `U.8` `` and upward. `research/A_chronology_feasibility.md` and
`research/A4_harvest_mine.md` are prior passes' dossiers, cited as dossiers and **never counted as a second
source**; where this pass re-measured one of their statements and got a different answer, the correction is
named in §Boundary 6 and no old number is carried forward silently.

## boundary

STATUS: WRITTEN 2026-10-06

**Geometry note.** This section enumerates the candidate subjects and dates, names the held document behind
each, and says why each rival **fails**. It does not assert a boundary and then defend it rhetorically. The
dispatch's own instruction is the shape this section takes: **the 2004 formation and the first working
product are different acts and must be separated by carrier** — so the formation is dated from a constitutive
recital, the product is left undated because nothing dates it, and the gap between them is reported as a
finding rather than filled with the famous month.

### 1. The entity question: which legal person, under which name, on which date

| # | Instrument as printed in held bytes | Dated | What it establishes | Stage-1 status |
|---|---|---|---|---|
| 1 | Ex-3.3 "FORM OF RESTATED CERTIFICATE OF INCORPORATION OF REGISTRANT … Facebook, Inc., a Delaware corporation, hereby certifies as follows. 1. The name of the corporation is Facebook, Inc. **The date of filing its original Certificate of Incorporation with the Secretary of State was July 29, 2004, under the name TheFacebook, Inc.**" | filed **2012-04-23** with S-1/A (acc. 0001193125-12-175673); the form's own `Dated:` line and signature block are **blank** | the **only day-level formation date in the corpus**, and the **original corporate name**, both stated by the company in a filing; the entity was formed **as TheFacebook, Inc.** and restated **as Facebook, Inc.** | **THE STAGE-1 SUBJECT'S FOUNDING ACT — company-asserted, filed, unexecuted in the form as held. Confidences capped accordingly (§B.4, U.1).** |
| 2 | S-1/424B4 "Corporate Information": "We were incorporated in Delaware in July 2004." + audited Note 1 "Organization and Description of Business — Facebook was incorporated in Delaware in July 2004." | S-1 filed 2012-02-01; 424B4 2012-05-18 | the month-level incorporation, stated twice inside one lineage in two different sections (Corporate Information and the audited notes) | corroborates row 1 at month level **only within the same lineage** — not an independent witness (§3) |
| 3 | Business overview: "We were incorporated in July 2004 and are headquartered in Menlo Park, California." | 2012-02-01 → 2012-05-18 | the registrant's own statement of its formation month and its HQ at filing | FACT about the 2012 printing; registrant-retrospective about 2004 |
| 4 | Court register: "**The Facebook, Inc.** v. Connectu, Inc", 5:07-cv-01389, N.D. Cal., `dateFiled` 2007-03-09; "Connectu, Inc. v. **Facebook, Inc.**", 1:07-cv-10593, D. Mass., 2007-03-28 (`sources/legal/cl2_%22ConnectU%22.json`) | 2007-03-09 / 2007-03-28 | a **third-party-generated register** printing the articular name "The Facebook, Inc." in a caption two-and-a-half years after formation, and "Facebook, Inc." in the same month | independent evidence that a person of that name was suing and being sued **by 2007-03**; **not** evidence of a formation date, and caption spelling in a mirror database is not a charter |
| 5 | Registrant record: `"registrant": "Meta Platforms, Inc."`, `"former_names": ["Facebook Inc"]`, `"count": 4194` | built 2026-09-29 | EDGAR itself says the CIK that filed as Facebook Inc is the CIK now named Meta Platforms, Inc. — **one continuous registrant, two names** | the **only** carrier in the corpus for the later renaming, and it carries **no date**. The 2021 act is UNKNOWN here (§Boundary 2 rival 6) |
| 6 | Nothing. | — | `Facemash` **0** hits, `PhotoManual` / `Photo Manual` **0** hits, `thefacebook` **0** hits except row 1's `TheFacebook`, `Harvard College` **0** hits, `February 2004` **0** hits, `dropout` not read — measured across all 31 stored SEC documents and the 7 stored periodical text files | the pre-corporate person's alleged school projects are **not in this corpus at all**: **UNANSWERED by every family, not answered as absent** (§D.3, `## Untried`) |

**Rule applied on every line below.** "The company" means **TheFacebook, Inc./Facebook, Inc., a Delaware
corporation**, from 2004-07-29 onward. Anything before that date belongs to **Mr Zuckerberg personally or to
no one**, and this volume says so wherever it reaches the temptation to write it otherwise — the Ceglia
matter is the test case: the prospectus itself pleads an agreement "allegedly entered into in April 2003",
i.e. **before any Delaware person existed**, and it is the *adversary's* claim, printed by the company in
quotes and characterised as "purported" and "supposed". Pre-formation activity stays attached to the person,
not to the registrant (**U.2**). This is the anachronism §6 exists to prevent, and it is the defect this
project has already paid for at Morgan Stanley, Cigna, AT&T, Marathon, Ford, Citigroup, Verizon, Kroger,
Boeing, ExxonMobil and BofA.

### 2. Candidate Stage-1 windows and why each rival fails

| # | Candidate open/close | Best held document | Verdict |
|---|---|---|---|
| 1 | **2004-07-29 → 2012-12-31** | Ex-3.3 recital (row 1 above); window carrier `_RUN.json` | **REJECTED AS THE OPEN** — and it is not for lack of a date. A boundary that opens at the *filing of the charter* discards the stage's own first three beats (origin, problem, first experiment), which is where all the interesting evidence *would* be if it existed. Adopted instead as **the date of the constitutive act inside the window**, not the window's floor. |
| 2 | **February 2004** (the dorm launch) → 2012 | none | **REJECTED — unestablishable at this reach, and it is the most folklore-loaded date in the company's story.** No document in the corpus prints "February 2004"; the only dated thing in the filings is July 2004 (month) and July 29, 2004 (day, in an unexecuted form). Recorded as UNKNOWN (**P1G01**), with the two routes that could fix it named (§Boundary 4). A retraction does **not** become a substitute number: withdrawing February buys nothing, and July is not "the launch". |
| 3 | **April 2003** (Ceglia's alleged contract) → 2012 | 424B4 Legal Proceedings, verbatim: "Paul D. Ceglia filed suit against us and Mark Zuckerberg on or about June 30, 2010, in the Supreme Court of the State of New York for the County of Allegheny claiming substantial ownership of our company based on a purported contract between Mr. Ceglia and Mr. Zuckerberg allegedly entered into in April 2003." | **REJECTED as the stage's origin.** It is an adversary's pleaded allegation reproduced inside the company's own filing, dated to a person, not to a corporation, and the probe already adjudicated it as *pleaded, not established* (**U.2**). **Admitted for one purpose only:** it is a Tier-1 register reason why the evidence window must open in 2003 rather than 2004 (§Header, Span). |
| 4 | **2005-05-06** (first EDGAR activity on the CIK) → 2012 | `sources/_index/submissions_pre2014.csv` row 1: `2005-05-06, REGDEX, 9999999997-05-023236` | **REJECTED.** Five `REGDEX`, two `REGDEX/A` (2005-05-06 → 2006-07-10) and one `NO ACT` (2008-10-14) sit on this CIK before the S-1 and **their attribution is UNKNOWN**: no document read by this pass or by the probe says which entity they belong to. The probe's instruction is carried forward as a standing prohibition — *do not let "Facebook registered in 2005" enter any register* (**U.3**). |
| 5 | **2004-09-02** (the first independent date) → 2012 | CourtListener register: ConnectU LLC v. Zuckerberg, 1:04-cv-11923, D. Mass., `dateFiled` 2004-09-02, "190 Contract: Other; 28:1332 Diversity-Breach of Contract" | **REJECTED as the open, adopted as the floor's witness.** It is the earliest *externally generated, machine-dated* record naming Zuckerberg as a defendant over company ownership, and it is a **terminus ante quem**: something disputable about ownership had already happened by 2004-09-02. It cannot date the thing it presumes. |
| 6 | **2003-01-01 → 2012-12-31** with the formation act at 2004-07-29 inside it | `_RUN.json` window field; `A4_harvest_mine.md` window line; Ex-3.3 recital; Ceglia's alleged April-2003 contract | **ADOPTED.** The window is a *reach* decision with two scripted carriers and one pleading-level reason (the earliest allegation in any Tier-1 document is dated 2003); the boundary is an *evidentiary* decision with one carrier (Ex-3.3). Holding the two apart is what keeps the dorm story from being dated by a charter and the charter from being dated by the dorm story. |
| 7 | close at **2012-02-01** (the S-1) or **2012-05-18** (the 424B4) | index rows for acc. 034517 and 240111 | **REJECTED for Stage 1 — and it is a live architecture conflict, not a solved one.** The probe assigns both dates to *Stage 2's end* and *Stage 3*. This volume writes §A–§J against the dispatched window and registers the divergence as **U.7** so the merge decides, rather than this pass re-staging the company on its own authority. |

### 3. Where the record physically stops — measured this session, not inherited

| Family | This pass's read of the held bytes | Verdict as found |
|---|---|---|
| (a) filings | 31 stored documents / 50,285,422 B / 1,901,418 words (`_RUN.json`, `built` 2026-09-29T19:06:04Z, `attempted` 31, `stored` 30 + `_UNANSWERED.csv` 1 + `_SKIPPED.csv` 0); index enumeration `submissions_pre2014.csv` = **397 rows with filingDate ≤ 2013-12-31**, oldest **2005-05-06**, and a **complete gap 2008-10-14 → 2012-02-01** | **THE ONLY FAMILY WITH IN-WINDOW TIER-1 TEXT.** Its floor is 2005-05-06 for activity and 2012-02-01 for narrative; every word it says about 2003-2004 is a 2012 statement about 2003-2004 |
| — legal records | `sources/legal/cl2_%22ConnectU%22.json` `count` 670 / `document_count` 4204; ten dockets read out of it with `dateFiled` values, incl. **2004-09-02**, 2006-10-26, 2007-02-21 ×4, 2007-03-09, 2007-03-28, 2007-05-22 and **Leader Technologies Inc. v. Facebook Inc., 1:08-cv-00862, D. Del., 2008-11-19** | **REGISTER-LEVEL TIER 1, IN-WINDOW, INDEPENDENT.** Pleadings not fetched: the register dates events, it does not narrate them. (The probe listed six in-window matters; this pass reads **seven** from the same payload — §Boundary 6, COR-4) |
| (b) web archives | three negative artifacts held: `cdx_thefacebook.com.txt` (160 B, "504 Gateway Time-out"), `cdx_facebook.com.txt` (11,832 B, "Internet Archive services are temporarily offline"), `cdx_thefacebook_retry.txt` (11,832 B, same). **Zero timestamps returned; zero capture dates exist** | **UNANSWERED — not a null.** The single fact the whole product beat needs (the first captured page of thefacebook.com) is one CDX call away once the service answers (`## FETCH REQUEST` F-1) |
| (c) periodical corpora | `_harvest/candidates.csv` = **30 rows**; `chronicling_america` 3 rows with blank item ids (403); `hathitrust` 2 rows (http_status 0); `google_books` 22 rows **metadata-only**, of which **exactly one is in the 2004-2006 press window** (`The New Yorker`, id `HsrjAAAAMAAJ`, date field "2006") | **NO IN-WINDOW TIER-1 TEXT.** A digitised volume existing is not a passage; the `TIER1_CANDIDATE` flag is mechanical and was not treated as evidence |
| (d) digitised corporate print | `corporate_print` 1 row and `internet_archive` 2 rows, all blank, `http_status` empty — skipped by the consecutive-failure breaker | **UNQUERIED, NOT ANSWERED.** The sentence "Facebook pre-IPO printed material exists only in private hands" remains unlicensed |
| (e) auction / museum | no request of any kind in `sources/` | **UNTRIED** — the one family whose skip cannot be blamed on an outage |
| — periodicals actually stored | 7 text files (`arxiv-*`, `DTIC_*`, `NASA_NTRS_*`), 2009-2012 | **BARE_WORD_MATCH only, per `A4_harvest_mine.md`**: they are about Facebook *as a platform* (a Zynga-adjacent research corpus, a 2011 "Anatomy of the Facebook Social Graph" paper), and **not one names the registrant's origin**. Citable as pointers, never as evidence, never counted in a tier verdict |

**Counted honestly: 2 of 5 families returned in-window Tier-1 text** (filings; and legal at register level).
That is the probe's arithmetic and this pass found no route to a third. The gap is one external outage plus
one breaker, exactly as the probe says, and **the two re-runs the probe names would change the tier** —
which is why this file emits fetch requests instead of pretending the corpus is deeper than it is.

### 4. The two routes that could date the launch, stated as routes

Neither is a guess about content; both are named because a null must be earned and the remedy identified.
**(i) Delaware Division of Corporations** — a certified copy of the original certificate filed 2004-07-29
under the name TheFacebook, Inc. would replace Ex-3.3's *recital* of the date with the *record* of it, and
would print the authorized-share structure at formation. The S-1 accession itself contains **no charter
exhibit** (its file list carries one exhibit, `d287954dex231.htm`, an auditor consent, and 26 `g287954g*.jpg`
figures per the probe's enumeration of `sources/_index/S1_accession_filelist.txt`) — **but that is now a
narrower statement than the probe drew from it**: a later amendment in the same chain does carry a form of
restated certificate with the day-level recital (§Boundary 6, COR-1). **(ii) Wayback CDX for
thefacebook.com** — one call returns the first capture timestamp, which is the only route in the world that
could show what the product looked like on the day it went up. The family is UNANSWERED, not empty.

### 5. CONTEMPORANEOUS / RESTATED test, run on the held bytes

Every origin statement in this corpus is **RESTATED / registrant-retrospective**: printed in 2012 about
2004-2005, inside one registration lineage. **Nothing about the origin period is contemporaneous.** What is
contemporaneous is thin and specific: the 2004-09-02 docket entry (a complaint filed by third parties in the
founding year); the 2005 Stock Plan as filed (Ex-10.2, "FACEBOOK, INC. 2005 Stock Plan (as amended April
2006)(as amended July 2006)…(as amended January 200…)" — an instrument whose *amendment headers* are
themselves a dated record of an equity-granting engineering organisation from 2005 onward); the Zynga
"Developer Addendum No. 2 … effective as of **December 26, 2010** … made by and between Facebook, Inc. and
Facebook Ireland Limited … and Zynga Inc." (Ex-10.13); and the Wilson Menlo Park lease (Ex-10.11,
"COMMENCEMENT DATE: February 7, 2011 … TERMINATION DATE: February 6, 2026"). Version evidence measured
across the lineage, in the same breath: the dorm sentence is **unchanged in all 12 stored documents that
carry it**, spanning the S-1 of 2012-02-01, seven amendments and the final prospectus — i.e. five staff-comment
rounds (`CORRESP` 2012-03-27, 05-14, 05-15 among them) did **not** move it, which tells us what the company
was willing to print and not what happened.

### 6. Corrections this pass took on its own dispatch premises and on the probe dossier

Five inherited statements failed against the bytes or needed narrowing. Each is corrected here and reaches
the registers; **none is carried forward quietly.**

1. **COR-1 — "No EDGAR document can ever fix the founding day for this company" — REFUTED.** The probe
   states this from the S-1 accession's 28-item file list, which indeed holds no charter. But exhibits filed
   with the *later* amendments were not on disk when the probe ran (`_MANIFEST.csv` rows 16-19, accession
   0001193125-12-175673, `fetched` 2026-09-29T19:05:53Z), and Ex-3.3 among them recites the day: **"was July
   29, 2004, under the name TheFacebook, Inc."** The corrected statement is narrower and still consequential:
   **EDGAR fixes the founding day at the company's own recital, in an unexecuted form; only the Delaware
   registry can fix it as a record** (**U.1**). This is §14 rule 11 in action — late-arriving primaries are
   evidence *for* the pass that reads them.
2. **COR-2 — "`Saverin` 0 hits across the lineage" — REFUTED for the exhibit set, CONFIRMED for the bodies.**
   The name appears **once** in the stored SEC corpus, in Ex-10.16A (Amendment No. 1 to Conversion Agreement,
   acc. 0001193125-12-208192, `fetched` 2026-09-29T19:05:57Z): "This Amendment together with the Conversion
   Agreement, Side Letter Agreement, any amendments hereto or thereto and **the Saverin Agreement** constitute
   the full and entire understanding…". It enters as **the defined title of a contract in a financing
   document**, not as a founder, not as a litigant, and with no text anywhere in the corpus describing what
   the Saverin Agreement does. `Winklevoss`, `ConnectU`, `Divya`, `Moskowitz` remain **0** in every stored
   document. Any Stage-1 or Stage-2 sentence of the form "the early equity disputes were disclosed in the
   S-1" is still forbidden, and now a sharper version is: **the only trace of one of the disputed parties in
   the whole SEC corpus is a defined term in an amendment to a conversion agreement.**
3. **COR-3 — the probe's "`Harvard` 0 / dorm not in the filings" framing — must be split.** `Harvard College`
   is 0, `February 2004` is 0, `thefacebook.com` is 0 — all confirmed. But `Harvard` occurs (in the director
   biography sentence "Mr. Zuckerberg attended Harvard University where he studied computer science", and as
   one of five named Pages), and the dorm claim **is** in the filing text: "Facebook has grown from our
   beginnings in a college dorm room in 2004…". So the correct ruling is: **the *place* is in the S-1 at
   year level, as a FOUNDER CLAIM inside a registration statement; the *month* and the *day* of the launch
   are not in it at all.** The probe's conclusion (the launch date stays UNKNOWN) survives; its string
   evidence did not.
4. **COR-4 — six in-window legal matters → seven.** The probe's table lists six; the same held payload
   carries a seventh in-window caption, `Leader Technologies Inc. v. Facebook Inc.`, 1:08-cv-00862, D. Del.,
   `dateFiled` 2008-11-19, inside the 2008-10-14 → 2012-02-01 EDGAR silence the probe called "a real null".
   The null is about **EDGAR**, and holds; it is not a null about **litigation**, and the register keeps
   speaking inside it.
5. **COR-5 — a provenance drift found in the stored bytes, reported not repaired.**
   `0001193125-12-034517_d287954ds1.htm` on disk is **2,657,075 B, sha1 `d749855a…`, mtime 2026-10-07**, while
   its own sidecar records **2,627,682 B, sha1 `bf14d107…`, `fetched` 2026-09-29T19:05:37Z**, and
   `_MANIFEST.csv` repeats the sidecar's numbers. The file was re-fetched after the manifest was written and
   the sidecar was not updated. The 424B4's sidecar **does** match its bytes (`sha1 f7fa2eb2…`). Every
   passage quoted in this volume was read from the bytes currently at the path, and the S-1 body is cited
   with that caveat attached (`P1S01.notes`). `sources/` is read-only to this pass (§14 rule 4): recorded
   here, in the register, and in `_parts/NOTES_meta_p1.md`; nothing was rewritten to make the numbers agree.

### 7. Post-boundary and pre-boundary conventions

Anything after **2012-12-31** is `(PB)`: the FY2013 10-K, the 2021 renaming (undated here — §Boundary 1 row
5), and every later restatement of the origin story may be used in this corpus only to (i) date a silence,
(ii) name a route, or (iii) show what the company later said about the window, always labelled
`RETROSPECTIVE SOURCE`. Anything before **2004-07-29** is `(PF)` — pre-corporate, and in this corpus it means
*attached to a person or to nobody*: the alleged April-2003 Ceglia contract, Facemash, Photo Manual, and the
launch itself. `(PF)` is not a licence to narrate a founder's biography backwards into a company's account,
and it is not a null either: it is the period where the corpus is silent **and the archives were unreachable**.

### 8. The seven conflicts this volume registers (anchors U.1–U.7)

| Anchor | Subject | Where adjudicated |
|---|---|---|
| **U.1** | Formation day: company recital in an unexecuted filed form vs the absent registry record | §Boundary 1 row 1, §B.4 |
| **U.2** | Subject of the origin: the registrant vs Mr Zuckerberg personally (April 2003, Ceglia) | §Boundary 1 rule, §C.2, §D.3 |
| **U.3** | First CIK activity 2005-05-06 (`REGDEX`, unattributed) vs "first filing = the 2012 S-1" | §Boundary 2 rival 4, §Boundary 3 |
| **U.4** | Prospectus silence on the origin disputes vs a live federal register naming them | §Boundary 1 row 4, §I.2, §D.2 |
| **U.5** | "Founded February 2004 / dorm room" vs the only dated origin statements in the filings | §Boundary 2 rival 2, §C.1, §D.1 |
| **U.6** | Growth claims tied to "thirty days" / user-count folklore vs the corpus's only "30 days" strings | §D.4, §F.3 |
| **U.7** | Stage architecture: probe's Stage-1 close July 2004 vs dispatched window 2003→2012 | §Header Span, §Boundary 2 rivals 1 and 7 |

## A

STATUS: WRITTEN 2026-10-06

### A.1 The state of the company at the close of the window, on the last day the corpus allows

The last in-window document is the final prospectus, 424B4, filed **2012-05-18** (acc. 0001193125-12-240111;
3,545,401 B; sha1 `f7fa2eb2…`, matching its sidecar). What it prints about the company at that moment:

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Registrant | Facebook, Inc., a Delaware corporation; "the terms 'Facebook,' 'company,' 'we,' 'us,' and 'our' … refer to Facebook, Inc., a Delaware corporation, and, where appropriate, its wholly-owned subsidiaries" | 424B4 Corporate Information | High (as a 2012 printing) |
| Formation | "We were incorporated in Delaware in July 2004"; day-level recital 2004-07-29 as **TheFacebook, Inc.** | 424B4; Ex-3.3 (filed 2012-04-23) | High / **Medium** on the day (unexecuted form, U.1) |
| Headquarters | Menlo Park, California | 424B4 Business overview | High |
| Revenue FY2011 | $3,711 million | 424B4 Selected Consolidated Financial Data (audited) | High |
| Operating income / net income FY2011 | $1,756 million / $1,000 million | same table | High |
| Revenue Q1 2012 | $1,058 million (unaudited), vs $731 million in Q1 2011 | same table | High |
| MAUs | 901 million as of 2012-03-31, +33% on 680 million as of 2011-03-31 | 424B4 "Our Size and Scale" | Medium (internal company data, self-declared) |
| DAUs | 526 million on average in March 2012, +41% on 372 million in March 2011; DAUs as % of MAUs 55% → 58% | 424B4 Trends in Our User Metrics | Medium (same caveat) |
| Mobile | 488 million MAUs who used Facebook mobile products in March 2012 | 424B4 | Medium |
| Graph size | "more than 125 billion friend connections on Facebook as of March 31, 2012" | 424B4 | Medium |
| Headcount | 3,539 full-time employees at 2012-03-31, from 2,431 at 2011-03-31 (+46%) | 424B4 Risk Factors; Facilities | High |
| Facilities | ~2.2 million sq ft leased worldwide, of which 1 million sq ft HQ; data centres owned in North Carolina and Oregon, leased in California and Virginia | 424B4 Facilities | High |
| Control | Class B to hold ~96.0% of voting power after the offering; the founder "will hold or have the ability to control approximately 55.9% of the voting power" | 424B4 The Offering | High (as a prospectus statement) |
| Listing | Class A approved for listing on the NASDAQ Global Select Market under the symbol **FB** | 424B4 The Offering | High |
| Balance sheet 2011-12-31 | cash+marketable securities $3,908M; P&E net $1,475M; total assets $6,331M; total liabilities $1,432M; stockholders' equity $4,899M | 424B4 Selected Financial Data (audited) | High |

### A.2 The state of the company at the open of the window — what is actually there

This is the honest version of the same table for 2003-2005. It has **six rows**, and every one of them is
either a 2012 recital or a third-party register entry.

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Legal person | none existed before **2004-07-29**; on that date a certificate of incorporation was filed in Delaware **under the name TheFacebook, Inc.** | Ex-3.3 recital, filed 2012-04-23 | **Medium** — company recital, unexecuted form, no registry copy held (**U.1**) |
| First money into the entity | "In 2004 and 2005, Mr. Zuckerberg's father provided us with initial working capital", in consideration of an option for 2,000,000 Class B shares that **expired unexercised one year after grant**; 2,000,000 shares were issued to **Glate LLC**, an entity owned by the father, in **December 2009** | 424B4 Related Party Transactions, "Class B Common Stock Restriction Agreement" | Medium (self-report, same lineage, restated) |
| First outside capital | "We originally entered into the IRA in connection with our **Series A financing in 2005** and it was amended in each of our future preferred stock financing rounds" | 424B4 Description of Capital Stock / Certain Relationships | Medium (year-level only; amount, price and purchasers not read by this pass) |
| First outside director | "James W. Breyer has served as a member of our board of directors **since April 2005**" (a Partner of Accel Partners since 1987) | 424B4 Management | Medium |
| First independent date attached to the founder | federal complaint **ConnectU LLC v. Zuckerberg**, 1:04-cv-11923, D. Mass., `dateFiled` **2004-09-02**, 190 Contract: Other / 28:1332 Diversity-Breach of Contract | `sources/legal/cl2_%22ConnectU%22.json` | High (as a register entry); **the claim's content is UNKNOWN — pleadings not fetched** |
| Product | **UNKNOWN.** No launch date, no first page, no first feature, no first user count, no first customer anywhere in 31 stored SEC documents, 7 stored periodical texts, or any archive response | §Boundary 3 family (b); §D | **UNKNOWN is the finding** |

**What is NOT in A.2, and would be in any ordinary telling:** the month the product went up; who else was a
founder; what the site looked like; how many users it had in 2004, 2005 or 2006; who bought the first
advertising; what the company's first revenue was; where it first sat physically. The audited series in the
prospectus **begins at FY2007** (revenue $153M, net loss $(138)M), and the XBRL series written by the script
begins later still: `sources/financials/xbrl_early_series.csv` holds **215 rows, `end` dates spanning
2010-12-31 → 2013-12-31, and zero rows before 2010** (`start` 2010-01-01 → 2013-07-01). The probe's
`facts 2004→2013` call therefore returned **no pre-2010 datum at all**. That is a TRIED–ANSWERED null about
the machine-readable record, not about the company — but it is why §A.2 has six rows and §A.1 has fourteen.

### A.3 What this stage is not

* This is **not** a stage in which the company was validated by a market. On the held evidence the firm
  reached product-market proof in the window is **unstated by any contemporaneous document**; the only
  quantities available are 2012 recitals of 2007-2012 audited results and third-party attention counts
  dated 2010-2012 (§G, §H).
* This is **not** a stage whose disputes were disclosed. The prospectus names **one** origin-era legal matter,
  Ceglia, and describes it as the adversary's claim; it names no Winklevoss, no Divya, no ConnectU, no
  Moskowitz — while the federal register shows those suits filed 2004, 2006, 2007 and appealed 2007
  (**U.4**). Silence in a disclosure document is not innocence and is not absence: it is a choice about what
  the company printed.
* This is **not** a stage about Meta Platforms, Inc. as a named person. That name belongs to the same CIK
  (EDGAR `former_names: ["Facebook Inc"]`) and to no document in this corpus (§Boundary 1 row 5).

### A.4 Load-bearing claim records for §A

P1-01 Claim: The final IPO prospectus of Facebook, Inc. was filed on 2012-05-18 and is the last in-window Tier-1 document for this stage. — Date: 2012-05-18 — Source: Form 424B4, Facebook, Inc. — Source date: 2012-05-18 — URL: https://www.sec.gov/Archives/edgar/data/1326801/000119312512240111/d287954d424b4.htm — Archived: UNKNOWN (no web capture held) — Tier: 1 — Class: FACT — Passage: "The information in this prospectus is accurate only as of the date of this prospectus" — Conf: High — Corroboration: 1 independent (same lineage as the S-1 and its eight amendments) — Conflicts: None

P1-02 Claim: The company reported FY2011 revenue of $3,711 million, operating income of $1,756 million and net income of $1,000 million. — Date: 2011-12-31 — Source: 424B4 Selected Consolidated Financial Data and Business overview — Source date: 2012-05-18 — URL: as P1-01 — Archived: UNKNOWN — Tier: 1 — Class: FACT (audited comparatives; CONTEMPORANEOUS for 2011, RESTATED for 2007-2008 which are "derived from audited consolidated financial statements that are not included in this prospectus") — Passage: "In 2011, we recorded revenue of $3,711 million, operating income of $1,756 million, and net income of $1,000 million." — Conf: High — Corroboration: 1 lineage — Conflicts: None

P1-03 Claim: A Delaware certificate of incorporation for this business was filed on July 29, 2004 under the name TheFacebook, Inc. — Date: 2004-07-29 — Source: Exhibit 3.3, Form of Restated Certificate of Incorporation, filed with the S-1/A of 2012-04-23 — Source date: 2012-04-23 — URL: https://www.sec.gov/Archives/edgar/data/0001326801/000119312512175673/d287954dex33.htm — Archived: UNKNOWN — Tier: 1 — Class: FACT about the recital; registrant assertion about the event (the exhibit is an unexecuted FORM whose `Dated:` line is blank) — Passage: "The date of filing its original Certificate of Incorporation with the Secretary of State was July 29, 2004, under the name TheFacebook, Inc." — Conf: Medium — Corroboration: 1 (month level only corroborated inside the same lineage) — Conflicts: **U.1**

P1-04 Claim: The earliest externally generated, machine-dated record naming Mark Zuckerberg over company ownership is a federal complaint filed 2004-09-02. — Date: 2004-09-02 — Source: CourtListener RECAP register, ConnectU LLC v. Zuckerberg, 1:04-cv-11923 (D. Mass.) — Source date: 2026-09-26 (payload retrieved; event date 2004-09-02) — URL: local bytes `sources/legal/cl2_%22ConnectU%22.json` — Archived: UNKNOWN — Tier: 1 — Class: FACT about the register entry; the pleaded content is UNKNOWN — Passage: NO_VERBATIM_PASSAGE_RECORDED (the payload holds these as separate JSON field values: `caseName` "ConnectU LLC v. Zuckerberg", `docketNumber` "1:04-cv-11923", `court` "District Court, D. Massachusetts", `dateFiled` "2004-09-02") — Conf: High — Corroboration: 1 register (docket text not fetched) — Conflicts: **U.4**

P1-05 Claim: No document in the corpus dates or describes the launch of the product. — Date: UNKNOWN — Source: this volume's own census of 31 stored SEC documents, 7 stored periodical texts, 3 failed CDX responses and 30 harvest rows — Source date: 2026-10-06 — URL: local — Archived: not applicable — Tier: 1 (a measured absence within Tier-1 bytes) — Class: UNKNOWN / TRIED–UNANSWERED for family (b), UNQUERIED for (d), UNTRIED for (e) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High on the absence in these files, UNKNOWN on the event — Corroboration: not applicable — Conflicts: **U.5**

## B

STATUS: WRITTEN 2026-10-06

### B.1 The founder, exactly as the registrant described him, and nothing beyond it

The prospectus's director-nomination paragraph is the fullest Tier-1 statement of who this company came from,
and it is four sentences long:

> "Mark Zuckerberg is our founder and has served as our CEO and as a member of our board of directors since
> July 2004. Mr. Zuckerberg has served as Chairman of our board of directors since January 2012. Mr.
> Zuckerberg attended Harvard University where he studied computer science."

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Title at formation | CEO and director **since July 2004** | 424B4 Management | Medium (2012 self-report about 2004) |
| Designation | "our founder" — singular | 424B4 The Offering; Management | High (as a 2012 printing); **FOUNDER CLAIM** as to the act |
| Education | "attended Harvard University where he studied computer science" — **no major, no class year, no withdrawal, no date of leaving** | 424B4 Management | High on the printing; the withdrawal question is **UNKNOWN in this corpus** |
| Age at 2012-03-31 | 27 (Chairman and CEO in the executive-officer table) | 424B4 Management table | High |
| Pre-IPO exercise | "has exercised an outstanding stock option with respect to 60,000,000 shares of Class B common stock and will offer 30,200,000 of those shares as Class A common stock" | 424B4 The Offering | High (as printed) |
| Co-founders | **Not named.** The filings name no co-founder anywhere. `Winklevoss` 0, `Divya` 0, `Moskowitz` 0, `Saverin` 1 (only as "the Saverin Agreement", a defined term in Ex-10.16A) | census of all 31 stored SEC documents, §Boundary 1 row 6, §Boundary 6 COR-2 | **High on the silence; the co-founder question is UNKNOWN, not settled** |

**The single most consequential thing §B can say** is what the corpus does *not* let it say. The folklore
record — that the company was founded by a board of five, that two classmates supplied the idea, that a
Brazilian co-founder was squeezed out — is **not contradicted by these documents either**, because these
documents never engage it. The register (2004-09-02, 2006-10-26, 2007-02-21, 2007-03-09, 2007-03-28,
2007-05-22, 2008-11-19) proves that *other people sued about this company's ownership in its founding year
and for four years after*, and that is the whole of what is independently datable. Everything past that
sentence is either the company's 2012 recital or an unfetched pleading (**U.4**).

### B.2 Company state at the open: where the entity's first money came from

| Item | Verbatim / value | Source | Confidence |
|---|---|---|---|
| Initial working capital | "In 2004 and 2005, Mr. Zuckerberg's father provided us with initial working capital." | 424B4 Related Party Transactions ("Class B Common Stock Restriction Agreement") | Medium — self-report, one lineage, restated; **it is nonetheless the only Tier-1 statement of the entity's first funding source anywhere in the corpus** |
| Consideration | an option to purchase 2,000,000 Class B shares, "as adjusted for splits and reclassifications"; "The option initially expired by its terms one year following the date of grant without having been exercised." | same | Medium |
| Cure, years later | a board **without Mr Zuckerberg** determined the option "did not reflect the intent of the parties … and a release from potential related claims", and "in December 2009, we issued an aggregate of 2,000,000 shares of our Class B common stock to Glate LLC, an entity owned by Mr. Zuckerberg's father" | same | Medium |
| First institutional round | "We originally entered into the IRA in connection with our Series A financing in 2005 and it was amended in each of our future preferred stock financing rounds." | 424B4 Certain Relationships / Description of Capital Stock | Medium — **2005 at year level; the month, size, price and purchasers were not read by this pass** |
| First outside director | "James W. Breyer has served as a member of our board of directors since April 2005." | 424B4 Management | Medium |
| Named IRA parties | "We, along with entities affiliated with Mr. Andreessen, Mr. Thiel, Mr. Breyer and Accel Partners, and DST Global Limited, as well as certain other parties, are parties to the IRA." | 424B4 | High as to the 2012 printing; **the date each joined is not printed**, which is precisely the hole the investor folklore fills |

**Why this matters for the folklore trap.** The most repeated early-financing stories in the secondary
literature attach investors to 2004 and attach drama to a Palo Alto house. What a Tier-1 document will
support is narrower: **the entity's first cash is described as family money in 2004 and 2005; its first
registered preferred round is dated 2005; its first outside director arrived April 2005.** Nothing in this
corpus dates any venture investor to 2004, and §K (part 2) must not manufacture the difference. The rows
above are the disciplined ceiling for the "early investor narratives" cluster.

### B.3 Organisation inside the window, on instruments rather than prose

| Date | What the corpus holds | Why it is stronger than a recital |
|---|---|---|
| 2005 (plan year) | Ex-10.2, printed as "FACEBOOK, INC. 2005 STOCK PLAN (as amended April 2006) (as amended July 2006) (as amended April 2007)" and carrying eight further dated amendment headers to 2008 | a plan **with a dated amendment trail** is evidence of an equity-granting engineering organisation from 2005 onward, without anyone narrating it |
| 2010-12-26 | Ex-10.13 "Developer Addendum No. 2 … effective as of December 26, 2010 … and is made by and between Facebook, Inc. and Facebook Ireland Limited … and Zynga Inc." (the stored HTML has stripped the filing's typographic quotation marks around the defined terms) | counterparty-signed; also the corpus's only evidence of an Irish subsidiary operating the service in Europe |
| 2011-02-07 | Ex-10.11 LEASE, parties block set in stacked centred lines as "WILSON MENLO PARK CAMPUS, LLC," / "a Wisconsin limited liability company" / "Landlord," and "FACEBOOK, INC., a Delaware corporation" / "Tenant"; "COMMENCEMENT DATE: February 7, 2011"; "TERM OF LEASE: Approximately fifteen (15) years"; "TERMINATION DATE: February 6, 2026" | a third-party instrument naming the registrant and its state two decades-worth of rent away from any press release; it is the **earliest held document that both names the entity and binds a stranger to it** |
| 2012-02-28 | Ex-10.14 Credit Agreement and Ex-10.15 Bridge Loan Agreement, each "dated as of February 28, 2012 among FACEBOOK, INC., THE LENDERS PARTY HERETO and JPMORGAN CHASE BANK, N.A., as Administrative Agent" | in-window, counterparty-dated, bank-reviewed: the company's debt shape immediately before registration |
| 2012-03-31 | 3,539 full-time employees; 774 issued US patents and 546 US applications; 42 million Pages with ten or more Likes; more than 125 billion friend connections | end-of-stage measured state (§A.1), all company-counted |

### B.4 What cannot be said about the founding, and why it stays UNKNOWN

* **The day.** Ex-3.3 recites July 29, 2004 and the name TheFacebook, Inc. — inside a **form** of restated
  certificate whose `Dated:` line and signature block are blank in the held bytes. A recital of a filing date
  in an unexecuted instrument is better than any other document this corpus has, and it is not a charter.
  **Confidence Medium; the upgrade route is a Delaware certified copy (`## FETCH REQUEST` F-2).** (**U.1**)
* **The original share structure.** Ex-3.3's Article IV is the **post-IPO** structure (9,241,000,000 shares
  total: 5,000,000,000 Class A, 4,141,000,000 Class B, 100,000,000 preferred, par $0.000006). It says nothing
  about what was authorized in 2004, and none of it may be read back as the founding capitalisation.
* **The first office.** The earliest facility evidence held is the 2011 lease. Anything about 2004 premises is
  **UNKNOWN**; the 2012 statement "headquartered in Menlo Park, California" is a statement about 2012.
* **The founders other than one.** See §B.1: the corpus names one founder and, separately, seven lawsuits
  about ownership. The two facts do not combine into a story without the pleadings.
* **The personal finances of the founder** (§K, part 2's section; not attempted here).

### B.5 Load-bearing claim records for §B

P1-06 Claim: The registrant describes Mark Zuckerberg as its singular founder, CEO and a director since July 2004. — Date: 2004-07 — Source: 424B4 Management (nomination basis paragraph) — Source date: 2012-05-18 — URL: as P1-01 — Archived: UNKNOWN — Tier: 1 — Class: FOUNDER CLAIM (registrant-retrospective about 2004; FACT about the 2012 printing) — Passage: "Mark Zuckerberg is our founder and has served as our CEO and as a member of our board of directors since July 2004." — Conf: Medium — Corroboration: 1 lineage — Conflicts: **U.4**

P1-07 Claim: The entity's first working capital is described in the prospectus as coming from the founder's father in 2004 and 2005. — Date: 2004 / 2005 — Source: 424B4 Related Party Transactions — Source date: 2012-05-18 — URL: as P1-01 — Archived: UNKNOWN — Tier: 1 — Class: RESTATED self-report; FACT about the disclosure — Passage: "In 2004 and 2005, Mr. Zuckerberg's father provided us with initial working capital." — Conf: Medium — Corroboration: 1 lineage — Conflicts: None (registered for §K continuity)

P1-08 Claim: The company's first registered preferred round is dated 2005 by its own prospectus, and the investors' rights agreement descends from it. — Date: 2005 — Source: 424B4, Certain Relationships and Related Transactions / Description of Capital Stock — Source date: 2012-05-18 — URL: as P1-01 — Archived: UNKNOWN — Tier: 1 — Class: RESTATED self-report — Passage: "We originally entered into the IRA in connection with our Series A financing in 2005 and it was amended in each of our future preferred stock financing rounds." — Conf: Medium — Corroboration: 1 lineage — Conflicts: None

P1-09 Claim: A landlord bound a fifteen-year lease to Facebook, Inc. as of February 7, 2011, which is the earliest held instrument naming the registrant and a stranger. — Date: 2011-02-07 — Source: Exhibit 10.11 (Lease), filed with the S-1/A of 2012-02-08 — Source date: 2012-02-08 — URL: https://www.sec.gov/Archives/edgar/data/0001326801/000119312512046715/d287954dex1011.htm — Archived: UNKNOWN — Tier: 1 — Class: FACT (counterparty-signed instrument) — Passage: "COMMENCEMENT DATE: February 7, 2011" (the parties are set as stacked centred lines — "WILSON MENLO PARK CAMPUS, LLC," / "a Wisconsin limited liability company" / "Landlord," … "FACEBOOK, INC.," / "a Delaware corporation" / "Tenant" — so the party sentence is quoted by layout, not as one contiguous string) — Conf: High — Corroboration: 2 origins (a company filing and a landlord's instrument, though only the company's copy is held) — Conflicts: None

P1-10 Claim: No SEC document in the lineage names Winklevoss, ConnectU, Divya or Moskowitz, and only one names Saverin, and then only as the title of an agreement. — Date: 2012-02-01 → 2012-05-18 — Source: census of all 31 stored documents in `sources/sec/` — Source date: 2026-10-06 — URL: local — Archived: not applicable — Tier: 1 — Class: FACT about the corpus (a measured string census) — Passage: "This Amendment together with the Conversion Agreement, Side Letter Agreement, any amendments hereto or thereto and the Saverin Agreement constitute the full and entire understanding and agreement among the parties" — Conf: High — Corroboration: 1 lineage, 31 files — Conflicts: **U.4**

## C

STATUS: WRITTEN 2026-10-06

### C.1 The problem, stated by the only entities that stated it — and the date they stated it

| Statement as printed | Where it is printed | Date of the printing | What it is evidence of | Class |
|---|---|---|---|---|
| "Our mission is to make the world more open and connected." | 424B4, Note 1 of the audited consolidated financial statements, "Organization and Description of Business" | 2012-05-18 | what the company chose to say its purpose was **in 2012**, in an audited note | FOUNDER CLAIM / corporate self-characterisation; FACT about the printing |
| "Facebook was not originally founded to be a company. We've always cared primarily about our social mission, the services we're building and the people who use them." | Letter from Mark Zuckerberg (the prospectus's founder letter) | 2012-02-01 → 2012-05-18 | a retrospective claim about the *origin*, printed inside a registration statement whose purpose was to sell equity | **FOUNDER CLAIM, retrospective**, and structurally self-interested: the sentence argues that the reader should not judge the company by its founding motive |
| "I started off by writing the first version of Facebook myself because it was something I wanted to exist." | same letter | 2012-05-18 | the founder's account of the first artifact: single authorship, personal utility, **no date, no place, no institution, no co-founder** | FOUNDER CLAIM, retrospective memory; **the closest thing in the corpus to a first-experiment statement** |
| "Simply put: we don't build services to make money; we make money to build better services." | same letter | 2012-05-18 | the stated ordering of motive, asserted eight weeks before the offering | FOUNDER CLAIM |
| "Our top priority is to build useful and engaging products that enable you to: Connect with Your Friends … Discover and Learn … Express Yourself …" | 424B4 Business, "How We Create Value for Users" | 2012-05-18 | the 2012 problem statement, addressed to 900 million users, not to a 2004 market | RESTATED |

**Nothing in this table was written in the window it describes.** The gap between the acts and the accounts is
eight years for every sentence, and that gap is the section's real finding: for 2003-2004 the corpus contains
**no problem statement at all** — no plan, no memo, no page, no letter, no user interview, nothing the company
or anyone else wrote while the outcome was unknown. The anti-hagiography test is what keeps §C from
improving on that: read as of 2004, the same sentences would describe a student's personal utility tool with
no market, no revenue model and no evidence of a plan, which is exactly what the evidence supports.

### C.2 What the problem was *not*, on this evidence

* **Not the company's problem before 2004-07-29.** There was no company. The only 2003-dated Tier-1 statement
  in the corpus is an adversary's: Ceglia's alleged April-2003 contract with Mr Zuckerberg personally, which
  the prospectus reproduces and characterises as "purported" and, of the emails, as "supposed" (§Boundary 1
  rule; **U.2**). Pre-formation activity is a fact about a person, and the registrant's own filing keeps it
  there.
* **Not an identified market.** No document in the corpus states a market the founder set out to enter, and
  the prospectus's market material (§H) is 2010-2012 third-party sizing of advertising spend, not a founding
  intent. Anyone writing "the problem was X" from the 2012 mission sentence is importing a later self-image
  into an earlier act.
* **Not a disclosed dispute.** The origin conflicts are in the court register, not in the company's account of
  itself (**U.4**), and the prospectus's single named origin-era matter (Ceglia) is the one the company did
  print — as someone else's claim.

### C.3 Knowability, for this stage (§7 format)

| Question | Status | Basis |
|---|---|---|
| What was the entity's stated mission at the moment of registration? | **KNOWABLE** | the 2012 filings, read as 2012 statements |
| What problem was the founder trying to solve in 2003-2004, in his own contemporaneous words? | **NOT KNOWABLE from this corpus**; the routes are family (b) (archived first page), the unfetched pleadings, and the Harvard student press, which has **no configured corpus route in this fleet at all** (probe's Untried item 8) | probe; §Boundary 3 |
| Whether anyone else was a co-founder of the *idea* | **UNKNOWN** | the filings name one founder; the register names seven suits; neither set answers it |
| Whether the mission sentence was written earlier than 2012 | **UNKNOWN** | no held document predates the registration statement |

### C.4 Claim records for §C

P1-11 Claim: The registrant's mission sentence appears inside the audited financial-statement note, not only in marketing matter. — Date: 2012-05-18 — Source: 424B4, Note 1 to the consolidated financial statements — Source date: 2012-05-18 — URL: as P1-01 — Archived: UNKNOWN — Tier: 1 — Class: FACT about the printing; FOUNDER CLAIM about intent — Passage: "Facebook was incorporated in Delaware in July 2004. Our mission is to make the world more open and connected." — Conf: High — Corroboration: 1 lineage (the same sentence pair appears in the Corporate Information section of the same document) — Conflicts: None

P1-12 Claim: The founder's account of the first artifact is a single-author personal-utility claim carrying no date, place or institution. — Date: 2012-05-18 (printing); event date UNKNOWN — Source: Letter from Mark Zuckerberg, 424B4 — Source date: 2012-05-18 — URL: as P1-01 — Archived: UNKNOWN — Tier: 1 — Class: FOUNDER CLAIM (retrospective memory) — Passage: "I started off by writing the first version of Facebook myself because it was something I wanted to exist." — Conf: Low as to the event, High as to the text — Corroboration: 1 — Conflicts: **U.5**

## D

STATUS: WRITTEN 2026-10-06

**Section note.** The method's second beat — *first real-world experiment* — is the beat this company's
evidence base cannot support, and §10 names exactly this situation as a standing research-debt trigger. This
section therefore does two things: it lists, with carriers, every proposition about an early experiment that
the corpus can actually hold up (§D.1–§D.2); and it states, without substitution, what it cannot
(§D.3–§D.4). **No number, date or name is imported to fill the hole.**

### D.1 The four propositions the corpus does support about an early experiment

| # | Proposition | Carrier | Reading |
|---|---|---|---|
| 1 | The company's own origin sentence places a beginning in **a college dorm room in 2004** | "Building on our use of authentic identity, the Social Graph, and social distribution, **Facebook has grown from our beginnings in a college dorm room in 2004** to a service that is fundamentally changing the way people connect, discover, and share around the world." — 424B4 Business, "Our Size and Scale"; identical in the S-1 of 2012-02-01 | **FOUNDER CLAIM inside a registration statement.** It gives a *place* and a *year*, and no month, no day, no product name, no URL, no first user. It survived all eight amendments and five staff-comment rounds unchanged (§Boundary 5) — which is version evidence about what the company was willing to print, not corroboration |
| 2 | A person who later ran this corporation was, in 2004, being sued over the ownership of a company by others | docket 1:04-cv-11923, `dateFiled` **2004-09-02**, "190 Contract: Other; 28:1332 Diversity-Breach of Contract" | **CONTEMPORANEOUS and independent of the founder account.** It proves activity, not content: a thing existed that people contractually disputed **before 2004-09-02**. As a terminus ante quem it is the strongest dating instrument in the corpus |
| 3 | The corporate person was created on **2004-07-29** as **TheFacebook, Inc.** | Ex-3.3 recital, filed 2012-04-23 | the formation act, not an experiment. **Formation is not launch.** The name at formation is the only in-corpus trace of the product's brand at the entity's birth, and it is a recital in an unexecuted form (**U.1**) |
| 4 | Money and governance followed fast: family working capital "in 2004 and 2005", a Series A and the first investors' rights agreement "in 2005", an outside director from **April 2005** | 424B4 Related Party Transactions; Certain Relationships; Management | an experiment that was worth capitalising within twelve months of formation, on the company's own accounting of it. **This is the closest the corpus comes to a validation signal for the origin period, and it is a financing fact, not a demand fact** (§L, part 2) |

### D.2 What the register adds, and what it does not

The same payload that dates the 2004 complaint also shows, in 2006-2007, a plaintiff called **ConnectU LLC**
and a caption printing **The Facebook, Inc.** as a defendant-petitioner (5:07-cv-01389, 2007-03-09) and
**Facebook, Inc.** as a defendant in a copyright suit brought by **Connectu, Inc.** (1:07-cv-10593,
2007-03-28, "820 Copyright; 17:101 Copyright Infringement"). Read as evidence, this is a rival product's
corporate person suing this one for copyright infringement in the same year the registrant was still private —
which is *competition* (§I.2) and *dispute* (**U.4**) at once. **What it does not add is any description of
either product**, because the register carries captions, not facts; the pleadings are the untried document
(FETCH REQUEST F-3). The four families that might have carried contemporaneous print about the launch
(archive captures, student newspaper, trade press, corporate print) returned, respectively: an outage, an
outage, a bot challenge, and no query at all (§Boundary 3).

### D.3 Facemash, Photo Manual, and the pre-corporate period: UNKNOWN, with the routes named

| Claim cluster in circulation | Census in this corpus | Status | Route that could settle it |
|---|---|---|---|
| "Facemash" (a 2003 Harvard site) | `Facemash` — **0 hits** across all 31 stored SEC documents, all 7 stored periodical texts, all 30 harvest rows, all 5 legal payloads | **UNTRIED / UNANSWERED — not refuted, not adopted.** No tier, no date, no role assigned | Wayback CDX for `facemash.*` and `thefacebook.com`; Harvard student press (no configured route); the unfetched Ceglia and ConnectU pleadings |
| "Photo Manual" / "PhotoManual" (a 2003 course-matching site) | **0 hits** (both spellings) | same as above | same routes |
| that the launch site was `thefacebook.com` | `thefacebook` — **1 hit in 31 SEC documents**, and it is the corporate-name recital "under the name TheFacebook, Inc."; `thefacebook.com` — 0 | **UNKNOWN as a URL**; the *corporate* name is the only held instance | CDX first-capture query (family (b), F-1) |
| that the launch was in **February 2004** | `February 2004` — **0 hits** | **UNKNOWN** | registry + CDX + pleadings |

**Discipline applied.** A claim with no carrier here is written as UNKNOWN and the route is named — it is not
"denied", and it is not replaced. The most common failure mode in this fleet's folklore-dense companies is a
repair pass that retracts a popular date and lets the reader absorb the retraction as a different date. The
February date is withdrawn from this volume's use, and **July 29, 2004 is not offered in its place**: July
29, 2004 is the date a *certificate was filed*, an act of formation; the launch, if it preceded formation, is
a separate act with **no date available at this reach** (**U.5**).

### D.4 The "thirty days" growth claim: what the corpus's only "30 days" strings are

Measured across `sources/sec/` (31 documents): `30 days` occurs **71 times** in the stored bytes and
`thirty days` occurs **exactly once**. The one "thirty days" is not a growth claim: it is an option-
administration clause in the 2005 Stock Plan (Ex-10.2) — an option may be exercised by an estate "within
thirty days following termination of Optionee's Continuous Service Status…". The `30 days` hits are of three
kinds, and only one kind touches users:

1. **A definition, not a rate:** "We define a monthly active user as a registered Facebook user who logged in
   and visited Facebook through our website or a mobile device, or took an action to share content or
   activity with his or her Facebook friends or connections via a third-party website that is integrated with
   Facebook, **in the last 30 days as of the date of measurement**." — this is the MAU measurement window,
   2012 text, 2011-2012 numbers attached to it.
2. **Equity mechanics:** the RSU settlement window ("we are permitted to deliver the underlying shares within
   30 days before or after the date on which the liquidity condition is satisfied").
3. **Contract and notice boilerplate** inside the filed exhibits (leases, agreements).

**Ruling.** There is **no carrier in this corpus for any "users grew X in thirty days" proposition**, and the
phrase that folklore attaches to the launch period is, in the bytes that exist, the *definition of a
measurement period* and a *vesting window*. Any such growth figure is **UNKNOWN**; the route that could
settle a 2004-2005 user count is the same triple as §D.3 (CDX, student press, pleadings) plus the S-1's
history graphic, which is un-extractable text (26 JPGs in the S-1 accession per the probe's enumeration;
`OCR of g287954g*.jpg` remains Untried item 7). **No substitute number is written anywhere in this volume, in
either part's registers, or in the timeline.** (**U.6**)

### D.5 Claim records for §D

P1-13 Claim: The registrant places its beginnings in a college dorm room in 2004 and says so in the body of its registration statement. — Date: 2004 (year only, as printed) — Source: 424B4 Business, "Our Size and Scale" — Source date: 2012-05-18 — URL: as P1-01 — Archived: UNKNOWN — Tier: 1 — Class: FOUNDER CLAIM about the event; FACT about the printing — Passage: "Facebook has grown from our beginnings in a college dorm room in 2004 to a service that is fundamentally changing the way people connect, discover, and share around the world." — Conf: Low as to the event — Corroboration: 1 lineage (identical text in the S-1 of 2012-02-01 and in seven amendments; repetition across drafts is not independence) — Conflicts: **U.5**

P1-14 Claim: Nothing in the corpus describes, dates or numbers the first working product. — Date: UNKNOWN — Source: census of `sources/sec/`, `sources/periodicals/`, `sources/legal/`, `sources/_harvest/`, `sources/web/` — Source date: 2026-10-06 — URL: local — Archived: not applicable — Tier: 1 corpus, Tier-1 families UNANSWERED/UNQUERIED/UNTRIED — Class: UNKNOWN, TRIED–UNANSWERED on family (b) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High on the absence in these files — Corroboration: not applicable — Conflicts: **U.5**, **U.6**

P1-15 Claim: The only "thirty days" in the stored SEC corpus is an option-exercise window in the 2005 stock plan, and the only user-metric "30 days" is the MAU measurement definition. — Date: 2005 plan text as filed 2012-02-08; definition printed 2012-05-18 — Source: Ex-10.2 (2005 Stock Plan) and 424B4 Trends in Our User Metrics — Source date: 2012-02-08 / 2012-05-18 — URL: https://www.sec.gov/Archives/edgar/data/0001326801/000119312512046715/d287954dex102.htm and as P1-01 — Archived: UNKNOWN — Tier: 1 — Class: FACT (string census, both readings verbatim-located) — Passage: "in the last 30 days as of the date of measurement" — Conf: High — Corroboration: 1 lineage, 31 files searched — Conflicts: **U.6**

P1-16 Claim: A rival product's corporate person sued Facebook, Inc. for copyright infringement while the registrant was still private. — Date: 2007-03-28 — Source: CourtListener register, Connectu, Inc. v. Facebook, Inc., 1:07-cv-10593, D. Mass., "820 Copyright; 17:101 Copyright Infringement" — Source date: payload retrieved 2026-09-26; event 2007-03-28 — URL: local bytes `sources/legal/cl2_%22ConnectU%22.json` — Archived: UNKNOWN — Tier: 1 — Class: FACT about the register entry; content UNKNOWN — Passage: NO_VERBATIM_PASSAGE_RECORDED (`caseName`/`docketNumber`/`court`/`dateFiled` field values) — Conf: High — Corroboration: 1 register — Conflicts: **U.4**

## E

STATUS: WRITTEN 2026-10-06

### E.1 The product as the only held description gives it — 2012, in the company's words

| Element | As printed | Basis label |
|---|---|---|
| What the company builds | "We build products that support our mission by providing utility to Facebook users, Platform developers, and advertisers." | audited Note 1, 424B4 — a **three-sided** structure stated as the design premise |
| Named products | core "News Feed, Photos, and Groups"; "new products such as Timeline and Ticker"; "Connect with Your Friends … Discover and Learn … Express Yourself" | Business section, 2012-05-18 |
| Reach of the surface | "As of March 31, 2012, there were more than 42 million Pages with ten or more Likes, including Harvard, Lady Gaga, The Metropolitan Museum of Art, Starbucks, and Boo (the World's Cutest Dog), as well as millions of local businesses." | Business section |
| The developer side | "The Facebook Platform is a set of tools and APIs that developers can use to build social apps on Facebook or to integrate their websites with Facebook. As of March 31, 2012, more than nine million apps and websites were integrated…" | Business section |
| Monetised relationship | "Advertisers can engage with more than 900 million monthly active users (MAUs) on Facebook or subsets of our users based on information they have chosen to share with us such as their age, location, gender, or interests." | Business section |
| Measurement definitions | MAU = a registered user who logged in and visited **in the last 30 days as of the date of measurement**; ARPU reported by region | Trends in Our User Metrics |

**Reading these as 2004 evidence is the anachronism §6 forbids.** Every element above is a 2012 state
described by the company. Their value to Stage 1 is structural, not chronological: they tell the reader what
the dorm claim grew *into*, and they are the reason §E.2's blank matters.

### E.2 The 2004-2006 product: what the corpus holds is a graphic and a name

* **The one place the filing narrates the early years is an image.** The Business section reads "Highlights
  in our history are depicted in the graphic on the next page." → "Our History" → page break → straight into
  "Trends in Our User Metrics". The accession carries **26 `g287954g*.jpg` figures** (the probe's enumeration
  of `sources/_index/S1_accession_filelist.txt`). **No text layer for the timeline is held anywhere**, so the
  corpus's only visual account of 2004-2006 is unreadable at this reach. Consequence for later passes: any
  sentence of the form "the S-1's history timeline shows X in 2005" is an **OCR claim**, not a text claim, and
  must be sourced as such. Route: OCR of the 26 JPGs (Untried item 7 in the probe; still untried).
* **The one word that survives from the product's own era is the corporate name.** *TheFacebook, Inc.*, at
  filing on 2004-07-29 (Ex-3.3). That is an entity name, and the only in-corpus evidence that the brand
  carried the definite article at birth. It is **not** a URL, not a feature set, and not a launch date.
* **Everything else is UNKNOWN**: the first page's content, the first feature set, whether real-name identity
  was a founding rule or a later policy ("authentic identity" is 2012 language), what networks were open and
  in what order, the first client software, the first hosting, the first mobile surface, and the first price
  of anything.

### E.3 What can be inferred, and how far

| Inference | Class | Supporting bytes | Ceiling |
|---|---|---|---|
| That a software artifact existed before 2004-09-02, and that people contractually disputed ownership of it. | **INFERENCE** (from the docket's cause code 190 Contract + the plaintiff being an LLC named for a rival site) | register row, `dateFiled` 2004-09-02 | Inference stops at "something disputable existed"; it does not reach what the artifact was |
| That the entity was capitalised and governed within a year of formation. | **INFERENCE, strong** | "initial working capital" 2004-2005; Series A "in 2005"; Breyer "since April 2005"; 2005 Stock Plan | Says nothing about product or users |
| That an engineering organisation existed by 2005. | **INFERENCE** | Ex-10.2's dated amendment trail; "the type of hands-on people" / Bootcamp / hackathon culture sentences (2012 text) | The 2005 plan is the only 2005-dated artifact of build-capacity; the culture sentences are 2012 |
| That the founding product and the 2012 product are the same continuous service. | **NOT SUPPORTED as an inference from these bytes**; it is the company's own retrospective claim and is classified FOUNDER CLAIM | the dorm sentence | No document in the corpus describes the 2004 product at all, so continuity of *design* cannot be checked |

### E.4 Claim records for §E

P1-17 Claim: The registration statement's account of the early years is a graphic with no extractable text. — Date: 2012-02-01 — Source: S-1 Business section; accession file list — Source date: 2012-02-01 — URL: as P1-01 (S-1 body: https://www.sec.gov/Archives/edgar/data/0001326801/000119312512034517/d287954ds1.htm) — Archived: UNKNOWN — Tier: 1 — Class: FACT (a measured property of the held bytes) — Passage: "Highlights in our history are depicted in the graphic on the next page." — Conf: High — Corroboration: 1 lineage — Conflicts: None

P1-18 Claim: The only word surviving from the product's own first year is the corporate name TheFacebook, Inc. — Date: 2004-07-29 — Source: Ex-3.3 — Source date: 2012-04-23 — URL: as P1-03 — Archived: UNKNOWN — Tier: 1 — Class: FACT about the recital; registrant assertion about the name — Passage: "under the name TheFacebook, Inc." — Conf: Medium — Corroboration: 1 — Conflicts: **U.1**

P1-19 Claim: By 2012 the registrant described itself as a three-sided service for users, Platform developers and advertisers. — Date: 2012-05-18 — Source: 424B4 Note 1 — Source date: 2012-05-18 — URL: as P1-01 — Archived: UNKNOWN — Tier: 1 — Class: FACT about the printing; RESTATED as description of the origin — Passage: "We build products that support our mission by providing utility to Facebook users, Platform developers, and advertisers." — Conf: High — Corroboration: 1 lineage — Conflicts: None

## F

STATUS: WRITTEN 2026-10-06

### F.1 Who the customer was, in the company's own structure, and when that structure is dated from

| Question | Answer available in the corpus | Date of the answer | Class |
|---|---|---|---|
| Who pays? | "We generate substantially all of our revenue from advertising and from fees associated with our Payments infrastructure that enables users to purchase virtual and digital goods from our Platform developers." | 2012-05-18 (audited Note 1) | FACT as disclosed |
| Who uses? | 901 million MAUs at 2012-03-31; 488 million mobile MAUs in March 2012; more than 125 billion friend connections | 2012-05-18 | company-internal counts (see §F.2) |
| Who is the counterparty in a named campaign? | "Walmart U.S. purchased advertising on Facebook targeting users in the United States between the ages of 18 and 49 during the days surrounding Black Friday in November 2011." | 2012-05-18, describing 2011 | FACT as disclosed; **the earliest named customer transaction in the corpus is 2011** |
| Who else is supplied to? | more than 42 million Pages with ten or more Likes; more than nine million integrated apps and websites | 2012-03-31 | company counts |
| **Who was the first customer?** | **Nothing.** No 2004-2010 customer, advertiser, invoice, order or contract is held | — | **UNKNOWN** |

**The earliest revenue datum of any kind** in this corpus is FY2007: revenue $153 million, cost of revenue
$41 million, operating loss $(124) million, net loss $(138) million, and share-based compensation of $73
million inside those expenses (424B4 Selected Consolidated Financial Data). The prospectus is explicit about
its provenance: the FY2007 and FY2008 statements of operations data "are derived from audited consolidated
financial statements **that are not included in this prospectus**". So FY2007 is a *filed restatement of an
unfiled audit* — Tier-1 in dignity, second-order in verifiability, and four years younger than the founding
act (§A.2).

### F.2 Independence problem, stated once for the whole section

Every user, Page, app and ARPU number in §F traces to **one company's internal counting, printed in one
registration lineage**, and the prospectus says so in two places: "This prospectus contains estimates and
information concerning our industry… based on industry publications and reports… **We have not independently
verified the accuracy or completeness of the data** contained in these industry publications and reports";
and "The numbers of our MAUs and DAUs and average revenue per user (ARPU) are **calculated using internal
company data**… there are inherent challenges in measuring usage of our products across large online and
mobile populations…". The company also volunteers the one quantified doubt about its own headline metric:
"We estimate that **false or duplicate accounts may have represented approximately 5-6% of our MAUs as of
December 31, 2011**. However, this estimate is based on an internal review of a limited samp[le]…". No
third party in this corpus counts users. That is the record-selection null operating exactly as §2 predicts:
the archive that survived is the company's, and it was compiled to sell shares.

### F.3 The first customer is UNKNOWN, and the trap that grows around it

The §10 trigger *the first customer is unknown* is **open** on this company, and it is open twice over: the
identity is unheld, and **the whole 2004-2006 commercial history is unheld** because the audited series starts
at 2007. Two folklore patterns must not be allowed to fill it: (i) importing a later advertiser (the Walmart
2011 sentence above) as an early one; and (ii) converting a **measurement window** into a **growth claim** —
the "30 days" ruling of §D.4 applies here too, and is registered as **U.6** so the merge can see that both
the metric definition and the vesting clause are *not* adoption evidence. The routes that could settle the
first customer: the unfetched `CORRESP` letters (the staff's questions, which sometimes force a commercial
history into text), the 26 history JPGs under OCR, and family (b) once archive.org answers.

### F.4 Claim records for §F

P1-20 Claim: The company's earliest revenue figures in any held document are for FY2007 and are recited from audits the prospectus does not contain. — Date: 2007-12-31 — Source: 424B4 Selected Consolidated Financial Data — Source date: 2012-05-18 — URL: as P1-01 — Archived: UNKNOWN — Tier: 1 — Class: RESTATED (audited elsewhere, recited here) — Passage: "The consolidated statements of operations data for the years ended December 31, 2007 and 2008 and the consolidated balance sheets data as of December 31, 2007, 2008, and 2009 are derived from audited consolidated financial statements that are not included in this prospectus." — Conf: High as printed; Medium as an audit trail — Corroboration: 1 lineage — Conflicts: None

P1-21 Claim: The company disclosed that its own user counts rest on internal data and that 5-6% of end-2011 MAUs may have been false or duplicate accounts. — Date: 2011-12-31 — Source: 424B4 Risk Factors — Source date: 2012-05-18 — URL: as P1-01 — Archived: UNKNOWN — Tier: 1 — Class: ESTIMATE by the company about itself (self-disclosed, uncheckable) — Passage: "false or duplicate accounts may have represented approximately 5-6% of our MAUs as of December 31, 2011" — Conf: High that it was disclosed; UNKNOWN what the true figure was — Corroboration: none independent — Conflicts: **U.6**

P1-22 Claim: No customer of the founding period is named anywhere in the corpus, and the earliest named transaction is a 2011 advertising purchase by Walmart U.S. — Date: 2011-11 (event); 2012-05-18 (printing) — Source: 424B4 Business — Source date: 2012-05-18 — URL: as P1-01 — Archived: UNKNOWN — Tier: 1 — Class: FACT as disclosed; the founding-period null is UNKNOWN — Passage: "Walmart U.S. purchased advertising on Facebook targeting users in the United States between the ages of 18 and 49 during the days surrounding Black Friday in November 2011." — Conf: High on the 2011 item; UNKNOWN on the first customer — Corroboration: 1 lineage — Conflicts: None

## G

STATUS: WRITTEN 2026-10-06

**Adaptation note (§7).** For a consumer network the standard "supply side" splits three ways, and this
section answers all three: **the host** (what serves the service), **the raw material** (users' own content
and connections, which the company does not buy), and **the third-party supply of function** (Platform
developers). What the frame cannot do here is run backwards: **none of the three is documented before 2007.**

### G.1 The host side, measured

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Property, plant & equipment, net | FY2007 $82M → FY2008 $131M → FY2009 $148M → FY2010 $574M → FY2011 $1,475M → 2012-03-31 $1,855M | 424B4 Selected Financial Data, balance-sheet columns (audited; FY2007-2009 statements not included in the prospectus) | High as printed; FY2007-2009 **RESTATED** |
| Cost of revenue | FY2007 $41M → $124M → $223M → $493M → FY2011 $860M | same, income-statement rows | High as printed |
| Owned data centres | "data center facilities that we own in North Carolina and Oregon" | 424B4 Facilities | High (as a 2012 statement) |
| Leased data centres | "leased data center facilities in California and Virginia" | same | High |
| Offices | "As of March 31, 2012, we leased office facilities around the world totaling approximately 2.2 million square feet, including one million square feet for our corporate headquarters in Menlo Park, California." | same | High |
| Anchor facility instrument | Ex-10.11 lease with Wilson Menlo Park Campus, LLC; commencement 2011-02-07; term ~15 years; termination 2026-02-06 | Ex-10.11, filed 2012-02-08 | High (counterparty instrument) |
| Design publication | "we have contributed certain specifications and designs related to our data center equipment to the Open Compute Project Foundation, a non-profit entity that shares and develops such information with the technology community, under the Open Web Foundation License" | 424B4 Risk Factors | High (as printed) |
| Pre-IPO debt for the build | Credit Agreement and Bridge Loan Agreement each "dated as of February 28, 2012", JPMorgan Chase as administrative agent | Ex-10.14, Ex-10.15 | High |
| **Any of this before 2007** | **UNKNOWN — no server, no rack, no hosting contract, no facility, no capex figure for 2004-2006 is held** | census, §Boundary 3 | the null is a **TRIED–ANSWERED** null for family (a) (the audited series simply starts at 2007) and UNANSWERED for (b)/(c)/(d) |

The shape of the P&E series is the most useful host-side fact in this volume because it is **not** a narrative:
a company whose net property stood at $148 million at the end of 2009 and $1,475 million two years later had
built its own capacity late and fast, and nothing in the corpus shows where that capacity was in 2004.

### G.2 The raw-material side: users as supply

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Friend connections | "more than 125 billion friend connections on Facebook as of March 31, 2012" | 424B4 | Medium (internal count) |
| Pages | more than 42 million Pages with ten or more Likes; plus "millions of local businesses" | 424B4 Business | Medium |
| Integrated surfaces | more than nine million apps and websites integrated as of 2012-03-31 | 424B4 Business | Medium |
| Language / footprint | "more than 70 different languages, and we have offices or data centers in more than 20 different countries" | 424B4 Risk Factors | High (as printed) |
| Supply-side dependence, in the company's own risk language | "Our Platform developers may choose to prioritize building or supporting Facebook-integrated websites as opposed to building or supporting apps that run on the Facebook website. When users visit a Platform partner's Facebook-integrated website, we do not deliver advertisements…" | 424B4 Risk Factors | High (as printed) — **the clearest statement in the corpus that the raw material is not owned** |

### G.3 The dependence that the corpus lets §G name

Two dependencies are documented rather than asserted. **On the demand side of the host**, the Zynga Developer
Addendum No. 2 (effective 2010-12-26) is a contract in which the company's largest third-party supplier of
function is *restricted* from communicating with "Zynga Users" through other "Social Platforms", and the
addendum's own definition of that category names Twitter, Google's social media properties (including Orkut,
Buzz), Gmail, LinkedIn, StudiVZ, Cyworld, Odnoklassniki, VKontakte, Mail.ru, kaixin001, 51.com and MySpace.
A contract that has to enumerate a supplier's alternatives is evidence of how the company itself saw the
field in 2010. **On the host side**, the 2012 credit and bridge facilities tie the physical build to
borrowed money weeks before registration — the company financed capacity while still private.

### G.4 Claim records for §G

P1-23 Claim: The registrant's owned data-centre capacity sat in North Carolina and Oregon, with leased capacity in California and Virginia, and its offices were 2.2 million leased square feet at 2012-03-31. — Date: 2012-03-31 — Source: 424B4 Facilities — Source date: 2012-05-18 — URL: as P1-01 — Archived: UNKNOWN — Tier: 1 — Class: FACT as disclosed, CONTEMPORANEOUS for the date measured — Passage: "We have data centers in the United States, including data center facilities that we own in North Carolina and Oregon and leased data center facilities in California and Virginia." — Conf: High — Corroboration: 1 lineage — Conflicts: None

P1-24 Claim: Net property, plant and equipment grew from $82 million at FY2007 to $1,475 million at FY2011 on the company's filed balance-sheet columns. — Date: 2007-12-31 → 2011-12-31 — Source: 424B4 Selected Consolidated Financial Data — Source date: 2012-05-18 — URL: as P1-01 — Archived: UNKNOWN — Tier: 1 — Class: FACT as printed; FY2007-2009 RESTATED (audited statements not included) — Passage: "Property and equipment, net 82 131 148 574 1,475 1,855" — Conf: High — Corroboration: 1 lineage — Conflicts: None

P1-25 Claim: A 2010 contract with Zynga enumerates the social platforms whose users the developer may not solicit, which is contemporaneous evidence of how the company defined its field. — Date: 2010-12-26 — Source: Exhibit 10.13, Developer Addendum No. 2 — Source date: 2012-02-08 — URL: https://www.sec.gov/Archives/edgar/data/0001326801/000119312512046715/d287954dex1013.htm — Archived: UNKNOWN — Tier: 1 — Class: FACT (counterparty-signed instrument) — Passage: "Twitter, Google's social media properties (including Orkut, Buzz, Google ME, or other properties with similar functionality), Gmail, LinkedIn, StudiVZ, Cyworld, Odnoklassniki, VKontakte, Mail.ru, kaixin001, 51.com and MySpace." — Conf: High — Corroboration: 1 (the instrument is inside the company's own filing; Zynga's copy is not held) — Conflicts: None

## H

STATUS: WRITTEN 2026-10-06

**Framing (§6, knowability first).** "The market as knowable in-period" for Stage 1 of this company has to be
answered twice, and the two answers are almost disjoint. **As knowable in 2004-2006: nothing.** Not one held
document reports a market condition, a competitor's scale, an ad-price benchmark or a user-count from inside
those years; the four non-filing families that could have returned 2004-2006 print are respectively offline,
bot-blocked, unreachable and unqueried (§Boundary 3). **As knowable by the end of the window (2010-2012):
three third-party datapoints, all of them recited by the company itself.**

### H.1 The market, as the window's last documents could state it

| Variable | Value | Third-party carrier and its date | Company's own caveat | Confidence |
|---|---|---|---|---|
| Total worldwide advertising spending, 2010 | $588 billion | "According to an IDC report dated August 2011" | "We have not independently verified the accuracy or completeness of the data contained in these industry publications and reports." | Medium (Tier-3 report, recited in a Tier-1 document) |
| Its offline share | "Television, print, and radio accounted for $363 billion, or 62% of the total advertising market in 2010 according to an IDC report dated August 2011." | same | same | Medium |
| The company's share of attention | "Facebook.com has been the number one online property accessed through personal computers worldwide as measured by total minutes spent and total page views, according to a comScore Media Metrix report dated February 2012" | comScore Media Metrix, Feb 2012 | same caveat; the sentence sits in Business, not in an audited note | Medium |
| Aggregate time | "users in the aggregate spent more than 10.5 billion minutes per day on Facebook on personal computers during January 2012. Aggregate minutes per day increased 57% and average minutes per user per day increased 14% during January 2012 compared to January 2011." | same report | same | Medium |
| Company revenue against that market | FY2011 revenue $3,711 million against 2010 worldwide advertising spend of $588 billion | 424B4 | the two figures are from different years, different bases and different sources | **ESTIMATE / DERIVED only if anyone divides them; this volume does not, and no held document does** |

**Why the $588 billion is not a founding fact.** The IDC report is dated **August 2011** and measures **2010**.
Reading it back into 2004 is the exact contamination §6 forbids: an entrant in 2004 could not have known it,
and the corpus contains no 2004-vintage market statement to substitute. The right use of the row is
diagnostic: by 2011-2012 the company could commission a self-description in which its own revenue was a small
slice of an enormous addressable pool — that is a **2012 argument about 2012**, and it is also a warning
against writing "the market was obviously huge" as if the size justified the entry.

### H.2 What the in-period knowable set excludes, stated as a null with its route

| Excluded | Why | Status |
|---|---|---|
| Any count of social-network users, sites or revenues for 2004-2006 | family (b) refused three times and returned zero timestamps; families (c)/(d) refused or were never queried; no configured route exists for the college press in `periodical_harvest.py`'s five families | **UNANSWERED, not empty** — the probe calls this "a genuine methodological gap for every 2000s-founded company in the fleet, not just this one", and this pass found no route around it |
| Any pricing or inventory market for the product's early supply side | the first advertising-pricing evidence in the corpus is 2011-2012 (campaign examples and the "we do not currently directly generate meaningful revenue" mobile sentence) | **UNKNOWN for 2004-2006** |
| Whether the 2006 New Yorker item in the harvest index bears on any of this | metadata only; `snippet_or_hitcount` carries no text; the row is a pointer to a volume, not a passage | **UNTRIED at the text layer** |

### H.3 Coda, with its mechanism named

What the window's evidence supports about *market* is narrow and slightly paradoxical: the company's own
filing, in the last months of the window, asserts leadership of a measured category (minutes spent) while
disclaiming verification of the industry data around it, and asserts a large addressable pool while
generating "substantially all" revenue from one category inside it. **Mechanism, as the documents state it:**
advertisers pay because users return; the company's leverage is attention it measures itself. **Alternative
explanation that the corpus cannot exclude:** the measured attention and the disclosed 5-6% duplicate-account
estimate (§F.2) sit in the same document, and no held third party counts users, so an alternative reading —
that the category leadership was as self-measured as the category size was self-disclaimed — is available and
unresolved. **Confidence: Medium on the printed facts, UNKNOWN on the underlying magnitudes.**

### H.4 Claim records for §H

P1-26 Claim: The prospectus's market sizing rests on two named third-party reports whose dates are printed, and the company disclaims verifying them. — Date: 2011-08 (IDC) / 2012-02 (comScore) — Source: 424B4 Industry Data and User Metrics; Business; Market Opportunity — Source date: 2012-05-18 — URL: as P1-01 — Archived: UNKNOWN — Tier: 1 (the recital) / 3 (the underlying reports, not held) — Class: RESTATED third-party estimate — Passage: "According to an IDC report dated August 2011, total worldwide advertising spending in 2010 was $588 billion." — Conf: Medium — Corroboration: 0 independent (neither report is held) — Conflicts: None

P1-27 Claim: No held document contains any market statement from 2004-2006. — Date: 2004-2006 — Source: this volume's family-by-family census — Source date: 2026-10-06 — URL: local — Archived: not applicable — Tier: — (a null across four families' held bytes) — Class: UNKNOWN / TRIED–UNANSWERED — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High on the absence in these files — Corroboration: not applicable — Conflicts: **U.7**

## I

STATUS: WRITTEN 2026-10-06

### I.1 Competition as the registrant itself framed it, at the end of the window

The prospectus's competition passage is the fullest named field in the corpus, and it is worth quoting whole
because what it *omits* is as informative as what it includes:

> "We compete broadly with Google's social networking offerings, including Google+, and also with other,
> largely regional, social networks that have strong positions in particular countries, including Cyworld in
> Korea, Mixi in Japan, Orkut (owned by Google) in Brazil and India, and vKontakte in Russia. We would also
> face competition from companies in China such as Renren, Sina, and Tencent in the event that we are able to
> access the market in China in the future."

| Rival named | Where named | What the naming establishes |
|---|---|---|
| Google's social offerings (Google+), Orkut | 424B4 Risk Factors, Business | a two-front rivalry with the largest search advertiser, one of them owned by the same parent, in Brazil and India — the same two countries where the company reports its fastest user growth |
| Cyworld (Korea), Mixi (Japan), vKontakte (Russia) | same | the company describes itself as competing against **regional incumbents**, not against a single global peer |
| Renren, Sina, Tencent (China) | same, conditional on entry | a market the company had **not** entered as of 2012 |
| "traditional and online media businesses for advertising budgets" | same | the revenue competition is for budget, not for users |
| Twitter, LinkedIn, StudiVZ, Odnoklassniki, Mail.ru, kaixin001, 51.com, MySpace | Ex-10.13 (Zynga addendum), effective 2010-12-26 | a **contractual** enumeration, by two counterparties, of the category "Social Platforms" — the only competitive set in the corpus that appears in an instrument rather than in prose |

### I.2 The competitor that was also a claimant

The register adds a rival the prose never mentions: **ConnectU / Connectu, Inc.**, whose corporate person
filed against Mr Zuckerberg on 2004-09-02 (contract), sued **Facebook, Inc.** for copyright infringement on
2007-03-28, and was removed to federal court at the registrant's own petition on 2007-03-09. In the ordinary
retelling this is pure grievance; in this corpus it is also the **only in-window evidence of an actual
competing product with a corporate person, in the founding year and in the same category** — and it comes
from a source that is not the founder's account. It does not establish who copied whom, whether a prior
product existed before the registrant's, or what any of the plaintiffs' claims were worth: **the pleadings
are unheld** (F-3), and the prospectus's silence means the company never printed an answer (**U.4**).

### I.3 Measured null: the rivals the corpus will not name

`Friendster` **0 hits**, `Bebo` **0 hits** across all 31 stored SEC documents and the 7 stored periodical
texts. `MySpace` occurs **twice**, and both occurrences are in the Zynga addendum's list, not in the
company's competition prose. `LinkedIn` occurs 14 times, almost all of them in director biographies and one
in the addendum. **Consequence:** the standard "2004 social-network landscape" (Friendster, MySpace, Bebo,
Classmates, LiveJournal) **cannot be sourced from this corpus at all**, and any §I or Stage-2 sentence that
describes Facebook's entry against those incumbents must be labelled Tier-4 or UNTRIED at the text layer.
The routes that could name them are the same three as §H.2.

### I.4 Claim records for §I

P1-28 Claim: The registrant's own competition statement names Google's social offerings and four regional networks, and conditions any Chinese rivalry on entering China. — Date: 2012-05-18 — Source: 424B4 Risk Factors / Business — Source date: 2012-05-18 — URL: as P1-01 — Archived: UNKNOWN — Tier: 1 — Class: FACT as disclosed; CONTEMPORANEOUS for 2012, useless for 2004 — Passage: "We compete broadly with Google's social networking offerings, including Google+, and also with other, largely regional, social networks that have strong positions in particular countries, including Cyworld in Korea, Mixi in Japan, Orkut (owned by Google) in Brazil and India, and vKontakte in Russia." — Conf: High — Corroboration: 1 lineage — Conflicts: None

P1-29 Claim: A competing social-network company sued the registrant for copyright infringement in 2007 and had sued its founder over company ownership in 2004. — Date: 2007-03-28; 2004-09-02 — Source: CourtListener register, 1:07-cv-10593 and 1:04-cv-11923 — Source date: payload 2026-09-26; events 2004-2007 — URL: local bytes `sources/legal/cl2_%22ConnectU%22.json` — Archived: UNKNOWN — Tier: 1 — Class: FACT about the register; claim content UNKNOWN — Passage: NO_VERBATIM_PASSAGE_RECORDED (field values `caseName` "Connectu, Inc. v. Facebook, Inc.", `dateFiled` "2007-03-28") — Conf: High on the entries — Corroboration: 1 register, 2 dockets — Conflicts: **U.4**

P1-30 Claim: The corpus cannot name the pre-2008 social-network incumbents usually cited as Facebook's competition. — Date: 2004-2007 — Source: string census of stored bytes — Source date: 2026-10-06 — URL: local — Archived: not applicable — Tier: — (a measured null) — Class: UNKNOWN / UNTRIED — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High on the absence — Corroboration: not applicable — Conflicts: **U.4**

## J

STATUS: WRITTEN 2026-10-06

### J.1 Technology as the window's last documents describe it

| Layer | As printed in the 424B4 | Class | Confidence |
|---|---|---|---|
| Language and performance | "Facebook.com is largely written in PHP, or Hypertext Preprocessor, a widely used, general-purpose scripting language. We developed HipHop, which programmatically transforms PHP source code into highly optimized C code." | FACT as disclosed (2012 state of the stack) | High |
| Media storage | "We have built a number of storage and serving technologies, such as Haystack, which allow us to efficiently serve and store the data." | FACT as disclosed | High |
| Data management | "We developed Apache Hive, a data warehouse infrastructure built on top of Hadoop, to provide tools to enable easy data summarization, ad hoc querying, and analysis of large datasets." | FACT as disclosed | High |
| Open contributions | "we have contributed certain specifications and designs related to our data center equipment to the Open Compute Project Foundation… under the Open Web Foundation License" | FACT as disclosed | High |
| Method of invention | "Many of our most successful products came out of hackathons, including Timeline, chat, video, our mobile development framework and some of our most important infrastructure like the HipHop compiler." — and "we require all new engineers — even managers whose primary job will not be to write code — to go through a program called Bootcamp where they learn our codebase, our tools and our approach" | FOUNDER CLAIM (it is the letter's account of process, and it dates what it names to no year) | Medium as printed; **UNKNOWN whether hackathons existed in 2004-2006** |
| Patents | "As of March 31, 2012, we had 774 issued patents and 546 filed patent applications in the United States and 96 corresponding patents and 194 filed patent applications in foreign countries relating to social networking…" | FACT as disclosed | High |
| IP inputs | the company's protection rests on "patents, patent applications, trademarks, copyrights, trade secrets, including know-how, license agreements, confidentiality procedures, non-disclosure agreements with third parties, employee disclosure and invention assignment agreements, and other contractual rights" | FACT as disclosed | High |
| Engineer supply | "We have also made and intend to make acquisitions with the primary objective of adding software engineers, product designers, and other personnel with certain technology expertise." | FACT as disclosed | High |

### J.2 The technology of 2004-2006: an unbroken silence, and the one dated exception

There is **no held statement, screenshot, datasheet, changelog, code artifact, or first-deployment record for
the founding technology.** The stack above is a 2012 description of a system that had already been rewritten
several times over; using it to characterise 2004 is the anachronism §6 forbids, and no inference from the
2012 stack to a 2004 architecture is licensed here (**"mechanism UNKNOWN"** in §J.4 terms).

The one exception is dated by an instrument rather than by prose: **Ex-10.2, the 2005 Stock Plan**, whose
printed amendment headers run "(as amended April 2006) (as amended July 2006) (as amended April 2007) (as
amended May 2007) (as amended July 2007) (as amended September 2007) (as amended October 2007) (as amended
December 2007) (as amended twice in August 2008)". A stock plan amended eleven times in three years is a
record of a hiring engineering organisation that needed new grant terms as it grew — which is *capacity*
evidence, not *capability* evidence: it does not say what anyone built. The plan also carries the corpus's
only "thirty days" (§D.4), a reminder that in this company's bytes that phrase belongs to equity mechanics.

### J.3 Independence and provenance notes for this section

The technology description is a **single lineage's self-report written to satisfy disclosure liability**, with
the risk factors' own admission that open-source contributions may force licensing of "innovations that turn
out to be mature" and that it "depend[s] upon effective operation with mobile operating systems, networks,
and standards that we do not control." No independent technical document — no benchmark, no paper by
non-employees, no conference talk, no code — is held in the corpus for the window. The three arXiv/DTIC/NASA
files under `sources/periodicals/` **do** contain 2010-2012 technical text *about* Facebook (a social-graph
measurement paper whose affiliation line reads "Facebook, Palo Alto, CA, USA"), but `A4_harvest_mine.md`
classifies them `BARE_WORD_MATCH`, and this volume treats them as pointers only: they date the company's
*research visibility*, not its technology, and they are outside the origin years.

### J.4 Coda under §16 (evidence, mechanism, alternative, confidence)

**Evidence:** the only technology facts in the window are 2012 self-descriptions plus one 2005-dated equity
instrument. **Mechanism (as the documents state it):** the company attributes its own outputs to hackathons,
a required onboarding programme, and acquisitions made "with the primary objective of adding software
engineers" — i.e. it describes technology production as an organisational habit, not as a founding artifact.
**Alternative explanation the corpus cannot exclude:** every one of those habits is documented only after the
company was large, so the direction of causation between "hackathon culture" and the company's success is
unestablished and, on this evidence, **UNKNOWN — no mechanism is asserted for 2004.** **Confidence:** High on
the 2012 printings, Medium on the 2005 capacity inference, UNKNOWN on everything about the founding stack.

### J.5 Claim records for §J

P1-31 Claim: The registrant described its 2012 stack as PHP transformed by its own HipHop compiler, with Haystack for media storage and Apache Hive on Hadoop for data management. — Date: 2012-03-31 (state); 2012-05-18 (printing) — Source: 424B4 Business, Technology — Source date: 2012-05-18 — URL: as P1-01 — Archived: UNKNOWN — Tier: 1 — Class: FACT as disclosed; RESTATED for anything earlier — Passage: "We developed HipHop, which programmatically transforms PHP source code into highly optimized C code." — Conf: High — Corroboration: 1 lineage — Conflicts: None

P1-32 Claim: The only 2005-dated artifact of technical capacity in the corpus is an equity plan with an eleven-amendment trail. — Date: 2005 (plan year); as filed 2012-02-08 — Source: Exhibit 10.2, 2005 Stock Plan — Source date: 2012-02-08 — URL: https://www.sec.gov/Archives/edgar/data/0001326801/000119312512046715/d287954dex102.htm — Archived: UNKNOWN — Tier: 1 — Class: FACT (instrument); the capacity reading is INFERENCE — Passage: "FACEBOOK, INC. 2005 STOCK PLAN (as amended April 2006) (as amended July 2006) (as amended April 2007)" — Conf: High as an instrument; Medium as capacity evidence — Corroboration: 1 — Conflicts: None

P1-33 Claim: No held document describes the technology of the founding period. — Date: 2004-2006 — Source: census of `sources/` — Source date: 2026-10-06 — URL: local — Archived: not applicable — Tier: — (a measured null) — Class: UNKNOWN, TRIED–UNANSWERED on family (b), UNQUERIED on (d) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High on the absence — Corroboration: not applicable — Conflicts: **U.5**

## Register rows for merge

STATUS: WRITTEN 2026-10-06

*Emit-only. **No register CSV on this company was opened, created or edited by this pass** — the company root
holds no `.csv` at all (only `research/`, `sources/`, `_parts/`), and a merge applies these rows with
`tools/id_mint.py` minting the global ids. `stage` is the controlled literal **`stage1`** on every row (§13).
All `P1x` ids are dossier-local. Two conventions the merge should know before it parses:*

1. ***One lineage, six rows of it.** The S-1 of 2012-02-01, its amendments of 2012-02-08 → 2012-05-15, the
   424B4 of 2012-05-18 and their filed exhibits are **one source** (§3). `independence_note` says so on every
   registration row. Corroboration counts in these rows are counts of **independent origins**, never of files.*
2. ***Quotation rendering.** Passages are transcribed from the stored HTML after tag and entity stripping.
   The filings' typographic apostrophes, quotation marks and the `+` in `Google+` are encoded as entities that
   disappear in the stored bytes, so a literal string comparison must use punctuation-squashed matching (the
   same rule `tools/gates.py` applies in `_squash`). Ellipses mark omitted text; nothing inside quotation marks
   is paraphrase.*

*Overlap note for the merge: rows below are limited to what §A–§J asserts. §P's quantitative table and §K's
financing series belong to `s1-meta-p2`; where p2 emits the same filed figures, p2's rows should be canonical
and these are the earlier claim of record — deduplicate by (date, metric, source), not by row id.*

### sources.csv — `source_id,stage,claim_supported,source_title,author_or_publication,source_type,primary_or_secondary,event_date,publication_date,access_date,url,archived_url,tier,evidence_class,confidence,independence_note,relevant_passage,notes`
> **[MERGE 2026-10-07]** The 11 row(s) this `sources.csv` block emitted were applied to `sources.csv` and are **not reprinted in this volume**: `_parts/s1_p1.md` stays the emission of record, and a second copy would read to `tools/merge_census.py` as new rows. Live keys and the local-tag map are in the register-application record at the foot of this file.

### quantitative.csv — `company,stage,date,metric,value,unit,source,source_date,evidence_class,confidence,derived_arithmetic,notes`
> **[MERGE 2026-10-07]** The 30 row(s) this `quantitative.csv` block emitted were applied to `quantitative.csv` and are **not reprinted in this volume**: `_parts/s1_p1.md` stays the emission of record, and a second copy would read to `tools/merge_census.py` as new rows. Live keys and the local-tag map are in the register-application record at the foot of this file.

### timeline.csv — `company,stage,date_or_range,event,actors,location,source_id,evidence_class,confidence,conflict_ref,notes`
> **[MERGE 2026-10-07]** The 22 row(s) this `timeline.csv` block emitted were applied to `timeline.csv` and are **not reprinted in this volume**: `_parts/s1_p1.md` stays the emission of record, and a second copy would read to `tools/merge_census.py` as new rows. Live keys and the local-tag map are in the register-application record at the foot of this file.

### decisions.csv — `company,stage,date,decision,state_before,information_available,unknowns,alternatives,constraints,rationale,expected_result,actual_result,source_id,confidence,claim_ref`
> **[MERGE 2026-10-07]** The 3 row(s) this `decisions.csv` block emitted were applied to `decisions.csv` and are **not reprinted in this volume**: `_parts/s1_p1.md` stays the emission of record, and a second copy would read to `tools/merge_census.py` as new rows. Live keys and the local-tag map are in the register-application record at the foot of this file.

### validation.csv — `company,stage,date,signal_or_failure,magnitude,what_it_demonstrated,what_it_did_not_demonstrate,source_id,evidence_class,confidence,notes`
> **[MERGE 2026-10-07]** The 6 row(s) this `validation.csv` block emitted were applied to `validation.csv` and are **not reprinted in this volume**: `_parts/s1_p1.md` stays the emission of record, and a second copy would read to `tools/merge_census.py` as new rows. Live keys and the local-tag map are in the register-application record at the foot of this file.

### failures.csv — `company,stage,date,signal_or_failure,magnitude,what_it_demonstrated,what_it_did_not_demonstrate,source_id,evidence_class,confidence,notes`
> **[MERGE 2026-10-07]** The 5 row(s) this `failures.csv` block emitted were applied to `failures.csv` and are **not reprinted in this volume**: `_parts/s1_p1.md` stays the emission of record, and a second copy would read to `tools/merge_census.py` as new rows. Live keys and the local-tag map are in the register-application record at the foot of this file.

### channels.csv — `company,stage,channel,date_tested,why_tested,cost_or_effort,result,repeatability,source_id,confidence,notes`
> **[MERGE 2026-10-07]** The 4 row(s) this `channels.csv` block emitted were applied to `channels.csv` and are **not reprinted in this volume**: `_parts/s1_p1.md` stays the emission of record, and a second copy would read to `tools/merge_census.py` as new rows. Live keys and the local-tag map are in the register-application record at the foot of this file.

### conflicts.csv — `company,stage,conflict_id,section,claim_a,claim_a_source,claim_a_date,claim_b,claim_b_source,claim_b_date,why_they_differ,evidence_weight,best_supported_interpretation,residual_uncertainty,confidence`
> **[MERGE 2026-10-07]** The 7 row(s) this `conflicts.csv` block emitted were applied to `conflicts.csv` and are **not reprinted in this volume**: `_parts/s1_p1.md` stays the emission of record, and a second copy would read to `tools/merge_census.py` as new rows. Live keys and the local-tag map are in the register-application record at the foot of this file.

### data_gaps.csv — `company,stage,gap,why_missing,importance,best_available_evidence,confidence,follow_up_task`
> **[MERGE 2026-10-07]** The 11 row(s) this `data_gaps.csv` block emitted were applied to `data_gaps.csv` and are **not reprinted in this volume**: `_parts/s1_p1.md` stays the emission of record, and a second copy would read to `tools/merge_census.py` as new rows. Live keys and the local-tag map are in the register-application record at the foot of this file.

**Row count requested: 99** — sources 11 · quantitative 30 · timeline 22 · decisions 3 · validation 6 ·
failures 5 · channels 4 · conflicts 7 · data_gaps 11. Every conflict row has its `U.1`–`U.7` anchor declared in
this volume's narrative (§Boundary 8 plus the section where each is adjudicated), and every block was written
from a line opened in this session. **No row here assumes a global `source_id` (RD-123): minting is the
merge's.** All rows carry `stage` = `stage1` (§13 register vocabulary) and each block was re-parsed through a
CSV reader after writing; the width check is recorded in `_parts/NOTES_meta_p1.md`.

## Untried

STATUS: WRITTEN 2026-10-06

**Tried and answered, so it is not repeated here:** family (a) filings read across 31 stored documents; the
EDGAR enumeration to 397 pre-2014 rows; the CourtListener register at two query keys; the XBRL early series
(215 rows, nothing before 2010); the harvest index (30 rows); the stored periodical texts (7 files).

1. **Delaware Division of Corporations** — certified copy of the original certificate filed 2004-07-29 as
   TheFacebook, Inc., plus the founding-era authorised-share structure. THE HIGHEST-VALUE UNTRIED ROUTE IN
   THIS STAGE: it is the only instrument that can convert §Boundary 1 row 1 from a recital into a record
   (**U.1**), and the only place the 2004 capitalisation exists. (F-2)
2. **Wayback CDX, one call each** — `thefacebook.com` and `facebook.com`, bare host and `www` as one test, plus
   the first-capture timestamp. The service refused three times in the probe session and this pass made no
   further request (web budget at the §14.2 cap). **Nothing in this corpus can date the launch until it
   answers.** (F-1)
3. **RECAP / PACER docket text** — the complaints in 1:04-cv-11923, 1:07-cv-10593, 5:07-cv-01389, 07-1796,
   1:08-cv-00862 and the Ceglia matters. These are the earliest *independent* narratives of 2003-2004 anywhere
   reachable, and the register is already proven. (F-3)
4. **The six `UPLOAD` / `.paper` items and the 2005-2006 REGDEX cluster** — the only route to attributing the
   earliest CIK activity, and the only way to close or kill **U.3**.
5. **The five `CORRESP` comment letters (2012-03-27, 05-14, 05-15, 2013-04-30 and one more)** — the likeliest
   place in EDGAR to find what the staff asked about the founding account and the undisclosed disputes. (F-5)
6. **OCR of the 26 `g287954g*.jpg` figures in acc. 0001193125-12-034517**, including the "Our History"
   graphic — the only path from the company's own pictorial timeline to citable text.
7. **The Harvard / student press for 2003-2006** — no configured route exists among
   `periodical_harvest.py`'s five families; a genuine fleet-level gap, not this company's.
8. **Family (e), auction and museum documentary records** — deliberately never attempted by the probe and
   still untried; the one skip that cannot be blamed on an outage.
9. **The FY2012 10-K (acc. 0001326801-13-000003, filed 2013-02-01)** — enumerated in the index but **not stored
   under `sources/sec/`**, so no part of this dossier has read it; it is the only in-lineage document that
   restates FY2011 against a full year of public-company reporting.
10. **The amendment bodies beyond the origin strings** — this pass read the eight stored S-1/A bodies for
    origin-critical strings and the exhibit set in full; it did **not** read their financial statements,
    share-ownership tables or underwriting sections, which §K, §N and §P (part 2) will need.
11. **Zynga's, the landlord's and the banks' own filed copies** of the three counterparty instruments (§G.3) —
    the cheapest available independence test in this stage.

>>> FETCH REQUEST <<<

**F-1** `tools/cdx_intake.py` (or one CDX call each) — `url=thefacebook.com` and `url=facebook.com`,
`from=2003&to=2008`, output to `company_017_meta/sources/web/`. Family (b) has never answered for this
company; the launch date, the first page and the first product description all sit behind this one request.

**F-2** Delaware Division of Corporations — certified copy / good-standing order for **TheFacebook, Inc.,
filed 2004-07-29**, plus the founding authorisation. Bytes to `company_017_meta/sources/legal/`. Only route to
a record-grade formation day and the 2004 share structure (**U.1**).

**F-3** RECAP/PACER docket text — complaints and answers in `1:04-cv-11923`, `2:06-cv-01640`, `5:07-cv-01389`,
`1:07-cv-10593`, `07-1796`, `1:08-cv-00862` and the Ceglia matter (W.D.N.Y.). Bytes to
`company_017_meta/sources/legal/`. The earliest independent narrative of 2003-2004 (**U.4**).

**F-4** EDGAR paper items on CIK 1326801 — the 6 `UPLOAD` / `.paper` documents behind `9999999997-05-023236`
and its REGDEX siblings, and the 2008 `NO ACT`. Bytes to `company_017_meta/sources/sec/`. Settles **U.3**.

**F-5** EDGAR `CORRESP` letters and their `UPLOAD` responses for accessions in 2012-03-27, 2012-05-14 and
2012-05-15. Bytes to `company_017_meta/sources/sec/`. Tests whether the staff asked about the origin account or
the undisclosed disputes (data_gaps row 7).



---

# PART 2 BODY — `_parts/s1_p2.md`, applied to this volume verbatim (§K–§U, claim records, registers pointer). Section letters and anchors are the author's and were not renumbered; the seven merge annotations inside it, `[MERGE 2026-10-07 …]` or `[MERGE: …]`, at §K.2, §K.5, §Q.1, §U.1 twice, §U.4 and §U.6, are the merge's: each follows the sentence it supersedes, adds nothing to it and deletes nothing from it.


## K

**K. Money / personal finances** — Stage-1 boundary is origin → **July 2004** (the Delaware incorporation,
fixed by the S-1; see §U.5 and §U.7, and part 1's boundary section). Everything here is judged against what a Stage-1
reader could have known about money at or before formation, which is nearly nothing in the held corpus.

**K.1 The registrant's own money is a filed void inside Stage 1.** `sources/_index/submissions_pre2014.csv`
enumerates every CIK 1326801 filing with `filingDate ≤ 2013-12-31` (397 rows, from two archive slices that
both returned HTTP 200). The **oldest row is 2005-05-06**, a `REGDEX` paper item of unattributed origin
(§U.3). There is **no filing of any form dated in 2004 on this CIK** — no capitalisation statement, share
structure, subscription proceeds or bank line for the incorporation year exists in EDGAR. This is a *true null
from a complete enumeration*, not a failed request. Founding capital, authorised shares and consideration at
July 2004 are **UNKNOWN** from the filings family.

**K.2 The charter that would carry the share structure is not in the record.** The S-1 accession's file list
(`sources/_index/S1_accession_filelist.txt`) is the complete item set of accession 0001193125-12-034517; the
only exhibit is `d287954dex231.htm`, an auditor consent. There is **no certificate-of-incorporation exhibit**
in the accession, and none anywhere in `sources/`. So the authorised-share structure, par value and the
day-level incorporation date are unobtainable from EDGAR permanently; the route that could fix them is the
**Delaware Division of Corporations** (UNTRIED — see §S and `## Untried`), not another SEC document. [MERGE 2026-10-07 — **SUPERSEDED IN PART, paragraph kept as written** (§14 rule 7): the sentence "There is no certificate-of-incorporation exhibit in the accession, **and none anywhere in `sources/`**" and the clause "the day-level incorporation date [is] unobtainable from EDGAR permanently" are refuted by bytes neither part-2 read opened. **Exhibit 3.3 of accession 0001193125-12-175673 (the S-1/A of 2012-04-23), stored at `sources/sec/0001193125-12-175673_d287954dex33.htm` and fetched 2026-09-29, recites: "The date of filing its original Certificate of Incorporation with the Secretary of State was July 29, 2004, under the name TheFacebook, Inc."** So EDGAR *does* fix the founding day, at the registrant's own recital. What survives of this paragraph is its narrower and still-correct half: the S-1 accession 0001193125-12-034517 carries exactly one exhibit, the auditor consent `d287954dex231.htm`; no **executed** charter and no founding-era share structure is in EDGAR, because Ex-3.3 is a **form** whose `Dated:` line and signature block are blank. That is why the day travels at **Medium**, not High, and why the Delaware registry (FETCH REQUEST F-2) remains the upgrade route. Registered at **U.1** (part 1's row canonical), carried as claim record `P1-03`/`P1-18` and source `S4497`; see COR-03.]

**K.3 The only money-adjacent statement about pre-incorporation work is an adversary's.** Both the S-1 and the
final prospectus disclose the Ceglia litigation and, inside it, plead a date earlier than July 2004. Verbatim
(S-1, Legal Proceedings): *"Paul D. Ceglia filed suit against us and Mark Zuckerberg on or about June 30,
2010 … claiming substantial ownership of our company based on a purported contract between Mr. Ceglia and Mr.
Zuckerberg allegedly entered into in April 2003."* The 424B4 prints the same paragraph; per §3 that is the
**same registration lineage**, not a second witness. The April-2003 contract is **pleaded by an adversary and
characterised by the registrant as fraudulent** — the company states it filed a motion *"showing that the
alleged contract and emails upon which Mr. Ceglia bases his complaint are fraudulent."* Stage-1 posture: the
2003 agreement is *alleged*, not established; it attaches to **Zuckerberg personally**, not to Facebook, Inc.
(§U.2); and no dollar amount or consideration is in evidence.

**K.4 Founder personal finances at formation are UNKNOWN.** Nothing in `sources/` states any co-founder's
personal capital contribution, outside income or living situation at or before July 2004. The dorm-room /
angel-capital story reaches this corpus only as retrospective founder-account literature (post-2011 titles in
`sources/_harvest/google_books/`), which is `RETROSPECTIVE SOURCE` material for 2004 (§6) and admissible only
for **how the money story was later told**, never for what money moved. Recorded as a High-importance gap.

**K.5 Where the filings *do* print money, it is five years past the boundary and restated.** The earliest
audited period anywhere in the registrant documents is **FY2009** — the S-1's Selected Consolidated Financial
Data covers *"the years ended December 31, 2009, 2010 and 2011."* The business-overview paragraph carrying the
incorporation sentence also prints FY2011 scale (*"… net income of $1,000 million. We were incorporated in
July 2004 and are headquartered in Menlo Park, California."*; revenue $3,711M, operating income $1,756M in the
same clause). These are **Stage-2 facts, RESTATED, out of the Stage-1 window**; §6 forbids importing them as
Stage-1 money, so they are excluded from the Stage-1 §P table and appear only to date the earliest quantitative
record and size the gap. (The `845 million` MAU figure the probe cited was **not found in the held S-1 text**
and is therefore not asserted here.) [MERGE 2026-10-07 — **REFUTED BY THE BYTES, sentence kept as written**: the figure *is* in the held S-1 text, printed as `845&nbsp;million` **eleven times**, so a literal `grep` for "845 million" returns 0. Measured context: "We had 845 million MAUs as of December 31, 2011, an increase of 39% as compared to 608 million MAUs as of December 31, 2010." This is the same non-breaking-space artifact part 1 recorded for `July&nbsp;29,&nbsp;2004`, and part 1's quantitative row (now `quantitative.csv`, 2011-12-31 monthly_active_users = 845) is verified by it. Nothing changes in this paragraph's argument: the figure is a **2011 restatement** and stays out of the Stage-1 §P table; only its status as "not found" is corrected. See COR-03.]

STATUS: WRITTEN 2026-10-07

## L

**L. Validation signals** — evidence, in-period, that the July-2004 entity's idea was being taken up.

**L.1 No contemporaneous 2004 traction metric exists in the held corpus.** There is no user count, adoption
number, registration count, revenue line or usage statistic printed anywhere in `sources/` for the period up
to July 2004. The registrant documents postdate the window by ~7.5 years and their earliest metric-bearing
period is FY2009–FY2011 (see §K.5); the S-1 narrates the founding era only through an un-extractable graphic
(§S.3). Every family that could have carried an in-period count — Wayback capture dates (family b, UNANSWERED:
HTTP 504/503, service self-declared "Temporarily Offline", bodies at `sources/web/cdx_*.txt`), student/college
press (family c, one in-window Google Books record, metadata only), corporate print (family d, UNQUERIED),
auction/museum (family e, UNTRIED) — returned nothing usable. Stage-1 validation is therefore **UNKNOWN as a
quantity**, not weak: nothing was measured on the record and reported here.

**L.2 The one externally-generated, dated signal that something had been built and was being fought over is
the federal docket.** `sources/legal/cl2_%22ConnectU%22.json` carries `ConnectU LLC v. Zuckerberg`,
docket **1:04-cv-11923**, D. Mass., `dateFiled` **2004-09-02**, cause of action `28:1332
Diversity-Breach of Contract`. This is Tier 1 (§5 court records), **independent of the founder account**, and
machine-dated. It is a *terminus ante quem*: by early September 2004 a plaintiff alleged a contractual claim
to ownership of a venture Zuckerberg was involved in — which is indirect evidence of a real, contested asset,
not a positive validation metric. Note the filing date sits just **after** the July 2004 boundary, so it is
strictly the opening of Stage 2 seen from Stage 1's edge; it is used here as the earliest *independent* trace
of the venture's existence, and its Stage-1/Stage-2 placement is itself recorded (§U.4, §U.7).

**L.3 What L.2 demonstrates vs. does not.** It demonstrates: (a) a venture connected to Zuckerberg existed by
2004-09-02; (b) an outside party claimed a contractual interest in it. It does **not** demonstrate: user
adoption, product quality, revenue, that "Facebook" the July-2004 entity was the venture at issue, or the
validity of the plaintiff's ownership claim (denied and, by the company, alleged fraudulent). Magnitude:
UNKNOWN — a suit filing is not a traction number. Mechanism linking it to product uptake: **UNKNOWN**.

STATUS: WRITTEN 2026-10-07

## M

**M. Negative signals / failures** — things that had already gone wrong or were contested at or before the
July-2004 boundary.

**M.1 An ownership dispute over the venture existed inside the founding year.** The register in
`sources/legal/cl2_%22ConnectU%22.json` shows `ConnectU LLC v. Zuckerberg` filed **2004-09-02** (1:04-cv-11923,
D. Mass., breach-of-contract). Contemporaneous negative signal: the venture's ownership was contested almost
immediately after incorporation. The complaint's text is not held (only the docket register), so the specific
allegation is UNKNOWN; the *existence and date* of the dispute are FACT (§5 court records).

**M.2 A claim to pre-incorporation authorship was pleaded against the founder personally.** The Ceglia matter
(§K.3) alleges an April-2003 contract — before the July-2004 incorporation — claiming "substantial ownership."
The registrant's own posture is that the emails/contract are *fraudulent* (its July 1 2011 motion was granted,
per the S-1). Two facts are in tension and both are Tier-1-sourced: the company *named* Ceglia in the S-1 and
424B4 (verified present in both files) while *naming no other origin claimant*. Stage-1 negative signal: even
as the entity formed, there was an unresolved, later-litigated dispute about who built what and when.
**Not established** — an adversary's allegation, denied; recorded as pleaded, not proven.

**M.3 The company's own filings conceal the origin disputes entirely.** Across the S-1 (2,627,678 B) and the
424B4 (3,545,401 B) the strings `Winklevoss`, `ConnectU`, `Divya`, `Saverin`, `Eduardo`, `Moskowitz`,
`thefacebook`, `Harvard College` all return **0 hits** (string counts, both files) — while the federal register
shows those suits filed 2004 → 2007 and appealed 2007. This is a *negative of disclosure*, not of evidence: it
means no Stage-1/Stage-2 agent may write "the early equity disputes were disclosed in the S-1." The docket
outranks the prospectus here (§U.4).

**M.4 Record-selection null (§2): the winners' archive is the one that was kept.** For 2004 there is no
internal deliberation, no rejected option, no contemporaneous count and no independent failure record on disk —
EDGAR is empty through 2011 and the web/periodical/auction families were never reachable this run. A
reconstruction that leans only on the survivor's 2012 filings would read as a story about a future winner; the
honest Stage-1 finding is that **the negative space of 2004 (what was tried and abandoned, what failed, what
was measured) is unrecoverable from this corpus**, and is named as such rather than filled with hindsight.

STATUS: WRITTEN 2026-10-07

## N

**N. Founder decisions (mandatory section)** — decisions attributable to the founder(s) at or before the
July-2004 boundary. The evidence base is the worst-possible for decision history: no board minutes, no
internal memo, no contemporaneous email and no pre-2012 filing is in `sources/`, so every cell below that is
not directly printed is **UNKNOWN**, and alternatives/rationale are **NOT KNOWABLE** in-period rather than
merely un-retrieved. `UNKNOWN` here is the deliverable (§2, §15.2).

| Date | Decision | State before | Information available | Unknowns | Alternatives | Constraints | Rationale | Expected result | Actual result | Evidence | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2004-07 | Form/cause to be incorporated a Delaware corporation (Facebook, Inc.) | An unregistered venture is alleged to have existed (Ceglia pleads work from April 2003); no corporate record before 2005-05-06 | Only the restated S-1 line "We were incorporated in Delaware in July 2004" | Day-level date; who signed; consideration; share structure; why Delaware | UNKNOWN — no document lists alternatives | UNKNOWN — no charter exhibit | UNKNOWN — no contemporaneous rationale | UNKNOWN | entity exists from July 2004 (month-level) | S-1 Corporate Information + Business (2 statements) | High (that it happened, month-level); UNKNOWN (why/how) |
| ≤ 2004-09 | Proceed with formation while an ownership claim was being asserted | Alleged April-2003 contract (Ceglia); ConnectU's contractual claim ripening into a 2004-09-02 suit | Two Tier-1 records: S-1 Ceglia paragraph (alleged 2003 contract); docket 1:04-cv-11923 dateFiled 2004-09-02 | Whether the founder knew of the claim before forming the entity; whether formation was timed to it | UNKNOWN | the disputes were not resolved pre-formation | UNKNOWN | UNKNOWN | formation proceeded; disputes continued into 2006–2007 litigation | S-1; `cl2_%22ConnectU%22.json` | Medium (a claim existed); UNKNOWN (the decision's internal logic) |
| 2004-07 (onward) | Set founder voting control | — | Only the 2012 restatement that Zuckerberg is "founder, Chairman, and CEO … largest and controlling stockholder" with Class A / Class B control | What control arrangement, if any, existed at July-2004 formation | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | dual-class control documented only as of 2012 | S-1 (restated) | LOW as a Stage-1 fact; High that the 2012 filing says it |

**N.1 Reading discipline.** Row 1 is the single decision the record fixes; rows 2–3 are reconstructed from
records that are *not* decision documents (an adversary's pleading; a 2012 control disclosure). None of these
may be read backwards as a "playbook move": the hindsight firewall (§2) forbids treating an outcome we know
(the entity survived and listed) as proof that any 2004 choice was rational or well-informed. Every rationale
cell above says **UNKNOWN** on purpose; §14.6 / RD-034 forbid implying a mechanism the bytes do not name.

**N.2 Emission note.** These three rows are also emitted in `decisions.csv` (the register), with `claim_ref`
pointing at the K–U claim records and `source_id` left provisional for central minting at merge.

STATUS: WRITTEN 2026-10-07

## O

**O. Counterfactual opportunities** — plausible paths open at or before July 2004 that the record lets us see,
assessed only from knowledge available then (§2 firewall: no use of the later success to rank them).

**O.1 A parallel/competing venture was in play — but under a contested name.** The docket register shows the
opposing party as **ConnectU / Connectu LLC** across 2004–2007 matters (`1:04-cv-11923` … `07-1796`). A
Stage-1 reader who could see the docket would know another social-network venture was being fought over in the
same period; whether the July-2004 entity could have taken that product, name or market path instead of its
own is **NOT KNOWABLE** from `sources/` — the filings mention neither name (`ConnectU` 0, `thefacebook` 0), so
the alternative is visible only through litigation, not through a business record. Class: INFERENCE from an
adversary's existence; confidence LOW.

**O.2 The pre-incorporation collaboration with Ceglia is the clearest concrete "road not taken," and it is an
adversary's account.** The S-1/424B4 plead that Ceglia and Zuckerberg allegedly contracted in **April 2003**
toward a jointly-owned venture that never became this registrant. That is a counterfactual only in the sense
that a claimed 2003 partnership did not mature into the July-2004 Delaware corporation; the registrant calls
the underlying emails fraudulent. Nothing in the corpus shows the founder consciously *chose against* an
opportunity — only that two parties later told incompatible stories about what was agreed. Class: FOUNDER
CLAIM (adversary-side) / RESTATED; confidence LOW; the "opportunity cost" framing is unavailable to a Stage-1
reader and would be hindsight.

**O.3 The ordinary early-stage options (financing, market entry, product scope) are unrankable.** A 2004
internet venture plausibly faced choices about external funding, campus rollout order, and advertising vs.
no-monetisation. But **no Stage-1 document prints any of these as options considered**, and the S-1's history
of the era is an image (see §S.3). Per the record-selection null (§2), the rejected options for 2004 are
unrecoverable because the winners' archive kept only the survivor's account. This section is therefore an
**earned null**: the counterfactual set is UNKNOWN from this evidence, and the routes that could populate it
(Delaware/California registries, RECAP/PACER pleadings, Harvard student press, OCR of the S-1 graphics) are
named in `## Untried`.

STATUS: WRITTEN 2026-10-07

## P

**P. Quantitative metrics table (Stage 1, boundary → July 2004)** — per §8 every value carries its source and
confidence cell; `UNKNOWN` is a complete value. Rows P5–P7 are shown to **date and size the evidence gap**,
not as Stage-1 observations — they sit outside the July-2004 boundary and are labelled `RESTATED` / Stage-2.

| ID | Date | Metric | Value | Unit | Source | Source date | Confidence |
|---|---|---|---|---|---|---|---|
| P1 | 2004-12-31 | Registrant filings on CIK 1326801 dated in 2004 | 0 | filings | `sources/_index/submissions_pre2014.csv` (397-row enumeration) | 2026-09-25 | High (FACT of absence) |
| P2 | 2005-05-06 | Earliest filing on CIK 1326801 (a `REGDEX` paper item, unattributed — §U.3) | 2005-05-06 | ISO date | `sources/_index/submissions_pre2014.csv` | 2026-09-25 | High |
| P3 | 2004-07 | Founding capital / consideration received at incorporation | UNKNOWN | USD | none in `sources/`; route = Delaware SoS charter (UNTRIED) | UNKNOWN | UNKNOWN |
| P4 | 2004-07 | Authorised share capital at formation | UNKNOWN | shares | no charter exhibit in S-1 accession (`S1_accession_filelist.txt`) | UNKNOWN | UNKNOWN |
| P5 | 2004-07 | Users / revenue / customers at the boundary | UNKNOWN | — | no in-period metric anywhere in `sources/` | UNKNOWN | UNKNOWN |
| P6 | 2009-12-31 | Earliest audited period printed in the registrant documents (RESTATED, out-of-window) | FY2009 | fiscal year | S-1 Selected Consolidated Financial Data | 2012-02-01 | High (that it is the earliest); RESTATED |
| P7 | 2011-12-31 | FY2011 revenue (Stage-2, RESTATED; not a Stage-1 value) | 3711 | USD-million | S-1 Business overview, `...d287954ds1.htm` | 2012-02-01 | High (that the S-1 prints it); RESTATED |

**P.1 Gap arithmetic (shown, per §3/ESTIMATE rule).** The earliest quantitative record (P2, a registration
administrivia dated 2005-05-06) is **0.8 years** after the boundary; the earliest *financial* record (P6,
FY2009) is **~4.4 years** after it; the earliest *metric* record (P7) is **~6.4 years** after it. A Stage-1
reader in July 2004 had **no company-generated number on the public record at all.** This table's honest shape
is therefore mostly `UNKNOWN`, and that shape is itself the Stage-1 finding.

STATUS: WRITTEN 2026-10-07

## Q

**Q. Chronological micro-timeline (Stage 1)** — dates carry their basis; a partial date stays partial
(§13). Two markers immediately outside the boundary are shown because they are the nearest independent traces
of the Stage-1 venture; they are labelled with their stage and, where they feed a conflict, the `U.n` anchor.

| Date | Event | Actors | Location | Source | Confidence |
|---|---|---|---|---|---|
| 2003-04 | A contract toward joint ownership is **alleged** (adversary Ceglia's pleading; registrant calls it fraudulent) | Ceglia; Zuckerberg | New York (per Ceglia suit venue) | S-1 Legal Proceedings; 424B4 (same lineage) | Low (pleaded, not proven) — §U.5 |
| 2004-02 | Dorm-room / February founding | — | — | **not in `sources/`** (`February 2004` = 0 hits in S-1 & 424B4) | UNKNOWN — §U.5 |
| 2004-07 | Incorporated in Delaware (Facebook, Inc.) | the registrant | Delaware | S-1, stated twice (`d287954ds1.htm`) | High (month-level only) — §U.1, §U.5 |
| 2004-09-02 | `ConnectU LLC v. Zuckerberg` filed (1:04-cv-11923, breach of contract) — Stage-2 filing, earliest independent trace of the venture | ConnectU LLC; Zuckerberg | D. Massachusetts | `sources/legal/cl2_%22ConnectU%22.json` | High (the filing); its Stage-1/2 placement §U.4, §U.7 |
| 2005-05-06 | First CIK 1326801 activity on record (`REGDEX` paper item, attribution UNKNOWN) | — | — | `sources/_index/submissions_pre2014.csv` | High (the row); attribution §U.3 |

**Q.1 What is deliberately absent from this timeline.** The 2006–2007 federal matters (2:06-cv-01640,
5:07-cv-01389, 1:07-cv-10593, 07-1796) and the 2008 `Leader Technologies Inc. v. Facebook Inc.` patent suit
(1:08-cv-00862, D. Del., seen in the same ConnectU query) are **Stage-2** and belong to the next stage's
timeline; they are cited in §U/registers only as the continuation of disputes whose origins predate the
boundary. The day-level founding date, first product launch and first user are **absent because no held
document prints them** [MERGE 2026-10-07 — half of this stays and half is superseded: the **first product launch and the first user remain absent because no held document prints them** (UNKNOWN, U.5, no substitute licensed); the **day-level founding date is printed** — Ex-3.3's recital of July 29, 2004 as `TheFacebook, Inc.` — so its absence here is a reading gap, not a documentary one. See U.1 and COR-03.], not because they did not happen.

STATUS: WRITTEN 2026-10-07

## R

**R. End-of-stage structured snapshot (state at the July-2004 boundary)** — fixed 4-column form per §8; a
value with no source is `UNKNOWN`, not a guess.

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Legal entity | Facebook, Inc., a Delaware corporation | S-1 Corporate Information ("incorporated in Delaware in July 2004") | High (FACT, restated) |
| Date of incorporation | July 2004 (month-level; **no day available from EDGAR**) | S-1, ×2 statements | High (month) / UNKNOWN (day) |
| Registered state | Delaware | S-1 | High |
| Headquarters at formation | UNKNOWN — S-1 prints "headquartered in Menlo Park" in **2012 present tense**, which must not be back-dated to 2004 (§6) | S-1 Business overview | UNKNOWN for 2004 |
| Founder (self-declared) | Mark Zuckerberg, "founder, Chairman, and CEO" (a **2012 wrapper** about the past → FOUNDER CLAIM) | S-1 | High that the filing says it; Low as a 2004 fact |
| Co-founders at formation | UNKNOWN from filings — Saverin / Moskowitz / Winklevoss / Divya are **0 hits** in S-1 & 424B4 | string counts, both files | UNKNOWN |
| Product name as of 2004 | UNKNOWN in primary — `thefacebook` = 0 hits; name appears only in the S-1 history **graphic** (image, un-OCR'd) | S-1 graphic; `S1_accession_filelist.txt` | UNKNOWN |
| Users / revenue / customers | UNKNOWN — no in-period figure anywhere in `sources/` | — | UNKNOWN |
| Funding / capital | UNKNOWN — no pre-2012 filing; no charter exhibit | — | UNKNOWN |
| Ownership structure | UNKNOWN at formation; dual-class control is documented only **as of 2012** | S-1 (restated) | UNKNOWN for 2004 |
| Open disputes at boundary | An ownership claim was being asserted — `ConnectU v. Zuckerberg` filed 2004-09-02; Ceglia pleads an April-2003 contract | docket JSON; S-1 | High (that claims existed); pleaded not proven |
| Independent date anchor | 2004-09-02 (D. Mass. complaint) — the single externally-generated, machine-dated founding-era record | `cl2_%22ConnectU%22.json` | High (FACT) |

**R.1 Reading.** The only cells a Stage-1 reader could fill from Tier-1 text are *legal entity* and
*incorporation month*; everything about scale, money and people is `UNKNOWN` because EDGAR is empty through
2011 and the archive families were unreachable this run. That thinness is the correct shape of this snapshot
(§15.2 "we cannot know is a deliverable"), and §2's firewall forbids filling it from the company's later
fame.

STATUS: WRITTEN 2026-10-07

## S

**S. Data gaps** — what is missing for Stage 1, whether it is a *true null* (complete enumeration came back
empty) or *UNANSWERED / UNTRIED* (a route was blocked or never run), and the specific route that could close
it. High-importance gaps carry a mandatory follow-up (§13). These rows are mirrored in `data_gaps.csv`.

| Gap | Status | Why missing | Importance | Best available evidence | Route that could close it |
|---|---|---|---|---|---|
| Day-level founding date; authorised capital; consideration at formation | TRUE NULL (EDGAR) | No 2004 filing on CIK; no charter exhibit in the S-1 accession | High | `submissions_pre2014.csv` (oldest row 2005-05-06); `S1_accession_filelist.txt` | Delaware Division of Corporations certificate / good-standing order (**UNTRIED**) |
| Company financial/metric data for 2004–2008 | TRUE NULL (EDGAR) | Registrant's earliest audited period is FY2009 | High | S-1 Selected Financial Data ("2009, 2010 and 2011"); `xbrl_early_series.csv` earliest period FY2010 | RECAP/PACER; college press; OCR of S-1 graphics |
| The 2004 founding narrative in text | UNRECOVERABLE-as-text | S-1 "Our History" is a **graphic** (23 JPGs + sig), no extractable date | Medium | `S1_accession_filelist.txt` (image inventory); prose jumps "Our History"→metrics | OCR `g287954g*.jpg` (**UNTRIED**) |
| First-capture date / earliest archived pages of thefacebook.com, facebook.com | **UNANSWERED** (not null) | Wayback CDX ×3 refused: HTTP 504 and HTTP 503 "Internet Archive services are temporarily offline"; bodies kept `sources/web/cdx_*.txt` | High | negative artifacts only; **zero capture dates obtained** | re-run the two bare-host CDX calls once archive.org answers (**re-run required**) |
| In-window 2004–2006 press (esp. Harvard student newspaper) | **UNANSWERED / UNQUERIED** | Chronicling America ×3 HTTP 403; HathiTrust ×2 http_status 0; internet_archive & corporate_print skipped by failure-breaker; Google Books live but metadata-only (1 in-window record) | Medium | `sources/_harvest/*` negative bodies; `google_books/*.xml` (2006 New Yorker, no text) | re-run `--source-family corporate_print --source-family internet_archive`; add a college-press corpus (**UNTRIED**) |
| Founder/co-founder personal capital & contributions at formation | TRUE NULL in this corpus | no document in `sources/` states it | High | retrospective founder-account books (post-2011) — inadmissible for 2004 | RECAP pleadings; Harvard/Crimson press; DE registry |
| Attribution of the 2005–2006 `REGDEX`/`REGDEX/A` + 2008 `NO ACT` + 6 `UPLOAD`/`.paper` items on the CIK | **UNTRIED** | paper items never opened; no read document names the entity | Medium | `submissions_pre2014.csv` rows 2005-05-06 onward | open the 6 `UPLOAD`/`.paper` PDFs; do not let "Facebook registered in 2005" enter any register (§U.3) |
| Full text of the founding-year complaint (1:04-cv-11923) | **UNTRIED** (register only) | CourtListener returned the docket register, not pleadings | High | `cl2_%22ConnectU%22.json` (dateFiled, cause, parties) | RECAP/PACER full docket text (route proven reachable) |

**S.1 Close-out re-enumeration (§14.11).** `sources/` was re-listed at the start of this pass; no primary
document arrived *during* it — every artifact under `sources/` is dated 2026-09-25/26, before this dossier
opened. The only newer file is part 1 (`_parts/s1_p1.md`), which was still a PENDING scaffold at this
part's start; per the brief, inputs part 1 would own (A–J, boundary) were cited to their **carrier** directly
(the S-1, the docket, the index files) rather than to a sibling sentence, so a not-yet-written part 1 could
not be a dependency.

**S.2 `## Untried`** (explicit UNTRIED list, per §15.2 — a null from one family is not a null): (1) Delaware
Division of Corporations charter; (2) California Secretary of State entity record; (3) RECAP/PACER full
pleadings for 1:04-cv-11923 / 1:07-cv-10593 / 07-1796 / Ceglia; (4) the 5 `CORRESP` + 6 `UPLOAD` items and the
8 `S-1/A` amendments already enumerated; (5) OCR of the 23 S-1 history JPGs; (6) auction/museum documentary
records (family e); (7) Wayback CDX re-run after the outage; (8) a Harvard/college student-press corpus (no
configured route exists in the five families).

STATUS: WRITTEN 2026-10-07

## T

**T. Source / provenance table** — the documents this part relied on, with the §3 lineage note that matters
most here (the S-1, its eight amendments and the 424B4 are **ONE registration lineage**, not six witnesses).
Full rows are in the `sources.csv` register; `source_id` values there are provisional and minted centrally at
merge.

| Source | Type | Primary/Secondary | Event date | Publication date | URL / held path | Tier | Confidence |
|---|---|---|---|---|---|---|---|
| S-1 (accession 0001193125-12-034517) | SEC registration statement | Secondary for 2004 (restated), primary for 2012 | 2004-07 (content) | 2012-02-01 | `sources/sec/0001193125-12-034517_d287954ds1.htm` | 1 | High (entity/date text) |
| 424B4 final prospectus (0001193125-12-240111) | SEC prospectus | Same lineage as S-1 | — | 2012-05-18 | `sources/sec/0001193125-12-240111_d287954d424b4.htm` | 1 | High; **not independent** of S-1 |
| S-1/A amendments (046715, 101422, 134663, 175673, 208192, 222368, 232582) | SEC amendments | Same lineage as S-1 | — | 2012-02-08 → 05-16 | `sources/sec/*_d287954ds1a.htm` | 1 | High; one lineage |
| Federal docket register — ConnectU query | Court records (RECAP/CourtListener mirror) | Secondary (register-level; pleadings not held) | 2004-09-02 … 2008-11-19 | retrieved 2026-09-25 | `sources/legal/cl2_%22ConnectU%22.json` | 1 | High (dates/parties); register only |
| EDGAR submissions enumeration | SEC index (2 archive slices re-fetched HTTP 200) | Primary (metadata census) | 2005-05-06 → 2013-12-30 | retrieved 2026-09-25 | `sources/_index/submissions_pre2014.csv` | 1 | High |
| S-1 accession file list | SEC index | Primary (item inventory) | — | 2012 | `sources/_index/S1_accession_filelist.txt` | 1 | High (proves no charter exhibit) |
| XBRL early financial series | SEC facts | Primary metadata, **restated** financials | earliest period FY2010 | retrieved 2026-09-25 | `sources/financials/xbrl_early_series.csv` | 1 | High (that it starts FY2010) |
| Registrant resolve record | SEC ticker lookup | Metadata | — | 2026-09-29 | `sources/_index/_registrant_CIK0001326801.json` (Meta Platforms; former name "Facebook Inc") | 1 | High |
| Wayback CDX attempts ×3 | Web archive | — (service refused; error bodies) | — | 2026-09-25 | `sources/web/cdx_facebook.com.txt`, `cdx_thefacebook.com.txt`, `cdx_thefacebook_retry.txt` | n/a | **UNANSWERED — not evidence** |
| Periodical-harvest artifacts | Chronicling America (403) / HathiTrust (0-byte) / Google Books (metadata) | Secondary / none | 2004–2006 window mostly missed | 2026-09-25 | `sources/_harvest/*` | 2–3 | **UNANSWERED/UNQUERIED — not evidence**; Google Books in-window = 1 record, no text |
| Retrospective founder-account titles (Google Books rows) | Post-2011 books | Secondary, retrospective | about 2004 | 2011–2023 | listed in `sources/_harvest/google_books/` | 2–3 | `RETROSPECTIVE SOURCE` — usable only for how the story was told |

**T.1 Independence census for Stage 1.** Truly independent origins reaching July 2004: (a) the registration
lineage (counted as ONE), and (b) the federal docket register (independent of the founder). Everything else is
either a metadata index (same registrant), an error page (no answer), or retrospective literature (not a
witness to 2004). So the count of *independent in-window Tier-1 witnesses to the founding itself* is effectively
**one dated fact (incorporation, restated) plus one dated external trace (the 2004-09-02 complaint)** — which is
why §U carries so much weight here.

STATUS: WRITTEN 2026-10-07

## U

**U. Conflicting evidence (mandatory section)** — eight conflicts, anchored `U.1`–`U.8` and mirrored 1:1 by a
row in `conflicts.csv` (the merge proves parity; a conflict with no anchor, or an anchor with no row, is a
defect). Format per §7: CLAIM A / CLAIM B / WHY THEY DIFFER / EVIDENCE WEIGHT / BEST-SUPPORTED INTERPRETATION /
RESIDUAL UNCERTAINTY / CONFIDENCE.

**Handoff / numbering note (read before citing).** Part 1 (`_parts/s1_p1.md`, owner `s1-meta-p1`) declared an
anchor range U.1–U.7 in its §ID-scheme note (its lines 104–106) and stated that *§U itself is owed by part 2,
which must fold or renumber them and continue from U.8*. This section therefore adopts part 1's anchor
**taxonomy verbatim** for U.1–U.7 (so every `§U.n` cross-reference part 1's A–J narrative carries resolves to
the intended conflict), and adds **U.8** for the one conflict part 1 did not enumerate (the truncated-index
tooling artifact, probe META-C3). Part 1 was not edited; where the two parts diverge on the stage boundary it
is itself registered at U.7 for the merge to decide.



### U.1 — Formation day: registrant recital in a filed (unexecuted) form vs the absent registry record
- CLAIM A: the filings recital fixes a founding act; the S-1 states *"We were incorporated in Delaware in July
2004."* — but only to **month precision**, and the S-1 is a registration statement, not the executed charter.
- CLAIM B: the day-level incorporation date lives only in the Delaware Division of Corporations certificate,
which is **not** in `sources/` — the S-1 accession's only exhibit is the auditor consent `d287954dex231.htm`
(`sources/_index/S1_accession_filelist.txt`).
  *[MERGE 2026-10-07, contributed by the merge, not either part: **CLAIM B as written is refuted.** Part 1 opened Ex-3.3 and part 2 did not — `TheFacebook` and `July 29, 2004` have **0 occurrences anywhere in part 2's reads** — so part 1's U.1 row is canonical for this conflict. The day is recited in EDGAR, in a **form**, unsigned, and only the Delaware registry makes it a record.*]
- WHY THEY DIFFER: the recital is month-level and derivative; the day-level primary record is unreachable from
EDGAR.
- EVIDENCE WEIGHT: Tier-1 registrant text for the month; the day has no byte.
- BEST-SUPPORTED INTERPRETATION: **July 2004, month-level; the day stays UNKNOWN** — "no EDGAR document can
ever fix the founding day" (§13/§S). The window's open date is a **reach** decision (see U.7), not an evidentiary one. [MERGE: adjudication restated on part 1's bytes — **July 2004 is FACT at month level (High); 2004-07-29 is the best-supported day and travels at Medium; the day is NOT UNKNOWN and is not "unobtainable from EDGAR permanently"**. Confidence cell: `Medium (day) / High (month)`.]
- RESIDUAL UNCERTAINTY: day-level date; original authorised-share structure. Routes: Delaware charter
(UNTRIED); California SoS (UNTRIED).
- CONFIDENCE: High (month) / UNKNOWN (day).

### U.2 — Subject of the origin: the registrant vs Mr Zuckerberg personally (April 2003 / Ceglia)
- CLAIM A: the Ceglia suit is "against **us and Mark Zuckerberg**" over a contract allegedly made in **April
2003**, seeking "a substantial share of **Mr. Zuckerberg's** ownership" (S-1 & 424B4, same lineage).
- CLAIM B: the registrant entity (Facebook, Inc.) did not exist until **July 2004** (S-1, ×2).
- WHY THEY DIFFER: an April-2003 agreement cannot have been with a July-2004 corporation; the claim attaches to
a person, not the entity.
- EVIDENCE WEIGHT: internal to one lineage; the chronology resolves it.
- BEST-SUPPORTED INTERPRETATION: **keep pre-2004 activity attached to Zuckerberg personally, not to Facebook,
Inc.** Conflating them is the anachronism §6 forbids (the Morgan-Stanley / AT&T / Marathon pattern). The 2003
contract is **pleaded, not proven**; the company asserts the emails are fraudulent.
- RESIDUAL UNCERTAINTY: the underlying 2003 relationship and its merits are UNKNOWN.
- CONFIDENCE: High (that they are distinct subjects); UNKNOWN (the merits).

### U.3 — First CIK activity 2005-05-06 (`REGDEX`, unattributed) vs "the first filing is the 2012 S-1"
- CLAIM A: pre-2012 the CIK shows only the 2012 registration chain (S-1 / S-1A / 424B4).
- CLAIM B: `sources/_index/submissions_pre2014.csv` carries 5 `REGDEX` + 2 `REGDEX/A` (2005-05-06 → 2006-07-10),
one `NO ACT` (2008-10-14) and 6 `UPLOAD`/`.paper` items on CIK 1326801 before the S-1.
- WHY THEY DIFFER: registration-type paper items sit on the ticker before the IPO filing.
- EVIDENCE WEIGHT: the rows are real (FACT) but **attribution is unproven** — no read document names the entity.
- BEST-SUPPORTED INTERPRETATION: **UNKNOWN.** The probe's standing prohibition is carried forward: *do not let
"Facebook registered in 2005" enter any register.* The §Q timeline lists 2005-05-06 only as a *marker of the
gap*, never as a founding event.
- RESIDUAL UNCERTAINTY: reading the 6 `UPLOAD`/`.paper` PDFs (UNTRIED) is required before any attribution.
- CONFIDENCE: UNKNOWN.

### U.4 — Prospectus silence on the origin disputes vs a live federal register naming them
- CLAIM A: the strings `Winklevoss`, `Divya`, `ConnectU`, `Saverin`, `Moskowitz` are **0 hits** across the S-1
(2,627,678 B) and the 424B4 (3,545,401 B) [MERGE: true for those two documents, and **not** a corpus-wide null — re-measured on the stored SEC corpus, `Saverin` occurs **exactly once** in 31 documents, in Ex-10.16A (`S4499`) as the defined title **"the Saverin Agreement"** in the Mail.ru/DST conversion amendment, never described. `Winklevoss`, `ConnectU`, `Divya`, `Moskowitz` remain 0 everywhere. Part 1's U.4 row carries the narrowing.] — yet both documents *do* name Ceglia (see U.2).
- CLAIM B: `sources/legal/cl2_%22ConnectU%22.json` shows those suits — `ConnectU LLC v. Zuckerberg` filed
2004-09-02, matters 2006-10-26 / 2007-02-21 / 2007-03-09 / 2007-03-28, appeal 07-1796 filed 2007-05-22.
- WHY THEY DIFFER: the prospectus discloses only what the registrant chose to; a settled-then-dropped dispute
need not be named. Both are Tier 1 and cannot both be read as complete.
- EVIDENCE WEIGHT: for the **existence and dating** of the disputes the externally-generated register outweighs
the self-authored prospectus.
- BEST-SUPPORTED INTERPRETATION: **the docket outranks the prospectus**; no agent may write "the early equity
disputes were disclosed in the S-1." (This is why the disclosure asymmetry — Ceglia named, co-claimants not — is
recorded here rather than as a separate anchor.)
- RESIDUAL UNCERTAINTY: pleadings not retrieved; the exclusion rationale is UNKNOWN.
- CONFIDENCE: High.

### U.5 — "Founded February 2004 / dorm room" vs the only dated origin statements in the filings
- CLAIM A: the venture was founded **February 2004** in a Harvard dorm room (the framing this brief supplied).
- CLAIM B: *"We were incorporated in Delaware in July 2004"* / *"We were incorporated in July 2004"* (S-1, ×2).
- WHY THEY DIFFER: A is founder/secondary lore; B is registrant primary text. The bytes show A is **not** in the
corpus: `February 2004` = 0 hits, `thefacebook` = 0 hits, `Harvard College` = 0 hits in both filings; the only
"Harvard" in the S-1 is a 2011 "popular pages" example, not a founding statement.
- EVIDENCE WEIGHT: B is Tier-1 for the corporate act; A has no supporting byte.
- BEST-SUPPORTED INTERPRETATION: **July 2004 is the dated origin of the entity; the February/dorm/product-launch
date is UNKNOWN, not a co-equal claim.**
- RESIDUAL UNCERTAINTY: launch day unobtainable from EDGAR; history section is a graphic. Routes: OCR of the
`g287954g*.jpg` history images (UNTRIED); Wayback first-capture (family b, UNANSWERED).
- CONFIDENCE: High (July-2004 entity) / UNKNOWN (February/dorm).

### U.6 — Growth / user-count claims tied to "thirty days" vs the corpus's only "30 days" strings
- CLAIM A: Stage-1 growth lore invokes "thirty days" / early user counts to narrate 2004 adoption.
- CLAIM B: the corpus contains **no** "thirty days" string at all (`thirty days` = 0 hits), and the only
  *[MERGE 2026-10-07: **refuted by 1 hit** — `thirty days` occurs exactly once in the stored SEC corpus, in `d287954dex102.htm` (`S4498`), the 2005 Stock Plan, as an **option-exercise window**. Measured `30 days` = 71 in raw bytes / 73 after tag-and-entity stripping across 19 documents. Part 1's census (1 and 71) is canonical. The adjudication is unaffected: no occurrence is a growth statement, so the 2004 growth claim has **no carrier and gets no substitute number**.*]
"30 days" user-metric text is the **MAU measurement definition** — *"in the last 30 days as of the date of
measurement"* (S-1 and 424B4) — plus the 2005 stock-plan option-exercise window; all definitional/legal, none
a 2004 traction number.
- WHY THEY DIFFER: a measurement window and an option window are not evidence of early growth; the scale the
filings do print is FY2011 and out-of-stage (see U.7) — e.g. *"more than 800 million MAUs"* (S-1) / *"900
million"* (424B4), and the company's self-disclosed *"false or duplicate accounts may have represented
approximately 5-6% of our MAUs as of December 31, 2011."*
- EVIDENCE WEIGHT: B is byte-located string census across both filings; A has no corpus basis for 2004.
- BEST-SUPPORTED INTERPRETATION: **Stage-1 traction cannot be quantified from "thirty days" or user counts**;
every numeric MAU/DAU figure is a 2011 restatement (RESTATED), and the 5-6% false/duplicate disclosure further
undercuts using MAU as a Stage-1 signal. Recorded so §L stays `UNKNOWN as a quantity` (per §L.1).
- RESIDUAL UNCERTAINTY: any genuine 2004 adoption figure remains UNKNOWN (families b/c/d/e empty this run).
- CONFIDENCE: High (that the corpus has no Stage-1 "thirty-day"/user-count basis); UNKNOWN (2004 adoption).

### U.7 — Stage architecture: probe's Stage-1 close July 2004 vs the dispatched window 2003→2012
- CLAIM A (this part, §K–§R): follows the probe's boundary — Stage 1 closes at the **July 2004 incorporation**;
the FY2009–FY2011 series is therefore **out-of-window RESTATED** and excluded from the Stage-1 §P table.
- CLAIM B (part 1, §Header/§Boundary, adopted in its dispatch): Stage 1 runs the **dispatched window
2003→2012**, so the S-1's own financials and MAU trend lines are *in-stage*.
- WHY THEY DIFFER: the two parts read the same probe differently — the probe proposed a July-2004 close, while
the harvest window and dispatch (A4_harvest_mine: `2003-01-01..2012-12-31`, "deliberately WIDE where the
founding date is itself unestablished") span to registration.
- EVIDENCE WEIGHT: this is a **live architecture conflict, not a solved one**; neither pass re-staged the
company on its own authority (part 1 §Boundary 2, rival 7; this part defers).
- BEST-SUPPORTED INTERPRETATION: **the merge decides the boundary.** Under either reading the load-bearing
findings are unchanged: there are **0 EDGAR filings dated in 2004** (true null), the entity is dated to July
2004 (month-level), and all quantified company metrics are 2009+ restatements. What shifts is whether §P/§T
list FY2009–FY2011 as in-stage or as out-of-window context.
- RESIDUAL UNCERTAINTY: the Stage-1/Stage-2/Stage-3 seam (the probe assigns S-1 close = Stage 2 end, 424B4 =
Stage 3) is unresolved pending the merge's staging call.
- CONFIDENCE: High (that the divergence is real and registered); deferred (resolution).

### U.8 — Tooling: script index "nothing before 2024" vs 397 pre-2014 filings (probe META-C3)
- CLAIM A: the automated `index --cik 1326801` returned 1000 rows **all from source `recent`**, earliest
2024-06-14, with two archive slices failing (TimeoutError / HTTP 503) → printed as an empty pre-2014 window.
- CLAIM B: a manual re-fetch of the same two slice URLs returned HTTP 200 (314,243 B and 184,731 B), parsed to
`sources/_index/submissions_pre2014.csv` = **397 filings ≤ 2013-12-31**, oldest row 2005-05-06.
- WHY THEY DIFFER: a transient-failure / tool artifact versus a complete enumeration — not an evidentiary
dispute (distinct from U.3, which is about the *meaning* of the earliest row, not about reachability).
- EVIDENCE WEIGHT: B (bytes on disk) settles it.
- BEST-SUPPORTED INTERPRETATION: **the pre-2014 EDGAR register is complete and reachable; the truncated index
was a tool failure.** Recorded so no later agent re-litigates it (and noting the `sec_intake.py` bytes-vs-str
`ERROR_MARKERS` bug the probe reported, which blocks `grab`/`auto` document storage fleet-wide).
- RESIDUAL UNCERTAINTY: none as to reachability; the 397-row census is the working basis.
- CONFIDENCE: High.

STATUS: WRITTEN 2026-10-07

## claims

**Claim records — sections K–U (one record per claim).** Class follows §3/§4; `Corroboration` counts
*independent origins*, and per §3 the S-1 + its amendments + the 424B4 are **one lineage (count = 1)** — the
federal docket register is the only independent witness reaching July 2004. `URL` gives the held byte path
(remote EDGAR URL was not re-recorded this pass).

K01 Claim: The registrant filed nothing on CIK 1326801 dated in 2004 — the oldest pre-2014 row is 2005-05-06 — Date: 2004-12-31 (absence) — Source: EDGAR submissions enumeration (manual re-fetch, 397 rows) — Source date: 2026-09-25 — URL: sources/_index/submissions_pre2014.csv — Archived: held locally — Tier: 1 — Class: FACT (of absence) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High — Corroboration: 1 (enumeration) — Conflicts: U.3, U.8
K02 Claim: There is no certificate-of-incorporation exhibit in the S-1 accession, so authorised capital and the founding day are unobtainable from EDGAR — Date: 2012-02-01 — Source: S-1 accession file list — Source date: 2026-09-25 — URL: sources/_index/S1_accession_filelist.txt — Archived: held locally — Tier: 1 — Class: FACT (of absence) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High — Corroboration: 1 — Conflicts: U.1
K03 Claim: Ceglia pleaded an April-2003 contract claiming substantial ownership, which the registrant says is fraudulent — Date: 2003-04 (alleged); suit 2010-06-30 — Source: S-1 Legal Proceedings (= 424B4) — Source date: 2012-02-01 — URL: sources/sec/0001193125-12-034517_d287954ds1.htm — Archived: held locally — Tier: 1 — Class: FOUNDER CLAIM (adversary-side), RESTATED — Passage: "based on a purported contract between Mr. Ceglia and Mr. Zuckerberg allegedly entered into in April 2003" — Conf: Medium (that it is pleaded) — Corroboration: 1 (S-1 and 424B4 same lineage) — Conflicts: U.2
K04 Claim: Founder personal capital / co-founder contributions at formation are not stated anywhere in the held corpus — Date: 2004-07 — Source: negative of all sources/ — Source date: UNKNOWN — URL: sources/ (nil) — Archived: — — Tier: 1 — Class: UNKNOWN — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: UNKNOWN — Corroboration: 0 — Conflicts: U.2
L01 Claim: No in-period (≤2004) user, revenue or traction metric is printed in any held document — Date: 2004-07 — Source: negative of sources/ (earliest metric FY2011) — Source date: 2026-09-25 — URL: sources/ (nil) — Archived: — — Tier: 1 — Class: FACT (of absence) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High — Corroboration: 1 — Conflicts: U.6
M01 Claim: A breach-of-contract ownership suit against Zuckerberg, ConnectU LLC v. Zuckerberg, was filed 2004-09-02 — Date: 2004-09-02 — Source: CourtListener federal docket register — Source date: 2026-09-25 — URL: sources/legal/cl2_%22ConnectU%22.json — Archived: held locally — Tier: 1 — Class: FACT — Passage: NO_VERBATIM_PASSAGE_RECORDED (register fields dateFiled=2004-09-02; cause=28:1332 Diversity-Breach of Contract) — Conf: High — Corroboration: 1 (independent of S-1) — Conflicts: U.4, U.7
M02 Claim: The S-1 and 424B4 name Winklevoss, Divya, ConnectU, Saverin and Moskowitz zero times while the register shows those suits — Date: 2012 (filing) — Source: string counts, S-1 & 424B4 — Source date: 2012-02-01 — URL: sources/sec/ (both) — Archived: held locally — Tier: 1 — Class: FACT (of absence) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High — Corroboration: 1 — Conflicts: U.4
M03 Claim: For 2004 the internal deliberations, rejected options and contemporaneous failures are unrecoverable because the survivor's archive is the one kept — Date: 2004 — Source: method §2 record-selection null applied to the empty 2004 corpus — Source date: 2026-10-07 — URL: sources/ (nil) — Archived: — — Tier: 1 — Class: INFERENCE — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: Medium — Corroboration: 1 — Conflicts: None
N01 Claim: Facebook, Inc. was incorporated in Delaware in July 2004 (month-level) — Date: 2004-07 — Source: S-1 Corporate Information + Business overview — Source date: 2012-02-01 — URL: sources/sec/0001193125-12-034517_d287954ds1.htm — Archived: held locally — Tier: 1 — Class: FACT (restated) — Passage: "We were incorporated in Delaware in July 2004." — Conf: High — Corroboration: 1 — Conflicts: U.1, U.5
N02 Claim: Formation proceeded while an ownership claim (Ceglia 2003; ConnectU 2004) was unresolved against the founder personally — Date: 2004-07 — Source: S-1 + docket register — Source date: 2012-02-01 — URL: sources/sec/…ds1.htm; sources/legal/cl2_%22ConnectU%22.json — Archived: held locally — Tier: 1 — Class: INFERENCE — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: Medium — Corroboration: 2 (registrant lineage + docket) — Conflicts: U.2
O01 Claim: A parallel/competing venture ("ConnectU") was in play in the founding era, visible only through litigation, not a business record — Date: 2004-09-02 — Source: docket register — Source date: 2026-09-25 — URL: sources/legal/cl2_%22ConnectU%22.json — Archived: held locally — Tier: 1 — Class: INFERENCE — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: Low — Corroboration: 1 — Conflicts: U.4
P01 Claim: The earliest audited period printed in any registrant document is FY2009; the earliest XBRL period is FY2010 — Date: 2009-12-31 — Source: S-1 Selected Financial Data; XBRL series — Source date: 2012-02-01 — URL: sources/sec/…ds1.htm; sources/financials/xbrl_early_series.csv — Archived: held locally — Tier: 1 — Class: FACT (RESTATED, out-of-window under the probe close) — Passage: "for the years ended December 31, 2009, 2010 and 2011" — Conf: High — Corroboration: 1 — Conflicts: U.7
P02 Claim: FY2011 revenue was $3,711M, operating income $1,756M, net income $1,000M — Date: 2011-12-31 — Source: S-1 Business overview — Source date: 2012-02-01 — URL: sources/sec/0001193125-12-034517_d287954ds1.htm — Archived: held locally — Tier: 1 — Class: FACT (RESTATED; in-stage only under the dispatched window, see U.7) — Passage: "operating income of $1,756 million, and net income of $1,000 million" — Conf: High — Corroboration: 1 — Conflicts: U.6, U.7
Q01 Claim: The first externally-generated, machine-dated founding-era record is the 2004-09-02 complaint — Date: 2004-09-02 — Source: docket register — Source date: 2026-09-25 — URL: sources/legal/cl2_%22ConnectU%22.json — Archived: held locally — Tier: 1 — Class: FACT — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High — Corroboration: 1 — Conflicts: U.4, U.7
R01 Claim: At the July-2004 boundary only legal entity and incorporation month are Tier-1 fillable; HQ, people, money and metrics are UNKNOWN — Date: 2004-07 — Source: S-1 + §3 lineage rules — Source date: 2012-02-01 — URL: sources/sec/…ds1.htm — Archived: held locally — Tier: 1 — Class: FACT + UNKNOWN — Passage: "We were incorporated in July 2004 and are headquartered in Menlo Park, California." (2012 present tense — not back-dated per §6) — Conf: High (entity) / UNKNOWN (rest) — Corroboration: 1 — Conflicts: U.1, U.5
S01 Claim: The registrant is CIK 0001326801, named Meta Platforms, Inc., former name "Facebook Inc" — Date: 2026-09-29 (lookup) — Source: SEC ticker resolve record — Source date: 2026-09-29 — URL: sources/_index/_registrant_CIK0001326801.json — Archived: held locally — Tier: 1 — Class: FACT — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High — Corroboration: 1 — Conflicts: None
T01 Claim: Independent in-window Tier-1 witnesses to the founding itself number effectively two (restated incorporation; dated complaint) — everything else is one lineage, metadata, an error page, or retrospective literature — Date: 2004 — Source: this part's provenance census (§T.1) — Source date: 2026-10-07 — URL: sources/ (aggregate) — Archived: held locally — Tier: 1 — Class: INFERENCE — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High — Corroboration: 2 — Conflicts: U.3, U.4

STATUS: WRITTEN 2026-10-07

## registers

**Register rows for merge — one block per register, header identical to the Amazon exemplar, `stage` =
`stage1`, every field at header width, free-text quoted where a comma can appear.** All `source_id` values are
**provisional / dossier-local** (prefix `P2SRC-`) and must be re-minted centrally by `tools/id_mint.py` at
merge (author-minted global ids have collided before). No company CSV is written here (§14 rule 4); these are
append blocks only. Anchor tokens `U.1`–`U.8` appear in `conflict_id`/`conflict_ref` and are declared 1:1 in
§U; the merge proves parity.

Provisional id map (for the merge): `P2SRC-1` S-1 (accession 0001193125-12-034517, same lineage as its S-1/A
chain and P2SRC-2) · `P2SRC-2` 424B4 final prospectus (0001193125-12-240111, **same lineage as P2SRC-1**) ·
`P2SRC-3` federal docket register (CourtListener ConnectU query) · `P2SRC-4` EDGAR submissions enumeration
(submissions_pre2014.csv) · `P2SRC-5` S-1 accession file list · `P2SRC-6` XBRL early series · `P2SRC-7`
registrant resolve record · `P2SRC-8` Wayback CDX negative artifacts (UNANSWERED) · `P2SRC-9` periodical-harvest
artifacts (UNANSWERED / UNQUERIED / metadata-only).

>>> REGISTER ROWS FOR MERGE <<<
Target register: `sources.csv` — rows emitted: 9.
> **[MERGE 2026-10-07]** The 9 row(s) this `sources.csv` block emitted were applied to `sources.csv` and are **not reprinted in this volume**: `_parts/s1_p2.md` stays the emission of record, and a second copy would read to `tools/merge_census.py` as new rows. Live keys and the local-tag map are in the register-application record at the foot of this file.

>>> REGISTER ROWS FOR MERGE <<<
Target register: `timeline.csv` — rows emitted: 4.
> **[MERGE 2026-10-07]** The 4 row(s) this `timeline.csv` block emitted were applied to `timeline.csv` and are **not reprinted in this volume**: `_parts/s1_p2.md` stays the emission of record, and a second copy would read to `tools/merge_census.py` as new rows. Live keys and the local-tag map are in the register-application record at the foot of this file.

>>> REGISTER ROWS FOR MERGE <<<
Target register: `quantitative.csv` — rows emitted: 6. (FY2011 revenue/operating/net-income are held in §P narrative as out-of-window RESTATED context and are deliberately NOT emitted as Stage-1 register rows.)
> **[MERGE 2026-10-07]** The 6 row(s) this `quantitative.csv` block emitted were applied to `quantitative.csv` and are **not reprinted in this volume**: `_parts/s1_p2.md` stays the emission of record, and a second copy would read to `tools/merge_census.py` as new rows. Live keys and the local-tag map are in the register-application record at the foot of this file.

>>> REGISTER ROWS FOR MERGE <<<
Target register: `conflicts.csv` — rows emitted: 8 (1:1 with §U anchors U.1–U.8; numbering adopts part 1's U.1–U.7 taxonomy per its handoff and continues at U.8).
> **[MERGE 2026-10-07]** The 8 row(s) this `conflicts.csv` block emitted were applied to `conflicts.csv` and are **not reprinted in this volume**: `_parts/s1_p2.md` stays the emission of record, and a second copy would read to `tools/merge_census.py` as new rows. Live keys and the local-tag map are in the register-application record at the foot of this file.

>>> REGISTER ROWS FOR MERGE <<<
Target register: `data_gaps.csv` — rows emitted: 8 (High-importance rows carry a follow_up_task).
> **[MERGE 2026-10-07]** The 8 row(s) this `data_gaps.csv` block emitted were applied to `data_gaps.csv` and are **not reprinted in this volume**: `_parts/s1_p2.md` stays the emission of record, and a second copy would read to `tools/merge_census.py` as new rows. Live keys and the local-tag map are in the register-application record at the foot of this file.

>>> REGISTER ROWS FOR MERGE <<<
Target register: `decisions.csv` — rows emitted: 3.
> **[MERGE 2026-10-07]** The 3 row(s) this `decisions.csv` block emitted were applied to `decisions.csv` and are **not reprinted in this volume**: `_parts/s1_p2.md` stays the emission of record, and a second copy would read to `tools/merge_census.py` as new rows. Live keys and the local-tag map are in the register-application record at the foot of this file.

>>> REGISTER ROWS FOR MERGE <<<
Target register: `validation.csv` — rows emitted: 2 (one signal, one earned null).
> **[MERGE 2026-10-07]** The 2 row(s) this `validation.csv` block emitted were applied to `validation.csv` and are **not reprinted in this volume**: `_parts/s1_p2.md` stays the emission of record, and a second copy would read to `tools/merge_census.py` as new rows. Live keys and the local-tag map are in the register-application record at the foot of this file.

>>> REGISTER ROWS FOR MERGE <<<
Target register: `failures.csv` — rows emitted: 3.
> **[MERGE 2026-10-07]** The 3 row(s) this `failures.csv` block emitted were applied to `failures.csv` and are **not reprinted in this volume**: `_parts/s1_p2.md` stays the emission of record, and a second copy would read to `tools/merge_census.py` as new rows. Live keys and the local-tag map are in the register-application record at the foot of this file.

>>> REGISTER ROWS FOR MERGE <<<
Target register: `channels.csv` — rows emitted: 0 (earned null). No Stage-1 distribution channel, cost, result or repeatability is printed anywhere in `sources/`; every cell would be UNKNOWN, so per the emission contract ("a row you cannot attribute to a register is worse than a paragraph") the register is left empty and the gap is carried in `data_gaps.csv` and §O/§S.
> **[MERGE 2026-10-07]** The 0 row(s) this `channels.csv` block emitted were applied to `channels.csv` and are **not reprinted in this volume**: `_parts/s1_p2.md` stays the emission of record, and a second copy would read to `tools/merge_census.py` as new rows. Live keys and the local-tag map are in the register-application record at the foot of this file.

STATUS: WRITTEN 2026-10-07




---

# REGISTER APPLICATION RECORD (the merge's own section — foot of the volume)

**142 rows were emitted by the two parts (p1 99 + p2 43); 120 rows are live** — 119 applied from the emissions and
1 authored by this merge on the dispatch's explicit instruction (the provenance-drift `validation.csv` row). The
**23 rows not carried as separate rows are named in full** in
`03_quality_control/meta_s1_merge.md` §"Register application account": each was **aliased into a surviving row of
the same subject with its text appended and attributed to its part**, never deleted.

| register | emitted p1+p2 | applied | cols | keys |
|---|---|---|---|---|
| `sources.csv` | 11 + 9 | **15** | 18 | `S4495…S4509`, 0 duplicates |
| `quantitative.csv` | 30 + 6 | **36** | 12 | (date, metric) unique after the merge |
| `timeline.csv` | 22 + 4 | **23** | 11 | 11 cols, 3 aliases |
| `decisions.csv` | 3 + 3 | **5** | 15 | 1 alias |
| `validation.csv` | 6 + 2 | **8** | 11 | 1 alias + 1 merge-authored row |
| `failures.csv` | 5 + 3 | **8** | 11 | 0 aliases |
| `channels.csv` | 4 + 0 | **4** | 11 | p2's 0-row block is an **earned null** and stays empty |
| `conflicts.csv` | 7 + 8 | **8** | 15 | `U.1…U.8`, one row per subject, 0 duplicates |
| `data_gaps.csv` | 11 + 8 | **13** | 8 | 6 aliases |

## Global id block and the local-tag map

Minted with `python tools/id_mint.py --count 15 --company company_017_meta --claim --agent merge-meta` →
**`S4495 … S4509`**, allocated above every live id (audit before minting: 383 distinct issued ids, range
`S0001–S4462`; highest live block `company_035_att` `S4449…S4462`; the audit's collision list confirms
`S4222–S4229` are cited by **both** `company_011_microsoft` and `company_042_target`, which is why no id was taken
from that neighbourhood). Author-minted ids have collided before, so `P1Sxx` and `P2SRC-n` were **never** carried
into the live registers; they survive only as this map:

| local tag | global | carrier | | local tag | global | carrier |
|---|---|---|---|---|---|---|
| `P1S01` | **S4495** | 424B4, final prospectus 2012-05-18 | | `P1S09` | **S4503** | CourtListener docket register |
| `P1S02` | **S4496** | Form S-1 2012-02-01 (← `P2SRC-1`) | | `P1S10` | **S4504** | intake negatives / census aggregate |
| `P1S03` | **S4497** | **Ex-3.3, form of restated certificate** | | `P1S11` | **S4505** | stored periodical text layers |
| `P1S04` | **S4498** | 2012-02-08 exhibits (10.2/10.11/10.13) | | `P2SRC-5` | **S4506** | S-1 accession file list |
| `P1S05` | **S4499** | Ex-10.16A ("the Saverin Agreement") | | `P2SRC-6` | **S4507** | XBRL early series |
| `P1S06` | **S4500** | Ex-10.14/10.15 credit and bridge | | `P2SRC-8` | **S4508** | Wayback CDX negative artifacts |
| `P1S07` | **S4501** | EDGAR registrant record (← `P2SRC-7`) | | `P2SRC-9` | **S4509** | periodical-harvest artifacts |
| `P1S08` | **S4502** | EDGAR 397-row enumeration (← `P2SRC-4`) | | `P2SRC-2/3` | folded into **S4495/S4503** | same lineage / same register |

## The five families, carried as the probe issued them (TRIED–ANSWERED / TRIED–UNANSWERED / UNTRIED kept distinct)

Verdict **T2 core, 2 of 5**, for the dossier window 2003-01-01 → 2012-12-31. No family this merge did not attempt
is reported as empty; no failed request is reported as a null.

| # | family | state at merge | measured basis | in-window Tier-1 text? | register home / closing route |
|---|---|---|---|---|---|
| (a) | SEC / EDGAR filings | **TRIED–ANSWERED**; registrant-retrospective for the origin | 31 stored documents (`_RUN.json`: 50,285,422 B, 1,901,418 words); 424B4, S-1, 7 S-1/A bodies, exhibits 3.3/3.4/4.2A/4.6/10.2/10.4/10.11/10.13/10.14/10.15/10.16A/1.1; the 397-row pre-2014 enumeration | **YES** | `S4495–S4500`, `S4502`; `timeline.csv`; `quantitative.csv`; the `_UNANSWERED.csv` 9 filings never listed at `--max-docs 30` → F-4/F-5 |
| — | legal records | **TRIED–ANSWERED at register level; UNTRIED for pleadings** | `cl2_%22ConnectU%22.json` count 670 / document_count 4204; `cl2_%22Winklevoss%22.json` 303 / 2939; 7 in-window matters 2004-09-02 → 2008-11-19; three HTTP 500 negative artifacts kept | **YES** (register, not narrative) | `S4503`; `timeline.csv` dockets; **F-3** RECAP/PACER text |
| (b) | web archives | **TRIED–UNANSWERED — the network refused; NOT a null, no capture disproved** | `web/cdx_thefacebook.com.txt` 160 B (504); `cdx_facebook.com.txt` and `cdx_thefacebook_retry.txt` 11,832 B each (503, "Internet Archive services are temporarily offline"); **zero timestamps ⇒ zero capture dates** | NO | `S4508`, `data_gaps.csv` row 12; **F-1 stands** — `tools/cdx_intake.py` exists but `tools/web_domains.json` carries **no meta slug**, so family (b) stays **UNANSWERED/UNTRIED at the route level** and this merge requested a provenance-sourced domain rather than invent one |
| (c) | periodical corpora | **TRIED–UNANSWERED** for Chronicling America (403 ×3) and HathiTrust (status 0 ×2); **ANSWERED as metadata-only** for Google Books (22 rows, 1 in-window, 2006 New Yorker); **UNQUERIED** for internet_archive | `_harvest/candidates.csv` 30 rows; 7 stored `periodicals/` texts, all `BARE_WORD_MATCH`; `TIER1_CANDIDATE` is a mechanical flag and was **never** cited as evidence | NO | `S4509`, `S4505`; `data_gaps.csv` row 8 |
| (d) | digitised corporate print | **UNQUERIED** — task authored, killed by the consecutive-failure breaker (blank HTTP status); the sentence "pre-IPO printed material exists only in private hands" is **not licensed** | one `corporate_print` task and two `internet_archive` tasks, all blank | NO | `S4509`; `data_gaps.csv` row 8; periodical re-run request stands |
| (e) | auction / museum / manuscript | **UNTRIED** — 0 calls, structurally: no tool exists for this family and `tools/web_domains.json` has no slug for it | nothing under `sources/`; the one skip no outage explains | NO | `data_gaps.csv`; `## Untried` route 8 in part 1 |

## Open follow-ups this merge did NOT close (named, not dropped)

* **F-1** (CDX, both hosts, `from=2003&to=2008`) — **part 1's request stands and this merge re-endorses it**; it
  cannot be executed as written because `tools/web_domains.json` has **no meta slug**, so a provenance-sourced
  domain must be requested, never invented. Family (b) stays UNANSWERED/UNTRIED.
* **F-2** Delaware certified copy (the only route from Ex-3.3's recital to a **record**, and the only route to
  the founding share structure) · **F-3** RECAP/PACER text for the seven matters · **F-4** the six `UPLOAD` /
  `.paper` items behind the 2005–06 `REGDEX` cluster (closes or kills **U.3**) · **F-5** the five `CORRESP`
  letters and their `UPLOAD` responses · OCR of the accession's **22 figure JPGs + 1 signature** (measured; see
  COR-05) · the FY2012 10-K, enumerated but never stored · Zynga's, the landlord's and the banks' own copies ·
  families (b) re-run, (c) re-run, (d), (e).
* **Standing prohibitions carried forward verbatim:** no "Facebook registered in 2005" in any register or narrative
  (U.3); no substitute date, month, day or growth figure in place of the retracted February/thirty-days lore (U.5,
  U.6); no 2004 attachable to pre-corporate acts of Mr Zuckerberg personally (U.2); no market-size figure read
  backwards into a 2004 motivation; no `TIER1_CANDIDATE` / `BARE_WORD_MATCH` row cited as evidence; no Amazon
  value imported (the exemplar was read for header and section shape only).

**Merger's limit:** I assembled, applied, verified and published. **I did not audit and I do not certify** this
volume; every number above is a measurement of my own writes and an audit must re-measure it independently.


## CORRECTIONS propagated at merge (the gate measures this reach; CORRECTIONS.md holds the full text)

| id | what it withdraws or records | register cells it reaches | volume places |
|---|---|---|---|
| **COR-01** | author-minted local ids `P1S01–P1S11`, `P2SRC-1–9` retired; block **S4495–S4509** minted centrally | all 15 `sources.csv` rows | `stage_1.md` id-map table |
| **COR-02** | the census could not bind `validation.csv` / `failures.csv` (identical 11-col schemas); bound by reading | `validation.csv` row 1, `failures.csv` row 1 | foot application record |
| **COR-03** | part 2's three byte-level nulls refuted: the day-level recital **is** in EDGAR (Ex-3.3, unexecuted form, Medium); `845 million` **is** in the S-1 (`845&nbsp;million` x11); `thirty days` = **1** hit (option window, not growth). `Saverin` = 1 occurrence corpus-wide, as "the Saverin Agreement" | `conflicts.csv` U.1 / U.4 / U.6, `quantitative.csv` 2011-12-31 MAU row, `timeline.csv` 2004-07-29 and 2004-07 rows, `sources.csv` S4496/S4497/S4499, `data_gaps.csv` row 2 | §K.2, §K.5, §Q.1, §U.1, §U.4, §U.6 annotations; head findings 1, 3, 4, 7 |
| **COR-04** | S-1 body 2,657,075 B / sha1 `d749855a…` vs sidecar+manifest 2,627,682 B / `bf14d107…` — **reported, not repaired**: neither hash nor bytes rewritten, and why | `validation.csv` row 8, `sources.csv` S4496, `data_gaps.csv` row 11 | head finding 6; `_MANIFEST.md` |
| **COR-05** | image inventory measured from the held file list: **22 `g287954g*.jpg` figures + 1 signature = 23 JPGs of 28 items**, not the "26 figures" the probe and part 1 print, and none stored | `sources.csv` S4506, `data_gaps.csv` row 1 | foot |
| **COR-06** | the dispatch label **T1** is wrong; the probe measures **T2 (2 of 5)** and the gate was run with `--tier core` passed explicitly | `conflicts.csv` U.7, `sources.csv` S4504 | head tier section |
| **COR-07** | conflict de-duplication: **15 emitted rows → 8 rows, one per subject**, part 1 canonical for U.1–U.7, U.8 part 2's alone, no anchor renumbered | all 8 `conflicts.csv` rows | head parity section |
| **COR-08** | `company` literal normalised carrier-faithfully (`Facebook, Inc.`; `Meta Platforms, Inc.` only on the two rows whose carrier prints it; bare `Meta` on no row) | row 1 of all nine registers | head convention |
| **COR-09** | what the merge **authored** (1 validation row) and the **10 empty cells** it conformed; `channels.csv` left unpadded | `validation.csv` row 8, `sources.csv` S4508/S4509, `quantitative.csv` rows 31–36 | foot application record |
