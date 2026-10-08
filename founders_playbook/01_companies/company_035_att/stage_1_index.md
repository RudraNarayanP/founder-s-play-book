# stage_1_index.md — company_035_att, Stage 1 (1875-01-01 → 1915-12-31)

Written by the Stage-1 merge pass (`merge-att`, 2026-10-07). This is a **map, not a volume**: it says where each
addressable thing lives so a cold reader does not have to re-derive it. It carries no claim and no evidence. The
volume is `stage_1.md`; the data is the nine registers at this root; the emission of record is
`_parts/s1_p1.md` (read-only).

## Reading order

1. `stage_1.md` **§Header 1** — the four legal persons (P1 Bell Telephone Company / American Bell, never a
   reachable registrant; **P2 = CIK 5907, New York, 1885**; P3 the seven 1983–84 RHCs; **P4 = CIK 732717,
   Delaware 1983 → SBC → AT&T Inc**, the ticker's registrant). Read it before any sentence of narrative: every
   section's first line names the person it describes, and the register `company` column follows the same rule.
2. `stage_1.md` **MERGE RECORD** (the head of the file) — what was applied, the `P1Snn` → `S44nn` id map, the
   `validation`/`failures` binding, and the four things the merge refused to tidy.
3. `stage_1.md` **§Boundary** — why 1875 is a search floor that prints 0, why 1915 is carried **in the future
   tense**, and why 1984-01-01 creates a registrant but is not Stage 1.
4. `stage_1.md` **§A–§R** (narrative + claim records), then **§S** (gaps, `FETCH REQUEST` R-1…R-5, `UNTRIED`),
   **§T** (provenance and the five-family ledger), **§U.1–§U.9** (the conflicts).
5. The registers, for anything tabular; `_MANIFEST.md` for live counts; `CORRECTIONS.md` for what is superseded.

## Address spaces (nothing here is renumbered)

| thing | form | where it is minted | example |
|---|---|---|---|
| claim records | `BD01`–`BD04`, `A01`…`U01` — **56**, all distinct | inside `stage_1.md`, one block per section (`### Claim records (§X)`) | `BD02` carries the 1915 future-tense finding |
| §P metric rows | `P01`–`P50` (+ the `P14` non-footing row cited by name) | `stage_1.md` §P table → `quantitative.csv` rows in the same order | `P14` = printed annual traffic 8,770,300,000, which does not foot |
| conflict anchors | `U.1`–`U.9` | declared at §U by `<!-- ANCHORS: U.1-U.9 -->`; one `conflicts.csv` row each | see the home map below |
| source keys, global | `S4449`–`S4462` | `00_universe/_ID_BLOCKS.tsv` via `tools/id_mint.py --claim --agent merge-att`; 14 rows in `sources.csv` | `S4449` = the FY1913 report |
| source keys, dossier-local | `P1S01`–`P1S14` | `_parts/s1_p1.md` and the **narrative** of `stage_1.md` only; superseded in every register cell by **COR-01** | `P1S01` ≡ `S4449` |
| registrant/person labels | `P1`–`P4` | §Header 1 table; carried in the register `company` column | — |

## Anchor → register homes (measured over the nine CSVs after application)

| anchor | §U heading in `stage_1.md` | register cells citing it (conflicts.csv always holds the row itself) |
|---|---|---|
| `U.1` | Which registrant answers the brand, and why the name route cannot tell you | `sources.csv` ×7, `timeline.csv` ×1, `conflicts.csv` ×2 |
| `U.2` | "Founded 1877" vs incorporated 1885 vs created 1983 | `sources.csv` ×3, `timeline.csv` ×4, `conflicts.csv` ×2 |
| `U.3` | The 1895 experiment and the 1915 opening against what a contemporaneous document prints | `quantitative.csv` ×1, `sources.csv` ×1, `timeline.csv` ×2, `conflicts.csv` ×2 |
| `U.4` | 1984-01-01: one event, two directions, two persons | `sources.csv` ×2, `timeline.csv` ×2, `conflicts.csv` ×2 |
| `U.5` | Internal inconsistencies inside one held document (and one OCR class) | `quantitative.csv` ×3, `failures.csv` ×1, `sources.csv` ×2, `timeline.csv` ×2, `conflicts.csv` ×2 |
| `U.6` | December 19, 1913: voluntary adjustment or compelled concession | `decisions.csv` ×1, `validation.csv` ×1, `channels.csv` ×1, `sources.csv` ×1, `timeline.csv` ×1, `conflicts.csv` ×2 |
| `U.7` | Who owns the legacy: the 2005 acquirer's sentence against the 1983 recital | `sources.csv` ×4, `conflicts.csv` ×2 |
| `U.8` | Whose incorporation, and with how much money | `failures.csv` ×1, `sources.csv` ×2, `timeline.csv` ×1, `conflicts.csv` ×2 |
| `U.9` | Whose words are inside the 1908 pamphlet between l.204 and l.273 | `data_gaps.csv` ×1, `sources.csv` ×3, `conflicts.csv` ×2 |

**Parity: 9 declared anchors ↔ 9 register anchors, every anchor has at least one home outside `conflicts.csv`, and
no register cites an anchor that §U does not declare.** Line locators (`l.238`, `l.5091`) are locators, not
addresses: they point into the held bytes under `sources/`, which no pass in this operation edited.

## What is deliberately NOT in the register layer

* No source row is minted for the DTIC document code printed as `S6-11-25-ATT`; it is quoted as print in §Header 1
  and §T.6, and `gates.py --checks keys` lists `S6-11` for review — that is the expected reading, not a defect
  (`CORRECTIONS.md`, "Not corrected, and why" item 2).
* No row was invented for a family that returned nothing: (b) web archives and (e) auction/museum/manuscript are
  **UNTRIED for lack of any route**, stated with the route each would need (§T.5, §S UNTRIED 1–2).
* The five `FETCH REQUEST` blocks are the orchestrator's dispatch list, not this pass's retrievals, and the two
  out-of-window P4 timeline rows stay marked `OUT OF WINDOW` rather than being moved to a Stage-2 register.
