# STAGE-1 AUTHOR WAVE — dispatch plan (2026-10-07, after the probe wave closed)

Tools verified before this plan was written: `gates.py --self-test` PASS (18 controls), `sec_intake.py selftest`
54/0, `harvest_mine.py --self-test` 9/0, `cdx_intake.py --self-test` 37/0. Tree clean, pushed, in sync.
Shared author contract: `03_quality_control/STAGE1_AUTHOR_BRIEF_SHARED.md` — **every brief below assumes it and
must tell the agent to read it first.** Cap: 20 concurrent subagents INCLUDING background scripts, so launch 14
and leave headroom; a refused dispatch must be re-appended here, never remembered.

Format per dispatch: agent name `s1-<slug>-p<k>`, WRITE only `01_companies/<dir>/_parts/s1_p<k>.md` plus one
gate file and one log line in `_parts/NOTES_<slug>_p<k>.md`. Tier comes from the probe dossier; `gates.py --tier
auto` now reads it from disk. 40 companies have no `stage_1.md`; 35 have a probe and a tier.

## Wave 1 — 12 agents (launch now, in one message)

| agent | company | scope | target |
|---|---|---|---|
| s1-meta-p1 | company_017_meta | Header, boundary, §A–§J | T1 (60k/stage) |
| s1-meta-p2 | company_017_meta | §K–§U + registers for both halves | T1 |
| s1-dell-p1 | company_041_dell | Header, boundary, §A–§J | ~~T1~~ **T2 prov.** (probe; my label was wrong) |
| s1-dell-p2 | company_041_dell | §K–§U + register emissions | T1 |
| s1-jpmorgan-p1 | company_012_jpmorgan | full §A–§U, 1799/1812-lineage split by person | T2 22k |
| s1-cigna-p1 | company_014_cigna | full §A–§U, INA + CG + 2018 shell as three persons | T2 22k |
| s1-gm-p1 | company_023_gm | full §A–§U | T2 22k |
| s1-att-p1 | company_035_att | full §A–§U, 1885 NY vs 1983 DE vs 2005 revived name | T2 22k |
| s1-jnj-p1 | company_045_jnj | full §A–§U | T2 22k |
| s1-pepsico-p1 | company_046_pepsico | full §A–§U, registrant recites 1919 DE / 1965 formed | T2 22k |
| s1-boeing-p1 | company_047_boeing | full §A–§U, "since 1916" is a different person | T2 22k |
| s1-cvs-p1 | company_006_cvs | full §A–§U, Melville successorship, 1996 is not an IPO | T2 22k |

## Wave 2 — 14 agents (after wave 1 slots free)

`cencora, cardinal, centene, elevance, humana, verizon, ups, fedex, marathon, valero, wellsfargo,
morganstanley, comcast, goldman` — all T3 (8k/stage), one author each, §K/§N/§U still mandatory, each carrying
its probe's family verdict and its predecessor-name trap.

## Wave 3 — remaining T3 tail (one author each)

`berkshire, exxonmobil, bofa(=company_020), chevron, ford, citigroup, homedepot, kroger, disney, mckesson,
fanniemae, phillips66, stonex, statefarm, freddiemac, rtx` — six of these (`mckesson, fanniemae, phillips66,
stonex, statefarm, freddiemac`) have **no probe dossier**: run `probe-<slug>` against
`03_quality_control/PROBE_BRIEF_SHARED.md` first, then author.

## Merge wave — after each company's parts exist (one agent per company, never two on one dir)

Command the merge must run first: `python tools/merge_census.py --company-dir <dir> --verbose`; ids only via
`python tools/id_mint.py --count N --company <dir> --claim --agent merge-<slug>`; `validation.csv` vs
`failures.csv` blocks are unattributable by schema and now print content hints — adjudicate them and say how;
`research/*.csv` third emissions are invisible to the census and must be picked up by hand (Tesla: 25 rows).
Merge agents may not certify. Then audits (numbers+hindsight; citation+verbatim) by different agents, then a
certifier who is neither author, merger, auditor nor repairer.

## Standing hazards to put in every brief
- **Never `--force` a claim; the ledger owns paths** (`scaffold.py status`), and dead agents keep locks —
  `scaffold.py release --agent X --all` is the orchestrator's job.
- Enumerate a CSV header before reading a field by name. Three agents lost work to invented columns.
- `sec_intake auto` now walks every slice and prints `walk: … date perimeter A -> B`; a pre-1994 silence is a
  perimeter, and a **ticker may resolve to the wrong legal person** (`XOM`→2115436 vs historic 34088; Comcast's
  2002 successor vs the 1963 company). Ancestors are reached by CIK: `python tools/legacy_cik.py detail <cik>`,
  and `search` is **unproven** — never treat its silence as absence.
- `tools/web_domains.json` gates family (b): if a slug is absent, (b) is UNTRIED and that must be said, and the
  agent must request a cited domain (a filing line printing the domain) rather than invent one.
- Family (e) auction/museum/manuscript has **no tool at all**: it is UNTRIED for every company, structurally.
- **Report paths are repo-root-relative, so write the whole thing**: `founders_playbook/03_quality_control/<file>.md`.
  Nine gate reports landed in a repository-root `03_quality_control/` because a brief said
  `03_quality_control/...`; that stray directory exists now, is untracked, and is NOT the canonical home -- do not
  add to it, and do not delete from it either while any agent may still hold a path inside it.
- Line numbers are locators; re-measure anything you publish after your last write.


## Correct three stale beliefs now circulating in briefs (2026-10-07, merge wave)

1. **`sec_intake auto` and `grab` work.** Two authors have refused to run intake because `auto` "rewrites
   `_RUN.json`/`_MANIFEST.csv` unconditionally" and `grab` was "broken fleet-wide". Both were fixed today:
   `version_aside()` keeps the previous run record beside the new one (RD-139, after Home Depot's probe proved
   the int-`cik` crash had faked an empty archive), and `grab`'s enumeration branch was unpacking 2 values from
   a 3-tuple (RD-138). Selftests: sec_intake 54/0, gates 18 controls PASS, harvest_mine 9/0, cdx_intake 37/0.
   A stale tool belief makes an agent request a fetch instead of running a script, which is the thing §15.1
   exists to prevent.
2. **Meta is merged** (30,212 w / 120 live rows, anchors 8↔8, `S4495–S4509`) and its part-2 anchor story is
   now history, not a warning: part 2 adopted part 1's `U.1–U.7` and added `U.8`; the merger de-duplicated
   15 conflict rows to 8 one-per-subject. Nobody renumbers Meta's sections.
3. **`--tier auto` is FIXED (RD-142) -- stop pinning `--tier core`.** It binds a tier to the stage that
   issues it, reading per-stage **table rows** and `Stage 1 -- T2 core` dispatch bullets, ranks
   dispatch-line > table-row > company-wide `TIER: Tn`, grades each volume at its own stage's tier, and prints
   the tier it used plus any disagreement between same-rank lines. So `gates.py --company-dir <dir> --checks
   budget` with no `--tier` is now the correct command, and an explicit `--tier` is a override you must
   *justify*, not a workaround. If the tool still contradicts your dossier, say so in your report and pass the
   flag -- but the three reports that started this (GM, Boeing, JPMorgan) now resolve T2 for Stage 1 with no
   override at all.

## Merge queue, in order of readiness (single-part dossiers merge immediately)

**Merged, under audit as of RD-142:** `cigna` (14,513 w / 78 rows; auditor FAILED it -- one blocker, held bytes
do print its incorporation date -- and a repairer is on it), `gm` (20,192 / 114), `att` (31,315 / 136),
`cvs` (19,520 / 126), `jnj` (27,043 / 102), `pepsico` (22,958 / 106), `boeing` (34,817 / 211), `meta`
(30,212 / 120). **Still to merge:** `jpmorgan` (running, single part), `dell` (part 2 has 2 `STATUS: PENDING`
blocks being finished first, and its merge must take the UNION of part 1's `U.101-U.111` and part 2's
declarations without renumbering either). Every merge is followed by audits from different agents and then a
certifier who is neither author, merger, auditor nor repairer.

## Correction to MY wave table, from Dell's author (2026-10-07)

I wrote `dell = T1` and `meta = T1` in the table above. **Dell's probe measures T3, T2-PROVISIONAL, and says T1
is structurally unreachable**; the author wrote to T2 density and logged the disagreement instead of silently
re-tiering. The rule this re-establishes: **the probe's measured tier governs, not my dispatch label** — §15.2
sets the tier from the five families, and a label from me is ambition, which is precisely what §15.2 was written
to stop. Before wave 2/3 dispatch, read each probe's verdict line and put THAT in the brief; where my table
already sent a wrong tier, the author's NOTES file is the correction to carry into the merge.

Dell's part 1 also declared anchors **U.101–U.111** (not U.1–U.11) because part 1 and part 2 are being written
concurrently against one id space — so the Dell merge must take the union of both parts' declarations and prove
parity once, not renumber either part.


## Tool-form corrections found by authors (put these in every later brief)
- `ia_text.py` file listing is **`list-files --id <identifier>`**; the form in my first briefs
  (`list-files <identifier>`) exits `unrecognized arguments`, so a probe reported a route as unrunnable
  when it was runnable. PepsiCo proved the route works and enumerated 102 layers / 17.86 MB, 27 of them
  pre-1965 — the first time family (d) has been *counted* for a tail company.
- The probe's CLI docstring in `tools/ia_text.py` should be aligned with the parser; until then, an agent
  that hits an argparse error on a documented form must report it rather than conclude the route is dead.

## `gate_quotes` cannot match a quotation of our own research files (Cigna merge, 2026-10-07)

Cigna's merge left one finding on the board that it correctly refused to "fix": the volume quotes
`research/A4_harvest_mine.md` l.5 verbatim, and **`gate_quotes` indexes only `sources/**`**, so a quotation of
a research dossier can never match. The finding pre-dates the merge (it was in the probe's gate file), and the
right response was exactly what happened — record the evidence, leave the data alone.

Two consequences for me: (1) quoting a harvest dossier inside a volume is legitimate practice and the gate
should know it, so the fix is to index `research/*.md` as a corpus of quotable text or to label such spans
`[research:]` and exempt them; (2) until then, **every merge at every company will carry one permanent false
advisory**, which trains people to ignore the quote gate — the failure mode §15.6 exists to prevent. Do the
fix with a self-test control, not by hand-waving it in a manifest.

**SHIPPED, RD-142.** `gate_quotes` now indexes a second-class reference corpus (the company's `research/*.md`,
`00_METHOD_AND_STYLE.md`, `03_quality_control/*BRIEF*.md`, `00_universe/_*.md`) and prints
`matched-in-project-text-only N` in its own note, so the exemption is counted rather than hidden. Measured
effect: Cigna's false advisory is gone (0 findings, 1 project-text match); Meta's 10 unmatched spans become
7 primary + 3 project-text; CVS's one real case (an in-quotation `[~]` OCR marker) stays visible as a
question for the auditor instead of disappearing. Control: `research-dossier quotation matches` in
`gates.py --self-test` (25 controls, all PASS).
