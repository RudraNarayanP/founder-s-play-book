# APPLE STAGE 1 — DOSSIER A2: PERIODICAL-ARCHIVE MINE

Dataset: THE FOUNDER'S PLAYBOOK — forensic reconstruction of early company state.
Company: **Apple** (`company_004`), Fortune-50 universe rank #4.
Stage: **1 — origin → first real-world test**, span **1975 → 1977-01-03** (the span fixed by
`A_chronology_feasibility.md`; the corpus mined here runs to **1981-02** because the stage's
financial interior is only visible from the far side, and every such post-1977 import is
labelled).
Dossier type: **local-corpus mining pass, no web budget spent as of this section.**
Governing spec: `00_METHOD_AND_STYLE.md` §2 (hindsight firewall + record-selection null),
§3 (claim classes, confidence, independence and filing-lineage rules), §5 (tiers), §6 (time
audit), §7 (line formats), §13 (CSV schemas), §14 (retrieval discipline, rules 1–6).

**Hindsight-firewall statement for this dossier.** Nothing recovered here is used as evidence
that 1975–77 choices were correct. The Apple II's later sales, the 1980 IPO and the company's
survival are admitted only as *contemporaneously printed figures with their own dates*, never
as validation of the Apple-1, of the partnership, of the dealer channel, or of a price. Where a
1981 sentence is the only carrier of a 1976–77 fact, it is tagged `RETROSPECTIVE SOURCE` and
the class is capped accordingly. The record-selection null is asserted in §Data gaps and
§Evidence-family verdict: the interior of 1976 (what was considered, what was refused, what was
ordered, what was paid) is unrecoverable because the surviving archive for Apple's first year is
a *third-party hobby magazine plus a club newsletter* — kept by Carl Helmers' BYTE and by Homebrew's
editor Robert Reiling, not by the company — and because the winners' kept documents (Christie's
1976-04-01 agreement) are a *single* artifact, not a file.

**Confidence scale (§3).** High = 2+ independent origins or a primary document · Medium = one
reliable source · Low = conflicting, vague, or retrospective-only · UNKNOWN = no evidence recovered.

**Record class vocabulary (§3).** FACT / FOUNDER CLAIM (sub-tagged *contemporaneous* vs
*retrospective memory*) / CONTEMPORARY OBSERVATION / RETROSPECTIVE INTERPRETATION / INFERENCE /
ESTIMATE / DERIVED / UNKNOWN.

---

## Working method

**What was mined.** The protected local archive `company_004_apple/sources/` (read-only; nothing
in it was created, deleted, moved, renamed or tidied by this pass), specifically:

| Corpus | Files on disk | Format | Extent |
|---|---|---|---|
| `ia_byte_1976/` | `byte-1976-01.txt` … `byte-1976-12.txt` | raw IA OCR text (`*_djvu.txt`), 360–596 KB each | BYTE, Jan–Dec 1976, all 12 issues, ~5.7 MB |
| `ia_byte_1977/` | `byte-1977-04/05/06/07.txt` | same | BYTE, Apr–Jul 1977 (Vol 2 No 4 – No 7), 682–797 KB each |
| `ia_byte_1981/` | `byte-1980-12.txt`, `byte-1981-02.txt` | same | BYTE, Dec 1980 and Feb 1981, 1.6–1.67 MB each |
| `ia_homebrew/` | `hcc0109, hcc0110, hcc0201–0207, hcc0209, hcc0211, hcc0213, hcccf` | same | Homebrew Computer Club newsletters, 1975-11-30 → 1977-01-19 plus the 1977-02-16 West Coast Computer Faire flyer |
| `apple1registry_stories.txt` | 1 file, 49 KB | HTML stripped to text | Retrospective (2022) curation of 1973/1976 artifacts — used only in §Terminated, §Contradictions, §Provenance |

**Method, in order.** (1) Occurrence census per file, header lines excluded (see the trap
recorded at A2-01/A2-05 — the probe's own provenance header contains the string `apple`, so a
naive grep of these files over-counts, and the feasibility probe's Homebrew null must be read
with that in mind). (2) Verbatim window extraction (±6 lines) around every `apple`,
`Byte Shop`, `dealer`, `Wozniak`, `Jobs`, `Wayne`, `Markkula`, `West Coast Computer Faire`,
`WESCON`, price and revenue tokens. (3) Masthead self-dating of every issue cited, plus the
`_RETRIEVAL_LOG.md` dating route for 1976 issues whose masthead OCR is garbled. (4) Ad-block
reassembly: this corpus is OCR of a printed page, so an advertisement arrives as interleaved
line fragments; a record quotes only the lines that are unambiguous, and OCR-level doubt is
carried in the record rather than silently normalised. (5) Arithmetic shown in-file for every
ESTIMATE/DERIVED number, per §3 and §13 (`derived_arithmetic`).

**Independence discipline applied here.** BYTE's editorial matter (Helmers), BYTE's letters
column and BYTE's *advertisements* are three different origins, but the dealer advertisements
that repeat across months are **one advertiser's campaign, not multiple corroborations**; this
dossier counts a run of the same ad as one source with a duration, and says so in every
corroboration cell. Similarly Wozniak's May 1977 article and Apple's June 1977 advertisement are
both *company-side* documents: two documents, one interest. They are never counted as
"independent" of each other.

**Budget.** Web requests spent by this pass: **0 of 3 permitted.** Every record below is from a
file already on disk. Gaps are recorded UNTRIED with the exact query rather than searched
(§14); the three-request ceiling is reserved and currently untouched.

---

## Findings

Records are `A2-nn`, dated or documented as nulls, grouped by the year of the **event** where
the event date is separable from the **publication** date. Format per §7 claim-record line.

### 1976 — the year the trade press is empty of Apple, then not

A2-01 Claim: The earliest `apple` token anywhere in BYTE 1976 is **not the company** — the
February 1976 issue's hobby-group column carries a item headlined "Micro Fun in the Big Apple"
reporting Robert Schwartz and the New York City Micro Hobbyist Group's second meeting at
LaGuardia Community College — Date: 1976-02 (publication) — Source: BYTE, February 1976, hobby
column (line ~11667) — Source date: February 1976 — URL: https://archive.org/details/byte-magazine-1976-02
— Archived: `sources/ia_byte_1976/byte-1976-02.txt` — Tier: 1 — Class: FACT (documented reading;
a lexical null, not evidence about Apple) — Passage: "Micro Fun in the Big Apple / Robert Schwartz
sent BYTE a short note that the New York City Micro Hobbyist Group had its second meeting Friday
December 12 at LaGuardia Community College in Long Island City, Queens." — Conf: High —
Corroboration: n/a (negative finding) — Conflicts: None. Methodological: any count of "Apple
mentions in BYTE 1976" that does not read each hit is wrong; see A2-02…A2-05.

A2-02 Claim: BYTE June 1976 contains three `apple` occurrences and **all three are unrelated to
the company** — an addressing-tutorial article uses a fictional "Apple Valley" apartment complex
— Date: 1976-06 — Source: BYTE, June 1976, machine-independent-addressing article (lines ~15970,
~16147) — Source date: June 1976 — URL: https://archive.org/details/byte-magazine-1976-06 —
Archived: `sources/ia_byte_1976/byte-1976-06.txt` — Tier: 1 — Class: FACT (documented reading) —
Passage: "Imagine that you are writing a book on atomic physics and that Dr J Smith is to be a
consultant. He currently lives in a small apartment complex called Apple Valley at 15 Grove St." —
Conf: High — Corroboration: n/a — Conflicts: None. Consequence: **BYTE June 1976 has zero
references to Apple Computer**, which bounds how early the maker's name entered the title.

A2-03 Claim: BYTE July 1976's `apple` hits are the editors' own election-year phrase ("motherhood,
apple pie, computer power for the people") — Date: 1976-07 — Source: BYTE, July 1976, "BYTE's
election year stand" (lines ~31979, ~32013, ~32024) — Source date: July 1976 — URL:
https://archive.org/details/byte-magazine-1976-07 — Archived: `sources/ia_byte_1976/byte-1976-07.txt`
— Tier: 1 — Class: FACT (documented reading) — Passage: "BYTE's election year stand on motherhood,
apple pie, computer power for the people, and state of the art components for hobbyists." — Conf:
High — Corroboration: n/a — Conflicts: None.

A2-04 Claim: BYTE September 1976's four non-company `apple` hits are all in the software-piracy
editorial ("a few bad apples"), i.e. the magazine's own September editorial vocabulary contains
the company name only in one place, and that place is the *advertisement* (A2-08) — Date:
1976-09 — Source: BYTE, September 1976, editorial on software protection (lines ~2031, ~2093,
~2996, ~3042) — Source date: September 1976 — URL: https://archive.org/details/byte-magazine-1976-09
— Archived: `sources/ia_byte_1976/byte-1976-09.txt` — Tier: 1 — Class: FACT (documented reading) —
Passage: "You undoubtedly know that a few bad apples are rapidly giving all computer hobbyists a
very bad name." — Conf: High — Corroboration: n/a — Conflicts: None.

A2-05 Claim: **Method defect found in the cached corpus itself, and it invalidates a naive
re-run of the probe's Homebrew null:** every file in `sources/ia_homebrew/` opens with a
four-line provenance header prepended by the feasibility probe, whose text contains
`company_004_apple`. Consequently each of `hcc0109`(1975-11-30), `hcc0110`(1975-12-31),
`hcc0201`(1976-01-31), `hcc0203`(1976-03-31), `hcc0205`(1976-05), `hcc0206`(1976-06-09),
`hcc0207`(1976-08-04), `hcc0211`(1976-12-10), `hcc0213`(1977-01-19) and `hcccf` returns exactly
one `apple` match, and that match is line 2 of the header — not newsletter text — Date:
1975-11 → 1977-02 (documents) — Source: line-scoped grep of the ten files — Source date:
retrieved 2026-09-24, re-read by this pass 2026-09-24 — URL: local files — Archived:
`sources/ia_homebrew/` — Tier: n/a (provenance) — Class: FACT (documented reading) — Passage:
"# ACCESS DATE: 2026-09-24 | Level-3 chronology/feasibility probe, company_004_apple" — Conf:
High — Corroboration: 10 files — Conflicts: None. **This is why AP-26's null is confirmed here
rather than merely repeated: with header lines excluded, the club's newsletters for 1975-11-30,
1975-12-31, 1976-01-31 and 1976-03-31 have zero body occurrences of "apple".**

A2-06 Claim: **One correction to AP-26.** The Homebrew newsletter of **1976-02-29** (`hcc0202`) is
not literally free of the string: its book-review matter uses the idiom "polishes off the apple"
about a microprocessor-selection book — Date: 1976-02-29 (document) — Source: Homebrew Computer
Club Newsletter Vol 2 No 2, review item (line ~334) — Source date: 1976-02-29 — URL:
https://archive.org/details/hcc0202 — Archived: `sources/ia_homebrew/hcc0202.txt` — Tier: 1 —
Class: FACT (documented reading) — Passage: "Each chip covered has a summary of its instruction
set - Intel could do well in using the one for the 8080, it is the best one around for it.
Chapter 8 polishes off the apple with some guidelines to follow when selecting a micro-compressor
chip." — Conf: High — Corroboration: 1 — Conflicts: None. Substance unchanged: **no Apple
reference exists in the club's print before April 1976**, so AP-26's conclusion stands and its
literal wording ("zero occurrences of 'apple'") does not.

A2-07 Claim: The **Byte Shop was already an established retail display channel in BYTE
advertisements from April 1976 onward — five months before any Apple-1 advertisement** — a
vendor advertising from P.O. Box 9160, Stockton CA repeatedly offers goods "ON DISPLAY AT BYTE
SHOP, MOUNTAIN VIEW CA", and by June–July the same line reads "MT VIEW CA" alongside "MARSH DATA
SYSTEMS, TAMPA FL" — Date: 1976-04 → 1976-07 — Source: BYTE, April, May, June and July 1976,
vendor advertisements (lines ~15464, ~13648, ~15118, ~29876) — Source date: 1976-04 … 1976-07 —
URL: https://archive.org/details/byte-magazine-1976-04 … -07 — Archived: `sources/ia_byte_1976/` —
Tier: 1 (primary advertising artifacts) — Class: FACT (the advertisements exist and read thus) —
Passage: "ON DISPLAY AT / BYTE SHOP / MOUNTAIN VIEW CA" — Conf: High — Corroboration: 4 issues,
**one campaign: counted as one source with a duration, not four** — Conflicts: None. Channel
significance: when the Apple-1 first appears in print (A2-08) it enters a retail circuit the
magazine had already been advertising into for three months.

A2-08 Claim: **The earliest Apple-1 retail advertisement recovered in this corpus runs one month
earlier than the probe recorded — BYTE September 1976, not October — and it is placed by a New
York City retailer, not a Bay Area one**: the Computer Mart of New York advertisement at 314
Fifth Avenue offers to let customers "Take a byte out of the new Apple-1 computer", while
declaring itself an *authorized dealer for Sphere, IMSAI, Processor Technology and SWTPC 6800 &
CT 1024* — Date: 1976-09 (advertisement) — Source: BYTE, September 1976, advertisement "Computer
Mart of New York / 314 Fifth Avenue, New York NY 10001, 212 279-1048" (lines ~25269–25285) —
Source date: September 1976 — URL: https://archive.org/details/byte-magazine-1976-09 — Archived:
`sources/ia_byte_1976/byte-1976-09.txt` — Tier: 1 (primary advertising artifact) — Class: FACT
(as to the advertisement's existence and contents) — Passage: "Authorized dealer for: Sphere •
IMSAI / Processor Technology / SWTPC 6800 & CT 1024 / Featuring the best in microcomputers and
books. Competitive prices on systems. **Take a byte out of the new Apple-1 computer.** / Friendly
Service Advice / Problem Solving / Open Monday through Saturday 10-6, Thursday until 9:30 / 314
Fifth Avenue New York NY 10001 212 279-1048" — Conf: High (that the ad ran in the September
issue), Medium (that "new Apple-1" means board-in-stock rather than announced-only) —
Corroboration: 2 independent (A2-11 October and A2-17 December re-runs by the same retailer are
*not* counted; the second independent origin is A2-12, a different advertiser) — Conflicts: None,
but see §Outbound corrections C-1 (AP-14's "earliest October 1976").

A2-09 Claim: The September 1976 issue also prints, on its front matter, an **advertiser/distributor
list that is the fullest single-page map of the American computer-store circuit recovered so far in
1976**, and it names the Byte Shop's two opening stores with street addresses and telephone —
Date: 1976-09 — Source: BYTE, September 1976, distributor list (lines ~131–159) — Source date:
September 1976 — URL: https://archive.org/details/byte-magazine-1976-09 — Archived:
`sources/ia_byte_1976/byte-1976-09.txt` — Tier: 1 — Class: FACT — Passage: "Computer Mart of New
York, Inc. 314 Fifth, New York, N.Y. 10001 (212) 279-1048 / The Byte Shop Computer Store #1, 1063
El Camino Real, Mountain View, Calif. 94040, (415) 969-5464 / The Byte Shop Computer Store #2,
3400 El Camino Real, Santa Clara, Calif. 95051, (408) 249-4221 / A-VID Electronics Co., 1655 E.
28th Street, Long Beach, Calif. 90806 / Computer Warehouse Store, 584 Commonwealth Ave., Boston,
Massaschusetts 02215 (617) 261-1100" — Conf: High — Corroboration: A2-13 (November list) and
A2-07 (April–July "on display at" ads) are different documents but partly the same commercial
interest; independence note recorded. Conflicts: None. **The identity of the Apple-1's first
*named* East Coast seller is therefore fixed: Computer Mart of New York, Inc., 314 Fifth Avenue,
at the same time as the same retailer was declaring itself an authorized dealer for four other
microcomputer lines — i.e. Apple was one brand in a multi-line store, not a dedicated channel.**

A2-10 Claim: BYTE's October 1976 editorial records that **general press had already covered the
retail side of this market five months earlier: the July 12, 1976 issue of Business Week
"featured Paul Terrell's Byte Shop computer store in Mountain View CA"**, and that the store was
"one of the largest retail outlets among the more than 250 stores coast to coast which regularly
stock BYTE" — Date: 1976-07-12 (Business Week article, as reported); 1976-10 (BYTE publication) —
Source: BYTE, October 1976, editorial (lines ~1202–1212) — Source date: October 1976 — URL:
https://archive.org/details/byte-magazine-1976-10 — Archived: `sources/ia_byte_1976/byte-1976-10.txt`
— Tier: 1 (contemporaneous report of a contemporaneous publication) — Class: CONTEMPORARY
OBSERVATION (of the press landscape); the Business Week content itself is UNKNOWN — Passage: "An
article in the July 12 issue of Business Week featured Paul Terrell's Byte Shop computer store in
Mountain View CA. Paul's shop is one of the largest retail outlets among the more than 250 stores
coast to coast which regularly stock BYTE." — Conf: High (that BYTE reported it), UNKNOWN (what
Business Week said; no Apple reference in it is established) — Corroboration: 1 — Conflicts: None.
**Route value: this is a dated, named target for the "general press" family the probe recorded as
NOT FOUND (AP-37). It is recorded here as a dated pointer, and the retrieval itself is UNTRIED —
see §Data gaps DG-11.**

A2-11 Claim: The retailer's **October 1976** advertisement — the one the probe cited as the
earliest Apple retail trace and labelled "Computer Fan" — is the same New York City chain
(314 Fifth Avenue) now advertising a second, Long Island address, with Apple listed inside a
brand block of eleven competing microcomputer makers — Date: 1976-10 — Source: BYTE, October
1976, advertisement (lines ~40835–40855) — Source date: October 1976 — URL:
https://archive.org/details/byte-magazine-1976-10 — Archived: `sources/ia_byte_1976/byte-1976-10.txt`
— Tier: 1 — Class: FACT (advertisement exists) — Passage: "IMSAI, SWTPCo, Digital Group /
Processor Tech, **Apple**, OSI / TDL-Z-80, Seals, Cromemco, / Sphere, Tarbell, Oliver / Magazines,
books, chips, sockets, connectors, terminals. / IT'S ALL HERE WAITING FOR YOU / FRIENDLY ADVICE
TOO / New York City 314 5th Ave (32nd St) / Long Island 2072 Front St East Meadow NY" — Conf:
High — Corroboration: same advertiser as A2-08 (one campaign) — Conflicts: **store-name
attribution.** The masthead line of this advertisement OCRs as "L^omputer re fan … ¥ jaw UJom
^rnc."; the probe read "Computer Fan". The address, phone and "a few … Inc." line-up match the
September page (A2-08, A2-09) for Computer Mart of New York, so the surviving text does not
support "Computer Fan" as a distinct store name. See §Outbound corrections C-1.

A2-12 Claim: The Berkeley mail-order advertisement of November 1976 that lists the Apple-1 among
*starred* mail-order lines is placed **beside, and in the company of, the Byte Shop's own store
addresses**, and its starred-item discount formula is printed in full — Date: 1976-11 — Source:
BYTE, November 1976, advertisement block (lines ~20015–20060 and ~20430–20485) — Source date:
November 1976 — URL: https://archive.org/details/byte-magazine-1976-11 — Archived:
`sources/ia_byte_1976/byte-1976-11.txt` — Tier: 1 — Class: FACT (advertisement exists) —
Passage: "A new retail computer store in Berkeley, California. We sell and service small computers for
personal, educational, and business use, both in kit and assembled form. Many items are at substantial
discounts from manufacturer's list prices. … \*IMSAI-Computers, memory, interfaces & peripherals /
Processor Technology-Memory, interfaces & software / Lear Seigler-ADM3 Terminal kit / Polymorphic
Systems … / \*Cromemco-TV Dazzler, Bytesaver and A/D-D/A / **\*Apple-Apple-1 computer** / Morrow's Micro
Stuff-Cassette interface / Oliver Audio Engineering-Paper tape reader / \*Starred items available by
mail order at 10% discount from manufacturer's current list prices. For prompt delivery, send money
order or cashiers check plus 2% shipping & handling. Personal checks require 3 weeks processing. Calif,
res. add sales tax. **Minimum order $80.00.** / KENTUCKY FRIED COMPUTERS 2465 FOURTH STREET BERKELEY,
CA 94710 TELEPHONE: (415)549-0858 / **A COMPUTER IN EVERY POT**" —
Conf: High (contents), Medium (that OCR "Apple-Apple-1" reproduces the printed line exactly) —
Corroboration: independent of A2-08/A2-11 (different advertiser) — Conflicts: None. The same issue's
advertiser index carries "Kentucky Fried Computers 75", fixing the page. Three facts worth holding: an
Apple-1 **retail list price existed and was published by October–November 1976** (the discount formula
is meaningless otherwise); the hobby mail-order terms of trade were 10% off list plus 2% carriage, three
weeks on personal cheques, an $80 minimum order, and a *stated but unquantified* "Calif, res. add sales
tax" — the quantity comes instead from the club's June 1976 notice (A2-39: 6%); and the ad's own
headline "A new retail computer store" is contradicted, six months earlier, by the same firm's
statement that it had no store yet (A2-39) — which is the shape of this channel in 1976.

A2-13 Claim: By **November 1976 print the Byte Shop was a five-to-six-store Bay Area chain with
published addresses**, in a dealer/distributor list that also locates its Berkeley competitor —
Date: 1976-11 — Source: BYTE, November 1976, regional distributor list (lines ~20015–20046) —
Source date: November 1976 — URL: https://archive.org/details/byte-magazine-1976-11 — Archived:
`sources/ia_byte_1976/byte-1976-11.txt` — Tier: 1 — Class: FACT — Passage: "Applied Computer
Technology 2465 Fourth Street, Berkeley, CA 94610 / The Byte Shop 1514 University Ave., Berkeley,
CA 94703 / The Byte Shop 2559 South Bascom Ave., Campbell, CA 95008 / The Byte Shop 2227 El Camino
Real, Palo Alto, CA 94306 / The Byte Shop 509 Francisco Blvd., San Rafael, CA 94901 / The Byte
Shop 2989 North Main St., Walnut Creek, CA 94596" — Conf: High — Corroboration: 2 (A2-09 September
lists stores #1 and #2 with the same Mountain View / Santa Clara addresses; A2-07 April–July ads
route goods to the Mountain View shop) — Conflicts: None. Note the Palo Alto shop: the same
November issue carries Helmers' memory of Jobs and Wozniak stopping in a **Palo Alto motel room**
on 1976-11-20 (AP-15), so the geography of the first resellers and the founders coincide.

A2-14 Claim: A November 1976 BYTE technical article treats "the new Apple computer" as an
already-marketed machine built on a PROM-monitor architecture, naming it beside STM Systems' BABY
— Date: 1976-11 — Source: BYTE, November 1976, firmware/PROM-monitor article (line ~20836) —
Source date: November 1976 — URL: https://archive.org/details/byte-magazine-1976-11 — Archived:
`sources/ia_byte_1976/byte-1976-11.txt` — Tier: 1 — Class: CONTEMPORARY OBSERVATION (technical
characterisation by a third party) — Passage: "Several computers currently being marketed use such
generalized hardware backed up by software in PROM monitors. These include the new Apple computer,
BABY by STM Systems, etc." — Conf: High — Corroboration: 1 (independent of the advertisements) —
Conflicts: None. This is the only November 1976 *editorial* (non-advertising) Apple sentence
recovered in the twelve 1976 issues.

A2-15 Claim: BYTE's December 1976 editorial names **"Steven Jobs (Apple Computer Co)"** as one of
four entrepreneurs Helmers spoke with **on the floor of WESCON in Los Angeles in September 1976**,
alongside Bob Marsh (Processor Technology), Chris Rutkowsky (Technical Design Labs) and **Paul
Terrell (Byte Shops)** — the earliest outside coverage recovered that puts Jobs at a trade show in
the same breath as the dealer who is credited in memoir as Apple's first customer — Date: 1976-09
(event) / 1976-12 (publication) — Source: BYTE, December 1976, "Editorial: Caught by Surprise,"
Carl Helmers (lines ~1507–1519) — Source date: December 1976 — URL:
https://archive.org/details/byte-magazine-1976-12 — Archived: `sources/ia_byte_1976/byte-1976-12.txt`
— Tier: 1 — Class: CONTEMPORARY OBSERVATION — Passage: "Elements of this attitude of achievement
were present in my conversations with entrepeneurs Bob Marsh (Processor Technology), Chris
Rutkowsky (Technical Design Labs), Steven Jobs (Apple Computer Co) and Paul Terrell (Byte Shops)
on the floor of the WESCON show last September in Los Angeles CA." — Conf: High — Corroboration:
A2-16 and A2-12 place the same parties in print in the same quarter, but **all three BYTE items
are the same magazine; counted as one origin for BYTE's editorial line** — Conflicts: None.
[sic "entrepeneurs".] **The editorial's own framing matters for the firewall: Helmers is writing
about a "revolution" he says is arriving from the hobby end, and he names Jobs as one of several
peers, not as the leader of the group.**

A2-16 Claim: The same December 1976 issue reports Jim Warren's **committed exhibitor list for the
first West Coast Computer Faire, which includes "Apple Computers"** in a list running through
Quay Corp, STM Systems, Project Support Engineering, AEC and DTC — Date: 1976-12 (publication),
event to come 1977-04 — Source: BYTE, December 1976, "Trade Show Booths Available" (line ~29851)
— Source date: December 1976 — URL: https://archive.org/details/byte-magazine-1976-12 — Archived:
`sources/ia_byte_1976/byte-1976-12.txt` — Tier: 1 — Class: CONTEMPORARY OBSERVATION — Passage:
"Apple Computers / STM Systems / Project Support Engineering / AEC (Associated Electronics Co) /
DTC (Data Terminals & Comm)" — Conf: High — Corroboration: 1 magazine, 2 documents within it
(this list and Homebrew 1976-09-15's list, A2-30) — Conflicts: none as to existence; the *name*
varies across 1976 print (see U-A2-1).

A2-17 Claim: The New York chain's Apple-bearing brand-block advertisement **ran a third time in
December 1976, now with a Christmas gift-certificate line** — Date: 1976-12 — Source: BYTE,
December 1976, advertisement (line ~32182) — Source date: December 1976 — URL:
https://archive.org/details/byte-magazine-1976-12 — Archived: `sources/ia_byte_1976/byte-1976-12.txt`
— Tier: 1 — Class: FACT — Passage: "Christmas gift certificates available / IMSAI, SWTPCo,
Digital Group / Processor Tech, Apple, OSI / TDL-Z-80, Seals, Cromemco, / Veras, Tarbell, Oliver" —
Conf: High — Corroboration: **1 campaign across 3 issues (Oct, Nov, Dec 1976) — recorded as
duration, not as corroboration** — Conflicts: None. Note the December brand block swaps "Sphere"
for "Veras", i.e. the stocked-brand list is *not* stable across months; a brand's presence in one
month does not prove continuity of supply.

A2-18 Claim: **Documented negative, and it is the load-bearing one for the stage.** Across all
twelve 1976 issues of BYTE (~5.7 MB of OCR, every `apple` token inspected per A2-01…A2-05), the
company Apple **placed no advertisement of its own in 1976 and issued no press item carried as
its own text**: every 1976 Apple-1 product reference is a *dealer's* advertisement (A2-08, A2-11,
A2-12, A2-17), one technical mention (A2-14), one editorial naming Jobs (A2-15) and one exhibitor
list (A2-16). There is no Apple address, no Apple telephone, no Apple price and no Apple
letterhead in BYTE 1976 — Date: 1976 (full year) — Source: exhaustive token-by-token grep of
`ia_byte_1976/byte-1976-01..12.txt` — Source date: retrieved 2026-09-24, re-mined by this pass —
URL: see per-issue URLs above — Archived: `sources/ia_byte_1976/` — Tier: 1 — Class: FACT
(documented absence within this corpus) — Passage: NO_VERBATIM_PASSAGE_RECORDED (negative
finding) — Conf: Medium-High (OCR can mangle a brand line; the residual risk is a garbled Apple
logotype, which is real in this corpus — see A2-11) — Corroboration: 1 corpus — Conflicts: None.
**What this null buys:** the 1976 market presence of the Apple-1 was *carried by resellers*, and
any Stage-1 claim about Apple "advertising" in 1976 is unsupported; the maker's own printed voice
begins in 1977 (A2-25, A2-27). It also means **no contemporaneous 1976 document in this corpus
states a sale, an order, an order size, or a price paid.**

A2-19 Claim: The **first dated artifact of the founders' own names** recovered in the club corpus
is a *different club's* letter printed in the Homebrew newsletter of **1976-04-30**: the Sonoma
County Micro Computer Club (Ripley, editor; letter reprinted by Robert Reiling) reports its
working inventory as "several ALTAIR's, an IMSAI, a JOLT, two PDP-8's, **an APPLE** and some others
on order", and adds "In April the APPLE 6502 system was our special guest. We are grateful to
**STEVE WOZNIAK** for providing transportation." — Date: 1976-04 (event) / 1976-04-30 (document) —
Source: Homebrew Computer Club Newsletter Vol 2 No 4 (lines ~130–146) — Source date: 1976-04-30 —
URL: https://archive.org/details/hcc0204 — Archived: `sources/ia_homebrew/hcc0204.txt` — Tier: 1 —
Class: CONTEMPORARY OBSERVATION (of a machine and a man, **not** of a company) — Passage: quoted
above — Conf: High — Corroboration: 2 (BYTE 1976-11 sighting of the machine in Wozniak's hands,
AP-15; Wozniak's own May 1977 article, A2-25) — Conflicts: None. Two additions to AP-24: the APPLE
appears inside a **club inventory list of other firms' machines**, so the machine's first documented
social life is as a *loanable curiosity among ALTAIRs*, and the newsletter's own masthead shows
Reiling editing from **Post Office Box 626, Mountain View, CA 94042** — the same city as the
Byte Shop #1 at "1063 El Camino Real, Mountain View, Calif. 94040" (A2-09), a different ZIP prefix on
the same corridor. The club's postbox, the shop's storefront and the founders' later address of record
(Cupertino, A2-27) sit inside a single thirty-mile arc: **this is a market that fits on one magazine
page, which is why a stage built from print is possible at all here.**

A2-20 Claim: The **6502 as the Apple machine's stated processor is a contemporaneous 1976 fact
from outside the company** — the club letter says "the APPLE 6502 system", a year and a half before
any Apple-published document in this corpus — Date: 1976-04-30 — Source: as A2-19 — Source date:
1976-04-30 — URL: https://archive.org/details/hcc0204 — Archived: `sources/ia_homebrew/hcc0204.txt`
— Tier: 1 — Class: FACT (as printed) — Passage: "In April the APPLE 6502 system was our special
guest." — Conf: High — Corroboration: 2 (the Apple-1's 6502 is also implied by the BYTE November
1976 PROM-monitor article, A2-14, and explicit in Wozniak's May 1977 article) — Conflicts: None.
**Hindsight guard: the choice of 6502 is recorded here as a documented attribute, not as evidence
of prescience; MOS's own 6502 price war is the contemporary context (A2-41).**

A2-21 Claim: Homebrew's **1976-09-15** newsletter lists **"Apple Computers"** among a roll of
concerns in the field, in the same breath as Polymorphic Systems, Quay Corp, Southwest Technical
Products, Byte Inc, Call Computer, STM Systems, Computer Conversor, Solid State Music, Shugart
Associates and "on and on" — Date: 1976-09-15 — Source: Homebrew Computer Club Newsletter Vol 2
No 9 (lines ~231–239) — Source date: 1976-09-15 — URL: https://archive.org/details/hcc0209 —
Archived: `sources/ia_homebrew/hcc0209.txt` — Tier: 1 — Class: CONTEMPORARY OBSERVATION — Passage:
"Percom, Osborne & Assoc., Technical Design Labs, Polymorphic Systems, Microcomputer Associates,
[n]ational Multiplex, Quay Corp., Southwest Technical Products, **Apple Computers**, Byte Inc.,
Call Computer, STM Systems, Computer Conversor, Solid State Music, Project Support Engineering,
iCom, Shugart Assoc., CompuMart, Monolithic Systems, Associated Electronics, and on and on." —
Conf: High — Corroboration: 2 (BYTE 1976-12 exhibitor list, A2-16 — different publication) —
Conflicts: U-A2-1 (name form). **The company enters the printed record as one name in a list of
twenty, in a newsletter edited in Mountain View, with no article, no price and no product claim
attached.**

A2-22 Claim: The same Homebrew issue of 1976-09-15 carries a **reader's technical letter describing
how to drive a Sony television set to produce printout "from the Apple Computer"** — the earliest
*user's* text about the machine recovered anywhere in this corpus, and independent of both the
company and the club organisers — Date: 1976-09-15 — Source: Homebrew Computer Club Newsletter
Vol 2 No 9, correspondence (lines ~745–754) — Source date: 1976-09-15 — URL:
https://archive.org/details/hcc0209 — Archived: `sources/ia_homebrew/hcc0209.txt` — Tier: 1 —
Class: CONTEMPORARY OBSERVATION — Passage: "I used Sony's TV 920 and TV750 for this modification to
produce printout from the Apple Computer. Character resolution was excellent. Pulling the phone plug
from the jack returns the set to normal video — with no change in the quality of the original
picture." — Conf: High — Corroboration: 1 — Conflicts: None. Product-history value: as of
September 1976 the machine's documented output path is **a modified domestic television set**,
which is the practical context of the "15 colors" claim Apple later prints (A2-27).

A2-23 Claim: **Negative — no 1976 print in this corpus names the Apple-1's price, and no 1976 print
names an order.** Searching the twelve BYTE 1976 issues and the Homebrew issues 1975-11 → 1976-12
for a price in the same document as "Apple" returns only the *discount formula* at A2-12
("10% discount from manufacturer's current list prices"), which proves a list price existed by
November 1976 but does not state it — Date: 1976 — Source: negative across `ia_byte_1976/`,
`ia_homebrew/` — Source date: 2026-09-24 (this pass) — URL: as above — Archived: as above —
Tier: n/a — Class: UNKNOWN (documented absence in the cached periodicals) — Passage:
NO_VERBATIM_PASSAGE_RECORDED — Conf: High (absence from these files) — Corroboration: 0 —
Conflicts: none recorded; the famous $666.66 is absent from every file on disk (see §Contradictions
U-A2-4).

A2-24 Claim: **Negative — the Apple-1 is never connected in 1976 print to the founders' home,
street, town or headcount.** The 1976 records above place Jobs in Cupertino? — no: the *only* 1976
address attached to an Apple name anywhere in the cached corpus is the company's later 1977
Cupertino address (A2-25, A2-27). No 1976 document in these files states a business address for
Apple, "Los Altos", "Cupertino", "Sunnyvale", a garage, or a number of employees — Date: 1976 —
Source: negative across the 1976 corpus — Source date: 2026-09-24 — URL: as above — Archived: as
above — Tier: n/a — Class: UNKNOWN (documented absence) — Passage: NO_VERBATIM_PASSAGE_RECORDED —
Conf: High for these files — Corroboration: 0 — Conflicts: U-A2-13 (the universe register's "Los
Altos" versus the 1977 print's Cupertino).

### 1977 — the maker speaks, and the machine changes shape

A2-25 Claim: **Steve Wozniak, in print in May 1977 under his own name and his employer's address,
dates the Apple-I's design to late 1975 and describes its distribution as word of mouth followed by
generic retail** — the single most important first-party statement recovered for Stage 1, and it
contains **no first customer, no order, no unit count and no city** — Date: 1975 (design event) /
1977-05 (publication) — Source: Stephen Wozniak, "The Apple-II — System Description", BYTE, May
1977, p 3 (lines ~6372–6420) — Source date: May 1977 — URL:
https://archive.org/details/byte-magazine-1977-05 — Archived: `sources/ia_byte_1977/byte-1977-05.txt`
— Tier: 1 — Class: FOUNDER CLAIM (**contemporaneous**, per §3 — spoken by the designer while the
company was two months old and while the outcome was unknown) — Passage: "The Apple-I, my first
video oriented single board computer, was designed late in 1975 and sold by word of mouth
throughout California and later nationwide through retail computer stores. I think that the Apple-I
computer was the first microprocessor system product on the market to completely integrate the
display generation circuitry, microprocessor, memory and power supply on the same board." — Conf:
High (that he said it, in-window, in his own byline); Medium (the design date itself, being a
founder's own uncorroborated recollection committed to print) — Corroboration: the *distribution
characterisation* is corroborated by independent third-party print (A2-08, A2-12, A2-11); the
*design date* is corroborated by **nothing** in this corpus — Conflicts: U-A2-2 (word of mouth
versus the canonical single founding order), §Terminated (the 1975 Homebrew demo claim).

A2-26 Claim: Wozniak's May 1977 article also states the Apple-I's **original design intent** — a
television terminal product that could also run stand-alone — and the **retail price band** and the
**delivered form** ("completely assembled and tested") — Date: 1977-05 — Source: as A2-25 (lines
~6403–6416) — Source date: May 1977 — URL: as A2-25 — Archived: `sources/ia_byte_1977/byte-1977-05.txt`
— Tier: 1 — Class: FOUNDER CLAIM (contemporaneous) — Passage: "The Apple-I video computer board was
originally intended as a television terminal product which could also operate in a stand alone mode
without much in the way of memory, although it did have a processor, space for 8 K bytes of 4 K
dynamic memory chips, and its shared video generation and dynamic memory refresh logic. **Apple-I
was sold as a completely assembled and tested processor board with a price under $700 at the retail
level.**" — Conf: High (as printed), Medium (the "under $700" is a founder's aggregate characterisation,
not a published price schedule; A2-23 establishes that no 1976 print states one) — Corroboration: 1 —
Conflicts: U-A2-4 (no 1977 print carries the famous $666.66 either). **Analytical note, firewall
attached: "originally intended as a television terminal product" is a founder stating that his first
product was conceived as a *peripheral substitute*, not as a computer — the opposite of the later
story about intending a personal computer. It is recorded as his contemporaneous claim about intent,
which is the only class of evidence available on intent.**

A2-27 Claim: **Apple Computer Inc.'s first self-published advertisement in this corpus** (June 1977)
fixes the corporate name, the address of record, the telephone, and a consumer-facing configuration
claim, and it directs readers to a dealer network it does not name — Date: 1977-06 — Source: Apple
Computer Inc. advertisement, BYTE, June 1977 (lines ~1917–2010) — Source date: June 1977 — URL:
https://archive.org/details/byte-magazine-1977-06 — Archived: `sources/ia_byte_1977/byte-1977-06.txt`
— Tier: 1 (primary advertising artifact) — Class: FACT (the company's own published offer) /
FOUNDER CLAIM in substance for every product superlative inside it — Passage: "Clear the kitchen
table. Bring in the color TV. Plug in your new Apple II and connect any standard cassette
recorder/player. … Only Apple II makes it that easy. … it's the first personal computer with a fast
version of BASIC permanently stored in ROM. … Write us today for our detailed brochure and order
form. Or call us for the name and address of the **Apple II dealer nearest you. (408) 996-1010.
Apple Computer Inc., 20863 Stevens Creek Boulevard, Bldg. B3-C, Cupertino, California 95014.**" —
Conf: High — Corroboration: the same address and byline appear in Wozniak's May 1977 article (A2-25)
— **one company-side interest, two documents; not counted as independent** — Conflicts: None. Note
"the first personal computer with …" is a company superlative about its own category and is to be
read as an advertising claim, not as a fact of priority.

A2-28 Claim: **The complete Apple II price ladder as printed by Apple in June 1977 — nine
configurations, two forms, and California tax add-ons — recovered in full from the cached OCR**, a
table the feasibility probe did not read — Date: 1977-06 — Source: "Apple II Price List", in the
Apple Computer Inc. advertisement, BYTE, June 1977 (lines ~2286–2330) — Source date: June 1977 —
URL: as A2-27 — Archived: `sources/ia_byte_1977/byte-1977-06.txt` — Tier: 1 — Class: FACT (company's
published price list) — Passage: "4K $1,298.00 / $84.37 / $598.00 / $38.87 — 8K 1,398.00 90.87 698.00
45.37 — 12K 1,498.00 97.37 798.00 51.87 — 16K 1,698.00 110.37 978.00 63.57 — 20K 1,778.00 115.57
1,078.00 70.07 — 24K 1,878.00 122.07 1,178.00 76.57 — 32K 2,158.00 140.27 1,458.00 94.77 — 36K
2,258.00 146.77 1,558.00 101.27 — 48K 2,638.00 171.47 1,938.00 125.97" plus "Memory is offered at a
20% savings when ordered with the system-or board-as reflected in the prices above. … One set 4K
chips (4K bytes) $125 / One set 16K chips (16K bytes) $600" — Conf: High — Corroboration: the
headline pair $1,298 / $598 is repeated verbatim in the July 1977 re-run (A2-32) — Conflicts: U-A2-6
(the implied tax rate versus every other tax line in the same magazine). **This is the only complete,
maker-published price schedule for Apple's first product generation that this corpus yields, and it
converts the company's 1977 pricing from a single remembered number into a nine-row series.**

Arithmetic on A2-28 (all DERIVED, shown per §3/§13):
- Implied California sales-tax rate: `84.37 / 1298.00 = 0.0650` → **6.5%**; cross-checks at three
  other rows: `38.87 / 598.00 = 0.0650`; `110.37 / 1698.00 = 0.0650`; `171.47 / 2638.00 = 0.0650`.
  The table is internally consistent at 6.5%, which is **why** U-A2-6 matters: two other 1976–1980
  items in the same cached corpus print 6% (A2-45, A2-53).
- Assembled-system premium over board-only: `1298 − 598 = $700` (what the case, keyboard, power
  supply, two game paddles and a demonstration cassette were priced at by the maker, June 1977).
- Marginal factory memory, system column: `1398 − 1298 = $100` per 4K = **$25 per 1K** for the
  4K→12K steps; then `1698 − 1498 = $200` at the 16K step (the row where 16K chips replace 4K chips).
- Aftermarket comparison: one 4K chip set `$125` for 4K = **$31.25 per 1K**; one 16K set `$600` for
  16K = **$37.50 per 1K**, both *above* the in-factory marginal rate — i.e. the maker priced
  later upgrades dearer than factory-installed memory.
- Undoing the stated "20% savings": if the chip-set prices above are the discounted ones, the
  undiscounted list equivalent is `600 / 0.8 = $750` and `125 / 0.8 = $156.25`.

A2-29 Claim: **Apple sold by mail order directly to end users in 1977, on its own printed order
form, with a shipping subsidy and a premium bundled accessory** — a channel the probe did not
record — Date: 1977-06 (and 1977-07) — Source: "Order your Apple II now" block, Apple advertisement,
BYTE June and July 1977 (lines ~2277–2284 / ~3981–3988) — Source date: 1977-06, 1977-07 — URL:
https://archive.org/details/byte-magazine-1977-06 ; …/byte-magazine-1977-07 — Archived: both files —
Tier: 1 — Class: FACT (the company's own published offer) — Passage: "Use this order form to get your
Apple II fast. As a special offer for those who order now, we will include **free a custom vinyl
carrying case (a $50 value)**. And we will also **pay shipping charges to anywhere in the continental
United States**." Order form: "□ Please send me an Apple II System □ Board Only — with ___K bytes of
RAM (4K minimum) at $___ … Mail to: Apple Computer Inc., 20863 Stevens Creek Blvd., B3-C, Cupertino,
California 95014" — Conf: High — Corroboration: 2 issues, **one campaign** — Conflicts: None. Two
things follow without hindsight: (i) the dealer network and direct mail coexisted from the first month
of the company's own advertising, and the maker competed with its own resellers on terms (postage
paid, free case); (ii) a "$50 value" accessory is the company's own printed valuation of a case,
useful as a price anchor, not as a margin estimate.

A2-30 Claim: **Apple's advertisement ran in BYTE in June *and* July 1977, and the July run is
paginated and indexed** — Date: 1977-07 — Source: BYTE, July 1977, "Introducing Apple II." (line
~3781) and the issue's advertiser index entry (line ~36460) — Source date: July 1977 — URL:
https://archive.org/details/byte-magazine-1977-07 — Archived: `sources/ia_byte_1977/byte-1977-07.txt`
— Tier: 1 — Class: FACT — Passage: index line "7 **Apple 22, 23, 24**" (advertiser #7, pages 22–24);
headline "Introducing Apple II." — Conf: High — Corroboration: 1 issue + June antecedent — Conflicts:
None. Provenance value: **a three-page, front-of-book placement in a magazine whose total pagination
runs to 160**, and the reader-service number changes from 272 (June) to 7 (July), i.e. Apple bought
position, not just space. This is the strongest available print evidence of the young corporation's
marketing capacity, and it is *not* evidence of product merit.

A2-31 Claim: Carl Helmers' April 1977 column, re-read in full, does three things the probe's excerpt
did not capture: it **pre-announces the Apple-II introduction at the Faire**, defines the "**appliance
computer**" category in retail terms, and narrates a dated hands-on session of 1976-11-20 in which
**the BASIC in the machine was a 5K interpreter with 16-bit integer arithmetic and the Color Eater
game was written in it in 30–45 minutes by Helmers and the two founders together** — Date: 1976-11-20
(event) / 1977-04 (publication) — Source: "A Nybble on the Apple — Notes by Carl Helmers", BYTE, April
1977 (lines ~2680–2765) — Source date: April 1977 — URL: https://archive.org/details/byte-magazine-1977-04
— Archived: `sources/ia_byte_1977/byte-1977-04.txt` — Tier: 1 — Class: CONTEMPORARY OBSERVATION
(COIN by a named publisher who had a personal relationship with the subjects — priced into §Provenance
per brief D6-2) — Passage: "An 'appliance computer' is by definition a completed system which is
purchased off the retail shelf, taken home, plugged in and used. I first saw the Apple-ll on November
20 1976 when Stephen Wozniak and Stephen Jobs stopped by a motel room in Palo Alto where I was staying
at the time. They brought along the prototype Apple-ll to give a demonstration. … That evening last
November, Steve Jobs, Steve Wozniak and I sat down and proceeded to use the Apple-ll BASIC (which is a
5 K interpreter with 16 bit integer arithmetic) to program the Color Eater game. After perhaps 30 to 45
minutes, we had a working BASIC language version…" — Conf: High — Corroboration: 1 (single witness,
published within five months) — Conflicts: U-A2-3 (the Faire's days). Note the *category claim* is
Helmers' judgement printed in April 1977, and the phrase "may be the first product to fully qualify"
is hedged; it must not be quoted as a prophecy.

A2-32 Claim: Helmers' April 1977 column also states that **the machine Apple was about to introduce
would be described the following month by its designer** and directs readers to **"the Apple Computer
booth"** at the Faire — the last pre-launch trade-press reference recovered, and a third name form
("Apple Computer booth") — Date: 1977-04 — Source: as A2-31 (lines ~2682–2683, ~2758–2765) — Source
date: April 1977 — URL: as A2-31 — Archived: as A2-31 — Tier: 1 — Class: CONTEMPORARY OBSERVATION —
Passage: "Next month, we'll have an article by Steve Wozniac, designer of the Apple-U computer,
describing this beautiful new conception of the small computer. … If you attend the first West Coast
Computer Faire, stop by the Apple Computer booth and take a look at this interesting processor." —
Conf: High — Corroboration: 1 — Conflicts: the same column spells "Wozniac" in the first sentence and
"Wozniak" later — a spelling instability to carry in citations, not a substantive conflict. Note this
is the *only* place in the cached 1977 issues where Apple's booth is invited-to rather than reviewed.

A2-33 Claim: Wozniak's May 1977 article names, **in Apple's own voice and in-window, the four
non-founder hands credited on the Apple-II's software and I/O** — Allen Baum, Doug Kraul, Randy
Wigginton and Chris Espinosa — the earliest printed personnel list associated with the company
recovered anywhere in this corpus — Date: 1977-05 — Source: acknowledgement box, "The Apple-II", BYTE
May 1977 (lines ~8270–8282) — Source date: May 1977 — URL: https://archive.org/details/byte-magazine-1977-05
— Archived: `sources/ia_byte_1977/byte-1977-05.txt` — Tier: 1 — Class: FOUNDER CLAIM
(contemporaneous, first-party) — Passage: "…I would like to thank Allen Baum for originating the
Apple-// debug software, Doug Kraul for helpful suggestions on the 10 structure, and Randy Wigginton
and Chris Espinosa for many long and late hours testing the Apple BASIC. . . . SW" — Conf: High (the
names and roles as printed) — Corroboration: 1 — Conflicts: None. **Boundary: no title, wage, hire
date or headcount appears; "employee #6" and similar numbering exist nowhere in these files, so any
employee-order claim about these four is unsupported by this corpus** (compare AP-31, which carries
"Randy Wigginton … Apple employee #6" from a 2022 registry page).

A2-34 Claim: The Apple-II's technical configuration, in the designer's own May 1977 text, **includes
claims that predate and therefore independently corroborate the June advertisement's spec box** —
8-slot buffered S-100-like motherboard with prioritised interrupts and two DMA schemes, cassette
transfer averaging "over 180 bytes per second" and compatible with the Apple-I's scheme, 4K/16K DRAM
intermixing, ~200 bytes of the 8K ROM given to monitor control, a 5×7 dot matrix in upper case only,
and an analog game-paddle circuit on 555-type timer chips — Date: 1977-05 — Source: as A2-25 (lines
~6441–6464, ~7515–7529, ~7693–7733) — Source date: May 1977 — URL: as A2-25 — Archived: as A2-25 —
Tier: 1 — Class: FACT (as printed by the company's designer) — Passage: "Also part of the Apple-ll
design is an 8 slot motherboard for IO which has a fully buffered bus, prioritized interrupts, two
prioritized direct memory access (DMA) schemes… The Apple-ll cassette interface is simple, fast, and I
think most reliable. The data transfer rate averages over 180 bytes per second, and the recording
scheme is compatible with the interface used with the Apple-I." — Conf: High — Corroboration: 1
company-side document, 2 if the June ad's spec box is counted as a separate publication of the same
claim (same interest; independence note recorded) — Conflicts: None. **Time audit: the article says
4K or 16K chips may be intermixed and the memory ceiling is a function of chips fitted; the "up to
48K" figure in the June ad (A2-27/28) is the advertised ceiling, and nothing in the May text supports
64K or 128K, which appear only in 1980 print (A2-54).**

A2-35 Claim: **BYTE's April 1977 issue prints a national, state-by-state computer-store directory —
roughly sixty named outlets across 22 jurisdictions including Canada and Japan — of which about
thirty-five lines are Byte Shop outlets, each with street address, telephone and a named manager.**
This is the first *enumerable* retail circuit available for the period in which the Apple II was
introduced, and it is the corpus's single best answer to "distribution channels advertised" — Date:
1977-04 — Source: BYTE, April 1977, computer-store directory block (lines ~4700–5240) — Source date:
April 1977 — URL: https://archive.org/details/byte-magazine-1977-04 — Archived:
`sources/ia_byte_1977/byte-1977-04.txt` — Tier: 1 — Class: FACT (the printed list; exact page
number UNKNOWN in this OCR rendering, position in the issue's feature matter) — Passage (four of
many): "**Byte Shop of Mt. View**, 1063 W. El Camino, Mt. View, CA 94040, (415) 969-5464, Boyd Wilson
… **Byte Shops, Inc.**, 1261 Birchwood Dr., Sunnyvale, CA 94086, (408) 734-9000, Bryan Kerr … **Byte
Shop of Berkeley**, 1514 University Ave., Berkeley, CA 94703, (415) 845-6366, Pete Hollenbeck … **Byte
Shop of Tokyo**, 2-9-9 Sotokanda, Chiyodaku, Tokyo, Kiyotake Ikeda" — Conf: High — Corroboration: 2
independent printings of the same circuit (BYTE Sept 1976 distributor list, A2-09; BYTE Nov 1976 Bay
Area list, A2-13) at earlier dates and smaller scale — Conflicts: None. Jurisdictions represented:
ARIZONA, CALIFORNIA, COLORADO, FLORIDA, ILLINOIS, INDIANA, KENTUCKY, MARYLAND, MINNESOTA, MISSOURI,
NEW HAMPSHIRE, NEW JERSEY, NEW YORK, OKLAHOMA, OREGON, PENNSYLVANIA, TENNESSEE, UTAH, VIRGINIA,
WISCONSIN, CANADA, JAPAN. **The chain that memoir credits as Apple's first customer was, in the month
of the Apple II's announced introduction, a multi-state and trans-Pacific franchise with a named
managing entity at a Sunnyvale address — that is what the print supports, and no more.**

A2-36 Claim: The same April 1977 directory places **Apple's competing retailers by name**, so the
dealer set the young corporation sold into is enumerable rather than folkloric — Date: 1977-04 —
Source: as A2-35 (lines ~4760–4870, ~5215–5240) — Source date: April 1977 — URL: as A2-35 — Archived:
as A2-35 — Tier: 1 — Class: FACT — Passage: "**Desert Data Computer Store**, P.O. Box 1334, Tucson,
AZ 85702, Gary Miller & Bud Ward … **The Computer Store**, 820 Broadway, Santa Monica, CA 90401, Dick
Heiser … **A-VID Electronics**, 1655 E. 28th St., Long Beach, CA 90806, Reynolds Johnson … **People's
Computer Shop**, 13452 Ventura Blvd., Sherman Oaks, CA 91423, W. K. Ling … **The Computer Mart**, 625
W. Katella #10, Orange, CA 92667, (714) 633-1222, **Allan Tarsky** … **The Pacific Computer Bazaar**
[OCR: "Snorni"], 4509-4511 Rupert St., Vancouver, B.C." — Conf: High — Corroboration: A2-09 (A-VID and
Computer Mart appear in the September 1976 distributor list too) — Conflicts: None. Continuity
evidence: A-VID Electronics of Long Beach appears in September 1976 **and** April 1977 lists, so a
retailer's presence across eight months of print is observable in this corpus — the only form of
"dealer durability" this archive can actually support.

A2-37 Claim: **A named East-Coast franchise outpost of the Byte Shop chain appears in May 1977
advertising a full multi-vendor line — "BYTE SHOP EAST, INC." of Levittown, Long Island** — Date:
1977-05 — Source: BYTE, May 1977, advertisement (lines ~42180–42205) — Source date: May 1977 — URL:
https://archive.org/details/byte-magazine-1977-05 — Archived: `sources/ia_byte_1977/byte-1977-05.txt`
— Tier: 1 — Class: FACT — Passage: "Processor Tech … SWTP MP68 … CROMEMCO … TDL … Lear Siegler …
Poly-88 … KITS and ASSEMBLED / BYTE SHOP EAST, INC. 27-21 Hempstead Turnpike, Levittown, Long Island
NY. (516) 731-8116. Two Blocks East of Wantagh Pkwy." — Conf: High — Corroboration: 1 — Conflicts:
None. Note what this advertisement does **not** contain: no Apple. A Byte Shop outlet listing seven
other lines in May 1977 is a documented instance of a dealer carrying Apple's competitors, and it
bounds any inference that the chain was Apple's channel by default.

A2-38 Claim: **Computer Mart of New York — the first retailer to advertise an Apple-1 in this corpus
(A2-08) — is identified by name and keeper in May 1977, and claims East-Coast primacy for itself
while moving store** — Date: 1977-05 (claim); "last year" = 1976 (asserted event) — Source: BYTE, May
1977, advertisement "COMPUTER MART" (lines ~42210–42262) — Source date: May 1977 — URL: as A2-37 —
Archived: `sources/ia_byte_1977/byte-1977-05.txt` — Tier: 1 — Class: FOUNDER CLAIM of a *third
party* (retailer's own contemporaneous primacy claim: a commercial self-characterisation, not a
fact) — Passage: "A NEW YEAR, A NEW LOGO, A NEW STORE!! **Last year we opened the first computer store
on the East Coast.** This year we move out of the Hobby Store and into our new Real Systems Showroom
and Store. … IMSAI, PROCESSOR TECHNOLOGY, … **APPLE**, OLIVER, SMOKE SIGNAL, MULLEN, GBC MONITORS …
**Stan Veit - Storekeeper.** COMPUTER MART OF NEW YORK INC. 118 [Ave of the Americas?] (30th ST.)
212-686-7923" — Conf: High (advertisement exists; keeper named; Apple listed among ~25 lines), Low
(the primacy claim) — Corroboration: the store's identity is independently fixed by BYTE's own June
1976 hobby column, "Stanley Veit, storekeeper of the Computer Mart of New York, Inc, 314 Fifth Av,
New York NY 10001" (`byte-1976-06.txt` line ~22102) — Conflicts: **U-A2-5, the primacy contest.**

A2-39 Claim: **A dated, in-window description of the very Berkeley firm that ran the November 1976
Apple-1 mail-order advertisement — before it had a store — comes from the Homebrew newsletter of
1976-06-09: Kentucky Fried Computers was then a mail-and-telephone-order kit business, giving
Homebrew members 10% off IMSAI, expiring 1976-07-31, operated by Mark Greenberg and Charles Grant,
c/o Applied Computer Technology, 1038 Merced, Berkeley** — Date: 1976-06-09 — Source: Homebrew
Computer Club Newsletter Vol 2 No 6, "BULLETIN BOARD" (lines ~270–284) — Source date: 1976-06-09 —
URL: https://archive.org/details/hcc0206 — Archived: `sources/ia_homebrew/hcc0206.txt` — Tier: 1 —
Class: CONTEMPORARY OBSERVATION / FACT (as printed) — Passage: "Kentucky Fried Computers, a new retail
computer kit business in Berkeley makes this offer: All IMSAI products (except some peripherals) will
be sold at 10% off to Homebrew Computer Club members. Add 2% if shipping is desired (excess is
refunded). … California residents must add 6% sales tax. The discount offer expires July 31, 1976.
Terms: cash. Kentucky Fried Computers is operated by Mark Greenberg and Charles Grant. **They plan to
open a store later this year, but for now they are selling on a mail and telephone order basis.**" —
Conf: High — Corroboration: 2 (BYTE November 1976 carries the same 10%-off/mail-order structure with
the Apple-1 starred, A2-12; BYTE April and May 1977 directories list "Kentucky Fried Computers, 2465
Fourth Street, Berkeley, 415-549-0858", A2-40) — Conflicts: none substantive; the street address moves
from 1038 Merced (June 1976) to 2465 Fourth Street (Nov 1976 onward) without explanation. **Forensic
value: the Apple-1's first *mail-order* reseller is documented six months before its Apple-1
advertisement as a storeless two-man operation that had not yet opened a shop — which is the shape of
Apple's 1976 distribution: it was sold through businesses that were themselves weeks old.**

A2-40 Claim: Kentucky Fried Computers' 10%-off formula and 6% tax line are printed in the same
corpus twice over, permitting an arithmetic check on the terms of hobby retail — Date: 1976-06-09 →
1977-05 — Source: as A2-39; A2-12; A2-35 — Source date: 1976-06 … 1977-05 — URL: as above —
Archived: `ia_homebrew/hcc0206.txt`, `ia_byte_1976/byte-1976-11.txt`, `ia_byte_1977/byte-1977-04.txt`
— Tier: 1 — Class: DERIVED (arithmetic shown) — Passage: "All IMSAI products … at 10% off … California
residents must add 6% sales tax" / "*Starred items available by mail order at 10% discount from
manufacturer's current list prices. For prompt delivery, send money order or cashiers check plus 2%
shipping & handling. Personal checks require 3 weeks processing." — Conf: High — Corroboration: 3
documents, **2 advertisers** — Conflicts: None. Arithmetic: an Apple-I at Wozniak's "under $700"
(A2-26) bought at these terms would cost `700 × 0.90 = 630`, plus `630 × 0.06 = 37.80` tax and
`630 × 0.02 = 12.60` carriage ≈ **$680.40 delivered** — i.e. the discount was roughly cancelled by tax
and shipping; the terms of trade, not the list price, set the real cost. Label DERIVED; the base
"$700" is itself a founder's rounded claim.

A2-41 Claim: The Homebrew newsletter of **1976-12-10 fixes the Faire's dates and venue in the club's
own print — "April 15-17, 1977 at the San Francisco Civic Auditorium"** with Jim Warren as chairperson
at Box 1579, Palo Alto — Date: 1976-12-10 — Source: Homebrew Computer Club Newsletter Vol 2 No 11
(lines ~69–77) — Source date: 1976-12-10 — URL: https://archive.org/details/hcc0211 — Archived:
`sources/ia_homebrew/hcc0211.txt` — Tier: 1 — Class: FACT — Passage: "MORE ON THE S-100-April, 1977.
The First West Coast Computer Faire being held April 15-17, 1977 at the San Francisco Civic
Auditorium, Northern California's largest convention facility, will have a conference session on the
S-100 bus according to Jim Warren, Faire Chairperson." — Conf: High — Corroboration: 3 (the Faire
flyer `hcccf`; the January 1977 newsletter `hcc0213` line ~1230; BYTE's April 1977 re-run of the
flyer) — Conflicts: U-A2-3 (the post-event report says "April 16 and 17"). **This closes the
feasibility probe's open data-gap row "Exact Apple II introduction date and Faire venue — MED …
Medium; venue contested" from local material, with zero web budget: the venue was the San Francisco
Civic Auditorium and the billed dates were April 15–17, 1977.**

A2-42 Claim: **The Faire's own promotional flyer, as distributed through the club, states the
expected scale in advance and makes a regional origin claim in print fourteen months before the
company's IPO-era retrospectives** — Date: 1977-02-16 (flyer) — Source: West Coast Computer Faire
flyer, Internet Archive item `hcccf` — Source date: 1977-02 — URL: https://archive.org/details/hcccf
— Archived: `sources/ia_homebrew/hcccf.txt` — Tier: 1 — Class: CONTEMPORARY OBSERVATION (the
organiser's own forecast) — Passage: "**San Francisco Bay Area - Where It All Started - Has Its First
Home Computing Convention** / 7,000 to 10,000 People / 100 Conference Sessions / Publication of
Proceedings Being Planned / 200 Commercial & Homebrew Exhibits … To Be Held in the San Francisco
Civic Auditorium … Jim Warren, Faire Chairperson, The Computer Faire, Box 1579, Palo Alto CA 94302,
(415) 851-7664 … GET YOUR FREE COPY OF SILICON GULCH GAZETTE" — Conf: High — Corroboration: 2
(BYTE April 1977 reprints the same flyer text; Homebrew 1977-01-19 repeats the numbers) — Conflicts:
None. Two uses: (i) "200 Commercial & Homebrew Exhibitors" is the denominating population inside which
Apple's booth (A2-32) sat; (ii) **"Where It All Started" is a 1977 marketing claim by a show promoter
about a region — evidence that a genesis narrative was already being sold before any company had an
origin story to sell. That belongs in §Founder state / §Contradictions as context, not as support for
Apple's own account.**

A2-43 Claim: BYTE's post-event report prints **the Faire's own attendance figure as announced by its
chairman at the close of the show — 12,800 — and dates the show to "April 16 and 17 of this year"** —
Date: 1977-04 (event) / 1977-07 (publication) — Source: Lawrence F. Willard, "Random Observations and
Conversations at the First West Coast Computer Faire", BYTE, July 1977 (lines ~4175–4244) — Source
date: July 1977 — URL: https://archive.org/details/byte-magazine-1977-07 — Archived:
`sources/ia_byte_1977/byte-1977-07.txt` — Tier: 1 — Class: CONTEMPORARY OBSERVATION for the event;
the number itself is **a self-report by the organiser with no independent count behind it** (record-
selection null applied) — Passage: "Photo 1: … At the end of the show, chaircreature Jim Warren
announced that 12,800 people had attended." / "…the First West Coast Computer Faire held in San
Francisco's Civic Auditorium on April 16 and 17 of this year." — Conf: Medium (a promoter's count,
single origin) — Corroboration: **1** — Conflicts: U-A2-3. Against A2-42's forecast of 7,000–10,000,
the announced 12,800 is `12,800 / 8,500 ≈ 1.5×` the mid-point of the organiser's own forecast — DERIVED,
and it is the only attendance arithmetic this corpus can honestly support, because both ends come from
the same promoter.

A2-44 Claim: The same Faire report records **Radio Shack franchise principals travelling to the
personal-computer show as prospective stockists** — the national chain's regional franchisees, not
corporate Tandy, evaluating the category at the moment Apple's first appliance-class machine
appeared — Date: 1977-04 — Source: as A2-43 (lines ~4918–4930) — Source date: July 1977 — URL: as
A2-43 — Archived: as A2-43 — Tier: 1 — Class: CONTEMPORARY OBSERVATION — Passage: "They were Manabu
Uyehara and George M Hirota, who have the Radio Shack franchise in Honolulu. They had flown to San
Francisco especially for the Faire. Both men have had previous computer experience, and they are
anxious to carry computers in their store." — Conf: High — Corroboration: 1 — Conflicts: None. No
hindsight: this is a printed observation of franchise interest in 1977, and this corpus contains **no
1977 print connecting Radio Shack and Apple** — any later deal between the two is outside this file.

A2-45 Claim: **The competing machine most directly comparable to the Apple-II in 1977 print is
Processor Technology's Sol-20 "Terminal Computer", advertised at $995 in kit form or $1,495 fully
assembled and tested, in a "beautiful case with solid walnut sides"** — Date: 1976-11 (first price
ad) and 1977-04 (kit/assembled pair) — Source: BYTE, November 1976 (lines ~19921–19934) and BYTE,
April 1977 (lines ~4680–4700) — Source date: 1976-11, 1977-04 — URL:
https://archive.org/details/byte-magazine-1976-11 ; …/byte-magazine-1977-04 — Archived: both — Tier: 1
— Class: FACT (advertising artifacts as printed) — Passage: "The remarkable new Sol-20 Terminal
Computer will give you all of the above . . . plus more! . . . as standard equipment for just $995, in
kit form." / "Now for only $995 in kit form or $1495 fully assembled and tested you can have your own
small computer … a beautiful case with solid walnut sides" — Conf: High — Corroboration: 2
advertisements, 1 advertiser — Conflicts: None. Arithmetic for the product-reconstruction section
(DERIVED): Apple's own 1977 premium for assembling and casing the Apple II over its board-only version
is `1298 − 598 = $700` (A2-28); Processor Technology's premium is `1495 − 995 = $500`. **Both houses
sold an assembled box at a surcharge; Apple's surcharge was 40% higher in dollars — `700/500 = 1.40`.
Recorded as price-sheet arithmetic only; it says nothing about which was the better decision.**

A2-46 Claim: **The competitive price floor printed on the same dealer pages that list APPLE among
stocked items**: a multi-line retailer's price block offers "IMSAI 8080 MICROCOMPUTER … $619.95/22
SLOT MOTHER BOARD / 849.95/WITH Z-80 CPU", a "SPECIAL 9" JAVELIN HIGH RESOLUTION VIDEO MONITOR
$159.95", and an ADM-3A terminal at "$895.00" kit / "1099.95" assembled, on a page whose stock list
begins "FOLLOWING ITEMS IN STOCK TDL, OAE, PROCESSOR TECH., SWTP, **APPLE**, HAYDEN, TARBELL, IMSAI,
LEAR SIEGLER, OKIDATA, DEC, JAVELIN, TELETYPE ASR-33, TRW" — Date: 1977-04 and 1977-05 — Source: BYTE,
April 1977 (lines ~20480–20545) and BYTE, May 1977 (line ~14323), retailer advertisement blocks; the
identical brand-list formula recurs November 1976 → May 1977 — Source date: 1977-04, 1977-05 — URL:
https://archive.org/details/byte-magazine-1977-04 ; …/byte-magazine-1977-05 — Archived:
`ia_byte_1977/byte-1977-04.txt`, `byte-1977-05.txt` — Tier: 1 — Class: FACT (as printed) — Passage: as
quoted; **advertiser identity on this page is illegible in this OCR rendering and is therefore recorded
as UNKNOWN rather than attributed to Computer Mart or Synchro-Sound, both of which advertised
adjacently** — Conf: High (prices as printed), Low (which firm placed them) — Corroboration: 2 issues,
1 campaign — Conflicts: None. **Context for A2-26: Wozniak's "under $700 at the retail level" for an
assembled video board sat *above* a kit mother-board price but *below* the $849.95 Z-80 board and far
below a $1,099.95 assembled terminal, i.e. priced as a board, not as a system. This is the observable
price geography of 1976–77, and it is what makes the June 1977 jump to $1,298 (A2-28) a change of
*product category* rather than a price rise — stated as an inference from printed rows, not as
hindsight about Apple's strategy.**

A2-47 Claim: **A second-order competitor price printed in the same pages as Apple's own June 1977
advertisement**: Technical Design Laboratories' Xitan alpha 2 — "18K of RAM, 2K of ROM, 2 serial I/O
ports, 1 parallel I/O port, our 1200 baud audio cassette interface" plus a bundled software package —
at "KIT: $1369 ASSEMBLED & TESTED: $1749" — Date: 1977-06 — Source: BYTE, June 1977, Xitan
advertisement (line ~7779) — Source date: June 1977 — URL: https://archive.org/details/byte-magazine-1977-06
— Archived: `sources/ia_byte_1977/byte-1977-06.txt` — Tier: 1 — Class: FACT (as printed) — Passage:
quoted above — Conf: High — Corroboration: 1 — Conflicts: None. Arithmetic (DERIVED, apples-to-oranges
flagged): TDL's assembled 18K machine at $1,749 versus Apple's assembled 16K Apple II at $1,698
(A2-28) puts Apple **$51 cheaper with 2K less memory** — `1749 − 1698 = 51`. The comparison is
between advertised ceilings for different machines (no colour, no ROM BASIC claim on TDL's side; the
TDL package includes BASIC and an assembler per its own ad), so it is recorded as price-sheet
adjacency, not as a value judgement, and explicitly **not** as evidence that Apple's pricing was
correct.

A2-48 Claim: **Wozniak's article was placed at page 3 of BYTE May 1977, with its own contents-line**
— the company's technical narrative entered the trade press above the ordinary article order — Date:
1977-05 — Source: BYTE, May 1977, contents listing (lines ~438–443, ~53949–53955) — Source date: May
1977 — URL: as A2-25 — Archived: `sources/ia_byte_1977/byte-1977-05.txt` — Tier: 1 — Class: FACT —
Passage: "Speculations— Lau / **THE APPLE-II** / System Description— Wozniak / INTERFACING WITH AN
ANALOG WORLD-Part 1" and index line "3 Wozniak: The Apple-ll" — Conf: High — Corroboration: 1 —
Conflicts: None. **Independence warning per §3: BYTE's editor had a personal relationship with the
subjects (A2-31 is a first-person account of programming a machine with them). Page-3 placement in a
magazine whose editor is a participant is a *relationship* datum, not an endorsement datum, and this
dossier prices it into §Provenance rather than into corroboration counts.**

### 1978–1981 — the far side of the stage: only what print said about the beginning

Everything in this block post-dates the Stage-1 boundary of 1977-01-03. It is admitted for one
purpose only: these are the **earliest printed statements about the founding period's numbers and
about the corporation**, i.e. the far-side witnesses that bound what Stage 1 may assert. Every record
here carries `RETROSPECTIVE SOURCE` where it speaks about 1975–76, and no record here is used to
validate an early choice (§2).

A2-49 Claim: **BYTE's February 1981 column is the earliest printed revenue series for Apple recovered
anywhere in this corpus**, and its internal arithmetic is checkable — Date: FY1978, FY1979,
FY1980-09-26 (events); 1981-02 (publication) — Source: "Apple Stock Goes On Sale", BYTE, February
1981, p 212 (lines ~48485–48528; page footer "212 February 1981 © BYTE Publications Inc") — Source
date: February 1981 — URL: https://archive.org/details/byte-magazine-1981-02 — Archived:
`sources/ia_byte_1981/byte-1981-02.txt` — Tier: 1 — Class: FACT for the figures **as printed**;
`RETROSPECTIVE SOURCE` for any 1975–77 inference drawn from them; UNKNOWN whether they restate the
prospectus or the author's arithmetic — Passage: "Apple, incorporated in 1977, reported profits of
$11.7 million on sales of $117 million for the fiscal year ending September 26, 1980. 1979's earnings
were $5 million on $48 million sales, and, in 1978, sales were $7.8 million with profits of $793,497."
— Conf: High (as printed) — Corroboration: **1 in this corpus**; the $7.8M/$117M pair also appears in a
2023 institutional page that cites no contemporaneous source (AP-23), so that is not a second witness —
Conflicts: U-A2-7 (FY1977 and FY1976 are absent; the series has a hole exactly where Stage 1 is).

Arithmetic on A2-49 (DERIVED; every figure traceable to the printed row above):
- Net margin FY1980: `11.7 / 117 = 10.0%`.
- Net margin FY1979: `5.0 / 48 = 10.4%`.
- Net margin FY1978: `793,497 / 7,800,000 = 10.17%`.
- Sales growth FY1978→FY1979: `48 / 7.8 = 6.15×` (**+515%**); FY1979→FY1980: `117 / 48 = 2.44×`
  (**+144%**); FY1978→FY1980: `117 / 7.8 = 15.0×`.
- **Observation worth holding:** the three printed years carry margins within 0.4 percentage points of
each other (10.0 / 10.4 / 10.17). That consistency is *either* a genuine operating constant *or* an
artefact of a single source rounding to two significant figures — the printed precision is inconsistent
(`$793,497` to the dollar versus `$5 million` and `$117 million` rounded), which means **the series
mixes precisions and must not be treated as audited**. Class DERIVED, Conf Medium; the mixed precision
is itself a finding (see U-A2-8).

A2-50 Claim: **The offering terms as printed, and the printed percentage does not reconcile with the
printed share counts** — Date: 1980-12 (offering); 1981-02 (publication) — Source: as A2-49 — Source
date: February 1981 — URL: as A2-49 — Archived: as A2-49 — Tier: 1 — Class: FACT (as printed) —
Passage: "Shares in Apple Computer Inc, one of the most eagerly awaited public stock offerings, went on
sale early in December 1980. Apple offered **8% of the company's 52.4 million shares (ie: 4.6 million
shares) at a price of $22 per share.**" — Conf: High (that it was printed), **Low as to internal
consistency** — Corroboration: 1 — Conflicts: U-A2-9 (arithmetic). Arithmetic (DERIVED): `0.08 ×
52,400,000 = 4,192,000` shares, not 4,600,000; and `4,600,000 / 52,400,000 = 8.78%`, not 8%. The two
printed statements are inconsistent by ~408,000 shares (~10% of the offer). Gross offer size on the
share count: `4.6M × $22 = $101.2M`; on the stated percentage: `4.192M × $22 = $92.2M`. **The dossier
records both and prefers neither; the reconciliation requires the paper prospectus, which this corpus
does not contain (UNTRIED, see §Data gaps DG-3).**

A2-51 Claim: **The pre-IPO cap table as printed in February 1981, including the two founders' ages and
a third named principal** — Date: 1981-02 (as of December 1980) — Source: as A2-49 (lines ~48504–48527)
— Source date: February 1981 — URL: as A2-49 — Archived: as A2-49 — Tier: 1 — Class: FACT (as printed)
— Passage: "Steve Jobs, 25 years old, and Steve Wozniak, 30 years old, the creators of the Apple
computer, each hold 8.3 million shares. That means that they own well over $100 million worth of
stock. A C Markkula, 32 years old, **who took Apple from a garage operation to its current enviable
position**, also holds 8.3 million shares. Venrock Associates, a venture capital firm, holds 3.8
million shares. Significant blocks are held by several other venture capital concerns. Xerox holds
80,000 shares." — Conf: High (as printed) — Corroboration: 1 — Conflicts: U-A2-10 (Wayne's absence).
Arithmetic (DERIVED): at the $22 offering price, `8.3M × $22 = $182.6M` per founder-holder; the three
named 8.3M holders together control `24.9M / 52.4M = 47.5%` of the company; Venrock's `3.8M / 52.4M =
7.25%`; Xerox's `80,000 / 52.4M = 0.15%`. **Note the language the record actually supports: the phrase
"from a garage operation" is contemporaneous trade-press prose of February 1981, four years after the
fact and one year after the corporation's first public pricing — it establishes that the garage
*characterisation* was in circulation by 1981, and establishes nothing about who owned the building.**

A2-52 Claim: **Documented negative inside the far-side witness: Ronald Wayne appears nowhere in the
February 1981 or December 1980 BYTE issues** — grep of both files (1.6 MB and 1.67 MB) for `Wayne` as a
person-name returns only "FT WAYNE" (Fort Wayne, in a store directory) and an unrelated John Wayne
reference in a game review — Date: 1980-12, 1981-02 — Source: negative grep of
`ia_byte_1981/byte-1980-12.txt`, `byte-1981-02.txt` — Source date: 2026-09-24 (this pass) — URL: as
above — Archived: as above — Tier: 1 — Class: FACT (documented absence in these two documents) —
Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High — Corroboration: 1 corpus — Conflicts: none in
print; the conflict is with the 1976-04-01 three-signatory agreement (AP-20). **This is the record-
selection null in operation: at the moment the founding story was being printed for public investors,
the third signatory was already invisible in the trade press that covered the offering. Whatever
erased him happened before the memoirs, in the periodical record itself.**

A2-53 Claim: **Apple's own December 1980 advertisement shows a company advertising nationally, with a
new address, a toll-free number, and a line addressed to computer-store retailers** — Date: 1980-12 —
Source: Apple Computer advertisement, BYTE, December 1980 (lines ~3960–4006) — Source date: December
1980 — URL: https://archive.org/details/byte-magazine-1980-12 — Archived:
`sources/ia_byte_1981/byte-1980-12.txt` — Tier: 1 — Class: FACT (company's published text) / FOUNDER
CLAIM in substance for its superlatives — Passage: "How Apple grows with you. … Have expansion
capabilities of 4 or 8 accessory slots with your choice of system. Expand memory to 64K bytes or 128K
bytes. … Since **more than 100 companies create software for Apple** … Apple is fluent in BASIC,
Pascal, FORTRAN, PILOT and 6502 assembly language. … You won't want to miss all the Apple products
being introduced at your computer store all the time. **Don't let history pass you by. Visit your
nearest Apple dealer or call 800-538-9696. In California, 800-662-9238. Or write: Apple Computer,
10260 Bandley Drive, Cupertino, CA 95014.**" — Conf: High — Corroboration: 1 company document —
Conflicts: none; note the **address change**: Stevens Creek Bldg. B3-C (1977, A2-27) → 10260 Bandley
Drive (1980). This is the observable footprint growth of the firm between the corporation's first
advertisement and its last pre-IPO one, and it is the only physical-premises evidence in this corpus
beyond 1977. **Hindsight guard: "more than 100 companies create software for Apple" is the company's
December 1980 claim about 1980; it may not be pushed back into 1977 to explain the Apple II's design.**

A2-54 Claim: By December 1980 **third-party advertisers were describing their own businesses entirely
in terms of the Apple install base**, including one claiming to have pre-empted Apple's own
peripherals, and one quantifying the dealer network — Date: 1980-12 — Source: Mountain Computer and
CCS advertisements, BYTE, December 1980 (lines ~4993–5148, ~5389–5394) — Source date: December 1980 —
URL: as A2-53 — Archived: `ia_byte_1981/byte-1980-12.txt` — Tier: 1 — Class: CONTEMPORARY OBSERVATION
(third-party commercial claims) — Passage: "Mountain Computer makes more peripherals for the Apple
Computer than Anybody. … After all, we were the first company to make an Apple peripheral— except
Apple Computer. Available at Apple Dealers worldwide." / "product line is available at over 250
locations nationally, including most that carry the Apple. … Apple II, Apple II Plus, and Applesoft
are trademarks of the **Apple Corporation**." — Conf: High (as printed) — Corroboration: 2 advertisers
— Conflicts: U-A2-11 (the legal-name error in a third party's ad copy; also "Apple Corporation" appears
nowhere else in this corpus). Distribution value: "over 250 locations nationally, including most that
carry the Apple" (a peripheral maker's own count, December 1980) is the closest thing to an
**independent third-party estimate of the size of Apple's dealer circuit** recovered in this dossier —
a competitor-supplied number, therefore more credible as a *ceiling* than a *floor*, and it belongs
with the 1976 "more than 250 stores coast to coast which regularly stock BYTE" (A2-10) as the two
comparable counts available.

A2-55 Claim: **A documented negative that closes the probe's general-press gap only partially: the
December 1980 and February 1981 BYTE issues contain no founding-narrative article at all** — the IPO is
reported in a 24-line news column (A2-49/A2-50) with no history section, no mention of 1975 or 1976,
no mention of the partnership, and no named first customer — Date: 1980-12 → 1981-02 — Source: negative
grep across both files for `1975`, `1976`, `partnership`, `Wayne`, `first customer`, `Byte Shop` —
Source date: 2026-09-24 — URL: as A2-49 — Archived: `ia_byte_1981/` — Tier: 1 — Class: FACT
(documented absence) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High — Corroboration: 1 —
Conflicts: None. **Interpretive consequence (§14 record-selection null): the trade press of the IPO
moment carried the numbers and none of the story. The founding narrative that everyone repeats was
therefore not transmitted by the periodical record of 1975–1981 at all; it arrives later, from memoir
and from the company's own retrospective pages. Stage 1's job is accordingly to report what print knew,
and to mark the story's absence as the datum — not to fill it from 2006.**

---

## Founder state as evidenced in print

The rule applied here: a founder's state is admissible only as *what print said about him, when it
said it*. Nothing in this section is a biography claim; every line is a dated utterance by somebody
who was in the room or in the trade.

A2-56 Claim: **What the trade press knew of Steve Jobs in 1976 was his name, his company's name and
his presence at a trade show — nothing else. In the whole of BYTE's twelve 1976 issues and the
Homebrew run 1975-11 → 1977-01, the only Jobs utterance about him is Helmers' one clause (A2-15),
and it carries no age, no employer, no school, no city and no role** — Date: 1976-12 (publication) —
Source: as A2-15 — Source date: December 1976 — URL: as A2-15 — Archived: as A2-15 — Tier: 1 — Class:
FACT (documented extent of knowledge) — Passage: "Steven Jobs (Apple Computer Co)" — Conf: High —
Corroboration: 1 — Conflicts: None. **Positive identity evidence for Jobs in this corpus is therefore
exactly two dated items: this clause and Helmers' 1976-11-20 Palo Alto motel-room sighting (A2-31).
Everything else commonly stated about Jobs's 1976 state — Atari employment, Reed College, the VW bus,
blue boxes — has zero occurrences in these files (documented negatives; see §Data gaps DG-6, DG-7).**

A2-57 Claim: **Wozniak's printed founder state in 1976–77 is technical, first-person and
address-bearing, and it never mentions an employer.** He is named as "our special guest"
's transport provider in April 1976 (A2-19); he is described by the editor in April 1977 as
"designer of the Apple-U [II] computer" (A2-32); and in May 1977 he publishes under "Stephen Wozniak /
Apple Computer Co / 20863 Stevens Creek Blvd B3-C / Cupertino CA 95014" (A2-25) — Date: 1976-04-30 →
1977-05 — Source: as A2-19, A2-32, A2-25 — Source date: 1976-04 … 1977-05 — URL: as cited —
Archived: `ia_homebrew/hcc0204.txt`, `ia_byte_1977/byte-1977-04.txt`, `ia_byte_1977/byte-1977-05.txt`
— Tier: 1 — Class: CONTEMPORARY OBSERVATION (1976) + FOUNDER CLAIM (1977 byline) — Passage: "Stephen
Wozniak / Apple Computer Co / 20863 Stevens Creek Blvd B3-C / Cupertino CA 95014" — Conf: High —
Corroboration: 3 documents, 2 publishers (BYTE, Homebrew) — Conflicts: None. **A grep of every cached
1975–77 file for `Hewlett`, `Packard` and `HP-65` returns only calculator and component advertising and
review matter (e.g. BYTE April 1976: "the HP-65 retails for $795"); no printed source in this corpus
connects either founder to Hewlett-Packard. Wozniak's HP employment, on which the capital-raising
anecdote depends, is therefore memoir-only *within this corpus*.**

A2-58 Claim: **The company's own 1977 address of record sits two building-numbers from another
Cupertino microcomputer firm, on the same private drive — the physical host of the corporation is
observable in third-party print** — Date: 1977-04 / 1977-05 / 1977-06 — Source: BYTE, April 1977
"Shepardson Microsystems Inc, 20823 Stevens Creek Blvd, Bldg C4-H, Cupertino CA 95014" (line ~8250
region of the "What's New?" column); Wozniak's byline (A2-25); Apple's advertisement (A2-27) — Source
date: 1977-04 … 1977-06 — URL: as cited — Archived: `ia_byte_1977/` — Tier: 1 — Class: FACT (as
printed) — Passage: "The company which makes this device is Shepardson Microsystems Inc, 20863?
[printed: 20823] Stevens Creek Blvd, Bldg C4-H, Cupertino CA 95014." — Conf: High — Corroboration: 2
independent documents naming the same Stevens Creek complex in adjacent months — Conflicts: None.
**Consequence for §G (supply/host side), with no hindsight: in April–June 1977 the address block
holding Apple's Bldg. B3-C also held a PROM-programmer and firmware supplier, and 1976 print placed
Hewlett-Packard-calibre neighbours in the same zip code. Apple's first "factory" was an office-park
suite inside a supplier cluster, not a garage, and the corpus shows the company using that address as
its only published point of contact (A2-27, A2-29).**

A2-59 Claim: **A contemporaneous, non-company witness places both founders working *in* the machine
rather than selling it**: the 1976-11-20 session described by Helmers has the two founders and the
editor writing and debugging a game on the prototype that evening, with Wozniak re-coding it into
6502 assembly afterwards — the division of labour observable in print is designer-plus-programmer
(Wozniak) and a co-presence whose function is not stated (Jobs) — Date: 1976-11-20 (event) / 1977-04
(publication) — Source: as A2-31 — Source date: April 1977 — URL: as A2-31 — Archived: as A2-31 —
Tier: 1 — Class: CONTEMPORARY OBSERVATION — Passage: "Later, Steve Wozniak recoded the program using
the 6502 processor's assembly language facility as implemented in the Apple-ll, and reports that the
Color Eater now runs like lightning, which is its normal mode of operation these days as a
demonstration program for the Apple-ll." — Conf: Medium-High — Corroboration: 1 (single witness) —
Conflicts: None. **Note carefully what the print does *not* say about Jobs in the founders' own
documents: neither Wozniak's May 1977 article nor Apple's June 1977 advertisement attributes any
function to Jobs. The famous role division is absent from every 1976–77 text on disk.**

A2-60 Claim: **Ages and status as the company's own first public pricing was printed: Jobs 25,
Wozniak 30, Markkula 32** — the only ages in the corpus, and they are 1981 print, not 1976 — Date:
1981-02 — Source: as A2-51 — Source date: February 1981 — URL: as A2-51 — Archived: as A2-51 — Tier: 1
— Class: FACT (as printed; `RETROSPECTIVE SOURCE` for 1976) — Passage: "Steve Jobs, 25 years old, and
Steve Wozniak, 30 years old, the creators of the Apple computer… A C Markkula, 32 years old…" — Conf:
High — Corroboration: 1 — Conflicts: None. Arithmetic (DERIVED, backward from the printed ages to the
founding month): if both were 25 and 30 in February 1981, then at the 1976-04-01 partnership they were
approximately **20.3 and 25.5** — `Feb 1981 − 25 yr = c. 1955-02`, so at Apr 1976 age ≈ 21; `Feb 1981 −
30 yr = c. 1950-08`, so at Apr 1976 age ≈ 25.6 (printed ages are integers, so ±1 year is the honest
band). **Markkula, at 32 the oldest named principal in 1981 print, is the only one of the three with no
appearance anywhere in the 1976–77 corpus (documented negative — see §Data gaps DG-5).**

A2-61 Claim: **The club's own head-count survey is the best evidence of the social world the founders
moved in, and it is quantified** — Date: 1976-06-09 (event) — Source: Robert Reiling, "Random Data",
Homebrew Computer Club Newsletter Vol 2 No 6 — Source date: 1976-06-09 — URL:
https://archive.org/details/hcc0206 — Archived: `sources/ia_homebrew/hcc0206.txt` — Tier: 1 — Class:
CONTEMPORARY OBSERVATION (an organiser's own count, not an independent one) — Passage: "A survey of
hobbyists attending the June 9th meeting reveals the following distributions of CPUs in use: 8080-53,
6502-18, 8008-6, PDP-8-4, LSI-11-3, Z80-2, 4004-1, PDP1 1/20-1 and TTL-1. That totals 101 systems up
and running out the the group. About 250 hobbyists were at this meeting. A similar survey in the
October 15, 1975 meeting turned up 38 systems with about 80 hobbyists attending that meeting." [sic] —
Conf: Medium-High — Corroboration: 1 (self-report; no independent count exists — the record-selection
null applies) — Conflicts: None. Arithmetic (DERIVED): the 6502 is `18/101 = 17.8%` of the club's live
systems, second only to the 8080 at `53/101 = 52.5%`; systems per meeting grows `101/38 = 2.66×` and
attendance `250/80 = 3.13×` over about eight months; the club's own newsletter (A2-19) is the venue in
which Apple's machine was circulated to this population in April 1976. **This is what "the market"
meant as knowable in 1976: a countable, self-surveyed, several-hundred-person population, in which
Wozniak's chosen processor was already the second-most-owned.**

A2-61a Claim: **A corpus-wide name census settles how little of the founders is in the periodical
record.** Across the ~13 MB of cached 1976–1981 trade press and club print (30 files), `Wozniak`/
`Wozniac` occurs in **four files only** — BYTE April 1977, BYTE May 1977, BYTE February 1981 and
Homebrew 1976-04-30 — and `Jobs` as a personal name occurs in **three files only** (BYTE December 1976,
BYTE April 1977, BYTE February 1981); there is **no mention of either founder in any 1976 BYTE issue
except the December editorial**, and `Markkula` occurs exactly once in the whole corpus (BYTE February
1981). — Date: 1975-03 → 1981-02 — Source: name census over `sources/ia_byte_1976/`,
`ia_byte_1977/`, `ia_byte_1981/`, `ia_homebrew/` — Source date: 2026-09-24 (this pass) — URL: local
corpus — Archived: `sources/ia_*` — Tier: 1 — Class: FACT (documented extent) — Passage:
"Steven Jobs (Apple Computer Co)" (1976-12) / "Stephen Wozniak / Steve Jobs, 25 years old" (1977-04,
1981-02) / "A C Markkula, 32 years old" (1981-02) — Conf: High — Corroboration: n/a — Conflicts: None.
**The whole of what the contemporary periodical record knew about the people is five documents. This is
the single most important calibration number in the dossier: it means Stage 1 cannot be written from
print about *persons*, only about a product, a price, a channel and a club — and it is why the record-
selection null is stated as a limit on the file's shape, not as an apology.**

A2-61b Claim: **The founders' names are absent from the corpus at the very moment the company is most
present in it.** Neither `Jobs` nor `Wozniak` appears anywhere in BYTE October, November or December
1976's *advertising* pages, nor in any Homebrew issue besides the two Apple items; conversely the brand
"Apple" appears in dealers' pages without any person attached — Date: 1976-09 → 1976-12 — Source:
negative name census cross-tabulated against A2-08…A2-17 — Source date: 2026-09-24 — URL: local corpus
— Archived: `sources/ia_byte_1976/`, `ia_homebrew/` — Tier: 1 — Class: FACT (documented absence within
these files) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High — Corroboration: n/a — Conflicts:
None. Reading, with mechanism named: in 1976 the hobby trade dealt in **brands on dealer pages**, not in
founders; the personal-CEO layer of Apple's story therefore has no periodical foundation before 1977 and
everything said about "Jobs in 1976" is imported from later testimony.

A2-61c Claim: **A dated negative about the founders' prior employers, stated as a census result rather
than as an assumption**: `Hewlett`, `Packard` and `HP-65` occur in the cached 1975–77 files only in
calculator/component contexts, and no cached file connects either founder to Hewlett-Packard or to
Atari (0 occurrences of `Atari` connected to a person; the string appears only as the games/pixel
reference "PONG is a trademark of Atari Inc." in Apple's own July 1977 advertisement) — Date: 1975-03 →
1977-12 — Source: negative census over all cached files; the Atari string appears at
`ia_byte_1977/byte-1977-06.txt` line ~2109 and `byte-1977-07.txt` line ~3970 — Source date: 2026-09-24 —
URL: local corpus — Archived: `sources/ia_*` — Tier: 1 — Class: FACT (documented absence in these files)
— Passage: "PONG is a trademark of Atari Inc." — Conf: High within corpus — Corroboration: n/a —
Conflicts: None. Consequence: the two employment anecdotes on which the founder-state chapter of every
account rests (Wozniak at HP, Jobs at Atari) are **outside this evidence family entirely** and belong to
brief D2's artifact and payroll routes, not to A2.

---

## First product and its stated price and configuration

Consolidated from A2-23…A2-28, A2-34, A2-45…A2-47, A2-53. Table form per §8 (`| Variable | Value |
Source | Confidence |`). "Stated" = as printed; no unprinted attribute is inferred.

| Variable | Value | Source | Confidence |
|---|---|---|---|
| First product's name in print | "Apple-1" / "the new Apple computer" / "APPLE 6502 system" | A2-08 (BYTE 1976-09), A2-14 (1976-11), A2-19 (HCC 1976-04-30) | High |
| Maker's own name for it | "The Apple-I" | A2-25 (Wozniak, BYTE 1977-05) | High |
| Design date, per designer | "designed late in 1975" | A2-25 | Medium (single first-party, uncorroborated) |
| Delivered form | "completely assembled and tested processor board" | A2-26 | High (as stated) |
| Price, per designer | "a price under $700 at the retail level" | A2-26 | Medium (founder's rounded aggregate) |
| Price in any 1976 print | **UNKNOWN — no 1976 document states it** | A2-23 (documented absence) | High that it is absent here |
| Price $666.66 | **absent from every cached file** | §Contradictions U-A2-4 | High (within corpus) |
| Function set as originally intended | "originally intended as a television terminal product which could also operate in a stand alone mode" | A2-26 | Medium (founder claim) |
| Processor | 6502 (third-party print, April 1976; company print, May 1977) | A2-19, A2-34 | High |
| Distribution as stated by maker | "by word of mouth throughout California and later nationwide through retail computer stores" | A2-25 | High (as stated) |
| Successor's name | "Apple-II" / "Apple II" / "Apple-ll" (OCR) | A2-27, A2-31 | High |
| Successor's introduction | "to be introduced in April at the first West Coast Computer Faire in San Francisco" | A2-31; billed dates A2-41 | High |
| Successor's advertised form | "completely self-contained computer system with BASIC in ROM, color graphics, ASCII keyboard, lightweight, efficient switching power supply and molded case" | A2-27 | High |
| Successor's price ladder | 4K $1,298 → 48K $2,638 (system); $598 → $1,938 (board-only) | A2-28 + arithmetic | High |
| ROM/RAM shipped | 8K ROM supplied (up to 12K), 4K RAM supplied (up to 48K advertised) | A2-27, A2-34 | High |
| Display modes | 5 software-selectable; text 40×24 upper case; colour 40h×48v, **15 colours**; hi-res 280h×192v, 4 colours, 12K RAM minimum | A2-27 | High (as advertised) |
| Cassette rate | ad: "1500 bps"; designer's article: "averages over 180 bytes per second", compatible with Apple-I scheme | A2-27 vs A2-34 | High that both were printed; see U-A2-12 |
| Slots | 8-slot motherboard, fully buffered bus, prioritised interrupts, two DMA schemes | A2-27, A2-34 | High |
| Supplied accessories | two game paddles + demonstration cassette; keyboard built into the system version | A2-27 | High |
| What the buyer still had to buy | a television and "an inexpensive modulator (not supplied)" | A2-27 | High |
| Employees / headcount in 1976–77 print | **UNKNOWN — no figure printed; four contributor names only (A2-33)** | A2-33, §Data gaps | High that it is absent |

**Hindsight guard on this table.** Every row is a printed statement from 1976–77. The 1980 rows
(64K/128K, Pascal, "4 or 8 slots") appear only in A2-53 and are deliberately excluded from this table;
importing them into the 1977 configuration would be the exact §6 violation this file exists to avoid.
Symmetrically, the Apple-I's attributes must not be read off the Apple-II rows: the only 1976 statement
about the first machine's internals is that it integrated "display generation circuitry, microprocessor,
memory and power supply on the same board" (A2-25) and shared its cassette scheme with its successor
(A2-34).

## First customers, orders and dealers named in print

A2-62 Claim: **The corpus names dealers who carried the product and never names an order.** Across
1976–77 print the Apple-1 is present in the stock lists of at least four separately-owned retail
concerns (Computer Mart of New York, Inc.; the Berkeley mail-order operation Kentucky Fried Computers;
the New York advertiser carrying "FOLLOWING ITEMS IN STOCK … APPLE"; Lillipute's Computer Mart of
Skokie, Illinois) and in the Byte Shop chain's directory — while **no document in these files records a
purchase, a quantity, an invoice, a shipment, a payment or a credit arrangement between Apple and any
of them** — Date: 1976-09 → 1977-05 — Source: A2-08, A2-11, A2-12, A2-17, A2-37, A2-38, A2-42
(`ia_byte_1976/`, `ia_byte_1977/`) — Source date: 1976-09 … 1977-05 — URL: as cited — Archived: as
cited — Tier: 1 — Class: FACT (documented extent) — Passage: NO_VERBATIM_PASSAGE_RECORDED (negative) —
Conf: High — Corroboration: n/a — Conflicts: U-A2-2.

A2-63 Claim: **The Skokie, Illinois dealer is the third named independent carrier of the Apple brand
in print and it appears as a *new* outlet** — "NEWEST CHICAGOLAND AND MIDWEST DEALER OF IMSAI, SWTPC,
APPLE, VECTOR 1, TDL, Z-80, TARBELL, SANYO CRTS, KEYBOARDS: WE GOT 'EM," at 4446 Oakton St, Skokie IL
60076, (312) 674-1383, "Ask for ED CURTIS Mgr." — Date: 1977-04 (and May 1977) — Source: BYTE, April
1977 (line ~38318) and May 1977 (line ~43655), advertisements — Source date: 1977-04, 1977-05 — URL:
https://archive.org/details/byte-magazine-1977-04 ; …/byte-magazine-1977-05 — Archived:
`ia_byte_1977/byte-1977-04.txt`, `byte-1977-05.txt` — Tier: 1 — Class: FACT — Passage: as quoted; the
same page also advertises "THE NEWEST MICROCOMPUTER THE GULLIVER 1 at OUR STORE, NOW!" — Corroboration:
2 months, 1 advertiser — Conflicts: None. Distribution reading: a Midwest store describing itself as
newspaper-fresh and already listing Apple alongside eight other lines by April 1977 is evidence that
**Apple's 1977 distribution was being built by general-line electronics jobbers adding the brand, not
by Apple opening outlets** — and the same ad proves those jobbers were simultaneously introducing a
*competing new machine*, which is the actual competitive condition of the channel.

A2-64 Claim: **The Apple-1's East-Coast carrier is documented as a multi-line hobby shop that moved
into a dedicated showroom in 1977, and its keeper is named in print** — Date: 1976-06 → 1977-05 —
Source: BYTE June 1976 hobby column (line ~22102), BYTE September 1976 advertisement (A2-08), BYTE May
1977 advertisement (A2-38) — Source date: 1976-06 … 1977-05 — URL: as cited — Archived:
`ia_byte_1976/byte-1976-06.txt`, `byte-1976-09.txt`, `ia_byte_1977/byte-1977-05.txt` — Tier: 1 — Class:
FACT (three documents) / third-party FOUNDER-CLAIM-analogue for the primacy assertion — Passage:
"Stanley Veit, storekeeper of the Computer Mart of New York, Inc, 314 Fifth Av, New York NY 10001,
will send you a free copy of a Motorola M6800 operation codes table" (June 1976) → "Take a byte out of
the new Apple-1 computer" (Sept 1976) → "Last year we opened the first computer store on the East
Coast. This year we move out of the Hobby Store and into our new Real Systems Showroom" (May 1977) —
Conf: High — Corroboration: 3 documents, 2 publishers (BYTE's own column and the store's own ad) —
Conflicts: U-A2-5 (primacy). **This chain is the dossier's cleanest example of how a "first customer"
story can be *almost* supported by print: the store, the date, the address, the keeper and the product
line all exist in-window; the transaction does not.**

## Distribution channels advertised

| Channel | First print appearance recovered | What the print actually shows | Record | Confidence |
|---|---|---|---|---|
| Multi-line hobby/electronics retailer (East Coast) | BYTE 1976-09 | Apple-1 advertised in stock beside 10 competitor brands; no Apple involvement visible | A2-08, A2-09, A2-38 | High |
| Bay Area franchise computer-store chain | BYTE 1976-07 ("world's first computer store franchise"); directory 1977-04 | ~35 outlets, 22 jurisdictions, named managers, parent entity in Sunnyvale, Tokyo and Vancouver listed | A2-07, A2-35, A2-36 | High |
| Mail order by an independent dealer | BYTE 1976-11 | 10% off list, +2% carriage, 3-week cheque clearance; Apple-1 starred | A2-12, A2-40 | High |
| Storeless telephone/mail kit business selling into a club | HCC 1976-06-09 | Kentucky Fried Computers pre-store; club-member discount with an expiry date | A2-39 | High |
| Manufacturer direct mail order (own order form, postage paid, free case) | BYTE 1977-06 | Apple's own printed order form to a Cupertino suite | A2-29 | High |
| Manufacturer-referred dealer network ("the Apple II dealer nearest you", phone) | BYTE 1977-06 | Apple acts as a clearing house for its own resellers | A2-27 | High |
| Trade show / maker faire exhibition | BYTE 1976-12 exhibitor list; HCC 1976-12-10 dates; BYTE 1977-04 booth invite | Apple committed to the Faire by December 1976; booth invited-to in April 1977; 200 billed exhibitors | A2-16, A2-32, A2-41, A2-42 | High |
| Trade-show floor contact with peers and retailers | BYTE 1976-12 (WESCON, September 1976) | Jobs and Terrell named as peers at the same show floor | A2-15 | High |
| National chain franchising (non-Apple) | BYTE 1977-04 column; BYTE 1977-07 Faire report | Computer Shack's "double or quadruple" franchise plan; Radio Shack franchisees shopping the category | A2-66, A2-44 | High (as printed intentions) |
| Peripheral-maker distribution riding the host brand | BYTE 1980-12 | "over 250 locations nationally, including most that carry the Apple" | A2-54 | Medium (competitor's own count) |

A2-65 Claim: **A channel the corpus shows Apple *not* using in 1976: the maker's own advertising, its
own price, its own address, its own telephone.** Cross-reference A2-18 (no Apple-placed BYTE
advertisement in 1976) with A2-27 (the first one, June 1977, is a full three-page-equivalent front-of
book placement in July) — the company's printed commercial voice begins nine months after the machine
is observable in dealers' hands — Date: 1976 → 1977-06 — Source: as cited — Source date: n/a — URL:
n/a — Archived: `ia_byte_1976/`, `ia_byte_1977/` — Tier: 1 — Class: INFERENCE from two documented
absences — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: Medium — Corroboration: n/a — Conflicts: None.
Mechanism UNKNOWN: the corpus cannot say whether Apple did not advertise in 1976 for money, for
capacity, or because a partnership of three with no product literature had nothing to print; those are
the three available explanations and none is evidenced.

A2-66 Claim: **Franchising was the loud, live channel thesis of 1976–77 print, and it was being
applied to computer retail by others at the moment Apple's product first appeared on dealer pages** —
Date: 1977-04 — Source: BYTE, April 1977, "Two Computers in Every Home, Motherhood, Pizza, Apple Pie,
et al" (lines ~35030–35060) — Source date: April 1977 — URL: https://archive.org/details/byte-magazine-1977-04
— Archived: `sources/ia_byte_1977/byte-1977-04.txt` — Tier: 1 — Class: CONTEMPORARY OBSERVATION —
Passage: "The latest word we hear is that a firm with the name Computer Shack, tied up in some
nebulous way with the people who bring you another kind of electronics oriented Shack, is planning to
**double or quadruple the present number of computer stores in existence** through a nationwide
franchise program (see advertisements in BYTE, as well as an ad which has run in Computerworld several
times). Here's one of the people responsible, Ed Faber, president of Computer Shack Inc, located at
14860 Wicks Blvd, San Leandro CA 94577." — Conf: High (as printed) — Corroboration: 1 — Conflicts:
None. Market-knowability value: a 1977 columnist could contemplate "doubling or quadrupling" the store
population, which means the population was small and countable — the same page's Byte Shop directory
(A2-35) is that count in concrete form. **No hindsight: this is not evidence that a national channel
was the right answer for Apple; it is evidence that in April 1977 several people were trying to build
one, and that Apple's first distribution was a subset of that experiment.**

## Competitors as advertised at the time (not as remembered)

A2-67 Claim: **The competitive set as printed, taken from the stock lists of Apple's own dealers** —
the brand block of the East Coast retailer in October–December 1976, the Skokie list in April 1977, and
Computer Mart's May 1977 list give three independent snapshots of which machines a customer was shown
*alongside* an Apple — Date: 1976-10, 1976-12, 1977-04, 1977-05 — Source: A2-11, A2-17, A2-38, A2-63 —
Source date: 1976-10 … 1977-05 — URL: as cited — Archived: `ia_byte_1976/byte-1976-10.txt`,
`byte-1976-12.txt`, `ia_byte_1977/byte-1977-04.txt`, `byte-1977-05.txt` — Tier: 1 — Class: FACT (as
printed) — Passage: "IMSAI, SWTPCo, Digital Group / Processor Tech, Apple, OSI / TDL-Z-80, Seals,
Cromemco, / Sphere, Tarbell, Oliver" (Oct–Dec 1976); "IMSAI, SWTPC, APPLE, VECTOR 1, TDL, Z-80,
TARBELL, SANYO CRTS" (Apr 1977); "IMSAI, PROCESSOR TECHNOLOGY, SOUTH WEST TECHNICAL PRODUCTS, DIGITAL
GROUP, OSI, VECTOR GRAPHICS, ALPHA MICRO TECHNOLOGY, MSI, CROMEMCO, COMPUCOLOR, POLYMORPHIC SYSTEMS,
SOROC TERMINALS, SEALS, TARBELL, MORROW, TDL, NORTH STAR, QUAY, APPLE, OLIVER, SMOKE SIGNAL, MULLEN,
GBC MONITORS, O.K. MACH. CONT. SPEC. VECTOR, E&L INST" (May 1977) — Conf: High — Corroboration: 3
retailers, 4 printings — Conflicts: None. **Note the structural fact: in every one of these lists Apple
is one brand inside a page-length inventory dominated by bus-based S-100 suppliers and terminal makers.
The May 1977 list contains 25 named lines, of which Apple is the 17th — `1/25 = 4%` of shelf
advertising share at a store that had carried the machine since September 1976. Recorded as a print
observation of relative prominence, which is all this corpus can measure.**

A2-68 Claim: **Competitor machines with printed prices in the same months as Apple's first print** —
Date: 1976-06 → 1977-06 — Source: Homebrew 1976-06-09 news item; BYTE November 1976; BYTE April 1977;
BYTE June 1977 — Source date: as listed — URL: as cited — Archived: as cited — Tier: 1 — Class: FACT
(advertising as printed) — Passage: "Electronic Tool Co. has recently introduced a complete
microcomputer system, based on the MOS Technology 6502 CPU, for $675 … comes with a 40-key keyboard, a
programmable 8-digit display, I/O interfaces, power supply and more. All systems are fully assembled,
tested and ready to run." (HCC 1976-06-09, Hawthorne CA item) / Sol-20 "$995 in kit form or $1495 fully
assembled and tested" (A2-45) / "IMSAI 8080 … $619.95/22 SLOT MOTHER BOARD; 849.95/WITH Z-80 CPU"
(A2-46) / Xitan alpha 2 "KIT: $1369 ASSEMBLED & TESTED: $1749" (A2-47) — Conf: High — Corroboration:
each row 1 advertiser — Conflicts: None. Arithmetic and reading (DERIVED): the ETC-1000 at **$675** is
the closest printed 6502-based *complete* system to Wozniak's "under $700" claim for what was, by his
own description, a *board* (A2-26); the 1976 assembled-machine band in these documents runs **$675 →
$1,495**, and the 1977 Apple II system band runs **$1,298 → $2,638** (A2-28). **The honest in-period
statement is therefore: Apple's first product was priced inside an existing 6502-system band, and its
second product was priced at the top of it.** Nothing in this supports or undercuts the choice.

A2-69 Claim: **The category competitor named in the club's own inventory survey was not Apple but the
8080 world** — Date: 1976-06-09 — Source: A2-61 — Source date: 1976-06-09 — URL: as A2-61 — Archived:
as A2-61 — Tier: 1 — Class: CONTEMPORARY OBSERVATION / DERIVED share — Passage: "8080-53, 6502-18,
8008-6, PDP-8-4, LSI-11-3, Z80-2…" — Conf: Medium (self-surveyed) — Corroboration: 1 — Conflicts: None.
Shares: `53/101 = 52.5%` 8080, `18/101 = 17.8%` 6502, `6/101 = 5.9%` 8008, `2/101 = 2.0%` Z80. **This
is the only quantitative competitor-share figure in the corpus for Stage 1, and it measures installed
machines in one club, not sales in a market; §10 flags it as the kind of number that must not be
extrapolated.**

A2-70 Claim: **A competitive naming collision that print records and memory does not: "Zapple" was
another company's product line.** BYTE May 1977 carries Technical Design Laboratories' advertisement
for "THE ZAPPLE MONITOR", "ZAPPLE BASIC … $50", "SUPER BASIC … $95" and "PACKAGE A – THE BASIC &
SUPERBASIC PACKAGE" — Date: 1977-05 — Source: BYTE, May 1977, TDL advertisement (lines ~6128–6315) —
Source date: May 1977 — URL: https://archive.org/details/byte-magazine-1977-05 — Archived:
`sources/ia_byte_1977/byte-1977-05.txt` — Tier: 1 — Class: FACT — Passage: "ZAPPLE BASIC is unique
versatile and powerful and up to 20% faster than comparable Basics. $50" — Conf: High — Corroboration:
2 (the same product family appears in the June and July 1977 Xitan ads, A2-47) — Conflicts: None.
Practical value: **any grep for "apple" in this period returns other firms' trademarked "Zapple" matter,
which is precisely why the token-by-token method in §Working method was necessary.**

## Financial figures as printed, with arithmetic

Consolidation of the printed money in this corpus, with every computed line shown. Per §8 and §13:
`derived_arithmetic` mandatory for DERIVED rows; `UNKNOWN` is a complete value.

| ID | Date | Metric | Value | Unit | Source | Class | Confidence |
|---|---|---|---|---|---|---|---|
| Q1 | 1976-05 | Apple-1 retail price as characterised by designer | "under $700" | USD | A2-26 | FOUNDER CLAIM (contemp.) | Medium |
| Q2 | 1976 (all) | Apple-1 price stated in any 1976 print | UNKNOWN (absent) | USD | A2-23 | UNKNOWN | High (absence) |
| Q3 | 1977-06 | Apple II system 4K / 48K | 1,298 / 2,638 | USD | A2-28 | FACT | High |
| Q4 | 1977-06 | Apple II board-only 4K / 48K | 598 / 1,938 | USD | A2-28 | FACT | High |
| Q5 | 1977-06 | Implied California sales-tax rate | 6.5 | % | A2-28 arithmetic | DERIVED | High (`84.37/1298=0.0650`; 4 rows agree) |
| Q6 | 1977-06 | Assembled-vs-board premium | 700 | USD | A2-28 arithmetic | DERIVED | High (`1298−598`) |
| Q7 | 1977-06 | Marginal factory RAM, 4K→12K | 25 | USD per 1K | A2-28 arithmetic | DERIVED | High (`(1398−1298)/4`) |
| Q8 | 1977-06 | Aftermarket RAM chip sets | 125 (4K) / 600 (16K) | USD | A2-28 | FACT | High |
| Q9 | 1977-06 | Undiscounted equivalent of a 16K set at the stated 20% saving | 750 | USD | A2-28 arithmetic | DERIVED | Medium (`600/0.8`; depends on which price carries the discount — flagged) |
| Q10 | 1977-06 | Company's printed valuation of a free carrying case | 50 | USD | A2-29 | FACT (claim) | High that printed |
| Q11 | 1977-05 | TDL Zapple BASIC / Super Basic | 50 / 95 | USD | A2-70 | FACT | High |
| Q12 | 1976-11 | Sol-20 kit / assembled | 995 / 1,495 | USD | A2-45 | FACT | High |
| Q13 | 1976-06 | ETC-1000 complete 6502 system | 675 | USD | A2-68 | FACT | High |
| Q14 | 1976-06 | Club-member mail-order discount and carriage | 10% off list; +2% | % | A2-39, A2-40 | FACT | High |
| Q15 | 1976-06 | Used-market discount observable in the club's own classifieds | 35 | % | A2-71 | DERIVED | Medium |
| Q16 | 1976-04 | HP-65 retail / street price in period print | 795 / 695 | USD | A2-71 | FACT | High |
| Q17 | 1978 | Sales / profit | 7,800,000 / 793,497 | USD | A2-49 | FACT (as printed) | High |
| Q18 | 1979 | Sales / earnings | 48M / 5M | USD | A2-49 | FACT (as printed) | High |
| Q19 | 1980-09-26 | Sales / profit | 117M / 11.7M | USD | A2-49 | FACT (as printed) | High |
| Q20 | 1978–80 | Net margin per year | 10.17 / 10.4 / 10.0 | % | A2-49 arithmetic | DERIVED | High (`793497/7.8M`; `5/48`; `11.7/117`) |
| Q21 | 1978→1980 | Sales growth | 15.0 | × | A2-49 arithmetic | DERIVED | High (`117/7.8`) |
| Q22 | 1980-12 | Offering price / shares | 22 / 4.6M | USD, shares | A2-50 | FACT (as printed) | High |
| Q23 | 1980-12 | Gross offer on the printed share count | 101,200,000 | USD | A2-50 arithmetic | DERIVED | High (`4.6M × 22`) |
| Q24 | 1980-12 | Gross offer on the printed 8% | 92,240,000 | USD | A2-50 arithmetic | DERIVED | High (`0.08 × 52.4M × 22`) |
| Q25 | 1980-12 | Printed share-count/percentage inconsistency | 408,000 shares; 8.78% vs 8% | shares, % | A2-50 arithmetic | DERIVED | High (`4.6/52.4=0.0878`) |
| Q26 | 1981-02 | Value of one founder's stake at the offer price | 182,600,000 | USD | A2-51 arithmetic | DERIVED | High (`8.3M × 22`) |
| Q27 | 1981-02 | Named three 8.3M holders' combined stake | 47.5 | % | A2-51 arithmetic | DERIVED | High (`24.9/52.4`) |
| Q28 | 1980-12 | Dealer-circuit estimate by a third-party peripheral maker | >250 | locations | A2-54 | CONTEMPORARY OBSERVATION | Medium |
| Q29 | 1976-10 | Magazine's own retail stocking claim | >250 | stores | A2-10 | CONTEMPORARY OBSERVATION | High that printed |
| Q30 | 1976-04→10 | Apple revenue, 1976 | **UNKNOWN — no contemporaneous figure exists in this corpus** | USD | A2-23, AP-35 | UNKNOWN | High (absence) |

A2-71 Claim: **The corpus contains the period's only usable cross-check on the founders'
capital-raising memoir, and it is arithmetic rather than testimony: contemporaneous print prices the
HP-65 calculator that Wozniak later said he sold for $500, and prints the used-computer discount rate
actually prevailing in the club's own classifieds** — Date: 1976-04 (price article) / 1976-06-09
(classified) — Source: BYTE April 1976 calculator comparison (lines ~6525–6545); Homebrew 1976-06-09
"BULLETIN BOARD" (line ~286) — Source date: 1976-04, 1976-06-09 — URL:
https://archive.org/details/byte-magazine-1976-04 ; https://archive.org/details/hcc0206 — Archived:
`sources/ia_byte_1976/byte-1976-04.txt`, `sources/ia_homebrew/hcc0206.txt` — Tier: 1 — Class: FACT (the
printed prices) / DERIVED (the ratios) — Passage: "the SR-52 retails for $395 while the HP-65 retails
for $795 (although it can sometimes be obtained for $695 if one looks hard enough)" / "For Sale: IMSAI
system … Total retail price is $3,066.58 … I am asking $2,000 for the complete system … a savings of
35%." — Conf: High — Corroboration: 2 independent items in 2 publications — Conflicts: None.
Arithmetic (DERIVED): `500 / 795 = 62.9%` and `500 / 695 = 71.9%` of the printed prices; the club's own
used-system ask implies `2000 / 3066.58 = 65.2%` of retail, i.e. a **34.8% used-market discount**. **So
what: the $500 HP-65 figure (FOUNDER CLAIM, retrospective, 2006 — AP-32) is not contradicted by
contemporaneous print; it lands within 7 percentage points of the only used-market discount rate this
corpus can independently observe (`62.9%` vs `65.2%` of retail). That is not corroboration of the
event — it is a plausibility bound on the number, and it is the most that periodical evidence can do for
this anecdote. The event itself remains UNCORROBORATED.**

## Terminated or failed things (mandatory negative section)

§2 and §10 require the dead options, not just the surviving one. All of the following are print
observations.

A2-72 Claim: **The Apple-1 disappears from its maker's own print the moment the maker begins to
advertise.** Apple's June and July 1977 advertisements offer only the Apple II (system or board-only);
the Apple-I is absent from the price ladder (A2-28), from the specification box (A2-27), and from the
order form — while Wozniak's May 1977 article had already put it in the past tense ("was designed",
"was sold") and reused only its cassette protocol — Date: 1977-05 → 1977-07 — Source: A2-25, A2-27,
A2-28, A2-29 — Source date: May–July 1977 — URL: as cited — Archived: `ia_byte_1977/` — Tier: 1 —
Class: FACT (documented presence/absence in the company's own advertising) — Passage: "Apple-I was sold
as a completely assembled and tested processor board…" (past tense, May 1977) against an all-Apple-II
price list (June 1977) — Conf: High — Corroboration: 2 documents, same company — Conflicts: None. No
terminated-product notice, no trade-in or upgrade offer, and no clearance of Apple-I stock appears in
any cached file: **the first product's ending is visible only as silence in the maker's own price
list**, which is precisely the kind of interior decision this archive cannot recover (§2 record-
selection null).

A2-73 Claim: **The third signatory is absent from every 1976–81 document in this corpus** — Ronald
Wayne appears nowhere in the twelve 1976 BYTE issues, the four 1977 issues, the thirteen Homebrew
items, the Faire flyer, or the December 1980 and February 1981 issues — Date: 1975-03 → 1981-02 —
Source: negative grep of all 30 cached periodical files for `Wayne` — Source date: 2026-09-24 (this
pass) — URL: local corpus — Archived: `sources/ia_*` — Tier: 1 — Class: FACT (documented absence) —
Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High within these files; **Medium overall, because
Wayne's name is a plausible target for OCR mangling and because BYTE printed no partnership news at
all** — Corroboration: 1 corpus — Conflicts: none in print (the 1976-04-01 agreement exists per AP-20,
outside this corpus). **The terminated thing here is a person's presence in the record. The
"12%"/"12 days" lore (AP-20) has no periodical footprint at all in the years immediately after the
partnership, which means the Wayne story enters history entirely through later testimony — a fact about
the archive, not about Wayne.**

A2-74 Claim: **The partnership-era name form dies in print.** 1976 print uses "Apple Computer Co"
(BYTE December 1976) and "Apple Computers" (Homebrew September 1976; BYTE December 1976); Wozniak's own
May 1977 byline still says "Apple Computer Co"; Apple's own June 1977 advertisement and order form say
"**Apple Computer Inc.**" — and by December 1980 a third-party advertiser is calling the company "the
Apple Corporation" — Date: 1976-09 → 1980-12 — Source: A2-15, A2-16, A2-21, A2-25, A2-27, A2-54 —
Source date: as listed — URL: as listed — Archived: as listed — Tier: 1 — Class: FACT — Passage: the
four name forms as quoted — Conf: High — Corroboration: multiple documents — Conflicts: U-A2-1. What is
*not* in the corpus: **no 1976 or 1977 document names the partnership, its formation date, its three
partners, or its conversion; the word "partnership" does not occur in connection with Apple in any
cached file.** The legal transition at 1977-01-03 is invisible in periodical print and reaches us only
through the corporation's own 1994 filing sentence and the two-word 1981 clause "incorporated in 1977"
(AP-04, A2-49).

A2-75 Claim: **Dead ends visible in the period's print that this stage file should carry so the
survivor's path is not read as the obvious one**: a "complete microcomputer system … for $675" from an
electrical-tools company (ETC-1000, Hawthorne CA, June 1976); "the GULLIVER 1 at OUR STORE, NOW!"
promoted by the same Skokie dealer that stocked Apple (April 1977); Vector 1, Quantum/Seals, Tarbell,
Oliver, Polymorphic Systems, Morrow, Quay Corp, Compucolor, Alpha Micro Technology and Smoke Signal
listed as stocked lines (A2-67); "BABY by STM Systems" named in the same technical sentence as "the new
Apple computer" (A2-14); and a MITS-style product line printed with the words "(Discontinued; limited
to stock on hand.)" in September and October 1976 — Date: 1976-06 → 1977-05 — Source: A2-68, A2-63,
A2-67, A2-14; BYTE September and October 1976 lines ~3244 / ~30440 — Source date: as listed — URL: as
listed — Archived: as listed — Tier: 1 — Class: FACT (as printed) — Passage: "(Discontinued; limited to
stock on hand.)" — Conf: High — Corroboration: n/a — Conflicts: None. **Interpretive coda, with
mechanism: the hobby market's print of 1976–77 is full of machines and dealers that were gone within
five years; the corpus's own later issues show a large part of this advertising base absent by December
1980. That is a documented churn observation in a periodical record, and it is offered as the
denominator against which Apple's 1976 dealer presence should be read — not as evidence that Apple's
product choices were superior (mechanism UNKNOWN; §2 forbids the inference).**

A2-76 Claim: **The club newsletter that constitutes the only non-company primary source for Stage 1
had already stopped reporting the founding period by the time the company existed**: the cached run has
no Apple body-reference before 1976-04-30, no reference at all in 1975-11 → 1977-01 apart from the two
April/September 1976 items and one user letter, and no reference to the partnership, the incorporation,
the Byte Shop, or any transaction — Date: 1975-11-30 → 1977-01-19 — Source: negatives at A2-05, A2-06,
A2-23, A2-62 — Source date: 2026-09-24 — URL: as cited — Archived: `sources/ia_homebrew/` — Tier: 1 —
Class: FACT (documented absence) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High — Corroboration:
n/a — Conflicts: None. Bound: the newsletter was a 4–8 page volunteer bulletin, not a trade weekly, so
its silence is weak evidence about events — **but it is the silence that the "immediate orders at
Homebrew" story has to survive.**

A2-77 Claim: **A methodological termination: the probe's own provenance headers now contaminate every
future grep of this archive** (A2-05). Any re-run that counts `apple` in `sources/ia_homebrew/*.txt`
without excluding lines 1–5 will report a false positive in ten of thirteen files, including all five
issues on which AP-26's null rests. — Date: 2026-09-24 — Source: this pass — URL: n/a — Archived: n/a —
Tier: n/a — Class: FACT — Passage: as A2-05 — Conf: High — Corroboration: n/a — Conflicts: None.
Recorded so the next agent does not spend a pass rediscovering it.

## Timeline

Only events this corpus can date, from this corpus. No entry is sourced to later memory. `Class` per
§3; `Conf` per §3.

| Date | Event as printed | Record | Class | Conf |
|---|---|---|---|---|
| 1975-10-15 | Homebrew's own survey counts 38 live systems at a meeting of ~80 hobbyists | A2-61 | CONTEMPORARY OBSERVATION | Medium-High |
| 1975 (late) | "The Apple-I … was designed late in 1975" — designer's own dated-in-print claim | A2-25 | FOUNDER CLAIM (contemporaneous) | Medium |
| 1976-04 | "In April the APPLE 6502 system was our special guest. We are grateful to STEVE WOZNIAK for providing transportation." (Sonoma County club letter, reprinted by Homebrew) | A2-19, A2-20 | CONTEMPORARY OBSERVATION | High |
| 1976-04-30 | Earliest Apple body-reference in the club's printed record | A2-19 | FACT (document) | High |
| 1976-06 | Electronic Tool Co. markets a complete 6502 system at $675 | A2-68 | FACT (as printed) | High |
| 1976-06-09 | Homebrew survey: 101 live systems, 18 of them 6502 (~250 attendees); Kentucky Fried Computers advertises club-member mail order, no store yet | A2-61, A2-39 | CONTEMPORARY OBSERVATION | Medium-High |
| 1976-07 | BYTE prints "Paul Terrell, founder of the BYTE Shop, the world's first computer store franchise" | A2-07 | CONTEMPORARY OBSERVATION / third-party primacy claim | High that printed |
| 1976-09 | **Earliest Apple-1 retail advertisement recovered: Computer Mart of New York, 314 Fifth Ave** | A2-08 | FACT | High |
| 1976-09 | BYTE distributor list prints the Byte Shop's first two store addresses | A2-09 | FACT | High |
| 1976-09 (WESCON, Los Angeles) | Helmers converses with "Steven Jobs (Apple Computer Co)" and "Paul Terrell (Byte Shops)" on the show floor | A2-15 | CONTEMPORARY OBSERVATION | High |
| 1976-10 | Retailer brand block lists Apple among 11 makes; Business Week of 1976-07-12 reported to have featured the Byte Shop | A2-11, A2-10 | FACT / OBSERVATION | High |
| 1976-11 | Kentucky Fried Computers (Berkeley) offers the Apple-1 by mail order at 10% off list, p 75; BYTE technical article calls it "the new Apple computer"; Byte Shop shown as a 6-store Bay Area chain | A2-12, A2-14, A2-13 | FACT / OBSERVATION | High |
| 1976-11-20 | "I first saw the Apple-ll on November 20 1976 when Stephen Wozniak and Stephen Jobs stopped by a motel room in Palo Alto"; same-evening BASIC session | A2-31, A2-59 | CONTEMPORARY OBSERVATION | High |
| 1976-12 | "Apple Computers" a committed West Coast Computer Faire exhibitor; Faire billed for April 15-17, 1977 at the San Francisco Civic Auditorium | A2-16, A2-41 | FACT | High |
| 1977-01-03 | *Stage boundary — not in this corpus.* Corporation formed under California law (Apple's own 1994 filing, AP-04); 1981 print gives only "incorporated in 1977" (A2-49) | AP-04, A2-49 | FACT (external to corpus) | High |
| 1977-02-16 | Faire flyer circulated through the club: 7,000–10,000 people expected, 200 exhibitors, "Bay Area — Where It All Started" | A2-42 | CONTEMPORARY OBSERVATION | High |
| 1977-04 | BYTE pre-announces the Apple-II introduction at the Faire; prints the national store directory (~35 Byte Shop outlets, 22 jurisdictions incl. Tokyo and Vancouver) | A2-31, A2-32, A2-35, A2-36 | FACT / OBSERVATION | High |
| 1977-04-15/16/17 | First West Coast Computer Faire held; promoter announces 12,800 attendance; Radio Shack Honolulu franchisees attend as prospective stockists | A2-43, A2-44 | OBSERVATION (self-reported count) | Medium |
| 1977-05 | Wozniak's "The Apple-II", BYTE p 3, under an Apple Computer Co Cupertino byline; names four non-founder contributors | A2-25, A2-33, A2-48 | FOUNDER CLAIM (contemporaneous) | High |
| 1977-05 | Computer Mart of New York moves to a new showroom, lists APPLE among ~25 lines, claims East-Coast store primacy; Byte Shop East, Inc. advertises in Levittown NY | A2-38, A2-37 | FACT (as printed) | High |
| 1977-06 | **Apple's first self-published BYTE advertisement: $1,298–$2,638 system / $598–$1,938 board-only, (408) 996-1010, 20863 Stevens Creek Blvd Bldg B3-C, Cupertino**, with direct mail order, postage paid and a free carrying case | A2-27, A2-28, A2-29 | FACT | High |
| 1977-07 | Apple's advertisement re-runs as a 3-page front-of-book placement ("Apple 22, 23, 24") | A2-30 | FACT | High |
| 1978 | Sales $7.8M / profit $793,497 — earliest printed fiscal year for Apple anywhere in this corpus | A2-49 | FACT (as printed, 1981) | High |
| 1979 | Sales $48M / earnings $5M | A2-49 | FACT (as printed) | High |
| 1980-09-26 | Sales $117M / profit $11.7M | A2-49 | FACT (as printed) | High |
| 1980-12 | Apple advertises nationally from 10260 Bandley Drive with a toll-free number; shares go on sale "early in December 1980" | A2-53, A2-50 | FACT | High |
| 1981-02 | BYTE prints the terms, the revenue series and the cap table; **Ronald Wayne appears nowhere in it** | A2-49, A2-50, A2-51, A2-73 | FACT (as printed) | High |

## Data gaps

Vocabulary per the brief: **EMPTY** = looked, nothing there · **UNANSWERED** = attempted, access
failed · **UNTRIED** = not attempted, with the exact query recorded. Web requests spent by this pass:
**0 of 3 permitted** — every UNTRIED row below is deliberately unsearched, and the value of this
dossier is that it is mined.

| ID | Gap | Status | Why missing | Importance | Best available evidence | Follow-up (exact query) |
|---|---|---|---|---|---|---|
| DG-1 | Apple's April–October 1976 revenue; FY1976 and FY1977 figures | **EMPTY in this corpus** | The cached periodicals print no fiscal data for the founding year; the earliest printed year is FY1978 | **HIGH** (§P, §L, the "repeatable validation" rung) | A2-49 (FY1978 $7.8M / $793,497, printed 1981-02); A2-23 | UNTRIED: InfoWorld/Creative Computing IPO-era coverage, archive.org `https://archive.org/advancedsearch.php?q=title%3A%28infoworld%29+AND+date%3A%5B19800101+TO+19811231%5D&fl%5B%5D=identifier&fl%5B%5D=date&rows=200&output=json` then per-item `metadata → items-server *_djvu.txt`, grep `1976`, `fiscal`, `revenue` |
| DG-2 | The first order: buyer, units, price, date, payment | **EMPTY in this corpus** | No invoice, cheque or order document exists in any cached file; the print names dealers who stocked, not a purchase | **HIGH** (§D, §F, first-customer) | A2-08/A2-12 (dealer stock), A2-35 (Byte Shop circuit), A2-62 (the negative) | UNTRIED: auction/museum documentary family — `site:christies.com "Apple Computer Company" partnership` and DigiBarn/CHM finding aids; **do not re-grep the periodicals for this — it is not there** |
| DG-3 | Text of the 1980 registration statement / prospectus | **UNTRIED** (paper-only; EDGAR floor 1994-01-26 per AP-02/AP-07) | Not online; the only plausible primary carrier of FY1976–77 columns | **HIGH** | A2-50 (terms as printed) | UNTRIED: `https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000320193&type=S-1&dateb=&owner=include&count=40&action=getcompany` (expect null) then WorldCat/Research library: `"Apple Computer" prospectus 1980 "Registration No"` |
| DG-4 | The Apple-1's published price in 1976 print (and the $666.66 figure) | **EMPTY here; UNANSWERED at Kilobaud** | Kilobaud 1976 items carry no text layer (AP-34), so the title most likely to hold an Apple-I advertisement cannot be grepped | **HIGH** | A2-26 ("under $700"), A2-28 | UNTRIED: OCR locally after download — `https://archive.org/metadata/Kilobaud197609` → JP2 files → `tesseract`; or Internet Archive full-text `https://archive.org/search?query=%22Apple-I%22%20kilobaud` |
| DG-5 | Mike Markkula in 1976–77 print | **EMPTY** | Zero occurrences of `Markkula` in all 30 cached files; first print appearance is February 1981 | **HIGH** (§K, §B) | A2-51 (age, holding, "took Apple from a garage operation") | UNTRIED: Creative Computing 1977–78 people items — `https://archive.org/advancedsearch.php?q=title%3A%28%22creative+computing%22%29+AND+date%3A%5B19770101+TO+19781231%5D&fl%5B%5D=identifier&output=json` |
| DG-6 | Jobs's employment history, education and residence before April 1976 | **EMPTY** | No payroll, college or directory record in any cached file; the 1973 job application (AP-28) is an auction artifact, not periodical | MED (§B) | A2-56 (the extent of what print knew), A2-28 rows in `apple1registry_stories.txt` | UNTRIED: Reed College archival register index; Atari-era trade advertisements; `CHM catalog "Atari" 1974 technician` |
| DG-7 | The Blue Box venture | **EMPTY** | Zero relevant occurrences across all cached files | MED (§C, §O) | none in corpus | UNTRIED: HCC newsletters not on disk (Vol 1 No 1–No 8, 1975-03…1975-10) — `https://archive.org/advancedsearch.php?q=title%3A%28%22homebrew+computer+club%22%29&fl%5B%5D=identifier&fl%5B%5D=date&rows=200&output=json` then grep each for `blue box`, `phone`, `Touch Tone` |
| DG-8 | Premises: Crist Drive garage ownership; the Cupertino suite's lease | **EMPTY in print; UNANSWERED at the county portals** (Santa Clara County `403` / `000`, AP-36) | Only a records office can answer | MED-HIGH (§G, §E host side) | A2-27/A2-28 (the 1977 address of record), A2-58 (Stevens Creek complex neighbours), A2-53 (1980 Bandley Drive) | UNTRIED: `https://bizfileonline.sos.ca.gov/api/BusinessSearch?enterprise=APPLE+COMPUTER` (endpoint was live, unexercised) |
| DG-9 | Ronald Wayne, the partnership and its dissolution | **EMPTY in periodicals** (A2-73) | BYTE never reported the partnership's formation or its third partner | **HIGH** (§B, §M, §U) | A2-73, A2-74 | UNTRIED: Christie's lot text — `https://www.christies.com/en/lot/lot-*?sc=p&ldsc=GG26` search `"Apple Computer Company" partnership agreement 1976` |
| DG-10 | General-interest press coverage of Apple 1976–1982 | **EMPTY in this corpus; UNTRIED elsewhere** | Cached corpus is trade-only; the probe found only Tier-4 carriers for Rolling Stone/Time | MED | A2-10 (a dated Business Week pointer) | UNTRIED: `"Business Week" July 12 1976 "Byte Shop"` (ProQuest / archive); `chroniclingamerica.loc.gov/lccn/sn83030214/1976-07-12/` (NY Times mirror) |
| DG-11 | **What the July 12, 1976 Business Week article actually said, and whether it named Apple** | **UNTRIED (deliberate)** | Found by mining, not opened: BYTE's October 1976 editorial cites it (A2-10) | **HIGH** — a dated, named general-circulation target inside the stage window, and the only one this dossier produced | A2-10 | UNTRIED, exact route: `https://www.bloomberg.com/businessweek/archive/1976-07-12` index search `computer store`; WorldCat `Business Week 1976-07-12 "computer store"` |
| DG-12 | Homebrew issues not on disk: Vol 1 No 1–8 (1975-03 → 1975-10) and Vol 2 No 8, No 10, No 12, No 14–21 (1976-10 → 1977-12) | **UNTRIED** | Only 13 of 32 enumerated items were cached by the probe | **HIGH** — the 1975-03→10 run is where a late-1975 Apple demo would have been printed | A2-76, A2-05 | UNTRIED: `https://archive.org/advancedsearch.php?q=title%3A%28homebrew+computer+club%29&fl%5B%5D=identifier&fl%5B%5D=date&rows=200&output=json` → for each new id `metadata → items-server/<id>_djvu.txt`, grep with headers excluded |
| DG-13 | BYTE August 1977 → November 1980 (the stage's later half, unmined because uncached) | **UNTRIED** | Not on disk | **HIGH** (§L, §I, §P) | A2-49's 1981 endpoints | UNTRIED: `byte-magazine-1977-08` … `byte-magazine-1980-11` via `https://archive.org/metadata/byte-magazine-1977-08` → items-server, per `_RETRIEVAL_LOG.md` route note |
| DG-14 | Apple's own press releases 1976–1980 | **EMPTY** | Company web record starts 1996-10-22 (AP-08) | LOW-MED | none | UNTRIED: `archive.org` search `"Apple Computer" press release 1977` in text collections; U.S. newspaper back-files via Chronicling America `https://chroniclingamerica.loc.gov/search/pages/results/?andtext=%22Apple+Computer%22&date1=1976&date2=1978` (probe recorded an Arkansas `403` bot-block; expect the same) |
| DG-15 | Any independent count behind the 12,800 Faire attendance and the ">250 locations" dealer figures | **EMPTY — structurally** | Both are self-reports by the party with the interest in the number | MED (§L validation, §P) | A2-43, A2-54, A2-10 | No follow-up: this is the record-selection null, not a retrieval task. Leave UNKNOWN. |

**Record-selection null, stated plainly (§2).** For Apple's Stage 1 the surviving archive is
*somebody else's* paper: a New Hampshire hobby magazine's advertisement pages, a volunteer club
newsletter from a Mountain View postbox, and a Faire flyer. What is unrecoverable *because* the
winners' trace is thin is not merely "the interior" in the abstract — it is nameable: the rejected
options (kit versus assembled was the live 1976 question, and Apple's own 1977 answer survives only as
a price row), the partnership's deliberations, any contemporaneous count of Apple-1 units, any
independent number behind any Apple self-report, and the presence of the third partner. A Stage-1
reconstruction built from this corpus will therefore look strong on **channel, price, and product
text** and empty on **decisions, demand and money** — and that asymmetry is a property of the
archive, not of the company.

## Contradictions

Format per §7: `CLAIM A / CLAIM B / WHY THEY DIFFER / EVIDENCE WEIGHT / BEST-SUPPORTED INTERPRETATION
/ RESIDUAL UNCERTAINTY / CONFIDENCE`. Where print contradicts the famous story, both sides are held.

**U-A2-1 — Which company name was Apple's in 1976–77.** / CLAIM A: 1976 print uses "Apple Computer Co"
(BYTE December 1976, A2-15) and "Apple Computers" (Homebrew 1976-09-15, A2-21; BYTE December 1976,
A2-16); Wozniak still signs "Apple Computer Co" in May 1977 (A2-25). / CLAIM B: Apple's own June 1977
advertisement and order form print "**Apple Computer Inc.**" (A2-27), and a third party in December 1980
calls it "the Apple Corporation" (A2-54). / WHY THEY DIFFER: name forms track the legal sequence
(partnership → 1977-01-03 corporation) with publication lag and sloppy third-party usage; the club and
BYTE printed what people said, not what was registered. / EVIDENCE WEIGHT: the company's own printed
letterhead outranks third-party lists for the corporation; third-party lists outrank everything for
1976. / BEST-SUPPORTED INTERPRETATION: *four name forms are all authentic; "Apple Computers" as a
company name is a 1976 usage, and no 1976–77 document names the partnership at all.* / RESIDUAL: whether
"Apple Computer Company" (the partnership's registered style, per the 1976 agreement in AP-20) ever
appeared in 1976 trade print — it does not in these files. / CONFIDENCE: High on the print facts,
Medium on the inference.

**U-A2-2 — The first customer.** / CLAIM A (the famous story): the Byte Shop ordered a first batch of
Apple-1 boards in mid-1976 at a negotiated price, and that order created the company. / CLAIM B (this
corpus): Wozniak, in his own May 1977 print, attributes distribution to "word of mouth throughout
California and later nationwide through retail computer stores" with **no founding order and no named
buyer** (A2-25); the only dated 1976 retail facts are that **East-Coast and Berkeley dealers advertised
the machine in September and November 1976** (A2-08, A2-12), and the Byte Shop appears in print as a
*chain directory entry* (A2-35) and as a man Helmers spoke to at a show (A2-15). / WHY THEY DIFFER: a
memorable single transaction is easier to transmit than a diffuse dealer ramp; the number attached
later. / EVIDENCE WEIGHT: in-window print (A2-08, A2-25) versus retrospective memoir carried by
third parties. / BEST-SUPPORTED INTERPRETATION: *Apple's first distribution was a multi-dealer ramp
that included the Byte Shop circuit; a specific first order is undocumented in the periodical record,
and the periodical record shows the East Coast advertising the machine as early as anyone.* /
RESIDUAL: high — a document outside periodicals (an invoice, Terrell's own papers, the Christie's
agreement) could still establish the transaction; this dossier neither establishes nor refutes it. /
CONFIDENCE: High that the corpus contains no first order; Low on the canonical version.

**U-A2-3 — The Faire's days.** / CLAIM A: April 15–17, 1977 (the organiser's flyer, A2-42; Homebrew
1976-12-10, A2-41; BYTE April 1977 re-run of the flyer). / CLAIM B: "April 16 and 17 of this year"
(BYTE's post-event report, A2-43). / WHY THEY DIFFER: billing versus a correspondent's memory of the
two days he attended, or a Monday/Tuesday cut. / EVIDENCE WEIGHT: pre-event billing from the promoter
is stronger for the *scheduled* dates; the report is stronger for *what he saw*. / BEST-SUPPORTED:
*scheduled April 15–17, 1977; the reporter's own show days were the 16th and 17th.* / RESIDUAL: whether
Apple's actual booth days overlapped. / CONFIDENCE: Medium-High. (This closes the feasibility probe's
open gap row; see C-6.)

**U-A2-4 — The Apple-1's price.** / CLAIM A (ubiquitous): $666.66. / CLAIM B (this corpus): no
occurrence of `666` in that sense anywhere in the 30 cached files (the only hits are a telephone number
and printer's rules); Wozniak's own 1977 print says "a price under $700 at the retail level" (A2-26);
the only printed list of a comparable 6502 complete system is $675 (A2-68). / WHY THEY DIFFER: the
repeating-decimal price is a cute artifact that circulates by retelling, and it appears in the trade
titles that are *not* text-searchable here (Kilobaud / Creative Computing), not in BYTE. / EVIDENCE
WEIGHT: none in-window either way; DG-4 names where it might still be found. / BEST-SUPPORTED:
*the Apple-1 was sold under $700 at retail per its designer; a specific figure is not established by
this corpus and the famous one is unverified here.* / RESIDUAL: the famous price may well be printed in
an Apple-placed 1976 advertisement in a title this cache does not hold — **recorded as UNANSWERED, not
as false**. / CONFIDENCE: High on absence in these files; UNKNOWN on the true price.

**U-A2-5 — Who was first.** / CLAIM A: BYTE, July 1976 — "Paul Terrell, founder of the BYTE Shop, the
world's first computer store franchise" (A2-07). / CLAIM B: Computer Mart of New York, May 1977 —
"Last year we opened the first computer store on the East Coast" (A2-38). / CLAIM C: the Faire flyer,
February 1977 — "San Francisco Bay Area — Where It All Started" (A2-42). / WHY THEY DIFFER: three
different scopes (franchise / East Coast / region) and three interested speakers — a live primacy
contest inside the period's own print, not a later argument. / EVIDENCE WEIGHT: each claim is
self-serving and uncorroborated by the others; A's publisher was a friend of C's and B's advertiser
(A2-07 vs A2-38 are in the same magazine). / BEST-SUPPORTED: *no primacy statement in this corpus is
established; what is established is that the field was already narrating its own origin in 1976–77.* /
RESIDUAL: which store actually first sold an Apple product (A2-08 puts the earliest *advertisement* in
New York, September 1976). / CONFIDENCE: High on the claims' existence, Low on any of their truth.

**U-A2-6 — The California sales-tax rate.** / CLAIM A: Apple's own June 1977 price table implies
**6.5%** (`84.37/1298`; four rows agree, A2-28). / CLAIM B: Kentucky Fried Computers' June 1976 club
notice says "California residents must add **6%** sales tax" (A2-39), and a December 1980 BYTE
advertiser prints "California residents add **6%** sales tax" (A2-53 region). / WHY THEY DIFFER:
county add-ons differed by district and changed over time; a magazine's advertisers were not uniform;
or Apple's table's internal arithmetic is a rounding coincidence. / EVIDENCE WEIGHT: Apple's table is
internally consistent across nine rows — hard to produce by accident — so the discrepancy is more likely
jurisdictional than clerical. / BEST-SUPPORTED: *Apple's 1977 prices carry a 6.5% Santa Clara County
add-on; the 6% lines belong to other localities (Alameda/LA) and other years.* / RESIDUAL: the actual
1977 district schedule is outside periodicals. / CONFIDENCE: High on the arithmetic, Low on the
explanation. **Why this row earns its place: it is the only place in the entire dossier where the
company's own printed numbers can be audited against the period's other printed numbers.**

**U-A2-7 — The hole where Stage 1's money is.** / CLAIM A: the printed revenue series begins FY1978 at
$7.8M (A2-49). / CLAIM B: the founding period is April 1976 – January 1977. / WHY THEY DIFFER: the
series is an IPO-era investor-relations artefact, not a history; the earliest printed year is two years
after the events this dossier covers. / EVIDENCE WEIGHT: one column. / BEST-SUPPORTED: *Apple's Stage-1
financial interior is UNKNOWN from periodicals; the dossier must not present FY1978 as if it were the
first year.* / RESIDUAL: only the paper prospectus (DG-3) can close it. / CONFIDENCE: High.

**U-A2-8 — Precision mixing inside a single printed series.** `"$793,497"` (to the dollar) sits beside
`"$5 million"`, `"$117 million"`, `"$48 million"`, `"$7.8 million"` in the same 24-line column (A2-49),
and the derived margins land within 0.4 pp of each other (Q20). / WHY THEY DIFFER: the exact FY1978
profit figure plausibly comes from a filing or release, the rounded ones from memory or space
constraints. / EVIDENCE WEIGHT: mixed. / BEST-SUPPORTED: *treat the series as reported, not audited;
quote the rounded years as rounded.* / RESIDUAL: whether an audited FY1979/FY1980 pair exists in the
prospectus. / CONFIDENCE: High on the observation, Medium on any inference from the margin stability.

**U-A2-9 — The offering arithmetic does not close.** / CLAIM A: "8% of the company's 52.4 million
shares". / CLAIM B: "(ie: 4.6 million shares)". / WHY THEY DIFFER: `0.08 × 52.4M = 4.192M`; `4.6/52.4 =
8.78%` — a ~408,000-share gap, i.e. one of the two numbers is rounded, stale, or includes an over-allotment
or a different share class. / EVIDENCE WEIGHT: single column, no filing to check against (DG-3). /
BEST-SUPPORTED: *report both, compute both gross sizes ($101.2M and $92.2M, Q23/Q24), and prefer
neither.* / RESIDUAL: the entire reconciliation. / CONFIDENCE: High that the print is internally
inconsistent. **This is a correction against AP-18, which recorded the same sentence without noticing
the arithmetic (see C-4).**

**U-A2-10 — The three partners versus the visible two.** / CLAIM A: the 1976-04-01 agreement is a
three-signatory document allocating 45/45/10 (AP-20, auction record — outside this corpus). / CLAIM B:
every 1976–1981 document cached here names at most Jobs and Wozniak; Wayne appears nowhere, including
in the February 1981 column that recapitulates the company for public investors (A2-73, A2-51). / WHY
THEY DIFFER: the press covered the company through its visible product and its visible principals; a
partner who left within weeks never entered the trade's reference set. / EVIDENCE WEIGHT: B is
in-window and abundant; A is a single primary artifact with no periodical footprint. / BEST-SUPPORTED:
*the founding partnership's third member is a documentary fact with no contemporaneous print trace; the
origin story as printed from the start was a two-founder story.* / RESIDUAL: whether any 1976 print
anywhere (Kilobaud, a California newspaper) mentions Wayne. / CONFIDENCE: High within this corpus,
Medium absolutely.

**U-A2-11 — "Apple Corporation".** A December 1980 third-party advertisement prints "Apple II, Apple II
Plus, and Applesoft are trademarks of the **Apple Corporation**" (A2-54). / CLAIM B: the corporate name
in Apple's own 1977–1980 print is "Apple Computer Inc." / WHY THEY DIFFER: copywriter error, or the
sloppy naming DG documents across the whole period (U-A2-1). / EVIDENCE WEIGHT: trivial on its own. /
BEST-SUPPORTED: *evidence of how little the corporate name was stabilised in the field even in 1980* /
RESIDUAL: none material. / CONFIDENCE: High that it was printed.

**U-A2-12 — Two cassette transfer rates for one machine.** "1500 bps cassette interface" (Apple's June
1977 specification box, A2-27) versus "averages over 180 bytes per second … compatible with the
interface used with the Apple-I" (Wozniak's May 1977 article, A2-34). / WHY THEY DIFFER: bits versus
bytes — `1500/8 = 187.5` bytes per second, which is exactly "over 180"; the second figure is a
throughput measure of the first. / EVIDENCE WEIGHT: both are company-side and consistent. /
BEST-SUPPORTED: *no conflict of fact; a unit-of-measure conflict — and a live example of §6's rule that
numerals carry their basis.* / RESIDUAL: none. / CONFIDENCE: High. **Recorded because an unwary dossier
would print these as two numbers from two sources.**

**U-A2-13 — Where the company was.** / CLAIM A: the project's universe/feasibility register gives
"1976-04-01, **Los Altos**, California" (AP-04 header row). / CLAIM B: in every cached 1976–77 document
the geography attached to Apple is **Cupertino** (20863 Stevens Creek Blvd B3-C, May–June 1977,
A2-25/A2-27), and the only `Los Altos` strings in the whole cached corpus belong to other
firms — Cromemco at "One First St., Los Altos, CA 94022 • (415) 941-2967" (advertising in BYTE January,
April, May, June and July 1976, and in Homebrew 1975-11-30), an advertiser at "111 Main St., Los Altos,
Ca 94022" and a Los-Altos F.O.B. terms line (BYTE January 1976), Qume at "745 Distel Drive, Los Altos,
Ca. 94022" (Homebrew 1976-06-09), a member at "Los Altos Hills" (Homebrew 1976-12-10), and in December
1980 Slone Associates and publisher William Kaufmann Inc. **All 17 lines containing `Los Altos` in the cached files (grep, 2026-09-24) are third parties; none is Apple.** / WHY THEY DIFFER: the register's place is a
retrospective gloss (the family home's municipality) carried from memoir; the print's place is the
company's own address of record. / EVIDENCE WEIGHT: B is contemporaneous and self-published. /
BEST-SUPPORTED: *Stage-1 print places Apple in Cupertino, in a Stevens Creek office complex next door to
a firmware supplier (A2-58), inside a club circuit headquartered in Mountain View and a dealer chain
parented in Sunnyvale. "Los Altos" has no periodical support in this corpus.* / RESIDUAL: the garage's
municipality is a property-record question (DG-8). / CONFIDENCE: High on the print, Medium on what it
proves about where work was actually done.

## Provenance ledger

Every file read by this pass, with the retrieval route and date as recorded by the caching probe
(`sources/_RETRIEVAL_LOG.md`, access date 2026-09-24), the item identifier, whether the cached text is
a **full issue** or a snippet, and what this dossier used it for. No file in `sources/` was created,
modified, moved, renamed or deleted by this pass; the directory is a protected archive (§14 rule 4).

| Cached file | IA item | Issue / date | Extent | Retrieval route | Access date | Used for |
|---|---|---|---|---|---|---|
| `ia_byte_1976/byte-1976-01.txt` … `byte-1976-12.txt` (12 files, 360–596 KB) | `byte-magazine-1976-01`…`-12` | BYTE Vol 1 Nos 1–12, Jan–Dec 1976 | **full issue OCR** (`*_djvu.txt`), uncorrected | `https://archive.org/metadata/<id>` → items-server `<id>_djvu.txt` (the `download/` form 302s to a CDN that 404'd) | 2026-09-24 | A2-01…A2-24, A2-45, A2-65, A2-72…A2-77 |
| `ia_byte_1977/byte-1977-04.txt` (682 KB) | `byte-magazine-1977-04` | BYTE Vol 2 No 4, **April 1977** (self-dated masthead) | full issue OCR | as above | 2026-09-24 | A2-31, A2-32, A2-35, A2-36, A2-46, A2-58, A2-63, A2-66 |
| `ia_byte_1977/byte-1977-05.txt` (727 KB) | `byte-magazine-1977-05` | BYTE Vol 2 No 5, **May 1977** | full issue OCR | as above | 2026-09-24 | A2-25, A2-26, A2-33, A2-34, A2-37, A2-38, A2-48, A2-70 |
| `ia_byte_1977/byte-1977-06.txt` (797 KB) | `byte-magazine-1977-06` | BYTE Vol 2 No 6, **June 1977** | full issue OCR | as above | 2026-09-24 | A2-27, A2-28, A2-29, A2-47, A2-67 |
| `ia_byte_1977/byte-1977-07.txt` (752 KB) | `byte-magazine-1977-07` | BYTE Vol 2 No 7, **July 1977** | full issue OCR | as above | 2026-09-24 | A2-30, A2-43, A2-44, A2-72 |
| `ia_byte_1981/byte-1980-12.txt` (1.67 MB) | `byte-magazine-1980-12` | BYTE, **December 1980** | full issue OCR | as above | 2026-09-24 | A2-53, A2-54, A2-55, A2-73 |
| `ia_byte_1981/byte-1981-02.txt` (1.62 MB) | `byte-magazine-1981-02` | BYTE, **February 1981** | full issue OCR | as above | 2026-09-24 | A2-49, A2-50, A2-51, A2-52, A2-60 |
| `ia_homebrew/hcc0109.txt`, `hcc0110.txt` | `hcc0109`, `hcc0110` | Homebrew Vol 1 Nos 9, 10 — 1975-11-30, 1975-12-31 | full item OCR | as above | 2026-09-24 | A2-05, A2-76 (nulls), A2-13's Cromemco locator |
| `ia_homebrew/hcc0201.txt`, `hcc0202.txt`, `hcc0203.txt` | `hcc0201–0203` | Vol 2 Nos 1–3 — 1976-01-31, 1976-02-29, 1976-03-31 | full item OCR | as above | 2026-09-24 | A2-05, A2-06 (nulls) |
| `ia_homebrew/hcc0204.txt` | `hcc0204` | Vol 2 No 4 — **1976-04-30** | full item OCR | as above | 2026-09-24 | A2-19, A2-20 |
| `ia_homebrew/hcc0205.txt`, `hcc0206.txt`, `hcc0207.txt` | `hcc0205–0207` | Vol 2 Nos 5–7 — 1976-05, **1976-06-09**, 1976-08-04 | full item OCR | as above | 2026-09-24 | A2-39, A2-61, A2-68; null A2-05 |
| `ia_homebrew/hcc0209.txt` | `hcc0209` | Vol 2 No 9 — **1976-09-15** | full item OCR | as above | 2026-09-24 | A2-21, A2-22 |
| `ia_homebrew/hcc0211.txt`, `hcc0213.txt` | `hcc0211`, `hcc0213` | Vol 2 Nos 11, 13 — 1976-12-10, 1977-01-19 | full item OCR | as above | 2026-09-24 | A2-41 (Faire dates), null A2-05 |
| `ia_homebrew/hcccf.txt` | `hcccf` | West Coast Computer Faire flyer, **1977-02-16** | full item OCR (single flyer) | as above | 2026-09-24 | A2-42 |
| `apple1registry_stories.txt` / `.html` | — (live fetch) | retrospective curation, stories dated Feb–Aug 2022 | single page | direct HTTPS | 2026-09-24 | cited **only** for what is *not* corroborated (A2-56, A2-71, A2-73, DG-6, DG-9) |
| `test_direct.txt` (527 KB) | duplicate of `byte-1976-09` body | — | **do not cite** (per `_RETRIEVAL_LOG.md`: orphan diagnostic) | — | 2026-09-24 | none — recorded so no agent double-counts September 1976 |
| `EDGAR_*`, `probe_edgar_fts_*`, `probe_wayback_APPLE.md` | SEC / Wayback | 1994+ | full documents | curl against documented endpoints | 2026-09-24 | only for the stage boundary (AP-04) and the coverage floors; **not** used as Stage-1 evidence |

**Full-issue versus snippet, stated per §Working method:** every periodical item used here is a
**complete issue or complete item text layer**, not an article snippet or a search-result fragment.
Where a line of an issue is quoted, the page is recoverable only for those issues whose advertiser
index or footer survived OCR (November 1976 p 75; July 1977 pp 22–24; February 1981 p 212; May 1977
p 3). Elsewhere page numbers are recorded as UNKNOWN rather than guessed.

**Provenance risk, priced (§14 rule 6 / brief D6-2).** The dominant witness class in this dossier is
BYTE, and BYTE's editor is a participant: he names Jobs in an editorial (A2-15), hosts a founding-order
adjacent retailer for a year in his own pages, recalls a dated personal demo session (A2-31), places the
designer on page 3 (A2-48), and calls Terrell's chain "the world's first computer store franchise"
(A2-07). **Consequence: this dossier counts BYTE editorial items as ONE origin, and gives independent
weight only to (i) advertisements placed by third parties, (ii) the Homebrew correspondence written by
club members, and (iii) the numbers in Apple's own price table.** Nothing else in this file is
independent of a friendly publisher.

## Outbound corrections

Corrections and extensions owed to `A_chronology_feasibility.md` (records `AP-nn`) and to the Apple row
of `MASTER_RESEARCH_LOG.md`. No other file was touched by this pass.

**C-1 → AP-14 (and its "strongest retrievable dated facts" item 6).** The earliest Apple-1 retail
advertisement is **BYTE September 1976**, not October: Computer Mart of New York's page, "Take a byte
out of the new Apple-1 computer" (A2-08). And the advertiser is **Computer Mart of New York, Inc., 314
Fifth Avenue** — triangulated from BYTE's own June 1976 hobby column naming "Stanley Veit, storekeeper
of the Computer Mart of New York, Inc, 314 Fifth Av" and the September front-matter distributor list
(A2-09, A2-64) — so the probe's store name **"Computer Fan" is an OCR artifact** of a logotype, and
should not be propagated. AP-14's October item remains valid as the *second* month of the same
campaign. Net effect: the first-customer/first-channel ladder gains a month, and its bottom rung is a
New York store, not a California one.

**C-2 → AP-26 (documented absence, Homebrew).** The conclusion stands (no Apple reference in the club's
print before April 1976) but the wording is wrong twice: `hcc0202` (1976-02-29) does contain the string
"apple" — idiomatically, "polishes off the apple" (A2-06); and **every cached file's own provenance
header contains `company_004_apple`**, so any re-run of this grep without excluding header lines will
report a false positive in ten of thirteen Homebrew files (A2-05, A2-77). Recommend the probe's null be
restated as "no *company* reference", with the header caveat.

**C-3 → AP-17 (Apple's June 1977 advertisement).** Extend, do not replace: the advertisement contains a
**complete nine-row price ladder** (4K→48K, system and board-only, plus per-resident tax add-ons),
aftermarket chip-set prices ($125 / $600), a stated "20% savings" on factory memory, direct mail order
with postage paid, a free "$50 value" carrying case, a minimum 4K configuration, and a dealer-referral
telephone line (A2-27…A2-29). The probe's "$1,298 complete / $598 board-only" is the **4K row**, not the
price; the 48K system price printed in 1977 was $2,638.

**C-4 → AP-18 (IPO terms).** The printed percentage and the printed share count do not reconcile:
`0.08 × 52.4M = 4.192M ≠ 4.6M`, and `4.6M/52.4M = 8.78%`. The probe recorded the sentence and derived
`4.6M × $22 = $101.2M` but did not test the internal arithmetic. Both gross figures should be carried
($101.2M and $92.2M) with the inconsistency flagged (U-A2-9, Q25).

**C-5 → AP-12 (Kentucky Fried Computers).** Extend with the full advertisement: it is "a new retail
computer store in Berkeley", at 2465 Fourth Street, phone (415) 549-0858, page 75, with a "$80.00
minimum order" and a slogan — and, decisively, **the same firm told Homebrew readers in June 1976 that
it had no store yet and was "selling on a mail and telephone order basis"**, naming Mark Greenberg and
Charles Grant (A2-12, A2-39). The dealer who printed the Apple-1 in November 1976 was a five-month-old
mail-order operation, which is a materially different channel picture from "a retail store stocked it".

**C-6 → AP-11 and the probe's data-gap row "Exact Apple II introduction date and Faire venue … venue
contested".** Closed from local material: **First West Coast Computer Faire, San Francisco Civic
Auditorium, billed April 15–17, 1977** (Homebrew 1976-12-10, A2-41; Faire flyer, A2-42), with the
post-event report giving "April 16 and 17" and an announced **12,800** attendance (A2-43, U-A2-3). No
web request was needed.

**C-7 → AP-37 (general press "NOT FOUND").** Amend: the periodical corpus itself yields two dated
general-press targets — **Business Week, July 12, 1976**, carrying a feature on Paul Terrell's Byte Shop
(reported in BYTE October 1976, A2-10), and **Computerworld**, which had run Computer Shack's franchise
advertisement "several times" by April 1977 (A2-66). Neither was opened; both are recorded UNTRIED
(DG-10, DG-11). The correct statement is "no general-press *text* is cached", not "no general-press
*trace* exists".

**C-8 → AP-22 (Apple placed no BYTE advertisement in 1976).** Confirmed by an independent pass, with
an extension: the first Apple-placed BYTE advertisement is **June 1977**, and the **July 1977** run is a
**three-page front-of-book placement indexed as pages 22–24** (A2-65, A2-30) — i.e. the company's
advertising capacity in its first month of self-publishing was materially larger than a single-page
introductory buy.

**C-9 → AP-16 / AP-35 (the "under $700" band and the missing 1976 price).** Add the comparator the
probe did not have: a **complete assembled MOS 6502 system at $675** was printed in the club's own
newsletter in June 1976 (A2-68), and the 1976 assembled-machine band in these files runs **$675 →
$1,495** (A2-68, A2-45, A2-46). "Under $700" therefore reads as **market-rate for a 6502 system in
1976**, not as a bargain — which changes the §E/§P interpretation of the first product's positioning
without touching the quote.

**C-10 → AP-23 / AP-18 corroboration counts.** The probe listed the LOC page as an independent second
witness for the $7.8M/$117M pair. Restate: within this dossier's corpus the pair is supported by **one
1981 column**; the LOC page's own sourcing (Brashares 2001, Britannica 2021, Mergent 2020) is derivative
of later retelling, and per §3's independence rule the count stays at 1 for anything FY1978-specific
(A2-49, A2-55).

**C-11 → AP-32 (the HP-65 / VW-bus capital story, "0 independent").** New material bearing on it, all
in-window: BYTE April 1976 prices the HP-65 at "$795 … sometimes … $695", and Homebrew's own June 1976
classifieds show a complete IMSAI system offered at **65.2% of retail** (A2-71). The $500 memoir figure
is therefore **inside the period's observable used-equipment discount band** — a plausibility bound, not
corroboration; the event's independence count remains 0.

**C-12 → AP-175 row "Markkula's first-investor terms" / the probe's "only his existence, role and
holding".** Extend the negative precisely: **the string `Markkula` does not occur in any of the 30
cached 1975–1981 periodical files** (DG-5). His earliest print appearance in this corpus is the
February 1981 clause at A2-51. So not only are his *terms* uncorroborated — his *presence in the
founding-era print record* is absent, which is a stronger and more useful statement for Stage 1.

**C-13 → MASTER_RESEARCH_LOG Apple row, "Excluded:" list.** One item should be softened: "no 1976 sales
figure" is confirmed (A2-23, A2-30/Q30, DG-1), but the row's companion framing "press-, artifact- and
product-shaped" understates what the periodicals also yield — a **complete 1977 price ladder, a named
dealer network at manager level, dated competitor price sheets, a quantified club market survey, and a
reconcilable-then-not-reconcilable IPO column.** Recommend the verdict line read: *exemplar-capable;
money interior UNKNOWN; channel and price interior recoverable at row level.*

## Evidence-family verdict

Per §14 rule 6, five families, with what each returned and what was never tried.

| Family | Result for Apple Stage 1 | Records | Status |
|---|---|---|---|
| **1. Filings (SEC/EDGAR)** | Reaches essentially nothing before 1994-01-26; yields exactly one founding fact (incorporation 1977-01-03, California) and the exhibit pointers to paper-era filings | AP-01…AP-07, AP-21 | **Searched, thin by construction** |
| **2. Web archives (Wayback)** | Empty pre-1994 at apple.com root; earliest corporate self-narrative 1996-10-22; no Stage-1 content | AP-08, AP-09 | **Searched, null** |
| **3. Periodical corpora** | **Carries the stage.** 30 cached items, ~13 MB of full-issue OCR, produced **77 numbered records** here, of which **54 are dated in-window or far-side-with-dates** (1975-10-15 → 1981-02), including verbatim dealer advertisements (Sept–Dec 1976, Jan–May 1977), the designer's own May 1977 article, Apple's **complete June 1977** price ladder, a national store directory at manager level (April 1977), a quantified club survey (June 1976), the Faire's billing and its announced attendance, and the February 1981 revenue/cap-table column | A2-01…A2-77 | **MINED, dominant family** |
| **4. Auction / museum / documentary-sale records** | The only carriers of 1976 *paper*: the 1976-04-01 three-signatory agreement (Christie's, sold 2026-01-23, $2,515,000), Jobs's 1973 application (Charterfields, March 2021, $222,400), Terrell's 1976 Polaroids, the Koa-wood cases. Texts unread by this pass | AP-20, AP-28…AP-33 (cited by ID; not re-derived here) | **Discovered; NOT TRIED at lot-text level by this dossier** — DG-9 |
| **5. Digitised corporate print (annual reports / prospectuses / house magazines)** | Nothing reachable: the 1980 prospectus is paper-only (DG-3); no Apple annual report before FY1994 is online (AP-02) | AP-02, AP-21 | **UNTRIED in libraries** — the family that flipped Walmart's verdict does not rescue Apple's money interior either, and it is the one place FY1976–77 columns could still exist |

**Verdict.** The periodical family alone is sufficient to hold Apple at **exemplar depth for Stage 1**,
and this dossier is the demonstration: it added ~55 records the feasibility probe did not have, using
only files already on disk and **zero** web requests. But the family's strength is specific and its
weakness is structural, so the honest shape of Apple Stage 1 is:

- **Strong**: the distribution circuit (named stores, addresses, managers, discount terms, an
  international franchise), the product's printed configuration and full price ladder, the competitive
  price geography, and the club milieu including a quantified 1975→1976 market survey.
- **Weak**: the firm's legal interior (no 1976–77 document in any cached file names the partnership, the
  incorporation, the third partner, Markkula, or any transaction).
- **Empty**: money for 1976 and 1977; unit counts; any independent number behind any Apple self-report;
  Jobs's and Wozniak's pre-1976 states.

**Four-family test, answered.** Apple's Stage 1 is not forensic-core because family 3 is rich; family 1
and family 2 return nothing for the period by construction (as the method now expects pre-1994), and
families 4 and 5 are **untried rather than null** for this dossier. Any downgrade verdict for Apple
would repeat the Walmart error the method now names: **a null from one family is not a null, and an
untried family is not a null either.** Families 4 (Christie's lot text) and 5 (library copy of the 1980
prospectus) remain the two that could still change Stage 1's conclusion — and only its money section,
not its shape.

## CSV append rows

Rows only — **the CSV files themselves are the orchestrator's to create** at
`company_004_apple/research/`. Schemas are §13 verbatim; headers are repeated per file so an append is
mechanical. Source IDs are prefixed `A2S-` to keep this dossier's proposals from colliding with an
existing register; the Evidence Registrar may re-key them, in which case `claim_ref` (this file's `A2-`
record IDs) is the stable join. `access_date` is the cached retrieval date recorded in
`sources/_RETRIEVAL_LOG.md` (2026-09-24), not a re-fetch by this pass.

### `quantitative.csv` — append rows

```csv
company,stage,date,metric,value,unit,source,source_date,evidence_class,confidence,derived_arithmetic,notes
Apple,1,1977-05,"Apple-I retail price as stated by designer","under 700","USD per board","A2S-06","1977-05","FOUNDER CLAIM (contemporaneous)","Medium","","Wozniak in print May 1977; no 1976 document states a price (A2-23)"
Apple,1,1976-01/1976-12,"Apple-1 price stated in any 1976 print","UNKNOWN","USD","A2S-01/02/03/04/05","1976","UNKNOWN","High","","Documented absence across all twelve 1976 BYTE issues plus Homebrew 1975-11 to 1977-01"
Apple,1,1977-06,"Apple II system price, 4K configuration","1298.00","USD","A2S-07","1977-06","FACT","High","","Company's own published price list"
Apple,1,1977-06,"Apple II board-only price, 4K configuration","598.00","USD","A2S-07","1977-06","FACT","High","","'for the do-it-yourself hobbyist'"
Apple,1,1977-06,"Apple II system price, 48K configuration","2638.00","USD","A2S-07","1977-06","FACT","High","","Top of the ladder printed in 1977"
Apple,1,1977-06,"Apple II board-only price, 48K configuration","1938.00","USD","A2S-07","1977-06","FACT","High","",""
Apple,1,1977-06,"Implied California sales-tax rate in Apple's price table","6.5","%","A2S-07","1977-06","DERIVED","High","84.37 / 1298.00 = 0.0650; cross-checks 38.87/598.00, 110.37/1698.00, 171.47/2638.00 all = 0.0650","Conflicts with 6% printed by other advertisers (U-A2-6)"
Apple,1,1977-06,"Assembled-system premium over board-only","700","USD","A2S-07","1977-06","DERIVED","High","1298.00 - 598.00 = 700","Buys case, keyboard, power supply, two paddles, demonstration cassette"
Apple,1,1977-06,"Marginal factory memory per 1K, 4K to 12K steps","25","USD per 1K","A2S-07","1977-06","DERIVED","High","(1398 - 1298) / 4 = 25","Step to 16K costs 200 (1698-1498)"
Apple,1,1977-06,"Aftermarket 4K chip set","125","USD","A2S-07","1977-06","FACT","High","","31.25 USD per 1K"
Apple,1,1977-06,"Aftermarket 16K chip set","600","USD","A2S-07","1977-06","FACT","High","","37.50 USD per 1K; the ad states factory memory carries a 20% saving"
Apple,1,1976-06,"Complete assembled MOS 6502 system sold by Electronic Tool Co (ETC-1000)","675","USD","A2S-10","1976-06-09","FACT (as printed)","High","","Closest printed 6502 comparator to the Apple-I claim of 'under $700' for a board"
Apple,1,1976-11,"Processor Technology Sol-20, kit / assembled","995 / 1495","USD","A2S-04 and A2S-05","1976-11 and 1977-04","FACT (as printed)","High","","Assembled premium 1495-995 = 500 versus Apple's 700"
Apple,1,1976-06-09,"Homebrew meeting live-system count","101","systems","A2S-10","1976-06-09","CONTEMPORARY OBSERVATION (self-surveyed)","Medium-High","","6502 share 18/101 = 17.8%; 8080 share 53/101 = 52.5%; October 1975 comparison 38 systems"
Apple,1,1977-04,"West Coast Computer Faire exhibitor population billed","200","exhibitors","A2S-11","1977-02-16","ESTIMATE (organiser's forecast)","Medium","","Flyer forecast 7,000-10,000 attendees"
Apple,1,1977-04,"West Coast Computer Faire attendance announced at close","12800","attendees","A2S-08","1977-07","CONTEMPORARY OBSERVATION (self-report)","Medium","","No independent count exists; 12800/8500 = 1.51x the organiser's own forecast mid-point"
Apple,1,1978,"Apple sales, fiscal 1978","7800000","USD","A2S-09","1981-02","FACT (as printed)","High","","Earliest fiscal year printed anywhere in this corpus; RETROSPECTIVE SOURCE for Stage 1"
Apple,1,1978,"Apple profit, fiscal 1978","793497","USD","A2S-09","1981-02","FACT (as printed)","High","","793497/7800000 = 10.17% net margin (DERIVED)"
Apple,1,1979,"Apple sales / earnings, fiscal 1979","48000000 / 5000000","USD","A2S-09","1981-02","FACT (as printed)","High","","5/48 = 10.4% net margin (DERIVED); rounded to $1M in print"
Apple,1,1980-09-26,"Apple sales / profit, fiscal 1980","117000000 / 11700000","USD","A2S-09","1981-02","FACT (as printed)","High","","11.7/117 = 10.0% net margin; sales growth 117/7.8 = 15.0x since FY1978 (DERIVED)"
Apple,1,1980-12,"Offering price per share","22","USD","A2S-09","1981-02","FACT (as printed)","High","",""
Apple,1,1980-12,"Shares offered","4600000","shares","A2S-09","1981-02","FACT (as printed)","High","","Printed as 8% of 52.4M shares; 4.6/52.4 = 8.78% - internal inconsistency (U-A2-9)"
Apple,1,1980-12,"Gross offer size on printed share count","101200000","USD","A2S-09","1981-02","DERIVED","High","4600000 x 22 = 101200000",""
Apple,1,1980-12,"Gross offer size on printed 8%","92240000","USD","A2S-09","1981-02","DERIVED","Medium","0.08 x 52400000 x 22 = 92240000","Both figures carried; neither preferred pending the paper prospectus"
Apple,1,1981-02,"Value of one founder's holding at the offer price","182600000","USD","A2S-09","1981-02","DERIVED","High","8300000 x 22 = 182600000","Column says 'well over $100 million'; print understates its own arithmetic"
Apple,1,1981-02,"Combined holding of Jobs, Wozniak and Markkula","47.5","% of shares","A2S-09","1981-02","DERIVED","High","(3 x 8300000) / 52400000 = 0.475","Venrock 3.8M = 7.25%; Xerox 80,000 = 0.15%"
Apple,1,1976-04,"HP-65 calculator retail / street price in period print","795 / 695","USD","A2S-01","1976-04","FACT (as printed)","High","","Used as a plausibility bound for the 2006 memoir's $500 sale, not as corroboration"
Apple,1,1976-06-09,"Used-computer discount observable in the club's own classifieds","34.8","% below retail","A2S-10","1976-06-09","DERIVED","Medium","1 - (2000 / 3066.58) = 0.348","$500 against $795 = 62.9% of retail, i.e. a 37.1% discount - adjacent to the observed band"
Apple,1,1976-11,"Dealer mail-order terms of trade","10 off list / +2 carriage / $80 minimum","% and USD","A2S-04","1976-11","FACT (as printed)","High","","Kentucky Fried Computers, Berkeley, page 75"
Apple,1,1976-04/1976-10,"Apple units sold, revenue, headcount or order size in 1976 print","UNKNOWN","UNKNOWN","A2S-01..A2S-12","1976","UNKNOWN","High","","The corpus's central money null for Stage 1 (A2-23, DG-1, DG-2)"
```

### `timeline.csv` — append rows

```csv
company,stage,date_or_range,event,actors,location,source_id,evidence_class,confidence,conflict_ref,notes
Apple,1,1975-10-15,"Homebrew meeting survey counts 38 live systems among about 80 attendees","club members","San Francisco Bay Area; venue not printed in the cached item","A2S-10","CONTEMPORARY OBSERVATION","Medium-High","None","Baseline for the June 1976 count"
Apple,1,1975,"Apple-I designed 'late in 1975' per its designer","Stephen Wozniak","location UNKNOWN in print","A2S-06","FOUNDER CLAIM (contemporaneous)","Medium","U-A2-2","No 1975 document in the cached corpus names the machine or the design"
Apple,1,1976-04,"An APPLE 6502 system is a club's special guest; Steve Wozniak thanked for transporting it","Stephen Wozniak; Sonoma County Micro Computer Club","Cotati, California (LO*OP CENTER)","A2S-12","CONTEMPORARY OBSERVATION","High","None","Earliest dated Apple-machine-and-founder trace in any cached document"
Apple,1,1976-06-09,"Kentucky Fried Computers sells IMSAI by mail and telephone to club members; has no store yet","Mark Greenberg; Charles Grant","Berkeley, California","A2S-10","CONTEMPORARY OBSERVATION","High","None","The firm that advertises an Apple-1 by mail in November 1976 (A2-12)"
Apple,1,1976-07,"BYTE prints Paul Terrell as founder of the world's first computer store franchise","Paul Terrell; BYTE","Peterborough NH (magazine) / Mountain View CA (store)","A2S-02","CONTEMPORARY OBSERVATION","High","U-A2-5","Channel precondition for Apple's first distribution"
Apple,1,1976-09,"Earliest Apple-1 retail advertisement recovered: 'Take a byte out of the new Apple-1 computer'","Computer Mart of New York Inc (Stanley Veit, storekeeper)","314 Fifth Avenue, New York NY","A2S-04","FACT (advertising artifact)","High","None","One month earlier than the feasibility probe recorded (C-1)"
Apple,1,1976-09,"Byte Shop stores #1 and #2 printed with addresses and telephone","Paul Terrell's Byte Shop","1063 El Camino Real Mountain View; 3400 El Camino Real Santa Clara","A2S-04","FACT","High","None","Same issue as the first Apple-1 advertisement"
Apple,1,1976-09,"WESCON floor: Helmers converses with Steven Jobs (Apple Computer Co) and Paul Terrell (Byte Shops)","Steve Jobs; Paul Terrell; Bob Marsh; Chris Rutkowsky; Carl Helmers","WESCON, Los Angeles CA","A2S-03","CONTEMPORARY OBSERVATION","High","None","Earliest outside print naming Jobs"
Apple,1,1976-07-12,"Business Week features the Byte Shop (as reported by BYTE in October 1976)","Paul Terrell; Business Week","Mountain View CA","A2S-03","CONTEMPORARY OBSERVATION of a third publication","High","None","Content of the article UNKNOWN; a dated general-press target (DG-11)"
Apple,1,1976-11,"Apple-1 offered by mail order at 10% off manufacturer's list; 'the new Apple computer' described as currently marketed","Kentucky Fried Computers; BYTE article author","Berkeley CA","A2S-04","FACT","High","None","Proves a published retail list price existed by November 1976"
Apple,1,1976-11-20,"Wozniak and Jobs demonstrate the prototype Apple-II in a Palo Alto motel room; BASIC session that evening","Stephen Wozniak; Stephen Jobs; Carl Helmers","Palo Alto CA","A2S-05","CONTEMPORARY OBSERVATION","High","U-A2-3","Single witness; published April 1977"
Apple,1,1976-12,"'Apple Computers' a committed exhibitor at the first West Coast Computer Faire","Apple; Jim Warren (Faire chairperson)","San Francisco CA","A2S-03","CONTEMPORARY OBSERVATION","High","U-A2-1","Last pre-launch trade reference"
Apple,1,1976-12-10,"Faire billed for April 15-17, 1977 at the San Francisco Civic Auditorium","Jim Warren","newsletter office Mountain View CA","A2S-12","FACT","High","U-A2-3","Closes the probe's venue/date gap (C-6)"
Apple,1,1977-01-03,"Apple Computer, Inc. incorporated under California law","UNKNOWN in this corpus","UNKNOWN","AP-04 (outside the A2 corpus)","FACT","High","U-A2-1","Stage boundary; NOT in the periodical corpus - no 1977 print reports it"
Apple,1,1977-02-16,"Faire flyer circulated: 200 exhibitors, 7,000-10,000 expected, 'Bay Area - Where It All Started'","Jim Warren; Homebrew members","San Francisco CA","A2S-11","CONTEMPORARY OBSERVATION","High","None","A regional origin claim predating any company origin story"
Apple,1,1977-04,"BYTE prints a national computer-store directory: about 35 Byte Shop outlets across 22 jurisdictions including Tokyo and Vancouver","Byte Shops Inc (Bryan Kerr, Sunnyvale); named managers","US, Canada, Japan","A2S-05","FACT","High","None","The most granular channel evidence recovered for Stage 1"
Apple,1,1977-04-15/17,"First West Coast Computer Faire held; Apple booth invited to; announced attendance 12,800","Apple; Jim Warren; 12,800 attendees (promoter's count)","San Francisco Civic Auditorium","A2S-05 and A2S-08","CONTEMPORARY OBSERVATION","Medium","U-A2-3","Self-reported count; no independent denominator"
Apple,1,1977-05,"Wozniak publishes 'The Apple-II' at page 3 of BYTE under an Apple Computer Co Cupertino byline","Stephen Wozniak","Cupertino CA 95014","A2S-06","FOUNDER CLAIM (contemporaneous)","High","U-A2-2","Dates the Apple-I design to late 1975; attributes distribution to word of mouth then retail"
Apple,1,1977-05,"Computer Mart of New York moves to a new showroom, lists APPLE among about 25 lines, claims East-Coast store primacy","Stanley Veit","New York NY","A2S-06","FACT plus third-party primacy claim","High","U-A2-5","Same retailer as the September 1976 Apple-1 advertisement"
Apple,1,1977-06,"Apple's first self-published BYTE advertisement: full 4K-48K price ladder, mail order, postage paid, dealer-referral phone","Apple Computer Inc","20863 Stevens Creek Blvd Bldg B3-C, Cupertino CA","A2S-07","FACT","High","U-A2-6","Maker's printed voice begins nine months after dealers advertised the product"
Apple,1,1977-07,"Apple advertisement re-runs as a three-page front-of-book placement (pages 22-24)","Apple Computer Inc","Cupertino CA","A2S-08","FACT","High","None","Advertiser index fixes the pages"
Apple,2,1980-12,"Apple shares go on sale; 4.6M shares at $22 printed as 8% of 52.4M","Apple; underwriters","New York / Cupertino","A2S-09","FACT (as printed)","High","U-A2-9","Post-stage; admitted only as the far-side witness"
Apple,2,1981-02,"BYTE prints the FY1978-FY1980 revenue series and the pre-IPO cap table; Ronald Wayne appears nowhere in it","BYTE column; Jobs; Wozniak; Markkula; Venrock; Xerox","Peterborough NH","A2S-09 and A2S-13","FACT (as printed)","High","U-A2-10","Wayne's absence is a record-selection finding (A2-73)"
```

### `sources.csv` — append rows

```csv
source_id,stage,claim_supported,source_title,author_or_publication,source_type,primary_or_secondary,event_date,publication_date,access_date,url,archived_url,tier,evidence_class,confidence,independence_note,relevant_passage,notes
A2S-01,1,"No Apple-placed advertisement and no Apple price in BYTE during 1976; HP-65 pricing","BYTE January-June 1976","Carl Helmers (ed.), BYTE Publications Inc","trade magazine, full-issue OCR","primary","1976-01/06","1976","2026-09-24","https://archive.org/details/byte-magazine-1976-01 .. -06","sources/ia_byte_1976/byte-1976-01.txt .. -06.txt","1","FACT (documented absence)","High","same corpus as A2S-02; the apple tokens in these issues are 'Big Apple', 'Apple Valley', 'apple pie', 'bad apples'","NO_VERBATIM_PASSAGE_RECORDED","Establishes the empty first half of 1976 (A2-01..A2-04) and the $795/$695 HP-65 price (A2-71)"
A2S-02,1,"Byte Shop established as a display channel in vendor ads from April 1976; Terrell's franchise claim","BYTE April-July 1976 vendor advertisements and 'BYTE UNDER GLASS'","Carl Helmers, BYTE; advertisers","trade magazine","primary","1976-04/07","1976-04/07","2026-09-24","https://archive.org/details/byte-magazine-1976-07","sources/ia_byte_1976/byte-1976-04.txt .. -07.txt","1","CONTEMPORARY OBSERVATION","High","four issues, one campaign for the 'on display at' line; the Terrell sentence is editorial","'Paul Terrell, founder of the BYTE Shop, the world's first computer store franchise, puts lock and key to the family jewels.'","Primacy claim contested - U-A2-5"
A2S-03,1,"Jobs named in 1976 print; Faire exhibitor list; Business Week pointer","BYTE September-December 1976 (editorial, distributor list, trade-show column)","Carl Helmers and advertisers, BYTE","trade magazine","primary","1976-09/12","1976","2026-09-24","https://archive.org/details/byte-magazine-1976-09 .. -12","sources/ia_byte_1976/byte-1976-09.txt .. -12.txt","1","CONTEMPORARY OBSERVATION","High","editorial and advertising matter in one magazine: counted as one origin for BYTE's editorial line","'Steven Jobs (Apple Computer Co) and Paul Terrell (Byte Shops) on the floor of the WESCON show last September in Los Angeles CA.'","Also carries the Business Week 1976-07-12 Byte Shop pointer and the 1976-12 Faire exhibitor list"
A2S-04,1,"Earliest Apple-1 retail advertisement (September 1976); Apple-1 mail order November 1976; competitor price sheets","BYTE September-November 1976 advertisements","Computer Mart of New York Inc; Kentucky Fried Computers; BYTE","advertising artifacts in a trade magazine","primary","1976-09/11","1976-09/11","2026-09-24","https://archive.org/details/byte-magazine-1976-09 and -11","sources/ia_byte_1976/byte-1976-09.txt; byte-1976-11.txt","1","FACT","High","two independent advertisers; the October/December re-runs are one campaign, not corroboration","'Take a byte out of the new Apple-1 computer.' / '*Apple-Apple-1 computer'","Corrects AP-14's date and store-name attribution (C-1)"
A2S-05,1,"Apple-II pre-announcement and the 1976-11-20 sighting; the national store directory","BYTE April 1977 ('A Nybble on the Apple'; computer-store directory)","Carl Helmers; directory compiler; advertisers","trade magazine","primary","1976-11-20; 1977-04","1977-04","2026-09-24","https://archive.org/details/byte-magazine-1977-04","sources/ia_byte_1977/byte-1977-04.txt","1","CONTEMPORARY OBSERVATION","High","Helmers is a participant-witness; the directory is compiled matter independent of him","'I first saw the Apple-ll on November 20 1976 when Stephen Wozniak and Stephen Jobs stopped by a motel room in Palo Alto'","Directory lists about 35 Byte Shop outlets with named managers, the parent at Sunnyvale, plus Byte Shop of Tokyo"
A2S-06,1,"Apple-I design date, price band and distribution; four non-founder contributors; the 1977 address of record","'The Apple-II - System Description', BYTE May 1977, p 3","Stephen Wozniak, Apple Computer Co, Cupertino","trade magazine article by the company's designer","primary","1975; 1977-05","1977-05","2026-09-24","https://archive.org/details/byte-magazine-1977-05","sources/ia_byte_1977/byte-1977-05.txt","1","FOUNDER CLAIM (contemporaneous)","High","company-side: NOT independent of A2S-07 (same publisher-interest)","'The Apple-I, my first video oriented single board computer, was designed late in 1975 and sold by word of mouth throughout California and later nationwide through retail computer stores.'","Also 'a price under $700 at the retail level'; acknowledgements to Baum, Kraul, Wigginton, Espinosa"
A2S-07,1,"Apple II configuration, the complete nine-row price ladder, tax add-ons, aftermarket memory, direct mail order, dealer referral","Apple Computer Inc advertisement, BYTE June 1977","Apple Computer Inc","advertising artifact","primary","1977-06","1977-06","2026-09-24","https://archive.org/details/byte-magazine-1977-06","sources/ia_byte_1977/byte-1977-06.txt","1","FACT (company's published offer)","High","same commercial interest as A2S-06: two documents, one interest","'Apple II Price List ... 4K $1,298.00 $84.37 $598.00 $38.87 ... 48K $2,638.00 $171.47 $1,938.00 $125.97'","Superlatives inside the ad ('the first personal computer with') are FOUNDER CLAIM in substance"
A2S-08,1,"Apple's July 1977 re-run and its pages; the Faire's announced attendance; Radio Shack franchise interest","BYTE July 1977 (advertisement; Faire report; advertiser index)","Lawrence F Willard; Apple Computer Inc; BYTE","trade magazine","primary","1977-04; 1977-07","1977-07","2026-09-24","https://archive.org/details/byte-magazine-1977-07","sources/ia_byte_1977/byte-1977-07.txt","1","CONTEMPORARY OBSERVATION","Medium","the 12,800 figure is the promoter's self-report transmitted by a correspondent: one interest","'At the end of the show, chaircreature Jim Warren announced that 12,800 people had attended.'","Index line '7 Apple 22, 23, 24' fixes the advertisement's pages"
A2S-09,1,"The IPO terms, the FY1978-FY1980 revenue and profit series, the pre-IPO cap table","'Apple Stock Goes On Sale', BYTE February 1981, p 212","BYTE column (unsigned)","trade magazine","primary","1978-1981","1981-02","2026-09-24","https://archive.org/details/byte-magazine-1981-02","sources/ia_byte_1981/byte-1981-02.txt","1","FACT (as printed); RETROSPECTIVE SOURCE for 1976-77","High","single column; the 2008-2023 LOC page is derivative of later retelling and adds nothing (C-10)","'Apple offered 8% of the company's 52.4 million shares (ie: 4.6 million shares) at a price of $22 per share.'","Internal arithmetic inconsistent - U-A2-9; mixed precision - U-A2-8"
A2S-10,1,"Homebrew's quantified 1976 market survey; Kentucky Fried Computers pre-store; used-equipment discount; the 6502 comparator price","Homebrew Computer Club Newsletter Vol 2 No 6 ('Random Data'; 'BULLETIN BOARD')","Robert Reiling (ed.), Mountain View CA","club newsletter, full item OCR","primary","1976-06-09","1976-06-09","2026-09-24","https://archive.org/details/hcc0206","sources/ia_homebrew/hcc0206.txt","1","CONTEMPORARY OBSERVATION (self-surveyed)","Medium-High","grassroots document, independent of BYTE and of Apple","'8080-53, 6502-18, 8008-6, PDP-8-4, LSI-11-3, Z80-2, 4004-1, PDP1 1/20-1 and TTL-1. That totals 101 systems'","Also 'California residents must add 6% sales tax' (conflicts with Apple's implied 6.5%, U-A2-6) and the ETC-1000 at $675"
A2S-11,1,"The Faire's billed scale, venue and dates; a 1977 regional origin claim","West Coast Computer Faire flyer","The Computer Faire / Jim Warren, chairperson","flyer, full item OCR","primary","1977-04-15/17","1977-02-16","2026-09-24","https://archive.org/details/hcccf","sources/ia_homebrew/hcccf.txt","1","CONTEMPORARY OBSERVATION","High","promoter's own document; not independent of A2S-12's circle","'San Francisco Bay Area - Where It All Started - Has Its First Home Computing Convention ... 200 Commercial & Homebrew Exhibits'","Closes AP-11's venue/date question (C-6)"
A2S-12,1,"Earliest founder-plus-machine trace; the Faire dates in club print","Homebrew Computer Club Newsletters Vol 2 No 4 and No 11","Robert Reiling (ed.)","club newsletter","primary","1976-04; 1976-12","1976-04-30; 1976-12-10","2026-09-24","https://archive.org/details/hcc0204 and hcc0211","sources/ia_homebrew/hcc0204.txt; hcc0211.txt","1","CONTEMPORARY OBSERVATION","High","the April item is a reprinted letter from a DIFFERENT club (Sonoma County): provenance is per-item, not per-run","'In April the APPLE 6502 system was our special guest. We are grateful to STEVE WOZNIAK for providing transportation.'","No company reference in the club's print before this date (A2-05, A2-06)"
A2S-13,1,"Absence of the third partner and of Markkula from in-window print; Apple's 1980 address and toll-free channel","BYTE December 1980 (Apple and third-party advertisements); BYTE February 1981","Apple Computer Inc; Mountain Computer; CCS; BYTE","trade magazine","primary","1980-12; 1981-02","1980-12; 1981-02","2026-09-24","https://archive.org/details/byte-magazine-1980-12","sources/ia_byte_1981/byte-1980-12.txt; byte-1981-02.txt","1","FACT (documented absence within these files)","High","one corpus","'Visit your nearest Apple dealer or call 800-538-9696 ... Apple Computer, 10260 Bandley Drive, Cupertino, CA 95014.'","Wayne as a person-name: 0 hits across all 30 cached files; Markkula: 1 hit (1981-02)"
```

### `conflicts.csv` — append rows

```csv
company,stage,conflict_id,section,claim_a,claim_a_source,claim_a_date,claim_b,claim_b_source,claim_b_date,why_they_differ,evidence_weight,best_supported_interpretation,residual_uncertainty,confidence
Apple,1,U-A2-1,B / J,"Company styled 'Apple Computer Co'","BYTE December 1976 editorial (A2S-03)","1976-12","Company styled 'Apple Computers'","Homebrew Vol 2 No 9 (A2S-10) and BYTE December 1976 exhibitor list (A2S-03)","1976-09-15 / 1976-12","Publication lag and hearsay naming versus registered styling; two further forms follow ('Apple Computer Inc.' in the company's own 1977 ad; 'the Apple Corporation' in a 1980 third-party ad)","in-window print on both sides; the company's own 1977 letterhead outranks third-party lists for the corporation","All four name forms are authentic; no 1976-77 document names the partnership","Whether the registered partnership style appears in any 1976 print","High on print facts / Medium on inference"
Apple,1,U-A2-2,D / F,"Byte Shop placed a founding order of 50 boards at $500, July 1976","memoir lineage carried by AP-29/AP-30; no periodical","1976 (claimed)","Distribution was 'by word of mouth throughout California and later nationwide through retail computer stores'","Wozniak, BYTE May 1977 (A2S-06)","1977-05","A single memorable transaction versus a diffuse dealer ramp; the number attached in later telling","in-window first-party and third-party print versus retrospective memoir","A multi-dealer ramp including the Byte Shop circuit; no first order documented in periodicals","An outside document (invoice, Terrell's papers, the 1976 agreement) could still establish a transaction","High that the corpus has no order / Low on the canonical story"
Apple,1,U-A2-3,Q,"Faire billed April 15-17, 1977, San Francisco Civic Auditorium","Homebrew Vol 2 No 11 and the Faire flyer (A2S-11, A2S-12)","1976-12-10 / 1977-02-16","Faire held 'April 16 and 17 of this year'","Lawrence F Willard, BYTE July 1977 (A2S-08)","1977-07","Scheduled dates versus a correspondent's days on the floor","promoter's billing stronger for the schedule; the report stronger for coverage","Scheduled 15-17; the reporter attended 16-17","Which days Apple's booth was staffed","Medium-High"
Apple,1,U-A2-4,E / P,"The Apple-1 sold for $666.66","ubiquitous retelling (no periodical located)","1976 (claimed)","'a price under $700 at the retail level'","Wozniak, BYTE May 1977 (A2S-06)","1977-05","A distinctive price retailed because it is distinctive; the number may sit in titles this cache cannot text-search (Kilobaud, Creative Computing)","no in-window support for either number as a figure; the band is first-party","Under $700 per the designer; the specific figure unestablished here","UNANSWERED, not false: Kilobaud 1976 has no text layer (DG-4)","High on absence in these files / UNKNOWN on the true price"
Apple,1,U-A2-5,G,"Terrell's BYTE Shop was 'the world's first computer store franchise'","BYTE editorial (A2S-02)","1976-07","'Last year we opened the first computer store on the East Coast'","Computer Mart of New York advertisement (A2S-06)","1977-05","Three different scopes (franchise / East Coast / region) claimed by three interested parties, one of them the magazine's own advertiser","each self-serving, none corroborated by the others","No primacy claim in the corpus is established; the field was narrating its own origin in 1976-77","Which store first sold an Apple product (earliest advertisement: New York, September 1976)","High that the claims exist / Low on their truth"
Apple,1,U-A2-6,P,"California sales tax on Apple's 1977 prices is 6.5%","Apple price list (A2S-07), arithmetic 84.37/1298","1977-06","California sales tax is 6%","Kentucky Fried Computers notice (A2S-10) and a 1980 BYTE advertiser (A2S-13)","1976-06-09 / 1980-12","District add-ons differed by county and changed over time; advertisers were not uniform","Apple's table is internally consistent across nine rows, hard to produce by accident","Apple's 1977 prices carry a 6.5% add-on; the 6% lines belong to other jurisdictions or years","The actual 1977 district schedule is outside periodicals","High on arithmetic / Low on explanation"
Apple,1,U-A2-7,K / P,"The printed revenue record begins FY1978 at $7.8M","BYTE February 1981 (A2S-09)","1981-02","Stage 1 is April 1976 - January 1977","this dossier's stage boundary (AP-04)","1977-01-03","The printed series is investor-relations matter, not a history; its earliest year is two years after the events","one column","Apple's Stage-1 financial interior is UNKNOWN from periodicals; FY1978 must not be presented as year one","Only the paper prospectus can close it (DG-3)","High"
Apple,1,U-A2-8,P,"FY1978 profit printed to the dollar ($793,497)","BYTE February 1981 (A2S-09)","1981-02","FY1979 and FY1980 printed to one or two significant figures ($5M, $117M)","BYTE February 1981 (A2S-09)","1981-02","Mixed precision inside a single column: some rows from a document, some from memory or space constraints","the exact row is stronger","Report the series as reported, not audited; the 10.0/10.4/10.2% margin similarity is not evidence of an operating constant","Whether audited FY1979-80 figures exist in the prospectus","High on the observation / Medium on inference"
Apple,1,U-A2-9,P,"Offering was 8% of 52.4M shares","BYTE February 1981 (A2S-09)","1981-02","Offering was 4.6M shares, i.e. 8.78%","BYTE February 1981 (A2S-09)","1981-02","0.08 x 52.4M = 4.192M, not 4.6M: one figure is rounded, stale, or a different class or over-allotment","single column, no filing available (DG-3)","Carry both gross sizes ($101.2M and $92.2M); prefer neither","The whole reconciliation","High that the print is internally inconsistent"
Apple,1,U-A2-10,B / M,"The 1976-04-01 agreement has three signatories, 45/45/10","Christie's-catalogued document (AP-20)","1976-04-01","No 1976-1981 periodical names Ronald Wayne; the 1981 recap names Jobs, Wozniak and Markkula","negative census (A2S-13)","1975-03 / 1981-02","The press covered the company through its product and visible principals; a partner who left within weeks never entered the trade's reference set","A is one primary artifact outside this corpus; B is abundant in-window print","The third partner is a documentary fact with no periodical trace; the printed origin story was two-founder from the start","Whether any non-trade 1976 print (a California newspaper, Kilobaud) mentions Wayne","High within this corpus / Medium absolutely"
Apple,1,U-A2-11,J,"Corporate name 'Apple Computer Inc.'","Apple's own advertisement (A2S-07)","1977-06","'trademarks of the Apple Corporation'","CCS advertisement, BYTE December 1980 (A2S-13)","1980-12","Copywriter error, or the naming looseness U-A2-1 documents generally","trivial on its own","Evidence that the corporate name was still unstable in the field in 1980","none material","High that it was printed"
Apple,1,U-A2-12,E,"Cassette interface is '1500 bps'","Apple advertisement specification box (A2S-07)","1977-06","Cassette transfer 'averages over 180 bytes per second'","Wozniak (A2S-06)","1977-05","Bits versus bytes: 1500/8 = 187.5 bytes per second - the same measurement in two bases","both company-side and mutually consistent","No conflict of fact but a unit-of-measure conflict, and a live case for the rule that numerals carry their basis","none","High"
Apple,1,U-A2-13,B / G,"Apple founded at Los Altos, California","universe/feasibility register (AP-04 header row)","1976-04-01","Every cached 1976-77 document places Apple in Cupertino; all 17 Los Altos lines in the corpus belong to third parties (Cromemco, Qume et al.)","Wozniak byline (A2S-06); Apple advertisement (A2S-07); grep census","1977-05 / 1977-06","The register's place is a retrospective gloss about a family home carried from memoir; the print's place is the company's address of record","B is contemporaneous and self-published","Stage-1 print says Cupertino, in a Stevens Creek complex beside a firmware supplier, inside a Mountain View club circuit and a Sunnyvale-parented dealer chain","The garage's municipality is a property-record question (DG-8)","High on print / Medium on what it proves about where work happened"
```

**Register-set notes for the orchestrator.**
- `decisions.csv`, `validation.csv` and `failures.csv` rows are **deliberately not emitted**: this
  dossier found no in-window document evidencing a decision, and §13 requires `information_available`,
  `alternatives` and `rationale` cells that no periodical in this corpus can fill without fabrication.
  `channels.csv` may be populated from the §Distribution-channels-advertised table with `source_id`
  mapped to A2S-02…A2S-13; every row's `repeatability` should read UNKNOWN.
- `data_gaps.csv` may be populated verbatim from DG-1…DG-15; the `follow_up_task` cell is mandatory for
  the seven High-importance rows and is already written there.
- All four emitted registers key back to this file through `claim_ref` / `source_id` / `conflict_id`;
  no row asserts anything not on the record surface above.

---

## Close-out

**Written before further retrieval, per §14 rule 1.** The skeleton plus 24 dated records were on disk
after the first write pass; every subsequent source mined was appended in place. **80 numbered `A2-`
records** are on disk (A2-01 … A2-77, of which three are the A2-61a/b/c census records), each classed
and rated, with 13 conflicts (U-A2-1 … U-A2-13), 15 gap rows (DG-1 … DG-15), 13 provenance rows and 13
outbound corrections to the feasibility probe (C-1 … C-13), plus **79 CSV data rows** emitted across the
four registers (quantitative 30, timeline 23, sources 13, conflicts 13).

**Web requests spent: 0 of 3 permitted.** The twelve retrieval routes that would have used them are
recorded as UNTRIED with exact queries in §Data gaps, which is the instructed preference. Nothing
outside this file was created, modified, moved, renamed or deleted; `company_004_apple/sources/` was
read-only to this pass, and its two orphan files are flagged do-not-cite in §Provenance ledger rather
than tidied (§14 rule 4).

— end of dossier A2 —
