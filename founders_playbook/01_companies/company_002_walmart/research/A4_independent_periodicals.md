# A4 — Walmart Stage 1: Independent-Periodical Evidence (Business Week annual indexes 1962–1971; *Stores* / NRDGA 1945–1975)

**Dataset:** THE FOUNDER'S PLAYBOOK — forensic longitudinal reconstruction
**Company:** Walmart (Ben Franklin era through the first public years) — `company_002_walmart`
**Stage:** 1 (origin → first real-world experiment → repeatable validation → scalable formation; the
period here is calendar 1945–1980, with the decisive question lying in FY1962–FY1980)
**File role:** the **independent-lineage** dossier. A2 and A3 are the registrant's own voice (annual
reports + auditor opinions, one lineage, independent-lineage count = 1 per A3 §7.2(c)). A4 exists to
test whether a **different publisher** ever printed a contemporaneous witness — of the sector around
Wal-Mart, and, where it exists, of Wal-Mart by name. A4 does not restate A3's financial register and
does not edit it.
**Hindsight firewall (§2):** nothing here states or implies that the discount-sector coverage of
1962–1971 was about a future winner. Business Week's indexes of those years carry no Wal-Mart entry;
that absence is itself reported as evidence, and no article is read forward into later success.
Anti-hagiography test applied per record: would the record still read as plausible if the chain had
failed in 1975? Where it would not, the record was rewritten.
**Confidence scale (§3):** High = 2+ independent lineages or a primary document · Medium = one reliable
source, or approximate date corroborated later · Low = conflicting, vague, or retrospective-only ·
UNKNOWN = no evidence recovered.
**Tier discipline as used here (§5):** Business Week and *Stores* (NRDGA) are **Tier 2** (serious
business publication) and **Tier 3** (industry/trade publication) respectively **for facts about the
company**, and **Tier 1 for "what was publicly known and when"** — because a dated, paginated printed
index is contemporaneous printed matter and is exactly what a market-as-knowable section (§H) needs.
Both usages are labelled in every record; a trade-press sector article is never promoted into a
company fact.

---

## Working method and request budget

**Method (in this order, deliberately):**

1. **Indexes first, issues second.** Business Week's annual index volume is a finding aid:
   subject/company alphabetical → headline → printed page → issue date. It was read to locate articles;
   only then were specific layers attempted. Per the intake's own state table (§3 of
   `00_universe/harvest/periodicals_intake/_MANIFEST.md`), Business Week **issue** scans on Internet
   Archive run 1929 → c.1961 and 1962–1976 is **index volumes only**; there is **no 1972–1976 at all**.
   So for 1962–1971 the index is not a convenience, it is the whole reachable surface, and index entries
   are cited as **index-level evidence** and labelled as such — headline + page + date, nothing about the
   article's content.
2. **Reuse of the harvester's proven-working routes only.** `advancedsearch.php` (48/48 HTTP 200 for the
   intake), `metadata/<identifier>` (29/29 HTTP 200, with `{}` = UNANSWERED), and the
   metadata→`<server>`+`<dir>`→`<file>_djvu.txt` text-layer GET. `archive.org/download/` is **not** used
   (reproduced TLS failure: "certificate has expired", 0 bytes). Sequential requests, `≥2.5 s` delay,
   UA `FoundersPlaybook-A4-walmart-periodicals/1.0 (research@example.org)`, TLS verification ON,
   back-off armed on 429/503 (and reported rather than blind-retried).
3. **Bounded extracts only, and never near the cap.** Full SIM text layers (1962 index 1.27 MB /
   196,549 words; 1964 index 1.29 MB / 205,497 words; a *Stores* issue ≈38,000 words) are written to an
   **OS scratch directory outside the repository** and only selected, topic-block extracts land in
   `sources/periodicals/` with a provenance header, character/line offsets and byte-count equality vs
   the item's own metadata — matching the naming conventions already in that directory
   (`_PROVENANCE_PERIODICALS.md`, `WALMART_AR_<year>.txt`, `ia_*.json`, `STUB_LEAD_*.md`). Raw catalogue
   JSON is kept to selected fields. No file approaches 60,000 words or 200 MB (§9.2).
4. **Write-first gate (§14 rule 1) — the log.** This file was created on the first write call after
   reading §3/§5/§7/§14 and the intake `_MANIFEST.md`, carrying its full section skeleton plus
   **16 real records** transcribed from the intake's already-retrieved, byte-verified Business Week index
   extract. Records are appended after every issue mined; nothing is accumulated in scratch.
   **Nothing outside this file and `sources/periodicals/` was written. No file was deleted, moved,
   renamed or tidied (§14 rule 4); A2/A3/B, every register CSV, `MASTER_RESEARCH_LOG.md` and the whole of
   `periodicals_intake/` are untouched.**
5. **Two separate tallies, kept apart.** *Wal-Mart-named* coverage (a witness to the company) and
   *sector* coverage (a contemporaneous witness to industry conditions) are counted in different sections
   and different columns. A sector article does not discharge a company-claim; A3 §7.2(d)'s requirement —
   a **non-company contemporaneous count of Wal-Mart's stores or sales** — is tested only against the
   first tally.
6. **No silent reconciliation.** Where a press figure disagrees with the registrant's filed figure, both
   sides go to `## Independent figures vs registrant figures` and `## Contradictions`.

**Web budget: hard cap 60.** Planned and spent as recorded in `## Provenance ledger` (one row per item,
with HTTP status and byte count). Spending at write-time of this skeleton: **0**. Kept unspent on
purposes that cannot answer (Chronicling America / HathiTrust / Google Books remain the blocked routes
and are recorded UNANSWERED, not re-burnt here except one confirming probe at most).

---

## Findings

Records follow §7 claim-record format, one line per field-set. "Item" = Internet Archive identifier;
"p." figures are Business Week's *own printed page* plus issue date, as printed in the index, not scan
pages (the SIM layers carry no page-boundary markers).

A4-01 Claim: **Business Week's 1962 annual index — the index of the very year the first Wal-Mart
Discount City opened at Rogers, Arkansas — carries a `DISCOUNT Houses` subject block with at least
eight dated entries, and carries NO entry for "Wal-Mart", "Wal-Mart Stores", "Ben Franklin" or
"Arkansas".** Date: 1962 (index covering Jan–Dec 1962) — Source: *Business Week 1962: Index*, item
`sim_business-week_1962_index`, text layer 1,273,570 B / 196,549 words — Source date: published 1963 for
volume 1962 (SIM microfilm binding) — URL:
`https://ia802906.us.archive.org/14/items/sim_business-week_1962_index/sim_business-week_1962_index_djvu.txt` —
Archived: intake scratch layer, byte-exact vs metadata; passages retained in
`00_universe/harvest/periodicals_intake/walmart_variety_sector/BUSINESSWEEK_INDEX_1964-1971_EXTRACT_discount_retail.txt`
L658–977 (offsets `DISCOUNT Houses` line 10086, 45100; `WALTON, William` line 68032) — Tier: 2 for
"what was publicly known in 1962"; N/A as to the company — Class: FACT (as to presence/absence in the
printed index; an absence inside one stated perimeter) — Passage: "DISCOUNT Houses … Discount store
dropouts # pl01, Oct.6 … Shake-out among discounters seen as chain files in bankruptcy p83, Oct.27" —
Conf: Medium (pending my own re-walk of this layer in this run, then High for the 1962 perimeter) —
Corroboration: 1 independent publisher (Business Week), 6 index years — Conflicts: none.

A4-02 Claim: **"Discount store dropouts", Business Week, printed page 101, issue of Oct.6 1962 — a
dated, paginated third-party citation on discount-store failures published within seven months of the
first Wal-Mart opening.** Date: 1962-10-06 (article); index printed 1963 — Source: `sim_business-week_1962_index`,
`DISCOUNT Houses` block, layer lines 45100–45117 — URL: as A4-01 — Archived: intake extract L873–887 —
Tier: 2 (market-knowability) — Class: CONTEMPORARY OBSERVATION, at **index level only** (headline +
page + date; the article text is NOT reachable on this route and nothing from it is quoted or implied) —
Passage: "Discount store dropouts # pl01, Oct.6" — Conf: High (that BW indexed such an article on that
date in that issue at that page) — Corroboration: same index family, 2 printings (lines 39239 and 45117
of the layer, SIM OCR duplicating the block with different left margins) — Conflicts: none.

A4-03 Claim: **"Shake-out among discounters seen as chain files in bankruptcy", Business Week p.83,
Oct.27 1962 — contemporaneous third-party statement that the discount sector was consolidating by
failure in the same calendar year as Wal-Mart's founding.** Date: 1962-10-27 — Source: `sim_business-week_1962_index`,
`DISCOUNT Houses` / `BANKRUPTCY Act` blocks, lines 45117–45119, 38668–38685 — URL: as A4-01 —
Archived: intake extract L852–887 — Tier: 2 — Class: CONTEMPORARY OBSERVATION (index-level evidence) —
Passage: "Shake-out among discounters seen as chain files in bankruptcy p83, Oct.27" — Conf: High —
Corroboration: 1 publisher, 2 printings within the layer — Conflicts: none.

A4-04 Claim: **"Discounters strive to ride out storm: Fast-growing $6-billion industry is facing a major
shakeout", Business Week p.78, Dec.1 1962 — an INDEPENDENT (non-registrant) size figure for the whole
discount industry at the moment Wal-Mart entered it: $6 billion.** Date: 1962-12-01 — Source:
`sim_business-week_1962_index`, `DISCOUNT Houses` block, lines 45119–45125 (also "Discounters strive to
ride out storm p78, Dec.1" at line 49785) — URL: as A4-01 — Archived: intake extract L885–912 — Tier: 2
— Class: FACT (that the figure was published) / CONTEMPORARY OBSERVATION (as to the industry) — Passage:
"Discounters strive to ride out storm: Fast-growing $6-billion industry is facing a major shakeout
(with illus) p78, Dec.1" — Conf: High (as an indexed publication) · UNKNOWN (as to BW's source for the
$6 billion, since no FY-registered definition of "discount industry" is in this corpus) —
Corroboration: 1 publisher, 2 printings — Conflicts: none; and note this is a **sector** figure, not a
company figure, so it cannot be entered as a Wal-Mart metric.

A4-05 Claim: **"Another discounter enters bankruptcy court as Grayson-Robinson case worries lenders",
Business Week p.146, Sep.22 1962, and "Discounter caught in cash bind: Grayson-Robinson's plight may
presage a discount house shakeout", p.109, Aug.18 1962 — the sector's credit conditions named
contemporaneously.** Date: 1962-08-18 and 1962-09-22 — Source: `sim_business-week_1962_index`, lines
45113–45117, 38668, 49785–50027 — URL: as A4-01 — Archived: intake extract L852–910 — Tier: 2 —
Class: CONTEMPORARY OBSERVATION (index-level) — Passage: "Another discounter enters bankruptcy court as
Grayson-Robinson case worries lenders p146, Sep.22" — Conf: High — Corroboration: 1 publisher, ≥2
printings — Conflicts: **see U-A4/1** — the Aug.18 page is printed variously `p109`, `pl109`, `pl169`
across the layer's duplicate printings of the same block.

A4-06 Claim: **Business Week's 1962 index points at TWO non-company data sources for discount-store
counts — `AUDITS & Surveys Co.` ("Data on discount stores offers … progress they have been making",
p.5?) and a truncated `Dun & Bradstreet reports on number of disc…` entry — i.e. the very
"non-company contemporaneous count" A3 §7.2(d) names as the witness that would move Walmart's depth
verdict was, in 1962, a real and indexed thing.** Date: 1962 — Source: `sim_business-week_1962_index`,
`AUDITS & Surveys Co.` block line 2449, `Discounters invade food field` block line 10099 (last line:
"Dun & Bradstreet reports on number of dis-") — URL: as A4-01 — Archived: intake extract L662–673,
L695–706 — Tier: 2 — Class: FACT (that the index carries the pointer) / INFERENCE (that such a count
exists in a reachable corpus — NOT established) — Passage: "Dun & Bradstreet reports on number of dis-" —
Conf: Medium (pointer legible, its object unread) — Corroboration: 1 publisher — Conflicts: none.
**Recorded as a LEAD, not as evidence: the D&B/AUDITS volume itself is UNTRIED and no page number for it
survives OCR in full.**

A4-07 Claim: **The only "Walton" strings in Business Week's 1962 and 1970 indexes are other people:
"WALTON, William — Motel chain finds profits in owning: Holiday Inns is acquiring franchised units",
p.47, Jul.14 1962, and "G. H. Dreyfus, H. C. Walton p4, Aug.29" (1970). Neither is the Arkansas family;
citing either as Wal-Mart would be a fabrication.** Date: 1962-07-14; 1970-08-29 — Source:
`sim_business-week_1962_index` line 68032; `sim_business-week_1970_index_0` — URL: as A4-01 and
`https://ia800500.us.archive.org/31/items/sim_business-week_1970_index_0/sim_business-week_1970_index_0_djvu.txt` —
Archived: intake extract L964–967, and L36–38 of its header note — Tier: 2 — Class: FACT (as to what the
index says) — Passage: "WALTON, William — Motel chain finds profits in owning: Holiday Inns is acquiring
franchised units (with illus) p47, Jul.14" — Conf: High — Corroboration: 1 publisher, checked in context
by the intake and re-checked here — Conflicts: none. **This is a documented decoy and is recorded so no
later pass mistakes it for a named witness.**

A4-08 Claim: **Business Week's 1964 index `DISCOUNT Houses` block carries "Nielsen survey shows an
increase in the number of mass merchandisers", p.100, May 16 1964 — an independent counting operation
(A. C. Nielsen) addressing the mass-merchandiser population two years after Wal-Mart's founding.**
Date: 1964-05-16 — Source: `sim_business-week_1964_index_0`, `DISCOUNT Houses` block, layer line 9299 —
URL: `https://ia902902.us.archive.org/33/items/sim_business-week_1964_index_0/sim_business-week_1964_index_0_djvu.txt` —
Archived: intake extract L98–105 — Tier: 2 — Class: CONTEMPORARY OBSERVATION (index-level) — Passage:
"Nielsen survey shows an increase in the number of mass merchandisers # p100, May 16" — Conf: High —
Corroboration: 1 publisher — Conflicts: none.

A4-09 Claim: **Business Week's 1964 index carries a `WOOLWORTH (F. W.) Co.` entry — "The old five-and-ten
spreads new wings: Woolworth branches out into mass merchandising in varied lines" (with cover and
illus) p.58, Nov.14 1964, plus the short item "…is setting up Worth Marts, discount mass-volume stores",
p.24, Dec.26 1964 — i.e. the largest incumbent five-and-dime publicly moving into discount
mass-merchandising, contemporaneously indexed.** Date: 1964-11-14; 1964-12-26 — Source:
`sim_business-week_1964_index_0`, lines 37549, 38625, 51331, 59275, 66309 — URL: as A4-08 — Archived:
intake extract L220–260 — Tier: 2 — Class: FACT (indexed publication) / CONTEMPORARY OBSERVATION (as to
industry structure) — Passage: "The old five-and-ten spreads new wings: Woolworth branches out into mass
merchandising in varied lines (with cover and illus) p58, Nov.14" — Conf: High — Corroboration: 1
publisher, ≥5 printings of the entry in the layer — Conflicts: none.

A4-10 Claim: **Business Week's 1969 index carries `DISCOUNT Stores` entries "Discount stores getting
tryout" p.98, Aug.2 1969 and "A discounter is a Washington department store" p.108, Sept.20 1969 — the
sector's reach into small/capital-city markets indexed in the year before Wal-Mart's NYSE listing.**
Date: 1969-08-02; 1969-09-20 — Source: `sim_business-week_1969_index_0`, `DISCOUNT Stores` block, layer
line 30150 — URL: `https://ia800408.us.archive.org/25/items/sim_business-week_1969_index_0/sim_business-week_1969_index_0_djvu.txt` —
Archived: intake extract L334–343 — Tier: 2 — Class: CONTEMPORARY OBSERVATION (index-level) — Passage:
"Discount stores getting tryout # p98, Aug.2" — Conf: High — Corroboration: 1 publisher — Conflicts: none.

A4-11 Claim: **Business Week's 1970 index runs "How Kresge became top discounter (with cover, chart and
illus) p.62, Oct.24 1970" under THREE separate subject blocks — `DISCOUNT Houses`, `KRESGE (S. S.) Co.`
and `VARIETY Stores` — which is third-party evidence that the discount-department-store race and the
variety-store (Ben Franklin) trade were publicly treated as one competitive field in Wal-Mart's first
public year.** Date: 1970-10-24 — Source: `sim_business-week_1970_index_0`, lines 6991–7010, 12772,
21795 — URL: `https://ia800500.us.archive.org/31/items/sim_business-week_1970_index_0/sim_business-week_1970_index_0_djvu.txt` —
Archived: intake extract L415–493 — Tier: 2 — Class: FACT (three block placements as printed) /
INFERENCE (that BW saw the two trades as one field — an inference from the taxonomy, mechanism stated) —
Passage: "How Kresge became top discounter (with cover, chart and illus) p62, Oct.24" — Conf: High —
Corroboration: 1 publisher, 3 index placements — Conflicts: none. **Kresge/Kmart is the comparator that
A2's competitor section relies on the registrant to name; here a third party names it independently.**

A4-12 Claim: **Business Week's 1970 index carries "Discounting: a food chain reaction (with illus) p.44,
Sept.26 1970" — grocery discounting indexed as an active process in the year Wal-Mart's FY1971 report
would have been written.** Date: 1970-09-26 — Source: `sim_business-week_1970_index_0`, lines 6991, 12601 —
URL: as A4-11 — Archived: intake extract L422–452 — Tier: 2 — Class: CONTEMPORARY OBSERVATION
(index-level) — Passage: "Discounting: a food chain reaction (with illus) p44, Sept.26" — Conf: High —
Corroboration: 1 publisher, 2 printings — Conflicts: none.

A4-13 Claim: **Business Week's 1971 index places discounting in an international frame — `DISCOUNT
Stores`: "France: The French go wild over discount stores (with illus) p.40, Nov.20 1971" — and keeps a
live `RETAILING` block with dated monthly reads (e.g. "Early gainer: retailing p20, Aug.21 1971"),
i.e. retail sales as a monitored series, not company narrative.** Date: 1971 — Source:
`sim_business-week_1971_index_0`, lines 7591–7600, 21105 — URL:
`https://ia800908.us.archive.org/33/items/sim_business-week_1971_index_0/sim_business-week_1971_index_0_djvu.txt` —
Archived: intake extract L496–633 — Tier: 2 — Class: CONTEMPORARY OBSERVATION (index-level) — Passage:
"France: The French go wild over discount stores (with illus) p40, Nov.20" — Conf: High —
Corroboration: 1 publisher — Conflicts: none.

A4-14 Claim: **Business Week's 1966 index carries the Kresge cover story in two incompatible page
readings: "Kresge's … (with cover and illus) p.126, Jan.29 1966" at layer line 8338/26577 and "…p26,
Jan.29" at line 18506/18507 — and its `DISCOUNT Houses` block is almost wholly lost to OCR ("Allied
Stores Corp. Fy, fi / Sar dincains be ee").** Date: 1966-01-29 — Source: `sim_business-week_1966_index_0`,
lines 8338, 9336, 18506, 26577 — URL:
`https://ia800606.us.archive.org/17/items/sim_business-week_1966_index_0/sim_business-week_1966_index_0_djvu.txt` —
Archived: intake extract L1005–1020, L1098–1102 — Tier: 2 — Class: FACT (that the layer prints both, and
that the block is illegible) — Passage: "Kresge's triple-threat … (with cover and illus) p126, Jan.29" —
Conf: Medium (the entry exists; the page is not settleable from this layer) — Corroboration: 1 publisher —
Conflicts: **U-A4/2**. **Nothing is quoted from the 1966 `DISCOUNT Houses` block; per the intake's own
OCR note it is unreadable and is recorded as UNANSWERED for that year's discount block.**

A4-15 Claim: **Across all six Business Week annual indexes retrieved (1962, 1964, 1966, 1969, 1970,
1971) there is NO index entry naming Wal-Mart, Wal-Mart Stores, Ben Franklin, or "five-and-dime" as a
subject — the company is absent from the largest general-business weekly's own subject apparatus
throughout its founding decade, including the two years in which it listed publicly.** Date: 1962–1971 —
Source: six items as above; intake header note lines 35–38 of
`BUSINESSWEEK_INDEX_1964-1971_EXTRACT_discount_retail.txt` — URL: as A4-01/08/11 and 1964/1966/1971
layers — Archived: intake scratch layers, each byte-exact vs metadata-declared size (1,273,570 /
1,286,804 / 1,177,551 / 711,758 / 336,463 / 397,185 B) — Tier: 2 — Class: FACT as to BW's apparatus;
**NOT a null as to the world** — Passage: NO_VERBATIM_PASSAGE_RECORDED (an absence; the supporting
passages are A4-01…A4-14) — Conf: Medium pending my re-walk of ≥3 of the six layers in this run —
Corroboration: 1 publisher × 6 years — Conflicts: none. **Honest statement of scope: an index absence
proves only that BW did not index the company that year. It does not prove BW did not print it, and it
does not prove no other periodical printed it.**

A4-16 Claim: **The *Stores* (National Retail Dry Goods Association) family holds a complete monthly run
1945–1961 — 205 digitised items with text layers — which spans Sam Walton's Newport, Kentucky and
Ben-Franklin decade, the nineteen years in which EDGAR, web archives and Wal-Mart's own printed report
run are all silent; one issue (Jan 1960, `sim_stores_1960-01_42_1`, 269,490 B, 38,238 words) was proved
retrievable and legible, returning 25 "discount" hits including a presidential editorial on the
mandatory functional-discount bills.** Date: 1945–1961 (run); 1960-01 (the proved issue) — Source:
Internet Archive `identifier:(sim_stores*) AND YEAR:[1945 TO 1990]` → numFound 205 — URL: search
endpoint `https://archive.org/advancedsearch.php?q=…` plus the metadata→server→dir text-layer route —
Archived: `…/periodicals_intake/walmart_variety_sector/STORES_NRDGA_1960-1975_EXTRACT_discount_variety.txt`
(8,017 B) — Tier: 3 for company facts; 1 for market-knowability — Class: FACT (as to the run's
existence, byte counts and retrieval) — Passage: recorded in the intake extract; not re-quoted here until
re-walked in this run — Conf: High (existence and retrievability), UNKNOWN (as to whether any issue names
Walton's or Wal-Mart) — Corroboration: 1 route (IA), 1 publisher class (association print) — Conflicts:
none. **This record is a capability statement, not a company fact, and is not used as one.**

### A4-re-01 … A4-re-16 — INDEPENDENT RE-WALK OF THE SIX LAYERS (my own greps, not the intake's)

The records A4-01…A4-16 above are transcribed from the intake's bounded extract. **This run re-fetched
and re-grepped the layers myself**, so the load-bearing negatives are now my own, not reported hearsay.
Each row: item · HTTP status · bytes received vs metadata-declared · verdict of the equality test · words ·
my term counts (case-folded over the whole layer).

| # | Item re-walked | Status / bytes | Word count | `wal-mart` `walmart` `walton` `arkansas` `rogers` `ben franklin` `newport` `discount` |
|---|---|---|---|---|
| R1 | `sim_business-week_1962_index` | 200 · 1,273,570 B = declared → **EXACT** | 196,549 | 0 · 0 · 1 · 1 · 4 · 0 · 3 · **88** |
| R2 | `sim_business-week_1964_index_0` | 200 · 1,286,804 B = declared → **EXACT** (after one read-timeout ERR then success) | 203,895 | 0 · 0 · 0 · 0 · 1 · 0 · 0 · 40 |
| R3 | `sim_business-week_1970_index_0` | 200 · 336,463 B = declared → **EXACT** | 52,380 | 0 · 0 · 1 · 1 · 2 · 0 · 2 · 14 |
| R4 | `sim_business-week_1963_index` **(NEW YEAR, intake had not touched 1963)** | 200 · 605,043 B = declared → **EXACT** | 100,003 | 0 · 0 · 0 · 0 · 1 · 0 · 0 · 6 |
| R5 | `sim_business-week_1965_index` **(NEW YEAR)** | 200 · 612,999 B = declared → **EXACT** | 98,569 | 0 · 0 · 0 · 0 · 0 · 0 · 0 · 14 |
| R6 | `sim_business-week_1967_index` **(NEW YEAR)** | 200 · 611,323 B = declared → **EXACT** | 96,935 | 0 · 0 · 0 · 3 · 0 · 0 · 0 · 10 |
| R7 | `sim_business-week_1968_index` **(NEW YEAR)** | 200 · 914,791 B = declared → **EXACT** | 147,820 | 0 · 0 · 3 · 0 · 3 · 0 · 4 · 24 |

A4-17 Claim: **An independent re-walk of the Business Week 1962 index layer — 1,273,570 bytes received
against 1,273,570 declared, 196,549 words read whole — returns `wal-mart` 0, `walmart` 0,
`ben franklin` 0, `five-and-dime` 0, `variety store` 0 against `discount` 88: the founding year of the
company is, in the largest general-business weekly's own apparatus, a year of heavy discount-sector
attention and zero company attention.** Date: index to the 1962 volume — Source:
`sim_business-week_1962_index` — Source date: 1963 (SIM bound index) — URL: as A4-01 —
Archived: A4 scratch (whole layer, outside repo), bounded extract in
`../sources/periodicals/BUSINESSWEEK_INDEX_1962-1971_EXTRACT_walmart_and_sector_hits.txt` —
Tier: 2 — Class: FACT (as to this index volume; an absence inside a stated perimeter) —
Passage: "WALTON, William — Motel chain finds profits in owning: Holiday Inns is acquiring franchised
units (with illus) p47, Jul.14" — Conf: **High (upgraded from A4-01/A4-15's Medium, now my own read)** —
Corroboration: 1 independent publisher × 7 years re-walked in this run; intake's byte-identical pass is a
second retrieval of the same item, **not** a second lineage — Conflicts: none.
**Every non-zero hit is a decoy, all located by character offset and read in context:**
`walton` 1 @1,250,972 = William Walton/Holiday Inns; `arkansas` 1 @682,589 = "ARKANSAS Louisiana Gas Co.
— Metering of air conditioning … p56, Jul.28"; `rogers` 4 @505,234 / 505,348 / 1,137,287 / 1,137,416 =
ROGERS Cartage Co., ROGERS Irving, ROGERS Charles, ROGERS Charles F. Jr. — **no Rogers, Arkansas**;
`newport` 3 @431,597 / 431,662 / 1,067,884 = NEWPORT News Shipbuilding & Dry Dock Co. and **"NEWPORT, Ky.
— Boycott of Communist-made goods bolstered through $1,000 license by Kentucky town p38, Dec.15"**.
**The Newport, Ky. entry matters twice:** it is a town-subject entry for exactly the town of Walton's
1945–1950 franchise, and it proves Business Week's index *does* carry Newport-Kentucky and
Arkansas entries when it has a story to carry — so the zero for Wal-Mart is an informed silence about
the company, not a blind one about the geography.

A4-18 Claim: **The three *Stores* (NRDGA) annual indexes never retrieved by the intake — 1971 and 1972 —
were fetched and grepped in this run and name neither Wal-Mart nor Walton: for FY1972, Wal-Mart's first
fiscal year with a contemporaneous printed report, the variety-trade's own journal produced no company
entry.** Date: indexes to volumes 53 (1971) and 54 (1972) — Source: `sim_stores_1971_53_index`
(201,20/20,120 B = declared → EXACT, 2,780 words) and `sim_stores_1972_54_index` (17,704 B = declared →
EXACT, 2,480 words) — Source date: 1972-01 and 1973-01 (each index is bound in the following January
issue) — URL: metadata→server→dir route, `https://ia600409.us.archive.org/32/items/sim_stores_1971_53_index/…`
and `https://ia903200.us.archive.org/7/items/sim_stores_1972_54_index/…` — Archived: A4 scratch, extracts
to `../sources/periodicals/` — Tier: 3 (company facts) / 1 (knowability) —
Class: FACT (as to these two volumes) — Passage: NO_VERBATIM_PASSAGE_RECORDED (absence) —
Conf: Medium — **downgraded from High by the structural caveat below** — Corroboration: 1 publisher
(NRDGA), 5 index volumes now searched (1970, 1971, 1972, 1974, 1975; the first, third-by-intake) —
Conflicts: none.
**Structural caveat that caps this at Medium, and must travel with the record:** *Stores*' annual index is
organised **by subject heading only** — `Advertising, Promotion, Display` / `Merchandising` / `Operations`
/ `Personnel` / `Consumer…` — with **no company-name alphabetical sequence** (my counts on both layers:
`Chain` 0, `Chains` 0, `Woolworth` 0, `Kresge` 0). A zero therefore means only "no article indexed under
that subject-word", not "the journal never mentioned the firm". Business Week's index, which does carry a
company sequence (`WOOLWORTH (F. W.) Co.`, `KRESGE (S. S.) Co.`, `VARIETY Stores`), is the stronger
instrument, and its seven-year zero is correspondingly stronger evidence.

A4-19 Claim: **Business Week's index volumes for the four years the intake never reached (1963, 1965, 1967,
1968) are in hand, and they are NOT all full-year: the items bound as `sim_business-week_1963_index`,
`…_1965_index` and `…_1967_index` are HALF-YEAR indexes, proven by month-token counts, and this must be
stated before any "no Wal-Mart that year" claim is made for them.** Date: 1963/1965/1967/1968 —
Source: the four layers (bytes EXACT, see table above) — Source date: as bound — URL: metadata→server→dir —
Archived: A4 scratch — Tier: 2 — Class: FACT (arithmetic of month tokens) / ESTIMATE —
Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High — Corroboration: 1 publisher —
Conflicts: none.
**The arithmetic (§7 requires the derivation to be shown):** occurrences of the month tokens in each
layer — 1963: Jan 652 · Feb 670 · Mar 792 · Apr 728 · May 949 · Jun 797 · **Jul 0 · Aug 0 · Sep 1 ·
Oct 0 · Nov 0 · Dec 0**, and the header string "January-June" appears 36 times, "July-December" 0 →
**1963 = January–June only**. 1965: **Jan 2 · Feb 4 · Apr 1 · May 185 · Jun 0** against Jul 646 · Aug 606 ·
Sep 719 · Oct 799 · Nov 746 · Dec 570, "July-December" 39, "January-June" 0 → **1965 = July–December only**.
1967: Jan 699 → Jun 776, **Jul–Dec all 0** → **January–June only**. 1968: every month 495–815, both
half-year headers present (Jan–Jun 31, Jul–Dec 20) → **full year**. Consequently the 1963/1965/1967 zeros
cover **half** of each year, and the missing halves are the enumerated siblings
`sim_business-week_business-week_july-december-1963_index`,
`…_january-june-1965_index`, `…_july-december-1967_index-contents` — pulled in the next pass.

A4-20 Claim: **The decoy that this dossier was created to catch: Business Week's "Small town greets the
discounters", p.90, Oct.3 1964 — the entry that reads most like Wal-Mart's own origin story — is indexed
under ALDENS, Inc., the Chicago mail-order and variety-discount chain. It is a witness to a COMPETITOR's
small-town discount expansion, and it is NOT evidence about Wal-Mart.** Date: 1964-10-03 — Source:
`sim_business-week_1964_index_0`, character offset 665,015 in the layer — URL: as A4-08 —
Archived: A4 scratch + extract file — Tier: 2 — Class: FACT (as printed in the index) —
Passage: "Gold rush begins for Alaska trade: Operators are crowding into the Alaskan — business (with map
and illus) p186, Oct.1 | ALDENS, Inc. | Small town greets the discounters p90, Oct.3 | ALEXANDER & Baldwin,
Inc." — Conf: High — Corroboration: 1 publisher; the headline appears 13 times across the duplicated OCR
blocks of the same layer, all inside the `ALDENS, Inc.`/subject alphabet, never under Wal-Mart —
Conflicts: none. **Recorded as RESEARCH DEBT CLOSED: an earlier hand would have filed this headline as
support for a "Walmart invented small-town discounting" claim.**

A4-21 Claim: **Business Week's 1968 index, the fullest of the four new years (914,791 B, 147,820 words,
all twelve months), carries `walton` 3 and `rogers` 3 and `newport` 4 and none of them is the company or
the town: Dr. C. Walton Lillehei (surgeon), "WALTON, Richard" of the Rhodes-tinkerer inventor story,
ROGERS Jimmy and ROGERS William P., NEWPORT News Shipbuilding / Newport Bridge / "NEWPORT, R. I.". And
`wal-mart` = 0 while `discount` = 24.** Date: 1968 — Source: `sim_business-week_1968_index` —
Source date: 1969 — URL: metadata→server→dir route — Archived: A4 scratch + extract file — Tier: 2 —
Class: FACT (with offsets) — Passage: "WALTON, Richard … tinkerer scoops the pros: Richard … Walton has a
talent for anticipating needs before the market becomes obvious" — Conf: High — Corroboration: 1 publisher —
Conflicts: none. **Note the Lillehei hit: Minnesota medicine, unrelated to company_003 as well — the
surname is a trap for two companies in this project.**

A4-22 Claim: **In the two years Business Week indexed Arkansas matter at all, the matter was infrastructure,
not retail: 1967 `arkansas` 3 = "ARKANSAS River — Oklahoma's stairway to the sea: Billion-dollar Arkansas
River project will open both Arkansas and Oklahoma to barges by 1970 (with map and illus) p186, Apr.22",
and 1970 `arkansas` 1 = "ARKANSAS River — The waterway that couldn't be done (with map and illus) p124,
Sept.12" — so Arkansas entered the national business press as a geography of transport, while Wal-Mart did
not enter it as a company.** Date: 1967-04-22; 1970-09-12 — Source: `sim_business-week_1967_index` offsets
36,129 / 36,197 / 426,395; `sim_business-week_1970_index_0` offset 15,949 — URL: as A4-19 / A4-11 —
Archived: A4 scratch + extract file — Tier: 2 — Class: FACT (index-level for the articles; the index text
itself is quoted) — Passage: "The waterway that couldn't be done (with map and illus) p124, Sept.12" —
Conf: High — Corroboration: 1 publisher, 2 years, 4 printings — Conflicts: none.

### A4-23 … A4-29 — *STORES* (NRDGA/NRMA) MONTHLY RUN 1945–1961, MINED ISSUE BY ISSUE

The monthly run is the only in-window periodical body that could name **Walton's** before FY1972 — i.e.
before A3's earliest witness of any kind (1972-03-22). Six issues have now been retrieved whole and
grepped in this run, one per year-band across the Newport and Bentonville decades, plus the Jan-1960
issue the intake proved. Each layer arrived HTTP 200 with bytes **equal to the metadata-declared size**
(241,457 / 312,972 / 218,329 / 260,354 / 288,685 B classes), and each was read whole through an OS
scratch directory; only the offsets below enter the repo.

A4-23 Claim: **The *Stores* issue of June 1950 (vol 32 no 6, `sim_stores_1950-06_32_6`, 241,457 B, 34,243
words — the year Sam Walton's Newport, Kentucky experiment ended) returns `walton` 0, `wal-mart` 0,
`ben franklin` 0, `newport, ky` 0, `arkansas` 0, against `nrdga` 6: the association's own journal gives no
独立 visibility to this franchisee at the close of his first five-and-a-half years.** Date: 1950-06 —
Source: `sim_stores_1950-06_32_6` — Source date: 1950-06 — URL: metadata→server→dir route —
Archived: A4 scratch; extract to `../sources/periodicals/STORES_NRDGA_1950-1961_EXTRACT_walton_and_discount.txt` —
Tier: 3 (company facts) / 1 (knowability) — Class: FACT (as to these six issues sampled; **NOT a null for
the 200-issue run**) — Passage: "June, 1950 THE PRESIDENT'S PAGE … By CHARLES G. NICHOLS President, NRDGA"
(@10,124) — Conf: Medium — Corroboration: 1 publisher — Conflicts: none.
**Perimeter stated exactly: 6 of ~200 issues in the 1945–1961 run have been read. The remaining 194 are
UNTRIED. This record may not be cited as "the trade press ignored Walton's", only as "the issues sampled
do not name it".**

A4-24 Claim: **June 1951 (`sim_stores_1951-06_33_6`, 312,972 B, 44,599 words): `walton` 0, `wal-mart` 0,
`bentonville` 0, `springdale` 0, `ben franklin` 0; the single `arkansas` hit is the U.S. Congress, not
retailing — "Representative Wilbur Mills, Democrat of Arkansas, prominent member of the Ways and Means
Committee, has introduced H.R. 4133"** — a decoy recorded so no later pass mistakes a state name for the
company's home state.** Date: 1951-06 — Source: as above, offset 17,822 — Source date: 1951-06 —
URL: metadata→server→dir — Archived: A4 scratch + extract — Tier: 3 — Class: FACT — Passage: "Employment
Security Financing Act of 1951. Representative Wilbur Mills, Democrat of Arkansas" — Conf: High —
Corroboration: 1 publisher — Conflicts: none. **This issue also carries the NRDGA's Washington
representative column (John Hazen) 14 times, i.e. the journal is a policy organ of the trade — which is
why its silence on a member's discount venture is informative rather than empty.**

A4-25 Claim: **June 1955 (`sim_stores_1955-06_37_6`, 218,329 B, 30,608 words): no company name at all, and
the trade's attention is downtown renewal and price-control policy, with `discount` 16 occurrences almost
all inside Controllers' Congress cost tables ("Cash Discounts — % of Sales 2.6 2.8 2.6 …") rather than
about discount stores — a caution for any later grep that counts the word.** Date: 1955-06 — Source:
offsets 22,681 / 29,879 / 29,946 / 32,027 — Source date: 1955-06 — URL: metadata→server→dir —
Archived: A4 scratch + extract — Tier: 3 — Class: FACT / INFERENCE (that a raw `discount` count conflates
employee- and cash-discount accounting with discount retailing — mechanism stated) — Passage: "Away With
Summer Slump — NRDGA President Philip M. Talbott kicked off the joint campaign of the NRDGA and the
American Newspaper Publishers Association to promote summer sales" — Conf: High — Corroboration: 1
publisher — Conflicts: none.

A4-26 Claim: **A QUANTIFIED, NON-COMPANY MEASUREMENT OF DISCOUNT PENETRATION, published four years before
Wal-Mart's founding: *Stores*, June 1958, reporting a survey of its own member stores — "It is evident,
too, according to this survey, that the spread of discount houses over the country is slowing down. Only
28 per cent of the stores reported more discount houses operating in their communities, six per cent
reported fewer such stores while the remainder (66 per cent) indicated no change."** Date: 1958-06 —
Source: `sim_stores_1958-06_40_6` (260,354 B, 36,833 words), offsets 32,746 and 32,858 — Source date:
1958-06 — URL: metadata→server→dir — Archived: A4 scratch + extract — Tier: 3 (2 for a serious survey
report) — Class: FACT (as printed) / CONTEMPORARY OBSERVATION — Passage: "Only 28 per cent of the stores
reported more discount houses operating in their communities, six per cent reported fewer such stores
while the remainder (66 per cent) indicated no change" — Conf: High — Corroboration: 1 publisher; the
survey's own respondent universe is **not disclosed in the passage and is UNTRIED** — Conflicts: none.
**This is the first hard, independent, numeric market-state datum this project holds for the years before
Wal-Mart, and it says the sector was already decelerating in the member stores' own report. It is
evidence about the SECTOR, and it is not evidence about Wal-Mart's prospects; the market-as-knowable use
is legitimate (§H), the company-use is not.**

A4-27 Claim: **March 1961 (`sim_stores_1961-03_43_3`, 288,685 B, 40,880 words) — the calendar year in which
the Wal-Mart project was being prepared — carries `walton` 0, `wal-mart` 0, `rogers, ark` 0, `arkansas` 0,
`ben franklin` 0, and its `discount` 7 hits include one sentence of pure sector ideology: "he cited the
willingness to try new ways as a factor in the success of the discount house".** Date: 1961-03 — Source:
offset 32,048 — Source date: 1961-03 — URL: metadata→server→dir — Archived: A4 scratch + extract —
Tier: 3 — Class: FACT (index of what the issue does and does not contain) / CONTEMPORARY OBSERVATION (the
sentence) — Passage: "…as a factor in the success of the discount house" (OCR interleaved: the column
reflow prints "wifi four ingness to try new ways as a facto other in the success of the discount house,
the") — Conf: Medium (**the sentence is recovered by reconstructing two interleaved OCR columns; the
reconstruction is stated, not laundered**) — Corroboration: 1 publisher — Conflicts: none.

A4-28 Claim: **The 1958 issue's `arkansas` hit is a state-name list in a table (a roster of states by
region, @173,557, "…Oklahoma Illinois Utah Connecticut Maryland Arkansas Wisconsin Montana…"), and the
journal by then styles itself "STORES, the NRMA Magazine" — the National Retail Dry Goods Association
having become NRMA, the same body whose franchise the Walton stores were.** Date: 1958-06 — Source:
`sim_stores_1958-06_40_6` offset 173,557 — Source date: 1958-06 — URL: metadata→server→dir — Archived: A4
scratch + extract — Tier: 3 — Class: FACT — Passage: "46 STORES, the NRMA Magazine" — Conf: High —
Corroboration: 1 publisher — Conflicts: none. **Recorded because the NRDGA→NRMA rename is the reason the
intake's `creator:("ben franklin stores")` route returned 0, and because a state roster is the second kind
of Arkansas decoy in this corpus (after the 1962 gas company).**

A4-29 Claim: **The methodological finding of the monthly pass: a named witness to Walton's Newport decade
is NOT produced by sampling ordinary issues, because *Stores* is a management-and-policy journal
(Controllers' Congress cost studies, Washington columns, convention and downtown-renewal reporting), not a
directory. The evidence that would name a member store — membership rosters, territory lists, chain
directories — lives in NRDGA/NRMA **yearbooks and directories**, which the intake proved ABSENT from this
corpus (Ben Franklin's own print: 0 hits; "chain statistical" yearbook queries: 1 irrelevant hit).**
Date: 1945–1961 (the run's character) — Source: six sampled layers + the intake's state table —
Source date: — URL: — Archived: A4 scratch — Tier: — Class: INFERENCE (mechanism: publication genre
determines whether a small franchisee is named at all; alternative explanation: the company simply was not
newsworthy, which no sample of 6 issues can exclude) — Passage: NO_VERBATIM_PASSAGE_RECORDED —
Conf: Medium — Corroboration: 1 publisher — Conflicts: none.
**Consequence for the depth verdict, stated plainly: the periodical route in hand is a good instrument for
the SECTOR and a weak one for the COMPANY, and no number of further *Stores* issues is likely to change
that. The named witness, if it exists, is more likely in local newspaper print (blocked family) or a
directory (absent family) than in either serial now reachable.**

### A4-30 … A4-36 — THE THREE HALVES THAT CLOSE 1963 / 1965 / 1967, AND WHAT THEY SAY ABOUT THE TRADE

A4-30 Claim: **The missing halves are now retrieved, so Business Week's index coverage of Wal-Mart's first
decade is continuous month-by-month 1962 → 1971, and `wal-mart` is 0 in every half-volume: 1963 Jul–Dec
(`sim_business-week_business-week_july-december-1963_index`, HTTP 200, 633,645 B = declared → EXACT,
99,760 words), 1965 Jan–Jun (`…_january-june-1965_index`, 637,923 B EXACT, 100,903 words), 1967 Jul–Dec
(`…_july-december-1967_index-contents`, 556,337 B EXACT, 88,978 words).** Date: 1963–1967 —
Source: the three layers — Source date: SIM-bound indexes of 1964 / 1966 / 1968 — URL:
`https://ia601007.us.archive.org/15/items/…1963_index_djvu.txt`,
`https://ia800104.us.archive.org/28/items/…1965_index_djvu.txt`,
`https://ia800809.us.archive.org/12/items/…1967_index-contents_djvu.txt` — Archived: A4 scratch, whole;
per-year counts and offsets in
`../sources/periodicals/BUSINESSWEEK_INDEX_1962-1971_EXTRACT_walmart_and_sector_hits.txt` — Tier: 2 —
Class: FACT (as to BW's index apparatus, now 10 index years / 13 half-and-full volumes read) —
Passage: NO_VERBATIM_PASSAGE_RECORDED (an absence) — Conf: High — Corroboration: 1 publisher —
Conflicts: none. **Month-token proof travels with the extract: 1963-H2 jul 698 · aug 871 · sep 782 ·
oct 729 · nov 1,000 · dec 594 against jan 3 · feb 0 · mar 0 · apr 0 · jun 0; 1965-H1 jan 799 → jun 703,
jul–dec 0; 1967-H2 jul 646 → dec 555, feb 0 · apr 0 · jun 0.**
**The company-naming result across the whole decade is now: 1962, 1963, 1964, 1965, 1966, 1967, 1968,
1969, 1970, 1971 — ten years, `wal-mart` 0 in all ten.**

A4-31 Claim: **The 1963 second-half index carries the two most useful independent industry statements in
this whole dossier, both with date and page: a discount-store sales total of $6.9 billion for calendar 1962
(short news item, p.132, Jul.13 1963) and a Dun & Bradstreet survey of discount stores' most profitable
departments (p.79, Nov.9 1963).** Date: 1963-07-13; 1963-11-09 — Source:
`sim_business-week_business-week_july-december-1963_index`, `DISCOUNT Houses` block, raw offset 180,304 —
Source date: index bound 1964 — URL: as A4-30 — Archived: extract file, block printed verbatim —
Tier: 2 — Class: FACT (as indexed; the printed entry is OCR-reflowed and is quoted exactly as it came) —
Passage: "stores amounted to $6.9 / billion in 1962 # p132, Jul.13" and "Survey by Dun \® Bradstreet shows
that / and television arte the most profitable departments / in a sampling of discount stores # p79, Nov.9" —
Conf: High (that BW indexed these items on those dates at those pages) · **Low (as to what universe the
$6.9 billion measures: no definition is reachable, and the department names are partly lost to OCR)** —
Corroboration: 1 publisher; see U-A4/5 against BW's own "$6-billion industry" of Dec.1 1962 —
Conflicts: **U-A4/5**.
**Why this is the record A3 asked for by name — and why it still does not move the verdict:** A3 §7.2(d)
asked for "a non-company contemporaneous count of Wal-Mart's stores or sales". Here at last is a
non-company contemporaneous count **of the trade** (D&B sampling discount stores; a national dollar
volume for 1962). It is independent of the registrant, dated, and paginated. **It is not a count of
Wal-Mart**, so the company's independent-lineage count is unchanged — but the market-state layer now rests
on third-party arithmetic instead of on inference from the company's own later account. **The D&B volume
itself remains UNTRIED.**

A4-32 Claim: **"Fewer stores to share the pie: They get bigger but decrease in number as discounters,
chains squeeze 'little guys'", Business Week p.182, Nov.16 1963 — the independent press statement that in
Wal-Mart's second year the DISCOUNT-STORE COUNT WAS FALLING while units grew, and that chains were
squeezing small operators.** Date: 1963-11-16 — Source: same `DISCOUNT Houses` block @180,304 —
Source date: index bound 1964 — URL: as A4-30 — Archived: extract file — Tier: 2 —
Class: CONTEMPORARY OBSERVATION (index-level: headline, page, date; the article text is unreachable) —
Passage: "Fewer stores to share the pie: They get bigger but decrease in number as discounters, chains
squeeze 'little guys' p182, Nov.16" — Conf: High (as an indexed citation) — Corroboration: 1 publisher —
Conflicts: **U-A4/6** (a falling industry unit-count set against the registrant's rising one).
**Hindsight-firewall duty (§2): this is what an operator could read in November 1963, and it is the
opposite of an obvious opportunity. The dataset records the squeeze narrative as the knowable state; it
does not recast it as a tide the founder cleverly rode, because no evidence in this corpus says he knew of
it or acted on it.**

A4-33 Claim: **1963's second half shows exactly what Business Week indexed when it indexed "Arkansas": ten
hits, all education, race and politics — "ECONOMIC Education Workshop of Arkansas — Arkansas schools get
economics-minded (with illus) p112, Jul.20", the same story indexed under "FAUBUS, Orval", plus
`WALTON, William B. — A single standard for travelers p114, Nov.16`, a third Walton decoy. Not one 1963
Arkansas hit concerns retailing, and not one Walton is the family.** Date: 1963 — Source: offsets 191,552 /
191,562 / 197,104 / 217,893 (arkansas); 610,172 (walton) — Source date: index bound 1964 — URL: as A4-30 —
Archived: extract file — Tier: 2 — Class: FACT (with offsets) — Passage: "Arkansas schools get
economics-minded (with illus) p112, Jul.20" — Conf: High — Corroboration: 1 publisher — Conflicts: none.
**Recorded twice over: as the fourth documented decoy family (`wal-mart` 0, `walton` 1 unrelated, 1963 H2),
and as the honest statement that the company's home state was visible in the national business press in
1963 for reasons that had nothing to do with discount retailing.**

A4-34 Claim: **By June 1965 — three years after opening — the sector's own success was being doubted in
print by name: "Is success spoiling discount stores? Moves to carry more costly merchandise worry
in[du]stry leaders (with illus)", Business Week p.97, Jun.2 1965; the same block prints "Is the franchise
system legal? Supreme Court answer[ed] … when it decides GM violated Sherman Act" p.66, Apr.3 1965 —
the franchise-law question that bore directly on the Ben Franklin form — and "Mix discounts and art—and
make sales jump: Honest Ed's, offbeat Toronto discounter, now a mink-coat trade" p.50.**
Date: 1965-06-02; 1965-04-03 — Source: `sim_business-week_business-week_january-june-1965_index`,
`DISCOUNT HOUSES` block @186,570; `ROGERS, Byron G. — Is the franchise system legal p66, Apr.3` @510,490 —
Source date: index bound 1966 — URL: as A4-30 — Archived: extract file — Tier: 2 — Class:
CONTEMPORARY OBSERVATION (index-level) — Passage: "Is success spoiling discount stores? Moves to carry
more costly merchandise worry me[n] industry leaders (with illus) p97, Jun.2" — Conf: High —
Corroboration: 1 publisher — Conflicts: none. **`wal-mart` 0 and `walton` 0 in this half-volume; the
sector was newsworthy, the company was not. Note also that a 1965 franchise-law story is indexed, which is
the nearest this corpus comes to the legal environment of Walton's own franchise form — and the article
text is unreachable, so it is a pointer only.**

A4-35 Claim: **1967's second half carries the fourth "small town" decoy: "Helping a small town cope with
prosperity (with illus) p.184, Sep.23 1967", indexed three times and belonging to a steel-mill town story
("Laughlin has kept its Hennepin [Ill.] steel mill from setting off a runaway boo[m]") — not to discount
retailing in any town, least of all Rogers.** Date: 1967-09-23 — Source:
`sim_business-week_business-week_july-december-1967_index-contents`, offsets 60,091 / 113,701 / 297,854 —
Source date: index bound 1968 — URL: as A4-30 — Archived: extract file — Tier: 2 — Class: FACT (offsets) —
Passage: "Helping a small town cope with prosperity (with illus) p184, Sep.23" — Conf: High —
Corroboration: 1 publisher, 3 index placements — Conflicts: none. **Recorded because "small town" is the
phrase most likely to be mistaken for Wal-Mart's own positioning; across ten index years it never once
attaches to the company, and where it does attach, it attaches to Aldens/Gamble-Skogmo (1964) or to a
steel town (1967).**

A4-36 Claim: **1958–1961: the trade's own arithmetic on discount penetration, in the journal of the
association Walton's franchise belonged to. June 1958 (*Stores* vol 40 no 6): "It is evident, too,
according to this survey, that the spread of discount houses over the country is slowing down. Only 28 per
cent of the stores reported more discount houses operating in their communities, six per cent reported
fewer such stores while the remainder (66 per cent) indicated no change." December 1961 (*Stores* vol 43
no 11, the NRMA Discount Seminar issue, `discount` 67 times in 24,370 words): NRMA "membership covers over
11,500 retail establishments with a combined annual sales of over $19 billion"; about "800 people" attended
the seminar, "about one half were representatives of conventional department stores, the rest were
discounters"; hard-goods discount markup "26 to 28 per cent"; a sizing formula pairing store square
footage with trading-area population; "a serious 'over-concentration' of discount stores"; and S. E.
Nichols Company, "operator of Nichols Discount Cities since 1958, and with a long previous history in
variety stores".** Date: 1958-06 and 1961-12 — Source: `sim_stores_1958-06_40_6` offsets 32,746 / 32,858;
`sim_stores_1961-12_43_11` offsets 13,749 (association scale), 61,464 (attendance), 74,633 (markup),
84,160 and 84,355 (the size/population formula and "over-concentration"), 91,292 (Nichols) — Source date:
as printed — URL: metadata→server→dir (both layers HTTP 200, bytes EXACT) — Archived:
`../sources/periodicals/STORES_NRDGA_1946-1972_EXTRACT_walton_and_discount.txt` — Tier: 3 for the company,
**Tier 1 for what the trade knew in 1958 and in December 1961** — Class: FACT (as printed) /
CONTEMPORARY OBSERVATION / ESTIMATE for the formula's column pairing —
Passage: "operator of Nichols Discount Cities since 1958, and with a long previous history in variety
stores" — Conf: High for the quoted sentences; **Medium for the size/population table, whose OCR reads
"Sq. Ft. Populal'en 30,000 . Under 100,000 60 000-100,000 . 250,000 500,000 100,000-125 000 . 1,000 000
Over 150,000 . Multi-million" — column pairing is not settleable from this layer (U-A4/7)** —
Corroboration: 1 publisher; the seminar figures are a trade body reporting on its own event, so they are
**self-report inside a third party** and are not treated as an independent measurement of the industry —
Conflicts: **U-A4/7**.
**Two duties discharged here. (a) Anti-hagiography: Nichols "with a long previous history in variety
stores" converting to discount cities from 1958 is a published precedent for exactly the move the
registrant later narrates as its own, printed three months before the first Wal-Mart opened; the origin
story therefore sits inside a trade-wide conversion, not outside it. (b) The $19 billion / 11,500 figures
must carry the label "NRMA membership aggregate", never "the discount industry" — it is not a discount
count and must not become a denominator (see the CSV notes).**

---

## Wal-Mart-named coverage, year by year 1962–1980

This is the section that decides the verdict. "Named witness" = a periodical item that prints
Wal-Mart / Wal-Mart Stores / Walton's by name, reached through a **finding aid that was actually
searched** for that year. Three states are kept distinct and are never collapsed:
**EMPTY** (the finding aid was searched and is silent), **UNANSWERED** (a route exists but the article
text is not reachable — index-level only), **UNTRIED** (no finding aid for that year has been reached).

| Year | Finding aid actually searched (this run unless noted) | Named witness? | Status | Precision of the silence |
|---|---|---|---|---|
| 1962 | BW 1962 index, **re-walked whole by A4** (196,549 words; bytes EXACT) | **NO** | **EMPTY within BW's index — full year** | Jan–Dec all indexed (month tokens 811–1,366 per month); the volume carries a company-name sequence. Sector hits `discount` 88. Decoys located by offset: WALTON William (Holiday Inns), ARKANSAS Louisiana Gas, 4× ROGERS, NEWPORT Ky. |
| 1963 | BW `sim_business-week_1963_index` (**NEW YEAR — intake never touched 1963**) | **NO** | **EMPTY within BW — but only JANUARY–JUNE** | Half-year item (Jul–Dec month tokens = 0). Sibling `sim_business-week_business-week_july-december-1963_index` **UNTRIED**. `discount` 6. |
| 1964 | BW 1964 index, **re-walked whole by A4** (203,895 words) | **NO** | **EMPTY within BW — full year** | "Small town greets the discounters" p.90 Oct.3 resolved to **ALDENS, Inc.** — a competitor, not us (A4-20). `variety store` 2, `woolworth` 6, `discount` 40. |
| 1965 | BW `sim_business-week_1965_index` (**NEW YEAR**) | **NO** | **EMPTY within BW — but only JULY–DECEMBER** | `discount` 14. The Jan–Jun sibling **UNTRIED**. |
| 1966 | BW 1966 index (intake-retrieved, byte-exact 1,177,551 B; not re-walked by A4) | **NO** | EMPTY within BW — full year | `DISCOUNT Houses` block OCR-lost (A4-14): the EMPTY covers the legible blocks, not the whole volume. |
| 1967 | BW `sim_business-week_1967_index` (**NEW YEAR**) | **NO** | **EMPTY within BW — but only JANUARY–JUNE** | `arkansas` 3 = the Arkansas River barge project only (A4-22). Jul–Dec sibling **UNTRIED**. |
| 1968 | BW `sim_business-week_1968_index` (**NEW YEAR, re-walked whole: 147,820 words**) | **NO** | **EMPTY within BW — full year** | `discount` 24; 3× WALTON / 3× ROGERS / 4× NEWPORT all unrelated persons and places (A4-21). |
| 1969 | BW 1969 index (intake-retrieved, byte-exact 711,758 B) | **NO** | EMPTY within BW — full year | `DISCOUNT Stores` tryout entries (A4-10). Not re-walked by A4: Medium as to my perimeter, High as to the intake's byte test. |
| 1970 | BW 1970 index **re-walked whole by A4** (52,380 words) **+** *Stores* 1970 annual index (intake) | **NO** | **EMPTY within BW (full year) + EMPTY within *Stores* (subject-only apparatus)** | Kresge "top discounter" cover story (A4-11); `walton` 1 = H. C. Walton, a letter-writer; `arkansas` 1 = Arkansas River. |
| 1971 | BW 1971 index (intake) **+** **Stores 1971 annual index — fetched and grepped by A4 this run** | **NO** | **EMPTY within both** | *Stores* 1971: `wal-mart` 0 · `walton` 0 · `ben franklin` 0 · `variety` 0 · `discount` 0 — A4-18 states why that zero is weak. |
| 1972 | **Stores 1972 annual index — fetched and grepped by A4 this run** | **NO** | **EMPTY within *Stores*** | Wal-Mart's first fiscal year with a contemporaneous printed report: the trade journal of the association that franchised Ben Franklin carries no entry naming it. No BW index for 1972 exists on IA. |
| 1973 | none exists on this route | UNKNOWN | **UNTRIED (no finding aid available)** | *Stores* 1973 index absent from the family; BW indexes stop at 1971. |
| 1974 | *Stores* 1974 annual index (intake-retrieved, 24,487 B) | **NO** | EMPTY within *Stores* (subject-only) | Sector content present: "The Discount Store Manager — MRI/duPont Study", Nov p.26 |
| 1975 | *Stores* 1975 annual index (intake-retrieved, 18,054 B) | **NO** | EMPTY within *Stores* (subject-only) | Sector: "Could Nostalgia Reverse the Trend Toward Discount Retailing", Feb p.39 |
| 1976 | none reached | UNKNOWN | **UNTRIED** | BW 1972–1976 indexes EMPTY on IA; no *Stores* 1976 index in the family. |
| 1977 | none reached | UNKNOWN | **UNTRIED** | |
| 1978 | none reached | UNKNOWN | **UNTRIED** | |
| 1979 | none reached | UNKNOWN | **UNTRIED** | |
| 1980 | none reached | UNKNOWN | **UNTRIED** | Stage-1 close. No finding aid for 1976–1980 has been reached by any pass in this project. |

**Tally at this point.** Years with an independent named witness: **0 of 19 (1962–1980)**.
Years whose absence is a *searched, full-year, company-sequence* EMPTY: **1962, 1964, 1968, 1970**
(Business Week, re-walked whole by A4) plus 1966 and 1969 (intake-retrieved, byte-exact, full-year).
Years whose absence is **half-year only**: 1963 (Jan–Jun), 1965 (Jul–Dec), 1967 (Jan–Jun).
Years whose absence rests on a **subject-only trade index**: 1970, 1971, 1972, 1974, 1975 (*Stores*).
Years with **no finding aid reached at all**: 1973, 1976, 1977, 1978, 1979, 1980.

**The remaining path to a named witness, and the only one in hand:** the *Stores* **monthly** run
1945–1961 (200 items enumerated by A4 this run, each with a text layer) is the only in-window periodical
body that could name **Walton's** before FY1972 — therefore the only route available to this project to a
witness dated earlier than **1972-03-22**, the date of A3's earliest witness of any kind.

---

## Sector coverage as market-state evidence

What the sector print establishes for §H ("Market as knowable in-period") is a **public, contemporaneous
catalogue of attention** — dated pages a 1962–1971 operator could have read — not company evidence.

1. **1962: the discount trade was publicly understood as being in financial distress.** Business Week
   indexed, within one calendar year: food-discount incursion (p.62 Feb.3), a Korvette move upmarket
   (p.72 Feb.10), Walgreen buying three Houston discount stores (p.36 Mar.24), Parke Davis switching to
   sell directly to discounters (p.54 Apr.), Grayson-Robinson's cash bind (p.109 Aug.18), another
   discounter in bankruptcy court (p.146 Sep.22), "Discount store dropouts" (p.101 Oct.6), a
   shake-out as a chain filed bankruptcy (p.83 Oct.27), and the industry-level statement of a
   fast-growing $6-billion industry facing a major shakeout (p.78 Dec.1).
   **Market-state effect:** a 1962 entrant into discounting was entering a sector the trade press was
   actively writing down. **That is a fact about the sector's condition and it does not tell us anything
   about whether the new entrant was well- or ill-run** — the hindsight firewall is satisfied only in this
   direction, by refusing to convert the sector's troubles into the company's good fortune.
2. **1964: the sector was being counted by third parties** (Nielsen mass-merchandiser count, May 16,
   p.100) **and the incumbent variety chains were entering it** (Woolworth cover story Nov.14 p.58;
   Worth Marts short item Dec.26 p.24; also "Bus line adds a destination: Houston transit company opens
   a discount house to lure riders" p.78).
3. **1966: Kresge's mix of "upgrading, discounting, and experimenting" ran with cover** (Jan.29) — the
   variety-to-discount conversion thesis was public print, not a later historian's frame.
4. **1969–1971: discounting becomes a named subject in its own right**, with the Kresge "top discounter"
   cover story (Oct.24 1970 p.62) cross-indexed under VARIETY STORES — the two trades publicly fused.
5. **1960 (*Stores*, NRDGA): the association's own journal carried a presidential editorial on the
   mandatory functional-discount bills** — i.e. the variety-store trade's politics of discounting were
   live in the exact trade body whose franchisee Walton was. Pending re-walk; see Findings.

**Coda (§7 interpretive-duty check).** Evidence: the six BW indexes and the *Stores* family as listed.
Mechanism: index volumes are published by the periodical about its own output, so a dated page is a
public, checkable statement of what the periodical chose to cover. Alternative explanation, kept live:
the sector's coverage may have been carried by titles Business Week did not index — *Chain Store Age*,
*Discount Store News*, *Discount Merchandising* — all three proved EMPTY-for-Internet-Archive by the
intake and therefore UNANSWERED as to their content (blocked hosts). Confidence: High that BW covered the
sector as described; Medium that this is a fair picture of *total* press attention, since the sector's own
trade press is not in hand.

---

## Independent figures vs registrant figures

**Rule: both sides stay. A press figure that disagrees with the filed figure opens a contradiction; it is
never reconciled silently, and never substituted.**

| Metric | Press value + citation | Filed value + document | Difference / status |
|---|---|---|---|
| Discount industry size, 1962 | **$6 billion** — Business Week, "Discounters strive to ride out storm: fast-growing $6-billion industry is facing a major shakeout", p.78, Dec.1 1962 (`sim_business-week_1962_index`) | NO FILED VALUE — the registrant's earliest printed report on disk is FY1972; FY1962 sales are EMPTY in A3 | **Not comparable.** Industry ≠ company. Kept as market-state only; entered in `quantitative.csv` as a sector metric, not as a Wal-Mart metric. |
| Wal-Mart net sales FY1962 | UNKNOWN — no periodical figure recovered in this run (BW 1962 index names no Wal-Mart) | EMPTY (A3: FY1962–FY1967 have no row in any summary table of any of the nine reports) | No conflict possible; the cell is empty on both sides. |
| Wal-Mart store count, FY1962–FY1971 | UNKNOWN as to a press count; a **pointer** to non-company counts exists (D&B / AUDITS & Surveys, 1962 index — A4-06, object UNTRIED) | FY1968 = 24 stores, FY1971 = 51, from the FY1972 report's own five-year table (A3, same lineage as the registrant) | **The independent count this row demands has not been reached.** Until then the store series has one voice. |
| Number of mass merchandisers / discount stores | Nielsen survey reported as increasing — BW p.100, May 16 1964 | Registrant prints no industry total | Different universes; the press figure is the only one available, and its denominator is not defined in this corpus. |
| FY1972–FY1980 sales / earnings / stores | none recovered yet in this run | A3's contemporaneous report values (nine files, `WALMART_AR_1972…1980.txt`) | Rows are added here as and when a press figure with an actual number is found; a headline without a number does not enter this table. |

---

## Contradictions

Format per §7 (`CLAIM A / CLAIM B / WHY THEY DIFFER / EVIDENCE WEIGHT / BEST-SUPPORTED INTERPRETATION /
RESIDUAL UNCERTAINTY / CONFIDENCE`). A4 IDs are U-A4/n and do not renumber U-A2/n or U-A3/n.

**U-A4/1 — Grayson-Robinson cash-bind story, printed page 109 or 169 (Aug.18 1962).**
CLAIM A: `p109, Aug.18` (1962 index, layer lines 38668 and 49785). CLAIM B: `pl169, Aug.18` (line 45113).
WHY THEY DIFFER: SIM microfilm OCR reflows the alphabetical block and duplicates it with different
left margins; the leading `1` is either a page digit or a margin artefact absorbed into the number.
EVIDENCE WEIGHT: two printings for A, one for B; both are the same machine's output on the same volume,
so they are NOT two witnesses. BEST-SUPPORTED INTERPRETATION: **p.109** (majority of printings), recorded
with the alternative printed beside it. RESIDUAL UNCERTAINTY: **the volume's own page images are not in
this corpus; Business Week issue scans for 1962 are not on this route, so this cannot be closed at all by
anything reachable now.** CONFIDENCE: Medium (A), Low (B).

**U-A4/2 — Kresge 1966 cover story, page 26 or 126 (Jan.29 1966).**
CLAIM A: `p26, Jan.29` (1966 index, lines 18506–18507). CLAIM B: `p126, Jan.29` (lines 8338, 26577).
WHY THEY DIFFER: same OCR duplication/reflow mechanism. EVIDENCE WEIGHT: equal printings, same volume.
BEST-SUPPORTED INTERPRETATION: **no page is asserted; the entry is cited by headline, issue date and
cover status only.** RESIDUAL UNCERTAINTY: unresolvable on this route. CONFIDENCE: High (the story
existed, with cover, on that date), UNKNOWN (its page).

**U-A4/3 — "the discount industry was in shakeout" (Business Week, 1962) vs the registrant's own origin
narrative (no distress, deliberate expansion).**
CLAIM A: BW 1962 indexed four failure/bankruptcy/shake-out stories and one industry-level "facing a
major shakeout" statement inside twelve months. CLAIM B: the nine Wal-Mart reports on disk describe the
1962 founding as a planned move (A3, the FY1972→FY1980 retrospective telling repeated in consecutive
reports). WHY THEY DIFFER: different subjects — A is an industry diagnosis made in real time; B is a
company's later account of its own decision. Neither is a factual contradiction about the same variable.
EVIDENCE WEIGHT: A is contemporaneous and third-party; B is retrospective and single-lineage.
BEST-SUPPORTED INTERPRETATION: **both are recorded, and the dataset states that the sector condition in
which the company was founded is independently evidenced while the founding decision itself is not.**
RESIDUAL UNCERTAINTY: whether Wal-Mart's founders read or acted on the shake-out coverage — NO evidence
either way, and no inference is offered. CONFIDENCE: High (that the two claims are of different kinds).

**U-A4/4 — press vs filed figures:** none open yet in this run; the table above is empty of company
figures from the press. Recorded here so the section cannot later be read as "checked and clean".

---

## Data gaps

**EMPTY / UNANSWERED / UNTRIED kept distinct, always.**

### EMPTY (searched, the record is silent, within a stated perimeter)

| Gap | Perimeter of the silence | What would fill it |
|---|---|---|
| Wal-Mart named in Business Week 1962, 1964, 1966, 1969, 1970, 1971 | six BW annual index layers, whole, byte-exact | BW issue text for those years (not on this route), or another periodical |
| Wal-Mart named in any 1962–1969 periodical at all | every item reached so far, incl. the six BW indexes | the *Stores* indexes and monthlies (this run), and the three blocked families |
| Ben Franklin Stores' own print | `creator:("ben franklin stores")` → 0; `title:("ben franklin")…YEAR:[1945 TO 1980]` → 36, all about the Founding Father; only 2 court-docket items | NRDGA circulars/yearbooks outside IA |
| *Chain Store Age*, *Discount Store News*, *Discount Merchandising* **on Internet Archive** | proved five ways by the intake, all 0; `collection:(pub_chain-store-age)` is a collection node with no indexed children | the same blocked-host question below |
| Business Week **issues** 1962–1976 on IA | `identifier:(sim_business-week*)` numFound 1,890; issue scans 1929→c.1961; 1962–1976 index-only; no 1972–1976 | Chronicling/Hathi/Google or paid newsbank |

### UNANSWERED (a route exists, it was reached, it did not give an application-layer reply)

Google Books volume/search API — **HTTP 429 / quota**; HathiTrust — **TLS failure, no HTTP status
exists**; Chronicling America and loc.gov — **HTTP 403 / Cloudflare**; UALR CONTENTdm — **HTTP 403**;
`arkdigitalcollections.org` — **DNS `getaddrinfo failed`, the host may not exist, never cite it**;
thefreelibrary — **HTTP 403**; `archive.org/download/` — **TLS "certificate has expired", 0 bytes**
(use the metadata→server→dir route instead). Each is a statement about **this environment**, not about
Walmart. **The sector's own trade press 1962–1975 is UNANSWERED, not empty** — the intake calls it "the
single biggest hole this pass could not reach", and A4 does not downgrade it.

### UNTRIED (not attempted; recorded so the next pass does not re-burn or mistake it for a null)

* The **Dun & Bradstreet** and **AUDITS & Surveys Co.** discount-store counts the 1962 BW index points at
  (A4-06) — one of the few routes in this whole dossier to a genuine non-company count of the trade.
* The **1963, 1965, 1967, 1968, 1973, 1976–1980** index years: no finding aid for them has been reached.
* `sim_stores_*` **monthly issues 1945–1959 and 1961** (the Newport/Ben-Franklin decade): registered as a
  retrievable class, not one issue read beyond Jan-1960.
* The **Census of Business 1963 / 1967** Arkansas/Missouri/Oklahoma/Kansas/Texas volumes (35 + 131 items,
  `1967censusofbusi674uns` in-set): the "independent count" family in its purest form — a government
  tabulation of retail establishments by state and kind of business, which could bound Wal-Mart's store
  and sales environment for 1963 and 1967 without asking the company. **Text layers are large
  (a probed 1963 volume: 6,620,933 B / item 2.69 GB), so any pull is extract-only.**
* Canada's `31761117266239` DBS "Chain Store Sales and Stocks" — found, out of scope, registered so it is
  not re-burnt.
* Page images of the BW index volumes themselves (would settle U-A4/1 and U-A4/2 in one look).

---

## Provenance ledger

| Source | Type | Primary/Secondary | Event date | Publication date | URL | Tier | Confidence |
|---|---|---|---|---|---|---|---|
| `sim_business-week_1962_index` | SIM microfilm annual index, full text layer | Primary (periodical's own apparatus) | 1962 | 1963 | `https://ia802906.us.archive.org/14/items/sim_business-week_1962_index/sim_business-week_1962_index_djvu.txt` | 2 | High (existence), Medium→High (as read) |
| `sim_business-week_1964_index_0` | same | Primary | 1964 | 1965 | `https://ia902902.us.archive.org/33/items/sim_business-week_1964_index_0/sim_business-week_1964_index_0_djvu.txt` | 2 | High |
| `sim_business-week_1966_index_0` | same | Primary | 1966 | 1967 | `https://ia800606.us.archive.org/17/items/sim_business-week_1966_index_0/sim_business-week_1966_index_0_djvu.txt` | 2 | Medium (OCR loss) |
| `sim_business-week_1969_index_0` | same | Primary | 1969 | 1970 | `https://ia800408.us.archive.org/25/items/sim_business-week_1969_index_0/sim_business-week_1969_index_0_djvu.txt` | 2 | High |
| `sim_business-week_1970_index_0` | same | Primary | 1970 | 1971 | `https://ia800500.us.archive.org/31/items/sim_business-week_1970_index_0/sim_business-week_1970_index_0_djvu.txt` | 2 | High |
| `sim_business-week_1971_index_0` | same | Primary | 1971 | 1972 | `https://ia800908.us.archive.org/33/items/sim_business-week_1971_index_0/sim_business-week_1971_index_0_djvu.txt` | 2 | High |
| `sim_stores_1960-01_42_1` | *Stores* (NRDGA) monthly issue | Primary (trade press) | 1960-01 | 1960 | metadata→server→dir `_djvu.txt` route | 3 (1 for knowability) | High (269,490 B, 38,238 words) |
| `sim_stores_1970_52_index`, `_1974_56_index`, `_1975_57_index` | *Stores* annual indexes | Primary | 1970/1974/1975 | 1971/1975/1976 | metadata→server→dir | 3 (1 for knowability) | High (16,985 / 24,487 / 18,054 B) |
| intake extract `BUSINESSWEEK_INDEX_1964-1971_EXTRACT_discount_retail.txt` (44,966 B, ~6,500 words) | bounded extract with provenance header | Secondary (derived from the six layers above) | 1962–1971 | 2026-09-25 | `00_universe/harvest/periodicals_intake/walmart_variety_sector/` | — | High as transcription; re-walked by A4 where cited |
| intake extract `STORES_NRDGA_1960-1975_EXTRACT_discount_variety.txt` (8,017 B) | bounded extract | Secondary | 1960–1975 | 2026-09-25 | same directory | — | High as transcription |
| `_REQUEST_LEDGER.tsv` (100 rows: timestamp · status · bytes · URL · note) | retrieval proof | Secondary | 2026-09-25 | 2026-09-25 | same directory | — | High |
| `WALMART_AR_1972…1980.txt` (nine files) | registrant corporate print | Primary, **one lineage** | FY1972–FY1980 | 1972-03-22 → 1980-04-01 | `company_002_walmart/sources/periodicals/` | 1 | High as to content; capped by single-lineage rule |

**A4 request ledger (this run, appended as spent — 60 hard cap):** *(rows appended below during the run;
the count in `## Working method and request budget` is kept in step with this list).*

---

## Depth-verdict assessment

**The question §14 rule 6 asks:** is the Walmart Stage-1 record still one voice? A3 §7.2(c) states the
count of independent lineages in the financial record is **1**, that nine consecutive fiscal years sit on
the registrant's own reports plus its auditor's opinions, and that "no number of further years of
Wal-Mart's own annual reports can move this verdict; only a different publisher can."

**A4's answer so far, stated conservatively and before the *Stores* greps land:**

1. **Family 3 (periodical corpora) has moved from UNANSWERED-never-tried to PARTIALLY POSITIVE.** Six
   Business Week annual indexes and a 205-issue *Stores* run with text layers are now in hand, dated,
   paginated and byte-verified. That is a different publisher and a different lineage from the
   registrant, and it is contemporaneous — which is exactly what §14 rule 6 says is missing.
2. **It does not yet move the company-level verdict, for one specific reason:** no item recovered so far
   **names Wal-Mart**. The independent-lineage count for the *financial* register is therefore still 1.
   What A4 adds is a **second, independent lineage for the market-state layer (§H/§I)** — Business Week's
   sector coverage of 1962–1971 is Tier-1 evidence for "what was publicly known and when", and it is not
   derivative of anything the company filed.
3. **The count A4 can honestly claim is: 2 independent lineages present in the corpus** (registrant+
   auditor; Business Week periodical), **with the second carrying zero company-naming records so far.**
   A verdict of `DEPTH-CORE` on that basis would be a category error; the correct statement remains
   A3's: **"the register is deep and the record is one voice"** — amended to "…and the sector around it
   is now independently evidenced."
4. **What would move it, in priority order:** (a) a *Stores* index entry or article naming Wal-Mart /
   Wal-Mart Stores in 1970–1975; (b) a *Stores* issue naming **Walton's** in Newport, Kentucky 1945–1950 —
   which would put an independent witness **before** 1972-03-22, currently the earliest dated witness of
   any kind in the corpus (A3 Data gaps: "No witness of any kind dated before 1972-03-22"); (c) the
   Census of Business 1963/1967 Arkansas establishment counts, which bound the company's environment
   without asking it.
5. **What keeps it provisional even if all three succeed:** the sector's own trade press (*Chain Store
   Age*, *Discount Store News*, *Discount Merchandising*) remains UNANSWERED because three host families
   are bot-blocked from this machine; the article TEXT behind every Business Week index entry remains
   unreachable for 1962–1976 on IA; and every FY1962–FY1967 financial line remains EMPTY in the
   registrant's own series, which no periodical can retroactively fill.

---

## Outbound corrections

**Reported only. No prior file was edited by this run** (§14 rule 4). Format as in A3: named prior
record, what A4 establishes, action the merge must take.

**COR-A4-01 — A3 §7.1 family-3 row and §7.2(c) must be amended: "UNCHANGED … not one word of
third-party contemporaneous text entered the corpus" is now superseded for the corpus as a whole.** A3
was correct at its writing (it downloaded only corporate print). A4 now places six Business Week annual
indexes (1962/64/66/69/70/71, ~5.18 MB of printed index matter) and the 205-issue *Stores* 1945–1961 run
on the record. **Action:** merge re-states family 3 as **PARTIALLY POSITIVE (periodical indexes and one
trade serial retrieved; no company-naming record yet)** and keeps the **independent-lineage count for the
financial register at 1**, which is unchanged. Do not let the amendment be read as a verdict upgrade.

**COR-A4-02 — A3 §7.2(d) names the missing witness as a *Chain Store Age* directory, a D&B/Hoover's
report, or local dailies. The Business Week 1962 index independently points at two of them.** A4-06
records `Dun & Bradstreet reports on number of disc[ount stores]…` and `AUDITS & Surveys Co. — Data on
discount stores…` as indexed 1962 items. **Action:** merge adds D-and-B discount-store counts to the
named-witness list as **documented-to-exist-in-1962, UNTRIED as a text**, and cites the 1962 index entry
as the pointer, so the next agent does not have to rediscover it.

**COR-A4-03 — A3 Data gaps, "No witness of any kind dated before 1972-03-22" is correct for the corpus
A3 held, and is now the specific target A4 states it will test.** The *Stores* run covers 1945–1961
monthly with text layers; a Newport-era hit would break the line. **Action:** do not delete A3's row —
A3's statement is true of the documents it mined; merge marks it "standing; under active test in A4"
and updates only after A4's greps are recorded.

**COR-A4-04 — the intake's `_MANIFEST.md` §3 Target 1 row for `walmart_variety_sector` warns that the
extract filename says 1964–1971 while the file also carries 1962 + 1966 (retained, not renamed, per
rule 4). A4's citations therefore cite the file plus the line/offset range, never the filename as a date
claim.** **Action:** any register row citing that extract must carry the internal year-block header
(`### BUSINESS WEEK 1962 INDEX …`) with its line offsets, so the reference survives a rename.

**COR-A4-05 — decoy warning for the harvest queries.** `q_05bcf478`-style searches and any future
"Walton" query hit `WALTON, William / Holiday Inns` (BW 1962 index p.47, Jul.14) and `H. C. Walton`
(BW 1970 index p.4, Aug.29). A2's W-54 family and the fleet's Chronicling queries already contain one
known state error (U-A2/7: "waltons newport **mo**" — wrong state; Newport is **Kentucky**).
**Action:** merge propagates both traps to `queries.json` known-traps and to A2's outbound list.

---

## CSV append rows

Schemas copied verbatim from `company_001_amazon/*.csv` headers (see the read-back at the foot of this
section). Every field containing a comma is double-quoted; dates ISO, partial where the evidence is
partial; `UNKNOWN` used as a value, empty cells forbidden. Rows are append-only and carry `A4-nn`
`claim_ref`s so the merge can find them.

*(Rows appended after each mined issue; the header blocks are printed once, the row blocks grow.)*
