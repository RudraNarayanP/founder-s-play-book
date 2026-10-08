# _MANIFEST — company_035_att (Stage 1)

**Counts regenerated 2026-10-07** by the Stage-1 merge pass (`merge-att`) with `wc -w` / `wc -c` and
`os.path.getsize` on the bytes **after the last write of this operation** (word = whitespace-delimited token,
byte = file size). Every figure below is a measurement, not a recollection: re-measure before publishing any of
them again. The merge applied **136 register rows against 136 requested**; the account, the census readings
before and after, the id allocation and the `validation`/`failures` adjudication live in
`03_quality_control/att_s1_merge.md`, and the same record is printed at the head of `stage_1.md`.

**Which ceiling governs which file.** §9.1's hard upload constraint — **500,000 words / 200 MB per file,
whichever binds first** — governs every file including the restored evidence under `sources/`. §9.2's caps govern a
stage volume and its companion deliverables: **soft target ≤ 40,000 words**, amber 40,000–60,000, **hard cap
60,000**. The **tier cap is a density target, not a file limit** (RD-122). `stage_1.md` measures **31,315 words**:
**52% of the 60,000 hard cap**, **78% of the 40,000-word soft target**, and **142% of the 22,000-word T2 planning
figure** — that last number is the overage, and `tools/gates.py` files it as `advisory` ("NOT a split mandate and
NOT a defect"), which is the status this manifest records for it. **No prose was edited, trimmed or split to satisfy
the tool** (§9.6: "Cutting evidence to fit a file limit is forbidden"), and no file in this directory is at or over
the hard cap, so **no splitting is required and none was done**.

**Tier as issued, as inherited, and as graded — all three kept.** `research/A_chronology_feasibility.md`
(agent `probe-att`) issues **Stage 1 = T2 core, PROVISIONAL** (22k words/stage, 6–9 runs); §Header 2 of the volume
inherits it and keeps the probe's two open re-grades ((c) folded into (d) would make T3; admitting the 1994 recital
as an origin answer would make T1). This pass **did not re-tier**. The budget check was run as
`python tools/gates.py --tier core`, and the reason is stated rather than hidden: `--tier auto` resolves a tier from
a **verdict-bearing line** in `research/*.md`, and this probe states its per-stage tiers **as table rows**, so the
automatic reader had no verdict line to read — measured on this company it prints `tier: T2 … 13 mentions, 0 on a
verdict line`, landing on T2 only through its mention tie-break, the same path that printed **T3** for Cigna's probe.
The explicit CLI value pins the same 22,000-word target without leaning on a tie-break.

## Deliverables (read these)

| File | Words | Bytes | Contents | Status |
|---|---|---|---|---|
| `stage_1.md` | **31,315** | 199,903 | merge record (assembly, 136-row application account, `P1S01–P1S14` → **S4449–S4462** id map, `validation`/`failures` adjudication, four-person preservation, anchor parity, tier and five-family statements, not-applied list) + the author's body **unchanged and unre-numbered**: Header (§1 registrant problem, §2 stage/span/tier, §3 firewall + record-selection null, §4 corrections, §5 conventions), Stage Boundary (§1 1875 floor, §2 1915 carried as design, §3 1984 creates a new registrant, §4 what the boundary does NOT claim, §5 knowability), §A–§U with §U.1–§U.9, **56 claim records** (`BD01–BD04`, `A01`…`U01`) and the §S `FETCH REQUEST` R-1…R-5 + `UNTRIED` list, + the register-application record | **MERGED 2026-10-07**; one volume; over the T2 density target (advisory), inside every hard ceiling |
| `sources.csv` | 1,707 | 14,051 | **14 data rows × 18 cols**, keys **S4449–S4462**; P2's two in-window carriers (S4449, S4450), the hostile 1908 pamphlet (S4451), the 1885 recital (S4452, RESTATED), the P4 recital line (S4453–S4456), the both-registrants-in-one-header 425 (S4457), the firewall object (S4458), **two NOT-EVIDENCE index artefacts with their perimeters** (S4459 1,255 rows 1994-01-07→2007-01-18; S4460 7,922 rows 1994-02-14→2026-10-02), the probe pointer (S4461, tier 4) and the DTIC decoy shelf as a negative artefact (S4462); `independence_note` on every row | APPLIED 14/14 |
| `quantitative.csv` | 1,073 | 12,282 | **44 × 12** — the FY1913 printed set on both stated bases (SYSTEM and COMPANY), the §K.3 footed arithmetic (rows marked `DERIVED`), the non-footing annualised traffic rate as printed (`P14`, conflict U.5), the per-station earnings series 1895→1913, and **two `UNKNOWN` rows kept as rows** (headcount; 1885 capitalisation) | APPLIED 44/44 |
| `timeline.csv` | 1,290 | 10,613 | **28 × 11** — 1875 null row, 1876 chart baseline, 1877 apparatus epoch, the 1881–1913 long-lines sequence, the 1894 patent expiry, the 1913-12-19 undertaking, the 1915 design row (`CONTEMPORANEOUS as DESIGN; event UNKNOWN`), and **two `OUT OF WINDOW` P4 rows** (1983, 1984-01-01) held apart from P2's infancy | APPLIED 28/28 |
| `conflicts.csv` | 1,085 | 7,830 | **9 × 15**, keyed **U.1–U.9**, one row per declared §U anchor, 1:1 | APPLIED 9/9 |
| `decisions.csv` | 669 | 5,406 | **7 × 15** — the 1887 conference, the twisted-pair adoption with plant abandonment, the 1911–13 loaded-cable programme, the 1913-12-19 acceptance, the depreciation-reserve policy, the 1912–13 pension plan, the refusal to convert to automatic switching | APPLIED 7/7 (two `claim_ref` cells named as residue, see `CORRECTIONS.md` "Not corrected") |
| `validation.csv` | 428 | 3,555 | **7 × 11** — validating signals; block bound at merge (**COR-02**) | APPLIED 7/7 |
| `failures.csv` | 761 | 5,926 | **10 × 11** — incurred adverse signals, incl. the 1905 Chicago & Milwaukee receivership (P2's line, **not** P4's); block bound at merge (**COR-02**) | APPLIED 10/10 |
| `channels.csv` | 400 | 3,085 | **5 × 11** — exchange subscription through the associated companies, the toll/long-lines business, the 1913-12-19 interconnection schedule (the window's only priced channel), the rural/co-operative sub-licence route, Western Electric's external apparatus sales | APPLIED 5/5 |
| `data_gaps.csv` | 632 | 4,806 | **12 × 8** — 5 High / 5 Medium / 1 Low / 1 n/a (Stage-2 scope) + the two-person 2005 name-change row; every High row carries a follow-up task naming its route (R-1, R-2/R-3, R-5 or the CDX/periodical re-run) | APPLIED 12/12 |
| `stage_1_index.md` | 832 | 5,418 | volume index: section map, anchor → register homes, id map pointer, reading order | MERGED 2026-10-07 |
| `CORRECTIONS.md` | 1,508 | 10,333 | **COR-01** id supersession · **COR-02** validation/failures binding · **COR-03** the probe's superseded counts and shelf total · **COR-04** the 1885/CIK-5907 rule and the NOT-EVIDENCE framing · "Not corrected, and why" | LIVING — append, never rewrite history |

## Intermediate merge volumes (`_parts/`) — retained, read-only to every later pass

| File | Words | Bytes | Contents | Why retained |
|---|---|---|---|---|
| `s1_p1.md` | 36,595 | 251,090 | the whole emission: Header, Boundary, §A–§U, 56 claim records and the **nine fenced register blocks at l.908–l.1096** (136 rows, verbatim) | **the emission of record for the merge.** Not edited, not moved, not renumbered, and carries **no `SUPERSEDED` footer**, because the merge found nothing in it that required correction — the four corrections are the author's own (§Header 4) and the two new counts are recorded in COR-03. A repair pass reads this file to see what was emitted; it writes `stage_1.md` |
| `NOTES_att_p1.md` | 2,216 | 15,898 | the authoring pass log: what was read, the five `FETCH REQUEST` blocks' evidentiary framing, the five issued corrections (`ATT-S1-C1`…`C5`) and the two new counts, the register-emission tally, the pre-merge gate reading | the source of COR-03 and of the "rows withheld: none" statement the census confirmed |

## Specialist dossiers (`research/`) — the archival evidence layer

| File | Words | Bytes | Scope |
|---|---|---|---|
| `A_chronology_feasibility.md` | 8,259 | 56,383 | the probe dossier: tier verdict (T2 core PROVISIONAL), registrant map (P1–P4), five-family verdict, `## Untried`, the quarantined-index perimeter measurements — **the scope this stage inherits** |
| `A4_harvest_mine.md` | 709 | 4,437 | the mine-label report, superseded **for label counts only** at §Header 4 / §T (its `VARIANT_TERM_HIT` reading of P2's own annual report is a grep artefact) |

## Evidence shelves (`sources/`) — primaries, checked against §9.1 only

| Shelf | Documents | Bytes | Notes |
|---|---|---|---|
| `sec/` | **33** (28 `.txt` + 5 `.htm`) | **10,500,602 B** (documents; 10,524,362 B with the 33 `.meta.json` sidecars) | both registrants' stored filings, every one with a sidecar; Stage 1 cites seven of them (S4452–S4458); the other 26 are Stage-3 material and were not read by either pass |
| `periodicals/` | **6 layers** | **707,735 B** (the six `.txt` layers; + 2,685 B of sidecars = 710,420 B) | re-measured by the authoring pass; the probe's 660,753 B is superseded at COR-03, and the volume still prints the inherited figure where the author wrote it. Three layers are cited (S4449, S4450, S4451), three are DTIC decoys (S4462) |
| `corporate_print/` | **0 files** | 0 B | empty shelf while the harvest index labels three held items `corporate_print`; nothing was moved (§14 rule 4) |
| `_index/` | 15 artefacts | 7,759,648 B | CIK 732717 index + registrant record (S4460) and the **quarantined** CIK 5907 index (S4459). Registered as NOT EVIDENCE — perimeters of the archive's reach, not witnesses and not absences |

**Upload batch 1** = the readable stage volume. **Batch 2** = the nine registers. **Batch 3** = `_parts/`,
`research/` and `sources/`. Word totals are counts of tokens, not of evidence.
