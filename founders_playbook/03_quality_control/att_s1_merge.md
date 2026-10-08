# AT&T (company_035_att) Stage 1 — MERGE RECORD (final, 2026-10-07)

Agent `merge-att`. Operation: merge `_parts/s1_p1.md` (the only part; **36,595 words** as emitted, §A–§U
complete, Header + Stage boundary + sections A–U, **56 claim records**, nine fenced register append blocks
totalling **136 rows**, anchors `U.1–U.9` at 1:1 with nine conflict rows) into
`founders_playbook/01_companies/company_035_att/stage_1.md` + the nine registers at that directory root +
`_MANIFEST.md` + `CORRECTIONS.md` + `stage_1_index.md`, then gate it. `_parts/` is **read-only** to this pass:
nothing under it was edited, moved, renamed or renumbered, and it stays the emission of record. Every path this
pass wrote was taken with `python tools/scaffold.py claim --path <p> --agent merge-att` (14 paths) and released
with `--done`; **no `--force` was used.**

**I am the merger. I did not audit and I do not certify.** Everything below is arithmetic, geometry, id
allocation and the application of what the part emitted. The five-family table restates the probe's verdict as
carried by the part; the tier is **not re-tiered**.

## Register application account — 136 requested = 136 applied, 0 withheld, 0 added, 0 folded

| register | requested | applied | cols | status (verified on the bytes written) |
|---|---|---|---|---|
| `sources.csv` | 14 | **14** | 18 | APPLIED 14 rows (keys **S4449–S4462**, 0 duplicates) |
| `quantitative.csv` | 44 | **44** | 12 | APPLIED 44 rows (0 duplicate row texts; 2 `UNKNOWN` rows kept) |
| `timeline.csv` | 28 | **28** | 11 | APPLIED 28 rows (0 duplicates; 12 rows carry a `conflict_ref`) |
| `decisions.csv` | 7 | **7** | 15 | APPLIED 7 rows (0 duplicates) |
| `validation.csv` | 7 | **7** | 11 | APPLIED 7 rows (block bound by content adjudication, COR-02) |
| `failures.csv` | 10 | **10** | 11 | APPLIED 10 rows (block bound by content adjudication, COR-02) |
| `channels.csv` | 5 | **5** | 11 | APPLIED 5 rows (0 duplicates) |
| `conflicts.csv` | 9 | **9** | 15 | APPLIED 9 rows (keys **U.1–U.9**, 0 duplicates) |
| `data_gaps.csv` | 12 | **12** | 8 | APPLIED 12 rows (0 duplicates) |
| **TOTAL** | **136** | **136** | — | **0 unapplied; every requested row is on disk** |

**No row was dropped, merged away, deduplicated or withheld, and none was added beyond the emission.** Headers
are byte-equal to the `company_001_amazon/` conformant headers (string equality, checked before each write);
`stage` is the literal `stage1` on all 136 rows; widths are 18/12/11/15/11/11/11/15/8 with **0 rows off header
width**.

**Cross-block duplicate-key check** (run across all nine blocks of this one operation together, not per block):
**0 exact duplicate rows** anywhere in the nine registers; `source_id` unique 14/14; `conflict_id` unique 9/9;
no key was emitted by two blocks (one part, one emission — the check still ran, because the duplicate that
`gate_csv` fails on is a key repeated in the register, and the only way to know is to count it after the write).
**Verbatim check, row by row, part vs disk:** 120 rows are identical after the mechanical id substitution;
**16 rows differ only by a merge annotation appended to the end of their existing last cell** (14 `sources.csv`
`notes`, 1 `validation.csv` `notes`, 1 `failures.csv` `notes`); **0 unexpected edits.** No value, date, source
key, evidence class or confidence on any applied row was altered, and no row moved between registers.

## Census BEFORE any write (run first, per the wave plan)

`python tools/merge_census.py --company-dir founders_playbook/01_companies/company_035_att --verbose`
(2026-10-07, before the first byte of this merge was written): 9 structured blocks parsed; **2 block-groups
could not be attributed**; per register — channels 5 requested / 5 unkeyed, conflicts 9 / **9 missing keyed**
(`s1_p1.md:U.1 … U.9`), data_gaps 12 / 12 unkeyed, decisions 7 / 7 unkeyed, quantitative 44 / 44 unkeyed,
sources 14 / **14 missing keyed** (`s1_p1.md:P1S01 … P1S14`), timeline 28 / 28 unkeyed.
**`TOTAL missing keyed rows: 23`**, `present` = 0 everywhere because the company held no register CSV at all
before this pass.

## Census AFTER the write

Same command, after the nine CSVs were written: **conflicts 9 requested / 9 present / 0 missing** — the keyed
anchor rows verify by key. **sources 14 requested / 0 present / 14 keyed-missing**, `TOTAL missing keyed rows:
14`. Those 14 are the re-key, not an absence: the census keys `sources.csv` on the literal string the part asked
for (`P1S01`…), and **COR-01 supersedes those provisional tags with the minted ids S4449–S4462**, which is what a
merge is required to do. All 14 rows are on disk, each carrying its `P1Snn` alias in its own `notes` cell so the
census string can be recovered by reading the row, and the map is printed in `stage_1.md` and here. The 7
unkeyed registers cannot be censused by key at all (the tool counts them), so they were verified by counting the
written files, per the table above. The 2 unattributed block-groups stay unattributed **by construction**:
`validation.csv` and `failures.csv` have byte-identical headers, so no schema-based attribution is possible for
any company, and the census exit code never turns on them.

## The validation / failures adjudication (the census cannot decide; I did, by reading)

Three rules, in order. (1) **Declared target.** Each `>>> REGISTER ROWS FOR MERGE <<<` marker names its target,
and `_parts/NOTES_att_p1.md` §5 declares validation **7** · failures **10** — exactly what the two blocks parse
to, so no count tension exists. (2) **Counts close.** 7 + 10 = 17 = the rows the census listed as unattributed,
and no row appears in both groups. (3) **Content, row by row**, against Amazon's conformant usage (`validation` =
a signal that validated something; `failures` = an incurred adverse signal): the 7-row group's
`what_it_demonstrated` cells are all validations (the 1912 New York–Washington and 1913 Boston–Washington
underground conversations, the 1913-12-19 acceptance by the Administration, the shareholder base reaching 55,983,
station and wire-mile growth, the ten-of-eleven cross-foots, the asserted self-financing capacity); the 10-row
group's are all incurred negatives (the defective tinsel-braid cable, lead-sheath corrosion, the 1884–87 Boston
cable failures, the 1883 1,500-foot ceiling, the 1905 Chicago & Milwaukee receivership, the Central Union consent
to receivers, surplus earnings falling to 11,735,194, the independent wave's own collapse, the loud-speaking
promotions, the asserted wholesale obsolescence). **The binding is recorded in the register itself**: the last
row of each block carries `· merge note: this N-row block is bound to \`validation.csv\`/\`failures.csv\` by
content adjudication (COR-02)`.

**Tool finding, recorded not repaired.** The content hints `merge_census.py` printed for these two groups were
the **decisions** block's rows: the AMBIGUOUS branch calls `hint_validation_or_failures(data)` before `data` is
assigned for that block, so it reports the previous iteration's rows. The adjudication was therefore made from
the block text, never from the hints. Same class as the note CVS's merge recorded; this pass changed no tool.

## Id allocation (minted centrally, above every live id, never into a gap)

`python tools/id_mint.py --audit` before minting: 351 distinct issued ids, range `S0001–S4430`, registry claims
held through `S4448` (`company_006_cvs`), tool's own **`next assignable: S4449`**. The audit's collision list
(`S0001`–`S0010` cited by both Amazon and Tesla; `S4222–S4229` by both Microsoft and Target) sits below this
range and was **not** touched or attempted-repaired by a merge.

Minted: `python tools/id_mint.py --count 14 --company company_035_att --claim --agent merge-att` →
**S4449 … S4462**, contiguous, 14 ids, recorded in `00_universe/_ID_BLOCKS.tsv` against `company_035_att /
merge-att`. Binding: `P1S01→S4449` (FY1913 Annual Report), `P1S02→S4450` (1887 conference print), `P1S03→S4451`
(1908 Johnston pamphlet), `P1S04→S4452` (CIK 5907 FY1993 10-K — the 1885 recital), `P1S05→S4453`, `P1S06→S4454`,
`P1S07→S4455`, `P1S08→S4456`, `P1S09→S4457`, `P1S10→S4458`, `P1S11→S4459` (quarantined 5907 index),
`P1S12→S4460` (732717 index), `P1S13→S4461` (probe pointer), `P1S14→S4462` (DTIC decoy shelf). Every `P1Snn`
citation in every applied register cell was replaced by its minted id **including inside prose cells**
(`claim_a_source`, `claim_b_source`, `best_available_evidence`); the narrative keeps the author's local tags and
is keyed by the map printed at the head of `stage_1.md`. Verified: 0 residual `P1Snn` **citations** in the
registers (the 14 remaining occurrences are the COR-01 alias annotations themselves), and 0 unresolvable `S####`
tokens — `gates.py` reports `all S#### tokens resolve` on all five registers with a `source_id` column.

## Volume geometry — one volume, kept

| file | words | bytes | what it is |
|---|---|---|---|
| `stage_1.md` | **31,315** | 199,903 | merge record + Header, Stage Boundary, §A–§U, **56 claim records**, §S requests/UNTRIED, §T ledger, register-application record |
| `_parts/s1_p1.md` (read-only) | 36,595 | 251,090 | the emission of record, incl. the nine fenced blocks (8,067 words of register data) at l.908–l.1096 |
| `CORRECTIONS.md` | 1,508 | 10,333 | COR-01…COR-04 + "Not corrected, and why" |
| `stage_1_index.md` | 832 | 5,418 | reading order, address spaces, anchor → register homes |
| the nine registers | 8,045 | 67,554 | 136 rows × the widths above |

**36,595 words exceeds the T2 planning figure (22,000/stage) and is inside the 60,000 hard cap, so the dossier
stays a single volume** (§9.3's split trigger is the hard cap and a section boundary, not a density target;
RD-122). After the register blocks left the prose for their CSVs and the merge record went in, the volume
measures **31,315 words = 142% of the tier target, 78% of the 40,000-word soft target, 52% of the hard cap.** The
overage is recorded as the advisory it is; **no prose was edited, trimmed or split to satisfy the tool.**

**Why the gate was run with `--tier core` and said so.** `--tier auto` resolves the tier from a **verdict-bearing
line** in `research/*.md`; AT&T's probe states its per-stage tiers **as table rows**, so auto had no verdict line
to read. Measured on this company it prints `tier: T2 … 13 mentions, 0 on a verdict line` — it lands on T2 only
through the mention tie-break, the same path that printed **T3** for Cigna's probe on this tool. The explicit
`--tier core` pins the same 22,000-word target without leaning on a tie-break.

## Anchor parity

**9 narrative anchors ↔ 9 register anchors; 0 residue in either direction.** §U declares
`<!-- ANCHORS: U.1-U.9 -->` and writes §U.1–§U.9; `conflicts.csv` holds exactly nine rows keyed `U.1 … U.9`,
one per anchor. Measured twice: `gates.py --checks anchors` (`anchors parity 9 narrative anchors <-> 9 register
anchors`; `citation resolution … 9 distinct ids across registers and volumes`) and independently, by scanning
every `U.nnn` token in all nine registers against the declared set. Every anchor has at least one citing home
besides its own `conflicts.csv` row: `U.1` sources ×7, timeline ×1 · `U.2` sources ×3, timeline ×4 · `U.3`
quantitative ×1, sources ×1, timeline ×2 · `U.4` sources ×2, timeline ×2 · `U.5` quantitative ×3, failures ×1,
sources ×2, timeline ×2 · `U.6` decisions ×1, validation ×1, channels ×1, sources ×1, timeline ×1 · `U.7`
sources ×4 · `U.8` failures ×1, sources ×2, timeline ×1 · `U.9` data_gaps ×1, sources ×3. The full home map is
in `stage_1_index.md`.

## The two AT&T-specific things, preserved rather than tidied

**(1) Four legal persons, named per section.** P1 Bell Telephone Company / American Bell (never a reachable
registrant — held only as officers and cables of *a different company* inside P2's own 1887 print), **P2 = CIK
0000005907, New York, 1885**, P3 the seven 1983–84 RHCs, **P4 = CIK 0000732717, Delaware 1983 → SBC → AT&T Inc,
the ticker's registrant**. The 1885 answer is **S4452** — P2's own FY1993 10-K l.238 — and its `evidence_class`
cell reads **`RESTATED as to 1885`**, so it cannot be read as an in-window document or attached to 732717; the
P4 rows (S4453–S4456) are labelled as the 1983 line and never used to date the brand's century. The quarantined
5907 index is registered as **"NOT EVIDENCE — a search-index row and a guard verdict are measurements of the
archive's reach"** **with its perimeter** (S4459: 1,255 filing rows, 1994-01-07 → 2007-01-18, earliest 10-K row
1994-03-25, 320 rows without `primaryDocument`), alongside S4460 for the 732717 side (7,922 rows, 1994-02-14 →
2026-10-02). 1915 stays in the **future tense**: S4449 l.400–402 is design evidence, the timeline row reads
`CONTEMPORANEOUS as DESIGN; event UNKNOWN`, and the author's new finding — that the layer's **second** `1915` hit
at **l.5091** is a 1914→1915 **stock-payable maturity** ("Indebtedness to Western Union Telegraph Co. for New York
Telephone Co. Stock Payable 1914 to 1915 … 4,000,000.00"), not an opening — is carried in §Boundary 2 and in
U.6's claim B, and is named in COR-03. The two out-of-window P4 timeline rows are kept, marked `OUT OF WINDOW`,
so no later pass can place 1983/1984 silently in the ticker registrant's infancy. **Nothing here was
re-tiered, re-dated or consolidated into "AT&T".**

**(2) Word count versus tier** — recorded above: single volume, overage advisory, no prose cut.

## Gate

`python tools/gates.py --company-dir founders_playbook/01_companies/company_035_att --tier core --out 03_quality_control/att_s1_gates_merge.md`
→ **exit 0**, **Findings: 2 | Passes: 18**, and **both findings are advisory**:
`advisory | stage_1.md | 31315 words over the core (this volume's issued tier) density target 22000 -- NOT a split
mandate and NOT a defect`
and `quotes | ADVISORY | 33 of 60 checked spans unmatched (55%) -- gate precision is not established, treat as a
triage list, NOT as defects`. Passes include all nine register widths
(timeline 28×11, quantitative 44×12, conflicts 9×15, sources 14×18, data_gaps 12×8, validation 7×11, failures
10×11, decisions 7×15, channels 5×11), `all S#### tokens resolve` on every register with a `source_id` column,
`keys … 14 source tokens all resolve`, `anchors parity 9 <-> 9`, and `corrections propagation … all 4 retraction(s)
reach registers and volumes`. Notes: `coverage 9 registers, 1 stage volumes, 39 source documents`;
`keys … cites 1 hyphenated record keys: S6-11` (expected, see below); `keys … mentions 3 retired keys inside
collision/re-key/range text -- protected history, not re-pointed: S0001, S4430, S4448` (the mint-context ids in
the merge record, deliberately backticked so the gate reads them as history). Written to both QC locations:
`03_quality_control/att_s1_gates_merge.md` (the literal `--out` path) and
`founders_playbook/03_quality_control/att_s1_gates_merge.md` + `.json`, next to `att_s1_gates_p1.md`.

**Before → after.** Pre-merge (`att_s1_gates_p1.md`): `Findings: 1 | Passes: 0`, coverage "no register CSVs at
root or research/", anchors "no register anchors found -- UNANSWERED, not passed", corrections gate DID NOT RUN.
Post-merge: every one of those gates runs and passes; the only remaining findings are the two advisories.

**Quotes triage, named for the audit pass and NOT repaired by the merge.** 33 of 60 attributed spans and 64
unattributed spans do not match the squashed local corpus. Re-running the gate's own matcher over the volume,
**100 of the 235 failing spans contain markdown emphasis (`**`) inside the quotation marks** — the author's
honest emphasis on words inside a quotation, which no whitespace-normalising matcher recovers; the rest are
scare-quotes/labels (including phrases quoted from the gate output itself) and fragments the author joined across
wrapped lines. A merge may not rewrite another pass's quotations (§14.10 and rule 4 bind both of us), so the
adjudication — emphasis vs paraphrase — is the citation/verbatim auditor's job, and this paragraph is the hand-off.

## Five families, as the part carried them (this pass ran no retrieval)

| family | verdict carried | route status |
|---|---|---|
| (a) SEC / EDGAR | **TRIED–ANSWERED** | bytes on disk; the 1885 recital (S4452), the 1983/1984 recital (S4453–S4456), two measured perimeters, **no in-window document** |
| (b) web archives / CDX | **UNTRIED — for lack of any route** | `tools/web_domains.json` cites **no domain for `att`** (`slugs` = centene, cencora, relevance, marathon, microsoft, target), so the family cannot even be scoped; the ask is a cited domain, and it is recorded as UNTRIED, **not empty and not null** |
| (c) periodical corpora | **TRIED–ANSWERED, thin**; the name-discovery re-runs TRIED–UNANSWERED | one opened third-party carrier (S4451, hostile print); `ca_endpoint_probe.py` / `periodical_harvest.py --company att --facet-free` still open |
| (d) digitised corporate print | **TRIED–ANSWERED — the strongest family** | S4449 and S4450 carry §E, §J, §K, §L, §M, §N, §P, the 1915 design statement and the 1877 epoch |
| (e) auction / museum / manuscript | **UNTRIED — for lack of any route, and UNIMPLEMENTED** | no auction/museum endpoint exists in any `tools/*.py`; structurally UNTRIED for every company, and it is exactly where the three documents Stage 1 most needs live (§S R-5) |

**Family (b) and family (e) are UNTRIED because there is no route to try, not because a search came back
empty** — the two are different findings and are labelled differently in every file this pass wrote.

## Not applied, not attempted, and why

1. **`conflicts.csv` — 9 of 9 applied. `sources.csv` — 14 of 14 applied. No register row in this dossier was
   refused.** The pre-merge emission declared "rows withheld: none", and the merge matched it: **136 requested,
   136 applied**. There is no refused row to name.
2. **`stage_1.md` §T.4's periodical-shelf byte total — NOT rewritten.** The volume still prints **660,753 B**,
   which `NOTES_att_p1.md` §2 supersedes at **707,735 B** over the same six `.txt` layers (re-measured by this
   pass too: 6 layers, 707,735 B documents; 710,420 B with the six sidecars). §14 rule 4 bars a merge from
   silently re-issuing another pass's number, so the supersession is carried as **COR-03**, is printed in
   `sources.csv` S4461's `notes` cell, and is handed to the audit pass to decide. **This is the one figure the
   merge knows to be stale inside the volume, and it is named rather than fixed.**
3. **`S6-11` left as print, not re-pointed.** The string is the DTIC document code **`S6-11-25-ATT`**, quoted in
   §Header 1 and §T.6 to demonstrate that a bare `att` token is a substring of somebody else's code. `gates.py
   --checks keys` lists it as a hyphenated record key for review; the merge minted **no** register key or source
   row for a document code (RD-131's shape) and changed **no** quotation. Same protection applied to
   `S0001`/`S4430`/`S4448`, which appear in the merge record only as backticked history of the mint.
4. **Two `claim_ref` cells in `decisions.csv` — applied verbatim, residue named.** Rows 4 and 5 print `L03` and
   `L07`, which match no claim-record id in the volume (§L's records are `L01`/`L02`; its table labels are
   `L-3`/`L-7`, the same two subjects). The merge did not rewrite a cross-reference it did not mint; named here,
   in `stage_1.md`'s application table and in `CORRECTIONS.md` ("Not corrected, and why"), for the audit pass.
5. **The five `FETCH REQUEST` blocks (R-1…R-5) and the probe's standing asks — NOT run.** They are the
   orchestrator's dispatch list; this pass had 0 web budget, and §14 rule 6 keeps each untried route named rather
   than reported empty. R-1 (HTTP 401), R-2 (0 B / HTTP 503 on five volumes) and R-5 (no tool) stay open exactly
   as the author left them, and every High-importance `data_gaps.csv` row still names its route.
6. **No de-duplication by deletion, no register created elsewhere, nothing moved.** The nine registers were
   created at the **company root** (Amazon's geometry; `gates.py::locate()` reads root first).
   **No third emission exists** for this company: `research/` holds only `A_chronology_feasibility.md` and
   `A4_harvest_mine.md`, and a `find . -name "*.csv"` over the whole company after the write returns only these
   nine at the root plus `sources/` intake artefacts (`_MANIFEST.csv`, `_PLAN.csv`, `_SKIPPED.csv`,
   `_UNANSWERED.csv` and the four submissions indexes), none of which is a register emission the census would be
   blind to (the wave plan's Tesla case — 25 rows in `research/*.csv` — has no counterpart here).
7. **Nothing was re-tiered, re-numbered or re-dated.** Claim ids (`BD01–BD04`, `A01`…`U01`, 56 distinct), §P
   metric ids, the four `P1`–`P4` person labels and the anchors `U.1–U.9` stand as the author minted them; the
   author's own re-issue of the four §Boundary ids from `B01–B04` to `BD01–BD04` survives untouched.
8. **Carried evidentiary positions, unchanged by the merge:** the 1885 answer is RESTATED and belongs to CIK
   5907 (U.1/U.2); 1915 is design, not event (U.3); 1984 is a two-person event, not one company's birth or the
   other's failure (U.4); the printed non-footing traffic rate carries no substituted value (U.5, `P14`); the
   1913-12-13 motive is unresolved across three interested voices (U.6); the 2005 "sharing a legacy" sentence is
   evidence only of a 2005 claim and stays the object of the firewall refusal (U.7); P2's 1885 capitalisation is
   UNKNOWN and the only incorporation-with-money sentence in held non-SEC bytes describes a **different, failed**
   firm (U.8); the 1908 pamphlet's l.204–273 block stays "most probably P2's 1907 text carried in a hostile
   vehicle", attributed in the same sentence (U.9). No averaging, no silent resolution.

## Tool-call budget

Ceiling 130; this pass closed out **before the 100-call close-out mark** (roughly 80 tool calls). The merge report
was written **incrementally** — the census-before, the request tally and the PENDING register table were on disk
before the first register byte, and each section was replaced with its measured account as the work completed, so a
stoppage would have left the account readable rather than absent. All 14 claimed paths were released `--done`; no
claim was forced.

## What this pass did NOT examine

The 26 stored SEC documents under `sources/sec/` that Stage 1 does not cite; the three DTIC layers beyond
counting them as decoys; `sources/_index/` beyond the two perimeter measurements the part already printed; every
sibling company except `company_001_amazon/` (**for format only** — no Amazon value, date or phrasing was
imported) and the three same-wave merge records read as shape precedents (`cigna_s1_merge.md`,
`cvs_s1_merge.md`, `apple_s1_merge.md`); `MASTER_RESEARCH_LOG.md`; and `tools/*.py` read only for check and
census semantics (`gates.py`, `merge_census.py`, `id_mint.py`, `scaffold.py`) — no tool was modified.
**No retrieval was attempted: 0 WebSearch, 0 WebFetch, 0 `sec_intake`/`harvest_mine`/`periodical_harvest`/
`ia_text`/`cdx_intake` runs.** Every byte cited in the merged volume was already on the shelf when this pass
started.
