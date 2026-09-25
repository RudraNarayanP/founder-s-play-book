# APPLE STAGE 1 — DOSSIER B: FOUNDER FORENSICS

Dataset: THE FOUNDER'S PLAYBOOK — forensic reconstruction of early company state.
Company: **Apple** (`company_004`), Fortune-50 universe rank #4.
Stage: **1 — origin → first real-world test**, span **1975 → 1977-01-03** (the span fixed by
`A_chronology_feasibility.md` and re-confirmed by `D_adversarial.md`; the partnership era, closing at
the corporation date 1977-01-03). Subjects: **Stephen (Steve) Jobs, Stephen (Steve) Wozniak, Ronald
(Ron) Wayne, A. C. (Mike) Markkula** — treated as founder-state subjects, not as biographies.
Dossier type: **founder-state reconstruction from dated public evidence**. Local corpus mined first;
web budget hard-capped at 10 and spent only after this file was on disk.
Governing spec: `00_METHOD_AND_STYLE.md` §2 (hindsight firewall + record-selection null), §3 (claim
classes, confidence, independence, filing-lineage), §5 (tiers), §6 (time audit), §7 (section set,
claim-record line formats — field list taken verbatim from §7's "C. FOUNDER STATE"), §8 (table
discipline), §13 (CSV schemas), §14 (retrieval discipline, rules 1–8).

**Hindsight-firewall statement for this dossier.** Nothing recovered here is used as evidence that
1975–77 founder choices were correct, that any of the four subjects was "destined", or that the
1980 corporation is readable backwards into the 1976 partnership. The IPO-year print (BYTE February
1981) is admitted **only** as a dated witness reporting earlier facts, and every sentence taken from
it that describes 1976–77 is tagged `RETROSPECTIVE SOURCE` with its class capped accordingly. The
famous anecdotes are treated as the primary hazard of this file, not as its content: each is traced to
its first dated appearance in the material this project can actually read, and classified there.
**Anti-hagiography test applied per §2:** the narrative notes are written so that they would still
read as plausible had Apple gone the way of Sphere, IMSAI or Processor Technology, all of which appear
as dated in-window competitors in the same pages.

**Record-selection null (§2), stated for this dossier specifically.** What is unrecoverable about
Apple's founders in Stage 1 is unrecoverable *because the surviving archive is not theirs*. The
periodical corpus that carries the company's first two years (BYTE 1975–77 and 1980–81, Homebrew
Computer Club newsletters, and the intake titles Creative Computing and Kilobaud) was kept by an
editor, a club, and dealers. It records products, prices, addresses and dealer lists. It records
almost nothing about persons: per A2's corpus-wide name census (A2-61a), `Wozniak` occurs in **four**
cached files and `Jobs` as a personal name in **three**, and there is **no mention of either founder in
any 1976 BYTE issue except the December editorial**. The founders' interior — what they were paid,
what they owned, who refused them, what they argued about, what they could actually raise — leaves no
trace in this family at all. The single 1976 documentary artifact of the partnership exists only as an
auction lot **this project has not read** (`D_adversarial.md` L-8, W9 `fetch failed`). A dossier on
"the founders as they were" written from this record can therefore only be a dossier of **dated
utterances about them**; where the record is silent the file prints UNKNOWN and names the artifact
class that would settle it, and it must not fill the silence with the memoir tradition.

**Confidence scale (§3).** High = 2+ independent origins or a primary document · Medium = one reliable
source · Low = conflicting, vague, or retrospective-only · UNKNOWN = no evidence recovered.

**Record class vocabulary (§3).** FACT / FOUNDER CLAIM (sub-tagged *contemporaneous* vs *retrospective
memory*) / CONTEMPORARY OBSERVATION / RETROSPECTIVE INTERPRETATION / INFERENCE / ESTIMATE / DERIVED /
UNKNOWN.

**Relationship to sibling dossiers (citation discipline).** This file does **not** re-derive what
`A_chronology_feasibility.md` (AP-nn), `A2_periodical_archive_mine.md` (A2-nn, U-A2-nn) and
`D_adversarial.md` (E-nn, L-n, H-n, D-n, DG-Dn) already established; it cites their record IDs and
builds the founder-state layer on top. Where this pass re-verifies a claim at line level in the cached
files it says `re-verified by this pass`. Where it inherits without re-verification it says
`[inherited]`. Per A2's finding and D's L-7 correction, **`Wayne` and `Markkula` are effectively absent
from all in-window print** — `Wayne` returns only third parties in the cached corpus and `Markkula`
occurs exactly once in 13 MB, in BYTE February 1981 — so **every claim about those two carries its true
vintage on its face**, and the 1981 and 2018–2026 witnesses are labelled as such rather than silently
allowed to speak for 1976.

---

## Working method

**What was mined locally (0 web requests against these; `sources/` is a protected read-only archive
per §14 rule 4 — nothing in it was created, moved, renamed, tidied or deleted by this pass).**

| Corpus | Extent on disk | Dated | Use in this dossier |
|---|---|---|---|
| `sources/ia_byte_1976/byte-1976-01..12.txt` | 12 full-issue IA OCR text layers, ≈5.7 MB | Jan–Dec 1976 | the 1976 silence baseline: what print did and did not know about the two visible founders |
| `sources/ia_byte_1977/byte-1977-04..07.txt` | 4 full-issue layers, 682–797 KB each | Apr–Jul 1977 | Wozniak's own byline and article; Apple's own advertisements; Helmers' 1976-11-20 sighting |
| `sources/ia_byte_1981/byte-1980-12.txt`, `byte-1981-02.txt` | 2 full-issue layers, 1.6 MB each | Dec 1980, Feb 1981 | the only print carrying ages, shareholdings and the "garage operation" gloss — `RETROSPECTIVE SOURCE` for Stage 1 |
| `sources/ia_homebrew/` (13 items) | hcc0109, hcc0110, hcc0201–0207, hcc0209, hcc0211, hcc0213, hcccf | 1975-11-30 → 1977-02-16 | club-level sightings of the subjects; the CPU census; the Faire flyer |
| `sources/10-K_FY1994_acc-0000320193-94-000016_filed-1994-12-13.txt` | 1 filing text | filed 1994-12-13 | the recital "incorporated … California on January 3, 1977"; nothing about persons |
| `sources/apple1registry_stories.txt` / `.html` | collector curation, published 2018–2022 | retrospective | artifact existence (1973 application, Koa cases, Wayne's letter); **never** used as a 1976 witness |
| `sources/EDGAR_*`, `sources/probe_*` | registry/probe indexes | 2026-09-24 | coverage facts only |
| `00_universe/harvest/periodicals_intake/apple_microcomputer_sector/` | **newer intake**: `SEARCH_LOG.md`, `BYTE_1977-09_EXTRACT…txt`, `CREATIVECOMPUTING_1977-11_EXTRACT…txt`, 2 IA inventory JSONs | retrieved 2026-09-25 | BYTE **September 1977** (a new month of a held title) and Creative Computing **Nov/Dec 1977** (a new title): Apple's own full-page advertisement in a third month, the advertiser-index page numbers, the Atari trademark line, and two dealer advertisements naming Apple as a stocked brand |

**Header-exclusion protocol (mandatory; the trap is documented).** The caching probe wrote four-line
provenance headers into the cached files that contain the literal token `company_004_apple`, so a
case-insensitive grep for `apple` over these files returns **at least one hit per file by
construction** (`D_adversarial.md` L-7.2, verified at hcc0109:2, hcc0110:2, hcc0201:2, hcc0202:2,
hcc0203:2; A2 noticed it at §Working method and A2-77). Two further carriers exist: the intake extracts
carry their own multi-line `# [PROVENANCE HEADER …]` blocks naming Apple and BYTE, and each extract's
own header line counts as a hit for `apple`. **Protocol applied in this pass:** every grep was run
across the four `sources/ia_*` directories and the intake directory, and its output was then filtered
to (i) drop any line whose content contains `company_004_apple`, `PROVENANCE`, `Retrieved`,
`archive.org`, `ia60`, `ia80`, `https`, or `_djvu.txt`, and (ii) read the surviving hit **in context**
before it was counted — a token hit is not a record. The consequence is stated positively rather than
as a disclaimer: all four founder-state **personal-name** records in this dossier (`Jobs`, `Wozniak`,
`Markkula`, and the negative for `Wayne`) were individually read in their surrounding paragraphs
before being written down, and the two 1981 lines are cited with line numbers rather than as
whole-sentence greps, because D's L-7.1 shows that the hard-wrapped filing text produces **false
negatives** under naive one-line matching.

**Independence discipline (§3, incl. the filing-lineage rule).** Company-side documents are one
interest even when they are several documents: Wozniak's May 1977 article, Apple's June 1977
advertisement, and Apple's September 1977 advertisement are **three documents, one company**, and are
never counted as corroborating each other. A run of the same dealer advertisement across months is
**one campaign with a duration**, not multiple witnesses (A2's rule, adopted). The FY1994 10-K and the
BYTE February 1981 column are genuinely independent of one another (different author, publisher,
decade, no shared lineage) — D's H-1 — and this is the only real corroboration pair available for any
founder-state fact. Repeated web restatement of the memoir tradition (RR Auction, apple-1-replica,
historyofinformation, Wikipedia) is **one lineage** however many sites carry it (D's L-1, L-2).

**Budget.** Local mining: unlimited, and completed first (batches 1–3, 0 web requests). Web: **10 of 10
requests spent** after the file was on disk with ≥10 records, all ten aimed at founder-state fields print
can date — Atari and HP employment, Homebrew membership, the partnership instrument's signatories, education
(B-42…B-45, and the W1–W10 table in §Sources consulted). **Net result: no field moved from UNKNOWN to
FACT; three legends gained a first-dated carrier, and one new route to the founding instrument was found
and could not be decoded by the fetch tool.** Every failure is recorded as UNANSWERED with its status code.

---

## Founder state, field by field (§7 "C. FOUNDER STATE")

Field list taken from method §7 and applied to each of the four subjects. The governing rule of this
dossier, and the reason it looks thin: **a field is populated only where a dated document populates
it.** `UNKNOWN` is a complete value (§8), and each UNKNOWN names the artifact class that would
evidence it. Reputation is not evidence of capability; capability is evidenced by work products
(§"capability" rows below).

### B.1 STEVE JOBS as of 1975 → 1977-01-03

| Field | Value | Source | Confidence |
|---|---|---|---|
| Age in window | **UNKNOWN from in-window print.** Only witness: BYTE Feb 1981 "Steve Jobs, 25 years old" → DERIVED birth c. Feb 1955, so **c. 20–22 at the 1976-04-01 partnership** (integer ages, ±1 yr band) | A2-60; `byte-1981-02.txt`:48509 (re-verified by this pass) | Medium for the printed age; Low for the 1976 inference |
| Education and completion status | **UNKNOWN at Tier 1.** No in-window document states schooling, attendance or a degree. The 1973-ish handwritten job application reproduced in a collector registry is the only first-party educational-adjacent artifact and its date is a curator's inference | E-30; `sources/apple1registry_stories.*` [inherited] | Low (artifact exists; date and reading are curator-supplied) |
| Career and employers, with dates | **UNKNOWN at Tier 1.** Atari employment is asserted only by curated auction prose and by a 2011 trade-press headline ("Steve Jobs, Atari Employee Number 40") whose body this pass could not retrieve; the cached corpus contains **no personal-name connection to Atari** — the string occurs only inside Apple's own advertisement, as a trademark notice for a game, and in unrelated coin-op advertising | A2-61c; re-verified by this pass in the intake BYTE Sept 1977 layer (extract §B, "PONG is a trademark of Atari Inc."); B-38, B-42 | High (documented absence in this family); Low on the Atari claim itself |
| Technical capability, as evidenced by work products | **NONE in-window.** No 1976–77 document attributes a design, a circuit, a line of code, a manual or an article to Jobs. His name appears in a byline address block only as a company marker. One qualification this pass can add: a single outside witness describes a programming session he took part in (B-32), which bars the claim that he wrote the software **and** bars the claim that no technical act of his was ever witnessed | A2-59 (print "does not say"), A2-57; B-32 | High (absence of any product); Low on the session's meaning |
| Business/commercial capability, as evidenced by work products | **Weakly evidenced, but better than A2 allowed.** He is named as present at a trade show and — uniquely — **classified as an operator by an outside editor**: Helmers lists him among four "entrepeneurs" he conversed with at WESCON in September 1976 (B-31). Still: no title in any document (B-37), no negotiation, no invoice, no account, no signature | A2-56, A2-31, B-31, B-37 | Medium-High for the naming and the class-word; UNKNOWN for any function |
| Design capability | **UNKNOWN.** No in-window artifact assigns him any design function | — | UNKNOWN |
| Prior ventures and prior failures | **UNKNOWN at Tier 1.** The "Blue Box" venture has no in-window document anywhere in the cached corpus and is classified FOLKLORE/UNKNOWN by D; no dated evidence of any venture of his preceding Apple | E-34 | Low; folklore class |
| Personal network as observable in dated documents | Five dated edges, and this is the field that moved most under mining: (i) **Wozniak** — co-named in the Dec 1976 clause and in the 1976-11-20 session; (ii) **Carl Helmers / BYTE** — met him, dated to the day; (iii) **Paul Terrell, Bob Marsh (Processor Technology) and Chris Rutkowsky (Technical Design Labs)** — all four named as peers in one December 1976 sentence recording a September 1976 conversation (B-31); (iv) **the Faire circuit** — the company is a billed exhibitor from Dec 1976, organised by Jim Warren and Bob Reiling (B-40). **No introduction is documented at any date** | A2-56, A2-31, B-31, B-40 (H-4) | Medium-High for the edges; the introduction question is UNKNOWN |
| Financial constraint / what he could put up | **UNKNOWN.** Every quantified founding-capital story attached to him (HP-65 sale at $500, VW bus at $750, a $15,000 loan) traces to memoir or to one participant's retrospective account; none is documented in this evidence family | E-13, E-14, DG-D9 | Folklore / Low |
| Employment status in window | **UNKNOWN.** No payroll, no employer record, no self-description of employment in any cached file. His company carries no officer title for him in any 1976–77 document (B-37) | B-37 | UNKNOWN |
| Location and living situation | **UNKNOWN for residence.** Publicly documented locations of *presence*: the WESCON floor, **Los Angeles, September 1976**; a Palo Alto motel room on 1976-11-20; the company's address of record from 1977-05 is Cupertino, 20863 Stevens Creek Blvd Bldg B3-C. The claim that he lived or worked at 20211 Crist Drive, Los Altos is **UNSOURCED within the period and not refuted** | A2-31, A2-58, B-31, E-07, H-7 | Medium-High for presence; UNKNOWN for residence |
| Division of labour | **Absent from every 1976–77 text on disk.** Wozniak's May 1977 article and Apple's June 1977 advertisement attribute no function to Jobs | A2-59, B-08 | High (documented absence) |
| Documented blind spots | Cannot be assessed from documents; see §Narrative notes for the two **evidenced** limits (channel and money), which are record blind spots, not personal ones | — | UNKNOWN as to person |
| Credibility / reputation at the time | **One dated outside designation, and it is a substantive one:** BYTE's editor files him under "entrepeneurs" alongside the principals of Processor Technology, Technical Design Labs and the Byte Shops, in the December 1976 issue (B-31). Beyond that, he is a name in a clause and a man in a motel room. By Feb 1981 print calls him one of "the creators of the Apple computer" and reports an 8.3 million-share holding | A2-56, A2-60, B-02, B-31, A2-51 [inherited] | Medium-High as to 1976 standing; the 1981 layer is `RETROSPECTIVE SOURCE` |

### B.2 STEVE WOZNIAK as of 1975 → 1977-01-03

| Field | Value | Source | Confidence |
|---|---|---|---|
| Age in window | **UNKNOWN from in-window print.** BYTE Feb 1981 "Steve Wozniak, 30 years old" → DERIVED birth c. 1950, so **c. 25–26 at the 1976-04-01 partnership** (±1 yr) | A2-60 | Medium for the printed age |
| Education and completion status | **UNKNOWN at Tier 1** — no in-window document mentions schooling | — | UNKNOWN |
| Career and employers, with dates | **UNKNOWN at Tier 1, and there is a positive dated negative:** a grep of every cached 1975–77 file for `Hewlett`, `Packard`, `HP-65` returns only calculator and component advertising and review matter (e.g. BYTE April 1976 "the HP-65 retails for $795"); **no printed source in this corpus connects either founder to Hewlett-Packard.** The claim's best datable carriers found by this pass are retrospective (Business Insider, 2013-02-01; a museum item of similar vintage) | A2-57; B-38, B-43 | High (documented absence in family); Low on the HP employment claim itself |
| Technical capability, as evidenced by work products | **The best-evidenced founder attribute in this dossier, and it is first-party plus outside-confirmed.** (i) He designs and signs: "Stephen Wozniak / Apple Computer Co / 20863 Stevens Creek Blvd B3-C / Cupertino CA 95014", BYTE May 1977; (ii) he is described by BYTE's editor in April 1977 as "designer of the Apple-ll computer" (B-33); (iii) the same magazine's May 1977 text says **"Wozniak's Apple BASIC interpreter"**, indexes him as the article's author, and summarizes his piece as describing "the design of such a system" (B-34); (iv) the 1976-11-20 session record has him re-coding a game into 6502 assembly **after the fact, on his own initiative, and reporting the result to the editor** | A2-57, A2-32, B-33, B-34, A2-31 (verbatim in B-11/B-32) | High — four documents, but **all from two publishers, one of them his own company**; the independent element is Helmers' observation, not the advertising |
| Business/commercial capability | **Weakly evidenced.** He publishes technical copy under a company address and states a distribution model and a price band in the same article, which is a commercial act; no document shows him negotiating, invoicing or collecting. The mail-order apparatus that did exist (B-35) names no person | A2-25/A2-57, B-35 | Medium (as printed), Low as a capability claim |
| Design capability | **Documented by the artifact class itself**: the machine bears his design in the editor's words, and he is the only one of the four subjects who is *named as a designer* in any in-window print. He is also the only subject whom a third party is shown **operating** the machine (a club contributor's TV-monitor modification, B-41) | A2-32, B-33, B-41 | High |
| Prior ventures and prior failures | **UNKNOWN at Tier 1.** One dated in-window observation touches his prior means of work: the Sonoma County club letter says he personally transported an "APPLE 6502 system" — evidence of unpaid, self-mobile distribution of his own design, not of a venture | A2-19 / L-3 (`hcc0204.txt`:141) | Medium (single ~40-word letter) |
| Personal network as observable in dated documents | (i) **Sonoma County Micro Computer Club** — 1976-04-30, he drives a machine ~60 miles to a club outside his own county; (ii) **Carl Helmers/BYTE** — 1976-11-20, in-person, then a commissioned article; (iii) **Homebrew's population** — the June 1976 CPU census puts 18 of 101 live club systems on his chosen 6502, which is the market his network addressed; (iv) **Shepardson Microsystems** at 20823 Stevens Creek Blvd, three building numbers away, in BYTE April 1977; (v) **the Faire organising pair** — Jim Warren and Bob Reiling, named with titles and telephones in the club print that also lists "Apple Computers" as a committing exhibitor (B-40) | A2-19, A2-31, A2-61, A2-58, B-40 | Medium-High |
| Financial constraint / what he could put up | **UNKNOWN.** No in-window document states any amount, any asset sale, or any loan | E-13 | UNKNOWN at Tier 1 |
| Employment status in window | **UNKNOWN in this family — with a caution:** the absence of an employer mention is documented (A2-57 "it never mentions an employer"), but newsletters and magazine bylines are not personnel records; silence here is not proof of unemployment. No officer title attaches to him in any 1976–77 document either (B-37) | A2-57, B-37 | High (absence of mention) / UNKNOWN (status) |
| Location and living situation | Address of record 1977-05: Cupertino, 20863 Stevens Creek Blvd Bldg B3-C (his own byline). Presence documented at a Palo Alto motel 1976-11-20, and at a club in **Cotati, Sonoma County**, in April 1976 (a ~60-mile trip from his own county). Residence: UNKNOWN | A2-25, A2-31, B-29 | High for the byline address |
| Division of labour | **Asymmetric in the record, and the asymmetry is the finding:** the only documented labour split in 1976–77 print is *inside one man* — designer plus programmer (Wozniak) — plus a co-presence whose function is not stated (Jobs) | A2-59, B-32 | High |
| Documented blind spots | Two are evidenced by his own in-window text rather than inferred: his May 1977 account names **no customer, no order, no unit count and no price figure**, and its channel sequence ("word of mouth throughout California and later nationwide through retail computer stores") is contradicted in ordering by the dated dealer advertisements | E-11/E-12, L-10 | High (documented) |
| Credibility / reputation at the time | BYTE publishes him as a contributor, credits the design (April–May 1977), **attributes the BASIC interpreter to him in the possessive, and lists him in its author index** — an outside professional endorsement, the strongest standing record for any subject in this dossier. The hedge that comes with it is equally dated: the machine "may be the first product to fully qualify as the 'appliance computer'" (B-33) | A2-32, A2-57, B-33, B-34 | Medium-High |

### B.3 RON WAYNE as of 1975 → 1977-01-03

**Vintage warning printed at the top of the section (per the brief):** Wayne appears in **zero**
in-window documents. Every sentence below is either a claim about a document this project has not read,
or a 2018–2026 retrospective witness. Nothing in this section may be cited as a 1976 record.

| Field | Value | Source | Confidence |
|---|---|---|---|
| Age in window | **UNKNOWN.** No witness of any vintage in the cache states it | — | UNKNOWN |
| Education and completion status | **UNKNOWN** | — | UNKNOWN |
| Career and employers | **UNKNOWN at Tier 1.** A grep of the cached corpus for `Wayne` returns only third parties — "Fort Wayne", "Wayne State", Wayne Green, Wayne Sewell, "Wayne Av" (D's own recount matching A2's) | E-04, H-9 [inherited] | High (documented absence) |
| Capability (technical / business / design) | **UNKNOWN.** No work product of his is named in any retrieved document | — | UNKNOWN |
| Prior ventures and failures | **UNKNOWN** | — | UNKNOWN |
| Personal network | **No dated edge exists.** The relationship to Jobs and Wozniak is asserted only downstream of the unread partnership instrument | L-8 | UNKNOWN |
| Financial constraint / what he put up | **UNKNOWN.** The 45/45/10 allocation, the "$800 plus later $1,500" exit and the "12 days" duration are auction prose and retrospective participant speech; "12%" is contradicted by every line in the corpus that speaks to the stake | E-04, E-05, H-9, D-11 | Folklore; 10% best supported among stated figures, instrument unread |
| Employment status | **UNKNOWN** | — | UNKNOWN |
| Location | **UNKNOWN.** Not a single cached document places him anywhere | — | UNKNOWN |
| Division of labour | **UNKNOWN — and materially so:** he is a signatory in a documentary claim, and contributes nothing observable to any 1976–77 text | U-A2-10 | UNKNOWN |
| Documented blind spots | The record's, not his: a third partner is invisible to the entire trade press of his own company's founding year | A2-61a | High (as a record statement) |
| Credibility / reputation at the time | **No in-window witness.** His standing rests on a 2018 collector-registry sentence written from his own letter ("reduce the story about Ron Wayne to the point when he sold his **10%** Apple share", `apple1registry_stories.html`:488) — i.e. **42 years after the event, and self-sourced** | H-9 | Low, correctly vintage-labelled |

### B.4 MIKE MARKKULA as of 1975 → 1977-01-03

**Vintage warning:** his entire in-window footprint is **one sentence in one unsigned column, BYTE
February 1981**, `Markkula` occurring exactly once in ~13 MB of cached trade print (A2-61a, H-9). That
sentence is about 1976–77 only insofar as a 1981 writer chose to characterise it.

| Field | Value | Source | Confidence |
|---|---|---|---|
| Age in window | **UNKNOWN from in-window print.** 1981 print: "A C Markkula, 32 years old" → DERIVED birth c. 1948, so **c. 27–28 at the 1976-04-01 partnership**; ±1 yr band | A2-60, A2-51 | Medium for printed age |
| Education | **UNKNOWN** — not stated in the 1981 line or anywhere else in the cache | — | UNKNOWN |
| Career and employers | **UNKNOWN at Tier 1.** The cached corpus carries no employer for him | — | UNKNOWN |
| Capability evidenced by work products | **One gloss, dated 1981, retrospective:** he "took Apple from a garage operation to its current enviable position". This is an editorial characterisation of a transition the writer did not document; it is nonetheless the **strongest in-window support for the garage motif anywhere in the cache**, and it is five years late | E-06, L-5 (`byte-1981-02.txt`:48514–48519) | High that it was printed; Low as evidence of what he did |
| Prior ventures / failures | **UNKNOWN.** No prior-venture record of any vintage in the cache | — | UNKNOWN |
| Personal network | **One dated edge only, and it is a holding, not an introduction:** 8.3 million shares in Feb 1981 print, the same count as Jobs's and Wozniak's; Venrock's 3.8 million shares sit in the same column, which is the only printed evidence of venture capital in the cap table | A2-51, E-15, E-16 | High as printed / UNKNOWN as relationship |
| Financial constraint / what he put up | **UNKNOWN.** The ~$250,000, the $91,000 guarantee and the ~26% stake are post-1981 book retellings; 1981 print carries name, age, holding and role gloss only | E-15 | Folklore / UNKNOWN at Tier 1 |
| Employment status | **UNKNOWN** | — | UNKNOWN |
| Location | **UNKNOWN** | — | UNKNOWN |
| Division of labour | **UNKNOWN**; and note the asymmetry this creates: the money-side of the popular division of labour is the *least* documented of all four subjects | — | UNKNOWN |
| Documented blind spots | His entry is not dated in any retrieved record. No document in the corpus says when he arrived, and A2's DG-5 fixes his first print appearance at Feb 1981 | DG-5, D-9 | High |
| Credibility / reputation at the time | No in-window reputation record. By 1981 he is printed as the operator who moved the company | A2-51 | Low for Stage 1 |

---

## Findings

Records are `B-nn`. Format per §7 claim-record line. `[inherited]` marks claims taken from a sibling
dossier without re-verification; `re-verified by this pass` marks line-level local confirmation.

### Batch 1 — the corpus-side founder-state bedrock (local mining, 0 web requests)

B-01 Claim: **The periodical record of Apple's founding year knows the founders as names, not as
people** — across ~13 MB of cached 1976–1981 trade print and club newsletters (30 files), `Wozniak`
occurs in four files only (BYTE Apr 1977, May 1977, Feb 1981; Homebrew 1976-04-30), `Jobs` as a personal
name in three (BYTE Dec 1976, Apr 1977, Feb 1981), `Markkula` exactly once (BYTE Feb 1981), and `Wayne`
never in an Apple attribution — Date: 1975-03 → 1981-02 (documentation window) — Source: A2-61a name
census over `sources/ia_byte_1976/`, `ia_byte_1977/`, `ia_byte_1981/`, `ia_homebrew/` — Source date:
2026-09-24 — URL: local corpus — Archived: `sources/ia_*` — Tier: 1 — Class: FACT (documented extent) —
Passage: "Steven Jobs (Apple Computer Co)" / "Stephen Wozniak / Apple Computer Co" / "A C Markkula, 32
years old" — Conf: High — Corroboration: n/a (census, not a claim) — Conflicts: None. **This is the
calibration record for the whole dossier: five documents in total constitute the contemporary printed
knowledge of the four subjects, so any founder-state sentence that appears to come from 1976 is being
imported from elsewhere.**

B-02 Claim: **What the 1976 trade press knew of Steve Jobs was his name, his company's style and his
presence at a trade show — no age, employer, school, city or role** — Date: 1976-12 (publication) —
Source: BYTE December 1976 editorial, Carl Helmers — Source date: 1976-12 — URL:
`sources/ia_byte_1976/byte-1976-12.txt` [inherited from A2-15/A2-56] — Archived: as cited — Tier: 1 —
Class: FACT (documented extent of knowledge) — Passage: "Steven Jobs (Apple Computer Co)" — Conf: High —
Corroboration: 1 — Conflicts: **extended by B-31, which reads the sentence this clause is the tail of: the
editor's word for the four men in it is "entrepeneurs", so the clause does carry a class designation even
though it carries no function.** Positive identity evidence for Jobs in this family is therefore
**exactly two dated items**: this clause and Helmers' 1976-11-20 sighting (B-09). Everything else
commonly stated about his 1976 state has zero occurrences in these files (B-05, B-38).

B-03 Claim: **Wozniak's printed founder state in 1976–77 is technical, first-person and
address-bearing, and it never mentions an employer** — Date: 1976-04-30 → 1977-05 — Source: Homebrew
1976-04-30 letter (A2-19); BYTE April 1977 editor's description (A2-32); BYTE May 1977 byline (A2-25) —
Source date: 1976-04 … 1977-05 — URL: `sources/ia_homebrew/hcc0204.txt`, `sources/ia_byte_1977/
byte-1977-04.txt`, `byte-1977-05.txt` — Archived: as cited — Tier: 1 — Class: CONTEMPORARY OBSERVATION
(1976) + FOUNDER CLAIM (1977 byline) — Passage: "Stephen Wozniak / Apple Computer Co / 20863 Stevens
Creek Blvd B3-C / Cupertino CA 95014" — Conf: High — Corroboration: 3 documents, 2 publishers (BYTE,
Homebrew) — Conflicts: None. Note the class discipline: three documents, but two are company-side
(A2's independence rule, adopted at B-16).

B-04 Claim: **The only 1981 print carrying founder ages reports Jobs at 25, Wozniak at 30 and
Markkula at 32 — and those ages are five years stale as witnesses to the partnership** — Date: 1981-02
— Source: BYTE February 1981 unsigned column (A2-51, A2-60) — Source date: 1981-02 — URL:
`sources/ia_byte_1981/byte-1981-02.txt`:48509 (opening of the Jobs clause **re-verified by this pass**,
which returned the exact line "Steve Jobs, 25 years old,") — Archived: as cited — Tier: 1 — Class: FACT
(as printed) / `RETROSPECTIVE SOURCE` for 1976 — Passage: "Steve Jobs, 25 years old, and Steve Wozniak,
30 years old, the creators of the Apple computer… A C Markkula, 32 years old…" — Conf: High —
Corroboration: 1 — Conflicts: None. Arithmetic (DERIVED): Feb 1981 − 25 yr ⇒ birth c. 1955-02 ⇒ c. 21 at
1976-04; Feb 1981 − 30 yr ⇒ birth c. 1950-08 ⇒ c. 25.6 at 1976-04; integer ages give a ±1-year band.
**This is the closest the dossier comes to an age for any subject, and it is not an in-window record.**

B-05 Claim: **No cached in-window document connects either founder to Hewlett-Packard; the HP-65
appears only as a calculator on sale** — Date: 1975-03 → 1977-12 — Source: A2-57/A2-61c negative census;
comparator price at BYTE April 1976 — Source date: 2026-09-24 (census) — URL: local corpus — Archived:
`sources/ia_*` — Tier: 1 — Class: FACT (documented absence in these files) — Passage: "the HP-65 retails
for $795" — Conf: High within corpus — Corroboration: n/a — Conflicts: None. Consequence: **Wozniak's HP
employment, on which the entire capital-raising anecdote depends, is outside this evidence family
entirely.** Recorded as a family-scoped negative, not as a disproof (§14 rule 6).

B-06 Claim: **The two employment anecdotes that found every account of Apple's founders — Wozniak at HP
and Jobs at Atari — have no in-window witness anywhere in the corpus; the string `Atari` occurs in the
cached 1975–77 files only inside Apple's own advertisement, as a trademark notice for a game** — Date:
1977-06/07 (occurrence) — Source: A2-61c; **re-verified by this pass** in the newer intake layer BYTE
September 1977, where the same notice appears in the Apple II advertisement's closing lines — Source
date: 1977-09 (intake retrieved 2026-09-25) — URL: `00_universe/harvest/periodicals_intake/
apple_microcomputer_sector/BYTE_1977-09_EXTRACT_apple2_ad_and_editorial.txt` §B — Archived: item
`byte-magazine-1977-09`, layer `1977_09_BYTE_02-09_Music_and_Computers_djvu.txt` 860,344 B — Tier: 1 —
Class: FACT (documented absence, plus one dated occurrence of the trademark line) — Passage: "PONG is a
trademark of Atari Inc." — Conf: High within corpus — Corroboration: n/a — Conflicts: None. **Reading
carefully: this line is not evidence of Jobs's Atari employment. It is Apple, in its own copy,
disclaiming a game's trademark — the closest the founding-era record comes to Atari and the weakest
possible reading of it.**

B-07 Claim: **The founders' names are absent from the corpus at the moment the brand is most present in
it; in 1976 the hobby trade dealt in brands on dealer pages, not in persons** — Date: 1976-09 → 1976-12
— Source: A2-61b (negative name census cross-tabulated against the dealer advertisements) — Source date:
2026-09-24 — URL: local corpus — Archived: `sources/ia_byte_1976/`, `ia_homebrew/` — Tier: 1 — Class:
FACT (documented absence within these files) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High —
Corroboration: n/a — Conflicts: None. Mechanism named, per §7's coda rule: dealer advertising bought
brand association cheaply and did not require knowing who made the boards, so the personal layer of
Apple's story has **no periodical foundation before 1977**, and everything said about "Jobs in 1976" is
imported from later testimony.

B-08 Claim: **The famous 1976 role division between Jobs and Wozniak is absent from every 1976–77 text
on disk; neither the designer's article nor the company's own advertisement attributes any function to
Jobs** — Date: 1977-05 / 1977-06 — Source: A2-59, against A2-25 and A2-27 — Source date: 1977-05,
1977-06 — URL: `sources/ia_byte_1977/byte-1977-05.txt`, `byte-1977-06.txt` [inherited] — Archived: as
cited — Tier: 1 — Class: FACT (documented absence) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High
— Corroboration: n/a — Conflicts: None. This does not show the division did not exist; it shows the
division is **not a Stage-1 record** and must be labelled by the vintage of whatever carries it.

B-09 Claim: **The only contemporaneous, non-company witness placing both founders with the machine is
dated to a single evening and was published five months later** — Date: 1976-11-20 (event) / 1977-04
(publication) — Source: Carl Helmers, BYTE April 1977 (A2-31) — Source date: 1977-04 — URL:
`sources/ia_byte_1977/byte-1977-04.txt`:2704 (line verified by D's H-4; the column's Jobs sentence opens
at line 2744 of the same file, re-verified by this pass) — Archived: as cited — Tier: 1 — Class:
CONTEMPORARY OBSERVATION, single witness — Passage: "That evening last November, Steve Jobs, …" — Conf:
Medium-High — Corroboration: 1 — Conflicts: None. D's H-4 records the two real weaknesses (an editor
with a commercial interest; one witness) and still holds the fact: **a named third party, a date to the
day, both founders, one named place.**

B-10 Claim: **Wozniak's own May 1977 article names no customer, no order, no unit count and no price
figure, and describes distribution as word of mouth then retail stores — the strongest available
first-party in-window text, and it is silent on the keystone events of the standard story** — Date:
1977-05 — Source: Stephen Wozniak, "the Apple II"/article, BYTE May 1977 (A2-25; E-11/E-12/H-2/L-1) —
Source date: 1977-05 — URL: `sources/ia_byte_1977/byte-1977-05.txt` lines 6385, 6397, 6420 — Archived:
as cited — Tier: 1 — Class: FOUNDER CLAIM (contemporaneous) — Passage: "1975 and sold by word of mouth
through-" (wrapping to the retail-stores clause) and "processor board with a price under $700 at" —
Conf: High that it is what he printed; Medium that it is accurate as description — Corroboration: 1
lineage — Conflicts: U-A2-2 / E-08 (the Byte Shop order), L-10 (the channel sequence inverts against the
dated dealer advertisements).

B-11 Claim: **The division of labour observable in the 1976-11-20 record is designer-plus-programmer on
one side and an unexplained co-presence on the other: the two founders and the editor write and debug a
game on the prototype that evening, and Wozniak then re-codes it into 6502 assembly on his own
initiative** — Date: 1976-11-20 (event) / 1977-04 (publication) — Source: as B-09 — Source date: 1977-04
— URL: as B-09 — Archived: as B-09 — Tier: 1 — Class: CONTEMPORARY OBSERVATION — Passage: "Later, Steve
Wozniak recoded the program using the 6502 processor's assembly language facility as implemented in the
Apple-ll, and reports that the Color Eater now runs like lightning, which is its normal mode of
operation these days as a demonstration program for the Apple-ll." — Conf: Medium-High — Corroboration:
1 — Conflicts: None. Note that the passage is evidence of a *work product* (a demonstration program,
recoded and reported), which is the class §7 demands for capability claims.

B-12 Claim: **Apple's address of record sits inside a supplier cluster, three building numbers from
another Cupertino microcomputer firm, and the corporation's only published point of contact through
1977 is that suite — not a garage, a dormitory or a home** — Date: 1977-04/05/06 — Source: A2-58
(Shepardson Microsystems masthead in BYTE April 1977; Wozniak's byline; Apple's advertisement) — Source
date: 1977-04 … 1977-06 — URL: `sources/ia_byte_1977/` — Archived: as cited — Tier: 1 — Class: FACT (as
printed) — Passage: "Shepardson Microsystems Inc, 20823 Stevens Creek Blvd, Bldg C4-H, Cupertino CA
95014" — Conf: High — Corroboration: 2 independent documents naming the same complex in adjacent months
— Conflicts: U-A2-13 / D-4 / E-07 (the address of record does not displace the unsourced Los Altos
home; D's H-7 holds that a Cupertino business address in 1977 is fully compatible with unpaid work at a
family home in 1976). **Re-verified by this pass in the new intake month:** BYTE September 1977 carries
the same address as the advertisement's only contact block, "Apple Computer Inc., 20863 Stevens Creek
Boulevard, Bldg. B3-C, Cupertino, California 95014", with telephone "(408) 996-1010".

B-13 Claim: **The newer intake month confirms that by September 1977 Apple was buying a two-page
front-of-book advertisement under its own corporate name, in a magazine where it had placed nothing at
all in 1976** — Date: 1977-09 — Source: BYTE September 1977 full-page advertisement plus the issue's own
advertiser/reader-service index — Source date: 1977-09 — URL: intake extract §B (text-layer offset
~50,193–54,500) and §C (offset ~847,242) — Archived: `byte-magazine-1977-09` — Tier: 1 — Class: FACT (as
printed; OCR partial) — Passage: "208 Apple 14, 15" (index line: reader-service number 208, printed
pages 14 and 15) — Conf: High on the index entry and the copy; Medium on numerals inside the spec table
(the extract's own OCR note: "Apple 11 / Apple n / Apple Ilf" for "Apple II") — Corroboration: **same
lineage as B-12/A2-27 — one advertiser, a later issue** (this is corroboration of *duration*, not of
independence; per A2's campaign rule and §3, counted as one company-side interest) — Conflicts: None.
Additional founder-state value: the advertisement's closing trademark notice is the Atari string of
B-06, and the copy's price pair ($1298 system / $598 board-only) repeats the June 1977 terms, which
extends the company's own printed pricing ladder by three months.

B-14 Claim: **The company's own 1977 advertising speaks to a national dealer network by telephone
referral, and the same pages show East-Coast general-line retailers stocking Apple as a brand among
twenty-odd lines — the distribution story is a dealer story, and no founder is attached to it in any
document** — Date: 1977-09 / 1977-11 — Source: BYTE September 1977 advertisement ("Or call us for the
name and address of the Apple n dealer nearest you"); Creative Computing Nov/Dec 1977 dealer
advertisements — Source date: 1977-11/12 — URL: intake extracts
`BYTE_1977-09_EXTRACT…txt` §B; `CREATIVECOMPUTING_1977-11_EXTRACT_apple_mentions.txt` offsets 598460,
621794 — Archived: `CreativeComputing_v03n06_NovDec1977` — Tier: 1 — Class: CONTEMPORARY OBSERVATION
(third-party advertisements) — Passage: "Imsai, Processor Technology, Polymorphic, Cromenco, Apple and
more" (The Computer Mart, 118 Madison Ave, New York 10016 — OCR 'Cromenco' for Cromemco) — Conf: Medium
— Corroboration: **one lineage with A2's Computer Mart of New York ladder (A2-08/A2-11) — the same
retailer group's campaign, not a second retailer**; the "IT'S ALL HERE WAITING… New York City 118
Madison Ave" verse advertisement is the same address family — Conflicts: None. The intake's own caution
is carried: no Apple review appears in the Creative Computing issue; Apple is a brand in dealer copy and
a machine in a reader's catalogue.

B-15 Claim: **BYTE's founding issue, September 1975 — eight months before the corporation's filing date
and the earliest issue of the title that would become Apple's best witness — contains zero occurrences
of "Apple"** — Date: 1975-09 — Source: intake content test on `byte-magazine-1975-09` (Vol 00 No 01 "The
Worlds Greatest Toy"), 63,757 words — Source date: 1975-09 — URL: intake
`SEARCH_LOG.md` §A; extract §D — Archived: `byte-magazine-1975-09`, layer 443,605 B — Tier: 1 — Class:
FACT (documented absence, one issue) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High —
Corroboration: n/a — Conflicts: None. **Scope discipline: this is one issue of a new year, not a null on
1975; BYTE 1975-10/-11/-12 remain UNTRIED (intake §D.1). The Stage-1 opening edge of 1975 is therefore
not evidenced by BYTE at all, and rests on Wozniak's single May 1977 clause (B-10).**

B-16 Claim: **Independence accounting for the company-side founder-state record: Wozniak's article, the
June 1977 advertisement and the September 1977 advertisement are three documents under one interest, so
the entire first-party in-window founder-state corpus reduces to one company and one editor** — Date:
1977-04 → 1977-09 — Source: A2's independence rule, extended by this pass to the intake month — Source
date: 2026-09-25 — URL: as B-03, B-10, B-12, B-13 — Archived: as cited — Tier: n/a — Class: INFERENCE
(methodological, from the provenance of the documents themselves) — Passage: NO_VERBATIM_PASSAGE_RECORDED
— Conf: High — Corroboration: n/a — Conflicts: None. Consequence for the merge: any stage-file sentence
that reads "corroborated in Wozniak's article and Apple's advertisement" is a **lineage error of the same
kind as §3's filing-lineage rule**, and the intake log's own framing of the September ad as
"corroboration of the same terms in a later issue, not a new claim" is the correct handling.

### Batch 2 — the Wayne/Markkula vintage problem and the unread instrument

B-17 Claim: **The origin story as printed from the start was a two-founder story; the third partner is
invisible to every in-window document** — Date: 1976-04 → 1981-02 — Source: D's E-04 grading, resting on
this project's own `Wayne` grep of all cached files — Source date: 2026-09-24 — URL:
`research/D_adversarial.md` E-04, H-9; grep log §Provenance — Archived: `sources/ia_*` — Tier: 1 (the
negative) / 3 (the attribution) — Class: FACT (documented absence in this family) — Passage: "Wayne"
hits resolve only to "Fort Wayne", "Wayne State", Wayne Green, Wayne Sewell, "Wayne Av" — Conf: High —
Corroboration: n/a — Conflicts: U-A2-10 (the 1976-04-01 agreement is a three-signatory instrument, per
auction prose). **Reading: the contradiction is not between two records of Wayne; it is between one
unread instrument and a printed record that never saw him.**

B-18 Claim: **Apple's founding date, its capital structure and its third partner all rest on a single
1976 paper that this project has not read** — Date: 1976-04-01 (claimed document date) — Source: Christie's
lot description, reached only through secondary reports; the project's own fetch failed — Source date:
2026 (sale-campaign prose) / 2026-09-24 (attempt) — URL: `christies.com/en/lot/lot-the-apple-computer-
company-partnership-agreement-6570347/` — Archived: **UNANSWERED — `fetch failed`** (D's W9; artnet HTTP
403 per the retrieval log) — Tier: 2/3 (secondary reports of a Tier-1 artifact) — Class: RETROSPECTIVE
/ CONTESTED — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: Low — Corroboration: 0 independent —
Conflicts: E-01, E-04, L-8, D-11. Merge decision inherited from D: **no sentence may assert the
45/45/10 split, the signing place, or Wayne's exit terms as document text**; the honest form is
"reported as 45/45/10 in auction and registry coverage of the document (Tier 2/3); the document unread".

B-19 Claim: **Wayne's stake is better supported at 10% than at the circulated 12%, and both readings
predate any document this project can read** — Date: 2018 (registry prose from Wayne's own letter) /
2025–26 (auction coverage) — Source: `sources/apple1registry_stories.html`:488; auction coverage
[inherited from H-9, D-11] — Source date: 2018 / 2026 — URL: as cited — Archived: `sources/` — Tier: 3 —
Class: RETROSPECTIVE INTERPRETATION (self-sourced via Wayne's own later letter) — Passage: "reduce the
story about Ron Wayne to the point when he sold his 10% Apple share" — Conf: Low-Medium — Corroboration:
2 carriers, but the 2018 registry prose and the 2026 auction prose are not shown to be independent of
each other or of the instrument — Conflicts: D-11. "12%" is barred.

B-20 Claim: **Wayne's departure — twelve days, $800, later $1,500, "no regrets" — has no dated
withdrawal instrument in evidence and no in-window witness of any kind** — Date: 1976 (claimed) —
Source: auction press plus Wayne's own later writings [inherited E-05] — Source date: 2025–26 / 2018 —
URL: `research/D_adversarial.md` E-05, §Unsourced — Archived: — — Tier: 2/3 — Class: FOLKLORE
(retrospective participant speech + commercial description) — Passage: NO_VERBATIM_PASSAGE_RECORDED —
Conf: Low — Corroboration: 0 independent — Conflicts: None in-window; U-A2-10 covers the three-partner
shape. **What survives founder-discard test, per D: that a withdrawal happened (an artifact class
exists). Duration, amounts and attitude are undocumented in this corpus.**

B-21 Claim: **Markkula's entire contemporaneous footprint is a name, an age, a share count and a
one-line role gloss in an unsigned February 1981 column; every figure for his deal is post-1981
retelling** — Date: 1981-02 (witness) about 1976–77 — Source: BYTE February 1981 (A2-51; E-15) — Source
date: 1981-02 — URL: `sources/ia_byte_1981/byte-1981-02.txt`:48514–48519 — Archived: as cited — Tier: 1
(contemporaneous to 1981) / `RETROSPECTIVE SOURCE` for Stage 1 — Class: CONTEMPORARY OBSERVATION of
1981; RETROSPECTIVE INTERPRETATION of 1976 — Passage: "A C Markkula, 32 years old, who took Apple from a
garage operation to its current enviable position, also holds 8.3 million shares" — Conf: High as
printed — Corroboration: 1 (the column is one lineage; U-A2-7) — Conflicts: E-15's figures ($91,000
guarantee / ~$250,000 / ~26%) are UNKNOWN at Tier 1 and must not be printed beside this sentence as if
they were of the same class.

B-22 Claim: **"Started in a garage" was a stock phrase of the field's own press before Apple's garage
could have entered anyone's memory — in July 1976 BYTE printed a reader's account of a different firm as
"all the company consisted of was two people in a garage"** — Date: 1976-07 — Source: letter/article on
Sphere, BYTE July 1976 (`byte-1976-07.txt`:3023–3027), via D's L-5 — Source date: 1976-07 — URL: as cited
— Archived: `sources/ia_byte_1976/byte-1976-07.txt` — Tier: 1 — Class: CONTEMPORARY OBSERVATION (about
another company) — Passage: "all the company consisted of was two people in a garage" — Conf: Medium-High
— Corroboration: 1 — Conflicts: None; this bears on E-06/E-07, not on them contradicting. **Method
value: it lowers the evidentiary weight of the garage motif in general and raises the value of a property
record, which is the only thing that can settle a garage at all (DG-D5).** Provenance caveat: the same
file carries D's L-6 issue-dating anomaly, so this citation travels with
`issue-date: provisional pending page-sequence verification`.

B-23 Claim: **The capital story that anchors Jobs's founder state in every popular account — $500 from
an HP-65 and $750 from a VW bus — traces to one 2006 autobiography, and the corpus's independent
comparator for one of its numbers is an unrelated calculator price** — Date: 1976 (claimed) / 2006
(carrier) — Source: *iWoz* (2006) ch. 12 p. 173, via the collector registry [inherited E-13, AP-32];
comparator "the HP-65 retails for $795", BYTE April 1976 — Source date: 2006 / 1976-04 — URL:
`sources/apple1registry_stories.txt`; `sources/ia_byte_1976/` — Archived: as cited — Tier: 3 (memoir) /
1 (comparator) — Class: FOUNDER CLAIM (retrospective memory) — Passage: NO_VERBATIM_PASSAGE_RECORDED —
Conf: Low — Corroboration: **0 independent — repetition across the web is one lineage** (§3) —
Conflicts: E-14 (a partner's retrospective belief in a $15,000 loan, in tension with the $1,000 total).
Nothing about the story is refuted; it has no evidential standing.

B-24 Claim: **No retrieved document of any vintage states when Markkula joined, or when Venrock
invested; the money side of the Stage-1 division of labour is therefore not merely undocumented but
undated** — Date: 1976–1977 (the hole) — Source: A2's DG-5; E-16 (only the 3.8M-share line) — Source
date: 1981-02 (earliest print) — URL: `sources/ia_byte_1981/byte-1981-02.txt`:48494–48525 — Archived: as
cited — Tier: 1 — Class: FACT (documented absence) / UNKNOWN (the events) — Passage: "Venrock Associates,
a venture capital firm, holds 3.8 million shares" — Conf: High as printed — Corroboration: 1 —
Conflicts: D-9 (A2's DG-5 and AP-18 quote the same line; neither flags that "garage operation" is doing
identity work about 1976 inside a 1981 text).

B-25 Claim: **The 1981 column's own share arithmetic checks out, which is a modest signal that its
founder-state sentences were drawn from real numbers rather than memory** — Date: 1981-02 — Source: E-15,
H-8 [inherited] — Source date: 1981-02 — URL: `sources/ia_byte_1981/byte-1981-02.txt`:48494–48525 —
Archived: as cited — Tier: 1 — Class: DERIVED — Passage: "they own well over $100 million worth of
stock" — Conf: Medium-High — Corroboration: 1 — Conflicts: U-A2-9 (the offering arithmetic in the same
column does **not** close). Arithmetic (DERIVED): 8.3M shares × $22 = **$182.6M** per founder, consistent
with "well over $100 million", while 0.08 × 52.4M = 4.192M ≠ the printed 4.6M shares and
4.6/52.4 = 8.78% ≠ 8%. Mixed reliability inside one document; both figures printed, neither preferred.

B-26 Claim: **The corporation's founding is the one founder-adjacent fact with two lineage-free Tier-1
witnesses, and it names no founder at all** — Date: 1977-01-03 — Source: FY1994 Form 10-K recital
(AP-04) and BYTE February 1981 (AP-19) — Source date: 1994-12-13 / 1981-02 — URL:
`sources/10-K_FY1994_acc-0000320193-94-000016_filed-1994-12-13.txt`:132–135 — Archived: EDGAR — Tier: 1 —
Class: FACT — Passage: "was incorporated under the laws of the State of California on January 3, 1977"
(wrapping at ~76 columns; **must be cited by line range, not by one-line equality** — L-7.1) — Conf: High
— Corroboration: 2 independent origins — Conflicts: D-7 (the 1981 witness gives the **year** only; the
day-and-month rests on the filing alone), E-03 (the fused "founded April 1, 1976" formulation is a
category error).

B-27 Claim: **The company's own legal style in the founding print is unstable across four authentic
forms, and no 1976–77 document names the partnership style — so the sentence "Apple Computer Company was
founded by three men" has no printed referent in the period** — Date: 1976-09 → 1980-12 — Source: U-A2-1,
E-36 [inherited] — Source date: 1976-09 … 1980-12 — URL: `sources/ia_homebrew/`,
`sources/ia_byte_1976/`, `sources/ia_byte_1977/`, `sources/ia_byte_1981/` — Archived: as cited — Tier: 1
— Class: FACT (as printed) — Passage: "Apple Computer Co" (BYTE Dec 1976 and Wozniak's May 1977 byline),
"Apple Computers" (Homebrew Sept 1976), "Apple Computer Inc." (Apple's own June 1977 advertisement),
"the Apple Corporation" (a third-party December 1980 advertisement) — Conf: High on the print facts,
Medium on any inference from them — Corroboration: 4 documents, 4 publishers — Conflicts: U-A2-1. **Note
the new-intake contribution: BYTE September 1977 adds a fifth dated occurrence of the corporation form,
"Apple Computer Inc.", from the company's own advertisement (B-13).**

B-28 Claim: **The social world the founders moved in is quantified by an organiser's own survey, and it
is the closest the corpus comes to documenting their market network: 101 live systems at the June 1976
Homebrew meeting, of which 18 on the 6502, against 38 systems at the October 1975 meeting** — Date:
1976-06-09 (event) — Source: Robert Reiling, "Random Data", Homebrew newsletter Vol 2 No 6 (A2-61) —
Source date: 1976-06-09 — URL: https://archive.org/details/hcc0206 — Archived:
`sources/ia_homebrew/hcc0206.txt` — Tier: 1 — Class: CONTEMPORARY OBSERVATION (self-report, no
independent count) — Passage: "A survey of hobbyists attending the June 9th meeting reveals the
following distributions of CPUs in use: 8080-53, 6502-18, 8008-6, PDP-8-4, LSI-11-3, Z80-2, 4004-1, PDP1
1/20-1 and TTL-1. That totals 101 systems up and running out the the group." [sic] — Conf: Medium-High —
Corroboration: 1 — Conflicts: None. Arithmetic (DERIVED): 6502 share 18/101 = **17.8%**, second only to
the 8080's 52.5%; systems per meeting grow 101/38 = **2.66×** and attendance 250/80 = **3.13×** in about
eight months. This is Wozniak's network as a countable population, and it is his processor's position in
it — a capability-adjacent fact, not a reputation claim.

B-29 Claim: **The one dated record of the machine reaching an audience outside the founders' own county
is a Sonoma County club letter, not a Homebrew record, and its gratitude names Wozniak as the
transport** — Date: 1976-04 (event) / 1976-04-30 (document) — Source: "Notes from the North", Sonoma
County Micro Computer Club letter reprinted in Homebrew newsletter (A2-19; corrected by D's L-3) —
Source date: 1976-04-30 — URL: `sources/ia_homebrew/hcc0204.txt`:131–144 (the sentence at line 141) —
Archived: as cited — Tier: 1 — Class: CONTEMPORARY OBSERVATION — Passage: "In April the APPLE 6502 system
was our special guest. We are grateful to STEVE WOZNIAK for providing transportation." — Conf: Medium —
Corroboration: 1 — Conflicts: L-3 (A's AP-24 headline reading, which treated it as Homebrew's own
meeting record, must be retired), and the same paragraph's "on order" ambiguity may make this a booking
rather than a delivery. Founder-state value: **it is the only in-window document showing a founder
personally moving his own design to an audience**, which is a work product of distribution rather than a
reputation.

B-30 Claim: **Jobs's only first-party-looking artifact in the founding-era corpus is a undated-to-1973
handwritten job application whose date is a curator's inference, and whose "a year later, he joined
Atari" gloss is curation prose rather than payroll** — Date: c. 1973 (curator's estimate) — Source:
collector registry / auction curation (E-30, AP-28) [inherited] — Source date: 2018–2022 — URL:
`sources/apple1registry_stories.txt` — Archived: as cited — Tier: 3 — Class: RETROSPECTIVE /
CONTEMPORARY OBSERVATION of an artifact, **not** of the event — Passage: NO_VERBATIM_PASSAGE_RECORDED;
the artifact's own text reportedly mentions "computers and calculators" — Conf: Low — Corroboration: 1 —
Conflicts: None. What would settle the field: a dated employer personnel record, a pay stub, or a
1973–75 periodical mention of the applicant.

### Batch 3 — new records from this pass's own line-level mining (local corpus + newer intake, 0 web requests)

B-31 Claim: **The one 1976 document that names Jobs does assign him a class, and it is a class of
operator: BYTE's editor lists him as one of four "entrepeneurs" he talked with on the WESCON floor in
September 1976, alongside the principals of Processor Technology, Technical Design Labs and the Byte
Shops** — Date: 1976-09 (event) / 1976-12 (publication) — Source: Carl Helmers, BYTE December 1976
editorial — Source date: 1976-12 — URL: `sources/ia_byte_1976/byte-1976-12.txt`:1513–1519 — Archived:
`ia_byte_1976/byte-1976-12.txt` — Tier: 1 — Class: CONTEMPORARY OBSERVATION — Passage: "Elements of this
attitude of achievement were present in my conversations with entrepeneurs Bob Marsh (Processor
Technology), Chris Rutkowsky (Technical Design Labs), Steven Jobs (Apple Computer Co) and Paul Terrell
(Byte Shops) on the floor of the WESCON show last September in Los Angeles CA." — Conf: High —
Corroboration: 1 (single author; the same author's April 1977 sighting is a second document by the same
witness, so it corroborates duration, not independence) — Conflicts: refines A2-56 and this file's B-02.
**This is the dossier's best dated network record and it changes two fields: Jobs's reputation-at-the-time
(an outside editor, in the year itself, files him under the same heading as three named industry peers)
and his documented location (a Los Angeles trade floor, September 1976). Read narrowly: "entrepeneurs" is
a category, not a function — the sentence attributes no act to him beyond the conversation, and Helmers
does not say what was said.** The word is also the **only** occurrence of `WESCON` anywhere in the cached
1976 corpus (this pass's grep: one hit, this line), so the event cannot be cross-checked inside the cache.

B-32 Claim: **The single document that places Jobs's hands on a keyboard is Helmers' account of the
1976-11-20 session, and it puts him inside a first-person-plural programming act — while the assembly
re-code, the design and the article are all assigned to Wozniak alone** — Date: 1976-11-20 (event) /
1977-04 (publication) — Source: "A Nybble on the Apple", Notes by Carl Helmers, BYTE April 1977 — Source
date: 1977-04 — URL: `sources/ia_byte_1977/byte-1977-04.txt`:2744–2761 — Archived: as cited — Tier: 1 —
Class: CONTEMPORARY OBSERVATION (single witness, commercially interested) — Passage: "That evening last
November, Steve Jobs, Steve Wozniak and I sat down and proceeded to use the Apple-ll BASIC (which is a 5 K
interpreter with 16 bit integer arithmetic) to program the Color Eater game. After perhaps 30 to 45
minutes, we had a working BASIC language version which used the Apple-ll's graphics facilities." — Conf:
Medium-High that the session happened as described; Low for any inference drawn from it — Corroboration:
1 — Conflicts: B-08 / A2-59. **The precise reading matters in both directions. Same paragraph set: Helmers
proposes the algorithm, all three sit down, "we" reach a working BASIC version, and "Later, Steve Wozniak
recoded the program using the 6502 processor's assembly language facility". The design credit goes to
Wozniak alone (B-33), and the promised article is "by Steve Wozniac, designer of the Apple-U [II]
computer" (line 2688). So this document bars the strong claim that Jobs wrote the machine's software; it
also bars the opposite claim that no technical act of his was ever witnessed. Anything beyond that is
UNKNOWN, and Helmers was an editor with a magazine to sell (D's H-4 records the same interest).**

B-33 Claim: **Wozniak's design credit is printed twice by BYTE's editor, once with a hedge that is the
honest limit of contemporary opinion: the Apple II "may be the first product to fully qualify as the
'appliance computer'"** — Date: 1977-04 — Source: as B-32 — Source date: 1977-04 — URL:
`sources/ia_byte_1977/byte-1977-04.txt`:2687–2698 — Archived: as cited — Tier: 1 — Class: CONTEMPORARY
OBSERVATION — Passage: "Next month, we'll have an article by Steve Wozniac, designer of the Apple-U
computer… The Apple-ll, which is to be introduced in April at the first West Coast Computer Faire in San
Francisco, may be the first product to fully qualify as the 'appliance computer.'" — Conf: High (as
printed) — Corroboration: 2 documents from one publisher (April and May 1977) — Conflicts: E-21 (the
"first in category" claim was already contested in-window by competing assembled 6502/8080 systems). Note
two things this record fixes that later testimony cannot: the **design credit attaches to Wozniak by name
in the same magazine that printed the company's advertising**, and the editor's own primacy claim is
**conditional**. The OCR form `Apple-U` for `Apple-II` in the credit line is why A2's census had to count
`Wozniac` as well as `Wozniak`.

B-34 Claim: **By May 1977 an independent technical publication was attributing the machine's BASIC
interpreter to Wozniak in the possessive, and indexing him as an author — the strongest
credibility-at-the-time record any subject of this dossier has** — Date: 1977-05 — Source: BYTE May 1977
editorial abstract (`byte-1977-05.txt`:763), author index (`:53956`), technical text (`:7662`), contents
listing (`:447`) — Source date: 1977-05 — URL: `sources/ia_byte_1977/byte-1977-05.txt` — Archived: as
cited — Tier: 1 — Class: CONTEMPORARY OBSERVATION — Passage: "What does it take to make a computer system
complete to the point of plugging it into the wall, plugging it into a color television, and turning it
on? Stephen Wozniak of Apple Computer describes the design of such a system in his product description
article on the Apple-! I [II]." / "Wozniak's Apple BASIC interpreter is a method of running the
interpreter with a statement number trace" / index line "3 Wozniak: The Apple-ll" — Conf: High —
Corroboration: multiple pages of **one issue of one magazine** — same publisher as B-33, so this is one
editorial interest across two months, counted as duration (per §Working method) — Conflicts: None. **For
the §7 field "credibility/reputation at the time", this is the answer for Wozniak and there is no
equivalent for anybody else: not for Jobs, not for Wayne, not for Markkula.**

B-35 Claim: **Apple's own 1977 advertisement is a direct-mail order form, which is a business work
product and is also the record's answer to the dealer question: through the summer of 1977 the maker sold
end users directly, by post, taking credit cards** — Date: 1977-06 (and repeated 1977-07, 1977-09) —
Source: "Introducing Apple II", Apple Computer Inc. advertisement, BYTE June 1977 — Source date: 1977-06
— URL: `sources/ia_byte_1977/byte-1977-06.txt`:2012–2013, 2286–2288, 2405–2459 — Archived: as cited —
Tier: 1 — Class: FACT (as printed) — Passage: "Order your Apple II now… we will include free a custom
vinyl carrying case (a $50 value). And we will also pay shipping charges to anywhere in the continental
United States." / "□ Cashier's check or money order enclosed. (Please allow 2 additional weeks for
personal checks.) Please charge to my □ BankAmericard □ VISA □ Master Charge" / "Mail to: Apple Computer
Inc., 20863 Stevens Creek Blvd., B3-C, Cupertino, California 95014" — Conf: High — Corroboration: same
lineage as B-12/B-13 (one advertiser, three months) — Conflicts: none in this file; **supports L-4's
finding** that no authorized-dealer relationship is evidenced for 1976, since the only sales mechanism the
company itself printed in 1977 is direct order plus telephone referral to a dealer. Founder-state reading,
with mechanism named: a nine-line price ladder, a separate shipping-address field, a named card set and a
held-check period are the artifacts of somebody running a **cash-flow-constrained mail-order operation** —
personal cheques are two weeks slow, freight is paid by the seller, and the inducement is a $50 case. What
it does **not** show is which of the four subjects did it: no person is named anywhere in the copy.

B-36 Claim: **The same order form recurs in July 1977 with the identical ladder and terms, extending the
company's direct-sale mechanism by one month and adding chip-level upgrade pricing** — Date: 1977-07 —
Source: Apple Computer Inc. advertisement, BYTE July 1977 — Source date: 1977-07 — URL:
`sources/ia_byte_1977/byte-1977-07.txt`:3960–4130 — Archived: as cited — Tier: 1 — Class: FACT (as
printed) — Passage: "Memory is offered at a 20% savings when ordered with the system-or board-as reflected
in the prices above… One set 4K chips (4K bytes) $125 / One set 16K chips (16K bytes) $600" and the
address block "20863 Stevens Creek Blvd., B3-C / Cupertino, California 95014 / (408) 996-1010" — Conf:
High — Corroboration: **one campaign, one advertiser** — Conflicts: None. Arithmetic check on the tax row,
supporting U-A2-6: `38.87 / 598.00 = 6.50%` and `84.37 / 1,298.00 = 6.50%` — the add-on column is
internally consistent at 6.5% across both the system and board-only rows (ESTIMATE/DERIVED basis shown).

B-37 Claim: **No document in the cached 1976–77 corpus assigns an officer title to any Apple person: a
grep for `president`, `vice-president` and `treasurer` restricted to Apple/Jobs/Wozniak context returns
zero hits, so the familiar "Jobs was president of Apple in 1976" is undocumented in this evidence
family** — Date: 1975-11 → 1977-12 — Source: negative grep over `sources/ia_byte_1976/`, `ia_byte_1977/`,
`ia_homebrew/` — Source date: 2026-09-26 (this pass) — URL: local corpus — Archived: as cited — Tier: 1 —
Class: FACT (documented absence in these files) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High
within corpus — Corroboration: n/a — Conflicts: None. What would evidence the field: the corporation's
Articles of Incorporation and first Statements of Information (California Secretary of State), the
initial stock ledger, or the partnership instrument's officer clauses (B-18/B-44).

B-38 Claim: **Three founder-state claims that every account treats as fact are confirmed by this pass to
have no personal-name referent anywhere in the cached corpus: Atari, Hewlett-Packard, and college
attendance** — Date: 1971 → 1977-12 — Source: negative censuses re-run by this pass — Source date:
2026-09-26 — URL: local corpus — Archived: `sources/ia_*` — Tier: 1 — Class: FACT (documented absence
within these files) — Passage: `Atari` resolves only to "PONG is a trademark of Atari Inc." inside Apple's
own advertisements (`byte-1977-06.txt`:2114, `byte-1977-07.txt`:3975) and to unrelated third-party "ATARI
GAME BOARDS" coin-op advertising (`byte-1977-04.txt`:43598, `-05`:48819, `-06`:38272, `-07`:33780);
`Hewlett`/`Packard` resolve only to component, calculator and press matter (e.g. `byte-1976-02.txt`:7393
"Hewlett Packard 5082-4487 LED", `byte-1976-04.txt`:6531 on the HP-65); `Reed College`, `dropout` and
`dropped out` return no Apple-person context at all (the `dropout` hits are tape-error prose) — Conf: High
within corpus — Corroboration: n/a — Conflicts: A2-61c, which this pass's count extends rather than
contradicts (A2 recorded the June/July trademark occurrences; this pass adds the four coin-op advertising
occurrences, all third-party). **Method point, per §14 rule 6: these are family-scoped negatives. They
show that periodical print cannot carry these three fields, not that the fields are empty.**

B-39 Claim: **The founding-era address reappears in December 1980 print as the contact for an "Apple
Education Foundation", with a different telephone — the only 1980 reference to the Stevens Creek suite in
the cache, and a dated marker of institutional continuity at the company's first published address** —
Date: 1980-12 — Source: BYTE December 1980, "What's New" style items column — Source date: 1980-12 — URL:
`sources/ia_byte_1981/byte-1980-12.txt`:81631–81637 — Archived: as cited — Tier: 1 — Class: FACT (as
printed) — Passage: "the grants are Apple II microcomputers. Other contributing organizations are Bell &
Howell, Mountain Computer Inc, Heuristics Inc, Integral Data Systems Inc, Interactive Structures Inc, ABW
Inc, and Videx. For more information, contact Apple Education Foundation, 20863 Stevens Creek Blvd,
Cupertino CA 95014, (408) 255-3295." — Conf: High — Corroboration: 1 — Conflicts: none; bears on A2-58.
Founder-state value is limited but real: it shows the same suite functioning two years later as the public
contact of a named Apple-linked foundation, and it lists the peer firms whose donations sat alongside
Apple's — the commercial circle the company had entered by 1980, which is the far edge of this stage and
must not be read backwards into 1976.

B-40 Claim: **The intermediaries who ran the club-and-faire circuit the founders passed through are
themselves documented with names, titles and telephone numbers in the club's own newsletter, even though
no introduction to a founder is ever recorded** — Date: 1976-09 (Homebrew Vol 2 No 9) — Source: Homebrew
Computer Club newsletter — Source date: 1976-09 — URL: `sources/ia_homebrew/hcc0209.txt`:225–262 —
Archived: as cited — Tier: 1 — Class: CONTEMPORARY OBSERVATION — Passage: "There are two people primarily
responsible for coordinating the organization of the Computer Faire: Jim Warren, General Chairperson
(Editor, Dr. Dobb's Journal & Vice-Chairman, Penninsula ACM Chapter), People's Computer Company, P.O. Box
310, Menlo Park, CA 94025 … —and— Bob Reiling, Operations Manager (Editor, Homebrew Computer Club
Newsletter), 193 Thompson Square, Mountain View, CA 94043" — Conf: High — Corroboration: the same issue's
exhibitor list names "Apple Computers" among "Zilog, National Semiconductor, … Processor Technology,
Cromemco, OSI" (line 234) — Conflicts: none. The Faire flyer in the same cache (`hcccf.txt`) fixes the
event itself: "april 15-17, 1977", "7,000 to 10,000 People / 100 Conference Sessions / 200 Commercial &
Homebrew Exhibits", chaired by "Jim Warren, Faire Chairperson, The Computer Faire, Box 1579, Palo Alto CA
94302, (415) 851-7664". **Why this belongs in a founder dossier: the two nodes through which the
Stage-1 public record of Apple's founders actually reaches us — BYTE's editor and the Faire/Homebrew
organisers — are dated, named and contactable in the corpus, whereas the founders' own relationships are
not. The network map is better documented one step outside the company than inside it.**

B-41 Claim: **The Apple-1 was in third parties' hands early enough that a club newsletter's technical
contributor used one to demonstrate a television-as-monitor modification, without naming anyone** — Date:
1976-09 — Source: Homebrew Vol 2 No 9, reader's technical article — Source date: 1976-09 — URL:
`sources/ia_homebrew/hcc0209.txt`:747–750 — Archived: as cited — Tier: 1 — Class: CONTEMPORARY
OBSERVATION — Passage: "I used Sony's TV 920 and TV750 for this modification to produce printout from the
Apple Computer." — Conf: Medium — Corroboration: independent of the company (a reader's own build note) —
Conflicts: none. Bearing on founder state: it is the earliest in-window evidence in this corpus of a
**stranger operating the machine**, which is the validation signal the designers' credibility rested on;
it says nothing about who sold it to him.

### Batch 4 — the web pass: what it bought, and what it did not (10 of 10 requests spent)

B-42 Claim: **The Jobs-at-Atari claim's best datable carrier found by this pass is a 2011 trade-press
article, "Steve Jobs, Atari Employee Number 40" — so the specificity of the payroll story (an employee
number) has a 2011 printed existence, roughly 35 years after the event, not a 1974–76 one** — Date: 1974
claimed (event) / 2011-10-06 (carrier) — Source: Game Developer (gamedeveloper.com), business column —
Source date: 2011-10-06 — URL: https://www.gamedeveloper.com/business/steve-jobs-atari-employee-number-40
— Archived: **UNANSWERED — WebFetch returned the page shell only; "the full article body is absent,
containing only JSON-LD schema, minified scripts, and site navigation". Only the headline and the
publication timestamp were recoverable.** — Tier: 2 (if the body is reached) / 4 as recovered — Class:
FOUNDER CLAIM (retrospective memory) at best; **unknown evidentiary basis** — Passage: "Steve Jobs, Atari
Employee Number 40" (headline) — Conf: Low — Corroboration: 0 documentary — Conflicts: E-34 (D bars Atari
tenure at Tier 1). A second carrier surfaced in the same search is a 2020 Q&A thread on whether the number
40 is right at all (retrocomputing.stackexchange.com, **HTTP 403 on fetch**), which is itself evidence that
the figure is contested rather than settled. **Merge consequence: the employee-number detail may not be
used to upgrade the Atari employment field; a number quoted only by parties who cannot agree on it is
weaker than the memoir it comes from.**

B-43 Claim: **The Wozniak-at-HP claim's carriers found by this pass are 2013-and-later retrospective
items — including a Business Insider piece dated 2013-02-01 reporting that Wozniak asked HP to make the
machine and was refused — so the HP field is a dated *retelling*, and its date of telling is 38+ years
after the employment it describes** — Date: 1969–1975 claimed (employment) / 2013-02-01 (carrier) —
Source: Business Insider, "Woz 'Begged' HP to Make the Apple PC" — Source date: 2013-02-01 — URL:
https://www.businessinsider.com/woz-begged-hp-to-make-the-apple-pc-2013-2 — Archived: not fetched
(budget); recorded as a lead with its date — Tier: 3 — Class: FOUNDER CLAIM (retrospective memory) —
Passage: NO_VERBATIM_PASSAGE_RECORDED (title and date only were recovered by search) — Conf: Low —
Corroboration: 0 in this project's reach — Conflicts: A2-57/A2-61c (no in-window HP connection of any
kind; B-38). A museum-side carrier also surfaced (a Computer History Museum item describing Wozniak as "an
engineer at Hewlett-Packard" before Apple), which is institutional but still retrospective. **Merge
consequence: HP employment may be recorded as a founder claim about the 1970s whose earliest carrier found
here is 2013, and it may not be printed as a dated employment fact without a personnel document.**

B-44 Claim: **The founding instrument's text appears to be publicly posted in a PDF that this project has
still not read — so the repository's longest-standing gate (D's L-8, W9, DG-D3) remains open, but the route
is now narrowed from "an unread auction catalogue" to "a downloadable document copy"** — Date: 1976-04-01
(document) — Source: Applefritter file copy, `applefritter.com/files/Apple PartnerShip Agreement.pdf`; a
Scribd copy ("Apple Computer Partnership Agreement 1976") and Reuters' 2025 auction photography item were
also returned — Source date: retrieved 2026-09-26 — URL:
https://www.applefritter.com/files/Apple%20PartnerShip%20Agreement.pdf — Archived: **UNANSWERED — WebFetch
returned a raw compressed PDF object stream with no extractable text: "It does not include any readable
portions of a 1976 Apple Computer partnership agreement."** The Christie's lot page was attempted again
and failed identically to D's W9 ("fetch failed"), and one news carrier returned **HTTP 404** — Tier: 1
(the document) / unreached — Class: UNKNOWN until read — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: n/a
— Corroboration: n/a — Conflicts: none. **This is a research-debt record, not a finding: the file exists at
a public URL, and the next pass should download the bytes and run local text extraction (the failure is an
extraction limit of the fetch tool, not evidence of absence). Until then B-18, B-19, B-20 and BC-1 hold
exactly where D left them.**

B-45 Claim: **Two of this dossier's UNKNOWN fields were targeted with the web budget and returned nothing
that could be cited: no dated Homebrew membership record naming either founder, and no dated employment or
schooling document, surfaced in the searches this pass was permitted** — Date: 2026-09-26 (attempt) —
Source: this pass's web log (§Sources consulted) — Source date: 2026-09-26 — URL: see W1–W10 table —
Archived: n/a — Tier: n/a — Class: UNKNOWN — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: n/a —
Corroboration: n/a — Conflicts: None. **Recorded so that no later agent mistakes an unexercised route for a
null (§14 rules 1 and 6): the searches returned folklore carriers and one unread PDF, not period records,
and four of the ten requests ended in a status code rather than in text.**

---

## Founder-state table at window start and end

Table form per §8. "Window start" = 1975 (Stage-1 opening edge, itself only Medium confidence per
E-17/B-15); "window end" = 1977-01-03 (the corporation date). Every cell is a **record**, and `UNKNOWN`
means what §3 says it means.

| Variable | Value at window start (1975) | Source | Confidence | Value at window end (1977-01-03) | Source | Confidence |
|---|---|---|---|---|---|---|
| Jobs — age | UNKNOWN | — | UNKNOWN | c. 21 (DERIVED backward from Feb 1981 print; ±1 yr) | A2-60, B-04 | Low |
| Jobs — named in Apple print | No (0 occurrences in 1975 cache) | B-15 [BYTE 1975-09 only] | Medium | Yes, once, four words ("Steven Jobs (Apple Computer Co)") | A2-56, B-02 | High |
| Jobs — function attributed | UNKNOWN | — | UNKNOWN | none stated | A2-59, B-08 | High (absence) |
| Jobs — address of record | UNKNOWN | — | UNKNOWN | UNKNOWN (company address is Cupertino, first printed 1977-05, after the window) | A2-25, A2-58, B-12 | High |
| Wozniak — age | UNKNOWN | — | UNKNOWN | c. 25–26 (DERIVED, ±1 yr) | A2-60, B-04 | Low |
| Wozniak — named in Apple print | No 1975 occurrence; first dated appearance 1976-04-30 as a club letter's benefactor | A2-19, B-29 | Medium | Yes — "designer of the Apple-ll computer" (April 1977 print, about the window's end) | A2-32 | High |
| Wozniak — work product in evidence | UNKNOWN for 1975 (no dated 1975 artifact names the machine; E-17) | A2 timeline row, E-17 | Low | Apple-1 designed and Apple II in demonstration; his own article in print 1977-05 | A2-25, B-10 | High |
| Wayne — presence in corpus | No | H-9, B-17 | High (absence) | No | H-9, B-17 | High (absence) |
| Wayne — stake | UNKNOWN | — | UNKNOWN | reported 10% (best supported) / 45/45/10 as allocation, **instrument unread** | E-04, D-11, B-18 | Low |
| Markkula — presence in corpus | No | A2-61a, B-01 | High (absence) | No | A2-61a, B-01 | High (absence) |
| Markkula — role | UNKNOWN | — | UNKNOWN | UNKNOWN in-window; 1981 print assigns the "from a garage operation" transition | E-06, B-21 | Low for Stage 1 |
| The company — legal form | UNKNOWN (no 1975 document) | B-15, E-17 | Low | partnership per an unread agreement; corporation filing date 1977-01-03 | B-18, B-26 | High for the filing date only |
| The company — name style in print | absent | A2-01…A2-04 | High (absence) | four authentic forms in circulation, none the partnership's | U-A2-1, B-27 | High |
| The company — price of first product in print | UNKNOWN | A2 quantitative row | High (absence) | UNKNOWN; maker's band "under $700" printed only 1977-05 | A2-25, B-10 | High |
| The company — revenue in print | UNKNOWN | E-12 | High | UNKNOWN; printed series begins FY1978 at $7.8M | E-28, U-A2-7 | High |
| The company — dealer relationship documented | none | L-4 | High (absence) | none for 1976 ("no 1976 document evidences an authorized Apple dealer relationship of any kind") | L-4 | High |
| Money — what each founder contributed | UNKNOWN | — | UNKNOWN | UNKNOWN for all four | DG-D9, B-23 | High (absence) |

---

## Network map as documented

Edges only where a dated document establishes them; each carries the earliest document that fixes it.
An edge absent here is not denied — it is undocumented in this evidence family.

| Edge | Type | Earliest dated document establishing it | Class | Confidence |
|---|---|---|---|---|
| Jobs ↔ Wozniak | named together | BYTE December 1976 editorial clause ("Steven Jobs (Apple Computer Co)") with Wozniak in the four-file census; strongest: the 1976-11-20 motel session | CONTEMPORARY OBSERVATION | Medium-High |
| Jobs ↔ Helmers ↔ **Bob Marsh, Chris Rutkowsky, Paul Terrell** | named as a four-person peer group, in one sentence, after a stated conversation | BYTE December 1976 editorial, recording conversations "on the floor of the WESCON show last September in Los Angeles CA" (`byte-1976-12.txt`:1513–1519) — **B-31** | CONTEMPORARY OBSERVATION; the class noun printed for all four is "entrepeneurs" | Medium-High |
| Jobs ↔ Carl Helmers / BYTE | in-person meeting | Helmers' account, published BYTE April 1977, event 1976-11-20 | CONTEMPORARY OBSERVATION, single witness | Medium-High |
| Wozniak ↔ Carl Helmers / BYTE | contributor relationship; commissioned article | BYTE April 1977 editor's credit and promise ("Next month, we'll have an article by Steve Wozniac, designer of the Apple-U computer"); BYTE May 1977 byline and author index | FACT (documents, same publisher) — B-33, B-34 | High |
| Wozniak ↔ Sonoma County Micro Computer Club | he transported a machine to them | Homebrew 1976-04-30, reprinting the club's letter | CONTEMPORARY OBSERVATION | Medium |
| Wozniak ↔ an unnamed club member operating his machine | a reader's build note uses "the Apple Computer" for a TV-monitor modification | Homebrew Vol 2 No 9 (`hcc0209.txt`:747–750) — **B-41** | CONTEMPORARY OBSERVATION, independent of the company | Medium |
| Jobs ↔ Paul Terrell (Byte Shop) | named as peers in one print list, in a stated conversation | BYTE December 1976, WESCON floor note (`byte-1976-12.txt`:1516–1518) | CONTEMPORARY OBSERVATION | Medium-High (strengthened by B-31's fuller sentence) |
| Apple ↔ Jim Warren (Faire General Chairperson) / Bob Reiling (Operations Manager, Homebrew newsletter editor) | the company is a committing exhibitor in the same document that names and telephones the two organisers | Homebrew Vol 2 No 9 (`hcc0209.txt`:225–262); Faire flyer `hcccf.txt` — **B-40** | CONTEMPORARY OBSERVATION | High as printed; the founder↔organiser contact itself is undocumented |
| Apple ↔ Computer Mart of New York | the product advertised by a retailer, no relationship claimed | BYTE September 1976 advertisement, 314 Fifth Avenue | CONTEMPORARY OBSERVATION | High (as printed); L-4 bars "dealer" framing |
| Apple ↔ Kentucky Fried Computers (Berkeley) | mail-order offer at 10% off manufacturer's list | BYTE November 1976 advertisement, 2465 Fourth Street, Berkeley (`byte-1976-11.txt`:20460–20500, read in full by this pass) | CONTEMPORARY OBSERVATION | Medium-High |
| Apple ↔ The Computer Mart (New York, 118 Madison Ave) | brand in a dealer's line-up list | Creative Computing Nov/Dec 1977 advertisement (intake) | CONTEMPORARY OBSERVATION | Medium; same retailer family as A2's ladder |
| Apple ↔ Shepardson Microsystems | co-location in one Stevens Creek complex, three building numbers apart | BYTE April 1977 masthead (`byte-1977-04.txt`:35103) + Wozniak's May 1977 byline (`byte-1977-05.txt`:6385) | FACT (as printed) | High |
| Apple ↔ Homebrew's membership | population of 6502 owners, counted | Homebrew Vol 2 No 6, 1976-06-09 survey | CONTEMPORARY OBSERVATION (organiser self-report) | Medium-High |
| Apple (as an institution) ↔ a peer-donor circle | the "Apple Education Foundation" is listed for information alongside Bell & Howell, Mountain Computer, Heuristics, Integral Data Systems, Interactive Structures, ABW and Videx | BYTE December 1980 (`byte-1980-12.txt`:81631–81637) — **B-39** | CONTEMPORARY OBSERVATION of 1980; out of window, printed to date the address's continuity | Medium |
| Jobs/Wozniak ↔ Markkula | **no document at any date in the corpus** | first print of Markkula is BYTE February 1981, which does not describe an introduction | — | UNKNOWN |
| Jobs/Wozniak ↔ Wayne | **no document at any date in the corpus** | — | — | UNKNOWN |
| Apple ↔ Venrock | shareholding only, no round documented | BYTE February 1981 ("holds 3.8 million shares") | FACT as printed | Medium (the holding) / UNKNOWN (the relationship) |
| Introduction events (who introduced whom) | **none documented** for any pair above | — | — | UNKNOWN |

**Reading of this map.** The documented network is a *trade* network — editor, clubs, dealers,
neighbouring firms — not a *founding* network. The three edges that a Stage-1 founder-state chapter
most needs (Jobs→Terrell, either founder→Markkula, either founder→Wayne) are the ones the record does not
supply: two are unknown at any date and one exists only as a same-page name list.

---

## Timeline

Events bearing on **founder state** only; product/channel/price chronology lives in A2's §Timeline and
is not duplicated. Conflicts cross-referenced.

| Date | Event | Source | Class | Confidence |
|---|---|---|---|---|
| 1975-09 | BYTE's founding issue prints zero "Apple"; the title that will carry Apple's first two years does not yet know it exists | intake `byte-magazine-1975-09` content test (B-15) | FACT (documented absence, one issue) | High |
| 1975 (late) | Apple-1 "designed late in 1975" — the Stage-1 opening edge, resting on the designer's single 1977 clause with no in-window 1975 witness | A2-25 / E-17 | FOUNDER CLAIM (contemporaneous) | Low-Medium |
| 1976-04-01 | Partnership agreement said to have been executed by three signatories; **no in-window print names it, dates it, or names the partnership** (U-A2-1, U-A2-10); instrument unread (B-18) | auction prose via D's L-8 | CONTESTED / document-based, unread | Low |
| 1976-04-30 | Sonoma County club letter, reprinted by Homebrew: an "APPLE 6502 system" was their guest and Wozniak provided transportation — first dated in-window appearance of a founder's name | `hcc0204.txt`:141 (B-29) | CONTEMPORARY OBSERVATION | Medium |
| 1976-06-09 | Homebrew survey: 101 live systems, 6502 second-most-owned at 18 — the size of the population the founders' network reached | A2-61 (B-28) | CONTEMPORARY OBSERVATION (self-report) | Medium-High |
| 1976-09 (WESCON, Los Angeles) | Helmers converses with "entrepeneurs" Bob Marsh, Chris Rutkowsky, **Steven Jobs (Apple Computer Co)** and Paul Terrell on the show floor — the dated peer-group edge, and the only location record for Jobs in 1976 outside the motel sighting | `byte-1976-12.txt`:1513–1519, published 1976-12 (B-31) | CONTEMPORARY OBSERVATION | Medium-High |
| 1976-09 | Computer Mart of New York advertises "the new Apple-1 computer" — the earliest product-naming advertisement, with no founder named; Homebrew's Vol 2 No 9 the same month lists "Apple Computers" among the firms committed to the Faire and names its two organisers with telephones | A2-08 / L-4; `hcc0209.txt`:225–262 (B-40) | FACT (as printed) | High |
| 1976-07 | BYTE prints another firm as "two people in a garage" — the garage was genre before it was Apple | `byte-1976-07.txt`:3023–3027 (B-22) | CONTEMPORARY OBSERVATION, different company; issue-date provisional (L-6) | Medium-High |
| 1976-09 | Computer Mart of New York advertises "the new Apple-1 computer" — the earliest product-naming advertisement, with no founder named | A2-08 / L-4 | FACT (as printed) | High |
| 1976-09 (WESCON) | Jobs and Terrell appear as peers in one printed floor note | `byte-1976-12.txt`:1516 (H-4) | CONTEMPORARY OBSERVATION | Medium |
| 1976-11 | Berkeley dealer offers the Apple-1 at 10% off "manufacturer's current list prices" — a list price no cached file prints | A2-11 (D's H-5) | FACT (as printed) | Medium-High |
| 1976-11-20 | Helmers sees both founders with the Apple II prototype in a Palo Alto motel room; Wozniak recodes a game afterwards — the strongest dated outside witness to either founder | A2-31 (B-09, B-11) | CONTEMPORARY OBSERVATION, single witness | Medium-High |
| 1976-12 | BYTE editorial prints "Steven Jobs (Apple Computer Co)" — the only 1976 printed mention of Jobs | A2-15/A2-56 (B-02) | FACT | High |
| 1976-12 | BYTE's 1976 ledger closes: 13 `Apple`-token lines, all accounted for, **zero maker copy, zero founder context** | H-6 | FACT (documented extent) | High |
| 1977-01-03 | Corporation incorporated in California (window end). Two lineage-free Tier-1 witnesses agree; the 1981 one gives the year only | AP-04/AP-19 (B-26, D-7) | FACT | High (year) / Medium (day) |
| 1977-04 | BYTE editor credits Wozniak as "designer of the Apple-ll computer" and promises next month's article by him; the Apple II is billed for the April Faire; Shepardson's masthead shows the address cluster; the "appliance computer" primacy claim is printed with the hedge "may be the first" | A2-32, A2-58, B-33, B-40 | CONTEMPORARY OBSERVATION | High |
| 1977-05 | Wozniak publishes under the Cupertino address: no customer, no order, no units, no figure, price "under $700". BYTE's own text says "Wozniak's Apple BASIC interpreter" and indexes him as author | A2-25, B-10, B-34 | FOUNDER CLAIM (contemporaneous) + CONTEMPORARY OBSERVATION | High (as printed) |
| 1977-06 | Apple's first self-published BYTE advertisement: $1,298 complete / $598 board-only, address and telephone — **and a direct-mail order form taking BankAmericard, VISA and Master Charge, with a free $50 carrying case and seller-paid shipping** | A2-27 (B-12, B-35) | FACT (as printed) | High |
| 1977-07 | The same order form and full nine-line ladder recur with RAM-chip prices; the PONG/Atari trademark line appears again in Apple's own copy | `byte-1977-07.txt`:3960–4130 (B-36, B-38) | FACT (as printed; one campaign) | High |
| 1977-09 | Apple buys a two-page front-of-book advertisement under "Apple Computer Inc."; the Atari trademark line appears in Apple's own copy | intake BYTE Sept 1977 (B-13, B-06) | FACT (as printed; OCR partial) | High on copy / Medium on spec numerals |
| 1977-11 | Creative Computing carries Apple as a brand in New York dealer advertisements; no Apple review in the issue | intake Creative Computing (B-14) | CONTEMPORARY OBSERVATION | Medium |
| 1981-02 | The only print carrying the founders' ages and holdings, and the only Apple-linked garaging in the cache: Jobs 25, Wozniak 30, Markkula 32, 8.3M shares each, "from a garage operation" | A2-51/A2-60, L-5 (B-04, B-21) | FACT as printed; `RETROSPECTIVE SOURCE` for Stage 1 | High (printed) / Low (as 1976 evidence) |

---

## Data gaps

`UNKNOWN` fields restated as gaps with the artifact class that would close them. `follow_up_task` is
mandatory where importance is High (§13).

| Gap ID | Field / gap | Why missing | Importance | What would evidence it | Confidence in the gap |
|---|---|---|---|---|---|
| BG-1 | Jobs's and Wozniak's education and completion status | Schooling is not a periodical subject; no cached document of any vintage mentions it | **HIGH** (§7 field list) | Registrar/enrolment records; a dated student newspaper mention; a transcript; a 1972–75 yearbook or employer application with the institution verified | High that the corpus is silent |
| BG-2 | Jobs's Atari employment, with dates | Auction curation prose only; the corpus's single `Atari` string is Apple's trademark disclaimer (B-06) | **HIGH** | Atari personnel records, a pay stub, a dated colleague testimony, or a 1974–76 trade mention of him by name | High that in-window print cannot carry it |
| BG-3 | Wozniak's Hewlett-Packard employment, with dates | A2-57/A2-61c: `Hewlett`/`Packard`/`HP-65` occur only as calculator/component matter | **HIGH** | HP employment record, an internal HP publication naming him, or a dated colleague statement | High |
| BG-4 | What each founder could actually put up, and how the money arrived | No founder-state money document exists in this family; the agreement is unread (B-18) and the printed revenue series starts FY1978 | **HIGH** | The partnership agreement's capital clause (DG-D3), a bank or credit instrument, a distributor credit record (Cramer route, DG-D9), the 1977 Statements of Information | High |
| BG-5 | Wayne's role, stake, exit date and amounts | Zero in-window presence; only retrospective and commercial carriers | **HIGH** | The instrument itself; a county FBN filing naming partners (DG-D6); Wayne's withdrawal document | High |
| BG-6 | Markkula's arrival date, terms, and any pre-1981 relationship to the founders | One 1981 sentence is his whole footprint | **HIGH** | Incorporation-era stock records; California SoS Statements of Information, 1977; any 1977–79 document naming him | High |
| BG-7 | The garage as a place: address, ownership, municipality, who worked there | Not a periodical question at all; all 17 `Los Altos` lines in the cache are third parties | **HIGH** | Assessor/recorder ownership chain; a 1976 lease or utility record; a contemporaneous photograph with a datable caption | High |
| BG-8 | Division of labour between the four subjects | Actively absent from 1976–77 text (B-08) | **HIGH** | A dated internal document — minutes, a letterhead with titles, a signature block, a cheque endorsement | High |
| BG-9 | Who introduced whom | No introduction is documented at any date in the corpus | MED-HIGH | Correspondence, meeting records, or a dated interview in which a third party — not a founder — fixes the meeting | High |
| BG-10 | Employment status of both Steves during 1976 | Bylines and newsletters are not personnel records; silence is not proof | MED-HIGH | Same artifact classes as BG-2/BG-3 | High that it is unresolved |
| BG-11 | Kilobaud 1976–77 and the remaining Interface Age issues, unread for founder mentions | 1976 Kilobaud items expose no text layer, but **Kilobaud 1977-onward does have one** (intake §B — a correction to the house note); Interface Age 1976 identifiers resolve inconsistently (metadata 200 with a 2-byte `{}` body) | **HIGH** — the titles most likely to print a founder name, a dealer list or a price | OCR/read the 1977+ Kilobaud layers and re-derive live Interface Age identifiers from the search body, then grep `Apple Computer`, `Wozniak`, `Jobs`, `Wayne`, `Markkula`, `666` | High that these remain untried |
| BG-12 | BYTE 1975-10/-11/-12 and 1981-03…12 unread | Intake enumerated all as new and left them unspent (intake §D.1–2) | MED — 1975 issues could move the Stage-1 start edge; 1981 issues carry the IPO-year founder reporting that might date Markkula's arrival | retrieve via `metadata/byte-magazine-YYYY-MM` → layer, mine in scratch, ship bounded extracts | High |
| BG-13 | Whether the September 1977 advertisement's spec-table numerals are reliable | The intake's own OCR note: 'Apple 11' / 'Apple n' / 'Apple Ilf' for 'Apple II'; numerals partly garbled | MED | inspect the scan at full zoom or the rescan twin item | High (declared by the source) |
| BG-14 | Any dated evidence of Jobs's negotiating, selling or financing activity | The corpus records his presence twice and never an act | **HIGH** (it is the §7 "capability evidenced by work products" field) | a signed invoice or purchase order, a dealer agreement with his signature, a dated letter in BYTE's correspondence columns | High |
| BG-15 | The text of the 1976-04-01 partnership agreement — signatories, addresses, capital clause, allocation, withdrawal terms | The document is **publicly posted as a PDF** (`applefritter.com/files/Apple PartnerShip Agreement.pdf`) and the fetch tool returned an undecoded compressed object stream; the official lot page failed twice from two different passes ("fetch failed"), one news carrier 404'd, and a name-quoted search returned nothing | **HIGH** — one instrument would settle BG-4, BG-5, BC-1 and the partnership's legal style at once | **Download the bytes and extract locally** (`pdftotext`/`mutool`, or render the pages and read the scan) rather than re-attempting the two endpoints that have now each failed; also the Scribd copy and Reuters' 2025 photography item | High that it remains unread; High that a copy is reachable |
| BG-16 | Dated employment records for Atari and Hewlett-Packard | Every carrier surfaced by this pass's web budget is retrospective: a 2011 trade article whose body would not render (W6), a 403'd dispute about the employee number (W7), a 2013 business-news item (W2) | **HIGH** (both are §7 fields and both are load-bearing for the capital story) | Atari and HP personnel/payroll records; a dated colleague statement; a museum or archive collection with accessioned employment documents | High that periodicals cannot carry these fields (B-38) |

---

## Contradictions

Format per §7 (CLAIM A / CLAIM B / WHY THEY DIFFER / EVIDENCE WEIGHT / BEST-SUPPORTED INTERPRETATION /
RESIDUAL UNCERTAINTY / CONFIDENCE). Cross-referenced to A2's U-A2-nn and D's D-nn rather than re-litigated.

**BC-1 — A three-partner founding versus a two-founder printed record.** / CLAIM A: the 1976-04-01
agreement had three signatories and Wayne's name on it (auction prose; U-A2-10). / CLAIM B: Wayne appears
in **zero** documents in the cached 1976–1981 corpus, including the February 1981 column written for
investors (B-17, E-04). / WHY THEY DIFFER: one side is a physical instrument nobody in this project has
read; the other is a press corpus that did not report people at all — the same corpus omits Markkula too,
so its silence is a property of the source class, not of Wayne's absence from the world. / EVIDENCE
WEIGHT: the document class outranks the print class for the *fact of a third signatory*; the print class
is decisive for what was publicly knowable in 1976. / BEST-SUPPORTED INTERPRETATION: print both — a
three-signatory instrument of reported date exists and is unread, and the founding-era public record was a
two-founder story. / RESIDUAL UNCERTAINTY: the actual names, percentages, signing place and any withdrawal
terms. / CONFIDENCE: High on the printed two-founder record; Low on the three-signatory reading until the
lot text or a page photograph is read. (Feeds U-A2-10, D-11, L-8.)

**BC-2 — The founders' ages as a Stage-1 fact versus a 1981 artifact.** / CLAIM A: the founders were 21
and 25 at the partnership (widely printed). / CLAIM B: the only ages in this corpus appear in BYTE
February 1981 (B-04), and any 1976 age is a backward derivation from an integer. / WHY THEY DIFFER:
derived versus observed; a later document is being quoted as if it were a period one. / EVIDENCE WEIGHT:
the 1981 sentence is Tier 1 for 1981 and `RETROSPECTIVE SOURCE` for 1976. / BEST-SUPPORTED
INTERPRETATION: state the ages as printed in 1981, and any Stage-1 age as a ±1-year derivation. /
RESIDUAL UNCERTAINTY: birth dates; the corpus carries none. / CONFIDENCE: High as printed / Low for the
window.

**BC-3 — Jobs as a salesman-founder versus a corpus that never records a sale.** / CLAIM A: the standard
division of labour — Jobs sold, Wozniak designed. / CLAIM B: no 1976–77 text attributes any function to
Jobs (B-08), and the only act he is documented performing is being present (B-02, B-09). / WHY THEY
DIFFER: the division of labour is reconstructed from retrospective testimony and inference from the
company's later shape; the in-window class of document (trade print, club letters, dealer ads) had no
reason to record roles. / EVIDENCE WEIGHT: Wozniak's design credit is contemporaneous and outside
(H-2, A2-32); Jobs's selling role has no contemporaneous witness. / BEST-SUPPORTED INTERPRETATION: the
designer side of the pair is documented; the salesman side is UNKNOWN for the window and must be
labelled by the vintage of whatever carries it. / RESIDUAL UNCERTAINTY: a signed 1976 order document, or
any dealer's dated statement naming him, would settle it. / CONFIDENCE: High (asymmetry is documented).

**BC-4 — The garage origin versus the address of record and the genre usage.** / CLAIM A: Apple was born
in the Los Altos garage at 20211 Crist Drive (E-07). / CLAIM B: the company's only 1976–77 published
address is Cupertino 20863 Stevens Creek Blvd Bldg B3-C (B-12, B-13), and the strongest Apple-linked
garaging line in the cache is a 1981 editorial gloss that post-dates the events by five years (B-21), while
"two people in a garage" was already a 1976 genre phrase about another firm (B-22). / WHY THEY DIFFER: a
residence/workplace claim and a business-address claim are different propositions; periodicals print the
latter and never the former. / EVIDENCE WEIGHT: property and lease records outrank both classes; neither
has been reached (DG-D5). / BEST-SUPPORTED INTERPRETATION: a Cupertino office-park suite is the documented
1977 premises; the garage remains UNSOURCED within the period and **not refuted** (D's H-7 warns against
overcorrection). / RESIDUAL UNCERTAINTY: whether any work occurred at a private residence in 1976, and
where. / CONFIDENCE: High on the address of record; UNKNOWN on the garage.

**BC-5 — The capital route: personal asset sales versus trade credit versus outside money.** / CLAIM A:
$500 (HP-65) + $750 (VW bus) paid for the first boards (memoir, B-23). / CLAIM B: a founding partner later
believed a $15,000 loan filled the order (E-14). / CLAIM C: the money in the printed record is 1981's —
Markkula's holding and Venrock's shares — with no date of arrival (B-24). / WHY THEY DIFFER: three
different vintages (2006 memoir, 2022 participant letter, 1981 trade column) describing three different
mechanisms, none contemporaneous. / EVIDENCE WEIGHT: none is documentary for 1976; the Cramer Electronics
credit mechanism is period-plausible because Cramer is a real Bay Area distributor in these same pages, and
that is mechanism, not evidence (D's Unsourced table). / BEST-SUPPORTED INTERPRETATION: §K and this
dossier carry founder-contributed capital as **UNKNOWN**, with the three tellings recorded as a lineage
table. / RESIDUAL UNCERTAINTY: everything about the money. / CONFIDENCE: High that it is unresolved.

**BC-6 — Whether Apple's founding-era channel was a dealer network.** / CLAIM A: Terrell's Byte Shop was
the founding customer and Apple ran a dealer network. / CLAIM B: no 1976 document evidences an authorized
Apple dealer relationship of any kind (L-4), the Byte Shop's own 1976 advertising never mentions Apple
(L-1), and the earliest product advertisement is New York, September 1976 (B-14, A2-08). / WHY THEY
DIFFER: retrospective scene-building versus an OCR brand list. / EVIDENCE WEIGHT: the dated
advertisements. / BEST-SUPPORTED INTERPRETATION: a house selling boards to whoever came, with a plausible
but undocumented Terrell relationship; "first store", "first dealer" and "dealer network" barred for 1976.
/ RESIDUAL UNCERTAINTY: an invoice or a Terrell statement dated in-window would change this. /
CONFIDENCE: High on the print facts.

**BC-7 — "Word of mouth, California first" versus the dated advertisement ladder.** / CLAIM A: Wozniak's
May 1977 sentence (B-10). / CLAIM B: New York September 1976, Berkeley November 1976, the maker's own
advertising only from June 1977 (L-10). / WHY THEY DIFFER: a compressed retrospective ordering versus a
publication ladder. / EVIDENCE WEIGHT: the ladder. / BEST-SUPPORTED INTERPRETATION: cite the sentence as
FOUNDER CLAIM (contemporaneous) for channel *type*; build *sequence* from dated advertisements. / RESIDUAL
UNCERTAINTY: whether California sales volume preceded New York's advertisement. / CONFIDENCE: High.

**BC-8 — One unsigned column as the sole founder-state money witness.** / CLAIM A: the 1981 column's ages,
holdings and revenue series are reliable company history. / CLAIM B: it is unsigned, single-lineage, mixes
dollar-exact and rounded figures internally (U-A2-8), and its offering arithmetic does not close (U-A2-9,
B-25). / WHY THEY DIFFER: a company-supplied PR series is being read as audited data. / EVIDENCE WEIGHT:
Tier 1 for what was printed; nothing for what was audited. / BEST-SUPPORTED INTERPRETATION: use it for the
1981 state and for the ages/holdings **as printed**, never as Stage-1 measurement. / RESIDUAL UNCERTAINTY:
the prospectus remains unread (AP-02, AP-21). / CONFIDENCE: High on printed content; Low on provenance.

**BC-9 — Whether any technical act of Jobs's was ever witnessed.** / CLAIM A: Helmers' first-person-plural
account of 1976-11-20 — "Steve Jobs, Steve Wozniak and I sat down and proceeded to use the Apple-ll BASIC
… After perhaps 30 to 45 minutes, **we** had a working BASIC language version" (B-32, BSS-02). / CLAIM B:
A2-59 and this file's B-08 — print attributes no function to Jobs in any 1976–77 text. / WHY THEY DIFFER:
they address different objects. B-08 speaks for the **company's own** documents, which name him nowhere;
B-32 is a **third party's collective pronoun**, which is not a function attribution but is not zero either.
/ EVIDENCE WEIGHT: one interested witness, published five months after the event, against a documented
absence in every first-party text. / BEST-SUPPORTED INTERPRETATION: hold both precisely — no document
attributes a design, a code contribution, a written work product or a commercial act to Jobs, and the only
pronoun that places him at a keyboard is Helmers' "we". Neither "Jobs programmed it" nor "Jobs never touched
the machine" is supported. / RESIDUAL UNCERTAINTY: what he actually did that evening is unrecoverable from
this witness; the second Wozniak sentence in the same passage ("Later, Steve Wozniak recoded the program")
is the only allocation of a technical act anyone makes. / CONFIDENCE: High that the tension exists; Low on
its resolution.

**BC-10 — Whether the December 1976 clause is silent about role.** / CLAIM A: A2-56 — the Jobs mention
"carries no age, no employer, no school, no city and no role" (adopted at this file's B-02). / CLAIM B: the
sentence of which the clause is the tail classes him: "my conversations with **entrepeneurs** Bob Marsh
(Processor Technology), Chris Rutkowsky (Technical Design Labs), Steven Jobs (Apple Computer Co) and Paul
Terrell (Byte Shops)" (B-31, BSS-01). / WHY THEY DIFFER: A2 quoted the four-word fragment rather than the
sentence containing it. / EVIDENCE WEIGHT: same document; the fuller quotation simply carries more of it. /
BEST-SUPPORTED INTERPRETATION: A2-56 remains correct for age, employer, school and city, and is corrected
for role: an outside editor assigned him a **class** (operator/entrepreneur) among four named peers, in the
year itself, with a place and a month. A class is not a function — the record still attributes no act. /
RESIDUAL UNCERTAINTY: whether Helmers's use of the word reflects a first-hand impression of Jobs's role or
a loose courtesy category applied to four exhibitors. / CONFIDENCE: High (it is a quotation-boundary error,
resolvable on the page).

---

## Knowability split

Rule applied: a founder-state item is KNOWABLE at window-end only if a document existing by 1977-01-03
carried it to somebody outside the partnership. Later proof that something *was* true then is not
knowability.

**KNOWABLE in-window (evidenced):** that an "APPLE" 6502 system existed and had a named designer who
delivered it himself to a club (1976-04-30, B-29); that a product named Apple-1 was being advertised by
retailers on both coasts (1976-09, 1976-11, B-14); that a company styled "Apple Computer Co" existed with
Jobs named on it, and named **as one of four "entrepeneurs"** by the editor of the field's leading title
(1976-12, B-02, B-31); that both founders were personally working with a working Apple II prototype in late
November 1976, and that the machine's design and BASIC were publicly credited to Wozniak (B-09, B-33, B-34);
the size and processor mix of the club population the machine addressed (B-28); the company's office-park
address cluster in April–June 1977 (B-12); the maker's own 1977 price pair **and its payment instruments,
freight terms and upgrade pricing** (B-13, B-35, B-36); the identity, titles and telephone numbers of the two
Faire organisers whose circuit carried the product (B-40).

**NOT KNOWABLE in-window:** whether any of the money in the later tellings had arrived; who the third
partner was (no printed document names the partnership at all); whether the Byte Shop relationship existed
and on what terms; whether the company had any revenue; whether Markkula had any connection to the firm; what
job title, if any, either founder held in his own company (B-37 — no officer word appears in founding print).

**UNKNOWN (no evidence either way):** every subject's education, birth date, employer, residence, cash
position, and any statement of role; every introduction edge; the partnership's terms; the 1976 price;
1976–77 revenue; production volume; the garage.

---

## Narrative notes

**What this dossier actually is.** A record of how little a founding-era press knew about four people, and
of how much of what is said about them descends from sources this project can date but cannot credit. Two
subjects are visible in the period and two are not visible at all; and of the two who are visible, one is
visible **as an author** — signed, address-bearing, credited by an editor as the machine's designer — and
the other is visible **as a name in a clause** and as a man standing in a motel room. That asymmetry is the
single most important finding in this file, and it is the opposite of the popular picture, in which the
less-documented of the two is the operating presence and the documented one is the support.

**The founders as the documents describe them, with no adjectives.** Wozniak: a person who by April 1976
owned or had built an "APPLE 6502 system" and drove it to a club in another county; who by November 1976
had a machine a magazine editor watched him re-code from game BASIC into 6502 assembly "and reports that
the Color Eater now runs like lightning"; who in May 1977 published under a Cupertino suite and printed no
customer, no order, no unit count and no price, only "a price under $700 at the retail level". Jobs: named
once in 1976 print, in four words, beside a company styled "Apple Computer Co" — but in the same sentence
sorted by BYTE's editor into a class, "entrepeneurs", whose other three members were the principals of
Processor Technology, Technical Design Labs and the Byte Shops, after conversations on the WESCON floor in
Los Angeles in September 1976; present with Wozniak in a Palo Alto motel room on 20 November 1976, where the
editor's pronoun for the programming session is "we" but the recoding is credited to Wozniak alone. Wayne: no
document at any date. Markkula: one sentence, dated February 1981, giving him 32 years, 8.3 million shares,
and credit for taking the company "from a garage operation".
Nothing in the cached corpus says what any of the four was paid, owned, owed, or refused. There is no
dated 1976 payroll, no dated 1976 bank instrument, no dated 1976 letter of introduction, and no document
of any vintage in this family that names all four together.

**The three most-cited founder-state legends this dossier could not source in-window.** (i) The
calculator-and-bus financing: single memoir lineage, 2006, zero independent witnesses, and the only
in-window `HP-65` string in the corpus is another advertiser's retail price for the calculator (B-05,
B-23). (ii) The $666.66 list price: absent from every cached in-window file, and the corpus's only
dollar-shaped 666 is a competitor's strike-through anchor for an IMSAI 8080 bundle (D's L-2); the maker's
only printed number is a band, "under $700" (B-10). (iii) Jobs's Atari employment: the string occurs in
the founding-era corpus exactly once, as Apple disclaiming somebody else's trademark in Apple's own
advertisement (B-06). A fourth deserves naming because it is a *role* legend rather than a number: the
salesman/designer division has no 1976–77 witness at all (BC-3).

**Where the record-selection null bites hardest.** The gaps are not evenly distributed; they are
structured. Trade print records brands, addresses, prices and dealer lists, because that is what its
advertisers and readers wanted. So the *company* side of Apple's Stage 1 reconstructs richly — the intake
alone extended the price ladder and the address of record into a new month (B-13) — while the *person*
side collapses to five documents (B-01). Any Stage-1 text that reads smoothly about the founders is
thereby suspicious, and this file's UNKNOWN density is the honest shape of the surviving evidence, not a
failure to find it.

**The 1981 problem, stated once and applied everywhere.** BYTE February 1981 is a Tier-1 document about
1981. It supplies every age, holding and share number in this dossier, and the "garage operation" phrase
that anchors the origin scene. Because it is unsigned, company-sourced in its financial series, internally
inconsistent in its offering arithmetic, and five years downstream of the events, **each of its Stage-1
uses is tagged in the record that uses it** (B-04, B-21, B-24, B-25, BC-2, BC-8) — and the file's founder
table carries the ages under a derivation label rather than as observations.

**The three best-documented founder-state facts in this dossier.** All three are dated, all three are
outside the company's own copy, and all three survive D's founder-discard test. (1) **Jobs was classified as
an operator by an outside editor, alongside three named industry peers, in the year itself**: Helmers names
"entrepeneurs Bob Marsh (Processor Technology), Chris Rutkowsky (Technical Design Labs), Steven Jobs (Apple
Computer Co) and Paul Terrell (Byte Shops)" after conversations "on the floor of the WESCON show last
September in Los Angeles CA" (B-31, BSS-01). (2) **Wozniak's design credit is printed by BYTE twice and
carries a work product with it** — "designer of the Apple-ll computer" in April 1977, and in May 1977 the
possessive "Wozniak's Apple BASIC interpreter", an author-index entry, and an abstract saying he "describes
the design of such a system" (B-33, B-34, BSS-02/BSS-03). (3) **Both founders were physically present with a
working Apple II prototype at a named place on a named evening**, and the only technical act any document
allocates to either of them in 1976 is Wozniak's assembly re-code (B-09, B-11, B-32). Nothing else about the
four subjects is documented this well: ages, schools, employers, cash, residences, titles and roles all fail
the same test.

**What would change this dossier most.** In order of leverage: reading the partnership agreement's actual
text, which is now known to be **publicly posted as a PDF** and needs only local text extraction rather than
another fetch attempt (names, date, capital clause, addresses and the partnership's legal style all at once —
B-18, B-44, BSS-14, BG-15); the October 1976 advertisement image at full resolution, the one realistic
candidate for an in-window price and letterhead (D's DG-D2); Kilobaud 1977-onward and a re-derived Interface
Age identifier run (BG-11, OC-B3), which is the class of trade print most likely to name a person rather than
a brand; and one county recorder's file for the premises (BG-7).

---

## Sources consulted

**Locally cached primary (0 web requests; every Apple-bearing citation either re-verified at line level
by this pass or marked `[inherited]`).**

| Source | Type | Primary/Secondary | Event date | Publication date | Route / location | Tier | Confidence |
|---|---|---|---|---|---|---|---|
| BYTE Jan–Dec 1976 (12 full-issue OCR layers) | trade magazine | primary | 1976 | 1976-01…12 | `sources/ia_byte_1976/` | 1 | High on content; Medium on Jan–Sep month labels (D's L-6/D-6) |
| BYTE Apr–Jul 1977 | trade magazine | primary | 1977 | 1977-04…07 | `sources/ia_byte_1977/` | 1 | High |
| BYTE Dec 1980, Feb 1981 | trade magazine | primary for 1980–81; `RETROSPECTIVE SOURCE` for 1976–77 | 1976–1981 | 1980-12 / 1981-02 | `sources/ia_byte_1981/byte-1981-02.txt`:48494–48525 | 1 | High as printed |
| Homebrew Computer Club newsletters (13 items, incl. Faire flyer) | club print | primary | 1975-11-30 → 1977-02-16 | same | `sources/ia_homebrew/`; `hcc0204.txt`:131–144; `hcc0206.txt` | 1 | High, with per-item provenance discipline (L-3) |
| Apple Computer, Inc. Form 10-K FY1994 | SEC filing | primary | 1977-01-03 (recited) | 1994-12-13 | `sources/10-K_FY1994_acc-0000320193-94-000016_filed-1994-12-13.txt`:132–135 | 1 | High |
| `apple1registry_stories.txt` / `.html` | collector curation | secondary reporting of artifacts | 1973 / 1976 claimed | 2018–2022 | `sources/` (Wayne at `.html`:488) | 3 | Medium on artifact existence; Low on curator dates |
| **Intake: BYTE September 1977 extract** (new month of a held title) | trade magazine, bounded extract | primary | 1977-09 | 1977-09 | `00_universe/harvest/periodicals_intake/apple_microcomputer_sector/BYTE_1977-09_EXTRACT_apple2_ad_and_editorial.txt` | 1 | High on ad copy and index; Medium on spec numerals (BG-13) |
| **Intake: BYTE September 1975 content test** (new year) | trade magazine | primary | 1975-09 | 1975-09 | same directory, `SEARCH_LOG.md` §A and extract §D | 1 | High (single-issue negative) |
| **Intake: Creative Computing Nov/Dec 1977 extract** (new title) | trade magazine, bounded extract | primary (third-party dealers) | 1977-11 | 1977-11 | `…/CREATIVECOMPUTING_1977-11_EXTRACT_apple_mentions.txt` | 1 | Medium (OCR noise; only 3 `Apple` hits, no review) |
| **Intake: IA inventory JSONs + SEARCH_LOG** (Kilobaud, Interface Age, Creative Computing, Popular Electronics) | registry index | primary about coverage only | — | 2026-09-25 | `…/ia_kilobaud_interfaceage_creativecomputing_popelectronics.json`, `ia_byte_run_1975-1995_by_issue.json` | 1 | High as index facts; Popular Electronics UNTRIED |
| `sources/_RETRIEVAL_LOG.md` and the probe JSONs | retrieval provenance | primary about the cache | — | 2026-09-24 | `sources/` | 1 | High — read before mining, per the header trap |
| A / A2 / C / D dossiers and the four registers | project dossiers | secondary (inherited and cross-cited) | — | 2026-09-24/25 | `research/` | n/a | used as cited |

**Web (hard cap 10; 10 spent after local mining was on disk, per §14 rule 1).** Status recorded per
§14 rule 1; every failure is UNANSWERED with its request and status code, never a null finding.

| # | Request | Status | What it bought |
|---|---|---|---|
| W1 | WebSearch — "Steve Jobs Atari employee 1974 1975 Pong designer employment record" | OK | The dated carrier inventory for the Atari field: gamedeveloper.com "Steve Jobs, Atari Employee Number 40" (2011-10-06), a 2020 retrocomputing.stackexchange dispute over whether the number is even right, plus Quora/Facebook/YouTube repetition → B-42 |
| W2 | WebSearch — "Steve Wozniak Hewlett-Packard employee 1973 1974 joined HP job" | OK | Carriers for the HP field are all retrospective: Business Insider 2013-02-01, a museum social item, Wikipedia → B-43. No period document surfaced |
| W3 | WebSearch — "Apple Computer Company partnership agreement April 1 1976 three partners signatories text" | OK | **The route to the instrument itself**: a public PDF copy at applefritter.com, a Scribd copy, the official Christie's lot URL, Reuters' 2025 auction photography item → B-44 |
| W4 | WebSearch — agreement text with "Ronald Wayne" / "45%" phrase | OK | No transcription surfaced; results were unrelated aggregator pages. Recorded as nothing, not as absence |
| W5 | WebFetch — `applefritter.com/files/Apple PartnerShip Agreement.pdf` | **FAILED (usable text)** — returned a raw compressed PDF object stream | The fetch tool could not decode the stream: "It does not include any readable portions of a 1976 Apple Computer partnership agreement." **UNANSWERED**; the lead stands and is now sharper than D's DG-D3 → B-44 |
| W6 | WebFetch — `gamedeveloper.com/business/steve-jobs-atari-employee-number-40` | **PARTIAL** — page shell only | Headline and the 2011-10-07 timestamp only; "the full article body is absent, containing only JSON-LD schema, minified scripts, and site navigation" → B-42 |
| W7 | WebFetch — retrocomputing.stackexchange question on employee #40 | **HTTP 403** | UNANSWERED (403 on fetch) — the tool advised no retry → B-42, B-45 |
| W8 | WebSearch — "Steven P. Jobs" "Stephen G. Wozniak" "Ronald G. Wayne" agreement address | OK | Two hits only, one of them an unrelated Atari history site: the exact-name search did **not** return a transcribed clause or an address from the instrument → B-45 |
| W9 | WebFetch — `expansion.mx/.../sothebys-subastara-el-contrato-de-fundacion...` (2011 Sotheby's report) | **HTTP 404** | UNANSWERED (404) |
| W10 | WebFetch — the Christie's lot page for the partnership agreement | **FAILED: "fetch failed"** | UNANSWERED — reproduces D's W9 failure exactly, which is itself a finding: **this URL is unreachable by the fetch route, and the next pass should use the applefritter PDF with local text extraction instead** |

**Net yield of the web budget, stated plainly:** no founder-state field moved from UNKNOWN to FACT. What
the 10 requests bought is (i) **first-dated-carrier evidence for three legends** — the Atari employee-number
claim has a 2011 carrier (W1/W6), the HP offer/refusal story a 2013 one (W2), and both therefore belong to
the retrospective class the brief prescribes; (ii) **a narrower, still-unread route to the founding
instrument** (W3/W5/W10), which converts a dead end into a specified next task; (iii) **confirmation of two
retrieval blockers** (the PDF stream, the Christie's endpoint) that a later pass can route around with
local extraction. Four of ten requests ended in a status code; nothing in this file asserts that a fact
"does not exist" because a fetch failed.

---

## Provenance and method notes

**Ownership and non-destruction (§14 rule 4).** One file written: this one. Nothing in `sources/`,
`00_universe/harvest/`, or anywhere else was created, moved, renamed, tidied or deleted by this pass; no
sibling dossier was edited, including `A_chronology_feasibility.md`, whose supersession markers were
left exactly as found. The protected archive is byte-untouched as at close.

**Grep log for this pass (2026-09-25/26, against `sources/` and the intake directory; headers and
provenance carriers filtered out per §Working method).** `jobs` across the four `ia_*` directories → 18
lines surviving the filter, of which **two** are personal-name references to Steve Jobs: `ia_byte_1977/
byte-1977-04.txt`:2744 ("That evening last November, Steve Jobs,") and `ia_byte_1981/byte-1981-02.txt`:48509
("Steve Jobs, 25 years old,"); the remaining 16 are the ordinary-English plural ("more jobs", "active jobs",
"Changing jobs", "losing their jobs", "quick and dirty jobs"), which is why a name census must be read in
context rather than counted. `666` re-run across `ia_byte_1976`, `ia_byte_1977`, `ia_homebrew` → **17
surviving lines**, and D's L-2 decoy inventory reproduces exactly: the only dollar-shaped occurrence is the
competitor's anchor `ia_byte_1976/byte-1976-12.txt`:39849 "a $666 value" (the IMSAI 8080 bundle), and the
rest are one New Hampshire advertiser's telephone "(501)666-2839" repeating across five issues, ZIP and
suite fragments, technical prose, and a Cupertino telephone ending 4666 — **no Apple price line exists
anywhere in the cached in-window files**. `wozni*` → 12 lines in four files (BYTE Apr 1977 ×5, May 1977 ×5, Feb 1981 ×1, Homebrew
1976-04-30 ×1), including the OCR form `Wozniac` at `byte-1977-04.txt`:2688 — A2's four-file census
reproduced exactly. `markkula` → **1 line** in the whole cache (`byte-1981-02.txt`:48516). `wayne` → 20+
lines, **zero** Apple-attributed (Fort Wayne, Wayne State, Wayne Green, Wayne Sewell, Wayne Smith, Wayne PA,
Wayne Av, Wayne County School District, Dwayne Jeffries). `wescon` → **1 line**, `byte-1976-12.txt`:1518.
`entrepene*|entreprene*` → 18 lines, of which exactly one applies to a founder (`byte-1976-12.txt`:1514).
`president|vice-president|treasurer` restricted to Apple/person context → **0 lines** (B-37). `atari` → 6
lines: two "PONG is a trademark of Atari Inc." in Apple's own June and July 1977 advertisements and four
third-party "ATARI GAME BOARDS" advertisement fragments (B-38). `hewlett|packard` in 1976/1977/Homebrew →
calculator, LED component and press matter only. `reed college|dropout|dropped out|college student` → no
Apple-person context; the `dropout` hits are tape-error prose. `stevens creek` → 3 lines across the whole
cache: `byte-1977-04.txt`:35103 (Shepardson, 20823), `byte-1977-05.txt`:6385 (Wozniak's byline, 20863),
`byte-1980-12.txt`:81635 (Apple Education Foundation, 20863) — the last found by this pass. `Order Form |
carrying case | pay shipping` in `byte-1977-06.txt` → the advertisement's mail-order apparatus at lines
2286–2288 and 2412–2459 (B-35). `apple` in `ia_homebrew/` → 5 body lines below the caching header
(`hcc0202.txt`:334 idiom, `hcc0204.txt`:133 and :140, `hcc0209.txt`:234 and :748), i.e. the corrected scope
D's L-7.2 demanded. Every other founder-state claim in this dossier is carried by a record whose line number
was verified by A2, by D, or by this pass, and the verification owner is named in the record.

**Two verification hazards inherited and applied.** (i) Hard-wrapped filings — the FY1994 10-K sentence
that anchors this chronology does not match a one-line literal grep; it must be cited by line range
(L-7.1). (ii) Self-referential cache — the caching headers inject `apple` into the files they describe, so
"zero occurrences" statements are scoped to document bodies below the header (L-7.2). This pass ran its
greps across the four `sources/ia_*` directories **and** the intake directory, then filtered header and
provenance carriers (`company_004_apple`, `PROVENANCE`, `Retrieved`, `archive.org`, `ia60`, `ia80`,
`https`, `_djvu.txt`) before reading survivors in context; the protocol and its reason are printed at
§Working method so an auditor can re-run it.

**Class discipline enforced in this file.** (1) No psychological trait appears anywhere; capability
statements are tied to a work product or are UNKNOWN. (2) No sentence says or implies that any founder was
destined, that the market was obviously huge, or that a 1976 choice was rational because of what happened
later. (3) The 1980–81 company is not read into 1976: the only 1981 sentences used are quoted with their
date and tagged `RETROSPECTIVE SOURCE`. (4) Absence claims are scoped to the evidence family —
"no occurrence in these files" — never to the world (§14 rule 6). (5) Repeated web restatements of memoir
are one lineage (§3). (6) Interpretive codas carry mechanism or say so (§7 coda rule): the readings
appended to B-07, B-16, B-29, B-14 and the narrative notes each name a mechanism or state UNKNOWN.

**What this dossier deliberately did not do.** It did not import a biography: no birth date, no college,
no employer, and no dollar figure appears here on the strength of a later book, and each appears as a
labelled claim with its carrier's date where it is quoted at all. It did not reconcile A's and A2's
registers beyond filing corrections. It did not mine any whole issue into the repository (the intake's own
compliance note: every issue layer is 60–130k words against a 60,000-word artifact cap, so extracts only).
It did not re-download anything already held.

---

## Outbound corrections

Corrections **from** this pass **to** sibling files. Not applied here — §14 rule 4; each owner applies it.

**OC-B1 → `A_chronology_feasibility.md`, founder-state rows and its "excluded" list.** A's probe predates
the name-census work: any sentence there implying that the periodical family supports a founder-state
narrative should carry A2-61a's calibration figure (four files for `Wozniak`, three for `Jobs`, one for
`Markkula`, none for `Wayne`). Confidence for the **1975 start edge** should read Low-Medium, since the
only carrier is Wozniak's single May 1977 clause and BYTE's 1975 issue, now retrieved, contains zero
Apple mentions (B-15).

**OC-B2 → `A2_periodical_archive_mine.md` §Founder state as evidenced in print.** Extend A2-56/A2-57 with
the intake month: BYTE September 1977 adds (i) a fifth dated occurrence of the corporate style
"Apple Computer Inc." in the company's own copy, (ii) the advertiser-index page pair "208 Apple 14, 15",
and (iii) the Atari trademark string in Apple's own advertisement, which strengthens A2-61c's negative by
showing the sole `Atari` occurrence is a disclaimer rather than a personnel reference (B-06, B-13).
**Do not** let (ii) be counted as an independent corroboration of the June 1977 price pair: same
advertiser, later month (B-16).

**OC-B3 → A2's §Provenance ledger / house note on Kilobaud (and `sources/_RETRIEVAL_LOG.md`).** The
intake corrects a scope error that matters to this dossier's biggest untried route: the house note "Kilobaud
1976 … no `_djvu.txt` text layer → scans only" holds for the three probed **1976** items but **Kilobaud
1977-onward does have a text layer** (`Kilobaud 1977-01_djvu.txt`, 746,892 B), and the layer filename
contains a space, so any `startswith(<identifier>)` layer test silently misses it (intake §B). Restate the
note with that scope; it converts DG-D7/BG-11 from "unOCRable" into "unworked".

**OC-B4 → `D_adversarial.md` E-06 and E-07 (garage rows).** E-06 already concedes the 1981 gloss is the
strongest Apple-linked garaging in the cache; this pass adds that B-22's genre line and BC-4's
address-of-record reading should be carried into the merge together, so the garage is neither asserted nor
"corrected away": premises UNKNOWN, business address documented, motif genre (B-12, B-21, B-22, BC-4).

**OC-B5 → `D_adversarial.md` §Contradictions D-11.** "10% best supported, 12% barred" is right, and the
register should also carry the harder point from BC-1: the corpus's silence about Wayne is a property of
the source class — the same corpus is silent about Markkula in 1976–80 — so Wayne's absence supports
"not publicly reported", not "not a partner".

**OC-B6 → any merge text for stage_1.md §B.** Barred as FACT unless a document is read: $666.66; 50 boards
at $500; July 1976; cash on delivery; $1,000 of personal capital; $15,000 loan; 12 days; $800; 10%/12% as
instrument text; Markkula's terms and arrival date; "employee #" numbering; Blue Box; Atari employment;
Reed/college status; the garage address; "founded April 1, 1976"; "first dealer" (D's R-3 list, adopted and
extended with the four founder-state fields from this file's §Data gaps). **This pass adds to that list:**
"Jobs wrote/programmed the software"; "Jobs was president of Apple"; "Wozniak designed the Apple II at HP";
the Atari employee number; and any sentence calling the 1976 role division documented.

**OC-B7 → `A2_periodical_archive_mine.md` A2-56 (and this file's B-02).** The sentence "it carries no age,
no employer, no school, no city and no role" is correct for the first four and **wrong for the fifth**: the
clause is the tail of Helmers' sentence classing all four men as "entrepeneurs" after a stated September 1976
conversation at WESCON in Los Angeles (B-31, BSS-01; BC-10). Restate as "no age, employer, school, city or
function — but a class designation, 'entrepeneurs', shared with three named peers". This raises Jobs's
reputation-at-the-time field from UNKNOWN to Medium-High and adds the corpus's only dated peer-group edge.

**OC-B8 → `A2_periodical_archive_mine.md` A2-59's closing emphasis.** "Neither Wozniak's May 1977 article
nor Apple's June 1977 advertisement attributes any function to Jobs" is true and should be kept, but A2's
adjacent framing ("The famous role division is absent from every 1976–77 text on disk") will be read by the
merge as "no act of his is witnessed". One act **is** witnessed, by a third party and collectively: Helmers'
"Steve Jobs, Steve Wozniak and I sat down and proceeded to use the Apple-ll BASIC … we had a working BASIC
language version" (`byte-1977-04.txt`:2744–2751; B-32, BC-9). Cross-reference the full paragraph, not the
four-word clause, so the merge bars both the strong claim and the too-weak one.

**OC-B9 → `A2_periodical_archive_mine.md` §Financial figures and A2-27.** A2 recorded the June 1977
advertisement's price ladder and the 6.5% tax rows. The same advertisement is also an **order form**, and its
payment terms are new to the register: BankAmericard / VISA / Master Charge accepted, "Cashier's check or
money order enclosed … allow 2 additional weeks for personal checks", free custom vinyl carrying case "(a
$50 value)", "we will also pay shipping charges to anywhere in the continental United States", separate
shipping-address field, and (July) RAM-chip upgrade prices of $125 and $600 per set (B-35, B-36, BSS-04).
Add as a §G/§K record: the company's own printed channel in 1977 is **direct mail order**, which is also the
cleanest available support for L-4's finding that no dealer relationship is documented.

**OC-B10 → `D_adversarial.md` DG-D3 / L-8 / W9 (the unread instrument).** The route should be re-pointed.
The lot page has now failed identically from two passes ("fetch failed", W10 reproducing D's W9), so
recommend **against** further attempts on it inside a fetch budget; instead target the public PDF copy at
`applefritter.com/files/Apple PartnerShip Agreement.pdf` (found by this pass, W3), which must be
**downloaded and text-extracted locally** — the WebFetch failure is a PDF-stream decoding limit (W5), not
evidence that the copy is unreadable. A Scribd copy and Reuters' 2025 photography item were returned by the
same search. Record retained as BSS-14 / BG-15; the instrument's status is unchanged (UNKNOWN until read).

**OC-B11 → `A2_periodical_archive_mine.md` §Provenance ledger / grep protocol.** A2's own §Working method
notes the header trap but its per-record grep scopes are not printed. This pass's counts are reproducible
only under the filter documented at §Provenance and method notes; add the filter to A2's method paragraph so
a re-run matches (this is the same defect class as D's L-7.2, in the opposite direction — an
under-specified positive rather than an under-specified negative).

**OC-B12 → `C_corporate_legal_org.md`.** Two dated items bear on the corporate-organ register and are not
periodical-derived: the "Apple Education Foundation" contact at 20863 Stevens Creek Blvd with telephone
(408) 255-3295 in BYTE December 1980 (B-39), and the absence of any officer title for either founder in
founding print (B-37). The first is a named entity at the founding address; the second means any officer
list for 1976–77 must be sourced from filings, not from print.

**OC-B13 → the fleet's `sources.csv` register.** Source IDs `BSS-01 … BSS-14` are opened by this dossier
(§CSV append rows) and must be appended, never renumbered; rows citing A2-registered documents reuse `A2S-nn`
IDs, because §13 makes `sources.csv` append-only per company.

---

## CSV append rows

Schemas copied verbatim from `company_001_amazon/*.csv` headers; every comma-bearing field is quoted;
`stage` = 1; dates ISO, partial where the record is partial (§13). These are **append rows only** — this
pass wrote no CSV file. **Source-ID convention:** `sources.csv` is append-only per company and existing IDs
(`A2S-nn`) are never redefined; this pass's new sources are registered as `BSS-nn`, and rows citing an
A2-registered document reuse the `A2S-nn` ID. **Register state observed by this pass:** Apple currently
holds four CSVs (`conflicts.csv`, `quantitative.csv`, `sources.csv`, `timeline.csv`) — `decisions.csv` and
`data_gaps.csv` do not yet exist for this company, so the `decisions.csv` rows below are the seed for a new
file and the §Data gaps table here should be converted to `data_gaps.csv` schema by whoever opens it (the
`follow_up_task` field is mandatory there for the High-importance rows BG-1…BG-8, BG-11, BG-14…BG-16).

### `decisions.csv`

```
company,stage,date,decision,state_before,information_available,unknowns,alternatives,constraints,rationale,expected_result,actual_result,source_id,confidence,claim_ref
```

```
Apple,1,1976-04,Operate as a named multi-person concern rather than as an unregistered hobby partnership (the agreement said to have been executed 1976-04-01),Two people building and delivering boards to whoever came; no printed document names a firm in 1975 or in the first months of 1976,That dealer pages and club letters were circulating the name APPLE by April 1976; that a machine existed and its designer was personally transporting it to clubs in another county,"Whether a firm was needed for trade credit, for liability, or only for a name to put on a dealer page - no document states the purpose",Remain unincorporated and unnamed; sell boards privately; attach to an existing distributor instead of forming a firm,"The instrument itself has never been read by this project; the 45/45/10 split, the signatories and the capital clause are auction prose",UNKNOWN: no document in this corpus states why a partnership was formed,A firm that could be dealt with by name by retailers and by the trade press,The style Apple Computer Co was in trade print by December 1976. RETROSPECTIVE framing of later outcomes is out of stage.,BSS-14,Low (the existence of the decision rests on an unread instrument),B-18; B-31; BC-1
Apple,1,1976-09/1976-11,Let retailers advertise the product before the maker advertised anything,BYTE's twelve 1976 issues carry zero maker copy; the brand name appears only inside other people's pages,East-Coast and Berkeley retailers were already naming the Apple-1 in their own brand lists; a manufacturer's list price existed that no cached file prints,"Whether the firm welcomed, tolerated or was unaware of the retailer advertising - nothing in the corpus records an internal decision",Advertise directly; sell only by hand as the designer later described; withhold stock from retailers,No documented authorized-dealer relationship of any kind in 1976 (D's L-4); no capital record exists,UNKNOWN: no internal document records the choice,Stock moved to buyers without advertising spend,"The product was named in New York print by September 1976 and offered by mail order in Berkeley by November 1976, with no founder named in either. RETROSPECTIVE: the maker's own advertising began only in June 1977.",BSS-01,Medium on the print sequence; UNKNOWN on the decision,B-07; B-14; BC-6
Apple,1,1976-11-20,Give a magazine editor a hands-on demonstration of an unreleased prototype,BYTE's editor had conversed with the firm's named principal at WESCON in September 1976 and had printed one clause about it,An editor with a national technical readership was present in Palo Alto that evening,"Whether the visit was arranged, opportunistic, or solicited; no document records who proposed it",Withhold the machine until it shipped; demonstrate only to dealers; decline press access,The editor was simultaneously a commercial party selling advertising space and buying design work,UNKNOWN: no document records who proposed the meeting or why,Print coverage by a technical editor who had handled the machine,"The prototype was demonstrated, a program was written on it that evening, and the editor promised next month's article. RETROSPECTIVE: the article appeared in April 1977 and the designer's own piece in May 1977.",BSS-02,Medium-High that it happened; UNKNOWN as to the decision behind it,B-09; B-31; B-32
Apple,1,1977-01-03,Incorporate in California,An unincorporated concern whose address of record was not yet published; the 1976-04-01 instrument (if executed) was still the only founding paper,"That a corporation was filed on 1977-01-03; nothing in the corpus states why, or who signed","Motive, signatories and the share structure at incorporation",Continue as a partnership; incorporate in another state; delay until outside money arrived,California fictitious-business-name and filing obligations; no printed reason appears in any retrieved document,UNKNOWN,A corporation able to issue stock,"Apple, incorporated in 1977, was reported as a public company in December 1980 print. Two lineage-free Tier-1 witnesses support the fact; none supports the motive.",BSS-04,High on the date; UNKNOWN on the decision's reasoning,B-26; BC-1
Apple,1,1977-04,Introduce the Apple II at the first West Coast Computer Faire rather than only through the club circuit,A machine in demonstration in November 1976; a magazine article commissioned for May 1977,"The Faire was billed for April 1977 with 200 commercial and homebrew exhibits and an expected 7,000 to 10,000 attendees; its organisers were the Homebrew newsletter's editor and the editor of Dr Dobb's Journal","Who decided on the Faire debut, and whether the company had a choice of venues",Debut in BYTE alone; debut at a dealer; skip the show,UNKNOWN who decided; the Faire's own flyer names no exhibitor,UNKNOWN: no internal document states the choice,A public introduction to a several-thousand-person buying audience,Apple was a billed exhibitor in December 1976 print and the introduction was reported afterwards. RETROSPECTIVE framing of the product's later reception is out of stage.,BSS-09,High that the debut was planned and billed; UNKNOWN as to who planned it,B-33; B-40
Apple,1,1977-06,"Take consumer orders directly by mail, on credit cards, with free shipping and a free carrying case",The maker had placed no advertisement of its own; distribution as described by the designer was word of mouth then retail,A nine-line price ladder and a working address and telephone; a $50-value case and continental freight could be absorbed; personal cheques needed three weeks to clear,Whether direct mail was a channel choice or a substitute for a dealer network that did not yet exist,Sell only through retailers; refuse cards; require cash instruments only,"The cash-flow constraint is inferred from the offer terms, not documented; no capital record exists",UNKNOWN: no document says who set the terms,Orders and payment arriving by post from anywhere in the continental United States,The company's own first advertising was simultaneously a mail-order catalogue. RETROSPECTIVE: the mechanism is visible only because the advertisement survives.,BSS-04,High that the terms were printed; UNKNOWN on the decision,B-35; B-36
```

### `timeline.csv`

```
company,stage,date_or_range,event,actors,location,source_id,evidence_class,confidence,conflict_ref,notes
```

```
Apple,1,1975-09,"BYTE's founding issue prints zero occurrences of Apple; the title that becomes the company's best witness does not yet know it","Carl Helmers (publisher), no Apple party named","Peterborough NH (magazine's own masthead); Apple location UNKNOWN","BSS-07","FACT (documented absence, one issue)",Medium,None,"New year from the 2026-09-25 intake. Scope limit: 1975-10/-11/-12 unread, so this is not a null on 1975."
Apple,1,1976-04-30,"A club letter reports that an APPLE 6502 system was its April guest and that Steve Wozniak provided transportation","Stephen Wozniak; Sonoma County Micro Computer Club","Cotati CA (L'OP Center), about 60 miles from the designer's own county","BSS-08","CONTEMPORARY OBSERVATION",Medium,U-A2-10 / L-3,"First dated in-window appearance of a founder's name. Sonoma County's letter, reprinted by Homebrew - NOT a Homebrew meeting record."
Apple,1,1976-06-09,"Homebrew's own CPU census counts 101 live systems among about 250 attendees, 18 of them 6502-based","Robert Reiling (editor), club members","San Francisco Bay Area; venue not printed in the cached item","A2S-10","CONTEMPORARY OBSERVATION (organiser self-report)",Medium-High,None,"Baseline for the population the founders' network addressed; 6502 share 17.8 per cent, second only to the 8080."
Apple,1,1976-09,"BYTE's editor converses with four microcomputer operators including Steven Jobs of Apple Computer Co on the WESCON show floor","Steven Jobs; Bob Marsh; Chris Rutkowsky; Paul Terrell; Carl Helmers","Los Angeles CA (WESCON)","BSS-01","CONTEMPORARY OBSERVATION",Medium-High,BC-1,"Printed 1976-12; the class noun Helmers uses for all four is 'entrepeneurs'. Only WESCON occurrence in the whole cached 1976 corpus."
Apple,1,1976-09,"Homebrew's Faire coverage lists Apple Computers among committing exhibitors and names the two organisers with titles and telephones","Jim Warren (General Chairperson); Bob Reiling (Operations Manager)","San Francisco Civic Auditorium (the Faire venue); Apple's own contact UNKNOWN","BSS-09","CONTEMPORARY OBSERVATION",High,None,"Documented intermediaries one step outside the company; no founder appears in the item."
Apple,1,1976-11-20,"Steve Wozniak and Steve Jobs bring a prototype Apple II to a Palo Alto motel room and program a demonstration with the editor","Stephen Wozniak; Steven Jobs; Carl Helmers","Motel room, Palo Alto CA","BSS-02","CONTEMPORARY OBSERVATION (single witness)",Medium-High,BC-9,"Strongest dated outside witness to both founders together with the machine; published 1977-04."
Apple,1,1976-12,"BYTE's December editorial prints 'Steven Jobs (Apple Computer Co)' - the only 1976 printed mention of either founder","Steven Jobs; Carl Helmers","Peterborough NH (publication); subject sighted in California","A2S-03","FACT",High,None,"Four words. No age, employer, school, city or function attached."
Apple,1,1977-05,"Wozniak publishes his description of the Apple II under the Cupertino address; the same issue attributes the BASIC interpreter to him and indexes him as author","Stephen Wozniak; BYTE editors","20863 Stevens Creek Blvd Bldg B3-C, Cupertino CA 95014","A2S-06","FOUNDER CLAIM (contemporaneous) + CONTEMPORARY OBSERVATION",High,None,"No customer, order, unit count or price figure named anywhere in his own text."
Apple,1,1977-06,"Apple's own BYTE advertisement runs as a direct-mail order form: nine price lines, 6.5 per cent California add-on, BankAmericard/VISA/Master Charge, free $50 case, seller-paid freight","Apple Computer Inc. (no person named)","20863 Stevens Creek Blvd B3-C, Cupertino CA 95014, telephone (408) 996-1010","A2S-07","FACT (as printed)",High,U-A2-6,"The only sales mechanism the company itself printed in 1977 that names no intermediary."
Apple,1,1977-09,"Apple buys a two-page front-of-book advertisement in BYTE under the corporate style, indexed at reader-service number 208 pages 14-15","Apple Computer Inc. (no person named)","Cupertino address and telephone as in June; advertisers' index in the same issue","BSS-07","FACT (as printed; OCR partial)",High,None,"New month from the 2026-09-25 intake. Same advertiser lineage as June - duration, not corroboration."
Apple,1,1977-11,"Creative Computing carries Apple as a brand in New York dealer advertisements; the issue contains no Apple review","Computer Mart (118 Madison Ave, New York); unnamed hobbyists","New York NY","BSS-10","CONTEMPORARY OBSERVATION",Medium,None,"New title for the project; three Apple occurrences in 100,162 words, all dealer or reader copy."
Apple,1,1980-12,"BYTE's December item gives Apple Education Foundation as the contact at the founding-era Stevens Creek address, with a different telephone","Apple Education Foundation; Bell and Howell, Mountain Computer, Heuristics, Integral Data Systems, Interactive Structures, ABW, Videx","20863 Stevens Creek Blvd, Cupertino CA 95014, (408) 255-3295","BSS-11","FACT (as printed)",High,None,"Out of window. Dated continuity of the address; must not be read back into 1976."
Apple,1,1981-02,"The only print carrying founder ages and holdings appears: Jobs 25 and Wozniak 30 as 'the creators', each holding 8.3 million shares; A C Markkula 32 credited with taking Apple 'from a garage operation'; Venrock 3.8 million shares; Xerox 80,000 shares","Steven Jobs; Stephen Wozniak; A C Markkula; Venrock Associates","unsigned column, BYTE February 1981","A2S-13","FACT as printed; RETROSPECTIVE SOURCE for Stage 1",High (printed) / Low (as 1976 evidence),BC-2 / U-A2-9,"The corpus's only ages, only Apple-linked garaging, and only cap table. Wayne appears nowhere in it."
```

### `sources.csv`

```
source_id,stage,claim_supported,source_title,author_or_publication,source_type,primary_or_secondary,event_date,publication_date,access_date,url,archived_url,tier,evidence_class,confidence,independence_note,relevant_passage,notes
```

```
BSS-01,1,"Jobs's dated peer network and his only 1976 class designation (B-31, network map, BC-1)","BYTE December 1976 editorial (WESCON conversations of September 1976)","Carl Helmers, BYTE Publications Inc","trade magazine, full-issue OCR text","primary","1976-09","1976-12","2026-09-26","https://archive.org/details/byte-magazine-1976-12","sources/ia_byte_1976/byte-1976-12.txt:1513-1519",1,CONTEMPORARY OBSERVATION,Medium-High,"same author and issue as A2S-03 (the 'Steven Jobs (Apple Computer Co)' clause) - one witness, counted once; independent of all company-side documents","Elements of this attitude of achievement were present in my conversations with entrepeneurs Bob Marsh (Processor Technology), Chris Rutkowsky (Technical Design Labs), Steven Jobs (Apple Computer Co) and Paul Terrell (Byte Shops) on the floor of the WESCON show last September in Los Angeles CA.","Read in context by this pass 2026-09-26. Extends A2-56/A2-15, which quoted only the four-word clause and therefore recorded 'no role'."
BSS-02,1,"The 1976-11-20 sighting and the only in-window technical act involving Jobs (B-09, B-11, B-32, B-33, BC-9)","A Nybble on the Apple (Notes by Carl Helmers), BYTE April 1977","Carl Helmers, BYTE","trade magazine, full-issue OCR text","primary","1976-11-20","1977-04","2026-09-26","https://archive.org/details/byte-magazine-1977-04","sources/ia_byte_1977/byte-1977-04.txt:2678-2770",1,CONTEMPORARY OBSERVATION (single witness with a commercial interest),Medium-High,"one witness for both founders; the April and May 1977 BYTE items are the same publisher, so they are duration not independence","That evening last November, Steve Jobs, Steve Wozniak and I sat down and proceeded to use the Apple-ll BASIC (which is a 5 K interpreter with 16 bit integer arithmetic) to program the Color Eater game.","Line numbers re-verified by this pass. OCR renders Apple-II as 'Apple-ll' and 'Apple-U'; Wozniak appears as 'Wozniac' at line 2688."
BSS-03,1,"Wozniak's design credit, the possessive BASIC attribution and his author index entry (B-33, B-34)","BYTE April and May 1977 - editor's credit, contents abstract, author index, technical text","BYTE Publications Inc","trade magazine, full-issue OCR text","primary","1977-04/05","1977-04/1977-05","2026-09-26","https://archive.org/details/byte-magazine-1977-05","sources/ia_byte_1977/byte-1977-05.txt:447, 763, 7662, 53956",1,CONTEMPORARY OBSERVATION,High,"same publisher as BSS-02 and A2S-06 - one editorial interest across two months","What does it take to make a computer system complete to the point of plugging it into the wall, plugging it into a color television, and turning it on? Stephen Wozniak of Apple Computer describes the design of such a system in his product description article on the Apple-II.","Plus index line '3 Wozniak: The Apple-ll' and the technical sentence 'Wozniak's Apple BASIC interpreter is a method of running the interpreter with a statement number trace'. Found by this pass's grep, not by A2."
BSS-04,1,"Apple's direct mail-order mechanism and its payment instruments (B-35, B-36)","Introducing Apple II - Apple Computer Inc. advertisement with order form, BYTE June and July 1977","Apple Computer Inc. (advertiser, no person named)","trade magazine advertisement, full-issue OCR text","primary","1977-06/07","1977-06/1977-07","2026-09-26","https://archive.org/details/byte-magazine-1977-07","sources/ia_byte_1977/byte-1977-06.txt:2012-2459; byte-1977-07.txt:3960-4130",1,FACT (as printed),High,"one advertiser's campaign across two months - a single lineage per A2's campaign rule","Please charge to my BankAmericard VISA Master Charge ... we will include free a custom vinyl carrying case (a $50 value). And we will also pay shipping charges to anywhere in the continental United States.","Order-form and payment-instrument detail is new to the project; A2 recorded the price ladder (A2S-07) but not the card set, the case offer or the cheque-hold period."
BSS-05,1,The absence of any officer title for either founder in founding print (B-37),"Negative census: president / vice-president / treasurer in Apple context, BYTE 1976-77 and Homebrew 1975-77",this pass,corpus census,primary (about the corpus),1975-11/1977-12,2026-09-26,2026-09-26,local corpus,"sources/ia_byte_1976, ia_byte_1977, ia_homebrew (header lines excluded)",1,FACT (documented absence within these files),High,derived from the same cached files as A2S-01..A2S-13; not an independent witness of the world,NO_VERBATIM_PASSAGE_RECORDED,"Zero hits. Scope stated per method: a family-scoped negative, not a disproof."
BSS-06,1,"Family-scoped negatives for Atari, Hewlett-Packard and college status (B-06, B-38, BG-1..BG-3)","Negative census: atari / hewlett / packard / reed / dropout / college, cached 1975-77 files",this pass,corpus census,primary (about the corpus),1971/1977-12,2026-09-26,2026-09-26,local corpus,"sources/ia_byte_1976, ia_byte_1977, ia_homebrew (header lines excluded)",1,FACT (documented absence within these files),High,confirms and extends A2S-13/A2-61c; the Atari coin-op advertising occurrences are additions by this pass,PONG is a trademark of Atari Inc.,"Atari appears in Apple's own advertisements (June and July 1977) and in unrelated third-party ATARI GAME BOARDS advertising; HP only as component, calculator and press matter; no education token at all."
BSS-07,1,"Apple's advertising at a new month in 1977 and the 1975 negative baseline (B-13, B-15)","BYTE September 1977 Apple II advertisement and advertiser index; BYTE September 1975 content test","periodicals intake agent (Internet Archive route)","bounded extract of full-issue OCR text","primary","1977-09 / 1975-09","1977-09 / 1975-09","2026-09-25","https://archive.org/details/byte-magazine-1977-09","00_universe/harvest/periodicals_intake/apple_microcomputer_sector/BYTE_1977-09_EXTRACT_apple2_ad_and_editorial.txt",1,FACT (as printed; OCR partial),High,"same advertiser as A2S-07 (June 1977) - corroboration of duration only; the Sept 1975 negative is a different issue and a new year for the project","208 Apple 14, 15","Reader-service index line; the extract's own header states the 'Apple' hit count (25) and the 1975 issue's count (0). Provenance header excluded from all greps per the documented trap."
BSS-08,1,"Wozniak personally transporting the machine to another county (B-29, BG-9)","Notes from the North - Sonoma County Micro Computer Club letter reprinted in Homebrew Computer Club newsletter","Robert Reiling (editor); Sonoma County club letter","club newsletter, full-item OCR text","primary","1976-04/1976-04-30","1976-04-30","2026-09-26","https://archive.org/details/hcc0204","sources/ia_homebrew/hcc0204.txt:131-144",1,CONTEMPORARY OBSERVATION,Medium,"independent of BYTE and of the company; single ~40-word letter","In April the APPLE 6502 system was our special guest. We are grateful to STEVE WOZNIAK for providing transportation.","Attribution corrected by D's L-3: this is the Sonoma club's letter inside the Homebrew newsletter, not a Homebrew meeting record."
BSS-09,1,"The documented intermediaries of the club-and-faire circuit (B-40, network map, BC-7)","Homebrew Computer Club newsletter Vol 2 No 9 - Faire exhibitor list and organiser block","Robert Reiling (editor), Homebrew Computer Club","club newsletter, full-item OCR text","primary","1976-09","1976-09","2026-09-26","https://archive.org/details/hcc0209","sources/ia_homebrew/hcc0209.txt:225-262, 747-750",1,CONTEMPORARY OBSERVATION,High,"independent of BYTE and of the company","Jim Warren, General Chairperson (Editor, Dr. Dobb's Journal & Vice-Chairman, Penninsula ACM Chapter) ... Bob Reiling, Operations Manager (Editor, Homebrew Computer Club Newsletter)","Same issue carries a reader's note using 'the Apple Computer' for a TV-monitor modification (line 748) - the earliest in-window evidence of a stranger operating the machine."
BSS-10,1,"Dealer-side distribution evidence from a new title (B-14)","Creative Computing v03 n06 (Nov/Dec 1977) - every Apple mention","Creative Computing (dealer advertisements and a reader's letter)","trade magazine, bounded extract of full-issue OCR text","primary","1977-11","1977-11","2026-09-25","https://archive.org/details/CreativeComputing_v03n06_NovDec1977","00_universe/harvest/periodicals_intake/apple_microcomputer_sector/CREATIVECOMPUTING_1977-11_EXTRACT_apple_mentions.txt",1,CONTEMPORARY OBSERVATION,Medium,"the 118 Madison Ave New York retailer family is the same concern behind A2's Computer Mart ladder - one retailer group, not two","Imsai, Processor Technology, Polymorphic, Cromenco, Apple and more","OCR noise acknowledged in the extract ('Cromenco'); the intake's caution is carried - three Apple hits in 100,162 words and no Apple review."
BSS-11,1,"Continuity of the founding-era address into 1980 (B-39)","BYTE December 1980 - Apple Education Foundation contact item","BYTE Publications Inc","trade magazine, full-issue OCR text","primary","1980-12","1980-12","2026-09-26","https://archive.org/details/byte-magazine-1980-12","sources/ia_byte_1981/byte-1980-12.txt:81631-81637",1,FACT (as printed),High,"independent of the February 1981 column's lineage? No - same publisher, different issue and month; treat as one magazine's continuing coverage","For more information, contact Apple Education Foundation, 20863 Stevens Creek Blvd, Cupertino CA 95014, (408) 255-3295.","Out of window for Stage 1; recorded because it dates the address, not the people."
BSS-12,1,"First dated carrier of the Jobs-at-Atari payroll legend (B-42, BC-3)","Steve Jobs, Atari Employee Number 40","Game Developer (gamedeveloper.com), business desk","trade web article","secondary","1974/1976 claimed","2011-10-06","2026-09-26","https://www.gamedeveloper.com/business/steve-jobs-atari-employee-number-40","UNANSWERED - fetch returned page shell only, no article body",2,RETROSPECTIVE INTERPRETATION (carrier date only established),Low,"independent of the iWoz lineage? Not established - the body was not readable, so its sourcing is unknown","Steve Jobs, Atari Employee Number 40","Headline and timestamp only. A 2020 stackexchange dispute over the number returned HTTP 403 (W7). Recorded as a dated carrier, never as evidence of employment."
BSS-13,1,First dated carrier found for the Wozniak-at-HP offer/refusal legend (B-43),Woz 'Begged' HP to Make the Apple PC,Business Insider,business web article,secondary,1970s claimed,2013-02-01,2026-09-26,https://www.businessinsider.com/woz-begged-hp-to-make-the-apple-pc-2013-2,not fetched (budget spent),3,"FOUNDER CLAIM (retrospective memory) - carrier dated, text unread",Low,part of the same retrospective interview cycle as the museum item returned by the same search; not independent of Wozniak's own telling,NO_VERBATIM_PASSAGE_RECORDED,Title and date recovered by search only (W2). Never to be printed as a dated employment fact.
BSS-14,1,"The route to the unread founding instrument (B-18, B-44, BC-1, BG-4, BG-5)","Apple Computer Company Partnership Agreement (public PDF copy) and the official Christie's lot page","Applefritter (file copy); Christie's New York","document copy / auction catalogue","primary (the document itself)",1976-04-01,"UNKNOWN (copy undated); lot campaign 2025-26","2026-09-26","https://www.applefritter.com/files/Apple%20PartnerShip%20Agreement.pdf ; https://www.christies.com/en/lot/lot-the-apple-computer-company-partnership-agreement-6570347/","UNANSWERED - PDF returned an undecoded compressed object stream (W5); Christie's returned 'fetch failed' (W10, reproducing D's W9)",1,UNKNOWN until read,UNKNOWN,"one document and one sale lineage; every secondary report of the 45/45/10 split is downstream of it","NO_VERBATIM_PASSAGE_RECORDED","This is the dossier's single highest-value open route. The failure is a tooling limit, not an absence: the next pass should download the bytes and extract text locally."
```

### `conflicts.csv`

```
company,stage,conflict_id,section,claim_a,claim_a_source,claim_a_date,claim_b,claim_b_source,claim_b_date,why_they_differ,evidence_weight,best_supported_interpretation,residual_uncertainty,confidence
```

```
Apple,1,BC-1,B / N / U-A2-10,"The 1976-04-01 partnership agreement had three signatories including Ronald G Wayne, with a 45/45/10 allocation","auction and collector-registry coverage of the instrument (Christie's/RR/provenance in D's L-8 and BSS-14)","2025-26 (sale campaign) and 2018 (registry)","Wayne appears in zero documents in the cached 1976-1981 corpus and Markkula in exactly one sentence, so the printed origin story is a two-founder story","D's E-04 and H-9 grep; this file's B-01 and B-17 name census","2026-09-24/26","One side is a physical instrument nobody in this project has read; the other is a press class that did not report persons at all - its silence is a property of the source, not of the men","The document class outranks print for the fact of a third signatory; the print class is decisive for what was publicly knowable in 1976","Print both: a three-signatory instrument of reported date exists and remains unread, and the founding-era public record named two people. Never 'three founders' as a 1976 fact.","Names, percentages, signing place and withdrawal terms - all rest on the unread paper","High on the printed record / Low on the instrument reading"
Apple,1,BC-2,B / Q,"The founders were 21 and 25 at the partnership, as widely printed","derived backward from the only ages in the corpus","1981-02","The only ages available anywhere in this evidence family are BYTE February 1981's 25, 30 and 32, and any Stage-1 age is an arithmetic projection from an integer","A2-60 and this file's B-04 (line re-verified at byte-1981-02.txt:48509)","1981-02","Derived versus observed: a later document is being quoted as though it were a period one","The 1981 sentence is Tier 1 for 1981 and RETROSPECTIVE SOURCE for 1976","State the ages as printed in 1981; any Stage-1 age carries a plus-or-minus one year band and a derivation label","Birth dates - the corpus carries none","High as printed / Low for the window"
Apple,1,BC-3,B / K,"Jobs was the salesman and Wozniak the designer, the standard division of labour","retrospective testimony and inference from the later company","post-1981 retelling","No 1976-77 text attributes any function to Jobs; the only design credit is Wozniak's, and it is printed by an outside editor","A2-59 and this file's B-08, B-31, B-33, B-34","1976-12 / 1977-04 / 1977-05","The division is reconstructed from later speech, while the period class of document (trade print, club letters, dealer ads) had no reason to record roles","Wozniak's design credit is contemporaneous and outside; Jobs's selling role has no contemporaneous witness","The designer side is documented; the salesman side is UNKNOWN for the window and must be labelled by the vintage of whatever carries it. 'Entrepeneurs' in Dec 1976 is a class, not a function","Whether any 1976 document naming a Jobs act exists outside this family - a signed order, a dealer letter, a cheque endorsement","High (the asymmetry is documented)"
Apple,1,BC-4,B / G,"Apple was born in the garage at 20211 Crist Drive, Los Altos","the memoir tradition and the universe register's place gloss","post-1977 retelling","The company's only 1976-77 published address is Cupertino 20863 Stevens Creek Blvd Bldg B3-C, and the only Apple-linked garaging in the cache is a February 1981 editorial gloss","A2S-06/A2S-07 bylines and advertisements; BSS-04; A2S-13 (1981 column); D's L-5 genre line","1977-05/06 and 1981-02","A residence or work-at-home claim and a business address of record are different propositions, and periodicals print only the latter","Property and lease records outrank both classes and neither has been reached (DG-D5); the 1976 'two people in a garage' phrase about Sphere shows the motif was genre","Print the documented 1977 office-park premises, keep the garage as a 1981 characterisation plus memoir, and hold premises UNKNOWN - neither asserted nor corrected away","Whether any work occurred at a private residence in 1976 and where","High on the address of record / UNKNOWN on the garage"
Apple,1,BC-5,B / K,"Founding capital came from personal asset sales: $500 from an HP-65 and $750 from a VW bus","iWoz (2006), carried by the collector registry","2006","A founding partner later understood that a $15,000 loan filled the first order","Wayne's 2022 written account via D's E-14","2022","Two retrospective participant tellings describing different mechanisms and incompatible totals, neither contemporaneous","Neither is documentary; the Cramer Electronics credit mechanism is period-plausible because Cramer advertises in these same pages, which is mechanism not evidence","Carry founder-contributed capital as UNKNOWN with the three tellings recorded as a lineage table; print no dollar figure","Everything: amounts, instruments, dates, collateral","High that it is unresolved"
Apple,1,BC-6,B / F,"Terrell's Byte Shop was the founding customer and Apple ran a dealer network","retrospective merchant and founder tellings","2021-2026 carriers","No 1976 document evidences an authorized Apple dealer relationship of any kind, the Byte Shop's own 1976 advertising never mentions Apple, and the maker's only printed 1977 sales mechanism is a direct mail-order form","D's L-1 and L-4; BSS-04; this file's B-14, B-35","1976-09 to 1977-09","Scene-building from later conversation versus an OCR brand list and an order form","The dated advertisements and the company's own order form control","Print the retailer ladder and the direct-mail mechanism; bar 'first store', 'first dealer' and 'dealer network' for 1976","An invoice, purchase order or Terrell statement dated in-window would change this","High on the print facts"
Apple,1,BC-7,B / L,"Wozniak's own print says distribution ran by word of mouth through California and only later nationwide through retail stores","A2S-06 (BYTE May 1977)","1977-05","The corpus puts the first named product advertisement in New York in September 1976, Berkeley mail order in November 1976, and the maker's own advertising only from June 1977","A2S-04/A2S-05 dealer ladder; D's L-10; BSS-10","1976-09 to 1977-11","A compressed retrospective ordering versus a publication ladder","The ladder is dated and multiparty; the sentence is one interested author's summary","Cite the sentence as FOUNDER CLAIM (contemporaneous) for channel type and build sequence from dated advertisements","Whether California unit sales preceded New York's advertisement","High"
Apple,1,BC-8,B / P,"The February 1981 column's ages, holdings and revenue series are reliable company history","A2S-13 (BYTE February 1981)","1981-02","The column is unsigned and company-sourced, mixes dollar-exact with rounded figures internally, and its offering arithmetic does not close","U-A2-7, U-A2-8, U-A2-9; this file's B-25","1981-02","A company-supplied public-relations series is being read as audited data","Tier 1 for what was printed; nothing at all for what was audited","Use for the 1981 state and for ages and holdings as printed, never as Stage-1 measurement","The 1980 prospectus remains unread (AP-02, AP-21)","High on printed content / Low on provenance"
Apple,1,BC-9,B / J,"Helmers' own sentence includes Jobs in a first-person-plural programming session on 1976-11-20, so a technical act of his was witnessed","BSS-02, byte-1977-04.txt:2744-2751","1977-04","A2-59 and this file's B-08 hold that print attributes no function to Jobs in 1976-77","A2-59; Wozniak's May 1977 article; Apple's June 1977 advertisement","1977-05 / 1977-06","The two statements are about different objects: B-08 is about the company's own documents, which name no function; B-32 is a third party's 'we', which is not a function attribution but is not nothing either","B-08 holds for every company-side text; B-32 holds only as one interested witness's collective pronoun","Keep both, precisely: no document attributes a design, a code contribution or a written work product to Jobs, and the sole collective pronoun placing him at a keyboard is Helmers' 'we', from a single commercially interested witness, published five months later. Neither 'Jobs programmed it' nor 'Jobs never touched the machine' is supported","What Jobs actually did that evening is unrecoverable from this witness","High that the tension exists / Low on its resolution"
Apple,1,BC-10,B / J,"A2-56 records that the December 1976 Jobs mention carries no role","A2-56, quoting the four-word clause 'Steven Jobs (Apple Computer Co)'","2026-09-24","The sentence containing that clause classes him: 'my conversations with entrepeneurs ... Steven Jobs (Apple Computer Co) ... on the floor of the WESCON show last September in Los Angeles CA'","BSS-01, byte-1976-12.txt:1513-1519, re-read in context by this pass","1976-12","A quotation-boundary error: the fragment was quoted without the governing noun of the full sentence","Same document; the fuller quotation simply carries more of it","Correct A2-56 for 'role' only: an outside editor assigned a class (entrepreneur) among four named peers, with a place and month. A class is not a function, so B-08 stands for acts","Whether Helmers's word reflects first-hand impression of Jobs's role or a courtesy category for four exhibitors","High, resolvable on the page"
```
