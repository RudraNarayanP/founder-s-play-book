# RESUME PROMPT — paste this into a fresh agent, nothing else needed

You are taking over **THE FOUNDER'S PLAYBOOK**. Repo root: `E:\founder's playbook` (Windows, Git Bash shell,
a git repo whose remote is `origin` = the user's GitHub). Work from that directory with absolute paths.

## 1. The mission
Reconstruct, from public evidence only, the early history of the 2026 Fortune 50 top-50 companies — origin →
first real-world experiment → first repeatable validation → scalable company — as a forensic dataset. The
method is the law: **read `founders_playbook/00_METHOD_AND_STYLE.md` (490 lines) before your first write.**
Every company directory lives in `founders_playbook/01_companies/company_<rank>_<slug>/`.

## 2. Non-negotiable rules (each of these was bought with lost work)
1. **Never fabricate a citation.** `UNKNOWN` is a preferred answer; an honest empty with a named route beats an
   invented completion every time. Every claim needs a carrier: file + line number, in `sources/` on disk.
2. **§3 source independence.** An S-1 + its amendments + the 424B = ONE lineage. md5-identical files = ONE
   document. A `TIER1_CANDIDATE` label, an index row, or a scanner result is a POINTER, not evidence. Only an
   opened byte proves a claim.
3. **Claim every path before writing** (`python tools/scaffold.py claim --agent <id> --path <p>`), release it
   `--done`, and **never `--force`**. One path, one owner. `scaffold.py ledger` is the authority on ownership —
   never your recollection of who died. Release a dead lane's locks with `release --agent <id> --all`.
4. **Never `git add -A`.** Agents and a nightly GitHub workflow write concurrently; stage explicit paths.
   Commit and push after each finished lane (pull/merge first — the nightly pushes to `main`).
5. **Do not delete, move, prune or "tidy" shared evidence**: `sources/`, `research/`, `00_universe/harvest/`,
   `00_universe/_EVIDENCE_CACHE*`. Supersede, don't erase: retractions go into the company's `CORRECTIONS.md`
   as `COR-nn` and must reach BOTH the registers and the volume that carried the withdrawn text (the
   `corrections` gate proves this mechanically).
6. **Role separation (§15.6):** author ≠ merger ≠ auditor ≠ repairer ≠ certifier. An ADVISORY gate output is
   **not** a defect and must never be "repaired" by rewriting evidence. Never loosen a threshold to get a
   better answer.
7. **Line numbers are locators.** Re-measure anything you publish AFTER your last write. A report that says
   "verified from disk" is itself a claim. A listing cut by `head` is not a census; counts need scopes.
8. **Cost discipline:** cap at **10 concurrent subagents** (background scripts count toward it — a 18-20 lane
   wave previously hit the provider's daily quota and killed every lane with no reports written). Agents cost
   ~10-25M tokens each; repairs cost 2-4× authoring. **Ask the user before launching a big wave**, and prefer
   lanes that convert bytes already on disk over lanes that create new ones.

## 3. Tools (all stdlib Python, all self-testing — use them, do not reinvent)
| tool | verified command |
|---|---|
| `tools/gates.py` | `python tools/gates.py --company-dir <dir> --out <path>` — `--tier auto` resolves the tier **per volume** from the company's own probe (fixed in RD-142; do NOT pin `--tier`). `--self-test` = 25 controls PASS |
| `tools/scaffold.py` | `claim` / `release --agent X --all` / `ledger` (alias `status`) / `section` / `touch` |
| `tools/merge_census.py` | `--company-dir <dir> --verbose` — run BEFORE any merge write; `validation.csv` vs `failures.csv` print AMBIGUOUS (identical schemas) — adjudicate by row and say how |
| `tools/id_mint.py` | `--count N --company <dir> --claim --agent <id>` — allocate above the highest live id, never re-enter a gap, **never enter `S4222-S4229`** (a known Microsoft/Target collision, task #31) |
| `tools/sec_intake.py` | `auto "Registrant Name" --company-dir <dir> --from --to --max-docs 30` — walks every EDGAR slice and prints `date perimeter A -> B`; `--selftest` 54/0. Run records are versioned, never clobbered |
| `tools/legacy_cik.py` | `detail <cik>` is solid (name, perimeter, slice count, formerNames); `search <term>` is **UNPROVEN** — its silence is never absence |
| `tools/cdx_intake.py` | family (b) Wayback route; `--self-test` 37 checks 0 defects; slugs in `tools/web_domains.json`: centene, cencora, elevance, marathon, microsoft, target. **No slug = UNTRIED, never a null** |
| `tools/harvest_mine.py` | `--company <slug> --limit 12 --max-mb 25` → writes `research/A4_harvest_mine.md`; `--self-test` 9/0 |
| `tools/periodical_harvest.py` | live IA/CP/CA/Hathi/GB queries; `--facet-free` drops the YEAR facet from `q` AND `year_range` |
| `tools/ia_text.py` | Internet Archive layers: `list-files --id <identifier>` (the `--id` is required), `<id> --file <name>` |
| `tools/provenance_check.py` | re-verifies every `.meta.json` sidecar against disk; `--self-test` 6/6. Current census: 6,898 sidecars, **0 SIZE / 0 HASH / 0 MISSING** |
| `tools/fleet_intake.py` | batch intake over the universe CSV (`--all`, `--only slug`, `--dry-run` writes nothing) |

`tools/_tmp_*.py` are leftover agent scratch — not maintained, don't extend them.

## 4. State as measured on disk (git `fa9db9e6`, tree clean, 0 live claims)
- **19 merged Stage-1 volumes: 734,262 words, 4,274 register rows.** Amazon 50,814 (**SIGNED**) · Walmart 59,516
  · Apple 57,502 (registers in `research/`) · Alphabet 57,358 · Tesla 55,347 (**CERTIFIED**) · UnitedHealth
  44,996 · Target 42,833 (**CERTIFIED**) · AT&T 31,315 · Nvidia 46,691 · Costco 46,992 · Boeing 34,817 ·
  JPMorgan 34,637 · Microsoft 34,707 · Meta 30,212 · J&J 27,043 · PepsiCo 22,958 · GM 20,192 · CVS 19,520 ·
  Cigna 16,812.
- **Certified: 2** (Tesla, Target) + Amazon signed. **Audited with a verdict: 1** (Cigna — FAILED: 1 blocker,
  8 findings, `03_quality_control/cigna_s1_audit1.md`).
- **Gates baseline (2026-10-08, `03_quality_control/_GATES_BASELINE_2026-10-08.md`): 14 substantive findings.**
  jpmorgan 4 (`anchors`,`keys`,`quotes`); cigna 2 (`corrections`,`keys`); cvs 2 (`csv`,`quotes`); walmart,
  unitedhealth, apple, costco, meta, pepsico 1 each (all `quotes` = the secondary-print gap, task #15, not
  fabrication); the other 10 volumes clean.
- **Parts complete, unmerged (0 PENDING blocks):** Cencora 14,916 · Verizon 17,293 · UPS 12,215 · Centene
  10,268 · FedEx 5,516 (thin — say so rather than padding). Dell p1 28,786 + p2 32,398 (**2 PENDING blocks**
  in p2; its merge must take the UNION of p1's anchors `U.101-U.111` and p2's, renumbering neither). Humana
  14,617 with **5 PENDING blocks**. Elevance 3,481 (incomplete).
- **Nothing written at all:** Cardinal, Marathon, Valero, Wells Fargo (scaffold stubs).
- **No volume, no part (~19 companies):** Berkshire, McKesson, ExxonMobil, BofA, Chevron, Ford, Citigroup,
  Home Depot, FannieMae, Kroger, Phillips66, StoneX, StateFarm, FreddieMac, Goldman, Comcast, Morgan Stanley,
  Disney, RTX. Six have **no probe dossier**: mckesson, fanniemae, phillips66, stonex, statefarm, freddiemac.
- Boeing has 211 rows merged but **no `CORRECTIONS.md`** — bookkeeping gap, check it.

## 5. Next actions, in order
1. **Finish JPMorgan's merge** (it is ~90% done: volume + nine registers exist). 23 `PROV-JP1-*` source ids were
   never minted; `CORRECTIONS.md` missing; `_MANIFEST.md` is a 35-word stub; no merge report.
2. **Finish Cigna's repair** from `cigna_s1_audit1.md`: the blocker is that a held byte DOES print the
   registrant's incorporation date (`sources/sec/0001140361-18-024107_s002268x1_s4.htm` l.48371 — "(Originally
   incorporated on March 6, 2018 under the name Halfmoon Parent, Inc.)") while the volume claims the opposite in
   eight places; the `corrections` gate still fails, which is proof the propagation is incomplete. Verify every
   item yourself — the auditor published that 8 of its 12 residual misses were its own false positives.
3. **Audit the 7 unaudited merged volumes** (GM, AT&T, CVS, J&J, PepsiCo, Boeing, Meta) against
   `03_quality_control/AUDIT_BRIEF_SHARED.md`. Their report files are stubs; nothing has been judged.
4. **Merge the ready parts** (Cencora, Verizon, UPS, Centene, FedEx), then close Humana's 5 and Dell's 2
   PENDING blocks and merge those two.
5. **Then certify** companies whose audits pass — a certifier who is neither author, merger, auditor nor
   repairer.
6. **Then** author the tail: probe first where no dossier exists, else author Stage 1 at **the tier the probe's
   own dossier issues** (never the tier anyone tells you it should be — §15.2 counts families, not prose).
7. Standing debts: task #15 secondary-print intake (the reason `quotes` still reports unmatched spans),
   task #31 the `S4222-S4229` id-namespace decision (decide it; never blind re-key), task #22 Walmart
   re-certification, task #29 Microsoft repair (46 findings, 5 HIGH, never dispatched), task #26 prove the
   Chronicling America endpoint from CI egress.

## 6. Hazards that will bite you specifically
- **A ticker maps to the surviving registrant, not the famous one.** XOM→2115436 while historic Exxon is CIK
  34088; Comcast's index floor is 2002; Morgan Stanley = Dean Witter; Cigna = a 2018 shell; AT&T = SBC;
  Marathon = MPC Holdings; Verizon = Bell Atlantic/NYNEX; Wells Fargo's legal survivor was Norwest. Resolve
  ancestors by CIK and check EDGAR's `FORMER CONFORMED NAME` dates for renames.
- **A pre-1994 silence is a perimeter, not an empty archive** (EDGAR's floor is ~1993-94). Same for a YEAR
  facet, a slice cap, a name-only matcher, or an unfetched family. Four of the corpus's five evidence families
  are (a) filings, (b) web archives, (c) periodicals, (d) digitised corporate print; family (e) auction/museum
  has **no tool** → report it UNTRIED, structurally, forever, never as a null.
- **False nulls live in correction markers** (RD-139: `COR-22` asserted "0 occurrences" while four held layers
  printed the phrase). Grep before you assert, and re-check the marker, not just the claim.
- **Tier caps are density targets, not file limits.** 60,000 words per volume is the only word count that is a
  defect (§9.2/9.3); splits happen at section boundaries, never by renumbering. Over a tier target = advisory.
- **Report paths are repo-root-relative in prose but must be written in full:** `founders_playbook/
  03_quality_control/<file>.md`. A stray repository-root `03_quality_control/` existed and was consolidated;
  `_lane_scratch/` holds 11 dumped census/probe logs. Do not re-create the root dir.
- **`MASTER_RESEARCH_LOG.md` is the durable memory** (entries RD-1…RD-145; RD-143 = the quota wipe, RD-144/145 =
  the `core.autocrlf` provenance defect and my own wrong-direction fix). Append an entry for every defect you
  find, including your own. `RESUME_HANDOFF.md` §1-§4 and `00_universe/_AUTHOR_WAVE_PLAN.md` carry the wave
  plan, the resume batch table and the standing hazards.
- **Do not touch the user's foreground browser** or pop windows: run long commands in the background; use a
  dedicated browser profile only if browser work is explicitly required.
- The QCA PAT must live only at `~/.qca/pat` (mode 600), never be committed or echoed; there is no `gh auth` —
  use anonymous public endpoints, and never extract the machine's stored git credential.

## 7. What "done" looks like
Per company: a `stage_1.md` (+2/3 later), nine registers with byte-identical headers to `company_001_amazon`,
`CORRECTIONS.md`, `_MANIFEST.md` with re-measured live counts, a five-family table that distinguishes
ANSWERED / RETURNS-NOTHING-WITH-PERIMETER / UNANSWERED / UNTRIED, gates passing with no substantive findings,
an audit from a different agent, and a certification signed by a fifth role — plus an honest list of what was
never tried and the route that would answer it.

Start by telling the user what you measured on disk (don't trust this prompt's numbers — verify them), then
propose step 1 and ask before dispatching any wave of subagents.
