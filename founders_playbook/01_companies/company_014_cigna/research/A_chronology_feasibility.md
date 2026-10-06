# A — Chronology feasibility probe: `company_014_cigna` (Fortune rank 14)

Agent `probe-cigna`, Stage-1 feasibility PROBE. Owner of this path by `scaffold.py claim`.
Dispatch context: 2026-10-06. Method binding: `00_METHOD_AND_STYLE.md` §3, §13, §14, §15;
`MASTER_RESEARCH_LOG.md` RD-112, RD-124, RD-130, RD-134.

**One-line verdict.** Stage 1 (PROPOSED window 1979-01-01 → 1995-12-31) is **T2 core,
PROVISIONAL** — two families return in-window Tier-1 text (§6) — and the two families are
**INA Corporation's own 1979 annual report** and **three 1989-1995 US Supreme Court microfiche
records**. Both landed or were confirmed only at 17:22-17:23 tonight, and both are about
**ancestors, not this registrant**: no held document in any family names CIK 0001739940 before
2018, because that legal person is the 2018 Express Scripts shell (`Halfmoon Parent, Inc.`). On
the strict-registrant reading of the same window the count is 0 families → **T3 register**, and
that divergence, not a missing document, is the finding. The 1792 Philadelphia origin is printed
twice and only inside the ancestor's own 1979 self-report; the "1872 / 1850s" ancestor is
**UNTRIED** — its names appear in no query this repository has ever run for this slug (§4, §9).

**HEADER REGRADE, on the record (method §14.10: a retraction must reach the instruction layer).**
The first version of this line, written against the 17:20 corpus (4 non-SEC documents), read
"Stage 1 … is **T3 register, PROVISIONAL**" and asserted that the two ancestor dates "occur **0
times in every held byte**". Both halves are superseded: at 17:22-17:23 the fleet mine re-ran this
slug and the shelves became 13 files / 11 distinct documents (§2 correction; §3b; §4 census).
`1792` now occurs **2** times; `1872` still occurs **0**; `1982` still pairs with no merger
sentence anywhere. Only the tier and the 1792 count changed. The 17:20 text is preserved here as
the retraction rather than deleted.

STATUS: WRITTEN

---

## 1. Windows — proposed, and why the inherited one is a search setting

`00_universe/fortune_top_50_2026.csv` header enumerated before any field was read
(hard rule 3), verbatim:

```
rank,company,revenue_usd_millions,revenue_fiscal_year,profit_usd_millions,hq_city,hq_state,
fortune_industry,universe_source_url,verified_by_second_source,confidence,notes
```

There is **no founding-date column** — confirmed by reading the header, not by assuming it.
The rank-14 row is `14,Cigna Group,274900,fiscal year ended 2025-12-31,5957,Bloomfield,
Connecticut,Health Care: Pharmacy and Other Services,…,SEC EDGAR 10-K XBRL: exact match on
revenue and profit,High,…`. So no window below is evidence; each is a PROPOSED measurement
frame, and per RD-112 each tier is judged only against its own window.

| stage | window (all PROPOSED) | basis for the frame |
|---|---|---|
| Stage 1 | **1979-01-01 → 1995-12-31** | inherited from `harvest_mine.WINDOWS` / `research/A4_harvest_mine.md` l.3. Chosen wide *because* the founding date is unestablished: narrowing it here would silently discard the bytes that could establish it. It brackets the decade before the 1982 name (asserted, not measured) through the mid-1990s. |
| Stage 2 | 1996-01-01 → 2018-05-15 | the day before the registrant's first EDGAR appearance to the day before it exists on EDGAR; held corpus inside this frame: **0 of 30** stored documents (§2). |
| Stage 3 | 2018-05-16 → present | the registrant's own measured EDGAR lifetime; all 30 stored documents and all 9 accessions sit here. |

**The frame conflict this probe has to name, not paper over.** On a strict *registrant*
reading, Stage 1 of CIK 0001739940 begins in Delaware in 2017-2018 as **Halfmoon Parent, Inc.**,
the shell the bytes prove this registrant to be (§3). Under that reading the 1979-1995 window is
a **predecessor window on the registrant's own paper** — Ford's worked example in RD-134 with the
polarity inverted. I keep the fleet's 1979-1995 frame as Stage 1 because the brand line and the
operating carrier line are what the playbook is about, but every date attached to it below is
labelled by *which legal person* the byte attaches it to. Where the corpus holds nothing for an
ancestor, that family is reported UNANSWERED/UNTRIED for **that ancestor**, never as
"no evidence exists".

STATUS: WRITTEN

---

## 2. Perimeter — measured, and it is a fact, not a null

Two passes exist for this company, and their results are recorded in the fleet state file,
which I read rather than re-ran (per dispatch instruction; `harvest_mine.py` and
`periodical_harvest.py` were left alone because the fleet lanes are writing them tonight).

`00_universe/_FLEET_INTAKE.tsv` row 18, verbatim:
`cigna ⇥ Cigna Group ⇥ company_014_cigna ⇥ rc0/inwindow0/UNANS0 ⇥ 0 ⇥ rc1/inwindow27/UNANS1 ⇥ 30 ⇥ 2018-05-16 ⇥ no ⇥ ⇥ DONE`
and `_FLEET_INTAKE_lane1.log` l.7: `cigna          p1=0 p2=30 floor=2018-05-16`.

- **In-window (Stage-1) pass stored 0 documents.** Not "CIGNA filed nothing in 1979-1995".
- **Forward recital pass stored 30**, measured filing floor **2018-05-16**. Those 30 are late
  for every proposed window: earliest stored document 2018-05-16, latest 2019-01-07
  (`sources/sec/_MANIFEST.csv`, 30 rows, field `filingDate` — header enumerated first).
- **The archive walk was NOT capped** (RD-134's defect is not biting here).
  `sources/_index/submissions.csv`: 1,018 rows, fields
  `filingDate,form,accession,reportDate,primaryDocument,source`; distinct `source` values
  = `recent` + `CIK0001739940-submissions-001.json`; 0 blank `filingDate`; 0 rows named
  `reportDate`-less matter; 29 distinct forms; min 2018-05-16, max 2026-09-08.
  `_INDEX.md`: "1018 filings enumerated; 0 submissions rows dropped…; **UNANSWERED slices:
  (none)**"; registrant guard **ok** — slug token `cigna` matches registrant `Cigna Group`.
  So the pre-2018 silence is *complete-enumeration* silence, which is the strongest form the
  negative can take.
- **Why the silence is structural, not evidential:** EDGAR's own floor is 1993-94
  (brief; RD-134), and CIK 0001739940 is a 2018-vintage registrant. The CIGNA Corporation that
  operated 1979-1995 filed under **a different CIK that has never been indexed in this
  repository** — see FETCH REQUEST FR-1. Family (a)'s Stage-1 answer is therefore
  "TRIED–ANSWERED as a perimeter / **UNTRIED for the predecessor registrant**", not a null.
- **One UNANSWERED inside family (a)**: `sources/sec/_UNANSWERED.csv` (1 row, header
  enumerated) — "18 in-window filings were never listed because `--max-docs 30` was reached;
  their documents exist but are unknown to this run". Remedy FR-3. `_SKIPPED.csv` is header-only
  (0 skipped slots).
- **Held bytes, counted and de-duplicated.** `sources/sec/` = 30 documents (35 entries incl. 5
  state files), 36,011,843 B / 1,499,314 words (`_RUN.json`). Non-SEC shelves at dispatch time:
  "30 sec, 4 corporate print, 8 periodicals" → 2 `.txt` + 2 sidecars in `corporate_print/`,
  4 `.txt` + 4 sidecars in `periodicals/`. md5 across shelves:
  `micro_IA40386012_1635` = `0a9920515c05f5046af09a03e051117e` in **both**, and
  `cia-…rdp84b00130…` = `4467e3bfabf010d70678580a161d726d` in **both** →
  **4 distinct documents, not 12** (hard rule 4). Two documents are one document stored twice;
  they corroborate nothing about a family split.
  **THIS MOVED UNDER ME — read before quoting any number above.** At 17:22-17:23 local
  (`ls --time-style`, files timestamped `10-06_17:22`/`17:23`) the fleet mine re-ran against this
  slug and six new text layers landed in `sources/periodicals/`, and
  `research/A4_harvest_mine.md` itself was rewritten (mtime now **2026-10-06 17:23:11 +0530**,
  5,611 B, re-read in full before use). The shelves are now **13 `.txt` files = 11 distinct
  documents** (md5: still exactly 2 duplicate pairs, `uniq -d | wc -l` = **2**). §3.5-§3.7 are the
  new evidence; §3.4 is the original. Anything in this dossier that says "4 documents" is a
  measurement of the 17:20 state, and is superseded by §4's census, not by a re-derivation.
- **§3 lineage collapse on the SEC side:** 30 documents = **9 accessions** = **5 documentary
  sources**: one registration lineage (S-4 2018-05-16 + S-4/A 2018-06-20, 07-09, 07-12, 07-16,
  23 files) and four independent 8-K accessions (2018-09-21 4 files, 2018-12-20 2, 2018-12-26 2,
  2019-01-07 2). The five S-4-family documents are ONE source however many files they are, so the
  "incorporated in Delaware in 1981" recital is **one** recital, not five corroborations.

STATUS: WRITTEN

---

## 3. What the held bytes actually print about identity and ancestors

All line numbers are raw line numbers in the stored file.

**3.1 The registrant is the 2018 shell, and the bytes say so twice.**

- `sources/sec/0001140361-18-024107_s002268x1_s4.htm` **l.52**: cover page of the S-4 —
  "FORM S-4 … **HALFMOON PARENT, INC.** (Exact name of registrant as specified in its
  certificate of incorporation) Delaware … 6324 (Primary Standard Industrial Classification Code
  Number) **82-4991898** (IRS Employer Identification Number) c/o Cigna Corporation, 900 Cottage
  Grove Road Bloomfield, Connecticut 06002".
- `sources/sec/0001140361-18-045493_form8k.htm` (8-K, event 2018-12-20) **l.35 / l.77**: the
  registrant is now "Cigna Corporation", Delaware, **EIN 82-4991898** — *the shell's EIN, carried
  forward* — with "**Halfmoon Parent, Inc.** (Former name or former address, if changed since
  last report)".
- same file **l.164-165**: "… by and among **Cigna Corporation (now known as Cigna Holding
  Company)**, a Delaware corporation ("Cigna"), Express Scripts Holding Company …, **Halfmoon
  Parent, Inc. (now known as Cigna Corporation)**, a Delaware corporation and a direct wholly
  owned subsidiary of Cigna prior to the Merger ("**New Cigna**)".
- same file **l.170-172**: "Merger Sub 1 merged with and into Cigna (the "Cigna Merger"), **with
  Cigna surviving** the Cigna Merger **as a direct wholly owned subsidiary of New Cigna** …
  Cigna and Express Scripts became direct wholly owned subsidiaries of New Cigna."

Read together this is the clean statement of the trap: the 1981 Delaware operating company
**survived as a subsidiary of the registrant**; the registrant is the former shell that took its
name. `EIN 82-4991898` occurs in 3 stored documents; the older corporation's EIN (whatever it
is) occurs **0** times in the corpus — measured, §4. **No held byte gives Halfmoon's own date of
incorporation.** Its registrant's-own-origin date is therefore UNANSWERED, not 2018-05-16 (which
is a filing floor, not a birth).

**3.2 The earliest year-bearing incorporation recital in the corpus — and its subject.**

`s002268x1_s4.htm` **l.4995** and **l.23191** (the same sentence in the summary and in Item 1,
same lineage): "**Cigna was incorporated in Delaware in 1981.** Cigna is a global health services
organization…" The adjacent recitals in the same passage name two *other* legal persons:
**l.5005** "Express Scripts was incorporated in Delaware in April 2012"; **l.5007** "Express
Scripts, Inc. was incorporated in Missouri in September 1986 and reincorporated in Delaware in
March 1992." So the corpus's year-bearing incorporation sentences describe **Cigna Corporation
(1981)**, **Express Scripts Holding (2012)** and **Express Scripts, Inc. (1986/1992)** — none of
them CIK 0001739940.

**3.3 The two ancestors appear by name, and appear with no date at all.**

- `sources/sec/0000950159-18-000404_ex4-1.htm` (Indenture, 8-K 2018-09-21) **l.2584**:
  ""Designated Subsidiary" means each of **Connecticut General Life Insurance Company** and
  **Life Insurance Company of North America**, so long as it remains a Subsidiary, or any
  Subsidiary which is a successor of a Designated Subsidiary."
- `sources/sec/0000950159-18-000404_ex4-2.htm` **l.72**: the same clause, listing "Cigna,
  Connecticut General Life Insurance Company, Life Insurance Company of North America, Express
  Scripts, Express Scripts, Inc. and Medco Health Solutions, Inc."

This is worth having: the registrant's own 2018 document family prints **both ancestor legal
persons as named subsidiaries** — one per ancestor family, in the family (a) lineage the probe
can actually reach. What it prints is *existence in 2018 as subsidiaries*, plus a "successor of a
Designated Subsidiary" clause. It prints **no formation date, no city, and no combination year**
for either. `"INA Corporation"` — the short-form ancestor name the harvester searched — occurs
**0 times** in every held byte; only the long form does.

**3.4 The one genuinely in-window Tier-1 document, and what it names.**

`micro_IA40386012_1635` (149,218 B; stored under both `corporate_print/` and `periodicals/`).
Its own head, l.1-27: "In The **Supreme Court of the United States**, October Term, 1994 …
DR. JOSEPH C. DEBLASE, AND BEN CERRA, Petitioners, **CIGNA INDIVIDUAL FINANCIAL SERVICES
COMPANY, CIGNA CORPORATION; CIGNA SECURITIES, INC.; NICHOLAS DISETTE**, Respondents", with the
receipt stamp "APR 19 1995". The harvest index titles it
`DeBlase v. CIGNA Individual Financial Services Co., 515 U.S. 1 (1995)`.
**l.2486-2487** is the ancestor sentence: "Subsequent to the filing of this litigation, CSI and
CIFSCO merged to form **CIGNA Financial Advisors, Inc.**, a wholly-owned subsidiary of
**Connecticut General Corporation**, whose ultimate corporate parent is **CIGNA Corporation**."

So the best held in-window document is a **third-party judicial record** (§5 Tier 1) that names
`CIGNA CORPORATION` as a party and names a **`Connecticut General Corporation`** parent, in
1994-95. It is an independent corporate-structure fact — and it attaches to neither of the two
ancestor formation dates. It is the reason family (c) counts for Stage 1 (§6) and the reason the
tier cannot go higher: it names a *predecessor*, not this registrant (hard rule 5).

STATUS: WRITTEN

---

## 3b. The ancestors DO print — but only one of the two families, and neither for this registrant

Six layers landed at 17:22-17:23 tonight. Three of them are the first origin-bearing text this
company directory has ever held.

**3b.1 INA Corporation's own 1979 annual report — the Philadelphia ancestor, with its date.**
`sources/periodicals/INAC2115_1979_djvu.txt`, 111,357 B, item title in the harvest index
`INA Corporation (1979)` (collection `larc`, University of Alberta microfiche).
- **l.1**: "INA Corporation/Annual Report 1979"
- **l.4-7**: "INA Corporation is among the nation's oldest commercial organizations. **Its
  history dates back to 1792, with the formation of its principal subsidiary and the nation's
  first stock insurance company, Insurance Company of North America.**"
- **l.371-372**: "…conducted primarily through Insurance Company of North America, **founded in
  1792 as America's first stock insurance company**…"
- **l.16-17**: "the headquarters of INA Corporation **in Philadelphia**."

`1792` occurs **2** times in the whole corpus and both are in this one document (census, §4).
This is **digitised corporate print returning in-window Tier-1 text** — an annual report is a
Tier-1 source under §5 — but read its epistemics exactly: it is a **retrospective self-narrative
printed in 1979 about an event 187 years earlier**, by a **different legal person** (INA
Corporation), and the sentence attributes 1792 to INA's *principal subsidiary*, not to INA
itself. It is one lineage, not two: no second document in the corpus repeats or contests it.

**3b.2 The 1991 Rule 29.1 statement — the two-ancestor structure, with no dates.**
`sources/periodicals/micro_IA40385013_0186_djvu.txt` (Pierre v. Connecticut General Life
Insurance, 502 U.S. 973 (1991); 164,349 B, 7,065 lines), **l.6110-6116**:
"The parent of both **Connecticut General Life Insurance Company ("CGLIC")** and **Life
Insurance Company of North America ("LINA")** is **Connecticut General Corporation**. The parent
of Connecticut General Corporation is **CIGNA Holdings, Inc.** The parent of CIGNA Holdings, Inc.
is **CIGNA Corporation**." — plus **l.6067** "CIGNA Companies 1050 Connecticut Avenue, N.W."
A **third-party judicial** filing (Tier-1, §5), in-window, that independently establishes the
*structure* the brief describes — two named carriers, one Connecticut body and one North-America
body, sitting under the CIGNA names — and establishes **nothing about when either was formed**.
The two independent 1979-1991 lineages (INA self-report; court record) agree on the existence of
both ancestors and cannot disagree on dates, because neither makes a date claim about the
Connecticut one.

**3b.3 The other new layers.** `micro_IA40385019_1642` (Creative Bath Products v. Connecticut
General Life Insurance Company, 1989, 94,646 B — CG named as a party at l.15, l.190, l.203,
l.498; `CIGNA` does not print). `assessingitperfo00wils` (1988, 62,186 B) — the mine promoted it
`TIER1_CANDIDATE_TEXT`, `promoted by cigna  corporation`, and the bytes show why: **l.48-57** is a
*research-sponsor acknowledgment list* ("…working partners in research are: American Express
Company / British Petroleum Company / BellSouth Corporation / **CIGNA Corporation** / Digital
Equipment Corporation…"). A naming, zero chronology — RD-124's lesson that a promotion label must
be opened, not trusted. `ERIC_ED460893` (1995, 125,176 B) and the two new CIA reading-room
memoranda (1983, 1987) are decoys (§5).

STATUS: WRITTEN

---

## 4. The term census — every quantifier in this dossier, with how it was got

Command, run from `company_014_cigna/sources/` (text normalised: tags stripped, lowercased, every
non-alphanumeric run → one space, then substring-counted; the SEC side is represented by 4 files —
the S-4 primary, the two 2018 indenture exhibits and the 2018-12-20 8-K — because 23 of the 30
stored SEC files are the same registration lineage or indenture boilerplate, and counting a recital
five times is what RD-124 warns about):

| term | 13 non-SEC shelf files | 4 representative SEC docs | what the number means |
|---|---|---|---|
| `1792` | **2** | 0 | both in `INAC2115_1979` l.5, l.371 — the Philadelphia ancestor's self-dated origin |
| `1794` / `1805` | 0 / 0 | 0 / 0 | no rival INA date prints anywhere held |
| `1872` | **0** | **0** | the second ancestor family: nothing held *and* nothing queried (see note) |
| `1850` / `1851` / `1853` / `1865` | 1 / 0 / 0 / 0 | 0 | the lone `1850` is `ERIC_ED460893` l.1133 "in 1850 New Haven with a…" — an education-statistics sentence |
| `1982` | 20 | **0** | `INAC2115_1979`'s own 3 hits are debt tables / redeemability (l.3760 `1982-$14,465,000`, l.3774, l.3873); **0 lines in any held file pair `1982` with `merg/comb/union/formed`** (measured) |
| `connecticut general` | 130 | 3 | splits as `…assembly` **18 lines** (decoy) / `…life insurance` **25 lines** / `…corporation` **3 lines** |
| `life insurance company of north america` | 19 | 3 | the INA ancestor's full name, in a court record and in the 2018 indentures |
| `ina corporation` | 27 | **0** | the short form lives only on the print/periodical shelves; **no SEC byte in this corpus uses it** |
| `cigna corporation` | 28 | 52 | of the 4 SEC docs, 52 occurrences are one S-4 lineage reusing the name — §3 forbids counting them separately |
| `cigna holdings` | 2 | 0 | only `micro_IA40385013_0186` l.6114-6115 |
| `first stock insurance` | 2 | 0 | only `INAC2115_1979` l.6, l.372 |
| `immigration life` / `continental life` / `state fidelity` / `farmers and merchants` | **0 / 0 / 0 / 0** | **0 / 0 / 0 / 0** | a **query-scope** zero, not a corpus zero — see note |
| `philadelphia` | 20 | 20 | and all 20 SEC hits are Express Scripts' PA-address boilerplate, not an origin |
| `hartford` | 17 | 0 | Connecticut General's home city, printed only in the new court/ERIC layers |
| `incorporated in Delaware in 1981` | 0 | **2** | one recital, twice in the same S-4 lineage (l.4995, l.23191); subject = Cigna Corporation |
| `82-4991898` (registrant's EIN) | — | 3 | carried unchanged from Halfmoon Parent, Inc. (8-K 2018-09-21) into Cigna Corporation (8-K 2018-12-20) |

**The vocabulary finding, which is what changes the meaning of the zeros.**
`tools/queries.json` **l.635-659** is this company's entire query block — 8 tasks: 2
chronicling_america, 2 internet_archive, 1 hathitrust, 1 google_books, 2 corporate_print. Its
entity vocabulary is, in full: `CIGNA`, `"Connecticut General"`, `"INA Corporation"`
(the `q` at l.644 is `(CIGNA OR "Connecticut General" OR "INA Corporation") AND mediatype:texts
AND YEAR:[1900 TO 1995]`). **`Continental Life`, `Immigration Life`, `State Fidelity` and
`Farmers and Merchants` appear in no cigna task.** So the ancestor the dispatch brief traces to
"an 1850s-1872 life-insurance body" has been searched for by **neither name this repository
knows**, and its zeros are reported as **UNTRIED for that ancestor family**, never as
"no evidence exists". The block's own `_note` (queries.json l.637) already says it: "NAME-VARIANT
HYPOTHESES below are routes to predecessor registrant names, flagged as hypotheses: **no document
in this repository names them yet**."

STATUS: WRITTEN

---

## 5. Decoys measured (hard rule 6 / RD-124 / the Berkshire place-name trap)

| item | bytes | why it reads as evidence | what the bytes actually are |
|---|---|---|---|
| `cia-…rdp84b00130r000600010246-7` | 4,428 | stored under `corporate_print/`; prints "Connecticut General" ×2 and 1982/1981 | CIA **staff-meeting minutes of 9 April 1980**: l.27/l.30 "Connecticut General has agreed to a withdrawal of 50 percent… to save the VIP account" is **the Agency's own VIP income fund / Credit Union**; l.38-40 the 1982/1981 years are **the Agency's budget**. Not corporate print of any carrier. Its shelf placement is a harvester error. |
| `micro_IA41153629_0618` | 54,748 | 5 "Connecticut General" hits, 1992, in-window | ERIC ED357426 *Connecticut Task Force on Charter Schools Report* — "**Connecticut General Assembly**". The pure place-name trap. |
| `ERIC_ED460893` | 125,176 | 1995, in-window, "Connecticut General" ×18 lines | *The Connecticut General Assembly: Teacher's Manual for Visitation* — same trap. |
| `micro_IA40386012_1635` | 149,218 | 3 × "1981", 1 × "1982" | all four are **Missouri reporter citations** (l.198, l.908, l.966, and l.2228 `Marler v. House, 637 S.W.2d 365, 367 (Mo. Ct. App. 1982)`). |
| `cia-…rdp88t00792r000300040001-2` | 43,176 | 1988, "US firm Cigna" | CIA *Africa Review*: l.1174 South-African disinvestment roundup; l.1334 "repayment of its 1982 loan" — a sovereign loan, not a combination. |
| `cia-…rdp91-00929r…` / `cia-…rdp90g00152r…` | 24,680 / 36,048 | 1-2 bare-word hits each | CIA memoranda; `rdp91` l.1071 is OCR of a chemical process ("water-~nitric acid system. CIGNA, Rez DI CAVE, S.ej3"). `rdp90g` l.1431/1436 is a real "CIGNA Consumer Marketing Department" advertisement reference — bare-word class, no chronology. |
| `assessingitperfo00wils` | 62,186 | index label **TIER1_CANDIDATE_TEXT** | label earned honestly (l.57 `CIGNA  Corporation`) but the passage is a **sponsor acknowledgment list**. Naming ≠ chronology. |
| 45 + 4 index rows labelled `TIER1_CANDIDATE` | — | the word "CANDIDATE" | RD-124: these echo the **query text**, not the document. The great bulk of the cigna IA candidates are CIA reading-room memoranda, ERIC/legislative documents or USDA/NIH items. **None was counted in any tier verdict here.** |

STATUS: WRITTEN

---

## 6. Five-family verdict table — every family gets an explicit state

| # | family | state | measured basis | in-window Tier-1 text for Stage 1 (1979-01-01→1995-12-31)? |
|---|---|---|---|---|
| (a) | **SEC / EDGAR filings** | **TRIED–ANSWERED as a perimeter; UNTRIED for the predecessor registrant** | 1,018 filings enumerated, **0 UNANSWERED slices**, perimeter **2018-05-16 → 2026-09-08**; 30 docs stored, all 2018-05-16→2019-01-07; the in-window Stage-1 pass stored **0**; 18 filings of the run's own window never listed (`_UNANSWERED.csv`) | **NO.** And the NO is structural: this registrant's EDGAR life begins 23 years after the window closes, EDGAR's own floor is 1993-94, and the CIGNA Corporation that filed 1981-2018 has **a CIK this repository has never indexed** (FR-1). Not "the company filed nothing". |
| (b) | **Web archives** | **UNTRIED — 0 calls** | the directory listing of this company dir shows **no `sources/web_archive/`** at all; no sidecar and no `http_status` residue anywhere under it, so this is **not** the Microsoft NR-1 class — the route was genuinely never attempted | NO — a search never run. |
| (c) | **Periodical corpora** (IA magazine/newspaper/government-microfiche text, Chronicling America, HathiTrust, Google Books) | **TRIED–ANSWERED for the IA main thread; TRIED–UNANSWERED for Chronicling America and HathiTrust; TRIED–ANSWERED as leads-only for Google Books** | Mine read 12 of 79 candidate rows (`A4`, mtime **2026-10-06 17:23:11**): 2 `TIER1_CANDIDATE_TEXT`, 5 `VARIANT_TERM_HIT`, 3 `BARE_WORD_MATCH`, 2 `UNANSWERED` (HTTP 503 after 3 tries), **65 UNTRIED at `--limit`**. Real namings held: `micro_IA40386012` (1994-95), `micro_IA40385013` (1991), `micro_IA40385019` (1989). CA: **all 4 cigna rows are 404/UNANSWERED**, and `00_universe/harvest/_CA_ENDPOINT_TEST.md` records **7 of 7 URL shapes CHALLENGED (403, Cloudflare)** with "ANSWERED shapes: none" and "no CA zero may be cited as a null". HT: 1 row, no status recorded. GB: 11 rows, **0 bytes fetched**. | **YES** — three US Supreme Court microfiche records (Tier-1 court text) in-window naming CIGNA Corporation / Connecticut General Life Insurance Company. Their subject is the **predecessor**, not this registrant. |
| (d) | **Digitised corporate print** (annual reports, house organs, directories) | **TRIED–ANSWERED by document class — but the answer arrived off-shelf; TRIED–UNANSWERED as the harvester's own `corporate_print` task** | `INAC2115_1979`, INA Corporation's **1979 Annual Report** (111,357 B), prints its own 1792 origin narrative (l.4-7, l.371-372) — the family's first genuine member here. It was fetched by the `internet_archive` task and stored in `sources/periodicals/`, **not** in `sources/corporate_print/`. Both tasks labelled `corporate_print` (queries.json l.654-659) carry `year_range: [1940, 1998]` — the **YEAR facet RD-130 measured as manufacturing corporate-print nulls**: they returned 3 rows, all LEAD_ONLY decoys, and `candidates.csv` holds **0 facet-free `corporate_print` rows for ANY company** (measured: 1,018 facet-free rows, every one `internet_archive`) although `drop_year_facet` does cover `corporate_print` (`tools/periodical_harvest.py` **l.1412**). | **YES** — one annual report, in-window (1979), Tier-1, self-reported and retrospective. Per RD-130 the *faceted* CP zero still counts as **UNANSWERED**, so this family is simultaneously "answered by a stray" and "not yet properly asked". |
| (e) | **Auction / museum / manuscript** | **UNTRIED — 0 calls** | no directory, no sidecar, no task in `queries.json`, no residue of any kind under this company dir. INA/CIGNA archival bodies (Hagley, Historical Society of Pennsylvania) are a known manuscript class; nothing here has ever asked them. | NO — a search never run. |

STATUS: WRITTEN

---

## 7. Per-stage tiers (RD-112), with the families that counted

RD-112: *"a tier is issued per stage, measured against that stage's own window — never against the
probe's search range, and never as a property of the company."* §15.2: ≥3 families in-window Tier-1
→ T1; 2 → T2; ≤1 → T3.

| stage | window (PROPOSED) | tier | families that counted | provisional / what could move it |
|---|---|---|---|---|
| **Stage 1** | 1979-01-01 → 1995-12-31 | **T2 CORE — PROVISIONAL** | **(c)** 3 in-window Tier-1 court records (1989, 1991, 1994-95) + **(d)** 1 in-window Tier-1 annual report (1979) | (a) answered only as a perimeter; (b), (e) UNTRIED (0 calls); (c)'s CA/HT sub-routes UNANSWERED and **65 of 79 candidate rows unmined**; (d)'s own tasks have never run facet-free. T1 needs a third family to answer for 1979-95, and only (b) and (e) are unwritten. |
| **Stage 1, strict-registrant reading** | the registrant's own legal life, whose start date **the corpus does not print** (first EDGAR appearance 2018-05-16) | **T3 REGISTER** | **0** — no held document in any family names CIK 0001739940 before 2018 | wholly provisional pending FR-2 (certificate of incorporation / first 10-K) |
| **Stage 2** | 1996-01-01 → 2018-05-15 | **T3 — PROVISIONAL** | **0** — earliest held document is 2018-05-16 | the predecessor-CIK EDGAR run (FR-1) is the route that most plausibly fills these 22 years; then facet-free CP |
| **Stage 3** | 2018-05-16 → present | **T2 — PROVISIONAL** | **(a)** 9 accessions / 30 documents / 5 §3-lineages, including the registrant's own 8-K describing its own birth | **(b)** being UNTRIED is the single fact holding this at T2: for a 2018→ window a CDX/Wayback pass over cigna.com plus the DEF 14A/10-K print would likely make three families |

**Why Stage 1 is T2 with a warning label, not T1 and not a clean T2.**
Two families return in-window Tier-1 text — that is the T2 condition, met. But the Tier-1 text is
*about ancestors*: `INA Corporation` / `Insurance Company of North America` (the 1792 narrative),
`Connecticut General Life Insurance Company`, `Connecticut General Corporation`, `CIGNA Holdings,
Inc.`, `CIGNA Corporation`. **Not one held document names CIK 0001739940 inside 1979-1995**,
because that legal person was created for the 2018 Express Scripts merger. So the tier buys
*depth on the lineage* and buys **nothing** toward "when was this registrant founded". A Stage-1
writer must run two registers side by side — the ancestor chronology (1792 printed; 1872 never
asked) and the registrant chronology (no date printed; 2018-05-16 measured floor) — and never let
the first answer the second. This is RD-112's unresolved boundary case (MASTER_RESEARCH_LOG
l.2371, Costco: in-window *text* but **no in-window document**), arrived at in a sharper form:
in-window documents, **none in-window about the registrant**.

STATUS: WRITTEN

---

## 8. Carriers for the origin / predecessor question (file + line)

Paths relative to `founders_playbook/01_companies/company_014_cigna/sources/`.

| # | carrier | file | line | prints | legal person it attaches to |
|---|---|---|---|---|---|
| C1 | earliest year-bearing incorporation recital in the corpus | `sec/0001140361-18-024107_s002268x1_s4.htm` | **4995**, 23191 | "Cigna was incorporated in Delaware in **1981**." | Cigna Corporation — **not** CIK 1739940 |
| C2 | the registrant's own identity | `sec/0001140361-18-024107_s002268x1_s4.htm` | **52** | "HALFMOON PARENT, INC. … Delaware … 6324 … 82-4991898" | CIK 1739940 |
| C3 | the registrant's own birth event | `sec/0001140361-18-045493_form8k.htm` | **163-172** | Closing 2018-12-20; "Cigna Corporation (now known as **Cigna Holding Company**)"; "Halfmoon Parent, Inc. (now known as **Cigna Corporation**) … ('New Cigna')"; Merger Sub 1 merged into Cigna, "with Cigna surviving … as a direct wholly owned subsidiary of New Cigna" | CIK 1739940 **is the shell**; the 1981 corporation became its **subsidiary** |
| C4 | former-name line on the same cover | `sec/0001140361-18-045493_form8k.htm` | **35**, 77 | "Cigna Corporation (Exact name of registrant…)" / "Halfmoon Parent, Inc. (Former name…)" | CIK 1739940 |
| C5 | both ancestors named inside the registrant's own document family | `sec/0000950159-18-000404_ex4-1.htm` | **2584** | ""Designated Subsidiary" means each of **Connecticut General Life Insurance Company** and **Life Insurance Company of North America**, so long as it remains a Subsidiary, or any Subsidiary which is a successor of a Designated Subsidiary" | ancestors as **2018 subsidiaries**; **no dates** |
| C6 | same clause, post-Acquisition form | `sec/0000950159-18-000404_ex4-2.htm` | **72** | adds Cigna / Express Scripts / Express Scripts, Inc. / Medco to the same list | as C5 |
| C7 | **the ancestor's own dated origin narrative** | `periodicals/INAC2115_1979_djvu.txt` | **4-7**, **371-372**, 16-17 | "Its history dates back to **1792**, with the formation of its principal subsidiary and the nation's first stock insurance company, **Insurance Company of North America**"; "founded in 1792 as America's first stock insurance company"; headquarters "in **Philadelphia**" | INA Corporation / Insurance Company of North America — **ancestor 1** |
| C8 | **two-ancestor structure, third-party judicial** | `periodicals/micro_IA40385013_0186_djvu.txt` | **6110-6116**, 6067 | parent of CGLIC and LINA is Connecticut General Corporation → CIGNA Holdings, Inc. → CIGNA Corporation | ancestors 1 and 2 **as structured in 1991**; **no formation dates** |
| C9 | in-window naming of CIGNA Corporation by a court | `periodicals/micro_IA40386012_1635_djvu.txt` | **25-27**, **2486-2487** | "Supreme Court of the United States, October Term, 1994 … CIGNA INDIVIDUAL FINANCIAL SERVICES COMPANY, **CIGNA CORPORATION**…"; "merged to form CIGNA Financial Advisors, Inc., a wholly-owned subsidiary of **Connecticut General Corporation**, whose ultimate corporate parent is CIGNA Corporation" | predecessor; receipt stamp "APR 19 1995" |
| C10 | ancestor named as a party, 1989 | `periodicals/micro_IA40385019_1642_djvu.txt` | 15, 190, 203, 498 | "CONNECTICUT GENERAL LIFE INSURANCE COMPANY" | ancestor 2 as a litigant |
| C11 | measured registrant perimeter (a state, not a document) | `_index/submissions.csv` + `_index/_INDEX.md` | header row; "UNANSWERED slices (none)" | 1,018 filings, floor **2018-05-16**, 29 forms, guard ok, registrant "Cigna Group" CIK 1739940 | CIK 1739940 |
| C12 | the fleet's own measurement of both passes | `00_universe/_FLEET_INTAKE.tsv` l.18; `00_universe/_FLEET_INTAKE_lane1.log` l.7 | — | `rc0/inwindow0/UNANS0 0 rc1/inwindow27/UNANS1 30 2018-05-16 DONE`; `cigna p1=0 p2=30 floor=2018-05-16` | CIK 1739940 |

STATUS: WRITTEN

---

## Untried (probe §9) — never a null, and never this probe's to close

Per §15.1 an agent brief may not include retrieval a script can reach; each is named with the
command that closes it.

1. **(a) The predecessor registrant.** CIK 1739940 has no pre-2018 existence, so the 1979-1995
   filings of *CIGNA Corporation* have never been indexed anywhere in this repository. No task, no
   directory, no sidecar. **UNTRIED, 0 calls.** Not attempted here because `sec_intake.py index`
   writes `sources/_index/submissions.csv` and `_INDEX.md` keyed by `--company-dir`, so a second
   CIK would overwrite the held 1,018-row index — a protected-archive write of exactly the class
   RD-112 defect 5 was minted over, with fleet lanes live on `sources/` tonight.
2. **(b) Web archives, entire family.** No `sources/web_archive/`, no CDX attempt, no sidecar.
   **UNTRIED, 0 calls** — including for Stage 3, where that is the tier-holding fact.
3. **(e) Auction / museum / manuscript, entire family.** **UNTRIED, 0 calls.**
4. **(c) 65 of 79 harvest candidate rows never opened.** `A4` l.5, re-read immediately before this
   quote (file mtime **2026-10-06 17:23:11 +0530**, 5,611 B): "79 candidate rows in the harvest
   index; 12 items mined; 65 left untried at the --limit." Among the unopened:
   `micro_IA40385607_0258` *Rozelle v. Connecticut General Life Insurance*, 411 U.S. 921 (1973);
   `micro_IA40385004_2284` *Fitzgerald v. CG*, 434 U.S. 859 (1977); `micro_IA40385003_0165`
   *Blanchette v. CG* (1974); `micro_IA41153501_0455` *Perspectives of a State Legislature* (1978);
   the pre-1948 Connecticut statutory items. **UNTRIED for the second ancestor family
   specifically**: `Continental Life`, `Immigration Life`, `State Fidelity`, `Farmers and
   Merchants` appear in **no** cigna task (§4), so nothing about the "1850s-1872 life-insurance
   body" has been asked of any corpus.
5. **(c) The trade-press thread that exists but barely answered.** queries.json **l.645-647** asks
   `Best's Review` / `Business Insurance` / `Mortality` — the natural carrier for a 1979-1995
   insurance chronology — and the index holds 1 `NULL` row for it. Corpus fact or facet artefact is
   **UNANSWERED** until the facet-free re-run lands.
6. **(d) A proper `corporate_print` question.** Both CP tasks are year-faceted (RD-130) and 0
   facet-free CP rows exist for any company. Also untried: a CP creator task for
   **`ina corporation`** — the existing creator task (queries.json l.657-659) uses only `cigna` and
   `"connecticut general"`, which is precisely why the INA 1979 report reached us through the
   *periodical* query instead of this family.
7. **(d) House organs and directories.** Nothing was asked for an employee magazine, a
   Hartford/Philadelphia city-directory entry or an insurance-yearbook page — the classes that
   carried J&J's 1890s chronology (RD-130).
8. **Registers, ids and caches I did not touch, by design.** No `sources.csv` / `timeline.csv` /
   `conflicts.csv` / `data_gaps.csv` row written (§13 — the merge mints those), no `source_id` block
   claimed, and **this company has no `research/_EVIDENCE_CACHE.md` at all** (§14.3): recorded as an
   open gap for the next agent rather than fixed by me, since I own one path.

STATUS: WRITTEN

---

## 10. FETCH REQUESTs

Per §15.1 / hard rule 1: **0 web calls by me**; these are for the orchestrator to run.

```
FETCH REQUEST: FR-1  family (a) — the predecessor registrant; the single highest-value route
  want: EDGAR filings of the 1979-1995 CIGNA Corporation (its own CIK, not 1739940), above all
        any 1993-1996 10-K / S-4 / proxy reciting the 1982 combination of Connecticut General
        and INA, and the 1981 reincorporation.
  command: python tools/sec_intake.py index "CIGNA Corporation" \
             --company-dir founders_playbook/01_companies/company_014_cigna
           python tools/sec_intake.py auto "CIGNA Corporation" --company-dir <same> \
             --from 1993-01-01 --to 1996-12-31 --max-docs 40
  WRITE-CARE: index artefacts are keyed by --company-dir; the run MUST land CIK-scoped files
        (submissions_CIK<prev>.csv, _INDEX_CIK<prev>.md) and MUST NOT clobber the held
        CIK0001739940 index. Read the guard line before accepting the write.
  status if not run: UNTRIED. If run: a 1990s recital of a 1982 event is FACT-classed but
        tagged RETROSPECTIVE SOURCE (§6), never contemporaneous.

FETCH REQUEST: FR-2  family (a) — the registrant's own certificate of incorporation
  accession 0001140361-18-045479 (8-K12B, 2018-12-20) — in the index, NOT held; its exhibit 3-2;
  and the first 10-K, accession 0001047469-19-000792 (2019-02-28, a2237767z10-k.htm) — in the
  index, NOT held. These are the only instruments that can print this registrant's own
  "incorporated in Delaware in ___" sentence. Nothing held gives it.
  command: python tools/sec_intake.py auto "Cigna Group" --company-dir <dir> \
             --from 2018-12-20 --to 2019-03-01 --max-docs 40

FETCH REQUEST: FR-3  family (a) — the 18 filings never listed
  _UNANSWERED.csv: "18 in-window filings were never listed because --max-docs 30 was reached".
  Re-run at --max-docs 60, or enumerate 2019-2020 separately (the 2019-02-28 10-K and the
  2019-03-15 DEF 14A are both indexed and both unheld).

FETCH REQUEST: FR-4  families (c)/(d) — mine the backlog, then ask CP without the facet
  command: python tools/harvest_mine.py --company cigna --limit 40 --max-mb 25
           python tools/periodical_harvest.py --company cigna --facet-free
  priority: the four pre-1975 Connecticut General SCOTUS microfiche layers; INA annual-report
  companion years 1940-1981 (one self-report becomes a series); every corporate_print creator
  hit for "ina corporation".
  DO NOT launch while the fleet lanes hold the harvest root — this probe watched the mine
  rewrite A4 and drop six files into sources/periodicals/ mid-pass at 17:22-17:23.

FETCH REQUEST: FR-5  family (c) — Chronicling America is a dead route, not a null
  evidence: 00_universe/harvest/_CA_ENDPOINT_TEST.md — 7 of 7 URL shapes CHALLENGED (403,
  Cloudflare bot challenge), "ANSWERED shapes: none … no CA zero may be cited as a null"; the
  4 cigna CA rows are 404/UNANSWERED (nightlies 2026-09-26/-27/-28/-29, 85,273-85,274 B of HTML).
  remedy: python tools/ca_endpoint_probe.py from the GitHub Actions egress, then re-run both
  cigna CA tasks. Hartford/Courant-class coverage of the 1982 combination is exactly what this
  family would carry.

FETCH REQUEST: FR-6  family (b) — first-ever CDX call for this company
  scripted Wayback/CDX pass over cigna.com, 1996-2010, into
  founders_playbook/01_companies/company_014_cigna/sources/web_archive/ with sidecars.
  This is the route that moves Stage 3 from T2 to T1.

FETCH REQUEST: FR-7  ancestor 2 by name — the query block does not exist
  add to tools/queries.json under company `cigna`, across IA / CP / CA / HT / GB:
  "Continental Life Insurance Company", "Immigration Life Association",
  "State Fidelity and Investment Company", "Farmers and Merchants Bank", plus an 1850s-1872
  founding frame. Until then the second ancestor family is UNTRIED and its zeros are mine to
  report, not to read.
```

STATUS: WRITTEN

---

## 11. What I refused to claim, and why

1. **I refused to attach 1792 to this registrant — and to attach it to any registrant at all.**
   The corpus prints 1792 twice (`INAC2115_1979` l.5, l.371) and the sentence's subject is
   *Insurance Company of North America*, "its principal subsidiary", of INA Corporation. Available
   claim class: **FACT (Tier-1 corporate self-report, in-window 1979) about an ancestor**,
   confidence capped at **Medium** because it is a **retrospective memory 187 years late** in the
   company's own promotional voice and no second lineage in the corpus repeats it (§3 independence,
   §6 time audit). Refused: "Cigna was founded in 1792."
2. **I refused to attach 1981 to CIK 1739940.** "Cigna was incorporated in Delaware in 1981" (C1)
   is in the held bytes, but it is about **Cigna Corporation**, which C3 proves became a
   *subsidiary of* the registrant, and the registrant carried the shell's EIN 82-4991898 forward.
   Attaching 1981 here is the Citigroup-1812 / Boeing-"since 1916" move the brief named as my trap
   (hard rule 5).
3. **I refused to treat the 1982 combination as evidence.** `1982` occurs **0** times in the 4
   representative SEC docs; on the non-SEC shelf it is 3 debt-table lines, 1 sovereign loan, 1
   Missouri reporter cite and 1 budget sentence — and **0 lines anywhere pair `1982` with
   merg/comb/union/formed** (measured, §4). The combination year stays a **hypothesis inherited from
   the dispatch brief**, reachable only by FR-1.
4. **I refused to attach 1872 or any 1850s date to the second ancestor.** `1872` = 0 occurrences in
   every held byte, and that ancestor's plausible names appear in no query that has ever run
   (§4, FR-7). Reported as **UNTRIED for that family**, per instruction, never as "no evidence
   exists". The lone `1850` in the corpus is an ERIC sentence about New Haven immigration.
5. **I refused to count two shelves as two families.** md5 shows `micro_IA40386012` and the 1980
   CIA memo byte-identical across `corporate_print/` and `periodicals/` (hard rule 4). Equally
   refused: counting the S-4 + four S-4/A + their exhibits as five corroborations of the 1981
   recital — **one** lineage (§3), therefore **one** recital.
6. **I refused to cite an index column as evidence.** The 45 IA + 4 GB `TIER1_CANDIDATE` labels and
   the mine's two `TIER1_CANDIDATE_TEXT` promotions were opened in the bytes first; one of the two
   turned out to be a **sponsor acknowledgment list** (RD-124, exactly).
7. **I refused to report the EDGAR in-window silence as "CIGNA filed nothing 1979-1995."** The walk
   has **0 UNANSWERED slices** and a measured floor of 2018-05-16: the silence is about *this
   registrant's age and this CIK's identity*, and is stated as a perimeter (§2, §6a).
8. **I refused to write registers, global ids, or an evidence cache** — one path is mine (§13,
   §14.4), and no byte under `sources/` was created, moved, renamed or deleted by this pass.
9. **I refused to let a stale measurement stand.** Numbers taken before 17:23 are marked as the
   17:20 state in §2 and superseded by §4's census, rather than quietly rewritten.

STATUS: WRITTEN

---

## 12. The route most likely to change this verdict, and the handoff

**One sentence:** *indexing the predecessor registrant — the CIGNA Corporation CIK that is not
1739940 (FR-1) — is the route most likely to change this verdict*, because it is the only route
that can put a **filing** inside the Stage-1 window at all, which would take family (a) from
perimeter-only to a third counting family and Stage 1 from **T2 to T1 exemplar** while
simultaneously supplying the 1982-combination recital that no held byte prints; the runner-up is
the facet-free `corporate_print` re-run (FR-4), the family RD-130 says has flipped tiers before —
Kroger at 104 layers, Boeing at 46 — and which for this company has never once been asked without
its year facet, nor with `INA Corporation` as a creator.

**Handoff.** Registers untouched. Two shelf findings for merge: (i) an **annual report is stored in
`periodicals/`, not `corporate_print/`** — family counting must follow document class, not shelf;
(ii) **`sources/corporate_print/` holds no corporate print at all** (one 1980 CIA staff memo plus a
md5-duplicate of a court record), so any future "print bytes" figure for this company must come
from the deduplicated list in §2, not from directory sizes. This dossier deliberately contains no
`source_id` block; the merge mints them.

STATUS: WRITTEN

---

## 13. Gate record

Command run as briefed (0 web calls, 1 file written by me):

```
python tools/gates.py --company-dir founders_playbook/01_companies/company_014_cigna \
  --checks csv,keys --fail-on substantive \
  --out founders_playbook/03_quality_control/cigna_s1_probe_gates.md
```

Result: **Findings 2 | Passes 0**, both findings `coverage` class, **0 substantive** →
`--fail-on substantive` is satisfied (the gate's own footer: "coverage-only findings (a gate had
no input yet): 2 of 2 — expected for a freshly probed company, and NOT failing the exit code
unless --fail-on all"). The two: `coverage / registers` — "no register CSVs at root or research/ —
csv/anchors gates DID NOT RUN"; `coverage / narrative` — "no stage_*.md volumes found — keys/anchors
gates DID NOT RUN". Both are true of a Stage-1 probe by construction (§15.2: the probe writes no
registers and no volumes), and the gate itself says so. `coverage 0 registers, 0 stage volumes,
**43 source documents**` — the 43 is 30 SEC + 13 shelf `.txt`, and after md5 the real count is
30 SEC files / 9 accessions / 5 §3-lineages + 11 distinct non-SEC documents (§2, §4).

**The tier the machine read, and why it is not the tier I issued.** The gate printed
`tier: T3 … from A_chronology_feasibility.md — T1,T2,T3 also stated in this company's files (16
mentions); the most recent write wins`. That is a tool tie-break, not a re-grade: the same command
run five minutes earlier printed **14** mentions, so the count is of T1/T2/T3 tokens inside the
first 30,000 characters and moves as the dossier grows — the stable part of this observation is the
tie-break, not the number. The mechanism: `tools/gates.py` **l.583-602** reads only the **first
30,000 characters** of each research dossier and, when all hits share one file (identical
verdict-flag, mtime and stem), `hits.sort(reverse=True)` falls through to the **tier string
itself**, so the lexicographically greatest label — `T3` — wins any file that mentions both `T2`
and `T3`. My §7 issues **Stage 1 = T2 core, PROVISIONAL** on the
lineage frame and **T3 register** on the strict-registrant frame; both labels are inside 30,000
characters, so the detector can only ever print T3 for this dossier. Reported as an observation for
§15.5 ("every gate proves itself") — **not** fixed by me, because `tools/gates.py` is not a path this
brief owns and gaming the detector by deleting the T3 mention would delete the finding. **If the
fleet takes one number from this file, take `T2 core — PROVISIONAL`, and read §7's second row before
spending against it.**

STATUS: WRITTEN
