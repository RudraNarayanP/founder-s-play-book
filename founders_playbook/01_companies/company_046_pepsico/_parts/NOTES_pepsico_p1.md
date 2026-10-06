# Author log — `company_046_pepsico` Stage 1, part 1 (`_parts/s1_p1.md`)

Agent `s1-pepsico-p1` · claimed 2026-10-07 via
`python tools/scaffold.py claim --path founders_playbook/01_companies/company_046_pepsico/_parts/s1_p1.md
--agent s1-pepsico-p1 --sections "Header,boundary,A..U,registers"` → CREATED (owner=s1-pepsico-p1, 4 claimed
tokens expanded into 26 stampable headings so each section could be marked WRITTEN as it was finished).

## Read first, in the briefed order

1. `03_quality_control/STAGE1_AUTHOR_BRIEF_SHARED.md` — in full.
2. `company_046_pepsico/research/A_chronology_feasibility.md` (probe `probe-pepsico`) — in full, and its hard
   facts carried: the recital "incorporated in Delaware in 1919 and reincorporated in North Carolina in 1986";
   "formed in 1965" printed **only inside the dividend-policy paragraph** of five filings; 0 occurrences of
   `1893`, `1898`, `1902`, `pharmacist`, `Bradham`, `Caleb`, `Herman Lay`, `bottle cap`, `crown`, `since 18`
   across the 27 stored SEC documents.
3. `company_046_pepsico/research/A4_harvest_mine.md` — read too, because the brief said read them all, and
   **it is a later dossier** (mtime 2026-10-06 18:14) than the probe (17:28).
4. `00_METHOD_AND_STYLE.md` §3–§9, §13–§15.
5. `company_001_amazon/_parts/s1_p1.md` **for format only** — its nine register header rows were copied
   verbatim (`head -1` of each Amazon CSV) and no Amazon value, date or phrasing was imported. Format
   cross-checked against the two most recent same-tier sibling volumes
   (`company_016_nvidia/_parts/s1_p1.md`, `company_013_costco/_parts/s1_p1.md`).

## The corpus is not what the probe measured — §14 r11 in action

The probe's A.1 recorded **0 periodical bytes**. When this pass opened, `sources/periodicals/` held **11 text
layers (4,130,659 B, fetched 2026-10-06 12:33–12:44 UTC / 18:03–18:14 local)**, and `research/A4_harvest_mine.md`
had been written over them. §14 rule 11 required me to account for the arrivals rather than inherit the probe's
silence, so every print-family row in §T.1 carries its own retrieval time and two probe conclusions were
re-tested against bytes. Outcome:

* **Superseded (probe A.3): "The merger story itself: UNKNOWN — no carrier in this corpus."**
  `periodicals/01-pepsi-co_djvu.txt` l.122 (the PepsiCo **2017** annual-report shareholder letter, signed
  Indra K. Nooyi) prints "Two years later, in 1965, Frito-Lay and Pepsi-Cola merged to form PepsiCo." That is
  one carrier, one sentence, 52 years late, same corporate lineage → the merger moves from UNKNOWN to **Low /
  RESTATED**, and the change is registered as conflict **U.10** rather than written as if the probe had been
  wrong about everything.
* **Carried forward unchanged:** every folklore zero; the two-origin-lines-plus-merger structure; the
  ex-21 subsidiary finding; the single-lineage verdict; the five-family states; the T3 tier.

## New measurements made by this pass (all reproducible from `sources/`)

* `1965` = 22 occurrences over 38 documents: 15 dividend clauses, **2 director-tenure decoys**
  ("ROBERT H. STEWART, III, a director since 1965", `K94` l.296, `K95` l.526), 2 unrelated `ERIC` facility
  dates, **1 merger sentence** → conflict U.11. The probe counted 5 filings and did not name the tenure rows.
* `1919` = 14 occurrences: 8 SEC files + 5 print reprints of the same Item 1 sentence + **1 A&W founding**
  inside `YUM08` → U.7. Also measured why a naive grep under-counts: the FY1999 filing spaces the recital so
  wide that a single-space pattern misses it; the count of 8 requires a loose pattern.
* `founder` = **0** and `founded` = **0** in all 27 SEC documents — the registrant's EDGAR voice contains no
  founder narrative at all, only a charter recital.
* `1893` = 1 occurrence: a **trademark name** in the 2020 proxy marks list ("including 1893, Agusha, Amp
  Energy, Aquafina") → U.8. `bottle cap` = 4 occurrences, all 2020–23 tethered-cap regulation text;
  `crown` = 2, both in the 1906 Hongkong Telegraph; `Herman` = 4, all decoys ("Hermanos", "Sherman Act" ×2,
  an artist "Sarai Sherman") → §D.1, U.9.
* `EX21` census: 91 rows with a countable jurisdiction (Delaware 81, California 4, New York 3, Texas 2,
  Nevada 1); `Pepsi-Cola Company` 40 occurrences in 10 files, `Frito` 455 (SEC) + 130 (print), none dated.
* One in-window dated document exists, and the probe did not have it: `CAT48`, *Pepsi-Cola Company's Fourth
  Annual Exhibition, Paintings of the Year*, venues 1947-10-01→1948-04-18, foreword signed
  "Walter S. Mack, Jr., President", with programme money ($15,250 awards; $1,500 fellowships; $14,700 of
  purchases) and a ~650,000-calendar circulation (§D, §L, three channels rows).
* `PR74` (Concordia University, Dec 1974) is the corpus's only third-party naming of a Pepsi-Cola-titled
  corporation — of `Pepsi Cola Canada Ltd.`, a different person (U.12).
* `OP5` (ex-5.1, 2001-02-28): the only counsel-signed situs statement, "PepsiCo, Inc., a North Carolina
  corporation", expressly "limited to the laws of the State of North Carolina" and printing **no** date.

## The route the probe called cheapest — run, and it answered

The brief said record it UNTRIED-by-order **unless I ran a script that already exists**. I ran the existing
script and reported it as TRIED:
`python tools/ia_text.py list-files --id 01-pepsi-co` → **102 text layers, 17,860,942 B**; 86 named
"PepsiCo, Inc. (PEP) Annual Report 1938–2024" with **one missing year (1984)**; **27 layers 1938–1964
(917,852 B)** and **21 layers 1965–1986 (1,994,223 B)** — i.e. **48 in-window corporate-print layers,
2,912,075 B, all unfetched**; **7 of them (1958–1964) tagged "(Frito-Lay)"** under a PepsiCo filename.
Two findings came out of that single call: (i) the probe's CLI form does not parse
(`list-files 01-pepsi-co` → `error: unrecognized arguments: 01-pepsi-co`; `mode` is positional, identifier
goes to `--id`) — U.15/P1-41; (ii) the layer filenames are anachronistic on their face, which escalates the
RD-130 artefact from "the metadata date is wrong" to "the uploader renamed 27 pre-1965 reports with a person's
name that, on the registrant's own word, began in 1965" — U.4, U.5.
I did **not** fetch the layers: `ia_text.py fetch` writes into `sources/periodicals/`, which is outside my
WRITE scope, and §15.1 routes script-reachable retrieval to the orchestrator. It is FETCH REQUEST 1 with the
exact `--file` arguments and byte sizes.

## Tier: T3 kept, and why the later dossier does not regrade it

`A4_harvest_mine.md` does not state a tier. This pass re-measured against §15.2 and **kept T3** for all three
sub-stages (1B/1C still PROVISIONAL), because the tier rule counts **in-window Tier-1 text held**, and:
family (a) holds 0 documents inside 1919–1986; family (d/c) holds exactly **one** in-window dated document, and
it is an art catalogue of the *subsidiary-line* person; everything else the print family added is
post-window (2017/2020/2022/2023/2024 layers) or another registrant's (YUM 2008) or a naming without a date
(Concordia 1974, Canada person). Recorded as U.15 together with the fact that `gates.py` printed
"tier: exemplar (no tier stated …)" for the probe — a tool default that is not a finding. `gates.py` this pass
read the tier as **T3** from the dossiers, so the stated tier and the gate's reader now agree.

## The window I propose, from carriers (the harvester's is rejected)

`harvest_mine.py:71`'s `1898-01-01 → 1965-12-31` is rejected and named as the cause of the wasted pass-1
(`pass1_docs=0`). Proposed: **Stage 1 = 1919-01-01 → 1986-12-31**, carried as **1B** (1919–1964, both ends
carrier-printed) and **1C** (1965–1986, the only sub-stage whose both endpoints are printed in held bytes),
plus **1A** kept as a named but **explicitly undated** claim-slot whose upper bound is 1919 and whose lower
bound is `UNKNOWN`. Refused as endpoints: 1893, 1898, 1902 (0-carrier terms).

## Refusals

Refused to claim: PepsiCo was founded 1893/1898/1902; that 1919 is a founding rather than a charter recital;
that five filings "corroborate" 1965 (one lineage, and one of its two clauses dates 1973 by arithmetic);
that `01-pepsi-co` proves a 1938 PepsiCo; that the printed layer counts of another registrant's report are
PepsiCo evidence; that the 2020 marks-list "1893" is a date; that the 1974 Canadian sponsor is a registrant
event; that `cor5` is a chronology carrier; that the franchise system's 1995 existence says anything about its
inception; that the 2001 BeverageCo structure is evidence about 1965. All are `UNKNOWN` rows with named routes.

## Defects found in the pipeline, recorded rather than repaired

(1) corporate_print YEAR-facet artefact: `drop_year_facet` (`periodical_harvest.py:1401–1427`) rewrites only
`params["q"]`, CP tasks carry `year_range` and no `q`, whole family skipped → `sources/corporate_print/` still
0 B while CP-classified items sit in `sources/periodicals/`. (2) `01-pepsi-co` = 2017 layer under a 1938 label;
`pepsicofritolayannualreports` = `yum2008_djvu.txt`, a YUM! Brands 2008 report, promoted to
TIER1_CANDIDATE_TEXT by `A4`. (3) `ERIC_ED337649` (130,917 B, the corpus's only third-party Frito-Lay naming)
appears in **neither** `A4` nor `harvest_mine/_index.json` (`grep -c ERIC` → 0). (4) `--max-docs 30` left 88
in-window filings unlisted — every occurrence count in this dossier is a minimum. (5) The probe's route CLI
form. All five are §M.2 rows and failures.csv rows P1F02–P1F08. I changed **no** tool and **no** data.

## Scratch and scope

Files written by this pass: `_parts/s1_p1.md` (25,400 words), this file, and
`03_quality_control/pepsico_s1_gates_p1.md`. One scratch artifact:
`E:\founder's playbook\_tmp_pepsico_layers.json` — repo-root, mine, the stdout of the single `list-files`
call, named in §T.1 and in the volume's closing paragraph so the next agent can delete or reuse it
deliberately rather than find it unexplained. Nothing under `sources/` was created, moved, pruned or edited;
no company register CSV was touched; no other `_parts/` path was opened.

## Word-count note

25,400 words against a T3 planning cap of ~8k for a stage. Per RD-122 the cap is a dispatch budget and §9.2
forbids trimming evidence to fit a limit, so nothing was cut; the excess is the price of a dossier whose
substance is a measured zero-set (50 census rows in §P.2 and quantitative.csv) plus 15 conflicts, and the
§9.2 hard cap (60k) is not approached. Flagged here so the merge does not treat the length as a defect.
