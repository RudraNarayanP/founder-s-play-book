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

