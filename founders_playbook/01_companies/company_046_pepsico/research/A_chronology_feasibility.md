# A — Stage-1 chronology feasibility: PEPSICO INC (company_046_pepsico, Fortune rank 46)

Probe agent: `probe-pepsico`. Claim: `scaffold.py claim --path …/research/A_chronology_feasibility.md --agent probe-pepsico` → CREATED (owner=probe-pepsico).
Web calls made by this probe: **0**. Scripts run by this probe: read-only local greps + the briefed `gates.py` command. `harvest_mine.py` and `periodical_harvest.py` were **not** run (per brief).
Every quantifier below is a measurement; the command that produced it is printed with it.

STATUS: WRITTEN

---

## A.1 What is actually on disk (measured tonight, re-measured by this probe)

| measure | value | how it was measured |
|---|---|---|
| SEC documents stored | **27** files (`.txt` + `.htm`), **17** distinct accessions, **27** `.meta.json` sidecars | `ls -1 *.txt *.htm \| wc -l` → `27`; `ls -1 *.meta.json \| wc -l` → `27` |
| SEC bytes / words | 5,645,960 B / 703,025 words (`sources/sec/_RUN.json` "bytes"/"words") | read sidecar/`_RUN.json` |
| byte-identical duplicates | **0** | `md5sum *.txt *.htm \| awk '{print $1}' \| sort \| uniq -d` → no output |
| index perimeter (whole registrant) | **3,058** accessions, `filingDate` **1995-01-06 → 2026-09-17** | python csv over `sources/_index/submissions_CIK0000077476.csv` (header enumerated first: `filingDate, form, accession, reportDate, primaryDocument, source`) |
| rows before 1995-01-06 | **0** | same measurement (`rows before 1995-01-06: 0`) |
| archive walk capped? | **no** | `00_universe/_FLEET_INTAKE.tsv` row `slug=pepsico`: `slices_capped=no`; index `source` column holds only 3 values (`CIK0000077476-submissions-001.json` 2,000 rows, `-002.json` 54, `recent` 1,004) — i.e. every slice this registrant has |
| pass 1 — in-window intake (1898-01-01→1965-12-31) | `rc0/inwindow0/UNANS0`, **pass1_docs = 0** | `_FLEET_INTAKE.tsv` `pass1_status`/`pass1_docs` |
| pass 2 — recital intake (window in `_RUN.json`: **1965-12-31..2006-12-31**) | `rc1/inwindow105/UNANS4`, **pass2_docs = 27**, floor **1995-01-06** | `_FLEET_INTAKE.tsv` + `sources/sec/_RUN.json` (`attempted 106 = stored 27 + unanswered 4 + skipped 75`, `identity_ok: true`) |
| 4 UNANSWERED (all of them the same accession) | 8-K **0000077476-00-000047** (2000-12-04) docs `0001.txt/0002.txt/0003.txt` — 404 NoSuchKey on all three path forms; 4th row is `listing:not-enumerated` — **88 in-window filings never listed because `--max-docs 30` was reached** | `sources/sec/_UNANSWERED.csv` |
| corporate print bytes | **0** — `sources/corporate_print/` exists and is empty | `ls -laR sources/corporate_print` → only `.`/`..` |
| periodical bytes | **0** — no `sources/periodicals*`, no `sources/harvest_mine/` | directory enumeration of `sources/` |
| web-archive bytes | **0** — no `sources/web_archive/` path at all (cf. `company_011_microsoft/sources/web_archive/cdx_*.json`) | `find founders_playbook/01_companies -maxdepth 3 -type d -name web_archive` → microsoft, target only |
| auction/museum/manuscript | **0** — no such path, and `tools/queries.json` has **no such family for any company** (families present: chronicling_america 111, internet_archive 104, corporate_print 103, hathitrust 56, google_books 53 tasks) | python over `tools/queries.json` `tasks[]` |
| `research/A4_harvest_mine.md` | **DOES NOT EXIST** — mtime: none. This company's research dir was empty when this probe claimed it (`ls -la research/` → `total 0`), and `_parts/` is empty too. Nothing from a harvest-mine dossier is quoted anywhere in this file, and none was invented. | `find` for `*harvest_mine*` across the repo: dossiers exist for ranks 1–45/50 (e.g. `company_010_cencora/research/A4_harvest_mine.md`) and **none** for `company_046_pepsico` |

Consequence: the local corpus for this company is **one family deep** — filings — and every one of those 27 documents post-dates the whole proposed Stage-1 window.

STATUS: WRITTEN

---

## A.2 Windows are PROPOSED (and where the inherited one came from)

`fortune_top_50_2026.csv` carries no founding-date column, so the window below is not evidence.

**The inherited window `1898-01-01 → 1965-12-31` is a harvester parameter.** It lives verbatim at `tools/harvest_mine.py:71`:

```
"pepsico": ("1898-01-01", "1965-12-31"), "boeing": ("1916-01-01", "1940-12-31"),
```

`tools/fleet_intake.py` read that same table for pass 1, which is why pass 1 stored 0 documents: it searched a window EDGAR cannot reach. It also silently adopted *both* contested origin dates (1898 as start, 1965 as end) as if the chronology were settled. Per RD-112 that is a search setting; this probe re-proposes the stages against legal persons instead:

| stage | PROPOSED window | legal person whose events fill it | does any held carrier print an event inside it? |
|---|---|---|---|
| **1A — the product before any corporation** | 1893-01-01 → 1918-12-31 | none. A pharmacy syrup and a trade name; no corporate person yet | **no** — 0 occurrences of `1893`, `1898`, `1902`, `pharmacist`, `Bradham`, `Caleb`, `since 18` in all 27 documents (see A.5) |
| **1B — the beverage charter line** | 1919-01-01 → 1964-12-31 | the Delaware corporation the registrant itself recites as its own 1919 incorporation; and the separate legal person "Pepsi-Cola Company" (still a **subsidiary** in the 2001 subsidiary exhibit, ex21.htm l.1366: `Pepsi-Cola Company | Delaware`) | **yes, retrospectively** — the 1919 charter date is printed by the registrant in 8 filings; nothing else in-window |
| **1C — the merged registrant** | 1965-01-01 → 1986-12-31 | "PepsiCo, Inc." — formed 1965 on its own word; reincorporated in North Carolina 1986 | **yes, retrospectively** — `since PepsiCo was formed in 1965` in 5 filings; **no document dated inside the window exists** (measured floor 1995-01-06) |

STATUS: WRITTEN

---

## A.3 The trap: two origin lines and a merger date — assigned to legal persons, not blended

Four dates compete to be "the founding" of rank-46. Each belongs to a **different legal person**, and only two of them are printed anywhere in the 27 documents this probe holds:

| date | the folklore statement it carries | whose legal act it would be | printed in a held carrier? | class this probe assigns |
|---|---|---|---|---|
| **1893** | the pharmacist created the drink in his pharmacy/drugstore in 1893 | no corporation; a product of a sole proprietorship | **0 occurrences** | **UNKNOWN** — no carrier |
| **1898** | the same creation, dated 1898 (the date `harvest_mine.py:71` adopted as Stage-1's start) | no corporation | **0 occurrences** | **UNKNOWN** — no carrier. The window's own start date is unproven by this corpus |
| **1902** | "incorporated in 1902" | a corporate first-holder of the brand; **not** the registrant's recited charter and **not** the registrant's CIK | **0 occurrences** | **UNKNOWN** — no carrier |
| **1919** | the registrant's own oldest self-date | **the registrant itself** (PepsiCo, Inc., Delaware charter line) | **8 filings**, verbatim: *"PepsiCo, Inc. (the 'Company') was incorporated in Delaware in 1919 and was reincorporated in North Carolina in 1986"* | **FOUNDER CLAIM — retrospective self-narrative**; the registrant's own corporate record, repeated (§3: one lineage, not eight sources). Confidence capped at **Medium**, needs an independent carrier (Delaware charter file / state record / contemporaneous third-party print) |
| **1965** | "PepsiCo is the 1965 merger of the beverage company with a snack company" | **PepsiCo, Inc.** — the merged firm, a different person from either constituent | **5 filings** print `since PepsiCo was formed in 1965`, **all inside the dividend-policy paragraph**; **0** filings print the merger, the snack constituent's charter, or the word `Delaware corporation` for the registrant | **1965 as a date**: FOUNDER CLAIM (retrospective, single lineage, and only ever in a dividends sentence — it proves *continuous dividend payment since 1965*, not *what happened in 1965*). **The merger story itself**: **UNKNOWN** — no carrier in this corpus. |
| **1986** | reincorporation | the registrant | 8 filings, same sentence | FACT-within-lineage (registrant's own record), Medium |

Two further traps specific to this registrant, both measured:

1. **The registrant's recital does *not* corroborate either 1890s origin line; it selects a third date.** A 1995 (or 1999, or 2001) PepsiCo filing printing a 1919 charter is one retrospective lineage, exactly as a hypothetical 1995 10-K printing "since 1898" would be — and here it prints neither 1898 nor 1902. `since 18` occurs **0** times across all 27 documents (command in A.5). So the 1890s are **outside the registrant's own stated continuity**: on its own word, the registrant begins in 1919 and the merged firm begins in 1965. Anything that pushes Stage 1 back to 1893/1898 is importing a *brand* lineage into a *registrant* chronology (hard rule 5 — the Ford/Boeing/Kroger class).
2. **"Pepsi-Cola Company" is not the registrant in the documents we hold.** Exhibit 21 to the FY2000 10-K (`0000077476-01-500016_ex21.htm`, "SUBSIDIARIES OF PEPSICO, INC. AS OF 12/30/2000") lists `Pepsi-Cola Company` with jurisdiction `Delaware` **as a subsidiary**, alongside `Frito-Lay, Inc.` `Delaware` and `S.W. Frito-Lay, Ltd` `Texas`. So the two names that would carry the 1898 and the snack origin lines are both *inside* the group as separate legal persons, and neither is recited with an incorporation date anywhere in the corpus. `Pepsi-Cola Company` occurs 18 times, never with a founding date; `Frito` 455 times, never with a founding date; `1961` and `1902` occur **0** times.
3. **A harvest index entry cannot repair this.** The corporate-print lead `01-pepsi-co` is titled *"PepsiCo Annual Reports: 1938-"* with IA metadata `creator: "PepsiCo Inc."`, `date: 1938-01-01`, `year: 1938`. On the registrant's own word PepsiCo, Inc. did not exist until 1965, so the creator/date fields are an **uploader's label on a compilation** (RD-130's Disney item-date artefact), and the underlying reports — if any exist — are the **predecessor Pepsi-Cola Company's** (hard rule 5). It is a route to open, not corroboration; no bytes are on disk (A.1).

STATUS: WRITTEN

---

## A.4 Carriers found for the origin / predecessor question (file + line)

All paths are `founders_playbook/01_companies/company_046_pepsico/sources/sec/`. Line numbers are locators, not addresses (§14 r12).

| # | file (accession, form, filed) | line | what the bytes print | legal person |
|---|---|---|---|---|
| C1 | `0000077476-95-000002_0000077476-95-000002.txt` (S-3, 1995-01-06) | 462-463 | "The Company was incorporated in Delaware in 1919 and was reincorporated in North Carolina in 1986." | registrant |
| C2 | `0000077476-95-000017_0000077476-95-000017.txt` (10-K FY1994, 1995-03-28) | 125-126 | "PepsiCo, Inc. (the 'Company') was incorporated in Delaware in 1919 and was reincorporated in North Carolina in 1986." | registrant |
| C3 | same file | 557-559 | "Quarterly cash dividends have been paid since **PepsiCo was formed in 1965**, and dividends per share have increased for 22 consecutive years." | registrant (dividend context) |
| C4 | `0000077476-96-000023_…txt` (10-K FY1995, 1996-03-26) | 121-122; 557 | 1919/1986 recital; "dividends have been paid since 1965" | registrant |
| C5 | `0000077476-97-000007_…txt` (10-K FY1996, 1997-03-25) | 128-129; 554 | 1919/1986 recital; "dividends have been paid since 1965" | registrant |
| C6 | `0000077476-98-000014_…txt` (10-K FY1997, 1998-03-24) | 122-123; 455 | 1919/1986 recital; "since PepsiCo was formed in 1965" | registrant |
| C7 | `0000077476-99-000013_…txt` (10-K FY1998, 1999-03-24) | 122; 542 | 1919/1986 recital; same dividends sentence | registrant |
| C8 | `0000077476-00-000006_…txt` (10-K FY1999, 2000-03-21) | 126-127; 487 | 1919/1986 recital; same dividends sentence | registrant |
| C9 | `0000077476-01-500016_k2000.htm` (10-K FY2000, 2001-03-15) | 79; 346 | 1919/1986 recital; same dividends sentence | registrant |
| C10 | `0000077476-01-500016_ex21.htm` (ex-21 to FY2000 10-K) | 1366 + table | "SUBSIDIARIES OF PEPSICO, INC. AS OF 12/30/2000" → `Pepsi-Cola Company` \| `Delaware`; `Frito-Lay, Inc.` \| `Delaware`; `S.W. Frito-Lay, Ltd` \| `Texas` | **two constituent-type legal persons, inside the group, each undated** |
| C11 | `0000077476-95-000002…txt` (S-3) | 472-477 | "Under appointments from PepsiCo, bottlers manufacture, sell, and distribute, **within defined territories**, carbonated soft drinks and syrups bearing trademarks owned by PepsiCo, including PEPSI-COLA, DIET PEPSI, MOUNTAIN DEW…" | registrant's **contemporary (1995)** franchise-licensing structure — no inception date |
| C12 | `0000077476-00-000006…txt` (10-K FY1999) | 238-241 | "PCNA's bottlers are licensed to manufacture, market, sell and distribute beverages and syrups bearing the Pepsi-Cola Beverage trademarks in **approximately 440 licensed territories**" | same: contemporary structure, no origin claim |
| C13 | `0000912057-01-000830_a2034530zs-4.txt` (S-4, 2001-01-09, Quaker) + `…007577_a2039895zs-4a.txt` (S-4/A) | 306, 357; ex-23 f/g/h l.16-34 | merger mechanics of **BeverageCo, Inc.** with and into PepsiCo, Inc. | post-Stage-1; shows the registrant recites entity changes when they matter to the instrument |

**Independence accounting (§3):** C1-C9 are one lineage — the registrant's own repeated corporate record. C13's S-4 + S-4/A + the 2001 S-3 are a second lineage group but a single registration lineage each and both post-date the window. **No second independent lineage prints any founding date.** Every carrier above is the company talking about itself.

STATUS: WRITTEN

---

## A.5 Measured zeros (the folklore audit) — 27 stored documents, restricted to `*.txt *.htm`

Command, run from `sources/sec/`:
```
for t in 1893 1898 1902 1899 1900 pharmacist Bradham Caleb "Herman Lay" "since 18" \
         "bottle cap" crown 1961 caramel; do echo "$t: $(grep -rio -- "$t" *.txt *.htm | wc -l)"; done
```
Result (occurrences, not files): `1893: 0  1898: 0  1902: 0  1899: 0  1900: 1  pharmacist: 0  Bradham: 0  Caleb: 0  Herman Lay: 0  "since 18": 0  "bottle cap": 0  crown: 0  1961: 0  caramel: 0`
Also measured: `"Pepsi-Cola Incorporated": 0`, `"crown cap": 0`, `"Delaware corporat…": 0`, `1938: 0 files matched`.

The single `1900` is **not** history: `0000077476-98-000014…txt:636` — "date-sensitive software may recognize a date using '00' as the year 1900 rather…" — a Y2K boilerplate line (OCR/keyword decoy, rule 6).

What the corpus does print about the three classic folklore entry points:

| folklore item | what the bytes actually say | verdict |
|---|---|---|
| **bottle / crown cap** | `bottle cap` 0, `crown` 0 | **UNKNOWN** — no carrier; anything written about it is importer's folklore |
| **franchise bottler system** | C11/C12: 1995-2000 appointments, defined territories, ~440 licensed territories — a *description of the system as it then was* | the system's **existence** in 1995-99 is FACT; its **inception date** is **UNKNOWN** |
| **trademark inception** | `trademark` 94 occurrences, none attached to a year; `PEPSI-COLA` appears only in a list of marks "owned by PepsiCo" (C11) | **UNKNOWN** — no first-use or registration date in any held carrier |

STATUS: WRITTEN

---

## A.6 Five-family verdict (three states only; an untried family is never a null)

Evidence base for (c)/(d): `00_universe/harvest/candidates.csv` rows with `company=pepsico` — **33 rows, 10 distinct queries**, header enumerated first (`company, source_family, query, item_id, title, date_or_issue, url, snippet_or_hitcount, http_status, classification, retrieved_at`).

| family | state | measurement | remedy if UNANSWERED |
|---|---|---|---|
| **(a) SEC / EDGAR filings** | **TRIED–ANSWERED (post-window only)** | 27 documents / 17 accessions on disk, md5-unique, 5,645,960 B; perimeter **1995-01-06 → 2026-09-17** over 3,058 accessions; `slices_capped=no` (RD-134 re-grade satisfied). It answers the 1919/1965/1986 recitals and **nothing** in 1893–1964 as a document. The 1995-01-06 floor is a **measured perimeter of EDGAR's own archive for this CIK**, not "PepsiCo filed nothing". | for 1965-1986: nothing to fetch — EDGAR has no digitised filings before ~1993-94 for this registrant; that leg must come from families (c)/(d)/(e) |
| **(b) web archives** | **UNTRIED — 0 calls** | no `sources/web_archive/` path exists for this company (`find … -type d -name web_archive` returns microsoft and target only), and `tools/` contains no CDX script. No sidecar with an `http_status` exists → reporting UNTRIED is correct here (the RD-134 NR-1 trap). | write `sources/web_archive/` + a CDX pass in the form Microsoft's `cdx_microsoft_com_earliest_200.json` uses (site + 1996-2005 range, and for a brand-history question an `PepsiCola.com`/`fritolay.com` capture set). Low ceiling for pre-1996, but it is the *only* route to the 1996-2001 brand-history pages that may recite the 1898 line. |
| **(c) periodical corpora** | **TRIED–UNANSWERED** | CA 2 rows both `UNANSWERED — SKIPPED: global max-requests cap 600 reached`; HT 1 row `UNANSWERED — hard stop: 5 consecutive failures (host halted)`; GB 1 row `UNANSWERED — cap 600`. IA was actually fetched: the facet-free wide query `("Pepsi-Cola" OR "Pepsi Co" OR "Frito" OR "Lay's") AND mediatype:texts` returned **numFound 747** (`internet_archive/4b2daba1f588ffa2.json`), whose top rows are `gov.uscourts.*` decisions naming **bottling franchisees and defendants** — `Ram Distribution Group LLC v. Pepsi-Cola Bottling Company of New York`, `Miller v. Frito Lay, Inc.`, `Ruiz-Troche v. Pepsi Cola of P. R.` — i.e. same-brand different-legal-person hits, correctly classified `LEAD_ONLY`. The one trade-press route (`Beverage World`/`Food Engineering`/`Progressive Grocer` + Pepsi, facet-free) returned **numFound 0 = a proven NULL** (`internet_archive/8ccd8ef2950b4e56.json`). | re-run CA and HT (the cap/host are tool limits, not archive emptiness); page the 747-hit IA result set past row 20 and filter by `date` before 1966; and add a bottler-name query set, since the beverage trade press is where a 1930s-50s franchise-bottler naming would live |
| **(d) digitised corporate print** | **TRIED (faceted)–UNANSWERED, 0 bytes stored** | 2 CP rows `UNANSWERED — cap 600`; then the 2026-09-29T19:14:39Z fetch returned **numFound 3**: `01-pepsi-co` *"PepsiCo Annual Reports: 1938-"* (collection `fund-and-stock-reports`), `cor5_0_s06_ss01_boxrg5_0_2008_006_f61` *"Pepsi-Cola Company's Fourth Annual Exhibition Paintings of the Year"* (Corcoran Gallery of Art — an **art show catalogue**, not corporate print), `1974-12-press-release` (Pepsi Cola Canada Ltd. basketball tournament). **RD-130 is still live for this family here**: the CP sidecar URL still ends `…AND%20YEAR%3A%5B1900%20TO%201980%5D` and **0 of the 21 facet-free-tagged pepsico rows are corporate_print** — because `drop_year_facet` (periodical_harvest.py:1401-1427) only rewrites `params["q"]`, while CP tasks carry `year_range` and **no `q`**, so `if not q: continue` skips the whole family. | fix the tool (strip `year_range` under `--facet-free`) and re-run; then `ia_text.py list-files 01-pepsi-co` and read the per-year layers inside — that single item is the only candidate for a genuine 1938-1980 annual-report run for this brand line |
| **(e) auction / museum / manuscript** | **UNTRIED** | no path, no sidecars, and **no task family exists in `tools/queries.json` for any company** (families present: chronicling_america 111, internet_archive 104, corporate_print 103, hathitrust 56, google_books 53 of 427 tasks) — so this is not a PepsiCo-specific miss, it is a corpus-level hole | new family + query block: Bradham pharmacy originals, Pepsi-Cola Company / Frito Co. manuscript collections, Lay family papers (Texas), and dealer catalogues. Also the Delaware State Division of Corporations charter file for the 1919 line (a court/registry record is the independent §3 lineage this company has none of) |

STATUS: WRITTEN

---

## A.7 Per-stage tiers (RD-112: each tier measured against its own window)

Tier rule §15.2 — ≥3 families with in-window Tier-1 text = T1 exemplar; 2 = T2 core; ≤1 = T3 register. For this company **no family returns in-window Tier-1 text at all**; family (a) returns *retrospective* Tier-1-adjacent text about in-window events (the registrant's own charter recital), which is what a T3 stage looks like, not a T2.

| stage (PROPOSED) | families returning text about events inside the window | tier | provisional? |
|---|---|---|---|
| **1A 1893–1918** (syrup, pharmacist, brand before charter) | **none**. (a) perimeter 1995-01-06 → 0 in-window documents; (c)/(d) tried-unanswered; (b)/(e) untried | **T3 register** — §K/§N/§U mandatory, origin claim stays UNKNOWN | firm as measured; can only move if (c) or (d) delivers in-window naming |
| **1B 1919–1964** (the beverage charter line) | **(a) only, retrospective**: the 1919 Delaware recital in 8 filings = **one lineage** (§3). No periodical or print naming of "Pepsi-Cola Company" inside the window is stored | **T3 register** | PROVISIONAL — hinges on the CP item `01-pepsi-co` (1938-) and the 747-hit IA set; one of these could make 1B **T2** in a single fetch |
| **1C 1965–1986** (the merged registrant) | **(a) only**: "since PepsiCo was formed in 1965" (5 filings) — but *0* documents dated inside the window exist; every other family is unanswered/untried | **T3 register** (T2 **not** reachable on the current corpus: 1 family) | PROVISIONAL — the same CP item may hold FY1965-1980 layers, which would be the second family |
| **Stage 1 overall** (as the orchestrator will dispatch it) | 1 family (a), single lineage | **T3 register**, with 1B/1C marked PROVISIONAL | re-grade after the CP/CA re-runs named in A.9 |

Per RD-112's ruling: this is a finding about the **record**, not an inconsistency — the same company is T3 for its origin and could become T2 for 1B on one fetched item. And per RD-134, family (a)'s verdict here is **not** provisional-on-tool: the walk reached every slice (`slices_capped=no`, 3 slice-keys observed for 3,058 rows), so the 1995-01-06 floor is a real perimeter.

STATUS: WRITTEN

---

## A.8 Untried (the list, explicitly)

1. **(b) web archives — UNTRIED, 0 calls.** No `sources/web_archive/` path, no CDX client for this company.
2. **(e) auction / museum / manuscript — UNTRIED**, and no query block exists for the family corpus-wide.
3. **(c) Chronicling America `CA 'Pepsi-Cola' beverage 1890-1975` and `CA 'Pepsi' Purchase / Harrison New York 1950-1995` — never actually queried** (both rows are `SKIPPED: global max-requests cap 600 reached`). The two towns in the second label are the HQ-disputed towns; the route is alive, just unspent.
4. **(c) HathiTrust `HT 'Pepsi-Cola' bottling company` — never completed** (`hard stop: 5 consecutive failures (host halted)`).
5. **(c) Google Books `GB 'PepsiCo' 'Pepsi-Cola' annual report shareholder` — never queried** (cap 600).
6. **(c/d) the Internet Archive wide set beyond row 20** — numFound 747, only the first 20 sampled; the pre-1966 subset has never been enumerated.
7. **(c) the local mine step — UNTRIED for this company**: no `research/A4_harvest_mine.md`, no `sources/harvest_mine/`, and `00_universe/harvest/mine_bytes/` contains **no `pepsico` directory** (`ls: cannot access mine_bytes/pepsico`). RD-124's relocated-bytes ledger also has **0** pepsico rows (`grep -i pepsico _RELOCATED_MINE_BYTES.tsv` → no output). So no local-index mining has ever been run over PepsiCo bytes; this probe did not run it (per brief).
8. **(d) `ia_text.py list-files 01-pepsi-co`** — the per-year layer count inside the compilation is unknown; that is the single highest-value untried measurement for this company.
9. **EDGAR pre-1994 paper era / SEC legacy microfilm** — no script reaches it; the 1965 merger's own registration statement (a 1965 S-1 or merger proxy for PepsiCo, Inc.) is **UNTRIED and unreachable by this toolchain**. Named here so no later agent reads it as a null.

STATUS: WRITTEN

---

## A.9 FETCH REQUESTS (the scripts can reach these; this probe made no web call)

```
FETCH REQUEST 1  (highest value)
  route:   python tools/ia_text.py list-files 01-pepsi-co
           then python tools/ia_text.py 01-pepsi-co --file <each per-year layer>
  item:    https://archive.org/details/01-pepsi-co   "PepsiCo Annual Reports: 1938-"
           collection: fund-and-stock-reports, periodicals, magazine_rack
  settles: whether a per-year corporate-print run exists for the beverage line 1938-1980 —
           the only candidate that could raise stage 1B/1C from T3 to T2.
  caution: metadata creator "PepsiCo Inc." + date 1938 is an uploader label; on the registrant's
           own word the person did not exist until 1965 (A.3). Read the title page of each layer
           and record WHICH legal person's name is printed before crediting it.
```
```
FETCH REQUEST 2
  route:   python tools/periodical_harvest.py --company pepsico --only-family chronicling_america
           (and, after fixing drop_year_facet to strip CP year_range, the corporate_print set)
  items:   CA 'Pepsi-Cola' beverage 1890-1975 (New York); CA 'Pepsi' Purchase / Harrison NY 1950-1995
  why now: both rows are UNANSWERED because of a tool cap ("global max-requests cap 600 reached"),
           not because the archive is empty — RD-130/RD-134 class.
```
```
FETCH REQUEST 3
  route:   python tools/ia_text.py / advancedsearch paging past rows=20 on query
           ("Pepsi-Cola" OR "Pepsi Co" OR "Frito" OR "Lay's") AND mediatype:texts   [numFound 747]
           filtered to date <= 1965
  settles: whether any pre-1966 periodical names the beverage company outside a court docket.
           Sampled rows so far are all usfederalcourts naming bottling franchisees (rule 5 decoys).
```
```
FETCH REQUEST 4  (low cost, do it in the same pass)
  identifier: NPTG19060630  (Hong Kong Telegraph, 1906-06-30) — in-window by date.
  verify what string matched: RD-124's bare-word class — "Pepsin"/"Pepsi" in an advertisement is
  not a naming of the registrant's predecessor; do not cite it until the page text is read.
  Identifier twelvefullounces0000mart (1962, "Twelve full ounces", printdisabled) is the other
  in-window TIER1_CANDIDATE row and is equally unverified: an index label is not a fact (rule 6).
  Identifier cor5_0_s06_ss01_boxrg5_0_2008_006_f61 (1948) is a Corcoran Gallery art-catalogue
  title-page ("Pepsi-Cola Company's Fourth Annual Exhibition … Paintings of the Year"): it names a
  sponsor, it is NOT corporate print — expect a VARIANT_TERM_HIT, not a naming of the registrant.
```
```
FETCH REQUEST 5  (registry line, would be the first INDEPENDENT lineage)
  Delaware Division of Corporations charter record for the 1919 Delaware corporation, and the
  1965-05 merger certificate naming the constituent corporations of "PepsiCo, Inc.".
  No script in tools/ reaches a state registry; dispatch only if the orchestrator can order a
  registry retrieval. Until then the 1919 and 1965 dates rest on the company's own word.
```

STATUS: WRITTEN

---

## A.10 What this probe refused to claim, and why

- **Refused: "PepsiCo was founded in 1893 / 1898 / 1902."** Measured **0** occurrences of all three dates, and of `pharmacist`, `Bradham`, `Caleb`, `Herman Lay`, `since 18`, across all 27 held documents (A.5 command). No carrier → the origin stage stays **UNKNOWN**, not a folklore date and not a "no".
- **Refused: "the registrant's filings say the company began in 1919, therefore 1919 is the founding."** The recital is real (C1-C9) but it is the **registrant's own corporate record repeated** — one lineage under §3 — and it is a *charter* statement, not a *founding* statement. Published as: *the registrant recites a Delaware incorporation in 1919* (FOUNDER CLAIM, retrospective, Medium).
- **Refused: "1965 is corroborated by several filings."** Five filings print it, all one lineage, and **all five inside the dividend-policy paragraph** — they prove continuous quarterly dividends since 1965. They do **not** state a merger, a partner company, or a date of the snack company's incorporation. **The merger itself is UNKNOWN in this corpus.**
- **Refused: to treat `01-pepsi-co` "PepsiCo Annual Reports: 1938-" as evidence that PepsiCo existed in 1938.** It is an index row with an uploader's creator/date metadata (§3 "a search-index row is not a fact"; RD-130's item-date artefact) and its bytes are not on disk; on the registrant's own word the person named in the label did not exist until 1965 (hard rule 5).
- **Refused: to call family (c) or (d) a null.** Both are **TRIED–UNANSWERED** with named remedies (A.6); the only proven null measured is the facet-free trade-press query, `numFound 0`.
- **Refused: to quote `research/A4_harvest_mine.md`.** It does not exist for this company, so there is nothing to re-read and no mtime to give; the mine step is recorded UNTRIED (A.8.7).
- **Refused: to run `harvest_mine.py` / `periodical_harvest.py` / any web call** (per brief and §15.1) — every route needing bytes is a FETCH REQUEST instead.

STATUS: WRITTEN

---

## A.11 Gate

Command run (briefed, verbatim):
```
python tools/gates.py --company-dir founders_playbook/01_companies/company_046_pepsico \
  --checks csv,keys --fail-on substantive \
  --out founders_playbook/03_quality_control/pepsico_s1_probe_gates.md
```
Result: `Findings: 2 | Passes: 0`, both **coverage-only** — "no register CSVs at root or research/ — csv/anchors gates DID NOT RUN" and "no stage_*.md volumes found — keys/anchors gates DID NOT RUN" — plus `coverage 0 registers, 0 stage volumes, 27 source documents`. The gate also printed `tier: exemplar (no tier stated in this company's research/ dossiers -- exemplar assumed)`: **that line is the gate's default, not this probe's finding. The stated tier is T3 register (A.7).** With `--fail-on substantive` the run does not fail on coverage-only findings, which is the expected state for a freshly probed company; nothing under `sources/` was modified, moved or deleted (add-only, rule 2).

STATUS: WRITTEN

---

## A.12 Handoff

- **Registers:** no `sources.csv` / `conflicts.csv` / `data_gaps.csv` written by this probe — a T3 register dossier still owes all three (§15.2), and this file names the rows they should carry: the 1919 recital, the 1965 dividend sentence, the ex-21 subsidiary table, and 8 UNKNOWN origin/folklore claims from A.3/A.5/A.10.
- **Conflicts to open at merge time:** (i) `1893` vs `1898` for the syrup — unresolvable on this corpus, both UNKNOWN; (ii) registrant's own 1919 charter line vs the folk 1902 incorporation line — different legal persons, do not reconcile by preference; (iii) the IA `creator: PepsiCo Inc. / 1938` metadata vs the registrant's own "formed in 1965" — a metadata-versus-carrier conflict, resolved in favour of the carrier.
- **Sentence that matters:** the verdict for stages 1B and 1C turns on **one fetch** — `ia_text.py list-files 01-pepsi-co`, the Internet Archive `fund-and-stock-reports` compilation *"PepsiCo Annual Reports: 1938-"* — because a per-year corporate-print run is the only second family on the horizon for a company whose EDGAR perimeter starts 1995-01-06, and nothing else in the corpus can name a Pepsi-Cola Company legal person before 1995.

STATUS: WRITTEN
