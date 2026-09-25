# query_coverage_50.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T20:07:45Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## Schema

Agent `query-coverage`, 2026-09-26. Scope: **queries only**. A query block in
`tools/queries.json` is a REQUEST TO SEARCH. Nothing on this sheet or in that file is
evidence; no hit counts, verdicts, tiers or founding facts are recorded here, and a company
with a block is not a covered company.

**Baseline counted before any append** (script, not eye): `TASKS 58`, companies
`walmart 26 / unitedhealth 15 / alphabet 9 / apple 8` = **4 of 50** universe companies
carry blocks; 46 carry none.

**Exact schema copied from the existing blocks** — no new key names, no reordering, no
reformatting. Allowed keys per task (the union present in the shipped file):
`company`, `source_family`, `kind`, `query_label`, `window` (optional), `params` (optional),
`_note` (optional). Existing task objects are byte-frozen: appends land only immediately
before the `tasks` array's closing bracket, anchored on the unique sentinel
`],\n  "_corporate_print_reference_exemplar"`, so no existing task can be renumbered,
reworded or re-indented by this pass.

**Families used** — the five the harvester actually dispatches
(`periodical_harvest.py` `FAMILY_ACCEPT` + `planned_url`): `chronicling_america` (newspapers),
`internet_archive`, `hathitrust`, `google_books`, `corporate_print` (bound company print).
Every company block carries all five; `corporate_print` carries two (title-scoped +
creator-scoped, the Apple-verified forms) and `chronicling_america` two (HQ-city paper +
name-variant paper). 8 tasks per company.

**params grammar is the shipped grammar only** — CA `andtext/date1/date2/dateFilterType/state/sort`
(legacy params, kept because the shipped blocks keep them; the zone itself is blocked, see
`_endpoint_verification_20260925`, so CA rows stay UNANSWERED); IA `q/rows` with
`mediatype:texts` + `YEAR:[a TO b]`; HT `q1` + `facets:["bothPublishDateRange:\"YYYY-YYYY\""]`
(the only facet field the file says is real — a wrong field name returns a fake 0);
GB `q/max_results/endpoint:"feeds"` (keyless v1 is quota-0); CP `company_terms/scope_field/
report_terms/report_field/mediatype/year_range/rows/name_patterns` where `scope_field` and
`report_field` may only be `title` or `creator`, because `cp_search_url` raises on any other
field rather than shipping an invented parameter.

**Two labelling rules invented here and used on every block** (because the CSV carries ranked
fiscal years, never founding dates):
- `ERA: REPO-ANCHORED` — the window is traceable to a document already in this repository (a
  company probe under `01_companies/<dir>/research/`, an existing `queries.json` block, or the
  CSV's own note field). The block names the file.
- `ERA: UNREFINED-WIDE` — no founding date exists in this repo for that company. The window is a
  deliberately wide superset chosen from the CSV row's industry + HQ state, NOT a claim about
  when the company was founded, and it is labelled so in the block's own `_note`. Windows are
  never narrowed to a date nobody in this repo has read.
- `NAME-VARIANT HYPOTHESIS` — a predecessor or former-registrant phrase used in a query that is
  NOT asserted by any document in this repo. It is a search route for discovering a name, not a
  record of one; a 0 on such a query indicts only the hypothesis. Where the CSV note or a probe
  does name the variant (Target/Dayton Hudson, Price Club/Costco, PC's Limited/Dell,
  Google Inc./Alphabet, Cadabra/Amazon, Charter Med/Metropolitan Health Plans/United Healthplan,
  the ExxonMobil Holdings/Exxon Mobil Corp registrant split) the variant is labelled
  `NAME-VARIANT: repo-attested`.

**per_source_caps**: the shipped `_note` states in terms that a cap below the task count writes
`SKIPPED: per-source cap reached` UNANSWERED rows for tasks never attempted — i.e. it
re-creates the exact untried-family-as-null defect this pass exists to close. Raising the six
numbers is therefore mandatory, not cosmetic; it changes no task and no existing text, and the
before/after values are in the Count section.

**Trade-journal back files named in `00_METHOD_AND_STYLE.md` §14 rule 6 / the harvest README**
and used where the industry fits: `Chain Store Age`, `Discount Store News`, `Progressive Grocer`,
`Stores`, `Women's Wear Daily`; plus the tech titles the corpus has already proved readable
(`BYTE`, `InfoWorld`, `PC Magazine`, `Popular Electronics`, Homebrew Computer Club newsletter) and
the sector titles carried as plain text queries. These are REQUESTS, not knowledge that any of
them holds the company.

## Per-company blocks authored

Batches of 10 companies, marked as each batch lands.

- [x] BATCH 1 ranks 1,6,7,8,9,10,11,12,13,14 — amazon, cvs, berkshire, mckesson, exxonmobil, cencora, microsoft, jpmorgan, costco, cigna (80 tasks)
- [x] BATCH 2 ranks 15,16,17,18,19,20,21,22,23,24 — cardinal, nvidia, meta, elevance, centene, bofa, chevron, ford, gm, citigroup (80 tasks, +1 repair task: see the Apple gap below)
- [x] BATCH 3 ranks 25,26,27,28,29,30,31,32,33 — homedepot, fanniemae, kroger, verizon, phillips66, marathon, stonex, statefarm, freddiemac (72 tasks)
- [x] BATCH 4 ranks 35,36,37,38,39,40,41,42,43 — att, goldman, comcast, wellsfargo, morganstanley, valero, dell, target, tesla (72 tasks)
- [x] BATCH 5 ranks 44,45,46,47,48,49,50 — disney, jnj, pepsico, boeing, ups, rtx, fedex (56 tasks)
- [x] BATCH 6 rank 34 — **humana** (8 tasks). Correction recorded: batch 3 was briefed at 10 companies and shipped 9; the 50-company fleet count caught the omission rather than the batch list, which is why the count check is scripted and not by eye.

**46 new companies, 369 new tasks, 8 tasks each (2 CA + 2 IA + 1 HT + 1 GB + 2 CP).**

## Per-company blocks authored (detail)

Every one of the 50 CSV rows now carries a block, and every block carries all five families
the harvester can dispatch — verified by script, not by eye (Parse check below).

**A second blind spot found by the same count, on a company that already had a block:** Apple
shipped 8 tasks in 4 families and had **NO `internet_archive` task at all** — while Apple's
exemplar-capable verdict is documented as resting on BYTE 1976/1977 and the Homebrew newsletters,
which live on Internet Archive. One `apple` / `internet_archive` task (BYTE + Homebrew, 1975-1982)
was **appended**; no shipped Apple task was altered. This is the §14 rule-6 error occurring one
level below the company level: a missing family *inside* a block reads as a searched family.

**Era basis, counted:** 8 of the 46 new companies carry a `REPO-ANCHORED` window
(amazon, costco, dell, meta, microsoft, nvidia, target, tesla — each named in its own block's
`_note` with the file it comes from). **38 of the 46 are `UNREFINED-WIDE`**: no founding date for
them exists anywhere in this repository, so their windows are deliberately wide supersets chosen
from the CSV row's industry + HQ state and are labelled as un-refined inside the block. No founding
year was guessed into any query. Home Depot is in the 38 even though a probe directory exists:
this pass's read of `company_025_homedepot` did not surface a dated Stage-1 span, and a wide window
was preferred to a narrowed guess.

**What is NOT in these blocks:** no hit counts, no verdicts, no tiers, no facts about any company.
Each `_note` records only (a) which document in this repo the window or name came from, or that none
did, and (b) the tokenisation hazard a query carries (ampersand/hyphen/space forms, short all-caps
tokens like `RTX`, surname-like brands like `Valero`/`Humana`/`Burke`).

## Name variants used

`NAME-VARIANT: repo-attested` (the name appears in a document already in this repo — the CSV note
field, an existing `queries.json` block, or a company probe):
- **target** — Dayton Hudson / Dayton Company / Dayton Corporation / J.L. Hudson / Target
  Corporation (`company_042_target/research/A_chronology_feasibility.md`, EDGAR `formerNames`
  1994-12-09→1999-04-12, and the held Dayton Hudson FY1965-FY1998 report layers).
- **dell** — PC's Limited / Dell Computer Corporation / Dell Technologies (the Dell probe's held
  BYTE Apr-1987 and Oct-1988 artefacts).
- **costco** — Price Club / The Price Company / Costco Wholesale (`company_013_costco` probe).
- **amazon** — Cadabra / Amazon.com (`company_001_amazon` Stage-1 records + the dispatch brief).
- **exxonmobil** — ExxonMobil Holdings vs legacy Exxon Mobil Corp (CIK 0002115436 / 0000034088),
  both registrant names queried (CSV note field verbatim).
- **alphabet, apple, walmart, unitedhealth** — already shipped (Google Inc./Alphabet,
  Charter Med / Metropolitan Health Plans / United Healthplan / Physicians Health Plan).

`NAME-VARIANT HYPOTHESIS` (a search route to a name NO document in this repo has established yet —
these are queries, and a 0 indicts only the phrase): Berkshire/Hathaway split; CVS/"Consumer Drug
Stores"; Citigroup/First National City Bank/Travelers; JPMorgan/Chase Manhattan; Goldman's
"&"↔"and" forms; AT&T/"Southwestern Bell"; Verizon/"Bell Atlantic"/"New York Telephone";
BofA/NationsBank; Humana; Disney/"Disney Brothers Studio"; PepsiCo/"Pepsi-Cola"; Boeing/"Pacific
Aerospace"; UPS/"…of America"; FedEx/"FDX Corporation"; Valero/"Diamond Shamrock"; Marathon/"Marathon
Oil"; Phillips 66/"Phillips Petroleum"; Fannie/Freddie long-form registrant names; Cigna/"Connecticut
General"/"INA"; Elevance/"WellPoint"; StoneX/"FCStone"/"INTL"; **RTX/"Raytheon"/"Hughes
Aircraft"/"E-systems"** (worst misnaming risk in the universe: a 2020-era ticker brand cannot appear
in an origin-period paper).

`NAME-DISCOVERY` (10 tasks): where neither the CSV nor any probe names a predecessor, the query
searches for the phrase `"formerly known as"` beside the current brand — cencora, stonex, rtx,
elevance, valero, citigroup, gm, bofa, kroger, marathon. That is a route to a name, not a name.

## Count before and after

```
BEFORE (scripted, first act of this pass):  TASKS 58
    walmart 26 / unitedhealth 15 / alphabet 9 / apple 8   = 4 of 50 companies
AFTER :                                       TASKS 427   (+369 authored by this pass, +1 repair = 370 new task objects)
```
Per-batch progression, each verified before the next opened:
`58 → 138 (B1) → 219 (B2, +1 apple IA repair) → 291 (B3) → 363 (B4) → 419 (B5) → 427 (B6 humana)`.

**Preservation of existing blocks — checked after EVERY append, not only at the end.** The 58
pre-existing tasks are the first 58 array elements in every reading, because appends land only
immediately before the array's closing bracket. Two SHA-1 digests over those 58 objects —
one over their `query_label` list in order, one over their `params` list in order — were taken
before any append and re-compared after each one:

| checkpoint | label digest | params digest | head-58 company counts |
|---|---|---|---|
| before append | `d645306e870e05f6` | `d6eab884c8134525` | walmart 26 / unitedhealth 15 / alphabet 9 / apple 8 |
| after B1 | `d645306e870e05f6` | `d6eab884c8134525` | identical |
| after B2 | `d645306e870e05f6` | `d6eab884c8134525` | identical |
| after B3 | `d645306e870e05f6` | `d6eab884c8134525` | identical |
| after B4 | `d645306e870e05f6` | `d6eab884c8134525` | identical |
| after B5/B6 (final) | `d645306e870e05f6` | `d6eab884c8134525` | identical |

No existing task was rewritten, reordered, renamed, reformatted or deleted; digests are byte-proof
of that, and they match at every checkpoint including the last.

**One non-task edit, declared:** `per_source_caps` numbers raised
(chronicling_america 17→120, internet_archive 40→115, corporate_print 16→110, hathitrust 9→60,
google_books 8→55; `chronicling_america_ocr` untouched at 4) and a new
`_caps_raised_20260926` key appended inside that object. No existing `_note` text was altered.
Rationale is the shipped note itself: a cap below the task count writes `SKIPPED: per-source cap
reached` UNANSWERED rows for tasks never attempted — leaving the caps at their 4-company values
would have re-created this pass's target defect for 369 of 427 tasks, so a "purely append-only"
reading of the file would have silently un-done the fix. Family counts after the append are
111/104/103/56/53, so every cap now sits above its own count.

## Parse check

Final scripted output, pasted verbatim:

```
PARSE OK. TASKS 427
HEAD58 companies {'walmart': 26, 'unitedhealth': 15, 'apple': 8, 'alphabet': 9} label True param True
DISTINCT COMPANIES 50 | per-company family complete: True
CSV rows 50
tasks whose params the harvester refuses to build a URL for: 0 of 427
```

`per-company family complete` means the set
`{chronicling_america, internet_archive, hathitrust, google_books, corporate_print}` is a subset of
the families present for EVERY company — the §14 rule-6 condition, checked structurally rather than
assumed. The last line is the stronger check: every one of the 427 task objects was passed through
`periodical_harvest.planned_url()` itself (URL construction only, no request sent), and none raised
— so no block in this file rests on an invented endpoint or a field the builder would refuse,
which is how the `scope_field`/`report_field` restriction (`title` or `creator` only) and the
HathiTrust `bothPublishDateRange` facet field were enforced by the tool rather than by my care.

Also verified: every appended task's key set is inside the shipped union
`{company, source_family, kind, query_label, window, params, _note}` — no new key names taught to
the fleet.

Two defects this pass created and fixed, recorded because a silent fix is a lost lesson: a malformed
param object (unquoted `date1`) and two trailing commas before the array close, each caught by the
parse check of the batch that introduced it, none surviving.

## Still unsearched

**This is the state of the fleet after this pass, and it is the sentence that must be carried
forward: every company now has a search route; none of the 47 previously-unqueried companies has
actually been searched.** Concretely:

1. **369 new tasks, 0 executed by me.** No request was sent for any of them (web budget 0, and
   none of them belongs in a query-authoring pass). No company has a hit count, a family outcome or
   a tier from this pass.
2. **46 companies have NO probe of any kind** — only 13 directories exist under
   `01_companies/`. All 46 remain UNTRIED in the §14 rule-6 sense until a harvester run reports on
   their block. Do not mark any of them covered.
3. **`chronicling_america` (111 tasks) is blocked, not empty.** This file's own `_endpoint_verification_20260925`
   proves 403 + `Cf-Mitigated: challenge` on every path including `robots.txt`. Every CA row this
   fleet produces stays UNANSWERED until a browser egress or the `Bentonville`/`Google Inc` canaries
   return 200. 111 tasks are queued against a host that may answer none of them — that is an
   untried family, and it must be reported as one, never as a null.
4. **`hathitrust` `/cgi/ls` is intermittent** (verified 200 earlier, 403 in a later window on the
   same bytes). 56 tasks; a 403 there is UNANSWERED-with-a-known-200-history.
5. **Two families are still not in this file's taxonomy at all**: `filings` (EDGAR, owned by
   `tools/sec_intake.py` and another live agent) and `web archives` / `auction-museum documentary
   sale records`. A five-family verdict cannot be closed from `queries.json` alone, and §14 rule 6
   requires all five searched. UNTRIED.
6. **No `corporate_print` `metadata`/`text` tasks were authored** — those kinds take an identifier
   copied verbatim from a live response, which is exactly the thing a pass with a 0 web budget
   cannot honestly supply. Every CP task here is a `search`; the follow-up that turns a promising
   identifier into held bytes is UNTRIED.
7. **38 windows are un-refined and stay that way** until a document narrows them. 24 tasks carry
   HYPOTHESIS-flagged names, and 10 are name-discovery queries whose whole purpose is to return a
   predecessor the repo does not yet name. A wrong predecessor name is a false null waiting to be
   read — which is the failure the Alphabet/Target/Dell probes each hit.
8. **`chronicling_america_ocr` cap left at 4 with 0 tasks** — deliberately: an OCR task needs a real
   `page_path` from a live CA response, and CA is blocked.
