# A_chronology_feasibility.md

# A — Chronology feasibility probe: Bank of America (rank 20)

Owner: `probe-bofa`. Stage-1 PROBE only. No volume, no registers, no certification, no ids minted.
Company dir (absolute): `E:\founder's playbook\founders_playbook\01_companies\company_020_bofa`
All `sources/...` paths below are relative to that directory. Windows are **PROPOSED**, never inherited.

**CONFIDENCE CAP (binding on every line here).** All **16** Internet Archive sidecars
(`sources/corporate_print/*.meta.json` 4 + `sources/periodicals/*.meta.json` 12) carry
**`"transport": "UNVERIFIED TLS -- re-check before citing at High confidence"`** — measured by
`json.load(...)['transport']` over every sidecar; 16 of 16, 0 verified. Nothing in this dossier is stated
above **Medium**. Line numbers are printed here so layer-level statements are checkable, but byte identity
between a held layer and the live archive item is asserted only "as fetched".

**INTAKE STATE (measured, not inherited).** The fleet record `00_universe/_FLEET_INTAKE.tsv` L29 reads:
`bofa | Bank of America | company_020_bofa | rc1/inwindow0/UNANS0 | 0 | rc1/inwindow0/UNANS0 | 0 | (no floor)
| no | no document stored; probes must cite the measured floor, not a null; identity guard refused the
write; resolve the CIK by hand | REFUSED`. `sources/sec/` **does not exist** and `sources/sec/_RUN.json`
**does not exist** (`ls -d sources/sec` → `No such file or directory`). What the intake *did* write is four
artefacts under `sources/_index/quarantine/CIK0000070858/`, mtime 2026-10-06 17:21 local — they arrived
minutes before this probe opened and are read here in full (§1).

**STATUS: WRITTEN** (§0-§8 + `## Untried` + FETCH REQUESTs; gate run recorded in §9).

---

## 0. Counts, each with the command that produced it

| count | value | command |
|---|---|---|
| files in the company dir after this pass | **39** | `find .. -type f \| wc -l` |
| held text layers (files) | **16** `.txt` | `ls sources/*/*.txt \| wc -l` |
| distinct documents among them | **13** | `md5sum */*.txt \| awk '{print $1}' \| sort -u \| wc -l` |
| byte-identical cross-shelf duplicates | **3 pairs** (§2d) | `md5sum corporate_print/*.txt periodicals/*.txt \| sort` |
| `corporate_print` shelf | **4 `.txt` / 1,734,546 B / 258,906 w** (+4 sidecars) | `ls $d/*.txt \| wc -l; cat $d/*.txt \| wc -c; wc -w` |
| `periodicals` shelf | **12 `.txt` / 1,931,967 B / 290,107 w** (+12 sidecars) | same |
| SEC documents stored | **0** — no `sources/sec/` at all | `ls -d sources/sec` |
| SEC index rows (quarantined) | **52,562**, CSV 4,434,230 B, sha1 `d2469bf3…` | `csv.DictReader` over `_index/quarantine/CIK0000070858/submissions_CIK0000070858.csv` |
| index enumeration span | **1994-02-22 → 2026-10-06** | min/max of `filingDate` over those 52,562 rows |
| index rows filed before 1994-01-01 | **0** | same, filtered |
| archive slices the walk read | **21 (`-001`…`-021`) + `recent`** | `Counter(r['source'])` on that CSV |
| harvest candidate rows for this slug | **109** (A4 recorded 103) | `csv.DictReader` over `00_universe/harvest/candidates.csv`, `r['company']=='bofa'` |
| distinct `item_id`s among them | **100** | set over those rows |
| items mined by the A4 pass | **12** (`sources/harvest_mine/_index.json` `mined`) | `json.load(...)` keys `window/candidates/mined/untried_by_limit/items` |
| mined items carrying the entity's own name | **12 of 12** (`named_terms` non-empty, verdict `TIER1_CANDIDATE_TEXT`) | `json.load(...)['items']` per item |
| mined items carrying a **founding** statement | **0 of 13 distinct layers** | vocabulary table §3 |
| layers fetched by this probe | **0** (2 attempted, both refused — §Untried U-3) | `ia_text.py fetch --id … --insecure` |

**CSV headers enumerated before any field was read** (hard rule 3).
`submissions_CIK0000070858.csv` header printed from `rows[0].keys()`:
`filingDate, form, accession, reportDate, primaryDocument, source` — note: **no** `periodOrDate`,
**no** `companyName`, **no** `query_label`.
`00_universe/harvest/candidates.csv` header:
`company, source_family, query, item_id, title, date_or_issue, url, snippet_or_hitcount, http_status,
classification, retrieved_at`.

**Three inherited figures are corrected here, not carried forward:**
1. Brief: "Strong shelf elsewhere: **8 corporate print and 20 periodical bytes**." Measured: the shelves hold
   **4 + 12 `.txt`** files (8 and 24 files *including* sidecars), 1,734,546 B and 1,931,967 B. The shelf is
   real; the counts in the brief are not reproducible and are superseded by §0.
2. Brief/RD-133: "**8 of 8** mined items entity-bearing". Measured in the file on disk: the A4 mine record is
   **12 items, 12 of 12 entity-bearing**. RD-133's 8/8 cannot be reproduced from `harvest_mine/_index.json`;
   the claim that matters — *entity-bearing* — holds at 12/12, and §3 shows why it does not carry the tier.
3. A4 L5: "103 candidate rows … 87 left untried at the `--limit`". Measured now: **109 rows / 100 distinct
   items / 88 distinct items never mined**. Rows grew because RD-134's facet-free reharvest added
   `[FACET-FREE per RD-130]` queries (§4c).

---

## 1. Which registrant does EDGAR answer, and which window does each line belong to?

This is the question this brief was dispatched to settle. Answered from artefacts on disk.

**(i) The literal briefed identity string reaches nothing.** The one re-run this brief authorised —
`python tools/sec_intake.py index "Bank of America Corporation" --company-dir <dir>` — printed, verbatim:

```
identity 'Bank of America Corporation' not resolved: NO-MATCH name 'Bank of America Corporation'
(0 candidates); pass --ticker or --cik -- pass --cik or --ticker explicitly
```

and wrote nothing. Seven name forms then tested against the same resolver (`tools/sec_intake.py
resolve_name`, one ticker-map read), **all** returning `NO-MATCH … (0 candidates)`:
`Bank of America` · `Bank of America Corporation` · `Bank of America Corp` · `Bank of America of California`
· `Bank of America NT&SA` · `NationsBank` · `MBNA`. **The name route is dead for this slug in both
directions**: neither the 1998 registrant's conformed name nor the 1904 bank's name resolves. Only `--cik`
or `--ticker` reaches EDGAR here, and the intake already did that by CIK.

**(ii) What EDGAR answers when addressed by CIK** — `sources/_index/quarantine/CIK0000070858/_registrant_CIK0000070858.json`:

```
cik                0000070858      requested_cik  70858
registrant         BANK OF AMERICA CORP /DE/      ticker  BAC   (17 tickers incl. BML-*/MER-PK)
former_names       ["BANKAMERICA CORP/DE/", "NATIONSBANK CORP"]
guard              quarantine
guard_reasons      no slug token ['bofa'] appears in registrant name 'BANK OF AMERICA CORP /DE/'
                   / tickers [... 'bac' ...] / former names
count              52562      rows_dropped_no_accession 0      rows_without_primaryDocument 605
```

`_INDEX_CIK0000070858.md` L13-96 gives the earliest filing per form: **SC 13G/A 1994-02-22**, PRE 14A
1994-03-15, **10-K 1994-03-30** (0000950168-94-000099), 10-Q 1994-05-13, **S-4 1994-08-18**
(0000950168-94-000291), S-4/A 1994-09-22, 10-K405 1995-03-30, 8-A12B 1996-11-27, **DEFA14A 1998-08-19**,
S-3DPOS 1998-09-28, 10-K/A 1999-03-23 — i.e. the walk **does** enumerate the 1997-98 merger period; its
`## UNANSWERED slices` section reads **(none)**, and §0's slice counter shows 21 archive slices plus
`recent` read, so **RD-134's uncapped walk is confirmed working on this registrant**.

**So EDGAR answers exactly one registrant: `BANK OF AMERICA CORP /DE/`, CIK 70858, whose two recorded
former names are `NATIONSBANK CORP` and `BANKAMERICA CORP/DE/`.** By the rule this brief set (registrant's
own cover page + `formerNames` decide which line is the registrant), the **1998 NationsBank/MBNA
continuation, Delaware-domiciled, is the registrant**; the other lines are **ancestors or brand kin**, and
the founding-decade filings of CIK 70858 do not exist because EDGAR's own floor for this CIK is
**measured at 1994-02-22** (0 rows before 1994-01-01), not assumed.

**(iii) The same three-way split is visible inside the held corporate print** — the registrant's own 2012
annual report (`sources/corporate_print/01-bank-of-america-bac_djvu.txt`, title block L4-5
"Bank of America Corporation / 2012 Annual Report"):

```
L803  | Bank of America Corporation (NYSE: BAC) is headquartered in Charlotte, N.C. As of December 31, 2012, we operated
L1245 | The Corporation is a Delaware corporation, a bank holding company
L15922-15924 | The Corporation operates its banking activities primarily under two charters: Bank of America, National
        Association (Bank of America, N.A. or BANA) and FIA Card Services, National Association (FIA).
L22800 | Bank of America Corporation and its predecessor companies and
L6448 | primarily under two charters: BANA and FIA Card Services, N.A.
```

That is **three different legal persons named in one document, none of them dated to a founding**: the
Delaware holding company (the registrant), `Bank of America, National Association` (its banking charter),
and — in the ERIC-distributed pamphlets — `Bank of America NT & SA, San Francisco, CA` (the California
line's own mid-century name). **No held byte links BANA to NT&SA**, and no held byte links either to the
registrant's `NATIONSBANK CORP` past by a merger instrument. The link is **held by nothing** — the
Citigroup finding, reproduced exactly (Citigroup probe §6 Q2: "the link between these two chains is held
by NOTHING").

**(iv) Three lineages, their asserted dates, and what the corpus holds for each.**

| line | entity as named | asserted window (PROPOSED, source below) | carriers held | earliest held naming |
|---|---|---|---|---|
| **L-1** | "1791/1802 Boston merchants' association" (some accounts' origin) | 1791-01-01 → 1802-12-31 | **0** — `1791` **0**, `1802` **0**, `massachusetts` 4 hits, none a bank (§3) | none |
| **L-2** | `Bank of America NT & SA, San Francisco, CA` (the California line: a 1904 San Francisco bank, Bank of Italy → renamed 1928 per the brief) | 1904 → 1928 → 1959 (NT&SA) — **0** carriers for 1904/1928 | **11** bank-issued pamphlets naming it at 1980-1983 + **1** municipal 1977 report + **1** 2012 AR naming `Bank of America, N.A.` | **1976-03-04** (letter inside the 1977 EIR, L865) |
| **L-3** | `BANK OF AMERICA CORP /DE/` ← `BANKAMERICA CORP/DE/` ← `NATIONSBANK CORP` | 1994-02-22 (EDGAR floor) → 1998-12-31 | **0 stored documents**; index enumerates 52,562 rows incl. 1994 S-4/10-K and 1998 DEFA14A; **1** 2012 corporate-print AR | **2012** (AR L4/L803/L1245) |

**L-1's only source in this repository is a tool constant.** `1791` occurs **0 times** in all 16 held layers
(§3 command). Its presence in this company's records comes from `tools/harvest_mine.py` **L58**:
`"bofa": ("1791-01-01", "1998-12-31")` — whose own header comment (L45-47) says windows are "deliberately
WIDE **where the founding date is itself unestablished in our corpus**". `sources/harvest_mine/_index.json`
records `window: ['1791-01-01','1998-12-31']`, and A4 L3 applied it. That is a **search setting, not
evidence** — the Citigroup 1812 case, verbatim. `00_universe/fortune_top_50_2026.csv` has **no founding-date
column** (header printed in §0 of the Citigroup probe; same file here).

**STATUS: WRITTEN**

---

## 2. What the mine actually holds — every item opened and read at line level

13 distinct documents, four genres. **None is a founding document.** Command for the vocabulary columns is
§3's; line numbers are from the held `.txt`.

### 2a. `01-bank-of-america-bac` — 1,332,198 B (1,327,549 B as text), **the registrant's own annual report, dated 2012**

Duplicated byte-for-byte across both shelves (§2d). Sidecar URL names the file
`Bank%20of%20America%20%28BAC%29%20Annual%20Report%202012_djvu.txt`; bytes L4-5 print
"Bank of America Corporation / 2012 Annual Report". **`harvest_mine/_index.json` records this item at
`date`/`meta_date` 1998-01-01 and `in_window: True`; the bytes print 2012.** RD-121's "the date field in the
index is not the date it claims to be", demonstrated on this company: A4 L26's "in-window" for this row is a
metadata artefact, and the document in fact **post-dates every proposed stage window** by 14 years.
Registrant-identity content: L4-5, L803 (Charlotte N.C.), L1245 (Delaware corporation, bank holding company),
L15922-15924 (two bank charters: BANA + FIA), L22800 ("and its predecessor companies").
`NationsBank` (4) and `MBNA` (6) are **not** merger history: L22743-22745 and L22759-22762 are capital-trust
line items in a long-term-debt schedule ("NationsBank Capital Trust II 289 76 365"), L22823-22833 and
L22837-22862 the same, and L29040-29049 is a **director biography block** — "Jack O. Bovender, Jr. / Former
Chairman and Chief Executive Officer / HCA, Inc." and "Frank P. Bramble, Sr. / Former Executive Officer /
**MBNA Corporation**". A former employer of a board member is not a predecessor naming (§14 r5).

### 2b. `micro_IA41153448_01xx` — 11 distinct items, 15,380-33,346 B each, **the bank's own consumer-education series**

`The CIRcular: Consumer Information Report`, reprinted by ERIC. Read at the top of each layer:
`INSTITUTION Bank of America NT & SA, San Francisco, CA.` with its own printed `PUB DATE` — e.g.
`micro_IA41153448_0107` L5/L8/L10 ("How to Balance Your Checkbook", **May 82**), `_0114` L5/L8/L10
("What's in Your Credit Report?", **Jan 83**), `_0109` L8 / PUB DATE **Jan 83** (ED 241 821), and `_0105`
whose label lines are split across rows (L2 TITLE / L3 INSTITUTION / L4 PUB DATE, values on following lines)
— an OCR-shape warning for anyone citing it later. Copyright lines corroborate the decade from inside the
bytes: `_0117` L305 "COPYRIGHT © BANK OF AMERICA NTASA 1981", `_0116` L280 "…NT&SA 1981", `_0115` L311
"© BANK OF AMERICA NT&SA 1979, 1961, 1983" (OCR noise: `1961` is **not** usable as a date), `_0108` L299
"…1976, 1979, 1980. 1982, 1963 ya" (likewise **not** citable).
**This is family (d): company-issued print, naming the L-2 entity by its own legal abbreviation, at
1980-1983.** All 11 sit in one ERIC microfilm run (`IA41153448`) and are one publisher's series, so §3's
independence rule caps corroboration across them: 11 documents, **one lineage witness**.
`micro_IA41153448_0109` is on disk (mtime 2026-09-26 15:26) but appears **neither** in A4's 12-row table
**nor** in `harvest_mine/_index.json`'s 12 items — an unaccounted layer, cited here for the first time
(§14 r11). Two siblings of the same run are still unmined and unheld: `_0110` (1982, "A Guide to Checks and
Checking") and `_0113` (1983, "Personal Record Keeping") — candidates.csv classifies both `corporate_print` /
`TIER1_CANDIDATE` / HTTP 200. **Fetchable, never fetched.**

### 2c. `bankofamericadat2619sanf` — 342,480 B, **not corporate print: a City and County of San Francisco document**

L1-14 read: "SAN FRANCISCO / DEPARTMENT OF CITY PLANNING 100 LARKIN STREET … / San Francisco City Planning
Commission / FINAL ENVIRONMENTAL IMPACT REPORT / ^ BANK OF AMERICA DATA PROCESSING CENTER / Parking
Structure / Twelfth and Kissling Streets / EE 75.414 / **May 26. 1977**". 51 lines name the bank
(`_index.json` `phrase_hits` 50, `named_terms ['bank of america']` — the double-spaced OCR is why the
normalised count differs). It is a **third-party municipal record** naming the bank as project sponsor:
L311 "of parking is considered by the Bank of America to be necessary if the bank is to", L506 "Bank of
America intends to provide for the use of its employees at the bank's data", L1161 "The Bank of America
currently maintains a temporary office", and it embeds correspondence dated **March 4, 1976** (L865
"…San Francisco, California; For the Bank of America.: March 4, 1976"; L1364 "…Bank of America." Letter to
Robert Towle, project architect). **Earliest dated naming of any lineage entity anywhere in this company's
bytes: 1976-03-04.** Genre: government print reached through the IA texts index — not (d) (not
company-issued), not a newspaper (so its (c) attribution is provisional; §4c).
The harvest index and the brief both class it `corporate_print`; **the bytes refuse that label** — recorded,
not resolved (Citigroup §1a made the identical finding).

### 2d. Duplicate check before any corroboration was counted (hard rule 4)

`md5sum corporate_print/*.txt periodicals/*.txt | sort` — **3** byte-identical cross-shelf pairs:

| md5 | pair | bytes |
|---|---|---|
| `bbd6e03c…` | `01-bank-of-america-bac` cp + per | 1,332,198 |
| `1a764ac5…` | `bankofamericadat2619sanf` cp + per | 342,480 |
| `c119d95a…` | `micro_IA41153448_0116` cp + per | 32,428 |

16 files → **13 distinct documents**. The brief's "8 corporate print and 20 periodical" shelf figure cannot
be reconciled with 4+12 `.txt`; §0's measurement governs. Two shelves holding the same bytes is **one**
carrier route, never two families (RD-124 rule 4).

**STATUS: WRITTEN**

---

## 3. Vocabularies, adjacency required (trap 2) — every quantifier below is a run command

Command, applied to each of the 16 `.txt` layers: `re.sub(r'[^a-z0-9]+',' ',text.lower())` for phrase work
(plus `\s+`→` ` normalisation, RD-124 defect 2) then `len(re.findall(re.escape(v), norm))`; line numbers via
`grep -n -i`. Totals are over **16 files / 13 distinct docs** (cross-shelf duplicates counted once unless noted).

| vocabulary | hits | where / what it names |
|---|---|---|
| `bank of america` | **1,077** | all 13 distinct docs; the naming wall is *not* a naming void |
| `the bank of america` | 59 | 21 in the 1977 EIR (both shelves), 8 in the 2012 AR |
| `bank of america corporation` | 124 (62 per shelf of one doc) | 2012 AR only — **L-3, the registrant, at 2012** |
| `nt & sa` | **15** | the 11 ERIC pamphlets — adjacency-verified `Bank of America NT & SA` = **L-2 at 1980-83** |
| `national trust and savings` | **0** | the expanded charter name appears **nowhere** in held bytes |
| `bank of america national trust` | **0** | ditto (the 1937 OCC row, unheld, is the only place it surfaces — §3b) |
| `bank of america of california` | **0** | no naming of the 1928 rename |
| `bank of italy` / `of italy` | **0** | **no carrier for the founding name at all** |
| `giannini` / `amadeo` | **0 / 0** | no founder name in any held byte |
| `1904` | **0** | no founding-date carrier |
| `1791` / `1802` | **0 / 0** | L-1 has no carrier of any kind (§1iv) |
| `security pacific` | **0** | the California line's later merger named nowhere |
| `founded` / `founder` | **0 / 2** | the 2 "founders" are 2012 AR L507: "**As founders of the BOKA Restaurant**" — a *customer* anecdote. False hit, refuted by opening it |
| `organized` | 5 | AR L16162 "organized exchanges"; EIR L1064 "vertically organized plants"; ERIC L128 "more organized" — all common nouns |
| `charter` | 11 | AR L6448 / L15922 "under two charters: BANA and FIA Card Services, N.A." — present-day **banking licences**, not a founding charter |
| `delaware` / `delaware corporation` | 4 / 1 | AR only; L1245 registrant domicile = **L-3, at 2012** |
| `nationsbank` / `mbna` | 4 / 6 | debt-schedule capital trusts + a director's former employer (§2a). **Not** lineage evidence |
| `massachusetts` | 4 | AR L696 "Massachusetts, and allow" (narrative fragment); L8738 "Massachusetts 4,381 4,919 …" — a **state row in a table**. Nothing to do with an 1802 Massachusetts association |
| `trust company` | 2 | AR L29210 "**Computershare Trust Company, N.A.** via the Internet" — a **transfer agent**, the exact adjacency trap this brief warned of, live in the same file |
| `america national` | **0** | so every "National/Trust" reading here comes from adjacency (`NT & SA`, `Bank of America, National Association`), not from a glued false name |

**Verdict on the naming:** the corpus is naming-**rich** and origin-**empty**. 13/13 distinct documents name
an entity spelled Bank of America; **0/13 name a founding act.**

### 3b. Adjacency traps found in the *index*, not the bytes (RD-124 rule 6, measured on candidates.csv)

Rows quoted from `00_universe/harvest/candidates.csv` (columns per §0), all `TIER1_CANDIDATE`, all unheld:

- `Rk5RAQAAMAAJ`, `c489AQAAMAAJ`, `Ni_jAAAAMAAJ` — Google Books, `date_or_issue` **1910**, three copies of
  "Annual Report / Annual Report of the Public Service Commission, Second District" (**New York State**),
  matched page **PA238**, snippet `… stock association , organized July 1 , 1854 . Managers : The managers
  are … Bank of America , N. Y`. A **New York** institution named "Bank of America" in a **New York**
  regulator's volume, six years after the San Francisco founding, beside an 1854 stock association. Either a
  fourth lineage or a same-name different legal person; §14 r5 forbids reading it as the registrant's
  origin, and it must **not** be read as corroborating L-1 either.
- `WjxOAAAAYAAJ` — Google Books **1897**, "United States Investor and Promoter of American Enterprises",
  PA1036, snippet `… the worst defaulters are not con- fined to the Western Hemisphere , and the … Bank of
  America … Phenix National .` — a **pre-1904** use of the brand in a defaulters passage. Opened, this row
  could *undercut* a founding story rather than support one.
- `fMUnAQAAMAAJ` — Google Books **1937**, "Annual Report of the Comptroller of the Currency … Congress of the
  United States", page **PA71**, snippet `… Bank of America National Trust and Savings Association , San
  Francisco . DISTRICT OF COLUMBIA Volunta…` — **the full expanded legal name of the L-2 entity, printed by
  a federal bank regulator in 1937.** Highest-value unheld row for this slug, and the only surfaced place
  where `national trust and savings` (0 in held bytes) appears at all. Third-party, contemporaneous,
  not self-narrative.
- `NPCM19311005` — IA, **China Mail**, 1931-10-05, collection `newspapers`: a genuine periodical naming, unheld.
- `bwb_S0-EKQ-844` — IA, **1954**, title "Biography Of A Bank The Story Of Bank Of America" (layer
  1,370,889 B, `text_layers: 1`). `gentlegiant00yeat` — IA, **1954**, "The gentle giant" (150,919 B, 1). Both
  carry the collections `printdisabled`/`inlibrary`. §Untried U-3 records what happened when I tried them.

**On trap 3 (a founder credited by one publisher and not another).** Both 1954 titles are unopened, so no
founder name can be reported from them; and `giannini`/`amadeo` are **0** in every held byte. When a founder
name does arrive from two publishers of the same decade and agrees in one and not the other, that is a
**lineage-count question** — how many separate lines are being claimed — not a corroboration event
(§3 independence rule). This probe records **zero founder claims**, and will not accept one that survives
only in print it could not open.

**STATUS: WRITTEN**

---

## 4. Five-family verdict (a)-(e). Every family was tried or is named UNTRIED; no family is reported as a null.

| family | state | what was measured |
|---|---|---|
| **(a) SEC / EDGAR** | **TRIED–ANSWERED at index level; TRIED–UNANSWERED at document level** | 52,562 rows enumerated, perimeter **1994-02-22 → 2026-10-06**, **0 rows before 1994-01-01**, 21 slices + `recent`, `## UNANSWERED slices: (none)` — RD-134's uncapped walk confirmed on this registrant. **0 documents stored**: `sources/sec/` absent, `_RUN.json` absent; the guard quarantined the write (§4a). Remedy named; not forced (hard rule 1/9). |
| **(b) Web archives** | **UNTRIED** | No tool in `tools/` reaches a CDX/capture index for this slug; probe ran **0 WebSearch / 0 WebFetch**. Floor ~1996-12-29, so it bears only on L-3's 1997-98 window. `sources/web_archive/` does not exist; here that is genuinely untried, and per RD-134 NR-1 the absence of a directory is not itself a verdict — the command gap is what makes it UNTRIED. |
| **(c) Periodical corpora** | **TRIED–ANSWERED (thin) + TRIED–UNANSWERED (2 sub-routes) + UNTRIED (2 sub-routes)** | Answered: IA texts surfaced the 1977 SF EIR (held) and **0 newspapers held**. **Chronicling America — TRIED–UNANSWERED:** 4 candidate rows, 2 `SKIPPED: hard stop: 5 consecutive failures (host halted)`, 2 `ERROR … saved:chronicling_america/…`; I opened the saved files — **85,274 B and 85,273 B of `<!DOCTYPE html> … <title>Page Not Found -- 404 -- Library of Congress</title>`, 0 `<entry>` elements** (`re.findall('<entry>')` → 0). A 404 page is not an empty result set: RD-129's "wrong path, not a refusal", confirmed for this slug. **HathiTrust — TRIED–UNANSWERED:** 1 row, host halted. **Google Books text — UNTRIED:** 21 rows incl. the 1937/1910/1897 rows above; no script here reaches GB full text. **IA periodical sub-route — UNTRIED for 64 rows** (§5 limit shortfall). `periodical_harvest.py` **not run** (brief forbids it; it races live merges on `candidates.csv`). |
| **(d) Digitised corporate print** | **TRIED–ANSWERED — the family that sets this tier** | **12 company-issued items held**: 11 `The CIRcular` pamphlets naming `Bank of America NT & SA, San Francisco, CA` at 1980-1983 + the 2012 Annual Report naming `Bank of America Corporation … a Delaware corporation`. **0 held items dated before 1976.** `_index.json` labels all 12 mined items `family: corporate_print` while 10 of the 12 bytes live under `sources/periodicals/` — family must be taken from the retrieval route and the genre, not the directory a file landed in (Citigroup §1a). |
| **(e) Auction / museum / manuscript** | **UNTRIED** | No tool reaches a sale-room or accession catalogue for this slug; 0 web calls. §14 r6 makes this a tier input in its own right (Apple, Walmart, Berkshire moved on it). |

**Tried to some degree: 3 (a, c, d). UNTRIED: 2 (b, e).**
**Families returning in-window Tier-1 *origin* text: 0** — no proposed origin window has a carrier at all (§1iv).

### 4a. Why the filings family is answerable and still empty: the guard, measured

`tools/sec_intake.py` `registrant_guard` (L285) requires signal A: "a slug token must occur as a **whole
word** in the registrant name, a former name, or a ticker", with RD-135's fix adding "compare the
**de-spaced** forms too" (L318). For this company both paths fail:

- whole-word tokens of `BANK OF AMERICA CORP /DE/` + `{BANKAMERICA CORP/DE/, NATIONSBANK CORP}` + 17 tickers
  → none equals `bofa`;
- de-spaced forms → `bankofamericacorpde`, `bankamericacorpde`, `nationsbankcorp`, `bac` … none equals `bofa`.

**RD-135's fix does not fix this slug, and it is a new sub-class.** Home Depot failed because a multi-word
name compresses into one word (`homedepot`); bofa fails because the slug is an **abbreviation of a phrase
whose letters are not in the registrant name** (`bofa` ← *B*ank *Of* *A*merica). The whole-word rule is right
for the Dell shell it was written for and blind to abbreviations — the same shape as RD-133's finding that
`harvest_mine.py` "could not see that `gm` is General Motors", which was fixed there by an explicit `ALIAS`
map (`Bank of America`→`bofa`). **`harvest_mine.py` has the alias; `sec_intake.py` does not.** That single
asymmetry is why the mine has 13 documents and the filings shelf has 0. Remedy (orchestrator action, a tool
change, not agent work): give `registrant_guard` the same slug→registrant alias vocabulary, then
`python tools/sec_intake.py auto --cik 0000070858 --company-dir <dir> --from 1994-01-01 --to 1998-12-31 --max-docs 30`.
**STATUS: WRITTEN**

---

## 5. Per-stage tiers, measured against each stage's own window (RD-112)

Windows are **PROPOSED** and labelled as such. `fortune_top_50_2026.csv` has no founding-date column; the
1791-1998 range in the mine is a tool constant (`harvest_mine.py` L58) — §1iv. "In-window" below means **a
document whose own printed date sits in that window and which names a lineage entity at Tier-1 strength**; a
2012 self-report about a Delaware corporation is not a 1998 document.

Because the record supports **three lines wearing one name** and not one continuous company, I stage them
separately, exactly as the Citigroup probe did — otherwise Stage 1 gets written from a 1980s tax pamphlet.

| stage / line | PROPOSED window, and why | families returning in-window Tier-1 text | tier | deliverable per §15.2 |
|---|---|---|---|---|
| **Stage 1 — registrant line (L-3)** | **1994-02-22 → 1998-12-31.** Lower bound = EDGAR's *measured* floor for CIK 70858 (0 rows before 1994-01-01); upper = the fleet's 1998 cut. Not a founding date: the registrant's own `formerNames` begin at `NATIONSBANK CORP`, and no held byte states when that entity was formed. | **0** — (a) index rows only, and *a search-index row is not a fact* (§3); (d) nearest company print is 2012, 14 years late; (c) nearest naming is 1977, wrong line and wrong decade. | **T3** | short narrative + registers; §K, §N, §U mandatory; 8k w/stage, ≈3-4 runs |
| **Stage 1 — California line (L-2, the founding act as conventionally told)** | **1904 → 1928** (founding to rename), per the brief's framing; the corpus itself supplies **no** date for either act, so the window is a hypothesis to be tested, not a fact. | **0** — `1904` 0, `bank of italy` 0, `giannini`/`amadeo` 0, `bank of america of california` 0 in all 13 distinct layers (§3). | **T3 — and origin UNKNOWN-first, not narrative-first** | as above; the honest Stage-1 text is "no carrier for the founding act" |
| **Stage 1 — Boston line (L-1)** | **1791-01-01 → 1802-12-31**, taken only from the harvester's own constant; zero evidentiary basis here. | **0**, plus zero naming of any entity at all. | **T3 / not writable** | a conflict entry + data gap; no chronology row may be minted from it |
| **Stage 2 — L-2 growth (proposed)** | **1929 → 1975** (between the rename hypothesis and the first held naming) | **0** — first dated held naming anywhere is **1976-03-04** (EIR L865), one quarter late for this window | **T3 PROVISIONAL** | 8k w/stage. **Flip condition:** `fMUnAQAAMAAJ` p.PA71 (1937 OCC, names `Bank of America National Trust and Savings Association, San Francisco`, third-party federal) → 1 family; plus any 1930s-50s print → 2 → **T2** |
| **Stage 3 — L-2 into L-3 (proposed)** | **1976 → 1998** (from the first held naming to the fleet cut) | **1 firm** — (d) the 11 Circular pamphlets, 1980-83, company-issued, adjacency-named. **1 provisional** — (c)/(grey): the 1977 municipal EIR, third-party, in-window | **T3 firm / T2 PROVISIONAL** | 8k w/stage firm; if a stage lead attributes the EIR to (c) as government periodical print, this stage has 2 families → **T2**. The probe does **not** resolve it: one carrier route (IA texts) produced both, and §3's independence rule caps the 11 pamphlets at one lineage witness regardless of count. |

**Planning tier = the minimum = T3** for Stage 1 under every framing (≈3-4 runs/stage, 8k words).
Per RD-112, **which window a future re-grade moves**: the `--cik 0000070858` intake moves **Stage 1 (L-3)**
and nothing else; opening `fMUnAQAAMAAJ` moves **Stage 2 (L-2)**; the EIR's family attribution moves
**Stage 3** only. None of them touches L-1, whose emptiness is structural (no carrier of any kind).

**Also measured for the tier rule:** `_index.json` records `candidates 103 / mined 12 / untried_by_limit 87`,
while candidates.csv now holds **109 rows / 100 distinct items** — so **88 distinct items were never opened**,
61 of them labelled `TIER1_CANDIDATE`. A tier set from 12 of 100 items is a tier set from a `--limit`, and this
dossier says so rather than presenting it as a census (§14 r8, and RD-135's "a listing that ends at a `head`
boundary is not a census").

---

## 6. Load-bearing open questions

**Q1 — Is there ANY carrier for a founding act?** **No, measured.** 0/13 distinct layers carry `1904`, `1791`,
`1802`, `bank of italy`, `founded`, a founder name, or a formation/incorporation sentence for any line. The
corpus names the company from **1976** onward and says nothing about how it began. Best available evidence for
the founding act is therefore **not in this repository**, and Q1 is the dossier's central gap.
Routes: U-2 (EDGAR in-window intake), U-3 (the two 1954 books, refused at HTTP 401), U-4 (the 1937 OCC page),
U-5 (Chronicling America 404 path fix).

**Q2 — Which line is the registrant, and what is the documentary link between the lines?**
Registrant = **CIK 70858 `BANK OF AMERICA CORP /DE/`**, whose EDGAR former names are `BANKAMERICA CORP/DE/`
and `NATIONSBANK CORP` — the 1998 NationsBank/MBNA continuation, Delaware. Its own 2012 print agrees
(L1245 "a Delaware corporation, a bank holding company"). **The link from that registrant to `Bank of America
NT & SA` (L-2) is held by NOTHING in this corpus**: `national trust and savings` 0, `security pacific` 0, and
the only `NationsBank`/`MBNA` strings are debt-schedule trusts and a director's former employer. The 2012 AR
does print that the Corporation operates banking "under two charters: **Bank of America, National
Association** (BANA) and FIA Card Services, N.A." (L15922-15924) — a *present-day licence list*, which is the
closest held byte to a bridge between L-2's national-bank identity and L-3's holding company. It is a
one-document, 2012 inference point, **not** a merger instrument, and no 1997-98 filing is stored to test it.
Stitching the 1904 bank into CIK 70858's founding on brand continuity would be an invented claim — the exact
Citigroup §7 refusal #1/#2, reproduced.

**Q3 — What is the "Bank of America, N. Y" that New York's PSC reports at 1910, and the "Bank of America" in
an 1897 defaulters passage?** UNTRIED (Google Books, no script route). They are either a **fourth lineage**
or a same-name different legal person, and they **pre-date or co-date** the San Francisco founding, so
whatever L-1's 1791/1802 claim is, these rows show the *brand name* was in use in the East before or apart
from it. This is trap 2 firing at corpus scale, and it is the question a Stage-1 author must not answer from
the index.

**Q4 — First real experiment / first repeatable validation.** **UNANSWERED, measured.** No held byte describes
a venture, branch, product, format, acquisition or underwriting attempt by any line. The only operational
text about the bank is third-party and architectural — the 1977 EIR describes a **parking structure** for a
data processing centre ("the Bank of America intends to request its…" L1998). The ERIC pamphlets are the
bank's *consumer-education output*, which is a real artefact of the firm at 1980-83 and the closest thing to
a "product" held: 11 titles, one series, distributed through the Federal ERIC system (`ED 241 8xx`,
`CE 800 121-133`). Treat as evidence of a **distribution channel** (a bank reaching households via a
government index), not of an origin. Route: U-2 (1994-98 10-Ks/S-4s describe the franchise), U-4.

**Q5 — First incurred failure.** **UNANSWERED.** Measured over all 16 layers: `insolven` 0, `receivership` 0,
`bank failure` 0, `failed bank` 0, `reorganis`/`reorganiz` 0, `panic` 0, `1904`-era and Depression-era event
language absent. The 2012 AR's litigation sections are 2012-window material about *later* entities (e.g.
L23367 "the Corporation is liable based on successor liability theories", L23446 MBIA successor-liability
claims) and are **not** Stage-1 failures. Nothing may be imported from general banking history here: the
1930s-40s California-line depositor dispute and the 1980s real-estate losses are the kind of item this
project has repeatedly had to retract for having no carrier (RD-127 class). Route: U-5 (CA newspapers), U-4.

**Q6 — Does anything in the record place the 1998 act on the registrant's own filings?** **Index yes,
documents no.** The enumeration carries 1998 rows — DEFA14A 1998-08-19 (0000898822-98-000824), S-3DPOS
1998-09-28 (0000950168-98-003089) — and 1994-98 S-4/10-K/10-K405 rows, but **0 bytes are stored**, so the
merger documents are UNTRIED at document level. The recital route the brief points at (a founding sentence
living in a 1990s filing) is *reachable* here in a way it is not for Citigroup — the index already proves the
filings exist — and it is the cheapest tier move in this dossier (U-2).

**STATUS: WRITTEN**

---

## 7. What this probe refused to claim

1. **Refused 1904, 1791, 1802 and 1928 as dated facts of this company.** Each is 0 occurrences in all 13
   distinct held layers (§3 table). No window in §5 is presented as established.
2. **Refused to make the 1791 date evidence at all.** Its only repository source is `harvest_mine.py` L58's
   window constant, whose own comment calls such windows a device for unestablished dates.
3. **Refused the three byte-identical cross-shelf pairs as corroboration** (md5 in §2d): 16 files, 13 documents.
4. **Refused `NationsBank` ×4 / `MBNA` ×6 as predecessor namings.** They are capital-trust line items and a
   director's former employer (§2a, with the lines quoted).
5. **Refused `charter` ×11 as founding charters.** L15922-15924 is a 2012 licence list (BANA, FIA).
6. **Refused `founder` ×2, `massachusetts` ×4, `trust company` ×2 as entity history** — "founders of the BOKA
   Restaurant" (a customer), a state row in a table, and Computershare Trust Company (a transfer agent).
   Trap 2 documented rather than asserted.
7. **Refused to date anything from an index column.** `_index.json`'s 1998-01-01 for the 2012 AR is the case
   in point (§2a); `date_or_issue` on GB rows is a publication year I did not open; ERIC `meta_date` years
   are 1980-83 and match the printed `PUB DATE`, which is why I cite the printed one.
8. **Refused to count RD-133's "entity-bearing" as tier-bearing.** 12/12 mined items are entity-bearing
   (measured, `named_terms`) and **0/13** carry a founding statement — RD-133's abbreviation fix did its job
   on the detector, and the detector was never the question.
9. **Refused to force the guard.** No `sources/sec/` write, no `--no-verify`-style bypass, nothing moved,
   renamed or "cleaned" under `sources/` (hard rule 2). The 4 quarantine artefacts are cited as found.
10. **Refused to report Chronicling America or HathiTrust as nulls** — their saved responses are 404 HTML
    pages and host halts (§4c). **UNANSWERED, with remedy.**
11. **Refused to claim the two 1954 books say anything.** My fetch attempts returned
    `UNANSWERED after 3 tries (HTTP 401)` for both layers (U-3). Refusing a service that refused me is the
    correct behaviour, not a gap.
12. **Refused `numFound`-style signals and the 61 unopened `TIER1_CANDIDATE` rows as evidence** — including
    the 1937 OCC snippet, which I quote as *what the index surfaces*, never as a citation to the page.
13. **Refused to state any confidence above Medium** (16/16 sidecars UNVERIFIED TLS).
14. **Refused to run `harvest_mine.py` / `periodical_harvest.py`** (brief), and re-read A4 in full before
    quoting it — every A4 line cited here (L3, L5, L21, L26) was checked against the file, and where the file
    and the bytes disagree, the bytes win (§0 corrections).
15. **Refused to mint source ids, write registers, author volumes, or certify depth.** No file outside this
    dossier and the assigned gate output was written.

## Untried

Every route below is a search never run or a byte never opened — **not** a null.

- **U-1 — The mine itself: 88 of 100 distinct candidate items never opened.** 61 carry
  `TIER1_CANDIDATE`; by family: `internet_archive` 64, `google_books` 20, `corporate_print` 3,
  `chronicling_america` 1; 23 rows have no parseable year at all. Orchestrator run
  (`harvest_mine.py` is mine to not run): `python tools/harvest_mine.py --company bofa --limit 40 --max-mb 25`.
  Highest-value rows inside it, named: `micro_IA41153448_0110` (1982) and `_0113` (1983) — same bank series,
  `corporate_print`-classed, HTTP 200, **directly fetchable by `ia_text.py`**.
- **U-2 — EDGAR documents for CIK 70858, 1994-01-01 → 1998-12-31 (cheapest tier move; the registrant's own
  recital route).** Blocked by the guard sub-class in §4a, not by the archive. Orchestrator action: add the
  slug→registrant alias to `registrant_guard`, then
  `python tools/sec_intake.py auto --cik 0000070858 --company-dir <dir> --from 1994-01-01 --to 1998-12-31 --max-docs 30`,
  and a forward pass `--from 1999-01-01 --to 2006-12-31` for the recital. Expect 1994 S-4
  (0000950168-94-000291) + 10-K (0000950168-94-000099) + 1998 DEFA14A/S-3DPOS. **Do not re-run `index` for a
  second registrant in this directory** — artefacts are CIK-keyed, but the B-2 no-clobber signal is the thing
  that caught the Dell shell (RD-135).
- **U-3 — The two 1954 IA books: TRIED, refused, remedy named.**
  `python tools/ia_text.py list-files --id bwb_S0-EKQ-844 --insecure` → `text_layers: 1`,
  `bwb_S0-EKQ-844_djvu.txt`, **1,370,889 B**. `… --id gentlegiant00yeat` → `gentlegiant00yeat_djvu.txt`,
  150,919 B. Both then: `fetch` → `"status": "UNANSWERED -- no text layer resolved (UNANSWERED after 3 tries
  (HTTP 401))"`, `"bytes": 0`. Collections on both rows read `printdisabled` / `inlibrary` — these are
  **lending-restricted**, so no unauthenticated script can reach them. Remedy: an authenticated Internet
  Archive lending session, or a non-`printdisabled` copy of the same work (HathiTrust/GB record), or accept
  the founding act as UNANSWERED. **This is the single route most likely to change the Stage-1 verdict.**
- **U-4 — Google Books full text, 21 rows, no script route.** Named pages: `fMUnAQAAMAAJ` **PA71** (1937 OCC),
  `Rk5RAQAAMAAJ` / `c489AQAAMAAJ` / `Ni_jAAAAMAAJ` **PA238** (1910 NY PSC), `WjxOAAAAYAAJ` **PA1036** (1897).
  URLs are in candidates.csv verbatim, e.g. `https://books.google.com/books?id=fMUnAQAAMAAJ&pg=PA71`.
  Under RD-130's rule these zeros/ones are un-refined until re-queried facet-free.
- **U-5 — Chronicling America, 4 rows, endpoint broken not empty.** Both saved responses are loc.gov 404 HTML
  (§4c). Remedy: fix the CA request path in the harvester (RD-129's diagnosis) and re-run the two queries
  `CA 'Bank of America' San Francisco 1900-1998` and `CA 'Bank of America' Charlotte NC / 'NationsBank'
  1970-2000` — the second is the only row in the whole index that queries the **Charlotte line** as a route,
  and it has never returned a result set. Note all 4 rows were emitted 2026-09-29 **before** RD-134's
  facet-free reharvest, so they are stale as well as broken.
- **U-6 — HathiTrust, 1 row, host halted.** `HT 'Bank of America' California (unbounded; ERA UNREFINED-WIDE)`.
  Responses exist under `00_universe/harvest/hathitrust/`; re-run facet-free per RD-130 before any zero.
- **U-7 — Web archives (family b).** No tool owns a CDX route here; 0 web calls by policy. Bears on L-3's
  1997-98 window only (floor ~1996-12-29).
- **U-8 — Auction / museum / manuscript (family e).** Never searched for this slug; no tool, no budget.
  §14 r6: this family has flipped tiers before (Apple, Walmart, Berkshire). For a bank founded on a
  storefront in the West, accession/photographic records are a plausible documentary route.
- **U-9 — State and federal charter routes.** The 1904 line began as a **California** institution and the
  1928/1959/1997 changes are **national-bank charter** acts, i.e. Comptroller-of-the-Currency / OCC and
  California Corporations-Commission records, not SEC ones. `tools/` reaches neither. The 1937 OCC row (U-4)
  is the *only* place this route has surfaced for this slug. Named as an intake gap, not attempted.

## FETCH REQUEST:

```
(1) IA  bwb_S0-EKQ-844      file bwb_S0-EKQ-844_djvu.txt   1,370,889 B  "Biography Of A Bank: The Story Of Bank Of America" (1954)
    IA  gentlegiant00yeat    file gentlegiant00yeat_djvu.txt  150,919 B  "The gentle giant" (1954)
    → refused HTTP 401 (printdisabled/inlibrary). Needs an authenticated IA lending session or an
      open copy of the same work. Claim class if obtained: RETROSPECTIVE INTERPRETATION, 1954 print about
      1904-1928 — Tier 2, never a Stage-1 fact without a contemporaneous carrier.
(2) EDGAR CIK 0000070858 (BANK OF AMERICA CORP /DE/) accessions enumerated in
    sources/_index/quarantine/CIK0000070858/submissions_CIK0000070858.csv:
      0000950168-94-000099 (10-K, 1994-03-30) · 0000950168-94-000291 (S-4, 1994-08-18)
      0000950168-95-000247 (10-K405, 1995-03-30) · 0000898822-98-000824 (DEFA14A, 1998-08-19)
      0000950168-98-003089 (S-3DPOS, 1998-09-28)
    → script-reachable the moment `registrant_guard` carries the bofa alias (U-2). Marked UNANSWERED until stored.
(3) Google Books pages: fMUnAQAAMAAJ?pg=PA71 (1937) · WjxOAAAAYAAJ?pg=PA1036 (1897) ·
    Rk5RAQAAMAAJ / c489AQAAMAAJ / Ni_jAAAAMAAJ ?pg=PA238 (1910) → no script route; FETCH REQUEST, UNANSWERED.
(4) IA micro_IA41153448_0110 (1982) and micro_IA41153448_0113 (1983) — same bank series as the 11 held
    pamphlets, HTTP 200, unopened; `python tools/ia_text.py fetch --id micro_IA41153448_0110 --file
    micro_IA41153448_0110_djvu.txt --company-dir <dir> --insecure`.
(5) Chronicling America: re-issue the two bofa queries against the corrected endpoint (U-5), then fetch the
    returned OCR text for 1904-1945 hits.
```

---

## 8. Corrections taken on this pass (mine, caught by re-measuring)

- **My own first grep of `nt & sa` was nearly a false negative**: raw-line matching against double-spaced OCR
  (`bank  of  america`) returns different counts than normalised text — EIR `phrase_hits` 50 in the index vs
  **51** naming lines measured with `\s+` collapse. RD-124 defect 2, live again; conclusion unchanged.
- **`01-bank-of-america-bac` is not an in-window 1998 item.** The mine's `date`/`meta_date`/`title_year`
  fields say 1998-01-01 and `in_window: True`; the bytes say **2012 Annual Report** (L4-5). A4's row is
  superseded on the date, and no stage window in §5 may be justified by it.
- **`micro_IA41153448_0109` is a 13th distinct document that neither A4 nor the mine index records**, though
  it has been on disk since 2026-09-26 and I read its ERIC header (ED 241 821, PUB DATE Jan 83). Cited here;
  §14 r11 satisfied — the only artefacts newer than A4 are the four `_index/quarantine/` files (2026-10-06
  17:21 local = 11:51 UTC, `built` field), and those are the subject of §1/§4a.
- **Candidate rows grew 103 → 109** and untried items are **88**, not A4's 87 — RD-134's facet-free reharvest
  added `[FACET-FREE per RD-130]` rows, so A4's arithmetic was right when written and is stale now.
- **RD-133's "8 of 8" is not reproducible against the current index** (it records 12 mined / 12 entity-bearing);
  the *substance* — every mined item names the entity — holds, and the *inference the brief drew from it*
  ("so the mine, not the filings, is likely to set this tier") is **confirmed**, since (a) stores 0 documents
  and (d) holds 12.
- **The brief's "8 corporate print and 20 periodical" shelf figure does not reproduce** (§0 commands): 4 and 12
  `.txt`; 1,734,546 B and 1,931,967 B; 3 of the cp files are the same bytes as per files.
- **I first read the CA rows as "harvest never reached them"** and then looked for the saved files named in
  the snippets: they exist (88 KB each). Opening them is what turned an assumed UNTRIED into a measured
  TRIED–UNANSWERED (404). RD-135's rule cuts both ways: an absence inferred from a list I did not open is my
  own defect class, and it is how a dead route gets written as an unattempted one (RD-134 NR-1).

## 9. Gate

```
python tools/gates.py --company-dir founders_playbook/01_companies/company_020_bofa \
  --checks csv,keys --fail-on substantive \
  --out founders_playbook/03_quality_control/bofa_s1_probe_gates.md
```
Result, as written to that file: **Findings 2 | Passes 0**, both `coverage` — "no register CSVs at root or
research/ -- csv/anchors gates DID NOT RUN" and "no stage_*.md volumes found -- keys/anchors gates DID NOT
RUN"; it also reports "coverage 0 registers, 0 stage volumes, **16 source documents**". The tool's own footer
says coverage-only findings are **expected for a freshly probed company and NOT failing the exit code unless
`--fail-on all`**. **Exit code 0** (measured `EXIT=0`). No substantive finding; nothing to repair.
The gate was run **twice**, and the difference is the proof that it reads this dossier: run 1 (before §5
existed) printed `tier: exemplar (no tier stated in this company's research/ dossiers -- exemplar assumed)`;
run 2 (this file complete) printed **`tier: T3 (tier T3 from A_chronology_feasibility.md)`**. Planning tier =
**T3**, per RD-112's per-stage rule; the assumed "exemplar" is superseded, not averaged.

**Verdict in one line, and the route that would change it:** Stage 1 is **T3 on all three lineages** — the
registrant is CIK 70858 (the 1998 Delaware continuation) per its own `formerNames`, the 1904 California line is
attested only at 1976-1983, and the Boston line has no carrier at all — and the single route most likely to
change that verdict is **a text-bearing print of the 1904-1945 California line**: either an authenticated
Internet Archive release of `bwb_S0-EKQ-844` / `gentlegiant00yeat` (both refused HTTP 401 here) or the fixed
Chronicling America endpoint, since those are the only routes that could put a *contemporaneous* naming of the
founding entity in a Stage-1 window; the `--cik 0000070858` intake is the cheaper move but it only upgrades
the **registrant-line** window, not the founding act.

**STATUS: WRITTEN — end of file**
