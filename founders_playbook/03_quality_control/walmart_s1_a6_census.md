# Walmart Stage 1 — the A6 re-census and repair (RD-123)

**Pass:** repair, not certification. Agent/claim owner `walmart-a6-census` (paths claimed via
`tools/scaffold.py` before writing: the four root registers, `CORRECTIONS.md`, `stage_1.md`,
`stage_1_index.md`, `_MANIFEST.md`, this file). **A different agent must certify.** Nothing here is a
verdict that the corpus is sound; the gate result below is a mechanical result on nine registers and three
volumes, and it says nothing about the five untried families.
**Company tier as issued:** exemplar (T1). **Date:** 2026-09-26. **Web budget spent: 0** — everything below
was read off bytes already on disk (§14 rule 8, §15.1).

---

## 1. The measured defect, re-verified line by line

| RD-123 / brief line | Re-measured on this pass | Verdict |
|---|---|---|
| A6 emits register rows in four fenced ` ```csv ` blocks, 22 rows, under a `>>> REGISTER ROWS FOR MERGE <<<` mark | parsed with the tool's own fence regex: 9 `sources.csv` + 6 `quantitative.csv` + 4 `timeline.csv` + 3 `conflicts.csv` = **22**, widths 18/12/11/15 — **no column drift**, unlike the 8 Target rows RD-122 had to re-join | **confirmed** |
| `grep -c "A6"` = 0 in all nine registers | 0 in all nine before this pass. Now: `sources.csv` 17, `quantitative.csv` 6, `timeline.csv` 4, `conflicts.csv` 3 (counting `A6_held_corpus_mine`); the other five registers carry no A6 content because A6 emitted none for them | **confirmed before, repaired now** |
| missing by content: FY1971 = 38, FY1973 = 64, FY1973 = 55, FY1973 = 9 | FY1971 = 38, FY1973 = 55, FY1973 = 9 absent. **FY1973 = 64 is NOT absent**: `quantitative.csv` carries a composite FY1973 row `Net income / EPS / Total assets / Equity / **Stores** / Inventories` = `4591469 / 0.70 / 46241 / 24754 / **64** / 29427119` (`S0102; S0103`). What is missing is a discrete fleet record, and that composite's `unit` cell omits stores entirely | **partly wrong — corrected here and at COR-305/COR-306** |
| the mine's FY1970 = 32 / FY1972 = 51 rows are "missing" | both values are already on the register (FY1970 = 32 discrete, `S0101`; FY1972 = 51 inside the composite). They were **not** re-minted; the second carrier was written into the existing cells | **folded, not dropped** |
| id collision: mine proposed `S0139`–`S0148`; those ids exist with different content (live `S0145` = EDGAR floor vs mine's `S0145` = the CA 403 bodies); the merge minted its own rows into the range | every one of the nine checked pair-by-pair; `sources.csv` had 47 rows, `S0101`–`S0147`, and the mine's `S0139`–`S0147` collide with all nine live rows. The merge's `+9` to sources is exactly that range | **confirmed** |
| `S0148` — "WALMART_AR_1973.txt is on disk but has no `sources.csv` row of its own, only being cited through S0102", "so that defect is still live" | **FALSE PREMISE, in both the log and the mine.** `S0102` **is** the FY1973 report's own row: `source_title` "Wal-Mart Stores, Inc. Annual Report, fiscal year ended January 31, 1973", `event_date` 1973-01-31, `publication_date` 1973-03-20, `archived_url sources/periodicals/WALMART_AR_1973.txt` — and it is in the 38-row `research/sources.csv` the mine itself read and counted ("sources.csv 38 rows"). The mine's sentence is self-refuting: a document "cited by S0102's row only" *is* S0102's row. No duplicate document row was minted (§13 forbids re-defining a source id, and minting one would have manufactured a fresh collision of exactly the class being repaired) | **corrected; see COR-305** |
| A6-08 / RD-097: "the search body is not in the repo" / "OUTSIDE the repository" for the HathiTrust lead | **WRONG.** The 34,171 B body is at `00_universe/harvest/_probe_fixed_20260925/hathitrust/640238bfc6cb7376-r20260925T131232Z.html`; the facet re-reads from it (term `"Wal-Mart" Bentonville`, `lmt=ft`, Date of Publication 1960-1969 → **All Items 45 / Full View 4**). The lead stays UNTRIED at text level; the correction makes it cheaper to chase, it does not close it | **corrected; `S0155` now points at the byte** |
| "six quantitative rows from the FY1974 five-year table and the FY1973 55 + 9 pair" (= 8 implied) | the block holds **6** quantitative rows: four legs of the FY1974 table (FY1970/FY1971/FY1972/FY1973 = 64) plus the two FY1973-report values. A6's own header line says "Five come from one table and one from the FY1973 report", which is also wrong | **both phrasings loose; the parsed truth is 4 + 2** |

## 2. Requested vs applied, per register — before and after

| Register | A6 requested | Applied at the merge (tagged) | Already carried by content | **This pass: minted** | **This pass: folded (row amended)** | After, rows |
|---|---|---|---|---|---|---|
| `sources.csv` | 9 | 0 | 0 | 8 (`S0148`–`S0155`) | 1 (its S0147 → live `S0145`) | 47 → **55** |
| `quantitative.csv` | 6 | 0 | 2 (FY1970 = 32; FY1972 = 51 in the composite) | 4 (FY1971 = 38; FY1973 = 64; FY1973 = 55; FY1973 = 9) | 2 (the two above, carriers extended in `notes`) | 114 → **118** |
| `timeline.csv` | 4 | 0 | 0 | 4 (1970-10; 1973; 1974; 1946-1947) | 0 | 59 → **63** |
| `conflicts.csv` | 3 | 0 | 1 (U-A6/1 **is** U.011, which already names A4's Kentucky prose) | 0 | 3 (→ **U.011**, **U.040**, **U.045**) | 39 → **39** |
| **total** | **22** | **0 tagged** | — | **16** | **6** | root 333 → **349** |

`data_gaps.csv` (52), `decisions.csv` (9), `failures.csv` (13), `validation.csv` (0), `channels.csv` (0) were not
touched: A6 requested no rows in them. **22 = 16 + 6 + 0 dropped.** The merge's own account
("`_MANIFEST.md`: 99 rows requested … 95 applied … Nothing dropped") is superseded, not erased: the requested
total for the merge was **121**.

## 3. `tools/merge_census.py` cannot see the emission — quoted, twice

Before and after this pass, unchanged:

```
# Merge census -- company_002_walmart

2 structured block(s) parsed; 0 block-group(s) could not be attributed (listed, never counted as zero).

| register | requested | present | missing | unkeyed | first missing keys |
|---|---|---|---|---|---|
| sources.csv | 4 | 4 | 0 | 0 |  |
| timeline.csv | 11 | 0 | 0 | 11 |  |

TOTAL missing keyed rows: 0        (exit 0)
```

**It cannot see the A6 emission, and that is a finding.** Three separate blindnesses, all measured:
1. **Directory scope.** `census()` globs `company_dir/_parts/*.md` only (line 94). `research/` is out of scope by
   construction, so all 4 of A6's blocks — 22 rows — are invisible. RD-122's dispatch rule ("over the whole company
   directory, parts *and* `research/`") is not implemented.
2. **Mark window.** A block is credited only when the `>>> … MERGE … <<<` mark appears in the **preceding 1,200
   characters**, so in a multi-block emission only the first block counts. Re-running the tool's own fence regex over
   the whole directory credits 15 rows (p2 5, p3 12, A6's first block 9 by my manual parse) where the merge actually
   processed ~99 and A6 alone requested 22.
3. **Keyless registers.** Of the 15 rows it does credit, 11 are `unkeyed` — censused by count, never by content — so
   `missing = 0` for `timeline.csv` carries no information about whether any timeline row landed.

A tool that returns exit 0 on a corpus where 22 requested rows went unapplied is a detector reporting success
(RD-124's class). `tools/` is outside this pass's write set, so the defect is reported, not fixed; the manual
substitute used here is `grep -rc "REGISTER ROWS FOR MERGE" _parts/*.md research/*.md` plus a per-block csv parse,
and that command line is recorded in `_MANIFEST.md` defect item 8.

## 4. The minted ids and the alias map

Minting is the merge's, and this pass merged; new ids start **after** the live maximum (`S0147`), and the mine's
numbers survive only as `notes` aliases so `research/A6_held_corpus_mine.md`'s citations resolve.

| A6 proposed | New global id | Content A6 meant | What the live occupant of that number actually is |
|---|---|---|---|
| S0139 | **S0148** | IA catalogue-print null FY1962–FY1971, `title:` route, numFound 0 | SEC "Securities Traded on Exchanges as of December 31 1970" |
| S0140 | **S0149** | IA printed-report run 1970–1998, numFound 27 | SEC *Statistical bulletin* November 1970 |
| S0141 | **S0150** | IA metadata manifest of the FY1972 item — the page-image routes | the company's curated history page (U.048's collision) |
| S0142 | **S0151** | FY1972 text layer, second physical copy, 23,989 B | Walmart Museum "First Walmart Advertisement" lead |
| S0143 | **S0152** | four IA `text:` queries, walton / Walton's / five-and-dime / $1.25 store 1945–1965 | PBS 2004 timeline |
| S0144 | **S0153** | the hyphen-artefact trap (1962 / Discount City zeros vs the 6,734 control) | SCDigest 2012 retrospective |
| S0145 | **S0154** | Chronicling America 403 Cloudflare challenge bodies | **the EDGAR floor** — the pair RD-123 named |
| S0146 | **S0155** | HathiTrust 1960–1969 facet, 45 / 4 full view, UNTRIED | `STUB_LEAD_*` files |
| S0147 | **folded into live S0145** | EDGAR `formerNames` + the three NoSuchKey probes + the tickers artefact | HathiTrust route-state record |

Each of the nine live rows `S0139`–`S0147` carries an **ID-COLLISION REDIRECT** in its `notes` cell naming what A6
meant by that number and where A6's content is now issued; each new row carries the **A6-ALIAS** running the other
way. The dossier's historical text is untouched (§14 rule 4 supersedes; rule 12 addresses a claim by a stable label,
which is what the alias now is). The mine's proposed **S0148-for-the-FY1973-report is void** and says so in three
places (`S0102`'s notes, the FY1973 rows, `stage_1.md`).

## 5. What was refused, and why (§14 rule 8: nothing lands that was not re-read)

| A6 request | Applied? | Reason, with the re-read |
|---|---|---|
| A **new `sources.csv` row for the FY1973 report** | **Refused — the premise is false** | `S0102` is that row (COR-305). §13: ids are never re-defined |
| A **new `sources.csv` row for EDGAR `formerNames`/probes** (its S0147) | **Refused as a duplicate — folded into live `S0145`** | same accession family; the fold applies the content (`formerNames` = exactly two names, earliest 1994-02-14; `probe_SEC_tickers.json` one 2005 STRATS trust, `walton` 0; the three `probe_EDGAR_*` are NoSuchKey = a route never correctly tried) |
| FY1970 = 32 and FY1972 = 51 as **new rows** | **Refused — folded into the existing rows' `notes`** | both values are already on the register; a second row for one metric-date manufactures a second witness inside a single lineage (§3) |
| **High** confidence on FY1973 = 64, as the dossier argued it | **Refused on its reasoning** | the 55 + 9 = 64 foot is one lineage cross-footing itself, and the value's year came from a table column position |
| **High** on the FY1974 two-sold/four-closed timeline row | **Refused — landed Medium** | the footnote names no year; the tie is the asterisk on the 78 column |
| The three conflict rows as **new rows** | **Refused — folded into U.011 / U.040 / U.045** | each question already has a canonical carrier; minting a second would re-define a conflict, the COR-304 class |
| A6's **two prose corrections to `A4_independent_periodicals.md`** (lines 278, 735) | **Not applied — out of write set** | another agent owns A4; the hand-off is recorded inside U.011 and stays open |
| Any **HathiTrust item text** (A6's U3, "the single best remaining chance") | **UNTRIED, unchanged** | no item opened; the viewer 403s a script and this pass spent zero web calls. `S0155` is a lead with a carrier, not evidence |
| The five-year table's column pairing, as a **settled** fact | **UNTRIED for FY1970/FY1971/FY1972** | page image unread; `S0150` enumerates what would settle it — a FETCH REQUEST, not a finding |

### The one value gain: Note 8, found by re-reading rather than by trusting the recap page

`WALMART_AR_1974.txt`, **Note 8 — Number of stores in operation** (lines 1595-1599, in the notes to the audited
statements): *"The 78 stores at January 31, 1974 consisted of 76 Wal-Mart Stores and 2 Family Center Stores whereas
the 64 stores at January 31, 1973 consisted of 55 Wal-Mart Stores and 9 Ben Franklin Variety and Family Center
Stores."* The dossier never cited it. It prints value **beside date**, which is the thing the header-pairing caveat
denied the table:

* FY1973 = 64, FY1973 = 55, FY1973 = 9 → **High**, on Note 8 (`S0103`) with `S0102`'s own sentence as the second
  printing — the promotion is written into each cell, into COR-306, into `_MANIFEST.md` and into `stage_1_index.md`,
  not slipped past the gate.
* FY1970 / FY1971 / FY1972 → **Medium**, caveat attached: Note 8 proves the table is *not* shifted at its two
  checkable columns (and FY1975's Note 8 repeats FY1974's composition), which is an inference about the table, not a
  printed date beside 38, and an inference inside one lineage cannot lift a ceiling.
* FY1974 "two sold and four closed" → held **Medium**: Note 8's FY1974 composition leaves zero Ben Franklin variety
  stores standing and the same report prints "During 1974 the Company opened 20 stores and closed 6 stores" — 2 + 4 =
  6, an internal foot shown, not assumed, but still not a date in the footnote's own sentence.

## 6. Corrections opened, and every place each one reaches

| Id | What it withdraws | Reaches (register rows) | Reaches (volume / instruction layer) |
|---|---|---|---|
| **COR-303** | the merge's "99 rows requested … Nothing dropped" and RD-115's use of it as proof of completeness | census sentence in the `notes` of `S0145`, `S0147`, `S0102`, `S0148`–`S0155`; the 4 new `quantitative.csv` rows; the 4 new `timeline.csv` rows; `conflicts.csv` U.011 / U.040 / U.045 fold notes | `stage_1.md` front-matter disposition paragraph; `stage_1_index.md` (label note + register counts); `_MANIFEST.md` (proof table supersede + addendum, defect items 7–8) |
| **COR-304** | the resolving power of the mine's `S0139`–`S0147` citations | ID-COLLISION REDIRECT on each of the 9 live rows; A6-ALIAS on each of the 8 new rows; U.040's fold note | `stage_1.md` front matter **and** a pointer line at §T.3 R-1 / the **U.048** entry (the volume's own earlier collision record); `stage_1_index.md`; `_MANIFEST.md` per-register addendum |
| **COR-305** | "the FY1973 report has no `sources.csv` row of its own … still live"; "the search body is not in the repo"; "the four renderings on offer" | `S0102` (premise correction), `S0155` (carrier corrected), `S0150` (20 files, five requestable routes); the three FY1973 `quantitative.csv` rows; the 1973 `timeline.csv` row | `stage_1.md` front matter; `stage_1_index.md` ("its proposed S0148 … is void"); `_MANIFEST.md` defect item 9(a)/(c) |
| **COR-306** | "51 (FY1971)" inside **U.040** CLAIM B, and every uniform confidence claim about the five-year series | U.040 (superseded parenthetical kept visible); FY1970 / FY1971 / FY1972 / FY1973 = 64 / 55 / 9 rows; the 1973 and 1974 `timeline.csv` rows | `stage_1.md` front matter (including the Note 8 promotion); `stage_1_index.md` confidence note; `_MANIFEST.md` quantitative/timeline rows and defect item 9(b) |

Propagation was **mechanically confirmed, not asserted**: `gates.py`'s corrections gate reports
`6 retraction ids; register layer reaches 6, volumes 6` / `all 6 retraction(s) reach registers and volumes`.
`CORRECTIONS.md`'s own propagation tables list every surface. Nothing was erased: the merge's arithmetic, U.040's
wrong parenthetical, the mine's High proposals and `_parts/`' wording all stay visible beside their corrections.

## 7. Gate output, verbatim (the command in the brief)

```
$ python tools/gates.py --company-dir "founders_playbook/01_companies/company_002_walmart" \
    --checks csv,keys,anchors,corrections --tier exemplar --fail-on substantive
# Mechanical gate report -- company_002_walmart

Findings: **0** | Passes: 20

- coverage 9 registers, 3 stage volumes, 24 source documents
- anchors  stage_1.md declares an explicit ANCHORS set (80 ids)
- anchors  stage_1.md declares 80 anchors
- anchors  stage_1_part_2.md declares 21 anchors
- anchors  32 id(s) read as backticked references or range endpoints, not citations (U.0, U.001, U.002, U.010, U.011, U.012, U.025, U.027)
- corrections 6 retraction ids; register layer reaches 6, volumes 6

## Passing checks

csv      timeline.csv                       63 rows x 11 cols
csv      timeline.csv.source_id             all S#### tokens resolve
csv      quantitative.csv                   118 rows x 12 cols
csv      conflicts.csv                      39 rows x 15 cols
csv      sources.csv                        55 rows x 18 cols
csv      data_gaps.csv                      52 rows x 8 cols
csv      validation.csv                     0 rows x 11 cols
csv      validation.csv.source_id           all S#### tokens resolve
csv      failures.csv                       13 rows x 11 cols
csv      failures.csv.source_id             all S#### tokens resolve
csv      decisions.csv                      9 rows x 15 cols
csv      decisions.csv.source_id            all S#### tokens resolve
csv      channels.csv                       0 rows x 11 cols
csv      channels.csv.source_id             all S#### tokens resolve
keys     stage_1.md                         41 source tokens all resolve
keys     stage_1_index.md                   7 source tokens all resolve
keys     stage_1_part_2.md                  4 source tokens all resolve
anchors  citation resolution                every register-cited anchor resolves (85 distinct ids across registers and volumes)
anchors  parity                             80 narrative anchors <-> 80 register anchors
corrections propagation                      all 6 retraction(s) reach registers and volumes
```
Exit 0. **No check reported DID NOT RUN** (the corrections gate found `CORRECTIONS.md`; every one of the nine
registers was parsed; three stage volumes were read). Baseline before this pass on the same four checks:
0 findings / **19** passes — the +1 is `keys stage_1_index.md`, which had no resolvable source tokens until this
pass put them there. Anchor parity is unchanged at 80 ↔ 80: no new `U.nnn` anchor was minted, because no new
conflict row was minted.

## 8. Coverage note — what this pass did NOT examine, and what is owed to the certifier

1. **A citation in the volume that the held byte contradicts (not repaired: narrative prose is outside this write
   set).** `stage_1.md` §U.104 says the FY1970/FY1971 reports are "proven absent from IA by `ia_q_92a4542e.json`,
   numFound 0". That file's single response block prints `title:("walmart")` → **numFound 6,734** (it is `S0153`'s
   hyphen-free control). The IA-holdings null itself survives on a different query (`S0148`), but §U.104 names the
   wrong byte. Referred.
2. **`merge_census.py` is still blind** (§3): re-running it after the repair returns the same "0 missing". A fix
   must add `research/` to the glob, drop the 1,200-character mark window, and report keyless registers as
   UNANSWERED rather than `missing 0`. Until then no company's "census clean" means anything, and every merge brief
   for the remaining 40 companies needs the manual grep.
3. **RD-123's own text needs the three corrections in §1 applied by the log's owner** — the "64 occur nowhere with
   `stores`" measurement, the "FY1973 has no row of its own, defect still live" claim, and RD-097's "the search body
   is not in the repo". Also owed: RD-115's "zero rows added or removed" is fine for its own pass, but its acceptance
   of "99 … Nothing dropped" as the completeness proof is what COR-303 supersedes. `MASTER_RESEARCH_LOG.md` and
   `03_quality_control/walmart_s1_merge.md` are not mine to edit.
4. **`_MANIFEST.md`'s two empty registers** (`validation.csv`, `channels.csv`) still have no drafted body; that
   follow-up is unrelated to A6 and remains open.
5. **A6's own internal tension, unresolved and out of scope here:** its §Holdings census says the retro-recap genre
   is "present in FY1973–FY1980, absent from FY1972" while A6-11 says the recap "begins with the FY1974 report". The
   FY1973 body does print "twenty-eight year history" (line 187) — which is the volume's stated earliest attestation
   of the 1945 start — so the second form overstates. No row landed by this pass depends on either reading.
6. **Still UNTRIED after this pass, and unchanged:** Chronicling America's 17 newspaper tasks (all 403, `S0154`);
   the page images of FY1972–FY1979 (`S0150` names the files); HathiTrust's 45 1960–1969 items (`S0155`); Google
   Books (429, `quota_limit_value: 0`); `chain-store-age-steel-for-stores` (1963-04-01, 0 B retrieved); the NLRB
   volumes. The pre-1972 naming perimeter is exactly where RD-097 left it: no held byte carries a printed date before
   **1972-03-22** that names the company, and that is a perimeter over four families, not a wall.

## 9. Read-back verification (path and record count as actually on disk, §14 rule 5)

Each file was re-parsed after writing; the numbers below are read back from the bytes, not from this report.

| Path | On disk | Read-back proof |
|---|---|---|
| `founders_playbook/01_companies/company_002_walmart/sources.csv` | 55 data rows × 18 cols, ids `S0101`–`S0155` contiguous | csv-parsed; `S0148`–`S0155` present and each `notes` cell contains `A6-ALIAS`; `S0139`–`S0147` each contain `ID-COLLISION REDIRECT` |
| `…/company_002_walmart/quantitative.csv` | 118 × 12 | 4 rows contain `COR-303` as new fleet records (FY1971 38 / FY1973 64 / 55 / 9); FY1970 and FY1972 rows contain the carrier-extension note |
| `…/company_002_walmart/timeline.csv` | 63 × 11 | 4 rows contain `COR-303` (1970-10, 1973, 1974, 1946-1947); the 1946-1947 row's `conflict_ref` resolves to **U.045** |
| `…/company_002_walmart/conflicts.csv` | 39 × 15, no row added or removed | U.011 / U.040 / U.045 each carry the A6 fold note; U.040 CLAIM B carries the superseded parenthetical |
| `…/company_002_walmart/CORRECTIONS.md` | 3,883 words / 25,538 bytes | six ids issued (`COR-301`…`COR-306`), each in the summary table, its own section, and a propagation table |
| `…/company_002_walmart/stage_1.md` | 59,516 words / 388,823 bytes — **484 words of headroom under the 60,000 cap** | two insertions only: the front-matter disposition paragraph and the §T.3 R-1 / U.048 pointer |
| `…/company_002_walmart/stage_1_index.md` | 890 words / 6,047 bytes | register counts re-pointed; the confidence note now matches the cells |
| `…/company_002_walmart/_MANIFEST.md` | 349 root register rows recorded (was 333) | per-file word/byte counts re-measured against the bytes; defect items 7–9 added; proof table superseded in place |
| `founders_playbook/03_quality_control/walmart_s1_a6_census.md` | this file | written last; the only new file created by this pass |

`data_gaps.csv` (52), `decisions.csv` (9), `failures.csv` (13), `validation.csv` (0), `channels.csv` (0), `_parts/`,
`research/`, every other company directory and `tools/` are byte-unchanged by this pass. Claims were taken before
writing on all nine paths (`scaffold.py claim --agent walmart-a6-census`) and released `--done` after the read-back.

