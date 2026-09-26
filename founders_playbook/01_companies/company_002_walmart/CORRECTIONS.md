# CORRECTIONS.md — company_002_walmart, Stage 1

Provenance correction register for this company. Standing rule (method §14 rule 8, rule 10): a withdrawal
**supersedes** the text it withdraws, it never erases it. The withdrawn wording stays visible where it was
written — in `_parts/`, in the part's own dated-record row, in a register cell — and the correction names the
carrier that replaces it. Reverting one of these is a defect.

The `corrections` gate checks propagation mechanically: every id below must reach **both** the register layer
and a stage volume. An entry that reaches the prose but no register is the failure this file exists to stop.

| Id | Withdrawn text | Where it lived (carrier of the stale claim) | Replaced by | Reaches |
|---|---|---|---|---|
| **COR-301** | "a **Delaware corporation**; incorporated **1969-10-01**" | merged `stage_1.md` identity line; `_parts/s1_p1.md` header; `stage_1.md` §D record **D-R03** | state **UNKNOWN**, day **UNKNOWN**, **1969 year-only and company-asserted** | `conflicts.csv` **U.014**; `stage_1.md` header + assembly note + §B.0 + §D-R03c |
| **COR-302** | "the operating entity from **1962** was **Wal-Mart, Inc., an Arkansas corporation**" | merged `stage_1.md` identity line only (second clause) | **no legal person is named for 1945–1962** anywhere on disk; the entity-forming fact is the **1970-02-01 pooling** out of **Walton Enterprises, Inc.** | `conflicts.csv` **U.013**; `stage_1.md` header + assembly note + §B.0 |
| **COR-303** | the merge's non-destruction arithmetic — "**99 rows requested … 95 applied; 4 refused … Nothing dropped**" (`_MANIFEST.md` §Proof of non-destruction), which is the record the RD-115 "0 findings" certification read | `_MANIFEST.md` proof table; `03_quality_control/walmart_s1_merge.md`; `MASTER_RESEARCH_LOG` RD-115 | the requested count was **121**, not 99: `research/A6_held_corpus_mine.md` §Records for merge (22 rows, 4 fenced `csv` blocks under a `>>> REGISTER ROWS FOR MERGE <<<` mark) was never censused. **22 requested = 16 minted + 6 folded with printed reasons + 0 dropped** | `sources.csv` **S0145, S0148–S0155**; `quantitative.csv` FY1970/FY1971/FY1972/FY1973 rows; `timeline.csv` 1970-10 / 1973 / 1974 / 1946-1947; `conflicts.csv` **U.011, U.040, U.045**; `stage_1.md` front matter + §T.3 R-1; `stage_1_index.md`; `03_quality_control/walmart_s1_a6_census.md` |
| **COR-304** | the resolving power of `research/A6_held_corpus_mine.md`'s proposed ids **S0139–S0147**: nine numbers that the merge re-used for nine *other* documents (live **S0145** = the EDGAR floor; A6's S0145 = the Chronicling America 403 challenge bodies) | the dossier's citations, which resolved to the wrong documents; and live `sources.csv` **S0139–S0147**, which carried no trace of the second claim on the number | **alias/redirect notes on both sides in the register** — each live row names what A6 meant by its number and where A6's content is issued; each new row names the id it replaced. The dossier's historical text is **not** rewritten (§14 rule 4, rule 12) | `sources.csv` **S0139–S0147** (redirects) + **S0148–S0155** (aliases); `stage_1.md` §T.3 R-1 / **U.048** entry + front matter |
| **COR-305** | "the FY1973 report … has **no row of its own** in `sources.csv` (it is reached only through S0102's note). Proposed as **S0148**" — and its restatement at RD-123 ("so that defect is still live") | `research/A6_held_corpus_mine.md` §Records for merge line 113 + the FY1973 quantitative rows' `source` cell + closing note; `MASTER_RESEARCH_LOG` RD-097/RD-123; `stage_1.md` front matter reads it through RD-123's "still live" | **FALSE PREMISE — S0102 *is* the FY1973 report's own row** (title "…fiscal year ended January 31, 1973", event 1973-01-31, pub 1973-03-20, `archived_url sources/periodicals/WALMART_AR_1973.txt`), in the root register *and* in the 38-row `research/sources.csv` the dossier itself read. **No duplicate document row minted** (§13 never re-define). What was genuinely uncarried was the **55 + 9 fleet-composition sentence**, now landed against **S0102**. Same entry withdraws A6's "the 34,171 B HathiTrust body is OUTSIDE the repository": it is at `00_universe/harvest/_probe_fixed_20260925/hathitrust/640238bfc6cb7376-r20260925T131232Z.html` | `sources.csv` **S0102, S0155**; `quantitative.csv` FY1973 × 3; `timeline.csv` 1973; `stage_1.md` front matter; `stage_1_index.md` |
| **COR-306** | the year attribution **"51 (FY1971) to 78 (FY1974)"** inside `conflicts.csv` **U.040** CLAIM B, and the dossier's own proposed **High** on the FY1973 = 64 row | `conflicts.csv` U.040; `research/A6_held_corpus_mine.md` quantitative block | the printed heads **1970 1971 1972 1973 1974** against the row **32 38 51 64 78***: 38 = FY1971, 51 = FY1972, 64 = FY1973. All four landed legs of the series are **Medium, not High** — the pairing rests on the OCR header, the **FY1974 page image is UNTRIED** (`S0150` names the renderings), and the 55 + 9 = 64 foot is **one lineage**, an internal check, not corroboration (§3). Original wording stays visible in the cell | `conflicts.csv` **U.040**; `quantitative.csv` FY1970/FY1971/FY1972/FY1973 = 32/38/51/64; `timeline.csv` 1974; `stage_1.md` front matter |

---

## Numbering space for this company

**Six ids are issued in this company's `COR-3xx` space: 301, 302, 303, 304, 305, 306** (301/302 by the 2026-09-26
identity-line repair; 303–306 by the RD-123 A6 re-census, 2026-09-26). The next free number is 307. Amazon's
`COR-0xx` space is separate and does not collide. Naming the range here is what stops a later pass minting a
second entry on an issued number, which is the same defect COR-304 repairs in `sources.csv`.

---

## COR-301 — the Delaware incorporation and the 1969-10-01 date are withdrawn from the volume's identity line

**Supersedes.** The `**Company:**` line of the merged Stage-1 volume (`stage_1.md`), which since the 2026-09-26
merge asserted "Wal-Mart Stores, Inc. — a **Delaware corporation**; incorporated **1969-10-01**". It also
supersedes the merge front matter's claim that the retraction had been disclosed: the disclosure note sat
**above** the identity line while the identity line itself repeated the withdrawn text in bold, present tense,
unretracted — the §14-rule-10 defect class at its highest-severity location, because the header is the line
every cold reader and every downstream pass copies.

**Document evidence (re-run against held documents on this pass, 2026-09-26).**
`grep -ci delaware sources/periodicals/WALMART_AR_1972.txt … _1980.txt` → **0, 0, 0, 0, 0, 0, 0, 0, 0**:
"Delaware" occurs **zero times in all nine held annual reports**. No held document states a state of
incorporation for any Wal-Mart entity, and none states any 1969 date at day precision. The only incorporation
statement anywhere on disk is the registrant's own undated curated history page
(`sources/EXTRACT_corporate_walmart_history_timeline.md`: "1969 — The company officially incorporates as
Wal-Mart Stores, Inc.") — **year only, no month, no day, no state, no citation**, and Tier-4-equivalent as
evidence even though the artifact is Tier-1.

**Replaced by (the carrier of each element now stated in the header).**
- **Registrant name at the close of the window: Wal-Mart Stores, Inc.** — carrier **S0101**
  (`sources/periodicals/WALMART_AR_1972.txt`), the FY1972 report's audited capital note; §B.0 row 1.
- **State of incorporation: UNKNOWN** — carrier: the nine-file verified negative; §B.0 row 2; conflict **U.014**.
- **Incorporation date: 1969, year only, company-asserted; day UNKNOWN** — carriers: the corporate history page
  (**S0141**) for the year, the verified negative for the day; §Q timeline row "1969"; **U.013** CLAIM A.
- **Formation of the consolidated registrant: 1970-02-01**, exchange of common stock accounted for as a
  **pooling of interests** out of "the various subsidiaries" held by **Walton Enterprises, Inc.** — carrier
  **S0101 Note 1**, printed again in the same note's capital breakdown at February 1, 1970; **U.013** CLAIM C.

**What is NOT erased.** `_parts/s1_p1.md`'s header and `stage_1.md` §D record **D-R03** keep their original
wording visible beside their own correction (**D-R03c**) and beside **U.014**: the correction-beside-the-row
pattern is the audit trail, and §14 rule 8 requires the superseded value to be printed where it stood.
**Nothing in this entry rescues the claim for later use.**

## COR-302 — "Wal-Mart, Inc., an Arkansas corporation" is withdrawn from the identity line

**Supersedes.** The second clause of the same `**Company:**` line: "the operating entity from **1962** was
**Wal-Mart, Inc., an Arkansas corporation**". Unlike COR-301 this clause was **disclosed nowhere** in the
merge front matter, so a reader trusting the disclosure note as the complete list of carried defects had no
reason to look for it.

**Document evidence (re-run on this pass).**
`grep -ciE "wal-mart,[[:space:]]*inc" sources/periodicals/WALMART_AR_1972.txt … _1980.txt` → **0 for every one
of the nine** (the pattern excludes "Wal-Mart Stores, Inc."). §B.0 classes the form as **UNATTESTED in this
corpus, Tier-4 folklore** — specifically the "Wal-Mart, Inc., incorporated 15 March 1962" variant — and **U.013**
holds it as CLAIM B, "unattested anywhere on disk". No document in `sources/` names **any** legal person for
1945–1962: the reports say "the various subsidiaries" and never enumerate them, and the FY1978 report's
partnership sentence is retrospective (**U.108**).

**Replaced by.** The header now states that the **1962** operating start is **registrant-retrospective** —
earliest printing **S0103** (`WALMART_AR_1974.txt`, printed 1974-03-21: "The Company's first Wal-Mart Discount
City store opened in Rogers. Arkansas in 1962"), **no in-period document** — and that no legal person is
identified for the 1945–1962 business. The documented formation fact is the **1970-02-01** pooling (COR-301).

**Named FETCH REQUEST (unchanged route, still open).** The question is settleable only outside the current
perimeter: **U.211** Arkansas Secretary of State entity index + Benton County deed/record searches for
"Wal-Mart, Inc." and "Walton Enterprises, Inc.", and **U.203** EDGAR `formerNames` for CIK 104169, which may
state a state of incorporation. Both were UNTRIED at the audit and remain UNTRIED on this pass — zero web
budget. Declining to fetch is the correct behaviour here, not a gap in the correction.

## COR-303 — the Stage-1 merge under-applied `research/A6_held_corpus_mine.md`, and nothing in the register layer showed it

**Supersedes.** `_MANIFEST.md`'s §Proof-of-non-destruction line — "**99 rows requested** (part 2: 40; part 3: 50 rows
+ 3 outbound corrections; A5 pending: 9). **95 applied; 4 refused with printed reasons** … **Nothing dropped**" — and
with it RD-115's use of that line as the evidence that the merge was complete. The arithmetic was right for the
emissions it counted. It counted the wrong set.

**What was missed (re-measured on this pass, 2026-09-26).** `research/A6_held_corpus_mine.md` carries a marked
`>>> REGISTER ROWS FOR MERGE <<<` block (its §Records for merge) with **22 rows in four fenced `csv` blocks** —
9 `sources.csv`, 6 `quantitative.csv`, 4 `timeline.csv`, 3 `conflicts.csv` — last written 2026-09-26 01:15, i.e. **41
minutes before** the merge commit `4781fa0` (01:57) minted the root registers. `grep -c "A6"` returned **0 in all nine
registers**: no applied row carried the emission's provenance, so the loss was invisible from the layer every later pass
reads first.

**Replaced by.** 22 requested = **16 minted** (source ids `S0148`–`S0155`; four `quantitative.csv` rows — FY1971 = 38,
FY1973 = 64, FY1973 = 55, FY1973 = 9; four `timeline.csv` rows — 1970-10, 1973, 1974, 1946-1947) + **6 folded, each with
a printed reason naming the carrier that already holds the content** (the dossier's S0147 → live **S0145**, the register's
existing EDGAR row; its FY1970 = 32 and FY1972 = 51 → the discrete FY1970 row and the composite FY1972 row, whose notes
now name the second carrier; its three conflict requests → **U.011**, **U.040**, **U.045**) + **0 dropped**. Minting was
done at the top of the existing range, never on an issued number (§13).

**Detector finding, reported rather than repaired here.** `tools/merge_census.py` — the tool RD-122 made binding for
exactly this failure — globs `company_dir/_parts/*.md` **only** (its `census()`, line 94). It cannot see an emission under
`research/`, and against this company it printed "**TOTAL missing keyed rows: 0**" and exited **0** while all 22 A6 rows
sat unapplied. A census that misses an emission and reports zero is a broken detector reporting success — the RD-124
class. RD-122's standing rule ("a register-emission census runs before the merge brief is written … over the whole
company directory, parts *and* `research/`") is not implemented by the tool. `tools/` is outside this pass's write set,
so the defect is handed to the orchestrator with this entry as its evidence.

## COR-304 — the merge re-used the ids A6 had proposed: nine numbers, two documents each

**Supersedes.** The reading on which `research/A6_held_corpus_mine.md`'s citations of `S0139`–`S0147` resolve to the
documents they describe. They did not, and do not: those nine ids exist in `sources.csv` carrying **different content**
(verified pair by pair on this pass — live **S0145** = "the EDGAR floor: nothing electronic before 1994-02-14" while
A6's S0145 = the Chronicling America 403 challenge bodies; live **S0141** = the company's curated history page while A6's
S0141 = the IA metadata manifest of the FY1972 item). The merge minted **its own** nine rows into the range
(`_MANIFEST.md`: "sources 38 to 47 (+9)") and never applied the dossier's nine, so a reader following an A6 citation was
sent to an unrelated document rather than told the row was missing. **A re-used id misleads in both files; a dropped row
is only silent** — RD-123's ordering, and the reason this entry is separate from COR-303.

**Repaired in the register, not in the dossier.** Each live row `S0139`–`S0147` now ends with an **ID-COLLISION
REDIRECT** naming what A6 meant by that number and where A6's content is issued; each new row `S0148`–`S0155` carries
the **A6-ALIAS** running the other way, plus the fold pointer for the ninth. The dossier's text is left exactly as
written (§14 rule 4 supersedes; rule 12 addresses a claim by a stable label, so the dossier's `S0145` is now a label with
a defined resolution instead of a broken pointer).

**This was already a known defect class at this company, which is the aggravating fact.** `stage_1.md` §T.3 R-1 and
**U.048** register a collision between `s1_p2.md`'s block and A5's block over `S0141`, with the residual "the final
numbering, which the register owner owns". The mechanism was named in the volume; the census that would have caught the
third claimant on the same numbers was never run. U.048's residual is answered for this range by the alias map now in
`sources.csv`.

## COR-305 — the FY1973 "missing source row" is not missing, and two carriers in the mine were mis-stated

**Supersedes.** `research/A6_held_corpus_mine.md`'s closing note in §Records for merge — "the FY1973 report … has **no
row of its own** in `sources.csv` (it is reached only through S0102's note). Proposed as S0148" — repeated at RD-123 as
"so the defect the mine flagged is still live", and inherited into `stage_1.md`'s front matter through that log.
**It is not live, and it was never true.** `S0102` *is* the FY1973 report's own row — `source_title` "Wal-Mart Stores,
Inc. Annual Report, fiscal year ended January 31, 1973", `event_date` 1973-01-31, `publication_date` 1973-03-20,
`archived_url` `sources/periodicals/WALMART_AR_1973.txt` — in the root register **and** in the 38-row
`research/sources.csv` the dossier itself read and counted (its own gate block prints "sources.csv 38 rows"). The
sentence is also internally contradictory: a document "cited by S0102's row only", where S0102's row *is* that document.
**No duplicate document row was minted** — §13 makes `sources.csv` append-only with ids never re-defined, and a second
FY1973 row would have manufactured precisely the collision COR-304 is repairing. What was genuinely uncarried is the
**fleet-composition sentence**, "the existing fifty-five Wal-Mart and nine variety and family center stores" (re-read on
this pass at lines 396-399 of the held text layer), which now has discrete records in `quantitative.csv` (× 2) and
`timeline.csv` (× 1) against **S0102**.

**Two carrier statements in the same emission are corrected with it.** (i) A6's S0146 clause "the underlying 34,171 B
body is OUTSIDE the repository", echoed at RD-097 as "the search body is not in the repo": the HathiTrust search body
**is** in the repository, at
`00_universe/harvest/_probe_fixed_20260925/hathitrust/640238bfc6cb7376-r20260925T131232Z.html`. `S0155` now points at
it, and the facet (term `"Wal-Mart" Bentonville`, `lmt=ft`, Date of Publication 1960-1969 → **All Items 45 / Full View
4**) re-reads from those bytes rather than from `LEADS.md`'s transcription. The lead stays **UNTRIED at text level** and
**UNKNOWN** as to whether any of the 45 names this company — a rights-verified 1968 customs bulletin matching the phrase
pair is as likely to be OCR or place-name noise. This entry does not upgrade it. (ii) A6's S0141 said the IA metadata
names "the four renderings on offer": the manifest lists **20 files**, and `S0150` now enumerates the requestable
image/text routes. Neither correction moves the naming perimeter RD-097 restored.

## COR-306 — "51 (FY1971)" is a column-shift, and no leg of the five-year series may be promoted above Medium

**Supersedes.** Inside `conflicts.csv` **U.040** CLAIM B, the parenthetical years "51 (FY1971) to 78 (FY1974)". The
printed heads in `WALMART_AR_1974.txt`'s FIVE YEAR PROGRESS REPORT are `1970 1971 1972 1973 1974`, and the store row
reads `32 38 51 64 78*` — so **38 is FY1971, 51 is FY1972, 64 is FY1973**. The digits are unchanged and the original
wording stays visible in the cell beside this pointer (§14 rule 4). The dossier's request to "amend U-A4/6's
parenthetical years" is applied as an amendment to the live carrier, not as a duplicate conflict row.

**Refused on the dossier's reasoning — and three legs carried to High on a better carrier found by re-reading the bytes (§14 rule 8).** The dossier asked **High** for the FY1973 = 64 row on
the ground that the FY1973 report's own "55 + 9" print agrees with it. That second print is the **same registrant
lineage** and is the very sentence being cross-footed, so under §3 it is **one source** and the foot is an internal
arithmetic check; and the pairing of column to year rests on an OCR header whose **page image is UNTRIED**. The dossier's **reason** is refused: no value lands on a lineage cross-footing itself, and the mine's own U-A6/3 cell says the four new store rows "carry Medium, not High". But re-reading for this application surfaced a carrier the mine never cited — **Note 8 — Number of stores in operation**, in the FY1974 report's notes to the audited statements (lines 1595-1599): "the 64 stores at January 31, 1973 consisted of 55 Wal-Mart Stores and 9 Ben Franklin Variety and Family Center Stores". A value printed **beside its date**, inside the audited notes, is not a column position, and the UNTRIED page image cannot bite it. So **FY1973 = 64, FY1973 = 55 and FY1973 = 9 land at High on that carrier**, and the promotion is written into every one of those cells and into this entry rather than slipping past the gate. **FY1970 / FY1971 / FY1972 stay Medium**: their years come only from the table's column order, and while Note 8 demonstrates that the heads are not shifted at the two checkable ends (and FY1975's Note 8 repeats FY1974's composition), an inference about a table is not a printed date beside 38. The FY1974 two-sold/four-closed timeline row is **held at Medium** on the same test: the footnote names no year, and the arithmetic foot (2 + 4 = the 6 closures the same report prints for 1974) is an internal check, not an attribution. `S0150` names what would settle the three legs that remain header-paired: `1974-annual-report-for-walmart-stores-inc` at `<item>.pdf`, `<item>_text.pdf`, `<item>_abbyy.gz`,
`<item>_hocr.html`, `<item>_jp2.zip` — a FETCH REQUEST, not a finding.

## Value refusals on this pass (rule 14-8: nothing lands that was not re-read from held bytes)

| A6 request | Applied? | Reason |
|---|---|---|
| FY1970 = 32, FY1972 = 51 as **new discrete rows** from the FY1974 table | **No — folded** | Both values are already on `quantitative.csv` (FY1970 = 32 discrete, carrier S0101; FY1972 = 51 inside the composite cell). A second row for one metric-date manufactures a witness inside a single lineage. The FY1974-table carrier is recorded in the existing cells' notes instead |
| A new `sources.csv` row for the FY1973 report (its S0148) | **No — premise false** | S0102 already is that row (COR-305). §13 forbids re-defining a source id |
| A new `sources.csv` row for EDGAR `formerNames` + the NoSuchKey probes (its S0147) | **No — folded into S0145** | Same accession family already carried; content applied in the notes |
| A new conflict row for Newport, Arkansas vs Kentucky (its U-A6/1) | **No — already applied by content** | **U.011** carries it and already names A4's prose; A6's decoy mechanism is recorded there |
| **High** confidence on FY1973 = 64 and on the FY1974 two-sold/four-closed timeline row | **Refused — landed Medium** | Same-lineage cross-foot, and the table's page image is UNTRIED (COR-306) |
| A4's two prose corrections (lines 278, 735) | **Not applied** | Another agent owns `research/A4_independent_periodicals.md`; the hand-off is recorded at **U.011** and stays open |
| Any HathiTrust text (its U3 / S0146 "best remaining chance") | **UNTRIED, unchanged** | No item opened; the viewer 403s a script and this pass had zero web budget. Recorded as a lead at `S0155`, never as evidence |

## Corrections still owed by the instruction layer (rule 14-10)

`MASTER_RESEARCH_LOG.md` RD-097 and RD-123 are outside this pass's write set (the log is the orchestrator's), so the
three statements below are handed on rather than fixed here: RD-097's "the search body is not in the repo" (**COR-305**),
RD-123's "the `S0148` source row … is still absent, so that defect is still live" (**COR-305** — the premise, not just
the row, is wrong), and RD-115's acceptance of the merge's "99 rows requested … Nothing dropped" as proof of a complete
merge (**COR-303** — the count was 121). `03_quality_control/walmart_s1_merge.md` also carries the 99/95 arithmetic and
is owned by its author.

## Propagation record

| Surface | COR-301 | COR-302 |
|---|---|---|
| merged volume identity line (`stage_1.md` header) | rewritten, both ids named | rewritten, id named |
| merge assembly note | third-item disclosure added | disclosure added (it was previously absent) |
| `conflicts.csv` | row **U.014** carries the id and the propagation note | row **U.013** carries the id and the propagation note |
| `_MANIFEST.md` defect list | item 1 re-statused | item added |
| registers re-tested | "Delaware" remains only inside retraction language in `conflicts.csv`, `timeline.csv`, `data_gaps.csv` | "Wal-Mart, Inc." appears in registers only as an unattested claim or as a named search target (**U.211**) |

## Propagation record — the RD-123 A6 re-census (2026-09-26, second pass)

Every surface each new id reaches. The `corrections` gate reads the register layer and the stage volumes; a retraction
that lands in one and not the other is the recurring failure this table exists to disprove (RD-105/106/107).

| Surface | COR-303 | COR-304 | COR-305 | COR-306 |
|---|---|---|---|---|
| `sources.csv` | census sentence in the notes of **S0148–S0155**, **S0145**, **S0147**, **S0102** | **ID-COLLISION REDIRECT** on live **S0139–S0147**; **A6-ALIAS** on new **S0148–S0155** | note on **S0102** (the FY1973 row exists) and on **S0155** (HathiTrust body is in-repo) | note on **S0150** (the renderings that would settle the pairing) |
| `quantitative.csv` | FY1970/FY1971/FY1972/FY1973 = 32/38/51/64 and the 55 / 9 rows | alias in each landed row's notes | the 55 + 9 rows cite **S0102**, not a minted duplicate | every leg states the header-pairing caveat and its **Medium** ceiling |
| `timeline.csv` | 1970-10, 1973, 1974, 1946-1947 | alias in each landed row's notes | the 1973 row's source re-resolved to **S0102** | the 1974 footnote row held at Medium |
| `conflicts.csv` | **U.011**, **U.040**, **U.045** carry the fold note | **U.040**'s fold names the re-used-number mechanism | — | **U.040** CLAIM B carries the superseded parenthetical |
| `stage_1.md` | front-matter disposition paragraph, new | same paragraph + a pointer line at **§T.3 R-1 / U.048** | same paragraph | same paragraph |
| `stage_1_index.md` | registers table + new label note | new label note | new label note | new label note |
| `_MANIFEST.md` | proof table re-statused with the 121/99 correction | defect-list item 8 | defect-list item 9 | defect-list item 9 |
| report | `03_quality_control/walmart_s1_a6_census.md` | same | same | same |

