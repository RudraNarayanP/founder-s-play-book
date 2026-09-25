# apple_s1_merge.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T20:01:00Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## Row application

STATUS: WRITTEN 2026-09-26 (apple-s1-merge)

**Inputs.** `_parts/s1_p1.md` minted 23 claim records (S1P1-12…34, plus 11 from the interrupted pass = 34 ids on
disk) and 10 part-local conflict keys (S1P1-CF-01…10) — **no register rows**; its output is narrative + appendix.
`_parts/s1_p2.md` minted 16 claim records (S1P2-01…16) and requested 27 rows. `_parts/s1_p3.md` minted the
canonical **U.001–U.055** spine and requested 85 rows. Column parity against each target header was validated
**before** writing (width by width, every row parsed with the `csv` module in RFC-4180 mode).

**Applied — 107 rows into 9 registers.** conflicts 25 (part 3, canonical `U.nnn`); data_gaps 35 (part 2's 5 +
part 3's 30); quantitative 14 (6 + 8); timeline 7; validation 6 (part 2); decisions 4; failures 6; sources 10
(9 mapped + 1 minted). Every applied row is verbatim from the requesting block **except** the mechanical repairs
listed in *Not applied and why* and the centrally assigned id cells (§13: `source_id` blocks are assigned at
merge, never per dossier).

**Refused — 5 rows, all of them part 2's `conflicts.csv` rows.** S1P2-CF-01…05 parse to **14 fields against a
15-column header**: the `residual_uncertainty` column is absent in all five, so a literal append would have
written a shifted record into the register. Nothing was lost by the refusal — each subject is carried twice-sided
by the canonical row it re-points to (S1P2-CF-01→U.005, -02→U.007, -03→U.003, -04→U.008, -05→U.009), and each
canonical row names the part-2 key as an alias in its last cell.

**Repaired so it could be applied — 7 rows, text unchanged.** `data_gaps.csv`: part 2's revenue-gap row and its
partnership-instrument row each carried an unquoted comma inside one cell (9 fields → 8 after quoting);
`quantitative.csv`: part 2's assembled-box-surcharge row had an unquoted comma in `metric` (13 → 12);
`sources.csv`: part 2's S1P2-S01/S02/S04/S05 rows omitted the `source_type` column entirely (17 → 18) — the
inserted labels ("Registrant filing", "Auction house catalogue", "Collector registry pages", "Club newsletter")
are the carrier descriptions those same rows already print, and part 3's parallel rows set the two-column pattern.

**Register counts before → after:** timeline 23→30 · quantitative 30→44 · conflicts 13→38 · sources 13→23 ·
data_gaps 0→35 · validation 0→6 · failures 0→6 · decisions 0→4 · channels 0→0 (created, header only).

## Key mapping and collisions

STATUS: WRITTEN 2026-09-26 (apple-s1-merge)

Every part-local and dossier-local key now has **exactly one canonical home**, the §U anchor, and no two ids mean
one thing. The full map is in `../01_companies/company_004_apple/stage_1_index.md`; the substance:

* `S1P1-CF-01…10` → U.001/U.002/U.012 · (CF-02 **not promoted**, boundary settled by decision with its cost at
  U.019) · U.003/U.004 · U.008 · U.055 · U.007 · U.005 · U.014 · U.018 · U.019.
* `S1P2-CF-01…05` → U.005, U.007, U.003, U.008, U.009.
* `U-AP-1…4` → U.001, U.003, U.006, U.005; `U-C-1…6` → U.001, U.005, U.006, U.003, U.011, U.013;
  `U-A2-1…13` → U.013, U.003, U.016, U.004, U.015, U.055, U.009, U.010, U.011, U.005+U.007 (split), U.013,
  U.017, U.002. The 13 legacy `conflicts.csv` rows were **left untouched** as dossier history; the alias is
  visible in the canonical row's `Maps:` cell, which is where §13 says global uniqueness lives.
* **Source ids assigned centrally:** S1P2-S01…05 → **S1M-01…05**; S1P3-S01/S02/S03/S05 → **S1M-06/07/08/09**;
  existing A2S-01…13 reused, never redefined (§9.4).
* **Collisions resolved rather than duplicated:** (1) `S1P3-S04` and `S1P2-S02` are the *same* Christie's lot 242
  object and its Sotheby's 2011-12-13 lot 241 custody chain — one lineage, one source → one row **S1M-02** with a
  visible collision note; S1P3-S04 was not given a second id. (2) The dossier-local `CS-01`, cited as a source key
  inside part 3's timeline and decisions rows, also lands on S1M-02 and is rewritten in those appended cells as
  `S1M-02 (was CS-01 local)`. (3) `CS-05` (patent register) was cited by requested rows but had **no** proposed
  register row, so the merge minted **S1M-10** with fields drawn only from part 2's S1P2-12 record and part 3's
  1977-04-11 timeline row — no evidence added — and re-pointed the cell to `S1M-10 (was CS-05 local)`.
  (4) Two retained near-duplicates are recorded, not deleted: the 1976-11-20 demonstration row in `timeline.csv`
  (dossier row + part 3's anchor-keyed U.033 row) and part 2's $675 / 101-system quantitative rows against existing
  dossier rows 12 and 14.
* **Claim-record ids were not renumbered anywhere:** S1P1-01…34, S1P2-01…16, S1P3-01…nn stand as minted; census
  below proves it.

## Registers created

STATUS: WRITTEN 2026-09-26 (apple-s1-merge)

Five registers did not exist for this company (part 3's merge contract item 5 is correct on the record):
`data_gaps.csv`, `decisions.csv`, `failures.csv`, `validation.csv`, `channels.csv`. Each was created in
`company_004_apple/research/` — the directory where Apple's registers already live, and the directory
`tools/gates.py::locate()` reads after the company root — with its **header row copied as raw bytes from
`company_001_amazon/<name>.csv`**, so drift by transcription is impossible. Verified against Amazon:
byte-equal headers, UTF-8, `\n` endings, no CRLF anywhere.

Rows: data_gaps **35** (part 2's 5 + part 3's 30, `U.025–U.054`, every High/VERY HIGH-importance gap carrying a
`follow_up_task` as §13 requires); decisions **4** (all four `claim_ref`s — S1P3-05 ×3, S1P3-06 — resolve to claim
records that exist in `stage_1.md` §N's block, verified by grep, so no dangling `claim_ref`); failures **6**;
validation **6**; **channels 0 rows, header only** — no part requested a channel row, and §I's channel material
(word of mouth, dealer advertisement, mail order, exhibitor list, direct mail) is narrated in §D.3/§F/§G/§L but
minting rows from prose would be inventing content the evidence passes did not stake. Recorded as an open shape,
not a filled one.

`stage` vocabulary: of the **107 rows this pass wrote** (and all **186** rows now on disk across the nine registers)
every `stage` cell carries the controlled literal
`stage1` (§13 vocabulary; numeric stage values would have failed the gate, and none were found in Apple's legacy
rows, so nothing needed normalising on touch).

## Volume split

STATUS: WRITTEN 2026-09-26 (apple-s1-merge)

Measured merged total: **65,250 words**, over the 60,000 hard cap if left as one file — so §9.3 applies and the
document is cut at **one** section boundary into two continuing volumes:

| Volume | Sections | Words | Bytes |
|---|---|---|---|
| `stage_1.md` (1 of 2) | Header + merge note, STAGE BOUNDARY JUSTIFICATION, §A–§U | **56,537** | 368,792 + header edit |
| `stage_1_part_2.md` (2 of 2) | §X consolidated untried routes, part 3 handoff, part 3 register-request blocks | **8,713** | ~65,000 |

The boundary is the end of §U — a section boundary, never mid-table or mid-claim-record-block — chosen because the
`U.nnn` spine §U mints is the addressable set the registers cite, and `gates.py`'s `NARR_GLOBS["stage1"]` reads
only `stage_1.md` (no `stage_1_part_*.md`, unlike its stage-2/3 entries). Cutting before §U would have hidden all
55 anchors from the parity gate and reported a failure that was geometry, not evidence. **That glob omission is a
gate defect logged for the audit pass**; volume 1 at 94% of cap is amber (§9.2) and is not split further.

Numbering continues and nothing was renumbered: §A–§U in volume 1, the §X continuation in volume 2, claim ids and
anchors untouched. Parts concatenated in part order, no sentence rewritten; removed only the two `# s1_pN.md`
titles and two stale `SCAFFOLDED … nothing written yet` comments (70 tokens), added 576 tokens of volume headers
and the merge note. **64,744 − 70 + 576 = 65,250** exactly. Non-destruction census, parts vs merged, identical:
claim records 66 distinct / 237 occurrences; part-local conflict keys 16 distinct; `U.nnn` 57 distinct;
dossier-local `[A-T]-\d{1,3}` 167 distinct / 1,391 occurrences. `_MANIFEST.md` and `stage_1_index.md` written; the
three `_parts/` files were **not edited** — each carries an appended `SUPERSEDED 2026-09-26` line instead.

## Anchor parity

STATUS: WRITTEN 2026-09-26 (apple-s1-merge)

**55 narrative anchors ↔ 55 register anchors; 0 residue in either direction**, measured twice: by
`gates.py --checks anchors` and independently (same declaration rule — line-start labels plus §U.i table cells —
run over `stage_1.md` **and** `stage_1_part_2.md`, and every `U.nnn` token in all nine registers). The spine is
**complete U.001–U.055**: no gap, no anchor declared without a citing row, no register token without a declared
anchor, and every anchor has ≥1 row (minimum 1 row/anchor; most carry 2–3 across conflicts/data_gaps/quantitative/
timeline/failures).

Gate evidence, before → after. **Before:** `Findings: 0 | Passes: 8`, but `anchors` read
`no register anchors found -- UNANSWERED, not passed` with `_parts/s1_p3.md declares 55 anchors` — the honest
pre-merge state part 3 predicted. **After:** `Findings: 0 | Passes: 17`,
`anchors parity 55 narrative anchors <-> 55 register anchors`, all nine registers width-clean
(timeline 30×11, quantitative 44×12, conflicts 38×15, sources 23×18, data_gaps 35×8, validation 6×11,
failures 6×11, decisions 4×15, channels 0×11), `budget` green on both volumes, `keys` green with one advisory note
(`stage_1.md cites 2 hyphenated record keys: S1M-01, S1M-10` — real register keys, resolved in `sources.csv`).

Residue named: none in the anchor layer. The two residues this pass could not close are elsewhere and are recorded,
not repaired — (a) part 2's 5 refused conflict rows above, and (b) the three requested edits inside
`_parts/s1_p1.md`, which §14 rules 4/12 bar a merge from making silently.

## Not applied and why

STATUS: WRITTEN 2026-09-26 (apple-s1-merge)

1. **`conflicts.csv` — part 2's 5 `S1P2-CF-*` rows: REFUSED.** 14 fields vs a 15-column header (no
   `residual_uncertainty`). Re-pointed to U.005/U.007/U.003/U.008/U.009, which restate both sides; no content lost.
2. **The three rewrites part 3 asked the merge to make inside `_parts/s1_p1.md`: NOT APPLIED.** S1P1-05/S1P1-06
   window labelling (U.019), S1P1-10's mis-pointed `Conflicts:` cell (U.011), the `Source`/`Tier`/`Conf` upgrades
   of S1P1-01…11. My brief binds the merged text to the parts verbatim and §14 rule 4 forbids tidying another
   pass's released words; U.011/U.019 already carry the merge action in the register, and the correction is
   handed to the audit pass in this sheet, in `stage_1_index.md` and in the merge note inside `stage_1.md`.
3. **`S1P3-S04`: NOT APPLIED as a second sources row** — same auction-lot lineage as S1P2-S02; folded into S1M-02
   with a collision note (§13 one-lineage-one-source).
4. **`channels.csv`: created empty.** No row was requested by any part; inventing them from prose is out of scope.
5. **Part 3's F1–F5 FETCH REQUESTs (routes U.037–U.054): NOT RUN.** They are the orchestrator's dispatch list;
   web budget on this pass was 0, and §14 rule 6 keeps each untried family named rather than a null.
6. **No de-duplication by deletion.** Retained near-duplicates: the 1976-11-20 timeline row (dossier + anchor-keyed
   U.033), part 2's $675 and 101/17.8% quantitative rows against existing dossier rows 12 and 14, and the 13
   legacy `U-A2-*` conflict rows. All collide visibly in `stage_1_index.md` with their canonical anchor named.
7. **Nothing deleted, moved or renamed** anywhere in the company: `_parts/` appended only, `research/` dossiers,
   `sources/`, `tools/` and all sibling companies untouched. Registers written by append (existing rows byte-intact).

**Carried-evidentiary-positions check (unchanged by the merge):** `$666.66` verified absent from every held byte and
still FOUNDER CLAIM/UNKNOWN (U.004); no in-window document gives 1976 price, order, units, revenue, supplier or a
founder officer title (U.003/U.026/U.027/U.047/U.014); Wayne 10%-vs-12%, Markkula terms, 50@$500,
word-of-mouth-vs-April-1977-BYTE-directory and $77,000-vs-$770,000 all still two-sided (U.005/U.007/U.003/U.008/
U.009) with no averaging anywhere; Apple's earliest EDGAR text is the 1994-01-26 / FY1994 Form 10-K, so everything
earlier is print and one lineage is one source (U.023/U.041, source row S1M-01).
