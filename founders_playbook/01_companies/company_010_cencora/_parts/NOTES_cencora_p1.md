# NOTES — company_010_cencora · Stage 1 · part 1 (agent `s1-cencora`)

STATUS: WRITTEN 2026-10-07. Pass log, not a deliverable volume. `_parts/s1_p1.md` is the deliverable.

## 1. Paths owned

- `founders_playbook/01_companies/company_010_cencora/_parts/s1_p1.md` (claimed, written, released `--done`)
- `founders_playbook/01_companies/company_010_cencora/_parts/NOTES_cencora_p1.md` (this file; claimed, released `--done`)

Claimed with `python tools/scaffold.py claim --agent s1-cencora --path <p>` (no `--force` used; the
`_parts/` directory was empty before this pass — verified by `ls -la` — so there was no live writer to
collide with, per §14 r7).

## 2. The tier I wrote to, and the probe's own verdict line quoted verbatim

From `research/A_chronology_feasibility.md`, "Verdict" ¶3:

> "**Tier issued (per RD-112, per stage, named window):** Stage 1 = `2001-03-16 → 2004-09-30` →
> **T3 register, PROVISIONAL** — one family (a) returning in-window Tier-1 text. It is a *count*-driven
> T3 with an unusually heavy carrier: 30 in-window documents across 6 filing lineages. Families (b) and
> (e) are UNTRIED, and (c) and (d) are TRIED–UNANSWERED for the reason in ¶2, so the ceiling is
> provisional, not the floor."

The probe's issued tier (**T3**, 8,000 words/stage, 3-4 runs) governed, not the dispatch label; the two
agree here. Wrote §Header/§Boundary/§A–§F/§K/§L/§M/§N/§P/§U + nine register blocks; §15.2's mandatory
T3 trio (§K money, §N decisions, §U conflicts) is inside p1 so the stage is not left depending on a
later run for its required sections.

## 3. Where I re-measured the probe and what changed under me (late-arriving bytes, §14 r11)

The probe (2026-10-06 17:36) recorded `sources/web_archive/` as absent and family (b) as **UNTRIED — 0
calls**. Enumerating `sources/` before writing showed the shelf had grown while that dossier stood:

| dir | probe saw | this pass measured |
|---|---|---|
| `sources/sec/` | 30 documents + metadata | **30 stored .txt documents + 30 sidecars + 5 run/plan/skipped/unanswered files** (unchanged) |
| `sources/web_archive/` | did not exist | **26 files = 12 html captures + 12 sidecars + `_RUN.json` + `_RUN.prev-20261006T123514Z.json`** |
| `sources/periodicals/` | 2 CIA layers | 2 CIA layers + 2 sidecars (unchanged) |
| `sources/corporate_print/` | 0 bytes | 0 bytes |
| `sources/financials/` | (not in the probe's table) | **1 file**: the XBRL `..._NULL.NULL.md` perimeter note |
| `sources/harvest_mine/` | (not enumerated) | **1 file**: `_index.json` (2 CIA items, both NULL, `in_window:false`) |
| `sources/_index/` | 7 files | 7 files (unchanged) |

Disposition: **family (b) is now TRIED–ANSWERED and is reported with its perimeter** (CDX
`matchType=domain&from=1994&to=2001`, `collapse=timestamp:6`, **`limit=500` returning exactly
`captures: 500`** = a capped enumeration, `fetch_attempted: 6` per domain, `stored: 0` /
`already_on_disk: 6`). Its 12 bytes span **1996-10-22 → 2001-02-02**, i.e. **all pre-date the
registrant's 2001-03-16 incorporation**, so it does **not** convert into an in-window Tier-1 family for
W-1 and I did **not** re-tier upward — nor did I write the perimeter-bounded silence as "the archive has
nothing". I raised **FR-6** to ask the W-1 half of the window for the first time. I disagree with
nothing in the tier; I note that the probe's family-(b) row is now stale, and gates' `--tier auto`
reader will keep returning T3 from the dossier that issued it.

## 4. Registrant resolution (the trap this company was briefed for)

Resolved **by CIK**, never by brand:
- `python tools/legacy_cik.py detail 11454 1140859` (run this pass, live EDGAR):
  `CIK 0000011454 BERGEN BRUNSWIG CORP | recent rows 190, earliest 1994-01-13, latest 2002-02-14 | 0 archive slice(s)`
  and `CIK 0001140859 Cencora, Inc. | recent rows 1000, earliest 2018-11-20 | 1 archive slice(s)`,
  formers `['AMERISOURCEBERGEN CORP', 'AMERISOURCE BERGEN CORP']`.
- `sources/_index/submissions.csv` (header enumerated first:
  `filingDate,form,accession,reportDate,primaryDocument,source`): 2,567 rows; **8 rows with accession
  prefix `0000011454`**, including the registrant's first 10-K (`2001-12-28 10-K 0000011454-01-500032
  reportDate 2001-09-30 abcform10k.htm`); **0 rows with `filingDate` < 2001-05-23**; **203 rows / 23
  forms inside W-1**.
- `legacy_cik.py search` was **not** used (UNPROVEN) and its silence would not have been read as absence.
- The 190-row "recent" slice is capped: 1994-01-13 is a floor of the slice, not the start of the record.

## 5. Names/ids discipline

- **No global `source_id` minted.** `python tools/id_mint.py --audit` only, to confirm: next assignable
  **S4531**, and the **S4222–S4229 range belongs to company_042_target** — untouched by this pass.
  Register `source_id` values are dossier-local `P1S01…P1S14`; claim records `P1-01…P1-24`; conflicts
  `P1U-01…P1U-04` with narrative anchors **U.1–U.4** and an explicit
  `<!-- ANCHORS: U.1-U.4 -->` declaration in the volume (gates reads that form as authoritative).
- Line numbers used only as locators; every address is carried by file + verbatim phrase or a stable
  label (§14 r12).
- Register headers copied field-for-field from the Amazon registers (`head -1` of each of the nine
  `company_001_amazon/*.csv` was read before writing). `stage` = `stage1` on every row; no numeric
  stage anywhere.

## 6. Corrections and disagreements I opened (all in the volume, not hidden here)

1. **Probe's W-1 closing basis does not foot.** It says "first three fiscal year-ends"; the index shows
   **four** September-30 year-ends up to 2004-09-30 (2001/2002/2003/2004). Window kept as issued;
   discrepancy recorded at §Boundary 2 and claim record P1-24. **Decision for the orchestrator:**
   either restate the basis as "three full years after the FY2001 stub" or close at 2003-09-30; I did
   not silently re-date.
2. **Ex-12.1 internal conflict (U.3)**: a "Year Ended September 30, 2001" column in an exhibit filed
   2001-08-24, whose own footnote describes FY2000 + 6M2001 pro forma inputs. New to this pass; the
   probe did not have Ex-12.1 in view.
3. **The `$36 billion` is not reproducible** from the held tables under either doubling (33.10b /
   37.08b), while the `$32 billion` **is** reproducible to within 0.5% ($32,143,496k). U.4.
4. **Decoy carriers found in family (b)**: three of six `amerisource.com` captures are a "Jay Creek
   Productions" real-estate/travel page. Registered (P1S13, P1-22) as a warning to future passes, not
   as evidence.
5. **U.1 three-way origin conflict** (1888 filing-independent web narrative vs 1956 S-4 recital vs the
   same web page's 1969 naming of "Bergen Brunswig Corporation") — the only place on this shelf where an
   off-lineage carrier touches the origin question, and it *disagrees* with the filing.

## 7. Independence calls made (§3)

- 30 stored files → **8 accessions**; the S-4 + S-4/A + S-4/A No. 2 (+ the unheld 424B3) = **one
  lineage**; the 2001-10-19 S-4 is a **different** lineage (own purpose: exchange offer).
- The three 2001 8-Ks are three filings but report **three different event dates** (2007-31 / 08-27 /
  08-29), so they are not three accounts of one fact; the 08-29 and 08-30 pair brackets one closing week.
- A predecessor's archived web page is an **independent origin but the same self-report class** — used
  for what Bergen *said*, never as third-party corroboration.
- Amazon, Tesla and every other company's values were not imported; `company_043_tesla/stage_1.md` was
  read for **format only** (header block, per-section claim records, `>>> REGISTER ROWS FOR MERGE <<<`
  marker style, the refiled-amendment-not-corroboration pattern).

## 8. Gates

Command run after the last write:
`python tools/gates.py --company-dir founders_playbook/01_companies/company_010_cencora --tier auto --out founders_playbook/03_quality_control/cencora_s1_gates_p1.md`
Findings recorded in that file and summarised in my report. Coverage findings ("no register CSVs at
root", "no stage volumes…") are the expected pre-merge state and were **not** repaired by inventing
files. `anchors` will read the ANCHORS declaration in the volume; register-cited anchors resolve only
after the merge writes the CSVs, so parity is expected to report UNANSWERED — stated here so nobody
"fixes" it by writing company CSVs from a part file.

## 9. Counts as re-measured after my final write (see report)

`wc -w` on `_parts/s1_p1.md`; per-block row counts re-counted by parsing each fenced csv block against
its own header width (a width check, not a visual one), and the ANCHORS declaration re-greped. If the
p2/p3 passes edit this file they must re-key any pointer into it (§14 r12) and re-measure these counts.

## 10. Not done by this pass (by design, per the brief)

No merge. No certification. No company register CSV written. No harvester or intake run (only
`legacy_cik.py detail` for the CIK resolution and `id_mint.py --audit` read-only). Nothing under
`sources/` was created, moved, pruned or renamed — the shelf is read-only to this agent.
