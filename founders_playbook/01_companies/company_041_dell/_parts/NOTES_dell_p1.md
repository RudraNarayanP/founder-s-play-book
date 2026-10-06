# NOTES — Dell Stage-1 part 1 (`_parts/s1_p1.md`, agent `s1-dell-p1`)

Log file, not a corpus file. Nothing here is evidence for a Dell claim; it is the record of choices,
disagreements and measurements the merge and the next agent need. Company: `company_041_dell`.
Window authored: **1984-05-03 → 1992-07-03** (Stage 1, §Header/boundary + §A–§J). Date of work: 2026-10-06.

## 1. Tier — I do not accept the dispatch label, and I did not re-tier the dossier either

The brief that dispatched this part called Dell a **T1 exemplar**. The probe (`research/A_chronology_feasibility.md`
§Verdict) measures **T3 register** on the founding window (1984 – mid-1988: one family returns in-window Tier-1
text), and its 2026-09-27 §SUPERSEDED block re-grades family (a) to **T2 PROVISIONAL** under §15.2's literal
in-window test, while stating that **T1 is structurally unreachable for Stage 1** (a floored 1994-02-11 by the
filing regime, b floored 1996-12-21 by the medium). Per the shared brief ("the probe's tier … is your scope; if
you disagree with a tier, say so in your log — do not silently re-tier"), this part:

* wrote to the **T2 density** the regrade licenses (evidence-bound §A–§J, all nine registers emitted, claim
  records for load-bearing claims only);
* stated the tier inheritance and the disagreement inside the dossier's own Header, so a cold reader cannot
  mistake the part for a T1 product;
* **did not** upgrade any confidence, family count or tier claim on the strength of the dispatch adjective.

For the orchestrator's convention ruling: family (a)'s held text is **retrospective about** the window
(1994-04-01 onward) but **dated inside** the assigned 1984-01-01 → 1992-12-31 stage window only via registry
fields; part 1 treated (a) as RESTATED-for-window and (c) as CONTEMPORANEOUS-in-window throughout, and every
row in `quantitative.csv` carries a `PERIOD BASIS:` label so the two conventions can be separated mechanically
at merge.

## 2. Corrections against the inherited probe (evidence first; no data file touched)

Two probe statements are wrong **as written**, and both were caught by reading bytes already on disk (§14.8).
The probe file is not this part's write target, so the corrections live here, in the dossier (§A.4, §U.111) and
in the `conflicts.csv` / `data_gaps.csv` rows:

1. **"The earliest Tier-1 EDGAR fiscal-year figure reachable for this registrant is FY1992"** and **"A five-year
   Item 301 table was searched for and its heading string does not appear in this accession — do not assume
   FY1990 exists here."** The FY1994 10-K **does** carry a five-column Selected Financial Data table at
   `sources/sec/0000950134-94-000347_0000950134-94-000347.txt` l.910-955; its caption is `YEAR ENDED` and its
   column heads are `JANUARY 30, 1994 / JANUARY 31, 1993 / FEBRUARY 2, 1992 / FEBRUARY 3, 1991 / FEBRUARY 2,
   1990`, with the consolidated-net-sales row at l.925 printing `2,873,165 2,013,924 889,939 546,235 388,558`.
   → Earliest held Tier-1 fiscal observation is **FY1990 (ended 1990-02-02) $388,558 thousand**. Cost of sales,
   gross profit, opex, operating income, net income, EPS, share count, working capital, total assets, long-term
   debt, preferred and equity all print for the same five columns (l.926-955). **Still nothing for FY1984-FY1989.**
2. **"No form S-1 of any vintage appears in either enumerated history" / "no S-1 among 1,851 filings".** Re-parsing
   `sources/_index_cik0000826083/sources/_index/submissions.csv` on this pass returns **9 S-1-family rows**:
   `S-1` dated **2008-06-05** ×3 (accessions 0000950134-08-010828 / -010830 / -010831), `S-1/A` dated
   **2008-07-21** ×3 and `S-1/A` dated **2008-08-08** ×3 — a Dell Financial Services securitisation vintage,
   **not** the IPO. The **window** null the
   probe was defending is intact and is now stated exactly: **0 filings of any form dated 1984-01-01 → 1992-12-31**
   (counted from the same CSV), and 0 S-1 inside it. A later agent that greps `form == "S-1"` and finds nothing
   in-window is right; one that reports "no S-1 exists for this registrant" is wrong.

Also **superseded, in the direction of more evidence** (both from bytes the probe itself held but did not read
that way):

3. **"The earliest Tier-1 address evidence held is a lease agreement for Arboretum Point dated 1987-07-25."**
   The April 1987 advertisement prints **1611 Headway Circle, Building 3, Austin, Texas 78754**
   (`sources/periodicals/byte-magazine-1987-04_djvu.txt` l.22484) — three months earlier, in-window, self-published.
   The October 1988 ad prints **9505 Arboretum Blvd., Austin, Texas 78759-7299** (l.42210-42211), which matches the
   lease's Arboretum Point and is independently echoed by BYTE's editorial review block at l.49074 of the same issue.
4. **"The legal identity link [PC's Limited → Dell] is unproven at Tier 1 in this corpus."** Two in-window artifacts
   share the **order line 1-800-426-5150** (87-AD l.22478 vs 88-AD l.42127, l.42164 and 88-REVIEW l.49076) and the
   **support line 1-800-624-9896** (87-AD l.22486 vs 88-AD l.42186), plus the same city, the same 30-day guarantee
   and the same one-year-from-shipment warranty. That is a mechanism (subscriber-assigned 800 routing) for
   **operational** continuity; the **instrument** remains unheld. The dossier grades them separately (Medium-High /
   Low) rather than collapsing them.
5. **C-4 (Honeywell Bull) upgraded from Low to Medium** on the reading that the service copy appears **twice** in
   two blocks of the same Dell-attributed spread (l.42109-42114 and l.42194-42211), each attached to "your Dell
   system" and to Dell's own name and address, with the `(c) 1988 DELL COMPUTER CORPORATION` + AD-code footer at
   l.42816. Page-image verification is still owed (FR-3), and the **contract** is still unverified (Low).

## 3. New nulls and false-positive warnings earned on this pass

* `grep -c "Michael Dell"` = **0** in all four held BYTE issues (re-counted, matching the probe); and
  word-boundary `\bDell\b` = **0** in BYTE April 1987 — the name is absent from the company's own 1987 print.
* The string **`$1,000`** in held EDGAR text is a **director attendance fee** (`94-PROXY@l607`; re-printed
  `95-10K405@l3465`, `@l3509`). Any keyword harvest for the "$1,000 founding capital" story over this corpus
  returns that fee. Registered as §U.105 so the merge cannot promote it into §K.
* `University of Texas` in held filings describes **a director's** affiliations (`94-PROXY@l510`), **not** Michael
  Dell's enrolment. Flagged in §B.2 as a misattribution trap.
* **`sources/periodicals/` grew during the run** (§14.11 duty): 9 DTIC reports, 2 monographs and 1 microfilm item
  arrived 2026-10-06 after the probe. All are accounted for in `data_gaps.csv` row 13 and considered-cited: the
  harvester's own verdict table (`research/A4_harvest_mine.md`) records 0 `TIER1_CANDIDATE_TEXT`, 0 entity hits,
  5 `BARE_WORD_MATCH` (a lake, a surname, an author's middle name) and 7 NULL. They bear on no part-1 claim and
  may not be cited.

## 4. Contract decisions taken while emitting

* **Anchor block reserved:** part 1 issues **U.101–U.111** only, each written in the narrative (declared-anchor
  section) and each with its `conflicts.csv` row — 11 anchors, 11 rows, 1:1. Part 2 is asked to number from
  **U.112+**. If the merge re-keys, both volumes' prose must be re-pointed together.
* **`source_id` left provisional** (`P1SRC-01…12`) because ids minted by authors have collided; the merge mints
  centrally via `tools/id_mint.py`. Nothing in the prose depends on a global id.
* **Company column is `Dell Computer Corporation` for every window row**, never "Dell Technologies": the 1984 line
  is CIK **0000826083** and the ranked registrant CIK **1571996** begins **2013-07-24** as the Denali/EMC vehicle
  (its first 10-Q primary document is `denaliq1fy1710q.htm`). The shell's index now lives CIK-keyed at
  `sources/_index/quarantine/CIK0001571996/`, and that file prints the registrant guard sentence; that quarantine
  artifact is what §U.110 cites for "the guard exists because of this collision".
* **`(PB)` applied aggressively**: FY1993 and FY1994 columns, the "fifth largest vendor / $2.87 billion" sentence,
  the One Dell Way Round Rock address, the 2008 S-1s, the 1994 SC 13G/A and the 1996 web floor are all carried as
  carriers or context and **excluded from window rows**. The **2013 take-private price** is withheld entirely.
* **Confidence ceilings:** no periodical-sourced row is graded High (all archive.org bytes are sidecar-stamped
  `transport: UNVERIFIED TLS`; the probe's verified-TLS control returned `cached` and tested nothing). Recorded as
  **U11** plus FR-3/FR-4 rather than quietly promoted.
* **Register hygiene measured, not assumed:** after writing, all nine blocks were re-parsed with a CSV reader —
  18/11/12/15/8/15/11/11/11 columns per header, **118 data rows, zero width drift, zero empty cells**. Five drift
  defects were found and fixed in place (four unquoted-comma fields, one doubled-quote field, one extra cell in a
  decisions row) — that is the exact defect class the brief warns about, so it is reported rather than hidden.

## 5. File geometry and length (measured after the last write, 2026-10-06)

`_parts/s1_p1.md` = **28,783 words** (840 lines): narrative **17,670**, nine register emission blocks **7,717**,
part-1 claim-record block **3,308**. Against §15.2 the T2 cap is 22k words **per stage**, so Stage 1 as a whole
will exceed it once part 2 lands; against §9.2 the part is comfortably inside the 60k hard per-file cap and the
narrative alone sits inside T2 density. Recorded rather than trimmed: **"Cutting evidence to fit a file limit is
forbidden — the limit governs file geometry, never research depth"** (§9.6), and §15.4 makes a missed length
target legitimate, not a failure. If the orchestrator wants strict T2 geometry, the lever is the emission blocks
(7,717 words of register rows that the merge moves into CSV anyway), not the narrative.

Gate run (the assigned command) returned **1 finding, coverage-only**: "no register CSVs at root or research/ --
csv/anchors gates DID NOT RUN", with `anchors _parts/s1_p1.md declares 11 anchors` and `corrections no
CORRECTIONS.md -- gate DID NOT RUN (not a pass)`. All three are the expected pre-merge state and none was
"fixed". Output: `03_quality_control/dell_s1_gates_p1.md`. One tool note worth the owner's eye: `--tier auto`
read the tier as **T3** ("25 mentions, 1 on a verdict line") while the dossier's own Header says **T2 PROVISIONAL
per the regrade** — the gate itself prints "if the dossier's own text names a different tier, trust the dossier",
which is the instruction followed here.

## 6. What part 1 did NOT do

No CSV was written to the company root; no other part or company was touched; no register was merged; the probe
files and `sources/` were not edited, moved or deleted; no git operation was run; no `WebSearch`/`WebFetch` call
was made (**0 spent** — every fact in this part came from bytes already in `sources/`, re-read directly); no
gate finding was "fixed" by inventing a file; `gates.py --checks csv,keys` coverage findings ("no registers yet",
"no stage volumes yet") are the **expected pre-merge state**.

## 7. Highest-value next actions, in yield order

1. **FR-3 / U10** — page images of BYTE Apr-1987 p.81 and Oct-1988 pp.160-163 + 179: settles §U.104, §U.108,
   §U.109 and lifts the OCR cap on every in-window row.
2. **FR-4 / U1** — HathiTrust + Google Books corporate print (FY1989-FY1993 reports/proxies, 1988 prospectus): the
   tier-deciding test, now script-triable.
3. **U4** — paper S-1 **33-21823** chain, asking by name for **Ex 10.25** (the 1984-05-03 agreement, which should
   name the predecessor) and the **Ex 10.22-10.24** lease/plan set: settles §U.101's instrument and §K's capital.
4. **FR-1 / U8** — the two FY1995 `10-K405/A`s and the 8-A12G (FR-2) already enumerated but unfetched: cheapest
   remaining Tier-1 bytes; the route to inventory figures and to the exchange-identity question behind §U.107.
5. **U3** — PC World / PC Week 1988 for the Knorr and Fastie material Dell quoted, and the 1984-1986 run never
   enumerated for Dell at all.
