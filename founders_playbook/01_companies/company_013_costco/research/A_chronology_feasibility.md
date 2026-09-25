# A_chronology_feasibility.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T19:07:16Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## Verdict

STATUS: WRITTEN (probe-costco)

**T3 (register tier) as measured — 1 of 5 families returned in-window Tier-1 text; T2 is one answered FETCH REQUEST away.**

| family | verdict | in-window Tier-1 text? |
|---|---|---|
| (a) filings | **TIER1_CANDIDATE** | YES — 3 documents on disk, 1994-01-05 → 1995-05-17, the FY1994 10-K naming 1976, 1977, 1983, 1985 and the merger mechanics of October 1993 |
| (b) web archives | **UNANSWERED** | no — Internet Archive served a service-wide "Temporarily Offline" page and one CDX request timed out; one of three CDX queries did answer |
| (c) periodicals | **LEAD_ONLY** | not yet read — but the DSN/Chain Store Age 1980-1984 run was proven to exist **with per-issue `_djvu.txt` layers**, i.e. the exact artefact class that flipped Walmart |
| (d) corporate print | **NULL (answered query)** | no — numFound=5 for the annual-report-shaped query, none a report; no Price Club / PriceCostco report run on IA |
| (e) documentary | **UNTRIED** | web ceiling reached on the tier-pivotal families; no auction/museum request issued |

Implied agent-run budget: **T3 = 3-4 runs (8k words/stage, §K, §N, §U still mandatory)**. If the family-(c) `FETCH REQUEST` returns 1982-83 Discount Store News text on Price Club/Costco, the count becomes 2 families and this is **re-graded T2 = 6-9 runs (22k/stage)**; the (c) fetch is 5-10 script-side downloads and is the highest-value single action available on this company. A third-family path to T1 exists only through (b) re-run after IA recovers (post-1995 corroboration, cannot reach 1976-1983) or through a legacy CIK for The Price Company (see §Entity question), which would still not pre-date 1994 in EDGAR.

Do **not** record this as "no early filings". The registrant's earliest EDGAR item is 1994-01-05, and the first 1994-11-17 10-K does carry registrant-asserted 1976/1983 text; the intake script missed all of it for the same reason it missed UnitedHealth's — a capped index and a mis-URLed older slice reported as a 404.

## Entity question

STATUS: WRITTEN (probe-costco) — **the choice of entity is this case's finding, and it splits**

Two predecessors, one registrant, and the registrant is **neither** of them:
- `CIK0000909832-main.json` formerNames: `PRICE/COSTCO INC` **from 1994-01-05 to 1997-01-06**, then `COSTCO COMPANIES INC` 1997-12-18 to 1999-06-29, now `COSTCO WHOLESALE CORP /NEW`. The CIK's first EDGAR filing (10-Q 0000912057-94-000012) is dated the same day its first name begins.
- FY1994 10-K, L174-178: "On **October 21, 1993**, the shareholders of both **The Price Company ("Price")** …" / ""Merger." **PriceCostco was formed to effect the Merger.** Pursuant to the Merger, …" — the registrant is a **merger vehicle formed in 1993**, so it has no legal existence reaching back to either 1976 or 1983.
- L985-989: "Prior to October 21, 1993, **Price Common Stock was quoted on The Nasdaq Stock** Market's National Market under the symbol **"PCLB"** and **Costco Common Stock was quoted on The Nasdaq Stock Market's National Market under the symbol "COST."** Trading in PriceCostco Common Stock **commenced on October 22, 1993.**" — correction entered on this pass: **both** predecessors were listed, so listed-share continuity does not choose between them. Exchange terms (L180-182, L980-983): each $.10-par Price share → **2.13** PriceCostco shares; each $.0033-par Costco share → **1** PriceCostco share.
- 10-Q 1994-01-05: "Costco") into Price/Costco" and "Costco shareholders on **October 21, 1993**"; 10-K L634-636: "The current Costco Designees are **Jeffrey H. Brotman** … **James D. Sinegal**" — a designation right attached to the *Costco* side, kept alive inside the merged registrant's governance text.

Call: argue **Stage-1's origin boundary on the Price Club line (The Price Company, 1976 concept) for the corporate-continuity spine, and put Costco's 1983 opening as the second, separately-argued origin node — not as a sub-clause of the 1983 one.** Reasons defensible from what was read: (i) the registrant's own earliest long-form document dates the concept to 1976 and attributes it to Price ("When Price pioneered the membership warehouse club concept in 1976", L398-400); (ii) **both** predecessors were Nasdaq-listed into the merger ("PCLB" and "COST", L985-989), so neither side can claim the boundary on listing continuity alone — the tie-breaker is textual: the registrant remembers **1976** as the origin of the concept and remembers itself only as a vehicle "formed to effect the Merger"; (iii) the 1983 side is evidenced in filings only by personnel dates of Costco officers ("joined Costco as Vice President, Operations in **May 1983**", L916-917; Galanti "…of Costco since **January 1985**", L921) — which proves Costco was operating by May 1983 but is **not** a filing-sourced founding date. The counter-argument, and it is strong, is that the registrant retained the CIK on the **Costco** side after the 1997 split-up (formerNames show PRICE/COSTCO → COSTCO COMPANIES, with a `15-12G` deregistration filed 1997-01-06 in the same window), so "the" successor narrative is Costco's. Both must be argued; the probe's job here is to state that the two-node framing is what the filings support and that any single-origin story is an anachronism imported from the modern brand.

## Family a filings

STATUS: WRITTEN (probe-costco) — verdict **TIER1_CANDIDATE** (in-window registrant text naming 1976 and 1983)

Scripted intake (all commands run this session, repo root):
- `resolve --ticker COST` → `{"ticker":"COST","cik":909832,"name":"COSTCO WHOLESALE CORP /NEW"}`
- `index --cik 909832` → "1007 filings … earliest forms: 10-K, 10-K/A, 10-Q, …". `submissions.csv` range: **min 2016-10-07, max 2026-09-24, n=1007**. The script enumerates only EDGAR's `recent` cap.
- `_INDEX.md` flags `CIK0000909832-submissions-001.json` as **UNANSWERED: HTTP 404** — that is the archive slice holding 1994-2016, and it is the reason `auto --from 1983-01-01 --to 1997-12-31 --max-docs 25` returned "**0 documents stored, 0 skipped/unanswered**". The 404 was a wrong-URL error (script uses `www.sec.gov/Archives/edgar/data/<cik>/…`; that path now 503s), **not absence**. Re-fetched from `https://data.sec.gov/submissions/CIK0000909832-submissions-001.json` → **HTTP 200, 268,868 bytes**, stored at `sources/_index/CIK0000909832-submissions-001.json`. It parses with **flat** keys (no `filings.recent` wrapper), which the script does not handle.
- That slice enumerates **1,716 filings, 1994-01-05 → 2016-10-06**. Earliest in-window per form: 10-Q **1994-01-05** (0000912057-94-000012); 11-K 1994-03-31; 8-K 1994-08-05; 10-K **1994-11-17** (0000912057-94-003945); SC 13E4 1994-11-21; DEF 14A 1994-12-23; SC 13D 1994-12-23; S-8 1995-02-03; S-3 1995-05-17 (0000891020-95-000177); 424B1 1995-06-02; 10-K405 1995-11-30; SC 13G 1996-02-12; 10-K/A 1996-03-15; PRE 14A 1996-11-29 (0000912057-96-027954); 15-12G 1997-01-06; 424B3 1997-12-04.
- `facts --from 1983-01-01 --to 1997-12-31` printed `sources\financials\xbrl_early_series.csv` but **wrote no file into company_013** (`sources/financials/` is empty; the only such CSV on disk is company_017_meta's, containing CIK 1326801 data — a concurrent agent's file, left untouched). Treat the XBRL series as **UNANSWERED-by-script**, not null; XBRL companyfacts cannot reach 1994-97 anyway.
- `grab` by accession failed on both tries (503 after 3 retries / 404 on `index-headers.txt`), while a single spaced `curl` of the same accessions returned **HTTP 200**. Documents are reachable; the script's burst behaviour is not.

Fetched by hand into `sources/sec/<accession>/<accession>.txt`, provenance in `sources/sec/fetch_log.txt` (url + http code + bytes per row):

| accession | filed | http | bytes | origin-year hits |
|---|---|---|---|---|
| 0000912057-94-000012 (10-Q) | 1994-01-05 | 200 | 64,490 | 1976=0 1983=0 1993=83 |
| 0000912057-94-003945 (10-K, FY ended 1994-08-31 per filing) | 1994-11-17 | 200 | 396,621 | **1976=3 1983=3 1985=6** 1993=176 |
| 0000891020-95-000177 (S-3) | 1995-05-17 | 200 | 324,751 | 1976=0 1983=0 1993=7 |
| 0000912057-96-027954 (PRE 14A) | 1996-11-29 | **503** | 7,747 | kept as a negative artifact |

Tier-1 in-window text actually read (FY1994 10-K, `0000912057-94-003945.txt`; line numbers are local locators only, §14.12):
- L398-401: "When **Price pioneered the membership warehouse club concept in 1976**, the dominant companies selling comparable lines of merchandise were department stores, grocery stores and traditional wholesalers."
- L875-876: "…Price **since 1976**, and was Chairman of the Board of Price since January 1989. Mr. Price was **President of Price from 1976 until December 1990**."
- L964-966: "He joined **Price** as a warehouse manager in **September 1977** and was its Vice President of Operations from **1983** to 1988."
- L916-917: an executive "joined **Costco** as Vice President, Operations in **May 1983**" (also L930 "November 1983"), plus L914-915 Costco directorships from **April 1986**, L918 **June 1985**, L921 Galanti "Senior Vice President, Chief Financial Officer and Treasurer of Costco since **January 1985**".
- 10-Q 1994-01-05, L762: "On **October 21, 1993**, the shareholders of **both Price and Costco** approved an…" and L168: "Price and Costco shareholders on October 21, 1993." FY1994 10-K L174-182 and L980-983 add the mechanics: "PriceCostco was **formed to effect the Merger**"; each **$.10**-par Price share exchanged for **2.13** PriceCostco shares; each **$.0033**-par Costco share for **1** share. L985-989: pre-merger Nasdaq symbols **"PCLB"** (Price) and **"COST"** (Costco); "Trading in PriceCostco Common Stock **commenced on October 22, 1993**."

Character of the evidence: this is **retrospective-but-contemporaneous** registrant text (written 1994 about 1976-1985), the same class that pinned UnitedHealth. It fixes entity names, merger mechanics and personnel dates, but it does **not** carry a founding narrative or any 1976-1983 document.

Predecessor entity's own filings — the structural question:
- `CIK0000909832-main.json` (data.sec.gov, HTTP 200, 159,116 bytes) gives `formerNames`: **`PRICE/COSTCO INC` from 1994-01-05 to 1997-01-06**, `COSTCO COMPANIES INC` 1997-12-18 to 1999-06-29. So CIK 909832's EDGAR life **begins at the merged registrant, on the same day as its first filing (1994-01-05)**; the CIK is not the pre-merger Costco's, and it holds **no S-1** at all.
- Searching for a pre-merger registrant ("The Price Company"/"Price Club Inc", "The Costco Companies") requires EDGAR company-name search: `www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=…` returned **HTTP 503 "SEC.gov | File Unavailable"** on every variant tried (atom + HTML, `price club`, `price company`, bare `sec.gov` → 301). The legacy full-text endpoint `efts.sec.gov/LATEST/search-index?q="Price Club"` answers (HTTP 200, hits) but EDGAR FTS coverage begins **2001**, so it cannot surface 1976-1993 filings by definition.
- Therefore predecessor filings are **UNTRIED**, not null. What is needed: one working `browse-edgar` company search (or the SEC's legacy paper index / Fort Worth accession records) for `PRICE CLUB INC`, `THE PRICE COMPANY`, `THE COSTCO COMPANIES INC`; and a re-run of `sec_intake index` against the older slice once `index` reads `data.sec.gov/submissions/CIK*-submissions-001.json` and its flat schema.
- `FETCH REQUEST:` for the orchestrator — accession `0000912057-96-027954` doc `0000912057-96-027954.txt` (PRE 14A, 1996-11-29, retry at single-digit rate; expected to carry the split-up history), plus `0000912057-94-003984` (SC 13E4, 1994-11-21), `0000891020-95-000228` (424B1, 1995-06-02), `0000912057-95-010555` (10-K405, 1995-11-30).

## Family b web

STATUS: WRITTEN (probe-costco) — verdict **UNANSWERED** (not null; Internet Archive was serving a service-wide offline page during the window)

Three CDX requests issued against `http://web.archive.org/cdx/search/cdx` (the whole family-b web budget), logged in `sources/webarchives/`:
1. `url=priceclub.com&filter=statuscode:200&collapse=timestamp:6&limit=12` → HTTP 200 body but the body is **`<title>Internet Archive: Temporarily Offline</title>`** — a service message, not a CDX answer. Bare-host test consumed; `www.priceclub.com` therefore NOT separately tested (§14: www vs bare host is ONE test).
2. `url=costco.com&filter=statuscode:200&limit=8` → `curl: (28) Operation timed out after 45010 ms with 0 bytes received`. No answer.
3. `url=sec.gov/cgi-bin/browse-edgar&matchType=exact&output=json&limit=2000` → **HTTP 200, real CDX JSON**; first row shown: `["gov,sec)/cgi-bin/browse-edgar","20041118073800","http://sec.gov/cgi-bin/browse-edgar","text/html","200",…]`. So the CDX endpoint itself was alive for this one key while queries 1-2 failed.

Consequence for the probe: **no archived snapshot of any 1990s warehouse-club site was reached**, and no archived EDGAR company-search page earlier than 2004-11-18 surfaced. Expected anyway — mid-1990s is the floor of the web-archive family (§14.6: "web archives nothing before the mid-1990s"), which is two decades after Price Club's 1976 opening and nine after Costco's 1983 opening. Even a fully healthy CDX run cannot make family (b) a Tier-1 carrier for the origin period; it can only corroborate post-1995 text. Re-run when IA is back: CDX for `priceclub.com`, `www.priceclub.com`, `costco.com`, and archived `browse-edgar?action=getcompany&company=price+club` result pages (the latter is the cheapest remaining route to a predecessor CIK, since live `browse-edgar` is 503-blocked from this box).

## Family c periodicals

STATUS: WRITTEN (probe-costco) — verdict **LEAD_ONLY**, and it is one download away from TIER1_CANDIDATE

`python tools/periodical_harvest.py --help` → the tool exists and takes `--company`, `--source-family`, `--config`, `--out`, `--max-requests`, `--delay`, `--cache-dir`. But `tools/queries.json` (read, not edited — not my path) carries **49 tasks for companies `['apple','unitedhealth','walmart']` only**; `periodical_harvest.py --company costco --dry-run` → **"PLANNED REQUESTS (0 tasks)"**. So the scripted route for this company is **UNTRIED-BY-CONFIG**: it needs a `costco` task block (chronicling_america / hathitrust / google_books / internet_archive / corporate_print), which is an orchestrator-side edit, not a null.

Direct probe instead (raw JSON kept under `sources/periodicals/`): `https://archive.org/advancedsearch.php?q=(title:("discount store news") OR title:("chain store age") OR title:("women's wear daily")) AND mediatype:(texts)` → `ia_c_trade_serials.json`, **HTTP 200, numFound=44**, and the run is contiguous across the founding years: `micro_IA40706901_0406` Discount Store News **1980**; `micro_IA40706905_0021` DSN **1981**; `micro_IA40706908_0058` DSN **1982**; `micro_IA40706911_0343` DSN **1983**; `micro_IA40706915_0204` DSN **1984**, with parallel `Chain Store Age` (Supermarkets / Executive / General Merchandise Edition) items for the same years. This is precisely the corpus §14.6 says carries the 1976-1983 warehouse-club story.

Decisiveness test: `https://archive.org/metadata/micro_IA40706911_0343` → `ia_meta_1983_discount_store_news.json`, **HTTP 200, 204,704 bytes, 219 files, of which 21 `_djvu.txt`** — per-issue OCR text layers with issue-level names: `"… 01. NOV 1 1982_djvu.txt"`, `"… 02. NOV 15 1982_djvu.txt"`, `"… 03. DEC 13 1982_djvu.txt"`, `"… 04. FEB 7 1983_djvu.txt"`. Host/dir from the same response: `ia803100.us.archive.org` `/0/items/micro_IA40706911_0343`; collection tags `['microfiche','statistical-reference-index']`. So the trade press covering Costco's first year (1983) exists on IA **with extractable text**.

Why this is not yet scored as Tier-1 text: no issue text has been retrieved or read this session, so no Price Club / Costco / Sinegal / Brotman sentence from 1982-83 is on disk. A full-text phrase query in the same family — `q="price club" AND mediatype:texts AND YEAR:[1976 TO 1993]` (`ia_c_periodicals.json`, HTTP 200) — returned **numFound=1**, an unrelated item (`100-fun-vol-2-no-1-virginia-beach-va`, 1985), which shows IA's indexed `text:` field does **not** reliably reach the microfiche items' txt layers. The route is therefore per-item download, not search.

`FETCH REQUEST:` for the orchestrator (script-reachable once a queries.json task exists; my 8-web budget was spent on proving the route rather than gambling it on one grep):
- download and grep for `Price Club|Costco|warehouse club|Sinegal|Brotman|price`, in issue layers of `micro_IA40706911_0343` (DSN 1982-83), `micro_IA40706915_0204` (DSN 1984), `micro_IA40706908_0058` (DSN 1982), `micro_IA40706905_0021` (DSN 1981), `micro_IA40706901_0406` (DSN 1980), via `https://archive.org/download/micro_IA40706911_0343/<file>_djvu.txt`
- then repeat for the `Chain Store Age` identifiers above, and for the 1976-1979 DSN/Chain Store Age run (query the same title set with `YEAR:[1975 TO 1980]` — **not yet attempted**, so Price Club's first three years are unprobed here).

## Family d corporate print

STATUS: WRITTEN (probe-costco) — verdict **NULL for the annual-report run** (query answered; nothing there), with one in-window non-financial item worth keeping

This is the family that flipped Walmart, so it was queried explicitly, Walmart's verified exemplar shape and all (`(title:(…) OR title:(…)) AND (title:(annual) OR title:(reports)) AND mediatype:(texts) AND YEAR:[…]`), before any "paper only" claim was made:
- `ia_d_corporate_print.json` — `q=(title:(costco) OR title:("price club") OR title:(pricecostco)) AND mediatype:(texts) AND YEAR:[1970 TO 1998]` → **HTTP 200, numFound=5**, none a corporate report: two 1991 items `costcowholesalef1619sanf` / `costcowholesaled1219sanf` "Costco Wholesale : final / draft, environmental impact report" (a lead-agency CEQA document naming Costco as applicant — in-window digitised print about the company, not by it), a 1995 Supreme Court reporter item, and two 1996-97 joke books.
- `ia_d_costco_any.json` — `q=costco AND mediatype:(texts)` (unbounded year) → **HTTP 200, numFound=2,208**, earliest company-relevant items 1991; the 2002+ mass is Costco-branded cookbooks. No `Price Club`/`PriceCostco` annual-report or shareholder-report run, and no `creator:`-scoped hit for either predecessor.

Contrast is the finding: Walmart's FY1972-FY1997 printed annual-report run sits on IA **free with text layers**; Costco's does not appear at all, which is consistent with Costco having no public annual-report tradition before its 1997-era registrant and with Price Club's reports having been filed on paper (pre-EDGAR) rather than deposited with IA. Recorded as a **documented null from an answered query**, not an error. Caveat kept open: my family-d queries were title-scoped (the Walmart exemplar's shape); a `creator:`-scoped and an unindexed-serials sweep were not run.

## Family e documentary

STATUS: WRITTEN (probe-costco) — verdict **UNTRIED** (deliberate budget allocation, not an error and not a null)

No auction or museum request was issued. The 8-web ceiling was reached exactly (3 Wayback CDX + 4 Internet Archive search + 1 Internet Archive metadata) with the last calls spent on the tier-pivotal family-(c)/(d) questions instead of on a coin-flip lot search. `periodical_harvest.py` has no auction/museum source family at all (tasks cover `chronicling_america, hathitrust, corporate_print, internet_archive, google_books` only), so this family is off-script for every company in the run, not just this one.

What would answer it (record verbatim for the next pass): search WorthPoint / LiveAuctioneers / Heritage Auctions and the UW Libraries/Washington State historical societies for "Price Club" and "Costco" founding ephemera — membership cards, warehouse-site photographs, 1983 first-store openings, founding prospectus or share certificates; Apple's precedent shows founding documents can surface at auction, and the 1976-1983 leg here is exactly the period where such items carry dates no filing carries.

## Boundaries

STATUS: WRITTEN (probe-costco) — proposed, tier T3/T2, two-track Stage 1

Earliest **defensible** origin: **1976**, on the registrant's own words — FY1994 10-K L398-400 "When Price pioneered the membership warehouse club concept in 1976…", filed 1994-11-17. This is Tier-1 registrant text but *retrospective*: no 1976 document exists in the corpus, and none is expected in EDGAR, whose coverage for this CIK begins 1994-01-05. Founder pre-history (Sol Price / Robert Price before 1976; Brotman and Sinegal before 1983) stays **UNKNOWN** and is not deleted from the schema — it is a named gap with a retrieval route (family c/d/e).

- **Stage 1 — two predecessor tracks, 1976 → 1993-10-21.** Track P: The Price Company / Price Club, opening 1976, evidenced in-filings only by retrospective 1994 text plus officer-service dates (L875-876 "President of Price from 1976 until December 1990"; L964-966 "joined Price as a warehouse manager in September 1977"). Track C: Costco, evidenced to **May 1983** as an operating floor ("joined Costco as Vice President, Operations in May 1983", L916-917) — i.e. "Costco founded 1983" is **not yet** a filing-sourced founding date, only a terminus ante quem for operations. Both tracks close on the shareholder vote of 1993-10-21 (10-Q + 10-K L174).
- **Stage 2 — the merged registrant, 1993-10-22 → 1997.** Opens on "Trading in PriceCostco Common Stock commenced on October 22, 1993" (L988) and on the registrant's formation ("PriceCostco was formed to effect the Merger", L178); closes on the split-up markers already enumerated: `15-12G` filed 1997-01-06 and formerName change PRICE/COSTCO INC → COSTCO COMPANIES INC (1997-12-18). This is the only stage where the corpus is filing-native end-to-end.
- **Stage 3 — Costco Wholesale as the surviving registrant, 1997 → window close (1997-12-31 for this probe; the index then runs to 2026).** Registrant's own name change to `COSTCO WHOLESALE CORP /NEW` is the marker; the 424B3 (1997-12-04) is the last enumerated pre-change document.
- Tier note for the orchestrator: at **T3** Stage 1 must be written as registers + short narrative with the 1976/1983 legs each carried by named retrospective filings, and §K/§N/§U mandatory; at **T2** (if the (c) fetch lands 1982-83 trade-press text) Stage 1 Track C earns contemporaneous sourcing, which is the only way this company can ever date its own opening rather than quote itself remembering it.

## Conflicts

STATUS: WRITTEN (probe-costco) — live, unresolved

1. **Index-vs-archive conflict.** `sources/_index/_INDEX.md` asserts "1007 filings … **This file is the source of truth for what exists**", range 2016-10-07 → 2026-09-24, while `sources/_index/CIK0000909832-submissions-001.json` (fetched this pass, HTTP 200) enumerates **1,716 further filings, 1994-01-05 → 2016-10-06**. Any agent trusting `_INDEX.md` will conclude 1983-1997 is empty. The header sentence is wrong for capped registrants.
2. **Tool-reporting conflict.** `auto … --from 1983-01-01 --to 1997-12-31` printed "**0 documents stored, 0 skipped/unanswered**" — a clean-looking null for a window that in fact contains 1994-1997 filings. `0 skipped/unanswered` is not "0 exist".
3. **Fetch-path conflict.** `grab --accession 0000912057-94-000012` → "UNANSWERED after 3 tries (HTTP 503)"; `grab --accession 0000912057-94-003945` → "HTTP 404" — yet spaced single `curl` calls for the identical accessions returned **HTTP 200** (64,490 and 396,621 bytes). The script's URL construction and retry cadence are the defect; treat every `sec_intake` document-level null as UNANSWERED until re-proved.
4. **XBRL conflict.** `facts` echoed `…company_013_costco\sources\financials\xbrl_early_series.csv`, but that path holds no file; the only `xbrl_early_series.csv` on disk is under `company_017_meta/…` and contains CIK 1326801 (Meta) rows, written during this same minute by a concurrent agent. Left untouched (§14.4). No XBRL series for this company may be inherited from either path.
5. **Entity-continuity conflict (substantive, keep open).** Registrant formed 1993 to effect the merger (so neither predecessor is "it"), vs. **both** predecessors having been Nasdaq-listed into it ("PCLB" Price / "COST" Costco, 10-K L985-989 — an earlier draft of this section wrongly read the listing as Price-only, corrected on this pass), vs. CIK continuity through the **Costco** side after the 1997 split-up. Whichever spine Stage 1 adopts, the other must be recorded as an alternative reading in the claim register.
6. **Merger-date pair.** 1993-10-21 (shareholder action; also the 10-Q's consideration date) vs. 1993-10-22 (first trading day). Downstream text that says "the merger closed October 22, 1993" is not supported as written by either sentence read here.
7. **Single-source risk inside family (a).** Origin-year text is concentrated in one document: 10-K 1994-11-17 (1976=3, 1983=3, 1985=6) while the 1994-01-05 10-Q and the 1995-05-17 S-3 return 1976=0, 1983=0. Every 1976/1983 statement currently rests on the FY1994 10-K alone.

## Nulls

STATUS: WRITTEN (probe-costco) — documented nulls from answered queries (contrast with §Untried)

- **Family (d), annual-report run: NULL, answered.** `title:(costco) OR title:("price club") OR title:(pricecostco)` AND `mediatype:(texts)` AND `YEAR:[1970 TO 1998]` → HTTP 200, **numFound=5**, none a corporate report (two 1991 environmental-impact-report items naming Costco as applicant; a 1995 court reporter; two 1996-97 humour items). Walmart's free FY1972-FY1997 printed-AR run has **no analogue here**.
- **No registration statement of any kind on CIK 909832.** The full older slice was parsed for earliest-per-form: the earliest `S-` forms are `S-8` 1995-02-03 and `S-3` 1995-05-17; there is **no S-1**, and nothing before 1994-01-05 on the CIK at all. This is the UnitedHealth pattern (earliest text pinned to a post-founding filing, no S-1 in existence), not a failed search.
- **1976/1983 absent from the other three fetched documents** (counts above), including the 1995 S-3, which one might expect to carry a business history.
- **EDGAR cannot hold the 1976-1993 leg.** EDGAR's own archive floor for this registrant is 1994-01-05 and the filings enumerated in 1994 are pre-EDGAR-mandate paper-era; no pre-1994 document will be found by any EDGAR route. That boundary is structural, and it is what makes families (c)/(d)/(e) the only possible contemporaneous-origin carriers.
- **Family (b) is NOT a null** — see §Untried/§Family b (IA temporarily offline; one of three CDX queries answered).
- **Family (c) is NOT a null** — the search answered and the serial items exist.

## Untried

STATUS: WRITTEN (probe-costco) — nothing below is a null; all of it is reachable

1. **Predecessor registrants' own EDGAR CIKs** — `THE PRICE COMPANY` / `PRICE CLUB INC` / `THE COSTCO COMPANIES INC`. Needed: one working EDGAR company-name search. Every variant tried returned a block, not an answer: `www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=price+club…` → **HTTP 503**; `…company=price+company…` → 503 page "SEC.gov | File Unavailable"; bare `sec.gov/…` → 301. `efts.sec.gov/LATEST/search-index?q="Price Club"` **answered HTTP 200** but EDGAR full-text search starts in 2001, so it cannot surface pre-1994 filings by construction. If a legacy CIK exists it would still begin ~1994 in EDGAR — worth proving, not assuming.
2. **In-window filings not yet fetched** (script-reachable; `FETCH REQUEST` in §Family a): PRE 14A `0000912057-96-027954` (503 page kept as a negative artifact, 7,747 bytes — most likely document in the set to carry a full predecessor history, being the split-up proxy), SC 13E4 `0000912057-94-003984`, 424B1 `0000891020-95-000228`, 10-K405 `0000912057-95-010555`, 10-K/A `0000912057-96-004594`, DEF 14A `0000950123-94-002087`, and the whole 1995-1997 run (13 10-Qs, 2 10-Ks, 4 S-3s in the slice).
3. **`sec_intake.py` fixes needed before the next pass trusts it:** read the older slices from `data.sec.gov/submissions/CIK…-submissions-001.json`, parse their **flat** schema (no `filings.recent`), and space `grab` retries (the same URL is 200 on a single spaced request, 503 in a burst).
4. **Family (c) harvest untried-by-config:** `periodical_harvest.py --company costco --dry-run` → **0 tasks**; `queries.json` covers apple/unitedhealth/walmart only. Untouched families for this company entirely: **chronicling_america** (17 tasks exist for other companies; local-paper route), **hathitrust**, **google_books** (WWD/Discount Store News back-file route). Also untried here even though internet_archive was probed by hand: the **1976-1979** DSN/Chain Store Age run (Price Club's own first years), and any `text:` search for `Costco` (only `price club` was phrase-queried for 1976-1993).
5. **Family (d) variants untried:** `creator:`-scoped search, `price club annual report` as a bare phrase, and the bound-book/serial search of *non-IA* deposit libraries (HathiTrust) for The Price Company reports.
6. **Family (e) auction/museum: UNTRIED, no request issued** (web ceiling consumed). Route recorded above; Apple's precedent makes this the live hope for an actual 1983 first-store artefact.
7. **Family (b) re-run when Internet Archive is healthy** — including `www.priceclub.com` (untested because bare-host test returned the service-wide offline page, and www-vs-bare is one test) and archived `browse-edgar` result pages, which double as the cheapest route to item 1.

## SUPERSEDED / RE-GRADED 2026-09-27

<!-- Appended by regrade-t3-batch. Nothing above this heading is rewritten or deleted; the record that
     this tier was measured on a broken `tools/sec_intake.py` is itself a finding (§14.4, §14.12). -->

**What this section supersedes: the intake measurement only, not the verdict.** Original verdict
"VERDICT: T3 as measured — 1 of 5 families returned in-window Tier-1 text" **stands unchanged at T3**,
because family (a) already counted as a YES; what the re-grade found is that the *volume* of family (a)
was reported as zero by a broken tool.

Re-measure of family (a) with the rebuilt script, window 1983-01-01 → 1997-12-31, CIK 909832
(verified this session: `resolve --ticker COST` → `{"cik": 909832, "name": "COSTCO WHOLESALE CORP /NEW"}`),
full figures in `A3_intake_regrade.md`:

- `index` now enumerates **2,723 filings** (was 1,007 `recent`-only) and the in-window slice parses to
  **59 filings, 1994-01-05 → 1997-12-04**. This **confirms** §Untried item 1's and §Nulls' structural claim
  that EDGAR holds nothing for this CIK before 1994-01-05 — that part of the probe was right.
- `auto … --max-docs 25` → **"11 documents stored (2285245 bytes, 293457 words), 0 UNANSWERED"**. The probe's
  §Conflicts 2 ("0 documents stored, 0 skipped/unanswered") is confirmed as a **tool artifact, not a null**.
- Stored bytes are filings, not apology pages: `grep -l -i "File Unavailable\|Temporarily Offline"` over
  `sources/sec/*.txt` → **0 matches**; `grep -c "1976"` on the newly stored 1994-11-17 10-K → **3**, i.e. the
  origin-year text the probe read by hand is present in script-stored bytes.
- **Earliest form/date actually held by the script: 8-K, 1994-08-05** (0000912057-94-002516, 125,566 B).
  Earliest held on disk at all: 10-Q 1994-01-05 (64,490 B, the probe's own hand fetch, not re-stored).
- **Earliest form/date merely existing in the index: 10-Q, 1994-01-05** (0000912057-94-000012).

Corrections to the probe's own claims, in the probe's favour and against it:
- §Family a "That slice enumerates 1,716 filings" — re-derived independently as 2,723 total rows / 59
  in-window; the hand-fetched accessions and the script now agree on dates and bytes.
- §Untried item 3 asked for three script fixes (read older slices, parse the flat schema, space retries).
  **Two are now demonstrably fixed** — the older slice is read and the flat schema parsed — and `grab`-style
  document fetch succeeded for all 11 stored rows with 0 UNANSWERED. Retry burst behaviour was not re-tested.
- **Residual defect, new on this pass:** all 59 in-window rows still carry a **blank `primaryDocument`**
  (nameless pre-2001 listing). The tool recovered names for 11 via directory-listing fallback and **dropped
  the other 48 silently** — `_UNANSWERED.csv` holds only its header, so "0 UNANSWERED" is still not
  "nothing remains". Predecessor filings (§Untried 1) and the 48 in-window documents remain **UNTRIED**.
- `facts` still prints `sources/financials/xbrl_early_series.csv` and writes nothing (directory empty);
  §Conflicts 4 stands — no XBRL series may be inherited for this company.

**Tier after re-grade: T3 PROVISIONAL** (was "T3 as measured"). §15.2 families with in-window Tier-1 text = 1
→ T3 unchanged; but families (b), (c) and (e) were **not in the denominator**: (c) was UNTRIED-BY-CONFIG
(`tools/queries.json` had no `costco` task block; the route was proven to exist with per-issue `_djvu.txt`
layers), (b) UNANSWERED on an IA outage, (e) never attempted. That gap is being fixed by another agent, so
this tier is recorded as provisional and a re-grade that repairs only family (a) **understates the ceiling**
— the probe's own upgrade path stands: one answered family-(c) harvest of 1982–83 Discount Store News /
Chain Store Age text makes it 2 families → **T2 (6–9 runs, 22k/stage)**. Original §Verdict, §Entity question
(two-origin-node framing), §Boundaries, §Conflicts 5–7 and §Family b–e are **not** superseded by this pass.

