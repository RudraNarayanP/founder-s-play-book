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

## Propagation record

| Surface | COR-301 | COR-302 |
|---|---|---|
| merged volume identity line (`stage_1.md` header) | rewritten, both ids named | rewritten, id named |
| merge assembly note | third-item disclosure added | disclosure added (it was previously absent) |
| `conflicts.csv` | row **U.014** carries the id and the propagation note | row **U.013** carries the id and the propagation note |
| `_MANIFEST.md` defect list | item 1 re-statused | item added |
| registers re-tested | "Delaware" remains only inside retraction language in `conflicts.csv`, `timeline.csv`, `data_gaps.csv` | "Wal-Mart, Inc." appears in registers only as an unattested claim or as a named search target (**U.211**) |
