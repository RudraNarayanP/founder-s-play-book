# FORENSIC LONGITUDINAL DATASET — AT&T, STAGE 1 (1875-01-01 → 1915-12-31)

**Company:** Fortune rank 35, `company_035_att`. The brand answers to **two registrants and one non-registrant ancestor**; the ticker `T` answers to only one of them. Read §Header 1 before any sentence of narrative.
**File:** Stage 1, **part 1 of 1 at this tier** — Header, Stage boundary, sections **A–U**, the load-bearing claim records (appended under each section, per method §7 and the T2 rule), and the nine register emission blocks. No part 2 or 3 is planned for this stage; if the merge splits it, section letters, claim IDs, metric IDs and `U.nn` anchors continue, they are never renumbered (method §9.3). Cross-references of the form `(AT&T S1 §K, this part)` name this volume.
**Probe inherited:** `research/A_chronology_feasibility.md` (agent `probe-att`, 0-web pass) — its tier verdict, five-family verdict, registrant map and `## Untried` list are this part's scope. Its `research/A4_harvest_mine.md` is read and superseded **for label-count purposes only** at §Header 4 and §T.3.
**Format exemplar:** `company_001_amazon/` — shape only. No Amazon value, date or phrasing is imported anywhere in this file.

---

## MERGE RECORD (assembly, application, id map, adjudication, parity, carry-forward)

Merged 2026-10-07 by `merge-att` from the single part `_parts/s1_p1.md` (author `s1-att-p1`; **36,595 words** as
emitted, 24 `STATUS: WRITTEN` markers and 0 PENDING, **56 claim records**, **9 anchors `U.1–U.9`**, **136 register
rows in 9 fenced blocks**). This volume measures 31,315 words and stays **one volume**: the emission exceeds the T2
planning figure (22,000/stage) but sits far inside method §9.2's 60,000-word hard cap, so §9.3 does not bite, no
split is required, and nothing was trimmed to make a number (RD-122: a tier cap is a **density target**, not a file
limit; §9.6 forbids cutting evidence to fit one). **Section letters, the four-person labels `P1`–`P4`, the claim
record ids (`BD01–BD04`, `A01`…`U01`), the §P metric ids (`P01`–`P50`, including `P14`) and the anchors `U.1–U.9` are
the author's and were not renumbered** (method §9.3 — numbering continues, it is never re-based). `_parts/` is
read-only to this pass and stays the emission of record; no `SUPERSEDED` footer was added, because nothing in it was
found to be wrong by the merge.

**What was moved out of the prose.** The part's nine fenced `csv` register blocks (8,067 words of register data) are
data, not narrative (method §13): they were **applied** to the nine CSVs at this directory root and the body's
`## Registers` section now records that application instead of repeating the blocks. Their verbatim text survives at
`_parts/s1_p1.md` l.908–l.1096. **Claim records are narrative**: all 56 appear below, unchanged.

**Register application: 136 requested = 136 applied, 0 withheld, 0 added by the merge, 0 folded.** Headers are
byte-identical to the `company_001_amazon/` conformant headers (compared by string equality before writing); `stage`
is the literal `stage1` on all 136 rows; widths are 18/12/11/15/11/11/11/15/8 with **0 rows off header width**;
**0 exact duplicate rows across the nine registers**; and the two keyed registers are unique — 14 `source_id`s, 9
`conflict_id`s. Per-register counts and the census readings are in
`03_quality_control/att_s1_merge.md`; the row-by-row account is repeated at the foot of this file.

**Provisional-to-global id map — the only place `P1S01–P1S14` bind.** Minted centrally with
`python tools/id_mint.py --count 14 --company company_035_att --claim --agent merge-att` → **S4449 … S4462**,
allocated above the highest live id (`--audit` at mint time: 351 distinct issued ids in range `S0001`–`S4430`, plus
registry claims held through `S4448` by `company_006_cvs`; the tool's own `next assignable: S4449`), so no gap is
re-entered and no number another company holds is reused. Every `P1Snn` token in every applied register cell was replaced by its minted
id, **including inside prose cells** (`claim_a_source`, `claim_b_source`, `best_available_evidence`, `notes`); the
narrative below keeps the author's local tags and is keyed by this table. The local tags also survive inside each
`sources.csv` `notes` cell as protected history, marked `COR-01`.

| local | minted | carrier (person · what it holds) |
|---|---|---|
| `P1S01` | **S4449** | P2 — Annual Report of the Directors for FY1913, New York 1914 (136,506 B / 5,631 lines): the spine of Stage 1 |
| `P1S02` | **S4450** | P2 — Report of a Conference Held … September 7, 8 and 9, 1887, "PRINTED, NOT PUBLISHED" (334,305 B / 8,784 lines) |
| `P1S03` | **S4451** | third party, hostile — Johnston, *Some Comments on the 1907 Annual Report…* (IITA, Chicago, 1908-09; 60,341 B / 1,390 lines) |
| `P1S04` | **S4452** | P2 — AT&T (CIK 0000005907) Form 10-K FY1993, acc. 0000005907-94-000008: **the only filed sentence for the 1885 New York incorporation, labelled RESTATED** |
| `P1S05` | **S4453** | P4 — Southwestern Bell (CIK 0000732717) Form 10-K FY1993, acc. 0000732717-94-000005: the 1983 Delaware / 1984-01-01 recital |
| `P1S06` | **S4454** | P4 — SBC Form 10-K405 FY1994, acc. 0000732717-95-000003 (same lineage as S4453/S4455, never a second witness) |
| `P1S07` | **S4455** | P4 — SBC Form 10-K FY1999, acc. 0000732717-00-000018 (the Bell operating-company family list) |
| `P1S08` | **S4456** | P4 — SBC Form S-4 / POS AM for the AT&T Corp exchange offer, d24647posam.htm, 2005-05-03 |
| `P1S09` | **S4457** | SBC filer / AT&T CORP subject — Form 425 SGML, acc. 0001047469-05-002185: **both registrants' identities printed in one header** |
| `P1S10` | **S4458** | P4 — Form 425 investor letter d425.htm, 2005-01-31: the "sharing a legacy" sentence, cited only as the object of the firewall refusal |
| `P1S11` | **S4459** | **NOT EVIDENCE — a measurement of the archive's reach**: quarantined submissions index for CIK 0000005907, 1,255 filing rows, perimeter 1994-01-07 → 2007-01-18 |
| `P1S12` | **S4460** | **NOT EVIDENCE — perimeter measurement**: index + registrant record for CIK 0000732717, 7,922 filing rows, 1994-02-14 → 2026-10-02, former names SBC COMMUNICATIONS INC / SOUTHWESTERN BELL CORP |
| `P1S13` | **S4461** | `research/A_chronology_feasibility.md` (agent `probe-att`) — a dossier pointer page, tier 4, not a witness |
| `P1S14` | **S4462** | the DTIC `ADA189269 / ADA189360 / ADA197243` layers — **negative artefact** (decoy shelf), cited to demonstrate the bare-`att` token trap |

**The `validation.csv` / `failures.csv` adjudication (the census cannot decide; the merge did, by reading).** The two
registers share a **byte-identical 11-column header**, so `merge_census.py` printed the 7-row and 10-row groups as
`AMBIGUOUS:validation.csv,failures.csv`. Binding rules applied, in order: (1) **declared target** — each
`>>> REGISTER ROWS FOR MERGE <<<` marker names its target, and `NOTES_att_p1.md` §5 states validation **7** ·
failures **10**, which is exactly what the two blocks parse to; (2) **counts close** — 7 + 10 = 17 = the rows the
census listed as unattributed, and no row appears in both groups; (3) **content, row by row** against Amazon's
conformant usage (`validation` = a signal that validated something; `failures` = an incurred adverse signal): the
7-row group's `what_it_demonstrated` cells are all positive validations (the 1912 and 1913 underground conversations,
the 1913-12-19 acceptance by the Administration, the shareholder count rising to 55,983, station and wire-mile growth,
the ten-of-eleven cross-foots, the asserted self-financing capacity); the 10-row group's are all incurred negatives
(the defective tinsel-braid cable, lead-sheath corrosion, the Boston Phillips/Clark cable failures, the 1883
1,500-foot ceiling, the 1905 receivership, the Central Union consent to receivers, the fall in surplus earnings to
11,735,194, the independent wave's own collapse, the loud-speaking promotions, the asserted wholesale obsolescence).
**No row was moved between registers, and no row was split.** The binding is printed in the `notes` cell of the last
row of each block and in `CORRECTIONS.md` as **COR-02**. (Recorded as a tool finding, not repaired here: the content
hints the census printed for these two groups were the *decisions* block's rows, because `merge_census.py` calls
`hint_validation_or_failures(data)` before `data` is assigned in that branch — the hints for this company are a stale
variable, so the adjudication was made from the block text itself.)

**Four legal persons, preserved rather than tidied.** §Header 1's table (P1 Bell Telephone Company / American Bell —
never a registrant reachable from this directory; P2 = **CIK 5907**, New York, 1885; P3 = the seven 1983–84 RHCs;
P4 = **CIK 732717**, Delaware 1983 → SBC → AT&T Inc, the ticker's registrant) is the author's and stands as written,
and every section's first line still names the person it describes. Three specific protections are verifiable in the
register layer, not just in the prose: (a) the 1885 answer is **S4452** — P2's own FY1993 10-K l.238 — and is
labelled **RESTATED** in its `evidence_class` cell, so it can never be read as an in-window document or attached to
CIK 732717, whose origin rows are S4453/S4454/S4456 and are labelled as the 1983 line; (b) the quarantined 5907 index
is registered as **"NOT EVIDENCE — a measurement of the archive's reach"** with its perimeter (S4459, and S4460 for
the 732717 side), and that framing — not a filing, not an absence — is what the rows carry; (c) **1915 stays in the
future tense**: S4449 l.400–402 is design evidence, the timeline row for 1915 reads
`CONTEMPORANEOUS as DESIGN; event UNKNOWN`, and the author's new finding that the layer's **second** `1915` hit at
l.5091 is a 1914→1915 stock-payable maturity ("Indebtedness to Western Union Telegraph Co. for New York Telephone Co.
Stock Payable 1914 to 1915 … 4,000,000.00"), not an opening, is carried in §Boundary 2 and §U.6's claim B. The two
out-of-window P4 rows (1983, 1984-01-01) are kept in the Stage-1 `timeline.csv` explicitly marked `OUT OF WINDOW` so
no later pass can place them silently in the ticker's registrant's infancy.

**Anchor parity: 9 narrative anchors ↔ 9 register anchors, 1:1, 0 residue in either direction.** §U declares
`<!-- ANCHORS: U.1-U.9 -->` and writes §U.1–§U.9 below; `conflicts.csv` holds exactly nine rows keyed `U.1 … U.9`, and
the anchors are cited from the `timeline.csv` `conflict_ref` column (12 of the 28 rows), the `quantitative.csv` notes
(`P14` → U.5) and the `data_gaps.csv` / `failures.csv` cells. Measured twice: by `gates.py --checks anchors` and by
scanning every `U.nnn` token across all nine registers against the declared set.

**Retractions and bindings issued by this pass** (`CORRECTIONS.md`): **COR-01** the dossier-local source keys are
superseded by the minted ids (the local tags survive only as aliases in the table above and in each `sources.csv`
`notes` cell); **COR-02** the two schema-identical blocks are bound, 7 rows → `validation.csv`, 10 rows →
`failures.csv`, by the content adjudication above; **COR-03** the probe's label counts and periodical-shelf byte
total are superseded by this part's re-measurements (`ATT-S1-C1/C2/C5`, and the second `1915` hit); **COR-04** the
1885 recital belongs to CIK 0000005907 (P2) and is never attachable to CIK 0000732717 (P4), and the quarantined 5907
index stays NOT EVIDENCE. Each is referenced in the register layer and in this volume.

**The tier, as issued and as measured, is not re-tiered here.** The probe issues **Stage 1 = T2 core, PROVISIONAL**
(22k words/stage, 6–9 runs) and §Header 2 keeps both of its re-grades open ((c) folded into (d) makes T3; admitting
the 1994 recital as an origin answer makes T1). The budget check for this volume was run as
`gates.py --tier core`, and that is stated rather than hidden: the auto reader resolves the tier from a
**verdict-bearing line** in `research/*.md`, and this probe states its per-stage tiers **as table rows**, so it had no
verdict line to read (measured on this company: `tier: T2 … 13 mentions, 0 on a verdict line` — it lands on T2 here
only through the mention tie-break, the same path that printed **T3** for Cigna's probe on the same tool). Pinned
explicitly, the 22,000-word target is unambiguous and identical either way. Against that target the merged volume is over, and `gates.py` now classifies that as
`advisory` ("NOT a split mandate and NOT a defect"), which is exactly the status of the overage in this dossier. No
prose was edited to satisfy the tool.

**Five families as the part carried them** (the merge re-measures nothing that it did not retrieve; (b) and (e) are
**UNTRIED for lack of any route**, not nulls):

| family | verdict carried | what it delivered for Stage 1 |
|---|---|---|
| (a) SEC / EDGAR | **TRIED–ANSWERED** (bytes on disk; the authoring pass ran 0 retrieval) | the 1885 recital (S4452) and the 1983/1984 recital (S4453–S4456); two measured perimeters; **no in-window document** |
| (b) web archives / CDX | **UNTRIED — there is no route to scope it**: `tools/web_domains.json` cites no domain for `att` (`slugs` = centene, cencora, relevance, marathon, microsoft, target) | nothing; the ask is a cited domain, not a guess (§S UNTRIED 1) |
| (c) periodical corpora | **TRIED–ANSWERED, thin** — one opened third-party carrier (S4451), which is hostile print; the name-discovery re-runs are TRIED–UNANSWERED | 1894 patent expiry, the independent wave, Western Electric 1907 pricing, the Columbus/Central Union rate and failure record |
| (d) digitised corporate print | **TRIED–ANSWERED — the strongest family**, two opened carriers of P2's own print | everything in §E, §J, §K, §L, §M, §N, §P; the 1915 design statement; the 1877 apparatus epoch |
| (e) auction / museum / manuscript | **UNTRIED and UNIMPLEMENTED — no tool exists in `tools/*.py`** | nothing; and the three documents Stage 1 most needs are all here (§S R-5) |

**Not applied, not attempted, and why.** (1) **§T.4's periodical-shelf byte total** — the volume prints **660,753 B**,
which `NOTES_att_p1.md` §2 supersedes at **707,735 B** over the same six layers. The merge did not rewrite it: §14
rule 4 bars a merge from silently re-issuing another pass's numbers, so the supersession is carried as **COR-03** and
handed to the audit pass. This is the only figure in the volume the merge knows to be stale, and it is named here
rather than fixed in place. (2) **`S6-11` is left as print, not re-pointed.** It is the DTIC document code
`S6-11-25-ATT`, quoted in §Header 1 and §T.6 as the demonstration that a bare `att` token is a substring of somebody
else's code; `gates.py --checks keys` reads it as a hyphenated record key and prints it as a review note, and the
correct answer is to leave the quotation alone — minting a source row or a register key for a document code is the
RD-131 mistake the tool exists to prevent. (3) **The five FETCH REQUEST blocks (R-1…R-5) and the probe's standing
asks were not run**: they are the orchestrator's dispatch list, this pass had a 0 web budget, and §14 rule 6 keeps
each untried route named rather than reported empty. (4) **Nothing was de-duplicated by deletion**, nothing was
moved, renamed or merged away, no register row was invented to fill an empty shape, and the two unresolvable
`claim_ref` cells named in the application table above were left verbatim rather than rewritten. (5) The merge **did not
audit and does not certify**: the five §14-class judgment calls (the (c)/(d) family count, the U.6 motive reading,
the U.9 attribution, the 1984 "birth vs amputation" direction, the tier) belong to the audit and certifier passes
behind this one.

**What this pass did not examine:** the 26 stored SEC documents under `sources/sec/` that Stage 1 does not cite, the
three DTIC layers beyond counting them as decoys, every sibling company, `MASTER_RESEARCH_LOG.md`, and `tools/`
except as the four commands bound to run (`merge_census`, `id_mint`, `scaffold`, `gates`).

---


## Header

STATUS: WRITTEN 2026-10-06 (agent `s1-att-p1`; every passage quoted here was opened in this session and its line locator re-measured here)

### 1. The registrant problem, stated before the narrative

Four legal persons have carried "Bell" / "American Telephone & Telegraph" / "AT&T" inside the span this dossier covers and after. **Every section below names the person it describes**, and §U registers the conflicts this produces rather than smoothing them.

| key | legal person | status in Stage 1 | is it the registrant today? | held carrier (file · line locator) |
|---|---|---|---|---|
| **P1** | **Bell Telephone Company (1877) → American Bell Telephone Company (1880)** | the operating ancestor of the art; **never a registrant under either CIK reachable from this directory**; no held document names its organisation | **No** | `sources/periodicals/report-of-a-conference…djvu.txt` l.332-333, l.353-354, l.7069-7073 — AT&T's own 1887 print lists officers **of a different company** ("W. W. JACQUES, Electrician, American Bell Telephone Company"; "in 1883 the American Bell Telephone Company laid a number of cables … afterwards being turned over to the New England Company") |
| **P2** | **American Telephone and Telegraph Company — a New York corporation, incorporated 1885** (EDGAR conformed `AT&T CORP`, **CIK 0000005907**, former conformed name `AMERICAN TELEPHONE & TELEGRAPH CO`, name change dated 1992-07-03, IRS 13-4924710, SEC file no. 001-01105) | **the subject of almost all of Stage 1**: its own 1887 print and its own FY1913 annual report are the in-window Tier-1 carriers | No — its EDGAR perimeter ends 2007-01-18 | `sources/sec/0000005907-94-000008_…txt` **l.238** ("incorporated in 1885 under the laws of the State of New York"); header l.22; `…djvu.txt` (the 1913 report) l.11, l.1245-1247 |
| **P3** | **the seven regional holding companies created in 1983 and divested 1984-01-01** | **outside Stage 1.** Named here only because 1984 is where the record creates a *new* registrant and stops describing P2's business | No, except through P4 | `0000732717-94-000005…txt` l.210-213; `0000005907-94-000008…txt` l.1121, l.6640 |
| **P4** | **Southwestern Bell Corporation (Delaware, 1983) → SBC Communications Inc (1992-07-03) → AT&T Inc (CIK 0000732717, ticker `T`)** | **does not exist at any date inside Stage 1.** It answers for rank 35 today and for Stage-2/3 money | **Yes — the ticker's registrant** | `0000732717-94-000005…txt` l.22 (`COMPANY CONFORMED NAME: SOUTHWESTERN BELL CORP`), l.210-213; `0000732717-95-000003…txt` l.151; `0000732717-00-000018…txt` l.226 |

**The answer to "which CIK", in one line.** CIK **0000005907** (P2, New York, incorporated 1885) is the registrant that carries the 1885–1984 brand history; CIK **0000732717** (P4, Delaware, 1983, ticker `T`) is the registrant that answers for Fortune rank 35 now. **No Stage-1 sentence about 1885, 1887 or 1913 is attributable to 732717**, and no 1983/1984 recital of 732717 is attributable to the 1885 line. §U.1, §U.2, §U.7 hold the conflicts this creates.

**A quarantined index is a fact about our tooling, not an absence of filings.** `index --cik 5907` measured P2's real perimeter — **1,255 filing rows, 1994-01-07 → 2007-01-18, earliest 10-K row 1994-03-25** — and then the identity guard wrote the artefacts to `sources/_index/quarantine/CIK0000005907/` because this directory already holds a canonical index for 732717. Nothing was clobbered; no `--allow-mismatch` was used. **It is not a null, and it is not evidence either**: a search-index row or a guard verdict is not a witness (method §15.1), which is why every P2 fact in this dossier is carried by a stored document read at a line, not by the index. See §T.4.

**Name-greping discipline (measured this pass, not inherited).** Two detector traps are live on this corpus.
* **Bare `att` is noise.** The three `DTIC_ADA*` layers on this shelf match `att` as a substring of a document code and of a trademark (`S6-11-25-ATT`, "AT&T UNIX Ada"), and one of them validates **another vendor's** compiler. `att` is used here only with entity adjacency (`American\s+Telephone`, `American Bell`, `Bell Telephone Company`), never bare.
* **OCR whitespace hides the registrant's own name from a single-space grep.** Re-measured this pass, case-sensitive, over the joined-line rendering of each held layer: in the FY1913 report `American Telephone` (single space) = **0**, `American\s+Telephone` = **29** case-sensitive / **35** case-insensitive, `American\s+Telephone\s+and\s+Telegraph\s+Company` = **20** / **25**; in the 1887 conference report `American\s+Telephone` = **2**, `"American Bell"` = **3**; in the 1908 pamphlet `American\s+Telephone` = **4**. **The probe's `35` is the case-insensitive count of the same pattern**; both numbers are recorded here so a later pass does not "discover" the discrepancy (§Header 4). The company's own report prints its name `AMERICAN  TELEPHONE  AND  TELEGRAPH  COMPANY`, double-spaced, so a single-space name phrase greps **0 against the registrant's own title page** — the mine's `VARIANT_TERM_HIT` label on AT&T's own annual report is an artefact of the grep, not a judgment about the document.

### 2. Stage definition, span, and tier

**Stage:** 1 of 3 (origin). **Span proposed and adopted:** **1875-01-01 → 1915-12-31.**
**Stage definition (method §1, adapted to a regulated network utility):** the window in which the telephone art acquires its first operating company, in which the registrant that will carry the brand is created for a specific engineering purpose (long-lines), and in which that registrant's own print first states — as *design* — the transcontinental intention that the legend later reports as an *event*. It is **not** "the founding story of the company that trades today"; that company is P4 and is not born until 1983.
**Tier:** **T2 core — PROVISIONAL**, 22k words/stage, 6–9 runs, inherited from the probe and **not re-tiered here** (method: if you disagree with a tier, log it, do not silently re-tier). Two families are firm in-window — **(d) digitised corporate print** (two opened carriers of P2's own print) and, thinly, **(c) periodicals** (one third-party carrier). The probe states both re-grades and this pass does not move them: (c) can be folded into (d) by an auditor, which makes Stage 1 **T3**; a 1994 recital can be admitted as the answer to an origin question, which makes it **T1**. §S records which fetches would decide it.

### 3. Hindsight firewall and record-selection null

**Firewall (§2).** Nothing here treats the later size of the Bell System, the 1984 divestiture, the 2005 re-acquisition, or today's `T` as evidence that any 1885–1915 decision was rational, that the independents were doomed, that government ownership was unrealistic, or that a transcontinental line was inevitable. Two specific contaminations are refused by name:
* the acquirer's own 2005 sentence — "SBC and AT&T are a potent combination, **sharing a legacy** of innovation, integrity and reliability" (`0001193125-05-015481_d425.htm` l.42-44, an investor letter, out-of-window, marketing instrument, P4's voice) — is **evidence of a 2005 claim about a brand**, recorded at §U.7, and is not used anywhere as evidence about 1885–1915;
* the 1915 transcontinental opening, which **no held in-window byte reports as having happened**, is not narrated in the past tense anywhere in this file (§D.4, §U.3).
Anti-hagiography test applied per §2 to every coda: each is written to still read as plausible if P2 had been broken up by the ICC valuation, or if the 1914 year had ended in receivership.

**Record-selection null (§2, stated in §A and §S).** What is unrecoverable *because the survivor's archive is the one that was kept*: every in-window figure in §P and §K is **the company's own print about its own system** — there is **no independent count behind any of it** in this corpus (no auditor's report, no regulator's return, no competitor's data for the same metric). The FY1907 report is **not held** (the 1908 pamphlet quotes it; the quotation is a derivative carrier of a document we do not have). The 1899/1900 transfer of the Bell System parentage from American Bell to P2 — the single most consequential legal event of the window for the brand question — **has no carrier on this shelf at all** (§S G-3). P1's 1877 organisation papers, P2's 1885 New York certificate of incorporation, and the patent-litigation record are reachable only through family (e), which is unimplemented here (§T.5). And the 1887 conference report's own imprint line, **"PRINTED, NOT PUBLISHED"** (l.15), is a fact about what survived: a house document kept because the company kept it.

### 4. Corrections taken on this pass, before anything is inherited

| id | inherited statement | this pass's measurement | effect |
|---|---|---|---|
| **ATT-S1-C1** | probe §3.4 table: FY1913 layer `American\s+Telephone` = **35** | **29** case-sensitive; **35** only case-insensitively; single-space literal **0** both ways | both numbers are printed in §Header 1 so neither is silently propagated; the finding (single-space greps miss the registrant's own name) is **unchanged** |
| **ATT-S1-C2** | probe §4 counts measured "over all 37 stored files": `1984` **74**, `Bell Telephone Company` **47**, `Southwestern Bell` **566**, `1885` **1**, `1877` **0** | re-measured **this pass over the 7 documents this part actually cites**: `1984` **40**, `1885` **1**, `Bell Telephone Company` **32**, `Southwestern Bell` **207**, `American Telephone and Telegraph` **7**; `1875` `1876` `1877` `1894` `1895` `1915` `transcontinental` `Alexander Graham Bell` `American Bell` all **0** | the zeros are the load-bearing findings and they survive at the smaller denominator; §P and §S cite **this pass's** numbers as this pass's measurement and the probe's as inherited |
| **ATT-S1-C3** | probe §2 "P4 … 1983 → present", and the divestiture date | verified independently at the bytes: `0000732717-94-000005` l.210-213 prints both the 1983 Delaware incorporation "**by AT&T** as one of seven regional holding companies" and the spin-off "**on January 1, 1984**" | no change; recorded as re-verified, not inherited |
| **ATT-S1-C4** | `somecommentsona00chicgoog` is a third-party carrier naming P2 | verified: it is a **hostile trade-association** carrier — Gansey R. Johnston, General Manager, The Columbus Citizens Telephone Company, published by the **International Independent Telephone Association**, Chicago, September 1908 (l.114-159) | strengthens §I and §C; narrows what it can carry about P2 (its extracts *from* the 1907 report are quotations in a hostile frame, and the 1907 report itself is not held) |

### 5. Confidence scale, transport cap, and conventions

**Confidence (§3):** **High** = a primary document speaking of its own year, or 2+ independent origins. **Medium** = one reliable source, or a retrospective-only primary. **Low** = conflicting, vague, or retrospective-only with no primary carrier. **UNKNOWN** = a finding, not a gap to fill.
**Transport cap (inherited and enforced).** All six `sources/periodicals/*.meta.json` sidecars carry `"transport": "UNVERIFIED TLS -- re-check before citing at High confidence"`. **Therefore no quotation from a periodical layer is offered above Medium in this file**, including the two carriers that make Stage-1 Tier-2 possible; this is the binding reason §K and §P rows read Medium even where the print is internally cross-footed. The SEC-sidecar documents (`sources/sec/*.meta.json`, fields `accession/cik/registrant/fetched/http_status/sha1/url/words`) carry **no** such caveat and are cited at High where a document speaks of itself.
**OCR transcription convention.** Multi-space runs inside a quotation are rendered with single spaces; stray OCR periods and the letter-substitutions of the scan ("Telegrah", "jpoo", "Beil", "(887") are reproduced **as printed** where quoted, and are never silently corrected. Where a word is uncertain the reader is told, because §14.10 makes a tidied quotation a defect.
**Citation convention (§14.12).** Claims are addressed by stable label — `§P K-07`, `U.3`, `P1S04`, a claim record id. **Line numbers are locators only** and are stated as `l.238 (locator)`; a repair pass that edits this file invalidates them, not the claim.
**Person labels.** `P1`/`P2`/`P3`/`P4` as in §Header 1. A section that describes P2 says so in its first line.
**Basis labels on every number.** `SYSTEM` = "Bell Telephone System in United States … all duplications … excluded" (a stated basis, not a company); `COMPANY` = the American Telephone and Telegraph Company's own account; `DERIVED` = arithmetic shown in the row; `ESTIMATE` = the company's own forward figure for 1914. Fiscal vs calendar, nominal vs current, is stated in each row (§6).

---

## Boundary

STATUS: WRITTEN 2026-10-06

### 1. Opening edge — 1875, and what it is not

The floor is **proposed, generous, and not evidenced as a founding.** The earliest dates any held byte prints as an epoch are **1877** and **1876**, and both belong to P2's own FY1913 report: "From the year 1877 to the present time improvements have followed each other with remarkable rapidity" and "During the thirty-seven years from 1877 to 1914 there were designed and constructed and installed fifty-three improved types and styles of telephone receiver, and seventy-three types and styles of transmitter" (`P1S01` l.1364-1372) — 1877 as the **opening of an apparatus-development period**; and the diagram "SHOWING THE GROWTH IN SUBSCRIBERS' STATIONS CONNECTED TO THE SYSTEM OF THE BELL TELEPHONE COMPANIES FROM **JAN. 1, 1876— JAN. 1, 1914**" (l.5485-5506, chart axis l.5552 with the tick 1894) — 1876 as a **statistical baseline**. Neither is an incorporation. **`1875` occurs 0 times in every held layer and 0 times in the 7 cited SEC documents** (measured this pass). The floor is set at 1875 to leave room for the patent-litigation era that the record here cannot reach, and is labelled for what it is: a **search boundary**, not a claim. **If the orchestrator prefers an evidenced floor, 1876-01-01 is the earliest date any held byte prints** — and 1887-09-07 is the date of the earliest held *document*.

### 2. Closing edge — 1915, carried only as design

The ceiling is evidenced by exactly one line, and evidenced **in the future tense**: "It is easier to talk with Denver to-day than with Chicago then, and **with the completion of the line to the Pacific Coast in 1915**, commercial communication **will be** dependable and practicable" (`P1S01` l.398-402). A report for FY1913 printed in 1914 cannot witness a 1915 demonstration; it can date an intention. The closing year is therefore drawn at the date the registrant's own print projects, **and Stage 1 is closed at 1915-12-31 with the validating event recorded as UNKNOWN** (§D.4, §U.3). `1915` occurs **2** times in the held 1913 layer: l.400 (the projection) and l.5091 ("Indebtedness to Western Union Telegraph Co. for New York Telephone Co. Stock Payable 1914 to 1915 … 4,000,000.00", a liability falling due across the new year — a *maturity*, not an opening).

### 3. Where the record creates a new registrant, and why that is not here

**1984-01-01 is the date the registrant count changes, and it is in Stage 3, not Stage 1.** P4's own FY1993 10-K prints the creation and the separation in two consecutive sentences (l.210-213): "The Corporation was incorporated under the laws of the State of Delaware in 1983 **by AT&T** as one of seven regional holding companies (RHCs) formed to hold AT&T's local telephone companies. **AT&T divested the Corporation by means of a spin-off of stock to its shareowners on January 1, 1984** (divestiture). The divestiture was made pursuant to a consent decree, referred to as the Modification of Final Judgment (MFJ)…" — and P2's own FY1993 10-K speaks of the same event from the other side: facilities "**leased from the regional holding companies created at divestiture**" (l.1121) and reimbursements under the "**Divestiture Plan of Reorganization**" (l.6640). **One event, two directions, two persons**: a birth for P4 and an amputation for P2 (§U.4). Nothing in Stage 1's window belongs to P4; the 1885→2005 line and the 1983→present line are written as separate registrants throughout.

### 4. What this boundary does NOT claim

(i) Not that AT&T was "founded in 1877"; no held byte makes 1877 an act of either registrant (§U.2). (ii) Not that 1875 is evidenced at all — it is a boundary, and it prints 0. (iii) Not that the 1895 "first transcontinental experiment" happened: `transcontinental` = **0** in every held byte, and all three `1895` occurrences in the 1913 layer are the **first column of a statistical series** (l.978, l.1031, l.1043) (§U.3). (iv) Not that 1915 validated anything: it is carried only as a projection (§2 above). (v) Not that the FY1913 numbers describe the company that trades today: they are P2's, and P4 did not exist (§Header 1). (vi) Not that the `1885-01-01 → 1984-12-31` window in `harvest_mine.py` / `sources/sec/_RUN.json` is a founding span: it is a **search setting**, and EDGAR's floor for **both** registrants is 1994 (P2's perimeter measured at 1994-01-07; P4's at 1994-02-14) — the in-window zero is a measured perimeter, not a finding of absence.

### 5. Knowability across the boundary (§7)

| Item | Verdict | Carrier or named route |
|---|---|---|
| P2 exists as a New York corporation in 1885 | **KNOWABLE, carried out-of-window** | `P1S04` l.238 — the registrant's own FY1993 10-K; in-window print of 1885 is **cable dates, not incorporation** (§C.2) |
| P1's 1877 organisation, and who did it | **NOT KNOWABLE at this reach** | no held document; family (e) unimplemented; `birthbabyhoodoft00wats` (1940) FETCH REQUEST §S-R1 |
| Whether P2 was created *for* long lines | **NOT KNOWABLE from held bytes** — the 1913 print shows P2 owning long-distance plant, which is consistent but not the charter purpose | `P1S01` l.5039 "Long-Distance Telephone Plant … 49,269,173.30"; the 1885 certificate is the carrier and is not held |
| The 1899/1900 parentage transfer from P1 to P2 | **UNKNOWN, no carrier** | §S G-3; the strongest indirect in-window evidence is P2's own asset mix (§K.2) |
| A 1915 transcontinental opening | **UNKNOWN as event; CARRIED as design** | `P1S01` l.400-402; `2xVAAAAAYAAJ` (1915) and `j4BbAAAAMAAJ` (1914) FETCH REQUESTS §S-R2 |
| Anything about P4 inside this window | **NOT KNOWABLE — P4 did not exist** | `P1S05` l.210 is the carrier of its absence-in-window, 1994 |

### Claim records (§Boundary)

BD01 Claim: Stage 1 is drawn 1875-01-01 → 1915-12-31, the floor generous by at least one year to the earliest date any held byte prints. — Date: 1875-01-01 — Source: `research/A_chronology_feasibility.md` §5 tier table (probe proposal, adopted here) — Source date: 2026-10-06 — URL: file-local `founders_playbook/01_companies/company_035_att/research/A_chronology_feasibility.md` — Archived: — — Tier: 4 (dossier pointer, not evidence) — Class: INFERENCE — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High (that the floor is unevidenced) — Corroboration: 1 independent (this pass's own token counts) — Conflicts: U.2

BD02 Claim: The closing year is carried by P2's own FY1913 report **in the future tense**. — Date: 1914 (print) projecting 1915-12-31 — Source: Annual Report of the Directors of American Telephone and Telegraph Company for the year ending December 31, 1913, New York, 1914 (P1S01) — Source date: 1914 — URL: https://archive.org/download/annualreportofdi00amer_14/annualreportofdi00amer_14_djvu.txt — Archived: — — Tier: 1 (company's own annual report; transport caveat caps it) — Class: CONTEMPORANEOUS OBSERVATION (as to design) / UNKNOWN (as to event) — Passage: "with the completion of the line to the Pacific Coast in 1915, commercial communication will be dependable and practicable" — Conf: Medium — Corroboration: 1 independent — Conflicts: U.3

BD03 Claim: The 1887 conference report is the earliest held document, and 1876 is the earliest date printed anywhere. — Date: 1887-09-07..09 — Source: Report of a Conference Held at the Office of the American Telephone and Telegraph Company, 18 Courtlandt Street, New York (P1S02) — Source date: 1887 — URL: https://archive.org/download/report-of-a-conference-held-at-the-office-of-the-american-telephone-and-telegraph-company/Report%20of%20a%20conference%20held%20at%20the%20office%20of%20the%20American%20Telephone%20and%20Telegraph%20Company_djvu.txt — Archived: — — Tier: 1 — Class: CONTEMPORANEOUS OBSERVATION — Passage: "HELD AT THE OFFIC A ОЎ THE AMERICAN TELEPHONE AND. TELEGRAPH COMPANY. September 7, 8 and. 9, (887. 18 COURTLANDT STREET, NEW YORK" — Conf: Medium — Corroboration: 1 independent — Conflicts: None

BD04 Claim: 1984-01-01 is where the registrant count changes, and it is outside Stage 1. — Date: 1984-01-01 — Source: Southwestern Bell Corporation Form 10-K for FY1993, filed 1994-03-18 (P1S05) — Source date: 1994-03-18 — URL: https://www.sec.gov/Archives/edgar/data/0000732717/000073271794000005/0000732717-94-000005.txt — Archived: — — Tier: 1 — Class: FACT (RESTATED as to 1983-84: a 1994 document reciting 1983-84) — Passage: "AT&T divested the Corporation by means of a spin-off of stock to its shareowners on January 1, 1984 (divestiture)." — Conf: High — Corroboration: 2 independent registrants, each speaking of itself (P1S05 and P1S04 l.1121) — Conflicts: U.4

---

## A. EXECUTIVE STATE SUMMARY

STATUS: WRITTEN 2026-10-06

**Person described: P2** (American Telephone and Telegraph Company, New York, incorporated 1885), and only P2. The figures below are its own print for the year ending 1913-12-31 (`P1S01`). P4 is not in this window; P1 is named in this window's print only as a different company's employer of record.

### A.1 The state at the stage edge, on the two bases the print itself uses

The registrant's FY1913 report is written in **two registers, and the difference is the finding**: a "Bell Telephone System in United States" register in which P2 is the largest single line, and a smaller "Report of the American Telephone and Telegraph Company" register in which P2's own earnings are **mostly dividends from other companies**. The report says so: the system tables "not including connecting independent or sub-licensee companies, nor the Western Electric Company and Western Union Telegraph Company except as investments in and dividends from those companies are included respectively in assets and revenue" (l.410-421).

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Registrant and state | P2, a New York corporation, "incorporated in 1885 under the laws of the State of New York"; principal executive offices 32 Avenue of the Americas, New York (1993 basis); in-window addresses of record **18 Courtlandt Street** (1887, `P1S02` l.28) and **15 Dey Street, New York City** (1913, `P1S01` l.1835) | P1S04 l.238 (locator); P1S01; P1S02 | High (recital); Medium (in-window addresses) |
| System subscriber stations at 1913-12-31 | **8,133,017**, an increase of 676,943 "including 215,181 connecting stations"; of the total **2,717,808** were operated by local, co-operative and rural independent companies under sub-license or connection contracts | P1S01 l.153-159 [SYSTEM] | Medium (transport cap) |
| Registrant's own telephone traffic revenue | **$5,548,089.00** net for 1913, against total earnings of $45,909,991.62 — i.e. **≈12% of the registrant's income was toll/long-lines working; the rest was dividends, interest and advances to associated companies** (DERIVED: 5,548,089.00 ÷ 45,909,991.62) | P1S01 l.5156-5164 [COMPANY] | Medium |
| Registrant's own asset composition | Stocks of associated companies $454,307,263.79 + bonds $581,000.00 + capital advances $76,096,615.35 = **$530,984,879.14**; its own telephones, real estate and **long-distance telephone plant** = $64,056,281.87; total assets **$655,956,307.97** | P1S01 l.5028-5067, l.5129 [COMPANY] | Medium; footing verified, §K.3 |
| System gross revenue 1913 | **$215,600,000** as printed in prose, **$215,572,822** in the table; increase over 1912 printed "over $16,000,000", tabled $16,400,668 | P1S01 l.423-425 vs l.502 | Medium — the prose/table pair is registered at §U.5 |
| Plant carried on the books | **$797,159,487** at 1913-12-31, an increase of $54,871,856 or **7.4%**, "which compares with an increase of 8.2 per cent. in gross earnings" | P1S01 l.470-473 [SYSTEM] | Medium |
| Who ran it | President **Theodore N. Vail**; Senior Vice President Union N. Bethell; Vice Presidents H. B. Thayer, N. C. Kingsbury, Edward J. Hall, R. W. Devonshire, B. E. Sunny, C. R. Bangs; Secretary Arthur A. Masters; Treasurer George D. Milne; Comptroller **Charles G. DuBois**; Chief Engineer John J. Carty; General Counsel Nathaniel T. Guernsey | P1S01 l.47-95 | Medium |
| Whose signature is on the accounts | "CHARLES G. DuBOIS, Comptroller" prints beneath the company balance sheet | P1S01 l.5132 | Medium |
| Owner base | **55,983 shareholders** at 1913-12-31, up 5,686 in the year; 49,144 held fewer than 100 shares; 11,595 held 5 shares or less; "The average number of shares held was 59. **A majority of the Company's shareholders are women.**" Less than 6% of the stock stood in the names of brokers | P1S01 l.1307-1330 [COMPANY] | Medium |
| Regulatory position | The Act of Congress approved 1913-03-01 directed the Interstate Commerce Commission to value the property of every common carrier in its jurisdiction, "which includes all the principal telephone companies"; the company's own engineers' appraisals "have shown that the cost of reproduction of the Bell properties, not including cost of intangibles, would exceed their book cost by some $61,000,000" | P1S01 l.454-468 | Medium |
| Political exposure stated in the open | "GOVERNMENT OWNERSHIP AND OPERATION" and "GOVERNMENT PURCHASE" are section headings of the report; "Our opposition to Government operation and ownership is not based on pecuniary, partisan, prejudiced or personal reasons" | P1S01 l.1900, l.1928-1931, l.1971 | Medium |
| Settlement with the Administration | A five-point course of action agreed with the Attorney General, dated **December 19, 1913**, signed for the company "By N. C. Kingsbury, Vice President", acknowledged by J. C. McReynolds and quoted approvingly by Woodrow Wilson | P1S01 l.1696-1890 | Medium — §N, §U.6 |
| Still broken at the edge | The registrant's own list: the Boston–Washington underground still mixed old and new cable types ("These short haul cables make up 47 per cent. of the total cable in the line", l.1482); automatic switching not adopted and its superiority "not … demonstrated" (l.1530-1541); a competitor's property in Chicago in the hands of a receiver (l.1660-1668); $4,000,000 of indebtedness to Western Union falling due across 1914-15 (l.5091); 1913 surplus earnings **lower** than 1912 ($11,735,194 vs $13,221,110) | P1S01 | Medium |

### A.2 What the state summary cannot say

No held byte prints **1877** as an act of P2, **1895** as a completed line, or **1915** as an achieved conversation (§Boundary). **`Alexander Graham Bell` occurs 0 times** across the six periodical layers and the seven cited SEC documents (measured this pass), so this file credits **no individual with founding anything** (§B). The registrant count that answers `T` today (P4) is absent from the entire window. No employee headcount for P2 is printed in the held bytes — the nearest figure is a staff statement, "we now have working at headquarters on the problems of the associated companies **550 engineers and scientists**" (l.1554), which is a headquarters technical staff, not a workforce (§S G-6). Nothing in the window dates the transfer of the Bell System parentage from P1 to P2 (§S G-3).

### A.3 Why failure remained plausible in 1914, on in-window evidence only

Net earnings fell short of the growth story on the print's own arithmetic: gross earnings rose $16.4M while total expenses rose $14.6M, so **net earnings rose $1.8M** and the balance after interest and dividends **fell $644,426** (l.543-577). The 1913 print's own six-year retrospective reports that of the $87,000,000 gross-earnings increase since 1907, "$69,500,000 has been absorbed by increase in expenses" (l.717-723). The regulator was building a valuation that could reprice the whole plant (l.454-468). The Attorney General's settlement obliged P2 to **sell its Western Union stock** and to **stop acquiring competing telephone companies** (l.1711-1728), while the independent movement it had just conceded the right to connect to was, in the words of its own fiercest critic, growing: "The Independent companies going into the field from 1895 to 1900 foresaw a greater development at a lower price" (`P1S03` l.1027-1028). Municipal and federal ownership of telephone service was an active political position stated in the registrant's own report as something to be argued against (l.1900-1975). Nothing in the held bytes makes the survival of P2's form of organisation look settled in 1914.

### Claim records (§A)

A01 Claim: P2 was incorporated in 1885 in New York, on the strength of its own FY1993 10-K recital. — Date: 1885 — Source: AT&T (CIK 0000005907) Form 10-K for FY1993, filed 1994-03-25 (P1S04) — Source date: 1994-03-25 — URL: https://www.sec.gov/Archives/edgar/data/0000005907/000000590794000008/0000005907-94-000008.txt — Archived: — — Tier: 1 — Class: FACT, RESTATED (a 1994 document reciting 1885; the in-window carrier of 1885 prints cable dates instead) — Passage: "American Telephone and Telegraph Company ("AT&T" or "Company") was incorporated in 1885 under the laws of the State of New York" — Conf: High — Corroboration: 1 independent (the recital; "New York Corporation" at l.3454 is the same lineage) — Conflicts: U.2

A02 Claim: Bell System subscriber stations at 1913-12-31 were 8,133,017, of which 2,717,808 were run by independent companies under contract. — Date: 1913-12-31 — Source: Annual Report of the Directors … 1913 (P1S01) — Source date: 1914 — URL: https://archive.org/download/annualreportofdi00amer_14/annualreportofdi00amer_14_djvu.txt — Archived: — — Tier: 1 — Class: CONTEMPORANEOUS OBSERVATION (company self-report; no independent count) — Passage: "the number of stations which constituted our system in the United States was 8,133,-017, an increase of 676,943" — Conf: Medium — Corroboration: 0 independent — Conflicts: None

A03 Claim: By 1913 the registrant's own earnings were mostly dividends from other companies, not telephone working. — Date: 1913-12-31 — Source: P1S01 company earnings statement — Source date: 1914 — URL: as A02 — Archived: — — Tier: 1 — Class: FACT as printed / DERIVED as share — Passage: "Telephone Traffic (net) . 5,472,812.66 … 5,548,089.00" — Conf: Medium — Corroboration: 0 independent — Conflicts: None

A04 Claim: The company's own print reports net earnings growth of $1,802,833 against gross growth of $16,400,668, and a fall in the balance after dividends. — Date: 1913-12-31 — Source: P1S01 l.494-577 — Source date: 1914 — URL: as A02 — Archived: — — Tier: 1 — Class: FACT as printed — Passage: "Net Earnings . $ 56,886,690 … $ 58,689,523 … $ 1,802,833" — Conf: Medium — Corroboration: 0 independent — Conflicts: None

A05 Claim: A majority of the registrant's 55,983 shareholders in 1913 were women. — Date: 1913-12-31 — Source: P1S01 l.1307-1330 — Source date: 1914 — URL: as A02 — Archived: — — Tier: 1 — Class: CONTEMPORANEOUS OBSERVATION (self-reported register) — Passage: "A majority of the Company's shareholders are women." — Conf: Medium — Corroboration: 0 independent — Conflicts: None

---

## B. FOUNDER / COMPANY STATE

STATUS: WRITTEN 2026-10-06

**Person described: P2 first, P1 by adjacency, P4 by absence.** This section is where the dossier records that **the entity answering for the brand was created by another company for a regulatory purpose, and that no founder event exists inside its own legal birth at all**.

### B.1 The founder question, answered as the corpus answers it

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Is any individual credited with founding anything in held bytes? | **No. `Alexander Graham Bell` = 0 occurrences** across the six periodical layers and the seven cited SEC documents (measured this pass, case-sensitive literals) | counts stated at §Header 1 | High (of the silence over held bytes) |
| What does the earliest held document contain instead? | An **engineering roster with company affiliations**: "EDWARD J. HALL, Jr., General Manager, American Telephone and Telegraph Company"; "Е. М. Barton, President, Western Electric Company"; "W. W. JACQUES, Electrician, **American Bell Telephone Company**"; "JosepH P. Davis, Consulting Engineer, **American Bell Telephone Company**"; "W. D. SARGENT, General Manager, New York and New Jersey Telephone Company"; "W. H. EckERT, General Superintendent, Metropolitan Telephone and Telegraph Company" | P1S02 l.326-358 | Medium |
| What does that roster prove about 1887? | That "Bell" already named **several legal persons**, that P2 was **not yet the head of the family** (its own print lists officers of another company), and that at least five companies with distinct names were working the same cable problem in the same room | P1S02 l.326-358, l.7069-7073 | Medium |
| Who held power at the registrant in 1913? | The officer slate at §A.1 (Vail, President; Kingsbury, Vice President — the signatory of the December 19, 1913 letter; DuBois, Comptroller — the signatory of the balance sheet) | P1S01 l.47-95, l.1823, l.5132 | Medium |
| Board of directors at 1914 print | 22 names printed, including Charles Francis Adams, 2d; George F. Baker; Henry L. Higginson; Lewis Cass Ledyard (OCR "LEWIS CASS LED YARD"); Richard Olney; Theodore N. Vail; Robert Winsor — with one footnote: "* Resigned January 20, 1914" against **Henry P. Davison** | P1S01 l.98-128 | Medium |
| P4's founder state | **Not applicable in Stage 1.** P4 is created in 1983 **by AT&T** (P1S05 l.210-213); no person founds it. Recorded here so no later pass imports a 1913 person into a 1983 registrant | P1S05 | High |
| A named-officer continuity worth flagging, not claiming | "EDWARD J. HALL, Jr., General Manager" (1887) vs "EDWARD J. HALL" listed as Vice President (1913). Whether these are the same man, or father and son, **no held byte states it** | P1S02 l.326; P1S01 l.64 | **UNKNOWN**; §S G-7 |

### B.2 The company state, as the company itself describes it at the edge

The report opens with a statement of what kind of organisation it is reporting on: "…ment covering the business of the Bell System as a whole, followed by the report of the American Telephone and Telegraph Company, for the year 1913" (l.144-146). P2 is, in its own 1913 words, simultaneously **an operator of long lines** and **a holder of other companies' stock** — and the print does not present those as unusual. Its long-distance plant is a $49.3M line inside a $656M balance sheet dominated by $531M of associated-company paper (§A.1). The 1913 report's own defence of that structure is a rate-of-return argument: "the property employed earned less than 6 per cent, per annum, and the dividends and interest paid were less than 5 per cent, upon the value of the property, which could not be considered unreasonable" (l.1001-1004). On the personnel side the print states a technical establishment, not a workforce: 550 engineers and scientists at headquarters (l.1554), and an employee-benefit plan "in effect a year, during which period in **16,054 cases** employees in this Company and the associated operating companies have participated in the benefits" (l.1340-1345).

### B.3 What this dossier refuses to write as biography

No paragraph here explains 1885–1915 through a person's character or foresight. There is no carrier for a founder, for a founding act, or for an internal deliberation. Where the record shows a decision, it shows it as an **institutional act with a date and a signatory** — the December 19, 1913 letter (§N) is the paradigm case, signed by a Vice President, acknowledged by the Attorney General, and reproduced in the annual report. **§14 rule 4 applied to AT&T: roles are not founders, and a predecessor is not the registrant.**

### Claim records (§B)

B01 Claim: Held bytes credit no individual with founding anything; the name that carries the art occurs zero times. — Date: 1875-01-01..1915-12-31 — Source: measurement over held `sources/periodicals/*` (6 layers) and the 7 cited `sources/sec/*` documents — Source date: 2026-10-06 — URL: file-local, paths at §T — Archived: — — Tier: 1 (the measurement) — Class: FACT (of a null over held bytes; **not** a corpus null) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High — Corroboration: 1 measurement, reproducible — Conflicts: U.2

B02 Claim: AT&T's own 1887 print lists officers of American Bell Telephone Company, proving P2 was not yet the family head. — Date: 1887-09 — Source: P1S02 — Source date: 1887 — URL: https://archive.org/download/report-of-a-conference-held-at-the-office-of-the-american-telephone-and-telegraph-company/Report%20of%20a%20conference%20held%20at%20the%20office%20of%20the%20American%20Telephone%20and%20Telegraph%20Company_djvu.txt — Archived: — — Tier: 1 — Class: CONTEMPORANEOUS OBSERVATION — Passage: "W. W. JACQUES, Electrician, American Bell Telephone Company" — Conf: Medium — Corroboration: 1 independent (a second mention at l.353 is the same document) — Conflicts: None

B03 Claim: Theodore N. Vail was the registrant's President and a director in the 1913-14 print. — Date: 1914 (print of FY1913) — Source: P1S01 l.50-52, l.125 — Source date: 1914 — URL: as B02 file family §A — Archived: — — Tier: 1 — Class: FACT as printed — Passage: "President THEODORE N. VAIL" — Conf: Medium — Corroboration: 0 independent — Conflicts: None

B04 Claim: P4 was created by a company, not by founders: "incorporated … in 1983 by AT&T". — Date: 1983 — Source: P1S05 — Source date: 1994-03-18 — URL: https://www.sec.gov/Archives/edgar/data/0000732717/000073271794000005/0000732717-94-000005.txt — Archived: — — Tier: 1 — Class: FACT, RESTATED (out-of-window document; cited only to establish that no Stage-1 person can be charged to P4) — Passage: "incorporated under the laws of the State of Delaware in 1983 by AT&T as one of seven regional holding companies (RHCs)" — Conf: High — Corroboration: 2 (P1S06 l.151, P1S07 l.226 — same lineage of filings by one registrant, so counted as **one** origin per §3) — Conflicts: U.1

---

## C. ORIGINAL PROBLEM

STATUS: WRITTEN 2026-10-06

**Person described: P2.** The problem this registrant was working is not "start a company"; it is a physical problem of transmission, and the corpus states it in the company's own technical print.

### C.1 The problem as stated in 1887, by the people in the room

The earliest held document opens with a manager defining why the meeting exists: "We meet here to-day for the purpose of discussing in an entirely informal manner the subject of telephone cables. We all realize how great the need is for more information on this subject, and how few sources of information are open in electrical literature or in the current published records of telephone work" (`P1S02` l.361-366). And it states the epistemic condition without embarrassment: "It is, perhaps, too much to expect that we can now reach the desired result of formulating definite rules covering all the details of specifications for telephone cables for any stated use. **The art of telephony is probably too new to have yet reached any such state of exact knowledge.**" (l.375-379). The purpose of writing it down is stated in the same breath: "we will have in the report of this meeting a large amount of valuable data preserved in a permanent form available for future reference" (l.390-392). This is a **company-not-a-founder origin problem**: the registrant's documented earliest activity is a three-day internal standards conference with practical tests, not a launch.

### C.2 The problem as stated in 1913, by the same registrant 26 years later

The FY1913 report states the problem as one of distance and loss, not of adoption: "the problem of talking through long underground cables or over great distances could not be solved by increasing the loudness of the transmitter or the receiver. **Failure to understand this has been the cause of loss to many who have invested in companies promoting so-called loud-speaking telephones**" (`P1S01` l.1386-1392). The economic form of the problem is stated as a rule: "In the transmission of speech one mile of underground cable is often equal to 50 or 100 miles of open wire overhead, and in underground transmission a point was soon reached where no speech could be got by any transmitter" (l.1394-1398). And the consequence is drawn as a growth limit: "Unless this difficulty could be minimized, further growth of the telephone was not to be expected" (l.1399-1400).

### C.3 The 1885 decoy, written down so it is not inherited

The only held in-window document that prints "1885" **does not print an incorporation**. It prints four cable dates: "Our first Paterson Underground Cable laid in New York was completed March 18th, 1885, with no special make up (manner of making). Number of conductors, one hundred; No. 18 American gauge; the longest or greatest length being 1,965 feet" (`P1S02` l.4572-4576); "The Edison Underground System was completed June 91 [sic], 1885, from Twenty-first street and Broadway" (l.4614-4615); "The Brooks System at our Spring Street Exchange, was completed May 28, 1885" (l.4631-4632); and "the two Clark cables in March, 1885, on account of defective insulation" (l.7107). **A grep for 1885 in an 1887 AT&T document returns four cable completions and no charter.** Anyone who later "confirms 1885" from this file has confirmed a cable; the incorporation is carried only by `P1S04` l.238, a 1994 recital (§U.2).

### C.4 What the original problem was NOT

| Claim later told | What the held record supports | Class |
|---|---|---|
| "AT&T was founded to run local telephone exchanges." | P2's own 1913 balance sheet shows its **own working plant was long-distance** ($49,269,173.30 of long-distance telephone plant; telephones $14,279,677.65) and its exchange business sat in **associated companies' stock** ($454,307,263.79) | FACT as printed, Medium; the inference "therefore built for long lines" is **INFERENCE, Low** — the certificate of incorporation is not held |
| "The company was the Bell System's parent from the start." | Its own 1887 print lists officers of **American Bell Telephone Company** and of four other companies; 0 held bytes describe a 1885–1887 parentage; the 1899/1900 transfer has **no carrier here** | FACT (of the silence); §S G-3 |
| "The problem was monopoly." | The 1887 print's problem is measurement and insulation; the 1913 print's problems are loading, crosstalk, distance, and a federal valuation. Monopoly appears in the corpus only in a **hostile third party's** description (`P1S03` l.188-190) and in the company's own defensive language about government ownership (`P1S01` l.1928-1968) | CONTEMPORANEOUS OBSERVATION / RETROSPECTIVE framing, Low |
| "Founding capital was raised in 1885." | **UNKNOWN. No held byte states any 1885 capital figure.** The only incorporation-with-a-dollar-figure in any held non-SEC layer belongs to **another company entirely**: the Chicago & Milwaukee Telegraph Line, "Built in 1878 by some linemen as a speculation … incorporated with a stock of $50,000" (`P1S01` l.2985-3000) | UNKNOWN, §U.8 |

### Claim records (§C)

C01 Claim: The registrant's earliest documented activity is a three-day technical conference on telephone cables, held at its own office. — Date: 1887-09-07..09 — Source: P1S02 — Source date: 1887 — URL: as B02 — Archived: — — Tier: 1 — Class: CONTEMPORANEOUS OBSERVATION — Passage: "We meet here to-day for the purpose of discussing in an entirely informal manner the subject of telephone cables" — Conf: Medium — Corroboration: 1 independent — Conflicts: None

C02 Claim: The company's own print states that the art had not reached exact knowledge, and that the meeting's value was to preserve data for future reference. — Date: 1887-09 — Source: P1S02 l.375-392 — Source date: 1887 — URL: as B02 — Archived: — — Tier: 1 — Class: FOUNDER-ADJACENT? No: **CONTEMPORANEOUS OBSERVATION by an officer** (no founder exists in this corpus) — Passage: "The art of telephony is probably too new to have yet reached any such state of exact knowledge." — Conf: Medium — Corroboration: 1 independent — Conflicts: None

C03 Claim: A grep of "1885" in the held in-window document returns cable completions, not an incorporation. — Date: 1885 (four dates) — Source: P1S02 l.4572-4576, l.4614-4615, l.4631-4632, l.7107 — Source date: 1887 — URL: as B02 — Archived: — — Tier: 1 — Class: FACT (of what the bytes print) — Passage: "Our first Paterson Underground Cable laid in New York was completed March 18th, 1885" — Conf: Medium — Corroboration: 1 independent — Conflicts: U.2

C04 Claim: The 1913 print frames the original problem as loss per mile, with a stated conversion rate of one underground mile to 50–100 overhead miles. — Date: 1913-12-31 — Source: P1S01 l.1394-1400 — Source date: 1914 — URL: as A02 — Archived: — — Tier: 1 — Class: CONTEMPORANEOUS OBSERVATION — Passage: "one mile of underground cable is often equal to 50 or 100 miles of open wire overhead" — Conf: Medium — Corroboration: 1 independent — Conflicts: None

---

## D. FIRST EXPERIMENT

STATUS: WRITTEN 2026-10-06

**Person described: P2.** For a network utility created before it had customers, "first experiment" cannot mean "first sale". Two carrier classes exist in this corpus and they must not be conflated: an **experiment reported as it was happening** (1887) and an **experiment sequence reported years afterwards by the same company** (1881–1913, inside `P1S01`). The second is in-window *print* but retrospective *as to the events it dates*, and is labelled so in every row below.

### D.1 The earliest documented experiment: September 1887, in the registrant's own house print

| Variable | Value | Source | Confidence |
|---|---|---|---|
| What was done | A three-day conference (Sept 7, 8, 9, 1887) at 18 Courtlandt Street, New York, on telephone cables, with papers, discussion, and practical tests: "we wish to add together the results of our observations and experience, to discuss the theories which explain observed phenomena, and to **illustrate, by practical tests, the application of the formulas** which we hope to have presented, for our practical use in the future" | P1S02 l.368-373 | Medium |
| Who performed it | nine named engineers and managers drawn from **five companies** (P2, American Bell, Western Electric, New York and New Jersey Telephone, Metropolitan Telephone and Telegraph) | P1S02 l.326-358 | Medium |
| What was prepared | papers by Jacques, Patterson and Barrett "in reply to a series of questions" — of which one was **not written up in time** ("through some misunderstanding Mr. Patterson tells me he has not put his report in writing, but will give us verbally the information we ask for"), plus statements of tests by Eckert, Sargent and Hibbard "on cables actually in use in their respective exchanges" | P1S02 l.398-412 | Medium |
| The experiment's own scope limit | "It is, perhaps, too much to expect that we can now reach the desired result of formulating definite rules covering all the details of specifications for telephone cables for any stated use" | P1S02 l.375-377 | Medium |
| A network-of-information test run live during the meeting | Hall wrote to Boston on September 6 about the condition of the 1883 cables; the reply printed in the report is dated **BOSTON, September 7, 1887** and opens "In reply to yours of September 6th, referring to underground cables laid down in this city several years ago, I have collected the following information to-day which I trust will answer your purpose to-morrow" | P1S02 l.7082-7094 | Medium |
| What it demonstrates | that by 1887 the firm's documented experimental method was **measurement, cross-company comparison and written specification** — and that the information network across companies answered inside 24 hours | INFERENCE from the above rows | Medium (that the method is as described); Low (on any effect size — none is measured here) |
| What it does NOT demonstrate | any customer, any revenue, any unit cost, and any decision to build. Nothing in the held 1887 bytes states how much the meeting changed, or what was decided | — | High (of the absence over held bytes) |

### D.2 The long-lines sequence, as the registrant reported it in 1913 (registrant-retrospective)

All dates in this table come from one in-window document describing events up to 32 years earlier. `P1S01` l.1416-1511.

| Date | What the company says it did | Line | Class |
|---|---|---|---|
| 1880 | quotes its **own earlier annual report**: "This work is expensive, hut [sic] it is of the first importance to our company and must he [sic] continued" — the held 1880 report is **not on this shelf**; the quotation is its only carrier here | l.1401-1409 | RESTATED within an in-window document |
| 1881 | "we had laid experimental underground cables for a short distance alongside of a Massachusetts railroad track with small results" | l.1416-1418 | registrant-retrospective |
| 1883 | "several cables were laid at Boston, the longest of which was 1,500 feet"; subscribers using it "could not talk satisfactorily further than the suburbs" | l.1418-1426 | registrant-retrospective; corroborated **independently in kind** by `P1S02` l.7069-7070 and l.7096-7098 (American Bell, 1883, Boston iron-pipe conduit, four Patterson lead cables + one Day kerite + one rubber, two Clark rubber in April 1883 — note the 1887 letter prints "April, 1853" for the Clark pair, an OCR slip) |
| 1887 | "the introduction of the twisted pair underground conductor began. This meant **the abandonment of the entire underground plant of the Bell System** and the introduction of the new type, without which the telephone system as we know it to-day would be an impossibility" | l.1431-1435 | registrant-retrospective; the abandonment claim is a company assertion with no independent count |
| 1902 | Pupin loading coils advance the art enough that a "loaded cable" for suburban service was "successfully installed between New York and Newark" | l.1438-1442 | registrant-retrospective |
| 1905 / 1906 | a loaded cable 20 miles from New York toward Philadelphia; then **90 miles** operated between those two cities, but "in the then state of the art this cable could not be used beyond Philadelphia or New York" | l.1444-1448 | registrant-retrospective |
| 1911 | "we were enabled to design an underground cable, capable of giving a satisfactory conversation between Washington and Boston" | l.1450-1453 | registrant-retrospective — a **design** claim |
| 1912 | a section laid Washington–Philadelphia, joining earlier cable to New York; "talking underground for the first time between New York and Washington represented the longest distance underground yet achieved" | l.1455-1457, l.1485-1487 | registrant-retrospective, near-contemporaneous |
| 1913 | a section laid New Haven–Providence; **satisfactory conversation Boston–Washington by underground wire**, "in part through types of cable formerly suitable for short haul distances only. These short haul cables make up 47 per cent, of the total cable in the line"; "By 1913, this distance had been doubled. The Boston-Washington telephone cable is several times longer than any other in the world" | l.1459-1490 | CONTEMPORANEOUS (the report's own year) — **this is the strongest validated achievement in Stage 1** |
| 1913 study → 1915 plan | "An exhaustive study of the New York-Denver line during the last year has shown that these improvements in transmission through underground wires are also applicable to overhead lines. **Plans are now making for the rearrangement of the New York-Denver circuit**; when accomplished, the telephone transmission between New York and Denver will be equal to that now given between points about 200 miles apart and will insure satisfactory talk from the Atlantic to the Pacific and in due course bring all points in the United States within speaking distance of each other" | l.1501-1511 | CONTEMPORANEOUS **as design**; UNKNOWN as event |

### D.3 What the corpus cannot answer about a "first"

There is no carrier for a first customer, a first toll call, a first revenue line, or an opening day of any long-lines circuit. The registrant's own report gives **aggregate traffic**, not firsts: "the daily average of toll connections was about 806,000, and of exchange connections about 26,431,000, as against corresponding figures in 1912 of 738,000 and 25,572,000" (l.191-194). §10's "first customer is unknown" trigger fires and is logged as a gap (§S G-4) with the route that could carry it (family (e) manuscript/print; the 1901–1928 annual-report run, §S R-3).

### D.4 The 1915 transcontinental claim: design evidence, not event evidence

This distinction is the load-bearing judgment of Stage 1 and is stated once, plainly.
* **What is carried.** `P1S01` l.398-402, the registrant's own FY1913 print: "It is easier to talk with Denver to-day than with Chicago then, and with the completion of the line to the Pacific Coast in 1915, commercial communication **will be** dependable and practicable." Also l.1509-1511: "will insure satisfactory talk from the Atlantic to the Pacific". **Both are future-tense statements of programme inside a document dated to the year they precede.** The most that can be claimed is that **as of the FY1913 report the registrant had announced an intention, a date, and a technical route.**
* **What is not carried.** `transcontinental` occurs **0 times** in every held byte, SEC and periodical alike (re-measured this pass). 1895 as an event has **no carrier**: its three occurrences in the 1913 layer are the first column of statistical series (l.978, l.1031, l.1043), and in the 1908 pamphlet 1895 is "The Independent companies going into the field from 1895 to 1900" — competition, not a line. **The 1915 opening is UNKNOWN as an event and CARRIED as design.** §U.3 registers it; §S R-2 names the two held-catalogue items that could settle it (`2xVAAAAAYAAJ` 1915, `j4BbAAAAMAAJ` 1914).

### Claim records (§D)

D01 Claim: The registrant's earliest documented experiment is a three-day 1887 cable conference with practical tests. — Date: 1887-09-07 — Source: P1S02 — Source date: 1887 — URL: as C01 — Archived: — — Tier: 1 — Class: CONTEMPORANEOUS OBSERVATION — Passage: "to illustrate, by practical tests, the application of the formulas which we hope to have presented" — Conf: Medium — Corroboration: 1 independent — Conflicts: None

D02 Claim: P2's own 1913 print dates the first New York–Boston loaded suburban cable to 1902 and the first 90-mile underground operation to 1906. — Date: 1902 / 1906 — Source: P1S01 l.1438-1448 — Source date: 1914 — URL: as A02 — Archived: — — Tier: 1 — Class: RETROSPECTIVE INTERPRETATION by the registrant, in an in-window document — Passage: "by 1906 a cable 90 miles long was successfully operated between those two cities" — Conf: Medium — Corroboration: 0 independent — Conflicts: None

D03 Claim: By its own account the registrant achieved satisfactory underground conversation Boston–Washington in 1913. — Date: 1913 — Source: P1S01 l.1476-1490 — Source date: 1914 — URL: as A02 — Archived: — — Tier: 1 — Class: CONTEMPORANEOUS OBSERVATION — Passage: "it is now possible to talk satisfactorily by underground wires from Boston to Washington" — Conf: Medium — Corroboration: 0 independent — Conflicts: None

D04 Claim: The 1915 Pacific Coast line is carried only in the future tense and is therefore design evidence. — Date: 1915 (projected) — Source: P1S01 l.398-402 — Source date: 1914 — URL: as A02 — Archived: — — Tier: 1 — Class: CONTEMPORANEOUS OBSERVATION as to intention; **UNKNOWN as to occurrence** — Passage: "with the completion of the line to the Pacific Coast in 1915, commercial communication will be dependable and practicable" — Conf: Medium (intention); UNKNOWN (event) — Corroboration: 1 independent for the intention only — Conflicts: U.3

---

## E. PRODUCT RECONSTRUCTION

STATUS: WRITTEN 2026-10-06

**Person described: P2, and (as a stated basis) the SYSTEM that its accounts consolidate.** The product in this window is not a device; it is **a circuit that works, sold by the message and by the station**. Reconstruction is therefore in three layers: the physical cable, the apparatus at its ends, and the tariff/interconnection terms that convert capacity into a purchasable service.

### E.1 The physical product, at the specification level 1887 gives

| Variable | Value | Source | Confidence |
|---|---|---|---|
| First New York Paterson cable (completed 1885-03-18) | 100 conductors, No. 18 American gauge, greatest length **1,965 feet**; insulation when laid **1 to 100 megohms**, the low figure attributed to "the necessity of cutting and splicing the cable, on account of the gas pipes in the street"; laid **in wooden boxes filled with sand**, the boxes "made from creosoted lumber"; result: "has worked well with no cross-talk" | P1S02 l.4572-4583 | Medium |
| Dorsett conduit cables, Sixth Avenue 21st–58th (completed 1887-04-01) | one 90-conductor (No. 14 AWG), one 100-conductor (No. 16), one 110-conductor (No. 18); conductors spaced ½ inch apart; **300 conductors in all, all working**; insulation 500–1,000 megohms per mile; static capacity 0.25 microfarad per mile | P1S02 l.4586-4611 | Medium |
| Edison system (completed June 1885 — print reads "June 91[, 18]85") | conductors transposed "about every (60) sixty feet"; greatest length 1,725 feet; insulation when laid 500,000 ohms; static capacity 0.40 µF/mile; 200 conductors in service | P1S02 l.4614-4626 | Medium; the OCR date defect is registered at §U.5 |
| Brooks system, Spring Street Exchange (completed 1885-05-28) | 400 wires drawn into an **iron pipe filled with oil under pressure**, 2,449 feet, No. 18 AWG, 30 megohms/mile; insulation deteriorated when water entered the pipe; the cable had to be "drawn, and boiled out, drawn in again and fresh oil put in" | P1S02 l.4631-4641 | Medium |
| Aerial cables | Paterson ~1 megohm/mile, kerite ~300; "The reason for not getting higher insulation on these cables is on account of its being impossible to make a perfect terminal box" | P1S02 l.4646-4650 | Medium |
| Conductor metallurgy as a product variable | Western Electric lead sheath "has now been down almost three years, and the lead pipe shows scarcely any signs of decay"; Brooks claimed-pure lead corroded to 44/100-inch crust in eight months; "the Western Electric has a small percentage of tin mixed with it for the purpose of hardening it", and the New York and New Jersey Telephone Company copied the tin practice | P1S02 l.5032-5055 | Medium |
| Scale of the plant by 1913 | 16,111,011 miles of wire in use (1,500,198 added in the year); ~13.8M exchange / >2.3M toll; **92% copper**; 8,817,815 miles underground, "including 543,923 miles of toll wires in underground cables"; underground conduits $85,700,000 + cables in them $95,800,000 = **$181,500,000** | P1S01 l.176-186 [SYSTEM] | Medium |

### E.2 The apparatus at the ends of the circuit

"During the thirty-seven years from 1877 to 1914 there were designed and constructed and installed **fifty-three improved types and styles of telephone receiver, and seventy-three types and styles of transmitter**. These figures do not include hundreds of minor improvements" (`P1S01` l.1368-1373). "At the beginning of 1914 there were in the Bell System **12,000,000 telephone receivers and transmitters** owned by the Bell Company. Of these practically none were made prior to 1902, and of all the instruments now in service the average are less than five years old" (l.1379-1383). That sentence is the company's own statement that its installed apparatus base turns over on a sub-five-year cycle, and it is the mechanism the depreciation section then argues from (l.366-384). Switchboards: "During the period of twenty-five years practically all of the switchboards have been changed several times… We have designed, manufactured and installed all kinds of switchboards — automatic, semi-automatic and manual" (l.1521-1527). Third-party corroboration of the type-churn from a hostile observer: in Detroit "the Michigan Bell Telephone Company has been taking out many of the still remaining old-style Blake transmitters, and making an extra charge for the modern transmitters" (`P1S03` l.1160-1165).

### E.3 The service as a purchasable thing: toll, exchange, and interconnection terms

The only in-window **tariff** text held for P2 is the interconnection schedule agreed with the Attorney General, which is a product definition as much as a policy: any independent company's subscriber may reach any Bell subscriber (and any subscriber of an independent the Bell System connects to) "who is served by an exchange which is **more than fifty miles distant** from the exchange in which the call originates"; the independent must supply "standard trunk lines between its exchanges and the toll board of the nearest exchange of the Bell operating company"; "the entire toll circuit involved … shall be operated by, and under the control of, the employees of the Bell System"; the independent's subscriber pays "the regular toll charge of the Bell Company, and in addition thereto … **a connection charge of ten cents for each message**" — while "long lines" business offered to A&T "shall be accepted at the regular toll rate and **no connecting charge** shall be required" (`P1S01` l.1750-1817). **The 50-mile rule is the sharpest in-window statement of what P2 considered its own product to be.** The traffic measures of that product in 1913: about 806,000 toll connections and about 26,431,000 exchange connections per day, "the total daily average for 1913 reaching 27,237,000, or at the rate of about 8,770,300,000 per year" (l.190-196). **That printed annual rate does not foot against the printed daily average** (27,237,000 × 365 = 9,941,505,000; the ratio implies ≈322 days) — recorded as an unexplained internal inconsistency, §U.5, and no value is substituted for either.

### Claim records (§E)

E01 Claim: The held record specifies the registrant's 1885–1887 cable product down to conductor count, gauge, insulation and laying method. — Date: 1885-1887 — Source: P1S02 l.4572-4650 — Source date: 1887 — URL: as C01 — Archived: — — Tier: 1 — Class: CONTEMPORANEOUS OBSERVATION — Passage: "Number of conductors, one hundred; No. 18 American gauge; the longest or greatest length being 1,965 feet" — Conf: Medium — Corroboration: 1 independent — Conflicts: U.5

E02 Claim: By 1914 the registrant reported 12,000,000 owned instruments of which practically none were made before 1902. — Date: 1914-01-01 — Source: P1S01 l.1379-1383 — Source date: 1914 — URL: as A02 — Archived: — — Tier: 1 — Class: CONTEMPORANEOUS OBSERVATION (self-report) — Passage: "Of these practically none were made prior to 1902, and of all the instruments now in service the average are less than five years old." — Conf: Medium — Corroboration: 0 independent — Conflicts: None

E03 Claim: The 1913 interconnection schedule defines P2's own product boundary at fifty miles and prices the independent's access at ten cents a message. — Date: 1913-12-19 — Source: P1S01 l.1750-1817 — Source date: 1914 — URL: as A02 — Archived: — — Tier: 1 — Class: FACT as printed (a document with legal effect) — Passage: "a connection charge of ten cents for each message which originates on its lines and is carried, in whole or in part, over the lines of the Bell System" — Conf: Medium — Corroboration: 1 independent (the Attorney General's acknowledgement at l.1837-1854 is a second voice confirming the same document's existence, not of its terms) — Conflicts: U.6

E04 Claim: The report's own annualised traffic rate does not foot against its daily average. — Date: 1913 — Source: P1S01 l.190-196 — Source date: 1914 — URL: as A02 — Archived: — — Tier: 1 — Class: ESTIMATE/DERIVED discrepancy; **DERIVED: 27,237,000 × 365 = 9,941,505,000 vs printed 8,770,300,000** — Passage: "the total daily average for 1913 reaching 27,237,000, or at the rate of about 8,770,300,000 per year" — Conf: Medium (both printed values); UNKNOWN (which basis produces the printed annual figure) — Corroboration: 1 — Conflicts: U.5

---

## F. CUSTOMER

STATUS: WRITTEN 2026-10-06

**Person described: P2 (its subscriber base) and, for the paying relationship, [SYSTEM].**

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Scale | 8,133,017 stations "constituted our system in the United States" at 1913-12-31, +676,943 on the year, including 215,181 connecting stations | P1S01 l.153-155 [SYSTEM] | Medium |
| How many customers P2 did **not** serve directly | **2,717,808** of those stations were "operated by local, co-operative and rural independent companies or associations having sub-license or connection contracts, so-called connecting companies" — 33% of the total on the report's own arithmetic (DERIVED: 2,717,808 ÷ 8,133,017) | P1S01 l.156-159 | Medium |
| Penetration claim printed by the company | "On January 1, 1914, there was one Bell Telephone Station to each 12 of the Total Population of the United States" | P1S01 l.5509-5511 | Medium |
| Geographic reach sold to the customer | "The Bell telephone toll lines of the United States now reach 70,000 places, from many of which a telegraph message can be sent", compared in the same paragraph with "less than 60,000 post offices, 60,000 railroad stations and regular telegraph offices at about 25,000 places" | P1S01 l.163-168 | Medium |
| What the customer bought | connection to a network, priced per station and per message. The plainest statement of the network-value logic in the whole held corpus is at `P1S03` l.242-251: "The value of any exchange system is measured by the number of the members of any community that are connected with it… Duplication of plant is a waste to the investor. Duplication of charges is a waste to the user." **Attribution warning:** the pamphlet introduces its quotations with "Certain extracts from the report are reproduced below" (l.186-187), so this sentence is most probably **the registrant's own 1907 words carried inside a hostile vehicle**, not the pamphleteer's; the extract/plain-text boundary is not recoverable from this OCR rendering, and the ambiguity is registered at §U.9 rather than resolved | P1S03 l.186-187, l.242-251 | Medium (the words); **UNKNOWN (whose words)** |
| First customer | **UNKNOWN; no carrier** (§D.3, §S G-4) | — | High (of the silence) |
| Customer identity, mix, churn, satisfaction | **UNKNOWN in every respect.** No held byte gives a customer count by class, any rate schedule for P2's own stations, a complaint, a disconnect, or a repeat measure. The 1913 print's customer-facing defence is a rate-of-return argument addressed to shareholders and regulators, not to subscribers (l.1001-1004) | — | High (of the silence over held bytes) |
| Who the customer's alternative was | independents, on the 1913 interconnection terms above; and, in the political register, the government-owned systems the report argues against ("no government-owned telephone system in the world is giving as cheap and efficient service as the American public is getting from all its telephone companies", l.1964-1968) | P1S01 | Medium |

**Adaptation note (method §7).** For a subscription utility the standard §F frame (first customer, buyer identity, unit price) has no in-window carrier at all; the adapted equivalents delivered here are **stations, share-of-network, reach, and the price mechanism stated in the interconnection schedule**, and the absence of the rest is recorded rather than narrated.

### Claim records (§F)

F01 Claim: A third of the Bell System's 1913 stations were operated by independent companies under sub-license or connection contracts. — Date: 1913-12-31 — Source: P1S01 l.156-159 — Source date: 1914 — URL: as A02 — Archived: — — Tier: 1 — Class: FACT as printed; share DERIVED — Passage: "2,717,808 of these were operated by local, co-operative and rural independent companies or associations having sub-license or connection contracts" — Conf: Medium — Corroboration: 0 independent — Conflicts: None

F02 Claim: No held byte names a first customer or any customer characteristic of P2 in 1875–1915. — Date: 1875-01-01..1915-12-31 — Source: measurement over the held bytes this part cites — Source date: 2026-10-06 — URL: file-local — Archived: — — Tier: 1 (of the measurement) — Class: FACT (of a null over held bytes) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High — Corroboration: 1 — Conflicts: None

F03 Claim: The company printed a penetration ratio of one station per twelve Americans at 1914-01-01. — Date: 1914-01-01 — Source: P1S01 l.5509-5511 — Source date: 1914 — URL: as A02 — Archived: — — Tier: 1 — Class: CONTEMPORANEOUS OBSERVATION (self-report; denominator not stated in the held line) — Passage: "there was one Bell Telephone Station to each 12 of the Total Popular tion of the United States" — Conf: Medium — Corroboration: 0 independent — Conflicts: None

---

## G. SUPPLY / HOST SIDE

STATUS: WRITTEN 2026-10-06

**Person described: P2 and the companies that supply it — none of which is P2's subsidiary in the way the 1913 print implies, and one of which (Western Union) P2 agreed in December 1913 to stop controlling.**

| Variable | Value | Source | Confidence |
|---|---|---|---|
| The manufacturing arm | "Sales of the Western Electric Company for 1913 amounted to **$77,532,860**, of which **$50,681,070** represents sales to the companies of the Bell Telephone System, and $26,851,790 represents sales to other customers" — i.e. **65.6% captive** (DERIVED: 50,681,070 ÷ 77,532,860) | P1S01 l.1008-1011 | Medium |
| Its plant consolidation | "The concentration of the company's manufacturing work at its main plant at **Hawthorne, near Chicago**, is now nearly completed" | P1S01 l.1013-1015 | Medium |
| The stated logic of the relation | "Each year the economies and efficiencies due to the relation between the Western Electric Company and the companies of the Bell Telephone System become more apparent" | P1S01 l.1017-1020 | Medium — company assertion, no measure given |
| The competitor's reading of the same event | "The Western Electric Company, late in 1907, presumably under stress of competition, **changed its selling plan so as to go into the competitive market with low prices.** This may be with the expectation, by unprofitable underselling temporarily, of starving out the manufacturing competition" | P1S03 l.755-758 | Medium; a **hostile inference** ("presumably", "may be") and labelled as such |
| Outside suppliers named in the 1887 record | **Paterson**, **Brooks of Philadelphia**, **Clark**, **Day** (kerite), an "okonite" cable, plus **Western Electric**; and the failures are attributed to specific suppliers (§M) | P1S02 l.4875-4900, l.5032-5034, l.7096-7107 | Medium |
| Materials as supply constraints | lead sheath alloyed with tin for hardening; creosoted-wood boxes and conduits; iron-pipe conduit; "impossible to make a perfect terminal box"; copper at 92% of 1913 wire mileage | P1S02 l.4583, l.5032-5055, l.4646-4650; P1S01 l.182 | Medium |
| In-house technical capacity | "we now have working at headquarters on the problems of the associated companies **550 engineers and scientists** carefully selected with due regard to the practical as well as the scientific nature of the problems encountered" | P1S01 l.1550-1556 | Medium |
| Labour as a stated obligation | an employees' pension/disability/insurance plan "in effect a year", with **16,054 cases** of participation by employees of "this Company and the associated operating companies"; the combined system carries an **Employees' Benefit Fund of $8,919,335** at 1913-12-31 against $8,845,000 in 1912 | P1S01 l.1336-1345, l.668-680 | Medium |
| Legal/host capacity | General Counsel Nathaniel T. Guernsey; Consulting Counsel George V. Leverett; a named litigation item in the year: "an action in Chicago involving the relations between this Company and the Central Union Telephone Company" | P1S01 l.79, l.91, l.1660-1662 | Medium |
| Headcount | **UNKNOWN.** No total workforce figure for P2 or the system is printed in held bytes; 550 is a headquarters technical staff and 16,054 is benefit-plan cases, not employees (§S G-6) | — | High (of the silence) |

### Claim records (§G)

G01 Claim: Western Electric's 1913 sales were two-thirds to Bell System companies. — Date: 1913-12-31 — Source: P1S01 l.1008-1011 — Source date: 1914 — URL: as A02 — Archived: — — Tier: 1 — Class: FACT as printed; share DERIVED — Passage: "of which $50,681,070 represents sales to the companies of the Bell Telephone System, and $26,851,790 represents sales to other customers" — Conf: Medium — Corroboration: 0 independent — Conflicts: None

G02 Claim: The registrant's 1913 technical establishment at headquarters is stated at 550 engineers and scientists. — Date: 1913 — Source: P1S01 l.1550-1556 — Source date: 1914 — URL: as A02 — Archived: — — Tier: 1 — Class: CONTEMPORANEOUS OBSERVATION — Passage: "550 engineers and scientists carefully selected" — Conf: Medium — Corroboration: 0 independent — Conflicts: None

G03 Claim: A hostile contemporary read Western Electric's 1907 price change as predatory underselling. — Date: 1907 — Source: P1S03 — Source date: 1908-09 — URL: https://archive.org/download/somecommentsona00chicgoog/somecommentsona00chicgoog_djvu.txt — Archived: — — Tier: 3 (trade association pamphlet) — Class: CONTEMPORANEOUS OBSERVATION + inference by an interested party — Passage: "changed its selling plan so as to go into the competitive market with low prices" — Conf: Medium — Corroboration: 1 independent of P2, but **interested** — Conflicts: None

## H. MARKET (AS KNOWABLE IN-PERIOD)

STATUS: WRITTEN 2026-10-06

**Person described: P2 as the reporter of a SYSTEM market.** The held corpus has no third-party market size for 1875–1915. What it has is the registrant's own comparative arithmetic, which is the period's way of defining a market: the telephone measured against the mail and the telegraph.

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Traffic mix, 1912, Europe vs United States | Europe: mails 17,775,000,000 (71.2%), telegrams 388,000,000 (1.5%), telephone conversations 6,809,000,000 (27.3%), total 24,972,000,000. United States: mails 10,212,000,000 (39.4%), telegrams 113,000,000 (0.4%), telephone conversations **15,600,000,000 (60.2%)**, total 25,925,000,000 | P1S01 l.205-223 | Medium |
| The company's reading of its own table | "although Europe has about three and a half times the telegraph traffic of the United States, and nearly twice the first class mail traffic, it has only two-fifths the telephone traffic of the United States"; and "The use of the telegraph in Europe was about 2 per cent, of the mails, while in the United States it was but 1 per cent., **the greater efficiency and distribution of the telephone causing the difference**" | P1S01 l.229-237 | Medium; the causal clause is a company assertion |
| Substitute/complement set sold against | 70,000 places reached by Bell toll lines vs "less than 60,000 post offices, 60,000 railroad stations and regular telegraph offices at about 25,000 places" | P1S01 l.163-168 | Medium |
| Market as capital | total capitalization of the system **$1,390,242,470**, "Of this $620,127,086 is owned and in the treasury of the companies of the Bell System"; capital stock, bonds and notes payable "outstanding in the hands of the public at the close of the year were $770,115,384"; with current accounts payable $26,471,681 the total obligations were $796,587,065, against liquid assets of $72,237,885, "leaving **$724,349,180** as the net permanent capital obligations of the whole system outstanding in the hands of the public" | P1S01 l.435-452 [SYSTEM] | Medium |
| The regulated-valuation event inside the window | "By Act of Congress approved March 1, 1913, the Interstate Commerce Commission is directed to make a valuation of all property owned or used by every common carrier under the jurisdiction of the commission, **which includes all the principal telephone companies**"; the company's engineers' appraisal says reproduction cost "would exceed their book cost by some $61,000,000" | P1S01 l.454-468 | Medium |
| The firm's own forward view of demand | "Estimates of all the associated operating companies and of the American Telephone and Telegraph Company for all new construction requirements in 1914 have been prepared. It is estimated that about **$56,000,000** will be required for current additions to plant in 1914, of which amount some $25,000,000 will be provided by the existing and current resources of the companies" | P1S01 l.339-354 | Medium; an **ESTIMATE printed by the company**, not a measurement |
| Long-run reinvestment behind the market | 1913 plant additions $54,871,856; "making a total for the fourteen years of **$646,915,200**" | P1S01 l.246, l.330-334 | Medium |
| What no held byte gives | any count of telephones **outside** the Bell System; any total U.S. demand; any price index; any competitor's revenue; any independent market estimate. The 2,717,808 contracted stations (§F) is the only figure that even partially sizes the non-Bell network, and it counts them **inside** the Bell report | — | High (of the silence over held bytes) |

**Adaptation note (§7).** For a network utility the "market as knowable in-period" is a **reach-and-rate** problem, not a unit-demand problem, and the registrant's own in-period framing says so: its case for the market is that the telephone has displaced the telegraph inside the United States (0.4% of messages vs 60.2% telephone) and that its plant must be re-built every few years to stay worth building. The knowability ceiling here is severe: **every market figure in this table is the company's own print**, so no row above is stronger than Medium and none is corroborated by a second origin.

### Claim records (§H)

H01 Claim: The registrant's own 1912 comparison put telephone conversations at 60.2% of U.S. messages of all three kinds, against 27.3% in Europe. — Date: 1912 — Source: P1S01 l.205-223 — Source date: 1914 — URL: https://archive.org/download/annualreportofdi00amer_14/annualreportofdi00amer_14_djvu.txt — Archived: — — Tier: 1 — Class: CONTEMPORANEOUS OBSERVATION (company-selected comparison) — Passage: "Telephone Conver sations . 6,809,000,000 27.3% 15,600,000,000 60.2%" — Conf: Medium — Corroboration: 0 independent — Conflicts: None

H02 Claim: The 1913 Act directing ICC valuation expressly reached the principal telephone companies, and the company answered with a reproduction-cost claim. — Date: 1913-03-01 — Source: P1S01 l.454-468 — Source date: 1914 — URL: as H01 — Archived: — — Tier: 1 — Class: FACT (of the statute's date and the company's statement); the $61,000,000 is a company ESTIMATE — Passage: "the Interstate Commerce Commission is directed to make a valuation of all property owned or used by every common carrier" — Conf: Medium — Corroboration: 1 (the Act's date is public law; the appraisal figure is the company's own) — Conflicts: None

H03 Claim: No held byte in this corpus gives a count of telephones outside the Bell System for any year in the window. — Date: 1875-01-01..1915-12-31 — Source: measurement over held bytes — Source date: 2026-10-06 — URL: file-local — Archived: — — Tier: 1 — Class: FACT (of a null over held bytes, not a corpus null; §S R-2/R-3 name the routes) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High — Corroboration: 1 — Conflicts: None

---

## I. COMPETITION

STATUS: WRITTEN 2026-10-06

**Person described: P2 vs the independent telephone companies; and P2's own operating-company family, which is a naming trap.** Every §I row below is carried either by a **hostile third party** (`P1S03`, 1908) or by the registrant's own regulatory settlement text (`P1S01`, 1913) — the two sources in this corpus that speak about competition at all.

### I.1 The competitive break, and its date as the record gives it

| Variable | Value | Source | Confidence |
|---|---|---|---|
| When competition opened | "**the original opening to competition after the expiration of the Bell patents in 1894**" — the only dated statement of the patent cliff anywhere in held bytes, and it is a competitor's, not the company's | P1S03 l.190-193 | Medium |
| When independents entered | "The Independent companies going into the field from **1895 to 1900** foresaw a greater development at a lower price and in their construction provided for a great deal of new territory and a larger number of telephones in existing territory" | P1S03 l.1027-1035 | Medium |
| The opponent's account of Bell's monopoly period | "The Bell companies, in their period of monopoly, evidently proceeded on the theory of treating the telephone as a luxury, to be used by the few who could afford a high price"; and "many inventions, which have since proved their value, were ignored or bought cheaply and shelved in the days of monopoly" | P1S03 l.1024-1027, l.1166-1168 | Medium; **an interested party's characterisation** |
| A named price of the monopoly period | "For several years after the Citizens Company in Columbus was providing with all instruments the so-called long-distance transmitter (purchased in the market at $1.75), the Central Union Company was charging an extra twelve dollars a year for service of the same grade as the Citizens service" | P1S03 l.1158-1162 | Medium |
| Bell's counter-argument in the corpus | the duplication argument printed at `P1S03` l.242-251 (see the §F attribution warning and §U.9); and in the registrant's own 1913 report the competition answer is **the interconnection schedule**, which prices and bounds what an independent may sell | P1S01 l.1750-1817 | Medium |
| Competitor named and dated twice, from two sides | **Central Union Telephone Company** — its own 1907 printed report, quoted by the pamphlet: "has not been making returns on the investment for the **past twelve years**, and it cannot expect to make any return whatever until rates are raised" (`P1S03` l.670-674); and in 1913 P2 "consented to the appointment of receivers" in a Chicago action involving it (`P1S01` l.1660-1668). The "twelve years" dates Central Union's loss-making to ≈1895 on the competitor's own words | both | Medium |
| A court holding in P2's favour inside the window | "The Supreme Court of California has sustained the contention of the Company upon an important question… that there is not power to order a physical connection except upon provision for compensation for the use of the property of this Company which such a connection involves" | P1S01 l.1670-1675 | Medium |
| Alleged methods, asserted by the opponent | "purchases at high prices of competing plants in the vain expectation of stopping competition"; "an organized department endeavoring, by threat and persuasion, to break down the continuity of Independent exchanges and toll lines by monopolizing strategic points"; "circulation of papers and pamphlets designed to influence the public mind toward monopoly" | P1S03 l.745-768 | Low as fact, **Medium as evidence that a competitor could print this in 1908** |
| **Naming trap, enforced** | "Pacific Bell Telephone Company and Southwestern Bell Telephone Company … Illinois Bell Telephone Company, Indiana Bell Telephone Company, Inc., Michigan Bell Telephone Company, The Ohio Bell Telephone Company" (`P1S07` l.1266 area) and "Bell Telephone Company" ×**32** across the seven cited SEC documents (measured this pass) are **operating-company names of the Bell family, not the registrant's ancestor**. "Southwestern Bell" ×**207** in the same subset is **P4's own** operating company and has no bearing on 1875–1915 | P1S07 | High (that the strings are a family list) |

### I.2 What the competition did to the registrant, measurably, in the held record

The one series in the corpus that behaves like a competitive signal is **average revenue per exchange station of the associated operating companies** across five years: 1895 **$81.10**, 1900 **$57.28**, 1910 **$40.75**, 1912 **$40.14**, 1913 **$39.48** (`P1S01` l.1043-1049; caption "Average Operating Units of Associated Operating Companies, 1895 to 1913", scope note excluding "the long-distance lines of American Telephone and Telegraph Co.", l.1029-1038). **DERIVED: −51.3% from 1895 to 1913** (`(39.48 − 81.10) ÷ 81.10`); the toll component fell from $11.35 to $9.03 over the same span (**DERIVED −20.4%**), while the exchange component fell from $69.75 to $30.45. The entry years of the independent wave (1895–1900) and the collapse in revenue per station coincide in the company's own table. **That is a coincidence of two company-printed series, not a demonstrated causal effect:** no held byte attributes the decline to competition, and the pamphlet attributes the Bell price structure to policy rather than to cost. Stated as **INFERENCE, Low**, with the alternative explanation (scale — new subscribers being added at the low end of demand, which the same table's station-growth rows would support) left open because nothing in the corpus can exclude it.

### Claim records (§I)

I01 Claim: The dated opening of competition in the held corpus is 1894, the expiration of the Bell patents, and it is stated by a competitor, not by the registrant. — Date: 1894 — Source: P1S03 — Source date: 1908-09 — URL: https://archive.org/download/somecommentsona00chicgoog/somecommentsona00chicgoog_djvu.txt — Archived: — — Tier: 3 (trade-association print) — Class: CONTEMPORANEOUS OBSERVATION by an interested party — Passage: "the expiration of the Bell patents in 1894" — Conf: Medium — Corroboration: 1 independent; the registrant's own print does **not** state it — Conflicts: None

I02 Claim: Average earnings per exchange station of the associated operating companies fell from $81.10 in 1895 to $39.48 in 1913 on the company's own table. — Date: 1895..1913 — Source: P1S01 l.1043-1049 — Source date: 1914 — URL: as H01 — Archived: — — Tier: 1 — Class: FACT as printed; the decline DERIVED; the competition explanation **INFERENCE, Low** — Passage: "Total . $ 81.10 8 57.28 8 40.75 8 40.14 8 39.48" — Conf: Medium (values); Low (mechanism) — Corroboration: 0 independent — Conflicts: None

I03 Claim: In 1913 the registrant consented to the appointment of receivers over a competitor's Chicago property rather than settle on terms it thought sustainable. — Date: 1913 — Source: P1S01 l.1660-1668 — Source date: 1914 — URL: as H01 — Archived: — — Tier: 1 — Class: CONTEMPORANEOUS OBSERVATION — Passage: "The Company therefore consented to the appointment of receivers, and the court has appointed capable men who are now taking charge of the property" — Conf: Medium — Corroboration: 1 independent in kind (P1S03 l.670-674 documents the same company's 1907 distress from the opposite side) — Conflicts: None

## J. TECHNOLOGY

STATUS: WRITTEN 2026-10-06

**Person described: P2's engineering programme, with Western Electric as the manufacturing counterpart.** The window's technology story is a **transmission-loss story**, and the corpus is unusually good on it because the 1887 document records the arguments while they were still uncertain.

| Variable | Value | Source | Confidence |
|---|---|---|---|
| The binding constraint, as stated in 1913 | "one mile of underground cable is often equal to 50 or 100 miles of open wire overhead, and in underground transmission a point was soon reached where no speech could be got by any transmitter"; "the problem of talking through long underground cables or over great distances could not be solved by increasing the loudness of the transmitter or the receiver" | P1S01 l.1394-1398, l.1386-1389 | Medium |
| The route out, in order | twisted-pair underground conductor (1887, whose adoption "meant the abandonment of the entire underground plant of the Bell System") → Pupin loading coils (by 1902) → loaded suburban cable New York–Newark (1902) → 20-mile loaded cable (1905) → 90-mile cable New York–Philadelphia (1906) → a cable designed for Washington–Boston (1911) → laid and talked Boston–Washington (1912–1913) → **the same loading and balancing theory transferred to overhead** by the New York–Denver study (1913) | P1S01 l.1431-1511 | Medium; registrant-retrospective for 1887–1912, contemporaneous for 1913 |
| Why the mix of cable generations is the point | the 1913 Boston–Washington success was achieved "in part through types of cable formerly suitable for short haul distances only. **These short haul cables make up 47 per cent, of the total cable in the line**" — network capability is set by the intermediate plant, not by the newest segment | P1S01 l.1479-1483 | Medium |
| Circuit engineering detail held | conductors **transposed about every sixty feet** in the Edison system; spacing ½ inch in the 1887 Dorsett cables; static capacity in microfarads per mile (0.25 and 0.40 in the two systems); insulation in megohms per mile, tracked seasonally ("during last summer in very hot weather the insulation was as low as 45 megohms per mile. The tests in the following winter, however, showed that the insulation was very nearly up") | P1S02 l.4599-4626, l.4890-4895 | Medium |
| The failure modes named as physical, not commercial | water entering an oil-filled iron pipe; creosoted-wood conduit suspected of attacking insulation from the exterior inward ("the manufacturer attributes this result to placing the cable in a conduit made of creosoted wood… the tests have not yet been completed and our investigations may lead to a different conclusion as to the cause of failure"); terminal boxes impossible to make perfect on aerial cable; lead-sheath corrosion | P1S02 l.4636-4641, l.7055-7064, l.4646-4650, l.5038-5048 | Medium |
| Switching | "We have designed, manufactured and installed all kinds of switchboards — automatic, semi-automatic and manual — and we have exhaustively studied the practical workings of every type of switchboard in use"; and the answer to the patent-suppression charge: "The Bell Company owns or has rights in every United States patent and patent application which would be necessary to operate its system upon the so-called automatic plan— **which is not automatic for the subscriber** as the subscriber does all the manipulation in the making of a connection. As yet it has not been demonstrated that the automatic system would give as good and dependable service as we now render to the public" | P1S01 l.1521-1541 | Medium |
| Human-capital origin of the function, as the company tells it | "At the beginning of the telephone industry there was no art of electrical engineering nor was there any school or university conferring the degree of electrical engineer. Notwithstanding this, the general engineering staff was soon organized, calling to their aid some of the most distinguished professors of science in our universities" — ending at 550 engineers and scientists at headquarters | P1S01 l.1543-1556 | Medium; a company's account of its own history |
| Instrument turnover as an engineering fact | 53 receiver types and 73 transmitter types designed, constructed and installed "from 1877 to 1914"; 12,000,000 instruments owned, "practically none… made prior to 1902", average age under five years | P1S01 l.1368-1383 | Medium |
| Depreciation as an engineering policy | "The necessity of providing fully for that depreciation which comes from **obsolescence** continues and will continue so long as the improvement of the equipment, apparatus and service, and increase in possible distance of communication continue"; and the standard argument that a plant giving "limited local service" "would be useless in a comprehensive system", so "the Bell plant must be maintained at a higher standard than would be necessary if it were a purely local exchange service" | P1S01 l.366-384 | Medium |
| What the corpus does **not** contain | any patent number, any patent-holder name, the word "transcontinental", any description of the 1915 line's construction, and any technical statement of the Pacific route. `patent` appears in the 1887 conference report exactly once, in an unrelated list of other work | P1S01 / P1S02 measurements this pass | High (of the silence over held bytes) |

### Claim records (§J)

J01 Claim: The company's own print attributes the 1913 Boston–Washington underground success to intermediate loading and balancing, and states that 47% of the cable in that line was of short-haul types. — Date: 1913 — Source: P1S01 l.1476-1483 — Source date: 1914 — URL: as H01 — Archived: — — Tier: 1 — Class: CONTEMPORANEOUS OBSERVATION — Passage: "These short haul cables make up 47 per cent, of the total cable in the line." — Conf: Medium — Corroboration: 0 independent — Conflicts: None

J02 Claim: The registrant met the charge of patent-suppressed automatic switching by asserting it held the necessary rights and that the automatic plan was not demonstrated to be as good. — Date: 1913 — Source: P1S01 l.1530-1541 — Source date: 1914 — URL: as H01 — Archived: — — Tier: 1 — Class: CONTEMPORANEOUS OBSERVATION plus company assertion — Passage: "As yet it has not been demonstrated that the automatic system would give as good and dependable service as we now render to the public" — Conf: Medium — Corroboration: 0 independent; the charge itself is `P1S03` l.1166-1168 — Conflicts: None

J03 Claim: The 1887 house document treats cause-of-failure as unsettled at the time of printing. — Date: 1887-09 — Source: P1S02 l.7058-7064 — Source date: 1887 — URL: as C01 — Archived: — — Tier: 1 — Class: CONTEMPORANEOUS OBSERVATION — Passage: "the tests have not yet been completed and our investigations may lead to a different conclusion as to the cause of failure" — Conf: Medium — Corroboration: 1 independent in-document (the Boston reply at l.7096-7115 records a different failure set from a different company) — Conflicts: None

---

## K. MONEY

STATUS: WRITTEN 2026-10-06

**Person described: P2.** Two registers again, kept apart: **[SYSTEM]** (duplications eliminated) and **[COMPANY]** (the registrant's own accounts). All are capped at Medium by the transport caveat (§Header 5) even where they cross-foot exactly (§K.3) — the cap is on the bytes' provenance, not on the arithmetic.

### K.1 The registrant's own money for the year (COMPANY)

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Net earnings | **$40,576,746.19**, "an increase of $2,669,101.93 over 1912" | P1S01 l.1252-1254 | Medium |
| Interest charges | $7,656,655.78 | P1S01 l.1255 | Medium |
| Dividends at the regular rate | **$27,454,037.15**, "at the regular rate of 8 per cent, per annum" | P1S01 l.1255-1256 | Medium |
| Balance and its split | "Of the balance, $5,466,053.26, there was carried to Reserves $2,500,000 and to Surplus $2,966,053.26" | P1S01 l.1256-1258 | Medium |
| Earnings composition | 1913: dividends $26,122,572.81; interest and other revenue from associated companies $13,564,952.47; **telephone traffic (net) $5,548,089.00**; other sources $674,377.34. 1912: $24,247,430.02 / $12,523,084.45 / $5,472,812.66 / $474,665.62 | P1S01 l.5144-5164 | Medium |
| Total assets = total liabilities | $655,956,307.97 both sides at 1913-12-31, signed beneath by the Comptroller | P1S01 l.5067, l.5129, l.5132 | Medium |
| Capital stock outstanding | $344,616,300.00, against **$369,136,414 paid into the treasury**: "the $24,520,114 in excess of par value represents premiums. All discounts on the bond issues have been charged off" | P1S01 l.1300-1305, l.5076 | Medium |
| Total outstanding stock and bonds | **$504,207,300** = Capital Stock 344,616,300 + 4% Collateral Trust Bonds 78,000,000 + 4% Convertible 4,591,000 + 5% Western Tel. & Tel. Co. Bonds 10,000,000 + 4½% Convertible Bonds 1933 67,000,000 | P1S01 l.1278-1298 | Medium |
| 1913 capital events | "$9,809,700 of stock was issued upon conversion of the 4 per cent, bonds of 1906, and in addition $900 of new stock… making the total increase of capital stock during 1913, $9,810,600"; "of the $150,000,000 of convertible bonds of 1906 had been handed in for conversion, leaving outstanding at the end of the year $4,591,000, a reduction in 1913 of $12,411,000" | P1S01 l.1262-1272 | Medium |
| Liquidity position | Cash and deposits $22,199,227.64; **Special Demand Notes $34,311,230.41** — more than the cash line | P1S01 l.5060-5062 | Medium |
| A cross-holding stated on its face | "**Indebtedness to Western Union Telegraph Co. for New York Telephone Co. Stock Payable 1914 to 1915** … 4,000,000.00" — the same Western Union whose stock the December 1913 letter promised to dispose of | P1S01 l.5089-5091, l.1711-1716 | Medium; §N, §U.6 |
| Dividend declared across the stage edge | "Dividend Payable January 15, 1914 … $6,892,326.00" | P1S01 l.5103 | Medium |
| Reserve and surplus (company) | Reserve for Depreciation and Contingencies $36,836,187.51; Surplus $63,655,972.63; Employees' Benefit Fund $2,035,652.99 | P1S01 l.5116-5126 | Medium |

### K.2 The system's money (SYSTEM), and the reinvestment policy

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Gross earnings | 1912 $199,172,154 → 1913 **$215,572,822** (+$16,400,668); the prose of the same report prints "$215,600,000" and "an increase of over $16,000,000" | P1S01 l.494-506 vs l.423-425 | Medium; §U.5 |
| Expenses of 1913 | Operation $75,404,092; current maintenance $32,442,979; depreciation $37,739,991; taxes $11,296,237; **total $156,883,299** | P1S01 l.508-541 | Medium |
| Net and its distribution | Net earnings $58,689,523; interest $16,652,624; balance net profits $42,036,899; dividends paid $30,301,705; **surplus earnings $11,735,194** (1912: $13,221,110) | P1S01 l.543-577 | Medium |
| Combined balance sheet 1913 | Plant $797,159,487; supplies $20,083,113; receivables $40,349,027; cash $31,888,858; stocks and bonds $90,523,610; **total $980,004,095**. Liabilities: capital stock $395,224,531; funded debts $341,147,485; bills payable $33,743,368; accounts payable $26,471,681 → outstanding obligations $796,587,065; Employees' Benefit Fund $8,919,335; surplus and reserves $174,497,695 | P1S01 l.582-694 | Medium |
| Reinvestment charged to revenue | "During the year **$70,183,000** was applied out of revenue to maintenance and reconstruction purposes; of this, over $13,000,000 was unexpended"; "The total provision for maintenance and reconstruction charged against revenue for the last ten years was over **$457,000,000**" | P1S01 l.358-364 | Medium |
| The financing policy stated outright | "The policy of investing the depreciation reserve in revenue-earning plant has continued, and the public is getting the advantage of the use of a large amount of plant upon which **no dividends or interest charges have to be earned**"; "All of the present surplus and reserves, aggregating over $174,000,000, is invested in tangible and productive property" | P1S01 l.402-406, l.710-714 | Medium |
| Ratio defence offered to the regulator | "Net earnings to plant and other assets . 5.69%" ; "Dividends and interest to plant and other assets . . . 4.92%" | P1S01 l.997-1004 | Medium |
| Six-year retrospective | gross +$87,000,000, "of which $69,500,000 has been absorbed by increase in expenses", net +$17,500,000, interest +$6,100,000, dividends +$12,200,000; assets + nearly $367,000,000 against capital obligations + less than $245,000,000; surplus and reserves $61,300,000 → $174,500,000 | P1S01 l.716-731 | Medium |
| Founder's / officers' personal money | **UNKNOWN in every respect.** No held byte states any officer's or founder's compensation, share purchase, or personal stake. The nearest incorporation-with-capital figure in the whole held non-SEC corpus belongs to a different company: the Chicago & Milwaukee Telegraph Line, "incorporated with a stock of $50,000… reorganized with a stock of $50,000 and $50,000 of bonds" | P1S01 l.2985-3010 | **UNKNOWN**; §U.8 |

### K.3 Arithmetic performed on the held print (all DERIVED; nothing substituted)

| Check | Arithmetic | Result |
|---|---|---|
| Company income statement closes | 40,576,746.19 − 7,656,655.78 − 27,454,037.15 = **5,466,053.26**; and 2,500,000 + 2,966,053.26 = **5,466,053.26** | **foots exactly** |
| Company earnings composition | 26,122,572.81 + 13,564,952.47 + 5,548,089.00 + 674,377.34 = **45,909,991.62**; telephone-traffic share = 5,548,089.00 ÷ 45,909,991.62 = **12.1%** | foots; the share is the §A.1 structural finding |
| Capital-stock premium | 369,136,414 − 344,616,300 = **24,520,114** | foots to the printed premium |
| Bond-conversion residual | 150,000,000 − 145,409,000 = **4,591,000** | foots |
| Outstanding stock and bonds | 344,616,300 + 78,000,000 + 4,591,000 + 10,000,000 + 67,000,000 = **504,207,300** | foots |
| Company asset side | 530,984,879.14 + 64,056,281.87 + 22,199,227.64 + 34,311,230.41 + 4,404,688.91 = **655,956,307.97** | foots |
| Company liability side | 344,616,300 + 197,896,000 + 10,916,194.84 + 2,035,652.99 + 100,492,160.14 = **655,956,307.97** | **both sides foot to the same total** |
| Company funded-debt line | 78,000,000 + 4,591,000 + 67,000,000 + 10,000,000 + 5,000 + 4,000,000 + 19,300,000 + 15,000,000 = **197,896,000** | foots; note this line is **wider than** the "capital stock and bonds" table at l.1278-1298 because it includes notes to associated companies — a definitional difference, recorded so it is not later read as an inconsistency |
| System expense build | 75,404,092 + 32,442,979 + 37,739,991 + 11,296,237 = **156,883,299**; 215,572,822 − 156,883,299 = **58,689,523**; − 16,652,624 = **42,036,899**; − 30,301,705 = **11,735,194** | foots end to end |
| System balance sheet, both years | 742,287,631 + 23,601,262 + 37,700,623 + 35,729,037 + 84,942,265 = **924,260,818**; 797,159,487 + 20,083,113 + 40,349,027 + 31,888,858 + 90,523,610 = **980,004,095**; liabilities 393,209,925 + 294,380,353 + 38,268,341 + 25,320,335 = **751,178,954** and 395,224,531 + 341,147,485 + 33,743,368 + 26,471,681 = **796,587,065** | foots; and 796,587,065 − 751,178,954 = **45,408,111**, exactly the printed increase (l.476-477) |
| **The one check that does not foot** | daily average 27,237,000 × 365 = **9,941,505,000** against the printed "about 8,770,300,000 per year" (l.194-196) | **does not foot** (the printed annual figure implies ≈322 days). No value substituted; §U.5 |
| Dividend-rate coherence | $6,892,326.00 payable 1914-01-15 × 4 = $27,569,304 against the printed $27,454,037.15 of 8%-rate dividends; implied average stock base 27,454,037.15 ÷ 0.08 = **$343,175,464** vs year-end stock $344,616,300 | coherent with the $9,810,600 of stock issued during the year — **not a defect**; recorded so a later pass does not "correct" it |

**§6 basis note, applied to every §K row:** all figures are **nominal U.S. dollars of the stated year**, unadjusted; fiscal year = calendar year ended 12-31; "[SYSTEM]" vs "[COMPANY]" as labelled per row; none is per-share, inflation-rebased, or independently attested. The 1913 gross-revenue line is a **total for the year**, not a run-rate; the 1914 $56,000,000 is the company's own **estimate**, not a plan with a date of adoption.

### Claim records (§K)

K01 Claim: The registrant's own FY1913 accounts close exactly, on the print, to a $5,466,053.26 balance split between reserves and surplus. — Date: 1913-12-31 — Source: P1S01 l.1252-1258 — Source date: 1914 — URL: as H01 — Archived: — — Tier: 1 — Class: FACT as printed; footing DERIVED by this pass — Passage: "there was carried to Reserves $2,500,000 and to Surplus $2,966,053.26" — Conf: Medium (capped by transport, not by arithmetic) — Corroboration: 0 independent — Conflicts: None

K02 Claim: The registrant's balance sheet is dominated by associated-company paper, its own working plant being small against it. — Date: 1913-12-31 — Source: P1S01 l.5028-5067 — Source date: 1914 — URL: as H01 — Archived: — — Tier: 1 — Class: FACT as printed; ratio DERIVED (530,984,879.14 ÷ 655,956,307.97 = 81%) — Passage: "Stocks of Associated Companies . $454,307,263.79" — Conf: Medium — Corroboration: 0 independent — Conflicts: None

K03 Claim: The company's stated financing policy was to reinvest the depreciation reserve in revenue-earning plant, so that part of the plant carries no capital charge. — Date: 1913-12-31 — Source: P1S01 l.402-406 — Source date: 1914 — URL: as H01 — Archived: — — Tier: 1 — Class: CONTEMPORANEOUS OBSERVATION (a policy the company asserts about itself) — Passage: "The policy of investing the depreciation reserve in revenue-earning plant has continued" — Conf: Medium — Corroboration: 0 independent — Conflicts: None

K04 Claim: No held byte states any officer's or founder's compensation or personal stake inside the window. — Date: 1875-01-01..1915-12-31 — Source: measurement over held bytes; the only incorporation-capital figure held belongs to another company — Source date: 2026-10-06 — URL: file-local — Archived: — — Tier: 1 — Class: **UNKNOWN**, recorded as a finding — Passage: "incorporated with a stock of $50,000" — Conf: High (of the silence) — Corroboration: 0 — Conflicts: U.8

K05 Claim: The registrant's 1913 indebtedness to Western Union for New York Telephone Co. stock was scheduled to fall due across 1914–15, in the same year it promised to release its Western Union control. — Date: 1913-12-19 / 1913-12-31 — Source: P1S01 l.5089-5091, l.1711-1716 — Source date: 1914 — URL: as H01 — Archived: — — Tier: 1 — Class: FACT as printed (two lines of one document) — Passage: "Indebtedness to Western Union Tele graph Co. for New York Telephone Co. Stock Payable 1914 to 1915. . . . 4,000,000.00" — Conf: Medium — Corroboration: 0 independent — Conflicts: U.6

## L. VALIDATION SIGNALS

STATUS: WRITTEN 2026-10-06

**Person described: P2.** No signal below has a second origin, and one of them (§L.1 row 6) is a **documentary** validation rather than an economic one — the accounts cross-foot. That distinction is kept explicit because a dossier that reports internal arithmetic as market proof is the hindsight defect in disguise.

| # | Date | Signal | Magnitude | What it demonstrated | What it did NOT demonstrate | Source / class / confidence |
|---|---|---|---|---|---|---|
| L-1 | 1912 | Talking underground for the first time between New York and Washington | "represented the longest distance underground yet achieved" | that the loading-and-balancing programme cleared its own stated test at ~200 miles | durability, cost, or commercial dependability; the sentence is the company's | P1S01 l.1485-1487 · CONTEMPORANEOUS (retrospective by weeks) · Medium |
| L-2 | 1913 | Satisfactory conversation by underground wire **Boston–Washington**, "in part through types of cable formerly suitable for short haul distances only" | distance "had been doubled" in one year; the cable "several times longer than any other in the world" | that the art now solves a multi-hundred-mile underground circuit, mixing cable generations | anything about 1915 or the Pacific; and no cost/price of the achievement | P1S01 l.1476-1490 · CONTEMPORANEOUS · Medium |
| L-3 | 1913-12-19 | The Administration accepted the company's five-point course of action; the Attorney General replied the same day and the President's note was printed in the report | one letter, one acknowledgement, one presidential endorsement, all dated the same day | that a litigated federal conflict was settled **without litigation**, on the company's stated terms of compensation and control | that the settlement improved demand, or that the independents accepted its fairness — `P1S03` shows the opposite view being printed in 1908 | P1S01 l.1696-1890 · CONTEMPORANEOUS, two voices · Medium |
| L-4 | 1913-12-31 | Shareholder count | 55,983, +5,686 in the year; 49,144 below 100 shares; less than 6% in brokers' names | that the equity was being absorbed by small permanent holders rather than dealers — the funding base is stable | that the stock was fairly valued; and any return to those holders beyond the printed 8% | P1S01 l.1307-1330 · CONTEMPORANEOUS self-report · Medium |
| L-5 | 1913 | Subscriber growth of the system | +676,943 stations to 8,133,017 (**DERIVED +9.1%**: 676,943 ÷ (8,133,017 − 676,943)); wire mileage +1,500,198 to 16,111,011 | repeat purchase at scale across the whole network | margin: the same year's surplus earnings **fell**; and revenue per station kept falling (§I.2) | P1S01 l.153-155, l.176-178 · CONTEMPORANEOUS · Medium |
| L-6 | 1914 (print of FY1913) | The held accounts cross-foot on every line tried | 10 of 11 checks foot exactly; 1 does not (§U.5) | that the document is internally coherent — a **documentary** validation of the bytes, not of the business | nothing at all about the market; an internally consistent document can still mislead | this pass §K.3 · DERIVED by this pass · High (the arithmetic), Medium (the underlying figures) |
| L-7 | 1913 | Self-financing capacity asserted | $70,183,000 applied out of revenue to maintenance and reconstruction; $25,000,000 of the 1914 estimate to come "from the existing and current resources of the companies" | that the programme could be funded internally | that it was in fact so funded — 1914 lies outside the window and no held byte reports it | P1S01 l.358, l.352-354 · CONTEMPORANEOUS · Medium |

### Claim records (§L)

L01 Claim: The registrant's own FY1913 print certifies satisfactory underground conversation between Boston and Washington. — Date: 1913 — Source: P1S01 l.1476-1490 — Source date: 1914 — URL: as H01 — Archived: — — Tier: 1 — Class: CONTEMPORANEOUS OBSERVATION — Passage: "it is now possible to talk satisfactorily by underground wires from Boston to Washington" — Conf: Medium — Corroboration: 0 independent — Conflicts: None

L02 Claim: The December 19, 1913 settlement was accepted by the Administration and endorsed by the President in print the same day. — Date: 1913-12-19 — Source: P1S01 l.1696-1890 — Source date: 1914 — URL: as H01 — Archived: — — Tier: 1 — Class: FACT (three documents printed together, two of them by the government) — Passage: "it seems to me clear that such action on your part will establish conditions under which there will be full opportunity throughout the country for competition in the transmission of intelligence by wire" — Conf: Medium — Corroboration: 2 origins inside one printed sequence (the company's letter and the Attorney General's reply are separately authored) — Conflicts: U.6

---

## M. NEGATIVE SIGNALS / FAILURES

STATUS: WRITTEN 2026-10-06

**Person described: P2 (and, in two rows, other people's failures that P2 absorbed or watched).** This is the strongest §M section in this company's dossier: the 1887 house print records **incurred engineering failures while they were happening**, with supplier names, lengths and dates, and no hindsight.

| # | Date | Failure | Magnitude as printed | Carrier / class / confidence |
|---|---|---|---|---|
| M-1 | 1885–1887 | A Brooks cable "laid up with tinsel braid interspersed amongst the wires … **proved to be so defective from the start that we have never been able to use it to any great extent; we have never connected more than 15 wires through it**" | lengths of 900 feet and 4,500 feet | P1S02 l.4879-4885 · CONTEMPORANEOUS · Medium |
| M-2 | 1886–1887 | Lead-sheath corrosion: "The Brooks cable at the end of eight months was found to be badly corroded, a crust of what proved to be carbonate of lead forming on the outside in that time 44 [sic] of an inch thick, cracking and peeling off whenever the cable was handled. **Six hundred feet of this cable was drawn out on account of defective insulation and replaced by another** … This also has corroded badly… with every prospect that it will continue until the lead is destroyed" | ~9,400 feet still in service under active corrosion | P1S02 l.5038-5048 · CONTEMPORANEOUS · Medium |
| M-3 | 1884–1887 | The Boston 1883 cable group: "The Phillips cable gave out in September, 1884, and the two Clark cables in March, 1885, on account of defective insulation. The two latter cables were removed at the time, but the former was **not removed until February, 1887**, as it could not be conveniently taken out until that time, and **the covering was found to be badly rotted in many places**" | 4 Patterson lead + 1 Day kerite + 1 rubber (Feb 1883) and 2 Clark rubber (Apr 1883); the letter's own print reads "April, 1853" for the Clark pair — an OCR defect, §U.5 | P1S02 l.7096-7112 · CONTEMPORANEOUS, from a **different company's** reply · Medium |
| M-4 | 1883 | The first long Boston cable did not work as hoped: "In 1883 several cables were laid at Boston, the longest of which was 1,500 feet. The subscribers using this cable **could not talk satisfactorily further than the suburbs**" | 1,500 feet | P1S01 l.1418-1426 · registrant-retrospective · Medium |
| M-5 | 1887 | Wholesale obsolescence, asserted by the company: the twisted pair "meant **the abandonment of the entire underground plant of the Bell System**"; and "Type after type of cable was installed only to be withdrawn in a few years and replaced by something better" | "Millions of dollars were spent in this construction and reconstruction and experimental work" | P1S01 l.1431-1438 · registrant-retrospective, no independent count of the abandoned plant · Medium (that the claim was made); **UNKNOWN** (its magnitude) |
| M-6 | 1905–1907 | The corpus's first **incurred commercial failure**: "THE CHICAGO & MILWAUKEE TELEGRAPH LINE. THE TRUE STORY." — "Built in 1878 by some linemen as a speculation, it was sold to some members of the boards of trade of Chicago and Milwaukee and incorporated with a stock of $50,000… later on the company was reorganized with a stock of $50,000 and $50,000 of bonds… operated until 1905, when it went into **receivership**… until 1907, when it was offered for sale, and the Chicago and the Wisconsin Telephone Companies… purchased it in connection with the American Telephone and Telegraph Company, for toll and long-distance telephone business" | $50,000 stock, then $50,000 stock + $50,000 bonds; 27 years from speculation to sale | P1S01 l.2985-3020 · appendix reprint inside the registrant's own print · Medium |
| M-7 | 1913 | A competitor's property taken out of the market: the Chicago action "involving the relations between this Company and the Central Union Telephone Company… It was impossible to adjust this matter upon any reasonable basis and it seemed that the ultimate outcome would render a reorganization of the Central Union Telephone Company necessary. The Company therefore consented to the appointment of receivers" | territory "most of Ohio and Indiana and part of Illinois, not including Cleveland, Cincinnati or Chicago" | P1S01 l.1660-1668 (with P1S03 l.670-674, l.698) · CONTEMPORANEOUS · Medium |
| M-8 | 1913 | Earnings direction: system **surplus earnings fell** to $11,735,194 from $13,221,110, and the balance of net profits fell $644,426, in a year when gross rose $16.4M | as printed | P1S01 l.560-577 · CONTEMPORANEOUS · Medium |
| M-9 | 1913 | A company-observed failure of *other people's* technology: "Failure to understand this has been the **cause of loss to many who have invested in companies promoting so-called loud-speaking telephones**" | unquantified | P1S01 l.1389-1392 · CONTEMPORANEOUS, self-serving · Medium (that it was printed); UNKNOWN (the losses) |
| M-10 | 1907–1908 | The independents' own collapse, printed by one of their number: "The result has been unfortunate in nearly every case… Most, if not all, of these companies… are now **asking for increased rates**, and to be absolved from onerous conditions freely accepted and assumed at the beginning. **Reorganizations are now in progress**" | the whole 1895–1900 promotion wave | P1S03 l.219-229 · CONTEMPORANEOUS by an interested party · Medium |

**Refusals recorded here, because §M is where dossiers get them wrong.** (i) **The 1984 divestiture is not written as a failure** — it is out of this stage's window, and it is a two-person separation (§U.4), not an amputation-of-blame. (ii) **P4 has no failure in this window because P4 did not exist.** (iii) M-5's "abandonment of the entire underground plant" is **not** converted into a dollar impairment: no held byte states the amount, and an unsourced impairment figure would be the invention this project pays auditors to catch.

### Claim records (§M)

M01 Claim: The registrant's own 1887 print records six hundred feet of cable drawn out for defective insulation and a replacement that was also corroding. — Date: 1886..1887 — Source: P1S02 l.5038-5048 — Source date: 1887 — URL: as C01 — Archived: — — Tier: 1 — Class: CONTEMPORANEOUS OBSERVATION — Passage: "Six hundred feet of this cable was drawn out on account of defective insulation and replaced by another" — Conf: Medium — Corroboration: 1 independent in kind (M-3's separate company reply records the same class of failure in Boston) — Conflicts: None

M02 Claim: The only incorporation-with-a-capital-figure in the held non-SEC corpus is another company's, and that company failed. — Date: 1878 (incorporation) / 1905 (receivership) / 1907 (sale) — Source: P1S01 l.2985-3020 — Source date: 1914 — URL: as H01 — Archived: — — Tier: 1 — Class: FACT (of what the reprint says); the "true story" framing is a polemic title, not a company statement — Passage: "it was sold to some members of the boards of trade of Chicago and Milwaukee and incorporated with a stock of $50,000" — Conf: Medium — Corroboration: 0 independent — Conflicts: U.8

M03 Claim: The registrant consented in 1913 to receivers over a competitor's property instead of settling. — Date: 1913 — Source: P1S01 l.1660-1668 — Source date: 1914 — URL: as H01 — Archived: — — Tier: 1 — Class: CONTEMPORANEOUS OBSERVATION — Passage: "The Company therefore consented to the appointment of receivers" — Conf: Medium — Corroboration: 1 in kind (P1S03 on the same company's 1907 condition) — Conflicts: None

---

## N. DECISIONS (FOUNDER DECISIONS — ADAPTED: THERE IS NO FOUNDER IN THIS RECORD)

STATUS: WRITTEN 2026-10-06

**Person described: P2, acting through named officers.** §7's "founder decisions" frame does not apply to a registrant created by incorporation in 1885 and run by a slate of officers in 1913; the adapted equivalent is **decisions of record**, each with a carrier and, where the print gives one, a signatory. Where no decision-maker is named, that is written, not inferred.

| Date | Decision | State before | Information available | Unknowns | Alternatives | Constraints | Rationale | Expected result | Actual result | Evidence / conf |
|---|---|---|---|---|---|---|---|---|---|---|
| 1887-09-07 | Convene a three-day cross-company engineering conference and **print its proceedings without publishing them** ("PRINTED, NOT PUBLISHED") | cable practice varied by company and by supplier; insulation and crosstalk failures were being absorbed locally | the participants' own tests; "how few sources of information are open in electrical literature" | who decided to convene it; cost; how many copies circulated | meet informally and not record; write separately to each company | a house print the company chose not to publish | "we will have in the report of this meeting a large amount of valuable data preserved in a permanent form available for future reference" | a shared basis for specification | cannot be assessed in-window; the report survives as bytes | P1S02 l.15, l.361-392 · Medium (decision), UNKNOWN (decision-maker) |
| 1887 (as dated by the company in 1913) | Adopt the twisted-pair underground conductor, accepting that it "meant the abandonment of the entire underground plant of the Bell System" | an installed underground plant of unquantified book value | comparative performance of types in service | who authorised it; the amount abandoned; whether the choice was contested | continue patching existing types | capital at risk; service continuity | new type "without which the telephone system as we know it to-day would be an impossibility" | a plant capable of long underground circuits | the 1902–1913 loading programme proceeded on that plant | P1S01 l.1431-1438 · registrant-retrospective, Low as to agency, Medium as to the claim being made |
| 1911–1913 | Design and lay progressively longer loaded underground cable (Washington–Boston capable design, then New Haven–Providence) | a 90-mile cable usable only New York–Philadelphia | the company's own transmission calculations | internal debate; budget lines; rejected routes | keep extending overhead only | copper cost; conduit access; storm damage to overhead | to isolate "seaboard cities from Washington to Boston" from "storms destroying the overhead wires" | dependable multi-hundred-mile circuits | achieved in 1913 on the company's own statement | P1S01 l.1450-1474 · Medium |
| **1913-12-19** | **Accept all of the Attorney General's suggestions** as a five-point course of action: dispose of **all Western Union stock**; **cease acquiring control** of competing telephone companies; open **toll interconnection** to independents on stated terms (standard trunk lines at the independent's cost, Bell control of the whole toll circuit, >50-mile scope, toll charge plus a **ten-cent connection charge**, long-lines at the regular rate with **no connecting charge**), and submit pending acquisitions to the Department and the ICC | a federal conflict the company describes as "national in their scope"; criticism "directed against the Bell System"; a Chicago action it had just let go to a receiver | sixty days of interviews ("a result of a number of interviews between us during the last sixty days"); the California physical-connection holding; the ICC valuation just begun | the internal vote; whether any point was resisted; what was traded away | litigate; refuse; offer less | pending federal action; public opinion; the valuation | "Wishing to put their affairs beyond fair criticism" | adjustment "without litigation" | accepted the same day by the Attorney General and endorsed by the President; **Western Union disposal was still a liability line on the 1913 balance sheet at $4,000,000** | P1S01 l.1696-1890, l.1711-1817, l.5089-5091 · Medium; signed "By N. C. Kingsbury, Vice President" |
| 1913 (stated as continuing) | Keep the policy of investing the depreciation reserve in revenue-earning plant | a reserve that could have been held liquid or returned | the reserve's size ("over $174,000,000") | whether it was ever contested | hold the reserve against future replacement | the need to fund 1914's ~$56,000,000 construction | so the public gets plant "upon which no dividends or interest charges have to be earned" | continued self-financed build-out | unchanged within the window | P1S01 l.402-406, l.710-714 · Medium |
| 1912–1913 | Put an employees' pension / disability / insurance plan in effect and fund it out of revenue | no such plan; a large dispersed workforce | one year of experience: "in 16,054 cases employees… have participated in the benefits" | the decision date, the debate, the actuarial basis | no plan; state or mutual provision | the 1913 charge against revenue | not stated in the held bytes | labour stability, unstated as a goal | the combined system carried an Employees' Benefit Fund of $8,919,335 at 1913-12-31 | P1S01 l.1336-1345, l.668-680 · Medium (existence), UNKNOWN (decision-maker and rationale) |
| 1913 | Decline to convert to automatic switching, on the stated ground that its quality "has not been demonstrated" | a manual/semi-automatic plant "changed several times" in twenty-five years | the company's own exhaustive study "of every type of switchboard in use" | the internal cost comparison; whether engineers dissented | adopt automatic; run both | subscriber behaviour ("the subscriber does all the manipulation"); interurban network scale | service quality and dependability | no change | no change inside the window; post-window outcome not used (§2) | P1S01 l.1521-1541 · Medium |

### Claim records (§N)

N01 Claim: The registrant's directors accepted every suggestion of the Attorney General and printed the correspondence in the annual report. — Date: 1913-12-19 — Source: P1S01 l.1680-1693, l.1696-1825 — Source date: 1914 — URL: as H01 — Archived: — — Tier: 1 — Class: FACT — Passage: "all of the suggestions of the Attorney General were accepted by the Directors of the American Telephone and Telegraph Company" — Conf: Medium — Corroboration: 1 independent (the Attorney General's reply, same printed sequence) — Conflicts: U.6

N02 Claim: The company undertook to stop acquiring control of competing telephone companies and to dispose of its Western Union holding. — Date: 1913-12-19 — Source: P1S01 l.1711-1728 — Source date: 1914 — URL: as H01 — Archived: — — Tier: 1 — Class: FACT (an undertaking on the face of the document) — Passage: "Neither the American Telephone and Telegraph Company nor any other company in the Bell System will hereafter acquire, directly or indirectly… dominion or control over any other telephone company" — Conf: Medium — Corroboration: 0 independent — Conflicts: U.6

N03 Claim: No decision in this window names a founder, and six of seven have no named decision-maker. — Date: 1875-01-01..1915-12-31 — Source: this part's §N table — Source date: 2026-10-06 — URL: file-local — Archived: — — Tier: 1 (as to what the bytes do and do not say) — Class: FACT of the record's silence; **INFERENCE** that the firm is a company-not-a-founder case — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High — Corroboration: 1 — Conflicts: U.2

---

## O. COUNTERFACTUAL OPPORTUNITIES

STATUS: WRITTEN 2026-10-06

**Person described: P2, and the road-not-taken set its own print records.** Every row is written so it would still read as plausible had P2 failed in 1920 (§2).

| Alternative open in-window | What the held record shows about it | Verdict |
|---|---|---|
| **Government ownership and operation of telephone service.** Actively in the political field: the registrant devotes two headed sections of its FY1913 report to it and reprints its own 1911 declarations ("we recognize a 'responsibility' and 'accountability' to the public… something different from and something more than the obligation of other public service companies") to answer the charge that it is arguing for itself. Its argument is empirical: "no government-owned telephone system in the world is giving as cheap and efficient service as the American public is getting"; and a valuation threat: "if our property is ever taken by the government it will be found to be in the very best possible condition" | a live, argued, **unresolved** alternative at the stage boundary; the ICC valuation of 1913-03-01 was the mechanism by which it could be approached | **open at the close of Stage 1**, with no in-window signal of resolution. CONFIDENCE Medium that it was contested; the outcome is outside the firewall |
| **Municipal and cooperative telephony.** `P1S03` is published by the International Independent Telephone Association and authored by the General Manager of a **citizens'** company (Columbus), printing the cooperative option and its own rate arithmetic | a third model with an organised national association inside the window | open; the pamphlet's own admission that "the gain of the public through competition based on low rates has not compensated for the loss of capital invested" (`P1S03` l.231-233) is the counter-evidence and it comes from **inside** the movement |
| **Automatic switching.** Named, studied ("we have exhaustively studied the practical workings of every type of switchboard in use"), and declined on quality grounds | a technology the registrant could have adopted and did not, in this window | open in 1913, declined on the company's stated grounds; **the dossier does not use the later outcome to judge the refusal** |
| **Interconnection instead of acquisition.** The 1913 Second Point forecloses the acquisition-led path that the same window's competitor had accused the Bell companies of following ("purchases at high prices of competing plants", `P1S03` l.745-746) | the company converted an acquisition strategy into a toll-access revenue strategy, on ten cents a message and a 50-mile scope line | taken, on the face of the document; whether it was a choice or a concession is §U.6 |
| **Long-speaking / high-power transmitter devices** as a route to distance | dismissed in the company's print as founded on a misunderstanding of loss, with investors' losses asserted but not quantified | rejected by the registrant; **no independent technical adjudication exists in the held corpus**, so the rejection is recorded as the company's position, not as the engineering verdict |

**§2 duty stated plainly.** No in-window byte records a **rejected internal option** — no board minute, no cancelled project, no costed alternative. The counterfactual inventory above is therefore assembled from what the company argued *against in public*, which is a different and weaker class of evidence, and it is presented as such. That asymmetry is itself the record-selection finding for §O.

### Claim records (§O)

O01 Claim: Government ownership of telephone service was an actively argued alternative inside the window, addressed by the registrant at length in its own report. — Date: 1913 — Source: P1S01 l.1900-1975 — Source date: 1914 — URL: as H01 — Archived: — — Tier: 1 — Class: CONTEMPORANEOUS OBSERVATION (the company's own polemic) — Passage: "We are opposed to government ownership because we know that no government-owned telephone system in the world is giving as cheap and efficient service" — Conf: Medium — Corroboration: 1 independent (the existence of the organised alternative is separately carried by P1S03) — Conflicts: None

O02 Claim: No held byte records any internal rejected option or cancelled project for P2 in the window. — Date: 1875-01-01..1915-12-31 — Source: measurement over held bytes — Source date: 2026-10-06 — URL: file-local — Archived: — — Tier: 1 — Class: FACT (of a null over held bytes; the §2 record-selection null) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High — Corroboration: 1 — Conflicts: None

## P. QUANTITATIVE METRICS TABLE

STATUS: WRITTEN 2026-10-06

**Person described: P2**, with the basis column carrying `[SYSTEM]` / `[COMPANY]` / `[1887 print]` on every row (method §6, §8: never a value without its source and confidence cell; `UNKNOWN` is an acceptable value). Every figure is nominal dollars or counts of the stated year; **no row is inflation-rebased**. Classes: `FACT as printed` unless marked `DERIVED` or `ESTIMATE`. All periodical-sourced rows are capped Medium by the transport caveat (§Header 5).

| ID | Date | Metric | Value | Unit | Source | Source date | Confidence |
|---|---|---|---|---|---|---|---|
| P01 | 1913-12-31 | Subscriber stations, Bell System US [SYSTEM] | 8,133,017 | stations | P1S01 l.154 | 1914 | Medium |
| P02 | 1913 | Year-on-year station increase [SYSTEM] | 676,943 | stations | P1S01 l.154-155 | 1914 | Medium |
| P03 | 1913-12-31 | Stations run by independent/co-operative companies under contract [SYSTEM] | 2,717,808 | stations | P1S01 l.156-159 | 1914 | Medium |
| P04 | 1913 | Contracted share of system stations [SYSTEM] | 33.4% | percent (DERIVED: 2,717,808 ÷ 8,133,017) | P1S01 l.156-159 | 1914 | Medium |
| P05 | 1913 | Station growth rate on the report's own base [SYSTEM] | +9.1% | percent (DERIVED: 676,943 ÷ 7,456,074) | P1S01 l.154 | 1914 | Medium |
| P06 | 1913-12-31 | Places reached by Bell toll lines | 70,000 | places | P1S01 l.163-164 | 1914 | Medium |
| P07 | 1913-12-31 | Total wire mileage in exchange and toll service [SYSTEM] | 16,111,011 | miles | P1S01 l.176-177 | 1914 | Medium |
| P08 | 1913 | Wire mileage added in the year [SYSTEM] | 1,500,198 | miles | P1S01 l.177 | 1914 | Medium |
| P09 | 1913-12-31 | Underground wire, of which toll in underground cables [SYSTEM] | 8,817,815 / 543,923 | miles | P1S01 l.182-184 | 1914 | Medium |
| P10 | 1913-12-31 | Underground plant: conduits / cables / total [SYSTEM] | 85,700,000 / 95,800,000 / 181,500,000 | USD | P1S01 l.184-186 | 1914 | Medium |
| P11 | 1913 | Daily average toll connections [SYSTEM] | 806,000 | connections/day | P1S01 l.191-192 | 1914 | Medium |
| P12 | 1913 | Daily average exchange connections [SYSTEM] | 26,431,000 | connections/day | P1S01 l.192-193 | 1914 | Medium |
| P13 | 1913 | Total daily average connections [SYSTEM] | 27,237,000 | connections/day | P1S01 l.195 | 1914 | Medium |
| P14 | 1913 | Annualised traffic **as printed** [SYSTEM] | 8,770,300,000 | conversations/year (does not foot against P13; U.5) | P1S01 l.196 | 1914 | Medium |
| P15 | 1912 | U.S. telephone conversations as a share of mail+telegraph+telephone messages | 60.2% | percent | P1S01 l.219-220 | 1914 | Medium |
| P16 | 1913 | Plant additions, all companies [SYSTEM] | 54,871,856 | USD | P1S01 l.246 | 1914 | Medium |
| P17 | 1900-1913 | Plant additions, fourteen-year total [SYSTEM] | 646,915,200 | USD | P1S01 l.334 | 1914 | Medium |
| P18 | 1914 | Estimated construction requirement (company's own) [SYSTEM] | 56,000,000 (of which ~25,000,000 from internal resources) | USD — **ESTIMATE** | P1S01 l.342-354 | 1914 | Medium |
| P19 | 1913 | Applied out of revenue to maintenance and reconstruction [SYSTEM] | 70,183,000 | USD | P1S01 l.358 | 1914 | Medium |
| P20 | 1904-1913 | Maintenance/reconstruction provision, ten years [SYSTEM] | over 457,000,000 | USD | P1S01 l.363-364 | 1914 | Medium |
| P21 | 1913 | Gross revenue [SYSTEM] | 215,572,822 (prose prints "215,600,000") | USD | P1S01 l.502 vs l.425 | 1914 | Medium; U.5 |
| P22 | 1913 | Total expenses [SYSTEM] | 156,883,299 | USD | P1S01 l.539 | 1914 | Medium |
| P23 | 1913 | Net earnings / interest / dividends paid / surplus earnings [SYSTEM] | 58,689,523 / 16,652,624 / 30,301,705 / 11,735,194 | USD | P1S01 l.550-575 | 1914 | Medium |
| P24 | 1913-12-31 | Telephone plant on the books [SYSTEM] | 797,159,487 | USD | P1S01 l.471, l.605 | 1914 | Medium |
| P25 | 1913 | Plant increase, dollars and percent, against gross-earnings growth | 54,871,856 / 7.4% vs 8.2% | USD; percent | P1S01 l.472-473 | 1914 | Medium |
| P26 | 1913-12-31 | Total assets = total liabilities [COMPANY] | 655,956,307.97 | USD | P1S01 l.5067, l.5129 | 1914 | Medium; footed both sides §K.3 |
| P27 | 1913-12-31 | Stocks + bonds + capital advances of associated companies [COMPANY] | 530,984,879.14 (81.0% of assets, DERIVED) | USD | P1S01 l.5048-5052 | 1914 | Medium |
| P28 | 1913-12-31 | Own long-distance telephone plant [COMPANY] | 49,269,173.30 | USD | P1S01 l.5058 | 1914 | Medium |
| P29 | 1913 | Net earnings [COMPANY] | 40,576,746.19 (+2,669,101.93 vs 1912) | USD | P1S01 l.1252-1254 | 1914 | Medium |
| P30 | 1913 | Dividends at the regular 8% rate [COMPANY] | 27,454,037.15 | USD | P1S01 l.1255-1256 | 1914 | Medium |
| P31 | 1913 | Telephone traffic revenue, net, against total earnings [COMPANY] | 5,548,089.00 of 45,909,991.62 = 12.1% (DERIVED) | USD; percent | P1S01 l.5156-5164 | 1914 | Medium |
| P32 | 1913-12-31 | Capital stock / total stock and bonds [COMPANY] | 344,616,300 / 504,207,300 | USD | P1S01 l.1284-1298 | 1914 | Medium |
| P33 | 1913 | Increase of capital stock during the year [COMPANY] | 9,810,600 | USD | P1S01 l.1266 | 1914 | Medium |
| P34 | 1913-12-31 | Shareholders, and the count holding under 100 shares | 55,983 / 49,144 | persons | P1S01 l.1307, l.1310 | 1914 | Medium |
| P35 | 1913-12-31 | Average shares held / brokers' share of stock | 59 / under 6% | shares; percent | P1S01 l.1327-1330 | 1914 | Medium |
| P36 | 1913 | Western Electric sales, and the Bell-internal share | 77,532,860 of which 50,681,070 (65.6%, DERIVED) | USD | P1S01 l.1008-1010 | 1914 | Medium |
| P37 | 1913 | Net earnings to plant and other assets; dividends+interest to plant and other assets | 5.69% ; 4.92% | percent | P1S01 l.997-1000 | 1914 | Medium |
| P38 | 1895 / 1900 / 1910 / 1912 / 1913 | Average earnings per exchange station, associated operating companies | 69.75 / 44.68 / 31.28 / 30.93 / 30.45 (exchange) ; 11.35 / 12.60 / 9.47 / 9.21 / 9.03 (toll) ; 81.10 / 57.28 / 40.75 / 40.14 / 39.48 (total) | USD per station per year | P1S01 l.1043-1049 | 1914 | Medium |
| P39 | 1895→1913 | Change in average earnings per station | −51.3% (DERIVED: (39.48−81.10) ÷ 81.10) | percent | P1S01 l.1049 | 1914 | Medium; mechanism INFERENCE Low, §I.2 |
| P40 | 1913 | Headquarters engineers and scientists | 550 | persons | P1S01 l.1554 | 1914 | Medium |
| P41 | 1913 | Employee benefit-plan participations in its first year | 16,054 | cases | P1S01 l.1343-1345 | 1914 | Medium |
| P42 | 1914-01-01 | Instruments owned by the Bell Company; types designed 1877-1914 | 12,000,000 ; 53 receiver types / 73 transmitter types | instruments; types | P1S01 l.1379-1381, l.1369-1371 | 1914 | Medium |
| P43 | 1913-12-31 | Interconnection price set by the December 1913 letter | 0.10 per message added to the regular toll charge; Bell toll scope beyond 50 miles | USD; miles | P1S01 l.1773-1781 | 1914 | Medium |
| P44 | 1885-03-18 | First Paterson underground cable in New York: conductors / gauge / greatest length / insulation as laid | 100 / No. 18 AWG / 1,965 feet / 1–100 megohms | mixed | P1S02 l.4572-4577 | 1887 | Medium |
| P45 | 1887-04-01 | Sixth Avenue conduit cables: conductor counts and insulation | 90 + 100 + 110 conductors (300 total) / 500–1,000 megohms per mile | mixed | P1S02 l.4590-4602 | 1887 | Medium |
| P46 | 1885-05-28 | Brooks system, Spring Street Exchange: wires / length / insulation / result | 400 wires / 2,449 feet / 30 megohms per mile / water ingress, drawn and re-drawn | mixed | P1S02 l.4631-4641 | 1887 | Medium |
| P47 | 1913 | Short-haul cable share of the Boston–Washington line | 47% | percent | P1S01 l.1482 | 1914 | Medium |
| P48 | 1875 / 1876 / 1877 / 1895 / 1915 | Occurrences of the candidate origin-and-opening dates across the 7 cited SEC documents | 0 / 0 / 0 / 0 / 0 | counts (measured this pass) | §Header 1 ATT-S1-C2 | 2026-10-06 | High (of the measurement) |
| P49 | 1875-01-01..1915-12-31 | Employee headcount of P2 | **UNKNOWN** | persons | no carrier in held bytes; §S G-6 | — | High (of the silence) |
| P50 | 1885 | P2's capitalisation at incorporation | **UNKNOWN** | USD | no carrier in held bytes; §S G-2, §U.8 | — | High (of the silence) |

---

## Q. CHRONOLOGICAL MICRO-TIMELINE

STATUS: WRITTEN 2026-10-06

**Persons named per row — this is the deliverable of the section.** `P1` rows are adjacency records inside P2's print; `P4` rows are out-of-window recitals kept in the chronology only to fix who is *not* present.

| Date | Event | Person | Carrier | Class | Conf |
|---|---|---|---|---|---|
| 1875 | No event carried. `1875` prints 0 times in held bytes | — | §Boundary 1 | UNKNOWN | High (of the null) |
| 1876-01-01 | Baseline of the company's own 38-year station-growth diagram | art/market, not a company act | P1S01 l.5506 | FACT (of the print) | Medium |
| 1877 | "From the year 1877 to the present time improvements have followed each other with remarkable rapidity" — the apparatus epoch opens | the art, **not** P2 and not P1 | P1S01 l.1364 | CONTEMPORANEOUS (as an epoch claim, made in 1914) | Medium; §U.2 |
| 1880 | The report quotes an 1880 annual report: "This work is expensive, hut [sic] it is of the first importance to our company and must he [sic] continued" | the "our" of 1880 is **not** P2's own print here — the 1880 document is not held | P1S01 l.1401-1409 | RESTATED quotation, carrier is P2's 1913 print | Medium; §S G-8 |
| 1881 | "experimental underground cables for a short distance alongside of a Massachusetts railroad track with small results" | P2's engineering programme (as later told) | P1S01 l.1416-1418 | registrant-retrospective | Medium |
| 1883-02 / 1883-04 | Boston iron-pipe conduit: four Patterson lead, one Day kerite, one rubber (February); two Clark rubber (April — printed "1853", OCR) | American Bell laid them; "afterwards being turned over to the New England Company" | P1S02 l.7069-7070, l.7096-7098 | CONTEMPORANEOUS 1887, incl. a third-party letter | Medium; §U.5 |
| 1883 | "several cables were laid at Boston, the longest of which was 1,500 feet"; users "could not talk satisfactorily further than the suburbs" | P2's retrospective account of the family's plant | P1S01 l.1418-1426 | registrant-retrospective | Medium |
| 1885-03-18 | First Paterson underground cable in New York completed, 100 conductors, 1,965 feet | P2 | P1S02 l.4572-4576 | CONTEMPORANEOUS | Medium; **the 1885 decoy, §C.3** |
| 1885-05-28 / 1885-06 | Brooks system at Spring Street Exchange completed; Edison underground system completed (print "June 91[, 18]85") | P2 | P1S02 l.4631, l.4614 | CONTEMPORANEOUS | Medium; §U.5 |
| **1885** | **P2 incorporated under the laws of the State of New York** | **P2** | **P1S04 l.238 — a 1994 recital; no in-window carrier** | FACT, RESTATED | High; §U.2 |
| 1887 | Twisted pair begins; "meant the abandonment of the entire underground plant of the Bell System" | P2's programme (family-wide claim) | P1S01 l.1431-1435 | registrant-retrospective | Medium |
| 1887-04-01 | Sixth Avenue Dorsett conduit cables completed, 300 conductors working | P2 | P1S02 l.4590-4607 | CONTEMPORANEOUS | Medium |
| 1887-09-06..07 | Hall writes to Boston (Sept 6) and receives the cable-condition reply (Sept 7) during the conference | P2 asking, New England company answering | P1S02 l.7073-7094 | CONTEMPORANEOUS | Medium |
| 1887-09-07..09 | Three-day conference on telephone cables at 18 Courtlandt Street; report "PRINTED, NOT PUBLISHED" | P2, with American Bell, Western Electric, NY&NJ, Metropolitan | P1S02 l.15-28, l.316-358 | CONTEMPORANEOUS | Medium |
| **1894** | "the expiration of the Bell patents" — competition opens | the art, and every independent company | P1S03 l.190-193 | CONTEMPORANEOUS, third party | Medium; **the registrant's own print never states it** |
| 1895 | "The Independent companies going into the field from 1895 to 1900" | the independents | P1S03 l.1027 | CONTEMPORANEOUS, third party | Medium |
| 1895 | First column of three statistical series (l.978, l.1031, l.1043) — **not** a transcontinental line | P2's associated operating companies | P1S01 | FACT (of what the columns are) | Medium; §U.3 |
| 1899 / 1900 | The transfer of the Bell System parentage | **UNKNOWN — no carrier in held bytes** | §S G-3 | UNKNOWN | High (of the silence) |
| 1902 | Pupin loading coils; loaded cable New York–Newark | P2's programme | P1S01 l.1438-1442 | registrant-retrospective | Medium |
| 1905 | Loaded cable 20 miles from New York toward Philadelphia | P2's programme | P1S01 l.1444 | registrant-retrospective | Medium |
| 1905 → 1907 | Chicago & Milwaukee Telegraph Line: receivership (1905), offered for sale (1907), bought by the Chicago and Wisconsin Telephone Companies "in connection with the American Telephone and Telegraph Company" | **another company's failure**, absorbed into the family | P1S01 l.2985-3020 | appendix reprint in P2's print | Medium; §M-6, §U.8 |
| 1906 | 90-mile loaded cable operated New York–Philadelphia | P2's programme | P1S01 l.1446 | registrant-retrospective | Medium |
| 1907 | $150,000,000 4% convertible bonds of 1906 (only $4,591,000 outstanding by 1913-12-31); Western Electric "changed its selling plan… with low prices" | P2's financing; and P2's manufacturer | P1S01 l.1268-1270; P1S03 l.755-758 | FACT / hostile observation | Medium |
| 1908-09 | International Independent Telephone Association publishes Johnston's comments on the 1907 report | third party, hostile, naming P2 | P1S03 l.114-159 | CONTEMPORANEOUS | Medium |
| 1911 | Cable designed "capable of giving a satisfactory conversation between Washington and Boston" | P2's engineering | P1S01 l.1450-1453 | registrant-retrospective, **design** | Medium |
| 1912 | Section laid Washington–Philadelphia; first underground talk New York–Washington, "the longest distance underground yet achieved" | P2 | P1S01 l.1455, l.1485 | near-contemporaneous | Medium |
| 1913-03-01 | Act of Congress directing ICC valuation of common carriers "which includes all the principal telephone companies" | P2 and every peer | P1S01 l.454-458 | FACT | Medium |
| 1913 | Section laid New Haven–Providence; satisfactory underground talk Boston–Washington; New York–Denver line "exhaustively" studied | P2 | P1S01 l.1459, l.1476, l.1501 | CONTEMPORANEOUS | Medium |
| 1913 | "an action in Chicago involving the relations between this Company and the Central Union Telephone Company"; company consents to receivers | P2 and a competitor | P1S01 l.1660-1668 | CONTEMPORANEOUS | Medium |
| 1913-12-19 | Five-point course of action accepted by the Directors; signed by N. C. Kingsbury, Vice President; acknowledged by J. C. McReynolds; Wilson's note printed | P2, the Department of Justice, the Presidency | P1S01 l.1696-1890 | FACT, three voices | Medium; §N, §U.6 |
| 1913-12-31 | The §P/§K year-end position; dividend payable 1914-01-15 of $6,892,326.00 | P2 | P1S01 l.5103 | FACT as printed | Medium |
| 1914-01-01 | 12,000,000 instruments owned; one Bell station to each 12 Americans; 38-year growth diagram runs to this date | the family, reported by P2 | P1S01 l.1379, l.5509 | CONTEMPORANEOUS | Medium |
| 1914-01-20 | Director Henry P. Davison resigned — footnote on the officers' page | P2's board | P1S01 l.114 | FACT as printed | Medium |
| **1915** | "with the completion of the line to the Pacific Coast in 1915, commercial communication will be dependable and practicable" — **and nothing else** | P2's plan | P1S01 l.400-402 | CONTEMPORANEOUS **as design**; event UNKNOWN | Medium; §U.3 |
| 1983 | Southwestern Bell Corporation incorporated in Delaware **by AT&T** as one of seven RHCs | **P4** (out-of-window recital) | P1S05 l.210-212 | FACT, RESTATED | High |
| 1984-01-01 | P4 divested by spin-off; P2 begins leasing "from the regional holding companies created at divestiture" | **P3/P4 and P2** | P1S05 l.213; P1S04 l.1121 | FACT, RESTATED | High; §U.4 |

---

## R. END-OF-STAGE STRUCTURED SNAPSHOT (1915-12-31, as far as the record will go)

STATUS: WRITTEN 2026-10-06

**Person: P2.** The last **dated position** this corpus can actually certify is 1913-12-31 (printed 1914); everything at the 1915 edge is a plan or a null, and is written that way.

| Variable | Value at the stage edge | Source | Confidence |
|---|---|---|---|
| Legal identity | a New York corporation, incorporated 1885, carrying the Bell System's long lines and holding the family's paper | P1S04 l.238; P1S01 l.5028-5058 | High (identity) / Medium (in-window detail) |
| Registrant count behind the brand | **one** in-window (P2). P1 is not a registrant; P4 does not exist for another 68 years | §Header 1 | High |
| Installed capability | underground telephony demonstrated Boston–Washington; the Pacific route planned, not evidenced | P1S01 l.1476-1490, l.400 | Medium |
| Financial shape | company net earnings $40.6M; system gross revenue $215.6M; system surplus earnings **down** $1.49M on 1912; stock $344.6M; bonds and notes to the public $770.1M at system level | P1S01 l.1252, l.502, l.575, l.1284, l.446 | Medium |
| Customer shape | 8,133,017 system stations, a third of them not directly the registrant's; 70,000 places on toll; average revenue per station still falling | P1S01 l.153-168, l.1049 | Medium |
| Supply shape | Western Electric 65.6% captive at Hawthorne; outside makers still being written about in the trade press; 550 headquarters engineers and scientists | P1S01 l.1008-1015, l.1554 | Medium |
| Regulatory shape | a federal valuation in progress under an 1913-03-01 Act; a settlement of December 19, 1913 binding the company to divest telegraph control and stop buying competitors | P1S01 l.454, l.1711-1728 | Medium |
| Political shape | government ownership argued in the open, in the company's own report | P1S01 l.1900-1975 | Medium |
| What the stage leaves unresolved at its own boundary | whether the Pacific line was built and opened; whether the ICC valuation would reprice the plant; whether the interconnection settlement would hold | §D.4, §H, §U.3 | **UNKNOWN**, and named as such |
| Founder state | **no founder appears in the record of this window**; roles, not founders | §B | High |

---

## S. DATA GAPS

STATUS: WRITTEN 2026-10-06

Every row states why the gap exists and the route that could close it. `UNKNOWN` here is a deliverable. High-importance rows carry a mandatory follow-up task, and the FETCH REQUEST blocks below are the tasks.

| ID | Gap | Why missing | Importance | Best available evidence | Conf | Follow-up task |
|---|---|---|---|---|---|---|
| G-1 | No datable act of P1 (Bell Telephone Company, 1877) anywhere in held bytes | P1 was never a registrant reachable from this directory; its papers are a family-(e) object, and the only plausible in-corpus carrier is a 1940 address that returned HTTP 401 | **High** | 1877 as an apparatus epoch, `P1S01` l.1364 | High (of the null) | **FETCH REQUEST R-1** below |
| G-2 | P2's 1885 certificate of incorporation, purpose clause and authorised capital | family (e) unimplemented; the in-window print of 1885 is four cable completions | **High** | the 1994 recital, `P1S04` l.238 | High | **FETCH REQUEST R-5** (registry route) |
| G-3 | The 1899/1900 parentage transfer from P1 to P2 — the single most consequential brand-lineage event in the window | no held byte mentions it; both registrants' EDGAR perimeters begin in 1994 | **High** | indirect: P2's 1913 asset mix (81% associated-company paper) and its 1887 print listing American Bell officers | Medium (that the event is unrepresented) | **FETCH REQUEST R-2/R-3** (annual-report run 1901-1928) |
| G-4 | First customer, first toll call, first priced sale of any P2 service | the company printed aggregates, not firsts; no trade press is held | Medium | daily averages, `P1S01` l.191-196 | Medium (of the null) | periodical re-run, §T.6 item 3 |
| G-5 | Whether the 1915 transcontinental line opened | the only in-window carrier is future-tense; the two 1914/1915 third-party items returned 0 B / HTTP 503 | **High** | `P1S01` l.400-402 | High (of the null) | **FETCH REQUEST R-2** |
| G-6 | Employee headcount, wage bill, and any officer compensation for P2 | not printed in the held layers | Medium | 550 HQ engineers and scientists; 16,054 benefit cases | High (of the silence) | the 1901-1928 run may print the operating returns |
| G-7 | Whether "Edward J. Hall, Jr." (1887 General Manager) and "Edward J. Hall" (1913 Vice President) are one person | no byte states it; an officer directory would | Low | both name-lines quoted at §B.1 | UNKNOWN | family (e) / an 1890s directory |
| G-8 | The held 1880 annual report whose words are quoted in the 1913 print; and the 1907 annual report the pamphlet quotes | neither document is on this shelf; the 1913 report is the only carrier of the 1880 sentence, the 1908 pamphlet of the 1907 extracts | Medium | `P1S01` l.1401-1409; `P1S03` l.186-187, l.204-273 | Medium | **FETCH REQUEST R-4** |
| G-9 | Whose words are whose inside the 1908 pamphlet between l.204 and l.273 | the OCR rendering flattens the extract/plain-text boundary; the pamphlet says extracts follow | Medium | the framing sentence at `P1S03` l.186-187 | Medium | page-image check of the same identifier (R-4) |
| G-10 | Any independent count behind **any** §P row | every figure is P2's own print; family (b) untried, family (e) unimplemented | **High** | §K.3 cross-foots (internal coherence only) | High | §T.6 items 1–4 |
| G-11 | The 1915–1984 half of P2's life | **Stage 2, and the probe refuses to dispatch it**: no in-window document at all, tier T3 resting on a fetch backlog, not a judgment | n/a | Stage 2 tier table, probe §4 | High (that Stage 1 carries nothing for it) | do not dispatch Stage 2 until R-1/R-2/R-3 return bytes |
| G-12 | The name-change date 2005-11-18 that the fleet record asserts for P4 | the probe found it printed in no held byte; the FY2005 10-K is the named carrier and was never fetched | Medium (for Stage 1 it is irrelevant, but the dossier must not inherit it as fact) | `P1S09` l.13-40 (both registrants in one header) | High (of the null) | the probe's §8 item 7 |

**FETCH REQUEST: R-1** (family (d)/(c), Internet Archive text route) — `birthbabyhoodoft00wats`, "The birth and babyhood of the telephone. An address delivered before the third…" (scan date 1940-01-01), **UNANSWERED at HTTP 401 after 3 tries** on the `_djvu.txt` route. Command: `python tools/ia_text.py list-files --id birthbabyhoodoft00wats --company-dir founders_playbook/01_companies/company_035_att` then `python tools/ia_text.py birthbabyhoodoft00wats --file <named layer>`. Why it matters: the likeliest in-corpus carrier of a datable **1875–1877** act (G-1, and the only route that could move §U.2).

**FETCH REQUEST: R-2** (family (c), five volumes that returned 0 B / HTTP 503 to `harvest_mine`) — `2xVAAAAAYAAJ` (**1915**), `j4BbAAAAMAAJ` (NY Public Service Commission, Second District, **1914** — a regulator's record on the Bell telephone lines, an independent lineage), `0ec-AQAAMAAJ` (Electrical Review and Western Electrician, **1910**), `xEJbUdD0uBsC` (**1921**, P2's annual report), `DFUSAQAAMAAJ` (**1901**, Corporation Annual Reports to Shareholders). Route: `ia_text.py list-files` + `--file` per identifier. Why: R-2's 1914/1915 pair is the **first-validation evidence** G-5 needs; the 1901/1921 pair is the annual-report run that decides G-3 and Stage 2's tier.

**FETCH REQUEST: R-3** (family (d), the P2 annual-report run 1901–1928) — `qYIphO8ACGAC` (1925), `KOBRAQAAMAAJ` (1928), `lDOj7-YW6C0C` (The Statist 1925), plus an identifier search for the **1899 and 1900** reports, which is the only way G-3 gets an in-window carrier.

**FETCH REQUEST: R-4** (family (d)/(c)) — the **1907 annual report of P2** (quoted by `P1S03` and not held) and the **1880 annual report** (quoted by `P1S01` l.1401 and not held). Both close G-8 and one of them settles G-9 by page image.

**FETCH REQUEST: R-5** (family (e), hand-off, **not an agent brief**) — P2's 1885 New York certificate of incorporation; P1's 1877 organisation papers; the 1984 Divestiture Plan of Reorganization. The probe records that no auction/museum endpoint exists in any `tools/*.py`, so this cannot be attempted at 0 web budget (G-2).

**UNTRIED (carried forward from the probe, unchanged by this pass, each with its command):**
1. **Family (b) web archives / Wayback CDX — UNTRIED for every stage, and `tools/web_domains.json` cites no domain for this company** (`slugs` keys read this pass: centene, cencora, relevance, marathon, microsoft, target — **`att` is absent**), so the family cannot even be scoped by domain here. Route: `python tools/cdx_intake.py` / the probe's CDX one-liner against `att.com`, `sbc.com`, `southwesternbell.com`. The project web floor (≈1996-12-29) puts it all in Stage 3 and after; it is recorded as **UNTRIED, not empty**.
2. **Family (e) — UNTRIED and UNIMPLEMENTED.** No auction/museum endpoint exists in any `tools/*.py`.
3. **Chronicling America / HathiTrust name-discovery re-run** — TRIED–UNANSWERED at search level by the probe (4 CA rows: 2 UNANSWERED, 2 HTTP 404; 1 HT row `SKIPPED: hard stop`), and **UNTRIED as a facet-free re-run**: `python tools/ca_endpoint_probe.py`, then `python tools/periodical_harvest.py --company att --facet-free`. Task text needed for G-5: `"American Telephone and Telegraph" "Pacific Coast" telephone 1915`.
4. **A whitespace-tolerant re-grep of the bytes already held** — UNTRIED as a fleet action and proven necessary by §Header 1: name phrases must be matched as `American\s+Telephone`, `Telephone\s+Compan`, `A.T.&T.`, `AT&T` with entity adjacency, **never bare `att`**.
5. **`sec_intake.py facts` (XBRL) for both registrants** — UNTRIED; would reach Stage-3 series, nothing in this window.
6. **The `corporate_print/` shelf as a destination** — it holds **0 files** while the harvest index labels three held items `corporate_print`; the bytes live in `sources/periodicals/`. Nothing was moved (§14 rule 4). A later fetch will land there and the next probe must re-enumerate `sources/` per §14.11.

---

## T. SOURCE / PROVENANCE TABLE

STATUS: WRITTEN 2026-10-06

| Source | Type | Primary/Secondary | Event date | Publication date | URL | Tier | Confidence |
|---|---|---|---|---|---|---|---|
| P1S01 — Annual Report of the Directors of American Telephone and Telegraph Company to the Stockholders for the year ending December 31, 1913 (136,506 B; 5,631 lines) | corporate print (digitised) | **Primary — P2 speaking of itself** | 1913-12-31 | 1914 (title page "NEW YORK, 1914"; "January 1, 1914" at l.44) | https://archive.org/download/annualreportofdi00amer_14/annualreportofdi00amer_14_djvu.txt | 1 | Medium (transport cap) |
| P1S02 — Report of a Conference Held at the Office of the American Telephone and Telegraph Company, September 7, 8 and 9, 1887; "PRINTED, NOT PUBLISHED" (334,305 B; 8,784 lines) | house print | **Primary — earliest carrier of P2 acting** | 1887-09-07..09 | 1887 | https://archive.org/download/report-of-a-conference-held-at-the-office-of-the-american-telephone-and-telegraph-company/Report%20of%20a%20conference%20held%20at%20the%20office%20of%20the%20American%20Telephone%20and%20Telegraph%20Company_djvu.txt | 1 | Medium |
| P1S03 — "Some Comments on the 1907 Annual Report of American Telephone and Telegraph Company", Gansey R. Johnston, General Manager, The Columbus Citizens Telephone Company; published by the International Independent Telephone Association, Chicago; Berlin Printing Company, Columbus, Ohio; l.114-159 | third-party trade pamphlet | **Secondary, independent of P2, hostile** | 1908 (on 1907) | 1908-09 | https://archive.org/download/somecommentsona00chicgoog/somecommentsona00chicgoog_djvu.txt | 3 | Medium |
| P1S04 — AT&T (CIK 0000005907) Form 10-K for FY1993, accession 0000005907-94-000008, 402,168 B / 48,745 words | SEC filing | Primary **for the recital only** — a 1994 document describing 1885 | 1885 (recited) | 1994-03-25 | https://www.sec.gov/Archives/edgar/data/0000005907/000000590794000008/0000005907-94-000008.txt | 1 | High |
| P1S05 — Southwestern Bell Corporation (CIK 0000732717) Form 10-K for FY1993, accession 0000732717-94-000005 | SEC filing | Primary for P4's own origin | 1983/1984 (recited) | 1994-03-18 | https://www.sec.gov/Archives/edgar/data/0000732717/000073271794000005/0000732717-94-000005.txt | 1 | High |
| P1S06 — SBC Form 10-K405 FY1994, accession 0000732717-95-000003 | SEC filing | Primary, same registrant as P1S05 → **same lineage** | 1983 (recited) | 1995-03-14 | https://www.sec.gov/Archives/edgar/data/0000732717/000073271795000003/0000732717-95-000003.txt | 1 | High |
| P1S07 — SBC Form 10-K FY1999, accession 0000732717-00-000018 | SEC filing | Primary, same lineage again; carries the Bell operating-company family list | 1983 (recited) | 2000-03-10 | https://www.sec.gov/Archives/edgar/data/0000732717/000073271700000018/0000732717-00-000018.txt | 1 | High |
| P1S08 — SBC Form S-4 / POS AM, file d24647posam.htm, accession 0000950134-05-008807 | SEC filing | Primary for "Delaware in 1983" inside the acquisition of its own parent | 2005 | 2005-05-03 | https://www.sec.gov/Archives/edgar/data/0000732717/000095013405008807/d24647posam.htm | 1 | High |
| P1S09 — Form 425 SGML, accession 0001047469-05-002185, 474,324 B | SEC filing | Primary; **co-filer header carries both registrants' identities in one document** | 2005-02-02 | 2005-02-02 | https://www.sec.gov/Archives/edgar/data/0000732717/000104746905002185/0001047469-05-002185.txt | 1 | High |
| P1S10 — SBC investor letter, Form 425 `d425.htm`, accession 0001193125-05-015481, 1,009 words | SEC filing (marketing instrument) | Primary as a 2005 claim; **useless as evidence about 1885–1915** | 2005-01-31 | 2005-01-31 | https://www.sec.gov/Archives/edgar/data/0000732717/000119312505015481/d425.htm | 1 | High (that it was said); the claim it makes is **not** adopted |
| P1S11 — `sources/_index/quarantine/CIK0000005907/` (1,255 filings, 1994-01-07→2007-01-18) | **index artefact** | **Not evidence.** A search-index row and a guard verdict are not witnesses (§15.1) | n/a | built 2026-10-06 | file-local | — | High (as a measurement of the archive's reach) |
| P1S12 — `sources/_index/_registrant_CIK0000732717.json` + `submissions.csv` (7,922 filings, 1994-02-14→2026-10-02; former names `SBC COMMUNICATIONS INC`, `SOUTHWESTERN BELL CORP`) | **index artefact** | Not evidence of any event; is evidence of **perimeter** | n/a | built 2026-10-06 | file-local | — | High (as a perimeter measurement) |
| P1S13 — `research/A_chronology_feasibility.md`, agent `probe-att` | dossier pointer page | Not evidence (§13: "a `TIER1_CANDIDATE` label, or a tier stamp is not evidence") | n/a | 2026-10-06 | file-local | 4 | — |

### T.4 What the tooling reached, stated as measurement
* **P2's EDGAR perimeter is 1994-01-07 → 2007-01-18, 1,255 filings** (`index --cik 5907`, guard → quarantine at `sources/_index/quarantine/CIK0000005907/`, 320 rows with no `primaryDocument`). **The 1885–1984 span is not missing from EDGAR because it is missing from the company's life — it is missing because EDGAR's filing universe starts in the 1990s for both registrants.** This is a measured perimeter, not a finding of absence.
* **P4's perimeter is 1994-02-14 → 2026-10-02, 7,922 filings**, walk 4 slices, 198 rows without a `primaryDocument`, 0 dropped.
* `sources/sec/` holds **33 stored documents / 10,500,602 B** (probe's count, re-enumerated this pass as §Header 1's file list); `sources/periodicals/` holds **6 layers / 660,753 B**, of which this part cites 3 and rejects 3 as decoys (§Header 1's `att`-token note; `DTIC_ADA197243` is an Irvine Company compiler validation).
* **md5 discipline before counting corroboration (§3):** the six periodical layers are pairwise distinct (probe §3.4) and the three documents of P1S05/P1S06/P1S07 are **one registrant describing itself three times** — they are cited as one lineage, and no row in this file claims corroboration from them.

### T.5 Five-family ledger, as this pass found it
| family | verdict this pass | what it delivered for Stage 1 |
|---|---|---|
| (a) SEC / EDGAR | **TRIED–ANSWERED** (bytes on disk; not re-fetched here — this is an authoring pass at 0 web budget) | the 1885 recital (P1S04) and the 1983/1984 recital (P1S05-S08); a measured perimeter; **no in-window document** |
| (b) web archives | **UNTRIED** — and not scopeable: `tools/web_domains.json` cites no domain for `att` | nothing; see §S UNTRIED 1 |
| (c) periodical corpora | **TRIED–ANSWERED, thin** — one opened third-party carrier (P1S03), which is hostile print, not company print | 1894 patent expiry; the independent wave; Western Electric's 1907 pricing; the Columbus/Central Union rate and failure record |
| (d) digitised corporate print | **TRIED–ANSWERED — the strongest family**, two opened carriers of P2's own print | everything in §E, §J, §K, §L, §M, §N, §P; the 1915 design statement; the 1877 epoch |
| (e) auction / museum / manuscript | **UNTRIED and UNIMPLEMENTED** | nothing; the three documents Stage 1 most needs (§S R-5) |

### T.6 What a later pass must not repeat, as an error this pass made or inherited
1. Do not report the `1885-01-01 → 1984-12-31` `harvest_mine`/`_RUN.json` window as a founding span (§Boundary 4 (vi)).
2. Do not treat the quarantined 5907 index as either evidence or absence (§Header 1).
3. Do not grep `att` bare, and do not grep the company's name with a single space (§Header 1); `A.T.&T.` and `AT&T` need entity adjacency too, because `AT&T` also appears on 1987 Ada-compiler validation reports.
4. Do not upgrade any periodical quotation above Medium while the six sidecars carry the UNVERIFIED TLS note; the remedy is a re-check of the transport, not a re-write of the sentence.
5. Do not import the 2005-11-18 name change, or any "founded 1877", or "the 1895 line", from outside this corpus: none has a carrier here (§S G-12, §U.2, §U.3).

---

## U. CONFLICTING EVIDENCE

STATUS: WRITTEN 2026-10-06

Nine conflicts are declared here and each carries exactly one row in the `conflicts` register block. `<!-- ANCHORS: U.1-U.9 -->`

### U.1 Which registrant answers the brand, and why the name route cannot tell you
**CLAIM A:** `index "AT&T Corp"` and `resolve --ticker T` both return CIK **732717 / AT&T INC.** — the name route answers with the modern registrant. **CLAIM B:** the co-filer header of a 2005 Form 425 prints CIK **0000005907 / AT&T CORP**, `STATE OF INCORPORATION: NY`, IRS 13-4924710, file no. 001-01105, former conformed name `AMERICAN TELEPHONE & TELEGRAPH CO` (`P1S09` l.13-40) — and `index --cik 5907` measures a second, different registrant. **WHY THEY DIFFER:** `NAME_STOP_WORDS` deletes both `corp` and `inc`, so the two strings normalise to the same token set and match one ticker-map title. **EVIDENCE WEIGHT:** both prints are EDGAR's; the mechanism is ours. **BEST-SUPPORTED INTERPRETATION:** two registrants; historic person ⇒ 5907, ticker/brand today ⇒ 732717; any downstream `index "AT&T Corp"` is a wrong-registrant generator and must carry an explicit `--cik`. **RESIDUAL UNCERTAINTY:** whether EDGAR's ticker map holds a second `AT&T` row unreachable at 0 web budget. **CONFIDENCE:** High.

### U.2 "Founded 1877" vs incorporated 1885 vs created 1983
**CLAIM A:** the brand's folklore origin is 1877, and the tooling's window floor is 1885. **CLAIM B:** P2's own filing says it "was incorporated in 1885 under the laws of the State of New York" (`P1S04` l.238), and P4's own filing says it "was incorporated under the laws of the State of Delaware in 1983 by AT&T" (`P1S05` l.210). **WHY THEY DIFFER:** four persons carry one name, and a harvester's window parameter reads as a date of birth. **EVIDENCE WEIGHT:** two registrants' primary filings, each speaking of itself; the 1877 has **no carrier for either** — its only in-window appearance is an apparatus epoch (`P1S01` l.1364, l.1368). **BEST-SUPPORTED INTERPRETATION:** 1885 is P2's incorporation, 1983 is P4's creation, and **neither is "founded 1877"**; "the Bell telephone art dates from 1877, on the company's own 1914 accounting of it" is the only 1877 sentence this dossier can write. **RESIDUAL UNCERTAINTY:** whether any 1877-era document is reachable at all (R-1, R-5). **CONFIDENCE:** High.

### U.3 The 1895 experiment and the 1915 opening, against what a contemporaneous document prints
**CLAIM A (legend):** a first transcontinental experiment in 1895 and a validated opening in 1915. **CLAIM B (held bytes):** `transcontinental` occurs **0 times** in every held layer; the three `1895` occurrences in the FY1913 report are the first column of statistical series (l.978, l.1031, l.1043); the second `1895` reading in the corpus is a competitor's — "The Independent companies going into the field from 1895 to 1900" (`P1S03` l.1027); and the single 1915 statement of the plan is **future tense** (`P1S01` l.400-402). **WHY THEY DIFFER:** later company histories assert what the registrant's own print only projected. **EVIDENCE WEIGHT:** the projection is the strongest contemporaneous statement available and it dates an **intention**, not an event. **BEST-SUPPORTED INTERPRETATION:** first experiment 1895 = **UNKNOWN**; first validation 1915 = **PARTIALLY CARRIED as design, UNKNOWN as event**. **RESIDUAL UNCERTAINTY:** whether R-2's 1914/1915 volumes carry the opening. **CONFIDENCE:** High that the distinction is right; UNKNOWN on the underlying event.

### U.4 1984-01-01: one event, two directions, two persons
**CLAIM A (P4's voice):** the divestiture is its **birth** — "incorporated … in 1983 by AT&T as one of seven regional holding companies … AT&T divested the Corporation by means of a spin-off … on January 1, 1984". **CLAIM B (P2's voice):** the same event is a **separation it then lived inside** — facilities "leased from the regional holding companies created at divestiture" (`P1S04` l.1121) and reimbursements under the "Divestiture Plan of Reorganization" (l.6640). **WHY THEY DIFFER:** one date read from each side of the cut. **EVIDENCE WEIGHT:** both are the registrants' own words about themselves; neither is independent of the other's drafting. **BEST-SUPPORTED INTERPRETATION:** report it as a **two-person event with two directions**, never as one company's beginning or as the other's failure. **RESIDUAL UNCERTAINTY:** none material for Stage 1, which ends 69 years earlier. **CONFIDENCE:** High.

### U.5 Internal inconsistencies inside one held document (and one OCR class)
**CLAIM A:** the FY1913 print's prose — gross revenue "$215,600,000", increase "over $16,000,000"; total daily average 27,237,000 "or at the rate of about 8,770,300,000 per year". **CLAIM B:** the same document's tables — gross $215,572,822, increase $16,400,668 (l.494-506); and 27,237,000 × 365 = 9,941,505,000 (§K.3). To the same class belong the scan's own corruptions: "June 91[, 18]85" (`P1S02` l.4615), "April, 1853" for a 1883 cable (`P1S02` l.7098), "Telegrah" (`P1S04` l.3454), "Beil System" (`P1S01` l.1920), "44 of an inch" for a crust thickness (l.5040). **WHY THEY DIFFER:** rounding in prose against exactness in tables, and an OCR letter-substitution class (RD-131). **EVIDENCE WEIGHT:** the table is the more precise of the company's two statements; the traffic annualisation implies a ≈322-day basis that is nowhere stated. **BEST-SUPPORTED INTERPRETATION:** cite the tabled values; report the printed annual figure **as printed**, with the non-footing noted; **no value is substituted** and no OCR defect is silently tidied. **RESIDUAL UNCERTAINTY:** the day-count basis of P14. **CONFIDENCE:** High that the discrepancies exist on the bytes; UNKNOWN which basis produces the printed figure.

### U.6 December 19, 1913: voluntary adjustment or compelled concession
**CLAIM A (the company and the Administration, in print):** "Wishing to put their affairs beyond fair criticism … at your suggestions"; "all of the suggestions of the Attorney General were accepted by the Directors"; McReynolds: "it seems to me clear that such action on your part will establish conditions under which there will be full opportunity … for competition"; Wilson: "very gratifying that the company should thus **volunteer** to adjust its business to the conditions of competition" (`P1S01` l.1704, l.1685, l.1849-1862, l.1876-1877). **CLAIM B (the same window's hostile print, and the company's own ledger):** the independents' side asserts a decade of "purchases at high prices of competing plants", a department "endeavoring, by threat and persuasion, to break down the continuity of Independent exchanges", and pamphlet-circulation "designed to influence the public mind toward monopoly" (`P1S03` l.745-768); and P2's own balance sheet still carries **$4,000,000** owed to Western Union for New York Telephone Co. stock, payable 1914 to 1915, in the year it promised to release Western Union (`P1S01` l.5089-5091). **WHY THEY DIFFER:** a settlement text describes itself as gracious, a competitor describes it as capitulation, and the accounts show the divestiture not yet executed. **EVIDENCE WEIGHT:** three contemporaneous voices, none independent of interest; the balance-sheet line is the only one that is an audited-style fact about the company's own position. **BEST-SUPPORTED INTERPRETATION:** the settlement is real, dated, signed and accepted — and its **motive is not knowable from this corpus**; the dossier records the undertaking and the unresolved liability, and does not choose between "voluntary" and "compelled". **RESIDUAL UNCERTAINTY:** whether any internal document shows resistance to a point; the 1914 execution of the Western Union disposal, which lies past the stage edge. **CONFIDENCE:** High (that the three statements exist); Low (any single motive reading).

### U.7 Who owns the legacy: the 2005 acquirer's sentence against the 1983 recital
**CLAIM A:** SBC, buying its own former parent, tells investors in a Form 425 letter that "SBC and AT&T are a potent combination, **sharing a legacy** of innovation, integrity and reliability" and that acquiring AT&T "secures our ability to remain a capable competitor" (`P1S10` l.42-44, l.57). **CLAIM B:** the same registrant's own 10-K prints that it was "incorporated … in 1983 **by AT&T** as one of seven regional holding companies" and was divested from it on 1984-01-01 (`P1S05` l.210-213) — i.e. the legacy was **split from it** for sixty-nine of the years in between, and the 1885–1913 record in this dossier belongs to the other registrant. **WHY THEY DIFFER:** a marketing instrument written for a sale compresses two registrants into one ancestry; a statutory recital keeps them apart. **EVIDENCE WEIGHT:** the 425 is a solicitation document and post-dates the whole of Stage 1; the 10-K recital is the registrant's own legal statement about itself. **BEST-SUPPORTED INTERPRETATION:** the 2005 sentence is **evidence of a 2005 claim**, and is admissible in this dossier only as the thing the hindsight firewall refuses (§Header 3). Stage 1 belongs to P2; nothing in it accrues to P4. **RESIDUAL UNCERTAINTY:** the exact date of the 2005 renaming, which no held byte prints (§S G-12). **CONFIDENCE:** High.

### U.8 Whose incorporation, and with how much money
**CLAIM A (as folklore would have it):** the window's origin company was capitalised at its 1885 incorporation. **CLAIM B (as the bytes have it):** the **only** sentence in any held non-SEC layer that joins an incorporation to a dollar amount describes a different firm — "Built in 1878 by some linemen as a speculation, it was sold to some members of the boards of trade of Chicago and Milwaukee and incorporated with a stock of $50,000… reorganized with a stock of $50,000 and $50,000 of bonds" — and that firm failed ("operated until 1905, when it went into receivership"), its lines then bought "in connection with the American Telephone and Telegraph Company" (`P1S01` l.2985-3020). **WHY THEY DIFFER:** one document's appendix reprint is the sole carrier of an incorporation figure in the entire in-window corpus, and it is somebody else's. **EVIDENCE WEIGHT:** the reprint is inside P2's own print, but it is titled "THE TRUE STORY" by its author and is a polemic, not a company statement. **BEST-SUPPORTED INTERPRETATION:** **P2's 1885 capitalisation is UNKNOWN (§S G-2)**; the Chicago & Milwaukee facts are recorded as the corpus's first incurred commercial failure and first documented acquisition by this registrant — and **not** as a failure of P4, which did not exist. **RESIDUAL UNCERTAINTY:** who wrote the appendix reprint and why it was included. **CONFIDENCE:** Medium (the reprint's contents); High (that no P2 capital figure exists in held bytes).

### U.9 Whose words are inside the 1908 pamphlet between l.204 and l.273
**CLAIM A:** the headed passages ("Promotion and Competition — Independent Companies", "Competition", "Public Control") are **the registrant's own 1907 words**, because the pamphlet says "Certain extracts from the report are reproduced below" at l.186-187 and then argues against them. **CLAIM B:** they are the **pamphleteer's own** text, because the OCR rendering carries no quotation marks or italic boundary and the section headings are the same style as Johnston's reply headings ("Independent Companies Not So Black as Painted", "One Bell Claim Inconsistent With the Purpose of its Argument"). **WHY THEY DIFFER:** an extract/plain-text boundary that the scan flattened. **EVIDENCE WEIGHT:** the framing sentence is explicit and printed; the typography is not recoverable from the text layer. **BEST-SUPPORTED INTERPRETATION:** treat the block as **most probably P2's 1907 text carried in a hostile vehicle**, cite it only with the attribution stated in the same sentence (as §F and §I.1 do), and let no §P row depend on it. **RESIDUAL UNCERTAINTY:** the whole of it, until a page image is read (R-4). **CONFIDENCE:** Medium (that the ambiguity exists); UNKNOWN (the resolution).

### Claim records (§U)

U01 Claim: Nine conflicts are declared, each with a register row, and none is resolved beyond the best-supported reading printed with it. — Date: 2026-10-06 — Source: this section — Source date: 2026-10-06 — URL: file-local — Archived: — — Tier: — — Class: **INFERENCE by the author on held bytes**, with each leg carried at its own line — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: as stated per anchor — Corroboration: per anchor — Conflicts: U.1-U.9

---


## Registers — APPLIED by the merge (not reproduced here)

**Emit-only as written; applied by the merge on 2026-10-07.** The nine blocks the author emitted at
`_parts/s1_p1.md` l.908–l.1096 are register data, not narrative (method §13), and they are **not reproduced here**:
they now live as the nine CSVs at this directory root, with the dossier-local `P1Snn` tags replaced by the minted
ids **S4449–S4462** per the map at the head of this file, and with the merge annotations described there. The
emission of record remains the read-only part.

| register | cols | data rows | key / integrity check at merge |
|---|---|---|---|
| `sources.csv` | 18 | **14** | keys **S4449–S4462**, 0 duplicates; 14 `notes` cells carry their `P1Snn` alias (COR-01); S4459/S4460 carry the NOT EVIDENCE framing; S4462 is the decoy shelf as a negative artefact |
| `quantitative.csv` | 12 | **44** | widths 12 on every row; 2 `UNKNOWN` rows kept as rows (§S G-2/G-6); `P14` (the non-footing annualised traffic rate) present with U.5 |
| `timeline.csv` | 11 | **28** | widths 11; 28 `source_id` cells all resolve to `sources.csv`; the 1915 row reads `CONTEMPORANEOUS as DESIGN; event UNKNOWN`; the two P4 rows carry `OUT OF WINDOW` |
| `decisions.csv` | 15 | **7** | widths 15; **residue named, not repaired:** the `claim_ref` cells of rows 4 and 5 print `L03` and `L07`, which match no claim-record id in this volume — §L's records are `L01`/`L02` and its table labels are `L-3`/`L-7`, the two same subjects. The merge applied the rows verbatim and handed the label to the audit pass (§14 rule 4) |
| `validation.csv` | 11 | **7** | block bound by content adjudication (COR-02); all 7 cite **S4449**, P2's own FY1913 print, and resolve |
| `failures.csv` | 11 | **10** | block bound by content adjudication (COR-02); includes the 1905 Chicago & Milwaukee receivership, which is P2's line and not P4's |
| `channels.csv` | 11 | **5** | widths 11; the 1913-12-19 interconnection channel is the window's only priced channel and cites U.6 |
| `conflicts.csv` | 15 | **9** | keys **U.1–U.9**, 0 duplicates, 1:1 with the nine anchors declared in §U |
| `data_gaps.csv` | 8 | **12** | widths 8; all five High-importance rows carry a follow-up task naming the route that could close them (R-1, R-2/R-3, R-5, or the CDX/periodical re-run §S UNTRIED asks for) |

**136 requested = 136 applied; 0 unapplied; 0 added by the merge; 0 folded; 0 rows moved between registers.** The
pre-write census, the post-write census, the id allocation and the `validation`/`failures` adjudication are recorded
in `03_quality_control/att_s1_merge.md`; live word and byte counts for every file are in `_MANIFEST.md`.


---

---

*End of part 1 — and of Stage 1 at this tier. Conflicts U.1-U.9 are declared in §U and each carries exactly one `conflicts.csv` row above; nothing is left pending in this file. Rows withheld from the emission blocks: none — every row drafted for a register is present in its block, and the five §F/§7 frames that do not fit a regulated network utility (first customer, unit price, churn, channel cost, founder compensation) are answered by the adapted equivalents in §F, §G, §K and §N plus `UNKNOWN` rows in `quantitative.csv` and `data_gaps.csv`, not by silent omission. One row was **moved rather than duplicated**: the Chicago & Milwaukee line appears in the timeline as an absorption event and in the failures register as a failure, and is registered as a conflict (U.8) only for the money-attribution question.*

**Not examined by this pass, stated once:** the three `DTIC_ADA*` layers beyond confirming they are decoys; the 26 `sources/sec/` documents this part does not cite (1996-2000 prospectuses, proxies and the 1998 Ameritech S-4 family, which belong to Stage 3); every sibling company; `MASTER_RESEARCH_LOG.md`; and `tools/`. No retrieval tool was run by this pass (0 web budget, authoring pass): every byte cited here was already in `sources/` when it started.


