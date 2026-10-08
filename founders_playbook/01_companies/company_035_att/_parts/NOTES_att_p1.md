# NOTES — `company_035_att` Stage 1, authoring pass 1 (`s1-att-p1`)

Owner of `founders_playbook/01_companies/company_035_att/_parts/s1_p1.md` by
`python tools/scaffold.py claim --path founders_playbook/01_companies/company_035_att/_parts/s1_p1.md --agent s1-att-p1 --sections "Header,boundary,A..U,registers"`
(claimed 2026-10-06T21:16:07Z, ttl 240 min, sections=4). This file is the pass log; it is not a corpus volume and
no other agent owns it.

## 1. What was read before writing (in order)

1. `founders_playbook/03_quality_control/STAGE1_AUTHOR_BRIEF_SHARED.md` — in full (64 lines).
2. `founders_playbook/00_METHOD_AND_STYLE.md` — in full (490 lines): §3 claim classes, §5 tiers, §6 time audit,
   §7 section set and fixed line formats, §8 table discipline, §9.2/§9.3/§9.6 file geometry, §13 register schemas
   and the `stage1` vocabulary, §14 defect catalogue, §15 pipeline and tier table.
3. `company_035_att/research/A_chronology_feasibility.md` — in full (254 lines). **Scope taken from it:** Stage 1
   **T2 core, PROVISIONAL**, 22k w/stage, 6–9 runs; five-family verdict (a) answered, (b) UNTRIED, (c) answered-thin
   / search routes UNANSWERED, (d) answered-strongest, (e) UNTRIED and unimplemented; the registrant answer
   (CIK 732717 = SBC/Southwestern Bell, Delaware 1983, ticker `T`; CIK 5907 = American Telephone & Telegraph
   Company, New York 1885, per its own FY1993 10-K l.237-240); the 1915 future-tense finding; 1877 as apparatus
   epoch with 0 carriers in SEC bytes.
4. `company_035_att/research/A4_harvest_mine.md` — in full (51 lines), re-read before quoting per the brief;
   superseded **for label counts only** at §Header 4 / §T.
5. `company_001_amazon/_parts/s1_p1.md` (163 lines) **for format only**; also `company_016_nvidia/_parts/s1_p1.md`
   and `company_043_tesla/_parts/s1_p1.md` for the register-emission block shape and the `>>> REGISTER ROWS FOR
   MERGE <<<` marker convention. No Amazon value, date or phrasing imported.
6. `tools/gates.py` §anchors/§keys/§corrections/§coverage read directly, to know what the gate would and would not see.
7. Held bytes, opened and read at lines (this is the substance of the dossier):
   * `sources/periodicals/annualreportofdi00amer_14_djvu.txt` (5,631 lines) — title block, officers l.47-95,
     directors l.98-128, l.144-260 (system statistics, plant additions), l.330-480 (construction, maintenance,
     depreciation, the 1915 projection, operating results, capitalisation, ICC valuation), l.484-760 (the 1912/1913
     comparison tables and combined balance sheets, the 1907/1913 retrospective), l.962-1120 (Western Electric,
     per-station earnings series 1895-1913), l.1245-1345 (the company's own earnings, capital issues, shareholders,
     pension plan), l.1360-1560 (the apparatus and cable chronology), l.1660-1900 (the December 19, 1913
     correspondence in full), l.1900-1975 (government ownership), l.2985-3020 (Chicago & Milwaukee reprint),
     l.5000-5180 (the company balance sheet and comparative earnings), l.5480-5631 (the growth diagram).
   * `sources/periodicals/report-of-a-conference…djvu.txt` (8,784 lines) — l.15-28 (imprint), l.316-419 (roster and
     Hall's opening), l.4565-4650 (the 1885/1887 cable specifications), l.4870-4900 and l.5030-5055 (supplier
     failures), l.7032-7115 (the Philadelphia/Boston failure exchange and the New England Company letter).
   * `sources/periodicals/somecommentsona00chicgoog_djvu.txt` (1,390 lines) — l.114-173 (imprint and author),
     l.177-300 (the extract frame and the competition/public-control passages), l.660-700 (Central Union),
     l.745-770 (Bell methods, Western Electric 1907), l.1015-1040 (independents 1895-1900), l.1150-1170 (patents,
     apparatus pricing), l.1231 (the *American Telephone Journal* reprint note).
   * The three `DTIC_ADA*` layers were **not** read as sources; they were counted and rejected as decoys.
   * Seven SEC documents cited, each located at a line: `0000005907-94-000008`, `0000732717-94-000005`,
     `0000732717-95-000003`, `0000732717-00-000018`, `0001047469-05-002185`, `0001193125-05-015481_d425.htm`,
     `0000950134-05-008807_d24647posam.htm`; plus their `.meta.json` sidecars (url, cik, accession, fetched, sha1,
     bytes, words, http_status) and `sources/sec/_MANIFEST.csv`.

## 2. Measurements taken by this pass (nothing below is inherited)

* **Quote-location check.** Every fragment quoted in the part file was searched in the held file it is cited to,
  with a whitespace-and-entity-normalising matcher, before being written. Line locators in the file are the raw-line
  numbers this produced (e.g. `0000005907-94-000008` l.238 for the 1885 recital; l.1121 for "leased from the regional
  holding companies created at divestiture"; l.3454 for "Telegrah"; `0000732717-94-000005` l.210 and l.213;
  `0000732717-95-000003` l.151; `0000732717-00-000018` l.226; `0000950134-05-008807` l.548;
  `0001193125-05-015481` l.15 and l.42-44). Two probe citations are **locators across wrapped lines**, so they read
  slightly differently from a raw grep: the probe's "l.237-240" and this pass's "l.238" are the same sentence.
* **Name-grep re-measurement (ATT-S1-C1).** Case-sensitive, joined-line rendering: FY1913 layer
  `American Telephone` **0**, `American\s+Telephone` **29** (**35** case-insensitive — the probe's number),
  `American\s+Telephone\s+and\s+Telegraph\s+Company` **20** / **25**. 1887 layer `American\s+Telephone` **2**,
  `"American Bell"` **3**. 1908 pamphlet **4**. Finding unchanged: a single-space name grep misses the registrant's
  own title page.
* **Token census on the seven cited SEC documents (ATT-S1-C2).** `1885` **1**, `1984` **40**,
  `Bell Telephone Company` **32**, `Southwestern Bell` **207**, `American Telephone and Telegraph` **7**;
  `1875` `1876` `1877` `1894` `1895` `1915` `transcontinental` `Alexander Graham Bell` `American Bell` all **0**.
  Within `0000005907-94-000008` alone: `1885` 1, `1984` 26, `divestiture` 5, `Bell System` 3, `1877`/`1915`/
  `transcontinental` 0. The probe's counts were taken over 37 files; both denominators are stated where used.
* **Periodical-layer date census.** FY1913: `1877` 2 (l.1364, l.1368), `1876` 2 (l.5506, l.5552 axis),
  `1895` 3, `1915` 2 — **the second `1915` is new to this dossier**: l.5091 is a *maturity*
  ("Indebtedness to Western Union Telegraph Co. for New York Telephone Co. Stock Payable 1914 to 1915 … 4,000,000.00"),
  not an opening; `1894` 1 (the chart axis tick at l.5552). 1908 pamphlet: `1894` 1, `1895` 1.
* **Arithmetic (all printed in §K.3).** Ten cross-foots performed on the held print, all footing exactly, one
  (**the annualised traffic rate**) not footing: 27,237,000 × 365 = 9,941,505,000 vs printed 8,770,300,000. No value
  substituted; the discrepancy is registered as **U.5** and as quantitative row `P14`.
* **Shelf re-enumeration (§14.11, done at close).** `sources/sec/` = **33 documents / 10,500,602 B**, every one with
  a `.meta.json` sidecar (0 sidecar-less); `sources/periodicals/` = **6 layers / 707,735 B**;
  `sources/corporate_print/` = **0 files**. The gate independently reports "39 source documents", which is 33 + 6.
  **Correction to the probe (ATT-S1-C5):** it prints the periodical shelf as 660,753 B; the six `.txt` layers sum to
  **707,735 B**. Byte totals were recomputed with `os.path.getsize` over the six files.
* **`tools/web_domains.json`** read this pass: keys `_provenance_note, _states, slugs`; `slugs` holds
  **centene, cencora, relevance, marathon, microsoft, target** — **no `att` entry**. Family (b) therefore stays
  **UNTRIED and unscopeable** in this dossier, exactly as the brief conditions it.

## 3. Judgment calls made here, and why

* **The pass is written as a multi-registrant dossier, not one company's childhood.** §Header 1 fixes four persons
  (P1 Bell Telephone Co./American Bell, P2 AT&T New York 1885/CIK 5907, P3 the seven 1983-84 RHCs, P4 Southwestern
  Bell → SBC → AT&T Inc/CIK 732717) and **every section's first line names the person it describes**. §Q names a
  person per row, including two explicitly out-of-window rows (1983, 1984-01-01) kept in the Stage-1 chronology so
  no later merge can place them silently in the wrong registrant's infancy. The `company` column of the register
  rows follows the printed convention in §Registers (P2 / P4 / the pair).
* **1984 is written as the place the record creates a new registrant** (§Boundary 3), from both sides' own sentences,
  and is registered as U.4 with the "birth vs amputation" direction kept. It is *not* narrated as Stage 1 and *not*
  narrated as failure (§M refusal (i)).
* **1915 is carried in the future tense and is labelled so everywhere it appears** (§Boundary 2, §D.4, §U.3,
  timeline row 1915, quantitative row set). The design/event distinction is stated as the section's
  "load-bearing judgment", and the two 1915 hits in the held print are separated (projection vs maturity).
* **The quarantined index is treated as tooling, not as absence** (§Header 1, §T.4, `P1S11`): the guard's verdict and
  the 1,255-row perimeter are reported as measurements of EDGAR's reach; no Stage-1 fact rests on an index row.
* **Family (a)'s 1885 answer is quoted as the 1885 line's own.** `P1S04` is CIK **5907**'s FY1993 10-K, and is
  labelled RESTATED (1994 document reciting 1885) so that it is never mistaken for an in-window document, and never
  attached to 732717. The reverse discipline is applied too: P4's 1983 recital is never used to date the brand's
  century.
* **Tier not re-tiered.** T2 core PROVISIONAL kept, including the probe's own two re-grades folded into it (c→d
  would make T3; admitting the 1994 recital would make T1). Logged here: this pass **adds evidence in favour of
  keeping (d) as the firm family and treating (c) as a hostile third-party carrier, not a second corporate-print
  carrier** — the 1908 pamphlet is an *opponent's* print whose P2 content is quotation. If the merge counts it as
  (c) alone, Stage 1 rests on (a)+ (d) for tier purposes, which is still two families and still T2.
* **Word count vs the tier cap.** The part file is **36,595 words** against a T2 planning cap of 22k/stage.
  Per RD-122 (cap = dispatch budget, not a limit on written evidence) **nothing was trimmed**, and the file is inside
  method §9.2's soft target of 40k for a stage file and far inside the 60k hard cap. The excess is recorded for the
  merge, not hidden: the density comes from two unusually rich in-window carriers (136,506 B FY1913 report with
  audited-style tables; 334,305 B conference print) and from §K.3's arithmetic, which cannot be cut without
  destroying the footing evidence. If the orchestrator wants the stage under 22k, the legitimate move is to
  **split** (§9.3: `s1_p1` Header/Boundary/A–H, `s1_p2` I–P, `s1_p3` Q–U+registers), not to trim.
* **`S6-11` in the keys note.** The gate reports "cites 1 hyphenated record keys: S6-11". That string is the DTIC
  document code `S6-11-25-ATT`, quoted as evidence that a bare `att` token is a substring of a code. It is a
  document code, not a register key, and was **not** re-pointed.

## 4. Corrections issued by this pass

| id | superseded / inherited statement | this pass's finding |
|---|---|---|
| ATT-S1-C1 | probe table: FY1913 `American\s+Telephone` = 35 | 29 case-sensitive / 35 case-insensitive; both printed, finding unchanged |
| ATT-S1-C2 | probe counts over 37 files (`1984` 74, `Bell Telephone Company` 47, `Southwestern Bell` 566) | re-measured over the 7 cited files (`1984` 40, 32, 207); the zeros survive at the smaller denominator |
| ATT-S1-C3 | P4's 1983/1984 sentences | re-verified at l.210-213 of the held 10-K |
| ATT-S1-C4 | the 1908 pamphlet as "an independent lineage naming P2" | it is a **hostile trade-association** pamphlet by the General Manager of a citizens' competing company; narrows what it can carry |
| ATT-S1-C5 | periodical shelf 660,753 B | **707,735 B** over the same 6 layers |
| (new) | `1915` = 1 in the FY1913 layer (probe implies one) | **2** hits: l.400 the projection, l.5091 a 1914→1915 stock-payable maturity |
| (new) | `1894` unreported in the FY1913 layer | **1** hit, l.5552, a chart-axis tick only — it is not the patent-expiry date in the company's own print |

## 5. Register emission — rows by register (all provisional; no company CSV touched)

sources **14** · quantitative **44** · timeline **28** · decisions **7** · validation **7** · failures **10** ·
channels **5** · conflicts **9** (U.1-U.9, 1:1 with the declared anchors) · data_gaps **12**. Total **136**.
Width validated by parsing every fenced block with `csv.reader`: 9 blocks, 0 rows off header width
(widths 18/12/11/15/11/11/11/15/8), `stage` = `stage1` on every row, `source_id` values dossier-local.
**Rows withheld: none.** The five §7 frames that do not fit a regulated utility are answered with adapted
equivalents plus `UNKNOWN` rows (§F customer identity, §G headcount, §K personal finances, §N decision-maker,
channels cost), not by omission.

## 6. Gate

`python tools/gates.py --company-dir founders_playbook/01_companies/company_035_att --tier auto --checks csv,keys,anchors,corrections --out founders_playbook/03_quality_control/att_s1_gates_p1.md`
→ **exit 0**, 1 finding, 0 passes-listed:
`coverage | registers | no register CSVs at root or research/ -- csv/anchors gates DID NOT RUN` — the expected
pre-merge state, **not repaired by inventing files**. Notes: 1 stage volume, 39 source documents; ANCHORS set of 9
read; "no register anchors found — UNANSWERED, not passed"; corrections gate did not run (no `CORRECTIONS.md`).
Nothing in the gate output was reshaped to make it quieter.

## 7. What this pass did NOT examine

The other 26 stored SEC documents in `sources/sec/` (1994-2000 prospectuses, proxies, the 1998 Ameritech S-4 family,
the 2005 8-K/13G set) — Stage-3 material, not cited and not read; the three `DTIC_ADA*` layers beyond counting and
rejecting them; `sources/_index/quarantine/*` beyond what the probe already measured; every sibling company;
`MASTER_RESEARCH_LOG.md`; `tools/*.py` except reading `gates.py` for its check semantics; `00_universe/harvest/
candidates.csv` (its row-level facts are taken from the probe, labelled as inherited, and were not re-counted).
No retrieval was attempted: 0 WebSearch, 0 WebFetch, 0 `sec_intake`/`harvest_mine`/`periodical_harvest` runs.
Six FETCH REQUEST blocks (R-1..R-5 plus the probe's standing asks) are emitted in §S for the orchestrator.

## 8. Tool-call budget

Ceiling 135; **closed out at 67 tool calls** (§14 rule: at 80% stop opening new work). Section-by-section append held: the
file was written Header→U→registers in order, each marked `STATUS: WRITTEN` (24 markers, 0 PENDING remaining), so a
stoppage at any point would have left a readable, mergeable file.

## 9. Ids and post-write repairs inside the part file

* **56 claim records, all unique.** The four §Boundary records were first written `B01-B04` and collided with §B's
  `B01-B04`; they are re-issued as **`BD01-BD04`**. Nothing else was renumbered: §A-U record ids, §P metric ids
  `P01-P50`, `U.1-U.9` anchors and the dossier-local `P1S01-P1S14` source keys are stable across the file as written.
* Six `csv` width defects (an unquoted comma inside a field, the drift §14 names) were found by parsing all nine
  fenced blocks with `csv.reader` and repaired in place; the final parse is **9 blocks / 136 rows / 0 rows off
  header width**. This is the check the `csv` gate will run once the merge creates the files, so it was run here first.
* The scaffold banner ("nothing written yet") was replaced by the written Header rather than left standing, since
  24 sections now carry `STATUS: WRITTEN` and the banner would mislead a cold reader.
