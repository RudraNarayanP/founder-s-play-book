# CVS Health — Stage-1 chronology-feasibility probe (company_006_cvs, Fortune rank 6)

Dataset: The Founder's Playbook · File: `A_chronology_feasibility.md` · Probe agent: `probe-cvs`
Dispatched: 2026-10-06 (session clock) · Method: `00_METHOD_AND_STYLE.md` §3, §13, §14, §15; `03_quality_control/PROBE_BRIEF_SHARED.md`.
Hindsight firewall: this file states what the **public record on disk** can and cannot support about CVS's origin and
early years. No claim here is improved by knowing CVS became a Fortune-6 registrant; the tiers are set from measured
corpus families only.
Confidence scale: High / Medium / Low / UNKNOWN (§3). Classes: FACT / FOUNDER CLAIM / CONTEMPORARY OBSERVATION /
RETROSPECTIVE INTERPRETATION / INFERENCE / ESTIMATE-DERIVED / UNKNOWN.

**Web calls made by this probe: 0.** All network reaches in this file are through the repo's own scripts, and only the
add-only `sec_intake.py grab` form (see §8). No fetch was performed by hand; no document was refused for lack of nerve.

---

## 0. Intake state: fleet record vs what I measured — STATUS: WRITTEN

The dispatch record I was handed is **stale, and wrong in both directions**. Measured against the files, on
2026-10-06, in this directory only (all commands and outputs in §8):

| Item | Fleet record (handed in) | Measured on disk | Class |
|---|---|---|---|
| SEC docs stored | 7 | **7** `.txt` under `sources/sec/` (+7 sidecars) — FACT | confirmed |
| Window candidate | 1963-01-01 → 1996-12-31 | **a search setting**, not evidence: it is `harvest_mine.py WINDOWS["cvs"] = ("1963-01-01","1996-12-31")`, copied into `sec_intake/_RUN.json` `window` and into `sources/harvest_mine/_index.json` `window` | FACT (that it is a parameter) |
| Filing floor | 1994-02-10 | **confirmed** as this registrant's earliest indexed EDGAR filing (SC 13G/A, accession 0000912057-94-000290) | FACT |
| Corporate print | 8 | **4** `.txt` in `sources/corporate_print/` (2,471,781 B, 2,571,972 B?? see §8.3) — and **none of them is corporate print** (see §4) | record wrong |
| Periodicals | 12 | **6** `.txt` in `sources/periodicals/` (2,503,477 B) | record wrong (2x overcount) |
| Unique periodical/print documents | — | **8**, after md5 de-duplication: two byte-identical cross-shelf duplicates (hard rule 4) | FACT |
| Total files under `sources/` | — | **47** (17 `.txt` + 17 sidecars + 6 index/plan artefacts + `_index/_INDEX*.md` etc.) | FACT |

`sources/sec/_RUN.json` (built `2026-09-29T19:01:11Z`, i.e. **before** tonight's guard/slice fixes landed — my brief
was right to tell me to re-measure): `registrant "CVS HEALTH Corp"`, `cik 0000064803`, `guard ok`, `attempted 47`,
`stored 7`, `unanswered 0`, `skipped 40`, `bytes 1091837`, `words 126745`, `identity_ok true`.
`00_universe/_FLEET_INTAKE.tsv` row `cvs`: `pass1 rc0/inwindow7/UNANS0`, **`pass2_status` empty**, `pass2_docs 0`,
`filing_floor 1994-02-10`, `slices_capped no`, `state DONE`.
Consequence I acted on: the fleet's **recital pass (pass 2, the forward window that RD-134 created) has never run for
this company** — pass 1 stored 7 documents, so `fleet_intake` had no reason to reach forward. For a 1963 origin whose
EDGAR floor is 1994-02-10, that is the whole origin question left open (§7).

## 1. Which legal person does each candidate date name? — STATUS: WRITTEN

This is the load-bearing section for CVS, because the registrant's own EDGAR identity is **not** a pharmacy company
and the brand is **not** a legal person.

**1.1 The registrant is Melville.** Every one of the 7 stored in-window SEC documents carries
`COMPANY CONFORMED NAME: MELVILLE CORP`, `CENTRAL INDEX KEY: 0000064803`, and
`FORMER CONFORMED NAME: MELVILLE SHOE CORP / DATE OF NAME CHANGE: 19760630`. The registrant json
(`sources/_index/_registrant_CIK0000064803.json`) records `former_names`: `CVS CORP`, `CVS/CAREMARK CORP`,
`CVS CAREMARK CORP`, `MELVILLE CORP` — i.e. today's `CVS HEALTH Corp` is **the same legal person as Melville
Corporation, renamed**, and the name-change chain runs *backwards* from the modern brand to a shoe company.
The 10-Ks themselves state the corporate form: *"Melville Corporation, a New York corporation …is one of the largest
diversified specialty retailers in the United States"* (FY1993 10-K, accession 0000950110-94-000133; same sentence
FY1994 and FY1995). So the registrant's state of incorporation is **New York**, and it describes itself in 1993-1996 as
a four-segment retailer: prescription drugs/HBC (the CVS business), apparel (Bob's, Wilson's, Marshalls up to
1995-11-17), footwear (Meldisco, Footaction, Thom McAn), toys and home furnishings (Kay-Bee, Linens 'n Things,
This End Up) — SC 13D, accession 0000950103-96-000813, Item 2 (L369-375 of that file).

**1.2 "CVS" inside the window is a trade name and a set of subsidiaries, not the registrant.**
The filed bytes name at least six distinct CVS-bearing legal persons, none of them CIK 64803 before 1996:

| Name in the bytes | Where it appears | What it is, on the document's own word |
|---|---|---|
| `CVS, Inc.` | FY1994 10-K (0000891092-95-000026), subsidiary list | "CVS, Inc., **a Rhode Island corporation**" — an operating subsidiary of Melville |
| `CVS Center, Inc.` | SC 13D 0000950103-96-000813 L100, L347 | first-tier holding company for Melville's CVS business; address One CVS Drive, Woonsocket RI |
| `CVS H.C., Inc.` | same, L101, L351 | second-tier holding company; address 400 Highway 169 So., Minneapolis MN; IRS no. 06-12870… |
| `Nashua Hollis CVS, Inc.` ("Nashua CVS") | same, L102, L356 | third-tier holding company, Minneapolis MN address |
| `"CVS"` as **trade name** | FY1993 10-K (0000950110-94-000133) | stores operating under `"CVS", "Peoples", "Standard Drug" and "Austin Drug" trade names` |
| `Peoples Drug Stores, Incorporated` | FY1993 and FY1994 10-K subsidiary lists | "**a Maryland corporation**" — a different drugstore chain inside the same segment |

Rule 5 of the brief is directly on point: a predecessor name, or a same-brand different legal person, is not the
registrant's origin. Here **all** of those apply at once, and the modern registrant's corporate form (a New York
corporation trading as Melville) **predates** 1963 rather than postdating it — see §1.3.

**1.3 The three candidate "origins" and who each names.** (Dates below are *candidates for the dossier to
adjudicate*, not findings of this probe unless a carrier is cited.)

- **1963, Jacksonville, a shoe store** — the folk origin. In the 7 stored in-window SEC files the string `1963`
  occurs **0 times**, `Consumer Value` **0 times**, `Jacksonville` **0 times**, `founded` **0 times** (§8.4). So the
  filings on disk do **not** name this event at all, let alone date it. What the filings *do* name is a **retail
  segment**, not a founding. CLASS: UNKNOWN from held bytes; the carrier would have to be a recital in a
  post-1996 filing (§7 FETCH REQUEST R-1) or periodical text.
- **1976-06-30** — `MELVILLE SHOE CORP` → `MELVILLE CORP`, EDGAR's own recorded date of name change. A FACT about the
  registrant's identity, but it is a *parent-company renaming*, not an origin event.
- **November 1995 / 1996** — the corporate reorganisation visible in the window: Marshalls sold to TJX
  (Stock Purchase Agreement dated 1995-10-14, consummated 1995-11-17 — SC 13D L396-400), the three "CVS Holding
  Companies" created as first/second/third-tier holders of the drugstore business, `Form 8-B12B` filed 1996-11-04
  (accession 0000950103-96-001174, per `sources/_index/_INDEX.md`), and the first post-window
  `10-K405`/`S-4` series in 1997. **This is a disclosure boundary and a re-cut of the corporate stack; it is not an
  origin** (trap 3 in my brief). The window's end at 1996-12-31 is where the *search* stopped, and separately where
  EDGAR's CVS-name paper begins — nothing more.

**1.4 What the insurance/health-services legs look like from here.** The health-services and pharmacy-benefit legs
arrive under **other names** and (on the held bytes) *after* the window edge: FY1994 10-K names
`Pharmacare Management Services, Inc., a Delaware corporation` — a pharmacy-management affiliate, the earliest
health-services-adjacent legal person I can point at in the stored corpus. Nothing in the window names a PBM or an
insurance underwriter; the registrant names that will carry them (`CVS Caremark`) are *renamings of CIK 64803* per the
`former_names` list, i.e. the modern registrant absorbed those businesses by changing its own name, not by being
founded. CLASS for the whole paragraph: FACT as to what the bytes say; the *dates* those legs begin are UNKNOWN in-window.

## 2. Proposed stage windows (PROPOSED — RD-112) — STATUS: WRITTEN

`00_universe/fortune_top_50_2026.csv` header, enumerated before use (§8.1):
`rank, company, revenue_usd_millions, revenue_fiscal_year, profit_usd_millions, hq_city, hq_state, fortune_industry,
universe_source_url, verified_by_second_source, confidence, notes`. **There is no founding-date column** — confirmed by
reading the header, not assumed. The CVS row (`rank 6`) supplies only revenue $402,067M for "fiscal year ended
2025-12-31", profit $1,768M, HQ **Woonsocket, Rhode Island**, industry "Health Care: Pharmacy and Other Services".
The RI HQ is a **present-state** fact and is not evidence about 1963 — yet it is already contaminating the query set:
two of the Chronicling America tasks restrict `state=Rhode Island` and one Google Books task searches `"CVS" Woonsocket`
(§6.2, trap 1 and 2 combined).

Windows I propose, each labelled PROPOSED, each measured against its own stage (never against the company's whole
history):

| Stage | PROPOSED window | Why this window | What the corpus on disk actually covers inside it |
|---|---|---|---|
| S1a — origin as folk-claimed | 1963-01-01 → 1968-12-31 | the only origin claim on the table; a shoe-store founding | **nothing**. SEC floor 1994-02-10. Oldest periodical item on disk is 1980. No print, no manuscript |
| S1b — first CVS drugstore / format shift | 1969-01-01 → 1979-12-31 | the claimed move from footwear to pharmacy | **nothing in-window on disk** for naming purposes; DSN 1980 is 1 year past the edge and is a *directory ad*, not a naming of the registrant |
| S1c — chain formation under Melville | 1980-01-01 → 1989-12-31 | periodical family's first continuous coverage; trade-name era `CVS`/`Peoples`/`Standard Drug` | periodicals TRIED–ANSWERED (weakly): DSN 1980, 1984, 1985, 1988, 1990 layers; entity hits only from 1980 (`CVS Stores, Woonsocket, R.I.`) |
| S1d — reorganisation and separation | 1990-01-01 → 1996-12-31 | Melville's drugstore leg grows, apparel leg is sold, registrant's own paper begins | **both** families answering: SEC 1994-02-10→1996-04-08 (7 docs, Melville) + DSN 1990/1992/1993/1994/1995 layers |

Per RD-112's ruling these are **stage** tiers, so the company's tier is the tier of the stage being assembled (§5).
S1a/S1b are the probe's real problem: they are the founding question, and the measured corpus is silent there for
three of five families and unattempted for two.

## 3. Five-family verdict table — STATUS: WRITTEN

Every family gets an explicit verdict; three states only (TRIED–ANSWERED / TRIED–UNANSWERED with the remedy named /
UNTRIED). An untried family is never reported as a null.

| Family | Verdict | Evidence for the verdict (measured) | In-window Tier-1 text? |
|---|---|---|---|
| (a) SEC / EDGAR filings | **TRIED–ANSWERED** (as to the registrant's identity) / **TRIED–UNANSWERED** (as to the 1963 origin) | 2,968 filings indexed in `sources/_index/submissions_CIK0000064803.csv`; floor 1994-02-10; 7 docs stored, 1,091,837 B, all `MELVILLE CORP`; `founded`/`1963`/`Consumer Value`/`Jacksonville` = **0 occurrences** in those bytes; recital pass never run (`pass2_status` empty) | **YES for S1d** (Tier-1, the registrant's own filings, 1994-03-31 / 1995-03-29 / 1996-03-29 10-Ks + DEF 14A + 8-K + SC 13G/A + SC 13D). **NO for S1a/S1b** |
| (b) Web archives | **UNTRIED** — 0 calls | No `sources/web_archive/` directory exists in this company; no CDX sidecar; no `http_status` artefact under any web-archive path (the NR-1 defect class of RD-133 is *avoided* here precisely because I am reporting UNTRIED with no bytes, not claiming an answer) | NO — and no tool in the verified list reaches it; remedy is named in §6.1 |
| (c) Periodical corpora | **TRIED–ANSWERED, in part; TRIED–UNANSWERED for Chronicling America; 29 of 36 candidates UNTRIED by limit** | `sources/harvest_mine/_index.json`: `window [1963-01-01, 1996-12-31]`, `candidates 36`, `mined 6`, `untried_by_limit 29`. Mined verdicts: 4 × `TIER1_CANDIDATE_TEXT` (DSN 1980/1990/1995 + …), 1 × `VARIANT_TERM_HIT` (DSN 1985), 2 × `NULL` (American Pharmacy 1983 and 1991 **annual index volumes**). CA: 2 `UNANSWERED` ("hard stop: 5 consecutive failures (host halted)") + 2 `classification ERROR` with `http_status 404`. HathiTrust: 1 `UNANSWERED` | **YES but shallow**: entity-bearing trade-press text 1980-1995 (S1c/S1d). **Nothing for S1a/S1b** — the oldest DSN layer in the candidate set is 1980 |
| (d) Digitised corporate print (annual reports, house organs, directories) | **TRIED–UNANSWERED** (facet) — and **the shelf is empty of real print** | `sources/corporate_print/` holds 4 `.txt`, all of them **Internet Archive serial/periodical items** (`micro_IA40706915_0203`, `…_928_0007`, `…_934_0338` = *Drug Store News*; `sim_…japha_1983_23_index` = an index volume) whose own sidecars read `route= download/<id>/<id>_djvu.txt (OCR text layer)` and family `internet_archive` in the mine index. `00_universe/harvest/candidates.csv` cvs corporate_print rows: 2 × `NULL` with `numFound=0` on **year-faceted** params (`year_range [1960,1998]`) and 2 × `UNANSWERED` | **NO** — zero corporate-print bytes on disk. RD-130's exact class: a faceted zero is a statement about our parameter, not about the archive |
| (e) Auction / museum / manuscript | **UNTRIED** — 0 calls | No `sources/auction/`, `sources/manuscript/`, no museum or sale-catalogue artefact anywhere under this company dir; no query block exists for it (the cvs block in `tools/queries.json` has families chronicling_america / internet_archive / hathitrust / google_books / corporate_print only) | NO; remedy named in §6.1 |

**Counting the families that counted (§15.2, per stage, never globally):**
- **S1a (1963 origin) and S1b (1969-1979): 0 of 5 families return in-window Tier-1 text.** ≤1 ⇒ T3. And this is
  *not* provisional in only one direction: family (d) went unanswered because of a year facet, and family (c) has 29
  untried candidates, so the 0 is a measured 0 **over the corpus that exists** — the route to a non-zero is real (§7).
- **S1c (1980-1989): 1 family** (c, periodicals) with entity-bearing in-window text.
- **S1d (1990-1996): 2 families** (a and c). Google Books' 8 `TIER1_CANDIDATE` rows are **not counted** — every item
  they name is 1997-2020 reference almanacs and out-of-window by the CSV's own dates, and the label is an index column,
  not evidence (hard rule 6; §8.6).

## 4. Shelving finding: the "corporate print" shelf is periodicals — STATUS: WRITTEN

Hard rule 4 (byte-identical duplicates are ONE document) and §3's lineage rule both bite here, and they reduce the
apparent corpus:

- `micro_IA40706934_0338_djvu.txt` md5 `4aa6d311f6c393b58b747b8c07d6215f` in **both** `sources/corporate_print/` and
  `sources/periodicals/` → one document (Drug Store News 1990, 1,716,443 B).
- `sim_journal-of-the-american-pharmacists-association-japha_1983_23_index_djvu.txt` md5
  `aed4a59ae87d7b53b66a04a2a3aef808` in **both** shelves → one document (67,074 B).
- 10 files → **8 unique documents**, 2 of which are *annual index volumes* (American Pharmacy 1983, 1991), which name
  nothing (`NULL`, hits 0) and cannot: an index has no article text.
- The 4 files on the `corporate_print` shelf are the same 4 the harvester relocated on 2026-09-26 —
  `00_universe/harvest/_RELOCATED_MINE_BYTES.tsv` lists them with slug `cvs` and destination
  `00_universe\harvest\mine_bytes\cvs\…`, but **that directory no longer exists** (`find` under
  `00_universe/harvest` returns 0 cvs-named paths; `mine_bytes/` is empty) and `harvest_mine/_index.json` records them
  under `family: "internet_archive"`. So they are RD-124's misplaced cache, later shelved into the company as "print".
  **They are family (c) carriers. Family (d) has zero bytes.** I report this as a shelving/lineage defect for the
  merge, and I did not move or rename anything to fix it (hard rule 2).

Sidecar transport warning carried forward: every one of the 10 sidecars says
`transport = "UNVERIFIED TLS -- re-check before citing at High confidence"`. Any periodical citation this probe or a
later pass lifts from these files is capped at **Medium** unless re-verified.

## 5. Tier per stage — STATUS: WRITTEN (final; recital adds of §9 applied in place)

Measured per stage against **that stage's own window** (RD-112), counting a family only where it returns in-window
Tier-1 text, and counting a recital only where the recital is the registrant's own Tier-1 paper naming the stage's event
(§15.2; Ford's precedent in RD-134):

| Stage | Families that counted | Tier | Provisional? |
|---|---|---|---|
| S1a origin 1963-1968 | **1 of 5** — (a) by recital only (1997 S-4 L762, `Founded in 1963`); (c) contributes the **name** `Consumer Value Stores` but no S1a-dated text | **T3 register** | Provisional on family (d) facet-free (R-3) and on the 55 untried periodical candidates (R-5); **no longer provisional on family (a)** |
| S1b 1969-1979 | **1 of 5** — (a) recital, same sentence, no 1969-79 content; (c) has the 1980 layer only 1 year past the edge, so S1b itself is empty | **T3 register** | YES; and S1b may be a **wrong window** — nothing held distinguishes "1963 shoe store" from "1979 CVS goes drugs", because neither is in the bytes |
| S1c 1980-1989 | **1 of 5** — (c) entity-bearing third-party text (`CVS Stores` 1980; `Melville` 21-39 hits/layer 1984-1988); (a) is silent (EDGAR floor 1994-02-10) | **T3 register** | YES — 55 untried candidates sit mostly inside this window |
| S1d 1990-1996 | **2 of 5** — (a) 10 SEC docs incl. the 1996-11-04 succession filing **and** (c) DSN 1990/1993/1994/1995 with `Consumer Value Stores` named | **T2 core** | Not provisional as to the count |
| **Whole Stage 1 as dispatched (1963-1996)** | **2 of 5** — (a) + (c) | **T2 core** | YES, one notch up to T1 only if (d) answers facet-free or a new family answers S1a |

What that means for a volume author: the §A–§U narrative can be evidence-bound from **1990** onward, and from
**1994-02-10** on the registrant's own paper; for 1963-1979 the deliverable is a **register** — §K (money), §N
(decisions) and §U (conflicts) carrying **UNKNOWN with the named routes R-1…R-5**, plus one dated fact the corpus does
give: the registrant's own form, **Delaware, organized 1996-08-22**. Do not write a shoe store. Per §15.2 every tier
still emits `sources.csv`, `conflicts.csv`, `data_gaps.csv` and an UNTRIED list. A T1 exemplar is not supportable from
anything on disk for this company at Stage 1.


## 6. Untried, refused and never-asked routes — STATUS: WRITTEN

### 6.1 `## Untried` (a search never run, not a null)
1. **Family (b) web archives: UNTRIED, 0 calls.** No CDX/wayback attempt exists in this company dir. CVS's 1963-1996
   material predates the mid-1990s web by design; the family could still answer S1d (Melville/CVS corporate pages,
   1996-era) and nothing earlier.
2. **Family (e) auction / museum / manuscript: UNTRIED, 0 calls, and no query block exists for it** in
   `tools/queries.json`'s cvs tasks. Apple was re-tiered to exemplar-capable on exactly this family (§14 r6); CVS has
   never been asked.
3. **Periodical candidates untried at the `--limit` cut — R-5.** At my first read (17:26) the mine index said
   `candidates 36 / mined 6 / untried_by_limit 29`; at close (17:36) it says **`candidates 68 / mined 12 / untried 55`**
   (§9.6) because the fleet lane is live. Either way this is a **limit cut, not a null**, and it is the cheapest in-
   corpus route: the untried set is the Drug Store News / American Pharmacy / Pharmacy Times annual layers
   **1981-1995** (enumerated from `00_universe/harvest/candidates.csv`, `item_id` column, §8.1) — note that **no
   candidate at all is dated before 1980 except three out-of-window pharmacy textbooks (1951, 1955, 1974, 1977) that
   the harvester itself shelved as `LEAD_ONLY`**, so the press route as currently queried cannot reach 1963-1979.
4. **HathiTrust: TRIED–UNANSWERED (1 row, classification `UNANSWERED`), and Google Books: metadata only.** The 12
   Google Books rows are `snippet_or_hitcount`/dates only — no text layer fetched — and are out-of-window (1997-2020).
5. **Chronicling America: TRIED–UNANSWERED, remedy named** — the 2026-09-26 rows say `SKIPPED: hard stop: 5
   consecutive failures (host halted)`; the 2026-09-29 rows say `http_status 404` with a saved response file
   (`chronicling_america/5752ac55d242188a-r20260929T130143Z.json`). Per RD-129/RD-135 the 404 is a wrong path, not a
   refusal. Remedy: fleet CA lane re-run with the corrected endpoint; I did not touch it.
6. **The recital route for this company: UNTRIED.** `pass2_status` is empty in `_FLEET_INTAKE.tsv` and I did not run
   `auto` (see §7 for why, and for what I ran instead).
7. **Family (d) facet-free: UNTRIED by me, deliberately.** `periodical_harvest.py` is owned by a fleet lane tonight
   (my brief), and `_REMINE_RUN.log` (0 B) plus `candidates.csv`/`_MANIFEST.md` mtimes of **2026-10-06 17:19:41** show
   the mine/reeharvest lanes are live. Both CP queries in `queries.json` still carry `year_range [1960, 1998]`, i.e.
   the RD-130 facet, so their `numFound=0` rows are **not** a corpus null.

### 6.2 Query-design defects I found and did not paper over
- The CA task `CA 'CVS' pharmacy Woonsocket RI 1960-1995` combines a **bare acronym** with `state=Rhode Island`.
  The folk origin is an **Illinois** Jacksonville and a New England chain; the HQ is RI only from the 1990s onward.
  A geographic facet built from the present-state CSV row (trap 2 + trap 1 together) can only return nulls for the
  founding decade. The task's own `_note` is honest — *"no founding date for this company exists anywhere in this
  repo, so the window is a deliberately wide superset … NOT a claim about when the company was founded"* — but the
  state facet contradicts that.
- The predecessor-name task exists and is correctly labelled a hypothesis: `CA 'Consumer Drug Stores'/'CVS' Rhode
  Mass 1960-1990 (NAME-VARIANT HYPOTHESIS: … not an assertion of it)`. Note the string it searches,
  **"Consumer Drug Stores"**, is not the string the folk story uses (**"Consumer Value Stores"**); only the
  internet_archive task has `"consumer value stores"`. If the name is `Consumer Value Stores`, the CA newspaper route
  was never searched under it. That is a naming-wall defect, not a null.
- The `IA CVS drug store periodical text` task and both CP tasks carry the year facet (§6.1.7).

## 7. Recital route: what I ran, what I refuse to overwrite, and the FETCH REQUESTs — STATUS: WRITTEN

The in-window SEC family cannot answer the origin (floor 1994-02-10 vs a 1963 event; 0 hits for `1963`/`founded`), so
per the brief's recital route the founding sentence must be sought in **later** paper. The local index tells me exactly
where to look without re-searching EDGAR (§INDEX.md: *"This file is the source of truth for what exists"*). First
carriers past the window edge, from `submissions_CIK0000064803.csv` (130 rows 1996-06-01→2002-12-31; the 1996-2000
rows carry **no** `primaryDocument` — the 125-row paper-era defect, so a document name must be enumerated, never
assumed): `10-K405 1997-03-31 (0000950135-97-001475)`, `S-4 1997-03-28 (0000950103-97-000191)`,
`424B4 1997-07-24 (0000950123-97-006169)`, `S-4 1998-03-02 (0000950103-98-000217)`, `424B1 1998-05-22`,
`10-K 1999-03-31 (0001029869-99-000377)`.

**What I refused to run, and why.** `python tools/sec_intake.py auto … --from 1997 … --to 2006` would answer this, but
reading the tool before touching it (`tools/sec_intake.py`, `auto` branch) shows `auto` writes `_PLAN.csv`,
`_MANIFEST.csv`, `_UNANSWERED.csv`, `_SKIPPED.csv` and `_RUN.json` through `_write_verified`, which is an unconditional
`open(path,"w")`. A forward-window `auto` would therefore **replace the in-window intake record** (window
1963→1996, 7 stored, 40 skipped) with a description of a different pass. That is hard rule 2 (`Add only`) and §14 r4
(one agent writes only what its brief names) — the fleet's `_RUN.json` is not my file, and RD-134 already shows how
much judgment the project loses when an intake record stops describing the pass that produced the bytes. I did not run
it. I used `grab`, which writes only `<accession>_<document>.txt` + sidecar, i.e. pure add: **three grabs run, all
landed, results in §9.1-§9.3 and the verbatim commands in §12 (8.9).**

`FETCH REQUEST:` blocks for the orchestrator (these are the correct behaviour, not gaps):

FETCH REQUEST: R-1 — recital pass for the origin sentence. **STILL OPEN, priority lowered.**
  tool: `python tools/sec_intake.py auto "CVS HEALTH Corp" --company-dir founders_playbook/01_companies/company_006_cvs --from 1997-01-01 --to 2006-12-31 --max-docs 12`
  why: `pass2_status` empty in `00_universe/_FLEET_INTAKE.tsv`; the 1963 event can only be recited by paper the window excludes (RD-134/Ford).
  note for the runner: this overwrites `sources/sec/_RUN.json`, `_MANIFEST.csv`, `_PLAN.csv`. The pre-state is recorded verbatim in §8.2 of this file. Land the two records as separate windows (e.g. key by window) or let the fleet lane do it.
  lowered because R-2's sample already produced the recital (§9.1); what R-1 adds beyond that is a **named 1963 legal
  person / founding town**, which nothing held yet supplies. Run it before the volume author writes §B or §Q.

FETCH REQUEST: R-2 — two named accessions, document-level, no directory assumption. **CLOSED BY THIS PROBE — both
fetched and read (§9.1, §9.2), plus a third, `0000950103-96-001174`, which is in-window (§9.3). Do not re-run these
accessions; 3 files totalling 1,416,914 B are on disk under `sources/sec/` and are absent from `_MANIFEST.csv` (§12.8.9).**
  `python tools/sec_intake.py grab --company-dir founders_playbook/01_companies/company_006_cvs --cik 0000064803 --accession 0000950135-97-001475` (10-K405, FY1996, filed 1997-03-31 — first annual report of the renamed registrant)
  `python tools/sec_intake.py grab --company-dir founders_playbook/01_companies/company_006_cvs --cik 0000064803 --accession 0000950103-97-000191` (S-4, filed 1997-03-28)
  why: both post-date the 1996 IPO/reorganisation boundary and are the likeliest filed carriers of a "founded/first store/1963" recital. `grab` with no `--file` enumerates the accession's documents rather than guessing (RD-130 fix), so these are safe adds.

FETCH REQUEST: R-3 — family (d) facet-free corporate print, 4 un-refined params removed.
  `python tools/periodical_harvest.py --company cvs --facet-free` (fleet lane owns it tonight; `_REMINE_RUN.log` created 2026-10-06 17:14)
  why: the two `NULL` corporate-print rows are year-faceted (`year_range [1960,1998]`), so the archive has never been
  asked the question facet-free (RD-130). Digitised bound corporate print is the one family that has flipped tiers in
  this project (Walmart, Target, Boeing, Kroger).

FETCH REQUEST: R-4 — predecessor-name newspaper search under the right string.
  CA task with `andtext:"Consumer Value Stores"` (no state facet, 1960-1980) and a second with `"Melville"` +
  `drug` for 1963-1979; the existing CA rows searched `"Consumer Drug Stores"`, a string no carrier in this repo uses.
  why: §6.2; and because the CA family is currently TRIED–UNANSWERED, so the remedy is a re-run, not a re-guess.

## 8. Measurements log — every quantifier in this file, with its command — STATUS: WRITTEN

### 8.1 CSV headers enumerated before any field was read by name (hard rule 3)
- `00_universe/fortune_top_50_2026.csv` → `rank,company,revenue_usd_millions,revenue_fiscal_year,profit_usd_millions,hq_city,hq_state,fortune_industry,universe_source_url,verified_by_second_source,confidence,notes` — **no founding-date column**.
- `00_universe/harvest/candidates.csv` → `company,source_family,query,item_id,title,date_or_issue,url,snippet_or_hitcount,http_status,classification,retrieved_at` (3,802 rows; `cvs` rows = **78**). No `query_label`, no `date` — those were RD-124's/RD-121's lost columns; this file's label lives in `query` and its date in `date_or_issue`.
- `sources/_index/submissions_CIK0000064803.csv` → `filingDate,form,accession,reportDate,primaryDocument,source` (2,968 rows).
- `sources/sec/_MANIFEST.csv` → `rank,slot,cik,accession,file,path,bytes,words,status,form,filingDate,url,why,listing`.

### 8.2 The 7 stored SEC documents, as filed (`sources/sec/_MANIFEST.csv`, quoted)
| form | filingDate | accession | bytes | subject / filer in the header |
|---|---|---|---|---|
| SC 13G/A | 1994-02-10 | 0000912057-94-000290 | 20,338 | subj MELVILLE CORP + INVESCO MIM PLC — **this is the filing floor** |
| DEF 14A | 1994-03-14 | 0000950110-94-000065 | 84,886 | MELVILLE CORP, meeting 1994-04-12 |
| 10-K | 1994-03-31 | 0000950110-94-000133 | 228,697 | MELVILLE CORP, period 19931231 |
| 10-K | 1995-03-29 | 0000891092-95-000026 | 267,332 | MELVILLE CORP (FY1994; header block absent — see §8.8) |
| 8-K | 1995-10-26 | 0000950103-95-000374 | 18,566 | MELVILLE CORP |
| 10-K | 1996-03-29 | 0000891092-96-000050 | 439,005 | MELVILLE CORP, period 19951231 |
| SC 13D | 1996-04-08 | 0000950103-96-000813 | 33,013 | **subj = TJX COMPANIES INC /DE/ (CIK 0000109198, formerly ZAYRE CORP)**; filer = MELVILLE CORP |
Sum 1,091,837 B — matches `_RUN.json` `bytes` exactly. `_UNANSWERED.csv` is header-only (0 rows); `_SKIPPED.csv` = 40 slots past `--max-docs 30` … note the internal tension: `_RUN.json` records `max_docs 30` but only 7 were attempted, so the 40 skips are the **per-filing document cut**, not the doc cap. Reported, not reconciled.

**The SC 13D row matters more than its size**: the only stored document that names CVS-named legal persons in bulk is a
**TJX** filing (Melville's receipt of TJX preferred stock as Marshalls consideration). Reading it as "CVS's 1996
control filing" is the same mistake as RD-133's abbreviation slugs mining nothing.

### 8.3 Shelf census (commands: `find sources -name '*.txt' | wc -l`, `wc -c -l`, `md5sum`)
17 `.txt` total = 7 (`sources/sec`) + 4 (`sources/corporate_print`, 5,987,081 B) + 6 (`sources/periodicals`, 5,908,027 B).
47 files under `sources/` overall. Cross-shelf md5 duplicates: 2 (§4). After dedup: **8 unique non-SEC documents**.

### 8.4 Origin-term census across the 7 stored SEC bytes
`python` over `sources/sec/*.txt`, case-insensitive, whitespace-normalised:
`1963` → **0**; `Consumer Value` → **0**; `Jacksonville` → **0**; `Woonsocket` → 2 (both in the SC 13D, as the
address "One CVS Drive, Woonsocket RI 02895"); `founded` (word) → **0**; `Woolworth` → **1** (1994 proxy peer list:
`Dayton Hudson, Edison Brothers, JC Penney, Longs Drug, Merry Go Round, Rite Aid, Sears, TJX, Toys R Us, U.S. Shoe,
Walgreen and Woolworth` — DEF 14A 0000950110-94-000065). Narrower claim preferred over "the filings say nothing": they
say a great deal about Melville and its CVS subsidiaries, and **0 things about a 1963 founding**.

### 8.5 Mine census (`sources/harvest_mine/_index.json`, quoted programmatically)
`window ["1963-01-01","1996-12-31"]`, `candidates 36`, `mined 6`, `untried_by_limit 29`. Per-item verdicts as mined:
`micro_IA40706901_0405` (DSN 1980) `TIER1_CANDIDATE_TEXT`, entity `cvs stores`, 5 hits, best line L14496
`. CVS Stores, Woonsocket, R.!. Baton Rouge, La.` → an **advertisement/directory line**, and note `R.!` for `R.I.`:
OCR decoy class, hard rule 6. `micro_IA40706934_0338` (DSN 1990) entity `cvs sales`, 66 hits, L61811
`CVS sales in 1989 totaled $1.02 billion. Peoples had $1.02 bil-`. `micro_IA40706951_0247` (DSN 1995) entity
`cvs stores`, 154 hits, L21684 `Peoples stores (renamed CVS stores` — the trade-name conversion, a *variant-term*
fact about Peoples, not a naming of the registrant's origin. `micro_IA40706918_0157` (DSN 1985) `VARIANT_TERM_HIT`
(18 hits, all `Drug Store News` subscription boilerplate — i.e. the **journal's own name** matching a query term
about the journal; zero entity hits). Two index volumes `NULL`, 0 hits.
I did **not** run `harvest_mine.py` (fleet lane owns it tonight).

### 8.6 Why Google Books contributes no counted family
8 `TIER1_CANDIDATE` + 4 `LEAD_ONLY` rows, item dates 1997, 1999, 2005-2008, 2006, 2007, 2020 — Plunkett's industry
almanacs, `The Almanac of American Employers`, `Hayes Druggist Directory`, `American Druggist`, a textbook. Every one
post-dates the window; the `TIER1_CANDIDATE` string is `classification` **in a harvester index**, which RD-124
established can be an artefact of the query text echoing. Not counted (hard rule 6, §3).

### 8.7 The mine's own `named_terms`/`other_terms` census
Every mined item carries `named_terms: []` and `other_terms: ["consumer drug stores","drug store news","pharmacy times"]`.
So the corpus never printed a *name phrase* hit of the kind RD-124 calls entity-bearing ("CVS Corporation"/"Consumer
Value Stores"); its entity promotions come from the `cvs`+noun identity-word pattern (`cvs stores`, `cvs sales`). That
is a real naming of the **brand's retail estate** in 1980-1995 and nothing at all for 1963-1979.

### 8.8 One artefact honestly reported as unexplained
`0000891092-95-000026.txt` (FY1994 10-K, 267,332 B) returns **no** `CONFORMED SUBMISSION TYPE` / `COMPANY CONFORMED
NAME` / `CENTRAL INDEX KEY` header fields under my regex pass, yet its body prints *Melville Corporation, a New York
corporation* and a subsidiary list naming `CVS, Inc., a Rhode Island corporation`. Either the SGML header is malformed
in the stored copy or my extraction pattern is too strict for it. **Recorded as a defect in my measurement method, not
in the file** — the identity claim in §1.1 rests on the other 6 headers plus the body text, so it stands; the form/date
for this accession comes from `_MANIFEST.csv` (`10-K`, `1995-03-29`), not from my regex.

## 9. The recital route, run add-only: this is what changed — STATUS: WRITTEN

I did not run `auto` (§7). I ran the pure-add form the tool itself documents, three times, and all three landed.
Commands and returns are in §8.9.

### 9.1 Family (a) now ANSWERS the origin question — by recital, Tier-1, one lineage
`sources/sec/0000950103-97-000191_0000950103-97-000191.txt` — Form **S-4**, filed as of **1997-03-28**, filer
`CVS CORP`, `CENTRAL INDEX KEY 0000064803`, `STATE OF INCORPORATION: DE`, `SIC: RETAIL-DRUG STORES AND PROPRIETARY
STORES [5912]`, `IRS NUMBER 050494040`. At **L762-765**:

> "Founded in 1963, CVS is the country's fifth largest drugstore chain in terms of store count and sales volume, with
> approximately 1,400 stores and $5.5 billion in 1996 annual revenue. CVS operates in 14 states along the Northeastern
> seaboard and the District of Columbia."

and immediately, **L767-770**:

> "In November 1996 CVS changed its name from Melville Corporation to CVS Corporation, reflecting its concentration on
> the chain drugstore business and the completion of its restructuring program that was approved by its Board in 1995
> following a strategic review initiated in 1994."

So the registrant's own Tier-1 paper **does** say 1963 — 34 years after the event, in a document about the **Revco D.S.,
Inc. merger** (Revco at 1925 Enterprise Parkway, Twinsburg, Ohio, L772-780; 1,737 `Revco` occurrences in the file).
CLASS: the sentence's existence is a FACT; the 1963 event it asserts is a **corporate self-narrative, RETROSPECTIVE
SOURCE (§6)** — exactly Disney's 21-years-late "YEARS OF PROGRESS" pattern (RD-130) at 34 years. Confidence for the
date: **Medium**, capped by §3 (an S-4 + its amendments + the 424B are one source; here there is not even a second
document in the lineage saying 1963 — see §9.2).

**Critically, what the recital does NOT say.** In this 877,087 B file: `Consumer Value` → **0**, `Jacksonville` → **0**,
`shoe` → **1** (and that one hit is the EDGAR header line `FORMER CONFORMED NAME: MELVILLE SHOE CORP`, L53),
`first store` / `first drugstore` → **0**, `Lowell` → **0**, `Kandel` → **0**. The registrant gives a **year and nothing
else**: no town, no original name, no business type. A Stage-1 author who writes "1963, Jacksonville, shoe store" is
supplying three facts that no held byte supplies.

### 9.2 The FY1996 10-K405 — the registrant's first annual report under the new name — says **no** 1963 at all
`sources/sec/0000950135-97-001475_0000950135-97-001475.txt` — Form **10-K405**, period 19961231, filed 1997-03-31,
`CVS CORP`, CIK 64803, **DE**, EIN 050494040; header carries *both* former-name records (`MELVILLE CORP`,
`MELVILLE SHOE CORP`). Item 1 opens (**L158-161**): *"CVS Corporation, a Delaware corporation ("CVS" or the "Company"),
is a leader in the chain drug industry with over $5.5 billion in revenue in 1996. As of December 31, 1996, the Company
operated 1,408 stores, in 14 states and the District of Columbia…"*
Measurements in this file: `1963` → **0**. And two dated lineage facts that matter more than a founding myth:
- **L469**: *"Pharmacare, founded in 1994, provides managed care providers a full range…"* — the health-services/PBM leg
  has its **own** founding date, later than everything else, under a name that survives nowhere in the modern brand
  (trap 2 answered: the insurance/PBM leg is `Pharmacare` / `Pharmacare Management Services, Inc., a Delaware
  corporation`, FY1994 10-K, accession 0000891092-95-000026).
- **L8352, L8376**: the operating and holding legal persons as of FY1996 — *"…Pharmacy, Inc., a Rhode Island corporation,
  and CVS H.C., Inc., a Minnesota…"* and *"…Connecticut corporation and CVS of DC & VA, Inc., a Maryland corporation…"*.
  So `CVS, Inc. (RI)` of the 1994 filings is by 1997 **CVS Pharmacy, Inc., a Rhode Island corporation**, and the
  `CVS H.C., Inc.` the 1996 SC 13D put in Minneapolis is on the record as a **Minnesota** corporation.
- **L178-186**: the restructuring plan "the product of a strategic review initiated in 1994", 29 `restructur*` hits —
  the 1994→1996 sequence is the registrant's own account of *becoming* a pure drugstore company.

### 9.3 The 1996 boundary, measured inside the window — and it is not an IPO
`sources/sec/0000950103-96-001174_0000950103-96-001174.txt` — Form **8-B12B** ("FOR REGISTRATION OF SECURITIES OF
CERTAIN SUCCESSOR ISSUERS", L62-70), filed **1996-11-04**, cover **L73-74** *"CVS CORPORATION (Successor to Melville
Corporation)"*, **L80** *"Delaware Applied For"*. Its header is still `MELVILLE CORP / NY / EIN 041611460` — the
predecessor filing on its own successor's behalf.
- **L108-109**: *"CVS Corporation ("CVS" or the "Registrant") was organized as a corporation on **August 22, 1996** under
  the laws of the State of Delaware."*
- **L115-116**: *"Melville Corporation, a New York corporation ("Melville"), which will be the predecessor of the
  Registrant at the time of the succession…"*
- **L120-133**: the registration is for a **reincorporation** ("Proposal: To Change the State of Incorporation From New
  York to Delaware", proxy statement dated 1996-10-07), producing *"shares of a new Delaware holding company named
  "CVS Corporation""* with *"Melville thereby becoming a wholly owned subsidiary of CVS"*.
- **L136-142**: triangular merger — *CVS New York, Inc.* ("Merger Subsidiary") merges into Melville; Melville is the
  **Surviving Corporation** and is renamed **"CVS New York, Inc."**; merger agreement dated **1996-08-30** (L149).

This is the answer to trap 3, with a date and a carrier. The registrant's current corporate form is **Delaware,
organized 1996-08-22**, i.e. **33 years after the claimed 1963 origin and inside the probe window** — and the mechanism
is **succession, not flotation**. Cross-check on the same registrant's EDGAR record: `S-1` rows in the 2,968-row index =
**0**, `S-1/A` = **0**, `SB-2` = **0**, `10-A` = **0**, `8-B12B` = **1** (§8.10). The only 1996 IPO named in the S-4 is
someone else's: **L3184** *"initial public offering for CVS' former subsidiary, Linens 'n Things, Inc."* (a banker's
transaction list, not a CVS flotation). So a Stage-1 dossier may not call 1996 "CVS's IPO" on this corpus; it may call it
a **reincorporation-and-rename with a Section 12(b) succession registration**. Whether CVS equity was separately floated
in 1996 is **UNKNOWN here** and is a `data_gaps` row with importance High for the volume author.

### 9.4 Legal-person resolution for every candidate date (the trap-2 answer, now with carriers)
| Candidate date | What it names | Legal person it attaches to | Carrier (file : line) |
|---|---|---|---|
| 1963 | "Founded in 1963" — the registrant's own retro-claim about "CVS" | CIK 64803 as it then stood (**Melville Corporation, NY**, renamed CVS Corporation Nov 1996) speaking of its **business**, not of a Delaware or RI corporation | `sources/sec/0000950103-97-000191_…txt : L762` |
| 1963 | "Consumer Value Stores" as the **name of the chain** (no date attached) | the chain/brand, parent Melville Corp | `sources/periodicals/micro_IA40706934_0338_djvu.txt : L33007` (DSN 1990); `…micro_IA40706938_0038_djvu.txt : L38088` (DSN 1990); `…micro_IA40706944_0407_djvu.txt : L34084` (DSN 1993); `…micro_IA40706948_0070_djvu.txt : L39047` (DSN 1994) |
| 1976-06-30 | Melville Shoe Corp → Melville Corp | the registrant itself | EDGAR header of every stored file, e.g. `…96-001174…txt : L48-50` |
| 1990 | "CVS acquired Peoples Drugs Stores in 1990" | Peoples' Drug Stores, **a Maryland corporation** (FY1993/FY1994 10-K subsidiary lists) | `sources/sec/0000950103-97-000191_…txt : L1576-1577`, `: L3424` |
| 1994 | "and Standard Drug Stores in 1994" | Standard Drug (a chain, not a naming of the registrant) | same file `: L1577` |
| 1994 | Pharmacare, PBM subsidiary, founded 1994 | Pharmacare / Pharmacare Management Services, Inc., a Delaware corporation | `sources/sec/0000950135-97-001475_…txt : L469`; `…0000891092-95-000026…txt` (FY1994 10-K subsidiary list) |
| 1996-08-22 | **the registrant's own corporate form** | CVS Corporation, a Delaware corporation | `sources/sec/0000950103-96-001174_…txt : L108-109` |
| 1996-11 | name change Melville → CVS Corporation | same registrant | `…97-000191…txt : L767`; 10-K405 header `FORMER CONFORMED NAME: MELVILLE CORP` |
| 1996-11-17 | Marshalls sold to TJX (event date of the SC 13D) | Melville ↔ TJX Companies, Inc. /DE/ (CIK 0000109198, formerly Zayre Corp) | `…96-000813…txt : L22-23, L396-400` |

### 9.5 Family (c) upgrade, and the decoys that had to be cleared first
The trade press is **independent** of the SEC lineage (Lebhar-Friedman's *Drug Store News*, not the company's paper), so
the `Consumer Value Stores` naming is a genuine second lineage for the **name** — §3's independence rule satisfied for
"the chain formerly/also called Consumer Value Stores", **not** for the date 1963 (which appears in the press only as
noise). Decoys I had to measure before I could count it (trap 1):
- `1963` in `micro_IA40706915_0203` (DSN 1984) → **10 hits**, all stock-table/ad digits: `Pay Less NW PAY 1963 1750
  = 1788 …` (L917), `… Spectro Indus SPO 2275 1963 2000 …` (L2313), `Dentemp … ©1963 mnt OMG CO. NY 10454` (L7199).
  A grep for "1963" in this family produces **another company's prices and other companies' copyright years**.
- `1963` in `micro_IA40706938_0038` (DSN 1990) L40105 is a **different chain's founding, told as a rival's story**:
  *"…just how far this company has come since its founder opened **Civic Drugs in Dearborn, Mich. in 1963**."* If a
  later pass greps "1963 + founder + opened" it will find **Kmart's** antecedent, not CVS's.
- `Consumer Value` generic in `micro_IA40706928_0007` (DSN 1988) → **5 hits, 0 of them the company name**:
  "extra consumer value" (a lighter advertisement, L29890), "special consumer values" (soft-drink promotions, L61617),
  "new consumer value combo" (shampoo, L68255). RD-124's bare-word class, reproduced exactly.
- `JACKSONVILLE` → 1-6 hits per file in **seven** different DSN layers, with no CVS context: the **place-name trap**
  of RD-130 (J&J's "New Brunswick", Berkshire's "Town of Vermont"). My brief's "Jacksonville" is therefore *dangerous*,
  not helpful: the held press cannot tell Jacksonville FL from Jacksonville IL, and neither can a grep.
- `Woolworth` → 16 hits in DSN 1990, 13 in 1985: Peoples Drug was Woolworth's chain before Melville, so the word is
  real and belongs to a **third** lineage.
- `Melville` → 21-39 hits per DSN layer 1984-1994: the parent is named in the trade press throughout S1c/S1d, which is
  why family (c) is stronger than my first pass (§3) scored it.
Verdict update for (c): **TRIED–ANSWERED**, entity + predecessor-name text **1980→1995**, in-window, third-party;
still **nothing before 1980**, and `untried_by_limit` is now **55** (§9.6).

### 9.6 The corpus moved under me during this run (§14 rule 11) — reported, not hidden
| Time (session) | `.txt` under `sources/` | mine `_index.json` | A4 dossier |
|---|---|---|---|
| 17:26 (first measurement) | 17 (7 sec + 4 cp + 6 per) | candidates 36 / mined 6 / untried 29 | stale, 3,712 B |
| 17:36 (this writing) | **28** (10 sec + 4 cp + **14** per) | **candidates 68 / mined 12 / untried 55** | regenerated **4,733 B, mtime 2026-10-06 17:28:41.110434400 +0530** |
New bytes that arrived while I worked (fleet lane, all in-window, all *periodicals* shelf): `micro_IA40706951_0252`
(DSN 1995, VARIANT_TERM_HIT), `micro_IA40706944_0407` (DSN 1993, TIER1_CANDIDATE_TEXT, entity `cvs sales`, 76 hits),
`micro_IA40706938_0038` (DSN 1990, `cvs sales`, 56), `micro_IA40706948_0070` (DSN 1994, `cvs stores`, 142), plus
index volumes 1981/1986/1990 (`NULL`) and `sim_pharmacy-times_1989_55_index` (VARIANT_TERM). I read `A4_harvest_mine.md`
immediately before quoting it, at **mtime 2026-10-06 17:28:41.110434400 +0530**, and it says: *"68 candidate rows in the
harvest index; 12 items mined; 55 left untried at the --limit."* Its class table says `BARE_WORD_MATCH | 0` — on the
bytes I read that is not the right frame (see §9.5: the bare-word hits are present in the files but were not promoted,
because the mine's entity vocabulary is `cvs stores`/`cvs sales` and its `named_terms` is `none`).
I did **not** run `harvest_mine.py` or `periodical_harvest.py`; the lane that owns them is live
(`00_universe/harvest/_REMINE_RUN.log` created 17:14, 0 B; `candidates.csv`/`_MANIFEST.md` mtime 17:19:41).

### 9.7 Supersessions issued by this section
- **§3 row (a)** now reads: **TRIED–ANSWERED for S1a by recital** (1997 S-4 L762) **and for S1d directly** (7 Melville
  docs + 3 new); the "0 occurrences of `founded`/`1963`" in §8.4 remains true **of the in-window set only** and no
  longer describes family (a) as a whole.
- **§3 row (c)**: TRIED–UNANSWERED-with-holes → **TRIED–ANSWERED**, in-window 1980-1995, two lineages for the *name*,
  one family only, still 55 untried.
- **§3 row (d)**: unchanged — **TRIED–UNANSWERED (facet), zero corporate-print bytes**. Tonight's new bytes all went
  to `sources/periodicals/`; `sources/corporate_print/` is still the same 4 IA serial layers (mtimes 2026-09-26 15:31).
- **§5 tiers**: replaced by the table in §5b below (I edited §5 in place rather than leaving a stale tier visible).
- **§10.1 and §10.8**: revised in place — the 1963 *date* is now carried; the 1963 *story* still is not.

## 10. What I refuse to claim, and why — STATUS: WRITTEN

1. **I refuse to claim CVS was founded in 1963 *as a Jacksonville shoe store called Consumer Value Stores*.** The
   *year* is now carried (registrant's own Tier-1 S-4, `Founded in 1963`, §9.1 L762) and I accept it as a
   Medium-confidence corporate self-claim. The **content** is not carried anywhere: `Jacksonville` → 0 in every SEC file
   I hold and 0 in any CVS context in the press; `Consumer Value Stores` → 4 in-window press hits, all **1990-1994**
   "CVS at a glance" boxes naming the *chain*, never a founding (§9.4); `shoe` → 1 hit, and it is EDGAR's own
   `MELVILLE SHOE CORP` header line, not a store. The dispatch brief asserted the full story; a brief is not a carrier
   (§14 r8). Written as: **1963 = FOUNDER/COMPANY CLAIM, retrospective, Medium; "shoe store / Jacksonville / Consumer
   Value Stores as the 1963 entity" = UNKNOWN, with the four press rows as the only partial support for the name.**
2. **I refuse to claim the registrant's origin is a pharmacy.** On the held bytes, CIK 64803's own words are a **New
   York corporation, diversified specialty retailer, formerly Melville Shoe Corp**. The pharmacy leg is a *division*
   (with Peoples, Standard Drug and Austin Drug alongside it) in 1993-1996.
3. **I refuse to treat 1996 as an origin or as a floor.** The 1996 IPO/reorganisation boundary is a **disclosure**
   boundary (trap 3): it is where CVS-named registrant paper starts, not where the business starts, and it is also
   where my own *search* window stopped. Keeping the two separate is the difference between a perimeter and a null.
4. **I refuse to claim 1994-02-10 is "when CVS began filing".** It is the earliest **indexed** filing for CIK 64803 in
   a walk that reached all slices (`_FLEET_INTAKE.tsv` `slices_capped no`; 2,968 rows ending 2025-05-13). EDGAR's own
   floor is 1993-94, so a pre-1994 silence is a **measured perimeter** (§15 tool note), not evidence of no filings:
   Melville was listed long before and its paper-era filings live outside EDGAR.
5. **I refuse to count the `corporate_print` shelf as family (d).** Its 4 files are Internet Archive serial layers with
   `family:"internet_archive"` in the mine index (§4). Reporting them as print would manufacture the RD-130 error in
   the opposite direction — a family "answering" with another family's bytes.
6. **I refuse to count a periodical item as naming the registrant** where the match is the journal's own title
   (DSN 1985, all 18 hits) or an OCR-degraded directory/ad line (DSN 1980 `Woonsocket, R.!`). Those are VARIANT_TERM /
   BARE_WORD-adjacent classes under RD-124 and must stay separated from entity-naming hits (trap 1).
7. **I refuse to publish a High-confidence periodical citation.** All 10 sidecars say `UNVERIFIED TLS`; capped Medium
   until re-verified (§4).
8. **I refuse to state that CVS's modern corporate form merely "postdates" 1963 without naming it.** Measured, and it
   is sharper than the brief's premise: the registrant's current form is **CVS Corporation, a Delaware corporation,
   "organized … on August 22, 1996"** (8-B12B L108-109, §9.3), which took CIK 64803 **by succession from Melville
   Corporation, a New York corporation** (L115-116, L120-142), with the EIN changing from `04-1611460` to
   `05-0494040` between the FY1995 and FY1996 filings — a *different taxpayer* wearing the *same CIK*. So the 1963
   recital attaches to **a business**, and the legal persons actually available in-window are: Melville Corp (NY),
   CVS Corporation (DE, 1996-08-22), CVS New York, Inc. (the renamed surviving Melville), CVS, Inc. (RI) →
   CVS Pharmacy, Inc. (RI), CVS H.C., Inc. (MN), CVS Center, Inc. (RI address), Nashua Hollis CVS, Inc., CVS of DC &
   VA, Inc. (MD), Peoples' Drug Stores, Inc. (MD), Standard Drug, Austin Drug, Pharmacare Management Services, Inc.
   (DE). **None of them is named in the bytes as the 1963 company.** Which one "CVS" was in 1963 is the volume author's
   §U conflict to adjudicate, and R-1 (a full forward recital pass over 1997-2006, e.g. the FY1999/FY2000 10-Ks and the
   2000s proffers) is the route most likely to name it.

## 11. The route most likely to change the verdict — STATUS: WRITTEN (final)

One sentence: **the recital route — one scripted forward pass (`sec_intake auto … --from 1997-01-01 --to 2006-12-31`)
over the same CIK 64803 lineage, which the fleet never ran (`_FLEET_INTAKE.tsv` `pass2_status` empty) and which I could
only sample add-only with `grab` — is the route most likely to change the verdict, because the three grabs I did run
already moved S1a from "0 families" to "1 family with a registrant-recited 1963" and produced the registrant's own
formation date (1996-08-22), so a fuller forward pass can still put a *named 1963 legal person* and a founding town into
Tier-1 text and would lift S1a/S1b toward T2.**

Runner-up, and it is a genuine second: **R-3**, the facet-free corporate-print reharvest, because family (d) is still
**zero bytes** and is the only family that has flipped tiers in this project (Walmart, Target, Boeing, Kroger); and
**R-5**, the 55 periodical candidates still untried at the `--limit` cut, which are the cheapest possible way to push
third-party naming back from 1980 toward 1963.

## 12. Addenda to §8 — the commands that produced §9 (appended here so the log stays in file order) — STATUS: WRITTEN

### 8.9 The three add-only fetches (verbatim returns; `web calls: 0`, scripts only)
```
python tools/sec_intake.py grab --company-dir founders_playbook/01_companies/company_006_cvs \
        --cik 0000064803 --accession 0000950135-97-001475 --file 0000950135-97-001475.txt
 -> status ok, 493,136 B, 61,886 words, url https://www.sec.gov/Archives/edgar/data/0000064803/000095013597001475/…
    form used: padded-cik/nodash-dir, tried_before: (none)
python tools/sec_intake.py grab … --accession 0000950103-97-000191 --file 0000950103-97-000191.txt
 -> status ok, 877,087 B, 127,094 words        [the S-4 that carries "Founded in 1963"]
python tools/sec_intake.py grab … --accession 0000950103-96-001174 --file 0000950103-96-001174.txt
 -> status ok, 46,691 B, 6,142 words           [the 8-B12B succession filing, IN WINDOW]
```
3 documents, 1,416,914 B added; `sources/sec/` now holds **10** `.txt`. No pre-existing file was modified:
`_RUN.json`, `_MANIFEST.csv`, `_PLAN.csv`, `_SKIPPED.csv`, `_UNANSWERED.csv` all still carry their
2026-09-30 00:31 mtimes and the in-window 7-doc record (§0). The 3 new sidecars were written by `grab` itself with
`http_status`, `sha1`, `bytes`, `words`, `accession`, `document`, `url_form`, so each add is attributable.
**Note for the merge:** these 3 files are *not* in `_MANIFEST.csv` or `_RUN.json`, so anything that counts "stored SEC
docs" from `_RUN.json` alone will under-count this company by 3 and will miss the only 1963 carrier. That is a
manifest/reality drift of exactly the RD-134 class, deliberately caused to avoid clobbering the lane's record.

### 8.10 Registration-statement census (from the local index, no network)
`sources/_index/submissions_CIK0000064803.csv`, 2,968 rows, `filingDate` min **1994-02-10**, max **2026-08-17**, rows
before 1994-01-01 = **0**. Form counts for flotation instruments: `S-1` **0**, `S-1/A` **0**, `SB-2` **0**, `10-A` **0**,
`8-B12B` **1** (1996-11-04, accession 0000950103-96-001174, `primaryDocument` empty — the 125-row paper-era defect).
`424B4` first appears 1997-07-24, `424B1` 1998-05-22. So: this registrant reached the public market on a **succession
registration**, and the EDGAR record contains **no CVS S-1** at all — which is why the window's "1996 IPO" frame had to
be refused (§9.3) and why the recital route is the only scripted way into the founding sentence.

### 8.11 Word count and self-check of this file
Regenerated at close with `wc -w`; see the probe report. Sections §0-§12 all `STATUS: WRITTEN`; no section left OPEN.

