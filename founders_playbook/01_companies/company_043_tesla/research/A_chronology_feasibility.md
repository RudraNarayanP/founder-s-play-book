# A_chronology_feasibility.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T19:42:19Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## Verdict

**TIER: T3 (register tier).** Fixed by §15.2 on families that returned **in-window Tier-1 text**, not on ambition: exactly **one** family did (filings). §15.2 deliverable for T3 = short narrative + registers; §K/§N/§U-equivalent content is carried here in Boundaries / Conflicts / Nulls and is not silently dropped.

| Family | Answered? | In-window Tier-1 text held? | What it returned |
|---|---|---|---|
| a — filings (EDGAR) | ANSWERED, held | **YES** | 4 documents held (≈5.9 MB). Nothing EDGAR-dated 2003–2008: earliest submission in the 1,750-filing window slice is Form D **2009-04-09**. All 2003–2004 content is therefore a **2010 retrospective self-report** inside one registration lineage. |
| b — web archives | PARTLY ANSWERED, no content bytes | NO | One CDX call answered with 14-digit capture timestamps for `tesla.com` root (2002-11-25, 2003-02-09, 2003-02-14, 2006-02-09/302). All later CDX attempts returned **504 / "Internet Archive temporarily offline"** → kept as negative artefacts. No page bytes held. |
| c — periodical corpora | ANSWERED at metadata layer only | NO | IA advancedsearch ×3 → 6 items, **all books 2015–2018**; 2 of 3 queries numFound 0 (a true null *at the metadata layer only* — `text:` matches item annotations, not pages). HathiTrust → Cloudflare interstitial (UNANSWERED). Chronicling America → **HTTP 403** (UNANSWERED, reproduces the nvidia-pass result). Google Books feed → answered, post-window trade books. |
| d — corporate print | ANSWERED at metadata layer only | NO | title-scoped numFound **2** (`tesla-logo` "Tesla, Inc. Annual Reports"; `teslaroadster0000maur` 2008); creator-scoped numFound **0**. **Identified, not opened** — no text layer fetched. |
| e — documentary (auction / museum sale records) | **UNTRIED** | NO | no scripted route exists in `tools/`; not attempted by hand. Not a null. |
| f — legal registers (extra family) | ANSWERED for federal only | NO founding-window record | CourtListener v4 (HTTP 200, bytes held): 497 hits `"elon musk tesla arbitration"`, 16 `"eberhard straubel"`; **none in 2003–2010** and none from a California Superior Court docket — the registry that would hold the founding dispute is not in this corpus. |

**What the tier means here, stated plainly.** This is the worst case for §14.6's asymmetry, and in an unusual direction: the entity is *new* (2003), so EDGAR is not merely thin before 1994 — it is **empty for the first five and a half years of the company's own existence**, because the company had no reporting obligation until it registered in 2009-04-09 (CIK 1318605). Web archives cover the period but this pass could not hold a single page byte because the Archive's CDX and search endpoints were degraded. Periodicals — the family §14.6 says rescues the pre-1994 gaps — are reachable only where someone has put the words in an item's metadata; a 2004 magazine page that says "Tesla Motors" is invisible to the route that was used. **T3 is therefore a statement about reachability, not about whether the founding is documented.**

**Would move to T2:** holding (i) tesla.com 2004–2006 page bytes (one re-run of CDX when the Archive is not 504-ing, then one `_djvu`-free fetch of an `id_` snapshot), **or** (ii) any in-window newspaper text from a non-blocked periodical route (Chronicling America is 403 from this egress; LOC's other endpoints and local-paper archives were not tried), **or** (iii) opening the two corporate-print items with `ia_text.py fetch`. Each is one intake task; none requires new judgment.

**Would move to T1:** (i)–(iii) plus the San Mateo County / JAMS record of the 2008–2009 dispute, or the parties' August 2009 joint statement held as bytes. That single document is the highest-value unwritten object in this company.

STATUS: WRITTEN

## Founder-attribution question

### The question this probe was dispatched on

Fortune's 2026 list flags Tesla (rank 43) `Founder is CEO = yes`. The incorporated entity's own
filings date the incorporation to **2003-07-01** with a set of earliest officers/directors, while a
later, high-visibility account credits the CEO-director with a founding role and start date that were
**disputed and litigated**. This section says only what documents exist, from what date, whose words
they are, and what follows at what confidence. It does not resolve the dispute; §Conflicts records it
as live, both-sided, with each side's carrier named.

### Every founding-window document this pass actually holds (bytes on disk, `sources/`)

| # | Document | Doc date | Whose words | Held bytes | Founding-relevant content |
|---|---|---|---|---|---|
| D1 | Form S-1, primary doc `ds1.htm`, acc. 0001193125-10-017054 | 2010-01-29 | **the registrant** (company counsel's drafting; signed by the board) | yes, 2,362,163 B | "formed in July 2003"; Delaware incorporation **2003-07-01** (audited note); Musk = Chairman **since April 2004**, Product Architect since May 2008, CEO since Oct 2008; Straubel CTO since May 2005, "Principal Engineer, Drive Systems **from March 2004**"; Eberhard and Tarpenning = "**former officer and director**"; **no use of "founder" for anyone at Tesla** |
| D2 | S-1/A No. 3, `ds1a.htm`, acc. 0001193125-10-099603 | 2010-04-29 | registrant | yes, 2,189,012 B | first held instance of the phrase "**one of our founders**" applied to Musk (director-qualifications paragraph); absent from D1 |
| D3 | 424B4 final prospectus, `d424b4.htm`, acc. 0001193125-10-149105 | 2010-06-29 | registrant | yes, 2,677,451 B | repeats D2's "one of our founders"; "contributed significantly and actively to us **since our earliest days in April 2004**"; Series D purchaser table incl. **Elon Musk Revocable Trust dated July 22, 2003**; 2003 Equity Incentive Plan adopted **July 2003**; 646 employees at 2010-05-31; Ian Wright in the beneficial-ownership table (180,188 sh) |
| D4 | FY2010 Form 10-K, `d10k.htm`, acc. 0001193125-11-054847 | 2011-03-03 | registrant, audited by an independent auditor (Ernst & Young LLP, reports dated) | yes, 1,669,538 B | "incorporated in the state of Delaware on **July 1, 2003**"; "formed in July 2003"; **zero** occurrences of "founder"/"co-founder" of Tesla; no Tarpenning; no mention of any arbitration |
| D5 | 2011 DEF 14A, `ddef14a.htm`, acc. 0001193125-11-092509 | 2011-04-08 | registrant (board nominating/compensation drafting) | yes, 588,431 B | repeats "one of our founders and our largest stockholder" for Musk; adds that his equity came from "**preferred stock acquired via investment**" rather than compensatory grants |
| D6 | EDGAR submissions slice 2003-01-01→2012-12-31, `sources/_index/submissions.csv` | retrieved 2026-09-26 | SEC registry | yes | **1,750 filings; earliest dated inside the window = Form D 2009-04-09.** EDGAR holds nothing for this company for 2003–2008 |
| D7 | Wayback CDX rows for `tesla.com` root (14-digit timestamps) | capture dates 2002-11-25 / 2003-02-09 / 2003-02-14 / 2006-02-09 | Internet Archive index | transcript-retained only (see `sources/wayback/README_retained_capture_evidence.md`) | root-page captures that **pre-date the incorporation by 5–8 months** → domain precedence, not company history |
| D8 | CourtListener v4 search answers, `sources/legal/cl_*.json` | 2026-09-26 retrieval | federal-court aggregator index | yes, 193 KB | no 2003–2010 record naming Musk/Eberhard/Straubel; **registry does not cover California Superior Court**, so silence is not absence |

**Lineage rule applied (§3).** D1, D2 and D3 are **one source** — a registration statement, its
amendments and the prospectus that superseded it. Every "the filings say X" statement below is
therefore one corporate voice, not corroboration. D4 is the same registrant's later periodic report
and D5 the same board's proxy language; **all five trace to one drafter lineage**. The count of
*independent* founding-window carriers in this pass is **zero**. That is the single most important
line in this dossier.

### What can be established, at what confidence

| Assertion | Class | Conf | Basis (document, date) |
|---|---|---|---|
| A Delaware corporation named Tesla Motors, Inc. with CIK 1318605 states it was incorporated on 2003-07-01 | FACT (as to the statement) / FOUNDER-adjacent corporate claim (as to the event) | **High that the statement exists**; **Medium that the date is independently right** | D3/D4, 2010-06-29 / 2011-03-03; no Delaware Secretary of State certificate held → the date is uncorroborated outside the lineage |
| A board-adopted, stockholder-approved equity plan existed in July 2003 | FACT within the lineage | Medium | D3 "In July 2003, we adopted the 2003 Equity Incentive Plan" |
| Elon Musk controlled a trust instrument dated 2003-07-22 that later bought Series D preferred | FACT within the lineage | Medium-High | D3 purchaser table; the trust's *formation* date is not evidence of a *founding* act |
| Musk's first documented relationship date with the registrant is **April 2004** (Chairman of the board) | FACT within the lineage | High (as to the statement) | D1 2010-01-29, carried unchanged into D2/D3/D5 |
| Straubel's first documented role date is **March 2004** (Principal Engineer, Drive Systems) | FACT within the lineage | High (as to the statement) | D1/D3 |
| Eberhard and Tarpenning are described only as "former officer and director" | FACT | High | D1, D3 |
| The word "founder" of Tesla is applied by the registrant **only to Musk**, and only in an amended registration statement (absent 2010-01-29, present 2010-04-29) | FACT + INFERENCE on timing | High for the text; Medium for why | D1 vs D2/D3/D5 |
| No EDGAR document of this issuer exists for the founding period 2003–2008 | FACT | High | D6 (1,750-row enumeration, min date 2009-04-09) |
| The registrant's own 2010–2011 disclosure corpus contains **no reference to any arbitration or founder dispute** | FACT (string-verified, 0 hits for `arbitrat` across ≈5.9 MB of held HTML text) | High | D1–D5 |

### What cannot be established from held bytes

1. **Whether any person "founded" Tesla in the sense Fortune's flag means.** The only carriers of the competing accounts this pass could reach are the registrant itself (one lineage) and *unheld* material: no interview transcript, no founder's own writing, no docket, no contemporaneous newspaper page is in `sources/`.
2. **Who the earliest directors were at incorporation.** The lineage names 2010 directors and gives Musk's and Kimbal Musk's board start as April 2004; it never enumerates the July 2003 incorporator/first-director slate. No corporate-registry document held.
3. **What the disputants actually said.** Musk's own founder statements (interviews, social posts) and Eberhard's/Tarpenning's/Straubel's counter-statements are **not held**, so this dossier deliberately does not quote, date, or grade them. They are listed as named unheld carriers below and in §Untried.
4. **Whether a court or arbitrator made any finding.** See the litigation carrier list; nothing reached.

### The live conflict and its carriers (both sides, neither averaged)

**Side 1 — the incorporated-entity account.** Tesla, incorporated 2003-07-01, with an officer/director
set whose earliest documented dates are March–April 2004; the CEO's relationship begins April 2004 and
his equity is characterised as investment-acquired. Carrier: **D1–D5, one lineage, all corporate
self-report**, i.e. a *retrospective* instrument written seven years after the events by the party with
an IPO to sell. Per §3/§2 it may not be counted as corroboration of itself, and per §6 every 2003–2004
date inside it is a **RETROSPECTIVE SOURCE** for 2003–2004 facts.

**Side 2 — the later high-visibility account.** A founder-role account for the CEO-director whose role
and start date are disputed and were litigated. Carriers **named but NOT held this pass**: (a) the
2008–2009 San Mateo County Superior Court / arbitration record and any settlement papers; (b) the
parties' joint public statement of 2009 (the candidate Tier-1 carrier is the *company-published* page
on tesla.com, reachable only through the web-archive family, which was degraded); (c) the founders'-own
interviews; (d) reported biographies — the 2015 Vance volume and the Isaacson successor are **identified
in IA metadata** (`elonmuskteslaspa0000vanc`, 2015) but their text layers were **not fetched**, so no
sentence from them is quoted here.

**Why they differ and what the probe does not do.** The two accounts are not two readings of one record;
they are different records with different genres — an issuer's IPO disclosure, whose legal incentive is
to date inception to the entity and to describe the CEO's equity as an investment, versus a founder-claim
genre whose incentive runs the other way. **No averaging, no compromise attribution, no "co-founder of
whom?" hedge.** The dossier's position: at the level of *held public evidence*, Tesla's founding has **one
documentary voice and no independent witness**, and the disagreement about who that voice omits is
itself the finding.

### Claim records (dossier-local IDs F01–F12)

F01 Claim: The registrant states it was incorporated in Delaware on 2003-07-01. — Date: 2003-07-01 — Source: Tesla Motors, Inc. FY2010 Form 10-K, Note 1 — Source date: 2011-03-03 — URL: https://www.sec.gov/Archives/edgar/data/0001318605/000119312511054847/d10k.htm — Archived: — — Tier: 1 — Class: FACT (statement) / RETROSPECTIVE INTERPRETATION (event) — Passage: "Tesla Motors, Inc. … was incorporated in the state of Delaware on July 1, 2003." — Conf: High (statement), Medium (event, single lineage) — Corroboration: 0 independent — Conflicts: U.1

F02 Claim: The registrant describes its formation in its risk factors as July 2003. — Date: 2003-07 — Source: 424B4 final prospectus — Source date: 2010-06-29 — URL: https://www.sec.gov/Archives/edgar/data/0001318605/000119312510149105/d424b4.htm — Archived: — — Tier: 1 — Class: FACT (statement) — Passage: "We were formed in July 2003." — Conf: High (statement) — Corroboration: same lineage as F01 — Conflicts: U.1

F03 Claim: Elon Musk's first documented role with the registrant is Chairman of the board, from April 2004. — Date: 2004-04 — Source: Form S-1 primary doc — Source date: 2010-01-29 — URL: https://www.sec.gov/Archives/edgar/data/0001318605/000119312510017054/ds1.htm — Archived: — — Tier: 1 — Class: FACT (statement) — Passage: "Elon Musk has served as our Product Architect since May 2008, our Chief Executive Officer since October 2008 and as Chairman of our board of directors since April 2004." — Conf: High — Corroboration: 0 independent, carried into F04 — Conflicts: U.1

F04 Claim: The registrant dates Musk's contribution to April 2004 while crediting pre-IPO engineering and capital-raising. — Date: 2010-06-29 — Source: 424B4, executive-compensation section — Source date: 2010-06-29 — URL: https://www.sec.gov/Archives/edgar/data/0001318605/000119312510149105/d424b4.htm — Archived: — — Tier: 1 — Class: FOUNDER CLAIM (corporate, retrospective) — Passage: "Mr. Musk has contributed significantly and actively to us since our earliest days in April 2004 by recruiting executives and engineers, contributing to the Tesla Roadster's engineering and design, raising capital for us" — Conf: High (statement), UNKNOWN (accuracy of the characterisation) — Corroboration: same lineage — Conflicts: U.2

F05 Claim: "One of our founders," applied to Musk, is absent from the original S-1 and present by the third amendment. — Date: 2010-01-29 → 2010-04-29 — Source: S-1 (0001193125-10-017054) vs S-1/A (0001193125-10-099603), string-verified on held bytes — Source date: 2010-04-29 — URL: https://www.sec.gov/Archives/edgar/data/0001318605/000119312510099603/ds1a.htm — Archived: — — Tier: 1 — Class: FACT (drafting change) + INFERENCE (it was added mid-IPO, motive UNKNOWN) — Passage: "the perspective and experience he brings as our Chief Executive Officer, one of our founders and our largest stockholder" — Conf: High that the text changed; Medium that the bracket is 2010-01-29…04-29 (2010-03-29 amendment not fetched) — Corroboration: 1 lineage — Conflicts: U.2

F06 Claim: The registrant never labels Eberhard or Tarpenning as founders; it calls them "former officer and director". — Date: 2010-01-29 — Source: Form S-1, certain-relationships/Series D section — Source date: 2010-01-29 — URL: https://www.sec.gov/Archives/edgar/data/0001318605/000119312510017054/ds1.htm — Archived: — — Tier: 1 — Class: FACT (absence of label + presence of description) — Passage: "Martin Eberhard and Marc Tarpenning, each of whom is a former officer and director" — Conf: High — Corroboration: 0 independent — Conflicts: U.3

F07 Claim: Straubel's earliest role date in the corporate record is March 2004, and his prior employer is described as a different company he co-founded. — Date: 2004-03 — Source: 424B4, director bios — Source date: 2010-06-29 — URL: https://www.sec.gov/Archives/edgar/data/0001318605/000119312510149105/d424b4.htm — Archived: — — Tier: 1 — Class: FACT (statement) — Passage: "previously served as our Principal Engineer, Drive Systems from March 2004 to May 2005" — Conf: High — Corroboration: 0 independent — Conflicts: None

F08 Claim: Musk's pre-IPO equity is characterised as investment-acquired preferred stock, not compensatory grants. — Date: 2011-04-08 — Source: 2011 DEF 14A, compensation discussion — Source date: 2011-04-08 — URL: https://www.sec.gov/Archives/edgar/data/0001318605/000119312511092509/ddef14a.htm — Archived: — — Tier: 1 — Class: FACT (statement) — Passage: "as opposed to preferred stock acquired via investment as was the case with Mr. Musk" — Conf: Medium-High — Corroboration: 1 (board lineage) — Conflicts: U.2

F09 Claim: The entity's own filings contain no reference to the founder litigation or arbitration. — Date: 2010-01-29 → 2011-04-08 — Source: string scan of D1–D5 held HTML, `arbitrat` — Source date: 2011-04-08 — URL: local `sources/sec/` — Archived: n/a — Tier: 1 — Class: FACT (documented null) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High (0 hits across ≈5.9 MB) — Corroboration: n/a — Conflicts: None

F10 Claim: No EDGAR filing of this issuer predates 2009-04-09, so the 2003–2008 founding period has no filing carrier at all. — Date: 2009-04-09 — Source: EDGAR submissions slice, `sources/_index/submissions.csv` (1,750 rows, window 2003-01-01→2012-12-31) — Source date: 2026-09-26 — URL: local `sources/_index/submissions.csv` — Archived: n/a — Tier: 1 — Class: FACT — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High — Corroboration: n/a — Conflicts: None

F11 Claim: The earliest archived captures of the `tesla.com` root pre-date the stated incorporation by 5–8 months, so the domain's first capture is not the company's first page. — Date: 2002-11-25 — Source: Wayback CDX rows for url=tesla.com (status 200, length 1113–1119 B) — Source date: 2002-11-25 — URL: local `sources/wayback/README_retained_capture_evidence.md` — Archived: transcript-retained; re-fetch 504/offline — Tier: 1 as an index record, content UNREAD — Class: FACT (capture date) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: Medium (timestamps trustworthy; the response body is transcribed, not held) — Corroboration: 0 — Conflicts: U.4

F12 Claim: The federal court registry reachable this pass holds no 2003–2010 founding-dispute record, and does not cover the state court where the dispute was heard. — Date: 2026-09-26 — Source: CourtListener v4 search answers, `sources/legal/` — Source date: 2026-09-26 — URL: https://www.courtlistener.com/api/rest/v4/search/ — Archived: n/a — Tier: 1 as a registry index — Class: FACT (scope of the answer) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High — Corroboration: n/a — Conflicts: None (silence ≠ absence; see §Nulls)

STATUS: WRITTEN 2026-09-26

## Family a filings

**Route:** `tools/sec_intake.py` (EDGAR submissions slice under `sources/_index`, documents under
`sources/sec`, each with a provenance sidecar carrying url / fetched / sha1 / bytes / words).
Retrieval outcome: **no 404, no 503, no refused accession** — the filings family answered every call
this pass. One tool fact worth recording for the next agent: the brief's `resolve --company-dir
--from --to` form errors (`resolve` accepts `--ticker` only); window filtering belongs to
`index`/`grab`.

**Enumeration (Tier-1 registry answer, and it is the load-bearing negative).** The 2003-01-01 →
2012-12-31 slice contains **1,750 filings** for CIK 0001318605 (Tesla, Inc.). The earliest is
**Form D, 2009-04-09**. Forms present from that date: D, S-1, S-1/A, 424B3/B4/B5, 425, 8-K, 10-K,
10-K/A, 10-Q, 3/4/5 and amendments, DEF 14A. **Zero documents dated 2003-07 through 2008-12.** For
this company the §14.6 "EDGAR reaches essentially nothing before ~1994" asymmetry inverts: the entity
is *younger* than EDGAR's coverage, but it was a private issuer, so the family's silence covers exactly
the founding period the probe needs. Every 2003–2008 date below is therefore **a 2009–2011 statement
about 2003–2008**, not a contemporaneous record.

**Documents held (all under `sources/sec/`):**

| Accession | Date | Doc | Bytes | What it settles |
|---|---|---|---|---|
| 0001193125-10-017054 | 2010-01-29 | `ds1.htm` (S-1 original) | 2,362,163 | earliest carrier of the corporate self-account; **contains no Tesla "founder" label for anyone** |
| 0001193125-10-099603 | 2010-04-29 | `ds1a.htm` (S-1/A) | 2,189,012 | first held instance of "one of our founders" for Musk |
| 0001193125-10-149105 | 2010-06-29 | `d424b4.htm` (final prospectus) | 2,677,451 | fullest founding account: inception, July 2003 plan adoption, Series D purchaser table, director/officer role dates, employee counts |
| 0001193125-11-054847 | 2011-03-03 | `d10k.htm` (FY2010 10-K) | 1,669,538 | the settled corporate history in periodic-report form; audited financial notes carry the 2003-07-01 date |
| 0001193125-11-092509 | 2011-04-08 | `ddef14a.htm` (2011 proxy) | 588,431 | board's own characterisation of Musk's role and the source of his equity |

**What the family establishes and what it cannot.** It establishes the *entity's* dating and role
chronology with high fidelity and it establishes, by exhaustive string search, what the entity
**chose not to say**: 0 hits for `arbitrat`, 0 for `Gottschlich`, 0 for `February 2004`, and — in the
10-K — 0 for `founder` and 0 for `Tarpenning`. Silence in a document is not silence in the record, but
in a registration statement a silence is a drafting decision, and it is evidence about the corporate
account rather than about 2003. **The family cannot establish who founded the company**, because the
question was never answered in a founder-election sense by the registrant: it lists officers, directors
and start dates, and — only from 2010-04 — one adjective.

**Independence accounting (the part that decides the tier).** The five documents are **two corporate
voices at most** (issuer's counsel-drafted registration lineage 0001193125-10-017054/099603/149105;
then the same issuer's periodic report and proxy), with no third-party carrier: no Delaware charter,
no county filing, no auditor's own chronology, no newspaper that did not use the filing. Corroboration
count for the founding period = **0**.

STATUS: WRITTEN 2026-09-26

## Family b web

**Route:** Wayback CDX by manual `curl` (there is no scripted web-archive route in `tools/`; §14.9
compliance: raw bodies written straight to `sources/wayback/` with `.meta.json` sidecars, including the
failures).

**Held answers and held failures.** One root-URL query answered, giving the only trustworthy capture
dates in this dossier (14-digit timestamps as returned): `20021125165605` (200, 1,119 B),
`20030209014400` (200, 1,116 B), `20030214143552` (200, 1,113 B), `20060209024141` (302, 394 B). Every
domain-scoped or filtered re-query — `matchType=domain` 2003–2005, and the 2008–2011 regex filter
built to find a founder/joint-statement page — returned **504 Gateway Time-out** or the Internet
Archive **"Temporarily Offline"** HTML page. Those bodies are kept verbatim
(`cdx_tesla_com_2003_2005.json`, `cdx_tesla_com_root_exacts.json`,
`cdx_www_tesla_com_root_exacts.json`, `cdx_tesla_com_2008_2011_founderish.json` [0 B]) and are
**UNANSWERED**, not nulls: the Archive's index service was degraded during this window, which is a
fact about the tool, not about Tesla's early web presence.

**The forensic trap the timestamps expose, and it matters.** The three successful pre-2006 captures of
the `tesla.com` root **all pre-date the stated 2003-07-01 incorporation** — by roughly 7 months, 4½
months and 4½ months. `tesla.com` was therefore not this company's domain at first capture, and any
reconstruction that reads "the company's website existed in Feb 2003" off the index is a **domain
precedence error** of exactly the kind Fortune's `Founder is CEO` flag is. The first capture that could
plausibly be the entity's own is the 2006-02-09 row, and it is a 302 — a redirect, i.e. a shell, not a
page. **No archived Tesla page content is held.** Consequently family b contributes **capture dates
and one negative** (the domain's pre-company history), and zero Tier-1 text.

**Named unheld carrier this family was supposed to produce:** the parties' **August 2009 joint
statement** about Musk's founding role, published on the company's own site (and therefore, if held,
Tier-1 *and* a corporate-published document, which does not make it independent of the corporate
account — it makes it the corporate account at an earlier date, which is its real value: it would be
the founding-dispute text from 2009 rather than from 2010). Lookup route: CDX domain query 2009
filtered on the press/blog URL pattern → fetch the `id_` raw snapshot. Blocked by the outage; see
§Untried U-1, U-2.

STATUS: WRITTEN 2026-09-26

## Family c periodicals

**Routes tried (3 of the 4 corpus sub-routes answered; 2 blocked; 1 config-crashed then re-proved):**
`tools/periodical_harvest.py` with a probe-scoped config
(`research/_harvest_queries_tesla.json`; raw responses under `sources/harvest/`, `_MANIFEST.md`
regenerated on the pass-2 run), plus the per-item OCR route of `tools/ia_text.py`.

| Sub-route | Query | Answer | In-window Tier-1 text? |
|---|---|---|---|
| Internet Archive `advancedsearch` | `"tesla motors" electric car AND mediatype:texts`, window 2003–2007 | numFound **6** | **NO** — the six hits are trade books dated **2015, 2015, 2015, 2017, 2018, 2015** (Vance's *Elon Musk: Tesla, SpaceX…*, two IA copies; *Car wars…*; *The Tesla revolution…*; *SpaceX and Tesla Motors engineer Elon Musk*). Not periodicals, not in-window. |
| Internet Archive `advancedsearch` | `"tesla motors" roadster AND mediatype:texts`, 2004–2008 | numFound **0** | No — a real metadata-layer null |
| Internet Archive `advancedsearch` | `Tarpenning Eberhard AND mediatype:texts`, 2004–2016 | numFound **0** | No — metadata-layer null |
| HathiTrust | `"Tesla Motors" electric roadster San Carlos` | **Cloudflare "Just a moment…" interstitial**, 6,113 B held | **UNANSWERED** (bot-block; reproduces the known expired-CA/blocked-host condition on this egress) |
| Chronicling America (LC historic newspapers) | canary, 2003–2008 | **HTTP 403**, 1 row `UNANSWERED` | **UNANSWERED** — the same 403 the nvidia pass recorded, so it is a standing property of this egress, not a fluke. Note the pass-1 defect honestly: my first config used unpublished CA parameters (`q`, `from`, `to`), the harvester refused to invent one and raised mid-run **after** the other 8 requests were already saved; pass 2 with `--source-family chronicling_america` produced the 403 above. |
| Google Books volumes feed | `"Tesla Motors" Eberhard Tarpenning founded`; `"Tesla Motors" Musk founder Straubel` | 2 × HTTP 200 Atom feeds, 27,950 B and 26,203 B held | **NO** — volume lists only, dated 2016–2026 (incl. *Ludicrous: The Unvarnished Story of Tesla Motors*). Retrospective carriers, and **not opened** |
| `ia_text.py mine` on the 2015 Vance item `elonmuskteslaspa0000vanc` | identifier-scoped search → fetch → grep | search returned the item but the pipeline reported **0 items mined / UNANSWERED**; no OCR text layer written | **UNANSWERED**, not a null: the book's page text was never held, so no sentence from the best-known founder-account carrier is quotable here |

**The methodological point, stated so the next agent does not repeat the mistake.** §14.6 prescribes
periodicals as the family that carries contemporaneous text for the period EDGAR and web archives
miss — but it carries it *only where the search route can see into pages*. IA `advancedsearch` matches
item metadata/annotations, and `ia_text.py`'s own docstring records the Microsoft-probe finding that a
`text:` hit can return a scan containing zero occurrences of the term. For a 2004 magazine or newspaper
page that mentions Tesla Motors without saying so in the item's catalog record, this route is blind,
and **numFound 0 is a statement about the catalog, not about the press**. No per-item full-text route
(`fulltext/inside.php`) was run against a candidate periodical, because no candidate periodical item
was identified: the searches above surfaced books only. **Family c therefore returned zero in-window
Tier-1 text and one honest structural null at the metadata layer; the periodical *page-text* layer is
UNTRIED.**

STATUS: WRITTEN 2026-09-26

## Family d corporate print

**Route:** `periodical_harvest.py --source-family corporate_print` (an IA title/creator-scoped search
built to find company-published print: annual reports, shareholder letters, brochures, product decks).

* Title-scoped, terms `tesla motors / tesla / teslamotors`, report terms `annual / report / shareholder
  / prospectus / roadster`, 2003–2010: **numFound 2** —
  `tesla-logo` "Tesla, Inc. Annual Reports" (metadata year **2003**) and `teslaroadster0000maur`
  "Tesla Roadster" (year **2008**).
* Creator-scoped, no report terms, 2003–2012: **numFound 0**.

**Reading.** The `tesla-logo` item's metadata year of 2003 cannot be taken as a 2003 company document:
an IA "Annual Reports" collection item labelled 2003 is a *container* whose date field is set by the
uploader, and Tesla's first annual report as a public issuer was for FY2010 — a 2003-dated report in
this collection is either a mis-dated aggregation or a later compilation. **This is precisely the
inherited-figure trap in §14.8: the item was not opened, so no date from it is written into this
dossier as evidence.** The `Tesla Roadster` (2008) item is a plausible genuine corporate-print
artefact of the *product* period — the brochure/deck family that would corroborate in-period product
claims — and it, like the two above, is a **FETCH REQUEST**, not evidence.

**Consequence for the founder question:** the corporate-print family produced **no held founding-window
text**, but unlike the web and periodical families it produced **two named, identified candidate
items** and no HTTP failure — the block here is my remaining budget, not the network. That is why
family d is scored "answered at metadata layer only" in §Verdict rather than UNTRIED.

STATUS: WRITTEN 2026-09-26

## Family e documentary

**NOT TRIED. This is a gap, not a null, and it is the largest one in the pass.**

§14.6's fifth family — auction and museum documentary sale records — is the family that, on Apple,
returned surviving founding documents (handwritten price lists, early letterhead) with dates EDGAR and
the web cannot reach. For Tesla the analogous objects would be: a 2003–2004 founding-era letterhead,
invoice, sales brochure or business plan; the original Roadster prototype signage; the founders'
hand-signed share or subscription papers; and — highest value of all — **any 2003–2004 document bearing
Musk's signature or absence of it**, which is the class of object that could bear on attribution
without being anyone's memory of it.

What was actually done: **nothing.** `tools/periodical_harvest.py` implements no auction/museum route
(families are internet_archive, corporate_print, hathitrust, google_books, chronicling_america), no
other script reaches sale-catalogue data, and no hand query was attempted against a catalogue, because
every remaining call in this pass had to go to closing the other families and writing the file.
**No claim of "no founding documents survive" is made or licensed by this dossier** — an untried family
is not a null (§14.6), and for the specific question the probe exists to serve, documentary evidence is
the family most likely to contain something that is neither the company's account nor the founder's.

STATUS: WRITTEN 2026-09-26

## Boundaries

Each boundary below names the document that fixes it, and says whether that document is contemporaneous
or retrospective. **Every date in the founding period is fixed by a retrospective instrument** — the
earliest carrier is 2009-04-09 (a Form D) and the earliest narrative carrier is 2010-01-29 (the S-1) —
so the whole Stage-1 frame is one company telling a securities regulator what happened seven years
earlier. That is stated here once and it qualifies every row.

| Boundary | Date | Fixing document (held) | Contemporaneity | Confidence | Why this edge and not another |
|---|---|---|---|---|---|
| **Stage 1 opens** — the entity exists | **2003-07-01** | 424B4 Note 1 (2010-06-29) and FY2010 10-K Note 1 (2011-03-03) — one corporate lineage | RETROSPECTIVE SOURCE for a 2003 event | **High** that the entity's own filings fix this date; **Medium** that it is the true date (no Delaware certificate, no county filing, no third party holds it) | It is the only inception date the corpus contains and the only one an auditor's report is attached to. Not chosen: 2004-04 (that fixes a *relationship*, not an existence), and not the "idea" layer (no carrier at all — see the contested-pre-history row) |
| Stage 1 internal marker — first governance act | **July 2003** (month precision only) | 424B4: board adopted, stockholders approved the 2003 Equity Incentive Plan "in July 2003" | RETROSPECTIVE | Medium | A plan adopted in the incorporation month is the earliest *act* (as opposed to *status*) in the record; the filing gives month precision only, so the boundary stays month-level per §13 |
| **Contested pre-history — recorded, not deleted** | 2001 → 2003-06-30 | **no held document** | n/a | **UNKNOWN** | This is the interval in which the attribution dispute lives: any account of who conceived the company, who was talking to whom, and who was funding it *before* incorporation has **zero carrier in this corpus**. The only artefacts reachable for the interval are three `tesla.com` root captures (2002-11-25, 2003-02-09, 2003-02-14) that **pre-date the entity** and therefore cannot be its history. Deleting the interval would silently resolve the dispute in favour of the entity's own dating; keeping it open is the finding |
| Stage 1 closes / **Stage 2 opens** — first documented participation of the disputed founder, and first documented engineering hire | **2004-03 → 2004-04** | S-1 2010-01-29 (Straubel "Principal Engineer, Drive Systems from March 2004"; Musk "Chairman … since April 2004") | RETROSPECTIVE | **High** as role-start statements; the *inference* that these bound the founding is **Low** | These are the earliest dates the lineage assigns to living named individuals. They are used as a Stage edge because they are the earliest **person-level** evidence, not because they are the earliest evidence of the company |
| First financing — **boundary NOT FIXABLE from held bytes** | **UNKNOWN** (structure known, date absent) | 424B4: Series A convertible preferred, 7,213,000 shares at $0.49, $3,549k net; Series B $0.74, $12,899k; Series C $1.14, $39,789k | RETROSPECTIVE | Medium as to amounts; **UNKNOWN as to dates** | String-checked: **0 occurrences of "February 2004"** anywhere in the held S-1/424B4/10-K/proxy text. The equity structure is filed; the closings are not, in the four documents taken. The fix is the S-1 exhibit index (Series A purchase agreement / founder-share purchase agreements), which is inside the same accession folder and was not fetched this pass — see §Untried U-4 |
| **Stage 2 → Stage 3** — first revenue-generating product in customers' hands | **"early 2008"** vs **"≈2008-09"** | 424B4 risk factor: "began delivering our first performance electric vehicle, the Tesla Roadster, in early 2008" — vs FY2010 10-K: "In June 2009, nine months after its commercial introduction" | Both retrospective, both the same registrant, **mutually inconsistent by ~2 quarters** | Medium at best; **this edge is contested inside one company's own corpus** → see U.5 | Two candidate edges with the same source and different implications; recorded as a conflict rather than averaged into "2008". The 10-K arithmetic (June 2009 minus nine months) is the tighter date-type; the S-1 phrase is the more explicit event-type |
| **Stage 3 opens** — scalable company formation | **2010-06-29** | 424B4 (final prospectus, effective S-1 2010-06-28); 646 full-time employees at 2010-05-31 across 6 named functions and 3 locations | **CONTEMPORANEOUS** — the only founding-window-adjacent document in this dossier that is not retrospective | **High** | This is the first date in the whole pass fixed by a document written at the time it describes, which is why the probe's own confidence profile jumps here. Everything before 2009-04-09 is memory-on-file; from here it is record |

**Hindsight firewall applied.** No boundary above is justified by the 2026 outcome. The IPO date is not
"when Tesla became real"; the 2003 date is not "when the future giant started". Each edge is fixed by
the earliest document that states it and is labelled with that document's date and genre. And per §2's
record-selection null: what is unrecoverable here is not merely "detail" — the entire **2003–2008
internal record of a private company with no filing duty** is gone by structure, and what survives in
its place is a 2010 securities narrative authored for a sale, plus a founder's-own-account genre that
this pass could not reach. A reader should expect the founding of this company to stay
**single-voiced** no matter how many documents are added, unless the added documents are *non-corporate*.

STATUS: WRITTEN 2026-09-26

## Conflicts

Six live conflicts. Each keeps both claims, names each claim's carrier and carrier date, and none is
resolved by averaging, by recency, or by preferring the corporate voice. Register mirror:
`conflicts.csv`.

**U.1 — When Tesla began**
CLAIM A: the entity began 2003-07-01 (Delaware incorporation). Carrier: 424B4 Note 1 (2010-06-29), FY2010 10-K Note 1 (2011-03-03), S-1 risk factor "formed in July 2003" (2010-01-29) — **one lineage, all retrospective**.
CLAIM B: the operative beginning is the 2004 money-and-hire layer (Chairman from April 2004, first engineering hire March 2004, first financing round in the same months). Carrier: the *same* lineage — the S-1's own role dates and the Series A/B/C structure.
WHY THEY DIFFER: a legal-entity inception date and a company's first functioning moment are different events, and the registrant needed the former for accounting ("since inception" losses) while the disputed account needs the latter for attribution. EVIDENCE WEIGHT: both claims are carried by the **same single corporate voice**; neither is corroborated externally. BEST-SUPPORTED INTERPRETATION: Stage 1 **opens** 2003-07-01 as an entity fact and the 2004 layer is a separate, later, person-level fact; the two are ordered, not alternatives. RESIDUAL UNCERTAINTY: whether a functioning team existed between 2003-07-01 and 2004-03 — no carrier reached. CONFIDENCE: High on the dates, **Low on the meaning of the gap**.

**U.2 — Is the CEO a founder of the entity, and in what capacity?**
CLAIM A: he is "one of our founders". Carrier: S-1/A 2010-04-29 (first held instance), 424B4 2010-06-29, DEF 14A 2011-04-08 — the registrant's own words, in a director-qualification paragraph, **absent from the original S-1 of 2010-01-29**.
CLAIM B: his documented relationship begins April 2004, nine months after inception, and the equity he held was investment-acquired preferred stock rather than founder's compensatory stock. Carrier: S-1 2010-01-29 ("Chairman … since April 2004"; "contributed significantly and actively to us since our earliest days in April 2004…"), DEF 14A 2011-04-08 ("preferred stock acquired via investment as was the case with Mr. Musk").
WHY THEY DIFFER: A is a characterisation added mid-registration; B is the dating and the capital structure stated in the same documents. The plausible mechanism — that the phrase entered the filing after press attention to the founder question — is **INFERENCE, and its motive is UNKNOWN from held bytes**; nothing in the corpus states why. EVIDENCE WEIGHT: A and B are **not independent**; both are the company's drafting. A company's retrospective self-description cannot corroborate an attribution claim, and per §3 the four documents here count as one lineage. BEST-SUPPORTED INTERPRETATION: the corporate record simultaneously (i) applies a founder label to Musk, (ii) dates his first role to April 2004, and (iii) characterises his equity as purchased — the three are **held in the same instrument and are not reconciled by it**. **No averaging: this dossier does not output "co-founder" as a settled fact, nor "not a founder".** RESIDUAL UNCERTAINTY: what Musk did between 2001 and 2004-04, and whether anything of his was in the entity before April 2004 — unanswerable from held bytes. CONFIDENCE: High (the conflict itself is documented), **UNKNOWN (the underlying question)**.

**U.3 — Who is called a founder and who is not**
CLAIM A: the two named early officers are not labelled founders anywhere in the corpus; they appear only as "former officer and director" (2010-01-29, 2010-06-29) and are absent from the FY2010 10-K entirely (0 hits for `Tarpenning`, 0 for `founder`). Carrier: same lineage.
CLAIM B: an external account treats at least one of them as the founder/co-founder. **Carrier NOT HELD this pass** — identified candidates are the 2015 trade book `elonmuskteslaspa0000vanc` (IA metadata hit; text layer never fetched, so its words are not quoted) and un-held interviews/press.
WHY THEY DIFFER: genre. An issuer lists people by the office they held at the measurement date; a biography lists them by the origin they narrate. EVIDENCE WEIGHT: A is held, dated and single-voiced; B is asserted by the probe's brief but **unverified in this pass** — recorded as a carrier to fetch, not as a fact. BEST-SUPPORTED INTERPRETATION: the corporate record's silence about a founder label for the early officers is a **drafting fact**, and must not be upgraded into evidence against them. RESIDUAL UNCERTAINTY: complete, on side B. CONFIDENCE: High (A), **UNKNOWN (B, unheld)**.

**U.4 — The domain's history is not the company's history**
CLAIM A: `tesla.com` has archived captures from **2002-11-25** (and 2003-02-09, 2003-02-14), status 200. Carrier: Wayback CDX index rows held this pass.
CLAIM B: Tesla Motors, Inc. came into existence **2003-07-01**. Carrier: 424B4/10-K Note 1.
WHY THEY DIFFER: the domain pre-existed its namesake registration; capture timestamps index a URL, not an owner. EVIDENCE WEIGHT: both are Tier-1 in their own kind (registry index vs issuer statement) and **neither is in conflict once the object is identified** — they answer different questions. BEST-SUPPORTED INTERPRETATION: earliest-capture evidence for a 2003-founded company **must be checked against the incorporation date before being treated as the company's first web presence**; here it fails that check, and the first plausibly-company capture in the held rows is 2006-02-09, which is a 302 redirect shell. RESIDUAL UNCERTAINTY: when the entity actually put a site on `tesla.com` — needs a domain-scoped CDX sweep and one page fetch (blocked by the 504/offline outage this pass). CONFIDENCE: High (both claims), High (the resolution rule).

**U.5 — When did the Roadster reach customers (Stage 2→3 edge)**
CLAIM A: "We began delivering our first performance electric vehicle, the Tesla Roadster, in early 2008." Carrier: 424B4 (2010-06-29) and S-1 (2010-01-29), same wording.
CLAIM B: "In June 2009, nine months after its commercial introduction…" ⇒ introduction ≈ 2008-09. Carrier: FY2010 10-K (2011-03-03).
WHY THEY DIFFER: most likely two different referents — first customer deliveries of hand-built/pre-production cars vs a declared "commercial introduction" milestone — but the corpus does not say so, and both sentences are the same registrant. EVIDENCE WEIGHT: equal, and **not independent**. BEST-SUPPORTED INTERPRETATION: the Stage-2→3 edge is **2008 (quarter UNKNOWN)**; the ~2-quarter spread is preserved, not smoothed. RESIDUAL UNCERTAINTY: exact delivery date of the first production Roadster (Tesla's own public count of the first-delivery event is a 2008 press item — unheld; family b blocked). CONFIDENCE: Medium on 2008, Low on the sub-year.

**U.6 — The classifier's flag against the documentary record**
CLAIM A: a 2026 list flags Tesla `Founder is CEO = yes`. Carrier: the brief's own framing (present-day third-party classification; **no document held**).
CLAIM B: the earliest dated corporate record places the CEO's first office in April 2004 as Chairman and his CEO office in **October 2008** — i.e. the person flagged as founder-CEO was neither founder-at-inception (per the dating) nor CEO for the first five years. Carrier: S-1 2010-01-29.
WHY THEY DIFFER: a binary list field resolves, by fiat, a question the record leaves open, and it is computed in 2026 from an account genre this pass did not reach. EVIDENCE WEIGHT: A is a present-day label; B is a dated primary statement. A label is never corroboration. BEST-SUPPORTED INTERPRETATION: the flag is recorded as **an artefact of the dispute, and one of the reasons the dispute is now hard to research** — by 2026 the contested account is the one encoded in structured data. RESIDUAL UNCERTAINTY: the flag's derivation. CONFIDENCE: High (B's dating), n/a (A is not evidence).

STATUS: WRITTEN 2026-09-26

## Nulls

Distinguished per §12/§14.6 into **NULL** (searched bytes held, zero hits), **UNANSWERED** (a request
failed: 0 B, 403, 504, offline, interstitial) and **UNTRIED** (§Untried). No UNANSWERED is written as a
null anywhere in this file.

**Documented nulls over held bytes (string-verified, this pass):**

| # | Zero result | Searched scope | Interpretation |
|---|---|---|---|
| N1 | `arbitrat` → **0 hits** | 4 held documents, ≈5,916,644 B of HTML / ≈2.7 M characters of tag-stripped text (S-1, S-1/A, 424B4, FY2010 10-K, 2011 proxy) | The registrant's own 2010–2011 disclosure corpus nowhere mentions the founder litigation. Evidence about the *corporate account*, not about whether a dispute existed |
| N2 | EDGAR filings dated 2003-01-01 → 2009-04-08 → **0 of 1,750** | `sources/_index/submissions.csv`, full window slice | No filing carrier exists for the founding period at all. A registry-scope fact, not an absence of records anywhere |
| N3 | `founder`/`co-founder` of Tesla in the FY2010 10-K → **0**; `Tarpenning` → **0** | 10-K held bytes (608,382 chars text) | The periodic report drops the 2010 prospectus's founder adjective entirely. Dated drafting difference between two instruments of the same issuer |
| N4 | `Gottschlich` → **0**; `February 2004` → **0** | all 5 held documents | The first-financing closing month and one named early figure are absent from the four documents taken |
| N5 | `Ian Wright` → **0 in the 2010-01-29 S-1**, **1 in the 424B4** (180,188 shares, beneficial-ownership table) | 2 held documents | An early individual holder enters the record only in the later instrument — shows the lineage *accretes* founding-period detail under amendment, which is why one lineage must not be read as one static statement |
| N6 | IA metadata `numFound 0` ×2 (`"tesla motors" roadster`; `Tarpenning Eberhard`) and corporate-print creator-scoped `numFound 0` | 3 saved query responses | Null **at the catalog layer only**; the page-text layer was never searched (see §Family c) |
| N7 | No Delaware certificate of incorporation, no county/corporate-registry document, no auditor's independent chronology in the corpus | enumeration of `sources/` | The founding-period date has **no non-corporate carrier held**. This is the null that caps every date in §Boundaries at Medium |

**UNANSWERED (attempted, service refused — retained as negative artefacts, never reported as absence):**
Wayback CDX domain-scoped 2003–2005 → **504**; CDX 2008–2011 founder-page filter → **0 B**; CDX re-query →
**IA "Temporarily Offline"** HTML; HathiTrust → **Cloudflare interstitial**; Chronicling America →
**HTTP 403** (twice, on two different company passes); `ia_text` mine on the 2015 book item → **0 mined /
UNANSWERED**; San Mateo County / California Superior Court registry → **never reached** (no route, so the
possibility that the docket is publicly indexable is entirely open). A blocked registry is UNANSWERED, and
the founding dispute is not thereby shown to be undocumented.

STATUS: WRITTEN 2026-09-26

## Untried

**The biggest gap in the pass: the dispute's own documents were never reached.** Everything the dossier
can say with High confidence is *about the corporate voice*; nothing it holds is an independent witness
to 2003–2004. Ordered by expected forensic yield per call.

- **U-1 / FETCH REQUEST** — Wayback: domain-scoped CDX for `tesla.com` **2003→2009** (`matchType=domain&from=2003&to=2009&fl=timestamp,original,statuscode`), then the raw `id_` snapshot of the company's **August 2009 joint statement** page about the founder dispute. This is the only object that could carry the disputants' **joint, contemporaneous, dated** words. Retry (Archive was degraded, not absent). Bytes → `sources/wayback/`.
- **U-2 / FETCH REQUEST** — Court/docket: **San Mateo County Superior Court** civil case register search (2008–2009, Musk v. Eberhard/Straubel), or the California state-docket index, or a secondary registry that carries state trial courts. CourtListener v4 (held) covers federal courts only, so this remains **untouched**; a settled filing here would be the pass's only genuinely independent Tier-1 carrier.
- **U-3 / FETCH REQUEST** — Founders'-own and CEO's-own statements: no interview, transcript, post or book text was held. Start with `ia_text.py fetch --id elonmuskteslaspa0000vanc` (the route returned UNANSWERED without a diagnostic this pass — retry with `--max-mb 20` and capture the HTTP status), and an IA/HathiTrust periodical **per-item full-text** query (`fulltext/inside.php`) against a 2004–2006 magazine item, which is the only way to search *inside* periodicals here.
- **U-4 / FETCH REQUEST** — `sec_intake.py grab --accession 0001193125-10-149105` **without `--file`**, to get the S-1/424B4 **exhibit index and exhibits**: certificate/restated charter, Series A–D purchase agreements, 2003 plan documents, employment agreements. This is where the **first-financing dates (N4)** and possibly the incorporator/first-director slate sit, inside an accession already resolved.
- **U-5 / FETCH REQUEST** — Corporate print: `ia_text.py fetch --id tesla-logo` and `--id teslaroadster0000maur` (both identified in family d, neither opened). An unopened candidate is not evidence and its metadata year is not a date (§Family d, §14.8).
- **U-6 / FETCH REQUEST** — Documentary/auction family (**entirely untried**, §Family e): founding-era letterhead, invoices, business-plan or brochure sales records; the class of object that could bear on attribution without being anyone's memory.
- **U-7 / FETCH REQUEST** — Delaware Division of Corporations (entity file / charter date) and, if reachable, USPTO **patent** records naming early inventors/assignees 2004–2008 — an independent dated registry of the entity's technical activity.
- **U-8** — Non-LA Bay Area contemporaneous press, 2004–2006, via a route not blocked from this egress (LOC Chronicling America is 403; try HathiTrust through a working proxy or a library-union catalogue), and trade-press coverage of the **2004-09 "Flash Forum"** style first public appearances — corporate print that a third party printed.

**Explicit non-claims, so the next pass does not over-read this one.** This dossier does **not** claim:
that no independent record of the founding exists; that the founder question is resolved either way; that
the corporate dating is wrong; or that any named person is or is not a founder. It claims that on
2026-09-26, from bytes in `sources/`, the founding of Tesla Motors, Inc. is documented by **one voice, in
two datable layers (a July 2003 entity statement and an April 2004 relationship statement), with a
founder adjective that entered the filing between 2010-01-29 and 2010-04-29 — and by no second voice at
all.** "We cannot know", on this evidence, is the deliverable.

STATUS: WRITTEN 2026-09-26

