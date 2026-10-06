# RESUME HANDOFF — read this first if you are starting this project cold

**Current block: 2026-09-30 ~02:15 IST (supersedes every section below it; the 09-23/24/25 blocks are kept as
history and are KNOWN-STALE in their status columns — do not quote them).**

## 1. State, measured from disk this hour

**Stage 1 merged (8):** Amazon 50,814 w **SIGNED**; Walmart 59,516 w (re-cert pending, task #22); Apple 57,502 w;
Alphabet 57,298 w (merge agent live as I write); UnitedHealth 44,996 w, 230 rows, audit 1 running; Microsoft
34,707 w, 127 rows, **audits 1+2 in → 46 findings / 5 HIGH, repair not yet dispatched** (task #29); Target
41,534 w, **172 rows** (conflicts 18 — *not* 23, my earlier figure was wrong and is corrected in RD-135),
repair pass 2 closed 5 blockers, re-certifier live; **Tesla 53,553 w, 208 rows, anchors 23↔23, audit 1 running**.
Costco and Nvidia merges were live at 01:00 — check their notes files before re-dispatching anything.

**Probes landed (17):** Berkshire, Boeing, Kroger, Disney, J&J, Chevron, GM, Citigroup, Ford, JPMorgan,
Comcast, Goldman, PepsiCo + the tranche running now (Cencora, Cigna, Elevance, Humana, Verizon, UPS, FedEx,
Marathon, Cardinal, CVS, RTX, Wells Fargo, AT&T, BofA, Home Depot, Morgan Stanley, Valero, ExxonMobil, Centene).

**Unprobed tail:** `fanniemae, stonex, phillips66, statefarm, freddiemac, dell, meta, ups(landed), rtx(in)` —
plus the **re-grade wave** for the ten companies whose filings verdict was taken under the 8-slice cap RD-134
removed: `jpmorgan, citigroup, gm, chevron, disney, boeing, kroger, jnj, berkshire, ford`.
Full held briefs: `00_universe/_DISPATCH_QUEUE.md`.

## 2. Tools (all stdlib, all self-testing — use these, do not re-invent them)

| tool | what it owns | verified form |
|---|---|---|
| `tools/sec_intake.py` | EDGAR index/facts/grab/auto, provenance sidecars, registrant guard | `auto "Registrant Name" --company-dir <dir> --from --to --max-docs 30` (walks **every** slice now; prints `walk: … date perimeter`) |
| `tools/fleet_intake.py` | the scripted tail: in-window pass + **forward recital pass** | `--only slug,slug` / `--all` / `--no-recital` / `--dry-run` (writes nothing) |
| `tools/legacy_cik.py` | predecessor CIK lookup + authoritative name/perimeter | `search "name root"` / `detail 34088 1166691` |
| `tools/harvest_mine.py` | mines the local harvest index into `research/A4_*.md` | `--company <slug> --limit 12 --max-mb 25`; `--self-test` = 9 controls |
| `tools/periodical_harvest.py` | live CA/Hathi/GB/IA queries | `--facet-free --source-family corporate_print --max-requests 220 --delay 2.5` |
| `tools/ia_text.py` | Internet Archive text layers, per-volume paths | `list-files <id>`, `<id> --file <name>` |
| `tools/merge_census.py` | what a merge asked for vs what landed | `--company-dir <dir> --verbose` |
| `tools/id_mint.py` | central source-id allocation, never into a gap | `--count N --company <dir> --claim --agent <name>` |
| `tools/gates.py` | csv/keys/anchors/quotes/budget/corrections | `--company-dir <dir> --tier auto --out <file.md>`; `--self-test` = **18 controls, PASS** |
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

## 4. Next actions, in order

1. When the CP facet-free pass lands, re-run `harvest_mine` for the companies whose CP rows changed, then close
   task #28 with measured row deltas.
2. Dispatch the Microsoft repair (task #29) once audit 3 lands, then a certifier that is neither repairer nor
   author. Target re-certification is running; Walmart #22 still waits.
3. Dispatch the held briefs in `00_universe/_DISPATCH_QUEUE.md` as slots free (**the cap is 20 concurrent
   subagents, and background scripts count toward it — budget to ~14 agents**), then the ten re-grades.
4. Resolve task #31: `S4222–S4225` denote different documents in Microsoft's and Target's `sources.csv`.
   Do NOT blind re-key — decide the id namespace first (RD-122's 138-dangling-site lesson).
5. Amazon Stage 2/3 are signed-to-audited; the remaining Amazon debt is the Stage-2 numbers/hindsight/adversarial
   re-checks and Stage-3's citation residue (tasks #5/#9/#10 are stale labels — read
   `03_quality_control/amazon_s3_*` before opening any of them).
6. Commit and push after each lane finishes; the nightly harvest workflow keeps pushing to `main`, so pull
   before pushing.
