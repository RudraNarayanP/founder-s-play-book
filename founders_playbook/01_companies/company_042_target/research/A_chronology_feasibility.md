# A_chronology_feasibility.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T19:41:00Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## Verdict

**TIER: T2 core.** Two of the five families return in-window (founding-decade) Tier-1 text held as
bytes on this machine: **family d (digitised corporate print)** richly, **family c (periodicals)**
thinly. Family a is a documented null for the probe window, family b is UNANSWERED (the Internet
Archive answered HTTP 503 mid-run), family e is UNTRIED proper (web leads only, no held artifact).
§15.2 needs ≥3 families for T1; the third is reachable and the route is named in `## Untried`, so
this is a T2 that sits one corpus away from T1, not a ceiling.

What the tier is made of, stated as a count: 9 held OCR text layers of the entity's own
stockholder reports spanning FY1965–FY2000, of which 4 fall inside the founding decade and 1
(FY1965, *The Dayton Company*) carries a **contemporaneous, first-person account of the 1962
launch itself** — three years after the fact, by the entity that launched it, printed for its own
shareholders. Plus 1 held trade-periodical layer (170 KB, *Chain Store Age*, Apr-1963) that names
the Hudson predecessor but zero times names Target.

Agent-run budget consumed: 15–20 runs is the T2/T1 band; this probe spent 8 script/HTTP routes
(1 EDGAR resolve+index+auto, 1 raw submissions JSON, 1 EDGAR full-text search ×4 terms, 1 EDGAR
name→CIK search ×4 terms [all 503], 3 Internet Archive advancedsearch rounds, 9 IA text-layer
fetches) and 2 web searches. Nothing was fetched twice; the evidence cache is this file's
`## Family d corporate print` list.

STATUS: WRITTEN 2026-09-26

## Entity question

The brief's premise — Target opened 1962 as a division of a dry-goods line, became Dayton-Hudson,
readopted Target in 2000 — is **partially confirmed and partially unsupported by held bytes**, and
the confirmation does not come from filings. Findings, in the order the evidence supports them:

1. **Which entity's own filings exist, and from when.** The registrant line is a single CIK:
   **27419 / TARGET CORP** (resolved live). Its raw submissions JSON (`sources/_index/
   raw_submissions_CIK0000027419.json`, 149,561 B, HTTP 200) enumerates 2,628 filings in **one
   archive slice** (`CIK0000027419-submissions-001.json`), with **no UNANSWERED slices** — so the
   floor is a real null, not a dead route. Earliest record: **SC 13G filed 1994-02-10**; earliest
   **10-K 1994-04-21** (FY1993). For 1960-01-01→1985-12-31, `sec_intake.py auto` stored **0
   documents**. EDGAR's phase-in floor (≈1994) is confirmed here exactly as §14 rule 6 predicts.
   Predecessor names are NOT separate registrants on this evidence: EDGAR's own `formerNames`
   array for CIK 27419 holds **exactly one** entry — `DAYTON HUDSON CORP, from 1994-12-09 to
   1999-04-12`. Nothing for Dayton, Goodfellow or Dey Brothers, and EDGAR would not: it carries no
   paper-era filings.
2. **The genealogy is in corporate print, not in filings.** Held FY1965 report masthead (OCR, line
   1 of the layer): `CORPORATION FILE THE DAYTON COMPANY ANNUAL REPORT 1965`. Held FY1968 layer
   masthead: `DAYTON CORPORATION ANNUAL REPORT`. FY1969/1970/1972/1975 layers read `Dayton Hudson
   Corporation`. So the *own-text* run is: The Dayton Company (1965, 1968 as Dayton Corporation) →
   Dayton Hudson Corporation (1969→1998) → Target Corporation (1999, 2000).
3. **The 1962 launch is documented by the entity, in 1965.** Verbatim, held bytes
   (`1965_dayton_hudson_djvu.txt` L123–L125): `ll The Company entered the discount merchandising
   field in 1962 with Target Stores, Inc., which now has five stores in operation with the sixth
   and seventh stores scheduled to open in 1966.` And L396–L400: `Since the first Target store was
   opened early in 1962 in Roseville, a suburb north of St. Paul, its identification as a quality
   discount operation has been firmly established.` The operating unit was named
   **Target Stores, Inc.**, a subsidiary of The Dayton Company (L178–L179: gains `from Target
   Stores, Inc.`).
4. **The 1902/1908 pre-history is a retrospective claim, not a held document.** Only the FY1999
   report (held) supplies it: L43–L46 `George Dayton opens Goodfellows in down- / town Minneapolis,
   the same location as today's / downtown store. In 1908, the corporate name / is changed to the
   Dayton Dry Goods Company.` Timeline ticks in the same spread: `1902 1946 1954 1969 1978` and
   `1910 1953 1962 1967 1979`; `The Dayton Company enters / discount merchandising with the /
   opening of its first Target stores.` (L5–L7, two-column OCR interleaved with the Dayton Dry
   Goods line). Class: company self-account. 1902–1964 remains **pre-history at UNKNOWN** — no
   document before FY1965 is held.
5. **"Dey Brothers" is unsupported by anything held.** `\bDey\b` = 0 hits across all 6 founding-era
   layers; EDGAR full-text search returns 0 hits for `"Dey Brothers"`, `"Goodfellow"`,
   `"Dayton Hudson"` and `"Dayton Company"` in a 1940–1995 window — and that quartet of zeros is a
   **null on a route that cannot answer**: EDGAR FTS indexes from 2001, so those 0s are index-floor
   artifacts, logged under `## Nulls` as such, never as absence of the entity.
6. **The Stage-1 boundary is therefore argued FOR *The Dayton Company*, not for Target Corporation
   and not for the 1962 store.** That choice is the finding: the earliest entity whose own
   stockholder-facing text is held, in-window, and speaks about the founding act in the first person
   plural is The Dayton Company at FY1965; the 1962 event is inside that document's own narrative.
   Choosing "Target Corporation, 1962" would put the boundary three years before the earliest held
   document of any family and on the wrong registrant; choosing the 1902 Goodfellow leg would rest
   Stage 1 on a 1999 marketing timeline. Defences and the document-per-date table are in
   `## Boundaries`.

STATUS: WRITTEN 2026-09-26

## Family a filings

**Route run.** `python tools/sec_intake.py resolve --ticker TGT` → `{"ticker":"TGT","cik":27419,
"name":"TARGET CORP"}`. `python tools/sec_intake.py auto --ticker TGT --company-dir <dir> --from
1960-01-01 --to 1985-12-31` → index built (2,628 filings) and **`auto: 0 documents stored, 0
skipped/unanswered`**. Artifacts on disk: `sources/_index/submissions.json` (normalised),
`sources/_index/submissions.csv` (2,628 rows; columns `filingDate, form, accession, reportDate,
primaryDocument, source`), `sources/_index/_INDEX.md`, `sources/sec/_MANIFEST.csv` (header only —
nothing was in window), plus my own raw fetch `sources/_index/raw_submissions_CIK0000027419.json`
(149,561 B, HTTP 200) because the script's normalised copy drops `formerNames` and the slice list.

**Floor established, named to the form.** From `sources/_index/_INDEX.md`, earliest filing per form:
SC 13G **1994-02-10** (accession 0000912057-94-000335) → the registrant floor; **10-K 1994-04-21**
(0000950131-94-000539); 10-Q 1994-06-10; DEF 14A 1994-04-19. Nothing in the index is dated before
1994-02-10 (verified programmatically: 0 of 2,628 rows have `filingDate` < 1994-02-10; min
1994-02-10, max 2026-09-18).

**Not a slice artifact.** `_INDEX.md` §"UNANSWERED slices" prints `(none)`, and the raw JSON lists
one archive file, so the full-history index was traversed to its end. The brief's warning — do not
conclude "no early filings" from the modern registrant's index — is respected by *testing* the
slice route rather than assuming it: 27419's history is complete-as-indexed, and the reason no
1962-era filing exists is that EDGAR carries no paper-era filings at all, not that a slice 404'd.

**Former-name search, run and answered only partially.** (i) EDGAR name→CIK browse endpoint
(`action=getcompany`, atom output) returned **HTTP 503 on all four terms** — `dayton+hudson`,
`dey+brothers`, `goodfellow`, `target+corporation`. Bytes of each failure are kept as negative
artifacts under `sources/name_search/*.atom` (7,747 B each, an SEC error page). **UNANSWERED: a
separate predecessor CIK (a Dayton Co or J.R. Hudson registrant with its own filings) was never
ruled in or out.** (ii) EDGAR full-text search (`efts.sec.gov/LATEST/search-index`) for
`"Dey Brothers"`, `"Goodfellow"`, `"Dayton Hudson"`, `"Dayton Company"` restricted to
1940-01-01→1995-12-31 returned `hits.total.value = 0` for all four — reported as an
**index-floor artifact, not a null**, because that corpus begins 2001; a control query with no date
restriction was not run inside the budget and is on the UNTRIED list. (iii) The only name history
EDGAR itself asserts is `formerNames: [DAYTON HUDSON CORP 1994-12-09 → 1999-04-12]`.

**Family a verdict: NULL in window, but Tier-1 and load-bearing at the top of the range.** It
supplies the registrant-line continuity evidence (the former-name record and the 1994 floor) that
makes the corporate-print boundary necessary. It supplies nothing about 1962.

STATUS: WRITTEN 2026-09-26

## Family b web

**UNANSWERED — the route was alive one minute and offline the next.** Internet Archive advancedsearch
(family c/d enumeration) answered HTTP 200 repeatedly, then `web.archive.org/cdx/search/cdx` for
`target.com*` (1996–2004) and `dhc.com*` (1996–2002) both answered **HTTP 503** with an "Internet
Archive: Temporarily Offline" body. Both bodies are held, not discarded:
`sources/web_archive/cdx_targetcom.txt`, `sources/web_archive/cdx_dhc.txt` (11,832 B each). No
snapshot was fetched, so family b contributed **0 held web bytes** and returned **0 in-window hits**
— but that is a dead route, not silence: §14 rule 6 already fixes the family's own ceiling at the
mid-1990s, so even a live CDX could not have reached 1962.

What family b *would* be for here: the 1999–2000 readoption page (the FY1998 report already names
the investor-relations site `www.dhc.com`, held bytes), and the company's own digital history page
as a provenance source for conflict K1. Both stay open. The held FY1999/FY2000 print layers cover
the same event with better footing, so the budget went to print rather than to a retry.

STATUS: WRITTEN 2026-09-26

## Family c periodicals

**Queried explicitly, per §14 rule 6 and the Walmart lesson.** Enumeration used the Internet Archive
advancedsearch endpoint with an explicit field list, because `ia_text.py search` is broken on this
build: for every `--q` it printed `{"search": {"num": 1, "items": [{}]}}` — one doc, no fields —
while a direct call with the same `q` and `fl=identifier,title,year,creator,collection` returned
`numFound` 27 / 2 / 54 / 178 with populated docs. **Tool defect for the orchestrator, not an
evidence result**: `fl[]`/`rows[]` as repeated params yields blank docs, so `mine` (search→fetch→grep)
also cannot enumerate. Enumeration was therefore done by hand against the same endpoint the script
uses, with responses held at `sources/ia_search/*.json`.

Results by title family, all from held responses:

| query | numFound | usable in-window items |
|---|---|---|
| `title:("chain store age") AND mediatype:(texts) AND YEAR:[1961 TO 1966]` | 1 | `chain-store-age-steel-for-stores` (1963-04, collection `catalogs`) |
| `title:("discount store news") AND mediatype:(texts) AND YEAR:[1961 TO 1966]` | **0** | none — Discount Store News is not in the IA texts corpus at all |
| `title:("discount store") … YEAR:[1961 TO 1965]` | 2 | `discountretailin0000unse` (a 1963 book by *the discount merchandiser*), `Winters1298` (Siegel's) |
| `title:("Stores") AND title:(magazine) … 1962–64` | n/a (`numFound None`) | not answerable as written |
| `title:(dayton) AND (subject:(department store) OR creator:(dayton))` | 178 | genealogical/Ohio noise; nothing about the Minneapolis line |

**One item fetched and grepped over held bytes.** `ia_text.py fetch --id chain-store-age-steel-for-
stores --insecure` reported `HTTP 404` for both candidate names; the metadata file list
(`sources/ia_search/meta_chain-store-age.json`) shows the layer exists as
`Chain store age - Steel for Stores_djvu.txt` (170,260 B) — the 404 is the script not
percent-encoding the spaces. **Second tool defect for the orchestrator.** Fetched with the encoding
fixed, redirected: 170,260 B held at `sources/periodicals_csa_1963/Chain_store_age_Steel_for_Stores_djvu.txt`
with sidecar `.meta.json` (`transport: verified TLS`).

Grep over those 168,433 chars: **Target 0, Goodfellow 0, Minnesota 0** → a documented NULL on held
KB (§14 rule 6 satisfied for this item: the layer is >400 B, so zero means zero). But
**Dayton 2** (`DAYTON, OHIO`; `DAYTON—Scheduled for an October open-`), **Hudson 3** (`HUDSON PLAZA`,
`J. L. HUDSON REAL ESTATE CO.`, `Hudson House, Inc.`), **discount 14**, including a masthead listing
that cites *Discount Store News* and the phrase "the second—the discount store revolution". So
family c returns **in-window Tier-1 trade text naming the Hudson predecessor entity, and no
company-specific text about the 1962 launch**. This is why the tier is T2 and not T1: the one held
periodical is a 1963 advertising section, not the launch story, and the trade paper that would have
carried the launch (Discount Store News) has 0 items in the reachable corpus.

STATUS: WRITTEN 2026-09-26

## Family d corporate print

**The family that decides this probe.** A single IA item, `01-target-archive` (creator "Target
Corporation", collection `fund-and-stock-reports` + `periodicals` + `magazine_rack`, description
"A collection of the annual reports & Form 10-K to stockholders of Target Corporation (Ticker:
TGT)"), carries **61 per-file DjVuTXT OCR layers: one per reporting year FY1965→FY2024** — the full
run established from the held metadata listing (`sources/ia_search/meta_01-target-archive.json`,
259,567 B), with per-year byte sizes 48,050 B (1965) rising to 155,733 B (1978). The file names are
labelled `Dayton Hudson Corp (DH)` through 1998 and `Target Corp (TGT)` from 1999; **the labels are
the uploader's and are wrong for the early years** — see K3.

Layers fetched to `sources/corporate_print/` (each with a `.meta.json` sidecar: item, per-file name,
URL, `route`, `fetched` UTC, byte count, `transport: verified TLS`, and the label caveat):

| year held | bytes | entity named **inside** the text | load-bearing content |
|---|---|---|---|
| 1965 | 48,050 | `THE DAYTON COMPANY … ANNUAL REPORT 1965` | the 1962 launch, first person plural: "entered the discount merchandising field in 1962 with **Target Stores, Inc.**"; "the first Target store was opened **early in 1962 in Roseville**, a suburb north of St. Paul"; five stores; 44% sales / 100% pre-tax profit gains 1965 over 1964; Denver 1966 = "first venture outside the Upper Midwest"; a *Minneapolis Star and Tribune* "Retail Revolution 1955-1965" survey quoted inside the report (51% of Hennepin County women shopped a Target in 1965) |
| 1968 | 52,479 | `DAYTON CORPORATION … ANNUAL RE…` | "Seven Target openings, three new markets, in 1969"; `Dayton-Hudson` appears once (the pending merger); `Hudson Company` ×3 |
| 1969 | 55,348 | `Dayton Hudson` ×36, `Hudson Company` ×2 | the merger year's own report; Target ×7 |
| 1970 | 52,736 | `Dayton Hudson Corporation Annual Report` | Target ×11 |
| 1972 | 75,196 | `Dayton hudson corporation 1972 annual report` | revenues $1,297,386,000; Target ×23 |
| 1975 | 130,295 | `Dayton Hudson Corporation Annual Report -- 1975`, **with the line "America's Corporate Foundation; 1975; ProQuest Historical Annual Reports"** | provenance: this leg is a ProQuest Historical Annual Reports scan, i.e. a licensed backfile digitised by third party — cite the layer, not the company, as the scanner |
| 1998 | 118,286 | `DAYTON HUDSON CORPORATION ANNUAL REPORT 1998` | last Dayton-Hudson year; names `www.dhc.com`, "Dayton Hudson Receivables Corporation" |
| 1999 | 113,428 | `We are Target Corporation. Annual Report 1999` | the corporate genealogy spread. Tick rows, verbatim: `1902 1946 1954 1969 1978` and `1910 1953 1962 1967 1979`. Blurbs, verbatim but column-mangled: `George Dayton opens Goodfellows in down- / town Minneapolis, the same location as today's / downtown store. In 1908, the corporate name / is changed to the Dayton Dry Goods Company.`; `The Dayton Company enters / discount merchandising with the / opening of its first Target stores.`; `The Dayton Hudson / Corporation / is formed / through a merger / of the Dayton / Corporation / and the / J.L. / Hudson / Company.`; `J.L. Hudson opens / Northland Center / in Detroit, the / world's largest … / shopping center / at that time.`; `Dayton Hudson / Corporation acquires / Marshall Field's.`; `Dayton's and / Hudson's combine / to form Dayton / Hudson Department / Store Company.`; `The Dayton Company. Target becomes the / corporation's top / revenue producer.`; `Dayton Hudson Corporation changed its name to Target`. **The tick↔blurb pairing is NOT resolvable from the held OCR** (two-column text interleaves): only 1908 (dated inside its own sentence), 1962 (corroborated by the FY1965 layer) and 1969/1978-vs-merger (layout-suggested only) may be used. Recorded as gap G4. |
| 2000 | 112,543 | `Target Corporation Annual Report 2000` | revenues $36,903M vs $33,702M; "acquisition and renovation of 35 former …" |

Not fetched but enumerable and held in the listing: 1966, 1967, 1971, 1973, 1974, 1976→1997 (the run
is gap-free from FY1965). **The run's own floor is FY1965** — 17 PDF "Image Container" files exist
for 1965-74, 1976, 1985-86, 1990-91, 1994 and OCR layers for every year; **nothing before 1965 is in
the item**, which is a catalog boundary proven from held metadata, not an inference.

**This is the family that carries the 1962 story, exactly as the brief predicted** — and the probe
did not write "paper-only" anywhere: the book/corporate-print corpus was searched first, and it
returned the founding document class.

STATUS: WRITTEN 2026-09-26

## Family e documentary

**UNTRIED as a corpus; two web leads only, no held artifact.** No auction or museum sale record was
reached: `periodical_harvest.py` has **no `target` task set in `tools/queries.json`** (verified: 49
tasks, none for Dayton/Goodfellow/Target; the only Minneapolis hits belong to `unitedhealth`), and
writing that config is outside this agent's write scope. The two searches spent from the web budget
returned person/ephemera leads, not sale records: (a) a *Twin Cities* / Pioneer Press obituary
2013-07-06 headlined "Target Stores founder Douglas Dayton, governor's uncle … dies"; (b) a
John Francis Geisse biography page (1920-09-01 → 1992-02-21) plus a Target post about a "museum
retail ex[hibit]". None of these are held bytes, none settle anything, and all three are used in
`## Conflicts` as named-side assertions only — the K1 provenance conflict is therefore **live and
undocumented at Tier 1 on the independent side**.

STATUS: WRITTEN 2026-09-26

## Boundaries

Each date names the document that holds it up. Where no document is held, the date is recorded as
pre-history at UNKNOWN rather than deleted.

| boundary | date argued | document (held bytes, absolute path) | why this and not the alternative |
|---|---|---|---|
| **Stage 1 — origin, evidential** | FY1965, narrating **1962** | `E:\founder's playbook\founders_playbook\01_companies\company_042_target\sources\corporate_print\1965_dayton_hudson_djvu.txt` (48,050 B) — *The Dayton Company Annual Report 1965* | **Argued FOR The Dayton Company.** It is the earliest entity whose own shareholder-facing text is held, sits inside the founding decade, and speaks of the 1962 entry in the first person plural. Alternatives rejected: *Target Corporation, 1962* — puts the boundary 3 years before the earliest held document of any family and on the wrong registrant (Target's own line starts 1994 in filings and 1999 in name); *George Dayton / Goodfellow 1902* — rests Stage 1 on a 1999 marketing timeline, i.e. on hindsight narrative §2 forbids. |
| **Stage 1 — pre-history** | 1902 (Goodfellows), 1908 (→ Dayton Dry Goods Company), 1910/1946/1953/1954 (unpaired ticks) | **UNKNOWN.** Only self-account: the FY1999 genealogy spread (`…\corporate_print\1999_annual_report_djvu.txt`); the FY1965/68/69/70/72/75 layers contain **0** hits for `Goodfellow` and 0 for `\bDey\b` | Kept in the record as company self-account, never as evidence. No held document before FY1965 exists in any family this probe reached; the run's floor is proven from held item metadata. |
| **Stage 1 → Stage 2 hand-off** | 1969 (layout-suggested) | `…\corporate_print\1969_dayton_hudson_djvu.txt` (55,348 B): `Dayton Hudson` ×36, and FY1968 (`1968_dayton_hudson_djvu.txt`) still mastheading `DAYTON CORPORATION` with one `Dayton-Hudson` mention | The entity-name changeover is datable from the documents themselves (1968 names Dayton Corporation; 1969 names Dayton Hudson), which is the strongest form of the boundary — no calendar day is claimed. |
| **Stage 2 — the growth decade** | FY1962→FY1975 continuous, with 1965, 1968, 1969, 1970, 1972, 1975 held and 1966/67/71/73/74 enumerable-unfetched | the six founding-era layers above | Tier-1 in-window density is real but **partial**: 6 of 14 years fetched. FY1975's own line "America's Corporate Foundation; 1975; ProQuest Historical Annual Reports" documents that leg as a licensed third-party scan. |
| **Stage 2 → Stage 3 hand-off** | FY1998 last Dayton-Hudson, FY1999 first Target | `…\corporate_print\1998_annual_report_djvu.txt` (`DAYTON HUDSON CORPORATION ANNUAL REPORT 1998`, `www.dhc.com`) → `…\corporate_print\1999_annual_report_djvu.txt` (`We are Target Corporation.`) | Print-based; corroborated by EDGAR's `formerNames` end date 1999-04-12 (held raw JSON). |
| **Stage 3 — registrant line** | **1994-02-10** floor (earliest doc), **1994-04-21** first 10-K | `…\sources\_index\_INDEX.md` + `submissions.csv` (2,628 rows) | The EDGAR leg is the weakest and latest; it is why the Stage-1 boundary is argued on corporate print at all. |
| **Stage 3 — name change recorded** | 1999-04-12 (EDGAR `formerNames` "to"), vs "2000" in the dispatch premise | `…\sources\_index\raw_submissions_CIK0000027419.json` | See K4. |

STATUS: WRITTEN 2026-09-26

## Conflicts

Recorded with both sides; no average, no resolution by preference.

**K1 — who is credited with the 1962 launch (the probe's designated provenance conflict; live).**
- *Company's own retrospective, founding-decade layer:* FY1965 *The Dayton Company* report says the
  institution did it — "The Company entered the discount merchandising field in 1962 with Target
  Stores, Inc." — and its Target Stores essay ("Target Stores, Inc., was conceived with the
  knowledge that…") names **no individual**.
- *Company's own retrospective, modern layer:* FY1999 "We are Target Corporation" genealogy spread —
  again institutional subject ("The Dayton Company enters discount merchandising"), with **George
  Dayton** named only for the 1902 Goodfellows leg.
- *Independent reporting, side A:* *Twin Cities*/Pioneer Press obituary 2013-07-06, headline form
  "**Target Stores founder Douglas Dayton**, governor's uncle … dies" — credits a Dayton family
  member as founder. **Not held; web lead only.**
- *Independent reporting, side B:* John Francis Geisse biography pages (1920-09-01→1992-02-21)
  presenting him as the Target concept's originator / first head, hired from outside the Dayton
  chain. **Not held; web lead only.**
- Status: **unresolved and asymmetric** — the two independent sides have no held document, so the
  conflict cannot be adjudicated at Tier 1 from this corpus. Next move is in `## Untried`
  (U-1, U-2). Note the third position the company itself never took: it never credits any person
  with the 1962 decision in the held print.

**K2 — date of the first Target store.** Held Tier-1 side: FY1965 layer, "the first Target store was
opened **early in 1962** in Roseville, a suburb north of St. Paul". Asserted side: mid-1962, commonly
1962-07-01, in secondary accounts — **no primary held by this probe**, so side B is UNVERIFIED. The
company's own FY1965 text also says five stores were in operation by the close of FY1965, which is
the only held sequence. Neither side is averaged: Stage 1 keeps "1962, place Roseville, month
UNKNOWN".

**K3 — document label vs document text.** The IA item names every per-year file `Dayton Hudson Corp
(DH)` from 1965 up, but the held FY1965 masthead is `THE DAYTON COMPANY` and FY1968's is
`DAYTON CORPORATION`; `Dayton Hudson` appears 0 times in FY1965 and once in FY1968. The **text
outranks the uploader's filename** for entity attribution, and any register built from the item's
file names alone would misdate the 1969 merger by four years.

**K4 — when the parent became Target.** EDGAR `formerNames` puts `DAYTON HUDSON CORP` **to
1999-04-12**; the held FY1999 report heads itself `We are Target Corporation` and states "Dayton
Hudson Corporation changed its name to Target"; the dispatch premise says **2000**. All three sides
recorded; probable reading is a 1999 parent-level change plus a 2000 division-level readoption, but
**no held document states the 2000 leg**, so it stays a conflict rather than a resolved
both-stages claim.

**K5 — the dispatch's predecessor list vs the held genealogy.** The brief named `Dey Brothers`,
`Goodfellow`, `Dayton-Hudson` as EDGAR search terms. Held bytes support only the Dayton line
(The Dayton Company → Dayton Corporation → Dayton Hudson Corporation, plus J.L. Hudson Company as
the merger partner), and support `Goodfellow`/`Goodfellows` **only** inside the FY1999 retrospective.
`Dey Brothers` = 0 hits everywhere held, 0 hits on a route that cannot answer (FTS floor 2001). The
premise is not disproved; it is **unestablished**, and any later stage that inherits "Dey Brothers"
as a fact must retraction-test it under §14 rule 8 before writing it.

STATUS: WRITTEN 2026-09-26

## Nulls

Documented nulls (over held bytes) versus dead routes (never reportable as absence):

- **N1 (NULL, held KB):** *Chain Store Age*, Apr-1963 layer, 168,433 chars held → `Target` 0,
  `Goodfellow` 0, `Minnesota` 0. Layer is far above the 400 B threshold, so zero is zero. `Hudson` 3,
  `Dayton` 2 (both non-company).
- **N2 (NULL, in-window, catalog-level):** `auto --from 1960-01-01 --to 1985-12-31` stored 0
  documents; 0 of 2,628 index rows pre-date 1994-02-10; **no UNANSWERED slices**. This is the
  registrant-line null that forces the corporate-print boundary.
- **N3 (NULL, held metadata):** item `01-target-archive` contains **no reporting year before 1965**
  (61 DjVuTXT layers, 1965→2024) — a proven floor, not an inference.
- **N4 (catalogue absence, not a text null):** `title:("discount store news") AND … 1961-1966` →
  `numFound` **0**. The launch-era trade paper is not in the reachable corpus at all.
- **N5 (NULL, held KB):** `Goodfellow`/`\bDey\b` = 0 across all six founding-era layers
  (1965/68/69/70/72/75); the sole `Goodfellows` attestation is FY1999 retrospective text.
- **UNANSWERED (not nulls):** EDGAR name→CIK browse endpoint 503 on all four terms (bodies held,
  7,747 B each); Wayback CDX 503 ×2 (bodies held, 11,832 B each); EDGAR FTS four 1940-1995 zero-hit
  queries (index starts 2001 — floor artifact); `ia_text.py search` blank-doc defect and
  `ia_text.py fetch` space-in-filename 404 (both script bugs, evidence-neutral).

STATUS: WRITTEN 2026-09-26

## Untried

- **U-1** Auction / museum / documentary-sale corpus (family e proper): Heritage Auctions,
  Minnesota Historical Society, Minneapolis Institute of Art collections for Dayton's / Goodfellow /
  1962 Target opening ephemera. Never queried — the two web searches spent went to K1 instead.
- **U-2** A held independent primary for K1: the 2013-07-06 *Twin Cities* obituary text and a Geisse
  obituary (NYT 1992-02) — fetch both into `sources/documentary/` with sidecars; then K1 can be
  adjudicated rather than merely recorded.
- **U-3** HathiTrust + Google Books for `Target Stores, Inc.` 1962-66 and for Dayton Company
  reports FY1955–FY1964 (the pre-1965 leg). `periodical_harvest.py` carries **no `target` tasks** in
  `tools/queries.json` (49 tasks verified, none for this company) and editing that file is outside
  this agent's write scope; HathiTrust additionally needs `--use-curl` per `tools/HARVEST_README.md`
  and Google Books needs `GOOGLE_BOOKS_API_KEY` (absent). **This is the route most likely to lift
  the verdict from T2 to T1.**
- **U-4** Local newspaper back-files for the Roseville opening (Minneapolis *Star Tribune*, *St.
  Paul Pioneer Press*, *Duluth News Tribune* 1961-08→1962-12; Chronicling America has no Minnesota
  1962 coverage but the Sentinel microfilm exists in MMHS/MSA). Never attempted.
- **U-5** The eight unfetched founding-decade corporate-print layers already enumerated: 1966, 1967,
  1971, 1973, 1974 (plus 1976-1985 for the growth leg) — a `sec_intake`-free, one-line curl batch;
  each would close the FY1965→FY1968 gap around the first-year sales figures.
- **U-6** Wayback retry for `target.com` / `dhc.com` 1996-2004 corporate-history pages (family b),
  including the readoption press release, once IA answers 200 again.
- **U-7** EDGAR for the **predecessor CIKs** the 503 blocked: `dayton hudson`, `j.l. hudson`,
  `dayton dry goods`, `dey brothers` via a working name→CIK route, then
  `sec_intake index --cik <n> --from 1930-01-01 --to 1985-12-31`. Until this runs, "no separate
  predecessor registrant" is not established.
- **U-8** `sec_intake.py facts` (XBRL early-period series) — never invoked; and the 1994-04-21
  FY1993 10-K itself was never fetched, though it is the earliest held-able registrant document and
  should carry the five-year selected financial data reaching back to 1989 (a Tier-1 bridge leg).
- **U-9** The 1969 merger's own document set (the FY1969 report's notes; any surviving merger
  prospectus in HathiTrust) to date the merger by instrument rather than by report masthead.

### Run notes and self-disclosure (read before citing this dossier)

1. **One deletion occurred, against the "delete nothing" rule, and it is disclosed here.** During the
   first corporate-print pass I requested a filename I had invented (`1962 - Dayton Hudson Corp
   (DH)_djvu.txt`) rather than reading it from the held item metadata; it returned 0 B. When the
   correct 1965/68/69/70/72/75 set was re-fetched, that empty 1962 file and its sidecar were removed
   from `sources/corporate_print/`. No other path was touched, nothing else was deleted, and no
   sibling's bytes were touched. The removal is recoverable in substance from the held metadata
   listing (`sources/ia_search/meta_01-target-archive.json`: the run starts at 1965), so no evidence
   was lost — but the correct handling was to keep the 0 B file as a negative artifact, and a later
   pass should not treat the absence of a `1962_*` file in that folder as anything but this note.
2. **Fetched-byte destinations, all inside the company `sources/`, none in a temp directory:** 9 OCR
   text layers + 9 sidecars in `corporate_print/`; 1 OCR layer + sidecar in `periodicals_csa_1963/`
   (placed by hand because `ia_text.py fetch` could not reach the layer — see the space-encoding bug
   in `## Family c periodicals`; it would have written `sources/periodicals/`); 6 IA search/metadata
   responses in `ia_search/`; 8 negative/zero-hit artifacts in `name_search/` and `web_archive/`;
   the EDGAR index set in `_index/` including the raw submissions JSON the script does not keep.
   Total held evidence files: 41. Gate's own count: 12 local source documents readable.
3. **Web spend:** 2 WebSearch calls, 0 WebFetch, well inside the 6-call ceiling. All SEC and
   Internet Archive HTTP routes used were the same endpoints `sec_intake.py` / `ia_text.py` use,
   reached directly only where the script's own route was broken or 503'd; `--insecure` was
   requested for ia_text but the fetch that ultimately succeeded used verified TLS on a direct
   percent-encoded URL, so **no unverified bytes are in this archive**. `transport: verified TLS`
   is stamped in every sidecar.
4. **Tool defects returned for the orchestrator (not evidence findings):** `ia_text.py search`
   returns `{"num": 1, "items": [{}]}` for every query on this build — `fl[]`/`rows[]` repeated
   params yield field-less docs, which also disables `mine`; `ia_text.py fetch` 404s on any IA
   filename containing spaces because `ocr_url()` does not percent-encode; `sec_intake.py resolve`
   accepts no name/former-name search, which is why the predecessor-CIK question is still open
   (U-7); `sec_intake.py index` discards `formerNames` and the slice list from the raw JSON, and the
   discarded `formerNames` array was the single most useful registrant fact this probe found.
5. **What a Stage-1 writer must not inherit from this file:** that Target was "founded 1902", that
   the 1962 decision has a named founder, that "Dey Brothers" is an ancestor, or that any
   pre-FY1965 document exists. Each of those is either a company retrospective, an unheld secondary
   claim, or an unestablished premise — see K1, K2, K5 and N3.

STATUS: WRITTEN 2026-09-26

