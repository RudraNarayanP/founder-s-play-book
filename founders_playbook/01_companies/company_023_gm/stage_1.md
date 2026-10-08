# FORENSIC LONGITUDINAL DATASET — GENERAL MOTORS, STAGE 1 (1908 ACT OF INCORPORATION – 1920-11-30 PROPOSED; 1930-12-31 AS OPERATIVE SEARCH WINDOW)

## MERGE RECORD (assembly, application, id map, adjudications, parity, carry-forward)

Merged 2026-10-07 by `merge-gm` from the single part `_parts/s1_p1.md` (author `s1-gm-p1`; 25,046 words as
emitted; Header, Stage boundary, §A–§U, the claim-record appendix GM1-C01…GM1-C33, and nine register append
blocks; every section marked `STATUS: WRITTEN`, no PENDING section left). **Section letters, claim ids, metric
ids and `U.nn` anchors are the author's and were not renumbered** — method §9.3: numbering continues, it is
never re-based. No sentence of narrative was rewritten, trimmed, averaged, re-tiered or merged away. `_parts/`
is read-only to this pass: it was not edited, moved, renamed or pruned, and it stays the emission of record.
Nothing here is an audit and nothing here is a certification.

**What was moved out of the prose, and why.** Two moves, both geometry, neither a content cut. (1) The part's
nine fenced `csv` blocks (114 rows) are register data, not narrative (method §9.1(2), §13): they are **applied
to the nine CSVs at this directory root**, and the `## REGISTERS` heading below now points at that application
instead of repeating the blocks; their verbatim text survives at `_parts/s1_p1.md` l.616–l.781. Apart from the
central `source_id` re-mint documented below, no cell was edited. (2) The **claim-record appendix**
(GM1-C01…GM1-C33, 2,801 words, one record per line, 33 lines) moved to the companion deliverable
`stage_1_claim_records.md` at the **§U / claim-record section boundary** — §9.1(3) and §9.3 allow exactly this
cut, it is the cut the author named in `_parts/NOTES_gm_p1.md` §8, and `gates.py`'s `stage_docs()` treats a
claim-record appendix as a companion rather than a narrative volume. Record ids are unchanged and nothing was
renumbered. Both moves together are what bring this volume inside the **T2 22,000-word target the probe
issued**, with evidence intact — §9.6 forbids cutting evidence to fit a limit, and no evidence was cut.

### Register application (requested ↔ applied, re-measured off the bytes on disk)

| register | rows requested | rows on disk | cols | status |
|---|---|---|---|---|
| `quantitative.csv` | 26 | **26** | 12 | APPLIED 26 rows |
| `timeline.csv` | 30 | **30** | 11 | APPLIED 30 rows |
| `sources.csv` | 8 | **8** | 18 | APPLIED 8 rows |
| `conflicts.csv` | 10 | **10** | 15 | APPLIED 10 rows |
| `data_gaps.csv` | 13 | **13** | 8 | APPLIED 13 rows |
| `decisions.csv` | 8 | **8** | 15 | APPLIED 8 rows |
| `validation.csv` | 6 | **6** | 11 | APPLIED 6 rows |
| `failures.csv` | 8 | **8** | 11 | APPLIED 8 rows |
| `channels.csv` | 5 | **5** | 11 | APPLIED 5 rows |
| **TOTAL** | **114** | **114** | — | every row on disk at its header width |

Unapplied rows: **none.** No row was dropped, folded into another, or added by the merge. Widths are uniform per
register, with zero empty cells and zero off-width rows. Header rows were compared against the corresponding
Amazon register column-for-column before writing (all nine identical).

### Id map (provisional → minted; the merge mints, authors do not)

`tools/id_mint.py --audit` first: 343 issued ids, range `S0001–S4422`, `next assignable: S4423`. Minted
`--count 8 --company company_023_gm --claim --agent merge-gm` → **S4423–S4430**, contiguous and **above every
live id**, so no gap was re-entered and the known live collision (`S4222–S4229`, cited by both
`company_011_microsoft` and `company_042_target`) was neither allocated into nor repaired here. The part's
narrative carries no `Snnnn` token, so the mint touches only the registers and the eight source rows below.

`PROV-FH28`→**S4423** (`financialhistory00selt`, 1928) · `PROV-AR37`→**S4424**
(`general-motors-annual-reports`, file `gm1937_djvu.txt`, FY1937) · `PROV-NPSH29`→**S4425** (`NPSH19290609`,
printed 1929-06-09) · `PROV-DW20`→**S4426** (`daytonwrightairp00gene`, 1920) · `PROV-TRUCK31`→**S4427**
(`GeneralMotorsTruckCo`, 1931, refused into Stage 1) · `PROV-CF95`→**S4428** (`commercialfinanc61newyuoft`, an
1895 shell used as a negative control) · `PROV-SEC1467858`→**S4429** (EDGAR CIK 1467858 index + 40 filings,
floor 2009-07-16, perimeter statement only) · `PROV-A4MINE`→**S4430** (`research/A4_harvest_mine.md`, pointer
only, never evidence). `PROV-*` now survives only in the read-only part and in this map; method §9.4 holds —
`sources.csv` is global-append-only, an id is reused, never redefined. The claim-record appendix's own preamble
still reads "`source_id` values in the registers are provisional (`PROV-*`) and are re-minted centrally at
merge"; that line is kept verbatim as a record of the part's state, and the map above is its fulfilment — the
registers on disk contain **no** `PROV-*` token (re-checked after writing: 0 occurrences).

### Duplicate-key and cross-block checking

Measured on the written rows, not on the blocks: **zero** identical rows within or across all nine blocks
(normalised full-row comparison); zero duplicates on `source_id` (8), on `conflict_id` (10), on `(date, metric)`
(26), `(date_or_range, event)` (30), `(date, decision)` (8), `channel` (5) and `(date, signal_or_failure)` in
both validation (6) and failures (8); `gap` keys run **G-01…G-13 with no gap and no repeat**;
`validation ∩ failures = 0` rows. Cross-register tension was also read, not only hashed: the timeline row for
1916-10-13 and the source row S4424 cite the same two-lineage act on purpose (one corporate-record lineage, gap
G-12) — that is one document cited twice, not a duplicate row, and the dossier says so in terms.

### The validation / failures adjudication (the census cannot decide; the reason is recorded)

The two registers share a **byte-identical 11-column header**, so `merge_census.py` printed the 6-row and the
8-row groups together as `AMBIGUOUS:validation.csv,failures.csv`, with content hints reading "either |" on all
14 rows: the tool refuses to decide, and a keyword split would have decided wrongly in both directions. Applied
by reading, in this order. (1) The part's own `>>> REGISTER ROWS FOR MERGE <<<` markers name `validation.csv` at
l.747 and `failures.csv` at l.759, and `_parts/NOTES_gm_p1.md` §8 states the same widths (6×11, 8×11). (2)
6 + 8 = 14 = exactly the unattributed rows, and the two groups share no row. (3) Content: the 6 rows are each a
signal that **validated** something — the 1908-10-01 exchange clearing, the 1910-11 full advance sale of the
notes, the 1915-10-15 first cash dividend on the common, the 1915-10-01 voting-trust expiry handing Durant's
group the near-majority, the 1916-05 United Motors distribution at $62 a share, the 1918-20 internal
self-financing — while the 8 rows are each an **incurred negative** — the abandonment of all but the Oakland of
the eight added lines, $600,000 lost unwinding the Elmore leg, the Ford option and Maxwell-Briscoe memorandum
lapsing, the 21%→7.8% share collapse, $12,531,013.19 of write-offs, the bankers' plant closures on partisan
testimony, the 1921-22 Sheridan and Scripps-Booth liquidations, the lost Dodge Brothers bid. **No row moved
between the registers.** The `what_it_did_not_demonstrate` cells in the validation rows are limits on a positive,
which is what that column exists for, and are not misfiled failures.

### Anchor ↔ conflict parity

10 anchors declared (`<!-- ANCHORS: U.01-U.10 -->`, l.3) ↔ 10 `### U.nn` sections written in §U (l.536–l.565) ↔
10 `conflicts.csv` rows keyed **U.01–U.10**. One-to-one, same ids both ways, no gap, no declared anchor without
a row, no register anchor without a written section. Nine of the ten are additionally cited from other registers
(`timeline.conflict_ref`, `quantitative.notes`, `sources.notes`, and the claim records' `Conflicts:` cells);
**U.03 is cited nowhere but its own §U.03 section, its `conflicts.csv` row and one narrative line at §B.1** —
named here, with no row invented to balance it, so a later pass does not "fix" an asymmetry that is the author's.

### Two GM carries the merge kept instead of smoothing

**1. An index label misreporting a year is a corpus-level hazard, so it stays registered, not corrected.**
`research/A4_harvest_mine.md` stamps the 197,373-byte layer `? / title:1918 | in-window |
TIER1_CANDIDATE_TEXT`, while the layer's own first pages print **"TWENTY-NINTH ANNUAL REPORT OF GENERAL MOTORS
CORPORATION / YEAR ENDED DECEMBER 31, 1937"** (L3-7), date the meeting to Wilmington, Delaware, 1938-04-26
(L20-21), and carry the sidecar URL naming the file `gm1937_djvu.txt`. It is **registrant-record material used
only as `RETROSPECTIVE`**: source row S4424 is classed `RESTATED / RETROSPECTIVE SOURCE`, every Stage-1 fact it
carries is tagged `RETRO` in `timeline` and in the claim records, and it was never used as an in-window carrier.
The mismatch stays live in three places: **`conflicts.csv` U.09** (both claims, the "the printed page wins"
weight of RD-121 class, and the residual question whether the same multi-file item holds genuine 1918-1920
reports), **`data_gaps.csv` G-04** (the enumerate-the-whole-item follow-up), and the **`sources.csv` S4424
note** ("A4 stamped this item 'title:1918 / in-window'; the layer prints 1937 — see U.09"). A harvester's
`title:` metadatum is not a document date and a `TIER1_CANDIDATE_TEXT` promotion is not evidence; nothing in
this volume was dated from either.

**2. The author's own withdrawn over-claim stays visible.** The part's first draft asserted its naming counts
held "over all six held layers". The author **withdrew that phrasing** because every count in this file is
**line-wise over OCR layers, and is therefore a floor, not a census** (method §14.14): the withdrawal is
recorded in the dossier itself — the §B.2 caveat, repeated in §I.3 and §R.2 — and in `_parts/NOTES_gm_p1.md` §8.
The merge left the text exactly where the author put it, restates it here so a reader of the merged volume
cannot miss it, and did not re-inflate any zero into an absence claim: `General Motors of Canada`,
`General Motors, Limited` and `General Motors of New York` are 0-line results on held layers, while the
Canadian and UK registry routes remain **UNTRIED** (G-09) — which is precisely U.07's residual uncertainty.

### Corrections seeded at merge (`CORRECTIONS.md`; gap G-13 answered)

`data_gaps.csv` **G-13** names the QC/merge owner as the owner of a `CORRECTIONS.md` this company did not have,
and asks that it be seeded from **U.04, U.05, U.06, U.07 and U.09**. It now exists, with nine entries, each
printed here as well, because method §14.10 wants a retraction in **both** layers (and `gates.py --checks
corrections` measures exactly that propagation): **COR-01** provisional `PROV-*` carrier keys superseded by the
minted **S4423–S4430** · **COR-02** the 6-row block is `validation.csv` and the 8-row block is `failures.csv`,
with no row moved · **COR-03** the claim-record appendix relocated to `stage_1_claim_records.md`, ids unchanged ·
**COR-04** the inherited "1910 receivership" premise refuted (U.04) · **COR-05** "Durant expelled in 1916"
re-dated to two attested acts (U.05) · **COR-06** "the 1920 Fisher merger" split into four printed acts
(U.06) · **COR-07** Fiat-of-Canada / Anderson / Sheridan / London unsupported on held bytes (U.07) ·
**COR-08** the `A4` `title:1918 / in-window` stamp against a layer printing 1937, kept as a **corpus-level
hazard** at U.09 / G-04 / S4424 rather than smoothed into a typo · **COR-09** the author's own withdrawal of "over
all six held layers", since line-wise counts are floors and not censuses.

**The register annotations are append-only.** Each tag was written at the end of an existing `notes` /
`residual_uncertainty` / `claim_supported` / `follow_up_task` cell. No value, date, metric, carrier key, evidence
class or confidence on any of the 114 applied rows was altered; no row was folded. `research/A4_harvest_mine.md`
— another pass's emission, and the file carrying the wrong stamp — was **not** edited: the correction lives in
the register layer and the dossier, where a reader of the evidence will meet it.

### Not applied, and handed forward by name

- **Rows: all 114 applied, none dropped.** The part's emission note (l.614) contains one self-contradictory
  sentence — "One row was withheld from every register: no row anywhere asserts a figure absent from a held
  line" — whose second clause states the opposite of its first. Nothing was withheld from the nine blocks the
  census parsed (114 rows requested, 114 on disk). The merge applied what exists and hands the wording to the
  audit pass rather than re-reading it silently.
- **FETCH REQUESTs: not run.** The four blocks in `_parts/NOTES_gm_p1.md` §6 — enumerate the whole
  `general-motors-annual-reports` item; retry the seven HTTP-503 in-window Google Books ids;
  `sec_intake.py index 140139` plus a `--max-docs 400` re-run; the Canadian/UK registry and the auction/museum
  route — are the orchestrator's dispatch list. This pass used **0 WebSearch / 0 WebFetch** and has no
  retrieval mandate, so they stay open as G-01, G-02, G-04, G-08, G-09 and G-10. None of them is read as a null.
- **Defects recorded, not repaired here** (method §14 rule 4 binds the merged text to the part): (i) three
  dangling cross-references to a section **§V** this part never wrote — l.7 "see the tier note in §V.3", l.17
  "used only as a negative control (§V.2)", l.44 "§V.3 records the disagreement". The substance they point at
  is present (§S G-01/G-13 and `_parts/NOTES_gm_p1.md` §2), so the address is wrong, not the claim. (ii) The
  part carries **no `## Untried` heading**; its untried routes live in §S's gap rows and in NOTES §5. (iii) The
  tier reader: `gates.py --tier auto` stamps **T3** from `research/A_chronology_feasibility.md` because the
  dossier's Stage-1 verdict — **T2 core**, §3's table row — sits on a table row the "verdict line" heuristic
  cannot see. The budget check was therefore run with **`--tier core` explicit**, as the tool's own message
  asks; the dossier was not edited to satisfy the tool and no data was reshaped to silence a gate.

STATUS: WRITTEN

---

<!-- ANCHORS: U.01-U.10 -->

**Company:** General Motors — Stage-1 dossier, `company_023_gm`. The name attaches to **four different legal persons** and this file never lets a bare "GM" stand for more than one of them (§U.01).
**File:** Stage 1, part 1 of *n* — Header, Stage boundary, sections **A–U**, and the nine register append blocks. Written by `s1-gm-p1`.
**Tier:** **T2 core**, inherited from `research/A_chronology_feasibility.md` §3 (Stage 1 measured at **2 of the five corpus families** returning in-window opened text: (c) periodical + (d) digitised corporate print). Cap 22k words/stage; records for load-bearing claims only. **No re-tiering on this pass** — but see the tier note in §V.3: the family count is 2 with a 3rd (a *filings*) family now holding a 1937 registrant document that is post-window, and the probe's Stage-1 tier does not depend on it.
**Held carriers used (all opened by me; every quotation below was read at the printed line):**

| Label (dossier-local) | File under `sources/` | What it prints about itself | Family | Use |
|---|---|---|---|---|
| `FH28` | `periodicals/financialhistory00selt_djvu.txt` (669,597 B) | *A financial history of the American automobile industry*, metadata 1928-01-01 | (c) periodical | primary in-window narrative carrier |
| `AR37` | `periodicals/general-motors-annual-reports_djvu.txt` (197,373 B) | L3-7 "TWENTY-NINTH ANNUAL REPORT OF GENERAL MOTORS CORPORATION / YEAR ENDED DECEMBER 31, 1937"; L20-21 annual meeting "Wilmington, Delaware" | (c) periodical | **registrant self-statement**; dated **1937**, so every Stage-1 fact it carries is `RETRO` |
| `NPSH29` | `corporate_print/NPSH19290609_djvu.txt` (332,625 B) — byte-identical duplicate also at `periodicals/NPSH19290609_djvu.txt`, md5 `cd7e652f831b79f44bb4a84e9d49006e` | L58 "HONG KONG, SUNDAY, JUNE 9, 1929." | newspaper, misfiled as (d) | in-window outward act, 1929 |
| `DW20` | `corporate_print/daytonwrightairp00gene_djvu.txt` (42,441 B; md5 `4c27ab836f…`) | L31 "Copyright. 1920 by The General Motors Corporation, Dayton-Wright Division, Dayton, Ohio." | (d) corporate print | earliest held **naming**; not a founding document |
| `TRUCK31` | `corporate_print/NewProfitsIn…_djvu.txt` (82,206 B; md5 `393fd6094b…`) | L23 "GENERAL MOTORS TRUCK COMR4NY"; content "during 1930" | (d) corporate print | **out of Stage-1 scope** (metadata 1931-01-01; a division, not the registrant) |
| `CF95` | `periodicals/commercialfinanc61newyuoft_djvu.txt` (8,388,633 B, `[TRUNCATED BY --max-mb]` L564712) | L26-35 "HUNT'S MERCHANTS' MAGAZINE … VOLUME LXI … JULY TO DECEMBER, 1895" | (c) periodical | **pre-window, partial, mixed shell** — used only as a negative control (§V.2) |
| `A4` | `research/A4_harvest_mine.md`, mtime **2026-10-07 02:37:54 +0530**, re-read immediately before this line was written | the fleet re-mine's own promotion table | index | pointer only; never evidence (§3) |
| `PROBE` | `research/A_chronology_feasibility.md` | the probe's five-family verdict | index | scope only |

**Cell convention:** *carrier*, *tier*, *class* — "verbatim" [CR-nn]. `RETRO` = retrospective source. `FACT` / `FOUNDER CLAIM` / `CONTEMPORANEOUS OBSERVATION` / `RESTATED` / `RETROSPECTIVE INTERPRETATION` / `INFERENCE` / `ESTIMATE` / `UNKNOWN` per method §3–§7.
**OCR quotation convention (standing, declared so no reader mistakes it for a repair):** every held layer is an OCR text dump. Quotations here are given as **reading text** — line-break hyphenation ("incorpora-ted") and the layers' double spacing are closed up, and no word is changed, added or re-spelled. Where the layer itself is corrupted the defect is shown in place: `COMR4NY`, `ecnt`, `likt`, `^iri^ht`, `W right`, `August I, 1917` (capital I for the numeral 1), `$2000` printed without a comma, and `L14714 "General Motors has formed an"` where the layer drops the corporate name entirely. **Any such rendering is quoted as printed and never silently normalised into a figure or a name.**

**Lineage warning that governs this whole file.** `FH28` prints its own pedigree at L10247-10249: its data were compiled "from the records of the General Motors Corporation for the present writer by, and through the courtesy of, Mr. Frank F. Kolbe, assistant treasurer." `FH28` and `AR37` therefore **both trace to the company's own records** — per method §3 filing-lineage rule they are treated as **one corporate-record lineage**, not two witnesses, wherever they agree. `NPSH29` (an unrelated Hong-Kong paper's column, which itself quotes corporate voice) and `DW20` (a divisional brochure) sit outside that lineage. **Independence for the founding act is therefore not established by any two held documents**; confidence is capped accordingly and stated per claim.

**Hindsight firewall.** Nothing here treats the 1920s combination's survival as proof that the 1908 portfolio policy was rational, that the 1910 bankers were fools, or that scale was foreseeable. The in-window record itself says the opposite was arguable: `FH28` L10229-10231 "In view of the speculative character of the automobile industry in 1910, the terms imposed by the bankers (the voting-trust agreement gave them complete control of the board of directors and its principal committees…"; L10196-10200 "The stringent terms exacted by the banking syndicate… offer abundant testimony of the uncertain, speculative character of the automobile industry, in the opinion of bankers and investors, at this period." Anti-hagiography test applied per section.

**Confidence scale** (method §3): **High** — 2+ independent carriers or a primary document; **Medium** — one reliable carrier, or an approximate date corroborated later; **Low** — conflicting, vague, or retrospective-only; **UNKNOWN** — no evidence recovered. Repeated copies of one origin story are **one** source.

STATUS: WRITTEN

---

## STAGE BOUNDARY — PROPOSED AGAINST CARRIERS

**The operative window for this file is the probe's inherited bracket, 1908-01-01 → 1930-12-31**, because the Stage-1 tier verdict was measured against it. But that bracket is a **harvest search setting, not a boundary** (`A4` L3 says so in terms: the window was applied "deliberately WIDE where the founding date is itself unestablished"). Against held carriers I propose:

| Boundary | Proposal | Carrier that prints it | Confidence |
|---|---|---|---|
| **Stage 1 start** | **1908-09-16**, the date the corpus gives the act that names this registrant | `FH28` L9463-9465 "Durant, on September 16, 1908, effected the incorporation in New Jersey of the General Motors Company, which obtained a perpetual charter containing a very broad grant of powers." Independently printed by the registrant itself, `AR37` L5386-5387 "Note: General Motors Corporation of Delaware was incorporated October 13, 1916, succeeding General Motors Company of New Jersey, organized September 16, 1908." And inside the corporate voice at `FH28` L10666-10667 (board, 1915): "The common stock has never received a cash dividend since the company was organized on September 16, 1908." | High **that all three held carriers print that date**; **Medium** that the date is the act (single lineage, no 1908 carrier held) → §U.01/U.02/U.08 |
| **Pre-window state, not Stage 1** | 1900 and 1904 belong to **Buick**, a bought operating company | `FH28` L9265-9268 "when the prospective failure of the Buick Motor Company threatened to involve important Flint creditors, Durant was called upon, and was willing, to undertake the reorganization of the Company"; L9270-9271 "Durant immediately had the authorized capitalization of the Company increased from $75,000 to $500,000". The 1900 nucleus at L9170 as cited by `PROBE` §1a. | High (that the corpus assigns these to Buick) |
| **Stage 1 end** | **1920-11-30** — the last in-window act that changes who controls the registrant, and the point where the corpus's own combination narrative stops | `FH28` L13196-13198: "The ambitious merger and combination projects that marked the history of the General Motors enterprise up to 1921 have played a relatively small rôle in the Corporation's recent history." And the dated act itself, L12465-12468: "On November 30, 1920, the General Motors Corporation announced the resignation of Durant from the presidency of the Corporation, and the succession of Pierre S. Du Pont." | Medium-High: the boundary is an **interpretation drawn from a carrier's own periodisation**, not a document that declares a stage |
| **Straddle band 1921-01-01 → 1930-12-31** | **Inside Stage 1 by the operative window, outside it by my proposal.** Every such item is tagged `(PB-proposed)` in narrative and register `notes`; none is deleted, because deleting them would silently re-tier the probe's own measurement | The Fisher absorption (1926), the Sheridan liquidation, the 1929 Opel act, the 1930 General Motors Management/Holding organizations | n/a (boundary statement) |
| **Consequence for Stages 2–3** | If the 1920-11-30 end is adopted, Stage 2 opens 1921-01-01 and the `TRUCK31`/1937 layers move accordingly; the probe's Stage-2 (1931-1960) and Stage-3 (1961-1984) windows would need re-cutting. **I do not re-cut them here** — the probe owns the tier, and §V.3 records the disagreement | `PROBE` §3 | n/a |

**What the proposed boundary does NOT claim.** (i) Not that 1908-01-01 → 1908-09-15 is covered: those 8.5 months are pre-registration for the registrant while live print for Buick/Olds (`PROBE` §3). (ii) Not that a document dated 1908 exists anywhere in hand — the naming wall is **1920** (`DW20` L31) and the **date** 1908 reaches us only through 1928 and 1937 print (§U.08). (iii) Not that 1920-11-30 is an operational break: GM continued the combination programme in 1926; it is the break in **who holds control** and in one book's periodisation. (iv) Not that the registrant is the 1916 Delaware person *and* the 1908 New Jersey person *and* the 2009 Delaware person: `AR37` L5386-5387 itself prints two of those as successive persons, and `PROBE` §0.2 records that `sec_intake` resolves "General Motors" to CIK 1467858, whose index floor is **2009-07-16**. (v) Not that Durant founded a company that had not already been founded by Buick's 1900 plant and had not yet been refounded in Delaware — three acts, three persons, one name.

STATUS: WRITTEN

## A. EXECUTIVE STATE SUMMARY (at the proposed close, 1920-11-30; and at the operative close, 1930-12-31)

**At 1920-11-30, on held carriers, the registrant was** a Delaware corporation (incorporated 1916-10-13, `FH28` L9151-9152; the same statement reprinted by the company in `AR37` L5386) that had taken over "direct ownership and operation of the bulk of the physical properties previously controlled by the holding company and its subsidiaries" (`FH28` L9157-9160, locator only), whose president had that day resigned in favour of Pierre S. Du Pont (`FH28` L12465-12468), and whose 1919 investment programme alone had added `$50,558,960` of "investments in unconsolidated companies" and `$47,741,698` expended "directly for real estate, plant, and equipment" (L11782-11784, class `FACT` on a company-furnished series).

**What a 1920 observer could measure.** Not a validated operating business but a **transition under way from holding company to operating company**, with a war-and-postwar capital programme attached. The corpus's own characterisation of the origin is the load-bearing sentence for this section, `FH28` L9145-9148: "The association of the enterprise with Eastern banking houses and financiers soon after its birth, and its status then as a holding company, early gave it a financial rather than industrial character; and in diminished degree this character has persisted to the present day." That is `RESTROSPECTIVE INTERPRETATION` (1928) about 1908-10, and it is also **anti-hagiographic**: it says the industrial character was secondary, which a failure narrative could have exploited.

**Still broken at the close of Stage 1 (all carried, none inferred):**
- Share of the market had already collapsed once and was not yet recovered: `FH28` L10633-10643, "The General Motors enterprises had contributed about 21 per cent of the total physical output and about 22 per cent of the wholesale value in 1910; by 1915, their combined share had fallen to about 7.8 per cent of the physical output and to about 13.3 per cent of the total wholesale value." (DERIVED from that pair: against the industry totals printed at L10630-10632 — 187,000 vehicles in 1910, 969,930 in 1915 — the arithmetic is 0.21 × 187,000 ≈ 39,300 units in 1910 and 0.078 × 969,930 ≈ 75,700 in 1915: **absolute output rose while relative share fell**; class `ESTIMATE`, arithmetic shown.)
- Write-offs the board itself reported: `$12,531,013.19` "required during the past five years to bring your plants, machinery, merchandise, and other assets down to a conservative figure" (`FH28` L10688-10690, quoting the 1915 annual report, footnote L10678 "Annual report of General Motors Company for 1915").
- Eight of the nine car lines bought in the first two years were "untried or unimportant products, all but one of which, the Oakland, were subsequently abandoned" (L9768-9771).
- The 1910 financing cost control: the voting trust "gave them complete control of the board of directors and its principal committees, to which they elected themselves and individuals affiliated with them" (L10230-10233).

**Evidence that existed and survives:** one 1928 industry history with company-supplied data (`FH28`); one registrant annual report on disk, but dated 1937 (`AR37`); one 1920 divisional brochure (`DW20`); one 1929 newspaper column (`NPSH29`). **No 1908-1919 document of any kind is held.** `PROBE` §5.1 states the wall and I adopt it: "The naming wall for GM is therefore 1920 for a document that names, and 1908 for a date asserted — and those are different claims."

**Unknown at the boundary and unresolvable on hand:** the corporation's 1920-12-31 balance sheet; unit output by make for 1919-20; the Fisher contract's full terms; dealer-network size; whether Durant's November 1920 departure was resignation, expulsion or both (§U.05); and any number for the registrant printed **within** the years it describes.

**Unrecoverable because the surviving archive is the winner's** (method §2 record-selection null): the rejected options and internal votes of 1908-10 survive only as the **author's** summaries and as one banker-free interview (A. B. C. Hardy, `FH28` L9817-9832, quoted from the writer's notes, L9847-9848); the "head over heels in debt" acquired companies' own boards left no minutes in this corpus; and no independent count of 1908-10 acquisitions exists other than the table compiled "from the original records in possession of the General Motors Corporation" (L9698).

STATUS: WRITTEN

---

## B. FOUNDER / COMPANY STATE

### B.1 The persons, and which act each is credited with

The brief's premise — that "founded" **splits by person and by act** — is what the carriers actually support. Five distinct acts, five attributions, no merging.

| Person | Act credited **in held print** | Carrier and printed words | Class | Confidence |
|---|---|---|---|---|
| **William C. Durant** | the 1908-09-16 incorporation of the *General Motors Company* (N.J.) | `FH28` L9462-9465, chapter "3. BEGINNINGS OF THE GENERAL MOTORS COMPANY" (heading printed L9438): "Undaunted by the failure of several combination projects which he and Benjamin Briscoe had initiated, Durant, on September 16, 1908, effected the incorporation in New Jersey of the General Motors Company…" | `RESTROSPECTIVE INTERPRETATION` (1928, single lineage) | **Medium** — one lineage; the company's own later note (`AR37` L5387) says the N.J. company was "organized September 16, 1908" and **names no person** (§U.03) |
| **Durant + Benjamin Briscoe** | failed combination projects **before** the act | `FH28` L9462-9463 "the failure of several combination projects which he and Benjamin Briscoe had initiated"; L2768 "Durant then proposed to Briscoe that the Buick and Maxwell…" | `RETROSPECTIVE INTERPRETATION` | Medium; the Briscoe material is at L2695-2811, in the chapter on a **different** enterprise |
| **Durant (as an act of the Company)** | the 1908-10 acquisition programme, and the **consideration** for the Buick leg | `FH28` L9470-9474 "On October 1, 1908, in exchange for 18,870 shares of the common stock of the Buick Motor Company, $500,000 in cash, and an underwriting agreement assuring the sale of $2,000,000 par value of its preferred stock, the General Motors Company issued to Durant $2,387,000 par value of its preferred and $2,193,500 of its common stock" (itemised L9494-9499) | `FACT` on a company-compiled basis | Medium-High that the transaction is printed; **Low** on the counterparty's intent |
| **David Buick / the Buick plant** | the 1900 manufacturing nucleus — a **predecessor**, not the registrant | `PROBE` §1a cites L9170 "David Buick, in 1900, entered the business…"; `NPSH29` L15340 prints the two together in one line: "Buick Motor Company, Flint, Michigan, Division of General Motors Corporation" | `FACT` (of the naming); `INFERENCE` (that this is not founding) | High — method §rule 4: predecessors are not the registrant |
| **The banking syndicate** | the 1910 change of control | `FH28` L10190-10194 names the board it installed: "James N. Wallace, of the Central Trust Company; Frederick Strauss, of J. & W. Seligman & Co.; James J. Storrow, of Lee, Higginson & Co.; William C. Durant, vice-president of the General Motors Company; and Anthony N. Brady, a large stockholder." Note Durant's printed title there: **vice-president**, not founder-president (§U.05) | `CONTEMPORANEOUS OBSERVATION` via 1928 text; the L10259-10274 quotation is a **Boston financial publication of 1910-10-18** | High that the print says this |
| **Pierre S. Du Pont** | the 1920-11-30 succession | `FH28` L12465-12468, and Du Pont's own company's 1920 report quoted at L12470-12480: "Late in November last, William C. Durant, then president of the General Motors Corporation, requested that we take over the management and control of that corporation, advising that he desired to…" | `FACT`, and — for once — **a second corporate lineage** (E. I. Du Pont de Nemours & Company's report, not GM's records) | Medium-High; the du Pont text reaches us only as quoted in `FH28` |

### B.2 Company state, as carried

| Variable | Value | Carrier | Class | Confidence |
|---|---|---|---|---|
| Legal origin of the registrant | "General Motors Company", New Jersey, 1908-09-16, "perpetual charter containing a very broad grant of powers" | `FH28` L9464-9466; `AR37` L5387 ("organized") | `FACT`-on-print, single lineage | Medium → §U.02 |
| Initial then increased capitalisation | "The initial capitalization of $2000 was increased two weeks later to $12,500,000, of which $7,000,000 consisted of seven per cent preferred stock and $5,500,000, of common stock, both classes being of $100 par value." | `FH28` L9467-9470 — **the held bytes print `$2000` with no comma**; do not "repair" it | `FACT`-on-print | Medium; §14.8 forbids rewriting a quotation |
| Status at birth | "its status then as a holding company" | `FH28` L9147 | `RETROSPECTIVE INTERPRETATION` | Medium |
| Dissolution of the N.J. person | 1917-08-01, "its principal constituent companies were likewise dissolved at this time" (OCR prints "August I, 1917") | `FH28` L9155-9157 | `FACT`-on-print | Medium-High |
| The Delaware person | incorporated 1916-10-13; `AR37` L5386 "General Motors Corporation of Delaware"; L20-21 meeting at Wilmington, Del. | both carriers | `FACT` | **Medium-High**: two carriers, but one corporate-record lineage → §U.01 |
| Operating state at 1919-12-31 | 1919 investment programme: +`$50,558,960` investments in unconsolidated companies; `$47,741,698` for real estate/plant/equipment; `$12,439,459` physical assets by consolidation; `$29,888,896` added on reappraisal | `FH28` L11782-11789, footnote L11757-11758 "The details of this expansion may be found in the annual reports of 1919-21, inclusive" | `FACT`-on-print (company-furnished) | Medium; **the underlying annual reports are not held** → FETCH REQUEST |
| Naming form actually used by the registrant | "General Motors Corporation" — 31 occurrences in `AR37`, 1 in `NPSH29` (L15340), and in `DW20` L31 as "The  General  Motors  Corporation"; **"General Motors Company" appears in no held layer as a single-line string**, its one occurrence in `AR37` being split by a line wrap across L5386-5387; **"General Motors of Canada" = 0 in all held layers; "General Motors, Limited" = 0; "General Motors of New York" = 0** | my adjacency counts, this pass | `FACT` (of the counts) | High — see the naming test in §G.2 and §I.3. **Method caveat, stated because it can under-count:** the regexes run **line-wise** over OCR layers, so any phrase broken by a line wrap is invisible to them; the Delaware *Corporation* counts are therefore floors, not censuses, and no null in this row is offered as a census (§14.14 / RD-134 class). |
| Personal position of the founder at the boundary | Durant **out** of the presidency as of 1920-11-30; his personal indebtedness "to forty-four brokerage houses was estimated by Dow, Jones & Co. at $27,000,000" (`FH28` L12456-12458) | `FH28` | `CONTEMPORANEOUS OBSERVATION` (via 1928) | Medium; the $27,000,000 is one broker's estimate, class `ESTIMATE` at source |
| Founder's own words in-window | **None held.** Durant is quoted only *about*, never *as*: the Hardy interview (L9817-9832) and Durant's own November 1920 announcement as reprinted (L12460-12464) | counts + `PROBE` §4 Q3 | `FOUNDER CLAIM` **status: unavailable** | High (that none is held) → FETCH REQUEST for a 1908-20 Durant utterance |

## C. ORIGINAL PROBLEM (as the record states it — the problem the 1908 act was a solution to)

The standard Stage-1 frame — "founder identifies an unserved customer need and builds a product" — **does not fit this company**, and method §7 requires me to adapt rather than delete. What the carriers show is a **portfolio/holding problem stated in financial terms**: how to assemble several competing makes under one capital structure, using stock rather than cash, before any of them is proved.

| Variable | Value | Carrier | Class | Confidence |
|---|---|---|---|---|
| The problem as the corpus states it | Uncertain demand per make while generic demand was large → pool the risk across makes | `FH28` L9810-9814: "the generic demand for automobiles was large, that for any particular 'make' was uncertain; risks could be pooled and minimized by producing a variety of automobile products. Durant's policy was summarized by Mr. A. B. C. Hardy…" | `RETROSPECTIVE INTERPRETATION` of an in-period policy | Medium |
| The policy in the associate's words (transcribed 1924-12-24, Lansing, Mich., from the writer's notes — footnote L9847-9848) | "Durant bought a lot of different companies, most of which were not much good; but he paid for them largely in stock… He wanted to have a lot of 'makes,' so that he would always be sure to have some popular cars… 'I was for getting every kind of car in sight, playing safe all along the line.'" | `FH28` L9817-9832 | `CONTEMPORANEOUS OBSERVATION` (a 1924 interview **about** 1908-10) — **not** a founder claim: it is a third party's memory of Durant | Medium; single witness → §U.10 |
| Why stock was the instrument | 1,000,000 GM common "immediately donated back to the Company for reissue as a fifty per cent bonus with the sale of its preferred stock" | `FH28` L9488-9491 | `FACT`-on-print | Medium |
| What the problem was **not**, in print | Not a manufacturing-scale problem at the moment of the act: the act preceded the plants it controlled | `FH28` L9145-9148 (financial rather than industrial character) | `RETROSPECTIVE INTERPRETATION` | Medium |
| Knowability in-period | Whether "a lot of makes" was a solution or a fraud on investors was **open**: the 1910 bankers priced it as speculation (L10229-10231); the whole US industry was 65,000 cars in 1908 (L9480-9481) | `FH28` | `FACT` | High |

**Not knowable then, knowable now, and therefore firewall-restricted:** that any particular acquired make would survive; that 1915 output would reach 969,930 units (L10631-10632); that Ford's single-model logic would beat a multi-make portfolio. **Nothing in §C imports these.**

STATUS: WRITTEN

---

## D. FIRST EXPERIMENT

The first experiment is **not a product**; on held print it is the **exchange of securities** — the act by which a paper holding company acquired a going concern and then a portfolio.

| Variable | Value | Carrier | Class | Confidence |
|---|---|---|---|---|
| Experiment 1 — the Buick exchange | 1908-10-01: the GM Company issued to Durant `$2,387,000` par preferred + `$2,193,500` common for 18,870 Buick common shares, `$500,000` cash, and an underwriting agreement for `$2,000,000` par preferred; `$1,000,000` of the common donated back | `FH28` L9470-9491; itemisation L9494-9499: "Issued for 18,870 shares of Buick common: $1,887,000 General Motors preferred and $943,500 General Motors common; Issued for $500,000 cash: $500,000 General Motors preferred and $250,000 General Motors common" | `FACT`-on-print, company-compiled | Medium-High on the print; **the itemised preferred lines (1,887,000 + 500,000 = 2,387,000) foot, and the common lines (943,500 + 250,000 + 1,000,000 donated back = 2,193,500) foot only if the donated-back million is counted as issued** — an arithmetic dependency the book never states → §U.10 |
| Experiment 2 — the acquisition programme, tabulated | "TABLE 30. ACQUISITIONS OF GENERAL MOTORS COMPANY, 1908-10" (heading L9586; recaptioned in the list of tables at L881); rows read this pass L9596-9647, columns "Worth / Cash / Preferred / Common" | `FH28` — Buick `$3,417,142 / $1,500 / $2,498,500 / $1,249,250`; Cadillac `2,862,709 / — / 4,400,000 / 275,000`; Olds Motor Works `2,961,769 / 17,279 / 1,827,694 / 1,195,880`; Oakland `305,523 / 305,523`; Marquette `300,000 / 100 / 161,200 / 32,200`; Cartercar `266,486 / 2,780 / 137,700`; Elmore `600,000 / 600,000`; Randolph `207,400 / 204,400`; Rapid Motor Vehicle `647,563 / 412,348 / 51,500`; Weston-Mott `199,302 / 230,000 / 94,000 / 7,000`; Welch `250,000 / 6,000`; **McLaughlin Motor Car Co., Ltd.** "5000 out of 10,030 shares" (value columns blank in the OCR layer) | `FACT`-on-print (footnote L9698: "Compiled from the original records in possession of the General Motors Corporation") | **Medium** — columns are OCR-garbled in places; I record only rows I could read |
| Experiment 2 totals, as printed | `$13,161,813 \| $6,127,668 \| $7,268,804 \| $8,512,830` (L9650), "Stock reacquired (deduct)… 1,654,000 / 581,700" (L9653), "Issued for cash ($4,504,306 realized)" (L9661), "Stock dividend (150 per cent)… 6,249,200" (L9662), "Total stock issues to September, 19[1]0… $10,042,100 \| $15,819,830" (L9665-9668) | `FH28` | `FACT`-on-print; several lines unreconcilable in OCR | Low-Medium → §U.10 (figures that do not close are recorded, not smoothed) |
| Experiment 3 — the Olds purchase as a discrete test | 1908-11-12: entire outstanding capital stock (200,000 shares of $10 par) plus `$1,044,174` of note-liabilities held by S. L. Smith, "for $1,827,694 of General Motors preferred stock, $1,195,880 of common, and $17,279 in cash"; Olds' 1908-08-01 balance sheet printed at L9757-9758 ("unsecured liabilities of $1,472,693, gross tangible assets of $2,763,838, and net tangible assets of $1,291,145"); "Durant purchased the Company chiefly for its reputation, according to Mr. A. B. C. Hardy, later its president" (L9765-9766) | `FH28` L9755-9766; Olds output decline 1905: 2381; 1906: 1372; 1907: 1045; 1908: 1146 | `FACT`-on-print | Medium-High: TABLE 30 row (L9598) and narrative (L9759-9764) **agree to the dollar** — corroboration **inside one lineage only** |
| Result, in the corpus's own words | "The remaining eight lines of automobiles acquired by the General Motors Company during its first two years were untried or unimportant products, all but one of which, the Oakland, were subsequently abandoned." (L9768-9771), each one's prior state listed: Oakland "in active operation for less than a year"; Marquette "organized by Durant only in March, 1909"; Reliance "incorporated only a year earlier"; Cartercar bought because it "boasted a 'friction-drive,' and 'maybe friction-drive would be the thing'"; Elmore for a two-cycle motor; Randolph "had only just been incorporated"; Welch "had produced less than a dozen cars" | `FH28` L9768-9782 | `FACT` (of the statement) + `RETROSPECTIVE INTERPRETATION` (of the causation) | Medium-High |
| A within-experiment reversal the table itself prints | "The $600,000 of preferred stock paid for this Company was repurchased by the General Motors Company some months later for $709,291 cash, when the Elmore stockholders exercised an option to this effect." (L9684-9686) — i.e. the Elmore leg cost **cash above the paper price** | `FH28` | `FACT`-on-print | Medium |
| Patent-line ventures inside the programme | footnote L9693: "The assets of these companies consisted of patent rights later voided; the transaction is discussed in detail below" — attaching to the Heany Lamp / Novelty Incandescent / B. F. Steward rows | `FH28` | `FACT`-on-print | Medium; **which rows the footnote covers is not legible** → §S gap |
| What the experiment did **not** test | No customer-facing test is held: no first-sale figure, no dealer count, no order data for 1908-10 anywhere in the corpus | counts over the held in-window layers, this pass | `UNKNOWN` | High (of the silence) → §S |

STATUS: WRITTEN

---

## E. PRODUCT RECONSTRUCTION (adapted: the Stage-1 "product" is a **make portfolio plus a security**)

| Variable | Value | Carrier | Class | Confidence |
|---|---|---|---|---|
| Makes carried in the first two years | Buick, Cadillac, Oldsmobile (Olds Motor Works), Oakland, Marquette, Reliance, Cartercar, Elmore, Randolph, Welch — plus trucks via Rapid Motor Vehicle, and components/bodies via Weston-Mott, Ewing, Dow Rim, Michigan Motor Castings, Northway, Michigan Auto Parts, Heany Lamp, Novelty Incandescent, the B. F. Steward body plant, McLaughlin (Canada), Champion Ignition, Brown-Lipe-Chapin, Oak Park Power | `FH28` TABLE 30 rows L9596-9647; narrative L9768-9782 | `FACT`-on-print | Medium-High for names. **I do not assert a count**: "nine"/"eight remaining" is the book's own arithmetic (L9768), not mine |
| Bodies as a contracted input | ". T. Stewart Body plant (assets) 160,000 / 160,000 / 0,000" (L9614, OCR rendering); later, the Fisher arrangement makes bodies "supplied by the Fisher company at cost plus 17.6 per cent" (L13225-13227) | `FH28` | `FACT`-on-print | Low (row OCR) / Medium (contract term) → §U.06 |
| The financial product | seven per cent preferred at $100 par (L9468-9470); 1910 first-lien five-year notes with a **20 per cent stock bonus** priced at "96 and interest" (L10264-10269); a 150 per cent stock dividend (L9662) | `FH28` | `FACT`-on-print | Medium |
| Per-make production signal in-window | the Olds decline series (L9755-9756) and Sheridan's single printed year: "The Sheridan division had been organized in 1920 and produced 1796 vehicles in 1921" (L12811-12812) `(PB-proposed)` | `FH28` | `CONTEMPORANEOUS OBSERVATION` via company records | Medium |
| Post-1920 product re-shaping `(PB-proposed)` | Frigidaire "now produced in greater volume than any other similar device" (L13052-13054); "added two new lines of passenger cars, reorganized its truck manufacture, absorbed the Fisher Body Corporation" (L13049-13051); "The original Winton Engine Company has been reorganized as the [Cleveland Diesel Engine Division]" (`AR37` L1531-1534) | `FH28`, `AR37` | `FACT`-on-print / `RESTATED` | Medium / Low (Winton re-org date not printed) |
| Aviation product, **explicitly not GM's origin** | `DW20` L24 prints "THE  BIRTHPLACE  OF  AVIATION" (the double spacing is in the layer), L34 prints "Orville" followed by an OCR-corrupted surname ("^iri^ht"), and L172 prints "In  1908,  we  developed  a  power  machine" — first person plural of the **Wright lineage**, printed under a 1920 copyright held by a GM division (L31 "Copyright.  1920  by  The  General  Motors  Corporation,  Dayton-W  right  Division,  Dayton,  Ohio." — the internal space in "W right" is the layer's) | `DW20` | `FACT` (that the bytes say this) | High — and see §U.08 and `PROBE` §5.2: using it as a GM 1908 date is the exact defect this project pays for |

STATUS: WRITTEN

---

## F. CUSTOMER (adapted: Stage-1 GM had two kinds of "customer", and the record is thicker on the second)

**Customer 1 — the retail purchaser of a make.** Almost nothing in-window. **Customer 2 — the capital-market subscriber**, whose demand the 1908-10 programme actually cleared, and who is documented to the sentence.

| Variable | Value | Carrier | Class | Confidence |
|---|---|---|---|---|
| In-window evidence of end-customer demand | Only two series, both company-adjacent: per-make output where printed (Olds 1905-08, L9755-9756) and the industry totals in §H. **No customer count, no order count, no first customer, no dealer count for 1908-20 is held anywhere in `sources/`.** | `FH28`; my counts over the held layers this pass (`CF95` and the `sources/sec/` set were not re-counted) | `UNKNOWN` (the family) | High (of the silence) → §S, gap G-03 |
| The 1910 subscriber as the immediate customer | "Private subscriptions have been coming in so rapidly to the $15,000,000 First Lien Five-Year General Motors notes that it seems doubtful whether there will be any public issue or any chance for the general public to subscribe. Applications have already been received… for more than a majority of the notes. We understand that these applications are based on 96 and interest for the notes, with a 20 per cent stock bonus. The common stock has been dealt in on the New York Curb at 40 to 45 these last two or three weeks. …" | `FH28` L10263-10270, introduced at L10259-10260: "the disposition of the note-issue. On October 18, 1910, a Boston financial publication declared:" | `CONTEMPORANEOUS OBSERVATION`, **printed within days of the event** — the closest this corpus comes to a live in-window document | High that the carrier dates the quotation 1910-10-18; Medium on substance — **the publication is unnamed** ("Name withheld by request", L10677) → §U.10 |
| Notes fully taken up | "In November, 1910, the bankers announced that all of the notes had been sold in advance of public offering." | `FH28` L10273-10274 | `FACT`-on-print | Medium |
| Dealer/retail financing as a designed channel `(PB-proposed)` | "the organization of the General Motors Acceptance Corporation to aid in financing distributors, dealers, and retail purchasers" | `FH28` L11774-11775, inside the 1919 expenditure list; **GMAC's own organization date is not printed at this line** | `FACT`-on-print of the purpose; `UNKNOWN` of the date | Medium → FETCH REQUEST |
| Dealer network as an object of corporate policy, 1929 `(PB-proposed)` | "The objective of this activity was to promote greater effectiveness of the Corporation's dealer organizations by an organized plan to make investments in approved dealerships, having the purpose of: (a) providing supplemental financial support where justified; and (b) providing financial assistance to individuals of ambition, ability and potentiality, whose restricted financial resources did not permit them to qualify for a General Motors dealership." | `AR37` L1640-1646, on the General Motors Holding Corporation "organized… in the year 1929" (L1638) | `RESTATED` (1937 corporate voice about 1929) | Medium; one corporate lineage |
| Retail advertising voice, 1929 `(PB-proposed)` | "Get behind the wheel and get the facts… then you'll get a Buick!" and the signature line "Buick Motor Company, Flint, Michigan, Division of General Motors Corporation" | `NPSH29` L15339-15340 | `CONTEMPORANEOUS OBSERVATION` (advertisement inside a dated newspaper) | High — and note it prints predecessor make **and** registrant in one line, which is why §B.1 keeps them apart |
| Overseas purchasers `(PB-proposed)` | "The cars and trucks assembled there are sold by 6,000" — the noun the layer needs after "6,000" is not in the layer | `NPSH29` L14758-14759 | `CONTEMPORANEOUS OBSERVATION` in corporate voice | Low (unit of the 6,000) → §U.10 |

STATUS: WRITTEN

---

## G. SUPPLY / HOST SIDE (adapted: for a combination, the supply side is **what was bought, and who fed the bought makes**)

### G.1 Acquired supply as the input base

The TABLE 30 parts list is §D's evidence and is not repeated. The structural point: parts and body supply were bought **with** the makes — Weston-Mott (wheels), the B. F. Steward body plant, Dow Rim, Michigan Motor Castings, Northway, Michigan Auto Parts, Champion Ignition, Brown-Lipe-Chapin (`FH28` L9607-9647). The same logic re-runs at larger scale in 1919: "the acquisition of new or additional interests in nine parts-making enterprises and in the Guardian Refrigerator Company (later, Frigidaire, producer of electric refrigerators), the Dayton Products Company (producer of detonators, pressure indicators, etc.), and the Domestic Engineering Company (producer of Delco-Light power plants)" (L11776-11781). `FACT`-on-print; **Medium**; one lineage.

### G.2 The body constraint, and the Fisher legal sequence (four separate acts, each with its own carrier line)

| Act | Date the record prints | Words | Class | Confidence |
|---|---|---|---|---|
| Fisher Body Corporation **incorporated** | 1916-08-21, New York | `FH28` L13204-13208: "The Fisher Body Corporation had been incorporated in New York on August 21, 1916, to combine into an operating and holding company several body-manufacturing enterprises that had been organized by the same interests in 1908, 1910, and 1912." | `FACT`-on-print | Medium (single lineage) |
| GM takes a **60 per cent stock interest** | 1919 | L11752-11755: "A sixty per cent stock interest was acquired in the Fisher Body Corporation, the largest producer of automobile bodies in the world, General Motors paying therefor approximately $5,800,000 in cash and $21,851,000 in five-year serial notes."; footnote L11760-11764: "The General Motors Corporation purchased 300,000 newly issued shares of no par value of the Fisher Body Corporation, these shares being deposited with four trustees, two representing the former and two the [latter]" | `FACT`-on-print | Medium-High |
| The **supply contract** | 1919, same transaction | L13220-13227: Fisher "increased its capitalization from 200,000 shares to 500,000 shares of common stock, selling the increase to the General Motors Corporation at $92 a share, and, at the same time, entering into an agreement with the latter whereby virtually all of the General Motors body requirements were to be supplied by the Fisher company at cost plus 17.6 per cent" | `FACT`-on-print | Medium |
| The **absorption** | agreement "in the spring of 1926" | L13199-13202 "The only important acquisition of the last half-dozen years has been that of the Fisher Body Corporation, which was absorbed in 1926, but control of which had been acquired in 1919."; L13232-13235 "Such an agreement was made, however, in the spring of 1926. In return for their 39.92 per cent interest in the Fisher Body Corporation, the minority stockholders received 664,720 shares of the common stock of the General [Motors Corporation]" | `FACT`-on-print | Medium-High `(PB-proposed)` |
| **Brief-premise test** | The brief's "1920 Fisher body merger" is **not** what the held print says: control 1919, absorption 1926, Fisher's own incorporation 1916-08-21 in **New York** | — | — | → **§U.06** |

### G.3 Host-side facts that cut against the combination

- The body contract favoured the supplier: "This contract was a very profitable one for the Fisher company; and the volume of its profits probably had much to do with the reluctance displayed by the minority interests, which were closely held, in agreeing to dispose of their holdings to the General Motors Corporation." (L13227-13232) — `RETROSPECTIVE INTERPRETATION`, Medium.
- Captive-plant diversion `(PB-proposed)`: "the Samson plants, as noted before, were diverted to automobile manufacture" (L12797-12798).
- Real estate as infrastructure, then as a financing device `(PB-proposed)`: a $20,000,000 Detroit office building "absorbed more than $4,000,000 during 1919" (L11750-11751); the General Motors Building, Detroit, "constructed at a total cost of $20,786,000", then spun out — "the Corporation organized a subsidiary, the General Motors Building Corporation, which sold to S. W. Strauss & Co. an issue of $12,000,000 of seven per cent serial bonds secured by a first mortgage on the building and by an agreement with the General Motors Corporation whereby the latter leased the building at an annual rental sufficient to provide the interest and retirement requirements of the bond issue" (L12800-12808).
- Employee housing as a supply-side commitment: "More than $20,000,000 in cash and $12,481,100 par value of General Motors' debenture and preferred stocks was expended for a large housing-construction program, initiated for the benefit of the Corporation's employees" (1919; L11770-11773).

STATUS: WRITTEN

---

## H. MARKET, AS KNOWABLE IN-PERIOD

| Variable | Value | Carrier | Class | Confidence |
|---|---|---|---|---|
| Market size at the founding act | "The combined output of the Ford, Buick, Cadillac, and Olds companies in 1908 was 18,411 (figures from records of General Motors Corporation and from The Ford Industries); the total American output was 65,000." | `FH28` L9478-9481 (footnote attached to the founding chapter) | `FACT`-on-print; pedigree **partly GM's own records** | Medium |
| Market growth across Stage 1 | "the aggregate American output rose from 187,000 vehicles valued at $225,000,000 in 1910 to 969,930 vehicles valued at $701,778,000 in 1915" | `FH28` L10630-10632; the chapter's footnote prints the statistical carrier "Facts and Figures of the Automobile Industry, 1927" (L10676) | `FACT`-on-print | Medium — lineage caveat at §U.10 |
| GM's share of that market | 1910 ≈21% of physical output, ≈22% of wholesale value → 1915 ≈7.8% and ≈13.3% | `FH28` L10633-10643 | `FACT`-on-print | Medium |
| Derived unit implication | 0.21 × 187,000 ≈ **39,300 units** (1910); 0.078 × 969,930 ≈ **75,700 units** (1915) — absolute output **up**, relative share **down** | arithmetic shown; inputs from the two rows above | `ESTIMATE` | Medium; both multipliers and both totals come from **one** document |
| Was the market obviously large in-period? | **No, on the print.** The same page that reports the growth reports bankers calling the industry speculative (L10229-10231), and a 150-corporation portfolio rival going into receivership in 1912 (L2908-2914) | `FH28` | `FACT` | High |
| Foreign market as understood at the window's close `(PB-proposed)` | "The Opel Company manufactures the Opel automobile, as well as other Opel products. It ranks among the first ten German industrial organisations and makes about 45 per ecnt. [sic] of the German cars."; "Germany' present position is somewhat likt [sic] that of the United States at the beginning of the development of the industry. A great expansion appears to be certain." | `NPSH29` L14722-14745 (corruptions are the layer's) | `CONTEMPORANEOUS OBSERVATION` of a corporate statement | High that it was printed 1929-06-09; the **assertion itself is the party's estimate**, class `ESTIMATE` at source → §U.10 |
| Post-window market scale, recorded only to show the boundary holds | `AR37` L841 prints a 1937 "United States and Canada" unit total — outside Stage 1 on either proposed window and **not used as Stage-1 evidence** | `AR37` | `FACT` | High |

STATUS: WRITTEN

---

## I. COMPETITION

### I.1 Competitors the record names, one carrier line each

| Competitor | What the held print says | Carrier | Confidence |
|---|---|---|---|
| **Ford Motor Company** | an option on Ford was obtained by Durant "following the latter's reverse in the Selden patent decision of 1909 — an option that Durant failed to exercise only because he could not procure the funds necessary for the initial payment" | `FH28` L9838-9856 | Medium-High (single lineage) → §O |
| **Maxwell-Briscoe** | "The projected acquisition of the Maxwell-Briscoe Company failed for the same reason. A memorandum dated July 19, 1909, provided for the purchase through exchange of securities of the Maxwell-Briscoe Company at a valuation of $3,500,000; and of the Brush Runabout Com-[pany]" | `FH28` L9856-9860 | Medium → §O |
| **United States Motor Company** | the portfolio rival that collapsed: "the large needs of scores of sales and parts-producing companies that it had purchased or organized, forced a receivership in 1912. More than a hundred and fifty distinct corporations possessing diverse and complicated interrelations were found to be controlled by the United States Motor Company. The bulk of these were liquidated; many of the plants, distributed over five states, were sold; and all of the automobile products were discontinued." | `FH28` L2907-2914 | **High** — the most important competitive fact in this section, because it is a Durant-shaped combination that **failed inside Stage 1** |
| **Electric Vehicle Company** | "which had acquired ownership of the Selden patent in 1899, issued more than $20,000,000 of securities by 1902; in 1907, it went into receivership, to be reorganized in 1909 as the Columbia Motor Car Company" | `FH28` L2236-2242 | High |
| **Chevrolet**, as competitor **before** it became the vehicle of reaccession | "incorporated in Michigan on November 6, 1911"; then "On September 23, 1915, Durant organized the Chevrolet Motor Company of Delaware; on October 21, $13,200,000 par value of the authorized capital stock ($20,000,000, all common, of $100 par value) was exchanged for the stocks of the Michigan and New York Chevrolet companies and of several small enterprises; and $6,800,000 par value was offered to the public through an underwriting syndicate headed by Hornblower & Weeks" | `FH28` L10710-10712; L10800-10807 | Medium-High |
| **Willys-Overland** | "John N. Willys performed a feat similar to Durant's, in connection with the Willys-Overland Company" | `FH28` L4381-4383 | Medium (a comparison, not a market datum) |
| **Nash / Jeffery** | Storrow, interviewed 1925-08-27 in the New York offices of Lee, Higginson & Co., transcribed from the writer's notes (L4435-4437): "I picked him to be head of General Motors. In five years, he turned a wreck into a concern having $25,000,000 in the bank. When Durant took control of General Motors away from us, I wired Nash to come here… He picked the Jeffery outfit, which we bought for less than $5,000,000." | `FH28` L4420-4450 | Medium; `CONTEMPORANEOUS OBSERVATION` (1925) about 1910-20. **Storrow is a witness inside the 1910 control board he is describing** (L10192) — not an independent party |
| **Opel** (Germany) `(PB-proposed)` | "General Motors has formed an [the layer drops the name] Company in Russelheim, Germany, a substantial interest in that company being taken at a cost of about $30,000,000."; "The event marks the transition of General Motors into an international manufacturing, as well as distributing, organisation." | `NPSH29` L14714-14720, L14750-14753 | High (printed 1929-06-09); the missing corporate name is an OCR hole, **not** a licence to fill it → §U.10 |

### I.2 The internal competitor

The competitor GM created against itself is on the record: Durant built Chevrolet **while** the bankers held GM, and the book prints the design as hostile — L10737 "Durant's ulterior object in establishing a New York" and L10749 "being turned out. That was Durant's object in this Tarrytown" (both fragments as the layer lines them, with page furniture between). Class `RETROSPECTIVE INTERPRETATION`; confidence **Low-Medium** because the sentence-halves are split and I have not read the full passage body.

### I.3 Naming test applied to competitors and to the registrant (the brief's `gm`-token trap)

`gm` as a bare token is noise and `General` / `Motors` occur in unrelated firms, so **every count in this file is an entity-adjacency count, never a keyword count.** The adjacency test was re-run on this pass **line-wise** over the four layers whose namings bear on it (`AR37`, `NPSH29`, `DW20`, `TRUCK31`) and over `FH28` through the targeted greps recorded in §B-§O; `CF95`'s counts are the probe's, re-measured by me on no line, and are used only as a negative control. The results are printed in §B.2, with the line-wrap caveat attached there. Two negatives earned here, recorded because they *look* like namings:
- `CF95` (Hunt's Merchants' Magazine, July–December **1895**) prints Durant **1** time — "Durant Land Improvement Company" — and Oakland **3** times, all "**Oakland, Cal.**" place-names (`PROBE` §5.7). Pre-window, truncated, mixed shell: **UNANSWERED, not a null**; a live demonstration of the trap.
- `FH28` L6137 "In October, 1908, the charter of the Company was amended, increasing the authorized capital stock from $150,000 to $2,000,000" is **Ford's** chapter, not GM's: the surrounding lines print Ford's stockholders (L6127-6133) and "The Ford Motor Company of Canada, Ltd., was incorporated in the province of Ontario on April 17, 1904" (L6105-6106). `PROBE` §7 left "which company is not yet determined"; **it is now determined** — reading it as GM would have minted a 1908 capital event for the wrong registrant.

STATUS: WRITTEN

---

## J. TECHNOLOGY (what the record shows the combination buying technology *for*)

Nothing in `sources/` documents a GM research activity in Stage 1. What it documents is **technology as a purchase rationale** — and the corpus is candid that the rationale was a guess.

| Variable | Value | Carrier | Class | Confidence |
|---|---|---|---|---|
| The stated selection rule | "the Cartercar had been purchased because it boasted a 'friction-drive,' and 'maybe friction-drive would be the thing'; the Elmore had been acquired for a similar reason — it produced a two-cycle motor, and 'maybe two-cycles was going to be the thing for automobiles'" | `FH28` L9775-9779 | `FACT`-on-print of the stated reason | Medium |
| The same rule in the associate's mouth | "It had the friction drive and no other car had it. How could I tell what these engineers would say next?… That's the kind they were using on motor-boats; maybe two-cycles was going to be the thing for automobiles." | `FH28` L9824-9830 (Hardy, transcribed 1924-12-24) | `CONTEMPORANEOUS OBSERVATION` of a 1908-10 policy | Medium; single witness |
| Patents as purchased assets, and their fate | TABLE 30 footnote: "The assets of these companies consisted of patent rights later voided; the transaction is discussed in detail below" (L9693-9694); the founding-era market was shaped by the Selden patent, whose owner "acquired ownership of the Selden patent in 1899" (L2237-2238) and whose adverse decision gave Durant the Ford option "following the latter's reverse in the Selden patent decision of 1909" (L9840-9843, L9854) | `FH28` | `FACT`-on-print | Medium; **the passage "discussed in detail below" is in a chapter I have not read on this pass** → §S gap G-07 |
| Balance-sheet weight of intangible technology at the 1910 recapitalisation | "Patents, agreements, etc. … 1,959,416.30" against "Real estate, plants and equipment … $14,094,909.55" in the condensed consolidated balance sheet "of the General Motors Company and its subsidiary companies on October 1, 1910, immediately after the new financing" (chapter heading §7 "REGIME OF THE BANKERS' CONTROL", L10277; table opens L10280-10299, also cash in banks "$15,000,473.66", notes and accounts receivable "4,090,028.81", deferred charges "107,302.16", inventories line printed as "39,000,287.90") | `FH28` | `FACT`-on-print | Medium — **the "39,000,287.90" sits where the label reads "Inventories"; whether it is the current-assets subtotal or the inventory line is not decidable from the layer** → §U.10 |
| electrification/components bought in 1919 | "the Dayton Products Company (producer of detonators, pressure indicators, etc.), and the Domestic Engineering Company (producer of Delco-Light power plants)"; "the Guardian Refrigerator Company (later, Frigidaire…)" | `FH28` L11776-11781 | `FACT`-on-print | Medium |
| Technology **not** attributable to GM in-window | aviation: `DW20` is a Wright-lineage brochure under a GM division's copyright (§E, §U.08) | `DW20` | refusal | High |

STATUS: WRITTEN

---

## K. MONEY / PERSONAL FINANCES

### K.1 Company money, as printed

| Date | Item | Value | Carrier | Class | Confidence |
|---|---|---|---|---|---|
| 1908-09-16 | initial capitalisation of the N.J. Company | **"$2000"** (layer prints no comma; not repaired) | `FH28` L9467 | `FACT`-on-print | Medium |
| ~1908-09 (two weeks later) | increased capitalisation | `$12,500,000` — "$7,000,000 … seven per cent preferred" + "$5,500,000, of common stock, both classes being of $100 par value" | `FH28` L9467-9470 | `FACT`-on-print | Medium |
| 1908-10-01 | consideration to Durant | `$2,387,000` par preferred + `$2,193,500` common, for 18,870 Buick shares, `$500,000` cash, and an underwriting agreement for `$2,000,000` par preferred | `FH28` L9470-9474 | `FACT`-on-print | Medium-High |
| 1908-10 → 1910-09 | acquisition consideration, as tabulated | `$13,161,813` net worth; cash `$6,127,668`; preferred `$7,268,804`; common `$8,512,830`; less "Stock reacquired (deduct) 1,654,000 / 581,700"; "Issued for cash ($4,504,306 realized)"; "Stock dividend (150 per cent) 6,249,200"; "Total stock issues to September, 19[1]0 $10,042,100 / $15,819,830" | `FH28` L9650-9668 | `FACT`-on-print | Low-Medium: several lines do not close in OCR → §U.10 |
| 1910-10 | first-lien five-year notes | `$15,000,000`, priced "on 96 and interest… with a 20 per cent stock bonus"; common "dealt in on the New York Curb at 40 to 45" | `FH28` L10264-10270; the board later confirms "the original issue of which was $15,000,000" (L10671-10673) | `FACT`-on-print, quoted from a 1910-10-18 publication | Medium-High |
| 1910-10-01 | post-financing balance sheet | fixed assets `$14,094,909.55`; patents/agreements `$1,959,416.30`; misc. investments `$408,944.07`; cash `$15,000,473.66` | `FH28` L10288-10295 | `FACT`-on-print | Medium |
| 1915 | first cash dividend on common | "a dividend of 50 per cent on the Common Stock, being $50 per share, payable October 15, 1915, to stockholders of record at the close of business, September 10, I9I5" | `FH28` L10693-10696, quoting "Annual report of General Motors Company for 1915" (footnote L10678) | `FACT`-on-print of a 1915 document; the 1915 document itself is **not held** | Medium-High → FETCH REQUEST |
| 1910-15 cumulative | write-offs | "$12,531,013.19, required during the past five years to bring your plants, machinery, merchandise, and other assets down to a conservative figure" | `FH28` L10688-10691 | `FACT`-on-print of the quoted report | Medium-High |
| 1916-05 | United Motors shares offered to the public | "at $62 a share", by the bankers | `FH28` L11325-11326 | `FACT`-on-print | Medium |
| 1918-20 | sources of fixed-capital expansion, TABLE 33 | net earned income 1918-20 "exclusive of extraordinary write-offs" `$193,801,804`; less federal taxes `$47,274,750`; less dividends paid `$57,386,370` → `$89,140,684`; from sale of securities (cash): `[OCR "MUTINY BLOCK"] 98,494,835`; 6% debenture stock `25,425,000`; 7% debenture stock `6,906,800`; employees' bonus "paid in newly issued stock" `13,569,144`; subtotal `134,395,779` | `FH28` L12243-12265 | `FACT`-on-print (company-compiled) | Medium; the "PUBLIC BLOCK" reading is **probable but not printed** → §U.10 |
| 1919 | securities issued for the consolidation legs | "Issued for Chevrolet Motor Co. (Del.) $28,268,400"; "Issued for United Motors Corp. $29,869,200 / 9,956,400"; "Issued for Canadian Chevrolet and McLaughlin Motor Companies 4,900,000"; "General Motors Co. (N.J.) $7,500"; "Acquired through McLaughlin Car-[riage] Co. (Ltd.) 13,300" | `FH28` L11560-11568 | `FACT`-on-print | Medium; row labels are OCR-truncated |
| 1920 | additional capital required | "further capital expenditures of more than $79,000,000 were required to com-[plete]" | `FH28` L11790-11791 | `FACT`-on-print | Low-Medium (sentence cut) |

### K.2 Personal finances of the founder

| Variable | Value | Carrier | Class | Confidence |
|---|---|---|---|---|
| Durant's market position before the fall | his GM common purchases with Du Pont and Kaufman from early 1915; the stock "on January 2, 1915… the closing price… was 82; by December 9g, 1915, it reached a 'high' of 558" | `FH28` L10765-10769, L10787-10789 | `FACT`-on-print (prices from "Ch. summaries of Commercial and Financial Chronicle", footnote L10781) | Medium |
| Durant's personal debt at the exit | "His personal indebtedness to forty-four brokerage houses was estimated by Dow, Jones & Co. at $27,000,000." | `FH28` L12456-12458 | `ESTIMATE` at source (one brokerage's estimate), `FACT`-on-print of the estimate | Medium |
| What he sold, and to whom | "On November 22, 1920, Durant announced that he had sold 'a substantial block of stock of the General Motors Corporation to the Du Pont Securities Corporation of Wilmington, Delaware, which has been formed by Pierre S. Du Pont and his associates, and in the stock of which I will have a large interest.'" | `FH28` L12460-12465 | `FOUNDER CLAIM` (Durant's own announced words, reprinted) | Medium-High that he announced it; **block size UNKNOWN** |
| Du Pont's account of the same act | "Late in November last, William C. Durant, then president of the General Motors Corporation, requested that we take over the management and control of that corporation, advising that he desired to…" — attributed by `FH28` to "the annual report of E. I. Du Pont de Nemours & Company for 1920" (L12470-12472, L12478-12480) | `FH28` | `FACT`-on-print; **a second corporate lineage** (du Pont's report, not GM's records) — the only genuine cross-lineage pair in this dossier | Medium-High |
| Durant's earlier personal stake | GM common "holdings of William C. Durant, then president of the… Durant as president of the Corporation… Durant's holdings, approximately 2,250,000 shares" | `FH28` L9012-9016 (fragmentary as lined) | `FACT`-on-print | Low-Medium (sentence split by page furniture) |
| Any 1908-10 personal financing document of Durant's | **NOT HELD** | counts, this pass | `UNKNOWN` | High (of the silence) → FETCH REQUEST |

STATUS: WRITTEN

---

## L. VALIDATION SIGNALS (in-period, and each labelled for what it did *not* demonstrate)

| Date | Signal | Magnitude | What it demonstrated | What it did NOT demonstrate | Carrier | Confidence |
|---|---|---|---|---|---|---|
| 1910-11 | All 1910 notes placed | "all of the notes had been sold in advance of public offering" | that a speculative industry could still absorb $15,000,000 of first-lien paper at 96 with a stock bonus | **nothing about product demand**; and the price paid for it was board control (§M, §N) | `FH28` L10273-10274 | Medium |
| 1915-10-15 | **First cash dividend on the common** | 50% / $50 per share | that the common had **never** been paid: the board's own words "The common stock has never received a cash dividend since the company was organized on September 16, 1908" — a *first*, printed by the issuer | that the dividend was repeatable: one payment is one payment; **`PROBE` §4 Q5 correctly refuses to certify "repeatable validation" here** | `FH28` L10666-10667, L10693-10696 | Medium-High |
| 1915-10-01 | Voting trust expired; control changed hands without a fight | "Durant and his associates controlled enough stock to elect nearly a clear majority of the board of directors; and the chairmanship of the board went to Pierre S. Du Pont" | that the equity route back to control worked | that the operating company was sound; the write-offs of the same five years say otherwise | `FH28` L10789-10793 | Medium |
| 1916-05 | Open distribution of United Motors shares | "$62 a share" | that the market would take a Durant-sponsored holding security at a price | product acceptance; and the buyer of that issue is not named here | `FH28` L11325-11326 | Medium |
| 1919 | Scale of the post-war programme | 1919 investments/asset movements in §K.1 (TABLE 33 series) | that capital could be deployed at ~$100M/yr scale | that deployment was efficient — the 1920 crisis follows in the same chapter sequence (L12052 "12. THE POST-WAR CRISIS") | `FH28` L12243-12265 | Medium |
| 1925-27 `(PB-proposed)` | Profits outrunning volume | "In 1925, with output and dollar-sales exceeding those of 1923 (the best previous year) by approximately 5 per cent, net profits rose by more than 73 per cent; and in 1926, when output and sales recorded a further increase of 47 and 44 per cent, respectively, over those of 1925, net profits again displayed a disproportionate gain, rising by more than 65 per cent"; "In 1927, when the aggregate American motor-vehicle output suffered a decline of 20 per cent, General Motors scored further substantial gains" | that the operating company had become volume-elastic | nothing about Stage-1 causes; and the same page prints the Fisher absorption as the acquisition of the period | `FH28` L13060-13069 | Medium (percentages printed; underlying table is OCR-garbled: net sales `$45,330,888 / 106,484,756 / 176,085,144 / 238,319,009` at L13079-13082 against output units `587,341 / 835,902 / 1,234,850 / 1,562,748` at L13092-13096 — **the pairing of columns to years is not decidable in the layer**) → §U.10 |

STATUS: WRITTEN

---

## M. NEGATIVE SIGNALS / FAILURES INCURRED (only what a carrier prints; the brief's premises tested first)

**Premise test — "the 1910 receivership": REFUTED ON HELD BYTES.** The word `receiver(ship)` occurs **5** times in `FH28` and **none** attaches to General Motors: L2239 Electric Vehicle Company "in 1907, it went into receivership"; L2908-2912 **United States Motor Company** "forced a receivership in 1912… controlled by the United States Motor Company"; L4329-4331 "The present Chrysler Corporation, now highly successful, is the only important producing enterprise that is the product of a receivership"; L7451-7453 and L5623 "On February 4, 1922, at a receiver's sale, it paid $8,000,000 for the plants and other assets of the Lincoln Motor Company" (Ford's chapter). What 1910 actually did to GM is worse in one respect and better in another: **it cost the founders control** — the voting-trust agreement "gave them complete control of the board of directors and its principal committees" (L10230-10233) — not a court. GM's own receivership history, if any, is **UNKNOWN on held bytes** and is a FETCH REQUEST, not a claim. → §U.04

| Date | Failure / negative signal | Magnitude as printed | Carrier | Class | Confidence |
|---|---|---|---|---|---|
| 1908-10 | Abandonment of nearly the whole acquired portfolio | "untried or unimportant products, all but one of which, the Oakland, were subsequently abandoned" | `FH28` L9768-9771 | `FACT`-on-print | Medium-High |
| 1909-10 | Cash lost unwinding one leg | Elmore preferred repurchased "for $709,291 cash" | `FH28` L9684-9686 | `FACT`-on-print | Medium |
| 1908-10 | Patent-line assets voided | "The assets of these companies consisted of patent rights later voided" | `FH28` L9693 | `FACT`-on-print | Medium |
| 1910-11 | Two intended acquisitions failed for want of money | the Ford option "failed to exercise only because he could not procure the funds"; the Maxwell-Briscoe project "failed for the same reason" | `FH28` L9854-9857 | `FACT`-on-print | Medium → §O |
| 1910-15 | Relative collapse under the bankers' cost-cutting | share 21% → 7.8% of physical output (1910 → 1915) | `FH28` L10633-10643 | `FACT`-on-print | Medium |
| 1910-15 | Write-offs | `$12,531,013.19` "required during the past five years" | `FH28` L10688-10691 | `FACT`-on-print | Medium-High |
| 1910-15, as told by GM's own operating vice-presidents | "The bankers were too skeptical about the future of the automobile industry. They were chiefly interested in trying to realize savings, so they closed down some plants, concentrating in others. They didn't take advantage of the opportunities. Under Durant, the Company might have had a little financial difficulty now and then, but it would have grown much faster and its earnings would have been much greater." | `FH28` L10644-10657 — introduced as "operating vice-presidents of the General Motors Corporation, speaking informally in an interview with the present writer" | `CONTEMPORANEOUS OBSERVATION` (1920s interview) that is **also** a partisan re-reading of 1910-15 | Medium that it was said; **Low as history** — the speakers are defending their own prior employer's strategy; recorded and not adopted |
| 1921-22 `(PB-proposed)` | Two divisions killed outright | "the Sheridan and Scripps-Booth enterprises were liquidated and discontinued"; Sheridan "had been organized in 1920 and produced 1796 vehicles in 1921"; Scripps-Booth "had produced 8128 cars in 1919; 8848 in 1920" | `FH28` L12796-12797, L12811-12815 | `FACT`-on-print | Medium — **a failed line launched and killed inside the wider 1908-30 window**, i.e. the Stage-1 pattern repeating |
| 1920 `(PB-proposed)` | The post-war crisis itself | a named chapter, "12. THE POST-WAR CRISIS" (L12052), and the 1920-11-30 presidency change (L12465-12468); **the chapter body was not read on this pass** | `FH28` | `UNKNOWN` (the magnitude, on this pass) | High (of the gap) → gap G-05, FETCH-adjacent internal read |
| 1925 | Out-bid, not bought | GM "made… a bid of $124,650,000 cash for Dodge Brothers, Inc."; the corpus separately prints "The sale of the assets of Dodge Brothers, Inc., to a group of investment bankers in April, 1925, for a net cash price of $146,000,000… the feat of Dillon, Read & Co., the principal purchasers" | `FH28` L13048 and L14356-14360 | `INFERENCE` (that the bid failed) — arithmetic basis: the printed sale price exceeds GM's printed bid and the printed purchaser is a different party; **no line says "GM was outbid"** | Medium |

STATUS: WRITTEN

---

## N. FOUNDER DECISIONS (each with state-before, alternatives and the carrier that prints it)

| Date | Decision | State before | Alternatives on the record | Constraint | Rationale as printed | Carrier | Confidence |
|---|---|---|---|---|---|---|---|
| 1908-09-16 | Incorporate a **holding** company in New Jersey rather than merge the plants into one operating company | Buick rescued and growing; failed Briscoe combination projects | (a) continue as Buick alone; (b) the failed broader combinations with Briscoe | "a very broad grant of powers" was obtainable | combination after failure of separate projects | `FH28` L9462-9466, L9147 | Medium |
| 1908-10-01 | Pay for Buick **in stock**, and donate a million common back as a selling bonus | paper with no cash | cash purchase; leave Buick independent | $500,000 cash only | to fund preferred sales | `FH28` L9470-9491 | Medium |
| 1908-11-12 | Buy Olds for reputation, not output | Olds declining (2381→1045→1146) | leave it | its president held $1,044,174 of notes | "chiefly for its reputation" | `FH28` L9755-9766 | Medium |
| 1909 | Attempt Ford, attempt Maxwell-Briscoe | growing portfolio | decline | "could not procure the funds necessary for the initial payment" | control of the largest producer | `FH28` L9838-9860 | Medium |
| 1910 | Accept the bankers' terms | post-panic funding need | default / slower scale | "the speculative character of the automobile industry in 1910" | "The stringent terms exacted by the banking syndicate… offer abundant testimony of the uncertain, speculative character of the automobile industry, in the opinion of bankers and investors" | `FH28` L10196-10200, L10229-10234 | Medium |
| 1911-11-06 | While boxed out of GM, build Chevrolet (Michigan) | vice-presidency under a bankers' board | wait for the trust to expire | his energies redirected | "he had transferred his energies, shortly after the accession of the bankers, to the organization of a new automobile enterprise" | `FH28` L10703-10712 | Medium |
| 1915-09-23 / 1915-10-21 | Reorganise Chevrolet into Delaware and take public money | Michigan + New York Chevrolets + small firms | stay private | needed to fund "increasing the output from 100 to 300 cars a day" | "In order to place his tenuous, but effective, control of General Motors on a surer basis" | `FH28` L10795-10814 | Medium |
| 1920-11-22 / 11-30 | Sell the block and resign the presidency to Du Pont | brokers' margin pressure; 44 brokerage houses | default on the margin position | "could not maintain his position" | Durant's own announcement vs du Pont's report of a request — **two accounts, one act** | `FH28` L12455-12480 | Medium; motive conflict → §U.05 |

STATUS: WRITTEN

---

## O. COUNTERFACTUAL OPPORTUNITIES (each is carried by a printed line; none is graded by later outcome)

| Road not taken | The printed evidence | Class | Confidence |
|---|---|---|---|
| **Ford Motor Company inside GM, 1909-10** | "the General Motors Company… made a serious attempt to acquire the Ford Motor Company and the Maxwell-Briscoe Motor Company. Mention has been made of the option obtained by Durant from the Ford Motor Company following the latter's reverse in the Selden patent decision of 1909 — an option that Durant failed to exercise only because he could not procure the funds necessary for the initial payment." | `FACT`-on-print (that an option existed and lapsed) | Medium-High |
| **Maxwell-Briscoe + Brush, by memorandum** | "A memorandum dated July 19, 1909, provided for the purchase through exchange of securities of the Maxwell-Briscoe Company at a valuation of $3,500,000; and of the Brush Runabout Com-[pany]" | `FACT`-on-print | Medium |
| **Dodge Brothers, 1925** | the $124,650,000 cash bid; the assets sold in April 1925 for a net cash price of $146,000,000 to a bankers' group | `FACT` + `INFERENCE` (§M) | Medium |
| **Keeping the acquired lines alive** | the book's own counterfactual is printed at L9768-9771 (all but Oakland abandoned); the *alternative* — the United States Motor route — is printed as a **failure**, not a promise | `FACT` | Medium |
| **"Fiat of Canada"** — a premise in my brief | **REFUTED as held:** `Fiat` occurs **0** times in `FH28`; the Canadian entity that actually appears in GM's own securities-issued-for table is **"McLaughlin Motor Car Co., Ltd."** (TABLE 30, L9635-9637) and "Issued for Canadian Chevrolet and McLaughlin Motor Companies 4,900,000" (L11566-11568); "General Motors of Canada" occurs **0** times in every held layer | refusal → §U.07 | High (of the count) |
| **"Anderson" as a GM acquisition** | **REFUTED:** every `Anderson` hit in `FH28` that could mean a person belongs to **Ford's** story — "J. W. Anderson" among Ford's thirteen original stockholders (L6132), "John W. Anderson" in the Ford founding finance passages (L5783, L7050, index L16654). No GM acquisition named Anderson is printed. | refusal → §U.07 | High |
| **"Sheridan"** | **SUPPORTED but not as an acquisition:** Sheridan is a GM **division** "organized in 1920" which "produced 1796 vehicles in 1921" and was "liquidated and discontinued" (L12793-12815) `(PB-proposed)` | `FACT`-on-print | Medium |
| **"the London branch"** | **NO CARRIER.** `London` hits in `FH28` are bibliographic imprints (L16229, L16264, L16359, L16389, L16417, L16460, L16552, L16603) plus one unrelated line, "the Explosives Trades, Ltd. (of London, England)" (L11995). A GM London entity is **UNTRIED** in this corpus, not absent from the record | UNKNOWN | High (of the count) → FETCH REQUEST |

**Coda (method §7 interpretive-coda duty).** The counterfactual set says something checkable: in 1909-10 GM's binding constraint was **cash, not ambition** — the two largest prizes lapsed for want of an initial payment, and the funding that was available in 1910 arrived only with board control attached. Mechanism: a holding company paying in its own paper could buy small makers whose owners accepted paper, but not Ford or Maxwell, whose owners wanted cash. Alternative explanation the record permits: the options lapsed because valuations, not funds, failed — `FH28` L9854-9856 names funds, so this alternative is **excluded on print**. Confidence: **Medium**, resting on one company-compiled document.

STATUS: WRITTEN

---

## P. QUANTITATIVE METRICS TABLE (every value read off a held line this pass; `UNKNOWN` is used where the layer is corrupt)

| ID | Date | Metric | Value | Unit | Source | Source date | Confidence |
|---|---|---|---|---|---|---|---|
| P1 | 1908-09-16 | Initial capitalisation, General Motors Company (N.J.) | $2000 | USD par, as printed | `FH28` L9467 | 1928 (metadata) | Medium |
| P2 | 1908-09 (two weeks after P1) | Authorised capitalisation after increase | $12,500,000 | USD | `FH28` L9467-9468 | 1928 | Medium |
| P3 | 1908-09 | …of which seven per cent preferred | $7,000,000 | USD, $100 par | `FH28` L9468-9469 | 1928 | Medium |
| P4 | 1908-09 | …of which common | $5,500,000 | USD, $100 par | `FH28` L9469-9470 | 1928 | Medium |
| P5 | 1908-10-01 | Buick common shares taken in exchange | 18,870 | shares | `FH28` L9471 | 1928 | Medium-High |
| P6 | 1908-10-01 | Cash in the founding consideration | $500,000 | USD | `FH28` L9472 | 1928 | Medium-High |
| P7 | 1908-10-01 | GM preferred par issued to Durant | $2,387,000 | USD par | `FH28` L9488 | 1928 | Medium |
| P8 | 1908-10-01 | GM common par issued to Durant | $2,193,500 | USD par | `FH28` L9488-9489 | 1928 | Medium |
| P9 | 1908 | Combined output, Ford + Buick + Cadillac + Olds | 18,411 | units | `FH28` L9478-9479 | 1928 | Medium |
| P10 | 1908 | Total American automobile output | 65,000 | units | `FH28` L9481 | 1928 | Medium |
| P11 | 1908-08-01 | Olds Motor Works: unsecured liabilities / gross tangible / net tangible | $1,472,693 / $2,763,838 / $1,291,145 | USD | `FH28` L9757-9758 | 1928 | Medium |
| P12 | 1908-11-12 | Olds purchase consideration | $1,827,694 pref + $1,195,880 common + $17,279 cash; plus $1,044,174 of note-liabilities | USD | `FH28` L9759-9764 | 1928 | Medium-High |
| P13 | 1908-10 | TABLE 30 totals, 1908-10 acquisitions | $13,161,813 net worth; cash $6,127,668; preferred $7,268,804; common $8,512,830 | USD | `FH28` L9650 | 1928 | Low-Medium (columns OCR-garbled) |
| P14 | to 1910-09 | "Total stock issues to September, 1910" | $10,042,100 preferred; $15,819,830 common | USD | `FH28` L9665-9668 | 1928 | Low |
| P15 | 1910-10-01 | Condensed consolidated balance sheet, immediately after the new financing | fixed assets $14,094,909.55; patents/agreements $1,959,416.30; misc. investments $408,944.07; cash $15,000,473.66; notes+receivables $4,090,028.81; deferred $107,302.16; "39,000,287.90" at the inventories label | USD | `FH28` L10288-10299 | 1928 | Medium; label ambiguity → U.10 |
| P16 | 1910-10 | First-lien five-year note issue | $15,000,000 | USD | `FH28` L10264, restated L10672 | 1928 quoting 1910-10-18 print | Medium-High |
| P17 | 1910 | American output / value | 187,000 vehicles; $225,000,000 | units; USD | `FH28` L10631-10632 | 1928 | Medium |
| P18 | 1910 | GM enterprises' share | about 21% physical output; about 22% wholesale value | per cent | `FH28` L10633-10635 | 1928 | Medium |
| P19 | 1915 | American output / value | 969,930 vehicles; $701,778,000 | units; USD | `FH28` L10632 | 1928 | Medium |
| P20 | 1915 | GM enterprises' share | about 7.8% physical; about 13.3% wholesale value | per cent | `FH28` L10637-10643 | 1928 | Medium |
| P21 | 1910→1915 | **Derived** implied GM units | 0.21 × 187,000 ≈ 39,300 → 0.078 × 969,930 ≈ 75,700 | units | DERIVED from P17-P20 | — | Medium; arithmetic shown in §A |
| P22 | 1910-15 | Cumulative write-offs reported by the board | $12,531,013.19 | USD | `FH28` L10688-10689 | 1928 quoting the 1915 annual report | Medium-High |
| P23 | 1915-10-15 | First cash dividend on the common | 50 per cent = $50 per share; record 1915-09-10 | USD/share | `FH28` L10693-10696 | 1928 quoting the 1915 report | Medium-High |
| P24 | 1911-01-02 → 1915-12-09 | GM common closing/price range | 82 (1915-01-02 close) → 558 ("high", 1915-12-09); 1911-1915 lows 25–37.37, highs 40–99.3 | exchange price | `FH28` L10763-10765, L10787-10789 | 1928 (prices footnoted to C&FC chapter summaries) | Medium |
| P25 | 1916-05 | United Motors public offering price | $62 | USD/share | `FH28` L11325-11326 | 1928 | Medium |
| P26 | 1918-20 | Net earned income, exclusive of extraordinary write-offs | $193,801,804 | USD | `FH28` L12248-12252 (TABLE 33) | 1928 | Medium |
| P27 | 1918-20 | Less federal taxes / less dividends paid | $47,274,750 / $57,386,370 → $89,140,684 retained | USD | `FH28` L12253-12254 | 1928 | Medium |
| P28 | 1918-20 | Cash from sale of securities (three lines) | 98,494,835 + 25,425,000 + 6,906,800 | USD | `FH28` L12256-12258 | 1928 | Medium; first line's label is OCR-corrupted |
| P29 | 1919 | Investments in unconsolidated companies, increase | $50,558,960 | USD | `FH28` L11782-11784 | 1928 | Medium |
| P30 | 1919 | Direct real estate / plant / equipment expenditure | $47,741,698 | USD | `FH28` L11784-11785 | 1928 | Medium |
| P31 | 1919 | Fisher 60 per cent interest price | ≈$5,800,000 cash + $21,851,000 five-year serial notes; 300,000 newly issued no-par shares | USD | `FH28` L11752-11764 | 1928 | Medium-High |
| P32 | 1919 | Securities issued for the consolidation legs | Chevrolet (Del.) $28,268,400; United Motors Corp. $29,869,200 and $9,956,400; Canadian Chevrolet and McLaughlin Motor Companies $4,900,000; General Motors Co. (N.J.) $7,500; via McLaughlin Carriage Co. (Ltd.) $13,300 | USD | `FH28` L11560-11568 | 1928 | Low-Medium (row labels truncated in the layer) |
| P33 | 1920 | Further capital expenditure required | more than $79,000,000 | USD | `FH28` L11790-11791 | 1928 | Low-Medium |
| P34 | 1920-11 | Durant's personal indebtedness | $27,000,000 estimated by Dow, Jones & Co., to forty-four brokerage houses | USD | `FH28` L12456-12458 | 1928 | Medium; itself an `ESTIMATE` at source |
| P35 | 1921 | Sheridan division output | 1796 | vehicles | `FH28` L12811-12812 | 1928 | Medium `(PB-proposed)` |
| P36 | 1925 | Dodge Brothers bid / actual sale | GM bid $124,650,000 cash; assets sold April 1925 for net cash $146,000,000 to a bankers' group (Dillon, Read & Co. principal); their resale profit $13,250,000 gross | USD | `FH28` L13048, L14356-14362 | 1928 | Medium `(PB-proposed)` |
| P37 | 1925-26 | Output / sales / profit growth as printed | +5% output and dollar sales vs 1923 with net profits +73% (1925); +47% output / +44% sales with net profits +65% (1926); 1927 industry output −20% with GM "further substantial gains" | per cent | `FH28` L13060-13069 | 1928 | Medium `(PB-proposed)` |
| P38 | 1927 (four years ended) | TABLE columns as read | net sales $45,330,888 / 106,484,756 / 176,085,144 / 238,319,009; a second column 587,341 / 835,902 / 1,234,850 / 1,562,748 | USD / units | `FH28` L13079-13096 | 1928 | **Low — year-to-column pairing not decidable in the layer**; registered as a gap, not asserted → §S G-06 |
| P39 | 1929 | Opel interest cost | about $30,000,000 | USD | `NPSH29` L14720 | 1929-06-09 | Medium `(PB-proposed)` |
| P40 | 1929 | Export-side investment | more than $65,000,000 across "24 operations overseas"; cars and trucks "sold by 6,000" | USD; count; count-unit UNKNOWN | `NPSH29` L14755-14759 | 1929-06-09 | Medium (investment); Low (6,000 unit) `(PB-proposed)` |
| P41 | 1929 | Opel share of German car output | "about 45 per ecnt. [sic]" | per cent | `NPSH29` L14727-14728 | 1929-06-09 | Low — party estimate reprinted by a newspaper `(PB-proposed)` |
| P42 | 1930-04 | General Motors Management Corporation, organised | sold 1,375,000 GM common shares at $40 = $55,000,000; GM's average cost ≈$33/share; profit realised $9,482,861; consideration $5,000,000 cash + $50,000,000 seven-year 6% serial bonds | USD | `AR37` L3961-3971 | 1937-12-31 FY (report), `RETRO` | Medium `(PB-proposed)` |
| P43 | 1937-12-31 | Reserve against that plan's assets | reserve $1,871,776; net amount remaining $3,541,195 | USD | `AR37` L3946-3947 | 1937 | Medium `(PB-proposed)` |
| P44 | **1908-09-16 → 1920-11-30 (in-window totals that are NOT held)** | revenue, unit sales, headcount, dealer count, dividend history other than P23, plant count, capacity | **UNKNOWN — no in-window operating total for the registrant exists in any held layer** | — | my counts, this pass; `PROBE` §4 | — | High (of the absence) |

**Table discipline note (method §8).** Every row above has a source cell and a confidence cell; no derived value is labelled as observed (P21 is the only DERIVED row and its arithmetic is shown in the cell). P38 and P15 are printed as `Low`/ambiguous **rather than repaired**.

STATUS: WRITTEN

---

## Q. CHRONOLOGICAL MICRO-TIMELINE (Stage 1; one line per event, each carried)

| Date | Event | Actors | Location | Carrier | Class | Conf. |
|---|---|---|---|---|---|---|
| 1904 | Buick Motor Company reorganisation after near-failure; authorised capitalisation raised from $75,000 to $500,000 | Durant; Flint creditors | Flint, Mich. | `FH28` L9265-9271 | `FACT`-on-print (predecessor) | Medium |
| 1908-09-16 | **General Motors Company incorporated in New Jersey** — the act that names this registrant; perpetual charter, broad powers; initial capitalisation $2000 | "Durant, on September 16, 1908, effected the incorporation…" | N.J. | `FH28` L9463-9467; `AR37` L5387 ("organized") | `FACT`-on-print, one lineage | **Medium** → U.01/U.02/U.08 |
| 1908-09 (late) | Capitalisation increased to $12,500,000 | the new Company | — | `FH28` L9467-9470 | `FACT` | Medium |
| 1908-10-01 | Buick taken into the Company for 18,870 shares + $500,000 cash + underwriting agreement | Durant / GM Company | — | `FH28` L9470-9499 | `FACT` | Medium-High |
| 1908-10 (Oct) | Cadillac and other early legs; TABLE 30 programme opens | GM Company | — | `FH28` L9596-9647 | `FACT` | Medium |
| 1908-11-12 | Olds Motor Works acquired | GM Company; S. L. Smith | Lansing, Mich. | `FH28` L9759-9764 | `FACT` | Medium-High |
| 1909-03 | Marquette "organized by Durant only in March, 1909" | Durant | Flint area (as printed) | `FH28` L9773 | `FACT` | Medium |
| 1909-07-19 | Maxwell-Briscoe purchase memorandum, $3,500,000 valuation | Durant; Briscoe interests | — | `FH28` L9858-9860 | `FACT` | Medium |
| 1909 | Ford option obtained after the Selden decision; **never exercised** (funds) | Durant; Ford | — | `FH28` L9840-9856 | `FACT` | Medium-High |
| 1910-10-01 | Condensed consolidated balance sheet taken "immediately after the new financing" | GM Company and subsidiaries | — | `FH28` L10280-10299 | `FACT` | Medium |
| 1910-10-18 | Boston financial publication reports the $15,000,000 first-lien note subscription running ahead | bankers' syndicate | Boston / New York Curb | `FH28` L10259-10270 | `CONTEMPORANEOUS OBSERVATION` | Medium-High |
| 1910-11 | "all of the notes had been sold in advance of public offering" | the bankers | — | `FH28` L10273-10274 | `FACT`-on-print | Medium |
| 1910 | Voting-trust agreement gives the bankers complete board control; named board: Wallace, Strauss, Storrow, Durant (vice-president), Brady | banking syndicate | New York / Boston | `FH28` L10190-10194, L10230-10233 | `FACT`-on-print | Medium-High. **Not** a receivership → U.04 |
| 1911-11-06 | Chevrolet Motor Company **incorporated in Michigan** | Durant and associates | Michigan | `FH28` L10710-10712 | `FACT` | Medium-High |
| 1912 | United States Motor Company forced into receivership (competitor; 150+ corporations liquidated) | U.S. Motor Co. | five states | `FH28` L2907-2914 | `FACT` | High |
| 1915-01 → 1915-12 | GM common 82 → high 558; Durant buys with Du Pont and Kaufman | Durant, Pierre S. Du Pont, Louis G. Kaufman | New York | `FH28` L10765-10789 | `FACT`-on-print | Medium |
| 1915-09-10 / 1915-10-15 | First cash dividend ever on the common: 50% / $50 per share | board of the GM Company | — | `FH28` L10661-10696 | `FACT` (board's own words) | Medium-High |
| 1915-10-01 | Voting trust expires; Durant's group elects "nearly a clear majority"; Du Pont takes the chair | Durant; Du Pont | — | `FH28` L10789-10793 | `FACT` | Medium |
| 1915 (post-trust) | Durant succeeds **Charles W. Nash** as president of the General Motors Company; Storrow, Emory W. Clark and Albert Strauss resign from the board | Durant; Nash; Storrow | — | `FH28` L10976-10982 | `FACT`-on-print | Medium-High |
| 1915-09-23 | **Chevrolet Motor Company of Delaware** organised; 1915-10-21 $13,200,000 par exchanged for the Michigan/New York companies, $6,800,000 offered via Hornblower & Weeks | Durant | Delaware | `FH28` L10800-10807 | `FACT` | Medium-High |
| 1916-08-21 | Fisher Body Corporation incorporated in New York | the Fisher interests | New York | `FH28` L13204-13205 | `FACT` | Medium |
| 1916-10-13 | **General Motors Corporation incorporated in Delaware** | (act not attributed to a person in the print) | Delaware | `FH28` L9151-9152; `AR37` L5386 | `FACT`-on-print | **Medium-High** → U.01 |
| 1917-08-01 | The New Jersey Company dissolved; principal constituent companies likewise dissolved; the Corporation takes over direct ownership | GM Corporation | — | `FH28` L9155-9160 | `FACT`-on-print | Medium |
| 1918 | General Motors Bonus Plan established | Corporation | — | `AR37` L3351 | `RESTATED` (1937 voice) | Medium |
| 1919 | 60% Fisher interest + cost-plus-17.6% contract; GMAC organised; Guardian/Dayton Products/Domestic Engineering interests; $50.5M/47.7M investment totals | Corporation | Detroit / Flint / Dayton | `FH28` L11750-11790, L13220-13227 | `FACT`-on-print | Medium |
| 1920-11-22 | Durant announces sale of "a substantial block" to Du Pont Securities Corporation of Wilmington, Del. | Durant; Pierre S. Du Pont | Wilmington, Del. | `FH28` L12460-12465 | `FOUNDER CLAIM` | Medium-High |
| **1920-11-30** | **Proposed Stage-1 end**: GM Corporation announces Durant's resignation from the presidency and Du Pont's succession | Corporation board | — | `FH28` L12465-12468; du Pont's own 1920 report quoted L12478-12480 | `FACT`-on-print, two corporate lineages | **Medium-High** → U.05 |
| 1921 | Sheridan division produces 1796 vehicles; Sheridan and Scripps-Booth "liquidated and discontinued" | Corporation | — | `FH28` L12793-12815 | `FACT` `(PB-proposed)` | Medium |
| 1922-02-04 | (Ford, not GM) buys Lincoln Motor Company plants at a receiver's sale for $8,000,000 | Ford Motor Company | Lincoln, Mich. | `FH28` L7451-7453 | `FACT` | High — recorded as a **negative control** on the receivership search |
| 1925-04 | Dodge Brothers assets sold to a bankers' group for $146,000,000 after GM's $124,650,000 bid | Corporation; Dillon, Read & Co. | — | `FH28` L13048, L14356-14358 | `FACT` + `INFERENCE` `(PB-proposed)` | Medium |
| 1926 (spring) | Fisher minority (39.92%) exchanged for 664,720 GM common shares; Fisher "absorbed in 1926" | Corporation; Fisher minority | — | `FH28` L13199-13202, L13232-13235 | `FACT` `(PB-proposed)` | Medium-High → U.06 |
| 1929 | "General Motors has formed an [name lost] Company in Russelheim, Germany", ≈$30,000,000; export investment >$65,000,000 across 24 overseas operations | General Motors (corporate voice) | Rüsselsheim, Germany | `NPSH29` L14714-14759 | `CONTEMPORANEOUS OBSERVATION` `(PB-proposed)` | Medium |
| 1929 | "In the year 1929 there was organized the General Motors Holding Corporation, now a Division" | Corporation | — | `AR37` L1638-1639 | `RESTATED` `(PB-proposed)` | Medium |
| 1930-04 | General Motors Management Corporation organised; 1,375,000 shares at $40 | Corporation | — | `AR37` L3961-3971 | `RESTATED` `(PB-proposed)` | Medium |
| 1937-12-31 | The registrant's own note printing the 1916/1908 succession | GM Corporation | Wilmington, Del. | `AR37` L5386-5387 | `RETRO` carrier for in-window facts | Medium-High |

STATUS: WRITTEN

---

## R. END-OF-STAGE STRUCTURED SNAPSHOT

### R.1 At the proposed boundary, 1920-11-30

| Variable | State | Carrier | Confidence |
|---|---|---|---|
| Legal person | General Motors **Corporation**, Delaware, incorporated 1916-10-13; the New Jersey Company of 1908-09-16 dissolved 1917-08-01 with its principal constituents | `FH28` L9151-9160; `AR37` L5386-5387 | Medium-High |
| Structure | Converted from **holding** company to **direct owner and operator** of "the bulk of the physical properties" | `FH28` L9157-9160 | Medium |
| Control | Du Pont succession printed at the moment of change; Durant out of the presidency | `FH28` L12465-12468 | Medium-High |
| Lines carried after the shake-out | Buick, Cadillac, Oldsmobile, Oakland survived from the 1908-10 programme; the other acquired makes abandoned | `FH28` L9768-9771 | Medium-High |
| Financial signature of the stage | a 1910 $15,000,000 first-lien issue bought with board control; a first common dividend in 1915; $12,531,013.19 of write-offs; a 1918-20 expansion financed as in TABLE 33 | `FH28` L10264, L10693-10696, L10688, L12243-12265 | Medium |
| What had **not** been demonstrated | repeatability of the dividend; survival of the make portfolio under direct operation; independence of the 1920 crisis; any customer-level metric | absence verified this pass | High (of the absence) |

### R.2 At the operative window's close, 1930-12-31 (all `(PB-proposed)` items collected)

| Variable | State | Carrier | Confidence |
|---|---|---|---|
| Product set | Fisher absorbed (1926); two new passenger lines; truck manufacture reorganised; Frigidaire "now produced in greater volume than any other similar device" | `FH28` L13048-13054 | Medium |
| Failures after 1920 | Sheridan and Scripps-Booth liquidated; Samson plants diverted | `FH28` L12793-12798 | Medium |
| Foreign manufacturing | Opel association at ≈$30,000,000; "the transition of General Motors into an international manufacturing, as well as distributing, organisation"; >$65,000,000 in 24 overseas operations | `NPSH29` L14714-14759 | Medium |
| New corporate vehicles | General Motors Holding Corporation (1929); General Motors Management Corporation (1930-04, $55,000,000 share sale) | `AR37` L1638-1646, L3961-3971 | Medium, `RETRO` |
| Registrant naming at the close | "General Motors Corporation" of Delaware; **no** held layer names a "General Motors of Canada", "General Motors, Limited", or a "General Motors of New York" as a line-wise string (floor, not census: §B.2 caveat) | my adjacency counts, §B.2, §I.3 | High (of the counts) |

STATUS: WRITTEN

---

## S. DATA GAPS (each classified TRIED–ANSWERED / TRIED–UNANSWERED / UNTRIED; High-importance gaps carry a follow-up)

| ID | Gap | Classification | Why missing | Importance | Best available evidence | Follow-up task |
|---|---|---|---|---|---|---|
| G-01 | Any document **printed 1908-1919** that names the registrant | **TRIED–UNANSWERED** — the mine reached seven in-window Google Books items and resolved **no text layer** for any (HTTP 503 after 3 tries each) | the archive answered with no text, not with an empty result | **High** — this is the only class of document that could certify the founding act | `PROBE` §2(c); `A4` rows 1-7 all `UNANSWERED` | Orchestrator run: `ia_text.py mine --q 'yndIAQAAMAAJ'` (C&FC 1909), `cHgpAAAAYAAJ` (Magazine of Wall Street 1917), `IyZKAQAAMAAJ` (Financial World 1920), `I1SmQH86zxIC` (General Motors World 1928), `GrdvdLXgLNgC` (Time 1928), `61sgJTm2wF8C` (Annual Report 1929), `ou0bAAAAIAAJ` (NYT Index 1926), each with `--max-mb` ≥ 20 |
| G-02 | A 1908-09-16 **charter, certificate of incorporation or related court filing** | **UNTRIED** — family (e), auction/museum documentary, has never been reached for gm | no tool in `tools/` and no run | **High** | none | `ia_text.py search --q '(title:(durant) OR creator:(durant)) AND text:(automobile) AND mediatype:(texts)' --rows 40`; plus an orchestrator fetch against Detroit Institute of Arts / Sloan Museum GM archives and stock-certificate sale records |
| G-03 | Any customer-side Stage-1 number (first sale, dealer count, unit sales 1908-20) | **TRIED–ANSWERED as absent** on held bytes: searched the in-window text layers this pass (6 files under `sources/periodicals/` and `sources/corporate_print/`; the 40 `sources/sec/` documents are out of window by their own index floor and were not re-searched) | pre-1994 operating statistics of this registrant are not in the families we hold | Medium | `FH28` per-make fragments (P11, P35) | raise `Facts and Figures of the Automobile Industry` years 1911-1920 as a text layer if one exists |
| G-04 | GM's own annual reports **inside** Stage 1 (1910-1920) | **TRIED–UNANSWERED** — the only held annual-report layer is the 1937 one; a targeted "annual report of" search returned 0 items, but the tool's own sidecar warns the `text:` field matches **annotations**, not layers | mis-specified field, not an empty archive | **High** — a 1915 report would upgrade P22/P23 from quoted-to-original | `AR37`; `PROBE` §2(d) | enumerate the **whole** `general-motors-annual-reports` item (it is a multi-file item; only `gm1937_djvu.txt` was fetched) — see U.09 |
| G-05 | The **body** of the post-war-crisis chapter (1920-21) | **TRIED–UNANSWERED by this pass** — heading read (`FH28` L12052), the resignation passage read (L12455-12480), the crisis body not read | internal read not completed inside the tool budget; **no network needed** | **High** | §K.2/§M/§N lines already cited | internal read: `FH28` L12052-12460 in full |
| G-06 | Year-to-column pairing of the 1924-27 TABLE (L13079-13096) | **TRIED–ANSWERED as illegible** — the OCR layer drops the year gutter | OCR | Medium | P38 | page-image read |
| G-07 | Which TABLE 30 rows the "patent rights later voided" footnote (L9693) covers | **TRIED–UNANSWERED** — footnote markers garbled in the layer | OCR | Medium | the footnote text itself | read the superscript sequence against the page image |
| G-08 | EDGAR-family evidence for the **historic** registrant | **TRIED–UNANSWERED** — `sec_intake.py auto 140139 --dry-run` → HTTP 404 `NoSuchKey`; and the resolved-registrant run left **319 in-window filings NOT-ENUMERATED** at our own `--max-docs 40` | our cap and our path guesses, not the archive's silence | Medium (Stage 1), **High** (Stage 3) | `PROBE` §2(a) | `sec_intake.py index 140139`; re-run at `--max-docs 400` |
| G-09 | A **General Motors of Canada / Ontario** legal person, and any **London** branch | **UNTRIED** — adjacency counts on held bytes are 0, and the queries that would reach Canadian or UK company print were never written (`PROBE` §6: all 8 gm query blocks use only "General Motors" / "General Motors Corporation") | missing query block, owned by the log owner, not by me | **High** — this is the most-cited genealogical error class for this company | `FH28` L9635-9637 (McLaughlin Motor Car Co., Ltd.), L11566-11568 ("Canadian Chevrolet and McLaughlin Motor Companies") | write the predecessor-vocabulary query block, re-mine, and add a Canadian/UK registry family |
| G-10 | Whether "General Motors Company" also named a **registered trade name** of the 1908 person | **UNTRIED** — corporate-registry (NJ/DE) print is not among the five families held | no tool | Medium | none | orchestrator: NJ Division of Records and Delaware registry routes |
| G-11 | The **1910 voting-trust** instrument and its named trustees | **TRIED–UNANSWERED** — the agreement is described (`FH28` L10230-10233) and its board named (L10190-10194), but no instrument text is held | secondary print only | Medium-High | those two passages | reach the 1910 note indenture via G-01's C&FC volumes |
| G-12 | Independence of `FH28` and `AR37` | **TRIED–ANSWERED**: both trace to the company's own records (`FH28` L10247-10249; `AR37` is the registrant's own report) — **one corporate-record lineage** for founding-era figures | established, not missing | **High** (caps confidence across this file) | `FH28` L10247-10249 | keep applying the cap in Stage 2/3; do not re-score |
| G-13 | A `CORRECTIONS.md` for this company | **UNTRIED** by this pass and **not mine to write** — the gate reported "no CORRECTIONS.md — gate DID NOT RUN (not a pass)" | the file belongs to the QC/merge owner | Medium | gate output `03_quality_control/gm_s1_gates_p1.md` | its owner should seed it from U.04, U.05, U.06, U.07, U.09 — five inherited premises this pass refuted or re-dated |

STATUS: WRITTEN

---

## T. SOURCE / PROVENANCE TABLE

| Source | Type | Primary/Secondary | Event date | Publication date | URL | Tier | Confidence |
|---|---|---|---|---|---|---|---|
| `FH28` *A financial history of the American automobile industry* | bound periodical/book text layer, company-assisted | secondary carrying primary quoted matter (1910 Boston print, the 1915 annual report, du Pont's 1920 report, Storrow 1925, Hardy 1924) | 1904-1927 | metadata 1928-01-01 | per its sidecar in `sources/periodicals/` | **T1 as printed 1928; T2 as testimony about 1908-10** | Medium; **one lineage** (G-12) |
| `AR37` *Twenty-ninth Annual Report of General Motors Corporation, year ended December 31, 1937* | registrant's own annual report, OCR layer | **primary** for what the company said in 1937-38; `RETRO` for every Stage-1 date it states | 1908/1916/1918/1929/1930 as stated | 1938 (meeting "Tuesday, April 26, 1938", L20-21) | `https://archive.org/download/general-motors-annual-reports/gm1937_djvu.txt` (sidecar) | **T1** | Medium-High on printed dates; **post-1930, never in-window evidence** (U.09) |
| `NPSH29` newspaper layer, masthead "HONG KONG, SUNDAY, JUNE 9, 1929." | newspaper, dated **inside** the layer; misfiled under `corporate_print/`, md5-identical twin at `periodicals/` | primary for the printed column, which reproduces corporate voice | 1929 | 1929-06-09 (L58) | sidecar | **T2** | High on date/naming; Medium on substance |
| `DW20` Dayton-Wright divisional brochure, copyright 1920 | digitised corporate print | **primary as a 1920 naming only** | 1920 | 1920-01-01 metadata + printed copyright line | sidecar | **T1 (artifact) / T4 (as founding evidence)** | High that it names; **nil** as origin evidence (U.08) |
| `TRUCK31` *New Profits in Delivering Building Materials* (General Motors **Truck** Company) | digitised corporate print | not used | — | 1931-01-01 | sidecar | T1 (artifact) | **out of scope**: post-window and a division, not the registrant |
| `CF95` *Hunt's Merchants' Magazine* vol. LXI, July–December 1895 | bound periodical, truncated at L564712 | negative control only | — | 1895 | sidecar | T2 | **UNANSWERED**; pre-window, partial, mixed shell |
| `A4_harvest_mine.md` (mtime **2026-10-07 02:37:54 +0530**) | harvester index/verdict sheet | **pointer only — never evidence** | — | 2026-10-07 | repo path | n/a | used solely for the promotion table and the `title:1918` mis-stamp (U.09) |
| `research/A_chronology_feasibility.md` | probe dossier | scope carrier (tier + five-family verdict) | — | 2026-09-30 | repo path | n/a | authoritative for scope per the brief |
| EDGAR CIK 1467858 submissions index (40 documents fetched, 96,229,567 B; 2138 index rows) | regulatory filings | **excluded**: earliest filingDate 2009-07-16 | 2009+ | — | `sources/sec/`, `sources/_index/submissions_CIK0001467858.csv` | T1 | High (that it is out of window) |

STATUS: WRITTEN

---

## U. CONFLICTING EVIDENCE

Format per method §7 (CLAIM A / CLAIM B / WHY THEY DIFFER / EVIDENCE WEIGHT / BEST-SUPPORTED INTERPRETATION / RESIDUAL UNCERTAINTY / CONFIDENCE). Each `U.nn` here has exactly one row in the conflicts register; no conflict is registered without its anchor.

### U.01 Which legal person "General Motors was founded in 1908" names
**CLAIM A** `FH28` L9151-9152: "The present General Motors Corporation was incorporated under the laws of Delaware on October 13, 1916." **CLAIM B** same document L9463-9465 plus `AR37` L5386-5387: a *General Motors Company* of New Jersey, 1908-09-16, which the Delaware person **succeeded**; **and** `PROBE` §0.2: `sec_intake` resolves "General Motors" to CIK 1467858, a **fourth** person — post-2009 Delaware *General Motors Company*, index floor 2009-07-16. **WHY THEY DIFFER** — one name, four registrations, none dissolved into the next by operation of law. **EVIDENCE WEIGHT** — the two held carriers agree; the fourth is proven by a machine-resolved identity. **BEST-SUPPORTED INTERPRETATION** — the 1908 date is real and belongs to the New Jersey *Company*; it is **not** the founding of the 1916 *Corporation*, and neither is the 2009 registrant. **RESIDUAL UNCERTAINTY** — whether the 1916 securities exchange was a continuation or a fresh promotion; `FH28` L9152-9154 describes a purchase ("By exchange of securities it acquired all of the capital stock"), which is not re-registration. **CONFIDENCE: Medium-High.**

### U.02 What kind of act 1908-09-16 was: *organized* vs *incorporated*
**CLAIM A** `AR37` L5387: "General Motors Company of New Jersey, **organized** September 16, 1908." **CLAIM B** `FH28` L9463-9465: "Durant, on September 16, 1908, **effected the incorporation** in New Jersey of the General Motors Company". **WHY THEY DIFFER** — a corporate note compresses promotion steps into "organized"; a historian separates filing from organisation. **EVIDENCE WEIGHT** — compatible in substance; they differ only in what the date denotes. **BEST-SUPPORTED INTERPRETATION** — write the date as the incorporation date with the registrant's own word recorded beside it; do not claim to know which paperwork event the day names. **RESIDUAL UNCERTAINTY** — whether the charter filing and effective organisation were the same day. **CONFIDENCE: Medium.** This is why `PROBE` §4 Q1 caps at Medium.

### U.03 Who is credited as founder, and by which document
**CLAIM A** `FH28` credits **Durant alone** with the act (L9463), **David Buick** with the 1900 nucleus, the **bankers** with the 1910 refounding (L10190-10234), and **Briscoe** with the failed predecessor projects (L9462-9463). **CLAIM B** `AR37` L5386-5387 names **no person** at either date; `NPSH29` names no person and speaks as "our" (L14755); `DW20` names no person in its copyright. **WHY THEY DIFFER** — a narrative history attributes agency; a corporate note, an advertisement and a brochure do not. **EVIDENCE WEIGHT** — the only person-bearing account held is one retrospective book. **BEST-SUPPORTED INTERPRETATION** — "a 1908 holding-company creation by **Durant** and others over a bought operating company (**Buick**)" is supportable as to Durant and Buick; "and others" is supportable only as **separate acts on separate dates** (Briscoe before 1908-09-16; the syndicate in 1910-10; S. L. Smith as Olds' president on 1908-11-12). No held document names co-founders **at the act**. **RESIDUAL UNCERTAINTY** — whether any 1908-era document credits anyone at all. **CONFIDENCE: Medium (Durant); UNKNOWN (co-founders at the act).**

### U.04 "The 1910 receivership" (inherited premise) vs what the bytes print
**CLAIM A** the premise that GM entered receivership in 1910. **CLAIM B** `FH28`: all five `receiver(ship)` occurrences attach to **other** firms — Electric Vehicle Company 1907 (L2239); United States Motor Company 1912 (L2908-2912); "The present Chrysler Corporation, now highly successful, is the only important producing enterprise that is the product of a receivership" (L4329-4331); Lincoln Motor Company "at a receiver's sale on February 4, 1922" for $8,000,000 (L7451-7453, L5623) — and for GM in 1910 the carrier prints a **$15,000,000 first-lien note issue with a 20 per cent stock bonus** (L10264-10269) and a **voting-trust agreement that gave the bankers complete control of the board** (L10230-10233). **WHY THEY DIFFER** — grepping `receiver` near `1910` in one book mints a fact from a neighbour's failure. **EVIDENCE WEIGHT** — decisive against the premise on held bytes. **BEST-SUPPORTED INTERPRETATION** — 1910 was a **change of control by contract, not a court receivership**; GM's own receivership history, if any, is UNKNOWN. **RESIDUAL UNCERTAINTY** — an unmentioned New Jersey equity proceeding remains possible. **CONFIDENCE: High (of the refutation on held bytes).** **Recommended for CORRECTIONS.md.**

### U.05 Durant's exit: date, direction, and who forced it
**CLAIM A** the inherited premise "the 1916 expulsion of Durant". **CLAIM B** `FH28` prints three movements and no 1916 one: 1910-11 loss of control with the printed title "**vice-president** of the General Motors Company" (L10193); 1915 **restoration** — "William C. Durant, president of the Chevrolet Motor Company, succeeded Charles W. Nash as president of the General Motors Company" (L10976-10979); **1920-11-30 resignation** — "the resignation of Durant from the presidency of the Corporation, and the succession of Pierre S. Du Pont" (L12466-12468). A second split runs across the speakers: Durant's 1920-11-22 announcement frames it as a **sale he made** (L12460-12465); du Pont's 1920 report frames it as Durant "**requested that we take over the management and control of that corporation**" (L12478-12480); Storrow frames 1915 as "When Durant took control of General Motors away from us" (L4445). **WHY THEY DIFFER** — three speakers with three interests, plus one premise with no carrier. **EVIDENCE WEIGHT** — held print supports 1910 (control) and 1920 (presidency), not 1916. **BEST-SUPPORTED INTERPRETATION** — record **two** exits: a contractual displacement in 1910-11 and a financed resignation on 1920-11-30; label 1916 **unattested here**. **RESIDUAL UNCERTAINTY** — whether "resignation" covered an ouster; L12455-12456 "tain his position" (i.e. *could not maintain his position*) implies pressure but the clause head is on the facing page. **CONFIDENCE: Medium-High (dates); Low (character of the act).** **Premise correction recommended.**

### U.06 The Fisher "merger": 1920 vs 1919 vs 1926 vs 1916
**CLAIM A** the inherited premise "the 1920 Fisher body merger". **CLAIM B** `FH28` prints four separate legal events: Fisher Body Corporation **incorporated in New York 1916-08-21** (L13204-13205); GM's **60 per cent interest** in 1919 for ≈$5,800,000 cash + $21,851,000 five-year serial notes, 300,000 newly issued no-par shares held by four trustees (L11752-11764); the **supply contract** at cost plus 17.6 per cent, 1919 (L13220-13227); the **absorption** in 1926, agreement "in the spring of 1926", 39.92 per cent minority for 664,720 GM common shares (L13199-13202, L13232-13235). **WHY THEY DIFFER** — "the Fisher merger" is used loosely for control, contract and absorption. **EVIDENCE WEIGHT** — complete against 1920. **BEST-SUPPORTED INTERPRETATION** — four register rows, four carrier lines; **no 1920 Fisher act is printed**. **RESIDUAL UNCERTAINTY** — the exact 1926 closing date (only "spring") and the fiscal alignment of the 1919/1920 figures. **CONFIDENCE: Medium-High.** **Premise correction recommended.**

### U.07 The 1926-28 acquisition premise set, tested one by one
**CLAIM A** "Fiat of Canada", "Anderson", "Sheridan", "the London branch" as GM acts of 1926-28. **CLAIM B** held bytes: `Fiat` occurs **0** times in `FH28` (my count this pass), and the Canadian entity that does appear in GM's own securities-issued-for table is **McLaughlin Motor Car Co., Ltd.** (L9635-9637) and "Issued for Canadian Chevrolet and McLaughlin Motor Companies 4,900,000" (L11566-11568); every **Anderson** hit is Ford's original stockholder John W. Anderson (L6132, L5783, L7050, index L16654); **Sheridan** is a GM **division organised 1920, producing 1796 vehicles in 1921, then "liquidated and discontinued"** (L12793-12815) — not a 1926-28 acquisition; **London** hits are bibliographic imprints plus "the Explosives Trades, Ltd. (of London, England)" (L11995), which is not a GM branch. **WHY THEY DIFFER** — the premises are memory of other firms' GM stories; the corpus's GM-adjacent foreign/Canadian print sits in **1908-10, 1919-20 and 1929**. **EVIDENCE WEIGHT** — three of four unsupported; the fourth supported but mis-typed. **BEST-SUPPORTED INTERPRETATION** — record the four tests as **refuted / refuted / supported-with-correction / UNTRIED**, and open G-09 for the Canadian and London lines instead of calling them absent. **RESIDUAL UNCERTAINTY** — real GM Canadian and UK incorporations are very likely documented in families never queried. **CONFIDENCE: High (of the counts); UNKNOWN (of the underlying legal history).**

### U.08 The naming wall (1920 attested vs 1908 asserted) and the `DW20` false friend
**CLAIM A** "founded 1908" as a **documented** fact. **CLAIM B** the earliest held layer naming the registrant is `DW20` L31 (1920); the 1908 date is carried only by `FH28` (1928) and `AR37` (1937), both retrospective and both in the **same** corporate-record lineage (G-12). Compounding trap: `DW20` L172 "In 1908, we developed a power machine" is **Orville Wright's first person** inside a GM divisional brochure (L24 "THE BIRTHPLACE OF AVIATION"; L34 "Orville" plus a corrupted surname). **WHY THEY DIFFER** — a date asserted and a naming attested are different claim types, and a GM-copyrighted document can carry a non-GM "we". **EVIDENCE WEIGHT** — unambiguous. **BEST-SUPPORTED INTERPRETATION** — founding act at **Medium**, lineage-capped; naming wall at **1920**; no 1908-10 first-person GM voice exists and none may be implied. **RESIDUAL UNCERTAINTY** — a 1908-10 printed naming could still be found (G-01). **CONFIDENCE: High (of the wall).**

### U.09 A carrier dated from metadata instead of from the layer: `AR37` stamped "1918"
**CLAIM A** `A4` (mtime 2026-10-07 02:37:54 +0530) promotion row: "`general-motors-annual-reports` | `? / title:1918` | in-window | 197,373 | … | `general motors` | **TIER1_CANDIDATE_TEXT**". **CLAIM B** the layer's own opening lines print "TWENTY-NINTH ANNUAL REPORT OF GENERAL MOTORS CORPORATION / YEAR ENDED DECEMBER 31, 1937" (L3-7) and its sidecar URL is `.../gm1937_djvu.txt`. **WHY THEY DIFFER** — an Internet Archive *title* metadatum is not the document's date, and the fetched file is one member of a multi-file item. **EVIDENCE WEIGHT** — the printed page wins (RD-121 class: a date printed in the layer beats an inherited scan/title year). **BEST-SUPPORTED INTERPRETATION** — `AR37` is a **1937/1938** document: Tier-1 for the Stage-1 facts it states but `RETRO`, and **not** an in-window carrier; the `A4` row's "in-window" verdict is wrong for this file. **RESIDUAL UNCERTAINTY** — whether the same item contains genuine 1918-1920 reports (that is exactly G-04). **CONFIDENCE: High (of the printed date).** **Flag for the harvester owner: print the fetched file name in the `dates` column for multi-file items.**

### U.10 Unreconciled counts, and arithmetic the layers do not close
**CLAIM A / CLAIM B (seven residuals, kept together only because each is a count).** (i) gm harvest rows: `candidates.csv` **72**, the mine reported **66**, an earlier A4 run **45**, tonight's `A4` header "**111 candidate rows** in the harvest index; 12 items mined; 97 left untried" — four numbers from four commands, canonical status UNKNOWN. (ii) `FH28` L9488 vs L9494-9499: the totals foot only if the donated-back $1,000,000 counts as issued. (iii) L9650/L9668 columns that do not close against L9596-9647 in OCR. (iv) L10298-10299: "Inventories… 39,000,287.90" printed where a current-assets subtotal belongs. (v) the 1924-27 table pairing (G-06). (vi) `NPSH29` L14714 "General Motors has formed an [ ] Company in Russelheim, Germany" — the corporate name is **absent from the layer**. (vii) the 1910 Boston publication is unnamed ("Name withheld by request", `FH28` L10677 area). **WHY THEY DIFFER** — OCR loss, index growth between runs, deliberate anonymisation. **EVIDENCE WEIGHT** — each limits precision, none threatens existence. **BEST-SUPPORTED INTERPRETATION** — record every figure **as printed**, never as repaired; where a foot fails, say so in the row. **RESIDUAL UNCERTAINTY** — all seven. **CONFIDENCE: High (of the residuals).**

STATUS: WRITTEN

---

---

**Companion deliverable.** The claim-record appendix **GM1-C01 … GM1-C33** (33 records; 2,801 words as emitted at `_parts/s1_p1.md` l.570–l.608, 2,921 in its own file including the one-paragraph merge preamble) is at `stage_1_claim_records.md` in this directory — split at the §U / claim-record section boundary per method §9.1(3) and §9.3, ids unchanged, nothing renumbered, no record rewritten or dropped. It is the same document read after §U, not a second account of it.

---

## REGISTERS (applied — the nine registers live as CSVs at this directory root)

Applied 2026-10-07 by `merge-gm` from the nine fenced append blocks at `_parts/s1_p1.md` l.616–l.781:
`quantitative.csv` **26** · `timeline.csv` **30** · `sources.csv` **8** · `conflicts.csv` **10** ·
`data_gaps.csv` **13** · `decisions.csv` **8** · `validation.csv` **6** · `failures.csv` **8** ·
`channels.csv` **5** = **114 rows**, each re-measured on disk at its header width with the id map above applied
(12 / 11 / 18 / 15 / 8 / 15 / 11 / 11 / 11 columns respectively). The requested↔applied table, the duplicate and
cross-block checks and the validation/failures adjudication are in the **MERGE RECORD** section at the head of
this volume; live word and row counts are regenerated in `_MANIFEST.md`. The verbatim blocks stay in the
read-only part, which remains the emission of record.

Carried from the part's own emission note (l.614), unchanged in substance: `stage` is `stage1` in every row;
the `(PB-proposed)` marker appears only in `notes` and in prose, never in a controlled column; `archived_url`
reads `NONE_HELD (no wayback capture exists under sources/)` in all eight source rows because family (b) is
**UNTRIED, not empty**; and the five-family verdicts are the probe's — restated at §S and §T and in
`_MANIFEST.md`, never re-run by this merge.
STATUS: WRITTEN

---

## END OF PART s1_p1

Sections written on this pass: Header, Stage boundary, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, claim records, registers (9 blocks). Sections pending: none for this part; Stage-1 parts 2+ are not planned by this agent — the merge agent decides whether a second volume is needed. Nothing in this file is registered without a held line behind it; nothing held was smoothed.
