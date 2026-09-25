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

**Web budget: hard cap 60. SPENT: 42 of 60, all sequential, `2.6 s` delay, TLS verification ON, UA
`FoundersPlaybook-A4-walmart-periodicals/1.0 (research@example.org)`.** Outcome mix: **41 × HTTP 200,
1 × read-timeout ERR (first `sim_business-week_1964_index_0` attempt; the item was subsequently pulled
successfully by a separately planned re-walk — no blind retry), 0 × 429, 0 × 503, 0 back-off events,
0 hosts halted, 18 requests left unspent.** Composition: **5** `advancedsearch.php` queries · **16**
`metadata/<id>` calls · **16** text-layer GETs through the metadata→server→dir route · **5** `REWALK` GETs
straight to the intake's documented server URLs. **10,015,606 bytes (~10.0 MB)** of periodical text
received into an OS scratch directory outside the repository across 18 distinct hosts
(`archive.org` + 17 `ia6*/ia8*/ia9*.us.archive.org` item servers); **~90 KB of bounded extract written into
the repository** across two files (`BUSINESSWEEK_INDEX_1962-1971_EXTRACT_walmart_and_sector_hits.txt`
47,277 B / 6,756 words; `STORES_NRDGA_1946-1972_EXTRACT_walton_and_discount.txt` 42,857 B / 5,821 words),
both an order of magnitude under the 60,000-word line. Every request is one row of the A4 scratch
`REQUEST_LEDGER.tsv` (utc · status · bytes · url · note), and the per-item HTTP status, byte count, URL and
timestamp are copied into the extract headers so a reader can re-walk without re-fetching.
**One retrieval inefficiency disclosed:** the 1964 and 1970 re-walks were issued by two overlapping
processes, costing 3 duplicate requests (visible as repeated rows in the ledger). Nothing was
blind-retried after a rate signal; the duplicates were concurrent planning, and they are reported rather
than hidden.
**Budget deliberately left unspent (18):** Chronicling America / HathiTrust / Google Books are blocked from
this machine and would return the same 403 / TLS failure / 429 that the intake and `B_periodical_retest.md`
already recorded, so they are logged UNANSWERED rather than re-burnt; and the page images (`_text.pdf`) of
the *Stores* and index volumes were not pulled. Both recorded as UNTRIED, never as nulls (§14 rule 6).

**Retrieval log, in order** (so a later agent can skip what is now settled): BW index-year enumeration
(→ 81 items, years 1951–1971, including the 1963/1965/1967/1968 volumes and the half-year siblings the
intake had not reached) · *Stores* 1962–1980 enumeration (→ 5 index volumes: 1970, 1971, 1972, 1974, 1975) ·
*Stores* 1945–1961 enumeration (→ numFound 200 monthlies, each with a text layer) · *Stores* 1971 and 1972
indexes fetched and grepped · BW 1962, 1964, 1970, 1963, 1965, 1967, 1968 volumes fetched whole and grepped ·
*Stores* monthlies 1950, 1951, 1955, 1958, 1961-03, 1961-12, 1946 fetched whole and grepped · BW 1963-H2,
1965-H1, 1967-H2 fetched, closing the three half-year gaps (3 × metadata + 3 × layer) · NRMA-directory and
discount-trade recheck searches (A4-41).

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
Conf: **High — upgraded by A4's own re-walk (R1: 1,273,570 B received = declared, 196,549 words read
whole, `wal-mart` 0 / `walton` 1 decoy / `arkansas` 1 gas company / `rogers` 4 persons and one cartage
firm / `ben franklin` 0 / `discount` 88; see A4-17)** —
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
passages are A4-01…A4-14) — Conf: **High for the seven volumes A4 re-walked whole (1962, 1963 both halves,
1964, 1965 both halves, 1967 both halves, 1968, 1970) and Medium-to-High for the three the intake pulled
byte-exact (1966, 1969, 1971) — see A4-17, A4-30** —
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
independent visibility to this franchisee at the close of his first five-and-a-half years.** Date: 1950-06 —
Source: `sim_stores_1950-06_32_6` — Source date: 1950-06 — URL: metadata→server→dir route —
Archived: A4 scratch; extract to `../sources/periodicals/STORES_NRDGA_1946-1972_EXTRACT_walton_and_discount.txt` —
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

A4-41 Claim: **The directory/yearbook family — the genre that would carry a membership roster and so name a
small franchisee — is absent from this corpus, searched two more ways by A4: NRMA-titled search
(`title:("yearbook of the national retail") OR title:("national retail merchants association") OR
creator:("national retail merchants association")`) returns numFound 10, every one a manual or handbook
("The buyer's manual" 1965/1979, "NRMA's standard classifications" 1967, "Retailers' guide to shopping
center leasing" 1977, "How to write better retail advertising copy" 1961) and **no membership list**; and
the discount-trade recheck (`identifier:(sim_discount*) OR title:("discount store news") OR
title:("discount merchandising")`) returns numFound 16, all microfilm year-records outside the window.**
Date: search run 2026-09-25 against holdings 1921–1987 — Source: `archive.org/advancedsearch.php` two
queries (HTTP 200 each) — Source date: as returned — URL: ledger rows 49–50 — Archived: A4 scratch,
selected fields only — Tier: — Class: FACT (as to Internet Archive's holdings) / **NOT a null as to the
literature** — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High (that IA holds no NRDGA/NRMA roster in
this family) — Corroboration: 2 query forms by A4 + the intake's 3 (Chain Store Age EMPTY five ways,
Discount Store News 16 microfilm rows, "chain statistical" yearbook → 1 irrelevant hit) —
Conflicts: none. **Consequence, stated for the merge: the one class of periodical document that could
have named Walton's independently — a trade directory — is not reachable from this machine, so the
pre-1972 named witness cannot be obtained from the corpus that is currently unblocked.**

A4-42 Claim: **Business Week's index matter is a *duplicating* apparatus, and the same headline can be
indexed under several subjects with different page readings; A4 therefore treats an index volume's
"full year" as covering only the blocks that OCR legibly.** Date: 1962–1971 — Source: seven re-walked
layers, e.g. 1964 "Woolworth branches out into mass merchandising" printed 5× (offsets 37549 / 38625 /
51331 / 59275 / 66309) and the 1962 Grayson-Robinson story as `p109` / `pl109` / `pl169` —
Source date: as bound — URL: as A4-30 — Archived: extract file — Tier: 2 — Class: FACT (counts and
offsets) — Passage: "Woolworth branches out into mass merchan-dising in varied lines (with cover and
illus) p58, Nov.14" — Conf: High — Corroboration: 1 publisher — Conflicts: **U-A4/1**.

---

### Numbering note (declare, do not destroy)

**A4-37, A4-38, A4-39 and A4-40 carry no record and are reserved.** They were drafted during an
intermediate append that covered the December 1961 seminar issue and the June 1946 issue separately; that
material was consolidated into **A4-36** (all four December 1961 passages, with raw offsets) and into
**A4-23/A4-29** for the pre-1972 null before this file reached its present form. The IDs are not reused
anywhere in this dossier, so any downstream citation to A4-37…A4-40 resolves to **A4-36** and is not
evidence of a lost record. Nothing was deleted to create the gap (§14 rule 7: one writer's two passes over
one file are declared here rather than silently renumbered).

**Total records on disk: 38** (A4-01…A4-36, A4-41, A4-42), plus 7 re-walk rows R1–R7 inside the
`A4-re-01 … A4-re-16` block, plus 7 contradictions U-A4/1…U-A4/7.

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
| 1963 | BW `sim_business-week_1963_index` (Jan–Jun) **+** `…_july-december-1963_index` (the missing half, **closed by A4**: 633,645 B EXACT, 99,760 words) | **NO** | **EMPTY within BW — FULL YEAR now** | Both halves `wal-mart` 0. The Jul–Dec half is the richest sector volume in the dossier: $6.9-billion 1962 discount sales (p.132 Jul.13), a Dun & Bradstreet discount-store survey (p.79 Nov.9), and "Fewer stores to share the pie … chains squeeze 'little guys'" (p.182 Nov.16) — A4-31, A4-32. Its 10 `arkansas` hits are school-desegregation stories, and `walton` 1 = William B. Walton, travelers' standards (A4-33). |
| 1964 | BW 1964 index, **re-walked whole by A4** (203,895 words) | **NO** | **EMPTY within BW — full year** | "Small town greets the discounters" p.90 Oct.3 resolved to **ALDENS, Inc.** — a competitor, not us (A4-20). `variety store` 2, `woolworth` 6, `discount` 40. |
| 1965 | BW `sim_business-week_1965_index` (Jul–Dec) **+** `…_january-june-1965_index` (**half closed by A4**: 637,923 B EXACT, 100,903 words) | **NO** | **EMPTY within BW — FULL YEAR now** | H1 `discount` 22 carries "Is success spoiling discount stores?" (p.97 Jun.2) and "Is the franchise system legal" (p.66 Apr.3) — A4-34. `walton` 0 in both halves; `arkansas` 1 = a Hughes Aircraft station. |
| 1966 | BW 1966 index (intake-retrieved, byte-exact 1,177,551 B; not re-walked by A4) | **NO** | EMPTY within BW — full year | `DISCOUNT Houses` block OCR-lost (A4-14): the EMPTY covers the legible blocks, not the whole volume. |
| 1967 | BW `sim_business-week_1967_index` (Jan–Jun) **+** `…_july-december-1967_index-contents` (**half closed by A4**: 556,337 B EXACT, 88,978 words) | **NO** | **EMPTY within BW — FULL YEAR now** | `discount` 10 (H1) + 15 (H2). H2's 4 `small town` hits are the J&L Steel "Helping a small town cope with prosperity" story, p.184 Sep.23 — a fourth decoy (A4-35). `walton` 0, `arkansas` 3 = the Arkansas River barge project (A4-22). |
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

**Tally, final.** Years with an independent witness **naming** Wal-Mart: **0 of 19 (1962–1980)**.
Years whose absence is a *searched, full-year, company-sequence* EMPTY: **1962, 1963, 1964, 1965, 1967,
1968, 1970** — Business Week, all seven read whole by A4 (1963, 1965 and 1967 only after A4 retrieved the
missing half-volumes) — plus **1966 and 1969** (intake-retrieved byte-exact, full year) and **1971**
(intake). **Ten consecutive years, 1962–1971, `wal-mart` = 0 in every one.**
Years whose absence rests on a **subject-only trade index** (weaker instrument, A4-18): 1970, 1971, 1972,
1974, 1975 (*Stores* annual indexes; 1971 and 1972 fetched by A4).
Years with **no finding aid reached at all**: 1973, 1976, 1977, 1978, 1979, 1980.
*Stores* **monthly** issues read whole by A4: 1946-06, 1950-06, 1951-06, 1955-06, 1958-06, 1961-03,
1961-12 — 7 of ~200 in the 1945–1961 run; `walton` 0, `wal-mart` 0, `ben franklin` 0 in all seven;
**193 issues UNTRIED**.

**The pre-1972 question, answered as far as this route can answer it.** The best periodical chance this
project has for a witness dated before 1972-03-22 was the *Stores* monthly run covering the Newport and
Bentonville decades. Seven issues spread across 1946–1961 produce no name. The reason is genre, not luck
(A4-29): *Stores* is a management-and-policy journal whose issues name officers, committees and large member
chains, while a small Arkansas/Kentucky franchisee would surface only in a membership roster or chain
directory — and the NRDGA/NRMA directory-yearbook family is **not in this corpus** (A4-41). The pre-1972
periodical result is therefore stated as **a genre-limited EMPTY plus one absent family**, never as proof
that no contemporaneous print named Walton's.

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
5. **1960 and 1958 (*Stores*, NRDGA/NRMA): the association's own journal carried a presidential editorial
   on the mandatory functional-discount bills (Jan 1960) and, in June 1958, a survey of its member stores
   reporting that "the spread of discount houses over the country is slowing down" — 28% of stores seeing
   more discount houses in their communities, 6% fewer, 66% no change.**
6. **1963, second half (Business Week): the trade's own arithmetic appears, dated and paginated — discount
   stores' 1962 sales put at $6.9 billion (p.132, Jul.13), a Dun & Bradstreet survey of discount-store
   department profitability (p.79, Nov.9), and the structural verdict "Fewer stores to share the pie: They
   get bigger but decrease in number as discounters, chains squeeze 'little guys'" (p.182, Nov.16).**
   This is the single most consequential market-state finding of A4: **one year after Wal-Mart's founding,
   the independent press was reporting a *shrinking number* of discount stores.** It is a sector statement,
   not a company statement, and it does not describe Wal-Mart.
7. **1965 (Business Week): self-doubt inside the sector — "Is success spoiling discount stores? Moves to
   carry more costly merchandise worry industry leaders" (p.97, Jun.2) — alongside a Supreme Court
   franchise-law question (p.66, Apr.3) that touches the Ben Franklin form directly.**
8. **December 1961 (*Stores*, the month before the first Wal-Mart opened): NRMA ran its first Discount
   Seminar as a formal programme — "Is It for You?", sessions on low-margin mass retailing, leasing,
   financing, buying offices, whether a food department is essential — with a stated attendance of about
   800, half of them conventional department-store representatives; a published hard-goods discount markup
   of 26 to 28 per cent; a consultant's warning of "a serious 'over-concentration' of discount stores"; a
   store-size-to-trading-area table; and **S. E. Nichols Company as a variety-store operator already
   running "Nichols Discount Cities since 1958"**. The trade had already formalised the exact transition
   the registrant's own narrative later presents as its own venture, three months before that venture
   opened. That is Tier-1 evidence for §H: **this is what was publicly knowable, in the company's own
   franchise association, at the moment of founding.**
9. **What is NOT in the sector evidence, and must not be inferred from it:** no Business Week index volume
   1962–1971 and no *Stores* item read in this run names Wal-Mart, Bentonville, Springdale or Rogers,
   Arkansas. The sector was newsworthy; the participant was not.

**Coda (§7 interpretive-duty check).** Evidence: the ten Business Week index/half-index volumes (13 layers,
~1.06 M words read whole, ~10.0 MB received, every byte count matched to the item's declared size) and
nine *Stores* items, all with offsets in the two extract files. Mechanism: an index is published by a
periodical about its own output, and a trade journal's seminar report is published by the association for
its members, so both are dated, checkable statements of attention — which is precisely the evidence a
market-as-knowable section (§H) is allowed to use, and the reason these items are Tier-1 for knowability
while remaining Tier-2/3 for company facts. Alternative explanations, kept live and not dismissed:
(a) the company may have been covered by titles no reachable host indexes — *Chain Store Age*,
*Discount Store News*, *Discount Merchandising*, all EMPTY-for-Internet-Archive and therefore UNANSWERED
as to content; (b) the press silence may reflect only Business Week's editorial selection, and *Stores*'
silence its subject-only index apparatus plus the loss risk of microfilm OCR; (c) an unindexed column or
brief may have carried the name without ever entering the finding aid. Confidence: **High** that BW covered
the sector as described across ten years; **High** that BW's indexes do not name the company in 1962–1971;
**Medium** that this is a fair picture of total press attention; **Medium** that *Stores* 1946–1961's seven
sampled issues are representative of the run, since they are not (193 issues UNTRIED).

---

## Independent figures vs registrant figures

**Rule: both sides stay. A press figure that disagrees with the filed figure opens a contradiction; it is
never reconciled silently, and never substituted.**

| Metric | Press value + citation (independent of the registrant) | Filed value + document (registrant) | Difference / status |
|---|---|---|---|
| Discount-store sales, calendar 1962 | **$6.9 billion** — Business Week short news item, p.132, Jul.13 1963 (`sim_business-week_business-week_july-december-1963_index`, `DISCOUNT Houses` block @180,304) | NO FILED VALUE — FY1962 is EMPTY in all nine reports (A3 §Data gaps) | **Press-internal difference, not press-vs-filed:** BW's own Dec.1 1962 lead called it "a fast-growing $6-billion industry" (p.78) while the Jul.13 1963 item prints $6.9 billion for 1962. Both kept; **U-A4/5**. Definitions of the industry are in neither reachable text. |
| Discount-industry character, 1962 | "Fast-growing … facing a major shakeout" — BW p.78, Dec.1 1962 | NO FILED VALUE | Sector statement; no company counterpart exists. Kept as market-state (§H). |
| Number of discount stores, 1963 | **"They get bigger but decrease in number as discounters, chains squeeze 'little guys'"** — BW p.182, Nov.16 1963 | Registrant's own store count rises 51 (FY1971) → 64 (FY1973) → 78 (FY1974), from its own reports (A3 Table S1/S3) | **Different universes; NOT reconciled and NOT a contradiction of arithmetic — but a real tension, recorded as U-A4/6**: the industry's unit count was contracting in the press while the company's was expanding, and nothing in this corpus says which of the two the founder could observe. |
| Discount-store department profitability, 1963 | A **Dun & Bradstreet survey** "shows that … and television are the most profitable departments in a sampling of discount stores" — BW p.79, Nov.9 1963 (one department name lost to OCR) | Registrant prints no department-profitability comparison | The D&B volume itself is **UNTRIED**; this row exists to mark the genre as documented-to-exist, dated, and not yet in hand. |
| Variety-store trade's penetration of discounting, 1958 | **28 % of member stores reported more discount houses in their communities, 6 % fewer, 66 % no change** — *Stores*, June 1958, offsets 32,746 / 32,858 (`sim_stores_1958-06_40_6`) | NO FILED VALUE — the company had no public report in 1958 | Sector measurement, four years before founding. Respondent universe not disclosed in the passage; **UNTRIED**. |
| Trade-body scale, Dec 1961 | NRMA "membership covers over 11,500 retail establishments with a combined annual sales of over $19 billion" — *Stores* Dec 1961 @13,749 | Registrant: FY1968 24 stores / $12,618,754; FY1972 51 stores / $78,014,164 (A3) | **Label discipline required:** $19 billion is an association MEMBERSHIP aggregate, not the discount industry and not a market denominator. Wal-Mart's share of it is deliberately **not computed** here. |
| Competitor unit economics, Dec 1961 | American Dixie Shops (Tumpowsky): "more than 40 departments in discount stores", volume "will hit $30 million next year", $100,000–$150,000 inventory per 8,000–10,000 sq ft leased department aiming at $1–1.5 million sales; hard-goods discount markup **26 to 28 per cent** — *Stores* Dec 1961 @74,633 / @75,78 (raw offsets) | Registrant's FY1977 report prints Wal-Mart store sizes 30,000–60,000 sq ft, average ≈42,000, and gross margin 26.11 → 26.34 % (FY1976→FY1977) | **A genuine comparator, and it disagrees in kind:** the press figure is a *leased-department operator's* markup on a store-within-a-store model; the filed figure is a *whole-store* gross margin. They are not the same measure and must not be subtracted. Recorded as an UNANSWERED comparison (U-A4/7 mechanism note), not as a conflict. |
| Store size vs trading-area population, Dec 1961 | A sizing table pairing 30,000 sq ft with a trading area "Under 100,000" up to "Over 150,000" with "multi-million" — *Stores* Dec 1961 @84,160 | Registrant: first Discount City in Rogers, "then a town of approximately 4700" (FY1975) / "approximately 5,000 people" (FY1978); communities served 5,000–25,000 (FY1978) | **U-A4/7 — a real divergence, unresolvable from this layer:** the printed table's column pairing is OCR-damaged, so the rule cannot be stated precisely; the registrant's own town-size figures (A3 U-A3/8) are themselves a range. Both sides kept, neither adjudicated. |
| Wal-Mart named in ANY press figure, 1962–1980 | **UNKNOWN — no figure recovered** in ten Business Week index years, five *Stores* annual indexes and nine *Stores* monthly items | A3's nine contemporaneous reports | **The decisive empty row.** The company's own numbers exist; no independent publication in hand carries any of them. |

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

**U-A4/4 — press vs filed figures:** **still none, and that is the finding.** No periodical reached in this
run carries a Wal-Mart figure at all, so no company figure can be cross-checked; the rows that do exist in
§"Independent figures vs registrant figures" are sector and comparator figures. RESIDUAL UNCERTAINTY: high,
and it is exactly the uncertainty A3 §7.2(c) named. CONFIDENCE: High (that the row is empty).

**U-A4/5 — the size of the discount industry in 1962: $6 billion or $6.9 billion.**
CLAIM A: "Discounters strive to ride out storm: Fast-growing $6-billion industry is facing a major
shakeout", Business Week p.78, Dec.1 1962. CLAIM B: an indexed short item of Business Week p.132, Jul.13
1963 printing "[discount] stores amounted to $6.9 / billion in 1962". WHY THEY DIFFER: A is a rounded
characterisation published *during* 1962 with no stated universe; B is a specific figure for the completed
year published seven months later, and the layer's column reflow splits the sentence so the subject noun
and the source attribution are lost. EVIDENCE WEIGHT: both are Business Week, both Tier-2, both
index-level; **neither can be checked against article text, which does not exist on this route.**
BEST-SUPPORTED INTERPRETATION: **$6.9 billion as the figure for calendar 1962 discount-store sales as the
weekly later reported it, with $6 billion recorded as the contemporaneous December 1962 characterisation —
and both printed, neither chosen.** RESIDUAL UNCERTAINTY: the industry definition behind each number
(establishments? lines of merchandise? including food discounters?) is UNKNOWN and unrecoverable here; the
difference is 15 % of the figure, which is large enough that any share calculation built on either must
carry the ambiguity. CONFIDENCE: Medium (that both figures were published), UNKNOWN (as to what either
measured). **Register effect: neither figure may be used as a denominator for a "Wal-Mart's share of the
industry" metric.**

**U-A4/6 — the industry's store count was falling while the company's rose.**
CLAIM A: Business Week, "Fewer stores to share the pie: They get bigger but decrease in number as
discounters, chains squeeze 'little guys'", p.182, Nov.16 1963 (headline as indexed). CLAIM B: the
registrant's own series — 51 stores FY1971, 64 FY1973, 78 FY1974 (`WALMART_AR_1974.txt` Five Year Progress
Report; A3 Table S1/S3). WHY THEY DIFFER: A counts *discount-store operators in the trade* and is a
journalistic headline whose numbers are in the unreachable article; B counts Wal-Mart's own units in an
audited filing. They are different universes measured by different instruments. EVIDENCE WEIGHT: B is
Tier-1 and auditor-attested; A is Tier-2 index-level, and its numeric content is NOT in hand.
BEST-SUPPORTED INTERPRETATION: **both stand; the dataset records that the sector Wal-Mart entered was being
described as consolidating away from small operators, while the company's own count grew, and it refuses to
explain the gap.** RESIDUAL UNCERTAINTY: **the mechanism is the whole question and it is unanswered** —
whether Wal-Mart was inside the "chains squeezing little guys" class, outside it, or irrelevant to it in
1963 cannot be determined from a two-store company's own later account plus one headline. Whether any
contemporaneous observer, including Walton, could have read that headline as an opportunity or as a warning
is UNKNOWN and no inference is offered. CONFIDENCE: High (that both claims exist), UNKNOWN (as to any
causal relation).

**U-A4/7 — the trade's published sizing rule vs the registrant's account of its own first store.**
CLAIM A: *Stores*, December 1961, reporting NRMA's Discount Seminar: a store-size-to-trading-area table
pairing 30,000 sq ft with a trading area "Under 100,000" and rising to "Over 150,000 … Multi-million",
with the same consultant warning of "a serious 'over-concentration' of discount stores" (offsets 84,160 /
84,355). CLAIM B: the registrant's own reports — the first Wal-Mart Discount City opened in Rogers,
Arkansas, "then a town of approximately 4700" (FY1975 report) / "approximately 5,000 people" (FY1978
report), and store sizes given later as 30,000–60,000 sq ft, average ≈42,000, in communities of
5,000–25,000. WHY THEY DIFFER: A is trade guidance addressed to conventional department stores considering
a discount venture; B is a self-report about a store actually built. EVIDENCE WEIGHT: A is third-party,
dated three months before the opening, but its table is **OCR-damaged and the column pairing is not
settleable from the layer**; B is Tier-1 audited print but retrospective about 1962, and its own two
population figures disagree with each other (that is A3's U-A3/8). BEST-SUPPORTED INTERPRETATION:
**recorded as an unresolved divergence, not as proof that the trade's advice was wrong or that the founder
ignored it.** If A's smallest bracket means "a 30,000 sq ft store belongs where the trading area is *up to*
100,000", a 4,700-person Rogers sits inside the rule's outer limit; if it means "at least", Rogers violates
it. The layer cannot tell us which, and the seminar's own text is not reachable. RESIDUAL UNCERTAINTY:
the pairing direction of the table, the definition of "trading area" (town vs trade radius), and whether any
Walton attended or read NRMA material at all — **all UNKNOWN; no evidence connects the founder to this
seminar.** CONFIDENCE: Medium (that the two texts diverge), UNKNOWN (as to which reading of A is correct).
**This is the closest this dossier comes to an independent check on the founding decision, and it is a
check that cannot be closed from index-and-OCR evidence alone — logged as RESEARCH DEBT under §10.**

---

## Data gaps

**EMPTY / UNANSWERED / UNTRIED kept distinct, always.**

### EMPTY (searched, the record is silent, within a stated perimeter)

| Gap | Perimeter of the silence | What would fill it |
|---|---|---|
| **Wal-Mart named in Business Week, every month 1962–1971** | ten index years / 13 half-and-full volumes: 7 read whole by A4 (1962, 1963 both halves, 1964, 1965 both halves, 1967 both halves, 1968, 1970), 3 read whole by the intake byte-exact (1966, 1969, 1971). `wal-mart` 0 and `walmart` 0 in all | BW **issue** text for those years (IA holds issue scans only to c.1961), or another publisher |
| **Wal-Mart named in *Stores*, 1970–1975** | all five annual indexes that exist on IA (1970, 1971, 1972, 1974, 1975); 1971/1972 fetched by A4 | *Stores* **issue** scans for those years — they do not exist on this route (the monthly run stops at 1961), so this is EMPTY within IA holdings only |
| **Walton's / Ben Franklin named in the variety trade, 1945–1961** | 7 of ~200 monthly issues read (1946, 1950, 1951, 1955, 1958, 1961-03, 1961-12), plus the intake's 1960-01: `walton` 0, `wal-mart` 0, `ben franklin` 0, `bentonville` 0, `springdale` 0 | the remaining 193 issues are UNTRIED; the genre that would actually name a member store — NRDGA/NRMA **membership roster or chain directory** — is absent from this corpus (A4-41) |
| **Any press figure for the company, any year, 1962–1980** | every item read in this run | nothing in the reachable corpus; see §Independent figures, final row |
| Ben Franklin Stores' own print | `creator:("ben franklin stores")` → 0; `title:("ben franklin")…1945–1980` → 36, all the Founding Father; 2 court-docket items only (intake §3) | NRDGA circulars/yearbooks held elsewhere |
| *Chain Store Age*, *Discount Store News*, *Discount Merchandising* **on Internet Archive** | proved five ways EMPTY by the intake; re-checked twice more by A4 (A4-41: all `sim_discount*` → 16 microfilm year-records outside the window; NRMA-titled → 10 items, **no roster**) | the three blocked hosts (below) |
| Business Week **issues** 1962–1976 on IA | `sim_business-week*` family numFound 1,890; issue scans 1929→c.1961; 1962–1976 index volumes only; nothing 1972–1976 | another holder (HathiTrust/Google/newsbank) |
| Bentonville / Benton County, Arkansas local print on IA | `title:(bentonville) OR title:("benton county")` → numFound 453, and the first 40 are 1854–1895 county histories, atlases and a Civil War battle — **no newspaper back-file, no 20th-century local press** | Chronicling America (403-blocked), which is where those dailies would be |
| Trade serial with "variety store" in the title on the SIM route | `identifier:(sim_*) AND title:("variety store")` → **0** | nothing on this host |

### UNANSWERED (a route exists, it was reached, it did not give an application-layer reply)

Google Books volume/search API — **HTTP 429 / quota**; HathiTrust — **TLS failure, no HTTP status
exists**; Chronicling America and loc.gov — **HTTP 403 / Cloudflare**; UALR CONTENTdm — **HTTP 403**;
`arkdigitalcollections.org` — **DNS `getaddrinfo failed`, the host may not exist, never cite it**;
thefreelibrary — **HTTP 403**; `archive.org/download/` — **TLS "certificate has expired", 0 bytes**
(use the metadata→server→dir route instead). Each is a statement about **this environment**, not about
Walmart. **The sector's own trade press 1962–1975 is UNANSWERED, not empty** — the intake calls it "the
single biggest hole this pass could not reach", and A4 does not downgrade it.

### UNTRIED (not attempted; recorded so the next pass does not re-burn or mistake it for a null)

* **Dun & Bradstreet's own discount-store volumes** — the genre is now *dated* by A4 (BW indexes a D&B
  discount-store survey at p.79, Nov.9 1963, and the 1962 index points at "Dun & Bradstreet reports on
  number of disc[ount stores]…"), but **no D&B volume has been retrieved**. This is the nearest thing in
  hand to A3 §7.2(d)'s missing witness, as a count *of the trade* rather than of the company.
* **AUDITS & Surveys Co.** discount-store data (BW 1962 index, A4-06) — object unread.
* **The other 193 *Stores* monthly issues, 1945–1961**, and specifically the numbers that would carry a
  roster or territory column (convention issues, May/June numbers, the "membership" divisions' reports) —
  2 requests each; a designed sample of ~10 is the right next act, not a sweep.
* **Census of Business 1963 / 1967** for Arkansas, Missouri, Oklahoma, Kansas, Texas (35 + 131 items,
  `1967censusofbusi674uns` in-set): a government tabulation of retail establishments by state and kind of
  business that could bound the company's environment without asking the company. Layers are large (a
  probed 1963 volume: 6,620,933 B text / item 2.69 GB) → **extract-only, never dumped**.
* **`hf-5465.-u-55-g-7`** — "Shopper attitudes and trade areas for discount stores in Greensboro, North
  Carolina", D. Gordon Bennett / Greensboro Chamber of Commerce, 1970 (metadata read by A4, HTTP 200,
  6,545 B; `_djvu.txt` layer present). A **local-chamber** discount-store study in window: registered as a
  LEAD and deliberately not pulled — it is North Carolina, not the company's four-state area, and one
  document does not justify the fetch while the roster question is open.
* **Page images (`_text.pdf`) of the BW and *Stores* volumes** — every page-number and table-pairing
  ambiguity in this dossier (U-A4/1, U-A4/2, U-A4/5, U-A4/7) is a microfilm-OCR artefact and is closed only
  by the image.
* **The duplicate BW index bindings** (`_1962_index_0`, `_1963_index_0/_1`, `_1964_index_1`, etc.) as a
  cross-check on whether a zero is OCR loss or real silence — **same publisher, so a retrieval check, never
  a second lineage.**
* Canada's `31761117266239` DBS "Chain Store Sales and Stocks" — found by the intake, out of scope,
  registered so it is not re-burnt.

---

## Provenance ledger

Format per §7: `| Source | Type | Primary/Secondary | Event date | Publication date | URL | Tier | Confidence |`
"Source date" of every retrieval is **2026-09-25**; bytes are the A4 ledger's received figure against the
size declared in the item's own metadata.

| Source | Type | Primary/Secondary | Event date | Publication date | URL | Tier | Confidence |
|---|---|---|---|---|---|---|---|
| `sim_business-week_1962_index` | BW annual index, whole text layer | Primary (periodical's own apparatus) | 1962 | 1963 | `https://ia802906.us.archive.org/14/items/sim_business-week_1962_index/sim_business-week_1962_index_djvu.txt` | 2 | High — 1,273,570 B EXACT, 196,549 words, read whole |
| `sim_business-week_1963_index` (Jan–Jun) | BW half-index | Primary | 1963 H1 | 1963/64 | metadata→server→dir | 2 | High — 605,043 B EXACT, 100,003 words |
| `sim_business-week_business-week_july-december-1963_index` | BW half-index | Primary | 1963 H2 | 1964 | `https://ia601007.us.archive.org/15/items/sim_business-week_business-week_july-december-1963_index/…_djvu.txt` | 2 | High — 633,645 B EXACT, 99,760 words |
| `sim_business-week_1964_index_0` | BW annual index | Primary | 1964 | 1965 | `https://ia902902.us.archive.org/33/items/sim_business-week_1964_index_0/sim_business-week_1964_index_0_djvu.txt` | 2 | High — 1,286,804 B EXACT, 203,895 words |
| `sim_business-week_1965_index` (Jul–Dec) | BW half-index | Primary | 1965 H2 | 1966 | metadata→server→dir | 2 | High — 612,999 B EXACT, 98,569 words |
| `sim_business-week_business-week_january-june-1965_index` | BW half-index | Primary | 1965 H1 | 1965/66 | `https://ia800104.us.archive.org/28/items/…_djvu.txt` | 2 | High — 637,923 B EXACT, 100,903 words |
| 1966 index (intake) | BW annual index | Primary | 1966 | 1967 | `https://ia800606.us.archive.org/17/items/sim_business-week_1966_index_0/…_djvu.txt` | 2 | Medium — 1,177,551 B EXACT, `DISCOUNT Houses` block OCR-lost |
| 1967 Jan–Jun (A4) + `…july-december-1967_index-contents` (A4) | BW half-indexes | Primary | 1967 | 1968 | metadata→server→dir | 2 | High — 611,323 B and 556,337 B, both EXACT |
| `sim_business-week_1968_index` | BW annual index | Primary | 1968 | 1969 | `https://ia600109.us.archive.org/30/items/sim_business-week_1968_index/…_djvu.txt` | 2 | High — 914,791 B EXACT, 147,820 words |
| 1969 index (intake) | BW annual index | Primary | 1969 | 1970 | `https://ia800408.us.archive.org/25/items/sim_business-week_1969_index_0/…_djvu.txt` | 2 | High as to bytes (711,758 B); Medium as to A4's own read |
| `sim_business-week_1970_index_0` | BW annual index | Primary | 1970 | 1971 | `https://ia800500.us.archive.org/31/items/sim_business-week_1970_index_0/sim_business-week_1970_index_0_djvu.txt` | 2 | High — 336,463 B EXACT, 52,380 words |
| 1971 index (intake) | BW annual index | Primary | 1971 | 1972 | `https://ia800908.us.archive.org/33/items/sim_business-week_1971_index_0/…_djvu.txt` | 2 | High as to bytes (397,185 B) |
| `sim_stores_1946-06_28_6` | *Stores* monthly (Bulletin era) | Primary (trade press) | 1946-06 | 1946-06 | metadata→server→dir | 3 (1 for knowability) | Medium — bytes EXACT, worst OCR of the run |
| `sim_stores_1950-06_32_6` · `_1951-06_33_6` · `_1955-06_37_6` · `_1958-06_40_6` · `_1961-03_43_3` · `_1961-12_43_11` | *Stores* monthlies | Primary (trade press) | 1950-06 … 1961-12 | same | metadata→server→dir | 3 (1 for knowability) | High — all bytes EXACT; 1961-12 is the NRMA Discount Seminar issue |
| `sim_stores_1971_53_index` · `sim_stores_1972_54_index` | *Stores* annual indexes | Primary | 1971 / 1972 | 1972-01 / 1973-01 | `https://ia600409.us.archive.org/32/items/…` · `https://ia903200.us.archive.org/7/items/…` | 3 (1 for knowability) | Medium — 20,120 B and 17,704 B EXACT, **subject-only index** (A4-18) |
| `sim_stores_1970_52_index` · `_1974_56_index` · `_1975_57_index` (intake) | *Stores* annual indexes | Primary | 1970 / 1974 / 1975 | 1971 / 1975 / 1976 | intake's documented server URLs | 3 (1 for knowability) | Medium — same apparatus caveat |
| `hf-5465.-u-55-g-7` | Chamber-of-Commerce discount-store study, 1970 | Primary, **metadata only** | 1970 | 1970 | `https://archive.org/metadata/hf-5465.-u-55-g-7` (6,545 B, HTTP 200) | 3 | Registered as LEAD; text UNTRIED |
| **A4 scratch, outside the repository:** 22 text layers totalling 10,015,606 B received; `REQUEST_LEDGER.tsv` with 46 rows (utc · status · bytes · url · note) | retrieval proof | Secondary | 2026-09-25 | 2026-09-25 | — | — | High; this dossier's byte claims rest on it |
| **`../sources/periodicals/BUSINESSWEEK_INDEX_1962-1971_EXTRACT_walmart_and_sector_hits.txt`** — 47,277 B / 6,756 words | bounded extract with provenance header, written by A4 | Secondary (derived from the layers above) | 1962–1971 | 2026-09-25 | in-repo | — | High as transcription; offsets and raw/norm offsets printed |
| **`../sources/periodicals/STORES_NRDGA_1946-1972_EXTRACT_walton_and_discount.txt`** — 42,857 B / 5,821 words | bounded extract with provenance header, written by A4 | Secondary | 1946–1972 | 2026-09-25 | in-repo | — | High as transcription |
| intake artefacts (read-only): `_MANIFEST.md`, `_REQUEST_LEDGER.tsv`, `walmart_variety_sector/BUSINESSWEEK_INDEX_1964-1971_EXTRACT_discount_retail.txt` (44,966 B), `…/STORES_NRDGA_1960-1975_EXTRACT_discount_variety.txt` (8,017 B), `…/SEARCH_LOG.md`, the four `ia_*.json` | prior pass, cited not copied | Secondary | 2026-09-25 | 2026-09-25 | `00_universe/harvest/periodicals_intake/` | — | High as transcription; **A4 re-walked the BW layers itself rather than relying on them** |
| `WALMART_AR_1972…1980.txt` (nine files) | registrant corporate print | Primary, **one lineage** | FY1972–FY1980 | 1972-03-22 → 1980-04-01 | `../sources/periodicals/` | 1 | High as to content; capped by the single-lineage rule (§3) |

**A4 request ledger (hard cap 60).** **46 of 60 spent**, all sequential at `2.6 s`, TLS verification ON,
UA `FoundersPlaybook-A4-walmart-periodicals/1.0 (research@example.org)`. **45 × HTTP 200, 1 × read-timeout
ERR (0 bytes, first 1964 attempt — recovered by a separately planned re-walk, not a blind retry),
0 × 429, 0 × 503, 0 back-off firings, 0 hosts halted, 0 retries after a rate signal.** Composition:
5 `advancedsearch.php` queries · 17 `metadata/<id>` calls · 21 text-layer GETs (16 via the
metadata→server→dir route + 5 direct re-walks of the intake's documented server URLs) · 3 malformed/empty
search results recorded as such. Bytes received 10,015,606 into scratch outside the repo; ~90 KB of
bounded extracts written into the repo across two new files. **18 requests left unspent and deliberately
not spent on the blocked hosts**, which would return the same 403 / TLS / 429 already on the record.

---

## Depth-verdict assessment

**The question §14 rule 6 asks:** is the Walmart Stage-1 record still one voice? A3 §7.2(c) states the
count of independent lineages in the financial record is **1**, that nine consecutive fiscal years sit on
the registrant's own reports plus its auditor's opinions, and that "no number of further years of
Wal-Mart's own annual reports can move this verdict; only a different publisher can."

**A4's answer, final (after 22 periodical layers read whole and grepped in this run):**

1. **Family 3 (periodical corpora) has moved from UNANSWERED-never-tried to PARTIALLY POSITIVE.** Ten
   Business Week index years 1962–1971 — read whole, month-by-month coverage proven continuous, ~1.06 M
   words of printed index matter — plus the *Stores* monthly run 1945–1961 (200 items enumerated, 8 read
   whole) and *Stores* annual indexes 1970–1975 (all five that exist, read). These are a **different
   publisher and a different lineage** from the registrant, contemporaneous, dated and paginated: exactly
   the family §14 rule 6 said was missing and that no other Walmart pass had actually searched.
2. **It does not move the company-level verdict, for one specific reason: not one item names Wal-Mart.**
   `wal-mart` and `walmart` are 0 in every volume read, and every hit on `walton`, `arkansas`, `rogers`,
   `newport`, `ben franklin`, `five-and-dime`, `small town` resolves to a different person, firm or place —
   eight decoys documented with character offsets (A4-07, A4-17, A4-20, A4-21, A4-28, A4-33, A4-35, A4-41).
   **The independent-lineage count for the financial register is therefore unchanged at 1.**
3. **What A4 does add, and it is not nothing: a second, independent lineage for the market-state layer.**
   Business Week's sector coverage 1962–1971 and *Stores*' November-1961 Discount Seminar report are
   Tier-1 evidence for "what was publicly known and when" (method §5 as applied in this brief), and they
   are not derivative of anything the company filed. §H and §I of the Stage-1 dossier can now be written
   against third-party print instead of against the registrant's later account of its own context.
4. **Family tally, restated for the merge.** POSITIVE: corporate print (FY1972–FY1980, 9 documents, one
   lineage) · periodicals **for the sector** (Business Week index matter 1962–1971; *Stores* 1945–1961 and
   indexes 1970–1975) · museum (1 artifact) · census inventory (enumerated, content UNTRIED).
   **EMPTY as proven null within a stated perimeter:** EDGAR pre-1994 · web archives pre-1990 · IA
   registrant print pre-FY1972 · **Wal-Mart naming: 10 BW index years + 5 *Stores* indexes + 8 *Stores*
   monthlies · IA holdings of *Chain Store Age* / *Discount Store News* / *Discount Merchandising* / any
   NRDGA-NRMA roster.** UNANSWERED: Google Books 429 · HathiTrust TLS (no status) · Chronicling America and
   loc.gov 403 · UALR CONTENTdm 403 · arkdigitalcollections DNS (never cite) · thefreelibrary 403 ·
   `archive.org/download/` TLS · Wayback prefix sweeps 504. UNTRIED: paper SEC records · county/SoS records
   · D&B and AUDITS & Surveys volumes · Census of Business Arkansas 1963/1967 text · 193 *Stores* issues ·
   all page images.
5. **Depth verdict recommended.**
   * FY1972–FY1980 financial interior: **unchanged** — `DEPTH-CORE (single-lineage)`.
   * §H market-as-knowable and §I competition-state, 1958–1971: **upgrade to DEPTH is now defensible** on
     the periodical lineage alone (this is the only section of Walmart Stage 1 that can be rated above
     provisional on any basis other than the company's own word).
   * **Company-level Stage-1 verdict: remains `PROVISIONAL`.** §14 rule 6's four-family requirement is now
     *searched* rather than *assumed*, which is what the rule actually polices; but the rule's purpose —
     independent corroboration of the company's own record — is not met, because the second lineage names
     the sector and never the firm.
   * **The one-line statement becomes: "the register is deep, the sector around it is now independently
     evidenced, and the record of the company is still one voice."**
6. **What keeps it provisional even if every UNTRIED item above is closed.** (a) The article **text**
   behind every Business Week index entry is unreachable for 1962–1971 on this route, so all sector records
   here are index-level by construction. (b) FY1962–FY1967 financial lines remain EMPTY in the registrant's
   own series and no periodical can retroactively fill them. (c) The sector's own trade press remains
   UNANSWERED because three host families are blocked from this machine, and it is where a small Arkansas
   chain would most plausibly have been noticed. (d) Microfilm OCR can lose a name: *Stores*' 1971 index
   shows `variety` 0 and `discount` 0 in a retail journal's own annual index whose 1974 counterpart plainly
   does carry discount entries — so no zero in this dossier is stated at High for a subject-only volume.
   (e) No page image was pulled, so every page-number ambiguity (U-A4/1, U-A4/2) is an OCR artefact that
   only an image can settle.
7. **What would actually change the verdict, named so the next pass does not guess:** one dated periodical
   item printing "Wal-Mart" or "Walton's" — ranked by likelihood: (i) NRMA/NRDGA membership rosters or a
   chain directory holding year (absent here, present on HathiTrust/Google Books most plausibly — blocked);
   (ii) an Arkansas, Missouri, Kansas or Oklahoma daily via an unblocked route (Benton County searches on IA
   return 1854–1895 county histories, not press — A4's EMPTY row); (iii) the D&B discount-store counts,
   which would at least convert a *sector* count from pointer to document; (iv) the 193 unread *Stores*
   issues, whose genre makes them the weakest candidate (A4-29) and which should be sampled
   convention/roster-wise rather than swept.

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
"Walton" query hit `WALTON, William / Holiday Inns` (BW 1962 index p.47, Jul.14), `WALTON, William B. /
A single standard for travelers` (BW 1963-H2 index p.114, Nov.16), `WALTON, Richard / Rhodes-tinkerer
inventor` and `Dr. C. Walton Lillehei` (BW 1968 index), and `H. C. Walton` (BW 1970 index p.4, Aug.29 — a
letter-writer). Arkansas hits resolve to the Arkansas Louisiana Gas Co. (1962), the Arkansas River barge
project (1967, 1970) and Arkansas school-desegregation stories (1963-H2, ten hits); Rogers hits to
ROGERS Cartage Co. and four persons; Newport hits to Newport News Shipbuilding, Newport Bridge and
Newport R.I./Ky. A2's family already contains one known state error (U-A2/7: "waltons newport **mo**" —
wrong state; Newport is **Kentucky**).
**Action:** merge propagates all eight decoy forms to `queries.json` known-traps and to A2's outbound list.
**A "Walton" search that returns a hit is not a witness; each must be read in context, as here.**

**COR-A4-06 — the "Small town greets the discounters" entry must never be cited as Wal-Mart evidence.**
It is indexed under **ALDENS, Inc.** in Business Week's 1964 company alphabet (offset 665,015) and its
`DISCOUNT Houses` cross-entry prints the fuller line "Small town greets the discounters: Gamble-Skogmo is
opening franchised T…" (offset 828,735). Aldens and Gamble-Skogmo were Minnesota-based
variety/mail-order discount operators — a **competitor's** small-town expansion, three months and two
thousand miles from Bentonville. The same headline reads so much like Wal-Mart's own later positioning
that it is the single most dangerous false positive in this corpus. **Action:** merge records it in
`conflicts.csv` as a resolved non-attribution and in the fleet's trap list; A4 states it at A4-20.

**COR-A4-07 — three of Business Week's index items on this route are HALF-YEAR volumes, and any count
taken from them must say which half.** `sim_business-week_1963_index` (Jan–Jun 1963 only; Jul–Dec month
tokens 0), `sim_business-week_1965_index` (Jul–Dec 1965 only), `sim_business-week_1967_index` (Jan–Jun
1967 only), proven by month-token arithmetic at A4-19; the missing halves are
`sim_business-week_business-week_july-december-1963_index`, `…_january-june-1965_index` and
`…_july-december-1967_index-contents`, which A4 retrieved and read, closing all three years. The intake's
`_MANIFEST.md` §3 and §4.2 describe the six volumes it held as "annual indexes", which is correct for its
own six; **the route fact worth carrying forward is that the SIM index family is not uniformly annual.**
**Action:** merge adds this to `queries.json` (an index-year harvest must check month tokens before calling
a year searched), and A4's §Wal-Mart-named table now shows 1962–1971 as ten continuous full years.

**COR-A4-08 — the *Stores* annual index cannot support a strong EMPTY, because it has no company-name
sequence.** Its headings are subjects only (A4-18, printed verbatim in the extract: `Advertising,
Promotion, Display` / `Merchandising` / `Operations` / `Personnel` / `Consumerism` / `Credit` /
`Finance and Sales` …), so a zero means "no article indexed under that subject-word in the legible part of
an OCR layer" rather than "the journal never mentioned the firm". A4 holds every *Stores* index EMPTY row
at Medium for exactly this reason, and 1971's index showing `discount` 0 where 1974's shows several
discount entries demonstrates the loss mechanism concretely. **Action:** any merge text that cites a
*Stores* index zero as proof of the company's absence from trade print must be corrected to
"absent from the reachable index apparatus of the trade journal for that year".

**COR-A4-09 — the intake's Target-1 suggestion that ~12 targeted *Stores* issues would add "a new family of
contemporaneous Tier-1 records to company_002's earliest period" did not survive the sample, and the reason
matters for fleet design.** Seven issues spread across 1946–1961 (14 requests) return `walton` 0,
`wal-mart` 0, `ben franklin` 0, `bentonville` 0 in every one; the journal's genre is management, policy and
Controllers' Congress cost studies, and it names a small franchisee only in a roster or directory — a
document class proved absent from this corpus (A4-41, NRMA-titled search → 10 items, no roster). **Action:**
the merge should re-point the fleet's Walmart Stage-1 periodical brief at (i) membership rosters/chain
directories on the blocked hosts, (ii) unblocked local-daily routes, and (iii) the Dun & Bradstreet discount
counts now *dated* by A4-31 — not at a deeper sweep of *Stores* monthlies, whose yield for company-naming is
now measured, not assumed. **The monthly run remains valuable, but for §H sector state (A4-26, A4-36), not
for the named witness.**

---

## CSV append rows

Schemas copied verbatim from `company_001_amazon/*.csv` (the header blocks below are byte-faithful to
`quantitative.csv`, `timeline.csv`, `sources.csv` and `conflicts.csv` as read on 2026-09-25). Every field
containing a comma is double-quoted; dates ISO, partial where the evidence is partial; `UNKNOWN` is a valid
value and no cell is empty; `source_id` values continue A3's register (A3 used S0101–S0111; **A4 opens at
S0112 and never redefines an earlier one**, §13). **A4 rows are append-only; nothing in A2's or A3's row
blocks is edited or removed by this file.**

**Category discipline, stated once before the rows:** every quantitative and timeline row below is a
**SECTOR** observation, a **market-knowability** observation, or a **null** about the company. **None is a
Wal-Mart financial or operational metric** — no independent publication in hand carries one — and the
`notes` cells say so, because a merge that reads a `Walmart,stage1,…` row whose metric is the discount
industry would otherwise propagate a category error into the master dataset.

### `quantitative.csv` — header
```
company,stage,date,metric,value,unit,source,source_date,evidence_class,confidence,derived_arithmetic,notes
```
### `quantitative.csv` — rows
```csv
Walmart,stage1,1962,"SECTOR — discount industry scale as the company entered it: Business Week's own characterisation 'fast-growing $6-billion industry'",6000000000,USD/year,"S0112 (BW 1962 index, p.78, Dec.1 1962, 'Discounters strive to ride out storm')",1962-12-01,FACT,Medium,,"SECTOR metric, NOT a Wal-Mart metric. Index-level evidence: headline as printed. The industry's definition/universe is UNKNOWN (article text unreachable for 1962-1971 on this route). Conflicts with S0114's $6.9 billion for the same calendar year — U-A4/5."
Walmart,stage1,1962,"SECTOR — discount-store sales amounted to $6.9 billion in 1962, as reported seven months later",6900000000,USD/year,"S0114 (BW 1963 Jul-Dec index, short item p.132, Jul.13 1963)",1963-07-13,FACT,Low,,"SECTOR metric. Printed in the layer as a reflowed fragment: 'stores amounted to $6.9 / billion in 1962 # p132, Jul.13'. Basis and universe UNKNOWN. Kept beside, not instead of, the $6.0 billion of 1962-12-01 — U-A4/5."
Walmart,stage1,1963,"SECTOR — count of discount stores: reported as DECREASING while units grew larger ('Fewer stores to share the pie … chains squeeze little guys')",UNKNOWN,direction-of-travel,"S0114 (BW 1963 Jul-Dec index, p.182, Nov.16 1963)",1963-11-16,CONTEMPORARY OBSERVATION,Medium,,"Numeric value UNKNOWN — the article text is unreachable, so the headline's direction is all that is recoverable. This is the contemporaneous sector statement closest to contradicting a 'small-town discounter was the future' reading; see U-A4/6 and the §2 hindsight audit."
Walmart,stage1,1958,"SECTOR — member stores reporting MORE discount houses in their communities",28,percent-of-respondents,"S0131 (Stores, June 1958, raw offsets 32746/32858)",1958-06,FACT,Medium,,"Survey of Stores' own readers. Respondent universe and n UNKNOWN (UNTRIED). Row is a SECTOR penetration measure, not a company measure. 2026-09-25 A4."
Walmart,stage1,1958,"SECTOR — member stores reporting FEWER discount houses in their communities",6,percent-of-respondents,"S0131 (Stores, June 1958)",1958-06,FACT,Medium,,"As above. Read with the 28% and 66% rows: the trade's own contemporaneous judgement was that discount spread was 'slowing down' four years before Wal-Mart opened."
Walmart,stage1,1958,"SECTOR — member stores reporting NO CHANGE in discount houses in their communities",66,percent-of-respondents,"S0131 (Stores, June 1958)",1958-06,FACT,Medium,,"28 + 6 + 66 = 100, consistent with a single-response survey; the check is stated, not assumed."
Walmart,stage1,1961,"SECTOR/ASSOCIATION — NRMA membership: retail establishments covered",11500,establishments,"S0133 (Stores, December 1961, raw offset 13749)",1961-12,FACT,Medium,,"MEMBERSHIP AGGREGATE, NOT a count of discount stores and NOT a market-size measure. Must never be used as a denominator for a Wal-Mart share of industry. Label travels with the number."
Walmart,stage1,1961,"SECTOR/ASSOCIATION — NRMA membership: combined annual sales of member stores",19000000000,USD/year,"S0133 (Stores, December 1961, raw offset 13749 'over $19 billion')",1961-12,FACT,Medium,,"Floor value ('over'), association self-report, universe = members only. Not comparable to the discount-industry figures above (different universes and definitions)."
Walmart,stage1,1961,"DERIVED — average annual sales per NRMA member establishment, 1961",1652174,USD/establishment/year,"S0133 (Stores, December 1961)",1961-12,DERIVED,Low,"19000000000 / 11500 = 1652174","A4's own arithmetic on the association's floor values; both inputs are 'over' figures so the quotient is a lower-bound-ish average of an undefined mix. Recorded to show the derivation is visible, not to be cited as an industry statistic."
Walmart,stage1,1961,"SECTOR — discount markup on hard goods as stated at NRMA's Discount Seminar",'26 to 28',percent,"S0133 (Stores, December 1961, raw offset 74633)",1961-12,FACT,Medium,,"As printed, a range, with the qualification that stores doing large small-electricals volume ran lower. NOT comparable with the registrant's gross-margin percentages, which are whole-store margins (A3 §5.5) — different measures, different bases; see U-A4/7's mechanism note."
Walmart,stage1,1961,"SECTOR — attendance at NRMA's first Discount Seminar (the trade body of Walton's own franchise form)",800,people,"S0133 (Stores, December 1961, raw offset 61464)",1961-11,FACT,Medium,,"Held November 1961, reported December 1961 — three months before the first Wal-Mart Discount City opened. 'About one half' conventional department stores; the rest discounters, lessees, buying offices, manufacturers, consultants, teachers, reporters. Association reporting its own event: third-party publisher, self-reported magnitude."
Walmart,stage1,1962-1971,"COMPANY — Wal-Mart named in Business Week index apparatus",0,named-index-entries,"S0112 S0113 S0114 S0115 S0116 S0117 S0118 S0119 S0120 S0121 S0122 S0123 S0124",1971,FACT,High,,"THE HEADLINE NULL OF THE DOSSIER. Ten consecutive index years (13 half-and-full volumes, ~1.06 million words, every layer byte-exact against its own metadata) return zero entries for Wal-Mart, Walmart, Ben Franklin (as a firm), five-and-dime, Bentonville, Springdale or Rogers Arkansas as a company. An index silence is BW's editorial record, NOT proof the company was unmentioned anywhere."
Walmart,stage1,1946-1961,"COMPANY — Walton's / Wal-Mart / Ben Franklin named in the *Stores* monthly issues sampled by A4",0,named-mentions,"S0127 S0128 S0129 S0130 S0131 S0132 S0133",1961-12,FACT,Medium,,"7 of ~200 issues in the 1945-1961 monthly run (1946-06, 1950-06, 1951-06, 1955-06, 1958-06, 1961-03, 1961-12), each read whole. 193 issues UNTRIED. OCR can lose a small name (the 1946 layer is the worst in the run), so this is Medium, not High — A4-40."
Walmart,stage1,1970-1975,"COMPANY — Wal-Mart named in *Stores* annual indexes",0,named-index-entries,"S0125 S0126 (A4: 1971, 1972) + intake: 1970, 1974, 1975",1975,FACT,Medium,,"All five index volumes that exist for the window on this route. Weaker instrument than BW: the *Stores* index is SUBJECT-only with no company alphabet, so a zero means 'no article indexed under that word', not 'the journal never mentioned the firm' (COR-A4-08)."
```

### `timeline.csv` — header
```
company,stage,date_or_range,event,actors,location,source_id,evidence_class,confidence,conflict_ref,notes
```
### `timeline.csv` — rows
```csv
Walmart,stage1,1958-06,"The variety/soft-goods trade's own journal reports that the spread of discount houses is 'slowing down' (28% more / 6% fewer / 66% no change among responding member stores)",NRDGA member stores (survey),United States,S0131,FACT,Medium,none,"SECTOR context four years before the first Wal-Mart Discount City. Evidence that a 1962 entrant was entering a sector its own trade journal was already describing as saturating — market-as-knowable, NOT a company claim."
Walmart,stage1,1961-11,"NRMA (the renamed NRDGA, Walton's own franchise association) holds its first Discount Seminar, 'The Discount Business — Is It for You?', ~800 attendees, half conventional department stores",National Retail Merchants Association; J. Gordon Dakins; Milton Woll; Richard Tumpowsky (American Dixie Shops); Perry Meyers; Stephen Masters; Alfred C. Thompson; Manfred Brecker (S. E. Nichols Co.),United States,S0133,FACT,High,none,"Reported in the December 1961 issue, three months before the first Wal-Mart opened. The trade formalised the discount transition before and independently of the company."
Walmart,stage1,1961-12,"S. E. Nichols Company is described as operator of 'Nichols Discount Cities since 1958, and with a long previous history in variety stores'",S. E. Nichols Company,United States,S0133,FACT,High,U-A4/7-adjacent,"A VARIETY-TO-DISCOUNT PRECEDENT printed in the company's own trade journal before the company existed. Anti-hagiography service (§2): it makes the registrant's later origin narrative one instance of a trade-wide move rather than an unprecedented act."
Walmart,stage1,1962-02-03,"'Discounters invade food field: And supermarkets are fighting back' (with illus) p.62",Business Week,United States,S0112,CONTEMPORARY OBSERVATION,High,none,"INDEX-LEVEL ONLY: headline, page, date. No article text is reachable for 1962 on this route, so nothing about its content is asserted anywhere in A4."
Walmart,stage1,1962-08-18,"'Discounter caught in cash bind: Grayson-Robinson's plight may presage a discount house shakeout' p.109 (OCR also prints p.169)",Business Week; Grayson-Robinson Stores Inc.,United States,S0112,CONTEMPORARY OBSERVATION,High,U-A4/1,"Page number unresolved between printings of the same OCR layer; both readings recorded, neither chosen. Sector, not company."
Walmart,stage1,1962-10-06,"'Discount store dropouts' p.101 — a short item on discount-store exits, within months of the first Wal-Mart opening",Business Week,United States,S0112,CONTEMPORARY OBSERVATION,High,none,"Same calendar year as the Rogers opening; BW indexed exits, not the new entrant. The absence is the record: A4-01, A4-17."
Walmart,stage1,1962-10-27,"'Shake-out among discounters seen as chain files in bankruptcy' p.83",Business Week,United States,S0112,CONTEMPORARY OBSERVATION,High,none,"Sector consolidation by failure, indexed in the founding year."
Walmart,stage1,1962-12-01,"'Discounters strive to ride out storm: fast-growing $6-billion industry is facing a major shakeout' p.78",Business Week,United States,S0112,CONTEMPORARY OBSERVATION,Medium,U-A4/5,"Carries the $6-billion sector figure. Disagrees with BW's own July 1963 report of $6.9 billion for calendar 1962; both kept."
Walmart,stage1,1963-07-13,"Short item: discount stores amounted to $6.9 billion in 1962, p.132",Business Week,United States,S0114,FACT,Low,U-A4/5,"The fragment is legible; the printed subject noun and universe are lost to OCR reflow. Recorded, not reconciled."
Walmart,stage1,1963-11-09,"'Survey by Dun & Bradstreet shows that … and television are the most profitable departments in a sampling of discount stores' p.79",Dun & Bradstreet via Business Week,United States,S0114,CONTEMPORARY OBSERVATION,Medium,none,"A NON-COMPANY SURVEY OF THE TRADE, now dated and paginated. The D&B volume itself is UNTRIED. This is the genre A3 §7.2(d) asked for, as a count of the industry rather than of the company — so it does not move the company's lineage count."
Walmart,stage1,1963-11-16,"'Fewer stores to share the pie: They get bigger but decrease in number as discounters, chains squeeze little guys' p.182",Business Week,United States,S0114,CONTEMPORARY OBSERVATION,Medium,U-A4/6,"Independent sector statement that the discount-store COUNT WAS FALLING in Wal-Mart's second year. Sector universes differ from the registrant's unit series; no reconciliation attempted."
Walmart,stage1,1964-05-16,"'Nielsen survey shows an increase in the number of mass merchandisers' p.100",A. C. Nielsen via Business Week,United States,S0115,CONTEMPORARY OBSERVATION,High,none,"Third-party counting operation on the mass-merchandiser population. Counterevidence to the 1963 'fewer stores' headline; different definitions of the counted class, so neither is preferred."
Walmart,stage1,1964-10-03,"'Small town greets the discounters' p.90 — indexed under ALDENS, Inc.; the cross-entry reads 'Gamble-Skogmo is opening franchised …'",Business Week; Aldens Inc.; Gamble-Skogmo Inc.,"small-town United States",S0115,FACT,High,U-A4/8,"THE DOSSIER'S MOST DANGEROUS FALSE POSITIVE: a headline that reads like Wal-Mart's own positioning, belonging to two Minnesota-based variety/mail-order operators. Not Wal-Mart evidence at any confidence. COR-A4-06."
Walmart,stage1,1964-11-14,"'The old five-and-ten spreads new wings: Woolworth branches out into mass merchandising in varied lines' (with cover and illus) p.58",F. W. Woolworth Co. via Business Week,United States,S0115,CONTEMPORARY OBSERVATION,High,none,"The largest incumbent variety chain publicly entering discount mass-merchandising — the same conversion path, at the top of the industry, in Wal-Mart's second year."
Walmart,stage1,1964-12-26,"Short item: Woolworth 'is setting up Worth Marts, discount mass-volume stores' p.24",F. W. Woolworth Co.,United States,S0115,CONTEMPORARY OBSERVATION,High,none,"Named-format evidence of the variety-to-discount conversion."
Walmart,stage1,1965-04-03,"'Is the franchise system legal? Supreme Court answer[ed] … when it decides GM violated Sherman Act' p.66",Business Week; U.S. Supreme Court,United States,S0117,CONTEMPORARY OBSERVATION,Medium,none,"Franchise-law question bearing on the Ben Franklin form. Article text UNREACHABLE, so the legal content is not asserted; the index entry is the whole fact."
Walmart,stage1,1965-06-02,"'Is success spoiling discount stores? Moves to carry more costly merchandise worry industry leaders' (with illus) p.97",Business Week,United States,S0117,CONTEMPORARY OBSERVATION,High,none,"Sector self-doubt indexed three years after Wal-Mart's founding."
Walmart,stage1,1967-09-23,"'Helping a small town cope with prosperity' (with illus) p.184 — a Jones & Laughlin steel-mill town story (Hennepin, Illinois)",Business Week; J.&L. Steel,United States,S0120,FACT,High,none,"Fifth documented decoy on the 'small town' theme. Recorded so no later pass reads BW's small-town coverage as Wal-Mart's."
Walmart,stage1,1969-08-02,"'Discount stores getting tryout' p.98; and 1969-09-20 'A discounter is a Washington department store' p.108",Business Week,United States,S0122,CONTEMPORARY OBSERVATION,High,none,"Sector spread into new markets in the year before Wal-Mart's OTC listing."
Walmart,stage1,1970-10-24,"'How Kresge became top discounter' (with cover, chart and illus) p.62 — cross-indexed under DISCOUNT Houses, KRESGE (S. S.) Co. AND VARIETY Stores",S. S. Kresge Co. via Business Week,United States,S0123,FACT,High,none,"Third-party naming of Wal-Mart's principal comparator, and BW's own taxonomy placing Kresge under VARIETY Stores is independent evidence that the variety and discount trades were publicly treated as one competitive field in Wal-Mart's first public year."
Walmart,stage1,1971-11-20,"'France: The French go wild over discount stores' (with illus) p.40",Business Week,France,S0124,CONTEMPORARY OBSERVATION,High,none,"Sector framing by 1971 is international; the discount model was a general business phenomenon, not an American teleology pointing at one chain."
Walmart,stage1,1962-1980,"NO independent periodical witness naming Wal-Mart recovered for ANY year of Stage 1",multiple publishers,United States,S0112-S0136,UNKNOWN,High,none,"The verdict-bearing row. 0 of 19 years. It is a statement about the corpus reachable from this machine plus three blocked host families (family 3 UNANSWERED in part), NOT a statement that no such print exists."
Walmart,stage1,1946-1961,"*Stores* monthly issues sampled contain no mention of Walton's, Wal-Mart, Ben Franklin Stores, Bentonville or Springdale",NRDGA/NRMA,United States,S0127-S0133,UNKNOWN,Medium,none,"7 of ~200 issues. The journal's genre (management and policy, not directory) is the probable reason and is stated as an INFERENCE with an alternative explanation, not as proof (A4-29)."
```

### `sources.csv` — header
```
source_id,stage,claim_supported,source_title,author_or_publication,source_type,primary_or_secondary,event_date,publication_date,access_date,url,archived_url,tier,evidence_class,confidence,independence_note,relevant_passage,notes
```
### `sources.csv` — rows
```csv
S0112,1,"1962 discount-sector coverage and the zero for the company's name (A4-01, A4-02, A4-04, A4-05, A4-07, A4-17)",Business Week 1962: Index (SIM bound index volume),Business Week (McGraw-Hill),printed periodical index / finding aid,primary,1962-01-01/1962-12-31,1963,2026-09-25,https://ia802906.us.archive.org/14/items/sim_business-week_1962_index/sim_business-week_1962_index_djvu.txt,OS scratch outside repo (whole layer) + sources/periodicals/BUSINESSWEEK_INDEX_1962-1971_EXTRACT_walmart_and_sector_hits.txt,2,FACT,High,"INDEPENDENT of the registrant (different publisher and lineage; contemporaneous). Names no Wal-Mart, so it corroborates no company figure. The intake's byte-identical pull of the same item is a second RETRIEVAL, not a second lineage,""","Discount store dropouts # pl01, Oct.6 / Discounters strive to ride out storm: Fast-growing $6-billion industry is facing a major shakeout (with illus) p78, Dec.1"",""","1,273,570 B received == metadata-declared (EXACT); 196,549 words read whole; wal-mart 0, walmart 0, ben franklin 0, five-and-dime 0; discount 88; four decoy families located by character offset"""
S0113,1,"1963 first-half sector coverage and the name-zero (A4-19, A4-30)",Business Week January-June 1963: Index,Business Week,printed periodical index,primary,1963-01-01/1963-06-30,1963,2026-09-25,https://archive.org/metadata/sim_business-week_1963_index (then server+dir to _djvu.txt),OS scratch + A4 bounded extract,2,FACT,High,INDEPENDENT publisher; HALF-YEAR volume (Jul-Dec month tokens = 0),"DISCOUNT Houses … Masters, Inc. files under Seed XI of the Bankruptcy Act # p36, Feb,""","605,043 B EXACT; 100,003 words; wal-mart 0; discount 6"""
S0114,1,"1963 second half: the $6.9bn 1962 sector figure, the Dun & Bradstreet discount survey, the 'fewer stores' headline, and the name-zero (A4-30, A4-31, A4-32, A4-33)",Business Week July-December 1963: Index,Business Week,printed periodical index,primary,1963-07-01/1963-12-31,1964,2026-09-25,https://ia601007.us.archive.org/15/items/sim_business-week_business-week_july-december-1963_index/sim_business-week_business-week_july-december-1963_index_djvu.txt,OS scratch + A4 bounded extract (block at raw offset 180304),2,FACT,High,INDEPENDENT publisher; NEW volume retrieved by A4 (the intake never held the 1963 second half),"stores amounted to $6.9 / billion in 1962 # p132, Jul.13 / Fewer stores to share the pie: They get bigger but decrease in number as discounters, chains squeeze little guys p182, Nov.16,""","633,645 B EXACT; 99,760 words; wal-mart 0; walton 1 (William B. Walton decoy); arkansas 10 (schools and Faubus, none retail); discount 34"""
S0115,1,"1964 sector coverage and the Aldens / Gamble-Skogmo resolution of 'Small town greets the discounters' (A4-08, A4-09, A4-20, A4-30)",Business Week 1964: Index,Business Week,printed periodical index,primary,1964-01-01/1964-12-31,1965,2026-09-25,https://ia902902.us.archive.org/33/items/sim_business-week_1964_index_0/sim_business-week_1964_index_0_djvu.txt,OS scratch + A4 bounded extract,2,FACT,High,"INDEPENDENT publisher. First GET returned a read-timeout ERR (0 B); the item was pulled whole on a separately planned re-walk, not a blind retry","Nielsen survey shows an increase in the number of mass merchandisers # p100, May 16 / Small town greets the discounters p90, Oct.3 (indexed under ALDENS, Inc.),""","1,286,804 B EXACT; 203,895 words; wal-mart 0, walton 0, arkansas 0, ben franklin 0; discount 40; small town 13; variety store 2"""
S0116,1,"1965 second-half coverage and the name-zero (A4-19, A4-30)",Business Week July-December 1965: Index,Business Week,printed periodical index,primary,1965-07-01/1965-12-31,1966,2026-09-25,https://archive.org/metadata/sim_business-week_1965_index (then server+dir to _djvu.txt),OS scratch + A4 bounded extract,2,FACT,High,INDEPENDENT publisher; HALF-YEAR volume (Jan-Jun tokens near zero),"Is success spoiling discount stores? (entry legible across the two 1965 halves),""","612,999 B EXACT; 98,569 words; wal-mart 0; discount 14"""
S0117,1,"1965 first half: franchise-law entry and the sector's own self-doubt; name-zero (A4-30, A4-34)",Business Week January-June 1965: Index,Business Week,printed periodical index,primary,1965-01-01/1965-06-30,1965,2026-09-25,https://ia800104.us.archive.org/28/items/sim_business-week_business-week_january-june-1965_index/sim_business-week_business-week_january-june-1965_index_djvu.txt,OS scratch + A4 bounded extract,2,FACT,High,INDEPENDENT publisher; NEW volume retrieved by A4,"Is success spoiling discount stores? Moves to carry more costly merchandise worry me[n] industry leaders (with illus) p97, Jun.2 / Is the franchise system legal p66, Apr.3,""","637,923 B EXACT; 100,903 words; wal-mart 0, walton 0; arkansas 1 (Hughes Aircraft); rogers 1 (a person); discount 22"""
S0118,1,1966 coverage (Kresge cover story) and the OCR-lost DISCOUNT Houses block (A4-14),Business Week 1966: Index,Business Week,printed periodical index,primary,1966-01-01/1966-12-31,1967,2026-09-24,https://ia800606.us.archive.org/17/items/sim_business-week_1966_index_0/sim_business-week_1966_index_0_djvu.txt,intake scratch layer; passages in periodicals_intake/walmart_variety_sector/BUSINESSWEEK_INDEX_1964-1971_EXTRACT_discount_retail.txt L979-1207,2,FACT,Medium,INDEPENDENT publisher; retrieved by the intake pass and NOT re-walked by A4,"NO_VERBATIM_PASSAGE_RECORDED (the 1966 discount block is unreadable and is cited as such),""","1,177,551 B EXACT per the intake's byte test; 193,116 words; page of the Kresge cover story ambiguous across printings (26 vs 126) — U-A4/2"""
S0119,1,"1967 first half: Arkansas indexed only as river infrastructure; name-zero (A4-19, A4-22, A4-30)",Business Week January-June 1967: Index,Business Week,printed periodical index,primary,1967-01-01/1967-06-30,1967,2026-09-25,https://archive.org/metadata/sim_business-week_1967_index (then server+dir to _djvu.txt),OS scratch + A4 bounded extract,2,FACT,High,INDEPENDENT publisher; HALF-YEAR volume,"ARKANSAS River … Oklahoma's stairway to the sea: Billion-dollar Arkansas River project will open both Arkansas and Oklahoma to barges by 1970 (with map and illus) p186, Apr.22,""","611,323 B EXACT; 96,935 words; wal-mart 0; arkansas 3 all infrastructure; discount 10"""
S0120,1,"1967 second half: the steel-town 'small town' decoy; name-zero (A4-30, A4-35)",Business Week July-December 1967: Index and Table of Contents,Business Week,printed periodical index,primary,1967-07-01/1967-12-31,1968,2026-09-25,https://ia800809.us.archive.org/12/items/sim_business-week_business-week_july-december-1967_index-contents/sim_business-week_business-week_july-december-1967_index-contents_djvu.txt,OS scratch + A4 bounded extract,2,FACT,High,INDEPENDENT publisher; NEW volume retrieved by A4,"Helping a small town cope with prosperity (with illus) p184, Sep.23 — a Jones & Laughlin steel-mill town story (Hennepin, Illinois),""","556,337 B EXACT; 88,978 words; wal-mart 0; arkansas 0; small town 4 none of them retail; discount 15"""
S0121,1,"1968 full-year coverage, three Walton / three Rogers / four Newport decoys, name-zero (A4-21, A4-30)",Business Week 1968: Index,Business Week,printed periodical index,primary,1968-01-01/1968-12-31,1969,2026-09-25,https://ia600109.us.archive.org/30/items/sim_business-week_1968_index/sim_business-week_1968_index_djvu.txt,OS scratch + A4 bounded extract,2,FACT,High,INDEPENDENT publisher; NEW volume retrieved by A4,"WALTON, Richard … tinkerer scoops the pros / LILLEHEIL, Dr. C. Walton … University of Minnesota,""","914,791 B EXACT; 147,820 words; all twelve months present (full year); wal-mart 0; discount 24"""
S0122,1,1969 sector coverage (discount tryouts) and the name-zero (A4-10),Business Week 1969: Index,Business Week,printed periodical index,primary,1969-01-01/1969-12-31,1970,2026-09-24,https://ia800408.us.archive.org/25/items/sim_business-week_1969_index_0/sim_business-week_1969_index_0_djvu.txt,intake scratch layer; passages in the intake extract L263-409,2,FACT,High,INDEPENDENT publisher; retrieved by the intake pass; not re-walked by A4,"Discount stores getting tryout # p98, Aug.2 / A discounter is a Washington department store # p108, Sept.20,""","711,758 B EXACT per the intake's byte test; 112,130 words"""
S0123,1,"1970 sector coverage; Kresge cross-indexed under VARIETY Stores; name-zero (A4-11, A4-12, A4-22, A4-30)",Business Week 1970: Index,Business Week,printed periodical index,primary,1970-01-01/1970-12-31,1971,2026-09-25,https://ia800500.us.archive.org/31/items/sim_business-week_1970_index_0/sim_business-week_1970_index_0_djvu.txt,OS scratch + A4 bounded extract,2,FACT,High,INDEPENDENT publisher; re-walked whole by A4,"How Kresge became top discounter (with cover, chart and illus) p62, Oct.24,""","336,463 B EXACT; 52,380 words; wal-mart 0; walton 1 (H. C. Walton, letter-writer); arkansas 1 (Arkansas River); kresge 7; variety store 1"""
S0124,1,1971 sector coverage and the name-zero (A4-13),Business Week 1971: Index,Business Week,printed periodical index,primary,1971-01-01/1971-12-31,1972,2026-09-24,https://ia800908.us.archive.org/33/items/sim_business-week_1971_index_0/sim_business-week_1971_index_0_djvu.txt,intake scratch layer; passages in the intake extract L496-633,2,FACT,High,INDEPENDENT publisher; retrieved by the intake pass; not re-walked by A4,"France: The French go wild over discount stores (with illus) p40, Nov.20,""","397,185 B EXACT per the intake's byte test; 63,140 words"""
S0125,1,1971 Stores annual index: subject-only apparatus and no Wal-Mart entry (A4-18),Stores 1971: Vol 53 Index,National Retail Merchants Association (formerly NRDGA),printed trade-journal index,primary,1971-01-01/1971-12-31,1972-01,2026-09-25,https://ia600409.us.archive.org/32/items/sim_stores_1971_53_index/sim_stores_1971_53_index_djvu.txt,OS scratch + sources/periodicals/STORES_NRDGA_1946-1972_EXTRACT_walton_and_discount.txt,3,FACT,Medium,"INDEPENDENT publisher and the trade body of Walton's own franchise form — but a WEAK instrument: no company alphabet, so a zero means 'no article indexed under that subject-word' and not 'the journal never mentioned the firm'","INDEX TO STORES MAGAZINE: 1971 | Advertising, Promotion, Display | … Merchandising …,""","20,120 B EXACT; 2,780 words; wal-mart 0, walton 0, ben franklin 0, variety 0, discount 0, Chain 0, Woolworth 0, Kresge 0. Bound January-1972 advertising pages ride in the same layer"""
S0126,1,1972 Stores annual index — the test at Wal-Mart's first contemporaneously-reported fiscal year (A4-18),Stores 1972: Vol 54 Index,National Retail Merchants Association,printed trade-journal index,primary,1972-01-01/1972-12-31,1973-01,2026-09-25,https://ia903200.us.archive.org/7/items/sim_stores_1972_54_index/sim_stores_1972_54_index_djvu.txt,OS scratch + A4 Stores extract,3,FACT,Medium,INDEPENDENT publisher; NEW volume retrieved by A4; same subject-only caveat,"INDEX TO STORES MAGAZINE: 1972 | Advertising, Promotion, Display | Bresee's Something Extra: A Smile.,""","17,704 B EXACT; 2,480 words; wal-mart 0; discount 1; Woolworth 0; Kresge 0. FY1972 is the registrant's first year with its own printed report, so this is the strongest available trade test at the fiscal boundary — and it is silent"""
S0127,1,June 1946: no Walton or Newport visibility the year after the first franchise (A4-23/A4-29),Stores (The Bulletin of the National Retail Dry Goods Association) 1946-06: Vol 28 Iss 6,NRDGA,printed trade journal,primary,1946-06-01,1946-06,2026-09-25,https://archive.org/metadata/sim_stores_1946-06_28_6 (then server+dir to _djvu.txt),OS scratch + A4 Stores extract,3,FACT,Medium,"INDEPENDENT publisher. Worst OCR of the run, which is why this EMPTY is Medium and not High","maikdowns at 4..j^ … casli discounts at 2..S' … rite axciage gross sale lor tlie vear stood at S3.41 (garble as printed),""","239,949 chars; 33,955 words; walton 0, wal-mart 0, ben franklin 0, arkansas 0, newport ky 0; discount 6 all in cash/employee-discount senses"""
S0128,1,June 1950: the close of the Newport era with no entry for the franchisee (A4-23),Stores 1950-06: Vol 32 Iss 6,NRDGA,printed trade journal,primary,1950-06-01,1950-06,2026-09-25,https://archive.org/metadata/sim_stores_1950-06_32_6 (then server+dir to _djvu.txt),OS scratch + A4 Stores extract,3,FACT,Medium,INDEPENDENT publisher,"June, 1950 THE PRESIDENT'S PAGE … By CHARLES G. NICHOLS President, NRDGA,""","241,457 chars EXACT; 34,243 words; walton 0, wal-mart 0, ben franklin 0, arkansas 0; nrdga 6; discount 9"""
S0129,1,June 1951: the Arkansas-Congressman decoy and the NRDGA Washington column (A4-24),Stores 1951-06: Vol 33 Iss 6,NRDGA,printed trade journal,primary,1951-06-01,1951-06,2026-09-25,https://archive.org/metadata/sim_stores_1951-06_33_6 (then server+dir to _djvu.txt),OS scratch + A4 Stores extract,3,FACT,Medium,INDEPENDENT publisher,"Employment Security Financing Act of 1951. Representative Wilbur Mills, Democrat of Arkansas,""","312,972 chars EXACT; 44,599 words; walton 0, ben franklin 0, bentonville 0; arkansas 1 (Congress, not retailing); nrdga 14"""
S0130,1,June 1955: the trade's attention on downtown renewal and price controls (A4-25),Stores 1955-06: Vol 37 Iss 6,NRDGA,printed trade journal,primary,1955-06-01,1955-06,2026-09-25,https://archive.org/metadata/sim_stores_1955-06_37_6 (then server+dir to _djvu.txt),OS scratch + A4 Stores extract,3,FACT,Medium,INDEPENDENT publisher,"Away With Summer Slump — NRDGA President Philip M. Talbott kicked off the joint campaign of the NRDGA and the American Newspaper Publishers Association,""","218,329 B EXACT; 30,608 words; walton 0; discount 16 mostly Controllers' Congress cash and employee discounts"""
S0131,1,"June 1958 discount-penetration survey: 28% more / 6% fewer / 66% no change (A4-26, A4-28)",Stores 1958-06: Vol 40 Iss 6,NRDGA,printed trade journal,primary,1958-06-01,1958-06,2026-09-25,https://archive.org/metadata/sim_stores_1958-06_40_6 (then server+dir to _djvu.txt),OS scratch + A4 Stores extract,3,FACT,High,INDEPENDENT publisher; a survey OF member stores BY their own journal — third-party instrument with self-reported responses; respondent universe UNTRIED,"It is evident, tcx), according to this survey, that the spread of discount houses over the country is slowing down. Only 28 per cent of the stores reported more discount houses operating in their communities, six per cent reported fewer such stores while the remainder (66 per cent) indicated no change,""","260,354 B EXACT; 36,833 words; raw offsets 32746/32858; arkansas 1 = a state roster @173557; masthead shows the 1958 rename to NRMA"""
S0132,1,March 1961: no name; the sector's willingness-to-try-new-ways sentence (A4-27),Stores 1961-03: Vol 43 Iss 3,NRMA,printed trade journal,primary,1961-03-01,1961-03,2026-09-25,https://archive.org/metadata/sim_stores_1961-03_43_3 (then server+dir to _djvu.txt),OS scratch + A4 Stores extract,3,FACT,Medium,INDEPENDENT publisher; the calendar year the Wal-Mart project was being prepared,"he cited the wifi four ingness to try new ways as a facto other in the success of the discount house, the (column reflow as printed),""","288,685 B EXACT; 40,880 words; walton 0, wal-mart 0, rogers ark 0, arkansas 0; discount 7"""
S0133,1,December 1961 NRMA Discount Seminar issue: the knowable market state three months before the first Wal-Mart (A4-36),Stores 1961-12: Vol 43 Iss 11,NRMA,printed trade journal,primary,1961-11-01/1961-12-31,1961-12,2026-09-25,https://archive.org/metadata/sim_stores_1961-12_43_11 (then server+dir to _djvu.txt),OS scratch + A4 Stores extract,3,FACT,High,"INDEPENDENT publisher, in-window and the closest document to the founding moment in this corpus. Its figures are the association's and the named speakers' own self-reports, so each is ONE voice inside a third party and is never counted as corroboration of a registrant figure","operator of Nichols Dis-ount Cities since 1958, and with a long previous history in variety stores / The Association's membership covers over 11,500 retail establishments with a combined annual sales of over $19 billion,""","174,925 chars EXACT; 24,370 words; discount 67; walton 0, wal-mart 0, ben franklin 0, bentonville 0, springdale 0, arkansas 0. Offsets: 13749 association scale, 61464 seminar attendance, 74633 markup 26-28%, 84160 and 84355 size-population table plus over-concentration, 91292 Nichols, 158315 seminar session list"""
S0134,1,The two bounded extracts A4 wrote into the company sources directory,"BUSINESSWEEK_INDEX_1962-1971_EXTRACT_walmart_and_sector_hits.txt (47,277 B / 6,756 words) and STORES_NRDGA_1946-1972_EXTRACT_walton_and_discount.txt (42,857 B / 5,821 words)",THE FOUNDER'S PLAYBOOK (A4 agent),derived bounded extract with provenance header,secondary,1945-01-01/1975-12-31,2026-09-25,2026-09-25,in-repo company_002_walmart/sources/periodicals/,same,—,TRANSCRIPT,High,"Derived from S0112-S0133; not an independent lineage. Written so byte counts, URLs, retrieval timestamps and character offsets travel with the text","headers carry the per-item completeness test and the OCR-state disclosure,""","every passage verbatim including garble; whitespace-normalised matching disclosed with raw offsets printed; both files an order of magnitude under the method 9.2 caps"""
S0135,1,Registered-not-downloaded lead: an in-window local discount-store trade-area study,"Shopper attitudes and trade areas for discount stores in Greensboro, North Carolina (D. Gordon Bennett;","Greensboro Chamber of Commerce, Population Committee, Research Division, 1970),Greensboro Chamber of Commerce",monograph with declared text layer,primary,1970,1970,2026-09-25,https://archive.org/metadata/hf-5465.-u-55-g-7,not downloaded,3,LEAD,UNKNOWN,"INDEPENDENT of the registrant; a chamber-of-commerce study, not a periodical. Text UNTRIED — one metadata request spent (6,545 B returned, HTTP 200); a _djvu.txt layer is declared present",NO_VERBATIM_PASSAGE_RECORDED,"registered so the next pass does not re-probe it; Greensboro NC sits outside the company's four-state area, so its value is sector-comparator, not company-witness"
S0136,1,The A4 retrieval proof behind every byte and status claim in this dossier,"REQUEST_LEDGER.tsv (47 rows: utc, status, bytes, url, note)",THE FOUNDER'S PLAYBOOK (A4 agent),retrieval log,secondary,2026-09-25,2026-09-25,2026-09-25,OS scratch directory outside the repository,copied into the two extract headers,—,PROVENANCE,High,not a source of facts; the re-walk proof for S0112-S0135,"NO_VERBATIM_PASSAGE_RECORDED,""","46 HTTP 200, 1 read-timeout ERR at 0 B, zero 429/503, zero back-off firings; 10,035,277 B received across 18 distinct hosts"""
```

### `conflicts.csv` — header
```
company,stage,conflict_id,section,claim_a,claim_a_source,claim_a_date,claim_b,claim_b_source,claim_b_date,why_they_differ,evidence_weight,best_supported_interpretation,residual_uncertainty,confidence
```
### `conflicts.csv` — rows
```csv
Walmart,stage1,U-A4/1,"T; A4 §Contradictions",Grayson-Robinson cash-bind story printed at p.109 (Aug.18 1962),sim_business-week_1962_index layer lines 38668 and 49785,1962-08-18,Same story printed at p.169,sim_business-week_1962_index DISCOUNT Houses block line 45113,1962-08-18,SIM microfilm OCR reflows and duplicates the same alphabetical block 2-5x with different truncated left margins; the leading 1 is either a page digit or an absorbed margin artefact,two printings for A and one for B but all from one machine pass on one volume — not two witnesses,p.109 by majority of printings with p.169 printed beside it and never erased,the 1962 issue scan is not on this route, so no page image is reachable and the question cannot be closed by anything currently available,Medium for A; Low for B
Walmart,stage1,U-A4/2,"T; A4 §Contradictions",Kresge 1966 cover story at p.26 (Jan.29 1966),sim_business-week_1966_index_0 lines 18506-18507,1966-01-29,Kresge 1966 cover story at p.126,sim_business-week_1966_index_0 lines 8338 and 26577,1966-01-29,the same OCR duplication mechanism; equal printings from the same volume,each reading has one printing and neither is independent,no page is asserted; the entry is cited by headline, cover status and date only only,unresolvable on this route,High that a Kresge cover story existed on that date; UNKNOWN as to its page
Walmart,stage1,U-A4/5,"H; A4 §Independent figures",The discount industry was a fast-growing $6-billion industry facing a major shakeout,Business Week p.78 Dec.1 1962 (S0112),1962-12-01,Discount stores amounted to $6.9 billion in 1962,Business Week short item p.132 Jul.13 1963 (S0114),1963-07-13,one is a rounded contemporaneous characterisation with an unstated universe; the other is a specific figure for the completed year published seven months later and printed as an OCR fragment whose subject noun is lost,both Tier-2 index-level citations from the SAME publisher, neither checkable because no article text is reachable,"$6.9bn is the figure the weekly later reported for calendar 1962 AND $6.0bn stands as the figure it published during 1962; both printed, neither chosen, neither used as a denominator",the definition of the counted class is UNKNOWN in both cases; the 15 percent gap is material to any share calculation,Medium that both were published; UNKNOWN what either measured
Walmart,stage1,U-A4/6,"H; A4 §Independent figures",The number of discount stores was decreasing while units grew larger and chains squeezed the little guys,Business Week p.182 Nov.16 1963 (S0114),1963-11-16,Wal-Mart's store count rose from 51 (FY1971) to 78 (FY1974) with positive same-store growth,WALMART_AR_1974.txt Five Year Progress Report; A3 Tables S1 and S3,1974-03-21,different universes measured by different instruments: an industry unit count in a headline versus one firm's audited store count,A is Tier-2 index-level with its numeric content unreachable; B is Tier-1 auditor-attested,both stand and the dataset refuses to explain the gap; the sector's contraction is NOT converted into the company's good fortune,whether anyone at Wal-Mart could or did observe the 1963 consolidation is UNKNOWN and no inference is offered,High that both claims exist; UNKNOWN as to any causal relation
Walmart,stage1,U-A4/7,"H; A4 §Independent figures",A published store-size-to-trading-area rule plus a warning of serious over-concentration of discount stores,Stores December 1961 NRMA Discount Seminar, Perry Meyers session (S0133 offsets 84160 and 84355),1961-12-01,The first Wal-Mart Discount City opened in Rogers, Arkansas, then a town of approximately 4700 / approximately 5,000 people, in a 30,000-60,000 sq ft format,WALMART_AR_1975.txt and WALMART_AR_1978.txt (and A3 U-A3/8),1975-03-28,A is trade guidance to conventional stores considering a discount venture, printed three months before the opening; B is a retrospective self-report about a store actually built, and B's own two population figures already disagree with each other,A is third-party and contemporaneous but its table is OCR-mangled; B is Tier-1 but retrospective and internally inconsistent,recorded as an unresolved divergence; NOT narrated as advice ignored and NOT as advice confirmed,column pairing of the printed table; the definition of trading area; and whether any Walton read or attended NRMA material — all UNKNOWN,Medium that the texts diverge; UNKNOWN which reading of the table is right
Walmart,stage1,U-A4/8,"T; A4 §Findings",Small town greets the discounters p.90 Oct.3 1964 is indexed under ALDENS, Inc.,sim_business-week_1964_index_0 offset 665015,1964-10-03,The same headline in the DISCOUNT Houses block continues Gamble-Skogmo is opening franchised …,sim_business-week_1964_index_0 offset 828735,1964-10-03,Business Week's company alphabet and its subject block attribute the same story to two different Minnesota-based variety and mail-order operators,same publisher, same volume, both placements genuine,immaterial to the verdict and therefore NOT adjudicated: under either attribution the article is a competitor's small-town discount expansion,Wwhich firm the article chiefly concerned; resolvable only from the unreachable article text,High that neither attribution supports a Wal-Mart reading
```

### Register notes for the merge

1. **`sources.csv` is append-only and global per company (§13).** A4 opens at **S0112** because A3 holds
   S0101–S0111. No A4 row redefines an existing identifier, and none re-uses a reserved one.
2. **`independence_note` is the field that carries this dossier's whole argument.** Every Business Week and
   *Stores* row is marked independent **of the registrant**; the *self-report-inside-a-third-party* caveat is
   written into S0131 and S0133 (a survey of members by their own journal; an association's account of its
   own seminar); and the intake's byte-identical retrieval of the same BW items is labelled a second
   **retrieval**, never a second **lineage** — §3's filing-lineage rule applied to periodicals.
3. **No row in `quantitative.csv` is a Wal-Mart company metric.** A merge that promotes any of them into §P
   of the stage file without the `SECTOR` label commits a §13 category error; the `notes` cells say so.
4. **`conflicts.csv` rows are reported, not resolved.** U-A4/5, U-A4/6 and U-A4/7 stay open on purpose — the
   brief's rule is "record both sides, never reconcile silently".
5. **`data_gaps.csv` is not reproduced here** because the brief's CSV list named four registers, not seven;
   §Data gaps in this file is its source, and its `follow_up_task` values are the five candidates listed at
   §Depth-verdict item 7 — all of them High importance, so none may be closed as "no further action".
6. **`claim_ref` cross-walk:** quantitative and conflicts rows cite A4 record IDs in their `source` /
   `section` cells; timeline rows cite the `S01xx` identifiers above, which is the §13 convention.
