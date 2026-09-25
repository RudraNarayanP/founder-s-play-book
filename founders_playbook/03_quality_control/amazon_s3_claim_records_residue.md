# amazon_s3_claim_records_residue.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T20:50:52Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## Sweep

STATUS: WRITTEN 2026-09-25

Literal-digit sweep, not a line list: recursive over every `.md`/`.csv` under `company_001_amazon`
(including `_parts/`), pattern `0\.194995` plus the percent rendering of the same withdrawn value
`(?<![0-9])19\.4995`, counted per occurrence.

**Verified totals: 25 occurrences in 11 files** = 13 × `0.194995` + 12 × `19.4995`; **14 outside
`_parts/`** (9 + 5) and 11 inside the two pre-merge intermediates `_parts/s2_p4.md` (8) and
`_parts/s3_p4.md` (3).

**The brief's "ten occurrences across the company" does not reproduce and is reported as refuted, not
adopted.** It is a line-list count from `amazon_s3_retraction_register_repairs.md`: it misses the second
`0.194995` occurrence, which sits on a *different register row* of the same file (the stage-2 gross-margin
row in `quantitative.csv`, whose note carries the withdrawn reading), and it counts only the `0.` form, so
every `19.4995` rendering of the same withdrawn value is invisible to it. What the brief *does* get right,
and what I re-verified independently rather than trusting: **exactly six Stage-3 sites** — the stage-3
gross-margin row of `quantitative.csv`, the gross-margin row of `stage_3_pending_registers.md`, `§P188` and
`§P.2 t1` of `stage_3_part_3.md`, and records **P95** and **P179** of `stage_3_claim_records_part_1b.md` —
of which four were already repaired and **two were live, both in `stage_3_claim_records_part_1b.md`, both in
my ownership**. `stage_3_claim_records.md` and `stage_3_claim_records_part_2.md` returned **zero** hits: the
residue is narrower than "two volumes", it is one volume.

Classification of all 25 (correct / quoted-source / retraction marker / stale):

| class | count | where |
|---|---|---|
| **stale / live** (asserts the withdrawn quotient as fact, no supersession in the window) | **6 before → 4 after**, of which **2 → 0 were mine** | before: records **P95** and **P179** (both fixed here) plus 4 in the pre-merge intermediates — `_parts/s3_p4.md` `§P188`, `§P.2 t1` and its `stage3` register row, and `_parts/s2_p4.md`'s `stage2` register row. All 4 are outside my write set and are gated out of the 17-volume set: see §Handed off |
| **retraction marker** (withdrawn digits kept inside supersession language) | **19 before → 21 after** | 12 outside `_parts/`: `CORRECTIONS.md` 2, `quantitative.csv` 2 (its stage-2 **and** stage-3 gross-margin rows), `stage_2_claim_records.md` 1, `stage_2_claim_records_part_2.md` 1, `stage_2_part_2.md` 2, `stage_2_part_3.md` 1, `stage_3_part_3.md` 2, `stage_3_pending_registers.md` 1 — plus 7 in `_parts/s2_p4.md` (`⟪SUPERSEDED …⟫` banners and paired renderings). After this pass P95 and P179 join this class, which is the §14 rule 8 outcome: the withdrawn reading stays visible rather than being erased |
| **quoted source text** | 0 | the filing prints only "19.5%" (`10-K405/97` l.1403 as registered); `0.194995` appears **nowhere** in `sources/` — which is exactly why it was withdrawn rather than versioned |
| correct value present (`0.1950013` / `19.50013`) | 16 hits in 9 files before → **22 in 10 files after** | independent second sweep; the repaired sites print the right quotient, they were not merely stripped |

Tally check: 6 + 19 = 25 before, 4 + 21 = 25 after; 14 hits outside `_parts/` (2 live → 0) and 11 inside
(4 live, untouched).

## 0.194995 fixes

STATUS: WRITTEN 2026-09-25

Basis identity re-derived before writing anything (§14 rule 8): `28,813 ÷ 147,758 = 0.19500135…` →
**0.1950013**, i.e. **19.50013%**, which is what the FY1997 10-K405 renders as "19.5%" at l.1403. The
`0.194995` quotient corresponds to no pair of filed figures; the *restated* basis `28,818 ÷ 147,787 =
0.194935` is a different and correct figure and was left alone at both sites. Both edits keep the withdrawn
reading visible inside supersession language rather than erasing it (§14 rules 8 and 10), and match the
wording already used at the repaired sibling site `stage_3_part_3.md` `§P.2 t1`.

**1. Record P95 (gross margin, FY1997) — `stage_3_claim_records_part_1b.md`.** Was:
`(19.4995 filed / 19.4935 restated)`. Now:
`(exact quotient **19.50013 filed** / 19.4935 restated — superseded: this record printed the filed quotient
as **19.4995**, which is not 28,813 ÷ 147,758; AUDIT-3 D-06; the restated basis … is a different, correct
figure and stays)`. The record's conclusion — the rendering survives the restatement, the exact quotient
does not, so no FY1997 margin may be quoted to two decimals — is unchanged and is now true on both sides of
the comparison; before the fix the sentence cited to its own supporting pair in `P179` and reproduced the
withdrawant value as the filed one.

**2. Record P179 (DERIVED arithmetic, `§P.2 t1`) — same volume.** Was:
`Value: filed 28,813 ÷ 147,758 = 0.194995 → **19.5%**; restated 28,818 ÷ 147,787 = 0.194935 → **19.5%**`.
Now: `filed 28,813 ÷ 147,758 = **0.1950013** → **19.5%** (superseded: this line printed **0.194995**, which
is not the quotient — AUDIT-3 D-06); restated … = 0.194935 → **19.5%** (different basis, unchanged)`.

No other file was touched for this job: the four already-repaired Stage-3 sites, the register rows,
`CORRECTIONS.md`, every `stage_2*` file and both `_parts/` intermediates are outside my write set and are
classified in §Sweep rather than edited. Post-fix sweep of the three claim-record volumes: **0 live
occurrences, 2 retraction markers, word count 40,764 → 41,043** (still under the 60,000 cap; §9.2 is a
geometry limit, and nothing was trimmed to keep it).

## S3007 decision

STATUS: WRITTEN 2026-09-25

**Decision: NOT re-pointed. The finding is cleared by retracting a false sentence in place and printing a
named `UNRESOLVED(S3007: …)` marker in record S52, with the minting of any canonical pairing handed to the
register/re-key-map owner.** No carrier was invented.

Evidence read, in this order:

1. `03_quality_control/stage3_sourceid_rekey_map.md` — the ST3_C block pairs `S3001`→`S30053` through
   `S3006`→`S30058` and then jumps to `S3008`→`S30059`. **There is no ST3_C/S3007 row on the map at all.**
   The map's own instruction is decisive against guessing: "Resolution is by content, never by position;
   irreducible references are held, not guessed."
2. `sources.csv`, read with the stdlib csv reader (not a hand-rolled split, per §15.1) — **204 rows, 0 with
   key `S3007`**, and no 5-character `S3…` ids of any kind remain in the register.
3. `03_quality_control/stage3_register_merge_held_rows.md` row 8 — the key's *content* is on record: the
   width-refused 19-field `sources.csv` row from `ST3_C_product_market.md`, keyed `S3007`, =
   "8-K event 1998-10-28 (Q3-1998 results release)", acc 0000891020-98-001498, local
   `sources/8-K_event-1998-10-28_acc-0000891020-98-001498_filed-1998-10-28.txt`, supporting ST3C-50..ST3C-57.
4. `sources/` glob — **those bytes do exist on disk.** And the accession is registered canonically, once:
   `S30051` = "Forms 8-K, events 1998-10-28 and 1999-01-05" (ST3_B's `S3021`), url
   `…/1018724/0000891020-98-001498.txt`.

So the brief's branch test resolves the *hard* way: the **document** exists, but the **key** does not, and
`S30051` is not this row — it is another dossier's two-event row carrying another dossier's claim block,
while the refused row carried ST3C-50..ST3C-57. Re-pointing `S3007` → `S30051` would (a) mint an ST3_C
pairing the map owner never made, (b) silently convert an unwritten row into a written one, and (c) be the
exact "right-looking number in the wrong file" laundering pattern. Declined.

**The part the gate was actually firing on is worse than a dangling token and was in my file.** Record S52
(read in full before editing) asserted, inside the very record about the ten held rows: *"`S3007` exists in
`sources.csv` already and must not be re-defined (§13: reuse ids)."* That is false on the register as it
stands — a phantom-id instruction sitting in an instruction-bearing layer, which §14 rule 10 ranks as the
highest-severity home for a stale claim, since a later pass trusting it would "reuse" an id that resolves
nowhere. It is now retracted in place, with the count that disproves it (0 of 204) printed next to the
retraction, and the record states which evidence does exist (item 3, 4) and what it does not license.
Category note kept in the edit: this mention of the key was never a *citation* of the 8-K — it is a statement
about id existence inside a REGISTER DEFECT record, so even a correct document-level carrier could not
"resolve" it; only the register owner appending the row, or the map owner minting a pairing, can.

## Evidence

STATUS: WRITTEN 2026-09-25

Reproduction record for this pass (zero web calls, zero git calls; nothing created under `sources/`,
nothing deleted, moved or renamed):

- Occurrence sweep: `rg`-equivalent Python walk over `company_001_amazon/**` (`.md`, `.csv`) with
  `0\.194995` and `(?<![0-9])19\.4995`, counted per match with a ±125-char context window printed for each
  of the 25 hits, so classification is auditable rather than asserted. Per-file counts before the fix:
  `_parts/s2_p4.md` 2+6, `_parts/s3_p4.md` 2+1, `CORRECTIONS.md` 1+1, `quantitative.csv` 2+0,
  `stage_2_claim_records.md` 1, `stage_2_claim_records_part_2.md` 1, `stage_2_part_2.md` 1+1,
  `stage_2_part_3.md` 0+1, `stage_3_claim_records_part_1b.md` 1+1, `stage_3_part_3.md` 1+1,
  `stage_3_pending_registers.md` 1.
- Cross-check of the corrected value (`0\.1950013|19\.50013`): 16 occurrences in 9 files before the fix —
  i.e. the repaired sites were not merely stripped of the withdrawn digits, they print the right quotient.
- Post-fix re-sweep with a supersession-language heuristic: **0 unmarked live occurrences in any file I
  own**; the only remaining flag-ables are the 4 `_parts/` intermediates and `CORRECTIONS.md` (whose hit is
  a paired withdrawn/correct marker — the heuristic's window, not the text, is what misreads it).
- `sources.csv`: read with `csv.DictReader` → `total rows 204`; exact `S3007` → **0**; `S30007` = "Form DEF
  14A 1998 proxy statement" (ST3_A's S3007), `S30037` = "Schedule 13G for Jeffrey P. Bezos" (ST3_B's),
  `S30058`/`S30059` = the map's flanking ST3_C rows — the three candidate carriers an positional guess
  would have picked, each a *different document* from the one the held row names, which is why the map's
  "resolve by content, never by position" was followed literally.
- Accession search across `sources/` + `sources.csv`: file on disk =
  `8-K_event-1998-10-28_acc-0000891020-98-001498_filed-1998-10-28.txt`; register rows mentioning that
  accession or date = **only `S30051`** (two-event row, ST3_B).
- Gate logic read, not assumed: `gate_keys` in `tools/gates.py` fails a `S\d{3,6}` token only when it is
  absent from `sources.csv` **and** not in a protected discussion window (`collision|re-?key|retired|
  supersed|provisional|UNRESOLVED|range|was|formerly|backtick`). Every `S3007`-class token left in the
  volume is there because it is genuinely being discussed as a retired or unwritten key — the protection is
  a consequence of the corrected prose, not keyword sprinkling; the record itself names each reason.

## Gate before and after

STATUS: WRITTEN 2026-09-25

Command, identical before and after:
`python tools/gates.py --company-dir founders_playbook/01_companies/company_001_amazon --checks keys,anchors,budget`

**BEFORE — `Findings: 1 | Passes: 33`**

| gate | subject | finding |
|---|---|---|
| keys | stage_3_claim_records_part_1b.md | unresolvable source tokens: S3007 |

```
- coverage 9 registers, 17 stage volumes, 101 source documents
- keys  stage_3_claim_records_part_1b.md mentions 3 retired keys inside collision/re-key/range
        text -- protected history, not re-pointed: S3001, S3007, S3081
anchors  citation resolution  every register-cited anchor resolves (191 distinct ids)
anchors  parity              183 narrative anchors <-> 183 register anchors
budget   stage_3_claim_records_part_1b.md  40764 words (cap 60000)
```

**AFTER — `Findings: 0 | Passes: 34`** (no table row; the sole `keys` subject moved into the passing list)

```
keys  stage_3_claim_records_part_1b.md   5 source tokens all resolve
- keys stage_3_claim_records_part_1b.md mentions 6 retired keys inside collision/re-key/range
       text -- protected history, not re-pointed: S3001, S3006, S3007, S3008, S3021, S3081
- coverage 9 registers, 17 stage volumes, 101 source documents
anchors citation resolution 191 distinct ids; anchors parity 183 <-> 183 (unchanged)
budget stage_3_claim_records_part_1b.md 41043 words (cap 60000)
```

The company-level volume gate therefore goes from **1 residual finding to 0**, and the clearance is not the
result of a carrier being found for `S3007`: the token is still unresolved in the register and still says so
on the page. What changed is that the sentence which *falsely claimed it resolved* is gone, and the four new
protected tokens (`S3006`, `S3008`, `S3021`, plus `S3007` itself) are the map keys the correction names as
evidence for why no pairing exists. Anchors parity and every budget line are unchanged, so nothing was moved
between volumes to achieve the pass. Register-layer and `corrections` gates were not re-run here — the
previous pass closed them at 0 findings and I touched no CSV.

## Handed off

STATUS: WRITTEN 2026-09-25

Four items need an edit outside my four files. **Stopped at the boundary, not worked around it.**

1. **`S3007` — FOR THE RE-KEY-MAP / REGISTER OWNER (the only real fix).** Either (a) add the missing
   ST3_C pairing row to `03_quality_control/stage3_sourceid_rekey_map.md` and append the refused
   19-field row to `sources.csv` under a free canonical id — the content is fully recoverable from
   `stage3_register_merge_held_rows.md` row 8, including the reason for the refusal (the `url` cell holds a
   comma, so the row is 19 fields against the canonical 18, §13 quoting rules), or (b) record the row as
   permanently dropped and point ST3C-50..ST3C-57's claims at `S30051` **with its two-event scope stated**.
   I did neither: minting an id or editing a register is not my ownership, and option (b) is precisely the
   carrier-invention the marker exists to prevent. The `UNRESOLVED(S3007: …)` text in record **S52** is
   written so it can be deleted wholesale once the pairing lands.
2. **`_parts/s2_p4.md`, `_parts/s3_p4.md` — FOR the `_parts/` owner.** 11 occurrences of the withdrawn value
   remain, 4 of them live (that file's own `§P188`, `§P.2 t1` and its `stage3` gross-margin register row,
   plus the un-bannerset stage-2 row at `§…DERIVED S2P4 P.2 s4`). These are pre-merge intermediates, outside
   the 17 gated stage volumes, so no gate sees them — which is exactly how a stale quotient survives. Fix
   only if either file is ever re-merged; a re-merge that reads `s3_p4.md` would re-import
   `0.194995` into `stage_3_part_3.md` and into `quantitative.csv`.
3. **`CORRECTIONS.md` and `quantitative.csv` — no action requested, classified only.** The `CORRECTIONS.md`
   hit at the Stage-2 residue list and both `quantitative.csv` hits (the stage-2 and stage-3 gross-margin
   rows) are correct retraction markers printing withdrawn-plus-correct. Noted here because the sweep's
   keyword heuristic flags `CORRECTIONS.md` as "live" on window size alone; a later automated sweep will
   re-flag it unless it reads the paired value.
4. **Carried from `amazon_s3_retraction_register_repairs.md` §Left for adjudication, untouched by me:** the
   D-1 "$349 million" S-3 composition question, COR-26's `$178.4m` / 264,000-vs-190,700 residue, and the
   Ex-4.1 indenture `data_gaps.csv` row. All three are register work, all three stay with the certifier.

**Coverage note (what I did not examine):** I swept for `0.194995` and its percent rendering only — other
withdrawn values in the 26-`COR` set were not re-swept and are presumed handled by the register pass; I did
not re-audit the four already-repaired Stage-3 sites beyond verifying the correct value is present; and
`stage_3_claim_records.md` / `stage_3_claim_records_part_2.md` were swept, not read end-to-end (both returned
zero hits, and part_2's `keys` line was already clean before and after).

**UNTRIED:** whether the 8-K event 1998-10-28 bytes on disk actually carry Q3-1998 results (I confirmed the
file exists and is registered, not its contents — reading them is the register owner's step for option (a));
whether any *other* company's Stage-3 claim records carry the same withdrawn quotient; and whether the
`⟪SUPERSEDED …⟫` banner convention used in `_parts/s2_p4.md` is what the `_parts/` owner intends to keep.

**Files changed by this pass: exactly one** —
`founders_playbook/01_companies/company_001_amazon/stage_3_claim_records_part_1b.md` (records **P95**,
**P179**, **S52**; 40,764 → 41,043 words), plus this sheet. `stage_3_claim_records.md` and
`stage_3_claim_records_part_2.md` needed no edit and were not written.

