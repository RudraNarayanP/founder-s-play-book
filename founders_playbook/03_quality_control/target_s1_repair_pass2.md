# target_s1_repair_pass2.md — Stage-1 REPAIR pass 2 (second successor), company_042_target

Agent `target-repair-2`. I own the Target repair paths and the write set named in my brief. **I did not
edit any corpus file that carries a live claim** (see `HELD-PATH CLAIM` below); every "what landed" line
is measured from the bytes on disk, not inherited from the certification, the audits, or `MASTER_RESEARCH_LOG`.
Method read first: `00_METHOD_AND_STYLE.md` §13, §14 (rules 4/6/8/9/10/11/12), §15.2/15.5/15.6;
`MASTER_RESEARCH_LOG.md` RD-123/127/128/130/132 (treated as a **history of claims**, several refuted);
`target_s1_certification.md` (the work order) and the three Target audit sheets; `tools/scaffold.py`,
`tools/gates.py`. Web calls used: **0**.

STATUS: WRITTEN 2026-09-30, agent `target-repair-2`. **Do not treat this file as a certification** — I am
the repairer; re-certification must be a different agent (§15.6).

---

## 0. DISK-STATE ESTABLISHED (what the dead `target-s1-repair2` had already landed)

The previous repair agent (`target-s1-repair2`) scaffolded its own log
`03_quality_control/target_s1_repairs2.md` but **wrote nothing into it** (242 B, 35 words, banner only,
claimed 2026-09-29T18:08:35Z). It *did* land corpus edits, all still uncommitted against the certification
commit `1a8f4f5 "Target Stage 1 NOT-CERTIFIED: 5 blockers"`:

```
CORRECTIONS.md          +363 lines  (opened COR-15 … COR-20)
stage_1.md              +264 lines  (grew to 41,534 w; B-1/B-2/B-3 prose legs)
quantitative.csv         +81 / -?   (68 → 72 rows; B-1 FY1966 row + PERIOD BASIS re-tags)
sources.csv              +24 lines  (21 → 25 rows; S4222-S4225 added, tiers/notes rewritten)
_MANIFEST.md             +44
stage_1_index.md         +39
data_gaps.csv            +16        (U.021 re-scoped, U.032 expectation withdrawn)
_INDEX.md                +22        (source-of-truth over-reach reworded)
conflicts.csv             +2 / -2   (one row edited; count unchanged at 18)
timeline.csv              +4 / -4   (row 17 fiscal-year note)
```

So the dead agent had already **substantially landed** blockers 1, 2, 3, 4(first leg) and certifier B-1…B-5(f),
but left no report and, critically, **left 14 scaffold claims LIVE and unreleased** (see §11).

Baseline vs the certifier's own measurements (what I re-measured, not trusted): the certifier read
sources.csv 21 / quantitative 68 / stage_1.md 38,489 w / 14 COR ids. Disk now: sources.csv **25** /
quantitative **72** / stage_1.md **41,534 w** / **20** COR ids.

---

## 1. BLOCKER 1 — Tier-1 error/apology pages registered as sources (S4218–S4221 class)

**Verdict: CLOSED — landed by the dead agent, verified by me against the bytes and citations.**

*Detection by content (my measurement this pass):*
- `sources/name_search/dayton+hudson.atom` (7,747 B) → SEC HTML error page: visible tokens `temporarily`,
  `500`; **no `503`**, no status line captured, no sidecar. Same shape for `dey+brothers.atom`,
  `goodfellow.atom`, `target+corporation.atom` (all 7,747 B).
- `sources/web_archive/cdx_dhc.txt` / `cdx_targetcom.txt` (11,832 B each) → `Internet Archive: Temporarily
  Offline` HTML, prints `500`, not `503`; no sidecar.
- `sources/sec/_MANIFEST.csv` (40 B) → one header line, zero data rows.

*What landed (dead agent):* all four rows are now **tier 3** with honest classes — S4218 `UNANSWERED - dead
route`, S4219 `INDEX FLOOR - not a null`, S4220 `UNANSWERED - dead route`, S4221 `MANIFEST OF AN EMPTY
WINDOW`; each `independence_note` says it is a **route** artifact, never an absence ("not a source of facts
and never citable as an absence"). **COR-19** ("four Tier-1 stamps on retrieval artefacts, and the claims
that hid behind them", opened 2026-09-30) covers the re-tier. S4221's **invented quote** is fixed:
`relevant_passage` now reads `accession,file,…,status (the whole file: this header line and nothing else)`
followed by `NOT-A-QUOTE: the run's statement "0 documents stored, 0 skipped/unanswered" describes this
file and is NOT text printed in it - COR-19 withdraws …` — verified against the 40-byte carrier.

*Citation re-check (mine):* S4218/S4219/S4220/S4221 are cited only in route/absence contexts
(`data_gaps.csv` U.025/U.026/U.005/U.027, `stage_1_index.md` mint map, `CORRECTIONS.md` COR-19/20). No live
register row now treats any of them as a Tier-1 fact carrier. The old "independent of the company" swap on
S4217 was also re-worded (now "registrant's own index … CANNOT witness anything before its own floor").

*Residual (reported, not forced):* the 503-vs-500 question is still **UNVERIFIABLE from bytes** (no sidecar
captures the status line) — this is a *provenance* gap (see §FETCH REQUESTS), not a tier error.

## 2. BLOCKER 2 — a scanner used as a second lineage (S4211)

**Verdict: CLOSED — the independence *claim* was fixed, the id kept (correct: "fix the claim, not the id").**

S4211 (FY1975 layer) `independence_note` now reads, verbatim from the register: `NO independent lineage: a
third party that SCANNED a company's own report is a conduit, not a second origin … it sits inside the
eleven-layer single lineage this volume already states. COR-19 WITHDREW the former note (digitised by a
third-party backfile service not by the company) … and the row's claim_supported no longer reads context
only, because timeline.csv row 17 now rests its Fiscal Year fact on this layer (COR-08).` This resolves the
certifier's B-5(f) outbound leg (S4211 `claim_supported` = `context only` while timeline row 17 relied on
it) **and** the audit-2 worst lineage defect. Verified against `sources/corporate_print/1975_dayton_hudson_djvu.txt`
masthead. Propagated: S4211 cited 12× across the corpus (stage_1.md ×2, timeline row 17, CORRECTIONS ×6).

## 3. BLOCKER 3 — held-but-uncited files (≥19 docs incl FY1998/FY2000 that U.026 depends on)

**Verdict: CLOSED at the citation layer — this is the highest-value finding and it was mostly landed before
I arrived; I confirmed it from disk and it holds.**

Re-enumeration per §14 rule 11 (list `sources/` at close, account for every doc). `sources/` = **51 files =
36 content docs + 15 `.meta.json` sidecars**. Audit-2's baseline was **8 content docs named by no row** and
**19 files carrying no provenance sidecar**. Measured now: **every one of the 36 content docs is named by a
`sources.csv` row AND its basename appears in the 15 corpus/instruction files → 0 uncited content docs.**

The 4 previously row-less FY1998/FY2000/derived/corporate layers were registered by the dead agent:
**S4222** (5 `ia_search` bodies, Tier 3), **S4223** (derived EDGAR trio incl. `_INDEX.md`, Tier 2),
**S4224** (FY1998, Tier 1 `(PB)`, U.026 digital-history leg), **S4225** (FY2000, Tier 1 `(PB)`, U.026).
`data_gaps.csv` U.026 now cites S4224/S4225 rather than asserting the layers uncited. I re-verified the two
U.026 strings the audit flagged: `www.dhc.com` is printed in the FY1998 layer and `Target Corporation Annual
Report 2000` in the FY2000 layer — the facts were always real; only the *rows* were missing. No second-hand
figure substituted; no null asserted before the corpus finished growing. Full per-file disposition: §12.

## 4. BLOCKER 4 — `_INDEX.md` over-reach + missing TLS/provenance stamps

**Verdict: CLOSED. First leg (over-reach) landed by the dead agent; second leg (TLS/provenance stamps) is
the repair I personally applied** — the only owned write-target that was both **free of a live claim** and
**not yet done**.

- *Over-reach (dead agent, COR-20):* `sources/_index/_INDEX.md` no longer says "this file is the source of
  truth." Corpus-wide grep for `source of truth`: 5 hits, all in **negation or retraction** ("It is NOT a
  source of truth"; COR-20 quoting the withdrawn wording; the `stage_1.md` merge note). The header now
  bounds itself to CIK 27419 from 1994-02-10, names what it cannot answer (pre-1994, predecessor CIK →
  U.025/U.036 open), and how it goes stale. Correct.
- *TLS/provenance (mine, this pass):* I appended a measured **"Provenance and transport"** table to
  `_INDEX.md` recording that the four `_index` bytes it summarizes (`raw_submissions…json` 149,561 B = S4217;
  `submissions.json` 576,114 B, `submissions.csv` 237,026 B/2,628 rows, `_INDEX.md` = S4223) carry **no
  `.meta.json` sidecar** → transport UNSTAMPED; and stating that the sidecars that **do** exist (15 layers:
  **10 `verified TLS`, 5 `UNVERIFIED TLS`** — FY1966/67/71/73/74, U.028) are stamped in the citing
  `sources.csv` rows, not restated here. Every byte figure in that block was re-read from the carrier/`stat`
  this pass, not copied from audit-2. §14 rule 4 honoured: appended, did not erase the dead agent's reword.
  (`_INDEX.md` 3,699 B → 1,008 words after my write; re-measured in §13.)

## 5. BLOCKER 5 — the certifier's fifth listed blocker (B-5, the minor list a–f)

**Stated before fixing, per my brief.** The certifier's fifth blocker is **B-5**, six minor legs:

- **(a) COR-07 six-vs-eight date count.** COR-07's table cell (CORRECTIONS.md:20) said the withdrawal
  covered "**six** `date` cells"; measured **seven** quantitative rows (r54-r60) + one timeline row = eight.
  *Landed by dead agent:* CORRECTIONS.md now prints "**seven December year-ends**" for the quantitative leg
  and stage_1.md:1493 states the split ("1973-12-31 ×4 + three singles"); `stage_1.md` still also carries a
  "**six December**" phrase in the emission-slice prose (a superseded slice, now marker-flagged under B-2).
  The two *layers* now agree that the register leg is seven (quantitative) + one (timeline) = eight. **RESIDUAL:**
  one "six December" phrase survives in a superseded slice — on held paths (`stage_1.md`/`CORRECTIONS.md`),
  **not forced**.
- **(b) COR-08 / timeline row 17 locator `L3246-3250` vs `L3251`.** `consisted of 52 weeks.` is L3251.
  *Partially landed:* `stage_1.md` and `CORRECTIONS.md` now also carry the corrected **`L3246-3251`** (2 hits
  each). **RESIDUAL:** `timeline.csv` row 17 still cites **`L3246-3250`** (1×, no `L3251` variant) — held
  path, **not forced**. (Re-verified: `1975_dayton_hudson_djvu.txt` L3246-3251 prints the six-line Fiscal
  Year note; the tail line is L3251.)
- **(c) P2-07 / P2-10 quote fidelity.** P2-10's corrupt label `SOLS AMIS)` is now **shown** in `stage_1.md`
  (measured present) — the §K.3/register disagreement is resolved. **RESIDUAL:** P2-07's OCR join at 1965
  `L1354-1355` still has **no `[L1354|L1355]` locator bracket** and the P2 preamble is not re-labelled
  "verbatim digits, normalized labels" (measured: `[L1354` = 0, "normalized label" preamble = 0) — held
  path, **not forced**.
- **(d) U.031 route-state.** *Landed:* the U.031 `why_missing`/`best_available_evidence` now names the route
  state (**"untried"** — measured present), matching U.030/U.032/U.036.
- **(e) `_parts/s1_p2.md` calls §I–§U "volume 1".** `_parts/s1_p2.md` still reads "**volume 1**" 2×; it does
  carry one superseded footer already. **NOT FIXED by me:** `_parts/*` is **not in my owned write set** and is
  a superseded audit-trail file (§14 rule 4: "nothing is a cleanup target"; §15.6/merge). Handed to re-cert
  as documentation debt; I did not append there.
- **(f) Outbound sources.csv legs (S4203 `(L1952)`, S4209 circular self-citation).** *Landed & verified:*
  S4203 `relevant_passage` now places the locator **outside** the quoted span — `JOHN F. GEISSE / Senior Vice
  President … [locator L1952-1956, placed OUTSIDE the quoted span per method 14 rule 12 …]` — and the
  possessive `Target’s` is restored in the passage; `(L1952)` inside the quote = 0. S4209 `source_title` and
  `independence_note` no longer open with the stray `U ` / self-circular `same lineage as S4208/S4209` (the
  note now names S4201-S4211 lineage and flags the former circular cell as withdrawn). The `U ` seen on
  S4219/S4220 titles is a § symbol / list bullet rendered by the cp1252 console, **not** corpus corruption
  (non-ASCII codepoints in sources.csv are only U+2014 em-dash, U+2019 apostrophe, U+00A7 §; **0 × U+FFFD**).

**Net:** B-5(c)/(a)/(b) have small residuals, all on **live-claimed** files; B-5(d)/(f) landed; B-5(e) is
out of my scope. None is blocking; none required a second-hand figure.

## 6–9. Inherited work-order blockers 1–4 — status recap

BLOCKER 1 CLOSED (§1) · BLOCKER 2 CLOSED (§2) · BLOCKER 3 CLOSED (§3) · BLOCKER 4 CLOSED (§4).

## 10. GATE — BEFORE / AFTER (measured from disk)

- **BEFORE (certifier, quoted from `target_s1_certification.md`, `--tier core --fail-on substantive`):**
  Findings **1** | Passes 20; the single finding = `budget` 38,489 > core cap 22,000. It saw **none** of the
  5 blockers. (The three audits' gate runs are separately quoted in each audit sheet.)
- **AFTER (my run, briefed cmd `python tools/gates.py --company-dir …company_042_target --tier exemplar`):**
  Findings **1** | Passes 21, rc=1. The one finding is `quotes` **ADVISORY** ("2 of 2 checked spans
  unmatched, 100% — gate precision not established, treat as triage list, NOT as defects"); its 2 evidence
  lines and 15 unattributed spans all sit in `stage_1.md`, a **held** path. `corrections` now reads **20
  retraction ids; register layer reaches 20, volumes 20**; all `S####` resolve; **37 ↔ 37 anchors**;
  `budget` **passes at exemplar cap 60,000** (41,534 < 60,000). Output saved to
  `03_quality_control/target_s1_gates_pass2.md`.
  *Note on the briefed `--out`:* `gates.py` treats `--out` as an **output directory** and writes
  `gates_company_042_target.md`/`.json`; passing `…/target_s1_gates_pass2.md` would `mkdir` a `.md`-named
  folder. I captured stdout to that path instead so the artifact is a file, not a directory. Tool/brief
  mismatch, logged — no evidence trimmed (§15.4).

## 11. HELD-PATH CLAIM — why I did not write most corpus files

My brief said "the dead agent's claims expired." **On disk they have not.** `tools/scaffold.py` has **no
`status` subcommand** (the equivalent is `ledger`); the ledger + raw JSON show **14 unexpired LIVE claims**
held by the dead agent `target-s1-repair2`, all heartbeat 2026-09-29T18:08Z, **ttl 240 min**, and the clock
at my measurement (~2026-09-30T19:0xZ on the box clock / ledger age ≈ 55 min) is **inside** the TTL. An
attempted `claim` on `stage_1.md` **REFUSED (rc=3)**: *"claimed by 'target-s1-repair2' (heartbeat 51 min
ago, ttl 240 min). One path, one owner."* Per my instruction ("If a live claim shows on a path you want,
hold that path and say so; do not force it") I **held**. Forcing is doubly unsafe here because
`scaffold claim --force` would **overwrite** the 41,534-word `stage_1.md` with an empty skeleton, and the
dead agent's repairs are already largely correct, so re-applying would double-apply fixes.

**Held (LIVE, not written by me):** `stage_1.md`, `stage_1_index.md`, `_MANIFEST.md`, `CORRECTIONS.md`,
`sources.csv`, `quantitative.csv`, `timeline.csv`, `conflicts.csv`, `data_gaps.csv`, `validation.csv`,
`failures.csv`, `decisions.csv`, `channels.csv`, and the dead agent's own `target_s1_repairs2.md`.
**Free & used by me:** `sources/_index/_INDEX.md` (provenance section), `sources/**` bytes (none needed,
web=0), this log, and the gate output. `tools/` and `MASTER_RESEARCH_LOG.md` are outside every agent's
write scope.

## 12. HELD-BUT-UNCITED — 36 content docs, one-line disposition each

All 36 are named by a `sources.csv` row **and** cited in-corpus (measured 0 uncited). The 19 audit-2
"no-sidecar" files are the non-`.txt` route/index artifacts (8 `name_search` + 6 `ia_search` + 4 `_index` +
1 `sec`) plus the 2 `web_archive/cdx_*.txt`; only `.txt` carriers get `.meta.json` sidecars, and 15 of 17
do (the 2 without are the cdx bodies — see FETCH REQUESTS).

FY1965 S4201 cites A01-A04/B01-B05/F01 etc. · FY1966 S4202 cites U.012/P2-08 (UNVERIFIED TLS, capped) ·
FY1967 S4203 cites B02/86,901,007 + **now the 60,731,468 FY1966 base (B-1)** · FY1968 S4204 cites
189,515,025/r18 · FY1969 S4205 cites Q6/Q15 · FY1970 S4206 cites B05/first-offering · FY1971 S4207 cites
Q7/Q8 (UNVERIFIED TLS) · FY1972 S4208 cites Q9/Q14/Q18 · FY1973 S4209 cites P2-10/Q16-Q19 + §K.3 (SOLS AMIS
shown) · FY1974 S4210 cites U.012 roster (UNVERIFIED TLS) · FY1975 S4211 cites timeline row 17 (conduit note)
· FY1998 **S4224** (NEW) cites U.026 digital-history, `www.dhc.com` verified in bytes · FY1999 S4212 cites
U.001 pre-history (Low, capped) · FY2000 **S4225** (NEW) cites U.026 readoption, masthead verified in bytes ·
CSA1963 S4215 cites H01/N1 null ("does not name the company once") · `meta_01-target-archive.json` S4216
cites A04/N7 (61 DjVuTXT/17 PDF verified) · `raw_submissions` S4217 cites Boundary 1 (floor 1994) ·
`submissions.json/.csv/_INDEX.md` **S4223** (NEW) derived index, registrant-line only · 4 `*.atom` **S4218**
(NEW) SEC error pages, Tier 3 · 4 `fts_*.json` **S4219** (NEW) index-floor zeros, Tier 3 · 2 `cdx_*.txt`
**S4220** (NEW) IA-offline pages, Tier 3, **no sidecar** · `sec/_MANIFEST.csv` **S4221** (NEW) empty-window
manifest, NOT-A-QUOTE fixed · 5 `ia_search` bodies **S4222** (NEW) periodical-route evidence, Tier 3.

## 13. REGISTER DELTAS (row deltas, re-measured after my last write)

| register | certifier baseline | disk now | delta | by |
|---|---|---|---|---|
| sources.csv | 21 | **25** | +4 (S4222-S4225) | dead agent |
| quantitative.csv | 68 | **72** | +4 (FY1966 60,731,468 base + restatement/PERIOD BASIS rows) | dead agent |
| timeline.csv | 24 | **24** | 0 (row 17 rewritten) | dead agent |
| conflicts.csv | 18 | **18** | 0 (1 row edited) — **NOT 23 as the orchestrator's STATE line said; disk = 18** | dead agent |
| data_gaps.csv | 22 | **22** | 0 (U.021/U.032 text changed) | dead agent |
| validation/failures/decisions/channels | 4/1/3/3 | 4/1/3/3 | 0 | — |
| COR ids | 14 | **20** | +6 (COR-15…20) | dead agent |

**9-register row total: 164 → 172 (+8, all in sources+quantitative). All +8 are the dead agent's; I added
no CSV rows** (my only corpus write was prose in `_INDEX.md`, referencing existing ids — no new `source_id`
minted, so no `id_mint` call was needed).

## 14. FETCH REQUESTS (§15.1 — carrier not held locally; claim marked UNANSWERED-with-fetch, no substitution)

```
FETCH REQUEST: EDGAR name-to-CIK browse — four terms (Dayton Hudson / Dey Brothers / Goodfellow / Target
  Corporation) via https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany
  WHY: sources/name_search/*.atom (4×7,747 B) hold the HTML error body but NO status line and no provenance
  sidecar. The register asserts HTTP 503 (U.025); the bytes print 500. Which failure (rate-limit vs service-
  down) changes the retry advice, and §14 rule 9 needs provenance beside the bytes.
  DESTINATION: sources/name_search/ (+ a .meta.json capturing the response status line and transport).
  STATUS UNTIL RUN: U.025 status code = UNVERIFIABLE-FROM-BYTES (UNANSWERED-with-fetch). Not a null.

FETCH REQUEST: Wayback CDX for target.com* and dhc.com* — https://web.archive.org/cdx/search/cdx
  WHY: sources/web_archive/cdx_targetcom.txt & cdx_dhc.txt (11,832 B each) are Internet-Archive "Temporarily
  Offline" pages with no sidecar and no captured status line; U.026's "503 twice" rests on the same gap.
  A CDX that actually returns is the only way to make U.026's "no pre-mid-1990s web archive" a measured null.
  DESTINATION: sources/web_archive/ (+ .meta.json). STATUS: U.026 = UNTRIED/UNANSWERED, held open.

FETCH REQUEST: FY1970/FY1971 Statement-of-Income year-end headers — the 17 `Image Container PDF` legs of
  archive.org item 01-target-archive (1965-76, 1985-86, 1990-91, 1994).
  WHY: two year-end days (r12/r13/r21/r22/r65/r66) stay UNKNOWN; no OCR layer prints them. Only the PDF legs
  can settle them. DESTINATION: sources/corporate_print/ . STATUS: U.030 = UNTRIED (zero web budget this pass).
  (This one was already carried by the first repair pass; I re-emit it rather than substitute a date.)
```

## 15. REMAINING DEBT (for the re-certifier / orchestrator, not silently dropped)

1. **14 live `target-s1-repair2` claims must be released** (`tools/scaffold.py release --path … --done`) or
   left to expire before another agent writes those 13 corpus paths. I did not force; I did not release
   another agent's claim (not mine to clobber).
2. **B-5 residuals on held paths** (all minor, none blocking): `timeline.csv` row 17 still `L3246-3250` → should
   read `L3246-3251`; `stage_1.md` P2-07 OCR join at `L1354-1355` still unmarked + P2 preamble not relabelled;
   one "six December" phrase survives in a superseded `stage_1.md` slice.
3. **`_parts/s1_p2.md` "volume 1"** (B-5e) — out of my write scope; `_parts/*` is a superseded audit trail.
4. **`quotes` gate advisory** (2 checked spans + 15 unattributed spans unmatched) lives in `stage_1.md` — a
   triage list per §15.6, not adjudicated by me; the certifier should sample those two lines.
5. **Tool/brief mismatches handed to the orchestrator (tools/ is outside every agent's write scope):**
   `gates.py --out` is a directory (briefed as a file); `scaffold.py` has no `status` (use `ledger`);
   `merge_census.py` cannot attribute validation/failures (RD-132) and globs only `_parts/*.md` (RD-127);
   `periodical_harvest` still has **no `target` task set** — which is exactly what would close U.032
   (B-4/COR-18), per stage_1.md:2091 and §15.2.
6. **The three "REFUTED" log claims I was warned about are correctly NOT relied on:** RD-123's
   `1972-03-22 floor` (grepped to zero bytes, COR-02/P1K11), RD-127's three self-refutations (S0102 exists;
   `64 stores` is registered in a composite cell; the HathiTrust body IS in the repo), and audit-2's
   "fabricated quote" charge on S4203 (refuted by the certifier: L1952 = `JOHN F. GEISSE` really). None of
   these is used as a value anywhere in the current registers; RD-127 is now cited **as a measurement**
   inside COR-18/U.032 (4× in stage_1.md, 1× data_gaps.csv), which is its correct use.

## 16. CLOSE-OUT

I established the dead agent's landed footprint from disk, re-verified all five inherited blockers against
it, found blockers 1/2/3/4 and certifier B-1…B-5(f) **already landed and correct**, and applied the single
remaining free-path repair (the `_INDEX.md` TLS/provenance stamps, blocker 4 second leg). I did **not**
force onto the 14 live-claimed corpus paths and **did not** re-apply fixes the dead agent had already made.
No value was back-solved, no citation was re-pointed to an unopened carrier, no null was asserted over an
untried family, and nothing was trimmed to satisfy the gate.

**This is a repair, not a certification.** A **different** agent — not `target-repair-2`, and not the dead
`target-s1-repair2` — must re-run `gates.py` at the tier it adjudicates and re-certify
`target_s1_certification.md`. Re-certification is **not** possible until the 14 stale-but-unexpired claims
are released (debt item 1).

STATUS: WRITTEN 2026-09-30, agent `target-repair-2`. Tool calls used ≈ 41 of 130. Stopped by choice, not
ceiling: every remaining item is either (a) on a live-claimed path I was told not to force, or (b) a
FETCH REQUEST / tool fix outside an agent's write scope.
