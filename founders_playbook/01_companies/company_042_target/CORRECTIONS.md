# CORRECTIONS.md — company_042_target, Stage 1

Provenance correction register for this company. Standing rule (method §14 rule 8 and rule 10): a withdrawal
**supersedes** the text it withdraws, it never erases it. The withdrawn wording stays visible where it was
written — in `_parts/`, in the part's own register-block preamble, in a register cell — and the correction
names the carrier that replaces it. Reverting one of these is a defect.

Opened 2026-09-26 by the Stage-1 merge pass (`03_quality_control/target_s1_merge.md`). The `corrections` gate
checks propagation mechanically: every id below must reach **both** the register layer and a stage volume. An
entry that reaches the prose but no register is the failure this file exists to stop.

| Id | Withdrawn text | Where it lived (carrier of the stale claim) | Replaced by | Reaches |
|---|---|---|---|---|
| **COR-01** | "fiscal year equals calendar year in these reports" (inherited premise; restated in `_parts/s1_p1.md` §Boundary 4 as P1K10 and refuted in `_parts/s1_p2.md` as K8) | `_parts/s1_p1.md` §Boundary 4 and its quantitative block's bare-year date cells; `research/B1_dayton_print_records.md` Q1–Q26 store-and-sales series, whose **Q20** dates 186,166,671 as "1965" | a report labelled **N** is a 52/53-week retail year ending in late January / early February of **N+1**: the FY1965 layer's period end is **1966-01-29**, its comparative column ends **1965-01-30**, FY1966 ends 1967-01-28, FY1967 ends 1968-02-03 pattern confirmed by the printed keys (year ended February 1 1969 = fiscal 1968) | `conflicts.csv` **U.011**; 29 `quantitative.csv` rows; 2 `timeline.csv` rows; `stage_1.md` merge note |
| **COR-02** | the documented floor for naming the company in the retail sense is **1972-03-22** | the Stage-1 dispatch brief, repeated in `MASTER_RESEARCH_LOG.md` line 1291 as a finding | **three defensible floors, none of them 1972-03-22**: the FY1965 document floor, the 1962 event floor carried only by retrospective print, the 1994-02-10 registrant floor. The string and its two alternate forms occur in **zero** bytes under `company_042_target/` | `conflicts.csv` **K16**; `stage_1.md` merge note. **Outbound:** `MASTER_RESEARCH_LOG.md` line 1291 still states it — that file is not owned by this pass, see below |
| **COR-03** | the trap: `_parts/s1_p1.md` §G's site-tenure UNKNOWN claim, and the adjacency in the FY1965 layer where **Brookdale** (L122-123) sits one line above the Target entry sentence (L124) so that a careless citation quotes a Dayton Development centre as a Target opening | the §G retraction was carried in volume 1's prose and in the cost/vendor gap row | Brookdale is the development arm's 1962 centre; the 1962 Target entry is **Roseville** and its three chronology companions; site **tenure is partially established** — buildings mortgaged, land sold and leased back — so "UNKNOWN" is withdrawn, and what remains unknown is the sale price, the cost, and the vendors | `conflicts.csv` **K17** (mis-citation), `timeline.csv` Brookdale row, `data_gaps.csv` cost/vendor row (shared with COR-04), `stage_1.md` merge note |
| **COR-04** | "site tenure of the founding stores is UNKNOWN" (volume 1 §G, retracted in the same pass that read the FY1966 notes) | `_parts/s1_p1.md` §G and the data-gap row that carried it | the FY1966 notes print a **land sale-and-leaseback at 225,000 annual rentals** with the buildings mortgaged: tenure is partially established; the unknowns are the price, the per-store cost and the vendor terms | `quantitative.csv` `annual_rentals_under_the_land_sale_and_leaseback`; `data_gaps.csv` (the cost/land-price/vendor gap); `stage_1.md` merge note |
| **COR-05** | the FY1970 layer byte count **52,736** printed in the probe table | `research/B1_dayton_print_records.md` probe table (volume 1's N6) | disk and sidecar both print **53,023 B**; the filed artifact wins; the probe figure is withdrawn and the correction is logged rather than quietly retyped | `sources.csv` **S4206**; `data_gaps.csv` **U.023**; `stage_1.md` merge note |
| **COR-06** | nothing was withdrawn — eight emitted rows arrived with **column drift** (unquoted thousands/place commas inside one cell): `s1_p2.md` sources l1179, l1185, l1186; quantitative l1211; timeline l1226, l1229, l1231, l1233 | the emitted blocks in `_parts/s1_p2.md` (which claimed, for volume 1 only, "0 misaligned rows") | re-joined at the printed split point so the cell holds the intended text; **no value altered, no cell re-worded**; repaired cells are tagged in place | `sources.csv` S4202/S4209/S4221; `timeline.csv` 4 rows; `quantitative.csv` 1 row; `stage_1.md` merge note |

---

## COR-01 — the year basis: no report labelled N is a calendar year

Volume 1 inherited from the records dossier the premise that these reports equate fiscal and calendar years,
and used it to date money. Volume 2 read the statement headers. The layer labelled **1965** prints "the fiscal
year ended January 29, 1966" and calls the same column 1966 in its notes; FY1966 ends 1967-01-28; the FY1969
layer prints the key itself ("year ended February 1, 1969" for fiscal 1968). Five printed year-ends across four
layers, three of them verified-TLS.

Consequences applied at merge: **B1's Q20 is re-based, not re-typed** — the 186,166,671 row now carries
`date = 1966-01-29` with the superseded "1965" label kept inside the same cell, and the 162,773,739 comparative
carries `1965-01-30`. Every quantitative row whose `date` is a bare year was re-tagged
`PERIOD BASIS: CONTEMPORANEOUS|RESTATED` against the printing layer, and the two conflict emissions (P1K10 and
K8) were folded into one row, **U.011**. The FY1974→FY1975 leg migrates to a 31-December year-end and any
series crossing it changes denominator; that migration is a `timeline.csv` row, not a footnote.

Residual: whether the B1 store-count series silently compared a January count to a December market figure is
resolved per row in the `PERIOD BASIS` tags, not globally, and the FY1968-onward pattern was not re-tested by
this pass.

## COR-02 — a received date that exists nowhere

§14 rule 8 applied to a date: the dispatch premise "1972-03-22" was grepped across the entire company
directory in three written forms and returned zero hits — no filing, no layer, no index, no negative artifact.
It is therefore **not evidence** and was not written as a value. It survives as conflict **K16** with its
provenance gap recorded ("where the date came from is UNKNOWN; if a carrier exists it is outside this company
directory and must be fetched before use").

**Outbound correction, not owned by this pass:** `MASTER_RESEARCH_LOG.md` line 1291 still states the withdrawn
date as a finding. This file is the instruction layer of a shared log and rule 10 says that is the
highest-severity home for a stale claim; the merge records it here and hands it to the log's owner rather than
editing a file outside its brief.

## COR-03 — the two 1962 openings that print one line apart

The FY1965 layer prints "Brookdale shopping center … 1962" at L122-123 and "early in 1962 … Roseville" at
L397-398 — two different subsidiaries, near-identical directional geography, one document. Both are true;
neither corroborates the other. Any later quotation that renders L122-123 as a Target opening is a mis-citation,
so the trap is registered as a conflict (K17) and as a timeline row whose note forbids the reading, rather than
by deleting the Brookdale fact.

## COR-04 — §G's site-tenure retraction reached the registers

Volume 1 retracted its own §G claim in the pass that read the notes pages. A retraction that stays in prose
leaves the register teaching the old answer, so the withdrawal is written into the gap row that carried it and
the 225,000-rental row that replaced it.

## COR-05 and COR-06 — transcription defects

A byte count that disagrees with the artifact is corrected by reading the artifact (53,023 B), and the eight
drifted rows were re-joined rather than dropped or re-worded. Both are recorded because a silent fix is
indistinguishable from a fabricated value.
