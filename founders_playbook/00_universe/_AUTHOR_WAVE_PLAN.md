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
| s1-dell-p1 | company_041_dell | Header, boundary, §A–§J | T1 |
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
- Line numbers are locators; re-measure anything you publish after your last write.


## Correct three stale beliefs now circulating in briefs (2026-10-07, merge wave)

1. **`sec_intake auto` and `grab` work.** Two authors have refused to run intake because `auto` "rewrites
   `_RUN.json`/`_MANIFEST.csv` unconditionally" and `grab` was "broken fleet-wide". Both were fixed today:
   `version_aside()` keeps the previous run record beside the new one (RD-139, after Home Depot's probe proved
   the int-`cik` crash had faked an empty archive), and `grab`'s enumeration branch was unpacking 2 values from
   a 3-tuple (RD-138). Selftests: sec_intake 54/0, gates 18 controls PASS, harvest_mine 9/0, cdx_intake 37/0.
   A stale tool belief makes an agent request a fetch instead of running a script, which is the thing §15.1
   exists to prevent.
2. **Meta: part 2 landed before part 1 and already adopted part 1's anchor ids.** `p2` found part 1's
   pre-declared `U.1–U.7`, took them verbatim so part 1's `§U.n` cross-references resolve, and added `U.8`
   itself. So do **not** renumber anchors at the Meta merge, and do not dispatch `merge-meta` until
   `s1_p1.md` reports its sections complete.
3. **`--tier auto` cannot see a table-row verdict** (GM and AT&T both reported T3/T2 mismatches). Pass
   `--tier core|register` explicitly for the budget check and record that you did, instead of editing prose
   to satisfy a tool.

## Merge queue, in order of readiness (single-part dossiers merge immediately)
`cigna` (running), `gm` (running), `att` (running), `cvs` (running) -> then `jnj`, `pepsico`, `boeing`,
`jpmorgan` as their authors close -> `meta` and `dell` need BOTH parts before merging. Every merge is followed
by audits from different agents and then a certifier who is neither author, merger, auditor nor repairer.
