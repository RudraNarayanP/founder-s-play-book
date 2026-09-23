# Register Gap Report — Amazon.com Stage 1 (`conflicts.csv`, `sources.csv`)

**Agent:** Level-3 Dataset Registrar (completion pass). **Date of work:** 2026-09-23.
**Files written by this pass (and nothing else):** `01_companies/company_001_amazon/conflicts.csv`,
`01_companies/company_001_amazon/sources.csv`, this report.
**Authority:** `00_METHOD_AND_STYLE.md` §13 (columns, quoting, `UNKNOWN` versus empty), §9.4, §3, §5, §6;
`company_001_amazon/CORRECTIONS.md` COR-01…COR-11; `_parts/U_CONCORDANCE.md` (the 42-id spine);
`stage_1.md` §U (the rendered blocks); `research/G_adversarial.md`; `adversarial_review.md`;
`research/_EVIDENCE_CACHE.md`; `sources/s1_graphics/INVENTORY.md`; `sources/` on disk.
**Discipline:** no new facts. Every value added here is present in one of those files. Nothing anywhere was
deleted, moved or tidied.

## Final counts (verified by reading the files back)

| File | Before this pass | After | Verification |
|---|---|---|---|
| `conflicts.csv` | 21 data rows (U.1–U.21) | **42 data rows (U.1–U.42)** | 15 columns on every row; ids strictly U.1…U.42 with **no duplicates and no gaps**; **zero empty cells**; UTF-8 with no non-ASCII bytes; `\n` endings; header unchanged |
| `sources.csv` | 93 data rows | **102 data rows** | 18 columns on every row; **no duplicate `source_id`**; **no duplicate URL** except one pre-existing pair (defect D5); zero empty cells; ASCII; `\n` endings; ids in ascending order |

---

## TASK 1 — `conflicts.csv` U.22–U.42

**Added: 21 rows, U.22 through U.42**, one per canonical id in `_parts/U_CONCORDANCE.md`, textured from
`stage_1.md` §U where §U is full and from the concordance's Adjudication cell where §U is terser (U.24's
AJ-U.25/U.49 pairing, U.27, U.29's basis rule, U.42 from p4's U8). U.1–U.21 were **not** rewritten.

**Missing narrative blocks: NONE.** All 21 of U.22–U.42 have a rendered §U block in `stage_1.md`. The check
was mechanical: the §U span (lines 1003–1907) was parsed into blocks at every `**U.n` line, and each block
was tested for the seven mandated labels (`CLAIM A`, `CLAIM B`, `WHY THEY DIFFER`, `EVIDENCE WEIGHT`,
`BEST-SUPPORTED INTERPRETATION`, `RESIDUAL UNCERTAINTY`, `CONFIDENCE`). All 21 carry all seven, so **zero
AUDIT-1 class defects of the "missing block" kind were found**, and none was fabricated. One artefact of the
test is recorded so nobody re-reads it as a gap: U.31's block initially looked short because a bare
cross-reference line `**U.7**.` sits *inside* it at line 1709 and was picked up as a block start.

**How the columns were populated, and where the text came from:**

* `section` — the sections a conflict actually bears on, taken as the union of (i) the §U block's own in-text
  section references and (ii) the claim-record appendix keys that point at that id in
  `stage_1_claim_records.md` (inverted from the `Conflicts:` fields). No section was invented. U.42 has no
  Amazon cell by design, so its `section` states that explicitly rather than being left empty (§13 forbids
  an empty cell).
* `claim_a_source` / `claim_b_source` — `sources.csv` ids wherever a registered document exists (41 of the 42
  rows cite at least one `S`-id), plus the accession number or filing identity for the SEC rows.
* Discipline held on every row: `evidence_weight` states which side is Tier 1/2/3/4 and why;
  `best_supported_interpretation` states what may be printed **and** what may not, never picking a side
  silently; `residual_uncertainty` states what stays open. 15 of the 21 new rows carry an explicit `UNKNOWN`
  value for something that could not be settled.

**Concordance instruction 3 (stale strings) checked across all 42 rows:** no row asserts "no round total is
disclosed", no row sources $511,000 to Sheff, and no row describes an S-1 page image as recoverable. Two
lexical hits exist and are correct as written: U.8's `evidence_weight` names dossier E's reading **in order to
delete it** ("is SUPERSEDED and deleted … (COR-10)"), and U.21 mentions "recovery-pending" only to forbid it
("must not describe the four page pictures as recovery-pending", COR-04/COR-11.6).

**Defect found in Task 1 and NOT closed:** the 2.7% side of U.37 (1994 CPI) is a compilation that **has no row
in `sources.csv`** — `stage_1.md` §H and `context_appendices.md` contested-figure 2 name it, and the BLS
January-1995 release returned 404. The U.37 row therefore states that the rival compilation is unregistered
and points to this report. This is an AUDIT-2 class provenance gap: the conflict is complete in §U but its
`claim_b` has no locatable source document. Closing it needs a retrieval, which this pass may not perform.

---

## TASK 2 — the G block (S1200–S1399) was never used

**Distinct new sources added: 9**, ids **S1201–S1209**, inserted in ascending id order between S1003 and S1501
(the register's evident geometry; no existing row moved).

| id | source | bears on |
|---|---|---|
| S1201 | Guardian, Hooper, "Amazon at 20" (2014-07-21) | G-15; review E-12 (carries the barred 16 July date) |
| S1202 | Seattle Times, "Amazon at 10: Will it keep clicking?" (2005-07-10) — this is `p.html` | G-16, G-28; review E-12, E-28 |
| S1203 | Wikipedia, "CUC International" (acquisition table) | G-12 |
| S1204 | join1440 "first book" item (HTTP 403, never read) | G-15; review N-8 |
| S1205 | Entrepreneur.com article of 2008-10-10, cited inside S1804 | G-06 |
| S1206 | Inc. / Josh Spiro, undated, cited inside S1804 | G-17; review E-15 |
| S1207 | Publishers Weekly, April 1997 (paywalled, never retrieved) | G-31 (and G-33); review R-8 |
| S1208 | Amazon.com definitive proxy statement for the 1998 meeting | review E-22, N-7; U.28 |
| S1209 | Network Wizards / ISC host-count tables (no capture before 2002-03-28) | review N-8; U.36 |

`claim_supported` carries the challenge ids as instructed; where the adversary files grade the item as a
review element rather than a G challenge, the row says so and cites that element (`E-12`, `N-8`, `R-8`).
`independence_note` is populated on **all 9** rows — that is the register's purpose — e.g. S1203 is marked as
downstream of S0803 and not corroboration of it, S1202 as a mutation of the S1701/S1702 lineage, S1207 as the
**ancestor** of both the S0202 quotation and the S0004 co-operation-talks item.

**Deduplication actually performed** (URL first, then filing identity, then title): the table in
`research/G_adversarial.md` carries 22 entries, and together with the items named in
`adversarial_review.md` the following resolved to rows **already in the register** and were not duplicated —
the three SEC accessions and the 10-K405 (S0801/S0802/S0803/S0805), the 1995-10-04 release and its URLwire
reprint (S1701/S1702), the 1996-bestseller release (S0606), Littman/LA Times (S0202), Sheff (S0203), the 2007
IR timeline (S1710), the Mosaic August-1995 archive (S1001), GeekWire 2013 (S0207), GeekWire 2019 (S0003),
Stone (S0206), HistoryLink (S0004), Wikipedia "History of Amazon" (S1804), Quill (S1501), MarketWatch
(S0611), Kaphan 2011 (S0002).
Four further items were resolved into **existing bundle rows** rather than given new ids, which is recorded
here so nobody re-adds them: the LinkedIn/Facebook/Instagram posts of 2025-2026 and the Grokipedia
"Book Stacks Unlimited" page (both inside **S1802**, whose carrier list already names them); the underlying
CBS Charlie Rose / 60 Minutes Extra appearance (**S0207**); Time's "10 Best Websites of 1996", which reaches
the corpus only as a citation inside the prospectus (**S0804**, with S0803 as the twin).

**Two existing rows had a URL that dossier G records and the register did not hold, and were backfilled**
(nothing else in them altered, original values preserved, reason appended to `notes`):
**S1803** ← `https://www.cnbc.com/2024-01-13/in-1997-jeff-bezos-said-why-he-chose-books-to-sell-on-amazon.html`
and **S1806** ← `https://www.pbs.org/wgbh/frontline/interview/shel-kaphan/`. Those two URLs are precisely the
identity match that deduped the dossier entries against the existing rows instead of creating new S1200 rows.

**Sources with no resolvable origin (registered, cannot be closed):** S1204 (403, no URL ever recorded),
S1205 and S1206 (known only through a Wikipedia sentence; no date, no URL), S1207 (paywalled trade
periodical), S1208 (accession never recorded), S1209 (no in-window capture exists). Each carries `url`,
`archived_url` and `evidence_class` as literal `UNKNOWN` — never empty — and a `notes` clause naming the
route that would close it. Consequence worth stating plainly: while S1206 remains unread, the circulating
"$20,000 a week within two months" figure has **no traceable origin at all**.

---

## TASK 3 — `restoration pending` re-checked against `sources/` on disk

`sources/` as found: the four Amazon accessions (`S-1_original_acc-0000891618-97-001309`,
`S-1A-No3_acc-0000891020-97-000755`, `S-1A-No5_acc-0000891020-97-000839`,
`10-K_FY1997_acc-0000891020-98-000448`), the Sheff interview (`.txt`/`.html`), HistoryLink 23230
(`.txt`/`.html`), `ncsa-mosaic-whats-new_1995-08_kitchencloset.html`, `NULL_RESULT_wayback_1995_1996.md`,
`edgar_s1_index.json`, a duplicate A-No.5 body (`s1_0000891020-97-000839.txt`), `idx.html`/`idx.json`
(which the cache and the directory's own notes identify as SEC "undeclared automated tool" **error pages**,
not sources), and `s1_graphics/` (17 artifacts + `INVENTORY.md`).

**Result: 1 flag cleared, 46 flags kept.** Of the 47 flagged rows, only one describes a document that is now
physically on disk:

* **S1713 cleared** — the Wayback availability-API responses this row asserts are recorded verbatim in
  `sources/NULL_RESULT_wayback_1995_1996.md` (4,427 B, query 7 of 7). Note changed to
  `restored 2026-09-23, re-verified against local copy` plus the file, the byte count and the match basis.
  Nothing else in the row was touched.

The other **46 kept** flags now each **name what is missing** instead of resting on a bare label, and each
states the basis of the match (accession number, publication, or URL — never filename resemblance). The
original note text is preserved after the phrase "Original note text retained verbatim:". The load-bearing
keeps are:

* **The four documents COR-08 names as still missing are all confirmed still missing:** `lat.txt` (S0202),
  `stone.txt` (S0206), `wiki.txt` (S1802, S1804), `amztimeline.html` (S1710), plus `p.html`, which this pass
  registered as **S1202**. `wb_amazon.html` (S1709) remains deliberately unrestored and was never flagged.
* **The named near-miss was refused:** **S1002**, the *NCSA Mosaic home page* as captured 1996-12-20, is **not**
  the restored *Mosaic "What's New" archive for August 1995* (S1001) — different page, different date,
  different URL and different document. Flag kept on that explicit basis.
* **Accession-level matching, not "a filing is on disk":** **S0804** (424B1 / S-1/A No. 6) stays flagged
  because accessions `-000847` and `-000868` exist in `sources/s1_graphics/` only as `index.json` **directory
  listings**, which enumerate a filing and are not the filing. **S0806** (FY1996 annual report) stays flagged
  because no accession or URL was ever recorded, so there is nothing to match against — which is why the 158
  employee figure still has no registered primary (COR-11.2).
* **The two in-window company press releases (S1701, S1703) are the most consequential keeps:** neither is in
  `sources/`. AUDIT 2 re-read both live on 2026-09-24 and recorded verbatim text, but saved no file, so
  **RD-027 remains open** and is the cheapest available closure (two dated in-window company artifacts,
  retrievable at zero research cost).
* Registry and API rows (S0007, S0008, S0009, S1504) stay flagged: re-read live by AUDIT 2, never saved;
  S0009 (`relational.com`) was not even among those re-read, and that is stated in its note.
* **S1707** keeps its flag on a distinction the register must not blur: the CDX **index row** for the
  1999-08-28 homepage is on disk, the **page** is not — existence proved, content not.

**Counting note:** the register now carries **55** rows beginning `restoration pending`, not 46 — the 46 kept
plus the **9 new G-block rows**, every one of whose documents is likewise absent from `sources/`. Clearing a
flag on a row this pass created would have been exactly the error the task warns against.

---

## INCIDENT — a register was destroyed and recovered, stated plainly

While verifying this pass's own additions to `conflicts.csv`, a stray write-mode placeholder line in a
throwaway verification command **truncated `conflicts.csv` to zero bytes** at 20:20. The directory is not a
version-controlled repository, so there was no revert. The file was rebuilt from the session transcript of
the agent that authored it (`Write` → `Edit` → `Edit` → the two recorded `Bash` normalizations, the second of
which replaces 42 descriptive date cells with the ISO values §13 requires), then verified:

* the rebuilt U.1–U.21 block is **43,515 bytes — identical to the pre-loss size recorded in the producing
  agent's own `wc -l`/`ls` output at 19:41**, and it is a byte-exact prefix of the current file;
* the producing agent's own verification output for that state (`cols 15 rows 21`, ids U.1–U.21, no bad rows,
  no empty cells) reproduces exactly;
* 18 field-level spot checks taken from this pass's reads **before** the truncation (section values for
  U.1–U.21, U.1's `claim_a_source`, U.8's `confidence`, U.4/U.16/U.17 date cells) all pass.

`sources.csv` was not affected. **No content was lost**, but the incident is a defect of this pass and is
recorded here rather than quietly repaired. One wording correction was also made to this pass's own new row
U.23: a citation to "COR-13", a directive that exists in `MASTER_RESEARCH_LOG.md` (RD-023) but **not** in the
binding `CORRECTIONS.md`, was replaced by the substance without the label. No row in either register now
cites COR-12, COR-13 or COR-14.

## Defects left open (for AUDIT 1 / AUDIT 2 and the next agent)

1. **U.37's 2.7% CPI compilation is unregistered** (`sources.csv` has S1609 at 2.6% and no row for the rival
   table; the BLS Jan-1995 release 404'd). Provenance gap, AUDIT-2 class.
2. **Six G-block sources have no resolvable origin** (S1204–S1209), itemised above; each is a registered lead,
   not evidence.
3. **Pre-existing duplicate URL:** S1802 and S1804 both carry `https://en.wikipedia.org/wiki/History_of_Amazon`
   while holding different claim bundles and different independence notes. Left alone — merging them would
   destroy a distinction; flagged for the sources auditor.
4. **Attribution mismatch:** S0605's note claims it is the venue of the "science textbook" first-sale variant,
   but `stage_1.md` §F (V3) and §U U.2 attribute that variant to the Seattle Times of **2005-07-10** (now
   S1202). Not reassigned on inference; recorded in both S0605's kept-flag note and here.
5. **46 rows still restoration-pending**, of which the highest-value closures are the two in-window press
   releases (S1701/S1703, RD-027) and the four COR-08 named losses (`lat.txt`, `stone.txt`, `wiki.txt`,
   `amztimeline.html`).
6. **`conflicts.csv` has no `notes`/reason column** in the §13 schema, so this pass recorded every reason for
   change in `sources.csv`'s `notes` field and, for conflict rows, inside `residual_uncertainty` — which is
   why the recovery note and the U.23 wording change live in this report rather than in the CSV.
7. **Register drift outside this brief's authority:** `MASTER_RESEARCH_LOG.md` cites COR-12 (superseding
   COR-03), COR-13 and COR-14, none of which exists in `CORRECTIONS.md`. This pass applied COR-01…COR-11 as
   briefed and followed `stage_1.md` §U text, which is itself written to COR-03/COR-11.2. Someone must
   reconcile the corrections file with the log; it is not this pass's file to edit.
8. **`stage_1.md`'s closing line still says the seven-plus CSVs are "none of which is emitted in this
   pass"** while `conflicts.csv` now stands complete at 42 rows. The narrative header is stale; it was not
   edited because it is outside this brief.
