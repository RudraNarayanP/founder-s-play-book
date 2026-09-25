# Apple (company_004_apple) — Stage 1 volume index

**Merged 2026-09-26 by `apple-s1-merge`** from `_parts/s1_p1.md`, `_parts/s1_p2.md`, `_parts/s1_p3.md`. One
forensic document, split at one section boundary for the 60,000-word hard cap (method §9.2/§9.3). Nothing was
cut to fit: the parts' words are here in part order under one document header, and the merge added header text
rather than removing evidence (§9.6).

## Volumes

| Volume | Contents | Words | Status |
|---|---|---|---|
| `stage_1.md` (volume 1 of 2) | Header + merge note, STAGE BOUNDARY JUSTIFICATION, §A–§U — i.e. `_parts/s1_p1.md` and `_parts/s1_p2.md` entire (their claim-record blocks, part-local conflict keys and part 2's register-request block included) plus §M–§U of `_parts/s1_p3.md` | **56,537** | 94% of cap — amber (§9.2), not split further |
| `stage_1_part_2.md` (volume 2 of 2) | Tail of `_parts/s1_p3.md`: the consolidated `Untried routes` section (§X continuation), part 3's handoff block, and its pre-merge `>>> REGISTER ROWS FOR MERGE <<<` blocks, verbatim | **8,713** | well under cap |

**Why the cut sits at the end of §U.** §9.3 permits a split only at a section boundary, and the anchor spine that
the §U block mints is the addressable set every register row cites; cutting after §U keeps all 55 `U.nnn` anchors
in one volume, so the parity check (gates `anchors`) is decidable on the merged document instead of being spread
across two volumes. Numbering is continuous and nothing is renumbered: §A–§U in volume 1, the §X continuation in
volume 2. Recorded against this: `tools/gates.py` `NARR_GLOBS["stage1"]` lists only `stage_1.md` (no
`stage_1_part_*.md`, unlike its stage-2 and stage-3 entries), so a cut before §U would have made volume 2's
anchors invisible to the gate. That is a **gate defect for the audit pass**, not a content finding, and it is the
reason for the boundary chosen here.

**Non-destruction arithmetic.** Parts as released measured 64,744 whitespace tokens (`wc -w`: 64,754; the 10-word
delta is whitespace counting, not text). The merge removed 70 tokens of per-part scaffolding (two `# s1_pN.md`
titles and two stale `SCAFFOLDED … nothing written yet` comments) and added 576 tokens of volume headers and the
merge note: **64,744 − 70 + 576 = 65,250 = 56,537 + 8,713** ✓. Record census, parts vs merged, identical:
claim records **66** distinct / **237** occurrences; part-local conflict keys **16** distinct; `U.nnn` tokens
**57** distinct; dossier-local keys `[A-T]-\d{1,3}` **167** distinct / **1,391** occurrences.

## Section map

`stage_1.md`: Header · STAGE BOUNDARY JUSTIFICATION · §A Executive state summary · §B Founder/company state ·
§C Original problem · §D First experiment · CLAIM RECORDS (S1P1-01…34) · CONFLICT KEYS (S1P1-CF-01…10) · part-1
handoff · §E Product · §F Customer · §G Supply/host · §H Market · §I Competition · §J Technology · §K Money ·
§L Validation · CLAIM RECORDS (S1P2-01…16) · part-2 register requests · §M Failures · §N Decisions ·
§O Counterfactuals · §P Metrics · §Q Timeline · §R End-of-stage snapshot · §S Data gaps · §T Provenance ·
§U Conflicts/nulls/untried (**U.001–U.055**).
`stage_1_part_2.md`: §X Untried routes consolidated · part-3 handoff · part-3 register requests · part-3 merge contract.

## Key governance (canonical homes)

Part-local and dossier-local keys are **aliases**; the canonical address is the §U anchor. No key was deleted, and
no two ids mean one thing.

| Namespace in the parts / dossiers | Canonical home applied at merge |
|---|---|
| `S1P1-CF-01…10` | **01**→U.001 (date legs) + U.002 (place leg) + U.012 (residual) · **02**→deliberately **not promoted**: the boundary is resolved by decision, not evidence, and its cost is registered at U.019 (§U.i) · **03**→U.003 (order leg) + U.004 (price leg) · **04**→U.008 · **05**→U.055 · **06**→U.007 · **07**→U.005 · **08**→U.014 · **09**→U.018 · **10**→U.019 |
| `S1P2-CF-01…05` | U.005, U.007, U.003, U.008, U.009 respectively |
| `U-AP-1…4` · `U-C-1…6` | U.001, U.003, U.006, U.005 · U.001, U.005, U.006, U.003, U.011, U.013 |
| `U-A2-1…13` (the 13 pre-existing `conflicts.csv` rows) | U.013, U.003, U.016, U.004, U.015, U.055, U.009, U.010, U.011, U.005/U.007 (split), U.013, U.017, U.002 — the 13 rows stay in the file untouched as dossier history; each has exactly one canonical anchor, and each canonical row's last cell carries the alias (`Maps: …`) |
| `S1P2-S01…05`, `S1P3-S01…05`, dossier-local `CS-01`, `CS-05` | centrally assigned source ids **S1M-01…S1M-10** (see below) |

**Collisions resolved at merge.** (1) `S1P3-S04` and `S1P2-S02` describe the **same** Christie's lot 242 object
and its Sotheby's 2011 custody chain: one lineage, one source → one row, **S1M-02**, with a collision note in its
`notes` cell; `S1P3-S04` was not given a second id. (2) `CS-01` (cited as a local source key by part 3's
timeline and decisions rows) also lands on S1M-02; `CS-05` (the patent-register read cited by the 1977-04-11
timeline row and by record S1P2-12) had **no** register row proposed for it, so the merge minted **S1M-10** with
fields taken only from that existing text, and the local keys in those rows now read
`S1M-02 (was CS-01 local)` / `S1M-10 (was CS-05 local)`. (3) The 1976-11-20 demonstration is now carried twice in
`timeline.csv` — the pre-existing dossier row and part 3's anchor-keyed row (U.033): both retained, the
anchor-keyed row is the canonical one. (4) Part 2's `675` comparator and `101`/`17.8%` quantitative rows duplicate
existing dossier rows 12 and 14 in substance; both retained, no de-duplication by deletion.

## Registers (all under `research/`, where this company's registers live until assembly)

| Register | Rows | Before → after | Applied from |
|---|---|---|---|
| `conflicts.csv` | **38** | 13 → 38 | part 3's 25 canonical `U.nnn` rows |
| `data_gaps.csv` | **35** | **created** | part 2's 5 + part 3's 30 (`U.025–U.054`) |
| `quantitative.csv` | **44** | 30 → 44 | part 2's 6 + part 3's 8 |
| `timeline.csv` | **30** | 23 → 30 | part 3's 7 anchor-keyed rows |
| `sources.csv` | **23** | 13 → 23 | 9 locally-proposed rows under `S1M-01…S1M-09` + minted `S1M-10` |
| `validation.csv` | **6** | **created** | part 2's 6 |
| `failures.csv` | **6** | **created** | part 3's 6 |
| `decisions.csv` | **4** | **created** | part 3's 4 |
| `channels.csv` | **0** | **created** | header only — no part requested a channel row and the merge invents none |

The five created registers carry the header row copied as **bytes** from
`company_001_amazon/<name>.csv`; every `stage` cell is the controlled literal `stage1` (§13 vocabulary — no
numeric stage values were introduced, and none were found in this company's legacy rows).

**Parity, measured.** 55 anchors declared in the narrative (`stage_1.md`) ↔ **55** anchor tokens in the registers;
0 narrative anchors without a register row, 0 register anchors without a declared anchor; every one of
U.001–U.055 has ≥1 citing row. Gate output agrees: `anchors parity 55 narrative anchors <-> 55 register anchors`.

## Rows refused, and repairs made (nothing dropped silently)

* **REFUSED — `conflicts.csv`, part 2's 5 `S1P2-CF-*` rows.** 14 fields against the target header's 15: the
  `residual_uncertainty` column is absent in all five, so applying them would have written a shifted row. Nothing
  is lost: each subject is restated with both sides and its residual uncertainty in the canonical
  `U.005/U.007/U.003/U.008/U.009` rows, which cite the part-2 keys as aliases.
* **PARITY REPAIR (text unchanged, quoting only) — 7 rows.** `data_gaps.csv`: two part-2 rows carried an unquoted
  comma inside the `gap` and `confidence` cells (9 fields → 8). `quantitative.csv`: one part-2 row carried an
  unquoted comma in `metric` (13 → 12). `sources.csv`: four part-2 rows omitted the `source_type` column
  (17 → 18); the inserted labels are the carrier descriptions the rows already stated, and part 3's parallel rows
  set the pattern.
* **NOT APPLIED — the three rewrites part 3 asked for inside `_parts/s1_p1.md`** (S1P1-05/S1P1-06 window
  labelling, U.019; S1P1-10's mis-pointed `Conflicts:` cell, U.011; the `Source`/`Tier`/`Conf` upgrades of
  S1P1-01…11). §14 rule 4 and rule 12 forbid a silent tidy of another pass's released text, and my brief binds the
  merged text to the parts verbatim. They are recorded here, in the merge note in `stage_1.md`, and in
  `../../03_quality_control/apple_s1_merge.md` **for the audit pass**; U.011 and U.019 carry the merge action in
  their register rows, so the record itself is corrected even though the released sentences are not.
* **CARRIED, not applied —** part 3's F1–F5 FETCH REQUEST list (routes U.037–U.054) is the orchestrator's
  dispatch list, not this pass's work; web budget on this pass was 0.

## Evidentiary positions the merge preserved

`$666.66` remains **verified absent from every held byte** and stays FOUNDER CLAIM / UNKNOWN (U.004); no
in-window document gives a 1976 price, order, unit count, revenue, supplier or founder officer title (U.003,
U.026, U.027, U.047, U.014); Wayne's 10%-vs-12%, Markkula's terms, the 50-boards-at-$500 story,
word-of-mouth-vs-the-April-1977-BYTE-directory, and $77,000-vs-$770,000 all stay **two-sided** (U.005, U.007,
U.003, U.008, U.009) with no averaging anywhere; Apple's earliest EDGAR text is the 1994-01-26 / FY1994 Form 10-K,
so everything earlier is print and **one lineage is one source** (U.023, U.041, sources row S1M-01).
