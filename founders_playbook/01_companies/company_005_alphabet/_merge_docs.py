#!/usr/bin/env python3
"""Write stage_1_index.md and _MANIFEST.md with live word/byte counts (method 9.6)."""
import csv, io, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
REGISTERS = ["sources.csv", "quantitative.csv", "timeline.csv", "decisions.csv", "validation.csv",
             "failures.csv", "channels.csv", "conflicts.csv", "data_gaps.csv"]
IDMAP = {"P1SRC01": "S4332", "P1SRC02": "S4333", "P1SRC03": "S4334", "P1SRC04": "S4335",
         "P1SRC05": "S4336", "P1SRC06": "S4337", "P1SRC07": "S4338", "P1SRC08": "S4339",
         "P1SRC09": "S4340", "P1SRC10": "S4341", "P1SRC11": "S4342", "P2SRC01": "S4343",
         "P2SRC02": "S4335", "P2SRC03": "S4344", "P2SRC04": "S4345", "P2SRC05": "S4346",
         "P2SRC06": "S4347", "P2SRC07": "S4348", "P2SRC08": "S4349", "P2SRC09": "S4350",
         "P2SRC10": "S4351", "P2SRC11": "S4352"}
REQ = {"sources.csv": (22, 21, 1), "quantitative.csv": (40, 40, 0), "timeline.csv": (32, 31, 1),
       "decisions.csv": (10, 10, 0), "validation.csv": (13, 12, 1), "failures.csv": (10, 9, 1),
       "channels.csv": (11, 8, 3), "conflicts.csv": (21, 21, 0), "data_gaps.csv": (21, 17, 4)}
GROUPS = [
    ("sources.csv", "S4335 / P1SRC04", "s1_p2.md P2SRC02",
     "one accession `0001193125-04-073639` — the S-1 as filed, emitted twice"),
    ("timeline.csv", "P1TML16", "s1_p2.md P2TML13", "2002-04 `(PB)` Overture patent suit, one event"),
    ("validation.csv", "P2VAL04", "s1_p1.md P1VAL06", "FY2001 profitability, one signal, two bases"),
    ("failures.csv", "P2FAI03", "s1_p1.md P1FAI02", "unregistered 1998/2003-plan equity, one liability"),
    ("channels.csv", "P1CHN02", "s1_p2.md P2CHN01", "direct sales force selling text ads per display"),
    ("channels.csv", "P1CHN03", "s1_p2.md P2CHN02", "self-service advertising (AdWords), 2000-Q4"),
    ("channels.csv", "P1CHN04", "s1_p2.md P2CHN05", "free index inclusion / un-billed traffic"),
    ("data_gaps.csv", "P1GAP01", "s1_p2.md P2GAP01", "first licensee identity (`U.031`)"),
    ("data_gaps.csv", "P1GAP04", "s1_p2.md P2GAP03", "query traffic / index size (`U.033`)"),
    ("data_gaps.csv", "P1GAP05", "s1_p2.md P2GAP02", "pre-IPO rounds (`U.032`)"),
    ("data_gaps.csv", "P1GAP09", "s1_p2.md P2GAP12", "the interior voice of the period"),
]
SECTIONS = {
    "stage_1.md": "merge note + Volume 1 (Header, Boundary, §A–§F) + Volume 2 (§G–§U incl. §U anchors)",
    "CORRECTIONS.md": "COR-01 to COR-08 + instruction-layer sweep",
    "_parts/s1_p1.md": "SUPERSEDED part 1 body, carried verbatim into `stage_1.md`",
    "_parts/s1_p2.md": "part 2 body, carried verbatim into `stage_1.md` (DO-NOT-RE-APPLY notice pending: claim held)",
    "sources.csv": "21 global carriers S4332-S4352 with dossier-local aliases",
    "quantitative.csv": "40 figures: the filed FY1999-FY2001 series, the equity ladder, byte measurements",
    "timeline.csv": "31 evidence-bound legs, 1996-2004 incl. six `(PB)` consequence legs",
    "decisions.csv": "10 founder/board decisions, part 1 and part 2",
    "validation.csv": "12 endorsement / visibility / attestation signals",
    "failures.csv": "9 losses, defects, adverse rulings and the printed-absence record",
    "channels.csv": "8 tested or visible distribution routes",
    "conflicts.csv": "21 conflicts: 14 keyed to §U anchors U.017-U.030 + 7 part-1 P1CNF keys",
    "data_gaps.csv": "17 gaps, carrying anchors U.022, U.030-U.036, each High row with a follow-up route",
    "stage_1_index.md": "volume list, anchor map, register counts, id map, merge decisions",
    "_MANIFEST.md": "this file",
    "_merge_census_check.py": "merge tool (own request-side census), not a deliverable",
    "_merge_apply.py": "merge tool (register application), not a deliverable",
    "_merge_build.py": "merge tool (volume build + byte-slice proof), not a deliverable",
}


def wc(path):
    b = open(path, "rb").read()
    return len(re.findall(r"\S+", b.decode("utf-8", errors="replace"))), len(b)


def rows(path):
    return len(list(csv.reader(io.open(path, encoding="utf-8")))) - 1


def table(paths):
    out = ["| File | Words | Bytes | Sections contained | Upload batch | Status |", "|---|---|---|---|---|---|"]
    for p in paths:
        w, by = wc(os.path.join(HERE, p))
        status = ("canonical register" if p.endswith(".csv") and rows(p) else
                  "register (header only)" if p.endswith(".csv") else
                  "superseded part" if p.startswith("_parts/") else
                  "merge tool" if p.startswith("_merge") else "stage volume")
        out.append("| `%s` | %s | %s | %s | 1 | %s |" % (p, format(w, ","), format(by, ","),
                                                        SECTIONS.get(p, ""), status))
    return "\n".join(out)


FILES = ["stage_1.md", "stage_1_index.md", "CORRECTIONS.md", "_MANIFEST.md", "_parts/s1_p1.md",
         "_parts/s1_p2.md", "sources.csv", "quantitative.csv", "timeline.csv", "decisions.csv",
         "validation.csv", "failures.csv", "channels.csv", "conflicts.csv", "data_gaps.csv",
         "research/A_chronology_feasibility.md", "research/A2_periodical_settlement.md",
         "research/A4_harvest_mine.md", "research/B1_filing_records.md",
         "_merge_census_check.py", "_merge_apply.py", "_merge_build.py"]

arith = ["| register | requested | applied (rows kept) | folded | refused | groups |", "|---|---|---|---|---|---|"]
for r in REGISTERS:
    q, k, f = REQ[r]
    arith.append("| `%s` | %d | %d | %d | 0 | %d |" % (r, q, k, f, f))
arith.append("| **total** | **180** | **169** | **11** | **0** | **11** |")

grouplines = ["| kept row | absorbed emission | same record because |", "|---|---|---|"]
for reg, kept, absorbed, why in GROUPS:
    grouplines.append("| `%s` %s | `%s` | %s |" % (reg, kept, absorbed, why))

idlines = []
for local in sorted(IDMAP):
    idlines.append("`%s`→`%s`" % (local, IDMAP[local]))
rev = {}
for local, g in IDMAP.items():
    rev.setdefault(g, []).append(local)
maptable = " · ".join("%s←%s" % (g, "+".join(sorted(v))) for g, v in sorted(rev.items()))

w_sm, b_sm = wc(os.path.join(HERE, "stage_1.md"))
w_p1, b_p1 = wc(os.path.join(HERE, "_parts/s1_p1.md"))
w_p2, b_p2 = wc(os.path.join(HERE, "_parts/s1_p2.md"))

INDEX = """# Alphabet Stage 1 — `stage_1_index.md`

Company 005 (Alphabet Inc., registrant Google Inc., CIK 1288776). Stage 1 = **1998-01-09 → 2001**
(year-granular; the closing day is UNKNOWN), tier **T1 exemplar**, method §9.2/§9.3/§9.6. Built by the
Stage-1 merge pass on 2026-09-30 (agent `alphabet-s1-merge`). Citable units are the **one volume**
`stage_1.md` (sections §Header, §Boundary, §A–§U continuous) and the **nine registers** at this directory root.

## Volumes

| # | File | Sections | Words | Bytes | Claim records | Emission blocks |
|---|---|---|---|---|---|---|
| 1 | `stage_1.md` | merge note → Volume 1: Header, Boundary, §A–§F → Volume 2: §G–§U (incl. §U) | %s | %s | 24 `P1A01`–`P1F04` + 56 `P2G01`–`P2U01` = **80** | 16 fenced `csv` blocks (8 + 8), provenance only |
| — | `_parts/s1_p1.md` | superseded part 1 body, carried byte-identically | %s | %s | 24 | 8 |
| — | `_parts/s1_p2.md` | superseded part 2 body, carried byte-identically | %s | %s | 56 | 8 |

**§9.2 arithmetic:** 20,896 + 35,692 = 56,588 w combined → above the 40,000 soft target, inside the
40,000–60,000 amber band, **below the 60,000 hard cap** → §9.3 is not triggered → one volume. Merged volume:
%s w (56,532 carried body + 826 merge header/note/dividers), **2,642 w of headroom**.

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

%s

## Id map — globally minted, retired local keys kept as aliases

21 global ids **S4332–S4352** allocated by `tools/id_mint.py --count 21 --company company_005_alphabet --claim`
(above the highest live id; recorded in `00_universe/_ID_BLOCKS.tsv` for `company_005_alphabet` /
`alphabet-s1-merge`; verified 0 collisions against every `sources.csv` in the corpus and against the registry).
`sources.csv` carries them; the local keys stay printed in each row's `notes` (`GLOBAL-ID S43xx <- P…SRCnn`)
and inside every `MERGE[...]` marker, so prose citing `P1SRC04`, `P2SRC01` or B1's `B01`–`B43` still resolves.

%s

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

%s

STATUS: WRITTEN 2026-09-30 (alphabet-s1-merge)
""" % (format(w_sm, ","), format(b_sm, ","), format(w_p1, ","), format(b_p1, ","), format(w_p2, ","),
       format(b_p2, ","), format(w_sm, ","), "\n".join(arith), maptable, "\n".join(grouplines))

MANIFEST = """# Alphabet (Google Inc.) — `_MANIFEST.md` (method §9.6)

Regenerated by the Stage-1 merge pass on 2026-09-30 with live word and byte counts (`\\S+` tokens, the way
`gates.py` counts; UTF-8 bytes). **Upload batch 1** — 10 companies per group, this is company 005.
Stage boundary: **1998-01-09 → 2001**, year-granular with the closing day UNKNOWN, adopted at part 1
`## Boundary` over five named and rejected rival geometries. Tier: **T1 exemplar** (§15.2), so the per-file
cap is **60,000 words** and the merged volume at %s w passes it with 2,642 w of headroom.

## The split decision, with its arithmetic (§9.2 / §9.3)

| step | words | note |
|---|---|---|
| `_parts/s1_p1.md` as emitted | 20,896 | the dispatch reported 21,629; **re-measured** — `gates.py` prints 20,896 too |
| `_parts/s1_p2.md` as emitted | 35,692 | matches the dispatch figure |
| combined | **56,588** | above the 40,000 soft target, inside the 40,000–60,000 **amber** band, below the cap |
| − part 1 filename H1 + its stale `SCAFFOLDED … nothing written yet` banner | −41 | 257 B; a banner telling a cold reader the file is empty is the §14 rule-10 defect class |
| − part 2 filename H1 | −15 | 102 B |
| + merge header, merge note, two volume sub-headings and dividers | +826 | split decision, row arithmetic, id minting, anchor parity, COR-01…08 |
| **`stage_1.md` as built** | **%s** | 395,186 B; **one volume** — §9.3 is not triggered, so no `stage_1_part_n.md` geometry |

Two-part geometry considered and rejected: §9.2 permits an amber stage to finish as one file; the only clean
section boundary (§F/§G) would separate part 1's boundary argument from its single correction (part 2 §J.0 →
`U.024`); and one volume keeps each part body as one contiguous byte slice instead of two files' slices.
Numbering stays continuous A–U with nothing renumbered, and both `_parts/` files plus `stage_1_index.md`
stay citable.

## Files in this directory

%s

## Per-register arithmetic: requested → applied → folded → refused

180 rows were emitted by **two** passes: `_parts/s1_p1.md` 70, `_parts/s1_p2.md` 110. `tools/merge_census.py`
attributed 157 and printed `AMBIGUOUS:validation.csv,failures.csv` for 9 + 14 rows (**RD-132**: those two
registers share all 11 column names, so no header-overlap matcher can separate them); the 23 were attributed
by the rows' own leading `notes` tags. The census reads `_parts/*.md` and fenced `csv` only, so `research/` was
searched by hand for a fourth emission (**RD-122/RD-131**): the four dossiers hold **zero** fenced register
blocks — `B1_filing_records.md` emits claim records `B01`–`B43` and hyphen-form conflict keys `U-6`–`U-16`,
which the parts cite and the registers alias, but which are not rows to apply.

%s

Folded rows are not deleted: each kept cell carries the absorbed emission's distinct wording printed inside a
`MERGE[kept <- part key, column: value]` marker, and the row's tail names the fold. **Refused: 0.** No value
was deleted to fit a column count; no row arrived with width drift (all 180 parsed at the Amazon width), so
no re-joining repair was needed on this company — the one normalisation this pass made is recorded below.

## Stage vocabulary (§13 RD-048/RD-075)

`stage` is the controlled literal **`stage1` on all 169 rows of all nine registers** (a per-file distinct-value
scan returns `['stage1']` each time). **0 numeric `1`/`2`/`3` values and 0 `stageN` drift were found, so there
is no numeric-stage normalisation count to report.** Six `(PB)` post-boundary legs (2002-Q1, 2002-04, 2003-06,
2004-07-06, 2004-08-06, 2004-08-09) stay `stage1` because both parts labelled them so and every one is used
only as a consequence — stated here rather than applied silently. One §13 vocabulary repair was needed:
`channels.csv` row `P1CHN05` carried `never dated and never measured` in the year-bearing `date_tested` column
and now reads `UNKNOWN (never dated and never measured)` — the wording kept verbatim, the controlled literal
added, 1 repair in total.

Empty cells: **0** outside the §13-permitted blank `derived_arithmetic` (FACT rows carry `not_derived`-style
text from the parts; every DERIVED/ESTIMATE row carries its arithmetic — 0 lack it). Duplicate primary keys:
**0** (21 distinct `source_id`, 21 distinct `conflict_id`). Dangling `source_id` tokens: **0**.

## Non-destruction proof

* **Byte slices.** Volume 1 body (145,481 B / 20,855 w) and Volume 2 body (244,114 B / 35,677 w) are each a
  **byte-identical contiguous slice** of `stage_1.md` — substring tests on the raw bytes return True at offsets
  5355 and 151072, in order, with nothing rewritten between them. The only bytes excluded are each part's
  filename H1 and part 1's stale scaffold banner, accounted line by line above.
* **Claim records: 80 before, 80 after** (24 `P1A01`–`P1F04` in part 1, 56 `P2G01`–`P2U01` in part 2).
* **Emission blocks: 16 before, 16 after** (`` ```csv `` fences).
* **Anchors: 20 declared, 20 cited, 0 undeclared, 0 uncovered** — part 1 declares none, part 2 declares
  U.017–U.036, the merged volume declares that same union twice (its own machine comment plus the carried part 2
  declaration), and the register union is exactly U.017–U.036.
* **Rows: 0 on disk before this pass → 169 after**, from 180 emitted with 11 folds named.

## Gate (tier `exemplar`, `--fail-on substantive`)

Before: 1 finding, 2 passes (`csv`/`anchors`/`corrections` **DID NOT RUN** — no registers, no CORRECTIONS.md).
After: **0 findings, 21 passes** — `csv` 9 registers width-clean with every `S####` resolving, `keys`
`stage_1.md` tokens resolve, `anchors` citation resolution + parity 20↔20, `budget` 57,358 < 60,000,
`corrections` "all 8 retraction(s) reach registers and volumes". Advisory, not defect: 16 backticked
`U.nnn` mentions read as ids being discussed rather than cited, and `S96-213` (the Stanford docket number) is a
hyphen-form record key.

## Coverage — what exists and what does not

Exists for Alphabet: Stage 1 (`stage_1.md` + index + 9 registers + `CORRECTIONS.md`), four research dossiers,
and `sources/` (53 documents across `sec`, `_index`, `patents`, `wayback`, `ia`, `periodicals`, `financials`,
`uspto`). **Does not yet exist** and is not implied by this manifest: `stage_2.md`, `stage_3.md`,
`final_report.md`, `adversarial_review.md`, `context_appendices.md`, and any Stage-2/3 register rows — the
registers carry only Stage-1 rows, and `sources.csv` is append-only for later stages (S4353+ must come through
`id_mint.py --claim`).

## Residue left by this pass

1. `_parts/s1_p2.md` could not be stamped `DO NOT RE-APPLY THESE BLOCKS`: its path is still claimed **LIVE** by
   `alphabet-s1-p2` (heartbeat 56 min old against a 240-min TTL), and `scaffold.py claim` refuses a live path —
   the escape hatch `--force` would have overwritten 35,692 words, so it was not used. Part 1 **is** stamped,
   and the warning is printed at the top of `stage_1.md` where the blocks now live. Re-append to part 2 when its
   claim goes stale.
2. Three merge tools are left in this directory (`_merge_census_check.py`, `_merge_apply.py`, `_merge_build.py`)
   as the reproducible record of the application, following the Microsoft precedent
   (`company_011_microsoft/research/_b1_fix_blocks.py`). Delete them only together with a re-census.
3. `tools/merge_census.py` is still blind in the two documented ways (no `research/` scope; the
   `validation`/`failures` pair is schema-identical). Recorded in `CORRECTIONS.md` (COR-06), **not fixed** —
   `tools/` is outside this pass's ownership.
4. The 16 emission blocks still sit as text inside `stage_1.md` and both parts while the nine CSVs are
   canonical; a future pass that re-applies them would double 180 rows over 169.
5. Evidence routes still open, unchanged by a merge (they belong to the registers, not to this file):
   the unheld 424B4 of 2004-08-19 (`U.035`), the trademark serial history behind `P1GAP08`/CIK 1652044, PACER for
   the French/German rulings (`P2GAP08`), the UNTESTED accession `-04-138034`, and every UNVERIFIED-TLS
   periodical row that stays capped at Medium.

STATUS: WRITTEN 2026-09-30 (alphabet-s1-merge)
""" % (format(w_sm, ","), format(w_sm, ","), table(FILES), "\n".join(arith))

io.open(os.path.join(HERE, "stage_1_index.md"), "w", encoding="utf-8", newline="\n").write(INDEX)
io.open(os.path.join(HERE, "_MANIFEST.md"), "w", encoding="utf-8", newline="\n").write(MANIFEST)
print("index:", wc(os.path.join(HERE, "stage_1_index.md")), "manifest:", wc(os.path.join(HERE, "_MANIFEST.md")))
