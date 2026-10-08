# BOEING (company_047_boeing) — STAGE 1 MERGE REPORT

Agent `merge-boeing`, 2026-10-07. Merge of the single part `_parts/s1_p1.md` (author `s1-boeing-p1`).
I am the merger: I **apply** rows, mint ids, bind schemas and run the mechanical gate. I **may not audit or
certify**; the audits (numbers+hindsight, citation+verbatim) and the certification belong to different agents.
`_parts/*` is read-only; the only text I added to the part is the `SUPERSEDED` footer (placement/keys only).

## 1. Headline

- **Part emitted 44,732 words / 211 register rows / 24 claim records / anchors U.001–U.017 (1:1 with 17
  conflict rows).** All 211 rows **applied to the nine CSVs at the company root**, none dropped, none added.
- **`stage_1.md` = 34,817 words, 224,150 bytes, ONE volume** (registers moved out of the prose to the CSVs).
- **Anchor ↔ conflict parity PROVEN by re-running the census**, not asserted (see §5).
- **Ids minted centrally: S4510 … S4528 (19 contiguous), above the highest live id** (see §3).
- **Gate `--tier core` : Findings 2 | Passes 17, exit 0 — both findings ADVISORY, 0 substantive.** (see §7).

## 2. Register application — `APPLIED n rows` per register (requested ↔ applied, measured on bytes written)

Rows are the count of data rows (below the header) in each live CSV; "cols" is the header width; the width and
duplicate-key pass ran **across all nine blocks in one operation**, not per block.

| register | requested | **APPLIED** | cols | width-drift | dup keys | source_id resolve | note |
|---|---|---|---|---|---|---|---|
| `sources.csv` | 19 | **APPLIED 19 rows** | 18 | 0 | 0 (19 keys S4510–S4528) | — (this is the key set) | seven corporate-print layers = ONE lineage; S4525 one registry record ×26; S4526 two lineages one sentence |
| `quantitative.csv` | 75 | **APPLIED 75 rows** | 12 | 0 | n/a (no id col) | n/a | **0 FY1937 and 0 FY1936 rows — withheld by design, see §6** |
| `timeline.csv` | 42 | **APPLIED 42 rows** | 11 | 0 | n/a | all resolve | 1916 RESTATED → 1940-12-31 boundary; U.003 DERIVED day; U.004 three dates |
| `conflicts.csv` | 17 | **APPLIED 17 rows** | 15 | 0 | 0 (17 keys U.001–U.017) | n/a (no S tokens) | 1:1 with §U anchors |
| `data_gaps.csv` | 18 | **APPLIED 18 rows** | 8 | 0 | n/a | n/a | P1GAP16/05/08 carry the withheld FY1937/FY1936 damage |
| `decisions.csv` | 11 | **APPLIED 11 rows** | 15 | 0 | n/a | all resolve | 1934-08 motive UNKNOWN; the 1936 decision-void row |
| `validation.csv` | 13 | **APPLIED 13 rows** | 11 | 0 | n/a | all resolve | bound by content (see §4) |
| `failures.csv` | 9 | **APPLIED 9 rows** | 11 | 0 | n/a | all resolve | bound by content (see §4) |
| `channels.csv` | 7 | **APPLIED 7 rows** | 11 | 0 | n/a | all resolve | A.M. 18, sub-contract, municipal leases, military, commercial, export, equity |
| **TOTAL** | **211** | **APPLIED 211** | — | **0** | **0** | **0 dangling** | **0 unapplied, 0 added by the merge** |

Every header is **byte-identical** to the corresponding `company_001_amazon/<name>` header (string equality);
`stage` is the literal `stage1` on all 211 rows (never a bare number); the post-boundary `(PB)` rows keep
`stage1` with the `(PB)` flag in `notes` only, so they are not pulled into the stage's own evidence series.

## 3. Id block allocated

Command: `python tools/id_mint.py --count 19 --company company_047_boeing --claim --agent merge-boeing` →
**S4510, S4511, S4512, S4513, S4514, S4515, S4516, S4517, S4518, S4519, S4520, S4521, S4522, S4523, S4524,
S4525, S4526, S4527, S4528** (19 contiguous). The `--audit` before the mint showed the top issued block was
PepsiCo `S4479`–`S4494` and registry claims reaching `S4509`; the tool allocated **above the highest live id**
and did not re-enter a gap. The known collision `S4222`–`S4229` (cited by both Microsoft and Target) and
Cigna's block `S4407`–`S4422` sit **below** this range and were untouched.

Only the **source-register keys** `P1SRC01–P1SRC19` were re-keyed to S-ids, in **every cell of every live CSV**
(so 0 `P1SRC` tokens remain in the registers). The dossier-local row tags `P1QTNnn / P1TMLnn / P1GAPnn /
P1DECnn / P1VALnn / P1FAInn / P1CHNnn` and the claim-record tags are preserved verbatim — they have no global
counterpart. The narrative in `stage_1.md` keeps the author's `P1SRCnn` reading keys, bound by the id-map
table at the head of that file. The `keys` gate resolves every `S45xx` token the merge record cites against
`sources.csv` (all 19 present); foreign ids used as allocation context are backticked so they read as
protected history, not dangling pointers.

## 4. `validation.csv` / `failures.csv` — adjudicated by content, reasoning printed in-cell

`merge_census.py` reports these two blocks as `AMBIGUOUS:validation.csv,failures.csv` because they **share the
same 11-column schema** (`company,stage,date,signal_or_failure,magnitude,what_it_demonstrated,
what_it_did_not_demonstrate,source_id,evidence_class,confidence,notes`). The census cannot bind them and must
not be read as leaving them unassigned. I adjudicated by **row content** and wrote the reasoning into each
row's `notes` cell:

- **validation.csv — 13 rows (P1VAL01–P1VAL13).** Every one is a **positive** signal: the 1927 competitive
  award, contract performance commenced, the 1931 mail-clerk testimony, the Tenth Circuit restraint of the
  Wyoming tax, the 1935 backlog inflection, the Army trainer win, the two bombardment contracts, the Clipper
  type certificate, the Pan American option at higher prices, the capital increase, the RFC facility
  arranged-then-retired, the emergency-plant funding, and the first audited profit. Bound to validation.csv.
- **failures.csv — 9 rows (P1FAI01–P1FAI09).** Every one is an **incurred loss or an attestation limit**: the
  Model 299 destruction, Canada dormant/boat-repair, the Clipper overrun, the T.W.A. termination, the
  Stratoliner cost escalation, the bombardment rework loss, the deficit written off against capital, the wage
  shocks, and the disclosure/audit-scope limits. Bound to failures.csv.

The two sets are **disjoint and complete** (13 + 9 = the 22 the author emitted), and the binding is
deterministic on the `P1VALnn`/`P1FAInn` prefix confirmed by reading the `what_it_demonstrated` cells. No row
was moved between them.

## 5. Anchor ↔ conflict parity — proven by re-running the census, not asserted

The part declares `<!-- ANCHORS: U.001-U.017 -->` and writes §U.001–§U.017. `merge_census.py --verbose`
**after the final write** reads:

| reading | before any write | after the final write |
|---|---|---|
| structured blocks parsed | 9 | 9 |
| rows requested | 211 | 211 |
| `conflicts.csv` requested / present / missing | 17 / 0 / 17 | **17 / 17 / 0 — parity proven** |
| `sources.csv` requested / present / missing | 19 / 0 / 19 | 19 / 0 / 19 — the 19 "missing" are the superseded local tags `P1SRC01–19`; the minted ids S4510–S4528 are on disk |
| unattributed block-groups | 2 (validation/failures, identical schemas) | 2 — same schema property; adjudicated by reading (§4) |
| duplicate keys across all nine blocks | — | 0 |
| rows off header width | — | 0 |
| `research/*.csv` third emission | none (0 CSVs under `research/`) | none |

All seventeen declared anchors U.001–U.017 exist as `conflicts.csv` keys, 1:1 with the seventeen §U sections;
no eighteenth row, no unanchored row. `gates.py anchors` reports `parity: 17 narrative anchors <-> 17 register
anchors` and `citation resolution: every register-cited anchor resolves`. The 18th distinct token, `U.001b`, is
a **subsection label used in prose** (§B.3 row 3), counted as an ADVISORY prose mention, not a defect — the
author's §U.001 records claims A/B/C and the sub-dissent `U.001b` is a pointer inside the naming table, not a
separate conflict.

## 6. Withheld rows and uncarried follow-ups — named, not dropped

The merge applied **all 211 emitted rows**; nothing was dropped at merge. The rows the **author** withheld
(beyond §P/quantitative) are damage, not laziness, and are carried as gaps + fetches, **never back-solved from
neighbours**:

- **Every FY1937 income-statement and balance-sheet figure** — the FY1937 layer (S4512) renders two-column text
  plus rotated table columns as interleaved garbage; only four fragments are legible (163,847 + 9,577 rights
  shares; the tax provision fragment). Recorded at `data_gaps.csv` **P1GAP16** and `FETCH REQUEST #3`
  (page images / re-OCR). `quantitative.csv` carries **0** FY1937 rows by design.
- **All FY1936 quantities** — the FY1936 layer is **absent from the archive item** (the 46-layer file list has
  no 1936). Recorded at `data_gaps.csv` **P1GAP05** (list not re-enumerated by this pass) and **P1GAP08**
  (the 600,000→800,000 capital step falls in the missing/damaged years); `FETCH REQUEST #4`.
- **FETCH #1** (family-(a) recital completion) and **FETCH #5** (Washington / Delaware charter records — the
  only route to U.001–U.003 as acts, and **no tool in `tools/` reaches either**) have **no dedicated
  `data_gaps.csv` row** because the author emitted none; their homes are `## Untried` #9/#10 in the volume and
  the `residual_uncertainty` cells of `conflicts.csv` U.001–U.003. Named here rather than dropped.
- **`sources/sec/_MANIFEST.csv` regression** (header row + 0 data rows, though 33 `.txt` + 37 sidecars are on
  disk) is **reported, not repaired** (`data_gaps.csv` P1GAP18, method §14 rule 4). This merge did **not**
  modify `sources/`.

## 7. Gate result (`--tier core` passed explicitly) and the two advisories

Command: `python tools/gates.py --company-dir founders_playbook/01_companies/company_047_boeing --tier core
--out 03_quality_control/boeing_s1_gates_merge.md`.

**Why `--tier core`:** `--tier auto` mis-stamps Boeing **T3** because its tier reader counts tier *mentions*
across `research/` rather than reading the verdict line (the dossier's own verdict is "**Stage 1 … TIER 2
(core)**"). `_AUTHOR_WAVE_PLAN.md` says `--tier auto` cannot see a table-row verdict, to pass the tier
explicitly, and to record that I did — not to edit prose to satisfy the tool. I did, and said so here and in
the volume.

**Result: Findings 2 | Passes 17, exit 0.** The 2 findings are **both ADVISORY (0 substantive)**:

1. `quotes / ADVISORY — 16 of 33 checked spans unmatched (48%)`. This is **not** a fabrication signal: I
   spot-checked the flagged spans against the held bytes and they are present (`deliver the mail to the
   employee of the Boeing`, `lowest responsible bidders`, `formed for the purpose of acquiring`, the
   University-of-Wind-Tunnel sentence). The volume's quotes are **cleaned transcriptions of IA OCR bytes** —
   soft-hyphens `¬` closed, quote glyphs rendered as `'`/`"`, interleaved columns reassembled and flagged
   COLUMN-REASSEMBLED, ellipses inside self-quotations — so they do not byte-match the raw `.txt` the gate
   indexes. The gate itself labels this "gate precision is not established, treat as a triage list, NOT as
   defects". I left the data alone (§15.6: never reshape real data to silence a gate). The `gate_quotes`
   **research-index gap** (it indexes only `sources/**`, so a quotation of `research/A4_harvest_mine.md` can
   never match — the wave plan's "three corrections" item) is carried here as the same permanent false advisory
   Cigna carried; no volume passage's confidence rests on a research dossier.
2. `advisory / stage_1.md — 34,817 words over the core (T2) density target 22,000 — NOT a split mandate and
   NOT a defect`. Recorded so the tier is measurable; **nothing was trimmed**.

`csv` passes on all nine registers (correct widths, `source_id` resolve), `anchors` passes on parity,
`keys` passes (0 dangling after the merge-record backtick fix; 7 protected foreign-history ids noted), and
`corrections` did **not** run — by design: this merge issued **no retraction** (no `CORRECTIONS.md`), so there
is no COR-nn to propagate. The author's pre-merge gate (`boeing_s1_gates_p1.md`, coverage-only) was the
expected pre-merge state.

## 8. Geometry / split decision — ONE volume

**Decision: do not split; keep `stage_1.md` as one volume; log the overage as advisory; trim nothing.** The
44,732-word part is above the §15.2 T2 density target (22,000) and under the §9.2 hard cap (60,000). Moving the
211 register rows into the CSVs drops the narrative volume to 34,817 words — under the hard cap with margin —
and the whole T2 deliverable (§A–§U + claim records + registers) fits one file, so there is no §9.2 defect to
repair. A boundary-only, never-renumbered split (author's NOTES §4 proposal) would add a volume map without
removing the advisory and would risk renumbering; §9.3 forbids renumbering and §9.6 forbids cutting evidence to
hit a number. **Volume map, live `wc`, the geometry decision and the five-family table are recorded in
`_MANIFEST.md`.**

## 9. The four registrant-identity items carried (Boeing is the corpus's sharpest case)

1. **Five namings, no held byte conjoining any two** (§B.3, U.001): FY1934 attaches "since 1916" to **Boeing
   Aircraft Company, a Washington corporation** owned 100% by the addressee; the **federal record** (S4517)
   calls the 1927 contracting party "**Boeing Airplane Company, Incorporated** … under the laws of
   **Washington**" — an in-window name collision, not a retrospective recital; FY1938 prints "organized in
   **August, 1934**"; the `1934a` layer (S4516) is an **undated Hamilton Metalplane advertisement**, so "one
   item, one layer per year" is a **file census, not a document census**, and the count is **six audited
   reports, not seven**. The **1960 renaming is refused** as a Stage-1 fact (EDGAR prints a conformed-name
   change of 1973-07-25 for **one registry record re-printed 26 times**; no held byte prints 1960 as a renaming).
2. **The origin day is DERIVED and stated as such** (§B.1, U.003, S4511): FY1935's "twentieth anniversary …
   will occur July 22 of this year" → **1916-07-22** by subtraction, Medium, one lineage. `July 22, 1916`
   occurs **0** times; **July 15 is unheld, not contradicted**. The A.M. 18 award date stays **three-valued
   inside one volume** (Jan 29 / "on or about Feb 1" / contract dated 1 Feb) at **U.004** — **not reconciled**.
3. **Withheld rows are damage, not laziness** (§6): all FY1937 figures and all FY1936 quantities withheld,
   carried as `data_gaps` + FETCH #3/#4, never back-solved.
4. **Antitrust motive is UNTRIED, not denied** (§C.1, U.010): three printings say tax / simplification /
   industry trend; "antitrust" has **0 Boeing-adjacent witnesses** (its single corpus occurrence is in the
   munitions volume where "Boeing" is 0). `mechanism UNKNOWN` is kept on the 1934–38 acts and on the §N "new
   management saved Boeing" coda.

## 10. Five-family table (Stage 1: 1916-01-01 → 1940-12-31; T2 core, tier NOT re-graded)

| family | state | in-window Tier-1 text? | basis / closing route |
|---|---|---|---|
| (a) SEC / EDGAR filings | TRIED–ANSWERED as a perimeter; **nothing in-window** | NO | earliest indexed 1994-03-15; **no S-1**; 333 accessions never enumerated (`--max-docs 40`); only origin voice is the 1996/1998 S-4 boilerplate `(PB)`. Route: charter records (no tool). |
| (b) Web archives | **UNTRIED** (now REACHABLE; still cannot bear on Stage 1) | NO | `tools/cdx_intake.py` exists since 2026-10-06 (the probe's "no script reaches CDX" is stale); family floor mid-1990s vs a 1916-1940 window (§14.6). |
| (c) Periodical / gov print | TRIED–ANSWERED, two content-verified NULLs | **YES** (two court records) | D.C. Cir. 1934 air-mail record + 1933 Wyoming record are Tier-1; *Aviation* 1916-08-01 (`Boeing` 0) and Senate munitions (`Boeing` 0/`Seattle` 0) are live negative controls. Route: UNTRIED #3/#6/#8. |
| (d) Digitised corporate print | TRIED–ANSWERED — **the family that moved Boeing** | **YES** | **six** in-window audited reports (1934a is a Hamilton ad, not a report), 137,518 B; FY1937 column-interleaved. Route: FY1937 re-OCR (#3), 39 unopened 1941-78 layers. |
| (e) Auction / museum / manuscript | **UNTRIED — structurally** | NO | no source-family in `queries.json`; no tool reaches a finding aid. **The single route most likely to change the verdict** (the only family that can carry an instrument, not a recital). |

## 11. What this merge did NOT examine

I did not re-run the author's term/noise/footing measurements over `sources/` (the 211 rows are the author's
emission of record, applied verbatim); I did not open or verify any held source byte beyond the five
spot-checks in §7 needed to classify the quote advisory; I did not modify anything under `sources/`; I did not
touch the research dossiers; I did not re-derive the tier; I did not run any of the `## Untried` fetches (web
calls by this merge: **0**); and I did not audit or certify — the numbers+hindsight and citation+verbatim
audits and the final certification belong to agents who are neither the author, the merger, the auditor, nor
the repairer.
