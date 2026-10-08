# Alphabet Stage 1 — `stage_1_index.md`

Company 005 (Alphabet Inc., registrant Google Inc., CIK 1288776). Stage 1 = **1998-01-09 → 2001**
(year-granular; the closing day is UNKNOWN), tier **T1 exemplar**, method §9.2/§9.3/§9.6. Built by the
Stage-1 merge pass on 2026-09-30 (agent `alphabet-s1-merge`). Citable units are the **one volume**
`stage_1.md` (sections §Header, §Boundary, §A–§U continuous) and the **nine registers** at this directory root.

## Volumes

| # | File | Sections | Words | Bytes | Claim records | Emission blocks |
|---|---|---|---|---|---|---|
| 1 | `stage_1.md` | merge note → Volume 1: Header, Boundary, §A–§F → Volume 2: §G–§U (incl. §U) | 57,358 | 395,186 | 24 `P1A01`–`P1F04` + 56 `P2G01`–`P2U01` = **80** | 16 fenced `csv` blocks (8 + 8), provenance only |
| — | `_parts/s1_p1.md` | superseded part 1 body, carried byte-identically | 21,301 | 148,456 | 24 | 8 |
| — | `_parts/s1_p2.md` | superseded part 2 body, carried byte-identically | 35,692 | 244,216 | 56 | 8 |

**§9.2 arithmetic:** 20,896 + 35,692 = 56,588 w combined → above the 40,000 soft target, inside the
40,000–60,000 amber band, **below the 60,000 hard cap** → §9.3 is not triggered → one volume. Merged volume:
57,358 w (56,532 carried body + 826 merge header/note/dividers), **2,642 w of headroom**.

## Anchor map — `<!-- ANCHORS: U.017-U.036 -->` (20, the union of both volumes' declarations)

Part 1 minted **no** `U.nnn` anchor; part 2 minted and declared U.017–U.036, so the merged volume declares the
same 20. Upstream dossiers' `U-1`–`U-16` (hyphen form, `research/A_chronology_feasibility.md` and
`research/B1_filing_records.md`) are a different namespace and are **not** anchors — the parts cite them as
`B07`, `B15`, `U-16`, `U.017`-style keys are never used for them.

| range | kind | lives in |
|---|---|---|
| U.017–U.030 | live two-sided conflicts | `conflicts.csv` rows keyed `U.017`…`U.030` (part 2 §U, part 2 §K/§M/§S) |
| U.031–U.036 | documented nulls / untried routes | `data_gaps.csv` `gap` cells: U.031 in the row folded from `P2GAP01` into `P1GAP01`, U.032 via `P2GAP02`→`P1GAP05`, U.033 via `P2GAP03`→`P1GAP04`, U.034–U.036 in `P2GAP04`, `P2GAP06`, `P2GAP10` |

Parity as measured: **20 narrative ↔ 20 register, 0 undeclared, 0 uncovered** (`gates.py` anchors, PASS).

## Registers (canonical data; 169 rows)

| register | requested | applied (rows kept) | folded | refused | groups |
|---|---|---|---|---|---|
| `sources.csv` | 22 | 21 | 1 | 0 | 1 |
| `quantitative.csv` | 40 | 40 | 0 | 0 | 0 |
| `timeline.csv` | 32 | 31 | 1 | 0 | 1 |
| `decisions.csv` | 10 | 10 | 0 | 0 | 0 |
| `validation.csv` | 13 | 12 | 1 | 0 | 1 |
| `failures.csv` | 10 | 9 | 1 | 0 | 1 |
| `channels.csv` | 11 | 8 | 3 | 0 | 3 |
| `conflicts.csv` | 21 | 21 | 0 | 0 | 0 |
| `data_gaps.csv` | 21 | 17 | 4 | 0 | 4 |
| **total** | **180** | **169** | **11** | **0** | **11** |

## Id map — globally minted, retired local keys kept as aliases

21 global ids **S4332–S4352** allocated by `tools/id_mint.py --count 21 --company company_005_alphabet --claim`
(above the highest live id; recorded in `00_universe/_ID_BLOCKS.tsv` for `company_005_alphabet` /
`alphabet-s1-merge`; verified 0 collisions against every `sources.csv` in the corpus and against the registry).
`sources.csv` carries them; the local keys stay printed in each row's `notes` (`GLOBAL-ID S43xx <- P…SRCnn`)
and inside every `MERGE[...]` marker, so prose citing `P1SRC04`, `P2SRC01` or B1's `B01`–`B43` still resolves.

S4332←P1SRC01 · S4333←P1SRC02 · S4334←P1SRC03 · S4335←P1SRC04+P2SRC02 · S4336←P1SRC05 · S4337←P1SRC06 · S4338←P1SRC07 · S4339←P1SRC08 · S4340←P1SRC09 · S4341←P1SRC10 · S4342←P1SRC11 · S4343←P2SRC01 · S4344←P2SRC03 · S4345←P2SRC04 · S4346←P2SRC05 · S4347←P2SRC06 · S4348←P2SRC07 · S4349←P2SRC08 · S4350←P2SRC09 · S4351←P2SRC10 · S4352←P2SRC11

## Merge decisions

1. **One volume, no §9.3 split** — the combined body sits in the amber band, which §9.2 explicitly allows to
   finish as one file; the split test is the 60,000 hard cap. Nothing was trimmed to buy margin (§9.6).
2. **Headers read as raw bytes** from `company_001_amazon/<name>.csv` and written back verbatim as line 1 of
   each register, so column drift cannot originate at the merge. All 169 rows are at the Amazon width;
   **0 width drift, 0 empty cells** except §13's permitted blank `derived_arithmetic` on non-derived rows.
3. **Fold, never drop** — 180 requested rows into 169, with 11 cross-part collisions folded and each absorbed
   emission named inside the kept row. 0 refused, 0 silent normalisations.
4. **Central id minting through the locked allocator** (RD-131/RD-132), never a snapshot of free ranges.
5. **The `AMBIGUOUS` register pair was attributed by content** (RD-132): the parts' own leading `notes` tags
   decide `validation` vs `failures` — 13 and 10, none dropped.
6. **Corrections propagate** — COR-01…COR-08 reach both the register rows that carried the withdrawn claim and
   the volume (`CORRECTIONS.md`); the instruction layer was swept and holds no stale Alphabet value.

## Collision groups (all 11, in full)

| kept row | absorbed emission | same record because |
|---|---|---|
| `sources.csv` S4335 / P1SRC04 | `s1_p2.md P2SRC02` | one accession `0001193125-04-073639` — the S-1 as filed, emitted twice |
| `timeline.csv` P1TML16 | `s1_p2.md P2TML13` | 2002-04 `(PB)` Overture patent suit, one event |
| `validation.csv` P2VAL04 | `s1_p1.md P1VAL06` | FY2001 profitability, one signal, two bases |
| `failures.csv` P2FAI03 | `s1_p1.md P1FAI02` | unregistered 1998/2003-plan equity, one liability |
| `channels.csv` P1CHN02 | `s1_p2.md P2CHN01` | direct sales force selling text ads per display |
| `channels.csv` P1CHN03 | `s1_p2.md P2CHN02` | self-service advertising (AdWords), 2000-Q4 |
| `channels.csv` P1CHN04 | `s1_p2.md P2CHN05` | free index inclusion / un-billed traffic |
| `data_gaps.csv` P1GAP01 | `s1_p2.md P2GAP01` | first licensee identity (`U.031`) |
| `data_gaps.csv` P1GAP04 | `s1_p2.md P2GAP03` | query traffic / index size (`U.033`) |
| `data_gaps.csv` P1GAP05 | `s1_p2.md P2GAP02` | pre-IPO rounds (`U.032`) |
| `data_gaps.csv` P1GAP09 | `s1_p2.md P2GAP12` | the interior voice of the period |

STATUS: WRITTEN 2026-09-30 (alphabet-s1-merge)
