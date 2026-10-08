# RESUME HANDOFF — read this first if you are starting this project cold

**Current block: 2026-10-08 ~04:30 IST (supersedes every section below it; the 09-23/24/25/30 blocks are kept as
history and are KNOWN-STALE in their status columns — do not quote them).**

## 1. State, measured from disk this hour

**The run stopped on a provider quota wall, not on a defect.** At ~04:00 IST on 2026-10-07/08 two platform
events killed every lane that was in flight: first `Queuing failed` (10 lanes, ~233 min into their runs), then
`You've reached your daily usage limit for Chat` (the remaining 8). **All locks are released** (`ledger` shows
nothing un-done), so tomorrow starts with an empty lane board and unwritten work that is still on disk.

**Stage 1 merged: 19 volumes, 734,262 words, 4,274 register rows** (measured, root registers unless noted):

| volume | words | rows | | volume | words | rows |
|---|---|---|---|---|---|---|
| amazon (SIGNED) | 50,814 | 1,315 | | gm | 20,192 | 114 |
| walmart | 59,516 | 349 | | att | 31,315 | 136 |
| apple | 57,502 | 186 (in `research/`) | | target (**CERTIFIED**) | 42,833 | 173 |
| alphabet | 57,358 | 169 | | tesla (**CERTIFIED**) | 55,347 | 210 |
| unitedhealth | 44,996 | 230 | | jnj | 27,043 | 102 |
| microsoft | 34,707 | 127 | | pepsico | 22,958 | 106 |
| jpmorgan | 34,637 | 214 | | boeing | 34,817 | 211 |
| costco | 46,992 | 191 | | cvs | 19,520 | 126 |
| nvidia | 46,691 | 194 | | cigna | 16,812 | 78 |
| meta | 30,212 | 120 | | | | |

**Certified: 2** (Tesla, Target) + Amazon signed. **Audited: 1** (Cigna — FAILED with 1 blocker + 8 findings;
its repairer got ~78 tool calls in and died holding 12 paths: `stage_1.md` is now 16,812 w with "March 6, 2018"
printed 3× and 13 COR entries, but the sentence "No held byte prints…" still survives in **2 places**, and
`cigna_s1_repairs.md` is an empty stub. Resume = verify-then-finish, not restart).

**Merged but never audited (7):** GM, AT&T, CVS, J&J, PepsiCo, Boeing, Meta — all five audit dispatches died
with report files at 35-word stubs. **The bytes are intact; only the judgment is missing.**

**Parts complete, awaiting merge (6):** Cencora 14,916 w (0 pending), Verizon 17,293 w (0), UPS 12,215 w (0),
Centene 10,268 w (0), FedEx 5,516 w (0, thin), Dell p1 28,786 + p2 32,398 (2 pending). JPMorgan's merge died
AFTER writing volume + all nine registers: 23 `PROV-JP1-*` source ids were never minted, and `CORRECTIONS.md`,
`_MANIFEST.md` content and both reports are missing.

**Authors that died before writing anything (4):** Cardinal (nothing), Marathon / Valero / Wells Fargo (35-word
stubs). Elevance reached 3,481 w. Boeing's `CORRECTIONS.md` is missing even though its merge reported 211 rows.

**Untried/unprobed tail (21 companies with no volume and no part):** berkshire, mckesson, exxonmobil, bofa,
chevron, ford, citigroup, homedepot, fanniemae, kroger, phillips66, stonex, statefarm, freddiemac, goldman,
comcast, morganstanley, disney, rtx + the six needing a probe first (mckesson, fanniemae, phillips66, stonex,
statefarm, freddiemac).

## 2. Tools (all stdlib, all self-testing — use these, do not re-invent them)

| tool | what it owns | verified form |
|---|---|---|
| `tools/sec_intake.py` | EDGAR index/facts/grab/auto, provenance sidecars, registrant guard | `auto "Registrant Name" --company-dir <dir> --from --to --max-docs 30` (walks **every** slice now; prints `walk: … date perimeter`) |
| `tools/fleet_intake.py` | the scripted tail: in-window pass + **forward recital pass** | `--only slug,slug` / `--all` / `--no-recital` / `--dry-run` (writes nothing) |
| `tools/legacy_cik.py` | predecessor CIK lookup + authoritative name/perimeter | `search "name root"` / `detail 34088 1166691` |
| `tools/harvest_mine.py` | mines the local harvest index into `research/A4_*.md` | `--company <slug> --limit 12 --max-mb 25`; `--self-test` = 9 controls |
| `tools/periodical_harvest.py` | live CA/Hathi/GB/IA queries | `--facet-free --source-family corporate_print --max-requests 220 --delay 2.5` |
| `tools/ia_text.py` | Internet Archive text layers, per-volume paths | `list-files --id <id>` (the documented `list-files <id>` exits `unrecognized arguments` -- PepsiCo proved the route works), `<id> --file <name>` |
| `tools/merge_census.py` | what a merge asked for vs what landed | `--company-dir <dir> --verbose` |
| `tools/id_mint.py` | central source-id allocation, never into a gap | `--count N --company <dir> --claim --agent <name>` |
| `tools/gates.py` | csv/keys/anchors/quotes/budget/corrections | `--company-dir <dir> --out <file.md>` -- `--tier auto` is the default and now **binds a tier to the stage that issues it**, reading per-stage table rows and `Stage 1 -- T2 core` bullets (RD-142: stop telling agents to pin `--tier core`); `--self-test` = **25 controls, PASS** |
| `tools/cdx_intake.py` | family (b) Wayback CDX enumerate + fetch, four-state honesty, sha256 sidecars, no-clobber `_v2` | `--self-test` = 37 checks 0 defects; slugs present in `tools/web_domains.json`: centene, cencora, elevance, marathon, microsoft, target -- **an absent slug means UNTRIED, never a null** |
| `tools/scaffold.py` | path ownership | `claim/section/touch/release/status`, and `release --agent X --all` frees a dead agent's locks |

## 3. Standing hazards (each one cost work this week — verify before you trust)

1. **A listing truncated by `head` is not a census.** I re-dispatched three Amazon Stage-3 audits that already
   existed (RD-135). Count with `wc -l` or grep the exact pattern.
2. **The ticker maps to the wrong legal person.** `XOM → CIK 2115436` (a 2026 holding company), while the
   historic registrant is `34088 EXXON MOBIL CORP`. Comcast's index floor is 2002 for the same reason. If a
   filings family comes back empty after a TICKER resolution, re-resolve by registrant NAME.
3. **The YEAR facet class is not dead.** `--facet-free` initially stripped only `q`; corporate-print tasks carry
   `year_range`, so 100 of 188 faceted queries stayed faceted behind a log line claiming otherwise. Verify a
   transform by re-reading one output URL, not by its printed count.
4. **Dead agents keep their claims.** `scaffold.py status` is the authority on ownership, never my recollection.
5. **`merge_census` cannot attribute `validation.csv` vs `failures.csv`** (identical schemas) and cannot see
   `research/*.csv` emissions. Every merge must hand-attribute those and say how.
6. **Enumerate a CSV header before reading a field.** Never assume `query_label`, `period_or_date`, `source_query`.
7. **Never `git add -A` while agents and script lanes hold writers**; never commit a file a lane is rewriting.
   Pull/merge can fail with 100+ dirty files mid-lane — wait for the lane, then pull (never force).
8. **A report that says "verified from disk" is itself a claim** — re-measure after the last write.
9. **A repository-root `03_quality_control/` exists and is a mistake** (nine gate reports landed there because
   briefs wrote the path without the `founders_playbook/` prefix). The canonical home is
   `founders_playbook/03_quality_control/`. Don't write to the root one, don't delete from it while an agent may
   hold a path inside it, and put the full path in every brief.
10. **Never release another agent's claims because a notification told you it stopped.** `merge-meta` finished
    and released its own paths while I was freeing them under it; `s1-dell-p2` died at its turn ceiling and its
    claim was still LIVE with a 70-minute heartbeat, so the finisher I dispatched correctly refused the write
    and reported the refusal. `scaffold.py ledger` is the authority on ownership — check the row, then release.
11. **`gate_quotes` counts project-internal matches separately as of RD-142** (`matched-in-project-text-only N`).
    That removed the permanent false advisory, so spans left unmatched are now more often the real class: under a
    25% miss rate the finding is `verbatim` and **substantive** (CVS and Meta flipped from advisory to defect
    exits for exactly this reason). The right response is still never to rewrite a quotation to force a match —
    quote an unsaved secondary print is a known intake gap (task #15), and an auditor decides, not a repairer.

## 4. Next actions, in order (written for the first hour after the quota resets)

**Budget discipline, learned the expensive way tonight:** I ran 18-20 concurrent lanes and the provider killed
all of them in two waves (~4.3M tokens consumed with no reports written). **Cap at 10 lanes, and prefer lanes
that convert existing bytes into certified data over lanes that create new bytes.** Every number below is a
measured disk fact, not a plan-of-record.

1. **Finish JPMorgan's merge** (highest value per call: volume + 214 rows already exist). Mint the 23
   `PROV-JP1-*` source ids, write `CORRECTIONS.md` + `_MANIFEST.md` live counts + the merge report, re-run
   `merge_census.py` to prove 0 missing keyed rows, then gates. ~1 agent, no retrieval.
2. **Verify-then-finish Cigna's repair** against `cigna_s1_audit1.md` (B-1 + F-2..F-9). Check the 2 surviving
   "No held byte prints…" sentences, the propagation `--checks corrections` proves, and write
   `cigna_s1_repairs.md`. A different agent certifies afterwards — certifier ≠ repairer ≠ auditor ≠ merger.
3. **Audit the 7 unaudited merged volumes** (GM, AT&T, CVS, J&J, PepsiCo, Boeing, Meta) using
   `03_quality_control/AUDIT_BRIEF_SHARED.md`. Each report is currently a 35-word stub, so nothing is lost by
   re-dispatching; expect a FAILED verdict on most — the repairers are the real cost and they must not be the
   auditors.
4. **Merge the 6 ready parts** (Cencora, Verizon, UPS, Centene, FedEx, Dell). Dell's merge must take the UNION
   of p1's `U.101–U.111` and p2's declarations without renumbering either, and finish p2's 2 pending blocks
   first; Humana's part has 5 pending blocks — close them before merging; Elevance needs ~4.5k more words.
5. **Boeing `CORRECTIONS.md` is missing** although its merge reported 211 rows applied — check whether the
   merge wrote corrections into the volume only, and repair the bookkeeping, not the evidence.
6. **Then** the 21 unvolumed companies, six of which need a probe first (mckesson, fanniemae, phillips66,
   stonex, statefarm, freddiemac), and the standing debts: task #15 secondary-print intake (now the reason
   Meta/CVS still show `verbatim` quote findings), task #31 the `S4222–S4229` Microsoft/Target collision,
   task #22 Walmart re-certification, task #29 Microsoft repair (46 findings, 5 HIGH, never dispatched),
   task #26 the Chronicling America endpoint proof from CI egress.
7. Consolidate the stray repository-root `03_quality_control/` (18 untracked files, 3 name-collisions with the
   canonical dir) **once no lane can hold a path in it**, and keep `--out` paths fully prefixed in every brief.
