# FORENSIC LONGITUDINAL DATASET — CIGNA, STAGE 1 (PROPOSED WINDOW 1979-01-01 → 1995-12-31)

## MERGE RECORD (assembly, application, id map, folds, anchor parity, carry-forward)

Merged 2026-10-06 by `merge-cigna` from the single part `_parts/s1_p1.md` (author `s1-cigna-p1`, 15,707 words
as emitted, 26 `STATUS: WRITTEN` markers, 0 PENDING). **Section letters are the author's and were not
renumbered**: Header, Stage boundary, §A–§U, the claim-record appendix and `## UNTRIED` appear below in the
order and with the labels the part gave them (method §9.3 — numbering continues, it is never re-based). Nothing
in the narrative was rewritten, trimmed, re-tiered or merged away. `_parts/s1_p1.md` stays **read-only** and is
the emission of record; the merge appended to it a `SUPERSEDED 2026-10-06` **footer** and edited nothing above
it — the footer supersedes the **placement and key-space** of the register emission (the 78 rows now live in
the CSVs; `CG01–CG16` are superseded there by S4407–S4422), not one word of the narrative, which required no
correction. The correction ledger for this operation is `CORRECTIONS.md`: three entries, of which COR-03
carries a withdrawal the probe had already made inside its own dossier up to the instruction layer.

**What was moved out of the prose.** The part's nine fenced `csv` register blocks (78 rows) are register data,
not narrative (method §13): they were **applied** to the nine CSVs at this directory root, and the body's
`## Register rows for merge` heading now points at that application instead of repeating the blocks. Their
verbatim text survives at `_parts/s1_p1.md` l.492–l.651. Claim records **are** narrative: all 25 of them
(A01…S01) are below, unchanged.

### Register application (requested ↔ applied, measured on the bytes written)

| register | rows requested | rows applied | cols | key / integrity check |
|---|---|---|---|---|
| `sources.csv` | 16 | **16** | 18 | keys S4407–S4422, 0 duplicates |
| `quantitative.csv` | 15 | **15** | 12 | 0 duplicate row texts |
| `timeline.csv` | 14 | **14** | 11 | 0 duplicate row texts |
| `data_gaps.csv` | 12 | **12** | 8 | 0 duplicate row texts |
| `conflicts.csv` | 6 | **6** | 15 | keys U.1–U.6, 0 duplicates |
| `failures.csv` | 6 | **6** | 11 | 0 duplicate row texts |
| `validation.csv` | 4 | **4** | 11 | 0 duplicate row texts |
| `decisions.csv` | 3 | **3** | 15 | 0 duplicate row texts |
| `channels.csv` | 2 | **2** | 11 | 0 duplicate row texts |
| **TOTAL** | **78** | **78** | — | **0 unapplied, 0 added by the merge** |

**Rows added after the merge, at the Stage-1 repair pass** (not merge application, so they are counted
separately and are attributed to their COR entries): `sources.csv` **+2** (S4529, S4530 — COR-08) and
`failures.csv` **+1** (the 1979 annuity revenue decline — COR-07). Post-repair register state: **79 rows**
across nine files — sources 18, quantitative 15, timeline 14, data_gaps 12, conflicts 6, failures 7, validation
4, decisions 3, channels 2. No existing row was folded or deleted.

Every header is **byte-identical** to the corresponding Amazon conformant register header (compared by string
equality against `company_001_amazon/<name>`), `stage` is the literal `stage1` on all 78 rows (never a bare
number), and the width and duplicate-key pass was run **across every block of this one operation together**,
not per block: **0** rows off-header-width, **0** empty cells, **0** exact duplicate rows across the nine
registers, **0** duplicate keys in the two keyed registers. Rows are written at the header's width with every
field that can contain a comma quoted, so no register can be shifted by one field.

### Provisional-to-global id map (the only place `CG01–CG16` bind; minted centrally)

Minted with `python tools/id_mint.py --count 16 --company company_014_cigna --claim --agent merge-cigna` →
**S4407 … S4422** (contiguous, 16 ids). `--audit` before the mint: 327 distinct issued ids in range
S0001–S4406, highest live block `company_013_costco` S4393..S4406, tool's own `next assignable: S4407`. The
block was allocated **above the highest live id**, so no gap is re-entered and no number another company holds
is reused; the audit's collision list — `S4222–S4229` cited by both `company_011_microsoft` and
`company_042_target` (task #31, and the reason Target's next mint is deliberately held) — sits below this
range and was not touched. Register rows carry the minted ids; the narrative below keeps the author's local
tags and is keyed by this table.

| local | minted | carrier |
|---|---|---|
| CG01 | **S4407** | Form S-4, Halfmoon Parent, Inc., acc. 0001140361-18-024107 — ONE lineage incl. 4 amendments + exhibits (**20 documents measured**, 5 accessions × 4) |
| CG02 | **S4408** | Form 8-K acc. 0001140361-18-045493, event 2018-12-20 — renaming, merger anatomy, EIN carried forward |
| CG03 | **S4409** | Indenture exhibits ex4-1 / ex4-2, acc. 0000950159-18-000404 — both ancestors named as Designated Subsidiaries |
| CG04 | **S4410** | INA Corporation Annual Report 1979 (`INAC2115_1979_djvu.txt`) — the 1792 narrative and the whole K/quantitative set |
| CG05 | **S4411** | Creative Bath Products v. Connecticut General Life Insurance Company (1989), micro_IA40385019_1642 |
| CG06 | **S4412** | Pierre v. Connecticut General Life Insurance (502 U.S. 973, 1991) Rule 29.1 statement, micro_IA40385013_0186 |
| CG07 | **S4413** | DeBlase v. CIGNA Individual Financial Services Co., micro_IA40386012_1635 — md5-identical on two shelves = ONE document |
| CG08 | **S4414** | CIA Africa Review chronology rdp88t00792r000300040001-2 (1988-11-18, "US firm Cigna") |
| CG09 | **S4415** | CIA staff-meeting minutes 9 Apr 1980, rdp84b00130… — DECOY row (mis-shelved as corporate print) |
| CG10 | **S4416** | Assessing It Performance (Wilsen 1988) — naming-only row (research-sponsor acknowledgment list) |
| CG11 | **S4417** | EDGAR submissions index for CIK 0001739940 (1,018 rows) + `_INDEX.md` — perimeter measurement carrier |
| CG12 | **S4418** | ERIC ED357426 / micro_IA41153629_0618 — DECOY (Connecticut General Assembly place-name trap) |
| CG13 | **S4419** | ERIC ED460893 Connecticut General Assembly Teacher's Manual — DECOY; blocks reading the lone `1850` as an ancestor date |
| CG14 | **S4420** | Harvest-index pointers to the pre-1975 Connecticut General SCOTUS layers (Rozelle/Fitzgerald/Blanchette) — BYTES UNHELD |
| CG15 | **S4421** | `research/A4_harvest_mine.md` — census carrier only (96 / 12 / 81 as re-read by the author; **96 − 12 = 84 ≠ 81**, the carrier's own non-closure, named at COR-10) |
| CG16 | **S4422** | `research/A_chronology_feasibility.md` — the probe dossier that issued this stage's window and tier |
| CG17 | **S4529** | CIA reading-room document rdp90g00152r001102380002-3 (1987, 36,048 B) — held, in-window, **NAMING-ONLY**: CIGNA address block + Consumer Marketing channel sentence |
| CG18 | **S4530** | CIA reading-room document rdp91-00929r000200960032-0 (24,680 B) — held, **DECOY**: the `CIGNA` hit is an OCR'd journal-article **author surname**, not a company |

**Folds applied: none.** No row was folded into another, no register was deduplicated on similarity, and no
`CG`-tagged lineage was minted twice — per the author's merge instruction (2), the four S-4 amendments and the
exhibits of acc. 0001140361-18-024107 received **no** additional `sources.csv` rows (CG01 is one lineage of 20
documents measured this pass — the merge had carried "23 files" from the probe, which reproduced from no
counting rule on this shelf: see COR-10i), CG03's two exhibits are one accession, and CG07's two-shelf md5 pair
is one document. **16 rows → 16 contiguous ids at merge; +2 rows (CG17/CG18 → S4529/S4530) at the repair pass,
minted separately, 18 in total.**

**Anchor parity, proven by re-running the census rather than asserted here.** The part declares
`<!-- ANCHORS: U.1-U.6 -->` and writes §U.1–§U.6 below. `python tools/merge_census.py --company-dir
founders_playbook/01_companies/company_014_cigna --verbose`, re-run **after the final write of this
operation**, reads `conflicts.csv | requested 6 | present 6 | missing 0`: all six declared anchors U.1–U.6
exist as register keys, 1:1 with the six `U.nn` sections in §U, with no seventh row and no unanchored row.
The same run's `sources.csv` line still lists the 16 `CG01–CG16` tags as "missing keyed rows" — the expected
residue of a central mint (the minted ids S4407–S4422 are present; the local tags exist only in the read-only
part and in the map above). The `validation.csv`/`failures.csv` pair remains `AMBIGUOUS` to the census because
the two registers share an 11-column schema; it was adjudicated by reading the rows, and the full reasoning is
in `03_quality_control/cigna_s1_merge.md`.

**Two tier frames, both carried, neither averaged.** Stage 1 is **T2 core, PROVISIONAL** on the lineage frame
the probe issued (`research/A_chronology_feasibility.md` §7 — two families return in-window Tier-1 text: (c)
three SCOTUS-era records 1989/1991/1994-95 and (d) the INA 1979 annual report), and **T3 register** on the
strict-registrant reading of the same window (§7 row 2 — zero families name CIK 0001739940 before 2018). This
volume keeps both as **states**, attributed: the Stage-boundary table's second row, §A, §B.2 and §R carry the
registrant line, §U.4 carries the machine-versus-dossier tier reading, and no figure or verdict anywhere below
averages the two frames into a middle tier. The divergence — in-window documents, none in-window *about the
registrant* — is the finding, not a gap to be papered over.

**Carry-forward.** `## UNTRIED` (9 items) and the FETCH REQUEST routes FR-1…FR-8 are carried below verbatim
from the part. Register homes: `data_gaps.csv` follow-up tasks carry **FR-1, FR-2, FR-3, FR-4, FR-5, FR-6,
FR-7** across its 12 rows; **FR-8** (pre-1979 outside witnesses to the 1792 claim) has **no dedicated
`data_gaps.csv` row**, because the author emitted none — its register home is the `residual_uncertainty` cell
of `conflicts.csv` U.2 together with UNTRIED item 8 below, and it is named here rather than dropped silently.
Family states stay distinct in every file of this operation: **TRIED–ANSWERED**, **TRIED–UNANSWERED** (the tool
or network refused; remedy named) and **UNTRIED** (never attempted, 0 calls). The five-family table is
reproduced in `_MANIFEST.md`.

**Counts.** Words and bytes of this volume and rows per register are published live in `_MANIFEST.md`
(method §9.6), re-measured with `wc` after the last write of this operation.
`tools/gates.py --tier auto` reads the tier from the dossier; the T2 22,000-word figure is a dispatch budget,
and an overage against it is advisory — no evidence was deleted to meet a number (method §9.6).

### Corrections issued at merge — `CORRECTIONS.md` COR-01…COR-03 (propagation, not rewriting)

| id | what it corrects | register cell(s) carrying it | this volume |
|---|---|---|---|
| **COR-01** | `CG01–CG16` are dossier-local keys and are superseded in the live registers by the minted ids **S4407–S4422**; no register row may keep a `CG` tag (author merge instruction (4)) | `sources.csv` S4407 `notes` | the id map above; §B, §K, §T, §U and the claim records keep the local tags as reading keys and are bound by that table |
| **COR-02** | the 4-row and 6-row emissions are bound to `validation.csv` and `failures.csv` on the row content — the two registers share a header, so the census cannot bind them and must not be read as leaving them unassigned | `validation.csv` first row `notes`; `failures.csv` first row `notes` | the merge record's adjudication paragraph; §L and §M |
| **COR-03** | the probe's 17:20 header claim — both ancestor dates occurring "0 times in every held byte", Stage 1 = **T3 register** — is withdrawn at the instruction layer; `1792` occurs **2** (both in `INAC2115_1979_djvu.txt` l.5, l.371) while `1872` stays **0** and the second ancestor stays **UNTRIED** | `conflicts.csv` U.2 `residual_uncertainty`; the census row of `quantitative.csv` | §U.2, §U.4 and the stage-boundary table |

### Corrections issued at the Stage-1 repair pass — COR-04…COR-12 (audit 1, `cigna_s1_audit1.md`)

Appended 2026-10-06 by `repair-cigna` (not the author, not the merger, not the certifier — §15.6). Every entry
was re-measured on the bytes before it was written; withdrawn text is quoted and refuted, never deleted.

| id | what it corrects | register cell(s) carrying it | this volume |
|---|---|---|---|
| **COR-04** | **BLOCKER B-1.** The null "No held byte prints this registrant's own date of incorporation" is **false**: held `s4.htm` **l.48371** prints `(Originally incorporated on March 6, 2018 under the name Halfmoon Parent, Inc.)` and **l.5011** prints `New Cigna was incorporated on March 6, 2018` (New Cigna = Halfmoon Parent, Inc., l.279/l.370). Line 3 re-dated **2018-03-06**, one lineage, FR-2 narrowed not closed | `timeline.csv` r13 (UNKNOWN→2018-03-06, FACT, S4407); `data_gaps.csv` r1; `conflicts.csv` U.1 | Header, the three-lines paragraph, §boundary row 2, §A.3, §A unknown-list, §B.2, §N, §Q, §R, §U.1, claim record A02 |
| **COR-05** | §A's PPO/managed-care null: `managed care` occurs **5× in held bytes** (S-4 l.26112/29379/33424/47186 + the four amendments, + 1 line each in acc. 0000950159-19-000007), all out-of-window — the true statement is **in-window-absent**; the `PPO` half (word-bound 0 corpus-wide) stays an archive null | `data_gaps.csv` r5; `sources.csv` S4407 `notes` | §A l.170, §E adjacency paragraph, claim records E01/E03 |
| **COR-06** | the INA Healthplan quotation was labelled truncated at the shelf edge with the completion UNKNOWN; `INAC2115_1979_djvu.txt` **l.2012-2019** prints the whole sentence — a **pre-determined monthly fee** design and an **employer subscriber channel** — so §E.1's "no plan design" is withdrawn and re-scoped | `timeline.csv` r9; `data_gaps.csv` r2 | §D row 2, §D.2, §E INA health row, §E.1 |
| **COR-07** | §D's "no failure disclosure in the held report" is false of the report: **l.1754-1760** prints annuity **revenues −5% to $195.8M** with a stated cause (table cell l.1645); scoped to the prepaid unit and added as an adverse row | `failures.csv` **r7** (new row) | §D row 4, §M (new row), §K.2 (new line) |
| **COR-08** | two **held** in-window CIGNA-naming CIA bytes mined by A4 were unregistered: rdp90g (l.1431 address block, l.1436 Consumer Marketing sentence) and rdp91 (l.1071, an OCR **author-surname decoy**, not a company naming) — minted **S4529/S4530** | `sources.csv` S4529, S4530; `data_gaps.csv` r6 | id map CG17/CG18, §T (two rows + ledger), §I, §B.1 |
| **COR-09** | four quoted spans are not verbatim in the carriers cited — a paraphrase-in-quotes (§G HMO), a condensation (§U.5 CLAIM A), an undisclosed **composite** (`sources.csv` S4417) and a silent **OCR repair** (§B.1 `at a23%`). Fixed by **marking**; no quotation was rewritten to force a match. Plus §F's "`membership` absent" → no membership *count* (token prints once, l.2618) | `sources.csv` S4417 `relevant_passage`/`notes`, S4421 `notes`; `data_gaps.csv` r2 | §G l.288, §U.5, §B.1, §H, §F, claim records N01/E03 |
| **COR-10** | two derived counts do not reproduce: CG01/S4407 "23 files" measures **20** (5 accessions × 4; 30 filing documents and 35 non-meta files in `sources/sec/`), and A4's own **96 − 12 = 84 ≠ 81** (79 − 12 = 67 ≠ 65) — the carriers are kept as printed and the **non-closure named** | `sources.csv` S4407/S4421 `notes`; `data_gaps.csv` r5, r10; `quantitative.csv` census row | id map, folds paragraph, §J, §S G5, §U.5, UNTRIED-4, claim record P01, the table above |
| **COR-11** | the coda duty was complete in §L.1 only: §H.1 had no confidence word, §D.2 named neither an alternative explanation nor a confidence | `decisions.csv` r1 `notes`; `quantitative.csv` ESTIMATE row `notes` | §H.1, §D.2 |
| **COR-12** | a published live count was stale — `_MANIFEST.md` l.55 put `_parts/NOTES_cigna_p1.md` at 1,003 words, measured **1,111** (bytes 7,830 unchanged); and every count this pass moved (sources 16→18, failures 6→7, registers 78→79) is re-measured with `wc` and re-published, not recollected | `sources.csv` S4529/S4530 `notes` (the mint that moved the counts) | `_MANIFEST.md`, `stage_1_index.md`, the register-application table above |

**No COR entry re-tiers, re-dates or re-values a claim it was not measured against.** COR-04 re-dates one line
because a held byte prints the date; nothing else moved. **No row was folded at merge: 78 emitted, 78 applied.**
The annotations above are appended to the end of existing cells and change no value except where a corrected
value is itself the correction (COR-04 `timeline.csv` r13, COR-07's added row, COR-08's added rows). FR-8 has no
`data_gaps.csv` row (the author emitted none) and its home is UNTRIED item 8 plus the `conflicts.csv` U.2
residual; `research/_EVIDENCE_CACHE.md` is still absent and its gap row stays open — both are named in
`CORRECTIONS.md` §"Not corrected, and why" rather than dropped.

---

# FORENSIC LONGITUDINAL DATASET — CIGNA, STAGE 1 (PROPOSED WINDOW 1979-01-01 → 1995-12-31)

**Company:** Cigna Group — registrant **CIK 0001739940** (`company_014_cigna`). The held bytes make this registrant **Halfmoon Parent, Inc.**, the Delaware shell that was renamed "Cigna Corporation" on 2018-12-20 at the Express Scripts merger closing (`sources/sec/0001140361-18-024107_s002268x1_s4.htm` l.52; `sources/sec/0001140361-18-045493_form8k.htm` l.77-78, l.163-166). ~~**No held byte prints this registrant's own date of incorporation.**~~ **WITHDRAWN at repair, COR-04:** a held byte does print it. `s4.htm` **l.48371** — the caption of Annex E, *Form of Amended and Restated Certificate of Incorporation of Cigna Corporation* — prints `(Originally incorporated on March 6, 2018 under the name Halfmoon Parent, Inc.)`, and **l.5011** prints `New Cigna was incorporated on March 6, 2018, solely for the purpose of effecting the mergers and, immediately after the mergers, New Cigna will be renamed "Cigna Corporation"` (the name chain is the same document, l.279: "Halfmoon Parent, Inc., which we refer to as New Cigna"). **This registrant's own date of incorporation is 2018-03-06, organised in Delaware as Halfmoon Parent, Inc. — FACT, one lineage (S4407), 12 literal occurrences of the date inside that lineage's files being copies of one instrument and not 12 witnesses.** The merger sub-entities printed at l.5033 and l.5037 were incorporated the same day and are **different legal persons**; nothing about this date is inferred from them. "Incorporated in Delaware in 1981" remains a recital about *another* legal person — Cigna Corporation, which the same 8-K (l.164-165) says became a *subsidiary of* the registrant.
**File:** Stage 1, part 1 of 1 — Header, Stage boundary, sections **A–U**, register append blocks, claim-record appendix. Tier **T2 core, PROVISIONAL** as issued by `research/A_chronology_feasibility.md` §7; the strict-registrant reading of the same window is **T3 register** (§7 row 2) and this dossier honors both.
**Author:** `s1-cigna-p1`, dispatch 2026-10-06, 0 web calls; every fact below traces to bytes under `sources/` or to the probe's measured census (which this pass re-verified where load-bearing).
**The three lines, kept apart everywhere in this file:** **Line 1** — the operating ancestors: INA Corporation / Insurance Company of North America (Philadelphia) and Connecticut General Life Insurance Company / Connecticut General (Hartford), and the CIGNA-named parentage that held bytes print from 1989 onward. **Line 2** — the asserted 1982 CIGNA combination: a hypothesis inherited from the dispatch brief, printed by **no held byte** (probe §4: 0 lines anywhere pair `1982` with merg/comb/union/formed), reachable only via FETCH REQUEST FR-1. **Line 3** — the registrant: the 2017/2018 Delaware continuation, born **2018-03-06** as Halfmoon Parent, Inc. (its measured EDGAR life begins later, 2018-05-16, and that gap is a filing floor, not a birth). ~~whose birth date is **not printed in the corpus**~~ — withdrawn at COR-04; `s4.htm` l.48371 and l.5011 print it.
**Register labels:** `CG01`–`CG16` are dossier-local source tags; the merge mints global ids via `tools/id_mint.py` (method §13). Claim ids `A01…U01` are dossier-local.
**Hindsight firewall:** Nothing here treats the later CIGNA/Express Scripts scale, the 2018 merger outcome, or the known future of either ancestor as evidence that any 1979–1995 decision was rational, obvious, or inevitable. The 1979 INA self-report is read as a company writing about itself **before** any of those outcomes; its growth claims are self-measured and capped accordingly. Anti-hagiography test applied: this file would read identically if either ancestor had failed within five years — it does not, on any held byte, call either survivor inevitable.
**Record-selection null (method §2):** What survives for 1979–1995 is (i) one digitised INA annual report, (ii) three US Supreme Court microfiche layers whose subject is litigation, and (iii) a 2018 SEC family about a different legal person. The internal deliberations of the 1982 combination, rejected options, pricing/underwriting failures nobody printed, and any independent count behind INA's self-report are **unrecoverable because the archive that was kept is the winners' one** — and even that kept nothing of the registrant's own pre-2018 life, because it had none.
**Confidence scale** (method §3): **High** — 2+ independent sources or a primary document. **Medium** — one reliable source, or approximate date corroborated later. **Low** — conflicting, vague, or retrospective-only. **UNKNOWN** — not established. Repeated copies of one origin story are **one** source; the S-4 + its four amendments + exhibits are ONE lineage (probe §2), and a scanner shelf is a carrier, not a witness.

---

## STAGE BOUNDARY JUSTIFICATION

STATUS: WRITTEN

| Stage | Window (all PROPOSED) | Why this boundary | Confidence |
|---|---|---|---|
| 1 | **1979-01-01 → 1995-12-31** | Inherited from the fleet's `harvest_mine.WINDOWS` (probe §1), kept deliberately WIDE because the founding date is itself unestablished — narrowing it would silently discard the bytes that could establish it. It brackets the decade before the asserted 1982 CIGNA name through the mid-1990s. Anchored at the front by the one in-window self-report (INA 1979 annual report) and at the back by the last in-window third-party record (DeBlase caption, receipt-stamped "APR 19 1995", probe §3.4). | The frame is a measurement setting, not evidence; High that it is the fleet's frame, Low as a claim about natural breaks |
| 1 — strict-registrant reading | start **2018-03-06** (Halfmoon Parent, Inc.'s incorporation date, printed by the registrant's own document family at `s4.htm` l.48371 and l.5011 — S4407, one lineage). ~~start **UNKNOWN** — no held byte gives Halfmoon Parent, Inc.'s incorporation date~~ is **withdrawn, COR-04**; the rest stands: measured EDGAR floor 2018-05-16 is a filing floor, not a birth, and the byte-printed date precedes it by 71 days | Under this reading Stage 1 of CIK 0001739940 begins as a 2017/2018 Delaware shell and the 1979–1995 window is a *predecessor window on the registrant's own paper* (RD-134's Ford case with polarity inverted). **Re-dating moved the registrant's front edge 22+ years further from the window than the 2018-05-16 floor already was, so this reading is strengthened, not weakened: the shell was already incorporated before its first filing and still nothing of it reaches 1995.** Both readings are carried; neither is allowed to answer for the other. | High (that the byte prints the date) / Medium (as the Delaware effective date — the print is inside a *form* of charter and a merger-description paragraph; the as-filed certificate is unheld, FR-2 narrowed) |
| 2 | 1996-01-01 → 2018-05-15 | Probe §7: T3, 0 of 30 stored documents inside it. Out of scope here. | — |
| 3 | 2018-05-16 → present | The registrant's measured EDGAR lifetime; out of scope for Stage 1 except as the Line-3 anchors. | — |

**What the boundary does NOT claim.** (i) Not that Cigna was "founded" in 1792, 1981, or 1982 — each of those dates belongs to a different legal person. As of COR-04 the registrant's own birth is no longer an unknown in this list: it is **2018-03-06** (`s4.htm` l.48371/l.5011), and it is the birth of the **shell**, not a founding of either operating line. (ii) Not that the 1979–1995 documents describe the registrant: probe §7 counted the families on the lineage frame while stating plainly that **not one held document names CIK 0001739940 inside 1979–1995**. (iii) Not that the window's end has an evidenced operational meaning for any line — 1995-12-31 is a frame edge, and the last in-window naming (DeBlase) was filed March–April 1995. (iv) Not that EDGAR's pre-2018 silence is the company's silence: the CIGNA Corporation that operated 1979–1995 filed under a CIK this repository has never indexed (FR-1); the walk of CIK 0001739940 is complete-enumeration silence (1,018 rows, 0 UNANSWERED slices, floor 2018-05-16 — probe §2, re-verified this pass: `sources/_index/submissions.csv` = 1,019 lines incl. header = 1,018 filings).

---

## A. EXECUTIVE STATE SUMMARY

STATUS: WRITTEN

At 1995-12-31, on the evidence actually held, **this registrant did not exist and no held document names it anywhere inside the window**. What existed, and what independent records witness, were three other legal structures:

1. **The CIGNA-named corporate family** — third-party judicial records establish its structure at three in-window moments: Connecticut General Life Insurance Company named as a litigant (1989); a 1991 Rule 29.1 statement printing the four-level chain CGLIC + LINA → Connecticut General Corporation → CIGNA Holdings, Inc. → **CIGNA Corporation**; and a 1994-95 caption naming CIGNA CORPORATION as a respondent with a merger sentence printing that CSI and CIFSCO had merged to form **CIGNA Financial Advisors, Inc.**, a subsidiary of Connecticut General Corporation whose ultimate corporate parent is CIGNA Corporation (CG05–CG07 in the sources block).
2. **The INA Corporation line** — its own 1979 annual report prints the group's state at that year-end: four business groups (property-casualty, life and group, health care, investment management), revenues **$4,551M**, net income **$262M**, total assets **$8,987M**, shareholders' equity **$1,526M**, 35,280 employees, and a self-dated origin: "Its history dates back to **1792**, with the formation of its principal subsidiary and the nation's first stock insurance company, Insurance Company of North America" (CG04). The 1792 sentence is a **retrospective self-narrative printed 187 years after the event, by a different legal person than the registrant, and attributed by its own grammar to the subsidiary, not to INA Corporation itself.** It occurs 2 times in the whole corpus and both occurrences are in this one document (re-measured this pass: `grep` over all shelf `.txt` = exactly l.5 and l.371 of `INAC2115_1979_djvu.txt`).
3. **The registrant's own line** — nothing inside the window, and now dated rather than undated: it was **incorporated 2018-03-06** in Delaware as Halfmoon Parent, Inc. (`s4.htm` l.48371, l.5011 — S4407, **one lineage**; COR-04 re-dates what this dossier previously carried as UNKNOWN). Its first EDGAR appearance is 2018-05-16 as Halfmoon Parent, Inc.; the S-4 it filed recites "Cigna was incorporated in Delaware in 1981" of the *counterparty*, which the 2018-12-20 8-K then makes a **subsidiary of** the renamed shell (CG01, CG02).

The **1982 combination** of Connecticut General and INA — the event that would fuse lines 1 and 2 — is printed by **zero held bytes** and pairs with no merger verb anywhere (probe §4, measured). It is carried here as hypothesis only. The second ancestor's claimed 1872/1850s origin is **UNTRIED, not null**: the plausible ancestor names (`Continental Life`, `Immigration Life`, `State Fidelity`, `Farmers and Merchants`) appear in no query this repository has ever run for this slug (`1872` = 0 occurrences in every held byte; probe §4, §11.4).

Unknown at the close of the window, **on in-window held bytes (1979–1995)**: membership or policy counts; earned-vs-written premium split for any *health* line; the PPO/managed-care vocabulary — with its two halves now measured separately, because lumping them produced a false archive null (COR-05): **`PPO` word-bounded occurs 0 times in every held byte in the corpus** (in-window and out; `grep -rnw "PPO" sources/` = 0), while **`managed care` is absent from every *in-window* byte but occurs 5 times in the held out-of-window S-4 lineage** (`s4.htm` l.26112, l.29379, l.33424, l.47186 ×2; and 1 line each in acc. 0000950159-19-000007), i.e. **in-window-absent, not archive-absent**; ~~the registrant's own incorporation date~~ — **no longer unknown, COR-04: 2018-03-06**, which is 22+ years outside this window and so does not re-open any in-window question; and whether the CIGNA family was by 1995 a health insurer in the modern sense at all — the held judicial records name life insurance, financial services and securities entities, and say nothing about membership.

---

## B. FOUNDER / COMPANY STATE

STATUS: WRITTEN

**There is no founder for this company at this stage, and saying so is the section.** The playbook's founder-state frame does not fit: neither ancestor was founder-era in 1979–1995 (both were already 87 and ~58 years old on their own accounts), and the registrant is a professionally-created merger shell with no natural person attached in any held byte. The standard frame is adapted, not deleted (method §7): the "company state" tables below carry (B.1) the ancestors' printed state, (B.2) the registrant's evidenced non-state.

### B.1 Ancestor state, as the held bytes print it

| Variable | Value | Source | Confidence |
|---|---|---|---|
| INA Corporation — self-description 1979 | "among the nation's oldest commercial organizations"; operates in "approximately 145 countries"; product families: property-casualty, life and group, health care, investment management; headquarters "in Philadelphia" (cover note) | CG04 l.4-10, l.15-17, T1 corporate self-report, CONTEMPORANEOUS (about 1979) | High that the report says this; the 145-countries figure is unaudited self-print |
| Insurance Company of North America ("the nation's first stock insurance company") | "founded in 1792" per the parent's 1979 report; **no second witness in the corpus** | CG04 l.5, l.371-372, T1, RESTATED (retrospective self-narrative, 187 years late) | Medium (one lineage, promotional voice; probe §11.1) |
| INA life insurance business | "began in 1957"; premium revenues grew "at a23% annual compound rate, compared with 9% growth for the overall field" over the past decade — **the byte prints `at a23%` with the space lost to OCR (l.382); the space is supplied here and the repair is disclosed, not silently applied (COR-09d)**; conducted by Life Insurance Company of North America, INA Life, Investors Life, Horace Mann | CG04 l.377-389, T1, CONTEMPORANEOUS self-report (the 1957 date is internally restated) | Medium (single lineage, self-measured) |
| INA health-care entry | "INA entered the health care field in 1969"; prepaid operations via **Hospital Affiliates, Inc.** (hospital management/ownership), **INA Healthplan, Inc.** (prepaid health care), International Rehabilitation Associates | CG04 l.391-412, T1, CONTEMPORANEOUS | Medium-High (one reliable self-report) |
| Connecticut General / LINA structure 1991 | parent of both CGLIC and LINA = Connecticut General Corporation; its parent = CIGNA Holdings, Inc.; its parent = **CIGNA Corporation**; CIGNA Companies address 1050 Connecticut Avenue N.W., Washington DC | CG06 l.6067-6068, l.6102-6121, T1 court record (third-party), CONTEMPORANEOUS | High (third-party filing under Supreme Court rule; independent of the company's own narrative) |
| CIGNA Financial Advisors formation | "Subsequent to the filing of this litigation, CSI and CIFSCO merged to form CIGNA Financial Advisors, Inc., a wholly-owned subsidiary of Connecticut General Corporation, whose ultimate corporate parent is CIGNA Corporation" | CG07 l.2484-2487, T1 court record, CONTEMPORANEOUS (bounded by the 1994-95 case record) | High that a court filing prints it; the merger's own date is bounded, not dated |
| Both ancestors alive and subsidiary 2018 | Indenture "Designated Subsidiary" = "each of Connecticut General Life Insurance Company and Life Insurance Company of North America, so long as it remains a Subsidiary, or any Subsidiary which is a **successor of** a Designated Subsidiary" | CG01 family, `ex4-1.htm` l.2584, `ex4-2.htm` l.72 (verified this pass), T1, CONTEMPORANEOUS (out of window; carried as terminal state of Line 1 inside the registrant's own paper) | High |
| The short name "INA Corporation" | occurs **0** times in every held SEC byte (probe §4); the ancestor names live on the print/court shelves | census, DERIVED | High (this pass reproduced the census method's two key zeros for 1792/`incorporated in Delaware in 1981`) |
| Held-but-bare-word `CIGNA` matches, now registered (COR-08) | Two in-window CIA reading-room bytes were mined by A4 (`BARE_WORD_MATCH`) and held on the shelf but carried **no** `sources.csv` row until this pass. **CG17/S4529** `rdp90g…` prints a real corporate block at l.1431 (`CIGNA / 1600 Arch Street - 3 Penn Center, Suite 110 / Philadelphia, PA 19103`) and l.1436 `The CIGNA Consumer Marketing Department offers insurance and non-insurance products to financial institutions through their customer base` — naming plus a channel sentence, **no event and no date moving**. **CG18/S4530** `rdp91-00929…` l.1071 `water-~nitric acid system. CIGNA, Rez DI CAVE, S.ej3` is an OCR'd **journal-article author surname** (Cigna/Di Cave/Giona/Mariani, translated from *Chimica Industriale*, Milan 1964): a **DECOY, not a company naming**, registered as a decoy so no later pass reads it as adjacency evidence | CG17, CG18 (both `sources.csv` rows added at repair) | High (the lines were re-read this pass) |

### B.2 Registrant state (Line 3)

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Name at first appearance | "HALFMOON PARENT, INC. (Exact name of registrant as specified in its certificate of incorporation) Delaware … 82-4991898" | CG01 `s4.htm` l.52-53 (verified), T1, FACT | High |
| Rename | 8-K filed for event 2018-12-20: registrant is "Cigna Corporation"; cover carries "Halfmoon Parent, Inc. (Former name…)"; EIN 82-4991898 carried forward from the shell | CG02 `form8k.htm` l.36, l.77-78 + EIN `grep -c` this pass = 1 in s4, 1 in form8k (T1, FACT) | High |
| Merger mechanics | "Cigna Corporation (now known as Cigna Holding Company)" … "Halfmoon Parent, Inc. (now known as Cigna Corporation) … ('New Cigna')"; Merger Sub 1 merged into Cigna "with Cigna surviving … as a direct wholly owned subsidiary of New Cigna" | CG02 l.163-166 (verified this pass), T1, FACT | High — this is the clean statement that the 1981 operating corporation **survived as a subsidiary of** the registrant |
| Date of incorporation | **2018-03-06**, organised in Delaware as Halfmoon Parent, Inc. ~~**UNKNOWN — no held byte prints it.**~~ **WITHDRAWN, COR-04** — refuted by the registrant's own document family at `s4.htm` **l.48371** (`(Originally incorporated on March 6, 2018 under the name Halfmoon Parent, Inc.)`, the Annex E form-of-charter caption) and **l.5011** (`New Cigna was incorporated on March 6, 2018, solely for the purpose of effecting the mergers…`), with the identity carried at l.279/l.370 (`Halfmoon Parent, Inc., which we refer to as New Cigna`). Still standing: **not 2018-05-16 (a filing floor)**. Route **FR-2 survives, narrowed**: the *as-filed* certificate (2018-12-20 8-K12B exhibit 3-2) and the first 10-K remain indexed-but-unheld, and they would confirm the effective date rather than supply it | CG01 `s4.htm` l.48371, l.5011 (verified this pass by `grep -n "Originally incorporated"`) | **FACT** — High (that the byte prints it) / Medium (as the Delaware effective date: one lineage, and the print is a *form* of charter plus a merger-description paragraph, not the filed certificate). `l.5033`/`l.5037` give the same date to **Cigna Merger Sub** and **Express Scripts Merger Sub** — different legal persons, not corroboration |
| Founder / natural persons | None attached in any held byte for Line 3 | census | High |

---

## C. ORIGINAL PROBLEM

STATUS: WRITTEN

The standard "original problem" frame presupposes an actor who identified an unsolved need; at this stage the bytes give none for the registrant (a shell's problem is the transaction it was made for, outside the window), and for the ancestors the window sits mid-life, not at origin. The adapted question — *what problem does each held in-window document show these entities organized themselves around?* — is answerable, narrowly:

| Variable | Value | Source | Confidence |
|---|---|---|---|
| INA's own framing, 1979 | Property-casualty "was INA's first business and continues today as its largest activity"; primary operations of the property-casualty and life-and-group units "are in commercial products and related services, although both offer a complete spectrum of coverages in their markets"; P&C = 66% of consolidated revenues, 69% of pre-tax operating earnings | CG04 l.651-652, l.360-368, T1, CONTEMPORANEOUS | Medium-High (self-report, single lineage) |
| INA's health-care construction of the problem | expansion of "prepaid health care plan operations" + hospital management for others (HAI "was the first company to engage in the management of hospitals owned by others and continues as the leader in this field" — a self-superlative, uncorroborated) | CG04 l.1960-1962, l.209-213, T1, CONTEMPORANEOUS; superlative = FOUNDER-CLASS corporate claim | Medium (print); UNKNOWN (the "first/leader" claim itself — no second witness) |
| CIGNA line's problem-scope as third parties saw it, 1991 | a case in which CGLIC/LINA acted as **claim administrators under an ERISA plan** — the federal question presented is the standard of review of administrators' factual determinations; i.e., by 1991 the holding records show the family inside employer-benefit claims administration | CG06 l.6081-6096, T1 court record, CONTEMPORANEOUS | High (of the naming and role); the underlying claim facts are beyond the caption/structure pages examined this pass |
| Registrant | frame NOT APPLICABLE inside the window — the entity was a shell-to-be for a 2018 merger; its "problem" first prints in the 2018 S-4 (Express Scripts combination), outside Stage 1 | CG01/CG02 | High (out of window) |
| The 1982 combination as "the founding act" of the brand | **UNANSWERED** — zero held bytes; hypothesis inherited from the dispatch brief only; route FR-1 | probe §4/§11.3, FR-1 | High (that it is unattested) |

**What the problem was NOT, on held bytes:** not a startup. Nothing in any held in-window document shows an origin moment, a founder, or a first customer for any Line-1 entity; the earliest origin text is INA's *already-ancient* self-history at l.4-7. Reading "Cigna's Stage 1" as entrepreneurism would import the playbook's Amazon-shaped expectations onto a conglomerate mid-life and a shell. Mechanism for why the corpus looks like this: EDGAR reaches essentially nothing before ~1994, and the predecessor CIK has never been indexed (family (a) UNTRIED for it); periodical shelves returned one corporate print year of a hoped-for series (FR-4 would make it a series).

---

## D. FIRST EXPERIMENT

STATUS: WRITTEN

Adapted frame (method §7): for the ancestors, the window's genuinely experiment-shaped bytes are INA's **prepaid health care entry**, because the self-report narrates it as an entry into a new field with discrete first steps; for the registrant, the frame returns a named null.

| Variable | Value | Source | Confidence |
|---|---|---|---|
| The experiment as printed | "INA entered the prepaid health care business in **1978** with the acquisition of a prepaid health plan in California. Early in **1979**, INA acquired a second prepaid health plan in Arizona and obtained **options to purchase two others in Florida**." During 1979 the unit "adopted the name **INA Healthplan**", "established headquarters in Dallas and initiated plans to develop a prepaid health plan there" | CG04 l.1997-2011, T1, CONTEMPORANEOUS self-report | Medium (single lineage, self-narrated; no external witness to any of the four steps) |
| Product of the experiment | **The whole sentence is in the byte — the "truncation" was a mis-read (COR-06).** "INA Healthplan provides comprehensive medical services, including preventive check-ups, physician office visits, and hospitalization, **for a pre-determined monthly fee**. Individuals and families are able to obtain health care services at a cost which they know in advance. **Subscribers join the plan primarily through their employers.**" (`INAC2115_1979_djvu.txt` **l.2012-2019**, unbroken; re-joined once across the hyphenated break `hos-/pitalization` at l.2014-2015 per the appendix's stated convention) | CG04 l.2012-2019 (re-read this pass; the shelf-edge claim against it was `l.2012-2013` only) | Medium (print complete, self-reported). ~~the sentence is incomplete in the byte — the completion is UNKNOWN~~ **WITHDRAWN**. What the completion actually supplies is a **prepaid monthly-fee product design** and an **employer-based subscriber channel**; what remains UNKNOWN is the price *level*, the provider network, utilization, and every membership/enrollment count |
| Parallel health build-out, same report | 1979: HAI "acquired two hospitals, began construction of two others, commissioned one new facility, began expansion programs at five, and reached agreements to acquire four others"; signed 20 new management agreements, year-end contracts for 94 hospitals / 11,000+ beds; owned 17 skilled-nursing facilities 2,000+ beds after acquiring two; International Division bought two hospitals in Australia and took UK/Saudi/UAE/Singapore management agreements | CG04 l.1954-1994 | Medium (self-printed counts, no second witness — the classic unsourced company count that method §10 flags) |
| What was learned / not learned | Nothing independent for the prepaid unit: no membership figures, no plan-level results, no failure narrative **about that unit** — ~~no failure disclosure in the held report~~ **is withdrawn (COR-07)**, because the same report *does* print in-window adverse product-line results elsewhere: annuity **revenues "decreased 5% to $195.8 million"** with a stated cause (CG04 **l.1754-1760**; table cell l.1645 `Annuity 195,825 24`; a further decline in annuity purchases at l.2217), a **Blyth Eastman Dillon operation loss** (l.503, l.516) and the 1975 P&C **"loss of $2 million"** (l.444, which §K.2 already carried). The annuity line is now a row in `failures.csv` and §M. Whether the Florida options were exercised is **UNTRIED** (the report is the only held byte; later years absent — FR-4 asks companion years 1940-1981) | CG04 l.1754-1760, l.444, l.503, l.2217 + probe §10 FR-4 | High (of the prepaid-unit silence) / Medium (of the newly carried annuity decline, a self-report against its own interest) |
| Registrant first experiment | **NAMED NULL, kept** — no held byte places any Halfmoon activity **inside the window**; COR-04's re-dating puts the shell's birth at 2018-03-06, still 22+ years after 1995-12-31, so this null is untouched by it. The shell's first documented act anywhere is the 2018 S-4 filing line. Route FR-2 (narrowed: the as-filed charter, not the date) | CG01 l.48371/l.5011, CG11 | High |
| 1982-combination "first act" | Hypothesis, unattested — see §C, §U.3 frame; FR-1 | probe §11.3 | — |

**D.2 Assessment** *(coda duty — evidence · mechanism · alternative · confidence, method §7/§16; completed at COR-11)*. The prepaid-health rows are the closest the held corpus comes to a founder-style experiment narrative, and they carry a different epistemic weight than Amazon's audited July-1995 trading: every figure is the company's own prose in a promotional year-end report, with no auditor's statement behind the plan counts and no press witness in the corpus. It is honest to say: one company, one document, describing itself buying its way into a field, and calling it growth. **Alternative explanation not excluded:** the sequence may be ordinary portfolio expansion by a diversified carrier — buying plans, renaming the unit, opening a headquarters — rather than an "experiment" in any founder sense, and nothing in the byte distinguishes the two readings because the byte prints no decision record at all; the experiment frame is this dossier's adaptation of the playbook's §7 shape, not the company's word. **Mechanism** for the shape of the evidence: only the annual report survives on the shelf for 1979 (FR-4 would supply the companion years). **Confidence: Low as a decision-as-decision, Medium as print** — the same split `decisions.csv` carries for these rows, so the coda cannot sit above the register. What the window's *independent* records show instead is litigation — which §L and §M use as the external witness set.

---

## E. PRODUCT RECONSTRUCTION

STATUS: WRITTEN

Reconstruction is limited to what the held bytes name; each row states the legal person it belongs to. Health-insurance vocabulary is admitted **only with entity adjacency** (dispatch rule): the adjacency check was run this pass over the INA report and the court shelves — `membership`, `PPO`, and `policyholder`-as-customer rows return **no managed-care naming inside the window**; what survives is INA's own "prepaid health care" wording attached to INA Healthplan, and the ERISA claim-administrator role attached to CGLIC/LINA. **Scope note added at COR-05:** "no managed-care naming **in-window**" is the measured claim. `PPO` word-bounded is 0 across the whole corpus; `managed care` is 0 in-window but **5 occurrences in the held out-of-window S-4 lineage** (`s4.htm` l.26112/29379/33424/47186), which describes Cigna Corporation in 2018 and is not admitted as in-window vocabulary here.

| Line | Product / service, as named by a held byte | Source | Class / Confidence |
|---|---|---|---|
| 1 (INA) | Property-casualty insurance, "commercial products and related services" at the core, "complete spectrum of coverages" at the edges | CG04 l.360-368 | FACT (of the print) / Medium |
| 1 (INA) | Life and group insurance via Life Insurance Company of North America, INA Life, Investors Life, Horace Mann; group coverage sold to "businesses, professional societies, trade associations, and other groups" | CG04 l.384-389, l.195-199 | FACT (of the print) / Medium |
| 1 (INA) | Health care as three distinct products: hospital **ownership** (48 hospitals / 7,200 beds own-account), hospital **management for others** (94 contracts / 11,000+ beds), **prepaid health plans** (INA Healthplan — and as of COR-06 the byte prints its design and channel too: "comprehensive medical services, including preventive check-ups, physician office visits, and hospitalization, **for a pre-determined monthly fee**", "Subscribers join the plan **primarily through their employers**", l.2012-2019), plus rehabilitation services | CG04 l.1948-1994, l.396-412, l.2012-2019 | FACT (of the print; counts self-reported) / Medium |
| 1 (INA) | Investment management, incl. the Blyth Eastman Dillon position "in connection with the merger" — investment-banking operations reclassified to **equity basis** in 1979 (footnote to the highlights table) | CG04 l.8-10, l.103, l.3666-3669 | FACT / Medium |
| 1 (CIGNA family) | Financial advisory/securities distribution implied by party names only: **CIGNA Individual Financial Services Company**, **CIGNA Securities, Inc.**, an individual agent (Nicholas Disette) as respondents; CSI + CIFSCO merged into **CIGNA Financial Advisors, Inc.** | CG07 l.19-30, l.2484-2487 | FACT (captions); product substance UNKNOWN — the held bytes examined do not print "annuity"/"variable life" (searched this pass); case subject-matter UNREAD beyond caption+structure pages |
| 1 (CIGNA family) | ERISA plan claim administration (medical-benefit determinations for employer-plan participants) — CGLIC/LINA named as "claim administrators" in the questions presented | CG06 l.6081-6096 | CONTEMPORANEOUS OBSERVATION / High (of the role), the benefit facts UNREAD |
| 3 (registrant) | none inside the window; first product statement is the 2018 S-4's "medical, pharmacy, behavioral, dental, disability, life and accident insurance" sentence about **Cigna Corporation (1981)** (l.4997), i.e. Line-1/2 successor paper, out of period | CG01 l.4997, verified this pass | RESTATED at 2018 / High (of the print) |

**E.1 What cannot be reconstructed.** ~~No plan design, no premium pricing~~ **corrected at COR-06: a plan design and a pricing *basis* ARE printed** — a pre-determined monthly fee covering preventive check-ups, physician office visits and hospitalization, subscribed chiefly through employers (CG04 l.2012-2019). What genuinely cannot be reconstructed is the **fee level** (no dollar figure for the monthly fee anywhere in the byte), the provider network, utilization data, and **any count** — members, policies, enrollments. Those zeros were re-measured here, and one of the audit's supporting zeros did not reproduce: `policy count` = **0** corpus-wide (correct), but `enroll` is **not** 0 — it occurs **11 times, all of them inside `sources/periodicals/micro_IA41153629_0618_djvu.txt`** (l.50, l.408, l.912, l.1166, l.1173, l.1320, l.1327, l.1509, l.1561, l.1593, l.1650), the 1992 ERIC **charter-school decoy** (CG12/S4418) where the word means parents enrolling children in school. **`enroll` = 0 in every insurance, court and corporate byte**, which is the claim that matters and which survives. Likewise `membership` prints once in the INA report — l.2618, "suggestions for **board** membership" — so "absent" was wrong but "no membership count" is right (COR-09). Beyond the counts: nothing about how a 1995 CIGNA medical product actually worked — the judicial records are procedural filings, and the one corporate print year is a marketing-grade report whose financial statements pages were not fully digitised (the highlights table's 1978 column shows OCR damage; see §K). Best route for product substance: FR-1 (predecessor CIK 10-Ks) and FR-4 (companion INA report years, Best's Review class trade press).

---

## F. CUSTOMER

STATUS: WRITTEN

| Variable | Value | Source | Class / Confidence |
|---|---|---|---|
| INA's customers, as INA names them | "businesses, the professions, and individuals" (a 1979 presentation theme); life/group customers specifically "businesses, professional societies, trade associations, and other groups"; hospital-management clients include "publicly owned, non-profit, and university-teaching institutions" | CG04 l.474-483, l.195-199, l.1966-1968 | CONTEMPORANEOUS self-report / Medium |
| CIGNA-family customers, as third parties show them | adverse parties: individual petitioners against claim administrators (Pierre — the estate of an individual claimant); individuals against the financial-services arm (DeBlase — "DR. JOSEPH C. DEBLASE, AND BEN CERRA"). The only in-window view of who faced these entities is **as litigants** | CG06 l.6102-6107; CG07 l.19-30 | CONTEMPORANEOUS (court filings) / High (of the names); do NOT generalize purchasers from plaintiffs |
| Counts | membership, policy count, plan enrollment, claim volume: **UNKNOWN everywhere** — no held byte prints any (searched this pass; wording corrected at COR-09: ~~`membership` absent from INA report~~ — the **token** occurs once, at l.2618, in a sentence about **board** membership, which is not a customer count. The load-bearing claim is the one that survives measurement: **no membership *count* is printed in the held report**, and `enroll` = 0 / `policy count` = 0 corpus-wide) | census | High (of the absence of **counts**); route FR-1 |
| First customer | frame NOT APPLICABLE — no origin event is in the corpus for any line; for the registrant the concept is empty (shell) | — | — |
| Independence behind the customer picture | none: the self-report side is one promotional lineage; the court side is third-party but selection-biased toward disputes. There is **no independent count** of satisfaction, retention, or scale for any 1979–1995 product statement in this corpus | method §2 null | — |

---

## G. SUPPLY / HOST SIDE

STATUS: WRITTEN

Adapted frame for insurers: "supply" is capital, balance-sheet reserves, and delivery capacity, not vendor contracts.

| Variable | Value | Source | Class / Confidence |
|---|---|---|---|
| Loss-reserve load-bearing | property-casualty reserves for losses and LAE **$2.9B** at year-end 1979, +$392M / +15% over 1978; 1975-79 compound +18%; reserves "grew more rapidly than earned premiums"; reserves-to-**earned**-premiums 111% (1979) vs 105% (1978) vs 96% (1975) | CG04 l.750-762 | CONTEMPORANEOUS self-report / Medium (audited statements exist in the same report but the digitised layer's statement pages are partial) |
| Leverage discipline, self-printed | premiums-**written**-to-statutory-surplus 3.0-to-1 in 1979, down from 3.5 (1978) and 4.5 (1975); "common stock investments … maintained at conservative levels" | CG04 l.765-773 | Same basis, labelled WRITTEN per row |
| Delivery capacity (health) | HAI owns 48 hospitals / 7,200 beds; manages 94 / 11,000+ beds; SNFs 17 / 2,000+ beds — supply-side vertical integration printed by the company itself | CG04 l.1948-1979 | CONTEMPORANEOUS self-report / Medium |
| Capital-markets side | Blyth Eastman Dillon merger carried GNMA "holdings and commitments to acquire approximately **$1.2 billion** ($700 million at January 31, 1980) of securities and commitments and options to sell similar amounts" — a large two-sided position printed in the notes | CG04 l.3666-3674 | CONTEMPORANEOUS (financial-statement note) / Medium-High |
| Acquired-entity feed | HMO International acquired December 1978 "through an exchange of stock … accounted for as a purchase"; pro-forma effect "would not have been material" (company's own words) | CG04 l.3676-3709 | Same |
| Registrant | no supply side in-window; its 2018 "host" structure (Merger Sub 1/2, Halfmoon I/II) is Line-3 material at Stage 3 | CG02 l.163-167 | — |

---

## H. MARKET (AS KNOWABLE IN-PERIOD)

STATUS: WRITTEN

What a 1979–1995 observer could have known **from this corpus**, with each basis stated:

| Variable | Value | Source | Class / Confidence |
|---|---|---|---|
| P&C industry size, 1979 | "approximately 2,900 firms which generated an **estimated** premium volume of **$90 billion** in 1979" — INA's own estimate of its industry, printed in INA's report; basis: gross premium volume, nominal, US domestic | CG04 l.653-657 | ESTIMATE-as-printed (a company's cite of an outside estimate; no outside document held) / Medium |
| INA's share arithmetic | $2.78B written premiums ÷ ~$90B industry ≈ **3.1%** (DERIVED: 2,780/90,000; numerator written-basis, denominator estimated volume — the two bases differ, flag carried) | CG04 l.675-676, l.655-657 + this pass | DERIVED / Medium |
| Growth comparison the company printed | INA life premium growth "23% annual compound … compared with 9% growth for the overall field"; health-care pre-tax compound 45% since 1975 | CG04 l.381-384, l.451-455 | CONTEMPORANEOUS self-report (market denominator unsourced in the byte) / Medium at most |
| International breadth claim | "operates in approximately 145 countries" | CG04 l.8 | self-print / Low-Medium |
| Anything about the *health-insurance* market as such | UNKNOWN — no held byte sizes managed care, PPO share, or membership growth for 1979–1995; the natural carriers (Best's Review, Business Insurance, Mortality) were queried by the fleet and returned 1 NULL row, facet-artifact status unresolved (RD-130), FR-4/FR-5 | probe §Untried-5 | High (of the silence being *query-scope*, not market) |

**H.1 coda duty (method §7/RD-034).** The market as knowable in-window looked like: a 2,900-firm P&C field INA itself estimated at $90B; a prepaid-health niche that INA treated as worth buying into at plan-level prices; and a life-group field growing 9% a year against INA's claimed 23%. Whether anyone outside INA's own report could have verified those denominators, mechanism UNKNOWN — the held bytes contain no independent market data at all, and per the record-selection null the absence is partly artifact of what was digitised, not of what existed.

---

## I. COMPETITION

STATUS: WRITTEN

| Variable | Value | Source | Class / Confidence |
|---|---|---|---|
| Named competitors in held in-window bytes | **NONE.** The INA report names only its own units, one acquired counterparty (HMO International), and one investment-banking counterparty absorbed via merger (Blyth Eastman Dillon). No rival carrier, no blue-cross/HMO-class competitor, is named by any held byte examined | census this pass + probe §4 | High (of the held-bytes silence); **UNTRIED as a fact about the world** — competitor names were in no query (FR-4/FR-7) |
| Industry counts as competitive context | 2,900 P&C firms (above, §H); "leading providers" self-description in life/group | CG04 | Medium |
| The registrant | frame NOT APPLICABLE in-window (shell); its first named rivalry context is the 2018 S-4's PBM/insurance convergence language, outside the window | CG01 | — |
| Bad-name adjacency guard | `assessingitperfo00wils` (1988) prints "CIGNA Corporation" in a **research-sponsor acknowledgment list** — naming, zero chronology, no competitive content; RD-124 applied. The probe's decoy table (its §5) governs all six such layers | CG10 | — |

---

## J. TECHNOLOGY

STATUS: WRITTEN

No held in-window byte describes a technology, platform, system, or process of any line; the era's natural carriers (trade press on claims systems, provider-data networks) are exactly the facets that returned NULL or were never asked facet-free. This is a named **query-scope** silence, not a null about the companies: `Best's Review`/`Business Insurance`/`Mortality` tasks exist with 1 NULL row (RD-130 facet caveat), and 81 of 96 harvest candidate rows sit unmined (A4 as re-measured this pass; see §U.5). Frame adaptation note: for an insurer-stage dossier, technology would ordinarily run through claims-processing and network data; nothing here reaches that. Route: FR-4 backlog, then FR-1 filings' Item 1/2. **J is not an empty section: it is the recorded absence, with its remedy.**

---

## K. MONEY / PERSONAL FINANCES

STATUS: WRITTEN

**Personal finances: frame NOT APPLICABLE** — no founder exists for any line inside the window (no natural person attached in any held byte), and none of the three lines has household-level money in the corpus. The corporate-money frame is adapted to underwriting and capital, and every premium row carries its basis label (gross/written vs earned) per dispatch rule. All figures are from the single 1979 INA self-report unless noted; the whole set is therefore **one lineage** and capped Medium. OCR damage is disclosed where it exists.

### K.1 Consolidated, dollars in millions unless noted (CG04 l.80-100 highlights table)

| Metric | 1979 | 1978 | Basis label / note |
|---|---|---|---|
| Revenues | **4,551** | 4,025 (+13%) | gross, as-printed; clean both years |
| Net operating income | **245** | "21" — 1978 cell **OCR-damaged**, NOT read as 211 | clean 1979 cell only |
| Realized securities gains net of taxes | 17 | 2 (+750%) | as-printed |
| Net income | **262** | 214 | clean both cells; change % garbled |
| Total assets | **8,987** | 8,036 (+12%) | clean |
| Shareholders' equity | **1,526** | "1 307" — OCR space-split (readable as 1,307 with a defect; treated as damaged-print) | clean 1979 cell |
| Primary EPS: net operating / net income | $6.34 / $6.13 | $5.58 / $5.39 | as-printed; post 3-for-2 split |
| Dividends declared per share | $2.05 | $1.73 | as-printed |
| Return on equity | 17.1% | 17.0% | as-printed |
| Employees | **35,280** | 33,987 | headcount, self-printed |
| Average shares outstanding | 38,579,370 | 37,888,500 | as-printed |

### K.2 Segment and underwriting detail (CG04 l.366-460, l.653-770)

| Metric | Value | Basis label |
|---|---|---|
| P&C group pre-tax income | $213.4M (1978: $209.3M; 1975: a **loss** of $2M) | company-segment, nominal |
| P&C **written** premiums | $2.78B (1978: $2.55B, +9%) | GROSS/WRITTEN — never earned |
| Combined ratio, before policyholders' dividends | 101.8% (1979) vs 99.8% (1978) | **mixed basis printed by INA itself**: claims(-to-earned) + expenses(-to-written) — >100% = underwriting loss on that definition |
| 1978 underwriting losses | $84.8M (prior year $20.8M) — "unprecedented series of disasters, including hurricanes David and Frederic" | company-level |
| Life group pre-tax income | $67.1M, +19% (1978: $56.2M); compound 28% since 1975 | segment |
| Health-care group pre-tax income | **$41.6M, +48%** (1978: $28.1M); compound 45% since 1975; group = 12% of revenues, 14% of pre-tax operating income | segment |
| Investment income | $450.4M, +27% (1978: $353.4M) | consolidated |
| Loss reserves | $2.9B year-end; 111% of **earned** premiums | earned-basis ratio |
| Premiums written-to-surplus | 3.0-to-1 (3.5 / 4.5 in 1978/1975) | written-basis leverage |
| Goodwill | aggregate $82,684,000; ~$27.6M pre-1971 non-amortized; extra $4.3M charged to operations 1979 | statement note |
| Parent company and other operations | 4% of revenues and **a 5% pre-tax loss** contribution | segment |

### K.3 What money facts are missing (named routes)

For **no line** does the corpus hold: a 1982 combination cost, a membership- or premium-based health series, CIGNA-corporate 1990s financials (FR-1), the registrant's own any-year financials (first 10-K indexed but **unheld** — FR-2/FR-3), or an auditor's opinion read from the digitised pages (the report's statement pages are partial in OCR). A null on the *written-vs-earned* split for health is recorded: the INA report prints earned only via ratios, never via a health-line dollar figure.

STATUS: WRITTEN

---

## L. VALIDATION SIGNALS

STATUS: WRITTEN

| Date | Signal | Magnitude | What it demonstrated | What it did NOT demonstrate | Source | Confidence |
|---|---|---|---|---|---|---|
| 1979 | Health-care group pre-tax income up 48% to $41.6M, 45% compound since 1975 | self-printed dollars | that INA's own books, as INA described them, showed the health segment growing faster than any other | that growth was externally verifiable, durable, or strategic — no second witness; single promotional lineage | CG04 l.451-455 | Medium (of the print) |
| 1979 | Prepaid plan #2 acquired (Arizona) + options on two Florida plans + Dallas build-out initiated | 3 discrete expansion steps | the company was repeating the buy-a-plan pattern within a year of entry | unit economics of any plan; whether options converted (UNTRIED) | CG04 l.1997-2011 | Medium |
| 1989 / 1991 / 1994-95 | Three independent Supreme Court records name the family: CGLIC as a party; the full CGLIC+LINA → Conn. Gen. Corp. → CIGNA Holdings → CIGNA Corporation chain; CIGNA Corporation as respondent with a parentage sentence | 3 filings, 3 different cases | **external persistence and structure of Line 1 across seven years** — the strongest independent witness this window holds, because these are third-party filings, not company copy | anything about performance, scale, customers, or the 1982 combination | CG05, CG06, CG07 | High (structure) |
| 2018-09-21 (out of window; terminal marker of Line 1) | Indenture "Designated Subsidiary" clause names both ancestor carriers with a "successor of" provision | 2 exhibits, one accession | that both ancestors were still contractually material 27 years after the window closes — a durability fact, not a validation of any in-period decision | nothing in-period at all; carried in notes only | CG01-family ex4-1 l.2584 / ex4-2 l.72 | High (print) / firewall-tagged |

**L.1 coda (method §7 duty).** The independent validation pattern of this window is *survival and structural legibility*, printed by courts, not by markets: the only non-company witnesses for 1979–1995 name the family repeatedly and say nothing about how well it sold anything. Mechanism for why: the families that would carry market validation (trade press, competitor press, filings of the predecessor CIK) are precisely the ones RD-130/FR-1/FR-4 show as never-fully-asked. Alternative explanation not excluded: period press validation exists in abundance and simply has not been harvested. Confidence that "no held validation is not no validation": **High — the probe's UNTRIED list forbids the stronger reading.**

---

## M. NEGATIVE SIGNALS / FAILURES

STATUS: WRITTEN

| Date | Signal or failure | Magnitude | What it demonstrated | What it did NOT demonstrate | Source | Confidence |
|---|---|---|---|---|---|---|
| 1979 | Combined ratio 101.8% (before policyholders' dividends), vs 99.8% in 1978; "a sharp increase in investment income offset higher underwriting losses" | >100 = underwriting loss on INA's own mixed definition | the P&C core lost money on underwriting in 1979 and was carried by investments | segment-level or accident-year detail; whether "disaster-driven" was the whole story (company's attribution, unverified) | CG04 l.742-747, l.664-665 | Medium (self-report against interest) |
| 1978 | Underwriting losses $84.8M vs $20.8M prior year; hurricanes David and Frederic, Eastern/Midwest winter storms, tornadoes named | 4× jump | a genuine bad-loss year in the company's own print | comparative industry loss experience (no external denominator held) | CG04 l.678-684 | Medium |
| 1975-79 | Loss reserves grew faster than earned premiums every measured year; reserves-to-earned 96% → 111% | +15 pts in 4 years | a widening reserve-to-premium load printed by the company itself | adequacy or weakness — rising reserves can be prudent; the byte prints the ratio, not its meaning | CG04 l.757-762 | Medium (ratio) / **UNKNOWN (interpretation)** |
| 1979 | Parent company & other operations: 4% of revenues, **5% pre-tax loss** | segment loss | disclosed loss area inside a headline-growth year | size of the loss in dollars (not printed in held layer) | CG04 l.414-416 | Medium |
| 1978-79 | Goodwill charges: extra $4.3M written off through operations (on top of normal amortization); $4.2M pre-1971 goodwill written off in 1978 | statement-note scale | management's own review downgraded parts of acquired value | which acquisitions (allocation not printed) | CG04 l.3712-3719 | Medium |
| 1989 / 1991 / 1994-95 | Line 1 appears in federal litigation three times, always as the party below: CGLIC as respondent (Creative Bath), CGLIC/LINA as respondent claim administrators (Pierre), CIFSCO/CIGNA Corp/CIGNA Securities/individual as respondents (DeBlase) | 3 records | that adverse proceedings reached the Supreme Court docket — external, non-company visibility of disputes | merits, outcomes, settlement values, or frequency (the corpus holds cert papers, not dockets or results) | CG05, CG06, CG07 | High (of the naming) / outcome **UNKNOWN** |
| 1988-11-18 | "US firm Cigna sells its South African operations to local management" — printed in a CIA *Africa Review* monthly chronology, the single "Cigna" hit in that document | divestiture of a country operation | an externally-compiled contemporaneous record of a CIGNA-line retreat from South Africa under disinvestment pressure | that this was corporately significant or distinctive (many US firms did so; the memo is a press-roundup, one lineage, no company doc corroborates) | CG08 l.1174 | Medium-Low |
| 1995-12-31 | the registrant line: **no failure and no success is observable — it did not exist**; the risk it was later created to carry (a merger) is Stage-3 material | — | firewall: silence here must not be read as the ancestors' silence | — | CG11 | High |

---

## N. FOUNDER DECISIONS

STATUS: WRITTEN

No founder; the mandatory decision set is therefore **corporate decisions evidenced inside the window**, in the fixed 12-field shape (cells the bytes cannot fill are UNKNOWN, not trimmed):

| Date | Decision | State before | Information available | Unknowns | Alternatives | Constraints | Rationale | Expected result | Actual result | Evidence | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1978-12 | INA acquires **HMO International** by stock exchange; accounted for as a purchase | prepaid health care since 1978 (California plan #1) | company's own note: pro-forma effect on revenues/net income/EPS "would not have been material" | board deliberations; consideration ratio rationale; who proposed | UNKNOWN | stock-for-stock terms as printed | "expanded … prepaid health care plan operations" (chairman text) | not printed | in-window: consolidated into Health Care Group print; post-1979 **out of scope** | CG04 l.3676-3709, l.1997-2004 | Medium (event, self-report) |
| early 1979 | Buy a second prepaid plan (Arizona); **take options on two Florida plans**; name the unit INA Healthplan; HQ to Dallas; initiate building a Dallas plan | 1 plan, 1 year in | nothing in the bytes beyond the print itself | why Dallas; did the Florida options later convert (UNTRIED) | build-only (they did begin a Dallas build); abandon | capital unknown | expansion "accelerated growth both domestically and internationally" (chairman) | not printed | bounded: unit existed to print at year-end | CG04 l.1997-2011, l.201-213 | Medium |
| 1979 | P&C: accept a combined ratio >100% and lean on investment income ("actions taken earlier to add … tax-exempt securities and foreign securities" drove after-tax P&C income +15%) | 1978's $84.8M underwriting loss | the report's attribution of earnings mix | whether pricing action was considered and rejected (record-selection null: rejected options are exactly what is unrecoverable) | raise rates / shrink book — named as alternatives only as generic insurer options, NOT as evidenced discussions | reserve load rising (L/M) | "sharp increase in investment income offset higher underwriting losses" | not printed | window ends with ratio still >100 | CG04 l.660-674, l.742-747 | Medium (print) / Low (decision-as-decision) |
| — | Registrant decisions in-window | **none observable**: a shell with no held pre-2018 byte made no recorded decision inside the window; the 2018 name choice (shell takes the Cigna name) is Line-3 Stage-3 material | — | its incorporation date itself (FR-2) | — | — | — | — | — | CG11 | High (of the silence) |

**N.1 firewall note.** No row above is narrated as a step toward anything later; the HMO International note's own "not material" sentence is kept *against* any retrospective weight.

---

## O. COUNTERFACTUAL OPPORTUNITIES

STATUS: WRITTEN

Adapted, kept thin because the corpus is thin: (i) the Florida **options** (1979) are the one held byte that names an unconverted branch — whether they were exercised is UNTRIED and FR-4's companion report years would answer it; (ii) the 1978/1979 build-vs-buy mix at INA Healthplan (Dallas "initiated plans to develop" — a self-funded plan attempted beside acquisitions; its outcome UNKNOWN, no later-year byte held); (iii) for Line 1's health carriers, the entire managed-care ascent of the 1990s sits inside the window and **not one held byte speaks to it** — the honest counterfactual statement is that the corpus cannot say whether CIGNA participated in it, let alone chose anything; the membership-vocabulary silence (§E) is a *shelf* fact. For Line 3 there is no counterfactual inside the window: a nonexistent entity forgone nothing. All claims in §O: **UNKNOWN** class with named routes; none is a null (method rule 5).

---

## P. QUANTITATIVE METRICS TABLE

STATUS: WRITTEN

| ID | Date | Metric | Value | Unit | Source | Source date | Confidence |
|---|---|---|---|---|---|---|---|
| P01 | 1979-12-31 | INA consolidated revenues (gross, as printed) | 4,551 | USD millions | CG04 l.82 | 1979 (report) | Medium |
| P02 | 1979-12-31 | INA net income | 262 | USD millions | CG04 l.85 | 1979 | Medium |
| P03 | 1979-12-31 | INA total assets | 8,987 | USD millions | CG04 l.86 | 1979 | Medium |
| P04 | 1979-12-31 | INA shareholders' equity | 1,526 | USD millions | CG04 l.87 | 1979 | Medium |
| P05 | 1979-12-31 | INA employees | 35,280 | persons | CG04 l.97 | 1979 | Medium |
| P06 | 1979-12-31 | P&C **written** premiums (gross written basis — NOT earned) | 2,780 | USD millions | CG04 l.675 | 1979 | Medium |
| P07 | 1978-12-31 | P&C written premiums, prior year (written basis) | 2,550 | USD millions | CG04 l.676 | 1979 (report on 1978) | Medium |
| P08 | 1979-12-31 | Combined ratio before policyholders' divs (claims-to-earned + expense-to-written, INA's own mixed definition) | 101.8 | percent | CG04 l.746 | 1979 | Medium |
| P09 | 1979-12-31 | Loss & LAE reserves (P&C) | 2,900 | USD millions | CG04 l.752-753 | 1979 | Medium |
| P10 | 1979-12-31 | Reserves-to-**earned** premiums (earned basis) | 111 | percent | CG04 l.761 | 1979 | Medium |
| P11 | 1979-12-31 | Health-care group pre-tax income | 41.6 | USD millions | CG04 l.451-452 | 1979 | Medium |
| P12 | 1979-12-31 | US P&C industry premium volume, per INA's own **estimated** figure | ~90,000 | USD millions (estimated) | CG04 l.656-657 | 1979 | Medium (of the print) / Low (as market fact) |
| P13 | 1979-12-31 | INA share of that estimated industry: DERIVED 2,780 ÷ 90,000 | ≈3.1 | percent | this pass; CG04 both inputs | 1979 | Low-Medium (mixed bases) |
| P14 | 1979 / 1995 | Occurrences of `1792` in the whole corpus (both in CG04 l.5, l.371); in-window SCOTUS naming records: 3 | 2 / 3 | occurrences / documents | census this pass; probe §4 | 2026-10-06 | High (re-measured) |
| P15 | 1995-12-31 boundary | Filings enumerated for CIK 0001739940 (complete walk; floor 2018-05-16; 0 UNANSWERED slices) | 1,018 | filings | CG11 `_index/submissions.csv` (1,019 lines incl. header; measured this pass) | index 2026 | High |
| P16 | window-wide | Registrant financials inside 1979-1995 | **UNKNOWN** — no byte | — | CG11 + probe §2 | — | High (of absence-in-corpus) |

---

## Q. CHRONOLOGICAL MICRO-TIMELINE

STATUS: WRITTEN

Three columns of one record, never merged. Line 1 = ancestors; Line 2 = the asserted 1982 combination (hypothesis row, unattested); Line 3 = the registrant.

| Date | Line | Event, as the byte prints it | Witness type |
|---|---|---|---|
| 1792 | 1 (INA) | "formation of … Insurance Company of North America" — the parent's 1979 retrospective self-dating only | company self-report, RESTATED |
| 1957 | 1 (INA) | "INA's life insurance business began in 1957" (self-printed) | self-report, restated-in-1979 |
| 1969 | 1 (INA) | "INA entered the health care field in 1969" | self-report |
| 1978 | 1 (INA) | Dec: HMO International acquired by stock exchange; first California prepaid plan bought; goodwill write-off $4.2M | self-report (purchase note) |
| 1979 | 1 (INA) | Annual report published (the held document); second prepaid plan (AZ); Florida options; INA Healthplan named, Dallas HQ; 2 hospitals bought/2 begun/5 expanded/20 management agreements; combined ratio 101.8% | self-report |
| **1982** | **2** | **CIGNA combination — asserted by the dispatch brief; 0 held bytes; 0 merger-verb pairings corpus-wide (probe §4). Status: UNATTESTED HYPOTHESIS, route FR-1.** | none |
| 1988-11-18 | 1 (CIGNA) | "US firm Cigna sells its South African operations to local management" (CIA monthly chronology) | third-party government roundup |
| 1989 | 1 (CIGNA) | Creative Bath Products et al. v. **Connecticut General Life Insurance Company** — cert petition; CG named as party | court record |
| 1991 | 1 (CIGNA) | Pierre v. CGLIC Rule 29.1 statement prints the full chain: CGLIC+LINA → Connecticut General Corporation → CIGNA Holdings, Inc. → **CIGNA Corporation**; Washington DC address | court record |
| 1994-1995-04 | 1 (CIGNA) | DeBlase & Cerra v. CIGNA Individual Financial Services Company, **CIGNA Corporation**, CIGNA Securities, Disette — Oct Term 1994, receipt stamp "APR 19 1995"; merger sentence: CSI+CIFSCO → CIGNA Financial Advisors, Inc. under Connecticut General Corporation | court record |
| (no date) | 3 (registrant) | incorporation of Halfmoon Parent, Inc. — **UNKNOWN, no held byte** | FR-2 |
| 2018-05-16 | 3 | registrant's first EDGAR appearance (S-4, as HALFMOON PARENT, INC.) — a floor, not a birth | EDGAR index + CG01 |
| 2018-12-20 | 3 | 8-K closing: shell renamed **Cigna Corporation**; old Cigna Corp → Cigna Holding Company, subsidiary of New Cigna; shell's EIN 82-4991898 carried forward | CG02 |

---

## R. END-OF-STAGE STRUCTURED SNAPSHOT (1995-12-31)

STATUS: WRITTEN

| Dimension | State on held evidence | Line | Knowability (method §7) |
|---|---|---|---|
| Legal structure | CIGNA Corporation at the top of a chain over Connecticut General Corporation, over CGLIC and LINA (1991 print) and over the merged CIGNA Financial Advisors (1994-95 print); INA Corporation alive in 1979 print, its later naming **unheld** | 1 | KNOWABLE (structure), NOT KNOWABLE (whether INA was inside the CIGNA chain by 1995 — zero bytes say so) |
| Registrant | nonexistent / date-unknown; measured life begins 2018-05-16 | 3 | KNOWABLE that UNKNOWN |
| Combination event | unattested | 2 | UNKNOWN — FR-1 |
| Money | last printed: 1979 INA set (P01-P13); 1980-1995: nothing held for any ancestor | 1 | UNKNOWN, route FR-4 |
| Products/health market position | "prepaid health care" (1979 INA self-naming) and ERISA administration (1991); no membership, no PPO byte | 1 | NOT KNOWABLE on this corpus |
| Competition | no named rival in any held byte | 1/2/3 | UNTRIED |
| Independent witnesses | 3 court records + 1 CIA roundup — all structure/adversity, none performance | 1 | KNOWABLE (they exist) |

---

## S. DATA GAPS

STATUS: WRITTEN

Named-route gap register (full rows in the `data_gaps` block below): **G1** registrant's own incorporation date — UNANSWERED, not none (FR-2). **G2** predecessor CIK 1979-1995 filings — UNTRIED for that registrant (FR-1). **G3** the 1982 combination — UNATTESTED HYPOTHESIS (FR-1, FR-5). **G4** second ancestor (Connecticut General line) origins 1850s-1872 — **UNTRIED**: its candidate names exist in no query (FR-7). **G5** 81 of 96 harvest candidate rows unmined (FR-4). **G6** trade-press NULL = facet artifact unresolved (FR-4). **G7** web-archive family never called (FR-6). **G8** auction/museum/manuscript never called. **G9** 18 filings never listed at `--max-docs 30` (FR-3). **G10** no `_EVIDENCE_CACHE.md` exists for this company. **G11** DeBlase/Pierre/Creative Bath subject matter unread beyond caption+structure. **G12** the *record-selection null* restated here per method §2: the internal deliberations, rejected options and contemporaneous failures behind every row in §L/§M/§N are unrecoverable because the kept archive is the winners' annual-report-and-court-docket layer; no independent count stands behind any company self-print in §K.
**Health-vocabulary specific gaps** (dispatch rule): membership/policy counts, earned-premium dollar series for any health line, PPO naming — **all UNKNOWN for 1979-1995 on this corpus, TRIED this pass over held bytes and answered nothing; the route that could answer is FR-1 (10-K Item 1/2 of the predecessor) and FR-4 (companion report years + Best's class trade press).**

---

## T. SOURCE / PROVENANCE TABLE

STATUS: WRITTEN

| Source | Type | Primary/Secondary | Event date | Publication date | URL | Tier | Confidence |
|---|---|---|---|---|---|---|---|
| CG01 S-4 (Halfmoon Parent, Inc.), acc. 0001140361-18-024107 (+4 amendments + exhibits = **same lineage**) | registration statement | primary (registrant's own paper) | 2018 | 2018-05-16 | local `sources/sec/0001140361-18-024107_s002268x1_s4.htm` | 1 | High (print) |
| CG02 8-K acc. 0001140361-18-045493 | current report | primary | 2018-12-20 | 2018-12-20 | local `sources/sec/0001140361-18-045493_form8k.htm` | 1 | High |
| CG03 indenture exhibits ex4-1/ex4-2 (acc. 0000950159-18-000404) | contract exhibit | primary | 2018-09-21 | 2018-09-21 | local | 1 | High |
| CG04 INA Corporation Annual Report 1979 (item INAC2115_1979, 111,357 B) | corporate print, annual report | primary (self-report) | 1979 | 1979 | local `sources/periodicals/INAC2115_1979_djvu.txt` | 1 | Medium (single lineage; OCR damage disclosed) |
| CG05 micro_IA40385019_1642 Creative Bath v. CGLIC (94,646 B) | court record | primary (judicial) | 1989 | 1989 | local `sources/periodicals/` | 1 | High (of naming) |
| CG06 micro_IA40385013_0186 Pierre v. CGLIC Rule 29.1 (164,349 B) | court record | primary (judicial, third-party counsel filing) | 1991 | 1991 | local | 1 | High |
| CG07 micro_IA40386012_1635 DeBlase v. CIGNA Individual Financial Services (149,218 B; also stored md5-identical under corporate_print/) | court record | primary (judicial) | 1994-95 | 1995-04 (stamp) | local | 1 | High |
| CG08 CIA Africa Review rdp88t00792 (43,176 B) | government periodical compilation | secondary (roundup of press) | 1988-11-18 | 1988 | local | 2 | Medium-Low |
| CG09 CIA staff memo rdp84b00130 (4,428 B) | government internal minutes | — | 1980-04-09 | 1980 | local (both shelves) | — | **NEGATIVE ARTIFACT / DECOY** — its "Connecticut General" is the Agency's own VIP fund (probe §5) |
| CG10 assessingitperfo00wils (62,186 B) | research report | secondary | 1988 | 1988 | local | 3 | **NAMING-ONLY** — sponsor acknowledgment list; zero chronology (probe §3b.3) |
| CG11 EDGAR submissions index (1,018 rows) + `_INDEX.md` | search/measurement state | n/a | 2018-05-16→2026-09-08 | 2026 | local `sources/_index/` | 1 | High (perimeter) |
| CG12/CG13 ERIC_ED460893 + micro_IA41153629_0618 | government/education documents | — | 1995 / 1992 | — | local | — | **DECOYS** — "Connecticut General Assembly" place-name trap (probe §5) |
| CG14 micro_IA40385607_0258 etc. Rozelle/Fitzgerald/Blanchette SCOTUS rows | harvest index rows | — | 1973-77 | — | index only, **bytes UNHELD** | — | UNTRIED (pointers, not evidence — FR-4) |
| CG15 A4_harvest_mine.md (re-read this pass; 96 rows / 12 mined / 81 untried) | internal measurement record | n/a | 2026-10-06 | 2026-10-06 | local `research/A4_harvest_mine.md` | 4 | used for census only; not evidence of company facts |
| CG16 probe dossier `research/A_chronology_feasibility.md` | internal dossier | n/a | 2026-10-06 | 2026-10-06 | local | 4 | tier/lineage source of this pass's scope |

**Independence ledger (method §3):** CG01+amendments+CG03 = **one** lineage. CG04 = one lineage (self-report). CG05/06/07 = three different cases, three independent filers, **but each is a court paper, not a market witness** — they corroborate structure across years, the one thing they were never meant to hide. No pair among CG04, CG05-07, CG08 shares an origin. The md5 duplicate (CG07 across two shelves) is **one** document.

---

## U. CONFLICTING EVIDENCE

STATUS: WRITTEN

<!-- ANCHORS: U.1-U.6 -->

### U.1 "Incorporated in Delaware in 1981" vs the registrant's own identity
**CLAIM A:** "Cigna was incorporated in Delaware in 1981" (CG01 `s4.htm` l.4995 and l.23191 — one lineage, twice). **CLAIM B:** the same document family's cover names the registrant HALFMOON PARENT, INC. (l.52), and CG02 l.163-166 makes the 1981 corporation a *subsidiary* of the renamed shell. **WHY THEY DIFFER:** both are filed-true; the conflict is only in the reader's referent — A is about Line-1/2 paper, B is about Line 3. **EVIDENCE WEIGHT:** B is structural fact printed by the registrant itself about its own transaction; A is a recital whose subject is another person. **BEST-SUPPORTED INTERPRETATION:** the registrant is the 2018 continuation; "1981" describes the operating subsidiary; **no held byte gives the registrant's own incorporation date.** **RESIDUAL UNCERTAINTY:** whether Delaware filings name Halfmoon's birth date (FR-2). **CONFIDENCE:** High.

### U.2 1792: whose origin, and what class of statement
**CLAIM A:** "Its history dates back to 1792, with the formation of its principal subsidiary … Insurance Company of North America" (CG04 l.4-7; restated l.371-372 "founded in 1792 as America's first stock insurance company"). **CLAIM B:** no second witness — `1792` occurs 2 times corpus-wide, both inside this one 1979 document (re-measured this pass). **WHY THEY DIFFER:** none in the bytes; the conflict is epistemic — a retrospective self-narrative 187 years late, grammatically attributed to the **subsidiary**, then habitually re-attributed to "Cigna." **EVIDENCE_WEIGHT:** one Tier-1 self-report lineage; promotional voice. **BEST-SUPPORTED INTERPRETATION:** FACT-class origin *of INA (the subsidiary) as stated by INA (the parent) in 1979*; **not** a founding date for the registrant, and not for Line-1's Connecticut side either. **RESIDUAL UNCERTAINTY:** pre-1979 records of 1792 (FR-4/FR-8 class). **CONFIDENCE:** Medium ceiling, per probe §11.1.

### U.3 The 1982 combination and the second-ancestor date: inherited assertions vs query-scope silence
**CLAIM A (inherited from the dispatch brief/brief-lineage):** CIGNA was formed 1982 by combining Connecticut General and INA; the CG line traces to an 1850s-1872 life-insurance body. **CLAIM B (the corpus):** `1982` pairs with no merger word in any held byte; `1872` occurs 0 times; and the ancestor's candidate names appear in **no query ever run** for this slug. **WHY THEY DIFFER:** A is external folklore-level inheritance without a held carrier; B is a measured query-scope silence. **EVIDENCE WEIGHT:** neither can settle it — A lacks bytes; B is "never asked," not "nothing found." **BEST-SUPPORTED INTERPRETATION:** carry 1982 as an unattested hypothesis and 1872 as **UNTRIED** (explicitly **not null** — dispatch rule); both reach evidence only via FR-1/FR-7. **RESIDUAL UNCERTAINTY:** everything about the combination. **CONFIDENCE:** High (that the corpus cannot currently adjudicate).

### U.4 Tier reading by machine vs tier issued by dossier
**CLAIM A:** `tools/gates.py`'s tier detector reads **T3** from the probe dossier (its tie-break on `hits.sort(reverse=True)` — probe §13). **CLAIM B:** the probe §7 issues **Stage 1 = T2 core, PROVISIONAL** (2 families: (c) SCOTUS records + (d) INA 1979 report), T3 only under the strict-registrant frame. **WHY THEY DIFFER:** a tool artifact (lexicographic tie-break inside the first 30,000 chars), not evidence. **EVIDENCE WEIGHT:** B is the issued verdict; A is self-described by the probe as an observation for §15.5. **BEST-SUPPORTED INTERPRETATION:** this dossier is authored at **T2 core** (registers full, records for load-bearing claims only, ≤22k words) while §A/§B/§R carry the strict-registrant T3 reading as a *state*, never as a downgrade of the lineage work. **RESIDUAL UNCERTAINTY:** none substantive. **CONFIDENCE:** High.

### U.5 Census movement: 79/12/65 vs 96/12/81
**CLAIM A:** probe §Untried cites A4 (at 17:23) for "79 candidate rows; 12 mined; 65 untried." **CLAIM B:** `research/A4_harvest_mine.md` as re-read this pass says "96 candidate rows in the harvest index; 12 items mined; 81 left untried at the --limit" (A4 l.5). **WHY THEY DIFFER:** the fleet mine and A4 were still being rewritten while the probe was writing — the probe itself documented files landing mid-pass at 17:22-17:23. **EVIDENCE WEIGHT:** B is the later measurement of the same index. **BEST-SUPPORTED INTERPRETATION:** report **96/12/81** as this pass's census with the 79/65 earlier reading preserved here; a capped enumeration is a sample, never a census (RD-134), so both numbers are *movement*, not verdicts. **RESIDUAL UNCERTAINTY:** the index may still be growing. **CONFIDENCE:** High (both measurements; of their readings).

### U.6 Shelf-vs-family miscount: the annual report lives on the periodicals shelf
**CLAIM A:** family-(d) "digitised corporate print" would read 0 from `sources/corporate_print/` (it holds one CIA staff memo and one md5-duplicate court record). **CLAIM B:** the shelf-independent document class is the family: CG04 is an **annual report** (Tier-1 corporate print by document class) stored under `periodicals/`. **WHY THEY DIFFER:** harvester placement, not content. **EVIDENCE WEIGHT:** B governs (probe §12 handoff rule: family counting follows document class, not shelf). **BEST-SUPPORTED INTERPRETATION:** family (d) = ANSWERED by CG04; `corporate_print/` directory size must never be quoted as "print bytes." **RESIDUAL UNCERTAINTY:** none. **CONFIDENCE:** High.

---

*End of narrative. Conflicts U.1–U.6 each carry a row in the `conflicts` block below (1:1 parity for the merge). This is part 1 of 1 for Stage 1; claim records immediately follow, then registers.*

---

## CLAIM RECORDS APPENDIX (A–U)

STATUS: WRITTEN

T2 rule applied: records for **load-bearing claims only**. Line numbers are locators as read 2026-10-06 by this pass; cite by stable label (CG-nn, P-nn, U.n). Where the digitised layer splits a sentence across lines with hyphenation, the passage is the re-joined print and says so. `Corroboration` counts **independent origins** per method §3, not copies.

A01 Claim: The registrant CIK 0001739940 is Halfmoon Parent, Inc., the Delaware shell renamed Cigna Corporation at the 2018-12-20 merger closing. — Date: 2018-12-20 — Source: Form 8-K, acc. 0001140361-18-045493 — Source date: 2018-12-20 — URL: local sources/sec/0001140361-18-045493_form8k.htm — Archived: local bytes — Tier: 1 — Class: FACT — Passage: "Halfmoon Parent, Inc. (now known as Cigna Corporation), a Delaware corporation and a direct wholly owned subsidiary of Cigna prior to the Merger" — Conf: High — Corroboration: 1 lineage (S-4 family + 8-K corroborate the same corporate record) — Conflicts: U.1
A02 Claim: No held byte anywhere in the corpus prints the registrant's own date of incorporation; its measured EDGAR life starts 2018-05-16, a filing floor, not a birth. — Date: UNKNOWN — Source: full-corpus census + `sources/_index/submissions.csv` — Source date: 2026-10-06 — URL: local — Archived: local — Tier: 1 — Class: UNKNOWN (of the date); FACT (of the silence and floor) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High — Corroboration: index walk (1,018 rows, 0 UNANSWERED slices) + probe §3.1 — Conflicts: U.1
A03 Claim: No held in-window document names CIK 0001739940 between 1979 and 1995, because that legal person was created for the 2018 Express Scripts merger. — Date: 1979/1995 — Source: probe §7 measured across 11 distinct non-SEC documents + 30 SEC files — Source date: 2026-10-06 — URL: local research/A_chronology_feasibility.md — Archived: local — Tier: 1 — Class: FACT (of the corpus state); INFERENCE (of the "because") — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High (corpus), Medium (counterfactual completeness — predecessor CIK unindexed, FR-1) — Conflicts: U.1
B01 Claim: The S-4 cover page identifies the registrant by the shell's name, state, SIC 6324 and EIN 82-4991898. — Date: 2018-05-16 — Source: Form S-4 acc. 0001140361-18-024107, l.52-53 — Source date: 2018-05-16 — URL: local sources/sec/0001140361-18-024107_s002268x1_s4.htm — Archived: local — Tier: 1 — Class: FACT — Passage: "HALFMOON PARENT, INC. … (Exact name of registrant as specified in its certificate of incorporation)" — Conf: High — Corroboration: 1 (one lineage) — Conflicts: U.1
B02 Claim: INA described itself in 1979 as one of the oldest US commercial organizations, operating in ~145 countries across property-casualty, life and group, health care, and investment management. — Date: 1979 — Source: INA Corporation Annual Report 1979, l.4-10 — Source date: 1979 — URL: local sources/periodicals/INAC2115_1979_djvu.txt — Archived: local (IA item INAC2115_1979) — Tier: 1 — Class: CONTEMPORANEOUS (self-report) — Passage: "Today, INA operates in approximately 145 countries, offering varied products and services in property-casualty insurance, life and group insurance, health care, and investment management." — Conf: Medium — Corroboration: 1 lineage; self-printed breadth — Conflicts: None
B03 Claim: The corpus's only year-bearing incorporation recital, "Cigna was incorporated in Delaware in 1981," has as its subject Cigna Corporation — a different legal person than the registrant — and appears once in one lineage, printed twice. — Date: 1981 (subject's); 2018 (recital's) — Source: S-4 l.4995 and l.23191 — Source date: 2018-05-16 — URL: local — Archived: local — Tier: 1 — Class: FACT (of the print); RESTATED (the 1981 fact within it) — Passage: "Cigna was incorporated in Delaware in 1981." — Conf: High (print) — Corroboration: 1 (two copies, one lineage — hard rule 3) — Conflicts: U.1
C01 Claim: INA's own 1979 report frames property-casualty as its first and still-largest business. — Date: 1979 — Source: INA AR 1979 l.651-652 — Source date: 1979 — URL: local — Archived: local — Tier: 1 — Class: CONTEMPORANEOUS (self-report) — Passage: "was INA's first business and continues today as its largest activity" — Conf: Medium — Corroboration: 1 — Conflicts: None
D01 Claim: INA entered prepaid health care by acquiring a California plan in 1978 — the window's best experiment-shaped first-act for the health line, printed only by the company itself. — Date: 1978 — Source: INA AR 1979 l.1999-2001 — Source date: 1979 — URL: local — Archived: local — Tier: 1 — Class: CONTEMPORANEOUS (self-report; the 1978 event is restated one year late inside a contemporaneous document) — Passage: "INA entered the prepaid health care business in 1978 with the acquisition of a prepaid health plan in California." — Conf: Medium — Corroboration: 1 — Conflicts: None
E01 Claim: A 1991 Supreme Court Rule 29.1 filing by outside counsel prints the ancestor chain: CGLIC and LINA under Connecticut General Corporation, under CIGNA Holdings, Inc., under CIGNA Corporation. — Date: 1991 — Source: Pierre v. Connecticut General Life Insurance (502 U.S. 973), micro_IA40385013_0186 l.6102-6121 — Source date: 1991 — URL: local sources/periodicals/micro_IA40385013_0186_djvu.txt — Archived: local (IA microfiche) — Tier: 1 — Class: CONTEMPORANEOUS OBSERVATION (third-party judicial) — Passage: "The parent of Connecticut General Corporation is CIGNA Holdings, Inc. The parent of CIGNA Holdings, Inc. is CIGNA Corporation" (re-joined across l.6113-6116) — Conf: High — Corroboration: 1 judicial origin, independent of every corporate lineage — Conflicts: None
E02 Claim: By the 1994-95 term a court filing prints CSI+CIFSCO merged into CIGNA Financial Advisors, Inc., a subsidiary of Connecticut General Corporation whose ultimate parent is CIGNA Corporation. — Date: bounded pre-1995-04 — Source: DeBlase v. CIGNA Individual Financial Services Co., micro_IA40386012_1635 l.2484-2487 — Source date: 1995 (receipt stamp APR 19 1995, OCR line "9417 46 APR 19 1995") — URL: local — Archived: local + md5-identical copy under corporate_print/ (ONE document, hard rule 4) — Tier: 1 — Class: CONTEMPORANEOUS OBSERVATION — Passage: "CSI and CIFSCO merged to form CIGNA Financial Advisors, Inc., a wholly-owned subsidiary of Connecticut General Corporation, whose ultimate corporate parent is CIGNA Corporation" (re-joined) — Conf: High — Corroboration: 1 — Conflicts: U.6
E03 Claim: Health-insurance vocabulary with entity adjacency inside the window is limited to INA's "prepaid health care"/"INA Healthplan" print and the ERISA claim-administrator role; membership and PPO print **nowhere** in held bytes. — Date: 1979-1995 — Source: census this pass over CG04-CG07 + probes §3b-§4 — Source date: 2026-10-06 — URL: local — Archived: local — Tier: 1 — Class: FACT (of the byte-states) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High (of the searched shelves) — Corroboration: multiple files, one method — Conflicts: None
F01 Claim: The held bytes show the customer only as the company describes target groups, or as court records show adverse parties; no count of members/policyholders exists anywhere in the corpus. — Date: 1979/1989-1995 — Source: CG04 l.195-199; CG05-CG07 captions — Source date: 1979/1989-1995 — URL: local — Archived: local — Tier: 1 — Class: CONTEMPORANEOUS (both sides); counts UNKNOWN — Passage: "leading providers of life and specialty group coverages for businesses, professional societies, trade associations, and other groups" (re-joined) — Conf: Medium (print); High (of absence of counts in corpus) — Corroboration: 2 independent classes (self-report; judicial) for *existence of the roles only* — Conflicts: None
G01 Claim: INA's P&C loss reserves reached $2.9B at year-end 1979, and the company printed that reserves grew faster than earned premiums across 1975-79. — Date: 1979-12-31 — Source: CG04 l.750-762 — Source date: 1979 — URL: local — Archived: local — Tier: 1 — Class: CONTEMPORANEOUS (self-report, financial-statement-adjacent narrative) — Passage: "Property-casualty reserves for losses and loss adjustment expenses totaled $2.9 billion at year-end 1979" (re-joined) — Conf: Medium — Corroboration: 1 lineage — Conflicts: None
H01 Claim: The only in-window market-size byte is INA's own estimate of the US P&C industry: ~2,900 firms, ~$90B estimated 1979 premium volume. — Date: 1979 — Source: CG04 l.653-657 — Source date: 1979 — URL: local — Archived: local — Tier: 1 — Class: ESTIMATE-as-printed (company cite of an unsourced external estimate) — Passage: "approximately 2,900 firms which generated an estimated premium volume of $90 billion in 1979" (re-joined) — Conf: Medium (of the print) / Low (as market fact) — Corroboration: 0 independent (the estimator's source is not held) — Conflicts: None
K01 Claim: INA's 1979 consolidated set as printed: revenues $4,551M, net income $262M, assets $8,987M, equity $1,526M, 35,280 employees (1978 cells partially OCR-damaged; only clean cells carried). — Date: 1979-12-31 — Source: CG04 l.80-100 — Source date: 1979 — URL: local — Archived: local — Tier: 1 — Class: FACT (of the print); CONTEMPORANEOUS basis — Passage: NO_VERBATIM_PASSAGE_RECORDED (tabular digits) — Conf: Medium — Corroboration: 1 lineage — Conflicts: None
K02 Claim: P&C written premiums (GROSS/WRITTEN basis, not earned) reached $2.78B in 1979, +9% over $2.55B. — Date: 1979 — Source: CG04 l.675-676 — Source date: 1979 — URL: local — Archived: local — Tier: 1 — Class: CONTEMPORANEOUS (self-report) — Passage: "Written premiums reached $2.78 billion, 9% above the $2.55 billion of 1978." — Conf: Medium — Corroboration: 1 — Conflicts: None
K03 Claim: The combined ratio before policyholders' dividends was 101.8% in 1979 vs 99.8% in 1978, on INA's own mixed earned/written definition. — Date: 1979 — Source: CG04 l.742-747 — Source date: 1979 — URL: local — Archived: local — Tier: 1 — Class: CONTEMPORANEOUS (self-report; definition re-joined verbatim) — Passage: "before policyholders' dividends was 101.8% in 1979, against 99.8% in 1978" (re-joined) — Conf: Medium — Corroboration: 1 — Conflicts: None
L01 Claim: The window's independent witnesses — three SCOTUS-era records (1989, 1991, 1994-95) — validate structure and persistence of Line 1, not performance. — Date: 1989-1995 — Source: CG05, CG06, CG07 — Source date: 1989/1991/1995 — URL: local — Archived: local — Tier: 1 — Class: CONTEMPORANEOUS OBSERVATION — Passage: NO_VERBATIM_PASSAGE_RECORDED (see E01/E02) — Conf: High — Corroboration: 3 independent filings, but ONE document class (court papers) — Conflicts: None
M01 Claim: CIGNA CORPORATION is named as a respondent in a 1994-95 Supreme Court filing alongside CIGNA Individual Financial Services Company, CIGNA Securities, Inc. and an individual. — Date: 1994-95 — Source: CG07 l.19-30 — Source date: 1995 — URL: local — Archived: local — Tier: 1 — Class: FACT (caption) — Passage: "CIGNA INDIVIDUAL FINANCIAL SERVICES COMPANY, CIGNA CORPORATION; CIGNA SECURITIES, INC.; NICHOLAS DISETTE, Respondents." — Conf: High — Corroboration: 1 (the second naming of CIGNA Corp in the same doc is same-origin) — Conflicts: None
M02 Claim: A third-party government chronology records that on 1988-11-18 "US firm Cigna" sold its South African operations to local management — the corpus's one in-window CIGNA-line divestiture naming from outside the company. — Date: 1988-11-18 — Source: CIA Africa Review rdp88t00792 l.1174-1175 — Source date: 1988 — URL: local sources/periodicals/ — Archived: local — Tier: 2 (government compilation of press; not a CIGNA document; entity adjacency = "US firm Cigna", not a CIGNA byte) — Class: CONTEMPORANEOUS OBSERVATION — Passage: "US firm Cigna sells its South African operations to local management" (re-joined across l.1174-1175) — Conf: Medium-Low — Corroboration: 0 (no second witness in corpus) — Conflicts: None
N01 Claim: INA acquired HMO International in December 1978 via stock exchange, purchase accounting, self-assessed as not material to consolidated results. — Date: 1978-12 — Source: CG04 l.3676-3679 and l.3694-3709 — Source date: 1979 — URL: local — Archived: local — Tier: 1 — Class: FACT (of the note; contemporaneous) — Passage: "In December 1978, the Corporation acquired HMO International (HMO) through an exchange of stock and has accounted for the transaction as a purchase." — Conf: Medium-High (financial-statement note within a lineage otherwise capped Medium) — Corroboration: 1 lineage, two passages (same doc) — Conflicts: None
N02 Claim: The prepaid unit was renamed INA Healthplan in 1979 with Dallas headquarters and an initiated home-market plan. — Date: 1979 — Source: CG04 l.2006-2010 — Source date: 1979 — URL: local — Archived: local — Tier: 1 — Class: CONTEMPORANEOUS (self-report) — Passage: "During 1979, the prepaid health care business adopted the name INA Healthplan. The unit established headquarters in Dallas" (re-joined) — Conf: Medium — Corroboration: 1 — Conflicts: None
P01 Claim: Census facts this dossier relies on were re-measured on this pass: `1792` = 2 occurrences corpus-wide (both CG04 l.5, l.371); index rows 1,018; A4 96/12/81; EIN 82-4991898 present in s4 and the 2018-12-20 8-K. — Date: 2026-10-06 — Source: grep/wc over sources shelves; CG15; CG11 — Source date: 2026-10-06 — URL: local — Archived: local — Tier: internal measurement — Class: DERIVED — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High — Corroboration: reproducible single-command greps — Conflicts: U.5
Q01 Claim: The asserted 1982 CIGNA combination is carried as an unattested hypothesis: zero held bytes print it and zero lines pair `1982` with a merger/combination verb. — Date: 1982 (asserted) — Source: probe §4 census, inherited as measurement — Source date: 2026-10-06 — URL: local — Archived: local — Tier: internal measurement — Class: UNKNOWN (the event's attestation), FACT (of the census) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High (of unattestedness) — Corroboration: none — that is the point — Conflicts: U.3
S01 Claim: The second ancestor's claimed 1850s-1872 origin is UNTRIED, not null: its candidate names appear in no query this repository has ever run for this slug. — Date: — — Source: probe §4 (queries.json l.635-659), FR-7 — Source date: 2026-10-06 — URL: local — Archived: local — Tier: internal measurement — Class: UNKNOWN — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High (of the query-scope fact) — Corroboration: — — Conflicts: U.3

---

## UNTRIED (explicit list — never a null, per method rule 5 / §14.6)

STATUS: WRITTEN

Carried forward from the probe (this pass ran **0** retrieval calls; every route below is script-reachable and is a `FETCH REQUEST`, not an agent task):

1. **Family (a) for the predecessor registrant** — the 1979-1995 CIGNA Corporation CIK has never been indexed here. UNTRIED, 0 calls. **FR-1** (with the CIK-scoped write-path guard the probe specified).
2. **Family (b) web archives, entire** — no `sources/web_archive/`, no CDX attempt. UNTRIED, 0 calls. **FR-6**.
3. **Family (e) auction/museum/manuscript, entire** — Hagley / Historical Society of Pennsylvania class never asked. UNTRIED, 0 calls.
4. **Family (c) backlog** — 81 of 96 harvest candidate rows unmined as of this pass's re-read of A4 (probe saw 65 of 79; movement logged at §U.5), including the pre-1975 Connecticut General SCOTUS layers (CG14, pointers only, bytes unheld). **FR-4**.
5. **Family (c) Chronicling America** — endpoint CHALLENGED (7/7 shapes 403); a dead route, not a null; no CA zero citable. **FR-5**.
6. **Family (d) asked properly** — `corporate_print` tasks have never run facet-free and no creator task for `ina corporation` has ever existed; house organs/yearbook/directory classes never asked. **FR-4**.
7. **Ancestor 2 by name** — `Continental Life`, `Immigration Life`, `State Fidelity`, `Farmers and Merchants`: in no query task; the 1850s-1872 frame has never been put to any corpus. **FR-7**.
8. **NEW this pass — FR-8**: pre-1979 witnesses to the 1792 claim (centennial/history print about the Insurance Company of North America, HathiTrust/GB text class) so the U.2 self-report line can meet an outside witness; command form per PROBE_BRIEF_SHARED tooling: `python tools/periodical_harvest.py --company cigna --facet-free` plus an added query-block term `"insurance company of north america" AND mediatype:texts AND YEAR:[1792 TO 1979]`.
9. **Litigation depths** — merits/outcomes of CG05-CG07 records (only caption+structure pages were opened this pass). UNTRIED at page level.

---

## Register rows for merge — APPLIED TO THE NINE CSVs (merge pass, 2026-10-06)

STATUS: APPLIED

The author's nine fenced `csv` append blocks — 78 rows, `_parts/s1_p1.md` l.492–l.651 — were applied to the
nine register CSVs at this directory root, with the local `CG01–CG16` tags replaced by the minted ids
**S4407–S4422** per the map at the head of this file. They are not reproduced here: method §13 puts register
data in CSV, `_parts/` remains the emission of record, and a copy inside this volume would read to
`merge_census.py` as a second emission of the same rows.

| register | cols | data rows | words | bytes | what it holds |
|---|---|---|---|---|---|
| `sources.csv` | 18 | 16 | 872 | 9,346 | S4407–S4422; three SEC lineages collapsed (one S-4 lineage, one two-exhibit accession, one md5 duplicate), two internal-measurement carriers, three decoy rows, one pointer-only unheld family |
| `quantitative.csv` | 12 | 15 | 353 | 3,511 | the INA 1979 printed set (revenues 4,551 / net income 262 / assets 8,987 / equity 1,526 / 35,280 employees), written-premium 2,780 vs 2,550, combined ratio 101.8, reserves 2,900 and the earned-basis 111%, segment shares 66/18/12/4, the $90B industry ESTIMATE and one DERIVED share, plus the 1792 census row |
| `timeline.csv` | 11 | 14 | 441 | 4,241 | Line 1 (1792 RESTATED; 1957; 1969; 1978; 1979; 1988 naming and divestiture; 1989; 1991; 1994-95), Line 2 (1982 as hypothesis only), Line 3 (UNKNOWN incorporation; 2018-05-16 floor; 2018-12-20 closing) |
| `data_gaps.csv` | 8 | 12 | 404 | 3,381 | six High, four Medium, two Low; follow-up tasks cite FR-1…FR-7; the last row is the record-selection null named as a permanent deliverable, not a retrieval task |
| `conflicts.csv` | 15 | 6 | 424 | 3,606 | U.1–U.6, one row per declared anchor, 1:1 with §U.1–§U.6 |
| `failures.csv` | 11 | 6 | 223 | 2,139 | 101.8 combined ratio; the $84.8M 1978 losses; reserves outgrowing earned premiums 96→111%; the 5%-of-income parent-and-other loss; goodwill write-downs; three appearances as litigation respondent |
| `validation.csv` | 11 | 4 | 150 | 1,503 | health pre-tax +48%; the buy-a-plan pattern repeated inside a year; three independent court records naming the structure; the 2018 indenture designation (firewall-tagged, not an in-window signal) |
| `decisions.csv` | 15 | 3 | 173 | 1,715 | HMO International stock-exchange acquisition (1978-12); the 1979 prepaid expansion mix; the 1979 underwriting posture, confidence split "Low as a decision-as-decision / Medium as print" |
| `channels.csv` | 11 | 2 | 90 | 908 | acquire-then-brand the prepaid channel; hospital management contracts (asset-light), both self-printed and externally unverified |

**78 requested = 78 applied; 0 unapplied rows; 0 rows added by the merge; 0 rows folded.** The per-register
account, the validation/failures adjudication, the census readings before and after, and the id allocation are
recorded in `03_quality_control/cigna_s1_merge.md`.
