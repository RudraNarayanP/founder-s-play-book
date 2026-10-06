# Tesla Stage 1 — merge notes

Agent `tesla-s1-merge`, 2026-09-30. Stage-1 MERGE pass for `company_043_tesla`. Web budget **0 calls; 0 made**
— every unreached object is named as a `FETCH REQUEST:` below rather than fetched. All figures in these notes
were re-measured from disk after the last write.

## 1. What landed

| deliverable | state |
|---|---|
| `stage_1.md` | **53,553 words / 370,566 B, ONE volume**, 34 `##` sections; under §9.2's 60,000-word hard cap so **no §9.3 split and no second volume**; above the 40,000 soft target (amber, legal) and 6.7× the T3 density target (accepted state, §4) |
| nine registers | **208 rows** at the company root (`_MANIFEST.md` has the per-register table) |
| `stage_1_index.md`, `_MANIFEST.md`, `CORRECTIONS.md` | written by this pass (Tesla had none) |
| `_parts/s1_p1.md`, `_parts/s1_p2.md` | **untouched except two appended `SUPERSEDED 2026-09-30 … DO NOT RE-APPLY` notices**; both part bodies remain **byte-identical contiguous slices** of `stage_1.md` (Volume 1 at offset 9,746; Volume 2 at offset 102,736) |

## 2. Starting measurement — the census, run before anything was written

`python tools/merge_census.py --company-dir founders_playbook/01_companies/company_043_tesla --verbose`

14 structured blocks parsed; **2 block-groups unattributable — exactly 20 rows**, `UNATTRIBUTED s1_p2.md (9
rows): AMBIGUOUS:validation.csv,failures.csv` and `(11 rows)` likewise. Requested by the tool: sources 28,
quantitative 61, timeline 47, conflicts 16, data_gaps 16, decisions 9, channels 10, `TOTAL missing keyed rows:
44`.

**The census under-requested by 25 rows and by one whole emission.** It globs `_parts/*.md` only (RD-127 defect
1), so the probe's `research/{sources,conflicts,data_gaps}.csv` — **S0001–S0012, U.1–U.6, 7 gap rows = 25
rows** — was invisible to it. Both parts *presuppose* those rows (part 1's §Header: "The probe's registers at
`research/` hold `S0001`–`S0012` and conflicts `U.1`–`U.6`"; part 2's §U-pre declares `U.1–U.6` as **the live
register**), and Tesla had **no** root register file, so applying only the 207 the parts emitted would have left
the six anchor rows, the CourtListener row and the whole independence null unregistered. This is RD-122 (Target)
and RD-131 (Microsoft) for the third time. True requested total: **232 rows**.

**The 20 ambiguous rows, attributed by content.** Both blocks copy the reference 11-column header verbatim, so
`match_register()` can never separate them (RD-132's unfixed tool defect; Tesla is the 20-row instance RD-132
names). Attribution evidence, strongest first:

1. **Content.** Block A (9 rows) = first revenue, first delivery, Model S reservation demand, the Daimler
   powertrain line, the capacity push, first positive gross margin, DOE draw, institutional distribution, the
   executed offering — all *what it demonstrated* cells are validation claims. Block B (11 rows) = FY2008 gross
   loss, Q4 2008 layoffs, 2007 cancellations, the repriced notes, the recall, the EPA settlement, the filed
   FY2009 understatement, the significant deficiency, the missing cash-receipt data, the deepening equity
   deficit, the unsupported near-collapse memory — all failures.
2. **Part 2's own arithmetic**, twice and consistent: the emission instruction list and the close-out census
   both print `validation 9 · failures 11`, and the blocks come back 9 and 11.
3. **Order**: validation precedes failures, as in the reference schema list (§13) and in the close-out tally.

Block A → `validation.csv` (9), block B → `failures.csv` (11). **No row dropped, none refused**, and the
reasoning is printed inside both registers as a `MERGE[…]` tag so a cold reader finds it in the data.

## 3. Duplicate-key check — run across BOTH parts and the probe emission in ONE operation

* **0 duplicate provisional `source_id` keys** across the 40 (P1S01–12, P2S01–16, probe S0001–12).
* **0 duplicate `conflict_id` keys** across the 22.
* **Same-accession collisions surfaced and adjudicated by document, not by accession**: part 1's S-1 primary
  document vs the exhibits inside accession `0001193125-10-017054`; part 2's DOE exhibit vs the primary document
  of `-129878`; part 1's S-1/A printing vs the CORRESP letter inside `-099603`. Different documents → different
  rows (§9.4). Same *document* registered twice → folded.
* **Keyless registers** were tested by content instead: timeline → 1 same-date/same-event duplicate;
  quantitative → 0 (the same-date/same-metric/same-value test found none; the two FY2009 rows are two carriers
  of one figure and are cross-tagged by `U.17`); data_gaps → 8 semantic duplicates found by reading (an
  automated token-overlap test found none, which is why the folds are listed by row below rather than claimed
  as machine-detected).

## 4. Row application — 232 requested → 208 applied, 25 aliased into 16 collision groups, 0 refused

| register | requested (p1 + p2 + probe) | applied | folds |
|---|---|---|---|
| `sources.csv` | 40 (12 + 16 + 12) | **24** | 16 aliased into 8 groups |
| `quantitative.csv` | 61 (22 + 39) | **61** | none |
| `timeline.csv` | 47 (26 + 21) | **46** | 1 (2010-06-29 closing edge) |
| `conflicts.csv` | 22 (3 + 13 + 6) | **23** | none — one row **minted** (`U.23`) |
| `data_gaps.csv` | 23 (6 + 10 + 7) | **15** | 8 aliased into 7 groups |
| `decisions.csv` | 9 (0 + 9) | **9** | none |
| `validation.csv` | 9 (0 + 9) | **9** | ambiguous-census block, attributed |
| `failures.csv` | 11 (0 + 11) | **11** | ambiguous-census block, attributed |
| `channels.csv` | 10 (0 + 10) | **10** | none |

Sources fold groups (kept row ← aliased rows): `S4369` ← P1S01 + **P1S10, P1S12, probe S0002** · `S4371` ← P1S03
+ **probe S0003** · `S4372` ← P1S04 + **P2S01, probe S0001** · `S4375` ← P1S07 + **P2S14, probe S0004** ·
`S4376` ← P1S08 + **probe S0005** · `S4377` ← P1S09 + **P2S13, P2S15, probe S0006** · `S4389` ← P2S12 + **probe
S0009, S0010** · `S4390` ← P2S16 + **probe S0007, S0008**.
Gap fold groups: p2 G1 ← p1 G1 + probe G3 · p2 G3 ← p1 G3 · p2 G7 ← probe G7 · p2 G10 ← probe G5 · p1 G2 ← probe
G4 · p1 G4 ← probe G1 · p1 G5 ← probe G2. Probe G6 (documentary/auction **UNTRIED**) kept as its own row.

**Non-destruction is proved from the register layer alone,** not asserted: all 40 provisional source keys and
all 16 provisional conflict keys print in `sources.csv`/`conflicts.csv` — either as the row they became or inside
a printed `MERGE[…]` alias — verified by re-scan after the final write. Folds preserve the aliased row's own
`relevant_passage` and `notes` (gaps: `gap`, `why_missing`, `best_available_evidence`, `follow_up_task`) verbatim.

**Tier.** T3 register (probe `research/A_chronology_feasibility.md`; **`research/A3_intake_regrade.md` re-issues
T3 unchanged** — family (a) grew 10× in bytes but no family joined, so §15.2's count is unmoved. **No later file
regrades it**, and the regrade explicitly withdraws the PROVISIONAL condition that applies to Costco). §K, §N and
§U are mandatory at T3 and all three are on disk. The 8k figure is a dispatch budget: RD-122's ruling, §9.6's ban
on trimming evidence to fit a limit, §15.4's "missed length targets are legitimate". Nothing was cut; the volume
is 53,553 words against a 60,000 hard cap, so it is legal geometry and an over-budget dispatch.

## 5. Minted id block and provisional → minted binding

`python tools/id_mint.py --count 24 --company company_043_tesla --claim --agent tesla-s1-merge` → **`S4369 …
S4392`**, allocated above the highest live id (next assignable `S4369`; the 37 registry ids never written into a
`sources.csv` were not re-entered). Registered in `00_universe/_ID_BLOCKS.tsv`.
`--audit` on this corpus also reports a **pre-existing collision it was not told about**: `S4222–S4225` are
cited by both `company_011_microsoft` and `company_042_target` — not this pass's defect, handed on.

| minted | kept from | also absorbs (dossier-local aliases) |
|---|---|---|
| S4369 | P1S01 (S-1 ds1.htm, 0001193125-10-017054) | P1S10, P1S12, probe S0002 |
| S4370 | P1S02 (S-1/A No. 1, -068933) | — |
| S4371 | P1S03 (acc -099603; ordinal corrected by COR-02) | probe S0003 |
| S4372 | P1S04 (424B4, -149105) | P2S01, probe S0001 |
| S4373 | P1S05 (ex 10.23 Lotus + ex 10.22 Stanford lease) | — |
| S4374 | P1S06 (XBRL `xbrl_early_series.csv`, 336 rows) | — |
| S4375 | P1S07 (FY2010 10-K) | P2S14, probe S0004 |
| S4376 | P1S08 (2011 DEF 14A) | probe S0005 |
| S4377 | P1S09 (EDGAR submissions index) | P2S13, P2S15, probe S0006 |
| S4378 | P1S11 (searched-and-null over 76 held documents) | — |
| S4379 | P2S02 (S-1/A No. 3 + dex1037 DOE + dex1041) | — |
| S4380 | P2S03 (dex231 PwC consent, Amendment No. 4) | — |
| S4381 | P2S04 (S-1/A No. 5, first FY2009 error printing) | — |
| S4382 | P2S05 (CORRESP filename13.htm, 2010-04-29) | — |
| S4383 | P2S06 (CORRESP filename1.htm, 2010-06-08 error analysis) | — |
| S4384 | P2S07 (acceleration + distribution letters) | — |
| S4385 | P2S08 (selling-stockholder letter) | — |
| S4386 | P2S09 (three UPLOAD staff PDFs, bytes corrupted at intake) | — |
| S4387 | P2S10 (Taiway / Polytec Holden / Chroma ATE agreements) | — |
| S4388 | P2S11 (Hull lease, subsidiaries, IRA, ESPP, warrant) | — |
| S4389 | P2S12 (harvest response bodies) | probe S0009, S0010 |
| S4390 | P2S16 (Wayback CDX rows + 504/offline negatives) | probe S0007, S0008 |
| S4391 | probe S0011 (CourtListener v4 federal registry) | — |
| S4392 | probe S0012 (no carrier held for the dispute's own documents) | — |

Narrative prose in both volume slices keeps `P1Sxx`/`P2Sxx`/`P1U-xx`/`P2U-xx` as protected history (RD-122
precedent); every register citation cell was re-pointed to the minted key, 0 unresolved `S####` in a
`source_id` column. **`S####` inside quoted OCR text is print, not a pointer** (RD-131): the gate flagged
`S435`, `S0001`, `S0012` as protected-history mentions in this volume and none was re-pointed or minted.
Conflicts re-keyed exactly as both parts instructed: `P1U-07/08/09` → `U.7/U.8/U.9`; `P2U-10…22` → `U.10…U.22`;
probe `U.1–U.6` unchanged; `U.23` minted at merge. `stage` column: all 208 rows carry the string `stage1`; the
probe's 25 emission rows carried `tesla` in `company` and were normalised on touch to `Tesla Motors Inc`.

## 6. §U anchors ↔ conflicts parity, proved

`<!-- ANCHORS: U.1-U.23 -->` is declared **in the merge header**, ahead of both slices, so the volume declares
23 anchors while part 2's own `U.1-U.6` line survives verbatim inside Volume 2 (the gate reads the first
declaration; part 2's §U-pre demanded exactly this widening). `conflicts.csv` holds `U.1 … U.23`, one row each.
Mechanical checks after the final write: declared set = 23, register token set = 23, **undeclared = 0, uncovered
= 0, duplicate conflict_ids = 0**; `gates.py` reports `anchors | parity | 23 narrative anchors <-> 23 register
anchors` and `anchors | citation resolution | every register-cited anchor resolves (23 distinct ids)`.

**The post-write census re-run still prints `missing` for the 44 keyed rows.** That is a **key-form mismatch, not
unapplied work**: the census compares the provisional keys printed in `_parts/*` (`P1S01`, `P1U-07`) against the
register's key column, which now holds minted keys, and it cannot see the third emission at all. The parity proof
this pass relies on is the gate result above plus the register-layer alias re-scan in §4, both re-run after the
last write. Reported, not worked around: the census's "missing" column is meaningless after a mint, which is the
same blindness RD-127 measured from the other side.

## 7. Contradictions kept visible (and the one thing this merge minted)

`U.23` — part 2's quantitative note claims its $26.0m refundable reservation liability "SUPERSEDES the 2009-09-30
$24.8m figure part 1 carried", while part 2's own channels and decision rows print $26.0m at **2009-12-31**, a
period-end neither emission registered a carrier for. Supersession across two different dates is not a
correction: $24.8m @ 2009-09-30 and $26.0m @ 2010-03-31 both stand, **$2009-12-31 is UNKNOWN**, and the
"liability held flat across the deposit-policy inversion" reading is not carried as a finding. Both figures are
the same registrant inside one lineage, so no third voice could settle it and the web budget was 0. See
`CORRECTIONS.md` COR-01.

`COR-02` (ordinal, adjudicated in `U.19`) · `COR-03` (EDGAR row-count wording, probe only) · `COR-04`
contemporaneous-instrument count, adjudicated in `U.18`) · `COR-05` (FY2009 audited statements enter the lineage
at Amendment No. 1) · `COR-06` (held-corpus denominator, measured: **83 documents / 32 accessions /
59,881,144 B** in `sources/sec/`; `_MANIFEST.csv` carries 76 rows / 25 accessions and omits the 3 corrupted
UPLOAD PDFs and the 4 CORRESP letters — reconciling part 1's 76/24, the regrade's 76/28 and part 2's 85/33).
All six reach both layers: `gates.py` → `corrections | propagation | all 6 retraction(s) reach registers and
volumes`.

## 8. Gate run (mandated command; note that `--out` is a **directory** to this tool)

`python tools/gates.py --company-dir founders_playbook/01_companies/company_043_tesla --tier register --out
founders_playbook/03_quality_control/tesla_s1_gates.md` → final state **Findings: 2 | Passes: 20**, written to
`03_quality_control/tesla_s1_gates.md/gates_company_043_tesla.md` (+ `.json`). **`gates.py` was edited by a
concurrent pass at 00:45 on 2026-09-30, between this pass's two runs**: the first run printed
`budget | stage_1.md | 53553 words > register cap 8000 (split required)` as a hard finding; the tool now separates
the two cases exactly as RD-122 demanded — only `> HARD_CAP` is a defect, and a tier cap overage is an advisory
that says "NOT a split mandate and NOT a defect". Both runs are reported here because the instruction layer must
not carry a stale claim about the instrument (§14 rule 10).

| finding | one-line adjudication |
|---|---|
| `advisory \| stage_1.md \| 53553 words over the register density target 8000` | The expected T3 overage: a dense dispatch against a T3 cap (RD-122). **Not a mandate to delete evidence** — §9.6, §15.4. Recorded as the known accepted state; nothing trimmed, no re-tier, no second volume (53,553 < the 60,000 hard cap) |
| `quotes \| ADVISORY \| 16 of 58 checked spans unmatched (28%)` | The tool labels this ADVISORY and "NOT defects" (§15.6). Tesla's intake is filings-only: the unmatched spans are (i) quotations from the probe's hand-fetched documents and secondary print never saved under `sources/`, (ii) spans the probe recorded as `NO_VERBATIM_PASSAGE_RECORDED`, and (iii) OCR/markup-split runs — RD-131's own example is in this corpus: "incorporated … on July 1, 2003" returns 0 hits in raw HTML because markup splits the run, while "formed in July 2003" = 1. No quotation was rewritten and no source row was minted for a phrase |

Passing: 9 × `csv` width checks (0 drift; widths 18/12/11/15/8/15/11/11/11), `stage` vocabulary, year-bearing date
columns, `source_id` resolution in all six registers that carry the column, `keys` (8 tokens resolve in the volume;
`S435`, `S0001`, `S0012` protected as print/history; `S4222`/`S4225` protected in the index), `anchors`
(citation resolution 23 distinct ids + parity 23 ↔ 23), `corrections` propagation 6/6. Two tool quirks reported,
not worked around: `coverage` counts **2 stage volumes** because `stage_docs()` globs `stage_*.md` and so swallows
`stage_1_index.md` (an index, not a volume — the mandated filename is the cause); and it reports **81 source
documents** against 83 measured in `sources/sec/` (the COR-06 counting question, nothing depends on it).

## 9. Residue NOT applied, and why

1. Probe claim records **F01–F12** — dossier prose, not register rows; never requested by the census; cited by
   label where Volume 1 extends or corrects one.
2. Probe rows **S0001–S0010** — folded as documented in §5 (their passages/notes survive inside the kept rows);
   only the two rows no part registered (`S4391`, `S4392`) were applied as rows.
3. Part 1's `P1S10`, `P1S12` and part 2's `P2S01`, `P2S13`, `P2S14`, `P2S15` — re-registrations of documents
   already on the register; folded per §9.4 ("never re-define a source id").
4. Part 1's **`## Untried` block is not on disk** — `_parts/s1_p1.md` ends at a stray `#` right after its
   `data_gaps` block while citing "## Untried NEW-1/2/3/4" four times (RD-132's Nvidia class). The *routes*
   survive inside part 2's list; **part 1's wording of them is unrecoverable and was not invented**. Reported in
   the volume's merge note and in the appended SUPERSEDED notice.
5. `research/_harvest_queries_tesla*.json`, `research/_write_registers_tesla.py`, `research/A_*.md`,
   `sources/`, `_parts/` bodies — read-only inputs; untouched except the two notices.
6. Nothing refused: the 20 ambiguous rows, the probe's 25 rows and both parts' 207 rows are all accounted for as
   applied, folded (with text preserved) or reported residue.

## 10. `FETCH REQUEST:` blocks (0 web calls made by this pass; refusing the fetch is the behaviour §15.1 requires)

* **FR-1 — `sec_intake.py grab` accession `0001193125-10-149105` and `-017054`, full exhibit folder** (no
  `--file` form is broken: it invents `index-headers.txt` and 404s; enumerate then pass `--file` per item).
  Wanted: certificate of incorporation / restated charter (the **only non-corporate-lineage carrier of the
  2003-07-01 date**, N7), Series A and B **stock purchase agreements** (first-financing closings — the empty
  `data_gaps` High rows), the 2003 Equity Incentive Plan document, and the **424B4 balance-sheet column heads**
  that settle `U.23`/COR-01 from bytes already on this disk.
* **FR-2 — binary re-fetch of the three SEC-staff UPLOAD PDFs**: `0000000000-10-010920`, `-10-019954`,
  `-10-027152`, `filename1.pdf`, expected sizes **125,766 / 47,907 / 39,093 B**, sha1-checked against the sidecar
  before any text is cited. Held bytes are text-mode-corrupted (23,268 / 13,489 / 10,637 U+FFFD; 0 text from two
  extractors; no image objects, so **OCR will not help**). Until then `S4386` is UNANSWERED, not empty.
* **FR-3 — Wayback domain-scoped CDX** `https://web.archive.org/cdx/search/cdx?url=tesla.com&matchType=domain&from=2003&to=2009&fl=timestamp,original,statuscode`
  → then one raw `id_` snapshot of the **August 2009 joint statement** page. Bytes → `sources/wayback/`. This is
  the highest-value unwritten object in the company (probe §Untried U-1). The CDX rows behind `U.4`/`S4390` are
  **transcribed, not re-fetched**, so that conflict currently rests on a LEAD.
* **FR-4 — San Mateo County Superior Court / California state trial-court index**, 2008–2009, Musk v.
  Eberhard/Straubel plus any settlement papers. CourtListener (`S4391`) is federal-only: this registry is
  **UNTRIED**, not empty.
* **FR-5 — corporate print, family (d)**: `ia_text.py fetch --id tesla-logo` and `--id teslaroadster0000maur`
  (2008, Tracy Maurer, print-disabled). Identified by metadata, **never opened**; a metadata year is not a date.
* **FR-6 — periodical page text**: `ia_text.py fetch --id elonmuskteslaspa0000vanc --max-mb 20` with the HTTP
  status recorded, and a per-item `fulltext/inside.php` search against 2004–2006 items. The page-text layer has
  **never** been searched for this company.
* **FR-7 — documentary/auction family (e)**: no scripted route exists in `tools/`; **UNTRIED by every pass**;
  needs an intake task, not an agent with a browser.
* **FR-8 — Delaware Division of Corporations** entity file for the 2003-07-01 charter; **USPTO** patents naming
  early inventors/assignees 2004–2008; the **8-A12B (2010-05-27), two FWPs + EFFECT (2010-06-28), S-8
  (2010-06-29)** index rows whose bytes are not on disk (`S4377`).

## 11. Five corpus families at close of merge (an untried family is never a null)

| family | status at close | evidence / obstacle |
|---|---|---|
| (a) **filings** | **TRIED — ANSWERED** | The only family with in-window Tier-1 text. 83 documents / 32 accessions / 59,881,144 B held; 336-row XBRL series `end` 2008-12-31 → 2012-12-31; 1,750-filing index (269 in-window, 0 blank `primaryDocument`); the 2005–2009 REGDEX band exists in the index and is **unheld**; the 3 UPLOAD PDFs are held-but-unreadable (FR-2) |
| (b) **web archives** | **TRIED — UNANSWERED** | One CDX answer, transcript-only, at `S4390`; every domain-scoped re-query 504 / "Internet Archive temporarily offline"; **no page bytes held**, so `U.4` rests on a LEAD and the 2009 joint statement is unreached (FR-3). A property of the Archive, not of Tesla's early web presence |
| (c) **periodicals** | **TRIED at the metadata layer — page-text layer UNTRIED** | IA `advancedsearch` ×3 answered (6 items, all books 2015–2018; two numFound-0 **catalog** nulls); Google Books feed answered (post-window); **HathiTrust Cloudflare interstitial and Chronicling America HTTP 403 = UNANSWERED** (`S4389`). `numFound 0` is a statement about the catalog, not the press (FR-6) |
| (d) **digitised corporate print** | **TRIED at the metadata layer — items UNTRIED** | title-scoped numFound 2 (`tesla-logo`, `teslaroadster0000maur`), creator-scoped 0; **identified, never opened**; the 2003 label on an Annual-Reports container is a mis-dating trap and is not treated as a 2003 document (FR-5) |
| (e) **auction / museum documentary** | **UNTRIED entirely — the largest gap in the company** | No scripted route in `tools/`, no hand query attempted by any pass. No claim that founding documents do not survive is made or licensed (FR-7) |

Extra family reached: **legal registers** — CourtListener v4 **TRIED / ANSWERED for federal only** (`S4391`:
497 + 16 hits, none in 2003–2010, California Superior Court out of scope), so the silence is **not** absence; the
state registry that would hold the founding dispute is UNTRIED (FR-4).

**Verdict this merge leaves standing:** Tesla's Stage 1 is documented by **one registrant voice in two datable
layers** (a July 2003 entity statement, an April 2004 relationship statement), plus a founder adjective that
entered the registration statement between 2010-01-29 and 2010-04-29 (bracketed by two held printings, `S4370`
and `S4371`), plus **nine contemporaneous instruments and five readable letters that are silent on 2003–2004**,
and by **no independent carrier of any 2003–2008 founding statement at all**. "We cannot know", at T3, is the
deliverable.

## 12. Carry-forward for the next pass

`## Untried` is carried **twice** in `stage_1.md`: part 2's eleven items verbatim inside Volume 2 (NEW-1…NEW-11)
and this merge's addendum at the foot of the volume (probe U-1…U-8 + the family table + the `U.23` anchor).
Highest-yield per call, in order: FR-1 (exhibit folder — settles three High-importance gaps and `U.23` from
bytes a script can reach), FR-2 (PDF re-fetch — converts three UNANSWERED staff letters into readable
in-window regulator documents), FR-3 (the 2009 joint statement), FR-4 (state docket), FR-5/FR-6 (the two
families that could move the tier to T2). **Three answered family-(c) nulls and one family-(d) count must not be
re-read as absence**: a wrong path is not a refusal (RD-129) and an unopened candidate is not evidence.
