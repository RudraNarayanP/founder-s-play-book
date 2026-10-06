# NOTES_meta_p2.md — author log for `company_017_meta` Stage-1, PART 2 (§K–§U + registers)

Owner: `s1-meta-p2`. Output file: `founders_playbook/01_companies/company_017_meta/_parts/s1_p2.md`
(gate: `founders_playbook/03_quality_control/meta_s1_gates_p2.md`). Nothing outside these was written.
Part 1 (`_parts/s1_p1.md`, owner `s1-meta-p1`) was read ONLY for its section list, its boundary, and — once
it appeared mid-run — its `ANCHORS` handoff; its prose was neither copied nor rewritten, and it was not edited.

## Tier: disagreement recorded, not silently re-tiered (§ brief rule; §15.2)

This dossier was **dispatched as T1** (the header and the probe both carry a T1 expectation), but
`research/A_chronology_feasibility.md` renders a **T2 verdict on the bytes standing on disk right now**
(2 of 5 families in-window: filings + legal register; web/periodical/auction missed on an outage or untried).
I did **not** re-tier. I wrote to the T1 *shape* (§K–§U full, nine registers, claim records) but let the
content honestly fall to T2/T3 density where the evidence is thin: §P and §L are dominated by `UNKNOWN`, and
that is the deliverable (§15.2 "we cannot know is a deliverable"). The probe is explicit that two cheap
re-runs (Wayback CDX once archive.org answers; RECAP/PACER docket text) would make this genuinely T1 — see
`## Untried` and the FETCH REQUESTs below.

## Boundary reconciliation (the main hazard found this pass)

The probe proposes Stage 1 closing at the **July-2004 incorporation**; the harvest/dispatch window
(`A4_harvest_mine.md`, `_RUN.json`) is **2003→2012**. Part 1 adopted the *dispatched* window for §A–§J and
registered the divergence as an anchor; I (this part, §K–§R) built against the *probe's* July-2004 close. Both
are defensible readings of the same probe, and the divergence is **registered at U.7 rather than resolved here**
(no agent re-stages the company on its own authority). Net effect for the reader: under either close the
load-bearing facts are identical (0 filings in 2004; July-2004 month; all company metrics are 2009+ restatements).
I softened my earlier "out-of-window" absolutes to name the U.7 conflict.

## §U anchor numbering — adopted part 1's taxonomy

Part 1 pre-declared anchors `U.1–U.7` for seven conflicts but owns **no `## U` section** (§U is part 2's), and
emits **zero register CSV blocks**. Its lines 104–106 state §U "is owed by part 2, which must fold or renumber
them and continue from U.8." My first draft used an *independent* 5-conflict numbering that reused the same ids
for different subjects — that would have made the two parts contradict at merge (p1 cites `§U.2/§U.4/§U.5/§U.6/
§U.7` across its A–J narrative). So I **rewrote §U to part 1's taxonomy verbatim** (U.1 formation-day, U.2
subject-of-origin, U.3 2005-vs-first-filing, U.4 silence-vs-register, U.5 Feb/dorm-vs-dated, U.6
thirty-days-growth, U.7 window), folded my analysis into those slots, and **added U.8** (the truncated-index
tooling artifact, probe META-C3, which p1 never enumerated). All `§U.n` cross-references in §K–§S and every
`conflict_ref`/`conflict_id` in the registers were remapped to match. Verified 1:1: declared == §U headings ==
conflict_ids == {U.1..U.8}, no stray token beyond U.8. (Also fixed a `gates.py` quirk: prose containing the
literal substring "ANCHORS:" hijacks `declared_anchors`; I reworded that prose so only the real `<!-- ANCHORS:
U.1-U.8 -->` comment is parsed — set went 10 → clean 8.)

## Corrections taken this pass (probe statement vs the bytes) — none reach the instruction layer, all noted here

The probe's load-bearing claims were re-verified against `sources/` before writing (§14.8 grep-before-write).
Three of its statements needed qualification — these are **my** corrections, NOT part-1 contradictions, so no
`conflicts.csv` row was opened against `s1_p1.md` (which had no contradicting content):

1. **`845 million` MAU is NOT in the held S-1 text.** The probe cites "845 M MAU at 31 Dec 2011"; the string
   `845 million` returns 0 hits in `0001193125-12-034517_d287954ds1.htm`. The S-1 prints "more than 800 million
   MAUs"; the 424B4 "more than 900 million." I therefore did **not** assert 845; §K.5/§U.6 use only verified
   figures (revenue $3,711M / op income $1,756M / net income $1,000M FY2011, all at S-1 line ~5602).
2. **Ceglia appears in the S-1 body, not only the 424B4.** The probe quoted the Ceglia paragraph as "from the
   424B4." Verified: `Ceglia` = 7 occurrences in the S-1 `.htm` too (S-1 and 424B4 are the same lineage — one
   instrument family, not two witnesses, §3). §K.3/§U.4 cite the S-1 bytes.
3. **"Harvard" in the S-1 is a 2011 popular-pages example, not a founding statement.** `Harvard College` = 0
   hits; the 7 bare "Harvard" hits include "Advertisers can engage…" / a Pages list ("Harvard, Lady Gaga…").
   Recorded so no agent back-dates a Harvard origin to the S-1 text (it is in the *graphic*, §S).

The probe's central zero-hits — `Winklevoss`, `ConnectU`/`Connectu`, `Divya`, `Saverin`, `Eduardo`, `Moskowitz`,
`thefacebook`, `Harvard College`, `February 2004` — were all confirmed 0 in both the S-1 and 424B4.

## What is a TRUE NULL (complete enumeration) vs UNANSWERED/UNQUERIED/UNTRIED — never report a blocked family as absent

- TRUE NULLs (earned): no CIK filing dated in 2004 (397-row `submissions_pre2014.csv`, oldest row 2005-05-06);
  no CIK filing before 2005-05-06; no certificate-of-incorporation exhibit in the S-1 accession (28-item file
  list, only `dex231`); the S-1 "Our History" section is image-only (23 JPGs); the contested-name strings are
  0 in both filings; the corpus has no "thirty days" string.
- UNANSWERED (blocked, NOT null): Wayback CDX ×3 (HTTP 504 / 503 "Internet Archive services are temporarily
  offline"; bodies kept, zero capture dates).
- UNQUERIED (killed by failure-breaker): `internet_archive`, `corporate_print`; HathiTrust ×2 returned 0-byte;
  Chronicling America ×3 HTTP 403.
- UNTRIED: family (e) auction/museum; Delaware SoS; California SoS; RECAP/PACER pleadings; the 2005–06 paper
  items; OCR of the history JPGs; the S-1/A + CORRESP comment trail.

## Registers emitted (nine fenced `csv` blocks in §registers; header identical to Amazon; `stage`=stage1; source_id provisional `P2SRC-n`)

- `sources.csv` — 9 rows (provisional P2SRC-1..9; independence noted; S-1+amendments+424B4 = ONE lineage).
- `timeline.csv` — 4 rows (2003-04 alleged, 2004-07 incorporation, 2004-09-02 docket, 2005-05-06 gap marker).
- `quantitative.csv` — 6 rows (all Stage-1; FY2011 revenue deliberately NOT emitted as a Stage-1 register row; kept in §P narrative as out-of-window context).
- `conflicts.csv` — 8 rows (U.1–U.8, 1:1 with §U anchors).
- `data_gaps.csv` — 8 rows (every High-importance gap carries a follow_up_task).
- `decisions.csv` — 3 rows (N01 incorporation; N02 proceed-despite-claim; control row, LOW as Stage-1).
- `validation.csv` — 2 rows (one docket signal; one earned null "NONE RECOVERABLE").
- `failures.csv` — 3 rows (contested ownership; alleged 2003 agreement; disclosure failure).
- `channels.csv` — 0 rows (earned null; stated in prose, no junk row).

Rows withheld / folded, as required: **channels** — no Stage-1 distribution channel is printed anywhere in
`sources/`, so the register is left empty (header only) and the gap is carried in `data_gaps.csv` + §O/§S,
per "a row you cannot attribute to a register is worse than a paragraph." **FY2011 revenue** — a genuine
Stage-2 quantitative fact; excluded from the Stage-1 `quantitative.csv` register (it lives only in the §P
narrative table as RESTATED out-of-window context) so the merge's stage filter is not polluted.

## FETCH REQUEST: (script-reachable documents this agent must not hand-fetch; §15.1)

The probe reports `sec_intake.py` `grab`/`auto` is broken fleet-wide (bytes-vs-str `ERROR_MARKERS` bug), so
documents below are enumerated-but-unstored; returning a request, not fetching, is the correct behaviour.

FETCH REQUEST: sec_intake — accession 0001193125-12-034517 — document: the 6 `UPLOAD`/`.paper` items and the
`NO ACT`/`REGDEX`/`REGDEX/A` paper rows (2005-05-06 → 2008-10-14) — purpose: resolve U.3 attribution ("is any
of it the registrant? do not let 'Facebook registered 2005' enter any register").

FETCH REQUEST: sec_intake — accessions 0001193125-12-046715 / -101422 / -134663 / -175673 / -208192 / -222368 /
-232582 (the eight S-1/A) and the five `CORRESP` + six `UPLOAD` comment-letter PDFs — purpose: see whether the
SEC staff asked about the founding account (would bear on U.5, §B/§D).

FETCH REQUEST: web (wayback_cdx) — `url=thefacebook.com` and `url=facebook.com`, bare+www, one window test each —
purpose: earliest capture date (family b re-run after the outage; would partly close U.5 and lift tier).

FETCH REQUEST: periodical_harvest — `--source-family corporate_print --source-family internet_archive` (meta) and
a Chronicling America / HathiTrust retry — purpose: in-window 2004–2006 press, esp. Harvard/Crimson student
paper (closes families c/d; §S).

FETCH REQUEST: legal (RECAP/PACER) — full docket text for **1:04-cv-11923**, 1:07-cv-10593, 07-1796 and the
Ceglia matter — purpose: the earliest *independent* narrative of 2003–2004 (register proven reachable;
pleadings not fetched).

## `## Untried` (explicit, per §15.2) — also in §S.2 of the part file

Delaware Division of Corporations charter; California SoS entity record; RECAP/PACER pleadings; the 5 `CORRESP`
+ 6 `UPLOAD` items and 8 `S-1/A` amendments; OCR of the 23 S-1 history JPGs; family (e) auction/museum; the
Wayback CDX re-run; a college/student-press corpus (no configured route in the five families).

## Refusals (what I would NOT claim)

- Did not assert a February-2004 or dorm-room founding date (0 supporting bytes; §U.5 → UNKNOWN).
- Did not back-date "headquartered in Menlo Park" (a 2012 present-tense statement) to 2004 (§6; §R).
- Did not treat the 424B4 as corroborating the S-1 (same registration lineage, §3; §T.1).
- Did not report families b/c/d as empty (they were blocked/unqueried, not null); did not let a
  `TIER1_CANDIDATE` scanner flag or an index row count as evidence.
- Did not invent a `channels.csv` row, a source_id, or a `fetch` a script can do.
- Did not re-tier the company; recorded the T1-vs-T2 divergence instead.
- Did not edit `s1_p1.md`; adopted its §U anchor taxonomy rather than colliding with it.

## What I did NOT examine

- I did not read the full S-1/424B4 narrative line-by-line (2.6 M / 3.5 M bytes); I string-censused the
  load-bearing terms and extracted the specific passages quoted.
- I did not open the eight S-1/A bodies, the `dex10x`/`dex3x` exhibits, `filename30/32.htm`, or the 215 XBRL
  rows individually — only the earliest-period bounds (XBRL min end 2010-12-31) and the accession inventory.
- I did not read the CourtListener *Winklevoss* payload or the post-2008 noise rows (unrelated parties); only
  the 2004–2007 Facebook/ConnectU/Zuckerberg docket rows were used.
- I did not open any `sources/web/cdx_*` or `sources/_harvest/*` body beyond confirming they are error/metadata
  pages (they are not evidence).
- Family (e) auction/museum was not attempted at all (probe skipped it; I concur for a 2004 internet company).
