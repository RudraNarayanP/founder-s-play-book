# A_chronology_feasibility.md

# A — Chronology feasibility probe: Verizon (Fortune rank 28)

Owner: `probe-verizon`. Written 2026-10-06 against the corpus already on disk. **STATUS: WRITTEN** for every
numbered section below. No register rows, no source ids, no volume, no other company's file was touched.
`harvest_mine.py` and `periodical_harvest.py` were **not run** (brief); A4 was re-read in full before being
quoted, and two of its numbers are superseded in §8.

**Headline.** The held record supports **three** lines, not one, and the 1877 claim belongs to none of them
as a *carrier*. (1) The **registrant line** is a Delaware corporation that says of itself "incorporated in
1983" and which was, to the last held filing, legally named **Bell Atlantic Corporation**. (2) The **brand
line** has two named births inside the held bytes — "Bell Atlantic" as a uniform brand in **January 1994**
and "Verizon" as a **d/b/a on 2000-06-30** — and the charter name `Verizon Communications Inc` appears
**0 times** in any held byte. (3) The **1877 / Bell System ancestor line** has **no carrier at all** in
local bytes: `1877` = 0 occurrences, `Alexander Graham Bell` = 0 occurrences, measured (§0). Meanwhile the
only corporate print and periodical bytes on disk for this slug are **The Bell Telephone Company of
CANADA** annual reports — a different legal person, named 0 times in the registrant's own filings.
**Planning tier = T3 (register) at every stage**; the tier is capped by *family count*, not by text volume,
and this company is the clearest case in the fleet of that rule (5313874 B / 627,330 words held, one family).

---

## 0. Counts, each with the command that produced it

All run from `founders_playbook/01_companies/company_028_verizon/sources` unless stated.

| # | quantity | value | command / measurement |
|---|---|---|---|
| 1 | SEC filings enumerated for the registrant | 10,240 rows | `python -c` over `sources/_index/submissions_CIK0000732712.csv`; header enumerated first: `filingDate,form,accession,reportDate,primaryDocument,source` |
| 2 | archive slices actually walked | 6 (`recent` + `-001…-005`) | same file, `Counter(r['source'])` → 1005/2001/2001/2015/2000/1218 |
| 3 | filingDate perimeter | **1994-01-21 → 2026-09-29** | `min(d)`, `max(d)` on the same column; rows `< 1994-01-21` = **0** |
| 4 | filings in the inherited window (≤ 2000-12-31) | **189** | same read; forms: 8-K 69, 10-Q 21, 10-K 5, 10-K/A 5, 10-K405 2, S-4 4, S-8 13, 424B3 11, DEF 14A 7, DEFM14A 1, POS AM 1, 425 3, … |
| 5 | documents stored by the in-window `auto` pass | **24** (25 accession slots, 178 attempted, 147 skipped, 7 UNANSWERED) | `sources/sec/_RUN.json`; `identity_ok: true`; bytes 5,313,874; words 627,330 |
| 6 | distinct non-SEC text layers on disk | **6** | `md5sum corporate_print/*.txt periodicals/*.txt` → 10 files, **4 md5-identical pairs** across the two shelves |
| 7 | `verizon` occurrences (case-insensitive), ALL held bytes | **115**, in **5 files**, earliest filingDate **2000-06-30** | `grep -a -r -o -i "verizon" sources --include="*.txt" \| wc -l` |
| 8 | `1877` in any held byte | **0** | `grep -a -r -c "1877" sources --include="*.txt"` → no file listed; re-measured whitespace-normalised over the 24 SEC layers = 0 |
| 9 | `Alexander Graham Bell` | **0** | `grep -a -r -i -c "alexander graham bell\|graham bell"` → no match |
| 10 | `Bell Telephone Company of Canada` in the SEC layers | **0** | whitespace-normalised python count over 24 files |
| 11 | `incorporated in 1983` | **7** occurrences, one per 10-K (1994,1995,1996,1997,1998,1999,2000) | python regex over the 24 layers — **one lineage**, see §3 |
| 12 | `changed its name` / `Verizon Communications Inc` | **0 / 0** | same python pass |
| 13 | harvest candidate rows for this slug | **186 rows / 162 distinct item_ids** | `00_universe/harvest/candidates.csv`, filter `company == verizon`; header enumerated first (`company,source_family,query,item_id,title,date_or_issue,url,snippet_or_hitcount,http_status,retrieved_at,classification` — names taken from line 1, not assumed) |
| 14 | candidates by family | internet_archive 117, corporate_print 47, google_books 17, chronicling_america 4, hathitrust 1 | same read |
| 15 | candidates by status | http 200 ×181, 404 ×2, blank ×3; classification TIER1_CANDIDATE 141, LEAD_ONLY 38, UNANSWERED 4, ERROR 2, NULL 1 | same read |

**A4 re-read and used, not inherited.** `research/A4_harvest_mine.md` applied window
1877-01-01..2000-12-31, mined 6 of 82 candidate rows, left 75 untried at `--limit`, and recorded
**0 `TIER1_CANDIDATE_TEXT`** with all six items NULL under its vocabulary
(`bell atlantic`, `bell system`, `chesapeake potomac`, `new york telephone`). Those six NULLs are correct
and are still NULL here — but they are NULLs **against Bell Canada bytes** (§2), and the index has grown to
186 rows since (supersession in §8).

---

## 1. Windows: the inherited one is a search setting, and it is wrong

`00_universe/fortune_top_50_2026.csv` has no founding-date column (checked against the probe brief §RD-112
note), so the 1877-01-01→2000-12-31 window in `_RUN.json` and A4 is a **harvester parameter**, not a
historical claim. It is 123 years wide, it spans four legal persons and two brands, and it makes every
"in-window" statement unfalsifiable — exactly the RD-112 defect. Proposed replacements, all **PROPOSED**:

| id | line | PROPOSED window | why this width | carriers dated inside it |
|---|---|---|---|---|
| **W-1** | registrant origin | **1983-01-01 → 1984-12-31** | the two dates the registrant itself asserts: incorporation 1983 (own recital) and Divestiture effectiveness 1984-01-01 | **0 held.** Recitals only, all 1994+ |
| **W-2** | independence / scaling as an RHC | **1985-01-01 → 1993-12-31** | charter amendment 1986-05-09 through the NYNEX agreement announcement; ends at EDGAR's floor | **0 held.** Untried print candidates exist (1989/1992/1993) |
| **W-3** | the recorded period | **1994-01-21 → 2000-12-31** | 1994-01-21 is the measured first row of this registrant's EDGAR existence; 2000-12-31 is the inherited ceiling and the brand launch year | **24 documents**, 627,330 words, all in family (a) |
| **W-0** | 1877 → 1983 "descent" | **not a stage** | an inherited origin story with **no carrier** in this tree; it belongs to the AT&T/Bell System registrant (`company_035_att`) and to no held Verizon byte | **0 held**, measured (§0 rows 8, 9) |

**Say it plainly:** W-0 should be authorised **UNKNOWN-first**, not narrative-first, and W-1/W-2 are
pre-perimeter windows for family (a) — a stage whose only possible carriers are print and periodical must
not be staged as though EDGAR were a witness.

---

## 2. What is on disk, and which line each carrier actually names

### 2a. Family (a) — the registrant's own bytes (24 documents, `sources/sec/`)

Everything below was opened and read this pass. Line numbers are locators in the stored `.txt`; §14 r12 —
cite by the quoted string, not the line.

**The registrant's founding act, in its own words.**
`sources/sec/0000950109-94-000587_0000950109-94-000587.txt` (10-K, filed 1994-03-31, FY1993, File No. 1-8606):
- L166-171: *"Bell Atlantic Corporation (the "Company" or "Bell Atlantic") is one of the seven regional
  holding companies ("RHCs") formed in connection with the court-approved divestiture (the "Divestiture"),
  effective January 1, 1984, of those assets of the American Telephone and Telegraph Company ("AT&T") related
  to exchange telecommunications, exchange access functions, printed directories and cellular mobile
  communications."*
- L236-238: *"The Company was incorporated in 1983 under the laws of the State of Delaware and has its
  principal executive offices at 1717 Arch Street, Philadelphia, Pennsylvania 19103."* ← **the single
  Tier-1 origin sentence for W-1, and it is a 1994 recital of a 1983 fact.** The recital route worked here
  exactly as RD-134's Ford paragraph predicts.
- L174-181: the descent mechanism — *"AT&T transferred to the Company, among other assets, its 100% ownership
  interest in seven Bell System operating companies ("BOCs"): New Jersey Bell Telephone Company; The Bell
  Telephone Company of Pennsylvania; The Diamond State Telephone Company; The Chesapeake and Potomac Telephone
  Company; … of Maryland; … of Virginia; … of West Virginia."* **Descent is by share transfer from AT&T, not
  by continuity of incorporation.** No BOC is given a founding date anywhere in the held bytes.
- L182-186: *"In January 1994, to facilitate the creation of a uniform "Bell Atlantic" brand name across the
  territories served by these seven telephone subsidiaries, the names of the Network Services Companies were
  changed to Bell Atlantic - New Jersey, Inc. …"* ← **brand-line event, dated, in the bytes.**
- L2138-2146 and L3068-3073 (exhibit index, twice): *"3a Certificate of Incorporation of Bell Atlantic
  Corporation ("Bell Atlantic"), dated October 7, 1983. (Exhibit 3a to Registration Statement on Form S-1
  No. 2-87842, File No. 1-8606.)"* and *"3b Certificate of Amendment of Certificate of Incorporation of Bell
  Atlantic, dated May 9, 1986 and filed May 16, 1986."* ← **the founding instrument has a name, a date and a
  filing number — and is not on disk.** This is the dossier's most valuable absence: the bytes tell us exactly
  what to ask for (FR-1).

**The commencement-of-operations date, from a proxy.**
`sources/sec/0000893220-94-000106_0000893220-94-000106.txt` (DEF 14A, filed 1994-02-23): *"… other regional
holding companies ("RHCs") which commenced operations on January 1, 1984, following a court-approved
divestiture of certain assets of the Bell System: Ameritech Corporation, BellSouth Corporation, NYNEX
Corporation, Pacific Telesis Group, Southwestern Bell Corporation, and U S West, Inc."* — one of only
**2** occurrences of "the Bell System" in 24 documents (the other is the 2000 press release).

**The co-registrant sibling, in-window.**
`sources/sec/0000950109-97-002420_0000950109-97-002420.txt` (10-K, 1997-03-25): *"NYNEX is another of the RHCs
created at Divestiture, and the BOCs owned by NYNEX serve …"*; *"In 1996, we announced a definitive agreement
to merge with NYNEX Corporation. The merger is expected to close in April 1997."* NYNEX is named 59 times in
this filing. **The NYNEX close date is not printed in any held byte** — do not date it from memory.

**The brand launch and the d/b/a split — the carrier that separates the two lines.**
`sources/sec/0000950134-00-005461/` (8-K filed **2000-06-30**, four documents stored):
- `…_e8-k.txt` L33-35: *"BELL ATLANTIC CORPORATION (D/B/A VERIZON COMMUNICATIONS) (Exact name of registrant as
  specified in its charter)"*; L70-79: on June 30, 2000 Bell Atlantic's merger with GTE completed under the
  1998-07-27 agreement and *"The combined company will be doing business as Verizon Communications."*
- `…_ex3-2.txt` L13-14, L54-55, L74-75, L171-172: the bylaws carry the same dual heading, *"BELL ATLANTIC
  CORPORATION (Doing Business As Verizon Communications)"*.
- `…_ex99-1.txt` L32: *"BECOME VERIZON COMMUNICATIONS"*; L44-48 is the **brand etymology, as a contemporaneous
  company statement**: *"The VZ symbol was selected because it uses the two letters of the Verizon logo that
  graphically portray speed, while also echoing the genesis of the company name: "veritas," connoting certainty
  and reliability, and "horizon," signifying forward-looking and visionary."*
- `…_ex99-2.txt`: *"VERIZON COMMUNICATIONS DECLARES PRO RATA DIVIDEND — The board of directors of Verizon
  Communications (NYSE:VZ) has declared…"*, i.e. the brand acting as a board subject **on the same day the
  charter name is still Bell Atlantic Corporation**.
- A **Bell System** ancestor sentence appears here too, which is why ex99-1 is the only place the brand line
  and the ancestor line touch in the held bytes.

`sources/sec/0001036050-00-001423_0001036050-00-001423.txt` (8-K filed **2000-08-08**, 44 `Verizon` lines):
L24 `COMPANY CONFORMED NAME: BELL ATLANTIC CORP`, CIK 0000732712, `STATE OF INCORPORATION: DE`; L80-82 the
same dual-name registrant block; L59-60 `<FILENAME>0001.txt</FILENAME>` *VERIZON COMMUNICATIONS FORM 8-K* and
L150-151 `<FILENAME>0002.txt` *PRESS RELEASE -- VERIZON COMMUNICATIONS 08/08/2000*. **Both of this accession's
"UNANSWERED" documents are inside the held consolidated file** (see §8, correction C-3).

**EDGAR's own name chain** — `sources/_index/_registrant_CIK0000732712.json`:
`"registrant": "VERIZON COMMUNICATIONS INC"`, `"former_names": ["BELL ATLANTIC CORP"]`, `"ticker": ["VZ"]`.
**No date is attached to the former-name row.** EDGAR records the name, not the corporate effective date; do
not convert one into the other (Citigroup §6 Q2, same defect).

### 2b. What the "corporate print" and "periodical" shelves actually hold

`sources/corporate_print/` (4 layers) and `sources/periodicals/` (6 layers) are **one carrier set, not two
families**: `md5sum` shows `McGillLibrary-630554-27071` = `c41b4c38…`, `-630557-27062` = `e3d4b0ef…`,
`-630559-27056` = `9e68aa3b…`, `-630577-27188` = `abe69df7…` **byte-identical across both shelves** (4 of 4
overlapping files; only `-630576-27185` `ee9d1fe3…` and `-632736-27035` `00c9747a…` are periodical-only).
Rule 4 applied: **no corroboration may be counted across the two shelves for these four items.**

All six are **The Bell Telephone Company of CANADA**:
- `periodicals/McGillLibrary-632736-27035_djvu.txt` (scan 1905) L1 *"The Bell Telephone Company of Canada"*,
  L7 *"The Directors beg to submit their twenty-sixth Annual Report."* — the sequence number is the only
  self-dating the item offers; **it is arithmetic, not evidence, and no 1877/1880 founding sentence is printed.**
- `…-630576-27185` (1965) L8-11: *"Our new trade mark, adopted in 1965, presents a stronger and more
  up-to-date image of the Company and reinforces the Canadian identity of our ownership, management and
  service."* and L989: *"President Marcel Vincent signs approval of the new Company trade mark."* ← a
  **brand-creation event for a different company**, in the same shelf the next agent will mine for Verizon.
- `…-630577-27188` (1966) L1-2: *"The Bell Telephone Company of Canada / 7 Annual Report 1966"*; "At Bell
  Canada switching centres … As part of the Trans-Canada Telephone System …".
- `…-630554-27071` (1917), `…-630557-27062` (1914), `…-630559-27056` (1912): all *"REPORT OF THE DIRECTORS TO
  THE SHAREHOLDERS"*.

Term counts in these six layers, measured: `verizon` **0**; `Bell Atlantic` / `bell system` / `chesapeake
potomac` / `new york telephone` **0** (A4's own table, confirmed by re-grep); `telephone` 1-76 per file;
`1877` **0** anywhere. Conversely `Bell Telephone Company of Canada` occurs **0 times in the 24 SEC layers**.
**The two halves of this company's local corpus do not name each other's entity.** That is the trap in one
line: the bytes that look like "Verizon's early print" are a Canadian company's annual reports, and the bytes
that are the registrant's own never mention them. Same evidence class as Ford's 16 `McGillLibrary-6355xx`
Canadian layers (RD-134) and Citigroup's travelers'-aid volumes — **same shelf, same failure mode, third
occurrence in this repository.**

### 2c. Cross-check on the two `Bell Telephone Company` strings (RD-131 class, run because they look alike)

Whitespace-normalised regex `The Bell Telephone Company of \w+` over all 24 SEC layers: **5 matches, and every
one resolves to `The Bell Telephone Company of Pennsylvania`** (in the 1994, 1995, 1996 and 1997 10-Ks).
It is **not** the 1877 Boston entity and **not** Bell Canada. Anyone later citing "a held byte names The Bell
Telephone Company" must say which of Pennsylvania.

STATUS: WRITTEN

---

## 3. The load-bearing question, answered from held bytes

**Q: is the 1877 Bell company the origin of this registrant, and can the held record carry it?**
**A: No — and the record separates cleanly into three claims of three different strengths.**

1. **The registrant line is evidenced, by the registrant's own repeated sentence.** CIK 0000732712 =
   *incorporated in 1983, Delaware* (`0000950109-94-000587` L236), *one of the seven RHCs formed in connection
   with the Divestiture effective January 1, 1984* (L166-171), *commenced operations 1984-01-01* (DEF 14A
   1994), named **Bell Atlantic Corporation** as late as 2000-08-08 (8-K header L24), renamed on EDGAR's own
   record to VERIZON COMMUNICATIONS INC with **no date**. Confidence **Medium**, not High: the seven recitals
   are **one lineage** (§3 of the method — "repeated copying of one origin story is one source"), so the
   count in §0 row 11 buys a 1994-2000 consistency check, **not** corroboration. Independence would need a
   second origin: the Delaware certificate (FR-1), a contemporaneous 1984 periodical, or a state registry.
2. **The brand line is evidenced by the bytes to the day, and it is younger than the company.** "Bell
   Atlantic" as a uniform brand: **January 1994** (L182-186). "Verizon": first held naming **2000-06-30**, and
   then only as a **d/b/a** — the charter name, the bylaws heading and the 8-K header all still read Bell
   Atlantic Corporation, and `Verizon Communications Inc` is measured at **0** occurrences. So the sentence
   "Verizon was founded in 1877" is **not supported by any held byte in this tree**, and the sentence "Verizon
   Communications Inc. is the same legal person as Bell Atlantic Corporation, incorporated in Delaware in
   1983" is supported **only** up to the rename, whose date is **UNANSWERED** on held bytes (FR-3).
3. **The 1877 ancestor line has no carrier here at all.** Measured zeros (§0 rows 8-9). The strongest
   ancestor text in the corpus is the registrant's own 1984 framing — *assets transferred from AT&T*, and
   *the Bell System* named twice. Descent from 1877 in this repository is reachable **only** through
   narratives that name AT&T or the BOCs as *property*, never as *the registrant's own birth*. That is
   Citigroup's exact structure: two chains, no byte linking them. Here the link is asserted by a
   **share transfer in 1984** (L174-181), which is a real document-backed event — but it makes the BOCs
   *assets acquired*, not *ancestors incorporated*, and it is the AT&T registrant's lineage that carries
   1877 (`company_035_att`, a sibling tree, **not** importable here).

**Classifications (§3 of the method):** item 1 = FACT (primary document, self-narrative, confidence Medium);
item 2 = FACT for the d/b/a and brand dates, **UNKNOWN** for the charter rename date; item 3 = the 1877 claim
is **RETROSPECTIVE INTERPRETATION with no carrier** and must be written **UNKNOWN** in any volume; "Verizon =
successor of Alexander Graham Bell's 1877 company" is a **founder-claim-shaped inheritance**, and citing it
here would be an invented claim.

---

## 4. Five-family verdict (plus (f), the state-charter route)

Three states only: **TRIED–ANSWERED**, **TRIED–UNANSWERED** (tool/network refused; remedy named),
**UNTRIED**. An untried family is never reported as a null (RD-112/RD-130).

| family | state | what it returned, measured | bearing on each window | remedy / next command |
|---|---|---|---|---|
| **(a) SEC / EDGAR** | **TRIED–ANSWERED**, with a hard measured perimeter | 10,240 rows walked through **all 6 archive slices**, perimeter **1994-01-21 → 2026-09-29**; 189 in-window filings; **24 docs stored**, 147 skipped beyond `--max-docs 30`, 7 slots UNANSWERED. Produced: the 1983 incorporation recital, the 1984-01-01 Divestiture framing, the 1994 brand-unification sentence, the 2000-06-30 d/b/a naming, the EDGAR former-name row. **No pre-1994 silence is our doing** — it is EDGAR's floor for this registrant, and the walk reached it. | **W-3 only.** Structurally absent from W-1 and W-2: rows `< 1994-01-21` = **0** in a full 6-slice walk. | `auto` with raised `--max-docs` and a forward window → **FR-2, FR-3** |
| **(b) web archives** | **UNTRIED** | 0 calls; no tool in `tools/` reaches a CDX capture index for this slug. | Bears only on **W-3** (floor ~1996) — and it is the one family that could hold the **2000-11 name-change pages**, i.e. the exact event missing from (a). | Orchestrator: a CDX route; the probe ran **0** web calls by brief |
| **(c) periodical corpora** | **TRIED–UNANSWERED / partially tried; 0 in-window Tier-1 for this registrant** | A4 opened **6** rows, all Bell Canada, all NULL. The index now holds **186 rows / 162 distinct ids** for this slug (internet_archive 117, google_books 17, chronicling_america 4, hathitrust 1), of which **≥75 were never attempted at `--limit`**. Chronicling America: **2 UNANSWERED** (`SKIPPED: hard stop: 5 consecutive failures (host halted)`) + **2 ERROR http 404** (sidecars `00_universe/harvest/chronicling_america/31497f1a48657a78-r20260929T130143Z.json`, `06c42b4fbc08ccb4-r20260929T130143Z.json`) → **network refusal, not an empty result**. HathiTrust: **1 UNANSWERED** row. **In-window unopened candidates exist**: `TelephonyMagazine17Dec84` (1984), `bitsavers_westernEleEngineeringandOperationsintheBellSystem2_49741719` (1984), `bc-1994-09-12`, `bc-1996-03-25`, `bc-1989-05-08`, `bc-1992-10-26`, `bellatlantictcim15unse` (1993, *"The Bell Atlantic/TCI Merger — The New Telecommunications Paradigm?"*). | W-1 and W-2 have **zero** answered carriers, but only because nobody opened these rows. W-3 is where a periodical naming "Bell Atlantic" is most likely to land. | **FR-5**; `harvest_mine.py --company verizon` with a raised `--limit` (probe forbidden to run it) |
| **(d) digitised corporate print** | **TRIED — returns nothing for this registrant, and it is NOT a second family today** | 47 candidate rows, **45 distinct ids**, of which **39 are McGill Bell Canada annual reports 1900-1967**. The 4 files on this shelf are **byte-identical to 4 of the 6 periodicals** (§2b) → **one carrier set**, rule 4, no cross-shelf corroboration. One row names a lineage *component*, not the registrant: `solarenergycheshire1979`, *"Monthly performance report : Bell Telephone of Pennsylvania"* (1979) — never opened. | None of W-1/W-2/W-3 on held bytes. The 1965 Bell Canada "new trade mark" page is a **brand-creation carrier for the wrong legal person**. | open `solarenergycheshire1979` (FR-5); exclude creator *Bell Telephone Company of Canada* from any Verizon re-harvest (§6 Q6) |
| **(e) auction / museum / manuscript** | **UNTRIED** | Never searched for this slug; no tool, 0 web budget. Under §14(6)/RD-112 this family has flipped tiers elsewhere (Apple, Walmart, Berkshire). | Would bear on W-1 only (share certificates, 1984 RHC promotional material). | orchestrator route; **not** attempted here |
| **(f) Delaware charter route** | **TRIED-BY-REFERENCE ONLY / UNTRIED as a route** | The bytes already **name the document and its number**: Certificate of Incorporation dated **1983-10-07**, Exhibit 3a to S-1 No. **2-87842**, File No. **1-8606**; amendment dated **1986-05-09**. No tool in `tools/` reaches a Delaware or SEC-historic-paper retrieval. | **W-1 — this is the only route that can produce a non-self-narrative founding record for this registrant.** | **FR-1** |

**Families that counted toward any tier this pass: one — (a).** (b), (e), (f) untried; (c), (d) tried but
returning **0** namings of this registrant, with (d) additionally collapsed into (c) by md5.

STATUS: WRITTEN

---

## 5. Per-stage tiers, measured against each stage's own window (RD-112)

"In-window" = a document **whose own filed/printed date sits inside that window** carrying a Tier-1 naming of
a lineage entity. A 1994 filing reciting 1983 is **not** a W-1 document; it is the W-3 record of a W-1 claim.

| stage (PROPOSED) | window | families returning in-window Tier-1 text | tier | deliverable, and the flip condition |
|---|---|---|---|---|
| **S1 — origin of the registrant** | 1983-01-01 → 1984-12-31 (W-1) | **0 of 5.** (a) floored at 1994-01-21 (measured); (c)/(d) hold Bell Canada; (b)/(e)/(f) untried. | **T3 — and structurally capped at T2** | short narrative + registers; §K, §N, §U still mandatory; 8k w/stage, ≈3-4 runs. **Flip:** `TelephonyMagazine17Dec84` opened and naming the RHC → (c) = 1 family → still T3. Two families in this window require (c) **and** (d)/(f) to be distinct non-self carriers — realistically **FR-1** (the 1983 certificate) or Bell Atlantic's own 1984/85 annual report. Nothing raises S1 to T1. |
| **S2 — independence and scaling as an RHC** | 1985-01-01 → 1993-12-31 (W-2) | **0 of 5.** Same perimeter logic; the only in-window untried capacity is print/periodical (`bc-1989-05-08`, `bc-1992-10-26`, `bellatlantictcim15unse`). | **T3 (PROVISIONAL — reaches T2 on one fetch)** | 8k w/stage. **Flip:** `bellatlantictcim15unse` (1993, title already names Bell Atlantic) opened as a third-party periodical → (c) counted → 1 family, still T3; needs a second distinct family to move. Honest statement: **S2 is a hole in the intake, not in the record.** |
| **S3 — the recorded period** | 1994-01-21 → 2000-12-31 (W-3) | **1 — family (a) only** (24 docs / 627,330 words; every §2a carrier sits in this window). (c)/(d) contribute **0** namings; (b)/(e)/(f) untried. | **T3 (PROVISIONAL — the cheapest T2 in the fleet)** | 8k w/stage, ≈3-4 runs, but the *content* available here is T2/T1-shaped: brand creation dated to the day, a d/b/a split, a merger completion, a charter-name lag. **Flip condition:** one in-window periodical naming "Bell Atlantic" — `bc-1994-09-12` or `bc-1996-03-25` or the Telephony Magazine 1984 row re-dated — makes (c) a second family and S3 **T2 immediately**. |

**Planning tier = the minimum across stages = T3** (≈3-4 agent runs/stage, 8k words/stage). Per RD-112, any
future re-grade must name the window it moved: **FR-5** moves **S3** (and possibly S2); **FR-1** is the only
route that moves **S1**; an EDGAR slice change moves **nothing** here, because the walk already reached the
archive floor (measured, §0 rows 2-3). **S1's emptiness is structural** (pre-dates EDGAR), and the 1877
claim must be written as **UNKNOWN** at every tier, not as background.

**A tier is not a word count.** Verizon holds more in-window prose than any probed sibling examined here
(627,330 words) and still sits at T3, because §15.2 counts *families*, and the family that would carry the
origin story is not the family that holds the bytes.

---

## 6. Load-bearing open questions

**Q1 — Which document makes the 1877 Bell company an ancestor *of this registrant*, and can any held route
reach it?**
**No document, and no held route.** Measured zeros (§0 rows 8-10). The bytes' own mechanism is *asset/ownership
transfer from AT&T effective 1984-01-01* (1994 10-K L166-181) — that makes the BOCs **property acquired**, not
incorporation continuity, and the 1877 person sits on the **AT&T** side of that transaction, which is
`company_035_att`'s tree. The only route that could produce a founding record for CIK 732712 is
**FR-1 / family (f)**: the Delaware certificate dated **1983-10-07**, already named in the bytes.

**Q2 — When did the charter name become `Verizon Communications Inc`, by what document?**
**UNANSWERED on held bytes.** `Verizon Communications Inc` = **0** occurrences; `changed its name` = **0**;
EDGAR's `former_names: ["BELL ATLANTIC CORP"]` carries **no date**; and the last held filing (2000-08-08) still
reads `COMPANY CONFORMED NAME: BELL ATLANTIC CORP` with `d/b/a Verizon Communications` on the face of the
document. The in-window filings that would settle it are enumerated in the index but **not stored**:
`0000950134-00-010188` (8-K, 2000-11-30), `0000950134-00-009772` (10-Q, 2000-11-14),
`0000912057-00-050722` (S-8, 2000-11-17) — all `SKIPPED beyond --max-docs 30` — plus the FY2000 10-K405
`0000950109-01-000760` (2001-03-23), which is **outside** the inherited window. → **FR-2, FR-3.**

**Q3 — First real experiment / first repeatable validation.** **UNANSWERED as stated, with one live pointer.**
This registrant was not founded by an experiment; it was created by consent decree and incorporated on paper.
The nearest held Tier-1 "the company went and did something to a named business" carrier found this pass is
`sources/sec/0000893220-95-000578_0000893220-95-000578.txt` (S-4, filed 1995-09-06, cover
`COMPANY CONFORMED NAME: BELL ATLANTIC CORP`): *"Howard W. Sams & Company ("Sams") was incorporated in Indiana
in December 1989. Sams was formed to acquire certain publishing assets of Macmillan, Inc."* — a small tuck-in
registration, **not** a founding event, and the registrant's own exhibit list shows the S-4 in this accession is
a 1995 publishing acquisition, **not** the NYNEX merger (the NYNEX S-4s are in the index but unstored).
The best *experiment* candidate for W-2 is the unopened third-party item `bellatlantictcim15unse` (1993,
"The Bell Atlantic/TCI Merger — The New Telecommunications Paradigm?") — it must be **opened**, not
remembered; nothing in held bytes names the TCI attempt.

**Q4 — What happened between 1985 and 1993?** Nothing in this repository can say, because the intake stopped
at EDGAR's floor and the print/periodical shelves were populated with the wrong company. **This is an intake
hole, not a historical silence** — 162 distinct candidate ids for this slug exist, ≥75 never attempted.

**Q5 — Is any named ancestor a registrant in its own right?** The bytes name the seven BOCs, NYNEX Corporation
(as co-subject of the merger, 59 mentions in the 1997 10-K), GTE Corporation (1999 10-K, merger agreement dated
1998-07-27), and the 1994 renamings (`Bell Atlantic - New Jersey, Inc.` etc.). Whether any of these has its own
EDGAR CIK with pre-1994 paper-era depth was **not tested** — `sec_intake resolve` reaches the network and the
web budget is 0. → orchestrator action, and a likely tier-mover for W-2.

**Q6 — A fleet-level defect this slug exposes (reporting up, not fixing here).** The harvest query
`CP verizon + Bell predecessor annual/shareholder print 1900-2005 (wide, un-refined)` returned **39 of its 45
distinct corporate-print ids as Bell Telephone Company of Canada**. Any Bell-adjacent slug with that query
shape inherits the same false ancestor set (Ford 1984's Canadian layers, RD-134; Citigroup's travelers'-aid
volumes). **Recommendation:** a creator exclusion for *Bell Telephone Company of Canada* and a
disambiguation note on *Bell System* in `tools/queries.json` — a tool change, owned by the orchestrator.
**Related decoy:** the candidate id `bstj50-6-1877` (Bell System Technical Journal 50:6) ends in **1877 as a
page number**, and `bstj` ids carry 1923-1947 metadata years; an id-level grep for `1877` across the harvest
index would manufacture a false Tier-1 ancestor hit. RD-131/RD-124 class; recorded so nobody repeats it.

STATUS: WRITTEN

---

## 7. What this probe refused to claim

1. **Refused 1877 as this registrant's founding date**, and refused "Verizon's history dates to the invention
   of the telephone" in any form: `1877` **0**, `Alexander Graham Bell` **0** across all held bytes. Stays
   UNKNOWN, written as a descent claim belonging to the AT&T tree.
2. **Refused the Bell Canada run as Verizon corporate print** — 6 unique layers, `verizon`/`bell atlantic`/
   `bell system`/`new york telephone`/`1877` all **0** in them, and `Bell Telephone Company of Canada` **0**
   in the registrant's SEC bytes. Refused to read their "twenty-sixth Annual Report" (1905) as an arithmetic
   origin, and refused the 1965 *new trade mark* page as a Verizon brand carrier — it is Bell Canada's brand,
   with the company's own Canadian-identity wording.
3. **Refused to count `corporate_print` and `periodicals` as two families.** 4 of 4 overlapping files are
   md5-identical; rule 4.
4. **Refused the 141 `TIER1_CANDIDATE` labels** in `candidates.csv` as evidence (RD-124: the column echoes the
   query, and the six rows that were actually opened came back NULL).
5. **Refused to convert EDGAR's undated `former_names` row into a rename date**, and refused to treat the
   `d/b/a Verizon Communications` heading as a name change. The legal person in every held in-window filing is
   **Bell Atlantic Corporation**.
6. **Refused to date the NYNEX merger close.** Held bytes say only *"expected to close in April 1997"*.
7. **Refused to date `bstj50-6-1877`, `micro_IA40385014_0418` (Verizon Communications Inc. v. FCC, "2001") or
   any row from `date_or_issue`** — metadata/scan years (RD-121); the FCC case is also outside the window.
8. **Refused to import Bell System history from `company_035_att`** or from general history; sibling trees are
   read-only leads and are excluded from every family verdict and tier above.
9. **Refused to call pre-1994 EDGAR, web archives, Chronicling America, HathiTrust, auction/museum, or the
   Delaware charter "absent" or "empty".** All are UNTRIED or UNANSWERED with a named remedy.
10. **Refused to run any retrieval script** (`sec_intake`, `harvest_mine`, `periodical_harvest`, `ia_text`):
    scripts reach the network, the brief's web budget is 0, and the two harvesters were named as forbidden.
    Every blocked route became a `FETCH REQUEST` below. Declining is the correct behaviour.
11. **Refused any confidence above Medium** — every IA sidecar on this slug reads
    `"transport": "UNVERIFIED TLS -- re-check before citing at High confidence"`.
12. **Refused to mint source ids, write registers or volumes, or certify depth.** No file outside this one was
    written; nothing under `sources/`, `_EVIDENCE_CACHE.md` or `00_universe/harvest/` was moved, renamed or
    deleted.

## FETCH REQUEST (for the orchestrator; each blocks a claim above)

```
FETCH REQUEST: FR-1  (highest value; only route to a non-self-narrative founding record; NOT reachable by any
                      tool in tools/)
  object : Bell Atlantic Corporation, Certificate of Incorporation dated 1983-10-07, Exhibit 3a to
           Registration Statement on Form S-1 No. 2-87842, File No. 1-8606 (+ Ex 3b amendment 1986-05-09)
  source : named inside sources/sec/0000950109-94-000587_0000950109-94-000587.txt L2138-2146 / L3068-3073
  action : historic paper-filing / Delaware Division of Corporations retrieval; route does not exist yet
  claim it would settle : W-1 origin, registrant line, independence for the "incorporated in 1983" recital
  status now : UNTRIED (family (f))
```

```
FETCH REQUEST: FR-2  in-window filings skipped beyond --max-docs 30 (147 slots)
  accessions : 0000950134-00-010188 (8-K 2000-11-30), 0000950134-00-009772 (10-Q 2000-11-14),
               0000912057-00-050722 (S-8 2000-11-17), 0000950133-96-001890 (DEFM14A 1996-09-16),
               the 4 in-window S-4s and 3 425s (GTE merger registration/prospectus), 0000893220-98-000616 (424B5)
  command    : python tools/sec_intake.py auto "VERIZON COMMUNICATIONS INC"
               --company-dir founders_playbook/01_companies/company_028_verizon
               --from 1996-01-01 --to 2000-12-31 --max-docs 45
  settles    : Q2 (the charter rename date), the NYNEX close, a second *filing* lineage for the GTE line
```

```
FETCH REQUEST: FR-3  recital route, forward window
  command    : python tools/sec_intake.py auto "VERIZON COMMUNICATIONS INC"
               --company-dir founders_playbook/01_companies/company_028_verizon
               --from 2001-01-01 --to 2003-12-31 --max-docs 20
  key object : accession 0000950109-01-000760 (10-K405, filed 2001-03-23)
  settles    : the legal-name-change sentence and, possibly, the first Verizon-era recital of the Bell System
               descent — i.e. whether the company itself ever put 1877 into a filing, which is the one thing
               that would move W-0 from UNKNOWN-forever to UNKNOWN-in-this-corpus
```

```
FETCH REQUEST: FR-4  the 7 UNANSWERED slots (4 remain genuinely unanswered)
  accessions : 0000950172-00-001477 documents 0001.txt, 0002.txt, 0003.txt, 0004.txt
               — all three path shapes returned HTTP 404 NoSuchKey (padded-cik/nodash, bare-cik/nodash,
                 bare-cik/dashed); remedy is the dashed-dir listing route, and note the run's own line
                 "listing:not-enumerated … 3 in-window filings were never listed because --max-docs 30 was
                 reached" — their documents exist and are unknown, not absent.
  (0001036050-00-001423:0001.txt and :0002.txt are NOT open requests — see correction C-3.)
```

```
FETCH REQUEST: FR-5  unopened in-window periodical/print candidates (families (c) and (d))
  identifiers: TelephonyMagazine17Dec84 (1984) ; bitsavers_westernEleEngineeringandOperationsintheBellSystem2_49741719
               (1984) ; bc-1994-09-12 ; bc-1996-03-25 ; bc-1989-05-08 ; bc-1992-10-26 ;
               bellatlantictcim15unse (1993) ; solarenergycheshire1979 ("Monthly performance report :
               Bell Telephone of Pennsylvania", 1979 — component company, NOT the registrant) ;
               plus 33 unopened McGillLibrary Bell Canada ids (low value, listed for completeness)
  command    : python tools/harvest_mine.py --company verizon --limit 60 --max-mb 40
               (probe forbidden to run it; A4 stopped at 6 of 82 candidates)
  settles    : S3 → T2, and possibly S2; the cheapest tier move in this dossier
```

## Untried

- **U-1 Web archives (family (b)).** 0 calls; no CDX route in `tools/`. Floor ~1996, so it bears on W-3 only —
  and specifically on the 2000-11 rename pages that family (a) did not store.
- **U-2 Auction / museum / manuscript (family (e)).** Never searched; no tool, no web budget. §14(6)/RD-112
  treat this as a tier input in its own right.
- **U-3 Delaware charter route (family (f)).** No tool reaches it; see FR-1. Until a route exists, **W-1 has no
  reachable primary carrier** and the correct verdict is UNTRIED with the gap named, not a null.
- **U-4 Chronicling America.** 2 rows UNANSWERED (`host halted`, 5 consecutive failures) + 2 ERROR http 404 with
  saved sidecars. **Remedy:** re-run the CA task after the halt, then re-read the saved 404 JSONs before
  judging the zero. Its query is the right one: `CA 'Bell Atlantic' / 'New York Telephone' / 'Chesapeake &
  Potomac' 1900-1995 (HYPOTHESIS predecessor-operating-company routes)`.
- **U-5 HathiTrust.** 1 row, UNANSWERED, query `HT 'Bell System' / 'Verizon' telephone operating company
  (unbounded; ERA UNREFINED-WIDE)` — unbounded means the zero, if any, is RD-130-shaped and must not be read
  as an absence.
- **U-6 Google Books text.** 17 rows / 16 distinct ids, 0 opened by this probe. Most surfaced titles are
  securities-regulation treatises and 2002-2016 books (`lPJUDwAAQBAJ` "Verizon Untethered", 2016-05-01 — outside
  every proposed window); `vYlFDAAAQBAJ` "The Corporate Directory of US Public Companies 1994" is a directory
  entry, which under rule 5 cannot be an origin carrier even if opened.
- **U-7 The 75+ untried harvest rows** behind A4's `--limit` (see FR-5) — the whole of family (c)'s remaining
  capacity for this slug.
- **U-8 The 147 SEC slots `SKIPPED beyond --max-docs 30`** (FR-2), including every pre-2000 S-4/425/DEFM14A for
  the two mergers that created this registrant's scale.
- **U-9 `sec_intake facts` / XBRL series** for 1994-2000: not run (network); the financial spine for W-3 is
  therefore untouched by this pass.
- **U-10 The registrant's own `sources/sec/_PLAN.csv` / `_SKIPPED.csv` full read** — enumerated as existing,
  not opened line by line; the `_RUN.json` identity equation was checked instead
  (`24 + 7 + 147 = 178 vs attempted 178 -> OK`).

STATUS: WRITTEN

---

## 8. Corrections taken on this pass (mine and the intake's, caught by re-measuring)

- **C-1 — A4's candidate counts are superseded, not inherited.** A4 reported *82 candidate rows, 6 mined, 75
  left untried*. Re-measured from `00_universe/harvest/candidates.csv` for `company == verizon`: **186 rows,
  162 distinct item_ids, 8 rows with no item_id**. The fleet re-harvest (RD-134) grew the index after A4 ran.
  A4's six NULLs stand; its **scope** did not.
- **C-2 — "24 sec, 8 corporate print, 12 periodicals" are FILE counts including sidecars.** Document-level,
  the local corpus is **24 SEC + 6 non-SEC = 30 unique text layers**, because `corporate_print` holds 4 `.txt`
  and `periodicals` holds 6, and **4 of those 6 are byte-identical across the shelves** (md5 in §2b). Anyone
  planning agent runs off "44 local documents" would be double-counting.
- **C-3 — 2 of the 7 "UNANSWERED" slots are actually held.** `_UNANSWERED.csv` ranks 24 and 25
  (`0001036050-00-001423:0001.txt` / `:0002.txt`, HTTP 404 `NoSuchKey` on all three path shapes) are both
  **present in full inside the stored consolidated accession** rank 26,
  `sources/sec/0001036050-00-001423_0001036050-00-001423.txt` — visible at its `<FILENAME>0001.txt` /
  `<FILENAME>0002.txt` blocks (L59-60, L150-151). By §3 they are **one source**, not two, and not a gap.
  The genuine unanswered slots are the 4 documents of `0000950172-00-001477` plus the one
  `listing:not-enumerated` row.
- **C-4 — Two of my own instruments were wrong before they were right.** (i) I read
  `submissions_CIK0000732712.csv` assuming a `formType` column and got a `KeyError`; the header is
  `filingDate,form,accession,reportDate,primaryDocument,source` — rule 3, paid for again, no data lost.
  (ii) My first pass at `The Bell Telephone Company of X` used single-space patterns and returned **0**; the
  OCR wraps and double-spaces, so the whitespace-normalised re-run returned **5** (§2c). RD-124 defect 2 and
  RD-131 in one error, exactly as the Citigroup probe recorded its own version of it.
- **C-5 — The registrant guard passed and still let a wrong company in.** `_registrant_CIK0000732712.json`
  reports `guard: ok` on slug token `verizon`, and the SEC intake is correctly keyed — but 39 of 45
  corporate-print candidate ids are Bell **Canada**. The guard protects family (a); nothing in the pipeline
  protects families (c)/(d). Recorded as Q6 for the orchestrator.

---

## 9. Gate

Command run as briefed:

```
python tools/gates.py --company-dir founders_playbook/01_companies/company_028_verizon \
  --checks csv,keys --fail-on substantive --out founders_playbook/03_quality_control/verizon_s1_probe_gates.md
```

Result: **Findings 2 | Passes 0**, both `coverage` and both non-substantive —
`no register CSVs at root or research/ — csv/anchors gates DID NOT RUN` and
`no stage_*.md volumes found — keys/anchors gates DID NOT RUN`. The gate's own note: *"coverage-only findings
(a gate had no input yet): 2 of 2 — expected for a freshly probed company, and NOT failing the exit code unless
`--fail-on all`."* It also read this file and reported **`tier: T3`**, and counted **34 source documents** —
which reconciles exactly with the `.txt` inventory (`ls sources/sec/*.txt` = 24, `corporate_print` = 4,
`periodicals` = 6; 24 + 4 + 6 = 34) once sidecars are excluded, and which is **30 unique text layers** after
collapsing the 4 md5 duplicates of §2b (correction C-2).
**No substantive finding. Nothing was repaired, because nothing was flagged; no register or volume was created
to satisfy it, per §13.**

STATUS: WRITTEN

---

### One sentence naming the route most likely to change this verdict

**FR-5** — opening the unopened in-window periodical rows (`TelephonyMagazine17Dec84`, `bc-1994-09-12`,
`bc-1996-03-25`, `bellatlantictcim15unse`) — is the cheapest move and would make family (c) a **second
family** inside the W-3 window, taking the recorded period from **T3 to T2**; only **FR-1** (the certificate of
incorporation dated 1983-10-07, Exhibit 3a to S-1 No. 2-87842, File No. 1-8606) can give the origin stage its
first non-self-narrative carrier, and no held or reachable route at all can give **1877** a carrier in this
tree.




