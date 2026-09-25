# AMAZON STAGE 1 — Evidence Cache

Local copies of primary and secondary documents already retrieved. **Check here before
fetching anything.** Re-downloading a document that is already on disk wastes the agent budget
that should go to reading it, and budget exhaustion is this project's dominant failure mode
(two wave-1 agents ended with a full head and an empty file).

Location: **`../sources/`** — `E:\founder's playbook\founders_playbook\01_companies\company_001_amazon\sources\`.
All paths in the tables below resolve there unless marked STILL-MISSING.

> **⚠ DELETION INCIDENT, 2026-09-23 — CLOSED.** An adversarial-review agent cleaned up the shared
> `_scratch\` folder as if it owned it, destroying every download listed here (the S-1, the 1997 10-K,
> Sheff's interview, HistoryLink, the Mosaic archive). The table is retained because each entry is the
> authoritative description of a document that *was* read and quoted in the dossiers.
> **RESTORED 2026-09-23 by the Level-3 Evidence Registrar:** the six primary documents were re-fetched
> from EDGAR, davidsheff.com, historylink.org and the Mosaic mirror, saved into `../sources/` under their
> own names with a provenance header block (retrieval URL, access date, accession/publication date, byte
> size, completeness), and the load-bearing dossier quotations were re-verified character-by-character.
> **The former "paths no longer resolve" warning is retired.** Restoration created files and amended this
> cache only; nothing anywhere was deleted, moved or tidied. `../sources/` is a protected evidence
> archive, **not** a scratch directory: it is read-only for retrieval agents, is never a cleanup target,
> and agents are forbidden from deleting anything outside their own assigned output file.

Consequences accepted honestly: (1) ~~any **T1** claim whose text is not preserved inside a dossier's
`Passage:` field must be re-retrieved~~ — **discharged for every restored row; the quotations now re-read
from disk (see "Re-verified" below)**; (2) ~~the citation spot-check and Audit 2 will have to re-fetch~~ —
**re-read, for the filings, Sheff, HistoryLink and Mosaic**; (3) the secondary press rows (`lat`, `stone`,
`wiki`, `p.html`, `amztimeline`) remain **STILL-MISSING**, so any claim resting only on them is still
un-reverifiable locally; (4) **restoration surfaced three metadata errors in this cache itself — most
seriously the Sheff date — which are more damaging than the file loss and are recorded in
*Corrections from the restoration*.**

### Restoration map (old `_scratch` name → new `../sources/` path → status, bytes confirmed)

| Former file | Now in `../sources/` | Body bytes / file bytes | Status |
|---|---|---|---|
| `s1_orig.txt` (1.44 MB) | `S-1_original_acc-0000891618-97-001309_filed-1997-03-24.txt` | 1,444,013 / 1,445,709 | **RESTORED** |
| `s1a_full.txt` (302 KB) | `S-1A-No5_acc-0000891020-97-000839_filed-1997-05-14.txt` | 301,685 / 303,069 | **RESTORED** (byte-exact to the lost file) |
| *(new — added by restoration)* | `S-1A-No3_acc-0000891020-97-000755_filed-1997-05-09.txt` | 304,886 / 306,425 | **RESTORED** |
| `amzn10k1997.txt` (606 KB) | `10-K_FY1997_acc-0000891020-98-000448_filed-1998-03-30.txt` | 606,461 / 607,959 | **RESTORED** |
| `sheff.txt` / `sheff.html` (52 KB / 132 KB) | `sheff-playboy-interview_davidsheff-com-jeff-bezos.txt` / `.html` | 50,116 B text / 52,098 file · 131,785 B html / 133,811 file | **RESTORED** (premise void — see C-1) |
| `ncsa.html` (984 KB) | `ncsa-mosaic-whats-new_1995-08_kitchencloset.html` | 983,573 / 985,639 | **RESTORED** |
| `hl.txt` / `idx.html` (29 KB / 14 KB) | `historylink-essay-23230_Amazon-The-Early-Years-1995-1999.txt` / `.html` | 21,399 / 54,616 | **RESTORED** |
| *(RD-006, Wayback)* | `NULL_RESULT_wayback_1995_1996.md` | 4,427 | **RESTORED as a documented null** |
| `s1a.txt`, `ddg1.html` | — | — | **NOT RESTORED, deliberately** (error/search pages; do not cite) |
| `lat.*`, `stone.*`, `wiki.txt`, `p.html`, `amztimeline.html`, `wb_amazon.html` | — | — | **STILL-MISSING** (outside restoration scope) |

Status key: **T1** primary/contemporaneous · **T2** reported secondary · **T4** lead only, chase
its underlying source · `date?` = publication date still to be extracted from the text itself.

## Corrections from the restoration (2026-09-23, Level-3 Evidence Registrar)

These were found by reading the documents themselves, not the dossiers. Agents J, K, F and Graphics
Recovery independently reached C-2/C-3; the table records all four in one place so a later agent does
not rediscover them.

| # | Cache / dossier said | Document actually says | Consequence |
|---|---|---|---|
| **C-1** | `sheff.txt` = "David Sheff's **1994** interview/profile of Jeff Bezos (**Wired**, 1994)", tier **T1**, "**quote verbatim with its 1994 date**" | Page states: "**This interview was conducted in 1999 and published in 2000.**" Venue is **PLAYBOY** — intro reads "Playboy sent Contributing Editor David Sheff to meet with the father of e-commerce" — and it dates the talk to when Amazon was "valued at \$22 billion" with "12 million users". Every "1994" in the body is the founding year, not publication | **The earliest contemporaneous founder-state document assumed by this stage does not exist.** Confirms and sharpens agent K's re-tier: the row is not Wired and not 1994, and no Sheff 1994 Bezos interview was located at that URL or elsewhere during restoration. Tag every quotation **FOUNDER CLAIM (RETROSPECTIVE, CONDUCTED 1999 / PUBLISHED 2000)** |
| **C-2** | accession `000089102097000839` = "Form S-1 … filed **1997-03-24**" | That accession is **Amendment No. 5**, filed **1997-05-14** (`CONFORMED SUBMISSION TYPE: S-1/A`, `PUBLIC DOCUMENT COUNT: 2`). The document filed 1997-03-24 is accession **`0000891618-97-001309`** — different filer-agent prefix | **Both now restored**, so either citation resolves locally |
| **C-3** | `amzn10k1997.txt` = "Form **10-K**, fiscal 1997" | EDGAR classes the FY1997 annual report as **`10-K405`**, accession `0000891020-98-000448`, filed **1998-03-30**, period **1997-12-31**. It *is* the FY1997 annual report | Cite as "Form 10-K405 (FY1997 annual report)". Found via `CIK0001018724-submissions-002.json`; the main submissions JSON carries only 2021+ |
| **C-4** | pricing-program sentence sourced to "**Amendment No. 4**", accession `0000891020-97-000755` (9 May 1997) | That accession's own text reads **AMENDMENT NO. 3**. EDGAR assigns "Amendment No. 4" to accession `0000891020-97-000822` (1997-05-13) | The dossier's **accession and date are correct; the ordinal is off by one.** Fix the label, keep the citation |

### Re-verified against the restored files, 2026-09-23

Found **verbatim** in each of the original S-1 (`…1309`), Amendment No. 3 (`…755`) and Amendment No. 5
(`…839`) — so the dossier citations hold whichever of the three is meant:

- `"Since opening for business as \"Earth's Biggest Bookstore\" in July 1995…"` — the Stage-1 anchor.
- `"The Company also intends to offer attractive pricing programs, which will reduce its gross margins. Because the Company has relatively low product gross margins, achieving profitability given planned investments…"` — **the adversarial dossier's pricing-program sentence is confirmed present in `0000891020-97-000755`.**
- `"Operating expenses in 1994 were minimal."` and `"the Company had no sales and its operating activities related primarily to the development of the necessary computer infrastructure and initial planning and development of the Amazon.com sit[e]"` — the 1994–mid-1995 pre-revenue statement the dossier quotes against the "2,300%" framing.

**Not** in the FY1997 `10-K405`: the pricing-programs and "no sales" sentences. It does carry the
"Earth's Biggest Bookstore" / July 1995 formula. Do not cite the 10-K for the other two.

## Filings — highest value in the cache

| File | Size | Document | Tier | Use for |
|---|---|---|---|---|
| `S-1_original_acc-0000891618-97-001309_filed-1997-03-24.txt` **RESTORED** | 1,444,013 B body / 1,445,709 B file | Amazon.com **Form S-1 (ORIGINAL)**, EDGAR accession **0000891618-97-001309** (CIK 1018724, SEC File No. 333-23795), filed **1997-03-24** — complete submission incl. 38 documents. *(This is the file the old `s1_orig.txt` row described while naming the wrong accession — see C-2.)* | **T1** | History of the Enterprise, business strategy, marketing, audited 1995/1996 financial data, property, employees, executive compensation, related-party transactions, certain beneficial owners, risk factors, legal proceedings. The anchor for every money and chronology claim |
| `S-1A-No5_acc-0000891020-97-000839_filed-1997-05-14.txt` **RESTORED** | 301,685 B body / 303,069 B file | **S-1/A Amendment No. 5**, accession `0000891020-97-000839`, filed 1997-05-14, 2 documents (main doc 299,426 B + EX-23.1 Ernst & Young consent 685 B). Byte-exact to the destroyed `s1a_full.txt` | **T1** | Faster to grep; the final pre-IPO amendment. Verify section headings against the original S-1 above and never conflate their dates |
| `S-1A-No3_acc-0000891020-97-000755_filed-1997-05-09.txt` **RESTORED (new)** | 304,886 B body / 306,425 B file | **S-1/A Amendment No. 3**, accession `0000891020-97-000755`, filed **1997-05-09** — restored because the adversarial dossier's pricing-program sentence is sourced to it (see C-4) | **T1** | Pricing-program / gross-margin strategy statement, present verbatim (see *Re-verified*) |
| `10-K_FY1997_acc-0000891020-98-000448_filed-1998-03-30.txt` **RESTORED** | 606,461 B body / 607,959 B file | Amazon.com annual report for **fiscal 1997**, filed as form type **`10-K405`**, accession `0000891020-98-000448`, period 1997-12-31 (see C-3) | **T1** | First full annual report: revenue growth, book-sales mix, international, category expansion into 1997 — the boundary between Stage 2 and 3 |
| `424B1_final-prospectus_acc-0000891020-97-000868_filed-1997-05-15.txt` **REGISTERED 2026-09-25** | 266,755 B / 35,054 w | Form **424B1**, description "FINAL PROSPECTUS FILED PURSUANT TO RULE 424(B)(1)", accession `0000891020-97-000868`, filed **1997-05-15**, sequence 1 | **T1** | This is the priced final prospectus — the document that carries the **$18.00** price and the **$49,103k** net proceeds. Registered here two days after it arrived, because a primary that is on disk but not in the cache is invisible to the next pass. **§3 lineage:** it is the *same registration statement* as the S-1 original and amendments (File No. 333-23795) — **one source**, so agreement between them is not corroboration; only the differential (what changed between No. 5 and the final) is evidential. Still not in `CORRECTIONS.md` COR-01's list of examined filings: recorded as a conflict at Stage 2 §U rather than patched silently |
| ~~`s1a.txt`~~ — **not restored, deliberately** | 317 B | EDGAR `NoSuchKey` error page | discard | Nothing. Do not cite |
| `sources/s1_graphics/` (dir, 17 artifacts + `INVENTORY.md`) | 0 image bytes | **GRAPHICS RECOVERY — CLEAN NEGATIVE, 2026-09-23 (agent "Graphics Recovery").** EDGAR accession 0000891618-97-001309 and all seven other 1997 Amazon registration filings enumerated by `index.json`, directory HTML, filing-detail page and header `PUBLIC DOCUMENT COUNT` | **T1 as evidence that no image exists; T1 for the bracketed art-plan text** | **There are NO screenshot files to recover.** The S-1 figure caption is not a lost graphic — it is a *printer's art-direction instruction in square brackets*, and it survives in the ASCII. It specifies, with quoted caption lines: the **welcome** page, the **search** page ("targeted searches of over **2.5 million titles**"), the **Amazon.com Journal** page, the **Amazon.com 500** page ("**40% discount** to list price"), the **editors' mailing-list sign-up** page, the **order-finalising** page ("24 hours a day, 7 days a week, worldwide"), plus **warehouse / barcode-scan / fulfilment** photographs and a specimen **e-mail order confirmation** (cover p.3 and p.66 of the S-1/A prospectus). Proof it is empty: original S-1 `PUBLIC DOCUMENT COUNT: 38` = the 38 unnamed directory rows = 38 `<DOCUMENT>` blocks all typed `S-1`/`EX-*`, zero `<TYPE>GRAPHIC`, zero `<img>`, zero `.gif`/`.jpg`, zero binhex/base64, zero non-ASCII bytes; those 38 rows sum to **1,438,356 B** against a **1,444,013 B** complete text file. **What section E may therefore NOT claim:** any recovered 1995-96 screenshot, any pixel-level description of the pages, any date printed "in the page furniture." What it MAY claim: that by **1997-05-09** the company had photographed those seven specific pages and intended them as the prospectus's visual argument. **Accession correction:** the original S-1 is **0000891618-97-001309** (filed 1997-03-24) — the `s1_orig.txt` row above mislabels it as 0000891020-97-000839, which is actually **S-1/A No. 5, filed 1997-05-14, 2 documents**; the caption appears ONLY in the original. Also fixed: 0000891020-97-000755 is an S-1/A of 1997-05-09 with `PUBLIC DOCUMENT COUNT: 4`. Full enumeration, verbatim quotations and the SEC header recipe in `../sources/s1_graphics/INVENTORY.md`. **Do not re-run this retrieval — 15 requests spent to prove an absence.** Residual, unverified: the SEC paper original / microfilm (film 97561192, file 333-23795) would carry the actual images, and five non-prospectus 1997 accessions (8-A12G, S-8, S-8 POS, two 10-Qs, 8-K) were never opened |

Grep these with `-n` and read at offsets; a 1.4 MB filing will not fit a single Read.

## Contemporaneous press and interviews (T1)

| File | Size | Document | Tier | Use for |
|---|---|---|---|---|
| `sheff-playboy-interview_davidsheff-com-jeff-bezos.txt` / `.html` **RESTORED** — **row premise VOID, see C-1** | 50,116 B text / 52,098 B file · 131,785 B html / 133,811 B file | **David Sheff interview of Jeff Bezos — NOT 1994, NOT Wired. The page states: "This interview was conducted in 1999 and published in 2000," and the venue is PLAYBOY** ("Playboy sent Contributing Editor David Sheff…"). Source URL: https://www.davidsheff.com/jeff-bezos | ~~T1~~ **T1 as artifact of 1999/2000; T4 as evidence for 1994** | **CORRECTED 2026-09-23 by agent K; venue+date re-confirmed from the document by the Registrar.** This is **not** a founder-state document from before the outcome; it is retrospective and discusses zShops, a \$22bn valuation and 12 million users. Quote it, but tag every claim `FOUNDER CLAIM (RETROSPECTIVE, 1999)`. Its value for Stage 1: Bezos's only first-person statement about authoring the plan — "I wrote the first draft of the business plan in the car on the way" — and his direct denial of ahead-of-time diversification: "at first, all we knew is that we were going to sell books." See `K_roadmap_provenance.md`. **Nothing was paywalled in this retrieval; the author's own page carries the full ~8,911-word text** |
| `lat.txt` / `lat.html` **STILL-MISSING** | 33 KB / 493 KB | Los Angeles Times, "The Book on Amazon.com" | **T1 artifact, retrospective for Stage 1** — dated **1997-07-20** | **1997, not 1995.** Useful as a contemporaneous account of the *post-Stage-1* company and as a source that may quote earlier material; any Stage-1 claim drawn from it must be tagged `RETROSPECTIVE SOURCE` and corroborated by something dated in-window |
| `ncsa-mosaic-whats-new_1995-08_kitchencloset.html` **RESTORED** | 983,573 B body / 985,639 B file | **NCSA Mosaic "What's New" archive, August 1995** (mirror at kitchencloset.com) | **T1** | The technology environment as it actually stood at launch: browser state, what a 1995 site could assume about visitors. Do not import later browser knowledge into Stage 1. **Restoration adds two verified findings, recorded so nobody re-mines this 984 KB file:** (a) POSITIVE — the August 1995 list carries many commercial web bookstores (Book Stacks Unlimited / books.com, The Bookstore at Houghton Mifflin, Putnam Berkley Bookstore Cafe, Shen's Books, Let There Be Books, Time Warner Electronic Publishing), which supports "Amazon was not first"; (b) NEGATIVE — the page's **only** occurrence of "Amazon" is a Nissan Pathfinder entry about the Amazon **River**, so **Amazon.com is not listed here and this page must never be cited as an appearance by Amazon** |
| `amztimeline.html` **STILL-MISSING** | 122 KB | Archived Amazon timeline page (embedded capture stamp `10/27/2007 8:27:11 AM`) | **T1 as artifact, T4 as claim** `verify` | 2007-era company self-narrative. Useful for what the company was telling people by 2007; not evidence for 1994-95 events without corroboration |

## Company self-description and regional history (T2)

| File | Size | Document | Tier | Use for |
|---|---|---|---|---|
| `historylink-essay-23230_Amazon-The-Early-Years-1995-1999.txt` / `.html` **RESTORED** | 20,086 chars text / 21,399 B file · 52,082 B html / 54,616 B file | **HistoryLink.org Essay 23230, "Amazon: The Early Years (1995–1999)", by Jennie Cecil Moore, posted 2025-04-07** — https://www.historylink.org/File/23230 | **T2** | Washington-state regional history: place, premises, local context, early operations. HistoryLink is a cited-essay resource — chase the footnotes it provides. **Restoration note:** its own Sources list is chiefly Brad Stone (2013) and Brandt (2011), i.e. retrospective books, plus newspaper files — do not cite the essay itself for a Stage-1 fact. Stage-1 details it aggregates (each still needing T1 corroboration): the Bellevue three-bedroom rental and its garage; door-desks from Home Depot; Bezos's $10,000 equity + $84,000 in loans + $150,000 from his parents; the beta site then the move to a small office with a 200-sq-ft warehouse in SODO; soft launch in 1995 with the order bell turned off within weeks; **official launch 16 July 1995**; $12,000 of orders in the first two days; the Yahoo feature; $16M sales in 1996; "Get Big Fast". Publisher licenses the essay text under CC with attribution to HistoryLink.org and the author |
| ~~`wb_amazon.html`~~ **STILL-MISSING — deliberately NOT restored** | 79 KB | Wayback capture of amazon.com — **timestamp read from markup: `2006-05-22 14:39:37`** | **T1 artifact of 2006; worthless as Stage-1 evidence** | A 2006 homepage tells us nothing about the 1995 product. **Gap G-ARCHIVE-1 is RESOLVED AS A NEGATIVE — see `../sources/NULL_RESULT_wayback_1995_1996.md`: no pre-1999 capture exists to substitute.** This 2006 file was therefore not restored, and it must never be used as a stand-in for the 1995 site |

## Reported secondary and leads (T2 / T4)

| File | Size | Document | Tier | Use for |
|---|---|---|---|---|
| `stone.txt` / `stone.html` **STILL-MISSING** | 30 KB / 363 KB | **NBC News excerpt of Brad Stone, *The Everything Store*** | **T2** | The most-cited modern founding narrative. Treat as *one* source: much online Amazon-origin folklore traces to Bezos's own interviews with Stone years later. Label founder-originated retrospective where it is |
| `wiki.txt` **STILL-MISSING** | 76 KB | Wikipedia article on Amazon's history / timeline of Amazon history | **T4** | Lead only. Extract its cited underlying sources and cite those instead; record which |
| `p.html` **STILL-MISSING** | 243 KB | Identified: **Seattle Times, "Amazon at 10: Will it keep clicking?"** (page carries 2005-07-10 and later re-stamp dates) | **T2, retrospective** | 2005 anniversary retrospective. Cites founding-period material; use only to locate underlying sources, never as Stage-1 evidence itself |
| `ddg1.html` **NOT RESTORED (deliberate)** | 14 KB | DuckDuckGo search-results page | discard | Retrieval artifact, not a source |

## Documented null results

A null result is evidence and belongs here, so no later agent burns budget rediscovering it.

- **2026-09-23, Wayback CDX `url=amazon.com`, 1995–1997:** no rows. Earliest capture in the root
  index is **1998-12-12 01:25:32**, and it is a 302 redirect, not a page. `matchType=prefix` with
  `from=1996&to=1996` returned empty. Treat "there is no 1996 homepage capture at the root URL"
  as established *for these queries*; agent J is testing deeper paths and status-code filters
  before the report concludes the artifact record is silent.
  > **SUPERSEDED / CORRECTED by J (2026-09-23).** The bullet above overstates one thing and
  > understates another. The prefix queries did **not** "return empty" — `prefix` +
  > `from=1995&to=1996&filter=statuscode:200`, and the same narrowed to calendar-1996-only and
  > calendar-1997-only, all returned **HTTP 504 Gateway Time-out** and never produced rows. What is
  > actually established is narrower and firmer: **`url=amazon.com/&matchType=exact&from=1994&to=1997`
  > returns `[]`**, the availability API resolves a 1996-06-01 target to **19990828014913**, and
  > Wayback's own nearest-capture resolver sends both a 1995 and a 1996 request to the same
  > **19981212012532** 302. So: **no archived homepage for 1994-1997 — confirmed.** Whether any
  > *deep* `/exec/obidos/` page was crawled in 1996 remains **unanswered by the index**, not answered
  > against. Also note `url=amazon.com` and `url=www.amazon.com` are **not two tests** — the host is
  > normalised out of the CDX urlkey and the queries return byte-identical results. Full query log in
  > `J_archive_artifacts.md`. Do not re-run the fat prefix queries; they will time out again.
  >
  > **Registrar addendum, 2026-09-23 (RD-006 closed as a negative; full log in
  > `../sources/NULL_RESULT_wayback_1995_1996.md`).** J's caveat that the null might be a timeout
  > artefact is now resolved. Two probes succeeded cleanly:
  > **`url=www.amazon.com&matchType=exact&filter=statuscode:200&from=1995&to=1998` returned HTTP 200 with
  > zero bytes — a genuinely empty result set, not a 504**, and the all-status-code exact query over
  > `from=1994&to=1999` returned 22 distinct timestamps in which **every** 1994–1998 row is a 302. The
  > only 200-status root captures in that whole span are **1999-08-28 01:49:13** (`www.amazon.com/?`,
  > 6,544 B) and **1999-10-13 09:18:17** (`amazon.com/`, 6,801 B) — both outside "pre-1999". The
  > availability API returned `{"archived_snapshots": {}}` for 1995, 1996, 1997 **and** 1998.
  > **So: no servable pre-1999 archived Amazon.com page exists at the root — established, no longer
  > inferred.** Still untested per J: arbitrary deep `/exec/obidos/...` paths, because the prefix sweep
  > that would enumerate them cannot complete (504 / curl exit 28, and Internet Archive itself returned a
  > "Temporarily Offline" 503 mid-run). Those timeouts are **upstream capacity failures, not evidence
  > about Amazon** — do not report them as "no captures exist", and do not re-run the broad sweep.

- **2026-09-23, agent K, the 1994 "roadmap"/notebook provenance — rung 1 and rung 2 are EMPTY.**
  `roadmap`, `business plan`, `plan of operations`, `notebook`, `Future of`, `everything store`,
  `Book Net` return **no matches anywhere** in the 1.44 MB S-1 (`s1_orig.txt`) or the 606 KB FY1997
  10-K, and a corpus-wide grep for `road ?map|91.page|page notebook|Future of Computer Stores` found
  **zero hits in every cached file**. Six external searches (facsimile, auction/manuscript sale,
  archive finding aid, exact "91 pages", exact "Future of Computer Stores", earliest "the roadmap")
  returned **only Facebook/Instagram/LinkedIn/SlideShare aggregators** — no repository, no sale, no
  quoted line. **Do not re-run these; they are spent.** The ladder tops out at rung 3: LA Times
  **1997-07-20** ("pecked out a business plan on his laptop") and Sheff **1999** ("I wrote the first
  draft of the business plan in the car on the way"). See `K_roadmap_provenance.md`.
- **Not the same document:** Brandt's *One Click* is **Portfolio/Penguin 2011**, not 1999 — there is
  no pre-2011 close secondary account to mine, and the 2011 text was never read (Scribd shell only).
- **`p.html` and `amztimeline.html` were already gone before the purge** — K could not read the 2005
  Seattle Times or the 2007 company timeline, so K's corpus null deliberately excludes them.
- **Open lead K could not reach (budget):** the two in-window Amazon press releases J added below
  carry Bezos speaking in **1995 and 1996 in his own contemporary words**. If any contemporary
  statement about how the business was planned exists, that is where to look next — it is the only
  route left to a genuine rung-3 CONTEMPORARY entry.

## Archive status of the 1995-96 site — RESOLVED
**Gap G-ARCHIVE-1 is closed.** No in-window archived Amazon.com page exists in the Wayback Machine,
and none was found in any other archive in this pass; every circulating "Amazon 1996 screenshot"
source is Tier 4 with no verifiable timestamp. Section E is therefore written from dated in-window
documentary evidence instead. See `J_archive_artifacts.md` (verdict, query log, inventory).

## Two IN-WINDOW primary product artifacts (added by J — highest value for Stage 1)
These are not local files; they are durable company URLs dated inside 1995-1996. They outrank every
retrospective source in this cache for describing the live product.

| Source | Document | Tier | Use for |
|---|---|---|---|
| [press.aboutamazon.com/1995/10/...worlds-largest-bookseller-opens-on-the-web](https://press.aboutamazon.com/1995/10/worlds-largest-bookseller-opens-on-the-web) | Amazon press release **"World's Largest Bookseller Opens on the Web"**, **1995-10-04** | **T1, in-window** | The live site as the company described it three months after launch: `http://www.amazon.com/`, "more than one million different titles", the search engine as the core feature, online ordering with UPS/Airborne Express delivery, "discounts all but the most obscure titles 10-40 percent from the list price", readers sharing thoughts on books, 45+ countries in four weeks, and a Bezos quote in his own contemporary words. **Fetch and save the HTML — J only captured a summarised extract** |
| [press.aboutamazon.com/1996/6/...shopping-for-books-on-the-internet](https://press.aboutamazon.com/1996/6/shopping-for-books-on-the-internet-isnt-just-for-tech-buyers-anymore-amazon-com-worlds-largest-bookseller-tracks-whos-buying-online) | Amazon press release, **1996-06-14** (index lists 06-13) | **T1, in-window** | Mid-window feature enumeration: "catalogue of 1.1 million titles", "easy online ordering", "easy-to-use search and browse features, email services, Web-based credit card payment and direct shipping to customers", customers from 95+ countries. **The 1.1M figure is the one to use for 1996 — not the filings' 2.5M, which is 1997** |

**The company's press archive is indexed by year and was only sampled at two dates.** Almost
certainly more 1995-96 releases exist (launch day, Associates Program, category and holiday-season
announcements). This is the best remaining place to find in-window product evidence — treat as an
open, high-yield lead.

## TOP UNREAD LEAD for Stage 1 (found by J, not yet read — J's budget ran out here)
**Fortune, "Amazon: The Next Big Thing Is a Bookstore?", 9 December 1996** —
https://fortune.com/1996/12/09/amazon-bookstore-next-big-thing/
A mainstream in-window feature published three weeks before the S-1's 31 December 1996 measurement
date, i.e. describing the end-of-window product. Existence and date are confirmed from the URL path
and search index; **its contents are unknown to this dossier and must not be cited until read.**
Read it for verbatim homepage copy, the search form's field labels, how an order completes, price
display, the on-screen catalog number, and which features the author notes are absent. This is the
single highest-value remaining action for section E — see `J_archive_artifacts.md` J-46.
Secondary lead: a claimed October 1996 *Fast Company* piece, traced only to a blog post (Tier 4);
locate it in the magazine or discard.

## Workspace warning — SUPERSEDED 2026-09-23 by the restoration
`_scratch/` was **purged by the pipeline mid-session on 2026-09-23**. The local copies of
`s1_orig.txt`, `amzn10k1997.txt`, `lat.txt`, `hl.txt`, `wb_amazon.html` and the `cdx_*.txt` outputs
referred to throughout this cache and in `J_archive_artifacts.md` were **no longer on disk**.

**Status now:** the primary documents are **back on disk in `../sources/`** with provenance headers, and
the S-1 / Amendment No. 3 / Amendment No. 5 / FY1997 10-K405 are all re-greppable (see the Restoration
map). Two parts of the old warning still hold and must not be forgotten: (1) `lat`, `stone`, `wiki`,
`p.html`, `amztimeline` and `wb_amazon` remain **STILL-MISSING**, and (2) **every line-number reference
into `_scratch` is dangling** — the restored files carry different byte offsets, so re-locate any quoted
passage by grep, never by remembered line number.

**Grep/URL recipe so nobody re-derives it:** SEC rejects any request without a declared contact
(`403 Your Request Originates from an Undeclared Automated Tool` — the two 4,819-byte `idx.html` /
`idx.json` files still sitting in `../sources/` are exactly that error page, not a source). Send
`User-Agent: FounderPlaybook Research AdminContact@example.com`, `Accept-Encoding: gzip, deflate`,
`Referer: https://www.sec.gov/`, and **negotiate decoding** — EDGAR returns `Content-Encoding: gzip`,
so a raw save is a binary blob. `data.sec.gov` also 503s intermittently and `www.sec.gov` briefly served
a genuine `503 File Unavailable` during this restoration: **retry before concluding a path is blocked.**
Amazon's pre-2000 filings are *not* in the main submissions JSON (2021+ only) — use
`https://data.sec.gov/submissions/CIK0001018724-submissions-002.json` (1997-03-24 → 2000-01-04).
Legacy 1997 `index.json` and directory listings **blank the document names**, so the reliable artifact is
the accession's `<accession>.txt` complete submission file.

## Corrections from the Stage-1 TECHNOLOGY agent (`F_technology.md`)

1. **The S-1 accession in the table above is the amendment, not the original.** `0000891020-97-000839`
   has EDGAR header `CONFORMED SUBMISSION TYPE: S-1/A`, `PUBLIC DOCUMENT COUNT: 2`,
   `FILED AS OF DATE: 19970514` — and it is the 299 KB file now restored to `../sources/`. The 1.44 MB
   full text read by the Technology agent was the **original Form S-1, accession 0000891618-97-001309,
   38 documents, filed 1997-03-24, SEC File No. 333-23795**. Both are legitimate Stage-1 sources; cite
   them separately and never conflate their dates. The S-1/A **independently corroborates** the T1/ISP
   connectivity, the non-integrated accounting, the nine customer-service e-mail addresses and the
   proprietary order-splitting software, so those disclosures now rest on two filings (F-86, F-87).
2. **Gap G-ARCHIVE-1 is worse than "not in the cache" — it is not in the Archive.** CDX-verified: the
   earliest capture of amazon.com's **root** anywhere in the Wayback index is **1998-12-12 01:25:32**, and
   probes aimed at 1995-08, 1996-01, 1996-05, 1996-10 and 1997-01 all 302-redirect to that same capture.
   The frequently-circulated `web/19960520121525/http://www.amazon.com/` URL silently lands on the
   **2006-05-22** page — which is how a large body of Tier-4 "Amazon's 1996 website" writing got
   published. Do not write Section E from an imagined homepage screenshot; write it from the S-1's
   functional description plus the 1997-07-20 LA Times walkthrough, labeled accordingly. One caveat left
   open: CDX `matchType=prefix` queries for 1996 deep links failed (HTTP 000/504, including a known-good
   1999 control), so whether any 1996 **sub-page** survives is untested, not answered. (F-38, F-88.)
3. **`ncsa.html` is confirmed correctly dated and is the highest-value surviving environment artifact** —
   "What's New With NCSA Mosaic: Archives for August 1995," 12 dated listings from 2 to 30 August 1995,
   **3,084 site entries** total. It contains listings for merchant-acquiring services ("Become a credit
   card merchant ... build an online form") and for Sun's Internet Commerce Group, but **no card-security
   or crypto vendor at all** — a real bound on the 1995 payments environment, not a search failure. (F-71
   … F-74.)
4. **Two Stage-1 questions are hard UNKNOWNs, not under-administered ones.** No Tier-1/2/3 document found
   names a programming language, OS, database or server for the 1995 system, and none names Amazon's
   bibliographic data vendor (the *Books in Print* attribution is Tier-4 folklore). The S-1's own wording
   is the ceiling: "licenses some of its catalog and other information from third parties." Record these
   as UNKNOWN rather than importing a listicle. (F-82, and the Data gaps table.)
5. **New name for the staffing files:** **Peri Hartman** appears as lead named inventor on US 5,960,411
   (filed 1997-09-12) alongside Bezos, **Shel Kaphan** and **Joel Spiegel**, but is absent from every
   Stage-1 document here and from the S-1 officer list — a probable undocumented engineer, and a lead
   worth chasing in the 1997-99 personnel work. Kaphan's inventorship is the one non-recollection
   corroboration that he authored Amazon's ordering systems. (F-80, F-80a.)

## End of Stage-1 technology corrections

## Rules of use

1. **Cite the document, not the file.** A cache entry's citation is the underlying publication
   plus a stable URL (EDGAR accession, newspaper archive link, wayback URL). Local paths are
   provenance support, recorded in the `archived` field.
2. **Extract dates before use.** Any entry marked `date?` must have its publication date read
   out of its own text; an undated source cannot carry a High-confidence claim.
   **C-1 is what happens when this rule is assumed rather than applied** — the Sheff row carried a
   confident "1994 / Wired" attribution that the document itself contradicts, and three stages of
   dossiers quoted it on that strength.
3. **Do not double-count.** Several agents may each quote the Sheff interview (formerly
   `sheff.txt`). In `sources.csv` that is **one** source with multiple claim linkages, not corroboration.
   Likewise the pricing-program sentence now sits in **three** restored accessions: one quotation, three
   witnesses to the same text — not three sources.
4. **Stage 2 and Stage 3 inherit this cache.** Add rows here as new documents land; never let a
   fetched document live only in `_scratch` where the next agent cannot find it.
5. **NEVER delete, move, empty or "tidy" anything in `../sources/`.** Create files, or amend this
   cache. The 2026-09-23 incident happened because a folder nobody owned was treated as trash; the
   restoration cost a full re-fetch of ~2.7 MB of filings and re-verification of every quotation.
6. **Every file in `../sources/` must open with a provenance header block** — retrieval URL, access date,
   accession or publication date, byte size, and completeness. A file without one has no citable
   provenance.

### Integrity note on `../sources/` as of 2026-09-23 (restoration pass)

The archive also holds files the Registrar did **not** write, and **none of them were deleted, moved or
tidied** — that is precisely the failure being repaired. Later agents should know:

- `idx.html` and `idx.json` (4,819 B each) are SEC **403 "Your Request Originates from an Undeclared
  Automated Tool"** error pages from the failed pre-restoration attempt. **Not sources; do not cite.**
  They survive as the diagnostic that the earlier failure was a missing `User-Agent` contact, not an SEC
  block.
- `s1_original_0000891618-97-001309.txt` and `s1_0000891020-97-000839.txt` are **unheadered** copies that
  `cmp` confirms are **byte-identical to the EDGAR bodies** the Registrar restored. That is welcome
  independent corroboration of reproducibility, but cite the **headered** filenames in the tables above —
  only those carry provenance.
- `s1_graphics/` is the parallel Level-3 Graphics Recovery agent's working folder inside the archive
  (18 items: `INVENTORY.md` plus EDGAR index/header scratch dumps). Its conclusion is already folded into
  the Filings table. It is that agent's output, not trash; leave it in place.

## THE LINE-KEYING RULE FOR `l.NNNN` — declared (AUDIT-2 DEFECT-6 repair, 2026-09-25)

**Read this before auditing or converting any `l.NNNN` reference in Stage 1, Stage 2 or their registers. Two
local copies of two accessions exist, and a future auditor who greps the wrong one will report roughly 900
phantom citation failures.**

**Rule.** Every `l.NNNN` / `ll.NNNN–NNNN` / `LNNNN` reference in the Stage-2 spine (`stage_2_part_1/2/3.md`,
`stage_2_claim_records.md`, `stage_2_claim_records_part_2.md`) and in the registers is a line of the
**convention-named, headered copy**: `sources/<FORM>_acc-<ACCN>_filed-<DATE>.txt`. The financial spine keys to
those same headered files. No Stage-2 reference resolves against a bare-named twin.

| Document cited | **KEY — cite this file** (headered) | Duplicate twin, on disk, NOT keyed | Lines key / twin | Δ |
|---|---|---|---|---|
| S-1 original, acc. 0000891618-97-001309 (1997-03-24) | `S-1_original_acc-0000891618-97-001309_filed-1997-03-24.txt` | `s1_original_0000891618-97-001309.txt` | 27,476 / 27,459 | **17** |
| S-1/A No. 5, acc. 0000891020-97-000839 (1997-05-14) | `S-1A-No5_acc-0000891020-97-000839_filed-1997-05-14.txt` | `s1_0000891020-97-000839.txt` | 5,120 / 5,103 | **17** |

**The offset is a constant 17 lines**, and it is exactly the Level-3 Registrar's `PROVENANCE HEADER` block: 17
physical lines of `=`-fenced provenance text sit above the first body line (`-----BEGIN PRIVACY-ENHANCED
MESSAGE-----`) in the headered copy and above nothing in the twin. It is also the byte difference:
1,445,709 − 1,444,013 = 1,696 B and 303,069 − 301,685 = 1,384 B, both attributable to that header.
**Conversion is therefore exact and directional: `twin line = keyed line − 17`, `keyed line = twin line + 17`.**

Verified probes (both directions, re-run 2026-09-25 with `grep -n`, not inherited from the audit sheet):

| Probe text | keyed copy | twin | Δ |
|---|---|---|---|
| `expanded from 11 to 151` (S-1 orig.) | **l.667** | l.650 | 17 |
| `Mr. Lipsky served` (S-1 orig.) | **l.2510** | l.2493 | 17 |
| `expanded from 11 to 256` (No. 5) | **l.796** | l.779 | 17 |
| `Mr. Lipsky served` (No. 5) | **l.2728** | l.2711 | 17 |

**Four more accessions are also duplicated on disk** by the Stage-3 intake's naming slip —
`S-1A_No1/2/4/6_acc-…_filed-….txt` (underscore) beside the convention-correct
`S-1A-No1/2/4/6_acc-…_filed-….txt` (hyphen). Those pairs are **byte-identical** (see the duplicate-file notice
in the Stage-3 intake section below and §8 of `../sources/STAGE3_INTAKE_MANIFEST.md`), so they carry **no
offset**: cite the hyphenated form, which is the one the Stage-2 spine uses, and expect a grep of the
underscore form to return the same line numbers.

**Nothing was deleted, moved or merged here (method §14 rule 4).** The twins are reproducibility evidence and
stay on disk; what was missing was the keying declaration, which is it. One document is never two sources, and
one document at two line numbers is never two witnesses.

## Additions by agent H (legal / IP / organization) — 2026-09-23, purely additive

C-2 (accession), C-1 (Sheff = **Playboy, conducted 1999, published 2000**) and the two in-window press
releases are already handled above; not repeated. New material only.

**Stage-1 corporate instruments now located in the ORIGINAL S-1 exhibit index (they exist only in
`0000891618-97-001309`, not in any amendment):**

| Exhibit | Instrument | Date |
|---|---|---|
| 2.1 | Agreement and Plan of Merger — "the Registrant, **a Washington corporation**, and Amazon.com, Inc., a Delaware corporation" | 1996-05-28 |
| 10.12 | Subscription: "**Cadabra, Inc., a Washington corporation**", 1,700,000 shares / $10,000, Bezos as a Washington resident, with restrictive legend + stop-transfer order | 1994-07-05 |
| 10.13 / 10.14 / 10.15 / 10.16 | Shareholder's Agreements — M. A. Bezos / Gise Family Trust / **Sheldon J. Kaphan** / **Tom A. Alberg** | 1995-02-09 / 07-24 / 08-08 / 11-26 |
| 10.20 / 10.22 | "**1994** Stock Option Plan" (amended & restated) and Kaphan's **Incentive** Stock Option Letter Agreement effective **1994-10-24** — earliest equity paper of the firm | 1994 |
| 10.23 / 10.24 | Alberg non-qualified option letters (60,000 @ $0.3333; 60,000 @ $0.6666) | 1995-12-06 |

**⚠ Documentary trap that will bite any chronology agent:** Exhibit 10.13 carries the execution date
**February 9, 1995** but recites the company as "**Amazon.com, Inc. … a Delaware corporation**" —
impossible before the May/June 1996 reincorporation, and flatly contradicted by Exhibit 10.12 in the
same exhibit set. The 1995 agreements were conformed to the later corporate form before filing. Do not
date the name change, or Delaware, from that preamble. (Full treatment: `H_legal_organization.md`
H-36 and Contradiction C-H1.)

**New Tier-1 sources outside EDGAR (durable URLs, retrieved and read):**

| Source | URL | Carries |
|---|---|---|
| USPTO TSDR, Serial 75008413, mark AMAZON | https://tsdr.uspto.gov/statusview/sn75008413 | Application **filed 1995-10-23** (in-window), Cl. 042 "computerized on line ordering service featuring the [wholesale and] retail distribution of books", Principal Register, Reg. 2078496 issued 1997-07-15, **no opposition and no cancellation** in the file (only 2020+ suit notifications). The closest dated public anchor for the Amazon name |
| Amazon press release, 1995-10-04 | https://press.aboutamazon.com/1995/10/worlds-largest-bookseller-opens-on-the-web | "Amazon.com, the business and domain name…"; **Bezos titled President, not CEO** — corroborates the S-1 (CEO only from May 1996). J asked someone to save the HTML; H read the text only, no local copy |
| 47 U.S.C. § 230 credit line | https://www.law.cornell.edu/uscode/text/47/230 | "as added Pub. L. 104–104, title V, § 509, **Feb. 8, 1996**, 110 Stat. 137" — Section 230's enactment date, settled |
| Federal Register 96-33030 (BIS, Commerce) | https://www.govinfo.gov/content/pkg/FR-1996-12-30/html/96-33030.htm | Cryptographic commodities/software moved **USML→CCL effective 1996-12-30**, after the 1996-11-15 directives. **Route note: `federalregister.gov/documents/...` 302s to `unblock.federalregister.gov/` and yields nothing — go straight to the `govinfo.gov/content/pkg/FR-<date>/html/<doc>.htm` form** |

**New documented nulls — do not re-spend budget on these:**
- `scholarship.law.unc.edu` full text → **HTTP 403**. The case name *Amazon.com v. N.Y. State Dept. of
  Taxation & Finance* came from a **search-result title only** and is unverified: no date, court, docket
  or outcome is asserted in the Stage-1 dossiers. Use a court-record route if the NY matter is needed.
- Original S-1 **and** Amendment No. 5, full text: **"Cadamia" = 0 hits; "Cadabra" = exactly 1 hit
  (Ex.10.12); "changed its name" / "renamed" / "formerly known as" = 0 hits.** The filings contain no
  name-change statement at all — the change is datable only by bounding instruments.
- **`Davis` (Paul Davis) = 0 hits in both S-1 texts.** Not filing-provable. And every officer bio except
  Bezos and Kaphan joins **1996-07 or later**, so the filings cannot supply the Stage-1 roster beyond
  two names.
- Searches on the 1994-96 name change return only Tier-4 aggregators (Reddit, Quora, Fandom, ITV
  listicles) plus post-2008 state "Amazon law" material — nothing in-window. Considered spent.
- **1996-12-31 headcount conflicts across filings: 151 (S-1, "full-time") vs 158 (FY1996 annual report).**
  Both Tier 1; report both with their definitions, never a merged figure.
- Bezos's post-IPO stake differs between the two filings (**43%** in the original S-1, **41%** in
  Amendment No. 5) — same risk factor, seven weeks apart. Quote with the accession date attached.

**Open lead H could not reach (budget exhausted):** the **Washington Secretary of State** entity file for
Cadabra, Inc. → Amazon.com, Inc. is the only authority that could date the name change; prior agents
could not connect (`corqs.access.wa.gov` failed, OpenCorporates 401 — see the retrieval-failure table in
`A_corporate_historian.md`). Second: **Peri Hartman** (agent F, item 5) and the 1995-96 press-release
archive, still sampled at only two dates.

---

# Stage-3 intake — the post-IPO filing set (appended 2026-09-25 by the Stage-3 Evidence Registrar)

**What landed here:** the whole EDGAR record for CIK 1018724 from the IPO to the end of 1999 that was not
already on disk — **75 complete submissions, 10,102,329 bytes, ~1,340,000 words**, each saved under the
existing naming convention with its own provenance header. Every one of the Stage-1/2 "UNTRIED" items is now
local: the FY1998 10-K, all eight 1997-99 10-Qs, both DEF 14As, the 1997-99 8-K run, the S-8s and S-8 POSs,
the 8-A12G, and registration Amendments Nos. 1, 2, 4 and 6.

Enumeration source: `https://data.sec.gov/submissions/CIK0001018724-submissions-002.json` — 125 filings,
1997-03-24 → 2000-01-04. **All 125 rows were enumerated; 75 were fetched; 45 were deliberately not fetched;
5 were already on disk.** Nothing in that catalogue returned an error to this pass, so nothing below is
"unreachable" — where a document is missing it is missing by choice or is recorded as a gap, and
**"not retrieved" never means "does not exist"**. Full accounting: `../sources/STAGE3_INTAKE_MANIFEST.md`.

> **RECIPE CORRECTION — read before spending a request.** The complete-submission file for a legacy filing is
> named with the **dashed** accession:
> `https://www.sec.gov/Archives/edgar/data/1018724/0000891020-99-000375.txt`.
> The de-dashed form (`…/000089102099000375.txt`) is the **directory** name, not the file name, and returns
> **404 for every one of Amazon's 1997-99 accessions**. This pass burned 150 zero-byte 404s rediscovering
> that; the correct form is already printed in the `Original URL` line of every restored header. Keep
> `Accept-Encoding: identity` (EDGAR will still serve `Content-Length` uncompressed, so no decode step is
> needed) and the declared `User-Agent: FounderPlaybook Research AdminContact@example.com`.

**Identity verification, 2026-09-25:** for all 75 files the in-file `SEC-HEADER` fields `ACCESSION NUMBER`,
`CONFORMED SUBMISSION TYPE` and `FILED AS OF DATE` were machine-compared with the submission index —
**75/75 agree, zero mismatches.** The AMENDMENT NO. printed inside each S-1/A body also agrees with EDGAR's
ordinal for Nos. 1, 2, 4 and 6 (so C-4's off-by-one is now bounded to the accession pair it named).

**Two Stage-2 UNKNOWNs moved by this intake — one resolved, one resolved-as-silent:**
- **Founder compensation is now on disk.** The 1998 proxy carries the FY1997 Summary Compensation Table and
  the 1999 proxy carries FY1996-98: **Bezos's salary was $64,333 (1996) → $79,197 (1997) → $81,840 (1998),
  with no bonus and no stock options granted in any of the three years.**
- **The personal-guarantee release is NOT in any filing in this window — and that is now proven, not
  assumed.** The FY1998 10-K's Item 13 defers to the 1999 proxy; the 1999 proxy's "Certain Transactions"
  contains only the $75,000 Dalzell loan (repaid 1998-10-23); the 1998 proxy's contains only the
  Cook/Stonesifer Series A purchases and the same loan; the FY1997 10-K never names Seafirst or a Bezos
  guarantee. A corpus scan of all 80 archived filings for "Seafirst" / "Wells Fargo" / "Bezos … guarantee" /
  "release … guarantee" returns hits **only in the 1997 registration lineage** (the S-1, its amendments and
  the 424B1) and never after 1997-05-15, except one lease clause quoting Seafirst's prime rate. The only
  in-filing statement of the release remains the S-1's forward-looking undertaking, "The Company intends to
  secure releases of all of Mr. Bezos' guarantees as soon as possible following the closing of this
  offering." Its completion is evidenced **nowhere in the SEC record** — keep it UNKNOWN, now with the
  searches recorded.

**The "merchant-account exhibits at S-1 (orig.) l.18509 were cited and never opened" gap is a READING gap,
not a retrieval gap, and it partly dissolves.** That line range is `EX-10.27 SUBROGATION AGREEMENT DATED
JUNE 19, 1996` (Bezos ↔ Amazon.com, Inc., l.18487-18622 of the file already on disk) — the complete
submission contains all 38 exhibit bodies inline, so nothing needed fetching. But **no merchant-services or
bank agreement is itself in the exhibit set**: the S-1's 38 documents run EX-2.1 … EX-27.1 and the only
bank-facing instrument filed is the Subrogation Agreement (Bezos's recourse against Amazon if he has to pay;
recital B names the Wells Fargo and Seafirst guarantees). The guarantees were never filed, so no amount can
ever be extracted from EDGAR.

## Annual and quarterly reports — the periodic spine (9)

| File | Size | Document | Tier | Use for |
|---|---|---|---|---|
| `10-K_FY1998_acc-0000891020-99-000375_filed-1999-03-05.txt` | 321,454 B / 41,642 w | Form **10-K**, accession `0000891020-99-000375`, filed **1999-03-05**, period **1998-12-31**, 5 documents | **T1** | **The first full post-IPO year on a filed basis** — the anchor of Stage 3. Selected financial data: net sales **$609,996k (1998) / $147,787k (1997) / $15,746k (1996) / $511k (1995)**; accumulated deficit **$162.1M**; ~$349M senior indebtedness at 12/31/98. Part III Items 11/12/13 **defer to the 1999 proxy** (meeting 1999-05-20). EX-21.1 list of subsidiaries = the corporate footprint of category and country expansion; EX-10.13 lease of 1998-12-14; Year 2000 section |
| `10-Q_Q2-1997_acc-0000891020-97-001148_filed-1997-08-14.txt` | 67,658 B / 6,702 w | Form **10-Q**, accession `0000891020-97-001148`, filed **1997-08-14**, period **1997-06-30**, 6 documents | **T1** | The **first post-IPO reported quarter**: net sales $27,855k for the quarter vs $2,230k a year earlier ($43,860k / $3,105k six months). Small enough to read whole. Cites the Registration Statement No. 333-23795 and the prospectus dated May 15, 1997 — the §3 lineage link between Stage 2 and Stage 3 filings |
| `10-Q_Q3-1997_acc-0000891020-97-001466_filed-1997-11-14.txt` | 198,200 B / 26,193 w | Form **10-Q**, accession `0000891020-97-001466`, filed **1997-11-14**, period **1997-09-30**, 6 documents | **T1** | Q3 1997 plus the pivot from equity to **debt**: "On November 7, 1997, the Company entered into a commitment letter for a **$75 million three year senior secured term credit facility** … with Deutsche Bank AG, New York Branch … as administrative agent and Deutsche Morgan Grenfell, Inc. … as arranger … may be increased to … $100 million". Read with the 8-K of 1997-11-10 |
| `10-Q_Q1-1998_acc-0000891020-98-000846_filed-1998-05-15.txt` | 835,834 B / 121,363 w | Form **10-Q**, accession `0000891020-98-000846`, filed **1998-05-15**, period **1998-03-31**, 9 documents | **T1** | The biggest 10-Q in the set because its exhibits **are the leverage story**: EX-4.1 indenture with Bank of New York as trustee, EX-4.2 form of **10% Senior Discount Note due 2008**, EX-4.3 registration rights agreement, plus two leases. Sales through 3/31/98 "more than $251 million to approximately 2.3 million customer accounts in over 150 countries"; accumulated deficit $42.9M at that date |
| `10-Q_Q2-1998_acc-0000891020-98-001313_filed-1998-08-14.txt` | 202,784 B / 25,762 w | Form **10-Q**, accession `0000891020-98-001313`, filed **1998-08-14**, period **1998-06-30**, 4 documents | **T1** | Q2 1998; EX-10.1/10.2 lease amendments and a new lease dated 1998-07-21 — the physical scaling behind the numbers (compare the $367M cumulative-sales and 3.1M-account figures in the 424B2) |
| `10-Q_Q3-1998_acc-0000891020-98-001632_filed-1998-11-13.txt` | 381,905 B / 53,069 w | Form **10-Q**, accession `0000891020-98-001632`, filed **1998-11-13**, period **1998-09-30**, 3 documents | **T1** | The music/video launch quarter as filed, including the acquisition accounting for Junglee/PlanetAll; EX-10.1 lease with WRC.com Tower LLC |
| `10-Q_Q1-1999_acc-0000891020-99-000894_filed-1999-05-17.txt` | 603,255 B / 84,809 w | Form **10-Q**, accession `0000891020-99-000894`, filed **1999-05-17**, period **1999-03-31**, 8 documents | **T1** | ~~Five separate "SALES AGREEMENT, DATED MARCH 11, 1999" exhibits (EX-10.1 … 10.5) — the contractual trace of the marketplace model~~ **CORRECTED 2026-09-25 — this row's reading was wrong, and two dossiers disproved it independently.** The five exhibits are **materials-handling EQUIPMENT purchase contracts**: Amazon.com is the *Purchaser*, **The Buschman Company** (Ohio; affiliate of Pinnacle Automation) the *Seller* of Equipment and Work — EX-10.1 Fernley Phase I (proposal 1999-01-18), EX-10.2 Fernley Phase II (1999-02-05), EX-10.3–10.5 Standard Proposal 1999-02-05 for "Site A/B/C" **yet to be determined**, with prices redacted under **Rule 24b-2**. They are evidence of a **build-out in progress**, not of third-party selling. The marketplace's real documentary trace is elsewhere: **8-K 1999-03-30** and **10-Q Q3-1999** L801–806, L1463–64, L1859–68 ("zShops … enables anyone to offer merchandise for sale on Amazon.com"; "we do not take responsibility for delivery of payment or goods"; commissions **inside net sales**). EX-10.6 lease of 1999-04-12. Source: `ST3_A` COR-101 + `ST3_C` OC-2 — **a claim this cache asserted before anyone read the exhibits, then repeated into two agent briefs.**
| `10-Q_Q2-1999_acc-0000891020-99-001426_filed-1999-08-16.txt` | 125,100 B / 15,108 w | Form **10-Q**, accession `0000891020-99-001426`, filed **1999-08-16**, period **1999-06-30**, 3 documents | **T1** | Q2 1999 (10.7 million customers per the 8-K of 1999-07-22). EX-10.1 is the **Offer Letter of Employment to Joseph Galli** — a filed post-IPO executive hiring package, the only one in the set, and the same "J. Galli Jr." who signs the POS AM powers of attorney |
| `10-Q_Q3-1999_acc-0000891020-99-001938_filed-1999-11-15.txt` | 176,570 B / 22,324 w | Form **10-Q**, accession `0000891020-99-001938`, filed **1999-11-15**, period **1999-09-30**, 3 documents | **T1** | Q3 1999 as filed; EX-10.1 re-files the **1997 Stock Option Plan** (the dilution instrument being amended in the open market). Toys/electronics/zShops quarter per the 1999-10-28 8-K |

## Proxies, shareholder letters and founder ownership — Part III and the money the founder took (8)

| File | Size | Document | Tier | Use for |
|---|---|---|---|---|
| `DEF14A_1998-proxy-statement_acc-0000891020-98-000601_filed-1998-04-17.txt` | 61,828 B / 8,127 w | Form **DEF 14A**, accession `0000891020-98-000601`, filed **1998-04-17**, meeting **1998-05-28** | **T1** | **The 1998 proxy the FY1997 10-K405 defers to for Part III.** Summary Compensation Table for 1997 with 1996 comparatives: **Bezos, President and CEO, $79,197 (1997) / $64,333 (1996), no bonus, no options, no other compensation**; the first post-IPO officer roster (Aposporos, Dalzell, Duenas, Kaphan, Spiegel) with their **start dates** (May 9 / Sept 2 / Jan 8 / Mar 17, 1997) — the personnel-boundary evidence Stage 1 needed. "Certain Transactions": 2,500 Series A shares at **$40.00** each to Cook and to Stonesifer, and the **$75,000 no-interest Dalzell relocation loan**. Board met 8 times in 1997, Audit Committee 4. **Silent on the personal guarantees** |
| `DEF14A_1999-proxy-statement_acc-0000891020-99-000635_filed-1999-04-07.txt` | 65,778 B / 8,592 w | Form **DEF 14A**, accession `0000891020-99-000635`, filed **1999-04-07**, meeting **1999-05-20** | **T1** | The FY1998 Part III. Three-year table: **Bezos $81,840 (1998), 79,197 (1997), 64,333 (1996) — zero bonus and zero options in all three years**, against Dalzell $201,512 and Aposporos $142,083: by 1998 the founder was paid **less than four of his own VPs**. Option counts are restated for the 3-for-1 split of 1999-01-04, so they are **not comparable** to the 1998 proxy's pre-split numbers (Dalzell's 1997 grant appears as 125,000 then 750,000). Agenda: increase in authorized shares. **Still silent on the guarantees** |
| `PRE14A_1998-preliminary-proxy_acc-0000891020-98-000720_filed-1998-05-05.txt` | 62,680 B / 8,160 w | Form **PRE 14A**, accession `0000891020-98-000720`, filed **1998-05-05**, meeting 1998-05-28 | **T1** | Preliminary version of the 1998 proxy — use only to diff against the definitive text and to date what was added or removed. Not a second source for the same numbers (§3 lineage rule) |
| `PRE14A_1999-preliminary-proxy_acc-0000891020-99-000439_filed-1999-03-15.txt` | 65,048 B / 8,512 w | Form **PRE 14A**, accession `0000891020-99-000439`, filed **1999-03-15**, meeting 1999-05-20 | **T1** | As above for the 1999 proxy |
| `ARS_1997-annual-report-to-shareholders_acc-0000891020-98-000600_filed-1998-04-17.txt` | 14,188 B / 1,807 w | Form **ARS**, accession `0000891020-98-000600`, filed **1998-04-17**, period **1997-12-31**, description "AMAZON.COM 1997 ANNUAL REPORT" | **T1 (founder-state, contemporary)** | **The 1997 shareholder letter in the company's own words** — "Amazon.com passed many milestones in 1997: by year-end, we had served more than 1.5 million customers, yielding **838% revenue growth to $147.8 million**, and extended our market leadership despite aggressive competitive entry. **But this is Day 1 for the Internet and, if we execute well, for Amazon.com.**" This is the in-window, dated, filed source for the "Day 1" posture that Stage 1 and 2 had only from retrospective interviews. Quote with the 1998-04-17 filing date attached |
| `ARS_1998-annual-report-to-shareholders_acc-0000891020-99-000637_filed-1999-04-07.txt` | 26,009 B / 3,624 w | Form **ARS**, accession `0000891020-99-000637`, filed **1999-04-07**, period **1998-12-31**, description "1998 ANNUAL REPORT" | **T1 (founder-state, contemporary)** | The 1998 letter, verbatim: "We've served a cumulative **6.2 million customers**, exited 1998 with a **$1 billion revenue run rate**, launched music, video, and gift stores in the U.S., opened shop in the U.K. and Germany, and, just recently, launched Amazon.com Auctions. **We predict the next 3 1/2 years will be even more exciting.**" The forward-looking self-description Stage 3 needs at the moment of maximum re-profilability |
| `SC13G_jeffrey-bezos_acc-0000891020-98-000175_filed-1998-02-17.txt` | 10,894 B / 914 w | Form **SC 13G**, accession `0000891020-98-000175`, filed **1998-02-17**, description "SCHEDULE 13G FOR JEFFREY BEZOS" | **T1** | **Bezos's own post-IPO stake, self-reported nine months after the offering: 9,885,000 shares** — the same figure the S-1's registration-rights paragraph uses. Fixes the founder-equity line for the FY1997→FY1998 boundary without inference from percentages |
| `SC13G_jacklyn-gise-bezos-miguel-bezos_acc-0000891020-98-000174_filed-1998-02-13.txt` | 18,625 B / 1,671 w | Form **SC 13G**, accession `0000891020-98-000174`, filed **1998-02-13**, description "SCHEDULE 13G FOR JACKLYN GISE BEZOS & MIGUEL BEZOS" | **T1** | **CORRECTED 2026-09-25 (`ST3_A` COR-102):** the form's own Item 2 states Jacklyn Gise Bezos and Miguel A. Bezos are **spouses of each other** and the founder's **parents** — not "spouse and brother", as this row and my dispatch brief both said. The family-side holdings, four days earlier than the founder's own row. **Do not aggregate with the Bezos row without checking for shared beneficial ownership** — the forms' own item 3/4 attribution governs |

## Current reports — the dated event record, 1997-11 → 1999-10 (26)

**All 25 Forms 8-K (1997-11-10 through 1999-10-28) plus the single Form 8-K/A — the entire current-report
record of the window, including the 1997-11-10 8-K Stage 2 listed as UNTRIED.** Each row cites the index
`form` / `accessionNumber` / `filingDate`; the event date is the index `reportDate`, i.e. the date of earliest
event reported on the face of the form.

| File | Size | Document | Tier | Use for |
|---|---|---|---|---|
| `8-K_event-1997-11-07_acc-0000950151-97-000357_filed-1997-11-10.txt` | 10,145 B / 1,048 w | Form **8-K**, accession `0000950151-97-000357`, filed **1997-11-10**, event **1997-11-07** | **T1** | **The 8-K Stage 2 recorded as UNTRIED.** Item 5: the **$75,000,000 three-year senior secured term credit facility** commitment letter with Deutsche Bank AG / Deutsche Morgan Grenfell, increasable to $100,000,000, "to finance working capital, capital add[itions]…" — the first debt instrument after the IPO and the document that ends any reading of Amazon as equity-funded only |
| `8-K_event-1998-04-24_acc-0000891020-98-000653_filed-1998-04-27.txt` | 7,040 B / 535 w | Form **8-K**, accession `0000891020-98-000653`, filed **1998-04-27**, event **1998-04-24** | **T1** | EX-99.1: **"ANNOUNCES $275 MILLION OFFERING OF SENIOR DISCOUNT NOTES"** — the launch of the leverage decision, three days after the first acquisition press releases |
| `8-K_event-1998-04-27_acc-0000891020-98-000662_filed-1998-04-28.txt` | 27,553 B / 2,903 w | Form **8-K**, accession `0000891020-98-000662`, filed **1998-04-28**, event **1998-04-27** | **T1** | **Three press releases in one filing**: the 2-for-1 stock split, the acquisitions, and first-quarter earnings. The single densest Stage-3 signal — a company raising $275M, splitting its stock and reporting at record scale in one week |
| `8-K_event-1998-04-17_acc-0000891020-98-000694_filed-1998-05-01.txt` | 7,466 B / 657 w | Form **8-K**, accession `0000891020-98-000694`, filed **1998-05-01**, event **1998-04-17** | **T1** | **Item 9, Regulation S**: "The Company issued **540,066 shares** of its Common Stock in connection with the acquisition of … **Bookpages Limited** (England, April 17 1998); **Telebook, Inc.** (Florida, April 24 1998); and **Internet Movie Database Limited**" — the first acquisitions paid in stock, and the first off-shore issuance. Settlement dates are in this document, not in the retrospectives |
| `8-K_event-1998-05-05_acc-0000891020-98-000722_filed-1998-05-06.txt` | 7,181 B / 579 w | Form **8-K**, accession `0000891020-98-000722`, filed **1998-05-06**, event **1998-05-05** | **T1** | EX-99.1: "ANNOUNCES **INCREASE IN SIZE** OF OFFERING OF SENIOR DISCOUNT NOTES" — the upsize that carried the deal to the ~$326M gross figure the S-4 later reports |
| `8-K_event-1998-08-03_acc-0000891020-98-001210_filed-1998-08-07.txt` | 449,123 B / 63,504 w | Form **8-K**, accession `0000891020-98-001210`, filed **1998-08-07**, event **1998-08-03** | **T1** | **The two merger agreements signed the same day**: EX-2.1 Plan of Merger **Amazon.com / AJ Acquisition, Inc. / Junglee Corp.** and EX-2.2 **Amazon.com / Pacific Acquisitions / PlanetAll** (Sage Enterprises, Inc.), with the Junglee and Sage **Investor Rights Agreements** and the 3 August press release. The primary text of the "buy the capability" strategy |
| `8-K_event-1998-08-12_acc-0000891020-98-001352_filed-1998-08-27.txt` | 73,465 B / 7,086 w | Form **8-K**, accession `0000891020-98-001352`, filed **1998-08-27**, event **1998-08-12** | **T1** | Item 7(a): **Junglee Corp. audited financial statements** (1997, 1996, inception 1996-06-03) and pro formas for the 1998-08-12 closings, with auditors' consent — what Amazon actually paid and absorbed for the data-comparison asset |
| `8-K_event-1998-08-27_acc-0000891020-98-001370_filed-1998-09-11.txt` | 194,817 B / 19,915 w | Form **8-K**, accession `0000891020-98-001370`, filed **1998-09-11**, event **1998-08-27** | **T1** | Item 2: PlanetAll (Sage Enterprises) merger **completed 1998-08-27**, PlanetAll Series A converted and options assumed under the **1997 Stock Option Plan**; seven EX-27 **restated** financial-data schedules (12/31/97, 12/31/96, 6M to 6/30/98, 3M to 3/31/98) + E&Y consent. The restatement trail — read before quoting any 1997-98 figure from a pre-restatement source |
| `8-KA_event-1998-08-12_acc-0000891020-98-001491_filed-1998-10-26.txt` | 26,979 B / 2,355 w | Form **8-K/A**, accession `0000891020-98-001491`, filed **1998-10-26**, event **1998-08-12** | **T1** | The amendment to the 1998-08-27 8-K (same event date): corrected acquired-company statements/pro formas. Cite the 8-K/A in preference to the original where they differ |
| `8-K_event-1998-10-28_acc-0000891020-98-001498_filed-1998-10-28.txt` | 25,410 B / 2,304 w | Form **8-K**, accession `0000891020-98-001498`, filed **1998-10-28**, event **1998-10-28** | **T1** | Q3 1998 results release: **"AMAZON.COM BECOMES #1 ONLINE MUSIC RETAILER WITH SALES OF $14.4 MILLION; FIRST QUARTER TO ADD MORE THAN 1 MILLION CUSTOMERS"** — the filed evidence that the second category reached leadership inside one quarter of launch |
| `8-K_event-1998-11-19_acc-0000891020-98-001686_filed-1998-11-20.txt` | 8,261 B / 691 w | Form **8-K**, accession `0000891020-98-001686`, filed **1998-11-20**, event **1998-11-19** | **T1** | **"ANNOUNCES 3-FOR-1 STOCK SPLIT"** (board approval, effective January 1999) — the second split in seven months; the reason every per-share and option figure in this archive is split-vintage dependent |
| `8-K_event-1999-01-05_acc-0000891020-99-000011_filed-1999-01-05.txt` | 11,555 B / 1,157 w | Form **8-K**, accession `0000891020-99-000011`, filed **1999-01-05**, event **1999-01-05** | **T1** | The holiday release: **"MORE THAN 1 MILLION NEW CUSTOMERS IN HOLIDAY SEASON"; "AMAZON.COM ACHIEVES $1 BILLION SALES RUN-RATE"** — the repeatability milestone, on a dated filed record rather than in retrospect |
| `8-K_event-1999-01-26_acc-0000891020-99-000103_filed-1999-01-27.txt` | 28,645 B / 2,928 w | Form **8-K**, accession `0000891020-99-000103`, filed **1999-01-27**, event **1999-01-26** | **T1** | Q4/FY1998 results: **"RECORD HOLIDAY SEASON PUSHES CUSTOMER TOTAL PAST 6.2 MILLION; LEADERSHIP IN BOOKS AND MUSIC EXTENDED TO VIDEO, U.K., GERMANY"** — the multi-category, multi-country claim stated by the company on the day |
| `8-K_event-1999-01-28_acc-0000891020-99-000107_filed-1999-01-28.txt` | 7,307 B / 567 w | Form **8-K**, accession `0000891020-99-000107`, filed **1999-01-28**, event **1999-01-28** | **T1** | **"ANNOUNCES $500 MILLION OFFERING OF SUBORDINATED CONVERTIBLE DEBENTURES"** — the launch of the raise that closed as $1.25B six days later |
| `8-K_event-1999-01-28_acc-0000891020-99-000110_filed-1999-01-29.txt` | 8,186 B / 697 w | Form **8-K**, accession `0000891020-99-000110`, filed **1999-01-29**, event **1999-01-28** | **T1** | The next-day pricing and upsize release. **Two 8-Ks, the same event date**: the pair is the day-by-day record of a $500M ask becoming a $1.25bn take |
| `8-K_event-1999-02-03_acc-0000891020-99-000125_filed-1999-02-04.txt` | 417,302 B / 62,435 w | Form **8-K**, accession `0000891020-99-000125`, filed **1999-02-04**, event **1999-02-03** | **T1** | Item 5: **"On February 3, 1999, Amazon.com, Inc. completed the sale of its private offering of $1,250,000,000 aggregate principal amount of 4 3/4% Convertible Subordinated Notes due 2009"**, with the **Indenture (EX-4.1)** and **Registration Rights Agreement (EX-4.2)** filed in full. The largest single capital event in the window and its governing instrument |
| `8-K_event-1999-03-28_acc-0000891020-99-000551_filed-1999-03-29.txt` | 8,135 B / 645 w | Form **8-K**, accession `0000891020-99-000551`, filed **1999-03-29**, event **1999-03-28** | **T1** | "ANNOUNCES NEW SERVICE … Amazon.com plans to launch a **person-to-person auction service**" — the pre-launch statement, one day before the launch 8-K |
| `8-K_event-1999-03-30_acc-0000891020-99-000568_filed-1999-03-30.txt` | 15,629 B / 1,634 w | Form **8-K**, accession `0000891020-99-000568`, filed **1999-03-30**, event **1999-03-30** | **T1** | **"LAUNCHES ONLINE AUCTION SITE … THIRD-PARTY SELLERS CAN NOW REACH AMAZON.COM'S COMMUNITY OF 8 MILLION PRE-REGISTERED, EXPERIENCED ONLINE BUYERS"** — announcement and launch dated a day apart: the cadence itself is evidence |
| `8-K_event-1999-04-26_acc-0000891020-99-000717_filed-1999-04-27.txt` | 12,003 B / 1,176 w | Form **8-K**, accession `0000891020-99-000717`, filed **1999-04-27**, event **1999-04-26** | **T1** | **"ACQUIRES EXCHANGE.COM, ADDING MORE THAN 12 MILLION BOOK AND MUSIC ITEMS"** — the inventory-scaling logic of the marketplace stated in the release |
| `8-K_event-1999-04-28_acc-0000891020-99-000726_filed-1999-04-29.txt` | 27,114 B / 2,573 w | Form **8-K**, accession `0000891020-99-000726`, filed **1999-04-29**, event **1999-04-28** | **T1** | Q1 1999 results: "community of online shoppers grows to **over 8.4 million**" |
| `8-K_event-1999-04-26_acc-0000891020-99-000805_filed-1999-05-12.txt` | 178,207 B / 16,102 w | Form **8-K**, accession `0000891020-99-000805`, filed **1999-05-12**, event **1999-04-26** | **T1** | Item 5 "PENDING TRANSACTIONS": the **Alexa Internet** agreement of 1999-04-24 (with **Brewster Kahle** named) and the e-Niche agreement, financial statements incorporated ahead of closing, PwC consents, consideration "**totaling approximately $250 million**". The filed record of how the 1999 acquisitions were sequenced and sized |
| `8-K_event-1999-05-14_acc-0000891020-99-000908_filed-1999-05-19.txt` | 270,396 B / 35,895 w | Form **8-K**, accession `0000891020-99-000908`, filed **1999-05-19**, event **1999-05-14** | **T1** | Item 2: **Exchange.com merger completed 1999-05-14** under the 1999-04-24 agreement, via **Amazon.com Auctions, Inc.**, options assumed; EX-2.1 the Agreement and Plan of Merger in full |
| `8-K_event-1999-06-09_acc-0000891020-99-000988_filed-1999-06-10.txt` | 275,234 B / 35,837 w | Form **8-K**, accession `0000891020-99-000988`, filed **1999-06-10**, event **1999-06-09** | **T1** | Item 2: **Accept.com merger completed 1999-06-09** via **ADC Acquisitions, Inc.** under the 1999-04-25 agreement, plus **Accept.com's audited development-stage financials** (Ernst & Young). The payments leg of the strategy, with its own numbers |
| `8-K_event-1999-06-08_acc-0000891020-99-000993_filed-1999-06-11.txt` | 221,804 B / 31,196 w | Form **8-K**, accession `0000891020-99-000993`, filed **1999-06-11**, event **1999-06-08** | **T1** | Item 2: **Alexa Internet merger completed 1999-06-10** via **AI Acquisition, Inc.** under the 1999-04-24 agreement, Amazon options substituted at a stated **Exchange Ratio**. Note the index event date (6/8) precedes the stated completion (6/10) — do not silently "fix" it; report the form as filed |
| `8-K_event-1999-07-21_acc-0000891020-99-001224_filed-1999-07-22.txt` | 35,938 B / 3,579 w | Form **8-K**, accession `0000891020-99-001224`, filed **1999-07-22**, event **1999-07-21** | **T1** | Q2 1999 results: community "grows to **10.7 million**" |
| `8-K_event-1999-10-28_acc-0000891020-99-001789_filed-1999-10-28.txt` | 31,637 B / 3,056 w | Form **8-K**, accession `0000891020-99-001789`, filed **1999-10-28**, event **1999-10-28** (release dated 1999-10-27) | **T1** | Q3 1999 results: **"TOYS, ELECTRONICS, AND zSHOPS MAKE AMAZON.COM THE ONE-STOP DESTINATION FOR HOLIDAY SHOPPING"** — the last periodic event record inside the intake window |

## Registration lineage completed and the Exchange Act registration (5)

| File | Size | Document | Tier | Use for |
|---|---|---|---|---|
| `S-1A-No1_acc-0000891020-97-000603_filed-1997-04-21.txt` | 438,685 B / 58,684 w | Form **S-1/A** Amendment No. 1, accession `0000891020-97-000603`, filed **1997-04-21**, 9 documents | **T1** | Closes the ordinal gap in C-4. **New instruments appear only here**: EX-3.1 restated certificate, **EX-10.1 form of indemnification agreement**, and shareholder agreements with **Rick R. Ayre, John D. Risher and Joel R. Spiegel** — the equity paper of the officers who joined after the S-1's original roster, and the earliest filing evidence for Risher and Spiegel |
| `S-1A-No2_acc-0000891020-97-000659_filed-1997-04-29.txt` | 405,557 B / 54,006 w | Form **S-1/A** Amendment No. 2, accession `0000891020-97-000659`, filed **1997-04-29**, 3 documents | **T1** | **EX-1.1 FORM OF UNDERWRITING AGREEMENT** — the only underwriting-compensation instrument in the whole archive; go here, not to the press, for what the banks were actually contracted to receive, and read it against COR-01's deferred/perpetual-compensation question |
| `S-1A-No4_acc-0000891020-97-000822_filed-1997-05-13.txt` | 312,174 B / 40,082 w | Form **S-1/A** Amendment No. 4, accession `0000891020-97-000822`, filed **1997-05-13**, 5 documents | **T1** | The accession C-4 assigns to "Amendment No. 4"; carries the Perkins Coie opinion and the per-share computation. Any dossier that cites "Amendment No. 4" for the pricing-program sentence should be re-pointed to No. 3 (`…000755`, on disk) |
| `S-1A-No6_acc-0000891020-97-000847_filed-1997-05-14.txt` | 303,840 B / 39,491 w | Form **S-1/A** Amendment No. 6, accession `0000891020-97-000847`, filed **1997-05-14**, 2 documents | **T1** | **The last amendment before the 424B1.** Diff it against No. 5 and the final prospectus to get the priced text — §3 lineage means these five accessions plus the 424B1 are one registration statement (File No. 333-23795), so the differential is the only evidential gain |
| `8-A12G_exchange-act-registration_acc-0000891020-97-000704_filed-1997-05-02.txt` | 17,860 B / 2,107 w | Form **8-A12G**, accession `0000891020-97-000704`, filed **1997-05-02**, Exchange Act file **000-22513**, 2 documents | **T1** | The §12(b) registration of the **Common Stock, $0.01 par**, signed by Joy D. Covey; EX-3 is pages 44-45 of the prospectus (the Description of Capital Stock). ⚠ **Trap:** Item 1 calls it "the Prospectus … dated **April 21, 1996** contained in the Registrant's Registration Statement on Form S-1 … filed … on **March 24, 1997**" — internally impossible; April 21, **1997** (Amendment No. 1's prospectus date) is meant. Never cite this document for a 1996 date |

## Equity-plan registrations — the compensation and dilution engine (10)

| File | Size | Document | Tier | Use for |
|---|---|---|---|---|
| `S-8_FileNo-333-28763_acc-0000950151-97-000177_filed-1997-06-06.txt` | 23,873 B / 2,751 w | Form **S-8**, accession `0000950151-97-000177`, filed **1997-06-06**, File No. 333-28763, 3 documents | **T1** | **The first post-IPO registration of the 1997 Stock Option Plan**, three weeks after pricing; incorporates the 424B1 prospectus by reference and carries the Item 6 DGCL §145 indemnification statement. The start of the equity-financed-compensation regime that replaces cash pay |
| `S-8POS_FileNo-333-28763_AmdtNo1_acc-0000891020-97-001216_filed-1997-09-11.txt` | 22,544 B / 2,576 w | Form **S-8 POS** Amendment No. 1, accession `0000891020-97-001216`, filed **1997-09-11**, File No. 333-28763 | **T1** | Post-effective amendment to the 1997 S-8 — the mechanism by which Exchange Act reporting obligations flow into the plan registration |
| `S-8_FileNo-333-63311_acc-0000891020-98-001371_filed-1998-09-11.txt` | 160,948 B / 24,219 w | Form **S-8**, accession `0000891020-98-001371`, filed **1998-09-11**, File No. 333-63311, 7 documents | **T1** | **Four acquired-company plans registered in one filing**: Junglee Corp. 1996 Stock Plan, Junglee 1998 Equity Incentive Plan (amended), Sage Enterprises 1997 Amended Stock Option Plan, Sage MVP Stock Option Plan. The full plan texts as EX-99 — this is where "we bought teams and issued options" becomes quotable |
| `S-8POS_FileNo-333-63311_AmdtNo1_acc-0000891020-98-001434_filed-1998-10-01.txt` | 12,841 B / 1,054 w | Form **S-8 POS** Amendment No. 1, accession `0000891020-98-001434`, filed **1998-10-01**, File No. 333-63311 | **T1** | Post-effective amendment; its two consents (E&Y and **Deloitte & Touche**) mark the auditor changeover inside the window — relevant to any audit-lineage claim |
| `S-8_FileNo-333-74419_acc-0000891020-99-000437_filed-1999-03-15.txt` | 57,300 B / 7,777 w | Form **S-8**, accession `0000891020-99-000437`, filed **1999-03-15**, File No. 333-74419, 5 documents | **T1** | **1999 Nonofficer Employee Stock Option Plan** — the first plan that separates rank-and-file equity from officer grants; the hiring-scale and retention instrument of the 1999 expansion |
| `S-8_FileNo-333-78651_acc-0000891020-99-000893_filed-1999-05-17.txt` | 57,594 B / 7,812 w | Form **S-8**, accession `0000891020-99-000893`, filed **1999-05-17**, File No. 333-78651, 7 documents | **T1** | **InnerLint Technologies Stock Option Plan** — an acquired-company plan registered the same day the Q1 1999 10-Q landed; four audit firms' consents in one filing |
| `S-8_FileNo-333-78653_acc-0000891020-99-000895_filed-1999-05-17.txt` | 66,005 B / 9,183 w | Form **S-8**, accession `0000891020-99-000895`, filed **1999-05-17**, File No. 333-78653, 7 documents | **T1** | **e-Niche Inc. 1998 Stock Option and Grant Plan** (the second same-day S-8 — distinguish by file number, the accessions differ by 2) |
| `S-8_FileNo-333-80491_acc-0000891020-99-000995_filed-1999-06-11.txt` | 67,869 B / 9,375 w | Form **S-8**, accession `0000891020-99-000995`, filed **1999-06-11**, File No. 333-80491, 8 documents | **T1** | **Alexa Internet Amended & Restated 1997 Stock Plan** — filed the day after the Alexa closing 8-K |
| `S-8_FileNo-333-80495_acc-0000891020-99-000996_filed-1999-06-11.txt` | 62,158 B / 8,519 w | Form **S-8**, accession `0000891020-99-000996`, filed **1999-06-11**, File No. 333-80495, 8 documents | **T1** | **Accept.com Financial Services Corp 1998 Stock Plan** — same day as the Alexa S-8: two acquisitions' equity absorbed within 24 hours |
| `S-8_FileNo-333-88825_acc-0000891020-99-001698_filed-1999-10-12.txt` | 49,192 B / 6,628 w | Form **S-8**, accession `0000891020-99-001698`, filed **1999-10-12**, File No. 333-88825, 8 documents | **T1** | **Convergence Corporation Stock Option Plan** — the last equity registration inside the window |

## Debt and shelf registrations — how the expansion was actually funded (17)

| File | Size | Document | Tier | Use for |
|---|---|---|---|---|
| `S-4_FileNo-333-55943_acc-0000891020-98-000931_filed-1998-06-03.txt` | 99,963 B / 13,177 w | Form **S-4**, accession `0000891020-98-000931`, filed **1998-06-03**, File No. 333-55943, 4 documents | **T1** | The exchange registration that becomes the 1999 Junglee/PlanetAll S-4 line. Text states sales "through March 31, 1998 … more than **$251 million** to approximately **2.3 million customer accounts in over 150 countries**" and an accumulated deficit of **$42.9 million** |
| `S-4_FileNo-333-56723_acc-0000891020-98-000978_filed-1998-06-12.txt` | 448,102 B / 63,557 w | Form **S-4**, accession `0000891020-98-000978`, filed **1998-06-12**, File No. 333-56723, 11 documents, description "FORM S-4 - 10% SENIOR DISCOUNT NOTES" | **T1** | **The registered exchange offer for the 10% Senior Discount Notes due 2008**, described as "**approximately $326 million gross proceeds**". Contains the full "Increased Leverage" risk factor and a T-1 offer document. Read this to date and size the first big debt decision |
| `S-4A_FileNo-333-55943_AmdtNo1_acc-0000891020-98-001238_filed-1998-08-11.txt` | 91,442 B / 11,957 w | Form **S-4/A** Amendment No. 1, accession `0000891020-98-001238`, filed **1998-08-11**, File No. 333-55943 | **T1** | Amendment filed the same week as the Junglee/PlanetAll merger agreements |
| `S-4A_FileNo-333-56723_AmdtNo1_acc-0000891020-98-001239_filed-1998-08-11.txt` | 293,706 B / 42,178 w | Form **S-4/A** Amendment No. 1, accession `0000891020-98-001239`, filed **1998-08-11**, File No. 333-56723, 3 documents | **T1** | Notes exchange amendment with the earnings-to-fixed-charges computation — the coverage ratio an adversarial reader will want |
| `424B2_final-prospectus_acc-0000891020-98-001279_filed-1998-08-13.txt` | 269,298 B / 39,390 w | Form **424B2**, accession `0000891020-98-001279`, filed **1998-08-13**, Reg. No. 333-56723 | **T1** | **The priced exchange-offer prospectus** for the 10% Senior Discount Notes. States sales "through June 30, 1998 … more than **$367 million** to approximately **3.1 million customer accounts**", accumulated deficit **$64.1M**, and that ex-Notes the company would carry only "**approximately $2.4 million** of indebtedness" — the before-picture of the leverage pivot |
| `S-3_FileNo-333-65091_acc-0000891020-98-001430_filed-1998-09-30.txt` | 142,749 B / 18,684 w | Form **S-3**, accession `0000891020-98-001430`, filed **1998-09-30**, File No. 333-65091, 5 documents | **T1** | The shelf under which the **2,662,125-share** selling-stockholder prospectus (below) is issued; registers a Registration Rights Agreement as EX-4.3 |
| `S-3A_FileNo-333-65091_AmdtNo1_acc-0000891020-98-001467_filed-1998-10-15.txt` | 105,373 B / 13,257 w | Form **S-3/A** Amendment No. 1, accession `0000891020-98-001467`, filed **1998-10-15**, File No. 333-65091 | **T1** | Amendment; dual auditor consents (E&Y + Deloitte) again date the auditor transition |
| `424B3_final-prospectus_acc-0000891020-98-001477_filed-1998-10-22.txt` | 84,558 B / 10,684 w | Form **424B3**, accession `0000891020-98-001477`, filed **1998-10-22**, Reg. No. 333-65091, description "FINAL PROSPECTUS" | **T1** | **2,662,125 shares of Common Stock** offered by "certain stockholders … or by their pledgees, donees, distributees" — the secondary-distribution channel and the insiders' liquidity path, which the retrospectives describe but do not document |
| `424B3_prospectus-supplement_acc-0000891020-98-001492_filed-1998-10-27.txt` | 90,245 B / 11,591 w | Form **424B3**, accession `0000891020-98-001492`, filed **1998-10-27**, Reg. No. 333-65091 | **T1** | Supplement to the same prospectus five days later (filed under 424(b)(3) and (c)) — diff against the 1998-10-22 final to see what changed |
| `S-3_FileNo-333-74435_acc-0000891020-99-000441_filed-1999-03-16.txt` | 171,624 B / 20,762 w | Form **S-3**, accession `0000891020-99-000441`, filed **1999-03-16**, File No. 333-74435, 6 documents | **T1** | The shelf behind the **$1.25bn 4¾% Convertible Subordinated Notes due 2009** (the 424B3 stream of 1999). Carries the "$349 million of outstanding senior indebtedness" and "$162.1 million" deficit statements as of 1998-12-31, and the subordination language |
| `S-3A_FileNo-333-74435_AmdtNo1_acc-0000891020-99-000825_filed-1999-05-13.txt` | 157,282 B / 20,078 w | Form **S-3/A** Amendment No. 1, accession `0000891020-99-000825`, filed **1999-05-13**, File No. 333-74435, 6 documents | **T1** | The amendment to that notes-resale shelf: "**Holders of our 4 3/4% Convertible Subordinated Notes due 2009 may offer for sale the notes and the shares** [into which they convert]" — i.e. the **selling-stockholder** registration whose supplements run weekly to 1999-12-30. Adds the earnings-to-fixed-charges computation and consents from **three** audit firms (E&Y, Deloitte, PwC ×2) — the auditor-portfolio trace of the 1999 acquisitions |
| `S-3_FileNo-333-78797_acc-0000891020-99-000910_filed-1999-05-19.txt` | 135,607 B / 18,490 w | Form **S-3**, accession `0000891020-99-000910`, filed **1999-05-19**, File No. 333-78797, 6 documents | **T1** | **A $2,000,000,000 universal shelf**: common, preferred, depositary shares, debt, warrants, **stock purchase units and stock purchase contracts**, third-party warrants. The single clearest filed sign that the company was building permanent, repeatable access to capital — four consents from three audit firms |
| `S-3A_FileNo-333-78797_AmdtNo1_acc-0000891020-99-000977_filed-1999-06-08.txt` | 135,113 B / 18,873 w | Form **S-3/A** Amendment No. 1, accession `0000891020-99-000977`, filed **1999-06-08**, File No. 333-78797, 6 documents | **T1** | The amendment that adds the **restated certificate of incorporation** (EX-3.1) to the $2bn shelf — the authorized-capital change behind the 1999 stock-funded moves |
| `POSAM_FileNo-333-55943_AmdtNo1_acc-0000891020-99-000716_filed-1999-04-26.txt` | 80,130 B / 10,183 w | Form **POS AM** Amendment No. 1, accession `0000891020-99-000716`, filed **1999-04-26**, File No. 333-55943 | **T1** | Post-effective amendment to the S-4 — the acquired-company equity staying in registration |
| `POSAM_FileNo-333-55943_AmdtNo2_acc-0000891020-99-001311_filed-1999-08-06.txt` | 95,058 B / 12,066 w | Form **POS AM** Amendment No. 2, accession `0000891020-99-001311`, filed **1999-08-06**, File No. 333-55943, 8 documents | **T1** | Adds five auditors' consents and the **powers of attorney of J. Galli, Jr. and K. Brannon** — a named-officer signature trail for 1999 |
| `POSAMI_FileNo-333-55943_AmdtNo1_acc-0000891020-99-001503_filed-1999-08-31.txt` | 10,603 B / 908 w | Form **POS AMI**, accession `0000891020-99-001503`, filed **1999-08-31**, File No. 333-55943 | **T1** | Post-effective amendment to an **inactive** shelf; the instrument by which a registration is retired. Note the index calls it "POST EFFECTIVE AMENDMENT NO.1 TO FORM **S-3**" while the file number is the **S-4** shelf 333-55943 — an index/description inconsistency, quote the form code not the prose |
| `POSAM_FileNo-333-65091_AmdtNo2_acc-0000891020-99-001766_filed-1999-10-26.txt` | 10,850 B / 961 w | Form **POS AM** Amendment No. 2, accession `0000891020-99-001766`, filed **1999-10-26**, File No. 333-65091 | **T1** | Retirement/termination of the 2,662,125-share shelf — closes that capital line inside the window |

**How to use this intake — do not re-fetch any of the above.** These 80 filings (75 new + 5 held) are now the
complete local EDGAR record from 1997-03-24 to 2000-01-04 except the 45 rows listed as deliberately-not-
fetched in `../sources/STAGE3_INTAKE_MANIFEST.md`. Same §3 lineage rule as always: the 1998-99 registration
family is **one** story per file number, and the 424B3s that only incorporate the 10-Qs by reference are
**not** independent corroboration of any figure. Request accounting, including this pass's own 150-request
false start, is in the manifest.

**Duplicate-file notice (nothing deleted, nothing moved).** Four of the S-1/A files exist twice, byte-identical:
`S-1A-No1/2/4/6_acc-…_filed-….txt` (convention-correct hyphen, **cite these**) and `S-1A_No1/2/4/6_acc-…`
(underscore, written first in the same session before the naming convention was checked). SHA-256 over the EDGAR
bodies matches pairwise, and each body size equals the catalogue `size` exactly (436,103 / 403,334 / 309,865 /
301,661 B). The underscore variants are duplicates in the same sense as the unheadered `s1_original_…` copies
noted in the *Integrity note* above — **one document, not two sources**, and never a count of corroboration.
Full disclosure in §8 of `../sources/STAGE3_INTAKE_MANIFEST.md`.

**Three Stage-3 needs this intake could not satisfy**, in priority order, all detailed in §7 of the manifest:
(1) the **FY1999 Form 10-K** — not in the enumerated slice at all (it ends 2000-01-04), one row in
`…-submissions-001.json` plus one fetch away, and until it lands Stage 3's closing year rests on quarterly
filings and the 1999-10-28 Q4 press release rather than an annual report; (2) the **Seafirst / Wells Fargo
merchant-account and guarantee-release instruments**, which were never filed with the SEC and so cannot be
retrieved from EDGAR at any request budget — the release status stays UNKNOWN, now with the exhaustion of the
EDGAR route demonstrated; (3) **Section 16 Forms 3/4/5 for 1997-99 — zero rows in the 125-row catalogue**, so
the founder's own option-exercise and sale activity in the window cannot be dated from the filings;
**UNTRIED, not answered** (the untested route is slice `-001`, not a re-query of `-002`).

