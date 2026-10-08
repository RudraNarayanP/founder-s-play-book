# A_chronology_feasibility.md — FEDEX (company_050_fedex, Fortune rank 50), Stage-1 PROBE

Owner: `probe-fedex`, claimed with
`python tools/scaffold.py claim --path founders_playbook/01_companies/company_050_fedex/research/A_chronology_feasibility.md --agent probe-fedex`
(claim returned `CREATED … (owner=probe-fedex ttl=240 min, sections=0, 35 words)`).

**Windows used, all PROPOSED (§15.2 / RD-112).** The fleet's Stage-1 candidate for this company is
**1971-01-01 → 1985-12-31**, and its provenance is a *search setting*: `tools/harvest_mine.py` **l.73** reads
`"fedex": ("1971-01-01", "1985-12-31")` (command: `grep -n "fedex" tools/harvest_mine.py`). It is **not** a
foundling date: `00_universe/fortune_top_50_2026.csv` has no founding-date column. This probe therefore
proposes a two-stage cut **from the dates the corpus itself recites** (§3 below, §5 for the tiers):
**Stage 1 PROPOSED 1971-06-24 → 1978-12-15**, **Stage 2 PROPOSED 1978-12-16 → 1985-12-31**, with the brief's
1971-01-01 → 1985-12-31 kept as the combined origin window so the fleet intake stays comparable.

**Web budget this pass: 0 WebSearch, 0 WebFetch.** Every byte quoted below was already on disk or reached
through `tools/sec_intake.py`. `tools/harvest_mine.py` and `tools/periodical_harvest.py` were **NOT run (by
order)**, so no family was re-harvested by this probe — but the **fleet's own facet-free re-harvest (RD-134)
landed 4 Internet Archive layers into `sources/periodicals/` during this pass**, which are read and adjudicated
at §10 rather than ignored. No family that owns bytes is reported as a null.

STATUS: WRITTEN

---

## 0. Measured state at probe start (verified this pass, not inherited)

| item | measured | how |
|---|---|---|
| files under `sources/` | **50 at claim time** (`sec/` 43 = 19 text layers + 19 sidecars + `_MANIFEST/_PLAN/_RUN/_SKIPPED/_UNANSWERED`, `_index/` 7, `corporate_print/` **0**) — and **no `periodicals/` and no `web_archive/` directory existed at all**. **Re-enumerated at close: 70 files**, the delta being 8 IA text layers + 8 sidecars (4 layers / 658,180 B at the first re-check, 12:04-12:05Z, and 4 more / 719,356 B at 12:07Z) that landed in `sources/periodicals/` **during this pass** → §10 | `find …/sources -maxdepth 1 -type d` + per-dir `find -type f \| wc -l`, repeated at close |
| held SEC text | **19 documents = 3,913,000 B** (matches `_RUN.json` `bytes: 3913000`, `words: 502648`); **19 distinct md5s over 19 files → 0 byte-identical duplicates** (rule 4 satisfied: no cross-shelf double-count is possible here) | `python -` md5/size loop over `sources/sec/*.txt` |
| distinct accessions behind the 19 docs | **14** | `python -c` set of `_MANIFEST.csv['accession']` |
| harvest-mine dossier `research/A4_harvest_mine.md` | **DOES NOT EXIST for this company** — `find . -name "A4*"` lists 48 other companies' A4s, none under `company_050_fedex`; `research/` holds only this file | `find`, `ls …/research` |
| → consequence | **Nothing in this report is quoted from an A4.** There is no fedex A4 to re-read, so no mined-bytes figure is inherited from it; the only local-byte statement below is my own `find`/`ls` enumeration | — |
| harvest-index rows naming this company | **30** (`internet_archive` 23, `corporate_print` 3, `chronicling_america` 2, `google_books` 1, `hathitrust` 1). Classification split: IA `LEAD_ONLY` 14 / `TIER1_CANDIDATE` 6 / `UNANSWERED` 2 / `NULL` 1; `corporate_print` `UNANSWERED` 2 / `TIER1_CANDIDATE` 1; CA 2 × `UNANSWERED`; HT 1, GB 1 `UNANSWERED`. `http_status`: 23 × `200`, **7 × blank** | `python -c` filter `candidates.csv` on `company=='fedex'` |
| `candidates.csv` header, enumerated **before** any field was read (rule 3) | `company, source_family, query, item_id, title, date_or_issue, url, snippet_or_hitcount, http_status, classification, retrieved_at` | `csv.DictReader(...).fieldnames` |
| query blocks exist for fedex | **8 tasks** in `tools/queries.json` (2 chronicling_america, 2 internet_archive, 2 corporate_print, 1 hathitrust, 1 google_books) — so family (c) is **not** "untried for want of a block" in the RD-112 Costco sense; it was asked and the bytes never arrived | `python -c` counter over `queries.json['tasks']` |
| stored periodical / corporate-print bytes for fedex | **0 at measurement time.** `find founders_playbook/00_universe/harvest -iname "*fedex*" -o -iname "*federal*express*" -o -iname "*fdx*"` returned **nothing** (and still does — re-run at close), because the late-arriving bytes went straight to the company directory, not to a harvest shelf: **8 layers / 1,377,536 B now in `sources/periodicals/` (§10), `sources/corporate_print/` still 0 non-JSON files** | that `find`, run twice; `python -c` glob+getsize over `sources/periodicals/*.txt` |
| EDGAR perimeter | `sources/_index/submissions_CIK0001048911.csv`: **2,157 rows, earliest `filingDate` 1997-11-04, latest 2026-09-25**; rows in **1971-01-01→1985-12-31 = 0**; rows in 1997-01-01→2010-12-31 = 770; only 3 forms pre-1998 (`S-4`, `S-4/A`, `424B3`) | `python -c` over the CSV, header enumerated first |
| walk not capped (RD-134) | `_INDEX.md`: "2157 filings enumerated; 0 submissions rows dropped"; **"UNANSWERED slices (never report these as absent): (none)"**; registrant guard `ok`, `identity: stored(19) + unanswered(12) + skipped(59) = 90 vs attempted(90) -> OK` | read `_INDEX.md`, `_RUN.json` |
| identity actually indexed | **FEDEX CORP, CIK 0001048911, ticker FDX, `former_names: ["FDX CORP"]`** — `_registrant_CIK0001048911.json`. The legacy operating carrier is **not** in this index and could not be resolved: `python tools/sec_intake.py index "Federal Express Corporation" --company-dir …` → `identity 'Federal Express Corporation' not resolved: NO-MATCH name (0 candidates)` (the tool resolves only through `company_tickers.json`, which carries tickered issuers — a delisted/subsidiary CIK is invisible to it) | that command, run this pass |

**The in-window pass measured, not inherited.** I did **not** re-run `auto --from 1971-01-01 --to 1985-12-31`
against this `--company-dir`, because `sec_intake.auto` writes `_MANIFEST.csv`, `_UNANSWERED.csv`,
`_SKIPPED.csv` and `_RUN.json` unconditionally after the dry-run branch (`tools/sec_intake.py` l.1369-1385),
which would have destroyed the recital pass's registers that this report cites (§14.4 "nothing is a cleanup
target"). The in-window zero is instead proven from the index the same pass left behind: `min filingDate =
1997-11-04` and **0 of 2,157 rows inside 1971-01-01→1985-12-31** (row above). That is a *measured perimeter*,
not "FedEx filed nothing before 1986" — EDGAR's own digital floor is 1993-94 and this registrant was not born
until 1997 (§1).

STATUS: WRITTEN

---

## 1. The identity finding: the registrant is a 1997 holdco; the 1971/1973 story belongs to a different legal person

Three facts, each with a held carrier, and each in a **different document type** (certificate, merger
financial statement, 10-K, proxy) yet **one corporate-record lineage** (§3 caps corroboration at 1):

1. **The registrant at CIK 1048911 was incorporated 1997-10-02 under a different name.**
   `sources/sec/0000912057-00-034322_ex-3_1.txt` **l.21-24** (Amended and Restated Certificate of
   Incorporation of FDX CORPORATION, exhibit to the FY2000 10-K405 accession): *"FDX Corporation, a
   corporation organized and existing under the laws of the State of Delaware (the 'Corporation'), hereby
   certifies that the Corporation was **originally incorporated under the name 'Fast Holding Inc.' on
   October 2, 1997**, and that its original Certificate of Incorporation was filed with the Secretary of
   State of the State of Delaware on the same date."*
   Corroborated in the same registrant's own merger financials: `0000950103-97-000667_0000950103-97-000667.txt`
   **l.5181-5185** — *"FDX Corporation (FDX), formerly Fast Holding Inc., was incorporated in the State of
   Delaware on October 2, 1997, as a wholly-owned subsidiary of Federal Express Corporation ('FedEx')"*
   (note-1 "Organization and Purpose", balance sheet dated **October 3, 1997**). Same sentence at
   `0000950103-97-000724…txt` **l.5050** (S-4/A — **same registration lineage**, one source).
2. **The operating carrier's own recital, and it is a single printing in the whole held corpus.**
   `0000899243-98-001610_0000899243-98-001610.txt` **l.304-307**, under the section heading
   `FEDERAL EXPRESS CORPORATION` / `INTRODUCTION` (10-K filed 1998-08-14): *"**FedEx was incorporated in
   Delaware on June 24, 1971 and began operations in 1973.** On January 27, 1998, FedEx became a wholly-owned
   subsidiary of the Company."* Census: `June 24, 1971` = **1 occurrence / 1 of 19 files**
   (`grep -n -F "June 24, 1971" *.txt`). The next year's filing drops the clause:
   `0001047469-99-032609_0001047469-99-032609.txt` **l.369** reads only *"FedEx began operations in 1973."*
3. **The label "FedEx" is attached to BOTH legal persons, 26 years apart, inside one corpus.**
   `0000912057-00-034322_a10-k405.txt` **l.183-185**: *"**FedEx was incorporated in Delaware on October 2,
   1997** to serve as the holding company parent of FedEx Express…"* — the identical sentence shape as
   l.306 above but the opposite entity. `grep -n -i "incorporated in Delaware"` → **7 occurrences / 5 of 19
   files**, split between the 1971 clause (1) and the 1997 clause (4), plus
   `0000899243-98-001610…txt` **l.186** and `0001047469-99-032609…txt` **l.193** (*"FDX Corporation ('FDX' or
   the 'Company') was incorporated in Delaware on October 2, 1997"*). **Any Stage-1 volume that quotes "FedEx
   was incorporated in Delaware on …" without naming which FedEx will be wrong half the time.** This is the
   Citigroup-1812 / Boeing-"since 1916" class, and here the wrong reading is one keystroke away because both
   sentences are in the same directory.

**Renaming, in the other direction from Ford.** For FedEx the *later* entity is the registrant and the *earlier*
one (Federal Express Corporation, 1971) is the ancestor whose business the dataset is actually about; the
registrant itself was renamed **twice**: `0000912057-00-034322_a10-k405.txt` **l.257** — *"formerly FDX
Corporation, was renamed FedEx Corporation."* The corpus therefore holds a three-name chain for one CIK:
**Fast Holding Inc. (1997-10-02) → FDX Corporation → FedEx Corporation (2000)**, and a separate chain for the
carrier the origin story needs — whose own predecessor name this corpus **never prints** (§3).

STATUS: WRITTEN

---

## 2. Carriers found for the origin / predecessor question (file + line), with tier and vintage

| # | claim element | carrier (file : line) | what it actually says | tier / vintage |
|---|---|---|---|---|
| C1 | registrant's birth | `sources/sec/0000912057-00-034322_ex-3_1.txt` **l.21-24** | originally incorporated as "Fast Holding Inc.", Delaware, **1997-10-02**, filed with DE Secretary of State same date | **Tier 1** (charter text filed with the SEC); 19 years after the window opens |
| C2 | holdco purpose/parentage | `…/0000950103-97-000667_0000950103-97-000667.txt` **l.5181-5185**; same lineage `0000950103-97-000724…` **l.5050** | FDX = former Fast Holding Inc., Delaware, 1997-10-02, wholly-owned sub of Federal Express Corporation | Tier 1; **one lineage** with C1 for §3 purposes (same corporate record) |
| C3 | **carrier's incorporation date** | `…/0000899243-98-001610_0000899243-98-001610.txt` **l.306-307** | "FedEx [Federal Express Corporation] was incorporated in Delaware on **June 24, 1971** and began operations in 1973" | Tier 1 doc, **RETROSPECTIVE company self-narrative**, 27 years late; **1 occurrence corpus-wide** |
| C4 | **incursion into market (dated)** | same file **l.9217-9220** (anniversary advertising page inside the FY1998 10-K accession, after `P56`) | "**When Federal Express took flight on April 17, 1973, it delivered 186 packages to 25 cities.** One courier sold his watch to buy fuel for his van. Others used their own cars for deliveries. The folks in Pittsburgh did business out of a motel room." + **l.9222** "FedEx's 25th anniversary … not only the founding of an industry" | Tier 1 **container**, Tier-4-grade **content**: promotional anniversary copy, 25 years late, single printing (`186 packages` = 1 occ, `April 17` = 1 occ, `25 cities` = 1 occ) |
| C5 | operations year, second printing (no date) | `…/0001047469-99-032609_0001047469-99-032609.txt` **l.369**; `…/0000912057-00-034322_a10-k405.txt` **l.499** and **l.623**; `…0000950103-98-000089…txt` **l.525** | "began operations in 1973" / "FedEx Express invented express distribution in 1973" / "the first integrated air/ground express transportation network in 1973" / "invented express distribution **25 years ago**" | Tier 1 docs, **same self-narrative lineage as C3/C4**; `invented express` = 3 occ / 3 files. Repeated copying of one origin story = **one source** (§3) |
| C6 | **first dated in-window corporate act of the carrier** | `…/0000950103-99-000191_0000950103-99-000191.txt` **l.1213-1217**; `0000950103-99-000356…` **l.1162**; `0000950103-97-000667…` **l.4926**; `0000950103-97-000724…` **l.4794** | "The description of common stock contained in the registration statement of **FedEx (as predecessor registrant) on Form 8-A filed with the SEC on December 15, 1978** … is incorporated herein by reference" — 4 printings, one fact | Tier 1 reference to a **1978-12-15** registration → the carrier was already a reporting company **inside** Stage 1. **The 8-A itself is NOT held** (paper era, pre-EDGAR) → FETCH REQUEST FR-3 |
| C7 | founder's dated role (not "founder") | `…/0000899243-98-001560…txt` **l.509-516**; `…/0000899243-98-001610…txt` **l.1267-1271**; `…/0000912057-00-037385_def14a.txt` **l.746**; `…/0000912057-00-034322_a10-k405.txt` **l.1787-1790** | "FREDERICK W. SMITH … **President of Federal Express Corporation from 1971 to 1975**" (1998 proxy) / "…President of FedEx from **June 1971 to February 1975**" (1998 10-K), "Chairman … since 1975", "CEO … from 1977" | Tier 1. Records an **office from June 1971**, never a founding act. `Founder`/`founder` see §3 |
| C8 | a second officer at the same June-1971 date | `…/0000899243-98-001560…txt` **l.537-539** | "Robert L. Cox … **Secretary of Federal Express Corporation from June 1971 to September 1993**" | Tier 1. Weak but real: a corporate secretary dated to June 1971 implies an organised corporation, **not** a term paper |
| C9 | "role recorded as founder" — the trap, in the corpus | `…/0000950103-00-001270_0000950103-00-001270.txt` **l.250-252**, **l.260-262** (8-K 2000-11-15) | "said **Sheridan Garrison, Chairman and Founder of American Freightways**" … "will serve as **Chairman Emeritus and Founder of American Freightways**" | **The only `Founder` title in all 19 held filings is an acquired company's founder.** Census: `Founder` **2 occ / 1 file**, lowercase `founder` **0 occ**, `founding` **1 occ / 1 file** (the C4 anniversary page) |

STATUS: WRITTEN

---

## 3. The founding is rehearsed as a story twice — what the corpus carries, and the measured zeros

The popular version has **two separate "founding" events** eight years apart, and neither is a carrier of the
other: (i) an entrepreneur's **idea** as a 1960s university term paper, and (ii) an **operating carrier**
launching in 1973 under a name this corpus never prints, with a later renaming. A graded class project is not a
first experiment, and a term paper is not a company. Measured against the 19 held filings (commands:
`grep -n -F "<term>" *.txt` and a python regex census over `sources/sec/*.txt`, both run this pass):

| element in the popular story | occurrences in held bytes | verdict |
|---|---|---|
| `Yale` | **family (a): 0 occ / 0 files.** **Late-arriving family (c): 1 hit — `sources/periodicals/DTIC_ADA540033_djvu.txt` l.291-292 (2009)** | **NO CARRIER in the corporate record.** In family (c) it is a **2009 third-party relay with a footnote to a source not held** (§10, C12) — a lead, not a source |
| `term paper` | **family (a): 0 occ / 0 files.** **Late family (c): 1 hit, same line** ("developed from a simple term paper as an undergraduate student at Yale University") | **NO CARRIER in (a); a Tier-3 relay exists in (c) at 44 years' remove.** It establishes that the story circulates, **not** that the paper existed or founded anything |
| `professor` / `Professor` | 0 / **3 occ / 2 files** — all three are "Professor of Physics at Rutgers University" (a 2000-era director bio: `0000912057-00-037385_def14a.txt` **l.740**, `0000912057-00-037385_0000912057-00-037385.txt` **l.797**, `0000950103-00-001294_0000950103-00-001294.txt` **l.503**) | **lexical decoy** (rule 6). The grader has no carrier; a "Professor" hit must not be read as the mentor |
| the grade itself | whole-word `grade`/`grades` **6 occ / 6 files**, all "investment grade" / "upgrade" boilerplate | **NO CARRIER.** "The professor gave it a low grade" is a **claim needing a carrier**, not a fact |
| `General Dynamics` (named early investor) | **family (a): 0 occ / 0 files.** Late family (c): **1 hit**, `fed-ex-corporation-fdx-proxy-statement-2014-09-29_djvu.txt` **l.9837**, inside a list of outside directorships ("Fox Networks Group … General Dynamics Corporation … GlaxoSmithKline plc") | **NO CARRIER** for the 1971 financing round; the one hit is a **2014 director-offices listing**, i.e. a decoy of the rule-6 class |
| `venture capital` | 3 occ / 2 files — both are "James L. Barksdale, Managing Partner, The Barksdale Group, a venture capital firm", a director bio | **decoy**; not an investor in FedEx |
| `Fred Smith Companies` (expected predecessor name) | **0 occ / 0 files** | **NO CARRIER** |
| `Air Scout` / `AirScout` / `Delta` | **0 occ / 0 files** (`Delta` = 0 in all 19 files) | **the predecessor-name / carrier-purchase leg has NO carrier in family (a)** |
| `Mayflower` (the operating-rights purchase in the popular account) | **0 occ / 0 files** | **NO CARRIER** |
| 1960s idea-to-company causality | no in-window document of any kind (0 of 2,157 indexed filings before 1997-11-04) | family (a) **cannot date the idea at all** |
| `Deregulation` | 0 occ / 0 files | the 1978 Airline Deregulation Act backdrop is absent from held text |
| **incursion into market** | **carried**: C3 `June 24, 1971` + C4 **`April 17, 1973`, 186 packages, 25 cities** | **a dated carrier DOES exist — but it is 1998-dated anniversary advertising quoting 1973, 25 years late, printed once.** Tier-1 *container*, Tier-4-grade *content*: **FACT only as to "the company publicly asserted this in 1998"; FOUNDER CLAIM / RETROSPECTIVE INTERPRETATION as to the event itself** |

**The dated-carrier requirement is met, weakly, and only for the launch — not for the idea.** C3+C4 give a
**June 24, 1971 Delaware incorporation** and an **April 17, 1973 first flight** out of the registrant's own
filing. That is enough to write Stage 1 as a *carrier chronology* and enough to reject a term-paper founding:
nothing in the record dates 1965 at all, and the earliest organisational fact the corpus can carry is a
Delaware incorporation plus a corporate secretary appointed "from June 1971" (C8). **The 1960s leg must enter
the register as `UNKNOWN / no carrier`, never as a dated event**; a line saying the company's origin "begins
with a 1965 paper" would be a §3 violation (a Tier-4 relay with nothing behind it in this corpus).

**Second-order lexical decoys, flagged so no later pass promotes them (rule 6):**
- `0000912057-01-001514_a2035201zex-10_1.txt` **l.1819-1820** cites *"Order 11755, December 29, 1973"* inside
  CLAUSE 9-1 CONVICT LABOR of a 2001 **USPS / Federal Express transportation agreement**. That is **Executive
  Order 11755** on convict labour — **not** a Civil Aeronautics Board order and **not** a 1973 act of the
  company. A grep for `1973` in this file returns it first; do **not** cite it as certification or route
  history. The same file carries *"Contract Disputes Act of 1978"* (l.1701), *"Public Law 89-176, September 10,
  1965"* (l.1723) and *"Veterans Readjustment Assistance Act of 1972"* (l.2559) — **a 1965 date does exist in
  this corpus, and it is a statute**, which is exactly how a term-paper year gets manufactured.
- **`Flying Tiger` 25 occ / 3 files** — all fleet and environmental-liability boilerplate about *The Flying
  Tiger Line Inc.* (e.g. `0000899243-98-001610…txt` **l.1219-1235**: "In November 1987, The Flying Tiger Line
  Inc. …"). It is a **later-acquired subsidiary**, not the 1971 predecessor, and the earliest held Flying Tiger
  sentence (l.1219) is dated **November 1987**, outside the origin window as briefed.
- **`1978` 12 occ / 10 files** — only the 4 C6 printings of the Form 8-A reference are about this company; the
  rest are the 1978 Contract Disputes Act and a 1978 Council resolution.
- **`1971` 19 occ / 7 files** — of these only **3** are company-history statements (C3 once, C7 twice as two
  renderings of the same director table); the remainder are director-bio years ("since 1971").
- **`186 packages`, `April 17`, `25 cities` each measured at 1 occurrence / 1 file**: the whole first-flight
  story of this dataset rests on one page of anniversary print. The 5 raw `watch` hits sit elsewhere (generic
  usage), so even the anecdote cannot be corroborated inside this corpus.

**Independence accounting (rule 4 + §3).** 19 stored documents, **19 distinct md5s** → no byte-identical
cross-shelf duplicate can inflate a count. But they collapse into **fewer lineages than files**:
`0000950103-97-000667` (S-4) + `0000950103-97-000724` (S-4/A) are **ONE** registration lineage; the four files
of accession `0000912057-00-034322` (10-K405 primary + ex-3_1 + ex-10_37 + ex-10_60) are **ONE** filing; the two
files of `0000912057-00-037385` (def14a + full submission) are **ONE**; the two files of
`0000912057-01-001514` are **ONE**. So the entire founding-sentence corpus (C3, C4, C5, C7) is **the
registrant's own corporate self-narrative, told 1998-2001 about events in 1971-1973 — one lineage,
corroboration count 1**, however many files print it.

**"Role recorded as founder" — the error is present in the corpus and it points at the wrong person.** The
only `Founder` title in all 19 filings attaches to **Sheridan Garrison, "Chairman and Founder of American
Freightways"** (`0000950103-00-001270_0000950103-00-001270.txt` **l.250-252**, **l.260-262**, 8-K filed
2000-11-15) — **a target company's founder**, in the sentence announcing his board seat. Census: `Founder`
**2 occ / 1 file**; lowercase `founder` **0 occ**; `founding` **1 occ / 1 file** (the C4 anniversary page).
Frederick W. Smith is called a founder by **no** held document — only an officer from 1971 / June 1971 (C7).
**Every register row for the investors, mentors or "the professor" must carry the role the carrier records, not
the role the folklore records, and must state `role_in_record = not stated` where the carrier is silent.**

STATUS: WRITTEN

---

## 4. The five family verdicts (stated as returns, never as hopes)

Vocabulary: **TRIED–ANSWERED** / **TRIED–UNANSWERED** (tool or network refused; remedy named) / **UNTRIED**
(§14.6, RD-097: an untried family may never be reported as a null).

| family | verdict | what was actually measured |
|---|---|---|
| **(a) SEC / EDGAR filings** | **TRIED–ANSWERED, but the answer is OUT-OF-WINDOW for events** | Full uncapped walk: 2,157 filings, perimeter **1997-11-04 → 2026-09-25**, **0 rows inside 1971-01-01→1985-12-31**. 19 documents / 3,913,000 B / 502,648 words stored by the forward recital pass (window `1985-12-31..2010-12-31`, `--max-docs 30`, `attempted 90`, `IDENTITY stored + unanswered + skipped == attempted -> OK`). It answers **the identity question at Tier 1** (C1, C2, C6) and carries **one** 1971 incorporation date and **one** 1973 launch sentence (C3, C4) — all from 1997-2001 documents, i.e. **24-30 years late**. **12 UNANSWERED rows, itemised in §6** — the largest refused count in tonight's intake |
| **(b) web archives** | **UNTRIED** (no scripted route, 0 bytes on disk; recorded as untried, never as a null) | `sources/web_archive/` does not exist for this company; `tools/` holds **no** CDX/Wayback tool (`ls tools/` → ca_endpoint_probe, company_status, fleet_intake, gates, harvest_mine, ia_text, id_mint, merge_census, periodical_harvest, scaffold, scaffold_company, sec_intake); `tools/queries.json` has **no `web_archive` family at all, fleet-wide** (family counter: chronicling_america 111, internet_archive 104, corporate_print 103, hathitrust 56, google_books 53). RD-134's NR-1 class. The family structurally cannot reach 1971-1985 (fleet floor mid-1990s, §14.6), which is a reason to record UNTRIED, not a reason to write a null |
| **(c) periodical corpora (Chronicling America / HathiTrust / Google Books / Internet Archive)** | **TRIED–ANSWERED at the query level (4 OCR layers arrived mid-pass, §10) — and the answer for Stage 1 is a decoy; CA / HT / GB remain TRIED–UNANSWERED** | 8 query blocks exist for fedex; **30 index rows** came back; **at first measurement 0 bytes had landed anywhere**, and the CA/HT/GB picture is still refusal-based: **7 of 30 rows carry a blank `http_status` = refusal, not emptiness**: CA 2/2 `UNANSWERED` (`CA 'Federal Express' Memphis Tennessee 1960-1995`; `CA 'FedEx' / 'FDX' air freight 1970-2000 (clipped-brand and ticker routes)`), HT 1/1 `UNANSWERED` (`HT 'Federal Express' Memphis air cargo (unbounded; ERA UNREFINED-WIDE)`), GB 1/1 `UNANSWERED` (`GB 'FDX Corporation' 'Federal Express' annual report shareholder (ticker-form registrant route)`), IA 2/23 `UNANSWERED` (`IA Federal Express periodical text 1965-1995`; `IA air-cargo/trucking trade press 1960-2000`) plus **1 IA `NULL`** on the trade-press query, which is the **facet-free** re-write (`IA air-cargo/trucking trade press 1960-2000 [FACET-FREE per RD-130]`, `http_status 200`) — a genuine returned-nothing on that question, and still not a corpus-wide null; whereas the two `UNANSWERED` IA rows carry **no** `[FACET-FREE]` label, i.e. they are the **faceted** originals, so RD-130's rule binds them: a faceted zero is a statement about our parameter. **What the delivered bytes actually are (§10 reads them line by line): 8 Internet Archive layers, 1,377,536 B at close (4 at the first measurement), none company print, none in-window about this company** — and the single in-window candidate in the entire index, `cia-rdp96-00788r001500120024-8` (1984-11-01, labelled `TIER1_CANDIDATE`), **is a declassified CIA procurement memo whose only `FEDERAL EXPRESS` strings (2) sit in a shipping-vendor/invoice field** (`_djvu.txt` l.74 "…RO FEDERAL EXPRESS USE", l.103 "GOVERNMENT PACKAGES … FEDERAL EXPRESS LOCATION SHOWN"). **Rule 6 confirmed by opening the file: the `TIER1_CANDIDATE` label was the query text echoing.** `periodical_harvest.py` / `harvest_mine.py` were not run by order. Of the 6 IA `TIER1_CANDIDATE` rows, **3 now
have bytes on disk** (§10: `DTIC_ADA273978`, and both CIA Reading Room items — the 1984 one being the only
in-window candidate the index holds for this company, and it is a decoy); the remaining 3
(`airlineindustry0000unse` 1992, `overnightsuccess0000trim` 1992 — **a biography, retrospective founder text
usable only as a RETROSPECTIVE SOURCE** — and `disciplineofmark0000trea` 1995) stay metadata labels, not text
(rule 6), and all three are out of window anyway. |
| **(d) digitised corporate print (annual reports, house organs, directories)** | **TRIED–UNANSWERED, 0 bytes** | `sources/corporate_print/` exists and is **empty (0 files)**. 3 `corporate_print` rows: 2 `UNANSWERED` with **blank http_status** (`CP fedex + predecessor annual/shareholder print 1971-2000`; `CP fedex corporate print by creator 1971-2000`) and 1 labelled `TIER1_CANDIDATE` — which is **`DTIC_ADA387307`, "Aircraft Accident Report: Crash during Landing Federal…", dated 1997-07-31**. Rule 6 fired exactly as predicted: the label is the query text echoing; the item is a **third-party DTIC-hosted accident investigation, out of window, and not company print at all**. **Zero in-window corporate-print bytes exist for this company** |
| **(e) auction / museum / manuscript** | **UNTRIED — and the family most likely to change this verdict. Explicitly UNTRIED, not TRIED–UNANSWERED, not a null** | No script reaches it: nothing in `tools/` queries a dealer, museum or finding aid; `ia_text.py` could read an item **only if an identifier were known**, and no manuscript identifier exists anywhere in the corpus (`grep -i "manuscript"` over `sources/sec/*.txt` → **0 occ**; `auction` 4 occ are S-3/S-8 plan-of-distribution boilerplate "bidding or auction"; `Smithsonian` 1 occ is an **award name** at `0001047469-99-032609…txt` **l.3531**, not a repository). Web budget 0. The legs family (a) cannot carry — the 1960s paper, the professor's grade, the **name the carrier was incorporated under**, the carrier purchase and renaming, and the **1978 Form 8-A below EDGAR's digital floor** — all live here. Routes in §6 |

**Counting toward §15.2:** families returning **in-window Tier-1 text = ZERO**. Family (a) returned Tier-1
*statements about* the window from *outside* it; (c) was tried and delivered 4 OCR layers during this pass, of
which **none contains a single in-window line about this company** (§10 — the only in-window item is a 1984
procurement memo using Federal Express as a shipping vendor); (d) was tried and refused without delivering a
byte; (b) and (e) were never touched. **No family is reported as a null, and no family is scored on an index
label — the two labels that mattered here (the 1984 CIA item and the DTIC accident report) were opened and
found to be decoys.**

STATUS: WRITTEN

---

## 5. Per-stage tiers (§15.2), each measured against that stage's own window (RD-112)

Windows below are **PROPOSED** and derived from dated carriers in §1-§2, not from a filename or a harvester
parameter (`harvest_mine.py` l.73's 1971-01-01→1985-12-31 is a search setting; the CSV has no founding column).

| stage | PROPOSED window | window justified by | families returning **in-window Tier-1 text naming the entity the stage is about** | tier | deliverable / cap | ≈ runs |
|---|---|---|---|---|---|---|
| **1 — origin: idea-to-carrier** | **1971-06-24 → 1978-12-15** | opens on the only in-window incorporation date the registrant prints (C3, 1998 10-K l.306); closes on the carrier's own **Form 8-A filed 1978-12-15**, the latest dated in-window corporate act referenced in held bytes (C6, 4 printings) | **ZERO.** (a) answered only from 1997-2001 documents *about* the window; (c) 7 blank-status refusals and **0 in-window lines about this company** in the 4 IA layers that arrived mid-pass (§10); (d) 0 bytes; (b),(e) UNTRIED. The single in-window harvest candidate, `cia-rdp96-00788r001500120024-8` (1984-11-01), falls in Stage 2 and **was opened this pass — `FEDERAL EXPRESS` appears in it only as a shipping-vendor field** | **T3 register — PROVISIONAL** | short narrative + registers; §K, §N, §U still mandatory; **8k w/stage** | **3-4** |
| **2 — scaling as a carrier** | **1978-12-16 → 1985-12-31** | begins at the registration act; ends at the brief's candidate ceiling, which held text neither supports nor contradicts (measured: nothing in held bytes is dated 1979-1985 at all; `1984`/`1985` appear only as a *Statute* year and a "since 1985" marketing claim at `a10-k405.txt` l.627) | **ZERO**, same reasons. The only candidate pointing into it is un-fetched metadata | **T3 register — PROVISIONAL** | **8k w/stage** | **3-4** |
| **3 — the registrant's own life** | **1986-01-01 → 1998-01-27** (proposed, unassessed) | opens on the Flying Tiger acquisition era (`0000899243-98-001610…txt` l.1219 "In November 1987"); closes on the Caliber/FDX merger consummation (8-K period `19980127`, `0000950103-98-000089…txt` header l.17-19) | family (a) **would** answer here — 770 indexed rows between 1997-01-01 and 2010-12-31, 14 of them already stored; tier **not assessed on this pass** (this probe owns Stage 1) | not issued | — | — |

**Tier rule applied literally (§15.2):** ≥3 in-window Tier-1 families = T1, 2 = T2, **≤1 = T3**. Stage 1 and
Stage 2 each return **0**, so both are **T3 register**, and the tier caps the *volume*, not the honesty: the
"we cannot know" deliverable is the point of a T3 (§15.2 last paragraph).

**Both tiers are PROVISIONAL in the RD-112 sense** — the same posture Ford's probe took. Three of five families
have no bytes at all, family (b) has no route, family (e) was never touched, and 126 recital-window filings
were never enumerated because `--max-docs 30` cut the stream (`_UNANSWERED.csv` last row). **A tier may not be
finalised while an untried family exists.**

**What would move the needle, stated falsifiably:** **two** families returning in-window Tier-1 text would make
Stage 1 **T2 core** (22k w/stage, 6-9 runs). The realistic pair is **(c) contemporaneous 1971-1978 newspaper
and trade-press print** (Memphis Commercial Appeal via Chronicling America; `Air Transport World` /
`Aviation Week` / `Forbes` via Internet Archive) **plus (e) a manuscript or regulatory record** (the Delaware
charter of the 1971 corporation, CAB/NATB case files, the founder's papers). Family (a) cannot join that count
at Stage 1 for the *events*: **no in-window filing can ever exist for CIK 1048911, because the registrant was
not incorporated until 1997-10-02** — that is arithmetic, not a tool limit (C1).

STATUS: WRITTEN

---

## 6. The 12 UNANSWERED, itemised — and the FETCH REQUESTs

`python`/`csv` enumeration of `sources/sec/_UNANSWERED.csv` (12 rows, header as in §0). **Comparative
measurement, stated narrowly:** 12 rows is the **largest of the 22 companies whose `_UNANSWERED.csv` was
written by the 2026-09-29 fleet intake** (next: verizon / ford / jpmorgan at 7), and the **3rd largest across
all 41 companies that have the file** (behind nvidia 15 dated 2026-09-25 and chevron 13 dated 2026-10-06) —
command: per-company `sum(1 for _ in csv.DictReader(...))` grouped by file mtime date, printed this pass.

**11 of the 12 are real document slots, all in four 2000-2001 accessions, all refused identically:**
`UNANSWERED (padded-cik/nodash-dir: 404 NoSuchKey | bare-cik/nodash-dir: 404 NoSuchKey |
bare-cik/dashed-dir: 404 NoSuchKey)` — i.e. the tool built the URL from the `primaryDocument` value
(`0001.txt`, `0002.txt`, …) recorded in `index.json` and S3 answered that no such key exists at any of the
three path forms. **The listing itself succeeded** (`listing via padded-cik/nodash-dir (12 items, 0 unnamed)`),
so the documents exist under some name the index did not carry — a **filename-resolution refusal, not an
archive gap**.

| # | accession | form / filed | refused slots | why |
|---|---|---|---|---|
| 1-2 | `0000950103-00-001270` | 8-K, 2000-11-15 | `0001.txt`, `0002.txt` | NoSuchKey ×3 path forms; 5 items listed, 0 unnamed |
| 3 | `0000950103-00-001294` | SC 13D, 2000-11-22 | `0001.txt` | same; 4 items listed |
| 4-7 | `0000931763-00-002718` | **S-4, 2000-12-13** | `0001.txt` (primaryDocument), `0009.txt`, `0003.txt`, `0002.txt` (index.json listings) | same; 12 items listed |
| 8-11 | `0000931763-01-000019` | **S-4/A, 2001-01-08** | `0001.txt`, `0006.txt`, `0002.txt`, `0005.txt` | same; 9 items listed |
| 12 | — | — | `listing:not-enumerated` | **"UNANSWERED NOT-ENUMERATED: 126 in-window filings were never listed because --max-docs 30 was reached"** — a tool-cut, not an absence |

**Second refusal bucket, reported because the tool put it in the wrong file.** `_SKIPPED.csv` holds **57**
rows whose status is `UNANSWERED NAMELESS-ROW: index.json listed a … item with an empty name (pre-2001
malformed directory); no URL can be built, content is reachable only through the full-submission
<accession>.txt` — 4 of them visible on the 1997 S-4 (a **556,200 B** unnamed item plus 837 B, 708 B, 583 B),
the rest on the other pre-2001 accessions. **`_RUN.json` reports `nameless_rows: 0`** while 57 such rows sit in
`_SKIPPED.csv`: the counter reads only the unanswered list, so tonight's headline arithmetic
`stored(19) + unanswered(12) + skipped(59) = 90 -> OK` hides 57 refusals inside "skipped". RD-112's defect #2
("a dropped row must be counted and reported, never vanish") recurs in a new form. **Honest tally: 69 slots
refused (11 doc + 1 not-enumerated line + 57 nameless), 19 stored.** Mitigation measured: the fallback the
status line itself names **did** run — the full-submission text `0000950103-97-000667_0000950103-97-000667.txt`
(568,308 B) is stored and carries the merger financials (C2) — so the 1997 S-4 nameless items are
**content-covered, not content-lost**. The 2000-2001 accessions have **no** stored full-submission file, so
those 11 slots are genuinely unread.

FETCH REQUEST: FR-1 (family a) — orchestrator runs, agent must not fetch by hand
```
cik: 0001048911
accessions: 0000931763-00-002718 (S-4, 2000-12-13), 0000931763-01-000019 (S-4/A, 2001-01-08),
            0000950103-00-001270 (8-K, 2000-11-15), 0000950103-00-001294 (SC 13D, 2000-11-22)
needed: the real primary-document filenames. `sec_intake.py grab --company-dir <dir> --accession <a>`
        with no --file lists the directory; or re-run auto with --max-docs 150 so the not-enumerated 126 are listed.
claim this settles: whether any 2000-2001 filing of the registrant recites a Federal Express history
        beyond the 1998 10-K's single June-24-1971 printing (C3) — i.e. whether the incorporation date has a
        SECOND, independently drafted carrier.
status if refused again: remains TRIED-UNANSWERED, never NULL.
```
FETCH REQUEST: FR-2 (family a, perimeter) — **126 recital-window filings never listed**
```
window: 1985-12-31..2010-12-31, cik 0001048911; command:
python tools/sec_intake.py auto "Fedex Corp" --company-dir founders_playbook/01_companies/company_050_fedex \
       --from 1985-12-31 --to 2010-12-31 --max-docs 150
CAUTION for whoever runs it: `auto` rewrites _MANIFEST/_UNANSWERED/_SKIPPED/_RUN unconditionally
       (sec_intake.py l.1369-1385); copy tonight's five register files to a dated sibling first
       (add-only; do not move or delete the originals).
```
FETCH REQUEST: FR-3 (family a, the paper-era gap) — **Federal Express Corporation Form 8-A filed 1978-12-15**
```
not on EDGAR (digital floor 1993-94). Referenced 4x in held bytes (C6) as "FedEx (as predecessor registrant)".
route: SEC Public Reference / paper-era accession retrieval by file number, or the DE Division of Corporations
franchise record for Federal Express Corporation (charter filed 1971-06-24 per C3).
claim this settles: the name the carrier was incorporated under, and whether 1971-06-24 is the charter date or
        a recital error -- the single most load-bearing undated-by-primary fact in Stage 1.
```
FETCH REQUEST: FR-4 (legacy registrant identity)
```
python tools/sec_intake.py index "Federal Express Corporation" --company-dir <dir>
  -> measured this pass: "NO-MATCH name (0 candidates)"; the tool resolves only via
     https://www.sec.gov/files/company_tickers.json (tickered issuers).
remedy: resolve the carrier's own CIK out of EDGAR's company_search (not company_tickers), then index it.
     A legacy Federal Express Corporation CIK would put 1981-1997 filings -- 16 years closer to the events
     than anything held -- inside reach.
```

STATUS: WRITTEN

---

## 7. Load-bearing Stage-1 questions, each with the carrier that could settle it

1. **Which founding act has a dated carrier, and which entity does it name?** Held answer: the carrier is
   **1998 print, not 1971 paper** — C3 (`0000899243-98-001610…txt` l.306-307) names **Federal Express
   Corporation, incorporated in Delaware on June 24, 1971, began operations 1973**, and C1/C2 name the
   registrant as a **different** corporation (Fast Holding Inc. → FDX Corp, 1997-10-02). Class: company
   self-narrative / **RETROSPECTIVE INTERPRETATION**, Conf **Medium** (Tier-1 container, verified TLS, but one
   lineage and 27 years late). Refused promotion: **the 1971 date is not a FACT until a charter or a
   contemporaneous 1971 document carries it** (FR-3).
2. **Was there a term paper, and did it found anything?** `Yale` 0, `term paper` 0, professor-as-grader 0
   (§3). **UNKNOWN / no carrier in this corpus.** Even if a paper exists, it is **not** an incursion into
   market and **not** a first experiment: the register's Stage-1 "first event" must be C3 (incorporation) or C4
   (first flight), and the 1960s leg can only appear as a `FOUNDER CLAIM, retrospective, no carrier` row.
   Route that could settle it: **family (e)** — see `## Untried` U-5.
3. **"The professor gave it a low grade."** 0 carriers (§3). A **claim needing a carrier**; the only grade words
   in the corpus are credit-quality boilerplate. If a grade story is ever published in a volume it must be
   attributed to the secondary source that repeats it, at Tier 4, chased to what it rests on (§5) — and nothing
   here shows what it rests on.
4. **Predecessor name and the renaming.** The brief's candidate lineage (FDX / Delta Airscout / a predecessor
   carrier bought for its operating certificate, later renamed Federal Express) has **0 carriers in family (a)**
   (`Delta` 0, `Air Scout` 0, `Mayflower` 0, `Fred Smith Companies` 0). What family (a) *does* hold is the
   registrant's own renaming chain (Fast Holding Inc. → FDX → FedEx Corporation, l.257 of the 10-K405) — the
   **wrong** renaming for the origin story. **Verdict on the predecessor leg: UNANSWERED in (a), UNTRIED in
   (c)/(d)/(e).** FR-3/FR-4 and U-2/U-3/U-5 are the routes; a CAB or Delaware charter record is the only thing
   that can date a carrier-purchase.
5. **The incursion-into-market claim (the one the method demands a dated carrier for).** Carried: **C4, "When
   Federal Express took flight on April 17, 1973, it delivered 186 packages to 25 cities"** — dated, specific,
   company-authored, but **1998 anniversary advertising**. Conf **Low-Medium**, capped at `Medium`: a single late
   self-report is one source; `High` requires a 1973 contemporaneous printing (U-2 CA, or the DOT/CAB
   certification record).
6. **Who is credited, by which document, with what role.** Smith: officer from June 1971 (C7), never "founder"
   (§3); Cox: Secretary from June 1971 (C8). The only `Founder` title in the corpus is **another company's**
   (C9). **No held document credits an investor, a mentor, a professor or a co-founder** — `General Dynamics` 0,
   `venture capital` = a director bio. Any such row must say `role_in_record = not stated`.
7. **First real experiment / first repeatable validation.** The corpus offers a *rhetorical* pair — "invented
   express distribution in 1973" (C5, 3 printings) and "invented express distribution 25 years ago" (8-K
   1998-02-02 l.525) — and no measured first result: **no in-window revenue, volume, aircraft count, headcount
   or loss figure exists in held bytes** (the anniversary page's "186 packages" is the only in-window quantity
   anywhere). Stage-1 `quantitative.csv` rows must therefore come from (c)/(d)/(e) or stay UNKNOWN; this probe
   found **0** in-window metrics.
8. **First incurred operational failure / first conflict with the state.** 0 carriers for 1971-1985 in family
   (a). Nearest held material is post-window and about other entities (the 1987 Flying Tiger EPA liability at
   l.1219-1235; DTIC accident reports 1993-1997 in the harvest index). **UNTRIED**, and the CAB/regulatory
   record (U-3) is the route that could answer it — 1970s night-air-freight certification disputes are exactly
   where a dated failure would live.

STATUS: WRITTEN

---

## Untried

One command per route. **None of these is a null**; every line states which family it belongs to and what it
could settle.

- **U-1 — (c) Internet Archive — PARTLY TRIED during this pass; 3 candidates still un-read.** The four rows
  that arrived are adjudicated in §10 (all out of window except the 1984 memo, which is a vendor-field decoy),
  so **this route is no longer untried — it is tried and returned nothing usable.** Still un-read:
  `airlineindustry0000unse` (1992), `overnightsuccess0000trim` (1992 biography — **retrospective founder text,
  usable only as a RETROSPECTIVE SOURCE**, and the single held item most likely to carry the term-paper and
  grade folklore as *folklore*, i.e. as a Tier-3 lead to be chased, not a source),
  `disciplineofmark0000trea` (1995). Command form for the next pass:
  `python tools/ia_text.py <identifier> --file <name>_djvu.txt --company-dir founders_playbook/01_companies/company_050_fedex --insecure`.
  A deeper page, now with a content filter that excludes the government/military corpora that produced all four
  decoys:
  `python tools/ia_text.py mine --q '"Federal Express" (Memphis OR "air freight" OR courier) -DTIC -cia-readingroom AND mediatype:texts' --rows 40 --pattern "Federal Express" --company-dir founders_playbook/01_companies/company_050_fedex --insecure`
  **(`harvest_mine.py` / `periodical_harvest.py` were not run, by order; this is the runner-less form.)**
- **U-2 — (c) Chronicling America, Memphis and national press 1971-1978.** Both fedex CA rows are UNANSWERED
  with **blank** `http_status`, so the family has never been answered at all:
  `curl -s "https://chroniclingamerica.loc.gov/search/pages/results/?andtext=%22Federal+Express%22+Memphis&date1=1971&date2=1978&dateFilterType=yearRange&state=Tennessee&format=json&rows=20"`
  → store under `sources/periodicals/CA/`. A 403-with-challenge or 404 keeps the family **UNANSWERED**; only a
  200 with rows answers it. This is the route that could turn C4's 25-years-late anniversary claim into a
  1973-dated contemporaneous one.
- **U-3 — (e/c) CAB / DOT and Delaware charter records — the regulatory spine of 1971-1978.** No script reaches
  NARA Record Group 398 (Civil Aeronautics Board) or the Delaware Division of Corporations. Needed: Federal
  Express Corporation's 1971-06-24 charter filing, its 1973 supplemental air-freight authorisation, and any
  certificate-transfer record for the predecessor carrier named in the popular account. Settles Q4, Q5, Q8.
- **U-4 — (c) HathiTrust and Google Books, never answered.** HT 1/1 and GB 1/1 rows are `UNANSWERED` with blank
  status; the HT query is even self-labelled "unbounded; ERA UNREFINED-WIDE". Routes:
  `curl -s "https://babel.hathitrust.org/cgi/ls?q1=%22Federal%20Express%22%20Memphis;a=srchls;anyall1=phrase;field1=ocr;rqn=1"`
  and `curl -s "https://www.googleapis.com/books/v1/volumes?q=%22Federal+Express%22+air+cargo+1973&maxResults=20"`
  → a 429 or zero-byte response is **UNANSWERED, not NULL**.
- **U-5 — (e) AUCTION / MANUSCRIPT / MUSEUM — TRIED or UNTRIED? UNTRIED, and it is the named route worth real
  effort.** No script, no identifier on disk (`grep -i manuscript` = 0 occ), web budget 0 — so nothing was even
  refused here; the family has simply never been asked. What it uniquely holds, and what no other family in
  this probe can supply: **(i)** the founder's own pre-company papers — the 1960s university paper, its grade,
  the professor who graded it; **(ii)** founding-era correspondence and the 1971 subscription/investment
  documents naming investors the proxy never mentions; **(iii)** 1973 launch ephemera (first airbill, the "186
  packages to 25 cities" day) that would make C4 contemporaneous; **(iv)** a house organ or in-flight magazine
  carrying 1971-1978 copy. Named repositories to query with a web budget or a new script: **Yale University
  Library, Manuscripts & Archives** (undergraduate papers / the named professor's papers); **the Smithsonian
  National Air and Space Museum** holdings (the corpus's single `Smithsonian` hit at l.3531 is an *award*, which
  is a lead to the museum relationship, not a repository record); **the corporate archive and the Memphis
  public-library / University of Memphis special collections** (local press clippings, the 25th-anniversary
  file); **auction-house lot records** for founder papers and founding-era documents. A dispatch here needs
  either a web budget or a `tools/` script; per §15.1 **no agent brief may include retrieval a script can
  reach, and this family has no script — so it must be dispatched with a budget, not improvised.**
- **U-6 — (b) web archives.** No tool exists fleet-wide and no `web_archive` task exists in `queries.json`
  (measured, §4(b)). If a script is written:
  `curl -s "http://web.archive.org/cdx/search/cdx?url=fedex.com&output=text&fl=timestamp,original,statuscode&from=1996&to=2004&limit=60"`
  → store under `sources/web_archive/`. **Zero in-window value for 1971-1985**; recorded so the family is
  queried rather than guessed at, and so RD-134's NR-1 defect (UNTRIED written as an attempted null) does not
  recur here.
- **U-7 — (d) corporate print, never answered.** Both CP queries returned blank-status UNANSWERED and
  `sources/corporate_print/` is empty. The one `TIER1_CANDIDATE` row is a DTIC accident report (§4(d)) and is
  discarded as a mislabel. Re-run facet-free with predecessor-name discriminators, e.g.
  `CP "Federal Express Corporation" annual report 1971-1985` with a `-DTIC -accident` exclusion — **but only
  once the entity question (which FedEx) is settled**, or it will mine the 1997-2001 holdco's print and call it
  the founder's company.
- **U-8 — (a) the un-enumerated tail.** 126 recital-window filings never listed (FR-2) and the legacy
  registrant never resolved (FR-4). All post-1985 for this CIK, so none can date a Stage-1 event; FR-4's legacy
  CIK is the only (a) route that could produce a **1981-1994** recital, i.e. one written 8-23 years after the
  events instead of 27.

STATUS: WRITTEN

---

## 8. Defects returned for the orchestrator (not evidence), and what this probe refuses to claim

**Defect findings:**
1. **`_RUN.json` reports `nameless_rows: 0` while `_SKIPPED.csv` holds 57 `UNANSWERED NAMELESS-ROW` rows** —
   the counter reads only the unanswered list, so the IDENTITY line `stored(19)+unanswered(12)+skipped(59)=90
   -> OK` reports 57 refusals as "skipped". RD-112 defect #2 in a new costume. (`sec_intake.py` l.1369:
   `nameless = sum(1 for u in unanswered if "NAMELESS-ROW" in str(u.get("status","")))`.)
2. **The "59 SKIPPED" here is NOT the `--max-docs` cut.** Ford's probe printed
   `SKIPPED beyond --max-docs N`; for fedex **0** rows carry that phrase (measured:
   `sum(1 for r in _SKIPPED rows if 'beyond' in r['why']) = 0`) — the 59 are 57 nameless + 2 plain listings.
   The max-docs loss instead went to `_UNANSWERED.csv` as one `NOT-ENUMERATED` row, which is then counted in
   the headline "12 UNANSWERED" next to 11 real document slots. **Two different failure kinds share one
   bucket**, so a reader cannot tell a 404 from a budget cut. Split them in the schema.
3. **Pre-2001 accessions whose `index.json` names a primary document S3 then rejects** (4 accessions, 11 slots,
   three path forms each): the URL builder trusts `primaryDocument` with no directory-listing fallback (FR-1).
4. **`sec_intake.py` cannot resolve a non-tickered registrant** (measured: `NO-MATCH … 0 candidates`; it
   resolves only via `company_tickers.json`), so a company whose origin entity was delisted or is now a
   subsidiary is **invisible to family (a)** — and that invisibility reads as "the ancestor filed nothing".
   Needs a CIK-by-name / company_search route (FR-4).
5. **`candidates.csv` mislabels a DTIC accident report as `corporate_print / TIER1_CANDIDATE`**, and offers a
   spam item (`cheapone`, "Buy Kenalog online") and a self-help book (`havenewhusbandby00lema`, twice) under a
   `Federal Express periodical text` query — the classifier matches query text, not content (rule 6). **For
   fedex, 0 of 30 index rows yield in-window evidence about this company**, so the whole periodical picture is
   label-only — **and §10, written at close, proves the phrase rather than assuming it: 4 of the 30 rows arrived
   as bytes during this pass, exactly 1 is dated inside the window, and its `FEDERAL EXPRESS` strings are a
   shipping-vendor field on a CIA form.**
   `queries.json` carries no discriminator excluding DTIC / NASA / CIA accident-and-military corpora, which
   dominate the fedex hits.
6. **No `web_archive` family exists anywhere in the fleet tooling** (restated for this company; RD-134 NR-1).
7. **`harvest_mine.py` WINDOWS fedex (1971-01-01→1985-12-31) is presented as a window** while
   `00_universe/fortune_top_50_2026.csv` has no founding column; this probe had to derive a Stage-1 opening date
   from a 1998 recital. The tool should print `SEARCH SETTING` next to its own window.

**Refused on this pass, each with the reason:**
- Refused to call **1971, 1973, or a 1960s term paper "the founding of FedEx"** in a FACT row. The registrant is
  the 1997-10-02 Delaware holdco (C1); "the carrier incorporated 1971-06-24 and flew 1973-04-17" is a
  **27-years-late company recital** (C3/C4, one lineage). Stage 1 may be written **about** 1971-1978 only with
  `RETROSPECTIVE SOURCE` labels and Conf ≤ Medium.
- Refused to treat the **graded-university-paper leg as an experiment or an incursion into market**, and
  refused the professor's grade outright (0 carriers, §3).
- Refused to promote any **`TIER1_CANDIDATE` label** in `candidates.csv` to Tier-1 status: none has bytes on
  disk and one is provably a mislabel (§4(d), defect 5). No family was scored on an index column.
- Refused to use **"Order 11755, December 29, 1973"**, the **1965 Public Law 89-176**, the **1978 Contract
  Disputes Act**, or the **1987 Flying Tiger** sentences as in-window company events (rule 6 decoys, §3).
- Refused to write any refused slot as a null: 12 rows itemised (§6), 57 nameless rows disclosed, 126
  un-enumerated filings named, FR-1…FR-4 issued instead of fetching by hand. **0 Web calls made.**
- Refused to count the 19 stored files as 19 sources: they collapse to **14 accessions and fewer lineages**, and
  the founding sentence is **one** self-narrative (§3).
- Refused to run `harvest_mine.py` / `periodical_harvest.py` (by order; and a second `auto` pass would have
  overwritten tonight's registers — §0), refused `gates.py` checks beyond the briefed `csv,keys`, and wrote no
  register, no volume, no ids, no certification. **Moved, deleted or renamed nothing** under `sources/`; the
  only other writes this pass were made by `sec_intake.py` itself to the CIK-keyed index files (the
  differently-CIK'd legacy copies were **left untouched**, per the tool's own guard).

**The route most likely to change this verdict:** **family (e)** — the founder's papers / university archive
behind the 1960s term-paper leg, together with the **Delaware charter and CAB record behind 1971-1973** (U-3,
U-5) — because it is the only family that can supply a document *contemporaneous with* the origin, which would
lift Stage 1 from T3 to T2 alongside the untouched Chronicling America route (U-2), where a 200-with-rows is
what finally carries the "incursion into market" claim in its own time instead of through a 1998 anniversary
advertisement.

STATUS: WRITTEN

---

## 9. Gate

Command (run before reporting; output written to
`founders_playbook/03_quality_control/fedex_s1_probe_gates.md`):
`python tools/gates.py --company-dir founders_playbook/01_companies/company_050_fedex --checks csv,keys --fail-on substantive --out founders_playbook/03_quality_control/fedex_s1_probe_gates.md`

**RAN 2026-10-06, exit code 0** (`--fail-on substantive` → not failed). Output:
`founders_playbook/03_quality_control/fedex_s1_probe_gates.md` —
**Findings: 2 | Passes: 0**, and **both findings are coverage-class, not substantive**:
`coverage | registers | no register CSVs at root or research/ -- csv/anchors gates DID NOT RUN` and
`coverage | narrative | no stage_*.md volumes found -- keys/anchors gates DID NOT RUN`;
summary line `coverage 0 registers, 0 stage volumes, 21 source documents` — the count **moved to 27 on the
re-run at this file's close**, because §10's late-arriving periodical layers were still landing while the
dossier was being written (the shelf is live; 19 SEC layers + 8 IA layers = 27 `.txt` sources). Either way the
2 findings are coverage-class, not substantive; the tool’s own note reads:
*"coverage-only findings … expected for a freshly probed company, and NOT failing the exit code unless
--fail-on all"*. The gate also independently read the tier it was told to check:
`tier: T3 (tier T3 from A_chronology_feasibility.md … the most recent write wins, §15.2 regrade)`.

GATE: PASS (substantive), 2 coverage findings as above.

---

## 10. Late-arriving bytes, accounted for (§14.11) — read at close

`find founders_playbook/00_universe/harvest -iname "*fedex*"` is still empty, but **`sources/periodicals/` was
created during this pass** (`ls -la` shows the directory itself timestamped after this probe's 11:47Z claim) and
now holds **4 Internet Archive OCR text layers, 658,180 B, + 4 sidecars** — the fleet facet-free re-harvest
(RD-134) delivering the fedex `internet_archive` rows **straight into the company directory**. Total
`sources/` file count moved 50 → **62** at 12:05Z and → **70** at this close. §14.11 requires each late document to be either cited or recorded as
considered-and-why-not; all four are read and adjudicated below. **Every one carries
`"transport": "UNVERIFIED TLS -- re-check before citing at High confidence"`** (sidecars, verbatim), so **no
layer is cited above Medium on this pass** — the Ford-precedent cap.

| layer (all under `sources/periodicals/`) | bytes / lines | sidecar `fetched` | what it is | in the brief's window 1971-01-01→1985-12-31? | verdict for Stage 1 |
|---|---|---|---|---|---|
| `cia-readingroom-document-cia-rdp96-00788r001500120024-8_djvu.txt` | 2,877 B / 129 l. | 2026-10-06T12:04:30Z | Declassified **CIA memo**, 01-Nov-84, "Contract Extension Dates, Request for" (To: LTC Brian Buzby, From: H. Puthoff, DA Project Letter Order 18 "DELEW-I-L") | **YES — the only in-window item the index holds** | **DECOY, now provably so.** `FEDERAL EXPRESS` = **2 occurrences**, both inside a shipping/invoice form field: **l.74** "YOUR NOTES/REFERENCE NUMBERS (FIRST 12 CHARACTERS WILL ALSO APPEAR ON INVOICE) … RO FEDERAL EXPRESS USE" and **l.103** "… GOVERNMENT PACKAGES … FEDERAL EXPRESS LOCATION SHOWN". Nothing about the carrier's founding, fleet, finance or route rights → **zero Tier-1 value for Stage 1** |
| `cia-readingroom-document-cia-rdp89-00063r000300260001-6_djvu.txt` | 34,244 B / 1,357 l. | 2026-10-06T12:05:51Z | CIA reading-room document, indexed **1987-02-17** | **NO**, outside the window by ~15 weeks | **Not Stage-1 evidence.** Its single `Federal Express` hit is a parenthetical courier list — **l.1199** "including United Parcel, Federal Express, etc. will be received" — a mention, not a subject |
| `DTIC_ADA273978_djvu.txt` | 295,534 B / 8,262 l. | 2026-10-06T12:05:09Z | DTIC monograph, indexed **1993**: "Benchmarking Practices of Air Cargo Carriers: A Case S…" | **NO** | **Not Stage-1 evidence, but the best third-party operational description on disk**: **l.4312-4314** "The Federal Express (FedEx) 'superhub' at the Memphis … FedEx's nighttime hub operations. During a four hour window …", **l.4352-4367** aircraft/container handling, **l.105** acknowledgements "to several people at UPS, FedEx, Emery" (OCR-mangled "Emexry", rule 6). **Tier-2, 1993; useful to a later stage, silent on 1971-1973** |
| `DTIC_ADA387307_djvu.txt` | 325,525 B / 12,859 l. | 2026-10-06T12:04:35Z | Aircraft **accident investigation**: "[MD-11] N611FE, operated by Federal Express, Inc. … flight 14, crashed while landing" | **NO** | **Not company print, not Stage 1** — this is the row §4(d) rejected as a `corporate_print / TIER1_CANDIDATE` **mislabel**, and the bytes confirm it. **l.605, l.645** the crash sentence; **l.183-185** "Cargo Operator Review and FedEx Postaccident Actions", "FedEx MD-11 Tailstrike Awareness". Note the carrier's legal name printed as **"Federal Express, Inc."** — a **fourth naming variant** for the register's `entity_named` column, alongside Federal Express Corporation (C3), FDX Corporation and FedEx Corporation (l.257) |

**Rule 4 re-checked on the new bytes:** `md5sum sources/periodicals/*.txt | uniq -d` → **0 duplicate digests**,
so these are 4 documents, not re-shelved copies of each other, and none duplicates anything in `sources/sec/`.
**They raise no tier:** in-window Tier-1 text about this company remains at **0 occurrences across all four
layers** (measured by the greps above). What they change is the *state* of family (c): it can no longer be
reported as "bytes never arrived" — it is **TRIED–ANSWERED, and the answer is that the fedex hits in the
harvest index are third-party government/military documents that merely mention the brand, not periodicals that
reported the founding.** That is a stronger result than a null and it redirects the remedy: **the missing family
for FedEx is not "IA text", it is contemporaneous *press* and *regulatory* print — U-2 (Chronicling America) and
U-3 (CAB / Delaware charter) — which is exactly where a Stage-1 volume must now be sent.** **Nothing was
deleted, moved or renamed**; the layers were read in place.

**Second wave (sidecars stamped 12:07:05Z-12:07:24Z) — the shelf is still filling, and this wave contains two
NEW CARRIERS, so it is recorded here rather than discarded: `sources/periodicals/` now holds 8 layers /
1,377,536 B** (measured twice more before this close; the count is moving because the fleet re-harvest is live,
which is itself the §14.11 condition the rule was written for):

| new layer | bytes / fetched | what it carries for the origin question | class |
|---|---|---|---|
| **`DTIC_ADA359870_djvu.txt`** (NTSB-format federal accident report, "In-Flight Fire/Emergency Landing Federal Express Fligh…", indexed 1998-07-22) | 349,897 B / 12:07:05Z | **C10 — §2 table extended.** **l.3420** heading "1.17 FedEx Organizational and Management Information"; **l.3422** "**FedEx began operations on April 17, 1973.** In fiscal year 1996, FedEx reported revenues of $10.3 billion … 325 airports … fleet of 559 airplanes" | **An independent origin under §3** — a U.S. federal safety investigation's own factual recital, not the company's marketing. It corroborates **C4's date** from outside the corporate lineage (publication 1998 = still outside the window; `143` FedEx mentions in the file) |
| **`DTIC_ADA540033_djvu.txt`** ("USCENTCOM's Intratheater Airlift: What Would FedEx Do?", indexed 2009-04-01) | 41,906 B / 12:07:24Z | **C11.** **l.278-280** "the Memphis-based shipping giant, **FedEx Corporation**, provided the optimal target because it has achieved consistent success **since its creation in 1971 by Frederick W. Smith**" | Tier-3 third-party, and **a live specimen of trap #5**: it attributes the 1971 creation to *FedEx Corporation*, the 1997 holdco's name — exactly the entity drift §1 documents. **Usable as evidence that the 1971-by-Smith claim circulates independently; NOT usable as a carrier for which legal person was created** |
| `fed-ex-corporation-fdx-proxy-statement-2014-09-29_djvu.txt` | 320,853 B / 12:07:18Z | l.411 `1971`, l.2512 "Director since: 1971", l.2521 "President of FedEx Express from 1971 to 1975" | **Same corporate-record lineage as C7 — one source, not two** (§3). Do not count as corroboration |
- | `cia-readingroom-document-06395705_djvu.txt` | 6,700 B / 12:07:08Z | 2 `federal express`/`fedex` hits, no founding content ("POSSIBLE FILMING", 2011) | Not evidence for Stage 1 |

**Consequence for the tier: none, and for confidence: real.** Under RD-112 a tier is measured against the
stage's own *window*, and every late layer post-dates 1985 or is a vendor-field mention, so **Stage 1 and
Stage 2 remain T3 register, PROVISIONAL, on 0 in-window Tier-1 families**. What C10 does is lift **C4's**
"April 17, 1973" from *one company self-narrative* to *company self-narrative plus an independent federal
record*, and C11 does the same for "1971, Frederick W. Smith" at Tier-3 with the naming error attached — so
**the launch date may be carried at Conf `Medium-High` (the UNVERIFIED-TLS cap still binds), while the
term-paper / grade leg still has no source, only a relay** (see the correction directly below: the folklore
does appear in these bytes, 44 years late, with a footnote to something not held).

**Correction, applied before this file left the editor (rule 8: a quantifier I had not yet measured).** An
earlier draft line here asserted "no `Yale`, no `term paper` in the 8 late layers". **That was false and is
withdrawn.** Measured by `grep -n -i "yale" *.txt` and `grep -ci "term paper"` over
`sources/periodicals/`: **`DTIC_ADA540033_djvu.txt` l.290-292** — *"Frederick Smith's empire developed from a
simple **term paper** as an undergraduate student at **Yale University**."* (with footnote marker "6", whose
source is **not held**). So **C12 = the term-paper leg's only carrier anywhere in this repository is a 2009
third-party military-student monograph repeating popular lore** — `FOUNDER CLAIM / RETROSPECTIVE`, Tier 3,
Conf **Low**, and a **lead to chase** (§5: a low-tier hit must be followed to what it rests on), never a fact.
The **grade** itself remains at **0 carriers in all 8 late layers and all 19 filings**. The same grep set found
`General Dynamics` exactly **1** time in the late bytes, at l.9837 of the 2014 proxy layer, inside a list of a
director's **outside board seats** — a decoy, not the 1971 investor (§3 table row corrected to match).

**A conflict the late bytes open, which the merge must carry as a `conflicts.csv` row.** First-day volume is
now attested two ways, by two lineages that cannot both be right as stated: **C4** (the company's own 1998
anniversary page, `sources/sec/0000899243-98-001610…txt` l.9217-9220) — *"took flight on April 17, 1973, it
delivered **186 packages to 25 cities**"* — against **C10's neighbour document** (`DTIC_ADA540033_djvu.txt`
**l.295**) — *"The **first two nights of operation delivered a mere seven packages**, yet through Smith's
persistence the company began to grow."* Both are decades-late; neither is in-window; **neither may be
promoted**. The register's correct state is `UNKNOWN` with a named conflict and a follow-up (U-2's 1973 press,
or the CAB/DOT record), and the popular "first night" number must never be written as a `DERIVED` figure from
these two.

**For the register: every one of these 8 layers must be**
entered with `event_date` inside 1971-1985 only where the *fact* is in-window (C10's 1973 date, C11's 1971
date) and `source_date` = 1998 / 2009, `evidence_class = RETROSPECTIVE`, `independence_note = third-party
federal record, not derivative of S00xx` for C10/C11 and `same lineage as the 1998-2001 proxies` for the 2014
proxy layer.**

STATUS: WRITTEN

---

## 11. Handoff

Stage 1 **T3 register, PROVISIONAL** · Stage 2 **T3 register, PROVISIONAL** · Stage 3 window proposed, tier
**not issued** · five families: (a) TRIED–ANSWERED-but-out-of-window, (b) UNTRIED, (c) **TRIED–ANSWERED with
4 late-arriving layers that are all out-of-window or decoys (§10)**, CA/HT/GB still TRIED–UNANSWERED,
(d) TRIED–UNANSWERED (0 bytes), (e) **UNTRIED — highest expected value** · 4 FETCH REQUESTs open ·
0 web calls made · **nothing in this file may be copied into a register as a FACT without the carrier named in
§2.**

STATUS: WRITTEN
