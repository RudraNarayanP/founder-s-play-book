# CORRECTIONS.md — company_013_costco (Stage 1)

Append-only provenance-correction register for the Costco Stage-1 dossier. Established **at the Stage-1 merge
pass, 2026-09-30** (agent `costco-s1-merge`), each item verified against the two author emissions under
`_parts/` and against the held bytes under `sources/`. Nothing here re-tiers, re-dates or re-values a claim:
these are key, propagation and schema corrections. A later pass adds a dated entry above; it does not delete one.

**Reading rule.** Every COR-nn below is printed in the register layer *and* in `stage_1.md` (that propagation is
what `tools/gates.py` checks, because a correction that reaches only the prose leaves the registers teaching the
withdrawn form). Where an entry says a row was *folded*, the folded row's differing cells are carried verbatim
into the surviving row's `notes` cell — a fold removes a duplicate key, never evidence.

---

## COR-01 — three part-2 source emissions are the same documents as three part-1 emissions (2026-09-30)

**What the parts emitted.** Part 1 registered twelve carriers `P1S01`–`P1S12`; part 2 registered five,
`P2S01`–`P2S05`. Key-collision checking run **across both part files in one operation** found three pairs naming
the same accession or the same index:

| part-2 emission | part-1 emission already holding it | the document |
|---|---|---|
| `P2S01` | `P1S07` | Schedule 13D naming Sol Price, accession 0000912057-94-004286 |
| `P2S02` | `P1S05` | Form 8-K dated 1994-07-28, accession 0000912057-94-002516 |
| `P2S05` | `P1S11` | fleet periodical harvest candidate index, rows `company=costco` |

**Evidence that this is the right call, not an invention.** Part 2 printed the collision itself in its emission
preamble (`_parts/s1_p2.md` l.1267-1269): "P2S01 and P2S02 are the SAME accessions already registered as P1S07
and P1S05 … fold or alias them and count them as one document each, never as an added source (method §3)". The
`archived_url` and `url` cells agree pair by pair in the two blocks.

**Action.** `sources.csv` carries **14 rows, not 17**. The folded emission's `claim_supported` token list is
unioned into the surviving row; every other differing cell of the folded row is quoted verbatim into that row's
`notes` under a `MERGE FOLD 2026-09-30 (COR-01)` tag. The independence position is unchanged and is the point of
the fold: the SC 13D is one lineage, and letting it occupy two ids would have made the founder-naming look
twice-corroborated (method §3, RD-124's fake-Tier-1 lesson).

**Propagation.** `sources.csv` rows S4397, S4399, S4403 (`notes`); `stage_1.md` merge record, "Register
application, fold list and id map".

---

## COR-02 — every source id in the register layer is centrally minted; the parts' `P1S`/`P2S` tokens are aliases (2026-09-30)

**What was minted.** `python tools/id_mint.py --count 14 --company company_013_costco --claim --agent
costco-s1-merge` returned **S4393–S4406** and recorded the claim in `00_universe/_ID_BLOCKS.tsv`. The block is
allocated **above the highest live id**, so no gap was re-entered, no number was reused, and nothing outside the
block is used by this company.

**What was not assumed.** No 4-digit-looking token inside either part was treated as an already-issued id, and no
provisional id was applied to the register as if it were global. RD-131's `S435` (an OCR'd dollar amount in the
BYTE layer, not a citation) is the defect class this guards against; RD-123's Walmart collision (`S0145` naming
two different documents) is the class the central mint prevents.

**Map.** P1S01→S4393 · P1S02→S4394 · P1S03→S4395 · P1S04→S4396 · P1S05→S4397 · P1S06→S4398 · P1S07→S4399 ·
P1S08→S4400 · P1S09→S4401 · P1S10→S4402 · P1S11→S4403 · P1S12→S4404 · P2S03→S4405 · P2S04→S4406 ·
P2S01→S4399, P2S02→S4397, P2S05→S4403 (the COR-01 folds).

**Action.** All `source_id` cells in the nine registers are global ids, and the provenance-bearing free-text
cells (`claim_a_source`, `claim_b_source`, `best_available_evidence`, `quantitative.source`) were re-pointed at
them; measured after the write, **0** `P1S`/`P2S` tokens remain anywhere in the register layer. Each
`sources.csv` row prints its own alias list in `notes`. **The prose of the two volumes keeps the dossier-local
aliases and was not rewritten** — the aliases sit inside author sentences and claim records, and `sources.csv`
plus `stage_1.md`'s map is what resolves them (RD-122 precedent: the register is the only place global uniqueness
lives).

**Propagation.** every `sources.csv` row (`notes`); the re-pointed cells of all nine registers; `stage_1.md`
merge record and "Provisional-to-global id map".

---

## COR-03 — ten duplicate emissions across and inside the parts were folded (2026-09-30)

`validation.csv` 11 requested → **8 rows**; `failures.csv` 15 requested → **11 rows**.

- part 1's "+6 percent comparable warehouse sales" (1992-08-30) and part 2's "comparable warehouse sales at a
  positive 6 percent annual rate" (same date, same magnitude, same carrier) are one signal.
- part 1's "37 gross warehouse openings in one fiscal year on an estate of 200" and part 2's "thirty-seven gross
  openings on an estate of two hundred" (1993-08-29) are one signal spelled two ways.
- part 1's "-3 percent comparable sales", "self-cannibalisation …" and "$5750 thousand lease dispute" rows are
  the same three signals as part 2's wider rows — part 2's own `notes` already said it carried part 1's row.
- part 2 emitted the 1992-04-16 San Francisco member-base row **twice in each file, byte-identical across all
  eleven columns**; one of each survives.

**Action.** the surviving row is the one that read the wider evidence; every differing cell of the folded row is
carried verbatim into its `notes` under `MERGE FOLD 2026-09-30 (COR-03)`, so the fold removes a duplicate record
and not a judgment.

**Explicit non-fold.** `quantitative.csv` keeps **both** 1993-08-29 rows — `warehouses_opened_in_fiscal_1993_gross`
= 37 (part 1, FACT) and `warehouses_opened_net_of_closings_fiscal_1993` = 30 (part 2, DERIVED,
`37 opened minus 7 closed = 30`). Near-identical metric names, two different measurements; folding them would
have destroyed a printed figure. This is recorded because a similarity-based fold would have looked tidy in the
gate output and lost evidence (RD-122's "drift repaired, not dropped" precedent).

**Propagation.** the eight `validation.csv` and eleven `failures.csv` rows carrying the tags; `stage_1.md` fold
list.

---

## COR-04 — five §U anchors had no register address; addresses were assigned, and two gap rows were minted (2026-09-30)

§U declares 32 anchors (`U.101`–`U.115` conflicts, `U.120`–`U.136` documented nulls and open routes). The
emitted rows cited 27, so five addresses pointed at nothing and a reader following them landed nowhere — which
`gates.py` reports as *anchor with no register row*, a hard parity defect.

| anchor | what §U says it addresses | register home given at merge |
|---|---|---|
| `U.112` | "K05 (part 1), as narrowed" — the boundary-date choice | `conflicts.csv` row **K05**, printed in its `section` cell |
| `U.113` | "K01 (part 1), unchanged and unclosed" — 1975 against 1976 | already cited by `timeline.csv` rows; no new row needed |
| `U.121` | founder identity and capacity for leg P, UNANSWERED | the part-1 `data_gaps.csv` row "Who founded the 1976 leg and in what capacity" |
| `U.132` | the web-archive family, UNANSWERED | the part-1 `data_gaps.csv` row that already registers families (b)/(c)/(e) |
| `U.120` | founding capital, first-unit cost, opening-day trade — EMPTY for the archive, UNTRIED as a route | **new `data_gaps.csv` row**, transcribed from the §U declaration, importance High, follow-up named |
| `U.124` | the fee schedule at either opening — not knowable here; the two schedules that exist disagree (K10/U.102) | **new `data_gaps.csv` row**, importance High, follow-up named |

**Action boundaries.** No anchor id was minted, no anchor was retired, and nothing was renumbered: the free block
`U.116`–`U.119` is deliberately *not* entered, because §U's own reading rules reserve `U.101`–`U.115` for
conflicts and `U.120`–`U.136 for nulls, and inventing an address inside a scheme the author declared would
re-create RD-122's renumbering defect. The two minted rows add register rows; they withdraw no claim, and each
carries a `follow_up_task` as §13 requires for a High-importance gap.

**Measured after the write:** 32 anchors cited in the register layer, 0 undeclared, 0 declared-and-unaddressed.

**Propagation.** `conflicts.csv` K05; `data_gaps.csv` (four rows tagged, two of them new); `stage_1.md` merge
record, "Anchors".

---

## COR-05 — a prose value in a date column became `UNKNOWN`, with the prose preserved verbatim (2026-09-30)

**What arrived.** One `channels.csv` row — the newspaper and local-press coverage channel for either chain
1976-1993 — carried `date_tested` = *"never attempted by any pass"*. §13 fixes the value space of a date column:
a date, a partial date, or the literal `UNKNOWN`. RD-122's precedent (Target's `access_date` = `NOT ACCESSED`)
repairs the cell and keeps the sentence.

**Action.** `date_tested` = `UNKNOWN`; the sentence is preserved verbatim in that row's `notes` under the
`MERGE REPAIR 2026-09-30 (COR-05)` tag, together with the row's own UNTRIED verdict. The register still records
the finding — that the family has never been attempted is the point of the row — and §U U.130/U.133 keep naming
the route.

**Counts for the manifest.** Numeric `stage` values normalised: **0** (all 199 emitted rows already carried the
controlled literal `stage1`, §13/RD-048 vocabulary). Width-drift rows re-joined: **0**. Empty cells filled: **0**.
Date-column prose values repaired: **1** (this entry).
