#!/usr/bin/env python3
"""Build stage_1.md from the two part bodies, proving non-destruction by byte slice."""
import io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
P1 = os.path.join(HERE, "_parts", "s1_p1.md")
P2 = os.path.join(HERE, "_parts", "s1_p2.md")
OUT = os.path.join(HERE, "stage_1.md")


def words(b):
    return len(re.findall(r"\S+", b.decode("utf-8", errors="replace")))


def slice_after(text, nlines):
    """bytes of `text` after dropping the first `nlines` lines (the filename H1 / stale banner)"""
    pos = 0
    for _ in range(nlines):
        pos = text.index(b"\n", pos) + 1
    return pos


HEADER = (
    "# Alphabet (Google Inc.) — Stage 1: the origin block, 1998-01-09 to 2001\n"
    "\n"
    "<!-- ANCHORS: U.017-U.036 -->\n"
    "\n"
    "**Dataset:** The Founder's Playbook, company 005 (Alphabet Inc., registrant Google Inc., CIK 1288776), "
    "Stage 1. **Tier T1 exemplar** (method §15.2), so the per-file cap is 60,000 words. **Canonical structured "
    "data is the nine CSV registers at this directory root** — the fenced `csv` blocks printed below are the "
    "parts' emissions, carried verbatim as provenance. **DO NOT RE-APPLY THOSE BLOCKS: they are already "
    "applied, 180 requested rows into 169 register rows (11 folded, 0 refused), and a second application would "
    "double-count them.**\n"
    "\n"
    "## Stage 1 merge note\n"
    "\n"
    "**Geometry (method §9.2/§9.3, arithmetic stated).** The two part bodies measure 20,855 and 35,677 words "
    "(145,481 B and 244,114 B) once each part's filename H1 and part 1's stale `SCAFFOLDED … nothing written "
    "yet` banner are dropped (−41 w and −15 w: 257 B and 102 B); as emitted, `_parts/s1_p1.md` is 20,896 w (not the 21,629 w my brief reported) and `_parts/s1_p2.md` 35,692 w, so "
    "**56,588 w combined — above §9.2's 40,000 soft target, inside the 40,000-60,000 amber band, and 3,412 w "
    "below the 60,000 hard cap for a T1 company, and the built volume lands 2,642 w below it**. §9.2 permits an amber stage to finish as one file and §9.3 "
    "triggers a split only *at* the cap, so this stage is merged as the single volume `stage_1.md` "
    "(**57,358 w / 395,186 B** as built) and no `stage_1_part_n.md` geometry is used. The two-part alternative was "
    "rejected on three grounds: it would put the §9.3 test to a file that has not hit the cap; a split between "
    "§F and §G would strand the boundary argument (part 1) from its one correction (part 2 §J.0 / U.024), which "
    "sit on either side of the only clean section boundary; and one volume keeps both part bodies provably "
    "intact. **§A–§U numbering is continuous and nothing was renumbered** (§9.3), and §9.6 forbids "
    "trimming evidence to fit a limit, which is why no content was cut to buy margin.\n"
    "\n"
    "**Carried stale prose, named not edited.** Part 1's Header still prints `**File:** part 1 of 3 for Stage "
    "1.`; the corpus has two parts and this pass built one volume. The sentence sits inside a protected byte "
    "slice, so it is corrected here rather than rewritten there, and §9.3 forbids renumbering a part to make a "
    "carried volume look self-contained.\n"
    "\n"
    "**What was applied.** 180 register rows from two emissions — 70 in `_parts/s1_p1.md` (§Header, §Boundary, "
    "§A–§F) and 110 in `_parts/s1_p2.md` (§G–§U) — into nine registers as **169 rows: 11 folded into 11 listed "
    "collision groups, 0 refused**. `tools/merge_census.py` attributed only 157 of them and printed the "
    "`validation.csv`/`failures.csv` pair as `AMBIGUOUS:validation.csv,failures.csv` (9 rows + 14 rows): the "
    "two schemas share all 11 column names, so no header-overlap matcher can separate them (**RD-132**). Those "
    "23 were attributed by the rows' own leading `notes` tags — 13 `validation`, 10 `failures`, 0 dropped. The "
    "census also reads `_parts/*.md` and fenced `csv` only, so `research/` was searched by hand for a fourth "
    "emission (**RD-122/RD-131**): `B1_filing_records.md`, `A_chronology_feasibility.md`, "
    "`A2_periodical_settlement.md` and `A4_harvest_mine.md` contain **zero** fenced blocks — B01–B43 are claim "
    "records and U-1–U-16 hyphen-form keys, cited and aliased in register `notes`, never rows to apply.\n"
    "\n"
    "**Ids.** 21 global source ids, **S4332–S4352**, allocated through the locked `tools/id_mint.py --claim` "
    "(above the highest live id; recorded in `00_universe/_ID_BLOCKS.tsv` against `company_005_alphabet` / "
    "`alphabet-s1-merge`) — not from a snapshot of free ranges, which is how RD-132's near-collision happened. "
    "Checked against the live register corpus and the registry before application: 0 collisions. The retired "
    "dossier-local keys `P1SRC01`–`P1SRC11` / `P2SRC01`–`P2SRC11` stay printed in the `notes` cell of the row "
    "that replaces them and inside every `MERGE[...]` marker (**COR-07**).\n"
    "\n"
    "**Anchors.** Part 1 minted and declared **none** (zero `U.n` tokens in `_parts/s1_p1.md`); part 2 declares "
    "**U.017–U.036 (20)**, which is therefore the union, restated in the machine comment above. The upstream "
    "dossiers' hyphen-form keys (`U-1`–`U-16`) are a different namespace and are not anchors. Register-cited "
    "anchors: exactly 20 distinct, **U.017–U.030 in `conflicts.csv`, U.031–U.036 in `data_gaps.csv`** → parity "
    "20 narrative ↔ 20 register, 0 undeclared, 0 uncovered.\n"
    "\n"
    "**Corrections on this pass: COR-01 … COR-08** (full text in `CORRECTIONS.md`, each tagged into the "
    "register rows that carried the withdrawn claim): COR-01 the probe's Q1-1999 close and the 1996-2004 "
    "harvest window, both refuted at §Boundary; COR-02 the records dossier's single-file-number lineage map; "
    "COR-03 part 1's 'no cost figure before 2003 / no carrier' leg; COR-04 refusal (iii)'s 'no money quantum' "
    "half; COR-05 the undated rescission ceiling; COR-06 the tool-blind shared register blocks; COR-07 the "
    "retired local source keys; COR-08 two carried citation defects (a line range that stops mid-sentence, a "
    "byte count the disk contradicts).\n"
    "\n"
    "## Volume 1 — origin block (Header, Boundary, §A–§F)\n"
    "\n"
    "*Carried byte-identically from `_parts/s1_p1.md`; its 24 claim records `P1A01`–`P1F04` and 8 emission "
    "blocks are intact below.*\n"
)
DIV2 = ("\n---\n\n## Volume 2 — channels, competition, scaling, money, closing blocks (§G–§U)\n\n"
        "*Carried byte-identically from `_parts/s1_p2.md`; its 56 claim records `P2G01`–`P2U01`, §U anchor set "
        "and 8 emission blocks are intact below.*\n\n")


def main():
    b1 = open(P1, "rb").read()
    b2 = open(P2, "rb").read()
    off1 = slice_after(b1, 3)
    # part 1 carries a DO-NOT-RE-APPLY notice that was appended AFTER this body was sliced;
    # cutting there keeps the volume at the part as merged (the notice stays provenance in the part file).
    cut = b1.find(b"## MERGED")
    b1 = b1[:cut] if cut > 0 else b1
    off2 = slice_after(b2, 2)   # H1, blank
    body1, body2 = b1[off1:], b2[off2:]
    hdr = HEADER.encode("utf-8")
    div = DIV2.encode("utf-8")
    merged = hdr + body1 + div + body2
    with open(OUT, "wb") as f:
        f.write(merged)
    chk = open(OUT, "rb").read()
    i1, i2 = chk.find(body1), chk.find(body2)
    print("part1 dropped prefix: %d B / %d w  %r" % (off1, words(b1[:off1]), b1[:60].decode("utf8", "replace")))
    print("part2 dropped prefix: %d B / %d w  %r" % (off2, words(b2[:off2]), b2[:60].decode("utf8", "replace")))
    print("body1 %d B %d w at offset %d | body2 %d B %d w at offset %d" %
          (len(body1), words(body1), i1, len(body2), words(body2), i2))
    print("byte-identical contiguous slice: body1=%s body2=%s" % (i1 >= 0, i2 >= 0))
    print("order preserved (body1 before body2): %s" % (0 <= i1 < i2))
    print("merged %d B / %d w ; header+divider = %d w ; accounted: %d + %d = %d" %
          (len(merged), words(merged), words(hdr) + words(div), words(body1) + words(body2),
           words(hdr) + words(div), words(merged)))
    t = chk.decode("utf-8")
    for label, pat in (("claim records P1", r"(?m)^\*{0,2}P1[A-F]\d{2} Claim:"),
                       ("claim records P2", r"(?m)^\*{0,2}P2[A-Z]\d{2} Claim:"),
                       ("fenced csv blocks", r"(?m)^```csv"),
                       ("ANCHORS decls", r"ANCHORS:")):
        print("%-22s %d" % (label, len(re.findall(pat, t))))
    print("anchors declared:", sorted(set(re.findall(r"ANCHORS: ([^>]*)", t))))
    print("cap headroom: %d w under 60,000" % (60000 - words(merged)))


main()
